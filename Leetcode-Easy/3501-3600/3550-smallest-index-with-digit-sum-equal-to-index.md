# 3550. Smallest Index With Digit Sum Equal to Index

## Cpp

```cpp
class Solution {
public:
    int smallestIndex(vector<int>& nums) {
        for (int i = 0; i < (int)nums.size(); ++i) {
            int x = nums[i];
            int sum = 0;
            if (x == 0) sum = 0;
            while (x > 0) {
                sum += x % 10;
                x /= 10;
            }
            if (sum == i) return i;
        }
        return -1;
    }
};
```

## Java

```java
class Solution {
    public int smallestIndex(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            if (digitSum(nums[i]) == i) {
                return i;
            }
        }
        return -1;
    }

    private int digitSum(int num) {
        int sum = 0;
        do {
            sum += num % 10;
            num /= 10;
        } while (num > 0);
        return sum;
    }
}
```

## Python

```python
class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, val in enumerate(nums):
            s = 0
            n = val
            if n == 0:
                s = 0
            else:
                while n:
                    s += n % 10
                    n //= 10
            if s == i:
                return i
        return -1
```

## Python3

```python
from typing import List

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, val in enumerate(nums):
            s = 0
            x = val
            if x == 0:
                s = 0
            else:
                while x:
                    s += x % 10
                    x //= 10
            if s == i:
                return i
        return -1
```

## C

```c
int digitSum(int x) {
    int sum = 0;
    do {
        sum += x % 10;
        x /= 10;
    } while (x > 0);
    return sum;
}

int smallestIndex(int* nums, int numsSize) {
    for (int i = 0; i < numsSize; ++i) {
        if (digitSum(nums[i]) == i)
            return i;
    }
    return -1;
}
```

## Csharp

```csharp
public class Solution {
    public int SmallestIndex(int[] nums) {
        for (int i = 0; i < nums.Length; i++) {
            int sum = DigitSum(nums[i]);
            if (sum == i) return i;
        }
        return -1;
    }

    private int DigitSum(int num) {
        int sum = 0;
        do {
            sum += num % 10;
            num /= 10;
        } while (num > 0);
        return sum;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var smallestIndex = function(nums) {
    const digitSum = (num) => {
        if (num === 0) return 0;
        let sum = 0;
        while (num > 0) {
            sum += num % 10;
            num = Math.floor(num / 10);
        }
        return sum;
    };
    
    for (let i = 0; i < nums.length; i++) {
        if (digitSum(nums[i]) === i) {
            return i;
        }
    }
    return -1;
};
```

## Typescript

```typescript
function smallestIndex(nums: number[]): number {
    const digitSum = (n: number): number => {
        let sum = 0;
        if (n === 0) return 0;
        while (n > 0) {
            sum += n % 10;
            n = Math.floor(n / 10);
        }
        return sum;
    };
    
    for (let i = 0; i < nums.length; i++) {
        if (digitSum(nums[i]) === i) {
            return i;
        }
    }
    return -1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function smallestIndex($nums) {
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if ($this->digitSum($nums[$i]) === $i) {
                return $i;
            }
        }
        return -1;
    }

    private function digitSum($num) {
        $sum = 0;
        // handle zero explicitly
        if ($num == 0) {
            return 0;
        }
        while ($num > 0) {
            $sum += $num % 10;
            $num = intdiv($num, 10);
        }
        return $sum;
    }
}
```

## Swift

```swift
class Solution {
    func smallestIndex(_ nums: [Int]) -> Int {
        for (i, num) in nums.enumerated() {
            var n = num
            var sum = 0
            while n > 0 {
                sum += n % 10
                n /= 10
            }
            if sum == i {
                return i
            }
        }
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun smallestIndex(nums: IntArray): Int {
        for (i in nums.indices) {
            var x = nums[i]
            var sum = 0
            while (x > 0) {
                sum += x % 10
                x /= 10
            }
            if (sum == i) return i
        }
        return -1
    }
}
```

## Dart

```dart
class Solution {
  int smallestIndex(List<int> nums) {
    for (int i = 0; i < nums.length; i++) {
      int sum = 0;
      int x = nums[i];
      if (x == 0) {
        sum = 0;
      } else {
        while (x > 0) {
          sum += x % 10;
          x ~/= 10;
        }
      }
      if (sum == i) return i;
    }
    return -1;
  }
}
```

## Golang

```go
func smallestIndex(nums []int) int {
	for i, v := range nums {
		if digitSum(v) == i {
			return i
		}
	}
	return -1
}

func digitSum(n int) int {
	sum := 0
	for n > 0 {
		sum += n % 10
		n /= 10
	}
	return sum
}
```

## Ruby

```ruby
def digit_sum(n)
  sum = 0
  while n > 0
    sum += n % 10
    n /= 10
  end
  sum
end

# @param {Integer[]} nums
# @return {Integer}
def smallest_index(nums)
  nums.each_with_index do |num, i|
    return i if digit_sum(num) == i
  end
  -1
end
```

## Scala

```scala
object Solution {
    def smallestIndex(nums: Array[Int]): Int = {
        def digitSum(x: Int): Int = {
            var n = x
            var sum = 0
            if (n == 0) return 0
            while (n > 0) {
                sum += n % 10
                n /= 10
            }
            sum
        }

        for (i <- nums.indices) {
            if (digitSum(nums(i)) == i) return i
        }
        -1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn smallest_index(nums: Vec<i32>) -> i32 {
        for (i, &num) in nums.iter().enumerate() {
            let mut n = num;
            let mut sum = 0;
            if n == 0 {
                sum = 0;
            } else {
                while n > 0 {
                    sum += n % 10;
                    n /= 10;
                }
            }
            if sum == i as i32 {
                return i as i32;
            }
        }
        -1
    }
}
```

## Racket

```racket
(define (digit-sum n)
  (let loop ((x n) (s 0))
    (if (= x 0)
        s
        (loop (quotient x 10) (+ s (remainder x 10))))))

(define/contract (smallest-index nums)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((lst nums) (idx 0))
    (cond
      [(null? lst) -1]
      [(= (digit-sum (car lst)) idx) idx]
      [else (loop (cdr lst) (+ idx 1))])))
```

## Erlang

```erlang
-module(solution).
-export([smallest_index/1]).

-spec smallest_index(Nums :: [integer()]) -> integer().
smallest_index(Nums) ->
    smallest_index(Nums, 0).

smallest_index([], _Idx) ->
    -1;
smallest_index([H|T], Idx) ->
    case digit_sum(H) of
        S when S =:= Idx -> Idx;
        _ -> smallest_index(T, Idx + 1)
    end.

digit_sum(0) -> 0;
digit_sum(N) ->
    (N rem 10) + digit_sum(N div 10).
```

## Elixir

```elixir
defmodule Solution do
  @spec smallest_index(nums :: [integer]) :: integer
  def smallest_index(nums) do
    Enum.with_index(nums)
    |> Enum.find_value(-1, fn {num, idx} ->
      if digit_sum(num) == idx, do: idx, else: nil
    end)
  end

  defp digit_sum(0), do: 0
  defp digit_sum(n) when n > 0 do
    Integer.digits(n) |> Enum.sum()
  end
end
```
