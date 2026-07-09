# 2256. Minimum Average Difference

## Cpp

```cpp
class Solution {
public:
    int minimumAverageDifference(std::vector<int>& nums) {
        int n = nums.size();
        long long total = 0;
        for (int v : nums) total += v;
        long long prefix = 0;
        long long bestDiff = LLONG_MAX;
        int bestIdx = 0;
        for (int i = 0; i < n; ++i) {
            prefix += nums[i];
            long long leftAvg = prefix / (i + 1);
            long long rightAvg = 0;
            if (i != n - 1) {
                long long rightSum = total - prefix;
                int rightCnt = n - i - 1;
                rightAvg = rightSum / rightCnt;
            }
            long long diff = std::llabs(leftAvg - rightAvg);
            if (diff < bestDiff) {
                bestDiff = diff;
                bestIdx = i;
            }
        }
        return bestIdx;
    }
};
```

## Java

```java
class Solution {
    public int minimumAverageDifference(int[] nums) {
        int n = nums.length;
        long total = 0L;
        for (int num : nums) total += num;
        long prefixSum = 0L;
        long minDiff = Long.MAX_VALUE;
        int answer = 0;
        for (int i = 0; i < n; i++) {
            prefixSum += nums[i];
            long leftAvg = prefixSum / (i + 1);
            long rightAvg = 0L;
            if (i != n - 1) {
                long suffixSum = total - prefixSum;
                rightAvg = suffixSum / (n - i - 1);
            }
            long diff = Math.abs(leftAvg - rightAvg);
            if (diff < minDiff) {
                minDiff = diff;
                answer = i;
            }
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def minimumAverageDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = sum(nums)
        prefix = 0
        min_diff = float('inf')
        answer = -1

        for i, val in enumerate(nums):
            prefix += val
            left_avg = prefix // (i + 1)

            if i < n - 1:
                right_sum = total - prefix
                right_cnt = n - i - 1
                right_avg = right_sum // right_cnt
            else:
                right_avg = 0

            diff = abs(left_avg - right_avg)
            if diff < min_diff:
                min_diff = diff
                answer = i

        return answer
```

## Python3

```python
from typing import List

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        prefix = 0
        min_diff = float('inf')
        ans = -1
        for i, val in enumerate(nums):
            prefix += val
            left_avg = prefix // (i + 1)
            right_cnt = n - i - 1
            if right_cnt:
                right_avg = (total - prefix) // right_cnt
            else:
                right_avg = 0
            diff = abs(left_avg - right_avg)
            if diff < min_diff:
                min_diff = diff
                ans = i
        return ans
```

## C

```c
#include <stdlib.h>
#include <limits.h>

int minimumAverageDifference(int* nums, int numsSize) {
    long long total = 0;
    for (int i = 0; i < numsSize; ++i) {
        total += nums[i];
    }
    
    long long prefix = 0;
    long long minDiff = LLONG_MAX;
    int ans = 0;
    
    for (int i = 0; i < numsSize; ++i) {
        prefix += nums[i];
        long long leftAvg = prefix / (i + 1);
        long long rightAvg = 0;
        if (i != numsSize - 1) {
            rightAvg = (total - prefix) / (numsSize - i - 1);
        }
        long long diff = llabs(leftAvg - rightAvg);
        if (diff < minDiff) {
            minDiff = diff;
            ans = i;
        }
    }
    
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinimumAverageDifference(int[] nums)
    {
        int n = nums.Length;
        long totalSum = 0;
        foreach (int num in nums) totalSum += num;

        long prefixSum = 0;
        long minDiff = long.MaxValue;
        int answer = 0;

        for (int i = 0; i < n; i++)
        {
            prefixSum += nums[i];
            long leftAvg = prefixSum / (i + 1);
            long rightAvg = 0;
            int rightCount = n - i - 1;
            if (rightCount > 0)
            {
                rightAvg = (totalSum - prefixSum) / rightCount;
            }
            long diff = Math.Abs(leftAvg - rightAvg);
            if (diff < minDiff)
            {
                minDiff = diff;
                answer = i;
            }
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumAverageDifference = function(nums) {
    const n = nums.length;
    let total = 0;
    for (let v of nums) total += v;

    let prefix = 0;
    let bestIdx = 0;
    let minDiff = Number.MAX_SAFE_INTEGER;

    for (let i = 0; i < n; ++i) {
        prefix += nums[i];
        const leftAvg = Math.floor(prefix / (i + 1));
        const rightLen = n - i - 1;
        const rightAvg = rightLen === 0 ? 0 : Math.floor((total - prefix) / rightLen);
        const diff = Math.abs(leftAvg - rightAvg);
        if (diff < minDiff) {
            minDiff = diff;
            bestIdx = i;
        }
    }

    return bestIdx;
};
```

