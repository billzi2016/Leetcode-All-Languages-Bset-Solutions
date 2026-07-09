# 0699. Falling Squares

## Cpp

```cpp
class Solution {
public:
    struct SegTree {
        int n;
        std::vector<int> tree, lazy;
        SegTree(int sz) : n(sz), tree(4 * sz, 0), lazy(4 * sz, -1) {}
        void push(int node, int l, int r) {
            if (lazy[node] != -1) {
                tree[node] = lazy[node];
                if (l != r) { // not leaf
                    lazy[node << 1] = lazy[node];
                    lazy[node << 1 | 1] = lazy[node];
                }
                lazy[node] = -1;
            }
        }
        int query(int node, int l, int r, int ql, int qr) {
            push(node, l, r);
            if (qr < l || ql > r) return 0;
            if (ql <= l && r <= qr) return tree[node];
            int mid = (l + r) >> 1;
            return std::max(query(node << 1, l, mid, ql, qr),
                            query(node << 1 | 1, mid + 1, r, ql, qr));
        }
        void update(int node, int l, int r, int ul, int ur, int val) {
            if (ur < l || ul > r) return;
            if (ul <= l && r <= ur) {
                lazy[node] = val;
                push(node, l, r);
                return;
            }
            push(node, l, r);
            int mid = (l + r) >> 1;
            update(node << 1, l, mid, ul, ur, val);
            update(node << 1 | 1, mid + 1, r, ul, ur, val);
            tree[node] = std::max(tree[node << 1], tree[node << 1 | 1]);
        }
    };
    
    vector<int> fallingSquares(vector<vector<int>>& positions) {
        int n = positions.size();
        vector<long long> coords;
        coords.reserve(2 * n);
        for (auto &p : positions) {
            long long l = p[0];
            long long r = (long long)p[0] + p[1];
            coords.push_back(l);
            coords.push_back(r);
        }
        sort(coords.begin(), coords.end());
        coords.erase(unique(coords.begin(), coords.end()), coords.end());
        int m = coords.size();
        if (m <= 1) return {};
        SegTree seg(m - 1); // intervals between points
        
        vector<int> ans;
        ans.reserve(n);
        int curMax = 0;
        for (auto &p : positions) {
            long long l = p[0];
            long long r = (long long)p[0] + p[1];
            int leftIdx = lower_bound(coords.begin(), coords.end(), l) - coords.begin();
            int rightIdx = lower_bound(coords.begin(), coords.end(), r) - coords.begin() - 1;
            int prevHeight = seg.query(1, 0, m - 2, leftIdx, rightIdx);
            int newHeight = prevHeight + p[1];
            seg.update(1, 0, m - 2, leftIdx, rightIdx, newHeight);
            curMax = max(curMax, newHeight);
            ans.push_back(curMax);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public java.util.List<Integer> fallingSquares(int[][] positions) {
        int n = positions.length;
        java.util.Set<Integer> set = new java.util.HashSet<>();
        for (int[] p : positions) {
            int left = p[0];
            int right = p[0] + p[1];
            set.add(left);
            set.add(right);
        }
        java.util.List<Integer> coordsList = new java.util.ArrayList<>(set);
        java.util.Collections.sort(coordsList);
        java.util.Map<Integer, Integer> idxMap = new java.util.HashMap<>();
        for (int i = 0; i < coordsList.size(); i++) {
            idxMap.put(coordsList.get(i), i);
        }
        int segCount = coordsList.size() - 1; // number of elementary intervals
        if (segCount <= 0) {
            java.util.List<Integer> ans = new java.util.ArrayList<>();
            for (int[] p : positions) ans.add(p[1]);
            return ans;
        }
        SegmentTree st = new SegmentTree(segCount);
        java.util.List<Integer> result = new java.util.ArrayList<>(n);
        int curMax = 0;
        for (int[] p : positions) {
            int left = p[0];
            int size = p[1];
            int right = left + size;
            int l = idxMap.get(left);
            int r = idxMap.get(right) - 1; // inclusive index in segment tree
            int baseHeight = st.query(l, r);
            int newHeight = baseHeight + size;
            st.update(l, r, newHeight);
            curMax = Math.max(curMax, newHeight);
            result.add(curMax);
        }
        return result;
    }

    private static class SegmentTree {
        int n;
        int[] tree;
        int[] lazy; // pending assignment (0 means none)

        SegmentTree(int size) {
            this.n = size;
            tree = new int[4 * n];
            lazy = new int[4 * n];
        }

        void push(int node, int l, int r) {
            if (lazy[node] != 0) {
                tree[node] = lazy[node];
                if (l != r) {
                    lazy[node << 1] = lazy[node];
                    lazy[(node << 1) | 1] = lazy[node];
                }
                lazy[node] = 0;
            }
        }

        int query(int ql, int qr) {
            return query(1, 0, n - 1, ql, qr);
        }

        private int query(int node, int l, int r, int ql, int qr) {
            push(node, l, r);
            if (qr < l || r < ql) return 0;
            if (ql <= l && r <= qr) return tree[node];
            int mid = (l + r) >>> 1;
            return Math.max(query(node << 1, l, mid, ql, qr),
                            query((node << 1) | 1, mid + 1, r, ql, qr));
        }

        void update(int ul, int ur, int val) {
            update(1, 0, n - 1, ul, ur, val);
        }

        private void update(int node, int l, int r, int ul, int ur, int val) {
            push(node, l, r);
            if (ur < l || r < ul) return;
            if (ul <= l && r <= ur) {
                lazy[node] = val;
                push(node, l, r);
                return;
            }
            int mid = (l + r) >>> 1;
            update(node << 1, l, mid, ul, ur, val);
            update((node << 1) | 1, mid + 1, r, ul, ur, val);
            tree[node] = Math.max(tree[node << 1], tree[(node << 1) | 1]);
        }
    }
}
```

