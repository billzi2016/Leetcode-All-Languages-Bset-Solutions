# 0152. Maximum Product Subarray

## Cpp

```cpp
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        long long curMax = nums[0];
        long long curMin = nums[0];
        long long ans = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] < 0) swap(curMax, curMin);
            curMax = max((long long)nums[i], curMax * nums[i]);
            curMin = min((long long)nums[i], curMin * nums[i]);
            ans = max(ans, curMax);
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int maxProduct(int[] nums) {
        int curMax = nums[0];
        int curMin = nums[0];
        int result = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int n = nums[i];
            if (n < 0) {
                int temp = curMax;
                curMax = curMin;
                curMin = temp;
            }
            curMax = Math.max(n, curMax * n);
            curMin = Math.min(n, curMin * n);
            result = Math.max(result, curMax);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_max = cur_min = result = nums[0]
        for num in nums[1:]:
            if num < 0:
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(num, cur_max * num)
            cur_min = min(num, cur_min * num)
            result = max(result, cur_max)
        return result
```

## Python3

```python
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_prod = min_prod = result = nums[0]
        for num in nums[1:]:
            if num < 0:
                max_prod, min_prod = min_prod, max_prod
            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)
            result = max(result, max_prod)
        return result
```

## C

```c
int maxProduct(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    int maxProd = nums[0];
    int minProd = nums[0];
    int result = nums[0];
    for (int i = 1; i < numsSize; ++i) {
        int cur = nums[i];
        if (cur < 0) {
            int temp = maxProd;
            maxProd = minProd;
            minProd = temp;
        }
        if ((long long)maxProd * cur > cur)
            maxProd = maxProd * cur;
        else
            maxProd = cur;

        if ((long long)minProd * cur < cur)
            minProd = minProd * cur;
        else
            minProd = cur;

        if (maxProd > result) result = maxProd;
    }
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxProduct(int[] nums) {
        int n = nums.Length;
        int curMax = nums[0];
        int curMin = nums[0];
        int result = nums[0];

        for (int i = 1; i < n; i++) {
            int x = nums[i];
            if (x < 0) {
                int temp = curMax;
                curMax = curMin;
                curMin = temp;
            }
            curMax = Math.Max(x, curMax * x);
            curMin = Math.Min(x, curMin * x);
            result = Math.Max(result, curMax);
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    if (nums.length === 0) return 0;
    let maxProd = nums[0];
    let minProd = nums[0];
    let result = nums[0];
    
    for (let i = 1; i < nums.length; i++) {
        const n = nums[i];
        if (n < 0) {
            // swap because multiplying by negative flips max/min
            [maxProd, minProd] = [minProd, maxProd];
        }
        maxProd = Math.max(n, maxProd * n);
        minProd = Math.min(n, minProd * n);
        result = Math.max(result, maxProd);
    }
    
    return result;
};
```

## Typescript

```typescript
function maxProduct(nums: number[]): number {
    if (nums.length === 0) return 0;
    let maxProd = nums[0];
    let minProd = nums[0];
    let result = nums[0];

    for (let i = 1; i < nums.length; i++) {
        const n = nums[i];
        if (n < 0) {
            // swap because multiplying by negative flips max/min
            const temp = maxProd;
            maxProd = minProd;
            minProd = temp;
        }
        maxProd = Math.max(n, maxProd * n);
        minProd = Math.min(n, minProd * n);
        result = Math.max(result, maxProd);
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxProduct($nums) {
        $n = count($nums);
        $maxProd = $nums[0];
        $minProd = $nums[0];
        $result = $nums[0];

        for ($i = 1; $i < $n; $i++) {
            $num = $nums[$i];
            if ($num < 0) {
                // swap max and min when multiplied by a negative number
                $temp = $maxProd;
                $maxProd = $minProd;
                $minProd = $temp;
            }

            $maxProd = max($num, $maxProd * $num);
            $minProd = min($num, $minProd * $num);

            if ($maxProd > $result) {
                $result = $maxProd;
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func maxProduct(_ nums: [Int]) -> Int {
        guard let first = nums.first else { return 0 }
        var maxSoFar = first
        var minSoFar = first
        var result = first
        
        for num in nums.dropFirst() {
            if num < 0 {
                swap(&maxSoFar, &minSoFar)
            }
            maxSoFar = max(num, maxSoFar * num)
            minSoFar = min(num, minSoFar * num)
            result = max(result, maxSoFar)
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxProduct(nums: IntArray): Int {
        var maxSoFar = nums[0]
        var minSoFar = nums[0]
        var result = nums[0]
        for (i in 1 until nums.size) {
            val n = nums[i]
            if (n < 0) {
                val temp = maxSoFar
                maxSoFar = minSoFar
                minSoFar = temp
            }
            maxSoFar = kotlin.math.max(n, maxSoFar * n)
            minSoFar = kotlin.math.min(n, minSoFar * n)
            result = kotlin.math.max(result, maxSoFar)
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  int maxProduct(List<int> nums) {
    int maxSoFar = nums[0];
    int minSoFar = nums[0];
    int result = nums[0];

    for (int i = 1; i < nums.length; ++i) {
      int cur = nums[i];
      if (cur < 0) {
        int temp = maxSoFar;
        maxSoFar = minSoFar;
        minSoFar = temp;
      }
      maxSoFar = cur > maxSoFar * cur ? cur : maxSoFar * cur;
      minSoFar = cur < minSoFar * cur ? cur : minSoFar * cur;
      if (maxSoFar > result) {
        result = maxSoFar;
      }
    }

    return result;
  }
}
```

