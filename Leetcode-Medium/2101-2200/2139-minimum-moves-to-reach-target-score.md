# 2139. Minimum Moves to Reach Target Score

## Cpp

```cpp
class Solution {
public:
    int minMoves(int target, int maxDoubles) {
        long long t = target;
        int moves = 0;
        while (t > 1 && maxDoubles > 0) {
            if (t % 2 == 0) {
                t /= 2;
                --maxDoubles;
            } else {
                --t; // undo an increment
            }
            ++moves;
        }
        moves += static_cast<int>(t - 1); // remaining increments
        return moves;
    }
};
```

## Java

```java
class Solution {
    public int minMoves(int target, int maxDoubles) {
        int moves = 0;
        while (target > 1 && maxDoubles > 0) {
            if ((target & 1) == 0) {
                target >>= 1;
                maxDoubles--;
                moves++;
            } else {
                target--;
                moves++;
            }
        }
        moves += target - 1;
        return moves;
    }
}
```

## Python

```python
class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        moves = 0
        while target > 1 and maxDoubles > 0:
            if target % 2 == 0:
                target //= 2
                maxDoubles -= 1
            else:
                target -= 1
            moves += 1
        # Remaining distance can only be covered by increments
        moves += target - 1
        return moves
```

## Python3

```python
class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        while target > 1:
            if maxDoubles > 0 and target % 2 == 0:
                target //= 2
                maxDoubles -= 1
                moves += 1
            else:
                if maxDoubles == 0:
                    moves += target - 1
                    break
                target -= 1
                moves += 1
        return moves
```

## C

```c
int minMoves(int target, int maxDoubles) {
    int moves = 0;
    while (target > 1 && maxDoubles > 0) {
        if (target % 2 == 0) {
            target /= 2;
            maxDoubles--;
            moves++; // double operation
        } else {
            target--;
            moves++; // increment operation reversed
        }
    }
    moves += (target - 1); // remaining increments
    return moves;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinMoves(int target, int maxDoubles)
    {
        int moves = 0;
        while (target > 1 && maxDoubles > 0)
        {
            if ((target & 1) == 0) // even
            {
                target >>= 1; // divide by 2
                maxDoubles--;
                moves++;
            }
            else
            {
                target--; // make it even
                moves++;
            }
        }
        // Remaining increments to reach 1
        moves += target - 1;
        return moves;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} target
 * @param {number} maxDoubles
 * @return {number}
 */
var minMoves = function(target, maxDoubles) {
    let moves = 0;
    while (target > 1 && maxDoubles > 0) {
        if (target % 2 === 0) {
            target = target / 2;
            maxDoubles--;
        } else {
            target -= 1;
        }
        moves++;
    }
    // Remaining increments to reach 1
    moves += target - 1;
    return moves;
};
```

## Typescript

```typescript
function minMoves(target: number, maxDoubles: number): number {
    let moves = 0;
    while (target > 1 && maxDoubles > 0) {
        if (target % 2 === 0) {
            target = target / 2;
            maxDoubles--;
        } else {
            target -= 1;
        }
        moves++;
    }
    // Remaining distance can only be covered by increments
    moves += target - 1;
    return moves;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $target
     * @param Integer $maxDoubles
     * @return Integer
     */
    function minMoves($target, $maxDoubles) {
        $moves = 0;
        while ($target > 1 && $maxDoubles > 0) {
            if ($target % 2 == 0) {
                $target = intdiv($target, 2);
                $maxDoubles--;
                $moves++;
            } else {
                $target -= 1;
                $moves++;
            }
        }
        $moves += $target - 1; // remaining increments
        return $moves;
    }
}
```

## Swift

