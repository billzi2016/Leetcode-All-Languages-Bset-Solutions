# 3479. Fruits Into Baskets III

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class SegmentTree {
    int n;
    vector<int> tree;
public:
    SegmentTree(const vector<int>& arr) {
        n = (int)arr.size();
        tree.assign(4 * n, INT_MAX);
        build(1, 0, n - 1, arr);
    }
    void update(int idx, int val) { update(1, 0, n - 1, idx, val); }
    int query(int l, int r) { return query(1, 0, n - 1, l, r); }

private:
    void build(int node, int l, int r, const vector<int>& arr) {
        if (l == r) {
            tree[node] = arr[l];
            return;
        }
        int mid = (l + r) >> 1;
        build(node << 1, l, mid, arr);
        build(node << 1 | 1, mid + 1, r, arr);
        tree[node] = min(tree[node << 1], tree[node << 1 | 1]);
    }
    void update(int node, int l, int r, int idx, int val) {
        if (l == r) {
            tree[node] = val;
            return;
        }
        int mid = (l + r) >> 1;
        if (idx <= mid) update(node << 1, l, mid, idx, val);
        else update(node << 1 | 1, mid + 1, r, idx, val);
        tree[node] = min(tree[node << 1], tree[node << 1 | 1]);
    }
    int query(int node, int l, int r, int ql, int qr) {
        if (qr < l || r < ql) return INT_MAX;
        if (ql <= l && r <= qr) return tree[node];
        int mid = (l + r) >> 1;
        return min(query(node << 1, l, mid, ql, qr),
                   query(node << 1 | 1, mid + 1, r, ql, qr));
    }
};

class Solution {
public:
    int numOfUnplacedFruits(vector<int>& fruits, vector<int>& baskets) {
        int n = (int)fruits.size();
        vector<pair<int,int>> sorted;
        sorted.reserve(n);
        for (int i = 0; i < n; ++i) sorted.emplace_back(baskets[i], i);
        sort(sorted.begin(), sorted.end()); // by capacity, then index

        vector<int> leafVals(n);
        vector<int> posInSorted(n);
        for (int i = 0; i < n; ++i) {
            leafVals[i] = sorted[i].second;
            posInSorted[sorted[i].second] = i;
        }

        SegmentTree seg(leafVals);
        int unplaced = 0;

        for (int f : fruits) {
            int lo = lower_bound(sorted.begin(), sorted.end(), f,
                                 [](const pair<int,int>& a, const int& val){ return a.first < val; })
                     - sorted.begin();
            if (lo == n) { ++unplaced; continue; }

            int minIdx = seg.query(lo, n - 1);
            if (minIdx == INT_MAX) {
                ++unplaced;
            } else {
                int pos = posInSorted[minIdx];
                seg.update(pos, INT_MAX); // mark as used
            }
        }
        return unplaced;
    }
};
```

## Java

```java
class Solution {
    private int[] seg;
    private int n;

    public int numOfUnplacedFruits(int[] fruits, int[] baskets) {
        n = baskets.length;
        seg = new int[4 * n];
        build(1, 0, n - 1, baskets);
        int unplaced = 0;
        for (int fruit : fruits) {
            int idx = queryFirst(1, 0, n - 1, fruit);
            if (idx == -1) {
                unplaced++;
            } else {
                update(1, 0, n - 1, idx, 0);
            }
        }
        return unplaced;
    }

    private void build(int node, int l, int r, int[] arr) {
        if (l == r) {
            seg[node] = arr[l];
            return;
        }
        int mid = (l + r) >>> 1;
        build(node << 1, l, mid, arr);
        build(node << 1 | 1, mid + 1, r, arr);
        seg[node] = Math.max(seg[node << 1], seg[node << 1 | 1]);
    }

    // returns leftmost index with value >= val, or -1 if none
    private int queryFirst(int node, int l, int r, int val) {
        if (seg[node] < val) return -1;
        if (l == r) return l;
        int mid = (l + r) >>> 1;
        if (seg[node << 1] >= val) {
            return queryFirst(node << 1, l, mid, val);
        } else {
            return queryFirst(node << 1 | 1, mid + 1, r, val);
        }
    }

