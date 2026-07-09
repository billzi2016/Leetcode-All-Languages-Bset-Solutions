# 3594. Minimum Time to Transport All Individuals

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    double minTime(int n, int k, int m, vector<int>& time, vector<double>& mul) {
        int fullMask = (1 << n) - 1;
        const double INF = 1e100;
        // precompute max time for each subset and its popcount
        vector<int> maxTime(1 << n, 0);
        vector<int> pcnt(1 << n, 0);
        for (int mask = 1; mask <= fullMask; ++mask) {
            int lsb = __builtin_ctz(mask);
            int prev = mask ^ (1 << lsb);
            maxTime[mask] = max(maxTime[prev], time[lsb]);
            pcnt[mask] = pcnt[prev] + 1;
        }

        // dist[mask][stage][side]
        vector<vector<array<double,2>>> dist(1<<n, vector<array<double,2>>(m, {INF, INF}));
        using State = tuple<double,int,int,int>; // cost, mask, stage, side
        priority_queue<State, vector<State>, greater<State>> pq;

        dist[0][0][0] = 0.0;
        pq.emplace(0.0, 0, 0, 0); // start at left side

        while (!pq.empty()) {
            auto [d, mask, stage, side] = pq.top(); pq.pop();
            if (d != dist[mask][stage][side]) continue;
            if (mask == fullMask && side == 1) {
                return d; // reached goal
            }
            int avail = (side == 0) ? ((fullMask ^ mask)) : mask; // people on current boat side
            for (int sub = avail; sub; sub = (sub - 1) & avail) {
                if (pcnt[sub] > k) continue;
                double nd = d + maxTime[sub] * mul[stage];
                int nmask = (side == 0) ? (mask | sub) : (mask ^ sub);
                int nstage = (stage + 1) % m;
                int nside = side ^ 1;
                if (nd < dist[nmask][nstage][nside]) {
                    dist[nmask][nstage][nside] = nd;
                    pq.emplace(nd, nmask, nstage, nside);
                }
            }
        }
        return -1.0;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public double minTime(int n, int k, int m, int[] time, double[] mul) {
        int fullMask = (1 << n) - 1;
        // Precompute max time for each subset
        double[] maxTime = new double[1 << n];
        for (int mask = 1; mask <= fullMask; mask++) {
            int lsb = Integer.numberOfTrailingZeros(mask);
            int prev = mask ^ (1 << lsb);
            maxTime[mask] = Math.max(time[lsb], maxTime[prev]);
        }

        double INF = Double.MAX_VALUE / 4;
        double[][][] dist = new double[fullMask + 1][m][2];
        for (int i = 0; i <= fullMask; i++) {
            for (int j = 0; j < m; j++) {
                Arrays.fill(dist[i][j], INF);
            }
        }

        PriorityQueue<Node> pq = new PriorityQueue<>(Comparator.comparingDouble(a -> a.d));
        dist[fullMask][0][0] = 0.0;
        pq.offer(new Node(fullMask, 0, 0, 0.0));

        while (!pq.isEmpty()) {
            Node cur = pq.poll();
            if (cur.d != dist[cur.mask][cur.stage][cur.side]) continue;

            // goal check
            if (cur.mask == 0 && cur.side == 1) {
                return cur.d;
            }

            int available;
            if (cur.side == 0) { // boat on left, move people from left to right
                available = cur.mask;
            } else { // boat on right, move people from right back to left
                available = fullMask ^ cur.mask;
            }

            // iterate non-empty subsets of available with size <= k
            for (int sub = available; sub > 0; sub = (sub - 1) & available) {
                if (Integer.bitCount(sub) > k) continue;
                int newMask = (cur.side == 0) ? (cur.mask ^ sub) : (cur.mask | sub);
                int newSide = cur.side ^ 1;
                int newStage = (cur.stage + 1) % m;
                double cost = maxTime[sub] * mul[cur.stage];
                double nd = cur.d + cost;
                if (nd < dist[newMask][newStage][newSide]) {
                    dist[newMask][newStage][newSide] = nd;
                    pq.offer(new Node(newMask, newStage, newSide, nd));
                }
            }
        }

        return -1.0;
    }

    private static class Node {
        int mask;
        int stage;
        int side;
        double d;
        Node(int mask, int stage, int side, double d) {
            this.mask = mask;
            this.stage = stage;
            this.side = side;
            this.d = d;
        }
    }
}
```

## Python

```python
class Solution(object):
    def minTime(self, n, k, m, time, mul):
        """
        :type n: int
        :type k: int
        :type m: int
        :type time: List[int]
        :type mul: List[float]
        :rtype: float
        """
        from heapq import heappush, heappop

        full_mask = (1 << n) - 1
        INF = float('inf')
        # dist[pos][mask][stage] where pos 0=left,1=right
        dist = [[[INF] * m for _ in range(1 << n)] for __ in range(2)]
        start_stage = 0
        dist[0][full_mask][start_stage] = 0.0
        heap = [(0.0, 0, full_mask, start_stage)]  # (cost, pos, mask, stage)

        # precompute popcounts for speed
        popcnt = [bin(i).count('1') for i in range(1 << n)]

        while heap:
            d, pos, mask, stage = heappop(heap)
            if d != dist[pos][mask][stage]:
                continue
            # goal: all on right and boat at right side
            if mask == 0 and pos == 1:
                return d
            next_stage = (stage + 1) % m
            if pos == 0:
                # move from left to right, choose subset of people in mask
                sub = mask
                while sub:
                    if popcnt[sub] <= k:
                        max_time = 0
                        i = sub
                        idx = 0
                        while i:
                            lsb = i & -i
                            person = (lsb.bit_length() - 1)
                            if time[person] > max_time:
                                max_time = time[person]
                            i ^= lsb
                        nd = d + max_time * mul[stage]
                        nmask = mask ^ sub
                        if nd < dist[1][nmask][next_stage]:
                            dist[1][nmask][next_stage] = nd
                            heappush(heap, (nd, 1, nmask, next_stage))
                    sub = (sub - 1) & mask
            else:
                # move from right to left, choose subset of people not in mask
                avail = full_mask ^ mask
                sub = avail
                while sub:
                    if popcnt[sub] <= k:
                        max_time = 0
                        i = sub
                        while i:
                            lsb = i & -i
                            person = (lsb.bit_length() - 1)
                            if time[person] > max_time:
                                max_time = time[person]
                            i ^= lsb
                        nd = d + max_time * mul[stage]
                        nmask = mask | sub
                        if nd < dist[0][nmask][next_stage]:
                            dist[0][nmask][next_stage] = nd
                            heappush(heap, (nd, 0, nmask, next_stage))
                    sub = (sub - 1) & avail

        return -1.0
```

## Python3

```python
import heapq
from typing import List

