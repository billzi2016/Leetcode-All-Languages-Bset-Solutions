# 1332. Remove Palindromic Subsequences

## Cpp

```cpp
class Solution {
public:
    int removePalindromeSub(string s) {
        if (s.empty()) return 0;
        int i = 0, j = (int)s.size() - 1;
        while (i < j && s[i] == s[j]) {
            ++i;
            --j;
        }
        return (i >= j) ? 1 : 2;
    }
};
```

## Java

```java
class Solution {
    public int removePalindromeSub(String s) {
        if (s.length() == 0) return 0;
        if (isPalindrome(s)) return 1;
        return 2;
    }
    
    private boolean isPalindrome(String s) {
        int i = 0, j = s.length() - 1;
        while (i < j) {
            if (s.charAt(i) != s.charAt(j)) return false;
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
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if s == s[::-1]:
            return 1
        return 2
```

## Python3

```python
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        if s == s[::-1]:
            return 1
        return 2
```

## C

```c
#include <string.h>

int removePalindromeSub(char* s) {
    if (!s) return 0;
    size_t n = strlen(s);
    if (n == 0) return 0;
    size_t i = 0, j = n - 1;
    while (i < j) {
        if (s[i] != s[j]) return 2;
        ++i;
        --j;
    }
    return 1;
}
```

## Csharp

```csharp
public class Solution
{
    public int RemovePalindromeSub(string s)
    {
        if (s.Length == 0) return 0;

        int i = 0, j = s.Length - 1;
        while (i < j && s[i] == s[j])
        {
            i++;
            j--;
        }

        return (i >= j) ? 1 : 2;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var removePalindromeSub = function(s) {
    if (s.length === 0) return 0;
    const rev = s.split('').reverse().join('');
    return s === rev ? 1 : 2;
};
```

## Typescript

```typescript
function removePalindromeSub(s: string): number {
    if (s.length === 0) return 0;
    let i = 0, j = s.length - 1;
    while (i < j && s[i] === s[j]) {
        i++;
        j--;
    }
    return i >= j ? 1 : 2;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function removePalindromeSub($s) {
        if ($s === "") {
            return 0;
        }
        if ($s === strrev($s)) {
            return 1;
        }
        return 2;
    }
}
```

## Swift

```swift
class Solution {
    func removePalindromeSub(_ s: String) -> Int {
        if s.isEmpty { return 0 }
        let chars = Array(s)
        var i = 0
        var j = chars.count - 1
        var isPal = true
        while i < j {
            if chars[i] != chars[j] {
                isPal = false
                break
            }
            i += 1
            j -= 1
        }
        return isPal ? 1 : 2
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun removePalindromeSub(s: String): Int {
        if (s.isEmpty()) return 0
        var i = 0
        var j = s.length - 1
        while (i < j) {
            if (s[i] != s[j]) return 2
            i++
            j--
        }
        return 1
    }
}
```

## Dart

```dart
class Solution {
  int removePalindromeSub(String s) {
    if (s.isEmpty) return 0;
    int i = 0, j = s.length - 1;
    while (i < j) {
      if (s[i] != s[j]) {
        return 2;
      }
      i++;
      j--;
    }
    return 1;
  }
}
```

## Golang

```go
func removePalindromeSub(s string) int {
	if len(s) == 0 {
		return 0
	}
	i, j := 0, len(s)-1
	for i < j && s[i] == s[j] {
		i++
		j--
	}
	if i >= j {
		return 1
	}
	return 2
}
```

## Ruby

```ruby
def remove_palindrome_sub(s)
  return 0 if s.empty?
  return 1 if s == s.reverse
  2
end
```

## Scala

```scala
object Solution {
    def removePalindromeSub(s: String): Int = {
        if (s.isEmpty) 0
        else if (s == s.reverse) 1
        else 2
    }
}
```

## Rust

```rust
impl Solution {
    pub fn remove_palindrome_sub(s: String) -> i32 {
        if s.is_empty() {
            0
        } else if s.chars().eq(s.chars().rev()) {
            1
        } else {
            2
        }
    }
}
```

## Racket

```racket
(define (palindrome? s)
  (let loop ((i 0) (j (sub1 (string-length s))))
    (cond [(>= i j) #t]
          [(char=? (string-ref s i) (string-ref s j))
           (loop (+ i 1) (- j 1))]
          [else #f])))

(define/contract (remove-palindrome-sub s)
  (-> string? exact-integer?)
  (cond [(zero? (string-length s)) 0]
        [(palindrome? s) 1]
        [else 2]))
```

## Erlang

```erlang
-module(solution).
-export([remove_palindrome_sub/1]).

-spec remove_palindrome_sub(S :: unicode:unicode_binary()) -> integer().
remove_palindrome_sub(<<>>) ->
    0;
remove_palindrome_sub(S) ->
    List = binary_to_list(S),
    case List == lists:reverse(List) of
        true -> 1;
        false -> 2
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec remove_palindrome_sub(String.t()) :: integer()
  def remove_palindrome_sub(s) do
    cond do
      s == "" -> 0
      s == String.reverse(s) -> 1
      true -> 2
    end
  end
end
```
