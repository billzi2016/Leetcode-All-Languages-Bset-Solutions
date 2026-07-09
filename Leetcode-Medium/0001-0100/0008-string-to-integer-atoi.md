# 0008. String to Integer (atoi)

## Cpp

```cpp
class Solution {
public:
    int myAtoi(string s) {
        int i = 0, n = s.size();
        // skip leading whitespaces
        while (i < n && s[i] == ' ') ++i;
        if (i == n) return 0;
        // sign
        int sign = 1;
        if (s[i] == '+' || s[i] == '-') {
            if (s[i] == '-') sign = -1;
            ++i;
        }
        long long result = 0;
        while (i < n && isdigit(s[i])) {
            result = result * 10 + (s[i] - '0');
            if (sign == 1 && result > INT_MAX) return INT_MAX;
            if (sign == -1 && -result < INT_MIN) return INT_MIN;
            ++i;
        }
        result *= sign;
        if (result > INT_MAX) return INT_MAX;
        if (result < INT_MIN) return INT_MIN;
        return static_cast<int>(result);
    }
};
```

## Java

```java
class Solution {
    public int myAtoi(String s) {
        int i = 0, n = s.length();
        // Skip leading whitespaces
        while (i < n && s.charAt(i) == ' ') {
            i++;
        }
        if (i == n) return 0;
        
        // Determine sign
        int sign = 1;
        char ch = s.charAt(i);
        if (ch == '+' || ch == '-') {
            sign = (ch == '-') ? -1 : 1;
            i++;
        }
        
        long result = 0;
        while (i < n && Character.isDigit(s.charAt(i))) {
            int digit = s.charAt(i) - '0';
            result = result * 10 + digit;
            if (sign == 1 && result > Integer.MAX_VALUE) return Integer.MAX_VALUE;
            if (sign == -1 && -result < Integer.MIN_VALUE) return Integer.MIN_VALUE;
            i++;
        }
        
        result *= sign;
        if (result > Integer.MAX_VALUE) return Integer.MAX_VALUE;
        if (result < Integer.MIN_VALUE) return Integer.MIN_VALUE;
        return (int) result;
    }
}
```

## Python

```python
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, n = 0, len(s)
        # Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1
        if i == n:
            return 0

        # Determine sign
        sign = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1

        result = 0
        INT_MAX, INT_MIN = 2**31 - 1, -2**31

        # Convert digits to integer
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            # Check overflow/underflow before adding the digit
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            result = result * 10 + digit
            i += 1

        return sign * result
```

## Python3

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        i, n = 0, len(s)
        while i < n and s[i] == ' ':
            i += 1
        if i == n:
            return 0

        sign = 1
        if s[i] in '+-':
            if s[i] == '-':
                sign = -1
            i += 1

        result = 0
        INT_MAX, INT_MIN = 2**31 - 1, -2**31

        while i < n and s[i].isdigit():
            digit = ord(s[i]) - 48
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            result = result * 10 + digit
            i += 1

        result *= sign
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        return result
```

## C

```c
#include <limits.h>

