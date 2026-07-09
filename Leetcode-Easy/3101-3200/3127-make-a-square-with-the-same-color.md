# 3127. Make a Square with the Same Color

## Cpp

```cpp
class Solution {
public:
    bool canMakeSquare(vector<vector<char>>& grid) {
        for (int i = 0; i < 2; ++i) {
            for (int j = 0; j < 2; ++j) {
                int cntB = 0;
                cntB += grid[i][j] == 'B';
                cntB += grid[i+1][j] == 'B';
                cntB += grid[i][j+1] == 'B';
                cntB += grid[i+1][j+1] == 'B';
                if (cntB >= 3 || cntB <= 1) return true; // cntW = 4 - cntB, so cntW>=3 <=> cntB<=1
            }
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean canMakeSquare(char[][] grid) {
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                int bCount = 0;
                int wCount = 0;
                // top-left cell of the 2x2 square
                if (grid[i][j] == 'B') bCount++; else wCount++;
                // top-right
                if (grid[i][j + 1] == 'B') bCount++; else wCount++;
                // bottom-left
                if (grid[i + 1][j] == 'B') bCount++; else wCount++;
                // bottom-right
                if (grid[i + 1][j + 1] == 'B') bCount++; else wCount++;
                
                // already uniform or can become uniform by changing at most one cell
                if (bCount >= 3 || wCount >= 3) {
                    return true;
                }
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def canMakeSquare(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        for i in range(2):
            for j in range(2):
                cntB = 0
                cntB += grid[i][j] == 'B'
                cntB += grid[i+1][j] == 'B'
                cntB += grid[i][j+1] == 'B'
                cntB += grid[i+1][j+1] == 'B'
                if cntB >= 3 or (4 - cntB) >= 3:
                    return True
        return False
```

## Python3

```python
from typing import List

class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for i in range(2):
            for j in range(2):
                cntB = (grid[i][j] == 'B') + (grid[i+1][j] == 'B') + (grid[i][j+1] == 'B') + (grid[i+1][j+1] == 'B')
                if cntB != 2:
                    return True
        return False
```

## C

```c
#include <stdbool.h>

bool canMakeSquare(char** grid, int gridSize, int* gridColSize) {
    (void)gridSize; // unused, always 3
    (void)gridColSize; // unused, always 3
    
    for (int i = 0; i < 2; ++i) {
        for (int j = 0; j < 2; ++j) {
            int cntB = 0, cntW = 0;
            if (grid[i][j] == 'B') cntB++; else cntW++;
            if (grid[i][j+1] == 'B') cntB++; else cntW++;
            if (grid[i+1][j] == 'B') cntB++; else cntW++;
            if (grid[i+1][j+1] == 'B') cntB++; else cntW++;
            if (cntB >= 3 || cntW >= 3) {
                return true;
            }
        }
    }
    return false;
}
```

## Csharp

```csharp
public class Solution {
    public bool CanMakeSquare(char[][] grid) {
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                int bCount = 0;
                if (grid[i][j] == 'B') bCount++;
                if (grid[i + 1][j] == 'B') bCount++;
                if (grid[i][j + 1] == 'B') bCount++;
                if (grid[i + 1][j + 1] == 'B') bCount++;
                if (bCount != 2) return true;
            }
        }
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {character[][]} grid
 * @return {boolean}
 */
var canMakeSquare = function(grid) {
    for (let i = 0; i < 2; ++i) {
        for (let j = 0; j < 2; ++j) {
            let b = 0, w = 0;
            for (let di = 0; di < 2; ++di) {
                for (let dj = 0; dj < 2; ++dj) {
                    if (grid[i + di][j + dj] === 'B') b++;
                    else w++;
                }
            }
            if (b >= 3 || w >= 3) return true;
        }
    }
    return false;
};
```

## Typescript

```typescript
function canMakeSquare(grid: string[][]): boolean {
    for (let i = 0; i < 2; i++) {
        for (let j = 0; j < 2; j++) {
            let b = 0, w = 0;
            for (let di = 0; di < 2; di++) {
                for (let dj = 0; dj < 2; dj++) {
                    if (grid[i + di][j + dj] === 'B') b++;
                    else w++;
                }
            }
            if (b >= 3 || w >= 3) return true;
        }
    }
    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param String[][] $grid
     * @return Boolean
     */
    function canMakeSquare($grid) {
        for ($i = 0; $i < 2; $i++) {
            for ($j = 0; $j < 2; $j++) {
                $bCount = 0;
                $wCount = 0;
                // top-left
                if ($grid[$i][$j] === 'B') $bCount++; else $wCount++;
                // top-right
                if ($grid[$i][$j + 1] === 'B') $bCount++; else $wCount++;
                // bottom-left
                if ($grid[$i + 1][$j] === 'B') $bCount++; else $wCount++;
                // bottom-right
                if ($grid[$i + 1][$j + 1] === 'B') $bCount++; else $wCount++;

                if (max($bCount, $wCount) >= 3) {
                    return true;
                }
            }
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func canMakeSquare(_ grid: [[Character]]) -> Bool {
        for i in 0..<2 {
            for j in 0..<2 {
                var bCount = 0
                var wCount = 0
                let positions = [(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)]
                for (x, y) in positions {
                    if grid[x][y] == "B" {
                        bCount += 1
                    } else {
                        wCount += 1
                    }
                }
                if bCount >= 3 || wCount >= 3 {
                    return true
                }
            }
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canMakeSquare(grid: Array<CharArray>): Boolean {
        for (i in 0..1) {
            for (j in 0..1) {
                var b = 0
                var w = 0
                for (dx in 0..1) {
                    for (dy in 0..1) {
                        if (grid[i + dx][j + dy] == 'B') b++ else w++
                    }
                }
                if (b >= 3 || w >= 3) return true
            }
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool canMakeSquare(List<List<String>> grid) {
    for (int i = 0; i < 2; ++i) {
      for (int j = 0; j < 2; ++j) {
        int bCount = 0;
        if (grid[i][j] == 'B') bCount++;
        if (grid[i + 1][j] == 'B') bCount++;
        if (grid[i][j + 1] == 'B') bCount++;
        if (grid[i + 1][j + 1] == 'B') bCount++;
        int wCount = 4 - bCount;
        if (bCount >= 3 || wCount >= 3) return true;
      }
    }
    return false;
  }
}
```

