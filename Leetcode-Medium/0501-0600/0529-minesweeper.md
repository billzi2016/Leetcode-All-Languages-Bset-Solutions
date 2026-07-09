# 0529. Minesweeper

## Cpp

```cpp
class Solution {
public:
    vector<vector<char>> updateBoard(vector<vector<char>>& board, vector<int>& click) {
        int rows = board.size();
        int cols = board[0].size();
        int r = click[0], c = click[1];
        if (board[r][c] == 'M') {
            board[r][c] = 'X';
            return board;
        }
        dfs(board, r, c, rows, cols);
        return board;
    }
private:
    const int dirs[8][2] = {{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};
    
    void dfs(vector<vector<char>>& board, int r, int c, int rows, int cols) {
        if (r < 0 || r >= rows || c < 0 || c >= cols || board[r][c] != 'E')
            return;
        
        int mines = 0;
        for (auto &d : dirs) {
            int nr = r + d[0], nc = c + d[1];
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && board[nr][nc] == 'M')
                ++mines;
        }
        
        if (mines > 0) {
            board[r][c] = char('0' + mines);
        } else {
            board[r][c] = 'B';
            for (auto &d : dirs) {
                dfs(board, r + d[0], c + d[1], rows, cols);
            }
        }
    }
};
```

## Java

```java
class Solution {
    private static final int[] DIRS = {-1, -1, -1, 0, -1, 1, 0, -1, 0, 1, 1, -1, 1, 0, 1, 1};

    public char[][] updateBoard(char[][] board, int[] click) {
        int r = click[0], c = click[1];
        if (board[r][c] == 'M') {
            board[r][c] = 'X';
            return board;
        }
        dfs(board, r, c);
        return board;
    }

    private void dfs(char[][] board, int r, int c) {
        if (r < 0 || c < 0 || r >= board.length || c >= board[0].length) return;
        if (board[r][c] != 'E') return;

        int mines = 0;
        for (int i = 0; i < DIRS.length; i += 2) {
            int nr = r + DIRS[i];
            int nc = c + DIRS[i + 1];
            if (nr >= 0 && nr < board.length && nc >= 0 && nc < board[0].length
                    && board[nr][nc] == 'M') {
                mines++;
            }
        }

        if (mines > 0) {
            board[r][c] = (char) ('0' + mines);
        } else {
            board[r][c] = 'B';
            for (int i = 0; i < DIRS.length; i += 2) {
                dfs(board, r + DIRS[i], c + DIRS[i + 1]);
            }
        }
    }
}
```

## Python

```python
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        rows, cols = len(board), len(board[0])
        r, c = click
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board

        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0), (1, 1)]

        def count_mines(x, y):
            cnt = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == 'M':
                    cnt += 1
            return cnt

        stack = [(r, c)]
        while stack:
            x, y = stack.pop()
            if board[x][y] != 'E':
                continue
            mines = count_mines(x, y)
            if mines > 0:
                board[x][y] = str(mines)
            else:
                board[x][y] = 'B'
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == 'E':
                        stack.append((nx, ny))
        return board
```

## Python3

```python
class Solution:
    def updateBoard(self, board, click):
        from sys import setrecursionlimit
        setrecursionlimit(10000)
        rows, cols = len(board), len(board[0])
        dirs = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1),          (0, 1),
                (1, -1),  (1, 0), (1, 1)]

        def count_mines(r, c):
            cnt = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'M':
                    cnt += 1
            return cnt

        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != 'E':
                return
            mines = count_mines(r, c)
            if mines:
                board[r][c] = str(mines)
            else:
                board[r][c] = 'B'
                for dr, dc in dirs:
                    dfs(r + dr, c + dc)

        cr, cc = click
        if board[cr][cc] == 'M':
            board[cr][cc] = 'X'
        else:
            dfs(cr, cc)
        return board
```

## C

