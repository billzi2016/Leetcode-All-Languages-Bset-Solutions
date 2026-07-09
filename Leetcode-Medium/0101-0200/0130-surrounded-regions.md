# 0130. Surrounded Regions

## Cpp

```cpp
class Solution {
public:
    void solve(std::vector<std::vector<char>>& board) {
        int m = board.size();
        if (m == 0) return;
        int n = board[0].size();
        auto bfs = [&](int si, int sj) {
            std::queue<std::pair<int,int>> q;
            q.emplace(si, sj);
            board[si][sj] = 'E';
            const int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
            while (!q.empty()) {
                auto [i,j] = q.front(); q.pop();
                for (auto &d : dirs) {
                    int ni = i + d[0], nj = j + d[1];
                    if (ni >= 0 && ni < m && nj >= 0 && nj < n && board[ni][nj] == 'O') {
                        board[ni][nj] = 'E';
                        q.emplace(ni, nj);
                    }
                }
            }
        };
        // top and bottom rows
        for (int j = 0; j < n; ++j) {
            if (board[0][j] == 'O') bfs(0, j);
            if (board[m-1][j] == 'O') bfs(m-1, j);
        }
        // left and right columns
        for (int i = 0; i < m; ++i) {
            if (board[i][0] == 'O') bfs(i, 0);
            if (board[i][n-1] == 'O') bfs(i, n-1);
        }
        // flip cells
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (board[i][j] == 'O')
                    board[i][j] = 'X';
                else if (board[i][j] == 'E')
                    board[i][j] = 'O';
            }
        }
    }
};
```

## Java

```java
import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public void solve(char[][] board) {
        if (board == null || board.length == 0) return;
        int m = board.length, n = board[0].length;
        // Process border cells
        for (int i = 0; i < m; i++) {
            if (board[i][0] == 'O') bfs(board, i, 0);
            if (n > 1 && board[i][n - 1] == 'O') bfs(board, i, n - 1);
        }
        for (int j = 1; j < n - 1; j++) {
            if (board[0][j] == 'O') bfs(board, 0, j);
            if (m > 1 && board[m - 1][j] == 'O') bfs(board, m - 1, j);
        }
        // Flip interior O to X and revert temporary marks
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O') board[i][j] = 'X';
                else if (board[i][j] == 'E') board[i][j] = 'O';
            }
        }
    }

    private void bfs(char[][] board, int startI, int startJ) {
        int m = board.length, n = board[0].length;
        Deque<int[]> q = new ArrayDeque<>();
        q.add(new int[]{startI, startJ});
        board[startI][startJ] = 'E';
        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int i = cur[0], j = cur[1];
            for (int[] d : dirs) {
                int ni = i + d[0], nj = j + d[1];
                if (ni >= 0 && ni < m && nj >= 0 && nj < n && board[ni][nj] == 'O') {
                    board[ni][nj] = 'E';
                    q.add(new int[]{ni, nj});
                }
            }
        }
    }
}
```

## Python

```python
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        from collections import deque

        def bfs(i, j):
            q = deque()
            q.append((i, j))
            board[i][j] = 'E'  # mark as escaped
            while q:
                x, y = q.popleft()
                for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'O':
                        board[nx][ny] = 'E'
                        q.append((nx, ny))

        # start from border cells
        for i in range(m):
            if board[i][0] == 'O':
                bfs(i, 0)
            if board[i][n-1] == 'O':
                bfs(i, n-1)
        for j in range(n):
            if board[0][j] == 'O':
                bfs(0, j)
            if board[m-1][j] == 'O':
                bfs(m-1, j)

        # flip captured regions and restore escaped ones
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'E':
                    board[i][j] = 'O"
```

## Python3

```python
from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        q = deque()
        # enqueue border 'O's
        for i in range(m):
            for j in (0, n - 1):
                if board[i][j] == 'O':
                    board[i][j] = 'E'
                    q.append((i, j))
        for j in range(n):
            for i in (0, m - 1):
                if board[i][j] == 'O':
                    board[i][j] = 'E'
                    q.append((i, j))
        # BFS to mark all connected 'O's
        while q:
            x, y = q.popleft()
            for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'O':
                    board[nx][ny] = 'E'
                    q.append((nx, ny))
        # flip cells to final states
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'E':
                    board[i][j] = 'O"
```

## C

