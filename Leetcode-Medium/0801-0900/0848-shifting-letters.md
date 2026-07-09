# 0848. Shifting Letters

## Cpp

```cpp
class Solution {
public:
    string shiftingLetters(string s, vector<int>& shifts) {
        int n = s.size();
        long long cum = 0;
        for (int i = n - 1; i >= 0; --i) {
            cum += shifts[i];
            int shift = cum % 26;
            s[i] = char('a' + (s[i] - 'a' + shift) % 26);
        }
        return s;
    }
};
```

## Java

```java
class Solution {
    public String shiftingLetters(String s, int[] shifts) {
        char[] chars = s.toCharArray();
        long totalShift = 0;
        for (int i = chars.length - 1; i >= 0; i--) {
            totalShift = (totalShift + shifts[i]) % 26;
            int originalPos = chars[i] - 'a';
            int newPos = (originalPos + (int) totalShift) % 26;
            chars[i] = (char) ('a' + newPos);
        }
        return new String(chars);
    }
}
```

## Python

```python
class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        total = 0
        res = list(s)
        for i in range(len(s) - 1, -1, -1):
            total = (total + shifts[i]) % 26
            orig = ord(s[i]) - ord('a')
            res[i] = chr((orig + total) % 26 + ord('a'))
        return ''.join(res)
```

## Python3

```python
class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        n = len(s)
        res = [''] * n
        total = 0
        for i in range(n - 1, -1, -1):
            total = (total + shifts[i]) % 26
            orig = ord(s[i]) - ord('a')
            new_char = chr((orig + total) % 26 + ord('a'))
            res[i] = new_char
        return ''.join(res)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* shiftingLetters(char* s, int* shifts, int shiftsSize) {
    int n = strlen(s);
    char *res = (char*)malloc(n + 1);
    long long total = 0;
    for (int i = n - 1; i >= 0; --i) {
        total = (total + shifts[i]) % 26;
        int orig = s[i] - 'a';
        int newc = (orig + total) % 26;
        res[i] = (char)('a' + newc);
    }
    res[n] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string ShiftingLetters(string s, int[] shifts) {
        char[] chars = s.ToCharArray();
        long cumulative = 0;
        for (int i = shifts.Length - 1; i >= 0; i--) {
            cumulative = (cumulative + shifts[i]) % 26;
            int original = chars[i] - 'a';
            int shifted = (int)((original + cumulative) % 26);
            chars[i] = (char)('a' + shifted);
        }
        return new string(chars);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number[]} shifts
 * @return {string}
 */
var shiftingLetters = function(s, shifts) {
    const n = s.length;
    const result = new Array(n);
    let cumulativeShift = 0;
    for (let i = n - 1; i >= 0; --i) {
        cumulativeShift = (cumulativeShift + shifts[i]) % 26;
        const originalCode = s.charCodeAt(i) - 97;
        const shiftedCode = (originalCode + cumulativeShift) % 26;
        result[i] = String.fromCharCode(shiftedCode + 97);
    }
    return result.join('');
};
```

## Typescript

```typescript
function shiftingLetters(s: string, shifts: number[]): string {
    const n = s.length;
    const result: string[] = new Array(n);
    let totalShift = 0;
    for (let i = n - 1; i >= 0; --i) {
        totalShift = (totalShift + shifts[i]) % 26;
        const originalCode = s.charCodeAt(i) - 97;
        const shiftedCode = (originalCode + totalShift) % 26;
        result[i] = String.fromCharCode(shiftedCode + 97);
    }
    return result.join('');
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @param Integer[] $shifts
     * @return String
     */
    function shiftingLetters($s, $shifts) {
        $n = strlen($s);
        $result = str_split($s);
        $total = 0;
        for ($i = $n - 1; $i >= 0; $i--) {
            $total = ($total + $shifts[$i]) % 26;
            $orig = ord($s[$i]) - 97;
            $result[$i] = chr(($orig + $total) % 26 + 97);
        }
        return implode('', $result);
    }
}
```

## Swift

```swift
class Solution {
    func shiftingLetters(_ s: String, _ shifts: [Int]) -> String {
        var chars = Array(s)
        let aScalar = UnicodeScalar("a").value
        var total = 0
        for i in stride(from: chars.count - 1, through: 0, by: -1) {
            total = (total + shifts[i]) % 26
            let origVal = Int(chars[i].unicodeScalars.first!.value - aScalar)
            let newVal = (origVal + total) % 26
            chars[i] = Character(UnicodeScalar(aScalar + UInt32(newVal))!)
        }
        return String(chars)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun shiftingLetters(s: String, shifts: IntArray): String {
        val n = s.length
        val result = CharArray(n)
        var totalShift = 0L
        for (i in n - 1 downTo 0) {
            totalShift = (totalShift + shifts[i]) % 26L
            val original = s[i].code - 'a'.code
            val shifted = ((original + totalShift) % 26).toInt()
            result[i] = ('a'.code + shifted).toChar()
        }
        return String(result)
    }
}
```

