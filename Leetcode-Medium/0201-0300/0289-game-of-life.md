# 0289. Game of Life

## Cpp

```cpp
class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        int m = board.size();
        if (m == 0) return;
        int n = board[0].size();
        vector<pair<int,int>> dirs = {{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};
        
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int live = 0;
                for (auto& d : dirs) {
                    int ni = i + d.first, nj = j + d.second;
                    if (ni >= 0 && ni < m && nj >= 0 && nj < n) {
                        if (board[ni][nj] == 1 || board[ni][nj] == -1)
                            ++live;
                    }
                }
                if (board[i][j] == 1) {
                    if (live < 2 || live > 3) {
                        board[i][j] = -1; // live -> dead
                    }
                } else { // dead cell
                    if (live == 3) {
                        board[i][j] = 2; // dead -> live
                    }
                }
            }
        }
        
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                board[i][j] = (board[i][j] > 0) ? 1 : 0;
    }
};
```

## Java

```java
class Solution {
    public void gameOfLife(int[][] board) {
        int m = board.length;
        int n = board[0].length;
        int[] dirs = {-1, 0, 1};
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int liveNeighbors = 0;
                for (int dx : dirs) {
                    for (int dy : dirs) {
                        if (dx == 0 && dy == 0) continue;
                        int ni = i + dx, nj = j + dy;
                        if (ni >= 0 && ni < m && nj >= 0 && nj < n && Math.abs(board[ni][nj]) == 1) {
                            liveNeighbors++;
                        }
                    }
                }
                if (board[i][j] == 1) {
                    if (liveNeighbors < 2 || liveNeighbors > 3) {
                        board[i][j] = -1; // live to dead
                    }
                } else { // dead cell
                    if (liveNeighbors == 3) {
                        board[i][j] = 2; // dead to live
                    }
                }
            }
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] > 0) board[i][j] = 1;
                else board[i][j] = 0;
            }
        }
    }
}
```

## Python

```python
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        dirs = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1),          (0, 1),
                (1, -1),  (1, 0), (1, 1)]
        for i in range(m):
            for j in range(n):
                live_neighbors = 0
                for dx, dy in dirs:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n:
                        live_neighbors += board[ni][nj] & 1
                cell = board[i][j] & 1
                if cell == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = -1  # live -> dead
                else:
                    if live_neighbors == 3:
                        board[i][j] = 2   # dead -> live
        for i in range(m):
            for j in range(n):
                board[i][j] = 1 if board[i][j] > 0 else 0
```

## Python3

```python
class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        dirs = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1),          (0, 1),
                (1, -1),  (1, 0), (1, 1)]
        
        for i in range(m):
            for j in range(n):
                live = 0
                for dx, dy in dirs:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n and (board[ni][nj] == 1 or board[ni][nj] == -1):
                        live += 1
                if board[i][j] == 1:
                    if live < 2 or live > 3:
                        board[i][j] = -1   # live -> dead
                else:  # dead cell
                    if live == 3:
                        board[i][j] = 2    # dead -> live
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1
```

## C

```c
void gameOfLife(int** board, int boardSize, int* boardColSize) {
    if (boardSize == 0 || boardColSize == NULL) return;
    int dirs[8][2] = {{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};
    
    for (int i = 0; i < boardSize; ++i) {
        int cols = boardColSize[i];
        for (int j = 0; j < cols; ++j) {
            int liveNeighbors = 0;
            for (int d = 0; d < 8; ++d) {
                int ni = i + dirs[d][0];
                int nj = j + dirs[d][1];
                if (ni >= 0 && ni < boardSize && nj >= 0 && nj < boardColSize[ni]) {
                    liveNeighbors += board[ni][nj] & 1;
                }
            }
            int cur = board[i][j] & 1;
            if (cur) {
                if (liveNeighbors == 2 || liveNeighbors == 3) {
                    board[i][j] |= 2; // becomes alive
                }
            } else {
                if (liveNeighbors == 3) {
                    board[i][j] |= 2; // becomes alive
                }
            }
        }
    }
    
    for (int i = 0; i < boardSize; ++i) {
        int cols = boardColSize[i];
        for (int j = 0; j < cols; ++j) {
            board[i][j] >>= 1;
        }
    }
}
```

