# 0051. N-Queens

## Cpp

```cpp
class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> res;
        vector<int> queens(n, -1);
        vector<bool> colUsed(n, false), diag1(2 * n - 1, false), diag2(2 * n - 1, false);
        
        function<void(int)> backtrack = [&](int row) {
            if (row == n) {
                vector<string> board(n, string(n, '.'));
                for (int r = 0; r < n; ++r) {
                    board[r][queens[r]] = 'Q';
                }
                res.push_back(move(board));
                return;
            }
            for (int c = 0; c < n; ++c) {
                if (colUsed[c] || diag1[row + c] || diag2[row - c + n - 1]) continue;
                queens[row] = c;
                colUsed[c] = diag1[row + c] = diag2[row - c + n - 1] = true;
                backtrack(row + 1);
                colUsed[c] = diag1[row + c] = diag2[row - c + n - 1] = false;
            }
        };
        
        backtrack(0);
        return res;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private int size;
    private List<List<String>> ans;
    private boolean[] col;
    private boolean[] diag1;
    private boolean[] diag2;
    private int[] queenPos;

    public List<List<String>> solveNQueens(int n) {
        size = n;
        ans = new ArrayList<>();
        col = new boolean[n];
        diag1 = new boolean[2 * n - 1];
        diag2 = new boolean[2 * n - 1];
        queenPos = new int[n];
        backtrack(0);
        return ans;
    }

    private void backtrack(int row) {
        if (row == size) {
            List<String> board = new ArrayList<>();
            for (int i = 0; i < size; i++) {
                char[] line = new char[size];
                Arrays.fill(line, '.');
                line[queenPos[i]] = 'Q';
                board.add(new String(line));
            }
            ans.add(board);
            return;
        }
        for (int c = 0; c < size; c++) {
            int d1Idx = row + c;
            int d2Idx = row - c + size - 1;
            if (!col[c] && !diag1[d1Idx] && !diag2[d2Idx]) {
                queenPos[row] = c;
                col[c] = diag1[d1Idx] = diag2[d2Idx] = true;
                backtrack(row + 1);
                col[c] = diag1[d1Idx] = diag2[d2Idx] = false;
            }
        }
    }
}
```

## Python

```python
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        cols = set()
        diag1 = set()  # row + col
        diag2 = set()  # row - col
        board = [-1] * n  # board[row] = col

        def backtrack(row):
            if row == n:
                solution = []
                for r in range(n):
                    line = ['.'] * n
                    line[board[r]] = 'Q'
                    solution.append(''.join(line))
                res.append(solution)
                return
            for col in range(n):
                if col in cols or (row + col) in diag1 or (row - col) in diag2:
                    continue
                cols.add(col)
                diag1.add(row + col)
                diag2.add(row - col)
                board[row] = col

                backtrack(row + 1)

                cols.remove(col)
                diag1.remove(row + col)
                diag2.remove(row - col)
                board[row] = -1

        backtrack(0)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res: List[List[str]] = []
        cols = set()
        pos_diag = set()  # r + c
        neg_diag = set()  # r - c
        board = [["."] * n for _ in range(n)]

        def backtrack(r: int) -> None:
            if r == n:
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                board[r][c] = "."
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)

        backtrack(0)
        return res
```

## C

