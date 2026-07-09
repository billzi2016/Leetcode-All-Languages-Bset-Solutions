# 0396. Rotate Function

## Cpp

```cpp
class Solution {
public:
    int maxRotateFunction(vector<int>& nums) {
        long long total = 0;
        long long f = 0;
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            total += nums[i];
            f += 1LL * i * nums[i];
        }
        long long maxVal = f;
        for (int k = 1; k < n; ++k) {
            // element that moves to front is nums[n - k]
            f = f + total - 1LL * n * nums[n - k];
            if (f > maxVal) maxVal = f;
        }
        return static_cast<int>(maxVal);
    }
};
```

## Java

```java
class Solution {
    public int maxRotateFunction(int[] nums) {
        int n = nums.length;
        long sum = 0, f = 0;
        for (int i = 0; i < n; i++) {
            sum += nums[i];
            f += (long) i * nums[i];
        }
        long max = f;
        long cur = f;
        for (int k = 1; k < n; k++) {
            cur = cur + sum - (long) n * nums[n - k];
            if (cur > max) {
                max = cur;
            }
        }
        return (int) max;
    }
}
```

## Python

```python
class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        total = sum(nums)
        f = sum(i * num for i, num in enumerate(nums))
        max_val = f
        # iterate k from 1 to n-1
        for k in range(1, n):
            # element that moves to front is nums[n - k]
            f += total - n * nums[n - k]
            if f > max_val:
                max_val = f
        return max_val
```

## Python3

```python
from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        total = sum(nums)
        f = sum(i * num for i, num in enumerate(nums))
        max_val = f
        for k in range(1, n):
            f += total - n * nums[-k]
            if f > max_val:
                max_val = f
        return max_val
```

## C

```c
int maxRotateFunction(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    long long total = 0;
    long long f = 0;
    for (int i = 0; i < numsSize; ++i) {
        total += nums[i];
        f += (long long)i * nums[i];
    }
    long long maxVal = f;
    long long cur = f;
    for (int k = 1; k < numsSize; ++k) {
        cur = cur + total - (long long)numsSize * nums[numsSize - k];
        if (cur > maxVal) maxVal = cur;
    }
    return (int)maxVal;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxRotateFunction(int[] nums)
    {
        int n = nums.Length;
        if (n == 0) return 0;

        long sum = 0;
        long f = 0;
        for (int i = 0; i < n; i++)
        {
            sum += nums[i];
            f += (long)i * nums[i];
        }

        long max = f;
        for (int k = 1; k < n; k++)
        {
            f = f + sum - (long)n * nums[n - k];
            if (f > max) max = f;
        }

        return (int)max;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxRotateFunction = function(nums) {
    const n = nums.length;
    if (n === 0) return 0;
    let sum = 0;
    let f = 0;
    for (let i = 0; i < n; ++i) {
        sum += nums[i];
        f += i * nums[i];
    }
    let max = f;
    for (let k = 1; k < n; ++k) {
        // element that moves to front after k rotations is nums[n - k]
        f = f + sum - n * nums[n - k];
        if (f > max) max = f;
    }
    return max;
};
```

## Typescript

```typescript
function maxRotateFunction(nums: number[]): number {
    const n = nums.length;
    if (n === 0) return 0;

    let totalSum = 0;
    let f = 0;
    for (let i = 0; i < n; i++) {
        totalSum += nums[i];
        f += i * nums[i];
    }

    let maxVal = f;
    // Compute F(k) using recurrence: F(k) = F(k-1) + totalSum - n * nums[n - k]
    for (let k = 1; k < n; k++) {
        f = f + totalSum - n * nums[n - k];
        if (f > maxVal) maxVal = f;
    }

    return maxVal;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxRotateFunction($nums) {
        $n = count($nums);
        if ($n == 0) return 0;
        $sum = 0;
        $f = 0;
        for ($i = 0; $i < $n; $i++) {
            $sum += $nums[$i];
            $f += $i * $nums[$i];
        }
        $max = $f;
        for ($k = 1; $k < $n; $k++) {
            $f = $f + $sum - $n * $nums[$n - $k];
            if ($f > $max) {
                $max = $f;
            }
        }
        return $max;
    }
}
```

## Swift

```swift
class Solution {
    func maxRotateFunction(_ nums: [Int]) -> Int {
        let n = nums.count
        if n == 0 { return 0 }
        var total = 0
        var f = 0
        for i in 0..<n {
            total += nums[i]
            f += i * nums[i]
        }
        var maxVal = f
        var cur = f
        if n > 1 {
            for k in 1..<n {
                cur = cur + total - n * nums[n - k]
                if cur > maxVal { maxVal = cur }
            }
        }
        return maxVal
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxRotateFunction(nums: IntArray): Int {
        val n = nums.size
        var sumAll = 0L
        var f = 0L
        for (i in 0 until n) {
            sumAll += nums[i].toLong()
            f += i.toLong() * nums[i]
        }
        var maxVal = f
        var cur = f
        for (k in 1 until n) {
            cur = cur + sumAll - n.toLong() * nums[n - k]
            if (cur > maxVal) maxVal = cur
        }
        return maxVal.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int maxRotateFunction(List<int> nums) {
    int n = nums.length;
    if (n == 0) return 0;
    int total = 0;
    int f = 0;
    for (int i = 0; i < n; i++) {
      total += nums[i];
      f += i * nums[i];
    }
    int maxVal = f;
    int cur = f;
    for (int k = 1; k < n; k++) {
      cur = cur + total - n * nums[n - k];
      if (cur > maxVal) maxVal = cur;
    }
    return maxVal;
  }
}
```

