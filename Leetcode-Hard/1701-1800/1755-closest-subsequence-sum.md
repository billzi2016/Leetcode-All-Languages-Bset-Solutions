# 1755. Closest Subsequence Sum

## Cpp

```cpp
class Solution {
public:
    void gen(const vector<int>& arr, int idx, long long cur, vector<long long>& out) {
        if (idx == (int)arr.size()) {
            out.push_back(cur);
            return;
        }
        // exclude
        gen(arr, idx + 1, cur, out);
        // include
        gen(arr, idx + 1, cur + arr[idx], out);
    }

    int minAbsDifference(vector<int>& nums, int goal) {
        int n = nums.size();
        int mid = n / 2;
        vector<int> left(nums.begin(), nums.begin() + mid);
        vector<int> right(nums.begin() + mid, nums.end());

        vector<long long> leftSums;
        vector<long long> rightSums;
        gen(left, 0, 0LL, leftSums);
        gen(right, 0, 0LL, rightSums);

        sort(leftSums.begin(), leftSums.end());

        long long ans = LLONG_MAX;
        long long goalLL = goal;

        for (long long s2 : rightSums) {
            long long target = goalLL - s2;
            auto it = lower_bound(leftSums.begin(), leftSums.end(), target);
            if (it != leftSums.end()) {
                ans = min(ans, llabs((*it + s2) - goalLL));
                if (ans == 0) return 0;
            }
            if (it != leftSums.begin()) {
                --it;
                ans = min(ans, llabs((*it + s2) - goalLL));
                if (ans == 0) return 0;
            }
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int minAbsDifference(int[] nums, int goal) {
        int n = nums.length;
        int mid = n / 2;
        int[] left = java.util.Arrays.copyOfRange(nums, 0, mid);
        int[] right = java.util.Arrays.copyOfRange(nums, mid, n);

        // generate all subset sums for the left part
        int leftSize = left.length;
        int totalLeft = 1 << leftSize;
        long[] leftSums = new long[totalLeft];
        for (int mask = 0; mask < totalLeft; ++mask) {
            long sum = 0;
            for (int i = 0; i < leftSize; ++i) {
                if ((mask & (1 << i)) != 0) {
                    sum += left[i];
                }
            }
            leftSums[mask] = sum;
        }
        java.util.Arrays.sort(leftSums);

        // iterate over all subset sums of the right part and binary search in leftSums
        int rightSize = right.length;
        int totalRight = 1 << rightSize;
        long minDiff = Long.MAX_VALUE;

        for (int mask = 0; mask < totalRight; ++mask) {
            long sumR = 0;
            for (int i = 0; i < rightSize; ++i) {
                if ((mask & (1 << i)) != 0) {
                    sumR += right[i];
                }
            }
            long target = (long) goal - sumR;
            int idx = java.util.Arrays.binarySearch(leftSums, target);
            if (idx >= 0) {
                return 0; // exact match found
            } else {
                int insertPos = -idx - 1;
                if (insertPos < leftSums.length) {
                    long diff = Math.abs(leftSums[insertPos] + sumR - goal);
                    if (diff < minDiff) minDiff = diff;
                }
                if (insertPos > 0) {
                    long diff = Math.abs(leftSums[insertPos - 1] + sumR - goal);
                    if (diff < minDiff) minDiff = diff;
                }
            }
        }

        return (int) minDiff;
    }
}
```

## Python

```python
import bisect

class Solution(object):
    def minAbsDifference(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        n = len(nums)
        mid = n // 2
        left = nums[:mid]
        right = nums[mid:]

        # generate all subset sums for a list
        def subset_sums(arr):
            sums = [0]
            for x in arr:
                # add current element to existing sums
                sums += [s + x for s in sums]
            return sums

        left_sums = subset_sums(left)
        right_sums = subset_sums(right)

        left_sums.sort()
        ans = float('inf')

        for rs in right_sums:
            target = goal - rs
            idx = bisect.bisect_left(left_sums, target)

            if idx < len(left_sums):
                diff = abs(left_sums[idx] + rs - goal)
                if diff < ans:
                    ans = diff
                    if ans == 0:
                        return 0
            if idx > 0:
                diff = abs(left_sums[idx-1] + rs - goal)
                if diff < ans:
                    ans = diff
                    if ans == 0:
                        return 0

        return int(ans)
```

## Python3

