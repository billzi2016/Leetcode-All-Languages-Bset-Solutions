# 2566. Maximum Difference by Remapping a Digit

## Cpp

```cpp
class Solution {
public:
    int minMaxDifference(int num) {
        string s = to_string(num);
        
        // Compute maximum value
        string max_s = s;
        char replace_max = 0;
        for (char c : s) {
            if (c != '9') { replace_max = c; break; }
        }
        if (replace_max) {
            for (char &c : max_s) {
                if (c == replace_max) c = '9';
            }
        }
        
        // Compute minimum value
        string min_s = s;
        char replace_min = s[0]; // leading digit, never '0' per constraints
        if (replace_min != '0') {
            for (char &c : min_s) {
                if (c == replace_min) c = '0';
            }
        }
        
        long long max_val = stoll(max_s);
        long long min_val = stoll(min_s);
        return static_cast<int>(max_val - min_val);
    }
};
```

## Java

```java
class Solution {
    public int minMaxDifference(int num) {
        String s = Integer.toString(num);
        int maxVal = getMax(s);
        int minVal = getMin(s);
        return maxVal - minVal;
    }

    private int getMax(String s) {
        char replaceChar = 0;
        for (char c : s.toCharArray()) {
            if (c != '9') {
                replaceChar = c;
                break;
            }
        }
        if (replaceChar == 0) {
            return Integer.parseInt(s);
        }
        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray()) {
            sb.append(c == replaceChar ? '9' : c);
        }
        return Integer.parseInt(sb.toString());
    }

    private int getMin(String s) {
        char replaceChar = 0;
        for (char c : s.toCharArray()) {
            if (c != '0') {
                replaceChar = c;
                break;
            }
        }
        // replaceChar will always be set because num >= 1, so first digit is non-zero
        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray()) {
            sb.append(c == replaceChar ? '0' : c);
        }
        return Integer.parseInt(sb.toString());
    }
}
```

## Python

```python
class Solution(object):
    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)

        # maximum value
        max_digit = None
        for ch in s:
            if ch != '9':
                max_digit = ch
                break
        if max_digit is not None:
            max_val = int(''.join('9' if c == max_digit else c for c in s))
        else:
            max_val = num

        # minimum value
        min_digit = None
        for ch in s:
            if ch != '0':
                min_digit = ch
                break
        if min_digit is not None:
            min_val = int(''.join('0' if c == min_digit else c for c in s))
        else:
            min_val = num

        return max_val - min_val
```

## Python3

```python
class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)

        # maximum value
        max_val = None
        for ch in s:
            if ch != '9':
                max_val = int(s.replace(ch, '9'))
                break
        if max_val is None:
            max_val = num

        # minimum value
        min_val = None
        for ch in s:
            if ch != '0':
                min_val = int(s.replace(ch, '0'))
                break
        if min_val is None:
            min_val = num

        return max_val - min_val
```

