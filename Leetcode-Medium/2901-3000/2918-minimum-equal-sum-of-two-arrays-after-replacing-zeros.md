# 2918. Minimum Equal Sum of Two Arrays After Replacing Zeros

## Cpp

```cpp
class Solution {
public:
    long long minSum(vector<int>& nums1, vector<int>& nums2) {
        long long sum1 = 0, sum2 = 0;
        long long z1 = 0, z2 = 0;
        for (int v : nums1) {
            sum1 += v;
            if (v == 0) ++z1;
        }
        for (int v : nums2) {
            sum2 += v;
            if (v == 0) ++z2;
        }
        long long min1 = sum1 + z1; // replace each zero with 1
        long long min2 = sum2 + z2;
        
        if (z1 > 0 && z2 > 0) {
            return max(min1, min2);
        } else if (z1 > 0) { // only nums1 has zeros
            if (sum2 >= min1) return sum2;
            return -1;
        } else if (z2 > 0) { // only nums2 has zeros
            if (sum1 >= min2) return sum1;
            return -1;
        } else { // no zeros in either array
            return (sum1 == sum2) ? sum1 : -1;
        }
    }
};
```

## Java

```java
class Solution {
    public long minSum(int[] nums1, int[] nums2) {
        long sum1 = 0, sum2 = 0;
        int zero1 = 0, zero2 = 0;
        for (int v : nums1) {
            sum1 += v;
            if (v == 0) zero1++;
        }
        for (int v : nums2) {
            sum2 += v;
            if (v == 0) zero2++;
        }
        long minSum1 = sum1 + zero1; // all zeros become 1
        long minSum2 = sum2 + zero2;

        if (zero1 > 0 && zero2 > 0) {
            return Math.max(minSum1, minSum2);
        }
        if (zero1 == 0 && zero2 == 0) {
            return sum1 == sum2 ? sum1 : -1;
        }
        if (zero1 == 0) { // only nums2 has zeros
            return minSum2 <= sum1 ? sum1 : -1;
        } else { // only nums1 has zeros
            return minSum1 <= sum2 ? sum2 : -1;
        }
    }
}
```

## Python

```python
class Solution(object):
    def minSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        sum1 = 0
        zero1 = 0
        for v in nums1:
            if v == 0:
                zero1 += 1
            else:
                sum1 += v

        sum2 = 0
        zero2 = 0
        for v in nums2:
            if v == 0:
                zero2 += 1
            else:
                sum2 += v

        min1 = sum1 + zero1  # minimal achievable sum for nums1
        min2 = sum2 + zero2  # minimal achievable sum for nums2

        if zero1 > 0 and zero2 > 0:
            return max(min1, min2)
        if zero1 == 0 and zero2 == 0:
            return sum1 if sum1 == sum2 else -1
        if zero1 > 0:  # only nums1 has zeros
            return sum2 if sum2 >= min1 else -1
        else:          # only nums2 has zeros
            return sum1 if sum1 >= min2 else -1
```

## Python3

```python
from typing import List

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = 0
        zero1 = 0
        for v in nums1:
            sum1 += v
            if v == 0:
                zero1 += 1

        sum2 = 0
        zero2 = 0
        for v in nums2:
            sum2 += v
            if v == 0:
                zero2 += 1

        min1 = sum1 + zero1
        min2 = sum2 + zero2

        if zero1 > 0 and zero2 > 0:
            return max(min1, min2)
        if zero1 == 0 and zero2 == 0:
            return sum1 if sum1 == sum2 else -1
        if zero1 == 0:  # nums1 fixed
            return sum1 if sum1 >= min2 else -1
        # zero2 == 0, nums2 fixed
        return sum2 if sum2 >= min1 else -1
```

## C

```c
long long minSum(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    long long sum1 = 0, sum2 = 0;
    long long zero1 = 0, zero2 = 0;
    for (int i = 0; i < nums1Size; ++i) {
        if (nums1[i] == 0) zero1++;
        else sum1 += nums1[i];
    }
    for (int i = 0; i < nums2Size; ++i) {
        if (nums2[i] == 0) zero2++;
        else sum2 += nums2[i];
    }
    long long minSum1 = sum1 + zero1; // each zero at least 1
    long long minSum2 = sum2 + zero2;
    
    if (zero1 > 0 && zero2 > 0) {
        return minSum1 > minSum2 ? minSum1 : minSum2;
    }
    if (zero1 == 0 && zero2 == 0) {
        return (sum1 == sum2) ? sum1 : -1;
    }
    if (zero1 > 0) { // zero2 == 0
        if (minSum1 > sum2) return -1;
        return sum2;
    } else { // zero2 > 0, zero1 == 0
        if (minSum2 > sum1) return -1;
        return sum1;
    }
}
```

