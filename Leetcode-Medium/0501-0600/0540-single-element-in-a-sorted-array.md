# 0540. Single Element in a Sorted Array

## Cpp

```cpp
class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int lo = 0, hi = nums.size() - 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (mid % 2 == 1) --mid; // make mid even
            if (nums[mid] == nums[mid + 1])
                lo = mid + 2;
            else
                hi = mid;
        }
        return nums[lo];
    }
};
```

## Java

```java
class Solution {
    public int singleNonDuplicate(int[] nums) {
        int low = 0;
        int high = nums.length - 1;
        while (low < high) {
            int mid = (low + high) >>> 1; // avoid overflow
            if ((mid & 1) == 1) {
                mid--; // make mid even
            }
            if (nums[mid] == nums[mid + 1]) {
                low = mid + 2;
            } else {
                high = mid;
            }
        }
        return nums[low];
    }
}
```

## Python

```python
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            # make mid even so it aligns with the first of a pair
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                low = mid + 2
            else:
                high = mid
        return nums[low]
```

## Python3

```python
from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                low = mid + 2
            else:
                high = mid
        return nums[low]
```

## C

```c
int singleNonDuplicate(int* nums, int numsSize) {
    int low = 0;
    int high = numsSize - 1;
    while (low < high) {
        int mid = (low + high) / 2;
        if (mid % 2 == 1) {
            mid--; // make sure mid is even
        }
        if (nums[mid] == nums[mid + 1]) {
            low = mid + 2;
        } else {
            high = mid;
        }
    }
    return nums[low];
}
```

## Csharp

```csharp
public class Solution {
    public int SingleNonDuplicate(int[] nums) {
        int low = 0, high = nums.Length - 1;
        while (low < high) {
            int mid = low + ((high - low) >> 1);
            // Ensure mid is even
            if ((mid & 1) == 1) mid--;
            if (nums[mid] == nums[mid + 1]) {
                low = mid + 2;
            } else {
                high = mid;
            }
        }
        return nums[low];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNonDuplicate = function(nums) {
    let low = 0, high = nums.length - 1;
    while (low < high) {
        let mid = Math.floor((low + high) / 2);
        // Ensure we are at the first index of a pair
        if (mid % 2 === 1) mid--;
        if (nums[mid] === nums[mid + 1]) {
            low = mid + 2;
        } else {
            high = mid;
        }
    }
    return nums[low];
};
```

## Typescript

```typescript
function singleNonDuplicate(nums: number[]): number {
    let low = 0;
    let high = nums.length - 1;

    while (low < high) {
        let mid = Math.floor((low + high) / 2);
        // Ensure we are at the first index of a pair
        if (mid % 2 === 1) {
            mid--;
        }
        if (nums[mid] === nums[mid + 1]) {
            low = mid + 2;
        } else {
            high = mid;
        }
    }

    return nums[low];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function singleNonDuplicate($nums) {
        $n = count($nums);
        $low = 0;
        $high = $n - 1;
        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            if ($mid % 2 == 1) {
                $mid--;
            }
            if ($nums[$mid] === $nums[$mid + 1]) {
                $low = $mid + 2;
            } else {
                $high = $mid;
            }
        }
        return $nums[$low];
    }
}
```

## Swift

```swift
class Solution {
    func singleNonDuplicate(_ nums: [Int]) -> Int {
        var low = 0
        var high = nums.count - 1
        while low < high {
            var mid = (low + high) / 2
            if mid % 2 == 1 { mid -= 1 }
            if nums[mid] == nums[mid + 1] {
                low = mid + 2
            } else {
                high = mid
            }
        }
        return nums[low]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun singleNonDuplicate(nums: IntArray): Int {
        var low = 0
        var high = nums.size - 1
        while (low < high) {
            var mid = (low + high) ushr 1 // avoid overflow, unsigned shift for floor division by 2
            if (mid % 2 == 1) mid-- // make mid even
            if (nums[mid] == nums[mid + 1]) {
                low = mid + 2
            } else {
                high = mid
            }
        }
        return nums[low]
    }
}
```

