# 2718. Sum of Matrix After Queries

## Cpp

```cpp
class Solution {
public:
    long long matrixSumQueries(int n, vector<vector<int>>& queries) {
        vector<char> rowSeen(n, 0), colSeen(n, 0);
        long long remainingRows = n, remainingCols = n;
        long long total = 0;
        for (int i = (int)queries.size() - 1; i >= 0; --i) {
            int type = queries[i][0];
            int idx = queries[i][1];
            int val = queries[i][2];
            if (type == 0) { // row
                if (!rowSeen[idx]) {
                    total += (long long)val * remainingCols;
                    rowSeen[idx] = 1;
                    --remainingRows;
                }
            } else { // column
                if (!colSeen[idx]) {
                    total += (long long)val * remainingRows;
                    colSeen[idx] = 1;
                    --remainingCols;
                }
            }
        }
        return total;
    }
};
```

## Java

```java
class Solution {
    public long matrixSumQueries(int n, int[][] queries) {
        boolean[] rowSeen = new boolean[n];
        boolean[] colSeen = new boolean[n];
        int rowsCount = 0;
        int colsCount = 0;
        long total = 0L;
        for (int i = queries.length - 1; i >= 0; --i) {
            int type = queries[i][0];
            int idx = queries[i][1];
            int val = queries[i][2];
            if (type == 0) { // row assignment
                if (!rowSeen[idx]) {
                    long cells = n - colsCount;
                    total += cells * (long) val;
                    rowSeen[idx] = true;
                    rowsCount++;
                }
            } else { // column assignment
                if (!colSeen[idx]) {
                    long cells = n - rowsCount;
                    total += cells * (long) val;
                    colSeen[idx] = true;
                    colsCount++;
                }
            }
        }
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def matrixSumQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: int
        """
        seen_rows = set()
        seen_cols = set()
        total = 0
        for typ, idx, val in reversed(queries):
            if typ == 0:
                if idx not in seen_rows:
                    cnt = n - len(seen_cols)
                    total += val * cnt
                    seen_rows.add(idx)
            else:  # typ == 1
                if idx not in seen_cols:
                    cnt = n - len(seen_rows)
                    total += val * cnt
                    seen_cols.add(idx)
        return total
```

## Python3

```python
from typing import List

class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        seen_row = [False] * n
        seen_col = [False] * n
        remaining_rows = n
        remaining_cols = n
        total = 0

        for typ, idx, val in reversed(queries):
            if typ == 0:  # row assignment
                if not seen_row[idx]:
                    total += val * remaining_cols
                    seen_row[idx] = True
                    remaining_rows -= 1
            else:         # column assignment
                if not seen_col[idx]:
                    total += val * remaining_rows
                    seen_col[idx] = True
                    remaining_cols -= 1

        return total
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

long long matrixSumQueries(int n, int** queries, int queriesSize, int* queriesColSize) {
    bool *rowSeen = (bool*)calloc(n, sizeof(bool));
    bool *colSeen = (bool*)calloc(n, sizeof(bool));
    int rowCnt = 0, colCnt = 0;
    long long ans = 0;
    for (int i = queriesSize - 1; i >= 0; --i) {
        int type = queries[i][0];
        int idx = queries[i][1];
        int val = queries[i][2];
        if (type == 0) { // row
            if (!rowSeen[idx]) {
                ans += (long long)val * (n - colCnt);
                rowSeen[idx] = true;
                ++rowCnt;
            }
        } else { // column
            if (!colSeen[idx]) {
                ans += (long long)val * (n - rowCnt);
                colSeen[idx] = true;
                ++colCnt;
            }
        }
    }
    free(rowSeen);
    free(colSeen);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public long MatrixSumQueries(int n, int[][] queries) {
        var seenRows = new HashSet<int>();
        var seenCols = new HashSet<int>();
        int remainingRows = n;
        int remainingCols = n;
        long total = 0L;

        for (int i = queries.Length - 1; i >= 0; --i) {
            int type = queries[i][0];
            int index = queries[i][1];
            int val = queries[i][2];

            if (type == 0) { // row
                if (!seenRows.Contains(index)) {
                    seenRows.Add(index);
                    total += (long)val * remainingCols;
                    remainingRows--;
                }
            } else { // column
                if (!seenCols.Contains(index)) {
                    seenCols.Add(index);
                    total += (long)val * remainingRows;
                    remainingCols--;
                }
            }

            // early exit if all rows and columns are processed
            if (remainingRows == 0 && remainingCols == 0) break;
        }

        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} queries
 * @return {number}
 */
var matrixSumQueries = function(n, queries) {
    const seenRows = new Set();
    const seenCols = new Set();
    let total = 0;
    
    for (let i = queries.length - 1; i >= 0; --i) {
        const [type, idx, val] = queries[i];
        if (type === 0) { // row
            if (!seenRows.has(idx)) {
                const cnt = n - seenCols.size;
                total += cnt * val;
                seenRows.add(idx);
            }
        } else { // column
            if (!seenCols.has(idx)) {
                const cnt = n - seenRows.size;
                total += cnt * val;
                seenCols.add(idx);
            }
        }
    }
    
    return total;
};
```

