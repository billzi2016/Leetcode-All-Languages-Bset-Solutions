# 0016. 3Sum Closest

## Cpp

```cpp
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int best = nums[0] + nums[1] + nums[2];
        for (int i = 0; i < n - 2; ++i) {
            int left = i + 1, right = n - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (abs(sum - target) < abs(best - target)) {
                    best = sum;
                }
                if (sum == target) return target;
                else if (sum < target) ++left;
                else --right;
            }
        }
        return best;
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int n = nums.length;
        int closest = nums[0] + nums[1] + nums[2];
        for (int i = 0; i < n - 2; i++) {
            int left = i + 1, right = n - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (Math.abs(sum - target) < Math.abs(closest - target)) {
                    closest = sum;
                }
                if (sum == target) {
                    return target;
                } else if (sum < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }
        return closest;
    }
}
```

## Python

```python
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        best = nums[0] + nums[1] + nums[2]
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if abs(cur_sum - target) < abs(best - target):
                    best = cur_sum
                if cur_sum == target:
                    return cur_sum
                elif cur_sum < target:
                    left += 1
                else:
                    right -= 1
        return best
```

## Python3

```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if abs(cur_sum - target) < abs(closest - target):
                    closest = cur_sum
                if cur_sum == target:
                    return target
                elif cur_sum < target:
                    left += 1
                else:
                    right -= 1
        return closest
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    return (*(const int *)a) - (*(const int *)b);
}

int threeSumClosest(int* nums, int numsSize, int target) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmp_int);
    
    int best = nums[0] + nums[1] + nums[2];
    for (int i = 0; i < numsSize - 2; ++i) {
        int left = i + 1;
        int right = numsSize - 1;
        while (left < right) {
            int sum = nums[i] + nums[left] + nums[right];
            if (abs(sum - target) < abs(best - target)) {
                best = sum;
            }
            if (sum == target) {
                return target;
            } else if (sum < target) {
                ++left;
            } else {
                --right;
            }
        }
    }
    return best;
}
```

## Csharp

```csharp
public class Solution
{
    public int ThreeSumClosest(int[] nums, int target)
    {
        System.Array.Sort(nums);
        int n = nums.Length;
        int closestSum = nums[0] + nums[1] + nums[2];
        for (int i = 0; i < n - 2; i++)
        {
            int left = i + 1;
            int right = n - 1;
            while (left < right)
            {
                int currentSum = nums[i] + nums[left] + nums[right];
                if (currentSum == target)
                    return target;

                if (System.Math.Abs(currentSum - target) < System.Math.Abs(closestSum - target))
                    closestSum = currentSum;

                if (currentSum < target)
                    left++;
                else
                    right--;
            }
        }
        return closestSum;
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
var threeSumClosest = function(nums, target) {
    nums.sort((a, b) => a - b);
    let n = nums.length;
    let closest = nums[0] + nums[1] + nums[2];
    
    for (let i = 0; i < n - 2; i++) {
        // Optional skip duplicates for slight optimization
        if (i > 0 && nums[i] === nums[i - 1]) continue;
        
        let left = i + 1;
        let right = n - 1;
        while (left < right) {
            const sum = nums[i] + nums[left] + nums[right];
            if (Math.abs(sum - target) < Math.abs(closest - target)) {
                closest = sum;
            }
            if (sum === target) {
                return sum; // exact match
            } else if (sum < target) {
                left++;
                while (left < right && nums[left] === nums[left - 1]) left++; // skip dup
            } else {
                right--;
                while (left < right && nums[right] === nums[right + 1]) right--; // skip dup
            }
        }
    }
    
    return closest;
};
```

## Typescript

```typescript
function threeSumClosest(nums: number[], target: number): number {
    nums.sort((a, b) => a - b);
    let n = nums.length;
    let closest = nums[0] + nums[1] + nums[2];
    for (let i = 0; i < n - 2; i++) {
        let left = i + 1;
        let right = n - 1;
        while (left < right) {
            const sum = nums[i] + nums[left] + nums[right];
            if (Math.abs(sum - target) < Math.abs(closest - target)) {
                closest = sum;
            }
            if (sum === target) {
                return target;
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
    }
    return closest;
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
    function threeSumClosest($nums, $target) {
        sort($nums);
        $n = count($nums);
        $closest = $nums[0] + $nums[1] + $nums[2];
        for ($i = 0; $i < $n - 2; $i++) {
            $left = $i + 1;
            $right = $n - 1;
            while ($left < $right) {
                $sum = $nums[$i] + $nums[$left] + $nums[$right];
                if (abs($sum - $target) < abs($closest - $target)) {
                    $closest = $sum;
                }
                if ($sum == $target) {
                    return $target;
                } elseif ($sum < $target) {
                    $left++;
                } else {
                    $right--;
                }
            }
        }
        return $closest;
    }
}
```

