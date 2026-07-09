# 2148. Count Elements With Strictly Smaller and Greater Elements

## Cpp

```cpp
class Solution {
public:
    int countElements(vector<int>& nums) {
        if (nums.empty()) return 0;
        int mn = nums[0], mx = nums[0];
        for (int x : nums) {
            if (x < mn) mn = x;
            if (x > mx) mx = x;
        }
        if (mn == mx) return 0;
        int cntMin = 0, cntMax = 0;
        for (int x : nums) {
            if (x == mn) ++cntMin;
            else if (x == mx) ++cntMax;
        }
        return static_cast<int>(nums.size()) - cntMin - cntMax;
    }
};
```

## Java

```java
class Solution {
    public int countElements(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int min = nums[0];
        int max = nums[0];
        for (int v : nums) {
            if (v < min) min = v;
            if (v > max) max = v;
        }
        if (min == max) return 0;
        int cntMin = 0, cntMax = 0;
        for (int v : nums) {
            if (v == min) cntMin++;
            else if (v == max) cntMax++;
        }
        return nums.length - cntMin - cntMax;
    }
}
```

## Python

```python
class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        min_val = min(nums)
        max_val = max(nums)
        if min_val == max_val:
            return 0
        cnt = 0
        for x in nums:
            if min_val < x < max_val:
                cnt += 1
        return cnt
```

## Python3

```python
from typing import List

class Solution:
    def countElements(self, nums: List[int]) -> int:
        if not nums:
            return 0
        mn = min(nums)
        mx = max(nums)
        if mn == mx:
            return 0
        cnt = 0
        for v in nums:
            if mn < v < mx:
                cnt += 1
        return cnt
```

## C

```c
int countElements(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    int mn = nums[0], mx = nums[0];
    for (int i = 1; i < numsSize; ++i) {
        if (nums[i] < mn) mn = nums[i];
        if (nums[i] > mx) mx = nums[i];
    }
    if (mn == mx) return 0;
    int cntMin = 0, cntMax = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == mn) ++cntMin;
        else if (nums[i] == mx) ++cntMax;
    }
    return numsSize - cntMin - cntMax;
}
```

## Csharp

```csharp
public class Solution {
    public int CountElements(int[] nums) {
        if (nums == null || nums.Length == 0) return 0;
        int min = nums[0], max = nums[0];
        foreach (int x in nums) {
            if (x < min) min = x;
            if (x > max) max = x;
        }
        if (min == max) return 0;
        int cntMin = 0, cntMax = 0;
        foreach (int x in nums) {
            if (x == min) cntMin++;
            else if (x == max) cntMax++;
        }
        return nums.Length - cntMin - cntMax;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var countElements = function(nums) {
    let min = Infinity, max = -Infinity;
    for (const v of nums) {
        if (v < min) min = v;
        if (v > max) max = v;
    }
    if (min === max) return 0;
    let cnt = 0;
    for (const v of nums) {
        if (v !== min && v !== max) cnt++;
    }
    return cnt;
};
```

## Typescript

```typescript
function countElements(nums: number[]): number {
    let min = nums[0];
    let max = nums[0];
    for (const v of nums) {
        if (v < min) min = v;
        if (v > max) max = v;
    }
    if (min === max) return 0;
    let minCount = 0, maxCount = 0;
    for (const v of nums) {
        if (v === min) minCount++;
        else if (v === max) maxCount++;
    }
    return nums.length - minCount - maxCount;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countElements($nums) {
        $n = count($nums);
        if ($n == 0) return 0;
        $min = $max = $nums[0];
        foreach ($nums as $v) {
            if ($v < $min) $min = $v;
            if ($v > $max) $max = $v;
        }
        if ($min === $max) return 0;
        $cntMin = $cntMax = 0;
        foreach ($nums as $v) {
            if ($v == $min) {
                $cntMin++;
            } elseif ($v == $max) {
                $cntMax++;
            }
        }
        return $n - $cntMin - $cntMax;
    }
}
```

## Swift

