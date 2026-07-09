# 0304. Range Sum Query 2D - Immutable

## Cpp

```cpp
class NumMatrix {
public:
    vector<vector<int>> prefix;
    NumMatrix(vector<vector<int>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) {
            prefix = {{0}};
            return;
        }
        int m = matrix.size();
        int n = matrix[0].size();
        prefix.assign(m + 1, vector<int>(n + 1, 0));
        for (int i = 0; i < m; ++i) {
            int rowSum = 0;
            for (int j = 0; j < n; ++j) {
                rowSum += matrix[i][j];
                prefix[i + 1][j + 1] = prefix[i][j + 1] + rowSum;
            }
        }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        return prefix[row2 + 1][col2 + 1]
             - prefix[row1][col2 + 1]
             - prefix[row2 + 1][col1]
             + prefix[row1][col1];
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */
```

## Java

```java
class NumMatrix {
    private final int[][] prefix;

    public NumMatrix(int[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            prefix = new int[1][1];
            return;
        }
        int m = matrix.length;
        int n = matrix[0].length;
        prefix = new int[m + 1][n + 1];
        for (int i = 0; i < m; i++) {
            int rowSum = 0;
            for (int j = 0; j < n; j++) {
                rowSum += matrix[i][j];
                prefix[i + 1][j + 1] = prefix[i][j + 1] + rowSum;
            }
        }
    }

    public int sumRegion(int row1, int col1, int row2, int col2) {
        return prefix[row2 + 1][col2 + 1]
                - prefix[row1][col2 + 1]
                - prefix[row2 + 1][col1]
                + prefix[row1][col1];
    }
}
```

## Python

```python
class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            self.prefix = [[0]]
            return
        m, n = len(matrix), len(matrix[0])
        # prefix sum with extra leading row and column
        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            row_sum = 0
            for j in range(n):
                row_sum += matrix[i][j]
                self.prefix[i + 1][j + 1] = self.prefix[i][j + 1] + row_sum

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        # using inclusion-exclusion on the prefix matrix
        return (self.prefix[row2 + 1][col2 + 1]
                - self.prefix[row1][col2 + 1]
                - self.prefix[row2 + 1][col1]
                + self.prefix[row1][col1])
```

## Python3

```python
from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.prefix = [[0]]
            return
        m, n = len(matrix), len(matrix[0])
        # prefix sum with extra leading row and column (size (m+1) x (n+1))
        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            row_sum = 0
            for j in range(n):
                row_sum += matrix[i][j]
                self.prefix[i + 1][j + 1] = self.prefix[i][j + 1] + row_sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # using inclusion-exclusion on the prefix matrix
        p = self.prefix
        return (
            p[row2 + 1][col2 + 1]
            - p[row1][col2 + 1]
            - p[row2 + 1][col1]
            + p[row1][col1]
        )
```

## C

```c
#include <stdlib.h>

typedef struct {
    int rows;
    int cols;
    int **pre;  // (rows+1) x (cols+1) prefix sums
} NumMatrix;

NumMatrix* numMatrixCreate(int** matrix, int matrixSize, int* matrixColSize) {
    if (matrixSize == 0 || matrixColSize == NULL) return NULL;
    NumMatrix *obj = (NumMatrix *)malloc(sizeof(NumMatrix));
    obj->rows = matrixSize;
    obj->cols = matrixColSize[0];

    int r = obj->rows + 1;
    int c = obj->cols + 1;

    obj->pre = (int **)malloc(r * sizeof(int *));
    for (int i = 0; i < r; ++i) {
        obj->pre[i] = (int *)calloc(c, sizeof(int)); // initialized to 0
    }

    for (int i = 1; i <= obj->rows; ++i) {
        for (int j = 1; j <= obj->cols; ++j) {
            obj->pre[i][j] = matrix[i - 1][j - 1]
                           + obj->pre[i - 1][j]
                           + obj->pre[i][j - 1]
                           - obj->pre[i - 1][j - 1];
        }
    }

    return obj;
}

int numMatrixSumRegion(NumMatrix* obj, int row1, int col1, int row2, int col2) {
    if (!obj) return 0;
    int r1 = row1 + 1;
    int c1 = col1 + 1;
    int r2 = row2 + 1;
    int c2 = col2 + 1;

    return obj->pre[r2][c2]
         - obj->pre[r1 - 1][c2]
         - obj->pre[r2][c1 - 1]
         + obj->pre[r1 - 1][c1 - 1];
}

void numMatrixFree(NumMatrix* obj) {
    if (!obj) return;
    for (int i = 0; i < obj->rows + 1; ++i) {
        free(obj->pre[i]);
    }
    free(obj->pre);
    free(obj);
}
```