```c
#include <stdlib.h>

typedef struct {
    int n;
    char ***solutions;
    int *colSizes;
    int count;
    int capacity;
    int *queens;
} Context;

static void backtrack(Context *ctx, int row, int *colUsed, int *diag1, int *diag2) {
    if (row == ctx->n) {
        char **board = (char **)malloc(ctx->n * sizeof(char *));
        for (int i = 0; i < ctx->n; ++i) {
            board[i] = (char *)malloc((ctx->n + 1) * sizeof(char));
            for (int j = 0; j < ctx->n; ++j)
                board[i][j] = '.';
            board[i][ctx->n] = '\0';
            board[i][ctx->queens[i]] = 'Q';
        }
        if (ctx->count == ctx->capacity) {
            ctx->capacity = ctx->capacity * 2 + 1;
            ctx->solutions = (char ***)realloc(ctx->solutions, ctx->capacity * sizeof(char **));
            ctx->colSizes = (int *)realloc(ctx->colSizes, ctx->capacity * sizeof(int));
        }
        ctx->solutions[ctx->count] = board;
        ctx->colSizes[ctx->count] = ctx->n;
        ctx->count++;
        return;
    }

    for (int col = 0; col < ctx->n; ++col) {
        int d1 = row + col;
        int d2 = row - col + ctx->n - 1;
        if (!colUsed[col] && !diag1[d1] && !diag2[d2]) {
            ctx->queens[row] = col;
            colUsed[col] = diag1[d1] = diag2[d2] = 1;
            backtrack(ctx, row + 1, colUsed, diag1, diag2);
            colUsed[col] = diag1[d1] = diag2[d2] = 0;
        }
    }
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
char*** solveNQueens(int n, int* returnSize, int** returnColumnSizes) {
    Context ctx;
    ctx.n = n;
    ctx.count = 0;
    ctx.capacity = 100;
    ctx.solutions = (char ***)malloc(ctx.capacity * sizeof(char **));
    ctx.colSizes = (int *)malloc(ctx.capacity * sizeof(int));
    ctx.queens = (int *)malloc(n * sizeof(int));

    int *colUsed = (int *)calloc(n, sizeof(int));
    int diagSize = 2 * n - 1;
    int *diag1 = (int *)calloc(diagSize, sizeof(int));
    int *diag2 = (int *)calloc(diagSize, sizeof(int));

    backtrack(&ctx, 0, colUsed, diag1, diag2);

    free(colUsed);
    free(diag1);
    free(diag2);
    free(ctx.queens);

    *returnSize = ctx.count;
    *returnColumnSizes = ctx.colSizes;
    return ctx.solutions;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<IList<string>> SolveNQueens(int n) {
        var results = new List<IList<string>>();
        if (n <= 0) return results;
        
        bool[] cols = new bool[n];
        bool[] diag1 = new bool[2 * n - 1]; // row + col
        bool[] diag2 = new bool[2 * n - 1]; // row - col + n - 1
        
        char[][] board = new char[n][];
        string emptyRow = new string('.', n);
        for (int i = 0; i < n; i++) {
            board[i] = emptyRow.ToCharArray();
        }
        
        void Backtrack(int row) {
            if (row == n) {
                var solution = new List<string>(n);
                foreach (var r in board) {
                    solution.Add(new string(r));
                }
                results.Add(solution);
                return;
            }
            
            for (int col = 0; col < n; col++) {
                int d1 = row + col;
                int d2 = row - col + n - 1;
                if (!cols[col] && !diag1[d1] && !diag2[d2]) {
                    board[row][col] = 'Q';
                    cols[col] = diag1[d1] = diag2[d2] = true;
                    
                    Backtrack(row + 1);
                    
                    cols[col] = diag1[d1] = diag2[d2] = false;
                    board[row][col] = '.';
                }
            }
        }
        
        Backtrack(0);
        return results;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {string[][]}
 */
var solveNQueens = function(n) {
    const solutions = [];
    const cols = new Array(n).fill(false);
    const diag1 = new Array(2 * n).fill(false); // row + col
    const diag2 = new Array(2 * n).fill(false); // row - col + n - 1
    const board = Array.from({ length: n }, () => new Array(n).fill('.'));

    function backtrack(row) {
        if (row === n) {
            solutions.push(board.map(r => r.join('')));
            return;
        }
        for (let col = 0; col < n; col++) {
            if (cols[col] || diag1[row + col] || diag2[row - col + n - 1]) continue;
            cols[col] = diag1[row + col] = diag2[row - col + n - 1] = true;
            board[row][col] = 'Q';
            backtrack(row + 1);
            board[row][col] = '.';
            cols[col] = diag1[row + col] = diag2[row - col + n - 1] = false;
        }
    }

    backtrack(0);
    return solutions;
};
```

## Typescript

