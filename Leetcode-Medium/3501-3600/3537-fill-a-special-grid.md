# 3537. Fill a Special Grid

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> specialGrid(int n) {
        if (n == 0) return {{0}};
        vector<vector<int>> prev = specialGrid(n - 1);
        int s = 1 << (n - 1);                 // size of subgrid
        int subsize = s * s;                  // number of cells in a quadrant
        vector<vector<int>> res(2 * s, vector<int>(2 * s));
        for (int i = 0; i < s; ++i) {
            for (int j = 0; j < s; ++j) {
                int val = prev[i][j];
                res[i][j] = val + 3 * subsize;          // top-left
                res[i][j + s] = val;                     // top-right
                res[i + s][j] = val + 2 * subsize;      // bottom-left
                res[i + s][j + s] = val + subsize;      // bottom-right
            }
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public int[][] specialGrid(int n) {
        return build(n);
    }
    
    private int[][] build(int n) {
        if (n == 0) {
            return new int[][]{{0}};
        }
        int[][] prev = build(n - 1);
        int m = prev.length;               // size of previous grid (2^{n-1})
        int sz = m * m;                    // number of cells in a quadrant
        int size = m << 1;                 // current grid size = 2^n
        int[][] res = new int[size][size];
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < m; j++) {
                int v = prev[i][j];
                res[i][j] = v + 3 * sz;          // top-left
                res[i][j + m] = v;               // top-right
                res[i + m][j] = v + 2 * sz;      // bottom-left
                res[i + m][j + m] = v + sz;      // bottom-right
            }
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def specialGrid(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def add_offset(mat, off):
            return [[val + off for val in row] for row in mat]

        def build(k, base):
            if k == 0:
                return [[base]]
            quarter = 4 ** (k - 1)  # number of cells in a sub‑grid
            sub = build(k - 1, 0)   # sub‑grid with values 0 .. quarter-1

            tl = add_offset(sub, base + 3 * quarter)
            tr = add_offset(sub, base)
            bl = add_offset(sub, base + 2 * quarter)
            br = add_offset(sub, base + quarter)

            top = [tl[i] + tr[i] for i in range(len(tl))]
            bottom = [bl[i] + br[i] for i in range(len(bl))]
            return top + bottom

        return build(n, 0)
```

## Python3

```python
from typing import List

class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        def build(k: int) -> List[List[int]]:
            if k == 0:
                return [[0]]
            sub = build(k - 1)
            sz = len(sub)
            block = sz * sz
            res = [[0] * (sz * 2) for _ in range(sz * 2)]
            for i in range(sz):
                for j in range(sz):
                    val = sub[i][j]
                    res[i][j] = val + 3 * block          # top‑left
                    res[i][j + sz] = val + 0 * block      # top‑right
                    res[i + sz][j] = val + 2 * block      # bottom‑left
                    res[i + sz][j + sz] = val + 1 * block # bottom‑right
            return res

        return build(n)
```

## C

```c
#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** specialGrid(int n, int* returnSize, int*** returnColumnSizes) {
    (void)returnColumnSizes; // placeholder to avoid unused warning if not used
    int size = 1 << n;
    *returnSize = size;

    /* Allocate column sizes array */
    int **colSizesPtr = (int**)malloc(sizeof(int*));
    *returnColumnSizes = (int*)malloc(size * sizeof(int));
    for (int i = 0; i < size; ++i) {
        (*returnColumnSizes)[i] = size;
    }

    /* Initialize grid with the base case */
    int curSize = 1;
    int **grid = (int**)malloc(sizeof(int*));
    grid[0] = (int*)malloc(sizeof(int));
    grid[0][0] = 0;

    for (int lvl = 1; lvl <= n; ++lvl) {
        int m = curSize;
        int newSize = m * 2;
        int c = m * m;               // number of cells in a quadrant

        /* Allocate new grid */
        int **newGrid = (int**)malloc(newSize * sizeof(int*));
        for (int i = 0; i < newSize; ++i) {
            newGrid[i] = (int*)malloc(newSize * sizeof(int));
        }

        /* Fill quadrants with appropriate offsets */
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < m; ++j) {
                int val = grid[i][j];
                newGrid[i][j]           = val + 3 * c;   // top‑left
                newGrid[i][j + m]       = val;           // top‑right
                newGrid[i + m][j]       = val + 2 * c;   // bottom‑left
                newGrid[i + m][j + m]   = val + c;       // bottom‑right
            }
        }

        /* Free old grid */
        for (int i = 0; i < m; ++i) {
            free(grid[i]);
        }
        free(grid);

        grid = newGrid;
        curSize = newSize;
    }

    return grid;
}
```

## Csharp

```csharp
public class Solution
{
    public int[][] SpecialGrid(int n)
    {
        return Build(n);
    }

