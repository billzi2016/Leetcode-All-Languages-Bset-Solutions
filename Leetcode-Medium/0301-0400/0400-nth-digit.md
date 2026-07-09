# 0400. Nth Digit

## Cpp

```cpp
class Solution {
public:
    int findNthDigit(int n) {
        long long len = 1;          // current digit length
        long long count = 9;        // numbers with 'len' digits
        long long start = 1;        // first number with 'len' digits
        long long nn = n;
        
        while (nn > len * count) {
            nn -= len * count;
            ++len;
            count *= 10;
            start *= 10;
        }
        
        long long number = start + (nn - 1) / len;   // the actual number containing the digit
        int idx = (int)((nn - 1) % len);             // index within that number
        
        string s = to_string(number);
        return s[idx] - '0';
    }
};
```

## Java

```java
class Solution {
    public int findNthDigit(int n) {
        long remaining = n;
        long digitLen = 1;
        long count = 9;
        while (remaining > digitLen * count) {
            remaining -= digitLen * count;
            digitLen++;
            count *= 10;
        }
        long start = (long)Math.pow(10, digitLen - 1);
        long number = start + (remaining - 1) / digitLen;
        int idx = (int)((remaining - 1) % digitLen);
        return Long.toString(number).charAt(idx) - '0';
    }
}
```

## Python

```python
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        length = 1          # current digit length
        count = 9           # numbers with this length
        while n > length * count:
            n -= length * count
            length += 1
            count *= 10

        start = 10 ** (length - 1)
        number = start + (n - 1) // length
        digit_index = (n - 1) % length
        return int(str(number)[digit_index])
```

## Python3

```python
class Solution:
    def findNthDigit(self, n: int) -> int:
        length = 1
        count = 9
        start = 1
        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10
        num = start + (n - 1) // length
        return int(str(num)[(n - 1) % length])
```

## C

```c
int findNthDigit(int n) {
    long long len = 1;
    long long count = 9;
    long long start = 1;
    while (n > len * count) {
        n -= (int)(len * count);
        ++len;
        count *= 10;
        start *= 10;
    }
    long long num = start + (n - 1) / len;
    int idx = (n - 1) % len; // zero‑based index from left
    long long divisor = 1;
    for (int i = 0; i < len - idx - 1; ++i) {
        divisor *= 10;
    }
    return (int)((num / divisor) % 10);
}
```

## Csharp

```csharp
public class Solution {
    public int FindNthDigit(int n) {
        long nn = n;
        long digitLength = 1;
        long count = 9;
        while (nn > digitLength * count) {
            nn -= digitLength * count;
            digitLength++;
            count *= 10;
        }
        long start = 1;
        for (int i = 1; i < digitLength; i++) {
            start *= 10;
        }
        long number = start + (nn - 1) / digitLength;
        int digitIndex = (int)((nn - 1) % digitLength);
        string s = number.ToString();
        return s[digitIndex] - '0';
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var findNthDigit = function(n) {
    let length = 1;          // current digit length
    let count = 9;           // numbers with this length
    while (n > length * count) {
        n -= length * count;
        length += 1;
        count *= 10;
    }
    const start = Math.pow(10, length - 1);
    const offset = Math.floor((n - 1) / length);
    const num = start + offset;
    const digitIndex = (n - 1) % length;
    return Number(String(num)[digitIndex]);
};
```

## Typescript

```typescript
function findNthDigit(n: number): number {
    let length = 1;
    let count = 9;
    let start = 1;

    while (n > length * count) {
        n -= length * count;
        length++;
        count *= 10;
        start *= 10;
    }

    const num = start + Math.floor((n - 1) / length);
    const digitStr = String(num);
    return Number(digitStr[(n - 1) % length]);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function findNthDigit($n) {
        $len = 1;
        $start = 1;
        while (true) {
            $count = 9 * $start;               // numbers with current length
            $totalDigits = $len * $count;      // total digits contributed by this group
            if ($n <= $totalDigits) {
                break;
            }
            $n -= $totalDigits;
            $len++;
            $start *= 10;
        }

        $num = $start + intdiv($n - 1, $len);   // the actual number containing the nth digit
        $digitIndex = ($n - 1) % $len;          // index within that number (0‑based)

        $s = strval($num);
        return intval($s[$digitIndex]);
    }
}
```

## Swift