## Csharp

```csharp
public class NumMatrix
{
    private readonly int[,] _prefix;

    public NumMatrix(int[][] matrix)
    {
        if (matrix == null || matrix.Length == 0 || matrix[0].Length == 0)
        {
            _prefix = new int[1, 1];
            return;
        }

        int m = matrix.Length;
        int n = matrix[0].Length;
        _prefix = new int[m + 1, n + 1];

        for (int i = 1; i <= m; i++)
        {
            int rowSum = 0;
            for (int j = 1; j <= n; j++)
            {
                rowSum += matrix[i - 1][j - 1];
                _prefix[i, j] = _prefix[i - 1, j] + rowSum;
            }
        }
    }

    public int SumRegion(int row1, int col1, int row2, int col2)
    {
        // Convert to 1‑based indices for the prefix array
        int r1 = row1 + 1;
        int c1 = col1 + 1;
        int r2 = row2 + 1;
        int c2 = col2 + 1;

        return _prefix[r2, c2] - _prefix[row1, c2] - _prefix[r2, col1] + _prefix[row1, col1];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} matrix
 */
var NumMatrix = function(matrix) {
    this.prefix = [];
    const m = matrix.length;
    if (m === 0) return;
    const n = matrix[0].length;
    // initialize (m+1) x (n+1) prefix sum array with zeros
    for (let i = 0; i <= m; i++) {
        this.prefix[i] = new Array(n + 1).fill(0);
    }
    // build prefix sums
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            this.prefix[i + 1][j + 1] =
                matrix[i][j] +
                this.prefix[i][j + 1] +
                this.prefix[i + 1][j] -
                this.prefix[i][j];
        }
    }
};

/** 
 * @param {number} row1 
 * @param {number} col1 
 * @param {number} row2 
 * @param {number} col2
 * @return {number}
 */
NumMatrix.prototype.sumRegion = function(row1, col1, row2, col2) {
    if (!this.prefix || this.prefix.length === 0) return 0;
    const p = this.prefix;
    return (
        p[row2 + 1][col2 + 1] -
        p[row1][col2 + 1] -
        p[row2 + 1][col1] +
        p[row1][col1]
    );
};
```

## Typescript

```typescript
class NumMatrix {
    private prefix: number[][];
    constructor(matrix: number[][]) {
        const m = matrix.length;
        const n = m ? matrix[0].length : 0;
        this.prefix = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));
        for (let i = 0; i < m; i++) {
            let rowSum = 0;
            for (let j = 0; j < n; j++) {
                rowSum += matrix[i][j];
                this.prefix[i + 1][j + 1] = this.prefix[i][j + 1] + rowSum;
            }
        }
    }

    sumRegion(row1: number, col1: number, row2: number, col2: number): number {
        const p = this.prefix;
        return (
            p[row2 + 1][col2 + 1] -
            p[row1][col2 + 1] -
            p[row2 + 1][col1] +
            p[row1][col1]
        );
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * var obj = new NumMatrix(matrix)
 * var param_1 = obj.sumRegion(row1,col1,row2,col2)
 */
```

## Php

```php
class NumMatrix {
    private $dp;
    
    /**
     * @param Integer[][] $matrix
     */
    function __construct($matrix) {
        $m = count($matrix);
        if ($m == 0) {
            $this->dp = [[0]];
            return;
        }
        $n = count($matrix[0]);
        // Initialize dp with extra row and column (all zeros)
        $this->dp = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $this->dp[$i + 1][$j + 1] = $matrix[$i][$j]
                    + $this->dp[$i][$j + 1]
                    + $this->dp[$i + 1][$j]
                    - $this->dp[$i][$j];
            }
        }
    }

    /**
     * @param Integer $row1
     * @param Integer $col1
     * @param Integer $row2
     * @param Integer $col2
     * @return Integer
     */
    function sumRegion($row1, $col1, $row2, $col2) {
        // Using inclusion-exclusion on the prefix sums
        return $this->dp[$row2 + 1][$col2 + 1]
            - $this->dp[$row1][$col2 + 1]
            - $this->dp[$row2 + 1][$col1]
            + $this->dp[$row1][$col1];
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * $obj = new NumMatrix($matrix);
 * $ret_1 = $obj->sumRegion($row1, $col1, $row2, $col2);
 */
```