    private int[][] Build(int n)
    {
        if (n == 0)
        {
            return new int[][] { new int[] { 0 } };
        }

        int half = 1 << (n - 1);
        int quadSize = half * half;
        int[][] sub = Build(n - 1);
        int size = half * 2;
        int[][] res = new int[size][];
        for (int i = 0; i < size; i++)
            res[i] = new int[size];

        for (int i = 0; i < half; i++)
        {
            for (int j = 0; j < half; j++)
            {
                int val = sub[i][j];
                // Top‑Left
                res[i][j] = val + 3 * quadSize;
                // Top‑Right
                res[i][j + half] = val + 0 * quadSize;
                // Bottom‑Left
                res[i + half][j] = val + 2 * quadSize;
                // Bottom‑Right
                res[i + half][j + half] = val + 1 * quadSize;
            }
        }

        return res;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number[][]}
 */
var specialGrid = function(n) {
    const build = (level) => {
        if (level === 0) return [[0]];
        const sub = build(level - 1);
        const m = sub.length;
        const k = Math.pow(4, level - 1); // cells per quadrant
        const size = m * 2;
        const res = Array.from({ length: size }, () => new Array(size));
        for (let i = 0; i < m; i++) {
            for (let j = 0; j < m; j++) {
                const v = sub[i][j];
                // top‑left
                res[i][j] = v + 3 * k;
                // top‑right
                res[i][j + m] = v;
                // bottom‑left
                res[i + m][j] = v + 2 * k;
                // bottom‑right
                res[i + m][j + m] = v + k;
            }
        }
        return res;
    };
    return build(n);
};
```

## Typescript

```typescript
function specialGrid(n: number): number[][] {
    if (n === 0) return [[0]];
    const prev = specialGrid(n - 1);
    const m = 1 << (n - 1); // size of previous grid
    const size = m * 2;
    const quarter = m * m;
    const res: number[][] = Array.from({ length: size }, () => Array(size).fill(0));
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < m; j++) {
            const v = prev[i][j];
            // top-left quadrant
            res[i][j] = v + 3 * quarter;
            // top-right quadrant
            res[i][j + m] = v;
            // bottom-left quadrant
            res[i + m][j] = v + 2 * quarter;
            // bottom-right quadrant
            res[i + m][j + m] = v + quarter;
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
     * @return Integer[][]
     */
    function specialGrid($n) {
        if ($n == 0) {
            return [[0]];
        }
        $prev = $this->specialGrid($n - 1);
        $m = count($prev);               // size of previous grid (2^{n-1})
        $block = $m * $m;                // number of elements in each quadrant
        $size = $m * 2;
        $grid = array_fill(0, $size, array_fill(0, $size, 0));

        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $m; $j++) {
                $val = $prev[$i][$j];
                // top‑left quadrant
                $grid[$i][$j] = $val + 3 * $block;
                // top‑right quadrant
                $grid[$i][$j + $m] = $val;               // offset 0
                // bottom‑left quadrant
                $grid[$i + $m][$j] = $val + 2 * $block;
                // bottom‑right quadrant
                $grid[$i + $m][$j + $m] = $val + $block;
            }
        }

