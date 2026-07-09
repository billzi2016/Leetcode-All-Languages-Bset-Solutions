# 2179. Count Good Triplets in an Array

## Cpp

```cpp
class Solution {
public:
    struct BIT {
        int n;
        vector<int> bit;
        BIT(int n): n(n), bit(n + 1, 0) {}
        void add(int idx, int val) { // idx: 0-based
            for (++idx; idx <= n; idx += idx & -idx) bit[idx] += val;
        }
        int sumPrefix(int idx) { // sum [0..idx], idx can be -1
            if (idx < 0) return 0;
            int res = 0;
            for (++idx; idx > 0; idx -= idx & -idx) res += bit[idx];
            return res;
        }
        int sumRange(int l, int r) { // inclusive, assume l<=r
            if (l > r) return 0;
            return sumPrefix(r) - (l ? sumPrefix(l - 1) : 0);
        }
    };
    
    long long goodTriplets(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size();
        vector<int> posIn2(n);
        for (int i = 0; i < n; ++i) posIn2[nums2[i]] = i;
        vector<int> a(n);
        for (int i = 0; i < n; ++i) a[i] = posIn2[nums1[i]];
        
        vector<int> leftLess(n), rightGreater(n);
        BIT bitL(n);
        for (int i = 0; i < n; ++i) {
            int v = a[i];
            leftLess[i] = bitL.sumPrefix(v - 1);
            bitL.add(v, 1);
        }
        BIT bitR(n);
        for (int i = n - 1; i >= 0; --i) {
            int v = a[i];
            rightGreater[i] = bitR.sumRange(v + 1, n - 1);
            bitR.add(v, 1);
        }
        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            ans += 1LL * leftLess[i] * rightGreater[i];
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    private static class BIT {
        private final int size;
        private final int[] tree;
        BIT(int n) {
            this.size = n;
            this.tree = new int[n + 2];
        }
        void update(int idx, int delta) {
            while (idx <= size) {
                tree[idx] += delta;
                idx += idx & -idx;
            }
        }
        int query(int idx) {
            int sum = 0;
            while (idx > 0) {
                sum += tree[idx];
                idx -= idx & -idx;
            }
            return sum;
        }
    }

    public long goodTriplets(int[] nums1, int[] nums2) {
        int n = nums1.length;
        int[] posInNums2 = new int[n];
        for (int i = 0; i < n; i++) {
            posInNums2[nums2[i]] = i;
        }
        int[] mapped = new int[n];
        for (int i = 0; i < n; i++) {
            mapped[i] = posInNums2[nums1[i]];
        }

        long[] leftLess = new long[n];
        BIT bitLeft = new BIT(n);
        for (int i = 0; i < n; i++) {
            // count of previous values with index less than mapped[i]
            leftLess[i] = bitLeft.query(mapped[i]);
            bitLeft.update(mapped[i] + 1, 1);
        }

        long[] rightGreater = new long[n];
        BIT bitRight = new BIT(n);
        for (int i = n - 1; i >= 0; i--) {
            int totalSeen = bitRight.query(n);
            int lessOrEqual = bitRight.query(mapped[i] + 1); // values <= mapped[i]
            rightGreater[i] = totalSeen - lessOrEqual;
            bitRight.update(mapped[i] + 1, 1);
        }

        long ans = 0L;
        for (int i = 0; i < n; i++) {
            ans += leftLess[i] * rightGreater[i];
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def goodTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        # position of each value in nums2
        pos2 = [0] * n
        for i, v in enumerate(nums2):
            pos2[v] = i

        a = [pos2[v] for v in nums1]

        class BIT:
            __slots__ = ("size", "tree")
            def __init__(self, size):
                self.size = size
                self.tree = [0] * (size + 1)
            def add(self, idx, delta):
                i = idx + 1
                while i <= self.size:
                    self.tree[i] += delta
                    i += i & -i
            def sum(self, idx):
                # prefix sum [0..idx], idx inclusive; if idx < 0 returns 0
                if idx < 0:
                    return 0
                i = idx + 1
                s = 0
                while i > 0:
                    s += self.tree[i]
                    i -= i & -i
                return s

        left_counts = [0] * n
        bit_left = BIT(n)
        for i in range(n):
            val = a[i]
            left_counts[i] = bit_left.sum(val - 1)  # strictly less on the left
            bit_left.add(val, 1)

        right_counts = [0] * n
        bit_right = BIT(n)
        total_seen = 0
        for i in range(n - 1, -1, -1):
            val = a[i]
            # numbers greater than val among those already seen (to the right)
            greater = total_seen - bit_right.sum(val)
            right_counts[i] = greater
            bit_right.add(val, 1)
            total_seen += 1

        ans = 0
        for i in range(n):
            ans += left_counts[i] * right_counts[i]
        return ans
```