## Python

```python
class Solution(object):
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        # coordinate compression
        coords = set()
        for left, size in positions:
            coords.add(left)
            coords.add(left + size)
        xs = sorted(coords)
        idx = {x: i for i, x in enumerate(xs)}
        n = len(xs) - 1  # number of elementary intervals

        class SegTree:
            __slots__ = ('N', 'tree', 'lazy')
            def __init__(self, size):
                N = 1
                while N < size:
                    N <<= 1
                self.N = N
                self.tree = [0] * (2 * N)
                self.lazy = [None] * (2 * N)

            def _push(self, node):
                val = self.lazy[node]
                if val is not None:
                    left = node << 1
                    right = left | 1
                    self.tree[left] = val
                    self.tree[right] = val
                    self.lazy[left] = val
                    self.lazy[right] = val
                    self.lazy[node] = None

            def query(self, l, r, node, nl, nr):
                if r < nl or nr < l:
                    return 0
                if l <= nl and nr <= r:
                    return self.tree[node]
                self._push(node)
                mid = (nl + nr) >> 1
                left_max = self.query(l, r, node << 1, nl, mid)
                right_max = self.query(l, r, (node << 1) | 1, mid + 1, nr)
                return left_max if left_max >= right_max else right_max

            def update(self, l, r, val, node, nl, nr):
                if r < nl or nr < l:
                    return
                if l <= nl and nr <= r:
                    self.tree[node] = val
                    self.lazy[node] = val
                    return
                self._push(node)
                mid = (nl + nr) >> 1
                self.update(l, r, val, node << 1, nl, mid)
                self.update(l, r, val, (node << 1) | 1, mid + 1, nr)
                left_val = self.tree[node << 1]
                right_val = self.tree[(node << 1) | 1]
                self.tree[node] = left_val if left_val >= right_val else right_val

        seg = SegTree(n)
        ans = []
        cur_max = 0
        for left, size in positions:
            l = idx[left]
            r = idx[left + size] - 1
            base_height = seg.query(l, r, 1, 0, seg.N - 1)
            new_h = base_height + size
            seg.update(l, r, new_h, 1, 0, seg.N - 1)
            cur_max = cur_max if cur_max >= new_h else new_h
            ans.append(cur_max)
        return ans
```

## Python3

```python
class Solution:
    def fallingSquares(self, positions):
        from bisect import bisect_left
        # collect unique coordinates
        coords = []
        for left, size in positions:
            coords.append(left)
            coords.append(left + size)
        xs = sorted(set(coords))
        idx = {x: i for i, x in enumerate(xs)}
        m = len(xs) - 1  # number of elementary intervals
        if m <= 0:
            return [size for _, size in positions]

        class SegTree:
            __slots__ = ('n', 'tree', 'lazy')
            def __init__(self, n):
                self.n = n
                self.tree = [0] * (4 * n)
                self.lazy = [0] * (4 * n)

            def _push(self, node):
                if self.lazy[node]:
                    val = self.lazy[node]
                    left = node << 1
                    right = left | 1
                    self.tree[left] = val
                    self.tree[right] = val
                    self.lazy[left] = val
                    self.lazy[right] = val
                    self.lazy[node] = 0

            def update(self, node, l, r, ql, qr, val):
                if ql > r or qr < l:
                    return
                if ql <= l and r <= qr:
                    self.tree[node] = val
                    self.lazy[node] = val
                    return
                self._push(node)
                mid = (l + r) >> 1
                self.update(node << 1, l, mid, ql, qr, val)
                self.update((node << 1) | 1, mid + 1, r, ql, qr, val)
                self.tree[node] = max(self.tree[node << 1], self.tree[(node << 1) | 1])

            def query(self, node, l, r, ql, qr):
                if ql > r or qr < l:
                    return 0
                if ql <= l and r <= qr:
                    return self.tree[node]
                self._push(node)
                mid = (l + r) >> 1
                left_max = self.query(node << 1, l, mid, ql, qr)
                right_max = self.query((node << 1) | 1, mid + 1, r, ql, qr)
                return max(left_max, right_max)

        seg = SegTree(m)
        res = []
        cur = 0
        for left, size in positions:
            l = idx[left]
            r = idx[left + size] - 1
            base = seg.query(1, 0, m - 1, l, r)
            h = base + size
            seg.update(1, 0, m - 1, l, r, h)
            cur = max(cur, h)
            res.append(cur)
        return res
```

## C