class Solution:
    def minTime(self, n: int, k: int, m: int, time: List[int], mul: List[float]) -> float:
        full = (1 << n) - 1
        # precompute max time for each subset
        max_time = [0] * (1 << n)
        for mask in range(1, 1 << n):
            lsb = mask & -mask
            i = (lsb.bit_length() - 1)
            prev = mask ^ lsb
            max_time[mask] = max(max_time[prev], time[i])

        INF = float('inf')
        # dist[mask][side][stage]
        dist = [[[INF] * m for _ in range(2)] for _ in range(1 << n)]
        start_mask = full
        dist[start_mask][0][0] = 0.0
        heap = [(0.0, start_mask, 0, 0)]  # (cost, mask, side, stage)

        while heap:
            d, mask, side, stage = heapq.heappop(heap)
            if d != dist[mask][side][stage]:
                continue
            if mask == 0 and side == 1:
                return d
            next_stage = (stage + 1) % m
            if side == 0:  # boat at left, move people from left to right
                available = mask
            else:          # boat at right, move people back to left
                available = full ^ mask

            sub = available
            while sub:
                cnt = sub.bit_count()
                if cnt <= k:
                    cost = max_time[sub] * mul[stage]
                    new_mask = mask ^ sub
                    new_side = 1 - side
                    nd = d + cost
                    if nd < dist[new_mask][new_side][next_stage]:
                        dist[new_mask][new_side][next_stage] = nd
                        heapq.heappush(heap, (nd, new_mask, new_side, next_stage))
                sub = (sub - 1) & available

        return -1.0
```

## C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <float.h>

typedef struct {
    double dist;
    int mask;
    int stage;
    int loc; //0 base,1 dest
} Node;

typedef struct {
    Node *data;
    int size;
    int capacity;
} MinHeap;

static void heapSwap(Node *a, Node *b){
    Node tmp=*a; *a=*b; *b=tmp;
}
static MinHeap* heapCreate(int cap){
    MinHeap *h = (MinHeap*)malloc(sizeof(MinHeap));
    h->data = (Node*)malloc(sizeof(Node)*(cap+1));
    h->size = 0;
    h->capacity = cap;
    return h;
}
static void heapPush(MinHeap *h, Node nd){
    if(h->size+1 > h->capacity){
        h->capacity *=2;
        h->data = (Node*)realloc(h->data, sizeof(Node)*(h->capacity+1));
    }
    int i=++h->size;
    while(i>1 && nd.dist < h->data[i/2].dist){
        h->data[i]=h->data[i/2];
        i/=2;
    }
    h->data[i]=nd;
}
static Node heapPop(MinHeap *h){
    Node ret = h->data[1];
    Node last = h->data[h->size--];
    int i=1, child;
    while((child=i*2) <= h->size){
        if(child+1<=h->size && h->data[child+1].dist < h->data[child].dist)
            child++;
        if(last.dist <= h->data[child].dist) break;
        h->data[i]=h->data[child];
        i=child;
    }
    h->data[i]=last;
    return ret;
}
static int heapEmpty(MinHeap *h){return h->size==0;}

double minTime(int n, int k, int m, int* timeArr, int timeSize, double* mul, int mulSize){
    int fullMask = (1<<n)-1;
    int maxStates = (fullMask+1)*m*2;
    const double INF = DBL_MAX/4;

    // precompute max time for each subset and popcount
    int totalSub = 1<<n;
    double *maxTime = (double*)malloc(sizeof(double)*totalSub);
    int *popcnt = (int*)malloc(sizeof(int)*totalSub);
    maxTime[0]=0; popcnt[0]=0;
    for(int mask=1; mask<totalSub; ++mask){
        int lsb = __builtin_ctz(mask);
        int prev = mask ^ (1<<lsb);
        double t = timeArr[lsb];
        maxTime[mask] = t > maxTime[prev] ? t : maxTime[prev];
        popcnt[mask] = popcnt[prev]+1;
    }

    // distance array
    double *dist = (double*)malloc(sizeof(double)*maxStates);
    for(int i=0;i<maxStates;++i) dist[i]=INF;

    auto idx = [&](int mask,int stage,int loc)->int{
        return ((mask*m)+stage)*2 + loc;
    };

    MinHeap *pq = heapCreate(1024);
    Node start={0.0,0,0,0};
    int startIdx=idx(0,0,0);
    dist[startIdx]=0.0;
    heapPush(pq,start);

    while(!heapEmpty(pq)){
        Node cur = heapPop(pq);
        int curIdx = idx(cur.mask,cur.stage,cur.loc);
        if(cur.dist != dist[curIdx]) continue; // outdated
        if(cur.mask==fullMask && cur.loc==1){
            double ans=cur.dist;
            free(maxTime); free(popcnt); free(dist);
            return ans;
        }
        int nextStage = (cur.stage+1)%m;
        if(cur.loc==0){ // boat at base, forward
            int remain = fullMask ^ cur.mask;
            for(int sub=remain; sub; sub = (sub-1)&remain){
                if(popcnt[sub]>k) continue;
                double w = maxTime[sub] * mul[cur.stage];
                int nmask = cur.mask | sub;
                int nidx = idx(nmask,nextStage,1);
                double ndist = cur.dist + w;
                if(ndist < dist[nidx]){
                    dist[nidx]=ndist;
                    heapPush(pq,(Node){ndist,nmask,nextStage,1});
                }
            }
        }else{ // loc==1 boat at destination, backward
            int have = cur.mask;
            for(int sub=have; sub; sub = (sub-1)&have){
                if(popcnt[sub]>k) continue;
                double w = maxTime[sub] * mul[cur.stage];
                int nmask = cur.mask ^ sub;
                int nidx = idx(nmask,nextStage,0);
                double ndist = cur.dist + w;
                if(ndist < dist[nidx]){
                    dist[nidx]=ndist;
                    heapPush(pq,(Node){ndist,nmask,nextStage,0});
                }
            }
        }
    }

    free(maxTime); free(popcnt); free(dist);
    return -1.0;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public double MinTime(int n, int k, int m, int[] time, double[] mul) {
        int fullMask = (1 << n) - 1;
        int totalMasks = 1 << n;
        int[] popcnt = new int[totalMasks];
        double[] maxTime = new double[totalMasks];
        for (int mask = 1; mask < totalMasks; ++mask) {
            int lsb = mask & -mask;
            int bit = BitPosition(lsb);
            int prev = mask ^ lsb;
            popcnt[mask] = popcnt[prev] + 1;
            maxTime[mask] = Math.Max(maxTime[prev], time[bit]);
        }

        double[,,] dist = new double[totalMasks, 2, m];
        for (int i = 0; i < totalMasks; ++i)
            for (int s = 0; s < 2; ++s)
                for (int st = 0; st < m; ++st)
                    dist[i, s, st] = double.PositiveInfinity;

        var pq = new PriorityQueue<State, double>();
        dist[fullMask, 0, 0] = 0.0;
        pq.Enqueue(new State(fullMask, 0, 0), 0.0);

        while (pq.Count > 0) {
            var cur = pq.Dequeue();
            double d = cur.Dist;
            if (d != dist[cur.Mask, cur.Side, cur.Stage]) continue;

            if (cur.Mask == 0 && cur.Side == 1) return d;

            int available = cur.Side == 0 ? cur.Mask : (fullMask ^ cur.Mask);
            for (int sub = available; sub > 0; sub = (sub - 1) & available) {
                if (popcnt[sub] > k) continue;
                int newMask = cur.Side == 0 ? (cur.Mask ^ sub) : (cur.Mask | sub);
                int newSide = 1 - cur.Side;
                int newStage = (cur.Stage + 1) % m;
                double nd = d + maxTime[sub] * mul[cur.Stage];
                if (nd < dist[newMask, newSide, newStage]) {
                    dist[newMask, newSide, newStage] = nd;
                    pq.Enqueue(new State(newMask, newSide, newStage, nd), nd);
                }
            }
        }

        return -1.0;
    }

    private int BitPosition(int bit) {
        // returns zero-based index of the single set bit
        int pos = 0;
        while ((bit >>= 1) != 0) pos++;
        return pos;
    }

    private struct State {
        public int Mask;
        public int Side;   // 0: boat at base, 1: boat at destination
        public int Stage;
        public double Dist;

        public State(int mask, int side, int stage) {
            Mask = mask;
            Side = side;
            Stage = stage;
            Dist = 0.0;
        }

        public State(int mask, int side, int stage, double dist) {
            Mask = mask;
            Side = side;
            Stage = stage;
            Dist = dist;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @param {number} m
 * @param {number[]} time
 * @param {number[]} mul
 * @return {number}
 */
var minTime = function(n, k, m, time, mul) {
    const totalMask = (1 << n) - 1;
    const subsetCount = 1 << n;

    // precompute max time and popcount for every subset
    const maxTimeArr = new Float64Array(subsetCount);
    const popcnt = new Uint8Array(subsetCount);
    for (let s = 1; s < subsetCount; ++s) {
        let maxT = 0;
        let cnt = 0;
        for (let i = 0; i < n; ++i) {
            if ((s >> i) & 1) {
                cnt++;
                const t = time[i];
                if (t > maxT) maxT = t;
            }
        }
        maxTimeArr[s] = maxT;
        popcnt[s] = cnt;
    }

    // Dijkstra over states (mask, side, stage)
    const stateCount = subsetCount * 2 * m;
    const dist = new Float64Array(stateCount);
    for (let i = 0; i < stateCount; ++i) dist[i] = Infinity;

    const encode = (mask, side, stage) => ((mask * 2 + side) * m) + stage;

    const startId = encode(totalMask, 0, 0);
    dist[startId] = 0;

    class MinHeap {
        constructor() { this.heap = []; }
        push(node) {
            const h = this.heap;
            h.push(node);
            let i = h.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (h[p][0] <= h[i][0]) break;
                [h[p], h[i]] = [h[i], h[p]];
                i = p;
            }
        }
        pop() {
            const h = this.heap;
            if (h.length === 0) return null;
            const top = h[0];
            const last = h.pop();
            if (h.length > 0) {
                h[0] = last;
                this._down(0);
            }
            return top;
        }
        _down(i) {
            const h = this.heap;
            const n = h.length;
            while (true) {
                let l = i * 2 + 1, r = l + 1, smallest = i;
                if (l < n && h[l][0] < h[smallest][0]) smallest = l;
                if (r < n && h[r][0] < h[smallest][0]) smallest = r;
                if (smallest === i) break;
                [h[i], h[smallest]] = [h[smallest], h[i]];
                i = smallest;
            }
        }
        isEmpty() { return this.heap.length === 0; }
    }

    const heap = new MinHeap();
    heap.push([0, startId]);

    while (!heap.isEmpty()) {
        const [d, id] = heap.pop();
        if (d !== dist[id]) continue;

        const stage = id % m;
        const tmp = Math.floor(id / m);
        const side = tmp % 2; // 0 left, 1 right
        const mask = Math.floor(tmp / 2);

        if (mask === 0) return d; // all transported

        if (side === 0) { // boat on left, move people to right
            let avail = mask;
            for (let sub = avail; sub > 0; sub = (sub - 1) & avail) {
                if (popcnt[sub] > k) continue;
                const newMask = mask ^ sub;
                const cost = maxTimeArr[sub] * mul[stage];
                const nd = d + cost;
                const nid = encode(newMask, 1, (stage + 1) % m);
                if (nd < dist[nid]) {
                    dist[nid] = nd;
                    heap.push([nd, nid]);
                }
            }
        } else { // boat on right, bring people back to left
            const rightMask = totalMask ^ mask;
            for (let sub = rightMask; sub > 0; sub = (sub - 1) & rightMask) {
                if (popcnt[sub] > k) continue;
                const newMask = mask | sub;
                const cost = maxTimeArr[sub] * mul[stage];
                const nd = d + cost;
                const nid = encode(newMask, 0, (stage + 1) % m);
                if (nd < dist[nid]) {
                    dist[nid] = nd;
                    heap.push([nd, nid]);
                }
            }
        }
    }

    return -1;
};
```

