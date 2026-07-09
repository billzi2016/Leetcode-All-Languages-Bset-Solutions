# 2038. Remove Colored Pieces if Both Neighbors are the Same Color

## Cpp

```cpp
class Solution {
public:
    bool winnerOfGame(string colors) {
        int aMoves = 0, bMoves = 0;
        int n = colors.size();
        for (int i = 0; i < n; ) {
            char c = colors[i];
            int j = i;
            while (j < n && colors[j] == c) ++j;
            int len = j - i;
            if (len >= 3) {
                if (c == 'A') aMoves += len - 2;
                else bMoves += len - 2;
            }
            i = j;
        }
        return aMoves > bMoves;
    }
};
```

## Java

```java
class Solution {
    public boolean winnerOfGame(String colors) {
        int alice = 0;
        int bob = 0;
        int n = colors.length();
        int i = 0;
        while (i < n) {
            char c = colors.charAt(i);
            int j = i;
            while (j < n && colors.charAt(j) == c) {
                j++;
            }
            int len = j - i;
            if (len >= 3) {
                if (c == 'A') {
                    alice += len - 2;
                } else { // c == 'B'
                    bob += len - 2;
                }
            }
            i = j;
        }
        return alice > bob;
    }
}
```

## Python

```python
class Solution(object):
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """
        a = b = 0
        n = len(colors)
        for i in range(1, n - 1):
            if colors[i] == colors[i-1] == colors[i+1]:
                if colors[i] == 'A':
                    a += 1
                else:
                    b += 1
        return a > b
```

## Python3

```python
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a_moves = b_moves = 0
        n = len(colors)
        i = 0
        while i < n:
            j = i
            while j < n and colors[j] == colors[i]:
                j += 1
            length = j - i
            if length >= 3:
                moves = length - 2
                if colors[i] == 'A':
                    a_moves += moves
                else:
                    b_moves += moves
            i = j
        return a_moves > b_moves
```

## C

```c
#include <stdbool.h>

bool winnerOfGame(char* colors) {
    int alice = 0, bob = 0;
    for (int i = 0; colors[i]; ) {
        char c = colors[i];
        int j = i;
        while (colors[j] == c) j++;
        int len = j - i;
        if (len >= 3) {
            if (c == 'A')
                alice += len - 2;
            else
                bob += len - 2;
        }
        i = j;
    }
    return alice > bob;
}
```

## Csharp

```csharp
public class Solution {
    public bool WinnerOfGame(string colors) {
        int alice = 0, bob = 0;
        for (int i = 1; i + 1 < colors.Length; i++) {
            if (colors[i] == 'A' && colors[i - 1] == 'A' && colors[i + 1] == 'A')
                alice++;
            else if (colors[i] == 'B' && colors[i - 1] == 'B' && colors[i + 1] == 'B')
                bob++;
        }
        return alice > bob;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} colors
 * @return {boolean}
 */
var winnerOfGame = function(colors) {
    let aMoves = 0, bMoves = 0;
    const n = colors.length;
    let i = 0;
    while (i < n) {
        let j = i;
        while (j < n && colors[j] === colors[i]) j++;
        const len = j - i;
        if (len >= 3) {
            if (colors[i] === 'A') aMoves += len - 2;
            else bMoves += len - 2;
        }
        i = j;
    }
    return aMoves > bMoves;
};
```

## Typescript

```typescript
function winnerOfGame(colors: string): boolean {
    let alice = 0, bob = 0;
    const n = colors.length;
    let i = 0;
    while (i < n) {
        const ch = colors.charAt(i);
        let j = i;
        while (j < n && colors.charAt(j) === ch) j++;
        const len = j - i;
        if (len >= 3) {
            if (ch === 'A') alice += len - 2;
            else bob += len - 2;
        }
        i = j;
    }
    return alice > bob;
}
```

## Php

```php
class Solution {

    /**
     * @param String $colors
     * @return Boolean
     */
    function winnerOfGame($colors) {
        $len = strlen($colors);
        $cntA = 0;
        $cntB = 0;
        for ($i = 1; $i < $len - 1; $i++) {
            if ($colors[$i] === $colors[$i - 1] && $colors[$i] === $colors[$i + 1]) {
                if ($colors[$i] === 'A') {
                    $cntA++;
                } else {
                    $cntB++;
                }
            }
        }
        return $cntA > $cntB;
    }
}
```

## Swift

```swift
class Solution {
    func winnerOfGame(_ colors: String) -> Bool {
        let chars = Array(colors)
        var aMoves = 0
        var bMoves = 0
        var i = 0
        while i < chars.count {
            let current = chars[i]
            var j = i
            while j < chars.count && chars[j] == current {
                j += 1
            }
            let length = j - i
            if current == "A" {
                aMoves += max(0, length - 2)
            } else { // 'B'
                bMoves += max(0, length - 2)
            }
            i = j
        }
        return aMoves > bMoves
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun winnerOfGame(colors: String): Boolean {
        var aMoves = 0
        var bMoves = 0
        var i = 0
        val n = colors.length
        while (i < n) {
            val ch = colors[i]
            var j = i
            while (j < n && colors[j] == ch) j++
            val len = j - i
            if (len >= 3) {
                if (ch == 'A') aMoves += len - 2 else bMoves += len - 2
            }
            i = j
        }
        return aMoves > bMoves
    }
}
```