```swift
class Solution {
    func countElements(_ nums: [Int]) -> Int {
        guard let minVal = nums.min(), let maxVal = nums.max() else { return 0 }
        if minVal == maxVal { return 0 }
        var count = 0
        for v in nums {
            if v != minVal && v != maxVal {
                count += 1
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countElements(nums: IntArray): Int {
        var minVal = Int.MAX_VALUE
        var maxVal = Int.MIN_VALUE
        for (v in nums) {
            if (v < minVal) minVal = v
            if (v > maxVal) maxVal = v
        }
        if (minVal == maxVal) return 0
        var cntMin = 0
        var cntMax = 0
        for (v in nums) {
            when (v) {
                minVal -> cntMin++
                maxVal -> cntMax++
            }
        }
        return nums.size - cntMin - cntMax
    }
}
```

## Dart

```dart
class Solution {
  int countElements(List<int> nums) {
    int minVal = nums[0];
    int maxVal = nums[0];
    for (int v in nums) {
      if (v < minVal) minVal = v;
      if (v > maxVal) maxVal = v;
    }
    if (minVal == maxVal) return 0;
    int cntMin = 0, cntMax = 0;
    for (int v in nums) {
      if (v == minVal) {
        cntMin++;
      } else if (v == maxVal) {
        cntMax++;
      }
    }
    return nums.length - cntMin - cntMax;
  }
}
```

## Golang

```go
func countElements(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	minVal, maxVal := nums[0], nums[0]
	for _, v := range nums {
		if v < minVal {
			minVal = v
		}
		if v > maxVal {
			maxVal = v
		}
	}
	if minVal == maxVal {
		return 0
	}
	cntMin, cntMax := 0, 0
	for _, v := range nums {
		if v == minVal {
			cntMin++
		}
		if v == maxVal {
			cntMax++
		}
	}
	return len(nums) - cntMin - cntMax
}
```

## Ruby

```ruby
def count_elements(nums)
  min_val = nums.min
  max_val = nums.max
  return 0 if min_val == max_val
  cnt_min = nums.count { |x| x == min_val }
  cnt_max = nums.count { |x| x == max_val }
  nums.length - cnt_min - cnt_max
end
```

## Scala

```scala
object Solution {
    def countElements(nums: Array[Int]): Int = {
        if (nums.isEmpty) return 0
        val minVal = nums.min
        val maxVal = nums.max
        if (minVal == maxVal) 0
        else nums.count(x => x != minVal && x != maxVal)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_elements(nums: Vec<i32>) -> i32 {
        let mut min_val = i32::MAX;
        let mut max_val = i32::MIN;
        for &v in &nums {
            if v < min_val { min_val = v; }
            if v > max_val { max_val = v; }
        }
        if min_val == max_val {
            return 0;
        }
        let cnt_min = nums.iter().filter(|&&x| x == min_val).count();
        let cnt_max = nums.iter().filter(|&&x| x == max_val).count();
        (nums.len() - cnt_min - cnt_max) as i32
    }
}
```

## Racket

```racket
(define/contract (count-elements nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((min-val (apply min nums))
         (max-val (apply max nums))
         (len (length nums)))
    (if (= min-val max-val)
        0
        (let loop ((lst nums) (cnt-min 0) (cnt-max 0))
          (cond [(null? lst) (- len cnt-min cnt-max)]
                [else (loop (cdr lst)
                            (+ cnt-min (if (= (car lst) min-val) 1 0))
                            (+ cnt-max (if (= (car lst) max-val) 1 0)))])))) )
```

## Erlang

```erlang
-spec count_elements([integer()]) -> integer().
count_elements(Nums) ->
    case Nums of
        [] -> 0;
        _ ->
            Min = lists:min(Nums),
            Max = lists:max(Nums),
            if Min == Max ->
                    0;
               true ->
                    CntMin = count_occurrences(Min, Nums),
                    CntMax = count_occurrences(Max, Nums),
                    length(Nums) - CntMin - CntMax
            end
    end.

-spec count_occurrences(integer(), [integer()]) -> integer().
count_occurrences(_, []) -> 0;
count_occurrences(V, [H|T]) ->
    (if H == V -> 1; true -> 0 end) + count_occurrences(V, T).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_elements(nums :: [integer]) :: integer
  def count_elements(nums) do
    min_val = Enum.min(nums)
    max_val = Enum.max(nums)

    if min_val == max_val do
      0
    else
      total = length(nums)
      cnt_min = Enum.count(nums, fn x -> x == min_val end)
      cnt_max = Enum.count(nums, fn x -> x == max_val end)
      total - cnt_min - cnt_max
    end
  end
end
```
