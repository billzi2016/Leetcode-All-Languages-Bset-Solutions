# 2342. Max Sum of a Pair With Equal Sum of Digits

## Cpp

```cpp
class Solution {
public:
    int maximumSum(vector<int>& nums) {
        auto digitSum = [](int x) {
            int s = 0;
            while (x) {
                s += x % 10;
                x /= 10;
            }
            return s;
        };
        
        const int MAX_SUM = 81; // max possible digit sum for numbers <= 1e9
        vector<int> best(MAX_SUM + 1, -1);
        int ans = -1;
        for (int num : nums) {
            int d = digitSum(num);
            if (best[d] != -1) {
                ans = max(ans, best[d] + num);
            }
            best[d] = max(best[d], num);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maximumSum(int[] nums) {
        int[] maxForSum = new int[82];
        int result = -1;
        for (int num : nums) {
            int ds = digitSum(num);
            if (maxForSum[ds] != 0) {
                result = Math.max(result, maxForSum[ds] + num);
            }
            if (num > maxForSum[ds]) {
                maxForSum[ds] = num;
            }
        }
        return result;
    }

    private int digitSum(int n) {
        int sum = 0;
        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }
        return sum;
    }
}
```

## Python

```python
class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_by_sum = [-1] * 82  # digit sum can be at most 81 (9*9)
        result = -1
        for num in nums:
            s = 0
            x = num
            while x:
                s += x % 10
                x //= 10
            if max_by_sum[s] != -1:
                result = max(result, num + max_by_sum[s])
            if num > max_by_sum[s]:
                max_by_sum[s] = num
        return result
```

## Python3

```python
from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        max_by_sum = [-1] * 82  # possible digit sums: 0..81
        ans = -1
        for num in nums:
            s = 0
            x = num
            while x:
                s += x % 10
                x //= 10
            if max_by_sum[s] != -1:
                ans = max(ans, max_by_sum[s] + num)
            if num > max_by_sum[s]:
                max_by_sum[s] = num
        return ans
```

## C

```c
int maximumSum(int* nums, int numsSize) {
    int maxByDigit[82];
    for (int i = 0; i < 82; ++i) maxByDigit[i] = -1;
    int best = -1;
    for (int i = 0; i < numsSize; ++i) {
        int x = nums[i];
        int sum = 0;
        while (x > 0) {
            sum += x % 10;
            x /= 10;
        }
        if (maxByDigit[sum] != -1) {
            int candidate = nums[i] + maxByDigit[sum];
            if (candidate > best) best = candidate;
        }
        if (nums[i] > maxByDigit[sum]) maxByDigit[sum] = nums[i];
    }
    return best;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaximumSum(int[] nums)
    {
        int[] maxForSum = new int[82];
        int result = -1;

        foreach (int num in nums)
        {
            int ds = DigitSum(num);
            if (maxForSum[ds] > 0)
            {
                int candidate = maxForSum[ds] + num;
                if (candidate > result) result = candidate;
            }
            if (num > maxForSum[ds]) maxForSum[ds] = num;
        }

        return result;
    }

    private int DigitSum(int n)
    {
        int sum = 0;
        while (n > 0)
        {
            sum += n % 10;
            n /= 10;
        }
        return sum;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumSum = function(nums) {
    const maxByDigit = new Array(82).fill(-1);
    let ans = -1;
    for (const num of nums) {
        let sum = 0, x = num;
        while (x > 0) {
            sum += x % 10;
            x = Math.trunc(x / 10);
        }
        if (maxByDigit[sum] !== -1) {
            ans = Math.max(ans, maxByDigit[sum] + num);
        }
        if (num > maxByDigit[sum]) {
            maxByDigit[sum] = num;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function maximumSum(nums: number[]): number {
    const maxBySum = new Array(82).fill(-1);
    let ans = -1;
    for (const num of nums) {
        let sum = 0;
        let x = num;
        while (x > 0) {
            sum += x % 10;
            x = Math.floor(x / 10);
        }
        // handle the case when num is 0
        if (maxBySum[sum] !== -1) {
            ans = Math.max(ans, num + maxBySum[sum]);
        }
        if (num > maxBySum[sum]) {
            maxBySum[sum] = num;
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
    function maximumSum($nums) {
        // Maximum possible digit sum for numbers up to 1e9 is 81 (9*9)
        $maxByDigitSum = array_fill(0, 82, -1);
        $result = -1;
        
        foreach ($nums as $num) {
            $ds = 0;
            $temp = $num;
            while ($temp > 0) {
                $ds += $temp % 10;
                $temp = intdiv($temp, 10);
            }
            
            if ($maxByDigitSum[$ds] != -1) {
                $candidate = $num + $maxByDigitSum[$ds];
                if ($candidate > $result) {
                    $result = $candidate;
                }
            }
            if ($num > $maxByDigitSum[$ds]) {
                $maxByDigitSum[$ds] = $num;
            }
        }
        
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func maximumSum(_ nums: [Int]) -> Int {
        var maxFor = Array(repeating: -1, count: 82)
        var result = -1
        for num in nums {
            var x = num
            var sum = 0
            while x > 0 {
                sum += x % 10
                x /= 10
            }
            if maxFor[sum] != -1 {
                result = max(result, num + maxFor[sum])
            }
            if num > maxFor[sum] {
                maxFor[sum] = num
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumSum(nums: IntArray): Int {
        val maxByDigitSum = IntArray(82) { -1 }
        var result = -1
        for (num in nums) {
            var x = num
            var digitSum = 0
            while (x > 0) {
                digitSum += x % 10
                x /= 10
            }
            if (maxByDigitSum[digitSum] != -1) {
                val candidate = maxByDigitSum[digitSum] + num
                if (candidate > result) result = candidate
            }
            if (num > maxByDigitSum[digitSum]) {
                maxByDigitSum[digitSum] = num
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  int _digitSum(int num) {
    int sum = 0;
    while (num > 0) {
      sum += num % 10;
      num ~/= 10;
    }
    return sum;
  }

  int maximumSum(List<int> nums) {
    List<int> best = List.filled(82, -1);
    int result = -1;
    for (int v in nums) {
      int ds = _digitSum(v);
      if (best[ds] != -1) {
        int candidate = best[ds] + v;
        if (candidate > result) result = candidate;
      }
      if (v > best[ds]) best[ds] = v;
    }
    return result;
  }
}
```