## Python3

```python
class Solution:
    def goodTriplets(self, nums1, nums2):
        n = len(nums1)
        pos2 = [0] * n
        for i, v in enumerate(nums2):
            pos2[v] = i

        a = [pos2[v] for v in nums1]

        class Fenwick:
            __slots__ = ("n", "bit")
            def __init__(self, n):
                self.n = n
                self.bit = [0] * (n + 1)
            def add(self, idx, delta):
                while idx <= self.n:
                    self.bit[idx] += delta
                    idx += idx & -idx
            def sum(self, idx):
                s = 0
                while idx > 0:
                    s += self.bit[idx]
                    idx -= idx & -idx
                return s

        left = [0] * n
        ft = Fenwick(n)
        for i in range(n):
            idx = a[i] + 1          # 1‑based index
            left[i] = ft.sum(idx - 1)   # count of smaller positions to the left
            ft.add(idx, 1)

        ft2 = Fenwick(n)
        processed = 0
        ans = 0
        for i in range(n - 1, -1, -1):
            idx = a[i] + 1
            leq = ft2.sum(idx)          # count of positions <= current on the right
            greater = processed - leq   # positions > current on the right
            ans += left[i] * greater
            ft2.add(idx, 1)
            processed += 1

        return ans
```

## C

```c
#include <stdlib.h>

static void bit_update(int *bit, int n, int idx, int delta) {
    while (idx <= n) {
        bit[idx] += delta;
        idx += idx & -idx;
    }
}

static int bit_query(int *bit, int idx) {
    int sum = 0;
    while (idx > 0) {
        sum += bit[idx];
        idx -= idx & -idx;
    }
    return sum;
}

long long goodTriplets(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int n = nums1Size;  // same as nums2Size
    int *posInNums2 = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n; ++i) {
        posInNums2[nums2[i]] = i;
    }

    int *arrPos = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n; ++i) {
        arrPos[i] = posInNums2[nums1[i]];
    }
    free(posInNums2);

    int *left = (int *)malloc(sizeof(int) * n);
    int *bit1 = (int *)calloc(n + 2, sizeof(int));

    for (int i = 0; i < n; ++i) {
        int p = arrPos[i];               // 0‑based position in nums2
        left[i] = bit_query(bit1, p);    // count of smaller positions to the left
        bit_update(bit1, n + 1, p + 1, 1);
    }
    free(bit1);

    int *bit2 = (int *)calloc(n + 2, sizeof(int));
    long long ans = 0;

    for (int i = n - 1; i >= 0; --i) {
        int p = arrPos[i];
        int totalSeen = bit_query(bit2, n + 1);
        int leq = bit_query(bit2, p + 1);          // positions <= p on the right
        int right = totalSeen - leq;                // positions > p on the right
        ans += (long long)left[i] * right;
        bit_update(bit2, n + 1, p + 1, 1);
    }
    free(bit2);
    free(arrPos);
    free(left);

    return ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    private class BIT {
        private readonly int[] tree;
        private readonly int n;
        public BIT(int size) {
            n = size;
            tree = new int[n + 2];
        }
        public void Update(int idx, int delta) {
            while (idx <= n) {
                tree[idx] += delta;
                idx += idx & -idx;
            }
        }
        public int Query(int idx) {
            int sum = 0;
            while (idx > 0) {
                sum += tree[idx];
                idx -= idx & -idx;
            }
            return sum;
        }
    }

    public long GoodTriplets(int[] nums1, int[] nums2) {
        int n = nums1.Length;
        int[] posIn2 = new int[n];
        for (int i = 0; i < n; i++) {
            posIn2[nums2[i]] = i;
        }

        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = posIn2[nums1[i]];
        }

        long[] left = new long[n];
        BIT bitLeft = new BIT(n);
        for (int i = 0; i < n; i++) {
            // query count of values less than a[i]
            left[i] = bitLeft.Query(a[i]);
            bitLeft.Update(a[i] + 1, 1);
        }

        long[] right = new long[n];
        BIT bitRight = new BIT(n);
        int seen = 0;
        for (int i = n - 1; i >= 0; i--) {
            int lessOrEqual = bitRight.Query(a[i] + 1);
            int greater = seen - lessOrEqual;
            right[i] = greater;
            bitRight.Update(a[i] + 1, 1);
            seen++;
        }

        long result = 0;
        for (int i = 0; i < n; i++) {
            result += left[i] * right[i];
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var goodTriplets = function(nums1, nums2) {
    const n = nums1.length;
    const posIn2 = new Array(n);
    for (let i = 0; i < n; ++i) posIn2[nums2[i]] = i;

    const arr = new Array(n);
    for (let i = 0; i < n; ++i) arr[i] = posIn2[nums1[i]];

    class BIT {
        constructor(size) {
            this.n = size;
            this.tree = new Int32Array(size + 2);
        }
        update(idx, delta) {
            for (let i = idx; i <= this.n; i += i & -i) this.tree[i] += delta;
        }
        query(idx) {
            let sum = 0;
            for (let i = idx; i > 0; i -= i & -i) sum += this.tree[i];
            return sum;
        }
        range(l, r) {
            if (r < l) return 0;
            return this.query(r) - this.query(l - 1);
        }
    }

    const leftLess = new Array(n);
    const bitL = new BIT(n);
    for (let i = 0; i < n; ++i) {
        const idx = arr[i] + 1; // 1‑based
        leftLess[i] = bitL.query(idx - 1);
        bitL.update(idx, 1);
    }

    const rightGreater = new Array(n);
    const bitR = new BIT(n);
    for (let i = n - 1; i >= 0; --i) {
        const idx = arr[i] + 1;
        rightGreater[i] = bitR.range(idx + 1, n);
        bitR.update(idx, 1);
    }

    let ans = 0;
    for (let i = 0; i < n; ++i) ans += leftLess[i] * rightGreater[i];
    return ans;
};
```

