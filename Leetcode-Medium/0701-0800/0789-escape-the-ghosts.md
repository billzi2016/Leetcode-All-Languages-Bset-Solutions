# 0789. Escape The Ghosts

## Cpp

```cpp
class Solution {
public:
    bool escapeGhosts(vector<vector<int>>& ghosts, vector<int>& target) {
        int myDist = abs(target[0]) + abs(target[1]);
        for (const auto& g : ghosts) {
            int ghostDist = abs(g[0] - target[0]) + abs(g[1] - target[1]);
            if (ghostDist <= myDist) return false;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean escapeGhosts(int[][] ghosts, int[] target) {
        int myDist = Math.abs(target[0]) + Math.abs(target[1]);
        for (int[] g : ghosts) {
            int ghostDist = Math.abs(g[0] - target[0]) + Math.abs(g[1] - target[1]);
            if (ghostDist <= myDist) {
                return false;
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        player_dist = abs(target[0]) + abs(target[1])
        for gx, gy in ghosts:
            if abs(gx - target[0]) + abs(gy - target[1]) <= player_dist:
                return False
        return True
```

## Python3

```python
from typing import List

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        player_dist = abs(target[0]) + abs(target[1])
        for gx, gy in ghosts:
            if abs(gx - target[0]) + abs(gy - target[1]) <= player_dist:
                return False
        return True
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

bool escapeGhosts(int** ghosts, int ghostsSize, int* ghostsColSize, int* target, int targetSize) {
    int playerDist = abs(target[0]) + abs(target[1]);
    for (int i = 0; i < ghostsSize; ++i) {
        int gx = ghosts[i][0];
        int gy = ghosts[i][1];
        int dist = abs(gx - target[0]) + abs(gy - target[1]);
        if (dist <= playerDist) {
            return false;
        }
    }
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool EscapeGhosts(int[][] ghosts, int[] target) {
        int playerDist = Math.Abs(target[0]) + Math.Abs(target[1]);
        foreach (var g in ghosts) {
            int ghostDist = Math.Abs(g[0] - target[0]) + Math.Abs(g[1] - target[1]);
            if (ghostDist <= playerDist) return false;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} ghosts
 * @param {number[]} target
 * @return {boolean}
 */
var escapeGhosts = function(ghosts, target) {
    const playerDist = Math.abs(target[0]) + Math.abs(target[1]);
    for (const g of ghosts) {
        const ghostDist = Math.abs(g[0] - target[0]) + Math.abs(g[1] - target[1]);
        if (ghostDist <= playerDist) return false;
    }
    return true;
};
```

## Typescript

```typescript
function escapeGhosts(ghosts: number[][], target: number[]): boolean {
    const myDist = Math.abs(target[0]) + Math.abs(target[1]);
    for (const g of ghosts) {
        const ghostDist = Math.abs(g[0] - target[0]) + Math.abs(g[1] - target[1]);
        if (ghostDist <= myDist) return false;
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $ghosts
     * @param Integer[] $target
     * @return Boolean
     */
    function escapeGhosts($ghosts, $target) {
        $playerDist = abs($target[0]) + abs($target[1]);
        foreach ($ghosts as $g) {
            $dist = abs($g[0] - $target[0]) + abs($g[1] - $target[1]);
            if ($dist <= $playerDist) {
                return false;
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func escapeGhosts(_ ghosts: [[Int]], _ target: [Int]) -> Bool {
        let myDist = abs(target[0]) + abs(target[1])
        for ghost in ghosts {
            let dist = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])
            if dist <= myDist {
                return false
            }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun escapeGhosts(ghosts: Array<IntArray>, target: IntArray): Boolean {
        val playerDist = kotlin.math.abs(target[0]) + kotlin.math.abs(target[1])
        for (g in ghosts) {
            val ghostDist = kotlin.math.abs(g[0] - target[0]) + kotlin.math.abs(g[1] - target[1])
            if (ghostDist <= playerDist) return false
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool escapeGhosts(List<List<int>> ghosts, List<int> target) {
    int playerDist = target[0].abs() + target[1].abs();
    for (var g in ghosts) {
      int ghostDist = (g[0] - target[0]).abs() + (g[1] - target[1]).abs();
      if (ghostDist <= playerDist) return false;
    }
    return true;
  }
}
```

## Golang

```go
func escapeGhosts(ghosts [][]int, target []int) bool {
	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}
	playerDist := abs(target[0]) + abs(target[1])
	for _, g := range ghosts {
		d := abs(g[0]-target[0]) + abs(g[1]-target[1])
		if d <= playerDist {
			return false
		}
	}
	return true
}
```

## Ruby

```ruby
def escape_ghosts(ghosts, target)
  my_dist = target[0].abs + target[1].abs
  ghosts.each do |g|
    return false if (g[0] - target[0]).abs + (g[1] - target[1]).abs <= my_dist
  end
  true
end
```

## Scala

```scala
object Solution {
    def escapeGhosts(ghosts: Array[Array[Int]], target: Array[Int]): Boolean = {
        val myDist = math.abs(target(0)) + math.abs(target(1))
        for (g <- ghosts) {
            val ghostDist = math.abs(g(0) - target(0)) + math.abs(g(1) - target(1))
            if (ghostDist <= myDist) return false
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn escape_ghosts(ghosts: Vec<Vec<i32>>, target: Vec<i32>) -> bool {
        let my_dist = (target[0].abs() + target[1].abs()) as i32;
        for g in ghosts.iter() {
            let dist = (g[0] - target[0]).abs() + (g[1] - target[1]).abs();
            if dist <= my_dist {
                return false;
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (escape-ghosts ghosts target)
  (-> (listof (listof exact-integer?)) (listof exact-integer?) boolean?)
  (let* ((player-dist (+ (abs (first target)) (abs (second target)))))
    (for/and ([g ghosts])
      (> (+ (abs (- (first g) (first target)))
            (abs (- (second g) (second target))))
         player-dist))))
```

## Erlang

```erlang
-module(solution).
-export([escape_ghosts/2]).

-spec escape_ghosts(Ghosts :: [[integer()]], Target :: [integer()]) -> boolean().
escape_ghosts(Ghosts, Target) ->
    [Tx, Ty] = Target,
    PlayerDist = manhattan({0,0}, {Tx,Ty}),
    case lists:any(fun(G) ->
        [Gx,Gy] = G,
        GhostDist = manhattan({Gx,Gy}, {Tx,Ty}),
        GhostDist =< PlayerDist
    end, Ghosts) of
        true -> false;
        false -> true
    end.

manhattan({X1,Y1},{X2,Y2}) ->
    erlang:abs(X1 - X2) + erlang:abs(Y1 - Y2).
```

## Elixir

```elixir
defmodule Solution do
  @spec escape_ghosts(ghosts :: [[integer]], target :: [integer]) :: boolean
  def escape_ghosts(ghosts, [tx, ty]) do
    player_dist = abs(tx) + abs(ty)

    Enum.all?(ghosts, fn [gx, gy] ->
      abs(gx - tx) + abs(gy - ty) > player_dist
    end)
  end
end
```
