# 2563. Count the Number of Fair Pairs

## Cpp

```cpp
class Solution {
public:
    long long countFairPairs(std::vector<int>& nums, int lower, int upper) {
        std::sort(nums.begin(), nums.end());
        auto countLessThan = [&](long long target) -> long long {
            long long cnt = 0;
            int left = 0, right = (int)nums.size() - 1;
            while (left < right) {
                long long sum = static_cast<long long>(nums[left]) + nums[right];
                if (sum < target) {
                    cnt += right - left;
                    ++left;
                } else {
                    --right;
                }
            }
            return cnt;
        };
        return countLessThan((long long)upper + 1) - countLessThan(lower);
    }
};
```

## Java

```java
class Solution {
    public long countFairPairs(int[] nums, int lower, int upper) {
        java.util.Arrays.sort(nums);
        return countLessThan(nums, (long) upper + 1) - countLessThan(nums, (long) lower);
    }

    private long countLessThan(int[] nums, long bound) {
        int left = 0;
        int right = nums.length - 1;
        long cnt = 0;
        while (left < right) {
            long sum = (long) nums[left] + nums[right];
            if (sum < bound) {
                cnt += right - left;
                left++;
            } else {
                right--;
            }
        }
        return cnt;
    }
}
```

## Python

```python
class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)

        def count_less(bound):
            left, right = 0, n - 1
            cnt = 0
            while left < right:
                if nums[left] + nums[right] < bound:
                    cnt += (right - left)
                    left += 1
                else:
                    right -= 1
            return cnt

        return count_less(upper + 1) - count_less(lower)
```

## Python3

```python
from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)

        def count_less(target: int) -> int:
            left, right = 0, n - 1
            cnt = 0
            while left < right:
                if nums[left] + nums[right] < target:
                    cnt += right - left
                    left += 1
                else:
                    right -= 1
            return cnt

        return count_less(upper + 1) - count_less(lower)
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    if (va < vb) return -1;
    if (va > vb) return 1;
    return 0;
}

/* Count pairs (i, j), i < j, with nums[i] + nums[j] < target */
static long long countLessThan(int *nums, int n, long long target) {
    long long cnt = 0;
    int left = 0, right = n - 1;
    while (left < right) {
        long long sum = (long long)nums[left] + (long long)nums[right];
        if (sum < target) {
            cnt += (right - left);
            ++left;
        } else {
            --right;
        }
    }
    return cnt;
}

long long countFairPairs(int* nums, int numsSize, int lower, int upper) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmp_int);
    long long totalUpper = countLessThan(nums, numsSize, (long long)upper + 1);
    long long totalLower = countLessThan(nums, numsSize, (long long)lower);
    return totalUpper - totalLower;
}
```

## Csharp

```csharp
public class Solution
{
    public long CountFairPairs(int[] nums, int lower, int upper)
    {
        Array.Sort(nums);
        return CountLessThan(nums, (long)upper + 1) - CountLessThan(nums, lower);
    }

    private long CountLessThan(int[] arr, long target)
    {
        int n = arr.Length;
        int left = 0;
        int right = n - 1;
        long count = 0;

        while (left < right)
        {
            long sum = (long)arr[left] + arr[right];
            if (sum < target)
            {
                count += right - left;
                left++;
            }
            else
            {
                right--;
            }
        }

        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} lower
 * @param {number} upper
 * @return {number}
 */
var countFairPairs = function(nums, lower, upper) {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    
    const countLessThan = (target) => {
        let left = 0, right = n - 1;
        let cnt = 0;
        while (left < right) {
            if (nums[left] + nums[right] < target) {
                cnt += (right - left);
                left++;
            } else {
                right--;
            }
        }
        return cnt;
    };
    
    return countLessThan(upper + 1) - countLessThan(lower);
};
```

## Typescript

