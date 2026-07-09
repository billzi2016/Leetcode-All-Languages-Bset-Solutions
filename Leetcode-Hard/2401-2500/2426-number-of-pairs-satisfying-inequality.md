# 2426. Number of Pairs Satisfying Inequality

## Cpp

```cpp
class Solution {
public:
    struct Fenwick {
        int n;
        vector<int> bit;
        Fenwick(int n): n(n), bit(n+1,0) {}
        void add(int idx, int val){
            for(; idx<=n; idx+=idx&-idx) bit[idx] += val;
        }
        int sumPrefix(int idx){
            int res=0;
            for(; idx>0; idx-=idx&-idx) res += bit[idx];
            return res;
        }
    };
    
    long long numberOfPairs(vector<int>& nums1, vector<int>& nums2, int diff) {
        int n = nums1.size();
        vector<long long> a(n);
        for(int i=0;i<n;++i){
            a[i] = (long long)nums1[i] - (long long)nums2[i];
        }
        vector<long long> vals;
        vals.reserve(2*n);
        for(long long v: a){
            vals.push_back(v);
            vals.push_back(v - diff);
        }
        sort(vals.begin(), vals.end());
        vals.erase(unique(vals.begin(), vals.end()), vals.end());
        Fenwick bit(vals.size());
        long long ans = 0;
        int seen = 0;
        for(int i=n-1;i>=0;--i){
            long long need = a[i] - diff;
            int pos = lower_bound(vals.begin(), vals.end(), need) - vals.begin(); // first >= need
            int less = bit.sumPrefix(pos); // values with index < pos (since BIT is 1-indexed)
            ans += (long long)seen - less;
            int idxA = lower_bound(vals.begin(), vals.end(), a[i]) - vals.begin() + 1;
            bit.add(idxA, 1);
            ++seen;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long numberOfPairs(int[] nums1, int[] nums2, int diff) {
        int n = nums1.length;
        long[] a = new long[n];
        for (int i = 0; i < n; i++) {
            a[i] = (long) nums1[i] - (long) nums2[i];
        }
        // collect values for compression
        long[] all = new long[2 * n];
        int idx = 0;
        for (int i = 0; i < n; i++) {
            all[idx++] = a[i];
            all[idx++] = a[i] + diff;
        }
        java.util.Arrays.sort(all);
        // deduplicate
        int m = 0;
        for (int i = 0; i < all.length; i++) {
            if (i == 0 || all[i] != all[i - 1]) {
                all[m++] = all[i];
            }
        }
        long[] uniq = java.util.Arrays.copyOf(all, m);
        Fenwick fenwick = new Fenwick(m);
        long ans = 0;
        for (int i = 0; i < n; i++) {
            long target = a[i] + diff;
            int pos = upperBound(uniq, target); // number of elements <= target
            if (pos > 0) {
                ans += fenwick.query(pos);
            }
            int idxUpdate = lowerBound(uniq, a[i]) + 1; // 1‑based index for BIT
            fenwick.update(idxUpdate, 1);
        }
        return ans;
    }

    private int lowerBound(long[] arr, long key) {
        int l = 0, r = arr.length;
        while (l < r) {
            int mid = (l + r) >>> 1;
            if (arr[mid] >= key) r = mid;
            else l = mid + 1;
        }
        return l;
    }

    private int upperBound(long[] arr, long key) {
        int l = 0, r = arr.length;
        while (l < r) {
            int mid = (l + r) >>> 1;
            if (arr[mid] > key) r = mid;
            else l = mid + 1;
        }
        return l; // count of elements <= key
    }

    private static class Fenwick {
        private final long[] bit;
        private final int n;

        Fenwick(int n) {
            this.n = n;
            this.bit = new long[n + 2];
        }

        void update(int idx, long delta) {
            for (int i = idx; i <= n; i += i & -i) {
                bit[i] += delta;
            }
        }

        long query(int idx) {
            long res = 0;
            for (int i = idx; i > 0; i -= i & -i) {
                res += bit[i];
            }
            return res;
        }
    }
}
```

## Python