## Typescript

```typescript
function goodTriplets(nums1: number[], nums2: number[]): number {
    const n = nums1.length;
    const posInNums2 = new Array<number>(n);
    for (let i = 0; i < n; i++) {
        posInNums2[nums2[i]] = i;
    }
    const arr = new Array<number>(n);
    for (let i = 0; i < n; i++) {
        arr[i] = posInNums2[nums1[i]];
    }

    class BIT {
        private readonly size: number;
        private readonly tree: number[];
        constructor(size: number) {
            this.size = size;
            this.tree = new Array<number>(size + 2).fill(0);
        }
        update(index: number, delta: number): void {
            for (let i = index; i <= this.size; i += i & -i) {
                this.tree[i] += delta;
            }
        }
        query(index: number): number {
            let sum = 0;
            for (let i = index; i > 0; i -= i & -i) {
                sum += this.tree[i];
            }
            return sum;
        }
    }

    const leftLess = new Array<number>(n);
    let bit = new BIT(n);
    for (let i = 0; i < n; i++) {
        const idx = arr[i] + 1; // shift to 1‑based
        leftLess[i] = bit.query(idx - 1); // count of smaller positions on the left
        bit.update(idx, 1);
    }

    bit = new BIT(n);
    let seen = 0;
    let ans = 0;
    for (let i = n - 1; i >= 0; i--) {
        const idx = arr[i] + 1;
        const leq = bit.query(idx); // count of positions <= current on the right
        const greater = seen - leq; // positions > current on the right
        ans += leftLess[i] * greater;
        bit.update(idx, 1);
        seen++;
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function goodTriplets($nums1, $nums2) {
        $n = count($nums1);
        // position of each value in nums2
        $posIn2 = array_fill(0, $n, 0);
        foreach ($nums2 as $i => $v) {
            $posIn2[$v] = $i;
        }

        // map nums1 order to positions in nums2
        $pos = [];
        for ($i = 0; $i < $n; $i++) {
            $pos[$i] = $posIn2[$nums1[$i]];
        }

        $size = $n + 2;               // BIT size (1-indexed)
        $bit = array_fill(0, $size, 0);
        $left = array_fill(0, $n, 0);

        // forward pass: count smaller positions on the left
        for ($i = 0; $i < $n; $i++) {
            $idx = $pos[$i] + 1;      // shift to 1-indexed

            // query sum of indices < idx
            $sum = 0;
            $j = $idx - 1;
            while ($j > 0) {
                $sum += $bit[$j];
                $j -= $j & (-$j);
            }
            $left[$i] = $sum;

            // update BIT at idx
            $j = $idx;
            while ($j < $size) {
                $bit[$j] += 1;
                $j += $j & (-$j);
            }
        }

        // reset BIT for right pass
        $bit = array_fill(0, $size, 0);
        $ans = 0;
        $processed = 0;

        // backward pass: count greater positions on the right
        for ($i = $n - 1; $i >= 0; $i--) {
            $idx = $pos[$i] + 1;

            // query sum of indices <= idx
            $sumLe = 0;
            $j = $idx;
            while ($j > 0) {
                $sumLe += $bit[$j];
                $j -= $j & (-$j);
            }

            $greater = $processed - $sumLe; // elements to the right with larger position
            $ans += $left[$i] * $greater;

            // update BIT at idx
            $j = $idx;
            while ($j < $size) {
                $bit[$j] += 1;
                $j += $j & (-$j);
            }
            $processed++;
        }

        return $ans;
    }
}
```

