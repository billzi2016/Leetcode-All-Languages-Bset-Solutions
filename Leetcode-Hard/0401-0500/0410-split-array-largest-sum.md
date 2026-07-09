# 0410. Split Array Largest Sum

## Cpp

```cpp
class Solution {
public:
    bool canSplit(const vector<int>& nums, long long maxSum, int k) {
        int count = 1;
        long long cur = 0;
        for (int num : nums) {
            if (cur + num > maxSum) {
                ++count;
                cur = num;
                if (count > k) return false;
            } else {
                cur += num;
            }
        }
        return true;
    }

    int splitArray(vector<int>& nums, int k) {
        long long low = 0, high = 0;
        for (int v : nums) {
            low = max<long long>(low, v);
            high += v;
        }
        while (low < high) {
            long long mid = low + (high - low) / 2;
            if (canSplit(nums, mid, k))
                high = mid;
            else
                low = mid + 1;
        }
        return static_cast<int>(low);
    }
};
```

## Java

```java
class Solution {
    public int splitArray(int[] nums, int k) {
        long low = 0;
        long high = 0;
        for (int num : nums) {
            low = Math.max(low, num);
            high += num;
        }
        while (low < high) {
            long mid = low + (high - low) / 2;
            if (canSplit(nums, k, mid)) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return (int) low;
    }

    private boolean canSplit(int[] nums, int k, long maxAllowed) {
        int required = 1;
        long currentSum = 0;
        for (int num : nums) {
            if (currentSum + num > maxAllowed) {
                required++;
                currentSum = num;
                if (required > k) {
                    return false;
                }
            } else {
                currentSum += num;
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left, right = max(nums), sum(nums)

        def can_split(limit):
            cnt, cur = 1, 0
            for x in nums:
                if cur + x > limit:
                    cnt += 1
                    cur = x
                    if cnt > k:
                        return False
                else:
                    cur += x
            return True

        while left < right:
            mid = (left + right) // 2
            if can_split(mid):
                right = mid
            else:
                left = mid + 1
        return left
```

## Python3

```python
from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)

        def can_split(limit: int) -> bool:
            cnt = 1
            cur = 0
            for x in nums:
                if cur + x > limit:
                    cnt += 1
                    cur = x
                    if cnt > k:
                        return False
                else:
                    cur += x
            return True

        while low < high:
            mid = (low + high) // 2
            if can_split(mid):
                high = mid
            else:
                low = mid + 1
        return low
```

## C

```c
#include <stddef.h>

int splitArray(int* nums, int numsSize, int k) {
    long long left = 0, right = 0;
    for (int i = 0; i < numsSize; ++i) {
        if ((long long)nums[i] > left) left = nums[i];
        right += nums[i];
    }
    while (left < right) {
        long long mid = left + (right - left) / 2;
        int required = 1;
        long long cur = 0;
        for (int i = 0; i < numsSize; ++i) {
            if (cur + nums[i] > mid) {
                ++required;
                cur = nums[i];
            } else {
                cur += nums[i];
            }
        }
        if (required <= k)
            right = mid;
        else
            left = mid + 1;
    }
    return (int)left;
}
```

## Csharp

