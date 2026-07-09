# 0704. Binary Search

## Cpp

```cpp
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0, right = (int)nums.size() - 1;
        while (left <= right) {
            int mid = left + ((right - left) >> 1);
            if (nums[mid] == target) return mid;
            if (nums[mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        return -1;
    }
};
```

## Java

```java
class Solution {
    public int search(int[] nums, int target) {
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
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
```

## Python3

```python
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
```

## C

```c
int search(int* nums, int numsSize, int target) {
    int left = 0, right = numsSize - 1;
    while (left <= right) {
        int mid = left + ((right - left) >> 1);
        if (nums[mid] == target) return mid;
        else if (nums[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}
```

## Csharp

```csharp
public class Solution {
    public int Search(int[] nums, int target) {
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
        return -1;
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
var search = function(nums, target) {
    let left = 0;
    let right = nums.length - 1;
    while (left <= right) {
        const mid = left + ((right - left) >> 1);
        if (nums[mid] === target) return mid;
        if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
};
```

## Typescript

```typescript
function search(nums: number[], target: number): number {
    let left = 0;
    let right = nums.length - 1;
    while (left <= right) {
        const mid = left + ((right - left) >> 1);
        if (nums[mid] === target) return mid;
        if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
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
    function search($nums, $target) {
        $left = 0;
        $right = count($nums) - 1;
        while ($left <= $right) {
            $mid = intdiv($left + $right, 2);
            if ($nums[$mid] == $target) {
                return $mid;
            } elseif ($nums[$mid] < $target) {
                $left = $mid + 1;
            } else {
                $right = $mid - 1;
            }
        }
        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func search(_ nums: [Int], _ target: Int) -> Int {
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
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun search(nums: IntArray, target: Int): Int {
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
        return -1
    }
}
```

## Dart

```dart
class Solution {
  int search(List<int> nums, int target) {
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
    return -1;
  }
}
```

## Golang

```go
func search(nums []int, target int) int {
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
    return -1
}
```

## Ruby

```ruby
def search(nums, target)
  left = 0
  right = nums.length - 1
  while left <= right
    mid = left + ((right - left) >> 1)
    if nums[mid] == target
      return mid
    elsif nums[mid] < target
      left = mid + 1
    else
      right = mid - 1
    end
  end
  -1
end
```

## Scala

```scala
object Solution {
    def search(nums: Array[Int], target: Int): Int = {
        var left = 0
        var right = nums.length - 1
        while (left <= right) {
            val mid = left + (right - left) / 2
            if (nums(mid) == target) return mid
            else if (nums(mid) < target) left = mid + 1
            else right = mid - 1
        }
        -1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        if nums.is_empty() {
            return -1;
        }
        let mut left: i32 = 0;
        let mut right: i32 = (nums.len() as i32) - 1;
        while left <= right {
            let mid = left + ((right - left) >> 1);
            let val = nums[mid as usize];
            if val == target {
                return mid;
            } else if val < target {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        -1
    }
}
```

## Racket

```racket
(define/contract (search nums target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((vec (list->vector nums))
         (n   (vector-length vec)))
    (let loop ((left 0) (right (- n 1)))
      (if (> left right)
          -1
          (let ((mid (quotient (+ left right) 2))
                (mid-val (vector-ref vec (quotient (+ left right) 2))))
            (cond [(= mid-val target) mid]
                  [(< mid-val target) (loop (+ mid 1) right)]
                  [else               (loop left (- mid 1))]))))))
```

## Erlang

```erlang
-spec search(Nums :: [integer()], Target :: integer()) -> integer().
search(Nums, Target) ->
    search_helper(Nums, Target, 0, length(Nums) - 1).

search_helper(_Nums, _Target, Left, Right) when Left > Right ->
    -1;
search_helper(Nums, Target, Left, Right) ->
    Mid = (Left + Right) div 2,
    MidVal = lists:nth(Mid + 1, Nums),
    case MidVal of
        V when V == Target -> Mid;
        V when V < Target -> search_helper(Nums, Target, Mid + 1, Right);
        _ -> search_helper(Nums, Target, Left, Mid - 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec search(nums :: [integer], target :: integer) :: integer
  def search(nums, target) do
    do_search(nums, target, 0, length(nums) - 1)
  end

  defp do_search(_nums, _target, left, right) when left > right,
    do: -1

  defp do_search(nums, target, left, right) do
    mid = div(left + right, 2)

    case Enum.at(nums, mid) do
      ^target ->
        mid

      val when val < target ->
        do_search(nums, target, mid + 1, right)

      _val ->
        do_search(nums, target, left, mid - 1)
    end
  end
end
```
