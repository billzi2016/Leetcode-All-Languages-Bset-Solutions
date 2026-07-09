# 3607. Power Grid Maintenance

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    struct DSU {
        vector<int> p, sz;
        DSU(int n = 0) { init(n); }
        void init(int n) {
            p.resize(n + 1);
            sz.assign(n + 1, 1);
            iota(p.begin(), p.end(), 0);
        }
        int find(int x) {
            if (p[x] == x) return x;
            return p[x] = find(p[x]);
        }
        void unite(int a, int b) {
            a = find(a); b = find(b);
            if (a == b) return;
            if (sz[a] < sz[b]) swap(a, b);
            p[b] = a;
            sz[a] += sz[b];
        }
    };
    
    vector<int> processQueries(int c, vector<vector<int>>& connections, vector<vector<int>>& queries) {
        DSU dsu(c);
        for (auto &e : connections) {
            dsu.unite(e[0], e[1]);
        }
        // sets per component root
        vector< set<int> > compSet(c + 1);
        for (int i = 1; i <= c; ++i) {
            int r = dsu.find(i);
            compSet[r].insert(i);
        }
        vector<int> ans;
        ans.reserve(queries.size());
        for (auto &q : queries) {
            int type = q[0];
            int x = q[1];
            int r = dsu.find(x);
            auto &s = compSet[r];
            if (type == 2) { // take offline
                s.erase(x);
            } else { // query
                if (s.find(x) != s.end()) {
                    ans.push_back(x);
                } else if (!s.empty()) {
                    ans.push_back(*s.begin());
                } else {
                    ans.push_back(-1);
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[] processQueries(int c, int[][] connections, int[][] queries) {
        DSU dsu = new DSU(c);
        for (int[] e : connections) {
            dsu.union(e[0], e[1]);
        }

        Map<Integer, TreeSet<Integer>> compMap = new HashMap<>();
        for (int i = 1; i <= c; i++) {
            int root = dsu.find(i);
            compMap.computeIfAbsent(root, k -> new TreeSet<>()).add(i);
        }

        List<Integer> answers = new ArrayList<>();
        for (int[] q : queries) {
            int type = q[0];
            int x = q[1];
            int root = dsu.find(x);
            TreeSet<Integer> set = compMap.get(root);
            if (type == 2) { // take offline
                set.remove(x);
            } else { // query
                if (set.contains(x)) {
                    answers.add(x);
                } else if (!set.isEmpty()) {
                    answers.add(set.first());
                } else {
                    answers.add(-1);
                }
            }
        }

        int[] res = new int[answers.size()];
        for (int i = 0; i < res.length; i++) {
            res[i] = answers.get(i);
        }
        return res;
    }

    private static class DSU {
        int[] parent;
        int[] size;

        DSU(int n) {
            parent = new int[n + 1];
            size = new int[n + 1];
            for (int i = 1; i <= n; i++) {
                parent[i] = i;
                size[i] = 1;
            }
        }

        int find(int x) {
            if (parent[x] != x) {
                parent[x] = find(parent[x]);
            }
            return parent[x];
        }

        void union(int a, int b) {
            int ra = find(a);
            int rb = find(b);
            if (ra == rb) return;
            if (size[ra] < size[rb]) {
                int tmp = ra; ra = rb; rb = tmp;
            }
            parent[rb] = ra;
            size[ra] += size[rb];
        }
    }
}
```

## Python

```python
class Solution(object):
    def processQueries(self, c, connections, queries):
        """
        :type c: int
        :type connections: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        import heapq

        # DSU implementation
        parent = list(range(c + 1))
        size = [1] * (c + 1)

        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u

        def union(u, v):
            ru, rv = find(u), find(v)
            if ru == rv:
                return
            if size[ru] < size[rv]:
                ru, rv = rv, ru
            parent[rv] = ru
            size[ru] += size[rv]

        # unite all connections
        for u, v in connections:
            union(u, v)

        # component root for each node
        comp_root = [0] * (c + 1)
        for i in range(1, c + 1):
            comp_root[i] = find(i)

        # build heap per component
        heaps = {}
        for i in range(1, c + 1):
            r = comp_root[i]
            if r not in heaps:
                heaps[r] = []
            heaps[r].append(i)
        for h in heaps.values():
            heapq.heapify(h)

        online = [True] * (c + 1)
        ans = []

        for typ, x in queries:
            if typ == 2:  # take offline
                if online[x]:
                    online[x] = False
                # lazy removal from heap; nothing else needed
            else:  # typ == 1, query
                if online[x]:
                    ans.append(x)
                else:
                    r = comp_root[x]
                    h = heaps.get(r, [])
                    while h and not online[h[0]]:
                        heapq.heappop(h)
                    if h:
                        ans.append(h[0])
                    else:
                        ans.append(-1)

        return ans
```

## Python3

```python
import heapq
from typing import List

class UnionFind:
    __slots__ = ("parent", "rank")
    def __init__(self, n: int):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, a: int, b: int):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        uf = UnionFind(c)
        for u, v in connections:
            uf.union(u, v)

        comp = [0] * (c + 1)
        groups = {}
        for i in range(1, c + 1):
            r = uf.find(i)
            comp[i] = r
            if r not in groups:
                groups[r] = []
            groups[r].append(i)

        heaps = {}
        for r, lst in groups.items():
            heapq.heapify(lst)
            heaps[r] = lst

        online = [True] * (c + 1)
        ans = []

        for typ, x in queries:
            if typ == 2:          # take offline
                online[x] = False
            else:                 # query
                if online[x]:
                    ans.append(x)
                else:
                    h = heaps[comp[x]]
                    while h and not online[h[0]]:
                        heapq.heappop(h)
                    ans.append(h[0] if h else -1)

        return ans
```

## C

```c
#include <stdlib.h>

typedef struct {
    int *data;
    int size;
    int capacity;
} MinHeap;

static void heapPush(MinHeap *h, int val) {
    if (h->size == h->capacity) {
        int newCap = h->capacity ? h->capacity * 2 : 4;
        h->data = (int *)realloc(h->data, newCap * sizeof(int));
        h->capacity = newCap;
    }
    int i = h->size++;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (h->data[p] <= val) break;
        h->data[i] = h->data[p];
        i = p;
    }
    h->data[i] = val;
}

static void heapPop(MinHeap *h) {
    int n = --h->size;
    if (n == 0) return;
    int val = h->data[n];
    int i = 0;
    while (1) {
        int l = (i << 1) + 1;
        if (l >= n) break;
        int r = l + 1;
        int child = (r < n && h->data[r] < h->data[l]) ? r : l;
        if (h->data[child] >= val) break;
        h->data[i] = h->data[child];
        i = child;
    }
    h->data[i] = val;
}

/* Union-Find */
static int *parentUF;
static unsigned char *rankUF;

static int findSet(int x) {
    if (parentUF[x] != x)
        parentUF[x] = findSet(parentUF[x]);
    return parentUF[x];
}

static void unionSet(int a, int b) {
    int ra = findSet(a);
    int rb = findSet(b);
    if (ra == rb) return;
    if (rankUF[ra] < rankUF[rb]) {
        parentUF[ra] = rb;
    } else if (rankUF[ra] > rankUF[rb]) {
        parentUF[rb] = ra;
    } else {
        parentUF[rb] = ra;
        rankUF[ra]++;
    }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* processQueries(int c, int** connections, int connectionsSize, int* connectionsColSize,
                    int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    /* Initialize Union-Find */
    parentUF = (int *)malloc((c + 1) * sizeof(int));
    rankUF   = (unsigned char *)calloc(c + 1, sizeof(unsigned char));
    for (int i = 1; i <= c; ++i) parentUF[i] = i;

    for (int i = 0; i < connectionsSize; ++i) {
        int u = connections[i][0];
        int v = connections[i][1];
        unionSet(u, v);
    }

    /* Build heaps per component */
    MinHeap *heaps = (MinHeap *)calloc(c + 1, sizeof(MinHeap));
    for (int i = 1; i <= c; ++i) {
        int r = findSet(i);
        heapPush(&heaps[r], i);
    }

    /* Online status */
    unsigned char *online = (unsigned char *)malloc((c + 1) * sizeof(unsigned char));
    for (int i = 1; i <= c; ++i) online[i] = 1;

    /* Count type-1 queries to allocate result array */
    int ansCount = 0;
    for (int i = 0; i < queriesSize; ++i)
        if (queries[i][0] == 1) ++ansCount;

    int *answers = (int *)malloc(ansCount * sizeof(int));
    int idx = 0;

    /* Process queries */
    for (int i = 0; i < queriesSize; ++i) {
        int type = queries[i][0];
        int x = queries[i][1];
        if (type == 2) {               // take offline
            online[x] = 0;
        } else {                       // query
            int res;
            if (online[x]) {
                res = x;
            } else {
                int r = findSet(x);
                MinHeap *h = &heaps[r];
                while (h->size > 0 && !online[h->data[0]]) heapPop(h);
                if (h->size == 0) res = -1;
                else res = h->data[0];
            }
            answers[idx++] = res;
        }
    }

    *returnSize = ansCount;

    /* Cleanup */
    free(parentUF);
    free(rankUF);
    for (int i = 1; i <= c; ++i) {
        if (heaps[i].data) free(heaps[i].data);
    }
    free(heaps);
    free(online);

    return answers;
}
```

## Csharp

```csharp
public class Solution {
    public int[] ProcessQueries(int c, int[][] connections, int[][] queries) {
        var adj = new List<int>[c + 1];
        for (int i = 1; i <= c; i++) adj[i] = new List<int>();
        foreach (var conn in connections) {
            int u = conn[0], v = conn[1];
            adj[u].Add(v);
            adj[v].Add(u);
        }

        int[] compId = new int[c + 1];
        var visited = new bool[c + 1];
        int compCount = 0;
        for (int i = 1; i <= c; i++) {
            if (!visited[i]) {
                var stack = new Stack<int>();
                stack.Push(i);
                visited[i] = true;
                while (stack.Count > 0) {
                    int node = stack.Pop();
                    compId[node] = compCount;
                    foreach (int nb in adj[node]) {
                        if (!visited[nb]) {
                            visited[nb] = true;
                            stack.Push(nb);
                        }
                    }
                }
                compCount++;
            }
        }

        var sets = new SortedSet<int>[compCount];
        for (int i = 0; i < compCount; i++) sets[i] = new SortedSet<int>();
        for (int node = 1; node <= c; node++) {
            sets[compId[node]].Add(node);
        }

        var result = new List<int>();
        foreach (var q in queries) {
            int type = q[0];
            int x = q[1];
            var set = sets[compId[x]];
            if (type == 2) {
                set.Remove(x);
            } else { // type == 1
                if (set.Contains(x)) {
                    result.Add(x);
                } else if (set.Count > 0) {
                    result.Add(set.Min);
                } else {
                    result.Add(-1);
                }
            }
        }

        return result.ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {number} c
 * @param {number[][]} connections
 * @param {number[][]} queries
 * @return {number[]}
 */
var processQueries = function(c, connections, queries) {
    const parent = new Array(c + 1);
    const rank = new Array(c + 1).fill(0);
    for (let i = 1; i <= c; i++) parent[i] = i;

    function find(x) {
        while (parent[x] !== x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    function union(a, b) {
        let ra = find(a), rb = find(b);
        if (ra === rb) return;
        if (rank[ra] < rank[rb]) [ra, rb] = [rb, ra];
        parent[rb] = ra;
        if (rank[ra] === rank[rb]) rank[ra]++;
    }

    for (const [u, v] of connections) {
        union(u, v);
    }

    // members per component (sorted because we iterate i increasing)
    const compMembers = {};
    for (let i = 1; i <= c; i++) {
        const r = find(i);
        if (!compMembers[r]) compMembers[r] = [];
        compMembers[r].push(i);
    }

    // pointer to first online node in each component
    const ptr = {};
    for (const r in compMembers) {
        ptr[r] = 0;
    }

    const online = new Array(c + 1).fill(true);
    const ans = [];

    for (const [type, x] of queries) {
        if (type === 2) { // go offline
            online[x] = false;
        } else { // query
            if (online[x]) {
                ans.push(x);
            } else {
                const r = find(x);
                const arr = compMembers[r];
                let p = ptr[r];
                while (p < arr.length && !online[arr[p]]) p++;
                ptr[r] = p;
                if (p === arr.length) ans.push(-1);
                else ans.push(arr[p]);
            }
        }
    }

    return ans;
};
```

## Typescript

```typescript
function processQueries(c: number, connections: number[][], queries: number[][]): number[] {
    class DSU {
        parent: number[];
        sz: number[];
        constructor(n: number) {
            this.parent = new Array(n + 1);
            this.sz = new Array(n + 1).fill(1);
            for (let i = 0; i <= n; i++) this.parent[i] = i;
        }
        find(x: number): number {
            if (this.parent[x] !== x) this.parent[x] = this.find(this.parent[x]);
            return this.parent[x];
        }
        union(a: number, b: number): void {
            a = this.find(a);
            b = this.find(b);
            if (a === b) return;
            if (this.sz[a] < this.sz[b]) [a, b] = [b, a];
            this.parent[b] = a;
            this.sz[a] += this.sz[b];
        }
    }

    class MinHeap {
        data: number[];
        constructor() { this.data = []; }
        size(): number { return this.data.length; }
        peek(): number { return this.data[0]; }
        push(val: number): void {
            const a = this.data;
            a.push(val);
            let i = a.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (a[p] <= a[i]) break;
                [a[p], a[i]] = [a[i], a[p]];
                i = p;
            }
        }
        pop(): number | undefined {
            const a = this.data;
            if (a.length === 0) return undefined;
            const root = a[0];
            const last = a.pop()!;
            if (a.length > 0) {
                a[0] = last;
                let i = 0;
                while (true) {
                    let l = i * 2 + 1, r = l + 1, smallest = i;
                    if (l < a.length && a[l] < a[smallest]) smallest = l;
                    if (r < a.length && a[r] < a[smallest]) smallest = r;
                    if (smallest === i) break;
                    [a[i], a[smallest]] = [a[smallest], a[i]];
                    i = smallest;
                }
            }
            return root;
        }
    }

    const dsu = new DSU(c);
    for (const [u, v] of connections) {
        dsu.union(u, v);
    }

    const compRoot = new Array(c + 1);
    for (let i = 1; i <= c; i++) compRoot[i] = dsu.find(i);

    const heaps = new Map<number, MinHeap>();
    for (let i = 1; i <= c; i++) {
        const r = compRoot[i];
        let heap = heaps.get(r);
        if (!heap) {
            heap = new MinHeap();
            heaps.set(r, heap);
        }
        heap.push(i);
    }

    const offline = new Array(c + 1).fill(false);
    const ans: number[] = [];

    for (const [type, x] of queries) {
        if (type === 2) {
            offline[x] = true;
        } else { // type === 1
            if (!offline[x]) {
                ans.push(x);
            } else {
                const r = compRoot[x];
                const heap = heaps.get(r)!;
                while (heap.size() > 0 && offline[heap.peek()]) heap.pop();
                if (heap.size() === 0) ans.push(-1);
                else ans.push(heap.peek());
            }
        }
    }

    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $c
     * @param Integer[][] $connections
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function processQueries($c, $connections, $queries) {
        // DSU initialization
        $parent = range(0, $c);
        $rank   = array_fill(0, $c + 1, 0);
        $find = function($x) use (&$parent, &$find) {
            while ($parent[$x] != $x) {
                $parent[$x] = $parent[$parent[$x]];
                $x = $parent[$x];
            }
            return $x;
        };
        $union = function($a, $b) use (&$parent, &$rank, $find) {
            $ra = $find($a);
            $rb = $find($b);
            if ($ra == $rb) return;
            if ($rank[$ra] < $rank[$rb]) {
                $parent[$ra] = $rb;
            } elseif ($rank[$ra] > $rank[$rb]) {
                $parent[$rb] = $ra;
            } else {
                $parent[$rb] = $ra;
                $rank[$ra]++;
            }
        };
        // Build components
        foreach ($connections as $conn) {
            $union($conn[0], $conn[1]);
        }
        // Prepare heaps for each component and online status
        $heaps = [];
        $online = array_fill(0, $c + 1, true);
        for ($i = 1; $i <= $c; $i++) {
            $root = $find($i);
            if (!isset($heaps[$root])) {
                $heaps[$root] = new SplMinHeap();
            }
            $heaps[$root]->insert($i);
        }
        $res = [];
        foreach ($queries as $q) {
            $type = $q[0];
            $x    = $q[1];
            if ($type == 2) { // go offline
                $online[$x] = false;
            } else { // query
                if ($online[$x]) {
                    $res[] = $x;
                } else {
                    $root = $find($x);
                    $heap = $heaps[$root];
                    while (!$heap->isEmpty()) {
                        $top = $heap->top();
                        if ($online[$top]) break;
                        $heap->extract(); // discard offline node
                    }
                    if ($heap->isEmpty()) {
                        $res[] = -1;
                    } else {
                        $res[] = $heap->top();
                    }
                }
            }
        }
        return $res;
    }
}
```

## Swift

```swift
import Foundation

class UnionFind {
    private var parent: [Int]
    private var rank: [Int]

    init(_ size: Int) {
        self.parent = Array(0...size)
        self.rank = Array(repeating: 0, count: size + 1)
    }

    func find(_ x: Int) -> Int {
        if parent[x] != x {
            parent[x] = find(parent[x])
        }
        return parent[x]
    }

    func union(_ a: Int, _ b: Int) {
        var rootA = find(a)
        var rootB = find(b)
        if rootA == rootB { return }
        if rank[rootA] < rank[rootB] {
            parent[rootA] = rootB
        } else if rank[rootA] > rank[rootB] {
            parent[rootB] = rootA
        } else {
            parent[rootB] = rootA
            rank[rootA] += 1
        }
    }
}

class MinHeap {
    private var data: [Int] = []

    func push(_ value: Int) {
        data.append(value)
        siftUp(data.count - 1)
    }

    func peek() -> Int? {
        return data.first
    }

    @discardableResult
    func pop() -> Int? {
        guard !data.isEmpty else { return nil }
        let result = data[0]
        let last = data.removeLast()
        if !data.isEmpty {
            data[0] = last
            siftDown(0)
        }
        return result
    }

    private func siftUp(_ index: Int) {
        var child = index
        while child > 0 {
            let parent = (child - 1) >> 1
            if data[parent] <= data[child] { break }
            data.swapAt(parent, child)
            child = parent
        }
    }

    private func siftDown(_ index: Int) {
        var parent = index
        while true {
            let left = (parent << 1) + 1
            let right = left + 1
            var smallest = parent
            if left < data.count && data[left] < data[smallest] { smallest = left }
            if right < data.count && data[right] < data[smallest] { smallest = right }
            if smallest == parent { break }
            data.swapAt(parent, smallest)
            parent = smallest
        }
    }
}

class Solution {
    func processQueries(_ c: Int, _ connections: [[Int]], _ queries: [[Int]]) -> [Int] {
        let uf = UnionFind(c)
        for conn in connections {
            uf.union(conn[0], conn[1])
        }

        var componentRoot = [Int](repeating: 0, count: c + 1)
        var heaps = [Int: MinHeap]()

        for i in 1...c {
            let root = uf.find(i)
            componentRoot[i] = root
            if heaps[root] == nil { heaps[root] = MinHeap() }
            heaps[root]?.push(i)
        }

        var online = [Bool](repeating: true, count: c + 1)
        var answer: [Int] = []

        for q in queries {
            let type = q[0]
            let x = q[1]

            if type == 2 {
                if online[x] { online[x] = false }
            } else { // type == 1
                if online[x] {
                    answer.append(x)
                } else {
                    let root = componentRoot[x]
                    if let heap = heaps[root] {
                        while let top = heap.peek(), !online[top] {
                            _ = heap.pop()
                        }
                        if let top = heap.peek() {
                            answer.append(top)
                        } else {
                            answer.append(-1)
                        }
                    } else {
                        answer.append(-1)
                    }
                }
            }
        }

        return answer
    }
}
```

## Kotlin

```kotlin
import java.util.*

class Solution {
    private class DSU(n: Int) {
        private val parent = IntArray(n + 1) { it }
        private val rank = IntArray(n + 1)

        fun find(x: Int): Int {
            var v = x
            while (parent[v] != v) {
                parent[v] = parent[parent[v]]
                v = parent[v]
            }
            return v
        }

        fun union(a: Int, b: Int) {
            var x = find(a)
            var y = find(b)
            if (x == y) return
            if (rank[x] < rank[y]) {
                val tmp = x; x = y; y = tmp
            }
            parent[y] = x
            if (rank[x] == rank[y]) rank[x]++
        }
    }

    fun processQueries(c: Int, connections: Array<IntArray>, queries: Array<IntArray>): IntArray {
        val dsu = DSU(c)
        for (conn in connections) {
            dsu.union(conn[0], conn[1])
        }

        val sets = arrayOfNulls<TreeSet<Int>>(c + 1)
        for (i in 1..c) {
            val root = dsu.find(i)
            var set = sets[root]
            if (set == null) {
                set = TreeSet()
                sets[root] = set
            }
            set.add(i)
        }

        var type1Count = 0
        for (q in queries) if (q[0] == 1) type1Count++
        val ans = IntArray(type1Count)
        var idx = 0

        for (q in queries) {
            val type = q[0]
            val x = q[1]
            val root = dsu.find(x)
            val set = sets[root]!!

            if (type == 2) {
                set.remove(x)
            } else { // type == 1
                ans[idx++] = when {
                    set.isEmpty() -> -1
                    set.contains(x) -> x
                    else -> set.first()
                }
            }
        }

        return ans
    }
}
```

## Dart

```dart
import 'dart:collection';

class DSU {
  late List<int> parent;
  late List<int> size;

  DSU(int n) {
    parent = List<int>.generate(n + 1, (i) => i);
    size = List<int>.filled(n + 1, 1);
  }

  int find(int x) {
    if (parent[x] != x) {
      parent[x] = find(parent[x]);
    }
    return parent[x];
  }

  void union(int a, int b) {
    int ra = find(a);
    int rb = find(b);
    if (ra == rb) return;
    if (size[ra] < size[rb]) {
      int tmp = ra;
      ra = rb;
      rb = tmp;
    }
    parent[rb] = ra;
    size[ra] += size[rb];
  }
}

class Solution {
  List<int> processQueries(int c, List<List<int>> connections, List<List<int>> queries) {
    DSU dsu = DSU(c);
    for (var conn in connections) {
      dsu.union(conn[0], conn[1]);
    }

    // component id for each node
    List<int> compId = List.filled(c + 1, 0);
    for (int i = 1; i <= c; ++i) {
      compId[i] = dsu.find(i);
    }

    // map from component root to ordered set of online nodes
    Map<int, SplayTreeSet<int>> sets = {};
    for (int i = 1; i <= c; ++i) {
      int root = compId[i];
      sets.putIfAbsent(root, () => SplayTreeSet<int>());
      sets[root]!.add(i);
    }

    List<int> ans = [];
    for (var q in queries) {
      int type = q[0];
      int x = q[1];
      int root = compId[x];
      var set = sets[root]!;

      if (type == 2) {
        // take offline
        set.remove(x);
      } else { // type == 1
        if (set.contains(x)) {
          ans.add(x);
        } else if (set.isNotEmpty) {
          ans.add(set.first);
        } else {
          ans.add(-1);
        }
      }
    }

    return ans;
  }
}
```

## Golang

```go
import (
	"container/heap"
)

type IntHeap []int

func (h IntHeap) Len() int            { return len(h) }
func (h IntHeap) Less(i, j int) bool  { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *IntHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func processQueries(c int, connections [][]int, queries [][]int) []int {
	adj := make([][]int, c+1)
	for _, e := range connections {
		u, v := e[0], e[1]
		adj[u] = append(adj[u], v)
		adj[v] = append(adj[v], u)
	}

	comp := make([]int, c+1) // 0 means unvisited
	cid := 0
	stack := make([]int, 0)

	for i := 1; i <= c; i++ {
		if comp[i] != 0 {
			continue
		}
		// start new component
		comp[i] = cid
		stack = append(stack, i)
		for len(stack) > 0 {
			v := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			for _, nb := range adj[v] {
				if comp[nb] == 0 {
					comp[nb] = cid
					stack = append(stack, nb)
				}
			}
		}
		cid++
	}

	numComp := cid
	heaps := make([]*IntHeap, numComp)
	for i := 0; i < numComp; i++ {
		h := &IntHeap{}
		heap.Init(h)
		heaps[i] = h
	}
	for node := 1; node <= c; node++ {
		id := comp[node]
		heap.Push(heaps[id], node)
	}

	offline := make([]bool, c+1)
	ans := make([]int, 0, len(queries))

	for _, q := range queries {
		t, x := q[0], q[1]
		if t == 2 { // take offline
			if !offline[x] {
				offline[x] = true
			}
		} else { // query
			if !offline[x] {
				ans = append(ans, x)
				continue
			}
			id := comp[x]
			h := heaps[id]
			for h.Len() > 0 && offline[(*h)[0]] {
				heap.Pop(h)
			}
			if h.Len() == 0 {
				ans = append(ans, -1)
			} else {
				ans = append(ans, (*h)[0])
			}
		}
	}

	return ans
}
```

## Ruby

```ruby
class MinHeap
  def initialize
    @data = []
  end

  def push(val)
    i = @data.size
    @data << val
    while i > 0
      p = (i - 1) / 2
      break if @data[p] <= @data[i]
      @data[p], @data[i] = @data[i], @data[p]
      i = p
    end
  end

  def top
    @data[0]
  end

  def pop
    return nil if @data.empty?
    min = @data[0]
    last = @data.pop
    unless @data.empty?
      @data[0] = last
      i = 0
      size = @data.size
      loop do
        l = i * 2 + 1
        r = l + 1
        break if l >= size
        smallest = l
        smallest = r if r < size && @data[r] < @data[l]
        break if @data[i] <= @data[smallest]
        @data[i], @data[smallest] = @data[smallest], @data[i]
        i = smallest
      end
    end
    min
  end

  def empty?
    @data.empty?
  end
end

# @param {Integer} c
# @param {Integer[][]} connections
# @param {Integer[][]} queries
# @return {Integer[]}
def process_queries(c, connections, queries)
  adj = Array.new(c + 1) { [] }
  connections.each do |u, v|
    adj[u] << v
    adj[v] << u
  end

  comp = Array.new(c + 1, -1)
  comp_id = 0
  (1..c).each do |i|
    next if comp[i] != -1
    stack = [i]
    comp[i] = comp_id
    until stack.empty?
      node = stack.pop
      adj[node].each do |nbr|
        if comp[nbr] == -1
          comp[nbr] = comp_id
          stack << nbr
        end
      end
    end
    comp_id += 1
  end

  heaps = Array.new(comp_id) { MinHeap.new }
  (1..c).each do |i|
    heaps[comp[i]].push(i)
  end

  online = Array.new(c + 1, true)
  result = []

  queries.each do |type, x|
    if type == 2
      next unless online[x]
      online[x] = false
    else # type == 1
      if online[x]
        result << x
      else
        heap = heaps[comp[x]]
        while !heap.empty? && !online[heap.top]
          heap.pop
        end
        if heap.empty?
          result << -1
        else
          result << heap.top
        end
      end
    end
  end

  result
end
```

## Scala

```scala
object Solution {
  def processQueries(c: Int, connections: Array[Array[Int]], queries: Array[Array[Int]]): Array[Int] = {
    val parent = new Array[Int](c + 1)
    val rank = new Array[Int](c + 1)
    for (i <- 1 to c) parent(i) = i

    def find(x: Int): Int = {
      if (parent(x) != x) parent(x) = find(parent(x))
      parent(x)
    }

    def union(a: Int, b: Int): Unit = {
      var ra = find(a)
      var rb = find(b)
      if (ra == rb) return
      if (rank(ra) < rank(rb)) {
        parent(ra) = rb
      } else if (rank(ra) > rank(rb)) {
        parent(rb) = ra
      } else {
        parent(rb) = ra
        rank(ra) += 1
      }
    }

    for (conn <- connections) union(conn(0), conn(1))

    import java.util.TreeSet
    val compMap = scala.collection.mutable.HashMap[Int, TreeSet[Int]]()
    for (i <- 1 to c) {
      val r = find(i)
      val set = compMap.getOrElseUpdate(r, new TreeSet[Int]())
      set.add(i)
    }

    val ans = scala.collection.mutable.ArrayBuffer[Int]()
    for (q <- queries) {
      q(0) match {
        case 1 =>
          val x = q(1)
          val r = find(x)
          val set = compMap(r)
          if (set.contains(x)) ans += x
          else if (set.isEmpty) ans += -1
          else ans += set.first()
        case 2 =>
          val x = q(1)
          val r = find(x)
          val set = compMap(r)
          set.remove(x)
      }
    }
    ans.toArray
  }
}
```

## Rust

```rust
use std::collections::BTreeSet;

struct DSU {
    parent: Vec<usize>,
    size: Vec<usize>,
}
impl DSU {
    fn new(n: usize) -> Self {
        let mut parent = Vec::with_capacity(n);
        for i in 0..n {
            parent.push(i);
        }
        DSU { parent, size: vec![1; n] }
    }
    fn find(&mut self, x: usize) -> usize {
        if self.parent[x] != x {
            let root = self.find(self.parent[x]);
            self.parent[x] = root;
        }
        self.parent[x]
    }
    fn union(&mut self, a: usize, b: usize) {
        let mut ra = self.find(a);
        let mut rb = self.find(b);
        if ra == rb {
            return;
        }
        if self.size[ra] < self.size[rb] {
            std::mem::swap(&mut ra, &mut rb);
        }
        self.parent[rb] = ra;
        self.size[ra] += self.size[rb];
    }
}

impl Solution {
    pub fn process_queries(c: i32, connections: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = c as usize;
        let mut dsu = DSU::new(n);
        for conn in connections.iter() {
            let u = (conn[0] - 1) as usize;
            let v = (conn[1] - 1) as usize;
            dsu.union(u, v);
        }

        // component root per node and sets of online stations
        let mut comp_root = vec![0usize; n];
        let mut sets: Vec<BTreeSet<i32>> = (0..n).map(|_| BTreeSet::new()).collect();

        for i in 0..n {
            let r = dsu.find(i);
            comp_root[i] = r;
            sets[r].insert((i + 1) as i32);
        }

        let mut ans = Vec::new();
        for q in queries.iter() {
            let typ = q[0];
            let x = q[1] as usize; // station id (1‑based)
            let root = comp_root[x - 1];
            if typ == 2 {
                sets[root].remove(&(x as i32));
            } else {
                let set = &sets[root];
                if set.contains(&(x as i32)) {
                    ans.push(x as i32);
                } else if !set.is_empty() {
                    let min_val = *set.iter().next().unwrap();
                    ans.push(min_val);
                } else {
                    ans.push(-1);
                }
            }
        }

        ans
    }
}
```

## Racket

```racket
(require racket/priority-queue)

(define/contract (process-queries c connections queries)
  (-> exact-integer?
      (listof (listof exact-integer?))
      (listof (listof exact-integer?))
      (listof exact-integer?))
  ;; Disjoint Set Union
  (let* ([parent (make-vector (+ c 1) 0)]
         [rank   (make-vector (+ c 1) 0)])
    (for ([i (in-range 1 (+ c 1))])
      (vector-set! parent i i))

    (define (find x)
      (let loop ([x x])
        (let ([p (vector-ref parent x)])
          (if (= p x)
              x
              (let ([root (loop p)])
                (vector-set! parent x root)
                root)))))

    (define (union a b)
      (let* ([ra (find a)]
             [rb (find b)])
        (when (not (= ra rb))
          (let ([rank-a (vector-ref rank ra)]
                [rank-b (vector-ref rank rb)])
            (cond
              [(< rank-a rank-b) (vector-set! parent ra rb)]
              [(> rank-a rank-b) (vector-set! parent rb ra)]
              [else
               (vector-set! parent rb ra)
               (vector-set! rank ra (+ rank-a 1))])))))

    ;; Build components
    (for ([e connections])
      (match e
        [(list u v) (union u v)]))

    (define roots (make-vector (+ c 1) 0))
    (for ([i (in-range 1 (+ c 1))])
      (vector-set! roots i (find i)))

    ;; Priority queues per component
    (define comp-pq (make-hash))
    (for ([i (in-range 1 (+ c 1))])
      (let* ([r (vector-ref roots i)]
             [pq (hash-ref comp-pq r
                           (lambda ()
                             (let ([new (make-pq <)])
                               (hash-set! comp-pq r new)
                               new)))])
        (pq-add! pq i)))

    ;; Offline status
    (define offline (make-vector (+ c 1) #f))

    ;; Process queries
    (define results '())
    (for ([q queries])
      (match q
        [(list type x)
         (cond
           [(= type 2)
            (vector-set! offline x #t)]
           [(= type 1)
            (if (not (vector-ref offline x))
                (set! results (cons x results))
                (let* ([r (vector-ref roots x)]
                       [pq (hash-ref comp-pq r)])
                  (let loop ()
                    (when (and (not (pq-empty? pq))
                               (vector-ref offline (pq-min pq)))
                      (pq-pop! pq)
                      (loop)))
                  (if (pq-empty? pq)
                      (set! results (cons -1 results))
                      (set! results (cons (pq-min pq) results))))))])))

    (reverse results)))
```

## Erlang

```erlang
-module(solution).
-export([process_queries/3]).

process_queries(C, Connections, Queries) ->
    Adj = build_adj(Connections, #{}),
    {CompMap, CompNodes} = assign_components(lists:seq(1, C), Adj),
    Trees0 = build_trees(CompNodes),
    ResultsRev = process_queries_loop(Queries, CompMap, Trees0, []),
    lists:reverse(ResultsRev).

build_adj([], Adj) -> Adj;
build_adj([[U,V]|Rest], Adj) ->
    Adj1 = maps:update_with(U,
            fun(L) -> [V|L] end,
            [V],
            Adj),
    Adj2 = maps:update_with(V,
            fun(L) -> [U|L] end,
            [U],
            Adj1),
    build_adj(Rest, Adj2).

assign_components(Nodes, Adj) ->
    assign_components(Nodes, Adj, #{}, #{}, #{}).

assign_components([], _Adj, _Visited, CompMap, CompNodes) ->
    {CompMap, CompNodes};
assign_components([Node|Rest], Adj, Visited, CompMap, CompNodes) ->
    case maps:is_key(Node, Visited) of
        true ->
            assign_components(Rest, Adj, Visited, CompMap, CompNodes);
        false ->
            {Visited1, CompMap1, CompNodes1} = bfs([Node], Node, Adj, Visited, CompMap, CompNodes),
            assign_components(Rest, Adj, Visited1, CompMap1, CompNodes1)
    end.

bfs([], _CompId, _Adj, Visited, CompMap, CompNodes) ->
    {Visited, CompMap, CompNodes};
bfs([Curr|Stack], CompId, Adj, Visited, CompMap, CompNodes) ->
    case maps:is_key(Curr, Visited) of
        true ->
            bfs(Stack, CompId, Adj, Visited, CompMap, CompNodes);
        false ->
            Visited1 = maps:put(Curr, true, Visited),
            CompMap1 = maps:put(Curr, CompId, CompMap),
            CompNodes1 = maps:update_with(CompId,
                                          fun(L) -> [Curr|L] end,
                                          [Curr],
                                          CompNodes),
            Neighs = maps:get(Curr, Adj, []),
            NewStack = lists:foldl(fun(Nb, Acc) ->
                                        case maps:is_key(Nb, Visited1) of
                                            true -> Acc;
                                            false -> [Nb|Acc]
                                        end
                                   end, Stack, Neighs),
            bfs(NewStack, CompId, Adj, Visited1, CompMap1, CompNodes1)
    end.

build_trees(CompNodes) ->
    maps:fold(fun(CompId, NodeList, Acc) ->
        Tree = lists:foldl(fun(Node, T) -> gb_trees:insert(Node, true, T) end,
                           gb_trees:empty(),
                           NodeList),
        maps:put(CompId, Tree, Acc)
    end, #{}, CompNodes).

process_queries_loop([], _CompMap, _Trees, Acc) ->
    Acc;
process_queries_loop([[Type,X]|Rest], CompMap, Trees, Acc) ->
    case Type of
        2 ->
            CompId = maps:get(X, CompMap),
            Tree0 = maps:get(CompId, Trees),
            Tree1 = case gb_trees:is_defined(X, Tree0) of
                        true -> gb_trees:delete(X, Tree0);
                        false -> Tree0
                    end,
            Trees1 = maps:put(CompId, Tree1, Trees),
            process_queries_loop(Rest, CompMap, Trees1, Acc);
        1 ->
            CompId = maps:get(X, CompMap),
            Tree = maps:get(CompId, Trees),
            Result =
                case gb_trees:is_defined(X, Tree) of
                    true -> X;
                    false ->
                        case gb_trees:is_empty(Tree) of
                            true -> -1;
                            false ->
                                {MinKey,_} = gb_trees:smallest(Tree),
                                MinKey
                        end
                end,
            process_queries_loop(Rest, CompMap, Trees, [Result|Acc])
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec process_queries(c :: integer, connections :: [[integer]], queries :: [[integer]]) :: [integer]
  def process_queries(c, connections, queries) do
    # Build adjacency map
    adj =
      Enum.reduce(connections, %{}, fn [u, v], acc ->
        acc = Map.update(acc, u, [v], fn lst -> [v | lst] end)
        Map.update(acc, v, [u], fn lst -> [u | lst] end)
      end)

    # Find components and assign component ids
    {comp_array, _visited, comp_cnt} =
      1..c
      |> Enum.reduce({:array.new(c + 1, default: 0), MapSet.new(), 0}, fn node,
                                                                      {arr, visited, cnt} ->
        if MapSet.member?(visited, node) do
          {arr, visited, cnt}
        else
          cid = cnt + 1
          {new_arr, new_visited} = dfs([node], adj, visited, cid, arr)
          {new_arr, new_visited, cid}
        end
      end)

    # Build sorted sets of online stations per component
    comp_sets =
      1..c
      |> Enum.reduce(%{}, fn node, acc ->
        cid = :array.get(comp_array, node)
        set = Map.get(acc, cid, :gb_sets.empty())
        Map.put(acc, cid, :gb_sets.add(node, set))
      end)

    # Process queries
    {_, results_rev} =
      Enum.reduce(queries, {comp_sets, []}, fn [type, x], {sets, res_acc} ->
        cid = :array.get(comp_array, x)
        set = Map.get(sets, cid)

        if type == 2 do
          new_set = :gb_sets.delete(x, set)
          {Map.put(sets, cid, new_set), res_acc}
        else
          answer =
            if :gb_sets.member(x, set) do
              x
            else
              if :gb_sets.is_empty(set) do
                -1
              else
                :gb_sets.smallest(set)
              end
            end

          {sets, [answer | res_acc]}
        end
      end)

    Enum.reverse(results_rev)
  end

  # Depth‑first search to assign component ids
  defp dfs([], _adj, visited, _cid, arr), do: {arr, visited}

  defp dfs([node | stack], adj, visited, cid, arr) do
    if MapSet.member?(visited, node) do
      dfs(stack, adj, visited, cid, arr)
    else
      visited = MapSet.put(visited, node)
      arr = :array.set(arr, node, cid)
      neighbors = Map.get(adj, node, [])
      new_stack = Enum.reduce(neighbors, stack, fn nb, acc -> [nb | acc] end)
      dfs(new_stack, adj, visited, cid, arr)
    end
  end
end
```