```swift
class Solution {
    func findNthDigit(_ n: Int) -> Int {
        var n = n
        var length = 1               // current digit length
        var count = 9                // numbers with 'length' digits
        var start = 1                // first number with 'length' digits
        
        while n > length * count {
            n -= length * count
            length += 1
            count *= 10
            start *= 10
        }
        
        let number = start + (n - 1) / length
        let digitIndex = (n - 1) % length   // index from left, 0‑based
        
        var num = number
        var digits = [Int]()
        for _ in 0..<length {
            digits.append(num % 10)
            num /= 10
        }
        // digits are stored least‑significant first
        return digits[length - 1 - digitIndex]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findNthDigit(n: Int): Int {
        var nLong = n.toLong()
        var digits = 1L
        var count = 9L
        var start = 1L

        while (nLong > digits * count) {
            nLong -= digits * count
            digits += 1
            count *= 10
            start *= 10
        }

        val offset = (nLong - 1) / digits
        val number = start + offset
        val digitIndex = ((nLong - 1) % digits).toInt()
        return number.toString()[digitIndex] - '0'
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int findNthDigit(int n) {
    int digitLength = 1;
    int count = 9;
    while (n > digitLength * count) {
      n -= digitLength * count;
      digitLength++;
      count *= 10;
    }
    int start = pow(10, digitLength - 1).toInt();
    int offset = (n - 1) ~/ digitLength;
    int number = start + offset;
    int digitIndex = (n - 1) % digitLength;
    return int.parse(number.toString()[digitIndex]);
  }
}
```

## Golang

```go
func findNthDigit(n int) int {
    length := 1
    count := 9
    start := 1

    for n > length*count {
        n -= length * count
        length++
        count *= 10
        start *= 10
    }

    num := start + (n-1)/length
    digitIdx := (n - 1) % length

    divisor := 1
    for i := 0; i < length-digitIdx-1; i++ {
        divisor *= 10
    }
    return (num / divisor) % 10
}
```

## Ruby

```ruby
def find_nth_digit(n)
  length = 1
  count = 9
  start = 1
  while n > length * count
    n -= length * count
    length += 1
    count *= 10
    start *= 10
  end
  number = start + (n - 1) / length
  digit_index = (n - 1) % length
  number.to_s[digit_index].ord - '0'.ord
end
```

## Scala

```scala
object Solution {
    def findNthDigit(n: Int): Int = {
        var remaining = n.toLong
        var length = 1L          // current digit length
        var count = 9L           // numbers with 'length' digits
        var start = 1L           // first number with 'length' digits

        while (remaining > length * count) {
            remaining -= length * count
            length += 1
            count *= 10
            start *= 10
        }

        val targetNumber = start + (remaining - 1) / length
        val digitIndex = ((remaining - 1) % length).toInt
        (targetNumber.toString.charAt(digitIndex) - '0')
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_nth_digit(n: i32) -> i32 {
        let mut n = n as i64;
        let mut length = 1i64;
        let mut count = 9i64;
        let mut start = 1i64;

        while n > length * count {
            n -= length * count;
            length += 1;
            count *= 10;
            start *= 10;
        }

        let num = start + (n - 1) / length;
        let digit_index = ((n - 1) % length) as usize;
        let s = num.to_string();
        (s.as_bytes()[digit_index] - b'0') as i32
    }
}
```

## Racket

```racket
(define/contract (find-nth-digit n)
  (-> exact-integer? exact-integer?)
  (let loop ((d 1) (remaining n))
    (define cnt (* 9 (expt 10 (- d 1)) d))
    (if (<= remaining cnt)
        (let* ((offset (quotient (- remaining 1) d))
               (digit-index (remainder (- remaining 1) d))
               (number (+ (expt 10 (- d 1)) offset))
               (s (number->string number)))
          (- (char->integer (string-ref s digit-index)) 48))
        (loop (+ d 1) (- remaining cnt)))))
```

## Erlang

```erlang
-spec find_nth_digit(N :: integer()) -> integer().
find_nth_digit(N) ->
    find_nth_digit(N, 1).

find_nth_digit(N, Digits) ->
    Count = 9 * pow10(Digits - 1),
    TotalDigits = Count * Digits,
    case N > TotalDigits of
        true ->
            find_nth_digit(N - TotalDigits, Digits + 1);
        false ->
            Offset = (N - 1) div Digits,
            DigitIndex = (N - 1) rem Digits,
            Number = pow10(Digits - 1) + Offset,
            Char = lists:nth(DigitIndex + 1, integer_to_list(Number)),
            Char - $0
    end.

pow10(0) -> 1;
pow10(N) ->
    trunc(math:pow(10, N)).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_nth_digit(n :: integer) :: integer
  def find_nth_digit(n) when is_integer(n) and n > 0 do
    locate_digit(n, 1, 9)
  end

  defp locate_digit(n, len, count) when n > len * count do
    locate_digit(n - len * count, len + 1, count * 10)
  end

  defp locate_digit(n, len, _count) do
    offset = div(n - 1, len)
    digit_index = rem(n - 1, len)

    start_number = trunc(:math.pow(10, len - 1))
    number = start_number + offset

    divisor = trunc(:math.pow(10, len - digit_index - 1))
    digit = div(number, divisor) |> rem(10)

    digit
  end
end
```
