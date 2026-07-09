# 2659. Make Array Empty

## Cpp

```cpp
class Solution {
public:
    struct Fenwick {
        int n;
        vector<int> bit;
        Fenwick(int n): n(n), bit(n+1, 0) {}
        void add(int idx, int delta) {
            for (++idx; idx <= n; idx += idx & -idx)
                bit[idx] += delta;
        }
        int sumPrefix(int idx) const {
            int res = 0;
            for (++idx; idx > 0; idx -= idx & -idx)
                res += bit[idx];
            return res;
        }
        int rangeSum(int l, int r) const {
            if (l > r) return 0;
            return sumPrefix(r) - (l ? sumPrefix(l-1) : 0);
        }
    };
    
    long long countOperationsToEmptyArray(vector<int>& nums) {
        int n = nums.size();
        vector<pair<int,int>> order;
        order.reserve(n);
        for (int i = 0; i < n; ++i)
            order.emplace_back(nums[i], i);
        sort(order.begin(), order.end());
        
        Fenwick ft(n);
        for (int i = 0; i < n; ++i) ft.add(i, 1);
        
        long long ans = 0;
        int cur = 0;
        for (auto &p : order) {
            int idx = p.second;
            if (cur <= idx) {
                ans += ft.rangeSum(cur, idx);
            } else {
                ans += ft.rangeSum(cur, n - 1) + ft.rangeSum(0, idx);
            }
            ft.add(idx, -1);
            cur = idx;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long countOperationsToEmptyArray(int[] nums) {
        int n = nums.length;
        Integer[] order = new Integer[n];
        for (int i = 0; i < n; i++) order[i] = i;
        java.util.Arrays.sort(order, (a, b) -> Integer.compare(nums[a], nums[b]));
        BIT bit = new BIT(n);
        for (int i = 0; i < n; i++) bit.add(i, 1);
        long ans = 0L;
        int cur = 0; // start from the first position
        for (int idx : order) {
            if (cur <= idx) {
                ans += bit.rangeSum(cur, idx);
            } else {
                ans += bit.rangeSum(cur, n - 1) + bit.rangeSum(0, idx);
            }
            bit.add(idx, -1); // remove this element
            cur = (idx + 1) % n;
        }
        return ans;
    }

    private static class BIT {
        private final int n;
        private final long[] tree;

        BIT(int size) {
            this.n = size;
            this.tree = new long[n + 1];
        }

        void add(int idx, int delta) {
            for (int i = idx + 1; i <= n; i += i & -i) {
                tree[i] += delta;
            }
        }

        private long prefixSum(int idx) {
            long res = 0;
            for (int i = idx + 1; i > 0; i -= i & -i) {
                res += tree[i];
            }
            return res;
        }

        long rangeSum(int l, int r) {
            if (l > r) return 0;
            return prefixSum(r) - (l == 0 ? 0 : prefixSum(l - 1));
        }
    }
}
```

## Python

```python
class Solution(object):
    def countOperationsToEmptyArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # Fenwick Tree for alive positions
        class Fenwick:
            __slots__ = ('n', 'bit')
            def __init__(self, n):
                self.n = n
                self.bit = [0] * (n + 1)
            def add(self, i, delta):
                i += 1
                while i <= self.n:
                    self.bit[i] += delta
                    i += i & -i
            def sum(self, i):
                if i < 0:
                    return 0
                i += 1
                s = 0
                while i > 0:
                    s += self.bit[i]
                    i -= i & -i
                return s
            # find smallest index such that prefix sum >= k (k is 1-indexed)
            def kth(self, k):
                idx = 0
                bitmask = 1 << (self.n.bit_length())
                while bitmask:
                    nxt = idx + bitmask
                    if nxt <= self.n and self.bit[nxt] < k:
                        k -= self.bit[nxt]
                        idx = nxt
                    bitmask >>= 1
                return idx  # zero‑based index

        ft = Fenwick(n)
        for i in range(n):
            ft.add(i, 1)

        order = sorted(((v, i) for i, v in enumerate(nums)), key=lambda x: x[0])
        cur = 0          # current pointer position (index in original array)
        alive = n
        ans = 0

        for _, idx in order:
            if cur <= idx:
                steps = ft.sum(idx) - ft.sum(cur - 1)
            else:
                steps = ft.sum(n - 1) - ft.sum(cur - 1) + ft.sum(idx)
            ans += steps

            # remove idx
            ft.add(idx, -1)
            alive -= 1
            if alive == 0:
                break

            # move pointer to next alive element after idx (circular)
            after = ft.sum(n - 1) - ft.sum(idx)
            if after > 0:
                # there is an alive element with rank ft.sum(idx)+1
                cur = ft.kth(ft.sum(idx) + 1)
            else:
                # wrap to first alive
                cur = ft.kth(1)

        return ans
```