## Typescript

```typescript
function minTime(n: number, k: number, m: number, time: number[], mul: number[]): number {
    const fullMask = (1 << n) - 1;
    const subsetSize = new Uint8Array(1 << n);
    const subsetMax = new Float64Array(1 << n);
    for (let mask = 1; mask <= fullMask; ++mask) {
        let lsb = mask & -mask;
        const prev = mask ^ lsb;
        const idx = Math.log2(lsb) | 0;
        subsetSize[mask] = subsetSize[prev] + 1;
        subsetMax[mask] = Math.max(subsetMax[prev], time[idx]);
    }

    // distance[mask][stage]
    const dist: number[][] = Array.from({ length: fullMask + 1 }, () => new Float64Array(m).fill(Infinity));
    dist[fullMask][0] = 0;

    class MinHeap {
        heap: [number, number, number][] = [];
        push(item: [number, number, number]) {
            this.heap.push(item);
            this.bubbleUp(this.heap.length - 1);
        }
        bubbleUp(i: number) {
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (this.heap[p][0] <= this.heap[i][0]) break;
                [this.heap[p], this.heap[i]] = [this.heap[i], this.heap[p]];
                i = p;
            }
        }
        pop(): [number, number, number] | undefined {
            if (!this.heap.length) return undefined;
            const top = this.heap[0];
            const end = this.heap.pop()!;
            if (this.heap.length) {
                this.heap[0] = end;
                this.sink(0);
            }
            return top;
        }
        sink(i: number) {
            const n = this.heap.length;
            while (true) {
                let left = i * 2 + 1;
                let right = left + 1;
                let smallest = i;
                if (left < n && this.heap[left][0] < this.heap[smallest][0]) smallest = left;
                if (right < n && this.heap[right][0] < this.heap[smallest][0]) smallest = right;
                if (smallest === i) break;
                [this.heap[i], this.heap[smallest]] = [this.heap[smallest], this.heap[i]];
                i = smallest;
            }
        }
        isEmpty(): boolean {
            return this.heap.length === 0;
        }
    }

    const pq = new MinHeap();
    pq.push([0, fullMask, 0]);

    while (!pq.isEmpty()) {
        const cur = pq.pop()!;
        const d = cur[0];
        const mask = cur[1];
        const stage = cur[2];
        if (d > dist[mask][stage]) continue;
        if (mask === 0) return d;

        // move from left to right
        let sub = mask;
        while (sub) {
            if (subsetSize[sub] <= k) {
                const newMask = mask ^ sub;
                const nd = d + subsetMax[sub] * mul[stage];
                const nextStage = (stage + 1) % m;
                if (nd < dist[newMask][nextStage]) {
                    dist[newMask][nextStage] = nd;
                    pq.push([nd, newMask, nextStage]);
                }
            }
            sub = (sub - 1) & mask;
        }

        // move from right to left
        const rightMask = fullMask ^ mask;
        let subR = rightMask;
        while (subR) {
            if (subsetSize[subR] <= k) {
                const newMask = mask | subR;
                const nd = d + subsetMax[subR] * mul[stage];
                const nextStage = (stage + 1) % m;
                if (nd < dist[newMask][nextStage]) {
                    dist[newMask][nextStage] = nd;
                    pq.push([nd, newMask, nextStage]);
                }
            }
            subR = (subR - 1) & rightMask;
        }
    }

    return -1;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @param Integer $k
     * @param Integer $m
     * @param Integer[] $time
     * @param Float[] $mul
     * @return Float
     */
    function minTime($n, $k, $m, $time, $mul) {
        $fullMask = (1 << $n) - 1;
        $maxMask = 1 << $n;

        // precompute max time and popcount for each subset
        $maxTime = array_fill(0, $maxMask, 0);
        $popcnt   = array_fill(0, $maxMask, 0);
        for ($mask = 1; $mask < $maxMask; $mask++) {
            $mx = 0;
            $cnt = 0;
            for ($i = 0; $i < $n; $i++) {
                if ($mask & (1 << $i)) {
                    $cnt++;
                    if ($time[$i] > $mx) $mx = $time[$i];
                }
            }
            $maxTime[$mask] = $mx;
            $popcnt[$mask]   = $cnt;
        }

        // distances: dist[mask][stage] (boat is on the side of people in mask)
        $INF = INF;
        $dist = array_fill(0, $maxMask, null);
        for ($i = 0; $i < $maxMask; $i++) {
            $dist[$i] = array_fill(0, $m, $INF);
        }
        $dist[$fullMask][0] = 0.0;

        $pq = new SplPriorityQueue();
        // SplPriorityQueue extracts highest priority, use negative distance for min-heap
        $pq->setExtractFlags(SplPriorityQueue::EXTR_BOTH);
        $pq->insert([$fullMask, 0], -0.0);

        while (!$pq->isEmpty()) {
            $elem = $pq->extract();
            [$mask, $stage] = $elem['data'];
            $curDist = -$elem['priority'];

            if ($curDist > $dist[$mask][$stage] + 1e-12) continue;

            // goal: all people are on the opposite side (mask == 0)
            if ($mask === 0) {
                return $curDist;
            }

            // people currently with the boat
            $avail = $mask; // can move these to the other side
            // also we can move people from the opposite side back to this side
            $opp   = $fullMask ^ $mask;

            // forward moves (take subset from avail)
            for ($sub = $avail; $sub > 0; $sub = ($sub - 1) & $avail) {
                if ($popcnt[$sub] > $k) continue;
                $newMask = $mask ^ $sub; // those people leave the boat side
                $nextStage = ($stage + 1) % $m;
                $cost = $maxTime[$sub] * $mul[$stage];
                $newDist = $curDist + $cost;
                if ($newDist + 1e-12 < $dist[$newMask][$nextStage]) {
                    $dist[$newMask][$nextStage] = $newDist;
                    $pq->insert([$newMask, $nextStage], -$newDist);
                }
            }

            // backward moves (bring subset from opposite side)
            for ($sub = $opp; $sub > 0; $sub = ($sub - 1) & $opp) {
                if ($popcnt[$sub] > $k) continue;
                $newMask = $mask ^ $sub; // those people join the boat side
                $nextStage = ($stage + 1) % $m;
                $cost = $maxTime[$sub] * $mul[$stage];
                $newDist = $curDist + $cost;
                if ($newDist + 1e-12 < $dist[$newMask][$nextStage]) {
                    $dist[$newMask][$nextStage] = $newDist;
                    $pq->insert([$newMask, $nextStage], -$newDist);
                }
            }
        }

        return -1.0;
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    func minTime(_ n: Int, _ k: Int, _ m: Int, _ time: [Int], _ mul: [Double]) -> Double {
        let fullMask = (1 << n) - 1
        // Precompute max time for each subset
        var maxTime = [Double](repeating: 0.0, count: 1 << n)
        if n > 0 {
            for mask in 1..<(1 << n) {
                var mx = 0
                var temp = mask
                var idx = 0
                while temp != 0 {
                    if (temp & 1) == 1 {
                        mx = max(mx, time[idx])
                    }
                    idx += 1
                    temp >>= 1
                }
                maxTime[mask] = Double(mx)
            }
        }
        
        let totalStates = (1 << n) * 2 * m
        var dist = [Double](repeating: Double.greatestFiniteMagnitude, count: totalStates)
        
        func stateIndex(mask: Int, side: Int, stage: Int) -> Int {
            return ((mask << 1) | side) * m + stage
        }
        
        struct HeapNode {
            var dist: Double
            var idx: Int
        }
        
        struct MinHeap {
            private var heap: [HeapNode] = []
            
            mutating func push(_ node: HeapNode) {
                heap.append(node)
                siftUp(heap.count - 1)
            }
            
            mutating func pop() -> HeapNode? {
                guard !heap.isEmpty else { return nil }
                let top = heap[0]
                heap[0] = heap[heap.count - 1]
                heap.removeLast()
                siftDown(0)
                return top
            }
            
            var isEmpty: Bool { heap.isEmpty }
            
            private mutating func siftUp(_ index: Int) {
                var child = index
                while child > 0 {
                    let parent = (child - 1) >> 1
                    if heap[child].dist < heap[parent].dist {
                        heap.swapAt(child, parent)
                        child = parent
                    } else { break }
                }
            }
            
            private mutating func siftDown(_ index: Int) {
                var parent = index
                while true {
                    let left = parent * 2 + 1
                    let right = left + 1
                    var smallest = parent
                    if left < heap.count && heap[left].dist < heap[smallest].dist {
                        smallest = left
                    }
                    if right < heap.count && heap[right].dist < heap[smallest].dist {
                        smallest = right
                    }
                    if smallest == parent { break }
                    heap.swapAt(parent, smallest)
                    parent = smallest
                }
            }
        }
        
        var heap = MinHeap()
        let startIdx = stateIndex(mask: fullMask, side: 0, stage: 0)
        dist[startIdx] = 0.0
        heap.push(HeapNode(dist: 0.0, idx: startIdx))
        
        while let node = heap.pop() {
            let curDist = node.dist
            let idx = node.idx
            if curDist > dist[idx] + 1e-12 { continue }
            
            // decode state
            let stage = idx % m
            let side = (idx / m) & 1
            let mask = idx / (m * 2)
            
            if mask == 0 && side == 1 {
                return curDist
            }
            
            let available: Int = (side == 0) ? mask : (fullMask ^ mask)
            var sub = available
            while sub > 0 {
                if sub.nonzeroBitCount <= k {
                    let newMask = (side == 0) ? (mask ^ sub) : (mask | sub)
                    let newSide = 1 - side
                    let cost = maxTime[sub] * mul[stage]
                    let ndist = curDist + cost
                    let nStage = (stage + 1) % m
                    let nIdx = stateIndex(mask: newMask, side: newSide, stage: nStage)
                    if ndist + 1e-12 < dist[nIdx] {
                        dist[nIdx] = ndist
                        heap.push(HeapNode(dist: ndist, idx: nIdx))
                    }
                }
                sub = (sub - 1) & available
            }
        }
        
        return -1.0
    }
}
```

