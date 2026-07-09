# 0162. Find Peak Element

## Cpp

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int low = 0, high = (int)nums.size() - 1;
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (nums[mid] > nums[mid + 1]) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }
};
```

## Java

```java
class Solution {
    public int findPeakElement(int[] nums) {
        int left = 0, right = nums.length - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < nums[mid + 1]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
}
```

## Python

```python
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[mid + 1]:
                hi = mid
            else:
                lo = mid + 1
        return lo
```

## Python3

```python
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[mid + 1]:
                hi = mid
            else:
                lo = mid + 1
        return lo
```

## C

```c
int findPeakElement(int* nums, int numsSize) {
    int left = 0, right = numsSize - 1;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] < nums[mid + 1]) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return left;
}
```

## Csharp

```csharp
public class Solution {
    public int FindPeakElement(int[] nums) {
        int left = 0, right = nums.Length - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < nums[mid + 1]) {
                left = mid + 1;
            } else {
                right = mid;
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
 * @return {number}
 */
var findPeakElement = function(nums) {
    let left = 0, right = nums.length - 1;
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (nums[mid] > nums[mid + 1]) {
            // Peak is in the left half including mid
            right = mid;
        } else {
            // Peak is in the right half excluding mid
            left = mid + 1;
        }
    }
    return left;
};
```

## Typescript

```typescript
function findPeakElement(nums: number[]): number {
    let left = 0;
    let right = nums.length - 1;
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (nums[mid] > nums[mid + 1]) {
            right = mid;
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
     * @return Integer
     */
    function findPeakElement($nums) {
        $n = count($nums);
        if ($n === 1) {
            return 0;
        }
        $low = 0;
        $high = $n - 1;
        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            if ($nums[$mid] > $nums[$mid + 1]) {
                // Peak is on the left side (including mid)
                $high = $mid;
            } else {
                // Peak is on the right side
                $low = $mid + 1;
            }
        }
        return $low;
    }
}
```

## Swift

```swift
class Solution {
    func findPeakElement(_ nums: [Int]) -> Int {
        var left = 0
        var right = nums.count - 1
        while left < right {
            let mid = (left + right) / 2
            if nums[mid] > nums[mid + 1] {
                right = mid
            } else {
                left = mid + 1
            }
        }
        return left
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findPeakElement(nums: IntArray): Int {
        var left = 0
        var right = nums.size - 1
        while (left < right) {
            val mid = left + (right - left) / 2
            if (nums[mid] < nums[mid + 1]) {
                left = mid + 1
            } else {
                right = mid
            }
        }
        return left
    }
}
```

## Dart

```dart
class Solution {
  int findPeakElement(List<int> nums) {
    int low = 0;
    int high = nums.length - 1;
    while (low < high) {
      int mid = (low + high) ~/ 2;
      if (nums[mid] > nums[mid + 1]) {
        high = mid;
      } else {
        low = mid + 1;
      }
    }
    return low;
  }
}
```

## Golang

```go
func findPeakElement(nums []int) int {
    left, right := 0, len(nums)-1
    for left < right {
        mid := (left + right) / 2
        if nums[mid] > nums[mid+1] {
            right = mid
        } else {
            left = mid + 1
        }
    }
    return left
}
```

## Ruby

```ruby
def find_peak_element(nums)
  left = 0
  right = nums.length - 1
  while left < right
    mid = (left + right) / 2
    if nums[mid] < nums[mid + 1]
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
    def findPeakElement(nums: Array[Int]): Int = {
        var left = 0
        var right = nums.length - 1
        while (left < right) {
            val mid = left + (right - left) / 2
            if (nums(mid) < nums(mid + 1)) {
                left = mid + 1
            } else {
                right = mid
            }
        }
        left
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_peak_element(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n == 1 {
            return 0;
        }
        let mut low = 0usize;
        let mut high = n - 1;
        while low < high {
            let mid = low + (high - low) / 2;
            if nums[mid] > nums[mid + 1] {
                // peak is in left part including mid
                high = mid;
            } else {
                // peak is in right part excluding mid
                low = mid + 1;
            }
        }
        low as i32
    }
}
```

## Racket

```racket
(define/contract (find-peak-element nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((vec (list->vector nums))
         (n (vector-length vec)))
    (let loop ((low 0) (high (- n 1)))
      (if (= low high)
          low
          (let ((mid (quotient (+ low high) 2)))
            (if (< (vector-ref vec mid) (vector-ref vec (+ mid 1)))
                (loop (+ mid 1) high)
                (loop low mid)))))))
```

## Erlang

```erlang
-module(solution).
-export([find_peak_element/1]).

-spec find_peak_element(Nums :: [integer()]) -> integer().
find_peak_element(Nums) ->
    Tuple = list_to_tuple(Nums),
    N = tuple_size(Tuple),
    find_peak(Tuple, N, 0, N - 1).

find_peak(_Tuple, _N, Low, High) when Low > High ->
    Low;
find_peak(Tuple, N, Low, High) ->
    Mid = (Low + High) div 2,
    MidIdx = Mid + 1,
    MidVal = element(MidIdx, Tuple),
    LeftVal = if
        Mid > 0 -> element(MidIdx - 1, Tuple);
        true -> -2147483649
    end,
    RightVal = if
        Mid < N - 1 -> element(MidIdx + 1, Tuple);
        true -> -2147483649
    end,
    if
        Mid > 0, MidVal < LeftVal ->
            find_peak(Tuple, N, Low, Mid - 1);
        Mid < N - 1, MidVal < RightVal ->
            find_peak(Tuple, N, Mid + 1, High);
        true ->
            Mid
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_peak_element(nums :: [integer]) :: integer
  def find_peak_element(nums) do
    bs(nums, 0, length(nums) - 1)
  end

  defp bs(_nums, low, high) when low == high, do: low

  defp bs(nums, low, high) do
    mid = div(low + high, 2)

    if Enum.at(nums, mid) > Enum.at(nums, mid + 1) do
      bs(nums, low, mid)
    else
      bs(nums, mid + 1, high)
    end
  end
end
```
