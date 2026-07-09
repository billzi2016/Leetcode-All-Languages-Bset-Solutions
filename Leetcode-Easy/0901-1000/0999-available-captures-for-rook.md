# 0999. Available Captures for Rook

## Cpp

```cpp
class Solution {
public:
    int numRookCaptures(vector<vector<char>>& board) {
        int rookRow = -1, rookCol = -1;
        for (int i = 0; i < 8; ++i) {
            for (int j = 0; j < 8; ++j) {
                if (board[i][j] == 'R') {
                    rookRow = i;
                    rookCol = j;
                    break;
                }
            }
            if (rookRow != -1) break;
        }
        int captures = 0;
        // up
        for (int i = rookRow - 1; i >= 0; --i) {
            if (board[i][rookCol] == 'B') break;
            if (board[i][rookCol] == 'p') { ++captures; break; }
        }
        // down
        for (int i = rookRow + 1; i < 8; ++i) {
            if (board[i][rookCol] == 'B') break;
            if (board[i][rookCol] == 'p') { ++captures; break; }
        }
        // left
        for (int j = rookCol - 1; j >= 0; --j) {
            if (board[rookRow][j] == 'B') break;
            if (board[rookRow][j] == 'p') { ++captures; break; }
        }
        // right
        for (int j = rookCol + 1; j < 8; ++j) {
            if (board[rookRow][j] == 'B') break;
            if (board[rookRow][j] == 'p') { ++captures; break; }
        }
        return captures;
    }
};
```

## Java

```java
class Solution {
    public int numRookCaptures(char[][] board) {
        int rookRow = -1, rookCol = -1;
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                if (board[i][j] == 'R') {
                    rookRow = i;
                    rookCol = j;
                    break;
                }
            }
            if (rookRow != -1) break;
        }

        int captures = 0;

        // Up
        for (int i = rookRow - 1; i >= 0; i--) {
            char cell = board[i][rookCol];
            if (cell == 'B') break;
            if (cell == 'p') { captures++; break; }
        }

        // Down
        for (int i = rookRow + 1; i < 8; i++) {
            char cell = board[i][rookCol];
            if (cell == 'B') break;
            if (cell == 'p') { captures++; break; }
        }

        // Left
        for (int j = rookCol - 1; j >= 0; j--) {
            char cell = board[rookRow][j];
            if (cell == 'B') break;
            if (cell == 'p') { captures++; break; }
        }

        // Right
        for (int j = rookCol + 1; j < 8; j++) {
            char cell = board[rookRow][j];
            if (cell == 'B') break;
            if (cell == 'p') { captures++; break; }
        }

        return captures;
    }
}
```

## Python

```python
class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        # Find rook position
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    r, c = i, j
                    break
            else:
                continue
            break

        captures = 0
        # Directions: up, down, left, right
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            while 0 <= nr < 8 and 0 <= nc < 8:
                cell = board[nr][nc]
                if cell == 'B':
                    break
                if cell == 'p':
                    captures += 1
                    break
                nr += dr
                nc += dc
        return captures
```

## Python3

```python
from typing import List

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # Locate the rook
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    r, c = i, j
                    break
            else:
                continue
            break

        captures = 0
        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            while 0 <= nr < 8 and 0 <= nc < 8:
                cell = board[nr][nc]
                if cell == 'B':
                    break
                if cell == 'p':
                    captures += 1
                    break
                nr += dr
                nc += dc

        return captures
```

## C