```swift
class Solution {
    func minMoves(_ target: Int, _ maxDoubles: Int) -> Int {
        var t = target
        var doubles = maxDoubles
        var moves = 0
        while t > 1 && doubles > 0 {
            if t % 2 == 0 {
                t /= 2
                doubles -= 1
                moves += 1
            } else {
                t -= 1
                moves += 1
            }
        }
        moves += (t - 1)
        return moves
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minMoves(target: Int, maxDoubles: Int): Int {
        var t = target
        var doublesLeft = maxDoubles
        var moves = 0L
        while (t > 1 && doublesLeft > 0) {
            if (t % 2 == 0) {
                t /= 2
                doublesLeft--
                moves++
            } else {
                t -= 1
                moves++
            }
        }
        moves += (t - 1)
        return moves.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int minMoves(int target, int maxDoubles) {
    int moves = 0;
    while (target > 1 && maxDoubles > 0) {
      if (target % 2 == 0) {
        target ~/= 2;
        maxDoubles--;
        moves++;
      } else {
        target -= 1;
        moves++;
      }
    }
    moves += target - 1;
    return moves;
  }
}
```

## Golang

```go
func minMoves(target int, maxDoubles int) int {
    moves := 0
    for target > 1 && maxDoubles > 0 {
        if target%2 == 0 {
            target /= 2
            maxDoubles--
            moves++
        } else {
            target--
            moves++
        }
    }
    moves += target - 1
    return moves
}
```

## Ruby

```ruby
def min_moves(target, max_doubles)
  moves = 0
  while target > 1 && max_doubles > 0
    if target.even?
      target /= 2
      max_doubles -= 1
    else
      target -= 1
    end
    moves += 1
  end
  moves + (target - 1)
end
```

## Scala

```scala
object Solution {
    def minMoves(target: Int, maxDoubles: Int): Int = {
        var t: Long = target.toLong
        var d = maxDoubles
        var moves: Long = 0L
        while (t > 1) {
            if (d > 0 && t % 2 == 0) {
                t /= 2
                d -= 1
                moves += 1
            } else {
                if (d == 0) {
                    moves += t - 1
                    t = 1
                } else {
                    // t is odd, perform a decrement
                    t -= 1
                    moves += 1
                }
            }
        }
        moves.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_moves(target: i32, max_doubles: i32) -> i32 {
        let mut t = target as i64;
        let mut d = max_doubles as i64;
        let mut moves: i64 = 0;
        while t > 1 && d > 0 {
            if t % 2 == 0 {
                t /= 2;
                d -= 1;
            } else {
                t -= 1;
            }
            moves += 1;
        }
        (moves + (t - 1)) as i32
    }
}
```

## Racket

```racket
(define/contract (min-moves target maxDoubles)
  (-> exact-integer? exact-integer? exact-integer?)
  (let loop ((t target) (d maxDoubles) (moves 0))
    (cond
      [(= t 1) moves]
      [(zero? d) (+ moves (- t 1))]
      [else
       (if (even? t)
           (loop (/ t 2) (sub1 d) (add1 moves))
           (loop (sub1 t) d (add1 moves)))])))
```

## Erlang

```erlang
-module(solution).
-export([min_moves/2]).

-spec min_moves(Target :: integer(), MaxDoubles :: integer()) -> integer().
min_moves(Target, MaxDoubles) ->
    min_moves_helper(Target, MaxDoubles, 0).

min_moves_helper(1, _MaxDoubles, Moves) ->
    Moves;
min_moves_helper(Target, MaxDoubles, Moves) when MaxDoubles =< 0 ->
    Moves + (Target - 1);
min_moves_helper(Target, MaxDoubles, Moves) ->
    case Target rem 2 of
        0 -> % even, use reverse double
            min_moves_helper(Target div 2, MaxDoubles - 1, Moves + 1);
        _ -> % odd, use reverse increment
            min_moves_helper(Target - 1, MaxDoubles, Moves + 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_moves(target :: integer, max_doubles :: integer) :: integer
  def min_moves(target, max_doubles) do
    do_min_moves(target, max_doubles, 0)
  end

  defp do_min_moves(1, _maxd, moves), do: moves

  defp do_min_moves(t, maxd, moves) when maxd > 0 do
    if rem(t, 2) == 0 do
      do_min_moves(div(t, 2), maxd - 1, moves + 1)
    else
      do_min_moves(t - 1, maxd, moves + 1)
    end
  end

  defp do_min_moves(t, _maxd, moves) do
    moves + (t - 1)
  end
end
```
