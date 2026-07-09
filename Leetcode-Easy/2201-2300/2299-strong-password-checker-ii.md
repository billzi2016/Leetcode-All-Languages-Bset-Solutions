# 2299. Strong Password Checker II

## Cpp

```cpp
class Solution {
public:
    bool strongPasswordCheckerII(string password) {
        if (password.size() < 8) return false;
        bool hasLower = false, hasUpper = false, hasDigit = false, hasSpecial = false;
        const string specials = "!@#$%^&*()-+";
        for (size_t i = 0; i < password.size(); ++i) {
            char c = password[i];
            if (islower(c)) hasLower = true;
            else if (isupper(c)) hasUpper = true;
            else if (isdigit(c)) hasDigit = true;
            else if (specials.find(c) != string::npos) hasSpecial = true;
            
            if (i > 0 && password[i] == password[i-1]) return false;
        }
        return hasLower && hasUpper && hasDigit && hasSpecial;
    }
};
```

## Java

```java
class Solution {
    public boolean strongPasswordCheckerII(String password) {
        if (password.length() < 8) return false;
        boolean hasLower = false, hasUpper = false, hasDigit = false, hasSpecial = false;
        String specials = "!@#$%^&*()-+";
        for (int i = 0; i < password.length(); i++) {
            char c = password.charAt(i);
            if (i > 0 && c == password.charAt(i - 1)) return false;
            if (c >= 'a' && c <= 'z') hasLower = true;
            else if (c >= 'A' && c <= 'Z') hasUpper = true;
            else if (c >= '0' && c <= '9') hasDigit = true;
            else if (specials.indexOf(c) != -1) hasSpecial = true;
        }
        return hasLower && hasUpper && hasDigit && hasSpecial;
    }
}
```

## Python

```python
class Solution(object):
    def strongPasswordCheckerII(self, password):
        """
        :type password: str
        :rtype: bool
        """
        if len(password) < 8:
            return False

        has_lower = has_upper = has_digit = has_special = False
        specials = set("!@#$%^&*()-+")
        prev_char = None

        for ch in password:
            if ch.islower():
                has_lower = True
            elif ch.isupper():
                has_upper = True
            elif ch.isdigit():
                has_digit = True

            if ch in specials:
                has_special = True

            if prev_char == ch:
                return False
            prev_char = ch

        return has_lower and has_upper and has_digit and has_special
```

## Python3

```python
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        specials = set("!@#$%^&*()-+")
        has_lower = has_upper = has_digit = has_special = False
        prev_char = None
        for ch in password:
            if ch.islower():
                has_lower = True
            elif ch.isupper():
                has_upper = True
            elif ch.isdigit():
                has_digit = True
            if ch in specials:
                has_special = True
            if prev_char is not None and ch == prev_char:
                return False
            prev_char = ch
        return has_lower and has_upper and has_digit and has_special
```

## C

```c
#include <stdbool.h>
#include <string.h>

bool strongPasswordCheckerII(char* password) {
    int n = strlen(password);
    if (n < 8) return false;

    bool hasLower = false, hasUpper = false, hasDigit = false, hasSpecial = false;
    const char *specials = "!@#$%^&*()-+";

    for (int i = 0; i < n; ++i) {
        char c = password[i];
        if (c >= 'a' && c <= 'z') hasLower = true;
        else if (c >= 'A' && c <= 'Z') hasUpper = true;
        else if (c >= '0' && c <= '9') hasDigit = true;
        else if (strchr(specials, c)) hasSpecial = true;

        if (i > 0 && password[i] == password[i - 1]) return false;
    }

    return hasLower && hasUpper && hasDigit && hasSpecial;
}
```

## Csharp