    private void update(int node, int l, int r, int idx, int newVal) {
        if (l == r) {
            seg[node] = newVal;
            return;
        }
        int mid = (l + r) >>> 1;
        if (idx <= mid) {
            update(node << 1, l, mid, idx, newVal);
        } else {
            update(node << 1 | 1, mid + 1, r, idx, newVal);
        }
        seg[node] = Math.max(seg[node << 1], seg[node << 1 | 1]);
    }
}
```

## Python

```python
class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        n = len(baskets)
        size = 1
        while size < n:
            size <<= 1
        tree = [0] * (2 * size)
        # build leaves
        for i in range(n):
            tree[size + i] = baskets[i]
        for i in range(size - 1, 0, -1):
            tree[i] = max(tree[2 * i], tree[2 * i + 1])

        def update(pos):
            idx = size + pos
            tree[idx] = 0
            idx //= 2
            while idx:
                new_val = max(tree[2 * idx], tree[2 * idx + 1])
                if tree[idx] == new_val:
                    break
                tree[idx] = new_val
                idx //= 2

        def find_leftmost(val):
            # assumes tree[1] >= val
            idx = 1
            while idx < size:
                if tree[2 * idx] >= val:
                    idx = 2 * idx
                else:
                    idx = 2 * idx + 1
            return idx - size

        unplaced = 0
        for fruit in fruits:
            if tree[1] < fruit:
                unplaced += 1
                continue
            pos = find_leftmost(fruit)
            update(pos)
        return unplaced
```

## Python3

```python
from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        size = 1
        while size < n:
            size <<= 1
        seg = [0] * (2 * size)

        # build leaves
        for i in range(n):
            seg[size + i] = baskets[i]
        # build internal nodes
        for i in range(size - 1, 0, -1):
            seg[i] = max(seg[i << 1], seg[(i << 1) | 1])

        def update(pos: int) -> None:
            idx = size + pos
            seg[idx] = 0
            idx >>= 1
            while idx:
                seg[idx] = max(seg[idx << 1], seg[(idx << 1) | 1])
                idx >>= 1

        def find_first(val: int) -> int:
            if seg[1] < val:
                return -1
            idx = 1
            while idx < size:
                left = idx << 1
                if seg[left] >= val:
                    idx = left
                else:
                    idx = left | 1
            pos = idx - size
            return pos if pos < n else -1

        unplaced = 0
        for f in fruits:
            pos = find_first(f)
            if pos == -1:
                unplaced += 1
            else:
                update(pos)

        return unplaced
```

## C

```c
#include <stdlib.h>
#include <limits.h>

typedef struct {
    int cap;
    int idx;
} Pair;

static Pair *arr;
static int *seg;
static int N;
static const int INF = INT_MAX;

static int cmpPair(const void *a, const void *b) {
    const Pair *pa = (const Pair *)a;
    const Pair *pb = (const Pair *)b;
    if (pa->cap != pb->cap) return pa->cap - pb->cap;
    return pa->idx - pb->idx;
}

static void build(int node, int l, int r) {
    if (l == r) {
        seg[node] = arr[l].idx;
        return;
    }
    int mid = (l + r) >> 1;
    build(node << 1, l, mid);
    build(node << 1 | 1, mid + 1, r);
    seg[node] = seg[node << 1] < seg[node << 1 | 1] ? seg[node << 1] : seg[node << 1 | 1];
}

static void update(int node, int l, int r, int idx, int val) {
    if (l == r) {
        seg[node] = val;
        return;
    }
    int mid = (l + r) >> 1;
    if (idx <= mid) update(node << 1, l, mid, idx, val);
    else update(node << 1 | 1, mid + 1, r, idx, val);
    seg[node] = seg[node << 1] < seg[node << 1 | 1] ? seg[node << 1] : seg[node << 1 | 1];
}

/* return position of leftmost leaf in [ql,qr] with value != INF, or -1 */
static int queryPos(int node, int l, int r, int ql, int qr) {
    if (r < ql || l > qr || seg[node] == INF) return -1;
    if (l == r) return l;
    int mid = (l + r) >> 1;
    int leftRes = queryPos(node << 1, l, mid, ql, qr);
    if (leftRes != -1) return leftRes;
    return queryPos(node << 1 | 1, mid + 1, r, ql, qr);
}

int numOfUnplacedFruits(int* fruits, int fruitsSize, int* baskets, int basketsSize) {
    N = fruitsSize;   // same as basketsSize
    arr = (Pair *)malloc(sizeof(Pair) * N);
    seg = (int *)malloc(sizeof(int) * 4 * N);
    
    for (int i = 0; i < N; ++i) {
        arr[i].cap = baskets[i];
        arr[i].idx = i;
    }
    qsort(arr, N, sizeof(Pair), cmpPair);
    build(1, 0, N - 1);
    
    int unplaced = 0;
    for (int i = 0; i < fruitsSize; ++i) {
        int f = fruits[i];
        // lower_bound on capacity
        int lo = 0, hi = N;
        while (lo < hi) {
            int mid = (lo + hi) >> 1;
            if (arr[mid].cap >= f) hi = mid;
            else lo = mid + 1;
        }
        if (lo == N) {
            ++unplaced;
            continue;
        }
        int pos = queryPos(1, 0, N - 1, lo, N - 1);
        if (pos == -1) {
            ++unplaced;
        } else {
            update(1, 0, N - 1, pos, INF); // mark used
        }
    }
    
    free(arr);
    free(seg);
    return unplaced;
}
```

## Csharp

```csharp
public class Solution
{
    private int[] seg;
    private int n;

