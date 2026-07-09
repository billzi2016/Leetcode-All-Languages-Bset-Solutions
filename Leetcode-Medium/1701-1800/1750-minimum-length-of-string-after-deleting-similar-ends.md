# 1750. Minimum Length of String After Deleting Similar Ends

## Cpp

```cpp
class Solution {
public:
    int minimumLength(string s) {
        int i = 0, j = (int)s.size() - 1;
        while (i < j && s[i] == s[j]) {
            char c = s[i];
            while (i <= j && s[i] == c) ++i;
            while (j >= i && s[j] == c) --j;
        }
        return (i > j) ? 0 : (j - i + 1);
    }
};
```

## Java

```java
class Solution {
    public int minimumLength(String s) {
        int left = 0;
        int right = s.length() - 1;
        while (left < right && s.charAt(left) == s.charAt(right)) {
            char c = s.charAt(left);
            while (left <= right && s.charAt(left) == c) {
                left++;
            }
            while (right >= left && s.charAt(right) == c) {
                right--;
            }
        }
        return Math.max(0, right - left + 1);
    }
}
```

## Python

```python
class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        left, right = 0, n - 1
        while left < right and s[left] == s[right]:
            ch = s[left]
            while left <= right and s[left] == ch:
                left += 1
            while right >= left and s[right] == ch:
                right -= 1
        return max(0, right - left + 1)
```

## Python3

```python
class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1
        while l < r and s[l] == s[r]:
            ch = s[l]
            while l <= r and s[l] == ch:
                l += 1
            while r >= l and s[r] == ch:
                r -= 1
        return max(0, r - l + 1)
```

## C

```c
#include <string.h>

int minimumLength(char* s) {
    int n = strlen(s);
    int i = 0, j = n - 1;
    while (i < j && s[i] == s[j]) {
        char c = s[i];
        while (i <= j && s[i] == c) i++;
        while (j >= i && s[j] == c) j--;
    }
    return (i > j) ? 0 : (j - i + 1);
}
```

## Csharp

```csharp
public class Solution
{
    public int MinimumLength(string s)
    {
        int left = 0;
        int right = s.Length - 1;

        while (left < right && s[left] == s[right])
        {
            char c = s[left];
            while (left <= right && s[left] == c) left++;
            while (right >= left && s[right] == c) right--;
        }

        return Math.Max(0, right - left + 1);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minimumLength = function(s) {
    let left = 0;
    let right = s.length - 1;
    while (left < right && s[left] === s[right]) {
        const ch = s[left];
        while (left <= right && s[left] === ch) left++;
        while (right >= left && s[right] === ch) right--;
    }
    return right >= left ? right - left + 1 : 0;
};
```

## Typescript

```typescript
function minimumLength(s: string): number {
    let left = 0;
    let right = s.length - 1;

    while (left < right && s[left] === s[right]) {
        const ch = s[left];
        while (left <= right && s[left] === ch) left++;
        while (right >= left && s[right] === ch) right--;
    }

    return Math.max(0, right - left + 1);
}
```

## Php

```php
class Solution {
    /**
     * @param string $s
     * @return int
     */
    function minimumLength($s) {
        $n = strlen($s);
        $l = 0;
        $r = $n - 1;
        while ($l < $r && $s[$l] === $s[$r]) {
            $c = $s[$l];
            while ($l <= $r && $s[$l] === $c) {
                $l++;
            }
            while ($r >= $l && $s[$r] === $c) {
                $r--;
            }
        }
        return $r >= $l ? $r - $l + 1 : 0;
    }
}
```

## Swift

```swift
class Solution {
    func minimumLength(_ s: String) -> Int {
        let bytes = Array(s.utf8)
        var left = 0
        var right = bytes.count - 1
        
        while left < right && bytes[left] == bytes[right] {
            let c = bytes[left]
            while left <= right && bytes[left] == c {
                left += 1
            }
            while right >= left && bytes[right] == c {
                right -= 1
            }
        }
        
        if left > right { return 0 }
        return right - left + 1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumLength(s: String): Int {
        var left = 0
        var right = s.length - 1
        while (left < right && s[left] == s[right]) {
            val ch = s[left]
            while (left <= right && s[left] == ch) left++
            while (right >= left && s[right] == ch) right--
        }
        return if (left > right) 0 else right - left + 1
    }
}
```

## Dart

```dart
class Solution {
  int minimumLength(String s) {
    int left = 0;
    int right = s.length - 1;

    while (left < right && s[left] == s[right]) {
      String ch = s[left];
      while (left <= right && s[left] == ch) {
        left++;
      }
      while (right >= left && s[right] == ch) {
        right--;
      }
    }

    return left > right ? 0 : right - left + 1;
  }
}
```

## Golang

