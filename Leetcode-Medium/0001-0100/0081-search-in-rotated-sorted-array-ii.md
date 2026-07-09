# 0081. Search in Rotated Sorted Array II

## Cpp

```cpp
class Solution {
public:
    bool search(std::vector<int>& nums, int target) {
        int left = 0, right = (int)nums.size() - 1;
        while (left <= right) {
            int mid = left + ((right - left) >> 1);
            if (nums[mid] == target) return true;

            // If we cannot decide the sorted part because of duplicates
            if (nums[left] == nums[mid] && nums[mid] == nums[right]) {
                ++left;
                --right;
            }
            else if (nums[left] <= nums[mid]) { // left half is sorted
                if (nums[left] <= target && target < nums[mid])
                    right = mid - 1;
                else
                    left = mid + 1;
            } else { // right half is sorted
                if (nums[mid] < target && target <= nums[right])
                    left = mid + 1;
                else
                    right = mid - 1;
            }
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean search(int[] nums, int target) {
        int lo = 0, hi = nums.length - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] == target) return true;
            if (nums[lo] == nums[mid] && nums[mid] == nums[hi]) {
                lo++;
                hi--;
            } else if (nums[lo] <= nums[mid]) { // left side is sorted
                if (nums[lo] <= target && target < nums[mid]) {
                    hi = mid - 1;
                } else {
                    lo = mid + 1;
                }
            } else { // right side is sorted
                if (nums[mid] < target && target <= nums[hi]) {
                    lo = mid + 1;
                } else {
                    hi = mid - 1;
                }
            }
        }
        return false;
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
        :rtype: bool
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True

            # If we cannot determine the sorted part because of duplicates
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue

            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # Right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
```

## Python3

```python
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return True
            if nums[lo] < nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            elif nums[lo] > nums[mid]:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                lo += 1
        return False
```

## C

```c
#include <stdbool.h>

bool search(int* nums, int numsSize, int target) {
    int left = 0, right = numsSize - 1;
    while (left <= right) {
        int mid = left + ((right - left) >> 1);
        if (nums[mid] == target) return true;

        // If we cannot determine the sorted part because of duplicates
        if (nums[left] == nums[mid] && nums[mid] == nums[right]) {
            ++left;
            --right;
        }
        else if (nums[left] <= nums[mid]) { // left side is sorted
            if (nums[left] <= target && target < nums[mid])
                right = mid - 1;
            else
                left = mid + 1;
        } else { // right side is sorted
            if (nums[mid] < target && target <= nums[right])
                left = mid + 1;
            else
                right = mid - 1;
        }
    }
    return false;
}
```

## Csharp

```csharp
public class Solution {
    public bool Search(int[] nums, int target) {
        int left = 0, right = nums.Length - 1;
        while (left <= right) {
            int mid = left + ((right - left) >> 1);
            if (nums[mid] == target) return true;

            if (nums[left] == nums[mid] && nums[mid] == nums[right]) {
                left++;
                right--;
            } else if (nums[left] <= nums[mid]) { // left half is sorted
                if (nums[left] <= target && target < nums[mid])
                    right = mid - 1;
                else
                    left = mid + 1;
            } else { // right half is sorted
                if (nums[mid] < target && target <= nums[right])
                    left = mid + 1;
                else
                    right = mid - 1;
            }
        }
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {boolean}
 */
var search = function(nums, target) {
    let lo = 0, hi = nums.length - 1;
    while (lo <= hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (nums[mid] === target) return true;

        // If left half is sorted
        if (nums[lo] < nums[mid]) {
            if (nums[lo] <= target && target < nums[mid]) {
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        // If right half is sorted
        else if (nums[lo] > nums[mid]) {
            if (nums[mid] < target && target <= nums[hi]) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        // nums[lo] == nums[mid], cannot determine, shrink range
        else {
            lo++;
        }
    }
    return false;
};
```

## Typescript

```typescript
function search(nums: number[], target: number): boolean {
    let left = 0;
    let right = nums.length - 1;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (nums[mid] === target) return true;

        // If we cannot determine the sorted side because of duplicates
        if (nums[left] === nums[mid] && nums[mid] === nums[right]) {
            left++;
            right--;
            continue;
        }

        // Left half is sorted
        if (nums[left] <= nums[mid]) {
            if (nums[left] <= target && target < nums[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        } else { // Right half is sorted
            if (nums[mid] < target && target <= nums[right]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
    }

    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Boolean
     */
    function search($nums, $target) {
        $left = 0;
        $right = count($nums) - 1;

        while ($left <= $right) {
            $mid = intdiv($left + $right, 2);

            if ($nums[$mid] == $target) {
                return true;
            }

            // If we cannot determine the sorted part because of duplicates
            if ($nums[$left] == $nums[$mid] && $nums[$mid] == $nums[$right]) {
                $left++;
                $right--;
                continue;
            }

            // Left half is sorted
            if ($nums[$left] <= $nums[$mid]) {
                if ($nums[$left] <= $target && $target < $nums[$mid]) {
                    $right = $mid - 1;
                } else {
                    $left = $mid + 1;
                }
            } else { // Right half is sorted
                if ($nums[$mid] < $target && $target <= $nums[$right]) {
                    $left = $mid + 1;
                } else {
                    $right = $mid - 1;
                }
            }
        }

        return false;
    }
}
```

