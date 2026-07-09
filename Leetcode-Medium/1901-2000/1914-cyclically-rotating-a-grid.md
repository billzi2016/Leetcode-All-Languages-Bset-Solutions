# 1914. Cyclically Rotating a Grid

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> rotateGrid(vector<vector<int>>& grid, int k) {
        int m = grid.size();
        int n = grid[0].size();
        int layers = min(m, n) / 2;
        for (int layer = 0; layer < layers; ++layer) {
            vector<int> vals;
            // top row
            for (int j = layer; j < n - layer; ++j)
                vals.push_back(grid[layer][j]);
            // right column
            for (int i = layer + 1; i < m - layer - 1; ++i)
                vals.push_back(grid[i][n - layer - 1]);
            // bottom row
            for (int j = n - layer - 1; j >= layer; --j)
                vals.push_back(grid[m - layer - 1][j]);
            // left column
            for (int i = m - layer - 2; i > layer; --i)
                vals.push_back(grid[i][layer]);

            int sz = vals.size();
            int rot = k % sz;
            vector<int> rotated(sz);
            for (int i = 0; i < sz; ++i) {
                rotated[i] = vals[(i + rot) % sz];
            }

            int idx = 0;
            // write back top row
            for (int j = layer; j < n - layer; ++j)
                grid[layer][j] = rotated[idx++];
            // right column
            for (int i = layer + 1; i < m - layer - 1; ++i)
                grid[i][n - layer - 1] = rotated[idx++];
            // bottom row
            for (int j = n - layer - 1; j >= layer; --j)
                grid[m - layer - 1][j] = rotated[idx++];
            // left column
            for (int i = m - layer - 2; i > layer; --i)
                grid[i][layer] = rotated[idx++];
        }
        return grid;
    }
};
```

## Java

```java
class Solution {
    public int[][] rotateGrid(int[][] grid, int k) {
        int m = grid.length;
        int n = grid[0].length;
        int layers = Math.min(m, n) / 2;

        for (int layer = 0; layer < layers; ++layer) {
            int top = layer;
            int left = layer;
            int bottom = m - 1 - layer;
            int right = n - 1 - layer;

            // Collect elements of the current layer in clockwise order
            java.util.List<Integer> vals = new java.util.ArrayList<>();

            for (int j = left; j <= right; ++j) {
                vals.add(grid[top][j]);
            }
            for (int i = top + 1; i < bottom; ++i) {
                vals.add(grid[i][right]);
            }
            if (bottom > top) {
                for (int j = right; j >= left; --j) {
                    vals.add(grid[bottom][j]);
                }
            }
            if (left < right) {
                for (int i = bottom - 1; i > top; --i) {
                    vals.add(grid[i][left]);
                }
            }

            int len = vals.size();
            int rot = k % len; // left rotation amount

            // Write rotated values back to the grid
            int idx = 0;
            for (int j = left; j <= right; ++j) {
                grid[top][j] = vals.get((idx + rot) % len);
                idx++;
            }
            for (int i = top + 1; i < bottom; ++i) {
                grid[i][right] = vals.get((idx + rot) % len);
                idx++;
            }
            if (bottom > top) {
                for (int j = right; j >= left; --j) {
                    grid[bottom][j] = vals.get((idx + rot) % len);
                    idx++;
                }
            }
            if (left < right) {
                for (int i = bottom - 1; i > top; --i) {
                    grid[i][left] = vals.get((idx + rot) % len);
                    idx++;
                }
            }
        }

        return grid;
    }
}
```

## Python

```python
class Solution(object):
    def rotateGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2

        for layer in range(layers):
            top, left = layer, layer
            bottom, right = m - 1 - layer, n - 1 - layer

            # extract elements of the current layer
            vals = []
            # top row
            for col in range(left, right + 1):
                vals.append(grid[top][col])
            # right column (excluding corners)
            for row in range(top + 1, bottom):
                vals.append(grid[row][right])
            # bottom row (if different from top)
            if bottom > top:
                for col in range(right, left - 1, -1):
                    vals.append(grid[bottom][col])
            # left column (excluding corners)
            for row in range(bottom - 1, top, -1):
                vals.append(grid[row][left])

            L = len(vals)
            rot = k % L
            if rot:
                vals = vals[rot:] + vals[:rot]

            # write back rotated values
            idx = 0
            for col in range(left, right + 1):
                grid[top][col] = vals[idx]; idx += 1
            for row in range(top + 1, bottom):
                grid[row][right] = vals[idx]; idx += 1
            if bottom > top:
                for col in range(right, left - 1, -1):
                    grid[bottom][col] = vals[idx]; idx += 1
            for row in range(bottom - 1, top, -1):
                grid[row][left] = vals[idx]; idx += 1

        return grid
