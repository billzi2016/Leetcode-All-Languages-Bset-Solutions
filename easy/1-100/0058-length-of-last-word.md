# 0058. Length of Last Word

## Cpp

```cpp
class Solution {
public:
    int lengthOfLastWord(string s) {
        int i = (int)s.size() - 1;
        while (i >= 0 && s[i] == ' ') --i;
        int len = 0;
        while (i >= 0 && s[i] != ' ') {
            ++len;
            --i;
        }
        return len;
    }
};
```

## Java

```java
class Solution {
    public int lengthOfLastWord(String s) {
        int i = s.length() - 1;
        while (i >= 0 && s.charAt(i) == ' ') {
            i--;
        }
        int len = 0;
        while (i >= 0 && s.charAt(i) != ' ') {
            len++;
            i--;
        }
        return len;
    }
}
```

## Python

```python
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s) - 1
        # Skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1
        # Count characters of the last word
        length = 0
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        return length
```

## Python3

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        length = 0
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        return length
```

## C

```c
#include <string.h>

int lengthOfLastWord(char* s) {
    int i = (int)strlen(s) - 1;
    while (i >= 0 && s[i] == ' ') i--;
    int len = 0;
    while (i >= 0 && s[i] != ' ') {
        len++;
        i--;
    }
    return len;
}
```

## Csharp

```csharp
public class Solution {
    public int LengthOfLastWord(string s) {
        int i = s.Length - 1;
        while (i >= 0 && s[i] == ' ') i--;
        int length = 0;
        while (i >= 0 && s[i] != ' ') {
            length++;
            i--;
        }
        return length;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let i = s.length - 1;
    while (i >= 0 && s[i] === ' ') i--;
    let len = 0;
    while (i >= 0 && s[i] !== ' ') {
        len++;
        i--;
    }
    return len;
};
```

## Typescript

```typescript
function lengthOfLastWord(s: string): number {
    let i = s.length - 1;
    while (i >= 0 && s[i] === ' ') i--;
    let len = 0;
    while (i >= 0 && s[i] !== ' ') {
        len++;
        i--;
    }
    return len;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function lengthOfLastWord($s) {
        $i = strlen($s) - 1;
        // Skip trailing spaces
        while ($i >= 0 && $s[$i] === ' ') {
            $i--;
        }
        $len = 0;
        // Count characters of the last word
        while ($i >= 0 && $s[$i] !== ' ') {
            $len++;
            $i--;
        }
        return $len;
    }
}
```

## Swift

```swift
class Solution {
    func lengthOfLastWord(_ s: String) -> Int {
        var count = 0
        var inWord = false
        for ch in s.reversed() {
            if ch == " " {
                if inWord { break }
            } else {
                inWord = true
                count += 1
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun lengthOfLastWord(s: String): Int {
        var i = s.length - 1
        while (i >= 0 && s[i] == ' ') i--
        var len = 0
        while (i >= 0 && s[i] != ' ') {
            len++
            i--
        }
        return len
    }
}
```

## Dart

```dart
class Solution {
  int lengthOfLastWord(String s) {
    int i = s.length - 1;
    while (i >= 0 && s[i] == ' ') {
      i--;
    }
    int len = 0;
    while (i >= 0 && s[i] != ' ') {
      len++;
      i--;
    }
    return len;
  }
}
```

## Golang

```go
func lengthOfLastWord(s string) int {
    n := len(s)
    i := n - 1
    // Skip trailing spaces
    for i >= 0 && s[i] == ' ' {
        i--
    }
    length := 0
    // Count characters of the last word
    for i >= 0 && s[i] != ' ' {
        length++
        i--
    }
    return length
}
```

## Ruby

```ruby
def length_of_last_word(s)
  i = s.length - 1
  # Skip trailing spaces (ASCII space = 32)
  while i >= 0 && s.getbyte(i) == 32
    i -= 1
  end
  len = 0
  while i >= 0 && s.getbyte(i) != 32
    len += 1
    i -= 1
  end
  len
end
```

## Scala

```scala
object Solution {
    def lengthOfLastWord(s: String): Int = {
        var i = s.length - 1
        while (i >= 0 && s.charAt(i) == ' ') i -= 1
        var len = 0
        while (i >= 0 && s.charAt(i) != ' ') {
            len += 1
            i -= 1
        }
        len
    }
}
```

## Rust

```rust
impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        let bytes = s.as_bytes();
        let mut i: isize = bytes.len() as isize - 1;
        while i >= 0 && bytes[i as usize] == b' ' {
            i -= 1;
        }
        let mut len: i32 = 0;
        while i >= 0 && bytes[i as usize] != b' ' {
            len += 1;
            i -= 1;
        }
        len
    }
}
```

## Racket

```racket
(define/contract (length-of-last-word s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (last-char-index
          (let loop ((i (- n 1)))
            (if (< i 0) -1
                (if (char=? (string-ref s i) #\space)
                    (loop (- i 1))
                    i)))))
    (if (= last-char-index -1)
        0
        (let loop ((i last-char-index) (cnt 0))
          (if (or (< i 0) (char=? (string-ref s i) #\space))
              cnt
              (loop (- i 1) (+ cnt 1)))))))
```

## Erlang

```erlang
-spec length_of_last_word(S :: unicode:unicode_binary()) -> integer().
length_of_last_word(S) ->
    Rev = binary:reverse(S),
    count_last_word(Rev, 0).

count_last_word(<<>>, Acc) ->
    Acc;
count_last_word(<<C, Rest/binary>>, Acc) when C == $ , Acc == 0 ->
    % skipping trailing spaces
    count_last_word(Rest, 0);
count_last_word(<<C, _Rest/binary>>, Acc) when C == $ , Acc > 0 ->
    % reached space after the last word
    Acc;
count_last_word(<<_, Rest/binary>>, Acc) ->
    count_last_word(Rest, Acc + 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec length_of_last_word(s :: String.t) :: integer
  def length_of_last_word(s) do
    s
    |> String.trim()
    |> String.split(~r/\s+/, trim: true)
    |> List.last()
    |> String.length()
  end
end
```
