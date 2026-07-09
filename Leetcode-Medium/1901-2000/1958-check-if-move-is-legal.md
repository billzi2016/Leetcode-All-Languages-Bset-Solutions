# 1958. Check if Move is Legal

## Cpp

```cpp
class Solution {
public:
    bool checkMove(vector<vector<char>>& board, int rMove, int cMove, char color) {
        const int n = 8;
        char opp = (color == 'B' ? 'W' : 'B');
        vector<pair<int,int>> dirs = {{-1,0},{1,0},{0,-1},{0,1},
                                      {-1,-1},{-1,1},{1,-1},{1,1}};
        for (auto [dx, dy] : dirs) {
            int x = rMove + dx;
            int y = cMove + dy;
            int middle = 0;
            // collect consecutive opposite-colored cells
            while (x >= 0 && x < n && y >= 0 && y < n && board[x][y] == opp) {
                ++middle;
                x += dx;
                y += dy;
            }
            if (middle >= 1 && x >= 0 && x < n && y >= 0 && y < n && board[x][y] == color) {
                return true;
            }
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean checkMove(char[][] board, int rMove, int cMove, char color) {
        int n = 8;
        char opposite = (color == 'B') ? 'W' : 'B';
        int[] dr = {-1,-1,-1,0,0,1,1,1};
        int[] dc = {-1,0,1,-1,1,-1,0,1};
        for (int dir = 0; dir < 8; ++dir) {
            int r = rMove + dr[dir];
            int c = cMove + dc[dir];
            // first cell must be opposite color
            if (r < 0 || r >= n || c < 0 || c >= n) continue;
            if (board[r][c] != opposite) continue;
            // move through consecutive opposite cells
            while (true) {
                r += dr[dir];
                c += dc[dir];
                if (r < 0 || r >= n || c < 0 || c >= n) break;
                char cur = board[r][c];
                if (cur == opposite) continue;
                if (cur == color) return true; // found good line
                break; // hit empty cell or other invalid
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def checkMove(self, board, rMove, cMove, color):
        """
        :type board: List[List[str]]
        :type rMove: int
        :type cMove: int
        :type color: str
        :rtype: bool
        """
        other = 'W' if color == 'B' else 'B'
        dirs = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1),          (0, 1),
                (1, -1),  (1, 0), (1, 1)]
        n = 8
        for dr, dc in dirs:
            r, c = rMove + dr, cMove + dc
            # first cell must be opposite color
            if not (0 <= r < n and 0 <= c < n):
                continue
            if board[r][c] != other:
                continue
            # consume consecutive opposite-colored cells
            while True:
                r += dr
                c += dc
                if not (0 <= r < n and 0 <= c < n):
                    break
                if board[r][c] == other:
                    continue
                if board[r][c] == color:
                    return True
                # hit empty cell or wrong color
                break
        return False
```

## Python3

```python
class Solution:
    def checkMove(self, board, rMove, cMove, color):
        opp = 'W' if color == 'B' else 'B'
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1),
                (-1, -1), (-1, 1), (1, -1), (1, 1)]
        n = 8
        for dr, dc in dirs:
            r, c = rMove + dr, cMove + dc
            # first cell must be opposite color and not empty
            if 0 <= r < n and 0 <= c < n and board[r][c] == opp:
                while True:
                    r += dr
                    c += dc
                    if not (0 <= r < n and 0 <= c < n):
                        break
                    cell = board[r][c]
                    if cell == '.':
                        break
                    if cell == color:
                        return True
                    # else continue if still opposite
        return False
```

## C

```c
#include <stdbool.h>

bool checkMove(char** board, int boardSize, int* boardColSize, int rMove, int cMove, char color) {
    const int dirs[8][2] = {{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};
    for (int d = 0; d < 8; ++d) {
        int dr = dirs[d][0], dc = dirs[d][1];
        int step = 1;
        while (true) {
            int nr = rMove + dr * step;
            int nc = cMove + dc * step;
            if (nr < 0 || nr >= 8 || nc < 0 || nc >= 8) break;
            char cur = board[nr][nc];
            if (cur == '.') break;
            if (cur == color) {
                if (step >= 2) return true;   // found a good line
                else break;                    // adjacent same color, cannot extend further
            }
            // opposite color, continue searching
            ++step;
        }
    }
    return false;
}
```

## Csharp