```csharp
public class Solution {
    public bool StrongPasswordCheckerII(string password) {
        if (password.Length < 8) return false;

        bool hasLower = false, hasUpper = false, hasDigit = false, hasSpecial = false;
        const string specials = "!@#$%^&*()-+";

        for (int i = 0; i < password.Length; i++) {
            char c = password[i];

            if (i > 0 && c == password[i - 1]) return false;

            if (char.IsLower(c)) hasLower = true;
            else if (char.IsUpper(c)) hasUpper = true;
            else if (char.IsDigit(c)) hasDigit = true;
            else if (specials.IndexOf(c) >= 0) hasSpecial = true;
        }

        return hasLower && hasUpper && hasDigit && hasSpecial;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} password
 * @return {boolean}
 */
var strongPasswordCheckerII = function(password) {
    if (password.length < 8) return false;
    const specials = new Set(['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']);
    let hasLower = false, hasUpper = false, hasDigit = false, hasSpecial = false;
    for (let i = 0; i < password.length; i++) {
        const c = password[i];
        if (c >= 'a' && c <= 'z') hasLower = true;
        else if (c >= 'A' && c <= 'Z') hasUpper = true;
        else if (c >= '0' && c <= '9') hasDigit = true;
        else if (specials.has(c)) hasSpecial = true;
        if (i > 0 && password[i] === password[i - 1]) return false;
    }
    return hasLower && hasUpper && hasDigit && hasSpecial;
};
```

## Typescript

```typescript
function strongPasswordCheckerII(password: string): boolean {
    if (password.length < 8) return false;
    const specialChars = "!@#$%^&*()-+";
    let hasLower = false, hasUpper = false, hasDigit = false, hasSpecial = false;

    for (let i = 0; i < password.length; i++) {
        const ch = password[i];

        if (i > 0 && ch === password[i - 1]) return false;

        if (ch >= 'a' && ch <= 'z') {
            hasLower = true;
        } else if (ch >= 'A' && ch <= 'Z') {
            hasUpper = true;
        } else if (ch >= '0' && ch <= '9') {
            hasDigit = true;
        } else if (specialChars.includes(ch)) {
            hasSpecial = true;
        }
    }

    return hasLower && hasUpper && hasDigit && hasSpecial;
}
```

## Php

```php
class Solution {

    /**
     * @param String $password
     * @return Boolean
     */
    function strongPasswordCheckerII($password) {
        if (strlen($password) < 8) {
            return false;
        }
        $hasLower = false;
        $hasUpper = false;
        $hasDigit = false;
        $hasSpecial = false;
        $specialChars = '!@#$%^&*()-+';
        $prevChar = '';
        $len = strlen($password);
        for ($i = 0; $i < $len; $i++) {
            $c = $password[$i];
            if (ctype_lower($c)) {
                $hasLower = true;
            } elseif (ctype_upper($c)) {
                $hasUpper = true;
            } elseif (ctype_digit($c)) {
                $hasDigit = true;
            } else {
                if (strpos($specialChars, $c) !== false) {
                    $hasSpecial = true;
                }
            }
            if ($i > 0 && $c === $prevChar) {
                return false;
            }
            $prevChar = $c;
        }
        return $hasLower && $hasUpper && $hasDigit && $hasSpecial;
    }
}
```

## Swift

```swift
class Solution {
    func strongPasswordCheckerII(_ password: String) -> Bool {
        if password.count < 8 { return false }
        
        var hasLower = false
        var hasUpper = false
        var hasDigit = false
        var hasSpecial = false
        let specials: Set<Character> = Set("!@#$%^&*()-+")
        var prevChar: Character? = nil
        
        for ch in password {
            if let prev = prevChar, prev == ch { return false }
            
            let scalar = ch.unicodeScalars.first!.value
            if scalar >= 97 && scalar <= 122 {          // a-z
                hasLower = true
            } else if scalar >= 65 && scalar <= 90 {    // A-Z
                hasUpper = true
            } else if scalar >= 48 && scalar <= 57 {    // 0-9
                hasDigit = true
            } else if specials.contains(ch) {
                hasSpecial = true
            }
            
            prevChar = ch
        }
        
        return hasLower && hasUpper && hasDigit && hasSpecial
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun strongPasswordCheckerII(password: String): Boolean {
        if (password.length < 8) return false
        var hasLower = false
        var hasUpper = false
        var hasDigit = false
        var hasSpecial = false
        val specials = setOf('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+')
        for (i in password.indices) {
            val c = password[i]
            if (c.isLowerCase()) hasLower = true
            else if (c.isUpperCase()) hasUpper = true
            else if (c.isDigit()) hasDigit = true
            else if (c in specials) hasSpecial = true

            if (i > 0 && c == password[i - 1]) return false
        }
        return hasLower && hasUpper && hasDigit && hasSpecial
    }
}
```

