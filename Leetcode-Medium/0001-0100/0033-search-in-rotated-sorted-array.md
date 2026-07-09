# 0033. Search in Rotated Sorted Array

## Cpp

```cpp
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int lo = 0, hi = (int)nums.size() - 1;
        while (lo <= hi) {
            int mid = lo + ((hi - lo) >> 1);
            if (nums[mid] == target) return mid;
            // Determine which side is properly sorted
            if (nums[lo] <= nums[mid]) { // left side sorted
                if (nums[lo] <= target && target < nums[mid])
                    hi = mid - 1;
                else
                    lo = mid + 1;
            } else { // right side sorted
                if (nums[mid] < target && target <= nums[hi])
                    lo = mid + 1;
                else
                    hi = mid - 1;
            }
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
            if (nums[mid] == target) return mid;
            if (nums[left] <= nums[mid]) { // left side is sorted
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else { // right side is sorted
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
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
            # Determine which side is properly sorted
            if nums[left] <= nums[mid]:
                # Left side is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Right side is sorted
                if nums[mid] < target <= nums[right]:
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
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
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
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) return mid;
        if (nums[left] <= nums[mid]) { // left half is sorted
            if (target >= nums[left] && target < nums[mid])
                right = mid - 1;
            else
                left = mid + 1;
        } else { // right half is sorted
            if (target > nums[mid] && target <= nums[right])
                left = mid + 1;
            else
                right = mid - 1;
        }
    }
    return -1;
}
```

## Csharp

```csharp
public class Solution {
    public int Search(int[] nums, int target) {
        int left = 0, right = nums.Length - 1;
        while (left <= right) {
            int mid = left + ((right - left) >> 1);
            if (nums[mid] == target) return mid;

            // Determine which side is properly sorted
            if (nums[left] <= nums[mid]) { // left half is sorted
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else { // right half is sorted
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
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
        const mid = Math.floor((left + right) / 2);
        if (nums[mid] === target) return mid;
        if (nums[left] <= nums[mid]) { // left half is sorted
            if (nums[left] <= target && target < nums[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        } else { // right half is sorted
            if (nums[mid] < target && target <= nums[right]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
    }
    return -1;
};
```

## Typescript