```c
#include <stdlib.h>
#include <string.h>

static const int dirs[8][2] = {
    {-1,-1},{-1,0},{-1,1},
    {0,-1},        {0,1},
    {1,-1},{1,0},{1,1}
};

static void dfs(int r, int c, char **board, int rows, int cols) {
    int cnt = 0;
    for (int i = 0; i < 8; ++i) {
        int nr = r + dirs[i][0];
        int nc = c + dirs[i][1];
        if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && board[nr][nc] == 'M')
            cnt++;
    }
    if (cnt > 0) {
        board[r][c] = (char)('0' + cnt);
    } else {
        board[r][c] = 'B';
        for (int i = 0; i < 8; ++i) {
            int nr = r + dirs[i][0];
            int nc = c + dirs[i][1];
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && board[nr][nc] == 'E')
                dfs(nr, nc, board, rows, cols);
        }
    }
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
char** updateBoard(char** board, int boardSize, int* boardColSize, int* click, int clickSize, int* returnSize, int*** returnColumnSizes) {
    int rows = boardSize;
    int cols = boardColSize[0];

    char **res = (char **)malloc(rows * sizeof(char *));
    for (int i = 0; i < rows; ++i) {
        res[i] = (char *)malloc(cols * sizeof(char));
        memcpy(res[i], board[i], cols * sizeof(char));
    }

    int r = click[0];
    int c = click[1];

    if (res[r][c] == 'M') {
        res[r][c] = 'X';
    } else if (res[r][c] == 'E') {
        dfs(r, c, res, rows, cols);
    }

    *returnSize = rows;
    *returnColumnSizes = (int **)malloc(sizeof(int *));
    **returnColumnSizes = (int *)malloc(rows * sizeof(int));
    for (int i = 0; i < rows; ++i) {
        (*(*returnColumnSizes))[i] = cols;
    }

    return res;
}
```

## Csharp

```csharp
public class Solution
{
    private static readonly int[] dr = { -1, -1, -1, 0, 0, 1, 1, 1 };
    private static readonly int[] dc = { -1, 0, 1, -1, 1, -1, 0, 1 };

    public char[][] UpdateBoard(char[][] board, int[] click)
    {
        int rows = board.Length;
        int cols = board[0].Length;
        int r = click[0];
        int c = click[1];

        if (board[r][c] == 'M')
        {
            board[r][c] = 'X';
            return board;
        }

        Reveal(board, r, c, rows, cols);
        return board;
    }

    private void Reveal(char[][] board, int r, int c, int rows, int cols)
    {
        if (r < 0 || r >= rows || c < 0 || c >= cols) return;
        if (board[r][c] != 'E') return;

        int mines = CountMines(board, r, c, rows, cols);
        if (mines > 0)
        {
            board[r][c] = (char)('0' + mines);
        }
        else
        {
            board[r][c] = 'B';
            for (int i = 0; i < 8; i++)
            {
                Reveal(board, r + dr[i], c + dc[i], rows, cols);
            }
        }
    }

    private int CountMines(char[][] board, int r, int c, int rows, int cols)
    {
        int count = 0;
        for (int i = 0; i < 8; i++)
        {
            int nr = r + dr[i];
            int nc = c + dc[i];
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && board[nr][nc] == 'M')
                count++;
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {character[][]} board
 * @param {number[]} click
 * @return {character[][]}
 */
var updateBoard = function(board, click) {
    const [sr, sc] = click;
    const rows = board.length, cols = board[0].length;
    const dirs = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]];
    const inBounds = (r,c) => r >= 0 && r < rows && c >= 0 && c < cols;
    
    if (board[sr][sc] === 'M') {
        board[sr][sc] = 'X';
        return board;
    }
    
    const stack = [[sr, sc]];
    while (stack.length) {
        const [r, c] = stack.pop();
        if (board[r][c] !== 'E') continue; // already processed
        
        let mines = 0;
        for (const [dr, dc] of dirs) {
            const nr = r + dr, nc = c + dc;
            if (inBounds(nr, nc) && board[nr][nc] === 'M') mines++;
        }
        
        if (mines > 0) {
            board[r][c] = String(mines);
        } else {
            board[r][c] = 'B';
            for (const [dr, dc] of dirs) {
                const nr = r + dr, nc = c + dc;
                if (inBounds(nr, nc) && board[nr][nc] === 'E') {
                    stack.push([nr, nc]);
                }
            }
        }
    }
    
    return board;
};
```

