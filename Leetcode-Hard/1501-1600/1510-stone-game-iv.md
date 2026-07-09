# 1510. Stone Game IV

## Cpp

```cpp
class Solution {
public:
    bool winnerSquareGame(int n) {
        std::vector<char> dp(n + 1, 0);
        for (int i = 1; i <= n; ++i) {
            for (int k = 1; k * k <= i; ++k) {
                if (!dp[i - k * k]) {
                    dp[i] = 1;
                    break;
                }
            }
        }
        return dp[n];
    }
};
```

## Java

```java
class Solution {
    public boolean winnerSquareGame(int n) {
        boolean[] dp = new boolean[n + 1];
        for (int i = 1; i <= n; i++) {
            for (int k = 1; k * k <= i; k++) {
                if (!dp[i - k * k]) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[n];
    }
}
```

## Python

```python
class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dp = [False] * (n + 1)
        # dp[0] is False by definition (no move -> lose)
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                if not dp[i - j * j]:
                    dp[i] = True
                    break
                j += 1
        return dp[n]
```

## Python3

```python
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        # precompute square numbers up to n
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        for stones in range(1, n + 1):
            win = False
            for sq in squares:
                if sq > stones:
                    break
                if not dp[stones - sq]:
                    win = True
                    break
            dp[stones] = win
        return dp[n]
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

bool winnerSquareGame(int n) {
    bool *dp = (bool *)malloc((n + 1) * sizeof(bool));
    if (!dp) return false;
    dp[0] = false;
    for (int i = 1; i <= n; ++i) {
        dp[i] = false;
        for (int j = 1; j * j <= i; ++j) {
            if (!dp[i - j * j]) {
                dp[i] = true;
                break;
            }
        }
    }
    bool result = dp[n];
    free(dp);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public bool WinnerSquareGame(int n)
    {
        bool[] dp = new bool[n + 1];
        // dp[0] is false by default (losing state)

        for (int i = 1; i <= n; i++)
        {
            int limit = (int)Math.Sqrt(i);
            for (int k = 1; k <= limit; k++)
            {
                int sq = k * k;
                if (!dp[i - sq])
                {
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[n];
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {boolean}
 */
var winnerSquareGame = function(n) {
    const dp = new Array(n + 1).fill(false);
    const maxRoot = Math.floor(Math.sqrt(n));
    const squares = [];
    for (let i = 1; i <= maxRoot; i++) {
        squares.push(i * i);
    }
    for (let i = 1; i <= n; i++) {
        for (const sq of squares) {
            if (sq > i) break;
            if (!dp[i - sq]) {
                dp[i] = true;
                break;
            }
        }
    }
    return dp[n];
};
```

## Typescript

```typescript
function winnerSquareGame(n: number): boolean {
    const dp: boolean[] = new Array(n + 1).fill(false);
    for (let i = 1; i <= n; i++) {
        let canWin = false;
        for (let k = 1; k * k <= i; k++) {
            if (!dp[i - k * k]) {
                canWin = true;
                break;
            }
        }
        dp[i] = canWin;
    }
    return dp[n];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Boolean
     */
    function winnerSquareGame($n) {
        $dp = array_fill(0, $n + 1, false);
        for ($i = 1; $i <= $n; $i++) {
            $j = 1;
            while ($j * $j <= $i) {
                if (!$dp[$i - $j * $j]) {
                    $dp[$i] = true;
                    break;
                }
                $j++;
            }
        }
        return $dp[$n];
    }
}
```

## Swift

```swift
class Solution {
    func winnerSquareGame(_ n: Int) -> Bool {
        var dp = [Bool](repeating: false, count: n + 1)
        for i in 1...n {
            var j = 1
            while j * j <= i {
                if !dp[i - j * j] {
                    dp[i] = true
                    break
                }
                j += 1
            }
        }
        return dp[n]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun winnerSquareGame(n: Int): Boolean {
        val dp = BooleanArray(n + 1)
        for (i in 1..n) {
            var j = 1
            while (j * j <= i) {
                if (!dp[i - j * j]) {
                    dp[i] = true
                    break
                }
                j++
            }
        }
        return dp[n]
    }
}
```

