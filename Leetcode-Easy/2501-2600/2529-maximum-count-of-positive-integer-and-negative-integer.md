# 2529. Maximum Count of Positive Integer and Negative Integer

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maximumCount(vector<int>& nums) {
        auto lower = lower_bound(nums.begin(), nums.end(), 0);
        auto upper = upper_bound(nums.begin(), nums.end(), 0);
        int negativeCnt = static_cast<int>(lower - nums.begin());
        int positiveCnt = static_cast<int>(nums.end() - upper);
        return max(negativeCnt, positiveCnt);
    }
};
```

## Java

```java
class Solution {
    public int maximumCount(int[] nums) {
        int n = nums.length;
        int firstNonNeg = lowerBound(nums, 0); // first index where value >= 0
        int firstPos = upperBound(nums, 0);   // first index where value > 0

        int negativeCount = firstNonNeg;          // all before first non-negative are negative
        int positiveCount = n - firstPos;         // all after last zero (i.e., from first positive) are positive

        return Math.max(negativeCount, positiveCount);
    }

    private int lowerBound(int[] nums, int target) {
        int left = 0, right = nums.length;
        while (left < right) {
            int mid = (left + right) >>> 1;
            if (nums[mid] >= target) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    private int upperBound(int[] nums, int target) {
        int left = 0, right = nums.length;
        while (left < right) {
            int mid = (left + right) >>> 1;
            if (nums[mid] > target) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}
```

## Python

```python
class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import bisect
        neg = bisect.bisect_left(nums, 0)          # count of numbers < 0
        pos = len(nums) - bisect.bisect_right(nums, 0)  # count of numbers > 0
        return max(neg, pos)
```

## Python3

```python
from typing import List
import bisect

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        lower = bisect.bisect_left(nums, 0)   # first index >= 0 (negative count)
        upper = bisect.bisect_right(nums, 0)  # first index > 0
        negative = lower
        positive = len(nums) - upper
        return max(negative, positive)
```

## C

```c
int lowerBound(int* nums, int size) {
    int left = 0, right = size - 1;
    int ans = size;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] < 0) {
            left = mid + 1;
        } else {
            ans = mid;
            right = mid - 1;
        }
    }
    return ans;
}

int upperBound(int* nums, int size) {
    int left = 0, right = size - 1;
    int ans = size;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] <= 0) {
            left = mid + 1;
        } else {
            ans = mid;
            right = mid - 1;
        }
    }
    return ans;
}