```python
class Solution(object):
    def numberOfPairs(self, nums1, nums2, diff):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type diff: int
        :rtype: int
        """
        n = len(nums1)
        A = [nums1[i] - nums2[i] for i in range(n)]
        
        # collect values for compression
        vals = set()
        for a in A:
            vals.add(a)
            vals.add(a - diff)
        sorted_vals = sorted(vals)
        idx_map = {v: i+1 for i, v in enumerate(sorted_vals)}  # 1-based index
        
        class BIT:
            def __init__(self, size):
                self.n = size
                self.bit = [0] * (size + 2)
            def update(self, i, delta):
                while i <= self.n:
                    self.bit[i] += delta
                    i += i & -i
            def query(self, i):
                s = 0
                while i > 0:
                    s += self.bit[i]
                    i -= i & -i
                return s
        
        bit = BIT(len(sorted_vals))
        ans = 0
        total = 0  # number of elements inserted so far (j > i)
        
        for i in range(n-1, -1, -1):
            thr = A[i] - diff
            idx_thr = idx_map[thr]
            cnt_ge = total - bit.query(idx_thr - 1)   # elements with value >= thr
            ans += cnt_ge
            
            idx_ai = idx_map[A[i]]
            bit.update(idx_ai, 1)
            total += 1
        
        return ans
```

## Python3

```python
class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], diff: int) -> int:
        from bisect import bisect_left

        n = len(nums1)
        a = [nums1[i] - nums2[i] for i in range(n)]

        vals = sorted(set(a))
        m = len(vals)

        class BIT:
            __slots__ = ("n", "bit")
            def __init__(self, n: int):
                self.n = n
                self.bit = [0] * (n + 1)
            def add(self, i: int, delta: int) -> None:
                while i <= self.n:
                    self.bit[i] += delta
                    i += i & -i
            def sum(self, i: int) -> int:
                s = 0
                while i:
                    s += self.bit[i]
                    i -= i & -i
                return s

        bit = BIT(m)
        ans = 0
        total = 0

        for i in range(n - 1, -1, -1):
            target = a[i] - diff
            pos = bisect_left(vals, target)          # number of values < target
            cnt_less = bit.sum(pos)                  # counts of inserted values < target
            ans += total - cnt_less

            idx = bisect_left(vals, a[i]) + 1        # BIT is 1-indexed
            bit.add(idx, 1)
            total += 1

        return ans
```

## C

