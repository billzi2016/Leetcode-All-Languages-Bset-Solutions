# 0209. Minimum Size Subarray Sum

## Cpp

```cpp
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int n = nums.size();
        int left = 0;
        long long sum = 0;
        int ans = n + 1;
        for (int right = 0; right < n; ++right) {
            sum += nums[right];
            while (sum >= target) {
                ans = min(ans, right - left + 1);
                sum -= nums[left++];
            }
        }
        return ans == n + 1 ? 0 : ans;
    }
};
```

## Java

```java
class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int n = nums.length;
        int left = 0;
        long sum = 0;
        int minLen = Integer.MAX_VALUE;
        for (int right = 0; right < n; right++) {
            sum += nums[right];
            while (sum >= target) {
                minLen = Math.min(minLen, right - left + 1);
                sum -= nums[left++];
            }
        }
        return minLen == Integer.MAX_VALUE ? 0 : minLen;
    }
}
```

## Python

```python
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = 0
        cur_sum = 0
        res = n + 1  # larger than any possible length
        
        for right in range(n):
            cur_sum += nums[right]
            while cur_sum >= target:
                res = min(res, right - left + 1)
                cur_sum -= nums[left]
                left += 1
                
        return 0 if res == n + 1 else res
```

## Python3

```python
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        cur_sum = 0
        best = n + 1
        for right in range(n):
            cur_sum += nums[right]
            while cur_sum >= target:
                best = min(best, right - left + 1)
                cur_sum -= nums[left]
                left += 1
        return 0 if best == n + 1 else best
```

## C

```c
int minSubArrayLen(int target, int* nums, int numsSize) {
    int left = 0;
    long long sum = 0;
    int res = numsSize + 1;
    for (int right = 0; right < numsSize; ++right) {
        sum += nums[right];
        while (sum >= target) {
            int len = right - left + 1;
            if (len < res) res = len;
            sum -= nums[left++];
        }
    }
    return (res == numsSize + 1) ? 0 : res;
}
```

## Csharp

```csharp
public class Solution {
    public int MinSubArrayLen(int target, int[] nums) {
        int n = nums.Length;
        int left = 0;
        int sum = 0;
        int minLen = int.MaxValue;

        for (int right = 0; right < n; right++) {
            sum += nums[right];
            while (sum >= target) {
                int currentLen = right - left + 1;
                if (currentLen < minLen) minLen = currentLen;
                sum -= nums[left];
                left++;
            }
        }

        return minLen == int.MaxValue ? 0 : minLen;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(target, nums) {
    let left = 0;
    let sum = 0;
    let res = Infinity;
    
    for (let right = 0; right < nums.length; right++) {
        sum += nums[right];
        while (sum >= target) {
            res = Math.min(res, right - left + 1);
            sum -= nums[left];
            left++;
        }
    }
    
    return res === Infinity ? 0 : res;
};
```

## Typescript

```typescript
function minSubArrayLen(target: number, nums: number[]): number {
    let left = 0;
    let sum = 0;
    let minLen = Infinity;
    for (let right = 0; right < nums.length; right++) {
        sum += nums[right];
        while (sum >= target) {
            const len = right - left + 1;
            if (len < minLen) minLen = len;
            sum -= nums[left];
            left++;
        }
    }
    return minLen === Infinity ? 0 : minLen;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $target
     * @param Integer[] $nums
     * @return Integer
     */
    function minSubArrayLen($target, $nums) {
        $n = count($nums);
        $left = 0;
        $sum = 0;
        $res = $n + 1; // sentinel larger than any possible length

        for ($right = 0; $right < $n; $right++) {
            $sum += $nums[$right];

            while ($sum >= $target) {
                $len = $right - $left + 1;
                if ($len < $res) {
                    $res = $len;
                }
                $sum -= $nums[$left];
                $left++;
            }
        }

        return $res === $n + 1 ? 0 : $res;
    }
}
```

## Swift

```swift
class Solution {
    func minSubArrayLen(_ target: Int, _ nums: [Int]) -> Int {
        var left = 0
        var sum = 0
        var result = Int.max
        
        for right in 0..<nums.count {
            sum += nums[right]
            while sum >= target {
                let length = right - left + 1
                if length < result { result = length }
                sum -= nums[left]
                left += 1
            }
        }
        
        return result == Int.max ? 0 : result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minSubArrayLen(target: Int, nums: IntArray): Int {
        var left = 0
        var sum = 0L
        var result = Int.MAX_VALUE
        for (right in nums.indices) {
            sum += nums[right].toLong()
            while (sum >= target) {
                val length = right - left + 1
                if (length < result) result = length
                sum -= nums[left].toLong()
                left++
            }
        }
        return if (result == Int.MAX_VALUE) 0 else result
    }
}
```

## Dart

```dart
class Solution {
  int minSubArrayLen(int target, List<int> nums) {
    int n = nums.length;
    int left = 0;
    int sum = 0;
    int res = n + 1;

    for (int right = 0; right < n; right++) {
      sum += nums[right];
      while (sum >= target) {
        int currentLen = right - left + 1;
        if (currentLen < res) res = currentLen;
        sum -= nums[left];
        left++;
      }
    }

    return res == n + 1 ? 0 : res;
  }
}
```

