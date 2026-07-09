# 0719. Find K-th Smallest Pair Distance

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int smallestDistancePair(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int low = 0;
        int high = nums.back() - nums.front();
        while (low < high) {
            int mid = low + (high - low) / 2;
            long long cnt = 0;
            int left = 0;
            for (int right = 0; right < (int)nums.size(); ++right) {
                while (nums[right] - nums[left] > mid) ++left;
                cnt += right - left;
            }
            if (cnt >= k)
                high = mid;
            else
                low = mid + 1;
        }
        return low;
    }
};
```

## Java

```java
class Solution {
    public int smallestDistancePair(int[] nums, int k) {
        java.util.Arrays.sort(nums);
        int n = nums.length;
        int low = 0;
        int high = nums[n - 1] - nums[0];
        while (low < high) {
            int mid = low + (high - low) / 2;
            long count = 0;
            int left = 0;
            for (int right = 0; right < n; ++right) {
                while (nums[right] - nums[left] > mid) {
                    left++;
                }
                count += right - left;
            }
            if (count >= k) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }
}
```

## Python

```python
class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        low, high = 0, nums[-1] - nums[0]

        while low < high:
            mid = (low + high) // 2
            count = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            if count < k:
                low = mid + 1
            else:
                high = mid

        return low
```

## Python3

```python
from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        low, high = 0, nums[-1] - nums[0]

        while low < high:
            mid = (low + high) // 2
            count = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            if count >= k:
                high = mid
            else:
                low = mid + 1

        return low
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    return *(const int *)a - *(const int *)b;
}