## Python3

```python
from typing import List

class BIT:
    def __init__(self, n: int):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, idx: int, delta: int) -> None:
        i = idx + 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def sum(self, idx: int) -> int:
        """prefix sum [0..idx]"""
        i = idx + 1
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        n = len(nums)
        order = sorted(((v, i) for i, v in enumerate(nums)), key=lambda x: x[0])
        bit = BIT(n)
        for i in range(n):
            bit.add(i, 1)

        cur = 0
        ans = 0
        total_alive = n

        for _, idx in order:
            if idx >= cur:
                left = bit.sum(cur - 1) if cur > 0 else 0
                steps = bit.sum(idx) - left
            else:
                left = bit.sum(cur - 1) if cur > 0 else 0
                steps = (bit.sum(n - 1) - left) + bit.sum(idx)

            ans += steps
            bit.add(idx, -1)
            total_alive -= 1
            cur = (idx + 1) % n

        return ans
```

## C

```c
#include <stdlib.h>

static void bit_add(int *bit, int n, int idx, int delta) {
    for (idx++; idx <= n; idx += idx & -idx)
        bit[idx] += delta;
}

static int bit_sum(int *bit, int idx) {
    int res = 0;
    for (idx++; idx > 0; idx -= idx & -idx)
        res += bit[idx];
    return res;
}

/* find smallest index such that prefix sum >= k (k is 1‑based) */
static int bit_find_kth(int *bit, int n, int k) {
    int idx = 0;
    int mask = 1;
    while ((mask << 1) <= n) mask <<= 1;   // highest power of two ≤ n
    for (; mask > 0; mask >>= 1) {
        int next = idx + mask;
        if (next <= n && bit[next] < k) {
            idx = next;
            k -= bit[next];
        }
    }
    return idx;   // zero‑based index
}

typedef struct {
    int val;
    int idx;
} Pair;

static int cmp_pair(const void *a, const void *b) {
    const Pair *pa = (const Pair *)a;
    const Pair *pb = (const Pair *)b;
    if (pa->val < pb->val) return -1;
    if (pa->val > pb->val) return 1;
    return 0;
}

long long countOperationsToEmptyArray(int* nums, int numsSize) {
    if (numsSize == 0) return 0LL;

    Pair *arr = (Pair *)malloc(sizeof(Pair) * numsSize);
    for (int i = 0; i < numsSize; ++i) {
        arr[i].val = nums[i];
        arr[i].idx = i;
    }
    qsort(arr, numsSize, sizeof(Pair), cmp_pair);

    int n = numsSize;
    int *bit = (int *)calloc(n + 1, sizeof(int));
    for (int i = 0; i < n; ++i) bit_add(bit, n, i, 1);   // all alive

    long long total = 0;
    int cur = 0;                     // start at index 0
    int remaining = n;

    for (int i = 0; i < n; ++i) {
        int target = arr[i].idx;

        int steps;
        if (cur <= target) {
            steps = bit_sum(target) - (cur == 0 ? 0 : bit_sum(cur - 1));
        } else {
            steps = bit_sum(n - 1) - (cur == 0 ? 0 : bit_sum(cur - 1)) + bit_sum(target);
        }
        total += steps;

        /* remove target */
        bit_add(bit, n, target, -1);
        remaining--;

        if (remaining == 0) break;

        int prefix = bit_sum(target);   // alive elements up to target after removal
        if (prefix == remaining) {
            cur = bit_find_kth(bit, n, 1);
        } else {
            cur = bit_find_kth(bit, n, prefix + 1);
        }
    }

    free(arr);
    free(bit);
    return total;
}
```

## Csharp

