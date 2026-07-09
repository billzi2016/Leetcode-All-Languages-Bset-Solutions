# 3030. Find the Grid of Region Average

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> resultGrid(vector<vector<int>>& image, int threshold) {
        int m = image.size();
        int n = image[0].size();
        vector<vector<long long>> sum(m, vector<long long>(n, 0));
        vector<vector<int>> cnt(m, vector<int>(n, 0));

        for (int i = 0; i + 2 < m; ++i) {
            for (int j = 0; j + 2 < n; ++j) {
                bool ok = true;
                // horizontal adjacencies
                for (int dx = 0; dx < 3 && ok; ++dx) {
                    for (int dy = 0; dy < 2; ++dy) {
                        if (abs(image[i + dx][j + dy] - image[i + dx][j + dy + 1]) > threshold) {
                            ok = false;
                            break;
                        }
                    }
                }
                // vertical adjacencies
                for (int dx = 0; dx < 2 && ok; ++dx) {
                    for (int dy = 0; dy < 3; ++dy) {
                        if (abs(image[i + dx][j + dy] - image[i + dx + 1][j + dy]) > threshold) {
                            ok = false;
                            break;
                        }
                    }
                }
                if (!ok) continue;

                long long regionSum = 0;
                for (int x = i; x < i + 3; ++x)
                    for (int y = j; y < j + 3; ++y)
                        regionSum += image[x][y];
                int avg = static_cast<int>(regionSum / 9); // floor

                for (int x = i; x < i + 3; ++x) {
                    for (int y = j; y < j + 3; ++y) {
                        sum[x][y] += avg;
                        cnt[x][y] += 1;
                    }
                }
            }
        }

        vector<vector<int>> res(m, vector<int>(n));
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (cnt[i][j] == 0)
                    res[i][j] = image[i][j];
                else
                    res[i][j] = static_cast<int>(sum[i][j] / cnt[i][j]);
            }
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public int[][] resultGrid(int[][] image, int threshold) {
        int m = image.length;
        int n = image[0].length;
        int[][] sum = new int[m][n];
        int[][] cnt = new int[m][n];

        for (int i = 0; i <= m - 3; i++) {
            for (int j = 0; j <= n - 3; j++) {
                boolean ok = true;
                // check horizontal adjacents
                outer:
                for (int r = i; r < i + 3 && ok; r++) {
                    for (int c = j; c < j + 2; c++) { // compare (c) with (c+1)
                        if (Math.abs(image[r][c] - image[r][c + 1]) > threshold) {
                            ok = false;
                            break outer;
                        }
                    }
                }
                if (!ok) continue;
                // check vertical adjacents
                for (int r = i; r < i + 2 && ok; r++) {
                    for (int c = j; c < j + 3; c++) { // compare (r) with (r+1)
                        if (Math.abs(image[r][c] - image[r + 1][c]) > threshold) {
                            ok = false;
                            break;
                        }
                    }
                }
                if (!ok) continue;

                int regionSum = 0;
                for (int r = i; r < i + 3; r++) {
                    for (int c = j; c < j + 3; c++) {
                        regionSum += image[r][c];
                    }
                }
                int avg = regionSum / 9;

                for (int r = i; r < i + 3; r++) {
                    for (int c = j; c < j + 3; c++) {
                        sum[r][c] += avg;
                        cnt[r][c]++;
                    }
                }
            }
        }

        int[][] res = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (cnt[i][j] == 0) {
                    res[i][j] = image[i][j];
                } else {
                    res[i][j] = sum[i][j] / cnt[i][j];
                }
            }
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def resultGrid(self, image, threshold):
        """
        :type image: List[List[int]]
        :type threshold: int
        :rtype: List[List[int]]
        """
        m = len(image)
        n = len(image[0])
        acc = [[0] * n for _ in range(m)]
        cnt = [[0] * n for _ in range(m)]

        for i in range(m - 2):
            for j in range(n - 2):
                ok = True
                # check adjacency condition within the 3x3 subgrid
                for di in range(3):
                    r = i + di
                    for dj in range(3):
                        c = j + dj
                        if dj + 1 < 3:
                            if abs(image[r][c] - image[r][c + 1]) > threshold:
                                ok = False
                                break
                        if di + 1 < 3:
                            if abs(image[r][c] - image[r + 1][c]) > threshold:
                                ok = False
                                break
                    if not ok:
                        break
                if not ok:
                    continue

                # compute sum of the region
                s = 0
                for di in range(3):
                    row = image[i + di]
                    s += row[j] + row[j + 1] + row[j + 2]

                avg = s // 9
                for di in range(3):
                    for dj in range(3):
                        acc[i + di][j + dj] += avg
                        cnt[i + di][j + dj] += 1

        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if cnt[i][j]:
                    res[i][j] = acc[i][j] // cnt[i][j]
                else:
                    res[i][j] = image[i][j]
        return res
