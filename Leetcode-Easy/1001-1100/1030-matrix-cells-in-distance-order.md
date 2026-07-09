# 1030. Matrix Cells in Distance Order

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> allCellsDistOrder(int rows, int cols, int rCenter, int cCenter) {
        vector<vector<int>> cells;
        cells.reserve(rows * cols);
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                cells.push_back({i, j});
            }
        }
        sort(cells.begin(), cells.end(),
             [&](const vector<int>& a, const vector<int>& b) {
                 int da = abs(a[0] - rCenter) + abs(a[1] - cCenter);
                 int db = abs(b[0] - rCenter) + abs(b[1] - cCenter);
                 return da < db;
             });
        return cells;
    }
};
```

## Java

```java
class Solution {
    public int[][] allCellsDistOrder(int rows, int cols, int rCenter, int cCenter) {
        int total = rows * cols;
        int maxDist = rows + cols - 2; // maximum possible Manhattan distance
        @SuppressWarnings("unchecked")
        java.util.ArrayList<int[]>[] buckets = new java.util.ArrayList[maxDist + 1];

        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                int d = Math.abs(r - rCenter) + Math.abs(c - cCenter);
                if (buckets[d] == null) {
                    buckets[d] = new java.util.ArrayList<>();
                }
                buckets[d].add(new int[]{r, c});
            }
        }

        int[][] result = new int[total][2];
        int idx = 0;
        for (int d = 0; d <= maxDist; ++d) {
            if (buckets[d] != null) {
                for (int[] cell : buckets[d]) {
                    result[idx++] = cell;
                }
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        cells = [[r, c] for r in range(rows) for c in range(cols)]
        cells.sort(key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))
        return cells
```

## Python3

```python
from typing import List

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        cells = [[r, c] for r in range(rows) for c in range(cols)]
        cells.sort(key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))
        return cells
```

## C

```c
#include <stdlib.h>

struct Cell {
    int r;
    int c;
    int d;
};

static int cmpCell(const void *a, const void *b) {
    const struct Cell *c1 = (const struct Cell *)a;
    const struct Cell *c2 = (const struct Cell *)b;
    if (c1->d != c2->d) return c1->d - c2->d;
    if (c1->r != c2->r) return c1->r - c2->r;
    return c1->c - c2->c;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** allCellsDistOrder(int rows, int cols, int rCenter, int cCenter, int* returnSize, int** returnColumnSizes) {
    int total = rows * cols;
    struct Cell *cells = (struct Cell *)malloc(total * sizeof(struct Cell));
    int idx = 0;
    for (int r = 0; r < rows; ++r) {
        for (int c = 0; c < cols; ++c) {
            cells[idx].r = r;
            cells[idx].c = c;
            cells[idx].d = abs(r - rCenter) + abs(c - cCenter);
            ++idx;
        }
    }

    qsort(cells, total, sizeof(struct Cell), cmpCell);

    int **result = (int **)malloc(total * sizeof(int *));
    *returnColumnSizes = (int *)malloc(total * sizeof(int));
    for (int i = 0; i < total; ++i) {
        result[i] = (int *)malloc(2 * sizeof(int));
        result[i][0] = cells[i].r;
        result[i][1] = cells[i].c;
        (*returnColumnSizes)[i] = 2;
    }

    free(cells);
    *returnSize = total;
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int[][] AllCellsDistOrder(int rows, int cols, int rCenter, int cCenter) {
        int total = rows * cols;
        int[][] cells = new int[total][];
        int idx = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                cells[idx++] = new int[] { i, j };
            }
        }
        System.Array.Sort(cells, (a, b) => {
            int d1 = System.Math.Abs(a[0] - rCenter) + System.Math.Abs(a[1] - cCenter);
            int d2 = System.Math.Abs(b[0] - rCenter) + System.Math.Abs(b[1] - cCenter);
            return d1.CompareTo(d2);
        });
        return cells;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} rows
 * @param {number} cols
 * @param {number} rCenter
 * @param {number} cCenter
 * @return {number[][]}
 */