```c
#include <stdlib.h>

void solve(char** board, int boardSize, int* boardColSize) {
    if (boardSize == 0 || boardColSize == NULL) return;
    int m = boardSize;
    int n = boardColSize[0];
    if (n == 0) return;

    int total = m * n;
    int *queue = (int *)malloc(total * sizeof(int));
    int front = 0, rear = 0;

    // Helper to enqueue a cell and mark it as safe ('E')
    #define ENQUEUE(i, j) do { \
        board[i][j] = 'E'; \
        queue[rear++] = (i) * n + (j); \
    } while (0)

    // Add border O's to the queue
    for (int i = 0; i < m; ++i) {
        if (board[i][0] == 'O') ENQUEUE(i, 0);
        if (n > 1 && board[i][n - 1] == 'O') ENQUEUE(i, n - 1);
    }
    for (int j = 1; j < n - 1; ++j) {
        if (board[0][j] == 'O') ENQUEUE(0, j);
        if (m > 1 && board[m - 1][j] == 'O') ENQUEUE(m - 1, j);
    }

    // BFS to mark all O's connected to border
    while (front < rear) {
        int idx = queue[front++];
        int x = idx / n;
        int y = idx % n;

        if (x > 0 && board[x - 1][y] == 'O') ENQUEUE(x - 1, y);
        if (x + 1 < m && board[x + 1][y] == 'O') ENQUEUE(x + 1, y);
        if (y > 0 && board[x][y - 1] == 'O') ENQUEUE(x, y - 1);
        if (y + 1 < n && board[x][y + 1] == 'O') ENQUEUE(x, y + 1);
    }

    // Flip captured regions and restore safe ones
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (board[i][j] == 'O')
                board[i][j] = 'X';
            else if (board[i][j] == 'E')
                board[i][j] = 'O';
        }
    }

    free(queue);
    #undef ENQUEUE
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public void Solve(char[][] board) {
        int m = board.Length;
        if (m == 0) return;
        int n = board[0].Length;
        var dirs = new int[,] { {1,0}, {-1,0}, {0,1}, {0,-1} };

        void Mark(int i, int j) {
            var stack = new Stack<(int, int)>();
            stack.Push((i, j));
            board[i][j] = 'E';
            while (stack.Count > 0) {
                var (x, y) = stack.Pop();
                for (int d = 0; d < 4; d++) {
                    int nx = x + dirs[d, 0];
                    int ny = y + dirs[d, 1];
                    if (nx >= 0 && nx < m && ny >= 0 && ny < n && board[nx][ny] == 'O') {
                        board[nx][ny] = 'E';
                        stack.Push((nx, ny));
                    }
                }
            }
        }

        // Top and bottom rows
        for (int j = 0; j < n; j++) {
            if (board[0][j] == 'O') Mark(0, j);
            if (m > 1 && board[m - 1][j] == 'O') Mark(m - 1, j);
        }

        // Left and right columns
        for (int i = 0; i < m; i++) {
            if (board[i][0] == 'O') Mark(i, 0);
            if (n > 1 && board[i][n - 1] == 'O') Mark(i, n - 1);
        }

        // Flip captured regions and restore border-connected ones
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O')
                    board[i][j] = 'X';
                else if (board[i][j] == 'E')
                    board[i][j] = 'O';
            }
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solve = function(board) {
    const m = board.length;
    if (m === 0) return;
    const n = board[0].length;
    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    
    const mark = (i, j) => {
        const stack = [[i, j]];
        while (stack.length) {
            const [x, y] = stack.pop();
            if (board[x][y] !== 'O') continue;
            board[x][y] = 'E';
            for (const [dx, dy] of dirs) {
                const nx = x + dx, ny = y + dy;
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && board[nx][ny] === 'O') {
                    stack.push([nx, ny]);
                }
            }
        }
    };
    
    // Top and bottom rows
    for (let j = 0; j < n; j++) {
        if (board[0][j] === 'O') mark(0, j);
        if (board[m - 1][j] === 'O') mark(m - 1, j);
    }
    // Left and right columns
    for (let i = 0; i < m; i++) {
        if (board[i][0] === 'O') mark(i, 0);
        if (board[i][n - 1] === 'O') mark(i, n - 1);
    }
    
    // Flip captured regions and restore safe ones
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (board[i][j] === 'O') {
                board[i][j] = 'X';
            } else if (board[i][j] === 'E') {
                board[i][j] = 'O';
            }
        }
    }
};
```

