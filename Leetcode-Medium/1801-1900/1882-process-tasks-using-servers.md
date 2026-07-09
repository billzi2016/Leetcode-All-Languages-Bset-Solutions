# 1882. Process Tasks Using Servers

## Cpp

```cpp
class Solution {
public:
    struct Server {
        int weight;
        int index;
    };
    struct Busy {
        long long time;
        int weight;
        int index;
    };
    struct CmpFree {
        bool operator()(const Server& a, const Server& b) const {
            if (a.weight != b.weight) return a.weight > b.weight;
            return a.index > b.index;
        }
    };
    struct CmpBusy {
        bool operator()(const Busy& a, const Busy& b) const {
            if (a.time != b.time) return a.time > b.time;
            if (a.weight != b.weight) return a.weight > b.weight;
            return a.index > b.index;
        }
    };
    
    vector<int> assignTasks(vector<int>& servers, vector<int>& tasks) {
        int n = servers.size(), m = tasks.size();
        priority_queue<Server, vector<Server>, CmpFree> freePQ;
        priority_queue<Busy, vector<Busy>, CmpBusy> busyPQ;
        
        for (int i = 0; i < n; ++i) {
            freePQ.push({servers[i], i});
        }
        
        vector<int> ans(m);
        long long curTime = 0;
        for (int i = 0; i < m; ++i) {
            curTime = max<long long>(curTime, i);
            
            // release servers that have become free by curTime
            while (!busyPQ.empty() && busyPQ.top().time <= curTime) {
                auto b = busyPQ.top(); busyPQ.pop();
                freePQ.push({b.weight, b.index});
            }
            
            if (freePQ.empty()) {
                // wait for the next server to become free
                curTime = busyPQ.top().time;
                while (!busyPQ.empty() && busyPQ.top().time == curTime) {
                    auto b = busyPQ.top(); busyPQ.pop();
                    freePQ.push({b.weight, b.index});
                }
            }
            
            // assign current task
            Server srv = freePQ.top(); freePQ.pop();
            ans[i] = srv.index;
            long long finish = curTime + tasks[i];
            busyPQ.push({finish, srv.weight, srv.index});
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] assignTasks(int[] servers, int[] tasks) {
        int n = servers.length;
        int m = tasks.length;
        int[] ans = new int[m];

        // Free servers: ordered by weight then index
        PriorityQueue<int[]> free = new PriorityQueue<>((a, b) -> {
            if (a[0] != b[0]) return a[0] - b[0];
            return a[1] - b[1];
        });
        for (int i = 0; i < n; i++) {
            free.offer(new int[]{servers[i], i});
        }

        // Busy servers: ordered by finish time, then weight, then index
        PriorityQueue<long[]> busy = new PriorityQueue<>((a, b) -> {
            if (a[0] != b[0]) return Long.compare(a[0], b[0]);          // finish time
            if (a[1] != b[1]) return Long.compare(a[1], b[1]);          // weight
            return Long.compare(a[2], b[2]);                            // index
        });

        long cur = 0; // current time
        for (int i = 0; i < m; i++) {
            cur = Math.max(cur, i); // task i arrives at second i

            // Release servers that have finished by current time
            while (!busy.isEmpty() && busy.peek()[0] <= cur) {
                long[] b = busy.poll();
                free.offer(new int[]{(int) b[1], (int) b[2]});
            }

            // If no free server, wait for the next one to become available
            if (free.isEmpty()) {
                long[] next = busy.poll();          // earliest finishing server
                cur = next[0];                      // jump time forward
                free.offer(new int[]{(int) next[1], (int) next[2]});
                while (!busy.isEmpty() && busy.peek()[0] == cur) {
                    long[] b = busy.poll();
                    free.offer(new int[]{(int) b[1], (int) b[2]});
                }
            }

            // Assign current task to the best free server
            int[] srv = free.poll();
            ans[i] = srv[1];
            long finishTime = cur + tasks[i];
            busy.offer(new long[]{finishTime, srv[0], srv[1]});
        }

        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def assignTasks(self, servers, tasks):
        """
        :type servers: List[int]
        :type tasks: List[int]
        :rtype: List[int]
        """
        import heapq
        n = len(servers)
        m = len(tasks)
        # available servers: (weight, index)
        avail = [(servers[i], i) for i in range(n)]
        heapq.heapify(avail)
        # busy servers: (free_time, weight, index)
        busy = []
        ans = [0] * m
        cur = 0  # current time pointer

        for i in range(m):
            cur = max(cur, i)  # tasks arrive at second i
            # release servers that have become free by cur
            while busy and busy[0][0] <= cur:
                ft, w, idx = heapq.heappop(busy)
                heapq.heappush(avail, (w, idx))
            # if no server is free, jump to next free time
            if not avail:
                ft, w, idx = heapq.heappop(busy)
                cur = ft
                heapq.heappush(avail, (w, idx))
                while busy and busy[0][0] == cur:
                    ft2, w2, idx2 = heapq.heappop(busy)
                    heapq.heappush(avail, (w2, idx2))
            # assign task i
            w, idx = heapq.heappop(avail)
            ans[i] = idx
            free_time = cur + tasks[i]
            heapq.heappush(busy, (free_time, w, idx))

        return ans
```

