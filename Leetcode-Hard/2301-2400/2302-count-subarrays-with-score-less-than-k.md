# 2302. Count Subarrays With Score Less Than K

## Cpp

```cpp
class Solution {
public:
    long long countSubarrays(std::vector<int>& nums, long long k) {
        long long total = 0;
        long long result = 0;
        int left = 0;
        for (int right = 0; right < (int)nums.size(); ++right) {
            total += nums[right];
            while (left <= right && total * (long long)(right - left + 1) >= k) {
                total -= nums[left];
                ++left;
            }
            result += (right - left + 1);
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public long countSubarrays(int[] nums, long k) {
        long res = 0;
        long sum = 0;
        int left = 0;
        for (int right = 0; right < nums.length; ++right) {
            sum += nums[right];
            while (left <= right && sum * (right - left + 1L) >= k) {
                sum -= nums[left];
                left++;
            }
            if (left <= right) {
                res += (right - left + 1);
            }
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        left = 0
        total = 0
        res = 0
        for right in range(n):
            total += nums[right]
            # shrink window while score >= k
            while left <= right and total * (right - left + 1) >= k:
                total -= nums[left]
                left += 1
            # all subarrays ending at right with start >= left are valid
            res += right - left + 1
        return res
```

## Python3

```python
class Solution:
    def countSubarrays(self, nums, k):
        n = len(nums)
        left = 0
        total = 0
        res = 0
        for right in range(n):
            total += nums[right]
            while left <= right and total * (right - left + 1) >= k:
                total -= nums[left]
                left += 1
            res += right - left + 1
        return res
```

## C

```c
long long countSubarrays(int* nums, int numsSize, long long k) {
    long long res = 0;
    long long total = 0;
    int left = 0;
    for (int right = 0; right < numsSize; ++right) {
        total += nums[right];
        while (left <= right && (__int128)total * (right - left + 1) >= k) {
            total -= nums[left];
            ++left;
        }
        res += (long long)(right - left + 1);
    }
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public long CountSubarrays(int[] nums, long k) {
        int n = nums.Length;
        long sum = 0;
        long result = 0;
        int left = 0;
        for (int right = 0; right < n; ++right) {
            sum += nums[right];
            while (left <= right && sum * (right - left + 1) >= k) {
                sum -= nums[left];
                left++;
            }
            result += (right - left + 1);
        }
        return result;
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
var countSubarrays = function(nums, k) {
    let left = 0;
    let sum = 0;
    let result = 0;
    for (let right = 0; right < nums.length; right++) {
        sum += nums[right];
        while (left <= right && sum * (right - left + 1) >= k) {
            sum -= nums[left];
            left++;
        }
        result += (right - left + 1);
    }
    return result;
};
```

## Typescript

```typescript
function countSubarrays(nums: number[], k: number): number {
    let left = 0;
    let sum = 0;
    let result = 0;
    for (let right = 0; right < nums.length; ++right) {
        sum += nums[right];
        while (left <= right && sum * (right - left + 1) >= k) {
            sum -= nums[left];
            left++;
        }
        result += right - left + 1;
    }
    return result;
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
    function countSubarrays($nums, $k) {
        $n = count($nums);
        $left = 0;
        $sum = 0;
        $res = 0;
        for ($right = 0; $right < $n; $right++) {
            $sum += $nums[$right];
            while ($left <= $right && $sum * ($right - $left + 1) >= $k) {
                $sum -= $nums[$left];
                $left++;
            }
            $res += $right - $left + 1;
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func countSubarrays(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var left = 0
        var sum: Int64 = 0
        var result: Int64 = 0
        let K = Int64(k)
        
        for right in 0..<n {
            sum += Int64(nums[right])
            while left <= right && sum * Int64(right - left + 1) >= K {
                sum -= Int64(nums[left])
                left += 1
            }
            result += Int64(right - left + 1)
        }
        
        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countSubarrays(nums: IntArray, k: Long): Long {
        var left = 0
        var sum = 0L
        var result = 0L
        for (right in nums.indices) {
            sum += nums[right].toLong()
            while (left <= right && sum * (right - left + 1) >= k) {
                sum -= nums[left].toLong()
                left++
            }
            result += (right - left + 1).toLong()
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  int countSubarrays(List<int> nums, int k) {
    int n = nums.length;
    int left = 0;
    int res = 0;
    int sum = 0;

    for (int right = 0; right < n; right++) {
      sum += nums[right];
      while (left <= right && sum * (right - left + 1) >= k) {
        sum -= nums[left];
        left++;
      }
      res += (right - left + 1);
    }

    return res;
  }
}
```

