# 2765. Longest Alternating Subarray

## Cpp

```cpp
class Solution {
public:
    int alternatingSubarray(vector<int>& nums) {
        int n = nums.size();
        int ans = -1;
        int cur = 1; // current length of potential alternating subarray
        int prevDiff = 0;
        for (int i = 1; i < n; ++i) {
            int diff = nums[i] - nums[i-1];
            if (abs(diff) == 1 && (cur == 1 || diff * prevDiff == -1)) {
                cur = (cur == 1 ? 2 : cur + 1);
                ans = max(ans, cur);
                prevDiff = diff;
            } else {
                if (abs(diff) == 1) {
                    cur = 2;
                    ans = max(ans, cur);
                    prevDiff = diff;
                } else {
                    cur = 1;
                    prevDiff = 0;
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int alternatingSubarray(int[] nums) {
        int n = nums.length;
        int maxLen = -1;
        int curLen = 1; // length of current alternating subarray ending at i
        int prevSign = 0; // sign of the last difference (+1 or -1)

        for (int i = 1; i < n; i++) {
            int diff = nums[i] - nums[i - 1];
            if (Math.abs(diff) == 1) {
                int sign = diff > 0 ? 1 : -1;
                if (curLen >= 2 && sign == prevSign) {
                    // same direction as previous, start new subarray from i-1
                    curLen = 2;
                } else {
                    curLen++;
                }
                prevSign = sign;
            } else {
                curLen = 1;
                prevSign = 0;
            }
            if (curLen > maxLen) {
                maxLen = curLen;
            }
        }

        return maxLen >= 2 ? maxLen : -1;
    }
}
```

## Python

```python
class Solution(object):
    def alternatingSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = -1
        cur_len = 1          # length of current candidate ending at i-1
        prev_diff = None     # previous valid difference (+1 or -1)

        for i in range(1, n):
            diff = nums[i] - nums[i - 1]
            if abs(diff) == 1:
                if prev_diff is not None and diff * prev_diff == -1:
                    cur_len += 1
                else:
                    cur_len = 2   # start new subarray with the pair (i-1, i)
                ans = max(ans, cur_len)
                prev_diff = diff
            else:
                cur_len = 1
                prev_diff = None

        return ans
```

## Python3

```python
class Solution:
    def alternatingSubarray(self, nums):
        n = len(nums)
        max_len = -1
        cur_len = 1
        last_sign = 0

        for i in range(1, n):
            diff = nums[i] - nums[i - 1]
            if abs(diff) == 1:
                if cur_len == 1:
                    cur_len = 2
                    last_sign = diff
                else:
                    if diff == -last_sign:
                        cur_len += 1
                        last_sign = diff
                    else:
                        cur_len = 2
                        last_sign = diff
                max_len = max(max_len, cur_len)
            else:
                cur_len = 1
                last_sign = 0

        return max_len
```

## C

```c
int alternatingSubarray(int* nums, int numsSize) {
    int maxLen = -1;
    int curLen = 0;
    int expect = 0; // expected difference for the next element
    
    for (int i = 1; i < numsSize; ++i) {
        int diff = nums[i] - nums[i - 1];
        
        if (diff == 1) {                 // start a new alternating subarray
            curLen = 2;
            expect = -1;
            if (curLen > maxLen) maxLen = curLen;
        } else if (curLen > 0 && diff == expect) {
            ++curLen;                    // extend current subarray
            expect = -expect;            // toggle expected difference
            if (curLen > maxLen) maxLen = curLen;
        } else {                         // cannot continue, reset
            curLen = 0;
        }
    }
    
    return maxLen;
}
```

## Csharp

```csharp
public class Solution
{
    public int AlternatingSubarray(int[] nums)
    {
        int n = nums.Length;
        int maxLen = -1;
        int curLen = 0;
        int prevDiff = 0;
        bool hasPrev = false;

        for (int i = 1; i < n; i++)
        {
            int diff = nums[i] - nums[i - 1];
            if (Math.Abs(diff) != 1)
            {
                curLen = 0;
                hasPrev = false;
                continue;
            }

            if (!hasPrev)
            {
                curLen = 2;
            }
            else
            {
                if (diff != prevDiff)
                    curLen += 1;
                else
                    curLen = 2; // restart from current pair
            }

            maxLen = Math.Max(maxLen, curLen);
            prevDiff = diff;
            hasPrev = true;
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
var alternatingSubarray = function(nums) {
    let maxLen = 0;
    let curLen = 1;
    let prevDiff = 0;
    
    for (let i = 1; i < nums.length; ++i) {
        const diff = nums[i] - nums[i - 1];
        if (Math.abs(diff) !== 1) {
            curLen = 1;
        } else {
            if (curLen === 1) {
                curLen = 2;
            } else {
                curLen = (diff === -prevDiff) ? curLen + 1 : 2;
            }
            prevDiff = diff;
        }
        if (curLen > maxLen) maxLen = curLen;
    }
    
    return maxLen >= 2 ? maxLen : -1;
};
```

