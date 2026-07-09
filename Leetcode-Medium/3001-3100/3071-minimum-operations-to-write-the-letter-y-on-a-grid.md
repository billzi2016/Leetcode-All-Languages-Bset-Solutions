# 3071. Minimum Operations to Write the Letter Y on a Grid

## Cpp

```cpp
class Solution {
public:
    int minimumOperationsToWriteY(vector<vector<int>>& grid) {
        int n = grid.size();
        int mid = n / 2;
        vector<int> cntY(3, 0), cntNon(3, 0);
        int sizeY = 0;
        for (int r = 0; r < n; ++r) {
            for (int c = 0; c < n; ++c) {
                bool isY = false;
                if (r < mid) {
                    if (c == r || c == n - 1 - r) isY = true;
                } else {
                    if (c == mid) isY = true;
                }
                if (isY) {
                    cntY[grid[r][c]]++;
                    ++sizeY;
                } else {
                    cntNon[grid[r][c]]++;
                }
            }
        }
        int sizeNon = n * n - sizeY;
        int ans = INT_MAX;
        for (int a = 0; a < 3; ++a) {
            for (int b = 0; b < 3; ++b) {
                int ops = (sizeY - cntY[a]) + (sizeNon - cntNon[b]);
                ans = min(ans, ops);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minimumOperationsToWriteY(int[][] grid) {
        int n = grid.length;
        int mid = n / 2;
        boolean[][] isY = new boolean[n][n];
        // Upper part including middle row: diagonals
        for (int i = 0; i <= mid; i++) {
            isY[i][i] = true;                     // main diagonal
            isY[i][n - 1 - i] = true;             // anti-diagonal
        }
        // Lower part including middle row: middle column
        for (int i = mid; i < n; i++) {
            isY[i][mid] = true;
        }

        int[] cntY = new int[3];
        int[] cntN = new int[3];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int val = grid[i][j];
                if (isY[i][j]) {
                    cntY[val]++;
                } else {
                    cntN[val]++;
                }
            }
        }

        int maxKeep = 0;
        for (int vY = 0; vY < 3; vY++) {
            for (int vN = 0; vN < 3; vN++) {
                if (vY == vN) continue;
                int keep = cntY[vY] + cntN[vN];
                if (keep > maxKeep) maxKeep = keep;
            }
        }

        return n * n - maxKeep;
    }
}
```

## Python

```python
class Solution(object):
    def minimumOperationsToWriteY(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        center = n // 2
        cnt_y = [0, 0, 0]
        cnt_n = [0, 0, 0]
        total_y = 0
        for r in range(n):
            for c in range(n):
                val = grid[r][c]
                isY = (r == c and r <= center) or (r + c == n - 1 and r <= center) or (c == center and r >= center)
                if isY:
                    cnt_y[val] += 1
                    total_y += 1
                else:
                    cnt_n[val] += 1
        total_n = n * n - total_y
        best = float('inf')
        for a in range(3):
            for b in range(3):
                if a == b:
                    continue
                ops = (total_y - cnt_y[a]) + (total_n - cnt_n[b])
                if ops < best:
                    best = ops
        return best
```

## Python3

```python
class Solution:
    def minimumOperationsToWriteY(self, grid):
        n = len(grid)
        mid = n // 2
        countY = [0, 0, 0]
        countNon = [0, 0, 0]

        for i in range(n):
            for j in range(n):
                # check if (i,j) belongs to Y
                belongs = False
                if i <= mid:
                    if j == i or j == n - 1 - i:
                        belongs = True
                else:
                    if j == mid:
                        belongs = True

                val = grid[i][j]
                if belongs:
                    countY[val] += 1
                else:
                    countNon[val] += 1

        max_keep = 0
        for a in range(3):
            for b in range(3):
                if a == b:
                    continue
                keep = countY[a] + countNon[b]
                if keep > max_keep:
                    max_keep = keep

        total_cells = n * n
        return total_cells - max_keep
```

## C