## Dart

```dart
class Solution {
  bool strongPasswordCheckerII(String password) {
    if (password.length < 8) return false;
    const String specials = "!@#\$%^&*()-+";
    bool hasLower = false, hasUpper = false, hasDigit = false, hasSpecial = false;

    for (int i = 0; i < password.length; i++) {
      if (i > 0 && password[i] == password[i - 1]) return false;
      int code = password.codeUnitAt(i);
      if (code >= 97 && code <= 122) {
        hasLower = true;
      } else if (code >= 65 && code <= 90) {
        hasUpper = true;
      } else if (code >= 48 && code <= 57) {
        hasDigit = true;
      } else if (specials.contains(password[i])) {
        hasSpecial = true;
      }
    }

    return hasLower && hasUpper && hasDigit && hasSpecial;
  }
}
```

## Golang

```go
func strongPasswordCheckerII(password string) bool {
	if len(password) < 8 {
		return false
	}
	hasLower, hasUpper, hasDigit, hasSpecial := false, false, false, false
	specials := map[byte]bool{
		'!': true, '@': true, '#': true, '$': true, '%': true,
		'^': true, '&': true, '*': true, '(': true, ')': true,
		'-': true, '+': true,
	}
	var prev byte
	for i := 0; i < len(password); i++ {
		c := password[i]
		if i > 0 && c == prev {
			return false
		}
		switch {
		case 'a' <= c && c <= 'z':
			hasLower = true
		case 'A' <= c && c <= 'Z':
			hasUpper = true
		case '0' <= c && c <= '9':
			hasDigit = true
		default:
			if specials[c] {
				hasSpecial = true
			}
		}
		prev = c
	}
	return hasLower && hasUpper && hasDigit && hasSpecial
}
```

## Ruby

```ruby
def strong_password_checker_ii(password)
  return false if password.length < 8
  has_lower = has_upper = has_digit = has_special = false
  specials = "!@#$%^&*()-+"
  prev = nil
  password.each_char do |ch|
    return false if ch == prev
    prev = ch
    has_lower ||= ('a' <= ch && ch <= 'z')
    has_upper ||= ('A' <= ch && ch <= 'Z')
    has_digit ||= ('0' <= ch && ch <= '9')
    has_special ||= specials.include?(ch)
  end
  has_lower && has_upper && has_digit && has_special
end
```

## Scala

```scala
object Solution {
    def strongPasswordCheckerII(password: String): Boolean = {
        if (password.length < 8) return false
        var hasLower = false
        var hasUpper = false
        var hasDigit = false
        var hasSpecial = false
        val specials = Set('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+')
        for (i <- password.indices) {
            if (i > 0 && password(i) == password(i - 1)) return false
            val c = password(i)
            if (c.isLower) hasLower = true
            else if (c.isUpper) hasUpper = true
            else if (c.isDigit) hasDigit = true
            else if (specials.contains(c)) hasSpecial = true
        }
        hasLower && hasUpper && hasDigit && hasSpecial
    }
}
```

## Rust

