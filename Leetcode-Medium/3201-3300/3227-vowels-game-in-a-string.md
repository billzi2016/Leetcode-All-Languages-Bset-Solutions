# 3227. Vowels Game in a String

## Cpp

```cpp
class Solution {
public:
    bool doesAliceWin(string s) {
        auto isVowel = [](char c)->bool{
            return c=='a' || c=='e' || c=='i' || c=='o' || c=='u';
        };
        int n = s.size();
        int xorSum = 0;
        int i = 0;
        while (i < n) {
            if (!isVowel(s[i])) {
                ++i;
                continue;
            }
            int len = 0;
            while (i < n && isVowel(s[i])) {
                ++len;
                ++i;
            }
            xorSum ^= len;
        }
        return xorSum != 0;
    }
};
```

## Java

```java
class Solution {
    public boolean doesAliceWin(String s) {
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                count++;
            }
        }
        return count % 2 == 1;
    }
}
```

## Python

```python
class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = set('aeiou')
        groups = 0
        i = 0
        n = len(s)
        while i < n:
            if s[i] in vowels:
                groups += 1
                while i < n and s[i] in vowels:
                    i += 1
            else:
                i += 1
        return groups % 2 == 1
```

## Python3

```python
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = set('aeiou')
        count = sum(1 for ch in s if ch in vowels)
        return count % 2 == 1
```

## C

```c
#include <stdbool.h>

bool doesAliceWin(char* s) {
    int count = 0;
    for (int i = 0; s[i] != '\0'; ++i) {
        char c = s[i];
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
            ++count;
    }
    return (count % 2) == 1;
}
```

## Csharp

```csharp
public class Solution {
    public bool DoesAliceWin(string s) {
        int vowelCount = 0;
        foreach (char c in s) {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
                vowelCount++;
        }
        return vowelCount != 0 && vowelCount != 2;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {boolean}
 */
var doesAliceWin = function(s) {
    let vowels = new Set(['a','e','i','o','u']);
    let count = 0;
    for (let ch of s) {
        if (vowels.has(ch)) count++;
    }
    return count % 2 === 1;
};
```

## Typescript

```typescript
function doesAliceWin(s: string): boolean {
    const vowels = new Set(['a', 'e', 'i', 'o', 'u']);
    let count = 0;
    for (let i = 0; i < s.length; ++i) {
        if (vowels.has(s[i])) {
            ++count;
        }
    }
    return count !== 0 && count !== 2;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function doesAliceWin($s) {
        $vowels = ['a'=>true,'e'=>true,'i'=>true,'o'=>true,'u'=>true];
        $cnt = 0;
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            if (isset($vowels[$s[$i]])) {
                $cnt++;
            }
        }
        return $cnt % 2 == 1;
    }
}
```

## Swift

```swift
class Solution {
    func doesAliceWin(_ s: String) -> Bool {
        let vowels: Set<Character> = ["a", "e", "i", "o", "u"]
        for ch in s {
            if vowels.contains(ch) {
                return true
            }
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun doesAliceWin(s: String): Boolean {
        for (ch in s) {
            when (ch) {
                'a', 'e', 'i', 'o', 'u' -> return true
            }
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool doesAliceWin(String s) {
    int vowelCount = 0;
    for (int i = 0; i < s.length; i++) {
      int c = s.codeUnitAt(i);
      if (c == 97 || // a
          c == 101 || // e
          c == 105 || // i
          c == 111 || // o
          c == 117) { // u
        vowelCount++;
      }
    }
    return vowelCount % 2 == 1;
  }
}
```

## Golang

```go
func doesAliceWin(s string) bool {
    cnt := 0
    for _, ch := range s {
        switch ch {
        case 'a', 'e', 'i', 'o', 'u':
            cnt++
        }
    }
    return cnt%2 == 1
}
```

## Ruby

```ruby
def does_alice_win(s)
  s.count('aeiou').odd?
end
```

## Scala

```scala
object Solution {
    def doesAliceWin(s: String): Boolean = {
        val vowels = Set('a', 'e', 'i', 'o', 'u')
        var count = 0
        for (ch <- s) {
            if (vowels.contains(ch)) count += 1
        }
        count % 2 == 1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn does_alice_win(s: String) -> bool {
        let bytes = s.as_bytes();
        let mut vowel_count = 0usize;
        let mut has_even_index_vowel = false; // 0-indexed even position
        for (i, &b) in bytes.iter().enumerate() {
            let is_vowel = matches!(b as char, 'a' | 'e' | 'i' | 'o' | 'u');
            if is_vowel {
                vowel_count += 1;
                if i % 2 == 0 {
                    has_even_index_vowel = true;
                }
            }
        }
        if vowel_count == 0 {
            return false;
        }
        if vowel_count % 2 == 1 {
            return true;
        }
        // even number of vowels
        has_even_index_vowel
    }
}
```

## Racket

```racket
(define/contract (does-alice-win s)
  (-> string? boolean?)
  (let* ([vowels (list #\a #\e #\i #\o #\u)]
         [cnt (for/sum ([ch (in-string s)])
                (if (memv ch vowels) 1 0))])
    (= (modulo cnt 2) 1)))
```

## Erlang

```erlang
-spec does_alice_win(S :: unicode:unicode_binary()) -> boolean().
does_alice_win(S) ->
    Count = count_vowels(binary_to_list(S), 0),
    (Count band 1) =:= 1.

count_vowels([], Acc) -> Acc;
count_vowels([H|T], Acc) ->
    NewAcc = case H of
        $a -> Acc + 1;
        $e -> Acc + 1;
        $i -> Acc + 1;
        $o -> Acc + 1;
        $u -> Acc + 1;
        _   -> Acc
    end,
    count_vowels(T, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec does_alice_win(s :: String.t()) :: boolean()
  def does_alice_win(s) do
    vowels = MapSet.new(["a", "e", "i", "o", "u"])

    count =
      s
      |> String.graphemes()
      |> Enum.reduce(0, fn ch, acc ->
        if MapSet.member?(vowels, ch), do: acc + 1, else: acc
      end)

    rem(count, 2) == 1
  end
end
```
