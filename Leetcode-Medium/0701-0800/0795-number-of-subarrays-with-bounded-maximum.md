# 0795. Number of Subarrays with Bounded Maximum

## Cpp

```cpp
class Solution {
public:
    int numSubarrayBoundedMax(vector<int>& nums, int left, int right) {
        auto countBound = [&](int bound) -> long long {
            long long res = 0, cur = 0;
            for (int x : nums) {
                if (x <= bound) {
                    ++cur;
                } else {
                    cur = 0;
                }
                res += cur;
            }
            return res;
        };
        long long total = countBound(right);
        long long lessThanLeft = countBound(left - 1);
        return static_cast<int>(total - lessThanLeft);
    }
};
```

## Java

```java
class Solution {
    public int numSubarrayBoundedMax(int[] nums, int left, int right) {
        return count(nums, right) - count(nums, left - 1);
    }

    private int count(int[] nums, int bound) {
        int ans = 0;
        int cur = 0;
        for (int x : nums) {
            if (x <= bound) {
                cur++;
            } else {
                cur = 0;
            }
            ans += cur;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def numSubarrayBoundedMax(self, nums, left, right):
        """
        :type nums: List[int]
        :type left: int
        :type right: int
        :rtype: int
        """
        def count(bound):
            total = cur = 0
            for v in nums:
                if v <= bound:
                    cur += 1
                else:
                    cur = 0
                total += cur
            return total

        return count(right) - count(left - 1)
```

## Python3

```python
from typing import List

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count(bound: int) -> int:
            total = cur = 0
            for v in nums:
                if v <= bound:
                    cur += 1
                else:
                    cur = 0
                total += cur
            return total

        return count(right) - count(left - 1)
```

## C

```c
int numSubarrayBoundedMax(int* nums, int numsSize, int left, int right) {
    long long countLeq(int bound) {
        long long res = 0;
        int cur = 0;
        for (int i = 0; i < numsSize; ++i) {
            if (nums[i] <= bound) {
                ++cur;
            } else {
                cur = 0;
            }
            res += cur;
        }
        return res;
    }
    
    long long totalRight = countLeq(right);
    long long totalLeftMinusOne = countLeq(left - 1);
    return (int)(totalRight - totalLeftMinusOne);
}
```

## Csharp

```csharp
public class Solution
{
    public int NumSubarrayBoundedMax(int[] nums, int left, int right)
    {
        return (int)(Count(nums, right) - Count(nums, left - 1));
    }

    private long Count(int[] nums, int bound)
    {
        long total = 0;
        long cur = 0;
        foreach (var x in nums)
        {
            if (x <= bound)
            {
                cur++;
            }
            else
            {
                cur = 0;
            }
            total += cur;
        }
        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} left
 * @param {number} right
 * @return {number}
 */
var numSubarrayBoundedMax = function(nums, left, right) {
    const count = (bound) => {
        let cur = 0;
        let total = 0;
        for (const x of nums) {
            if (x <= bound) {
                cur += 1;
            } else {
                cur = 0;
            }
            total += cur;
        }
        return total;
    };
    
    return count(right) - count(left - 1);
};
```

## Typescript

```typescript
function numSubarrayBoundedMax(nums: number[], left: number, right: number): number {
    const count = (bound: number): number => {
        let res = 0;
        let cur = 0;
        for (const x of nums) {
            if (x <= bound) {
                cur += 1;
                res += cur;
            } else {
                cur = 0;
            }
        }
        return res;
    };
    return count(right) - count(left - 1);
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $left
     * @param Integer $right
     * @return Integer
     */
    function numSubarrayBoundedMax($nums, $left, $right) {
        $count = function($arr, $bound) {
            $res = 0;
            $curr = 0;
            foreach ($arr as $v) {
                if ($v <= $bound) {
                    $curr++;
                } else {
                    $curr = 0;
                }
                $res += $curr;
            }
            return $res;
        };
        $totalRight = $count($nums, $right);
        $totalLeftMinusOne = $count($nums, $left - 1);
        return $totalRight - $totalLeftMinusOne;
    }
}
```

## Swift