```csharp
public class Solution
{
    public long CountOperationsToEmptyArray(int[] nums)
    {
        int n = nums.Length;
        var pairs = new (int val, int idx)[n];
        for (int i = 0; i < n; i++) pairs[i] = (nums[i], i);
        Array.Sort(pairs, (a, b) => a.val.CompareTo(b.val));

        Fenwick fenwick = new Fenwick(n);
        for (int i = 0; i < n; i++) fenwick.Add(i, 1);

        long ops = 0;
        int cur = 0;

        foreach (var p in pairs)
        {
            int idx = p.idx;
            if (cur <= idx)
            {
                ops += fenwick.Sum(idx) - fenwick.Sum(cur - 1);
            }
            else
            {
                ops += fenwick.Sum(n - 1) - fenwick.Sum(cur - 1);
                ops += fenwick.Sum(idx);
            }

            fenwick.Add(idx, -1);
            cur = idx;
        }

        return ops;
    }

    private class Fenwick
    {
        private readonly int[] bit;
        private readonly int n;

        public Fenwick(int size)
        {
            n = size;
            bit = new int[n + 1];
        }

        public void Add(int index, int delta)
        {
            for (int i = index + 1; i <= n; i += i & -i)
                bit[i] += delta;
        }

        public long Sum(int index)
        {
            if (index < 0) return 0;
            long res = 0;
            for (int i = index + 1; i > 0; i -= i & -i)
                res += bit[i];
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
var countOperationsToEmptyArray = function(nums) {
    const n = nums.length;
    // Fenwick Tree (Binary Indexed Tree)
    class BIT {
        constructor(size) {
            this.n = size;
            this.tree = new Array(size + 1).fill(0);
        }
        add(idx, delta) {
            for (let i = idx + 1; i <= this.n; i += i & -i) {
                this.tree[i] += delta;
            }
        }
        sum(idx) {
            let res = 0;
            for (let i = idx + 1; i > 0; i -= i & -i) {
                res += this.tree[i];
            }
            return res;
        }
    }

    const bit = new BIT(n);
    for (let i = 0; i < n; ++i) bit.add(i, 1);

    // pair values with original indices and sort by value
    const order = nums.map((v, i) => [v, i]);
    order.sort((a, b) => a[0] - b[0]);

    let cur = 0;
    let ans = 0;

    for (const [, idx] of order) {
        if (cur <= idx) {
            // alive elements from cur to idx inclusive
            const steps = bit.sum(idx) - (cur > 0 ? bit.sum(cur - 1) : 0);
            ans += steps;
        } else {
            // wrap around
            const steps = (bit.sum(n - 1) - (cur > 0 ? bit.sum(cur - 1) : 0)) + bit.sum(idx);
            ans += steps;
        }
        // remove current index
        bit.add(idx, -1);
        cur = (idx + 1) % n;
    }

    return ans;
};
```

## Typescript