```python
from typing import List
import bisect

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        mid = n // 2
        left, right = nums[:mid], nums[mid:]

        def gen(arr):
            sums = [0]
            for x in arr:
                cur_len = len(sums)
                for i in range(cur_len):
                    sums.append(sums[i] + x)
            return sums

        left_sums = gen(left)
        right_sums = gen(right)
        left_sums.sort()

        ans = float('inf')
        for rs in right_sums:
            target = goal - rs
            idx = bisect.bisect_left(left_sums, target)

            if idx < len(left_sums):
                ans = min(ans, abs(left_sums[idx] + rs - goal))
                if ans == 0:
                    return 0
            if idx > 0:
                l = left_sums[idx - 1]
                ans = min(ans, abs(l + rs - goal))
                if ans == 0:
                    return 0

        return ans
```

## C

```c
#include <stdlib.h>
#include <limits.h>

static int cmp_ll(const void *a, const void *b) {
    long long la = *(const long long *)a;
    long long lb = *(const long long *)b;
    if (la < lb) return -1;
    if (la > lb) return 1;
    return 0;
}

int minAbsDifference(int* nums, int numsSize, int goal) {
    int n = numsSize;
    int n1 = n / 2;
    int n2 = n - n1;

    int size1 = 1 << n1;                     // subsets of first half
    long long *leftSums = (long long *)malloc(sizeof(long long) * size1);
    for (int mask = 0; mask < size1; ++mask) {
        long long sum = 0;
        for (int i = 0; i < n1; ++i)
            if (mask & (1 << i))
                sum += nums[i];
        leftSums[mask] = sum;
    }

    qsort(leftSums, size1, sizeof(long long), cmp_ll);

    long long best = LLONG_MAX;

    int size2 = 1 << n2;                     // subsets of second half
    for (int mask = 0; mask < size2; ++mask) {
        long long sumR = 0;
        for (int i = 0; i < n2; ++i)
            if (mask & (1 << i))
                sumR += nums[n1 + i];

        long long target = (long long)goal - sumR;

        // lower_bound in leftSums
        int l = 0, r = size1;
        while (l < r) {
            int m = l + ((r - l) >> 1);
            if (leftSums[m] < target)
                l = m + 1;
            else
                r = m;
        }

        if (l < size1) {
            long long total = sumR + leftSums[l];
            long long diff = llabs(total - goal);
            if (diff < best) best = diff;
        }
        if (l > 0) {
            long long total = sumR + leftSums[l - 1];
            long long diff = llabs(total - goal);
            if (diff < best) best = diff;
        }

        if (best == 0) break; // optimal possible
    }

    free(leftSums);
    return (int)best;
}
```

## Csharp

```csharp
public class Solution {
    public int MinAbsDifference(int[] nums, int goal) {
        int n = nums.Length;
        int mid = n / 2;
        int leftLen = mid;
        int rightLen = n - mid;

        int leftCount = 1 << leftLen;
        long[] leftSums = new long[leftCount];
        for (int mask = 0; mask < leftCount; ++mask) {
            long sum = 0;
            for (int i = 0; i < leftLen; ++i) {
                if ((mask >> i & 1) == 1) sum += nums[i];
            }
            leftSums[mask] = sum;
        }

        Array.Sort(leftSums);

        long ans = long.MaxValue;
        int rightCount = 1 << rightLen;
        for (int mask = 0; mask < rightCount; ++mask) {
            long sumR = 0;
            for (int i = 0; i < rightLen; ++i) {
                if ((mask >> i & 1) == 1) sumR += nums[mid + i];
            }

            long target = goal - sumR;
            int idx = Array.BinarySearch(leftSums, target);
            if (idx >= 0) {
                return 0; // exact match
            } else {
                int insert = ~idx;
                if (insert < leftSums.Length) {
                    long diff = Math.Abs((sumR + leftSums[insert]) - goal);
                    if (diff < ans) ans = diff;
                }
                if (insert > 0) {
                    long diff = Math.Abs((sumR + leftSums[insert - 1]) - goal);
                    if (diff < ans) ans = diff;
                }
            }
        }

        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} goal
 * @return {number}
 */
var minAbsDifference = function(nums, goal) {
    const n = nums.length;
    const mid = Math.floor(n / 2);
    const left = nums.slice(0, mid);
    const right = nums.slice(mid);

    // generate all subset sums for an array (size <= 20)
    const genSums = arr => {
        const m = arr.length;
        const total = 1 << m; // safe because m <= 20
        const res = new Array(total);
        for (let mask = 0; mask < total; ++mask) {
            let sum = 0;
            for (let i = 0; i < m; ++i) {
                if (mask & (1 << i)) sum += arr[i];
            }
            res[mask] = sum;
        }
        return res;
    };

    const sumsLeft = genSums(left);
    sumsLeft.sort((a, b) => a - b);

    let best = Infinity;

    const totalRight = 1 << right.length;
    for (let mask = 0; mask < totalRight; ++mask) {
        let sumR = 0;
        for (let i = 0; i < right.length; ++i) {
            if (mask & (1 << i)) sumR += right[i];
        }

        const target = goal - sumR;

        // binary search lower bound in sumsLeft
        let lo = 0, hi = sumsLeft.length - 1;
        while (lo <= hi) {
            const midIdx = (lo + hi) >> 1;
            if (sumsLeft[midIdx] < target) lo = midIdx + 1;
            else hi = midIdx - 1;
        }

        // check candidate at lo
        if (lo < sumsLeft.length) {
            const totalSum = sumR + sumsLeft[lo];
            const diff = Math.abs(totalSum - goal);
            if (diff < best) best = diff;
            if (best === 0) return 0;
        }
        // check candidate at hi
        if (hi >= 0) {
            const totalSum = sumR + sumsLeft[hi];
            const diff = Math.abs(totalSum - goal);
            if (diff < best) best = diff;
            if (best === 0) return 0;
        }
    }

    return best;
};
```

