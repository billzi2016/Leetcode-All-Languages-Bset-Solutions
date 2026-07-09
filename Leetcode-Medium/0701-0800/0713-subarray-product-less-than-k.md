# 0713. Subarray Product Less Than K

## Cpp

```cpp
class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        if (k <= 1) return 0;
        long long prod = 1;
        int left = 0;
        int count = 0;
        for (int right = 0; right < (int)nums.size(); ++right) {
            prod *= nums[right];
            while (left <= right && prod >= k) {
                prod /= nums[left];
                ++left;
            }
            count += right - left + 1;
        }
        return count;
    }
};
```

## Java

```java
class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        if (k <= 1) return 0;
        long product = 1;
        int left = 0;
        int count = 0;
        for (int right = 0; right < nums.length; right++) {
            product *= nums[right];
            while (product >= k && left <= right) {
                product /= nums[left++];
            }
            count += right - left + 1;
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0
        prod = 1
        left = 0
        count = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k and left <= right:
                prod //= nums[left]
                left += 1
            count += right - left + 1
        return count
```

## Python3

```python
from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        prod = 1
        left = 0
        count = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod //= nums[left]
                left += 1
            count += right - left + 1
        return count
```

## C

```c
int numSubarrayProductLessThanK(int* nums, int numsSize, int k) {
    if (k <= 1) return 0;
    long long prod = 1;
    int left = 0;
    long long result = 0;
    for (int right = 0; right < numsSize; ++right) {
        prod *= nums[right];
        while (prod >= k && left <= right) {
            prod /= nums[left];
            ++left;
        }
        result += right - left + 1;
    }
    return (int)result;
}
```

## Csharp

```csharp
public class Solution
{
    public int NumSubarrayProductLessThanK(int[] nums, int k)
    {
        if (k <= 1) return 0;

        long product = 1;
        int left = 0;
        int count = 0;

        for (int right = 0; right < nums.Length; right++)
        {
            product *= nums[right];

            while (product >= k && left <= right)
            {
                product /= nums[left];
                left++;
            }

            count += right - left + 1;
        }

        return count;
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
var numSubarrayProductLessThanK = function(nums, k) {
    if (k <= 1) return 0;
    let prod = 1;
    let left = 0;
    let count = 0;
    for (let right = 0; right < nums.length; ++right) {
        prod *= nums[right];
        while (prod >= k && left <= right) {
            prod /= nums[left];
            left++;
        }
        count += right - left + 1;
    }
    return count;
};
```

## Typescript

```typescript
function numSubarrayProductLessThanK(nums: number[], k: number): number {
    if (k <= 1) return 0;
    let prod = 1;
    let left = 0;
    let count = 0;
    for (let right = 0; right < nums.length; right++) {
        prod *= nums[right];
        while (prod >= k && left <= right) {
            prod /= nums[left];
            left++;
        }
        count += right - left + 1;
    }
    return count;
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
    function numSubarrayProductLessThanK($nums, $k) {
        if ($k <= 1) {
            return 0;
        }
        $prod = 1.0;
        $left = 0;
        $count = 0;
        $n = count($nums);
        for ($right = 0; $right < $n; $right++) {
            $prod *= $nums[$right];
            while ($prod >= $k && $left <= $right) {
                $prod /= $nums[$left];
                $left++;
            }
            $count += $right - $left + 1;
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func numSubarrayProductLessThanK(_ nums: [Int], _ k: Int) -> Int {
        if k <= 1 { return 0 }
        var product: Double = 1.0
        var left = 0
        var result = 0
        let target = Double(k)
        for right in 0..<nums.count {
            product *= Double(nums[right])
            while product >= target && left <= right {
                product /= Double(nums[left])
                left += 1
            }
            result += right - left + 1
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numSubarrayProductLessThanK(nums: IntArray, k: Int): Int {
        if (k <= 1) return 0
        var product = 1L
        var left = 0
        var count = 0L
        for (right in nums.indices) {
            product *= nums[right].toLong()
            while (product >= k && left <= right) {
                product /= nums[left].toLong()
                left++
            }
            count += (right - left + 1)
        }
        return count.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int numSubarrayProductLessThanK(List<int> nums, int k) {
    if (k <= 1) return 0;
    double product = 1.0;
    int left = 0;
    int count = 0;
    for (int right = 0; right < nums.length; right++) {
      product *= nums[right];
      while (left <= right && product >= k) {
        product /= nums[left];
        left++;
      }
      count += right - left + 1;
    }
    return count;
  }
}
```

## Golang

```go
func numSubarrayProductLessThanK(nums []int, k int) int {
	if k <= 1 {
		return 0
	}
	prod := int64(1)
	kk := int64(k)
	left := 0
	count := 0
	for right, v := range nums {
		prod *= int64(v)
		for prod >= kk && left <= right {
			prod /= int64(nums[left])
			left++
		}
		count += right - left + 1
	}
	return count
}
```