## Csharp

```csharp
public class Solution {
    public long MinSum(int[] nums1, int[] nums2) {
        long sum1 = 0, sum2 = 0;
        long zero1 = 0, zero2 = 0;

        foreach (int x in nums1) {
            if (x == 0) zero1++;
            else sum1 += x;
        }
        foreach (int x in nums2) {
            if (x == 0) zero2++;
            else sum2 += x;
        }

        long minSum1 = sum1 + zero1; // each zero replaced by at least 1
        long minSum2 = sum2 + zero2;

        if (zero1 == 0 && zero2 == 0) {
            return sum1 == sum2 ? sum1 : -1;
        } else if (zero1 == 0) { // only nums2 can be increased
            return sum1 >= minSum2 ? sum1 : -1;
        } else if (zero2 == 0) { // only nums1 can be increased
            return sum2 >= minSum1 ? sum2 : -1;
        } else {
            return Math.Max(minSum1, minSum2);
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var minSum = function(nums1, nums2) {
    let sum1 = 0, zero1 = 0;
    for (let v of nums1) {
        if (v === 0) zero1++;
        else sum1 += v;
    }
    let sum2 = 0, zero2 = 0;
    for (let v of nums2) {
        if (v === 0) zero2++;
        else sum2 += v;
    }

    const minSum1 = sum1 + zero1; // each zero at least 1
    const minSum2 = sum2 + zero2;

    if (zero1 > 0 && zero2 > 0) {
        return Math.max(minSum1, minSum2);
    }
    if (zero1 === 0 && zero2 === 0) {
        return sum1 === sum2 ? sum1 : -1;
    }
    // exactly one array has zeros
    if (zero1 > 0) { // nums2 fixed
        return minSum1 > sum2 ? -1 : sum2;
    } else { // zero2 > 0, nums1 fixed
        return minSum2 > sum1 ? -1 : sum1;
    }
};
```

## Typescript

```typescript
function minSum(nums1: number[], nums2: number[]): number {
    let sum1 = 0, zero1 = 0;
    for (const v of nums1) {
        if (v === 0) zero1++;
        else sum1 += v;
    }
    let sum2 = 0, zero2 = 0;
    for (const v of nums2) {
        if (v === 0) zero2++;
        else sum2 += v;
    }

    const min1 = sum1 + zero1; // all zeros become 1
    const min2 = sum2 + zero2;

    // both arrays have no zeros: sums are fixed
    if (zero1 === 0 && zero2 === 0) {
        return sum1 === sum2 ? sum1 : -1;
    }

    // nums1 has no zeros, its sum is fixed
    if (zero1 === 0) {
        return min2 > sum1 ? -1 : sum1;
    }

    // nums2 has no zeros, its sum is fixed
    if (zero2 === 0) {
        return min1 > sum2 ? -1 : sum2;
    }

    // both have at least one zero: we can raise the smaller side to match the larger minimal sum
    return Math.max(min1, min2);
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function minSum($nums1, $nums2) {
        $sum1 = 0;
        $zero1 = 0;
        foreach ($nums1 as $v) {
            if ($v == 0) {
                $zero1++;
            } else {
                $sum1 += $v;
            }
        }

        $sum2 = 0;
        $zero2 = 0;
        foreach ($nums2 as $v) {
            if ($v == 0) {
                $zero2++;
            } else {
                $sum2 += $v;
            }
        }

        $minSum1 = $sum1 + $zero1; // each zero at least 1
        $minSum2 = $sum2 + $zero2;

        if ($zero1 > 0 && $zero2 > 0) {
            return max($minSum1, $minSum2);
        }

        if ($zero1 == 0 && $zero2 == 0) {
            return $sum1 === $sum2 ? $sum1 : -1;
        }

        if ($zero1 == 0) { // only nums2 has zeros
            return $minSum2 > $sum1 ? -1 : $sum1;
        } else { // only nums1 has zeros
            return $minSum1 > $sum2 ? -1 : $sum2;
        }
    }
}
```

## Swift