    public int NumOfUnplacedFruits(int[] fruits, int[] baskets)
    {
        n = baskets.Length;
        seg = new int[4 * n];
        Build(1, 0, n - 1, baskets);
        int unplaced = 0;
        foreach (int fruit in fruits)
        {
            if (seg[1] < fruit)
            {
                unplaced++;
            }
            else
            {
                int idx = FindFirst(1, 0, n - 1, fruit);
                Update(1, 0, n - 1, idx, 0);
            }
        }
        return unplaced;
    }

    private void Build(int node, int l, int r, int[] arr)
    {
        if (l == r)
        {
            seg[node] = arr[l];
            return;
        }
        int mid = (l + r) >> 1;
        Build(node << 1, l, mid, arr);
        Build(node << 1 | 1, mid + 1, r, arr);
        seg[node] = Math.Max(seg[node << 1], seg[node << 1 | 1]);
    }

    private void Update(int node, int l, int r, int idx, int val)
    {
        if (l == r)
        {
            seg[node] = val;
            return;
        }
        int mid = (l + r) >> 1;
        if (idx <= mid) Update(node << 1, l, mid, idx, val);
        else Update(node << 1 | 1, mid + 1, r, idx, val);
        seg[node] = Math.Max(seg[node << 1], seg[node << 1 | 1]);
    }

    private int FindFirst(int node, int l, int r, int fruit)
    {
        if (seg[node] < fruit) return -1;
        if (l == r) return l;
        int mid = (l + r) >> 1;
        if (seg[node << 1] >= fruit) return FindFirst(node << 1, l, mid, fruit);
        else return FindFirst(node << 1 | 1, mid + 1, r, fruit);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} fruits
 * @param {number[]} baskets
 * @return {number}
 */
var numOfUnplacedFruits = function(fruits, baskets) {
    const n = baskets.length;
    const seg = new Array(4 * n).fill(0);
    
    const build = (node, l, r) => {
        if (l === r) {
            seg[node] = baskets[l];
            return;
        }
        const mid = (l + r) >> 1;
        build(node << 1, l, mid);
        build((node << 1) | 1, mid + 1, r);
        seg[node] = Math.max(seg[node << 1], seg[(node << 1) | 1]);
    };
    
    const update = (node, l, r, idx, val) => {
        if (l === r) {
            seg[node] = val;
            return;
        }
        const mid = (l + r) >> 1;
        if (idx <= mid) update(node << 1, l, mid, idx, val);
        else update((node << 1) | 1, mid + 1, r, idx, val);
        seg[node] = Math.max(seg[node << 1], seg[(node << 1) | 1]);
    };
    
    const findFirst = (node, l, r, need) => {
        if (seg[node] < need) return -1;
        if (l === r) return l;
        const mid = (l + r) >> 1;
        if (seg[node << 1] >= need) return findFirst(node << 1, l, mid, need);
        return findFirst((node << 1) | 1, mid + 1, r, need);
    };
    
    build(1, 0, n - 1);
    let unplaced = 0;
    for (const f of fruits) {
        const idx = findFirst(1, 0, n - 1, f);
        if (idx === -1) {
            ++unplaced;
        } else {
            update(1, 0, n - 1, idx, 0);
        }
    }
    return unplaced;
};
```

## Typescript

```typescript
function numOfUnplacedFruits(fruits: number[], baskets: number[]): number {
    const n = baskets.length;
    const size = 1 << Math.ceil(Math.log2(n));
    const seg = new Array(2 * size).fill(0);
    for (let i = 0; i < n; ++i) seg[size + i] = baskets[i];
    for (let i = size - 1; i > 0; --i) seg[i] = Math.max(seg[i << 1], seg[(i << 1) | 1]);

    function update(pos: number): void {
        let idx = size + pos;
        seg[idx] = 0;
        idx >>= 1;
        while (idx) {
            const newVal = Math.max(seg[idx << 1], seg[(idx << 1) | 1]);
            if (seg[idx] === newVal) break;
            seg[idx] = newVal;
            idx >>= 1;
        }
    }

    function findFirst(node: number, l: number, r: number, need: number): number {
        if (seg[node] < need) return -1;
        if (l === r) return l;
        const mid = (l + r) >> 1;
        if (seg[node << 1] >= need) {
            const leftRes = findFirst(node << 1, l, mid, need);
            if (leftRes !== -1) return leftRes;
        }
        return findFirst((node << 1) | 1, mid + 1, r, need);
    }

    let unplaced = 0;
    for (const f of fruits) {
        const idx = findFirst(1, 0, size - 1, f);
        if (idx === -1 || idx >= n) {
            ++unplaced;
        } else {
            update(idx);
        }
    }
    return unplaced;
}
```

## Php

```php
class Solution {
    private $tree = [];
    private $n;

