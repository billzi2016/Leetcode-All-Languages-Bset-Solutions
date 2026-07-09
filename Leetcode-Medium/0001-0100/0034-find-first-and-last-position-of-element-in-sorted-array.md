# 0034. Find First and Last Position of Element in Sorted Array

## Cpp

```cpp
class Solution {
public:
    int lowerBound(const vector<int>& nums, int target) {
        int lo = 0, hi = nums.size();
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] < target)
                lo = mid + 1;
            else
                hi = mid;
        }
        return lo;
    }
    
    int upperBound(const vector<int>& nums, int target) {
        int lo = 0, hi = nums.size();
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] <= target)
                lo = mid + 1;
            else
                hi = mid;
        }
        return lo;
    }
    
    vector<int> searchRange(vector<int>& nums, int target) {
        int n = nums.size();
        if (n == 0) return {-1, -1};
        int left = lowerBound(nums, target);
        if (left == n || nums[left] != target) return {-1, -1};
        int right = upperBound(nums, target) - 1;
        return {left, right};
    }
};
```

## Java

```java
class Solution {
    public int[] searchRange(int[] nums, int target) {
        int left = findBound(nums, target, true);
        if (left == -1) {
            return new int[]{-1, -1};
        }
        int right = findBound(nums, target, false);
        return new int[]{left, right};
    }

    private int findBound(int[] nums, int target, boolean first) {
        int lo = 0;
        int hi = nums.length - 1;
        int bound = -1;
        while (lo <= hi) {
            int mid = lo + ((hi - lo) >> 1);
            if (nums[mid] == target) {
                bound = mid;
                if (first) {
                    hi = mid - 1; // search left part
                } else {
                    lo = mid + 1; // search right part
                }
            } else if (nums[mid] < target) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return bound;
    }
}
```

## Python

```python
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def find_left():
            lo, hi = 0, len(nums) - 1
            ans = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] < target:
                    lo = mid + 1
                else:
                    if nums[mid] == target:
                        ans = mid
                    hi = mid - 1
            return ans

        def find_right():
            lo, hi = 0, len(nums) - 1
            ans = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] > target:
                    hi = mid - 1
                else:
                    if nums[mid] == target:
                        ans = mid
                    lo = mid + 1
            return ans

        left = find_left()
        right = find_right()
        return [left, right]
```

## Python3

```python
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]

        # Find first index >= target
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        left = lo

        # Check if target exists
        if left == n or nums[left] != target:
            return [-1, -1]

        # Find first index > target
        lo, hi = left, n
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        right = lo - 1

        return [left, right]
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* searchRange(int* nums, int numsSize, int target, int* returnSize) {
    int* result = (int*)malloc(2 * sizeof(int));
    *returnSize = 2;
    
    if (numsSize == 0) {
        result[0] = -1;
        result[1] = -1;
        return result;
    }
    
    // lower bound: first index >= target
    int left = 0, right = numsSize;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] < target)
            left = mid + 1;
        else
            right = mid;
    }
    
    if (left == numsSize || nums[left] != target) {
        result[0] = -1;
        result[1] = -1;
        return result;
    }
    
    int firstPos = left;
    
    // upper bound: first index > target
    left = 0; right = numsSize;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] <= target)
            left = mid + 1;
        else
            right = mid;
    }
    
    int lastPos = left - 1;
    
    result[0] = firstPos;
    result[1] = lastPos;
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int[] SearchRange(int[] nums, int target) {
        if (nums == null || nums.Length == 0) return new int[] { -1, -1 };
        
        int left = FindFirst(nums, target);
        if (left == -1) return new int[] { -1, -1 };
        int right = FindLast(nums, target);
        return new int[] { left, right };
    }
    
    private int FindFirst(int[] nums, int target) {
        int lo = 0, hi = nums.Length - 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] < target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return nums[lo] == target ? lo : -1;
    }
    
    private int FindLast(int[] nums, int target) {
        int lo = 0, hi = nums.Length - 1;
        while (lo < hi) {
            int mid = lo + (hi - lo + 1) / 2; // bias right
            if (nums[mid] > target) {
                hi = mid - 1;
            } else {
                lo = mid;
            }
        }
        return lo; // guaranteed to be target because left check succeeded
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    const n = nums.length;
    if (n === 0) return [-1, -1];
    
    // lower bound: first index >= target
    let left = 0, right = n;
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    const start = left;
    if (start === n || nums[start] !== target) return [-1, -1];
    
    // upper bound: first index > target
    left = start; right = n;
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (nums[mid] <= target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    const end = left - 1;
    
    return [start, end];
};
```

## Typescript