## Typescript

```typescript
function minimumAverageDifference(nums: number[]): number {
    const n = nums.length;
    let total = 0;
    for (const v of nums) total += v;

    let prefix = 0;
    let minDiff = Number.MAX_SAFE_INTEGER;
    let ans = 0;

    for (let i = 0; i < n; i++) {
        prefix += nums[i];
        const leftAvg = Math.floor(prefix / (i + 1));
        const rightCount = n - i - 1;
        const rightAvg = rightCount === 0 ? 0 : Math.floor((total - prefix) / rightCount);
        const diff = Math.abs(leftAvg - rightAvg);

        if (diff < minDiff) {
            minDiff = diff;
            ans = i;
        }
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumAverageDifference($nums) {
        $n = count($nums);
        $total = array_sum($nums);
        $prefix = 0;
        $minDiff = PHP_INT_MAX;
        $ans = 0;

        for ($i = 0; $i < $n; $i++) {
            $prefix += $nums[$i];
            $leftAvg = intdiv($prefix, $i + 1);
            if ($i == $n - 1) {
                $rightAvg = 0;
            } else {
                $rightAvg = intdiv($total - $prefix, $n - $i - 1);
            }
            $diff = abs($leftAvg - $rightAvg);
            if ($diff < $minDiff) {
                $minDiff = $diff;
                $ans = $i;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minimumAverageDifference(_ nums: [Int]) -> Int {
        let n = nums.count
        var total: Int64 = 0
        for v in nums {
            total += Int64(v)
        }
        var prefix: Int64 = 0
        var minDiff: Int64 = Int64.max
        var answer = 0
        for i in 0..<n {
            prefix += Int64(nums[i])
            let leftAvg = prefix / Int64(i + 1)
            let rightCount = n - i - 1
            let rightAvg: Int64 = rightCount > 0 ? (total - prefix) / Int64(rightCount) : 0
            let diff = leftAvg >= rightAvg ? leftAvg - rightAvg : rightAvg - leftAvg
            if diff < minDiff {
                minDiff = diff
                answer = i
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumAverageDifference(nums: IntArray): Int {
        val n = nums.size
        var total = 0L
        for (v in nums) total += v.toLong()
        var prefix = 0L
        var minDiff = Long.MAX_VALUE
        var answer = 0
        for (i in 0 until n) {
            prefix += nums[i].toLong()
            val leftAvg = prefix / (i + 1)
            val rightCount = n - i - 1
            val rightAvg = if (rightCount > 0) (total - prefix) / rightCount else 0L
            val diff = kotlin.math.abs(leftAvg - rightAvg)
            if (diff < minDiff) {
                minDiff = diff
                answer = i
            }
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int minimumAverageDifference(List<int> nums) {
    int n = nums.length;
    int total = 0;
    for (int v in nums) {
      total += v;
    }

    int prefix = 0;
    int bestIdx = 0;
    int bestDiff = 1 << 62; // sufficiently large

    for (int i = 0; i < n; ++i) {
      prefix += nums[i];
      int leftAvg = prefix ~/ (i + 1);
      int rightCount = n - i - 1;
      int rightAvg = rightCount > 0 ? (total - prefix) ~/ rightCount : 0;
      int diff = (leftAvg - rightAvg).abs();

      if (diff < bestDiff) {
        bestDiff = diff;
        bestIdx = i;
      }
    }

    return bestIdx;
  }
}
```

## Golang

```go
func minimumAverageDifference(nums []int) int {
    n := len(nums)
    var total int64
    for _, v := range nums {
        total += int64(v)
    }
    var prefix int64
    minDiff := int64(^uint64(0) >> 1) // max int64
    result := 0

    for i, v := range nums {
        prefix += int64(v)
        leftAvg := prefix / int64(i+1)

        rightCount := n - i - 1
        var rightAvg int64
        if rightCount > 0 {
            rightAvg = (total - prefix) / int64(rightCount)
        } else {
            rightAvg = 0
        }

        diff := leftAvg - rightAvg
        if diff < 0 {
            diff = -diff
        }
        if diff < minDiff {
            minDiff = diff
            result = i
        }
    }
    return result
}
```

## Ruby