```typescript
function solveNQueens(n: number): string[][] {
    const solutions: string[][] = [];
    const board: string[] = new Array(n).fill('.'.repeat(n));
    const cols = new Array(n).fill(false);
    const diag1 = new Array(2 * n - 1).fill(false); // row + col
    const diag2 = new Array(2 * n - 1).fill(false); // row - col + n - 1

    function backtrack(row: number): void {
        if (row === n) {
            solutions.push([...board]);
            return;
        }
        for (let col = 0; col < n; col++) {
            const d1 = row + col;
            const d2 = row - col + n - 1;
            if (!cols[col] && !diag1[d1] && !diag2[d2]) {
                cols[col] = diag1[d1] = diag2[d2] = true;
                board[row] = '.'.repeat(col) + 'Q' + '.'.repeat(n - col - 1);
                backtrack(row + 1);
                cols[col] = diag1[d1] = diag2[d2] = false;
                board[row] = '.'.repeat(n);
            }
        }
    }

    backtrack(0);
    return solutions;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return String[][]
     */
    function solveNQueens($n) {
        $res = [];
        $cols = array_fill(0, $n, false);
        $diag1 = array_fill(0, 2*$n-1, false); // row + col
        $diag2 = array_fill(0, 2*$n-1, false); // row - col + n - 1
        $queens = array_fill(0, $n, -1);

        $backtrack = function($row) use (&$backtrack, &$res, &$cols, &$diag1, &$diag2, &$queens, $n) {
            if ($row == $n) {
                $board = [];
                for ($i = 0; $i < $n; $i++) {
                    $line = str_repeat('.', $n);
                    $col = $queens[$i];
                    $line[$col] = 'Q';
                    $board[] = $line;
                }
                $res[] = $board;
                return;
            }

            for ($c = 0; $c < $n; $c++) {
                if (!$cols[$c] && !$diag1[$row + $c] && !$diag2[$row - $c + $n - 1]) {
                    $cols[$c] = true;
                    $diag1[$row + $c] = true;
                    $diag2[$row - $c + $n - 1] = true;
                    $queens[$row] = $c;

                    $backtrack($row + 1);

                    $cols[$c] = false;
                    $diag1[$row + $c] = false;
                    $diag2[$row - $c + $n - 1] = false;
                    $queens[$row] = -1;
                }
            }
        };

        $backtrack(0);
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func solveNQueens(_ n: Int) -> [[String]] {
        var results = [[String]]()
        var cols = [Bool](repeating: false, count: n)
        var diag1 = [Bool](repeating: false, count: 2 * n) // row + col
        var diag2 = [Bool](repeating: false, count: 2 * n) // row - col + n - 1
        var positions = [Int](repeating: -1, count: n)
        
        func backtrack(_ row: Int) {
            if row == n {
                var board = [String]()
                for r in 0..<n {
                    var line = Array(repeating: ".", count: n)
                    let c = positions[r]
                    line[c] = "Q"
                    board.append(String(line))
                }
                results.append(board)
                return
            }
            for col in 0..<n {
                if !cols[col] && !diag1[row + col] && !diag2[row - col + n - 1] {
                    cols[col] = true
                    diag1[row + col] = true
                    diag2[row - col + n - 1] = true
                    positions[row] = col
                    backtrack(row + 1)
                    cols[col] = false
                    diag1[row + col] = false
                    diag2[row - col + n - 1] = false
                }
            }
        }
        
        backtrack(0)
        return results
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun solveNQueens(n: Int): List<List<String>> {
        val results = mutableListOf<List<String>>()
        val cols = BooleanArray(n)
        val diag1 = BooleanArray(2 * n) // row + col
        val diag2 = BooleanArray(2 * n) // row - col + n
        val queens = IntArray(n)

        fun backtrack(row: Int) {
            if (row == n) {
                val board = mutableListOf<String>()
                for (r in 0 until n) {
                    val line = CharArray(n) { '.' }
                    line[queens[r]] = 'Q'
                    board.add(String(line))
                }
                results.add(board)
                return
            }
            for (col in 0 until n) {
                if (!cols[col] && !diag1[row + col] && !diag2[row - col + n]) {
                    cols[col] = true
                    diag1[row + col] = true
                    diag2[row - col + n] = true
                    queens[row] = col

                    backtrack(row + 1)

                    cols[col] = false
                    diag1[row + col] = false
                    diag2[row - col + n] = false
                }
            }
        }

        backtrack(0)
        return results
    }
}
```

## Dart

```dart
class Solution {
  List<List<String>> solveNQueens(int n) {
    List<List<String>> res = [];
    List<int> queens = List.filled(n, -1);
    Set<int> cols = {};
    Set<int> diag1 = {}; // row - col
    Set<int> diag2 = {}; // row + col

    void backtrack(int row) {
      if (row == n) {
        List<String> board = [];
        for (int i = 0; i < n; i++) {
          StringBuffer sb = StringBuffer();
          for (int j = 0; j < n; j++) {
            sb.write(j == queens[i] ? 'Q' : '.');
          }
          board.add(sb.toString());
        }
        res.add(board);
        return;
      }
      for (int col = 0; col < n; col++) {
        if (cols.contains(col) ||
            diag1.contains(row - col) ||
            diag2.contains(row + col)) continue;

        queens[row] = col;
        cols.add(col);
        diag1.add(row - col);
        diag2.add(row + col);

        backtrack(row + 1);

        cols.remove(col);
        diag1.remove(row - col);
        diag2.remove(row + col);
        queens[row] = -1;
      }
    }

    backtrack(0);
    return res;
  }
}
```

