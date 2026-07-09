# 2760. Longest Even Odd Subarray With Threshold

## Cpp

```cpp
class Solution {
public:
    int longestAlternatingSubarray(vector<int>& nums, int threshold) {
        int maxLen = 0;
        int curLen = 0;
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (nums[i] > threshold) {
                curLen = 0;
                continue;
            }
            if (curLen == 0) {
                // can only start if even
                if (nums[i] % 2 == 0) {
                    curLen = 1;
                } else {
                    curLen = 0;
                }
            } else {
                // expect opposite parity of previous element
                int prev = nums[i - 1];
                if ((prev % 2 != nums[i] % 2)) {
                    ++curLen;
                } else {
                    // restart if current is even, otherwise reset
                    curLen = (nums[i] % 2 == 0) ? 1 : 0;
                }
            }
            maxLen = max(maxLen, curLen);
        }
        return maxLen;
    }
};
```

## Java

```java
class Solution {
    public int longestAlternatingSubarray(int[] nums, int threshold) {
        int maxLen = 0;
        int curLen = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > threshold) {
                curLen = 0;
                continue;
            }
            if (curLen == 0) {
                if ((nums[i] & 1) == 0) { // even start
                    curLen = 1;
                    maxLen = Math.max(maxLen, curLen);
                }
            } else {
                if ((nums[i] & 1) != (nums[i - 1] & 1)) {
                    curLen++;
                    maxLen = Math.max(maxLen, curLen);
                } else {
                    if ((nums[i] & 1) == 0) { // start new from even
                        curLen = 1;
                        maxLen = Math.max(maxLen, curLen);
                    } else {
                        curLen = 0;
                    }
                }
            }
        }
        return maxLen;
    }
}
```

## Python

```python
class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        max_len = 0
        cur_len = 0
        for i in range(len(nums)):
            if nums[i] > threshold:
                cur_len = 0
                continue
            if cur_len == 0:
                if nums[i] % 2 == 0:
                    cur_len = 1
                    max_len = max(max_len, cur_len)
                else:
                    cur_len = 0
            else:
                if nums[i] % 2 != nums[i - 1] % 2:
                    cur_len += 1
                    max_len = max(max_len, cur_len)
                else:
                    if nums[i] % 2 == 0:
                        cur_len = 1
                        max_len = max(max_len, cur_len)
                    else:
                        cur_len = 0
        return max_len
```

## Python3

```python
from typing import List

class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        max_len = 0
        cur_len = 0
        prev_parity = -1  # placeholder
        
        for num in nums:
            if num > threshold:
                cur_len = 0
                prev_parity = -1
                continue
            
            parity = num & 1
            if cur_len == 0:
                if parity == 0:  # must start with even
                    cur_len = 1
                    prev_parity = parity
                else:
                    cur_len = 0
                    prev_parity = -1
            else:
                if parity != prev_parity:
                    cur_len += 1
                    prev_parity = parity
                else:
                    # restart if current num is even, otherwise reset
                    if parity == 0:
                        cur_len = 1
                        prev_parity = parity
                    else:
                        cur_len = 0
                        prev_parity = -1
            if cur_len > max_len:
                max_len = cur_len
        
        return max_len
```

## C

```c
int longestAlternatingSubarray(int* nums, int numsSize, int threshold) {
    int maxLen = 0;
    int curLen = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] > threshold) {
            curLen = 0;
            continue;
        }
        if (curLen == 0) {
            if ((nums[i] & 1) == 0) {
                curLen = 1;
            }
        } else {
            if ((nums[i] & 1) != (nums[i - 1] & 1)) {
                ++curLen;
            } else {
                curLen = ((nums[i] & 1) == 0) ? 1 : 0;
            }
        }
        if (curLen > maxLen) maxLen = curLen;
    }
    return maxLen;
}
```

## Csharp

```csharp
public class Solution {
    public int LongestAlternatingSubarray(int[] nums, int threshold) {
        int maxLen = 0;
        int curLen = 0;
        bool expectEven = true; // when starting a new subarray we need even
        
        foreach (int x in nums) {
            if (x > threshold) {
                curLen = 0;
                expectEven = true;
                continue;
            }
            
            if (curLen == 0) {
                if (x % 2 == 0) {
                    curLen = 1;
                    expectEven = false; // next should be odd
                } else {
                    curLen = 0;
                    expectEven = true;
                }
            } else {
                bool isEven = x % 2 == 0;
                if ((expectEven && isEven) || (!expectEven && !isEven)) {
                    // parity matches expectation
                    curLen++;
                    expectEven = !expectEven; // toggle expectation
                } else {
                    // start new subarray from current element if it's even
                    if (isEven) {
                        curLen = 1;
                        expectEven = false;
                    } else {
                        curLen = 0;
                        expectEven = true;
                    }
                }
            }
            
            if (curLen > maxLen) maxLen = curLen;
        }
        
        return maxLen;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} threshold
 * @return {number}
 */
var longestAlternatingSubarray = function(nums, threshold) {
    let maxLen = 0;
    let curLen = 0;
    for (let i = 0; i < nums.length; ++i) {
        if (nums[i] > threshold) {
            curLen = 0;
        } else if (i > 0 && (nums[i] % 2) === (nums[i - 1] % 2)) {
            // same parity as previous, start new subarray from current element
            curLen = 1;
        } else {
            curLen += 1;
        }
        if (curLen > maxLen) maxLen = curLen;
    }
    return maxLen;
};
```

