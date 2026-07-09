# 1884. Egg Drop With 2 Eggs and N Floors

## Cpp

```cpp
class Solution {
public:
    int twoEggDrop(int n) {
        int m = 0;
        while (m * (m + 1) / 2 < n) {
            ++m;
        }
        return m;
    }
};
```

## Java

```java
class Solution {
    public int twoEggDrop(int n) {
        int moves = 0;
        while (moves * (moves + 1) / 2 < n) {
            moves++;
        }
        return moves;
    }
}
```

## Python

```python
class Solution(object):
    def twoEggDrop(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        return int(math.ceil((math.sqrt(1 + 8 * n) - 1) / 2))
```

## Python3

```python
class Solution:
    def twoEggDrop(self, n: int) -> int:
        import math
        return math.ceil((math.sqrt(1 + 8 * n) - 1) / 2)
```

## C

```c
int twoEggDrop(int n) {
    int moves = 0;
    while (moves * (moves + 1) / 2 < n) {
        ++moves;
    }
    return moves;
}
```

## Csharp

```csharp
public class Solution
{
    public int TwoEggDrop(int n)
    {
        int moves = 0;
        while (moves * (moves + 1) / 2 < n)
        {
            moves++;
        }
        return moves;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var twoEggDrop = function(n) {
    let m = 0;
    while (m * (m + 1) / 2 < n) {
        m++;
    }
    return m;
};
```

## Typescript

```typescript
function twoEggDrop(n: number): number {
    let moves = 0;
    while (moves * (moves + 1) / 2 < n) {
        moves++;
    }
    return moves;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function twoEggDrop($n) {
        $moves = ceil(( -1 + sqrt(1 + 8 * $n) ) / 2);
        return (int)$moves;
    }
}
```

## Swift

```swift
class Solution {
    func twoEggDrop(_ n: Int) -> Int {
        var moves = 0
        var covered = 0
        while covered < n {
            moves += 1
            covered += moves
        }
        return moves
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun twoEggDrop(n: Int): Int {
        var moves = 0
        var covered = 0
        while (covered < n) {
            moves++
            covered += moves
        }
        return moves
    }
}
```

## Dart

```dart
class Solution {
  int twoEggDrop(int n) {
    int m = 0;
    while ((m * (m + 1)) ~/ 2 < n) {
      m++;
    }
    return m;
  }
}
```

## Golang

```go
func twoEggDrop(n int) int {
	moves, total := 0, 0
	for total < n {
		moves++
		total += moves
	}
	return moves
}
```

## Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def two_egg_drop(n)
  moves = 0
  total = 0
  while total < n
    moves += 1
    total += moves
  end
  moves
end
```

## Scala

```scala
object Solution {
    def twoEggDrop(n: Int): Int = {
        var moves = 0
        var covered = 0L
        while (covered < n) {
            moves += 1
            covered += moves
        }
        moves
    }
}
```

## Rust

```rust
impl Solution {
    pub fn two_egg_drop(n: i32) -> i32 {
        let mut moves = 0;
        let mut covered = 0;
        while covered < n {
            moves += 1;
            covered += moves;
        }
        moves
    }
}
```

## Racket

```racket
(define/contract (two-egg-drop n)
  (-> exact-integer? exact-integer?)
  (let loop ((m 0) (tri 0))
    (if (>= tri n)
        m
        (loop (+ m 1) (+ tri (+ m 1))))))
```

## Erlang

```erlang
-spec two_egg_drop(N :: integer()) -> integer().
two_egg_drop(N) when N =< 0 ->
    0;
two_egg_drop(N) ->
    find_moves(N, 1).

find_moves(N, M) ->
    case (M * (M + 1)) div 2 >= N of
        true -> M;
        false -> find_moves(N, M + 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec two_egg_drop(n :: integer) :: integer
  def two_egg_drop(n) when n > 0 do
    find_moves(1, 0, n)
  end

  defp find_moves(step, acc, target) do
    if acc + step >= target do
      step
    else
      find_moves(step + 1, acc + step, target)
    end
  end
end
```
