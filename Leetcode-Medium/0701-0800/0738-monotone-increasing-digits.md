# 0738. Monotone Increasing Digits

## Cpp

```cpp
class Solution {
public:
    int monotoneIncreasingDigits(int n) {
        string s = to_string(n);
        int marker = s.size();
        for (int i = s.size() - 1; i > 0; --i) {
            if (s[i - 1] > s[i]) {
                s[i - 1]--;
                marker = i;
            }
        }
        for (int i = marker; i < (int)s.size(); ++i) {
            s[i] = '9';
        }
        return stoi(s);
    }
};
```

## Java

```java
class Solution {
    public int monotoneIncreasingDigits(int n) {
        char[] digits = Integer.toString(n).toCharArray();
        int len = digits.length;
        int marker = len; // first position to set to '9'
        for (int i = len - 1; i > 0; i--) {
            if (digits[i - 1] > digits[i]) {
                digits[i - 1]--;
                marker = i;
            }
        }
        for (int i = marker; i < len; i++) {
            digits[i] = '9';
        }
        return Integer.parseInt(new String(digits));
    }
}
```

## Python

```python
class Solution(object):
    def monotoneIncreasingDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = list(map(int, str(n)))
        marker = len(digits)
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] < digits[i - 1]:
                digits[i - 1] -= 1
                marker = i
        for i in range(marker, len(digits)):
            digits[i] = 9
        return int(''.join(map(str, digits)))
```

## Python3

```python
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = list(map(int, str(n)))
        marker = len(digits)
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] < digits[i - 1]:
                digits[i - 1] -= 1
                marker = i
        for i in range(marker, len(digits)):
            digits[i] = 9
        return int(''.join(map(str, digits)))
```