```c
int minimumOperationsToWriteY(int** grid, int gridSize, int* gridColSize) {
    int n = gridSize;
    int mid = n / 2;
    int cntY[3] = {0, 0, 0};
    int cntN[3] = {0, 0, 0};

    for (int r = 0; r < n; ++r) {
        for (int c = 0; c < n; ++c) {
            int val = grid[r][c];
            int isY = 0;
            if ((r == c && r <= mid) ||
                (r + c == n - 1 && r <= mid) ||
                (c == mid && r >= mid)) {
                isY = 1;
            }
            if (isY) {
                ++cntY[val];
            } else {
                ++cntN[val];
            }
        }
    }

    int totalY = cntY[0] + cntY[1] + cntY[2];
    int totalN = n * n - totalY;

    int best = n * n; // upper bound
    for (int a = 0; a < 3; ++a) {
        for (int b = 0; b < 3; ++b) {
            int ops = (totalY - cntY[a]) + (totalN - cntN[b]);
            if (ops < best) best = ops;
        }
    }
    return best;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumOperationsToWriteY(int[][] grid) {
        int n = grid.Length;
        int mid = n / 2;
        int totalY = 0, totalNonY = 0;
        int[] yCnt = new int[3];
        int[] nonCnt = new int[3];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                bool isY = false;
                if (i <= mid && i == j) {
                    isY = true;
                } else if (i <= mid && i + j == n - 1) {
                    isY = true;
                } else if (j == mid && i >= mid) {
                    isY = true;
                }

                int val = grid[i][j];
                if (isY) {
                    totalY++;
                    yCnt[val]++;
                } else {
                    totalNonY++;
                    nonCnt[val]++;
                }
            }
        }

        int minOps = int.MaxValue;
        for (int v = 0; v < 3; v++) {
            for (int w = 0; w < 3; w++) {
                if (v == w) continue;
                int ops = (totalY - yCnt[v]) + (totalNonY - nonCnt[w]);
                if (ops < minOps) minOps = ops;
            }
        }

        return minOps;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minimumOperationsToWriteY = function(grid) {
    const n = grid.length;
    const mid = Math.floor(n / 2);
    const freqY = [0, 0, 0];
    const freqN = [0, 0, 0];
    let sizeY = 0, sizeN = 0;
    
    for (let r = 0; r < n; ++r) {
        for (let c = 0; c < n; ++c) {
            const val = grid[r][c];
            let isY = false;
            if (r <= mid && (c === r || c === n - 1 - r)) {
                isY = true;
            } else if (r >= mid && c === mid) {
                isY = true;
            }
            if (isY) {
                freqY[val]++;
                sizeY++;
            } else {
                freqN[val]++;
                sizeN++;
            }
        }
    }
    
    let ans = Infinity;
    for (let a = 0; a <= 2; ++a) {
        const opsY = sizeY - freqY[a];
        for (let b = 0; b <= 2; ++b) {
            const opsN = sizeN - freqN[b];
            ans = Math.min(ans, opsY + opsN);
        }
    }
    return ans;
};
```

## Typescript