## Ruby

```ruby
def num_subarray_product_less_than_k(nums, k)
  return 0 if k <= 1
  prod = 1
  left = 0
  count = 0
  nums.each_with_index do |num, right|
    prod *= num
    while prod >= k && left <= right
      prod /= nums[left]
      left += 1
    end
    count += right - left + 1
  end
  count
end
```

## Scala

```scala
object Solution {
    def numSubarrayProductLessThanK(nums: Array[Int], k: Int): Int = {
        if (k <= 1) return 0
        var prod: Long = 1L
        var left = 0
        var count: Long = 0L
        for (right <- nums.indices) {
            prod *= nums(right).toLong
            while (left <= right && prod >= k) {
                prod /= nums(left).toLong
                left += 1
            }
            count += (right - left + 1)
        }
        count.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_subarray_product_less_than_k(nums: Vec<i32>, k: i32) -> i32 {
        if k <= 1 {
            return 0;
        }
        let mut prod: i64 = 1;
        let mut left: usize = 0;
        let mut count: i64 = 0;
        let k_i64 = k as i64;

        for right in 0..nums.len() {
            prod *= nums[right] as i64;
            while prod >= k_i64 && left <= right {
                prod /= nums[left] as i64;
                left += 1;
            }
            count += (right - left + 1) as i64;
        }

        count as i32
    }
}
```

## Racket

```racket
(define/contract (num-subarray-product-less-than-k nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (if (<= k 1)
      0
      (let* ((vec (list->vector nums))
             (n   (vector-length vec)))
        (let loop ((right 0) (left 0) (prod 1) (cnt 0))
          (if (= right n)
              cnt
              (let* ((new-prod (* prod (vector-ref vec right))))
                (define-values (shrink-left shrink-prod)
                  (let shrink ((l left) (p new-prod))
                    (if (and (>= p k) (< l (+ right 1)))
                        (shrink (+ l 1) (/ p (vector-ref vec l)))
                        (values l p))))
                (let ((add (- (+ right 1) shrink-left))) ; right - left + 1
                  (loop (+ right 1) shrink-left shrink-prod (+ cnt add)))))))))
```

## Erlang

```erlang
-spec num_subarray_product_less_than_k(Nums :: [integer()], K :: integer()) -> integer().
num_subarray_product_less_than_k(_Nums, K) when K =< 1 ->
    0;
num_subarray_product_less_than_k(Nums, K) ->
    N = length(Nums),
    Tuple = list_to_tuple(Nums),
    loop(Tuple, N, K, 1, 1, 1, 0).

%% loop over right pointer
-spec loop(tuple(), integer(), integer(), integer(), integer(), integer(), integer()) -> integer().
loop(_Tuple, N, _K, _Left, Right, _Prod, Count) when Right > N ->
    Count;
loop(Tuple, N, K, Left, Right, Prod, Count) ->
    Elem = element(Right, Tuple),
    NewProd = Prod * Elem,
    {NewLeft, ShrunkProd} = shrink(NewProd, Left, Right, K, Tuple),
    NewCount = Count + (Right - NewLeft + 1),
    loop(Tuple, N, K, NewLeft, Right + 1, ShrunkProd, NewCount).

%% shrink window until product < K
-spec shrink(integer(), integer(), integer(), integer(), tuple()) -> {integer(), integer()}.
shrink(Prod, Left, _Right, K, _Tuple) when Prod < K ->
    {Left, Prod};
shrink(Prod, Left, Right, K, Tuple) ->
    ElemL = element(Left, Tuple),
    shrink(Prod div ElemL, Left + 1, Right, K, Tuple).
```

## Elixir

```elixir
defmodule Solution do
  @spec num_subarray_product_less_than_k(nums :: [integer], k :: integer) :: integer
  def num_subarray_product_less_than_k(_nums, k) when k <= 1, do: 0

  def num_subarray_product_less_than_k(nums, k) do
    arr = List.to_tuple(nums)
    len = tuple_size(arr)

    {_, _, total} =
      0..(len - 1)
      |> Enum.reduce({0, 1, 0}, fn right, {left, prod, total} ->
        new_prod = prod * elem(arr, right)

        {new_left, final_prod} = shrink_window(new_prod, left, arr, k)

        new_total = total + (right - new_left + 1)
        {new_left, final_prod, new_total}
      end)

    total
  end

  defp shrink_window(prod, left, _arr, k) when prod < k do
    {left, prod}
  end

  defp shrink_window(prod, left, arr, k) do
    new_prod = div(prod, elem(arr, left))
    shrink_window(new_prod, left + 1, arr, k)
  end
end
```