```c
#include <stdlib.h>

static int cmp_ll(const void *a, const void *b) {
    long long la = *(const long long *)a;
    long long lb = *(const long long *)b;
    if (la < lb) return -1;
    if (la > lb) return 1;
    return 0;
}

/* binary search: first index >= target */
static int lower_bound(const long long *arr, int size, long long target) {
    int l = 0, r = size; // [l, r)
    while (l < r) {
        int m = l + ((r - l) >> 1);
        if (arr[m] < target) l = m + 1;
        else r = m;
    }
    return l;
}

/* Fenwick Tree */
typedef struct {
    long long *bit;
    int n;
} Fenwick;

static Fenwick* fenwick_create(int n) {
    Fenwick *f = (Fenwick *)malloc(sizeof(Fenwick));
    f->n = n;
    f->bit = (long long *)calloc(n + 1, sizeof(long long));
    return f;
}

static void fenwick_add(Fenwick *f, int idx, long long delta) {
    while (idx <= f->n) {
        f->bit[idx] += delta;
        idx += idx & -idx;
    }
}

static long long fenwick_sum(Fenwick *f, int idx) {
    long long res = 0;
    while (idx > 0) {
        res += f->bit[idx];
        idx -= idx & -idx;
    }
    return res;
}

static void fenwick_free(Fenwick *f) {
    free(f->bit);
    free(f);
}

/* Main solution */
long long numberOfPairs(int* nums1, int nums1Size, int* nums2, int nums2Size, int diff) {
    int n = nums1Size;
    long long *a = (long long *)malloc(n * sizeof(long long));
    for (int i = 0; i < n; ++i) {
        a[i] = (long long)nums1[i] - (long long)nums2[i];
    }

    /* collect values for compression */
    int totalVals = 2 * n;
    long long *vals = (long long *)malloc(totalVals * sizeof(long long));
    for (int i = 0; i < n; ++i) {
        vals[i] = a[i];
        vals[n + i] = a[i] - (long long)diff;
    }

    qsort(vals, totalVals, sizeof(long long), cmp_ll);
    /* unique */
    int m = 0;
    for (int i = 0; i < totalVals; ++i) {
        if (i == 0 || vals[i] != vals[i - 1]) {
            vals[m++] = vals[i];
        }
    }

    Fenwick *fen = fenwick_create(m);
    long long ans = 0;

    for (int i = n - 1; i >= 0; --i) {
        long long target = a[i] - (long long)diff;
        int idxLow = lower_bound(vals, m, target);          // first >= target
        long long totalInserted = fenwick_sum(fen, m);
        long long lessThanTarget = fenwick_sum(fen, idxLow); // sum up to idxLow (since BIT is 1-indexed)
        /* we need count of values >= target */
        ans += totalInserted - lessThanTarget;

        int pos = lower_bound(vals, m, a[i]) + 1;            // convert to 1-indexed
        fenwick_add(fen, pos, 1);
    }

    free(a);
    free(vals);
    fenwick_free(fen);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public long NumberOfPairs(int[] nums1, int[] nums2, int diff) {
        int n = nums1.Length;
        long[] a = new long[n];
        List<long> vals = new List<long>(n * 2);
        for (int i = 0; i < n; i++) {
            a[i] = (long)nums1[i] - (long)nums2[i];
            vals.Add(a[i]);
            vals.Add(a[i] + diff);
        }
        long[] uniq = vals.Distinct().ToArray();
        Array.Sort(uniq);
        var indexMap = new Dictionary<long, int>(uniq.Length);
        for (int i = 0; i < uniq.Length; i++) {
            indexMap[uniq[i]] = i + 1; // 1-based for BIT
        }
        Fenwick bit = new Fenwick(uniq.Length);
        long ans = 0;
        foreach (var val in a) {
            long target = val + diff;
            int pos = Array.BinarySearch(uniq, target);
            if (pos < 0) pos = ~pos - 1; // last index <= target
            else {
                // exact match found, keep pos as is (unique values)
            }
            int idxTarget = pos >= 0 ? pos + 1 : 0;
            if (idxTarget > 0) ans += bit.Query(idxTarget);
            int idxVal = indexMap[val];
            bit.Update(idxVal, 1);
        }
        return ans;
    }

    private class Fenwick {
        private readonly long[] tree;
        public Fenwick(int size) {
            tree = new long[size + 2];
        }
        public void Update(int idx, long delta) {
            for (int i = idx; i < tree.Length; i += i & -i) {
                tree[i] += delta;
            }
        }
        public long Query(int idx) {
            long sum = 0;
            for (int i = idx; i > 0; i -= i & -i) {
                sum += tree[i];
            }
            return sum;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} diff
 * @return {number}
 */
var numberOfPairs = function(nums1, nums2, diff) {
    const n = nums1.length;
    const a = new Array(n);
    for (let i = 0; i < n; ++i) {
        a[i] = nums1[i] - nums2[i];
    }

    // coordinate compression of a[i] and a[i] + diff
    const vals = [];
    for (let i = 0; i < n; ++i) {
        vals.push(a[i]);
        vals.push(a[i] + diff);
    }
    vals.sort((x, y) => x - y);
    const uniq = [];
    for (const v of vals) {
        if (uniq.length === 0 || uniq[uniq.length - 1] !== v) uniq.push(v);
    }
    const idxMap = new Map();
    for (let i = 0; i < uniq.length; ++i) {
        idxMap.set(uniq[i], i + 1); // 1‑based index for BIT
    }

    class BIT {
        constructor(size) {
            this.n = size;
            this.tree = new Array(size + 2).fill(0);
        }
        add(i, delta) {
            while (i <= this.n) {
                this.tree[i] += delta;
                i += i & -i;
            }
        }
        sum(i) {
            let res = 0;
            while (i > 0) {
                res += this.tree[i];
                i -= i & -i;
            }
            return res;
        }
    }

    const bit = new BIT(uniq.length);
    let ans = 0;

    for (let j = 0; j < n; ++j) {
        const targetIdx = idxMap.get(a[j] + diff);
        ans += bit.sum(targetIdx);          // count of previous a[i] <= a[j] + diff
        const curIdx = idxMap.get(a[j]);
        bit.add(curIdx, 1);                 // insert current a[j]
    }

    return ans;
};
```

## Typescript

