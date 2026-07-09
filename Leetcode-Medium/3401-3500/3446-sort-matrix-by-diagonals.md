# 3446. Sort Matrix by Diagonals

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> sortMatrix(vector<vector<int>>& grid) {
        int n = grid.size();
        unordered_map<int, vector<int>> diag;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                diag[i - j].push_back(grid[i][j]);
            }
        }
        for (auto& kv : diag) {
            if (kv.first >= 0)
                sort(kv.second.begin(), kv.second.end(), greater<int>());
            else
                sort(kv.second.begin(), kv.second.end());
        }
        unordered_map<int, int> idx;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                int d = i - j;
                grid[i][j] = diag[d][idx[d]++];
            }
        }
        return grid;
    }
};
```

## Java

```java
class Solution {
    public int[][] sortMatrix(int[][] grid) {
        int n = grid.length;
        java.util.Map<Integer, java.util.List<Integer>> diagMap = new java.util.HashMap<>();
        // Collect values per diagonal
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int diff = i - j;
                diagMap.computeIfAbsent(diff, k -> new java.util.ArrayList<>()).add(grid[i][j]);
            }
        }
        // Sort each diagonal according to the rule
        for (java.util.Map.Entry<Integer, java.util.List<Integer>> entry : diagMap.entrySet()) {
            java.util.List<Integer> list = entry.getValue();
            if (entry.getKey() >= 0) { // descending
                list.sort(java.util.Collections.reverseOrder());
            } else { // ascending
                java.util.Collections.sort(list);
            }
        }
        // Index map to track position while writing back
        java.util.Map<Integer, Integer> idxMap = new java.util.HashMap<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int diff = i - j;
                int idx = idxMap.getOrDefault(diff, 0);
                grid[i][j] = diagMap.get(diff).get(idx);
                idxMap.put(diff, idx + 1);
            }
        }
        return grid;
    }
}
```

## Python

```python
class Solution(object):
    def sortMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        diag = {}
        # Collect elements of each diagonal identified by i - j
        for i in range(n):
            for j in range(n):
                d = i - j
                if d not in diag:
                    diag[d] = []
                diag[d].append(grid[i][j])
        # Sort each diagonal according to the rule
        for d, vals in diag.items():
            if d >= 0:  # bottom-left triangle and main diagonal: non‑increasing
                vals.sort(reverse=True)
            else:       # top-right triangle: non‑decreasing
                vals.sort()
        # Refill the matrix using the sorted diagonals
        for i in range(n):
            for j in range(n):
                d = i - j
                grid[i][j] = diag[d].pop(0)
        return grid
```

## Python3

```python
from typing import List

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for d in range(-(n - 1), n):
            vals = []
            positions = []
            for i in range(n):
                j = i - d
                if 0 <= j < n:
                    vals.append(grid[i][j])
                    positions.append((i, j))
            if d >= 0:
                vals.sort(reverse=True)   # non‑increasing
            else:
                vals.sort()               # non‑decreasing
            for (i, j), v in zip(positions, vals):
                grid[i][j] = v
        return grid
```

## C

```c
#include <stdlib.h>
#include <string.h>

/* Comparator for ascending order */
static int cmp_asc(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return va - vb;
}

