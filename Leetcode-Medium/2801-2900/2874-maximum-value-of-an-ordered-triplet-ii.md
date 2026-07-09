# 2874. Maximum Value of an Ordered Triplet II

## Cpp

```cpp
class Solution {
public:
    long long maximumTripletValue(vector<int>& nums) {
        int n = nums.size();
        vector<int> suffixMax(n);
        suffixMax[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; --i) {
            suffixMax[i] = max(nums[i], suffixMax[i + 1]);
        }
        long long ans = 0;
        int leftMax = nums[0];
        for (int j = 1; j <= n - 2; ++j) {
            leftMax = max(leftMax, nums[j - 1]);
            long long cur = (long long)(leftMax - nums[j]) * suffixMax[j + 1];
            if (cur > ans) ans = cur;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long maximumTripletValue(int[] nums) {
        int n = nums.length;
        if (n < 3) return 0L;

        long[] suffixMax = new long[n];
        suffixMax[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; --i) {
            suffixMax[i] = Math.max(nums[i], suffixMax[i + 1]);
        }

        int leftMax = nums[0];
        long best = Long.MIN_VALUE;

        for (int j = 1; j <= n - 2; ++j) {
            long rightMax = suffixMax[j + 1];
            long value = ((long) leftMax - (long) nums[j]) * rightMax;
            if (value > best) {
                best = value;
            }
            leftMax = Math.max(leftMax, nums[j]);
        }

        return Math.max(best, 0L);
    }
}
```

## Python

```python
class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            return 0

        # suffix_max[i] = max of nums[i..n-1]
        suffix_max = [0] * n
        suffix_max[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], nums[i])

        left_max = nums[0]
        best = 0
        # j is the middle index
        for j in range(1, n - 1):
            right_max = suffix_max[j + 1]
            val = (left_max - nums[j]) * right_max
            if val > best:
                best = val
            if nums[j] > left_max:
                left_max = nums[j]

        return best
```

## Python3

```python
from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        imax = max(nums[0], nums[1])
        dmax = nums[0] - nums[1]
        ans = 0
        for k in range(2, n):
            val = dmax * nums[k]
            if val > ans:
                ans = val
            diff = imax - nums[k]
            if diff > dmax:
                dmax = diff
            if nums[k] > imax:
                imax = nums[k]
        return ans
```

## C

```c
#include <stdlib.h>

long long maximumTripletValue(int* nums, int numsSize) {
    if (numsSize < 3) return 0LL;
    
    int *suffixMax = (int *)malloc(numsSize * sizeof(int));
    suffixMax[numsSize - 1] = nums[numsSize - 1];
    for (int i = numsSize - 2; i >= 0; --i) {
        suffixMax[i] = nums[i] > suffixMax[i + 1] ? nums[i] : suffixMax[i + 1];
    }
    
    int leftMax = nums[0];
    long long ans = 0LL;
    
    for (int j = 1; j <= numsSize - 2; ++j) {
        int rightMax = suffixMax[j + 1];
        long long diff = (long long)leftMax - (long long)nums[j];
        long long value = diff * (long long)rightMax;
        if (value > ans) ans = value;
        
        if (nums[j] > leftMax) leftMax = nums[j];
    }
    
    free(suffixMax);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public long MaximumTripletValue(int[] nums) {
        int n = nums.Length;
        int[] prefixMax = new int[n];
        prefixMax[0] = nums[0];
        for (int i = 1; i < n; i++) {
            prefixMax[i] = Math.Max(prefixMax[i - 1], nums[i]);
        }

        int[] suffixMax = new int[n];
        suffixMax[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            suffixMax[i] = Math.Max(suffixMax[i + 1], nums[i]);
        }

        long maxVal = 0;
        for (int j = 1; j <= n - 2; j++) {
            long diff = (long)prefixMax[j - 1] - (long)nums[j];
            long candidate = diff * (long)suffixMax[j + 1];
            if (candidate > maxVal) {
                maxVal = candidate;
            }
        }

        return maxVal;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumTripletValue = function(nums) {
    const n = nums.length;
    if (n < 3) return 0;

    // suffix max: max value from i to end
    const suffixMax = new Array(n);
    suffixMax[n - 1] = nums[n - 1];
    for (let i = n - 2; i >= 0; --i) {
        suffixMax[i] = Math.max(nums[i], suffixMax[i + 1]);
    }

    let leftMax = -Infinity;
    let best = 0;

    // j is the middle index
    for (let j = 1; j <= n - 2; ++j) {
        leftMax = Math.max(leftMax, nums[j - 1]); // max in [0, j-1]
        const rightMax = suffixMax[j + 1];       // max in [j+1, n-1]
        const value = (leftMax - nums[j]) * rightMax;
        if (value > best) best = value;
    }

    return best;
};
```

## Typescript