```typescript
function numberOfPairs(nums1: number[], nums2: number[], diff: number): number {
    const n = nums1.length;
    const a: number[] = new Array(n);
    for (let i = 0; i < n; i++) a[i] = nums1[i] - nums2[i];

    const vals: number[] = [];
    for (let i = 0; i < n; i++) {
        vals.push(a[i]);
        vals.push(a[i] - diff);
    }
    vals.sort((x, y) => x - y);
    const uniq: number[] = [];
    for (const v of vals) {
        if (uniq.length === 0 || uniq[uniq.length - 1] !== v) uniq.push(v);
    }

    const indexMap = new Map<number, number>();
    for (let i = 0; i < uniq.length; i++) indexMap.set(uniq[i], i + 1); // 1‑based

    class BIT {
        private tree: number[];
        private n: number;
        constructor(n: number) {
            this.n = n;
            this.tree = new Array(n + 2).fill(0);
        }
        add(i: number, delta: number): void {
            for (let x = i; x <= this.n; x += x & -x) this.tree[x] += delta;
        }
        sum(i: number): number {
            let res = 0;
            for (let x = i; x > 0; x -= x & -x) res += this.tree[x];
            return res;
        }
    }

    function lowerBound(arr: number[], target: number): number {
        let l = 0, r = arr.length;
        while (l < r) {
            const m = (l + r) >> 1;
            if (arr[m] < target) l = m + 1;
            else r = m;
        }
        return l; // count of elements < target
    }

    const bit = new BIT(uniq.length);
    let totalSeen = 0;
    let ans = 0;

    for (let i = n - 1; i >= 0; i--) {
        const threshold = a[i] - diff;
        const idxLess = lowerBound(uniq, threshold); // number of values < threshold
        const lessCount = bit.sum(idxLess);
        const geCount = totalSeen - lessCount;
        ans += geCount;

        const idx = indexMap.get(a[i])!;
        bit.add(idx, 1);
        totalSeen++;
    }

    return ans;
}
```

## Php

