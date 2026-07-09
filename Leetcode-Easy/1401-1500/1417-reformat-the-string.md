# 1417. Reformat The String

## Cpp

```cpp
class Solution {
public:
    string reformat(string s) {
        string letters, digits;
        for (char c : s) {
            if (isdigit(c)) digits.push_back(c);
            else letters.push_back(c);
        }
        int nL = letters.size(), nD = digits.size();
        if (abs(nL - nD) > 1) return "";
        string res;
        bool startWithLetter = nL >= nD;
        int i = 0, j = 0;
        while (i < nL || j < nD) {
            if (startWithLetter) {
                if (i < nL) res.push_back(letters[i++]);
                if (j < nD) res.push_back(digits[j++]);
            } else {
                if (j < nD) res.push_back(digits[j++]);
                if (i < nL) res.push_back(letters[i++]);
            }
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public String reformat(String s) {
        java.util.List<Character> letters = new java.util.ArrayList<>();
        java.util.List<Character> digits = new java.util.ArrayList<>();
        for (char c : s.toCharArray()) {
            if (Character.isLetter(c)) {
                letters.add(c);
            } else {
                digits.add(c);
            }
        }
        int l = letters.size(), d = digits.size();
        if (Math.abs(l - d) > 1) return "";
        StringBuilder sb = new StringBuilder(s.length());
        boolean startWithLetter = l >= d;
        int i = 0, j = 0;
        while (i < l || j < d) {
            if (startWithLetter) {
                if (i < l) sb.append(letters.get(i++));
                if (j < d) sb.append(digits.get(j++));
            } else {
                if (j < d) sb.append(digits.get(j++));
                if (i < l) sb.append(letters.get(i++));
            }
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        letters = []
        digits = []
        for ch in s:
            if ch.isalpha():
                letters.append(ch)
            else:
                digits.append(ch)
        if abs(len(letters) - len(digits)) > 1:
            return ""
        # Ensure we start with the group that has more elements
        if len(letters) < len(digits):
            letters, digits = digits, letters  # swap so letters is longer or equal
        res = []
        for i in range(len(s)):
            if i % 2 == 0:
                res.append(letters[i // 2])
            else:
                res.append(digits[i // 2])
        return "".join(res)
```

## Python3

```python
class Solution:
    def reformat(self, s: str) -> str:
        letters, digits = [], []
        for ch in s:
            (digits if ch.isdigit() else letters).append(ch)
        if abs(len(letters) - len(digits)) > 1:
            return ""
        # start with the longer list
        first, second = (letters, digits) if len(letters) >= len(digits) else (digits, letters)
        res = []
        for i in range(len(second)):
            res.append(first[i])
            res.append(second[i])
        if len(first) > len(second):
            res.append(first[-1])
        return "".join(res)
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char* reformat(char* s) {
    int n = strlen(s);
    char *letters = (char*)malloc(n + 1);
    char *digits  = (char*)malloc(n + 1);
    int l = 0, d = 0;
    
    for (int i = 0; i < n; ++i) {
        if (isalpha(s[i]))
            letters[l++] = s[i];
        else
            digits[d++] = s[i];
    }
    letters[l] = '\0';
    digits[d] = '\0';
    
    if (abs(l - d) > 1) {
        free(letters);
        free(digits);
        return "";
    }
    
    char *res = (char*)malloc(n + 1);
    int iL = 0, iD = 0, idx = 0;
    bool startLetter = l >= d; // if equal, start with letter
    
    while (iL < l || iD < d) {
        if (startLetter) {
            if (iL < l) res[idx++] = letters[iL++];
        } else {
            if (iD < d) res[idx++] = digits[iD++];
        }
        startLetter = !startLetter;
    }
    res[n] = '\0';
    
    free(letters);
    free(digits);
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string Reformat(string s)
    {
        var letters = new System.Collections.Generic.Queue<char>();
        var digits = new System.Collections.Generic.Queue<char>();

        foreach (char c in s)
        {
            if (char.IsLetter(c))
                letters.Enqueue(c);
            else
                digits.Enqueue(c);
        }

        int lCount = letters.Count;
        int dCount = digits.Count;

        if (System.Math.Abs(lCount - dCount) > 1)
            return string.Empty;

        var sb = new System.Text.StringBuilder();
        bool takeLetter = lCount >= dCount; // start with the larger group, or letters when equal

        while (letters.Count > 0 || digits.Count > 0)
        {
            if (takeLetter && letters.Count > 0)
                sb.Append(letters.Dequeue());
            else if (!takeLetter && digits.Count > 0)
                sb.Append(digits.Dequeue());

            takeLetter = !takeLetter;
        }

        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var reformat = function(s) {
    const letters = [];
    const digits = [];
    for (let i = 0; i < s.length; i++) {
        const ch = s[i];
        if (ch >= '0' && ch <= '9') {
            digits.push(ch);
        } else {
            letters.push(ch);
        }
    }
    if (Math.abs(letters.length - digits.length) > 1) return "";
    
    // start with the longer (or any when equal)
    const first = letters.length >= digits.length ? letters : digits;
    const second = first === letters ? digits : letters;
    
    let i = 0, j = 0;
    const res = [];
    while (i < first.length || j < second.length) {
        if (i < first.length) res.push(first[i++]);
        if (j < second.length) res.push(second[j++]);
    }
    return res.join('');
};
```

