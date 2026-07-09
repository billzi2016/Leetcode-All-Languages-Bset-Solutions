# 1210. Minimum Moves to Reach Target with Rotations

## Cpp

```cpp
class Solution {
public:
    int minimumMoves(vector<vector<int>>& grid) {
        int n = grid.size();
        auto freeCell = [&](int x, int y) -> bool {
            return x >= 0 && x < n && y >= 0 && y < n && grid[x][y] == 0;
        };
        vector<vector<array<bool,2>>> vis(n, vector<array<bool,2>>(n, {false,false}));
        queue<array<int,3>> q; // row, col of tail (left/top), orientation 0=horizontal,1=vertical
        q.push({0,0,0});
        vis[0][0][0] = true;
        int steps = 0;
        while (!q.empty()) {
            int sz = q.size();
            while (sz--) {
                auto cur = q.front(); q.pop();
                int x = cur[0], y = cur[1], o = cur[2];
                if (x == n-1 && y == n-2 && o == 0) return steps;
                if (o == 0) { // horizontal
                    // move right
                    if (freeCell(x, y+2) && !vis[x][y+1][0]) {
                        vis[x][y+1][0] = true;
                        q.push({x, y+1, 0});
                    }
                    // move down
                    if (freeCell(x+1, y) && freeCell(x+1, y+1) && !vis[x+1][y][0]) {
                        vis[x+1][y][0] = true;
                        q.push({x+1, y, 0});
                    }
                    // rotate clockwise to vertical
                    if (freeCell(x+1, y) && freeCell(x+1, y+1) && !vis[x][y][1]) {
                        vis[x][y][1] = true;
                        q.push({x, y, 1});
                    }
                } else { // vertical
                    // move down
                    if (freeCell(x+2, y) && !vis[x+1][y][1]) {
                        vis[x+1][y][1] = true;
                        q.push({x+1, y, 1});
                    }
                    // move right
                    if (freeCell(x, y+1) && freeCell(x+1, y+1) && !vis[x][y+1][1]) {
                        vis[x][y+1][1] = true;
                        q.push({x, y+1, 1});
                    }
                    // rotate counterclockwise to horizontal
                    if (freeCell(x, y+1) && freeCell(x+1, y+1) && !vis[x][y][0]) {
                        vis[x][y][0] = true;
                        q.push({x, y, 0});
                    }
                }
            }
            ++steps;
        }
        return -1;
    }
};
```

## Java

```java
class Solution {
    public int minimumMoves(int[][] grid) {
        int n = grid.length;
        boolean[][][] visited = new boolean[n][n][2]; // 0: horizontal, 1: vertical
        java.util.ArrayDeque<int[]> q = new java.util.ArrayDeque<>();
        // start at (0,1) horizontal
        q.offer(new int[]{0, 1, 0, 0});
        visited[0][1][0] = true;
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int x = cur[0], y = cur[1], dir = cur[2], steps = cur[3];
            if (x == n - 1 && y == n - 1 && dir == 0) return steps;
            if (dir == 0) { // horizontal
                // move right
                if (y + 1 < n && grid[x][y + 1] == 0) {
                    if (!visited[x][y + 1][0]) {
                        visited[x][y + 1][0] = true;
                        q.offer(new int[]{x, y + 1, 0, steps + 1});
                    }
                }
                // move down (stay horizontal)
                if (x + 1 < n && grid[x + 1][y] == 0 && grid[x + 1][y - 1] == 0) {
                    if (!visited[x + 1][y][0]) {
                        visited[x + 1][y][0] = true;
                        q.offer(new int[]{x + 1, y, 0, steps + 1});
                    }
                }
                // rotate clockwise to vertical
                if (x + 1 < n && grid[x + 1][y] == 0 && grid[x + 1][y - 1] == 0) {
                    if (!visited[x + 1][y][1]) {
                        visited[x + 1][y][1] = true;
                        q.offer(new int[]{x + 1, y, 1, steps + 1});
                    }
                }
            } else { // vertical
                // move down (stay vertical)
                if (x + 1 < n && grid[x + 1][y] == 0) {
                    if (!visited[x + 1][y][1]) {
                        visited[x + 1][y][1] = true;
                        q.offer(new int[]{x + 1, y, 1, steps + 1});
                    }
                }
                // move right (stay vertical)
                if (y + 1 < n && grid[x][y + 1] == 0 && grid[x - 1][y + 1] == 0) {
                    if (!visited[x][y + 1][1]) {
                        visited[x][y + 1][1] = true;
                        q.offer(new int[]{x, y + 1, 1, steps + 1});
                    }
                }
                // rotate counterclockwise to horizontal
                if (y + 1 < n && grid[x][y + 1] == 0 && grid[x - 1][y + 1] == 0) {
                    if (!visited[x][y + 1][0]) {
                        visited[x][y + 1][0] = true;
                        q.offer(new int[]{x, y + 1, 0, steps + 1});
                    }
                }
            }
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def minimumMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque
        n = len(grid)
        start = (0, 0, 0)          # i, j, orientation (0=horizontal,1=vertical)
        target = (n - 1, n - 2, 0) # bottom‑right horizontal position

        q = deque()
        q.append((0, 0, 0, 0))     # i, j, orient, steps
        visited = {start}

        while q:
            i, j, o, step = q.popleft()
            if (i, j, o) == target:
                return step

            if o == 0:  # horizontal
                # move right
                if j + 2 < n and grid[i][j + 2] == 0:
                    ns = (i, j + 1, 0)
                    if ns not in visited:
                        visited.add(ns)
                        q.append((i, j + 1, 0, step + 1))
                # move down
                if i + 1 < n and grid[i + 1][j] == 0 and grid[i + 1][j + 1] == 0:
                    ns = (i + 1, j, 0)
                    if ns not in visited:
                        visited.add(ns)
                        q.append((i + 1, j, 0, step + 1))
                # rotate clockwise to vertical
                if i + 1 < n and j + 1 < n and grid[i + 1][j] == 0 and grid[i + 1][j + 1] == 0:
                    ns = (i, j, 1)
                    if ns not in visited:
                        visited.add(ns)
                        q.append((i, j, 1, step + 1))
            else:       # vertical
                # move down
                if i + 2 < n and grid[i + 2][j] == 0:
                    ns = (i + 1, j, 1)
                    if ns not in visited:
                        visited.add(ns)
                        q.append((i + 1, j, 1, step + 1))
                # move right
                if j + 1 < n and grid[i][j + 1] == 0 and grid[i + 1][j + 1] == 0:
                    ns = (i, j + 1, 1)
                    if ns not in visited:
                        visited.add(ns)
                        q.append((i, j + 1, 1, step + 1))
                # rotate counter‑clockwise to horizontal
                if i + 1 < n and j + 1 < n and grid[i][j + 1] == 0 and grid[i + 1][j + 1] == 0:
                    ns = (i, j, 0)
                    if ns not in visited:
                        visited.add(ns)
                        q.append((i, j, 0, step + 1))

        return -1
```