```c
int numRookCaptures(char** board, int boardSize, int* boardColSize) {
    int rookRow = -1, rookCol = -1;
    for (int i = 0; i < boardSize; ++i) {
        for (int j = 0; j < boardColSize[i]; ++j) {
            if (board[i][j] == 'R') {
                rookRow = i;
                rookCol = j;
                break;
            }
        }
        if (rookRow != -1) break;
    }

    int captures = 0;
    // Up
    for (int i = rookRow - 1; i >= 0; --i) {
        char c = board[i][rookCol];
        if (c == 'B') break;
        if (c == 'p') { ++captures; break; }
    }
    // Down
    for (int i = rookRow + 1; i < boardSize; ++i) {
        char c = board[i][rookCol];
        if (c == 'B') break;
        if (c == 'p') { ++captures; break; }
    }
    // Left
    for (int j = rookCol - 1; j >= 0; --j) {
        char c = board[rookRow][j];
        if (c == 'B') break;
        if (c == 'p') { ++captures; break; }
    }
    // Right
    for (int j = rookCol + 1; j < boardColSize[0]; ++j) {
        char c = board[rookRow][j];
        if (c == 'B') break;
        if (c == 'p') { ++captures; break; }
    }

    return captures;
}
```

## Csharp

```csharp
public class Solution
{
    public int NumRookCaptures(char[][] board)
    {
        int rookRow = -1, rookCol = -1;
        for (int i = 0; i < 8; i++)
        {
            for (int j = 0; j < 8; j++)
            {
                if (board[i][j] == 'R')
                {
                    rookRow = i;
                    rookCol = j;
                    break;
                }
            }
            if (rookRow != -1) break;
        }

        int captures = 0;

        // Up
        for (int i = rookRow - 1; i >= 0; i--)
        {
            char cell = board[i][rookCol];
            if (cell == 'B') break;
            if (cell == 'p')
            {
                captures++;
                break;
            }
        }

        // Down
        for (int i = rookRow + 1; i < 8; i++)
        {
            char cell = board[i][rookCol];
            if (cell == 'B') break;
            if (cell == 'p')
            {
                captures++;
                break;
            }
        }

        // Left
        for (int j = rookCol - 1; j >= 0; j--)
        {
            char cell = board[rookRow][j];
            if (cell == 'B') break;
            if (cell == 'p')
            {
                captures++;
                break;
            }
        }

        // Right
        for (int j = rookCol + 1; j < 8; j++)
        {
            char cell = board[rookRow][j];
            if (cell == 'B') break;
            if (cell == 'p')
            {
                captures++;
                break;
            }
        }

        return captures;
    }
}
```

## Javascript

```javascript
/**
 * @param {character[][]} board
 * @return {number}
 */
var numRookCaptures = function(board) {
    let rookRow = -1, rookCol = -1;
    for (let i = 0; i < 8; i++) {
        for (let j = 0; j < 8; j++) {
            if (board[i][j] === 'R') {
                rookRow = i;
                rookCol = j;
                break;
            }
        }
        if (rookRow !== -1) break;
    }

    let captures = 0;
    const dirs = [
        [-1, 0], // up
        [1, 0],  // down
        [0, -1], // left
        [0, 1]   // right
    ];

    for (const [dr, dc] of dirs) {
        let r = rookRow + dr;
        let c = rookCol + dc;
        while (r >= 0 && r < 8 && c >= 0 && c < 8) {
            const cell = board[r][c];
            if (cell === 'B') break;          // blocked by bishop
            if (cell === 'p') {               // capture pawn
                captures++;
                break;
            }
            // empty, continue moving
            r += dr;
            c += dc;
        }
    }

    return captures;
};
```

## Typescript

```typescript
function numRookCaptures(board: string[][]): number {
    let rookRow = -1, rookCol = -1;
    for (let i = 0; i < 8; i++) {
        for (let j = 0; j < 8; j++) {
            if (board[i][j] === 'R') {
                rookRow = i;
                rookCol = j;
                break;
            }
        }
        if (rookRow !== -1) break;
    }

    const dirs = [
        [-1, 0], // up
        [1, 0],  // down
        [0, -1], // left
        [0, 1]   // right
    ];

    let captures = 0;

    for (const [dr, dc] of dirs) {
        let r = rookRow + dr;
        let c = rookCol + dc;
        while (r >= 0 && r < 8 && c >= 0 && c < 8) {
            const cell = board[r][c];
            if (cell === 'B') break;          // blocked by bishop
            if (cell === 'p') {               // capture pawn
                captures++;
                break;
            }
            // empty, continue moving
            r += dr;
            c += dc;
        }
    }

    return captures;
}
```

