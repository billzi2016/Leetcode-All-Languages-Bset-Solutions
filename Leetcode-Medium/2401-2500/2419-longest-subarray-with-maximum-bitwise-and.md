# 2419. Longest Subarray With Maximum Bitwise AND

## Cpp

```cpp
class Solution {
public:
    int longestSubarray(std::vector<int>& nums) {
        int maxVal = 0;
        for (int x : nums) {
            if (x > maxVal) maxVal = x;
        }
        int ans = 0, cur = 0;
        for (int x : nums) {
            if (x == maxVal) {
                ++cur;
                if (cur > ans) ans = cur;
            } else {
                cur = 0;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int longestSubarray(int[] nums) {
        int maxVal = Integer.MIN_VALUE;
        int cur = 0;
        int best = 0;
        for (int num : nums) {
            if (num > maxVal) {
                maxVal = num;
                cur = 1;
                best = 1;
            } else if (num == maxVal) {
                cur++;
                if (cur > best) best = cur;
            } else {
                cur = 0;
            }
        }
        return best;
    }
}
```

## Python

```python
class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = max(nums)
        cur = ans = 0
        for num in nums:
            if num == max_val:
                cur += 1
                if cur > ans:
                    ans = cur
            else:
                cur = 0
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)
        ans = cur = 0
        for num in nums:
            if num == max_val:
                cur += 1
                if cur > ans:
                    ans = cur
            else:
                cur = 0
        return ans
```

## C

```c
int longestSubarray(int* nums, int numsSize) {
    int max_val = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] > max_val) {
            max_val = nums[i];
        }
    }
    
    int cur = 0, best = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == max_val) {
            ++cur;
            if (cur > best) best = cur;
        } else {
            cur = 0;
        }
    }
    
    return best;
}
```

## Csharp

```csharp
public class Solution
{
    public int LongestSubarray(int[] nums)
    {
        int maxVal = int.MinValue;
        int currentStreak = 0;
        int longest = 0;

        foreach (int num in nums)
        {
            if (num > maxVal)
            {
                maxVal = num;
                currentStreak = 1;
                longest = 1;
            }
            else if (num == maxVal)
            {
                currentStreak++;
                if (currentStreak > longest) longest = currentStreak;
            }
            else
            {
                currentStreak = 0;
            }
        }

        return longest;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSubarray = function(nums) {
    let maxVal = nums[0];
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > maxVal) maxVal = nums[i];
    }
    let best = 0, cur = 0;
    for (const v of nums) {
        if (v === maxVal) {
            cur++;
            if (cur > best) best = cur;
        } else {
            cur = 0;
        }
    }
    return best;
};
```

## Typescript

```typescript
function longestSubarray(nums: number[]): number {
    let maxVal = -Infinity;
    for (const v of nums) {
        if (v > maxVal) maxVal = v;
    }
    let cur = 0, ans = 0;
    for (const v of nums) {
        if (v === maxVal) {
            cur++;
            if (cur > ans) ans = cur;
        } else {
            cur = 0;
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
    function longestSubarray($nums) {
        // Find the maximum value in the array
        $maxVal = $nums[0];
        foreach ($nums as $num) {
            if ($num > $maxVal) {
                $maxVal = $num;
            }
        }

        $best = 0;
        $cur = 0;
        foreach ($nums as $num) {
            if ($num === $maxVal) {
                $cur++;
                if ($cur > $best) {
                    $best = $cur;
                }
            } else {
                $cur = 0;
            }
        }

        return $best;
    }
}
```

## Swift

```swift
class Solution {
    func longestSubarray(_ nums: [Int]) -> Int {
        guard let first = nums.first else { return 0 }
        var maxVal = first
        for v in nums {
            if v > maxVal { maxVal = v }
        }
        var current = 0
        var ans = 0
        for v in nums {
            if v == maxVal {
                current += 1
                if current > ans { ans = current }
            } else {
                current = 0
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestSubarray(nums: IntArray): Int {
        var maxVal = 0
        for (v in nums) {
            if (v > maxVal) maxVal = v
        }
        var ans = 0
        var cur = 0
        for (v in nums) {
            if (v == maxVal) {
                cur++
                if (cur > ans) ans = cur
            } else {
                cur = 0
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int longestSubarray(List<int> nums) {
    int maxVal = nums[0];
    for (int v in nums) {
      if (v > maxVal) maxVal = v;
    }
    int ans = 0, cur = 0;
    for (int v in nums) {
      if (v == maxVal) {
        cur++;
        if (cur > ans) ans = cur;
      } else {
        cur = 0;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func longestSubarray(nums []int) int {
	maxVal := 0
	for _, v := range nums {
		if v > maxVal {
			maxVal = v
		}
	}
	ans, cur := 0, 0
	for _, v := range nums {
		if v == maxVal {
			cur++
			if cur > ans {
				ans = cur
			}
		} else {
			cur = 0
		}
	}
	return ans
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def longest_subarray(nums)
  max_val = nums.max
  longest = 0
  current = 0
  nums.each do |num|
    if num == max_val
      current += 1
      longest = current if current > longest
    else
      current = 0
    end
  end
  longest
end
```

## Scala

```scala
object Solution {
    def longestSubarray(nums: Array[Int]): Int = {
        var maxVal = Int.MinValue
        for (v <- nums) {
            if (v > maxVal) maxVal = v
        }
        var ans = 0
        var cur = 0
        for (v <- nums) {
            if (v == maxVal) {
                cur += 1
                if (cur > ans) ans = cur
            } else {
                cur = 0
            }
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_subarray(nums: Vec<i32>) -> i32 {
        let max_val = *nums.iter().max().unwrap();
        let mut cur = 0;
        let mut ans = 0;
        for &num in nums.iter() {
            if num == max_val {
                cur += 1;
                if cur > ans {
                    ans = cur;
                }
            } else {
                cur = 0;
            }
        }
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (longest-subarray nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((max-val (apply max nums))
         (iter
          (lambda (lst cur best)
            (if (null? lst)
                best
                (let ((x (car lst)))
                  (if (= x max-val)
                      (let ((new-cur (+ cur 1)))
                        (iter (cdr lst) new-cur (max best new-cur)))
                      (iter (cdr lst) 0 best)))))))
    (iter nums 0 0)))
```

## Erlang

```erlang
-spec longest_subarray(Nums :: [integer()]) -> integer().
longest_subarray(Nums) ->
    Max = lists:max(Nums),
    {Ans,_} = lists:foldl(
        fun(X, {Best, Cur}) ->
            case X of
                _ when X =:= Max ->
                    NewCur = Cur + 1,
                    {erlang:max(Best, NewCur), NewCur};
                _ ->
                    {Best, 0}
            end
        end,
        {0,0},
        Nums),
    Ans.
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_subarray(nums :: [integer]) :: integer
  def longest_subarray(nums) do
    max_val = Enum.max(nums)

    {best, _} =
      Enum.reduce(nums, {0, 0}, fn x, {best, cur} ->
        if x == max_val do
          cur = cur + 1
          {max(best, cur), cur}
        else
          {best, 0}
        end
      end)

    best
  end
end
```