## Golang

```go
func countSubarrays(nums []int, k int64) int64 {
	var left int
	var sum int64
	var result int64

	for right, v := range nums {
		sum += int64(v)
		// shrink window while score >= k
		for left <= right && sum*int64(right-left+1) >= k {
			sum -= int64(nums[left])
			left++
		}
		result += int64(right - left + 1)
	}
	return result
}
```

## Ruby

```ruby
def count_subarrays(nums, k)
  left = 0
  sum = 0
  result = 0
  nums.each_with_index do |val, right|
    sum += val
    while left <= right && sum * (right - left + 1) >= k
      sum -= nums[left]
      left += 1
    end
    result += (right - left + 1)
  end
  result
end
```

## Scala

```scala
object Solution {
    def countSubarrays(nums: Array[Int], k: Long): Long = {
        var left = 0
        var sum: Long = 0L
        var result: Long = 0L
        val n = nums.length
        for (right <- 0 until n) {
            sum += nums(right).toLong
            while (left <= right && sum * (right - left + 1) >= k) {
                sum -= nums(left).toLong
                left += 1
            }
            result += (right - left + 1)
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, k: i64) -> i64 {
        let mut left = 0usize;
        let mut sum: i64 = 0;
        let mut res: i64 = 0;
        for right in 0..nums.len() {
            sum += nums[right] as i64;
            while left <= right && sum * ((right - left + 1) as i64) >= k {
                sum -= nums[left] as i64;
                left += 1;
            }
            res += (right - left + 1) as i64;
        }
        res
    }
}
```

## Racket

```racket
(define/contract (count-subarrays nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((v (list->vector nums))
         (n (vector-length v)))
    (let loop ((j 0) (i 0) (sum 0) (res 0))
      (if (= j n)
          res
          (let* ((new-sum (+ sum (vector-ref v j))))
            (letrec ((shrink (lambda (i cur-sum)
                               (if (and (<= i j)
                                        (>= (* cur-sum (- j i + 1)) k))
                                   (shrink (+ i 1) (- cur-sum (vector-ref v i)))
                                   (values i cur-sum)))))
              (let-values ([(i2 sum2) (shrink i new-sum)])
                (loop (+ j 1) i2 sum2 (+ res (+ 1 (- j i2)))))))))))
```

## Erlang

```erlang
-spec count_subarrays(Nums :: [integer()], K :: integer()) -> integer().
count_subarrays(Nums, K) ->
    Tuple = list_to_tuple(Nums),
    N = tuple_size(Tuple),
    loop(0, 0, 0, 0, K, Tuple, N).

loop(J, I, Total, Res, _K, _Tuple, N) when J >= N ->
    Res;
loop(J, I, Total, Res, K, Tuple, N) ->
    NumJ = element(J + 1, Tuple),
    NewTotal = Total + NumJ,
    {NewI, ShrinkedTotal} = shrink(I, NewTotal, J, K, Tuple),
    Count = J - NewI + 1,
    loop(J + 1, NewI, ShrinkedTotal, Res + Count, K, Tuple, N).

shrink(I, Total, J, K, Tuple) when I =< J ->
    Len = J - I + 1,
    case Total * Len >= K of
        true ->
            NumI = element(I + 1, Tuple),
            shrink(I + 1, Total - NumI, J, K, Tuple);
        false ->
            {I, Total}
    end;
shrink(I, Total, _J, _K, _Tuple) ->
    {I, Total}.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_subarrays(nums :: [integer], k :: integer) :: integer
  def count_subarrays(nums, k) do
    tup = List.to_tuple(nums)

    {_, _, res} =
      Enum.with_index(nums)
      |> Enum.reduce({0, 0, 0}, fn {val, j}, {i, total, acc} ->
        total = total + val
        {i, total} = shrink(i, total, j, k, tup)
        acc = acc + (j - i + 1)
        {i, total, acc}
      end)

    res
  end

  defp shrink(i, total, j, k, tup) do
    if i <= j and total * (j - i + 1) >= k do
      shrink(i + 1, total - elem(tup, i), j, k, tup)
    else
      {i, total}
    end
  end
end
```
