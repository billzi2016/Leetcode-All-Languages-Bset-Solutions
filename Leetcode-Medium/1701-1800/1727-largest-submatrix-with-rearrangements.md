# 1727. Largest Submatrix With Rearrangements

## Cpp

```cpp
class Solution {
public:
    int largestSubmatrix(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        vector<int> heights(n, 0);
        int best = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (matrix[i][j] == 1) {
                    heights[j] += 1;
                } else {
                    heights[j] = 0;
                }
            }
            vector<int> sorted = heights;
            sort(sorted.begin(), sorted.end(), greater<int>());
            for (int k = 0; k < n; ++k) {
                int area = sorted[k] * (k + 1);
                if (area > best) best = area;
            }
        }
        return best;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int largestSubmatrix(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        int ans = 0;

        for (int i = 0; i < m; i++) {
            // update heights
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 1 && i > 0) {
                    matrix[i][j] += matrix[i - 1][j];
                }
            }

            // sort current row in descending order
            Integer[] cur = new Integer[n];
            for (int j = 0; j < n; j++) {
                cur[j] = matrix[i][j];
            }
            Arrays.sort(cur, Collections.reverseOrder());

            // compute max area with this baseline
            for (int k = 0; k < n; k++) {
                int area = cur[k] * (k + 1);
                if (area > ans) {
                    ans = area;
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
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    if i:
                        matrix[i][j] += matrix[i-1][j]
            row_sorted = sorted(matrix[i], reverse=True)
            for k, h in enumerate(row_sorted):
                area = h * (k + 1)
                if area > ans:
                    ans = area
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        heights = [0] * n
        ans = 0
        for r in range(m):
            row = matrix[r]
            for c in range(n):
                if row[c]:
                    heights[c] += 1
                else:
                    heights[c] = 0
            sorted_heights = sorted(heights, reverse=True)
            for i, h in enumerate(sorted_heights):
                area = h * (i + 1)
                if area > ans:
                    ans = area
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int cmp_desc(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    if (va < vb) return 1;
    if (va > vb) return -1;
    return 0;
}

int largestSubmatrix(int** matrix, int matrixSize, int* matrixColSize) {
    int m = matrixSize;
    if (m == 0) return 0;
    int n = matrixColSize[0];
    int ans = 0;

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (matrix[i][j]) {
                if (i > 0) matrix[i][j] += matrix[i - 1][j];
            }
        }

        int *rowCopy = (int *)malloc(n * sizeof(int));
        memcpy(rowCopy, matrix[i], n * sizeof(int));

        qsort(rowCopy, n, sizeof(int), cmp_desc);

        for (int k = 0; k < n; ++k) {
            int area = rowCopy[k] * (k + 1);
            if (area > ans) ans = area;
        }

        free(rowCopy);
    }

    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int LargestSubmatrix(int[][] matrix)
    {
        int m = matrix.Length;
        int n = matrix[0].Length;
        int[] heights = new int[n];
        int maxArea = 0;

        for (int i = 0; i < m; i++)
        {
            // Update consecutive ones height for each column
            for (int j = 0; j < n; j++)
            {
                if (matrix[i][j] == 1)
                    heights[j]++;
                else
                    heights[j] = 0;
            }

            // Sort a copy of heights to simulate optimal column rearrangement
            int[] sorted = (int[])heights.Clone();
            Array.Sort(sorted); // ascending

            // Compute max area using descending order values
            for (int k = 0; k < n; k++)
            {
                int height = sorted[n - 1 - k]; // kth largest height
                int area = height * (k + 1);
                if (area > maxArea)
                    maxArea = area;
            }
        }

        return maxArea;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} matrix
 * @return {number}
 */
var largestSubmatrix = function(matrix) {
    const m = matrix.length;
    const n = matrix[0].length;
    const heights = new Array(n).fill(0);
    let maxArea = 0;

    for (let i = 0; i < m; ++i) {
        // update consecutive ones height for each column
        for (let j = 0; j < n; ++j) {
            if (matrix[i][j] === 1) {
                heights[j] += 1;
            } else {
                heights[j] = 0;
            }
        }

        // sort heights in descending order to simulate column rearrangement
        const sorted = heights.slice().sort((a, b) => b - a);
        for (let k = 0; k < n; ++k) {
            const area = sorted[k] * (k + 1);
            if (area > maxArea) maxArea = area;
        }
    }

    return maxArea;
};
```

## Typescript