## Typescript

```typescript
function reformat(s: string): string {
    const letters: string[] = [];
    const digits: string[] = [];
    for (const ch of s) {
        if (ch >= '0' && ch <= '9') {
            digits.push(ch);
        } else {
            letters.push(ch);
        }
    }
    if (Math.abs(letters.length - digits.length) > 1) return "";
    const result: string[] = [];
    let i = 0, j = 0;
    const startWithLetter = letters.length >= digits.length;
    while (i < letters.length || j < digits.length) {
        if (startWithLetter) {
            if (i < letters.length) result.push(letters[i++]);
            if (j < digits.length) result.push(digits[j++]);
        } else {
            if (j < digits.length) result.push(digits[j++]);
            if (i < letters.length) result.push(letters[i++]);
        }
    }
    return result.join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function reformat($s) {
        $letters = [];
        $digits = [];

        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $ch = $s[$i];
            if (ctype_digit($ch)) {
                $digits[] = $ch;
            } else {
                $letters[] = $ch;
            }
        }

        $cntL = count($letters);
        $cntD = count($digits);

        if (abs($cntL - $cntD) > 1) {
            return "";
        }

        // decide which type starts first
        $startWithLetter = $cntL >= $cntD;

        $iL = 0;
        $iD = 0;
        $result = '';

        for ($i = 0; $i < $len; $i++) {
            if (($i % 2 == 0 && $startWithLetter) || ($i % 2 == 1 && !$startWithLetter)) {
                // take a letter
                $result .= $letters[$iL++];
            } else {
                // take a digit
                $result .= $digits[$iD++];
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func reformat(_ s: String) -> String {
        var letters = [Character]()
        var digits = [Character]()
        
        for ch in s {
            if ch.isNumber {
                digits.append(ch)
            } else {
                letters.append(ch)
            }
        }
        
        if abs(letters.count - digits.count) > 1 {
            return ""
        }
        
        var result = ""
        var i = 0, j = 0
        var takeLetterFirst = letters.count >= digits.count
        
        while i < letters.count || j < digits.count {
            if takeLetterFirst {
                if i < letters.count {
                    result.append(letters[i])
                    i += 1
                }
                takeLetterFirst = false
            } else {
                if j < digits.count {
                    result.append(digits[j])
                    j += 1
                }
                takeLetterFirst = true
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun reformat(s: String): String {
        val letters = mutableListOf<Char>()
        val digits = mutableListOf<Char>()
        for (c in s) {
            if (c.isDigit()) digits.add(c) else letters.add(c)
        }
        if (kotlin.math.abs(letters.size - digits.size) > 1) return ""
        val sb = StringBuilder()
        var i = 0
        var j = 0
        val startWithLetter = letters.size >= digits.size
        while (i < letters.size || j < digits.size) {
            if (startWithLetter) {
                if (i < letters.size) sb.append(letters[i++])
                if (j < digits.size) sb.append(digits[j++])
            } else {
                if (j < digits.size) sb.append(digits[j++])
                if (i < letters.size) sb.append(letters[i++])
            }
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String reformat(String s) {
    List<String> letters = [];
    List<String> digits = [];

    for (int i = 0; i < s.length; i++) {
      var ch = s[i];
      if (ch.codeUnitAt(0) >= 48 && ch.codeUnitAt(0) <= 57) {
        digits.add(ch);
      } else {
        letters.add(ch);
      }
    }

    if ((letters.length - digits.length).abs() > 1) return "";

    StringBuffer sb = StringBuffer();
    bool startWithLetter = letters.length >= digits.length;
    int i = 0, j = 0;

    while (i < letters.length || j < digits.length) {
      if (startWithLetter) {
        if (i < letters.length) sb.write(letters[i++]);
        if (j < digits.length) sb.write(digits[j++]);
      } else {
        if (j < digits.length) sb.write(digits[j++]);
        if (i < letters.length) sb.write(letters[i++]);
      }
    }

    return sb.toString();
  }
}
```