## Typescript

```typescript
function longestAlternatingSubarray(nums: number[], threshold: number): number {
    let maxLen = 0;
    let curLen = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] > threshold) {
            curLen = 0;
            continue;
        }
        const isEven = nums[i] % 2 === 0;
        if (curLen === 0) {
            curLen = isEven ? 1 : 0;
        } else {
            // previous element is part of the current subarray at i-1
            if ((nums[i] % 2) !== (nums[i - 1] % 2)) {
                curLen++;
            } else {
                curLen = isEven ? 1 : 0;
            }
        }
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
     * @param Integer $threshold
     * @return Integer
     */
    function longestAlternatingSubarray($nums, $threshold) {
        $maxLen = 0;
        $curLen = 0;
        $prevParity = null; // null indicates no previous element in current window

        foreach ($nums as $num) {
            if ($num > $threshold) {
                $curLen = 0;
                $prevParity = null;
                continue;
            }

            $parity = $num % 2; // 0 for even, 1 for odd

            if ($curLen == 0) {
                // can only start a new subarray with an even number
                if ($parity == 0) {
                    $curLen = 1;
                    $prevParity = $parity;
                } else {
                    $curLen = 0;
                    $prevParity = null;
                }
            } else {
                // we have a valid subarray so far
                if ($parity != $prevParity) {
                    $curLen++;
                    $prevParity = $parity;
                } else {
                    // parity repeats, restart only if current is even
                    if ($parity == 0) {
                        $curLen = 1;
                        $prevParity = $parity;
                    } else {
                        $curLen = 0;
                        $prevParity = null;
                    }
                }
            }

            if ($curLen > $maxLen) {
                $maxLen = $curLen;
            }
        }

        return $maxLen;
    }
}
```

## Swift

```swift
class Solution {
    func longestAlternatingSubarray(_ nums: [Int], _ threshold: Int) -> Int {
        var maxLen = 0
        var curLen = 0
        for i in 0..<nums.count {
            let val = nums[i]
            if val > threshold {
                curLen = 0
                continue
            }
            if curLen == 0 {
                if val % 2 == 0 {
                    curLen = 1
                    maxLen = max(maxLen, curLen)
                } else {
                    curLen = 0
                }
            } else {
                let prev = nums[i - 1]
                if (val % 2) != (prev % 2) {
                    curLen += 1
                    maxLen = max(maxLen, curLen)
                } else {
                    if val % 2 == 0 {
                        curLen = 1
                        maxLen = max(maxLen, curLen)
                    } else {
                        curLen = 0
                    }
                }
            }
        }
        return maxLen
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestAlternatingSubarray(nums: IntArray, threshold: Int): Int {
        var maxLen = 0
        var cur = 0
        for (i in nums.indices) {
            val v = nums[i]
            if (v > threshold) {
                cur = 0
                continue
            }
            if (cur == 0) {
                if (v % 2 == 0) {
                    cur = 1
                    if (cur > maxLen) maxLen = cur
                }
            } else {
                val prev = nums[i - 1]
                if (v % 2 != prev % 2) {
                    cur += 1
                } else {
                    cur = if (v % 2 == 0) 1 else 0
                }
                if (cur > maxLen) maxLen = cur
            }
        }
        return maxLen
    }
}
```

## Dart

```dart
class Solution {
  int longestAlternatingSubarray(List<int> nums, int threshold) {
    int maxLen = 0;
    int curLen = 0;
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] > threshold) {
        curLen = 0;
        continue;
      }
      if (curLen == 0) {
        // can only start if current is even
        curLen = (nums[i] % 2 == 0) ? 1 : 0;
      } else {
        // check alternating parity with previous element which was part of subarray
        if ((nums[i - 1] <= threshold) && (nums[i - 1] % 2 != nums[i] % 2)) {
          curLen += 1;
        } else {
          // restart: only if current is even
          curLen = (nums[i] % 2 == 0) ? 1 : 0;
        }
      }
      if (curLen > maxLen) maxLen = curLen;
    }
    return maxLen;
  }
}
```

## Golang

