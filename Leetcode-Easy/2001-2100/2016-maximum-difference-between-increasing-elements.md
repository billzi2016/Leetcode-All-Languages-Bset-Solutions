# 2016. Maximum Difference Between Increasing Elements

## Cpp

```cpp
class Solution {
public:
    int maximumDifference(vector<int>& nums) {
        int n = nums.size();
        int preMin = nums[0];
        int ans = -1;
        for (int j = 1; j < n; ++j) {
            if (nums[j] > preMin) {
                ans = max(ans, nums[j] - preMin);
            } else {
                preMin = nums[j];
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maximumDifference(int[] nums) {
        int min = nums[0];
        int maxDiff = -1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > min) {
                maxDiff = Math.max(maxDiff, nums[i] - min);
            } else {
                min = Math.min(min, nums[i]);
            }
        }
        return maxDiff;
    }
}
```

## Python

```python
class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val = nums[0]
        max_diff = -1
        for num in nums[1:]:
            if num > min_val:
                diff = num - min_val
                if diff > max_diff:
                    max_diff = diff
            else:
                min_val = num
        return max_diff
```

## Python3

```python
class Solution:
    def maximumDifference(self, nums):
        pre_min = nums[0]
        max_diff = -1
        for x in nums[1:]:
            if x > pre_min:
                diff = x - pre_min
                if diff > max_diff:
                    max_diff = diff
            else:
                pre_min = x
        return max_diff
```

## C

```c
int maximumDifference(int* nums, int numsSize) {
    if (numsSize < 2) return -1;
    int minVal = nums[0];
    int maxDiff = -1;
    for (int i = 1; i < numsSize; ++i) {
        if (nums[i] > minVal) {
            int diff = nums[i] - minVal;
            if (diff > maxDiff) maxDiff = diff;
        } else {
            minVal = nums[i];
        }
    }
    return maxDiff;
}
```

## Csharp

```csharp
public class Solution {
    public int MaximumDifference(int[] nums) {
        int n = nums.Length;
        int minVal = nums[0];
        int maxDiff = -1;
        for (int i = 1; i < n; i++) {
            if (nums[i] > minVal) {
                int diff = nums[i] - minVal;
                if (diff > maxDiff) maxDiff = diff;
            } else {
                if (nums[i] < minVal) minVal = nums[i];
            }
        }
        return maxDiff;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumDifference = function(nums) {
    let minVal = nums[0];
    let maxDiff = -1;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > minVal) {
            const diff = nums[i] - minVal;
            if (diff > maxDiff) maxDiff = diff;
        } else {
            if (nums[i] < minVal) minVal = nums[i];
        }
    }
    return maxDiff;
};
```

## Typescript

```typescript
function maximumDifference(nums: number[]): number {
    let minVal = nums[0];
    let maxDiff = -1;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > minVal) {
            const diff = nums[i] - minVal;
            if (diff > maxDiff) maxDiff = diff;
        } else {
            minVal = Math.min(minVal, nums[i]);
        }
    }
    return maxDiff;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximumDifference($nums) {
        $n = count($nums);
        if ($n < 2) return -1;
        $minVal = $nums[0];
        $maxDiff = -1;
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] > $minVal) {
                $diff = $nums[$i] - $minVal;
                if ($diff > $maxDiff) {
                    $maxDiff = $diff;
                }
            } else {
                if ($nums[$i] < $minVal) {
                    $minVal = $nums[$i];
                }
            }
        }
        return $maxDiff;
    }
}
```

## Swift