```csharp
public class Solution {
    public int SplitArray(int[] nums, int k) {
        int left = 0;
        long right = 0;
        foreach (int num in nums) {
            if (num > left) left = num;
            right += num;
        }
        while (left < right) {
            int mid = left + (int)((right - left) / 2);
            if (CanSplit(nums, k, mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    private bool CanSplit(int[] nums, int k, int maxSum) {
        int subarrays = 1;
        long current = 0;
        foreach (int num in nums) {
            if (current + num > maxSum) {
                subarrays++;
                current = num;
                if (subarrays > k) return false;
            } else {
                current += num;
            }
        }
        return true;
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
var splitArray = function(nums, k) {
    let low = Math.max(...nums);
    let high = nums.reduce((a, b) => a + b, 0);
    
    const canSplit = (limit) => {
        let groups = 1;
        let curSum = 0;
        for (const num of nums) {
            if (curSum + num > limit) {
                groups++;
                curSum = num;
                if (groups > k) return false;
            } else {
                curSum += num;
            }
        }
        return true;
    };
    
    while (low < high) {
        const mid = Math.floor((low + high) / 2);
        if (canSplit(mid)) {
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
function splitArray(nums: number[], k: number): number {
    let left = Math.max(...nums);
    let right = nums.reduce((sum, v) => sum + v, 0);

    const canSplit = (limit: number): boolean => {
        let groups = 1;
        let curSum = 0;
        for (const num of nums) {
            if (curSum + num > limit) {
                groups++;
                curSum = num;
                if (groups > k) return false;
            } else {
                curSum += num;
            }
        }
        return true;
    };

    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (canSplit(mid)) {
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
     * @param Integer $k
     * @return Integer
     */
    function splitArray($nums, $k) {
        $low = max($nums);
        $high = array_sum($nums);

        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            if ($this->canSplit($nums, $k, $mid)) {
                $high = $mid;
            } else {
                $low = $mid + 1;
            }
        }

        return $low;
    }

    private function canSplit($nums, $k, $limit) {
        $cnt = 1;
        $curr = 0;
        foreach ($nums as $num) {
            if ($curr + $num > $limit) {
                $cnt++;
                $curr = $num;
                if ($cnt > $k) {
                    return false;
                }
            } else {
                $curr += $num;
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func splitArray(_ nums: [Int], _ k: Int) -> Int {
        var low = nums.max() ?? 0
        var high = nums.reduce(0, +)
        
        while low < high {
            let mid = (low + high) / 2
            if canSplit(nums, k, limit: mid) {
                high = mid
            } else {
                low = mid + 1
            }
        }
        return low
    }
    
    private func canSplit(_ nums: [Int], _ k: Int, limit: Int) -> Bool {
        var required = 1
        var currentSum = 0
        for num in nums {
            if currentSum + num > limit {
                required += 1
                currentSum = num
                if required > k { return false }
            } else {
                currentSum += num
            }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun splitArray(nums: IntArray, k: Int): Int {
        var left = nums.maxOrNull()!!.toLong()
        var right = nums.fold(0L) { acc, v -> acc + v }
        while (left < right) {
            val mid = (left + right) / 2
            if (canSplit(nums, mid, k)) {
                right = mid
            } else {
                left = mid + 1
            }
        }
        return left.toInt()
    }

    private fun canSplit(nums: IntArray, limit: Long, k: Int): Boolean {
        var required = 1
        var currentSum = 0L
        for (num in nums) {
            if (currentSum + num > limit) {
                required++
                currentSum = num.toLong()
                if (required > k) return false
            } else {
                currentSum += num
            }
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  int splitArray(List<int> nums, int k) {
    int left = nums[0];
    int right = 0;
    for (int num in nums) {
      if (num > left) left = num;
      right += num;
    }

    bool canSplit(int maxSum) {
      int count = 1;
      int current = 0;
      for (int num in nums) {
        if (current + num > maxSum) {
          count++;
          current = num;
          if (count > k) return false;
        } else {
          current += num;
        }
      }
      return true;
    }

    while (left < right) {
      int mid = left + ((right - left) >> 1);
      if (canSplit(mid)) {
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
func splitArray(nums []int, k int) int {
	// Find the lower and upper bounds for binary search.
	maxNum := 0
	sum := 0
	for _, v := range nums {
		if v > maxNum {
			maxNum = v
		}
		sum += v
	}
	low, high := maxNum, sum

	// Helper to check if we can split into <=k subarrays with each sum <= limit.
	canSplit := func(limit int) bool {
		subCount := 1
		current := 0
		for _, v := range nums {
			if current+v > limit {
				subCount++
				current = v
				if subCount > k {
					return false
				}
			} else {
				current += v
			}
		}
		return true
	}

	// Binary search for the minimal feasible maximum subarray sum.
	for low < high {
		mid := (low + high) / 2
		if canSplit(mid) {
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
def split_array(nums, k)
  left = nums.max
  right = nums.sum
  while left < right
    mid = (left + right) / 2
    required = 1
    cur = 0
    nums.each do |num|
      if cur + num <= mid
        cur += num
      else
        required += 1
        cur = num
      end
    end
    if required <= k
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
    def splitArray(nums: Array[Int], k: Int): Int = {
        var low: Long = nums.max.toLong
        var high: Long = nums.map(_.toLong).sum
        while (low < high) {
            val mid = (low + high) / 2
            var required = 1
            var cur: Long = 0
            for (num <- nums) {
                if (cur + num > mid) {
                    required += 1
                    cur = num
                } else {
                    cur += num
                }
            }
            if (required <= k) high = mid
            else low = mid + 1
        }
        low.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn split_array(nums: Vec<i32>, k: i32) -> i32 {
        let mut lo = *nums.iter().max().unwrap() as i64;
        let mut hi: i64 = nums.iter().map(|&x| x as i64).sum();
        let k = k as usize;

        while lo < hi {
            let mid = (lo + hi) / 2;
            if Self::can_split(&nums, mid, k) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo as i32
    }

    fn can_split(nums: &[i32], limit: i64, k: usize) -> bool {
        let mut count = 1usize;
        let mut cur: i64 = 0;
        for &num in nums {
            let val = num as i64;
            if cur + val <= limit {
                cur += val;
            } else {
                count += 1;
                cur = val;
                if count > k {
                    return false;
                }
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (split-array nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (define (can-split? limit)
    (let loop ((lst nums) (curr 0) (cnt 1))
      (cond
        [(null? lst) (<= cnt k)]
        [else
         (let ((x (car lst)))
           (if (> (+ curr x) limit)
               (loop (cdr lst) x (+ cnt 1))
               (loop (cdr lst) (+ curr x) cnt)))])))
  (define max-num (apply max nums))
  (define sum-num (apply + nums))
  (let loop ((low max-num) (high sum-num))
    (if (= low high)
        low
        (let* ((mid (quotient (+ low high) 2))
               (feas (can-split? mid)))
          (if feas
              (loop low mid)
              (loop (+ mid 1) high))))))
```

