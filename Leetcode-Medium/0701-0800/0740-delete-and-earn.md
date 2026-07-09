# 0740. Delete and Earn

## Cpp

```cpp
class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        if (nums.empty()) return 0;
        const int MAX_VAL = 10000;
        vector<long long> points(MAX_VAL + 1, 0);
        int maxNum = 0;
        for (int v : nums) {
            points[v] += v;
            if (v > maxNum) maxNum = v;
        }
        vector<long long> dp(maxNum + 2, 0); // extra space to avoid bounds
        dp[0] = 0;
        dp[1] = points[1];
        for (int i = 2; i <= maxNum; ++i) {
            dp[i] = max(dp[i - 1], dp[i - 2] + points[i]);
        }
        return static_cast<int>(dp[maxNum]);
    }
};
```

## Java

```java
class Solution {
    public int deleteAndEarn(int[] nums) {
        int maxVal = 0;
        for (int num : nums) {
            if (num > maxVal) maxVal = num;
        }
        long[] points = new long[maxVal + 1];
        for (int num : nums) {
            points[num] += num;
        }
        long[] dp = new long[maxVal + 1];
        dp[0] = 0;
        if (maxVal >= 1) dp[1] = points[1];
        for (int i = 2; i <= maxVal; i++) {
            dp[i] = Math.max(dp[i - 1], dp[i - 2] + points[i]);
        }
        return (int) dp[maxVal];
    }
}
```

## Python

```python
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_val = max(nums)
        points = [0] * (max_val + 1)
        for v in nums:
            points[v] += v

        take, skip = 0, 0
        for i in range(len(points)):
            take_i = skip + points[i]
            skip_i = max(take, skip)
            take, skip = take_i, skip_i
        return max(take, skip)
```

## Python3

```python
from typing import List
import collections

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cnt = collections.Counter(nums)
        max_val = max(cnt)
        earn = [0] * (max_val + 1)
        for val, frequency in cnt.items():
            earn[val] = val * frequency

        dp0, dp1 = 0, earn[1] if max_val >= 1 else 0
        for i in range(2, max_val + 1):
            dp0, dp1 = dp1, max(dp1, dp0 + earn[i])
        return dp1
```

## C

```c
int deleteAndEarn(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    int maxVal = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] > maxVal) maxVal = nums[i];
    }
    long long *freq = (long long *)calloc(maxVal + 1, sizeof(long long));
    for (int i = 0; i < numsSize; ++i) {
        freq[nums[i]] += 1;
    }
    long long prev2 = 0; // dp[i-2]
    long long prev1 = 0; // dp[i-1]
    for (int i = 1; i <= maxVal; ++i) {
        long long take = prev2 + (long long)i * freq[i];
        long long cur = (prev1 > take) ? prev1 : take;
        prev2 = prev1;
        prev1 = cur;
    }
    free(freq);
    return (int)prev1;
}
```

## Csharp

```csharp
public class Solution {
    public int DeleteAndEarn(int[] nums) {
        if (nums == null || nums.Length == 0) return 0;
        int maxVal = 0;
        foreach (int v in nums) {
            if (v > maxVal) maxVal = v;
        }
        long[] points = new long[maxVal + 1];
        foreach (int v in nums) {
            points[v] += v;
        }
        long takePrev = 0; // dp[i-2]
        long skipPrev = 0; // dp[i-1]
        for (int i = 1; i <= maxVal; i++) {
            long cur = Math.Max(skipPrev, takePrev + points[i]);
            takePrev = skipPrev;
            skipPrev = cur;
        }
        return (int)skipPrev;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var deleteAndEarn = function(nums) {
    let maxVal = 0;
    for (const v of nums) {
        if (v > maxVal) maxVal = v;
    }
    const points = new Array(maxVal + 1).fill(0);
    for (const v of nums) {
        points[v] += v;
    }
    let earnPrev = 0;                     // dp[i-2]
    let earnCurr = points[1] || 0;        // dp[i-1] when i == 1
    for (let i = 2; i <= maxVal; ++i) {
        const next = Math.max(earnCurr, earnPrev + points[i]);
        earnPrev = earnCurr;
        earnCurr = next;
    }
    return earnCurr;
};
```

