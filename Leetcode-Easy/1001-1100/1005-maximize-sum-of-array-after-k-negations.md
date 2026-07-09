# 1005. Maximize Sum Of Array After K Negations

## Cpp

```cpp
class Solution {
public:
    int largestSumAfterKNegations(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        for (int i = 0; i < (int)nums.size() && k > 0 && nums[i] < 0; ++i) {
            nums[i] = -nums[i];
            --k;
        }
        long long sum = 0;
        int minAbs = INT_MAX;
        for (int v : nums) {
            sum += v;
            minAbs = min(minAbs, abs(v));
        }
        if (k % 2 == 1) {
            sum -= 2LL * minAbs;
        }
        return (int)sum;
    }
};
```

## Java

```java
class Solution {
    public int largestSumAfterKNegations(int[] nums, int k) {
        java.util.Arrays.sort(nums);
        for (int i = 0; i < nums.length && k > 0 && nums[i] < 0; i++) {
            nums[i] = -nums[i];
            k--;
        }
        int sum = 0;
        int minAbs = Integer.MAX_VALUE;
        for (int num : nums) {
            sum += num;
            int absVal = Math.abs(num);
            if (absVal < minAbs) {
                minAbs = absVal;
            }
        }
        if ((k & 1) == 1) {
            sum -= 2 * minAbs;
        }
        return sum;
    }
}
```

## Python

```python
class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        i = 0
        n = len(nums)
        while i < n and k > 0 and nums[i] < 0:
            nums[i] = -nums[i]
            k -= 1
            i += 1
        total = sum(nums)
        if k % 2 == 1:
            min_abs = min(abs(x) for x in nums)
            total -= 2 * min_abs
        return total
```

## Python3

```python
from typing import List

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        n = len(nums)
        # Flip negative numbers while we have operations left
        while i < n and k > 0 and nums[i] < 0:
            nums[i] = -nums[i]
            i += 1
            k -= 1
        total = sum(nums)
        # If there are remaining flips, they affect the smallest absolute value element
        if k % 2 == 1:
            min_val = min(nums)  # after previous flips, all numbers are non‑negative except possibly some positives
            total -= 2 * min_val
        return total
```

## C

```c
#include <stdlib.h>
#include <limits.h>

static int cmp_int(const void *a, const void *b) {
    return (*(const int *)a) - (*(const int *)b);
}

int largestSumAfterKNegations(int* nums, int numsSize, int k) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmp_int);

    for (int i = 0; i < numsSize && k > 0 && nums[i] < 0; ++i) {
        nums[i] = -nums[i];
        --k;
    }

    long long sum = 0;
    int minAbs = INT_MAX;
    for (int i = 0; i < numsSize; ++i) {
        sum += nums[i];
        int absVal = nums[i] >= 0 ? nums[i] : -nums[i];
        if (absVal < minAbs) minAbs = absVal;
    }

    if (k % 2 == 1) {
        sum -= 2LL * minAbs;
    }

    return (int)sum;
}
```

## Csharp

```csharp
public class Solution {
    public int LargestSumAfterKNegations(int[] nums, int k) {
        System.Array.Sort(nums);
        int n = nums.Length;
        for (int i = 0; i < n && k > 0 && nums[i] < 0; i++) {
            nums[i] = -nums[i];
            k--;
        }
        long sum = 0;
        int minVal = int.MaxValue;
        foreach (int v in nums) {
            sum += v;
            if (v < minVal) minVal = v;
        }
        if ((k & 1) == 1) {
            sum -= 2L * minVal;
        }
        return (int)sum;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var largestSumAfterKNegations = function(nums, k) {
    nums.sort((a, b) => a - b);
    for (let i = 0; i < nums.length && k > 0 && nums[i] < 0; i++) {
        nums[i] = -nums[i];
        k--;
    }
    let sum = 0;
    let minAbs = Infinity;
    for (const v of nums) {
        sum += v;
        const av = Math.abs(v);
        if (av < minAbs) minAbs = av;
    }
    if (k % 2 === 1) {
        sum -= 2 * minAbs;
    }
    return sum;
};
```

## Typescript

```typescript
function largestSumAfterKNegations(nums: number[], k: number): number {
    nums.sort((a, b) => a - b);
    let i = 0;
    while (k > 0 && i < nums.length && nums[i] < 0) {
        nums[i] = -nums[i];
        k--;
        i++;
    }
    let sum = 0;
    let minAbs = Infinity;
    for (const v of nums) {
        sum += v;
        const a = Math.abs(v);
        if (a < minAbs) minAbs = a;
    }
    if (k % 2 === 1) {
        sum -= 2 * minAbs;
    }
    return sum;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function largestSumAfterKNegations($nums, $k) {
        sort($nums);
        $n = count($nums);
        for ($i = 0; $i < $n && $k > 0 && $nums[$i] < 0; $i++) {
            $nums[$i] = -$nums[$i];
            $k--;
        }
        $sum = array_sum($nums);
        if ($k % 2 == 1) {
            $minVal = min($nums);
            $sum -= 2 * $minVal;
        }
        return $sum;
    }
}
```

## Swift

```swift
class Solution {
    func largestSumAfterKNegations(_ nums: [Int], _ k: Int) -> Int {
        var arr = nums.sorted()
        var remaining = k
        var index = 0
        while index < arr.count && remaining > 0 && arr[index] < 0 {
            arr[index] = -arr[index]
            remaining -= 1
            index += 1
        }
        var sum = 0
        var minAbs = Int.max
        for v in arr {
            sum += v
            let a = abs(v)
            if a < minAbs { minAbs = a }
        }
        if remaining % 2 == 1 {
            sum -= 2 * minAbs
        }
        return sum
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun largestSumAfterKNegations(nums: IntArray, k: Int): Int {
        java.util.Arrays.sort(nums)
        var remaining = k
        for (i in nums.indices) {
            if (remaining > 0 && nums[i] < 0) {
                nums[i] = -nums[i]
                remaining--
            }
        }
        var sum = 0
        var minVal = Int.MAX_VALUE
        for (v in nums) {
            sum += v
            if (v < minVal) minVal = v
        }
        if (remaining % 2 == 1) {
            sum -= 2 * minVal
        }
        return sum
    }
}
```