    private function build(&$arr, $node, $l, $r) {
        if ($l == $r) {
            $this->tree[$node] = $arr[$l];
            return;
        }
        $mid = intdiv($l + $r, 2);
        $this->build($arr, $node * 2, $l, $mid);
        $this->build($arr, $node * 2 + 1, $mid + 1, $r);
        $this->tree[$node] = max($this->tree[$node * 2], $this->tree[$node * 2 + 1]);
    }

    private function queryFirst($node, $l, $r, $value) {
        if ($this->tree[$node] < $value) {
            return -1;
        }
        if ($l == $r) {
            return $l;
        }
        $mid = intdiv($l + $r, 2);
        $leftRes = $this->queryFirst($node * 2, $l, $mid, $value);
        if ($leftRes != -1) {
            return $leftRes;
        }
        return $this->queryFirst($node * 2 + 1, $mid + 1, $r, $value);
    }

    private function update($node, $l, $r, $idx) {
        if ($l == $r) {
            $this->tree[$node] = 0;
            return;
        }
        $mid = intdiv($l + $r, 2);
        if ($idx <= $mid) {
            $this->update($node * 2, $l, $mid, $idx);
        } else {
            $this->update($node * 2 + 1, $mid + 1, $r, $idx);
        }
        $this->tree[$node] = max($this->tree[$node * 2], $this->tree[$node * 2 + 1]);
    }

    /**
     * @param Integer[] $fruits
     * @param Integer[] $baskets
     * @return Integer
     */
    function numOfUnplacedFruits($fruits, $baskets) {
        $this->n = count($baskets);
        if ($this->n == 0) return count($fruits);
        $this->tree = array_fill(0, $this->n * 4, 0);
        $this->build($baskets, 1, 0, $this->n - 1);

        $unplaced = 0;
        foreach ($fruits as $fruit) {
            $pos = $this->queryFirst(1, 0, $this->n - 1, $fruit);
            if ($pos == -1) {
                $unplaced++;
            } else {
                $this->update(1, 0, $this->n - 1, $pos);
            }
        }
        return $unplaced;
    }
}
```

## Swift

```swift
class SegmentTree {
    private var n: Int
    private var tree: [Int]

    init(_ arr: [Int]) {
        self.n = arr.count
        self.tree = Array(repeating: 0, count: 4 * n)
        build(1, 0, n - 1, arr)
    }

    private func build(_ node: Int, _ l: Int, _ r: Int, _ arr: [Int]) {
        if l == r {
            tree[node] = arr[l]
            return
        }
        let mid = (l + r) >> 1
        build(node << 1, l, mid, arr)
        build((node << 1) | 1, mid + 1, r, arr)
        tree[node] = max(tree[node << 1], tree[(node << 1) | 1])
    }

    func findFirst(_ target: Int) -> Int? {
        return findFirstRec(1, 0, n - 1, target)
    }

    private func findFirstRec(_ node: Int, _ l: Int, _ r: Int, _ target: Int) -> Int? {
        if tree[node] < target { return nil }
        if l == r { return l }
        let mid = (l + r) >> 1
        if tree[node << 1] >= target {
            return findFirstRec(node << 1, l, mid, target)
        } else {
            return findFirstRec((node << 1) | 1, mid + 1, r, target)
        }
    }

    func update(_ idx: Int) {
        updateRec(1, 0, n - 1, idx)
    }

