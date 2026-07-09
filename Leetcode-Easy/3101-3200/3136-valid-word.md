# 3136. Valid Word

## Cpp

```cpp
class Solution {
public:
    bool isValid(string word) {
        if (word.size() < 3) return false;
        bool hasVowel = false, hasConsonant = false;
        for (char c : word) {
            if (isdigit(static_cast<unsigned char>(c))) continue;
            if (isalpha(static_cast<unsigned char>(c))) {
                char lower = tolower(c);
                if (lower == 'a' || lower == 'e' || lower == 'i' || lower == 'o' || lower == 'u')
                    hasVowel = true;
                else
                    hasConsonant = true;
            } else {
                return false; // invalid character like '@', '#', '$'
            }
        }
        return hasVowel && hasConsonant;
    }
};
```

## Java

```java
class Solution {
    public boolean isValid(String word) {
        if (word == null || word.length() < 3) return false;
        boolean hasVowel = false;
        boolean hasConsonant = false;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (Character.isLetter(c)) {
                char lower = Character.toLowerCase(c);
                if (lower == 'a' || lower == 'e' || lower == 'i' || lower == 'o' || lower == 'u') {
                    hasVowel = true;
                } else {
                    hasConsonant = true;
                }
            } else if (!Character.isDigit(c)) {
                return false; // invalid character
            }
        }
        return hasVowel && hasConsonant;
    }
}
```

## Python

```python
class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) < 3:
            return False

        vowels = set('aeiouAEIOU')
        has_vowel = False
        has_consonant = False

        for ch in word:
            if ch.isalpha():
                if ch in vowels:
                    has_vowel = True
                else:
                    has_consonant = True
            elif ch.isdigit():
                continue
            else:
                # invalid character like '@', '#', '$'
                return False

        return has_vowel and has_consonant
```

## Python3

```python
class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowels = set('aeiouAEIOU')
        has_vowel = False
        has_consonant = False

        for ch in word:
            if ch.isalpha():
                if ch in vowels:
                    has_vowel = True
                else:
                    has_consonant = True
            elif ch.isdigit():
                continue
            else:
                return False  # invalid character

        return has_vowel and has_consonant
```

## C

```c
#include <stdbool.h>
#include <ctype.h>
#include <string.h>

bool isValid(char* word) {
    if (!word) return false;
    size_t n = strlen(word);
    if (n < 3) return false;

    bool hasVowel = false, hasConsonant = false;
    for (size_t i = 0; i < n; ++i) {
        unsigned char c = word[i];
        if (isdigit(c)) {
            continue;
        } else if (isalpha(c)) {
            char lower = tolower(c);
            if (lower == 'a' || lower == 'e' || lower == 'i' || lower == 'o' || lower == 'u')
                hasVowel = true;
            else
                hasConsonant = true;
        } else {
            return false;
        }
    }
    return hasVowel && hasConsonant;
}
```

## Csharp

```csharp
public class Solution {
    public bool IsValid(string word) {
        if (word == null || word.Length < 3) return false;
        bool hasVowel = false, hasConsonant = false;
        foreach (char c in word) {
            if (char.IsLetter(c)) {
                char lower = char.ToLowerInvariant(c);
                if ("aeiou".IndexOf(lower) >= 0) {
                    hasVowel = true;
                } else {
                    hasConsonant = true;
                }
            } else if (!char.IsDigit(c)) {
                return false;
            }
        }
        return hasVowel && hasConsonant;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word
 * @return {boolean}
 */
var isValid = function(word) {
    if (word.length < 3) return false;
    let hasVowel = false, hasConsonant = false;
    for (let i = 0; i < word.length; i++) {
        const ch = word[i];
        if ((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z')) {
            const lower = ch.toLowerCase();
            if ('aeiou'.includes(lower)) hasVowel = true;
            else hasConsonant = true;
        } else if (ch >= '0' && ch <= '9') {
            // digits are allowed but don't affect vowel/consonant flags
        } else {
            return false; // invalid character
        }
    }
    return hasVowel && hasConsonant;
};
```

## Typescript