## Dart

```dart
class Solution {
  int singleNonDuplicate(List<int> nums) {
    int low = 0;
    int high = nums.length - 1;
    while (low < high) {
      int mid = (low + high) >> 1;
      if ((mid & 1) == 1) {
        mid--;
      }
      if (nums[mid] == nums[mid + 1]) {
        low = mid + 2;
      } else {
        high = mid;
      }
    }
    return nums[low];
  }
}
```

## Golang

```go
func singleNonDuplicate(nums []int) int {
    lo, hi := 0, len(nums)-1
    for lo < hi {
        mid := (lo + hi) / 2
        if mid%2 == 1 {
            mid--
        }
        if nums[mid] == nums[mid+1] {
            lo = mid + 2
        } else {
            hi = mid
        }
    }
    return nums[lo]
}
```

## Ruby

```ruby
def single_non_duplicate(nums)
  left = 0
  right = nums.length - 1
  while left < right
    mid = (left + right) / 2
    mid -= 1 if mid.odd?
    if nums[mid] == nums[mid + 1]
      left = mid + 2
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
    def singleNonDuplicate(nums: Array[Int]): Int = {
        var low = 0
        var high = nums.length - 1
        while (low < high) {
            var mid = (low + high) / 2
            if (mid % 2 == 1) mid -= 1 // make mid even
            if (nums(mid) == nums(mid + 1)) {
                low = mid + 2
            } else {
                high = mid
            }
        }
        nums(low)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn single_non_duplicate(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n == 1 {
            return nums[0];
        }
        let mut lo = 0usize;
        let mut hi = n - 1;
        while lo < hi {
            let mid = (lo + hi) / 2;
            // make sure we compare a pair starting at an even index
            let m = if mid % 2 == 1 { mid - 1 } else { mid };
            if nums[m] == nums[m + 1] {
                lo = m + 2;
            } else {
                hi = m;
            }
        }
        nums[lo]
    }
}
```

## Racket

```racket
#lang racket

(define/contract (single-non-duplicate nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((v (list->vector nums))
         (n (vector-length v)))
    (let loop ((low 0) (high (- n 1)))
      (if (= low high)
          (vector-ref v low)
          (let* ((mid (quotient (+ low high) 2))
                 (mid (if (odd? mid) (- mid 1) mid))) ; ensure even index
            (if (= (vector-ref v mid) (vector-ref v (+ mid 1)))
                (loop (+ mid 2) high)
                (loop low mid)))))))
```

## Erlang

```erlang
-module(solution).
-export([single_non_duplicate/1]).

-spec single_non_duplicate(Nums :: [integer()]) -> integer().
single_non_duplicate(Nums) ->
    Tuple = list_to_tuple(Nums),
    Len = tuple_size(Tuple),
    binary_search(Tuple, 0, Len - 1).

binary_search(Tuple, Index, Index) ->
    element(Index + 1, Tuple);
binary_search(Tuple, Low, High) ->
    Mid = (Low + High) div 2,
    AdjMid = case Mid rem 2 of
                1 -> Mid - 1;
                0 -> Mid
            end,
    Elem = element(AdjMid + 1, Tuple),
    NextElem = element(AdjMid + 2, Tuple),
    if
        Elem == NextElem ->
            binary_search(Tuple, AdjMid + 2, High);
        true ->
            binary_search(Tuple, Low, AdjMid)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec single_non_duplicate(nums :: [integer]) :: integer
  def single_non_duplicate(nums) do
    arr = List.to_tuple(nums)
    len = tuple_size(arr)
    binary_search(arr, 0, len - 1)
  end

  defp binary_search(arr, low, high) when low == high do
    elem(arr, low)
  end

  defp binary_search(arr, low, high) do
    mid = div(low + high, 2)
    mid = if rem(mid, 2) == 1, do: mid - 1, else: mid

    if elem(arr, mid) == elem(arr, mid + 1) do
      binary_search(arr, mid + 2, high)
    else
      binary_search(arr, low, mid)
    end
  end
end
```
