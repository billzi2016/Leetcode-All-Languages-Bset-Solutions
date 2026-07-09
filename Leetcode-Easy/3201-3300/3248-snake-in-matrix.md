# 3248. Snake in Matrix

## Cpp

```cpp
class Solution {
public:
    int finalPositionOfSnake(int n, vector<string>& commands) {
        int r = 0, c = 0;
        for (const string& cmd : commands) {
            if (cmd == "UP") {
                --r;
            } else if (cmd == "DOWN") {
                ++r;
            } else if (cmd == "LEFT") {
                --c;
            } else if (cmd == "RIGHT") {
                ++c;
            }
        }
        return r * n + c;
    }
};
```

## Java

```java
class Solution {
    public int finalPositionOfSnake(int n, java.util.List<String> commands) {
        int row = 0;
        int col = 0;
        for (String cmd : commands) {
            switch (cmd) {
                case "UP":
                    row--;
                    break;
                case "DOWN":
                    row++;
                    break;
                case "LEFT":
                    col--;
                    break;
                case "RIGHT":
                    col++;
                    break;
                default:
                    // Should not happen based on constraints
                    break;
            }
        }
        return row * n + col;
    }
}
```

## Python

```python
class Solution(object):
    def finalPositionOfSnake(self, n, commands):
        """
        :type n: int
        :type commands: List[str]
        :rtype: int
        """
        r, c = 0, 0
        for cmd in commands:
            if cmd == "UP":
                r -= 1
            elif cmd == "DOWN":
                r += 1
            elif cmd == "LEFT":
                c -= 1
            else:  # "RIGHT"
                c += 1
        return r * n + c
```

## Python3

```python
from typing import List

class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        row, col = 0, 0
        for cmd in commands:
            if cmd == "UP":
                row -= 1
            elif cmd == "DOWN":
                row += 1
            elif cmd == "LEFT":
                col -= 1
            elif cmd == "RIGHT":
                col += 1
        return row * n + col
```

## C

```c
#include <string.h>

int finalPositionOfSnake(int n, char** commands, int commandsSize) {
    int row = 0, col = 0;
    for (int i = 0; i < commandsSize; ++i) {
        if (strcmp(commands[i], "UP") == 0) {
            --row;
        } else if (strcmp(commands[i], "DOWN") == 0) {
            ++row;
        } else if (strcmp(commands[i], "LEFT") == 0) {
            --col;
        } else if (strcmp(commands[i], "RIGHT") == 0) {
            ++col;
        }
    }
    return row * n + col;
}
```

## Csharp

```csharp
public class Solution {
    public int FinalPositionOfSnake(int n, IList<string> commands) {
        int row = 0, col = 0;
        foreach (var cmd in commands) {
            switch (cmd) {
                case "UP":
                    row--;
                    break;
                case "DOWN":
                    row++;
                    break;
                case "LEFT":
                    col--;
                    break;
                case "RIGHT":
                    col++;
                    break;
            }
        }
        return row * n + col;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {string[]} commands
 * @return {number}
 */
var finalPositionOfSnake = function(n, commands) {
    let row = 0, col = 0;
    for (const cmd of commands) {
        if (cmd === "UP") {
            row--;
        } else if (cmd === "DOWN") {
            row++;
        } else if (cmd === "LEFT") {
            col--;
        } else if (cmd === "RIGHT") {
            col++;
        }
    }
    return row * n + col;
};
```

## Typescript

```typescript
function finalPositionOfSnake(n: number, commands: string[]): number {
    let row = 0, col = 0;
    for (const cmd of commands) {
        if (cmd === "UP") row--;
        else if (cmd === "DOWN") row++;
        else if (cmd === "LEFT") col--;
        else if (cmd === "RIGHT") col++;
    }
    return row * n + col;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param String[] $commands
     * @return Integer
     */
    function finalPositionOfSnake($n, $commands) {
        $row = 0;
        $col = 0;
        foreach ($commands as $cmd) {
            switch ($cmd) {
                case "UP":
                    $row--;
                    break;
                case "DOWN":
                    $row++;
                    break;
                case "LEFT":
                    $col--;
                    break;
                case "RIGHT":
                    $col++;
                    break;
            }
        }
        return $row * $n + $col;
    }
}
```

## Swift