## Typescript

```typescript
/**
 Do not return anything, modify board in-place instead.
 */
function solve(board: string[][]): void {
    const m = board.length;
    if (m === 0) return;
    const n = board[0].length;
    const dirs: number[][] = [[1, 0], [-1, 0], [0, 1], [0, -1]];

    const bfs = (i: number, j: number): void => {
        const stack: [number, number][] = [[i, j]];
        board[i][j] = 'E';
        while (stack.length) {
            const [x, y] = stack.pop()!;
            for (const [dx, dy] of dirs) {
                const nx = x + dx;
                const ny = y + dy;
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && board[nx][ny] === 'O') {
                    board[nx][ny] = 'E';
                    stack.push([nx, ny]);
                }
            }
        }
    };

    // Top and bottom rows
    for (let j = 0; j < n; j++) {
        if (board[0][j] === 'O') bfs(0, j);
        if (board[m - 1][j] === 'O') bfs(m - 1, j);
    }
    // Left and right columns
    for (let i = 0; i < m; i++) {
        if (board[i][0] === 'O') bfs(i, 0);
        if (board[i][n - 1] === 'O') bfs(i, n - 1);
    }

    // Flip cells to final state
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (board[i][j] === 'O') {
                board[i][j] = 'X';
            } else if (board[i][j] === 'E') {
                board[i][j] = 'O';
            }
        }
    }
}
```

## Php

```php
class Solution {

    /**
     * @param String[][] $board
     * @return NULL
     */
    function solve(&$board) {
        $m = count($board);
        if ($m == 0) return;
        $n = count($board[0]);
        $stack = [];

        // top and bottom rows
        for ($j = 0; $j < $n; $j++) {
            if ($board[0][$j] === 'O') {
                $board[0][$j] = 'E';
                $stack[] = [0, $j];
            }
            if ($m - 1 != 0 && $board[$m - 1][$j] === 'O') {
                $board[$m - 1][$j] = 'E';
                $stack[] = [$m - 1, $j];
            }
        }

        // left and right columns
        for ($i = 0; $i < $m; $i++) {
            if ($board[$i][0] === 'O') {
                $board[$i][0] = 'E';
                $stack[] = [$i, 0];
            }
            if ($n - 1 != 0 && $board[$i][$n - 1] === 'O') {
                $board[$i][$n - 1] = 'E';
                $stack[] = [$i, $n - 1];
            }
        }

        $dirs = [[1,0],[-1,0],[0,1],[0,-1]];
        while (!empty($stack)) {
            [$i, $j] = array_pop($stack);
            foreach ($dirs as $d) {
                $ni = $i + $d[0];
                $nj = $j + $d[1];
                if ($ni >= 0 && $ni < $m && $nj >= 0 && $nj < $n && $board[$ni][$nj] === 'O') {
                    $board[$ni][$nj] = 'E';
                    $stack[] = [$ni, $nj];
                }
            }
        }

        // flip cells to final state
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($board[$i][$j] === 'O') {
                    $board[$i][$j] = 'X';
                } elseif ($board[$i][$j] === 'E') {
                    $board[$i][$j] = 'O';
                }
            }
        }
    }
}
```

## Swift