int maximumCount(int* nums, int numsSize) {
    int negCnt = lowerBound(nums, numsSize);
    int posCnt = numsSize - upperBound(nums, numsSize);
    return (negCnt > posCnt) ? negCnt : posCnt;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaximumCount(int[] nums)
    {
        int n = nums.Length;
        int negCount = LowerBound(nums);
        int posCount = n - UpperBound(nums);
        return Math.Max(negCount, posCount);
    }

    private int LowerBound(int[] nums)
    {
        int left = 0, right = nums.Length;
        while (left < right)
        {
            int mid = left + (right - left) / 2;
            if (nums[mid] < 0)
                left = mid + 1;
            else
                right = mid;
        }
        return left; // first index with value >= 0, also count of negatives
    }

    private int UpperBound(int[] nums)
    {
        int left = 0, right = nums.Length;
        while (left < right)
        {
            int mid = left + (right - left) / 2;
            if (nums[mid] <= 0)
                left = mid + 1;
            else
                right = mid;
        }
        return left; // first index with value > 0
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumCount = function(nums) {
    const n = nums.length;
    
    const lowerBound = (arr) => {
        let left = 0, right = arr.length - 1;
        let idx = arr.length;
        while (left <= right) {
            const mid = Math.floor((left + right) / 2);
            if (arr[mid] >= 0) {
                idx = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return idx;
    };
    
    const upperBound = (arr) => {
        let left = 0, right = arr.length - 1;
        let idx = arr.length;
        while (left <= right) {
            const mid = Math.floor((left + right) / 2);
            if (arr[mid] > 0) {
                idx = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return idx;
    };
    
    const negativeCount = lowerBound(nums);          // first index >= 0
    const positiveCount = n - upperBound(nums);      // elements > 0
    
    return Math.max(negativeCount, positiveCount);
};
```

## Typescript

```typescript
function maximumCount(nums: number[]): number {
    const n = nums.length;

    const lowerBound = (arr: number[]): number => {
        let left = 0, right = arr.length;
        while (left < right) {
            const mid = Math.floor((left + right) / 2);
            if (arr[mid] < 0) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left; // first index with value >= 0
    };

    const upperBound = (arr: number[]): number => {
        let left = 0, right = arr.length;
        while (left < right) {
            const mid = Math.floor((left + right) / 2);
            if (arr[mid] <= 0) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left; // first index with value > 0
    };

    const negativeCount = lowerBound(nums);
    const positiveCount = n - upperBound(nums);

    return Math.max(negativeCount, positiveCount);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximumCount($nums) {
        $n = count($nums);
        
        // Find first index with value >= 0 (lower bound)
        $l = 0;
        $r = $n - 1;
        $firstNonNeg = $n; // default if all are negative
        while ($l <= $r) {
            $mid = intdiv($l + $r, 2);
            if ($nums[$mid] < 0) {
                $l = $mid + 1;
            } else {
                $firstNonNeg = $mid;
                $r = $mid - 1;
            }
        }
        
        // Find first index with value > 0 (upper bound)
        $l = 0;
        $r = $n - 1;
        $firstPos = $n; // default if no positive numbers
        while ($l <= $r) {
            $mid = intdiv($l + $r, 2);
            if ($nums[$mid] <= 0) {
                $l = $mid + 1;
            } else {
                $firstPos = $mid;
                $r = $mid - 1;
            }
        }
        
        $negativeCount = $firstNonNeg;               // all before first non‑negative are negative
        $positiveCount = $n - $firstPos;             // all after last zero (i.e., from first positive) are positive
        
        return max($negativeCount, $positiveCount);
    }
}
```

## Swift

```swift
class Solution {
    func maximumCount(_ nums: [Int]) -> Int {
        let negativeCount = lowerBound(nums)
        let positiveCount = nums.count - upperBound(nums)
        return max(negativeCount, positiveCount)
    }
    
    private func lowerBound(_ nums: [Int]) -> Int {
        var left = 0
        var right = nums.count - 1
        var ans = nums.count
        while left <= right {
            let mid = (left + right) / 2
            if nums[mid] < 0 {
                left = mid + 1
            } else {
                ans = mid
                right = mid - 1
            }
        }
        return ans
    }
    
    private func upperBound(_ nums: [Int]) -> Int {
        var left = 0
        var right = nums.count - 1
        var ans = nums.count
        while left <= right {
            let mid = (left + right) / 2
            if nums[mid] <= 0 {
                left = mid + 1
            } else {
                ans = mid
                right = mid - 1
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumCount(nums: IntArray): Int {
        val n = nums.size
        // first index where value >= 0
        var left = 0
        var right = n
        while (left < right) {
            val mid = (left + right) ushr 1
            if (nums[mid] < 0) {
                left = mid + 1
            } else {
                right = mid
            }
        }
        val negativeCount = left

        // first index where value > 0
        left = 0
        right = n
        while (left < right) {
            val mid = (left + right) ushr 1
            if (nums[mid] <= 0) {
                left = mid + 1
            } else {
                right = mid
            }
        }
        val positiveCount = n - left

        return maxOf(negativeCount, positiveCount)
    }
}
```

## Dart

```dart
class Solution {
  int maximumCount(List<int> nums) {
    int n = nums.length;

    int lowerBound() {
      int left = 0, right = n - 1;
      int ans = n;
      while (left <= right) {
        int mid = left + ((right - left) >> 1);
        if (nums[mid] < 0) {
          left = mid + 1;
        } else {
          ans = mid;
          right = mid - 1;
        }
      }
      return ans;
    }

    int upperBound() {
      int left = 0, right = n - 1;
      int ans = n;
      while (left <= right) {
        int mid = left + ((right - left) >> 1);
        if (nums[mid] <= 0) {
          left = mid + 1;
        } else {
          ans = mid;
          right = mid - 1;
        }
      }
      return ans;
    }

    int negativeCount = lowerBound();
    int positiveCount = n - upperBound();

    return negativeCount > positiveCount ? negativeCount : positiveCount;
  }
}
```

## Golang

```go
package main

import "sort"

func maximumCount(nums []int) int {
	n := len(nums)
	// first index where value >= 0
	negEnd := sort.Search(n, func(i int) bool { return nums[i] >= 0 })
	// first index where value > 0
	posStart := sort.Search(n, func(i int) bool { return nums[i] > 0 })

	negativeCount := negEnd
	positiveCount := n - posStart

	if positiveCount > negativeCount {
		return positiveCount
	}
	return negativeCount
}
```

## Ruby

```ruby
def maximum_count(nums)
  n = nums.length
  lower = nums.bsearch_index { |x| x >= 0 } || n
  upper = nums.bsearch_index { |x| x > 0 } || n
  neg = lower
  pos = n - upper
  neg > pos ? neg : pos
end
```

## Scala

```scala
object Solution {
  def maximumCount(nums: Array[Int]): Int = {
    val n = nums.length

    def lowerBound(): Int = {
      var left = 0
      var right = n - 1
      var ans = n
      while (left <= right) {
        val mid = left + (right - left) / 2
        if (nums(mid) < 0) {
          left = mid + 1
        } else {
          ans = mid
          right = mid - 1
        }
      }
      ans
    }

    def upperBound(): Int = {
      var left = 0
      var right = n - 1
      var ans = n
      while (left <= right) {
        val mid = left + (right - left) / 2
        if (nums(mid) <= 0) {
          left = mid + 1
        } else {
          ans = mid
          right = mid - 1
        }
      }
      ans
    }

    val negCount = lowerBound()
    val posCount = n - upperBound()
    math.max(negCount, posCount)
  }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_count(nums: Vec<i32>) -> i32 {
        fn lower_bound(nums: &Vec<i32>) -> usize {
            let mut left = 0usize;
            let mut right = nums.len();
            while left < right {
                let mid = left + (right - left) / 2;
                if nums[mid] < 0 {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }
            left
        }

        fn upper_bound(nums: &Vec<i32>) -> usize {
            let mut left = 0usize;
            let mut right = nums.len();
            while left < right {
                let mid = left + (right - left) / 2;
                if nums[mid] <= 0 {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }
            left
        }

        let neg = lower_bound(&nums);
        let pos = nums.len() - upper_bound(&nums);
        std::cmp::max(neg, pos) as i32
    }
}
```

## Racket

```racket
(define/contract (maximum-count nums)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((lst nums) (pos 0) (neg 0))
    (cond
      [(null? lst) (max pos neg)]
      [else
       (let ((x (car lst)))
         (cond
           [(> x 0) (loop (cdr lst) (+ pos 1) neg)]
           [(< x 0) (loop (cdr lst) pos (+ neg 1))]
           [else   (loop (cdr lst) pos neg)]))])))
```

## Erlang

```erlang
-spec maximum_count(Nums :: [integer()]) -> integer().
maximum_count(Nums) ->
    {Neg, Pos} = count(Nums, 0, 0),
    max(Neg, Pos).

count([], Neg, Pos) -> {Neg, Pos};
count([H|T], Neg, Pos) when H < 0 ->
    count(T, Neg + 1, Pos);
count([H|T], Neg, Pos) when H > 0 ->
    count(T, Neg, Pos + 1);
count([_|T], Neg, Pos) -> % zero
    count(T, Neg, Pos).

max(A, B) when A >= B -> A;
max(_, B) -> B.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_count(nums :: [integer]) :: integer
  def maximum_count(nums) do
    {neg, pos} =
      Enum.reduce(nums, {0, 0}, fn x, {n, p} ->
        cond do
          x < 0 -> {n + 1, p}
          x > 0 -> {n, p + 1}
          true -> {n, p}
        end
      end)

    max(neg, pos)
  end
end
```