```typescript
function isValid(word: string): boolean {
    if (word.length < 3) return false;
    const vowels = new Set(['a','e','i','o','u','A','E','I','O','U']);
    let hasVowel = false, hasConsonant = false;
    for (let i = 0; i < word.length; i++) {
        const code = word.charCodeAt(i);
        if (code >= 48 && code <= 57) {
            continue; // digit
        } else if ((code >= 65 && code <= 90) || (code >= 97 && code <= 122)) {
            const ch = word[i];
            if (vowels.has(ch)) hasVowel = true;
            else hasConsonant = true;
        } else {
            return false; // invalid character
        }
    }
    return hasVowel && hasConsonant;
}
```

## Php

```php
class Solution {

    /**
     * @param String $word
     * @return Boolean
     */
    function isValid($word) {
        if (strlen($word) < 3) {
            return false;
        }
        $hasVowel = false;
        $hasConsonant = false;
        $vowels = ['a','e','i','o','u'];
        $len = strlen($word);
        for ($i = 0; $i < $len; $i++) {
            $ch = $word[$i];
            if (!ctype_alnum($ch)) {
                return false;
            }
            if (ctype_alpha($ch)) {
                $lower = strtolower($ch);
                if (in_array($lower, $vowels, true)) {
                    $hasVowel = true;
                } else {
                    $hasConsonant = true;
                }
            }
        }
        return $hasVowel && $hasConsonant;
    }
}
```

## Swift

```swift
class Solution {
    func isValid(_ word: String) -> Bool {
        if word.count < 3 { return false }
        var hasVowel = false
        var hasConsonant = false
        let vowels: Set<Character> = ["a","e","i","o","u","A","E","I","O","U"]
        for ch in word {
            if ch.isNumber {
                continue
            } else if ch.isLetter {
                if vowels.contains(ch) {
                    hasVowel = true
                } else {
                    hasConsonant = true
                }
            } else {
                return false
            }
        }
        return hasVowel && hasConsonant
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isValid(word: String): Boolean {
        if (word.length < 3) return false
        var hasVowel = false
        var hasConsonant = false
        for (ch in word) {
            if (!ch.isLetterOrDigit()) return false
            if (ch.isLetter()) {
                when (ch.lowercaseChar()) {
                    'a', 'e', 'i', 'o', 'u' -> hasVowel = true
                    else -> hasConsonant = true
                }
            }
        }
        return hasVowel && hasConsonant
    }
}
```

## Dart

```dart
class Solution {
  bool isValid(String word) {
    if (word.length < 3) return false;
    bool hasVowel = false, hasConsonant = false;
    const vowels = 'aeiou';
    for (int i = 0; i < word.length; ++i) {
      int code = word.codeUnitAt(i);
      if ((code >= 65 && code <= 90) || (code >= 97 && code <= 122)) {
        String lower = word[i].toLowerCase();
        if (vowels.contains(lower)) {
          hasVowel = true;
        } else {
          hasConsonant = true;
        }
      } else if (code >= 48 && code <= 57) {
        // digit, allowed
      } else {
        return false; // invalid character
      }
    }
    return hasVowel && hasConsonant;
  }
}
```

## Golang

```go
func isValid(word string) bool {
	if len(word) < 3 {
		return false
	}
	hasVowel, hasConsonant := false, false
	for i := 0; i < len(word); i++ {
		c := word[i]
		switch {
		case c >= 'a' && c <= 'z':
			switch c {
			case 'a', 'e', 'i', 'o', 'u':
				hasVowel = true
			default:
				hasConsonant = true
			}
		case c >= 'A' && c <= 'Z':
			switch c {
			case 'A', 'E', 'I', 'O', 'U':
				hasVowel = true
			default:
				hasConsonant = true
			}
		case c >= '0' && c <= '9':
			// digits are allowed but don't affect vowel/consonant flags
		default:
			return false // invalid character
		}
	}
	return hasVowel && hasConsonant
}
```

## Ruby