```swift
class Solution {
    func solve(_ board: inout [[Character]]) {
        let m = board.count
        guard m > 0 else { return }
        let n = board[0].count
        if n == 0 { return }

        var queue = [(Int, Int)]()
        // Add border O's
        for i in 0..<m {
            if board[i][0] == "O" {
                queue.append((i, 0))
            }
            if n > 1 && board[i][n - 1] == "O" {
                queue.append((i, n - 1))
            }
        }
        for j in 0..<n {
            if board[0][j] == "O" {
                queue.append((0, j))
            }
            if m > 1 && board[m - 1][j] == "O" {
                queue.append((m - 1, j))
            }
        }

        let dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        var idx = 0
        while idx < queue.count {
            let (x, y) = queue[idx]
            idx += 1
            if board[x][y] != "O" { continue }
            board[x][y] = "E"
            for d in dirs {
                let nx = x + d.0
                let ny = y + d.1
                if nx >= 0 && nx < m && ny >= 0 && ny < n && board[nx][ny] == "O" {
                    queue.append((nx, ny))
                }
            }
        }

        // Flip cells
        for i in 0..<m {
            for j in 0..<n {
                if board[i][j] == "O" {
                    board[i][j] = "X"
                } else if board[i][j] == "E" {
                    board[i][j] = "O"
                }
            }
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun solve(board: Array<CharArray>) {
        val m = board.size
        if (m == 0) return
        val n = board[0].size
        val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
        val queue: ArrayDeque<Pair<Int, Int>> = ArrayDeque()

        fun enqueueIfO(i: Int, j: Int) {
            if (board[i][j] == 'O') {
                board[i][j] = 'E'
                queue.add(Pair(i, j))
            }
        }

        // Top and bottom rows
        for (j in 0 until n) {
            enqueueIfO(0, j)
            enqueueIfO(m - 1, j)
        }
        // Left and right columns
        for (i in 0 until m) {
            enqueueIfO(i, 0)
            enqueueIfO(i, n - 1)
        }

        while (queue.isNotEmpty()) {
            val (x, y) = queue.removeFirst()
            for (d in dirs) {
                val nx = x + d[0]
                val ny = y + d[1]
                if (nx in 0 until m && ny in 0 until n && board[nx][ny] == 'O') {
                    board[nx][ny] = 'E'
                    queue.add(Pair(nx, ny))
                }
            }
        }

        for (i in 0 until m) {
            for (j in 0 until n) {
                when (board[i][j]) {
                    'O' -> board[i][j] = 'X'
                    'E' -> board[i][j] = 'O'
                }
            }
        }
    }
}
```

## Dart

```dart
class Solution {
  void solve(List<List<String>> board) {
    int m = board.length;
    if (m == 0) return;
    int n = board[0].length;

    void dfs(int i, int j) {
      var stack = <List<int>>[];
      stack.add([i, j]);
      while (stack.isNotEmpty) {
        var cell = stack.removeLast();
        int x = cell[0], y = cell[1];
        if (x < 0 || x >= m || y < 0 || y >= n || board[x][y] != 'O') continue;
        board[x][y] = '#';
        stack.add([x - 1, y]);
        stack.add([x + 1, y]);
        stack.add([x, y - 1]);
        stack.add([x, y + 1]);
      }
    }

    // Mark border-connected 'O's
    for (int i = 0; i < m; i++) {
      if (board[i][0] == 'O') dfs(i, 0);
      if (n > 1 && board[i][n - 1] == 'O') dfs(i, n - 1);
    }
    for (int j = 0; j < n; j++) {
      if (board[0][j] == 'O') dfs(0, j);
      if (m > 1 && board[m - 1][j] == 'O') dfs(m - 1, j);
    }

    // Flip captured regions and restore safe ones
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (board[i][j] == 'O') {
          board[i][j] = 'X';
        } else if (board[i][j] == '#') {
          board[i][j] = 'O';
        }
      }
    }
  }
}
```

## Golang

```go
func solve(board [][]byte) {
	m := len(board)
	if m == 0 {
		return
	}
	n := len(board[0])

	bfs := func(i, j int) {
		queue := make([][2]int, 0)
		queue = append(queue, [2]int{i, j})
		board[i][j] = 'E'
		dirs := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
		for len(queue) > 0 {
			cur := queue[0]
			queue = queue[1:]
			x, y := cur[0], cur[1]
			for _, d := range dirs {
				nx, ny := x+d[0], y+d[1]
				if nx >= 0 && nx < m && ny >= 0 && ny < n && board[nx][ny] == 'O' {
					board[nx][ny] = 'E'
					queue = append(queue, [2]int{nx, ny})
				}
			}
		}
	}

	for j := 0; j < n; j++ {
		if board[0][j] == 'O' {
			bfs(0, j)
		}
		if m > 1 && board[m-1][j] == 'O' {
			bfs(m-1, j)
		}
	}
	for i := 1; i < m-1; i++ {
		if board[i][0] == 'O' {
			bfs(i, 0)
		}
		if n > 1 && board[i][n-1] == 'O' {
			bfs(i, n-1)
		}
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if board[i][j] == 'O' {
				board[i][j] = 'X'
			} else if board[i][j] == 'E' {
				board[i][j] = 'O'
			}
		}
	}
}
```

## Ruby