## Typescript

```typescript
function matrixSumQueries(n: number, queries: number[][]): number {
    const rowSeen = new Array<boolean>(n).fill(false);
    const colSeen = new Array<boolean>(n).fill(false);
    let remainingRows = n;
    let remainingCols = n;
    let total = 0;

    for (let i = queries.length - 1; i >= 0; --i) {
        const [type, index, val] = queries[i];
        if (type === 0) { // row
            if (!rowSeen[index]) {
                rowSeen[index] = true;
                remainingRows--;
                total += val * remainingCols;
            }
        } else { // column
            if (!colSeen[index]) {
                colSeen[index] = true;
                remainingCols--;
                total += val * remainingRows;
            }
        }
    }

    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $queries
     * @return Integer
     */
    function matrixSumQueries($n, $queries) {
        $rowSeen = [];
        $colSeen = [];
        $remainingRows = $n;
        $remainingCols = $n;
        $total = 0;

        for ($i = count($queries) - 1; $i >= 0; --$i) {
            $type = $queries[$i][0];
            $idx  = $queries[$i][1];
            $val  = $queries[$i][2];

            if ($type == 0) { // row operation
                if (!isset($rowSeen[$idx])) {
                    $total += $val * $remainingCols;
                    $rowSeen[$idx] = true;
                    $remainingRows--;
                }
            } else { // column operation
                if (!isset($colSeen[$idx])) {
                    $total += $val * $remainingRows;
                    $colSeen[$idx] = true;
                    $remainingCols--;
                }
            }

            // early exit if all rows and columns are processed
            if ($remainingRows == 0 && $remainingCols == 0) {
                break;
            }
        }

        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func matrixSumQueries(_ n: Int, _ queries: [[Int]]) -> Int {
        var seenRows = Set<Int>()
        var seenCols = Set<Int>()
        var remainingRows = n
        var remainingCols = n
        var total: Int64 = 0

        for query in queries.reversed() {
            let type = query[0]
            let idx = query[1]
            let val = query[2]

            if type == 0 {
                if !seenRows.contains(idx) {
                    total += Int64(val) * Int64(remainingCols)
                    seenRows.insert(idx)
                    remainingRows -= 1
                }
            } else {
                if !seenCols.contains(idx) {
                    total += Int64(val) * Int64(remainingRows)
                    seenCols.insert(idx)
                    remainingCols -= 1
                }
            }

            if remainingRows == 0 && remainingCols == 0 {
                break
            }
        }

        return Int(total)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun matrixSumQueries(n: Int, queries: Array<IntArray>): Long {
        var total = 0L
        val rowSeen = BooleanArray(n)
        val colSeen = BooleanArray(n)
        var remainingRows = n
        var remainingCols = n

        for (i in queries.size - 1 downTo 0) {
            val q = queries[i]
            val type = q[0]
            val idx = q[1]
            val value = q[2].toLong()
            if (type == 0) { // row operation
                if (!rowSeen[idx]) {
                    total += value * remainingCols
                    rowSeen[idx] = true
                    remainingRows--
                }
            } else { // column operation
                if (!colSeen[idx]) {
                    total += value * remainingRows
                    colSeen[idx] = true
                    remainingCols--
                }
            }
        }

        return total
    }
}
```