int myAtoi(char* s) {
    int i = 0;
    while (s[i] == ' ') i++;

    int sign = 1;
    if (s[i] == '+' || s[i] == '-') {
        if (s[i] == '-') sign = -1;
        i++;
    }

    long long num = 0;
    while (s[i] >= '0' && s[i] <= '9') {
        int digit = s[i] - '0';
        num = num * 10 + digit;

        if (sign == 1 && num > INT_MAX) return INT_MAX;
        if (sign == -1 && num > (long long)INT_MAX + 1) return INT_MIN;

        i++;
    }

    long long result = sign * num;
    if (result > INT_MAX) return INT_MAX;
    if (result < INT_MIN) return INT_MIN;
    return (int)result;
}
```

## Csharp

```csharp
public class Solution {
    public int MyAtoi(string s) {
        int i = 0, n = s.Length;
        // Skip leading whitespaces
        while (i < n && s[i] == ' ') i++;
        if (i == n) return 0;

        // Sign handling
        int sign = 1;
        if (s[i] == '+' || s[i] == '-') {
            if (s[i] == '-') sign = -1;
            i++;
        }

        long result = 0;
        while (i < n && char.IsDigit(s[i])) {
            int digit = s[i] - '0';
            result = result * 10 + digit;

            long signedResult = result * sign;
            if (signedResult > int.MaxValue) return int.MaxValue;
            if (signedResult < int.MinValue) return int.MinValue;

            i++;
        }

        return (int)(result * sign);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function(s) {
    let i = 0, n = s.length;
    while (i < n && s[i] === ' ') i++;
    if (i === n) return 0;
    
    let sign = 1;
    if (s[i] === '+' || s[i] === '-') {
        if (s[i] === '-') sign = -1;
        i++;
    }
    
    const INT_MAX = 2 ** 31 - 1;
    const INT_MIN = -(2 ** 31);
    let result = 0;
    
    while (i < n && s[i] >= '0' && s[i] <= '9') {
        const digit = s.charCodeAt(i) - 48;
        if (result > Math.floor(INT_MAX / 10) || 
            (result === Math.floor(INT_MAX / 10) && digit > INT_MAX % 10)) {
            return sign === 1 ? INT_MAX : INT_MIN;
        }
        result = result * 10 + digit;
        i++;
    }
    
    return result * sign;
};
```

## Typescript

```typescript
function myAtoi(s: string): number {
    let i = 0, n = s.length;
    while (i < n && s[i] === ' ') i++;
    let sign = 1;
    if (i < n && (s[i] === '+' || s[i] === '-')) {
        if (s[i] === '-') sign = -1;
        i++;
    }
    const INT_MAX = 2147483647;
    const INT_MIN = -2147483648;
    let result = 0;
    while (i < n) {
        const code = s.charCodeAt(i);
        if (code < 48 || code > 57) break;
        const digit = code - 48;
        if (result > Math.floor((INT_MAX - digit) / 10)) {
            return sign === 1 ? INT_MAX : INT_MIN;
        }
        result = result * 10 + digit;
        i++;
    }
    return result * sign;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function myAtoi($s) {
        $i = 0;
        $n = strlen($s);
        // Skip leading whitespaces
        while ($i < $n && $s[$i] === ' ') {
            $i++;
        }
        if ($i >= $n) {
            return 0;
        }

        // Determine sign
        $sign = 1;
        if ($s[$i] === '+' || $s[$i] === '-') {
            if ($s[$i] === '-') {
                $sign = -1;
            }
            $i++;
        }

        $result = 0;
        $INT_MAX = 2147483647;
        $INT_MIN = -2147483648;

        // Process digits
        while ($i < $n && ctype_digit($s[$i])) {
            $digit = ord($s[$i]) - ord('0');

            // Check overflow before adding the digit
            if (
                $result > intdiv($INT_MAX, 10) ||
                ($result == intdiv($INT_MAX, 10) && $digit > $INT_MAX % 10)
            ) {
                return $sign === 1 ? $INT_MAX : $INT_MIN;
            }

            $result = $result * 10 + $digit;
            $i++;
        }

        return $result * $sign;
    }
}
```

## Swift

```swift
class Solution {
    func myAtoi(_ s: String) -> Int {
        var i = s.startIndex
        let n = s.endIndex
        
        // Skip leading whitespaces
        while i < n && s[i] == " " {
            i = s.index(after: i)
        }
        
        if i == n { return 0 }
        
        // Determine sign
        var sign = 1
        if s[i] == "+" {
            i = s.index(after: i)
        } else if s[i] == "-" {
            sign = -1
            i = s.index(after: i)
        }
        
        var result: Int64 = 0
        while i < n, let digit = s[i].wholeNumberValue {
            result = result * 10 + Int64(digit)
            
            // Early overflow detection
            if sign == 1 && result > Int64(Int32.max) {
                return Int(Int32.max)
            }
            if sign == -1 && -result < Int64(Int32.min) {
                return Int(Int32.min)
            }
            
            i = s.index(after: i)
        }
        
        let signedResult = result * Int64(sign)
        if signedResult > Int64(Int32.max) { return Int(Int32.max) }
        if signedResult < Int64(Int32.min) { return Int(Int32.min) }
        return Int(signedResult)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun myAtoi(s: String): Int {
        var i = 0
        val n = s.length
        // Skip leading whitespaces
        while (i < n && s[i] == ' ') i++
        if (i >= n) return 0

        var sign = 1
        when (s[i]) {
            '+' -> i++
            '-' -> { sign = -1; i++ }
        }

        var result = 0L
        while (i < n && s[i].isDigit()) {
            val digit = (s[i] - '0')
            result = result * 10 + digit
            // Early overflow check
            if (sign == 1 && result > Int.MAX_VALUE) return Int.MAX_VALUE
            if (sign == -1 && result > Int.MAX_VALUE.toLong() + 1) return Int.MIN_VALUE
            i++
        }

        val finalVal = sign * result
        return when {
            finalVal > Int.MAX_VALUE -> Int.MAX_VALUE
            finalVal < Int.MIN_VALUE -> Int.MIN_VALUE
            else -> finalVal.toInt()
        }
    }
}
```

## Dart

```dart
class Solution {
  int myAtoi(String s) {
    int i = 0;
    int n = s.length;

    // Skip leading whitespaces
    while (i < n && s[i] == ' ') {
      i++;
    }
    if (i == n) return 0;

    // Sign handling
    int sign = 1;
    if (s[i] == '+' || s[i] == '-') {
      if (s[i] == '-') sign = -1;
      i++;
    }

    const int INT_MAX = 2147483647;
    const int INT_MIN = -2147483648;

    int result = 0;
    while (i < n) {
      int code = s.codeUnitAt(i);
      if (code < 48 || code > 57) break; // not a digit
      int digit = code - 48;

      // Check overflow before adding the digit
      if (result > (INT_MAX - digit) ~/ 10) {
        return sign == 1 ? INT_MAX : INT_MIN;
      }

      result = result * 10 + digit;
      i++;
    }

    return result * sign;
  }
}
```

## Golang

```go
func myAtoi(s string) int {
	const INT_MAX = 2147483647
	const INT_MIN = -2147483648

	i, n := 0, len(s)
	// Skip leading spaces
	for i < n && s[i] == ' ' {
		i++
	}
	// Determine sign
	sign := 1
	if i < n {
		if s[i] == '+' {
			i++
		} else if s[i] == '-' {
			sign = -1
			i++
		}
	}
	// Convert digits
	result := 0
	for i < n && s[i] >= '0' && s[i] <= '9' {
		digit := int(s[i] - '0')
		if result > (INT_MAX-digit)/10 {
			if sign == 1 {
				return INT_MAX
			}
			return INT_MIN
		}
		result = result*10 + digit
		i++
	}
	return result * sign
}
```

## Ruby

```ruby
def my_atoi(s)
  i = 0
  n = s.length
  while i < n && s.getbyte(i) == 32
    i += 1
  end
  return 0 if i >= n

  sign = 1
  if (b = s.getbyte(i)) == 43 || b == 45
    sign = -1 if b == 45
    i += 1
  end

  num = 0
  while i < n
    c = s.getbyte(i)
    break unless c >= 48 && c <= 57
    num = num * 10 + (c - 48)
    i += 1
  end

  result = sign * num
  int_min = -2**31
  int_max = 2**31 - 1
  if result < int_min
    int_min
  elsif result > int_max
    int_max
  else
    result
  end
end
```

## Scala

```scala
object Solution {
  def myAtoi(s: String): Int = {
    val n = s.length
    var i = 0
    while (i < n && s.charAt(i).isWhitespace) i += 1
    if (i >= n) return 0

    var sign = 1
    val first = s.charAt(i)
    if (first == '+' || first == '-') {
      if (first == '-') sign = -1
      i += 1
    }

    var num: Long = 0L
    while (i < n && s.charAt(i).isDigit) {
      val digit = s.charAt(i) - '0'
      if (num > (Int.MaxValue - digit) / 10) {
        return if (sign == 1) Int.MaxValue else Int.MinValue
      }
      num = num * 10 + digit
      i += 1
    }

    val result = sign * num
    if (result > Int.MaxValue) Int.MaxValue
    else if (result < Int.MinValue) Int.MinValue
    else result.toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn my_atoi(s: String) -> i32 {
        let bytes = s.as_bytes();
        let mut i = 0;
        let n = bytes.len();

        // Skip leading spaces
        while i < n && bytes[i] == b' ' {
            i += 1;
        }
        if i >= n {
            return 0;
        }

        // Determine sign
        let mut sign: i64 = 1;
        if bytes[i] == b'+' {
            i += 1;
        } else if bytes[i] == b'-' {
            sign = -1;
            i += 1;
        }

        // Parse digits
        let mut result: i64 = 0;
        while i < n && (bytes[i] >= b'0' && bytes[i] <= b'9') {
            let digit = (bytes[i] - b'0') as i64;
            result = result * 10 + digit;

            // Early overflow handling
            if sign == 1 && result > i32::MAX as i64 {
                return i32::MAX;
            }
            if sign == -1 && -result < i32::MIN as i64 {
                return i32::MIN;
            }

            i += 1;
        }

        let ans = sign * result;
        if ans > i32::MAX as i64 {
            i32::MAX
        } else if ans < i32::MIN as i64 {
            i32::MIN
        } else {
            ans as i32
        }
    }
}
```

## Racket

```racket
(define/contract (my-atoi s)
  (-> string? exact-integer?)
  (let* ((len (string-length s))
         (skip (let loop ((i 0))
                 (if (and (< i len) (char-whitespace? (string-ref s i)))
                     (loop (+ i 1))
                     i))))
    (if (>= skip len)
        0
        (let* ((first (string-ref s skip))
               (sign (cond [(char=? first #\-) -1]
                           [(char=? first #\+) 1]
                           [else 1]))
               (start (if (or (char=? first #\-) (char=? first #\+)) (+ skip 1) skip))
               (INT-MAX 2147483647)
               (INT-MIN -2147483648)
               (LIMIT-NEG-ABS (- INT-MIN))) ; = 2147483648
          (let loop ((i start) (res 0))
            (if (and (< i len) (char-digit? (string-ref s i)))
                (let* ((digit (- (char->integer (string-ref s i))
                                 (char->integer #\0))))
                  (cond
                    [(and (= sign 1)
                          (or (> res (quotient INT-MAX 10))
                              (and (= res (quotient INT-MAX 10))
                                   (> digit (remainder INT-MAX 10)))))
                     INT-MAX]
                    [(and (= sign -1)
                          (or (> res (quotient LIMIT-NEG-ABS 10))
                              (and (= res (quotient LIMIT-NEG-ABS 10))
                                   (> digit (remainder LIMIT-NEG-ABS 10)))))
                     INT-MIN]
                    [else
                     (loop (+ i 1) (+ (* res 10) digit))]))
                (* sign res)))))))
```

## Erlang

```erlang
-module(solution).
-export([my_atoi/1]).

-spec my_atoi(S :: unicode:unicode_binary()) -> integer().
my_atoi(S) ->
    Bin = unicode:characters_to_binary(S),
    Trimmed = skip_spaces(Bin),
    {Sign, Rest} = case Trimmed of
        <<"+" , R/binary>> -> {1, R};
        <<"-", R/binary>> -> {-1, R};
        _ -> {1, Trimmed}
    end,
    Number = parse_digits(Rest, 0),
    Signed = Sign * Number,
    clamp(Signed).

skip_spaces(<<>>) -> <<>>;
skip_spaces(<<" ", Rest/binary>>) -> skip_spaces(Rest);
skip_spaces(Bin) -> Bin.

parse_digits(<<>>, Acc) -> Acc;
parse_digits(<<C, Rest/binary>>, Acc) when C >= $0, C =< $9 ->
    Digit = C - $0,
    parse_digits(Rest, Acc * 10 + Digit);
parse_digits(_, Acc) -> Acc.

clamp(N) when N > 2147483647 -> 2147483647;
clamp(N) when N < -2147483648 -> -2147483648;
clamp(N) -> N.
```

## Elixir

```elixir
defmodule Solution do
  @spec my_atoi(s :: String.t()) :: integer
  def my_atoi(s) do
    s = String.trim_leading(s)

    {sign, rest} =
      case s do
        <<?- , tail::binary>> -> {-1, tail}
        <<?+ , tail::binary>> -> {1, tail}
        _ -> {1, s}
      end

    digits = extract_digits(rest, "")

    result =
      if digits == "" do
        0
      else
        String.to_integer(digits)
      end

    clamp(sign * result)
  end

  defp extract_digits(<<c, rest::binary>>, acc) when c >= ?0 and c <= ?9 do
    extract_digits(rest, <<acc::binary, c>>)
  end

  defp extract_digits(_, acc), do: acc

  defp clamp(val) do
    min = -2_147_483_648
    max = 2_147_483_647

    cond do
      val < min -> min
      val > max -> max
      true -> val
    end
  end
end
```
