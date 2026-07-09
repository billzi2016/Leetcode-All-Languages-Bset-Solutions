# 2319. Check if Matrix Is X-Matrix

## Cpp

```cpp
class Solution {
public:
    bool checkXMatrix(vector<vector<int>>& grid) {
        int n = grid.size();
        for (int i = 0; i < n; ++i) {
            if ((int)grid[i].size() != n) return false;
            for (int j = 0; j < n; ++j) {
                bool onDiag = (i == j) || (i + j == n - 1);
                if (onDiag) {
                    if (grid[i][j] == 0) return false;
                } else {
                    if (grid[i][j] != 0) return false;
                }
            }
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean checkXMatrix(int[][] grid) {
        int n = grid.length;
        for (int i = 0; i < n; i++) {
            if (grid[i].length != n) return false; // safety, though constraints guarantee square
            for (int j = 0; j < n; j++) {
                boolean onDiagonal = (i == j) || (i + j == n - 1);
                if (onDiagonal) {
                    if (grid[i][j] == 0) return false;
                } else {
                    if (grid[i][j] != 0) return false;
                }
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def checkXMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if i == j or i + j == n - 1:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False
        return True
```

## Python3

```python
class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if i == j or i + j == n - 1:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False
        return True
```

## C

```c
#include <stdbool.h>

bool checkXMatrix(int** grid, int gridSize, int* gridColSize) {
    for (int i = 0; i < gridSize; ++i) {
        for (int j = 0; j < gridColSize[i]; ++j) {
            if (i == j || i == gridSize - 1 - j) {
                if (grid[i][j] == 0) return false;
            } else {
                if (grid[i][j] != 0) return false;
            }
        }
    }
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool CheckXMatrix(int[][] grid) {
        int n = grid.Length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                bool onDiagonal = (i == j) || (i == n - 1 - j);
                if (onDiagonal) {
                    if (grid[i][j] == 0) return false;
                } else {
                    if (grid[i][j] != 0) return false;
                }
            }
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {boolean}
 */
var checkXMatrix = function(grid) {
    const n = grid.length;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (i === j || i === n - 1 - j) {
                if (grid[i][j] === 0) return false;
            } else {
                if (grid[i][j] !== 0) return false;
            }
        }
    }
    return true;
};
```

## Typescript

```typescript
function checkXMatrix(grid: number[][]): boolean {
    const n = grid.length;
    for (let i = 0; i < n; i++) {
        if (grid[i].length !== n) return false; // safety, though constraints guarantee square
        for (let j = 0; j < n; j++) {
            const onDiagonal = i === j || i === n - 1 - j;
            if (onDiagonal) {
                if (grid[i][j] === 0) return false;
            } else {
                if (grid[i][j] !== 0) return false;
            }
        }
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Boolean
     */
    function checkXMatrix($grid) {
        $n = count($grid);
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($i == $j || $i == $n - 1 - $j) {
                    if ($grid[$i][$j] == 0) {
                        return false;
                    }
                } else {
                    if ($grid[$i][$j] != 0) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func checkXMatrix(_ grid: [[Int]]) -> Bool {
        let n = grid.count
        for i in 0..<n {
            for j in 0..<n {
                if i == j || i == n - 1 - j {
                    if grid[i][j] == 0 { return false }
                } else {
                    if grid[i][j] != 0 { return false }
                }
            }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun checkXMatrix(grid: Array<IntArray>): Boolean {
        val n = grid.size
        for (i in 0 until n) {
            for (j in 0 until n) {
                val onDiagonal = i == j || i + j == n - 1
                if (onDiagonal) {
                    if (grid[i][j] == 0) return false
                } else {
                    if (grid[i][j] != 0) return false
                }
            }
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool checkXMatrix(List<List<int>> grid) {
    int n = grid.length;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if (i == j || i == n - 1 - j) {
          if (grid[i][j] == 0) return false;
        } else {
          if (grid[i][j] != 0) return false;
        }
      }
    }
    return true;
  }
}
```

## Golang

```go
func checkXMatrix(grid [][]int) bool {
	n := len(grid)
	for i := 0; i < n; i++ {
		if len(grid[i]) != n {
			return false
		}
		for j := 0; j < n; j++ {
			val := grid[i][j]
			if i == j || i == n-1-j {
				if val == 0 {
					return false
				}
			} else {
				if val != 0 {
					return false
				}
			}
		}
	}
	return true
}
```

## Ruby

```ruby
def check_x_matrix(grid)
  n = grid.length
  (0...n).each do |i|
    (0...n).each do |j|
      if i == j || i == n - 1 - j
        return false if grid[i][j] == 0
      else
        return false if grid[i][j] != 0
      end
    end
  end
  true
end
```

## Scala

```scala
object Solution {
    def checkXMatrix(grid: Array[Array[Int]]): Boolean = {
        val n = grid.length
        for (i <- 0 until n) {
            for (j <- 0 until n) {
                if (i == j || i + j == n - 1) {
                    if (grid(i)(j) == 0) return false
                } else {
                    if (grid(i)(j) != 0) return false
                }
            }
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn check_x_matrix(grid: Vec<Vec<i32>>) -> bool {
        let n = grid.len();
        for i in 0..n {
            for j in 0..n {
                let val = grid[i][j];
                if i == j || i + j == n - 1 {
                    if val == 0 {
                        return false;
                    }
                } else {
                    if val != 0 {
                        return false;
                    }
                }
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (check-x-matrix grid)
  (-> (listof (listof exact-integer?)) boolean?)
  (let ((n (length grid)))
    (for/and ([i (in-range n)])
      (for/and ([j (in-range n)])
        (let* ((row (list-ref grid i))
               (val (list-ref row j))
               (diag? (or (= i j) (= i (- n 1 j)))))
          (if diag?
              (not (= val 0))
              (= val 0)))))))
```

## Erlang

```erlang
-spec check_x_matrix(Grid :: [[integer()]]) -> boolean().
check_x_matrix(Grid) ->
    N = length(Grid),
    check_rows(Grid, 0, N).

check_rows([], _I, _N) -> true;
check_rows([Row|Rest], I, N) ->
    case check_row(Row, I, N, 0) of
        true -> check_rows(Rest, I + 1, N);
        false -> false
    end.

check_row([], _I, _N, _J) -> true;
check_row([Val|Vals], I, N, J) ->
    Diag = (I =:= J) orelse (I =:= N - 1 - J),
    case (Diag andalso Val =/= 0) orelse ((not Diag) andalso Val =:= 0) of
        true -> check_row(Vals, I, N, J + 1);
        false -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec check_x_matrix(grid :: [[integer]]) :: boolean
  def check_x_matrix(grid) do
    n = length(grid)

    Enum.with_index(grid)
    |> Enum.any?(fn {row, i} ->
      Enum.with_index(row)
      |> Enum.any?(fn {val, j} ->
        if i == j or i == n - 1 - j do
          val == 0
        else
          val != 0
        end
      end)
    end)
    |> Kernel.not()
  end
end
```
