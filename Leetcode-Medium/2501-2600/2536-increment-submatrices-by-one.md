# 2536. Increment Submatrices by One

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> rangeAddQueries(int n, vector<vector<int>>& queries) {
        vector<vector<int>> diff(n, vector<int>(n + 1, 0));
        for (const auto& q : queries) {
            int r1 = q[0], c1 = q[1], r2 = q[2], c2 = q[3];
            for (int i = r1; i <= r2; ++i) {
                diff[i][c1] += 1;
                if (c2 + 1 < n) diff[i][c2 + 1] -= 1;
            }
        }
        vector<vector<int>> ans(n, vector<int>(n, 0));
        for (int i = 0; i < n; ++i) {
            int cur = 0;
            for (int j = 0; j < n; ++j) {
                cur += diff[i][j];
                ans[i][j] = cur;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[][] rangeAddQueries(int n, int[][] queries) {
        int[][] diff = new int[n][n + 1];
        for (int[] q : queries) {
            int r1 = q[0], c1 = q[1], r2 = q[2], c2 = q[3];
            for (int i = r1; i <= r2; i++) {
                diff[i][c1] += 1;
                diff[i][c2 + 1] -= 1;
            }
        }
        int[][] res = new int[n][n];
        for (int i = 0; i < n; i++) {
            int cur = 0;
            for (int j = 0; j < n; j++) {
                cur += diff[i][j];
                res[i][j] = cur;
            }
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def rangeAddQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[List[int]]
        """
        # difference array per row with an extra column for easier subtraction
        diff = [[0] * (n + 1) for _ in range(n)]

        for r1, c1, r2, c2 in queries:
            for i in range(r1, r2 + 1):
                diff[i][c1] += 1
                diff[i][c2 + 1] -= 1

        res = [[0] * n for _ in range(n)]
        for i in range(n):
            cur = 0
            row_res = res[i]
            row_diff = diff[i]
            for j in range(n):
                cur += row_diff[j]
                row_res[j] = cur

        return res
```

## Python3

```python
from typing import List

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0] * (n + 1) for _ in range(n)]
        for r1, c1, r2, c2 in queries:
            inc_col = c1
            dec_col = c2 + 1
            for i in range(r1, r2 + 1):
                diff[i][inc_col] += 1
                if dec_col <= n:
                    diff[i][dec_col] -= 1
        res = [[0] * n for _ in range(n)]
        for i in range(n):
            cur = 0
            row_diff = diff[i]
            row_res = res[i]
            for j in range(n):
                cur += row_diff[j]
                row_res[j] = cur
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
int** rangeAddQueries(int n, int** queries, int queriesSize, int* queriesColSize, int* returnSize, int** returnColumnSizes) {
    // Allocate diff matrix with an extra column for easier subtraction
    int **diff = (int **)calloc(n, sizeof(int *));
    for (int i = 0; i < n; ++i) {
        diff[i] = (int *)calloc(n + 1, sizeof(int));
    }

    // Apply each query using row-wise difference technique
    for (int q = 0; q < queriesSize; ++q) {
        int r1 = queries[q][0];
        int c1 = queries[q][1];
        int r2 = queries[q][2];
        int c2 = queries[q][3];
        for (int row = r1; row <= r2; ++row) {
            diff[row][c1] += 1;
            if (c2 + 1 < n) {
                diff[row][c2 + 1] -= 1;
            }
        }
    }

    // Prepare return structures
    *returnSize = n;
    *returnColumnSizes = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) {
        (*returnColumnSizes)[i] = n;
    }

    int **ans = (int **)malloc(n * sizeof(int *));
    for (int i = 0; i < n; ++i) {
        ans[i] = (int *)malloc(n * sizeof(int));
        int cur = 0;
        for (int j = 0; j < n; ++j) {
            cur += diff[i][j];
            ans[i][j] = cur;
        }
    }

    // Free temporary diff matrix
    for (int i = 0; i < n; ++i) {
        free(diff[i]);
    }
    free(diff);

    return ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int[][] RangeAddQueries(int n, int[][] queries) {
        int[][] diff = new int[n][];
        for (int i = 0; i < n; i++) {
            diff[i] = new int[n + 1];
        }

        foreach (var q in queries) {
            int r1 = q[0], c1 = q[1], r2 = q[2], c2 = q[3];
            for (int row = r1; row <= r2; row++) {
                diff[row][c1] += 1;
                if (c2 + 1 < n) {
                    diff[row][c2 + 1] -= 1;
                }
            }
        }

        int[][] result = new int[n][];
        for (int i = 0; i < n; i++) {
            result[i] = new int[n];
            int cur = 0;
            for (int j = 0; j < n; j++) {
                cur += diff[i][j];
                result[i][j] = cur;
            }
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} queries
 * @return {number[][]}
 */
var rangeAddQueries = function(n, queries) {
    const diff = Array.from({ length: n }, () => new Int32Array(n + 1));
    
    for (const [r1, c1, r2, c2] of queries) {
        for (let i = r1; i <= r2; ++i) {
            diff[i][c1] += 1;
            diff[i][c2 + 1] -= 1; // c2+1 is within n+1 length
        }
    }
    
    const result = Array.from({ length: n }, () => new Array(n));
    for (let i = 0; i < n; ++i) {
        let cur = 0;
        const dRow = diff[i];
        const resRow = result[i];
        for (let j = 0; j < n; ++j) {
            cur += dRow[j];
            resRow[j] = cur;
        }
    }
    
    return result;
};
```

## Typescript

```typescript
function rangeAddQueries(n: number, queries: number[][]): number[][] {
    const diff: number[][] = Array.from({ length: n }, () => Array(n + 1).fill(0));
    for (const q of queries) {
        const [r1, c1, r2, c2] = q;
        for (let i = r1; i <= r2; i++) {
            diff[i][c1] += 1;
            diff[i][c2 + 1] -= 1;
        }
    }
    const res: number[][] = Array.from({ length: n }, () => Array(n).fill(0));
    for (let i = 0; i < n; i++) {
        let cur = 0;
        for (let j = 0; j < n; j++) {
            cur += diff[i][j];
            res[i][j] = cur;
        }
    }
    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $queries
     * @return Integer[][]
     */
    function rangeAddQueries($n, $queries) {
        // Difference matrix with an extra column for easier handling of col2+1
        $diff = array_fill(0, $n, array_fill(0, $n + 1, 0));

        foreach ($queries as $q) {
            [$r1, $c1, $r2, $c2] = $q;
            for ($i = $r1; $i <= $r2; $i++) {
                $diff[$i][$c1] += 1;
                if ($c2 + 1 < $n) {
                    $diff[$i][$c2 + 1] -= 1;
                }
            }
        }

        // Build the final matrix using prefix sums on each row
        $result = array_fill(0, $n, array_fill(0, $n, 0));
        for ($i = 0; $i < $n; $i++) {
            $curr = 0;
            for ($j = 0; $j < $n; $j++) {
                $curr += $diff[$i][$j];
                $result[$i][$j] = $curr;
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func rangeAddQueries(_ n: Int, _ queries: [[Int]]) -> [[Int]] {
        var diff = Array(repeating: Array(repeating: 0, count: n + 1), count: n)
        for q in queries {
            let r1 = q[0], c1 = q[1], r2 = q[2], c2 = q[3]
            if r1 > r2 || c1 > c2 { continue }
            for i in r1...r2 {
                diff[i][c1] += 1
                if c2 + 1 < n {
                    diff[i][c2 + 1] -= 1
                }
            }
        }
        var result = Array(repeating: Array(repeating: 0, count: n), count: n)
        for i in 0..<n {
            var cur = 0
            for j in 0..<n {
                cur += diff[i][j]
                result[i][j] = cur
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun rangeAddQueries(n: Int, queries: Array<IntArray>): Array<IntArray> {
        val diff = Array(n) { IntArray(n + 1) }
        for (q in queries) {
            val r1 = q[0]
            val c1 = q[1]
            val r2 = q[2]
            val c2 = q[3]
            for (i in r1..r2) {
                diff[i][c1] += 1
                if (c2 + 1 < n) diff[i][c2 + 1] -= 1
            }
        }
        val res = Array(n) { IntArray(n) }
        for (i in 0 until n) {
            var cur = 0
            for (j in 0 until n) {
                cur += diff[i][j]
                res[i][j] = cur
            }
        }
        return res
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> rangeAddQueries(int n, List<List<int>> queries) {
    var diff = List.generate(n, (_) => List.filled(n + 1, 0));
    for (var q in queries) {
      int r1 = q[0], c1 = q[1], r2 = q[2], c2 = q[3];
      for (int i = r1; i <= r2; ++i) {
        diff[i][c1] += 1;
        if (c2 + 1 < n) diff[i][c2 + 1] -= 1;
      }
    }
    var res = List.generate(n, (_) => List.filled(n, 0));
    for (int i = 0; i < n; ++i) {
      int cur = 0;
      for (int j = 0; j < n; ++j) {
        cur += diff[i][j];
        res[i][j] = cur;
      }
    }
    return res;
  }
}
```

## Golang

```go
func rangeAddQueries(n int, queries [][]int) [][]int {
	diff := make([][]int, n)
	for i := 0; i < n; i++ {
		diff[i] = make([]int, n+1)
	}
	for _, q := range queries {
		r1, c1, r2, c2 := q[0], q[1], q[2], q[3]
		for i := r1; i <= r2; i++ {
			diff[i][c1]++
			if c2+1 < n {
				diff[i][c2+1]--
			}
		}
	}
	res := make([][]int, n)
	for i := 0; i < n; i++ {
		row := make([]int, n)
		cur := 0
		for j := 0; j < n; j++ {
			cur += diff[i][j]
			row[j] = cur
		}
		res[i] = row
	}
	return res
}
```

## Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} queries
# @return {Integer[][]}
def range_add_queries(n, queries)
  diff = Array.new(n) { Array.new(n + 1, 0) }

  queries.each do |qr|
    r1, c1, r2, c2 = qr
    (r1..r2).each do |i|
      diff[i][c1] += 1
      diff[i][c2 + 1] -= 1 if c2 + 1 < n
    end
  end

  result = Array.new(n) { Array.new(n, 0) }
  (0...n).each do |i|
    cur = 0
    (0...n).each do |j|
      cur += diff[i][j]
      result[i][j] = cur
    end
  end

  result
end
```

## Scala

```scala
object Solution {
    def rangeAddQueries(n: Int, queries: Array[Array[Int]]): Array[Array[Int]] = {
        val diff = Array.ofDim[Int](n, n + 1)
        var qIdx = 0
        while (qIdx < queries.length) {
            val q = queries(qIdx)
            val r1 = q(0)
            val c1 = q(1)
            val r2 = q(2)
            val c2 = q(3)
            var i = r1
            while (i <= r2) {
                diff(i)(c1) += 1
                diff(i)(c2 + 1) -= 1
                i += 1
            }
            qIdx += 1
        }

        val res = Array.ofDim[Int](n, n)
        var i = 0
        while (i < n) {
            var sum = 0
            var j = 0
            while (j < n) {
                sum += diff(i)(j)
                res(i)(j) = sum
                j += 1
            }
            i += 1
        }
        res
    }
}
```

## Rust

```rust
impl Solution {
    pub fn range_add_queries(n: i32, queries: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n_usize = n as usize;
        let mut diff = vec![vec![0i32; n_usize]; n_usize];
        for q in queries.iter() {
            let r1 = q[0] as usize;
            let c1 = q[1] as usize;
            let r2 = q[2] as usize;
            let c2 = q[3] as usize;
            for i in r1..=r2 {
                diff[i][c1] += 1;
                if c2 + 1 < n_usize {
                    diff[i][c2 + 1] -= 1;
                }
            }
        }
        let mut result = vec![vec![0i32; n_usize]; n_usize];
        for i in 0..n_usize {
            let mut cur = 0i32;
            for j in 0..n_usize {
                cur += diff[i][j];
                result[i][j] = cur;
            }
        }
        result
    }
}
```

## Racket

```racket
#lang racket
(require racket/match)

(define/contract (range-add-queries n queries)
  (-> exact-integer? (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  (let* ((diff (for/vector ([i (in-range n)]) (make-vector (+ n 1) 0))))
    ;; apply each query using difference array per row
    (for ([q queries])
      (match q
        [(list r1 c1 r2 c2)
         (for ([row (in-range r1 (+ r2 1))])
           (let ((rowvec (vector-ref diff row)))
             (vector-set! rowvec c1 (+ (vector-ref rowvec c1) 1))
             (when (< (+ c2 1) n)
               (vector-set! rowvec (+ c2 1)
                            (- (vector-ref rowvec (+ c2 1)) 1)))))]))
    ;; compute final matrix from diff
    (let ((result (for/vector ([i (in-range n)]) (make-vector n 0))))
      (for ([i (in-range n)])
        (let* ((rowdiff (vector-ref diff i))
               (rowres  (vector-ref result i)))
          (let loop ((j 0) (cur 0))
            (when (< j n)
              (set! cur (+ cur (vector-ref rowdiff j)))
              (vector-set! rowres j cur)
              (loop (+ j 1) cur)))))
      ;; convert vectors to lists for output
      (for/list ([i (in-range n)])
        (vector->list (vector-ref result i))))))
```

## Erlang

```erlang
-module(solution).
-export([range_add_queries/2]).

-spec range_add_queries(N :: integer(), Queries :: [[integer()]]) -> [[integer()]].
range_add_queries(N, Queries) ->
    RowArrays = [array:new(N + 1, {default, 0}) || _ <- lists:seq(1, N)],
    Outer0 = array:from_list(RowArrays),
    Outer = apply_all_queries(Queries, N, Outer0),
    build_result(Outer, N).

apply_all_queries([], _, Outer) -> Outer;
apply_all_queries([Q | Qs], N, Outer) ->
    Outer1 = apply_query(Q, N, Outer),
    apply_all_queries(Qs, N, Outer1).

apply_query([R1, C1, R2, C2], N, Outer) ->
    apply_rows(R1, R2, C1, C2, N, Outer).

apply_rows(RowIdx, RowEnd, C1, C2, N, Outer) when RowIdx =< RowEnd ->
    RowPos = RowIdx + 1,
    RowArr0 = array:get(RowPos, Outer),

    ColPos1 = C1 + 1,
    Val1 = array:get(ColPos1, RowArr0) + 1,
    RowArr1 = array:set(ColPos1, Val1, RowArr0),

    RowArr2 =
        case C2 + 1 < N of
            true ->
                DecPos = C2 + 2,
                Val2 = array:get(DecPos, RowArr1) - 1,
                array:set(DecPos, Val2, RowArr1);
            false -> RowArr1
        end,

    Outer1 = array:set(RowPos, RowArr2, Outer),
    apply_rows(RowIdx + 1, RowEnd, C1, C2, N, Outer1);
apply_rows(_, _, _, _, _, Outer) -> Outer.

build_result(Outer, N) ->
    build_rows(0, N - 1, Outer, N, []).

build_rows(Cur, Max, _Outer, _N, Acc) when Cur > Max -> lists:reverse(Acc);
build_rows(Cur, Max, Outer, N, Acc) ->
    RowPos = Cur + 1,
    RowArr = array:get(RowPos, Outer),
    RowList = prefix_row(RowArr, N),
    build_rows(Cur + 1, Max, Outer, N, [RowList | Acc]).

prefix_row(RowArr, N) ->
    prefix_row(1, N, RowArr, 0, []).

prefix_row(Index, N, _RowArr, _Sum, Acc) when Index > N -> lists:reverse(Acc);
prefix_row(Index, N, RowArr, Sum, Acc) ->
    Val = array:get(Index, RowArr),
    NewSum = Sum + Val,
    prefix_row(Index + 1, N, RowArr, NewSum, [NewSum | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec range_add_queries(n :: integer, queries :: [[integer]]) :: [[integer]]
  def range_add_queries(n, queries) do
    zero_row = :erlang.make_tuple(n + 1, 0)

    diff =
      Enum.reduce(0..(n - 1), :array.new(n, default: nil), fn i, acc ->
        :array.set(i, zero_row, acc)
      end)

    final_diff =
      Enum.reduce(queries, diff, fn [r1, c1, r2, c2], acc_diff ->
        Enum.reduce(r1..r2, acc_diff, fn r, inner_acc ->
          row = :array.get(r, inner_acc)

          row = put_elem(row, c1, elem(row, c1) + 1)

          row =
            if c2 + 1 < n do
              put_elem(row, c2 + 1, elem(row, c2 + 1) - 1)
            else
              row
            end

          :array.set(r, row, inner_acc)
        end)
      end)

    Enum.map(0..(n - 1), fn i ->
      row_tuple = :array.get(i, final_diff)
      row_vals = Tuple.to_list(row_tuple) |> Enum.take(n)
      Enum.scan(row_vals, 0, fn x, acc -> acc + x end) |> tl
    end)
  end
end
```