## Python3

```python
import heapq
from typing import List

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        n = len(servers)
        available = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(available)
        busy = []  # (free_time, weight, index)
        ans = [0] * len(tasks)

        for i, dur in enumerate(tasks):
            # release servers that have become free by time i
            while busy and busy[0][0] <= i:
                ft, w, idx = heapq.heappop(busy)
                heapq.heappush(available, (w, idx))

            if available:
                w, idx = heapq.heappop(available)
                ans[i] = idx
                heapq.heappush(busy, (i + dur, w, idx))
            else:
                # wait for the earliest server to become free
                ft, w, idx = heapq.heappop(busy)
                heapq.heappush(available, (w, idx))
                while busy and busy[0][0] == ft:
                    ft2, w2, idx2 = heapq.heappop(busy)
                    heapq.heappush(available, (w2, idx2))

                w, idx = heapq.heappop(available)
                ans[i] = idx
                heapq.heappush(busy, (ft + dur, w, idx))

        return ans
```

## C

```c
#include <stdlib.h>

typedef struct {
    int weight;
    int idx;
} FreeNode;

typedef struct {
    long long finish;
    int weight;
    int idx;
} BusyNode;

/* ---------- Free Heap (min by weight, then idx) ---------- */
static void freeHeapSwap(FreeNode *a, FreeNode *b) {
    FreeNode tmp = *a; *a = *b; *b = tmp;
}
static int freeLess(const FreeNode *a, const FreeNode *b) {
    if (a->weight != b->weight) return a->weight < b->weight;
    return a->idx < b->idx;
}
static void freeHeapPush(FreeNode *heap, int *size, FreeNode val) {
    int i = (*size)++;
    heap[i] = val;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (!freeLess(&heap[i], &heap[p])) break;
        freeHeapSwap(&heap[i], &heap[p]);
        i = p;
    }
}
static FreeNode freeHeapPop(FreeNode *heap, int *size) {
    FreeNode top = heap[0];
    heap[0] = heap[--(*size)];
    int i = 0, n = *size;
    while (1) {
        int l = i * 2 + 1, r = l + 1, smallest = i;
        if (l < n && freeLess(&heap[l], &heap[smallest])) smallest = l;
        if (r < n && freeLess(&heap[r], &heap[smallest])) smallest = r;
        if (smallest == i) break;
        freeHeapSwap(&heap[i], &heap[smallest]);
        i = smallest;
    }
    return top;
}

/* ---------- Busy Heap (min by finish, weight, idx) ---------- */
static void busyHeapSwap(BusyNode *a, BusyNode *b) {
    BusyNode tmp = *a; *a = *b; *b = tmp;
}
static int busyLess(const BusyNode *a, const BusyNode *b) {
    if (a->finish != b->finish) return a->finish < b->finish;
    if (a->weight != b->weight) return a->weight < b->weight;
    return a->idx < b->idx;
}
static void busyHeapPush(BusyNode *heap, int *size, BusyNode val) {
    int i = (*size)++;
    heap[i] = val;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (!busyLess(&heap[i], &heap[p])) break;
        busyHeapSwap(&heap[i], &heap[p]);
        i = p;
    }
}
static BusyNode busyHeapPop(BusyNode *heap, int *size) {
    BusyNode top = heap[0];
    heap[0] = heap[--(*size)];
    int i = 0, n = *size;
    while (1) {
        int l = i * 2 + 1, r = l + 1, smallest = i;
        if (l < n && busyLess(&heap[l], &heap[smallest])) smallest = l;
        if (r < n && busyLess(&heap[r], &heap[smallest])) smallest = r;
        if (smallest == i) break;
        busyHeapSwap(&heap[i], &heap[smallest]);
        i = smallest;
    }
    return top;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* assignTasks(int* servers, int serversSize, int* tasks, int tasksSize, int* returnSize) {
    int totalCap = serversSize + tasksSize;          // enough for both heaps
    FreeNode *freeHeap = (FreeNode*)malloc(sizeof(FreeNode) * totalCap);
    BusyNode *busyHeap = (BusyNode*)malloc(sizeof(BusyNode) * totalCap);
    int freeSize = 0, busySize = 0;

    for (int i = 0; i < serversSize; ++i) {
        FreeNode fn = {servers[i], i};
        freeHeapPush(freeHeap, &freeSize, fn);
    }

    int *ans = (int*)malloc(sizeof(int) * tasksSize);
    *returnSize = tasksSize;

    for (int i = 0; i < tasksSize; ++i) {
        long long curTime = i;

        /* release servers that have finished by curTime */
        while (busySize > 0 && busyHeap[0].finish <= curTime) {
            BusyNode bn = busyHeapPop(busyHeap, &busySize);
            FreeNode fn = {bn.weight, bn.idx};
            freeHeapPush(freeHeap, &freeSize, fn);
        }

        if (freeSize == 0) {
            /* wait for the earliest server to become free */
            curTime = busyHeap[0].finish;
            while (busySize > 0 && busyHeap[0].finish <= curTime) {
                BusyNode bn = busyHeapPop(busyHeap, &busySize);
                FreeNode fn = {bn.weight, bn.idx};
                freeHeapPush(freeHeap, &freeSize, fn);
            }
        }

        /* assign task */
        FreeNode server = freeHeapPop(freeHeap, &freeSize);
        ans[i] = server.idx;
        BusyNode busy = {curTime + tasks[i], server.weight, server.idx};
        busyHeapPush(busyHeap, &busySize, busy);
    }

    free(freeHeap);
    free(busyHeap);
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    private class ServerComparer : IComparer<(int weight, int index)>
    {
        public int Compare((int w, int i) a, (int w, int i) b)
        {
            int cmp = a.w.CompareTo(b.w);
            if (cmp != 0) return cmp;
            return a.i.CompareTo(b.i);
        }
    }

    private class BusyComparer : IComparer<(long freeTime, int weight, int index)>
    {
        public int Compare((long ft, int w, int i) a, (long ft, int w, int i) b)
        {
            int cmp = a.ft.CompareTo(b.ft);
            if (cmp != 0) return cmp;
            cmp = a.w.CompareTo(b.w);
            if (cmp != 0) return cmp;
            return a.i.CompareTo(b.i);
        }
    }

    public int[] AssignTasks(int[] servers, int[] tasks)
    {
        int n = servers.Length;
        int m = tasks.Length;

        var available = new SortedSet<(int weight, int index)>(new ServerComparer());
        for (int i = 0; i < n; i++)
            available.Add((servers[i], i));

        var busy = new SortedSet<(long freeTime, int weight, int index)>(new BusyComparer());

        int[] ans = new int[m];
        long time = 0;

        for (int j = 0; j < m; j++)
        {
            if (time < j) time = j;

            while (busy.Count > 0 && busy.Min.freeTime <= time)
            {
                var s = busy.Min;
                busy.Remove(s);
                available.Add((s.weight, s.index));
            }

            if (available.Count == 0)
            {
                var next = busy.Min;
                time = next.freeTime;
                while (busy.Count > 0 && busy.Min.freeTime <= time)
                {
                    var s = busy.Min;
                    busy.Remove(s);
                    available.Add((s.weight, s.index));
                }
            }

            var server = available.Min;
            available.Remove(server);
            ans[j] = server.index;

            long freeAt = time + tasks[j];
            busy.Add((freeAt, server.weight, server.index));
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} servers
 * @param {number[]} tasks
 * @return {number[]}
 */
var assignTasks = function(servers, tasks) {
    class MinHeap {
        constructor(cmp) {
            this.cmp = cmp;
            this.heap = [];
        }
        size() { return this.heap.length; }
        peek() { return this.heap[0]; }
        push(item) {
            const h = this.heap;
            h.push(item);
            let i = h.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (this.cmp(h[p], h[i]) <= 0) break;
                [h[p], h[i]] = [h[i], h[p]];
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
                    if (l < h.length && this.cmp(h[l], h[smallest]) < 0) smallest = l;
                    if (r < h.length && this.cmp(h[r], h[smallest]) < 0) smallest = r;
                    if (smallest === i) break;
                    [h[i], h[smallest]] = [h[smallest], h[i]];
                    i = smallest;
                }
            }
            return top;
        }
    }

    const n = servers.length, m = tasks.length;
    const availCmp = (a, b) => a.w !== b.w ? a.w - b.w : a.id - b.id;
    const busyCmp = (a, b) => {
        if (a.time !== b.time) return a.time - b.time;
        if (a.w !== b.w) return a.w - b.w;
        return a.id - b.id;
    };
    const available = new MinHeap(availCmp);
    const busy = new MinHeap(busyCmp);

    for (let i = 0; i < n; ++i) {
        available.push({ w: servers[i], id: i });
    }

    const ans = new Array(m);
    let curTime = 0;

    for (let i = 0; i < m; ++i) {
        curTime = Math.max(curTime, i);

        // release servers that have become free by curTime
        while (busy.size() && busy.peek().time <= curTime) {
            const s = busy.pop();
            available.push({ w: s.w, id: s.id });
        }

        if (!available.size()) {
            // wait for the next server to free up
            const nextFree = busy.peek().time;
            curTime = nextFree;
            while (busy.size() && busy.peek().time <= curTime) {
                const s = busy.pop();
                available.push({ w: s.w, id: s.id });
            }
        }

        const srv = available.pop();
        ans[i] = srv.id;
        busy.push({ time: curTime + tasks[i], w: srv.w, id: srv.id });
    }

    return ans;
};
```