```typescript
function countFairPairs(nums: number[], lower: number, upper: number): number {
    nums.sort((a, b) => a - b);
    const n = nums.length;

    function countLessThan(target: number): number {
        let left = 0;
        let right = n - 1;
        let cnt = 0;
        while (left < right) {
            if (nums[left] + nums[right] < target) {
                cnt += right - left;
                left++;
            } else {
                right--;
            }
        }
        return cnt;
    }

    const totalUpper = countLessThan(upper + 1);
    const totalLower = countLessThan(lower);
    return totalUpper - totalLower;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $lower
     * @param Integer $upper
     * @return Integer
     */
    function countFairPairs($nums, $lower, $upper) {
        sort($nums);
        $cntUpper = $this->countLessThan($nums, $upper + 1);
        $cntLower = $this->countLessThan($nums, $lower);
        return $cntUpper - $cntLower;
    }

    /**
     * Count pairs (i, j) with i < j and nums[i] + nums[j] < target
     *
     * @param Integer[] $arr
     * @param Integer $target
     * @return Integer
     */
    private function countLessThan($arr, $target) {
        $n = count($arr);
        $left = 0;
        $right = $n - 1;
        $count = 0;
        while ($left < $right) {
            if ($arr[$left] + $arr[$right] < $target) {
                // all elements between left+1 and right form valid pairs with left
                $count += $right - $left;
                $left++;
            } else {
                $right--;
            }
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func countFairPairs(_ nums: [Int], _ lower: Int, _ upper: Int) -> Int {
        let sorted = nums.sorted()
        
        func countLessThan(_ bound: Int) -> Int {
            var left = 0
            var right = sorted.count - 1
            var cnt = 0
            while left < right {
                let sum = Int64(sorted[left]) + Int64(sorted[right])
                if sum < Int64(bound) {
                    cnt += (right - left)
                    left += 1
                } else {
                    right -= 1
                }
            }
            return cnt
        }
        
        let countUpper = countLessThan(upper + 1)
        let countLower = countLessThan(lower)
        return countUpper - countLower
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countFairPairs(nums: IntArray, lower: Int, upper: Int): Long {
        nums.sort()
        val n = nums.size

        fun countLessThan(target: Long): Long {
            var left = 0
            var right = n - 1
            var cnt = 0L
            while (left < right) {
                val sum = nums[left].toLong() + nums[right]
                if (sum < target) {
                    cnt += (right - left).toLong()
                    left++
                } else {
                    right--
                }
            }
            return cnt
        }

        val totalUpper = countLessThan(upper.toLong() + 1)
        val totalLower = countLessThan(lower.toLong())
        return totalUpper - totalLower
    }
}
```

## Dart

```dart
class Solution {
  int countFairPairs(List<int> nums, int lower, int upper) {
    nums.sort();
    return _countLessThan(nums, upper + 1) - _countLessThan(nums, lower);
  }

  int _countLessThan(List<int> nums, int target) {
    int n = nums.length;
    int left = 0;
    int right = n - 1;
    int count = 0;
    while (left < right) {
      if (nums[left] + nums[right] < target) {
        count += right - left;
        left++;
      } else {
        right--;
      }
    }
    return count;
  }
}
```

## Golang

```go
import "sort"

func countFairPairs(nums []int, lower int, upper int) int64 {
	sort.Ints(nums)
	return countLess(nums, upper+1) - countLess(nums, lower)
}

func countLess(nums []int, target int) int64 {
	var cnt int64
	n := len(nums)
	left, right := 0, n-1
	for left < right {
		if nums[left]+nums[right] < target {
			cnt += int64(right - left)
			left++
		} else {
			right--
		}
	}
	return cnt
}
```

## Ruby

```ruby
def count_fair_pairs(nums, lower, upper)
  nums.sort!
  count_less = lambda do |bound|
    left = 0
    right = nums.length - 1
    cnt = 0
    while left < right
      if nums[left] + nums[right] < bound
        cnt += (right - left)
        left += 1
      else
        right -= 1
      end
    end
    cnt
  end

  count_less.call(upper + 1) - count_less.call(lower)
end
```

## Scala