```typescript
function largestSubmatrix(matrix: number[][]): number {
    const m = matrix.length;
    const n = matrix[0].length;
    let prev = new Array<number>(n).fill(0);
    let maxArea = 0;

    for (let i = 0; i < m; i++) {
        const curr = new Array<number>(n);
        for (let j = 0; j < n; j++) {
            if (matrix[i][j] === 1) {
                curr[j] = prev[j] + 1;
            } else {
                curr[j] = 0;
            }
        }

        const sorted = curr.slice().sort((a, b) => b - a);
        for (let k = 0; k < n; k++) {
            const area = sorted[k] * (k + 1);
            if (area > maxArea) maxArea = area;
        }

        prev = curr;
    }

    return maxArea;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $matrix
     * @return Integer
     */
    function largestSubmatrix($matrix) {
        $m = count($matrix);
        if ($m == 0) return 0;
        $n = count($matrix[0]);
        $ans = 0;

        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($matrix[$i][$j] == 1) {
                    if ($i > 0) {
                        $matrix[$i][$j] += $matrix[$i - 1][$j];
                    }
                } else {
                    // keep zero, streak resets
                }
            }

            $row = $matrix[$i];
            rsort($row, SORT_NUMERIC); // descending

            for ($k = 0; $k < $n; $k++) {
                $area = $row[$k] * ($k + 1);
                if ($area > $ans) {
                    $ans = $area;
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
    func largestSubmatrix(_ matrix: [[Int]]) -> Int {
        let m = matrix.count
        guard m > 0 else { return 0 }
        let n = matrix[0].count
        var heights = [Int](repeating: 0, count: n)
        var maxArea = 0
        
        for i in 0..<m {
            // Update consecutive ones height for each column
            for j in 0..<n {
                if matrix[i][j] == 1 {
                    heights[j] += 1
                } else {
                    heights[j] = 0
                }
            }
            
            // Sort heights descending to simulate optimal column rearrangement
            var sortedHeights = heights
            sortedHeights.sort(by: >)
            
            // Compute maximal area using current row as bottom of submatrix
            for (idx, h) in sortedHeights.enumerated() {
                let area = h * (idx + 1)
                if area > maxArea {
                    maxArea = area
                }
            }
        }
        
        return maxArea
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun largestSubmatrix(matrix: Array<IntArray>): Int {
        val m = matrix.size
        val n = matrix[0].size
        val heights = IntArray(n)
        var maxArea = 0
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (matrix[i][j] == 1) {
                    heights[j] += 1
                } else {
                    heights[j] = 0
                }
            }
            val sorted = heights.clone()
            java.util.Arrays.sort(sorted) // ascending order
            var width = 1
            for (k in n - 1 downTo 0) {
                val h = sorted[k]
                if (h == 0) break
                val area = h * width
                if (area > maxArea) maxArea = area
                width++
            }
        }
        return maxArea
    }
}
```

## Dart

```dart
class Solution {
  int largestSubmatrix(List<List<int>> matrix) {
    int m = matrix.length;
    int n = matrix[0].length;
    List<int> heights = List.filled(n, 0);
    int ans = 0;

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (matrix[i][j] == 1) {
          heights[j] += 1;
        } else {
          heights[j] = 0;
        }
      }

      List<int> cur = List.from(heights);
      cur.sort((a, b) => b.compareTo(a));

      for (int k = 0; k < n; k++) {
        int area = cur[k] * (k + 1);
        if (area > ans) ans = area;
      }
    }

    return ans;
  }
}
```

## Golang

```go
import "sort"

func largestSubmatrix(matrix [][]int) int {
	m := len(matrix)
	if m == 0 {
		return 0
	}
	n := len(matrix[0])
	heights := make([]int, n)
	tmp := make([]int, n)
	ans := 0

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if matrix[i][j] == 1 {
				heights[j]++
			} else {
				heights[j] = 0
			}
		}
		copy(tmp, heights)
		sort.Ints(tmp) // ascending

		for k := 0; k < n; k++ {
			h := tmp[n-1-k]      // descending order
			area := h * (k + 1) // width = k+1
			if area > ans {
				ans = area
			}
		}
	}
	return ans
}
```

## Ruby

```ruby
def largest_submatrix(matrix)
  m = matrix.size
  n = matrix[0].size
  heights = Array.new(n, 0)
  max_area = 0

  matrix.each do |row|
    row.each_with_index do |val, j|
      if val == 1
        heights[j] += 1
      else
        heights[j] = 0
      end
    end

    sorted = heights.sort.reverse
    sorted.each_with_index do |h, i|
      area = h * (i + 1)
      max_area = area if area > max_area
    end
  end

  max_area
end
```

## Scala

