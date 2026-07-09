# 3099. Harshad Number

## Cpp

```cpp
class Solution {
public:
    int sumOfTheDigitsOfHarshadNumber(int x) {
        int original = x;
        int sum = 0;
        while (x > 0) {
            sum += x % 10;
            x /= 10;
        }
        if (sum == 0) return -1; // avoid division by zero, though not needed per constraints
        return (original % sum == 0) ? sum : -1;
    }
};
```

## Java

```java
class Solution {
    public int sumOfTheDigitsOfHarshadNumber(int x) {
        int original = x;
        int sum = 0;
        while (x > 0) {
            sum += x % 10;
            x /= 10;
        }
        if (sum != 0 && original % sum == 0) {
            return sum;
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = 0
        temp = x
        while temp > 0:
            s += temp % 10
            temp //= 10
        return s if x % s == 0 else -1
```

## Python3

```python
class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = 0
        n = x
        while n > 0:
            s += n % 10
            n //= 10
        return s if s != 0 and x % s == 0 else -1
```

## C

```c
int sumOfTheDigitsOfHarshadNumber(int x) {
    int sum = 0;
    int t = x;
    while (t > 0) {
        sum += t % 10;
        t /= 10;
    }
    if (sum != 0 && x % sum == 0)
        return sum;
    return -1;
}
```

## Csharp

```csharp
public class Solution {
    public int SumOfTheDigitsOfHarshadNumber(int x) {
        int sum = 0;
        int temp = x;
        while (temp > 0) {
            sum += temp % 10;
            temp /= 10;
        }
        return (sum != 0 && x % sum == 0) ? sum : -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} x
 * @return {number}
 */
var sumOfTheDigitsOfHarshadNumber = function(x) {
    let sum = 0;
    let n = x;
    while (n > 0) {
        sum += n % 10;
        n = Math.floor(n / 10);
    }
    return sum !== 0 && x % sum === 0 ? sum : -1;
};
```

## Typescript

```typescript
function sumOfTheDigitsOfHarshadNumber(x: number): number {
    let n = x;
    let sum = 0;
    while (n > 0) {
        sum += n % 10;
        n = Math.floor(n / 10);
    }
    return x % sum === 0 ? sum : -1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $x
     * @return Integer
     */
    function sumOfTheDigitsOfHarshadNumber($x) {
        $sum = 0;
        $temp = $x;
        while ($temp > 0) {
            $sum += $temp % 10;
            $temp = intdiv($temp, 10);
        }
        return ($x % $sum === 0) ? $sum : -1;
    }
}
```

## Swift

```swift
class Solution {
    func sumOfTheDigitsOfHarshadNumber(_ x: Int) -> Int {
        var n = x
        var sum = 0
        while n > 0 {
            sum += n % 10
            n /= 10
        }
        return (sum != 0 && x % sum == 0) ? sum : -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sumOfTheDigitsOfHarshadNumber(x: Int): Int {
        var n = x
        var sum = 0
        while (n > 0) {
            sum += n % 10
            n /= 10
        }
        return if (x % sum == 0) sum else -1
    }
}
```

## Dart

```dart
class Solution {
  int sumOfTheDigitsOfHarshadNumber(int x) {
    int original = x;
    int sum = 0;
    while (x > 0) {
      sum += x % 10;
      x ~/= 10;
    }
    if (sum == 0) return -1; // though not possible for x>=1
    return (original % sum == 0) ? sum : -1;
  }
}
```

## Golang

```go
func sumOfTheDigitsOfHarshadNumber(x int) int {
	sum := 0
	for t := x; t > 0; t /= 10 {
		sum += t % 10
	}
	if sum != 0 && x%sum == 0 {
		return sum
	}
	return -1
}
```

## Ruby

```ruby
# @param {Integer} x
# @return {Integer}
def sum_of_the_digits_of_harshad_number(x)
  sum = 0
  n = x
  while n > 0
    sum += n % 10
    n /= 10
  end
  (sum != 0 && x % sum == 0) ? sum : -1
end
```

## Scala

```scala
object Solution {
    def sumOfTheDigitsOfHarshadNumber(x: Int): Int = {
        var n = x
        var sum = 0
        while (n > 0) {
            sum += n % 10
            n /= 10
        }
        if (sum != 0 && x % sum == 0) sum else -1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sum_of_the_digits_of_harshad_number(x: i32) -> i32 {
        let mut n = x;
        let mut sum = 0;
        while n > 0 {
            sum += n % 10;
            n /= 10;
        }
        if sum != 0 && x % sum == 0 { sum } else { -1 }
    }
}
```

## Racket

```racket
(define/contract (sum-of-the-digits-of-harshad-number x)
  (-> exact-integer? exact-integer?)
  (let ((sum (let loop ((n x) (s 0))
               (if (= n 0)
                   s
                   (loop (quotient n 10) (+ s (remainder n 10)))))))
    (if (and (> sum 0) (= (remainder x sum) 0))
        sum
        -1)))
```

## Erlang

```erlang
-spec sum_of_the_digits_of_harshad_number(X :: integer()) -> integer().
sum_of_the_digits_of_harshad_number(X) ->
    Sum = digit_sum(X),
    case X rem Sum of
        0 -> Sum;
        _ -> -1
    end.

digit_sum(0) -> 0;
digit_sum(N) when N < 10 -> N;
digit_sum(N) ->
    digit_sum(N div 10) + (N rem 10).
```

## Elixir

```elixir
defmodule Solution do
  @spec sum_of_the_digits_of_harshad_number(x :: integer) :: integer
  def sum_of_the_digits_of_harshad_number(x) do
    sum = Integer.digits(x) |> Enum.sum()
    if sum != 0 and rem(x, sum) == 0, do: sum, else: -1
  end
end
```