## Swift

```swift
class NumMatrix {
    private var prefix: [[Int]]
    
    init(_ matrix: [[Int]]) {
        let m = matrix.count
        if m == 0 || matrix[0].isEmpty {
            self.prefix = [[]]
            return
        }
        let n = matrix[0].count
        self.prefix = Array(repeating: Array(repeating: 0, count: n + 1), count: m + 1)
        for i in 0..<m {
            for j in 0..<n {
                prefix[i + 1][j + 1] = matrix[i][j] + prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j]
            }
        }
    }
    
    func sumRegion(_ row1: Int, _ col1: Int, _ row2: Int, _ col2: Int) -> Int {
        if prefix.isEmpty { return 0 }
        return prefix[row2 + 1][col2 + 1] - prefix[row1][col2 + 1] - prefix[row2 + 1][col1] + prefix[row1][col1]
    }
}
```

## Kotlin

```kotlin
class NumMatrix(matrix: Array<IntArray>) {
    private val prefix: Array<IntArray>

    init {
        val m = matrix.size
        val n = if (m > 0) matrix[0].size else 0
        prefix = Array(m + 1) { IntArray(n + 1) }
        for (i in 0 until m) {
            for (j in 0 until n) {
                prefix[i + 1][j + 1] = matrix[i][j] +
                        prefix[i][j + 1] +
                        prefix[i + 1][j] -
                        prefix[i][j]
            }
        }
    }

    fun sumRegion(row1: Int, col1: Int, row2: Int, col2: Int): Int {
        return prefix[row2 + 1][col2 + 1] -
                prefix[row1][col2 + 1] -
                prefix[row2 + 1][col1] +
                prefix[row1][col1]
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * var obj = NumMatrix(matrix)
 * var param_1 = obj.sumRegion(row1,col1,row2,col2)
 */
```

## Dart

```dart
class NumMatrix {
  late final List<List<int>> _prefix;

  NumMatrix(List<List<int>> matrix) {
    if (matrix.isEmpty || matrix[0].isEmpty) {
      _prefix = [[0]];
      return;
    }
    int m = matrix.length;
    int n = matrix[0].length;
    _prefix = List.generate(m + 1, (_) => List.filled(n + 1, 0));
    for (int i = 1; i <= m; ++i) {
      for (int j = 1; j <= n; ++j) {
        _prefix[i][j] = matrix[i - 1][j - 1] +
            _prefix[i - 1][j] +
            _prefix[i][j - 1] -
            _prefix[i - 1][j - 1];
      }
    }
  }

  int sumRegion(int row1, int col1, int row2, int col2) {
    // Convert to 1‑based indices for the prefix matrix
    int r1 = row1 + 1;
    int c1 = col1 + 1;
    int r2 = row2 + 1;
    int c2 = col2 + 1;
    return _prefix[r2][c2] -
        _prefix[r1 - 1][c2] -
        _prefix[r2][c1 - 1] +
        _prefix[r1 - 1][c1 - 1];
  }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = NumMatrix(matrix);
 * int param1 = obj.sumRegion(row1,col1,row2,col2);
 */
```

## Golang

```go
type NumMatrix struct {
	dp [][]int
}

func Constructor(matrix [][]int) NumMatrix {
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return NumMatrix{dp: [][]int{{0}}}
	}
	m, n := len(matrix), len(matrix[0])
	dp := make([][]int, m+1)
	for i := range dp {
		dp[i] = make([]int, n+1)
	}
	for i := 1; i <= m; i++ {
		rowSum := 0
		for j := 1; j <= n; j++ {
			rowSum += matrix[i-1][j-1]
			dp[i][j] = dp[i-1][j] + rowSum
		}
	}
	return NumMatrix{dp: dp}
}

func (this *NumMatrix) SumRegion(row1 int, col1 int, row2 int, col2 int) int {
	return this.dp[row2+1][col2+1] - this.dp[row1][col2+1] - this.dp[row2+1][col1] + this.dp[row1][col1]
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * obj := Constructor(matrix);
 * param_1 := obj.SumRegion(row1,col1,row2,col2);
 */
```

## Ruby