## Typescript

```typescript
function updateBoard(board: string[][], click: number[]): string[][] {
    const rows = board.length;
    const cols = board[0].length;
    const dirs: [number, number][] = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1],           [0, 1],
        [1, -1],  [1, 0],  [1, 1]
    ];

    const countMines = (r: number, c: number): number => {
        let cnt = 0;
        for (const [dr, dc] of dirs) {
            const nr = r + dr, nc = c + dc;
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && board[nr][nc] === 'M') {
                cnt++;
            }
        }
        return cnt;
    };

    const dfs = (r: number, c: number): void => {
        if (r < 0 || r >= rows || c < 0 || c >= cols) return;
        if (board[r][c] !== 'E') return;

        const mines = countMines(r, c);
        if (mines > 0) {
            board[r][c] = mines.toString();
        } else {
            board[r][c] = 'B';
            for (const [dr, dc] of dirs) {
                dfs(r + dr, c + dc);
            }
        }
    };

    const [clickR, clickC] = click;
    if (board[clickR][clickC] === 'M') {
        board[clickR][clickC] = 'X';
    } else {
        dfs(clickR, clickC);
    }

    return board;
}
```

## Php

```php
class Solution {

    /**
     * @param String[][] $board
     * @param Integer[] $click
     * @return String[][]
     */
    function updateBoard($board, $click) {
        $row = $click[0];
        $col = $click[1];
        $m = count($board);
        $n = count($board[0]);

        // If click on a mine, mark as X
        if ($board[$row][$col] === 'M') {
            $board[$row][$col] = 'X';
            return $board;
        }

        $dirs = [
            [-1, -1], [-1, 0], [-1, 1],
            [0, -1],           [0, 1],
            [1, -1],  [1, 0],  [1, 1]
        ];

        $queue = new SplQueue();
        $queue->enqueue([$row, $col]);

        while (!$queue->isEmpty()) {
            [$r, $c] = $queue->dequeue();

            // Process only unrevealed empty cells
            if ($board[$r][$c] !== 'E') {
                continue;
            }

            // Count adjacent mines
            $count = 0;
            foreach ($dirs as $d) {
                $nr = $r + $d[0];
                $nc = $c + $d[1];
                if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n && $board[$nr][$nc] === 'M') {
                    $count++;
                }
            }

            if ($count > 0) {
                // Reveal number
                $board[$r][$c] = strval($count);
            } else {
                // Reveal blank and expand to neighbors
                $board[$r][$c] = 'B';
                foreach ($dirs as $d) {
                    $nr = $r + $d[0];
                    $nc = $c + $d[1];
                    if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n && $board[$nr][$nc] === 'E') {
                        $queue->enqueue([$nr, $nc]);
                    }
                }
            }
        }

        return $board;
    }
}
```

## Swift