    private func updateRec(_ node: Int, _ l: Int, _ r: Int, _ idx: Int) {
        if l == r {
            tree[node] = 0
            return
        }
        let mid = (l + r) >> 1
        if idx <= mid {
            updateRec(node << 1, l, mid, idx)
        } else {
            updateRec((node << 1) | 1, mid + 1, r, idx)
        }
        tree[node] = max(tree[node << 1], tree[(node << 1) | 1])
    }
}

class Solution {
    func numOfUnplacedFruits(_ fruits: [Int], _ baskets: [Int]) -> Int {
        let n = baskets.count
        if n == 0 { return fruits.count }
        let seg = SegmentTree(baskets)
        var unplaced = 0
        for fruit in fruits {
            if let idx = seg.findFirst(fruit) {
                seg.update(idx)
            } else {
                unplaced += 1
            }
        }
        return unplaced
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numOfUnplacedFruits(fruits: IntArray, baskets: IntArray): Int {
        val seg = SegmentTree(baskets)
        var unplaced = 0
        for (f in fruits) {
            val idx = seg.findFirst(f)
            if (idx == -1) {
                unplaced++
            } else {
                seg.update(idx, 0)
            }
        }
        return unplaced
    }

    private class SegmentTree(arr: IntArray) {
        private val n = arr.size
        private val tree = IntArray(n * 4)

        init {
            build(1, 0, n - 1, arr)
        }

        private fun build(node: Int, l: Int, r: Int, arr: IntArray) {
            if (l == r) {
                tree[node] = arr[l]
                return
            }
            val mid = (l + r) ushr 1
            build(node shl 1, l, mid, arr)
            build(node shl 1 or 1, mid + 1, r, arr)
            tree[node] = kotlin.math.max(tree[node shl 1], tree[node shl 1 or 1])
        }

        fun update(idx: Int, value: Int) {
            update(1, 0, n - 1, idx, value)
        }

        private fun update(node: Int, l: Int, r: Int, idx: Int, value: Int) {
            if (l == r) {
                tree[node] = value
                return
            }
            val mid = (l + r) ushr 1
            if (idx <= mid) {
                update(node shl 1, l, mid, idx, value)
            } else {
                update(node shl 1 or 1, mid + 1, r, idx, value)
            }
            tree[node] = kotlin.math.max(tree[node shl 1], tree[node shl 1 or 1])
        }

        fun findFirst(target: Int): Int {
            if (tree[1] < target) return -1
            return find(1, 0, n - 1, target)
        }

        private fun find(node: Int, l: Int, r: Int, target: Int): Int {
            if (l == r) return l
            val leftMax = tree[node shl 1]
            val mid = (l + r) ushr 1
            return if (leftMax >= target) {
                find(node shl 1, l, mid, target)
            } else {
                find(node shl 1 or 1, mid + 1, r, target)
            }
        }
    }
}
```

## Dart

```dart
class Solution {
  int numOfUnplacedFruits(List<int> fruits, List<int> baskets) {
    int n = baskets.length;
    List<int> seg = List.filled(4 * n, 0);

    void build(int node, int l, int r) {
      if (l == r) {
        seg[node] = baskets[l];
        return;
      }
      int mid = (l + r) >> 1;
      build(node << 1, l, mid);
      build((node << 1) | 1, mid + 1, r);
      seg[node] = seg[node << 1] > seg[(node << 1) | 1]
          ? seg[node << 1]
          : seg[(node << 1) | 1];
    }

    void update(int node, int l, int r, int idx) {
      if (l == r) {
        seg[node] = 0;
        return;
      }
      int mid = (l + r) >> 1;
      if (idx <= mid) {
        update(node << 1, l, mid, idx);
      } else {
        update((node << 1) | 1, mid + 1, r, idx);
      }
      seg[node] = seg[node << 1] > seg[(node << 1) | 1]
          ? seg[node << 1]
          : seg[(node << 1) | 1];
    }

    int queryFirst(int node, int l, int r, int val) {
      if (seg[node] < val) return -1;
      if (l == r) return l;
      int mid = (l + r) >> 1;
      if (seg[node << 1] >= val) {
        return queryFirst(node << 1, l, mid, val);
      } else {
        return queryFirst((node << 1) | 1, mid + 1, r, val);
      }
    }

    build(1, 0, n - 1);
    int unplaced = 0;
    for (int fruit in fruits) {
      if (seg[1] < fruit) {
        unplaced++;
        continue;
      }
      int idx = queryFirst(1, 0, n - 1, fruit);
      update(1, 0, n - 1, idx);
    }
    return unplaced;
  }
}
```

## Golang

```go
func numOfUnplacedFruits(fruits []int, baskets []int) int {
	n := len(baskets)
	if n == 0 {
		return len(fruits)
	}
	size := 4 * n
	tree := make([]int, size)

	var build func(node, l, r int)
	build = func(node, l, r int) {
		if l == r {
			tree[node] = baskets[l]
			return
		}
		mid := (l + r) >> 1
		build(node<<1, l, mid)
		build(node<<1|1, mid+1, r)
		if tree[node<<1] > tree[node<<1|1] {
			tree[node] = tree[node<<1]
		} else {
			tree[node] = tree[node<<1|1]
		}
	}
	build(1, 0, n-1)

	var update func(node, l, r, idx int)
	update = func(node, l, r, idx int) {
		if l == r {
			tree[node] = 0
			return
		}
		mid := (l + r) >> 1
		if idx <= mid {
			update(node<<1, l, mid, idx)
		} else {
			update(node<<1|1, mid+1, r, idx)
		}
		if tree[node<<1] > tree[node<<1|1] {
			tree[node] = tree[node<<1]
		} else {
			tree[node] = tree[node<<1|1]
		}
	}

	var findFirst func(node, l, r, need int) int
	findFirst = func(node, l, r, need int) int {
		if tree[node] < need {
			return -1
		}
		if l == r {
			return l
		}
		mid := (l + r) >> 1
		if tree[node<<1] >= need {
			return findFirst(node<<1, l, mid, need)
		}
		return findFirst(node<<1|1, mid+1, r, need)
	}

	unplaced := 0
	for _, f := range fruits {
		if tree[1] < f {
			unplaced++
			continue
		}
		idx := findFirst(1, 0, n-1, f)
		if idx != -1 {
			update(1, 0, n-1, idx)
		} else {
			unplaced++
		}
	}
	return unplaced
}
```

## Ruby

```ruby
def num_of_unplaced_fruits(fruits, baskets)
  n = fruits.length
  pairs = []
  baskets.each_with_index { |cap, i| pairs << [cap, i] }
  pairs.sort!
  caps = Array.new(n)
  idxs = Array.new(n)
  pos_of_idx = Array.new(n)
  pairs.each_with_index do |(c, i), pos|
    caps[pos] = c
    idxs[pos] = i
    pos_of_idx[i] = pos
  end