## Golang

```go
import "math/bits"

func solveNQueens(n int) [][]string {
	var res [][]string
	board := make([]int, n)
	var cols, hill, dale int

	var backtrack func(row int)
	backtrack = func(row int) {
		if row == n {
			sol := make([]string, n)
			for i := 0; i < n; i++ {
				rowBytes := make([]byte, n)
				for j := 0; j < n; j++ {
					rowBytes[j] = '.'
				}
				rowBytes[board[i]] = 'Q'
				sol[i] = string(rowBytes)
			}
			res = append(res, sol)
			return
		}
		freePositions := ((1 << n) - 1) & ^(cols | hill | dale)
		for freePositions != 0 {
			currPos := freePositions & -freePositions
			col := bits.TrailingZeros(uint(currPos))
			board[row] = col

			cols ^= currPos
			hill ^= currPos << 1
			dale ^= currPos >> 1

			backtrack(row + 1)

			cols ^= currPos
			hill ^= currPos << 1
			dale ^= currPos >> 1

			freePositions &= freePositions - 1
		}
	}

	backtrack(0)
	return res
}
```

## Ruby

```ruby
# @param {Integer} n
# @return {String[][]}
def solve_n_queens(n)
  res = []
  board = Array.new(n) { '.' * n }
  cols = Array.new(n, false)
  d1 = Array.new(2 * n, false)   # row - col + n
  d2 = Array.new(2 * n, false)   # row + col

  backtrack = lambda do |row|
    if row == n
      res << board.map(&:dup)
      return
    end

    (0...n).each do |col|
      next if cols[col] || d1[row - col + n] || d2[row + col]

      board[row][col] = 'Q'
      cols[col] = d1[row - col + n] = d2[row + col] = true

      backtrack.call(row + 1)

      board[row][col] = '.'
      cols[col] = d1[row - col + n] = d2[row + col] = false
    end
  end

  backtrack.call(0)
  res
end
```

## Scala

```scala
object Solution {
    def solveNQueens(n: Int): List[List[String]] = {
        val cols = Array.fill(n)(false)
        val diag1 = Array.fill(2 * n)(false) // row + col
        val diag2 = Array.fill(2 * n)(false) // row - col + n
        val positions = new Array[Int](n)
        val res = scala.collection.mutable.ListBuffer[List[String]]()

        def backtrack(row: Int): Unit = {
            if (row == n) {
                val board = (0 until n).map { r =>
                    val sb = new StringBuilder
                    for (c <- 0 until n) {
                        if (positions(r) == c) sb.append('Q') else sb.append('.')
                    }
                    sb.toString()
                }.toList
                res += board
            } else {
                for (col <- 0 until n) {
                    val d1 = row + col
                    val d2 = row - col + n
                    if (!cols(col) && !diag1(d1) && !diag2(d2)) {
                        cols(col) = true
                        diag1(d1) = true
                        diag2(d2) = true
                        positions(row) = col

                        backtrack(row + 1)

                        cols(col) = false
                        diag1(d1) = false
                        diag2(d2) = false
                    }
                }
            }
        }

        backtrack(0)
        res.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn solve_n_queens(n: i32) -> Vec<Vec<String>> {
        let n = n as usize;
        if n == 0 {
            return vec![];
        }
        let mut cols = vec![false; n];
        let mut diag1 = vec![false; 2 * n - 1]; // row + col
        let mut diag2 = vec![false; 2 * n - 1]; // row - col + n - 1
        let mut positions: Vec<usize> = Vec::with_capacity(n);
        let mut results: Vec<Vec<String>> = Vec::new();

        fn backtrack(
            row: usize,
            n: usize,
            cols: &mut [bool],
            diag1: &mut [bool],
            diag2: &mut [bool],
            positions: &mut Vec<usize>,
            results: &mut Vec<Vec<String>>,
        ) {
            if row == n {
                let mut board = Vec::with_capacity(n);
                for &c in positions.iter() {
                    let mut line = vec!['.'; n];
                    line[c] = 'Q';
                    board.push(line.into_iter().collect());
                }
                results.push(board);
                return;
            }

            for col in 0..n {
                let d1 = row + col;
                let d2 = row + n - 1 - col;
                if !cols[col] && !diag1[d1] && !diag2[d2] {
                    cols[col] = true;
                    diag1[d1] = true;
                    diag2[d2] = true;
                    positions.push(col);

                    backtrack(row + 1, n, cols, diag1, diag2, positions, results);

                    positions.pop();
                    cols[col] = false;
                    diag1[d1] = false;
                    diag2[d2] = false;
                }
            }
        }

        backtrack(
            0,
            n,
            &mut cols,
            &mut diag1,
            &mut diag2,
            &mut positions,
            &mut results,
        );
        results
    }
}
```