## Golang

```go
func canMakeSquare(grid [][]byte) bool {
	for i := 0; i < 2; i++ {
		for j := 0; j < 2; j++ {
			cnt := 0
			if grid[i][j] == 'B' {
				cnt++
			}
			if grid[i+1][j] == 'B' {
				cnt++
			}
			if grid[i][j+1] == 'B' {
				cnt++
			}
			if grid[i+1][j+1] == 'B' {
				cnt++
			}
			if cnt != 2 {
				return true
			}
		}
	}
	return false
}
```

## Ruby

```ruby
def can_make_square(grid)
  (0..1).each do |i|
    (0..1).each do |j|
      b = 0
      2.times do |dx|
        2.times do |dy|
          b += 1 if grid[i + dx][j + dy] == 'B'
        end
      end
      w = 4 - b
      return true if b >= 3 || w >= 3
    end
  end
  false
end
```

## Scala

```scala
object Solution {
    def canMakeSquare(grid: Array[Array[Char]]): Boolean = {
        for (i <- 0 until 2; j <- 0 until 2) {
            var b = 0
            var w = 0
            for (dx <- 0 to 1; dy <- 0 to 1) {
                if (grid(i + dx)(j + dy) == 'B') b += 1 else w += 1
            }
            if (b >= 3 || w >= 3) return true
        }
        false
    }
}
```

## Rust

```rust
impl Solution {
    pub fn can_make_square(grid: Vec<Vec<char>>) -> bool {
        for i in 0..2 {
            for j in 0..2 {
                let mut b = 0;
                if grid[i][j] == 'B' { b += 1; }
                if grid[i + 1][j] == 'B' { b += 1; }
                if grid[i][j + 1] == 'B' { b += 1; }
                if grid[i + 1][j + 1] == 'B' { b += 1; }
                let w = 4 - b;
                if b >= 3 || w >= 3 {
                    return true;
                }
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (can-make-square grid)
  (-> (listof (listof char?)) boolean?)
  (letrec ((cell (lambda (r c) (list-ref (list-ref grid r) c))))
    (let loop-i ((i 0))
      (if (> i 1)
          #f
          (let loop-j ((j 0))
            (if (> j 1)
                (loop-i (+ i 1))
                (let* ((c1 (cell i j))
                       (c2 (cell i (+ j 1)))
                       (c3 (cell (+ i 1) j))
                       (c4 (cell (+ i 1) (+ j 1)))
                       (b-count (+ (if (char=? c1 #\B) 1 0)
                                   (if (char=? c2 #\B) 1 0)
                                   (if (char=? c3 #\B) 1 0)
                                   (if (char=? c4 #\B) 1 0)))
                       (w-count (- 4 b-count)))
                  (if (or (>= b-count 3) (>= w-count 3))
                      #t
                      (loop-j (+ j 1)))))))))))
```

## Erlang

```erlang
-spec can_make_square(Grid :: [[char()]]) -> boolean().
can_make_square(Grid) ->
    Squares = [{0,0},{0,1},{1,0},{1,1}],
    check_squares(Squares, Grid).

check_squares([], _Grid) -> false;
check_squares([Pos|Rest], Grid) ->
    {B,W} = count_square(Grid, Pos),
    case {B,W} of
        {4,_} -> true;
        {_,4} -> true;
        {3,1} -> true;
        {1,3} -> true;
        _ -> check_squares(Rest, Grid)
    end.

count_square(Grid,{I,J}) ->
    C1 = cell(Grid, I,   J),
    C2 = cell(Grid, I+1, J),
    C3 = cell(Grid, I,   J+1),
    C4 = cell(Grid, I+1, J+1),
    count([C1,C2,C3,C4]).

cell(Grid, I, J) ->
    Row = lists:nth(I+1, Grid),
    lists:nth(J+1, Row).

count(List) -> count(List, 0, 0).
count([], B,W) -> {B,W};
count([C|Rest], B,W) ->
    case C of
        $B -> count(Rest, B+1, W);
        $W -> count(Rest, B,   W+1);
        _  -> count(Rest, B,   W)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec can_make_square(grid :: [[char]]) :: boolean
  def can_make_square(grid) do
    conditions =
      for i <- 0..1, j <- 0..1 do
        a = grid |> Enum.at(i) |> Enum.at(j)
        b = grid |> Enum.at(i) |> Enum.at(j + 1)
        c = grid |> Enum.at(i + 1) |> Enum.at(j)
        d = grid |> Enum.at(i + 1) |> Enum.at(j + 1)

        b_count = Enum.count([a, b, c, d], fn x -> x == "B" end)
        max(b_count, 4 - b_count) >= 3
      end

    Enum.any?(conditions)
  end
end
```