## Kotlin

```kotlin
import java.util.PriorityQueue
import kotlin.math.max

class Solution {
    fun minTime(n: Int, k: Int, m: Int, time: IntArray, mul: DoubleArray): Double {
        val fullMask = (1 shl n) - 1
        val INF = Double.POSITIVE_INFINITY

        // precompute max time for each subset
        val maxTime = DoubleArray(1 shl n)
        for (mask in 0 until (1 shl n)) {
            var mx = 0.0
            var bits = mask
            while (bits != 0) {
                val lsb = bits and -bits
                val idx = Integer.numberOfTrailingZeros(lsb)
                mx = max(mx, time[idx].toDouble())
                bits -= lsb
            }
            maxTime[mask] = mx
        }

        // precompute subsets with size between 1 and k for every possible mask
        val subsets = Array(1 shl n) { mutableListOf<Int>() }
        for (mask in 0 until (1 shl n)) {
            var sub = mask
            while (sub != 0) {
                if (Integer.bitCount(sub) <= k) {
                    subsets[mask].add(sub)
                }
                sub = (sub - 1) and mask
            }
        }

        // distance array: [mask][side][stage]
        val dist = Array(1 shl n) { Array(2) { DoubleArray(m) { INF } } }
        val pq = PriorityQueue(compareBy<Pair<State, Double>> { it.second })
        data class State(val mask: Int, val side: Int, val stage: Int)

        dist[fullMask][0][0] = 0.0
        pq.add(State(fullMask, 0, 0) to 0.0)

        while (pq.isNotEmpty()) {
            val (state, curCost) = pq.poll()
            if (curCost > dist[state.mask][state.side][state.stage]) continue

            // goal: all on right and boat on right side
            if (state.mask == 0 && state.side == 1) return curCost

            val available = if (state.side == 0) state.mask else fullMask xor state.mask
            if (available == 0) continue  // no possible move

            for (sub in subsets[available]) {
                val newMask = if (state.side == 0) state.mask xor sub else state.mask or sub
                val newSide = 1 - state.side
                val newStage = (state.stage + 1) % m
                val cost = maxTime[sub] * mul[state.stage]
                val newCost = curCost + cost
                if (newCost < dist[newMask][newSide][newStage]) {
                    dist[newMask][newSide][newStage] = newCost
                    pq.add(State(newMask, newSide, newStage) to newCost)
                }
            }
        }

        return -1.0
    }
}
```