/* Comparator for descending order */
static int cmp_desc(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return vb - va;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** sortMatrix(int** grid, int gridSize, int* gridColSize, int* returnSize, int*** returnColumnSizes) {
    int n = gridSize;
    /* Allocate result matrix and copy original values */
    int **res = (int **)malloc(n * sizeof(int *));
    for (int i = 0; i < n; ++i) {
        res[i] = (int *)malloc(gridColSize[i] * sizeof(int));
        memcpy(res[i], grid[i], gridColSize[i] * sizeof(int));
    }

    /* Process each diagonal identified by offset = i - j */
    for (int offset = -(n - 1); offset <= n - 1; ++offset) {
        int start_i = offset >= 0 ? offset : 0;
        int start_j = offset >= 0 ? 0 : -offset;
        int len = n - (start_i > start_j ? start_i : start_j);
        if (len <= 1) continue;  /* single element diagonal is already ordered */

        int *vals = (int *)malloc(len * sizeof(int));
        int idx = 0;
        for (int i = start_i, j = start_j; i < n && j < n; ++i, ++j) {
            vals[idx++] = grid[i][j];
        }

        if (offset < 0) {
            qsort(vals, len, sizeof(int), cmp_asc);
        } else {
            qsort(vals, len, sizeof(int), cmp_desc);
        }

        idx = 0;
        for (int i = start_i, j = start_j; i < n && j < n; ++i, ++j) {
            res[i][j] = vals[idx++];
        }
        free(vals);
    }

    *returnSize = n;
    *returnColumnSizes = (int **)malloc(sizeof(int *));
    (*returnColumnSizes)[0] = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) {
        (*returnColumnSizes)[0][i] = gridColSize[i];
    }
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public int[][] SortMatrix(int[][] grid) {
        int n = grid.Length;
        var diagValues = new Dictionary<int, List<int>>();
        
        // Collect values for each diagonal identified by (col - row)
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < grid[i].Length; j++) {
                int d = j - i;
                if (!diagValues.ContainsKey(d)) diagValues[d] = new List<int>();
                diagValues[d].Add(grid[i][j]);
            }
        }
        
        // Sort each diagonal according to the rule and store in queues for easy retrieval
        var diagQueues = new Dictionary<int, Queue<int>>();
        foreach (var kvp in diagValues) {
            var list = kvp.Value;
            if (kvp.Key <= 0) {
                // Diagonals on or below main diagonal: non‑increasing order
                list.Sort((a, b) => b.CompareTo(a));
            } else {
                // Diagonals above main diagonal: non‑decreasing order
                list.Sort();
            }
            diagQueues[kvp.Key] = new Queue<int>(list);
        }
        
        // Write sorted values back into the matrix
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < grid[i].Length; j++) {
                int d = j - i;
                grid[i][j] = diagQueues[d].Dequeue();
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
 * @return {number[][]}
 */
var sortMatrix = function(grid) {
    const n = grid.length;
    // Diagonals starting from the first row (ascending order)
    for (let col = 0; col < n; col++) {
        let i = 0, j = col;
        const vals = [];
        while (i < n && j < n) {
            vals.push(grid[i][j]);
            i++; j++;
        }
        vals.sort((a, b) => a - b);
        i = 0; j = col;
        let idx = 0;
        while (i < n && j < n) {
            grid[i][j] = vals[idx++];
            i++; j++;
        }
    }
    // Diagonals starting from the first column (descending order), skip (0,0)
    for (let row = 1; row < n; row++) {
        let i = row, j = 0;
        const vals = [];
        while (i < n && j < n) {
            vals.push(grid[i][j]);
            i++; j++;
        }
        vals.sort((a, b) => b - a);
        i = row; j = 0;
        let idx = 0;
        while (i < n && j < n) {
            grid[i][j] = vals[idx++];
            i++; j++;
        }
    }
    return grid;
};
```

## Typescript

```typescript
function sortMatrix(grid: number[][]): number[][] {
    const n = grid.length;
    const diagMap = new Map<number, number[]>();

    // Collect values for each diagonal identified by (j - i)
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            const d = j - i;
            if (!diagMap.has(d)) diagMap.set(d, []);
            diagMap.get(d)!.push(grid[i][j]);
        }
    }

    // Sort each diagonal according to its region
    for (const [d, arr] of diagMap.entries()) {
        if (d > 0) {
            // top‑right triangle: non‑decreasing
            arr.sort((a, b) => a - b);
        } else {
            // bottom‑left triangle (including main): non‑increasing
            arr.sort((a, b) => b - a);
        }
    }

    // Refill the matrix using sorted values
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            const d = j - i;
            grid[i][j] = diagMap.get(d)!.shift()!;
        }
    }

    return grid;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer[][]
     */
    function sortMatrix($grid) {
        $n = count($grid);
        $diags = [];

        // Collect values for each diagonal identified by (col - row)
        for ($i = 0; $i < $n; ++$i) {
            for ($j = 0; $j < $n; ++$j) {
                $d = $j - $i;
                if (!isset($diags[$d])) {
                    $diags[$d] = [];
                }
                $diags[$d][] = $grid[$i][$j];
            }
        }

        // Sort each diagonal according to the rule
        foreach ($diags as $d => &$arr) {
            if ($d > 0) {
                sort($arr, SORT_NUMERIC);          // non‑decreasing
            } else {
                rsort($arr, SORT_NUMERIC);         // non‑increasing
            }
        }
        unset($arr);

        // Refill the matrix using sorted diagonals
        for ($i = 0; $i < $n; ++$i) {
            for ($j = 0; $j < $n; ++$j) {
                $d = $j - $i;
                $grid[$i][$j] = array_shift($diags[$d]);
            }
        }

        return $grid;
    }
}
```

## Swift

```swift
class Solution {
    func sortMatrix(_ grid: [[Int]]) -> [[Int]] {
        let n = grid.count
        var diagMap = [Int: [Int]]()
        
        // Collect values for each diagonal identified by offset i - j
        for i in 0..<n {
            for j in 0..<n {
                let off = i - j
                diagMap[off, default: []].append(grid[i][j])
            }
        }
        
        // Sort each diagonal: descending if offset >= 0, otherwise ascending
        for (off, _) in diagMap {
            if off >= 0 {
                diagMap[off]!.sort(by: >)
            } else {
                diagMap[off]!.sort()
            }
        }
        
        // Prepare indices to track current position within each sorted diagonal
        var idxMap = [Int: Int]()
        var result = grid
        
        for i in 0..<n {
            for j in 0..<n {
                let off = i - j
                let curIdx = idxMap[off] ?? 0
                result[i][j] = diagMap[off]![curIdx]
                idxMap[off] = curIdx + 1
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sortMatrix(grid: Array<IntArray>): Array<IntArray> {
        val n = grid.size
        if (n == 0) return grid
        val m = grid[0].size
        val diagMap = HashMap<Int, MutableList<Int>>()
        for (i in 0 until n) {
            for (j in 0 until m) {
                val key = i - j
                diagMap.computeIfAbsent(key) { mutableListOf() }.add(grid[i][j])
            }
        }
        for ((key, list) in diagMap) {
            if (key >= 0) {
                list.sortDescending()
            } else {
                list.sort()
            }
        }
        val idxMap = HashMap<Int, Int>()
        for (i in 0 until n) {
            for (j in 0 until m) {
                val key = i - j
                val list = diagMap[key]!!
                val idx = idxMap.getOrDefault(key, 0)
                grid[i][j] = list[idx]
                idxMap[key] = idx + 1
            }
        }
        return grid
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> sortMatrix(List<List<int>> grid) {
    int n = grid.length;
    Map<int, List<int>> diagMap = {};

    // Collect elements of each diagonal
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        int d = i - j;
        diagMap.putIfAbsent(d, () => []).add(grid[i][j]);
      }
    }

    // Sort each diagonal according to its position
    for (var entry in diagMap.entries) {
      int d = entry.key;
      List<int> lst = entry.value;
      if (d < 0) {
        lst.sort(); // ascending for upper‑right triangle
      } else {
        lst.sort((a, b) => b - a); // descending for lower‑left triangle (including main)
      }
    }

    // Place sorted values back into the matrix
    Map<int, int> idxMap = {};
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        int d = i - j;
        int idx = idxMap.putIfAbsent(d, () => 0);
        grid[i][j] = diagMap[d]![idx];
        idxMap[d] = idx + 1;
      }
    }

    return grid;
  }
}
```

## Golang

```go
func sortMatrix(grid [][]int) [][]int {
    n := len(grid)
    if n == 0 {
        return grid
    }
    // collect values per diagonal identified by i-j
    diags := make(map[int][]int)
    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            d := i - j
            diags[d] = append(diags[d], grid[i][j])
        }
    }
    // sort each diagonal according to its side
    for d, vals := range diags {
        if d >= 0 { // bottom-left triangle (including main) -> descending
            sort.Sort(sort.Reverse(sort.IntSlice(vals)))
        } else { // top-right triangle -> ascending
            sort.Ints(vals)
        }
        diags[d] = vals
    }
    // place sorted values back
    idx := make(map[int]int)
    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            d := i - j
            pos := idx[d]
            grid[i][j] = diags[d][pos]
            idx[d] = pos + 1
        }
    }
    return grid
}
```

## Ruby

```ruby
def sort_matrix(grid)
  n = grid.size
  diag = Hash.new { |h, k| h[k] = [] }

  (0...n).each do |i|
    (0...n).each do |j|
      d = i - j
      diag[d] << grid[i][j]
    end
  end

  diag.each do |d, arr|
    if d >= 0
      arr.sort!.reverse!
    else
      arr.sort!
    end
  end

  result = Array.new(n) { Array.new(n) }
  (0...n).each do |i|
    (0...n).each do |j|
      d = i - j
      result[i][j] = diag[d].shift
    end
  end

  result
