# 3105. Longest Strictly Increasing or Strictly Decreasing Subarray

## Cpp

```cpp
class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {
        if (nums.empty()) return 0;
        int inc = 1, dec = 1, ans = 1;
        for (size_t i = 1; i < nums.size(); ++i) {
            if (nums[i] > nums[i - 1]) {
                ++inc;
                dec = 1;
            } else if (nums[i] < nums[i - 1]) {
                ++dec;
                inc = 1;
            } else {
                inc = dec = 1;
            }
            ans = max(ans, max(inc, dec));
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int longestMonotonicSubarray(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int inc = 1, dec = 1, max = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[i - 1]) {
                inc++;
                dec = 1;
            } else if (nums[i] < nums[i - 1]) {
                dec++;
                inc = 1;
            } else {
                inc = dec = 1;
            }
            max = Math.max(max, Math.max(inc, dec));
        }
        return max;
    }
}
```

## Python

```python
class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        inc = dec = max_len = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i - 1]:
                dec += 1
                inc = 1
            else:
                inc = dec = 1
            max_len = max(max_len, inc, dec)
        return max_len
```

## Python3

```python
from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        inc = dec = max_len = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i - 1]:
                dec += 1
                inc = 1
            else:
                inc = dec = 1
            max_len = max(max_len, inc, dec)
        return max_len
```

## C

```c
int longestMonotonicSubarray(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    int inc = 1, dec = 1, ans = 1;
    for (int i = 1; i < numsSize; ++i) {
        if (nums[i] > nums[i - 1]) {
            inc++;
            dec = 1;
        } else if (nums[i] < nums[i - 1]) {
            dec++;
            inc = 1;
        } else {
            inc = dec = 1;
        }
        if (inc > ans) ans = inc;
        if (dec > ans) ans = dec;
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int LongestMonotonicSubarray(int[] nums)
    {
        if (nums == null || nums.Length == 0) return 0;
        int inc = 1, dec = 1, maxLen = 1;
        for (int i = 1; i < nums.Length; i++)
        {
            if (nums[i] > nums[i - 1])
            {
                inc++;
                dec = 1;
            }
            else if (nums[i] < nums[i - 1])
            {
                dec++;
                inc = 1;
            }
            else
            {
                inc = dec = 1;
            }
            maxLen = Math.Max(maxLen, Math.Max(inc, dec));
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
var longestMonotonicSubarray = function(nums) {
    if (nums.length === 0) return 0;
    let inc = 1, dec = 1, maxLen = 1;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > nums[i - 1]) {
            inc += 1;
            dec = 1;
        } else if (nums[i] < nums[i - 1]) {
            dec += 1;
            inc = 1;
        } else {
            inc = dec = 1;
        }
        maxLen = Math.max(maxLen, inc, dec);
    }
    return maxLen;
};
```

## Typescript

```typescript
function longestMonotonicSubarray(nums: number[]): number {
    if (nums.length === 0) return 0;
    let inc = 1, dec = 1, maxLen = 1;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > nums[i - 1]) {
            inc++;
            dec = 1;
        } else if (nums[i] < nums[i - 1]) {
            dec++;
            inc = 1;
        } else {
            inc = dec = 1;
        }
        maxLen = Math.max(maxLen, inc, dec);
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
    function longestMonotonicSubarray($nums) {
        $n = count($nums);
        if ($n == 0) return 0;
        $inc = 1;
        $dec = 1;
        $max = 1;
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] > $nums[$i - 1]) {
                $inc++;
                $dec = 1;
            } elseif ($nums[$i] < $nums[$i - 1]) {
                $dec++;
                $inc = 1;
            } else {
                $inc = $dec = 1;
            }
            if ($inc > $max) $max = $inc;
            if ($dec > $max) $max = $dec;
        }
        return $max;
    }
}
```

## Swift

```swift
class Solution {
    func longestMonotonicSubarray(_ nums: [Int]) -> Int {
        guard !nums.isEmpty else { return 0 }
        var inc = 1
        var dec = 1
        var maxLen = 1
        for i in 1..<nums.count {
            if nums[i] > nums[i - 1] {
                inc += 1
                dec = 1
            } else if nums[i] < nums[i - 1] {
                dec += 1
                inc = 1
            } else {
                inc = 1
                dec = 1
            }
            maxLen = max(maxLen, inc)
            maxLen = max(maxLen, dec)
        }
        return maxLen
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestMonotonicSubarray(nums: IntArray): Int {
        if (nums.isEmpty()) return 0
        var inc = 1
        var dec = 1
        var maxLen = 1
        for (i in 1 until nums.size) {
            when {
                nums[i] > nums[i - 1] -> {
                    inc += 1
                    dec = 1
                }
                nums[i] < nums[i - 1] -> {
                    dec += 1
                    inc = 1
                }
                else -> {
                    inc = 1
                    dec = 1
                }
            }
            if (inc > maxLen) maxLen = inc
            if (dec > maxLen) maxLen = dec
        }
        return maxLen
    }
}
```

## Dart