```typescript
function countOperationsToEmptyArray(nums: number[]): number {
    const n = nums.length;
    // Pair each value with its original index
    const pairs: [number, number][] = nums.map((v, i) => [v, i]);
    pairs.sort((a, b) => a[0] - b[0]); // sort by value ascending

    class BIT {
        n: number;
        tree: number[];
        constructor(n: number) {
            this.n = n;
            this.tree = new Array(n + 1).fill(0);
        }
        add(idx: number, delta: number): void {
            for (let i = idx + 1; i <= this.n; i += i & -i) {
                this.tree[i] += delta;
            }
        }
        sum(idx: number): number {
            let res = 0;
            for (let i = idx + 1; i > 0; i -= i & -i) {
                res += this.tree[i];
            }
            return res;
        }
        total(): number {
            return this.sum(this.n - 1);
        }
    }

    const bit = new BIT(n);
    for (let i = 0; i < n; ++i) bit.add(i, 1); // all positions are initially alive

    let curPos = 0; // current pointer in the remaining array (0‑based)
    let steps = 0;
    let size = n;

    for (const [, idx] of pairs) {
        const rank = bit.sum(idx) - 1; // position of this element among alive ones (0‑based)

        if (rank >= curPos) {
            steps += rank - curPos + 1;
        } else {
            steps += (size - curPos) + rank + 1;
        }

        // remove the element
        bit.add(idx, -1);
        size--;

        if (size === 0) break;

        // update current pointer for next iteration
        if (rank === size) { // removed last element, wrap to start
            curPos = 0;
        } else {
            curPos = rank; // next element shifts into this position
        }
    }

    return steps;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countOperationsToEmptyArray($nums) {
        $n = count($nums);
        // Fenwick Tree implementation
        $tree = array_fill(0, $n + 1, 0);
        $add = function($idx, $delta) use (&$tree, $n) {
            for ($i = $idx + 1; $i <= $n; $i += $i & (-$i)) {
                $tree[$i] += $delta;
            }
        };
        $prefixSum = function($idx) use (&$tree) {
            $res = 0;
            for ($i = $idx + 1; $i > 0; $i -= $i & (-$i)) {
                $res += $tree[$i];
            }
            return $res;
        };
        $rangeSum = function($l, $r) use ($prefixSum) {
            if ($l > $r) return 0;
            $left = $l > 0 ? $prefixSum($l - 1) : 0;
            return $prefixSum($r) - $left;
        };
        // initialize all positions as present
        for ($i = 0; $i < $n; ++$i) {
            $add($i, 1);
        }
        // pair values with original indices and sort by value
        $pairs = [];
        for ($i = 0; $i < $n; ++$i) {
            $pairs[] = [$nums[$i], $i];
        }
        usort($pairs, function($a, $b) {
            return $a[0] <=> $b[0];
        });
        $cur = 0;
        $ans = 0;
        foreach ($pairs as $p) {
            $idx = $p[1];
            if ($idx >= $cur) {
                $steps = $rangeSum($cur, $idx);
            } else {
                $steps = $rangeSum($cur, $n - 1) + $rangeSum(0, $idx);
            }
            $ans += $steps;
            $add($idx, -1); // remove element
            $cur = $idx;    // next start position
        }
        return $ans;
    }
}
```

## Swift

```swift
class Fenwick {
    private var n: Int
    private var bit: [Int]
    
    init(_ size: Int) {
        self.n = size
        self.bit = Array(repeating: 0, count: size + 1)
    }
    
    func add(_ index: Int, _ delta: Int) {
        var i = index + 1
        while i <= n {
            bit[i] += delta
            i += i & -i
        }
    }
    
    // prefix sum [0...index]
    func sum(_ index: Int) -> Int {
        if index < 0 { return 0 }
        var i = index + 1
        var res = 0
        while i > 0 {
            res += bit[i]
            i -= i & -i
        }
        return res
    }
    
    // find smallest index such that prefix sum >= k (k is 1‑based)
    func findByOrder(_ k: Int) -> Int {
        var idx = 0
        var mask = 1
        while mask << 1 <= n { mask <<= 1 }
        var need = k
        var curMask = mask
        while curMask != 0 {
            let next = idx + curMask
            if next <= n && bit[next] < need {
                need -= bit[next]
                idx = next
            }
            curMask >>= 1
        }
        return idx   // zero‑based index
    }
}

class Solution {
    func countOperationsToEmptyArray(_ nums: [Int]) -> Int {
        let n = nums.count
        var pairs = [(value: Int, index: Int)]()
        for i in 0..<n {
            pairs.append((nums[i], i))
        }
        pairs.sort { $0.value < $1.value }
        
        let ft = Fenwick(n)
        for i in 0..<n {
            ft.add(i, 1)
        }
        
        var cur = 0               // current position (original index)
        var remaining = n
        var answer: Int64 = 0
        
        for p in pairs {
            let idx = p.index
            var steps: Int
            if cur <= idx {
                steps = ft.sum(idx) - (cur > 0 ? ft.sum(cur - 1) : 0)
            } else {
                steps = (ft.sum(n - 1) - (cur > 0 ? ft.sum(cur - 1) : 0)) + ft.sum(idx)
            }
            answer += Int64(steps)
            
            // rank of idx before removal
            let rankBefore = ft.sum(idx)
            ft.add(idx, -1)
            remaining -= 1
            if remaining == 0 { break }
            
            var nextRank: Int
            if rankBefore <= remaining {
                nextRank = rankBefore          // successor keeps the same order number
            } else {
                nextRank = 1                    // wrap around to first element
            }
            cur = ft.findByOrder(nextRank)
        }
        
        return Int(answer)
    }
}
```

## Kotlin