## Typescript

```typescript
function alternatingSubarray(nums: number[]): number {
    let maxLen = 0;
    let curLen = 1;
    for (let i = 1; i < nums.length; i++) {
        if (Math.abs(nums[i] - nums[i - 1]) === 1) {
            curLen += 1;
            if (curLen > maxLen) maxLen = curLen;
        } else {
            curLen = 1;
        }
    }
    return maxLen >= 2 ? maxLen : -1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function alternatingSubarray($nums) {
        $n = count($nums);
        $maxLen = 0;
        $cur = 1; // length of current candidate subarray

        for ($i = 1; $i < $n; ++$i) {
            $diff = $nums[$i] - $nums[$i - 1];
            if (abs($diff) != 1) {
                $cur = 1;
                continue;
            }

            // check alternation with previous difference
            if ($i >= 2 && abs($nums[$i - 1] - $nums[$i - 2]) == 1 &&
                $diff * ($nums[$i - 1] - $nums[$i - 2]) < 0) {
                $cur += 1;
            } else {
                // start a new alternating subarray of length 2
                $cur = 2;
            }

            if ($cur > $maxLen) {
                $maxLen = $cur;
            }
        }

        return $maxLen >= 2 ? $maxLen : -1;
    }
}
```

## Swift

```swift
class Solution {
    func alternatingSubarray(_ nums: [Int]) -> Int {
        var maxLen = 0
        var curLen = 1
        var prevDiff = 0
        
        for i in 1..<nums.count {
            let diff = nums[i] - nums[i - 1]
            if abs(diff) == 1 {
                if curLen == 1 {
                    curLen = 2
                } else {
                    if diff * prevDiff == -1 {
                        curLen += 1
                    } else {
                        curLen = 2
                    }
                }
                prevDiff = diff
                maxLen = max(maxLen, curLen)
            } else {
                curLen = 1
                prevDiff = 0
            }
        }
        
        return maxLen >= 2 ? maxLen : -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun alternatingSubarray(nums: IntArray): Int {
        var maxLen = -1
        var curDiffCount = 0 // number of consecutive diffs satisfying the pattern
        for (i in 0 until nums.size - 1) {
            val diff = nums[i + 1] - nums[i]
            when (diff) {
                1 -> {
                    if (curDiffCount > 0 && curDiffCount % 2 == 0) {
                        // expecting +1 after a -1
                        curDiffCount++
                    } else {
                        // start new potential subarray
                        curDiffCount = 1
                    }
                }
                -1 -> {
                    if (curDiffCount > 0 && curDiffCount % 2 == 1) {
                        // expecting -1 after a +1
                        curDiffCount++
                    } else {
                        // cannot extend, reset
                        curDiffCount = 0
                    }
                }
                else -> {
                    curDiffCount = 0
                }
            }
            if (curDiffCount >= 1) {
                val len = curDiffCount + 1
                if (len > maxLen) maxLen = len
            }
        }
        return maxLen
    }
}
```

## Dart

```dart
class Solution {
  int alternatingSubarray(List<int> nums) {
    int n = nums.length;
    int ans = -1;
    int cur = 1; // current length of a potential alternating subarray
    for (int i = 1; i < n; ++i) {
      int diff = nums[i] - nums[i - 1];
      if (diff == 1) {
        if (cur >= 2 && cur % 2 == 1) {
          cur += 1;
        } else {
          cur = 2;
        }
      } else if (diff == -1) {
        if (cur >= 2 && cur % 2 == 0) {
          cur += 1;
        } else {
          cur = 1; // cannot start with a -1 difference
        }
      } else {
        cur = 1;
      }
      if (cur >= 2 && cur > ans) {
        ans = cur;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func alternatingSubarray(nums []int) int {
	n := len(nums)
	if n < 2 {
		return -1
	}
	maxLen := -1
	curLen := 1
	prevDiff := 0

	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}

	for i := 0; i < n-1; i++ {
		diff := nums[i+1] - nums[i]
		if abs(diff) != 1 {
			curLen = 1
			prevDiff = 0
			continue
		}
		if curLen == 1 {
			curLen = 2
		} else if prevDiff*diff == -1 {
			curLen++
		} else {
			curLen = 2
		}
		if curLen > maxLen {
			maxLen = curLen
		}
		prevDiff = diff
	}
	return maxLen
}
```

## Ruby