```swift
class Solution {
    func finalPositionOfSnake(_ n: Int, _ commands: [String]) -> Int {
        var row = 0
        var col = 0
        for cmd in commands {
            switch cmd {
            case "UP":
                row -= 1
            case "DOWN":
                row += 1
            case "LEFT":
                col -= 1
            case "RIGHT":
                col += 1
            default:
                break
            }
        }
        return row * n + col
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun finalPositionOfSnake(n: Int, commands: List<String>): Int {
        var row = 0
        var col = 0
        for (cmd in commands) {
            when (cmd) {
                "UP" -> row--
                "DOWN" -> row++
                "LEFT" -> col--
                "RIGHT" -> col++
            }
        }
        return row * n + col
    }
}
```

## Dart

```dart
class Solution {
  int finalPositionOfSnake(int n, List<String> commands) {
    int row = 0;
    int col = 0;
    for (var cmd in commands) {
      switch (cmd) {
        case 'UP':
          row--;
          break;
        case 'DOWN':
          row++;
          break;
        case 'LEFT':
          col--;
          break;
        case 'RIGHT':
          col++;
          break;
      }
    }
    return row * n + col;
  }
}
```

## Golang

```go
func finalPositionOfSnake(n int, commands []string) int {
    row, col := 0, 0
    for _, cmd := range commands {
        switch cmd {
        case "UP":
            row--
        case "DOWN":
            row++
        case "LEFT":
            col--
        case "RIGHT":
            col++
        }
    }
    return row*n + col
}
```

## Ruby

```ruby
# @param {Integer} n
# @param {String[]} commands
# @return {Integer}
def final_position_of_snake(n, commands)
  row = 0
  col = 0

  commands.each do |cmd|
    case cmd
    when "UP"
      row -= 1
    when "DOWN"
      row += 1
    when "LEFT"
      col -= 1
    when "RIGHT"
      col += 1
    end
  end

  row * n + col
end
```

## Scala

```scala
object Solution {
    def finalPositionOfSnake(n: Int, commands: List[String]): Int = {
        var row = 0
        var col = 0
        for (cmd <- commands) {
            cmd match {
                case "UP" => row -= 1
                case "DOWN" => row += 1
                case "LEFT" => col -= 1
                case "RIGHT" => col += 1
                case _ => // do nothing
            }
        }
        row * n + col
    }
}
```

## Rust

```rust
impl Solution {
    pub fn final_position_of_snake(n: i32, commands: Vec<String>) -> i32 {
        let mut row = 0i32;
        let mut col = 0i32;
        for cmd in commands.iter() {
            match cmd.as_str() {
                "UP" => row -= 1,
                "DOWN" => row += 1,
                "LEFT" => col -= 1,
                "RIGHT" => col += 1,
                _ => {}
            }
        }
        row * n + col
    }
}
```

## Racket

```racket
(define/contract (final-position-of-snake n commands)
  (-> exact-integer? (listof string?) exact-integer?)
  (let loop ((row 0) (col 0) (cmds commands))
    (if (null? cmds)
        (+ (* row n) col)
        (let* ((cmd (car cmds))
               (new-row (cond [(string=? cmd "UP")    (- row 1)]
                              [(string=? cmd "DOWN")  (+ row 1)]
                              [else row]))
               (new-col (cond [(string=? cmd "LEFT")  (- col 1)]
                              [(string=? cmd "RIGHT") (+ col 1)]
                              [else col])))
          (loop new-row new-col (cdr cmds))))))
```

## Erlang

```erlang
-spec final_position_of_snake(N :: integer(), Commands :: [unicode:unicode_binary()]) -> integer().
final_position_of_snake(N, Commands) ->
    {Row, Col} = lists:foldl(
        fun(Command, {R, C}) ->
            case Command of
                <<"UP">> -> {R - 1, C};
                <<"DOWN">> -> {R + 1, C};
                <<"LEFT">> -> {R, C - 1};
                <<"RIGHT">> -> {R, C + 1}
            end
        end,
        {0, 0},
        Commands),
    Row * N + Col.
```

## Elixir

```elixir
defmodule Solution do
  @spec final_position_of_snake(n :: integer, commands :: [String.t]) :: integer
  def final_position_of_snake(n, commands) do
    {row, col} =
      Enum.reduce(commands, {0, 0}, fn
        "UP", {r, c} -> {r - 1, c}
        "DOWN", {r, c} -> {r + 1, c}
        "LEFT", {r, c} -> {r, c - 1}
        "RIGHT", {r, c} -> {r, c + 1}
      end)

    row * n + col
  end
end
```
