# 1222. Queens That Can Attack the King

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> queensAttacktheKing(vector<vector<int>>& queens, vector<int>& king) {
        unordered_set<int> queenSet;
        for (const auto& q : queens) {
            queenSet.insert(q[0] * 8 + q[1]);
        }
        vector<vector<int>> ans;
        const int dirs[8][2] = {{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};
        for (auto& d : dirs) {
            int x = king[0] + d[0];
            int y = king[1] + d[1];
            while (x >= 0 && x < 8 && y >= 0 && y < 8) {
                if (queenSet.count(x * 8 + y)) {
                    ans.push_back({x, y});
                    break;
                }
                x += d[0];
                y += d[1];
            }
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<List<Integer>> queensAttacktheKing(int[][] queens, int[] king) {
        Set<Integer> queenSet = new HashSet<>();
        for (int[] q : queens) {
            queenSet.add(q[0] * 8 + q[1]);
        }
        int[] dx = {-1, -1, -1, 0, 0, 1, 1, 1};
        int[] dy = {-1, 0, 1, -1, 1, -1, 0, 1};
        List<List<Integer>> result = new ArrayList<>();
        for (int dir = 0; dir < 8; dir++) {
            int x = king[0] + dx[dir];
            int y = king[1] + dy[dir];
            while (x >= 0 && x < 8 && y >= 0 && y < 8) {
                if (queenSet.contains(x * 8 + y)) {
                    List<Integer> pos = new ArrayList<>(2);
                    pos.add(x);
                    pos.add(y);
                    result.add(pos);
                    break;
                }
                x += dx[dir];
                y += dy[dir];
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        queen_set = { (q[0], q[1]) for q in queens }
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0), (1, 1)]
        res = []
        kx, ky = king
        for dx, dy in directions:
            x, y = kx + dx, ky + dy
            while 0 <= x < 8 and 0 <= y < 8:
                if (x, y) in queen_set:
                    res.append([x, y])
                    break
                x += dx
                y += dy
        return res
```

## Python3

```python
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queen_set = { (q[0], q[1]) for q in queens }
        dirs = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1),          (0, 1),
                (1, -1),  (1, 0), (1, 1)]
        res = []
        xk, yk = king
        for dx, dy in dirs:
            x, y = xk + dx, yk + dy
            while 0 <= x < 8 and 0 <= y < 8:
                if (x, y) in queen_set:
                    res.append([x, y])
                    break
                x += dx
                y += dy
        return res
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** queensAttacktheKing(int** queens, int queensSize, int* queensColSize,
                         int* king, int kingSize, int* returnSize, int*** returnColumnSizes) {
    bool board[8][8] = {false};
    for (int i = 0; i < queensSize; ++i) {
        int x = queens[i][0];
        int y = queens[i][1];
        board[x][y] = true;
    }

    int dirs[8][2] = {{-1,0},{1,0},{0,-1},{0,1},{-1,-1},{-1,1},{1,-1},{1,1}};
    int** ans = (int**)malloc(8 * sizeof(int*));
    int* colSizes = (int*)malloc(8 * sizeof(int));
    int cnt = 0;

    int kx = king[0];
    int ky = king[1];

    for (int d = 0; d < 8; ++d) {
        int dx = dirs[d][0], dy = dirs[d][1];
        int x = kx + dx, y = ky + dy;
        while (x >= 0 && x < 8 && y >= 0 && y < 8) {
            if (board[x][y]) {
                ans[cnt] = (int*)malloc(2 * sizeof(int));
                ans[cnt][0] = x;
                ans[cnt][1] = y;
                colSizes[cnt] = 2;
                ++cnt;
                break;
            }
            x += dx;
            y += dy;
        }
    }

    *returnSize = cnt;
    *returnColumnSizes = &colSizes;
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public IList<IList<int>> QueensAttacktheKing(int[][] queens, int[] king) {
        var queenSet = new HashSet<(int, int)>();
        foreach (var q in queens) {
            queenSet.Add((q[0], q[1]));
        }

        int[,] dirs = new int[,] { {-1,-1}, {-1,0}, {-1,1}, {0,-1}, {0,1}, {1,-1}, {1,0}, {1,1} };
        var result = new List<IList<int>>();

        for (int i = 0; i < 8; i++) {
            int dx = dirs[i, 0];
            int dy = dirs[i, 1];
            int x = king[0] + dx;
            int y = king[1] + dy;

            while (x >= 0 && x < 8 && y >= 0 && y < 8) {
                if (queenSet.Contains((x, y))) {
                    result.Add(new List<int> { x, y });
                    break;
                }
                x += dx;
                y += dy;
            }
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} queens
 * @param {number[]} king
 * @return {number[][]}
 */
var queensAttacktheKing = function(queens, king) {
    const queenSet = new Set();
    for (const [x, y] of queens) {
        queenSet.add(`${x},${y}`);
    }
    
    const directions = [
        [-1, 0], [1, 0], [0, -1], [0, 1],
        [-1, -1], [-1, 1], [1, -1], [1, 1]
    ];
    
    const result = [];
    for (const [dx, dy] of directions) {
        let x = king[0] + dx;
        let y = king[1] + dy;
        while (x >= 0 && x < 8 && y >= 0 && y < 8) {
            if (queenSet.has(`${x},${y}`)) {
                result.push([x, y]);
                break;
            }
            x += dx;
            y += dy;
        }
    }
    
    return result;
};
```

## Typescript

```typescript
function queensAttacktheKing(queens: number[][], king: number[]): number[][] {
    const queenSet = new Set<string>();
    for (const [x, y] of queens) {
        queenSet.add(`${x},${y}`);
    }

    const directions = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1],          [0, 1],
        [1, -1],  [1, 0], [1, 1]
    ];

    const result: number[][] = [];

    for (const [dx, dy] of directions) {
        let x = king[0] + dx;
        let y = king[1] + dy;
        while (x >= 0 && x < 8 && y >= 0 && y < 8) {
            if (queenSet.has(`${x},${y}`)) {
                result.push([x, y]);
                break;
            }
            x += dx;
            y += dy;
        }
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $queens
     * @param Integer[] $king
     * @return Integer[][]
     */
    function queensAttacktheKing($queens, $king) {
        $queenSet = [];
        foreach ($queens as $q) {
            $queenSet[$q[0] . ',' . $q[1]] = true;
        }

        $directions = [
            [-1, 0], [1, 0], [0, -1], [0, 1],
            [-1, -1], [-1, 1], [1, -1], [1, 1]
        ];

        $result = [];

        foreach ($directions as $dir) {
            $x = $king[0] + $dir[0];
            $y = $king[1] + $dir[1];

            while ($x >= 0 && $x < 8 && $y >= 0 && $y < 8) {
                $key = $x . ',' . $y;
                if (isset($queenSet[$key])) {
                    $result[] = [$x, $y];
                    break;
                }
                $x += $dir[0];
                $y += $dir[1];
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func queensAttacktheKing(_ queens: [[Int]], _ king: [Int]) -> [[Int]] {
        var queenSet = Set<Int>()
        for q in queens {
            queenSet.insert(q[0] * 8 + q[1])
        }
        let directions = [(-1, -1), (-1, 0), (-1, 1),
                          (0, -1),          (0, 1),
                          (1, -1),  (1, 0), (1, 1)]
        var result = [[Int]]()
        for dir in directions {
            var x = king[0] + dir.0
            var y = king[1] + dir.1
            while x >= 0 && x < 8 && y >= 0 && y < 8 {
                if queenSet.contains(x * 8 + y) {
                    result.append([x, y])
                    break
                }
                x += dir.0
                y += dir.1
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun queensAttacktheKing(queens: Array<IntArray>, king: IntArray): List<List<Int>> {
        val queenSet = HashSet<Int>()
        for (q in queens) {
            queenSet.add(q[0] * 8 + q[1])
        }
        val result = mutableListOf<List<Int>>()
        val directions = arrayOf(
            intArrayOf(-1, -1), intArrayOf(-1, 0), intArrayOf(-1, 1),
            intArrayOf(0, -1),                 intArrayOf(0, 1),
            intArrayOf(1, -1), intArrayOf(1, 0), intArrayOf(1, 1)
        )
        for (dir in directions) {
            var x = king[0] + dir[0]
            var y = king[1] + dir[1]
            while (x in 0..7 && y in 0..7) {
                if (queenSet.contains(x * 8 + y)) {
                    result.add(listOf(x, y))
                    break
                }
                x += dir[0]
                y += dir[1]
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> queensAttacktheKing(List<List<int>> queens, List<int> king) {
    final Set<String> queenSet = {};
    for (var q in queens) {
      queenSet.add('${q[0]},${q[1]}');
    }

    final List<List<int>> result = [];
    const directions = [
      [-1, -1],
      [-1, 0],
      [-1, 1],
      [0, -1],
      [0, 1],
      [1, -1],
      [1, 0],
      [1, 1]
    ];

    for (var dir in directions) {
      int x = king[0] + dir[0];
      int y = king[1] + dir[1];
      while (x >= 0 && x < 8 && y >= 0 && y < 8) {
        if (queenSet.contains('$x,$y')) {
          result.add([x, y]);
          break;
        }
        x += dir[0];
        y += dir[1];
      }
    }

    return result;
  }
}
```

## Golang

```go
func queensAttacktheKing(queens [][]int, king []int) [][]int {
    // Create a set for quick lookup of queen positions
    queenSet := make(map[int]bool)
    for _, q := range queens {
        key := q[0]*8 + q[1]
        queenSet[key] = true
    }

    dirs := [8][2]int{
        {-1, -1}, {-1, 0}, {-1, 1},
        {0, -1},          {0, 1},
        {1, -1}, {1, 0}, {1, 1},
    }

    var result [][]int
    kx, ky := king[0], king[1]

    for _, d := range dirs {
        x, y := kx+d[0], ky+d[1]
        for x >= 0 && x < 8 && y >= 0 && y < 8 {
            if queenSet[x*8+y] {
                result = append(result, []int{x, y})
                break
            }
            x += d[0]
            y += d[1]
        }
    }

    return result
}
```

## Ruby

```ruby
require 'set'

def queens_attackthe_king(queens, king)
  queen_set = Set.new
  queens.each { |q| queen_set.add([q[0], q[1]]) }

  directions = [[-1, 0], [1, 0], [0, -1], [0, 1],
                [-1, -1], [-1, 1], [1, -1], [1, 1]]

  result = []

  directions.each do |dx, dy|
    x, y = king
    loop do
      x += dx
      y += dy
      break unless x.between?(0, 7) && y.between?(0, 7)
      if queen_set.include?([x, y])
        result << [x, y]
        break
      end
    end
  end

  result
end
```

## Scala

```scala
object Solution {
    def queensAttacktheKing(queens: Array[Array[Int]], king: Array[Int]): List[List[Int]] = {
        val queenSet = queens.map(q => (q(0), q(1))).toSet
        val dirs = Array((-1, -1), (-1, 0), (-1, 1),
                         (0, -1),          (0, 1),
                         (1, -1), (1, 0), (1, 1))
        var result = List.empty[List[Int]]
        for ((dx, dy) <- dirs) {
            var x = king(0) + dx
            var y = king(1) + dy
            var found = false
            while (x >= 0 && x < 8 && y >= 0 && y < 8 && !found) {
                if (queenSet.contains((x, y))) {
                    result = List(x, y) :: result
                    found = true
                } else {
                    x += dx
                    y += dy
                }
            }
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn queens_attackthe_king(queens: Vec<Vec<i32>>, king: Vec<i32>) -> Vec<Vec<i32>> {
        use std::collections::HashSet;
        let mut set = HashSet::new();
        for q in queens.iter() {
            set.insert((q[0], q[1]));
        }
        let dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)];
        let mut res: Vec<Vec<i32>> = Vec::new();
        let (kx, ky) = (king[0], king[1]);
        for &(dx, dy) in dirs.iter() {
            let mut x = kx + dx;
            let mut y = ky + dy;
            while x >= 0 && x < 8 && y >= 0 && y < 8 {
                if set.contains(&(x, y)) {
                    res.push(vec![x, y]);
                    break;
                }
                x += dx;
                y += dy;
            }
        }
        res
    }
}
```

## Racket

```racket
#lang racket

(define/contract (queens-attackthe-king queens king)
  (-> (listof (listof exact-integer?))
      (listof exact-integer?)
      (listof (listof exact-integer?)))
  (let* ((queen-set (make-hash))
         (kx (first king))
         (ky (second king))
         (dirs '((-1 -1) (-1 0) (-1 1)
                 (0 -1)  (0 1)
                 (1 -1)  (1 0)  (1 1)))
         (result '()))
    ;; store queen positions for O(1) lookup
    (for-each (lambda (pos)
                (hash-set! queen-set (+ (* (first pos) 8) (second pos)) #t))
              queens)
    ;; search each direction from the king
    (for ([d dirs])
      (let loop ((x (+ kx (first d))) (y (+ ky (second d))))
        (cond [(or (< x 0) (> x 7) (< y 0) (> y 7)) (void)]
              [(hash-has-key? queen-set (+ (* x 8) y))
               (set! result (cons (list x y) result))]
              [else (loop (+ x (first d)) (+ y (second d)))])))
    (reverse result)))
```

## Erlang

```erlang
-module(solution).
-export([queens_attackthe_king/2]).

-spec queens_attackthe_king(Queens :: [[integer()]], King :: [integer()]) -> [[integer()]].
queens_attackthe_king(Queens, King) ->
    Set = sets:from_list([list_to_tuple(Q) || Q <- Queens]),
    [Kx, Ky] = King,
    Directions = [{-1,0},{1,0},{0,-1},{0,1},{-1,-1},{-1,1},{1,-1},{1,1}],
    ResTuples = lists:foldl(
        fun({DX,DY}, Acc) ->
            case find_step(Kx+DX, Ky+DY, DX, DY, Set) of
                [] -> Acc;
                [{X,Y}] -> [{X,Y}|Acc]
            end
        end,
        [],
        Directions),
    [tuple_to_list(T) || T <- lists:reverse(ResTuples)].

find_step(X, Y, DX, DY, Set) when X >= 0, X < 8, Y >= 0, Y < 8 ->
    case sets:is_element({X,Y}, Set) of
        true -> [{X,Y}];
        false -> find_step(X+DX, Y+DY, DX, DY, Set)
    end;
find_step(_, _, _, _, _) -> [].
```

## Elixir

```elixir
defmodule Solution do
  @spec queens_attackthe_king(queens :: [[integer]], king :: [integer]) :: [[integer]]
  def queens_attackthe_king(queens, king) do
    qset = MapSet.new(Enum.map(queens, fn [x, y] -> {x, y} end))
    [kx, ky] = king

    directions = [
      {-1, -1}, {-1, 0}, {-1, 1},
      {0, -1},           {0, 1},
      {1, -1},  {1, 0},  {1, 1}
    ]

    Enum.reduce(directions, [], fn {dx, dy}, acc ->
      start = {kx + dx, ky + dy}

      queen =
        Stream.iterate(start, fn {cx, cy} -> {cx + dx, cy + dy} end)
        |> Enum.take_while(fn {cx, cy} -> cx in 0..7 and cy in 0..7 end)
        |> Enum.find(&MapSet.member?(qset, &1))

      case queen do
        nil -> acc
        {qx, qy} -> [[qx, qy] | acc]
      end
    end)
  end
end
```