## Dart

```dart
class Solution {
  int matrixSumQueries(int n, List<List<int>> queries) {
    final Set<int> seenRows = {};
    final Set<int> seenCols = {};
    int unseenRows = n;
    int unseenCols = n;
    int total = 0;

    for (int i = queries.length - 1; i >= 0; --i) {
      final q = queries[i];
      final type = q[0];
      final idx = q[1];
      final val = q[2];

      if (type == 0) {
        if (!seenRows.contains(idx)) {
          total += val * unseenCols;
          seenRows.add(idx);
          unseenRows--;
        }
      } else {
        if (!seenCols.contains(idx)) {
          total += val * unseenRows;
          seenCols.add(idx);
          unseenCols--;
        }
      }
    }

    return total;
  }
}
```

## Golang

```go
func matrixSumQueries(n int, queries [][]int) int64 {
	rowsSeen := make([]bool, n)
	colsSeen := make([]bool, n)
	remainingRows, remainingCols := n, n
	var total int64

	for i := len(queries) - 1; i >= 0; i-- {
		typ, idx, val := queries[i][0], queries[i][1], int64(queries[i][2])
		if typ == 0 { // row operation
			if !rowsSeen[idx] {
				rowsSeen[idx] = true
				total += val * int64(remainingCols)
				remainingRows--
			}
		} else { // column operation
			if !colsSeen[idx] {
				colsSeen[idx] = true
				total += val * int64(remainingRows)
				remainingCols--
			}
		}
	}
	return total
}
```

## Ruby

```ruby
def matrix_sum_queries(n, queries)
  seen_rows = Array.new(n, false)
  seen_cols = Array.new(n, false)
  rows_seen = 0
  cols_seen = 0
  total = 0

  (queries.length - 1).downto(0) do |i|
    type, idx, val = queries[i]
    if type == 0
      next if seen_rows[idx]
      total += val * (n - cols_seen)
      seen_rows[idx] = true
      rows_seen += 1
    else
      next if seen_cols[idx]
      total += val * (n - rows_seen)
      seen_cols[idx] = true
      cols_seen += 1
    end
  end

  total
end
```

## Scala

```scala
object Solution {
    def matrixSumQueries(n: Int, queries: Array[Array[Int]]): Long = {
        val rowSeen = new Array[Boolean](n)
        val colSeen = new Array[Boolean](n)
        var seenRows = 0
        var seenCols = 0
        var total: Long = 0L
        var i = queries.length - 1
        while (i >= 0) {
            val q = queries(i)
            val typ = q(0)
            val idx = q(1)
            val v = q(2).toLong
            if (typ == 0) { // row operation
                if (!rowSeen(idx)) {
                    total += v * (n - seenCols)
                    rowSeen(idx) = true
                    seenRows += 1
                }
            } else { // column operation
                if (!colSeen(idx)) {
                    total += v * (n - seenRows)
                    colSeen(idx) = true
                    seenCols += 1
                }
            }
            i -= 1
        }
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn matrix_sum_queries(n: i32, queries: Vec<Vec<i32>>) -> i64 {
        let n = n as usize;
        let mut row_seen = vec![false; n];
        let mut col_seen = vec![false; n];
        let mut remaining_rows = n;
        let mut remaining_cols = n;
        let mut total: i64 = 0;

        for q in queries.iter().rev() {
            let typ = q[0];
            let idx = q[1] as usize;
            let val = q[2] as i64;
            if typ == 0 {
                if !row_seen[idx] {
                    total += val * remaining_cols as i64;
                    row_seen[idx] = true;
                    remaining_rows -= 1;
                }
            } else {
                if !col_seen[idx] {
                    total += val * remaining_rows as i64;
                    col_seen[idx] = true;
                    remaining_cols -= 1;
                }
            }
        }

        total
    }
}
```

