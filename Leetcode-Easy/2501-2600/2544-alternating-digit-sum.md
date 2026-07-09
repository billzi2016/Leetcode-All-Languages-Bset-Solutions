# 2544. Alternating Digit Sum

## Cpp

```cpp
class Solution {
public:
    int alternateDigitSum(int n) {
        std::string s = std::to_string(n);
        int sign = 1;
        int ans = 0;
        for (char c : s) {
            ans += sign * (c - '0');
            sign = -sign;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int alternateDigitSum(int n) {
        String s = Integer.toString(n);
        int sign = 1;
        int ans = 0;
        for (int i = 0; i < s.length(); i++) {
            int digit = s.charAt(i) - '0';
            ans += sign * digit;
            sign = -sign;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        sign = 1
        for ch in str(n):
            total += sign * (ord(ch) - 48)
            sign = -sign
        return total
```

## Python3

```python
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        total = 0
        sign = 1
        for ch in str(n):
            total += sign * (ord(ch) - 48)
            sign = -sign
        return total
```

## C

```c
int alternateDigitSum(int n) {
    int sign = 1, ans = 0;
    int divisor = 1;
    while (n / divisor >= 10) divisor *= 10;
    while (divisor > 0) {
        int digit = n / divisor;
        ans += sign * digit;
        sign = -sign;
        n %= divisor;
        divisor /= 10;
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int AlternateDigitSum(int n) {
        int sign = 1;
        int sum = 0;
        foreach (char c in n.ToString()) {
            int digit = c - '0';
            sum += sign * digit;
            sign = -sign;
        }
        return sum;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var alternateDigitSum = function(n) {
    const s = n.toString();
    let sum = 0;
    let sign = 1;
    for (let i = 0; i < s.length; i++) {
        sum += sign * (s.charCodeAt(i) - 48);
        sign = -sign;
    }
    return sum;
};
```

## Typescript

```typescript
function alternateDigitSum(n: number): number {
    const s = n.toString();
    let sign = 1;
    let sum = 0;
    for (let i = 0; i < s.length; i++) {
        sum += sign * (s.charCodeAt(i) - 48);
        sign = -sign;
    }
    return sum;
}
```

## Php

```php
<?php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function alternateDigitSum($n) {
        $s = strval($n);
        $sign = 1;
        $ans = 0;
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $digit = intval($s[$i]);
            $ans += $sign * $digit;
            $sign = -$sign;
        }
        return $ans;
    }
}
?>
```

## Swift

```swift
class Solution {
    func alternateDigitSum(_ n: Int) -> Int {
        var sign = 1
        var result = 0
        for ch in String(n) {
            if let digit = ch.wholeNumberValue {
                result += sign * digit
                sign *= -1
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun alternateDigitSum(n: Int): Int {
        var sign = 1
        var sum = 0
        for (ch in n.toString()) {
            val digit = ch - '0'
            sum += sign * digit
            sign = -sign
        }
        return sum
    }
}
```

## Dart

```dart
class Solution {
  int alternateDigitSum(int n) {
    int sign = 1;
    int ans = 0;
    for (int i = 0; i < n.toString().length; i++) {
      int digit = n.toString().codeUnitAt(i) - 48;
      ans += sign * digit;
      sign = -sign;
    }
    return ans;
  }
}
```

## Golang

```go
package main

import "strconv"

func alternateDigitSum(n int) int {
	s := strconv.Itoa(n)
	sum, sign := 0, 1
	for i := 0; i < len(s); i++ {
		digit := int(s[i] - '0')
		sum += sign * digit
		sign = -sign
	}
	return sum
}
```

## Ruby

```ruby
def alternate_digit_sum(n)
  sum = 0
  n.to_s.each_char.with_index do |ch, idx|
    digit = ch.ord - 48
    sum += (idx.even? ? 1 : -1) * digit
  end
  sum
end
```

## Scala

```scala
object Solution {
    def alternateDigitSum(n: Int): Int = {
        var sum = 0
        var sign = 1
        for (c <- n.toString) {
            sum += sign * (c - '0')
            sign = -sign
        }
        sum
    }
}
```

## Rust

```rust
impl Solution {
    pub fn alternate_digit_sum(n: i32) -> i32 {
        let mut sign = 1;
        let mut sum = 0;
        for ch in n.to_string().chars() {
            let digit = ch.to_digit(10).unwrap() as i32;
            sum += sign * digit;
            sign = -sign;
        }
        sum
    }
}
```

## Racket

```racket
(define/contract (alternate-digit-sum n)
  (-> exact-integer? exact-integer?)
  (let* ((s (number->string n))
         (len (string-length s)))
    (for/sum ([i (in-range len)])
      (let* ((digit (- (char->integer (string-ref s i)) (char->integer #\0)))
             (sign (if (even? i) 1 -1)))
        (* sign digit)))))
```

## Erlang

```erlang
-module(solution).
-export([alternate_digit_sum/1]).

-spec alternate_digit_sum(N :: integer()) -> integer().
alternate_digit_sum(N) ->
    Digits = integer_to_list(N),
    alt_sum(Digits, 1).

alt_sum([], _Sign) -> 0;
alt_sum([C|Cs], Sign) ->
    Digit = C - $0,
    Sign * Digit + alt_sum(Cs, -Sign).
```

## Elixir

```elixir
defmodule Solution do
  @spec alternate_digit_sum(n :: integer) :: integer
  def alternate_digit_sum(n) do
    n
    |> Integer.to_string()
    |> String.graphemes()
    |> Enum.with_index()
    |> Enum.reduce(0, fn {ch, idx}, acc ->
      digit = String.to_integer(ch)
      sign = if rem(idx, 2) == 0, do: 1, else: -1
      acc + sign * digit
    end)
  end
end
```
