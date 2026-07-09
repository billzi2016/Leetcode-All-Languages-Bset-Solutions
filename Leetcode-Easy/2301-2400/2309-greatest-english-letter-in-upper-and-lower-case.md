# 2309. Greatest English Letter in Upper and Lower Case

## Cpp

```cpp
class Solution {
public:
    string greatestLetter(string s) {
        bool lower[26] = {false};
        bool upper[26] = {false};
        for (char c : s) {
            if ('a' <= c && c <= 'z')
                lower[c - 'a'] = true;
            else if ('A' <= c && c <= 'Z')
                upper[c - 'A'] = true;
        }
        for (int i = 25; i >= 0; --i) {
            if (lower[i] && upper[i])
                return string(1, char('A' + i));
        }
        return "";
    }
};
```

## Java

```java
class Solution {
    public String greatestLetter(String s) {
        boolean[] upper = new boolean[26];
        boolean[] lower = new boolean[26];
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c >= 'A' && c <= 'Z') {
                upper[c - 'A'] = true;
            } else { // assume lowercase
                lower[c - 'a'] = true;
            }
        }
        for (int i = 25; i >= 0; i--) {
            if (upper[i] && lower[i]) {
                return String.valueOf((char) ('A' + i));
            }
        }
        return "";
    }
}
```

## Python

```python
class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = set(s)
        for c in map(chr, range(ord('Z'), ord('A') - 1, -1)):
            if c in chars and c.lower() in chars:
                return c
        return ""
```

## Python3

```python
class Solution:
    def greatestLetter(self, s: str) -> str:
        chars = set(s)
        for c in range(ord('Z'), ord('A') - 1, -1):
            upper = chr(c)
            lower = chr(c + 32)  # 'a' - 'A' = 32
            if upper in chars and lower in chars:
                return upper
        return ""
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

char* greatestLetter(char* s) {
    bool lower[26] = {false};
    bool upper[26] = {false};

    for (int i = 0; s[i] != '\0'; ++i) {
        char c = s[i];
        if (c >= 'a' && c <= 'z')
            lower[c - 'a'] = true;
        else if (c >= 'A' && c <= 'Z')
            upper[c - 'A'] = true;
    }

    for (int i = 25; i >= 0; --i) {
        if (lower[i] && upper[i]) {
            char *res = (char *)malloc(2);
            res[0] = 'A' + i;
            res[1] = '\0';
            return res;
        }
    }

    char *empty = (char *)malloc(1);
    empty[0] = '\0';
    return empty;
}
```

## Csharp

```csharp
public class Solution
{
    public string GreatestLetter(string s)
    {
        bool[] lower = new bool[26];
        bool[] upper = new bool[26];

        foreach (char c in s)
        {
            if (c >= 'a' && c <= 'z')
                lower[c - 'a'] = true;
            else if (c >= 'A' && c <= 'Z')
                upper[c - 'A'] = true;
        }

        for (int i = 25; i >= 0; i--)
        {
            if (lower[i] && upper[i])
                return ((char)('A' + i)).ToString();
        }

        return "";
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var greatestLetter = function(s) {
    const chars = new Set(s);
    for (let code = 90; code >= 65; code--) { // 'Z' to 'A'
        const upper = String.fromCharCode(code);
        const lower = upper.toLowerCase();
        if (chars.has(upper) && chars.has(lower)) {
            return upper;
        }
    }
    return "";
};
```

## Typescript

```typescript
function greatestLetter(s: string): string {
    const seen = new Set<string>();
    for (const ch of s) {
        seen.add(ch);
    }
    for (let code = 90; code >= 65; code--) {
        const upper = String.fromCharCode(code);
        const lower = upper.toLowerCase();
        if (seen.has(upper) && seen.has(lower)) {
            return upper;
        }
    }
    return "";
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function greatestLetter($s) {
        $upper = [];
        $lower = [];

        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $c = $s[$i];
            if (ctype_upper($c)) {
                $upper[$c] = true;
            } else {
                $lower[$c] = true;
            }
        }

        for ($code = ord('Z'); $code >= ord('A'); $code--) {
            $ch = chr($code);
            $lc = strtolower($ch);
            if (isset($upper[$ch]) && isset($lower[$lc])) {
                return $ch;
            }
        }

        return "";
    }
}
```

## Swift

```swift
class Solution {
    func greatestLetter(_ s: String) -> String {
        var chars = Set<Character>()
        for ch in s {
            chars.insert(ch)
        }
        for ascii in stride(from: 90, through: 65, by: -1) { // 'Z' to 'A'
            if let upperScalar = UnicodeScalar(ascii),
               let lowerScalar = UnicodeScalar(ascii + 32) {
                let upperChar = Character(upperScalar)
                let lowerChar = Character(lowerScalar)
                if chars.contains(upperChar) && chars.contains(lowerChar) {
                    return String(upperChar)
                }
            }
        }
        return ""
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun greatestLetter(s: String): String {
        val lower = BooleanArray(26)
        val upper = BooleanArray(26)
        for (ch in s) {
            if (ch.isLowerCase()) {
                lower[ch - 'a'] = true
            } else {
                upper[ch - 'A'] = true
            }
        }
        for (i in 25 downTo 0) {
            if (lower[i] && upper[i]) {
                return ('A'.code + i).toChar().toString()
            }
        }
        return ""
    }
}
```