  size = 1
  size <<= 1 while size < n
  inf = (1 << 60)
  tree = Array.new(2 * size, inf)

  n.times { |i| tree[size + i] = idxs[i] }
  (size - 1).downto(1) { |i| tree[i] = [tree[2 * i], tree[2 * i + 1]].min }

  update = lambda do |pos|
    i = size + pos
    tree[i] = inf
    i >>= 1
    while i >= 1
      newv = [tree[2 * i], tree[2 * i + 1]].min
      break if tree[i] == newv
      tree[i] = newv
      i >>= 1
    end
  end

  query = lambda do |l, r|
    l += size
    r += size
    res = inf
    while l <= r
      if (l & 1) == 1
        res = [res, tree[l]].min
        l += 1
      end
      if (r & 1) == 0
        res = [res, tree[r]].min
        r -= 1
      end
      l >>= 1
      r >>= 1
    end
    res
  end

  unplaced = 0
  fruits.each do |f|
    lo = 0
    hi = n
    while lo < hi
      mid = (lo + hi) / 2
      if caps[mid] >= f
        hi = mid
      else
        lo = mid + 1
      end
    end
    pos = lo
    if pos == n
      unplaced += 1
      next
    end
    min_idx = query.call(pos, n - 1)
    if min_idx >= inf / 2
      unplaced += 1
    else
      p = pos_of_idx[min_idx]
      update.call(p)
    end
  end

  unplaced
end
```

## Scala

```scala
object Solution {
  def numOfUnplacedFruits(fruits: Array[Int], baskets: Array[Int]): Int = {
    val n = fruits.length

    class SegTree(val n: Int) {
      var size: Int = 1
      while (size < n) size <<= 1
      private val tree: Array[Int] = new Array[Int](size * 2)

      def build(arr: Array[Int]): Unit = {
        for (i <- 0 until n) tree(size + i) = arr(i)
        for (i <- n until size) tree(size + i) = Int.MinValue
        for (i <- size - 1 to 1 by -1) tree(i) = math.max(tree(i << 1), tree((i << 1) | 1))
      }

      def maxRoot: Int = tree(1)

      def update(idx: Int, value: Int): Unit = {
        var pos = idx + size
        tree(pos) = value
        pos >>= 1
        while (pos >= 1) {
          tree(pos) = math.max(tree(pos << 1), tree((pos << 1) | 1))
          pos >>= 1
        }
      }

      def findFirst(node: Int, l: Int, r: Int, fruit: Int): Int = {
        if (tree(node) < fruit) return -1
        if (l == r) return l
        val mid = (l + r) >>> 1
        val leftNode = node << 1
        if (tree(leftNode) >= fruit) findFirst(leftNode, l, mid, fruit)
        else findFirst(leftNode + 1, mid + 1, r, fruit)
      }
    }

    val seg = new SegTree(n)
    seg.build(baskets)

    var unplaced = 0
    for (fruit <- fruits) {
      if (seg.maxRoot < fruit) {
        unplaced += 1
      } else {
        val idx = seg.findFirst(1, 0, seg.size - 1, fruit)
        if (idx == -1 || idx >= n) unplaced += 1
        else seg.update(idx, Int.MinValue)
      }
    }
    unplaced
  }
}
```

## Rust

```rust
use std::cmp::max;

struct SegTree {
    size: usize,
    tree: Vec<i32>,
}

impl SegTree {
    fn new(arr: &[i32]) -> Self {
        let n = arr.len();
        let mut size = 1usize;
        while size < n {
            size <<= 1;
        }
        let mut tree = vec![0; size * 2];
        for i in 0..n {
            tree[size + i] = arr[i];
        }
        for i in (1..size).rev() {
            tree[i] = max(tree[i << 1], tree[i << 1 | 1]);
        }
        SegTree { size, tree }
    }

    fn update(&mut self, idx: usize, value: i32) {
        let mut pos = self.size + idx;
        self.tree[pos] = value;
        while pos > 1 {
            pos >>= 1;
            self.tree[pos] = max(self.tree[pos << 1], self.tree[pos << 1 | 1]);
        }
    }