```

## Python3

```python
from typing import List

class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        sum_grid = [[0] * n for _ in range(m)]
        cnt_grid = [[0] * n for _ in range(m)]

        for i in range(m - 2):
            for j in range(n - 2):
                # check horizontal edges
                ok = True
                for x in range(i, i + 3):
                    for y in range(j, j + 2):
                        if abs(image[x][y] - image[x][y + 1]) > threshold:
                            ok = False
                            break
                    if not ok:
                        break
                if not ok:
                    continue

                # check vertical edges
                for x in range(i, i + 2):
                    for y in range(j, j + 3):
                        if abs(image[x][y] - image[x + 1][y]) > threshold:
                            ok = False
                            break
                    if not ok:
                        break
                if not ok:
                    continue

                # valid region: compute average (floor)
                total = 0
                for x in range(i, i + 3):
                    row = image[x]
                    for y in range(j, j + 3):
                        total += row[y]
                avg = total // 9

                # distribute to cells
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        sum_grid[x][y] += avg
                        cnt_grid[x][y] += 1

        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if cnt_grid[i][j]:
                    result[i][j] = sum_grid[i][j] // cnt_grid[i][j]
                else:
                    result[i][j] = image[i][j]
        return result
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

int** resultGrid(int** image, int imageSize, int* imageColSize, int threshold,
                 int* returnSize, int*** returnColumnSizes) {
    int rows = imageSize;
    int cols = imageColSize[0];

    long long *sum = (long long *)calloc((size_t)rows * cols, sizeof(long long));
    int *cnt = (int *)calloc((size_t)rows * cols, sizeof(int));

    for (int i = 0; i <= rows - 3; ++i) {
        for (int j = 0; j <= cols - 3; ++j) {
            bool ok = true;
            // horizontal edges inside the 3x3
            for (int di = 0; di < 3 && ok; ++di) {
                for (int dj = 0; dj < 2; ++dj) {
                    int a = image[i + di][j + dj];
                    int b = image[i + di][j + dj + 1];
                    if (abs(a - b) > threshold) { ok = false; break; }
                }
            }
            // vertical edges inside the 3x3
            for (int di = 0; di < 2 && ok; ++di) {
                for (int dj = 0; dj < 3; ++dj) {
                    int a = image[i + di][j + dj];
                    int b = image[i + di + 1][j + dj];
                    if (abs(a - b) > threshold) { ok = false; break; }
                }
            }
            if (!ok) continue;

            int sum9 = 0;
            for (int di = 0; di < 3; ++di)
                for (int dj = 0; dj < 3; ++dj)
                    sum9 += image[i + di][j + dj];
            int avg = sum9 / 9;

            for (int di = 0; di < 3; ++di) {
                int baseRow = i + di;
                for (int dj = 0; dj < 3; ++dj) {
                    int idx = baseRow * cols + (j + dj);
                    sum[idx] += avg;
                    cnt[idx] += 1;
                }
            }
        }
    }

    *returnSize = rows;
    *returnColumnSizes = (int **)malloc(rows * sizeof(int *));
    for (int r = 0; r < rows; ++r) {
        (*returnColumnSizes)[r] = (int *)malloc(sizeof(int));
        (*returnColumnSizes)[r][0] = cols;
    }

    int **result = (int **)malloc(rows * sizeof(int *));
    for (int i = 0; i < rows; ++i) {
        result[i] = (int *)malloc(cols * sizeof(int));
        for (int j = 0; j < cols; ++j) {
            int idx = i * cols + j;
            if (cnt[idx] == 0)
                result[i][j] = image[i][j];
            else
                result[i][j] = (int)(sum[idx] / cnt[idx]);
        }
    }

    free(sum);
    free(cnt);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int[][] ResultGrid(int[][] image, int threshold)
    {
        int m = image.Length;
        int n = image[0].Length;

        long[,] sum = new long[m, n];
        int[,] cnt = new int[m, n];

        for (int i = 0; i <= m - 3; i++)
        {
            for (int j = 0; j <= n - 3; j++)
            {
                bool ok = true;
                int regionSum = 0;

                // Check adjacency and compute sum
                for (int di = 0; di < 3 && ok; di++)
                {
                    for (int dj = 0; dj < 3 && ok; dj++)
                    {
                        int val = image[i + di][j + dj];
                        regionSum += val;

                        if (dj < 2)
                        {
                            if (Math.Abs(val - image[i + di][j + dj + 1]) > threshold)
                            {
                                ok = false;
                                break;
                            }
                        }

                        if (di < 2)
                        {
                            if (Math.Abs(val - image[i + di + 1][j + dj]) > threshold)
                            {
                                ok = false;
                                break;
                            }
                        }
                    }
                }

                if (!ok) continue;

                int avg = regionSum / 9; // floor average of the region

                for (int di = 0; di < 3; di++)
                {
                    for (int dj = 0; dj < 3; dj++)
                    {
                        sum[i + di, j + dj] += avg;
                        cnt[i + di, j + dj]++;
                    }
                }
            }
        }

        int[][] result = new int[m][];
        for (int i = 0; i < m; i++)
        {
            result[i] = new int[n];
            for (int j = 0; j < n; j++)
            {
                if (cnt[i, j] == 0)
                    result[i][j] = image[i][j];
                else
                    result[i][j] = (int)(sum[i, j] / cnt[i, j]);
            }
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} image
 * @param {number} threshold
 * @return {number[][]}
 */
var resultGrid = function(image, threshold) {
    const m = image.length;
    const n = image[0].length;
    const sumVals = Array.from({ length: m }, () => Array(n).fill(0));
    const cnt = Array.from({ length: m }, () => Array(n).fill(0));

    for (let i = 0; i <= m - 3; i++) {
        for (let j = 0; j <= n - 3; j++) {
            let ok = true;
            let regionSum = 0;

            // Check adjacency and compute sum
            for (let di = 0; di < 3 && ok; di++) {
                const x = i + di;
                for (let dj = 0; dj < 3 && ok; dj++) {
                    const y = j + dj;
                    regionSum += image[x][y];
                    if (dj < 2) {
                        if (Math.abs(image[x][y] - image[x][y + 1]) > threshold) {
                            ok = false;
                            break;
                        }
                    }
                    if (di < 2) {
                        if (Math.abs(image[x][y] - image[x + 1][y]) > threshold) {
                            ok = false;
                            break;
                        }
                    }
                }
            }

            if (!ok) continue;

            const avg = Math.floor(regionSum / 9);
            for (let di = 0; di < 3; di++) {
                const x = i + di;
                for (let dj = 0; dj < 3; dj++) {
                    const y = j + dj;
                    sumVals[x][y] += avg;
                    cnt[x][y] += 1;
                }
            }
        }
    }

    const result = Array.from({ length: m }, () => Array(n));
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (cnt[i][j] === 0) {
                result[i][j] = image[i][j];
            } else {
                result[i][j] = Math.floor(sumVals[i][j] / cnt[i][j]);
            }
        }
    }

    return result;
};
```

## Typescript

```typescript
function resultGrid(image: number[][], threshold: number): number[][] {
    const m = image.length;
    const n = image[0].length;
    const sum: number[][] = Array.from({ length: m }, () => Array(n).fill(0));
    const cnt: number[][] = Array.from({ length: m }, () => Array(n).fill(0));

    for (let i = 0; i <= m - 3; i++) {
        for (let j = 0; j <= n - 3; j++) {
            let ok = true;
            // check horizontal edges
            for (let r = i; r < i + 3 && ok; r++) {
                for (let c = j; c < j + 2; c++) {
                    if (Math.abs(image[r][c] - image[r][c + 1]) > threshold) {
                        ok = false;
                        break;
                    }
                }
            }
            // check vertical edges
            for (let r = i; r < i + 2 && ok; r++) {
                for (let c = j; c < j + 3; c++) {
                    if (Math.abs(image[r][c] - image[r + 1][c]) > threshold) {
                        ok = false;
                        break;
                    }
                }
            }
            if (!ok) continue;

            let total = 0;
            for (let r = i; r < i + 3; r++) {
                for (let c = j; c < j + 3; c++) {
                    total += image[r][c];
                }
            }
            const avg = Math.floor(total / 9);
            for (let r = i; r < i + 3; r++) {
                for (let c = j; c < j + 3; c++) {
                    sum[r][c] += avg;
                    cnt[r][c] += 1;
                }
            }
        }
    }

    const result: number[][] = Array.from({ length: m }, () => Array(n).fill(0));
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (cnt[i][j] === 0) {
                result[i][j] = image[i][j];
            } else {
                result[i][j] = Math.floor(sum[i][j] / cnt[i][j]);
            }
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $image
     * @param Integer $threshold
     * @return Integer[][]
     */
    function resultGrid($image, $threshold) {
        $m = count($image);
        $n = count($image[0]);
        $sum = array_fill(0, $m, array_fill(0, $n, 0));
        $cnt = array_fill(0, $m, array_fill(0, $n, 0));

        for ($r = 0; $r <= $m - 3; $r++) {
            for ($c = 0; $c <= $n - 3; $c++) {
                $valid = true;
                // check horizontal adjacencies
                for ($i = $r; $i < $r + 3 && $valid; $i++) {
                    for ($j = $c; $j < $c + 2; $j++) {
                        if (abs($image[$i][$j] - $image[$i][$j + 1]) > $threshold) {
                            $valid = false;
                            break;
                        }
                    }
                }
                // check vertical adjacencies
                for ($i = $r; $i < $r + 2 && $valid; $i++) {
                    for ($j = $c; $j < $c + 3; $j++) {
                        if (abs($image[$i][$j] - $image[$i + 1][$j]) > $threshold) {
                            $valid = false;
                            break;
                        }
                    }
                }

                if (!$valid) {
                    continue;
                }

                // compute average of the region
                $total = 0;
                for ($i = $r; $i < $r + 3; $i++) {
                    for ($j = $c; $j < $c + 3; $j++) {
                        $total += $image[$i][$j];
                    }
                }
                $avg = intdiv($total, 9);

                // accumulate to each cell
                for ($i = $r; $i < $r + 3; $i++) {
                    for ($j = $c; $j < $c + 3; $j++) {
                        $sum[$i][$j] += $avg;
                        $cnt[$i][$j] += 1;
                    }
                }
            }
        }

        $result = [];
        for ($i = 0; $i < $m; $i++) {
            $row = [];
            for ($j = 0; $j < $n; $j++) {
                if ($cnt[$i][$j] > 0) {
                    $val = intdiv($sum[$i][$j], $cnt[$i][$j]);
                } else {
                    $val = $image[$i][$j];
                }
                $row[] = $val;
            }
            $result[] = $row;
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func resultGrid(_ image: [[Int]], _ threshold: Int) -> [[Int]] {
        let m = image.count
        let n = image[0].count
        var sumGrid = Array(repeating: Array(repeating: 0, count: n), count: m)
        var cntGrid = Array(repeating: Array(repeating: 0, count: n), count: m)
        
        if m >= 3 && n >= 3 {
            for r in 0..<(m - 2) {
                for c in 0..<(n - 2) {
                    var valid = true
                    // Check adjacency constraints within the 3x3 subgrid
                    outer: for i in 0..<3 {
                        for j in 0..<3 {
                            if i < 2 {
                                let diff = abs(image[r + i][c + j] - image[r + i + 1][c + j])
                                if diff > threshold {
                                    valid = false
                                    break outer
                                }
                            }
                            if j < 2 {
                                let diff = abs(image[r + i][c + j] - image[r + i][c + j + 1])
                                if diff > threshold {
                                    valid = false
                                    break outer
                                }
                            }
                        }
                    }
                    
                    if !valid { continue }
                    
                    var regionSum = 0
                    for i in 0..<3 {
                        for j in 0..<3 {
                            regionSum += image[r + i][c + j]
                        }
                    }
                    let avgFloor = regionSum / 9
                    
                    for i in 0..<3 {
                        for j in 0..<3 {
                            sumGrid[r + i][c + j] += avgFloor
                            cntGrid[r + i][c + j] += 1
                        }
                    }
                }
            }
        }
        
        var result = image
        for i in 0..<m {
            for j in 0..<n {
                if cntGrid[i][j] > 0 {
                    result[i][j] = sumGrid[i][j] / cntGrid[i][j]
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
    fun resultGrid(image: Array<IntArray>, threshold: Int): Array<IntArray> {
        val m = image.size
        val n = image[0].size
        val sum = Array(m) { LongArray(n) }
        val cnt = Array(m) { IntArray(n) }

        for (i in 0 until m - 2) {
            for (j in 0 until n - 2) {
                var ok = true

                // Check horizontal adjacents
                outerH@ for (dx in 0..2) {
                    for (dy in 0 until 2) {
                        if (kotlin.math.abs(image[i + dx][j + dy] - image[i + dx][j + dy + 1]) > threshold) {
                            ok = false
                            break@outerH
                        }
                    }
                }
                if (!ok) continue

                // Check vertical adjacents
                outerV@ for (dx in 0 until 2) {
                    for (dy in 0..2) {
                        if (kotlin.math.abs(image[i + dx][j + dy] - image[i + dx + 1][j + dy]) > threshold) {
                            ok = false
                            break@outerV
                        }
                    }
                }
                if (!ok) continue

                var regionSum = 0
                for (dx in 0..2) {
                    for (dy in 0..2) {
                        regionSum += image[i + dx][j + dy]
                    }
                }

                val avg = regionSum / 9
                for (dx in 0..2) {
                    for (dy in 0..2) {
                        sum[i + dx][j + dy] += avg.toLong()
                        cnt[i + dx][j + dy]++
                    }
                }
            }
        }

        val result = Array(m) { IntArray(n) }
        for (i in 0 until m) {
            for (j in 0 until n) {
                result[i][j] = if (cnt[i][j] > 0) {
                    (sum[i][j] / cnt[i][j]).toInt()
                } else {
                    image[i][j]
                }
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> resultGrid(List<List<int>> image, int threshold) {
    int m = image.length;
    int n = image[0].length;
    List<List<int>> sum = List.generate(m, (_) => List.filled(n, 0));
    List<List<int>> cnt = List.generate(m, (_) => List.filled(n, 0));

    for (int i = 0; i <= m - 3; ++i) {
      for (int j = 0; j <= n - 3; ++j) {
        bool ok = true;
        // horizontal adjacents
        for (int di = 0; di < 3 && ok; ++di) {
          for (int dj = 0; dj < 2; ++dj) {
            if ((image[i + di][j + dj] - image[i + di][j + dj + 1]).abs() > threshold) {
              ok = false;
              break;
            }
          }
        }
        // vertical adjacents
        for (int di = 0; di < 2 && ok; ++di) {
          for (int dj = 0; dj < 3; ++dj) {
            if ((image[i + di][j + dj] - image[i + di + 1][j + dj]).abs() > threshold) {
              ok = false;
              break;
            }
          }
        }

        if (!ok) continue;

        int total = 0;
        for (int di = 0; di < 3; ++di) {
          for (int dj = 0; dj < 3; ++dj) {
            total += image[i + di][j + dj];
          }
        }
        int avg = total ~/ 9;

        for (int di = 0; di < 3; ++di) {
          for (int dj = 0; dj < 3; ++dj) {
            sum[i + di][j + dj] += avg;
            cnt[i + di][j + dj] += 1;
          }
        }
      }
    }

    List<List<int>> result = List.generate(m, (_) => List.filled(n, 0));
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (cnt[i][j] > 0) {
          result[i][j] = sum[i][j] ~/ cnt[i][j];
        } else {
          result[i][j] = image[i][j];
        }
      }
    }
    return result;
  }
}
```

## Golang

```go
func resultGrid(image [][]int, threshold int) [][]int {
	m := len(image)
	n := len(image[0])
	sum := make([][]int, m)
	cnt := make([][]int, m)
	for i := 0; i < m; i++ {
		sum[i] = make([]int, n)
		cnt[i] = make([]int, n)
	}
	abs := func(a int) int {
		if a < 0 {
			return -a
		}
		return a
	}
	for i := 0; i <= m-3; i++ {
		for j := 0; j <= n-3; j++ {
			ok := true
			// check all adjacent pairs inside the 3x3 block
			for x := 0; x < 3 && ok; x++ {
				for y := 0; y < 3 && ok; y++ {
					if y+1 < 3 {
						if abs(image[i+x][j+y]-image[i+x][j+y+1]) > threshold {
							ok = false
							break
						}
					}
					if x+1 < 3 {
						if abs(image[i+x][j+y]-image[i+x+1][j+y]) > threshold {
							ok = false
							break
						}
					}
				}
			}
			if !ok {
				continue
			}
			total := 0
			for dx := 0; dx < 3; dx++ {
				for dy := 0; dy < 3; dy++ {
					total += image[i+dx][j+dy]
				}
			}
			avg := total / 9
			for dx := 0; dx < 3; dx++ {
				rowIdx := i + dx
				for dy := 0; dy < 3; dy++ {
					colIdx := j + dy
					sum[rowIdx][colIdx] += avg
					cnt[rowIdx][colIdx]++
				}
			}
		}
	}
	result := make([][]int, m)
	for i := 0; i < m; i++ {
		row := make([]int, n)
		for j := 0; j < n; j++ {
			if cnt[i][j] == 0 {
				row[j] = image[i][j]
			} else {
				row[j] = sum[i][j] / cnt[i][j]
			}
		}
		result[i] = row
	}
	return result
}
```

## Ruby

```ruby
def result_grid(image, threshold)
  m = image.size
  n = image[0].size
  sum_grid = Array.new(m) { Array.new(n, 0) }
  cnt_grid = Array.new(m) { Array.new(n, 0) }

  (0..m - 3).each do |i|
    (0..n - 3).each do |j|
      valid = true

      # check horizontal adjacencies
      3.times do |dx|
        2.times do |dy|
          a = image[i + dx][j + dy]
          b = image[i + dx][j + dy + 1]
          if (a - b).abs > threshold
            valid = false
            break
          end
        end
        break unless valid
      end
      next unless valid

      # check vertical adjacencies
      2.times do |dx|
        3.times do |dy|
          a = image[i + dx][j + dy]
          b = image[i + dx + 1][j + dy]
          if (a - b).abs > threshold
            valid = false
            break
          end
        end
        break unless valid
      end
      next unless valid

      total = 0
      3.times do |dx|
        3.times do |dy|
          total += image[i + dx][j + dy]
        end
      end
      avg = total / 9

      3.times do |dx|
        3.times do |dy|
          x = i + dx
          y = j + dy
          sum_grid[x][y] += avg
          cnt_grid[x][y] += 1
        end
      end
    end
  end

  result = Array.new(m) { Array.new(n, 0) }
  m.times do |i|
    n.times do |j|
      if cnt_grid[i][j] == 0
        result[i][j] = image[i][j]
      else
        result[i][j] = sum_grid[i][j] / cnt_grid[i][j]
      end
    end
  end
  result
end
```

## Scala

```scala
object Solution {
    def resultGrid(image: Array[Array[Int]], threshold: Int): Array[Array[Int]] = {
        val m = image.length
        val n = image(0).length
        val sumArr = Array.ofDim[Int](m, n)
        val cntArr = Array.ofDim[Int](m, n)

        var i = 0
        while (i <= m - 3) {
            var j = 0
            while (j <= n - 3) {
                var ok = true

                // check horizontal adjacencies
                var r = i
                while (ok && r < i + 3) {
                    var c = j
                    while (ok && c < j + 2) { // compare (r,c) with (r,c+1)
                        if (math.abs(image(r)(c) - image(r)(c + 1)) > threshold) ok = false
                        c += 1
                    }
                    r += 1
                }

                // check vertical adjacencies
                var c = j
                while (ok && c < j + 3) {
                    var r2 = i
                    while (ok && r2 < i + 2) { // compare (r2,c) with (r2+1,c)
                        if (math.abs(image(r2)(c) - image(r2 + 1)(c)) > threshold) ok = false
                        r2 += 1
                    }
                    c += 1
                }

                if (ok) {
                    var sum = 0
                    var rr = i
                    while (rr < i + 3) {
                        var cc = j
                        while (cc < j + 3) {
                            sum += image(rr)(cc)
                            cc += 1
                        }
                        rr += 1
                    }
                    val avgFloor = sum / 9

                    rr = i
                    while (rr < i + 3) {
                        var cc = j
                        while (cc < j + 3) {
                            sumArr(rr)(cc) += avgFloor
                            cntArr(rr)(cc) += 1
                            cc += 1
                        }
                        rr += 1
                    }
                }

                j += 1
            }
            i += 1
        }

        val result = Array.ofDim[Int](m, n)
        var rIdx = 0
        while (rIdx < m) {
            var cIdx = 0
            while (cIdx < n) {
                if (cntArr(rIdx)(cIdx) > 0) result(rIdx)(cIdx) = sumArr(rIdx)(cIdx) / cntArr(rIdx)(cIdx)
                else result(rIdx)(cIdx) = image(rIdx)(cIdx)
                cIdx += 1
            }
            rIdx += 1
        }

        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn result_grid(image: Vec<Vec<i32>>, threshold: i32) -> Vec<Vec<i32>> {
        let m = image.len();
        let n = image[0].len();
        let mut sum_grid = vec![vec![0i64; n]; m];
        let mut cnt_grid = vec![vec![0i32; n]; m];

        for r in 0..=m - 3 {
            for c in 0..=n - 3 {
                // Check adjacency constraints
                let mut ok = true;
                'check: {
                    // horizontal adjacencies
                    for i in 0..3 {
                        for j in 0..2 {
                            if (image[r + i][c + j] - image[r + i][c + j + 1]).abs() > threshold {
                                ok = false;
                                break 'check;
                            }
                        }
                    }
                    // vertical adjacencies
                    for i in 0..2 {
                        for j in 0..3 {
                            if (image[r + i][c + j] - image[r + i + 1][c + j]).abs() > threshold {
                                ok = false;
                                break 'check;
                            }
                        }
                    }
                }

                if ok {
                    // Compute average of the region
                    let mut total: i64 = 0;
                    for i in 0..3 {
                        for j in 0..3 {
                            total += image[r + i][c + j] as i64;
                        }
                    }
                    let avg = total / 9;

                    // Accumulate to each cell
                    for i in r..r + 3 {
                        for j in c..c + 3 {
                            sum_grid[i][j] += avg;
                            cnt_grid[i][j] += 1;
                        }
                    }
                }
            }
        }

        let mut result = vec![vec![0i32; n]; m];
        for i in 0..m {
            for j in 0..n {
                if cnt_grid[i][j] > 0 {
                    result[i][j] = (sum_grid[i][j] / cnt_grid[i][j] as i64) as i32;
                } else {
                    result[i][j] = image[i][j];
                }
            }
        }
        result
    }
}
```

## Racket

```racket
#lang racket

(define/contract (result-grid image threshold)
  (-> (listof (listof exact-integer?)) exact-integer?
       (listof (listof exact-integer?)))
  (let* ([m (length image)]
         [n (if (zero? m) 0 (length (first image)))]
         [imgVec (list->vector (map list->vector image))]
         [sumVec (for/vector ([i m]) (make-vector n 0))]
         [cntVec (for/vector ([i m]) (make-vector n 0))])
    ;; Scan all possible 3×3 sub‑grids
    (for ([i (in-range (- m 2))])
      (for ([j (in-range (- n 2))])
        (let ([valid #t] [total 0])
          ;; Compute sum and verify adjacency condition
          (for ([dx (in-range 3)])
            (let ([x (+ i dx)])
              (for ([dy (in-range 3)])
                (let* ([y   (+ j dy)]
                       [val (vector-ref (vector-ref imgVec x) y)])
                  (set! total (+ total val))
                  (when (and (< dy 2) valid)
                    (let ([right (vector-ref (vector-ref imgVec x) (+ y 1))])
                      (when (> (abs (- val right)) threshold)
                        (set! valid #f))))
                  (when (and (< dx 2) valid)
                    (let ([down (vector-ref (vector-ref imgVec (+ x 1)) y)])
                      (when (> (abs (- val down)) threshold)
                        (set! valid #f)))))))))
          (when valid
            (define avg (quotient total 9))
            ;; Accumulate average for each cell in the region
            (for ([dx (in-range 3)])
              (let ([x (+ i dx)])
                (for ([dy (in-range 3)])
                  (let ([y (+ j dy)])
                    (vector-set! (vector-ref sumVec x) y
                                 (+ (vector-ref (vector-ref sumVec x) y) avg))
                    (vector-set! (vector-ref cntVec x) y
                                 (+ (vector-ref (vector-ref cntVec x) y) 1))))))))))
    ;; Build the resulting grid
    (for/list ([i (in-range m)])
      (for/list ([j (in-range n)])
        (let* ([cnt (vector-ref (vector-ref cntVec i) j)]
               [s   (vector-ref (vector-ref sumVec i) j)])
          (if (> cnt 0)
              (quotient s cnt)
              (vector-ref (vector-ref imgVec i) j)))))))
```

## Erlang

```erlang
-spec result_grid(Image :: [[integer()]], Threshold :: integer()) -> [[integer()]].
result_grid(Image, Threshold) ->
    PixelMap = build_pixel_map(Image, 0, #{}),
    M = length(Image),
    N = case Image of
            [] -> 0;
            [Row|_] -> length(Row)
        end,
    TopLefts = [{I,J} || I <- lists:seq(0, M-3), J <- lists:seq(0, N-3)],
    {SumMap, CntMap} =
        lists:foldl(fun({I,J}, {SM, CM}) ->
            case check_region(I, J, Threshold, PixelMap) of
                {ok, RegionAvg, Coords} ->
                    update_maps(Coords, RegionAvg, SM, CM);
                false ->
                    {SM, CM}
            end
        end, {#{}, #{}}, TopLefts),
    [ [ case maps:get({I,J}, CntMap, 0) of
            0 -> maps:get({I,J}, PixelMap);
            Count -> maps:get({I,J}, SumMap) div Count
        end
      || J <- lists:seq(0, N-1) ]
    || I <- lists:seq(0, M-1) ].

%% Build a map from coordinates to pixel values.
build_pixel_map([], _RowIdx, Map) -> Map;
build_pixel_map([Row|Rest], RowIdx, Map) ->
    NewMap = build_row(Row, RowIdx, 0, Map),
    build_pixel_map(Rest, RowIdx + 1, NewMap).

build_row([], _RowIdx, _ColIdx, Map) -> Map;
build_row([V|Vs], RowIdx, ColIdx, Map) ->
    Updated = maps:put({RowIdx, ColIdx}, V, Map),
    build_row(Vs, RowIdx, ColIdx + 1, Updated).

%% Verify a 3x3 region and compute its average if valid.
check_region(I, J, Threshold, PixelMap) ->
    CoordsVals = [{DX,DY,maps:get({I+DX,J+DY}, PixelMap)} ||
                  DX <- [0,1,2], DY <- [0,1,2]],
    Sum = lists:foldl(fun({_X,_Y,V}, Acc) -> Acc + V end, 0, CoordsVals),
    Valid = lists:all(
        fun({X,Y,V}) ->
            (if Y < 2 ->
                    VRight = maps:get({I+X,J+Y+1}, PixelMap),
                    erlang:abs(V - VRight) =< Threshold;
               true -> true
             end)
            andalso
            (if X < 2 ->
                    VDown = maps:get({I+X+1,J+Y}, PixelMap),
                    erlang:abs(V - VDown) =< Threshold;
               true -> true
             end)
        end, CoordsVals),
    case Valid of
        true ->
            RegionAvg = Sum div 9,
            Coords = [{I+DX, J+DY} || {DX,DY,_} <- CoordsVals],
            {ok, RegionAvg, Coords};
        false -> false
    end.

%% Update sum and count maps for all cells in a region.
update_maps([], _RegionAvg, SumMap, CntMap) ->
    {SumMap, CntMap};
update_maps([{X,Y}|Rest], RegionAvg, SumMap, CntMap) ->
    Key = {X,Y},
    NewSumMap = maps:update_with(Key, fun(V) -> V + RegionAvg end,
                                 RegionAvg, SumMap),
    NewCntMap = maps:update_with(Key, fun(C) -> C + 1 end,
                                 1, CntMap),
    update_maps(Rest, RegionAvg, NewSumMap, NewCntMap).
```

## Elixir

```elixir
defmodule Solution do
  @spec result_grid(image :: [[integer]], threshold :: integer) :: [[integer]]
  def result_grid(image, threshold) do
    m = length(image)
    n = length(hd(image))
    max_r = m - 3
    max_c = n - 3

    region_map =
      Enum.reduce(0..max_r, %{}, fn r, acc ->
        Enum.reduce(0..max_c, acc, fn c, acc2 ->
          sub_rows =
            for dr <- 0..2 do
              row = Enum.at(image, r + dr)
              Enum.slice(row, c, 3)
            end

          valid? =
            Enum.reduce_while(0..2, true, fn i, _ ->
              Enum.reduce_while(0..2, true, fn j, _ ->
                val = Enum.at(Enum.at(sub_rows, i), j)

                cond do
                  j < 2 and abs(val - Enum.at(Enum.at(sub_rows, i), j + 1)) > threshold ->
                    {:halt, false}

                  i < 2 and abs(val - Enum.at(Enum.at(sub_rows, i + 1), j)) > threshold ->
                    {:halt, false}

                  true ->
                    {:cont, true}
                end
              end)
              |> case do
                false -> {:halt, false}
                true -> {:cont, true}
              end
            end)

          if valid? do
            sum = Enum.reduce(sub_rows, 0, fn row, acc_sum -> acc_sum + Enum.sum(row) end)
            avg = div(sum, 9)

            Enum.reduce(0..2, acc2, fn dr, map1 ->
              Enum.reduce(0..2, map1, fn dc, map2 ->
                key = {r + dr, c + dc}
                {s, cnt} = Map.get(map2, key, {0, 0})
                Map.put(map2, key, {s + avg, cnt + 1})
              end)
            end)
          else
            acc2
          end
        end)
      end)

    for i <- 0..(m - 1) do
      row =
        for j <- 0..(n - 1) do
          case Map.get(region_map, {i, j}) do
            nil -> Enum.at(Enum.at(image, i), j)
            {s, cnt} -> div(s, cnt)
          end
        end

      row
    end
  end
end
```