```scala
object Solution {
    def largestSubmatrix(matrix: Array[Array[Int]]): Int = {
        val m = matrix.length
        val n = matrix(0).length
        var ans = 0
        val heights = new Array[Int](n)
        import java.util.Arrays

        for (i <- 0 until m) {
            var j = 0
            while (j < n) {
                if (matrix(i)(j) == 1) heights(j) += 1 else heights(j) = 0
                j += 1
            }
            val sorted = heights.clone()
            Arrays.sort(sorted) // ascending

            var k = 0
            while (k < n) {
                val h = sorted(n - 1 - k) // descending order
                val area = h * (k + 1)
                if (area > ans) ans = area
                k += 1
            }
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn largest_submatrix(matrix: Vec<Vec<i32>>) -> i32 {
        let m = matrix.len();
        if m == 0 {
            return 0;
        }
        let n = matrix[0].len();
        let mut heights = vec![0i32; n];
        let mut ans = 0i32;

        for row in matrix.iter() {
            for (j, &val) in row.iter().enumerate() {
                if val == 1 {
                    heights[j] += 1;
                } else {
                    heights[j] = 0;
                }
            }

            let mut sorted = heights.clone();
            sorted.sort_unstable_by(|a, b| b.cmp(a)); // descending

            for (i, &h) in sorted.iter().enumerate() {
                if h == 0 {
                    break;
                }
                let area = h * ((i + 1) as i32);
                if area > ans {
                    ans = area;
                }
            }
        }

        ans
    }
}
```

## Racket

```racket
#lang racket

(define/contract (largest-submatrix matrix)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((m (length matrix))
         (n (if (null? matrix) 0 (length (car matrix))))
         (row-vecs (map list->vector matrix))
         (heights (make-vector n 0)))
    (let ((ans 0))
      (for ([row row-vecs])
        (for ([i (in-range n)])
          (if (= (vector-ref row i) 1)
              (vector-set! heights i (+ (vector-ref heights i) 1))
              (vector-set! heights i 0)))
        (let ((sorted (sort (vector->list heights) >)))
          (for ([h sorted] [idx (in-naturals 1)])
            (when (> (* h idx) ans)
                  (set! ans (* h idx))))))
      ans)))
```

## Erlang

```erlang
-spec largest_submatrix(Matrix :: [[integer()]]) -> integer().
largest_submatrix(Matrix) ->
    case Matrix of
        [] -> 0;
        [FirstRow|_] ->
            N = length(FirstRow),
            ZeroPrev = lists:duplicate(N, 0),
            process_rows(Matrix, ZeroPrev, 0)
    end.

process_rows([], _Prev, Max) -> Max;
process_rows([Row | Rows], Prev, MaxSoFar) ->
    Curr = compute_heights(Row, Prev),
    RowArea = row_max_area(Curr),
    NewMax = if RowArea > MaxSoFar -> RowArea; true -> MaxSoFar end,
    process_rows(Rows, Curr, NewMax).

compute_heights([], []) -> [];
compute_heights([R | Rs], [P | Ps]) ->
    H = case R of
            1 -> P + 1;
            _ -> 0
        end,
    [H | compute_heights(Rs, Ps)].

row_max_area(Heights) ->
    Sorted = lists:sort(fun(A, B) -> A > B end, Heights),
    row_max_area(Sorted, 1, 0).

row_max_area([], _Idx, Max) -> Max;
row_max_area([H | Rest], Idx, Max) ->
    Area = H * Idx,
    NewMax = if Area > Max -> Area; true -> Max end,
    row_max_area(Rest, Idx + 1, NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec largest_submatrix(matrix :: [[integer]]) :: integer
  def largest_submatrix(matrix) do
    # Number of columns (assumes matrix is non‑empty)
    n = length(List.first(matrix))

    # Initial heights are all zero
    initial_heights = List.duplicate(0, n)

    {_final_heights, answer} =
      Enum.reduce(matrix, {initial_heights, 0}, fn row, {prev_heights, best} ->
        # Update consecutive ones height for each column
        new_heights =
          Enum.map(Enum.zip(row, prev_heights), fn
            {1, h} -> h + 1
            {_val, _h} -> 0
          end)

        # Sort heights descending to simulate optimal column rearrangement
        sorted = Enum.sort(new_heights, &>=/2)

        # Compute maximal area for this row as the bottom of the submatrix
        current_best =
          sorted
          |> Enum.with_index(1)
          |> Enum.reduce(best, fn {h, idx}, acc ->
            area = h * idx
            if area > acc, do: area, else: acc
          end)

        {new_heights, current_best}
      end)

    answer
  end
end
```