```typescript
function minimumOperationsToWriteY(grid: number[][]): number {
    const n = grid.length;
    const mid = Math.floor(n / 2);
    const countY = [0, 0, 0];
    const countN = [0, 0, 0];

    for (let r = 0; r < n; r++) {
        for (let c = 0; c < n; c++) {
            const val = grid[r][c];
            const isY =
                (r <= mid && (c === r || c === n - 1 - r)) ||
                (r >= mid && c === mid);
            if (isY) {
                countY[val]++;
            } else {
                countN[val]++;
            }
        }
    }

    const totalY = countY[0] + countY[1] + countY[2];
    const totalN = countN[0] + countN[1] + countN[2];

    let ans = Number.MAX_SAFE_INTEGER;
    for (let vy = 0; vy < 3; vy++) {
        const opsY = totalY - countY[vy];
        for (let vn = 0; vn < 3; vn++) {
            const opsN = totalN - countN[vn];
            const cur = opsY + opsN;
            if (cur < ans) ans = cur;
        }
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minimumOperationsToWriteY($grid) {
        $n = count($grid);
        $mid = intdiv($n, 2);
        $cntY = [0, 0, 0];
        $cntN = [0, 0, 0];

        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $val = $grid[$i][$j];
                $isY = false;
                if ($i <= $mid) {
                    if ($j == $i || $j == $n - 1 - $i) {
                        $isY = true;
                    }
                } else { // i > mid
                    if ($j == $mid) {
                        $isY = true;
                    }
                }

                if ($isY) {
                    $cntY[$val]++;
                } else {
                    $cntN[$val]++;
                }
            }
        }

        $totalY = $cntY[0] + $cntY[1] + $cntY[2];
        $totalN = $n * $n - $totalY;

        $ans = PHP_INT_MAX;
        for ($a = 0; $a < 3; $a++) {
            for ($b = 0; $b < 3; $b++) {
                $ops = ($totalY - $cntY[$a]) + ($totalN - $cntN[$b]);
                if ($ops < $ans) {
                    $ans = $ops;
                }
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minimumOperationsToWriteY(_ grid: [[Int]]) -> Int {
        let n = grid.count
        let mid = n / 2
        var totalY = 0
        var yCount = [0, 0, 0]
        var nCount = [0, 0, 0]
        
        for r in 0..<n {
            for c in 0..<n {
                let val = grid[r][c]
                let isY = (r == c && r <= mid) ||
                          (r + c == n - 1 && r <= mid) ||
                          (c == mid && r >= mid)
                if isY {
                    totalY += 1
                    yCount[val] += 1
                } else {
                    nCount[val] += 1
                }
            }
        }
        
        let totalN = n * n - totalY
        var answer = Int.max
        
        for a in 0...2 {
            for b in 0...2 where a != b {
                let ops = (totalY - yCount[a]) + (totalN - nCount[b])
                if ops < answer { answer = ops }
            }
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumOperationsToWriteY(grid: Array<IntArray>): Int {
        val n = grid.size
        val mid = n / 2
        val countY = IntArray(3)
        val countN = IntArray(3)
        var totalY = 0
        var totalN = 0

        for (i in 0 until n) {
            val row = grid[i]
            for (j in 0 until n) {
                val v = row[j]
                val isY = (i == j && i <= mid) ||
                           (i + j == n - 1 && i <= mid) ||
                           (j == mid && i >= mid)
                if (isY) {
                    countY[v]++
                    totalY++
                } else {
                    countN[v]++
                    totalN++
                }
            }
        }

        var minOps = Int.MAX_VALUE
        for (vy in 0..2) {
            for (vn in 0..2) {
                if (vy == vn) continue
                val ops = (totalY - countY[vy]) + (totalN - countN[vn])
                if (ops < minOps) minOps = ops
            }
        }
        return minOps
    }
}
```

## Dart

```dart
class Solution {
  int minimumOperationsToWriteY(List<List<int>> grid) {
    int n = grid.length;
    int mid = n ~/ 2;
    List<int> cntY = [0, 0, 0];
    List<int> cntN = [0, 0, 0];

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        bool isY = false;
        if (i == j && i <= mid) isY = true;
        if (i + j == n - 1 && i <= mid) isY = true;
        if (j == mid && i >= mid) isY = true;

        int val = grid[i][j];
        if (isY) {
          cntY[val]++;
        } else {
          cntN[val]++;
        }
      }
    }

    int sizeY = cntY.reduce((a, b) => a + b);
    int sizeN = cntN.reduce((a, b) => a + b);

    int ans = n * n;
    for (int a = 0; a < 3; a++) {
      for (int b = 0; b < 3; b++) {
        int ops = (sizeY - cntY[a]) + (sizeN - cntN[b]);
        if (ops < ans) ans = ops;
      }
    }

    return ans;
  }
}
```

## Golang

```go
func minimumOperationsToWriteY(grid [][]int) int {
    n := len(grid)
    mid := n / 2

    // counts[value][group] where group 0 = Y, 1 = non-Y
    countY := [3]int{}
    countNonY := [3]int{}

    for r := 0; r < n; r++ {
        for c := 0; c < n; c++ {
            val := grid[r][c]
            // check if cell belongs to Y
            inY := false
            if r == c && r <= mid {
                inY = true
            } else if r+c == n-1 && r <= mid {
                inY = true
            } else if c == mid && r >= mid {
                inY = true
            }
            if inY {
                countY[val]++
            } else {
                countNonY[val]++
            }
        }
    }

    totalY := 0
    for _, v := range countY {
        totalY += v
    }
    totalNonY := n*n - totalY

    minOps := n * n // upper bound
    for a := 0; a <= 2; a++ {
        for b := 0; b <= 2; b++ {
            ops := (totalY - countY[a]) + (totalNonY - countNonY[b])
            if ops < minOps {
                minOps = ops
            }
        }
    }
    return minOps
}
```

