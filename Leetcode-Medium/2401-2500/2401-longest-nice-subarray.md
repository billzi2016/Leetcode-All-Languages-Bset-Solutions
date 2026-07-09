# 2401. Longest Nice Subarray

## Cpp

```cpp
class Solution {
public:
    int longestNiceSubarray(vector<int>& nums) {
        int n = nums.size();
        int left = 0;
        int usedBits = 0;
        int best = 0;
        for (int right = 0; right < n; ++right) {
            while ((usedBits & nums[right]) != 0) {
                usedBits ^= nums[left];
                ++left;
            }
            usedBits |= nums[right];
            best = max(best, right - left + 1);
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public int longestNiceSubarray(int[] nums) {
        int usedBits = 0;
        int left = 0;
        int maxLen = 0;
        for (int right = 0; right < nums.length; right++) {
            while ((usedBits & nums[right]) != 0) {
                usedBits ^= nums[left];
                left++;
            }
            usedBits |= nums[right];
            maxLen = Math.max(maxLen, right - left + 1);
        }
        return maxLen;
    }
}
```

## Python

```python
class Solution(object):
    def longestNiceSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        used = 0
        left = 0
        max_len = 0
        for right, val in enumerate(nums):
            while (used & val) != 0:
                used ^= nums[left]
                left += 1
            used |= val
            cur_len = right - left + 1
            if cur_len > max_len:
                max_len = cur_len
        return max_len
```

## Python3

```python
from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        used = 0
        left = 0
        max_len = 0
        for right, val in enumerate(nums):
            while (used & val) != 0:
                used ^= nums[left]
                left += 1
            used |= val
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
        return max_len
```

## C

```c
int longestNiceSubarray(int* nums, int numsSize) {
    unsigned int used = 0;
    int left = 0, maxLen = 0;
    for (int right = 0; right < numsSize; ++right) {
        while ((used & (unsigned int)nums[right]) != 0) {
            used ^= (unsigned int)nums[left];
            ++left;
        }
        used |= (unsigned int)nums[right];
        int curLen = right - left + 1;
        if (curLen > maxLen) maxLen = curLen;
    }
    return maxLen;
}
```

## Csharp

```csharp
public class Solution
{
    public int LongestNiceSubarray(int[] nums)
    {
        int left = 0;
        int mask = 0;
        int maxLen = 0;

        for (int right = 0; right < nums.Length; ++right)
        {
            while ((mask & nums[right]) != 0)
            {
                mask ^= nums[left];
                left++;
            }

            mask |= nums[right];
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
 * @return {number}
 */
var longestNiceSubarray = function(nums) {
    let left = 0;
    let mask = 0; // bits used in current window
    let maxLen = 0;
    
    for (let right = 0; right < nums.length; ++right) {
        while ((mask & nums[right]) !== 0) {
            // remove leftmost element's bits
            mask ^= nums[left];
            left++;
        }
        mask |= nums[right];
        maxLen = Math.max(maxLen, right - left + 1);
    }
    
    return maxLen;
};
```

## Typescript

```typescript
function longestNiceSubarray(nums: number[]): number {
    let usedBits = 0;
    let left = 0;
    let maxLen = 0;
    for (let right = 0; right < nums.length; ++right) {
        while ((usedBits & nums[right]) !== 0) {
            usedBits ^= nums[left];
            left++;
        }
        usedBits |= nums[right];
        const curLen = right - left + 1;
        if (curLen > maxLen) maxLen = curLen;
    }
    return maxLen;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function longestNiceSubarray($nums) {
        $n = count($nums);
        $usedBits = 0;
        $left = 0;
        $maxLen = 0;

        for ($right = 0; $right < $n; $right++) {
            while (($usedBits & $nums[$right]) != 0) {
                // remove leftmost element's bits
                $usedBits ^= $nums[$left];
                $left++;
            }
            $usedBits |= $nums[$right];
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
    func longestNiceSubarray(_ nums: [Int]) -> Int {
        var usedBits = 0
        var left = 0
        var maxLength = 0
        
        for right in 0..<nums.count {
            let current = nums[right]
            while (usedBits & current) != 0 {
                usedBits ^= nums[left]
                left += 1
            }
            usedBits |= current
            maxLength = max(maxLength, right - left + 1)
        }
        
        return maxLength
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestNiceSubarray(nums: IntArray): Int {
        var mask = 0
        var left = 0
        var maxLen = 0
        for (right in nums.indices) {
            while ((mask and nums[right]) != 0) {
                mask = mask xor nums[left]
                left++
            }
            mask = mask or nums[right]
            val curLen = right - left + 1
            if (curLen > maxLen) maxLen = curLen
        }
        return maxLen
    }
}
```

## Dart