## Golang

```go
package main

import "strings"

func reformat(s string) string {
    letters := []byte{}
    digits := []byte{}
    for i := 0; i < len(s); i++ {
        c := s[i]
        if c >= 'a' && c <= 'z' {
            letters = append(letters, c)
        } else {
            digits = append(digits, c)
        }
    }
    if abs(len(letters)-len(digits)) > 1 {
        return ""
    }

    var first, second []byte
    if len(letters) >= len(digits) {
        first = letters
        second = digits
    } else {
        first = digits
        second = letters
    }

    var b strings.Builder
    b.Grow(len(s))
    i, j := 0, 0
    for k := 0; k < len(s); k++ {
        if k%2 == 0 {
            b.WriteByte(first[i])
            i++
        } else {
            b.WriteByte(second[j])
            j++
        }
    }
    return b.String()
}

func abs(a int) int {
    if a < 0 {
        return -a
    }
    return a
}
```

## Ruby

```ruby
def reformat(s)
  letters = []
  digits = []
  s.each_char do |ch|
    if ch =~ /[a-z]/
      letters << ch
    else
      digits << ch
    end
  end

  return "" if (letters.size - digits.size).abs > 1

  res = +""
  i = j = 0
  turn_letter = letters.size >= digits.size

  while i < letters.size || j < digits.size
    if turn_letter
      if i < letters.size
        res << letters[i]
        i += 1
      end
    else
      if j < digits.size
        res << digits[j]
        j += 1
      end
    end
    turn_letter = !turn_letter
  end

  res
end
```

## Scala

```scala
object Solution {
    def reformat(s: String): String = {
        val letters = scala.collection.mutable.ArrayBuffer[Char]()
        val digits = scala.collection.mutable.ArrayBuffer[Char]()
        for (c <- s) {
            if (c.isLetter) letters += c else digits += c
        }
        if (math.abs(letters.length - digits.length) > 1) return ""
        val sb = new StringBuilder()
        var i = 0
        var j = 0
        var turnLetter = letters.length >= digits.length
        while (i < letters.length || j < digits.length) {
            if (turnLetter && i < letters.length) {
                sb.append(letters(i))
                i += 1
            } else if (!turnLetter && j < digits.length) {
                sb.append(digits(j))
                j += 1
            }
            turnLetter = !turnLetter
        }
        sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn reformat(s: String) -> String {
        let mut letters = Vec::new();
        let mut digits = Vec::new();

        for ch in s.chars() {
            if ch.is_ascii_digit() {
                digits.push(ch);
            } else {
                letters.push(ch);
            }
        }

        if (letters.len() as i32 - digits.len() as i32).abs() > 1 {
            return String::new();
        }

        let mut result = String::with_capacity(s.len());

        if letters.len() >= digits.len() {
            for i in 0..letters.len().max(digits.len()) {
                if i < letters.len() {
                    result.push(letters[i]);
                }
                if i < digits.len() {
                    result.push(digits[i]);
                }
            }
        } else {
            for i in 0..letters.len().max(digits.len()) {
                if i < digits.len() {
                    result.push(digits[i]);
                }
                if i < letters.len() {
                    result.push(letters[i]);
                }
            }
        }

        result
    }
}
```