## Swift

```swift
class Solution {
    func threeSumClosest(_ nums: [Int], _ target: Int) -> Int {
        let sorted = nums.sorted()
        var closest = sorted[0] + sorted[1] + sorted[2]
        for i in 0..<(sorted.count - 2) {
            var left = i + 1
            var right = sorted.count - 1
            while left < right {
                let sum = sorted[i] + sorted[left] + sorted[right]
                if abs(sum - target) < abs(closest - target) {
                    closest = sum
                }
                if sum == target {
                    return target
                } else if sum < target {
                    left += 1
                } else {
                    right -= 1
                }
            }
        }
        return closest
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun threeSumClosest(nums: IntArray, target: Int): Int {
        nums.sort()
        var closest = nums[0] + nums[1] + nums[2]
        for (i in 0 until nums.size - 2) {
            var left = i + 1
            var right = nums.lastIndex
            while (left < right) {
                val sum = nums[i] + nums[left] + nums[right]
                if (kotlin.math.abs(sum - target) < kotlin.math.abs(closest - target)) {
                    closest = sum
                }
                when {
                    sum == target -> return sum
                    sum < target -> left++
                    else -> right--
                }
            }
        }
        return closest
    }
}
```

## Dart

```dart
class Solution {
  int threeSumClosest(List<int> nums, int target) {
    nums.sort();
    int n = nums.length;
    int closest = nums[0] + nums[1] + nums[2];
    for (int i = 0; i < n - 2; i++) {
      int left = i + 1;
      int right = n - 1;
      while (left < right) {
        int sum = nums[i] + nums[left] + nums[right];
        if ((sum - target).abs() < (closest - target).abs()) {
          closest = sum;
        }
        if (sum == target) {
          return target;
        } else if (sum < target) {
          left++;
        } else {
          right--;
        }
      }
    }
    return closest;
  }
}
```

## Golang

```go
import "sort"

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func threeSumClosest(nums []int, target int) int {
	sort.Ints(nums)
	n := len(nums)
	closest := nums[0] + nums[1] + nums[2]

	for i := 0; i < n-2; i++ {
		l, r := i+1, n-1
		for l < r {
			sum := nums[i] + nums[l] + nums[r]
			if abs(sum-target) < abs(closest-target) {
				closest = sum
			}
			if sum == target {
				return sum
			} else if sum < target {
				l++
			} else {
				r--
			}
		}
	}
	return closest
}
```

## Ruby

```ruby
def three_sum_closest(nums, target)
  nums.sort!
  n = nums.length
  closest = nums[0] + nums[1] + nums[2]
  (0...n - 2).each do |i|
    left = i + 1
    right = n - 1
    while left < right
      sum = nums[i] + nums[left] + nums[right]
      if (sum - target).abs < (closest - target).abs
        closest = sum
      end
      if sum == target
        return target
      elsif sum < target
        left += 1
      else
        right -= 1
      end
    end
  end
  closest
end
```

## Scala

```scala
object Solution {
    def threeSumClosest(nums: Array[Int], target: Int): Int = {
        val sorted = nums.sorted
        var closestSum = sorted(0) + sorted(1) + sorted(2)
        var minDiff = math.abs(closestSum - target)

        for (i <- 0 until sorted.length - 2) {
            var left = i + 1
            var right = sorted.length - 1

            while (left < right) {
                val sum = sorted(i) + sorted(left) + sorted(right)
                val diff = math.abs(sum - target)

                if (diff < minDiff) {
                    minDiff = diff
                    closestSum = sum
                }

                if (sum == target) return sum
                else if (sum < target) left += 1
                else right -= 1
            }
        }

        closestSum
    }
}
```

## Rust