## C

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int minMaxDifference(int num) {
    char s[12];
    sprintf(s, "%d", num);

    // Compute maximum value
    char max_s[12];
    strcpy(max_s, s);
    char replace_max = 0;
    for (int i = 0; max_s[i]; ++i) {
        if (max_s[i] != '9') {
            replace_max = max_s[i];
            break;
        }
    }
    if (replace_max) {
        for (int i = 0; max_s[i]; ++i) {
            if (max_s[i] == replace_max) max_s[i] = '9';
        }
    }
    int max_val = atoi(max_s);

    // Compute minimum value
    char min_s[12];
    strcpy(min_s, s);
    char replace_min = 0;
    for (int i = 0; min_s[i]; ++i) {
        if (min_s[i] != '0') {
            replace_min = min_s[i];
            break;
        }
    }
    if (replace_min) {
        for (int i = 0; min_s[i]; ++i) {
            if (min_s[i] == replace_min) min_s[i] = '0';
        }
    }
    int min_val = atoi(min_s);

    return max_val - min_val;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int MinMaxDifference(int num) {
        string s = num.ToString();
        // Compute maximum value
        char[] maxArr = s.ToCharArray();
        char targetMax = '\0';
        foreach (char c in maxArr) {
            if (c != '9') {
                targetMax = c;
                break;
            }
        }
        int maxVal;
        if (targetMax == '\0') {
            maxVal = num;
        } else {
            for (int i = 0; i < maxArr.Length; i++) {
                if (maxArr[i] == targetMax) maxArr[i] = '9';
            }
            maxVal = int.Parse(new string(maxArr));
        }

        // Compute minimum value
        char[] minArr = s.ToCharArray();
        char firstDigit = minArr[0];
        for (int i = 0; i < minArr.Length; i++) {
            if (minArr[i] == firstDigit) minArr[i] = '0';
        }
        int minVal = int.Parse(new string(minArr));

        return maxVal - minVal;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} num
 * @return {number}
 */
var minMaxDifference = function(num) {
    const s = String(num);
    
    // Compute maximum value
    let maxStr = s;
    for (let i = 0; i < s.length; i++) {
        if (s[i] !== '9') {
            const target = s[i];
            maxStr = [...s].map(ch => ch === target ? '9' : ch).join('');
            break;
        }
    }
    
    // Compute minimum value
    let minStr = s;
    for (let i = 0; i < s.length; i++) {
        if (s[i] !== '0') {
            const target = s[i];
            minStr = [...s].map(ch => ch === target ? '0' : ch).join('');
            break;
        }
    }
    
    const maxVal = Number(maxStr);
    const minVal = Number(minStr);
    return maxVal - minVal;
};
```

## Typescript

```typescript
function minMaxDifference(num: number): number {
    const s = num.toString();

    // Compute maximum value
    let maxStr = s;
    for (let i = 0; i < s.length; i++) {
        if (s[i] !== '9') {
            const target = s[i];
            let builder = '';
            for (const ch of s) {
                builder += ch === target ? '9' : ch;
            }
            maxStr = builder;
            break;
        }
    }

    // Compute minimum value
    let minStr = s;
    for (let i = 0; i < s.length; i++) {
        if (s[i] !== '0') {
            const target = s[i];
            let builder = '';
            for (const ch of s) {
                builder += ch === target ? '0' : ch;
            }
            minStr = builder;
            break;
        }
    }

    const maxNum = Number(maxStr);
    const minNum = Number(minStr);
    return maxNum - minNum;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $num
     * @return Integer
     */
    function minMaxDifference($num) {
        $s = strval($num);
        $len = strlen($s);

        // Compute maximum value
        $maxStr = $s;
        for ($i = 0; $i < $len; $i++) {
            if ($s[$i] !== '9') {
                $target = $s[$i];
                $maxStr = str_replace($target, '9', $s);
                break;
            }
        }

        // Compute minimum value
        $minStr = $s;
        for ($i = 0; $i < $len; $i++) {
            if ($s[$i] !== '0') {
                $target = $s[$i];
                $minStr = str_replace($target, '0', $s);
                // Remove leading zeros
                $minStr = ltrim($minStr, '0');
                if ($minStr === '') {
                    $minStr = '0';
                }
                break;
            }
        }

        $maxVal = intval($maxStr);
        $minVal = intval($minStr);
        return $maxVal - $minVal;
    }
}
```

## Swift

```swift
class Solution {
    func minMaxDifference(_ num: Int) -> Int {
        let s = String(num)
        
        // Compute maximum value
        var maxChars = Array(s)
        var replaceForMax: Character? = nil
        for ch in maxChars where ch != "9" {
            replaceForMax = ch
            break
        }
        if let target = replaceForMax {
            for i in 0..<maxChars.count {
                if maxChars[i] == target {
                    maxChars[i] = "9"
                }
            }
        }
        let maxVal = Int(String(maxChars))!
        
        // Compute minimum value
        var minChars = Array(s)
        var replaceForMin: Character? = nil
        for ch in minChars where ch != "0" {
            replaceForMin = ch
            break
        }
        if let target = replaceForMin {
            for i in 0..<minChars.count {
                if minChars[i] == target {
                    minChars[i] = "0"
                }
            }
        }
        let minVal = Int(String(minChars))!
        
        return maxVal - minVal
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minMaxDifference(num: Int): Int {
        val s = num.toString()
        var maxStr = s
        for (c in s) {
            if (c != '9') {
                maxStr = s.replace(c, '9')
                break
            }
        }
        var minStr = s
        for (c in s) {
            if (c != '0') {
                minStr = s.replace(c, '0')
                break
            }
        }
        val maxVal = maxStr.toInt()
        val minVal = minStr.toInt()
        return maxVal - minVal
    }
}
```

## Dart

```dart
class Solution {
  int minMaxDifference(int num) {
    String s = num.toString();

    // Compute maximum value
    String maxStr = s;
    for (int i = 0; i < s.length; i++) {
      if (s[i] != '9') {
        maxStr = s.replaceAll(s[i], '9');
        break;
      }
    }

    // Compute minimum value
    String minStr = s;
    for (int i = 0; i < s.length; i++) {
      if (s[i] != '0') {
        minStr = s.replaceAll(s[i], '0');
        break;
      }
    }

    int maxVal = int.parse(maxStr);
    int minVal = int.parse(minStr);
    return maxVal - minVal;
  }
}
```

## Golang

```go
func minMaxDifference(num int) int {
    s := strconv.Itoa(num)

    // Compute maximum value
    maxStr := s
    for i := 0; i < len(s); i++ {
        if s[i] != '9' {
            target := s[i]
            b := []byte(s)
            for j := 0; j < len(b); j++ {
                if b[j] == target {
                    b[j] = '9'
                }
            }
            maxStr = string(b)
            break
        }
    }

    // Compute minimum value
    minStr := s
    first := s[0]
    b2 := []byte(s)
    for j := 0; j < len(b2); j++ {
        if b2[j] == first {
            b2[j] = '0'
        }
    }
    minStr = string(b2)

    maxVal, _ := strconv.Atoi(maxStr)
    minVal, _ := strconv.Atoi(minStr)

    return maxVal - minVal
}
```

## Ruby

```ruby
def min_max_difference(num)
  s = num.to_s

  # Compute maximum value
  first_non_nine = nil
  s.each_char do |ch|
    if ch != '9'
      first_non_nine = ch
      break
    end
  end
  max_val = if first_non_nine
    s.tr(first_non_nine, '9').to_i
  else
    num
  end

  # Compute minimum value
  first_char = s[0]
  min_val = s.tr(first_char, '0').to_i

  max_val - min_val
end
```

## Scala

```scala
object Solution {
  def minMaxDifference(num: Int): Int = {
    val s = num.toString

    // Compute maximum value
    var maxStr = s
    var idx = 0
    while (idx < s.length && s(idx) == '9') idx += 1
    if (idx < s.length) {
      val target = s(idx)
      maxStr = s.map(ch => if (ch == target) '9' else ch)
    }

    // Compute minimum value
    var minStr = s
    idx = 0
    while (idx < s.length && s(idx) == '0') idx += 1
    if (idx < s.length) {
      val target = s(idx)
      minStr = s.map(ch => if (ch == target) '0' else ch)
    }

    maxStr.toInt - minStr.toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn min_max_difference(num: i32) -> i32 {
        let s = num.to_string();
        let chars: Vec<char> = s.chars().collect();

        // maximum value
        let mut max_target: Option<char> = None;
        for &c in &chars {
            if c != '9' {
                max_target = Some(c);
                break;
            }
        }
        let max_val: i32 = if let Some(t) = max_target {
            s.chars()
                .map(|ch| if ch == t { '9' } else { ch })
                .collect::<String>()
                .parse()
                .unwrap()
        } else {
            num
        };

        // minimum value
        let mut min_target: Option<char> = None;
        for &c in &chars {
            if c != '0' {
                min_target = Some(c);
                break;
            }
        }
        let min_val: i32 = if let Some(t) = min_target {
            s.chars()
                .map(|ch| if ch == t { '0' } else { ch })
                .collect::<String>()
                .parse()
                .unwrap()
        } else {
            num
        };

        max_val - min_val
    }
}
```

## Racket

```racket
(define/contract (min-max-difference num)
  (-> exact-integer? exact-integer?)
  (let* ((s (number->string num))
         ;; helper to replace all occurrences of a character
         (replace-all
          (lambda (str old new)
            (list->string
             (map (lambda (ch) (if (char=? ch old) new ch))
                  (string->list str)))))
         ;; first character in str that is not equal to given char, or #f if none
         (first-non-char
          (lambda (str ch)
            (let loop ((lst (string->list str)))
              (cond [(null? lst) #f]
                    [(not (char=? (car lst) ch)) (car lst)]
                    [else (loop (cdr lst))]))))
         ;; maximum value
         (max-char (first-non-char s #\9))
         (max-str (if max-char
                      (replace-all s max-char #\9)
                      s))
         ;; minimum value: replace the first digit (non‑zero) with '0'
         (first-digit (string-ref s 0))
         (min-str (replace-all s first-digit #\0))
         (max-num (string->number max-str))
         (min-num (string->number min-str)))
    (- max-num min-num)))
```

## Erlang

```erlang
-spec min_max_difference(integer()) -> integer().
min_max_difference(Num) ->
    Digits = integer_to_list(Num),
    MaxDigits = case find_first_not(Digits, $9) of
        undefined -> Digits;
        C -> replace_all(Digits, C, $9)
    end,
    MinDigits = case find_first_not(Digits, $0) of
        undefined -> Digits;
        D -> replace_all(Digits, D, $0)
    end,
    MaxNum = list_to_integer(MaxDigits),
    MinNum = list_to_integer(MinDigits),
    MaxNum - MinNum.

find_first_not([H|_], Target) when H =/= Target ->
    H;
find_first_not([_|T], Target) ->
    find_first_not(T, Target);
find_first_not([], _) ->
    undefined.

replace_all(List, From, To) ->
    [if X == From -> To; true -> X end || X <- List].
```

## Elixir

```elixir
defmodule Solution do
  @spec min_max_difference(num :: integer) :: integer
  def min_max_difference(num) do
    s = Integer.to_string(num)

    max_s =
      case Enum.find(String.graphemes(s), fn c -> c != "9" end) do
        nil -> s
        d -> String.replace(s, d, "9")
      end

    min_s =
      case Enum.find(String.graphemes(s), fn c -> c != "0" end) do
        nil -> s
        d -> String.replace(s, d, "0")
      end

    max = String.to_integer(max_s)
    min = String.to_integer(min_s)

    max - min
  end
end
```
