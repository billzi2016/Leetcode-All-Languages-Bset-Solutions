# 1041. Robot Bounded In Circle

## Cpp

```cpp
class Solution {
public:
    bool isRobotBounded(string instructions) {
        int x = 0, y = 0;
        // directions: north, east, south, west
        int dx[4] = {0, 1, 0, -1};
        int dy[4] = {1, 0, -1, 0};
        int dir = 0; // start facing north
        for (char c : instructions) {
            if (c == 'G') {
                x += dx[dir];
                y += dy[dir];
            } else if (c == 'L') {
                dir = (dir + 3) % 4;
            } else if (c == 'R') {
                dir = (dir + 1) % 4;
            }
        }
        return (x == 0 && y == 0) || dir != 0;
    }
};
```

## Java

```java
class Solution {
    public boolean isRobotBounded(String instructions) {
        int x = 0, y = 0;
        // 0: north, 1: east, 2: south, 3: west
        int dir = 0;
        for (char c : instructions.toCharArray()) {
            if (c == 'G') {
                switch (dir) {
                    case 0 -> y++;
                    case 1 -> x++;
                    case 2 -> y--;
                    case 3 -> x--;
                }
            } else if (c == 'L') {
                dir = (dir + 3) % 4;
            } else if (c == 'R') {
                dir = (dir + 1) % 4;
            }
        }
        return (x == 0 && y == 0) || dir != 0;
    }
}
```

## Python

```python
class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        x = y = 0
        # 0:N, 1:E, 2:S, 3:W
        dir_idx = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for c in instructions:
            if c == 'G':
                dx, dy = dirs[dir_idx]
                x += dx
                y += dy
            elif c == 'L':
                dir_idx = (dir_idx + 3) % 4
            else:  # 'R'
                dir_idx = (dir_idx + 1) % 4
        return (x == 0 and y == 0) or dir_idx != 0
```

## Python3

```python
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # Directions: North, East, South, West
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x = y = 0
        d = 0  # start facing north

        for ch in instructions:
            if ch == 'G':
                dx, dy = dirs[d]
                x += dx
                y += dy
            elif ch == 'L':
                d = (d + 3) % 4  # turn left
            else:  # 'R'
                d = (d + 1) % 4  # turn right

        # Robot is bounded if it returns to origin or doesn't face north
        return (x == 0 and y == 0) or d != 0
```

## C

```c
#include <stdbool.h>

bool isRobotBounded(char* instructions) {
    int x = 0, y = 0;
    int dir = 0; // 0: north, 1: east, 2: south, 3: west
    for (int i = 0; instructions[i] != '\0'; ++i) {
        char c = instructions[i];
        if (c == 'G') {
            if (dir == 0) y++;
            else if (dir == 1) x++;
            else if (dir == 2) y--;
            else x--;
        } else if (c == 'L') {
            dir = (dir + 3) % 4;
        } else if (c == 'R') {
            dir = (dir + 1) % 4;
        }
    }
    return (x == 0 && y == 0) || dir != 0;
}
```

## Csharp

```csharp
public class Solution
{
    public bool IsRobotBounded(string instructions)
    {
        int x = 0, y = 0;
        // 0:N, 1:E, 2:S, 3:W
        int dir = 0;
        foreach (char c in instructions)
        {
            if (c == 'G')
            {
                switch (dir)
                {
                    case 0: y++; break; // north
                    case 1: x++; break; // east
                    case 2: y--; break; // south
                    case 3: x--; break; // west
                }
            }
            else if (c == 'L')
            {
                dir = (dir + 3) % 4; // turn left
            }
            else if (c == 'R')
            {
                dir = (dir + 1) % 4; // turn right
            }
        }

        // Bounded if back at origin or not facing north
        return (x == 0 && y == 0) || dir != 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} instructions
 * @return {boolean}
 */
var isRobotBounded = function(instructions) {
    let x = 0, y = 0;
    // 0: north, 1: east, 2: south, 3: west
    let dir = 0;
    for (let ch of instructions) {
        if (ch === 'G') {
            if (dir === 0) y++;
            else if (dir === 1) x++;
            else if (dir === 2) y--;
            else x--;
        } else if (ch === 'L') {
            dir = (dir + 3) % 4;
        } else if (ch === 'R') {
            dir = (dir + 1) % 4;
        }
    }
    return (x === 0 && y === 0) || dir !== 0;
};
```

