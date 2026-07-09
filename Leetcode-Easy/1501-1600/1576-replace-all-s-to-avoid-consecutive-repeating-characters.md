# 1576. Replace All ?'s to Avoid Consecutive Repeating Characters

## Cpp

```cpp
class Solution {
public:
    string modifyString(string s) {
        int n = s.size();
        for (int i = 0; i < n; ++i) {
            if (s[i] == '?') {
                for (char c = 'a'; c <= 'z'; ++c) {
                    bool left_ok = (i == 0) || (s[i-1] != c);
                    bool right_ok = (i == n - 1) || (s[i+1] == '?' ) || (s[i+1] != c);
                    if (left_ok && right_ok) {
                        s[i] = c;
                        break;
                    }
                }
            }
        }
        return s;
    }
};
```

## Java

```java
class Solution {
    public String modifyString(String s) {
        char[] chars = s.toCharArray();
        int n = chars.length;
        for (int i = 0; i < n; i++) {
            if (chars[i] == '?') {
                for (char c = 'a'; c <= 'c'; c++) {
                    boolean leftOk = i == 0 || chars[i - 1] != c;
                    boolean rightOk = i == n - 1 || s.charAt(i + 1) == '?' || s.charAt(i + 1) != c;
                    if (leftOk && rightOk) {
                        chars[i] = c;
                        break;
                    }
                }
            }
        }
        return new String(chars);
    }
}
```

## Python

```python
class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        res = list(s)
        for i in range(n):
            if res[i] == '?':
                left = res[i-1] if i > 0 else None
                right = s[i+1] if i + 1 < n and s[i+1] != '?' else None
                for c in ('a', 'b', 'c'):
                    if c != left and c != right:
                        res[i] = c
                        break
        return ''.join(res)
```

## Python3

```python
class Solution:
    def modifyString(self, s: str) -> str:
        chars = list(s)
        n = len(chars)
        for i in range(n):
            if chars[i] == '?':
                left = chars[i - 1] if i > 0 else ''
                right = chars[i + 1] if i + 1 < n else ''
                for c in 'abc':
                    if c != left and c != right:
                        chars[i] = c
                        break
        return ''.join(chars)
```

## C

```c
#include <string.h>

char* modifyString(char* s) {
    int n = strlen(s);
    for (int i = 0; i < n; ++i) {
        if (s[i] == '?') {
            char left = (i > 0) ? s[i - 1] : '#';
            char right = (i + 1 < n && s[i + 1] != '?') ? s[i + 1] : '#';
            for (char ch = 'a'; ch <= 'z'; ++ch) {
                if (ch != left && ch != right) {
                    s[i] = ch;
                    break;
                }
            }
        }
    }
    return s;
}
```

## Csharp

```csharp
public class Solution {
    public string ModifyString(string s) {
        char[] arr = s.ToCharArray();
        int n = arr.Length;
        for (int i = 0; i < n; i++) {
            if (arr[i] == '?') {
                for (char c = 'a'; c <= 'c'; c++) {
                    bool leftOk = i == 0 || arr[i - 1] != c;
                    bool rightOk = i == n - 1 || (arr[i + 1] != '?' && arr[i + 1] != c);
                    if (leftOk && rightOk) {
                        arr[i] = c;
                        break;
                    }
                }
            }
        }
        return new string(arr);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var modifyString = function(s) {
    const n = s.length;
    const arr = s.split('');
    const letters = ['a', 'b', 'c'];
    for (let i = 0; i < n; i++) {
        if (arr[i] === '?') {
            const left = i > 0 ? arr[i - 1] : null;
            // look ahead to the original next character if it's not a '?'
            const right = (i + 1 < n && s[i + 1] !== '?') ? s[i + 1] : null;
            for (const ch of letters) {
                if (ch !== left && ch !== right) {
                    arr[i] = ch;
                    break;
                }
            }
        }
    }
    return arr.join('');
};
```

## Typescript