## Racket

```racket
(define/contract (reformat s)
  (-> string? string?)
  (let* ((chars (string->list s))
         (letters '())
         (digits '()))
    (for ([c chars])
      (if (char-alphabetic? c)
          (set! letters (cons c letters))
          (set! digits (cons c digits))))
    (set! letters (reverse letters))
    (set! digits (reverse digits))
    (define lenL (length letters))
    (define lenD (length digits))
    (if (> (abs (- lenL lenD)) 1)
        ""
        (let* ((start-with-letter? (>= lenL lenD))
               (longer (if start-with-letter? letters digits))
               (shorter (if start-with-letter? digits letters)))
          (let loop ((ls longer) (ss shorter) (acc '()))
            (if (null? ls)
                (list->string (reverse acc))
                (let ((new-acc (cons (car ls)
                                     (if (null? ss) acc (cons (car ss) acc)))))
                  (loop (cdr ls)
                        (if (null? ss) '() (cdr ss))
                        new-acc))))))))
```

## Erlang

```erlang
-module(solution).
-export([reformat/1]).

-spec reformat(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
reformat(S) when is_binary(S) ->
    Chars = binary_to_list(S),
    Letters = [C || C <- Chars, $a =< C, C =< $z],
    Digits  = [C || C <- Chars, $0 =< C, C =< $9],
    LenL = length(Letters),
    LenD = length(Digits),
    case abs(LenL - LenD) > 1 of
        true -> <<>>;
        false ->
            StartWithLetter = LenL >= LenD,
            ResultList = merge(Letters, Digits, StartWithLetter, []),
            list_to_binary(ResultList)
    end.

merge([], [], _, Acc) ->
    lists:reverse(Acc);
merge([L|Lt], Ds, true, Acc) ->
    merge(Lt, Ds, false, [L|Acc]);
merge(Ls, [D|Dt], false, Acc) ->
    merge(Ls, Dt, true, [D|Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec reformat(s :: String.t()) :: String.t()
  def reformat(s) do
    chars = String.graphemes(s)

    {letters_rev, digits_rev} =
      Enum.reduce(chars, {[], []}, fn ch, {ls, ds} ->
        if ch >= "0" and ch <= "9" do
          {ls, [ch | ds]}
        else
          {[ch | ls], ds}
        end
      end)

    letters = Enum.reverse(letters_rev)
    digits = Enum.reverse(digits_rev)

    len_l = length(letters)
    len_d = length(digits)

    if abs(len_l - len_d) > 1 do
      ""
    else
      result =
        cond do
          len_l >= len_d ->
            Enum.map(0..(len_l + len_d - 1), fn idx ->
              if rem(idx, 2) == 0 do
                Enum.at(letters, div(idx, 2))
              else
                Enum.at(digits, div(idx, 2))
              end
            end)

          true ->
            Enum.map(0..(len_l + len_d - 1), fn idx ->
              if rem(idx, 2) == 0 do
                Enum.at(digits, div(idx, 2))
              else
                Enum.at(letters, div(idx, 2))
              end
            end)
        end

      Enum.join(result)
    end
  end
end
```
