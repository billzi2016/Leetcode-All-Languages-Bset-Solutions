# 3122. Minimum Number of Operations to Satisfy Conditions

## Cpp

```cpp
class Solution {
public:
    int minimumOperations(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int operations = 0;
        for (int col = 0; col < n; ++col) {
            int freq[10] = {0};
            for (int row = 0; row < m; ++row) {
                ++freq[grid[row][col]];
            }
            int best = 0;
            for (int v = 0; v < 10; ++v) {
                if (freq[v] > best) best = freq[v];
            }
            operations += m - best;
        }
        return operations;
    }
};
```

## Java

```java
class Solution {
    public int minimumOperations(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int operations = 0;
        for (int col = 0; col < n; col++) {
            int[] freq = new int[10];
            int maxFreq = 0;
            for (int row = 0; row < m; row++) {
                int val = grid[row][col];
                freq[val]++;
                if (freq[val] > maxFreq) {
                    maxFreq = freq[val];
                }
            }
            operations += m - maxFreq;
        }
        return operations;
    }
}
```

## Python

```python
class Solution(object):
    def minimumOperations(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        ops = 0
        for j in range(n):
            freq = [0] * 10  # values are between 0 and 9 inclusive
            max_cnt = 0
            for i in range(m):
                val = grid[i][j]
                freq[val] += 1
                if freq[val] > max_cnt:
                    max_cnt = freq[val]
            ops += m - max_cnt
        return ops
```

## Python3

```python
from typing import List

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        ops = 0
        for col in range(n):
            freq = [0] * 10  # values are within [0,9]
            for row in range(m):
                val = grid[row][col]
                if 0 <= val < 10:
                    freq[val] += 1
                else:
                    # fallback for unexpected larger values
                    # expand frequency list dynamically (rare given constraints)
                    # using dict would be simpler, but this path is unlikely.
                    pass
            max_freq = max(freq)
            ops += m - max_freq
        return ops
```

## C

```c
int minimumOperations(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize;
    if (m == 0) return 0;
    int n = gridColSize[0];
    int operations = 0;
    for (int j = 0; j < n; ++j) {
        int freq[10] = {0};
        for (int i = 0; i < m; ++i) {
            int val = grid[i][j];
            if (val >= 0 && val <= 9) {
                ++freq[val];
            }
        }
        int maxFreq = 0;
        for (int v = 0; v < 10; ++v) {
            if (freq[v] > maxFreq) maxFreq = freq[v];
        }
        operations += m - maxFreq;
    }
    return operations;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumOperations(int[][] grid) {
        int m = grid.Length;
        if (m == 0) return 0;
        int n = grid[0].Length;
        int operations = 0;

        for (int col = 0; col < n; col++) {
            int[] freq = new int[10];
            int maxFreq = 0;
            for (int row = 0; row < m; row++) {
                int val = grid[row][col];
                freq[val]++;
                if (freq[val] > maxFreq) maxFreq = freq[val];
            }
            operations += m - maxFreq;
        }

        return operations;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minimumOperations = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    let totalOps = 0;
    for (let col = 0; col < n; col++) {
        const freq = new Array(10).fill(0);
        for (let row = 0; row < m; row++) {
            freq[grid[row][col]]++;
        }
        let maxFreq = 0;
        for (let v = 0; v < 10; v++) {
            if (freq[v] > maxFreq) maxFreq = freq[v];
        }
        totalOps += m - maxFreq;
    }
    return totalOps;
};
```

## Typescript

```typescript
function minimumOperations(grid: number[][]): number {
    const m = grid.length;
    if (m === 0) return 0;
    const n = grid[0].length;
    let operations = 0;

    for (let col = 0; col < n; col++) {
        const freq = new Array(10).fill(0);
        for (let row = 0; row < m; row++) {
            const val = grid[row][col];
            freq[val]++;
        }
        let maxFreq = 0;
        for (let v = 0; v < 10; v++) {
            if (freq[v] > maxFreq) maxFreq = freq[v];
        }
        operations += m - maxFreq;
    }

    return operations;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minimumOperations($grid) {
        $m = count($grid);
        if ($m == 0) return 0;
        $n = count($grid[0]);
        $operations = 0;

        for ($j = 0; $j < $n; $j++) {
            $freq = array_fill(0, 10, 0);
            for ($i = 0; $i < $m; $i++) {
                $val = $grid[$i][$j];
                $freq[$val]++;
            }
            $maxFreq = max($freq);
            $operations += $m - $maxFreq;
        }

        return $operations;
    }
}
```