```typescript
function modifyString(s: string): string {
    const chars = s.split('');
    const n = chars.length;
    for (let i = 0; i < n; i++) {
        if (chars[i] === '?') {
            for (let c = 97; c <= 122; c++) { // 'a' to 'z'
                const ch = String.fromCharCode(c);
                const leftOk = i === 0 || chars[i - 1] !== ch;
                const rightOk = i === n - 1 || chars[i + 1] === '?' || chars[i + 1] !== ch;
                if (leftOk && rightOk) {
                    chars[i] = ch;
                    break;
                }
            }
        }
    }
    return chars.join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function modifyString($s) {
        $n = strlen($s);
        $chars = str_split($s);
        for ($i = 0; $i < $n; $i++) {
            if ($chars[$i] === '?') {
                $left = $i > 0 ? $chars[$i - 1] : '';
                $right = $i + 1 < $n ? $chars[$i + 1] : '';
                for ($c = ord('a'); $c <= ord('z'); $c++) {
                    $ch = chr($c);
                    if ($ch !== $left && $ch !== $right) {
                        $chars[$i] = $ch;
                        break;
                    }
                }
            }
        }
        return implode('', $chars);
    }
}
```

## Swift

```swift
class Solution {
    func modifyString(_ s: String) -> String {
        var chars = Array(s)
        let n = chars.count
        for i in 0..<n {
            if chars[i] == "?" {
                let leftChar: Character? = i > 0 ? chars[i - 1] : nil
                let rightChar: Character? = i + 1 < n ? chars[i + 1] : nil
                for candidate in ["a", "b", "c"] {
                    let ch = Character(candidate)
                    if (leftChar == nil || ch != leftChar!) && (rightChar == nil || ch != rightChar!) {
                        chars[i] = ch
                        break
                    }
                }
            }
        }
        return String(chars)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun modifyString(s: String): String {
        val n = s.length
        val chars = s.toCharArray()
        for (i in 0 until n) {
            if (chars[i] == '?') {
                val left = if (i > 0) chars[i - 1] else '\u0000'
                val rightOrig = if (i + 1 < n) s[i + 1] else '\u0000'
                for (c in 'a'..'z') {
                    if (c != left && c != rightOrig) {
                        chars[i] = c
                        break
                    }
                }
            }
        }
        return String(chars)
    }
}
```

## Dart

```dart
class Solution {
  String modifyString(String s) {
    List<String> chars = s.split('');
    int n = chars.length;
    for (int i = 0; i < n; i++) {
      if (chars[i] == '?') {
        for (int offset = 0; offset < 26; offset++) {
          String cand = String.fromCharCode('a'.codeUnitAt(0) + offset);
          bool leftOk = i == 0 || chars[i - 1] != cand;
          bool rightOk = i == n - 1 ||
              chars[i + 1] == '?' ||
              chars[i + 1] != cand;
          if (leftOk && rightOk) {
            chars[i] = cand;
            break;
          }
        }
      }
    }
    return chars.join();
  }
}
```

## Golang

```go
func modifyString(s string) string {
	n := len(s)
	b := []byte(s)
	for i := 0; i < n; i++ {
		if b[i] == '?' {
			var left, right byte
			if i > 0 {
				left = b[i-1]
			}
			if i+1 < n && b[i+1] != '?' {
				right = b[i+1]
			}
			for c := byte('a'); c <= 'z'; c++ {
				if c != left && (right == 0 || c != right) {
					b[i] = c
					break
				}
			}
		}
	}
	return string(b)
}
```

## Ruby

```ruby
def modify_string(s)
  chars = s.chars
  n = chars.length
  (0...n).each do |i|
    next unless chars[i] == '?'
    left = i > 0 ? chars[i - 1] : nil
    right = i + 1 < n ? chars[i + 1] : nil
    ('a'..'c').each do |c|
      next if c == left || (right && c == right)
      chars[i] = c
      break
    end
  end
  chars.join
end
```

## Scala