## Swift

```swift
class BIT {
    private var tree: [Int]
    private let size: Int

    init(_ n: Int) {
        self.size = n
        self.tree = Array(repeating: 0, count: n + 2)
    }

    func update(_ index: Int, _ delta: Int) {
        var i = index
        while i <= size {
            tree[i] += delta
            i += i & -i
        }
    }

    func query(_ index: Int) -> Int {
        if index <= 0 { return 0 }
        var i = index
        var sum = 0
        while i > 0 {
            sum += tree[i]
            i -= i & -i
        }
        return sum
    }
}

class Solution {
    func goodTriplets(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let n = nums1.count
        var posInNums2 = Array(repeating: 0, count: n)
        for (i, v) in nums2.enumerated() {
            posInNums2[v] = i
        }

        var mapped = [Int](repeating: 0, count: n)
        for i in 0..<n {
            mapped[i] = posInNums2[nums1[i]]
        }

        // left counts
        var left = [Int](repeating: 0, count: n)
        let bitLeft = BIT(n)
        for i in 0..<n {
            let idx = mapped[i] + 1          // 1‑based index for BIT
            left[i] = bitLeft.query(idx - 1) // numbers smaller to the left
            bitLeft.update(idx, 1)
        }

        // right counts
        var right = [Int](repeating: 0, count: n)
        let bitRight = BIT(n)
        var seen = 0
        for i in stride(from: n - 1, through: 0, by: -1) {
            let idx = mapped[i] + 1
            let lessOrEqual = bitRight.query(idx)
            right[i] = seen - lessOrEqual   // numbers greater to the right
            bitRight.update(idx, 1)
            seen += 1
        }

        var ans: Int64 = 0
        for i in 0..<n {
            ans += Int64(left[i]) * Int64(right[i])
        }
        return Int(ans)
    }
}
```

## Kotlin

