# 0611. Valid Triangle Number

## Cpp

```cpp
class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        long long count = 0;
        for (int i = 0; i < n - 2; ++i) {
            int k = i + 2;
            for (int j = i + 1; j < n - 1; ++j) {
                while (k < n && nums[i] + nums[j] > nums[k]) {
                    ++k;
                }
                count += k - j - 1;
            }
        }
        return static_cast<int>(count);
    }
};
```

## Java

```java
class Solution {
    public int triangleNumber(int[] nums) {
        if (nums == null || nums.length < 3) return 0;
        java.util.Arrays.sort(nums);
        int n = nums.length;
        int count = 0;
        for (int i = n - 1; i >= 2; i--) {
            int left = 0, right = i - 1;
            while (left < right) {
                if (nums[left] + nums[right] > nums[i]) {
                    count += right - left;
                    right--;
                } else {
                    left++;
                }
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            return 0
        nums.sort()
        count = 0
        # iterate over the largest side index i
        for i in range(n - 1, 1, -1):
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    # all elements from left to right-1 will also satisfy
                    count += right - left
                    right -= 1
                else:
                    left += 1
        return count
```

## Python3

```python
from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        nums.sort()
        count = 0
        # i is the index of the largest side
        for i in range(n - 1, 1, -1):
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    count += right - left
                    right -= 1
                else:
                    left += 1
        return count
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    return (*(const int *)a) - (*(const int *)b);
}

int triangleNumber(int* nums, int numsSize) {
    if (numsSize < 3) return 0;
    qsort(nums, numsSize, sizeof(int), cmp_int);
    long long count = 0;
    for (int i = 0; i < numsSize - 2; ++i) {
        int k = i + 2;
        for (int j = i + 1; j < numsSize - 1; ++j) {
            while (k < numsSize && nums[i] + nums[j] > nums[k]) {
                ++k;
            }
            count += k - j - 1;
        }
    }
    return (int)count;
}
```

## Csharp

```csharp
public class Solution
{
    public int TriangleNumber(int[] nums)
    {
        if (nums == null || nums.Length < 3) return 0;
        Array.Sort(nums);
        int n = nums.Length;
        int count = 0;

        for (int i = 0; i < n - 2; i++)
        {
            int k = i + 2;
            for (int j = i + 1; j < n - 1; j++)
            {
                while (k < n && nums[i] + nums[j] > nums[k])
                {
                    k++;
                }
                count += k - j - 1;
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
 * @return {number}
 */
var triangleNumber = function(nums) {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    let count = 0;
    for (let i = n - 1; i >= 2; i--) {
        let left = 0, right = i - 1;
        while (left < right) {
            if (nums[left] + nums[right] > nums[i]) {
                count += right - left;
                right--;
            } else {
                left++;
            }
        }
    }
    return count;
};
```

## Typescript

```typescript
function triangleNumber(nums: number[]): number {
    const n = nums.length;
    if (n < 3) return 0;
    nums.sort((a, b) => a - b);
    let count = 0;
    for (let i = n - 1; i >= 2; i--) {
        let left = 0;
        let right = i - 1;
        while (left < right) {
            if (nums[left] + nums[right] > nums[i]) {
                count += right - left;
                right--;
            } else {
                left++;
            }
        }
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function triangleNumber($nums) {
        $n = count($nums);
        if ($n < 3) return 0;
        sort($nums, SORT_NUMERIC);
        $count = 0;
        for ($i = 0; $i < $n - 2; $i++) {
            $k = $i + 2;
            for ($j = $i + 1; $j < $n - 1; $j++) {
                while ($k < $n && $nums[$i] + $nums[$j] > $nums[$k]) {
                    $k++;
                }
                $count += $k - $j - 1;
            }
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func triangleNumber(_ nums: [Int]) -> Int {
        let n = nums.count
        if n < 3 { return 0 }
        var sorted = nums.sorted()
        var count = 0
        for i in 0..<(n - 2) {
            var k = i + 2
            for j in (i + 1)..<(n - 1) {
                while k < n && sorted[i] + sorted[j] > sorted[k] {
                    k += 1
                }
                count += max(0, k - j - 1)
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun triangleNumber(nums: IntArray): Int {
        nums.sort()
        var count = 0L
        val n = nums.size
        for (i in 0 until n - 2) {
            var k = i + 2
            for (j in i + 1 until n - 1) {
                while (k < n && nums[i] + nums[j] > nums[k]) {
                    k++
                }
                count += (k - j - 1).toLong()
            }
        }
        return count.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int triangleNumber(List<int> nums) {
    int n = nums.length;
    if (n < 3) return 0;
    nums.sort();
    int count = 0;
    for (int k = n - 1; k >= 2; --k) {
      int left = 0, right = k - 1;
      while (left < right) {
        if (nums[left] + nums[right] > nums[k]) {
          count += right - left;
          right--;
        } else {
          left++;
        }
      }
    }
    return count;
  }
}
```