```ruby
class NumMatrix
  # :type matrix: Integer[][]
  def initialize(matrix)
    @m = matrix.length
    @n = @m > 0 ? matrix[0].length : 0
    @dp = Array.new(@m + 1) { Array.new(@n + 1, 0) }
    (1..@m).each do |i|
      row = matrix[i - 1]
      (1..@n).each do |j|
        @dp[i][j] = @dp[i - 1][j] + @dp[i][j - 1] - @dp[i - 1][j - 1] + row[j - 1]
      end
    end
  end

  # :type row1: Integer
  # :type col1: Integer
  # :type row2: Integer
  # :type col2: Integer
  # :rtype: Integer
  def sum_region(row1, col1, row2, col2)
    r1 = row1
    c1 = col1
    r2 = row2
    c2 = col2
    @dp[r2 + 1][c2 + 1] - @dp[r1][c2 + 1] - @dp[r2 + 1][c1] + @dp[r1][c1]
  end
end
```

## Scala

```scala
class NumMatrix(_matrix: Array[Array[Int]]) {
  private val rows = _matrix.length
  private val cols = if (rows > 0) _matrix(0).length else 0
  private val prefix = Array.ofDim[Int](rows + 1, cols + 1)

  for (i <- 1 to rows) {
    for (j <- 1 to cols) {
      prefix(i)(j) = _matrix(i - 1)(j - 1) +
        prefix(i - 1)(j) +
        prefix(i)(j - 1) -
        prefix(i - 1)(j - 1)
    }
  }

  def sumRegion(row1: Int, col1: Int, row2: Int, col2: Int): Int = {
    val r1 = row1
    val c1 = col1
    val r2 = row2
    val c3 = col2
    prefix(r2 + 1)(c3 + 1) - prefix(r1)(c3 + 1) - prefix(r2 + 1)(c1) + prefix(r1)(c1)
  }
}
```

## Rust

```rust
struct NumMatrix {
    prefix: Vec<Vec<i32>>,
}

impl NumMatrix {
    fn new(matrix: Vec<Vec<i32>>) -> Self {
        let m = matrix.len();
        let n = if m > 0 { matrix[0].len() } else { 0 };
        let mut prefix = vec![vec![0; n + 1]; m + 1];
        for i in 0..m {
            for j in 0..n {
                prefix[i + 1][j + 1] = matrix[i][j]
                    + prefix[i][j + 1]
                    + prefix[i + 1][j]
                    - prefix[i][j];
            }
        }
        NumMatrix { prefix }
    }

    fn sum_region(&self, row1: i32, col1: i32, row2: i32, col2: i32) -> i32 {
        let r1 = row1 as usize;
        let c1 = col1 as usize;
        let r2 = row2 as usize;
        let c2 = col2 as usize;
        self.prefix[r2 + 1][c2 + 1]
            - self.prefix[r1][c2 + 1]
            - self.prefix[r2 + 1][c1]
            + self.prefix[r1][c1]
    }
}
```

## Racket

```racket
#lang racket

(define num-matrix%
  (class object%
    (super-new)
    (init-field matrix)
    (field prefix)

    ;; Build 2‑D prefix sum table
    (let* ([m (length matrix)]
           [mat-vec (list->vector (map list->vector matrix))]
           [n (if (= m 0) 0 (vector-length (vector-ref mat-vec 0)))])
      (set! prefix (make-vector (+ m 1)))
      (for ([i (in-range (+ m 1))])
        (vector-set! prefix i (make-vector (+ n 1) 0)))
      (for ([i (in-range 1 (+ m 1))])
        (let* ([row-vec (vector-ref mat-vec (- i 1))]
               [pref-row (vector-ref prefix i)]
               [pref-up-row (vector-ref prefix (- i 1))])
          (for ([j (in-range 1 (+ n 1))])
            (define val (vector-ref row-vec (- j 1)))
            (define up (vector-ref pref-up-row j))
            (define left (vector-ref pref-row (- j 1))) ; already computed
            (define diag (vector-ref pref-up-row (- j 1)))
            (vector-set! pref-row j (+ val up left (- diag))))))))

    (define/public (sum-region row1 col1 row2 col2)
      (let* ([br-row (+ row2 1)]
             [br-col (+ col2 1)]
             [top-row row1]
             [left-col col1]
             [br (vector-ref (vector-ref prefix br-row) br-col)]
             [top (vector-ref (vector-ref prefix top-row) br-col)]
             [left (vector-ref (vector-ref prefix br-row) left-col)]
             [corner (vector-ref (vector-ref prefix top-row) left-col)])
        (+ br (- top) (- left) corner)))))
```