```swift
class Solution {
    func numSubarrayBoundedMax(_ nums: [Int], _ left: Int, _ right: Int) -> Int {
        var result = 0
        var lastInvalid = -1   // index of most recent element > right
        var lastValid = -1     // index of most recent element within [left, right]
        
        for i in 0..<nums.count {
            let value = nums[i]
            if value > right {
                lastInvalid = i
            }
            if value >= left && value <= right {
                lastValid = i
            }
            let add = max(0, lastValid - lastInvalid)
            result += add
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numSubarrayBoundedMax(nums: IntArray, left: Int, right: Int): Int {
        fun count(bound: Int): Long {
            var total = 0L
            var cur = 0L
            for (v in nums) {
                if (v <= bound) {
                    cur++
                    total += cur
                } else {
                    cur = 0
                }
            }
            return total
        }
        val result = count(right) - count(left - 1)
        return result.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int numSubarrayBoundedMax(List<int> nums, int left, int right) {
    return _count(nums, right) - _count(nums, left - 1);
  }

  int _count(List<int> nums, int bound) {
    int ans = 0;
    int cur = 0;
    for (int x in nums) {
      if (x <= bound) {
        cur += 1;
      } else {
        cur = 0;
      }
      ans += cur;
    }
    return ans;
  }
}
```

## Golang

```go
func numSubarrayBoundedMax(nums []int, left int, right int) int {
	count := func(bound int) int {
		res, cur := 0, 0
		for _, v := range nums {
			if v <= bound {
				cur++
				res += cur
			} else {
				cur = 0
			}
		}
		return res
	}
	return count(right) - count(left-1)
}
```

## Ruby

```ruby
def num_subarray_bounded_max(nums, left, right)
  res = 0
  start = -1   # index of last element > right
  last = -1    # index of last element within [left, right]
  nums.each_with_index do |x, i|
    start = i if x > right
    last = i if x >= left && x <= right
    res += [0, last - start].max
  end
  res
end
```

## Scala

```scala
object Solution {
    def numSubarrayBoundedMax(nums: Array[Int], left: Int, right: Int): Int = {
        def count(bound: Int): Long = {
            var cur = 0L
            var total = 0L
            var i = 0
            while (i < nums.length) {
                if (nums(i) <= bound) cur += 1 else cur = 0
                total += cur
                i += 1
            }
            total
        }
        (count(right) - count(left - 1)).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_subarray_bounded_max(nums: Vec<i32>, left: i32, right: i32) -> i32 {
        let mut res: i64 = 0;
        let mut last_invalid: i32 = -1; // index of element > right
        let mut last_valid: i32 = -1;   // index of element >= left
        for (i, &v) in nums.iter().enumerate() {
            if v > right {
                last_invalid = i as i32;
            }
            if v >= left {
                last_valid = i as i32;
            }
            let add = last_valid - last_invalid;
            if add > 0 {
                res += add as i64;
            }
        }
        res as i32
    }
}
```

## Racket

```racket
(define (count-bound nums bound)
  (let loop ((lst nums) (cur 0) (total 0))
    (if (null? lst)
        total
        (let* ((x (car lst))
               (new-cur (if (<= x bound) (+ cur 1) 0)))
          (loop (cdr lst) new-cur (+ total new-cur))))))

(define/contract (num-subarray-bounded-max nums left right)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (- (count-bound nums right)
     (count-bound nums (- left 1))))
```

## Erlang

```erlang
-module(solution).
-export([num_subarray_bounded_max/3]).

-spec num_subarray_bounded_max(Nums :: [integer()], Left :: integer(), Right :: integer()) -> integer().
num_subarray_bounded_max(Nums, Left, Right) ->
    CountRight = count(Nums, Right),
    CountLeftMinusOne = count(Nums, Left - 1),
    CountRight - CountLeftMinusOne.

-spec count([integer()], integer()) -> integer().
count(Nums, Bound) ->
    {_, Total} = lists:foldl(
        fun(Elem, {Cur, Tot}) ->
            if Elem =< Bound ->
                NewCur = Cur + 1,
                {NewCur, Tot + NewCur};
               true ->
                {0, Tot}
            end
        end,
        {0,0},
        Nums),
    Total.
```

## Elixir

```elixir
defmodule Solution do
  @spec num_subarray_bounded_max(nums :: [integer], left :: integer, right :: integer) :: integer
  def num_subarray_bounded_max(nums, left, right) do
    count(nums, right) - count(nums, left - 1)
  end

  defp count(nums, bound) do
    {total, _} =
      Enum.reduce(nums, {0, 0}, fn x, {acc, cur} ->
        if x <= bound do
          new_cur = cur + 1
          {acc + new_cur, new_cur}
        else
          {acc, 0}
        end
      end)

    total
  end
end
```