```go
func minimumLength(s string) int {
    l, r := 0, len(s)-1
    for l < r && s[l] == s[r] {
        c := s[l]
        for l <= r && s[l] == c {
            l++
        }
        for r >= l && s[r] == c {
            r--
        }
    }
    if l > r {
        return 0
    }
    return r - l + 1
}
```

## Ruby

```ruby
def minimum_length(s)
  left = 0
  right = s.length - 1
  while left < right && s.getbyte(left) == s.getbyte(right)
    c = s.getbyte(left)
    while left <= right && s.getbyte(left) == c
      left += 1
    end
    while right >= left && s.getbyte(right) == c
      right -= 1
    end
  end
  remaining = right - left + 1
  remaining > 0 ? remaining : 0
end
```

## Scala

```scala
object Solution {
    def minimumLength(s: String): Int = {
        var left = 0
        var right = s.length - 1
        while (left < right && s.charAt(left) == s.charAt(right)) {
            val c = s.charAt(left)
            while (left <= right && s.charAt(left) == c) left += 1
            while (right >= left && s.charAt(right) == c) right -= 1
        }
        if (left > right) 0 else right - left + 1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_length(s: String) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        if n == 0 {
            return 0;
        }
        let mut left: usize = 0;
        let mut right: usize = n - 1;

        while left < right && bytes[left] == bytes[right] {
            let c = bytes[left];
            // skip all leading characters equal to c
            while left <= right && bytes[left] == c {
                left += 1;
                if left > right {
                    break;
                }
            }
            // skip all trailing characters equal to c
            while right >= left && bytes[right] == c {
                if right == 0 {
                    // cannot decrement further without underflow
                    break;
                }
                right -= 1;
                if right < left {
                    break;
                }
            }
        }

        if left > right {
            0
        } else {
            (right - left + 1) as i32
        }
    }
}
```

## Racket

```racket
(define/contract (minimum-length s)
  (-> string? exact-integer?)
  (let* ((n (string-length s)))
    (let loop ((i 0) (j (- n 1)))
      (if (or (>= i j) (not (= (string-ref s i) (string-ref s j))))
          (max 0 (+ (- j i) 1))
          (let ((c (string-ref s i)))
            (define new-i
              (let advance-left ((idx i))
                (if (and (<= idx j) (= (string-ref s idx) c))
                    (advance-left (+ idx 1))
                    idx)))
            (define new-j
              (let advance-right ((idx j))
                (if (and (>= idx i) (= (string-ref s idx) c))
                    (advance-right (- idx 1))
                    idx)))
            (loop new-i new-j))))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_length/1]).

-spec minimum_length(S :: unicode:unicode_binary()) -> integer().
minimum_length(S) ->
    Len = byte_size(S),
    loop(S, 0, Len - 1).

loop(_S, Start, End) when Start > End ->
    0;
loop(_S, _Start, _End) when Start == End ->
    1;
loop(S, Start, End) ->
    First = binary:at(S, Start),
    Last = binary:at(S, End),
    if
        First =:= Last ->
            C = First,
            NewStart = advance_start(S, Start, End, C),
            NewEnd = retreat_end(S, NewStart, End, C),
            loop(S, NewStart, NewEnd);
        true ->
            End - Start + 1
    end.

advance_start(_S, Start, End, _C) when Start > End ->
    Start;
advance_start(S, Start, End, C) when binary:at(S, Start) =:= C ->
    advance_start(S, Start + 1, End, C);
advance_start(_S, Start, _End, _C) ->
    Start.

retreat_end(_S, Start, End, _C) when End < Start ->
    End;
retreat_end(S, Start, End, C) when binary:at(S, End) =:= C ->
    retreat_end(S, Start, End - 1, C);
retreat_end(_S, _Start, End, _C) ->
    End.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_length(s :: String.t()) :: integer
  def minimum_length(s) do
    len = byte_size(s)
    process(0, len - 1, s)
  end

  defp process(l, r, s) when l < r do
    left_char = :binary.at(s, l)
    right_char = :binary.at(s, r)

    if left_char == right_char do
      new_l = skip_left(l, r, s, left_char)
      new_r = skip_right(new_l, r, s, left_char)
      process(new_l, new_r, s)
    else
      r - l + 1
    end
  end

  defp process(l, r, _s) do
    if l > r, do: 0, else: 1
  end

  defp skip_left(l, r, s, c) when l <= r and :binary.at(s, l) == c do
    skip_left(l + 1, r, s, c)
  end

  defp skip_left(l, _r, _s, _c), do: l

  defp skip_right(l, r, s, c) when r >= l and :binary.at(s, r) == c do
    skip_right(l, r - 1, s, c)
  end

  defp skip_right(_l, r, _s, _c), do: r
end
```
