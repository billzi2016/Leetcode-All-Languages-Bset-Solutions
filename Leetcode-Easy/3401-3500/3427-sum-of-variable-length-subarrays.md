# 3427. Sum of Variable Length Subarrays

## Cpp

```cpp
class Solution {
public:
    int subarraySum(vector<int>& nums) {
        int n = nums.size();
        vector<long long> pref(n + 1, 0);
        for (int i = 0; i < n; ++i) pref[i + 1] = pref[i] + nums[i];
        long long total = 0;
        for (int i = 0; i < n; ++i) {
            int start = i - nums[i];
            if (start < 0) start = 0;
            total += pref[i + 1] - pref[start];
        }
        return static_cast<int>(total);
    }
};
```

## Java

```java
class Solution {
    public int subarraySum(int[] nums) {
        int n = nums.length;
        int[] prefix = new int[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + nums[i];
        }
        int total = 0;
        for (int i = 0; i < n; i++) {
            int start = i - nums[i];
            if (start < 0) start = 0;
            total += prefix[i + 1] - prefix[start];
        }
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def subarraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        total = 0
        for i, val in enumerate(nums):
            start = i - val
            if start < 0:
                start = 0
            total += prefix[i + 1] - prefix[start]
        return total
```

## Python3

```python
from typing import List

class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        total = 0
        for i, val in enumerate(nums):
            start = i - val
            if start < 0:
                start = 0
            total += prefix[i + 1] - prefix[start]
        return total
```

## C

```c
int subarraySum(int* nums, int numsSize) {
    int prefix[101] = {0};
    for (int i = 0; i < numsSize; ++i) {
        prefix[i + 1] = prefix[i] + nums[i];
    }
    int total = 0;
    for (int i = 0; i < numsSize; ++i) {
        int start = i - nums[i];
        if (start < 0) start = 0;
        total += prefix[i + 1] - prefix[start];
    }
    return total;
}
```

## Csharp

```csharp
public class Solution
{
    public int SubarraySum(int[] nums)
    {
        int n = nums.Length;
        int[] prefix = new int[n + 1];
        for (int i = 0; i < n; i++)
        {
            prefix[i + 1] = prefix[i] + nums[i];
        }

        long total = 0;
        for (int i = 0; i < n; i++)
        {
            int start = i - nums[i];
            if (start < 0) start = 0;
            total += prefix[i + 1] - prefix[start];
        }
        return (int)total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var subarraySum = function(nums) {
    const n = nums.length;
    const prefix = new Array(n + 1);
    prefix[0] = 0;
    for (let i = 0; i < n; ++i) {
        prefix[i + 1] = prefix[i] + nums[i];
    }
    let total = 0;
    for (let i = 0; i < n; ++i) {
        const start = Math.max(0, i - nums[i]);
        total += prefix[i + 1] - prefix[start];
    }
    return total;
};
```

## Typescript

```typescript
function subarraySum(nums: number[]): number {
    const n = nums.length;
    const prefix: number[] = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        prefix[i + 1] = prefix[i] + nums[i];
    }
    let total = 0;
    for (let i = 0; i < n; i++) {
        const start = Math.max(0, i - nums[i]);
        total += prefix[i + 1] - prefix[start];
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function subarraySum($nums) {
        $n = count($nums);
        if ($n == 0) return 0;
        $prefix = [];
        for ($i = 0; $i < $n; $i++) {
            $prefix[$i] = $i == 0 ? $nums[0] : $prefix[$i - 1] + $nums[$i];
        }
        $total = 0;
        for ($i = 0; $i < $n; $i++) {
            $start = max(0, $i - $nums[$i]);
            if ($start == 0) {
                $subSum = $prefix[$i];
            } else {
                $subSum = $prefix[$i] - $prefix[$start - 1];
            }
            $total += $subSum;
        }
        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func subarraySum(_ nums: [Int]) -> Int {
        let n = nums.count
        var prefix = [Int](repeating: 0, count: n + 1)
        for i in 0..<n {
            prefix[i + 1] = prefix[i] + nums[i]
        }
        var total = 0
        for i in 0..<n {
            let start = max(0, i - nums[i])
            total += prefix[i + 1] - prefix[start]
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun subarraySum(nums: IntArray): Int {
        val n = nums.size
        val prefix = IntArray(n + 1)
        for (i in 0 until n) {
            prefix[i + 1] = prefix[i] + nums[i]
        }
        var total = 0
        for (i in 0 until n) {
            val start = kotlin.math.max(0, i - nums[i])
            total += prefix[i + 1] - prefix[start]
        }
        return total
    }
}
```