    fn find_first(&self, need: i32) -> Option<usize> {
        if self.tree[1] < need {
            return None;
        }
        let mut node = 1usize;
        let mut l = 0usize;
        let mut r = self.size - 1;
        while l != r {
            let mid = (l + r) / 2;
            let left = node << 1;
            if self.tree[left] >= need {
                node = left;
                r = mid;
            } else {
                node = left | 1;
                l = mid + 1;
            }
        }
        Some(l)
    }
}

impl Solution {
    pub fn num_of_unplaced_fruits(fruits: Vec<i32>, baskets: Vec<i32>) -> i32 {
        let mut seg = SegTree::new(&baskets);
        let mut unplaced = 0i32;
        for f in fruits {
            if let Some(idx) = seg.find_first(f) {
                seg.update(idx, 0);
            } else {
                unplaced += 1;
            }
        }
        unplaced
    }
}
```

## Racket

```racket
(define/contract (num-of-unplaced-fruits fruits baskets)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((n (length baskets))
         ;; size is the smallest power of two >= n
         (size (let loop ((s 1)) (if (< s n) (loop (* s 2)) s)))
         (tree (make-vector (* 2 size) 0)))
    ;; initialize leaves
    (for ([i (in-range n)])
      (vector-set! tree (+ size i) (list-ref baskets i)))
    ;; build internal nodes (max)
    (let loop ((i (- size 1)))
      (when (>= i 1)
        (define left (vector-ref tree (* 2 i)))
        (define right (vector-ref tree (+ (* 2 i) 1)))
        (vector-set! tree i (max left right))
        (loop (- i 1))))
    ;; point update: set leaf idx to val and recompute ancestors
    (define (update idx val)
      (let ((pos (+ size idx)))
        (vector-set! tree pos val)
        (let loop ((p (quotient pos 2)))
          (when (> p 0)
            (define left (vector-ref tree (* 2 p)))
            (define right (vector-ref tree (+ (* 2 p) 1)))
            (vector-set! tree p (max left right))
            (loop (quotient p 2))))))
    ;; find leftmost index in [l,r] whose value >= x; returns -1 if none
    (define (find-first node l r x)
      (if (< (vector-ref tree node) x)
          -1
          (if (= l r)
              l
              (let* ((mid (quotient (+ l r) 2))
                     (left-node (* 2 node))
                     (right-node (+ left-node 1)))
                (if (>= (vector-ref tree left-node) x)
                    (find-first left-node l mid x)
                    (find-first right-node (+ mid 1) r x))))))
    ;; process fruits sequentially
    (let loop ((i 0) (unplaced 0))
      (if (= i n)
          unplaced
          (let* ((fruit (list-ref fruits i))
                 (idx (find-first 1 0 (- size 1) fruit)))
            (if (or (= idx -1) (>= idx n))
                (loop (+ i 1) (+ unplaced 1))
                (begin
                  (update idx 0)
                  (loop (+ i 1) unplaced))))))))
```

## Erlang

```erlang
-spec num_of_unplaced_fruits(Fruits :: [integer()], Baskets :: [integer()]) -> integer().
num_of_unplaced_fruits(Fruits, Baskets) ->
    N = length(Fruits),
    BlockSize = trunc(math:sqrt(N)) + 1,
    NumBlocks = (N + BlockSize - 1) div BlockSize,

    %% build baskets array (1‑based)
    EmptyB = array:new(N, [{default,0}]),
    {BasketsArr, _} =
        lists:foldl(
          fun({Val, Idx}, {Arr, _}) ->
                  {array:set(Idx, Val, Arr), Idx + 1}
          end,
          {EmptyB, 1},
          lists:zip(Baskets, lists:seq(1, N))
        ),

    %% build max per block array (1‑based)
    EmptyM = array:new(NumBlocks, [{default,0}]),
    MaxArr = build_max_blocks(1, NumBlocks, BlockSize, N, BasketsArr, EmptyM),