var allCellsDistOrder = function(rows, cols, rCenter, cCenter) {
    const maxDist = rows + cols - 2;
    const buckets = Array.from({ length: maxDist + 1 }, () => []);
    
    for (let r = 0; r < rows; ++r) {
        for (let c = 0; c < cols; ++c) {
            const d = Math.abs(r - rCenter) + Math.abs(c - cCenter);
            buckets[d].push([r, c]);
        }
    }
    
    const result = [];
    for (let d = 0; d <= maxDist; ++d) {
        if (buckets[d].length) {
            result.push(...buckets[d]);
        }
    }
    return result;
};
```

## Typescript

```typescript
function allCellsDistOrder(rows: number, cols: number, rCenter: number, cCenter: number): number[][] {
    const cells: number[][] = [];
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            cells.push([r, c]);
        }
    }
    cells.sort((a, b) => {
        const d1 = Math.abs(a[0] - rCenter) + Math.abs(a[1] - cCenter);
        const d2 = Math.abs(b[0] - rCenter) + Math.abs(b[1] - cCenter);
        return d1 - d2;
    });
    return cells;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $rows
     * @param Integer $cols
     * @param Integer $rCenter
     * @param Integer $cCenter
     * @return Integer[][]
     */
    function allCellsDistOrder($rows, $cols, $rCenter, $cCenter) {
        $cells = [];
        for ($i = 0; $i < $rows; $i++) {
            for ($j = 0; $j < $cols; $j++) {
                $cells[] = [$i, $j];
            }
        }

        usort($cells, function($a, $b) use ($rCenter, $cCenter) {
            $da = abs($a[0] - $rCenter) + abs($a[1] - $cCenter);
            $db = abs($b[0] - $rCenter) + abs($b[1] - $cCenter);
            if ($da == $db) return 0;
            return ($da < $db) ? -1 : 1;
        });

        return $cells;
    }
}
```

## Swift

```swift
class Solution {
    func allCellsDistOrder(_ rows: Int, _ cols: Int, _ rCenter: Int, _ cCenter: Int) -> [[Int]] {
        var cells = [[Int]]()
        cells.reserveCapacity(rows * cols)
        for r in 0..<rows {
            for c in 0..<cols {
                cells.append([r, c])
            }
        }
        cells.sort { (a, b) -> Bool in
            let d1 = abs(a[0] - rCenter) + abs(a[1] - cCenter)
            let d2 = abs(b[0] - rCenter) + abs(b[1] - cCenter)
            return d1 < d2
        }
        return cells
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun allCellsDistOrder(rows: Int, cols: Int, rCenter: Int, cCenter: Int): Array<IntArray> {
        val total = rows * cols
        val cells = Array(total) { IntArray(2) }
        var idx = 0
        for (r in 0 until rows) {
            for (c in 0 until cols) {
                cells[idx][0] = r
                cells[idx][1] = c
                idx++
            }
        }
        java.util.Arrays.sort(cells) { a, b ->
            val d1 = kotlin.math.abs(a[0] - rCenter) + kotlin.math.abs(a[1] - cCenter)
            val d2 = kotlin.math.abs(b[0] - rCenter) + kotlin.math.abs(b[1] - cCenter)
            d1 - d2
        }
        return cells
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> allCellsDistOrder(int rows, int cols, int rCenter, int cCenter) {
    List<List<int>> cells = [];
    for (int r = 0; r < rows; ++r) {
      for (int c = 0; c < cols; ++c) {
        cells.add([r, c]);
      }
    }
    cells.sort((a, b) {
      int d1 = (a[0] - rCenter).abs() + (a[1] - cCenter).abs();
      int d2 = (b[0] - rCenter).abs() + (b[1] - cCenter).abs();
      return d1.compareTo(d2);
    });
    return cells;
  }
}
```

## Golang

```go
func allCellsDistOrder(rows int, cols int, rCenter int, cCenter int) [][]int {
	type cell struct{ r, c int }
	cells := make([]cell, 0, rows*cols)
	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			cells = append(cells, cell{i, j})
		}
	}
	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}
	sort.Slice(cells, func(i, j int) bool {
		d1 := abs(cells[i].r-rCenter) + abs(cells[i].c-cCenter)
		d2 := abs(cells[j].r-rCenter) + abs(cells[j].c-cCenter)
		if d1 == d2 {
			if cells[i].r == cells[j].r {
				return cells[i].c < cells[j].c
			}
			return cells[i].r < cells[j].r
		}
		return d1 < d2
	})
	ans := make([][]int, len(cells))
	for i, c := range cells {
		ans[i] = []int{c.r, c.c}
	}
	return ans
}

