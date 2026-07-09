# 2552. Count Increasing Quadruplets

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Fenwick {
    vector<int> bit;
    int n;
public:
    Fenwick(int n = 0) { init(n); }
    void init(int n_) {
        n = n_;
        bit.assign(n + 2, 0);
    }
    void add(int idx, int delta) {
        for (; idx <= n; idx += idx & -idx) bit[idx] += delta;
    }
    int sumPrefix(int idx) const {
        int res = 0;
        for (; idx > 0; idx -= idx & -idx) res += bit[idx];
        return res;
    }
    int rangeSum(int l, int r) const { // inclusive
        if (l > r) return 0;
        return sumPrefix(r) - sumPrefix(l - 1);
    }
};

class Solution {
public:
    long long countQuadruplets(vector<int>& nums) {
        int n = nums.size();
        Fenwick leftBIT(n);
        // initially left side contains index 0
        leftBIT.add(nums[0], 1);
        long long ans = 0;
        for (int j = 1; j <= n - 3; ++j) {
            // build right BIT with elements after j
            Fenwick rightBIT(n);
            for (int idx = j + 1; idx < n; ++idx)
                rightBIT.add(nums[idx], 1);
            // iterate k
            for (int k = j + 1; k <= n - 2; ++k) {
                rightBIT.add(nums[k], -1); // remove current k from suffix
                if (nums[k] < nums[j]) {
                    long long leftCnt = leftBIT.sumPrefix(nums[k] - 1);
                    long long rightCnt = rightBIT.rangeSum(nums[j] + 1, n);
                    ans += leftCnt * rightCnt;
                }
            }
            // add current j to left BIT for next iteration
            leftBIT.add(nums[j], 1);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long countQuadruplets(int[] nums) {
        int n = nums.length;
        long ans = 0L;
        for (int j = 1; j <= n - 3; ++j) {
            Fenwick left = new Fenwick(n);
            for (int i = 0; i < j; ++i) {
                left.add(nums[i], 1);
            }
            Fenwick right = new Fenwick(n);
            for (int l = j + 1; l < n; ++l) {
                right.add(nums[l], 1);
            }
            for (int k = j + 1; k <= n - 2; ++k) {
                // remove current k from right side so that l > k
                right.add(nums[k], -1);
                if (nums[k] < nums[j]) {
                    long leftCount = left.sum(nums[k] - 1); // values less than nums[k]
                    long rightCount = right.total() - right.sum(nums[j]); // values greater than nums[j]
                    ans += leftCount * rightCount;
                }
            }
        }
        return ans;
    }

    private static class Fenwick {
        private final int[] bit;
        private final int n;

        Fenwick(int size) {
            this.n = size;
            this.bit = new int[n + 2];
        }

        void add(int idx, int delta) {
            for (int i = idx; i <= n; i += i & -i) {
                bit[i] += delta;
            }
        }

        int sum(int idx) {
            int res = 0;
            for (int i = idx; i > 0; i -= i & -i) {
                res += bit[i];
            }
            return res;
        }

        long total() {
            return sum(n);
        }
    }
}
```

## Python

```python
class Solution(object):
    def countQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0
        # iterate over j (second position)
        for j in range(1, n - 2):
            # count of values less than nums[j] appearing before j
            cnt = [0] * (n + 1)
            for i in range(j):
                if nums[i] < nums[j]:
                    cnt[nums[i]] += 1
            # prefix sums to query how many are < a given value
            pref = [0] * (n + 2)
            for v in range(1, n + 1):
                pref[v] = pref[v - 1] + cnt[v]
            # total number of elements after j that are greater than nums[j]
            total_greater = 0
            for idx in range(j + 1, n):
                if nums[idx] > nums[j]:
                    total_greater += 1
            # iterate over k (third position)
            for k in range(j + 1, n - 1):
                if nums[k] > nums[j]:
                    total_greater -= 1  # this element can no longer be l
                if nums[k] < nums[j]:
                    left = pref[nums[k] - 1]   # i<j with nums[i] < nums[k]
                    ans += left * total_greater
        return ans
```

## Python3

```python
from typing import List

class Fenwick:
    def __init__(self, n: int):
        self.n = n
        self.bit = [0] * (n + 2)

    def add(self, idx: int, delta: int) -> None:
        while idx <= self.n:
            self.bit[idx] += delta
            idx += idx & -idx

    def sum(self, idx: int) -> int:
        s = 0
        while idx > 0:
            s += self.bit[idx]
            idx -= idx & -idx
        return s


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for j in range(1, n - 2):
            # BIT for values before j
            bit = Fenwick(n)
            for i in range(j):
                bit.add(nums[i], 1)

            # suffix[k] = number of l > k with nums[l] > nums[j]
            suffix = [0] * n
            cnt = 0
            for idx in range(n - 1, j, -1):
                if nums[idx] > nums[j]:
                    cnt += 1
                suffix[idx] = cnt

            for k in range(j + 1, n - 1):
                left = bit.sum(nums[k] - 1)   # i < j with nums[i] < nums[k]
                right = suffix[k]             # l > k with nums[l] > nums[j]
                ans += left * right
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

long long countQuadruplets(int* nums, int numsSize) {
    int n = numsSize;
    long long ans = 0;

    int *freq = (int*)calloc(n + 2, sizeof(int));
    int *pref = (int*)malloc((n + 2) * sizeof(int));

    for (int j = 1; j <= n - 3; ++j) {
        /* build frequency of values to the left of j */
        memset(freq, 0, (n + 2) * sizeof(int));
        for (int i = 0; i < j; ++i) {
            freq[nums[i]]++;
        }
        pref[0] = 0;
        for (int v = 1; v <= n; ++v) {
            pref[v] = pref[v - 1] + freq[v];
        }

        int rightGreater = (nums[n - 1] > nums[j]) ? 1 : 0;

        for (int k = n - 2; k > j; --k) {
            if (nums[k] < nums[j]) {
                int leftCnt = pref[nums[k] - 1];
                ans += (long long)leftCnt * rightGreater;
            }
            if (nums[k] > nums[j]) {
                ++rightGreater;
            }
        }
    }

    free(freq);
    free(pref);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    private class FenwickTree {
        private readonly long[] tree;
        private readonly int size;
        public FenwickTree(int n) {
            size = n;
            tree = new long[n + 2];
        }
        public void Add(int index, int delta) {
            for (int i = index; i <= size; i += i & -i)
                tree[i] += delta;
        }
        // sum of [1..index]
        public long Sum(int index) {
            long res = 0;
            for (int i = index; i > 0; i -= i & -i)
                res += tree[i];
            return res;
        }
    }

    public long CountQuadruplets(int[] nums) {
        int n = nums.Length;
        long ans = 0;
        // values are from 1..n
        for (int j = 1; j <= n - 3; ++j) {
            var leftBIT = new FenwickTree(n);
            for (int i = 0; i < j; ++i)
                leftBIT.Add(nums[i], 1);

            var rightBIT = new FenwickTree(n);
            for (int p = j + 1; p < n; ++p)
                rightBIT.Add(nums[p], 1);

            for (int k = j + 1; k <= n - 2; ++k) {
                // remove current k from right side so l > k
                rightBIT.Add(nums[k], -1);
                if (nums[k] < nums[j]) {
                    long leftLess = leftBIT.Sum(nums[k] - 1);               // i<j, nums[i] < nums[k]
                    long rightGreater = rightBIT.Sum(n) - rightBIT.Sum(nums[j]); // l>k, nums[l] > nums[j]
                    ans += leftLess * rightGreater;
                }
            }
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var countQuadruplets = function(nums) {
    const n = nums.length;
    let ans = 0;
    // j is the second index in the quadruplet (i < j < k < l)
    for (let j = 1; j <= n - 3; ++j) {
        // prefix: count of values among indices < j
        const pref = new Array(n + 1).fill(0);
        for (let i = 0; i < j; ++i) {
            pref[nums[i]] = 1;
        }
        // cumulative to allow O(1) queries of "how many values <= v"
        for (let v = 1; v <= n; ++v) {
            pref[v] += pref[v - 1];
        }
        // suffix: for each position p, number of elements after p with value > nums[j]
        const suff = new Array(n + 1).fill(0);
        for (let p = n - 1; p >= j + 1; --p) {
            suff[p] = suff[p + 1] + (nums[p] > nums[j] ? 1 : 0);
        }
        // iterate k as the third index
        for (let k = j + 1; k <= n - 2; ++k) {
            if (nums[k] >= nums[j]) continue; // need nums[k] < nums[j]
            const left = pref[nums[k] - 1];   // i < j with nums[i] < nums[k]
            const right = suff[k + 1];        // l > k with nums[l] > nums[j]
            ans += left * right;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function countQuadruplets(nums: number[]): number {
    const n = nums.length;
    let ans = 0;

    class Fenwick {
        private tree: number[];
        private size: number;
        constructor(size: number) {
            this.size = size;
            this.tree = new Array(size + 2).fill(0);
        }
        add(idx: number, delta: number): void {
            for (let i = idx; i <= this.size; i += i & -i) {
                this.tree[i] += delta;
            }
        }
        sum(idx: number): number {
            let res = 0;
            for (let i = idx; i > 0; i -= i & -i) {
                res += this.tree[i];
            }
            return res;
        }
    }

    // Iterate over middle index j
    for (let j = 1; j <= n - 3; ++j) {
        // rightGreater[k] = number of l > k with nums[l] > nums[j]
        const rightGreater: number[] = new Array(n).fill(0);
        let cnt = 0;
        for (let l = n - 1; l > j; --l) {
            if (nums[l] > nums[j]) cnt++;
            rightGreater[l] = cnt;
        }

        // Fenwick tree for values before j
        const bit = new Fenwick(n);
        for (let i = 0; i < j; ++i) {
            bit.add(nums[i], 1);
        }

        // Iterate over k
        for (let k = j + 1; k <= n - 2; ++k) {
            if (nums[k] < nums[j]) {
                const left = bit.sum(nums[k] - 1); // i < j, nums[i] < nums[k]
                const right = rightGreater[k];     // l > k, nums[l] > nums[j]
                ans += left * right;
            }
        }
    }

    return ans;
}
```

## Php

```php
class Fenwick {
    private int $size;
    private array $tree;

    public function __construct(int $n) {
        $this->size = $n + 2; // extra space
        $this->tree = array_fill(0, $this->size, 0);
    }

    public function add(int $index, int $delta): void {
        while ($index < $this->size) {
            $this->tree[$index] += $delta;
            $index += $index & (-$index);
        }
    }

    // sum of [1..index]
    public function sum(int $index): int {
        $res = 0;
        while ($index > 0) {
            $res += $this->tree[$index];
            $index -= $index & (-$index);
        }
        return $res;
    }
}

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countQuadruplets($nums) {
        $n = count($nums);
        $ans = 0;

        for ($j = 1; $j <= $n - 3; $j++) {
            // BIT for values before j
            $bit = new Fenwick($n);
            for ($i = 0; $i < $j; $i++) {
                $bit->add($nums[$i], 1);
            }

            // suffix counts of numbers greater than nums[j]
            $suffix = array_fill(0, $n, 0);
            $greaterSoFar = 0;
            for ($idx = $n - 1; $idx > $j; $idx--) {
                if ($nums[$idx] > $nums[$j]) {
                    $greaterSoFar++;
                }
                $suffix[$idx] = $greaterSoFar;
            }

            // iterate k
            for ($k = $j + 1; $k <= $n - 2; $k++) {
                if ($nums[$k] < $nums[$j]) {
                    $left = $bit->sum($nums[$k] - 1);   // i count
                    $right = $suffix[$k + 1];           // l count
                    $ans += $left * $right;
                }
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countQuadruplets(_ nums: [Int]) -> Int {
        let n = nums.count
        var answer = 0
        if n < 4 { return 0 }
        for j in 1..<(n - 2) {
            // frequency of values to the left of j
            var freq = [Int](repeating: 0, count: n + 1)
            for i in 0..<j {
                freq[nums[i]] += 1
            }
            // prefix sums of frequencies for O(1) less-than queries
            var pref = [Int](repeating: 0, count: n + 1)
            for v in 1...n {
                pref[v] = pref[v - 1] + freq[v]
            }
            // suffix counts of values greater than nums[j]
            var suffixGreater = [Int](repeating: 0, count: n)
            var cnt = 0
            for idx in stride(from: n - 1, through: j + 1, by: -1) {
                suffixGreater[idx] = cnt          // elements after idx
                if nums[idx] > nums[j] { cnt += 1 }
            }
            // evaluate each k between j and the end
            for k in (j + 1)..<(n - 1) {
                let left = pref[nums[k] - 1]      // i < j with nums[i] < nums[k]
                let right = suffixGreater[k]     // l > k with nums[l] > nums[j]
                answer += left * right
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    private class Fenwick(val size: Int) {
        val bit = IntArray(size + 2)
        fun add(idx: Int, delta: Int) {
            var i = idx
            while (i <= size) {
                bit[i] += delta
                i += i and -i
            }
        }
        fun sum(idx: Int): Int {
            var res = 0
            var i = idx
            while (i > 0) {
                res += bit[i]
                i -= i and -i
            }
            return res
        }
        fun total(): Int = sum(size)
    }

    fun countQuadruplets(nums: IntArray): Long {
        val n = nums.size
        // BIT containing all elements initially (right side for j = -1)
        val baseRight = Fenwick(n)
        for (v in nums) baseRight.add(v, 1)

        val left = Fenwick(n)
        var answer = 0L

        for (j in 0 until n) {
            // remove current j from right side so that it represents indices > j
            baseRight.add(nums[j], -1)

            // copy the current state of right BIT to use while iterating k
            val right = Fenwick(n)
            System.arraycopy(baseRight.bit, 0, right.bit, 0, baseRight.bit.size)

            var k = j + 1
            while (k < n) {
                // element at k is no longer in the >k set
                right.add(nums[k], -1)

                if (k == n - 1) break   // no l after k

                val leftLess = left.sum(nums[k] - 1)
                if (leftLess != 0) {
                    val rightGreater = right.total() - right.sum(nums[j])
                    if (rightGreater != 0) {
                        answer += leftLess.toLong() * rightGreater.toLong()
                    }
                }
                k++
            }

            // move current j element to the left side for next iteration
            left.add(nums[j], 1)
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int countQuadruplets(List<int> nums) {
    int n = nums.length;
    List<int> freq = List.filled(n + 1, 0);
    // first element is to the left of j=1
    freq[nums[0]]++;
    int ans = 0;

    for (int j = 1; j <= n - 3; ++j) {
      // cumulative counts of values on the left side (i < j)
      List<int> cum = List.filled(n + 1, 0);
      int running = 0;
      for (int v = 1; v <= n; ++v) {
        running += freq[v];
        cum[v] = running;
      }

      // rightGreater[k] = number of l > k with nums[l] > nums[j]
      List<int> rightGreater = List.filled(n, 0);
      int cnt = 0;
      for (int idx = n - 1; idx > j; --idx) {
        if (nums[idx] > nums[j]) cnt++;
        rightGreater[idx] = cnt;
      }

      // enumerate k and accumulate contributions
      for (int k = j + 1; k <= n - 2; ++k) {
        if (nums[k] < nums[j]) {
          int leftCount = cum[nums[k] - 1];   // i < j, nums[i] < nums[k]
          int rightCount = rightGreater[k]; // l > k, nums[l] > nums[j]
          ans += leftCount * rightCount;
        }
      }

      // add current j element to the left side for next iteration
      freq[nums[j]]++;
    }

    return ans;
  }
}
```

## Golang

```go
type fenwick struct {
	tree []int
}

func newFenwick(n int) *fenwick {
	return &fenwick{tree: make([]int, n+2)}
}

func (f *fenwick) add(idx, delta int) {
	for idx < len(f.tree) {
		f.tree[idx] += delta
		idx += idx & -idx
	}
}

func (f *fenwick) sum(idx int) int {
	res := 0
	for idx > 0 {
		res += f.tree[idx]
		idx -= idx & -idx
	}
	return res
}

func (f *fenwick) total() int {
	return f.sum(len(f.tree) - 1)
}

func countQuadruplets(nums []int) int64 {
	n := len(nums)
	bit := newFenwick(n)
	var ans int64

	for k := n - 2; k >= 2; k-- {
		// add element at position k+1 to the suffix structure
		bit.add(nums[k+1], 1)

		// leftPrefix[i] = number of indices <= i with nums[idx] < nums[k]
		leftCnt := 0
		leftPrefix := make([]int, k)
		for i := 0; i < k; i++ {
			if nums[i] < nums[k] {
				leftCnt++
			}
			leftPrefix[i] = leftCnt
		}

		for j := 1; j < k; j++ { // need at least one i before j
			if nums[j] > nums[k] {
				left := leftPrefix[j-1]
				right := bit.total() - bit.sum(nums[j])
				ans += int64(left) * int64(right)
			}
		}
	}
	return ans
}
```

## Ruby

```ruby
class Fenwick
  def initialize(n)
    @size = n + 2
    @tree = Array.new(@size, 0)
  end

  def add(idx, delta)
    i = idx
    while i < @size
      @tree[i] += delta
      i += i & -i
    end
  end

  # sum of [1..idx]
  def sum(idx)
    res = 0
    i = idx
    while i > 0
      res += @tree[i]
      i -= i & -i
    end
    res
  end
end

# @param {Integer[]} nums
# @return {Integer}
def count_quadruplets(nums)
  n = nums.length
  return 0 if n < 4

  bit_left = Fenwick.new(n)
  # initially include nums[0] for j = 1
  bit_left.add(nums[0], 1)

  ans = 0

  (1...n - 2).each do |j|
    # right_counts[k] = number of l > k with nums[l] > nums[j]
    right_counts = Array.new(n, 0)
    cnt = 0
    (n - 1).downto(j + 1) do |k|
      cnt += 1 if nums[k] > nums[j]
      right_counts[k] = cnt
    end

    (j + 1...n - 1).each do |k|
      next unless nums[k] < nums[j]

      left = bit_left.sum(nums[k] - 1)   # i < j and nums[i] < nums[k]
      right = right_counts[k]            # l > k and nums[l] > nums[j]
      ans += left * right
    end

    # add current nums[j] to left BIT for next iteration
    bit_left.add(nums[j], 1)
  end

  ans
end
```

## Scala

```scala
object Solution {
  def countQuadruplets(nums: Array[Int]): Long = {
    val n = nums.length
    // Fenwick Tree for counting values less than a given number among indices < j
    class Fenwick(val size: Int) {
      private val tree = new Array[Int](size + 2)
      def add(idx: Int, delta: Int): Unit = {
        var i = idx
        while (i <= size) {
          tree(i) += delta
          i += i & -i
        }
      }
      // sum of [1..idx]
      def query(idx: Int): Int = {
        var res = 0
        var i = idx
        while (i > 0) {
          res += tree(i)
          i -= i & -i
        }
        res
      }
    }

    val bit = new Fenwick(n)
    var ans = 0L

    // iterate j as the second index of the quadruplet
    var j = 1
    while (j <= n - 3) {
      // include nums(j-1) into left side counts
      bit.add(nums(j - 1), 1)

      // compute for this j: for each k > j, number of l > k with nums[l] > nums[j]
      val greaterAfter = new Array[Int](n)
      var cnt = 0
      var idx = n - 1
      while (idx > j) {
        if (nums(idx) > nums(j)) cnt += 1
        // store count for position k = idx-1
        greaterAfter(idx - 1) = cnt
        idx -= 1
      }

      // iterate over possible k
      var k = j + 1
      while (k < n - 1) {
        val leftCount = bit.query(nums(k) - 1)          // i < j and nums[i] < nums[k]
        val rightCount = greaterAfter(k)                // l > k and nums[l] > nums[j]
        ans += leftCount.toLong * rightCount.toLong
        k += 1
      }

      j += 1
    }

    ans
  }
}
```

## Rust

```rust
use std::cmp::max;

struct Fenwick {
    tree: Vec<i32>,
}

impl Fenwick {
    fn new(size: usize) -> Self {
        Fenwick { tree: vec![0; size + 2] }
    }
    fn add(&mut self, mut idx: usize, delta: i32) {
        let n = self.tree.len();
        while idx < n {
            self.tree[idx] += delta;
            idx += idx & (!idx + 1);
        }
    }
    fn sum(&self, mut idx: usize) -> i32 {
        let mut res = 0;
        while idx > 0 {
            res += self.tree[idx];
            idx &= idx - 1;
        }
        res
    }
}

impl Solution {
    pub fn count_quadruplets(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        if n < 4 {
            return 0;
        }
        // convert to usize for indexing (values are from 1..=n)
        let vals: Vec<usize> = nums.iter().map(|&x| x as usize).collect();
        let mut ans: i64 = 0;

        for j in 1..=n - 3 {
            // build BIT with elements before j
            let mut bit = Fenwick::new(n);
            for i in 0..j {
                bit.add(vals[i], 1);
            }

            // count of elements > nums[j] after position j
            let mut right_greater: i32 = 0;
            for idx in (j + 1)..n {
                if nums[idx] > nums[j] {
                    right_greater += 1;
                }
            }

            // iterate k from j+1 to n-2
            for k in (j + 1)..(n - 1) {
                if nums[k] > nums[j] {
                    right_greater -= 1; // this element can no longer be l
                }
                if nums[k] < nums[j] {
                    let left_cnt = bit.sum(vals[k] - 1);
                    ans += (left_cnt as i64) * (right_greater as i64);
                }
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (count-quadruplets nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (arr (list->vector nums)))
    (define (fenwick-add! ft idx delta)
      (let ((size (vector-length ft)))
        (let loop ((i idx))
          (when (< i size)
            (vector-set! ft i (+ (vector-ref ft i) delta))
            (loop (+ i (bitwise-and i (- i))))))))
    (define (fenwick-sum ft idx)
      (let loop ((i idx) (acc 0))
        (if (= i 0)
            acc
            (loop (bitwise-and i (- i)) (+ acc (vector-ref ft i))))))
    (let ((ans 0))
      (for ([j (in-range 1 (- n 2))]) ; j from 1 to n-3 inclusive
        (define ft (make-vector (+ n 1) 0))
        ;; add elements before j into Fenwick tree
        (for ([i (in-range 0 j)])
          (fenwick-add! ft (vector-ref arr i) 1))
        ;; count of elements to the right of j that are greater than nums[j]
        (define right-greater 0)
        (for ([l (in-range (+ j 1) n)])
          (when (> (vector-ref arr l) (vector-ref arr j))
            (set! right-greater (+ right-greater 1))))
        ;; iterate k
        (for ([k (in-range (+ j 1) (- n 1))]) ; k from j+1 to n-2 inclusive
          (when (> (vector-ref arr k) (vector-ref arr j))
            (set! right-greater (- right-greater 1)))
          (define left-count (fenwick-sum ft (- (vector-ref arr k) 1))) ; nums[i] < nums[k]
          (set! ans (+ ans (* left-count right-greater)))))
      ans)))
```

## Erlang

```erlang
-spec count_quadruplets(Nums :: [integer()]) -> integer().
count_quadruplets(Nums) ->
    N = length(Nums),
    NumTuple = list_to_tuple(Nums),
    MaxJ = N - 3,
    j_loop(1, MaxJ, NumTuple, N, 0).

j_loop(J, MaxJ, _NumTuple, _N, AccAns) when J > MaxJ ->
    AccAns;
j_loop(J, MaxJ, NumTuple, N, AccAns) ->
    %% build left frequency array for indices < J
    LeftFreq = build_counts(0, J - 1, NumTuple, array:new(N + 1, 0)),
    PrefLeft = build_prefix(LeftFreq, N),
    ValJ = element(J + 1, NumTuple),
    %% total number of elements after J that are greater than ValJ
    TotalGreaterInit = count_greater(J + 1, N - 1, NumTuple, ValJ),
    {AddAns, _} = k_loop(J + 1, N - 2, NumTuple, ValJ, PrefLeft, TotalGreaterInit, 0),
    j_loop(J + 1, MaxJ, NumTuple, N, AccAns + AddAns).

k_loop(K, MaxK, _NumTuple, _ValJ, _PrefLeft, TotalGreater, Acc) when K > MaxK ->
    {Acc, TotalGreater};
k_loop(K, MaxK, NumTuple, ValJ, PrefLeft, TotalGreater, Acc) ->
    ValK = element(K + 1, NumTuple),
    NewTotal =
        if ValK > ValJ -> TotalGreater - 1;
           true       -> TotalGreater
        end,
    Add =
        if ValK < ValJ ->
                LeftLess = 
                    case ValK of
                        1 -> 0;
                        _ -> array:get(ValK - 1, PrefLeft)
                    end,
                LeftLess * NewTotal;
           true -> 0
        end,
    k_loop(K + 1, MaxK, NumTuple, ValJ, PrefLeft, NewTotal, Acc + Add).

build_counts(I, EndI, _NumTuple, Count) when I > EndI ->
    Count;
build_counts(I, EndI, NumTuple, Count) ->
    V = element(I + 1, NumTuple),
    Cur = array:get(V, Count),
    NewCount = array:set(V, Cur + 1, Count),
    build_counts(I + 1, EndI, NumTuple, NewCount).

build_prefix(CountArray, N) ->
    build_prefix(1, N, CountArray, 0, array:new(N + 1, 0)).

build_prefix(V, N, _CountArray, Sum, Pref) when V > N ->
    Pref;
build_prefix(V, N, CountArray, Sum, Pref) ->
    C = array:get(V, CountArray),
    NewSum = Sum + C,
    NewPref = array:set(V, NewSum, Pref),
    build_prefix(V + 1, N, CountArray, NewSum, NewPref).

count_greater(I, EndI, _NumTuple, _ValJ) when I > EndI ->
    0;
count_greater(I, EndI, NumTuple, ValJ) ->
    V = element(I + 1, NumTuple),
    Rest = count_greater(I + 1, EndI, NumTuple, ValJ),
    if V > ValJ -> Rest + 1; true -> Rest end.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_quadruplets(nums :: [integer]) :: integer
  def count_quadruplets(nums) do
    nums = List.to_tuple(nums)
    n = tuple_size(nums)

    1..(n - 3)
    |> Enum.reduce(0, fn j, total ->
      # frequency of values before position j
      freq =
        0..(j - 1)
        |> Enum.reduce(:array.new(n + 1, default: 0), fn i, acc ->
          v = elem(nums, i)
          cur = :array.get(v, acc)
          :array.set(v, cur + 1, acc)
        end)

      # prefix cumulative counts: prefCum[v] = count of numbers <= v before j
      {pref_cum, _} =
        1..n
        |> Enum.reduce({:array.new(n + 1, default: 0), 0}, fn val, {arr, sum} ->
          cnt = :array.get(val, freq)
          new_sum = sum + cnt
          {:array.set(val, new_sum, arr), new_sum}
        end)

      # greaterAfter[k] = number of indices l > k with nums[l] > nums[j]
      {greater_after, _} =
        Enum.reduce(Enum.reverse((j + 1)..(n - 1)), {:array.new(n, default: 0), 0}, fn idx,
                                                                                     {arr, cnt} ->
          arr = :array.set(idx, cnt, arr)

          if elem(nums, idx) > elem(nums, j) do
            {arr, cnt + 1}
          else
            {arr, cnt}
          end
        end)

      # accumulate contributions for each k
      add =
        (j + 1)..(n - 2)
        |> Enum.reduce(0, fn k, acc ->
          vk = elem(nums, k)

          if vk < elem(nums, j) do
            left =
              if vk > 1 do
                :array.get(vk - 1, pref_cum)
              else
                0
              end

            right = :array.get(k, greater_after)
            acc + left * right
          else
            acc
          end
        end)

      total + add
    end)
  end
end
```