```kotlin
class Solution {
    private class Fenwick(private val n: Int) {
        private val bit = LongArray(n + 2)
        fun add(idx: Int, delta: Long) {
            var i = idx + 1
            while (i <= n) {
                bit[i] += delta
                i += i and -i
            }
        }
        private fun sum(idx: Int): Long {
            var res = 0L
            var i = idx + 1
            while (i > 0) {
                res += bit[i]
                i -= i and -i
            }
            return res
        }
        fun rangeSum(l: Int, r: Int): Long {
            if (l > r) return 0L
            val right = sum(r)
            val left = if (l > 0) sum(l - 1) else 0L
            return right - left
        }
    }

    fun countOperationsToEmptyArray(nums: IntArray): Long {
        val n = nums.size
        // pair each value with its original index and sort by value
        val order = nums.mapIndexed { idx, v -> Pair(v, idx) }.sortedBy { it.first }
        val fenwick = Fenwick(n)
        for (i in 0 until n) {
            fenwick.add(i, 1L) // all positions initially present
        }

        var cur = 0          // current starting index in the circular array
        var ans = 0L

        for ((_, idx) in order) {
            val steps = if (cur <= idx) {
                fenwick.rangeSum(cur, idx)
            } else {
                fenwick.rangeSum(cur, n - 1) + fenwick.rangeSum(0, idx)
            }
            ans += steps
            // remove the element at idx
            fenwick.add(idx, -1L)

            // next start position is right after removed index
            cur = idx
            if (fenwick.rangeSum(cur, n - 1) == 0L) {
                cur = 0
            }
        }
        return ans
    }
}
```

## Dart

```dart
class BIT {
  final List<int> _tree;
  final int n;
  BIT(this.n) : _tree = List.filled(n + 2, 0);

  void add(int idx, int delta) {
    while (idx <= n) {
      _tree[idx] += delta;
      idx += idx & -idx;
    }
  }

  int sum(int idx) {
    int res = 0;
    while (idx > 0) {
      res += _tree[idx];
      idx -= idx & -idx;
    }
    return res;
  }

  int rangeSum(int l, int r) {
    if (l > r) return 0;
    return sum(r) - sum(l - 1);
  }
}

class Solution {
  int countOperationsToEmptyArray(List<int> nums) {
    final int n = nums.length;
    // pair each value with its original index
    List<List<int>> order = [];
    for (int i = 0; i < n; ++i) {
      order.add([nums[i], i]);
    }
    order.sort((a, b) => a[0].compareTo(b[0]));

    final BIT bit = BIT(n);
    // initialize all positions as present
    for (int i = 1; i <= n; ++i) {
      bit.add(i, 1);
    }

    int cur = 0; // current position in original array (0‑based)
    int ops = 0;

    for (var pair in order) {
      final int idx = pair[1]; // target index to remove
      if (cur <= idx) {
        // move forward without wrapping
        ops += bit.rangeSum(cur + 1, idx + 1);
      } else {
        // wrap around the end of the array
        ops += bit.rangeSum(cur + 1, n);
        ops += bit.rangeSum(1, idx + 1);
      }
      // remove the element at idx
      bit.add(idx + 1, -1);
      // next starting position is the index after the removed one
      cur = idx + 1;
      if (cur >= n) cur = 0;
    }

    return ops;
  }
}
```

## Golang

```go
import "sort"

type BIT struct {
	tree []int
}

func NewBIT(n int) *BIT {
	return &BIT{make([]int, n+1)}
}
func (b *BIT) Add(idx, delta int) {
	for i := idx + 1; i < len(b.tree); i += i & -i {
		b.tree[i] += delta
	}
}
func (b *BIT) Sum(idx int) int {
	res := 0
	for i := idx + 1; i > 0; i -= i & -i {
		res += b.tree[i]
	}
	return res
}

func countOperationsToEmptyArray(nums []int) int64 {
	n := len(nums)
	type pair struct{ val, idx int }
	arr := make([]pair, n)
	for i, v := range nums {
		arr[i] = pair{v, i}
	}
	sort.Slice(arr, func(i, j int) bool { return arr[i].val < arr[j].val })

	bit := NewBIT(n)
	for i := 0; i < n; i++ {
		bit.Add(i, 1)
	}

	cur := 0
	var ans int64

	for _, p := range arr {
		target := p.idx
		leftSum := 0
		if cur > 0 {
			leftSum = bit.Sum(cur - 1)
		}
		steps := 0
		if cur <= target {
			steps = bit.Sum(target) - leftSum
		} else {
			steps = (bit.Sum(n-1) - leftSum) + bit.Sum(target)
		}
		ans += int64(steps)

		bit.Add(target, -1)
		cur = (target + 1) % n
	}

	return ans
}
```