```ruby
def is_valid(word)
  return false if word.length < 3
  has_vowel = false
  has_consonant = false
  vowels = "aeiouAEIOU"
  word.each_char do |ch|
    if ch =~ /[A-Za-z]/
      if vowels.include?(ch)
        has_vowel = true
      else
        has_consonant = true
      end
    elsif ch =~ /\d/
      # valid digit, continue
    else
      return false
    end
  end
  has_vowel && has_consonant
end
```

## Scala

```scala
object Solution {
    def isValid(word: String): Boolean = {
        if (word.length < 3) return false
        var hasVowel = false
        var hasConsonant = false
        val vowels = Set('a','e','i','o','u','A','E','I','O','U')
        for (c <- word) {
            if (c.isLetterOrDigit) {
                if (c.isLetter) {
                    if (vowels.contains(c)) hasVowel = true
                    else hasConsonant = true
                }
            } else {
                return false
            }
        }
        hasVowel && hasConsonant
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_valid(word: String) -> bool {
        let bytes = word.as_bytes();
        if bytes.len() < 3 {
            return false;
        }
        let mut has_vowel = false;
        let mut has_consonant = false;
        for &c in bytes {
            if c.is_ascii_alphabetic() {
                match c.to_ascii_lowercase() {
                    b'a' | b'e' | b'i' | b'o' | b'u' => has_vowel = true,
                    _ => has_consonant = true,
                }
            } else if c.is_ascii_digit() {
                continue;
            } else {
                return false;
            }
        }
        has_vowel && has_consonant
    }
}
```

## Racket

```racket
(define/contract (is-valid word)
  (-> string? boolean?)
  (let ((len (string-length word)))
    (if (< len 3)
        #f
        (let loop ((i 0) (has-vowel #f) (has-consonant #f))
          (cond
            [(= i len) (and has-vowel has-consonant)]
            [else
             (define ch (string-ref word i))
             (cond
               [(char-alphabetic? ch)
                (if (member (char-downcase ch) '(#\a #\e #\i #\o #\u))
                    (loop (+ i 1) #t has-consonant)
                    (loop (+ i 1) has-vowel #t))]
               [(char-numeric? ch) (loop (+ i 1) has-vowel has-consonant)]
               [else #f])])))))
```

## Erlang

```erlang
-module(solution).
-export([is_valid/1]).

-spec is_valid(Word :: unicode:unicode_binary()) -> boolean().
is_valid(Word) ->
    Len = byte_size(Word),
    if Len < 3 -> false;
       true -> check_chars(Word, false, false)
    end.

check_chars(<<>>, VowelSeen, ConsonantSeen) ->
    VowelSeen andalso ConsonantSeen;
check_chars(<<C, Rest/binary>>, VowelSeen, ConsonantSeen) ->
    case is_allowed(C) of
        true ->
            NewVowel = VowelSeen orelse is_vowel(C),
            NewConsonant = ConsonantSeen orelse (is_letter(C) andalso not is_vowel(C)),
            check_chars(Rest, NewVowel, NewConsonant);
        false -> false
    end.

is_allowed(C) when ($0 =< C, C =< $9); ($A =< C, C =< $Z); ($a =< C, C =< $z) -> true;
is_allowed(_) -> false.

is_letter(C) when ($A =< C, C =< $Z); ($a =< C, C =< $z) -> true;
is_letter(_) -> false.

is_vowel(C) ->
    case C of
        $a; $e; $i; $o; $u; $A; $E; $I; $O; $U -> true;
        _ -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_valid(word :: String.t) :: boolean
  def is_valid(word) do
    if String.length(word) < 3 do
      false
    else
      result =
        word
        |> String.graphemes()
        |> Enum.reduce_while({false, false}, fn ch, {has_vowel, has_consonant} ->
          cond do
            ch =~ ~r/^[A-Za-z0-9]$/ ->
              cond do
                ch =~ ~r/[AEIOUaeiou]/ -> {:cont, {true, has_consonant}}
                ch =~ ~r/[A-Za-z]/ -> {:cont, {has_vowel, true}}
                true -> {:cont, {has_vowel, has_consonant}} # digit
              end

            true ->
              {:halt, :invalid}
          end
        end)

      case result do
        :invalid -> false
        {has_vowel, has_consonant} -> has_vowel and has_consonant
      end
    end
  end
end
```
