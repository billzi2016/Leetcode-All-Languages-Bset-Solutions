# 0200. Number of Islands

## Cpp

```cpp
class Solution {
public:
    int numIslands(std::vector<std::vector<char>>& grid) {
        if (grid.empty() || grid[0].empty()) return 0;
        int m = grid.size(), n = grid[0].size();
        int islands = 0;
        const int dr[4] = { -1, 1, 0, 0 };
        const int dc[4] = { 0, 0, -1, 1 };
        std::queue<std::pair<int,int>> q;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == '1') {
                    ++islands;
                    grid[i][j] = '0';
                    q.emplace(i, j);
                    while (!q.empty()) {
                        auto [r, c] = q.front(); q.pop();
                        for (int k = 0; k < 4; ++k) {
                            int nr = r + dr[k];
                            int nc = c + dc[k];
                            if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == '1') {
                                grid[nr][nc] = '0';
                                q.emplace(nr, nc);
                            }
                        }
                    }
                }
            }
        }
        return islands;
    }
};
```

## Java

```java
class Solution {
    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0) return 0;
        int rows = grid.length, cols = grid[0].length;
        int count = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == '1') {
                    count++;
                    dfs(grid, i, j, rows, cols);
                }
            }
        }
        return count;
    }

    private void dfs(char[][] grid, int r, int c, int rows, int cols) {
        if (r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] != '1') return;
        grid[r][c] = '0';
        dfs(grid, r - 1, c, rows, cols);
        dfs(grid, r + 1, c, rows, cols);
        dfs(grid, r, c - 1, rows, cols);
        dfs(grid, r, c + 1, rows, cols);
    }
}
```

## Python

```python
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    islands += 1
                    stack = [(i, j)]
                    while stack:
                        x, y = stack.pop()
                        if grid[x][y] != '1':
                            continue
                        grid[x][y] = '0'
                        if x > 0 and grid[x - 1][y] == '1':
                            stack.append((x - 1, y))
                        if x + 1 < rows and grid[x + 1][y] == '1':
                            stack.append((x + 1, y))
                        if y > 0 and grid[x][y - 1] == '1':
                            stack.append((x, y - 1))
                        if y + 1 < cols and grid[x][y + 1] == '1':
                            stack.append((x, y + 1))
        return islands
```

## Python3

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands += 1
                    stack = [(i, j)]
                    while stack:
                        x, y = stack.pop()
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                            grid[x][y] = '0'
                            stack.append((x + 1, y))
                            stack.append((x - 1, y))
                            stack.append((x, y + 1))
                            stack.append((x, y - 1))
        return islands