## Ruby

```ruby
class Fenwick
  def initialize(n)
    @n = n
    @bit = Array.new(n + 2, 0)
  end

  def add(i, delta)
    i += 1
    while i <= @n
      @bit[i] += delta
      i += i & -i
    end
  end

  def sum(i)
    return 0 if i < 0
    res = 0
    i += 1
    while i > 0
      res += @bit[i]
      i -= i & -i
    end
    res
  end

  def range_sum(l, r)
    return 0 if l > r
    sum(r) - (l == 0 ? 0 : sum(l - 1))
  end
end

# @param {Integer[]} nums
# @return {Integer}
def count_operations_to_empty_array(nums)
  n = nums.length
  order = (0...n).to_a.sort_by { |i| nums[i] }

  bit = Fenwick.new(n)
  (0...n).each { |i| bit.add(i, 1) }

  cur = 0
  ops = 0

  order.each do |idx|
    if idx >= cur
      steps = bit.range_sum(cur, idx)
    else
      steps = bit.range_sum(cur, n - 1) + bit.range_sum(0, idx)
    end
    ops += steps
    bit.add(idx, -1)
    cur = idx
  end

  ops
end
```

## Scala

```scala
object Solution {
  def countOperationsToEmptyArray(nums: Array[Int]): Long = {
    val n = nums.length
    // Pair each value with its original index and sort by value (ascending)
    val sortedIdx = nums.zipWithIndex.sortBy(_._1).map(_._2)

    // Fenwick Tree (Binary Indexed Tree) for counting alive elements
    class BIT(size: Int) {
      private val tree = new Array[Long](size + 1)

      def add(idx: Int, delta: Long): Unit = {
        var i = idx + 1
        while (i <= size) {
          tree(i) += delta
          i += i & -i
        }
      }

      private def prefixSum(idx: Int): Long = {
        var res = 0L
        var i = idx + 1
        while (i > 0) {
          res += tree(i)
          i -= i & -i
        }
        res
      }

      def rangeSum(l: Int, r: Int): Long = {
        if (l > r) 0L else prefixSum(r) - (if (l > 0) prefixSum(l - 1) else 0L)
      }
    }

    val bit = new BIT(n)
    for (i <- 0 until n) bit.add(i, 1L)

    var cur = 0          // current position in the original array
    var ans = 0L

    for (idx <- sortedIdx) {
      val steps =
        if (bit.rangeSum(cur, idx) > 0) {
          // target is reachable without wrapping
          bit.rangeSum(cur, idx)
        } else {
          // need to wrap around the end of the array
          bit.rangeSum(cur, n - 1) + bit.rangeSum(0, idx)
        }
      ans += steps
      // remove the element at idx
      bit.add(idx, -1L)
      cur = idx
    }

    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn count_operations_to_empty_array(nums: Vec<i32>) -> i64 {
        struct Fenwick {
            n: usize,
            bit: Vec<i32>,
        }
        impl Fenwick {
            fn new(n: usize) -> Self {
                Fenwick { n, bit: vec![0; n + 1] }
            }
            #[inline]
            fn lowbit(x: usize) -> usize {
                x & (!x + 1)
            }
            fn add(&mut self, idx: usize, delta: i32) {
                let mut i = idx + 1;
                while i <= self.n {
                    self.bit[i] += delta;
                    i += Self::lowbit(i);
                }
            }
            fn sum(&self, idx: usize) -> i32 {
                let mut res = 0;
                let mut i = idx + 1;
                while i > 0 {
                    res += self.bit[i];
                    i -= Self::lowbit(i);
                }
                res
            }
            fn range_sum(&self, l: usize, r: usize) -> i32 {
                if l == 0 {
                    self.sum(r)
                } else {
                    self.sum(r) - self.sum(l - 1)
                }
            }
        }

        let n = nums.len();
        let mut order: Vec<(i32, usize)> = nums
            .into_iter()
            .enumerate()
            .map(|(i, v)| (v, i))
            .collect();
        order.sort_by_key(|k| k.0);

        let mut bit = Fenwick::new(n);
        for i in 0..n {
            bit.add(i, 1);
        }

        let mut cur: usize = 0;
        let mut ans: i64 = 0;

        for &(_, idx) in order.iter() {
            let steps = if cur <= idx {
                bit.range_sum(cur, idx)
            } else {
                bit.range_sum(cur, n - 1) + bit.range_sum(0, idx)
            };
            ans += steps as i64;
            bit.add(idx, -1);
            cur = idx;
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (count-operations-to-empty-array nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         ;; Binary Indexed Tree
         (make-bit (lambda (size) (make-vector (+ size 1) 0)))
         (bit (make-bit n))
         (bit-add!
          (lambda (idx delta)
            (let loop ((i (+ idx 1)))
              (when (< i (vector-length bit))
                (vector-set! bit i (+ (vector-ref bit i) delta))
                (loop (+ i (bitwise-and i (- i))))))))
         (bit-sum
          (lambda (idx)
            (let loop ((i (+ idx 1)) (acc 0))
              (if (= i 0)
                  acc
                  (loop (bitwise-and i (- i)) (+ acc (vector-ref bit i)))))))
         (range-sum
          (lambda (l r)
            (if (> l r)
                0
                (- (bit-sum r)
                   (if (> l 0) (bit-sum (- l 1)) 0)))))
         ;; initialize BIT with 1 at each position
         (_ (for ([i (in-range n)]) (bit-add! i 1)))
         ;; pair indices with values and sort by value
         (indexed (for/list ([i (in-range n)])
                    (list i (list-ref nums i))))
         (sorted (sort indexed (lambda (a b) (< (cadr a) (cadr b)))))
         (sorted-ids (map car sorted))
         ;; simulation variables
         (cur 0)
         (total 0))
    (for ([idx sorted-ids])
      (let ((steps (if (<= cur idx)
                       (range-sum cur idx)
                       (+ (range-sum cur (- n 1)) (range-sum 0 idx)))))
        (set! total (+ total steps)))
      (bit-add! idx -1)          ; remove element
      (set! cur idx))            ; next start position
    total))
```