## Typescript

```typescript
function isRobotBounded(instructions: string): boolean {
    let x = 0, y = 0;
    let dir = 0; // 0:N, 1:E, 2:S, 3:W
    for (const c of instructions) {
        if (c === 'G') {
            if (dir === 0) y++;
            else if (dir === 1) x++;
            else if (dir === 2) y--;
            else x--;
        } else if (c === 'L') {
            dir = (dir + 3) % 4;
        } else { // 'R'
            dir = (dir + 1) % 4;
        }
    }
    return (x === 0 && y === 0) || dir !== 0;
}
```

## Php

```php
class Solution {

    /**
     * @param String $instructions
     * @return Boolean
     */
    function isRobotBounded($instructions) {
        $x = 0;
        $y = 0;
        // 0: north, 1: east, 2: south, 3: west
        $dir = 0;
        $len = strlen($instructions);
        for ($i = 0; $i < $len; $i++) {
            $c = $instructions[$i];
            if ($c === 'G') {
                switch ($dir) {
                    case 0: $y++; break; // north
                    case 1: $x++; break; // east
                    case 2: $y--; break; // south
                    case 3: $x--; break; // west
                }
            } elseif ($c === 'L') {
                $dir = ($dir + 3) % 4; // turn left
            } else { // 'R'
                $dir = ($dir + 1) % 4; // turn right
            }
        }
        return ($x == 0 && $y == 0) || $dir != 0;
    }
}
```

## Swift

```swift
class Solution {
    func isRobotBounded(_ instructions: String) -> Bool {
        var x = 0, y = 0
        var dir = 0 // 0:N, 1:E, 2:S, 3:W
        let moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for ch in instructions {
            switch ch {
            case "G":
                x += moves[dir].0
                y += moves[dir].1
            case "L":
                dir = (dir + 3) % 4
            case "R":
                dir = (dir + 1) % 4
            default:
                break
            }
        }
        
        return (x == 0 && y == 0) || dir != 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isRobotBounded(instructions: String): Boolean {
        var x = 0
        var y = 0
        // 0:N, 1:E, 2:S, 3:W
        var dir = 0
        for (c in instructions) {
            when (c) {
                'G' -> {
                    when (dir) {
                        0 -> y++
                        1 -> x++
                        2 -> y--
                        3 -> x--
                    }
                }
                'L' -> dir = (dir + 3) % 4
                'R' -> dir = (dir + 1) % 4
            }
        }
        return (x == 0 && y == 0) || dir != 0
    }
}
```

## Dart

```dart
class Solution {
  bool isRobotBounded(String instructions) {
    int x = 0, y = 0;
    // 0: north, 1: east, 2: south, 3: west
    int dir = 0;
    for (int i = 0; i < instructions.length; i++) {
      final ch = instructions[i];
      if (ch == 'G') {
        switch (dir) {
          case 0:
            y += 1;
            break;
          case 1:
            x += 1;
            break;
          case 2:
            y -= 1;
            break;
          case 3:
            x -= 1;
            break;
        }
      } else if (ch == 'L') {
        dir = (dir + 3) % 4; // turn left
      } else if (ch == 'R') {
        dir = (dir + 1) % 4; // turn right
      }
    }
    return (x == 0 && y == 0) || dir != 0;
  }
}
```

## Golang

```go
func isRobotBounded(instructions string) bool {
	x, y := 0, 0
	dir := 0 // 0:N,1:E,2:S,3:W
	dx := []int{0, 1, 0, -1}
	dy := []int{1, 0, -1, 0}

	for i := 0; i < len(instructions); i++ {
		switch instructions[i] {
		case 'G':
			x += dx[dir]
			y += dy[dir]
		case 'L':
			dir = (dir + 3) % 4
		case 'R':
			dir = (dir + 1) % 4
		}
	}
	return (x == 0 && y == 0) || dir != 0
}
```

## Ruby

