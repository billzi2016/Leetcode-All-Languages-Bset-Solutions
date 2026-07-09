# 2124. Check if All A's Appears Before All B's

## Cpp

```cpp
class Solution {
public:
    bool checkString(string s) {
        bool seenB = false;
        for (char c : s) {
            if (c == 'b') {
                seenB = true;
            } else { // c == 'a'
                if (seenB) return false;
            }
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean checkString(String s) {
        boolean seenB = false;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == 'b') {
                seenB = true;
            } else { // c == 'a'
                if (seenB) {
                    return false;
                }
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return "ba" not in s
```

## Python3

```python
class Solution:
    def checkString(self, s: str) -> bool:
        return "ba" not in s
```

## C

```c
#include <stdbool.h>

bool checkString(char* s) {
    bool seenB = false;
    for (int i = 0; s[i] != '\0'; ++i) {
        if (s[i] == 'b') {
            seenB = true;
        } else { // s[i] == 'a'
            if (seenB) return false;
        }
    }
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool CheckString(string s) {
        bool seenB = false;
        foreach (char c in s) {
            if (c == 'b') {
                seenB = true;
            } else { // c == 'a'
                if (seenB) return false;
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
var checkString = function(s) {
    let seenB = false;
    for (let ch of s) {
        if (ch === 'b') {
            seenB = true;
        } else { // ch === 'a'
            if (seenB) return false;
        }
    }
    return true;
};
```

## Typescript

```typescript
function checkString(s: string): boolean {
    let bSeen = false;
    for (const ch of s) {
        if (ch === 'b') {
            bSeen = true;
        } else { // ch === 'a'
            if (bSeen) return false;
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
    function checkString($s) {
        return strpos($s, "ba") === false;
    }
}
```

## Swift

```swift
class Solution {
    func checkString(_ s: String) -> Bool {
        var seenB = false
        for ch in s {
            if ch == "b" {
                seenB = true
            } else { // ch == 'a'
                if seenB {
                    return false
                }
            }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun checkString(s: String): Boolean {
        return !s.contains("ba")
    }
}
```

## Dart

```dart
class Solution {
  bool checkString(String s) {
    return !s.contains('ba');
  }
}
```

## Golang

```go
func checkString(s string) bool {
    seenB := false
    for _, ch := range s {
        if ch == 'b' {
            seenB = true
        } else { // ch == 'a'
            if seenB {
                return false
            }
        }
    }
    return true
}
```

## Ruby

```ruby
# @param {String} s
# @return {Boolean}
def check_string(s)
  !s.include?('ba')
end
```

## Scala

```scala
object Solution {
    def checkString(s: String): Boolean = {
        !s.contains("ba")
    }
}
```

## Rust

```rust
impl Solution {
    pub fn check_string(s: String) -> bool {
        !s.contains("ba")
    }
}
```

## Racket

```racket
(define/contract (check-string s)
  (-> string? boolean?)
  (let loop ((i 0) (seen-b? #f))
    (if (= i (string-length s))
        #t
        (let ((ch (string-ref s i)))
          (cond [(char=? ch #\b) (loop (+ i 1) #t)]
                [(char=? ch #\a)
                 (if seen-b?
                     #f
                     (loop (+ i 1) seen-b?))]
                [else (loop (+ i 1) seen-b?)])))))
```

## Erlang

```erlang
-module(solution).
-export([check_string/1]).

-spec check_string(S :: unicode:unicode_binary()) -> boolean().
check_string(S) ->
    check_bin(S, false).

-spec check_bin(binary(), boolean()) -> boolean().
check_bin(<<>>, _) -> 
    true;
check_bin(<<$a, Rest/binary>>, SeenB) ->
    case SeenB of
        true -> false;
        false -> check_bin(Rest, false)
    end;
check_bin(<<$b, Rest/binary>>, _SeenB) ->
    check_bin(Rest, true).
```

## Elixir

```elixir
defmodule Solution do
  @spec check_string(s :: String.t) :: boolean
  def check_string(s) do
    not String.contains?(s, "ba")
  end
end
```