## Typescript

```typescript
function minAbsDifference(nums: number[], goal: number): number {
    const n = nums.length;
    const mid = Math.floor(n / 2);
    const left = nums.slice(0, mid);
    const right = nums.slice(mid);

    const getSums = (arr: number[]): number[] => {
        const sums: number[] = [0];
        for (const v of arr) {
            const curLen = sums.length;
            for (let i = 0; i < curLen; ++i) {
                sums.push(sums[i] + v);
            }
        }
        return sums;
    };

    const leftSums = getSums(left);
    leftSums.sort((a, b) => a - b);
    const rightSums = getSums(right);

    let ans = Number.MAX_SAFE_INTEGER;

    for (const rs of rightSums) {
        const need = goal - rs;
        let l = 0, h = leftSums.length;
        while (l < h) {
            const m = (l + h) >> 1;
            if (leftSums[m] < need) {
                l = m + 1;
            } else {
                h = m;
            }
        }
        if (l < leftSums.length) {
            const total = leftSums[l] + rs;
            const diff = Math.abs(total - goal);
            if (diff < ans) ans = diff;
        }
        if (l > 0) {
            const total = leftSums[l - 1] + rs;
            const diff = Math.abs(total - goal);
            if (diff < ans) ans = diff;
        }
        if (ans === 0) return 0;
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $goal
     * @return Integer
     */
    function minAbsDifference($nums, $goal) {
        $n = count($nums);
        $mid = intdiv($n, 2);
        $left = array_slice($nums, 0, $mid);
        $right = array_slice($nums, $mid);

        // generate all subset sums for a given half
        $genSums = function($arr) {
            $len = count($arr);
            $total = 1 << $len;
            $sums = [];
            for ($mask = 0; $mask < $total; $mask++) {
                $sum = 0;
                for ($i = 0; $i < $len; $i++) {
                    if ($mask & (1 << $i)) {
                        $sum += $arr[$i];
                    }
                }
                $sums[] = $sum;
            }
            return $sums;
        };

        $leftSums = $genSums($left);
        sort($leftSums, SORT_NUMERIC);
        $rightSums = $genSums($right);

        $ans = PHP_INT_MAX;
        $lsCount = count($leftSums);

        foreach ($rightSums as $sumR) {
            $target = $goal - $sumR;

            // lower bound binary search in leftSums
            $lo = 0;
            $hi = $lsCount;
            while ($lo < $hi) {
                $midIdx = intdiv($lo + $hi, 2);
                if ($leftSums[$midIdx] < $target) {
                    $lo = $midIdx + 1;
                } else {
                    $hi = $midIdx;
                }
            }

            // check candidate at lo
            if ($lo < $lsCount) {
                $candidate = $leftSums[$lo] + $sumR;
                $diff = abs($candidate - $goal);
                if ($diff < $ans) $ans = $diff;
            }
            // check previous element
            if ($lo > 0) {
                $candidate = $leftSums[$lo - 1] + $sumR;
                $diff = abs($candidate - $goal);
                if ($diff < $ans) $ans = $diff;
            }

            if ($ans === 0) {
                return 0;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minAbsDifference(_ nums: [Int], _ goal: Int) -> Int {
        let n = nums.count
        let mid = n / 2
        let left = Array(nums[0..<mid])
        let right = Array(nums[mid..<n])

        var leftSums = getSums(left)
        leftSums.sort()
        let rightSums = getSums(right)

        var best = Int.max

        for s in rightSums {
            let target = goal - s
            let idx = lowerBound(leftSums, target)

            if idx < leftSums.count {
                let diff = abs(leftSums[idx] + s - goal)
                if diff < best { best = diff }
                if best == 0 { return 0 }
            }
            if idx > 0 {
                let diff = abs(leftSums[idx - 1] + s - goal)
                if diff < best { best = diff }
                if best == 0 { return 0 }
            }
        }

        return best
    }

    private func getSums(_ arr: [Int]) -> [Int] {
        let m = arr.count
        let total = 1 << m
        var sums = [Int]()
        sums.reserveCapacity(total)
        for mask in 0..<total {
            var sum = 0
            var i = 0
            var bits = mask
            while i < m {
                if (bits & 1) == 1 {
                    sum += arr[i]
                }
                i += 1
                bits >>= 1
            }
            sums.append(sum)
        }
        return sums
    }

    private func lowerBound(_ arr: [Int], _ target: Int) -> Int {
        var l = 0
        var r = arr.count
        while l < r {
            let mid = (l + r) >> 1
            if arr[mid] < target {
                l = mid + 1
            } else {
                r = mid
            }
        }
        return l
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minAbsDifference(nums: IntArray, goal: Int): Int {
        val n = nums.size
        val mid = n / 2

        // Generate all subset sums for left part
        val leftSums = generateSums(nums, 0, mid)
        java.util.Arrays.sort(leftSums)

        var answer = Long.MAX_VALUE
        val rightSize = n - mid
        val totalRight = 1 shl rightSize

        for (mask in 0 until totalRight) {
            var sumR = 0L
            var i = 0
            while (i < rightSize) {
                if ((mask shr i) and 1 == 1) {
                    sumR += nums[mid + i].toLong()
                }
                i++
            }

            val target = goal.toLong() - sumR
            var idx = java.util.Arrays.binarySearch(leftSums, target)
            if (idx >= 0) {
                // Exact match found, answer is zero
                return 0
            } else {
                idx = -idx - 1
                if (idx < leftSums.size) {
                    val diff = kotlin.math.abs(leftSums[idx] + sumR - goal.toLong())
                    if (diff < answer) answer = diff
                }
                if (idx > 0) {
                    val diff = kotlin.math.abs(leftSums[idx - 1] + sumR - goal.toLong())
                    if (diff < answer) answer = diff
                }
            }

            // Early exit if we already reached zero
            if (answer == 0L) return 0
        }

        return answer.toInt()
    }

    private fun generateSums(nums: IntArray, start: Int, end: Int): LongArray {
        val size = end - start
        val total = 1 shl size
        val res = LongArray(total)
        for (mask in 0 until total) {
            var sum = 0L
            var i = 0
            while (i < size) {
                if ((mask shr i) and 1 == 1) {
                    sum += nums[start + i].toLong()
                }
                i++
            }
            res[mask] = sum
        }
        return res
    }
}
```