```kotlin
class Solution {
    private class Fenwick(private val n: Int) {
        private val bit = IntArray(n + 2)
        fun add(idx0: Int, delta: Int) {
            var idx = idx0 + 1
            while (idx <= n) {
                bit[idx] += delta
                idx += idx and -idx
            }
        }
        fun sum(idx0: Int): Int {
            if (idx0 < 0) return 0
            var idx = idx0 + 1
            var res = 0
            while (idx > 0) {
                res += bit[idx]
                idx -= idx and -idx
            }
            return res
        }
    }

    fun goodTriplets(nums1: IntArray, nums2: IntArray): Long {
        val n = nums1.size
        val posIn2 = IntArray(n)
        for (i in 0 until n) {
            posIn2[nums2[i]] = i
        }
        val arr = IntArray(n)
        for (i in 0 until n) {
            arr[i] = posIn2[nums1[i]]
        }

        val left = IntArray(n)
        val bitLeft = Fenwick(n)
        for (i in 0 until n) {
            val v = arr[i]
            left[i] = if (v > 0) bitLeft.sum(v - 1) else 0
            bitLeft.add(v, 1)
        }

        val right = IntArray(n)
        val bitRight = Fenwick(n)
        var seen = 0
        for (i in n - 1 downTo 0) {
            val v = arr[i]
            val prefix = bitRight.sum(v) // count <= v on the right side
            right[i] = seen - prefix          // count > v on the right side
            bitRight.add(v, 1)
            seen++
        }

        var ans = 0L
        for (i in 0 until n) {
            ans += left[i].toLong() * right[i].toLong()
        }
        return ans
    }
}
```

## Dart

```dart
class BIT {
  final List<int> _tree;
  final int _n;

  BIT(this._n) : _tree = List.filled(_n + 2, 0);

  void update(int idx, int delta) {
    while (idx <= _n) {
      _tree[idx] += delta;
      idx += idx & -idx;
    }
  }

  int query(int idx) {
    int sum = 0;
    while (idx > 0) {
      sum += _tree[idx];
      idx -= idx & -idx;
    }
    return sum;
  }
}

class Solution {
  int goodTriplets(List<int> nums1, List<int> nums2) {
    final int n = nums1.length;
    final List<int> posInNums2 = List.filled(n, 0);
    for (int i = 0; i < n; i++) {
      posInNums2[nums2[i]] = i;
    }

    final List<int> mapping = List.filled(n, 0);
    for (int i = 0; i < n; i++) {
      mapping[i] = posInNums2[nums1[i]];
    }

    final List<int> left = List.filled(n, 0);
    final BIT bitLeft = BIT(n);
    for (int i = 0; i < n; i++) {
      final int p = mapping[i];
      left[i] = bitLeft.query(p); // count of smaller positions to the left
      bitLeft.update(p + 1, 1);
    }

    final List<int> right = List.filled(n, 0);
    final BIT bitRight = BIT(n);
    for (int i = n - 1; i >= 0; i--) {
      final int p = mapping[i];
      final int totalSeen = n - 1 - i;
      final int lessOrEq = bitRight.query(p + 1); // positions <= p on the right
      right[i] = totalSeen - lessOrEq; // positions > p on the right
      bitRight.update(p + 1, 1);
    }

    int ans = 0;
    for (int i = 0; i < n; i++) {
      ans += left[i] * right[i];
    }
    return ans;
  }
}
```

## Golang

```go
type bit struct {
	tree []int
	n    int
}

func newBit(size int) *bit {
	return &bit{
		tree: make([]int, size+2),
		n:    size + 2,
	}
}

func (b *bit) add(idx, val int) {
	for idx < b.n {
		b.tree[idx] += val
		idx += idx & -idx
	}
}

func (b *bit) sum(idx int) int {
	res := 0
	for idx > 0 {
		res += b.tree[idx]
		idx -= idx & -idx
	}
	return res
}

// nums1 and nums2 are permutations of [0, n-1]
func goodTriplets(nums1 []int, nums2 []int) int64 {
	n := len(nums1)
	pos2 := make([]int, n)
	for i, v := range nums2 {
		pos2[v] = i
	}
	a := make([]int, n)
	for i, v := range nums1 {
		a[i] = pos2[v]
	}

	left := make([]int64, n)
	b := newBit(n)
	for i := 0; i < n; i++ {
		idx := a[i] + 1 // BIT is 1-indexed
		cnt := b.sum(idx - 1)
		left[i] = int64(cnt)
		b.add(idx, 1)
	}

	rightBIT := newBit(n)
	var result int64
	seen := 0
	for i := n - 1; i >= 0; i-- {
		idx := a[i] + 1
		lessOrEq := rightBIT.sum(idx) // count <= a[i] on the right side
		greater := seen - lessOrEq
		result += left[i] * int64(greater)
		rightBIT.add(idx, 1)
		seen++
	}
	return result
}
```

