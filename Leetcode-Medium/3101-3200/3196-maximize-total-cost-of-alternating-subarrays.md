# 3196. Maximize Total Cost of Alternating Subarrays

## Cpp

```cpp
class Solution {
public:
    long long maximumTotalCost(vector<int>& nums) {
        int n = nums.size();
        long long notFlip = nums[0];
        const long long NEG_INF = LLONG_MIN / 4;
        long long flip = NEG_INF;
        for (int i = 1; i < n; ++i) {
            long long newNotFlip = max(notFlip, flip) + (long long)nums[i];
            long long newFlip = notFlip - (long long)nums[i];
            notFlip = newNotFlip;
            flip = newFlip;
        }
        return max(notFlip, flip);
    }
};
```

## Java

```java
class Solution {
    public long maximumTotalCost(int[] nums) {
        int n = nums.length;
        long dp0 = nums[0];                     // last element taken positively
        long dp1 = Long.MIN_VALUE / 4;          // impossible state (last element negative)
        for (int i = 1; i < n; i++) {
            long ndp0 = Math.max(dp0, dp1) + nums[i];
            long ndp1 = dp0 - nums[i];
            dp0 = ndp0;
            dp1 = ndp1;
        }
        return Math.max(dp0, dp1);
    }
}
```

## Python

```python
class Solution(object):
    def maximumTotalCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        INF_NEG = -10**18
        pos = nums[0]          # dp[i][0]: i-th element taken as positive
        neg = INF_NEG          # dp[i][1]: i-th element taken as negative (cannot for first)
        for x in nums[1:]:
            new_pos = max(pos, neg) + x
            new_neg = pos - x
            pos, neg = new_pos, new_neg
        return max(pos, neg)
```

## Python3

```python
from typing import List

class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        n = len(nums)
        # dp0: max sum up to i with i not flipped (positive sign)
        # dp1: max sum up to i with i flipped (negative sign), impossible for first element
        dp0 = nums[0]
        dp1 = float('-inf')
        for i in range(1, n):
            ndp0 = max(dp0, dp1) + nums[i]
            ndp1 = dp0 - nums[i]  # can only flip if previous not flipped
            dp0, dp1 = ndp0, ndp1
        return int(max(dp0, dp1))
```

## C

```c
#include <limits.h>

long long maximumTotalCost(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    long long notFlip = (long long)nums[0];
    long long flip = LLONG_MIN / 4;  // sufficiently small sentinel
    
    for (int i = 1; i < numsSize; ++i) {
        long long curNot = (notFlip > flip ? notFlip : flip) + (long long)nums[i];
        long long curFlip = notFlip - (long long)nums[i];
        notFlip = curNot;
        flip = curFlip;
    }
    
    return notFlip > flip ? notFlip : flip;
}
```

## Csharp

```csharp
public class Solution {
    public long MaximumTotalCost(int[] nums) {
        int n = nums.Length;
        long prevPos = nums[0];
        const long NEG_INF = long.MinValue / 4;
        long prevNeg = NEG_INF;

        for (int i = 1; i < n; i++) {
            long val = nums[i];
            long curPos = Math.Max(prevPos, prevNeg) + val;
            long curNeg = prevPos - val;
            prevPos = curPos;
            prevNeg = curNeg;
        }

        return Math.Max(prevPos, prevNeg);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumTotalCost = function(nums) {
    const n = nums.length;
    if (n === 0) return 0;
    let dpNoFlip = nums[0];                 // dp[i][0]
    let dpFlip = Number.NEGATIVE_INFINITY; // dp[i][1], impossible for i=0
    for (let i = 1; i < n; ++i) {
        const val = nums[i];
        const newNoFlip = Math.max(dpNoFlip, dpFlip) + val;
        const newFlip = dpNoFlip - val; // can only come from previous not flipped
        dpNoFlip = newNoFlip;
        dpFlip = newFlip;
    }
    return Math.max(dpNoFlip, dpFlip);
};
```

## Typescript

```typescript
function maximumTotalCost(nums: number[]): number {
    const n = nums.length;
    if (n === 0) return 0;
    // First element cannot be flipped
    let prev0 = nums[0];
    let prev1 = Number.NEGATIVE_INFINITY; // impossible state
    
    for (let i = 1; i < n; i++) {
        const cur0 = Math.max(prev0, prev1) + nums[i];
        const cur1 = prev0 - nums[i]; // previous must be not flipped
        prev0 = cur0;
        prev1 = cur1;
    }
    
    return Math.max(prev0, prev1);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximumTotalCost($nums) {
        $n = count($nums);
        if ($n == 0) return 0;
        // first element cannot be flipped
        $prev0 = $nums[0];
        $negInf = - (1 << 60); // sufficiently small
        $prev1 = $negInf;

        for ($i = 1; $i < $n; ++$i) {
            $cur0 = max($prev0, $prev1) + $nums[$i];
            $cur1 = $prev0 - $nums[$i]; // previous must be not flipped
            $prev0 = $cur0;
            $prev1 = $cur1;
        }

        return max($prev0, $prev1);
    }
}
```

## Swift