```scala
import scala.util.control.Breaks._

object Solution {
  def modifyString(s: String): String = {
    val n = s.length
    val arr = s.toCharArray
    for (i <- 0 until n) {
      if (arr(i) == '?') {
        val left = if (i > 0) arr(i - 1) else 0.toChar
        val rightOrig = if (i + 1 < n) s.charAt(i + 1) else 0.toChar
        breakable {
          for (c <- 'a' to 'z') {
            if ((left == 0 || c != left) && (rightOrig == '?' || c != rightOrig)) {
              arr(i) = c
              break
            }
          }
        }
      }
    }
    new String(arr)
  }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn modify_string(s: String) -> String {
        let mut chars: Vec<char> = s.chars().collect();
        let n = chars.len();
        for i in 0..n {
            if chars[i] == '?' {
                for c in b'a'..=b'z' {
                    let ch = c as char;
                    let left_ok = if i > 0 { chars[i - 1] != ch } else { true };
                    let right_ok = if i + 1 < n {
                        let next = chars[i + 1];
                        if next == '?' { true } else { next != ch }
                    } else {
                        true
                    };
                    if left_ok && right_ok {
                        chars[i] = ch;
                        break;
                    }
                }
            }
        }
        chars.iter().collect()
    }
}
```

## Racket

```racket
(define/contract (modify-string s)
  (-> string? string?)
  (let* ((chars (string->list s))
         (n (length chars)))
    (define (choose-char left right)
      (for/first ([ch (in-string "abcdefghijklmnopqrstuvwxyz")]
                  #:when (and (not (char=? ch left))
                             (or (char=? right #\?) (not (char=? ch right)))))
        ch))
    (let loop ((i 0) (prev #\space) (acc '()))
      (if (= i n)
          (list->string (reverse acc))
          (let ((c (list-ref chars i)))
            (if (char=? c #\?)
                (let* ((right (if (< (+ i 1) n) (list-ref chars (+ i 1)) #\space))
                       (newc (choose-char prev right)))
                  (loop (+ i 1) newc (cons newc acc)))
                (loop (+ i 1) c (cons c acc))))))))
```

## Erlang

```erlang
-module(solution).
-export([modify_string/1]).

-spec modify_string(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
modify_string(S) ->
    Orig = unicode:characters_to_list(S),
    RevResult = process(Orig, undefined, []),
    Result = lists:reverse(RevResult),
    unicode:characters_to_binary(Result).

process([], _Prev, Acc) ->
    Acc;
process([C|Rest], Prev, Acc) when C =:= $? ->
    NextOrig = case Rest of
                   [] -> undefined;
                   [N|_] -> N
               end,
    NewChar = pick_char(Prev, NextOrig),
    process(Rest, NewChar, [NewChar | Acc]);
process([C|Rest], _Prev, Acc) ->
    process(Rest, C, [C | Acc]).

pick_char(Prev, Next) ->
    lists:nth(
        1,
        [X || X <- [$a,$b,$c,$d,$e,$f,$g,$h,$i,$j,$k,$l,$m,$n,$o,$p,$q,$r,$s,$t,$u,$v,$w,$x,$y,$z],
             (Prev =:= undefined orelse X =/= Prev) andalso
             (Next =:= undefined orelse X =/= Next)]
    ).
```

## Elixir

```elixir
defmodule Solution do
  @spec modify_string(s :: String.t()) :: String.t()
  def modify_string(s) do
    chars = String.to_charlist(s)
    result = replace(chars, [], nil)
    List.to_string(Enum.reverse(result))
  end

  defp replace([], acc, _prev), do: acc

  defp replace([h | t] = rest, acc, prev) do
    if h == ?? do
      next_char =
        case t do
          [n | _] -> n
          [] -> nil
        end

      chosen =
        Enum.find(?a..?z, fn c ->
          c != prev && (next_char == nil || next_char == ?? || c != next_char)
        end)

      replace(t, [chosen | acc], chosen)
    else
      replace(t, [h | acc], h)
    end
  end
end
```
