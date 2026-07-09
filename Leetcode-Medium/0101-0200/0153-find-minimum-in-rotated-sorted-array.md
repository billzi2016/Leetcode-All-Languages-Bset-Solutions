# 0153. Find Minimum in Rotated Sorted Array

## Cpp

```cpp
class Solution {
public:
    int findMin(std::vector<int>& nums) {
        int left = 0, right = (int)nums.size() - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else {
                right = mid;
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
            } else {
                right = mid;
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
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]
```

## Python3

```python
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]
```

## C

```c
int findMin(int* nums, int numsSize) {
    int left = 0;
    int right = numsSize - 1;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] > nums[right]) {
            left = mid + 1;
        } else {
            right = mid;
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
            } else {
                right = mid;
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
        if (nums[left] < nums[right]) return nums[left];
        const mid = Math.floor((left + right) / 2);
        if (nums[mid] >= nums[left]) {
            left = mid + 1;
        } else {
            right = mid;
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
        } else {
            right = mid;
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
            } else {
                $right = $mid;
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
            } else {
                right = mid
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
            if (nums[left] < nums[right]) return nums[left]
            val mid = left + (right - left) / 2
            if (nums[mid] >= nums[left]) {
                left = mid + 1
            } else {
                right = mid
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
    int left = 0, right = nums.length - 1;
    while (left < right) {
      int mid = left + ((right - left) >> 1);
      if (nums[mid] > nums[right]) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }
    return nums[left];
  }
}
```

## Golang

```go
func findMin(nums []int) int {
    lo, hi := 0, len(nums)-1
    for lo < hi {
        mid := lo + (hi-lo)/2
        if nums[mid] > nums[hi] {
            lo = mid + 1
        } else {
            hi = mid
        }
    }
    return nums[lo]
}
```

## Ruby

```ruby
def find_min(nums)
  left = 0
  right = nums.length - 1
  while left < right
    mid = (left + right) / 2
    if nums[mid] > nums[right]
      left = mid + 1
    else
      right = mid
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
            } else {
                right = mid
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
            if nums[left] < nums[right] {
                return nums[left];
            }
            let mid = left + (right - left) / 2;
            if nums[mid] >= nums[left] {
                left = mid + 1;
            } else {
                right = mid;
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
    (let loop ((lo 0) (hi (- n 1)))
      (if (= lo hi)
          (vector-ref v lo)
          (let ((mid (quotient (+ lo hi) 2)))
            (if (> (vector-ref v mid) (vector-ref v hi))
                (loop (+ mid 1) hi)
                (loop lo mid)))))))
```

## Erlang

```erlang
-module(solution).
-export([find_min/1]).

-spec find_min(Nums :: [integer()]) -> integer().
find_min(Nums) ->
    Tuple = list_to_tuple(Nums),
    Len = tuple_size(Tuple),
    find_min_binary(Tuple, 1, Len).

find_min_binary(T, L, R) when L == R ->
    element(L, T);
find_min_binary(T, L, R) ->
    Mid = (L + R) div 2,
    MidVal = element(Mid, T),
    RightVal = element(R, T),
    if
        MidVal > RightVal ->
            find_min_binary(T, Mid + 1, R);
        true ->
            find_min_binary(T, L, Mid)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_min(nums :: [integer]) :: integer
  def find_min(nums) do
    binary_search(nums, 0, length(nums) - 1)
  end

  defp binary_search(_nums, low, high) when low == high,
    do: Enum.at(_nums, low)

  defp binary_search(nums, low, high) do
    mid = div(low + high, 2)

    if Enum.at(nums, mid) > Enum.at(nums, high) do
      binary_search(nums, mid + 1, high)
    else
      binary_search(nums, low, mid)
    end
  end
end
```
