# 1760. Minimum Limit of Balls in a Bag

## Cpp

```cpp
class Solution {
public:
    int minimumSize(std::vector<int>& nums, int maxOperations) {
        long long maxOps = maxOperations;
        int left = 1;
        int right = *std::max_element(nums.begin(), nums.end());
        
        auto can = [&](int limit) -> bool {
            long long opsNeeded = 0;
            for (int x : nums) {
                // number of pieces needed so that each piece <= limit
                long long pieces = (x + limit - 1LL) / limit;
                opsNeeded += pieces - 1; // splits required
                if (opsNeeded > maxOps) return false;
            }
            return true;
        };
        
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (can(mid))
                right = mid;
            else
                left = mid + 1;
        }
        return left;
    }
};
```

## Java

```java
class Solution {
    public int minimumSize(int[] nums, int maxOperations) {
        int left = 1;
        int right = 0;
        for (int v : nums) {
            if (v > right) right = v;
        }
        while (left < right) {
            int mid = left + (right - left) / 2;
            long opsNeeded = 0;
            for (int v : nums) {
                opsNeeded += ((long) v + mid - 1) / mid - 1;
                if (opsNeeded > maxOperations) break;
            }
            if (opsNeeded <= maxOperations) {
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
    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """
        def can(limit):
            ops = 0
            for x in nums:
                # splits needed so that each part <= limit
                ops += (x - 1) // limit
                if ops > maxOperations:
                    return False
            return True

        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if can(mid):
                right = mid
            else:
                left = mid + 1
        return left
```

## Python3

```python
from typing import List

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def can(limit: int) -> bool:
            ops = 0
            for x in nums:
                ops += (x - 1) // limit
                if ops > maxOperations:
                    return False
            return True

        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if can(mid):
                right = mid
            else:
                left = mid + 1
        return left
```

## C

```c
#include <stdbool.h>

static bool canAchieve(int *nums, int numsSize, long long maxOps, long long limit) {
    long long used = 0;
    for (int i = 0; i < numsSize; ++i) {
        // operations needed = ceil(nums[i] / limit) - 1
        long long ops = (nums[i] + limit - 1) / limit - 1;
        used += ops;
        if (used > maxOps) return false;
    }
    return true;
}

int minimumSize(int* nums, int numsSize, int maxOperations) {
    int maxVal = 0;
    for (int i = 0; i < numsSize; ++i)
        if (nums[i] > maxVal) maxVal = nums[i];

    long long left = 1, right = maxVal;
    while (left < right) {
        long long mid = left + (right - left) / 2;
        if (canAchieve(nums, numsSize, maxOperations, mid))
            right = mid;
        else
            left = mid + 1;
    }
    return (int)left;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinimumSize(int[] nums, int maxOperations)
    {
        int left = 1;
        int right = 0;
        foreach (int v in nums)
            if (v > right) right = v;

        bool Can(int limit)
        {
            long ops = 0;
            foreach (int v in nums)
            {
                ops += ((v + limit - 1) / limit) - 1;
                if (ops > maxOperations) return false;
            }
            return true;
        }

        while (left < right)
        {
            int mid = left + (right - left) / 2;
            if (Can(mid))
                right = mid;
            else
                left = mid + 1;
        }

        return left;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} maxOperations
 * @return {number}
 */
var minimumSize = function(nums, maxOperations) {
    const can = (limit) => {
        let ops = 0;
        for (let v of nums) {
            // operations needed = ceil(v / limit) - 1 = floor((v-1)/limit)
            ops += Math.floor((v - 1) / limit);
            if (ops > maxOperations) return false;
        }
        return true;
    };
    
    let left = 1;
    let right = Math.max(...nums);
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (can(mid)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
};
```

## Typescript