## Golang

```go
package main

import "sort"

func triangleNumber(nums []int) int {
	n := len(nums)
	if n < 3 {
		return 0
	}
	sort.Ints(nums)
	count := 0
	for i := n - 1; i >= 2; i-- {
		left, right := 0, i-1
		for left < right {
			if nums[left]+nums[right] > nums[i] {
				count += right - left
				right--
			} else {
				left++
			}
		}
	}
	return count
}
```

## Ruby

```ruby
def triangle_number(nums)
  nums.sort!
  n = nums.length
  count = 0
  (0...n - 2).each do |i|
    k = i + 2
    (i + 1...n - 1).each do |j|
      while k < n && nums[i] + nums[j] > nums[k]
        k += 1
      end
      count += k - j - 1 if k > j + 1
    end
  end
  count
end
```

## Scala

```scala
object Solution {
  def triangleNumber(nums: Array[Int]): Int = {
    val n = nums.length
    java.util.Arrays.sort(nums)
    var count: Long = 0L
    for (i <- 0 until n - 2) {
      var k = i + 2
      for (j <- i + 1 until n - 1) {
        while (k < n && nums(i) + nums(j) > nums(k)) {
          k += 1
        }
        count += (k - j - 1)
      }
    }
    count.toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn triangle_number(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n < 3 {
            return 0;
        }
        let mut arr = nums;
        arr.sort_unstable();

        let mut count: i64 = 0;

        for k in (2..n).rev() {
            let mut left: usize = 0;
            let mut right: usize = k - 1;
            while left < right {
                if arr[left] + arr[right] > arr[k] {
                    count += (right - left) as i64;
                    // move the right pointer to explore smaller pairs
                    right -= 1;
                } else {
                    left += 1;
                }
            }
        }

        count as i32
    }
}
```

## Racket

```racket
(define/contract (triangle-number nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((sorted (list->vector (sort nums <)))
         (n (vector-length sorted)))
    (let loop-i ((i 0) (total 0))
      (if (>= i (- n 2))
          total
          (let loop-j ((j (+ i 1)) (k (+ i 2)) (sub-total total))
            (if (>= j (- n 1))
                (loop-i (+ i 1) sub-total)
                (let move-k ((kk k))
                  (if (and (< kk n)
                           (> (+ (vector-ref sorted i)
                                 (vector-ref sorted j))
                              (vector-ref sorted kk)))
                      (move-k (+ kk 1))
                      (let* ((newk kk)
                             (valid (- newk j 1)))
                        (loop-j (+ j 1)
                                (max (+ j 2) newk)
                                (+ sub-total valid)))))))))))
```

## Erlang

```erlang
-module(solution).
-export([triangle_number/1]).

-spec triangle_number(Nums :: [integer()]) -> integer().
triangle_number(Nums) ->
    Sorted = lists:sort(Nums),
    Arr = list_to_tuple(Sorted),
    N = tuple_size(Arr),
    count_triangles(N - 1, Arr, 0).

count_triangles(K, _Arr, Acc) when K < 2 ->
    Acc;
count_triangles(K, Arr, Acc) ->
    CountForK = count_two_pointer(0, K - 1, K, Arr, 0),
    NewAcc = Acc + CountForK,
    count_triangles(K - 1, Arr, NewAcc).

count_two_pointer(I, J, K, Arr, Acc) when I >= J ->
    Acc;
count_two_pointer(I, J, K, Arr, Acc) ->
    A = element(I + 1, Arr),
    B = element(J + 1, Arr),
    C = element(K + 1, Arr),
    if
        A + B > C ->
            count_two_pointer(I, J - 1, K, Arr, Acc + (J - I));
        true ->
            count_two_pointer(I + 1, J, K, Arr, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec triangle_number(nums :: [integer]) :: integer
  def triangle_number(nums) do
    sorted = Enum.sort(nums)
    n = length(sorted)

    if n < 3 do
      0
    else
      0..(n - 3)
      |> Enum.reduce(0, fn i, acc ->
        {new_acc, _k} =
          Enum.reduce((i + 1)..(n - 2), {acc, i + 2}, fn j, {inner_acc, k} ->
            sum = Enum.at(sorted, i) + Enum.at(sorted, j)
            k = advance_k(sorted, n, sum, k)

            add = max(k - j - 1, 0)
            {inner_acc + add, k}
          end)

        new_acc
      end)
    end
  end

  defp advance_k(_sorted, n, _sum, k) when k >= n, do: k

  defp advance_k(sorted, n, sum, k) do
    if sum > Enum.at(sorted, k) do
      advance_k(sorted, n, sum, k + 1)
    else
      k
    end
  end
end
```