```c
#include <stdlib.h>

int* fallingSquares(int** positions, int positionsSize, int* positionsColSize, int* returnSize) {
    *returnSize = positionsSize;
    int *ans = (int *)malloc(sizeof(int) * positionsSize);
    if (!ans) return NULL;

    int *heights = (int *)malloc(sizeof(int) * positionsSize);
    if (!heights) {
        free(ans);
        return NULL;
    }

    int maxHeight = 0;
    for (int i = 0; i < positionsSize; ++i) {
        long left = positions[i][0];
        long size = positions[i][1];
        long right = left + size;               // exclusive right bound
        int base = 0;

        for (int j = 0; j < i; ++j) {
            long l2 = positions[j][0];
            long r2 = l2 + positions[j][1];
            if (!(right <= l2 || left >= r2)) { // intervals overlap with positive length
                if (heights[j] > base)
                    base = heights[j];
            }
        }

        int curHeight = base + (int)size;
        heights[i] = curHeight;

        if (curHeight > maxHeight)
            maxHeight = curHeight;
        ans[i] = maxHeight;
    }

    free(heights);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public IList<int> FallingSquares(int[][] positions) {
        var coords = new List<long>();
        foreach (var p in positions) {
            long l = p[0];
            long r = l + p[1];
            coords.Add(l);
            coords.Add(r);
        }
        coords.Sort();
        // deduplicate
        var uniq = new List<long>();
        long prev = long.MinValue;
        foreach (var x in coords) {
            if (x != prev) {
                uniq.Add(x);
                prev = x;
            }
        }
        int m = uniq.Count;
        if (m == 0) return new List<int>();

        // map coordinate to index
        var idxMap = new Dictionary<long, int>(m);
        for (int i = 0; i < m; i++) {
            idxMap[uniq[i]] = i;
        }

        int segN = m - 1; // number of intervals
        if (segN <= 0) {
            // all squares have zero width, which cannot happen per constraints
            var resZero = new List<int>();
            foreach (var p in positions) {
                resZero.Add(p[1]);
            }
            return resZero;
        }

        int[] tree = new int[4 * segN];
        int[] lazy = new int[4 * segN];
        for (int i = 0; i < lazy.Length; i++) lazy[i] = -1;

        int Query(int node, int l, int r, int ql, int qr) {
            if (ql > r || qr < l) return 0;
            if (ql <= l && r <= qr) return tree[node];
            Push(node);
            int mid = (l + r) >> 1;
            int leftMax = Query(node << 1, l, mid, ql, qr);
            int rightMax = Query((node << 1) | 1, mid + 1, r, ql, qr);
            return Math.Max(leftMax, rightMax);
        }

        void Update(int node, int l, int r, int ul, int ur, int val) {
            if (ul > r || ur < l) return;
            if (ul <= l && r <= ur) {
                tree[node] = val;
                lazy[node] = val;
                return;
            }
            Push(node);
            int mid = (l + r) >> 1;
            Update(node << 1, l, mid, ul, ur, val);
            Update((node << 1) | 1, mid + 1, r, ul, ur, val);
            tree[node] = Math.Max(tree[node << 1], tree[(node << 1) | 1]);
        }

        void Push(int node) {
            if (lazy[node] != -1) {
                int v = lazy[node];
                lazy[node << 1] = v;
                lazy[(node << 1) | 1] = v;
                tree[node << 1] = v;
                tree[(node << 1) | 1] = v;
                lazy[node] = -1;
            }
        }

        var result = new List<int>();
        int curMax = 0;
        foreach (var p in positions) {
            long l = p[0];
            long r = l + p[1];
            int li = idxMap[l];
            int ri = idxMap[r] - 1; // inclusive interval index
            int baseHeight = Query(1, 0, segN - 1, li, ri);
            int newHeight = baseHeight + p[1];
            Update(1, 0, segN - 1, li, ri, newHeight);
            curMax = Math.Max(curMax, newHeight);
            result.Add(curMax);
        }
        return result;
    }
}
```

## Javascript

```javascript
var fallingSquares = function(positions) {
    const n = positions.length;
    const coords = [];
    for (let i = 0; i < n; i++) {
        const left = positions[i][0];
        const right = left + positions[i][1];
        coords.push(left, right);
    }
    coords.sort((a, b) => a - b);
    const uniq = [];
    for (const v of coords) {
        if (uniq.length === 0 || uniq[uniq.length - 1] !== v) uniq.push(v);
    }
    const m = uniq.length;
    if (m === 0) return [];
    const indexMap = new Map();
    for (let i = 0; i < m; i++) indexMap.set(uniq[i], i);
    const segCount = m - 1; // number of elementary intervals
    const tree = new Array(segCount * 4).fill(0);
    const lazy = new Array(segCount * 4).fill(null);
    function push(node) {
        if (lazy[node] !== null) {
            const val = lazy[node];
            const leftChild = node << 1;
            const rightChild = leftChild | 1;
            tree[leftChild] = val;
            tree[rightChild] = val;
            lazy[leftChild] = val;
            lazy[rightChild] = val;
            lazy[node] = null;
        }
    }
    function query(node, l, r, ql, qr) {
        if (ql > r || qr < l) return 0;
        if (ql <= l && r <= qr) return tree[node];
        push(node);
        const mid = (l + r) >> 1;
        const leftMax = query(node << 1, l, mid, ql, qr);
        const rightMax = query((node << 1) | 1, mid + 1, r, ql, qr);
        return leftMax > rightMax ? leftMax : rightMax;
    }
    function update(node, l, r, ul, ur, val) {
        if (ul > r || ur < l) return;
        if (ul <= l && r <= ur) {
            tree[node] = val;
            lazy[node] = val;
            return;
        }
        push(node);
        const mid = (l + r) >> 1;
        update(node << 1, l, mid, ul, ur, val);
        update((node << 1) | 1, mid + 1, r, ul, ur, val);
        tree[node] = tree[node << 1] > tree[(node << 1) | 1] ? tree[node << 1] : tree[(node << 1) | 1];
    }
    const result = [];
    let curMax = 0;
    for (let i = 0; i < n; i++) {
        const left = positions[i][0];
        const size = positions[i][1];
        const right = left + size;
        const lIdx = indexMap.get(left);
        const rIdx = indexMap.get(right) - 1; // inclusive
        const baseHeight = query(1, 0, segCount - 1, lIdx, rIdx);
        const newHeight = baseHeight + size;
        update(1, 0, segCount - 1, lIdx, rIdx, newHeight);
        curMax = Math.max(curMax, newHeight);
        result.push(curMax);
    }
    return result;
};
```