```rust
impl Solution {
    pub fn three_sum_closest(mut nums: Vec<i32>, target: i32) -> i32 {
        nums.sort();
        let n = nums.len();
        let mut closest = nums[0] + nums[1] + nums[2];
        for i in 0..n - 2 {
            let mut left = i + 1;
            let mut right = n - 1;
            while left < right {
                let sum = nums[i] + nums[left] + nums[right];
                if (sum - target).abs() < (closest - target).abs() {
                    closest = sum;
                }
                if sum == target {
                    return target;
                } else if sum < target {
                    left += 1;
                } else {
                    right -= 1;
                }
            }
        }
        closest
    }
}
```

## Racket

```racket
(define/contract (three-sum-closest nums target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((sorted (list->vector (sort nums <)))
         (n (vector-length sorted))
         (initial (+ (vector-ref sorted 0)
                     (vector-ref sorted 1)
                     (vector-ref sorted 2))))
    (let loop-i ((i 0) (best initial))
      (if (>= i (- n 2))
          best
          (let inner-loop ((left (+ i 1)) (right (- n 1)) (cur-best best))
            (cond
              [(> left right)
               (loop-i (+ i 1) cur-best)]
              [else
               (define s (+ (vector-ref sorted i)
                            (vector-ref sorted left)
                            (vector-ref sorted right)))
               (define new-best (if (< (abs (- s target))
                                      (abs (- cur-best target))) s cur-best))
               (if (> s target)
                   (inner-loop left (- right 1) new-best)
                   (inner-loop (+ left 1) right new-best))]))))))
```

## Erlang

```erlang
-module(solution).
-export([three_sum_closest/2]).

-spec three_sum_closest(Nums :: [integer()], Target :: integer()) -> integer().
three_sum_closest(Nums, Target) ->
    Sorted = lists:sort(Nums),
    T = list_to_tuple(Sorted),
    Len = tuple_size(T),
    InitSum = element(1, T) + element(2, T) + element(3, T),
    loop_i(1, Len - 2, T, Target, InitSum).

loop_i(I, MaxI, _T, _Target, BestSum) when I > MaxI ->
    BestSum;
loop_i(I, MaxI, T, Target, BestSum) ->
    A = element(I, T),
    NewBest = loop_lr(A, I + 1, tuple_size(T), T, Target, BestSum),
    loop_i(I + 1, MaxI, T, Target, NewBest).

loop_lr(_A, Left, Right, _T, _Target, BestSum) when Left >= Right ->
    BestSum;
loop_lr(A, Left, Right, T, Target, BestSum) ->
    B = element(Left, T),
    C = element(Right, T),
    Sum = A + B + C,
    NewBest = if
        erlang:abs(Sum - Target) < erlang:abs(BestSum - Target) -> Sum;
        true -> BestSum
    end,
    case Sum of
        _ when Sum == Target ->
            NewBest; % exact match, stop this inner loop
        _ when Sum < Target ->
            loop_lr(A, Left + 1, Right, T, Target, NewBest);
        _ ->
            loop_lr(A, Left, Right - 1, T, Target, NewBest)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec three_sum_closest(nums :: [integer], target :: integer) :: integer
  def three_sum_closest(nums, target) do
    arr = nums |> Enum.sort() |> List.to_tuple()
    n = tuple_size(arr)

    init_best = elem(arr, 0) + elem(arr, 1) + elem(arr, 2)

    {best_sum, _} =
      0..(n - 3)
      |> Enum.reduce({init_best, abs(init_best - target)}, fn i, {best, diff} ->
        a = elem(arr, i)
        two_pointer(i + 1, n - 1, a, arr, target, best, diff)
      end)

    best_sum
  end

  defp two_pointer(l, r, a, arr, target, best, diff) do
    if l >= r do
      {best, diff}
    else
      b = elem(arr, l)
      c = elem(arr, r)
      sum = a + b + c
      cur_diff = abs(sum - target)

      {new_best, new_diff} =
        if cur_diff < diff do
          {sum, cur_diff}
        else
          {best, diff}
        end

      cond do
        cur_diff == 0 ->
          {sum, 0}

        sum < target ->
          two_pointer(l + 1, r, a, arr, target, new_best, new_diff)

        true ->
          two_pointer(l, r - 1, a, arr, target, new_best, new_diff)
      end
    end
  end
end
```