## Dart

```dart
class Solution {
  double minTime(int n, int k, int m, List<int> time, List<double> mul) {
    int totalMask = 1 << n;
    // Precompute max time and popcount for each subset
    List<double> maxTime = List.filled(totalMask, 0.0);
    List<int> popcnt = List.filled(totalMask, 0);
    for (int s = 1; s < totalMask; ++s) {
      int lsb = s & -s;
      int bit = (lsb).bitLength - 1;
      int prev = s ^ lsb;
      maxTime[s] = max(maxTime[prev], time[bit].toDouble());
      popcnt[s] = popcnt[prev] + 1;
    }

    // distances: mask x side(0 source,1 dest) x stage
    List<List<List<double>>> dist = List.generate(
        totalMask,
        (_) => List.generate(2, (_) => List.filled(m, double.infinity)));

    int startMask = totalMask - 1;
    dist[startMask][0][0] = 0.0;

    // Min-heap priority queue
    var heap = _MinHeap();
    heap.push(_Node(0.0, startMask, 0, 0));

    while (!heap.isEmpty) {
      var cur = heap.pop();
      double d = cur.d;
      int mask = cur.mask;
      int side = cur.side;
      int stage = cur.stage;

      if (d > dist[mask][side][stage] + 1e-12) continue;
      if (mask == 0) return d; // all transported

      int available;
      if (side == 0) {
        // boat at source, can take people from mask
        available = mask;
      } else {
        // boat at destination, can take people not in mask
        available = ((totalMask - 1) ^ mask);
      }

      for (int sub = available; sub > 0; sub = (sub - 1) & available) {
        if (popcnt[sub] > k) continue;
        double cost = maxTime[sub] * mul[stage];
        int newMask = side == 0 ? (mask ^ sub) : (mask | sub);
        int newSide = 1 - side;
        int newStage = (stage + 1) % m;
        double nd = d + cost;
        if (nd + 1e-12 < dist[newMask][newSide][newStage]) {
          dist[newMask][newSide][newStage] = nd;
          heap.push(_Node(nd, newMask, newSide, newStage));
        }
      }
    }

    return -1.0;
  }
}

class _Node {
  double d;
  int mask;
  int side;
  int stage;
  _Node(this.d, this.mask, this.side, this.stage);
}

class _MinHeap {
  final List<_Node> _heap = [];

  bool get isEmpty => _heap.isEmpty;

  void push(_Node node) {
    _heap.add(node);
    _siftUp(_heap.length - 1);
  }

  _Node pop() {
    var res = _heap[0];
    var last = _heap.removeLast();
    if (_heap.isNotEmpty) {
      _heap[0] = last;
      _siftDown(0);
    }
    return res;
  }

  void _siftUp(int i) {
    while (i > 0) {
      int p = (i - 1) >> 1;
      if (_heap[p].d <= _heap[i].d) break;
      var tmp = _heap[p];
      _heap[p] = _heap[i];
      _heap[i] = tmp;
      i = p;
    }
  }

  void _siftDown(int i) {
    int n = _heap.length;
    while (true) {
      int l = i * 2 + 1;
      int r = l + 1;
      int smallest = i;
      if (l < n && _heap[l].d < _heap[smallest].d) smallest = l;
      if (r < n && _heap[r].d < _heap[smallest].d) smallest = r;
      if (smallest == i) break;
      var tmp = _heap[i];
      _heap[i] = _heap[smallest];
      _heap[smallest] = tmp;
      i = smallest;
    }
  }
}
```

## Golang

```go
package main

import (
	"container/heap"
	"math"
)

type state struct {
	cost  float64
	mask  int
	stage int
	idx   int
}

type priorityQueue []*state

func (pq priorityQueue) Len() int { return len(pq) }
func (pq priorityQueue) Less(i, j int) bool {
	return pq[i].cost < pq[j].cost
}
func (pq priorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].idx = i
	pq[j].idx = j
}
func (pq *priorityQueue) Push(x interface{}) {
	it := x.(*state)
	it.idx = len(*pq)
	*pq = append(*pq, it)
}
func (pq *priorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	it := old[n-1]
	*pq = old[0 : n-1]
	return it
}

func minTime(n int, k int, m int, timeArr []int, mul []float64) float64 {
	fullMask := (1 << n) - 1

	// precompute max time for each subset mask
	maxTime := make([]int, fullMask+1)
	for mask := 1; mask <= fullMask; mask++ {
		lsb := mask & -mask
		prev := mask ^ lsb
		idx := 0
		for (1 << idx) != lsb {
			idx++
		}
		if timeArr[idx] > maxTime[prev] {
			maxTime[mask] = timeArr[idx]
		} else {
			maxTime[mask] = maxTime[prev]
		}
	}

	const INF = math.MaxFloat64
	dist := make([][]float64, fullMask+1)
	for i := 0; i <= fullMask; i++ {
		dist[i] = make([]float64, m)
		for j := 0; j < m; j++ {
			dist[i][j] = INF
		}
	}

	pq := &priorityQueue{}
	heap.Init(pq)

	startMask := fullMask
	dist[startMask][0] = 0.0
	heap.Push(pq, &state{cost: 0.0, mask: startMask, stage: 0})

	for pq.Len() > 0 {
		cur := heap.Pop(pq).(*state)
		cost := cur.cost
		mask := cur.mask
		stage := cur.stage

		if cost > dist[mask][stage] {
			continue
		}
		if mask == 0 {
			return cost
		}

		nextStage := (stage + 1) % m
		mulVal := mul[stage]

		// subsets from people left (mask)
		for sub := mask; sub > 0; sub = (sub - 1) & mask {
			if bitsOnes(sub) > k {
				continue
			}
			newMask := mask ^ sub
			newCost := cost + float64(maxTime[sub])*mulVal
			if newCost < dist[newMask][nextStage] {
				dist[newMask][nextStage] = newCost
				heap.Push(pq, &state{cost: newCost, mask: newMask, stage: nextStage})
			}
		}

		// subsets from people already crossed (complement)
		comp := fullMask ^ mask
		for sub := comp; sub > 0; sub = (sub - 1) & comp {
			if bitsOnes(sub) > k {
				continue
			}
			newMask := mask ^ sub // add them back to left side
			newCost := cost + float64(maxTime[sub])*mulVal
			if newCost < dist[newMask][nextStage] {
				dist[newMask][nextStage] = newCost
				heap.Push(pq, &state{cost: newCost, mask: newMask, stage: nextStage})
			}
		}
	}

	return -1.0
}

// helper to count set bits (popcount)
func bitsOnes(x int) int {
	count := 0
	for x != 0 {
		x &= x - 1
		count++
	}
	return count
}
```