## Golang

```go
func maximumSum(nums []int) int {
    var maxBySum [82]int
    result := -1

    for _, num := range nums {
        sum := 0
        x := num
        for x > 0 {
            sum += x % 10
            x /= 10
        }
        if maxBySum[sum] != 0 {
            if candidate := maxBySum[sum] + num; candidate > result {
                result = candidate
            }
        }
        if num > maxBySum[sum] {
            maxBySum[sum] = num
        }
    }

    return result
}
```

## Ruby

```ruby
def digit_sum(num)
  sum = 0
  while num > 0
    sum += num % 10
    num /= 10
  end
  sum
end

# @param {Integer[]} nums
# @return {Integer}
def maximum_sum(nums)
  max_by_digit = Array.new(82, -1)
  best = -1
  nums.each do |num|
    ds = digit_sum(num)
    if max_by_digit[ds] != -1
      best = [best, num + max_by_digit[ds]].max
    end
    max_by_digit[ds] = [max_by_digit[ds], num].max
  end
  best
end
```

## Scala

```scala
object Solution {
    def maximumSum(nums: Array[Int]): Int = {
        val maxByDigitSum = Array.fill(82)(-1)
        var result = -1

        def digitSum(x: Int): Int = {
            var n = x
            var sum = 0
            while (n > 0) {
                sum += n % 10
                n /= 10
            }
            sum
        }

        for (num <- nums) {
            val ds = digitSum(num)
            if (maxByDigitSum(ds) != -1) {
                result = math.max(result, maxByDigitSum(ds) + num)
            }
            if (num > maxByDigitSum(ds)) {
                maxByDigitSum(ds) = num
            }
        }

        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_sum(nums: Vec<i32>) -> i32 {
        const MAX_DIGIT_SUM: usize = 82; // max possible sum of digits for nums[i] <= 10^9
        let mut best = [-1i32; MAX_DIGIT_SUM];
        let mut answer = -1i32;

        for &num in nums.iter() {
            let mut x = num;
            let mut ds: usize = 0;
            while x > 0 {
                ds += (x % 10) as usize;
                x /= 10;
            }
            if best[ds] != -1 {
                answer = answer.max(num + best[ds]);
            }
            if num > best[ds] {
                best[ds] = num;
            }
        }

        answer
    }
}
```

## Racket

```racket
(define (digit-sum n)
  (let loop ((x n) (s 0))
    (if (= x 0)
        s
        (loop (quotient x 10) (+ s (remainder x 10))))))

(define/contract (maximum-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((max-digit-sum 81)
         (best (make-vector (+ max-digit-sum 1) -1)))
    (let loop ((lst nums) (res -1))
      (if (null? lst)
          res
          (let* ((num (car lst))
                 (ds (digit-sum num))
                 (prev (vector-ref best ds))
                 (new-res (if (= prev -1)
                              res
                              (max res (+ num prev)))))
            (when (> num prev)
              (vector-set! best ds num))
            (loop (cdr lst) new-res))))))
```

## Erlang

```erlang
-module(solution).
-export([maximum_sum/1]).

-spec maximum_sum(Nums :: [integer()]) -> integer().
maximum_sum(Nums) ->
    Tuple0 = erlang:make_tuple(82, 0),
    {_, Result} = lists:foldl(
        fun(N, {TupleAcc, Res}) ->
            DS = digit_sum(N),
            Index = DS + 1,
            Prev = element(Index, TupleAcc),
            NewRes = case Prev of
                0 -> Res;
                _ -> erlang:max(Res, N + Prev)
            end,
            UpdatedTuple = if N > Prev -> setelement(Index, TupleAcc, N); true -> TupleAcc end,
            {UpdatedTuple, NewRes}
        end,
        {Tuple0, -1},
        Nums),
    Result.

digit_sum(0) -> 0;
digit_sum(N) when N < 10 -> N;
digit_sum(N) ->
    digit_sum(N div 10) + (N rem 10).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_sum(nums :: [integer]) :: integer
  def maximum_sum(nums) do
    max_by_digit = List.duplicate(-1, 82)

    {_final_arr, result} =
      Enum.reduce(nums, {max_by_digit, -1}, fn num, {arr, res} ->
        ds = digit_sum(num)
        prev = Enum.at(arr, ds)

        new_res =
          if prev != -1 do
            max(res, prev + num)
          else
            res
          end

        new_max = if num > prev, do: num, else: prev
        new_arr = List.replace_at(arr, ds, new_max)
        {new_arr, new_res}
      end)

    result
  end

  defp digit_sum(0), do: 0

  defp digit_sum(num) when is_integer(num) and num > 0 do
    digit_sum(num, 0)
  end

  defp digit_sum(0, acc), do: acc

  defp digit_sum(n, acc) do
    digit_sum(div(n, 10), acc + rem(n, 10))
  end
end
```