end
```

## Scala

```scala
object Solution {
    def sortMatrix(grid: Array[Array[Int]]): Array[Array[Int]] = {
        val n = grid.length

        // Process diagonals starting from the first row
        for (col <- 0 until n) {
            var i = 0
            var j = col
            val vals = scala.collection.mutable.ArrayBuffer[Int]()
            while (i < n && j < n) {
                vals += grid(i)(j)
                i += 1
                j += 1
            }
            if (col == 0) {
                // bottom‑left triangle: non‑increasing order
                vals.sortInPlaceWith(_ > _)
            } else {
                // top‑right triangle: non‑decreasing order
                vals.sortInPlace()
            }
            i = 0
            j = col
            var idx = 0
            while (i < n && j < n) {
                grid(i)(j) = vals(idx)
                idx += 1
                i += 1
                j += 1
            }
        }

        // Process diagonals starting from the first column (excluding the main diagonal already handled)
        for (row <- 1 until n) {
            var i = row
            var j = 0
            val vals = scala.collection.mutable.ArrayBuffer[Int]()
            while (i < n && j < n) {
                vals += grid(i)(j)
                i += 1
                j += 1
            }
            // bottom‑left triangle: non‑increasing order
            vals.sortInPlaceWith(_ > _)

            i = row
            j = 0
            var idx = 0
            while (i < n && j < n) {
                grid(i)(j) = vals(idx)
                idx += 1
                i += 1
                j += 1
            }
        }

        grid
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sort_matrix(grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n = grid.len();
        if n == 0 {
            return grid;
        }
        // There are (2*n-1) possible diagonals identified by i - j ranging from -(n-1) to (n-1)
        let mut diags: Vec<Vec<i32>> = vec![Vec::new(); 2 * n - 1];
        for i in 0..n {
            for j in 0..n {
                let idx = i as isize - j as isize + (n as isize - 1);
                diags[idx as usize].push(grid[i][j]);
            }
        }
        // Sort each diagonal according to its position relative to the main diagonal
        for d in 0..diags.len() {
            let diff = d as isize - (n as isize - 1);
            if diff >= 0 {
                // non‑increasing order
                diags[d].sort_by(|a, b| b.cmp(a));
            } else {
                // non‑decreasing order
                diags[d].sort();
            }
        }
        let mut result = grid.clone();
        let mut pos = vec![0usize; diags.len()];
        for i in 0..n {
            for j in 0..n {
                let idx = i as isize - j as isize + (n as isize - 1);
                let p = pos[idx as usize];
                result[i][j] = diags[idx as usize][p];
                pos[idx as usize] += 1;
            }
        }
        result
    }
}
```

## Racket

```racket
(define/contract (sort-matrix grid)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  (let* ((n (length grid))
         (vec (list->vector (map list->vector grid))))
    ;; process diagonals starting from the first row (ascending order)
    (for ([col (in-range n)])
      (let loop ((i 0) (j col) (vals '()))
        (if (or (>= i n) (>= j n))
            (let ((sorted (sort vals <)))
              (let assign ((i2 0) (j2 col) (lst sorted))
                (when (and (< i2 n) (< j2 n) (pair? lst))
                  (vector-set! (vector-ref vec i2) j2 (car lst))
                  (assign (+ i2 1) (+ j2 1) (cdr lst)))))
            (loop (+ i 1) (+ j 1)
                  (cons (vector-ref (vector-ref vec i) j) vals)))))
    ;; process diagonals starting from the first column (excluding (0,0), descending order)
    (for ([row (in-range 1 n)])
      (let loop ((i row) (j 0) (vals '()))
        (if (or (>= i n) (>= j n))
            (let ((sorted (sort vals >)))
              (let assign ((i2 row) (j2 0) (lst sorted))
                (when (and (< i2 n) (< j2 n) (pair? lst))
                  (vector-set! (vector-ref vec i2) j2 (car lst))
                  (assign (+ i2 1) (+ j2 1) (cdr lst)))))
            (loop (+ i 1) (+ j 1)
                  (cons (vector-ref (vector-ref vec i) j) vals)))))
    ;; convert back to list of lists
    (for/list ([i (in-range n)])
      (vector->list (vector-ref vec i)))))
```

## Erlang

```erlang
-spec sort_matrix([[integer()]]) -> [[integer()]].
sort_matrix(Grid) ->
    N = length(Grid),
    DiagMap = collect_diagonals(Grid, N),
    SortedMap = sort_diagonals(DiagMap),
    fill_grid(N, SortedMap).

collect_diagonals(Grid, N) ->
    lists:foldl(fun(I, M) ->
        Row = lists:nth(I + 1, Grid),
        lists:foldl(fun(J, M2) ->
            Val = lists:nth(J + 1, Row),
            D = I - J,
            Updated = maps:get(D, M2, []) ++ [Val],
            maps:put(D, Updated, M2)
        end, M, lists:seq(0, N - 1))
    end, #{}, lists:seq(0, N - 1)).

sort_diagonals(Map) ->
    maps:fold(fun(D, List, Acc) ->
        Sorted = if D >= 0 -> lists:reverse(lists:sort(List));
                    true -> lists:sort(List)
                end,
        maps:put(D, Sorted, Acc)
    end, #{}, Map).

fill_grid(N, SortedMap) ->
    IdxMap0 = maps:fold(fun(D, _L, Acc) -> maps:put(D, 0, Acc) end, #{}, SortedMap),
    {Rows, _} = lists:foldl(fun(I, {AccRows, IdxMap}) ->
        RowIdx = I - 1,
        {NewRow, NewIdxMap} = lists:foldl(fun(J, {AccVals, IM}) ->
            ColIdx = J - 1,
            D = RowIdx - ColIdx,
            List = maps:get(D, SortedMap),
            Idx = maps:get(D, IM),
            Val = lists:nth(Idx + 1, List),
            UpdatedIM = maps:put(D, Idx + 1, IM),
            {AccVals ++ [Val], UpdatedIM}
        end, {[], IdxMap}, lists:seq(1, N)),
        {AccRows ++ [NewRow], NewIdxMap}
    end, {[], IdxMap0}, lists:seq(1, N)),
    Rows.
```

## Elixir

```elixir
defmodule Solution do
  @spec sort_matrix(grid :: [[integer]]) :: [[integer]]
  def sort_matrix(grid) do
    n = length(grid)

    diag_map =
      Enum.reduce(Enum.with_index(grid), %{}, fn {row, i}, acc ->
        Enum.reduce(Enum.with_index(row), acc, fn {val, j}, acc2 ->
          d = i - j
          Map.update(acc2, d, [val], &[val | &1])
        end)
      end)

    sorted_map =
      diag_map
      |> Enum.map(fn {d, vals} ->
        sorted_vals =
          if d >= 0 do
            Enum.sort(vals, &>=/2)
          else
            Enum.sort(vals, &<=/2)
          end

        {d, sorted_vals}
      end)
      |> Enum.into(%{})

    {result_rows, _} =
      Enum.map_reduce(0..(n - 1), sorted_map, fn i, map_acc ->
        {row_vals, new_map} =
          Enum.map_reduce(0..(n - 1), map_acc, fn j, m ->
            d = i - j
            [head | tail] = Map.get(m, d)
            {head, Map.put(m, d, tail)}
          end)

        {row_vals, new_map}
      end)

    result_rows
  end
end
```