## Typescript

```typescript
function deleteAndEarn(nums: number[]): number {
    if (nums.length === 0) return 0;
    const maxVal = Math.max(...nums);
    const sums = new Array(maxVal + 1).fill(0);
    for (const v of nums) {
        sums[v] += v;
    }
    let dpPrev2 = 0; // dp[i-2]
    let dpPrev1 = 0; // dp[i-1]
    for (let i = 0; i <= maxVal; i++) {
        const cur = Math.max(dpPrev1, dpPrev2 + sums[i]);
        dpPrev2 = dpPrev1;
        dpPrev1 = cur;
    }
    return dpPrev1;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function deleteAndEarn($nums) {
        if (empty($nums)) return 0;
        $max = 0;
        foreach ($nums as $v) {
            if ($v > $max) $max = $v;
        }
        $points = array_fill(0, $max + 1, 0);
        foreach ($nums as $v) {
            $points[$v] += $v;
        }
        $dpPrev2 = 0;               // dp[i-2]
        $dpPrev1 = $points[0];      // dp[i-1] for i=0
        for ($i = 1; $i <= $max; $i++) {
            $curr = max($dpPrev1, $dpPrev2 + $points[$i]);
            $dpPrev2 = $dpPrev1;
            $dpPrev1 = $curr;
        }
        return $dpPrev1;
    }
}
```

## Swift

```swift
class Solution {
    func deleteAndEarn(_ nums: [Int]) -> Int {
        guard !nums.isEmpty else { return 0 }
        let maxVal = nums.max()!
        var points = Array(repeating: 0, count: maxVal + 1)
        for v in nums {
            points[v] += v
        }
        var dpPrev2 = 0
        var dpPrev1 = 0
        for i in 0...maxVal {
            let cur = max(dpPrev1, dpPrev2 + points[i])
            dpPrev2 = dpPrev1
            dpPrev1 = cur
        }
        return dpPrev1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun deleteAndEarn(nums: IntArray): Int {
        if (nums.isEmpty()) return 0
        val maxVal = nums.maxOrNull() ?: 0
        val points = IntArray(maxVal + 1)
        for (v in nums) {
            points[v] += v
        }
        var twoBack = 0
        var oneBack = 0
        for (i in 0..maxVal) {
            val cur = maxOf(oneBack, twoBack + points[i])
            twoBack = oneBack
            oneBack = cur
        }
        return oneBack
    }
}
```

## Dart

```dart
class Solution {
  int deleteAndEarn(List<int> nums) {
    if (nums.isEmpty) return 0;
    int maxVal = 0;
    for (int v in nums) {
      if (v > maxVal) maxVal = v;
    }
    List<int> points = List.filled(maxVal + 1, 0);
    for (int v in nums) {
      points[v] += v;
    }
    int prev2 = 0; // dp[i-2]
    int prev1 = 0; // dp[i-1]
    for (int i = 0; i <= maxVal; ++i) {
      int cur = (prev1 > prev2 + points[i]) ? prev1 : prev2 + points[i];
      prev2 = prev1;
      prev1 = cur;
    }
    return prev1;
  }
}
```

## Golang

```go
func deleteAndEarn(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	maxVal := 0
	freq := make([]int, 10001)
	for _, v := range nums {
		freq[v]++
		if v > maxVal {
			maxVal = v
		}
	}
	points := make([]int, maxVal+1)
	for i := 0; i <= maxVal; i++ {
		points[i] = i * freq[i]
	}
	prev2, prev1 := 0, 0
	for i := 1; i <= maxVal; i++ {
		cur := prev1
		if val := prev2 + points[i]; val > cur {
			cur = val
		}
		prev2 = prev1
		prev1 = cur
	}
	return prev1
}
```

## Ruby

