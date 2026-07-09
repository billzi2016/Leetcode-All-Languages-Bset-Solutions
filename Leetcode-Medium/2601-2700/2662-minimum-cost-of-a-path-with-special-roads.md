# 2662. Minimum Cost of a Path With Special Roads

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minimumCost(vector<int>& start, vector<int>& target, vector<vector<int>>& specialRoads) {
        map<pair<int,int>, int> idx;
        vector<pair<int,int>> pts;
        auto add = [&](int x, int y){
            pair<int,int> p = {x,y};
            if (!idx.count(p)) {
                idx[p] = (int)pts.size();
                pts.push_back(p);
            }
        };
        add(start[0], start[1]);
        add(target[0], target[1]);
        for (auto &r : specialRoads) {
            add(r[0], r[1]);
            add(r[2], r[3]);
        }
        int n = pts.size();
        vector<vector<pair<int,long long>>> adj(n);
        // normal Manhattan edges
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                long long w = llabs((long long)pts[i].first - pts[j].first) +
                              llabs((long long)pts[i].second - pts[j].second);
                adj[i].push_back({j, w});
                adj[j].push_back({i, w});
            }
        }
        // special roads (directed)
        for (auto &r : specialRoads) {
            int u = idx[{r[0], r[1]}];
            int v = idx[{r[2], r[3]}];
            long long w = r[4];
            adj[u].push_back({v, w});
        }
        const long long INF = (1LL<<60);
        vector<long long> dist(n, INF);
        int s = idx[{start[0], start[1]}];
        int t = idx[{target[0], target[1]}];
        using P = pair<long long,int>;
        priority_queue<P, vector<P>, greater<P>> pq;
        dist[s] = 0;
        pq.push({0, s});
        while (!pq.empty()) {
            auto [d, u] = pq.top(); pq.pop();
            if (d != dist[u]) continue;
            if (u == t) break;
            for (auto &e : adj[u]) {
                int v = e.first;
                long long w = e.second;
                if (dist[v] > d + w) {
                    dist[v] = d + w;
                    pq.push({dist[v], v});
                }
            }
        }
        return (int)dist[t];
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int minimumCost(int[] start, int[] target, int[][] specialRoads) {
        // Map each unique point to an index
        List<int[]> points = new ArrayList<>();
        Map<String, Integer> idxMap = new HashMap<>();

        BiConsumer<Integer, Integer> addPoint = (x, y) -> {
            String key = x + "," + y;
            if (!idxMap.containsKey(key)) {
                idxMap.put(key, points.size());
                points.add(new int[]{x, y});
            }
        };

        addPoint.accept(start[0], start[1]);
        addPoint.accept(target[0], target[1]);

        // Prepare adjacency list for special directed edges
        List<int[]>[] specialAdj;
        // Temporarily store edges to add after all points are known
        List<int[][]> tempEdges = new ArrayList<>();

        for (int[] road : specialRoads) {
            int x1 = road[0], y1 = road[1];
            int x2 = road[2], y2 = road[3];
            int cost = road[4];
            addPoint.accept(x1, y1);
            addPoint.accept(x2, y2);
            tempEdges.add(new int[][]{{x1, y1}, {x2, y2}, {cost}});
        }

        int n = points.size();
        specialAdj = new ArrayList[n];
        for (int i = 0; i < n; ++i) specialAdj[i] = new ArrayList<>();

        // Populate special adjacency using indices
        for (int[][] e : tempEdges) {
            int[] src = e[0];
            int[] dst = e[1];
            int cost = e[2][0];
            int srcIdx = idxMap.get(src[0] + "," + src[1]);
            int dstIdx = idxMap.get(dst[0] + "," + dst[1]);
            specialAdj[srcIdx].add(new int[]{dstIdx, cost});
        }

        // Coordinates arrays for fast access
        int[] xs = new int[n];
        int[] ys = new int[n];
        for (int i = 0; i < n; ++i) {
            xs[i] = points.get(i)[0];
            ys[i] = points.get(i)[1];
        }

        int startIdx = idxMap.get(start[0] + "," + start[1]);
        int targetIdx = idxMap.get(target[0] + "," + target[1]);

        long[] dist = new long[n];
        Arrays.fill(dist, Long.MAX_VALUE);
        boolean[] visited = new boolean[n];
        dist[startIdx] = 0;

        // Dense Dijkstra (O(N^2))
        for (int iter = 0; iter < n; ++iter) {
            int u = -1;
            long best = Long.MAX_VALUE;
            for (int i = 0; i < n; ++i) {
                if (!visited[i] && dist[i] < best) {
                    best = dist[i];
                    u = i;
                }
            }
            if (u == -1) break;
            visited[u] = true;

            // Relax normal Manhattan edges
            for (int v = 0; v < n; ++v) {
                if (visited[v]) continue;
                long w = Math.abs(xs[u] - xs[v]) + Math.abs(ys[u] - ys[v]);
                if (dist[v] > dist[u] + w) {
                    dist[v] = dist[u] + w;
                }
            }

            // Relax special directed edges
            for (int[] e : specialAdj[u]) {
                int v = e[0];
                long w = e[1];
                if (!visited[v] && dist[v] > dist[u] + w) {
                    dist[v] = dist[u] + w;
                }
            }
        }

        return (int) dist[targetIdx];
    }
}
```

## Python

```python
class Solution(object):
    def minimumCost(self, start, target, specialRoads):
        """
        :type start: List[int]
        :type target: List[int]
        :type specialRoads: List[List[int]]
        :rtype: int
        """
        # collect all unique points: start, target and road endpoints
        pts = [tuple(start), tuple(target)]
        for x1, y1, x2, y2, _ in specialRoads:
            pts.append((x1, y1))
            pts.append((x2, y2))

        idx = {}
        nodes = []
        for p in pts:
            if p not in idx:
                idx[p] = len(nodes)
                nodes.append(p)

        n = len(nodes)
        adj = [[] for _ in range(n)]

        # add Manhattan edges between every pair of points
        for i in range(n):
            xi, yi = nodes[i]
            for j in range(i + 1, n):
                xj, yj = nodes[j]
                w = abs(xi - xj) + abs(yi - yj)
                adj[i].append((j, w))
                adj[j].append((i, w))

        # add directed special roads
        for x1, y1, x2, y2, cost in specialRoads:
            u = idx[(x1, y1)]
            v = idx[(x2, y2)]
            adj[u].append((v, cost))

        import heapq
        INF = 10 ** 18
        dist = [INF] * n
        s = idx[tuple(start)]
        t = idx[tuple(target)]
        dist[s] = 0
        heap = [(0, s)]

        while heap:
            d, u = heapq.heappop(heap)
            if d != dist[u]:
                continue
            if u == t:
                break
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))

        return dist[t]