```swift
class Solution {
    func minSum(_ nums1: [Int], _ nums2: [Int]) -> Int {
        var sum1 = 0
        var zero1 = 0
        for v in nums1 {
            if v == 0 {
                zero1 += 1
            } else {
                sum1 += v
            }
        }
        
        var sum2 = 0
        var zero2 = 0
        for v in nums2 {
            if v == 0 {
                zero2 += 1
            } else {
                sum2 += v
            }
        }
        
        let minSum1 = sum1 + zero1
        let minSum2 = sum2 + zero2
        
        if zero1 > 0 && zero2 > 0 {
            return max(minSum1, minSum2)
        } else if zero1 == 0 && zero2 == 0 {
            return sum1 == sum2 ? sum1 : -1
        } else if zero1 > 0 { // only nums1 has zeros
            let fixed = sum2
            return fixed >= minSum1 ? fixed : -1
        } else { // only nums2 has zeros
            let fixed = sum1
            return fixed >= minSum2 ? fixed : -1
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minSum(nums1: IntArray, nums2: IntArray): Long {
        var sum1 = 0L
        var zero1 = 0
        for (v in nums1) {
            if (v == 0) zero1++ else sum1 += v.toLong()
        }
        var sum2 = 0L
        var zero2 = 0
        for (v in nums2) {
            if (v == 0) zero2++ else sum2 += v.toLong()
        }
        val min1 = sum1 + zero1
        val min2 = sum2 + zero2

        return when {
            zero1 > 0 && zero2 > 0 -> kotlin.math.max(min1, min2)
            zero1 == 0 && zero2 == 0 -> if (sum1 == sum2) sum1 else -1L
            zero1 == 0 -> if (sum1 >= min2) sum1 else -1L
            else -> if (sum2 >= min1) sum2 else -1L
        }
    }
}
```

## Dart

```dart
class Solution {
  int minSum(List<int> nums1, List<int> nums2) {
    int sum1 = 0;
    int zero1 = 0;
    for (int v in nums1) {
      if (v == 0) {
        zero1++;
      } else {
        sum1 += v;
      }
    }

    int sum2 = 0;
    int zero2 = 0;
    for (int v in nums2) {
      if (v == 0) {
        zero2++;
      } else {
        sum2 += v;
      }
    }

    int min1 = sum1 + zero1; // replace all zeros with 1
    int min2 = sum2 + zero2;

    if (zero1 > 0 && zero2 > 0) {
      return min1 > min2 ? min1 : min2;
    } else if (zero1 == 0 && zero2 == 0) {
      return sum1 == sum2 ? sum1 : -1;
    } else if (zero1 == 0) {
      // nums1 cannot change
      return (min2 <= sum1) ? sum1 : -1;
    } else {
      // nums2 cannot change
      return (min1 <= sum2) ? sum2 : -1;
    }
  }
}
```

## Golang

```go
func minSum(nums1 []int, nums2 []int) int64 {
	var sum1, sum2 int64
	zero1, zero2 := 0, 0

	for _, v := range nums1 {
		sum1 += int64(v)
		if v == 0 {
			zero1++
		}
	}
	for _, v := range nums2 {
		sum2 += int64(v)
		if v == 0 {
			zero2++
		}
	}

	// No zeros in either array
	if zero1 == 0 && zero2 == 0 {
		if sum1 == sum2 {
			return sum1
		}
		return -1
	}

	// nums1 has no zeros, cannot increase its sum
	if zero1 == 0 {
		minSum2 := sum2 + int64(zero2) // replace all zeros in nums2 with 1
		if minSum2 > sum1 {
			return -1
		}
		// Increase nums2 to match sum1
		return sum1
	}

	// nums2 has no zeros, cannot increase its sum
	if zero2 == 0 {
		minSum1 := sum1 + int64(zero1) // replace all zeros in nums1 with 1
		if minSum1 > sum2 {
			return -1
		}
		// Increase nums1 to match sum2
		return sum2
	}

	// Both arrays have at least one zero
	minSum1 := sum1 + int64(zero1)
	minSum2 := sum2 + int64(zero2)
	if minSum1 > minSum2 {
		return minSum1
	}
	return minSum2
}
```

## Ruby

```ruby
def min_sum(nums1, nums2)
  sum1 = 0
  zero1 = 0
  nums1.each do |v|
    if v == 0
      zero1 += 1
    else
      sum1 += v
    end
  end

  sum2 = 0
  zero2 = 0
  nums2.each do |v|
    if v == 0
      zero2 += 1
    else
      sum2 += v
    end
  end

  min1 = sum1 + zero1
  min2 = sum2 + zero2

  if zero1 > 0 && zero2 > 0
    [min1, min2].max
  elsif zero1 > 0
    sum2 >= min1 ? sum2 : -1
  elsif zero2 > 0
    sum1 >= min2 ? sum1 : -1
  else
    sum1 == sum2 ? sum1 : -1
  end
end
```

## Scala