```typescript
function maximumTripletValue(nums: number[]): number {
    const n = nums.length;
    if (n < 3) return 0;

    // suffixMax[i] = max of nums[i..n-1]
    const suffixMax = new Array<number>(n);
    suffixMax[n - 1] = nums[n - 1];
    for (let i = n - 2; i >= 0; --i) {
        suffixMax[i] = Math.max(nums[i], suffixMax[i + 1]);
    }

    let prefixMax = nums[0]; // max of nums[0..j-1]
    let best = 0;

    for (let j = 1; j <= n - 2; ++j) {
        const left = prefixMax;
        const right = suffixMax[j + 1];
        const value = (left - nums[j]) * right;
        if (value > best) best = value;

        // update prefix max for next iteration
        if (nums[j] > prefixMax) prefixMax = nums[j];
    }

    return best;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximumTripletValue($nums) {
        $n = count($nums);
        if ($n < 3) {
            return 0;
        }

        // Prefix maximums
        $prefix = array_fill(0, $n, 0);
        $curMax = $nums[0];
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] > $curMax) {
                $curMax = $nums[$i];
            }
            $prefix[$i] = $curMax;
        }

        // Suffix maximums
        $suffix = array_fill(0, $n, 0);
        $curMax = $nums[$n - 1];
        for ($i = $n - 1; $i >= 0; $i--) {
            if ($nums[$i] > $curMax) {
                $curMax = $nums[$i];
            }
            $suffix[$i] = $curMax;
        }

        $best = PHP_INT_MIN;
        for ($j = 1; $j <= $n - 2; $j++) {
            $value = ($prefix[$j - 1] - $nums[$j]) * $suffix[$j + 1];
            if ($value > $best) {
                $best = $value;
            }
        }

        return max(0, $best);
    }
}
```

## Swift

```swift
class Solution {
    func maximumTripletValue(_ nums: [Int]) -> Int {
        let n = nums.count
        if n < 3 { return 0 }
        var imax = nums[0]          // max of nums[i] for i < current j
        var dmax = Int.min          // max of (nums[i] - nums[j]) for i < j processed so far
        var answer = 0
        
        // Iterate j from 1 to n-2; after processing each j we can evaluate k = j+1
        for j in 1..<(n - 1) {
            let diffCandidate = imax - nums[j]
            if diffCandidate > dmax {
                dmax = diffCandidate
            }
            if nums[j] > imax {
                imax = nums[j]
            }
            // k is the next index after j
            let k = j + 1
            let value = dmax * nums[k]
            if value > answer {
                answer = value
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumTripletValue(nums: IntArray): Long {
        var imax = nums[0]
        var dmax = Long.MIN_VALUE
        var answer = 0L
        for (idx in 1 until nums.size) {
            if (idx >= 2 && dmax != Long.MIN_VALUE) {
                val prod = dmax * nums[idx].toLong()
                if (prod > answer) answer = prod
            }
            val diff = imax - nums[idx]
            if (diff.toLong() > dmax) dmax = diff.toLong()
            if (nums[idx] > imax) imax = nums[idx]
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int maximumTripletValue(List<int> nums) {
    int n = nums.length;
    List<int> leftMax = List.filled(n, 0);
    leftMax[0] = nums[0];
    for (int i = 1; i < n; ++i) {
      leftMax[i] = leftMax[i - 1] > nums[i] ? leftMax[i - 1] : nums[i];
    }
    List<int> rightMax = List.filled(n, 0);
    rightMax[n - 1] = nums[n - 1];
    for (int i = n - 2; i >= 0; --i) {
      rightMax[i] = rightMax[i + 1] > nums[i] ? rightMax[i + 1] : nums[i];
    }
    int ans = 0;
    for (int j = 1; j <= n - 2; ++j) {
      int diff = leftMax[j - 1] - nums[j];
      int val = diff * rightMax[j + 1];
      if (val > ans) ans = val;
    }
    return ans;
  }
}
```

## Golang

```go
func maximumTripletValue(nums []int) int64 {
	n := len(nums)
	if n < 3 {
		return 0
	}
	prefixMax := make([]int, n)
	maxVal := nums[0]
	for i := 0; i < n; i++ {
		if nums[i] > maxVal {
			maxVal = nums[i]
		}
		prefixMax[i] = maxVal
	}
	suffixMax := make([]int, n)
	maxVal = nums[n-1]
	for i := n - 1; i >= 0; i-- {
		if nums[i] > maxVal {
			maxVal = nums[i]
		}
		suffixMax[i] = maxVal
	}
	var ans int64 = 0
	for j := 1; j <= n-2; j++ {
		left := prefixMax[j-1]
		right := suffixMax[j+1]
		diff := left - nums[j]
		if diff <= 0 {
			continue
		}
		val := int64(diff) * int64(right)
		if val > ans {
			ans = val
		}
	}
	return ans
}
```

## Ruby