## Php

```php
class Solution {

    /**
     * @param String[][] $board
     * @return Integer
     */
    function numRookCaptures($board) {
        $r = -1;
        $c = -1;
        for ($i = 0; $i < 8; $i++) {
            for ($j = 0; $j < 8; $j++) {
                if ($board[$i][$j] === 'R') {
                    $r = $i;
                    $c = $j;
                    break 2;
                }
            }
        }

        $captures = 0;

        // up
        for ($i = $r - 1; $i >= 0; $i--) {
            $cell = $board[$i][$c];
            if ($cell === 'B') {
                break;
            }
            if ($cell === 'p') {
                $captures++;
                break;
            }
        }

        // down
        for ($i = $r + 1; $i < 8; $i++) {
            $cell = $board[$i][$c];
            if ($cell === 'B') {
                break;
            }
            if ($cell === 'p') {
                $captures++;
                break;
            }
        }

        // left
        for ($j = $c - 1; $j >= 0; $j--) {
            $cell = $board[$r][$j];
            if ($cell === 'B') {
                break;
            }
            if ($cell === 'p') {
                $captures++;
                break;
            }
        }

        // right
        for ($j = $c + 1; $j < 8; $j++) {
            $cell = $board[$r][$j];
            if ($cell === 'B') {
                break;
            }
            if ($cell === 'p') {
                $captures++;
                break;
            }
        }

        return $captures;
    }
}
```

## Swift

```swift
class Solution {
    func numRookCaptures(_ board: [[Character]]) -> Int {
        var rookRow = -1
        var rookCol = -1
        for i in 0..<8 {
            for j in 0..<8 {
                if board[i][j] == "R" {
                    rookRow = i
                    rookCol = j
                    break
                }
            }
            if rookRow != -1 { break }
        }
        
        var captures = 0
        let directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for (dx, dy) in directions {
            var x = rookRow + dx
            var y = rookCol + dy
            while x >= 0 && x < 8 && y >= 0 && y < 8 {
                let cell = board[x][y]
                if cell == "B" { break }
                if cell == "p" {
                    captures += 1
                    break
                }
                x += dx
                y += dy
            }
        }
        
        return captures
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numRookCaptures(board: Array<CharArray>): Int {
        var rookRow = -1
        var rookCol = -1
        for (i in 0 until 8) {
            for (j in 0 until 8) {
                if (board[i][j] == 'R') {
                    rookRow = i
                    rookCol = j
                    break
                }
            }
            if (rookRow != -1) break
        }

        var captures = 0
        val dr = intArrayOf(-1, 1, 0, 0)
        val dc = intArrayOf(0, 0, -1, 1)

        for (k in 0..3) {
            var r = rookRow + dr[k]
            var c = rookCol + dc[k]
            while (r in 0..7 && c in 0..7) {
                when (board[r][c]) {
                    'B' -> break
                    'p' -> {
                        captures++
                        break
                    }
                    else -> {
                        r += dr[k]
                        c += dc[k]
                    }
                }
            }
        }

        return captures
    }
}
```

## Dart

```dart
class Solution {
  int numRookCaptures(List<List<String>> board) {
    int rookRow = -1, rookCol = -1;
    for (int i = 0; i < 8; i++) {
      for (int j = 0; j < 8; j++) {
        if (board[i][j] == 'R') {
          rookRow = i;
          rookCol = j;
          break;
        }
      }
      if (rookRow != -1) break;
    }

    int captures = 0;
    // Directions: up, down, left, right
    const List<List<int>> dirs = [
      [-1, 0],
      [1, 0],
      [0, -1],
      [0, 1]
    ];

    for (var d in dirs) {
      int x = rookRow + d[0];
      int y = rookCol + d[1];
      while (x >= 0 && x < 8 && y >= 0 && y < 8) {
        String cell = board[x][y];
        if (cell == 'B') break; // blocked by bishop
        if (cell == 'p') {
          captures++;
          break;
        }
        // empty, continue moving
        x += d[0];
        y += d[1];
      }
    }

    return captures;
  }
}
```