```csharp
public class Solution {
    public bool CheckMove(char[][] board, int rMove, int cMove, char color) {
        char opp = color == 'B' ? 'W' : 'B';
        int[] dirs = { -1, 0, 1 };
        foreach (int dr in dirs)
            foreach (int dc in dirs)
                if (!(dr == 0 && dc == 0)) {
                    int r = rMove + dr;
                    int c = cMove + dc;
                    // first cell must be opposite color
                    if (r < 0 || r >= 8 || c < 0 || c >= 8) continue;
                    if (board[r][c] != opp) continue;
                    // continue moving in the same direction
                    while (true) {
                        r += dr;
                        c += dc;
                        if (r < 0 || r >= 8 || c < 0 || c >= 8) break;
                        char cur = board[r][c];
                        if (cur == color) return true;      // good line found
                        else if (cur == opp) continue;       // still middle part
                        else break;                           // free cell or invalid
                    }
                }
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {character[][]} board
 * @param {number} rMove
 * @param {number} cMove
 * @param {character} color
 * @return {boolean}
 */
var checkMove = function(board, rMove, cMove, color) {
    const opp = color === 'B' ? 'W' : 'B';
    const dirs = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1],          [0, 1],
        [1, -1],  [1, 0], [1, 1]
    ];
    for (const [dr, dc] of dirs) {
        let i = rMove + dr;
        let j = cMove + dc;
        let oppCount = 0;
        while (i >= 0 && i < 8 && j >= 0 && j < 8) {
            const cell = board[i][j];
            if (cell === opp) {
                oppCount++;
                i += dr;
                j += dc;
            } else {
                break;
            }
        }
        if (oppCount > 0 &&
            i >= 0 && i < 8 && j >= 0 && j < 8 &&
            board[i][j] === color) {
            return true;
        }
    }
    return false;
};
```

## Typescript

```typescript
function checkMove(board: string[][], rMove: number, cMove: number, color: string): boolean {
    const opp = color === 'B' ? 'W' : 'B';
    const dirs = [
        [1, 0], [-1, 0],
        [0, 1], [0, -1],
        [1, 1], [-1, -1],
        [1, -1], [-1, 1]
    ];
    const n = 8;
    for (const [dx, dy] of dirs) {
        let x = rMove + dx;
        let y = cMove + dy;
        // first cell must be opposite color
        if (x < 0 || x >= n || y < 0 || y >= n) continue;
        if (board[x][y] !== opp) continue;
        // move through consecutive opposite cells
        while (true) {
            x += dx;
            y += dy;
            if (x < 0 || x >= n || y < 0 || y >= n) break;
            const cell = board[x][y];
            if (cell === opp) continue;
            if (cell === color) return true; // good line found
            break; // hit '.' or other invalid cell
        }
    }
    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param String[][] $board
     * @param Integer $rMove
     * @param Integer $cMove
     * @param String $color
     * @return Boolean
     */
    function checkMove($board, $rMove, $cMove, $color) {
        $opp = ($color === 'B') ? 'W' : 'B';
        $dirs = [
            [-1, -1], [-1, 0], [-1, 1],
            [0, -1],          [0, 1],
            [1, -1],  [1, 0], [1, 1]
        ];
        foreach ($dirs as $d) {
            $dx = $d[0];
            $dy = $d[1];
            $x = $rMove + $dx;
            $y = $cMove + $dy;
            // first cell must be opposite color
            if ($x < 0 || $x >= 8 || $y < 0 || $y >= 8) continue;
            if ($board[$x][$y] !== $opp) continue;
            // move through consecutive opposite colors
            while (true) {
                $nx = $x + $dx;
                $ny = $y + $dy;
                if ($nx < 0 || $nx >= 8 || $ny < 0 || $ny >= 8) break;
                if ($board[$nx][$ny] !== $opp) break;
                $x = $nx;
                $y = $ny;
            }
            // next cell after the run of opposite colors
            $nx = $x + $dx;
            $ny = $y + $dy;
            if ($nx >= 0 && $nx < 8 && $ny >= 0 && $ny < 8 && $board[$nx][$ny] === $color) {
                return true;
            }
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func checkMove(_ board: [[Character]], _ rMove: Int, _ cMove: Int, _ color: Character) -> Bool {
        let other: Character = (color == "B") ? "W" : "B"
        let n = 8
        let directions = [(-1, -1), (-1, 0), (-1, 1),
                          (0, -1),          (0, 1),
                          (1, -1),  (1, 0), (1, 1)]
        
        for (dx, dy) in directions {
            var x = rMove + dx
            var y = cMove + dy
            var oppositeCount = 0
            
            // Count consecutive opposite-colored cells
            while x >= 0 && x < n && y >= 0 && y < n && board[x][y] == other {
                oppositeCount += 1
                x += dx
                y += dy
            }
            
            // Need at least one opposite cell and then a same-colored endpoint
            if oppositeCount > 0,
               x >= 0 && x < n && y >= 0 && y < n && board[x][y] == color {
                return true
            }
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun checkMove(board: Array<CharArray>, rMove: Int, cMove: Int, color: Char): Boolean {
        val dirs = arrayOf(
            intArrayOf(-1, -1), intArrayOf(-1, 0), intArrayOf(-1, 1),
            intArrayOf(0, -1),                 intArrayOf(0, 1),
            intArrayOf(1, -1), intArrayOf(1, 0), intArrayOf(1, 1)
        )
        for (d in dirs) {
            var x = rMove + d[0]
            var y = cMove + d[1]
            var oppositeCount = 0
            while (x in 0..7 && y in 0..7) {
                val cell = board[x][y]
                if (cell == '.') break
                if (cell == color) {
                    if (oppositeCount >= 1) return true
                    else break
                } else {
                    oppositeCount++
                }
                x += d[0]
                y += d[1]
            }
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool checkMove(List<List<String>> board, int rMove, int cMove, String color) {
    const List<List<int>> dirs = [
      [-1, 0],
      [1, 0],
      [0, -1],
      [0, 1],
      [-1, -1],
      [-1, 1],
      [1, -1],
      [1, 1]
    ];
    String opp = (color == 'B') ? 'W' : 'B';
    for (var d in dirs) {
      int dr = d[0];
      int dc = d[1];
      int r = rMove + dr;
      int c = cMove + dc;
      if (!_inBounds(r, c) || board[r][c] != opp) continue;
      while (_inBounds(r, c) && board[r][c] == opp) {
        r += dr;
        c += dc;
      }
      if (_inBounds(r, c) && board[r][c] == color) return true;
    }
    return false;
  }

  bool _inBounds(int r, int c) => r >= 0 && r < 8 && c >= 0 && c < 8;
}
```