## Golang

```go
func minSubArrayLen(target int, nums []int) int {
    n := len(nums)
    left, sum := 0, 0
    res := n + 1
    for right, v := range nums {
        sum += v
        for sum >= target {
            if length := right - left + 1; length < res {
                res = length
            }
            sum -= nums[left]
            left++
        }
    }
    if res == n+1 {
        return 0
    }
    return res
}
```

## Ruby

```ruby
def min_sub_array_len(target, nums)
  left = 0
  sum = 0
  best = Float::INFINITY
  nums.each_with_index do |num, right|
    sum += num
    while sum >= target
      length = right - left + 1
      best = length if length < best
      sum -= nums[left]
      left += 1
    end
  end
  best == Float::INFINITY ? 0 : best
end
```

## Scala

```scala
object Solution {
    def minSubArrayLen(target: Int, nums: Array[Int]): Int = {
        var left = 0
        var sum: Long = 0L
        var minLen = Int.MaxValue

        for (right <- nums.indices) {
            sum += nums(right)
            while (sum >= target) {
                val len = right - left + 1
                if (len < minLen) minLen = len
                sum -= nums(left)
                left += 1
            }
        }

        if (minLen == Int.MaxValue) 0 else minLen
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_sub_array_len(target: i32, nums: Vec<i32>) -> i32 {
        let mut left = 0usize;
        let mut sum: i64 = 0;
        let mut best = usize::MAX;
        let target_i64 = target as i64;

        for right in 0..nums.len() {
            sum += nums[right] as i64;
            while sum >= target_i64 {
                let len = right - left + 1;
                if len < best {
                    best = len;
                }
                sum -= nums[left] as i64;
                left += 1;
            }
        }

        if best == usize::MAX {
            0
        } else {
            best as i32
        }
    }
}
```

## Racket

```racket
(define/contract (min-sub-array-len target nums)
  (-> exact-integer? (listof exact-integer?) exact-integer?)
  (let* ((v (list->vector nums))
         (n (vector-length v)))
    (let ((left 0)
          (sum 0)
          (ans (+ n 1))) ; sentinel larger than any possible length
      (for ([right (in-range n)])
        (set! sum (+ sum (vector-ref v right)))
        (let loop ()
          (when (and (>= sum target) (< (+ (- right left) 1) ans))
            (set! ans (+ (- right left) 1))
            (set! sum (- sum (vector-ref v left)))
            (set! left (add1 left))
            (loop))))
      (if (= ans (+ n 1)) 0 ans))))
```

## Erlang

```erlang
-spec min_sub_array_len(Target :: integer(), Nums :: [integer()]) -> integer().
min_sub_array_len(Target, Nums) ->
    Tuple = list_to_tuple(Nums),
    Len = tuple_size(Tuple),
    loop(Tuple, Target, Len, 1, 1, 0, Len + 1).

loop(_Tuple, _Target, Len, Right, _Left, _Sum, Res) when Right > Len ->
    case Res of
        R when R =:= Len + 1 -> 0;
        _ -> Res
    end;
loop(Tuple, Target, Len, Right, Left, Sum, Res) ->
    NewSum = Sum + element(Right, Tuple),
    {NewLeft, NewSum2, NewRes} = shrink(Target, Tuple, Right, Left, NewSum, Res),
    loop(Tuple, Target, Len, Right + 1, NewLeft, NewSum2, NewRes).

shrink(Target, Tuple, Right, Left, Sum, Res) when Sum >= Target ->
    CurrLen = Right - Left + 1,
    UpdatedRes = if CurrLen < Res -> CurrLen; true -> Res end,
    NewSum = Sum - element(Left, Tuple),
    shrink(Target, Tuple, Right, Left + 1, NewSum, UpdatedRes);
shrink(_Target, _Tuple, _Right, Left, Sum, Res) ->
    {Left, Sum, Res}.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_sub_array_len(target :: integer, nums :: [integer]) :: integer
  def min_sub_array_len(target, nums) do
    max_len = length(nums) + 1

    init = %{
      queue: :queue.new(),
      sum: 0,
      len: 0,
      res: max_len
    }

    final =
      Enum.reduce(nums, init, fn v, acc ->
        sum = acc.sum + v
        queue = :queue.in(v, acc.queue)
        len = acc.len + 1

        {sum2, queue2, len2, res2} = shrink(sum, queue, len, acc.res, target)

        %{queue: queue2, sum: sum2, len: len2, res: res2}
      end)

    if final.res == max_len, do: 0, else: final.res
  end

  defp shrink(sum, queue, len, res, target) when sum >= target do
    new_res = min(res, len)
    {{:value, val}, q2} = :queue.out(queue)
    shrink(sum - val, q2, len - 1, new_res, target)
  end

  defp shrink(sum, queue, len, res, _target), do: {sum, queue, len, res}
end
```