## Dart

```dart
class Solution {
  int largestSumAfterKNegations(List<int> nums, int k) {
    nums.sort();
    for (int i = 0; i < nums.length && k > 0 && nums[i] < 0; i++) {
      nums[i] = -nums[i];
      k--;
    }
    int sum = 0;
    int minAbs = 1 << 30;
    for (int v in nums) {
      sum += v;
      int a = v.abs();
      if (a < minAbs) minAbs = a;
    }
    if (k % 2 == 1) {
      sum -= 2 * minAbs;
    }
    return sum;
  }
}
```

## Golang

```go
package main

import "sort"

func largestSumAfterKNegations(nums []int, k int) int {
	sort.Ints(nums)
	for i := 0; i < len(nums) && k > 0 && nums[i] < 0; i++ {
		nums[i] = -nums[i]
		k--
	}
	sum := 0
	minAbs := int(^uint(0) >> 1)
	for _, v := range nums {
		sum += v
		if v < 0 {
			v = -v
		}
		if v < minAbs {
			minAbs = v
		}
	}
	if k%2 == 1 {
		sum -= 2 * minAbs
	}
	return sum
}
```

## Ruby

```ruby
def largest_sum_after_k_negations(nums, k)
  nums.sort!
  i = 0
  while i < nums.length && k > 0 && nums[i] < 0
    nums[i] = -nums[i]
    k -= 1
    i += 1
  end
  sum = nums.sum
  if k.odd?
    min_abs = nums.map { |x| x.abs }.min
    sum -= 2 * min_abs
  end
  sum
end
```

## Scala

```scala
object Solution {
    def largestSumAfterKNegations(nums: Array[Int], k: Int): Int = {
        val arr = nums.clone()
        java.util.Arrays.sort(arr) // ascending order
        var remaining = k
        var idx = 0
        while (idx < arr.length && remaining > 0 && arr(idx) < 0) {
            arr(idx) = -arr(idx)
            remaining -= 1
            idx += 1
        }
        var sum: Long = 0L
        var minAbs = Int.MaxValue
        for (v <- arr) {
            sum += v
            val av = if (v < 0) -v else v
            if (av < minAbs) minAbs = av
        }
        if ((remaining & 1) == 1) {
            sum -= 2L * minAbs
        }
        sum.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn largest_sum_after_k_negations(mut nums: Vec<i32>, mut k: i32) -> i32 {
        nums.sort();
        for i in 0..nums.len() {
            if k > 0 && nums[i] < 0 {
                nums[i] = -nums[i];
                k -= 1;
            } else {
                break;
            }
        }
        let mut sum = 0i32;
        let mut min_abs = i32::MAX;
        for &v in &nums {
            sum += v;
            let av = if v < 0 { -v } else { v };
            if av < min_abs {
                min_abs = av;
            }
        }
        if k % 2 == 1 {
            sum -= 2 * min_abs;
        }
        sum
    }
}
```

## Racket

```racket
(define/contract (largest-sum-after-k-negations nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((sorted (sort nums <))
         (process
          (let loop ((lst sorted) (krem k) (acc '()))
            (if (null? lst)
                (values (reverse acc) krem)
                (let ((x (car lst)))
                  (if (and (< x 0) (> krem 0))
                      (loop (cdr lst) (- krem 1) (cons (- x) acc))
                      (loop (cdr lst) krem (cons x acc))))))))
    (let-values ([(newlist kleft) process])
      (define sum (foldl + 0 newlist))
      (if (odd? kleft)
          (let ((min-abs (apply min (map abs newlist))))
            (- sum (* 2 min-abs)))
          sum))))
```

## Erlang

```erlang
-module(solution).
-export([largest_sum_after_k_negations/2]).

largest_sum_after_k_negations(Nums, K) ->
    Sorted = lists:sort(Nums),
    {NewList, RemK, MinAbs} = flip_negatives(Sorted, K, [], 101),
    Sum = lists:sum(NewList),
    case RemK rem 2 of
        0 -> Sum;
        1 -> Sum - 2 * MinAbs
    end.

flip_negatives([], K, Acc, Min) ->
    {lists:reverse(Acc), K, Min};
flip_negatives([H|T], K, Acc, Min) when K > 0, H < 0 ->
    NewVal = -H,
    NewMin = erlang:min(erlang:abs(NewVal), Min),
    flip_negatives(T, K - 1, [NewVal | Acc], NewMin);
flip_negatives([H|T], K, Acc, Min) ->
    NewMin = erlang:min(erlang:abs(H), Min),
    flip_negatives(T, K, [H | Acc], NewMin).
```

## Elixir

```elixir
defmodule Solution do
  @spec largest_sum_after_k_negations(nums :: [integer], k :: integer) :: integer
  def largest_sum_after_k_negations(nums, k) do
    sorted = Enum.sort(nums)

    {changed, remaining_k} =
      Enum.map_reduce(sorted, k, fn x, acc_k ->
        if acc_k > 0 and x < 0 do
          {-x, acc_k - 1}
        else
          {x, acc_k}
        end
      end)

    sum = Enum.sum(changed)
    min_abs = changed |> Enum.map(&abs/1) |> Enum.min()

    if rem(remaining_k, 2) == 1 do
      sum - 2 * min_abs
    else
      sum
    end
  end
end
```
