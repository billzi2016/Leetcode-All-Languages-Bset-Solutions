# 3222. Find the Winning Player in Coin Game

## Cpp

```cpp
class Solution {
public:
    string winningPlayer(int x, int y) {
        int turns = min(x, y / 4);
        return (turns % 2 == 1) ? "Alice" : "Bob";
    }
};
```

## Java

```java
class Solution {
    public String winningPlayer(int x, int y) {
        int turns = Math.min(x, y / 4);
        return (turns % 2 == 1) ? "Alice" : "Bob";
    }
}
```

## Python

```python
class Solution(object):
    def winningPlayer(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: str
        """
        turns = min(x, y // 4)
        return "Alice" if turns % 2 == 1 else "Bob"
```

## Python3

```python
class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        turns = min(x, y // 4)
        return "Alice" if turns % 2 == 1 else "Bob"
```

## C

```c
char* winningPlayer(int x, int y) {
    int turns = x < y / 4 ? x : y / 4;
    return (turns % 2 == 1) ? "Alice" : "Bob";
}
```

## Csharp

```csharp
public class Solution {
    public string WinningPlayer(int x, int y) {
        int turns = Math.Min(x, y / 4);
        return (turns % 2 == 1) ? "Alice" : "Bob";
    }
}
```

## Javascript

```javascript
/**
 * @param {number} x
 * @param {number} y
 * @return {string}
 */
var winningPlayer = function(x, y) {
    const turns = Math.min(x, Math.floor(y / 4));
    return (turns % 2 === 1) ? "Alice" : "Bob";
};
```

## Typescript

```typescript
function winningPlayer(x: number, y: number): string {
    const turns = Math.min(x, Math.floor(y / 4));
    return turns % 2 === 1 ? "Alice" : "Bob";
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $x
     * @param Integer $y
     * @return String
     */
    function winningPlayer($x, $y) {
        $turns = min($x, intdiv($y, 4));
        return ($turns % 2 == 1) ? "Alice" : "Bob";
    }
}
```

## Swift

```swift
class Solution {
    func winningPlayer(_ x: Int, _ y: Int) -> String {
        let turns = min(x, y / 4)
        return turns % 2 == 1 ? "Alice" : "Bob"
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun winningPlayer(x: Int, y: Int): String {
        val turns = minOf(x, y / 4)
        return if (turns % 2 == 1) "Alice" else "Bob"
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  String winningPlayer(int x, int y) {
    int turns = min(x, y ~/ 4);
    return (turns % 2 == 1) ? "Alice" : "Bob";
  }
}
```

## Golang

```go
func winningPlayer(x int, y int) string {
	turns := x
	if y/4 < turns {
		turns = y / 4
	}
	if turns%2 == 1 {
		return "Alice"
	}
	return "Bob"
}
```

## Ruby

```ruby
def winning_player(x, y)
  turns = [x, y / 4].min
  turns.odd? ? "Alice" : "Bob"
end
```

## Scala

```scala
object Solution {
    def winningPlayer(x: Int, y: Int): String = {
        val turns = math.min(x, y / 4)
        if (turns % 2 == 1) "Alice" else "Bob"
    }
}
```

## Rust

```rust
impl Solution {
    pub fn winning_player(x: i32, y: i32) -> String {
        let turns = std::cmp::min(x, y / 4);
        if turns % 2 == 1 {
            "Alice".to_string()
        } else {
            "Bob".to_string()
        }
    }
}
```

## Racket

```racket
(define/contract (winning-player x y)
  (-> exact-integer? exact-integer? string?)
  (let* ([turns (min x (quotient y 4))])
    (if (odd? turns) "Alice" "Bob")))
```

## Erlang

```erlang
-spec winning_player(X :: integer(), Y :: integer()) -> unicode:unicode_binary().
winning_player(X, Y) ->
    Turns = erlang:min(X, Y div 4),
    case Turns rem 2 of
        1 -> <<"Alice">>;
        0 -> <<"Bob">>
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec winning_player(x :: integer, y :: integer) :: String.t()
  def winning_player(x, y) do
    turns = min(x, div(y, 4))
    if rem(turns, 2) == 1, do: "Alice", else: "Bob"
  end
end
```