## Dart

```dart
class Solution {
  bool winnerOfGame(String colors) {
    int aliceMoves = 0;
    int bobMoves = 0;
    int n = colors.length;
    int i = 0;
    while (i < n) {
      int j = i;
      while (j < n && colors[j] == colors[i]) {
        j++;
      }
      int len = j - i;
      if (colors[i] == 'A') {
        if (len >= 3) aliceMoves += len - 2;
      } else { // 'B'
        if (len >= 3) bobMoves += len - 2;
      }
      i = j;
    }
    return aliceMoves > bobMoves;
  }
}
```

## Golang

```go
func winnerOfGame(colors string) bool {
    aMoves, bMoves := 0, 0
    n := len(colors)
    for i := 0; i < n; {
        j := i + 1
        for j < n && colors[j] == colors[i] {
            j++
        }
        length := j - i
        if length >= 3 {
            cnt := length - 2
            if colors[i] == 'A' {
                aMoves += cnt
            } else {
                bMoves += cnt
            }
        }
        i = j
    }
    return aMoves > bMoves
}
```

## Ruby

```ruby
def winner_of_game(colors)
  a_moves = 0
  b_moves = 0
  i = 0
  n = colors.length
  while i < n
    j = i
    while j < n && colors[j] == colors[i]
      j += 1
    end
    len = j - i
    if len >= 3
      if colors[i] == 'A'
        a_moves += len - 2
      else
        b_moves += len - 2
      end
    end
    i = j
  end
  a_moves > b_moves
end
```

## Scala

```scala
object Solution {
    def winnerOfGame(colors: String): Boolean = {
        var alice = 0
        var bob = 0
        var i = 0
        val n = colors.length
        while (i < n) {
            val c = colors.charAt(i)
            var j = i
            while (j < n && colors.charAt(j) == c) j += 1
            val len = j - i
            if (len >= 3) {
                if (c == 'A') alice += len - 2 else bob += len - 2
            }
            i = j
        }
        alice > bob
    }
}
```

## Rust

```rust
impl Solution {
    pub fn winner_of_game(colors: String) -> bool {
        let bytes = colors.as_bytes();
        let mut a_moves: i64 = 0;
        let mut b_moves: i64 = 0;
        let mut i = 0usize;
        while i < bytes.len() {
            let cur = bytes[i];
            let mut j = i + 1;
            while j < bytes.len() && bytes[j] == cur {
                j += 1;
            }
            let len = j - i;
            if len >= 3 {
                if cur == b'A' {
                    a_moves += (len - 2) as i64;
                } else {
                    b_moves += (len - 2) as i64;
                }
            }
            i = j;
        }
        a_moves > b_moves
    }
}
```

## Racket

```racket
(define/contract (winner-of-game colors)
  (-> string? boolean?)
  (let ((n (string-length colors)))
    (let loop ((i 0) (a 0) (b 0))
      (if (>= i n)
          (> a b)
          (let* ((ch (string-ref colors i))
                 (j (let find ((k i))
                      (if (and (< k n) (char=? (string-ref colors k) ch))
                          (find (+ k 1))
                          k)))
                 (len (- j i))
                 (add (max 0 (- len 2))))
            (if (char=? ch #\A)
                (loop j (+ a add) b)
                (loop j a (+ b add))))))))
```

## Erlang

```erlang
-spec winner_of_game(Colors :: unicode:unicode_binary()) -> boolean().
winner_of_game(Colors) ->
    List = binary_to_list(Colors),
    {Alice0, Bob0, Prev, Cnt} =
        lists:foldl(
            fun(Char, {A, B, P, C}) ->
                case P of
                    undefined ->
                        {A, B, Char, 1};
                    _ when Char =:= P ->
                        {A, B, P, C + 1};
                    _ ->
                        Moves = erlang:max(0, C - 2),
                        case P of
                            $A -> {A + Moves, B, Char, 1};
                            $B -> {A, B + Moves, Char, 1}
                        end
                end
            end,
            {0, 0, undefined, 0},
            List),
    {Alice, Bob} =
        case Prev of
            undefined ->
                {Alice0, Bob0};
            _ ->
                Moves = erlang:max(0, Cnt - 2),
                case Prev of
                    $A -> {Alice0 + Moves, Bob0};
                    $B -> {Alice0, Bob0 + Moves}
                end
        end,
    Alice > Bob.
```

## Elixir

```elixir
defmodule Solution do
  @spec winner_of_game(colors :: String.t) :: boolean
  def winner_of_game(colors) do
    {a_moves, b_moves, prev, len} =
      colors
      |> String.graphemes()
      |> Enum.reduce({0, 0, nil, 0}, fn ch, {a, b, p, l} ->
        cond do
          p == nil ->
            {a, b, ch, 1}
          ch == p ->
            {a, b, p, l + 1}
          true ->
            add = max(l - 2, 0)
            case p do
              "A" -> {a + add, b, ch, 1}
              "B" -> {a, b + add, ch, 1}
            end
        end
      end)

    {final_a, final_b} =
      if prev == nil do
        {a_moves, b_moves}
      else
        add = max(len - 2, 0)
        case prev do
          "A" -> {a_moves + add, b_moves}
          "B" -> {a_moves, b_moves + add}
        end
      end

    final_a > final_b
  end
end
```