## Csharp

```csharp
public class Solution {
    public void GameOfLife(int[][] board) {
        int m = board.Length;
        if (m == 0) return;
        int n = board[0].Length;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int liveNeighbors = 0;
                for (int di = -1; di <= 1; di++) {
                    for (int dj = -1; dj <= 1; dj++) {
                        if (di == 0 && dj == 0) continue;
                        int ni = i + di, nj = j + dj;
                        if (ni >= 0 && ni < m && nj >= 0 && nj < n) {
                            if (Math.Abs(board[ni][nj]) == 1) liveNeighbors++;
                        }
                    }
                }

                if (board[i][j] == 1) {
                    if (liveNeighbors < 2 || liveNeighbors > 3) {
                        board[i][j] = -1; // live to dead
                    }
                } else { // dead cell
                    if (liveNeighbors == 3) {
                        board[i][j] = 2; // dead to live
                    }
                }
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] > 0) board[i][j] = 1;
                else board[i][j] = 0;
            }
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var gameOfLife = function(board) {
    const m = board.length;
    if (m === 0) return;
    const n = board[0].length;
    const dirs = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1],          [0, 1],
        [1, -1],  [1, 0], [1, 1]
    ];
    
    // First pass: compute next state with encoding
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            let liveNeighbors = 0;
            for (const [dx, dy] of dirs) {
                const x = i + dx, y = j + dy;
                if (x >= 0 && x < m && y >= 0 && y < n) {
                    const val = board[x][y];
                    if (val === 1 || val === 2) liveNeighbors++; // originally alive
                }
            }
            const cell = board[i][j];
            if (cell === 1) {
                if (liveNeighbors < 2 || liveNeighbors > 3) {
                    board[i][j] = 2; // alive -> dead
                }
            } else { // cell === 0
                if (liveNeighbors === 3) {
                    board[i][j] = -1; // dead -> alive
                }
            }
        }
    }
    
    // Second pass: finalize the state
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (board[i][j] === 2) board[i][j] = 0;
            else if (board[i][j] === -1) board[i][j] = 1;
        }
    }
};
```

## Typescript

```typescript
function gameOfLife(board: number[][]): void {
    const m = board.length;
    if (m === 0) return;
    const n = board[0].length;
    const dirs = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1],          [0, 1],
        [1, -1],  [1, 0], [1, 1]
    ];
    
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            let liveNeighbors = 0;
            for (const [dx, dy] of dirs) {
                const x = i + dx, y = j + dy;
                if (x >= 0 && x < m && y >= 0 && y < n) {
                    const val = board[x][y];
                    if (val === 1 || val === -1) liveNeighbors++;
                }
            }
            if (board[i][j] === 1) {
                if (liveNeighbors < 2 || liveNeighbors > 3) {
                    board[i][j] = -1; // live -> dead
                }
            } else { // dead cell
                if (liveNeighbors === 3) {
                    board[i][j] = 2; // dead -> live
                }
            }
        }
    }
    
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (board[i][j] === -1) board[i][j] = 0;
            else if (board[i][j] === 2) board[i][j] = 1;
        }
    }
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $board
     * @return NULL
     */
    function gameOfLife(&$board) {
        $m = count($board);
        if ($m == 0) return;
        $n = count($board[0]);
        $dirs = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]];
        
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $liveNeighbors = 0;
                foreach ($dirs as $d) {
                    $ni = $i + $d[0];
                    $nj = $j + $d[1];
                    if ($ni >= 0 && $ni < $m && $nj >= 0 && $nj < $n) {
                        $liveNeighbors += $board[$ni][$nj] & 1;
                    }
                }
                $cell = $board[$i][$j] & 1;
                if ($cell == 1) {
                    // live cell
                    if ($liveNeighbors == 2 || $liveNeighbors == 3) {
                        $board[$i][$j] = 3; // 11: stays alive
                    } else {
                        $board[$i][$j] = 2; // 10: dies
                    }
                } else {
                    // dead cell
                    if ($liveNeighbors == 3) {
                        $board[$i][$j] = 1; // 01: becomes alive
                    } else {
                        $board[$i][$j] = 0; // stays dead
                    }
                }
            }
        }
        
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $board[$i][$j] >>= 1;
            }
        }
    }
}
```