## Ruby

```ruby
def minimum_operations_to_write_y(grid)
  n = grid.size
  mid = n / 2
  count_y = [0, 0, 0]
  count_non = [0, 0, 0]

  (0...n).each do |r|
    (0...n).each do |c|
      belongs =
        if r < mid
          c == r || c == n - 1 - r
        else
          c == mid
        end

      val = grid[r][c]
      if belongs
        count_y[val] += 1
      else
        count_non[val] += 1
      end
    end
  end

  size_y = (mid * 2) + (n - mid) # actually compute directly
  size_y = 0
  (0...n).each do |r|
    if r < mid
      size_y += 2
    else
      size_y += 1
    end
  end
  size_non = n * n - size_y

  min_ops = Float::INFINITY
  (0..2).each do |v|
    (0..2).each do |w|
      ops = (size_y - count_y[v]) + (size_non - count_non[w])
      min_ops = ops if ops < min_ops
    end
  end

  min_ops.to_i
end
```

## Scala

```scala
object Solution {
    def minimumOperationsToWriteY(grid: Array[Array[Int]]): Int = {
        val n = grid.length
        val mid = n / 2
        val countY = Array(0, 0, 0)
        val countN = Array(0, 0, 0)

        for (i <- 0 until n) {
            for (j <- 0 until n) {
                val v = grid(i)(j)
                val isY = (i == j && i <= mid) ||
                          (i + j == n - 1 && i <= mid) ||
                          (j == mid && i >= mid)
                if (isY) countY(v) += 1 else countN(v) += 1
            }
        }

        val totalY = countY.sum
        val totalN = countN.sum

        var ans = Int.MaxValue
        for (vy <- 0 to 2) {
            val costY = totalY - countY(vy)
            for (vn <- 0 to 2) {
                val costN = totalN - countN(vn)
                val cur = costY + costN
                if (cur < ans) ans = cur
            }
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_operations_to_write_y(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let mid = n / 2;
        let mut cnt_y = [0i32; 3];
        let mut cnt_n = [0i32; 3];

        for i in 0..n {
            for j in 0..n {
                let val = grid[i][j] as usize;
                let is_y = (i == j && i <= mid)
                    || (i + j == n - 1 && i <= mid)
                    || (j == mid && i >= mid);
                if is_y {
                    cnt_y[val] += 1;
                } else {
                    cnt_n[val] += 1;
                }
            }
        }

        let total = (n * n) as i32;
        let mut best = 0i32;
        for a in 0..3 {
            for b in 0..3 {
                let sum = cnt_y[a] + cnt_n[b];
                if sum > best {
                    best = sum;
                }
            }
        }

        total - best
    }
}
```

## Racket

```racket
(define/contract (minimum-operations-to-write-y grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length grid))
         (mid (quotient n 2))
         (freqY (make-vector 3 0))
         (freqN (make-vector 3 0)))
    ;; count frequencies for Y cells and non‑Y cells
    (for ([i (in-range n)]
          [row (in-list grid)])
      (for ([j (in-range n)]
            [val (in-list row)])
        (if (or (and (= i j) (<= i mid))
                (and (= (+ i j) (- n 1)) (<= i mid))
                (and (= j mid) (>= i mid)))
            (vector-set! freqY val (add1 (vector-ref freqY val)))
            (vector-set! freqN val (add1 (vector-ref freqN val))))))
    (let* ((lenY (+ (vector-ref freqY 0)
                    (vector-ref freqY 1)
                    (vector-ref freqY 2)))
           (lenN (- (* n n) lenY))
           (minOps (+ n n))) ; upper bound
      (for ([x (in-range 3)])
        (for ([y (in-range 3)])
          (when (not (= x y))
            (let ((ops (+ (- lenY (vector-ref freqY x))
                          (- lenN (vector-ref freqN y)))))
              (when (< ops minOps)
                (set! minOps ops))))))
      minOps)))
```

