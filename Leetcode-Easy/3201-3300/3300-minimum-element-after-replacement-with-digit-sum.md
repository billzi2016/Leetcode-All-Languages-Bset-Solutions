# 3300. Minimum Element After Replacement With Digit Sum

## Cpp

```cpp
class Solution {
public:
    int minElement(vector<int>& nums) {
        auto digitSum = [](int x) {
            int sum = 0;
            while (x > 0) {
                sum += x % 10;
                x /= 10;
            }
            return sum;
        };
        int ans = INT_MAX;
        for (int &num : nums) {
            int replaced = digitSum(num);
            if (replaced < ans) ans = replaced;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minElement(int[] nums) {
        int min = Integer.MAX_VALUE;
        for (int num : nums) {
            int sum = digitSum(num);
            if (sum < min) {
                min = sum;
            }
        }
        return min;
    }

    private int digitSum(int n) {
        int s = 0;
        while (n > 0) {
            s += n % 10;
            n /= 10;
        }
        return s;
    }
}
```

## Python

```python
class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def digit_sum(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        return min(digit_sum(num) for num in nums)
```

## Python3

```python
from typing import List

class Solution:
    def minElement(self, nums: List[int]) -> int:
        def digit_sum(x: int) -> int:
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s
        
        return min(digit_sum(num) for num in nums)
```

## C

```c
int minElement(int* nums, int numsSize) {
    int minVal = 2147483647;
    for (int i = 0; i < numsSize; ++i) {
        int n = nums[i];
        int sum = 0;
        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }
        if (sum < minVal) {
            minVal = sum;
        }
    }
    return minVal;
}
```

## Csharp

```csharp
public class Solution {
    public int MinElement(int[] nums) {
        int min = int.MaxValue;
        foreach (int num in nums) {
            int sum = 0, x = num;
            while (x > 0) {
                sum += x % 10;
                x /= 10;
            }
            if (sum < min) min = sum;
        }
        return min;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minElement = function(nums) {
    const digitSum = (n) => {
        let sum = 0;
        while (n > 0) {
            sum += n % 10;
            n = Math.floor(n / 10);
        }
        return sum;
    };
    
    let minVal = Infinity;
    for (let i = 0; i < nums.length; i++) {
        const s = digitSum(nums[i]);
        if (s < minVal) minVal = s;
    }
    return minVal;
};
```

## Typescript

```typescript
function minElement(nums: number[]): number {
    let minVal = Infinity;
    for (const num of nums) {
        let n = num;
        let sum = 0;
        while (n > 0) {
            sum += n % 10;
            n = Math.floor(n / 10);
        }
        if (sum < minVal) minVal = sum;
    }
    return minVal;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minElement($nums) {
        $min = PHP_INT_MAX;
        foreach ($nums as $num) {
            $sum = 0;
            while ($num > 0) {
                $sum += $num % 10;
                $num = intdiv($num, 10);
            }
            if ($sum < $min) {
                $min = $sum;
            }
        }
        return $min;
    }
}
```

## Swift

```swift
class Solution {
    func minElement(_ nums: [Int]) -> Int {
        var minValue = Int.max
        for num in nums {
            var n = num
            var sum = 0
            while n > 0 {
                sum += n % 10
                n /= 10
            }
            if sum < minValue {
                minValue = sum
            }
        }
        return minValue
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minElement(nums: IntArray): Int {
        var minVal = Int.MAX_VALUE
        for (num in nums) {
            var x = num
            var sum = 0
            while (x > 0) {
                sum += x % 10
                x /= 10
            }
            if (sum < minVal) minVal = sum
        }
        return minVal
    }
}
```

## Dart

```dart
class Solution {
  int minElement(List<int> nums) {
    int minVal = 1 << 30;
    for (int num in nums) {
      int sum = 0;
      int x = num;
      while (x > 0) {
        sum += x % 10;
        x ~/= 10;
      }
      if (sum < minVal) minVal = sum;
    }
    return minVal;
  }
}
```

## Golang

```go
func minElement(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	digitSum := func(n int) int {
		sum := 0
		for n > 0 {
			sum += n % 10
			n /= 10
		}
		return sum
	}
	minVal := digitSum(nums[0])
	for i := 1; i < len(nums); i++ {
		if s := digitSum(nums[i]); s < minVal {
			minVal = s
		}
	}
	return minVal
}
```

## Ruby

```ruby
def min_element(nums)
  nums.map { |num| num.to_s.each_char.sum { |ch| ch.ord - 48 } }.min
end
```

## Scala

```scala
object Solution {
    def minElement(nums: Array[Int]): Int = {
        var minVal = Int.MaxValue
        for (num <- nums) {
            var x = num
            var sum = 0
            while (x > 0) {
                sum += x % 10
                x /= 10
            }
            if (sum < minVal) minVal = sum
        }
        minVal
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_element(nums: Vec<i32>) -> i32 {
        let mut min_val = i32::MAX;
        for num in nums {
            let mut x = num;
            let mut sum = 0;
            while x > 0 {
                sum += x % 10;
                x /= 10;
            }
            if sum < min_val {
                min_val = sum;
            }
        }
        min_val
    }
}
```

## Racket

```racket
#lang racket

(define (digit-sum n)
  (let loop ((x n) (sum 0))
    (if (= x 0)
        sum
        (loop (quotient x 10) (+ sum (remainder x 10))))))

(define/contract (min-element nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ((sums (map digit-sum nums)))
    (apply min sums)))
```

## Erlang

```erlang
-spec min_element(Nums :: [integer()]) -> integer().
min_element(Nums) ->
    Sums = [digit_sum(N) || N <- Nums],
    lists:min(Sums).

digit_sum(0) -> 0;
digit_sum(N) when N < 10 -> N;
digit_sum(N) ->
    (N rem 10) + digit_sum(N div 10).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_element(nums :: [integer]) :: integer
  def min_element(nums) do
    nums
    |> Enum.map(&digit_sum/1)
    |> Enum.min()
  end

  defp digit_sum(n) when n >= 0 do
    Integer.digits(n) |> Enum.sum()
  end
end
```
