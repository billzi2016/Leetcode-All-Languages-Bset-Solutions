# 2351. First Letter to Appear Twice

## Cpp

```cpp
class Solution {
public:
    char repeatedCharacter(string s) {
        bool seen[26] = {false};
        for (char c : s) {
            int idx = c - 'a';
            if (seen[idx]) return c;
            seen[idx] = true;
        }
        return '\0'; // Should never reach here as per problem constraints
    }
};
```

## Java

```java
class Solution {
    public char repeatedCharacter(String s) {
        boolean[] seen = new boolean[26];
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            int idx = c - 'a';
            if (seen[idx]) {
                return c;
            }
            seen[idx] = true;
        }
        // According to constraints, this line is never reached.
        return '\0';
    }
}
```

## Python

```python
class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        seen = set()
        for ch in s:
            if ch in seen:
                return ch
            seen.add(ch)
```

## Python3

```python
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for ch in s:
            if ch in seen:
                return ch
            seen.add(ch)
```

## C

```c
char repeatedCharacter(char* s) {
    int seen[26] = {0};
    for (int i = 0; s[i]; ++i) {
        int idx = s[i] - 'a';
        if (seen[idx]) return s[i];
        seen[idx] = 1;
    }
    return '\0';
}
```

## Csharp

```csharp
public class Solution {
    public char RepeatedCharacter(string s) {
        var seen = new HashSet<char>();
        foreach (char c in s) {
            if (!seen.Add(c)) {
                return c;
            }
        }
        // According to constraints, this line is never reached.
        return '\0';
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {character}
 */
var repeatedCharacter = function(s) {
    const seen = new Set();
    for (const ch of s) {
        if (seen.has(ch)) return ch;
        seen.add(ch);
    }
};
```

## Typescript

```typescript
function repeatedCharacter(s: string): string {
    const seen = new Set<string>();
    for (const ch of s) {
        if (seen.has(ch)) return ch;
        seen.add(ch);
    }
    // According to constraints, this line is never reached.
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
    function repeatedCharacter($s) {
        $seen = [];
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $ch = $s[$i];
            if (isset($seen[$ch])) {
                return $ch;
            }
            $seen[$ch] = true;
        }
        return "";
    }
}
```

## Swift

```swift
class Solution {
    func repeatedCharacter(_ s: String) -> Character {
        var seen = Set<Character>()
        for ch in s {
            if seen.contains(ch) {
                return ch
            }
            seen.insert(ch)
        }
        // As per constraints, this line will never be reached.
        return "\0"
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun repeatedCharacter(s: String): Char {
        val seen = BooleanArray(26)
        for (ch in s) {
            val idx = ch - 'a'
            if (seen[idx]) return ch
            seen[idx] = true
        }
        // As per problem constraints, this line is never reached.
        throw IllegalArgumentException("No repeated character found")
    }
}
```

## Dart

```dart
class Solution {
  String repeatedCharacter(String s) {
    final Set<String> seen = {};
    for (int i = 0; i < s.length; i++) {
      String ch = s[i];
      if (seen.contains(ch)) return ch;
      seen.add(ch);
    }
    // According to constraints, this line is never reached.
    return '';
  }
}
```

## Golang

```go
func repeatedCharacter(s string) byte {
    var seen [26]bool
    for i := 0; i < len(s); i++ {
        idx := s[i] - 'a'
        if seen[idx] {
            return s[i]
        }
        seen[idx] = true
    }
    return 0
}
```

## Ruby

```ruby
def repeated_character(s)
  seen = {}
  s.each_char do |ch|
    return ch if seen.key?(ch)
    seen[ch] = true
  end
end
```

## Scala

```scala
object Solution {
    def repeatedCharacter(s: String): Char = {
        val seen = new Array[Boolean](26)
        for (ch <- s) {
            val idx = ch - 'a'
            if (seen(idx)) return ch
            seen(idx) = true
        }
        // This line will never be reached because the problem guarantees a repeated character.
        '\u0000'
    }
}
```

## Rust

```rust
impl Solution {
    pub fn repeated_character(s: String) -> char {
        let mut seen = [false; 26];
        for b in s.bytes() {
            let idx = (b - b'a') as usize;
            if seen[idx] {
                return b as char;
            }
            seen[idx] = true;
        }
        unreachable!()
    }
}
```

## Racket

```racket
(define/contract (repeated-character s)
  (-> string? char?)
  (let ([len (string-length s)]
        [seen (make-hash)])
    (let recur ((i 0))
      (if (= i len)
          (error "No repeated character found")
          (let ([c (string-ref s i)])
            (if (hash-has-key? seen c)
                c
                (begin
                  (hash-set! seen c #t)
                  (recur (add1 i)))))))))
```

## Erlang

```erlang
-spec repeated_character(unicode:unicode_binary()) -> char().
repeated_character(S) ->
    repeated_character(lists:binary_to_list(S), #{}).

repeated_character([H|T], Seen) ->
    case maps:is_key(H, Seen) of
        true -> H;
        false -> repeated_character(T, maps:put(H, true, Seen))
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec repeated_character(s :: String.t()) :: String.t()
  def repeated_character(s) do
    Enum.reduce_while(String.graphemes(s), MapSet.new(), fn ch, set ->
      if MapSet.member?(set, ch) do
        {:halt, ch}
      else
        {:cont, MapSet.put(set, ch)}
      end
    end)
  end
end
```
