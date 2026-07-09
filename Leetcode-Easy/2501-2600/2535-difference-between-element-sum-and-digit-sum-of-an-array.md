# 2535. Difference Between Element Sum and Digit Sum of an Array

## Cpp

```cpp
class Solution {
public:
    int differenceOfSum(vector<int>& nums) {
        long long elementSum = 0;
        long long digitSum = 0;
        for (int num : nums) {
            elementSum += num;
            int x = num;
            while (x > 0) {
                digitSum += x % 10;
                x /= 10;
            }
        }
        return std::abs(elementSum - digitSum);
    }
};
```

## Java

```java
class Solution {
    public int differenceOfSum(int[] nums) {
        int elementSum = 0;
        int digitSum = 0;
        for (int num : nums) {
            elementSum += num;
            int n = num;
            while (n > 0) {
                digitSum += n % 10;
                n /= 10;
            }
        }
        return Math.abs(elementSum - digitSum);
    }
}
```

## Python

```python
class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        element_sum = sum(nums)
        digit_sum = 0
        for num in nums:
            while num:
                digit_sum += num % 10
                num //= 10
        return abs(element_sum - digit_sum)
```

## Python3

```python
from typing import List

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = 0
        digit_sum = 0
        for num in nums:
            element_sum += num
            while num:
                digit_sum += num % 10
                num //= 10
        return abs(element_sum - digit_sum)
```

## C

```c
#include <stdlib.h>

int differenceOfSum(int* nums, int numsSize) {
    long long elementSum = 0;
    long long digitSum = 0;
    for (int i = 0; i < numsSize; ++i) {
        int val = nums[i];
        elementSum += val;
        while (val > 0) {
            digitSum += val % 10;
            val /= 10;
        }
    }
    long long diff = elementSum - digitSum;
    if (diff < 0) diff = -diff;
    return (int)diff;
}
```

## Csharp

```csharp
public class Solution {
    public int DifferenceOfSum(int[] nums) {
        int elementSum = 0;
        int digitSum = 0;
        foreach (int num in nums) {
            elementSum += num;
            int n = num;
            while (n > 0) {
                digitSum += n % 10;
                n /= 10;
            }
        }
        return Math.Abs(elementSum - digitSum);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var differenceOfSum = function(nums) {
    let elementSum = 0;
    let digitSum = 0;
    for (let num of nums) {
        elementSum += num;
        while (num > 0) {
            digitSum += num % 10;
            num = Math.floor(num / 10);
        }
    }
    return Math.abs(elementSum - digitSum);
};
```

## Typescript

```typescript
function differenceOfSum(nums: number[]): number {
    let elementSum = 0;
    let digitSum = 0;
    for (const num of nums) {
        elementSum += num;
        let x = num;
        while (x > 0) {
            digitSum += x % 10;
            x = Math.floor(x / 10);
        }
    }
    return Math.abs(elementSum - digitSum);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function differenceOfSum($nums) {
        $elementSum = 0;
        $digitSum = 0;
        foreach ($nums as $num) {
            $elementSum += $num;
            $temp = $num;
            while ($temp > 0) {
                $digitSum += $temp % 10;
                $temp = intdiv($temp, 10);
            }
        }
        return abs($elementSum - $digitSum);
    }
}
```

## Swift

```swift
class Solution {
    func differenceOfSum(_ nums: [Int]) -> Int {
        var elementSum = 0
        var digitSum = 0
        
        for num in nums {
            elementSum += num
            var n = num
            while n > 0 {
                digitSum += n % 10
                n /= 10
            }
        }
        
        return abs(elementSum - digitSum)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun differenceOfSum(nums: IntArray): Int {
        var elementSum = 0
        var digitSum = 0
        for (num in nums) {
            elementSum += num
            var x = num
            while (x > 0) {
                digitSum += x % 10
                x /= 10
            }
        }
        return kotlin.math.abs(elementSum - digitSum)
    }
}
```

## Dart

```dart
class Solution {
  int differenceOfSum(List<int> nums) {
    int elementSum = 0;
    int digitSum = 0;
    for (int num in nums) {
      elementSum += num;
      int x = num;
      while (x > 0) {
        digitSum += x % 10;
        x ~/= 10;
      }
    }
    return (elementSum - digitSum).abs();
  }
}
```

## Golang

```go
func differenceOfSum(nums []int) int {
    elementSum, digitSum := 0, 0
    for _, v := range nums {
        elementSum += v
        n := v
        for n > 0 {
            digitSum += n % 10
            n /= 10
        }
    }
    diff := elementSum - digitSum
    if diff < 0 {
        diff = -diff
    }
    return diff
}
```

## Ruby

```ruby
def difference_of_sum(nums)
  element_sum = nums.sum
  digit_sum = 0
  nums.each do |num|
    while num > 0
      digit_sum += num % 10
      num /= 10
    end
  end
  (element_sum - digit_sum).abs
end
```

## Scala

```scala
object Solution {
    def differenceOfSum(nums: Array[Int]): Int = {
        var elementSum = 0
        var digitSum = 0
        for (num <- nums) {
            elementSum += num
            var n = num
            while (n > 0) {
                digitSum += n % 10
                n /= 10
            }
        }
        math.abs(elementSum - digitSum)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn difference_of_sum(nums: Vec<i32>) -> i32 {
        let mut element_sum = 0i32;
        let mut digit_sum = 0i32;
        for &num in nums.iter() {
            element_sum += num;
            let mut x = num;
            while x > 0 {
                digit_sum += x % 10;
                x /= 10;
            }
        }
        (element_sum - digit_sum).abs()
    }
}
```

## Racket

```racket
(define/contract (difference-of-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((lst nums) (elem-sum 0) (digit-sum 0))
    (if (null? lst)
        (abs (- elem-sum digit-sum))
        (let* ((x (car lst))
               (new-elem (+ elem-sum x))
               (sum-digits
                (let rec ((n x) (s 0))
                  (if (= n 0)
                      s
                      (rec (quotient n 10) (+ s (modulo n 10))))))
               (new-digit (+ digit-sum sum-digits)))
          (loop (cdr lst) new-elem new-digit)))))
```

## Erlang

```erlang
-spec sum_digits(integer()) -> integer().
sum_digits(0) -> 0;
sum_digits(N) -> (N rem 10) + sum_digits(N div 10).

-spec difference_of_sum(Nums :: [integer()]) -> integer().
difference_of_sum(Nums) ->
    ElementSum = lists:sum(Nums),
    DigitSum = lists:foldl(fun(N, Acc) -> Acc + sum_digits(N) end, 0, Nums),
    erlang:abs(ElementSum - DigitSum).
```

## Elixir

```elixir
defmodule Solution do
  @spec difference_of_sum(nums :: [integer]) :: integer
  def difference_of_sum(nums) do
    element_sum = Enum.sum(nums)

    digit_sum =
      nums
      |> Enum.flat_map(&Integer.digits/1)
      |> Enum.sum()

    Kernel.abs(element_sum - digit_sum)
  end
end
```