## Typescript

```typescript
function assignTasks(servers: number[], tasks: number[]): number[] {
    class MinHeap<T> {
        private data: T[];
        private compare: (a: T, b: T) => boolean;
        constructor(compare: (a: T, b: T) => boolean) {
            this.data = [];
            this.compare = compare;
        }
        size(): number { return this.data.length; }
        peek(): T | undefined { return this.data[0]; }
        push(item: T): void {
            const a = this.data;
            a.push(item);
            let i = a.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (this.compare(a[i], a[p])) {
                    [a[i], a[p]] = [a[p], a[i]];
                    i = p;
                } else break;
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
                    let l = i * 2 + 1, r = i * 2 + 2, smallest = i;
                    if (l < a.length && this.compare(a[l], a[smallest])) smallest = l;
                    if (r < a.length && this.compare(a[r], a[smallest])) smallest = r;
                    if (smallest !== i) {
                        [a[i], a[smallest]] = [a[smallest], a[i]];
                        i = smallest;
                    } else break;
                }
            }
            return top;
        }
    }

    const n = servers.length, m = tasks.length;
    const available = new MinHeap<[number, number]>((a, b) =>
        a[0] !== b[0] ? a[0] < b[0] : a[1] < b[1]
    );
    for (let i = 0; i < n; ++i) available.push([servers[i], i]);

    const busy = new MinHeap<[number, number, number]>((a, b) => {
        if (a[0] !== b[0]) return a[0] < b[0];
        if (a[1] !== b[1]) return a[1] < b[1];
        return a[2] < b[2];
    });

    const ans = new Array<number>(m);
    let time = 0;

    for (let i = 0; i < m; ++i) {
        time = Math.max(time, i);

        while (busy.size() && busy.peek()![0] <= time) {
            const [ft, w, idx] = busy.pop()!;
            available.push([w, idx]);
        }

        if (available.size() === 0) {
            const [nextFree, w, idx] = busy.pop()!;
            time = nextFree;
            available.push([w, idx]);
            while (busy.size() && busy.peek()![0] <= time) {
                const [ft2, w2, idx2] = busy.pop()!;
                available.push([w2, idx2]);
            }
        }

        const [w, idx] = available.pop()!;
        ans[i] = idx;
        busy.push([time + tasks[i], w, idx]);
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $servers
     * @param Integer[] $tasks
     * @return Integer[]
     */
    function assignTasks($servers, $tasks) {
        $n = count($servers);
        $m = count($tasks);

        // free servers heap: min weight, then min index (implemented as max-heap with negative priorities)
        $free = new SplPriorityQueue();
        $free->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        for ($i = 0; $i < $n; $i++) {
            $weight = $servers[$i];
            $free->insert(['index' => $i, 'weight' => $weight], [-$weight, -$i]);
        }

        // busy servers heap: earliest finish time, then min weight, then min index
        $busy = new SplPriorityQueue();
        $busy->setExtractFlags(SplPriorityQueue::EXTR_DATA);

        $ans = array_fill(0, $m, 0);
        $currentTime = 0;

        for ($taskIdx = 0; $taskIdx < $m; $taskIdx++) {
            $arrival = $taskIdx;
            if ($currentTime < $arrival) {
                $currentTime = $arrival;
            }

            // Release servers that have finished by current time
            while (!$busy->isEmpty()) {
                $top = $busy->top(); // peek without removing
                if ($top['finish'] <= $currentTime) {
                    $released = $busy->extract();
                    $free->insert(['index' => $released['index'], 'weight' => $released['weight']],
                                  [-$released['weight'], -$released['index']]);
                } else {
                    break;
                }
            }

            // If no free server, wait for the next one to become available
            if ($free->isEmpty()) {
                $next = $busy->extract(); // earliest finishing server
                $currentTime = $next['finish'];
                $free->insert(['index' => $next['index'], 'weight' => $next['weight']],
                              [-$next['weight'], -$next['index']]);
                while (!$busy->isEmpty()) {
                    $top = $busy->top();
                    if ($top['finish'] == $currentTime) {
                        $released = $busy->extract();
                        $free->insert(['index' => $released['index'], 'weight' => $released['weight']],
                                      [-$released['weight'], -$released['index']]);
                    } else {
                        break;
                    }
                }
            }

            // Assign current task to the best free server
            $server = $free->extract();
            $ans[$taskIdx] = $server['index'];
            $finishTime = $currentTime + $tasks[$taskIdx];
            $busy->insert(['index' => $server['index'], 'weight' => $server['weight'], 'finish' => $finishTime],
                          [-$finishTime, -$server['weight'], -$server['index']]);
        }

        return $ans;
    }
}
```

