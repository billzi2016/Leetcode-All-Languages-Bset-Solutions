# 1658. Minimum Operations to Reduce X to Zero

## Cpp

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        long long total = 0;
        for (int v : nums) total += v;
        long long target = total - x;
        if (target < 0) return -1;
        if (target == 0) return nums.size();
        int n = nums.size();
        int left = 0;
        long long cur = 0;
        int maxLen = -1;
        for (int right = 0; right < n; ++right) {
            cur += nums[right];
            while (left <= right && cur > target) {
                cur -= nums[left++];
            }
            if (cur == target) {
                maxLen = max(maxLen, right - left + 1);
            }
        }
        return maxLen == -1 ? -1 : n - maxLen;
    }
};
```

## Java

```java
class Solution {
    public int minOperations(int[] nums, int x) {
        int total = 0;
        for (int v : nums) total += v;
        int target = total - x;
        if (target < 0) return -1;
        if (target == 0) return nums.length;
        int maxLen = -1;
        int left = 0, cur = 0;
        for (int right = 0; right < nums.length; ++right) {
            cur += nums[right];
            while (cur > target && left <= right) {
                cur -= nums[left++];
            }
            if (cur == target) {
                maxLen = Math.max(maxLen, right - left + 1);
            }
        }
        return maxLen == -1 ? -1 : nums.length - maxLen;
    }
}
```

## Python

```python
class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        total = sum(nums)
        target = total - x
        if target < 0:
            return -1
        n = len(nums)
        # If we need to keep whole array (target == 0), remove all elements
        if target == 0:
            return n

        left = 0
        cur_sum = 0
        max_len = -1

        for right in range(n):
            cur_sum += nums[right]
            while cur_sum > target and left <= right:
                cur_sum -= nums[left]
                left += 1
            if cur_sum == target:
                max_len = max(max_len, right - left + 1)

        return n - max_len if max_len != -1 else -1
```

## Python3

```python
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total = sum(nums)
        target = total - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)

        max_len = -1
        cur_sum = 0
        left = 0

        for right, val in enumerate(nums):
            cur_sum += val
            while cur_sum > target and left <= right:
                cur_sum -= nums[left]
                left += 1
            if cur_sum == target:
                max_len = max(max_len, right - left + 1)

        return -1 if max_len == -1 else len(nums) - max_len