## Golang

```go
func checkMove(board [][]byte, rMove int, cMove int, color byte) bool {
	opp := byte('W')
	if color == 'W' {
		opp = 'B'
	}
	dirs := [][2]int{{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}}
	for _, d := range dirs {
		x, y := rMove+d[0], cMove+d[1]
		if x < 0 || x >= 8 || y < 0 || y >= 8 {
			continue
		}
		if board[x][y] != opp {
			continue
		}
		for {
			x += d[0]
			y += d[1]
			if x < 0 || x >= 8 || y < 0 || y >= 8 {
				break
			}
			cur := board[x][y]
			if cur == '.' {
				break
			}
			if cur == color {
				return true
			}
			// else continue scanning opposite-colored cells
		}
	}
	return false
}
```

## Ruby

```ruby
def check_move(board, r_move, c_move, color)
  opp = color == 'B' ? 'W' : 'B'
  dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
  dirs.each do |dx, dy|
    x = r_move + dx
    y = c_move + dy
    cnt = 0
    while x.between?(0, 7) && y.between?(0, 7) && board[x][y] == opp
      cnt += 1
      x += dx
      y += dy
    end
    if cnt >= 1 && x.between?(0, 7) && y.between?(0, 7) && board[x][y] == color
      return true
    end
  end
  false
end
```

## Scala

```scala
object Solution {
  def checkMove(board: Array[Array[Char]], rMove: Int, cMove: Int, color: Char): Boolean = {
    val dirs = Array(
      (-1, -1), (-1, 0), (-1, 1),
      (0, -1),          (0, 1),
      (1, -1),  (1, 0), (1, 1)
    )
    for ((dx, dy) <- dirs) {
      var i = 1
      var continue = true
      while (continue) {
        val x = rMove + i * dx
        val y = cMove + i * dy
        if (x < 0 || x >= 8 || y < 0 || y >= 8) {
          continue = false
        } else {
          board(x)(y) match {
            case '.' => continue = false
            case `color` =>
              if (i >= 2) return true
              else continue = false
            case _ => // opposite color
              i += 1
          }
        }
      }
    }
    false
  }
}
```

## Rust