## Ruby

```ruby
class BIT
  def initialize(n)
    @n = n
    @tree = Array.new(n + 2, 0)
  end

  def add(idx, delta)
    while idx <= @n
      @tree[idx] += delta
      idx += idx & -idx
    end
  end

  def sum(idx)
    res = 0
    while idx > 0
      res += @tree[idx]
      idx -= idx & -idx
    end
    res
  end
end

def good_triplets(nums1, nums2)
  n = nums1.length
  pos = Array.new(n)
  nums2.each_with_index { |v, i| pos[v] = i }
  arr = nums1.map { |v| pos[v] }

  left = Array.new(n, 0)
  bit = BIT.new(n)
  arr.each_with_index do |val, i|
    left[i] = bit.sum(val)
    bit.add(val + 1, 1)
  end

  ans = 0
  bit2 = BIT.new(n)
  (n - 1).downto(0) do |i|
    val = arr[i]
    greater = bit2.sum(n) - bit2.sum(val + 1)
    ans += left[i] * greater
    bit2.add(val + 1, 1)
  end

  ans
end
```

## Scala

```scala
object Solution {
  def goodTriplets(nums1: Array[Int], nums2: Array[Int]): Long = {
    val n = nums1.length
    // position of each value in nums2
    val pos2 = new Array[Int](n)
    var i = 0
    while (i < n) {
      pos2(nums2(i)) = i
      i += 1
    }

    // map nums1 order to positions in nums2
    val arr = new Array[Int](n)
    i = 0
    while (i < n) {
      arr(i) = pos2(nums1(i))
      i += 1
    }

    // Fenwick tree implementation
    class Fenwick(val size: Int) {
      private val tree = new Array[Int](size + 2)
      def update(idx0: Int, delta: Int): Unit = {
        var idx = idx0
        while (idx <= size) {
          tree(idx) += delta
          idx += idx & -idx
        }
      }
      def query(idx0: Int): Int = {
        var idx = idx0
        var sum = 0
        while (idx > 0) {
          sum += tree(idx)
          idx -= idx & -idx
        }
        sum
      }
    }

    // left smaller counts
    val left = new Array[Long](n)
    val bitLeft = new Fenwick(n + 2)
    i = 0
    while (i < n) {
      val v = arr(i)               // value in [0, n-1]
      val cnt = bitLeft.query(v)   // numbers < v to the left
      left(i) = cnt.toLong
      bitLeft.update(v + 1, 1)
      i += 1
    }

    // right greater counts
    val right = new Array[Long](n)
    val bitRight = new Fenwick(n + 2)
    var seen = 0
    i = n - 1
    while (i >= 0) {
      val v = arr(i)
      val leq = bitRight.query(v + 1) // numbers <= v to the right
      val greater = seen - leq
      right(i) = greater.toLong
      bitRight.update(v + 1, 1)
      seen += 1
      i -= 1
    }

    var ans: Long = 0L
    i = 0
    while (i < n) {
      ans += left(i) * right(i)
      i += 1
    }
    ans
  }
}
```

## Rust