## Dart

```dart
class Solution {
  int subarraySum(List<int> nums) {
    int n = nums.length;
    List<int> prefix = List.filled(n + 1, 0);
    for (int i = 0; i < n; i++) {
      prefix[i + 1] = prefix[i] + nums[i];
    }
    int total = 0;
    for (int i = 0; i < n; i++) {
      int start = i - nums[i];
      if (start < 0) start = 0;
      total += prefix[i + 1] - prefix[start];
    }
    return total;
  }
}
```

## Golang

```go
func subarraySum(nums []int) int {
    total := 0
    n := len(nums)
    for i := 0; i < n; i++ {
        start := i - nums[i]
        if start < 0 {
            start = 0
        }
        for j := start; j <= i; j++ {
            total += nums[j]
        }
    }
    return total
}
```

## Ruby

```ruby
def subarray_sum(nums)
  n = nums.length
  prefix = Array.new(n + 1, 0)
  (0...n).each { |i| prefix[i + 1] = prefix[i] + nums[i] }
  total = 0
  (0...n).each do |i|
    start = i - nums[i]
    start = 0 if start < 0
    total += prefix[i + 1] - prefix[start]
  end
  total
end
```

## Scala

```scala
object Solution {
    def subarraySum(nums: Array[Int]): Int = {
        val n = nums.length
        val pref = new Array[Long](n + 1)
        for (i <- 0 until n) {
            pref(i + 1) = pref(i) + nums(i)
        }
        var total: Long = 0L
        for (i <- 0 until n) {
            val start = math.max(0, i - nums(i))
            total += pref(i + 1) - pref(start)
        }
        total.toInt
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn subarray_sum(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut pref = vec![0i64; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + nums[i] as i64;
        }
        let mut ans: i64 = 0;
        for i in 0..n {
            let len = nums[i] as usize;
            let start = if i >= len { i - len } else { 0 };
            ans += pref[i + 1] - pref[start];
        }
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (subarray-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (vec (list->vector nums))
         (pref (make-vector (+ n 1) 0)))
    (for ([i (in-range n)])
      (vector-set! pref (+ i 1)
                   (+ (vector-ref pref i) (vector-ref vec i))))
    (let loop ((i 0) (total 0))
      (if (= i n)
          total
          (let* ((val (vector-ref vec i))
                 (start (max 0 (- i val)))
                 (subsum (- (vector-ref pref (+ i 1))
                            (vector-ref pref start))))
            (loop (+ i 1) (+ total subsum)))))))
```

## Erlang

```erlang
-module(solution).
-export([subarray_sum/1]).

-spec subarray_sum(Nums :: [integer()]) -> integer().
subarray_sum(Nums) ->
    {Total,_} = lists:foldl(fun({Val,Idx}, {SumAcc,_}) ->
        Start = max(0, Idx - Val),
        SubSum = sum_range(Nums, Start, Idx),
        {SumAcc + SubSum, nil}
    end, {0, nil}, zip_with_index(Nums)),
    Total.

zip_with_index(Nums) ->
    Indices = lists:seq(0, length(Nums)-1),
    lists:zip(Nums, Indices).

sum_range(List, Start, End) ->
    sum_range(List, Start, End, 0).

sum_range(_List, I, End, Acc) when I > End -> Acc;
sum_range(List, I, End, Acc) ->
    Val = lists:nth(I+1, List),
    sum_range(List, I+1, End, Acc + Val).
```

## Elixir

```elixir
defmodule Solution do
  @spec subarray_sum(nums :: [integer]) :: integer
  def subarray_sum(nums) do
    pref = [0 | Enum.scan(nums, fn x, acc -> x + acc end)]

    Enum.with_index(nums)
    |> Enum.reduce(0, fn {val, i}, total ->
      start = max(0, i - val)
      sum_i = Enum.at(pref, i + 1) - Enum.at(pref, start)
      total + sum_i
    end)
  end
end
```