## Erlang

```erlang
-module(solution).
-export([split_array/2]).

-spec split_array(Nums :: [integer()], K :: integer()) -> integer().
split_array(Nums, K) ->
    Max = lists:max(Nums),
    Sum = lists:foldl(fun(X, Acc) -> X + Acc end, 0, Nums),
    binary_search(Max, Sum, Nums, K).

binary_search(Low, High, _Nums, _K) when Low >= High ->
    Low;
binary_search(Low, High, Nums, K) ->
    Mid = (Low + High) div 2,
    case feasible(Nums, K, Mid) of
        true -> binary_search(Low, Mid, Nums, K);
        false -> binary_search(Mid + 1, High, Nums, K)
    end.

feasible(Nums, K, Limit) ->
    {Count, _} = lists:foldl(
        fun(X, {Cnt, Cur}) ->
            if
                Cur + X > Limit -> {Cnt + 1, X};
                true -> {Cnt, Cur + X}
            end
        end,
        {1, 0},
        Nums),
    Count =< K.
```

## Elixir

```elixir
defmodule Solution do
  @spec split_array(nums :: [integer], k :: integer) :: integer
  def split_array(nums, k) do
    low = Enum.max(nums)
    high = Enum.sum(nums)

    binary_search(nums, k, low, high)
  end

  defp binary_search(_nums, _k, low, high) when low == high, do: low

  defp binary_search(nums, k, low, high) do
    mid = div(low + high, 2)

    if feasible?(nums, k, mid) do
      binary_search(nums, k, low, mid)
    else
      binary_search(nums, k, mid + 1, high)
    end
  end

  defp feasible?(nums, k, limit) do
    {cnt, _} =
      Enum.reduce(nums, {1, 0}, fn num, {cnt, cur_sum} ->
        if cur_sum + num > limit do
          {cnt + 1, num}
        else
          {cnt, cur_sum + num}
        end
      end)

    cnt <= k
  end
end
```