## Golang

```go
func numRookCaptures(board [][]byte) int {
    var rx, ry int
    found := false
    for i := 0; i < 8 && !found; i++ {
        for j := 0; j < 8; j++ {
            if board[i][j] == 'R' {
                rx, ry = i, j
                found = true
                break
            }
        }
    }

    dirs := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
    captures := 0

    for _, d := range dirs {
        x, y := rx+d[0], ry+d[1]
        for x >= 0 && x < 8 && y >= 0 && y < 8 {
            if board[x][y] == 'B' {
                break
            }
            if board[x][y] == 'p' {
                captures++
                break
            }
            x += d[0]
            y += d[1]
        }
    }

    return captures
}
```

## Ruby

```ruby
def num_rook_captures(board)
  r = c = nil
  board.each_with_index do |row, i|
    if (j = row.index('R'))
      r = i
      c = j
      break
    end
  end

  count = 0

  # up
  i = r - 1
  while i >= 0
    cell = board[i][c]
    if cell == 'p'
      count += 1
      break
    elsif cell == 'B'
      break
    else
      i -= 1
    end
  end

  # down
  i = r + 1
  while i < 8
    cell = board[i][c]
    if cell == 'p'
      count += 1
      break
    elsif cell == 'B'
      break
    else
      i += 1
    end
  end

  # left
  j = c - 1
  while j >= 0
    cell = board[r][j]
    if cell == 'p'
      count += 1
      break
    elsif cell == 'B'
      break
    else
      j -= 1
    end
  end

  # right
  j = c + 1
  while j < 8
    cell = board[r][j]
    if cell == 'p'
      count += 1
      break
    elsif cell == 'B'
      break
    else
      j += 1
    end
  end

  count
end
```

## Scala

```scala
object Solution {
  def numRookCaptures(board: Array[Array[Char]]): Int = {
    var rookRow = -1
    var rookCol = -1
    for (i <- 0 until 8; j <- 0 until 8) {
      if (board(i)(j) == 'R') {
        rookRow = i
        rookCol = j
      }
    }

    val dirs = Array((-1, 0), (1, 0), (0, -1), (0, 1))
    var captures = 0

    for ((dr, dc) <- dirs) {
      var r = rookRow + dr
      var c = rookCol + dc
      while (r >= 0 && r < 8 && c >= 0 && c < 8) {
        board(r)(c) match {
          case 'B' => // blocked
            r = -1 // exit loop
          case 'p' =>
            captures += 1
            r = -1 // exit loop
          case _ =>
            r += dr
            c += dc
        }
      }
    }

    captures
  }
}
```

## Rust

```rust
impl Solution {
    pub fn num_rook_captures(board: Vec<Vec<char>>) -> i32 {
        let mut rook_i = 0usize;
        let mut rook_j = 0usize;
        'found: for i in 0..8 {
            for j in 0..8 {
                if board[i][j] == 'R' {
                    rook_i = i;
                    rook_j = j;
                    break 'found;
                }
            }
        }

        let dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)];
        let mut captures = 0;

        for &(dx, dy) in &dirs {
            let mut x = rook_i as isize + dx;
            let mut y = rook_j as isize + dy;
            while x >= 0 && x < 8 && y >= 0 && y < 8 {
                match board[x as usize][y as usize] {
                    'B' => break,
                    'p' => {
                        captures += 1;
                        break;
                    }
                    _ => {}
                }
                x += dx;
                y += dy;
            }
        }

        captures as i32
    }
}
```