```rust
impl Solution {
    pub fn check_move(board: Vec<Vec<char>>, r_move: i32, c_move: i32, color: char) -> bool {
        let opp = if color == 'B' { 'W' } else { 'B' };
        let dirs = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ];
        for &(dx, dy) in &dirs {
            let mut step = 1;
            loop {
                let nr = r_move + dx * step;
                let nc = c_move + dy * step;
                if nr < 0 || nr >= 8 || nc < 0 || nc >= 8 {
                    break;
                }
                let ch = board[nr as usize][nc as usize];
                if ch == '.' {
                    break;
                } else if ch == opp {
                    step += 1;
                    continue;
                } else if ch == color {
                    if step >= 2 {
                        return true;
                    } else {
                        break;
                    }
                } else {
                    break;
                }
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (check-move board rMove cMove color)
  (-> (listof (listof char?)) exact-integer? exact-integer? char? boolean?)
  (let* ((n 8)
         (opponent (if (char=? color #\B) #\W #\B))
         (dirs '((-1 -1) (-1 0) (-1 1) (0 -1) (0 1) (1 -1) (1 0) (1 1)))
         (inside?
          (lambda (r c)
            (and (>= r 0) (< r n) (>= c 0) (< c n))))
         (cell
          (lambda (r c)
            (list-ref (list-ref board r) c))))
    (define (check-dir dx dy)
      (let loop ((r (+ rMove dx)) (c (+ cMove dy)) (seen-opponent #f))
        (if (not (inside? r c))
            #f
            (let ((ch (cell r c)))
              (cond
                [(char=? ch #\.) #f]
                [(char=? ch opponent) (loop (+ r dx) (+ c dy) #t)]
                [(char=? ch color) seen-opponent]
                [else #f])))))
    (for/or ([d dirs])
      (apply check-dir d))))
```

## Erlang

```erlang
-module(solution).
-export([check_move/4]).

-spec check_move(Board :: [[char()]], RMove :: integer(), CMove :: integer(), Color :: char()) -> boolean().
check_move(Board, RMove, CMove, Color) ->
    Opp = opposite(Color),
    Directions = [{1,0}, {-1,0}, {0,1}, {0,-1},
                  {1,1}, {1,-1}, {-1,1}, {-1,-1}],
    lists:any(fun({DX,DY}) -> check_dir(Board, RMove, CMove, Color, Opp, DX, DY) end,
              Directions).

%% Check a single direction starting from (R,C)
-spec check_dir([[char()]], integer(), integer(), char(), char(), integer(), integer()) -> boolean().
check_dir(Board, R, C, Color, Opp, DX, DY) ->
    R1 = R + DX,
    C1 = C + DY,
    case in_bounds(R1, C1) of
        false -> false;
        true ->
            case get_cell(Board, R1, C1) of
                Opp -> explore_opps(Board, R1, C1, Color, Opp, DX, DY);
                _   -> false
            end
    end.

%% Continue moving over opposite-colored cells until a same-colored endpoint is found
-spec explore_opps([[char()]], integer(), integer(), char(), char(), integer(), integer()) -> boolean().
explore_opps(Board, R, C, Color, Opp, DX, DY) ->
    Rn = R + DX,
    Cn = C + DY,
    case in_bounds(Rn, Cn) of
        false -> false;
        true ->
            case get_cell(Board, Rn, Cn) of
                Opp   -> explore_opps(Board, Rn, Cn, Color, Opp, DX, DY);
                Color -> true;          % good line found
                _     -> false
            end
    end.

%% Retrieve cell content; assumes indices are valid
-spec get_cell([[char()]], integer(), integer()) -> char().
get_cell(Board, R, C) ->
    Row = lists:nth(R + 1, Board),
    lists:nth(C + 1, Row).

%% Check board boundaries (0..7)
-spec in_bounds(integer(), integer()) -> boolean().
in_bounds(R, C) ->
    R >= 0 andalso R < 8 andalso C >= 0 andalso C < 8.

%% Opposite color helper
-spec opposite(char()) -> char().
opposite($B) -> $W;
opposite($W) -> $B.
```

## Elixir

```elixir
defmodule Solution do
  @spec check_move(board :: [[char]], r_move :: integer, c_move :: integer, color :: char) :: boolean
  def check_move(board, r_move, c_move, color) do
    opposite = if color == "B", do: "W", else: "B"

    directions =
      for dr <- -1..1,
          dc <- -1..1,
          dr != 0 or dc != 0,
          do: {dr, dc}

    Enum.any?(directions, fn {dr, dc} ->
      check_dir(board, r_move, c_move, dr, dc, color, opposite)
    end)
  end

  defp get_cell(_board, r, _c) when r < 0 or r >= 8, do: nil
  defp get_cell(_board, _r, c) when c < 0 or c >= 8, do: nil
  defp get_cell(board, r, c), do: board |> Enum.at(r) |> Enum.at(c)

  defp check_dir(board, r_move, c_move, dr, dc, color, opposite) do
    nr = r_move + dr
    nc = c_move + dc

    case get_cell(board, nr, nc) do
      ^opposite ->
        {r_end, c_end} = advance_opposite(board, nr + dr, nc + dc, dr, dc, opposite)

        case get_cell(board, r_end, c_end) do
          ^color -> true
          _ -> false
        end

      _ ->
        false
    end
  end

  defp advance_opposite(board, r, c, dr, dc, opposite) do
    case get_cell(board, r, c) do
      ^opposite -> advance_opposite(board, r + dr, c + dc, dr, dc, opposite)
      _ -> {r, c}
    end
  end
end
```