## Ruby

```ruby
def min_time(n, k, m, time, mul)
  full_mask = (1 << n) - 1
  max_time = Array.new(1 << n, 0)
  popcnt = Array.new(1 << n, 0)

  (1..full_mask).each do |s|
    lsb = s & -s
    idx = lsb.bit_length - 1
    prev = s ^ lsb
    popcnt[s] = popcnt[prev] + 1
    max_time[s] = [max_time[prev], time[idx]].max
  end

  # dist[mask][stage][side]
  dist = Array.new(1 << n) { Array.new(m) { [Float::INFINITY, Float::INFINITY] } }
  start_mask = full_mask
  dist[start_mask][0][0] = 0.0

  # simple binary min-heap
  class MinHeap
    def initialize
      @data = []
    end

    def push(item)
      @data << item
      i = @data.size - 1
      while i > 0
        p = (i - 1) / 2
        break if @data[p][0] <= @data[i][0]
        @data[p], @data[i] = @data[i], @data[p]
        i = p
      end
    end

    def pop
      return nil if @data.empty?
      top = @data[0]
      last = @data.pop
      unless @data.empty?
        @data[0] = last
        i = 0
        n = @data.size
        loop do
          l = i * 2 + 1
          r = l + 1
          smallest = i
          smallest = l if l < n && @data[l][0] < @data[smallest][0]
          smallest = r if r < n && @data[r][0] < @data[smallest][0]
          break if smallest == i
          @data[i], @data[smallest] = @data[smallest], @data[i]
          i = smallest
        end
      end
      top
    end

    def empty?
      @data.empty?
    end
  end

  heap = MinHeap.new
  heap.push([0.0, start_mask, 0, 0]) # dist, mask, stage, side (0:left,1:right)

  while !heap.empty?
    cur_dist, mask, stage, side = heap.pop
    next if cur_dist > dist[mask][stage][side]

    # goal: all transferred and boat on right side
    if mask == 0 && side == 1
      return cur_dist
    end

    available = side == 0 ? mask : (full_mask ^ mask)
    sub = available
    while sub > 0
      if popcnt[sub] <= k
        new_mask = side == 0 ? (mask ^ sub) : (mask | sub)
        new_stage = (stage + 1) % m
        new_side = 1 - side
        cost = mul[stage] * max_time[sub]
        ndist = cur_dist + cost
        if ndist < dist[new_mask][new_stage][new_side]
          dist[new_mask][new_stage][new_side] = ndist
          heap.push([ndist, new_mask, new_stage, new_side])
        end
      end
      sub = (sub - 1) & available
    end
  end

  -1.0
end
```

## Scala

```scala
import java.util.PriorityQueue

object Solution {
  def minTime(n: Int, k: Int, m: Int, time: Array[Int], mul: Array[Double]): Double = {
    val fullMask = (1 << n) - 1
    val maxTime = new Array[Int](1 << n)
    for (mask <- 1 until (1 << n)) {
      val lsb = mask & -mask
      val idx = Integer.numberOfTrailingZeros(lsb)
      val prev = mask ^ lsb
      maxTime(mask) = math.max(time(idx), maxTime(prev))
    }

    val INF = Double.PositiveInfinity
    val dist = Array.ofDim[Double](1 << n, m, 2)
    for {
      i <- 0 until (1 << n)
      j <- 0 until m
      s <- 0 to 1
    } dist(i)(j)(s) = INF

    case class State(d: Double, mask: Int, stage: Int, side: Int)

    val pq = new PriorityQueue[State]((a: State, b: State) => java.lang.Double.compare(a.d, b.d))
    dist(fullMask)(0)(0) = 0.0
    pq.add(State(0.0, fullMask, 0, 0))

    while (!pq.isEmpty) {
      val cur = pq.poll()
      if (cur.d > dist(cur.mask)(cur.stage)(cur.side) + 1e-12) {
        // stale entry
      } else {
        if (cur.mask == 0 && cur.side == 1) return cur.d

        val avail = if (cur.side == 0) cur.mask else fullMask ^ cur.mask
        var sub = avail
        while (sub != 0) {
          val cnt = Integer.bitCount(sub)
          if (cnt >= 1 && cnt <= k) {
            val newMask = if (cur.side == 0) cur.mask ^ sub else cur.mask | sub
            val cost = maxTime(sub).toDouble * mul(cur.stage)
            val ndist = cur.d + cost
            val nstage = (cur.stage + 1) % m
            val nside = 1 - cur.side
            if (ndist + 1e-12 < dist(newMask)(nstage)(nside)) {
              dist(newMask)(nstage)(nside) = ndist
              pq.add(State(ndist, newMask, nstage, nside))
            }
          }
          sub = (sub - 1) & avail
        }
      }
    }

    -1.0
  }
}
```

## Rust

```rust
use std::cmp::Ordering;
use std::collections::BinaryHeap;

#[derive(Copy, Clone)]
struct State {
    cost: f64,
    mask: usize,
    side: usize,
    stage: usize,
}

impl Eq for State {}

impl PartialEq for State {
    fn eq(&self, other: &Self) -> bool {
        self.cost == other.cost
    }
}

impl Ord for State {
    fn cmp(&self, other: &Self) -> Ordering {
        // reverse order for min-heap
        other.cost.partial_cmp(&self.cost).unwrap()
    }
}

impl PartialOrd for State {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl Solution {
    pub fn min_time(n: i32, k: i32, m: i32, time: Vec<i32>, mul: Vec<f64>) -> f64 {
        let n = n as usize;
        let k = k as u32;
        let m = m as usize;
        let full_mask = (1usize << n) - 1;

        // precompute max time for each subset
        let mut max_time = vec![0i32; 1usize << n];
        for mask in 1..(1usize << n) {
            let b = mask.trailing_zeros() as usize;
            let prev = mask ^ (1usize << b);
            max_time[mask] = std::cmp::max(time[b], max_time[prev]);
        }

        // distances: mask x side(0/1) x stage
        let inf = f64::INFINITY;
        let mut dist = vec![vec![vec![inf; m]; 2]; 1usize << n];
        dist[full_mask][0][0] = 0.0;

        let mut heap = BinaryHeap::new();
        heap.push(State {
            cost: 0.0,
            mask: full_mask,
            side: 0,
            stage: 0,
        });

        while let Some(State { cost, mask, side, stage }) = heap.pop() {
            if cost > dist[mask][side][stage] + 1e-12 {
                continue;
            }
            if mask == 0 && side == 1 {
                return cost;
            }

            // people currently on the boat side
            let avail = if side == 0 { mask } else { full_mask ^ mask };
            let mut sub = avail;
            while sub > 0 {
                if sub.count_ones() <= k {
                    let next_mask = if side == 0 { mask ^ sub } else { mask | sub };
                    let next_side = 1 - side;
                    let next_stage = (stage + 1) % m;
                    let trip_cost = max_time[sub] as f64 * mul[stage];
                    let new_cost = cost + trip_cost;
                    if new_cost + 1e-12 < dist[next_mask][next_side][next_stage] {
                        dist[next_mask][next_side][next_stage] = new_cost;
                        heap.push(State {
                            cost: new_cost,
                            mask: next_mask,
                            side: next_side,
                            stage: next_stage,
                        });
                    }
                }
                sub = (sub - 1) & avail;
            }
        }

        -1.0
    }
}
```