## Swift

```swift
class Heap<T> {
    private var elements: [T] = []
    private let priorityFunction: (T, T) -> Bool
    
    init(sort: @escaping (T, T) -> Bool) {
        self.priorityFunction = sort
    }
    
    var isEmpty: Bool { elements.isEmpty }
    
    func peek() -> T? {
        return elements.first
    }
    
    func push(_ value: T) {
        elements.append(value)
        siftUp(from: elements.count - 1)
    }
    
    func pop() -> T? {
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
    
    private func parent(_ index: Int) -> Int { (index - 1) / 2 }
    private func leftChild(_ index: Int) -> Int { 2 * index + 1 }
    private func rightChild(_ index: Int) -> Int { 2 * index + 2 }
    
    private func siftUp(from index: Int) {
        var child = index
        var parentIdx = parent(child)
        while child > 0 && priorityFunction(elements[child], elements[parentIdx]) {
            elements.swapAt(child, parentIdx)
            child = parentIdx
            parentIdx = parent(child)
        }
    }
    
    private func siftDown(from index: Int) {
        var parentIdx = index
        while true {
            let left = leftChild(parentIdx)
            let right = rightChild(parentIdx)
            var candidate = parentIdx
            if left < elements.count && priorityFunction(elements[left], elements[candidate]) {
                candidate = left
            }
            if right < elements.count && priorityFunction(elements[right], elements[candidate]) {
                candidate = right
            }
            if candidate == parentIdx { return }
            elements.swapAt(parentIdx, candidate)
            parentIdx = candidate
        }
    }
}

struct Server {
    let weight: Int
    let index: Int
}

class Solution {
    func assignTasks(_ servers: [Int], _ tasks: [Int]) -> [Int] {
        let n = servers.count
        var available = Heap<Server>(sort: { a, b in
            if a.weight == b.weight {
                return a.index < b.index
            }
            return a.weight < b.weight
        })
        for i in 0..<n {
            available.push(Server(weight: servers[i], index: i))
        }
        
        var busy = Heap<(Int, Int, Int)>(sort: { a, b in
            // compare freeTime, then weight, then index
            if a.0 == b.0 {
                if a.1 == b.1 {
                    return a.2 < b.2
                }
                return a.1 < b.1
            }
            return a.0 < b.0
        })
        
        var ans = [Int](repeating: 0, count: tasks.count)
        var time = 0
        
        for i in 0..<tasks.count {
            time = max(time, i)
            
            while let top = busy.peek(), top.0 <= time {
                let (_, w, idx) = busy.pop()!
                available.push(Server(weight: w, index: idx))
            }
            
            if available.isEmpty {
                if let nextFree = busy.peek()?.0 {
                    time = nextFree
                    while let top = busy.peek(), top.0 <= time {
                        let (_, w, idx) = busy.pop()!
                        available.push(Server(weight: w, index: idx))
                    }
                }
            }
            
            let server = available.pop()!
            ans[i] = server.index
            let finishTime = time + tasks[i]
            busy.push((finishTime, server.weight, server.index))
        }
        
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    data class Server(val weight: Int, val index: Int)
    data class Busy(val freeTime: Int, val weight: Int, val index: Int)

    fun assignTasks(servers: IntArray, tasks: IntArray): IntArray {
        val n = servers.size
        val m = tasks.size
        val ans = IntArray(m)

        val available = java.util.PriorityQueue<Server>(compareBy<Server> { it.weight }.thenBy { it.index })
        for (i in 0 until n) {
            available.add(Server(servers[i], i))
        }

        val busy = java.util.PriorityQueue<Busy>(compareBy<Busy> { it.freeTime }
            .thenBy { it.weight }
            .thenBy { it.index })

        var time = 0
        for (i in 0 until m) {
            // Ensure current time is at least the arrival time of task i
            if (time < i) time = i

            // Release servers that have become free up to current time
            while (busy.isNotEmpty() && busy.peek().freeTime <= time) {
                val b = busy.poll()
                available.add(Server(b.weight, b.index))
            }

            // If no server is free, jump forward to the next freeing time
            if (available.isEmpty()) {
                val nextFree = busy.peek().freeTime
                time = nextFree
                while (busy.isNotEmpty() && busy.peek().freeTime <= time) {
                    val b = busy.poll()
                    available.add(Server(b.weight, b.index))
                }
            }

            // Assign the task to the best available server
            val srv = available.poll()
            ans[i] = srv.index
            val freeAt = time + tasks[i]
            busy.add(Busy(freeAt, srv.weight, srv.index))
        }

        return ans
    }
}
```