```rust
use std::cmp::Ordering;

struct Fenwick {
    tree: Vec<i32>,
}

impl Fenwick {
    fn new(size: usize) -> Self {
        Fenwick { tree: vec![0; size + 1] }
    }

    fn add(&mut self, mut idx: usize, delta: i32) {
        // internal index is 1‑based
        idx += 1;
        let n = self.tree.len() - 1;
        while idx <= n {
            self.tree[idx] += delta;
            idx += idx & (!idx + 1);
        }
    }

    fn sum(&self, mut idx: usize) -> i32 {
        // prefix sum [0..=idx]
        idx += 1;
        let mut res = 0;
        while idx > 0 {
            res += self.tree[idx];
            idx &= idx - 1;
        }
        res
    }
}

impl Solution {
    pub fn good_triplets(nums1: Vec<i32>, nums2: Vec<i32>) -> i64 {
        let n = nums1.len();
        // position of each value in nums2
        let mut pos2 = vec![0usize; n];
        for (i, &v) in nums2.iter().enumerate() {
            pos2[v as usize] = i;
        }

        // map nums1 order to positions in nums2
        let mut a: Vec<usize> = Vec::with_capacity(n);
        for &v in nums1.iter() {
            a.push(pos2[v as usize]);
        }

        // left smaller counts
        let mut left = vec![0i64; n];
        let mut bit = Fenwick::new(n);
        for (j, &val) in a.iter().enumerate() {
            let cnt = if val == 0 { 0 } else { bit.sum(val - 1) as i64 };
            left[j] = cnt;
            bit.add(val, 1);
        }

        // right greater counts
        let mut right = vec![0i64; n];
        let mut bit2 = Fenwick::new(n);
        let mut seen: i64 = 0;
        for (j_rev, &val) in a.iter().enumerate().rev() {
            let le_cnt = bit2.sum(val) as i64; // <= val on the right side
            let greater = seen - le_cnt;
            right[j_rev] = greater;
            bit2.add(val, 1);
            seen += 1;
        }

        // total good triplets
        let mut ans: i64 = 0;
        for i in 0..n {
            ans += left[i] * right[i];
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (good-triplets nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((n (length nums1))
         (pos2 (make-vector n)))
    ;; map each value to its index in nums2
    (for ([v nums2] [i (in-range n)])
      (vector-set! pos2 v i))
    ;; positions of nums1 values according to nums2 ordering
    (define poslist (make-vector n))
    (for ([v nums1] [i (in-range n)])
      (vector-set! poslist i (vector-ref pos2 v)))
    ;; Binary Indexed Tree helpers
    (define bit (make-vector (+ n 1) 0))
    (define (bit-add! idx delta)
      (let loop ((i idx))
        (when (<= i n)
          (vector-set! bit i (+ (vector-ref bit i) delta))
          (loop (+ i (bitwise-and i (- i)))))))
    (define (bit-sum idx)
      (let loop ((i idx) (s 0))
        (if (= i 0)
            s
            (loop (- i (bitwise-and i (- i))) (+ s (vector-ref bit i))))))
    ;; left counts: numbers smaller on the left
    (define left (make-vector n 0))
    (for ([i (in-range n)])
      (let* ((p (vector-ref poslist i))
             (cnt (bit-sum p)))
        (vector-set! left i cnt)
        (bit-add! (+ p 1) 1)))
    ;; right counts: numbers larger on the right
    (define right (make-vector n 0))
    ;; reset BIT
    (for ([i (in-range (+ n 1))])
      (vector-set! bit i 0))
    (for ([i (in-range (sub1 n) -1 -1)])
      (let* ((p (vector-ref poslist i))
             (totalSeen (- n 1 i))
             (leq (bit-sum (+ p 1)))
             (cnt (- totalSeen leq)))
        (vector-set! right i cnt)
        (bit-add! (+ p 1) 1)))
    ;; accumulate answer
    (let ((ans 0))
      (for ([i (in-range n)])
        (set! ans (+ ans (* (vector-ref left i) (vector-ref right i)))))
      ans)))
```

## Erlang