## Typescript

```typescript
function fallingSquares(positions: number[][]): number[] {
    // Collect all unique coordinates (left and right edges)
    const coordSet = new Set<number>();
    for (const [l, size] of positions) {
        coordSet.add(l);
        coordSet.add(l + size);
    }
    const coords = Array.from(coordSet).sort((a, b) => a - b);
    const indexMap = new Map<number, number>();
    for (let i = 0; i < coords.length; i++) {
        indexMap.set(coords[i], i);
    }

    // Number of elementary segments between consecutive coordinates
    const segCount = Math.max(0, coords.length - 1);
    if (segCount === 0) return [];

    class SegmentTree {
        n: number;
        tree: number[];
        lazy: (number | null)[];
        constructor(n: number) {
            this.n = n;
            const size = 4 * n;
            this.tree = new Array(size).fill(0);
            this.lazy = new Array(size).fill(null);
        }
        private push(node: number, l: number, r: number): void {
            const val = this.lazy[node];
            if (val !== null && l !== r) {
                const left = node << 1;
                const right = left | 1;
                this.tree[left] = val;
                this.tree[right] = val;
                this.lazy[left] = val;
                this.lazy[right] = val;
                this.lazy[node] = null;
            }
        }
        private update(node: number, l: number, r: number, ql: number, qr: number, val: number): void {
            if (ql > r || qr < l) return;
            if (ql <= l && r <= qr) {
                this.tree[node] = val;
                this.lazy[node] = val;
                return;
            }
            this.push(node, l, r);
            const mid = (l + r) >> 1;
            this.update(node << 1, l, mid, ql, qr, val);
            this.update((node << 1) | 1, mid + 1, r, ql, qr, val);
            this.tree[node] = Math.max(this.tree[node << 1], this.tree[(node << 1) | 1]);
        }
        private query(node: number, l: number, r: number, ql: number, qr: number): number {
            if (ql > r || qr < l) return 0;
            if (ql <= l && r <= qr) return this.tree[node];
            this.push(node, l, r);
            const mid = (l + r) >> 1;
            return Math.max(
                this.query(node << 1, l, mid, ql, qr),
                this.query((node << 1) | 1, mid + 1, r, ql, qr)
            );
        }
        rangeUpdate(l: number, r: number, val: number): void {
            this.update(1, 0, this.n - 1, l, r, val);
        }
        rangeQuery(l: number, r: number): number {
            return this.query(1, 0, this.n - 1, l, r);
        }
    }

    const segTree = new SegmentTree(segCount);
    const result: number[] = [];
    let currentMax = 0;

    for (const [left, size] of positions) {
        const lIdx = indexMap.get(left)!;
        const rIdxExclusive = indexMap.get(left + size)!; // exclusive right index in coords
        const rIdx = rIdxExclusive - 1; // inclusive leaf index

        const baseHeight = segTree.rangeQuery(lIdx, rIdx);
        const newHeight = baseHeight + size;
        segTree.rangeUpdate(lIdx, rIdx, newHeight);

        currentMax = Math.max(currentMax, newHeight);
        result.push(currentMax);
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $positions
     * @return Integer[]
     */
    function fallingSquares($positions) {
        $coords = [];
        foreach ($positions as $p) {
            $left = $p[0];
            $size = $p[1];
            $coords[] = $left;
            $coords[] = $left + $size;
        }
        sort($coords);
        // deduplicate
        $unique = [];
        $prev = null;
        foreach ($coords as $c) {
            if ($prev === null || $c !== $prev) {
                $unique[] = $c;
                $prev = $c;
            }
        }

        $coordIndex = [];
        foreach ($unique as $i => $c) {
            $coordIndex[$c] = $i;
        }

        $segmentCount = count($unique) - 1;
        if ($segmentCount < 0) {
            $segmentCount = 0;
        }
        $heights = array_fill(0, $segmentCount, 0);
        $ans = [];
        $globalMax = 0;

        foreach ($positions as $p) {
            $left = $p[0];
            $size = $p[1];
            $right = $left + $size;
            $lIdx = $coordIndex[$left];
            $rIdx = $coordIndex[$right]; // exclusive

            $maxH = 0;
            for ($i = $lIdx; $i < $rIdx; $i++) {
                if ($heights[$i] > $maxH) {
                    $maxH = $heights[$i];
                }
            }

            $newHeight = $maxH + $size;
            for ($i = $lIdx; $i < $rIdx; $i++) {
                $heights[$i] = $newHeight;
            }

            if ($newHeight > $globalMax) {
                $globalMax = $newHeight;
            }
            $ans[] = $globalMax;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func fallingSquares(_ positions: [[Int]]) -> [Int] {
        var coordSet = Set<Int>()
        for p in positions {
            let left = p[0]
            let size = p[1]
            coordSet.insert(left)
            coordSet.insert(left + size)
        }
        let sortedCoords = coordSet.sorted()
        var indexMap = [Int: Int]()
        for (i, v) in sortedCoords.enumerated() {
            indexMap[v] = i
        }
        let intervalCount = max(0, sortedCoords.count - 1)
        if intervalCount == 0 { return [] }
        var segMax = Array(repeating: 0, count: 4 * intervalCount)
        var lazy = Array(repeating: 0, count: 4 * intervalCount)

        func push(_ node: Int) {
            let val = lazy[node]
            if val != 0 {
                let leftChild = node << 1
                let rightChild = leftChild | 1
                segMax[leftChild] = val
                segMax[rightChild] = val
                lazy[leftChild] = val
                lazy[rightChild] = val
                lazy[node] = 0
            }
        }

        func query(_ node: Int, _ l: Int, _ r: Int, _ ql: Int, _ qr: Int) -> Int {
            if ql > r || qr < l { return 0 }
            if ql <= l && r <= qr { return segMax[node] }
            push(node)
            let mid = (l + r) >> 1
            let leftRes = query(node << 1, l, mid, ql, qr)
            let rightRes = query((node << 1) | 1, mid + 1, r, ql, qr)
            return max(leftRes, rightRes)
        }

        func update(_ node: Int, _ l: Int, _ r: Int, _ ul: Int, _ ur: Int, _ val: Int) {
            if ul > r || ur < l { return }
            if ul <= l && r <= ur {
                segMax[node] = val
                lazy[node] = val
                return
            }
            push(node)
            let mid = (l + r) >> 1
            update(node << 1, l, mid, ul, ur, val)
            update((node << 1) | 1, mid + 1, r, ul, ur, val)
            segMax[node] = max(segMax[node << 1], segMax[(node << 1) | 1])
        }

        var result: [Int] = []
        var currentMax = 0
        for p in positions {
            let left = p[0]
            let size = p[1]
            let right = left + size
            let l = indexMap[left]!               // inclusive
            let r = indexMap[right]! - 1          // inclusive
            let baseHeight = query(1, 0, intervalCount - 1, l, r)
            let newHeight = baseHeight + size
            update(1, 0, intervalCount - 1, l, r, newHeight)
            currentMax = max(currentMax, newHeight)
            result.append(currentMax)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun fallingSquares(positions: Array<IntArray>): List<Int> {
        val coords = mutableListOf<Int>()
        for (p in positions) {
            val left = p[0]
            val size = p[1]
            coords.add(left)
            coords.add(left + size)
        }
        coords.sort()
        val uniq = mutableListOf<Int>()
        var prev = Int.MIN_VALUE
        for (c in coords) {
            if (c != prev) {
                uniq.add(c)
                prev = c
            }
        }
        val nSeg = uniq.size - 1
        if (nSeg <= 0) return emptyList()
        val tree = IntArray(4 * nSeg)
        val lazy = IntArray(4 * nSeg)

        fun push(node: Int) {
            val v = lazy[node]
            if (v != 0) {
                val leftNode = node shl 1
                val rightNode = leftNode + 1
                tree[leftNode] = v
                tree[rightNode] = v
                lazy[leftNode] = v
                lazy[rightNode] = v
                lazy[node] = 0
            }
        }

        fun query(node: Int, l: Int, r: Int, ql: Int, qr: Int): Int {
            if (ql > r || qr < l) return 0
            if (ql <= l && r <= qr) return tree[node]
            push(node)
            val mid = (l + r) ushr 1
            val leftMax = query(node shl 1, l, mid, ql, qr)
            val rightMax = query((node shl 1) + 1, mid + 1, r, ql, qr)
            return if (leftMax > rightMax) leftMax else rightMax
        }

        fun update(node: Int, l: Int, r: Int, ul: Int, ur: Int, value: Int) {
            if (ul > r || ur < l) return
            if (ul <= l && r <= ur) {
                tree[node] = value
                lazy[node] = value
                return
            }
            push(node)
            val mid = (l + r) ushr 1
            update(node shl 1, l, mid, ul, ur, value)
            update((node shl 1) + 1, mid + 1, r, ul, ur, value)
            tree[node] = if (tree[node shl 1] > tree[(node shl 1) + 1]) tree[node shl 1] else tree[(node shl 1) + 1]
        }

        fun lowerBound(arr: List<Int>, target: Int): Int {
            var l = 0
            var r = arr.size
            while (l < r) {
                val m = (l + r) ushr 1
                if (arr[m] < target) l = m + 1 else r = m
            }
            return l
        }

        val result = mutableListOf<Int>()
        var curMax = 0
        for (p in positions) {
            val left = p[0]
            val size = p[1]
            val right = left + size
            val lIdx = lowerBound(uniq, left)
            val rIdx = lowerBound(uniq, right) - 1
            val baseHeight = query(1, 0, nSeg - 1, lIdx, rIdx)
            val newHeight = baseHeight + size
            update(1, 0, nSeg - 1, lIdx, rIdx, newHeight)
            if (newHeight > curMax) curMax = newHeight
            result.add(curMax)
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> fallingSquares(List<List<int>> positions) {
    // Collect all unique coordinates (left and right edges)
    final Set<int> coordSet = {};
    for (var p in positions) {
      int left = p[0];
      int size = p[1];
      coordSet.add(left);
      coordSet.add(left + size);
    }
    final List<int> xs = coordSet.toList()..sort();
    // Map each coordinate to its index
    final Map<int, int> idx = {};
    for (int i = 0; i < xs.length; i++) {
      idx[xs[i]] = i;
    }

    // Number of elementary segments between coordinates
    final int segCount = xs.length - 1;
    if (segCount <= 0) {
      // Edge case: no segment, just return cumulative heights
      List<int> ans = [];
      int curMax = 0;
      for (var p in positions) {
        curMax = (curMax > p[1]) ? curMax : p[1];
        ans.add(curMax);
      }
      return ans;
    }

    final SegmentTree st = SegmentTree(segCount);

    List<int> result = [];
    int globalMax = 0;

    for (var p in positions) {
      int left = p[0];
      int size = p[1];
      int right = left + size;

      int lIdx = idx[left]!;
      int rIdx = idx[right]! - 1; // inclusive segment index

      int curHeight = st.query(1, 0, segCount - 1, lIdx, rIdx);
      int newHeight = curHeight + size;
      st.update(1, 0, segCount - 1, lIdx, rIdx, newHeight);

      if (newHeight > globalMax) globalMax = newHeight;
      result.add(globalMax);
    }

    return result;
  }
}

class SegmentTree {
  final int n;
  late List<int> tree;
  late List<int?> lazy;

  SegmentTree(this.n) {
    tree = List.filled(4 * n, 0);
    lazy = List.filled(4 * n, null);
  }

  void _push(int node, int l, int r) {
    if (lazy[node] != null) {
      tree[node] = lazy[node]!;
      if (l != r) {
        lazy[node << 1] = lazy[node];
        lazy[(node << 1) + 1] = lazy[node];
      }
      lazy[node] = null;
    }
  }

  int query(int node, int l, int r, int ql, int qr) {
    _push(node, l, r);
    if (qr < l || r < ql) return 0;
    if (ql <= l && r <= qr) return tree[node];
    int mid = (l + r) >> 1;
    int leftMax = query(node << 1, l, mid, ql, qr);
    int rightMax = query((node << 1) + 1, mid + 1, r, ql, qr);
    return leftMax > rightMax ? leftMax : rightMax;
  }

  void update(int node, int l, int r, int ul, int ur, int val) {
    _push(node, l, r);
    if (ur < l || r < ul) return;
    if (ul <= l && r <= ur) {
      lazy[node] = val;
      _push(node, l, r);
      return;
    }
    int mid = (l + r) >> 1;
    update(node << 1, l, mid, ul, ur, val);
    update((node << 1) + 1, mid + 1, r, ul, ur, val);
    tree[node] = tree[node << 1] > tree[(node << 1) + 1]
        ? tree[node << 1]
        : tree[(node << 1) + 1];
  }
}
```