## Python3

```python
class Solution:
    def minimumMoves(self, grid):
        from collections import deque
        n = len(grid)
        # orientation 0: horizontal (tail at (i,j), head at (i,j+1))
        # orientation 1: vertical   (tail at (i,j), head at (i+1,j))
        start = (0, 0, 0)
        target = (n - 1, n - 2, 0)
        q = deque()
        q.append((start, 0))
        visited = set([start])
        while q:
            (i, j, o), d = q.popleft()
            if (i, j, o) == target:
                return d
            # horizontal moves
            if o == 0:
                # move right
                if j + 2 < n and grid[i][j + 2] == 0:
                    nxt = (i, j + 1, 0)
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, d + 1))
                # move down
                if i + 1 < n and grid[i + 1][j] == 0 and grid[i + 1][j + 1] == 0:
                    nxt = (i + 1, j, 0)
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, d + 1))
                # rotate clockwise to vertical
                if i + 1 < n and grid[i + 1][j] == 0 and grid[i + 1][j + 1] == 0:
                    nxt = (i, j, 1)
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, d + 1))
            else:  # vertical
                # move down
                if i + 2 < n and grid[i + 2][j] == 0:
                    nxt = (i + 1, j, 1)
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, d + 1))
                # move right
                if j + 1 < n and grid[i][j + 1] == 0 and grid[i + 1][j + 1] == 0:
                    nxt = (i, j + 1, 1)
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, d + 1))
                # rotate counterclockwise to horizontal
                if j + 1 < n and grid[i][j + 1] == 0 and grid[i + 1][j + 1] == 0:
                    nxt = (i, j, 0)
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, d + 1))
        return -1
```

## C

