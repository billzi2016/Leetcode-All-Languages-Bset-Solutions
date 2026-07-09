# 2825. Make String a Subsequence Using Cyclic Increments

## Cpp

```cpp
class Solution {
public:
    bool canMakeSubsequence(string str1, string str2) {
        int n = str1.size(), m = str2.size();
        int j = 0;
        for (int i = 0; i < n && j < m; ++i) {
            char c = str1[i];
            char need = str2[j];
            if (c == need || (c == 'z' ? 'a' : c + 1) == need) {
                ++j;
            }
        }
        return j == m;
    }
};
```

## Java

```java
class Solution {
    public boolean canMakeSubsequence(String str1, String str2) {
        int j = 0;
        int n2 = str2.length();
        for (int i = 0; i < str1.length() && j < n2; i++) {
            char c = str1.charAt(i);
            char target = str2.charAt(j);
            char next = (c == 'z') ? 'a' : (char) (c + 1);
            if (c == target || next == target) {
                j++;
            }
        }
        return j == n2;
    }
}
```

## Python

```python
class Solution(object):
    def canMakeSubsequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        n, m = len(str1), len(str2)
        j = 0
        for i in range(n):
            if j == m:
                break
            c1 = str1[i]
            target = str2[j]
            # check original or incremented (cyclic)
            if c1 == target or (chr(((ord(c1) - 97 + 1) % 26) + 97)) == target:
                j += 1
        return j == m
```

## Python3

```python
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        j = 0
        n2 = len(str2)
        for c in str1:
            if j == n2:
                break
            target = str2[j]
            if c == target or (chr(((ord(c) - 97 + 1) % 26) + 97)) == target:
                j += 1
        return j == n2
```

## C

```c
#include <stdbool.h>

bool canMakeSubsequence(char* str1, char* str2) {
    int i = 0, j = 0;
    while (str1[i] && str2[j]) {
        char c = str1[i];
        char t = str2[j];
        if (c == t || ((c - 'a' + 1) % 26 + 'a') == t) {
            j++;
        }
        i++;
    }
    return str2[j] == '\0';
}
```

## Csharp

```csharp
public class Solution
{
    public bool CanMakeSubsequence(string str1, string str2)
    {
        int j = 0;
        for (int i = 0; i < str1.Length && j < str2.Length; i++)
        {
            char c = str1[i];
            if (c == str2[j] || ((c == 'z' ? 'a' : (char)(c + 1)) == str2[j]))
                j++;
        }
        return j == str2.Length;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} str1
 * @param {string} str2
 * @return {boolean}
 */
var canMakeSubsequence = function(str1, str2) {
    const n = str1.length;
    const m = str2.length;
    let j = 0;
    for (let i = 0; i < n && j < m; ++i) {
        const c1 = str1.charCodeAt(i);
        const c2 = str2.charCodeAt(j);
        if (c1 === c2 || ((c1 - 97 + 1) % 26 + 97) === c2) {
            ++j;
        }
    }
    return j === m;
};
```

## Typescript

```typescript
function canMakeSubsequence(str1: string, str2: string): boolean {
    let j = 0;
    for (let i = 0; i < str1.length && j < str2.length; i++) {
        const c = str1[i];
        if (
            c === str2[j] ||
            (c === 'z' ? 'a' : String.fromCharCode(c.charCodeAt(0) + 1)) === str2[j]
        ) {
            j++;
        }
    }
    return j === str2.length;
}
```

## Php

```php
class Solution {

    /**
     * @param String $str1
     * @param String $str2
     * @return Boolean
     */
    function canMakeSubsequence($str1, $str2) {
        $n = strlen($str1);
        $m = strlen($str2);
        $j = 0;
        for ($i = 0; $i < $n && $j < $m; $i++) {
            $c = $str1[$i];
            $next = ($c === 'z') ? 'a' : chr(ord($c) + 1);
            if ($c === $str2[$j] || $next === $str2[$j]) {
                $j++;
            }
        }
        return $j === $m;
    }
}
```

## Swift

```swift
class Solution {
    func canMakeSubsequence(_ str1: String, _ str2: String) -> Bool {
        let s1 = Array(str1.utf8)
        let s2 = Array(str2.utf8)
        var j = 0
        for ch in s1 {
            if j >= s2.count { break }
            if ch == s2[j] || (ch == 122 ? 97 : ch + 1) == s2[j] {
                j += 1
            }
        }
        return j == s2.count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canMakeSubsequence(str1: String, str2: String): Boolean {
        var j = 0
        val m = str2.length
        if (m == 0) return true
        for (c in str1) {
            if (j >= m) break
            val target = str2[j]
            val inc = if (c == 'z') 'a' else c + 1
            if (c == target || inc == target) {
                j++
            }
        }
        return j == m
    }
}
```