## Dart

```dart
class Server {
  int weight;
  int index;
  Server(this.weight, this.index);
}

class Busy {
  int freeTime;
  int weight;
  int index;
  Busy(this.freeTime, this.weight, this.index);
}

class Heap<T> {
  List<T> _data = [];
  final int Function(T a, T b) _cmp;
  Heap(this._cmp);

  bool get isEmpty => _data.isEmpty;

  T peek() => _data[0];

  void push(T item) {
    _data.add(item);
    _siftUp(_data.length - 1);
  }

  T pop() {
    var res = _data[0];
    var last = _data.removeLast();
    if (_data.isNotEmpty) {
      _data[0] = last;
      _siftDown(0);
    }
    return res;
  }

  void _siftUp(int i) {
    while (i > 0) {
      int p = (i - 1) >> 1;
      if (_cmp(_data[i], _data[p]) < 0) {
        var tmp = _data[i];
        _data[i] = _data[p];
        _data[p] = tmp;
        i = p;
      } else {
        break;
      }
    }
  }

  void _siftDown(int i) {
    int n = _data.length;
    while (true) {
      int l = i * 2 + 1;
      int r = l + 1;
      int smallest = i;
      if (l < n && _cmp(_data[l], _data[smallest]) < 0) smallest = l;
      if (r < n && _cmp(_data[r], _data[smallest]) < 0) smallest = r;
      if (smallest != i) {
        var tmp = _data[i];
        _data[i] = _data[smallest];
        _data[smallest] = tmp;
        i = smallest;
      } else {
        break;
      }
    }
  }
}

class Solution {
  List<int> assignTasks(List<int> servers, List<int> tasks) {
    int n = servers.length;
    int m = tasks.length;

    var avail = Heap<Server>((a, b) {
      if (a.weight != b.weight) return a.weight - b.weight;
      return a.index - b.index;
    });

    for (int i = 0; i < n; ++i) {
      avail.push(Server(servers[i], i));
    }

    var busy = Heap<Busy>((a, b) {
      if (a.freeTime != b.freeTime) return a.freeTime - b.freeTime;
      if (a.weight != b.weight) return a.weight - b.weight;
      return a.index - b.index;
    });

    List<int> ans = List.filled(m, 0);
    int curTime = 0;

    for (int i = 0; i < m; ++i) {
      curTime = i;

      while (!busy.isEmpty && busy.peek().freeTime <= curTime) {
        var b = busy.pop();
        avail.push(Server(b.weight, b.index));
      }

      if (avail.isEmpty) {
        var b = busy.pop();
        curTime = b.freeTime;
        avail.push(Server(b.weight, b.index));
        while (!busy.isEmpty && busy.peek().freeTime <= curTime) {
          var nb = busy.pop();
          avail.push(Server(nb.weight, nb.index));
        }
      }

      var s = avail.pop();
      ans[i] = s.index;
      int freeAt = curTime + tasks[i];
      busy.push(Busy(freeAt, s.weight, s.index));
    }

    return ans;
  }
}
```