## Swift

```swift
class Solution {
    func gameOfLife(_ board: inout [[Int]]) {
        let m = board.count
        guard m > 0 else { return }
        let n = board[0].count
        let dirs = [(-1, -1), (-1, 0), (-1, 1),
                    (0, -1),          (0, 1),
                    (1, -1),  (1, 0),  (1, 1)]
        
        for i in 0..<m {
            for j in 0..<n {
                var liveNeighbors = 0
                for d in dirs {
                    let ni = i + d.0
                    let nj = j + d.1
                    if ni >= 0 && ni < m && nj >= 0 && nj < n {
                        if (board[ni][nj] & 1) == 1 {
                            liveNeighbors += 1
                        }
                    }
                }
                
                let current = board[i][j] & 1
                var newState = 0
                if current == 1 {
                    if liveNeighbors == 2 || liveNeighbors == 3 {
                        newState = 1
                    }
                } else {
                    if liveNeighbors == 3 {
                        newState = 1
                    }
                }
                
                board[i][j] |= (newState << 1)
            }
        }
        
        for i in 0..<m {
            for j in 0..<n {
                board[i][j] >>= 1
            }
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun gameOfLife(board: Array<IntArray>) {
        val m = board.size
        if (m == 0) return
        val n = board[0].size
        val dirs = arrayOf(
            intArrayOf(-1, -1), intArrayOf(-1, 0), intArrayOf(-1, 1),
            intArrayOf(0, -1),                 intArrayOf(0, 1),
            intArrayOf(1, -1), intArrayOf(1, 0), intArrayOf(1, 1)
        )
        // First pass: encode transitions
        for (i in 0 until m) {
            for (j in 0 until n) {
                var live = 0
                for (d in dirs) {
                    val ni = i + d[0]
                    val nj = j + d[1]
                    if (ni in 0 until m && nj in 0 until n) {
                        if ((board[ni][nj] and 1) == 1) live++
                    }
                }
                when (board[i][j]) {
                    1 -> { // currently alive
                        if (live < 2 || live > 3) {
                            board[i][j] = 2 // alive -> dead
                        }
                    }
                    0 -> { // currently dead
                        if (live == 3) {
                            board[i][j] = 3 // dead -> alive
                        }
                    }
                }
            }
        }
        // Second pass: finalize states
        for (i in 0 until m) {
            for (j in 0 until n) {
                when (board[i][j]) {
                    2 -> board[i][j] = 0
                    3 -> board[i][j] = 1
                }
            }
        }
    }
}
```

## Dart

```dart
class Solution {
  void gameOfLife(List<List<int>> board) {
    int m = board.length;
    if (m == 0) return;
    int n = board[0].length;

    const dirs = [-1, 0, 1];

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        int liveNeighbors = 0;
        for (int dx in dirs) {
          for (int dy in dirs) {
            if (dx == 0 && dy == 0) continue;
            int ni = i + dx;
            int nj = j + dy;
            if (ni >= 0 && ni < m && nj >= 0 && nj < n) {
              int val = board[ni][nj];
              if (val == 1 || val == 2) {
                liveNeighbors++;
              }
            }
          }
        }

        if (board[i][j] == 1) {
          if (liveNeighbors < 2 || liveNeighbors > 3) {
            board[i][j] = 2; // live -> dead
          }
        } else {
          if (liveNeighbors == 3) {
            board[i][j] = -1; // dead -> live
          }
        }
      }
    }

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (board[i][j] == -1) {
          board[i][j] = 1;
        } else if (board[i][j] == 2) {
          board[i][j] = 0;
        }
      }
    }
  }
}
```

## Golang

