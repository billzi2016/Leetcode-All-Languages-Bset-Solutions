# 1496. Path Crossing

## Cpp

```cpp
class Solution {
public:
    bool isPathCrossing(string path) {
        unordered_set<long long> visited;
        int x = 0, y = 0;
        auto encode = [&](int a, int b) -> long long {
            return (static_cast<long long>(a) << 32) ^ (b & 0xffffffffLL);
        };
        visited.insert(encode(x, y));
        for (char c : path) {
            if (c == 'N') ++y;
            else if (c == 'S') --y;
            else if (c == 'E') ++x;
            else if (c == 'W') --x;
            long long key = encode(x, y);
            if (visited.count(key)) return true;
            visited.insert(key);
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean isPathCrossing(String path) {
        java.util.HashSet<String> visited = new java.util.HashSet<>();
        int x = 0, y = 0;
        visited.add("0,0");
        for (char c : path.toCharArray()) {
            switch (c) {
                case 'N': y++; break;
                case 'S': y--; break;
                case 'E': x++; break;
                case 'W': x--; break;
            }
            String key = x + "," + y;
            if (!visited.add(key)) {
                return true;
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        x = y = 0
        visited = {(0, 0)}
        moves = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
        for c in path:
            dx, dy = moves[c]
            x += dx
            y += dy
            if (x, y) in visited:
                return True
            visited.add((x, y))
        return False
```

## Python3

```python
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = y = 0
        visited = {(0, 0)}
        moves = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
        for c in path:
            dx, dy = moves[c]
            x += dx
            y += dy
            if (x, y) in visited:
                return True
            visited.add((x, y))
        return False
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool isPathCrossing(char* path) {
    int x = 0, y = 0;
    int len = strlen(path);
    int capacity = len + 1;               // include starting point
    int *xs = (int *)malloc(capacity * sizeof(int));
    int *ys = (int *)malloc(capacity * sizeof(int));
    if (!xs || !ys) {
        // allocation failure, treat as no crossing
        if (xs) free(xs);
        if (ys) free(ys);
        return false;
    }

    int count = 0;
    xs[count] = x;
    ys[count] = y;
    ++count;

    for (int i = 0; path[i]; ++i) {
        char c = path[i];
        if (c == 'N') ++y;
        else if (c == 'S') --y;
        else if (c == 'E') ++x;
        else if (c == 'W') --x;

        for (int j = 0; j < count; ++j) {
            if (xs[j] == x && ys[j] == y) {
                free(xs);
                free(ys);
                return true;
            }
        }

        xs[count] = x;
        ys[count] = y;
        ++count;
    }

    free(xs);
    free(ys);
    return false;
}
```

## Csharp

```csharp
public class Solution
{
    public bool IsPathCrossing(string path)
    {
        var visited = new HashSet<(int, int)>();
        int x = 0, y = 0;
        visited.Add((x, y));

        foreach (char c in path)
        {
            switch (c)
            {
                case 'N': y++; break;
                case 'S': y--; break;
                case 'E': x++; break;
                case 'W': x--; break;
            }

            var pos = (x, y);
            if (!visited.Add(pos))
                return true;
        }

        return false;
    }
}
```

## Javascript

```javascript
var isPathCrossing = function(path) {
    const visited = new Set();
    let x = 0, y = 0;
    visited.add('0,0');
    for (let i = 0; i < path.length; i++) {
        const c = path[i];
        if (c === 'N') y++;
        else if (c === 'S') y--;
        else if (c === 'E') x++;
        else if (c === 'W') x--;
        const key = `${x},${y}`;
        if (visited.has(key)) return true;
        visited.add(key);
    }
    return false;
};
```

## Typescript

```typescript
function isPathCrossing(path: string): boolean {
    const visited = new Set<string>();
    let x = 0, y = 0;
    visited.add("0,0");
    for (const ch of path) {
        if (ch === 'N') y++;
        else if (ch === 'S') y--;
        else if (ch === 'E') x++;
        else if (ch === 'W') x--;
        const key = `${x},${y}`;
        if (visited.has(key)) return true;
        visited.add(key);
    }
    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param String $path
     * @return Boolean
     */
    function isPathCrossing($path) {
        $x = 0;
        $y = 0;
        $visited = [];
        $visited["0,0"] = true;

        $len = strlen($path);
        for ($i = 0; $i < $len; $i++) {
            switch ($path[$i]) {
                case 'N':
                    $y += 1;
                    break;
                case 'S':
                    $y -= 1;
                    break;
                case 'E':
                    $x += 1;
                    break;
                case 'W':
                    $x -= 1;
                    break;
            }
            $key = $x . ',' . $y;
            if (isset($visited[$key])) {
                return true;
            }
            $visited[$key] = true;
        }

        return false;
    }
}
```

## Swift