## Dart

```dart
class Solution {
  String greatestLetter(String s) {
    List<bool> lower = List.filled(26, false);
    List<bool> upper = List.filled(26, false);
    for (int i = 0; i < s.length; i++) {
      int code = s.codeUnitAt(i);
      if (code >= 97 && code <= 122) {
        lower[code - 97] = true;
      } else if (code >= 65 && code <= 90) {
        upper[code - 65] = true;
      }
    }
    for (int i = 25; i >= 0; i--) {
      if (lower[i] && upper[i]) {
        return String.fromCharCode(65 + i);
      }
    }
    return "";
  }
}
```

## Golang

```go
func greatestLetter(s string) string {
	lower := [26]bool{}
	upper := [26]bool{}
	for i := 0; i < len(s); i++ {
		c := s[i]
		if c >= 'a' && c <= 'z' {
			lower[c-'a'] = true
		} else if c >= 'A' && c <= 'Z' {
			upper[c-'A'] = true
		}
	}
	for i := 25; i >= 0; i-- {
		if lower[i] && upper[i] {
			return string('A' + byte(i))
		}
	}
	return ""
}
```

## Ruby

```ruby
def greatest_letter(s)
  seen = {}
  s.each_char { |c| seen[c] = true }
  ('Z'.ord).downto('A'.ord) do |code|
    up = code.chr
    low = (code + 32).chr
    return up if seen[up] && seen[low]
  end
  ""
end
```

## Scala

```scala
object Solution {
    def greatestLetter(s: String): String = {
        val lower = new Array[Boolean](26)
        val upper = new Array[Boolean](26)
        for (c <- s) {
            if (c >= 'a' && c <= 'z') lower(c - 'a') = true
            else if (c >= 'A' && c <= 'Z') upper(c - 'A') = true
        }
        for (i <- 25 to 0 by -1) {
            if (lower(i) && upper(i)) return ((i + 'A'.toInt).toChar).toString
        }
        ""
    }
}
```

## Rust

```rust
impl Solution {
    pub fn greatest_letter(s: String) -> String {
        let mut lower = [false; 26];
        let mut upper = [false; 26];
        for ch in s.chars() {
            if ch.is_ascii_lowercase() {
                lower[(ch as u8 - b'a') as usize] = true;
            } else if ch.is_ascii_uppercase() {
                upper[(ch as u8 - b'A') as usize] = true;
            }
        }
        for i in (0..26).rev() {
            if lower[i] && upper[i] {
                let c = (b'A' + i as u8) as char;
                return c.to_string();
            }
        }
        String::new()
    }
}
```

## Racket

```racket
(define/contract (greatest-letter s)
  (-> string? string?)
  (let* ([len (string-length s)]
         [upper (make-vector 26 #f)]
         [lower (make-vector 26 #f)])
    (for ([i (in-range len)])
      (let ([c (string-ref s i)])
        (cond
          [(and (char>=? c #\A) (char<=? c #\Z))
           (vector-set! upper (- (char->integer c) (char->integer #\A)) #t)]
          [(and (char>=? c #\a) (char<=? c #\z))
           (vector-set! lower (- (char->integer c) (char->integer #\a)) #t)])))
    (let loop ([i 25])
      (if (< i 0)
          ""
          (if (and (vector-ref upper i) (vector-ref lower i))
              (string (integer->char (+ (char->integer #\A) i)))
              (loop (- i 1)))))))
```

## Erlang

```erlang
-module(solution).
-export([greatest_letter/1]).

-spec greatest_letter(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
greatest_letter(S) ->
    CharList = unicode:characters_to_list(S),
    {UpperSet, LowerSet} = build_sets(CharList, #{}, #{}),
    find_greatest(UpperSet, LowerSet).

build_sets([], Upper, Lower) -> {Upper, Lower};
build_sets([C|Rest], Upper, Lower) ->
    case C of
        _ when $A =< C, C =< $Z ->
            build_sets(Rest, maps:put(C, true, Upper), Lower);
        _ when $a =< C, C =< $z ->
            build_sets(Rest, Upper, maps:put(C, true, Lower));
        _ ->
            build_sets(Rest, Upper, Lower)
    end.

find_greatest(UpperSet, LowerSet) -> find_greatest($Z, UpperSet, LowerSet).

find_greatest(Char, _UpperSet, _LowerSet) when Char < $A -> <<>>;

find_greatest(Char, UpperSet, LowerSet) ->
    LowerChar = Char + 32,
    case {maps:is_key(Char, UpperSet), maps:is_key(LowerChar, LowerSet)} of
        {true, true} -> <<Char>>;
        _ -> find_greatest(Char - 1, UpperSet, LowerSet)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec greatest_letter(s :: String.t) :: String.t
  def greatest_letter(s) do
    set = s |> String.graphemes() |> MapSet.new()

    Enum.find(Enum.reverse(?A..?Z), fn c ->
      upper = <<c>>
      lower = <<c + 32>>
      MapSet.member?(set, upper) and MapSet.member?(set, lower)
    end)
    |> case do
      nil -> ""
      c -> <<c>>
    end
  end
end
```