```dart
class Solution {
  int longestMonotonicSubarray(List<int> nums) {
    if (nums.isEmpty) return 0;
    int inc = 1, dec = 1, maxLen = 1;
    for (int i = 1; i < nums.length; ++i) {
      if (nums[i] > nums[i - 1]) {
        inc += 1;
        dec = 1;
      } else if (nums[i] < nums[i - 1]) {
        dec += 1;
        inc = 1;
      } else {
        inc = dec = 1;
      }
      if (inc > maxLen) maxLen = inc;
      if (dec > maxLen) maxLen = dec;
    }
    return maxLen;
  }
}
```

## Golang

```go
func longestMonotonicSubarray(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	inc, dec, maxLen := 1, 1, 1
	for i := 1; i < len(nums); i++ {
		if nums[i] > nums[i-1] {
			inc++
			dec = 1
		} else if nums[i] < nums[i-1] {
			dec++
			inc = 1
		} else {
			inc, dec = 1, 1
		}
		if inc > maxLen {
			maxLen = inc
		}
		if dec > maxLen {
			maxLen = dec
		}
	}
	return maxLen
}
```

## Ruby

```ruby
def longest_monotonic_subarray(nums)
  return 0 if nums.empty?
  inc = dec = max_len = 1
  (1...nums.length).each do |i|
    if nums[i] > nums[i - 1]
      inc += 1
      dec = 1
    elsif nums[i] < nums[i - 1]
      dec += 1
      inc = 1
    else
      inc = dec = 1
    end
    max_len = [max_len, inc, dec].max
  end
  max_len
end
```

## Scala

```scala
object Solution {
    def longestMonotonicSubarray(nums: Array[Int]): Int = {
        if (nums.isEmpty) return 0
        var inc = 1
        var dec = 1
        var maxLen = 1
        var i = 1
        while (i < nums.length) {
            if (nums(i) > nums(i - 1)) {
                inc += 1
                dec = 1
            } else if (nums(i) < nums(i - 1)) {
                dec += 1
                inc = 1
            } else {
                inc = 1
                dec = 1
            }
            maxLen = math.max(maxLen, math.max(inc, dec))
            i += 1
        }
        maxLen
    }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_monotonic_subarray(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        let mut inc = 1;
        let mut dec = 1;
        let mut max_len = 1;
        for i in 1..n {
            if nums[i] > nums[i - 1] {
                inc += 1;
                dec = 1;
            } else if nums[i] < nums[i - 1] {
                dec += 1;
                inc = 1;
            } else {
                inc = 1;
                dec = 1;
            }
            max_len = max_len.max(inc).max(dec);
        }
        max_len as i32
    }
}
```

## Racket

```racket
(define/contract (longest-monotonic-subarray nums)
  (-> (listof exact-integer?) exact-integer?)
  (if (null? nums)
      0
      (let loop ((prev (car nums))
                 (rest (cdr nums))
                 (inc 1)
                 (dec 1)
                 (maxlen 1))
        (if (null? rest)
            maxlen
            (let* ((curr (car rest))
                   (new-inc (if (> curr prev) (+ inc 1) 1))
                   (new-dec (if (< curr prev) (+ dec 1) 1))
                   (new-max (max maxlen new-inc new-dec)))
              (loop curr (cdr rest) new-inc new-dec new-max))))))
```

## Erlang

```erlang
-spec longest_monotonic_subarray(Nums :: [integer()]) -> integer().
longest_monotonic_subarray([]) ->
    0;
longest_monotonic_subarray([H|T]) ->
    process(T, H, 1, 1, 1).

process([], _Prev, Max, _Inc, _Dec) ->
    Max;
process([Curr|Rest], Prev, Max, Inc, Dec) ->
    NewMax =
        if
            Curr > Prev ->
                NewInc = Inc + 1,
                NewDec = 1,
                erlang:max(Max, NewInc);
            Curr < Prev ->
                NewDec = Dec + 1,
                NewInc = 1,
                erlang:max(Max, NewDec);
            true -> % Curr == Prev
                NewInc = 1,
                NewDec = 1,
                Max
        end,
    process(Rest, Curr, NewMax, NewInc, NewDec).
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_monotonic_subarray(nums :: [integer]) :: integer
  def longest_monotonic_subarray([]), do: 0
  def longest_monotonic_subarray([_]), do: 1

  def longest_monotonic_subarray([first | rest]) do
    {max_len, _inc_len, _dec_len, _prev} =
      Enum.reduce(rest, {1, 1, 1, first}, fn curr,
                                            {max_len, inc_len, dec_len, prev} ->
        cond do
          curr > prev ->
            inc = inc_len + 1
            dec = 1
            new_max = if inc > max_len, do: inc, else: max_len
            {new_max, inc, dec, curr}

          curr < prev ->
            dec = dec_len + 1
            inc = 1
            new_max = if dec > max_len, do: dec, else: max_len
            {new_max, inc, dec, curr}

          true ->
            {max_len, 1, 1, curr}
        end
      end)

    max_len
  end
end
```