## Golang

```go
import "sort"

func fallingSquares(positions [][]int) []int {
    xs := make([]int, 0, len(positions)*2)
    for _, p := range positions {
        l := p[0]
        r := p[0] + p[1]
        xs = append(xs, l, r)
    }
    sort.Ints(xs)
    uniq := []int{}
    for _, v := range xs {
        if len(uniq) == 0 || uniq[len(uniq)-1] != v {
            uniq = append(uniq, v)
        }
    }
    idxMap := make(map[int]int, len(uniq))
    for i, v := range uniq {
        idxMap[v] = i
    }
    n := len(uniq) - 1 // number of elementary intervals
    if n <= 0 {
        n = 1
    }
    tree := make([]int, 4*n)
    lazy := make([]int, 4*n)

    var push func(int)
    push = func(node int) {
        if lazy[node] != 0 {
            val := lazy[node]
            left, right := node*2, node*2+1
            tree[left], tree[right] = val, val
            lazy[left], lazy[right] = val, val
            lazy[node] = 0
        }
    }

    var query func(node, l, r, ql, qr int) int
    query = func(node, l, r, ql, qr int) int {
        if ql > r || qr < l {
            return 0
        }
        if ql <= l && r <= qr {
            return tree[node]
        }
        push(node)
        mid := (l + r) / 2
        leftMax := query(node*2, l, mid, ql, qr)
        rightMax := query(node*2+1, mid+1, r, ql, qr)
        if leftMax > rightMax {
            return leftMax
        }
        return rightMax
    }

    var update func(node, l, r, ul, ur, val int)
    update = func(node, l, r, ul, ur, val int) {
        if ul > r || ur < l {
            return
        }
        if ul <= l && r <= ur {
            tree[node] = val
            lazy[node] = val
            return
        }
        push(node)
        mid := (l + r) / 2
        update(node*2, l, mid, ul, ur, val)
        update(node*2+1, mid+1, r, ul, ur, val)
        if tree[node*2] > tree[node*2+1] {
            tree[node] = tree[node*2]
        } else {
            tree[node] = tree[node*2+1]
        }
    }

    res := make([]int, len(positions))
    curMax := 0
    for i, p := range positions {
        lIdx := idxMap[p[0]]
        rIdx := idxMap[p[0]+p[1]] - 1 // inclusive
        prev := query(1, 0, n-1, lIdx, rIdx)
        h := prev + p[1]
        update(1, 0, n-1, lIdx, rIdx, h)
        if h > curMax {
            curMax = h
        }
        res[i] = curMax
    }
    return res
}
```