```ruby
def delete_and_earn(nums)
  max_val = nums.max
  counts = Array.new(max_val + 1, 0)
  nums.each { |v| counts[v] += 1 }
  points = Array.new(max_val + 1, 0)
  (0..max_val).each { |i| points[i] = i * counts[i] }

  dp_two_back = 0
  dp_one_back = points[1] || 0

  (2..max_val).each do |i|
    current = [dp_one_back, dp_two_back + points[i]].max
    dp_two_back = dp_one_back
    dp_one_back = current
  end

  max_val == 0 ? 0 : dp_one_back
end
```

## Scala

```scala
object Solution {
    def deleteAndEarn(nums: Array[Int]): Int = {
        if (nums.isEmpty) return 0
        val maxVal = nums.max
        val points = new Array[Long](maxVal + 1)
        for (v <- nums) {
            points(v) += v.toLong
        }
        var dpPrev2: Long = 0L
        var dpPrev1: Long = if (maxVal >= 1) points(1) else 0L
        var i = 2
        while (i <= maxVal) {
            val cur = math.max(dpPrev1, dpPrev2 + points(i))
            dpPrev2 = dpPrev1
            dpPrev1 = cur
            i += 1
        }
        dpPrev1.toInt
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn delete_and_earn(nums: Vec<i32>) -> i32 {
        use std::cmp::max;
        let max_val = *nums.iter().max().unwrap() as usize;
        let mut sums = vec![0i64; max_val + 1];
        for v in nums {
            sums[v as usize] += v as i64;
        }
        if max_val == 0 {
            return sums[0] as i32;
        }
        let mut dp_prev2: i64 = 0;
        let mut dp_prev1: i64 = sums[0];
        for i in 1..=max_val {
            let cur = max(dp_prev1, dp_prev2 + sums[i]);
            dp_prev2 = dp_prev1;
            dp_prev1 = cur;
        }
        dp_prev1 as i32
    }
}
```

## Racket

```racket
(define/contract (delete-and-earn nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((max-val (apply max nums))
         (freq (make-vector (+ max-val 1) 0)))
    ;; count frequencies
    (for ([n nums])
      (vector-set! freq n (+ 1 (vector-ref freq n))))
    (define dp0 0)
    (if (= max-val 0)
        dp0
        (let loop ((i 1) (prev2 dp0) (prev1 (* 1 (vector-ref freq 1))))
          (if (> i max-val)
              prev1
              (let* ((cur (max prev1 (+ prev2 (* i (vector-ref freq i))))))
                (loop (+ i 1) prev1 cur)))))))
```

## Erlang

```erlang
-spec delete_and_earn(Nums :: [integer()]) -> integer().
delete_and_earn(Nums) ->
    case Nums of
        [] -> 0;
        _ ->
            FreqMap = lists:foldl(
                fun(N, Acc) ->
                    maps:update_with(N, fun(C) -> C + 1 end, 1, Acc)
                end,
                #{},
                Nums),
            MaxVal = lists:max(Nums),
            Points1 = 1 * maps:get(1, FreqMap, 0),
            case MaxVal of
                0 -> 0;
                1 -> Points1;
                _ ->
                    dp(2, 0, Points1, MaxVal, FreqMap)
            end
    end.

dp(I, Prev2, Prev1, Max, Map) when I =< Max ->
    PointsI = I * maps:get(I, Map, 0),
    Curr = erlang:max(Prev1, Prev2 + PointsI),
    dp(I + 1, Prev1, Curr, Max, Map);
dp(_, _, Prev1, _, _) -> Prev1.
```

## Elixir

```elixir
defmodule Solution do
  @spec delete_and_earn(nums :: [integer]) :: integer
  def delete_and_earn(nums) do
    case nums do
      [] -> 0
      _ ->
        max_val = Enum.max(nums)

        counts =
          Enum.reduce(nums, %{}, fn x, acc ->
            Map.update(acc, x, 1, &(&1 + 1))
          end)

        {_prev2, result} =
          Enum.reduce(0..max_val, {0, 0}, fn i, {dp_i_2, dp_i_1} ->
            cur = max(dp_i_1, dp_i_2 + i * Map.get(counts, i, 0))
            {dp_i_1, cur}
          end)

        result
    end
  end
end
```
