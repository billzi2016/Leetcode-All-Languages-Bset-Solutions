# 2532. Time to Cross a Bridge

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findCrossingTime(int n, int k, vector<vector<int>>& time) {
        using ll = long long;
        vector<ll> eff(k);
        for (int i = 0; i < k; ++i) eff[i] = (ll)time[i][0] + time[i][2];
        
        // waiting queues: pair<efficiency, id>
        priority_queue<pair<ll,int>, vector<pair<ll,int>>, greater<pair<ll,int>>> leftWait, rightWait;
        for (int i = 0; i < k; ++i) leftWait.emplace(eff[i], i);
        
        // busy queues: pair<available_time, id>
        priority_queue<pair<ll,int>, vector<pair<ll,int>>, greater<pair<ll,int>>> leftBusy, rightBusy;
        
        ll cur = 0;
        int delivered = 0;
        while (delivered < n) {
            // move workers that become idle at current time to waiting queues
            while (!leftBusy.empty() && leftBusy.top().first <= cur) {
                int id = leftBusy.top().second;
                leftBusy.pop();
                leftWait.emplace(eff[id], id);
            }
            while (!rightBusy.empty() && rightBusy.top().first <= cur) {
                int id = rightBusy.top().second;
                rightBusy.pop();
                rightWait.emplace(eff[id], id);
            }
            
            bool canLeft  = !leftWait.empty() && delivered < n; // can go to right to fetch
            bool canRight = !rightWait.empty();                 // can go to left delivering
            
            if (canLeft && canRight) {
                auto lTop = leftWait.top();
                auto rTop = rightWait.top();
                // compare efficiency (smaller sum, then smaller index)
                if (lTop.first < rTop.first || (lTop.first == rTop.first && lTop.second < rTop.second)) {
                    // left worker goes to right
                    leftWait.pop();
                    int id = lTop.second;
                    cur += time[id][0];                     // crossing to right
                    ll ready = cur + time[id][1];            // after picking
                    rightBusy.emplace(ready, id);
                } else {
                    // right worker returns with box
                    rightWait.pop();
                    int id = rTop.second;
                    cur += time[id][2];                     // crossing to left
                    ++delivered;                            // box arrived
                    ll finishPut = cur + time[id][3];
                    leftBusy.emplace(finishPut, id);
                }
            } else if (canRight) {
                auto rTop = rightWait.top(); rightWait.pop();
                int id = rTop.second;
                cur += time[id][2];
                ++delivered;
                ll finishPut = cur + time[id][3];
                leftBusy.emplace(finishPut, id);
            } else if (canLeft) {
                auto lTop = leftWait.top(); leftWait.pop();
                int id = lTop.second;
                cur += time[id][0];
                ll ready = cur + time[id][1];
                rightBusy.emplace(ready, id);
            } else {
                // no one can move now, jump to next event
                ll nxt = LLONG_MAX;
                if (!leftBusy.empty()) nxt = min(nxt, leftBusy.top().first);
                if (!rightBusy.empty()) nxt = min(nxt, rightBusy.top().first);
                cur = nxt;
            }
        }
        return (int)cur;
    }
};
```

## Java

```java
class Solution {
    public int findCrossingTime(int n, int k, int[][] time) {
        Comparator<Integer> comp = (a, b) -> {
            int sumA = time[a][0] + time[a][2];
            int sumB = time[b][0] + time[b][2];
            if (sumA != sumB) return Integer.compare(sumA, sumB);
            return Integer.compare(a, b);
        };
        PriorityQueue<Integer> leftWait = new PriorityQueue<>(comp);
        PriorityQueue<Integer> rightWait = new PriorityQueue<>(comp);
        for (int i = 0; i < k; i++) leftWait.add(i);

        PriorityQueue<long[]> busyLeft = new PriorityQueue<>((x, y) -> Long.compare(x[0], y[0]));
        PriorityQueue<long[]> busyRight = new PriorityQueue<>((x, y) -> Long.compare(x[0], y[0]));

        int boxes = n;
        long cur = 0;
        long ans = 0;

        while (boxes > 0 || !rightWait.isEmpty() || !busyLeft.isEmpty() || !busyRight.isEmpty()) {
            // move workers that have finished putting/picking to waiting queues
            while (!busyLeft.isEmpty() && busyLeft.peek()[0] <= cur) {
                long[] p = busyLeft.poll();
                leftWait.add((int) p[1]);
            }
            while (!busyRight.isEmpty() && busyRight.peek()[0] <= cur) {
                long[] p = busyRight.poll();
                rightWait.add((int) p[1]);
            }

            if (!rightWait.isEmpty()) { // cross from right to left with a box
                int id = rightWait.poll();
                cur += time[id][2];               // crossing left
                ans = Math.max(ans, cur);          // arrival on left side
                long finishPut = cur + time[id][3];
                busyLeft.add(new long[]{finishPut, id}); // will be idle after putting
            } else if (boxes > 0 && !leftWait.isEmpty()) { // cross from left to right to get a box
                int id = leftWait.poll();
                cur += time[id][0];               // crossing right
                long finishPick = cur + time[id][1];
                busyRight.add(new long[]{finishPick, id}); // will be ready on right side
                boxes--;
            } else {
                long next = Long.MAX_VALUE;
                if (!busyLeft.isEmpty()) next = Math.min(next, busyLeft.peek()[0]);
                if (!busyRight.isEmpty()) next = Math.min(next, busyRight.peek()[0]);
                cur = next;
            }
        }
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def findCrossingTime(self, n, k, time):
        """
        :type n: int
        :type k: int
        :type time: List[List[int]]
        :rtype: int
        """
        import heapq

        # max-heap for waiting workers on each side based on inefficiency
        left_wait = []
        right_wait = []

        for i in range(k):
            ineff = -(time[i][0] + time[i][2])  # larger sum => more inefficient
            heapq.heappush(left_wait, (ineff, -i))

        # busy workers: (available_time, worker_id, side) side 0=left,1=right
        busy = []
        cur = 0
        boxes = n

        while True:
            # release workers that have finished their pick/put tasks by current time
            while busy and busy[0][0] <= cur:
                t, w, side = heapq.heappop(busy)
                ineff = -(time[w][0] + time[w][2])
                if side == 0:   # now waiting on left side
                    heapq.heappush(left_wait, (ineff, -w))
                else:           # now waiting on right side
                    heapq.heappush(right_wait, (ineff, -w))

            if right_wait:
                _, neg_i = heapq.heappop(right_wait)
                i = -neg_i
                cur += time[i][2]          # crossing back to left with a box
                boxes -= 1
                # after crossing, worker puts the box (does not affect answer)
                finish = cur + time[i][3]
                heapq.heappush(busy, (finish, i, 0))
                if boxes == 0:
                    return cur
            elif boxes > 0 and left_wait:
                _, neg_i = heapq.heappop(left_wait)
                i = -neg_i
                cur += time[i][0]          # crossing to right side
                finish = cur + time[i][1]   # picking a box
                heapq.heappush(busy, (finish, i, 1))
            else:
                if not busy:   # no more events; should not happen while boxes remain
                    break
                # jump forward to the next event when some worker becomes idle
                cur = busy[0][0]
```

## Python3

```python
import heapq
from typing import List

class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        # priority for less efficient worker: larger left+right, tie larger index
        def eff(i):
            return -(time[i][0] + time[i][2]), -i  # negative for max-heap behavior using min-heap

        left_wait = []   # workers on left ready to go right (need a box)
        right_wait = []  # workers on right ready to go left (carrying a box)

        for i in range(k):
            heapq.heappush(left_wait, (*eff(i), i))

        # busy heaps store (available_time, worker_id)
        # after picking: becomes available on right side
        pick_busy = []   # workers currently picking on right side
        # after putting: becomes available on left side
        put_busy = []    # workers currently putting on left side

        cur = 0
        boxes_left = n
        delivered = 0
        last_arrival = 0

        while delivered < n:
            # move finished pick/put tasks to waiting queues
            while pick_busy and pick_busy[0][0] <= cur:
                ft, w = heapq.heappop(pick_busy)
                heapq.heappush(right_wait, (*eff(w), w))
            while put_busy and put_busy[0][0] <= cur:
                ft, w = heapq.heappop(put_busy)
                heapq.heappush(left_wait, (*eff(w), w))

            # decide who can cross now
            cand_left = left_wait[0] if left_wait and boxes_left > 0 else None
            cand_right = right_wait[0] if right_wait else None

            if not cand_left and not cand_right:
                # no one ready, jump to next event
                nxt = float('inf')
                if pick_busy:
                    nxt = min(nxt, pick_busy[0][0])
                if put_busy:
                    nxt = min(nxt, put_busy[0][0])
                cur = max(cur, nxt)
                continue

            # choose the less efficient (higher priority) worker
            if cand_right and (not cand_left or cand_right < cand_left):
                _, _, w = heapq.heappop(right_wait)
                # cross right -> left with a box
                cur += time[w][2]
                last_arrival = max(last_arrival, cur)
                delivered += 1
                # start putting the box
                finish_put = cur + time[w][3]
                heapq.heappush(put_busy, (finish_put, w))
            else:
                _, _, w = heapq.heappop(left_wait)
                # cross left -> right to get a box
                cur += time[w][0]
                # start picking the box
                finish_pick = cur + time[w][1]
                heapq.heappush(pick_busy, (finish_pick, w))
                boxes_left -= 1

        return last_arrival
```

## C

```c
#include <stdlib.h>

typedef struct {
    long long t;
    int id;
    int side; // 0 = left waiting, 1 = right waiting
} Event;

/* global data for comparator */
static int **gTimeArr;
static long long *gEffSum;

/* ---------- max-heap for workers (left/right) ---------- */
static void workerPush(int *heap, int *size, int id) {
    int i = ++(*size);
    heap[i] = id;
    while (i > 1) {
        int p = i >> 1;
        long long sum_i = gEffSum[heap[i]];
        long long sum_p = gEffSum[heap[p]];
        if (sum_i > sum_p || (sum_i == sum_p && heap[i] > heap[p])) {
            int tmp = heap[i];
            heap[i] = heap[p];
            heap[p] = tmp;
            i = p;
        } else break;
    }
}
static int workerPop(int *heap, int *size) {
    int top = heap[1];
    heap[1] = heap[(*size)--];
    int i = 1;
    while (1) {
        int l = i << 1, r = l + 1, best = i;
        if (l <= *size) {
            long long sum_l = gEffSum[heap[l]];
            long long sum_best = gEffSum[heap[best]];
            if (sum_l > sum_best || (sum_l == sum_best && heap[l] > heap[best]))
                best = l;
        }
        if (r <= *size) {
            long long sum_r = gEffSum[heap[r]];
            long long sum_best = gEffSum[heap[best]];
            if (sum_r > sum_best || (sum_r == sum_best && heap[r] > heap[best]))
                best = r;
        }
        if (best != i) {
            int tmp = heap[i];
            heap[i] = heap[best];
            heap[best] = tmp;
            i = best;
        } else break;
    }
    return top;
}

/* ---------- min-heap for busy events ---------- */
static void eventPush(Event *heap, int *size, Event ev) {
    int i = ++(*size);
    heap[i] = ev;
    while (i > 1) {
        int p = i >> 1;
        if (heap[i].t < heap[p].t) {
            Event tmp = heap[i];
            heap[i] = heap[p];
            heap[p] = tmp;
            i = p;
        } else break;
    }
}
static Event eventPop(Event *heap, int *size) {
    Event top = heap[1];
    heap[1] = heap[(*size)--];
    int i = 1;
    while (1) {
        int l = i << 1, r = l + 1, best = i;
        if (l <= *size && heap[l].t < heap[best].t) best = l;
        if (r <= *size && heap[r].t < heap[best].t) best = r;
        if (best != i) {
            Event tmp = heap[i];
            heap[i] = heap[best];
            heap[best] = tmp;
            i = best;
        } else break;
    }
    return top;
}
static Event eventPeek(Event *heap, int size) {
    return heap[1];
}

/* ---------- main function ---------- */
int findCrossingTime(int n, int k, int** time, int timeSize, int* timeColSize){
    gTimeArr = time;
    gEffSum = (long long*)malloc(sizeof(long long) * k);
    for (int i = 0; i < k; ++i)
        gEffSum[i] = (long long)time[i][0] + (long long)time[i][2];

    /* worker heaps */
    int *leftHeap = (int*)malloc(sizeof(int) * (k + 5));
    int *rightHeap = (int*)malloc(sizeof(int) * (k + 5));
    int leftSize = 0, rightSize = 0;
    for (int i = 0; i < k; ++i)
        workerPush(leftHeap, &leftSize, i);

    /* busy event heap */
    int maxEvents = n + 3 * k + 10;
    Event *busyHeap = (Event*)malloc(sizeof(Event) * (maxEvents));
    int busySize = 0;

    long long cur = 0;
    int delivered = 0;

    while (delivered < n) {
        /* move completed events to waiting heaps */
        while (busySize > 0 && eventPeek(busyHeap, busySize).t <= cur) {
            Event ev = eventPop(busyHeap, &busySize);
            if (ev.side == 0)
                workerPush(leftHeap, &leftSize, ev.id);
            else
                workerPush(rightHeap, &rightSize, ev.id);
        }

        int crossed = 0;
        if (rightSize > 0) {
            int id = workerPop(rightHeap, &rightSize);
            long long finishCross = cur + time[id][2];
            /* schedule put operation */
            Event ne; ne.t = finishCross + time[id][3]; ne.id = id; ne.side = 0;
            eventPush(busyHeap, &busySize, ne);
            delivered++;
            if (delivered == n) {
                free(gEffSum); free(leftHeap); free(rightHeap); free(busyHeap);
                return (int)finishCross;
            }
            cur = finishCross;
            crossed = 1;
        } else if (leftSize > 0 && delivered < n) {
            int id = workerPop(leftHeap, &leftSize);
            long long finishCross = cur + time[id][0];
            /* after crossing, pick box then become right waiting */
            Event ne; ne.t = finishCross + time[id][1]; ne.id = id; ne.side = 1;
            eventPush(busyHeap, &busySize, ne);
            cur = finishCross;
            crossed = 1;
        }

        if (!crossed) {
            if (busySize > 0)
                cur = eventPeek(busyHeap, busySize).t;
        }
    }

    free(gEffSum); free(leftHeap); free(rightHeap); free(busyHeap);
    return (int)cur;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution
{
    private struct Event
    {
        public int Time;
        public int Id;
    }

    private class WorkerComparer : IComparer<int>
    {
        private readonly int[] _totalCross;
        public WorkerComparer(int[] totalCross)
        {
            _totalCross = totalCross;
        }
        public int Compare(int a, int b)
        {
            if (a == b) return 0;
            // larger totalCross => less efficient => should come first (smaller in ordering)
            if (_totalCross[a] != _totalCross[b])
                return _totalCross[b].CompareTo(_totalCross[a]); // descending totalCross
            // larger index => less efficient
            return b.CompareTo(a); // descending id
        }
    }

    public int FindCrossingTime(int n, int k, int[][] time)
    {
        int[] right = new int[k];
        int[] pick = new int[k];
        int[] left = new int[k];
        int[] put = new int[k];
        int[] totalCross = new int[k];
        for (int i = 0; i < k; i++)
        {
            right[i] = time[i][0];
            pick[i] = time[i][1];
            left[i] = time[i][2];
            put[i] = time[i][3];
            totalCross[i] = right[i] + left[i];
        }

        var leftWait = new SortedSet<int>(new WorkerComparer(totalCross));
        var rightWait = new SortedSet<int>(new WorkerComparer(totalCross));

        // initially all workers are on the left side, ready to cross
        for (int i = 0; i < k; i++) leftWait.Add(i);

        var leftAvail = new PriorityQueue<Event, int>();
        var rightAvail = new PriorityQueue<Event, int>();

        long cur = 0;
        int delivered = 0;
        int taken = 0; // number of boxes already picked (i.e., workers that have crossed to the right)

        while (delivered < n)
        {
            // move workers whose pick/put finished into waiting sets
            while (leftAvail.Count > 0 && leftAvail.Peek().Time <= cur)
            {
                var ev = leftAvail.Dequeue();
                leftWait.Add(ev.Id);
            }
            while (rightAvail.Count > 0 && rightAvail.Peek().Time <= cur)
            {
                var ev = rightAvail.Dequeue();
                rightWait.Add(ev.Id);
            }

            if (rightWait.Count > 0)
            {
                int id = rightWait.Min;
                rightWait.Remove(id);
                cur += left[id]; // cross back to the left with a box
                delivered++;
                if (delivered == n) return (int)cur; // arrival time of last box

                // after arriving, spend put time then become idle on left side
                int finishPut = (int)(cur + put[id]);
                leftAvail.Enqueue(new Event { Time = finishPut, Id = id }, finishPut);
            }
            else if (taken < n && leftWait.Count > 0)
            {
                int id = leftWait.Min;
                leftWait.Remove(id);
                cur += right[id]; // cross to the right side
                taken++;

                // after arriving, spend pick time then become ready on right side
                int finishPick = (int)(cur + pick[id]);
                rightAvail.Enqueue(new Event { Time = finishPick, Id = id }, finishPick);
            }
            else
            {
                // bridge idle, jump to next event time
                long nextTime = long.MaxValue;
                if (leftAvail.Count > 0) nextTime = Math.Min(nextTime, leftAvail.Peek().Time);
                if (rightAvail.Count > 0) nextTime = Math.Min(nextTime, rightAvail.Peek().Time);
                cur = nextTime;
            }
        }

        return (int)cur; // should never reach here
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @param {number[][]} time
 * @return {number}
 */
var findCrossingTime = function(n, k, time) {
    // Max-heap for idle workers (less efficient first)
    class MaxHeap {
        constructor(cmp) {
            this.cmp = cmp; // returns true if a has higher priority than b
            this.heap = [];
        }
        size() { return this.heap.length; }
        peek() { return this.heap[0]; }
        push(val) {
            const h = this.heap;
            h.push(val);
            let i = h.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (!this.cmp(h[i], h[p])) break;
                [h[i], h[p]] = [h[p], h[i]];
                i = p;
            }
        }
        pop() {
            const h = this.heap;
            if (h.length === 0) return undefined;
            const top = h[0];
            const last = h.pop();
            if (h.length > 0) {
                h[0] = last;
                let i = 0;
                while (true) {
                    let l = i * 2 + 1, r = i * 2 + 2, best = i;
                    if (l < h.length && this.cmp(h[l], h[best])) best = l;
                    if (r < h.length && this.cmp(h[r], h[best])) best = r;
                    if (best === i) break;
                    [h[i], h[best]] = [h[best], h[i]];
                    i = best;
                }
            }
            return top;
        }
    }

    // Min-heap for events ordered by time
    class MinHeap {
        constructor() {
            this.heap = [];
        }
        size() { return this.heap.length; }
        peek() { return this.heap[0]; }
        push(val) {
            const h = this.heap;
            h.push(val);
            let i = h.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (h[p].time <= h[i].time) break;
                [h[i], h[p]] = [h[p], h[i]];
                i = p;
            }
        }
        pop() {
            const h = this.heap;
            if (h.length === 0) return undefined;
            const top = h[0];
            const last = h.pop();
            if (h.length > 0) {
                h[0] = last;
                let i = 0;
                while (true) {
                    let l = i * 2 + 1, r = i * 2 + 2, smallest = i;
                    if (l < h.length && h[l].time < h[smallest].time) smallest = l;
                    if (r < h.length && h[r].time < h[smallest].time) smallest = r;
                    if (smallest === i) break;
                    [h[i], h[smallest]] = [h[smallest], h[i]];
                    i = smallest;
                }
            }
            return top;
        }
    }

    // comparator for workers: less efficient first (larger total crossing, then larger index)
    const workerCmp = (a, b) => {
        const sumA = time[a][0] + time[a][2];
        const sumB = time[b][0] + time[b][2];
        if (sumA !== sumB) return sumA > sumB;
        return a > b;
    };

    const leftIdle = new MaxHeap(workerCmp);
    const rightIdle = new MaxHeap(workerCmp);
    for (let i = 0; i < k; ++i) leftIdle.push(i);

    // events: {time, worker, side} side 0 -> becomes idle on right after picking,
    // side 1 -> becomes idle on left after putting
    const events = new MinHeap();

    let cur = 0;
    let moved = 0;
    let answer = 0;

    while (moved < n) {
        // release all workers whose tasks finished up to current time
        while (events.size() && events.peek().time <= cur) {
            const ev = events.pop();
            if (ev.side === 0) { // idle on right
                rightIdle.push(ev.worker);
            } else { // side ===1, idle on left
                leftIdle.push(ev.worker);
            }
        }

        if (rightIdle.size() > 0) {
            const w = rightIdle.pop();
            cur += time[w][2];               // cross right -> left with box
            moved++;
            answer = cur;                    // arrival time at left with the box
            // schedule put operation, after which worker becomes idle on left
            events.push({time: cur + time[w][3], worker: w, side: 1});
        } else if (moved < n && leftIdle.size() > 0) {
            const w = leftIdle.pop();
            cur += time[w][0];               // cross left -> right empty
            // schedule pick operation, after which worker becomes idle on right
            events.push({time: cur + time[w][1], worker: w, side: 0});
        } else {
            // no one can move now, jump to next event time
            if (events.size() === 0) break; // safety
            cur = events.peek().time;
        }
    }

    return answer;
};
```

## Typescript

```typescript
function findCrossingTime(n: number, k: number, time: number[][]): number {
    // MinHeap implementation
    class MinHeap<T> {
        private data: T[] = [];
        private cmp: (a: T, b: T) => boolean;
        constructor(cmp: (a: T, b: T) => boolean) {
            this.cmp = cmp;
        }
        size(): number { return this.data.length; }
        peek(): T | undefined { return this.data[0]; }
        push(item: T): void {
            const a = this.data;
            a.push(item);
            let i = a.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (!this.cmp(a[i], a[p])) break;
                [a[i], a[p]] = [a[p], a[i]];
                i = p;
            }
        }
        pop(): T | undefined {
            const a = this.data;
            if (a.length === 0) return undefined;
            const top = a[0];
            const last = a.pop()!;
            if (a.length > 0) {
                a[0] = last;
                let i = 0;
                while (true) {
                    let l = i * 2 + 1;
                    let r = i * 2 + 2;
                    let smallest = i;
                    if (l < a.length && this.cmp(a[l], a[smallest])) smallest = l;
                    if (r < a.length && this.cmp(a[r], a[smallest])) smallest = r;
                    if (smallest === i) break;
                    [a[i], a[smallest]] = [a[smallest], a[i]];
                    i = smallest;
                }
            }
            return top;
        }
    }

    // Comparator for workers based on efficiency
    const workerCmp = (i: number, j: number): boolean => {
        const sumI = time[i][0] + time[i][2];
        const sumJ = time[j][0] + time[j][2];
        if (sumI !== sumJ) return sumI < sumJ;
        return i < j;
    };

    // Heaps for available workers on each side
    const leftHeap = new MinHeap<number>(workerCmp);
    const rightHeap = new MinHeap<number>(workerCmp);

    // Initialize all workers on the left side
    for (let i = 0; i < k; ++i) leftHeap.push(i);

    type Event = { t: number; id: number; side: 'left' | 'right' };
    const eventCmp = (a: Event, b: Event): boolean => a.t < b.t;
    const busyHeap = new MinHeap<Event>(eventCmp);

    let cur = 0;
    let boxesRemaining = n;
    let delivered = 0;
    let answer = 0;

    while (delivered < n) {
        // Release workers whose tasks have finished by current time
        while (busyHeap.size() && busyHeap.peek()!.t <= cur) {
            const ev = busyHeap.pop()!;
            if (ev.side === 'left') leftHeap.push(ev.id);
            else rightHeap.push(ev.id);
        }

        if (rightHeap.size()) {
            // Worker on the right returns with a box
            const id = rightHeap.pop()!;
            cur += time[id][2];          // crossing to left
            answer = cur;                // arrival time of this box
            delivered++;
            // After putting the box, worker becomes idle on left
            busyHeap.push({ t: cur + time[id][3], id, side: 'left' });
        } else if (boxesRemaining > 0 && leftHeap.size()) {
            // Send a worker from left to right to fetch a box
            const id = leftHeap.pop()!;
            cur += time[id][0];          // crossing to right
            // After picking the box, worker becomes ready on right side
            busyHeap.push({ t: cur + time[id][1], id, side: 'right' });
            boxesRemaining--;
        } else {
            // No available workers; jump to next event time
            if (busyHeap.size() === 0) break;
            cur = busyHeap.peek()!.t;
        }
    }

    return answer;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @param Integer $k
     * @param Integer[][] $time
     * @return Integer
     */
    function findCrossingTime($n, $k, $time) {
        // priority for idle workers: higher = more efficient (smaller total crossing time, then smaller index)
        $leftIdle = new SplPriorityQueue();
        $rightIdle = new SplPriorityQueue();
        $leftIdle->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        $rightIdle->setExtractFlags(SplPriorityQueue::EXTR_DATA);

        for ($i = 0; $i < $k; ++$i) {
            $eff = $time[$i][0] + $time[$i][2]; // right + left crossing times
            $priority = -$eff * 100000 - $i;   // larger priority => more efficient
            $leftIdle->insert($i, $priority);
        }

        // busy heap: min-heap based on event time (use negative time as priority for max-heap behavior)
        $busy = new SplPriorityQueue();
        $busy->setExtractFlags(SplPriorityQueue::EXTR_DATA);

        $currentTime = 0;
        $boxesRemaining = $n;
        $lastArrival = 0;

        while ($boxesRemaining > 0 || !$rightIdle->isEmpty() || !$busy->isEmpty()) {
            // move completed busy events to idle queues
            while (!$busy->isEmpty()) {
                $event = $busy->top(); // [time, id, side]
                if ($event[0] <= $currentTime) {
                    $busy->extract();
                    $id   = $event[1];
                    $side = $event[2]; // 0 -> left idle, 1 -> right idle
                    $eff = $time[$id][0] + $time[$id][2];
                    $priority = -$eff * 100000 - $id;
                    if ($side === 0) {
                        $leftIdle->insert($id, $priority);
                    } else {
                        $rightIdle->insert($id, $priority);
                    }
                } else {
                    break;
                }
            }

            if (!$leftIdle->isEmpty() && $boxesRemaining > 0) {
                // take most efficient worker from left side to fetch a box
                $id = $leftIdle->extract();
                $boxesRemaining--;

                // cross empty to right (bridge occupied)
                $crossTime = $time[$id][0];
                $currentTime += $crossTime;

                // after arriving, pick the box (no bridge)
                $pickTime = $time[$id][1];
                $readyTime = $currentTime + $pickTime; // becomes ready on right side

                // schedule becoming idle on right side (ready to cross left with box)
                $busy->insert([$readyTime, $id, 1], -$readyTime);
            } elseif (!$rightIdle->isEmpty()) {
                // take most efficient worker from right side to bring a box back
                $id = $rightIdle->extract();

                // cross left with box (bridge occupied)
                $crossTime = $time[$id][2];
                $currentTime += $crossTime;

                // record arrival time of the box at left side
                if ($currentTime > $lastArrival) {
                    $lastArrival = $currentTime;
                }

                // after arriving, put the box (no bridge)
                $putTime = $time[$id][3];
                $readyTime = $currentTime + $putTime; // becomes idle on left side

                // schedule becoming idle on left side
                $busy->insert([$readyTime, $id, 0], -$readyTime);
            } else {
                // no worker ready to cross, jump to next event time
                if (!$busy->isEmpty()) {
                    $nextEvent = $busy->top(); // [time, id, side]
                    $currentTime = $nextEvent[0];
                }
            }
        }

        return $lastArrival;
    }
}
```

## Swift

```swift
class Solution {
    func findCrossingTime(_ n: Int, _ k: Int, _ time: [[Int]]) -> Int {
        // total crossing time for efficiency comparison
        var total = [Int](repeating: 0, count: k)
        for i in 0..<k {
            total[i] = time[i][0] + time[i][2]
        }
        
        var leftHeap = Heap<(Int, Int)>(sort: { a, b in
            if a.0 == b.0 { return a.1 < b.1 } else { return a.0 < b.0 }
        })
        var rightHeap = Heap<(Int, Int)>(sort: { a, b in
            if a.0 == b.0 { return a.1 < b.1 } else { return a.0 < b.0 }
        })
        for i in 0..<k {
            leftHeap.insert((total[i], i))
        }
        
        // busy heap stores (availableTime, side(0:left,1:right), workerIdx)
        var busyHeap = Heap<(Int, Int, Int)>(sort: { $0.0 < $1.0 })
        
        var cur = 0
        var delivered = 0
        var answer = 0
        
        while delivered < n {
            // release workers whose tasks finished by current time
            while let top = busyHeap.peek, top.0 <= cur {
                let (_, side, idx) = busyHeap.remove()!
                if side == 0 {
                    leftHeap.insert((total[idx], idx))
                } else {
                    rightHeap.insert((total[idx], idx))
                }
            }
            
            if !rightHeap.isEmpty {
                // worker on right goes left with a box
                let (_, idx) = rightHeap.remove()!
                cur += time[idx][2]               // crossing left
                delivered += 1
                answer = cur                       // arrival time on left
                let finish = cur + time[idx][3]    // put box
                busyHeap.insert((finish, 0, idx))
            } else if !leftHeap.isEmpty && delivered < n {
                // worker on left goes right empty
                let (_, idx) = leftHeap.remove()!
                cur += time[idx][0]               // crossing right
                let finish = cur + time[idx][1]    // pick box
                busyHeap.insert((finish, 1, idx))
            } else {
                // no idle workers can move now, jump to next event
                if let next = busyHeap.peek {
                    cur = next.0
                }
            }
        }
        
        return answer
    }
}

// Generic min-heap
struct Heap<Element> {
    private var elements: [Element] = []
    private let sort: (Element, Element) -> Bool
    
    init(sort: @escaping (Element, Element) -> Bool) {
        self.sort = sort
    }
    
    var isEmpty: Bool { elements.isEmpty }
    var peek: Element? { elements.first }
    
    mutating func insert(_ value: Element) {
        elements.append(value)
        siftUp(from: elements.count - 1)
    }
    
    mutating func remove() -> Element? {
        guard !elements.isEmpty else { return nil }
        if elements.count == 1 {
            return elements.removeLast()
        } else {
            let value = elements[0]
            elements[0] = elements.removeLast()
            siftDown(from: 0)
            return value
        }
    }
    
    private mutating func siftUp(from index: Int) {
        var child = index
        var parent = (child - 1) / 2
        while child > 0 && sort(elements[child], elements[parent]) {
            elements.swapAt(child, parent)
            child = parent
            parent = (child - 1) / 2
        }
    }
    
    private mutating func siftDown(from index: Int) {
        var parent = index
        while true {
            let left = parent * 2 + 1
            let right = left + 1
            var candidate = parent
            if left < elements.count && sort(elements[left], elements[candidate]) {
                candidate = left
            }
            if right < elements.count && sort(elements[right], elements[candidate]) {
                candidate = right
            }
            if candidate == parent { return }
            elements.swapAt(parent, candidate)
            parent = candidate
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findCrossingTime(n: Int, k: Int, time: Array<IntArray>): Int {
        // Comparator for efficiency: smaller (left+right) sum is more efficient,
        // tie broken by smaller index.
        val cmp = Comparator<Int> { a, b ->
            val sumA = time[a][0] + time[a][2]
            val sumB = time[b][0] + time[b][2]
            if (sumA != sumB) sumA - sumB else a - b
        }
        val leftPQ = java.util.PriorityQueue<Int>(cmp)
        val rightPQ = java.util.PriorityQueue<Int>(cmp)

        for (i in 0 until k) leftPQ.add(i)

        data class Event(val t: Int, val id: Int, val side: Int) // side: 0=left,1=right
        val busyPQ = java.util.PriorityQueue<Event>(Comparator { e1, e2 -> e1.t - e2.t })

        var cur = 0
        var boxesLeft = n
        var delivered = 0
        var answer = 0

        while (delivered < n) {
            // Move workers that have finished their non‑bridge work to waiting queues.
            while (busyPQ.isNotEmpty() && busyPQ.peek().t <= cur) {
                val ev = busyPQ.poll()
                if (ev.side == 0) leftPQ.add(ev.id) else rightPQ.add(ev.id)
            }

            var id: Int? = null
            var fromRight = false

            // Choose the next worker to cross according to the rules.
            if (rightPQ.isNotEmpty() && leftPQ.isNotEmpty()) {
                val l = leftPQ.peek()
                val r = rightPQ.peek()
                val sumL = time[l][0] + time[l][2]
                val sumR = time[r][0] + time[r][2]
                if (sumL < sumR || (sumL == sumR && l < r)) {
                    id = leftPQ.poll()
                    fromRight = false
                } else {
                    id = rightPQ.poll()
                    fromRight = true
                }
            } else if (rightPQ.isNotEmpty()) {
                id = rightPQ.poll()
                fromRight = true
            } else if (leftPQ.isNotEmpty() && boxesLeft > 0) {
                id = leftPQ.poll()
                fromRight = false
            }

            if (id == null) {
                // No one can cross now; jump to the next event time.
                cur = busyPQ.peek().t
                continue
            }

            val w = id!!

            if (!fromRight) {
                // Left -> Right: fetch a box.
                cur += time[w][0]                     // crossing time
                val readyTime = cur + time[w][1]      // after picking the box
                busyPQ.add(Event(readyTime, w, 1))    // now waiting on right side
                boxesLeft--
            } else {
                // Right -> Left: deliver a box.
                cur += time[w][2]                     // crossing back time
                delivered++
                answer = cur                          // last arrival time so far
                val readyTime = cur + time[w][3]      // after putting the box down
                busyPQ.add(Event(readyTime, w, 0))    // now waiting on left side
            }
        }

        return answer
    }
}
```

## Dart

```dart
import 'dart:io';

class _Heap<T> {
  final List<T> _data = [];
  final bool Function(T a, T b) _cmp;
  _Heap(this._cmp);
  bool get isEmpty => _data.isEmpty;
  T peek() => _data[0];
  void push(T value) {
    _data.add(value);
    _siftUp(_data.length - 1);
  }
  T pop() {
    final res = _data[0];
    final last = _data.removeLast();
    if (_data.isNotEmpty) {
      _data[0] = last;
      _siftDown(0);
    }
    return res;
  }
  void _siftUp(int i) {
    while (i > 0) {
      final p = (i - 1) >> 1;
      if (_cmp(_data[i], _data[p])) {
        final tmp = _data[i];
        _data[i] = _data[p];
        _data[p] = tmp;
        i = p;
      } else {
        break;
      }
    }
  }

  void _siftDown(int i) {
    final n = _data.length;
    while (true) {
      int l = i * 2 + 1;
      int r = l + 1;
      int best = i;
      if (l < n && _cmp(_data[l], _data[best])) best = l;
      if (r < n && _cmp(_data[r], _data[best])) best = r;
      if (best == i) break;
      final tmp = _data[i];
      _data[i] = _data[best];
      _data[best] = tmp;
      i = best;
    }
  }
}

class _Event {
  int time;
  int side; // 0: left, 1: right
  int worker;
  _Event(this.time, this.side, this.worker);
}

class Solution {
  int findCrossingTime(int n, int k, List<List<int>> time) {
    // Precompute total crossing time for each worker.
    final List<int> total = List.filled(k, 0);
    for (int i = 0; i < k; ++i) {
      total[i] = time[i][0] + time[i][2];
    }

    // Max-heap for waiting workers on left/right: less efficient first.
    bool workerCmp(int a, int b) {
      if (total[a] != total[b]) return total[a] > total[b];
      return a > b;
    }

    final _Heap<int> leftHeap = _Heap<int>(workerCmp);
    final _Heap<int> rightHeap = _Heap<int>(workerCmp);

    for (int i = 0; i < k; ++i) leftHeap.push(i);

    // Min-heap for events based on time.
    final _Heap<_Event> eventHeap = _Heap<_Event>((a, b) => a.time < b.time);

    int cur = 0;
    int remainingBoxes = n;
    int delivered = 0;
    int lastArrival = 0;

    while (delivered < n) {
      if (!rightHeap.isEmpty) {
        // Worker on right brings box to left.
        final w = rightHeap.pop();
        cur += time[w][2]; // crossing left
        lastArrival = cur; // arrival with box
        delivered++;

        // After arriving, worker puts the box.
        eventHeap.push(_Event(cur + time[w][3], 0, w));
      } else if (remainingBoxes > 0 && !leftHeap.isEmpty) {
        // Send a worker from left to right empty.
        final w = leftHeap.pop();
        cur += time[w][0]; // crossing right
        // After arriving, worker picks a box.
        eventHeap.push(_Event(cur + time[w][1], 1, w));
        remainingBoxes--;
      } else {
        // No one can cross now; advance to next event.
        final ev = eventHeap.pop();
        cur = ev.time;
        if (ev.side == 0) {
          leftHeap.push(ev.worker);
        } else {
          rightHeap.push(ev.worker);
        }
        while (!eventHeap.isEmpty && eventHeap.peek().time == cur) {
          final e2 = eventHeap.pop();
          if (e2.side == 0) {
            leftHeap.push(e2.worker);
          } else {
            rightHeap.push(e2.worker);
          }
        }
      }
    }

    return lastArrival;
  }
}
```

## Golang

```go
package main

import (
	"container/heap"
)

var gTime [][]int

type workerHeap struct {
	data []int
}

func (h workerHeap) Len() int { return len(h.data) }
func (h workerHeap) Less(i, j int) bool {
	sumI := gTime[h.data[i]][0] + gTime[h.data[i]][2]
	sumJ := gTime[h.data[j]][0] + gTime[h.data[j]][2]
	if sumI != sumJ {
		return sumI > sumJ // larger sum = less efficient, should come first
	}
	return h.data[i] > h.data[j] // larger index = less efficient
}
func (h workerHeap) Swap(i, j int) { h.data[i], h.data[j] = h.data[j], h.data[i] }
func (h *workerHeap) Push(x interface{}) {
	h.data = append(h.data, x.(int))
}
func (h *workerHeap) Pop() interface{} {
	old := h.data
	n := len(old)
	it := old[n-1]
	h.data = old[:n-1]
	return it
}

type busyItem struct {
	ready int
	idx   int
}

type busyHeap []busyItem

func (h busyHeap) Len() int           { return len(h) }
func (h busyHeap) Less(i, j int) bool { return h[i].ready < h[j].ready }
func (h busyHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *busyHeap) Push(x interface{}) {
	*h = append(*h, x.(busyItem))
}
func (h *busyHeap) Pop() interface{} {
	old := *h
	n := len(old)
	it := old[n-1]
	*h = old[:n-1]
	return it
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func findCrossingTime(n int, k int, time [][]int) int {
	gTime = time

	leftWait := &workerHeap{}
	rightWait := &workerHeap{}
	heap.Init(leftWait)
	heap.Init(rightWait)

	for i := 0; i < k; i++ {
		heap.Push(leftWait, i)
	}

	leftBusy := &busyHeap{}
	rightBusy := &busyHeap{}
	heap.Init(leftBusy)
	heap.Init(rightBusy)

	t := 0
	delivered := 0
	ans := 0

	for delivered < n {
		// move workers that have finished their tasks to waiting queues
		for leftBusy.Len() > 0 && (*leftBusy)[0].ready <= t {
			it := heap.Pop(leftBusy).(busyItem)
			heap.Push(leftWait, it.idx)
		}
		for rightBusy.Len() > 0 && (*rightBusy)[0].ready <= t {
			it := heap.Pop(rightBusy).(busyItem)
			heap.Push(rightWait, it.idx)
		}

		if rightWait.Len() > 0 {
			idx := heap.Pop(rightWait).(int)
			// cross left
			t += gTime[idx][2]
			ans = max(ans, t) // arrival time of the box
			delivered++
			ready := t + gTime[idx][3] // after putting the box
			heap.Push(leftBusy, busyItem{ready, idx})
		} else if leftWait.Len() > 0 && delivered < n {
			idx := heap.Pop(leftWait).(int)
			// cross right
			t += gTime[idx][0]
			ready := t + gTime[idx][1] // after picking the box
			heap.Push(rightBusy, busyItem{ready, idx})
		} else {
			// no one can move now, jump to next event time
			next := int(^uint(0) >> 1) // max int
			if leftBusy.Len() > 0 && (*leftBusy)[0].ready < next {
				next = (*leftBusy)[0].ready
			}
			if rightBusy.Len() > 0 && (*rightBusy)[0].ready < next {
				next = (*rightBusy)[0].ready
			}
			t = next
		}
	}

	return ans
}
```

## Ruby

```ruby
class MinHeap
  def initialize(&comp)
    @data = []
    @comp = comp || ->(a, b) { a < b }
  end

  def push(item)
    @data << item
    sift_up(@data.size - 1)
  end

  def pop
    return nil if @data.empty?
    top = @data[0]
    last = @data.pop
    unless @data.empty?
      @data[0] = last
      sift_down(0)
    end
    top
  end

  def peek
    @data[0]
  end

  def empty?
    @data.empty?
  end

  private

  def sift_up(idx)
    while idx > 0
      parent = (idx - 1) / 2
      break unless @comp.call(@data[idx], @data[parent])
      @data[idx], @data[parent] = @data[parent], @data[idx]
      idx = parent
    end
  end

  def sift_down(idx)
    size = @data.size
    loop do
      left = idx * 2 + 1
      right = left + 1
      smallest = idx
      if left < size && @comp.call(@data[left], @data[smallest])
        smallest = left
      end
      if right < size && @comp.call(@data[right], @data[smallest])
        smallest = right
      end
      break if smallest == idx
      @data[idx], @data[smallest] = @data[smallest], @data[idx]
      idx = smallest
    end
  end
end

# @param {Integer} n
# @param {Integer} k
# @param {Integer[][]} time
# @return {Integer}
def find_crossing_time(n, k, time)
  total = Array.new(k) { |i| time[i][0] + time[i][2] }

  left_wait = MinHeap.new do |a, b|
    if a[0] == b[0]
      a[1] < b[1]
    else
      a[0] < b[0]
    end
  end

  right_wait = MinHeap.new do |a, b|
    if a[0] == b[0]
      a[1] < b[1]
    else
      a[0] < b[0]
    end
  end

  busy = MinHeap.new { |a, b| a[0] < b[0] } # compare finish_time

  k.times { |i| left_wait.push([total[i], i]) }

  cur = 0
  boxes_left = n
  last_arrival = 0

  while boxes_left > 0 || !right_wait.empty? || !busy.empty?
    while !busy.empty? && busy.peek[0] <= cur
      ft, i, state = busy.pop
      if state == :after_pick
        right_wait.push([total[i], i])
      else # :after_put
        left_wait.push([total[i], i])
      end
    end

    if boxes_left > 0 && !left_wait.empty?
      _, i = left_wait.pop
      cur += time[i][0]                     # cross to right
      finish = cur + time[i][1]             # pick box
      busy.push([finish, i, :after_pick])
    elsif !right_wait.empty?
      _, i = right_wait.pop
      cur += time[i][2]                     # cross left with box
      last_arrival = [last_arrival, cur].max
      finish = cur + time[i][3]             # put box
      busy.push([finish, i, :after_put])
      boxes_left -= 1
    else
      cur = busy.peek[0] if !busy.empty?
    end
  end

  last_arrival
end
```

## Scala

```scala
object Solution {
    import java.util.{PriorityQueue => JPQ}
    case class Event(t: Int, w: Int, side: Int) // side: 0 left, 1 right

    def findCrossingTime(n: Int, k: Int, time: Array[Array[Int]]): Int = {
        val sum = new Array[Int](k)
        for (i <- 0 until k) sum(i) = time(i)(0) + time(i)(2)

        // Comparator for waiting queues: less efficient first (larger sum, larger index)
        val waitCmp = new java.util.Comparator[Int] {
            override def compare(a: Int, b: Int): Int = {
                if (sum(a) != sum(b)) sum(b) - sum(a) else b - a
            }
        }

        val leftWait = new JPQ[Int](waitCmp)
        val rightWait = new JPQ[Int](waitCmp)

        for (i <- 0 until k) leftWait.add(i)

        // Busy events: when worker finishes pick/put and becomes waiting on a side
        val busyCmp = new java.util.Comparator[Event] {
            override def compare(a: Event, b: Event): Int = {
                if (a.t != b.t) a.t - b.t else a.w - b.w
            }
        }
        val busy = new JPQ[Event](busyCmp)

        var cur = 0
        var bridgeFree = 0 // time when bridge becomes free
        var boxes = n
        var answer = 0

        while (boxes > 0 || !rightWait.isEmpty || !busy.isEmpty) {
            // move completed actions to waiting queues
            while (!busy.isEmpty && busy.peek().t <= cur) {
                val ev = busy.poll()
                if (ev.side == 0) leftWait.add(ev.w) else rightWait.add(ev.w)
            }

            if (cur < bridgeFree) {
                var next = bridgeFree
                if (!busy.isEmpty && busy.peek().t < next) next = busy.peek().t
                cur = next
                // continue loop to process newly available workers
            } else {
                if (!rightWait.isEmpty) {
                    val w = rightWait.poll()
                    // cross back to left
                    bridgeFree = cur + time(w)(2) // left_i
                    val ready = bridgeFree + time(w)(3) // put_i
                    answer = Math.max(answer, ready)
                    busy.add(Event(ready, w, 0)) // becomes waiting on left after putting
                } else if (boxes > 0 && !leftWait.isEmpty) {
                    val w = leftWait.poll()
                    // cross to right
                    bridgeFree = cur + time(w)(0) // right_i
                    val ready = bridgeFree + time(w)(1) // pick_i
                    busy.add(Event(ready, w, 1)) // becomes waiting on right after picking
                    boxes -= 1
                } else {
                    // no one can cross now; jump to next event time
                    if (!busy.isEmpty) {
                        cur = Math.max(cur, busy.peek().t)
                    }
                }
            }
        }

        answer
    }
}
```

## Rust

```rust
use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn find_crossing_time(n: i32, k: i32, time: Vec<Vec<i32>>) -> i32 {
        let n_boxes = n as i64;
        let k_usize = k as usize;
        // left_wait and right_wait store (efficiency, idx) where larger is less efficient
        let mut left_wait: BinaryHeap<(i32, i32)> = BinaryHeap::new();
        for i in 0..k_usize {
            let eff = time[i][0] + time[i][2];
            left_wait.push((eff, i as i32));
        }
        let mut right_wait: BinaryHeap<(i32, i32)> = BinaryHeap::new();

        // busy events: (available_time, idx, side) where side 0 -> left_wait, 1 -> right_wait
        let mut busy: BinaryHeap<Reverse<(i64, usize, u8)>> = BinaryHeap::new();

        let mut cur: i64 = 0;
        let mut done: i64 = 0;

        while done < n_boxes {
            // move ready workers from busy to waiting queues
            while let Some(&Reverse((t, _, _))) = busy.peek() {
                if t <= cur {
                    let Reverse((_, idx, side)) = busy.pop().unwrap();
                    let eff = time[idx][0] + time[idx][2];
                    if side == 0 {
                        left_wait.push((eff, idx as i32));
                    } else {
                        right_wait.push((eff, idx as i32));
                    }
                } else {
                    break;
                }
            }

            if let Some((_, idx_i32)) = left_wait.pop() {
                let idx = idx_i32 as usize;
                cur += time[idx][0] as i64; // cross to right
                let ready_time = cur + time[idx][1] as i64; // finish picking
                busy.push(Reverse((ready_time, idx, 1))); // will wait on right side
            } else if let Some((_, idx_i32)) = right_wait.pop() {
                let idx = idx_i32 as usize;
                cur += time[idx][2] as i64; // cross to left (box delivered)
                done += 1;
                let ready_time = cur + time[idx][3] as i64; // finish putting
                busy.push(Reverse((ready_time, idx, 0))); // will wait on left side
            } else {
                // no one waiting, jump to next event time
                if let Some(&Reverse((t, _, _))) = busy.peek() {
                    cur = t;
                }
            }
        }

        cur as i32
    }
}
```

## Racket

```racket
(require racket/heap)

(define (find-crossing-time n k time)
  ;; convert to vectors for O(1) indexing
  (let* ((time-vec (list->vector (map list->vector time)))
         (eff-sums (for/vector ([i (in-range k)])
                     (+ (vector-ref (vector-ref time-vec i) 0)
                        (vector-ref (vector-ref time-vec i) 2))))
         ;; comparator for efficiency: smaller sum, then smaller index
         (eff-compare
          (lambda (a b)
            (let* ((sa (first a)) (ia (second a))
                   (sb (first b)) (ib (second b)))
              (or (< sa sb) (and (= sa sb) (< ia ib))))))
         ;; comparator for time events: earlier time first
         (time-compare (lambda (a b) (< (first a) (first b))))
         (left-heap (make-heap eff-compare))
         (right-heap (make-heap eff-compare))
         (busy-heap (make-heap time-compare)))
    ;; initially all workers are on the left side
    (for ([i (in-range k)])
      (heap-push! left-heap (list (vector-ref eff-sums i) i)))
    (let loop ((cur 0) (delivered 0))
      (cond
        [(= delivered n) cur] ; answer: time when last box arrives at left side
        [else
         ;; move workers that have finished their current task to waiting queues
         (let move ()
           (when (and (not (heap-empty? busy-heap))
                      (<= (first (heap-peek busy-heap)) cur))
             (define ev (heap-pop! busy-heap))
             (define side (second ev))   ; 0 = left, 1 = right
             (define idx (third ev))
             (if (= side 0)
                 (heap-push! left-heap (list (vector-ref eff-sums idx) idx))
                 (heap-push! right-heap (list (vector-ref eff-sums idx) idx)))
             (move)))
         (cond
           ;; a worker on the right can bring a box back
           [(not (heap-empty? right-heap))
            (define pair (heap-pop! right-heap))
            (define idx (second pair))
            (define new-cur (+ cur (vector-ref (vector-ref time-vec idx) 2))) ; cross right→left
            (if (= (+ delivered 1) n)
                (loop new-cur n)   ; last box has just arrived
                (begin
                  ;; after arriving, worker puts the box then becomes idle on left
                  (define finish (+ new-cur (vector-ref (vector-ref time-vec idx) 3)))
                  (heap-push! busy-heap (list finish 0 idx))
                  (loop new-cur (+ delivered 1)))))]

           ;; no box to bring back, send a worker from left to right to pick one
           [(and (not (heap-empty? left-heap)) (< delivered n))
            (define pair (heap-pop! left-heap))
            (define idx (second pair))
            (define new-cur (+ cur (vector-ref (vector-ref time-vec idx) 0))) ; cross left→right
            (define finish (+ new-cur (vector-ref (vector-ref time-vec idx) 1))) ; pick box
            (heap-push! busy-heap (list finish 1 idx))
            (loop new-cur delivered)]

           ;; no idle workers; jump to next event time
           [else
            (define next-time (first (heap-peek busy-heap)))
            (loop next-time delivered)]))]))))
```

## Erlang

```erlang
-spec find_crossing_time(N :: integer(), K :: integer(), Time :: [[integer()]]) -> integer().
find_crossing_time(N, K, Time) ->
    Times = list_to_tuple(Time),
    TotalsList = [element(1, element(I + 1, Times)) + element(3, element(I + 1, Times)) || I <- lists:seq(0, K - 1)],
    Totals = list_to_tuple(TotalsList),
    LeftWait0 = build_left_wait(K, Totals),
    loop(0, 0, N, LeftWait0, [], [], [], Times, Totals, 0).

%% Build initial left waiting heap (sorted by less efficient first)
build_left_wait(K, Totals) ->
    lists:foldl(fun(I, Acc) -> insert_wait(Acc, I, Totals) end, [], lists:seq(0, K - 1)).

%% Insert worker into wait list sorted descending by total crossing time then index
insert_wait([], Idx, Totals) ->
    [{total(Idx, Totals), Idx}];
insert_wait([{TCi, Ii}|Rest] = List, Idx, Totals) ->
    TCnew = total(Idx, Totals),
    if
        TCnew > TCi orelse (TCnew == TCi andalso Idx > Ii) ->
            [{TCnew, Idx} | List];
        true ->
            [{TCi, Ii} | insert_wait(Rest, Idx, Totals)]
    end.

total(Idx, Totals) -> element(Idx + 1, Totals).

%% Move workers whose busy time <= Cur into waiting list
move_ready([], Wait, _Cur, _Totals) ->
    {Wait, []};
move_ready([{T, Idx}|Rest], Wait, Cur, Totals) ->
    if T =< Cur ->
        NewWait = insert_wait(Wait, Idx, Totals),
        move_ready(Rest, NewWait, Cur, Totals);
    true ->
        {W2, B2} = move_ready(Rest, Wait, Cur, Totals),
        {W2, [{T, Idx}|B2]}
    end.

loop(Cur, Delivered, N, LeftWait, RightWait, LeftBusy, RightBusy, Times, Totals, LastArr) ->
    %% Update waiting lists with workers whose actions have finished
    {LeftWait1, LeftBusy1} = move_ready(LeftBusy, LeftWait, Cur, Totals),
    {RightWait1, RightBusy1} = move_ready(RightBusy, RightWait, Cur, Totals),
    case Delivered >= N of
        true ->
            LastArr;
        false ->
            case RightWait1 of
                [] ->
                    case (Delivered < N) andalso (LeftWait1 =/= []) of
                        true ->
                            [{_, Idx}|RestLeft] = LeftWait1,
                            CrossRight = element(1, element(Idx + 1, Times)),
                            Cur2 = Cur + CrossRight,
                            PickTime = element(2, element(Idx + 1, Times)),
                            ReadyTime = Cur2 + PickTime,
                            NewRightBusy = [{ReadyTime, Idx} | RightBusy1],
                            loop(Cur2, Delivered, N, RestLeft, RightWait1, LeftBusy1, NewRightBusy, Times, Totals, LastArr);
                        false ->
                            %% No waiting workers; jump to next event time
                            NextTimes = [T || {T,_} <- LeftBusy1] ++ [T || {T,_} <- RightBusy1],
                            MinNext = lists:min(NextTimes),
                            loop(MinNext, Delivered, N, LeftWait1, RightWait1, LeftBusy1, RightBusy1, Times, Totals, LastArr)
                    end;
                [{_, Idx}|RestRight] ->
                    CrossLeft = element(3, element(Idx + 1, Times)),
                    Cur2 = Cur + CrossLeft,
                    Delivered2 = Delivered + 1,
                    LastArr2 = Cur2,
                    PutTime = element(4, element(Idx + 1, Times)),
                    ReadyTime = Cur2 + PutTime,
                    NewLeftBusy = [{ReadyTime, Idx} | LeftBusy1],
                    loop(Cur2, Delivered2, N, LeftWait1, RestRight, NewLeftBusy, RightBusy1, Times, Totals, LastArr2)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_crossing_time(n :: integer, k :: integer, time :: [[integer]]) :: integer
  def find_crossing_time(n, _k, time) do
    # Initialize left waiting tree with all workers
    left_wait = Enum.reduce(0..(length(time) - 1), :gb_trees.empty(), fn i, acc ->
      insert_wait(acc, i, time)
    end)

    simulate(
      n,
      0,          # current time
      0,          # boxes delivered
      0,          # answer (last arrival time)
      left_wait,
      :gb_trees.empty(),   # right waiting tree
      :gb_trees.empty(),   # left busy min-heap
      :gb_trees.empty(),   # right busy min-heap
      time
    )
  end

  defp simulate(n, cur, delivered, ans, left_wait, right_wait, left_busy, right_busy, times) do
    if delivered == n do
      ans
    else
      {left_wait, left_busy} = release_ready(cur, left_wait, left_busy, :left, times)
      {right_wait, right_busy} = release_ready(cur, right_wait, right_busy, :right, times)

      cond do
        # prioritize workers on the right side (they carry a box)
        not :gb_trees.is_empty(right_wait) ->
          {{_key, w}, new_right_wait} = pop_min(right_wait)
          cur2 = cur + Enum.at(times[w], 2)               # cross left with box
          delivered2 = delivered + 1
          ans2 = cur2                                      # arrival time of this box
          ready_time = cur2 + Enum.at(times[w], 3)        # put action finishes
          new_left_busy = insert_min(left_busy, {ready_time, w})
          simulate(n, cur2, delivered2, ans2, left_wait, new_right_wait, left_busy, new_left_busy, times)

        # send a worker from the left side to fetch a box
        not :gb_trees.is_empty(left_wait) and delivered < n ->
          {{_key, w}, new_left_wait} = pop_min(left_wait)
          cur2 = cur + Enum.at(times[w], 0)               # cross right
          ready_time = cur2 + Enum.at(times[w], 1)        # pick finishes
          new_right_busy = insert_min(right_busy, {ready_time, w})
          simulate(n, cur2, delivered, ans, new_left_wait, right_wait, left_busy, new_right_busy, times)

        true ->
          # no worker ready; jump to next event time
          next_times =
            []
            |> maybe_add_next_time(left_busy)
            |> maybe_add_next_time(right_busy)

          cur_next = Enum.min(next_times)
          simulate(n, cur_next, delivered, ans, left_wait, right_wait, left_busy, right_busy, times)
      end
    end
  end

  defp maybe_add_next_time(list, heap) do
    if :gb_trees.is_empty(heap) do
      list
    else
      {{{t, _}, _}, _} = peek_min(heap)
      [t | list]
    end
  end

  # Move workers whose busy time has elapsed into the appropriate waiting tree
  defp release_ready(cur, wait_tree, busy_tree, side, times) do
    case peek_min(busy_tree) do
      nil ->
        {wait_tree, busy_tree}

      {{{t, _}, w}, _} when t <= cur ->
        {_key, new_busy} = pop_min(busy_tree)
        updated_wait =
          if side == :left do
            insert_wait(wait_tree, w, times)
          else
            insert_wait(wait_tree, w, times)   # same insertion logic for both sides
          end

        release_ready(cur, updated_wait, new_busy, side, times)

      _ ->
        {wait_tree, busy_tree}
    end
  end

  defp insert_wait(tree, i, times) do
    [r, _pick, l, _put] = Enum.at(times, i)
    sum = r + l
    key = {-sum, -i}
    :gb_trees.insert(key, i, tree)
  end

  defp insert_min(tree, {time, idx}) do
    key = {time, idx}
    :gb_trees.insert(key, idx, tree)
  end

  defp peek_min(tree) do
    iterator = :gb_trees.iterator(tree)

    case :gb_trees.next(iterator) do
      {key, value, _} -> {{key, value}, nil}
      :none -> nil
    end
  end

  defp pop_min(tree) do
    iterator = :gb_trees.iterator(tree)

    case :gb_trees.next(iterator) do
      {key, value, _next_iter} ->
        new_tree = :gb_trees.delete(key, tree)
        {{key, value}, new_tree}

      :none ->
        {{nil, nil}, tree}
    end
  end
end
```
