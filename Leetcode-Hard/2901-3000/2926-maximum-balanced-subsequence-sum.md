# 2926. Maximum Balanced Subsequence Sum

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Fenwick {
    vector<long long> bit;
    int n;
public:
    Fenwick(int n): n(n), bit(n + 1, LLONG_MIN) {}
    void update(int idx, long long val) {
        for (; idx <= n; idx += idx & -idx)
            bit[idx] = max(bit[idx], val);
    }
    long long query(int idx) const {
        long long res = LLONG_MIN;
        for (; idx > 0; idx -= idx & -idx)
            res = max(res, bit[idx]);
        return res;
    }
};

class Solution {
public:
    long long maxBalancedSubsequenceSum(vector<int>& nums) {
        int n = nums.size();
        vector<long long> keys(n);
        for (int i = 0; i < n; ++i)
            keys[i] = (long long)nums[i] - i;
        vector<long long> comp = keys;
        sort(comp.begin(), comp.end());
        comp.erase(unique(comp.begin(), comp.end()), comp.end());
        Fenwick ft(comp.size());
        long long answer = LLONG_MIN;
        for (int i = 0; i < n; ++i) {
            long long key = keys[i];
            int pos = lower_bound(comp.begin(), comp.end(), key) - comp.begin() + 1; // 1-indexed
            long long bestPrev = ft.query(pos);
            long long dp_i;
            if (bestPrev == LLONG_MIN)
                dp_i = nums[i];
            else
                dp_i = max((long long)nums[i], (long long)nums[i] + bestPrev);
            answer = max(answer, dp_i);
            ft.update(pos, dp_i);
        }
        return answer;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public long maxBalancedSubsequenceSum(int[] nums) {
        int n = nums.length;
        long[] keys = new long[n];
        for (int i = 0; i < n; i++) {
            keys[i] = (long) nums[i] - i;
        }

        // Coordinate compression
        long[] sorted = keys.clone();
        Arrays.sort(sorted);
        int m = 0;
        long[] uniq = new long[n];
        for (long v : sorted) {
            if (m == 0 || v != uniq[m - 1]) {
                uniq[m++] = v;
            }
        }

        BIT bit = new BIT(m);
        long answer = Long.MIN_VALUE;

        for (int i = 0; i < n; i++) {
            int idx = Arrays.binarySearch(uniq, 0, m, keys[i]);
            idx++; // make it 1-indexed for BIT
            long bestPrev = bit.query(idx);
            long dp = nums[i];
            if (bestPrev != Long.MIN_VALUE) {
                long cand = nums[i] + bestPrev;
                if (cand > dp) dp = cand;
            }
            if (dp > answer) answer = dp;
            bit.update(idx, dp);
        }

        return answer;
    }

    private static class BIT {
        private final long[] tree;

        BIT(int size) {
            tree = new long[size + 2];
            Arrays.fill(tree, Long.MIN_VALUE);
        }

        void update(int i, long val) {
            for (int n = tree.length; i < n; i += i & -i) {
                if (val > tree[i]) tree[i] = val;
            }
        }

        long query(int i) {
            long res = Long.MIN_VALUE;
            for (; i > 0; i -= i & -i) {
                if (tree[i] > res) res = tree[i];
            }
            return res;
        }
    }
}
```

## Python

```python
class Solution(object):
    def maxBalancedSubsequenceSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        vals = [num - i for i, num in enumerate(nums)]
        uniq = sorted(set(vals))
        comp = {v: i + 1 for i, v in enumerate(uniq)}  # 1-indexed for BIT

        size = len(uniq)
        INF_NEG = -(10**18)

        tree = [INF_NEG] * (size + 2)

        def bit_update(pos, value):
            while pos <= size:
                if value > tree[pos]:
                    tree[pos] = value
                pos += pos & -pos

        def bit_query(pos):
            res = INF_NEG
            while pos > 0:
                if tree[pos] > res:
                    res = tree[pos]
                pos -= pos & -pos
            return res

