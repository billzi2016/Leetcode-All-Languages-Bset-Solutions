# 1329. Sort the Matrix Diagonally

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> diagonalSort(vector<vector<int>>& mat) {
        int m = mat.size();
        int n = mat[0].size();
        unordered_map<int, vector<int>> diag;
        // Collect values for each diagonal identified by (i - j)
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                diag[i - j].push_back(mat[i][j]);
            }
        }
        // Sort each diagonal's values
        for (auto& kv : diag) {
            sort(kv.second.begin(), kv.second.end());
        }
        // Index to track the next element to place from each sorted diagonal
        unordered_map<int, int> idx;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int key = i - j;
                mat[i][j] = diag[key][idx[key]++];
            }
        }
        return mat;
    }
};
```

## Java

```java
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

class Solution {
    public int[][] diagonalSort(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;
        Map<Integer, PriorityQueue<Integer>> map = new HashMap<>();
        
        // Collect values of each diagonal
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int key = i - j;
                map.computeIfAbsent(key, k -> new PriorityQueue<>()).add(mat[i][j]);
            }
        }
        
        // Write back sorted values
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int key = i - j;
                mat[i][j] = map.get(key).poll();
            }
        }
        
        return mat;
    }
}
```

## Python

```python
class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import defaultdict

        m, n = len(mat), len(mat[0])
        diag = defaultdict(list)

        # Collect all elements of each diagonal
        for i in range(m):
            for j in range(n):
                diag[i - j].append(mat[i][j])

        # Sort each diagonal in descending order so we can pop smallest efficiently
        for key in diag:
            diag[key].sort(reverse=True)

        # Write back the sorted values
        for i in range(m):
            for j in range(n):
                mat[i][j] = diag[i - j].pop()

        return mat
```

## Python3

```python
from typing import List
from collections import defaultdict

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        diag = defaultdict(list)
        for i in range(m):
            for j in range(n):
                diag[i - j].append(mat[i][j])
        for k in diag:
            diag[k].sort()
        pos = {k: 0 for k in diag}
        for i in range(m):
            for j in range(n):
                d = i - j
                mat[i][j] = diag[d][pos[d]]
                pos[d] += 1
        return mat
```

## C

```c
#include <stdlib.h>
#include <string.h>

/* Comparator for qsort */
static int cmp_int(const void *a, const void *b) {
    return (*(const int *)a) - (*(const int *)b);
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** diagonalSort(int** mat, int matSize, int* matColSize, int* returnSize, int*** returnColumnSizes) {
    if (matSize == 0 || matColSize == NULL) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }

    int rows = matSize;
    int cols = *matColSize;

    /* Allocate result matrix and copy original values */
    int **res = (int **)malloc(rows * sizeof(int *));
    for (int i = 0; i < rows; ++i) {
        res[i] = (int *)malloc(cols * sizeof(int));
        memcpy(res[i], mat[i], cols * sizeof(int));
    }

    /* Process diagonals starting from first row */
    for (int c = 0; c < cols; ++c) {
        int r = 0, cc = c;
        int len = 0;
        int temp[101];   // max possible length is min(rows, cols) <= 100
        while (r + len < rows && cc + len < cols) {
            temp[len] = res[r + len][cc + len];
            ++len;
        }
        qsort(temp, len, sizeof(int), cmp_int);
        for (int k = 0; k < len; ++k) {
            res[r + k][cc + k] = temp[k];
        }
    }

    /* Process diagonals starting from first column (excluding the top-left cell already handled) */
    for (int r = 1; r < rows; ++r) {
        int rr = r, c = 0;
        int len = 0;
        int temp[101];
        while (rr + len < rows && c + len < cols) {
            temp[len] = res[rr + len][c + len];
            ++len;
        }
        qsort(temp, len, sizeof(int), cmp_int);
        for (int k = 0; k < len; ++k) {
            res[rr + k][c + k] = temp[k];
        }
    }

    *returnSize = rows;
    *returnColumnSizes = (int **)malloc(rows * sizeof(int *));
    int *colSizes = (int *)malloc(rows * sizeof(int));
    for (int i = 0; i < rows; ++i) {
        colSizes[i] = cols;
    }
    **returnColumnSizes = colSizes;

    return res;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[][] DiagonalSort(int[][] mat) {
        int m = mat.Length;
        int n = mat[0].Length;
        var diagMap = new Dictionary<int, List<int>>();
        
        // Collect values for each diagonal identified by (i - j)
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int key = i - j;
                if (!diagMap.ContainsKey(key)) {
                    diagMap[key] = new List<int>();
                }
                diagMap[key].Add(mat[i][j]);
            }
        }
        
        // Sort each diagonal's list in ascending order
        foreach (var kvp in diagMap) {
            kvp.Value.Sort();
        }
        
        // Pointers to current index within each sorted diagonal list
        var idxMap = new Dictionary<int, int>();
        foreach (int key in diagMap.Keys) {
            idxMap[key] = 0;
        }
        
        // Reassign sorted values back to the matrix
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int key = i - j;
                mat[i][j] = diagMap[key][idxMap[key]];
                idxMap[key]++;
            }
        }
        
        return mat;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} mat
 * @return {number[][]}
 */