```scala
object Solution {
    def minSum(nums1: Array[Int], nums2: Array[Int]): Long = {
        var sum1: Long = 0L
        var zero1: Long = 0L
        for (v <- nums1) {
            if (v == 0) zero1 += 1 else sum1 += v
        }
        var sum2: Long = 0L
        var zero2: Long = 0L
        for (v <- nums2) {
            if (v == 0) zero2 += 1 else sum2 += v
        }

        val minSum1 = sum1 + zero1
        val minSum2 = sum2 + zero2

        if (zero1 == 0 && zero2 == 0) {
            if (sum1 == sum2) sum1 else -1L
        } else if (zero1 == 0) {
            if (minSum2 > sum1) -1L else sum1
        } else if (zero2 == 0) {
            if (minSum1 > sum2) -1L else sum2
        } else {
            math.max(minSum1, minSum2)
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_sum(nums1: Vec<i32>, nums2: Vec<i32>) -> i64 {
        let mut sum1: i64 = 0;
        let mut zero1: i64 = 0;
        for &v in &nums1 {
            if v == 0 {
                zero1 += 1;
            } else {
                sum1 += v as i64;
            }
        }

        let mut sum2: i64 = 0;
        let mut zero2: i64 = 0;
        for &v in &nums2 {
            if v == 0 {
                zero2 += 1;
            } else {
                sum2 += v as i64;
            }
        }

        // No zeros in either array
        if zero1 == 0 && zero2 == 0 {
            return if sum1 == sum2 { sum1 } else { -1 };
        }

        // Zeros present in both arrays
        if zero1 > 0 && zero2 > 0 {
            let min_sum1 = sum1 + zero1; // replace all zeros with 1
            let min_sum2 = sum2 + zero2;
            return std::cmp::max(min_sum1, min_sum2);
        }

        // Only nums1 has zeros
        if zero1 > 0 {
            let min_sum1 = sum1 + zero1;
            if min_sum1 <= sum2 {
                return sum2;
            } else {
                return -1;
            }
        }

        // Only nums2 has zeros
        let min_sum2 = sum2 + zero2;
        if min_sum2 <= sum1 {
            sum1
        } else {
            -1
        }
    }
}
```

## Racket

```racket
(define/contract (min-sum nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((sum1 (apply + nums1))
         (zero1 (length (filter zero? nums1)))
         (sum2 (apply + nums2))
         (zero2 (length (filter zero? nums2))))
    (cond
      [(and (= zero1 0) (= zero2 0))
       (if (= sum1 sum2) sum1 -1)]
      [(= zero1 0)
       (let ((min-sum2 (+ sum2 zero2)))
         (if (< sum1 min-sum2) -1 sum1))]
      [(= zero2 0)
       (let ((min-sum1 (+ sum1 zero1)))
         (if (< sum2 min-sum1) -1 sum2))]
      [else
       (max (+ sum1 zero1) (+ sum2 zero2))])))
```

## Erlang

```erlang
-module(solution).
-export([min_sum/2]).

-spec min_sum(Nums1 :: [integer()], Nums2 :: [integer()]) -> integer().
min_sum(Nums1, Nums2) ->
    {Sum1, Z1} = calc(Nums1),
    {Sum2, Z2} = calc(Nums2),
    Min1 = Sum1 + Z1,
    Min2 = Sum2 + Z2,
    case {Z1 > 0, Z2 > 0} of
        {true, true} ->
            erlang:max(Min1, Min2);
        {false, false} ->
            if Sum1 == Sum2 -> Sum1; true -> -1 end;
        {false, true} ->
            Fixed = Sum1,
            if Min2 > Fixed -> -1; true -> Fixed end;
        {true, false} ->
            Fixed = Sum2,
            if Min1 > Fixed -> -1; true -> Fixed end
    end.

calc(List) ->
    lists:foldl(fun(0,{Sum,ZeroCnt}) -> {Sum, ZeroCnt+1};
                (Val,{Sum,ZeroCnt}) -> {Sum+Val, ZeroCnt}
               end, {0,0}, List).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_sum(nums1 :: [integer], nums2 :: [integer]) :: integer
  def min_sum(nums1, nums2) do
    {sum1, zero1} =
      Enum.reduce(nums1, {0, 0}, fn x, {s, z} ->
        {s + x, z + if x == 0, do: 1, else: 0}
      end)

    {sum2, zero2} =
      Enum.reduce(nums2, {0, 0}, fn x, {s, z} ->
        {s + x, z + if x == 0, do: 1, else: 0}
      end)

    min_sum1 = sum1 + zero1
    min_sum2 = sum2 + zero2

    cond do
      zero1 > 0 and zero2 > 0 ->
        max(min_sum1, min_sum2)

      zero1 == 0 and zero2 == 0 ->
        if sum1 == sum2, do: sum1, else: -1

      zero1 > 0 ->
        if sum2 >= min_sum1, do: sum2, else: -1

      true ->
        # zero2 > 0
        if sum1 >= min_sum2, do: sum1, else: -1
    end
  end
end
```
