# 1582. Special Positions in a Binary Matrix

## Cpp

```cpp
class Solution {
public:
    int numSpecial(vector<vector<int>>& mat) {
        int m = mat.size();
        if (m == 0) return 0;
        int n = mat[0].size();
        vector<int> rowCount(m, 0), colCount(n, 0);
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (mat[i][j] == 1) {
                    ++rowCount[i];
                    ++colCount[j];
                }
            }
        }
        int ans = 0;
        for (int i = 0; i < m; ++i) {
            if (rowCount[i] != 1) continue;
            for (int j = 0; j < n; ++j) {
                if (mat[i][j] == 1 && colCount[j] == 1) {
                    ++ans;
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int numSpecial(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;
        int[] rowCount = new int[m];
        int[] colCount = new int[n];
        
        // Count ones in each row and column
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 1) {
                    rowCount[i]++;
                    colCount[j]++;
                }
            }
        }
        
        int ans = 0;
        // Find special positions
        for (int i = 0; i < m; i++) {
            if (rowCount[i] != 1) continue; // optional early skip
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 1 && colCount[j] == 1) {
                    ans++;
                }
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m = len(mat)
        n = len(mat[0]) if m else 0

        row_count = [0] * m
        col_count = [0] * n

        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    row_count[i] += 1
                    col_count[j] += 1

        ans = 0
        for i in range(m):
            if row_count[i] != 1:
                continue
            for j in range(n):
                if mat[i][j] and col_count[j] == 1:
                    ans += 1
                    break  # each qualifying row has at most one special column

        return ans
```

## Python3

```python
from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row_count = [0] * m
        col_count = [0] * n

        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    row_count[i] += 1
                    col_count[j] += 1

        ans = 0
        for i in range(m):
            if row_count[i] != 1:
                continue
            for j in range(n):
                if mat[i][j] and col_count[j] == 1:
                    ans += 1
                    break  # each qualifying row has at most one special column

        return ans
```

## C

```c
#include <stdlib.h>

int numSpecial(int** mat, int matSize, int* matColSize) {
    if (matSize == 0) return 0;
    int n = matColSize[0];
    int *rowCount = (int *)calloc(matSize, sizeof(int));
    int *colCount = (int *)calloc(n, sizeof(int));

    for (int i = 0; i < matSize; ++i) {
        for (int j = 0; j < n; ++j) {
            if (mat[i][j] == 1) {
                rowCount[i]++;
                colCount[j]++;
            }
        }
    }

    int ans = 0;
    for (int i = 0; i < matSize; ++i) {
        if (rowCount[i] != 1) continue;
        for (int j = 0; j < n; ++j) {
            if (mat[i][j] == 1 && colCount[j] == 1) {
                ans++;
                break; // each row can have at most one special element
            }
        }
    }

    free(rowCount);
    free(colCount);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int NumSpecial(int[][] mat) {
        int m = mat.Length;
        int n = mat[0].Length;
        int[] rowCount = new int[m];
        int[] colCount = new int[n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 1) {
                    rowCount[i]++;
                    colCount[j]++;
                }
            }
        }

        int ans = 0;
        for (int i = 0; i < m; i++) {
            if (rowCount[i] != 1) continue; // optional early skip
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 1 && colCount[j] == 1) {
                    ans++;
                }
            }
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} mat
 * @return {number}
 */
var numSpecial = function(mat) {
    const m = mat.length;
    const n = mat[0].length;
    const rowCount = new Array(m).fill(0);
    const colCount = new Array(n).fill(0);
    
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (mat[i][j] === 1) {
                rowCount[i]++;
                colCount[j]++;
            }
        }
    }
    
    let ans = 0;
    for (let i = 0; i < m; i++) {
        if (rowCount[i] !== 1) continue; // optional early skip
        for (let j = 0; j < n; j++) {
            if (mat[i][j] === 1 && colCount[j] === 1) {
                ans++;
            }
        }
    }
    
    return ans;
};
```

## Typescript

