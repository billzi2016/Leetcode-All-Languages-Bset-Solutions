# 0125. Valid Palindrome

## Cpp

```cpp
class Solution {
public:
    bool isPalindrome(string s) {
        int i = 0, j = (int)s.size() - 1;
        while (i < j) {
            while (i < j && !isalnum(static_cast<unsigned char>(s[i]))) ++i;
            while (i < j && !isalnum(static_cast<unsigned char>(s[j]))) --j;
            if (i < j) {
                char a = tolower(static_cast<unsigned char>(s[i]));
                char b = tolower(static_cast<unsigned char>(s[j]));
                if (a != b) return false;
                ++i;
                --j;
            }
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean isPalindrome(String s) {
        int i = 0, j = s.length() - 1;
        while (i < j) {
            char left = s.charAt(i);
            char right = s.charAt(j);
            if (!Character.isLetterOrDigit(left)) {
                i++;
                continue;
            }
            if (!Character.isLetterOrDigit(right)) {
                j--;
                continue;
            }
            if (Character.toLowerCase(left) != Character.toLowerCase(right)) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        return True
```

## Python3

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        return True
```

## C

```c
#include <stdbool.h>
#include <ctype.h>
#include <string.h>

bool isPalindrome(char* s) {
    int left = 0;
    int right = (int)strlen(s) - 1;
    while (left < right) {
        while (left < right && !isalnum((unsigned char)s[left])) left++;
        while (left < right && !isalnum((unsigned char)s[right])) right--;
        if (left >= right) break;
        if (tolower((unsigned char)s[left]) != tolower((unsigned char)s[right]))
            return false;
        left++;
        right--;
    }
    return true;
}
```

## Csharp

```csharp
public class Solution
{
    public bool IsPalindrome(string s)
    {
        int left = 0;
        int right = s.Length - 1;

        while (left < right)
        {
            while (left < right && !char.IsLetterOrDigit(s[left]))
                left++;
            while (left < right && !char.IsLetterOrDigit(s[right]))
                right--;

            if (left < right)
            {
                char cLeft = char.ToLowerInvariant(s[left]);
                char cRight = char.ToLowerInvariant(s[right]);

                if (cLeft != cRight)
                    return false;

                left++;
                right--;
            }
        }

        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let i = 0, j = s.length - 1;
    const isAlphaNum = (c) => {
        return (c >= 48 && c <= 57) || (c >= 65 && c <= 90) || (c >= 97 && c <= 122);
    };
    const toLower = (c) => {
        if (c >= 65 && c <= 90) return c + 32;
        return c;
    };
    while (i < j) {
        let ci = s.charCodeAt(i);
        while (i < j && !isAlphaNum(ci)) {
            i++;
            ci = s.charCodeAt(i);
        }
        let cj = s.charCodeAt(j);
        while (i < j && !isAlphaNum(cj)) {
            j--;
            cj = s.charCodeAt(j);
        }
        if (i < j) {
            if (toLower(ci) !== toLower(cj)) return false;
            i++;
            j--;
        }
    }
    return true;
};
```

## Typescript

```typescript
function isPalindrome(s: string): boolean {
    const isAlphaNum = (c: string): boolean => {
        const code = c.charCodeAt(0);
        return (
            (code >= 48 && code <= 57) || // '0'-'9'
            (code >= 65 && code <= 90) || // 'A'-'Z'
            (code >= 97 && code <= 122)   // 'a'-'z'
        );
    };
    const toLower = (code: number): number => {
        return code >= 65 && code <= 90 ? code + 32 : code;
    };

    let i = 0, j = s.length - 1;
    while (i < j) {
        while (i < j && !isAlphaNum(s[i])) i++;
        while (i < j && !isAlphaNum(s[j])) j--;
        if (i < j) {
            const leftCode = toLower(s.charCodeAt(i));
            const rightCode = toLower(s.charCodeAt(j));
            if (leftCode !== rightCode) return false;
            i++;
            j--;
        }
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function isPalindrome($s) {
        $left = 0;
        $right = strlen($s) - 1;

        while ($left < $right) {
            while ($left < $right && !ctype_alnum($s[$left])) {
                $left++;
            }
            while ($left < $right && !ctype_alnum($s[$right])) {
                $right--;
            }

            if (strtolower($s[$left]) !== strtolower($s[$right])) {
                return false;
            }

            $left++;
            $right--;
        }

        return true;
    }
}
```

## Swift

```swift
class Solution {
    func isPalindrome(_ s: String) -> Bool {
        let chars = Array(s.lowercased())
        var i = 0
        var j = chars.count - 1
        
        while i < j {
            while i < j && !isAlnum(chars[i]) { i += 1 }
            while i < j && !isAlnum(chars[j]) { j -= 1 }
            if i < j {
                if chars[i] != chars[j] { return false }
                i += 1
                j -= 1
            }
        }
        return true
    }
    
    private func isAlnum(_ c: Character) -> Bool {
        guard let v = c.unicodeScalars.first?.value else { return false }
        // '0'..'9' => 48...57, 'a'..'z' => 97...122
        return (v >= 48 && v <= 57) || (v >= 97 && v <= 122)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isPalindrome(s: String): Boolean {
        var left = 0
        var right = s.length - 1
        while (left < right) {
            while (left < right && !s[left].isLetterOrDigit()) left++
            while (left < right && !s[right].isLetterOrDigit()) right--
            if (left < right) {
                if (s[left].lowercaseChar() != s[right].lowercaseChar()) return false
                left++
                right--
            }
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool isPalindrome(String s) {
    int left = 0;
    int right = s.length - 1;

    while (left < right) {
      while (left < right && !_isAlphaNumeric(s.codeUnitAt(left))) {
        left++;
      }
      while (left < right && !_isAlphaNumeric(s.codeUnitAt(right))) {
        right--;
      }
      if (left < right) {
        String lChar = s[left].toLowerCase();
        String rChar = s[right].toLowerCase();
        if (lChar != rChar) return false;
        left++;
        right--;
      }
    }
    return true;
  }

  bool _isAlphaNumeric(int code) {
    return (code >= 48 && code <= 57) || // '0'-'9'
        (code >= 65 && code <= 90) ||   // 'A'-'Z'
        (code >= 97 && code <= 122);    // 'a'-'z'
  }
}
```

## Golang

```go
func isAlnum(b byte) bool {
	if (b >= 'a' && b <= 'z') || (b >= 'A' && b <= 'Z') || (b >= '0' && b <= '9') {
		return true
	}
	return false
}

func isPalindrome(s string) bool {
	i, j := 0, len(s)-1
	for i < j {
		for i < j && !isAlnum(s[i]) {
			i++
		}
		for i < j && !isAlnum(s[j]) {
			j--
		}
		if i >= j {
			break
		}
		ci, cj := s[i], s[j]
		if ci >= 'A' && ci <= 'Z' {
			ci += 32
		}
		if cj >= 'A' && cj <= 'Z' {
			cj += 32
		}
		if ci != cj {
			return false
		}
		i++
		j--
	}
	return true
}
```

## Ruby

```ruby
def is_palindrome(s)
  i = 0
  j = s.length - 1
  while i < j
    while i < j && !(s[i] =~ /[A-Za-z0-9]/)
      i += 1
    end
    while i < j && !(s[j] =~ /[A-Za-z0-9]/)
      j -= 1
    end
    break if i >= j
    return false unless s[i].downcase == s[j].downcase
    i += 1
    j -= 1
  end
  true
end
```

## Scala

```scala
object Solution {
    def isPalindrome(s: String): Boolean = {
        var i = 0
        var j = s.length - 1
        while (i < j) {
            while (i < j && !s.charAt(i).isLetterOrDigit) i += 1
            while (i < j && !s.charAt(j).isLetterOrDigit) j -= 1
            if (i < j) {
                val left = s.charAt(i).toLower
                val right = s.charAt(j).toLower
                if (left != right) return false
                i += 1
                j -= 1
            }
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let bytes = s.as_bytes();
        if bytes.is_empty() {
            return true;
        }
        let mut left: usize = 0;
        let mut right: usize = bytes.len() - 1;

        while left < right {
            while left < right && !bytes[left].is_ascii_alphanumeric() {
                left += 1;
            }
            while left < right && !bytes[right].is_ascii_alphanumeric() {
                if right == 0 { break; }
                right -= 1;
            }
            if left >= right {
                break;
            }
            let l = bytes[left].to_ascii_lowercase();
            let r = bytes[right].to_ascii_lowercase();
            if l != r {
                return false;
            }
            left += 1;
            if right == 0 { break; }
            right -= 1;
        }
        true
    }
}
```

## Racket

```racket
(define/contract (is-palindrome s)
  (-> string? boolean?)
  (let ((len (string-length s)))
    (let loop ((i 0) (j (- len 1)))
      (cond
        [(>= i j) #t]
        [else
         (let* ((ci (string-ref s i))
                (cj (string-ref s j)))
           (cond
             [(not (or (char-alphabetic? ci) (char-numeric? ci))) (loop (+ i 1) j)]
             [(not (or (char-alphabetic? cj) (char-numeric? cj))) (loop i (- j 1))]
             [else (if (char=? (char-downcase ci) (char-downcase cj))
                       (loop (+ i 1) (- j 1))
                       #f)]))]))))
```

## Erlang

```erlang
-module(solution).
-export([is_palindrome/1]).

-spec is_palindrome(S :: unicode:unicode_binary()) -> boolean().
is_palindrome(S) ->
    Chars = unicode:characters_to_list(S),
    Filtered = [lower(C) || C <- Chars, is_alnum(C)],
    Filtered == lists:reverse(Filtered).

lower(C) when $A =< C, C =< $Z -> C + 32;
lower(C) -> C.

is_alnum(C) when $0 =< C, C =< $9 -> true;
is_alnum(C) when $a =< C, C =< $z -> true;
is_alnum(C) when $A =< C, C =< $Z -> true;
is_alnum(_) -> false.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_palindrome(s :: String.t) :: boolean
  def is_palindrome(s) do
    filtered =
      s
      |> String.to_charlist()
      |> Enum.reduce([], fn c, acc ->
        cond do
          c >= ?a and c <= ?z -> [c | acc]
          c >= ?0 and c <= ?9 -> [c | acc]
          c >= ?A and c <= ?Z -> [(c + 32) | acc]
          true -> acc
        end
      end)
      |> Enum.reverse()

    filtered == Enum.reverse(filtered)
  end
end
```