```

## Python3

```python
from typing import List

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2
        for layer in range(layers):
            top, left = layer, layer
            bottom, right = m - 1 - layer, n - 1 - layer

            # extract elements of the current layer
            elems = []
            # top row
            for col in range(left, right + 1):
                elems.append(grid[top][col])
            # right column (excluding corners)
            for row in range(top + 1, bottom):
                elems.append(grid[row][right])
            # bottom row (if different from top)
            if bottom > top:
                for col in range(right, left - 1, -1):
                    elems.append(grid[bottom][col])
            # left column (excluding corners)
            for row in range(bottom - 1, top, -1):
                elems.append(grid[row][left])

            L = len(elems)
            rot = k % L
            if rot:
                rotated = elems[rot:] + elems[:rot]
            else:
                rotated = elems

            # write back rotated elements
            idx = 0
            for col in range(left, right + 1):
                grid[top][col] = rotated[idx]; idx += 1
            for row in range(top + 1, bottom):
                grid[row][right] = rotated[idx]; idx += 1
            if bottom > top:
                for col in range(right, left - 1, -1):
                    grid[bottom][col] = rotated[idx]; idx += 1
            for row in range(bottom - 1, top, -1):
                grid[row][left] = rotated[idx]; idx += 1

        return grid
```

## C

```c
#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** rotateGrid(int** grid, int gridSize, int* gridColSize, int k, int* returnSize, int*** returnColumnSizes){
    int m = gridSize;
    int n = gridColSize[0];
    
    *returnSize = m;
    *returnColumnSizes = (int**)malloc(m * sizeof(int*));
    for (int i = 0; i < m; ++i) {
        (*returnColumnSizes)[i] = (int*)malloc(sizeof(int));
        (*returnColumnSizes)[i][0] = n;
    }
    
    int** res = (int**)malloc(m * sizeof(int*));
    for (int i = 0; i < m; ++i) {
        res[i] = (int*)malloc(n * sizeof(int));
    }
    
    int layers = (m < n ? m : n) / 2;
    for (int l = 0; l < layers; ++l) {
        int top = l, bottom = m - l - 1;
        int left = l, right = n - l - 1;
        
        int len = 2 * (bottom - top + right - left);
        if (len == 0) continue;
        int* arr = (int*)malloc(len * sizeof(int));
        int idx = 0;
        
        for (int c = left; c <= right; ++c) arr[idx++] = grid[top][c];
        for (int r = top + 1; r < bottom; ++r) arr[idx++] = grid[r][right];
        if (bottom > top) {
            for (int c = right; c >= left; --c) arr[idx++] = grid[bottom][c];
        }
        for (int r = bottom - 1; r > top; --r) arr[idx++] = grid[r][left];
        
        int shift = k % len;
        idx = 0;
        for (int c = left; c <= right; ++c) {
            res[top][c] = arr[(idx + shift) % len];
            ++idx;
        }
        for (int r = top + 1; r < bottom; ++r) {
            res[r][right] = arr[(idx + shift) % len];
            ++idx;
        }
        if (bottom > top) {
            for (int c = right; c >= left; --c) {
                res[bottom][c] = arr[(idx + shift) % len];
                ++idx;
            }
        }
        for (int r = bottom - 1; r > top; --r) {
            res[r][left] = arr[(idx + shift) % len];
            ++idx;
        }
        
        free(arr);
    }
    
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public int[][] RotateGrid(int[][] grid, int k) {
        int m = grid.Length;
        int n = grid[0].Length;
        int layers = Math.Min(m, n) / 2;

        for (int layer = 0; layer < layers; ++layer) {
            var vals = new System.Collections.Generic.List<int>();

            // top row
            for (int j = layer; j <= n - 1 - layer; ++j)
                vals.Add(grid[layer][j]);

            // right column (excluding corners)
            for (int i = layer + 1; i <= m - 2 - layer; ++i)
                vals.Add(grid[i][n - 1 - layer]);

            // bottom row
            if (m - 1 - layer != layer) {
                for (int j = n - 1 - layer; j >= layer; --j)
                    vals.Add(grid[m - 1 - layer][j]);
            }

            // left column (excluding corners)
            if (n - 1 - layer != layer) {
                for (int i = m - 2 - layer; i > layer; --i)
                    vals.Add(grid[i][layer]);
            }

            int len = vals.Count;
            int r = k % len;
            if (r != 0) {
                var rotated = new System.Collections.Generic.List<int>(len);
                for (int i = 0; i < len; ++i)
                    rotated.Add(vals[(i + r) % len]);
                vals = rotated;
            }

            int idx = 0;

            // write back top row
            for (int j = layer; j <= n - 1 - layer; ++j)
                grid[layer][j] = vals[idx++];

            // right column
            for (int i = layer + 1; i <= m - 2 - layer; ++i)
                grid[i][n - 1 - layer] = vals[idx++];

            // bottom row
            if (m - 1 - layer != layer) {
                for (int j = n - 1 - layer; j >= layer; --j)
                    grid[m - 1 - layer][j] = vals[idx++];
            }

            // left column
            if (n - 1 - layer != layer) {
                for (int i = m - 2 - layer; i > layer; --i)
                    grid[i][layer] = vals[idx++];
            }
        }

        return grid;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number[][]}
 */