## Erlang

```erlang
-module(solution).
-export([num_matrix_init_/1, num_matrix_sum_region/4]).

-spec num_matrix_init_(Matrix :: [[integer()]]) -> any().
num_matrix_init_(Matrix) ->
    Prefix = compute_prefix(Matrix),
    put(num_matrix_prefix, Prefix).

-spec num_matrix_sum_region(Row1 :: integer(), Col1 :: integer(),
                            Row2 :: integer(), Col2 :: integer()) -> integer().
num_matrix_sum_region(Row1, Col1, Row2, Col2) ->
    Prefix = get(num_matrix_prefix),
    Sum = get_val(Prefix, Row2 + 1, Col2 + 1)
        - get_val(Prefix, Row1,     Col2 + 1)
        - get_val(Prefix, Row2 + 1, Col1)
        + get_val(Prefix, Row1,     Col1),
    Sum.

%% Helper functions

compute_prefix(Matrix) ->
    case Matrix of
        [] -> [[0]];
        _ ->
            N = length(hd(Matrix)),
            ZeroRow = lists:duplicate(N + 1, 0),
            PrefixRowsRev = compute_rows(Matrix, ZeroRow, [ZeroRow]),
            lists:reverse(PrefixRowsRev)
    end.

compute_rows([], _PrevPrefixRow, AccRows) -> AccRows;
compute_rows([OrigRow | Rest], PrevPrefixRow, AccRows) ->
    CurrPrefixRow = compute_one_row(OrigRow, PrevPrefixRow),
    compute_rows(Rest, CurrPrefixRow, [CurrPrefixRow | AccRows]).

compute_one_row(OrigRow, PrevPrefixRow) ->
    N = length(OrigRow),
    compute_one_row(1, N, OrigRow, PrevPrefixRow, 0, []).

compute_one_row(J, N, _OrigRow, _PrevPrefixRow, _PrevCurr, Acc) when J > N ->
    RowVals = lists:reverse(Acc),
    [0 | RowVals];
compute_one_row(J, N, OrigRow, PrevPrefixRow, PrevCurr, Acc) ->
    V = lists:nth(J, OrigRow),
    PrevRowJ = lists:nth(J, PrevPrefixRow),
    PrevRowPrev = lists:nth(J - 1, PrevPrefixRow),
    Curr = V + PrevRowJ + PrevCurr - PrevRowPrev,
    compute_one_row(J + 1, N, OrigRow, PrevPrefixRow, Curr, [Curr | Acc]).

get_val(Prefix, RowIdx, ColIdx) ->
    RowList = lists:nth(RowIdx + 1, Prefix),
    lists:nth(ColIdx + 1, RowList).
```

## Elixir

```elixir
defmodule NumMatrix do
  @spec init_(matrix :: [[integer]]) :: any
  def init_(matrix) do
    m = length(matrix)
    n = if m == 0, do: 0, else: length(hd(matrix))

    zero_row = for _ <- 0..n, do: 0
    prefix = [zero_row]

    prefix =
      Enum.reduce(0..(m - 1), prefix, fn i, acc ->
        prev_row = Enum.at(acc, i)
        cur_matrix_row = Enum.at(matrix, i)

        new_row_rev =
          Enum.reduce(0..n, [], fn j, row_acc ->
            if j == 0 do
              [0 | row_acc]
            else
              val = Enum.at(cur_matrix_row, j - 1)
              top = Enum.at(prev_row, j)
              left = hd(row_acc)
              diag = Enum.at(prev_row, j - 1)
              sum = val + top + left - diag
              [sum | row_acc]
            end
          end)

        new_row = Enum.reverse(new_row_rev)
        acc ++ [new_row]
      end)

    Process.put(:num_matrix_prefix, prefix)
  end

  @spec sum_region(row1 :: integer, col1 :: integer, row2 :: integer, col2 :: integer) :: integer
  def sum_region(row1, col1, row2, col2) do
    pref = Process.get(:num_matrix_prefix)

    a = get(pref, row2 + 1, col2 + 1)
    b = get(pref, row1, col2 + 1)
    c = get(pref, row2 + 1, col1)
    d = get(pref, row1, col1)

    a - b - c + d
  end

  defp get(mat, i, j) do
    mat |> Enum.at(i) |> Enum.at(j)
  end
end
```