```

## C

```c
int numIslands(char** grid, int gridSize, int* gridColSize) {
    if (grid == NULL || gridSize == 0) return 0;
    int rows = gridSize;
    int maxCells = 0;
    for (int i = 0; i < rows; ++i) {
        maxCells += gridColSize[i];
    }
    int *stackR = (int *)malloc(maxCells * sizeof(int));
    int *stackC = (int *)malloc(maxCells * sizeof(int));
    int islands = 0;

    for (int r = 0; r < rows; ++r) {
        int cols = gridColSize[r];
        for (int c = 0; c < cols; ++c) {
            if (grid[r][c] == '1') {
                ++islands;
                int top = 0;
                stackR[top] = r;
                stackC[top] = c;
                ++top;
                grid[r][c] = '0';

                while (top > 0) {
                    --top;
                    int cr = stackR[top];
                    int cc = stackC[top];

                    if (cr - 1 >= 0 && grid[cr - 1][cc] == '1') {
                        grid[cr - 1][cc] = '0';
                        stackR[top] = cr - 1;
                        stackC[top] = cc;
                        ++top;
                    }
                    if (cr + 1 < rows && grid[cr + 1][cc] == '1') {
                        grid[cr + 1][cc] = '0';
                        stackR[top] = cr + 1;
                        stackC[top] = cc;
                        ++top;
                    }
                    if (cc - 1 >= 0 && grid[cr][cc - 1] == '1') {
                        grid[cr][cc - 1] = '0';
                        stackR[top] = cr;
                        stackC[top] = cc - 1;
                        ++top;
                    }
                    if (cc + 1 < gridColSize[cr] && grid[cr][cc + 1] == '1') {
                        grid[cr][cc + 1] = '0';
                        stackR[top] = cr;
                        stackC[top] = cc + 1;
                        ++top;
                    }
                }
            }
        }
    }

    free(stackR);
    free(stackC);
    return islands;
}
```

## Csharp

```csharp
public class Solution
{
    public int NumIslands(char[][] grid)
    {
        if (grid == null || grid.Length == 0) return 0;
        int m = grid.Length, n = grid[0].Length;
        int islands = 0;

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (grid[i][j] == '1')
                {
                    islands++;
                    var q = new System.Collections.Generic.Queue<(int, int)>();
                    q.Enqueue((i, j));
                    grid[i][j] = '0';

                    while (q.Count > 0)
                    {
                        var (x, y) = q.Dequeue();

                        if (x > 0 && grid[x - 1][y] == '1')
                        {
                            grid[x - 1][y] = '0';
                            q.Enqueue((x - 1, y));
                        }
                        if (x + 1 < m && grid[x + 1][y] == '1')
                        {
                            grid[x + 1][y] = '0';
                            q.Enqueue((x + 1, y));
                        }
                        if (y > 0 && grid[x][y - 1] == '1')
                        {
                            grid[x][y - 1] = '0';
                            q.Enqueue((x, y - 1));
                        }
                        if (y + 1 < n && grid[x][y + 1] == '1')
                        {
                            grid[x][y + 1] = '0';
                            q.Enqueue((x, y + 1));
                        }
                    }
                }
            }
        }

        return islands;
    }
}
```

## Javascript

```javascript
/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    if (!grid || grid.length === 0) return 0;
    const rows = grid.length;
    const cols = grid[0].length;
    let islands = 0;

    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (grid[r][c] === '1') {
                islands++;
                const stack = [[r, c]];
                while (stack.length) {
                    const [cr, cc] = stack.pop();
                    if (
                        cr < 0 || cr >= rows ||
                        cc < 0 || cc >= cols ||
                        grid[cr][cc] !== '1'
                    ) continue;
                    grid[cr][cc] = '0';
                    stack.push([cr - 1, cc]);
                    stack.push([cr + 1, cc]);
                    stack.push([cr, cc - 1]);
                    stack.push([cr, cc + 1]);
                }
            }
        }
    }

    return islands;
};
```

## Typescript

```typescript
function numIslands(grid: string[][]): number {
    if (!grid || grid.length === 0) return 0;
    const rows = grid.length;
    const cols = grid[0].length;
    let islands = 0;
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]] as const;

    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (grid[r][c] === '1') {
                islands++;
                const stack: [number, number][] = [[r, c]];
                grid[r][c] = '0';
                while (stack.length) {
                    const [cr, cc] = stack.pop()!;
                    for (const [dr, dc] of dirs) {
                        const nr = cr + dr;
                        const nc = cc + dc;
                        if (
                            nr >= 0 && nr < rows &&
                            nc >= 0 && nc < cols &&
                            grid[nr][nc] === '1'
                        ) {
                            stack.push([nr, nc]);
                            grid[nr][nc] = '0';
                        }
                    }
                }
            }
        }
    }

    return islands;
}
```

## Php

```php
class Solution {

