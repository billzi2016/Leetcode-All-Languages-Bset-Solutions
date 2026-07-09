# 2027. Minimum Moves to Convert String

## Cpp

```cpp
class Solution {
public:
    int minimumMoves(string s) {
        int n = s.size();
        int ans = 0;
        int i = 0;
        while (i < n) {
            if (s[i] == 'X') {
                ++ans;
                i += 3; // this move converts positions i, i+1, i+2 to 'O'
            } else {
                ++i;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minimumMoves(String s) {
        int n = s.length();
        int moves = 0;
        int i = 0;
        while (i < n) {
            if (s.charAt(i) == 'X') {
                moves++;
                i += 3; // apply move covering positions i, i+1, i+2
            } else {
                i++;
            }
        }
        return moves;
    }
}
```

## Python

```python
class Solution(object):
    def minimumMoves(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        moves = 0
        n = len(s)
        while i < n:
            if s[i] == 'X':
                moves += 1
                i += 3
            else:
                i += 1
        return moves
```

## Python3

```python
class Solution:
    def minimumMoves(self, s: str) -> int:
        n = len(s)
        i = 0
        moves = 0
        while i < n:
            if s[i] == 'X':
                moves += 1
                i += 3
            else:
                i += 1
        return moves
```

## C

```c
#include <string.h>

int minimumMoves(char* s) {
    int n = (int)strlen(s);
    int moves = 0;
    int i = 0;
    while (i < n) {
        if (s[i] == 'X') {
            moves++;
            i += 3; // this move will convert positions i, i+1, i+2
        } else {
            i++;
        }
    }
    return moves;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumMoves(string s) {
        int moves = 0;
        for (int i = 0; i < s.Length; ++i) {
            if (s[i] == 'X') {
                moves++;
                i += 2; // skip the next two characters as they become 'O'
            }
        }
        return moves;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minimumMoves = function(s) {
    let moves = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === 'X') {
            moves++;
            i += 2; // skip the next two characters covered by this move
        }
    }
    return moves;
};
```

## Typescript

```typescript
function minimumMoves(s: string): number {
    let moves = 0;
    for (let i = 0; i < s.length;) {
        if (s[i] === 'X') {
            moves++;
            i += 3;
        } else {
            i++;
        }
    }
    return moves;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minimumMoves($s) {
        $n = strlen($s);
        $i = 0;
        $moves = 0;
        while ($i < $n) {
            if ($s[$i] === 'X') {
                $moves++;
                $i += 3;
            } else {
                $i++;
            }
        }
        return $moves;
    }
}
```

## Swift

```swift
class Solution {
    func minimumMoves(_ s: String) -> Int {
        let chars = Array(s)
        var i = 0
        var moves = 0
        while i < chars.count {
            if chars[i] == "X" {
                moves += 1
                i += 3
            } else {
                i += 1
            }
        }
        return moves
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumMoves(s: String): Int {
        var i = 0
        var moves = 0
        val n = s.length
        while (i < n) {
            if (s[i] == 'X') {
                moves++
                i += 3
            } else {
                i++
            }
        }
        return moves
    }
}
```

## Dart

```dart
class Solution {
  int minimumMoves(String s) {
    int n = s.length;
    int moves = 0;
    int i = 0;
    while (i < n) {
      if (s[i] == 'X') {
        moves++;
        i += 3;
      } else {
        i++;
      }
    }
    return moves;
  }
}
```

## Golang

```go
func minimumMoves(s string) int {
    ans, i, n := 0, 0, len(s)
    for i < n {
        if s[i] == 'X' {
            ans++
            i += 3
        } else {
            i++
        }
    }
    return ans
}
```

## Ruby

```ruby
def minimum_moves(s)
  chars = s.chars
  i = 0
  moves = 0
  while i < chars.length
    if chars[i] == 'X'
      moves += 1
      i += 3
    else
      i += 1
    end
  end
  moves
end
```

## Scala

```scala
object Solution {
    def minimumMoves(s: String): Int = {
        var moves = 0
        var i = 0
        val n = s.length
        while (i < n) {
            if (s.charAt(i) == 'X') {
                moves += 1
                i += 3
            } else {
                i += 1
            }
        }
        moves
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_moves(s: String) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut i = 0usize;
        let mut moves = 0i32;
        while i < n {
            if bytes[i] == b'X' {
                moves += 1;
                i += 3;
            } else {
                i += 1;
            }
        }
        moves
    }
}
```

## Racket

```racket
(define/contract (minimum-moves s)
  (-> string? exact-integer?)
  (let* ((n (string-length s)))
    (let loop ((i 0) (cnt 0))
      (if (>= i n)
          cnt
          (if (char=? (string-ref s i) #\X)
              (loop (+ i 3) (+ cnt 1))
              (loop (+ i 1) cnt))))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_moves/1]).

-spec minimum_moves(S :: unicode:unicode_binary()) -> integer().
minimum_moves(S) ->
    go(binary_to_list(S), 0).

go([], Moves) -> Moves;
go([H|T], Moves) when H =:= $X ->
    NewMoves = Moves + 1,
    T2 = case T of
            [] -> [];
            [_] -> [];
            [_ , _ | Rest] -> Rest
         end,
    go(T2, NewMoves);
go([_H|T], Moves) ->
    go(T, Moves).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_moves(s :: String.t()) :: integer
  def minimum_moves(s) do
    chars = String.to_charlist(s)
    go(chars, 0)
  end

  defp go([], moves), do: moves

  # At least three characters remaining, we can apply a move and skip next two.
  defp go([?X, _a, _b | rest], moves) do
    go(rest, moves + 1)
  end

  # Exactly two characters remaining, starting with 'X'.
  defp go([?X, _a], moves), do: moves + 1

  # Exactly one character remaining, which is 'X'.
  defp go([?X], moves), do: moves + 1

  # Current character is not 'X', move to the next.
  defp go([_ | rest], moves), do: go(rest, moves)
end
```