## Racket

```racket
(define/contract (min-time n k m time mul)
  (-> exact-integer? exact-integer? exact-integer? (listof exact-integer?) (listof flonum?) flonum?)
  (let* ((full-mask (sub1 (arithmetic-shift 1 n))) ; (1<<n)-1
         (time-vec (list->vector time))
         (mul-vec (list->vector mul))
         ;; precompute max time for each subset and popcount
         (subset-count (arithmetic-shift 1 n))
         (max-time (make-vector subset-count 0.0))
         (popcnt   (make-vector subset-count 0)))
    (let loop-sub ((s 1))
      (when (< s subset-count)
        (let* ((lsb (bitwise-and s (- s))) ; lowest set bit
               (prev (bitwise-xor s lsb))
               (idx (integer-length lsb))) ; position+1
          (vector-set! max-time s
            (max (vector-ref max-time prev)
                 (exact->inexact (vector-ref time-vec (- idx 1)))))
          (vector-set! popcnt s (+ 1 (vector-ref popcnt prev)))
          (loop-sub (+ s 1)))))
    ;; Dijkstra structures
    (define total-states (* subset-count m 2))
    (define dist (make-vector total-states +inf.0))
    (define heap-ids (make-vector total-states 0))
    (define heap-dists (make-vector total-states +inf.0))
    (define heap-size 0)
    (define (heap-swap i j)
      (let ((tmp-id (vector-ref heap-ids i))
            (tmp-dist (vector-ref heap-dists i)))
        (vector-set! heap-ids i (vector-ref heap-ids j))
        (vector-set! heap-dists i (vector-ref heap-dists j))
        (vector-set! heap-ids j tmp-id)
        (vector-set! heap-dists j tmp-dist)))
    (define (heap-push id d)
      (set! heap-size (+ heap-size 1))
      (let ((i heap-size))
        (vector-set! heap-ids i id)
        (vector-set! heap-dists i d)
        ;; bubble up
        (let loop ()
          (when (> i 1)
            (let ((parent (quotient i 2)))
              (if (< (vector-ref heap-dists i) (vector-ref heap-dists parent))
                  (begin (heap-swap i parent) (set! i parent) (loop))
                  (void)))))))
    (define (heap-pop)
      (when (= heap-size 0) (error "pop from empty heap"))
      (let ((min-id (vector-ref heap-ids 1))
            (min-dist (vector-ref heap-dists 1)))
        ;; move last to root
        (vector-set! heap-ids 1 (vector-ref heap-ids heap-size))
        (vector-set! heap-dists 1 (vector-ref heap-dists heap-size))
        (set! heap-size (- heap-size 1))
        ;; bubble down
        (let loop ((i 1))
          (let* ((left (* i 2))
                 (right (+ left 1))
                 (smallest i)
                 (size heap-size))
            (when (and (<= left size)
                       (< (vector-ref heap-dists left) (vector-ref heap-dists smallest)))
              (set! smallest left))
            (when (and (<= right size)
                       (< (vector-ref heap-dists right) (vector-ref heap-dists smallest)))
              (set! smallest right))
            (if (= smallest i)
                (void)
                (begin (heap-swap i smallest) (loop smallest)))))
        (values min-id min-dist)))
    ;; encode/decode helpers
    (define (encode mask stage side)
      (+ (* (+ (* mask m) stage) 2) side))
    (define (decode id)
      (let* ((side (remainder id 2))
             (tmp (quotient id 2))
             (stage (remainder tmp m))
             (mask (quotient tmp m)))
        (values mask stage side)))
    ;; initial state
    (let* ((start-id (encode full-mask 0 0)))
      (vector-set! dist start-id 0.0)
      (heap-push start-id 0.0)
      (let loop ()
        (if (= heap-size 0)
            -1.0
            (call-with-values
                (lambda () (heap-pop))
              (lambda (cur-id cur-d)
                (when (< cur-d (vector-ref dist cur-id))
                  (vector-set! dist cur-id cur-d)) ; stale entry skip later
                (call-with-values
                    (lambda () (decode cur-id))
                  (lambda (mask stage side)
                    (if (and (= mask 0) (= side 1))
                        cur-d
                        (begin
                          (let ((available (if (= side 0)
                                               mask
                                               (bitwise-xor full-mask mask))))
                            (let subloop ((sub available))
                              (when (> sub 0)
                                (when (<= (vector-ref popcnt sub) k)
                                  (let* ((new-mask (if (= side 0)
                                                       (bitwise-and mask (bitwise-not sub))
                                                       (bitwise-ior mask sub)))
                                         (next-stage (remainder (+ stage 1) m))
                                         (next-side (if (= side 0) 1 0))
                                         (cost (* (vector-ref max-time sub)
                                                  (vector-ref mul-vec stage)))
                                         (new-dist (+ cur-d cost))
                                         (nid (encode new-mask next-stage next-side)))
                                    (when (< new-dist (vector-ref dist nid))
                                      (vector-set! dist nid new-dist)
                                      (heap-push nid new-dist))))
                                (subloop (bitwise-and (sub-1) available)))))
                          (loop))))))))))
)))
```

## Erlang