```

## Python3

```python
import heapq
from typing import List

class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        points = [(start[0], start[1]), (target[0], target[1])]
        special_edges = []
        for x1, y1, x2, y2, c in specialRoads:
            src_idx = len(points)
            points.append((x1, y1))
            dst_idx = len(points)
            points.append((x2, y2))
            special_edges.append((src_idx, dst_idx, c))

        n = len(points)
        adj = [[] for _ in range(n)]

        # Manhattan edges (undirected)
        xs = [p[0] for p in points]
        ys = [p[1] for p in points]
        for i in range(n):
            xi, yi = xs[i], ys[i]
            for j in range(i + 1, n):
                w = abs(xi - xs[j]) + abs(yi - ys[j])
                adj[i].append((j, w))
                adj[j].append((i, w))

        # Special directed edges
        for src, dst, cost in special_edges:
            adj[src].append((dst, cost))

        # Dijkstra
        INF = 10**18
        dist = [INF] * n
        dist[0] = 0
        heap = [(0, 0)]
        while heap:
            d, u = heapq.heappop(heap)
            if d != dist[u]:
                continue
            if u == 1:  # reached target
                break
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))
        return dist[1]
```

## C

```c
#include <stdlib.h>
#include <limits.h>

typedef struct {
    int x;
    int y;
} Point;

int minimumCost(int* start, int startSize, int* target, int targetSize,
                int** specialRoads, int specialRoadsSize, int* specialRoadsColSize) {
    int N = 2 + 2 * specialRoadsSize;               // total nodes
    Point *pts = (Point *)malloc(sizeof(Point) * N);
    pts[0].x = start[0];
    pts[0].y = start[1];
    pts[1].x = target[0];
    pts[1].y = target[1];

    int *roadSrc = (int *)malloc(sizeof(int) * specialRoadsSize);
    int *roadDst = (int *)malloc(sizeof(int) * specialRoadsSize);
    int *roadCost = (int *)malloc(sizeof(int) * specialRoadsSize);

    for (int i = 0; i < specialRoadsSize; ++i) {
        int srcIdx = 2 + 2 * i;
        int dstIdx = srcIdx + 1;
        pts[srcIdx].x = specialRoads[i][0];
        pts[srcIdx].y = specialRoads[i][1];
        pts[dstIdx].x = specialRoads[i][2];
        pts[dstIdx].y = specialRoads[i][3];
        roadSrc[i] = srcIdx;
        roadDst[i] = dstIdx;
        roadCost[i] = specialRoads[i][4];
    }

    long long INF = (long long)LLONG_MAX / 4;
    long long *dist = (long long *)malloc(sizeof(long long) * N);
    int *vis = (int *)calloc(N, sizeof(int));
    for (int i = 0; i < N; ++i) dist[i] = INF;
    dist[0] = 0;

    for (int iter = 0; iter < N; ++iter) {
        int u = -1;
        long long best = INF;
        for (int i = 0; i < N; ++i) {
            if (!vis[i] && dist[i] < best) {
                best = dist[i];
                u = i;
            }
        }
        if (u == -1) break;
        vis[u] = 1;

        // walking edges to all other nodes
        for (int v = 0; v < N; ++v) {
            if (vis[v]) continue;
            long long w = llabs((long long)pts[u].x - pts[v].x) +
                          llabs((long long)pts[u].y - pts[v].y);
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
            }
        }

        // special road edges outgoing from u
        for (int i = 0; i < specialRoadsSize; ++i) {
            if (roadSrc[i] == u) {
                int v = roadDst[i];
                long long c = roadCost[i];
                if (dist[u] + c < dist[v]) {
                    dist[v] = dist[u] + c;
                }
            }
        }
    }

    int answer = (int)dist[1]; // target node index is 1

    free(pts);
    free(roadSrc);
    free(roadDst);
    free(roadCost);
    free(dist);
    free(vis);
    return answer;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MinimumCost(int[] start, int[] target, int[][] specialRoads) {
        var idx = new Dictionary<(int, int), int>();
        var points = new List<(int x, int y)>();

        void AddPoint(int x, int y) {
            var key = (x, y);
            if (!idx.ContainsKey(key)) {
                idx[key] = points.Count;
                points.Add(key);
            }
        }

        AddPoint(start[0], start[1]);
        AddPoint(target[0], target[1]);

        foreach (var road in specialRoads) {
            AddPoint(road[0], road[1]);
            AddPoint(road[2], road[3]);
        }

        int n = points.Count;
        var graph = new List<(int to, long w)>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<(int, long)>();

        // Complete Manhattan edges
        for (int i = 0; i < n; i++) {
            var (xi, yi) = points[i];
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                var (xj, yj) = points[j];
                long w = Math.Abs(xi - xj) + Math.Abs(yi - yj);
                graph[i].Add((j, w));
            }
        }

        // Special roads
        foreach (var road in specialRoads) {
            int u = idx[(road[0], road[1])];
            int v = idx[(road[2], road[3])];
            long w = road[4];
            graph[u].Add((v, w));
        }

        int startIdx = idx[(start[0], start[1])];
        int targetIdx = idx[(target[0], target[1])];

        const long INF = long.MaxValue / 4;
        var dist = new long[n];
        for (int i = 0; i < n; i++) dist[i] = INF;
        dist[startIdx] = 0;

        var pq = new PriorityQueue<(int node, long d), long>();
        pq.Enqueue((startIdx, 0L), 0L);

        while (pq.Count > 0) {
            var cur = pq.Dequeue();
            int u = cur.node;
            long du = cur.d;
            if (du != dist[u]) continue; // outdated entry

            foreach (var edge in graph[u]) {
                int v = edge.to;
                long nd = du + edge.w;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    pq.Enqueue((v, nd), nd);
                }
            }
        }

        return (int)dist[targetIdx];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} start
 * @param {number[]} target
 * @param {number[][]} specialRoads
 * @return {number}
 */