```ruby
def alternating_subarray(nums)
  max_len = -1
  cur = 1
  prev_diff = nil

  (1...nums.length).each do |i|
    diff = nums[i] - nums[i - 1]
    if diff.abs == 1
      if cur == 1 || (prev_diff && prev_diff * diff == -1)
        cur += 1
      else
        cur = 2
      end
      max_len = [max_len, cur].max
      prev_diff = diff
    else
      cur = 1
      prev_diff = nil
    end
  end

  max_len
end
```

## Scala

```scala
object Solution {
    def alternatingSubarray(nums: Array[Int]): Int = {
        var maxLen = 0
        var curLen = 0
        for (i <- 1 until nums.length) {
            val diff = nums(i) - nums(i - 1)
            if (math.abs(diff) == 1) {
                if (curLen > 0 && math.abs(nums(i - 1) - nums(i - 2)) == 1 &&
                    (nums(i - 1) - nums(i - 2)) * diff == -1) {
                    curLen += 1
                } else {
                    curLen = 2
                }
            } else {
                curLen = 0
            }
            if (curLen > maxLen) maxLen = curLen
        }
        if (maxLen < 2) -1 else maxLen
    }
}
```

## Rust

```rust
impl Solution {
    pub fn alternating_subarray(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n < 2 {
            return -1;
        }
        let mut ans = 0i32;
        let mut cur_len = 1i32;
        let mut last_diff = 0i32; // placeholder
        for i in 1..n {
            let diff = nums[i] - nums[i - 1];
            if diff.abs() == 1 && (cur_len == 1 || diff.signum() != last_diff.signum()) {
                cur_len += 1;
            } else if diff.abs() == 1 {
                cur_len = 2;
            } else {
                cur_len = 1;
            }
            if cur_len >= 2 {
                ans = ans.max(cur_len);
            }
            if diff.abs() == 1 {
                last_diff = diff;
            } else {
                last_diff = 0;
            }
        }
        if ans == 0 { -1 } else { ans }
    }
}
```

## Racket

```racket
(define/contract (alternating-subarray nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (maxlen -1)
         (curr 0)
         (prev-diff 0))
    (for ([i (in-range (- n 1))])
      (let* ((a (list-ref nums i))
             (b (list-ref nums (+ i 1)))
             (diff (- b a)))
        (if (= (abs diff) 1)
            (begin
              (if (= curr 0)
                  (set! curr 2)
                  (if (= (* diff prev-diff) -1)
                      (set! curr (+ curr 1))
                      (set! curr 2)))
              (when (> curr maxlen) (set! maxlen curr))
              (set! prev-diff diff))
            (begin
              (set! curr 0)
              (set! prev-diff 0)))))
    maxlen))
```

## Erlang

```erlang
-module(solution).
-export([alternating_subarray/1]).

-spec alternating_subarray(Nums :: [integer()]) -> integer().
alternating_subarray(Nums) ->
    case Nums of
        [_] -> -1;
        [First, Second | Rest] ->
            Diff = Second - First,
            InitCur = if erlang:abs(Diff) =:= 1 -> 2; true -> 0 end,
            InitMax = if InitCur >= 2 -> InitCur; true -> -1 end,
            loop(Rest, Second, Diff, InitCur, InitMax)
    end.

loop([], _Prev, _PrevDiff, _CurLen, Max) ->
    Max;
loop([Next | Rest], Prev, PrevDiff, CurLen, Max) ->
    Diff = Next - Prev,
    NewCur =
        case erlang:abs(Diff) of
            1 ->
                if PrevDiff * Diff =:= -1 ->
                        case CurLen of
                            0 -> 2;
                            _ -> CurLen + 1
                        end;
                   true ->
                        2
                end;
            _ -> 0
        end,
    NewMax = if NewCur >= 2, NewCur > Max -> NewCur; true -> Max end,
    loop(Rest, Next, Diff, NewCur, NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec alternating_subarray(nums :: [integer]) :: integer
  def alternating_subarray(nums) do
    case nums do
      [] -> -1
      [_] -> -1
      [first | rest] ->
        helper(rest, first, nil, 1, -1)
    end
  end

  defp helper([], _prev, _prev_diff, _cur_len, max_len), do: max_len

  defp helper([curr | tail], prev, prev_diff, cur_len, max_len) do
    diff = curr - prev

    if abs(diff) == 1 do
      new_cur =
        if not is_nil(prev_diff) and diff != prev_diff do
          cur_len + 1
        else
          2
        end

      new_max = if new_cur > max_len, do: new_cur, else: max_len
      helper(tail, curr, diff, new_cur, new_max)
    else
      helper(tail, curr, nil, 1, max_len)
    end
  end
end
```