    %% process fruits
    process_fruits(Fruits, 1, BasketsArr, MaxArr,
                   BlockSize, N, NumBlocks, 0).

%% ------------------------------------------------------------------
%% Build max value for each block.
%% ------------------------------------------------------------------
build_max_blocks(BlockIdx, NumBlocks, _BlockSize, _N, _BasketsArr, MaxAcc)
    when BlockIdx > NumBlocks ->
    MaxAcc;
build_max_blocks(BlockIdx, NumBlocks, BlockSize, N, BasketsArr, MaxAcc) ->
    Start = (BlockIdx - 1) * BlockSize + 1,
    End   = erlang:min(N, BlockIdx * BlockSize),
    MaxVal = block_max(Start, End, BasketsArr, 0),
    NewMaxAcc = array:set(BlockIdx, MaxVal, MaxAcc),
    build_max_blocks(BlockIdx + 1, NumBlocks, BlockSize, N,
                     BasketsArr, NewMaxAcc).

block_max(I, End, _Arr, Cur) when I > End ->
    Cur;
block_max(I, End, Arr, Cur) ->
    Val = array:get(I, Arr),
    NewCur = if Val > Cur -> Val; true -> Cur end,
    block_max(I + 1, End, Arr, NewCur).

%% ------------------------------------------------------------------
%% Process each fruit, counting unplaced ones.
%% ------------------------------------------------------------------
process_fruits([], _Idx, _BArr, _MArr, _BS, _N, _NB, Count) ->
    Count;
process_fruits([Fruit | Rest], _Idx,
               BArr, MArr, BlockSize, N, NumBlocks, Count) ->
    case find_place(Fruit, 1, NumBlocks, BlockSize, N, BArr, MArr) of
        {NewB, NewM} ->
            process_fruits(Rest, 0, NewB, NewM,
                           BlockSize, N, NumBlocks, Count);
        not_found ->
            process_fruits(Rest, 0, BArr, MArr,
                           BlockSize, N, NumBlocks, Count + 1)
    end.

%% ------------------------------------------------------------------
%% Find the leftmost basket that can hold Fruit.
%% Returns {NewBasketsArray, NewMaxArray} if placed,
%% otherwise not_found.
%% ------------------------------------------------------------------
find_place(Fruit, BlockIdx, NumBlocks, _BlockSize, _N, BArr, MArr)
    when BlockIdx > NumBlocks ->
    not_found;
find_place(Fruit, BlockIdx, NumBlocks, BlockSize, N, BArr, MArr) ->
    MaxVal = array:get(BlockIdx, MArr),
    if MaxVal < Fruit ->
            find_place(Fruit, BlockIdx + 1, NumBlocks,
                       BlockSize, N, BArr, MArr);
       true ->
            Start = (BlockIdx - 1) * BlockSize + 1,
            End   = erlang:min(N, BlockIdx * BlockSize),
            case scan_block(Start, End, Fruit, BArr) of
                {found, Index} ->
                    NewB = array:set(Index, 0, BArr),
                    NewMaxVal = block_max(Start, End, NewB, 0),
                    NewM = array:set(BlockIdx, NewMaxVal, MArr),
                    {NewB, NewM};
                not_found ->
                    %% All baskets in this block are used despite MaxVal >= Fruit
                    find_place(Fruit, BlockIdx + 1, NumBlocks,
                               BlockSize, N, BArr, MArr)
            end
    end.

scan_block(I, End, _Fruit, _Arr) when I > End ->
    not_found;
scan_block(I, End, Fruit, Arr) ->
    Val = array:get(I, Arr),
    if Val >= Fruit ->
            {found, I};
       true ->
            scan_block(I + 1, End, Fruit, Arr)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec num_of_unplaced_fruits(fruits :: [integer], baskets :: [integer]) :: integer
  def num_of_unplaced_fruits(fruits, baskets) do
    n = length(baskets)

    size =
      Stream.iterate(1, &(&1 * 2))
      |> Enum.find(fn s -> s >= n end)

    tree_len = size * 2

    # initialize empty segment tree
    tree0 = :array.new(tree_len, default: 0)

    # set leaves with basket capacities
    tree1 =
      Enum.with_index(baskets)
      |> Enum.reduce(tree0, fn {val, i}, acc ->
        :array.set(i + size, val, acc)
      end)

    # build internal nodes (max values)
    tree =
      Enum.reduce((size - 1)..1, tree1, fn idx, acc ->
        left = :array.get(idx * 2, acc)
        right = :array.get(idx * 2 + 1, acc)
        maxv = if left > right, do: left, else: right
        :array.set(idx, maxv, acc)
      end)

    {_, unplaced} =
      Enum.reduce(fruits, {tree, 0}, fn fruit, {t, cnt} ->
        if :array.get(1, t) < fruit do
          {t, cnt + 1}
        else
          leaf_idx = find_index(t, size, fruit)
          pos = leaf_idx + size
          t2 = :array.set(pos, 0, t)
          t3 = update_upwards(t2, pos)
          {t3, cnt}
        end
      end)

    unplaced
  end

  # Recursively find the leftmost leaf index with value >= fruit
  defp find_index(tree, size, fruit), do: find_rec(tree, 1, size, fruit)

  defp find_rec(_tree, idx, size, _fruit) when idx >= size, do: idx - size

  defp find_rec(tree, idx, size, fruit) do
    left = idx * 2

    if :array.get(left, tree) >= fruit do
      find_rec(tree, left, size, fruit)
    else
      find_rec(tree, left + 1, size, fruit)
    end
  end

  # Update ancestors after setting a leaf to 0
  defp update_upwards(tree, pos) when pos == 1, do: tree

  defp update_upwards(tree, pos) do
    parent = div(pos, 2)

    left = :array.get(parent * 2, tree)
    right = :array.get(parent * 2 + 1, tree)
    maxv = if left > right, do: left, else: right

    t2 = :array.set(parent, maxv, tree)
    update_upwards(t2, parent)
  end
end
```