## Golang

```go
package main

import "container/heap"

type server struct {
	weight int
	idx    int
}

type serverHeap []server

func (h serverHeap) Len() int { return len(h) }
func (h serverHeap) Less(i, j int) bool {
	if h[i].weight != h[j].weight {
		return h[i].weight < h[j].weight
	}
	return h[i].idx < h[j].idx
}
func (h serverHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h *serverHeap) Push(x interface{}) {
	*h = append(*h, x.(server))
}
func (h *serverHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

type busy struct {
	freeTime int
	weight   int
	idx      int
}

type busyHeap []busy

func (h busyHeap) Len() int { return len(h) }
func (h busyHeap) Less(i, j int) bool {
	if h[i].freeTime != h[j].freeTime {
		return h[i].freeTime < h[j].freeTime
	}
	if h[i].weight != h[j].weight {
		return h[i].weight < h[j].weight
	}
	return h[i].idx < h[j].idx
}
func (h busyHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h *busyHeap) Push(x interface{}) {
	*h = append(*h, x.(busy))
}
func (h *busyHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func assignTasks(servers []int, tasks []int) []int {
	m := len(tasks)
	ans := make([]int, m)

	avail := &serverHeap{}
	for i, w := range servers {
		*avail = append(*avail, server{weight: w, idx: i})
	}
	heap.Init(avail)

	busyQ := &busyHeap{}
	heap.Init(busyQ)

	curTime := 0
	for i := 0; i < m; i++ {
		curTime = i

		// release servers that have become free by curTime
		for busyQ.Len() > 0 && (*busyQ)[0].freeTime <= curTime {
			b := heap.Pop(busyQ).(busy)
			heap.Push(avail, server{weight: b.weight, idx: b.idx})
		}

		if avail.Len() == 0 {
			// wait for the next server to become free
			nextFree := (*busyQ)[0].freeTime
			curTime = nextFree
			for busyQ.Len() > 0 && (*busyQ)[0].freeTime <= curTime {
				b := heap.Pop(busyQ).(busy)
				heap.Push(avail, server{weight: b.weight, idx: b.idx})
			}
		}

		s := heap.Pop(avail).(server)
		ans[i] = s.idx
		heap.Push(busyQ, busy{
			freeTime: curTime + tasks[i],
			weight:   s.weight,
			idx:      s.idx,
		})
	}
	return ans
}
```

## Ruby