var minimumCost = function(start, target, specialRoads) {
    const pointIndex = new Map();
    const points = [];
    const addPoint = (x, y) => {
        const key = x + ',' + y;
        if (!pointIndex.has(key)) {
            pointIndex.set(key, points.length);
            points.push({ x, y });
        }
        return pointIndex.get(key);
    };
    
    const startIdx = addPoint(start[0], start[1]);
    const specialEdges = [];
    for (const r of specialRoads) {
        const src = addPoint(r[0], r[1]);
        const dst = addPoint(r[2], r[3]);
        specialEdges.push([src, dst, r[4]]);
    }
    const targetIdx = addPoint(target[0], target[1]);
    
    const n = points.length;
    const adj = Array.from({ length: n }, () => []);
    
    // walking edges (complete graph)
    for (let i = 0; i < n; ++i) {
        const pi = points[i];
        for (let j = 0; j < n; ++j) {
            if (i === j) continue;
            const pj = points[j];
            const w = Math.abs(pi.x - pj.x) + Math.abs(pi.y - pj.y);
            adj[i].push([j, w]);
        }
    }
    
    // special roads
    for (const [src, dst, cost] of specialEdges) {
        adj[src].push([dst, cost]);
    }
    
    // Dijkstra
    const dist = new Array(n).fill(Infinity);
    dist[startIdx] = 0;
    
    class MinHeap {
        constructor() { this.heap = []; }
        push(item) {
            this.heap.push(item);
            this._up(this.heap.length - 1);
        }
        _up(i) {
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (this.heap[p][0] <= this.heap[i][0]) break;
                [this.heap[p], this.heap[i]] = [this.heap[i], this.heap[p]];
                i = p;
            }
        }
        pop() {
            if (!this.heap.length) return null;
            const top = this.heap[0];
            const end = this.heap.pop();
            if (this.heap.length) {
                this.heap[0] = end;
                this._down(0);
            }
            return top;
        }
        _down(i) {
            const n = this.heap.length;
            while (true) {
                let l = i * 2 + 1, r = l + 1, smallest = i;
                if (l < n && this.heap[l][0] < this.heap[smallest][0]) smallest = l;
                if (r < n && this.heap[r][0] < this.heap[smallest][0]) smallest = r;
                if (smallest === i) break;
                [this.heap[i], this.heap[smallest]] = [this.heap[smallest], this.heap[i]];
                i = smallest;
            }
        }
        isEmpty() { return this.heap.length === 0; }
    }
    
    const heap = new MinHeap();
    heap.push([0, startIdx]);
    
    while (!heap.isEmpty()) {
        const [d, u] = heap.pop();
        if (d !== dist[u]) continue;
        if (u === targetIdx) break;
        for (const [v, w] of adj[u]) {
            const nd = d + w;
            if (nd < dist[v]) {
                dist[v] = nd;
                heap.push([nd, v]);
            }
        }
    }
    
    return dist[targetIdx];
};
```

## Typescript

```typescript
function minimumCost(start: number[], target: number[], specialRoads: number[][]): number {
    const points: [number, number][] = [];
    const pointMap = new Map<string, number>();
    function addPoint(x: number, y: number): number {
        const key = x + ',' + y;
        if (!pointMap.has(key)) {
            pointMap.set(key, points.length);
            points.push([x, y]);
        }
        return pointMap.get(key)!;
    }

    const startIdx = addPoint(start[0], start[1]);
    const targetIdx = addPoint(target[0], target[1]);

    for (const r of specialRoads) {
        addPoint(r[0], r[1]);
        addPoint(r[2], r[3]);
    }

    const n = points.length;
    interface Edge { to: number; w: number; }
    const adj: Edge[][] = Array.from({ length: n }, () => []);

    // Manhattan edges (undirected)
    for (let i = 0; i < n; i++) {
        const [xi, yi] = points[i];
        for (let j = i + 1; j < n; j++) {
            const [xj, yj] = points[j];
            const w = Math.abs(xi - xj) + Math.abs(yi - yj);
            adj[i].push({ to: j, w });
            adj[j].push({ to: i, w });
        }
    }

    // Special directed edges
    for (const r of specialRoads) {
        const fromIdx = pointMap.get(r[0] + ',' + r[1])!;
        const toIdx = pointMap.get(r[2] + ',' + r[3])!;
        adj[fromIdx].push({ to: toIdx, w: r[4] });
    }

    // Dijkstra
    const dist = new Array<number>(n).fill(Infinity);
    dist[startIdx] = 0;

    class MinHeap {
        heap: [number, number][] = [];
        push(item: [number, number]) {
            this.heap.push(item);
            this.bubbleUp(this.heap.length - 1);
        }
        bubbleUp(idx: number) {
            while (idx > 0) {
                const parent = (idx - 1) >> 1;
                if (this.heap[parent][0] <= this.heap[idx][0]) break;
                [this.heap[parent], this.heap[idx]] = [this.heap[idx], this.heap[parent]];
                idx = parent;
            }
        }
        pop(): [number, number] | undefined {
            if (this.heap.length === 0) return undefined;
            const top = this.heap[0];
            const end = this.heap.pop()!;
            if (this.heap.length > 0) {
                this.heap[0] = end;
                this.sinkDown(0);
            }
            return top;
        }
        sinkDown(idx: number) {
            const n = this.heap.length;
            while (true) {
                let left = idx * 2 + 1;
                let right = left + 1;
                let smallest = idx;
                if (left < n && this.heap[left][0] < this.heap[smallest][0]) smallest = left;
                if (right < n && this.heap[right][0] < this.heap[smallest][0]) smallest = right;
                if (smallest === idx) break;
                [this.heap[smallest], this.heap[idx]] = [this.heap[idx], this.heap[smallest]];
                idx = smallest;
            }
        }
        isEmpty() {
            return this.heap.length === 0;
        }
    }

    const pq = new MinHeap();
    pq.push([0, startIdx]);

    while (!pq.isEmpty()) {
        const [d, u] = pq.pop()!;
        if (d !== dist[u]) continue;
        if (u === targetIdx) break;
        for (const e of adj[u]) {
            const nd = d + e.w;
            if (nd < dist[e.to]) {
                dist[e.to] = nd;
                pq.push([nd, e.to]);
            }
        }
    }

    return dist[targetIdx];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $start
     * @param Integer[] $target
     * @param Integer[][] $specialRoads
     * @return Integer
     */
    function minimumCost($start, $target, $specialRoads) {
        // Collect all points: start, each road's endpoints, target
        $points = [];
        $points[] = [$start[0], $start[1]]; // index 0 is start

        $srcIdx = [];
        $dstIdx = [];

        foreach ($specialRoads as $i => $road) {
            $sx = $road[0];
            $sy = $road[1];
            $dx = $road[2];
            $dy = $road[3];

            $srcIdx[$i] = count($points);
            $points[] = [$sx, $sy];   // source point

            $dstIdx[$i] = count($points);
            $points[] = [$dx, $dy];   // destination point
        }

        $targetIdx = count($points);
        $points[] = [$target[0], $target[1]]; // target point

        $n = count($points);

        // Build adjacency list for special directed edges
        $adjSpecial = array_fill(0, $n, []);
        foreach ($specialRoads as $i => $road) {
            $cost = $road[4];
            $src = $srcIdx[$i];
            $dst = $dstIdx[$i];
            $adjSpecial[$src][] = [$dst, $cost];
        }

        // Dijkstra
        $INF = PHP_INT_MAX;
        $dist = array_fill(0, $n, $INF);
        $dist[0] = 0; // start index is 0

        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        // store [node, distance] as data, priority = -distance (min-heap behavior)
        $pq->insert([0, 0], 0);

        while (!$pq->isEmpty()) {
            $item = $pq->extract(); // [node, distance]
            [$u, $d] = $item;
            if ($d != $dist[$u]) {
                continue; // outdated entry
            }

            // Move to any other point using Manhattan distance
            for ($v = 0; $v < $n; $v++) {
                if ($v === $u) continue;
                $cost = abs($points[$u][0] - $points[$v][0]) + abs($points[$u][1] - $points[$v][1]);
                $newDist = $d + $cost;
                if ($newDist < $dist[$v]) {
                    $dist[$v] = $newDist;
                    $pq->insert([$v, $newDist], -$newDist);
                }
            }

            // Use special roads starting from u
            foreach ($adjSpecial[$u] as $edge) {
                [$dst, $c] = $edge;
                $newDist = $d + $c;
                if ($newDist < $dist[$dst]) {
                    $dist[$dst] = $newDist;
                    $pq->insert([$dst, $newDist], -$newDist);
                }
            }
        }

        return $dist[$targetIdx];
    }
}
```

## Swift

```swift
class Solution {
    func minimumCost(_ start: [Int], _ target: [Int], _ specialRoads: [[Int]]) -> Int {
        var pointIndex = [String:Int]()
        var points = [(Int,Int)]()
        func addPoint(_ x:Int,_ y:Int) -> Int {
            let key = "\(x)#\(y)"
            if let idx = pointIndex[key] { return idx }
            let idx = points.count
            points.append((x,y))
            pointIndex[key] = idx
            return idx
        }

        let startIdx = addPoint(start[0], start[1])
        let targetIdx = addPoint(target[0], target[1])

        var specialEdges: [(Int,Int,Int)] = [] // src,dst,cost

        for road in specialRoads {
            let sx = road[0], sy = road[1]
            let ex = road[2], ey = road[3]
            let cost = road[4]
            let sIdx = addPoint(sx, sy)
            let eIdx = addPoint(ex, ey)
            specialEdges.append((sIdx, eIdx, cost))
        }

        let n = points.count
        var adj = Array(repeating: [(to:Int, weight:Int)](), count: n)

        // Manhattan edges between all pairs
        for i in 0..<n {
            let (xi, yi) = points[i]
            for j in i+1..<n {
                let (xj, yj) = points[j]
                let w = abs(xi - xj) + abs(yi - yj)
                adj[i].append((to:j, weight:w))
                adj[j].append((to:i, weight:w))
            }
        }

        // special directed edges
        for (s,d,cost) in specialEdges {
            adj[s].append((to:d, weight:cost))
        }

        // Dijkstra
        let INF = Int.max/4
        var dist = Array(repeating: INF, count: n)
        dist[startIdx] = 0

        var pq = PriorityQueue()
        pq.push((0,startIdx))

        while let (d,u) = pq.pop() {
            if d != dist[u] { continue }
            if u == targetIdx { break }
            for edge in adj[u] {
                let v = edge.to
                let nd = d + edge.weight
                if nd < dist[v] {
                    dist[v] = nd
                    pq.push((nd, v))
                }
            }
        }

        return dist[targetIdx]
    }
}