```swift
class Solution {
    func maximumTotalCost(_ nums: [Int]) -> Int {
        guard !nums.isEmpty else { return 0 }
        var prevNoFlip = nums[0]
        let NEG_INF = Int.min / 2
        var prevFlip = NEG_INF
        for i in 1..<nums.count {
            let val = nums[i]
            let curNoFlip = max(prevNoFlip, prevFlip) + val
            let curFlip = prevNoFlip - val
            prevNoFlip = curNoFlip
            prevFlip = curFlip
        }
        return max(prevNoFlip, prevFlip)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumTotalCost(nums: IntArray): Long {
        val n = nums.size
        var dpStart = nums[0].toLong()               // dp[i][0]: i is start of a subarray (positive sign)
        var dpNeg = Long.MIN_VALUE / 4                // dp[i][1]: i has negative sign, impossible for i=0
        for (i in 1 until n) {
            val v = nums[i].toLong()
            val newStart = kotlin.math.max(dpStart, dpNeg) + v   // start new subarray at i
            val newNeg = dpStart - v                             // continue alternation, i gets negative sign
            dpStart = newStart
            dpNeg = newNeg
        }
        return kotlin.math.max(dpStart, dpNeg)
    }
}
```

## Dart

```dart
class Solution {
  int maximumTotalCost(List<int> nums) {
    if (nums.isEmpty) return 0;
    const int negInf = -1 << 60; // sufficiently small
    int dp0 = nums[0]; // not flipped
    int dp1 = negInf;   // cannot flip first element

    for (int i = 1; i < nums.length; i++) {
      int ndp0 = (dp0 > dp1 ? dp0 : dp1) + nums[i];
      int ndp1 = dp0 - nums[i];
      dp0 = ndp0;
      dp1 = ndp1;
    }
    return dp0 > dp1 ? dp0 : dp1;
  }
}
```

## Golang

```go
func maximumTotalCost(nums []int) int64 {
	n := len(nums)
	if n == 0 {
		return 0
	}
	if n == 1 {
		return int64(nums[0])
	}
	dp0 := int64(nums[0]) + int64(nums[1]) // dp[i][0]
	dp1 := int64(nums[0]) - int64(nums[1]) // dp[i][1]

	for i := 2; i < n; i++ {
		val := int64(nums[i])
		new0 := dp0
		if dp1 > new0 {
			new0 = dp1
		}
		new0 += val
		new1 := dp0 - val
		dp0, dp1 = new0, new1
	}

	if dp1 > dp0 {
		return dp1
	}
	return dp0
}
```

## Ruby

```ruby
def maximum_total_cost(nums)
  n = nums.length
  return 0 if n == 0

  dp0 = nums[0]          # last element not flipped (positive sign)
  dp1 = -10**18          # impossible state for first element being flipped

  i = 1
  while i < n
    x = nums[i]
    new_dp0 = [dp0, dp1].max + x   # keep positive sign at i
    new_dp1 = dp0 - x              # flip sign at i (previous must be positive)
    dp0 = new_dp0
    dp1 = new_dp1
    i += 1
  end

  [dp0, dp1].max
end
```

## Scala

```scala
object Solution {
    def maximumTotalCost(nums: Array[Int]): Long = {
        val n = nums.length
        if (n == 1) return nums(0).toLong

        var dp0: Long = nums(0).toLong + nums(1).toLong // i not flipped
        var dp1: Long = nums(0).toLong - nums(1).toLong // i flipped

        var i = 2
        while (i < n) {
            val cur = nums(i).toLong
            val newDp0 = math.max(dp0, dp1) + cur
            val newDp1 = dp0 - cur
            dp0 = newDp0
            dp1 = newDp1
            i += 1
        }
        math.max(dp0, dp1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_total_cost(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        let mut prev0 = nums[0] as i64;               // sign + at index 0
        let mut prev1 = i64::MIN / 4;                 // impossible state (sign -)
        for &val in nums.iter().skip(1) {
            let cur0 = std::cmp::max(prev0, prev1) + val as i64;
            let cur1 = prev0 - val as i64;
            prev0 = cur0;
            prev1 = cur1;
        }
        std::cmp::max(prev0, prev1)
    }
}
```

## Racket

```racket
(define/contract (maximum-total-cost nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((first-num (car nums))
         (rest-nums (cdr nums)))
    (let loop ((prev0 first-num)          ; max sum ending at previous index, not flipped
               (prev1 #f)                ; max sum ending at previous index, flipped; #f means unavailable
               (lst rest-nums))
      (if (null? lst)
          (max prev0 (or prev1 prev0))
          (let* ((x (car lst))
                 (best-prev (if prev1 (max prev0 prev1) prev0))
                 (cur0 (+ best-prev x))   ; current not flipped
                 (cur1 (- prev0 x)))      ; current flipped, previous must be not flipped
            (loop cur0 cur1 (cdr lst)))))))
```

## Erlang

```erlang
-module(solution).
-export([maximum_total_cost/1]).

-spec maximum_total_cost(Nums :: [integer()]) -> integer().
maximum_total_cost([]) ->
    0;
maximum_total_cost([H]) ->
    H;
maximum_total_cost([First, Second | Rest]) ->
    DP0 = First + Second,
    DP1 = First - Second,
    final_max(DP0, DP1, Rest).

final_max(DP0, DP1, []) ->
    max(DP0, DP1);
final_max(DP0, DP1, [X | Tail]) ->
    New0 = max(DP0, DP1) + X,
    New1 = DP0 - X,
    final_max(New0, New1, Tail).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_total_cost(nums :: [integer]) :: integer
  def maximum_total_cost(nums) do
    [first | rest] = nums
    dp0 = first
    dp1 = -1_000_000_000_000_000_000

    {final0, final1} =
      Enum.reduce(rest, {dp0, dp1}, fn x, {prev0, prev1} ->
        new0 = max(prev0, prev1) + x
        new1 = prev0 - x
        {new0, new1}
      end)

    max(final0, final1)
  end
end
```
