# 2733. Neither Minimum nor Maximum

## Cpp

```cpp
class Solution {
public:
    int findNonMinOrMax(vector<int>& nums) {
        if (nums.size() <= 2) return -1;
        int mn = nums[0], mx = nums[0];
        for (int v : nums) {
            if (v < mn) mn = v;
            if (v > mx) mx = v;
        }
        for (int v : nums) {
            if (v != mn && v != mx) return v;
        }
        return -1;
    }
};
```

## Java

```java
class Solution {
    public int findNonMinOrMax(int[] nums) {
        if (nums.length < 3) return -1;
        int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
        for (int v : nums) {
            if (v < min) min = v;
            if (v > max) max = v;
        }
        for (int v : nums) {
            if (v != min && v != max) return v;
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return -1
        mn = min(nums)
        mx = max(nums)
        for x in nums:
            if x != mn and x != mx:
                return x
        return -1
```

## Python3

```python
from typing import List

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return -1
        mn = min(nums)
        mx = max(nums)
        for x in nums:
            if x != mn and x != mx:
                return x
        return -1
```

## C

```c
int findNonMinOrMax(int* nums, int numsSize) {
    if (numsSize < 3) return -1;
    int min = nums[0], max = nums[0];
    for (int i = 1; i < numsSize; ++i) {
        if (nums[i] < min) min = nums[i];
        else if (nums[i] > max) max = nums[i];
    }
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] != min && nums[i] != max) return nums[i];
    }
    return -1;
}
```

## Csharp

```csharp
public class Solution {
    public int FindNonMinOrMax(int[] nums) {
        if (nums == null || nums.Length < 3) return -1;
        int min = nums[0], max = nums[0];
        foreach (int v in nums) {
            if (v < min) min = v;
            else if (v > max) max = v;
        }
        foreach (int v in nums) {
            if (v != min && v != max) return v;
        }
        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findNonMinOrMax = function(nums) {
    if (nums.length < 3) return -1;
    let min = Infinity, max = -Infinity;
    for (const v of nums) {
        if (v < min) min = v;
        if (v > max) max = v;
    }
    for (const v of nums) {
        if (v !== min && v !== max) return v;
    }
    return -1;
};
```

## Typescript

```typescript
function findNonMinOrMax(nums: number[]): number {
    if (nums.length <= 2) return -1;
    let min = nums[0], max = nums[0];
    for (const v of nums) {
        if (v < min) min = v;
        if (v > max) max = v;
    }
    for (const v of nums) {
        if (v !== min && v !== max) return v;
    }
    return -1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findNonMinOrMax($nums) {
        if (count($nums) <= 2) {
            return -1;
        }
        $min = min($nums);
        $max = max($nums);
        foreach ($nums as $v) {
            if ($v !== $min && $v !== $max) {
                return $v;
            }
        }
        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func findNonMinOrMax(_ nums: [Int]) -> Int {
        guard nums.count >= 3 else { return -1 }
        var minVal = nums[0]
        var maxVal = nums[0]
        for v in nums {
            if v < minVal { minVal = v }
            if v > maxVal { maxVal = v }
        }
        for v in nums {
            if v != minVal && v != maxVal {
                return v
            }
        }
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findNonMinOrMax(nums: IntArray): Int {
        if (nums.size < 3) return -1
        var min = nums[0]
        var max = nums[0]
        for (v in nums) {
            if (v < min) min = v
            if (v > max) max = v
        }
        for (v in nums) {
            if (v != min && v != max) return v
        }
        return -1
    }
}
```

## Dart

```dart
class Solution {
  int findNonMinOrMax(List<int> nums) {
    if (nums.length < 3) return -1;
    int minVal = nums[0];
    int maxVal = nums[0];
    for (int v in nums) {
      if (v < minVal) minVal = v;
      if (v > maxVal) maxVal = v;
    }
    for (int v in nums) {
      if (v != minVal && v != maxVal) return v;
    }
    return -1;
  }
}
```

## Golang

```go
func findNonMinOrMax(nums []int) int {
	if len(nums) <= 2 {
		return -1
	}
	min, max := nums[0], nums[0]
	for _, v := range nums {
		if v < min {
			min = v
		}
		if v > max {
			max = v
		}
	}
	for _, v := range nums {
		if v != min && v != max {
			return v
		}
	}
	return -1
}
```

## Ruby

```ruby
def find_non_min_or_max(nums)
  return -1 if nums.length < 3
  min_val = nums.min
  max_val = nums.max
  nums.each do |num|
    return num unless num == min_val || num == max_val
  end
  -1
end
```

## Scala

```scala
object Solution {
    def findNonMinOrMax(nums: Array[Int]): Int = {
        if (nums.length < 3) return -1
        var minVal = nums(0)
        var maxVal = nums(0)
        for (v <- nums) {
            if (v < minVal) minVal = v
            if (v > maxVal) maxVal = v
        }
        for (v <- nums) {
            if (v != minVal && v != maxVal) return v
        }
        -1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_non_min_or_max(nums: Vec<i32>) -> i32 {
        if nums.len() < 3 {
            return -1;
        }
        let min = *nums.iter().min().unwrap();
        let max = *nums.iter().max().unwrap();
        for &x in nums.iter() {
            if x != min && x != max {
                return x;
            }
        }
        -1
    }
}
```

## Racket

```racket
(define/contract (find-non-min-or-max nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ((n (length nums)))
    (if (<= n 2)
        -1
        (let* ((mn (apply min nums))
               (mx (apply max nums)))
          (let loop ((lst nums))
            (cond [(empty? lst) -1]
                  [(and (not (= (first lst) mn)) (not (= (first lst) mx))) (first lst)]
                  [else (loop (rest lst))]))))))
```

## Erlang

```erlang
-spec find_non_min_or_max(Nums :: [integer()]) -> integer().
find_non_min_or_max(Nums) ->
    case Nums of
        [] -> -1;
        _ ->
            Min = lists:min(Nums),
            Max = lists:max(Nums),
            find_non_min_or_max(Nums, Min, Max)
    end.

-spec find_non_min_or_max([integer()], integer(), integer()) -> integer().
find_non_min_or_max([], _, _) -> -1;
find_non_min_or_max([H|T], Min, Max) ->
    if
        H =/= Min, H =/= Max -> H;
        true -> find_non_min_or_max(T, Min, Max)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_non_min_or_max(nums :: [integer]) :: integer
  def find_non_min_or_max(nums) do
    min = Enum.min(nums)
    max = Enum.max(nums)

    case Enum.find(nums, fn x -> x != min and x != max end) do
      nil -> -1
      val -> val
    end
  end
end
```