## Ruby

```ruby
class SegTree
  def initialize(size)
    @n = size
    @tree = Array.new(4 * size, 0)
    @lazy = Array.new(4 * size, 0)
  end

  def query(l, r)
    _query(1, 0, @n - 1, l, r)
  end

  def update(l, r, val)
    _update(1, 0, @n - 1, l, r, val)
  end

  private

  def push(node)
    if @lazy[node] != 0
      @tree[node * 2] = @lazy[node]
      @tree[node * 2 + 1] = @lazy[node]
      @lazy[node * 2] = @lazy[node]
      @lazy[node * 2 + 1] = @lazy[node]
      @lazy[node] = 0
    end
  end

  def _query(node, start, finish, l, r)
    return 0 if r < start || finish < l
    if l <= start && finish <= r
      return @tree[node]
    end
    push(node)
    mid = (start + finish) / 2
    left = _query(node * 2, start, mid, l, r)
    right = _query(node * 2 + 1, mid + 1, finish, l, r)
    left > right ? left : right
  end

  def _update(node, start, finish, l, r, val)
    return if r < start || finish < l
    if l <= start && finish <= r
      @tree[node] = val
      @lazy[node] = val
      return
    end
    push(node)
    mid = (start + finish) / 2
    _update(node * 2, start, mid, l, r, val)
    _update(node * 2 + 1, mid + 1, finish, l, r, val)
    @tree[node] = @tree[node * 2] > @tree[node * 2 + 1] ? @tree[node * 2] : @tree[node * 2 + 1]
  end
end

def falling_squares(positions)
  coords = []
  positions.each do |left, size|
    coords << left
    coords << left + size
  end
  xs = coords.uniq.sort
  index = {}
  xs.each_with_index { |x, i| index[x] = i }
  n = xs.length
  seg = SegTree.new(n)
  result = []
  cur_max = 0
  positions.each do |left, size|
    l = index[left]
    r = index[left + size] - 1
    height = seg.query(l, r) + size
    seg.update(l, r, height)
    cur_max = height if height > cur_max
    result << cur_max
  end
  result
end
```