```typescript
function minimumSize(nums: number[], maxOperations: number): number {
    const can = (limit: number): boolean => {
        let ops = 0;
        for (const v of nums) {
            // operations needed to make each part <= limit
            ops += Math.floor((v - 1) / limit);
            if (ops > maxOperations) return false;
        }
        return true;
    };

    let left = 1;
    let right = Math.max(...nums);
    while (left < right) {
        const mid = Math.floor((left + right) >> 1);
        if (can(mid)) {
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
     * @param Integer $maxOperations
     * @return Integer
     */
    function minimumSize($nums, $maxOperations) {
        $left = 1;
        $right = max($nums);
        while ($left < $right) {
            $mid = intdiv($left + $right, 2);
            if ($this->canAchieve($nums, $maxOperations, $mid)) {
                $right = $mid;
            } else {
                $left = $mid + 1;
            }
        }
        return $left;
    }

    private function canAchieve($nums, $maxOps, $limit) {
        $opsNeeded = 0;
        foreach ($nums as $num) {
            $ops = intdiv($num + $limit - 1, $limit) - 1;
            $opsNeeded += $ops;
            if ($opsNeeded > $maxOps) {
                return false;
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func minimumSize(_ nums: [Int], _ maxOperations: Int) -> Int {
        var left = 1
        var right = nums.max()!
        
        func canAchieve(_ limit: Int) -> Bool {
            var opsNeeded = 0
            for v in nums {
                // ceil division without floating point
                let splits = (v + limit - 1) / limit - 1
                opsNeeded += splits
                if opsNeeded > maxOperations {
                    return false
                }
            }
            return true
        }
        
        while left < right {
            let mid = (left + right) / 2
            if canAchieve(mid) {
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
    fun minimumSize(nums: IntArray, maxOperations: Int): Int {
        var left = 1
        var right = nums.maxOrNull() ?: 0
        val maxOpsLong = maxOperations.toLong()
        fun can(limit: Int): Boolean {
            var ops = 0L
            for (v in nums) {
                // splits needed so that each part <= limit
                val need = ((v.toLong() + limit - 1) / limit) - 1
                ops += need
                if (ops > maxOpsLong) return false
            }
            return true
        }
        while (left < right) {
            val mid = left + (right - left) / 2
            if (can(mid)) {
                right = mid
            } else {
                left = mid + 1
            }
        }
        return left
    }
}
```

## Dart

```dart
class Solution {
  int minimumSize(List<int> nums, int maxOperations) {
    int left = 1;
    int right = 0;
    for (var v in nums) {
      if (v > right) right = v;
    }

    bool can(int limit) {
      int opsNeeded = 0;
      for (var v in nums) {
        // ceil(v / limit) - 1
        opsNeeded += ((v + limit - 1) ~/ limit) - 1;
        if (opsNeeded > maxOperations) return false;
      }
      return true;
    }

    while (left < right) {
      int mid = left + ((right - left) >> 1);
      if (can(mid)) {
        right = mid;
      } else {
        left = mid + 1;
      }
    }
    return left;
  }
}
```

## Golang

```go
func minimumSize(nums []int, maxOperations int) int {
	if len(nums) == 0 {
		return 0
	}
	maxVal := nums[0]
	for _, v := range nums {
		if v > maxVal {
			maxVal = v
		}
	}
	left, right := 1, maxVal
	for left < right {
		mid := (left + right) / 2
		if can(mid, nums, maxOperations) {
			right = mid
		} else {
			left = mid + 1
		}
	}
	return left
}

func can(limit int, nums []int, maxOps int) bool {
	var ops int64
	lim := int64(limit)
	maxOps64 := int64(maxOps)
	for _, v := range nums {
		val := int64(v)
		ops += (val - 1) / lim // ceil(val/limit)-1
		if ops > maxOps64 {
			return false
		}
	}
	return true
}
```

## Ruby

```ruby
def minimum_size(nums, max_operations)
  left = 1
  right = nums.max
  while left < right
    mid = (left + right) / 2
    ops_needed = 0
    nums.each do |v|
      ops_needed += (v + mid - 1) / mid - 1
      break if ops_needed > max_operations
    end
    if ops_needed <= max_operations
      right = mid
    else
      left = mid + 1
    end
  end
  left
end
```

## Scala