```php
class Fenwick {
    private $tree;
    private $n;
    public function __construct($n) {
        $this->n = $n;
        $this->tree = array_fill(0, $n + 2, 0);
    }
    public function update($i, $delta) {
        for (; $i <= $this->n; $i += $i & (-$i)) {
            $this->tree[$i] += $delta;
        }
    }
    public function query($i) {
        $sum = 0;
        for (; $i > 0; $i -= $i & (-$i)) {
            $sum += $this->tree[$i];
        }
        return $sum;
    }
    public function rangeQuery($l, $r) {
        if ($l > $r) return 0;
        return $this->query($r) - $this->query($l - 1);
    }
}
function lowerBound($arr, $target) {
    $low = 0;
    $high = count($arr);
    while ($low < $high) {
        $mid = intdiv($low + $high, 2);
        if ($arr[$mid] < $target) {
            $low = $mid + 1;
        } else {
            $high = $mid;
        }
    }
    return $low;
}
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @param Integer $diff
     * @return Integer
     */
    function numberOfPairs($nums1, $nums2, $diff) {
        $n = count($nums1);
        $b = [];
        for ($i = 0; $i < $n; $i++) {
            $b[$i] = $nums1[$i] - $nums2[$i];
        }
        $vals = $b;
        foreach ($b as $v) {
            $vals[] = $v - $diff;
        }
        sort($vals);
        $sortedVals = array_values(array_unique($vals));
        $size = count($sortedVals);
        $fenwick = new Fenwick($size);
        $ans = 0;
        for ($i = $n - 1; $i >= 0; $i--) {
            $threshold = $b[$i] - $diff;
            $idx = lowerBound($sortedVals, $threshold); // first index with value >= threshold
            $l = $idx + 1; // convert to 1‑based Fenwick index
            if ($l <= $size) {
                $ans += $fenwick->rangeQuery($l, $size);
            }
            $pos = lowerBound($sortedVals, $b[$i]); // exact position of b[i]
            $fenwick->update($pos + 1, 1);
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func numberOfPairs(_ nums1: [Int], _ nums2: [Int], _ diff: Int) -> Int {
        let n = nums1.count
        var a = [Int](repeating: 0, count: n)
        for i in 0..<n {
            a[i] = nums1[i] - nums2[i]
        }
        
        // coordinate compression of values in a
        var setVals = Set<Int>()
        for v in a { setVals.insert(v) }
        let sortedVals = Array(setVals).sorted()
        let m = sortedVals.count
        
        let fenwick = Fenwick(m)
        var result: Int64 = 0
        
        for i in stride(from: n - 1, through: 0, by: -1) {
            let target = a[i] - diff
            let idx = lowerBound(sortedVals, target)
            if idx < m {
                let total = fenwick.query(m - 1)
                let less = fenwick.query(idx - 1)
                result += Int64(total - less)
            }
            // insert current value
            let pos = lowerBound(sortedVals, a[i])   // exact position
            fenwick.update(pos, 1)
        }
        return Int(result)
    }
}

// Fenwick Tree for prefix sums
private class Fenwick {
    private var tree: [Int]
    private let n: Int
    
    init(_ size: Int) {
        self.n = size
        self.tree = Array(repeating: 0, count: size + 1)
    }
    
    func update(_ index: Int, _ delta: Int) {
        var i = index + 1
        while i <= n {
            tree[i] += delta
            i += i & -i
        }
    }
    
    // sum of [0...index]
    func query(_ index: Int) -> Int {
        if index < 0 { return 0 }
        var i = index + 1
        var res = 0
        while i > 0 {
            res += tree[i]
            i -= i & -i
        }
        return res
    }
}

// lower bound: first position where arr[pos] >= target
private func lowerBound(_ arr: [Int], _ target: Int) -> Int {
    var left = 0, right = arr.count
    while left < right {
        let mid = (left + right) >> 1
        if arr[mid] < target {
            left = mid + 1
        } else {
            right = mid
        }
    }
    return left
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfPairs(nums1: IntArray, nums2: IntArray, diff: Int): Long {
        val n = nums1.size
        val a = LongArray(n)
        for (i in 0 until n) {
            a[i] = nums1[i].toLong() - nums2[i].toLong()
        }
        val values = mutableListOf<Long>()
        for (v in a) {
            values.add(v)
            values.add(v + diff)
        }
        val sorted = values.distinct().sorted()
        val indexMap = HashMap<Long, Int>(sorted.size * 2)
        for ((idx, v) in sorted.withIndex()) {
            indexMap[v] = idx + 1 // 1‑based for BIT
        }

        class Fenwick(private val size: Int) {
            private val tree = LongArray(size + 2)
            fun update(idx0: Int, delta: Long) {
                var idx = idx0
                while (idx <= size) {
                    tree[idx] += delta
                    idx += idx and -idx
                }
            }

            fun query(idx0: Int): Long {
                var idx = idx0
                var res = 0L
                while (idx > 0) {
                    res += tree[idx]
                    idx -= idx and -idx
                }
                return res
            }
        }

        val bit = Fenwick(sorted.size)
        var ans = 0L
        for (j in 0 until n) {
            val key = a[j] + diff
            val qIdx = indexMap[key]!!
            ans += bit.query(qIdx)
            val updIdx = indexMap[a[j]]!!
            bit.update(updIdx, 1L)
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int numberOfPairs(List<int> nums1, List<int> nums2, int diff) {
    int n = nums1.length;
    List<int> a = List.generate(n, (i) => nums1[i] - nums2[i]);

    // coordinate compression of values in a
    List<int> sortedVals = List.from(a);
    sortedVals.sort();
    sortedVals = sortedVals.toSet().toList(); // unique and sorted

    Map<int, int> indexMap = {};
    for (int i = 0; i < sortedVals.length; ++i) {
      indexMap[sortedVals[i]] = i;
    }

    BIT bit = BIT(sortedVals.length);
    int totalSeen = 0;
    int ans = 0;

    for (int i = n - 1; i >= 0; --i) {
      int target = a[i] - diff;
      int idx = _lowerBound(sortedVals, target); // first position >= target
      int lessCount = bit.sum(idx); // number of elements with value < target
      ans += totalSeen - lessCount;

      int pos = indexMap[a[i]]!;
      bit.add(pos + 1, 1);
      totalSeen++;
    }

    return ans;
  }

  int _lowerBound(List<int> list, int target) {
    int l = 0, r = list.length;
    while (l < r) {
      int m = (l + r) >> 1;
      if (list[m] < target) {
        l = m + 1;
      } else {
        r = m;
      }
    }
    return l;
  }
}

class BIT {
  final List<int> _tree;
  final int _n;

  BIT(this._n) : _tree = List.filled(_n + 2, 0);

  void add(int idx, int delta) {
    for (int i = idx; i <= _n; i += i & -i) {
      _tree[i] += delta;
    }
  }

  int sum(int idx) {
    int res = 0;
    for (int i = idx; i > 0; i -= i & -i) {
      res += _tree[i];
    }
    return res;
  }
}
```

## Golang