## Dart

```dart
class Solution {
  bool winnerSquareGame(int n) {
    List<bool> dp = List.filled(n + 1, false);
    for (int i = 1; i <= n; ++i) {
      for (int k = 1; k * k <= i; ++k) {
        if (!dp[i - k * k]) {
          dp[i] = true;
          break;
        }
      }
    }
    return dp[n];
  }
}
```

## Golang

```go
func winnerSquareGame(n int) bool {
    dp := make([]bool, n+1)
    squares := []int{}
    for i := 1; i*i <= n; i++ {
        squares = append(squares, i*i)
    }
    for i := 1; i <= n; i++ {
        win := false
        for _, sq := range squares {
            if sq > i {
                break
            }
            if !dp[i-sq] {
                win = true
                break
            }
        }
        dp[i] = win
    }
    return dp[n]
}
```

## Ruby

```ruby
def winner_square_game(n)
  dp = Array.new(n + 1, false)
  squares = []
  i = 1
  while i * i <= n
    squares << i * i
    i += 1
  end

  (1..n).each do |stones|
    squares.each do |sq|
      break if sq > stones
      unless dp[stones - sq]
        dp[stones] = true
        break
      end
    end
  end

  dp[n]
end
```

## Scala

```scala
object Solution {
    def winnerSquareGame(n: Int): Boolean = {
        val dp = new Array[Boolean](n + 1)
        for (i <- 1 to n) {
            var j = 1
            var canWin = false
            while (j * j <= i && !canWin) {
                if (!dp(i - j * j)) canWin = true
                j += 1
            }
            dp(i) = canWin
        }
        dp(n)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn winner_square_game(n: i32) -> bool {
        let n = n as usize;
        let mut dp = vec![false; n + 1];
        for i in 1..=n {
            let mut k = 1usize;
            while k * k <= i {
                if !dp[i - k * k] {
                    dp[i] = true;
                    break;
                }
                k += 1;
            }
        }
        dp[n]
    }
}
```

## Racket

```racket
(define/contract (winner-square-game n)
  (-> exact-integer? boolean?)
  (let* ((dp (make-vector (add1 n) #f))) ; dp[0] = #f by default
    (for ([i (in-range 1 (add1 n))])
      (let loop ((k 1) (win #f))
        (cond [(or win (> (* k k) i))
               (vector-set! dp i win)]
              [else
               (define sq (* k k))
               (loop (+ k 1)
                     (or win (not (vector-ref dp (- i sq)))))])))
    (vector-ref dp n)))
```

## Erlang

```erlang
-module(solution).
-export([winner_square_game/1]).

-spec winner_square_game(N :: integer()) -> boolean().
winner_square_game(N) when N >= 0 ->
    Squares = [S*S || S <- lists:seq(1, trunc(math:sqrt(N)))],
    DP0 = array:new(N + 1, {default, false}),
    DP = fill_dp(1, N, Squares, DP0),
    array:get(N, DP).

fill_dp(I, N, _Squares, DP) when I > N ->
    DP;
fill_dp(I, N, Squares, DP) ->
    Win = any_square_losing(I, Squares, DP),
    DP2 = array:set(I, Win, DP),
    fill_dp(I + 1, N, Squares, DP2).

any_square_losing(I, Squares, DP) ->
    lists:any(
        fun(Sq) ->
            if
                Sq > I -> false;
                true -> not array:get(I - Sq, DP)
            end
        end,
        Squares
    ).
```

## Elixir

```elixir
defmodule Solution do
  @spec winner_square_game(n :: integer) :: boolean
  def winner_square_game(n) do
    max_root = :math.sqrt(n) |> trunc()
    squares = for i <- 1..max_root, do: i * i

    dp = :array.new(n + 1, default: false)

    dp =
      Enum.reduce(1..n, dp, fn i, acc ->
        win =
          Enum.any?(squares, fn s ->
            if s > i do
              false
            else
              not :array.get(i - s, acc)
            end
          end)

        :array.set(i, win, acc)
      end)

    :array.get(n, dp)
  end
end
```
