# 1004. Max Consecutive Ones III

## Cpp

```cpp
class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int left = 0, zeroCount = 0, maxLen = 0;
        for (int right = 0; right < (int)nums.size(); ++right) {
            if (nums[right] == 0) ++zeroCount;
            while (zeroCount > k) {
                if (nums[left] == 0) --zeroCount;
                ++left;
            }
            maxLen = max(maxLen, right - left + 1);
        }
        return maxLen;
    }
};
```

## Java

```java
class Solution {
    public int longestOnes(int[] nums, int k) {
        int left = 0, zeroCount = 0, maxLen = 0;
        for (int right = 0; right < nums.length; right++) {
            if (nums[right] == 0) {
                zeroCount++;
            }
            while (zeroCount > k) {
                if (nums[left] == 0) {
                    zeroCount--;
                }
                left++;
            }
            maxLen = Math.max(maxLen, right - left + 1);
        }
        return maxLen;
    }
}
```

## Python

```python
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        zeros = 0
        max_len = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
```

## Python3

```python
from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zero_count = 0
        max_len = 0
        for right, val in enumerate(nums):
            if val == 0:
                zero_count += 1
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
        return max_len
```

## C

```c
int longestOnes(int* nums, int numsSize, int k) {
    int left = 0;
    int zeroCount = 0;
    int maxLen = 0;
    for (int right = 0; right < numsSize; ++right) {
        if (nums[right] == 0) {
            ++zeroCount;
        }
        while (zeroCount > k) {
            if (nums[left] == 0) {
                --zeroCount;
            }
            ++left;
        }
        int currentLen = right - left + 1;
        if (currentLen > maxLen) {
            maxLen = currentLen;
        }
    }
    return maxLen;
}
```

## Csharp

```csharp
public class Solution
{
    public int LongestOnes(int[] nums, int k)
    {
        int left = 0, zeroCount = 0, maxLen = 0;
        for (int right = 0; right < nums.Length; right++)
        {
            if (nums[right] == 0) zeroCount++;

            while (zeroCount > k)
            {
                if (nums[left] == 0) zeroCount--;
                left++;
            }

            int currentLen = right - left + 1;
            if (currentLen > maxLen) maxLen = currentLen;
        }
        return maxLen;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var longestOnes = function(nums, k) {
    let left = 0, zeros = 0, maxLen = 0;
    for (let right = 0; right < nums.length; ++right) {
        if (nums[right] === 0) zeros++;
        while (zeros > k) {
            if (nums[left] === 0) zeros--;
            left++;
        }
        const len = right - left + 1;
        if (len > maxLen) maxLen = len;
    }
    return maxLen;
};
```

## Typescript

```typescript
function longestOnes(nums: number[], k: number): number {
    let left = 0;
    let zeroCount = 0;
    let maxLen = 0;
    for (let right = 0; right < nums.length; right++) {
        if (nums[right] === 0) zeroCount++;
        while (zeroCount > k) {
            if (nums[left] === 0) zeroCount--;
            left++;
        }
        const currentLen = right - left + 1;
        if (currentLen > maxLen) maxLen = currentLen;
    }
    return maxLen;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function longestOnes($nums, $k) {
        $left = 0;
        $zeroCount = 0;
        $maxLen = 0;
        $n = count($nums);
        for ($right = 0; $right < $n; $right++) {
            if ($nums[$right] == 0) {
                $zeroCount++;
            }
            while ($zeroCount > $k) {
                if ($nums[$left] == 0) {
                    $zeroCount--;
                }
                $left++;
            }
            $currentLen = $right - $left + 1;
            if ($currentLen > $maxLen) {
                $maxLen = $currentLen;
            }
        }
        return $maxLen;
    }
}
```

## Swift

```swift
class Solution {
    func longestOnes(_ nums: [Int], _ k: Int) -> Int {
        var left = 0
        var zeroCount = 0
        var maxLength = 0
        
        for right in 0..<nums.count {
            if nums[right] == 0 {
                zeroCount += 1
            }
            
            while zeroCount > k {
                if nums[left] == 0 {
                    zeroCount -= 1
                }
                left += 1
            }
            
            let currentLength = right - left + 1
            if currentLength > maxLength {
                maxLength = currentLength
            }
        }
        
        return maxLength
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestOnes(nums: IntArray, k: Int): Int {
        var left = 0
        var zeroCount = 0
        var maxLen = 0
        for (right in nums.indices) {
            if (nums[right] == 0) zeroCount++
            while (zeroCount > k) {
                if (nums[left] == 0) zeroCount--
                left++
            }
            val currentLen = right - left + 1
            if (currentLen > maxLen) maxLen = currentLen
        }
        return maxLen
    }
}
```

## Dart

```dart
class Solution {
  int longestOnes(List<int> nums, int k) {
    int left = 0;
    int zeroCount = 0;
    int maxLen = 0;
    for (int right = 0; right < nums.length; right++) {
      if (nums[right] == 0) zeroCount++;
      while (zeroCount > k) {
        if (nums[left] == 0) zeroCount--;
        left++;
      }
      int currentLen = right - left + 1;
      if (currentLen > maxLen) maxLen = currentLen;
    }
    return maxLen;
  }
}
```