```c
#include <stdlib.h>

typedef struct {
    int x;
    int y;
    int ori;   // 0 = horizontal, 1 = vertical
    int dist;
} Node;

int minimumMoves(int** grid, int gridSize, int* gridColSize) {
    int n = gridSize;
    if (n == 0) return -1;

    /* visited[x][y][ori] */
    char ***visited = (char ***)malloc(n * sizeof(char **));
    for (int i = 0; i < n; ++i) {
        visited[i] = (char **)malloc(n * sizeof(char *));
        for (int j = 0; j < n; ++j) {
            visited[i][j] = (char *)calloc(2, sizeof(char));
        }
    }

    int maxStates = n * n * 2 + 5;
    Node *queue = (Node *)malloc(maxStates * sizeof(Node));
    int head = 0, tail = 0;

    queue[tail++] = (Node){0, 0, 0, 0};
    visited[0][0][0] = 1;

    while (head < tail) {
        Node cur = queue[head++];
        int x = cur.x, y = cur.y, ori = cur.ori, d = cur.dist;

        if (x == n - 1 && y == n - 2 && ori == 0) {
            /* free memory */
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j) free(visited[i][j]);
                free(visited[i]);
            }
            free(visited);
            free(queue);
            return d;
        }

        if (ori == 0) { /* horizontal */
            /* move right */
            if (y + 2 < n && grid[x][y + 2] == 0 && !visited[x][y + 1][0]) {
                visited[x][y + 1][0] = 1;
                queue[tail++] = (Node){x, y + 1, 0, d + 1};
            }
            /* move down */
            if (x + 1 < n && grid[x + 1][y] == 0 && grid[x + 1][y + 1] == 0 && !visited[x + 1][y][0]) {
                visited[x + 1][y][0] = 1;
                queue[tail++] = (Node){x + 1, y, 0, d + 1};
            }
            /* rotate clockwise to vertical */
            if (x + 1 < n && grid[x + 1][y] == 0 && grid[x + 1][y + 1] == 0 && !visited[x][y][1]) {
                visited[x][y][1] = 1;
                queue[tail++] = (Node){x, y, 1, d + 1};
            }
        } else { /* vertical */
            /* move down */
            if (x + 2 < n && grid[x + 2][y] == 0 && !visited[x + 1][y][1]) {
                visited[x + 1][y][1] = 1;
                queue[tail++] = (Node){x + 1, y, 1, d + 1};
            }
            /* move right */
            if (y + 1 < n && grid[x][y + 1] == 0 && grid[x + 1][y + 1] == 0 && !visited[x][y + 1][1]) {
                visited[x][y + 1][1] = 1;
                queue[tail++] = (Node){x, y + 1, 1, d + 1};
            }
            /* rotate counterclockwise to horizontal */
            if (y + 1 < n && grid[x][y + 1] == 0 && grid[x + 1][y + 1] == 0 && !visited[x][y][0]) {
                visited[x][y][0] = 1;
                queue[tail++] = (Node){x, y, 0, d + 1};
            }
        }
    }

    /* free memory */
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) free(visited[i][j]);
        free(visited[i]);
    }
    free(visited);
    free(queue);
    return -1;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumMoves(int[][] grid) {
        int n = grid.Length;
        // orientation: 0 = horizontal, 1 = vertical
        bool[,,] visited = new bool[n, n, 2];
        var queue = new System.Collections.Generic.Queue<int[]>();
        queue.Enqueue(new int[] { 0, 0, 0 }); // x, y, orientation
        visited[0, 0, 0] = true;
        int moves = 0;

        while (queue.Count > 0) {
            int levelSize = queue.Count;
            for (int i = 0; i < levelSize; i++) {
                var cur = queue.Dequeue();
                int x = cur[0], y = cur[1], o = cur[2];

                if (x == n - 1 && y == n - 2 && o == 0) return moves;

                if (o == 0) { // horizontal
                    // move right
                    if (y + 2 < n && grid[x][y + 2] == 0 && !visited[x, y + 1, 0]) {
                        visited[x, y + 1, 0] = true;
                        queue.Enqueue(new int[] { x, y + 1, 0 });
                    }
                    // move down
                    if (x + 1 < n && grid[x + 1][y] == 0 && grid[x + 1][y + 1] == 0 && !visited[x + 1, y, 0]) {
                        visited[x + 1, y, 0] = true;
                        queue.Enqueue(new int[] { x + 1, y, 0 });
                    }
                    // rotate clockwise to vertical
                    if (x + 1 < n && y + 1 < n && grid[x + 1][y] == 0 && grid[x + 1][y + 1] == 0 && !visited[x, y, 1]) {
                        visited[x, y, 1] = true;
                        queue.Enqueue(new int[] { x, y, 1 });
                    }
                } else { // vertical
                    // move down
                    if (x + 2 < n && grid[x + 2][y] == 0 && !visited[x + 1, y, 1]) {
                        visited[x + 1, y, 1] = true;
                        queue.Enqueue(new int[] { x + 1, y, 1 });
                    }
                    // move right
                    if (y + 1 < n && grid[x][y + 1] == 0 && grid[x + 1][y + 1] == 0 && !visited[x, y + 1, 1]) {
                        visited[x, y + 1, 1] = true;
                        queue.Enqueue(new int[] { x, y + 1, 1 });
                    }
                    // rotate counterclockwise to horizontal
                    if (x + 1 < n && y + 1 < n && grid[x][y + 1] == 0 && grid[x + 1][y + 1] == 0 && !visited[x, y, 0]) {
                        visited[x, y, 0] = true;
                        queue.Enqueue(new int[] { x, y, 0 });
                    }
                }
            }
            moves++;
        }

        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minimumMoves = function(grid) {
    const n = grid.length;
    // visited[x][y][0] -> horizontal, [1] -> vertical
    const visited = Array.from({ length: n }, () =>
        Array.from({ length: n }, () => [false, false])
    );
    const queue = [];
    let head = 0;
    // start at (0,0) horizontal
    queue.push([0, 0, 0, 0]); // x, y, orientation(0=h,1=v), distance
    visited[0][0][0] = true;

    while (head < queue.length) {
        const [x, y, ori, d] = queue[head++];
        if (x === n - 1 && y === n - 2 && ori === 0) return d;

        if (ori === 0) { // horizontal
            // move right
            if (y + 2 < n && grid[x][y + 2] === 0 && !visited[x][y + 1][0]) {
                visited[x][y + 1][0] = true;
                queue.push([x, y + 1, 0, d + 1]);
            }
            // move down
            if (x + 1 < n && grid[x + 1][y] === 0 && grid[x + 1][y + 1] === 0 && !visited[x + 1][y][0]) {
                visited[x + 1][y][0] = true;
                queue.push([x + 1, y, 0, d + 1]);
            }
            // rotate clockwise to vertical
            if (x + 1 < n && y + 1 < n && grid[x + 1][y] === 0 && grid[x + 1][y + 1] === 0 && !visited[x][y][1]) {
                visited[x][y][1] = true;
                queue.push([x, y, 1, d + 1]);
            }
        } else { // vertical
            // move down
            if (x + 2 < n && grid[x + 2][y] === 0 && !visited[x + 1][y][1]) {
                visited[x + 1][y][1] = true;
                queue.push([x + 1, y, 1, d + 1]);
            }
            // move right
            if (y + 1 < n && grid[x][y + 1] === 0 && grid[x + 1][y + 1] === 0 && !visited[x][y + 1][1]) {
                visited[x][y + 1][1] = true;
                queue.push([x, y + 1, 1, d + 1]);
            }
            // rotate counterclockwise to horizontal
            if (x + 1 < n && y + 1 < n && grid[x][y + 1] === 0 && grid[x + 1][y + 1] === 0 && !visited[x][y][0]) {
                visited[x][y][0] = true;
                queue.push([x, y, 0, d + 1]);
            }
        }
    }

    return -1;
};
```