```go
func gameOfLife(board [][]int) {
    m := len(board)
    n := len(board[0])
    dirs := [8][2]int{{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}}

    // First pass: compute next state using temporary markers
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            liveNeighbors := 0
            for _, d := range dirs {
                ni, nj := i+d[0], j+d[1]
                if ni >= 0 && ni < m && nj >= 0 && nj < n {
                    if board[ni][nj] == 1 || board[ni][nj] == -1 {
                        liveNeighbors++
                    }
                }
            }
            if board[i][j] == 1 {
                if liveNeighbors < 2 || liveNeighbors > 3 {
                    board[i][j] = -1 // live -> dead
                }
            } else { // board[i][j] == 0
                if liveNeighbors == 3 {
                    board[i][j] = 2 // dead -> live
                }
            }
        }
    }

    // Second pass: finalize the state
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if board[i][j] == -1 {
                board[i][j] = 0
            } else if board[i][j] == 2 {
                board[i][j] = 1
            }
        }
    }
}
```

## Ruby

```ruby
def game_of_life(board)
  m = board.size
  n = board[0].size
  dirs = [-1, 0, 1]

  (0...m).each do |i|
    (0...n).each do |j|
      live_neighbors = 0
      dirs.each do |dx|
        dirs.each do |dy|
          next if dx == 0 && dy == 0
          x = i + dx
          y = j + dy
          if x.between?(0, m - 1) && y.between?(0, n - 1) && board[x][y].abs == 1
            live_neighbors += 1
          end
        end
      end

      if board[i][j] == 1
        board[i][j] = -1 if live_neighbors < 2 || live_neighbors > 3
      else
        board[i][j] = 2 if live_neighbors == 3
      end
    end
  end

  (0...m).each do |i|
    (0...n).each do |j|
      board[i][j] = board[i][j] > 0 ? 1 : 0
    end
  end
end
```

## Scala

```scala
object Solution {
    def gameOfLife(board: Array[Array[Int]]): Unit = {
        val m = board.length
        val n = board(0).length
        val dirs = Array(
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1),  (1, 0), (1, 1)
        )
        for (i <- 0 until m) {
            for (j <- 0 until n) {
                var live = 0
                for ((dx, dy) <- dirs) {
                    val x = i + dx
                    val y = j + dy
                    if (x >= 0 && x < m && y >= 0 && y < n) {
                        val v = board(x)(y)
                        if (v == 1 || v == -1) live += 1 // originally alive
                    }
                }
                if (board(i)(j) == 1) {
                    if (live < 2 || live > 3) board(i)(j) = -1 // live -> dead
                } else {
                    if (live == 3) board(i)(j) = 2 // dead -> live
                }
            }
        }
        for (i <- 0 until m) {
            for (j <- 0 until n) {
                board(i)(j) match {
                    case -1 => board(i)(j) = 0
                    case 2  => board(i)(j) = 1
                    case _  => // unchanged
                }
            }
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn game_of_life(board: &mut Vec<Vec<i32>>) {
        let m = board.len();
        if m == 0 { return; }
        let n = board[0].len();

        // Directions for the eight neighbors
        let dirs = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1),  (1, 0), (1, 1),
        ];

        // First pass: compute next state and store it in the second bit
        for i in 0..m {
            for j in 0..n {
                let mut live_neighbors = 0;
                for &(dx, dy) in &dirs {
                    let ni = i as isize + dx;
                    let nj = j as isize + dy;
                    if ni >= 0 && ni < m as isize && nj >= 0 && nj < n as isize {
                        // original state is stored in the least significant bit
                        live_neighbors += (board[ni as usize][nj as usize] & 1) as i32;
                    }
                }

                let cell = board[i][j] & 1;
                if cell == 1 {
                    // Live cell stays alive with 2 or 3 live neighbors
                    if live_neighbors == 2 || live_neighbors == 3 {
                        board[i][j] |= 2; // set second bit to 1
                    }
                } else {
                    // Dead cell becomes alive with exactly 3 live neighbors
                    if live_neighbors == 3 {
                        board[i][j] |= 2;
                    }
                }
            }
        }

        // Second pass: shift bits to make next state the current state
        for i in 0..m {
            for j in 0..n {
                board[i][j] >>= 1;
            }
        }
    }
}
```