## Erlang

```erlang
-module(solution).
-export([count_operations_to_empty_array/1]).

-spec count_operations_to_empty_array(Nums :: [integer()]) -> integer().
count_operations_to_empty_array(Nums) ->
    N = length(Nums),
    Indexed = lists:zip(Nums, lists:seq(0, N - 1)),
    Sorted = lists:keysort(1, Indexed),               % sort by value
    Bit0 = init_bit(N),
    Bit = fill_bit(Bit0, N, 1),
    process(Sorted, Bit, N, 0, 0).

%% Initialize BIT with zeros (size N+1 for 1‑based indexing)
init_bit(N) ->
    array:new(N + 1, [{default, 0}]).

%% Fill BIT with initial value `Val` at every position 1..N
fill_bit(Bit, N, Val) -> fill_bit(Bit, N, 1, Val).
fill_bit(Bit, _N, I, _Val) when I > array:size(Bit) - 1 ->
    Bit;
fill_bit(Bit, N, I, Val) ->
    NewBit = add(Bit, N, I, Val),
    fill_bit(NewBit, N, I + 1, Val).

%% Add `Delta` at position `Idx` (1‑based)
add(Bit, N, Idx, Delta) when Idx =< N ->
    Cur = array:get(Idx, Bit),
    Updated = array:set(Idx, Cur + Delta, Bit),
    Next = Idx + (Idx band -Idx),
    add(Updated, N, Next, Delta);
add(Bit, _N, _Idx, _Delta) -> Bit.

%% Prefix sum up to index `Idx` (1‑based)
prefix_sum(Bit, Idx) when Idx > 0 ->
    prefix_sum(Bit, Idx, 0);
prefix_sum(_Bit, 0, Acc) -> Acc;
prefix_sum(Bit, Idx, Acc) ->
    Cur = array:get(Idx, Bit),
    Next = Idx - (Idx band -Idx),
    prefix_sum(Bit, Next, Acc + Cur).

%% Number of alive elements in inclusive range [L,R] where L,R are 0‑based
range_count(Bit, L, R) ->
    prefix_sum(Bit, R + 1) - prefix_sum(Bit, L).

%% Find smallest index (1‑based) such that prefix sum >= K
find_kth(Bit, K, N) ->
    MaxPow = highest_one_bit(N),
    find_kth(Bit, K, 0, MaxPow).

find_kth(_Bit, _K, Idx, Step) when Step =< 0 -> Idx;
find_kth(Bit, K, Idx, Step) ->
    Next = Idx + Step,
    Size = array:size(Bit) - 1,
    case Next =< Size of
        true ->
            Val = array:get(Next, Bit),
            if Val < K ->
                    find_kth(Bit, K - Val, Next, Step bsr 1);
               true ->
                    find_kth(Bit, K, Idx, Step bsr 1)
            end;
        false ->
            find_kth(Bit, K, Idx, Step bsr 1)
    end.

%% Largest power of two <= N
highest_one_bit(N) -> highest_one_bit(N, 1).
highest_one_bit(N, Pow) when Pow * 2 =< N ->
    highest_one_bit(N, Pow * 2);
highest_one_bit(_, Pow) -> Pow.

%% Main processing loop
process([], _Bit, _N, _Cur, Acc) -> Acc;
process([{_Val, Idx} | Rest], Bit0, N, Cur, Acc) ->
    Steps = if
        Cur =< Idx ->
            range_count(Bit0, Cur, Idx);
        true ->
            range_count(Bit0, Cur, N - 1) + range_count(Bit0, 0, Idx)
    end,
    NewAcc = Acc + Steps,
    % remove current index (convert to 1‑based for BIT)
    Bit1 = add(Bit0, N, Idx + 1, -1),
    Total = prefix_sum(Bit1, N),
    case Total of
        0 -> NewAcc;
        _ ->
            R = prefix_sum(Bit1, Idx + 1),   % alive up to removed position
            NextPos =
                if R == Total ->
                        find_kth(Bit1, 1, N);
                   true ->
                        find_kth(Bit1, R + 1, N)
                end,
            process(Rest, Bit1, N, NextPos - 1, NewAcc)
    end.
```