```ruby
def solve(board)
  return if board.empty?
  m = board.size
  n = board[0].size
  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  stack = []

  add_border_o = lambda do |i, j|
    if board[i][j] == 'O'
      board[i][j] = '#'
      stack << [i, j]
    end
  end

  (0...m).each do |i|
    add_border_o.call(i, 0)
    add_border_o.call(i, n - 1) if n > 1
  end

  (0...n).each do |j|
    add_border_o.call(0, j)
    add_border_o.call(m - 1, j) if m > 1
  end

  until stack.empty?
    i, j = stack.pop
    dirs.each do |di, dj|
      ni = i + di
      nj = j + dj
      next unless ni.between?(0, m - 1) && nj.between?(0, n - 1)
      if board[ni][nj] == 'O'
        board[ni][nj] = '#'
        stack << [ni, nj]
      end
    end
  end

  (0...m).each do |i|
    (0...n).each do |j|
      case board[i][j]
      when 'O' then board[i][j] = 'X'
      when '#'
        board[i][j] = 'O'
      end
    end
  end
end
```

## Scala

```scala
object Solution {
  def solve(board: Array[Array[Char]]): Unit = {
    val m = board.length
    if (m == 0) return
    val n = board(0).length
    import java.util.ArrayDeque

    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))

    def bfs(si: Int, sj: Int): Unit = {
      val q = new ArrayDeque[(Int, Int)]()
      q.add((si, sj))
      board(si)(sj) = 'E'
      while (!q.isEmpty) {
        val (i, j) = q.poll()
        var k = 0
        while (k < 4) {
          val ni = i + dirs(k)._1
          val nj = j + dirs(k)._2
          if (ni >= 0 && ni < m && nj >= 0 && nj < n && board(ni)(nj) == 'O') {
            board(ni)(nj) = 'E'
            q.add((ni, nj))
          }
          k += 1
        }
      }
    }

    // top and bottom rows
    for (j <- 0 until n) {
      if (board(0)(j) == 'O') bfs(0, j)
      if (m > 1 && board(m - 1)(j) == 'O') bfs(m - 1, j)
    }
    // left and right columns
    for (i <- 0 until m) {
      if (board(i)(0) == 'O') bfs(i, 0)
      if (n > 1 && board(i)(n - 1) == 'O') bfs(i, n - 1)
    }

    // flip cells
    for (i <- 0 until m) {
      for (j <- 0 until n) {
        board(i)(j) match {
          case 'O' => board(i)(j) = 'X'
          case 'E' => board(i)(j) = 'O'
          case _   =>
        }
      }
    }
  }
}
```

## Rust

```rust
impl Solution {
    pub fn solve(board: &mut Vec<Vec<char>>) {
        let m = board.len();
        if m == 0 { return; }
        let n = board[0].len();
        if n == 0 { return; }

        // Helper closure to perform DFS from a border 'O'
        let mut dfs = |i: usize, j: usize, board: &mut Vec<Vec<char>>| {
            let mut stack = Vec::new();
            stack.push((i, j));
            while let Some((x, y)) = stack.pop() {
                if board[x][y] != 'O' { continue; }
                board[x][y] = 'E'; // mark as escaped
                // up
                if x > 0 && board[x - 1][y] == 'O' {
                    stack.push((x - 1, y));
                }
                // down
                if x + 1 < m && board[x + 1][y] == 'O' {
                    stack.push((x + 1, y));
                }
                // left
                if y > 0 && board[x][y - 1] == 'O' {
                    stack.push((x, y - 1));
                }
                // right
                if y + 1 < n && board[x][y + 1] == 'O' {
                    stack.push((x, y + 1));
                }
            }
        };

        // Scan first and last rows
        for j in 0..n {
            if board[0][j] == 'O' {
                dfs(0, j, board);
            }
            if m > 1 && board[m - 1][j] == 'O' {
                dfs(m - 1, j, board);
            }
        }

        // Scan first and last columns (excluding corners already handled)
        for i in 1..m.saturating_sub(1) {
            if board[i][0] == 'O' {
                dfs(i, 0, board);
            }
            if n > 1 && board[i][n - 1] == 'O' {
                dfs(i, n - 1, board);
            }
        }

        // Flip captured regions and restore escaped ones
        for i in 0..m {
            for j in 0..n {
                match board[i][j] {
                    'O' => board[i][j] = 'X',
                    'E' => board[i][j] = 'O',
                    _ => {}
                }
            }
        }
    }
}
```