## Scala

```scala
object Solution {
    def fallingSquares(positions: Array[Array[Int]]): List[Int] = {
        val n = positions.length
        val topHeights = new Array[Int](n)
        var globalMax = 0
        val result = scala.collection.mutable.ListBuffer[Int]()
        for (i <- 0 until n) {
            val left = positions(i)(0)
            val size = positions(i)(1)
            val right = left + size
            var baseHeight = 0
            var j = 0
            while (j < i) {
                val l2 = positions(j)(0)
                val r2 = l2 + positions(j)(1)
                if (!(right <= l2 || left >= r2)) { // overlap with positive length
                    baseHeight = math.max(baseHeight, topHeights(j))
                }
                j += 1
            }
            topHeights(i) = baseHeight + size
            globalMax = math.max(globalMax, topHeights(i))
            result += globalMax
        }
        result.toList
    }
}
```

## Rust

```rust
use std::cmp::max;

struct SegTree {
    n: usize,
    tree: Vec<i32>,
    lazy: Vec<Option<i32>>,
}

impl SegTree {
    fn new(n: usize) -> Self {
        let size = 4 * n + 5;
        SegTree {
            n,
            tree: vec![0; size],
            lazy: vec![None; size],
        }
    }

    fn push(&mut self, idx: usize) {
        if let Some(val) = self.lazy[idx] {
            let left = idx << 1;
            let right = left | 1;
            self.tree[left] = val;
            self.tree[right] = val;
            self.lazy[left] = Some(val);
            self.lazy[right] = Some(val);
            self.lazy[idx] = None;
        }
    }

    fn update(&mut self, idx: usize, l: usize, r: usize, ql: usize, qr: usize, val: i32) {
        if ql > r || qr < l {
            return;
        }
        if ql <= l && r <= qr {
            self.tree[idx] = val;
            self.lazy[idx] = Some(val);
            return;
        }
        self.push(idx);
        let mid = (l + r) / 2;
        self.update(idx * 2, l, mid, ql, qr, val);
        self.update(idx * 2 + 1, mid + 1, r, ql, qr, val);
        self.tree[idx] = max(self.tree[idx * 2], self.tree[idx * 2 + 1]);
    }

    fn query(&mut self, idx: usize, l: usize, r: usize, ql: usize, qr: usize) -> i32 {
        if ql > r || qr < l {
            return 0;
        }
        if ql <= l && r <= qr {
            return self.tree[idx];
        }
        self.push(idx);
        let mid = (l + r) / 2;
        let left = self.query(idx * 2, l, mid, ql, qr);
        let right = self.query(idx * 2 + 1, mid + 1, r, ql, qr);
        max(left, right)
    }
}

impl Solution {
    pub fn falling_squares(positions: Vec<Vec<i32>>) -> Vec<i32> {
        let n = positions.len();
        if n == 0 {
            return vec![];
        }

        // coordinate compression
        let mut coords: Vec<i64> = Vec::with_capacity(2 * n);
        for p in &positions {
            let l = p[0] as i64;
            let r = (p[0] + p[1]) as i64;
            coords.push(l);
            coords.push(r);
        }
        coords.sort_unstable();
        coords.dedup();

        // number of elementary intervals
        let seg_len = if coords.len() > 1 { coords.len() - 1 } else { 0 };
        let mut seg = SegTree::new(seg_len);

        let mut ans: Vec<i32> = Vec::with_capacity(n);
        let mut cur_max = 0i32;

        for p in positions {
            let l = p[0] as i64;
            let r = (p[0] + p[1]) as i64;
            let left_idx = coords.binary_search(&l).unwrap();
            // right coordinate index points to the start of the next interval,
            // so we subtract 1 to get the last covered segment index.
            let right_idx = coords.binary_search(&r).unwrap() - 1;

            let max_h = if seg_len == 0 {
                0
            } else {
                seg.query(1, 0, seg_len - 1, left_idx, right_idx)
            };
            let new_h = max_h + p[1];
            if seg_len > 0 {
                seg.update(1, 0, seg_len - 1, left_idx, right_idx, new_h);
            }
            cur_max = max(cur_max, new_h);
            ans.push(cur_max);
        }

        ans
    }
}
```