```swift
class Solution {
    func isPathCrossing(_ path: String) -> Bool {
        var visited = Set<(Int, Int)>()
        var x = 0
        var y = 0
        visited.insert((x, y))
        
        for ch in path {
            switch ch {
            case "N":
                y += 1
            case "S":
                y -= 1
            case "E":
                x += 1
            case "W":
                x -= 1
            default:
                continue
            }
            if visited.contains((x, y)) {
                return true
            }
            visited.insert((x, y))
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isPathCrossing(path: String): Boolean {
        var x = 0
        var y = 0
        val visited = HashSet<Pair<Int, Int>>()
        visited.add(Pair(0, 0))
        for (c in path) {
            when (c) {
                'N' -> y++
                'S' -> y--
                'E' -> x++
                'W' -> x--
            }
            val point = Pair(x, y)
            if (!visited.add(point)) return true
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool isPathCrossing(String path) {
    int x = 0, y = 0;
    final visited = <String>{'0,0'};
    for (int i = 0; i < path.length; i++) {
      switch (path[i]) {
        case 'N':
          y++;
          break;
        case 'S':
          y--;
          break;
        case 'E':
          x++;
          break;
        case 'W':
          x--;
          break;
      }
      final key = '$x,$y';
      if (!visited.add(key)) return true;
    }
    return false;
  }
}
```

## Golang

```go
func isPathCrossing(path string) bool {
    visited := make(map[[2]int]bool)
    x, y := 0, 0
    visited[[2]int{x, y}] = true

    for i := 0; i < len(path); i++ {
        switch path[i] {
        case 'N':
            y++
        case 'S':
            y--
        case 'E':
            x++
        case 'W':
            x--
        }
        coord := [2]int{x, y}
        if visited[coord] {
            return true
        }
        visited[coord] = true
    }
    return false
}
```

## Ruby

```ruby
require 'set'

# @param {String} path
# @return {Boolean}
def is_path_crossing(path)
  visited = Set.new
  x = y = 0
  visited.add([x, y])
  path.each_char do |c|
    case c
    when 'N' then y += 1
    when 'S' then y -= 1
    when 'E' then x += 1
    when 'W' then x -= 1
    end
    return true if visited.include?([x, y])
    visited.add([x, y])
  end
  false
end
```

## Scala

```scala
object Solution {
    def isPathCrossing(path: String): Boolean = {
        val visited = scala.collection.mutable.HashSet[(Int, Int)]()
        var x = 0
        var y = 0
        visited.add((x, y))
        for (c <- path) {
            c match {
                case 'N' => y += 1
                case 'S' => y -= 1
                case 'E' => x += 1
                case 'W' => x -= 1
                case _   => // ignore invalid characters
            }
            if (visited.contains((x, y))) return true
            visited.add((x, y))
        }
        false
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn is_path_crossing(path: String) -> bool {
        let mut visited: HashSet<(i32, i32)> = HashSet::new();
        let (mut x, mut y) = (0_i32, 0_i32);
        visited.insert((x, y));
        for c in path.chars() {
            match c {
                'N' => y += 1,
                'S' => y -= 1,
                'E' => x += 1,
                'W' => x -= 1,
                _ => {}
            }
            if !visited.insert((x, y)) {
                return true;
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (is-path-crossing path)
  (-> string? boolean?)
  (let* ((visited (make-hash))
         (add-visit (lambda (x y) (hash-set! visited (list x y) #t)))
         (has-visited? (lambda (x y) (hash-has-key? visited (list x y)))))
    (add-visit 0 0)
    (let loop ((i 0) (x 0) (y 0))
      (if (= i (string-length path))
          #f
          (let* ((c (string-ref path i))
                 (dx (cond [(char=? c #\N) 0]
                           [(char=? c #\S) 0]
                           [(char=? c #\E) 1]
                           [(char=? c #\W) -1]))
                 (dy (cond [(char=? c #\N) 1]
                           [(char=? c #\S) -1]
                           [(char=? c #\E) 0]
                           [(char=? c #\W) 0]))
                 (nx (+ x dx))
                 (ny (+ y dy)))
            (if (has-visited? nx ny)
                #t
                (begin
                  (add-visit nx ny)
                  (loop (+ i 1) nx ny))))))))
```

## Erlang

```erlang
-export([is_path_crossing/1]).
-spec is_path_crossing(Path :: unicode:unicode_binary()) -> boolean().
is_path_crossing(Path) ->
    is_path_crossing(Path, 0, 0, #{ {0,0} => true }).

is_path_crossing(<<>>, _X, _Y, _Visited) ->
    false;
is_path_crossing(<<C, Rest/binary>>, X, Y, Visited) ->
    {DX,DY} = case C of
        $N -> {0,1};
        $S -> {0,-1};
        $E -> {1,0};
        $W -> {-1,0}
    end,
    NX = X + DX,
    NY = Y + DY,
    case maps:is_key({NX,NY}, Visited) of
        true -> true;
        false ->
            is_path_crossing(Rest, NX, NY, Visited#{ {NX,NY} => true })
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_path_crossing(path :: String.t) :: boolean
  def is_path_crossing(path) do
    result =
      Enum.reduce_while(String.graphemes(path), {0, 0, MapSet.new([{0, 0}])}, fn dir, {x, y, visited} ->
        {nx, ny} = case dir do
          "N" -> {x, y + 1}
          "S" -> {x, y - 1}
          "E" -> {x + 1, y}
          "W" -> {x - 1, y}
        end

        if MapSet.member?(visited, {nx, ny}) do
          {:halt, true}
        else
          {:cont, {nx, ny, MapSet.put(visited, {nx, ny})}}
        end
      end)

    case result do
      true -> true
      _ -> false
    end
  end
end
```