struct PriorityQueue {
    private var heap: [(Int, Int)] = [] // (dist,node)

    mutating func push(_ element: (Int, Int)) {
        heap.append(element)
        siftUp(heap.count - 1)
    }

    mutating func pop() -> (Int, Int)? {
        guard !heap.isEmpty else { return nil }
        if heap.count == 1 {
            return heap.removeLast()
        }
        let top = heap[0]
        heap[0] = heap.removeLast()
        siftDown(0)
        return top
    }

    private mutating func siftUp(_ index: Int) {
        var child = index
        while child > 0 {
            let parent = (child - 1) >> 1
            if heap[child].0 < heap[parent].0 {
                heap.swapAt(child, parent)
                child = parent
            } else {
                break
            }
        }
    }

    private mutating func siftDown(_ index: Int) {
        var parent = index
        while true {
            let left = parent * 2 + 1
            let right = left + 1
            var smallest = parent
            if left < heap.count && heap[left].0 < heap[smallest].0 {
                smallest = left
            }
            if right < heap.count && heap[right].0 < heap[smallest].0 {
                smallest = right
            }
            if smallest == parent { break }
            heap.swapAt(parent, smallest)
            parent = smallest
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumCost(start: IntArray, target: IntArray, specialRoads: Array<IntArray>): Int {
        // Collect all unique points: start, target, and endpoints of special roads
        val points = mutableListOf<Pair<Int, Int>>()
        points.add(Pair(start[0], start[1]))
        points.add(Pair(target[0], target[1]))
        for (road in specialRoads) {
            points.add(Pair(road[0], road[1]))
            points.add(Pair(road[2], road[3]))
        }

        // Map each unique point to an index
        val idxMap = HashMap<Long, Int>()
        val uniqPoints = mutableListOf<Pair<Int, Int>>()
        for (p in points) {
            val key = (p.first.toLong() shl 32) or (p.second.toLong() and 0xffffffffL)
            if (!idxMap.containsKey(key)) {
                idxMap[key] = uniqPoints.size
                uniqPoints.add(p)
            }
        }

        val n = uniqPoints.size
        val adj = Array(n) { mutableListOf<Pair<Int, Int>>() } // neighbor index, weight

        // Add undirected edges with Manhattan distance between every pair of points
        for (i in 0 until n) {
            val (xi, yi) = uniqPoints[i]
            for (j in i + 1 until n) {
                val (xj, yj) = uniqPoints[j]
                val w = kotlin.math.abs(xi - xj) + kotlin.math.abs(yi - yj)
                adj[i].add(Pair(j, w))
                adj[j].add(Pair(i, w))
            }
        }

        // Add directed special road edges
        for (road in specialRoads) {
            val sx = road[0]
            val sy = road[1]
            val ex = road[2]
            val ey = road[3]
            val cost = road[4]

            val startKey = (sx.toLong() shl 32) or (sy.toLong() and 0xffffffffL)
            val endKey = (ex.toLong() shl 32) or (ey.toLong() and 0xffffffffL)

            val u = idxMap[startKey]!!
            val v = idxMap[endKey]!!

            adj[u].add(Pair(v, cost))
        }

        // Dijkstra's algorithm from start to target
        val startKey = (start[0].toLong() shl 32) or (start[1].toLong() and 0xffffffffL)
        val targetKey = (target[0].toLong() shl 32) or (target[1].toLong() and 0xffffffffL)

        val src = idxMap[startKey]!!
        val dst = idxMap[targetKey]!!

        val dist = LongArray(n) { Long.MAX_VALUE }
        dist[src] = 0L
        val pq = java.util.PriorityQueue<Pair<Long, Int>>(compareBy { it.first })
        pq.add(Pair(0L, src))

        while (pq.isNotEmpty()) {
            val (d, u) = pq.poll()
            if (d != dist[u]) continue
            if (u == dst) break
            for ((v, w) in adj[u]) {
                val nd = d + w
                if (nd < dist[v]) {
                    dist[v] = nd
                    pq.add(Pair(nd, v))
                }
            }
        }

        return dist[dst].toInt()
    }
}
```

## Dart

```dart
class Solution {
  int minimumCost(List<int> start, List<int> target, List<List<int>> specialRoads) {
    // Collect all points: start, target, and each road's endpoints.
    List<List<int>> points = [];
    int startIdx = 0;
    points.add([start[0], start[1]]);
    int targetIdx = 1;
    points.add([target[0], target[1]]);

    // Keep indices of each special road's source and destination.
    List<int> srcIdx = [];
    List<int> dstIdx = [];
    List<int> roadCost = [];

    for (var r in specialRoads) {
      int s = points.length;
      points.add([r[0], r[1]]);
      int d = points.length;
      points.add([r[2], r[3]]);
      srcIdx.add(s);
      dstIdx.add(d);
      roadCost.add(r[4]);
    }

    int n = points.length;
    // Build adjacency list with walking edges (Manhattan distance).
    List<List<List<int>>> adj = List.generate(n, (_) => []);
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        if (i == j) continue;
        int w = (points[i][0] - points[j][0]).abs() + (points[i][1] - points[j][1]).abs();
        adj[i].add([j, w]);
      }
    }

    // Add special road edges.
    for (int k = 0; k < srcIdx.length; ++k) {
      int s = srcIdx[k];
      int d = dstIdx[k];
      int c = roadCost[k];
      adj[s].add([d, c]);
    }

    // Dijkstra's algorithm (O(N^2) is fine for N <= 402).
    const int INF = 1 << 60;
    List<int> dist = List.filled(n, INF);
    List<bool> visited = List.filled(n, false);
    dist[startIdx] = 0;

    for (int iter = 0; iter < n; ++iter) {
      int u = -1;
      int best = INF;
      for (int i = 0; i < n; ++i) {
        if (!visited[i] && dist[i] < best) {
          best = dist[i];
          u = i;
        }
      }
      if (u == -1) break;
      visited[u] = true;
      if (u == targetIdx) break;

      for (var edge in adj[u]) {
        int v = edge[0];
        int w = edge[1];
        if (!visited[v] && dist[u] + w < dist[v]) {
          dist[v] = dist[u] + w;
        }
      }
    }

    return dist[targetIdx];
  }
}
```

## Golang

```go
package main