```ruby
class MinHeap
  def initialize(&comp)
    @data = []
    @comp = comp || ->(a, b) { a <=> b }
  end

  def push(item)
    @data << item
    sift_up(@data.size - 1)
    self
  end

  alias << push

  def pop
    return nil if empty?
    top = @data[0]
    last = @data.pop
    unless empty?
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
      if @comp.call(@data[idx], @data[parent]) < 0
        @data[idx], @data[parent] = @data[parent], @data[idx]
        idx = parent
      else
        break
      end
    end
  end

  def sift_down(idx)
    size = @data.size
    loop do
      left = idx * 2 + 1
      right = left + 1
      smallest = idx
      if left < size && @comp.call(@data[left], @data[smallest]) < 0
        smallest = left
      end
      if right < size && @comp.call(@data[right], @data[smallest]) < 0
        smallest = right
      end
      break if smallest == idx
      @data[idx], @data[smallest] = @data[smallest], @data[idx]
      idx = smallest
    end
  end
end

# @param {Integer[]} servers
# @param {Integer[]} tasks
# @return {Integer[]}
def assign_tasks(servers, tasks)
  avail = MinHeap.new do |a, b|
    if a[0] == b[0]
      a[1] <=> b[1]
    else
      a[0] <=> b[0]
    end
  end

  busy = MinHeap.new do |a, b|
    if a[0] == b[0]
      if a[1] == b[1]
        a[2] <=> b[2]
      else
        a[1] <=> b[1]
      end
    else
      a[0] <=> b[0]
    end
  end

  servers.each_with_index do |w, i|
    avail << [w, i]
  end

  ans = Array.new(tasks.length)

  tasks.each_with_index do |duration, i|
    while !busy.empty? && busy.peek[0] <= i
      ft, w, idx = busy.pop
      avail << [w, idx]
    end

    if avail.empty?
      ft, w, idx = busy.pop
      current_time = ft
      avail << [w, idx]
      while !busy.empty? && busy.peek[0] == ft
        ft2, w2, idx2 = busy.pop
        avail << [w2, idx2]
      end
      w2, idx2 = avail.pop
      ans[i] = idx2
      busy << [current_time + duration, w2, idx2]
    else
      w, idx = avail.pop
      ans[i] = idx
      busy << [i + duration, w, idx]
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def assignTasks(servers: Array[Int], tasks: Array[Int]): Array[Int] = {
        import java.util.PriorityQueue

        case class Server(weight: Int, index: Int)
        val available = new PriorityQueue[Server]((a: Server, b: Server) => {
            if (a.weight != b.weight) a.weight - b.weight else a.index - b.index
        })

        case class Busy(freeTime: Long, weight: Int, index: Int)
        val busy = new PriorityQueue[Busy]((a: Busy, b: Busy) => {
            if (a.freeTime != b.freeTime) java.lang.Long.compare(a.freeTime, b.freeTime)
            else if (a.weight != b.weight) a.weight - b.weight
            else a.index - b.index
        })

        for (i <- servers.indices) {
            available.offer(Server(servers(i), i))
        }

        val m = tasks.length
        val ans = new Array[Int](m)

        var time: Long = 0L

        for (i <- 0 until m) {
            if (time < i) time = i.toLong

            while (!busy.isEmpty && busy.peek().freeTime <= time) {
                val b = busy.poll()
                available.offer(Server(b.weight, b.index))
            }

            if (available.isEmpty) {
                time = busy.peek().freeTime
                while (!busy.isEmpty && busy.peek().freeTime <= time) {
                    val b = busy.poll()
                    available.offer(Server(b.weight, b.index))
                }
            }

            val s = available.poll()
            ans(i) = s.index
            val finish = time + tasks(i).toLong
            busy.offer(Busy(finish, s.weight, s.index))
        }

        ans
    }
}
```

## Rust

```rust
use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn assign_tasks(servers: Vec<i32>, tasks: Vec<i32>) -> Vec<i32> {
        let n = servers.len();
        let m = tasks.len();

        // Min-heap of available servers ordered by (weight, index)
        let mut available: BinaryHeap<Reverse<(i32, usize)>> = BinaryHeap::new();
        for (idx, &w) in servers.iter().enumerate() {
            available.push(Reverse((w, idx)));
        }

        // Min-heap of busy servers ordered by (free_time, weight, index)
        let mut busy: BinaryHeap<Reverse<(i64, i32, usize)>> = BinaryHeap::new();

        let mut ans = vec![0i32; m];
        let mut time: i64 = 0;

        for j in 0..m {
            // task arrives at second j
            time = time.max(j as i64);

            // release servers that have become free by current time
            while let Some(&Reverse((free_time, w, idx))) = busy.peek() {
                if free_time <= time {
                    busy.pop();
                    available.push(Reverse((w, idx)));
                } else {
                    break;
                }
            }

            // if no server is free, jump to the next freeing time
            if available.is_empty() {
                let Reverse((next_free, w, idx)) = busy.pop().unwrap();
                time = next_free;
                available.push(Reverse((w, idx)));
                while let Some(&Reverse((ft, w2, idx2))) = busy.peek() {
                    if ft == time {
                        busy.pop();
                        available.push(Reverse((w2, idx2)));
                    } else {
                        break;
                    }
                }
            }

            // assign current task to the best available server
            let Reverse((w_best, idx_best)) = available.pop().unwrap();
            ans[j] = idx_best as i32;
            let finish_time = time + tasks[j] as i64;
            busy.push(Reverse((finish_time, w_best, idx_best)));
        }

        ans
    }
}
```

## Racket

```racket
#lang racket
(require racket/priority-queue)

(define (assign-tasks servers tasks)
  (let* ((srv-vec (list->vector servers))
         (task-vec (list->vector tasks))
         (n (vector-length srv-vec))
         (m (vector-length task-vec))
         (available
          (make-pq
           (lambda (a b)
             (let ((w1 (vector-ref a 0)) (i1 (vector-ref a 1))
                   (w2 (vector-ref b 0)) (i2 (vector-ref b 1)))
               (or (< w1 w2) (and (= w1 w2) (< i1 i2)))))))
         (busy
          (make-pq
           (lambda (a b)
             (let ((t1 (vector-ref a 0)) (w1 (vector-ref a 1)) (i1 (vector-ref a 2))
                   (t2 (vector-ref b 0)) (w2 (vector-ref b 1)) (i2 (vector-ref b 2)))
               (or (< t1 t2)
                   (and (= t1 t2)
                        (or (< w1 w2)
                            (and (= w1 w2) (< i1 i2)))))))))
         (ans (make-vector m)))
    ;; initialize available servers
    (for ([i (in-range n)])
      (pq-add! available (vector (vector-ref srv-vec i) i)))
    (let loop ((time 0) (idx 0))
      (when (< idx m)
        ;; release servers that have become free by current time
        (let release ()
          (when (and (> (pq-count busy) 0)
                     (<= (vector-ref (pq-peek busy) 0) time))
            (define srv (pq-pop! busy))
            (pq-add! available (vector (vector-ref srv 1) (vector-ref srv 2)))
            (release)))
        (if (> (pq-count available) 0)
            (begin
              (define srv (pq-pop! available))
              (vector-set! ans idx (vector-ref srv 1))
              (pq-add! busy
                       (vector (+ time (vector-ref task-vec idx))
                               (vector-ref srv 0)
                               (vector-ref srv 1)))
              (loop (+ time 1) (+ idx 1)))
            (let ((next-time (vector-ref (pq-peek busy) 0)))
              (loop next-time idx)))))
    (vector->list ans)))
```

