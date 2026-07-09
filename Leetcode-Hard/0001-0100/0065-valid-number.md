# 0065. Valid Number

## Cpp

```cpp
class Solution {
public:
    bool isNumber(string s) {
        int n = s.size();
        int i = 0, j = n - 1;
        while (i <= j && isspace(s[i])) ++i;
        while (j >= i && isspace(s[j])) --j;
        if (i > j) return false;

        bool seenDigit = false, seenDot = false, seenExp = false;
        for (int k = i; k <= j; ++k) {
            char c = s[k];
            if (isdigit(c)) {
                seenDigit = true;
            } else if (c == '+' || c == '-') {
                if (k != i && !(s[k - 1] == 'e' || s[k - 1] == 'E')) return false;
            } else if (c == '.') {
                if (seenDot || seenExp) return false;
                seenDot = true;
            } else if (c == 'e' || c == 'E') {
                if (seenExp || !seenDigit) return false;
                seenExp = true;
                seenDigit = false; // need a digit after exponent
            } else {
                return false;
            }
        }
        return seenDigit;
    }
};
```

## Java

```java
class Solution {
    public boolean isNumber(String s) {
        if (s == null) return false;
        s = s.trim();
        int n = s.length();
        if (n == 0) return false;

        boolean numSeen = false;
        boolean dotSeen = false;
        boolean expSeen = false;

        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (c >= '0' && c <= '9') {
                numSeen = true;
            } else if (c == '+' || c == '-') {
                // sign must be at start or just after an exponent
                if (i != 0) {
                    char prev = s.charAt(i - 1);
                    if (prev != 'e' && prev != 'E') return false;
                }
            } else if (c == 'e' || c == 'E') {
                // exponent must not have appeared before and there must be a number before it
                if (expSeen || !numSeen) return false;
                expSeen = true;
                numSeen = false; // need at least one digit after exponent
            } else if (c == '.') {
                // dot cannot appear after exponent or another dot
                if (dotSeen || expSeen) return false;
                dotSeen = true;
            } else {
                return false;
            }
        }
        return numSeen;
    }
}
```

## Python

```python
import re

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        pattern = re.compile(r'^[\+\-]?((\d+\.?\d*)|(\.\d+))([eE][\+\-]?\d+)?$')
        return bool(pattern.fullmatch(s))
```

## Python3

```python
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False

        seen_digit = False
        seen_dot = False
        seen_exp = False

        for i, ch in enumerate(s):
            if ch.isdigit():
                seen_digit = True
            elif ch in '+-':
                # sign must be at start or just after an exponent
                if i != 0 and s[i - 1] not in 'eE':
                    return False
            elif ch == '.':
                if seen_dot or seen_exp:
                    return False
                seen_dot = True
            elif ch in 'eE':
                if seen_exp or not seen_digit:
                    return False
                seen_exp = True
                seen_digit = False  # need at least one digit after exponent
            else:
                return False

        return seen_digit
```

## C

```c
#include <stdbool.h>
#include <ctype.h>
#include <string.h>

bool isNumber(char* s) {
    int n = (int)strlen(s);
    int i = 0;
    while (i < n && isspace((unsigned char)s[i])) i++;
    int j = n - 1;
    while (j >= i && isspace((unsigned char)s[j])) j--;
    if (i > j) return false;

    bool numSeen = false, dotSeen = false, eSeen = false, numAfterE = true;

    for (int k = i; k <= j; ++k) {
        char c = s[k];
        if (c >= '0' && c <= '9') {
            numSeen = true;
            if (eSeen) numAfterE = true;
        } else if (c == '+' || c == '-') {
            if (k == i) continue;
            if (s[k - 1] == 'e' || s[k - 1] == 'E') continue;
            return false;
        } else if (c == '.') {
            if (dotSeen || eSeen) return false;
            dotSeen = true;
        } else if (c == 'e' || c == 'E') {
            if (eSeen || !numSeen) return false;
            eSeen = true;
            numAfterE = false; // must have a digit after e
        } else {
            return false;
        }
    }

    if (!numSeen) return false;
    if (eSeen && !numAfterE) return false;
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool IsNumber(string s) {
        if (s == null) return false;
        s = s.Trim();
        int n = s.Length;
        if (n == 0) return false;

        bool seenDigit = false;
        bool seenDot = false;
        bool seenExp = false;

        for (int i = 0; i < n; i++) {
            char c = s[i];
            if (c >= '0' && c <= '9') {
                seenDigit = true;
            } else if (c == '+' || c == '-') {
                // sign must be at start or just after exponent
                if (i != 0 && !(s[i - 1] == 'e' || s[i - 1] == 'E')) {
                    return false;
                }
            } else if (c == '.') {
                // dot cannot appear after exponent and only once
                if (seenDot || seenExp) {
                    return false;
                }
                seenDot = true;
            } else if (c == 'e' || c == 'E') {
                // exponent cannot appear twice, must follow a digit, and not at end
                if (seenExp || !seenDigit) {
                    return false;
                }
                seenExp = true;
                seenDigit = false; // need at least one digit after exponent
            } else {
                return false;
            }
        }

        return seenDigit;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {boolean}
 */
var isNumber = function(s) {
    s = s.trim();
    const n = s.length;
    if (n === 0) return false;
    
    let numSeen = false;      // digit before 'e' or overall
    let dotSeen = false;      // '.' encountered
    let eSeen = false;        // 'e' or 'E' encountered
    let numAfterE = true;     // at least one digit after 'e' if it exists
    
    for (let i = 0; i < n; i++) {
        const c = s[i];
        if (c >= '0' && c <= '9') {
            numSeen = true;
            if (eSeen) numAfterE = true;
        } else if (c === '+' || c === '-') {
            // sign must be at start or just after an exponent
            if (i !== 0 && s[i - 1] !== 'e' && s[i - 1] !== 'E') return false;
        } else if (c === '.') {
            if (dotSeen || eSeen) return false;
            dotSeen = true;
        } else if (c === 'e' || c === 'E') {
            if (eSeen || !numSeen) return false;
            eSeen = true;
            numAfterE = false; // need a digit after exponent
        } else {
            return false;
        }
    }
    
    return numSeen && (!eSeen || numAfterE);
};
```