        ans = INF_NEG
        for i, num in enumerate(nums):
            v = num - i
            idx = comp[v]
            best = bit_query(idx)          # max dp[j] with nums[j]-j <= v
            dp_i = max(num, num + best)
            if dp_i > ans:
                ans = dp_i
            bit_update(idx, dp_i)

        return ans
```

## Python3

```python
class Solution:
    def maxBalancedSubsequenceSum(self, nums):
        n = len(nums)
        keys = [nums[i] - i for i in range(n)]
        uniq = sorted(set(keys))
        comp = {v: i + 1 for i, v in enumerate(uniq)}  # 1-indexed BIT
        m = len(uniq)
        INF_NEG = -(10**18)
        bit = [INF_NEG] * (m + 2)

        def query(i):
            res = INF_NEG
            while i:
                if bit[i] > res:
                    res = bit[i]
                i -= i & -i
            return res

        def update(i, val):
            while i <= m:
                if val > bit[i]:
                    bit[i] = val
                i += i & -i

        ans = INF_NEG
        for i in range(n):
            idx = comp[keys[i]]
            best = query(idx)
            cur = nums[i]
            if best != INF_NEG:
                cand = nums[i] + best
                if cand > cur:
                    cur = cand
            update(idx, cur)
            if cur > ans:
                ans = cur
        return ans
```

## C

```c
#include <stdlib.h>
#include <limits.h>

static int cmp_ll(const void *a, const void *b) {
    long long x = *(const long long *)a;
    long long y = *(const long long *)b;
    if (x < y) return -1;
    if (x > y) return 1;
    return 0;
}

/* Fenwick tree for prefix maximum */
static void fenwick_update(long long *tree, int size, int idx, long long val) {
    while (idx <= size) {
        if (tree[idx] < val) tree[idx] = val;
        idx += idx & -idx;
    }
}

static long long fenwick_query(long long *tree, int idx) {
    long long res = LLONG_MIN;
    while (idx > 0) {
        if (tree[idx] > res) res = tree[idx];
        idx -= idx & -idx;
    }
    return res;
}

/* binary search for lower bound */
static int lower_bound_ll(const long long *arr, int n, long long target) {
    int l = 0, r = n; // [l, r)
    while (l < r) {
        int m = l + ((r - l) >> 1);
        if (arr[m] < target) l = m + 1;
        else r = m;
    }
    return l;
}

long long maxBalancedSubsequenceSum(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    int n = numsSize;

    long long *val = (long long *)malloc(sizeof(long long) * n);
    for (int i = 0; i < n; ++i) {
        val[i] = (long long)nums[i] - i;
    }

    /* coordinate compression */
    long long *comp = (long long *)malloc(sizeof(long long) * n);
    for (int i = 0; i < n; ++i) comp[i] = val[i];
    qsort(comp, n, sizeof(long long), cmp_ll);
    int m = 0;
    for (int i = 0; i < n; ++i) {
        if (i == 0 || comp[i] != comp[i - 1]) {
            comp[m++] = comp[i];
        }
    }

    long long *tree = (long long *)malloc(sizeof(long long) * (m + 2));
    for (int i = 0; i <= m + 1; ++i) tree[i] = LLONG_MIN;

    long long answer = LLONG_MIN;
    for (int i = 0; i < n; ++i) {
        int idx = lower_bound_ll(comp, m, val[i]) + 1; // Fenwick is 1-indexed
        long long bestPrev = fenwick_query(tree, idx);
        long long cur = (long long)nums[i];
        if (bestPrev != LLONG_MIN) {
            long long cand = (long long)nums[i] + bestPrev;
            if (cand > cur) cur = cand;
        }
        fenwick_update(tree, m, idx, cur);
        if (cur > answer) answer = cur;
    }

    free(val);
    free(comp);
    free(tree);
    return answer;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public long MaxBalancedSubsequenceSum(int[] nums) {
        int n = nums.Length;
        long[] keys = new long[n];
        for (int i = 0; i < n; i++) {
            keys[i] = (long)nums[i] - i;
        }

        var sorted = keys.Distinct().ToList();
        sorted.Sort();

        var dict = new Dictionary<long, int>(sorted.Count);
        for (int i = 0; i < sorted.Count; i++) {
            dict[sorted[i]] = i + 1; // 1‑based index for Fenwick
        }

        var fenwick = new Fenwick(sorted.Count);
        long answer = long.MinValue;

        for (int i = 0; i < n; i++) {
            int idx = dict[keys[i]];
            long bestPrev = fenwick.Query(idx);
            if (bestPrev < 0) bestPrev = 0;
            long cur = (long)nums[i] + bestPrev;
            if (cur > answer) answer = cur;
            fenwick.Update(idx, cur);
        }

        return answer;
    }

    private class Fenwick {
        private readonly long[] bit;
        private readonly int size;

        public Fenwick(int n) {
            size = n;
            bit = new long[n + 2];
            for (int i = 0; i < bit.Length; i++) bit[i] = long.MinValue;
        }

        public void Update(int idx, long val) {
            while (idx <= size) {
                if (val > bit[idx]) bit[idx] = val;
                idx += idx & -idx;
            }
        }

        public long Query(int idx) {
            long res = long.MinValue;
            while (idx > 0) {
                if (bit[idx] > res) res = bit[idx];
                idx -= idx & -idx;
            }
            return res;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxBalancedSubsequenceSum = function(nums) {
    const n = nums.length;
    // compute transformed values v_i = nums[i] - i
    const vals = new Array(n);
    for (let i = 0; i < n; ++i) {
        vals[i] = nums[i] - i;
    }
    // coordinate compression
    const sorted = Array.from(new Set(vals)).sort((a, b) => a - b);
    const indexMap = new Map();
    for (let i = 0; i < sorted.length; ++i) {
        indexMap.set(sorted[i], i + 1); // 1‑based for BIT
    }
    class Fenwick {
        constructor(size) {
            this.n = size;
            this.tree = new Array(size + 2).fill(Number.NEGATIVE_INFINITY);
        }
        update(i, val) {
            for (let x = i; x <= this.n; x += x & -x) {
                if (val > this.tree[x]) this.tree[x] = val;
            }
        }
        query(i) {
            let res = Number.NEGATIVE_INFINITY;
            for (let x = i; x > 0; x -= x & -x) {
                if (this.tree[x] > res) res = this.tree[x];
            }
            return res;
        }
    }
    const bit = new Fenwick(sorted.length);
    let answer = Number.NEGATIVE_INFINITY;
    for (let i = 0; i < n; ++i) {
        const idx = indexMap.get(vals[i]);
        const bestPrev = bit.query(idx);
        let cur;
        if (bestPrev === Number.NEGATIVE_INFINITY) {
            cur = nums[i];
        } else {
            cur = Math.max(nums[i], nums[i] + bestPrev);
        }
        if (cur > answer) answer = cur;
        bit.update(idx, cur);
    }
    return answer;
};
```

## Typescript

```typescript
function maxBalancedSubsequenceSum(nums: number[]): number {
    const n = nums.length;
    const keys = new Array<number>(n);
    for (let i = 0; i < n; i++) {
        keys[i] = nums[i] - i;
    }
    const uniq = Array.from(new Set(keys)).sort((a, b) => a - b);
    const comp = new Map<number, number>();
    for (let i = 0; i < uniq.length; i++) {
        comp.set(uniq[i], i + 1); // 1‑based index for BIT
    }

    class Fenwick {
        n: number;
        tree: number[];
        constructor(n: number) {
            this.n = n;
            this.tree = new Array(n + 2).fill(Number.NEGATIVE_INFINITY);
        }
        update(i: number, val: number): void {
            for (let x = i; x <= this.n; x += x & -x) {
                if (val > this.tree[x]) this.tree[x] = val;
            }
        }
        query(i: number): number {
            let res = Number.NEGATIVE_INFINITY;
            for (let x = i; x > 0; x -= x & -x) {
                if (this.tree[x] > res) res = this.tree[x];
            }
            return res;
        }
    }

    const bit = new Fenwick(uniq.length);
    let answer = Number.NEGATIVE_INFINITY;

    for (let i = 0; i < n; i++) {
        const idx = comp.get(keys[i])!;
        const bestPrev = bit.query(idx);
        let cur = nums[i];
        if (bestPrev > Number.NEGATIVE_INFINITY) {
            cur = Math.max(cur, nums[i] + bestPrev);
        }
        bit.update(idx, cur);
        if (cur > answer) answer = cur;
    }

    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxBalancedSubsequenceSum($nums) {
        $n = count($nums);
        if ($n == 0) return 0;

        // Collect keys nums[i] - i for compression
        $keys = [];
        foreach ($nums as $i => $v) {
            $keys[] = $v - $i;
        }

        // Coordinate compression
        $sorted = $keys;
        sort($sorted, SORT_NUMERIC);
        $map = [];               // string key -> compressed index (1‑based)
        $idx = 1;
        foreach ($sorted as $val) {
            $s = (string)$val;
            if (!isset($map[$s])) {
                $map[$s] = $idx++;
            }
        }
        $size = $idx; // one past last index, safe for Fenwick size

        // Fenwick tree for prefix maximum
        $tree = array_fill(0, $size + 2, 0);

        $ans = PHP_INT_MIN;

        for ($i = 0; $i < $n; ++$i) {
            $keyVal = $nums[$i] - $i;
            $pos = $map[(string)$keyVal];

            // query max dp for keys <= current key
            $bestPrev = 0;
            $j = $pos;
            while ($j > 0) {
                if ($tree[$j] > $bestPrev) $bestPrev = $tree[$j];
                $j -= $j & (-$j);
            }

            // compute dp for current position
            $candidate = $nums[$i] + $bestPrev;
            $curr = $nums[$i] > $candidate ? $nums[$i] : $candidate;

            // update Fenwick tree at pos with curr
            $j = $pos;
            while ($j <= $size) {
                if ($curr > $tree[$j]) $tree[$j] = $curr;
                $j += $j & (-$j);
            }

            if ($curr > $ans) $ans = $curr;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxBalancedSubsequenceSum(_ nums: [Int]) -> Int {
        let n = nums.count
        var transformed = [Int64]()
        transformed.reserveCapacity(n)
        for i in 0..<n {
            transformed.append(Int64(nums[i]) - Int64(i))
        }
        
        // Coordinate compression
        let uniqueVals = Array(Set(transformed)).sorted()
        var indexMap = [Int64: Int]()
        for (i, v) in uniqueVals.enumerated() {
            indexMap[v] = i + 1   // 1‑based index for BIT
        }
        
        // Fenwick Tree for maximum prefix query
        struct BIT {
            var tree: [Int64]
            init(_ size: Int) {
                tree = Array(repeating: 0, count: size + 2)
            }
            mutating func update(_ idx: Int, _ value: Int64) {
                var i = idx
                while i < tree.count {
                    if value > tree[i] { tree[i] = value }
                    i += i & -i
                }
            }
            func query(_ idx: Int) -> Int64 {
                var res: Int64 = 0
                var i = idx
                while i > 0 {
                    if tree[i] > res { res = tree[i] }
                    i -= i & -i
                }
                return res
            }
        }
        
        var bit = BIT(uniqueVals.count)
        var answer: Int64 = Int64.min
        
        for i in 0..<n {
            let aVal = transformed[i]
            guard let idx = indexMap[aVal] else { continue }
            let bestPrev = bit.query(idx)          // max dp with transformed <= current
            let curNum = Int64(nums[i])
            var cur = curNum                       // start new subsequence
            let candidate = curNum + bestPrev      // extend previous subsequence
            if candidate > cur { cur = candidate }
            bit.update(idx, cur)
            if cur > answer { answer = cur }
        }
        
        return Int(answer)
    }
}
```

## Kotlin

```kotlin
import java.util.HashMap
import kotlin.math.max

class Solution {
    private class BIT(private val n: Int) {
        private val tree = LongArray(n + 2) { 0L }
        fun update(idx: Int, value: Long) {
            var i = idx
            while (i <= n) {
                if (value > tree[i]) tree[i] = value
                i += i and -i
            }
        }

        fun query(idx: Int): Long {
            var res = 0L
            var i = idx
            while (i > 0) {
                if (tree[i] > res) res = tree[i]
                i -= i and -i
            }
            return res
        }
    }

    fun maxBalancedSubsequenceSum(nums: IntArray): Long {
        val n = nums.size
        val keys = LongArray(n)
        for (i in 0 until n) {
            keys[i] = nums[i].toLong() - i.toLong()
        }

        // Coordinate compression
        val sorted = keys.clone()
        java.util.Arrays.sort(sorted)
        val uniq = mutableListOf<Long>()
        var prev: Long? = null
        for (v in sorted) {
            if (prev == null || v != prev) {
                uniq.add(v)
                prev = v
            }
        }
        val map = HashMap<Long, Int>(uniq.size * 2)
        for ((idx, value) in uniq.withIndex()) {
            map[value] = idx + 1 // 1‑based index for BIT
        }

        val bit = BIT(uniq.size)
        var answer = Long.MIN_VALUE

        for (i in 0 until n) {
            val key = keys[i]
            val idx = map[key]!!
            val bestPrev = bit.query(idx)
            var dp = nums[i].toLong()
            dp = max(dp, nums[i].toLong() + bestPrev)
            if (dp > answer) answer = dp
            bit.update(idx, dp)
        }

        return answer
    }
}
```

## Dart

```dart
class Fenwick {
  final List<int> _tree;
  final int _n;
  static const int _negInf = - (1 << 60);
  Fenwick(this._n) : _tree = List.filled(_n + 2, _negInf);

  void update(int idx, int value) {
    for (int i = idx; i <= _n; i += i & -i) {
      if (value > _tree[i]) _tree[i] = value;
    }
  }

  int query(int idx) {
    int res = _negInf;
    for (int i = idx; i > 0; i -= i & -i) {
      if (_tree[i] > res) res = _tree[i];
    }
    return res;
  }
}

class Solution {
  static const int _negInf = - (1 << 60);
  int maxBalancedSubsequenceSum(List<int> nums) {
    final int n = nums.length;
    List<int> vals = List.generate(n, (i) => nums[i] - i);
    List<int> sortedVals = List.from(vals)..sort();
    // deduplicate
    List<int> uniq = [];
    int? prev;
    for (int v in sortedVals) {
      if (prev == null || v != prev) {
        uniq.add(v);
        prev = v;
      }
    }
    Map<int, int> idxMap = {};
    for (int i = 0; i < uniq.length; ++i) {
      idxMap[uniq[i]] = i + 1; // 1‑based index for Fenwick
    }

    Fenwick ft = Fenwick(uniq.length);
    int answer = _negInf;

    for (int i = 0; i < n; ++i) {
      int v = nums[i] - i;
      int idx = idxMap[v]!;
      int bestPrev = ft.query(idx);
      int cur = nums[i];
      if (bestPrev != _negInf) {
        int cand = nums[i] + bestPrev;
        if (cand > cur) cur = cand;
      }
      ft.update(idx, cur);
      if (cur > answer) answer = cur;
    }

    return answer;
  }
}
```

## Golang

```go
package main

import (
	"math"
	"sort"
)

type Fenwick struct {
	tree []int64
	n    int
}

func NewFenwick(n int) *Fenwick {
	f := &Fenwick{
		tree: make([]int64, n+2),
		n:    n,
	}
	for i := range f.tree {
		f.tree[i] = math.MinInt64
	}
	return f
}

// update position idx (1‑based) with value val if val is larger
func (f *Fenwick) Update(idx int, val int64) {
	for i := idx; i <= f.n; i += i & -i {
		if val > f.tree[i] {
			f.tree[i] = val
		}
	}
}

// query maximum value in prefix [1..idx]
func (f *Fenwick) Query(idx int) int64 {
	res := math.MinInt64
	for i := idx; i > 0; i -= i & -i {
		if f.tree[i] > res {
			res = f.tree[i]
		}
	}
	return res
}

func maxBalancedSubsequenceSum(nums []int) int64 {
	n := len(nums)
	if n == 0 {
		return 0
	}
	keys := make([]int64, n)
	for i, v := range nums {
		keys[i] = int64(v) - int64(i)
	}
	// coordinate compression
	comp := append([]int64(nil), keys...)
	sort.Slice(comp, func(i, j int) bool { return comp[i] < comp[j] })
	uniq := make([]int64, 0, len(comp))
	for _, v := range comp {
		if len(uniq) == 0 || uniq[len(uniq)-1] != v {
			uniq = append(uniq, v)
		}
	}
	posMap := make(map[int64]int, len(uniq))
	for i, v := range uniq {
		posMap[v] = i + 1 // 1‑based index for Fenwick
	}

	fenwick := NewFenwick(len(uniq))
	ans := math.MinInt64

	for i, v := range nums {
		key := keys[i]
		idx := posMap[key]

		bestPrev := fenwick.Query(idx)
		cur := int64(v)
		if bestPrev != math.MinInt64 {
			if cand := cur + bestPrev; cand > cur {
				cur = cand
			}
		}
		// update structures
		fenwick.Update(idx, cur)
		if cur > ans {
			ans = cur
		}
	}
	return ans
}
```

## Ruby

```ruby
def max_balanced_subsequence_sum(nums)
  n = nums.length
  vals = Array.new(n) { |i| nums[i] - i }
  uniq_vals = vals.uniq.sort
  index_map = {}
  uniq_vals.each_with_index { |v, idx| index_map[v] = idx + 1 } # 1-based

  size = uniq_vals.size
  neg_inf = -(1 << 60)
  bit = Array.new(size + 2, neg_inf)

  update = lambda do |idx, value|
    while idx <= size
      bit[idx] = value if value > bit[idx]
      idx += idx & -idx
    end
  end

  query = lambda do |idx|
    res = neg_inf
    while idx > 0
      cur = bit[idx]
      res = cur if cur > res
      idx -= idx & -idx
    end
    res
  end

  ans = neg_inf
  n.times do |i|
    v = vals[i]
    idx = index_map[v]
    best_prev = query.call(idx)
    cur = nums[i]
    if best_prev > neg_inf / 2
      tmp = nums[i] + best_prev
      cur = tmp if tmp > cur
    end
    ans = cur if cur > ans
    update.call(idx, cur)
  end

  ans
end
```

## Scala

```scala
object Solution {
    def maxBalancedSubsequenceSum(nums: Array[Int]): Long = {
        val n = nums.length
        val transformed = new Array[Long](n)
        for (i <- 0 until n) {
            transformed(i) = nums(i).toLong - i.toLong
        }
        val uniq = transformed.distinct.sorted
        val idxMap = scala.collection.mutable.HashMap[Long, Int]()
        for ((v, i) <- uniq.zipWithIndex) {
            idxMap(v) = i + 1 // 1‑based index for BIT
        }

        class Fenwick(val size: Int) {
            private val tree = new Array[Long](size + 2)
            java.util.Arrays.fill(tree, Long.MinValue)

            def update(pos0: Int, value: Long): Unit = {
                var pos = pos0
                while (pos <= size) {
                    if (value > tree(pos)) tree(pos) = value
                    pos += pos & -pos
                }
            }

            def query(pos0: Int): Long = {
                var res = Long.MinValue
                var pos = pos0
                while (pos > 0) {
                    if (tree(pos) > res) res = tree(pos)
                    pos -= pos & -pos
                }
                res
            }
        }

        val bit = new Fenwick(uniq.length)
        var answer = Long.MinValue

        for (i <- 0 until n) {
            val pos = idxMap(transformed(i))
            var bestPrev = bit.query(pos)
            if (bestPrev == Long.MinValue) bestPrev = 0L
            val cur = nums(i).toLong
            val dp = math.max(cur, cur + bestPrev)
            answer = math.max(answer, dp)
            bit.update(pos, dp)
        }

        answer
    }
}
```

## Rust

```rust
use std::cmp::max;

const NEG_INF: i64 = i64::MIN / 4;

struct BIT {
    n: usize,
    bit: Vec<i64>,
}

impl BIT {
    fn new(size: usize) -> Self {
        BIT { n: size, bit: vec![NEG_INF; size + 2] }
    }
    fn update(&mut self, mut idx: usize, val: i64) {
        while idx <= self.n {
            if val > self.bit[idx] {
                self.bit[idx] = val;
            }
            idx += idx & (!idx + 1);
        }
    }
    fn query(&self, mut idx: usize) -> i64 {
        let mut res = NEG_INF;
        while idx > 0 {
            if self.bit[idx] > res {
                res = self.bit[idx];
            }
            idx &= idx - 1;
        }
        res
    }
}

impl Solution {
    pub fn max_balanced_subsequence_sum(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        // compute transformed values a_i = nums[i] - i
        let mut vals: Vec<i64> = (0..n)
            .map(|i| nums[i] as i64 - i as i64)
            .collect();
        vals.sort_unstable();
        vals.dedup();

        let mut bit = BIT::new(vals.len());
        let mut answer = NEG_INF;

        for i in 0..n {
            let a_i = nums[i] as i64 - i as i64;
            let idx = vals.binary_search(&a_i).unwrap() + 1; // 1-based index
            let best_prev = bit.query(idx);
            let mut cur = nums[i] as i64;
            if best_prev != NEG_INF {
                cur = max(cur, nums[i] as i64 + best_prev);
            }
            answer = max(answer, cur);
            bit.update(idx, cur);
        }

        answer
    }
}
```

## Racket

```racket
(define/contract (max-balanced-subsequence-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (arr (list->vector nums))
         (keys (for/list ([i (in-range n)]) (- (vector-ref arr i) i)))
         (sorted-keys (sort keys <))
         (uniq-keys (remove-duplicates sorted-keys))
         (m (length uniq-keys))
         (key->idx (make-hash)))
    ;; map each unique key to a 1‑based index
    (let loop ((lst uniq-keys) (pos 1))
      (unless (null? lst)
        (hash-set! key->idx (car lst) pos)
        (loop (cdr lst) (+ pos 1))))
    (define INF-NEG -1000000000000000000)
    (define bit (make-vector (+ m 2) INF-NEG))
    ;; BIT update: set position idx to max(current, val)
    (define (bit-update! idx val)
      (let loop ((i idx))
        (when (<= i (+ m 1))
          (vector-set! bit i (max (vector-ref bit i) val))
          (loop (+ i (bitwise-and i (- i)))))))
    ;; BIT query: maximum value in prefix [1..idx]
    (define (bit-query idx)
      (let loop ((i idx) (res INF-NEG))
        (if (= i 0)
            res
            (loop (bitwise-and i (- i)) (max res (vector-ref bit i))))))
    (let ((ans INF-NEG))
      (for ([i (in-range n)])
        (define key (- (vector-ref arr i) i))
        (define idx (hash-ref key->idx key))
        (define bestPrev (bit-query idx))
        (define cur (if (= bestPrev INF-NEG)
                        (vector-ref arr i)
                        (max (vector-ref arr i) (+ (vector-ref arr i) bestPrev))))
        (when (> cur ans) (set! ans cur))
        (bit-update! idx cur))
      ans)))
```

## Erlang

```erlang
-define(NEG_INF, -1000000000000000000).

-export([max_balanced_subsequence_sum/1]).
-spec max_balanced_subsequence_sum(Nums :: [integer()]) -> integer().
max_balanced_subsequence_sum(Nums) ->
    NegInf = ?NEG_INF,
    N = length(Nums),
    Indexed = lists:zip(lists:seq(0, N-1), Nums),
    Keys = [Num - Idx || {Idx, Num} <- Indexed],
    SortedKeys = lists:usort(Keys),
    PosMap = maps:from_list(lists:zip(SortedKeys, lists:seq(1, length(SortedKeys)))),
    Size = length(SortedKeys),
    Bit0 = #{},
    {Ans,_} = lists:foldl(fun({Idx, Num}, {CurMax, Bit}) ->
        Key = Num - Idx,
        Pos = maps:get(Key, PosMap),
        BestPrev = query(Pos, Bit, NegInf),
        DP = case BestPrev of
            B when B == NegInf -> Num;
            _ -> max(Num, Num + BestPrev)
        end,
        NewMax = max(CurMax, DP),
        NewBit = update(Pos, DP, Size, Bit, NegInf),
        {NewMax, NewBit}
    end, {NegInf, Bit0}, Indexed),
    Ans.

query(Idx, Bit, NegInf) ->
    query_loop(Idx, Bit, NegInf).

query_loop(0, _Bit, Max) -> Max;
query_loop(Idx, Bit, Max) ->
    Cur = maps:get(Idx, Bit, NegInf),
    NewMax = if Cur > Max -> Cur; true -> Max end,
    query_loop(Idx - (Idx band (-Idx)), Bit, NewMax).

update(Pos, Val, Size, Bit, NegInf) ->
    update_loop(Pos, Val, Size, Bit, NegInf).

update_loop(Index, Val, Size, Bit, NegInf) when Index =< Size ->
    Cur = maps:get(Index, Bit, NegInf),
    NewBit = if Val > Cur -> maps:put(Index, Val, Bit); true -> Bit end,
    update_loop(Index + (Index band (-Index)), Val, Size, NewBit, NegInf);
update_loop(_Index, _Val, _Size, Bit, _NegInf) ->
    Bit.
```

## Elixir

```elixir
defmodule BIT do
  import Bitwise, only: [&&&: 2]

  def new(size) do
    {size, :array.new(size + 2, default: 0)}
  end

  def update({size, tree} = bit, idx, val) when idx <= size do
    cur = :array.get(idx, tree)
    new_tree = if val > cur, do: :array.set(idx, val, tree), else: tree
    update({size, new_tree}, idx + (idx &&& -idx), val)
  end

  def update(bit, _idx, _val), do: bit

  def query({_size, tree}, idx) do
    query(tree, idx, 0)
  end

  defp query(_tree, 0, acc), do: acc

  defp query(tree, i, acc) do
    cur = :array.get(i, tree)
    new_acc = if cur > acc, do: cur, else: acc
    query(tree, i - (i &&& -i), new_acc)
  end
end

defmodule Solution do
  @spec max_balanced_subsequence_sum(nums :: [integer]) :: integer
  def max_balanced_subsequence_sum(nums) do
    n = length(nums)

    keys =
      Enum.map(Enum.with_index(nums), fn {v, i} -> v - i end)

    sorted_keys = keys |> Enum.uniq() |> Enum.sort()
    comp = Enum.with_index(sorted_keys, 1) |> Enum.into(%{}, fn {k, idx} -> {k, idx} end)
    bit = BIT.new(length(sorted_keys))

    {answer, _} =
      Enum.reduce(Enum.with_index(nums), {nil, bit}, fn {val, i}, {ans, cur_bit} ->
        key = val - i
        idx = comp[key]
        best_prev = BIT.query(cur_bit, idx)
        dp = max(val, val + best_prev)

        new_ans =
          case ans do
            nil -> dp
            _ -> if dp > ans, do: dp, else: ans
          end

        {new_ans, BIT.update(cur_bit, idx, dp)}
      end)

    answer
  end
end
```