## Racket

```racket
#lang racket

(define/contract (falling-squares positions)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ((n (length positions))
         (lefts (make-vector n 0))
         (rights (make-vector n 0))
         (heights (make-vector n 0))
         (result (make-vector n 0)))
    (for ([i (in-range n)])
      (define pos (list-ref positions i))
      (define left (first pos))
      (define size (second pos))
      (define right (+ left size))
      (vector-set! lefts i left)
      (vector-set! rights i right)
      (define cur size)
      (for ([j (in-range i)])
        (when (and (< left (vector-ref rights j))
                   (< (vector-ref lefts j) right))
          (set! cur (max cur (+ (vector-ref heights j) size)))))
      (vector-set! heights i cur)
      (define max-so-far (if (= i 0) cur (max (vector-ref result (- i 1)) cur)))
      (vector-set! result i max-so-far))
    (let loop ((idx n) (acc '()))
      (if (= idx 0)
          acc
          (loop (- idx 1) (cons (vector-ref result (- idx 1)) acc))))))
```

## Erlang

```erlang
-spec falling_squares(Positions :: [[integer()]]) -> [integer()].
falling_squares(Positions) ->
    falling_squares(Positions, [], 0, []).

falling_squares([], _Intervals, _GlobalMax, AccRev) ->
    lists:reverse(AccRev);
falling_squares([[L,S]|Rest], Intervals, GlobalMax, AccRev) ->
    R = L + S,
    MaxPrev = max_overlap_height(L, R, Intervals),
    Height = MaxPrev + S,
    NewIntervals = [{L,R,Height}|Intervals],
    NewGlobal = erlang:max(GlobalMax, Height),
    falling_squares(Rest, NewIntervals, NewGlobal, [NewGlobal|AccRev]).

max_overlap_height(_L,_R,[]) -> 0;
max_overlap_height(L,R,Intervals) ->
    lists:foldl(fun({L1,R1,H}, Acc) ->
        if L < R1 andalso R > L1 -> erlang:max(Acc, H);
           true -> Acc
        end
    end, 0, Intervals).
```

## Elixir

```elixir
defmodule Solution do
  @spec falling_squares(positions :: [[integer]]) :: [integer]
  def falling_squares(positions) do
    n = length(positions)

    {ans_rev, _heights_rev, _} =
      Enum.reduce(0..(n - 1), {[], [], 0}, fn i, {ans_acc, heights_acc, cur_max} ->
        [left, size] = Enum.at(positions, i)
        r = left + size

        h =
          if i == 0 do
            size
          else
            Enum.reduce(0..(i - 1), size, fn j, acc ->
              [pl, ps] = Enum.at(positions, j)
              pr = pl + ps

              if not (r <= pl or left >= pr) do
                prev_h = Enum.at(heights_acc, j)
                max(acc, prev_h + size)
              else
                acc
              end
            end)
          end

        new_max = max(cur_max, h)
        {[new_max | ans_acc], heights_acc ++ [h], new_max}
      end)

    Enum.reverse(ans_rev)
  end
end
```