```go
package main

import (
	"sort"
)

type Fenwick struct {
	tree []int64
}

func NewFenwick(n int) *Fenwick {
	return &Fenwick{tree: make([]int64, n+1)}
}

func (f *Fenwick) Add(idx int, delta int64) {
	for i := idx; i < len(f.tree); i += i & -i {
		f.tree[i] += delta
	}
}

func (f *Fenwick) Sum(idx int) int64 {
	var res int64
	for i := idx; i > 0; i -= i & -i {
		res += f.tree[i]
	}
	return res
}

func numberOfPairs(nums1 []int, nums2 []int, diff int) int64 {
	n := len(nums1)
	a := make([]int, n)
	for i := 0; i < n; i++ {
		a[i] = nums1[i] - nums2[i]
	}
	vals := make([]int, n)
	copy(vals, a)
	sort.Ints(vals)
	uniq := make([]int, 0, n)
	for _, v := range vals {
		if len(uniq) == 0 || uniq[len(uniq)-1] != v {
			uniq = append(uniq, v)
		}
	}
	ft := NewFenwick(len(uniq))
	var ans int64
	total := 0
	for i := n - 1; i >= 0; i-- {
		target := a[i] - diff
		idx := sort.Search(len(uniq), func(j int) bool { return uniq[j] >= target })
		less := ft.Sum(idx)
		cntGe := total - int(less)
		ans += int64(cntGe)

		pos := sort.Search(len(uniq), func(j int) bool { return uniq[j] >= a[i] })
		ft.Add(pos+1, 1)
		total++
	}
	return ans
}
```

## Ruby

```ruby
class BIT
  def initialize(n)
    @n = n
    @tree = Array.new(n + 2, 0)
  end

  def add(i, delta)
    while i <= @n
      @tree[i] += delta
      i += i & -i
    end
  end

  def sum(i)
    s = 0
    while i > 0
      s += @tree[i]
      i -= i & -i
    end
    s
  end
end

def lower_bound(arr, target)
  l = 0
  r = arr.length
  while l < r
    m = (l + r) / 2
    if arr[m] < target
      l = m + 1
    else
      r = m
    end
  end
  l
end

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer} diff
# @return {Integer}
def number_of_pairs(nums1, nums2, diff)
  n = nums1.length
  a = Array.new(n) { |i| nums1[i] - nums2[i] }

  vals = a + a.map { |x| x - diff }
  sorted = vals.uniq.sort
  index_map = {}
  sorted.each_with_index { |v, i| index_map[v] = i + 1 } # 1-based

  bit = BIT.new(sorted.length)
  ans = 0

  (n - 1).downto(0) do |i|
    threshold = a[i] - diff
    idx_thr = lower_bound(sorted, threshold) + 1 # first >= threshold, 1‑based
    if idx_thr <= sorted.length
      cnt = bit.sum(sorted.length) - bit.sum(idx_thr - 1)
      ans += cnt
    end
    bit.add(index_map[a[i]], 1)
  end

  ans
end
```

## Scala

```scala
object Solution {
  def numberOfPairs(nums1: Array[Int], nums2: Array[Int], diff: Int): Long = {
    val n = nums1.length
    val a = new Array[Int](n)
    var i = 0
    while (i < n) {
      a(i) = nums1(i) - nums2(i)
      i += 1
    }
    val sortedVals = a.distinct.sorted

    class BIT(size: Int) {
      private val tree = Array.fill[Long](size + 2)(0L)
      def add(idx0: Int, delta: Long): Unit = {
        var idx = idx0
        while (idx <= size) {
          tree(idx) += delta
          idx += idx & -idx
        }
      }
      def sum(idx0: Int): Long = {
        var idx = idx0
        var res = 0L
        while (idx > 0) {
          res += tree(idx)
          idx -= idx & -idx
        }
        res
      }
    }

    def lowerBound(arr: Array[Int], target: Int): Int = {
      var l = 0
      var r = arr.length
      while (l < r) {
        val m = (l + r) >>> 1
        if (arr(m) < target) l = m + 1 else r = m
      }
      l
    }

    val bit = new BIT(sortedVals.length)
    var seen: Long = 0L
    var ans: Long = 0L

    var idx = n - 1
    while (idx >= 0) {
      val ai = a(idx)
      val t = ai - diff
      val pos = lowerBound(sortedVals, t) // number of values < t
      val less = bit.sum(pos) // sum of first 'pos' elements
      ans += seen - less

      val posAi = java.util.Arrays.binarySearch(sortedVals, ai)
      val insertPos = if (posAi >= 0) posAi else -posAi - 1
      bit.add(insertPos + 1, 1L)

      seen += 1L
      idx -= 1
    }

    ans
  }
}
```