```ruby
def minimum_average_difference(nums)
  n = nums.length
  total = nums.sum
  prefix = 0
  min_diff = Float::INFINITY
  answer = 0

  nums.each_with_index do |val, i|
    prefix += val
    left_avg = prefix / (i + 1)

    if i == n - 1
      right_avg = 0
    else
      right_sum = total - prefix
      right_cnt = n - i - 1
      right_avg = right_sum / right_cnt
    end

    diff = (left_avg - right_avg).abs
    if diff < min_diff
      min_diff = diff
      answer = i
    end
  end

  answer
end
```

## Scala

```scala
object Solution {
    def minimumAverageDifference(nums: Array[Int]): Int = {
        val n = nums.length
        var total: Long = 0L
        for (v <- nums) total += v.toLong

        var prefix: Long = 0L
        var minDiff: Long = Long.MaxValue
        var answer: Int = 0

        var i = 0
        while (i < n) {
            prefix += nums(i).toLong
            val leftAvg = prefix / (i + 1)
            val rightCount = n - i - 1
            val rightAvg = if (rightCount > 0) (total - prefix) / rightCount else 0L
            val diff = math.abs(leftAvg - rightAvg)

            if (diff < minDiff) {
                minDiff = diff
                answer = i
            }
            i += 1
        }

        answer
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_average_difference(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let total: i64 = nums.iter().map(|&x| x as i64).sum();
        let mut prefix: i64 = 0;
        let mut min_diff: i64 = i64::MAX;
        let mut ans: usize = 0;

        for (i, &val) in nums.iter().enumerate() {
            prefix += val as i64;
            let left_avg = prefix / ((i + 1) as i64);
            let right_len = n - i - 1;
            let right_avg = if right_len > 0 {
                (total - prefix) / (right_len as i64)
            } else {
                0
            };
            let diff = (left_avg - right_avg).abs();
            if diff < min_diff {
                min_diff = diff;
                ans = i;
            }
        }

        ans as i32
    }
}
```

## Racket

```racket
(define/contract (minimum-average-difference nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (vec (list->vector nums))
         (total
          (let loop ((i 0) (acc 0))
            (if (= i n)
                acc
                (loop (+ i 1) (+ acc (vector-ref vec i))))))
         (result
          (let loop ((i 0) (pref 0) (best-diff #f) (best-idx 0))
            (if (= i n)
                best-idx
                (let* ((pref2 (+ pref (vector-ref vec i)))
                       (left-avg (quotient pref2 (+ i 1)))
                       (right-len (- n i 1))
                       (right-sum (- total pref2))
                       (right-avg (if (> right-len 0)
                                      (quotient right-sum right-len)
                                      0))
                       (diff (abs (- left-avg right-avg))))
                  (if (or (not best-diff) (< diff best-diff))
                      (loop (+ i 1) pref2 diff i)
                      (loop (+ i 1) pref2 best-diff best-idx)))))))
    result))
```

## Erlang

```erlang
-spec minimum_average_difference([integer()]) -> integer().
minimum_average_difference(Nums) ->
    Total = lists:foldl(fun(X, Acc) -> X + Acc end, 0, Nums),
    N = length(Nums),
    loop(Nums, 0, 0, Total, N, 1 bsl 62, 0).

loop([], _Idx, _Prefix, _Total, _N, _BestDiff, BestIdx) ->
    BestIdx;
loop([H|T], Idx, Prefix, Total, N, BestDiff, BestIdx) ->
    NewPrefix = Prefix + H,
    LeftAvg = NewPrefix div (Idx + 1),
    RightLen = N - Idx - 1,
    RightAvg = case RightLen > 0 of
        true -> (Total - NewPrefix) div RightLen;
        false -> 0
    end,
    Diff = abs(LeftAvg - RightAvg),
    {NewBestDiff, NewBestIdx} =
        if Diff < BestDiff ->
                {Diff, Idx};
           true ->
                {BestDiff, BestIdx}
        end,
    loop(T, Idx + 1, NewPrefix, Total, N, NewBestDiff, NewBestIdx).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_average_difference(nums :: [integer]) :: integer
  def minimum_average_difference(nums) do
    n = length(nums)
    total = Enum.sum(nums)

    {_, _, ans} =
      nums
      |> Enum.with_index()
      |> Enum.reduce({0, nil, 0}, fn {val, i}, {pref_sum, min_diff, best_idx} ->
        pref_sum = pref_sum + val

        left_avg = div(pref_sum, i + 1)

        right_len = n - i - 1

        right_avg =
          if right_len == 0 do
            0
          else
            div(total - pref_sum, right_len)
          end

        diff = abs(left_avg - right_avg)

        case min_diff do
          nil ->
            {pref_sum, diff, i}

          md when diff < md ->
            {pref_sum, diff, i}

          _ ->
            {pref_sum, min_diff, best_idx}
        end
      end)

    ans
  end
end
```
