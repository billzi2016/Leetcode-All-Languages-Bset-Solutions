# 1283. Find the Smallest Divisor Given a Threshold

## Cpp

```cpp
class Solution {
public:
    int smallestDivisor(vector<int>& nums, int threshold) {
        int left = 1;
        int right = *max_element(nums.begin(), nums.end());
        while (left < right) {
            int mid = left + (right - left) / 2;
            long long sum = 0;
            for (int num : nums) {
                sum += (num + mid - 1) / mid; // ceil division
                if (sum > threshold) break; // early stop
            }
            if (sum <= threshold) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
};
```

## Java

```java
class Solution {
    public int smallestDivisor(int[] nums, int threshold) {
        int left = 1;
        int right = 0;
        for (int num : nums) {
            if (num > right) right = num;
        }
        while (left < right) {
            int mid = left + (right - left) / 2;
            long sum = 0;
            for (int num : nums) {
                sum += (num + mid - 1) / mid; // ceil division
                if (sum > threshold) break;   // early exit
            }
            if (sum <= threshold) {
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
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            total = 0
            for num in nums:
                total += (num + mid - 1) // mid
                if total > threshold:  # early break
                    break
            if total <= threshold:
                right = mid
            else:
                left = mid + 1
        return left
```

## Python3

```python
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            total = sum((num + mid - 1) // mid for num in nums)
            if total <= threshold:
                right = mid
            else:
                left = mid + 1
        return left
```

## C

```c
int smallestDivisor(int* nums, int numsSize, int threshold) {
    int maxVal = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] > maxVal) maxVal = nums[i];
    }
    
    int left = 1, right = maxVal;
    while (left < right) {
        int mid = left + (right - left) / 2;
        long long sum = 0;
        for (int i = 0; i < numsSize; ++i) {
            sum += (nums[i] + mid - 1) / mid; // ceil division
            if (sum > threshold) break; // early exit to avoid unnecessary work
        }
        if (sum <= threshold) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
}
```

## Csharp

```csharp
public class Solution {
    public int SmallestDivisor(int[] nums, int threshold) {
        int left = 1;
        int right = 0;
        foreach (int num in nums) {
            if (num > right) right = num;
        }
        while (left < right) {
            int mid = left + (right - left) / 2;
            long sum = 0;
            foreach (int num in nums) {
                sum += (num + mid - 1) / mid; // ceil division
                if (sum > threshold) break; // early exit
            }
            if (sum <= threshold) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} threshold
 * @return {number}
 */
var smallestDivisor = function(nums, threshold) {
    let left = 1;
    let right = Math.max(...nums);
    
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        let sum = 0;
        for (const num of nums) {
            sum += Math.ceil(num / mid);
            if (sum > threshold) break; // early exit
        }
        if (sum <= threshold) {
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
function smallestDivisor(nums: number[], threshold: number): number {
    let left = 1;
    let right = Math.max(...nums);
    
    const computeSum = (div: number): number => {
        let total = 0;
        for (const num of nums) {
            total += Math.ceil(num / div);
            if (total > threshold) break; // early exit
        }
        return total;
    };
    
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (computeSum(mid) <= threshold) {
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
     * @param Integer $threshold
     * @return Integer
     */
    function smallestDivisor($nums, $threshold) {
        $low = 1;
        $high = max($nums);
        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            $sum = 0;
            foreach ($nums as $num) {
                $sum += intdiv($num + $mid - 1, $mid); // ceil division
                if ($sum > $threshold) {
                    break;
                }
            }
            if ($sum <= $threshold) {
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
    func smallestDivisor(_ nums: [Int], _ threshold: Int) -> Int {
        var left = 1
        var right = nums.max()!
        while left < right {
            let mid = (left + right) / 2
            var sum = 0
            for num in nums {
                sum += (num + mid - 1) / mid
                if sum > threshold { break }
            }
            if sum <= threshold {
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
    fun smallestDivisor(nums: IntArray, threshold: Int): Int {
        var left = 1
        var right = nums.maxOrNull() ?: 1
        while (left < right) {
            val mid = left + (right - left) / 2
            var sum = 0L
            for (num in nums) {
                sum += ((num + mid - 1) / mid)
                if (sum > threshold) break
            }
            if (sum <= threshold) {
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
  int smallestDivisor(List<int> nums, int threshold) {
    int left = 1;
    int right = nums.reduce((a, b) => a > b ? a : b);
    while (left < right) {
      int mid = left + ((right - left) >> 1);
      int sum = 0;
      for (int num in nums) {
        sum += (num + mid - 1) ~/ mid; // ceil division
        if (sum > threshold) break;
      }
      if (sum <= threshold) {
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
func smallestDivisor(nums []int, threshold int) int {
    // Find maximum value in nums to set upper bound
    maxVal := 0
    for _, v := range nums {
        if v > maxVal {
            maxVal = v
        }
    }

    // Helper to check if a divisor satisfies the condition
    feasible := func(d int) bool {
        var sum int64 = 0
        limit := int64(threshold)
        for _, v := range nums {
            // ceil(v/d) = (v + d - 1) / d
            sum += int64((v + d - 1) / d)
            if sum > limit { // early exit
                return false
            }
        }
        return true
    }

    lo, hi := 1, maxVal
    for lo < hi {
        mid := (lo + hi) / 2
        if feasible(mid) {
            hi = mid
        } else {
            lo = mid + 1
        }
    }
    return lo
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} threshold
# @return {Integer}
def smallest_divisor(nums, threshold)
  left = 1
  right = nums.max

  while left < right
    mid = (left + right) / 2
    sum = 0
    nums.each do |num|
      sum += (num + mid - 1) / mid
      break if sum > threshold
    end

    if sum <= threshold
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
    def smallestDivisor(nums: Array[Int], threshold: Int): Int = {
        var left = 1
        var right = nums.max
        while (left < right) {
            val mid = left + (right - left) / 2
            var sum: Long = 0L
            var i = 0
            val n = nums.length
            while (i < n && sum <= threshold) {
                sum += ((nums(i) + mid - 1) / mid)
                i += 1
            }
            if (sum <= threshold) right = mid else left = mid + 1
        }
        left
    }
}
```