## Swift

```swift
class Solution {
    func search(_ nums: [Int], _ target: Int) -> Bool {
        var left = 0
        var right = nums.count - 1
        
        while left <= right {
            let mid = (left + right) / 2
            if nums[mid] == target { return true }
            
            // If we cannot determine the sorted part because of duplicates
            if nums[left] == nums[mid] && nums[mid] == nums[right] {
                left += 1
                right -= 1
                continue
            }
            
            // Left half is sorted
            if nums[left] <= nums[mid] {
                if nums[left] <= target && target < nums[mid] {
                    right = mid - 1
                } else {
                    left = mid + 1
                }
            } else { // Right half is sorted
                if nums[mid] < target && target <= nums[right] {
                    left = mid + 1
                } else {
                    right = mid - 1
                }
            }
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun search(nums: IntArray, target: Int): Boolean {
        var left = 0
        var right = nums.size - 1
        while (left <= right) {
            val mid = left + ((right - left) ushr 1)
            if (nums[mid] == target) return true

            // If we cannot determine the sorted part because of duplicates
            if (nums[left] == nums[mid]) {
                left++
                continue
            }

            // Left half is sorted
            if (nums[left] < nums[mid]) {
                if (target >= nums[left] && target < nums[mid]) {
                    right = mid - 1
                } else {
                    left = mid + 1
                }
            } else { // Right half is sorted
                if (target > nums[mid] && target <= nums[right]) {
                    left = mid + 1
                } else {
                    right = mid - 1
                }
            }
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool search(List<int> nums, int target) {
    int left = 0;
    int right = nums.length - 1;
    while (left <= right) {
      int mid = left + ((right - left) >> 1);
      if (nums[mid] == target) return true;

      // If duplicates blur the decision, shrink bounds
      if (nums[left] == nums[mid] && nums[mid] == nums[right]) {
        left++;
        right--;
        continue;
      }

      // Left half is sorted
      if (nums[left] <= nums[mid]) {
        if (nums[left] <= target && target < nums[mid]) {
          right = mid - 1;
        } else {
          left = mid + 1;
        }
      } else { // Right half is sorted
        if (nums[mid] < target && target <= nums[right]) {
          left = mid + 1;
        } else {
          right = mid - 1;
        }
      }
    }
    return false;
  }
}
```

## Golang

```go
func search(nums []int, target int) bool {
	lo, hi := 0, len(nums)-1
	for lo <= hi {
		mid := (lo + hi) / 2
		if nums[mid] == target {
			return true
		}
		if nums[lo] < nums[mid] { // left part sorted
			if nums[lo] <= target && target < nums[mid] {
				hi = mid - 1
			} else {
				lo = mid + 1
			}
		} else if nums[lo] > nums[mid] { // right part sorted
			if nums[mid] < target && target <= nums[hi] {
				lo = mid + 1
			} else {
				hi = mid - 1
			}
		} else { // nums[lo] == nums[mid], cannot determine, shrink left bound
			lo++
		}
	}
	return false
}
```

## Ruby

```ruby
def search(nums, target)
  left = 0
  right = nums.length - 1
  while left <= right
    mid = (left + right) / 2
    return true if nums[mid] == target

    if nums[left] == nums[mid] && nums[mid] == nums[right]
      left += 1
      right -= 1
    elsif nums[left] <= nums[mid] # left side is sorted
      if nums[left] <= target && target < nums[mid]
        right = mid - 1
      else
        left = mid + 1
      end
    else # right side is sorted
      if nums[mid] < target && target <= nums[right]
        left = mid + 1
      else
        right = mid - 1
      end
    end
  end
  false
end
```

## Scala