## Golang

```go
func longestOnes(nums []int, k int) int {
    left, zeros, maxLen := 0, 0, 0
    for right, v := range nums {
        if v == 0 {
            zeros++
        }
        for zeros > k {
            if nums[left] == 0 {
                zeros--
            }
            left++
        }
        if cur := right - left + 1; cur > maxLen {
            maxLen = cur
        }
    }
    return maxLen
}
```

## Ruby

```ruby
def longest_ones(nums, k)
  left = 0
  zero_count = 0
  max_len = 0
  nums.each_with_index do |num, right|
    zero_count += 1 if num == 0
    while zero_count > k
      zero_count -= 1 if nums[left] == 0
      left += 1
    end
    cur_len = right - left + 1
    max_len = cur_len if cur_len > max_len
  end
  max_len
end
```

## Scala

```scala
object Solution {
    def longestOnes(nums: Array[Int], k: Int): Int = {
        var left = 0
        var zeroCount = 0
        var maxLen = 0
        for (right <- nums.indices) {
            if (nums(right) == 0) zeroCount += 1
            while (zeroCount > k) {
                if (nums(left) == 0) zeroCount -= 1
                left += 1
            }
            val windowLen = right - left + 1
            if (windowLen > maxLen) maxLen = windowLen
        }
        maxLen
    }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_ones(nums: Vec<i32>, k: i32) -> i32 {
        let mut left = 0usize;
        let mut zero_cnt = 0i32;
        let mut max_len = 0i32;

        for right in 0..nums.len() {
            if nums[right] == 0 {
                zero_cnt += 1;
            }
            while zero_cnt > k {
                if nums[left] == 0 {
                    zero_cnt -= 1;
                }
                left += 1;
            }
            let cur_len = (right - left + 1) as i32;
            if cur_len > max_len {
                max_len = cur_len;
            }
        }

        max_len
    }
}
```

## Racket

```racket
(define/contract (longest-ones nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([v (list->vector nums)]
         [n (vector-length v)])
    (let loop ((right 0) (left 0) (zero-count 0) (max-len 0))
      (if (= right n)
          max-len
          (let* ([is-zero (if (= (vector-ref v right) 0) 1 0)]
                 [new-zero (+ zero-count is-zero)])
            (let-values ([(new-left new-zero2)
                          (let shrink ((l left) (zc new-zero))
                            (if (> zc k)
                                (shrink (+ l 1)
                                        (- zc (if (= (vector-ref v l) 0) 1 0)))
                                (values l zc)))])
              (let ((new-max (max max-len (+ 1 (- right new-left)))))
                (loop (+ right 1) new-left new-zero2 new-max)))))))))
```

## Erlang

```erlang
-module(solution).
-export([longest_ones/2]).

-spec longest_ones(Nums :: [integer()], K :: integer()) -> integer().
longest_ones(Nums, K) ->
    loop(Nums, 0, 0, 0, {[], []}, 0, K).

loop([], _Idx, _Left, MaxLen, _Queue, _ZeroCnt, _K) ->
    MaxLen;
loop([H|T], I, Left, MaxLen, Queue, ZeroCnt, K) ->
    case H of
        0 ->
            Q1 = queue_push_back(Queue, I),
            Z1 = ZeroCnt + 1;
        _ ->
            Q1 = Queue,
            Z1 = ZeroCnt
    end,
    {NewLeft, NewZeroCnt, NewQueue} =
        if Z1 > K ->
                {OldIdx, Q2} = queue_pop_front(Q1),
                {OldIdx + 1, Z1 - 1, Q2};
           true ->
                {Left, Z1, Q1}
        end,
    CurrLen = I - NewLeft + 1,
    MaxLen1 = erlang:max(MaxLen, CurrLen),
    loop(T, I + 1, NewLeft, MaxLen1, NewQueue, NewZeroCnt, K).

queue_push_back({F,B}, X) ->
    {F, [X|B]}.

queue_pop_front({[H|T], B}) ->
    {H, {T, B}};
queue_pop_front({[], B}) when B =/= [] ->
    Front = lists:reverse(B),
    queue_pop_front({Front, []});
queue_pop_front({[], []}) ->
    erlang:error(empty).
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_ones(nums :: [integer], k :: integer) :: integer
  def longest_ones(nums, k) do
    {_queue, _zero_cnt, max_len} =
      Enum.reduce(nums, {:queue.new(), 0, 0}, fn num, {q, zero_cnt, max_len} ->
        q = :queue.in(num, q)
        zero_cnt = if num == 0, do: zero_cnt + 1, else: zero_cnt

        {q, zero_cnt} = adjust_window(q, zero_cnt, k)

        size = :queue.len(q)
        max_len = if size > max_len, do: size, else: max_len
        {q, zero_cnt, max_len}
      end)

    max_len
  end

  defp adjust_window(q, zero_cnt, k) when zero_cnt <= k, do: {q, zero_cnt}

  defp adjust_window(q, zero_cnt, k) do
    {{:value, val}, q2} = :queue.out(q)
    zero_cnt = if val == 0, do: zero_cnt - 1, else: zero_cnt
    adjust_window(q2, zero_cnt, k)
  end
end
```