```rust
impl Solution {
    pub fn strong_password_checker_ii(password: String) -> bool {
        let bytes = password.as_bytes();
        if bytes.len() < 8 {
            return false;
        }
        let specials = b"!@#$%^&*()-+";
        let mut has_lower = false;
        let mut has_upper = false;
        let mut has_digit = false;
        let mut has_special = false;

        for i in 0..bytes.len() {
            let c = bytes[i];
            if c.is_ascii_lowercase() {
                has_lower = true;
            } else if c.is_ascii_uppercase() {
                has_upper = true;
            } else if c.is_ascii_digit() {
                has_digit = true;
            } else if specials.contains(&c) {
                has_special = true;
            }

            if i > 0 && bytes[i] == bytes[i - 1] {
                return false;
            }
        }

        has_lower && has_upper && has_digit && has_special
    }
}
```

## Racket

```racket
(define/contract (strong-password-checker-ii password)
  (-> string? boolean?)
  (let ((len (string-length password)))
    (if (< len 8)
        #false
        (let loop ((i 0) (prev #f)
                   (has-lower #f) (has-upper #f)
                   (has-digit #f) (has-special #f))
          (if (= i len)
              (and has-lower has-upper has-digit has-special)
              (let* ((c (string-ref password i))
                     (lower? (and (char>=? c #\a) (char<=? c #\z)))
                     (upper? (and (char>=? c #\A) (char<=? c #\Z)))
                     (digit? (and (char>=? c #\0) (char<=? c #\9)))
                     (special? (member c (string->list "!@#$%^&*()-+")))
                     (adjacent? (and prev (char=? c prev))))
                (if adjacent?
                    #false
                    (loop (+ i 1) c
                          (or has-lower lower?)
                          (or has-upper upper?)
                          (or has-digit digit?)
                          (or has-special special?)))))))))
```

## Erlang

```erlang
-module(solution).
-export([strong_password_checker_ii/1]).

-spec strong_password_checker_ii(Password :: unicode:unicode_binary()) -> boolean().
strong_password_checker_ii(Password) ->
    List = unicode:characters_to_list(Password),
    case length(List) >= 8 of
        false -> false;
        true -> check(List, none, {false,false,false,false})
    end.

check([], _Prev, {L,U,D,S}) ->
    L andalso U andalso D andalso S;
check([Char|Rest], Prev, Flags) ->
    case Char == Prev of
        true -> false;
        false ->
            NewFlags = update_flags(Char, Flags),
            check(Rest, Char, NewFlags)
    end.

update_flags(Char, {L,U,D,S}) when Char >= $a, Char =< $z ->
    {true,U,D,S};
update_flags(Char, {L,U,D,S}) when Char >= $A, Char =< $Z ->
    {L,true,D,S};
update_flags(Char, {L,U,D,S}) when Char >= $0, Char =< $9 ->
    {L,U,true,S};
update_flags(Char, Flags) ->
    case is_special(Char) of
        true -> set_special(Flags);
        false -> Flags
    end.

set_special({L,U,D,_}) -> {L,U,D,true}.

is_special(C) ->
    lists:member(C, [$!, $@, $#,$$, $%, $^, $&, $*, $(, $), $-, $+]).
```

## Elixir

```elixir
defmodule Solution do
  @spec strong_password_checker_ii(password :: String.t) :: boolean
  def strong_password_checker_ii(password) do
    if String.length(password) < 8 do
      false
    else
      specials = MapSet.new(["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+"])
      chars = String.graphemes(password)
      check(chars, nil, false, false, false, false, specials)
    end
  end

  defp check([], _prev, lower, upper, digit, special, _specials) do
    lower and upper and digit and special
  end

  defp check([h | t], prev, lower, upper, digit, special, specials) do
    if h == prev do
      false
    else
      new_lower = lower or (h >= "a" and h <= "z")
      new_upper = upper or (h >= "A" and h <= "Z")
      new_digit = digit or (h >= "0" and h <= "9")
      new_special = special or MapSet.member?(specials, h)
      check(t, h, new_lower, new_upper, new_digit, new_special, specials)
    end
  end
end
```