## Golang

```go
func maxRotateFunction(nums []int) int {
    n := len(nums)
    if n == 0 {
        return 0
    }
    var sum, f int64
    for i, v := range nums {
        sum += int64(v)
        f += int64(i * v)
    }
    maxVal := f
    cur := f
    for k := 1; k < n; k++ {
        cur = cur + sum - int64(n)*int64(nums[n-k])
        if cur > maxVal {
            maxVal = cur
        }
    }
    return int(maxVal)
}
```

## Ruby

```ruby
def max_rotate_function(nums)
  n = nums.length
  total = nums.sum
  f = 0
  nums.each_with_index { |val, i| f += i * val }
  max_val = f
  cur = f
  (1...n).each do |k|
    cur = cur + total - n * nums[n - k]
    max_val = cur if cur > max_val
  end
  max_val
end
```

## Scala

```scala
object Solution {
    def maxRotateFunction(nums: Array[Int]): Int = {
        val n = nums.length
        var totalSum: Long = 0L
        var f0: Long = 0L
        for (i <- 0 until n) {
            totalSum += nums(i).toLong
            f0 += i.toLong * nums(i)
        }
        var maxVal = f0
        var cur = f0
        for (k <- 1 until n) {
            val idx = n - k
            cur = cur + totalSum - n.toLong * nums(idx)
            if (cur > maxVal) maxVal = cur
        }
        maxVal.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_rotate_function(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        let total: i64 = nums.iter().map(|&x| x as i64).sum();
        let mut f: i64 = (0..n).map(|i| i as i64 * nums[i] as i64).sum();
        let mut max_f = f;
        for k in 1..n {
            let idx = n - k;
            f = f + total - (n as i64) * nums[idx] as i64;
            if f > max_f {
                max_f = f;
            }
        }
        max_f as i32
    }
}
```

## Racket

```racket
(define/contract (max-rotate-function nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([v (list->vector nums)]
         [n (vector-length v)])
    (if (= n 0)
        0
        (let loop ((i 0) (f0 0) (sum 0))
          (if (= i n)
              (let recur ((k 1) (prev f0) (mx f0))
                (if (= k n)
                    mx
                    (let* ([idx (- n k)]
                           [curr (+ prev sum (* -1 n (vector-ref v idx)))])
                      (recur (+ k 1) curr (if (> curr mx) curr mx)))))
              (let* ([val (vector-ref v i)])
                (loop (+ i 1)
                      (+ f0 (* i val))
                      (+ sum val))))))))
```

## Erlang

```erlang
-module(solution).
-export([max_rotate_function/1]).

-spec max_rotate_function(Nums :: [integer()]) -> integer().
max_rotate_function(Nums) ->
    Tuple = list_to_tuple(Nums),
    N = tuple_size(Tuple),
    Total = total_sum(Tuple, N),
    F0 = calc_f0(Tuple, N, 0, 0),
    max_rotate(N, Tuple, Total, F0, F0, 1).

total_sum(_Tuple, N) when N =:= 0 -> 0;
total_sum(Tuple, N) ->
    total_sum(Tuple, N, 1, 0).

total_sum(_Tuple, N, Index, Acc) when Index > N ->
    Acc;
total_sum(Tuple, N, Index, Acc) ->
    Val = element(Index, Tuple),
    total_sum(Tuple, N, Index + 1, Acc + Val).

calc_f0(_Tuple, N, _Idx, Sum) when Idx >= N -> Sum;
calc_f0(Tuple, N, Idx, Sum) when Idx >= N ->
    Sum;
calc_f0(Tuple, N, Idx, Sum) ->
    Val = element(Idx + 1, Tuple),
    calc_f0(Tuple, N, Idx + 1, Sum + Idx * Val).

max_rotate(N, _Tuple, _Total, Max, _Prev, K) when K >= N ->
    Max;
max_rotate(N, Tuple, Total, Max, Prev, K) ->
    Idx = N - K,
    Val = element(Idx + 1, Tuple),
    Cur = Prev + Total - N * Val,
    NewMax = if Cur > Max -> Cur; true -> Max end,
    max_rotate(N, Tuple, Total, NewMax, Cur, K + 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_rotate_function(nums :: [integer]) :: integer
  def max_rotate_function(nums) do
    n = length(nums)
    total = Enum.sum(nums)

    f0 =
      nums
      |> Enum.with_index()
      |> Enum.reduce(0, fn {val, idx}, acc -> acc + idx * val end)

    if n == 1 do
      f0
    else
      tuple = List.to_tuple(nums)

      {max_val, _} =
        Enum.reduce(1..(n - 1), {f0, f0}, fn i, {cur_max, prev_f} ->
          moved = elem(tuple, n - i)
          new_f = prev_f + total - n * moved
          new_max = if new_f > cur_max, do: new_f, else: cur_max
          {new_max, new_f}
        end)

      max_val
    end
  end
end
```