## Typescript

```typescript
function minimumMoves(grid: number[][]): number {
    const n = grid.length;
    // visited[x][y][orientation] where orientation 0 = horizontal, 1 = vertical
    const visited: boolean[][][] = Array.from({ length: n }, () =>
        Array.from({ length: n }, () => [false, false])
    );

    type State = [number, number, number, number]; // x, y, orientation, steps
    const queue: State[] = [];
    queue.push([0, 0, 0, 0]); // start at (0,0)-(0,1), horizontal
    visited[0][0][0] = true;

    let head = 0;
    while (head < queue.length) {
        const [x, y, ori, steps] = queue[head++];
        if (x === n - 1 && y === n - 2 && ori === 0) return steps; // reached target

        if (ori === 0) { // horizontal
            // move right
            if (y + 2 < n && grid[x][y + 2] === 0) {
                if (!visited[x][y + 1][0]) {
                    visited[x][y + 1][0] = true;
                    queue.push([x, y + 1, 0, steps + 1]);
                }
            }
            // move down
            if (x + 1 < n && grid[x + 1][y] === 0 && grid[x + 1][y + 1] === 0) {
                if (!visited[x + 1][y][0]) {
                    visited[x + 1][y][0] = true;
                    queue.push([x + 1, y, 0, steps + 1]);
                }
            }
            // rotate clockwise to vertical
            if (x + 1 < n && y + 1 < n && grid[x + 1][y] === 0 && grid[x + 1][y + 1] === 0) {
                if (!visited[x][y + 1][1]) {
                    visited[x][y + 1][1] = true;
                    queue.push([x, y + 1, 1, steps + 1]);
                }
            }
        } else { // vertical
            // move down
            if (x + 2 < n && grid[x + 2][y] === 0) {
                if (!visited[x + 1][y][1]) {
                    visited[x + 1][y][1] = true;
                    queue.push([x + 1, y, 1, steps + 1]);
                }
            }
            // move right
            if (y + 1 < n && grid[x][y + 1] === 0 && grid[x + 1][y + 1] === 0) {
                if (!visited[x][y + 1][1]) {
                    visited[x][y + 1][1] = true;
                    queue.push([x, y + 1, 1, steps + 1]);
                }
            }
            // rotate counterclockwise to horizontal
            if (x + 1 < n && y + 1 < n && grid[x][y + 1] === 0 && grid[x + 1][y + 1] === 0) {
                if (!visited[x + 1][y][0]) {
                    visited[x + 1][y][0] = true;
                    queue.push([x + 1, y, 0, steps + 1]);
                }
            }
        }
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
    function minimumMoves($grid) {
        $n = count($grid);
        // visited[x][y][orientation] where orientation 0=horizontal,1=vertical
        $visited = [];
        for ($i = 0; $i < $n; $i++) {
            $visited[$i] = [];
            for ($j = 0; $j < $n; $j++) {
                $visited[$i][$j] = [false, false];
            }
        }

        $queue = new SplQueue();
        // start at (0,1) horizontal
        $queue->enqueue([0, 1, 0, 0]); // x, y, orientation, steps
        $visited[0][1][0] = true;

        while (!$queue->isEmpty()) {
            [$x, $y, $ori, $steps] = $queue->dequeue();

            if ($x == $n - 1 && $y == $n - 1 && $ori == 0) {
                return $steps;
            }

            if ($ori == 0) { // horizontal
                // move right
                if ($y + 1 < $n && $grid[$x][$y + 1] == 0) {
                    if (!$visited[$x][$y + 1][0]) {
                        $visited[$x][$y + 1][0] = true;
                        $queue->enqueue([$x, $y + 1, 0, $steps + 1]);
                    }
                }
                // move down
                if ($x + 1 < $n && $grid[$x + 1][$y] == 0 && $grid[$x + 1][$y - 1] == 0) {
                    if (!$visited[$x + 1][$y][0]) {
                        $visited[$x + 1][$y][0] = true;
                        $queue->enqueue([$x + 1, $y, 0, $steps + 1]);
                    }
                }
                // rotate clockwise to vertical
                if ($x + 1 < $n && $grid[$x + 1][$y] == 0 && $grid[$x + 1][$y - 1] == 0) {
                    $nx = $x + 1;
                    $ny = $y - 1; // new head (bottom cell)
                    if (!$visited[$nx][$ny][1]) {
                        $visited[$nx][$ny][1] = true;
                        $queue->enqueue([$nx, $ny, 1, $steps + 1]);
                    }
                }
            } else { // vertical
                // move down
                if ($x + 1 < $n && $grid[$x + 1][$y] == 0) {
                    if (!$visited[$x + 1][$y][1]) {
                        $visited[$x + 1][$y][1] = true;
                        $queue->enqueue([$x + 1, $y, 1, $steps + 1]);
                    }
                }
                // move right
                if ($y + 1 < $n && $grid[$x][$y + 1] == 0 && $grid[$x - 1][$y + 1] == 0) {
                    if (!$visited[$x][$y + 1][1]) {
                        $visited[$x][$y + 1][1] = true;
                        $queue->enqueue([$x, $y + 1, 1, $steps + 1]);
                    }
                }
                // rotate counterclockwise to horizontal
                if ($y + 1 < $n && $grid[$x][$y + 1] == 0 && $grid[$x - 1][$y + 1] == 0) {
                    $nx = $x - 1;
                    $ny = $y + 1; // new head (rightmost cell)
                    if (!$visited[$nx][$ny][0]) {
                        $visited[$nx][$ny][0] = true;
                        $queue->enqueue([$nx, $ny, 0, $steps + 1]);
                    }
                }
            }
        }

        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func minimumMoves(_ grid: [[Int]]) -> Int {
        let n = grid.count
        // visited[row][col][orientation] where orientation 0 = horizontal, 1 = vertical
        var visited = Array(repeating: Array(repeating: Array(repeating: false, count: 2), count: n), count: n)
        
        struct Node {
            let r: Int
            let c: Int
            let o: Int   // 0 horizontal, 1 vertical
            let d: Int   // distance (moves)
        }
        
        var queue = [Node]()
        var idx = 0
        
        // start at (0,0)-(0,1) => head at (0,1), horizontal
        visited[0][1][0] = true
        queue.append(Node(r: 0, c: 1, o: 0, d: 0))
        
        while idx < queue.count {
            let cur = queue[idx]
            idx += 1
            
            // check target: head at (n-1,n-1) horizontal
            if cur.r == n - 1 && cur.c == n - 1 && cur.o == 0 {
                return cur.d
            }
            
            if cur.o == 0 { // horizontal
                // move right
                if cur.c + 1 < n && grid[cur.r][cur.c + 1] == 0 {
                    let nr = cur.r, nc = cur.c + 1, no = 0
                    if !visited[nr][nc][no] {
                        visited[nr][nc][no] = true
                        queue.append(Node(r: nr, c: nc, o: no, d: cur.d + 1))
                    }
                }
                // move down (stay horizontal)
                if cur.r + 1 < n && grid[cur.r + 1][cur.c] == 0 && grid[cur.r + 1][cur.c - 1] == 0 {
                    let nr = cur.r + 1, nc = cur.c, no = 0
                    if !visited[nr][nc][no] {
                        visited[nr][nc][no] = true
                        queue.append(Node(r: nr, c: nc, o: no, d: cur.d + 1))
                    }
                }
                // rotate clockwise to vertical
                if cur.r + 1 < n && grid[cur.r + 1][cur.c] == 0 && grid[cur.r + 1][cur.c - 1] == 0 {
                    let nr = cur.r + 1, nc = cur.c, no = 1
                    if !visited[nr][nc][no] {
                        visited[nr][nc][no] = true
                        queue.append(Node(r: nr, c: nc, o: no, d: cur.d + 1))
                    }
                }
            } else { // vertical
                // move down (stay vertical)
                if cur.r + 1 < n && grid[cur.r + 1][cur.c] == 0 {
                    let nr = cur.r + 1, nc = cur.c, no = 1
                    if !visited[nr][nc][no] {
                        visited[nr][nc][no] = true
                        queue.append(Node(r: nr, c: nc, o: no, d: cur.d + 1))
                    }
                }
                // move right (stay vertical)
                if cur.c + 1 < n && grid[cur.r][cur.c + 1] == 0 && grid[cur.r - 1][cur.c + 1] == 0 {
                    let nr = cur.r, nc = cur.c + 1, no = 1
                    if !visited[nr][nc][no] {
                        visited[nr][nc][no] = true
                        queue.append(Node(r: nr, c: nc, o: no, d: cur.d + 1))
                    }
                }
                // rotate counterclockwise to horizontal
                if cur.c - 1 >= 0 && grid[cur.r][cur.c - 1] == 0 && grid[cur.r - 1][cur.c - 1] == 0 {
                    let nr = cur.r, nc = cur.c, no = 0
                    if !visited[nr][nc][no] {
                        visited[nr][nc][no] = true
                        queue.append(Node(r: nr, c: nc, o: no, d: cur.d + 1))
                    }
                }
            }
        }
        
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumMoves(grid: Array<IntArray>): Int {
        val n = grid.size
        // visited[row][col][orientation] where orientation 0 = horizontal, 1 = vertical
        val visited = Array(n) { Array(n) { BooleanArray(2) } }
        data class State(val r: Int, val c: Int, val o: Int)
        val queue: java.util.ArrayDeque<State> = java.util.ArrayDeque()
        queue.add(State(0, 0, 0))
        visited[0][0][0] = true
        var moves = 0
        while (queue.isNotEmpty()) {
            repeat(queue.size) {
                val cur = queue.poll()
                if (cur.r == n - 1 && cur.c == n - 2 && cur.o == 0) return moves
                if (cur.o == 0) { // horizontal
                    // move right
                    if (cur.c + 2 < n && grid[cur.r][cur.c + 2] == 0 && !visited[cur.r][cur.c + 1][0]) {
                        visited[cur.r][cur.c + 1][0] = true
                        queue.add(State(cur.r, cur.c + 1, 0))
                    }
                    // move down
                    if (cur.r + 1 < n &&
                        grid[cur.r + 1][cur.c] == 0 && grid[cur.r + 1][cur.c + 1] == 0 &&
                        !visited[cur.r + 1][cur.c][0]
                    ) {
                        visited[cur.r + 1][cur.c][0] = true
                        queue.add(State(cur.r + 1, cur.c, 0))
                    }
                    // rotate clockwise to vertical
                    if (cur.r + 1 < n &&
                        grid[cur.r + 1][cur.c] == 0 && grid[cur.r + 1][cur.c + 1] == 0 &&
                        !visited[cur.r][cur.c][1]
                    ) {
                        visited[cur.r][cur.c][1] = true
                        queue.add(State(cur.r, cur.c, 1))
                    }
                } else { // vertical
                    // move down
                    if (cur.r + 2 < n && grid[cur.r + 2][cur.c] == 0 && !visited[cur.r + 1][cur.c][1]) {
                        visited[cur.r + 1][cur.c][1] = true
                        queue.add(State(cur.r + 1, cur.c, 1))
                    }
                    // move right
                    if (cur.c + 1 < n &&
                        grid[cur.r][cur.c + 1] == 0 && grid[cur.r + 1][cur.c + 1] == 0 &&
                        !visited[cur.r][cur.c + 1][1]
                    ) {
                        visited[cur.r][cur.c + 1][1] = true
                        queue.add(State(cur.r, cur.c + 1, 1))
                    }
                    // rotate counterclockwise to horizontal
                    if (cur.c + 1 < n &&
                        grid[cur.r][cur.c + 1] == 0 && grid[cur.r + 1][cur.c + 1] == 0 &&
                        !visited[cur.r][cur.c][0]
                    ) {
                        visited[cur.r][cur.c][0] = true
                        queue.add(State(cur.r, cur.c, 0))
                    }
                }
            }
            moves++
        }
        return -1
    }
}
```