```ruby
def is_robot_bounded(instructions)
  x = y = 0
  dir = 0 # 0:N,1:E,2:S,3:W
  instructions.each_char do |c|
    case c
    when 'G'
      case dir
      when 0 then y += 1
      when 1 then x += 1
      when 2 then y -= 1
      else        # 3
        x -= 1
      end
    when 'L'
      dir = (dir + 3) % 4
    when 'R'
      dir = (dir + 1) % 4
    end
  end
  (x == 0 && y == 0) || dir != 0
end
```

## Scala

```scala
object Solution {
    def isRobotBounded(instructions: String): Boolean = {
        var x = 0
        var y = 0
        var dir = 0 // 0:N, 1:E, 2:S, 3:W
        for (c <- instructions) {
            c match {
                case 'G' =>
                    dir match {
                        case 0 => y += 1
                        case 1 => x += 1
                        case 2 => y -= 1
                        case 3 => x -= 1
                    }
                case 'L' => dir = (dir + 3) % 4
                case 'R' => dir = (dir + 1) % 4
                case _   =>
            }
        }
        (x == 0 && y == 0) || dir != 0
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_robot_bounded(instructions: String) -> bool {
        let mut x = 0;
        let mut y = 0;
        // 0: North, 1: East, 2: South, 3: West
        let mut dir = 0;
        for ch in instructions.chars() {
            match ch {
                'G' => match dir {
                    0 => y += 1,
                    1 => x += 1,
                    2 => y -= 1,
                    3 => x -= 1,
                    _ => {}
                },
                'L' => dir = (dir + 3) % 4,
                'R' => dir = (dir + 1) % 4,
                _ => {}
            }
        }
        (x == 0 && y == 0) || dir != 0
    }
}
```

## Racket

```racket
(define/contract (is-robot-bounded instructions)
  (-> string? boolean?)
  (let* ((dx '#(0 1 0 -1))
         (dy '#(1 0 -1 0)))
    (let loop ((i 0) (x 0) (y 0) (dir 0)) ; dir: 0=N,1=E,2=S,3=W
      (if (= i (string-length instructions))
          (or (and (= x 0) (= y 0)) (not (= dir 0)))
          (let ((c (string-ref instructions i)))
            (cond
              [(char=? c #\G)
               (loop (+ i 1)
                     (+ x (vector-ref dx dir))
                     (+ y (vector-ref dy dir))
                     dir)]
              [(char=? c #\L)
               (loop (+ i 1) x y (modulo (+ dir 3) 4))]
              [(char=? c #\R)
               (loop (+ i 1) x y (modulo (+ dir 1) 4))]))))))
```

## Erlang

```erlang
-spec is_robot_bounded(Instructions :: unicode:unicode_binary()) -> boolean().
is_robot_bounded(Instructions) ->
    {X, Y, Dir} = lists:foldl(fun process_char/2, {0, 0, 0}, binary_to_list(Instructions)),
    (X == 0 andalso Y == 0) orelse Dir =/= 0.

process_char(Char, {X, Y, Dir}) ->
    case Char of
        $G ->
            case Dir of
                0 -> {X, Y + 1, Dir};
                1 -> {X + 1, Y, Dir};
                2 -> {X, Y - 1, Dir};
                3 -> {X - 1, Y, Dir}
            end;
        $L ->
            NewDir = (Dir + 3) rem 4,
            {X, Y, NewDir};
        $R ->
            NewDir = (Dir + 1) rem 4,
            {X, Y, NewDir}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_robot_bounded(instructions :: String.t) :: boolean
  def is_robot_bounded(instructions) do
    {x, y, dir} =
      instructions
      |> String.graphemes()
      |> Enum.reduce({0, 0, 0}, fn ch, {x, y, d} ->
        case ch do
          "G" ->
            case d do
              0 -> {x, y + 1, d}
              1 -> {x + 1, y, d}
              2 -> {x, y - 1, d}
              3 -> {x - 1, y, d}
            end

          "L" ->
            {x, y, rem(d + 3, 4)}

          "R" ->
            {x, y, rem(d + 1, 4)}
        end
      end)

    dir != 0 or (x == 0 and y == 0)
  end
end
```