## Racket

```racket
(define/contract (num-rook-captures board)
  (-> (listof (listof char?)) exact-integer?)
  (let* ((rows (length board))
         (cols (if (> rows 0) (length (first board)) 0))
         (rook-pos
           (let loop ((i 0))
             (cond [(= i rows) (error "Rook not found")]
                   [else
                    (let inner ((j 0) (row (list-ref board i)))
                      (cond [(= j cols) (loop (+ i 1))]
                            [(char=? (list-ref row j) #\R) (cons i j)]
                            [else (inner (+ j 1) row)]))])))
         (ri (car rook-pos))
         (rj (cdr rook-pos)))
    (define (scan di dj)
      (let loop ((i (+ ri di)) (j (+ rj dj)) (cnt 0))
        (cond [(or (< i 0) (>= i rows) (< j 0) (>= j cols)) cnt]
              [else
               (let ((c (list-ref (list-ref board i) j)))
                 (cond [(char=? c #\p) (+ cnt 1)]
                       [(char=? c #\B) cnt]
                       [else (loop (+ i di) (+ j dj) cnt)]))])))
    (+ (scan -1 0)   ; up
       (scan 1 0)    ; down
       (scan 0 -1)   ; left
       (scan 0 1))))   ; right
```

## Erlang

```erlang
-module(solution).
-export([num_rook_captures/1]).

-spec num_rook_captures(Board :: [[char()]]) -> integer().
num_rook_captures(Board) ->
    {RRow, RCol} = find_rook(Board, 0),
    Directions = [{-1,0},{1,0},{0,-1},{0,1}],
    lists:foldl(fun({DR,DC}, Acc) ->
        Acc + count_dir(Board, RRow, RCol, DR, DC)
    end, 0, Directions).

find_rook([Row|Rest], I) ->
    case find_col(Row, 0) of
        undefined -> find_rook(Rest, I+1);
        Col -> {I, Col}
    end.

find_col([], _) -> undefined;
find_col([$R|_], J) -> J;
find_col([_|Tail], J) -> find_col(Tail, J+1).

count_dir(Board, Row, Col, DR, DC) ->
    NextR = Row + DR,
    NextC = Col + DC,
    case in_bounds(NextR, NextC) of
        false -> 0;
        true ->
            Char = get_cell(Board, NextR, NextC),
            case Char of
                $p -> 1;
                $B -> 0;
                _ -> count_dir(Board, NextR, NextC, DR, DC)
            end
    end.

in_bounds(R, C) when R >= 0, R < 8, C >= 0, C < 8 -> true;
in_bounds(_, _) -> false.

get_cell(Board, R, C) ->
    Row = lists:nth(R+1, Board),
    lists:nth(C+1, Row).
```

## Elixir

```elixir
defmodule Solution do
  @spec num_rook_captures(board :: [[char]]) :: integer
  def num_rook_captures(board) do
    {r, c} = find_rook(board)

    dirs = [{-1, 0}, {1, 0}, {0, -1}, {0, 1}]

    Enum.reduce(dirs, 0, fn {dr, dc}, acc ->
      acc + capture_in_dir(board, r + dr, c + dc, dr, dc)
    end)
  end

  defp find_rook(board) do
    Enum.with_index(board)
    |> Enum.reduce_while({-1, -1}, fn {row, i}, _acc ->
      case Enum.find_index(row, &(&1 == "R")) do
        nil -> {:cont, {-1, -1}}
        j -> {:halt, {i, j}}
      end
    end)
  end

  defp capture_in_dir(board, r, c, dr, dc) when r < 0 or r >= 8 or c < 0 or c >= 8,
    do: 0

  defp capture_in_dir(board, r, c, dr, dc) do
    case Enum.at(Enum.at(board, r), c) do
      "." -> capture_in_dir(board, r + dr, c + dc, dr, dc)
      "p" -> 1
      _ -> 0
    end
  end
end
```