## Dart

```dart
class Solution {
  int minAbsDifference(List<int> nums, int goal) {
    int n = nums.length;
    int mid = n ~/ 2;
    List<int> left = nums.sublist(0, mid);
    List<int> right = nums.sublist(mid);

    List<int> leftSums = _subsetSums(left);
    leftSums.sort();
    List<int> rightSums = _subsetSums(right);

    int ans = goal.abs(); // using empty subsequence (sum=0)

    for (int sR in rightSums) {
      int target = goal - sR;
      int idx = _lowerBound(leftSums, target);
      if (idx < leftSums.length) {
        int diff = (leftSums[idx] + sR - goal).abs();
        if (diff < ans) ans = diff;
        if (ans == 0) return 0;
      }
      if (idx > 0) {
        int diff = (leftSums[idx - 1] + sR - goal).abs();
        if (diff < ans) ans = diff;
        if (ans == 0) return 0;
      }
    }

    return ans;
  }

  List<int> _subsetSums(List<int> arr) {
    int m = arr.length;
    int total = 1 << m;
    List<int> sums = List.filled(total, 0);
    for (int mask = 0; mask < total; ++mask) {
      int sum = 0;
      for (int i = 0; i < m; ++i) {
        if ((mask >> i) & 1 == 1) sum += arr[i];
      }
      sums[mask] = sum;
    }
    return sums;
  }

  int _lowerBound(List<int> arr, int target) {
    int lo = 0, hi = arr.length;
    while (lo < hi) {
      int mid = (lo + hi) >> 1;
      if (arr[mid] < target) {
        lo = mid + 1;
      } else {
        hi = mid;
      }
    }
    return lo;
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

func minAbsDifference(nums []int, goal int) int {
	n := len(nums)
	mid := n / 2
	leftArr := nums[:mid]
	rightArr := nums[mid:]

	leftSums := genSumsInt64(leftArr)
	sort.Slice(leftSums, func(i, j int) bool { return leftSums[i] < leftSums[j] })

	goal64 := int64(goal)
	ans := int64(math.MaxInt64)

	m := len(rightArr)
	sizeR := 1 << m
	for mask := 0; mask < sizeR; mask++ {
		var sumR int64 = 0
		for i := 0; i < m; i++ {
			if (mask>>i)&1 == 1 {
				sumR += int64(rightArr[i])
			}
		}
		target := goal64 - sumR

		idx := sort.Search(len(leftSums), func(i int) bool { return leftSums[i] >= target })
		if idx < len(leftSums) {
			diff := absInt64(sumR + leftSums[idx] - goal64)
			if diff < ans {
				ans = diff
				if ans == 0 {
					return 0
				}
			}
		}
		if idx > 0 {
			diff := absInt64(sumR + leftSums[idx-1] - goal64)
			if diff < ans {
				ans = diff
				if ans == 0 {
					return 0
				}
			}
		}
	}

	return int(ans)
}

func genSumsInt64(arr []int) []int64 {
	n := len(arr)
	size := 1 << n
	sums := make([]int64, size)
	for mask := 0; mask < size; mask++ {
		var sum int64 = 0
		for i := 0; i < n; i++ {
			if (mask>>i)&1 == 1 {
				sum += int64(arr[i])
			}
		}
		sums[mask] = sum
	}
	return sums
}

func absInt64(a int64) int64 {
	if a < 0 {
		return -a
	}
	return a
}
```