## Rust

```rust
impl Solution {
    pub fn smallest_divisor(nums: Vec<i32>, threshold: i32) -> i32 {
        let mut left = 1i32;
        let mut right = *nums.iter().max().unwrap();
        while left < right {
            let mid = left + (right - left) / 2;
            let mut sum: i64 = 0;
            for &num in nums.iter() {
                sum += ((num as i64) + (mid as i64) - 1) / (mid as i64);
                if sum > threshold as i64 {
                    break;
                }
            }
            if sum <= threshold as i64 {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        left
    }
}
```

## Racket

```racket
(define (valid-divisor? d nums thr)
  (let loop ((lst nums) (acc 0))
    (cond
      [(null? lst) #t]
      [else
       (let* ([n (car lst)]
              [add (quotient (+ n (- d 1)) d)]
              [new-acc (+ acc add)])
         (if (> new-acc thr)
             #f
             (loop (cdr lst) new-acc)))])))

(define/contract (smallest-divisor nums threshold)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([max-num (apply max nums)])
    (let search ((low 1) (high max-num))
      (if (= low high)
          low
          (let* ([mid (quotient (+ low high) 2)]
                 [ok (valid-divisor? mid nums threshold)])
            (if ok
                (search low mid)
                (search (+ mid 1) high)))))))
```

## Erlang

```erlang
-spec smallest_divisor(Nums :: [integer()], Threshold :: integer()) -> integer().
smallest_divisor(Nums, Threshold) ->
    Max = lists:max(Nums),
    bs(1, Max, Nums, Threshold).

bs(Low, High, _Nums, _Threshold) when Low >= High ->
    Low;
bs(Low, High, Nums, Threshold) ->
    Mid = (Low + High) div 2,
    Sum = sum_div(Nums, Mid, Threshold),
    if
        Sum =< Threshold -> bs(Low, Mid, Nums, Threshold);
        true -> bs(Mid + 1, High, Nums, Threshold)
    end.

sum_div(Nums, D, Threshold) ->
    sum_div(Nums, D, 0, Threshold).

sum_div([], _D, Acc, _Threshold) ->
    Acc;
sum_div([H|T], D, Acc, Threshold) ->
    NewAcc = Acc + ((H + D - 1) div D),
    if
        NewAcc > Threshold -> NewAcc;
        true -> sum_div(T, D, NewAcc, Threshold)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec smallest_divisor(nums :: [integer], threshold :: integer) :: integer
  def smallest_divisor(nums, threshold) do
    max_num = Enum.max(nums)
    binary_search(nums, threshold, 1, max_num)
  end

  defp binary_search(_nums, _threshold, low, high) when low >= high, do: low

  defp binary_search(nums, threshold, low, high) do
    mid = div(low + high, 2)

    sum =
      Enum.reduce(nums, 0, fn x, acc ->
        acc + div(x + mid - 1, mid)
      end)

    if sum <= threshold do
      binary_search(nums, threshold, low, mid)
    else
      binary_search(nums, threshold, mid + 1, high)
    end
  end
end
```