```typescript
function searchRange(nums: number[], target: number): number[] {
    const n = nums.length;
    if (n === 0) return [-1, -1];

    // Find first index >= target
    let left = 0, right = n; // [left, right)
    while (left < right) {
        const mid = left + ((right - left) >> 1);
        if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    const start = left;

    // If target not present
    if (start === n || nums[start] !== target) return [-1, -1];

    // Find first index > target
    left = 0; right = n;
    while (left < right) {
        const mid = left + ((right - left) >> 1);
        if (nums[mid] <= target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    const end = left - 1;

    return [start, end];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */
    function searchRange($nums, $target) {
        $n = count($nums);
        if ($n == 0) {
            return [-1, -1];
        }
        $start = $this->lowerBound($nums, $target);
        if ($start == $n || $nums[$start] != $target) {
            return [-1, -1];
        }
        $end = $this->upperBound($nums, $target) - 1;
        return [$start, $end];
    }

    private function lowerBound($nums, $target) {
        $left = 0;
        $right = count($nums);
        while ($left < $right) {
            $mid = intdiv($left + $right, 2);
            if ($nums[$mid] < $target) {
                $left = $mid + 1;
            } else {
                $right = $mid;
            }
        }
        return $left;
    }

    private function upperBound($nums, $target) {
        $left = 0;
        $right = count($nums);
        while ($left < $right) {
            $mid = intdiv($left + $right, 2);
            if ($nums[$mid] <= $target) {
                $left = $mid + 1;
            } else {
                $right = $mid;
            }
        }
        return $left;
    }
}
```

## Swift

```swift
class Solution {
    func searchRange(_ nums: [Int], _ target: Int) -> [Int] {
        let n = nums.count
        if n == 0 { return [-1, -1] }
        
        // Find first position >= target
        var left = 0
        var right = n
        while left < right {
            let mid = left + (right - left) / 2
            if nums[mid] < target {
                left = mid + 1
            } else {
                right = mid
            }
        }
        if left == n || nums[left] != target {
            return [-1, -1]
        }
        let start = left
        
        // Find first position > target
        left = 0
        right = n
        while left < right {
            let mid = left + (right - left) / 2
            if nums[mid] <= target {
                left = mid + 1
            } else {
                right = mid
            }
        }
        let end = left - 1
        
        return [start, end]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun searchRange(nums: IntArray, target: Int): IntArray {
        val n = nums.size
        var left = 0
        var right = n
        // Find first index >= target
        while (left < right) {
            val mid = left + (right - left) / 2
            if (nums[mid] < target) {
                left = mid + 1
            } else {
                right = mid
            }
        }
        if (left == n || nums[left] != target) return intArrayOf(-1, -1)
        val start = left

        // Find first index > target
        var l = start
        var r = n
        while (l < r) {
            val mid = l + (r - l) / 2
            if (nums[mid] <= target) {
                l = mid + 1
            } else {
                r = mid
            }
        }
        val end = l - 1
        return intArrayOf(start, end)
    }
}
```

## Dart

```dart
class Solution {
  List<int> searchRange(List<int> nums, int target) {
    int lowerBound() {
      int left = 0, right = nums.length;
      while (left < right) {
        int mid = left + ((right - left) >> 1);
        if (nums[mid] < target) {
          left = mid + 1;
        } else {
          right = mid;
        }
      }
      return left;
    }

    int upperBound() {
      int left = 0, right = nums.length;
      while (left < right) {
        int mid = left + ((right - left) >> 1);
        if (nums[mid] <= target) {
          left = mid + 1;
        } else {
          right = mid;
        }
      }
      return left;
    }

    int l = lowerBound();
    if (l == nums.length || nums[l] != target) {
      return [-1, -1];
    }
    int r = upperBound() - 1;
    return [l, r];
  }
}
```

## Golang

```go
func searchRange(nums []int, target int) []int {
    left := lowerBound(nums, target)
    if left == len(nums) || nums[left] != target {
        return []int{-1, -1}
    }
    right := upperBound(nums, target) - 1
    return []int{left, right}
}

func lowerBound(nums []int, target int) int {
    lo, hi := 0, len(nums)
    for lo < hi {
        mid := (lo + hi) >> 1
        if nums[mid] < target {
            lo = mid + 1
        } else {
            hi = mid
        }
    }
    return lo
}

func upperBound(nums []int, target int) int {
    lo, hi := 0, len(nums)
    for lo < hi {
        mid := (lo + hi) >> 1
        if nums[mid] <= target {
            lo = mid + 1
        } else {
            hi = mid
        }
    }
    return lo
}
```

## Ruby

```ruby
def search_range(nums, target)
  n = nums.length
  left = lower_bound(nums, target)
  return [-1, -1] if left == n || nums[left] != target
  right = upper_bound(nums, target) - 1
  [left, right]
end

def lower_bound(arr, target)
  l = 0
  r = arr.length
  while l < r
    m = (l + r) / 2
    if arr[m] < target
      l = m + 1
    else
      r = m
    end
  end
  l
end

def upper_bound(arr, target)
  l = 0
  r = arr.length
  while l < r
    m = (l + r) / 2
    if arr[m] <= target
      l = m + 1
    else
      r = m
    end
  end
  l
end
```

## Scala