```

## C

```c
int minOperations(int* nums, int numsSize, int x) {
    long long total = 0;
    for (int i = 0; i < numsSize; ++i) total += nums[i];
    long long target = total - x;
    if (target < 0) return -1;
    if (target == 0) return numsSize;

    int left = 0;
    long long cur = 0;
    int maxLen = -1;

    for (int right = 0; right < numsSize; ++right) {
        cur += nums[right];
        while (cur > target && left <= right) {
            cur -= nums[left++];
        }
        if (cur == target) {
            int len = right - left + 1;
            if (len > maxLen) maxLen = len;
        }
    }

    return (maxLen == -1) ? -1 : (numsSize - maxLen);
}
```

## Csharp

```csharp
public class Solution {
    public int MinOperations(int[] nums, int x) {
        long total = 0;
        foreach (int num in nums) total += num;
        long target = total - x;
        if (target < 0) return -1;
        if (target == 0) return nums.Length;

        int n = nums.Length;
        int left = 0;
        long cur = 0;
        int maxLen = -1;

        for (int right = 0; right < n; right++) {
            cur += nums[right];
            while (cur > target && left <= right) {
                cur -= nums[left];
                left++;
            }
            if (cur == target) {
                int len = right - left + 1;
                if (len > maxLen) maxLen = len;
            }
        }

        return maxLen == -1 ? -1 : n - maxLen;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} x
 * @return {number}
 */
var minOperations = function(nums, x) {
    const n = nums.length;
    const total = nums.reduce((s, v) => s + v, 0);
    const target = total - x;
    if (target < 0) return -1;
    if (target === 0) return n; // need to remove all elements

    let left = 0;
    let cur = 0;
    let maxLen = -1;

    for (let right = 0; right < n; ++right) {
        cur += nums[right];
        while (cur > target && left <= right) {
            cur -= nums[left++];
        }
        if (cur === target) {
            const len = right - left + 1;
            if (len > maxLen) maxLen = len;
        }
    }

    return maxLen === -1 ? -1 : n - maxLen;
};
```

## Typescript

```typescript
function minOperations(nums: number[], x: number): number {
    const total = nums.reduce((a, b) => a + b, 0);
    if (total < x) return -1;
    const target = total - x;
    let maxLen = -1;
    let left = 0;
    let sum = 0;
    for (let right = 0; right < nums.length; right++) {
        sum += nums[right];
        while (sum > target && left <= right) {
            sum -= nums[left++];
        }
        if (sum === target) {
            const len = right - left + 1;
            if (len > maxLen) maxLen = len;
        }
    }
    return maxLen === -1 ? -1 : nums.length - maxLen;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $x
     * @return Integer
     */
    function minOperations($nums, $x) {
        $total = array_sum($nums);
        $target = $total - $x;
        if ($target < 0) {
            return -1;
        }
        $n = count($nums);
        if ($target == 0) {
            return $n;
        }

        $maxLen = -1;
        $left = 0;
        $curr = 0;

        for ($right = 0; $right < $n; $right++) {
            $curr += $nums[$right];
            while ($curr > $target && $left <= $right) {
                $curr -= $nums[$left];
                $left++;
            }
            if ($curr == $target) {
                $len = $right - $left + 1;
                if ($len > $maxLen) {
                    $maxLen = $len;
                }
            }
        }

        return $maxLen == -1 ? -1 : $n - $maxLen;
    }
}
```

## Swift

```swift
class Solution {
    func minOperations(_ nums: [Int], _ x: Int) -> Int {
        let total = nums.reduce(0, +)
        let target = total - x
        if target < 0 { return -1 }
        if target == 0 { return nums.count }
        
        var left = 0
        var sum = 0
        var maxLen = -1
        
        for right in 0..<nums.count {
            sum += nums[right]
            while sum > target && left <= right {
                sum -= nums[left]
                left += 1
            }
            if sum == target {
                let length = right - left + 1
                if length > maxLen {
                    maxLen = length
                }
            }
        }
        
        return maxLen == -1 ? -1 : nums.count - maxLen
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minOperations(nums: IntArray, x: Int): Int {
        var total = 0L
        for (v in nums) total += v
        val target = total - x
        if (target < 0) return -1
        if (target == 0L) return nums.size

        var left = 0
        var cur = 0L
        var maxLen = -1

        for (right in nums.indices) {
            cur += nums[right]
            while (cur > target && left <= right) {
                cur -= nums[left]
                left++
            }
            if (cur == target) {
                val len = right - left + 1
                if (len > maxLen) maxLen = len
            }
        }

        return if (maxLen != -1) nums.size - maxLen else -1
    }
}
```

## Dart

```dart
class Solution {
  int minOperations(List<int> nums, int x) {
    int total = 0;
    for (var v in nums) total += v;
    int target = total - x;
    if (target < 0) return -1;
    if (target == 0) return nums.length;

    int left = 0;
    int cur = 0;
    int maxLen = -1;

    for (int right = 0; right < nums.length; ++right) {
      cur += nums[right];
      while (cur > target && left <= right) {
        cur -= nums[left];
        left++;
      }
      if (cur == target) {
        int len = right - left + 1;
        if (len > maxLen) maxLen = len;
      }
    }

    return maxLen == -1 ? -1 : nums.length - maxLen;
  }
}
```

## Golang

```go
func minOperations(nums []int, x int) int {
    total := 0
    for _, v := range nums {
        total += v
    }
    target := total - x
    if target == 0 {
        return len(nums)
    }
    if target < 0 {
        return -1
    }

    maxLen := -1
    currSum := 0
    left := 0

    for right, v := range nums {
        currSum += v
        for currSum > target && left <= right {
            currSum -= nums[left]
            left++
        }
        if currSum == target {
            length := right - left + 1
            if length > maxLen {
                maxLen = length
            }
        }
    }

    if maxLen == -1 {
        return -1
    }
    return len(nums) - maxLen
}
```

## Ruby

```ruby
def min_operations(nums, x)
  total = nums.sum
  target = total - x
  return -1 if target < 0
  return nums.length if target == 0

  max_len = -1
  left = 0
  cur_sum = 0

  nums.each_with_index do |num, right|
    cur_sum += num
    while cur_sum > target && left <= right
      cur_sum -= nums[left]
      left += 1
    end
    if cur_sum == target
      max_len = [max_len, right - left + 1].max
    end
  end