```dart
class Solution {
  int longestNiceSubarray(List<int> nums) {
    int usedBits = 0;
    int left = 0;
    int maxLen = 0;

    for (int right = 0; right < nums.length; right++) {
      while ((usedBits & nums[right]) != 0) {
        usedBits ^= nums[left];
        left++;
      }
      usedBits |= nums[right];
      int currentLen = right - left + 1;
      if (currentLen > maxLen) {
        maxLen = currentLen;
      }
    }

    return maxLen;
  }
}
```

## Golang

```go
func longestNiceSubarray(nums []int) int {
    left, usedBits, maxLen := 0, 0, 0
    for right, val := range nums {
        // shrink window until no overlapping bits with current value
        for (usedBits & val) != 0 {
            usedBits ^= nums[left]
            left++
        }
        usedBits |= val
        if curLen := right - left + 1; curLen > maxLen {
            maxLen = curLen
        }
    }
    return maxLen
}
```

## Ruby

```ruby
def longest_nice_subarray(nums)
  used = 0
  left = 0
  max_len = 0
  nums.each_with_index do |num, right|
    while (used & num) != 0
      used ^= nums[left]
      left += 1
    end
    used |= num
    cur_len = right - left + 1
    max_len = cur_len if cur_len > max_len
  end
  max_len
end
```

## Scala

```scala
object Solution {
    def longestNiceSubarray(nums: Array[Int]): Int = {
        var usedBits = 0
        var left = 0
        var maxLen = 0
        for (right <- nums.indices) {
            while ((usedBits & nums(right)) != 0) {
                usedBits ^= nums(left)
                left += 1
            }
            usedBits |= nums(right)
            val curLen = right - left + 1
            if (curLen > maxLen) maxLen = curLen
        }
        maxLen
    }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_nice_subarray(nums: Vec<i32>) -> i32 {
        let mut used: i32 = 0;
        let mut left: usize = 0;
        let mut max_len: usize = 0;

        for (right, &val) in nums.iter().enumerate() {
            while (used & val) != 0 {
                used ^= nums[left];
                left += 1;
            }
            used |= val;
            let cur_len = right - left + 1;
            if cur_len > max_len {
                max_len = cur_len;
            }
        }

        max_len as i32
    }
}
```

## Racket

```racket
(define/contract (longest-nice-subarray nums)
  (-> (listof exact-integer?) exact-integer?)
  (if (null? nums)
      0
      (let* ((v (list->vector nums))
             (n (vector-length v)))
        (let loop ((i 0) (l 0) (used 0) (ans 0))
          (if (= i n)
              ans
              (let* ((cur (vector-ref v i))
                     (shrink
                       (let recur ((u used) (ll l))
                         (if (= (bitwise-and u cur) 0)
                             (values u ll)
                             (recur (bitwise-xor u (vector-ref v ll)) (+ ll 1)))))
                     )
                (let-values ([(u ll) shrink])
                  (let ((new-used (bitwise-ior u cur))
                        (new-ans (max ans (+ (- i ll) 1))))
                    (loop (+ i 1) ll new-used new-ans))))))))))
```

## Erlang

```erlang
-export([longest_nice_subarray/1]).

-spec longest_nice_subarray(Nums :: [integer()]) -> integer().
longest_nice_subarray(Nums) ->
    loop(Nums, [], 0, 0).

loop([], _Queue, _Used, Max) ->
    Max;
loop([X | Rest], Queue, Used, Max) ->
    case (Used band X) of
        0 ->
            NewUsed = Used bor X,
            NewQueue = Queue ++ [X],
            NewMax = max(Max, length(NewQueue)),
            loop(Rest, NewQueue, NewUsed, NewMax);
        _ ->
            {ShrunkQueue, ShrunkUsed} = shrink(Queue, Used, X),
            NewUsed2 = ShrunkUsed bor X,
            NewQueue2 = ShrunkQueue ++ [X],
            NewMax2 = max(Max, length(NewQueue2)),
            loop(Rest, NewQueue2, NewUsed2, NewMax2)
    end.

shrink([], Used, _X) ->
    {[], Used};
shrink([H | T], Used, X) ->
    case (Used band X) of
        0 -> {[H | T], Used};
        _ ->
            NewUsed = Used bxor H,
            shrink(T, NewUsed, X)
    end.
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec longest_nice_subarray(nums :: [integer]) :: integer
  def longest_nice_subarray(nums) do
    n = length(nums)
    tup = List.to_tuple(nums)

    {_, _, max_len} =
      0..(n - 1)
      |> Enum.reduce({0, 0, 0}, fn right, {left, used, max_len} ->
        num = elem(tup, right)

        {new_left, new_used} =
          if (used &&& num) == 0 do
            {left, used}
          else
            shrink_conflict(left, used, tup, num)
          end

        new_used2 = new_used ||| num
        new_max = max(max_len, right - new_left + 1)
        {new_left, new_used2, new_max}
      end)

    max_len
  end

  defp shrink_conflict(left, used, tup, num) do
    if (used &&& num) == 0 do
      {left, used}
    else
      left_num = elem(tup, left)
      shrink_conflict(left + 1, used ^^^ left_num, tup, num)
    end
  end
end
```