    /**
     * @param String[][] $grid
     * @return Integer
     */
    function numIslands($grid) {
        $rows = count($grid);
        if ($rows == 0) {
            return 0;
        }
        $cols = count($grid[0]);
        $count = 0;
        $queue = new SplQueue();

        for ($i = 0; $i < $rows; $i++) {
            for ($j = 0; $j < $cols; $j++) {
                if ($grid[$i][$j] === '1') {
                    $count++;
                    $grid[$i][$j] = '0';
                    $queue->enqueue([$i, $j]);

                    while (!$queue->isEmpty()) {
                        [$r, $c] = $queue->dequeue();

                        if ($r > 0 && $grid[$r - 1][$c] === '1') {
                            $grid[$r - 1][$c] = '0';
                            $queue->enqueue([$r - 1, $c]);
                        }
                        if ($r < $rows - 1 && $grid[$r + 1][$c] === '1') {
                            $grid[$r + 1][$c] = '0';
                            $queue->enqueue([$r + 1, $c]);
                        }
                        if ($c > 0 && $grid[$r][$c - 1] === '1') {
                            $grid[$r][$c - 1] = '0';
                            $queue->enqueue([$r, $c - 1]);
                        }
                        if ($c < $cols - 1 && $grid[$r][$c + 1] === '1') {
                            $grid[$r][$c + 1] = '0';
                            $queue->enqueue([$r, $c + 1]);
                        }
                    }
                }
            }
        }

        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func numIslands(_ grid: [[Character]]) -> Int {
        var grid = grid
        let m = grid.count
        guard m > 0 else { return 0 }
        let n = grid[0].count
        var count = 0
        let dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        for i in 0..<m {
            for j in 0..<n {
                if grid[i][j] == "1" {
                    count += 1
                    var queue: [(Int, Int)] = [(i, j)]
                    var idx = 0
                    grid[i][j] = "0"
                    
                    while idx < queue.count {
                        let (x, y) = queue[idx]
                        idx += 1
                        
                        for d in dirs {
                            let nx = x + d.0
                            let ny = y + d.1
                            if nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] == "1" {
                                grid[nx][ny] = "0"
                                queue.append((nx, ny))
                            }
                        }
                    }
                }
            }
        }
        
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numIslands(grid: Array<CharArray>): Int {
        val rows = grid.size
        if (rows == 0) return 0
        val cols = grid[0].size
        var count = 0
        val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
        for (i in 0 until rows) {
            for (j in 0 until cols) {
                if (grid[i][j] == '1') {
                    count++
                    val stack: ArrayDeque<Pair<Int, Int>> = ArrayDeque()
                    stack.add(Pair(i, j))
                    while (stack.isNotEmpty()) {
                        val (x, y) = stack.removeFirst()
                        if (x !in 0 until rows || y !in 0 until cols || grid[x][y] != '1') continue
                        grid[x][y] = '0'
                        for (d in dirs) {
                            stack.add(Pair(x + d[0], y + d[1]))
                        }
                    }
                }
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int numIslands(List<List<String>> grid) {
    if (grid.isEmpty) return 0;
    int m = grid.length;
    int n = grid[0].length;
    int count = 0;

    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (grid[i][j] == '1') {
          count++;
          var stack = <List<int>>[];
          stack.add([i, j]);
          grid[i][j] = '0';

          while (stack.isNotEmpty) {
            var cell = stack.removeLast();
            int x = cell[0];
            int y = cell[1];

            if (x > 0 && grid[x - 1][y] == '1') {
              grid[x - 1][y] = '0';
              stack.add([x - 1, y]);
            }
            if (x + 1 < m && grid[x + 1][y] == '1') {
              grid[x + 1][y] = '0';
              stack.add([x + 1, y]);
            }
            if (y > 0 && grid[x][y - 1] == '1') {
              grid[x][y - 1] = '0';
              stack.add([x, y - 1]);
            }
            if (y + 1 < n && grid[x][y + 1] == '1') {
              grid[x][y + 1] = '0';
              stack.add([x, y + 1]);
            }
          }
        }
      }
    }

    return count;
  }
}
```

## Golang

```go
func numIslands(grid [][]byte) int {
	if len(grid) == 0 || len(grid[0]) == 0 {
		return 0
	}
	rows, cols := len(grid), len(grid[0])
	islands := 0

	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			if grid[i][j] != '1' {
				continue
			}
			islands++
			stack := [][2]int{{i, j}}
			grid[i][j] = '0'

			for len(stack) > 0 {
				cur := stack[len(stack)-1]
				stack = stack[:len(stack)-1]
				x, y := cur[0], cur[1]

				if x > 0 && grid[x-1][y] == '1' {
					grid[x-1][y] = '0'
					stack = append(stack, [2]int{x - 1, y})
				}
				if x+1 < rows && grid[x+1][y] == '1' {
					grid[x+1][y] = '0'
					stack = append(stack, [2]int{x + 1, y})
				}
				if y > 0 && grid[x][y-1] == '1' {
					grid[x][y-1] = '0'
					stack = append(stack, [2]int{x, y - 1})
				}
				if y+1 < cols && grid[x][y+1] == '1' {
					grid[x][y+1] = '0'
					stack = append(stack, [2]int{x, y + 1})
				}
			}
		}
	}