## Swift

```swift
class Solution {
    func minimumOperations(_ grid: [[Int]]) -> Int {
        let m = grid.count
        guard m > 0 else { return 0 }
        let n = grid[0].count
        var operations = 0
        
        for col in 0..<n {
            var freq = [Int](repeating: 0, count: 10)
            for row in 0..<m {
                let val = grid[row][col]
                freq[val] += 1
            }
            var maxFreq = 0
            for f in freq {
                if f > maxFreq { maxFreq = f }
            }
            operations += m - maxFreq
        }
        
        return operations
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumOperations(grid: Array<IntArray>): Int {
        val m = grid.size
        if (m == 0) return 0
        val n = grid[0].size
        var ops = 0
        for (j in 0 until n) {
            val cnt = IntArray(10)
            for (i in 0 until m) {
                val v = grid[i][j]
                if (v in 0..9) {
                    cnt[v]++
                } else {
                    // For values outside 0-9, expand counting using a map
                    // but per constraints this branch won't be hit.
                }
            }
            var maxFreq = 0
            for (c in cnt) if (c > maxFreq) maxFreq = c
            ops += m - maxFreq
        }
        return ops
    }
}
```

## Dart

```dart
class Solution {
  int minimumOperations(List<List<int>> grid) {
    int m = grid.length;
    if (m == 0) return 0;
    int n = grid[0].length;
    int total = 0;
    for (int j = 0; j < n; ++j) {
      List<int> freq = List.filled(10, 0);
      for (int i = 0; i < m; ++i) {
        int val = grid[i][j];
        freq[val]++;
      }
      int maxFreq = 0;
      for (int cnt in freq) {
        if (cnt > maxFreq) maxFreq = cnt;
      }
      total += m - maxFreq;
    }
    return total;
  }
}
```

## Golang

```go
func minimumOperations(grid [][]int) int {
    m := len(grid)
    if m == 0 {
        return 0
    }
    n := len(grid[0])
    ops := 0
    for col := 0; col < n; col++ {
        var freq [10]int
        maxFreq := 0
        for row := 0; row < m; row++ {
            v := grid[row][col]
            freq[v]++
            if freq[v] > maxFreq {
                maxFreq = freq[v]
            }
        }
        ops += m - maxFreq
    }
    return ops
}
```

## Ruby

```ruby
def minimum_operations(grid)
  m = grid.size
  n = grid[0].size
  total = 0
  (0...n).each do |j|
    freq = Hash.new(0)
    (0...m).each do |i|
      freq[grid[i][j]] += 1
    end
    max_freq = freq.values.max
    total += m - max_freq
  end
  total
end
```

## Scala

```scala
object Solution {
    def minimumOperations(grid: Array[Array[Int]]): Int = {
        val m = grid.length
        if (m == 0) return 0
        val n = grid(0).length
        var totalOps = 0
        for (col <- 0 until n) {
            val freq = new Array[Int](10)
            var maxFreq = 0
            var row = 0
            while (row < m) {
                val v = grid(row)(col)
                freq(v) += 1
                if (freq(v) > maxFreq) maxFreq = freq(v)
                row += 1
            }
            totalOps += m - maxFreq
        }
        totalOps
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_operations(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        if m == 0 {
            return 0;
        }
        let n = grid[0].len();
        let mut ops: i32 = 0;
        for col in 0..n {
            let mut cnt = [0i32; 10];
            let mut maxc = 0i32;
            for row in 0..m {
                let val = grid[row][col] as usize;
                if val < 10 {
                    cnt[val] += 1;
                    if cnt[val] > maxc {
                        maxc = cnt[val];
                    }
                }
            }
            ops += (m as i32) - maxc;
        }
        ops
    }
}
```