## Dart

```dart
class Solution {
  bool canMakeSubsequence(String str1, String str2) {
    int j = 0;
    int n = str1.length;
    int m = str2.length;
    for (int i = 0; i < n && j < m; i++) {
      int c1 = str1.codeUnitAt(i);
      int c2 = str2.codeUnitAt(j);
      if (c1 == c2 ||
          ((c1 - 97 + 1) % 26 + 97) == c2) {
        j++;
      }
    }
    return j == m;
  }
}
```

## Golang

```go
func canMakeSubsequence(str1 string, str2 string) bool {
    n, m := len(str1), len(str2)
    j := 0
    for i := 0; i < n && j < m; i++ {
        c := str1[i]
        var nxt byte
        if c == 'z' {
            nxt = 'a'
        } else {
            nxt = c + 1
        }
        if c == str2[j] || nxt == str2[j] {
            j++
        }
    }
    return j == m
}
```

## Ruby

```ruby
def can_make_subsequence(str1, str2)
  b1 = str1.bytes
  b2 = str2.bytes
  i = 0
  j = 0
  n = b1.length
  m = b2.length
  while i < n && j < m
    if b1[i] == b2[j] || ((b1[i] - 97 + 1) % 26 + 97) == b2[j]
      j += 1
    end
    i += 1
  end
  j == m
end
```

## Scala

```scala
object Solution {
    def canMakeSubsequence(str1: String, str2: String): Boolean = {
        var j = 0
        val m = str2.length
        for (i <- 0 until str1.length if j < m) {
            val c1 = str1.charAt(i)
            val need = str2.charAt(j)
            val inc = if (c1 == 'z') 'a' else (c1 + 1).toChar
            if (c1 == need || inc == need) {
                j += 1
            }
        }
        j == m
    }
}
```

## Rust

```rust
impl Solution {
    pub fn can_make_subsequence(str1: String, str2: String) -> bool {
        let s1 = str1.as_bytes();
        let s2 = str2.as_bytes();
        let mut j = 0usize;
        for &c in s1.iter() {
            if j == s2.len() {
                break;
            }
            let target = s2[j];
            let inc = if c == b'z' { b'a' } else { c + 1 };
            if c == target || inc == target {
                j += 1;
            }
        }
        j == s2.len()
    }
}
```

## Racket

```racket
(define (next-char ch)
  (if (char=? ch #\z)
      #\a
      (integer->char (+ (char->integer ch) 1))))

(define/contract (can-make-subsequence str1 str2)
  (-> string? string? boolean?)
  (let* ([n (string-length str1)]
         [m (string-length str2)])
    (let loop ((i 0) (j 0))
      (cond
        [(= j m) #t]
        [(>= i n) #f]
        [else
          (define c1 (string-ref str1 i))
          (define t (string-ref str2 j))
          (if (or (char=? c1 t)
                  (char=? (next-char c1) t))
              (loop (+ i 1) (+ j 1))
              (loop (+ i 1) j))]))))
```

## Erlang

```erlang
-spec can_make_subsequence(Str1 :: unicode:unicode_binary(), Str2 :: unicode:unicode_binary()) -> boolean().
can_make_subsequence(Str1, Str2) ->
    Len2 = byte_size(Str2),
    case match(Str1, Str2, 0, Len2) of
        J when J == Len2 -> true;
        _ -> false
    end.

match(_, _, J, Len2) when J >= Len2 -> J;
match(<<>>, _, J, _) -> J;
match(<<C1, Rest/binary>>, Str2, J, Len2) ->
    C2 = binary:at(Str2, J),
    NextC = if C1 == $z -> $a; true -> C1 + 1 end,
    case (C1 =:= C2) orelse (NextC =:= C2) of
        true -> match(Rest, Str2, J + 1, Len2);
        false -> match(Rest, Str2, J, Len2)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec can_make_subsequence(str1 :: String.t(), str2 :: String.t()) :: boolean()
  def can_make_subsequence(str1, str2) do
    s1 = String.to_charlist(str1)
    s2 = String.to_charlist(str2)
    go(s1, s2)
  end

  defp go(_s1, []), do: true
  defp go([], _s2), do: false
  defp go([c | rest1], [d | rest2]) do
    if c == d or next_char(c) == d do
      go(rest1, rest2)
    else
      go(rest1, [d | rest2])
    end
  end

  defp next_char(?z), do: ?a
  defp next_char(c), do: c + 1
end
```