var diagonalSort = function(mat) {
    const m = mat.length;
    const n = mat[0].length;
    const diagMap = new Map();
    
    // Collect values for each diagonal identified by (i - j)
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            const key = i - j;
            if (!diagMap.has(key)) diagMap.set(key, []);
            diagMap.get(key).push(mat[i][j]);
        }
    }
    
    // Sort each diagonal in descending order so we can pop smallest later
    for (const arr of diagMap.values()) {
        arr.sort((a, b) => b - a);
    }
    
    // Write back sorted values to the matrix
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            const key = i - j;
            mat[i][j] = diagMap.get(key).pop();
        }
    }
    
    return mat;
};
```

## Typescript

```typescript
function diagonalSort(mat: number[][]): number[][] {
    const m = mat.length;
    const n = mat[0].length;
    const diagMap = new Map<number, number[]>();
    
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            const key = i - j;
            let arr = diagMap.get(key);
            if (!arr) {
                arr = [];
                diagMap.set(key, arr);
            }
            arr.push(mat[i][j]);
        }
    }
    
    for (const arr of diagMap.values()) {
        arr.sort((a, b) => b - a); // descending
    }
    
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            const key = i - j;
            const arr = diagMap.get(key)!;
            mat[i][j] = arr.pop()!;
        }
    }
    
    return mat;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $mat
     * @return Integer[][]
     */
    function diagonalSort($mat) {
        $m = count($mat);
        if ($m == 0) return $mat;
        $n = count($mat[0]);
        $diag = [];

        // Collect values for each diagonal identified by (i - j)
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $key = $i - $j;
                if (!isset($diag[$key])) {
                    $diag[$key] = [];
                }
                $diag[$key][] = $mat[$i][$j];
            }
        }

        // Sort each diagonal and reverse for efficient pop
        foreach ($diag as $key => $arr) {
            sort($arr);
            $diag[$key] = array_reverse($arr);
        }

        // Write sorted values back to matrix
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $key = $i - $j;
                $mat[$i][$j] = array_pop($diag[$key]);
            }
        }

        return $mat;
    }
}
```

## Swift

```swift
class Solution {
    func diagonalSort(_ mat: [[Int]]) -> [[Int]] {
        let m = mat.count
        guard m > 0 else { return mat }
        let n = mat[0].count
        var diagMap = [Int: [Int]]()
        
        // Collect values for each diagonal identified by (i - j)
        for i in 0..<m {
            for j in 0..<n {
                let key = i - j
                diagMap[key, default: []].append(mat[i][j])
            }
        }
        
        // Sort each diagonal's values in descending order so we can pop the smallest efficiently
        for (key, var arr) in diagMap {
            arr.sort(by: >)
            diagMap[key] = arr
        }
        
        var result = mat
        // Reassign sorted values back to their positions
        for i in 0..<m {
            for j in 0..<n {
                let key = i - j
                if var arr = diagMap[key] {
                    let val = arr.removeLast()
                    result[i][j] = val
                    diagMap[key] = arr
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
    fun diagonalSort(mat: Array<IntArray>): Array<IntArray> {
        val m = mat.size
        val n = mat[0].size
        val diagMap = HashMap<Int, MutableList<Int>>()

        // Collect values for each diagonal identified by (i - j)
        for (i in 0 until m) {
            for (j in 0 until n) {
                val key = i - j
                val list = diagMap.getOrPut(key) { mutableListOf() }
                list.add(mat[i][j])
            }
        }

        // Sort each diagonal's values in ascending order
        for (list in diagMap.values) {
            list.sort()
        }

        // Reassign sorted values back to the matrix
        val indexMap = HashMap<Int, Int>()
        for (i in 0 until m) {
            for (j in 0 until n) {
                val key = i - j
                val idx = indexMap.getOrDefault(key, 0)
                mat[i][j] = diagMap[key]!![idx]
                indexMap[key] = idx + 1
            }
        }

        return mat
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> diagonalSort(List<List<int>> mat) {
    int m = mat.length;
    int n = mat[0].length;
    Map<int, List<int>> diagMap = {};

    // Collect elements of each diagonal
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        int key = i - j;
        diagMap.putIfAbsent(key, () => []).add(mat[i][j]);
      }
    }

    // Sort each diagonal in descending order so we can pop smallest from the end
    for (var list in diagMap.values) {
      list.sort((a, b) => b.compareTo(a));
    }

    // Write back sorted values to matrix
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        int key = i - j;
        List<int> list = diagMap[key]!;
        mat[i][j] = list.removeLast();
      }
    }

    return mat;
  }
}
```

## Golang

```go
import "sort"

func diagonalSort(mat [][]int) [][]int {
    m := len(mat)
    if m == 0 {
        return mat
    }
    n := len(mat[0])

    diagMap := make(map[int][]int)

    // Collect values for each diagonal identified by i-j
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            diff := i - j
            diagMap[diff] = append(diagMap[diff], mat[i][j])
        }
    }

    // Sort each diagonal's values in ascending order
    for k := range diagMap {
        sort.Ints(diagMap[k])
    }

    // Write back sorted values to the matrix
    pos := make(map[int]int) // current index for each diagonal
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            diff := i - j
            idx := pos[diff]
            mat[i][j] = diagMap[diff][idx]
            pos[diff] = idx + 1
        }
    }

    return mat
}
```

## Ruby

```ruby
# @param {Integer[][]} mat
# @return {Integer[][]}
def diagonal_sort(mat)
  m = mat.size
  n = mat[0].size
  diag = Hash.new { |h, k| h[k] = [] }

  (0...m).each do |i|
    (0...n).each do |j|
      diag[i - j] << mat[i][j]
    end
  end

  diag.each_value { |arr| arr.sort!.reverse! }

  (0...m).each do |i|
    (0...n).each do |j|
      mat[i][j] = diag[i - j].pop
    end
  end

  mat