var rotateGrid = function(grid, k) {
    const m = grid.length;
    const n = grid[0].length;
    const layers = Math.min(m, n) >> 1; // number of concentric layers

    for (let layer = 0; layer < layers; ++layer) {
        const top = layer, bottom = m - 1 - layer;
        const left = layer, right = n - 1 - layer;

        const elems = [];

        // top row
        for (let j = left; j <= right; ++j) elems.push(grid[top][j]);
        // right column (excluding corners)
        for (let i = top + 1; i <= bottom - 1; ++i) elems.push(grid[i][right]);
        // bottom row
        if (bottom > top) {
            for (let j = right; j >= left; --j) elems.push(grid[bottom][j]);
        }
        // left column (excluding corners)
        if (right > left) {
            for (let i = bottom - 1; i >= top + 1; --i) elems.push(grid[i][left]);
        }

        const len = elems.length;
        const rot = k % len;
        if (rot === 0) continue;

        // rotate counter‑clockwise by shifting left
        const rotated = elems.slice(rot).concat(elems.slice(0, rot));

        let idx = 0;
        // write back top row
        for (let j = left; j <= right; ++j) grid[top][j] = rotated[idx++];
        // right column
        for (let i = top + 1; i <= bottom - 1; ++i) grid[i][right] = rotated[idx++];
        // bottom row
        if (bottom > top) {
            for (let j = right; j >= left; --j) grid[bottom][j] = rotated[idx++];
        }
        // left column
        if (right > left) {
            for (let i = bottom - 1; i >= top + 1; --i) grid[i][left] = rotated[idx++];
        }
    }

    return grid;
};
```

## Typescript

```typescript
function rotateGrid(grid: number[][], k: number): number[][] {
    const m = grid.length;
    const n = grid[0].length;
    const res = grid.map(row => row.slice());
    const layers = Math.min(m, n) >> 1; // divide by 2

    for (let layer = 0; layer < layers; ++layer) {
        const top = layer, bottom = m - 1 - layer;
        const left = layer, right = n - 1 - layer;

        const positions: [number, number][] = [];

        // top row
        for (let col = left; col <= right; ++col) positions.push([top, col]);
        // right column
        for (let row = top + 1; row < bottom; ++row) positions.push([row, right]);
        // bottom row
        for (let col = right; col >= left; --col) positions.push([bottom, col]);
        // left column
        for (let row = bottom - 1; row > top; --row) positions.push([row, left]);

        const len = positions.length;
        const shift = k % len;
        if (shift === 0) continue;

        const vals = positions.map(p => grid[p[0]][p[1]]);
        for (let i = 0; i < len; ++i) {
            const [r, c] = positions[i];
            res[r][c] = vals[(i + shift) % len];
        }
    }

    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @param Integer $k
     * @return Integer[][]
     */
    function rotateGrid($grid, $k) {
        $m = count($grid);
        $n = count($grid[0]);
        $layers = intdiv(min($m, $n), 2);

        for ($layer = 0; $layer < $layers; $layer++) {
            $top = $layer;
            $bottom = $m - 1 - $layer;
            $left = $layer;
            $right = $n - 1 - $layer;

            $vals = [];

            // top row
            for ($c = $left; $c <= $right; $c++) {
                $vals[] = $grid[$top][$c];
            }
            // right column
            for ($r = $top + 1; $r <= $bottom - 1; $r++) {
                $vals[] = $grid[$r][$right];
            }
            // bottom row
            for ($c = $right; $c >= $left; $c--) {
                $vals[] = $grid[$bottom][$c];
            }
            // left column
            for ($r = $bottom - 1; $r >= $top + 1; $r--) {
                $vals[] = $grid[$r][$left];
            }

            $len = count($vals);
            if ($len == 0) continue;
            $rot = $k % $len;
            if ($rot != 0) {
                $rotated = array_merge(array_slice($vals, $rot), array_slice($vals, 0, $rot));
            } else {
                $rotated = $vals;
            }

            $idx = 0;
            // write back top row
            for ($c = $left; $c <= $right; $c++) {
                $grid[$top][$c] = $rotated[$idx++];
            }
            // right column
            for ($r = $top + 1; $r <= $bottom - 1; $r++) {
                $grid[$r][$right] = $rotated[$idx++];
            }
            // bottom row
            for ($c = $right; $c >= $left; $c--) {
                $grid[$bottom][$c] = $rotated[$idx++];
            }
            // left column
            for ($r = $bottom - 1; $r >= $top + 1; $r--) {
                $grid[$r][$left] = $rotated[$idx++];
            }
        }

        return $grid;
    }
}
```

## Swift

```swift
class Solution {
    func rotateGrid(_ grid: [[Int]], _ k: Int) -> [[Int]] {
        let m = grid.count
        let n = grid[0].count
        var result = grid
        let layers = min(m, n) / 2
        
        for layer in 0..<layers {
            let top = layer
            let bottom = m - 1 - layer
            let left = layer
            let right = n - 1 - layer
            
            var positions: [(Int, Int)] = []
            
            // top row
            for col in left...right {
                positions.append((top, col))
            }
            // right column (excluding corners)
            if top + 1 <= bottom - 1 {
                for row in (top + 1)...(bottom - 1) {
                    positions.append((row, right))
                }
            }
            // bottom row
            for col in stride(from: right, through: left, by: -1) {
                positions.append((bottom, col))
            }
            // left column (excluding corners)
            if top + 1 <= bottom - 1 {
                for row in stride(from: bottom - 1, through: top + 1, by: -1) {
                    positions.append((row, left))
                }
            }
            
            let len = positions.count
            var values: [Int] = []
            values.reserveCapacity(len)
            for (i, j) in positions {
                values.append(grid[i][j])
            }
            
            let shift = k % len
            if shift != 0 {
                for idx in 0..<len {
                    let (i, j) = positions[idx]
                    result[i][j] = values[(idx + shift) % len]
                }
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun rotateGrid(grid: Array<IntArray>, k: Int): Array<IntArray> {
        val m = grid.size
        val n = grid[0].size
        val layers = minOf(m, n) / 2

        for (layer in 0 until layers) {
            val top = layer
            val left = layer
            val bottom = m - 1 - layer
            val right = n - 1 - layer

            // Extract elements of the current layer in clockwise order
            val elems = mutableListOf<Int>()
            for (j in left..right) elems.add(grid[top][j])
            for (i in top + 1 until bottom) elems.add(grid[i][right])
            for (j in right downTo left) elems.add(grid[bottom][j])
            for (i in bottom - 1 downTo top + 1) elems.add(grid[i][left])

            val len = elems.size
            val rot = k % len
            if (rot != 0) {
                // Rotate left by rot positions (counter‑clockwise rotation)
                val rotated = IntArray(len)
                for (i in 0 until len) {
                    rotated[i] = elems[(i + rot) % len]
                }

                var idx = 0
                for (j in left..right) grid[top][j] = rotated[idx++]
                for (i in top + 1 until bottom) grid[i][right] = rotated[idx++]
                for (j in right downTo left) grid[bottom][j] = rotated[idx++]
                for (i in bottom - 1 downTo top + 1) grid[i][left] = rotated[idx++]
            }
        }

        return grid
    }
}
```

## Golang

```go
func rotateGrid(grid [][]int, k int) [][]int {
	m := len(grid)
	n := len(grid[0])
	layers := m
	if n < layers {
		layers = n
	}
	layers /= 2

	for layer := 0; layer < layers; layer++ {
		top, bottom := layer, m-1-layer
		left, right := layer, n-1-layer

		var vals []int
		// top row
		for col := left; col <= right; col++ {
			vals = append(vals, grid[top][col])
		}
		// right column (excluding corners)
		for row := top + 1; row <= bottom-1; row++ {
			vals = append(vals, grid[row][right])
		}
		// bottom row
		for col := right; col >= left; col-- {
			vals = append(vals, grid[bottom][col])
		}
		// left column (excluding corners)
		for row := bottom - 1; row >= top+1; row-- {
			vals = append(vals, grid[row][left])
		}

		l := len(vals)
		if l == 0 {
			continue
		}
		rot := k % l

		newVals := make([]int, l)
		for i := 0; i < l; i++ {
			newVals[i] = vals[(i+rot)%l]
		}

		idx := 0
		// write back top row
		for col := left; col <= right; col++ {
			grid[top][col] = newVals[idx]
			idx++
		}
		// right column
		for row := top + 1; row <= bottom-1; row++ {
			grid[row][right] = newVals[idx]
			idx++
		}
		// bottom row
		for col := right; col >= left; col-- {
			grid[bottom][col] = newVals[idx]
			idx++
		}
		// left column
		for row := bottom - 1; row >= top+1; row-- {
			grid[row][left] = newVals[idx]
			idx++
		}
	}
	return grid
}
```

## Ruby

```ruby
def rotate_grid(grid, k)
  m = grid.length
  n = grid[0].length
  layers = [m, n].min / 2

  (0...layers).each do |layer|
    top = layer
    left = layer
    bottom = m - 1 - layer
    right = n - 1 - layer

    elems = []
    (left..right).each { |j| elems << grid[top][j] }
    ((top + 1)...bottom).each { |i| elems << grid[i][right] }
    right.downto(left) { |j| elems << grid[bottom][j] }
    (bottom - 1).downto(top + 1) { |i| elems << grid[i][left] }

    len = elems.length
    rot = k % len
    next if rot == 0

    rotated = elems[rot..-1] + elems[0...rot]

    idx = 0
    (left..right).each { |j| grid[top][j] = rotated[idx]; idx += 1 }
    ((top + 1)...bottom).each { |i| grid[i][right] = rotated[idx]; idx += 1 }
    right.downto(left) { |j| grid[bottom][j] = rotated[idx]; idx += 1 }
    (bottom - 1).downto(top + 1) { |i| grid[i][left] = rotated[idx]; idx += 1 }
  end

  grid
end
```

## Scala

```scala
object Solution {
    def rotateGrid(grid: Array[Array[Int]], k: Int): Array[Array[Int]] = {
        val m = grid.length
        val n = grid(0).length
        val layers = Math.min(m, n) / 2

        for (layer <- 0 until layers) {
            val top = layer
            val bottom = m - 1 - layer
            val left = layer
            val right = n - 1 - layer

            val elems = scala.collection.mutable.ArrayBuffer[Int]()

            // top row
            for (c <- left to right) elems += grid(top)(c)
            // right column
            for (r <- top + 1 until bottom) elems += grid(r)(right)
            // bottom row
            if (bottom > top) {
                for (c <- right to left by -1) elems += grid(bottom)(c)
            }
            // left column
            if (left < right) {
                for (r <- bottom - 1 to top + 1 by -1) elems += grid(r)(left)
            }

            val len = elems.length
            val rot = k % len
            if (rot != 0) {
                val rotated = new Array[Int](len)
                for (i <- 0 until len) {
                    rotated(i) = elems((i + rot) % len)
                }

                var idx = 0
                // top row
                for (c <- left to right) { grid(top)(c) = rotated(idx); idx += 1 }
                // right column
                for (r <- top + 1 until bottom) { grid(r)(right) = rotated(idx); idx += 1 }
                // bottom row
                if (bottom > top) {
                    for (c <- right to left by -1) { grid(bottom)(c) = rotated(idx); idx += 1 }
                }
                // left column
                if (left < right) {
                    for (r <- bottom - 1 to top + 1 by -1) { grid(r)(left) = rotated(idx); idx += 1 }
                }
            }
        }

        grid
    }
}
```

## Rust

```rust
impl Solution {
    pub fn rotate_grid(grid: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        let m = grid.len();
        let n = grid[0].len();
        let mut res = grid.clone();

        let layers = std::cmp::min(m, n) / 2;
        for layer in 0..layers {
            let top = layer;
            let left = layer;
            let bottom = m - 1 - layer;
            let right = n - 1 - layer;

            // collect positions of the current layer in clockwise order
            let mut pos: Vec<(usize, usize)> = Vec::new();

            // top row (left -> right)
            for col in left..=right {
                pos.push((top, col));
            }
            // right column (top+1 -> bottom-1)
            for row in (top + 1)..bottom {
                pos.push((row, right));
            }
            // bottom row (right -> left)
            if bottom > top {
                for col in (left..=right).rev() {
                    pos.push((bottom, col));
                }
            }
            // left column (bottom-1 -> top+1)
            if right > left {
                for row in ((top + 1)..bottom).rev() {
                    pos.push((row, left));
                }
            }

            let len = pos.len();
            if len == 0 {
                continue;
            }
            let rot = (k as usize) % len;

            // extract current values
            let vals: Vec<i32> = pos.iter().map(|&(r, c)| grid[r][c]).collect();

            // write rotated values back
            for i in 0..len {
                let (r, c) = pos[i];
                res[r][c] = vals[(i + rot) % len];
            }
        }

        res
    }
}
```

## Racket

```racket
(define/contract (rotate-grid grid k)
  (-> (listof (listof exact-integer?)) exact-integer? (listof (listof exact-integer?)))
  (let* ((rows (list->vector (map list->vector grid)))
         (m (vector-length rows))
         (n (if (> m 0) (vector-length (vector-ref rows 0)) 0))
         (num-layers (/ (min m n) 2)))
    (for ([layer (in-range num-layers)])
      (let* ((top layer)
             (bottom (- m 1 layer))
             (left layer)
             (right (- n 1 layer))
             (positions '()))
        ;; top row
        (for ([col (in-range left (+ right 1))])
          (set! positions (cons (list top col) positions)))
        ;; right column (excluding corners)
        (for ([row (in-range (+ top 1) bottom)])
          (set! positions (cons (list row right) positions)))
        ;; bottom row
        (for ([col (in-range right (- left 1) -1)])
          (set! positions (cons (list bottom col) positions)))
        ;; left column (excluding corners)
        (for ([row (in-range (- bottom 1) (+ top 1) -1)])
          (set! positions (cons (list row left) positions)))
        (set! positions (reverse positions)) ; clockwise order
        (define len (length positions))
        (when (> len 0)
          (define rot (modulo k len))
          (define vals (make-vector len))
          ;; extract current values
          (for ([idx (in-range len)])
            (let* ((pos (list-ref positions idx))
                   (i (first pos))
                   (j (second pos)))
              (vector-set! vals idx (vector-ref (vector-ref rows i) j))))
          ;; rotate left by rot
          (define new-vals (make-vector len))
          (for ([idx (in-range len)])
            (let ((new-idx (modulo (+ idx (- rot)) len)))
              (vector-set! new-vals new-idx (vector-ref vals idx))))
          ;; write back rotated values
          (for ([idx (in-range len)])
            (let* ((pos (list-ref positions idx))
                   (i (first pos))
                   (j (second pos)))
              (vector-set! (vector-ref rows i) j (vector-ref new-vals idx)))))))
    (map vector->list (vector->list rows))))
```