## Erlang

```erlang
-module(solution).
-export([assign_tasks/2]).

-spec assign_tasks(Servers :: [integer()], Tasks :: [integer()]) -> [integer()].
assign_tasks(Servers, Tasks) ->
    Available0 = build_available_tree(Servers),
    AnswersRev = process(Tasks, 0, Available0, gb_trees:empty(), []),
    lists:reverse(AnswersRev).

build_available_tree(Servers) ->
    build_available_tree(Servers, 0, gb_trees:empty()).

build_available_tree([], _Idx, Tree) -> Tree;
build_available_tree([W|Rest], Idx, Tree) ->
    NewTree = gb_trees:insert({W, Idx}, Idx, Tree),
    build_available_tree(Rest, Idx + 1, NewTree).

process([], _Idx, _Avail, _Busy, Acc) ->
    Acc;
process([Dur|Rest], Idx, Avail, Busy, Acc) ->
    CurTime = Idx,
    {Avail1, Busy1} = release_servers(CurTime, Avail, Busy),
    case gb_trees:is_empty(Avail1) of
        false ->
            {{Weight, SIdx}, _} = gb_trees:smallest(Avail1),
            Avail2 = gb_trees:delete_any({Weight, SIdx}, Avail1),
            Finish = CurTime + Dur,
            Busy2 = gb_trees:insert({Finish, Weight, SIdx}, SIdx, Busy1),
            process(Rest, Idx + 1, Avail2, Busy2, [SIdx | Acc]);
        true ->
            {{FreeTime, Weight, SIdx}, _} = gb_trees:smallest(Busy1),
            {Avail2, Busy2} = release_servers(FreeTime, Avail1, Busy1),
            {{Weight2, SIdx2}, _} = gb_trees:smallest(Avail2),
            Avail3 = gb_trees:delete_any({Weight2, SIdx2}, Avail2),
            Finish = FreeTime + Dur,
            Busy3 = gb_trees:insert({Finish, Weight2, SIdx2}, SIdx2, Busy2),
            process(Rest, Idx + 1, Avail3, Busy3, [SIdx2 | Acc])
    end.

release_servers(Time, Avail, Busy) ->
    case gb_trees:is_empty(Busy) of
        true -> {Avail, Busy};
        false ->
            {{FreeTime, Weight, SIdx}, _} = gb_trees:smallest(Busy),
            if FreeTime =< Time ->
                    Busy1 = gb_trees:delete_any({FreeTime, Weight, SIdx}, Busy),
                    Avail1 = gb_trees:insert({Weight, SIdx}, SIdx, Avail),
                    release_servers(Time, Avail1, Busy1);
               true -> {Avail, Busy}
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec assign_tasks(servers :: [integer], tasks :: [integer]) :: [integer]
  def assign_tasks(servers, tasks) do
    # heap of available servers ordered by {weight, index}
    avail =
      Enum.reduce(Enum.with_index(servers), :heap.new(), fn {w, i}, h ->
        :heap.insert({w, i}, h)
      end)

    busy = :heap.new()

    {ans_rev, _final_avail, _final_busy} =
      Enum.reduce(Enum.with_index(tasks), {[], avail, busy}, fn {duration, idx},
                                                                 {acc, av, bu} ->
        current_time = idx

        # release servers that have become free by current_time
        {av1, bu1} = release_servers(av, bu, current_time)

        # if no server is free, jump to the next time a server becomes free
        {av2, bu2, cur_time} =
          if :heap.size(av1) == 0 do
            {{free_time, _w, _i}, _} = :heap.min(bu1)
            {a, b} = release_servers(av1, bu1, free_time)
            {a, b, free_time}
          else
            {av1, bu1, current_time}
          end

        # assign the task to the best available server
        {{w, i}, av_next} = :heap.delete_min(av2)

        acc_next = [i | acc]

        # push the server into busy heap with its new free time
        bu_next = :heap.insert({cur_time + duration, w, i}, bu2)

        {acc_next, av_next, bu_next}
      end)

    Enum.reverse(ans_rev)
  end

  defp release_servers(avail, busy, time) do
    if :heap.size(busy) == 0 do
      {avail, busy}
    else
      case :heap.min(busy) do
        {free_time, w, i} when free_time <= time ->
          {{_ft, _w, _i}, busy2} = :heap.delete_min(busy)
          avail2 = :heap.insert({w, i}, avail)
          release_servers(avail2, busy2, time)

        _ ->
          {avail, busy}
      end
    end
  end
end
```
