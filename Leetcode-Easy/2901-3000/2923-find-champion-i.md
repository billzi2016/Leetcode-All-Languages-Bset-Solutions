# 2923. Find Champion I

## Cpp

```cpp
class Solution {
public:
    int findChampion(vector<vector<int>>& grid) {
        int n = grid.size();
        int champion = 0;
        for (int i = 1; i < n; ++i) {
            if (grid[champion][i] == 0) { // team i is stronger than current champion
                champion = i;
            }
        }
        return champion;
    }
};
```

## Java

```java
class Solution {
    public int findChampion(int[][] grid) {
        int n = grid.length;
        for (int i = 0; i < n; i++) {
            boolean champion = true;
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                if (grid[i][j] != 1) {
                    champion = false;
                    break;
                }
            }
            if (champion) return i;
        }
        // According to problem constraints, this line should never be reached.
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def findChampion(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        for i in range(n):
            # Champion must beat every other team
            if all(grid[i][j] == 1 for j in range(n) if i != j):
                return i
        # According to problem constraints, this line is never reached
        return -1
```

## Python3

```python
from typing import List

class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i in range(n):
            # champion must beat every other team
            if all(grid[i][j] == 1 for j in range(n) if i != j):
                return i
        return -1
```

## C

```c
int findChampion(int** grid, int gridSize, int* gridColSize){
    int champion = 0;
    for (int i = 1; i < gridSize; ++i) {
        if (grid[champion][i] == 0) {
            champion = i;
        }
    }
    return champion;
}
```

## Csharp

```csharp
public class Solution {
    public int FindChampion(int[][] grid) {
        int n = grid.Length;
        for (int i = 0; i < n; i++) {
            bool isChampion = true;
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                if (grid[i][j] == 0) { // i is not stronger than j
                    isChampion = false;
                    break;
                }
            }
            if (isChampion) return i;
        }
        return -1; // Should never reach here as per problem guarantees
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var findChampion = function(grid) {
    const n = grid.length;
    let champion = 0;
    for (let i = 1; i < n; i++) {
        if (grid[champion][i] === 0) {
            champion = i;
        }
    }
    return champion;
};
```

## Typescript

```typescript
function findChampion(grid: number[][]): number {
    const n = grid.length;
    for (let i = 0; i < n; i++) {
        let isChampion = true;
        for (let j = 0; j < n; j++) {
            if (i === j) continue;
            if (grid[i][j] !== 1) {
                isChampion = false;
                break;
            }
        }
        if (isChampion) return i;
    }
    return -1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function findChampion($grid) {
        $n = count($grid);
        $candidate = 0;
        for ($i = 1; $i < $n; $i++) {
            if ($grid[$candidate][$i] == 0) {
                $candidate = $i;
            }
        }
        return $candidate;
    }
}
```

## Swift

```swift
class Solution {
    func findChampion(_ grid: [[Int]]) -> Int {
        let n = grid.count
        var champion = 0
        for i in 1..<n {
            if grid[champion][i] == 0 { // team i is stronger than current champion
                champion = i
            }
        }
        return champion
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findChampion(grid: Array<IntArray>): Int {
        val n = grid.size
        for (i in 0 until n) {
            var isChampion = true
            for (j in 0 until n) {
                if (i == j) continue
                // If team j is stronger than i, then grid[j][i] == 1
                if (grid[j][i] == 1) {
                    isChampion = false
                    break
                }
            }
            if (isChampion) return i
        }
        return -1 // Should never reach here given problem guarantees a champion
    }
}
```

## Dart

```dart
class Solution {
  int findChampion(List<List<int>> grid) {
    int n = grid.length;
    for (int i = 0; i < n; i++) {
      bool isChampion = true;
      for (int j = 0; j < n; j++) {
        if (i == j) continue;
        if (grid[i][j] != 1) {
          isChampion = false;
          break;
        }
      }
      if (isChampion) return i;
    }
    return -1;
  }
}
```

## Golang

```go
func findChampion(grid [][]int) int {
    n := len(grid)
    for i := 0; i < n; i++ {
        champion := true
        for j := 0; j < n; j++ {
            if i == j {
                continue
            }
            if grid[i][j] == 0 {
                champion = false
                break
            }
        }
        if champion {
            return i
        }
    }
    return -1
}
```

## Ruby

```ruby
def find_champion(grid)
  n = grid.length
  (0...n).each do |i|
    champion = true
    (0...n).each do |j|
      next if i == j
      unless grid[i][j] == 1
        champion = false
        break
      end
    end
    return i if champion
  end
end
```

## Scala

```scala
object Solution {
    def findChampion(grid: Array[Array[Int]]): Int = {
        var champion = 0
        val n = grid.length
        for (i <- 1 until n) {
            if (grid(champion)(i) == 0) {
                champion = i
            }
        }
        champion
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_champion(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        for i in 0..n {
            let mut win_cnt = 0;
            for j in 0..n {
                if i != j && grid[i][j] == 1 {
                    win_cnt += 1;
                }
            }
            if win_cnt == n - 1 {
                return i as i32;
            }
        }
        -1
    }
}
```

## Racket

```racket
(define/contract (find-champion grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length grid))
         (champ (for/first ([i (in-range n)]
                            #:when (for/and ([j (in-range n)] #:unless (= i j))
                                     (= (list-ref (list-ref grid i) j) 1)))
                  i)))
    (if (void? champ) -1 champ)))
```

## Erlang

```erlang
-module(find_champion).
-export([find_champion/1]).

-spec find_champion(Grid :: [[integer()]]) -> integer().
find_champion(Grid) ->
    find_champion(Grid, 0).

find_champion([], _Idx) ->
    -1; % should never happen with valid input
find_champion([Row|Rest], Idx) ->
    case row_is_champion(Row, Idx) of
        true -> Idx;
        false -> find_champion(Rest, Idx + 1)
    end.

row_is_champion(Row, I) ->
    row_is_champion(Row, 0, I).

row_is_champion([], _J, _I) ->
    true;
row_is_champion([Val|Rest], J, I) ->
    case J =:= I of
        true -> 
            row_is_champion(Rest, J + 1, I);
        false ->
            if Val =:= 1 ->
                    row_is_champion(Rest, J + 1, I);
               true ->
                    false
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_champion(grid :: [[integer]]) :: integer
  def find_champion(grid) do
    n = length(grid)

    Enum.find(0..(n - 1), fn i ->
      row = Enum.at(grid, i)

      Enum.with_index(row)
      |> Enum.all?(fn {val, j} -> j == i or val == 1 end)
    end)
  end
end
```