import "sort"
```

## Ruby

```ruby
def all_cells_dist_order(rows, cols, r_center, c_center)
  cells = []
  rows.times do |r|
    cols.times do |c|
      cells << [r, c]
    end
  end
  cells.sort_by! { |r, c| (r - r_center).abs + (c - c_center).abs }
end
```

## Scala

```scala
object Solution {
    def allCellsDistOrder(rows: Int, cols: Int, rCenter: Int, cCenter: Int): Array[Array[Int]] = {
        val cells = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
        for (r <- 0 until rows; c <- 0 until cols) {
            cells += Array(r, c)
        }
        cells.sortBy(cell => math.abs(cell(0) - rCenter) + math.abs(cell(1) - cCenter)).toArray
    }
}
```

## Rust

```rust
impl Solution {
    pub fn all_cells_dist_order(rows: i32, cols: i32, r_center: i32, c_center: i32) -> Vec<Vec<i32>> {
        let mut cells = Vec::with_capacity((rows * cols) as usize);
        for r in 0..rows {
            for c in 0..cols {
                let d = (r - r_center).abs() + (c - c_center).abs();
                cells.push((d, r, c));
            }
        }
        cells.sort_by_key(|k| k.0);
        cells.into_iter().map(|(_, r, c)| vec![r, c]).collect()
    }
}
```

## Racket

```racket
#lang racket

(define/contract (all-cells-dist-order rows cols rCenter cCenter)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?
      (listof (listof exact-integer?)))
  (let* ([cells (for*/list ([r (in-range rows)]
                            [c (in-range cols)])
                  (list r c))]
         [dist (lambda (cell)
                 (+ (abs (- (first cell) rCenter))
                    (abs (- (second cell) cCenter)) ))]
         [cmp (lambda (a b)
                (let ([da (dist a)]
                      [db (dist b)])
                  (cond [(< da db) #t]
                        [(> da db) #f]
                        [else (or (< (first a) (first b))
                                  (and (= (first a) (first b))
                                       (< (second a) (second b))))])))])
    (sort cells cmp)))
```

## Erlang

```erlang
-spec all_cells_dist_order(Rows :: integer(), Cols :: integer(), RCenter :: integer(), CCenter :: integer()) -> [[integer()]].
all_cells_dist_order(Rows, Cols, RCenter, CCenter) ->
    Cells = [{erlang:abs(R - RCenter) + erlang:abs(C - CCenter), R, C}
             || R <- lists:seq(0, Rows - 1),
                C <- lists:seq(0, Cols - 1)],
    Sorted = lists:keysort(1, Cells),
    [[R, C] || {_Dist, R, C} <- Sorted].
```

## Elixir

```elixir
defmodule Solution do
  @spec all_cells_dist_order(rows :: integer, cols :: integer, r_center :: integer, c_center :: integer) :: [[integer]]
  def all_cells_dist_order(rows, cols, r_center, c_center) do
    cells =
      for r <- 0..(rows - 1),
          c <- 0..(cols - 1) do
        [r, c]
      end

    Enum.sort_by(cells, fn [r, c] ->
      abs(r - r_center) + abs(c - c_center)
    end)
  end
end
```