```typescript
function numSpecial(mat: number[][]): number {
    const m = mat.length;
    const n = mat[0].length;
    const rowCounts = new Array(m).fill(0);
    const colCounts = new Array(n).fill(0);
    
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (mat[i][j] === 1) {
                rowCounts[i]++;
                colCounts[j]++;
            }
        }
    }
    
    let ans = 0;
    for (let i = 0; i < m; i++) {
        if (rowCounts[i] !== 1) continue;
        for (let j = 0; j < n; j++) {
            if (mat[i][j] === 1 && colCounts[j] === 1) {
                ans++;
            }
        }
    }
    
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $mat
     * @return Integer
     */
    function numSpecial($mat) {
        $m = count($mat);
        $n = count($mat[0]);
        $rowCount = array_fill(0, $m, 0);
        $colCount = array_fill(0, $n, 0);

        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($mat[$i][$j] == 1) {
                    $rowCount[$i]++;
                    $colCount[$j]++;
                }
            }
        }

        $ans = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($mat[$i][$j] == 1 && $rowCount[$i] == 1 && $colCount[$j] == 1) {
                    $ans++;
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
    func numSpecial(_ mat: [[Int]]) -> Int {
        let m = mat.count
        guard m > 0 else { return 0 }
        let n = mat[0].count
        
        var rowCount = Array(repeating: 0, count: m)
        var colCount = Array(repeating: 0, count: n)
        
        for i in 0..<m {
            for j in 0..<n {
                if mat[i][j] == 1 {
                    rowCount[i] += 1
                    colCount[j] += 1
                }
            }
        }
        
        var ans = 0
        for i in 0..<m where rowCount[i] == 1 {
            for j in 0..<n {
                if mat[i][j] == 1 && colCount[j] == 1 {
                    ans += 1
                }
            }
        }
        
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numSpecial(mat: Array<IntArray>): Int {
        val m = mat.size
        if (m == 0) return 0
        val n = mat[0].size
        val rowCount = IntArray(m)
        val colCount = IntArray(n)

        for (i in 0 until m) {
            for (j in 0 until n) {
                if (mat[i][j] == 1) {
                    rowCount[i]++
                    colCount[j]++
                }
            }
        }

        var ans = 0
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (mat[i][j] == 1 && rowCount[i] == 1 && colCount[j] == 1) {
                    ans++
                }
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int numSpecial(List<List<int>> mat) {
    int m = mat.length;
    int n = mat[0].length;
    List<int> rowCount = List.filled(m, 0);
    List<int> colCount = List.filled(n, 0);

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (mat[i][j] == 1) {
          rowCount[i]++;
          colCount[j]++;
        }
      }
    }

    int ans = 0;
    for (int i = 0; i < m; i++) {
      if (rowCount[i] != 1) continue;
      for (int j = 0; j < n; j++) {
        if (mat[i][j] == 1 && colCount[j] == 1) {
          ans++;
        }
      }
    }

    return ans;
  }
}
```

## Golang

```go
func numSpecial(mat [][]int) int {
	m := len(mat)
	if m == 0 {
		return 0
	}
	n := len(mat[0])
	rowCount := make([]int, m)
	colCount := make([]int, n)

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if mat[i][j] == 1 {
				rowCount[i]++
				colCount[j]++
			}
		}
	}

	ans := 0
	for i := 0; i < m; i++ {
		if rowCount[i] != 1 {
			continue
		}
		for j := 0; j < n; j++ {
			if mat[i][j] == 1 && colCount[j] == 1 {
				ans++
				break // since rowCount[i]==1, no other 1 in this row
			}
		}
	}
	return ans
}
```

## Ruby