import (
	"container/heap"
)

type Edge struct {
	to   int
	cost int
}

type Item struct {
	node int
	dist int
}
type PriorityQueue []Item

func (pq PriorityQueue) Len() int { return len(pq) }
func (pq PriorityQueue) Less(i, j int) bool {
	return pq[i].dist < pq[j].dist
}
func (pq PriorityQueue) Swap(i, j int) { pq[i], pq[j] = pq[j], pq[i] }

func (pq *PriorityQueue) Push(x interface{}) {
	*pq = append(*pq, x.(Item))
}
func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	it := old[n-1]
	*pq = old[:n-1]
	return it
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func minimumCost(start []int, target []int, specialRoads [][]int) int {
	points := make([][]int, 0)
	points = append(points, []int{start[0], start[1]}) // index 0 is start

	type roadEdge struct {
		from int
		to   int
		cost int
	}
	roads := make([]roadEdge, 0)

	for _, r := range specialRoads {
		srcIdx := len(points)
		points = append(points, []int{r[0], r[1]})
		dstIdx := len(points)
		points = append(points, []int{r[2], r[3]})
		roads = append(roads, roadEdge{from: srcIdx, to: dstIdx, cost: r[4]})
	}

	targetIdx := len(points)
	points = append(points, []int{target[0], target[1]})

	n := len(points)
	graph := make([][]Edge, n)

	// add Manhattan edges between all pairs (undirected)
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			c := abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
			graph[i] = append(graph[i], Edge{to: j, cost: c})
			graph[j] = append(graph[j], Edge{to: i, cost: c})
		}
	}

	// add special directed edges
	for _, re := range roads {
		graph[re.from] = append(graph[re.from], Edge{to: re.to, cost: re.cost})
	}

	const INF int = int(1e18)
	dist := make([]int, n)
	for i := range dist {
		dist[i] = INF
	}
	dist[0] = 0

	pq := &PriorityQueue{}
	heap.Push(pq, Item{node: 0, dist: 0})

	visited := make([]bool, n)

	for pq.Len() > 0 {
		it := heap.Pop(pq).(Item)
		u := it.node
		if visited[u] {
			continue
		}
		visited[u] = true
		if u == targetIdx {
			break
		}
		for _, e := range graph[u] {
			v := e.to
			newDist := dist[u] + e.cost
			if newDist < dist[v] {
				dist[v] = newDist
				heap.Push(pq, Item{node: v, dist: newDist})
			}
		}
	}

	return dist[targetIdx]
}
```

## Ruby

```ruby
def minimum_cost(start, target, special_roads)
  # Helper to get or create node index for a coordinate
  point_index = {}
  points = []

  get_idx = lambda do |x, y|
    key = [x, y]
    unless point_index.key?(key)
      point_index[key] = points.length
      points << [x, y]
    end
    point_index[key]
  end

  start_idx = get_idx.call(start[0], start[1])
  target_idx = nil

  special_edges = []

  special_roads.each do |road|
    sx, sy, ex, ey, cost = road
    s_idx = get_idx.call(sx, sy)
    e_idx = get_idx.call(ex, ey)
    special_edges << [s_idx, e_idx, cost]
  end

  target_idx = get_idx.call(target[0], target[1])

  n = points.size
  adj = Array.new(n) { [] }

  # walking edges (undirected Manhattan distance)
  (0...n).each do |i|
    xi, yi = points[i]
    ((i + 1)...n).each do |j|
      xj, yj = points[j]
      w = (xi - xj).abs + (yi - yj).abs
      adj[i] << [j, w]
      adj[j] << [i, w]
    end
  end

  # special road edges (directed)
  special_edges.each do |s_idx, e_idx, cost|
    adj[s_idx] << [e_idx, cost]
  end

  # Dijkstra's algorithm with a binary min-heap
  class MinHeap
    def initialize
      @data = []
    end

    def push(item)
      @data << item
      sift_up(@data.size - 1)
    end

    def pop
      return nil if @data.empty?
      min = @data[0]
      last = @data.pop
      unless @data.empty?
        @data[0] = last
        sift_down(0)
      end
      min
    end

    def empty?
      @data.empty?
    end

    private

    def sift_up(i)
      while i > 0
        p = (i - 1) / 2
        break if @data[p][0] <= @data[i][0]
        @data[p], @data[i] = @data[i], @data[p]
        i = p
      end
    end

    def sift_down(i)
      n = @data.size
      loop do
        l = 2 * i + 1
        r = l + 1
        smallest = i
        smallest = l if l < n && @data[l][0] < @data[smallest][0]
        smallest = r if r < n && @data[r][0] < @data[smallest][0]
        break if smallest == i
        @data[i], @data[smallest] = @data[smallest], @data[i]
        i = smallest
      end
    end
  end

  dist = Array.new(n, Float::INFINITY)
  dist[start_idx] = 0
  heap = MinHeap.new
  heap.push([0, start_idx])

  until heap.empty?
    d_u, u = heap.pop
    next if d_u != dist[u]
    adj[u].each do |v, w|
      nd = d_u + w
      if nd < dist[v]
        dist[v] = nd
        heap.push([nd, v])
      end
    end
  end

  dist[target_idx].to_i
