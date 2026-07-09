# 0154. Find Minimum in Rotated Sorted Array II

## Cpp

```cpp
class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0, right = (int)nums.size() - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else if (nums[mid] < nums[right]) {
                right = mid;
            } else { // nums[mid] == nums[right]
                --right;
            }
        }
        return nums[left];
    }
};
```

## Java

```java
class Solution {
    public int findMin(int[] nums) {
        int left = 0, right = nums.length - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else if (nums[mid] < nums[right]) {
                right = mid;
            } else { // nums[mid] == nums[right]
                right--; // shrink the search space
            }
        }
        return nums[left];
    }
}
```

## Python

```python
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        return nums[left]
```

## Python3

```python
class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        return nums[left]
```

## C

```c
int findMin(int* nums, int numsSize) {
    int left = 0, right = numsSize - 1;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] > nums[right]) {
            left = mid + 1;
        } else if (nums[mid] < nums[right]) {
            right = mid;
        } else {
            // nums[mid] == nums[right], cannot decide, shrink right
            right--;
        }
    }
    return nums[left];
}
```

## Csharp

```csharp
public class Solution {
    public int FindMin(int[] nums) {
        int left = 0, right = nums.Length - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else if (nums[mid] < nums[right]) {
                right = mid;
            } else {
                right--;
            }
        }
        return nums[left];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    let left = 0, right = nums.length - 1;
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (nums[mid] > nums[right]) {
            left = mid + 1;
        } else if (nums[mid] < nums[right]) {
            right = mid;
        } else {
            // nums[mid] == nums[right], cannot decide, shrink right
            right--;
        }
    }
    return nums[left];
};
```

## Typescript

```typescript
function findMin(nums: number[]): number {
    let left = 0;
    let right = nums.length - 1;
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (nums[mid] > nums[right]) {
            left = mid + 1;
        } else if (nums[mid] < nums[right]) {
            right = mid;
        } else {
            right--;
        }
    }
    return nums[left];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findMin($nums) {
        $left = 0;
        $right = count($nums) - 1;
        while ($left < $right) {
            $mid = intdiv($left + $right, 2);
            if ($nums[$mid] > $nums[$right]) {
                $left = $mid + 1;
            } elseif ($nums[$mid] < $nums[$right]) {
                $right = $mid;
            } else {
                $right--;
            }
        }
        return $nums[$left];
    }
}
```

## Swift

```swift
class Solution {
    func findMin(_ nums: [Int]) -> Int {
        var left = 0
        var right = nums.count - 1
        while left < right {
            let mid = left + (right - left) / 2
            if nums[mid] > nums[right] {
                left = mid + 1
            } else if nums[mid] < nums[right] {
                right = mid
            } else {
                right -= 1
            }
        }
        return nums[left]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findMin(nums: IntArray): Int {
        var left = 0
        var right = nums.size - 1
        while (left < right) {
            val mid = left + (right - left) / 2
            when {
                nums[mid] > nums[right] -> left = mid + 1
                nums[mid] < nums[right] -> right = mid
                else -> right-- // nums[mid] == nums[right]
            }
        }
        return nums[left]
    }
}
```

## Dart

```dart
class Solution {
  int findMin(List<int> nums) {
    int left = 0;
    int right = nums.length - 1;
    while (left < right) {
      int mid = left + ((right - left) >> 1);
      if (nums[mid] > nums[right]) {
        left = mid + 1;
      } else if (nums[mid] < nums[right]) {
        right = mid;
      } else {
        // nums[mid] == nums[right], cannot decide, shrink right
        right--;
      }
    }
    return nums[left];
  }
}
```

## Golang

```go
func findMin(nums []int) int {
    left, right := 0, len(nums)-1
    for left < right {
        mid := left + (right-left)/2
        if nums[mid] > nums[right] {
            left = mid + 1
        } else if nums[mid] < nums[right] {
            right = mid
        } else {
            right--
        }
    }
    return nums[left]
}
```

## Ruby

```ruby
def find_min(nums)
  left = 0
  right = nums.length - 1
  while left < right
    mid = left + (right - left) / 2
    if nums[mid] > nums[right]
      left = mid + 1
    elsif nums[mid] < nums[right]
      right = mid
    else
      right -= 1
    end
  end
  nums[left]
end
```

## Scala

```scala
object Solution {
    def findMin(nums: Array[Int]): Int = {
        var left = 0
        var right = nums.length - 1
        while (left < right) {
            val mid = left + (right - left) / 2
            if (nums(mid) > nums(right)) {
                left = mid + 1
            } else if (nums(mid) < nums(right)) {
                right = mid
            } else {
                // nums[mid] == nums[right], cannot decide, shrink right
                right -= 1
            }
        }
        nums(left)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_min(nums: Vec<i32>) -> i32 {
        let mut left = 0usize;
        let mut right = nums.len() - 1;
        while left < right {
            let mid = left + (right - left) / 2;
            if nums[mid] > nums[right] {
                left = mid + 1;
            } else if nums[mid] < nums[right] {
                right = mid;
            } else {
                // nums[mid] == nums[right], cannot determine the side; shrink right
                right -= 1;
            }
        }
        nums[left]
    }
}
```

## Racket

```racket
(define/contract (find-min nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((v (list->vector nums))
         (n (vector-length v)))
    (let loop ((low 0) (high (- n 1)))
      (if (= low high)
          (vector-ref v low)
          (let* ((mid (quotient (+ low high) 2))
                 (mid-val (vector-ref v mid))
                 (high-val (vector-ref v high)))
            (cond
              [(> mid-val high-val) (loop (+ mid 1) high)]
              [(< mid-val high-val) (loop low mid)]
              [else (loop low (- high 1))]))))))
```

## Erlang

```erlang
-spec find_min(Nums :: [integer()]) -> integer().
find_min(Nums) ->
    Tuple = list_to_tuple(Nums),
    Len = tuple_size(Tuple),
    find_min_loop(0, Len - 1, Tuple).

find_min_loop(Low, High, Tuple) when Low < High ->
    Mid = (Low + High) div 2,
    MidVal = element(Mid + 1, Tuple),
    HighVal = element(High + 1, Tuple),
    if
        MidVal > HighVal ->
            find_min_loop(Mid + 1, High, Tuple);
        MidVal < HighVal ->
            find_min_loop(Low, Mid, Tuple);
        true ->
            find_min_loop(Low, High - 1, Tuple)
    end;
find_min_loop(Index, Index, Tuple) ->
    element(Index + 1, Tuple).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_min(nums :: [integer]) :: integer
  def find_min(nums) do
    arr = List.to_tuple(nums)
    binary_search(arr, 0, tuple_size(arr) - 1)
  end

  defp binary_search(arr, l, r) when l == r, do: elem(arr, l)

  defp binary_search(arr, l, r) do
    mid = div(l + r, 2)
    mid_val = elem(arr, mid)
    right_val = elem(arr, r)

    cond do
      mid_val > right_val ->
        binary_search(arr, mid + 1, r)

      mid_val < right_val ->
        binary_search(arr, l, mid)

      true ->
        binary_search(arr, l, r - 1)
    end
  end
end
```