```swift
class Solution {
    func updateBoard(_ board: [[Character]], _ click: [Int]) -> [[Character]] {
        var b = board
        let rows = b.count
        let cols = b[0].count
        let r = click[0]
        let c = click[1]
        
        if b[r][c] == "M" {
            b[r][c] = "X"
            return b
        }
        
        var queue: [(Int, Int)] = [(r, c)]
        var idx = 0
        let dirs = [(-1,-1), (-1,0), (-1,1),
                    (0,-1),          (0,1),
                    (1,-1),  (1,0),  (1,1)]
        
        while idx < queue.count {
            let (cr, cc) = queue[idx]
            idx += 1
            
            var mineCount = 0
            for (dr, dc) in dirs {
                let nr = cr + dr
                let nc = cc + dc
                if nr >= 0 && nr < rows && nc >= 0 && nc < cols {
                    if b[nr][nc] == "M" {
                        mineCount += 1
                    }
                }
            }
            
            if mineCount > 0 {
                b[cr][cc] = Character(String(mineCount))
            } else {
                b[cr][cc] = "B"
                for (dr, dc) in dirs {
                    let nr = cr + dr
                    let nc = cc + dc
                    if nr >= 0 && nr < rows && nc >= 0 && nc < cols {
                        if b[nr][nc] == "E" {
                            queue.append((nr, nc))
                        }
                    }
                }
            }
        }
        
        return b
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun updateBoard(board: Array<CharArray>, click: IntArray): Array<CharArray> {
        val rows = board.size
        val cols = board[0].size
        val dr = intArrayOf(-1, -1, -1, 0, 0, 1, 1, 1)
        val dc = intArrayOf(-1, 0, 1, -1, 1, -1, 0, 1)

        fun inBounds(r: Int, c: Int) = r >= 0 && r < rows && c >= 0 && c < cols

        fun dfs(r: Int, c: Int) {
            if (!inBounds(r, c) || board[r][c] != 'E') return
            var mines = 0
            for (k in 0..7) {
                val nr = r + dr[k]
                val nc = c + dc[k]
                if (inBounds(nr, nc) && board[nr][nc] == 'M') mines++
            }
            if (mines > 0) {
                board[r][c] = ('0'.code + mines).toChar()
            } else {
                board[r][c] = 'B'
                for (k in 0..7) {
                    dfs(r + dr[k], c + dc[k])
                }
            }
        }

        val r = click[0]
        val c = click[1]

        if (board[r][c] == 'M') {
            board[r][c] = 'X'
        } else {
            dfs(r, c)
        }

        return board
    }
}
```

## Dart

```dart
class Solution {
  List<List<String>> updateBoard(List<List<String>> board, List<int> click) {
    int m = board.length;
    int n = board[0].length;
    int r = click[0];
    int c = click[1];

    if (board[r][c] == 'M') {
      board[r][c] = 'X';
      return board;
    }

    const List<List<int>> dirs = [
      [-1, -1],
      [-1, 0],
      [-1, 1],
      [0, -1],
      [0, 1],
      [1, -1],
      [1, 0],
      [1, 1]
    ];

    void dfs(int i, int j) {
      if (i < 0 || i >= m || j < 0 || j >= n) return;
      if (board[i][j] != 'E') return;

      int mines = 0;
      for (var d in dirs) {
        int ni = i + d[0];
        int nj = j + d[1];
        if (ni >= 0 && ni < m && nj >= 0 && nj < n && board[ni][nj] == 'M') {
          mines++;
        }
      }

      if (mines > 0) {
        board[i][j] = mines.toString();
      } else {
        board[i][j] = 'B';
        for (var d in dirs) {
          dfs(i + d[0], j + d[1]);
        }
      }
    }

    dfs(r, c);
    return board;
  }
}
```

## Golang

```go
func updateBoard(board [][]byte, click []int) [][]byte {
    r, c := click[0], click[1]
    if board[r][c] == 'M' {
        board[r][c] = 'X'
        return board
    }

    rows, cols := len(board), len(board[0])
    dirs := [8][2]int{{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}}

    var dfs func(int, int)
    dfs = func(r, c int) {
        // Count adjacent mines
        cnt := 0
        for _, d := range dirs {
            nr, nc := r+d[0], c+d[1]
            if nr >= 0 && nr < rows && nc >= 0 && nc < cols && board[nr][nc] == 'M' {
                cnt++
            }
        }

        if cnt > 0 {
            board[r][c] = byte('0' + cnt)
            return
        }

        // No adjacent mines
        board[r][c] = 'B'
        for _, d := range dirs {
            nr, nc := r+d[0], c+d[1]
            if nr >= 0 && nr < rows && nc >= 0 && nc < cols && board[nr][nc] == 'E' {
                dfs(nr, nc)
            }
        }
    }

    dfs(r, c)
    return board
}
```

## Ruby