## Racket

```racket
(define/contract (solve-n-queens n)
  (-> exact-integer? (listof (listof string?)))
  (letrec ((place
            (lambda (row cols d1 d2 pos)
              (if (= row n)
                  (list (reverse pos))
                  (apply append
                         (for/list ([c (in-range n)]
                                    #:when (and (not (member c cols))
                                                (not (member (+ row c) d1))
                                                (not (member (- row c) d2))))
                           (place (add1 row)
                                  (cons c cols)
                                  (cons (+ row c) d1)
                                  (cons (- row c) d2)
                                  (cons c pos)))))))
           (positions->board
            (lambda (pos)
              (map (lambda (c)
                     (let ((s (make-string n #\.)))
                       (string-set! s c #\Q)
                       s))
                   pos))))
    (map positions->board (place 0 '() '() '() '()))))
```

## Erlang

```erlang
-module(solution).
-export([solve_n_queens/1]).

-spec solve_n_queens(N :: integer()) -> [[unicode:unicode_binary()]].
solve_n_queens(N) when N >= 1 ->
    Solutions = backtrack(0, N, [], [], [], []),
    [format_solution(Sol, N) || Sol <- Solutions].

backtrack(Row, N, Cols, D1, D2, PosAcc) when Row == N ->
    [lists:reverse(PosAcc)];
backtrack(Row, N, Cols, D1, D2, PosAcc) ->
    lists:foldl(
        fun(Col, Acc) ->
            case (not lists:member(Col, Cols)) andalso
                 (not lists:member(Row - Col, D1)) andalso
                 (not lists:member(Row + Col, D2)) of
                true ->
                    NewCols = [Col | Cols],
                    NewD1   = [Row - Col | D1],
                    NewD2   = [Row + Col | D2],
                    Sub     = backtrack(Row + 1, N, NewCols, NewD1, NewD2, [Col | PosAcc]),
                    Acc ++ Sub;
                false ->
                    Acc
            end
        end,
        [],
        lists:seq(0, N - 1)
    ).

format_solution(Positions, N) ->
    [make_row(Col, N) || Col <- Positions].

make_row(QCol, N) ->
    Row = [if I == QCol -> $Q; true -> $. end || I <- lists:seq(0, N - 1)],
    list_to_binary(Row).
```

## Elixir

```elixir
defmodule Solution do
  @spec solve_n_queens(n :: integer) :: [[String.t]]
  def solve_n_queens(n) do
    backtrack(0, n, [], MapSet.new(), MapSet.new(), MapSet.new())
  end

  defp backtrack(row, n, positions_rev, cols_set, d1_set, d2_set) do
    if row == n do
      positions = Enum.reverse(positions_rev)
      [build_board(positions, n)]
    else
      0..(n - 1)
      |> Enum.flat_map(fn col ->
        cond_ok =
          not MapSet.member?(cols_set, col) and
            not MapSet.member?(d1_set, row + col) and
            not MapSet.member?(d2_set, row - col)

        if cond_ok do
          backtrack(
            row + 1,
            n,
            [col | positions_rev],
            MapSet.put(cols_set, col),
            MapSet.put(d1_set, row + col),
            MapSet.put(d2_set, row - col)
          )
        else
          []
        end
      end)
    end
  end

  defp build_board(positions, n) do
    Enum.map(positions, fn col -> row_string(col, n) end)
  end

  defp row_string(col, n) do
    left = String.duplicate(".", col)
    right = String.duplicate(".", n - col - 1)
    left <> "Q" <> right
  end
end
```