```scala
object Solution {
    def search(nums: Array[Int], target: Int): Boolean = {
        var left = 0
        var right = nums.length - 1

        while (left <= right) {
            val mid = left + (right - left) / 2
            if (nums(mid) == target) return true

            if (nums(left) < nums(mid)) { // left part is sorted
                if (nums(left) <= target && target < nums(mid))
                    right = mid - 1
                else
                    left = mid + 1
            } else if (nums(left) > nums(mid)) { // right part is sorted
                if (nums(mid) < target && target <= nums(right))
                    left = mid + 1
                else
                    right = mid - 1
            } else {
                // nums[left] == nums[mid], cannot determine the sorted side
                left += 1
            }
        }

        false
    }
}
```

## Rust

```rust
impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> bool {
        if nums.is_empty() {
            return false;
        }
        let mut lo: i32 = 0;
        let mut hi: i32 = (nums.len() as i32) - 1;

        while lo <= hi {
            let mid = lo + ((hi - lo) / 2);
            let m = nums[mid as usize];
            if m == target {
                return true;
            }

            // If we cannot determine the sorted part because of duplicates
            if nums[lo as usize] == m && m == nums[hi as usize] {
                lo += 1;
                hi -= 1;
                continue;
            }

            // Left side is sorted
            if nums[lo as usize] <= m {
                if nums[lo as usize] <= target && target < m {
                    hi = mid - 1;
                } else {
                    lo = mid + 1;
                }
            } else {
                // Right side is sorted
                if m < target && target <= nums[hi as usize] {
                    lo = mid + 1;
                } else {
                    hi = mid - 1;
                }
            }
        }

        false
    }
}
```

## Racket

```racket
(define/contract (search nums target)
  (-> (listof exact-integer?) exact-integer? boolean?)
  (let* ([v (list->vector nums)]
         [n (vector-length v)])
    (let loop ([low 0] [high (sub1 n)])
      (cond
        [(> low high) #f]
        [else
         (define mid (quotient (+ low high) 2))
         (define mid-val (vector-ref v mid))
         (cond
           [(= mid-val target) #t]
           [(and (= (vector-ref v low) mid-val)
                 (= (vector-ref v high) mid-val))
            (loop (add1 low) (sub1 high))]
           [(<= (vector-ref v low) mid-val) ; left side sorted
            (if (and (>= target (vector-ref v low)) (< target mid-val))
                (loop low (sub1 mid))
                (loop (add1 mid) high))]
           [else ; right side sorted
            (if (and (> target (vector-ref v mid)) (<= target (vector-ref v high)))
                (loop (add1 mid) high)
                (loop low (sub1 mid)))])]))))
```

## Erlang

```erlang
-module(solution).
-export([search/2]).

-spec search(Nums :: [integer()], Target :: integer()) -> boolean().
search(Nums, Target) ->
    Tuple = list_to_tuple(Nums),
    Len = tuple_size(Tuple),
    search_helper(Tuple, 0, Len - 1, Target).

search_helper(_, Low, High, _) when Low > High ->
    false;
search_helper(T, Low, High, Target) ->
    Mid = (Low + High) div 2,
    MidVal = element(Mid + 1, T),
    case MidVal == Target of
        true -> true;
        false ->
            LowVal = element(Low + 1, T),
            HighVal = element(High + 1, T),
            if
                LowVal == MidVal andalso MidVal == HighVal ->
                    search_helper(T, Low + 1, High - 1, Target);
                (LowVal =< MidVal) -> % left side is sorted
                    if
                        LowVal =< Target, Target < MidVal ->
                            search_helper(T, Low, Mid - 1, Target);
                        true ->
                            search_helper(T, Mid + 1, High, Target)
                    end;
                true -> % right side is sorted
                    if
                        MidVal < Target, Target =< HighVal ->
                            search_helper(T, Mid + 1, High, Target);
                        true ->
                            search_helper(T, Low, Mid - 1, Target)
                    end
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec search(nums :: [integer], target :: integer) :: boolean
  def search(nums, target) do
    arr = List.to_tuple(nums)
    helper(arr, target, 0, tuple_size(arr) - 1)
  end

  defp helper(_arr, _target, lo, hi) when lo > hi, do: false

  defp helper(arr, target, lo, hi) do
    mid = div(lo + hi, 2)
    val_mid = elem(arr, mid)

    cond do
      val_mid == target ->
        true

      elem(arr, lo) == val_mid and val_mid == elem(arr, hi) ->
        helper(arr, target, lo + 1, hi - 1)

      elem(arr, lo) <= val_mid ->
        if elem(arr, lo) <= target && target < val_mid do
          helper(arr, target, lo, mid - 1)
        else
          helper(arr, target, mid + 1, hi)
        end

      true ->
        if val_mid < target && target <= elem(arr, hi) do
          helper(arr, target, mid + 1, hi)
        else
          helper(arr, target, lo, mid - 1)
        end
    end
  end
end
```
