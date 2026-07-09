# 2160. Minimum Sum of Four Digit Number After Splitting Digits

## Cpp

```cpp
class Solution {
public:
    int minimumSum(int num) {
        std::vector<int> d;
        for (int i = 0; i < 4; ++i) {
            d.push_back(num % 10);
            num /= 10;
        }
        std::sort(d.begin(), d.end());
        return (d[0] * 10 + d[2]) + (d[1] * 10 + d[3]);
    }
};
```

## Java

```java
class Solution {
    public int minimumSum(int num) {
        int[] digits = new int[4];
        for (int i = 3; i >= 0; i--) {
            digits[i] = num % 10;
            num /= 10;
        }
        java.util.Arrays.sort(digits);
        int first = digits[0] * 10 + digits[2];
        int second = digits[1] * 10 + digits[3];
        return first + second;
    }
}
```

## Python

```python
class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = [int(d) for d in str(num)]
        digits.sort()
        return (digits[0] * 10 + digits[2]) + (digits[1] * 10 + digits[3])
```

## Python3

```python
class Solution:
    def minimumSum(self, num: int) -> int:
        digits = sorted(int(d) for d in str(num))
        return (digits[0] * 10 + digits[2]) + (digits[1] * 10 + digits[3])
```

## C

```c
int minimumSum(int num) {
    int d[4];
    for (int i = 0; i < 4; ++i) {
        d[i] = num % 10;
        num /= 10;
    }
    // Simple sort for 4 elements
    for (int i = 0; i < 3; ++i) {
        for (int j = i + 1; j < 4; ++j) {
            if (d[i] > d[j]) {
                int tmp = d[i];
                d[i] = d[j];
                d[j] = tmp;
            }
        }
    }
    int n1 = d[0] * 10 + d[2];
    int n2 = d[1] * 10 + d[3];
    return n1 + n2;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumSum(int num) {
        int[] d = new int[4];
        for (int i = 0; i < 4; i++) {
            d[i] = num % 10;
            num /= 10;
        }
        Array.Sort(d);
        return (d[0] * 10 + d[2]) + (d[1] * 10 + d[3]);
    }
}
```

## Javascript

```javascript
/**
 * @param {number} num
 * @return {number}
 */
var minimumSum = function(num) {
    const digits = String(num).split('').map(Number).sort((a, b) => a - b);
    const new1 = digits[0] * 10 + digits[2];
    const new2 = digits[1] * 10 + digits[3];
    return new1 + new2;
};
```

## Typescript

```typescript
function minimumSum(num: number): number {
    const digits = num.toString().split('').map(d => parseInt(d)).sort((a, b) => a - b);
    const new1 = digits[0] * 10 + digits[2];
    const new2 = digits[1] * 10 + digits[3];
    return new1 + new2;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $num
     * @return Integer
     */
    function minimumSum($num) {
        $digits = [];
        while ($num > 0) {
            $digits[] = $num % 10;
            $num = intdiv($num, 10);
        }
        sort($digits); // ascending order
        return ($digits[0] * 10 + $digits[2]) + ($digits[1] * 10 + $digits[3]);
    }
}
```

## Swift

```swift
class Solution {
    func minimumSum(_ num: Int) -> Int {
        var digits = [Int]()
        var n = num
        for _ in 0..<4 {
            digits.append(n % 10)
            n /= 10
        }
        digits.sort()
        return (digits[0] * 10 + digits[2]) + (digits[1] * 10 + digits[3])
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumSum(num: Int): Int {
        val digits = IntArray(4)
        var n = num
        for (i in 3 downTo 0) {
            digits[i] = n % 10
            n /= 10
        }
        digits.sort()
        return (digits[0] + digits[1]) * 10 + (digits[2] + digits[3])
    }
}
```

## Dart

```dart
class Solution {
  int minimumSum(int num) {
    List<int> digits = [];
    for (int i = 0; i < 4; i++) {
      digits.add(num % 10);
      num ~/= 10;
    }
    digits.sort();
    return (digits[0] * 10 + digits[2]) + (digits[1] * 10 + digits[3]);
  }
}
```

## Golang

```go
package main

import "sort"

func minimumSum(num int) int {
	digits := []int{0, 0, 0, 0}
	for i := 0; i < 4; i++ {
		digits[i] = num % 10
		num /= 10
	}
	sort.Ints(digits)
	return 10*(digits[0]+digits[1]) + digits[2] + digits[3]
}
```

## Ruby

```ruby
def minimum_sum(num)
  digits = num.to_s.chars.map(&:to_i).sort
  a, b, c, d = digits
  (a * 10 + c) + (b * 10 + d)
end
```

## Scala

```scala
object Solution {
    def minimumSum(num: Int): Int = {
        val digits = num.toString.map(_.asDigit).sorted
        (digits(0) * 10 + digits(2)) + (digits(1) * 10 + digits(3))
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_sum(num: i32) -> i32 {
        let mut digits = Vec::with_capacity(4);
        let mut n = num;
        for _ in 0..4 {
            digits.push((n % 10) as i32);
            n /= 10;
        }
        digits.sort();
        (digits[0] * 10 + digits[2]) + (digits[1] * 10 + digits[3])
    }
}
```

## Racket

```racket
(define/contract (minimum-sum num)
  (-> exact-integer? exact-integer?)
  (let* ([digits (map (lambda (c) (- (char->integer c) (char->integer #\0)))
                      (string->list (number->string num)))]
         [sorted (sort digits <)])
    (+ (* 10 (+ (list-ref sorted 0) (list-ref sorted 1)))
       (+ (list-ref sorted 2) (list-ref sorted 3)))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_sum/1]).

-spec minimum_sum(Num :: integer()) -> integer().
minimum_sum(Num) ->
    D0 = Num div 1000,
    D1 = (Num rem 1000) div 100,
    D2 = (Num rem 100) div 10,
    D3 = Num rem 10,
    Sorted = lists:sort([D0, D1, D2, D3]),
    [A, B, C, D] = Sorted,
    N1 = A * 10 + C,
    N2 = B * 10 + D,
    N1 + N2.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_sum(num :: integer) :: integer
  def minimum_sum(num) do
    digits = Integer.digits(num) |> Enum.sort()
    a = Enum.at(digits, 0) * 10 + Enum.at(digits, 2)
    b = Enum.at(digits, 1) * 10 + Enum.at(digits, 3)
    a + b
  end
end
```