## Ruby

```ruby
def min_abs_difference(nums, goal)
  n = nums.length
  mid = n / 2
  left = nums[0...mid]
  right = nums[mid..-1] || []

  sums_left = []
  lsize = left.size
  (0...(1 << lsize)).each do |mask|
    sum = 0
    i = 0
    while i < lsize
      sum += left[i] if (mask & (1 << i)) != 0
      i += 1
    end
    sums_left << sum
  end

  sums_left.sort!
  ans = goal.abs

  rsize = right.size
  (0...(1 << rsize)).each do |mask|
    sum_r = 0
    i = 0
    while i < rsize
      sum_r += right[i] if (mask & (1 << i)) != 0
      i += 1
    end

    target = goal - sum_r
    idx = sums_left.bsearch_index { |x| x >= target } || sums_left.size

    if idx < sums_left.size
      diff = (sums_left[idx] + sum_r - goal).abs
      ans = diff if diff < ans
    end
    if idx > 0
      diff = (sums_left[idx - 1] + sum_r - goal).abs
      ans = diff if diff < ans
    end

    return 0 if ans == 0
  end

  ans
end
```

## Scala

```scala
object Solution {
    def minAbsDifference(nums: Array[Int], goal: Int): Int = {
        val n = nums.length
        val mid = n / 2
        val left = nums.slice(0, mid)
        val right = nums.slice(mid, n)

        def subsetSums(arr: Array[Int]): Array[Long] = {
            val m = 1 << arr.length
            val res = new Array[Long](m)
            var mask = 0
            while (mask < m) {
                var sum: Long = 0L
                var i = 0
                while (i < arr.length) {
                    if ((mask >> i & 1) == 1) sum += arr(i).toLong
                    i += 1
                }
                res(mask) = sum
                mask += 1
            }
            res
        }

        val leftSums = subsetSums(left).sorted
        val rightSums = subsetSums(right)

        var ans: Long = Long.MaxValue

        import scala.collection.Searching._

        for (b <- rightSums) {
            val target = goal.toLong - b
            leftSums.search(target) match {
                case Found(_) =>
                    return 0
                case InsertionPoint(ip) =>
                    if (ip < leftSums.length) {
                        val diff = math.abs(leftSums(ip) + b - goal)
                        if (diff < ans) ans = diff
                    }
                    if (ip > 0) {
                        val diff = math.abs(leftSums(ip - 1) + b - goal)
                        if (diff < ans) ans = diff
                    }
            }
        }

        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_abs_difference(nums: Vec<i32>, goal: i32) -> i32 {
        let n = nums.len();
        let mid = n / 2;
        let left = &nums[..mid];
        let right = &nums[mid..];

        fn gen_sums(slice: &[i32]) -> Vec<i64> {
            let m = slice.len();
            let total = 1usize << m;
            let mut res = Vec::with_capacity(total);
            for mask in 0..total {
                let mut sum: i64 = 0;
                for i in 0..m {
                    if (mask >> i) & 1 == 1 {
                        sum += slice[i] as i64;
                    }
                }
                res.push(sum);
            }
            res
        }

        let mut left_sums = gen_sums(left);
        left_sums.sort_unstable();

        let right_sums = gen_sums(right);

        let goal_i64 = goal as i64;
        let mut best: i64 = goal_i64.abs(); // empty subsequence

        for &r in &right_sums {
            let target = goal_i64 - r;
            match left_sums.binary_search(&target) {
                Ok(_) => return 0,
                Err(idx) => {
                    if idx < left_sums.len() {
                        let diff = (left_sums[idx] + r - goal_i64).abs();
                        if diff < best { best = diff; }
                    }
                    if idx > 0 {
                        let diff = (left_sums[idx - 1] + r - goal_i64).abs();
                        if diff < best { best = diff; }
                    }
                }
            }
        }

        best as i32
    }
}
```