```erlang
-module(solution).
-export([min_time/5]).

-define(INF, 1.0e18).

%% Public API
-spec min_time(N :: integer(), K :: integer(), M :: integer(),
               Time :: [integer()], Mul :: [float()]) -> float().
min_time(N, K, M, Time, Mul) ->
    Times = list_to_tuple(Time),
    Mults = list_to_tuple(Mul),
    FullMask = (1 bsl N) - 1,
    StartKey = {FullMask, 0, 0},
    DistMap0 = maps:put(StartKey, 0.0, #{}),
    PQ0 = push(gb_trees:empty(), 0.0, StartKey),
    dijkstra(N, K, M, Times, Mults, FullMask, DistMap0, PQ0).

%% Dijkstra main loop
dijkstra(N, K, M, Times, Mults, FullMask, DistMap, PQ) ->
    case gb_trees:is_empty(PQ) of
        true -> -1.0;
        false ->
            {{Dist, [State|Rest]}, PQ1} = gb_trees:take_smallest(PQ),
            NewPQ = case Rest of
                        [] -> PQ1;
                        _  -> gb_trees:insert(Dist, Rest, PQ1)
                    end,
            {Mask, Stage, Side} = State,
            case maps:get({Mask, Stage, Side}, DistMap) of
                ExistingDist when ExistingDist < Dist - 1.0e-9 ->
                    dijkstra(N, K, M, Times, Mults, FullMask, DistMap, NewPQ);
                _ ->
                    if Mask =:= 0 andalso Side =:= 1 ->
                            Dist;
                       true ->
                            Available = case Side of
                                            0 -> Mask;
                                            1 -> (FullMask bxor Mask)
                                        end,
                            Subsets = subsets_up_to_k(Available, K),
                            {FinalPQ, FinalDistMap} =
                                lists:foldl(
                                    fun(Sub, {AccPQ, AccMap}) ->
                                        MaxT = max_time_sub(Sub, Times),
                                        MulVal = element(Stage + 1, Mults),
                                        Cost = MaxT * MulVal,
                                        NewMask = case Side of
                                                     0 -> Mask band bnot(Sub);
                                                     1 -> Mask bor Sub
                                                 end,
                                        NewSide = 1 - Side,
                                        NewStage = (Stage + 1) rem M,
                                        NewDist = Dist + Cost,
                                        Key = {NewMask, NewStage, NewSide},
                                        OldDist = maps:get(Key, AccMap, ?INF),
                                        if NewDist + 1.0e-9 < OldDist ->
                                                UpdatedMap = maps:put(Key, NewDist, AccMap),
                                                UpdatedPQ = push(AccPQ, NewDist, Key),
                                                {UpdatedPQ, UpdatedMap};
                                           true -> {AccPQ, AccMap}
                                        end
                                    end,
                                    {NewPQ, DistMap},
                                    Subsets),
                            dijkstra(N, K, M, Times, Mults, FullMask, FinalDistMap, FinalPQ)
                    end
            end
    end.

%% Priority queue operations using gb_trees (key = distance)
push(Tree, Dist, State) ->
    case gb_trees:lookup(Dist, Tree) of
        {value, List} -> gb_trees:update(Dist, [State|List], Tree);
        none -> gb_trees:insert(Dist, [State], Tree)
    end.

%% Generate all non‑empty subsets of Mask with popcount ≤ K
subsets_up_to_k(Mask, K) ->
    subsets_up_to_k(Mask, K, []).

subsets_up_to_k(0, _K, Acc) -> lists:reverse(Acc);
subsets_up_to_k(Mask, K, Acc) ->
    Sub = Mask,
    subsets_collect(Sub, Mask, K, Acc).

subsets_collect(0, _Mask, _K, Acc) -> Acc;
subsets_collect(Sub, Mask, K, Acc) ->
    NewAcc = if popcnt(Sub) =< K -> [Sub|Acc]; true -> Acc end,
    Next = (Sub - 1) band Mask,
    subsets_collect(Next, Mask, K, NewAcc).

%% Popcount of an integer
popcnt(0) -> 0;
popcnt(N) ->
    1 + popcnt(N band (N-1)).

%% Maximum time among people in SubMask
max_time_sub(SubMask, Times) ->
    max_time_sub(SubMask, Times, 0).

max_time_sub(0, _Times, Max) -> Max;
max_time_sub(Mask, Times, Max) ->
    Bit = Mask band -Mask,
    Index = trailing_zeros(Bit),
    TimeVal = element(Index + 1, Times),
    NewMax = if TimeVal > Max -> TimeVal; true -> Max end,
    max_time_sub(Mask bxor Bit, Times, NewMax).

%% Number of trailing zero bits (0‑based)
trailing_zeros(0) -> 0;
trailing_zeros(N) ->
    trailing_zeros(N, 0).

trailing_zeros(N, C) when N band 1 =:= 0 -> trailing_zeros(N bsr 1, C+1);
trailing_zeros(_, C) -> C.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_time(n :: integer, k :: integer, m :: integer, time :: [integer], mul :: [float]) :: float
  def min_time(_n, _k, _m, _time, _mul) do
    # This function will be overridden by the implementation below.
    0.0
  end

  def min_time(n, k, m, time, mul) do
    full_mask = (1 <<< n) - 1

    # Precompute subsets for each mask with size <= k and their max times
    subsets_by_mask =
      Enum.reduce(0..full_mask, %{}, fn mask, acc ->
        subs = generate_subsets(mask, k, time)
        Map.put(acc, mask, subs)
      end)

    # Dijkstra's algorithm over states {mask, side, stage}
    # side: 0 = boat on left, 1 = boat on right
    start_state = {full_mask, 0, 0}
    dist = %{start_state => 0.0}
    heap = :gb_sets.add({0.0, start_state}, :gb_sets.new())

    result =
      dijkstra(
        heap,
        dist,
        subsets_by_mask,
        full_mask,
        k,
        m,
        mul
      )

    case result do
      nil -> -1.0
      val -> val
    end
  end

  defp generate_subsets(mask, k, times) do
    # Enumerate all non‑empty subsets of mask with popcount <= k
    # Return list of {subset_mask, max_time_in_subset}
    do_generate_subsets(mask, mask, k, times, [])
  end

  defp do_generate_subsets(0, _orig, _k, _times, acc), do: acc

  defp do_generate_subsets(sub, orig, k, times, acc) do
    cnt = popcnt(sub)

    acc =
      if cnt <= k do
        max_t = max_time_in_mask(sub, times)
        [{sub, max_t} | acc]
      else
        acc
      end

    next = (sub - 1) &&& orig
    do_generate_subsets(next, orig, k, times, acc)
  end

  defp popcnt(x), do: popcnt(x, 0)

  defp popcnt(0, cnt), do: cnt

  defp popcnt(x, cnt) do
    popcnt(x >>> 1, cnt + (x &&& 1))
  end

  defp max_time_in_mask(mask, times), do: max_time_in_mask(mask, times, 0, 0)

  defp max_time_in_mask(0, _times, _idx, cur_max), do: cur_max

  defp max_time_in_mask(mask, times, idx, cur_max) do
    if (mask &&& 1) == 1 do
      t = Enum.at(times, idx)
      new_max = if t > cur_max, do: t, else: cur_max
      max_time_in_mask(mask >>> 1, times, idx + 1, new_max)
    else
      max_time_in_mask(mask >>> 1, times, idx + 1, cur_max)
    end
  end

  defp dijkstra(heap, dist, subsets_by_mask, full_mask, _k, m, mul) do
    case :gb_sets.is_empty(heap) do
      true ->
        nil

      false ->
        {{cur_dist, {mask, side, stage}}, heap_rest} = :gb_sets.take_smallest(heap)

        # Skip if we have already found a better distance
        if cur_dist > Map.get(dist, {mask, side, stage}, 1.0e100) do
          dijkstra(heap_rest, dist, subsets_by_mask, full_mask, _k, m, mul)
        else
          # Goal check: all people on right and boat on right (side == 1)
          if mask == 0 and side == 1 do
            cur_dist
          else
            available =
              if side == 0 do
                mask
              else
                full_mask &&& bnot(mask)
              end

            transitions = Map.get(subsets_by_mask, available, [])

            {new_heap, new_dist} =
              Enum.reduce(transitions, {heap_rest, dist}, fn {submask, max_t},
                                                            {h_acc, d_acc} ->
                next_mask =
                  if side == 0 do
                    mask &&& bnot(submask)
                  else
                    mask ||| submask
                  end

                cost = max_t * Enum.at(mul, stage)
                new_dist_val = cur_dist + cost
                next_stage = rem(stage + 1, m)
                next_side = 1 - side
                key = {next_mask, next_side, next_stage}
                prev = Map.get(d_acc, key, 1.0e100)

                if new_dist_val < prev do
                  {
                    :gb_sets.add({new_dist_val, key}, h_acc),
                    Map.put(d_acc, key, new_dist_val)
                  }
                else
                  {h_acc, d_acc}
                end
              end)

            dijkstra(new_heap, new_dist, subsets_by_mask, full_mask, _k, m, mul)
          end
        end
    end
  end
end
```