## C

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int monotoneIncreasingDigits(int n) {
    char s[12];
    sprintf(s, "%d", n);
    int len = strlen(s);
    int marker = len;
    for (int i = len - 1; i > 0; --i) {
        if (s[i - 1] > s[i]) {
            s[i - 1]--;
            marker = i;
        }
    }
    for (int i = marker; i < len; ++i) {
        s[i] = '9';
    }
    return atoi(s);
}
```

## Csharp

```csharp
public class Solution {
    public int MonotoneIncreasingDigits(int n) {
        char[] digits = n.ToString().ToCharArray();
        int marker = digits.Length;
        for (int i = digits.Length - 1; i > 0; --i) {
            if (digits[i - 1] > digits[i]) {
                digits[i - 1]--;
                marker = i;
            }
        }
        for (int i = marker; i < digits.Length; ++i) {
            digits[i] = '9';
        }
        return int.Parse(new string(digits));
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var monotoneIncreasingDigits = function(n) {
    const digits = n.toString().split('').map(Number);
    let marker = digits.length;
    for (let i = digits.length - 1; i > 0; i--) {
        if (digits[i - 1] > digits[i]) {
            digits[i - 1]--;
            marker = i;
        }
    }
    for (let i = marker; i < digits.length; i++) {
        digits[i] = 9;
    }
    return Number(digits.join(''));
};
```

## Typescript

```typescript
function monotoneIncreasingDigits(n: number): number {
    const digits = n.toString().split('').map(ch => Number(ch));
    for (let i = digits.length - 1; i > 0; i--) {
        if (digits[i - 1] > digits[i]) {
            digits[i - 1]--;
            for (let j = i; j < digits.length; j++) {
                digits[j] = 9;
            }
        }
    }
    return Number(digits.join(''));
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function monotoneIncreasingDigits($n) {
        $s = str_split((string)$n);
        $len = count($s);
        for ($i = $len - 2; $i >= 0; $i--) {
            if ($s[$i] > $s[$i + 1]) {
                $s[$i] = (string)((int)$s[$i] - 1);
                for ($j = $i + 1; $j < $len; $j++) {
                    $s[$j] = '9';
                }
            }
        }
        $resultStr = ltrim(implode('', $s), '0');
        return $resultStr === '' ? 0 : (int)$resultStr;
    }
}
```

## Swift

```swift
class Solution {
    func monotoneIncreasingDigits(_ n: Int) -> Int {
        if n < 10 { return n }
        var digits = Array(String(n)).map { Int(String($0))! }
        let len = digits.count
        var i = 1
        while i < len && digits[i] >= digits[i - 1] {
            i += 1
        }
        if i == len {
            return n
        }
        var mark = i - 1
        digits[mark] -= 1
        for k in (mark + 1)..<len {
            digits[k] = 9
        }
        while mark > 0 && digits[mark] < digits[mark - 1] {
            digits[mark] = 9
            mark -= 1
            digits[mark] -= 1
        }
        for k in (mark + 1)..<len {
            digits[k] = 9
        }
        var result = 0
        for d in digits {
            result = result * 10 + d
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun monotoneIncreasingDigits(n: Int): Int {
        val digits = n.toString().toCharArray()
        var marker = digits.size
        for (i in digits.lastIndex downTo 1) {
            if (digits[i - 1] > digits[i]) {
                digits[i - 1] = (digits[i - 1] - 1)
                marker = i
            }
        }
        for (i in marker until digits.size) {
            digits[i] = '9'
        }
        return String(digits).toInt()
    }
}
```

## Dart

```dart
class Solution {
  int monotoneIncreasingDigits(int n) {
    List<int> digits = n.toString().split('').map(int.parse).toList();
    int marker = digits.length;
    for (int i = digits.length - 1; i > 0; i--) {
      if (digits[i - 1] > digits[i]) {
        digits[i - 1]--;
        marker = i;
      }
    }
    for (int i = marker; i < digits.length; i++) {
      digits[i] = 9;
    }
    int result = 0;
    for (int d in digits) {
      result = result * 10 + d;
    }
    return result;
  }
}
```

## Golang

```go
import "strconv"

func monotoneIncreasingDigits(n int) int {
	s := strconv.Itoa(n)
	digits := make([]int, len(s))
	for i, ch := range s {
		digits[i] = int(ch - '0')
	}
	marker := len(digits)
	for i := len(digits) - 1; i > 0; i-- {
		if digits[i-1] > digits[i] {
			digits[i-1]--
			marker = i
		}
	}
	for i := marker; i < len(digits); i++ {
		digits[i] = 9
	}
	res := 0
	for _, d := range digits {
		res = res*10 + d
	}
	return res
}
```

## Ruby

```ruby
def monotone_increasing_digits(n)
  digits = n.to_s.chars.map(&:to_i)
  i = digits.length - 1
  while i > 0 && digits[i - 1] <= digits[i]
    i -= 1
  end
  return n if i == 0

  digits[i - 1] -= 1
  (i...digits.length).each { |j| digits[j] = 9 }

  i -= 1
  while i > 0 && digits[i - 1] > digits[i]
    digits[i - 1] -= 1
    digits[i] = 9
    i -= 1
  end

  ((i + 1)...digits.length).each { |j| digits[j] = 9 }
  digits.join.to_i
end
```

## Scala

```scala
object Solution {
    def monotoneIncreasingDigits(n: Int): Int = {
        val s = n.toString.toCharArray
        var i = 1
        while (i < s.length && s(i) >= s(i - 1)) {
            i += 1
        }
        if (i == s.length) return n

        var j = i - 1
        s(j) = ((s(j) - 1).toChar)
        while (j > 0 && s(j) < s(j - 1)) {
            s(j - 1) = ((s(j - 1) - 1).toChar)
            j -= 1
        }

        var k = j + 1
        while (k < s.length) {
            s(k) = '9'
            k += 1
        }
        new String(s).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn monotone_increasing_digits(n: i32) -> i32 {
        let mut digits: Vec<i32> = n
            .to_string()
            .chars()
            .map(|c| c.to_digit(10).unwrap() as i32)
            .collect();
        if digits.is_empty() {
            return 0;
        }
        for i in (0..digits.len() - 1).rev() {
            if digits[i] > digits[i + 1] {
                digits[i] -= 1;
                for j in i + 1..digits.len() {
                    digits[j] = 9;
                }
            }
        }
        let mut result: i32 = 0;
        for d in digits {
            result = result * 10 + d;
        }
        result
    }
}
```

## Racket

```racket
(define/contract (monotone-increasing-digits n)
  (-> exact-integer? exact-integer?)
  (if (< n 10)
      n
      (let* ([s (number->string n)]
             [len (string-length s)]
             [digits (list->vector
                      (for/list ([i (in-range len)])
                        (- (char->integer (string-ref s i))
                           (char->integer #\0))))])
        (let loop ((i (- len 1)))
          (when (> i 0)
            (when (> (vector-ref digits (- i 1)) (vector-ref digits i))
              (vector-set! digits (- i 1) (- (vector-ref digits (- i 1)) 1))
              (for ([j (in-range i len)])
                (vector-set! digits j 9)))
            (loop (- i 1))))
        (foldl (lambda (d acc) (+ (* acc 10) d)) 0
               (vector->list digits))))))
```

## Erlang

```erlang
-spec monotone_increasing_digits(N :: integer()) -> integer().
monotone_increasing_digits(N) ->
    case N of
        0 -> 0;
        _ ->
            Digits = [C - $0 || C <- integer_to_list(N)],
            Tuple0 = list_to_tuple(Digits),
            Len = tuple_size(Tuple0),
            FixedTuple = fix_loop(Tuple0, Len, Len),
            DigitsList = tuple_to_list(FixedTuple),
            Str = [D + $0 || D <- DigitsList],
            list_to_integer(Str)
    end.

fix_loop(Tuple, Len, I) when I =< 1 ->
    Tuple;
fix_loop(Tuple, Len, I) ->
    Prev = element(I - 1, Tuple),
    Curr = element(I, Tuple),
    if
        Prev > Curr ->
            NewPrev = Prev - 1,
            T1 = setelement(I - 1, Tuple, NewPrev),
            T2 = set_all_to_9(T1, I, Len),
            fix_loop(T2, Len, I - 1);
        true ->
            fix_loop(Tuple, Len, I - 1)
    end.

set_all_to_9(Tuple, Start, Max) when Start > Max ->
    Tuple;
set_all_to_9(Tuple, Start, Max) ->
    T1 = setelement(Start, Tuple, 9),
    set_all_to_9(T1, Start + 1, Max).
```

## Elixir

```elixir
defmodule Solution do
  @spec monotone_increasing_digits(n :: integer) :: integer
  def monotone_increasing_digits(n) do
    digits = Integer.digits(n)
    new_digits = fix(digits, length(digits) - 2)

    Enum.reduce(new_digits, 0, fn d, acc -> acc * 10 + d end)
  end

  defp fix(digits, i) when i < 0, do: digits

  defp fix(digits, i) do
    if Enum.at(digits, i) > Enum.at(digits, i + 1) do
      dec = Enum.at(digits, i) - 1
      digits = List.replace_at(digits, i, dec)
      digits = set_nines(digits, i + 1)
    end

    fix(digits, i - 1)
  end

  defp set_nines(digits, start_idx) do
    len = length(digits)

    Enum.reduce(start_idx..(len - 1), digits, fn idx, acc ->
      List.replace_at(acc, idx, 9)
    end)
  end
end
```