        return $grid;
    }
}
```

## Swift

```swift
class Solution {
    func specialGrid(_ n: Int) -> [[Int]] {
        if n == 0 { return [[0]] }
        let smaller = specialGrid(n - 1)
        let m = smaller.count
        let quadSize = m * m
        var result = Array(repeating: Array(repeating: 0, count: 2 * m), count: 2 * m)
        for i in 0..<m {
            for j in 0..<m {
                let val = smaller[i][j]
                result[i][j] = val + 3 * quadSize               // top‑left
                result[i][j + m] = val + 0 * quadSize           // top‑right
                result[i + m][j] = val + 2 * quadSize           // bottom‑left
                result[i + m][j + m] = val + 1 * quadSize       // bottom‑right
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun specialGrid(n: Int): Array<IntArray> {
        if (n == 0) return arrayOf(intArrayOf(0))
        val half = 1 shl (n - 1)
        val subSize = half * half
        val smaller = specialGrid(n - 1)
        val size = half * 2
        val res = Array(size) { IntArray(size) }
        for (i in 0 until half) {
            for (j in 0 until half) {
                val v = smaller[i][j]
                res[i][j] = v + 3 * subSize          // top-left
                res[i][j + half] = v                 // top-right
                res[i + half][j] = v + 2 * subSize   // bottom-left
                res[i + half][j + half] = v + subSize// bottom-right
            }
        }
        return res
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> specialGrid(int n) {
    int size = 1 << n;
    return _build(size);
  }

  List<List<int>> _build(int sz) {
    if (sz == 1) return [[0]];
    int half = sz >> 1;
    var sub = _build(half);
    List<List<int>> res = List.generate(sz, (_) => List.filled(sz, 0));
    int offsetTL = 3 * half * half;
    int offsetTR = 0;
    int offsetBL = 2 * half * half;
    int offsetBR = 1 * half * half;

    for (int i = 0; i < half; ++i) {
      for (int j = 0; j < half; ++j) {
        int val = sub[i][j];
        res[i][j] = val + offsetTL;               // top-left
        res[i][j + half] = val + offsetTR;        // top-right
        res[i + half][j] = val + offsetBL;        // bottom-left
        res[i + half][j + half] = val + offsetBR; // bottom-right
      }
    }
    return res;
  }
}
```

## Golang

```go
func specialGrid(n int) [][]int {
	if n == 0 {
		return [][]int{{0}}
	}
	sub := specialGrid(n - 1)
	m := len(sub)
	size := m * m
	res := make([][]int, 2*m)
	for i := range res {
		res[i] = make([]int, 2*m)
	}
	for i := 0; i < m; i++ {
		for j := 0; j < m; j++ {
			val := sub[i][j]
			res[i][j] = val + 3*size       // top‑left
			res[i][j+m] = val + 0*size     // top‑right
			res[i+m][j] = val + 2*size     // bottom‑left
			res[i+m][j+m] = val + 1*size   // bottom‑right
		}
	}
	return res
}
```

## Ruby

```ruby
def special_grid(n)
  return [[0]] if n == 0
  sub = special_grid(n - 1)
  s = sub.size
  block = s * s
  res = Array.new(2 * s) { Array.new(2 * s) }
  (0...s).each do |i|
    (0...s).each do |j|
      val = sub[i][j]
      res[i][j] = val + 3 * block          # top‑left
      res[i][j + s] = val                  # top‑right
      res[i + s][j] = val + 2 * block      # bottom‑left
      res[i + s][j + s] = val + block      # bottom‑right
    end
  end
  res
end
```

## Scala

```scala
object Solution {
  def specialGrid(n: Int): Array[Array[Int]] = {
    if (n == 0) return Array(Array(0))
    val sub = specialGrid(n - 1)
    val m = sub.length
    val block = m * m
    val res = Array.ofDim[Int](2 * m, 2 * m)
    var i = 0
    while (i < m) {
      var j = 0
      while (j < m) {
        val v = sub(i)(j)
        res(i)(j) = v + 3 * block          // top-left
        res(i)(j + m) = v                  // top-right
        res(i + m)(j) = v + 2 * block      // bottom-left
        res(i + m)(j + m) = v + block      // bottom-right
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
    pub fn special_grid(n: i32) -> Vec<Vec<i32>> {
        fn build(k: i32) -> Vec<Vec<i32>> {
            if k == 0 {
                return vec![vec![0]];
            }
            let sub = build(k - 1);
            let s = sub.len();
            let m = (s * s) as i32; // number of cells in a quadrant
            let mut res = vec![vec![0i32; 2 * s]; 2 * s];
            for i in 0..s {
                for j in 0..s {
                    let v = sub[i][j];
                    // top‑left
                    res[i][j] = v + 3 * m;
                    // bottom‑left
                    res[i + s][j] = v + 2 * m;
                    // bottom‑right
                    res[i + s][j + s] = v + 1 * m;
                    // top‑right
                    res[i][j + s] = v;
                }
            }
            res
        }
        build(n)
    }
}
```

## Racket

```racket
(define/contract (special-grid n)
  (-> exact-integer? (listof (listof exact-integer?)))
  (let recur ((k n))
    (if (= k 0)
        '((0))
        (let* ((sub (recur (- k 1)))
               (m (length sub))
               (block (* m m))
               (tl (* 3 block))   ; top‑left offset
               (tr 0)             ; top‑right offset
               (bl (* 2 block))   ; bottom‑left offset
               (br block))        ; bottom‑right offset
          (define top-rows
            (map (lambda (row)
                   (append (map (lambda (v) (+ v tl)) row)
                           (map (lambda (v) (+ v tr)) row)))
                 sub))
          (define bottom-rows
            (map (lambda (row)
                   (append (map (lambda (v) (+ v bl)) row)
                           (map (lambda (v) (+ v br)) row)))
                 sub))
          (append top-rows bottom-rows))))))
```

## Erlang

```erlang
-module(solution).
-export([special_grid/1]).

-spec special_grid(N :: integer()) -> [[integer()]].
special_grid(0) ->
    [[0]];
special_grid(N) when N > 0 ->
    Sub = special_grid(N - 1),
    M = length(Sub),
    Count = M * M,
    TL = add_offset(Sub, 3 * Count),
    TR = add_offset(Sub, 0),
    BL = add_offset(Sub, 2 * Count),
    BR = add_offset(Sub, 1 * Count),

    TopRows = [lists:append([TLRow, TRRow]) || {TLRow, TRRow} <- lists:zip(TL, TR)],
    BottomRows = [lists:append([BLRow, BRRow]) || {BLRow, BRRow} <- lists:zip(BL, BR)],

    TopRows ++ BottomRows.

add_offset(Grid, Offset) ->
    [[X + Offset || X <- Row] || Row <- Grid].
```

## Elixir

```elixir
defmodule Solution do
  @spec special_grid(n :: integer) :: [[integer]]
  def special_grid(0), do: [[0]]

  def special_grid(n) when n > 0 do
    sub = special_grid(n - 1)
    m = :math.pow(2, n - 1) |> trunc()
    cells = m * m

    tl_off = 3 * cells
    tr_off = 0
    bl_off = 2 * cells
    br_off = 1 * cells

    top =
      Enum.map(sub, fn row ->
        left = Enum.map(row, &(&1 + tl_off))
        right = Enum.map(row, &(&1 + tr_off))
        left ++ right
      end)

    bottom =
      Enum.map(sub, fn row ->
        left = Enum.map(row, &(&1 + bl_off))
        right = Enum.map(row, &(&1 + br_off))
        left ++ right
      end)

    top ++ bottom
  end
end
```