```ruby
def update_board(board, click)
  rows = board.size
  cols = board[0].size
  r, c = click

  return board if board[r][c] == 'X'

  # Click on a mine
  if board[r][c] == 'M'
    board[r][c] = 'X'
    return board
  end

  dirs = [[-1, -1], [-1, 0], [-1, 1],
          [0, -1],           [0, 1],
          [1, -1],  [1, 0],  [1, 1]]

  stack = [[r, c]]
  while !stack.empty?
    cr, cc = stack.pop
    next unless board[cr][cc] == 'E'

    # Count adjacent mines
    mine_cnt = 0
    dirs.each do |dr, dc|
      nr = cr + dr
      nc = cc + dc
      if nr.between?(0, rows - 1) && nc.between?(0, cols - 1)
        mine_cnt += 1 if board[nr][nc] == 'M'
      end
    end

    if mine_cnt > 0
      board[cr][cc] = mine_cnt.to_s
    else
      board[cr][cc] = 'B'
      dirs.each do |dr, dc|
        nr = cr + dr
        nc = cc + dc
        if nr.between?(0, rows - 1) && nc.between?(0, cols - 1) && board[nr][nc] == 'E'
          stack << [nr, nc]
        end
      end
    end
  end

  board
end
```

## Scala

```scala
object Solution {
    def updateBoard(board: Array[Array[Char]], click: Array[Int]): Array[Array[Char]] = {
        val m = board.length
        val n = board(0).length
        val dirs = Array(
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1),  (1, 0), (1, 1)
        )
        var r = click(0)
        var c = click(1)

        if (board(r)(c) == 'M') {
            board(r)(c) = 'X'
            return board
        }

        val q = scala.collection.mutable.Queue[(Int, Int)]()
        q.enqueue((r, c))

        while (q.nonEmpty) {
            val (cr, cc) = q.dequeue()
            if (board(cr)(cc) != 'E') {
                // already processed
            } else {
                var cnt = 0
                for ((dr, dc) <- dirs) {
                    val nr = cr + dr
                    val nc = cc + dc
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n && board(nr)(nc) == 'M') {
                        cnt += 1
                    }
                }

                if (cnt > 0) {
                    board(cr)(cc) = (cnt + '0').toChar
                } else {
                    board(cr)(cc) = 'B'
                    for ((dr, dc) <- dirs) {
                        val nr = cr + dr
                        val nc = cc + dc
                        if (nr >= 0 && nr < m && nc >= 0 && nc < n && board(nr)(nc) == 'E') {
                            q.enqueue((nr, nc))
                        }
                    }
                }
            }
        }

        board
    }
}
```

## Rust

```rust
impl Solution {
    pub fn update_board(mut board: Vec<Vec<char>>, click: Vec<i32>) -> Vec<Vec<char>> {
        let rows = board.len();
        let cols = board[0].len();
        let (r, c) = (click[0] as usize, click[1] as usize);
        if board[r][c] == 'M' {
            board[r][c] = 'X';
            return board;
        }

        let dirs: [(i32, i32); 8] = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ];

        let mut stack: Vec<(usize, usize)> = vec![(r, c)];
        while let Some((x, y)) = stack.pop() {
            if board[x][y] != 'E' {
                continue;
            }
            // Count adjacent mines
            let mut cnt = 0;
            for &(dx, dy) in &dirs {
                let nx = x as i32 + dx;
                let ny = y as i32 + dy;
                if nx >= 0 && nx < rows as i32 && ny >= 0 && ny < cols as i32 {
                    if board[nx as usize][ny as usize] == 'M' {
                        cnt += 1;
                    }
                }
            }

            if cnt > 0 {
                board[x][y] = ((cnt as u8) + b'0') as char;
            } else {
                board[x][y] = 'B';
                for &(dx, dy) in &dirs {
                    let nx = x as i32 + dx;
                    let ny = y as i32 + dy;
                    if nx >= 0 && nx < rows as i32 && ny >= 0 && ny < cols as i32 {
                        let ux = nx as usize;
                        let uy = ny as usize;
                        if board[ux][uy] == 'E' {
                            stack.push((ux, uy));
                        }
                    }
                }
            }
        }

        board
    }
}
```

