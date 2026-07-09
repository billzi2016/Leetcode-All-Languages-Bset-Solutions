# 2486. Append Characters to String to Make Subsequence

## Cpp

```cpp
class Solution {
public:
    int appendCharacters(string s, string t) {
        int i = 0, j = 0;
        while (i < (int)s.size() && j < (int)t.size()) {
            if (s[i] == t[j]) ++j;
            ++i;
        }
        return (int)t.size() - j;
    }
};
```

## Java

```java
class Solution {
    public int appendCharacters(String s, String t) {
        int i = 0, j = 0;
        int n = s.length(), m = t.length();
        while (i < n && j < m) {
            if (s.charAt(i) == t.charAt(j)) {
                j++;
            }
            i++;
        }
        return m - j;
    }
}
```

## Python

```python
class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        i = j = 0
        n, m = len(s), len(t)
        while i < n and j < m:
            if s[i] == t[j]:
                j += 1
            i += 1
        return m - j
```

## Python3

```python
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = j = 0
        n, m = len(s), len(t)
        while i < n and j < m:
            if s[i] == t[j]:
                j += 1
            i += 1
        return m - j
```

## C

```c
#include <string.h>

int appendCharacters(char* s, char* t) {
    int i = 0, j = 0;
    int len_t = (int)strlen(t);
    
    while (s[i] && j < len_t) {
        if (s[i] == t[j]) {
            ++j;
        }
        ++i;
    }
    
    return len_t - j;
}
```

## Csharp

```csharp
public class Solution
{
    public int AppendCharacters(string s, string t)
    {
        int i = 0, j = 0;
        while (i < s.Length && j < t.Length)
        {
            if (s[i] == t[j])
                j++;
            i++;
        }
        return t.Length - j;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var appendCharacters = function(s, t) {
    let i = 0, j = 0;
    const n = s.length, m = t.length;
    while (i < n && j < m) {
        if (s[i] === t[j]) {
            j++;
        }
        i++;
    }
    return m - j;
};
```

## Typescript

```typescript
function appendCharacters(s: string, t: string): number {
    let i = 0, j = 0;
    while (i < s.length && j < t.length) {
        if (s[i] === t[j]) {
            j++;
        }
        i++;
    }
    return t.length - j;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @return Integer
     */
    function appendCharacters($s, $t) {
        $lenS = strlen($s);
        $lenT = strlen($t);
        $i = 0;
        $j = 0;
        while ($i < $lenS && $j < $lenT) {
            if ($s[$i] === $t[$j]) {
                $j++;
            }
            $i++;
        }
        return $lenT - $j;
    }
}
```

## Swift

```swift
class Solution {
    func appendCharacters(_ s: String, _ t: String) -> Int {
        let sBytes = Array(s.utf8)
        let tBytes = Array(t.utf8)
        var i = 0
        var j = 0
        while i < sBytes.count && j < tBytes.count {
            if sBytes[i] == tBytes[j] {
                j += 1
            }
            i += 1
        }
        return tBytes.count - j
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun appendCharacters(s: String, t: String): Int {
        var i = 0
        var j = 0
        val n = s.length
        val m = t.length
        while (i < n && j < m) {
            if (s[i] == t[j]) {
                j++
            }
            i++
        }
        return m - j
    }
}
```

## Dart

```dart
class Solution {
  int appendCharacters(String s, String t) {
    int i = 0, j = 0;
    while (i < s.length && j < t.length) {
      if (s.codeUnitAt(i) == t.codeUnitAt(j)) {
        j++;
      }
      i++;
    }
    return t.length - j;
  }
}
```

## Golang

```go
func appendCharacters(s string, t string) int {
    i, j := 0, 0
    for i < len(s) && j < len(t) {
        if s[i] == t[j] {
            j++
        }
        i++
    }
    return len(t) - j
}
```

## Ruby

```ruby
# @param {String} s
# @param {String} t
# @return {Integer}
def append_characters(s, t)
  i = 0
  j = 0
  while i < s.length && j < t.length
    j += 1 if s[i] == t[j]
    i += 1
  end
  t.length - j
end
```

## Scala

```scala
object Solution {
    def appendCharacters(s: String, t: String): Int = {
        var i = 0
        var j = 0
        val n = s.length
        val m = t.length
        while (i < n && j < m) {
            if (s.charAt(i) == t.charAt(j)) j += 1
            i += 1
        }
        m - j
    }
}
```

## Rust

```rust
impl Solution {
    pub fn append_characters(s: String, t: String) -> i32 {
        let s_bytes = s.as_bytes();
        let t_bytes = t.as_bytes();
        let mut i = 0usize;
        let mut j = 0usize;
        while i < s_bytes.len() && j < t_bytes.len() {
            if s_bytes[i] == t_bytes[j] {
                j += 1;
            }
            i += 1;
        }
        (t_bytes.len() - j) as i32
    }
}
```

## Racket

```racket
(define/contract (append-characters s t)
  (-> string? string? exact-integer?)
  (let* ((n (string-length s))
         (m (string-length t))
         (i 0)
         (j 0))
    (let loop ()
      (if (or (= i n) (= j m))
          (- m j)
          (begin
            (when (char=? (string-ref s i) (string-ref t j))
              (set! j (+ j 1)))
            (set! i (+ i 1))
            (loop))))))
```

## Erlang

```erlang
-spec append_characters(S :: unicode:unicode_binary(), T :: unicode:unicode_binary()) -> integer().
append_characters(S, T) ->
    SList = binary_to_list(S),
    TList = binary_to_list(T),
    Remaining = match_prefix(SList, TList),
    length(Remaining).

match_prefix(_, []) -> [];
match_prefix([], T) -> T;
match_prefix([Sh|St], [Th|Tt]) ->
    case Sh == Th of
        true -> match_prefix(St, Tt);
        false -> match_prefix(St, [Th|Tt])
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec append_characters(s :: String.t(), t :: String.t()) :: integer()
  def append_characters(s, t) do
    s_len = byte_size(s)
    t_len = byte_size(t)

    matched = loop(s, s_len, 0, t, t_len, 0)
    t_len - matched
  end

  defp loop(s, s_len, i, t, t_len, j) when i < s_len and j < t_len do
    si = :binary.at(s, i)
    tj = :binary.at(t, j)

    if si == tj do
      loop(s, s_len, i + 1, t, t_len, j + 1)
    else
      loop(s, s_len, i + 1, t, t_len, j)
    end
  end

  defp loop(_s, _s_len, _i, _t, _t_len, j), do: j
end
```