## Golang

```go
func maxProduct(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	maxProd, minProd := nums[0], nums[0]
	result := nums[0]

	for i := 1; i < len(nums); i++ {
		n := nums[i]
		if n < 0 {
			maxProd, minProd = minProd, maxProd
		}
		if n > maxProd*n {
			maxProd = n
		} else {
			maxProd = maxProd * n
		}
		if n < minProd*n {
			minProd = n
		} else {
			minProd = minProd * n
		}
		if maxProd > result {
			result = maxProd
		}
	}
	return result
}
```

## Ruby

```ruby
def max_product(nums)
  return 0 if nums.empty?
  max_prod = min_prod = result = nums[0]
  nums[1..-1].each do |num|
    if num < 0
      max_prod, min_prod = min_prod, max_prod
    end
    max_prod = [num, max_prod * num].max
    min_prod = [num, min_prod * num].min
    result = [result, max_prod].max
  end
  result
end
```

## Scala

```scala
object Solution {
    def maxProduct(nums: Array[Int]): Int = {
        var maxOverall = nums(0)
        var curMax = nums(0)
        var curMin = nums(0)

        for (i <- 1 until nums.length) {
            val n = nums(i)
            if (n < 0) {
                val tmp = curMax
                curMax = curMin
                curMin = tmp
            }
            curMax = math.max(n, curMax * n)
            curMin = math.min(n, curMin * n)

            maxOverall = math.max(maxOverall, curMax)
        }

        maxOverall
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_product(nums: Vec<i32>) -> i32 {
        let mut max_prod = nums[0] as i64;
        let mut min_prod = nums[0] as i64;
        let mut ans = nums[0] as i64;
        for &num in nums.iter().skip(1) {
            let n = num as i64;
            if n < 0 {
                std::mem::swap(&mut max_prod, &mut min_prod);
            }
            max_prod = std::cmp::max(n, max_prod * n);
            min_prod = std::cmp::min(n, min_prod * n);
            ans = std::cmp::max(ans, max_prod);
        }
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (max-product nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((first (car nums))
         (init-max first)
         (init-min first)
         (global first))
    (let-values ([(final-max final-min ans)
                  (for/fold ([cur-max init-max] [cur-min init-min] [ans global])
                            ([x (in-list (cdr nums))])
                    (define candidates (list x (* cur-max x) (* cur-min x)))
                    (define new-max (apply max candidates))
                    (define new-min (apply min candidates))
                    (values new-max new-min (max ans new-max)))])
      ans)))
```

## Erlang

```erlang
-spec max_product(Nums :: [integer()]) -> integer().
max_product([H|T]) ->
    loop(T, H, H, H);
max_product([]) ->
    0.

loop([], Result, _, _) ->
    Result;
loop([X|Xs], Result, MaxEnd, MinEnd) ->
    {MaxE, MinE} = if X < 0 -> {MinEnd, MaxEnd}; true -> {MaxEnd, MinEnd} end,
    NewMaxEnd = erlang:max(X, MaxE * X),
    NewMinEnd = erlang:min(X, MinE * X),
    NewResult = erlang:max(Result, NewMaxEnd),
    loop(Xs, NewResult, NewMaxEnd, NewMinEnd).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_product(nums :: [integer]) :: integer
  def max_product([head | tail]) do
    {global_max, _, _} =
      Enum.reduce(tail, {head, head, head}, fn x, {gmax, cmax, cmin} ->
        new_cmax = max(x, max(cmax * x, cmin * x))
        new_cmin = min(x, min(cmax * x, cmin * x))
        new_gmax = max(gmax, new_cmax)
        {new_gmax, new_cmax, new_cmin}
      end)

    global_max
  end
end
```
