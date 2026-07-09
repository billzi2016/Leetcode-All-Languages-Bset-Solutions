# 2000. Reverse Prefix of Word

## Cpp

```cpp
class Solution {
public:
    string reversePrefix(string word, char ch) {
        size_t idx = word.find(ch);
        if (idx == string::npos) return word;
        reverse(word.begin(), word.begin() + idx + 1);
        return word;
    }
};
```

## Java

```java
class Solution {
    public String reversePrefix(String word, char ch) {
        int idx = word.indexOf(ch);
        if (idx == -1) {
            return word;
        }
        StringBuilder sb = new StringBuilder(word.length());
        for (int i = idx; i >= 0; --i) {
            sb.append(word.charAt(i));
        }
        sb.append(word.substring(idx + 1));
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        idx = word.find(ch)
        if idx == -1:
            return word
        return word[:idx+1][::-1] + word[idx+1:]
```

## Python3

```python
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        if idx == -1:
            return word
        return word[:idx + 1][::-1] + word[idx + 1:]
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* reversePrefix(char* word, char ch) {
    size_t n = strlen(word);
    char *res = (char *)malloc(n + 1);
    if (!res) return NULL;
    memcpy(res, word, n + 1); // copy including null terminator

    size_t idx = 0;
    while (idx < n && res[idx] != ch) {
        ++idx;
    }
    if (idx < n) { // character found
        size_t left = 0, right = idx;
        while (left < right) {
            char tmp = res[left];
            res[left] = res[right];
            res[right] = tmp;
            ++left;
            --right;
        }
    }
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string ReversePrefix(string word, char ch)
    {
        int idx = word.IndexOf(ch);
        if (idx == -1) return word;
        char[] prefix = word.Substring(0, idx + 1).ToCharArray();
        System.Array.Reverse(prefix);
        return new string(prefix) + word.Substring(idx + 1);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word
 * @param {character} ch
 * @return {string}
 */
var reversePrefix = function(word, ch) {
    const idx = word.indexOf(ch);
    if (idx === -1) return word;
    const reversed = word.slice(0, idx + 1).split('').reverse().join('');
    return reversed + word.slice(idx + 1);
};
```

## Typescript

```typescript
function reversePrefix(word: string, ch: string): string {
    const idx = word.indexOf(ch);
    if (idx === -1) return word;
    const reversed = word.slice(0, idx + 1).split('').reverse().join('');
    return reversed + word.slice(idx + 1);
}
```

## Php

```php
<?php
class Solution {
    /**
     * @param String $word
     * @param String $ch
     * @return String
     */
    function reversePrefix($word, $ch) {
        $pos = strpos($word, $ch);
        if ($pos === false) {
            return $word;
        }
        $prefix = substr($word, 0, $pos + 1);
        $reversed = strrev($prefix);
        $suffix = substr($word, $pos + 1);
        return $reversed . $suffix;
    }
}
?>
```

## Swift

```swift
class Solution {
    func reversePrefix(_ word: String, _ ch: Character) -> String {
        guard let idx = word.firstIndex(of: ch) else { return word }
        
        // Extract and reverse the prefix up to and including idx
        let prefix = word[word.startIndex...idx]
        let reversedPrefix = String(prefix.reversed())
        
        // Append the remaining suffix, if any
        let afterIdx = word.index(after: idx)
        let suffix = afterIdx < word.endIndex ? String(word[afterIdx...]) : ""
        
        return reversedPrefix + suffix
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun reversePrefix(word: String, ch: Char): String {
        val idx = word.indexOf(ch)
        if (idx == -1) return word
        val sb = StringBuilder()
        for (i in idx downTo 0) {
            sb.append(word[i])
        }
        sb.append(word.substring(idx + 1))
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String reversePrefix(String word, String ch) {
    int idx = word.indexOf(ch);
    if (idx == -1) return word;
    String prefixReversed = word.substring(0, idx + 1).split('').reversed.join();
    return prefixReversed + word.substring(idx + 1);
  }
}
```

## Golang

```go
func reversePrefix(word string, ch byte) string {
	idx := -1
	for i := 0; i < len(word); i++ {
		if word[i] == ch {
			idx = i
			break
		}
	}
	if idx == -1 {
		return word
	}
	b := []byte(word)
	for l, r := 0, idx; l < r; l, r = l+1, r-1 {
		b[l], b[r] = b[r], b[l]
	}
	return string(b)
}
```

## Ruby

```ruby
def reverse_prefix(word, ch)
  idx = word.index(ch)
  return word unless idx
  word[0..idx].reverse + (word[(idx + 1)..-1] || "")
end
```

## Scala

```scala
object Solution {
    def reversePrefix(word: String, ch: Char): String = {
        val idx = word.indexOf(ch)
        if (idx == -1) word
        else word.substring(0, idx + 1).reverse + word.substring(idx + 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn reverse_prefix(word: String, ch: char) -> String {
        // Find the first occurrence of `ch`
        let mut pos = None;
        for (i, c) in word.chars().enumerate() {
            if c == ch {
                pos = Some(i);
                break;
            }
        }

        match pos {
            None => word,
            Some(idx) => {
                // Since the input consists of lowercase English letters,
                // each character occupies exactly one byte.
                let mut bytes = word.into_bytes();
                let mut left = 0usize;
                let mut right = idx;
                while left < right {
                    bytes.swap(left, right);
                    left += 1;
                    right -= 1;
                }
                // SAFETY: we only swapped ASCII bytes, so the result is valid UTF‑8.
                unsafe { String::from_utf8_unchecked(bytes) }
            }
        }
    }
}
```

## Racket

```racket
(define/contract (reverse-prefix word ch)
  (-> string? char? string?)
  (let* ((len (string-length word))
         (idx (let loop ((i 0))
                (cond [(= i len) -1]
                      [(char=? (string-ref word i) ch) i]
                      [else (loop (+ i 1))]))))
    (if (= idx -1)
        word
        (let* ((prefix (substring word 0 (+ idx 1)))
               (reversed-prefix (list->string (reverse (string->list prefix))))
               (suffix (substring word (+ idx 1) len)))
          (string-append reversed-prefix suffix)))))
```

## Erlang

```erlang
-spec reverse_prefix(Word :: unicode:unicode_binary(), Ch :: char()) -> unicode:unicode_binary().
reverse_prefix(Word, Ch) ->
    case binary:match(Word, <<Ch>>) of
        {Pos, 1} ->
            PrefixLen = Pos + 1,
            Prefix = binary:part(Word, 0, PrefixLen),
            RestSize = byte_size(Word) - PrefixLen,
            Rest = if RestSize > 0 -> binary:part(Word, PrefixLen, RestSize);
                      true -> <<>>
                   end,
            RevPrefix = list_to_binary(lists:reverse(binary_to_list(Prefix))),
            <<RevPrefix/binary, Rest/binary>>;
        nomatch ->
            Word
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec reverse_prefix(word :: String.t(), ch :: char) :: String.t()
  def reverse_prefix(word, ch) do
    # Convert the character to a one‑character string if necessary
    ch_str =
      cond do
        is_integer(ch) -> <<ch::utf8>>
        is_binary(ch) and byte_size(ch) == 1 -> ch
        true -> String.at(to_string(ch), 0)
      end

    graphemes = String.graphemes(word)

    case Enum.find_index(graphemes, fn c -> c == ch_str end) do
      nil ->
        word

      idx ->
        {prefix, suffix} = Enum.split(graphemes, idx + 1)
        (Enum.reverse(prefix) ++ suffix) |> Enum.join()
    end
  end
end
```