```ruby
def maximum_triplet_value(nums)
  n = nums.length
  imax = nums[0]
  dmax = -(1 << 60)
  ans = 0

  (1...n).each do |idx|
    if idx >= 2 && dmax > -(1 << 60)
      cand = dmax * nums[idx]
      ans = cand if cand > ans
    end

    diff = imax - nums[idx]
    dmax = diff if diff > dmax
    imax = nums[idx] if nums[idx] > imax
  end

  ans
end
```

## Scala

```scala
object Solution {
    def maximumTripletValue(nums: Array[Int]): Long = {
        val n = nums.length
        if (n < 3) return 0L

        // suffix maximums
        val suffixMax = new Array[Int](n)
        var cur = 0
        for (i <- (0 until n).reverse) {
            if (i == n - 1) cur = nums(i)
            else cur = math.max(cur, nums(i))
            suffixMax(i) = cur
        }

        var leftMax = nums(0)
        var ans: Long = 0L

        for (j <- 1 until n - 1) {
            val right = suffixMax(j + 1)
            val diff = leftMax - nums(j)
            if (diff > 0 && right > 0) {
                val value = diff.toLong * right.toLong
                if (value > ans) ans = value
            }
            leftMax = math.max(leftMax, nums(j))
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_triplet_value(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        if n < 3 {
            return 0;
        }
        // prefix maximums
        let mut left_max = vec![0i32; n];
        left_max[0] = nums[0];
        for i in 1..n {
            left_max[i] = left_max[i - 1].max(nums[i]);
        }
        // suffix maximums
        let mut right_max = vec![0i32; n];
        right_max[n - 1] = nums[n - 1];
        for i in (0..n - 1).rev() {
            right_max[i] = right_max[i + 1].max(nums[i]);
        }
        // evaluate each middle index j
        let mut ans: i64 = 0;
        for j in 1..n - 1 {
            let diff = left_max[j - 1] as i64 - nums[j] as i64;
            let prod = diff * right_max[j + 1] as i64;
            if prod > ans {
                ans = prod;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (maximum-triplet-value nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((v (list->vector nums))
         (n (vector-length v)))
    (if (< n 3)
        0
        (let ((neg-inf (- (expt 10 15)))) ; sufficiently small sentinel
          (let loop ((idx 1)
                     (imax (vector-ref v 0))
                     (best-diff neg-inf)
                     (ans 0))
            (if (= idx n)
                ans
                (let* ((val (vector-ref v idx))
                       (new-ans (if (>= idx 2)
                                    (max ans (* best-diff val))
                                    ans))
                       (diff (- imax val))
                       (new-best-diff (if (> diff best-diff) diff best-diff) )
                       (new-imax (if (> val imax) val imax)))
                  (loop (+ idx 1) new-imax new-best-diff new-ans)))))))))
```

## Erlang

```erlang
-module(solution).
-export([maximum_triplet_value/1]).

-spec maximum_triplet_value(Nums :: [integer()]) -> integer().
maximum_triplet_value(Nums) ->
    case Nums of
        [_ , _ , _ | _] = L ->
            [First|Tail] = L,
            process(Tail, First, -1000000000, 0);
        _ -> 0
    end.

process([], _Imax, _Dmax, Ans) ->
    Ans;
process([X|Rest], Imax, Dmax, Ans) ->
    NewAns = if Dmax > 0 -> max(Ans, Dmax * X); true -> Ans end,
    Diff = Imax - X,
    NewDmax = max(Dmax, Diff),
    NewImax = max(Imax, X),
    process(Rest, NewImax, NewDmax, NewAns).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_triplet_value(nums :: [integer]) :: integer
  def maximum_triplet_value(nums) do
    len = length(nums)
    if len < 3, do: 0, else: compute_max(nums, len)
  end

  defp compute_max(nums, len) do
    # Convert nums to array for O(1) access
    nums_arr = :array.from_list(nums)

    # Build suffix max array where suffix[i] = max(nums[i..end])
    suffix_list = build_suffix(nums)
    suffix_arr = :array.from_list(suffix_list)

    # Initialize prefix maximum with first element and result with 0
    prefix_max = :array.get(0, nums_arr)
    loop(1, len, prefix_max, 0, nums_arr, suffix_arr)
  end

  defp build_suffix(nums) do
    {list, _} =
      Enum.reduce(Enum.reverse(nums), {[], -1}, fn x, {acc, cur_max} ->
        new_max = if x > cur_max, do: x, else: cur_max
        {[new_max | acc], new_max}
      end)

    list
  end

  defp loop(j, len, _prefix_max, max_val, _nums_arr, _suffix_arr) when j > len - 2,
    do: max_val

  defp loop(j, len, prefix_max, max_val, nums_arr, suffix_arr) do
    cur_num = :array.get(j, nums_arr)
    right = :array.get(j + 1, suffix_arr)

    val = (prefix_max - cur_num) * right
    new_max = if val > max_val, do: val, else: max_val
    new_prefix = if cur_num > prefix_max, do: cur_num, else: prefix_max

    loop(j + 1, len, new_prefix, new_max, nums_arr, suffix_arr)
  end
end
```