## Racket

```racket
(define/contract (update-board board click)
  (-> (listof (listof char?)) (listof exact-integer?) (listof (listof char?)))
  (let* ((rows (length board))
         (cols (if (zero? rows) 0 (length (first board))))
         (vec-board (list->vector (map list->vector board)))
         (r (list-ref click 0))
         (c (list-ref click 1)))
    (define (in-bounds? rr cc)
      (and (>= rr 0) (< rr rows) (>= cc 0) (< cc cols)))
    (define dirs '((-1 -1) (-1 0) (-1 1) (0 -1) (0 1) (1 -1) (1 0) (1 1)))
    (define (count-adj rr cc)
      (let loop ((ds dirs) (cnt 0))
        (if (null? ds)
            cnt
            (let* ((dr (first (first ds))) (dc (second (first ds)))
                   (nr (+ rr dr)) (nc (+ cc dc)))
              (loop (rest ds)
                    (if (and (in-bounds? nr nc)
                             (char=? (vector-ref (vector-ref vec-board nr) nc) #\M))
                        (+ cnt 1) cnt))))))
    (define (push-neighbors rr cc stack)
      (let loop ((ds dirs) (stk stack))
        (if (null? ds)
            stk
            (let* ((dr (first (first ds))) (dc (second (first ds)))
                   (nr (+ rr dr)) (nc (+ cc dc)))
              (loop (rest ds)
                    (if (and (in-bounds? nr nc)
                             (char=? (vector-ref (vector-ref vec-board nr) nc) #\E))
                        (cons (cons nr nc) stk)
                        stk))))))
    (cond
      [(char=? (vector-ref (vector-ref vec-board r) c) #\M)
       (vector-set! (vector-ref vec-board r) c #\X)]
      [else
       (let loop ((stack (list (cons r c))))
         (when (not (null? stack))
           (define pos (car stack))
           (define rest (cdr stack))
           (define rr (car pos))
           (define cc (cdr pos))
           (if (and (in-bounds? rr cc)
                    (char=? (vector-ref (vector-ref vec-board rr) cc) #\E))
               (let ((cnt (count-adj rr cc)))
                 (if (> cnt 0)
                     (begin
                       (vector-set! (vector-ref vec-board rr) cc
                                    (integer->char (+ cnt (char->integer #\0))))
                       (loop rest))
                     (let ((new-stack (push-neighbors rr cc rest)))
                       (vector-set! (vector-ref vec-board rr) cc #\B)
                       (loop new-stack))))
               (loop rest))))]))
    (map vector->list (vector->list vec-board))))
```

## Erlang