	return islands
}
```

## Ruby

```ruby
def num_islands(grid)
  return 0 if grid.empty?
  m = grid.size
  n = grid[0].size
  count = 0
  dirs = [[1,0],[-1,0],[0,1],[0,-1]]

  (0...m).each do |i|
    (0...n).each do |j|
      next unless grid[i][j] == '1'
      count += 1
      stack = [[i, j]]
      while !stack.empty?
        x, y = stack.pop
        next unless grid[x][y] == '1'
        grid[x][y] = '0'
        dirs.each do |dx, dy|
          nx = x + dx
          ny = y + dy
          if nx.between?(0, m - 1) && ny.between?(0, n - 1) && grid[nx][ny] == '1'
            stack << [nx, ny]
          end
        end
      end
    end
  end

  count
end
```

## Scala

```scala
object Solution {
    def numIslands(grid: Array[Array[Char]]): Int = {
        if (grid == null || grid.isEmpty) return 0
        val m = grid.length
        val n = grid(0).length
        var count = 0
        val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))
        import java.util.ArrayDeque

        for (i <- 0 until m) {
            for (j <- 0 until n) {
                if (grid(i)(j) == '1') {
                    count += 1
                    val deque = new ArrayDeque[(Int, Int)]()
                    deque.add((i, j))
                    while (!deque.isEmpty) {
                        val (x, y) = deque.poll()
                        if (x >= 0 && x < m && y >= 0 && y < n && grid(x)(y) == '1') {
                            grid(x)(y) = '0'
                            for ((dx, dy) <- dirs) {
                                deque.add((x + dx, y + dy))
                            }
                        }
                    }
                }
            }
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_islands(grid: Vec<Vec<char>>) -> i32 {
        if grid.is_empty() {
            return 0;
        }
        let mut g = grid;
        let m = g.len();
        let n = g[0].len();
        let dirs = [(1i32, 0i32), (-1, 0), (0, 1), (0, -1)];
        let mut count = 0;
        for i in 0..m {
            for j in 0..n {
                if g[i][j] == '1' {
                    count += 1;
                    let mut stack = vec![(i, j)];
                    while let Some((x, y)) = stack.pop() {
                        if g[x][y] != '1' {
                            continue;
                        }
                        g[x][y] = '0';
                        for (dx, dy) in &dirs {
                            let nx = x as i32 + dx;
                            let ny = y as i32 + dy;
                            if nx >= 0 && nx < m as i32 && ny >= 0 && ny < n as i32 {
                                let ux = nx as usize;
                                let uy = ny as usize;
                                if g[ux][uy] == '1' {
                                    stack.push((ux, uy));
                                }
                            }
                        }
                    }
                }
            }
        }
        count as i32
    }
}
```

## Racket

```racket
(define/contract (num-islands grid)
  (-> (listof (listof char?)) exact-integer?)
  (let* ((rows (length grid))
         (cols (if (zero? rows) 0 (length (first grid))))
         (visited (make-vector rows)))
    (for ([i rows])
      (vector-set! visited i (make-vector cols #f)))
    (define (in-bounds? r c)
      (and (>= r 0) (< r rows) (>= c 0) (< c cols)))
    (let ((count 0))
      (for ([r rows])
        (for ([c cols])
          (when (and (char=? (list-ref (list-ref grid r) c) #\1)
                     (not (vector-ref (vector-ref visited r) c)))
            (set! count (+ count 1))
            (let loop ((stack (list (cons r c))))
              (when (pair? stack)
                (define cur (car stack))
                (define rest (cdr stack))
                (define rr (car cur))
                (define cc (cdr cur))
                (if (and (in-bounds? rr cc)
                         (char=? (list-ref (list-ref grid rr) cc) #\1)
                         (not (vector-ref (vector-ref visited rr) cc)))
                    (begin
                      (vector-set! (vector-ref visited rr) cc #t)
                      (loop (append rest
                                    (list (cons (+ rr 1) cc))
                                    (list (cons (- rr 1) cc))
                                    (list (cons rr (+ cc 1)))
                                    (list (cons rr (- cc 1))))))
                    (loop rest)))))))
      count)))
```

## Erlang

```erlang
-spec num_islands(Grid :: [[char()]]) -> integer().
num_islands(Grid) ->
    GridT = list_to_tuple([list_to_tuple(Row) || Row <- Grid]),
    M = tuple_size(GridT),
    N = case M of
            0 -> 0;
            _ -> tuple_size(element(1, GridT))
        end,
    Coords = [{I,J} || I <- lists:seq(0, M-1), J <- lists:seq(0, N-1)],
    {Count,_Vis} = lists:foldl(fun({I,J},{Cnt,Vis}) ->
        case maps:is_key({I,J}, Vis) of
            true -> {Cnt,Vis};
            false ->
                case cell(GridT,I,J) of
                    $1 ->
                        NewVis = bfs([{I,J}], GridT, M, N, Vis),
                        {Cnt+1, NewVis};
                    _ -> {Cnt, Vis}
                end
        end
    end, {0, #{}}, Coords),
    Count.

cell(GridT,I,J) ->
    element(J+1, element(I+1, GridT)).

bfs([], _,_,_,Vis) -> Vis;
bfs([{I,J}|Rest], GridT,M,N,Vis) ->
    case maps:is_key({I,J}, Vis) of
        true ->
            bfs(Rest, GridT,M,N,Vis);
        false ->
            case cell(GridT,I,J) of
                $1 ->
                    Vis1 = maps:put({I,J}, true, Vis),
                    Neigh = neighbors(I,J,M,N),
                    bfs(Rest ++ Neigh, GridT,M,N, Vis1);
                _ ->
                    bfs(Rest, GridT,M,N, Vis)
            end
    end.

neighbors(I,J,M,N) ->
    Up = if I-1 >= 0 -> [{I-1,J}] else [] end,
    Down = if I+1 < M -> [{I+1,J}] else [] end,
    Left = if J-1 >= 0 -> [{I,J-1}] else [] end,
    Right = if J+1 < N -> [{I,J+1}] else [] end,
    Up ++ Down ++ Left ++ Right.
```

## Elixir

```elixir
defmodule Solution do
  @spec num_islands(grid :: [[char]]) :: integer
  def num_islands(grid) do
    rows = length(grid)

    cols =
      if rows == 0 do
        0
      else
        grid |> List.first() |> length()
      end

    {count, _visited} =
      Enum.reduce(0..rows - 1, {0, MapSet.new()}, fn i, {cnt, visited} ->
        Enum.reduce(0..cols - 1, {cnt, visited}, fn j, {c, v} ->
          if cell(grid, i, j) == "1" and not MapSet.member?(v, {i, j}) do
            new_visited = dfs(grid, i, j, rows, cols, v)
            {c + 1, new_visited}
          else
            {c, v}
          end
        end)
      end)

    count
  end

  defp cell(grid, i, j) do
    grid |> Enum.at(i) |> Enum.at(j)
  end

  defp dfs(grid, i, j, rows, cols, visited) do
    cond do
      i < 0 or j < 0 or i >= rows or j >= cols ->
        visited

      cell(grid, i, j) != "1" ->
        visited

      MapSet.member?(visited, {i, j}) ->
        visited

      true ->
        visited = MapSet.put(visited, {i, j})

        visited = dfs(grid, i + 1, j, rows, cols, visited)
        visited = dfs(grid, i - 1, j, rows, cols, visited)
        visited = dfs(grid, i, j + 1, rows, cols, visited)
        visited = dfs(grid, i, j - 1, rows, cols, visited)

        visited
    end
  end
end
```