## Racket

```racket
(require racket/list)

(define/contract (min-abs-difference nums goal)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n   (length nums))
         (mid (quotient n 2))
         (left  (take nums mid))
         (right (drop nums mid)))

    ;; all subset sums of a list
    (define (subset-sums lst)
      (let loop ((rest lst) (sums (list 0)))
        (if (null? rest)
            sums
            (let* ((x   (car rest))
                   (new (map (lambda (s) (+ s x)) sums)))
              (loop (cdr rest) (append sums new))))))

    (define sums1 (subset-sums left))
    (define sums2 (subset-sums right))

    ;; sorted vector of first half sums
    (define sorted1 (list->vector (sort sums1 <)))
    (define n1 (vector-length sorted1))

    (define initial-best (abs (- goal 0))) ; empty subsequence

    (let loop ((best initial-best) (rest sums2))
      (if (null? rest)
          best
          (let* ((s2     (car rest))
                 (target (- goal s2)))

            ;; binary search for closest value to target in sorted1
            (define (search lo hi cur-best)
              (if (> lo hi)
                  cur-best
                  (let* ((mid   (quotient (+ lo hi) 2))
                         (val   (vector-ref sorted1 mid))
                         (total (+ val s2))
                         (diff  (abs (- total goal))))
                    (cond
                      [(= diff 0) 0]
                      [(< diff cur-best)
                       (if (< val target)
                           (search (+ mid 1) hi diff)
                           (search lo (- mid 1) diff))]
                      [else
                       (if (< val target)
                           (search (+ mid 1) hi cur-best)
                           (search lo (- mid 1) cur-best))]))))

            (let ((new-best (search 0 (- n1 1) best)))
              (loop new-best (cdr rest))))))))
```

## Erlang