## Rust

```rust
use std::cmp::Ordering;

struct Fenwick {
    n: usize,
    tree: Vec<i64>,
}

impl Fenwick {
    fn new(n: usize) -> Self {
        Fenwick { n, tree: vec![0; n + 1] }
    }

    fn add(&mut self, mut idx: usize, delta: i64) {
        idx += 1;
        while idx <= self.n {
            self.tree[idx] += delta;
            idx += idx & (!idx + 1);
        }
    }

    // sum of [0, idx)
    fn sum(&self, mut idx: usize) -> i64 {
        let mut res = 0i64;
        while idx > 0 {
            res += self.tree[idx];
            idx &= idx - 1;
        }
        res
    }
}

impl Solution {
    pub fn number_of_pairs(nums1: Vec<i32>, nums2: Vec<i32>, diff: i32) -> i64 {
        let n = nums1.len();
        let mut a: Vec<i64> = Vec::with_capacity(n);
        for i in 0..n {
            a.push(nums1[i] as i64 - nums2[i] as i64);
        }

        // coordinate compression of a values
        let mut uniq = a.clone();
        uniq.sort_unstable();
        uniq.dedup();

        let mut fenwick = Fenwick::new(uniq.len());
        let mut ans: i64 = 0;

        for i in (0..n).rev() {
            let ai = a[i];
            let threshold = ai - diff as i64;

            // position of first element >= threshold
            let pos = match uniq.binary_search(&threshold) {
                Ok(p) => p,
                Err(p) => p,
            };

            let total = fenwick.sum(uniq.len());
            let less = fenwick.sum(pos);
            ans += total - less;

            // add current ai to Fenwick tree
            let idx_ai = uniq.binary_search(&ai).unwrap();
            fenwick.add(idx_ai, 1);
        }

        ans
    }
}
```

## Racket

```racket
#lang racket

(require racket/list)

(provide number-of-pairs)

(define (lower-bound vec target)
  (let loop ([lo 0] [hi (vector-length vec)])
    (if (= lo hi)
        lo
        (let* ([mid (quotient (+ lo hi) 2)]
               [mid-val (vector-ref vec mid)])
          (if (< mid-val target)
              (loop (+ mid 1) hi)
              (loop lo mid))))))

(define (fenwick-add! ft idx delta)
  (let ([n (vector-length ft)])
    (let loop ([i idx])
      (when (< i n)
        (vector-set! ft i (+ (vector-ref ft i) delta))
        (loop (+ i (bitwise-and i (- i))))))))

(define (fenwick-sum ft idx)
  (let loop ([i idx] [acc 0])
    (if (= i 0)
        acc
        (loop (bitwise-and i (- i)) (+ acc (vector-ref ft i))))))

(define/contract (number-of-pairs nums1 nums2 diff)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([n (length nums1)]
         [a-list (map - nums1 nums2)]
         [sorted (sort a-list <)]
         [all-vals (list->vector (remove-duplicates sorted))]
         [m (vector-length all-vals)]
         [ft (make-vector (+ m 1) 0)])
    (let loop ([i (- n 1)] [totalSeen 0] [ans 0])
      (if (< i 0)
          ans
          (let* ([a (list-ref a-list i)]
                 [threshold (- a diff)]
                 [idxThresh (lower-bound all-vals threshold)]
                 [sumLess (if (= idxThresh 0) 0 (fenwick-sum ft idxThresh))]
                 [countGe (- totalSeen sumLess)]
                 [ans2 (+ ans countGe)])
            (let ([idxA (lower-bound all-vals a)]) ; exact position
              (fenwick-add! ft (+ idxA 1) 1)
              (loop (- i 1) (+ totalSeen 1) ans2)))))))
```

## Erlang