int smallestDistancePair(int* nums, int numsSize, int k) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmp_int);
    
    int low = 0;
    int high = nums[numsSize - 1] - nums[0];
    
    while (low < high) {
        int mid = low + (high - low) / 2;
        int count = 0;
        int left = 0;
        for (int right = 0; right < numsSize; ++right) {
            while (nums[right] - nums[left] > mid) {
                ++left;
            }
            count += right - left;
        }
        if (count >= k)
            high = mid;
        else
            low = mid + 1;
    }
    
    return low;
}
```

## Csharp

```csharp
public class Solution {
    public int SmallestDistancePair(int[] nums, int k) {
        System.Array.Sort(nums);
        int n = nums.Length;
        int low = 0;
        int high = nums[n - 1] - nums[0];
        while (low < high) {
            int mid = low + (high - low) / 2;
            long count = 0;
            int left = 0;
            for (int right = 0; right < n; ++right) {
                while (nums[right] - nums[left] > mid) {
                    left++;
                }
                count += right - left;
            }
            if (count >= k) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
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
var smallestDistancePair = function(nums, k) {
    nums.sort((a, b) => a - b);
    let low = 0;
    let high = nums[nums.length - 1] - nums[0];
    
    const countPairs = (maxDist) => {
        let count = 0;
        let left = 0;
        for (let right = 0; right < nums.length; ++right) {
            while (nums[right] - nums[left] > maxDist) {
                left++;
            }
            count += right - left;
        }
        return count;
    };
    
    while (low < high) {
        const mid = Math.floor((low + high) / 2);
        if (countPairs(mid) >= k) {
            high = mid;
        } else {
            low = mid + 1;
        }
    }
    
    return low;
};
```

## Typescript

```typescript
function smallestDistancePair(nums: number[], k: number): number {
    nums.sort((a, b) => a - b);
    let low = 0;
    let high = nums[nums.length - 1] - nums[0];
    
    const countPairs = (maxDist: number): number => {
        let count = 0;
        let left = 0;
        for (let right = 0; right < nums.length; right++) {
            while (nums[right] - nums[left] > maxDist) left++;
            count += right - left;
        }
        return count;
    };
    
    while (low < high) {
        const mid = Math.floor((low + high) / 2);
        if (countPairs(mid) >= k) {
            high = mid;
        } else {
            low = mid + 1;
        }
    }
    return low;
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
    function smallestDistancePair($nums, $k) {
        sort($nums);
        $n = count($nums);
        $low = 0;
        $high = $nums[$n - 1] - $nums[0];
        
        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            $count = 0;
            $left = 0;
            for ($right = 0; $right < $n; $right++) {
                while ($nums[$right] - $nums[$left] > $mid) {
                    $left++;
                }
                $count += $right - $left;
            }
            if ($count >= $k) {
                $high = $mid;
            } else {
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
    func smallestDistancePair(_ nums: [Int], _ k: Int) -> Int {
        let sorted = nums.sorted()
        var low = 0
        var high = sorted.last! - sorted.first!
        
        while low < high {
            let mid = (low + high) / 2
            var count = 0
            var left = 0
            for right in 0..<sorted.count {
                while sorted[right] - sorted[left] > mid {
                    left += 1
                }
                count += right - left
            }
            if count >= k {
                high = mid
            } else {
                low = mid + 1
            }
        }
        return low
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun smallestDistancePair(nums: IntArray, k: Int): Int {
        nums.sort()
        var low = 0
        var high = nums[nums.size - 1] - nums[0]
        while (low < high) {
            val mid = (low + high) ushr 1
            var count = 0
            var left = 0
            for (right in nums.indices) {
                while (nums[right] - nums[left] > mid) {
                    left++
                }
                count += right - left
            }
            if (count >= k) {
                high = mid
            } else {
                low = mid + 1
            }
        }
        return low
    }
}
```

## Dart

```dart
class Solution {
  int smallestDistancePair(List<int> nums, int k) {
    nums.sort();
    int low = 0;
    int high = nums.last - nums.first;

    while (low < high) {
      int mid = (low + high) >> 1;
      int count = 0;
      int left = 0;
      for (int right = 0; right < nums.length; ++right) {
        while (nums[right] - nums[left] > mid) {
          left++;
        }
        count += right - left;
      }

      if (count >= k) {
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
package main

import "sort"

func smallestDistancePair(nums []int, k int) int {
	sort.Ints(nums)
	low := 0
	high := nums[len(nums)-1] - nums[0]
	for low < high {
		mid := (low + high) / 2
		count, left := 0, 0
		for right, v := range nums {
			for v-nums[left] > mid {
				left++
			}
			count += right - left
		}
		if count >= k {
			high = mid
		} else {
			low = mid + 1
		}
	}
	return low
}
```

## Ruby

```ruby
def smallest_distance_pair(nums, k)
  nums.sort!
  low = 0
  high = nums[-1] - nums[0]
  while low < high
    mid = (low + high) / 2
    cnt = 0
    left = 0
    nums.each_with_index do |val, right|
      while val - nums[left] > mid
        left += 1
      end
      cnt += right - left
    end
    if cnt >= k
      high = mid
    else
      low = mid + 1
    end
  end
  low
end
```

## Scala

```scala
object Solution {
  def smallestDistancePair(nums: Array[Int], k: Int): Int = {
    java.util.Arrays.sort(nums)
    var low = 0
    var high = nums(nums.length - 1) - nums(0)

    def countPairs(maxDist: Int): Long = {
      var left = 0
      var total = 0L
      for (right <- nums.indices) {
        while (nums(right) - nums(left) > maxDist) left += 1
        total += (right - left)
      }
      total
    }

    while (low < high) {
      val mid = (low + high) >>> 1
      if (countPairs(mid) >= k) high = mid else low = mid + 1
    }
    low
  }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn smallest_distance_pair(nums: Vec<i32>, k: i32) -> i32 {
        let mut nums = nums;
        nums.sort_unstable();
        let n = nums.len();
        let mut low = 0i32;
        let mut high = nums[n - 1] - nums[0];
        while low < high {
            let mid = low + (high - low) / 2;
            let mut cnt: i64 = 0;
            let mut left = 0usize;
            for right in 0..n {
                while left < right && nums[right] - nums[left] > mid {
                    left += 1;
                }
                cnt += (right - left) as i64;
            }
            if cnt >= k as i64 {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        low
    }
}
```

## Racket

```racket
#lang racket

(define/contract (smallest-distance-pair nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([sorted-list (sort nums <)]
         [sorted (list->vector sorted-list)]
         [n (vector-length sorted)])
    (define (count-pairs maxDist)
      (let ([cnt 0]
            [left 0])
        (for ([right (in-range n)])
          (let recur ()
            (when (and (< left right)
                       (> (- (vector-ref sorted right) (vector-ref sorted left)) maxDist))
              (set! left (+ left 1))
              (recur)))
          (set! cnt (+ cnt (- right left))))
        cnt))
    (let loop ((low 0)
               (high (- (vector-ref sorted (sub1 n)) (vector-ref sorted 0))))
      (if (= low high)
          low
          (let* ([mid (quotient (+ low high) 2)]
                 [cnt (count-pairs mid)])
            (if (< cnt k)
                (loop (+ mid 1) high)
                (loop low mid)))))))
```

## Erlang

```erlang
-spec smallest_distance_pair([integer()], integer()) -> integer().
smallest_distance_pair(Nums, K) ->
    Sorted = lists:sort(Nums),
    High = max_minus_min(Sorted),
    binary_search(0, High, Sorted, K).

max_minus_min([]) -> 0;
max_minus_min([H|T]) ->
    Max = last_elem(T, H),
    Max - H.

last_elem([], Acc) -> Acc;
last_elem([X|Xs], _Acc) -> last_elem(Xs, X).

binary_search(Low, High, Sorted, K) when Low < High ->
    Mid = (Low + High) div 2,
    Count = count_pairs(Mid, Sorted),
    if
        Count >= K ->
            binary_search(Low, Mid, Sorted, K);
        true ->
            binary_search(Mid + 1, High, Sorted, K)
    end;
binary_search(Low, _High, _Sorted, _K) -> Low.

count_pairs(MaxDist, Sorted) ->
    count_pairs_loop(Sorted, Sorted, 0, 0, 0, MaxDist).

count_pairs_loop([], _LeftList, _RIdx, _LIdx, Acc, _MaxDist) ->
    Acc;
count_pairs_loop([RVal | RestRight], LeftList, RIdx, LIdx, Acc, MaxDist) ->
    {NewLeft, NewLIdx} = advance_left(LeftList, LIdx, RVal, MaxDist),
    NewAcc = Acc + (RIdx - NewLIdx),
    count_pairs_loop(RestRight, NewLeft, RIdx + 1, NewLIdx, NewAcc, MaxDist).

advance_left([], LIdx, _RVal, _MaxDist) ->
    {[], LIdx};
advance_left([LVal | Rest] = LeftList, LIdx, RVal, MaxDist)
        when RVal - LVal > MaxDist ->
    advance_left(Rest, LIdx + 1, RVal, MaxDist);
advance_left(LeftList, LIdx, _RVal, _MaxDist) ->
    {LeftList, LIdx}.
```

## Elixir

```elixir
defmodule Solution do
  @spec smallest_distance_pair(nums :: [integer], k :: integer) :: integer
  def smallest_distance_pair(nums, k) do
    sorted = Enum.sort(nums)
    arr = List.to_tuple(sorted)

    low = 0
    high = elem(arr, tuple_size(arr) - 1) - elem(arr, 0)

    binary_search(arr, low, high, k)
  end

  defp binary_search(_arr, low, high, _k) when low == high, do: low

  defp binary_search(arr, low, high, k) do
    mid = div(low + high, 2)
    cnt = count_pairs(arr, mid)

    if cnt >= k do
      binary_search(arr, low, mid, k)
    else
      binary_search(arr, mid + 1, high, k)
    end
  end

  defp count_pairs(arr, max_dist) do
    len = tuple_size(arr)
    count_pairs_recursive(arr, max_dist, 0, 0, 0, len)
  end

  defp count_pairs_recursive(_arr, _max_dist, left, right, cnt, len) when right == len,
    do: cnt

  defp count_pairs_recursive(arr, max_dist, left, right, cnt, len) do
    if elem(arr, right) - elem(arr, left) > max_dist do
      count_pairs_recursive(arr, max_dist, left + 1, right, cnt, len)
    else
      new_cnt = cnt + (right - left)
      count_pairs_recursive(arr, max_dist, left, right + 1, new_cnt, len)
    end
  end
end
```