```scala
object Solution {
    def searchRange(nums: Array[Int], target: Int): Array[Int] = {
        val n = nums.length
        if (n == 0) return Array(-1, -1)

        // lower bound: first index >= target
        var l = 0
        var r = n
        while (l < r) {
            val m = (l + r) >>> 1
            if (nums(m) < target) l = m + 1 else r = m
        }
        if (l == n || nums(l) != target) return Array(-1, -1)
        val first = l

        // upper bound: first index > target
        l = 0
        r = n
        while (l < r) {
            val m = (l + r) >>> 1
            if (nums(m) <= target) l = m + 1 else r = m
        }
        val last = l - 1

        Array(first, last)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn search_range(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let n = nums.len();
        if n == 0 {
            return vec![-1, -1];
        }
        // lower bound: first index >= target
        let mut lo = 0usize;
        let mut hi = n;
        while lo < hi {
            let mid = lo + (hi - lo) / 2;
            if nums[mid] < target {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        if lo == n || nums[lo] != target {
            return vec![-1, -1];
        }
        let left = lo as i32;

        // upper bound: first index > target
        lo = 0;
        hi = n;
        while lo < hi {
            let mid = lo + (hi - lo) / 2;
            if nums[mid] <= target {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        let right = (lo - 1) as i32;

        vec![left, right]
    }
}
```

## Racket

```racket
(define (lower-bound v target)
  (let loop ((lo 0) (hi (vector-length v)))
    (if (= lo hi)
        lo
        (let* ((mid (quotient (+ lo hi) 2))
               (mid-val (vector-ref v mid)))
          (if (< mid-val target)
              (loop (+ mid 1) hi)
              (loop lo mid))))))

(define (upper-bound v target)
  (let loop ((lo 0) (hi (vector-length v)))
    (if (= lo hi)
        lo
        (let* ((mid (quotient (+ lo hi) 2))
               (mid-val (vector-ref v mid)))
          (if (<= mid-val target)
              (loop (+ mid 1) hi)
              (loop lo mid))))))

(define/contract (search-range nums target)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let* ((v (list->vector nums))
         (n (vector-length v))
         (left (lower-bound v target)))
    (if (or (= left n) (not (= (vector-ref v left) target)))
        (list -1 -1)
        (let ((right (- (upper-bound v target) 1)))
          (list left right)))))
```

## Erlang

```erlang
-spec search_range(Nums :: [integer()], Target :: integer()) -> [integer()].
search_range(Nums, Target) ->
    Tuple = list_to_tuple(Nums),
    Len = tuple_size(Tuple),
    Left = lower_bound(Tuple, Target, Len),
    case (Left >= Len) orelse (element(Left + 1, Tuple) =/= Target) of
        true -> [-1, -1];
        false ->
            RightIdx = upper_bound(Tuple, Target, Len) - 1,
            [Left, RightIdx]
    end.

lower_bound(Tuple, Target, Len) ->
    lower_bound(Tuple, Target, 0, Len - 1, Len).

lower_bound(_Tuple, _Target, Low, High, Ans) when Low > High ->
    Ans;
lower_bound(Tuple, Target, Low, High, _Ans) ->
    Mid = (Low + High) div 2,
    Val = element(Mid + 1, Tuple),
    if
        Val < Target ->
            lower_bound(Tuple, Target, Mid + 1, High, Len);
        true ->
            lower_bound(Tuple, Target, Low, Mid - 1, Mid)
    end.

upper_bound(Tuple, Target, Len) ->
    upper_bound(Tuple, Target, 0, Len - 1, Len).

upper_bound(_Tuple, _Target, Low, High, Ans) when Low > High ->
    Ans;
upper_bound(Tuple, Target, Low, High, _Ans) ->
    Mid = (Low + High) div 2,
    Val = element(Mid + 1, Tuple),
    if
        Val =< Target ->
            upper_bound(Tuple, Target, Mid + 1, High, Len);
        true ->
            upper_bound(Tuple, Target, Low, Mid - 1, Mid)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec search_range(nums :: [integer], target :: integer) :: [integer]
  def search_range(nums, target) do
    arr = List.to_tuple(nums)
    len = tuple_size(arr)

    start_idx = lower_bound(arr, target, 0, len)

    if start_idx == len or elem(arr, start_idx) != target do
      [-1, -1]
    else
      end_idx = upper_bound(arr, target, 0, len) - 1
      [start_idx, end_idx]
    end
  end

  defp lower_bound(_arr, _target, low, high) when low >= high, do: low

  defp lower_bound(arr, target, low, high) do
    mid = div(low + high, 2)

    if elem(arr, mid) < target do
      lower_bound(arr, target, mid + 1, high)
    else
      lower_bound(arr, target, low, mid)
    end
  end

  defp upper_bound(_arr, _target, low, high) when low >= high, do: low

  defp upper_bound(arr, target, low, high) do
    mid = div(low + high, 2)

    if elem(arr, mid) <= target do
      upper_bound(arr, target, mid + 1, high)
    else
      upper_bound(arr, target, low, mid)
    end
  end
end
```