## Typescript

```typescript
function isNumber(s: string): boolean {
    s = s.trim();
    const n = s.length;
    if (n === 0) return false;

    let seenDigit = false;
    let seenDot = false;
    let seenExp = false;

    for (let i = 0; i < n; i++) {
        const c = s[i];
        if (c >= '0' && c <= '9') {
            seenDigit = true;
        } else if (c === '+' || c === '-') {
            if (i !== 0) {
                const prev = s[i - 1];
                if (prev !== 'e' && prev !== 'E') return false;
            }
        } else if (c === '.') {
            if (seenDot || seenExp) return false;
            seenDot = true;
        } else if (c === 'e' || c === 'E') {
            if (seenExp || !seenDigit) return false;
            seenExp = true;
            seenDigit = false; // need at least one digit after exponent
        } else {
            return false;
        }
    }

    return seenDigit;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function isNumber($s) {
        $s = trim($s);
        if ($s === '') return false;
        return preg_match('/^[\+\-]?((\d+(\.\d*)?)|(\.\d+))(e[\+\-]?\d+)?$/i', $s) === 1;
    }
}
```

## Swift

```swift
class Solution {
    func isNumber(_ s: String) -> Bool {
        let str = s.trimmingCharacters(in: .whitespaces)
        if str.isEmpty { return false }
        
        var seenDigit = false
        var seenDot = false
        var seenExp = false
        
        let chars = Array(str)
        for i in 0..<chars.count {
            let c = chars[i]
            if c >= "0" && c <= "9" {
                seenDigit = true
            } else if c == "+" || c == "-" {
                if i != 0 && !(chars[i - 1] == "e" || chars[i - 1] == "E") {
                    return false
                }
            } else if c == "." {
                if seenDot || seenExp {
                    return false
                }
                seenDot = true
            } else if c == "e" || c == "E" {
                if seenExp || !seenDigit {
                    return false
                }
                seenExp = true
                seenDigit = false // need at least one digit after exponent
            } else {
                return false
            }
        }
        return seenDigit
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isNumber(s: String): Boolean {
        val str = s.trim()
        if (str.isEmpty()) return false

        var seenDigit = false
        var seenDot = false
        var seenExp = false

        for (i in str.indices) {
            when (val c = str[i]) {
                in '0'..'9' -> seenDigit = true
                '+', '-' -> {
                    if (i != 0 && str[i - 1] != 'e' && str[i - 1] != 'E') return false
                }
                '.' -> {
                    if (seenDot || seenExp) return false
                    seenDot = true
                }
                'e', 'E' -> {
                    if (seenExp || !seenDigit) return false
                    seenExp = true
                    seenDigit = false // need at least one digit after exponent
                }
                else -> return false
            }
        }
        return seenDigit
    }
}
```

## Dart

```dart
class Solution {
  bool isNumber(String s) {
    s = s.trim();
    if (s.isEmpty) return false;
    final RegExp pattern = RegExp(r'^[\+\-]?((\d+(\.\d*)?)|(\.\d+))([eE][\+\-]?\d+)?$');
    return pattern.hasMatch(s);
  }
}
```

## Golang