## Dart

```dart
class Solution {
  String shiftingLetters(String s, List<int> shifts) {
    int n = s.length;
    List<int> result = List.filled(n, 0);
    int totalShift = 0;
    const int aCode = 97; // 'a'.codeUnitAt(0)
    for (int i = n - 1; i >= 0; i--) {
      totalShift = (totalShift + shifts[i]) % 26;
      int original = s.codeUnitAt(i) - aCode;
      int shifted = (original + totalShift) % 26;
      result[i] = shifted + aCode;
    }
    return String.fromCharCodes(result);
  }
}
```

## Golang

```go
func shiftingLetters(s string, shifts []int) string {
	n := len(s)
	res := make([]byte, n)
	total := 0
	for i := n - 1; i >= 0; i-- {
		total = (total + shifts[i]) % 26
		orig := int(s[i] - 'a')
		newc := (orig + total) % 26
		res[i] = byte(newc) + 'a'
	}
	return string(res)
}
```

## Ruby

```ruby
def shifting_letters(s, shifts)
  n = s.length
  total = 0
  result = Array.new(n)
  (n - 1).downto(0) do |i|
    total = (total + shifts[i]) % 26
    orig = s.getbyte(i) - 97
    result[i] = ((orig + total) % 26 + 97).chr
  end
  result.join
end
```

## Scala

```scala
object Solution {
    def shiftingLetters(s: String, shifts: Array[Int]): String = {
        val n = s.length
        val result = new Array[Char](n)
        var totalShift = 0L
        var i = n - 1
        while (i >= 0) {
            totalShift = (totalShift + shifts(i).toLong) % 26
            val original = s.charAt(i) - 'a'
            val shifted = ((original + totalShift) % 26).toInt
            result(i) = (shifted + 'a').toChar
            i -= 1
        }
        new String(result)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn shifting_letters(s: String, shifts: Vec<i32>) -> String {
        let mut bytes = s.into_bytes();
        let n = bytes.len();
        let mut total: i64 = 0;
        for i in (0..n).rev() {
            total += shifts[i] as i64;
            total %= 26;
            let shift = total as u8;
            let c = bytes[i];
            bytes[i] = ((c - b'a') + shift) % 26 + b'a';
        }
        // SAFETY: we only produce lowercase ASCII letters, which are valid UTF-8.
        unsafe { String::from_utf8_unchecked(bytes) }
    }
}
```

## Racket

```racket
(define/contract (shifting-letters s shifts)
  (-> string? (listof exact-integer?) string?)
  (let* ((n (string-length s))
         (shift-vec (list->vector shifts)))
    (let loop ((i (- n 1)) (cum 0) (acc '()))
      (if (< i 0)
          (list->string (reverse acc))
          (let* ((cum (+ cum (vector-ref shift-vec i)))
                 (total (modulo cum 26))
                 (orig (char->integer (string-ref s i)))
                 (a-code (char->integer #\a))
                 (new-char (integer->char
                            (+ a-code
                               (modulo (+ (- orig a-code) total) 26)))))
            (loop (- i 1) cum (cons new-char acc)))))))
```

## Erlang

```erlang
-spec shifting_letters(S :: unicode:unicode_binary(), Shifts :: [integer()]) -> unicode:unicode_binary().
shifting_letters(S, Shifts) ->
    CharList = binary:bin_to_list(S),
    RevChars = lists:reverse(CharList),
    RevShifts = lists:reverse(Shifts),
    {_, RevResult} = lists:foldl(
        fun({C, Shift}, {AccShift, AccRes}) ->
            NewShift = (AccShift + Shift) rem 26,
            NewChar = ((C - $a + NewShift) rem 26) + $a,
            {NewShift, [NewChar | AccRes]}
        end,
        {0, []},
        lists:zip(RevChars, RevShifts)
    ),
    ResultList = lists:reverse(RevResult),
    list_to_binary(ResultList).
```

## Elixir

```elixir
defmodule Solution do
  @spec shifting_letters(s :: String.t(), shifts :: [integer]) :: String.t()
  def shifting_letters(s, shifts) do
    chars = String.to_charlist(s)
    rev_chars = Enum.reverse(chars)
    rev_shifts = Enum.reverse(shifts)

    {_total, result} =
      Enum.reduce(Enum.zip(rev_shifts, rev_chars), {0, []}, fn {shift, ch}, {total, acc} ->
        total = rem(total + shift, 26)
        new_c = ?a + rem(ch - ?a + total, 26)
        {total, [new_c | acc]}
      end)

    List.to_string(result)
  end
end
```