end
```

## Scala

```scala
object Solution {
  def minimumCost(start: Array[Int], target: Array[Int], specialRoads: Array[Array[Int]]): Int = {
    import scala.collection.mutable

    val points = mutable.ArrayBuffer[(Int, Int)]()
    points += ((start(0), start(1)))

    case class Edge(src: Int, dst: Int, cost: Int)
    val roadEdges = mutable.ArrayBuffer[Edge]()

    for (road <- specialRoads) {
      val x1 = road(0); val y1 = road(1); val x2 = road(2); val y2 = road(3); val c = road(4)
      val srcIdx = points.length
      points += ((x1, y1))
      val dstIdx = points.length
      points += ((x2, y2))
      roadEdges += Edge(srcIdx, dstIdx, c)
    }

    val targetIdx = points.length
    points += ((target(0), target(1)))

    val n = points.size
    val adj = Array.fill(n)(mutable.ArrayBuffer[(Int, Int)]())

    // walking edges (complete graph)
    for (i <- 0 until n) {
      var j = 0
      while (j < n) {
        if (i != j) {
          val w = math.abs(points(i)._1 - points(j)._1) + math.abs(points(i)._2 - points(j)._2)
          adj(i).addOne((j, w))
        }
        j += 1
      }
    }

    // special road edges
    for (e <- roadEdges) {
      adj(e.src).addOne((e.dst, e.cost))
    }

    val INF = Long.MaxValue / 4
    val dist = Array.fill[Long](n)(INF)
    dist(0) = 0L

    val pq = new java.util.PriorityQueue[(Long, Int)](
      new java.util.Comparator[(Long, Int)] {
        override def compare(o1: (Long, Int), o2: (Long, Int)): Int =
          java.lang.Long.compare(o1._1, o2._1)
      }
    )
    pq.offer((0L, 0))

    while (!pq.isEmpty) {
      val cur = pq.poll()
      val d = cur._1
      val u = cur._2
      if (d != dist(u)) {
        // outdated entry
      } else {
        for ((v, w) <- adj(u)) {
          val nd = d + w.toLong
          if (nd < dist(v)) {
            dist(v) = nd
            pq.offer((nd, v))
          }
        }
      }
    }

    dist(targetIdx).toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_cost(start: Vec<i32>, target: Vec<i32>, special_roads: Vec<Vec<i32>>) -> i32 {
        use std::cmp::Reverse;
        use std::collections::BinaryHeap;

        // collect all points: start, target, and every road endpoint
        let mut points: Vec<(i64, i64)> = Vec::new();
        points.push((start[0] as i64, start[1] as i64));   // index 0
        points.push((target[0] as i64, target[1] as i64)); // index 1

        let mut special_edges: Vec<(usize, usize, i64)> = Vec::new();

        for road in special_roads.iter() {
            let sx = road[0] as i64;
            let sy = road[1] as i64;
            let ex = road[2] as i64;
            let ey = road[3] as i64;
            let cost = road[4] as i64;

            let src_idx = points.len();
            points.push((sx, sy));
            let dst_idx = points.len();
            points.push((ex, ey));

            special_edges.push((src_idx, dst_idx, cost));
        }

        let n = points.len();
        let mut adj: Vec<Vec<(usize, i64)>> = vec![Vec::new(); n];

        // walking edges between every pair of nodes (Manhattan distance)
        for i in 0..n {
            for j in 0..n {
                if i == j {
                    continue;
                }
                let (xi, yi) = points[i];
                let (xj, yj) = points[j];
                let w = (xi - xj).abs() + (yi - yj).abs();
                adj[i].push((j, w));
            }
        }

        // add directed special road edges
        for (src, dst, cost) in special_edges {
            adj[src].push((dst, cost));
        }

        let start_idx = 0usize;
        let target_idx = 1usize;

        const INF: i64 = i64::MAX / 4;
        let mut dist = vec![INF; n];
        dist[start_idx] = 0;

        let mut heap = BinaryHeap::new();
        heap.push((Reverse(0_i64), start_idx));

        while let Some((Reverse(d), u)) = heap.pop() {
            if d != dist[u] {
                continue;
            }
            if u == target_idx {
                break;
            }
            for &(v, w) in &adj[u] {
                let nd = d + w;
                if nd < dist[v] {
                    dist[v] = nd;
                    heap.push((Reverse(nd), v));
                }
            }
        }

        dist[target_idx] as i32
    }
}
```

## Racket

```racket
#lang racket
(require racket/heap)

(define (manhattan p q)
  (+ (abs (- (first p) (first q))) (abs (- (second p) (second q)))))

(define/contract (minimum-cost start target specialRoads)
  (-> (listof exact-integer?) (listof exact-integer?) (listof (listof exact-integer?)) exact-integer?)
  (let* ((nroads (length specialRoads))
         (total-nodes (+ 2 (* 2 nroads))) ; start + target + each endpoint
         (points (make-vector total-nodes)))
    ;; set start point
    (vector-set! points 0 start)
    ;; set road endpoints
    (for ([i (in-range nroads)])
      (define road (list-ref specialRoads i))
      (define s-idx (+ 1 (* 2 i)))
      (define e-idx (+ s-idx 1))
      (vector-set! points s-idx (list (list-ref road 0) (list-ref road 1)))
      (vector-set! points e-idx (list (list-ref road 2) (list-ref road 3))))
    ;; set target point
    (define target-index (- total-nodes 1))
    (vector-set! points target-index target)

    ;; build adjacency list
    (define adj (make-vector total-nodes '()))
    ;; Manhattan edges (undirected)
    (for ([i (in-range total-nodes)])
      (for ([j (in-range (+ i 1) total-nodes)])
        (define w (manhattan (vector-ref points i) (vector-ref points j)))
        (vector-set! adj i (cons (list j w) (vector-ref adj i)))
        (vector-set! adj j (cons (list i w) (vector-ref adj j)))))
    ;; special road directed edges
    (for ([i (in-range nroads)])
      (define road (list-ref specialRoads i))
      (define s-idx (+ 1 (* 2 i)))
      (define e-idx (+ s-idx 1))
      (define c (list-ref road 4))
      (vector-set! adj s-idx (cons (list e-idx c) (vector-ref adj s-idx))))

    ;; Dijkstra
    (define INF (expt 10 15))
    (define dist (make-vector total-nodes INF))
    (vector-set! dist 0 0)
    (define heap (make-heap (lambda (a b) (< (first a) (first b)))))
    (heap-push! heap (list 0 0))

    (let loop ()
      (unless (heap-empty? heap)
        (define top (heap-pop! heap))
        (define d (first top))
        (define u (second top))
        (when (= d (vector-ref dist u))
          (for ([edge (vector-ref adj u)])
            (define v (first edge))
            (define w (second edge))
            (define nd (+ d w))
            (when (< nd (vector-ref dist v))
              (vector-set! dist v nd)
              (heap-push! heap (list nd v)))))
        (loop)))
    (vector-ref dist target-index)))
```

## Erlang

```erlang
-module(solution).
-export([minimum_cost/3]).

-define(INF, 1000000000000000). % sufficiently large

minimum_cost(Start, Target, SpecialRoads) ->
    {Map, Points} = build_points(Start, Target, SpecialRoads),
    N = length(Points),
    Adj0 = array:new(N, [{default, []}]),
    Adj1 = add_manhattan_edges(Adj0, Points, 0, N),
    Adj2 = add_special_edges(Adj1, Map, SpecialRoads),
    StartIdx = maps:get({hd(Start), hd(tl(Start))}, Map),
    TargetIdx = maps:get({hd(Target), hd(tl(Target))}, Map),
    dijkstra(N, Adj2, StartIdx, TargetIdx).

%% Build mapping from coordinate to index and list of unique points
build_points(Start, Target, SpecialRoads) ->
    AllCoords = [list_to_tuple(Start)] ++
                lists:flatten(
                    [ [ {X1,Y1}, {X2,Y2} ] ||
                        [X1,Y1,X2,Y2,_] <- SpecialRoads ]) ++
                [list_to_tuple(Target)],
    build_coords(AllCoords, 0, #{}, []).

build_coords([], _Idx, Map, Acc) ->
    {Map, lists:reverse(Acc)};
build_coords([Coord|Rest], Idx, Map, Acc) ->
    case maps:is_key(Coord, Map) of
        true -> build_coords(Rest, Idx, Map, Acc);
        false ->
            NewMap = maps:put(Coord, Idx, Map),
            build_coords(Rest, Idx + 1, NewMap, [Coord|Acc])
    end.

%% Add Manhattan edges between all pairs of points
add_manhattan_edges(Adj, Points, I, N) when I < N ->
    Adj1 = add_edges_from_i(Adj, Points, I, I+1, N),
    add_manhattan_edges(Adj1, Points, I+1, N);
add_manhattan_edges(Adj, _Points, _I, _N) -> Adj.

add_edges_from_i(Adj, Points, I, J, N) when J < N ->
    Pi = lists:nth(I+1, Points),
    Pj = lists:nth(J+1, Points),
    D = manhattan(Pi, Pj),
    Adj1 = add_undirected_edge(Adj, I, J, D),
    add_edges_from_i(Adj1, Points, I, J+1, N);
add_edges_from_i(Adj, _Points, _I, _J, _N) -> Adj.

manhattan({X1,Y1}, {X2,Y2}) ->
    abs(X1 - X2) + abs(Y1 - Y2).

add_undirected_edge(Adj, I, J, W) ->
    Adj1 = add_directed_edge(Adj, I, J, W),
    add_directed_edge(Adj1, J, I, W).

add_directed_edge(Adj, From, To, W) ->
    List = array:get(From, Adj),
    NewList = [{To, W} | List],
    array:set(From, NewList, Adj).

%% Add special road edges (directed)
add_special_edges(Adj, Map, SpecialRoads) ->
    lists:foldl(fun([X1,Y1,X2,Y2,C], AccAdj) ->
        SrcIdx = maps:get({X1,Y1}, Map),
        DstIdx = maps:get({X2,Y2}, Map),
        add_directed_edge(AccAdj, SrcIdx, DstIdx, C)
    end, Adj, SpecialRoads).

%% Dijkstra's algorithm (O(N^2) version)
dijkstra(N, Adj, StartIdx, TargetIdx) ->
    Dist0 = array:new(N, [{default, ?INF}]),
    Dist1 = array:set(StartIdx, 0, Dist0),
    Visited0 = array:new(N, [{default, false}]),
    dijkstra_loop(N, Adj, Dist1, Visited0, TargetIdx).

dijkstra_loop(N, Adj, Dist, Visited, TargetIdx) ->
    case find_min_unvisited(Dist, Visited, N, ?INF, undefined) of
        {undefined, _} -> array:get(TargetIdx, Dist);
        {U, _DistU} when U =:= TargetIdx ->
            array:get(TargetIdx, Dist);
        {U, DistU} ->
            Visited1 = array:set(U, true, Visited),
            AdjList = array:get(U, Adj),
            Dist2 = relax_neighbors(AdjList, Dist, Visited1, DistU),
            dijkstra_loop(N, Adj, Dist2, Visited1, TargetIdx)
    end.

find_min_unvisited(_Dist, _Visited, I, _BestVal, BestIdx) when I >= 0 ->
    {BestIdx, _BestVal};
find_min_unvisited(Dist, Visited, I, BestVal, BestIdx) ->
    case array:get(I, Visited) of
        true -> find_min_unvisited(Dist, Visited, I-1, BestVal, BestIdx);
        false ->
            CurDist = array:get(I, Dist),
            if CurDist < BestVal ->
                    find_min_unvisited(Dist, Visited, I-1, CurDist, I);
               true ->
                    find_min_unvisited(Dist, Visited, I-1, BestVal, BestIdx)
            end
    end.

relax_neighbors([], Dist, _Visited, _BaseDist) -> Dist;
relax_neighbors([{V,W}|Rest], Dist, Visited, BaseDist) ->
    case array:get(V, Visited) of
        true -> relax_neighbors(Rest, Dist, Visited, BaseDist);
        false ->
            Cur = array:get(V, Dist),
            NewVal = BaseDist + W,
            Dist1 = if NewVal < Cur -> array:set(V, NewVal, Dist); true -> Dist end,
            relax_neighbors(Rest, Dist1, Visited, BaseDist)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_cost(start :: [integer], target :: [integer], special_roads :: [[integer]]) :: integer
  def minimum_cost(start, target, special_roads) do
    {sx, sy} = {Enum.at(start, 0), Enum.at(start, 1)}
    {tx, ty} = {Enum.at(target, 0), Enum.at(target, 1)}

    # Build unique points and index mapping
    {idx_map, points_list} =
      Enum.reduce(special_roads, {%{}, []}, fn [x1, y1, x2, y2, _c], {m, lst} ->
        {m, lst} = add_point({x1, y1}, m, lst)
        add_point({x2, y2}, m, lst)
      end)

    {idx_map, points_list} = add_point({sx, sy}, idx_map, points_list)
    {idx_map, points_list} = add_point({tx, ty}, idx_map, points_list)

    points = List.to_tuple(points_list)
    n = tuple_size(points)

    start_idx = Map.fetch!(idx_map, {sx, sy})
    target_idx = Map.fetch!(idx_map, {tx, ty})

    # Build adjacency for special roads (directed)
    special_adj =
      Enum.reduce(special_roads, %{}, fn [x1, y1, x2, y2, c], acc ->
        src = Map.fetch!(idx_map, {x1, y1})
        dst = Map.fetch!(idx_map, {x2, y2})

        Map.update(acc, src, [{dst, c}], fn lst -> [{dst, c} | lst] end)
      end)

    inf = 1_000_000_000_000

    # Dijkstra with O(N^2) scanning
    unvisited = MapSet.new(0..(n - 1))
    dist = %{start_idx => 0}

    dijkstra(unvisited, dist, points, special_adj, target_idx, inf)
    |> Map.get(target_idx, inf)
  end

  defp add_point(coord, map, list) do
    case Map.has_key?(map, coord) do
      true ->
        {map, list}

      false ->
        idx = map_size(map)
        {Map.put(map, coord, idx), list ++ [coord]}
    end
  end

  defp manhattan(points, i, j) do
    {x1, y1} = elem(points, i)
    {x2, y2} = elem(points, j)
    abs(x1 - x2) + abs(y1 - y2)
  end

  defp dijkstra(unvisited, dist, points, special_adj, target_idx, inf) do
    if MapSet.size(unvisited) == 0 do
      dist
    else
      # find unvisited node with minimal distance
      {u, du} =
        Enum.reduce(unvisited, {nil, inf}, fn idx, {best_idx, best_dist} ->
          d = Map.get(dist, idx, inf)

          if d < best_dist do
            {idx, d}
          else
            {best_idx, best_dist}
          end
        end)

      # If the smallest distance is infinite, remaining nodes are unreachable
      if du == inf do
        dist
      else
        unvisited2 = MapSet.delete(unvisited, u)

        # relax normal edges (Manhattan distances)
        dist1 =
          Enum.reduce(MapSet.to_list(unvisited2), dist, fn v, acc ->
            nd = du + manhattan(points, u, v)
            cur = Map.get(acc, v, inf)

            if nd < cur do
              Map.put(acc, v, nd)
            else
              acc
            end
          end)

        # relax special directed edges from u
        dist2 =
          case Map.get(special_adj, u) do
            nil ->
              dist1

            list ->
              Enum.reduce(list, dist1, fn {v, cost}, acc ->
                nd = du + cost
                cur = Map.get(acc, v, inf)

                if nd < cur do
                  Map.put(acc, v, nd)
                else
                  acc
                end
              end)
          end

        # early exit if target reached and its distance won't improve further
        if u == target_idx do
          dist2
        else
          dijkstra(unvisited2, dist2, points, special_adj, target_idx, inf)
        end
      end
    end
  end
end
```