```erlang
-spec min_abs_difference(Nums :: [integer()], Goal :: integer()) -> integer().
min_abs_difference(Nums, Goal) ->
    Len = length(Nums),
    Half = Len div 2,
    {Left, Right} = lists:split(Half, Nums),

    LeftSums = gen_sums(Left),
    RightSums = gen_sums(Right),

    SortedLeft = lists:sort(LeftSums),
    TupleLeft = list_to_tuple(SortedLeft),

    InitialMin = erlang:abs(Goal), % empty subsequence sum 0
    fold_right_sums(RightSums, Goal, TupleLeft, InitialMin).

%% generate all subset sums for a list (size <= 20)
gen_sums(List) ->
    Len = length(List),
    MaxMask = 1 bsl Len,
    gen_sums(0, MaxMask, List, []).

gen_sums(Mask, MaxMask, List, Acc) when Mask < MaxMask ->
    Sum = sum_mask(Mask, List, 0),
    gen_sums(Mask + 1, MaxMask, List, [Sum | Acc]);
gen_sums(_Mask, _MaxMask, _List, Acc) -> Acc.

sum_mask(0, _List, _Shift) -> 0;
sum_mask(_Mask, [], _Shift) -> 0;
sum_mask(Mask, [H|T], Shift) ->
    Rest = sum_mask(Mask bsr 1, T, Shift + 1),
    case (Mask band 1) of
        1 -> H + Rest;
        _ -> Rest
    end.

%% iterate over right sums and keep minimal difference
fold_right_sums([], _Goal, _TupleLeft, Min) -> Min;
fold_right_sums([RSum|Rest], Goal, TupleLeft, Min) ->
    Target = Goal - RSum,
    {Diff,_} = search_best(Target, TupleLeft),
    NewMin = if Diff < Min -> Diff; true -> Min end,
    case NewMin of
        0 -> 0;
        _ -> fold_right_sums(Rest, Goal, TupleLeft, NewMin)
    end.

%% binary search for closest value to Target in sorted tuple
search_best(Target, Tuple) ->
    Size = tuple_size(Tuple),
    search(Target, Tuple, 0, Size - 1, 10000000000, undefined).

search(_Target, _Tuple, Low, High, BestDiff, BestSum) when Low > High -> {BestDiff, BestSum};
search(Target, Tuple, Low, High, BestDiff, BestSum) ->
    Mid = (Low + High) div 2,
    MidVal = element(Mid + 1, Tuple),
    CurrDiff = erlang:abs(MidVal - Target),
    {NewBestDiff, NewBestSum} =
        if CurrDiff < BestDiff -> {CurrDiff, MidVal};
           true -> {BestDiff, BestSum}
        end,
    case MidVal of
        _ when MidVal < Target ->
            search(Target, Tuple, Mid + 1, High, NewBestDiff, NewBestSum);
        _ when MidVal > Target ->
            search(Target, Tuple, Low, Mid - 1, NewBestDiff, NewBestSum);
        _ -> % equal
            {0, MidVal}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_abs_difference(nums :: [integer], goal :: integer) :: integer
  def min_abs_difference(nums, goal) do
    import Bitwise

    n = length(nums)
    mid = div(n, 2)

    left = Enum.slice(nums, 0, mid)
    right = Enum.slice(nums, mid, n - mid)

    left_sums = gen_sums(left) |> Enum.sort()
    left_tuple = List.to_tuple(left_sums)
    len_left = tuple_size(left_tuple)

    right_sums = gen_sums(right)

    initial_best = :erlang.abs(goal) + 1_000_000_000

    Enum.reduce(right_sums, initial_best, fn rsum, best ->
      target = goal - rsum
      idx = lower_bound(left_tuple, len_left, target)

      cand1 =
        if idx < len_left do
          :erlang.abs(elem(left_tuple, idx) + rsum - goal)
        else
          best
        end

      cand2 =
        if idx > 0 do
          :erlang.abs(elem(left_tuple, idx - 1) + rsum - goal)
        else
          best
        end

      min(best, min(cand1, cand2))
    end)
  end

  defp gen_sums(arr) do
    import Bitwise
    len = length(arr)
    max_mask = (1 <<< len) - 1

    Enum.map(0..max_mask, fn mask ->
      compute_sum(arr, mask)
    end)
  end

  defp compute_sum(arr, mask) do
    import Bitwise

    {sum, _} =
      Enum.reduce(Enum.with_index(arr), {0, 0}, fn {val, i}, {acc, _} ->
        if (mask &&& (1 <<< i)) != 0 do
          {acc + val, 0}
        else
          {acc, 0}
        end
      end)

    sum
  end

  defp lower_bound(tuple, len, target) do
    lb(0, len, tuple, target)
  end

  defp lb(low, high, _tuple, _target) when low >= high, do: low

  defp lb(low, high, tuple, target) do
    mid = div(low + high, 2)
    val = elem(tuple, mid)

    if val < target do
      lb(mid + 1, high, tuple, target)
    else
      lb(low, mid, tuple, target)
    end
  end
end
```