end
```

## Scala

```scala
object Solution {
    def diagonalSort(mat: Array[Array[Int]]): Array[Array[Int]] = {
        val m = mat.length
        val n = mat(0).length
        import scala.collection.mutable.{Map => MutableMap, ArrayBuffer}
        val diagMap = MutableMap.empty[Int, ArrayBuffer[Int]]
        for (i <- 0 until m) {
            for (j <- 0 until n) {
                val key = i - j
                val buf = diagMap.getOrElseUpdate(key, ArrayBuffer[Int]())
                buf += mat(i)(j)
            }
        }
        // sort each diagonal buffer
        for ((_, buf) <- diagMap) {
            val sorted = buf.sorted
            buf.clear()
            buf ++= sorted
        }
        val idxMap = MutableMap.empty[Int, Int].withDefaultValue(0)
        for (i <- 0 until m) {
            for (j <- 0 until n) {
                val key = i - j
                val buf = diagMap(key)
                mat(i)(j) = buf(idxMap(key))
                idxMap(key) += 1
            }
        }
        mat
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn diagonal_sort(mut mat: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let m = mat.len();
        if m == 0 {
            return mat;
        }
        let n = mat[0].len();

        let mut map: HashMap<i32, Vec<i32>> = HashMap::new();

        for i in 0..m {
            for j in 0..n {
                let key = i as i32 - j as i32;
                map.entry(key).or_insert_with(Vec::new).push(mat[i][j]);
            }
        }

        for vec in map.values_mut() {
            vec.sort_by(|a, b| b.cmp(a)); // descending
        }

        for i in 0..m {
            for j in 0..n {
                let key = i as i32 - j as i32;
                if let Some(v) = map.get_mut(&key) {
                    mat[i][j] = v.pop().unwrap();
                }
            }
        }

        mat
    }
}
```

## Racket

```racket
(define/contract (diagonal-sort mat)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  (let* ((m (length mat))
         (n (if (= m 0) 0 (length (car mat))))
         ;; mutable grid for easy updates
         (grid (list->vector
                (map (lambda (row) (list->vector row)) mat)))
         (ht (make-hash))) ; key -> list of values on that diagonal

    ;; collect all elements per diagonal
    (for ([i (in-range m)])
      (for ([j (in-range n)])
        (let* ((key (- i j))
               (val (vector-ref (vector-ref grid i) j)))
          (hash-update! ht key (lambda (lst) (cons val lst)) '()))))

    ;; sort each diagonal and store as vector
    (define sorted-ht (make-hash))
    (for ([k (in-hash-keys ht)])
      (let* ((lst (hash-ref ht k))
             (sorted (sort lst <))
             (vec (list->vector sorted)))
        (hash-set! sorted-ht k vec)))

    ;; position tracker for each diagonal
    (define pos-ht (make-hash))

    ;; write back sorted values into grid
    (for ([i (in-range m)])
      (for ([j (in-range n)])
        (let* ((key (- i j))
               (vec (hash-ref sorted-ht key))
               (idx (hash-ref pos-ht key 0))
               (val (vector-ref vec idx)))
          (vector-set! (vector-ref grid i) j val)
          (hash-set! pos-ht key (+ idx 1)))))

    ;; convert mutable vectors back to immutable lists
    (map vector->list (vector->list grid))))
```

## Erlang

```erlang
-module(solution).
-export([diagonal_sort/1]).

-spec diagonal_sort(Mat :: [[integer()]]) -> [[integer()]].
diagonal_sort(Mat) ->
    Map0 = collect_diagonals(Mat, 0, #{}),
    SortedMap = maps:map(fun(_K, L) -> lists:sort(L) end, Map0),
    {Result, _} = rebuild_rows(Mat, 0, SortedMap),
    Result.

collect_diagonals([], _I, Map) ->
    Map;
collect_diagonals([Row|Rest], I, Map) ->
    NewMap = collect_row(Row, I, 0, Map),
    collect_diagonals(Rest, I + 1, NewMap).

collect_row([], _I, _J, Map) ->
    Map;
collect_row([Val|Vals], I, J, Map) ->
    Key = I - J,
    UpdatedMap = case maps:find(Key, Map) of
        {ok, List} -> maps:put(Key, [Val | List], Map);
        error      -> maps:put(Key, [Val], Map)
    end,
    collect_row(Vals, I, J + 1, UpdatedMap).

rebuild_rows([], _I, Map) ->
    {[], Map};
rebuild_rows([Row|RestRows], I, Map) ->
    {NewRow, NewMap} = rebuild_row(Row, I, 0, Map),
    {RestNewRows, FinalMap} = rebuild_rows(RestRows, I + 1, NewMap),
    {[NewRow | RestNewRows], FinalMap}.

rebuild_row([], _I, _J, Map) ->
    {[], Map};
rebuild_row([_Old|Vals], I, J, Map) ->
    Key = I - J,
    case maps:find(Key, Map) of
        {ok, [H | T]} ->
            UpdatedMap = maps:put(Key, T, Map),
            {RestRow, FinalMap} = rebuild_row(Vals, I, J + 1, UpdatedMap),
            {[H | RestRow], FinalMap};
        error ->
            erlang:error(bad_diagonal)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec diagonal_sort(mat :: [[integer]]) :: [[integer]]
  def diagonal_sort(mat) do
    m = length(mat)
    n = if m == 0, do: 0, else: mat |> hd() |> length()

    # Collect values for each diagonal identified by i - j
    diag_map =
      Enum.reduce(Enum.with_index(mat), %{}, fn {row, i}, acc ->
        Enum.reduce(Enum.with_index(row), acc, fn {val, j}, a2 ->
          diff = i - j
          Map.update(a2, diff, [val], fn list -> [val | list] end)
        end)
      end)

    # Sort each diagonal ascending
    sorted_map =
      diag_map
      |> Enum.map(fn {k, lst} -> {k, Enum.sort(lst)} end)
      |> Enum.into(%{})

    # Reconstruct the matrix using the sorted diagonals
    {_final_map, rows_rev} =
      Enum.reduce(0..(m - 1), {sorted_map, []}, fn i, {cur_map, rows_acc} ->
        {new_map, row_rev} =
          Enum.reduce(0..(n - 1), {cur_map, []}, fn j, {cmap, row_acc} ->
            diff = i - j
            [val | rest] = Map.get(cmap, diff)
            {Map.put(cmap, diff, rest), [val | row_acc]}
          end)

        {new_map, [Enum.reverse(row_rev) | rows_acc]}
      end)

    Enum.reverse(rows_rev)
  end
end
```
