# 1260. Shift 2D Grid

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
        int m = grid.size();
        int n = grid[0].size();
        int total = m * n;
        if (total == 0) return grid;
        k %= total;
        if (k == 0) return grid;
        
        vector<int> flat(total);
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                flat[i * n + j] = grid[i][j];
        
        vector<int> shifted(total);
        int start = (total - k) % total;
        for (int idx = 0; idx < total; ++idx) {
            shifted[idx] = flat[(start + idx) % total];
        }
        
        vector<vector<int>> result(m, vector<int>(n));
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                result[i][j] = shifted[i * n + j];
        
        return result;
    }
};
```

## Java

```java
class Solution {
    public List<List<Integer>> shiftGrid(int[][] grid, int k) {
        int m = grid.length;
        int n = grid[0].length;
        int total = m * n;
        k %= total;
        List<List<Integer>> result = new ArrayList<>(m);
        for (int i = 0; i < m; i++) {
            List<Integer> row = new ArrayList<>(n);
            for (int j = 0; j < n; j++) {
                int idx = i * n + j;
                int oldIdx = idx - k;
                if (oldIdx < 0) oldIdx += total;
                int val = grid[oldIdx / n][oldIdx % n];
                row.add(val);
            }
            result.add(row);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        total = m * n
        k %= total
        if k == 0:
            return grid

        # flatten the grid
        flat = [grid[i][j] for i in range(m) for j in range(n)]
        # shift right by k: take last k elements to front
        shifted = flat[-k:] + flat[:-k]

        # reconstruct the grid
        res = []
        for i in range(m):
            start = i * n
            res.append(shifted[start:start + n])
        return res
```

## Python3

```python
from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total
        if k == 0:
            return [row[:] for row in grid]

        flat = [grid[i][j] for i in range(m) for j in range(n)]
        rotated = flat[-k:] + flat[:-k]

        res = []
        idx = 0
        for _ in range(m):
            res.append(rotated[idx:idx + n])
            idx += n
        return res
```

## C

```c
#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** shiftGrid(int** grid, int gridSize, int* gridColSize, int k, int* returnSize, int*** returnColumnSizes) {
    int m = gridSize;
    int n = gridColSize[0];
    int total = m * n;
    if (total == 0) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }
    
    int shift = k % total;
    
    // Flatten original grid
    int* flat = (int*)malloc(total * sizeof(int));
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            flat[i * n + j] = grid[i][j];
        }
    }
    
    // Apply shift
    int* shifted = (int*)malloc(total * sizeof(int));
    if (shift == 0) {
        for (int i = 0; i < total; ++i) shifted[i] = flat[i];
    } else {
        for (int idx = 0; idx < total; ++idx) {
            int newIdx = (idx + shift) % total;
            shifted[newIdx] = flat[idx];
        }
    }
    
    // Prepare return structures
    *returnSize = m;
    *returnColumnSizes = (int**)malloc(m * sizeof(int*));
    for (int i = 0; i < m; ++i) {
        (*returnColumnSizes)[i] = (int*)malloc(sizeof(int));
        (*returnColumnSizes)[i][0] = n;
    }
    
    int** result = (int**)malloc(m * sizeof(int*));
    for (int i = 0; i < m; ++i) {
        result[i] = (int*)malloc(n * sizeof(int));
        for (int j = 0; j < n; ++j) {
            result[i][j] = shifted[i * n + j];
        }
    }
    
    free(flat);
    free(shifted);
    
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public IList<IList<int>> ShiftGrid(int[][] grid, int k) {
        int m = grid.Length;
        int n = grid[0].Length;
        int total = m * n;
        int shift = k % total;

        // Flatten the grid
        int[] flat = new int[total];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                flat[i * n + j] = grid[i][j];
            }
        }

        // Rotate right by shift positions
        int[] rotated = new int[total];
        for (int idx = 0; idx < total; idx++) {
            int newIdx = (idx + shift) % total;
            rotated[newIdx] = flat[idx];
        }

        // Build the result grid
        var result = new List<IList<int>>(m);
        for (int i = 0; i < m; i++) {
            var row = new List<int>(n);
            for (int j = 0; j < n; j++) {
                row.Add(rotated[i * n + j]);
            }
            result.Add(row);
        }

        return result;
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
var shiftGrid = function(grid, k) {
    const m = grid.length;
    const n = grid[0].length;
    const total = m * n;
    k %= total;
    if (k === 0) return grid;

    const flat = new Array(total);
    let idx = 0;
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            flat[idx++] = grid[i][j];
        }
    }

    const rotated = flat.slice(-k).concat(flat.slice(0, total - k));

    const res = new Array(m);
    idx = 0;
    for (let i = 0; i < m; ++i) {
        const row = new Array(n);
        for (let j = 0; j < n; ++j) {
            row[j] = rotated[idx++];
        }
        res[i] = row;
    }

    return res;
};
```

## Typescript

```typescript
function shiftGrid(grid: number[][], k: number): number[][] {
    const m = grid.length;
    const n = grid[0].length;
    const total = m * n;
    const shift = k % total;
    if (shift === 0) return grid.map(row => row.slice());

    // flatten the grid
    const flat: number[] = [];
    for (let i = 0; i < m; ++i) {
        flat.push(...grid[i]);
    }

    // rotate right by 'shift'
    const start = total - shift;
    const rotated = flat.slice(start).concat(flat.slice(0, start));

    // rebuild the grid
    const result: number[][] = new Array(m);
    let idx = 0;
    for (let i = 0; i < m; ++i) {
        const row: number[] = new Array(n);
        for (let j = 0; j < n; ++j) {
            row[j] = rotated[idx++];
        }
        result[i] = row;
    }
    return result;
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
    function shiftGrid($grid, $k) {
        $m = count($grid);
        $n = count($grid[0]);
        $total = $m * $n;
        if ($total == 0) return [];

        $k = $k % $total;
        // flatten the grid
        $flat = [];
        foreach ($grid as $row) {
            foreach ($row as $val) {
                $flat[] = $val;
            }
        }

        if ($k > 0) {
            // rotate right by k positions
            $rotated = array_merge(
                array_slice($flat, -$k),
                array_slice($flat, 0, $total - $k)
            );
        } else {
            $rotated = $flat;
        }

        // reconstruct the grid
        $result = [];
        for ($i = 0; $i < $m; $i++) {
            $result[$i] = array_slice($rotated, $i * $n, $n);
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func shiftGrid(_ grid: [[Int]], _ k: Int) -> [[Int]] {
        let m = grid.count
        guard m > 0 else { return [] }
        let n = grid[0].count
        let total = m * n
        let shift = k % total
        if shift == 0 { return grid }
        
        var flat = [Int]()
        flat.reserveCapacity(total)
        for row in grid {
            flat.append(contentsOf: row)
        }
        
        let split = total - shift
        let rotated = Array(flat[split..<total]) + Array(flat[0..<split])
        
        var result = [[Int]]()
        result.reserveCapacity(m)
        for i in 0..<m {
            let start = i * n
            let row = Array(rotated[start..<(start + n)])
            result.append(row)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun shiftGrid(grid: Array<IntArray>, k: Int): List<List<Int>> {
        val m = grid.size
        val n = grid[0].size
        val total = m * n
        val shift = k % total
        if (shift == 0) return grid.map { it.toList() }

        val flat = IntArray(total)
        var idx = 0
        for (i in 0 until m) {
            for (j in 0 until n) {
                flat[idx++] = grid[i][j]
            }
        }

        val rotated = IntArray(total)
        for (i in 0 until total) {
            val newIdx = (i + shift) % total
            rotated[newIdx] = flat[i]
        }

        val result = ArrayList<List<Int>>(m)
        idx = 0
        for (i in 0 until m) {
            val row = ArrayList<Int>(n)
            for (j in 0 until n) {
                row.add(rotated[idx++])
            }
            result.add(row)
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> shiftGrid(List<List<int>> grid, int k) {
    int m = grid.length;
    int n = grid[0].length;
    int total = m * n;
    int shift = k % total;
    if (shift == 0) {
      return List.generate(m, (i) => List.from(grid[i]));
    }
    List<int> flat = [];
    for (var row in grid) {
      flat.addAll(row);
    }
    int split = total - shift;
    List<int> rotated = [];
    rotated.addAll(flat.sublist(split));
    rotated.addAll(flat.sublist(0, split));
    List<List<int>> res = List.generate(m, (_) => List.filled(n, 0));
    int idx = 0;
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        res[i][j] = rotated[idx++];
      }
    }
    return res;
  }
}
```

## Golang

```go
func shiftGrid(grid [][]int, k int) [][]int {
    m := len(grid)
    if m == 0 {
        return grid
    }
    n := len(grid[0])
    total := m * n
    k %= total
    if k == 0 {
        return grid
    }

    result := make([][]int, m)
    for i := range result {
        result[i] = make([]int, n)
    }

    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            idx := i*n + j
            newIdx := (idx + k) % total
            newI := newIdx / n
            newJ := newIdx % n
            result[newI][newJ] = grid[i][j]
        }
    }
    return result
}
```

## Ruby

```ruby
def shift_grid(grid, k)
  m = grid.size
  n = grid[0].size
  total = m * n
  k %= total
  return grid if k == 0

  flat = grid.flatten
  rotated = flat[-k, k] + flat[0, total - k]

  result = []
  (0...m).each do |i|
    result << rotated[i * n, n]
  end
  result
end
```

## Scala

```scala
object Solution {
    def shiftGrid(grid: Array[Array[Int]], k: Int): List[List[Int]] = {
        val m = grid.length
        val n = if (m > 0) grid(0).length else 0
        val total = m * n
        val kk = k % total
        if (kk == 0) return grid.map(_.toList).toList

        // flatten the grid
        val flat = new Array[Int](total)
        var idx = 0
        for (i <- 0 until m; j <- 0 until n) {
            flat(idx) = grid(i)(j)
            idx += 1
        }

        // rotate right by kk positions
        val rotated = new Array[Int](total)
        val start = (total - kk) % total
        for (i <- 0 until total) {
            rotated(i) = flat((start + i) % total)
        }

        // reconstruct the 2D grid
        val ans = Array.ofDim[Int](m, n)
        idx = 0
        for (i <- 0 until m; j <- 0 until n) {
            ans(i)(j) = rotated(idx)
            idx += 1
        }
        ans.map(_.toList).toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn shift_grid(grid: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        let m = grid.len();
        if m == 0 {
            return vec![];
        }
        let n = grid[0].len();
        let total = m * n;
        let shift = (k as usize) % total;

        // Flatten the grid
        let mut flat: Vec<i32> = Vec::with_capacity(total);
        for row in &grid {
            flat.extend_from_slice(row);
        }

        if shift == 0 {
            return grid;
        }

        // Rotate right by 'shift' positions
        let mut rotated = vec![0i32; total];
        for i in 0..total {
            let new_idx = (i + shift) % total;
            rotated[new_idx] = flat[i];
        }

        // Reconstruct the 2D grid
        let mut result = vec![vec![0i32; n]; m];
        for idx in 0..total {
            let r = idx / n;
            let c = idx % n;
            result[r][c] = rotated[idx];
        }
        result
    }
}
```

## Racket

```racket
#lang racket
(require racket/list)

(provide shift-grid)

(define/contract (shift-grid grid k)
  (-> (listof (listof exact-integer?)) exact-integer? (listof (listof exact-integer?)))
  (let* ((m (length grid))
         (n (if (null? grid) 0 (length (first grid))))
         (flat (apply append grid))
         (len (* m n))
         (r (modulo k len))
         (split (- len r))
         (rotated (append (drop flat split) (take flat split)))
         (result
           (let loop ((lst rotated) (acc '()))
             (if (null? lst)
                 (reverse acc)
                 (loop (drop lst n) (cons (take lst n) acc))))))
    result))
```

## Erlang

```erlang
-spec shift_grid(Grid :: [[integer()]], K :: integer()) -> [[integer()]].
-export([shift_grid/2]).

shift_grid(Grid, K) ->
    M = length(Grid),
    N = case Grid of
            [] -> 0;
            [Row|_] -> length(Row)
        end,
    Len = M * N,
    K1 = K rem Len,
    Flat = lists:flatten(Grid),
    Rotated = if
                  K1 == 0 ->
                      Flat;
                  true ->
                      SplitPos = Len - K1,
                      {Front, Back} = lists:split(SplitPos, Flat),
                      Back ++ Front
              end,
    rebuild(Rotated, N).

rebuild([], _N) -> [];
rebuild(List, N) ->
    {Row, Rest} = lists:split(N, List),
    [Row | rebuild(Rest, N)].
```

## Elixir

```elixir
defmodule Solution do
  @spec shift_grid(grid :: [[integer]], k :: integer) :: [[integer]]
  def shift_grid(grid, k) do
    m = length(grid)
    n = length(hd(grid))
    total = m * n
    k_mod = rem(k, total)

    if k_mod == 0 do
      grid
    else
      flat = Enum.flat_map(grid, & &1)
      {head, tail} = Enum.split(flat, total - k_mod)
      rotated = tail ++ head
      Enum.chunk_every(rotated, n)
    end
  end
end
```