```erlang
-spec number_of_pairs(Nums1 :: [integer()], Nums2 :: [integer()], Diff :: integer()) -> integer().
number_of_pairs(Nums1, Nums2, Diff) ->
    A = lists:zipwith(fun(X, Y) -> X - Y end, Nums1, Nums2),
    SortedVals = lists:usort(A),
    Size = length(SortedVals),
    Tuple = list_to_tuple(SortedVals),
    ValueToIdx = build_index_map(SortedVals, 1, #{}),
    Bit0 = bit_new(Size),
    RevA = lists:reverse(A),
    {Ans, _BitFinal, _Tot} =
        lists:foldl(
            fun(Val, {AccAns, AccBit, Tot}) ->
                Thresh = Val - Diff,
                Pos = lower_bound(Thresh, Tuple, Size),          % first index >= Thresh
                Prefix = case Pos of
                             1 -> 0;
                             _ -> bit_sum(AccBit, Pos - 1)
                         end,
                CountGe = Tot - Prefix,
                NewAns = AccAns + CountGe,
                IdxA = maps:get(Val, ValueToIdx),
                NewBit = bit_add(AccBit, IdxA, 1),
                {NewAns, NewBit, Tot + 1}
            end,
            {0, Bit0, 0},
            RevA
        ),
    Ans.

%% Build map from value to its 1‑based index in the sorted unique array.
-spec build_index_map([integer()], integer(), map()) -> map().
build_index_map([], _Idx, Map) ->
    Map;
build_index_map([H | T], Idx, Map) ->
    build_index_map(T, Idx + 1, maps:put(H, Idx, Map)).

%% Binary search for the first position (1‑based) where Tuple[pos] >= Target.
-spec lower_bound(integer(), tuple(), integer()) -> integer().
lower_bound(Target, Tuple, Size) ->
    lower_bound(1, Size + 1, Target, Tuple).

-spec lower_bound(integer(), integer(), integer(), tuple()) -> integer().
lower_bound(Low, High, _Target, _Tuple) when Low >= High ->
    Low;
lower_bound(Low, High, Target, Tuple) ->
    Mid = (Low + High) bsr 1,
    Val = element(Mid, Tuple),
    if
        Val < Target -> lower_bound(Mid + 1, High, Target, Tuple);
        true          -> lower_bound(Low, Mid, Target, Tuple)
    end.

%% Fenwick tree (Binary Indexed Tree) implementation using a map.
-spec bit_new(integer()) -> {integer(), map()}.
bit_new(Size) ->
    {Size, #{}}.

-spec bit_add({integer(), map()}, integer(), integer()) -> {integer(), map()}.
bit_add({Size, M}, Index, Delta) when Index =< Size ->
    NewM = add_loop(Index, Delta, Size, M),
    {Size, NewM};
bit_add(Bit, _Index, _Delta) ->
    Bit.

-spec add_loop(integer(), integer(), integer(), map()) -> map().
add_loop(I, D, Size, M) when I =< Size ->
    V = maps:get(I, M, 0) + D,
    M1 = maps:put(I, V, M),
    add_loop(I + (I band -I), D, Size, M1);
add_loop(_I, _D, _Size, M) ->
    M.

-spec bit_sum({integer(), map()}, integer()) -> integer().
bit_sum({_, M}, Index) ->
    sum_loop(Index, M, 0).

-spec sum_loop(integer(), map(), integer()) -> integer().
sum_loop(0, _M, Acc) ->
    Acc;
sum_loop(I, M, Acc) ->
    V = maps:get(I, M, 0),
    sum_loop(I - (I band -I), M, Acc + V).
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_pairs(nums1 :: [integer], nums2 :: [integer], diff :: integer) :: integer
  def number_of_pairs(nums1, nums2, diff) do
    a = Enum.zip(nums1, nums2) |> Enum.map(fn {x, y} -> x - y end)

    vals =
      (a ++ Enum.map(a, fn v -> v + diff end))
      |> Enum.uniq()
      |> Enum.sort()

    compress = Map.new(Enum.with_index(vals, 1), fn {v, i} -> {v, i} end)
    size = length(vals)

    bit = :array.new(size + 2, 0)

    {ans, _bit} =
      Enum.reduce(a, {0, bit}, fn val, {acc, bit_acc} ->
        target = val + diff
        idx_target = Map.get(compress, target)
        cnt = query(bit_acc, idx_target)

        idx_val = Map.get(compress, val)
        new_bit = update(bit_acc, size, idx_val, 1)

        {acc + cnt, new_bit}
      end)

    ans
  end

  defp update(bit, size, idx, delta) when idx <= size do
    cur = :array.get(idx, bit)
    bit2 = :array.set(idx, cur + delta, bit)
    update(bit2, size, idx + (idx &&& -idx), delta)
  end

  defp update(bit, size, idx, _delta) when idx > size do
    bit
  end

  defp query(bit, idx) when idx > 0 do
    cur = :array.get(idx, bit)
    cur + query(bit, idx - (idx &&& -idx))
  end

  defp query(_bit, 0), do: 0
end
```