## Racket

```racket
(define/contract (minimum-operations grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((m (length grid))
         (n (if (> m 0) (length (car grid)) 0))
         ;; compute cost vectors for each column
         (col-costs
          (for/list ([j (in-range n)])
            (let ((freq (make-vector 10 0)))
              (for ([row grid])
                (let ((v (list-ref row j)))
                  (when (and (>= v 0) (< v 10))
                    (vector-set! freq v (+ (vector-ref freq v) 1)))))
              (let ((c (make-vector 11 0))) ; 0-9 digits, 10 = dummy
                (for ([d (in-range 10)])
                  (vector-set! c d (- m (vector-ref freq d))))
                (vector-set! c 10 m)
                c))))
         ;; helper to find min over all entries except excluded index
         (min-excluding
          (lambda (vec excl)
            (let ((len (vector-length vec))
                  (best +inf.0))
              (let loop ((i 0) (b best))
                (if (= i len)
                    b
                    (if (= i excl)
                        (loop (+ i 1) b)
                        (let ((val (vector-ref vec i)))
                          (loop (+ i 1) (if (< val b) val b))))))))))
    (if (= n 0)
        0
        (let loop ((idx 0) (prev #f))
          (if (= idx n)
              (apply min (vector->list prev))
              (let* ((cur-cost (list-ref col-costs idx))
                     (cur-dp (make-vector 11 0)))
                (if (= idx 0)
                    (for ([v (in-range 11)])
                      (vector-set! cur-dp v (vector-ref cur-cost v)))
                    (for ([v (in-range 11)])
                      (let ((best (min-excluding prev v)))
                        (vector-set! cur-dp v (+ (vector-ref cur-cost v) best)))))
                (loop (+ idx 1) cur-dp)))))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_operations/1]).

-spec minimum_operations(Grid :: [[integer()]]) -> integer().
minimum_operations(Grid) ->
    Columns = transpose(Grid),
    NumRows = length(Grid),
    lists:foldl(fun(Col, Acc) ->
        {_Map, Max} = lists:foldl(
            fun(V, {M, CurMax}) ->
                Cnt = maps:get(V, M, 0) + 1,
                NewM = maps:put(V, Cnt, M),
                NewMax = if Cnt > CurMax -> Cnt; true -> CurMax end,
                {NewM, NewMax}
            end,
            {#{}, 0},
            Col
        ),
        Acc + (NumRows - Max)
    end, 0, Columns).

transpose([]) -> [];
transpose([[]|_]) -> [];
transpose(Matrix) ->
    FirstCol = [hd(Row) || Row <- Matrix],
    RestRows = [tl(Row) || Row <- Matrix],
    [FirstCol | transpose(RestRows)].
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_operations(grid :: [[integer]]) :: integer
  def minimum_operations(grid) do
    m = length(grid)
    n = length(List.first(grid))

    # Convert rows to tuples for O(1) access, then pack all rows into a tuple
    rows =
      grid
      |> Enum.map(&List.to_tuple/1)
      |> List.to_tuple()

    max_i = div(m - 1, 2)
    max_j = div(n - 1, 2)

    Enum.reduce(0..max_i, 0, fn i, acc ->
      Enum.reduce(0..max_j, acc, fn j, inner_acc ->
        positions = [
          {i, j},
          {i, n - 1 - j},
          {m - 1 - i, j},
          {m - 1 - i, n - 1 - j}
        ]
        |> Enum.uniq()

        values =
          Enum.map(positions, fn {x, y} ->
            row = elem(rows, x)
            elem(row, y)
          end)

        freq_map =
          Enum.reduce(values, %{}, fn v, m ->
            Map.update(m, v, 1, &(&1 + 1))
          end)

        max_freq = freq_map |> Map.values() |> Enum.max()
        inner_acc + (length(values) - max_freq)
      end)
    end)
  end
end
```