```erlang
-spec update_board(Board :: [[char()]], Click :: [integer()]) -> [[char()]].
-export([update_board/2]).
-update_board(Board, Click) ->
-    M = length(Board),
-    N = case Board of [] -> 0; [Row|_] -> length(Row) end,
-    Map0 = board_to_map(Board, 0, #{}),
-    [ClickR, ClickC] = Click,
-    CharClicked = maps:get({ClickR, ClickC}, Map0),
-    Map1 =
-        if
-            CharClicked == $M ->
-                maps:put({ClickR, ClickC}, $X, Map0);
-            true ->
-                reveal(Map0, [{ClickR, ClickC}], M, N)
-        end,
-    map_to_board(Map1, M, N).

-reveal(Map, [], _M, _N) -> Map;
-reveal(Map, [{R, C} | Rest], M, N) ->
-    case maps:get({R, C}, Map) of
-        $E ->
-            Count = count_adjacent_mines(Map, R, C, M, N),
-            if
-                Count > 0 ->
-                    NewChar = $0 + Count,
-                    NewMap = maps:put({R, C}, NewChar, Map),
-                    reveal(NewMap, Rest, M, N);
-                true ->
-                    NewMap1 = maps:put({R, C}, $B, Map),
-                    Neighs = neighbors(R, C, M, N),
-                    ToAdd = [Pos || Pos <- Neighs,
-                                   maps:get(Pos, NewMap1) == $E],
-                    reveal(NewMap1, ToAdd ++ Rest, M, N)
-            end;
-        _Other ->
-            reveal(Map, Rest, M, N)
-    end.

-count_adjacent_mines(Map, R, C, M, N) ->
-    lists:foldl(
-      fun({Nr, Nc}, Acc) ->
-          case maps:get({Nr, Nc}, Map) of
-              $M -> Acc + 1;
-              _ -> Acc
-          end
-      end,
-      0,
-      neighbors(R, C, M, N)
-    ).

-neighbors(R, C, M, N) ->
-    Dirs = [{-1,-1},{-1,0},{-1,1},
-            {0,-1},        {0,1},
-            {1,-1},{1,0},{1,1}],
-    [ {Nr, Nc} ||
-      {Dr, Dc} <- Dirs,
-      Nr = R + Dr,
-      Nc = C + Dc,
-      0 =< Nr, Nr < M,
-      0 =< Nc, Nc < N ].

-board_to_map([], _RowIdx, Acc) -> Acc;
-board_to_map([Row|RestRows], RowIdx, Acc) ->
-    NewAcc = row_to_map(Row, RowIdx, 0, Acc),
-    board_to_map(RestRows, RowIdx + 1, NewAcc).

-row_to_map([], _R, _C, Acc) -> Acc;
-row_to_map([Char|Cs], R, C, Acc) ->
-    Updated = maps:put({R, C}, Char, Acc),
-    row_to_map(Cs, R, C + 1, Updated).

-map_to_board(Map, M, N) ->
-    [ row_from_map(R, Map, N) || R <- lists:seq(0, M - 1) ].

-row_from_map(R, Map, N) ->
-    [ maps:get({R, C}, Map) || C <- lists:seq(0, N - 1) ].
```

## Elixir

```elixir
defmodule Solution do
  @spec update_board(board :: [[char]], click :: [integer]) :: [[char]]
  def update_board(board, [r, c]) do
    case get_in(board, [Access.at(r), Access.at(c)]) do
      "M" ->
        put_in(board, [Access.at(r), Access.at(c)], "X")

      "E" ->
        bfs(board, :queue.from_list([{r, c}]), MapSet.new())

      _ ->
        board
    end
  end

  @dirs [
    {-1, -1},
    {-1, 0},
    {-1, 1},
    {0, -1},
    {0, 1},
    {1, -1},
    {1, 0},
    {1, 1}
  ]

  defp bfs(board, queue, visited) do
    case :queue.out(queue) do
      {:empty, _} ->
        board

      {{:value, {r, c}}, q_rest} ->
        if MapSet.member?(visited, {r, c}) do
          bfs(board, q_rest, visited)
        else
          visited = MapSet.put(visited, {r, c})
          count = count_mines(board, r, c)

          if count > 0 do
            board = put_in(board, [Access.at(r), Access.at(c)], Integer.to_string(count))
            bfs(board, q_rest, visited)
          else
            board = put_in(board, [Access.at(r), Access.at(c)], "B")

            q_new =
              Enum.reduce(@dirs, q_rest, fn {dr, dc}, acc ->
                nr = r + dr
                nc = c + dc

                if in_bounds(nr, nc, board) and
                     get_in(board, [Access.at(nr), Access.at(nc)]) == "E" do
                  :queue.in({nr, nc}, acc)
                else
                  acc
                end
              end)

            bfs(board, q_new, visited)
          end
        end
    end
  end

  defp count_mines(board, r, c) do
    Enum.count(@dirs, fn {dr, dc} ->
      nr = r + dr
      nc = c + dc

      in_bounds(nr, nc, board) and get_in(board, [Access.at(nr), Access.at(nc)]) == "M"
    end)
  end

  defp in_bounds(r, c, board) do
    rows = length(board)
    cols = board |> List.first() |> length()
    r >= 0 and r < rows and c >= 0 and c < cols
  end
end
```