```scala
object Solution {
    def countFairPairs(nums: Array[Int], lower: Int, upper: Int): Long = {
        val arr = nums.sorted.map(_.toLong)
        val n = arr.length
        def countLessThan(bound: Long): Long = {
            var left = 0
            var right = n - 1
            var cnt = 0L
            while (left < right) {
                if (arr(left) + arr(right) < bound) {
                    cnt += (right - left)
                    left += 1
                } else {
                    right -= 1
                }
            }
            cnt
        }
        countLessThan(upper.toLong + 1L) - countLessThan(lower.toLong)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_fair_pairs(nums: Vec<i32>, lower: i32, upper: i32) -> i64 {
        // Convert to i64 for safe sum calculations and sort
        let mut v: Vec<i64> = nums.into_iter().map(|x| x as i64).collect();
        v.sort_unstable();

        // Helper: count pairs with sum < target
        fn count_pairs(arr: &Vec<i64>, target: i64) -> i64 {
            let mut left = 0usize;
            let mut right = arr.len().saturating_sub(1);
            let mut cnt: i64 = 0;
            while left < right {
                if arr[left] + arr[right] < target {
                    // All elements between left+1..=right form valid pairs with left
                    cnt += (right - left) as i64;
                    left += 1;
                } else {
                    right -= 1;
                }
            }
            cnt
        }

        let lower_i64 = lower as i64;
        let upper_i64 = upper as i64;

        count_pairs(&v, upper_i64 + 1) - count_pairs(&v, lower_i64)
    }
}
```

## Racket

```racket
(define/contract (count-fair-pairs nums lower upper)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (let* ((sorted-vec (list->vector (sort nums <)))
         (n (vector-length sorted-vec))
         (count-less-than
          (lambda (target)
            (let loop ((l 0) (r (- n 1)) (cnt 0))
              (if (>= l r)
                  cnt
                  (let ((s (+ (vector-ref sorted-vec l)
                              (vector-ref sorted-vec r))))
                    (if (< s target)
                        (loop (+ l 1) r (+ cnt (- r l)))
                        (loop l (- r 1) cnt))))))))
    (- (count-less-than (+ upper 1))
       (count-less-than lower))))
```

## Erlang

```erlang
-module(solution).
-export([count_fair_pairs/3]).
-spec count_fair_pairs(Nums :: [integer()], Lower :: integer(), Upper :: integer()) -> integer().
count_fair_pairs(Nums, Lower, Upper) ->
    Sorted = lists:sort(Nums),
    Tuple = list_to_tuple(Sorted),
    Len = tuple_size(Tuple),
    CountUpper = count_less_than(Upper + 1, Tuple, Len),
    CountLower = count_less_than(Lower, Tuple, Len),
    CountUpper - CountLower.

count_less_than(Target, Tuple, Len) ->
    count_less_than(0, Target, Tuple, Len, 0).

count_less_than(I, _Target, _Tuple, Len, Acc) when I >= Len - 1 ->
    Acc;
count_less_than(I, Target, Tuple, Len, Acc) ->
    Elem = element(I + 1, Tuple),
    Needed = Target - Elem,
    Pos = lower_bound(Tuple, Len, I + 1, Needed),
    NewAcc = Acc + (Pos - I - 1),
    count_less_than(I + 1, Target, Tuple, Len, NewAcc).

lower_bound(_Tuple, _Len, L, R, _Value) when L >= R ->
    L;
lower_bound(Tuple, Len, L, R, Value) ->
    Mid = (L + R) div 2,
    Elem = element(Mid + 1, Tuple),
    if
        Elem < Value ->
            lower_bound(Tuple, Len, Mid + 1, R, Value);
        true ->
            lower_bound(Tuple, Len, L, Mid, Value)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_fair_pairs(nums :: [integer], lower :: integer, upper :: integer) :: integer
  def count_fair_pairs(nums, lower, upper) do
    sorted_tuple = nums |> Enum.sort() |> List.to_tuple()
    count_less(sorted_tuple, upper + 1) - count_less(sorted_tuple, lower)
  end

  defp count_less(arr, target) do
    n = tuple_size(arr)
    count_pairs(arr, target, 0, n - 1, 0)
  end

  defp count_pairs(_arr, _target, left, right, acc) when left >= right, do: acc

  defp count_pairs(arr, target, left, right, acc) do
    sum = elem(arr, left) + elem(arr, right)

    if sum < target do
      # all pairs (left, k) for k in (left+1)..right are valid
      count_pairs(arr, target, left + 1, right, acc + (right - left))
    else
      count_pairs(arr, target, left, right - 1, acc)
    end
  end
end
```