```scala
object Solution {
  def minimumSize(nums: Array[Int], maxOperations: Int): Int = {
    val maxOpsLong = maxOperations.toLong
    var left: Long = 1L
    var right: Long = nums.max.toLong

    def possible(limit: Long): Boolean = {
      var opsNeeded: Long = 0L
      for (v <- nums) {
        // Number of splits needed so that each part <= limit
        val need = (v.toLong + limit - 1) / limit - 1
        opsNeeded += need
        if (opsNeeded > maxOpsLong) return false
      }
      true
    }

    while (left < right) {
      val mid = (left + right) >>> 1 // avoid overflow, use unsigned shift for division by 2
      if (possible(mid)) {
        right = mid
      } else {
        left = mid + 1
      }
    }
    left.toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_size(nums: Vec<i32>, max_operations: i32) -> i32 {
        let max_val = *nums.iter().max().unwrap() as i64;
        let mut left: i64 = 1;
        let mut right: i64 = max_val;
        let max_ops = max_operations as i64;

        while left < right {
            let mid = (left + right) / 2;
            if Self::can(mid, &nums, max_ops) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        left as i32
    }

    fn can(limit: i64, nums: &[i32], max_ops: i64) -> bool {
        let mut ops_needed: i64 = 0;
        for &v in nums.iter() {
            let v64 = v as i64;
            // operations needed = ceil(v / limit) - 1
            ops_needed += (v64 + limit - 1) / limit - 1;
            if ops_needed > max_ops {
                return false;
            }
        }
        true
    }
}
```

## Racket

```racket
#lang racket

(define/contract (minimum-size nums maxOperations)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((left 1)
         (right (apply max nums)))
    (define (is-possible limit)
      (let loop ((lst nums) (total 0))
        (cond
          [(null? lst) #t]
          [else
           (define n (car lst))
           (define needed (quotient (+ n (sub1 limit)) limit)) ; ceil division
           (define new-total (+ total (- needed 1)))            ; ops for this bag
           (if (> new-total maxOperations)
               #f
               (loop (cdr lst) new-total))])))
    (letrec ((search (lambda (l r)
                       (if (= l r)
                           l
                           (let* ((mid (quotient (+ l r) 2))
                                  (possible? (is-possible mid)))
                             (if possible?
                                 (search l mid)
                                 (search (add1 mid) r)))))))
      (search left right))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_size/2]).

-spec minimum_size(Nums :: [integer()], MaxOperations :: integer()) -> integer().
minimum_size(Nums, MaxOperations) ->
    MaxNum = lists:max(Nums),
    binary_search(1, MaxNum, Nums, MaxOperations).

binary_search(L, R, Nums, MaxOps) when L < R ->
    Mid = (L + R) div 2,
    case possible(Mid, Nums, MaxOps) of
        true -> binary_search(L, Mid, Nums, MaxOps);
        false -> binary_search(Mid + 1, R, Nums, MaxOps)
    end;
binary_search(L, _R, _Nums, _MaxOps) ->
    L.

possible(MaxBag, Nums, MaxOps) ->
    Total = lists:foldl(fun(Num, Acc) ->
                Ops = ((Num + MaxBag - 1) div MaxBag) - 1,
                Acc + Ops
            end, 0, Nums),
    Total =< MaxOps.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_size(nums :: [integer], max_operations :: integer) :: integer
  def minimum_size(nums, max_operations) do
    left = 1
    right = Enum.max(nums)
    binary_search(left, right, nums, max_operations)
  end

  defp binary_search(left, right, _nums, _max_ops) when left == right, do: left

  defp binary_search(left, right, nums, max_ops) do
    mid = div(left + right, 2)

    if possible?(nums, max_ops, mid) do
      binary_search(left, mid, nums, max_ops)
    else
      binary_search(mid + 1, right, nums, max_ops)
    end
  end

  defp possible?([], _max_ops, _limit), do: true

  defp possible?([h | t], max_ops, limit) when max_ops >= 0 do
    needed = div(h + limit - 1, limit) - 1

    if needed > max_ops do
      false
    else
      possible?(t, max_ops - needed, limit)
    end
  end
end
```