## Golang

```go
func minimumMoves(grid [][]int) int {
    n := len(grid)
    type node struct {
        x, y, dir, steps int
    }
    visited := make([][][]bool, n)
    for i := 0; i < n; i++ {
        visited[i] = make([][]bool, n)
        for j := 0; j < n; j++ {
            visited[i][j] = make([]bool, 2)
        }
    }
    q := []node{{0, 0, 0, 0}}
    visited[0][0][0] = true

    for len(q) > 0 {
        cur := q[0]
        q = q[1:]
        x, y, d, s := cur.x, cur.y, cur.dir, cur.steps
        if x == n-1 && y == n-2 && d == 0 {
            return s
        }
        if d == 0 { // horizontal
            // move right
            if y+2 < n && grid[x][y+2] == 0 && !visited[x][y+1][0] {
                visited[x][y+1][0] = true
                q = append(q, node{x, y + 1, 0, s + 1})
            }
            // move down
            if x+1 < n && grid[x+1][y] == 0 && grid[x+1][y+1] == 0 && !visited[x+1][y][0] {
                visited[x+1][y][0] = true
                q = append(q, node{x + 1, y, 0, s + 1})
            }
            // rotate clockwise to vertical
            if x+1 < n && y+1 < n && grid[x+1][y] == 0 && grid[x+1][y+1] == 0 && !visited[x][y+1][1] {
                visited[x][y+1][1] = true
                q = append(q, node{x, y + 1, 1, s + 1})
            }
        } else { // vertical
            // move down
            if x+2 < n && grid[x+2][y] == 0 && !visited[x+1][y][1] {
                visited[x+1][y][1] = true
                q = append(q, node{x + 1, y, 1, s + 1})
            }
            // move right
            if y+1 < n && grid[x][y+1] == 0 && grid[x+1][y+1] == 0 && !visited[x][y+1][1] {
                visited[x][y+1][1] = true
                q = append(q, node{x, y + 1, 1, s + 1})
            }
            // rotate counterclockwise to horizontal
            if x+1 < n && y+1 < n && grid[x][y+1] == 0 && grid[x+1][y+1] == 0 && !visited[x+1][y][0] {
                visited[x+1][y][0] = true
                q = append(q, node{x + 1, y, 0, s + 1})
            }
        }
    }
    return -1
}
```