```ruby
def num_special(mat)
  m = mat.length
  n = mat[0].length
  row_counts = Array.new(m, 0)
  col_counts = Array.new(n, 0)

  mat.each_with_index do |row, i|
    row.each_with_index do |val, j|
      if val == 1
        row_counts[i] += 1
        col_counts[j] += 1
      end
    end
  end

  ans = 0
  mat.each_with_index do |row, i|
    row.each_with_index do |val, j|
      if val == 1 && row_counts[i] == 1 && col_counts[j] == 1
        ans += 1
      end
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def numSpecial(mat: Array[Array[Int]]): Int = {
        val m = mat.length
        if (m == 0) return 0
        val n = mat(0).length
        val rowCount = new Array[Int](m)
        val colCount = new Array[Int](n)

        for (i <- 0 until m) {
            for (j <- 0 until n) {
                if (mat(i)(j) == 1) {
                    rowCount(i) += 1
                    colCount(j) += 1
                }
            }
        }

        var ans = 0
        for (i <- 0 until m) {
            for (j <- 0 until n) {
                if (mat(i)(j) == 1 && rowCount(i) == 1 && colCount(j) == 1) {
                    ans += 1
                }
            }
        }
        ans
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn num_special(mat: Vec<Vec<i32>>) -> i32 {
        let m = mat.len();
        if m == 0 {
            return 0;
        }
        let n = mat[0].len();

        let mut row_cnt = vec![0usize; m];
        let mut col_cnt = vec![0usize; n];

        for i in 0..m {
            for j in 0..n {
                if mat[i][j] == 1 {
                    row_cnt[i] += 1;
                    col_cnt[j] += 1;
                }
            }
        }

        let mut ans = 0i32;
        for i in 0..m {
            if row_cnt[i] != 1 {
                continue;
            }
            for j in 0..n {
                if mat[i][j] == 1 && col_cnt[j] == 1 {
                    ans += 1;
                }
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (num-special mat)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((m (length mat))
         (n (if (null? mat) 0 (length (car mat))))
         (row-counts (make-vector m 0))
         (col-counts (make-vector n 0)))
    ;; First pass: count ones per row and column
    (for ([i (in-range m)]
          [row (in-list mat)])
      (for ([j (in-range n)]
            [val (in-list row)])
        (when (= val 1)
          (vector-set! row-counts i (+ (vector-ref row-counts i) 1))
          (vector-set! col-counts j (+ (vector-ref col-counts j) 1)))))
    ;; Second pass: count special positions
    (let ((ans 0))
      (for ([i (in-range m)]
            [row (in-list mat)])
        (for ([j (in-range n)]
              [val (in-list row)])
          (when (and (= val 1)
                     (= (vector-ref row-counts i) 1)
                     (= (vector-ref col-counts j) 1))
            (set! ans (+ ans 1)))))
      ans)))
```

## Erlang

```erlang
-module(solution).
-export([num_special/1]).

-spec num_special(Mat :: [[integer()]]) -> integer().
num_special(Mat) ->
    RowCounts = [lists:sum(Row) || Row <- Mat],
    N = case Mat of
            [] -> 0;
            [First|_] -> length(First)
        end,
    ColCounts = col_counts(Mat, N),
    count_special(Mat, RowCounts, ColCounts, 0).

%% Compute column counts by folding rows into an accumulator list.
col_counts(Rows, N) ->
    Init = lists:duplicate(N, 0),
    col_counts(Rows, Init).

col_counts([], Acc) -> Acc;
col_counts([Row|Rest], Acc) ->
    NewAcc = lists:zipwith(fun(E, S) -> E + S end, Row, Acc),
    col_counts(Rest, NewAcc).

%% Iterate over rows together with their row counts.
count_special(_, [], _, Acc) -> Acc;
count_special([], [], _, Acc) -> Acc;
count_special([Row|RestRows], [Rcnt|RestRCnts], ColCounts, Acc) ->
    Zipped = lists:zip(Row, ColCounts),
    RowAcc = count_row(Zipped, Rcnt, 0),
    count_special(RestRows, RestRCnts, ColCounts, Acc + RowAcc).

%% Count special positions within a single row.
count_row([], _, Acc) -> Acc;
count_row([{Val, Ccnt}|Rest], Rcnt, Acc) ->
    NewAcc = if Val == 1, Rcnt == 1, Ccnt == 1 -> Acc + 1; true -> Acc end,
    count_row(Rest, Rcnt, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec num_special(mat :: [[integer]]) :: integer
  def num_special(mat) do
    m = length(mat)
    n = mat |> List.first() |> length()

    row_counts =
      Enum.map(mat, fn row ->
        Enum.count(row, &(&1 == 1))
      end)

    col_counts =
      for j <- 0..(n - 1) do
        Enum.reduce(mat, 0, fn row, acc ->
          if Enum.at(row, j) == 1, do: acc + 1, else: acc
        end)
      end

    Enum.with_index(mat)
    |> Enum.reduce(0, fn {row, i}, ans ->
      Enum.with_index(row)
      |> Enum.reduce(ans, fn {val, j}, inner_ans ->
        if val == 1 and Enum.at(row_counts, i) == 1 and Enum.at(col_counts, j) == 1 do
          inner_ans + 1
        else
          inner_ans
        end
      end)
    end)
  end
end
```