## Racket

```racket
(define/contract (matrix-sum-queries n queries)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ((len (length queries))
         (qvec (list->vector queries))
         (row-seen (make-vector n #f))
         (col-seen (make-vector n #f)))
    (let loop ((i (sub1 len))          ; current index in reversed order
               (rows-covered 0)        ; number of rows already fixed
               (cols-covered 0)        ; number of columns already fixed
               (total 0))              ; accumulated sum
      (if (< i 0)
          total
          (let* ((q (vector-ref qvec i))
                 (type (list-ref q 0))
                 (idx (list-ref q 1))
                 (val (list-ref q 2)))
            (cond
              [(= type 0) ; row operation
               (if (vector-ref row-seen idx)
                   (loop (sub1 i) rows-covered cols-covered total)
                   (let* ((unfixed-cols (- n cols-covered))
                          (add (* unfixed-cols val)))
                     (vector-set! row-seen idx #t)
                     (loop (sub1 i) (+ rows-covered 1) cols-covered (+ total add))))]
              [else ; column operation
               (if (vector-ref col-seen idx)
                   (loop (sub1 i) rows-covered cols-covered total)
                   (let* ((unfixed-rows (- n rows-covered))
                          (add (* unfixed-rows val)))
                     (vector-set! col-seen idx #t)
                     (loop (sub1 i) rows-covered (+ cols-covered 1) (+ total add))))]))))))
```

## Erlang

```erlang
-module(solution).
-export([matrix_sum_queries/2]).

-spec matrix_sum_queries(N :: integer(), Queries :: [[integer()]]) -> integer().
matrix_sum_queries(N, Queries) ->
    Rev = lists:reverse(Queries),
    process(Rev, N, N, #{}, #{}, 0).

process([], _RemRows, _RemCols, _RowSeen, _ColSeen, Sum) ->
    Sum;
process([[0, Index, Val] | Rest], RemRows, RemCols, RowSeen, ColSeen, Sum) ->
    case maps:is_key(Index, RowSeen) of
        true -> process(Rest, RemRows, RemCols, RowSeen, ColSeen, Sum);
        false ->
            NewSum = Sum + Val * RemCols,
            NewRowSeen = maps:put(Index, true, RowSeen),
            process(Rest, RemRows - 1, RemCols, NewRowSeen, ColSeen, NewSum)
    end;
process([[1, Index, Val] | Rest], RemRows, RemCols, RowSeen, ColSeen, Sum) ->
    case maps:is_key(Index, ColSeen) of
        true -> process(Rest, RemRows, RemCols, RowSeen, ColSeen, Sum);
        false ->
            NewSum = Sum + Val * RemRows,
            NewColSeen = maps:put(Index, true, ColSeen),
            process(Rest, RemRows, RemCols - 1, RowSeen, NewColSeen, NewSum)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec matrix_sum_queries(n :: integer, queries :: [[integer]]) :: integer
  def matrix_sum_queries(n, queries) do
    {total, _rows, _cols, _, _} =
      Enum.reduce(Enum.reverse(queries), {0, MapSet.new(), MapSet.new(), n, n}, fn
        [type, idx, val], {sum, rows, cols, rem_rows, rem_cols} ->
          cond do
            type == 0 and not MapSet.member?(rows, idx) ->
              contribution = val * rem_cols
              {
                sum + contribution,
                MapSet.put(rows, idx),
                cols,
                rem_rows - 1,
                rem_cols
              }

            type == 1 and not MapSet.member?(cols, idx) ->
              contribution = val * rem_rows
              {
                sum + contribution,
                rows,
                MapSet.put(cols, idx),
                rem_rows,
                rem_cols - 1
              }

            true ->
              {sum, rows, cols, rem_rows, rem_cols}
          end
      end)

    total
  end
end
```
