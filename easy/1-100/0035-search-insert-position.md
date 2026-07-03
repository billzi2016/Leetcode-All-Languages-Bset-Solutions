# 0035. Search Insert Position

## Cpp

```cpp
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left = 0, right = nums.size();
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < target)
                left = mid + 1;
            else
                right = mid;
        }
        return left;
    }
};
```

## Java

```java
class Solution {
    public int searchInsert(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int mid = left + ((right - left) >> 1);
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }
}
```

## Python

```python
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo
```

## Python3

```python
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo
```

## C

```c
int searchInsert(int* nums, int numsSize, int target) {
    int left = 0, right = numsSize - 1;
    while (left <= right) {
        int mid = left + ((right - left) >> 1);
        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return left;
}
```

## Csharp

```csharp
public class Solution {
    public int SearchInsert(int[] nums, int target) {
        int left = 0;
        int right = nums.Length - 1;
        while (left <= right) {
            int mid = left + ((right - left) >> 1);
            if (nums[mid] == target) return mid;
            if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    let left = 0, right = nums.length - 1;
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (nums[mid] === target) return mid;
        if (nums[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return left;
};
```

## Typescript

```typescript
function searchInsert(nums: number[], target: number): number {
    let left = 0;
    let right = nums.length - 1;
    while (left <= right) {
        const mid = left + ((right - left) >> 1);
        if (nums[mid] === target) return mid;
        if (target < nums[mid]) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return left;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function searchInsert($nums, $target) {
        $low = 0;
        $high = count($nums) - 1;
        while ($low <= $high) {
            $mid = intdiv($low + $high, 2);
            if ($nums[$mid] == $target) {
                return $mid;
            } elseif ($nums[$mid] < $target) {
                $low = $mid + 1;
            } else {
                $high = $mid - 1;
            }
        }
        return $low;
    }
}
```

## Swift

```swift
class Solution {
    func searchInsert(_ nums: [Int], _ target: Int) -> Int {
        var left = 0
        var right = nums.count - 1
        
        while left <= right {
            let mid = left + (right - left) / 2
            if nums[mid] == target {
                return mid
            } else if nums[mid] < target {
                left = mid + 1
            } else {
                right = mid - 1
            }
        }
        return left
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun searchInsert(nums: IntArray, target: Int): Int {
        var left = 0
        var right = nums.size - 1
        while (left <= right) {
            val mid = left + (right - left) / 2
            when {
                nums[mid] == target -> return mid
                nums[mid] < target -> left = mid + 1
                else -> right = mid - 1
            }
        }
        return left
    }
}
```

## Dart

```dart
class Solution {
  int searchInsert(List<int> nums, int target) {
    int left = 0;
    int right = nums.length - 1;
    while (left <= right) {
      int mid = left + ((right - left) >> 1);
      if (nums[mid] == target) return mid;
      if (nums[mid] < target) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
    return left;
  }
}
```

## Golang

```go
func searchInsert(nums []int, target int) int {
    left, right := 0, len(nums)-1
    for left <= right {
        mid := left + (right-left)/2
        if nums[mid] == target {
            return mid
        } else if nums[mid] < target {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }
    return left
}
```

## Ruby

```ruby
def search_insert(nums, target)
  left = 0
  right = nums.length
  while left < right
    mid = (left + right) / 2
    if nums[mid] < target
      left = mid + 1
    else
      right = mid
    end
  end
  left
end
```

## Scala

```scala
object Solution {
    def searchInsert(nums: Array[Int], target: Int): Int = {
        var left = 0
        var right = nums.length - 1
        while (left <= right) {
            val mid = left + (right - left) / 2
            if (nums(mid) == target) return mid
            else if (nums(mid) < target) left = mid + 1
            else right = mid - 1
        }
        left
    }
}
```

## Rust

```rust
impl Solution {
    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
        match nums.binary_search(&target) {
            Ok(idx) => idx as i32,
            Err(idx) => idx as i32,
        }
    }
}
```

## Racket

```racket
(define/contract (search-insert nums target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((vec (list->vector nums))
         (len (vector-length vec)))
    (let loop ((lo 0) (hi len))
      (if (= lo hi)
          lo
          (let* ((mid (quotient (+ lo hi) 2))
                 (mid-val (vector-ref vec mid)))
            (cond [(= target mid-val) mid]
                  [(< target mid-val) (loop lo mid)]
                  [else (loop (add1 mid) hi)]))))))
```

## Erlang

```erlang
-module(solution).
-export([search_insert/2]).

-spec search_insert(Nums :: [integer()], Target :: integer()) -> integer().
search_insert(Nums, Target) ->
    Len = length(Nums),
    bin_search(Nums, Target, 0, Len - 1).

bin_search(_Nums, _Target, Low, High) when Low > High ->
    Low;
bin_search(Nums, Target, Low, High) ->
    Mid = (Low + High) div 2,
    MidVal = lists:nth(Mid + 1, Nums),
    if
        Target == MidVal -> Mid;
        Target < MidVal -> bin_search(Nums, Target, Low, Mid - 1);
        true -> bin_search(Nums, Target, Mid + 1, High)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec search_insert(nums :: [integer], target :: integer) :: integer
  def search_insert(nums, target) do
    do_search(nums, target, 0, length(nums) - 1)
  end

  defp do_search(_nums, _target, low, high) when low > high, do: low

  defp do_search(nums, target, low, high) do
    mid = div(low + high, 2)

    case Enum.at(nums, mid) do
      val when val == target ->
        mid

      val when val < target ->
        do_search(nums, target, mid + 1, high)

      _val ->
        do_search(nums, target, low, mid - 1)
    end
  end
end
```