## Ruby

```ruby
def minimum_moves(grid)
  n = grid.size
  # visited[i][j][orientation] where orientation: 0 = horizontal, 1 = vertical
  visited = Array.new(n) { Array.new(n) { [false, false] } }

  queue = []
  head_i = 0
  head_j = 1
  ori = 0 # start horizontal
  queue << [head_i, head_j, ori, 0]
  visited[head_i][head_j][ori] = true

  idx = 0
  while idx < queue.length
    i, j, o, steps = queue[idx]
    idx += 1

    return steps if i == n - 1 && j == n - 1 && o == 0

    if o == 0 # horizontal
      # move right
      if j + 1 < n && grid[i][j + 1] == 0 && !visited[i][j + 1][0]
        visited[i][j + 1][0] = true
        queue << [i, j + 1, 0, steps + 1]
      end

      # move down
      if i + 1 < n && j - 1 >= 0 && grid[i + 1][j] == 0 && grid[i + 1][j - 1] == 0 && !visited[i + 1][j][0]
        visited[i + 1][j][0] = true
        queue << [i + 1, j, 0, steps + 1]
      end

      # rotate clockwise to vertical
      if i + 1 < n && j - 1 >= 0 && grid[i + 1][j] == 0 && grid[i + 1][j - 1] == 0 && !visited[i + 1][j - 1][1]
        visited[i + 1][j - 1][1] = true
        queue << [i + 1, j - 1, 1, steps + 1]
      end
    else # vertical
      # move down
      if i + 1 < n && grid[i + 1][j] == 0 && !visited[i + 1][j][1]
        visited[i + 1][j][1] = true
        queue << [i + 1, j, 1, steps + 1]
      end

      # move right
      if j + 1 < n && i - 1 >= 0 && grid[i][j + 1] == 0 && grid[i - 1][j + 1] == 0 && !visited[i][j + 1][1]
        visited[i][j + 1][1] = true
        queue << [i, j + 1, 1, steps + 1]
      end

      # rotate counterclockwise to horizontal
      if i - 1 >= 0 && j + 1 < n && grid[i - 1][j + 1] == 0 && grid[i][j + 1] == 0 && !visited[i - 1][j + 1][0]
        visited[i - 1][j + 1][0] = true
        queue << [i - 1, j + 1, 0, steps + 1]
      end
    end
  end

  -1
end
```