```go
import "strings"

func isNumber(s string) bool {
	s = strings.TrimSpace(s)
	if len(s) == 0 {
		return false
	}
	seenDigit, seenDot, seenExp := false, false, false

	for i, ch := range s {
		switch {
		case ch >= '0' && ch <= '9':
			seenDigit = true
		case ch == '+' || ch == '-':
			if i != 0 && !(s[i-1] == 'e' || s[i-1] == 'E') {
				return false
			}
		case ch == '.':
			if seenDot || seenExp {
				return false
			}
			seenDot = true
		case ch == 'e' || ch == 'E':
			if seenExp || !seenDigit {
				return false
			}
			seenExp = true
			seenDigit = false // need at least one digit after exponent
		default:
			return false
		}
	}
	return seenDigit
}
```

## Ruby

```ruby
def is_number(s)
  s = s.strip
  !!(s =~ /\A[+-]?((\d+(\.\d*)?)|(\.\d+))(e[+-]?\d+)?\z/i)
end
```

## Scala

```scala
object Solution {
    def isNumber(s: String): Boolean = {
        val str = s.trim
        if (str.isEmpty) return false

        var seenDigit = false
        var seenDot = false
        var seenExp = false
        var digitAfterExp = true // true by default, will set to false when e appears

        for (i <- 0 until str.length) {
            val c = str.charAt(i)
            if (c >= '0' && c <= '9') {
                seenDigit = true
                if (seenExp) digitAfterExp = true
            } else if (c == '+' || c == '-') {
                if (i != 0 && !(str.charAt(i - 1) == 'e' || str.charAt(i - 1) == 'E')) return false
            } else if (c == '.') {
                if (seenDot || seenExp) return false
                seenDot = true
            } else if (c == 'e' || c == 'E') {
                if (seenExp || !seenDigit) return false
                seenExp = true
                digitAfterExp = false // need at least one digit after exponent
            } else {
                return false
            }
        }

        seenDigit && (!seenExp || digitAfterExp)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_number(s: String) -> bool {
        let s = s.trim();
        if s.is_empty() {
            return false;
        }
        let chars: Vec<char> = s.chars().collect();
        let mut has_num = false;
        let mut has_dot = false;
        let mut has_exp = false;
        let mut num_after_exp = true; // true unless we see an exponent without following digit

        for i in 0..chars.len() {
            match chars[i] {
                '0'..='9' => {
                    has_num = true;
                    if has_exp {
                        num_after_exp = true;
                    }
                }
                '+' | '-' => {
                    if i != 0 && !matches!(chars[i - 1], 'e' | 'E') {
                        return false;
                    }
                }
                '.' => {
                    if has_dot || has_exp {
                        return false;
                    }
                    has_dot = true;
                }
                'e' | 'E' => {
                    if has_exp || !has_num {
                        return false;
                    }
                    has_exp = true;
                    num_after_exp = false; // need at least one digit after exponent
                }
                _ => return false,
            }
        }

        has_num && (!has_exp || num_after_exp)
    }
}
```

## Racket

```racket
(define/contract (is-number s)
  (-> string? boolean?)
  (let ([pattern "^\\s*[+-]?((([0-9]+)(\\.[0-9]*)?)|(\\.[0-9]+))([eE][+-]?[0-9]+)?\\s*$"])
    (regexp-match? pattern s)))
```

## Erlang

```erlang
-spec is_number(S :: unicode:unicode_binary()) -> boolean().
is_number(S) ->
    Str = string:trim(S),
    case re:run(Str,
                "^[\\+\\-]?((\\d+(\\.\\d*)?)|(\\.\\d+))([eE][\\+\\-]?\\d+)?$",
                [{capture, none}]) of
        match -> true;
        nomatch -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_number(s :: String.t()) :: boolean()
  def is_number(s) do
    parse(String.to_charlist(s), true, false, false, false, false)
  end

  defp parse([], _allow_sign, has_num, _has_dot, has_exp, exp_has_digit) do
    has_num and (not has_exp or exp_has_digit)
  end

  defp parse([c | rest], allow_sign, has_num, has_dot, has_exp, exp_has_digit) do
    cond do
      c in ?0..?9 ->
        if has_exp do
          parse(rest, false, has_num, has_dot, true, true)
        else
          parse(rest, false, true, has_dot, false, exp_has_digit)
        end

      c == ?. ->
        if has_dot or has_exp do
          false
        else
          parse(rest, false, has_num, true, has_exp, exp_has_digit)
        end

      c == ?e or c == ?E ->
        if has_exp or not has_num do
          false
        else
          parse(rest, true, has_num, has_dot, true, false)
        end

      c == ?+ or c == ?- ->
        if allow_sign do
          parse(rest, false, has_num, has_dot, has_exp, exp_has_digit)
        else
          false
        end

      true ->
        false
    end
  end
end
```