```erlang
-module(solution).
-export([good_triplets/2]).

good_triplets(Nums1, Nums2) ->
    PosMap = build_pos_map(Nums2, 0, #{}),
    Mapping = [maps:get(V, PosMap) || V <- Nums1],
    N = length(Mapping),
    RightBit = lists:foldl(fun(Pos, Acc) -> bit_add(Acc, N, Pos + 1, 1) end,
                           maps:new(),
                           Mapping),
    loop(Mapping, 0, N, maps:new(), RightBit, 0).

build_pos_map([], _, Acc) ->
    Acc;
build_pos_map([V | Rest], I, Acc) ->
    build_pos_map(Rest, I + 1, maps:put(V, I, Acc)).

bit_add(Map, N, Idx, Delta) when Idx =< N ->
    NewMap = maps:update_with(Idx,
                              fun(V) -> V + Delta end,
                              Delta,
                              Map),
    bit_add(NewMap, N, Idx + (Idx band (-Idx)), Delta);
bit_add(Map, _, Idx, _) ->
    Map.

bit_sum(_Map, 0) ->
    0;
bit_sum(Map, Idx) when Idx > 0 ->
    Val = maps:get(Idx, Map, 0),
    Val + bit_sum(Map, Idx - (Idx band (-Idx))).

loop([], _, _, _, _, Acc) ->
    Acc;
loop([Pos | Rest], Index, N, LeftMap, RightMap, Acc) ->
    Idx = Pos + 1,
    RightMap2 = bit_add(RightMap, N, Idx, -1),
    LeftLess = bit_sum(LeftMap, Idx - 1),
    TotalRight = N - Index - 1,
    CountLE = bit_sum(RightMap2, Idx),
    RightGreater = TotalRight - CountLE,
    Acc2 = Acc + LeftLess * RightGreater,
    LeftMap3 = bit_add(LeftMap, N, Idx, 1),
    loop(Rest, Index + 1, N, LeftMap3, RightMap2, Acc2).
```

## Elixir

```elixir
defmodule Fenwick do
  use Bitwise

  defstruct size: 0, tree: nil

  def new(n) do
    %Fenwick{size: n, tree: :array.new(n + 2, default: 0)}
  end

  def update(%Fenwick{size: size, tree: tree} = ft, idx, delta) when idx <= size do
    new_tree = do_update(tree, idx, delta, size)
    %Fenwick{ft | tree: new_tree}
  end

  defp do_update(tree, idx, delta, size) when idx <= size do
    cur = :array.get(idx, tree)
    tree = :array.set(idx, cur + delta, tree)
    next = idx + (idx &&& -idx)
    do_update(tree, next, delta, size)
  end

  defp do_update(tree, _idx, _delta, _size), do: tree

  def query(%Fenwick{tree: tree}, idx) when idx > 0 do
    do_query(tree, idx, 0)
  end

  def query(_ft, _idx), do: 0

  defp do_query(_tree, 0, acc), do: acc

  defp do_query(tree, idx, acc) do
    cur = :array.get(idx, tree)
    next = idx - (idx &&& -idx)
    do_query(tree, next, acc + cur)
  end
end

defmodule Solution do
  @spec good_triplets(nums1 :: [integer], nums2 :: [integer]) :: integer
  def good_triplets(nums1, nums2) do
    n = length(nums1)

    pos_map =
      Enum.with_index(nums2)
      |> Enum.reduce(%{}, fn {v, i}, acc -> Map.put(acc, v, i) end)

    positions = Enum.map(nums1, &Map.get(pos_map, &1))

    # left counts
    ft_left = Fenwick.new(n)
    {rev_left, _ft_left} =
      Enum.reduce(Enum.with_index(positions), {[], ft_left}, fn {pos, _i},
                                                                {rev_acc, ft} ->
        l = Fenwick.query(ft, pos)
        new_ft = Fenwick.update(ft, pos + 1, 1)
        {[l | rev_acc], new_ft}
      end)

    left_counts = Enum.reverse(rev_left)

    # right counts
    ft_right = Fenwick.new(n)

    {rev_right, _ft_right, _} =
      Enum.reduce(Enum.reverse(positions), {[], ft_right, 0}, fn pos,
                                                                {rev_acc, ft,
                                                                 seen} ->
        leq = Fenwick.query(ft, pos)
        greater = seen - leq
        new_ft = Fenwick.update(ft, pos + 1, 1)
        {[greater | rev_acc], new_ft, seen + 1}
      end)

    right_counts = Enum.reverse(rev_right)

    # total good triplets
    Enum.zip(left_counts, right_counts)
    |> Enum.reduce(0, fn {l, r}, acc -> acc + l * r end)
  end
end
```