```go
func longestAlternatingSubarray(nums []int, threshold int) int {
    ans := 0
    cur := 0
    var lastParity int

    for _, v := range nums {
        if v > threshold {
            cur = 0
            continue
        }
        parity := v & 1
        if cur == 0 {
            if parity == 0 { // start with even
                cur = 1
                lastParity = parity
            } else {
                cur = 0
            }
        } else {
            if parity != lastParity {
                cur++
                lastParity = parity
            } else {
                if parity == 0 { // restart from this even element
                    cur = 1
                    lastParity = parity
                } else {
                    cur = 0
                }
            }
        }
        if cur > ans {
            ans = cur
        }
    }
    return ans
}
```

## Ruby

```ruby
def longest_alternating_subarray(nums, threshold)
  max_len = 0
  cur_len = 0
  prev_val = nil

  nums.each do |val|
    if val > threshold
      cur_len = 0
      prev_val = nil
      next
    end

    if cur_len == 0
      if val.even?
        cur_len = 1
        max_len = [max_len, cur_len].max
        prev_val = val
      else
        prev_val = nil
      end
    else
      if (prev_val % 2 != val % 2)
        cur_len += 1
        max_len = [max_len, cur_len].max
        prev_val = val
      else
        if val.even?
          cur_len = 1
          max_len = [max_len, cur_len].max
          prev_val = val
        else
          cur_len = 0
          prev_val = nil
        end
      end
    end
  end

  max_len
end
```

## Scala

```scala
object Solution {
    def longestAlternatingSubarray(nums: Array[Int], threshold: Int): Int = {
        var maxLen = 0
        var curLen = 0
        var prev = -1

        for (num <- nums) {
            if (num > threshold) {
                curLen = 0
                prev = -1
            } else {
                if (curLen == 0) {
                    curLen = 1
                } else {
                    if ((prev % 2) != (num % 2)) {
                        curLen += 1
                    } else {
                        curLen = 1
                    }
                }
                maxLen = math.max(maxLen, curLen)
                prev = num
            }
        }

        maxLen
    }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_alternating_subarray(nums: Vec<i32>, threshold: i32) -> i32 {
        let n = nums.len();
        let mut max_len: usize = 0;
        let mut cur_len: usize = 0;
        for i in 0..n {
            if nums[i] > threshold {
                cur_len = 0;
                continue;
            }
            if cur_len == 0 {
                if nums[i] % 2 == 0 {
                    cur_len = 1;
                } else {
                    cur_len = 0;
                }
            } else {
                if nums[i] % 2 != nums[i - 1] % 2 {
                    cur_len += 1;
                } else {
                    if nums[i] % 2 == 0 {
                        cur_len = 1;
                    } else {
                        cur_len = 0;
                    }
                }
            }
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
(define/contract (longest-alternating-subarray nums threshold)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let loop ((prev #f)          ; previous element in current window
             (curr-len 0)       ; length of current valid window
             (max-len 0)        ; best length seen so far
             (lst nums))        ; remaining list to process
    (if (null? lst)
        max-len
        (let* ((x (car lst))
               (valid (<= x threshold)))
          (cond
            [(not valid)
             (loop #f 0 (max max-len curr-len) (cdr lst))]
            [else
             (if (and prev (eq? (even? prev) (even? x))) ; same parity → break alternation
                 (let ((newlen 1))
                   (loop x newlen (max max-len (max curr-len newlen)) (cdr lst)))
                 (let ((newlen (if prev (+ curr-len 1) 1)))
                   (loop x newlen (max max-len newlen) (cdr lst))))])))))
```

## Erlang

```erlang
-spec longest_alternating_subarray(Nums :: [integer()], Threshold :: integer()) -> integer().
longest_alternating_subarray(Nums, Threshold) ->
    helper(Nums, undefined, 0, 0, Threshold).

helper([], _Prev, _Curr, Max, _Thresh) ->
    Max;
helper([H|T], Prev, Curr, Max, Thresh) when H =< Thresh ->
    NewCurr =
        case Prev of
            undefined -> 1;
            _ when (H rem 2) =/= (Prev rem 2) -> Curr + 1;
            _ -> 1
        end,
    NewMax = erlang:max(Max, NewCurr),
    helper(T, H, NewCurr, NewMax, Thresh);
helper([_H|T], _Prev, _Curr, Max, _Thresh) ->
    %% Element exceeds threshold, reset the window
    helper(T, undefined, 0, Max, _Thresh).
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_alternating_subarray(nums :: [integer], threshold :: integer) :: integer
  def longest_alternating_subarray(nums, threshold) do
    {max_len, _, _} =
      Enum.reduce(nums, {0, 0, nil}, fn num, {max_len, cur_len, prev} ->
        if num > threshold do
          {max_len, 0, nil}
        else
          cond do
            cur_len == 0 ->
              new_cur = 1
              {Kernel.max(max_len, new_cur), new_cur, num}

            rem(num, 2) != rem(prev, 2) ->
              new_cur = cur_len + 1
              {Kernel.max(max_len, new_cur), new_cur, num}

            true ->
              new_cur = 1
              {Kernel.max(max_len, new_cur), new_cur, num}
          end
        end
      end)

    max_len
  end
end
```