## Scala

```scala
object Solution {
    def minimumMoves(grid: Array[Array[Int]]): Int = {
        val n = grid.length
        // orientation: 0 = horizontal, 1 = vertical
        val visited = Array.ofDim[Boolean](n, n, 2)
        val deque = new java.util.ArrayDeque[(Int, Int, Int, Int)]()
        // start at (0,0) horizontal
        deque.add((0, 0, 0, 0))
        visited(0)(0)(0) = true

        while (!deque.isEmpty) {
            val (x, y, ori, dist) = deque.poll()
            if (x == n - 1 && y == n - 2 && ori == 0) return dist

            if (ori == 0) { // horizontal
                // move right
                if (y + 2 < n && grid(x)(y + 2) == 0 && !visited(x)(y + 1)(0)) {
                    visited(x)(y + 1)(0) = true
                    deque.add((x, y + 1, 0, dist + 1))
                }
                // move down
                if (x + 1 < n && grid(x + 1)(y) == 0 && grid(x + 1)(y + 1) == 0 && !visited(x + 1)(y)(0)) {
                    visited(x + 1)(y)(0) = true
                    deque.add((x + 1, y, 0, dist + 1))
                }
                // rotate clockwise to vertical
                if (x + 1 < n && grid(x + 1)(y) == 0 && grid(x + 1)(y + 1) == 0 && !visited(x)(y + 1)(1)) {
                    visited(x)(y + 1)(1) = true
                    deque.add((x, y + 1, 1, dist + 1))
                }
            } else { // vertical
                // move down
                if (x + 2 < n && grid(x + 2)(y) == 0 && !visited(x + 1)(y)(1)) {
                    visited(x + 1)(y)(1) = true
                    deque.add((x + 1, y, 1, dist + 1))
                }
                // move right
                if (y + 1 < n && grid(x)(y + 1) == 0 && grid(x + 1)(y + 1) == 0 && !visited(x)(y + 1)(1)) {
                    visited(x)(y + 1)(1) = true
                    deque.add((x, y + 1, 1, dist + 1))
                }
                // rotate counterclockwise to horizontal
                if (y + 1 < n && grid(x)(y + 1) == 0 && grid(x + 1)(y + 1) == 0 && !visited(x)(y)(0)) {
                    visited(x)(y)(0) = true
                    deque.add((x, y, 0, dist + 1))
                }
            }
        }

        -1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_moves(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        if n == 0 {
            return -1;
        }
        // visited[i][j][ori] where (i,j) is the head cell, ori: 0=horiz,1=vert
        let mut visited = vec![vec![[false; 2]; n]; n];
        use std::collections::VecDeque;
        let mut q: VecDeque<(usize, usize, usize, i32)> = VecDeque::new();
        // start at (0,1) horizontal
        visited[0][1][0] = true;
        q.push_back((0, 1, 0, 0));
        while let Some((i, j, ori, dist)) = q.pop_front() {
            if i == n - 1 && j == n - 1 && ori == 0 {
                return dist;
            }
            if ori == 0 {
                // horizontal
                // move right
                if j + 1 < n && grid[i][j + 1] == 0 && !visited[i][j + 1][0] {
                    visited[i][j + 1][0] = true;
                    q.push_back((i, j + 1, 0, dist + 1));
                }
                // move down
                if i + 1 < n && grid[i + 1][j] == 0 && grid[i + 1][j - 1] == 0 && !visited[i + 1][j][0] {
                    visited[i + 1][j][0] = true;
                    q.push_back((i + 1, j, 0, dist + 1));
                }
                // rotate clockwise to vertical
                if i + 1 < n && grid[i + 1][j] == 0 && grid[i + 1][j - 1] == 0 {
                    let ni = i + 1;
                    let nj = j - 1; // new head (bottom cell)
                    if !visited[ni][nj][1] {
                        visited[ni][nj][1] = true;
                        q.push_back((ni, nj, 1, dist + 1));
                    }
                }
            } else {
                // vertical
                // move down
                if i + 1 < n && grid[i + 1][j] == 0 && !visited[i + 1][j][1] {
                    visited[i + 1][j][1] = true;
                    q.push_back((i + 1, j, 1, dist + 1));
                }
                // move right
                if j + 1 < n && grid[i][j + 1] == 0 && grid[i - 1][j + 1] == 0 && !visited[i][j + 1][1] {
                    visited[i][j + 1][1] = true;
                    q.push_back((i, j + 1, 1, dist + 1));
                }
                // rotate counterclockwise to horizontal
                if j + 1 < n && grid[i][j + 1] == 0 && grid[i - 1][j + 1] == 0 {
                    let ni = i;
                    let nj = j + 1; // new head (right cell)
                    if !visited[ni][nj][0] {
                        visited[ni][nj][0] = true;
                        q.push_back((ni, nj, 0, dist + 1));
                    }
                }
            }
        }
        -1
    }
}
```