```typescript
function search(nums: number[], target: number): number {
    let left = 0, right = nums.length - 1;
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (nums[mid] === target) return mid;

        // Determine which side is properly sorted
        if (nums[left] <= nums[mid]) { // left half is sorted
            if (nums[left] <= target && target < nums[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        } else { // right half is sorted
            if (nums[mid] < target && target <= nums[right]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
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
            }
            // Determine which side is properly sorted
            if ($nums[$left] <= $nums[$mid]) { // left half is sorted
                if ($nums[$left] <= $target && $target < $nums[$mid]) {
                    $right = $mid - 1;
                } else {
                    $left = $mid + 1;
                }
            } else { // right half is sorted
                if ($nums[$mid] < $target && $target <= $nums[$right]) {
                    $left = $mid + 1;
                } else {
                    $right = $mid - 1;
                }
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
            let mid = (left + right) / 2
            if nums[mid] == target {
                return mid
            }
            
            // Determine which side is properly sorted
            if nums[left] <= nums[mid] { // Left half is sorted
                if target >= nums[left] && target < nums[mid] {
                    right = mid - 1
                } else {
                    left = mid + 1
                }
            } else { // Right half is sorted
                if target > nums[mid] && target <= nums[right] {
                    left = mid + 1
                } else {
                    right = mid - 1
                }
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
            if (nums[mid] == target) return mid
            if (nums[left] <= nums[mid]) {
                if (target >= nums[left] && target < nums[mid]) {
                    right = mid - 1
                } else {
                    left = mid + 1
                }
            } else {
                if (target > nums[mid] && target <= nums[right]) {
                    left = mid + 1
                } else {
                    right = mid - 1
                }
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
      if (nums[left] <= nums[mid]) {
        if (nums[left] <= target && target < nums[mid]) {
          right = mid - 1;
        } else {
          left = mid + 1;
        }
      } else {
        if (nums[mid] < target && target <= nums[right]) {
          left = mid + 1;
        } else {
          right = mid - 1;
        }
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
        mid := (left + right) / 2
        if nums[mid] == target {
            return mid
        }
        // Determine which side is properly sorted
        if nums[left] <= nums[mid] { // left half is sorted
            if nums[left] <= target && target < nums[mid] {
                right = mid - 1
            } else {
                left = mid + 1
            }
        } else { // right half is sorted
            if nums[mid] < target && target <= nums[right] {
                left = mid + 1
            } else {
                right = mid - 1
            }
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
    mid = (left + right) / 2
    return mid if nums[mid] == target
    if nums[left] <= nums[mid]
      if nums[left] <= target && target < nums[mid]
        right = mid - 1
      else
        left = mid + 1
      end
    else
      if nums[mid] < target && target <= nums[right]
        left = mid + 1
      else
        right = mid - 1
      end
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
            if (nums(left) <= nums(mid)) { // left side is sorted
                if (nums(left) <= target && target < nums(mid)) {
                    right = mid - 1
                } else {
                    left = mid + 1
                }
            } else { // right side is sorted
                if (nums(mid) < target && target <= nums(right)) {
                    left = mid + 1
                } else {
                    right = mid - 1
                }
            }
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
            let mid = left + ((right - left) / 2);
            let mid_val = nums[mid as usize];
            if mid_val == target {
                return mid;
            }
            if nums[left as usize] <= mid_val {
                // Left half is sorted
                if nums[left as usize] <= target && target < mid_val {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                // Right half is sorted
                if mid_val < target && target <= nums[right as usize] {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
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
  (let* ([v (list->vector nums)]
         [n (vector-length v)])
    (let loop ([low 0] [high (sub1 n)])
      (if (> low high)
          -1
          (let* ([mid (quotient (+ low high) 2)]
                 [midVal (vector-ref v mid)])
            (cond [(= midVal target) mid]
                  [(<= (vector-ref v low) midVal) ; left half is sorted
                   (if (and (>= target (vector-ref v low)) (< target midVal))
                       (loop low (sub1 mid))
                       (loop (add1 mid) high))]
                  [else ; right half is sorted
                   (if (and (> target midVal) (<= target (vector-ref v high)))
                       (loop (add1 mid) high)
                       (loop low (sub1 mid)))])))))))
```

## Erlang

```erlang
-spec search(Nums :: [integer()], Target :: integer()) -> integer().
search(Nums, Target) ->
    Tuple = list_to_tuple(Nums),
    Len = tuple_size(Tuple),
    binary_search(Tuple, 0, Len - 1, Target).

binary_search(_Tuple, Low, High, _Target) when Low > High ->
    -1;
binary_search(Tuple, Low, High, Target) ->
    Mid = (Low + High) div 2,
    MidVal = element(Mid + 1, Tuple),
    case MidVal of
        Target -> Mid;
        _ ->
            LowVal = element(Low + 1, Tuple),
            HighVal = element(High + 1, Tuple),
            if
                LowVal =< MidVal ->
                    (Target >= LowVal andalso Target < MidVal) ->
                        binary_search(Tuple, Low, Mid - 1, Target);
                    true ->
                        binary_search(Tuple, Mid + 1, High, Target)
                ;
                true -> % right half is sorted
                    (Target > MidVal andalso Target =< HighVal) ->
                        binary_search(Tuple, Mid + 1, High, Target);
                    true ->
                        binary_search(Tuple, Low, Mid - 1, Target)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec search(nums :: [integer], target :: integer) :: integer
  def search(nums, target) do
    arr = List.to_tuple(nums)
    n = tuple_size(arr)

    do_search(arr, target, 0, n - 1)
  end

  defp do_search(_arr, _target, low, high) when low > high, do: -1

  defp do_search(arr, target, low, high) do
    mid = div(low + high, 2)
    mid_val = elem(arr, mid)

    if mid_val == target do
      mid
    else
      low_val = elem(arr, low)
      high_val = elem(arr, high)

      cond do
        low_val <= mid_val ->
          if low_val <= target and target < mid_val do
            do_search(arr, target, low, mid - 1)
          else
            do_search(arr, target, mid + 1, high)
          end

        true ->
          if mid_val < target and target <= high_val do
            do_search(arr, target, mid + 1, high)
          else
            do_search(arr, target, low, mid - 1)
          end
      end
    end
  end
end
```