## Erlang

```erlang
-spec minimum_operations_to_write_y(Grid :: [[integer()]]) -> integer().
minimum_operations_to_write_y(Grid) ->
    N = length(Grid),
    Mid = N div 2,
    {FreqY, FreqN, TotalY} = count_grid(Grid, 0, Mid, {0,0,0}, {0,0,0}, 0),
    TotalCells = N * N,
    TotalN = TotalCells - TotalY,
    min_ops(FreqY, FreqN, TotalY, TotalN).

%% Count frequencies of values in Y cells and non‑Y cells
count_grid([], _RowIdx, _Mid, FY, FN, TY) ->
    {FY, FN, TY};
count_grid([Row|RestRows], RowIdx, Mid, FY, FN, TY) ->
    {NewFY, NewFN, NewTY} = count_row(Row, 0, RowIdx, Mid, FY, FN, TY),
    count_grid(RestRows, RowIdx + 1, Mid, NewFY, NewFN, NewTY).

count_row([], _ColIdx, _RowIdx, _Mid, FY, FN, TY) ->
    {FY, FN, TY};
count_row([Val|Rest], ColIdx, RowIdx, Mid, FY, FN, TY) ->
    IsY = if
        RowIdx =< Mid ->
            (ColIdx =:= Mid - RowIdx) orelse (ColIdx =:= Mid + RowIdx);
        true ->
            ColIdx =:= Mid
    end,
    case IsY of
        true ->
            NewFY = inc_val(Val, FY),
            count_row(Rest, ColIdx + 1, RowIdx, Mid, NewFY, FN, TY + 1);
        false ->
            NewFN = inc_val(Val, FN),
            count_row(Rest, ColIdx + 1, RowIdx, Mid, FY, NewFN, TY)
    end.

inc_val(0, {C0, C1, C2}) -> {C0 + 1, C1, C2};
inc_val(1, {C0, C1, C2}) -> {C0, C1 + 1, C2};
inc_val(2, {C0, C1, C2}) -> {C0, C1, C2 + 1}.

get_freq({C0, _, _}, 0) -> C0;
get_freq({_, C1, _}, 1) -> C1;
get_freq({_, _, C2}, 2) -> C2.

min_ops(FY, FN, TY, TN) ->
    Values = [0,1,2],
    lists:foldl(
        fun(A, AccA) ->
            lists:foldl(
                fun(B, AccB) ->
                    Ops = (TY - get_freq(FY, A)) + (TN - get_freq(FN, B)),
                    if Ops < AccB -> Ops; true -> AccB end
                end,
                AccA,
                Values)
        end,
        1000000,
        Values).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_operations_to_write_y(grid :: [[integer]]) :: integer
  def minimum_operations_to_write_y(grid) do
    n = length(grid)
    mid = div(n, 2)

    {cnt_y, cnt_n} =
      Enum.with_index(grid)
      |> Enum.reduce({%{0 => 0, 1 => 0, 2 => 0}, %{0 => 0, 1 => 0, 2 => 0}}, fn {row, r},
                                                                                 {cy, cn} ->
        Enum.with_index(row)
        |> Enum.reduce({cy, cn}, fn {val, c}, {cy_acc, cn_acc} ->
          belongs =
            (r <= mid and (c == r or c == n - 1 - r)) or
              (r >= mid and c == mid)

          if belongs do
            {Map.update!(cy_acc, val, &(&1 + 1)), cn_acc}
          else
            {cy_acc, Map.update!(cn_acc, val, &(&1 + 1))}
          end
        end)
      end)

    size_y = Enum.reduce(cnt_y, 0, fn {_k, v}, acc -> acc + v end)
    total = n * n
    size_n = total - size_y

    ops =
      for a <- 0..2, b <- 0..2 do
        (size_y - Map.get(cnt_y, a)) + (size_n - Map.get(cnt_n, b))
      end

    Enum.min(ops)
  end
end
```