## Elixir

```elixir
defmodule Fenwick do
  require Bitwise

  def new(n) do
    :array.new(n + 1, default: 0)
  end

  def add(tree, idx, delta) when idx > 0 do
    size = :array.size(tree) - 1
    do_add(tree, idx, delta, size)
  end

  defp do_add(tree, i, delta, size) when i <= size do
    val = :array.get(i, tree)
    tree = :array.set(i, val + delta, tree)
    next = i + (i &&& -i)
    do_add(tree, next, delta, size)
  end

  defp do_add(tree, _i, _delta, _size), do: tree

  def sum(tree, idx) when idx >= 0 do
    do_sum(tree, idx, 0)
  end

  defp do_sum(_tree, 0, acc), do: acc

  defp do_sum(tree, i, acc) do
    val = :array.get(i, tree)
    next = i - (i &&& -i)
    do_sum(tree, next, acc + val)
  end
end

defmodule Solution do
  @spec count_operations_to_empty_array(nums :: [integer]) :: integer
  def count_operations_to_empty_array(nums) do
    n = length(nums)

    indexed =
      nums
      |> Enum.with_index()
      |> Enum.map(fn {v, i} -> {v, i} end)

    sorted = Enum.sort_by(indexed, fn {v, _i} -> v end)

    # initialize Fenwick tree with 1 at each position
    tree =
      0..(n - 1)
      |> Enum.reduce(Fenwick.new(n), fn i, acc ->
        Fenwick.add(acc, i + 1, 1)
      end)

    {_, _, _, answer} =
      Enum.reduce(sorted, {tree, n, 0, 0}, fn {_val, idx}, {tr, total, cur_rank, ans} ->
        # rank of idx among alive elements (0‑based)
        rank = Fenwick.sum(tr, idx + 1) - 1

        dist =
          if rank >= cur_rank do
            rank - cur_rank
          else
            total - (cur_rank - rank)
          end

        ans2 = ans + dist + 1

        # remove the element
        tr2 = Fenwick.add(tr, idx + 1, -1)
        total2 = total - 1

        cur_rank2 =
          if total2 == 0 do
            0
          else
            rem(rank, total2)
          end

        {tr2, total2, cur_rank2, ans2}
      end)

    answer
  end
end
```