```swift
class Solution {
    func maximumDifference(_ nums: [Int]) -> Int {
        var minVal = nums[0]
        var maxDiff = -1
        for i in 1..<nums.count {
            let val = nums[i]
            if val > minVal {
                let diff = val - minVal
                if diff > maxDiff { maxDiff = diff }
            } else {
                minVal = val
            }
        }
        return maxDiff
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumDifference(nums: IntArray): Int {
        var minVal = nums[0]
        var maxDiff = -1
        for (i in 1 until nums.size) {
            val cur = nums[i]
            if (cur > minVal) {
                val diff = cur - minVal
                if (diff > maxDiff) maxDiff = diff
            } else {
                if (cur < minVal) minVal = cur
            }
        }
        return maxDiff
    }
}
```

## Dart

```dart
class Solution {
  int maximumDifference(List<int> nums) {
    int minVal = nums[0];
    int maxDiff = -1;
    for (int i = 1; i < nums.length; i++) {
      if (nums[i] > minVal) {
        int diff = nums[i] - minVal;
        if (diff > maxDiff) {
          maxDiff = diff;
        }
      } else {
        minVal = nums[i];
      }
    }
    return maxDiff;
  }
}
```

## Golang

```go
func maximumDifference(nums []int) int {
	if len(nums) < 2 {
		return -1
	}
	minVal := nums[0]
	maxDiff := -1
	for i := 1; i < len(nums); i++ {
		if nums[i] > minVal {
			if diff := nums[i] - minVal; diff > maxDiff {
				maxDiff = diff
			}
		} else if nums[i] < minVal {
			minVal = nums[i]
		}
	}
	return maxDiff
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def maximum_difference(nums)
  min_val = nums[0]
  max_diff = -1

  (1...nums.length).each do |i|
    if nums[i] > min_val
      diff = nums[i] - min_val
      max_diff = diff if diff > max_diff
    else
      min_val = nums[i] if nums[i] < min_val
    end
  end

  max_diff
end
```

## Scala

```scala
object Solution {
    def maximumDifference(nums: Array[Int]): Int = {
        var minVal = nums(0)
        var maxDiff = -1
        for (i <- 1 until nums.length) {
            if (nums(i) > minVal) {
                val diff = nums(i) - minVal
                if (diff > maxDiff) maxDiff = diff
            } else {
                minVal = nums(i)
            }
        }
        maxDiff
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_difference(nums: Vec<i32>) -> i32 {
        let mut min_val = nums[0];
        let mut ans = -1;
        for &num in nums.iter().skip(1) {
            if num > min_val {
                let diff = num - min_val;
                if diff > ans {
                    ans = diff;
                }
            } else {
                min_val = num;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (maximum-difference nums)
  (-> (listof exact-integer?) exact-integer?)
  (if (< (length nums) 2)
      -1
      (let loop ((rest (cdr nums))
                 (min-so-far (car nums))
                 (max-diff -1))
        (if (null? rest)
            max-diff
            (let* ((x (car rest))
                   (new-max (if (> x min-so-far) (max max-diff (- x min-so-far)) max-diff))
                   (new-min (min min-so-far x)))
              (loop (cdr rest) new-min new-max))))))
```

## Erlang

```erlang
-spec maximum_difference(Nums :: [integer()]) -> integer().
maximum_difference(Nums) ->
    case Nums of
        [] -> -1;
        [_] -> -1;
        [First | Rest] ->
            loop(Rest, First, -1)
    end.

loop([], _Min, MaxDiff) ->
    MaxDiff;
loop([H | T], Min, MaxDiff) ->
    Diff = H - Min,
    NewMax =
        if
            H > Min andalso Diff > MaxDiff -> Diff;
            true -> MaxDiff
        end,
    NewMin = erlang:min(Min, H),
    loop(T, NewMin, NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_difference(nums :: [integer]) :: integer
  def maximum_difference([head | tail]) do
    {_min_val, max_diff} =
      Enum.reduce(tail, {head, -1}, fn x, {min_val, max_diff} ->
        if x > min_val do
          {min_val, max(max_diff, x - min_val)}
        else
          {min(x, min_val), max_diff}
        end
      end)

    max_diff
  end

  def maximum_difference(_), do: -1
end
```