  max_len == -1 ? -1 : nums.length - max_len
end
```

## Scala

```scala
object Solution {
    def minOperations(nums: Array[Int], x: Int): Int = {
        val n = nums.length
        var total: Long = 0L
        for (v <- nums) total += v.toLong

        val target = total - x.toLong
        if (target < 0) return -1
        if (target == 0) return n

        var left = 0
        var curSum: Long = 0L
        var maxLen = -1

        for (right <- 0 until n) {
            curSum += nums(right).toLong
            while (curSum > target && left <= right) {
                curSum -= nums(left).toLong
                left += 1
            }
            if (curSum == target) {
                val len = right - left + 1
                if (len > maxLen) maxLen = len
            }
        }

        if (maxLen == -1) -1 else n - maxLen
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_operations(nums: Vec<i32>, x: i32) -> i32 {
        let total: i64 = nums.iter().map(|&v| v as i64).sum();
        let target = total - x as i64;
        if target == 0 {
            return nums.len() as i32;
        }
        if target < 0 {
            return -1;
        }

        let mut left: usize = 0;
        let mut sum: i64 = 0;
        let mut max_len: i32 = -1;

        for right in 0..nums.len() {
            sum += nums[right] as i64;
            while sum > target && left <= right {
                sum -= nums[left] as i64;
                left += 1;
            }
            if sum == target {
                let len = (right - left + 1) as i32;
                if len > max_len {
                    max_len = len;
                }
            }
        }

        if max_len == -1 {
            -1
        } else {
            nums.len() as i32 - max_len
        }
    }
}
```

## Racket

```racket
#lang racket

(require racket/contract)

(define/contract (min-operations nums x)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length nums))
         (total (apply + nums))
         (target (- total x)))
    (cond
      [(= target 0) n]
      [(< target 0) -1]
      [else
       (let* ((vec (list->vector nums))
              (maxlen -1)
              (left 0)
              (sum 0))
         (for ([right (in-range n)])
           (set! sum (+ sum (vector-ref vec right)))
           (let-values ([(new-sum new-left)
                         (let loop ((s sum) (l left))
                           (if (and (> s target) (<= l right))
                               (loop (- s (vector-ref vec l)) (+ l 1))
                               (values s l)))])
             (set! sum new-sum)
             (set! left new-left))
           (when (= sum target)
             (let ((currlen (+ 1 (- right left))))
               (when (> currlen maxlen) (set! maxlen currlen)))))
         (if (= maxlen -1) -1 (- n maxlen)))])))
```

## Erlang

```erlang
-spec min_operations(Nums :: [integer()], X :: integer()) -> integer().
min_operations(Nums, X) ->
    Total = lists:sum(Nums),
    Target = Total - X,
    case Target of
        T when T < 0 ->
            -1;
        0 ->
            length(Nums);
        _ ->
            {_, _, _, MaxLen} = lists:foldl(
                fun(Val, {Idx, Sum, Map, MaxL}) ->
                    NewIdx = Idx + 1,
                    NewSum = Sum + Val,
                    PrevIdx = maps:get(NewSum - Target, Map, undefined),
                    NewMaxL = case PrevIdx of
                        undefined -> MaxL;
                        _ -> erlang:max(MaxL, NewIdx - PrevIdx)
                    end,
                    UpdatedMap = case maps:is_key(NewSum, Map) of
                        true -> Map;
                        false -> maps:put(NewSum, NewIdx, Map)
                    end,
                    {NewIdx, NewSum, UpdatedMap, NewMaxL}
                end,
                {0, 0, #{0 => 0}, 0},
                Nums),
            if MaxLen == 0 ->
                    -1;
               true ->
                    length(Nums) - MaxLen
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_operations(nums :: [integer], x :: integer) :: integer
  def min_operations(nums, x) do
    total = Enum.sum(nums)
    target = total - x
    n = length(nums)

    cond do
      target < 0 -> -1
      target == 0 -> n
      true ->
        {_, _, max_len} =
          Enum.with_index(nums)
          |> Enum.reduce({0, %{0 => -1}, nil}, fn {num, idx}, {cum, map, max_len} ->
            new_cum = cum + num
            needed = new_cum - target

            max_len =
              case Map.fetch(map, needed) do
                {:ok, start_idx} ->
                  len = idx - start_idx
                  case max_len do
                    nil -> len
                    _ when len > max_len -> len
                    _ -> max_len
                  end
                :error -> max_len
              end

            map = Map.put_new(map, new_cum, idx)
            {new_cum, map, max_len}
          end)

        case max_len do
          nil -> -1
          len -> n - len
        end
    end
  end
end
```
