# 2397. Maximum Rows Covered by Columns

## Cpp

```cpp
class Solution {
public:
    int maximumRows(vector<vector<int>>& matrix, int numSelect) {
        int m = matrix.size();
        int n = matrix[0].size();
        vector<int> rowMask(m, 0);
        for (int i = 0; i < m; ++i) {
            int mask = 0;
            for (int j = 0; j < n; ++j) {
                if (matrix[i][j] == 1) mask |= (1 << j);
            }
            rowMask[i] = mask;
        }
        int best = 0;
        int totalMasks = 1 << n;
        for (int sel = 0; sel < totalMasks; ++sel) {
            if (__builtin_popcount(sel) != numSelect) continue;
            int cnt = 0;
            for (int rm : rowMask) {
                if ((rm & ~sel) == 0) ++cnt;
            }
            best = max(best, cnt);
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public int maximumRows(int[][] matrix, int numSelect) {
        int m = matrix.length;
        int n = matrix[0].length;
        int[] rowMask = new int[m];
        for (int i = 0; i < m; i++) {
            int mask = 0;
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 1) {
                    mask |= (1 << j);
                }
            }
            rowMask[i] = mask;
        }

        int maxCovered = 0;
        int totalMasks = 1 << n;
        for (int mask = 0; mask < totalMasks; mask++) {
            if (Integer.bitCount(mask) != numSelect) continue;
            int covered = 0;
            int notSelectedMask = ~mask;
            for (int rm : rowMask) {
                // If all 1-bits of the row are within selected columns
                if ((rm & notSelectedMask) == 0) {
                    covered++;
                }
            }
            if (covered > maxCovered) {
                maxCovered = covered;
            }
        }
        return maxCovered;
    }
}
```

## Python

```python
class Solution(object):
    def maximumRows(self, matrix, numSelect):
        """
        :type matrix: List[List[int]]
        :type numSelect: int
        :rtype: int
        """
        from itertools import combinations

        m = len(matrix)
        n = len(matrix[0])
        # Convert each row to a bitmask of columns containing 1
        row_masks = []
        for i in range(m):
            mask = 0
            for j, val in enumerate(matrix[i]):
                if val:
                    mask |= 1 << j
            row_masks.append(mask)

        max_covered = 0
        # Enumerate all subsets of columns with exactly numSelect bits set
        cols_range = range(n)
        for combo in combinations(cols_range, numSelect):
            sel_mask = 0
            for c in combo:
                sel_mask |= 1 << c
            covered = 0
            for rm in row_masks:
                if rm & ~sel_mask == 0:   # all required columns are selected
                    covered += 1
            if covered > max_covered:
                max_covered = covered

        return max_covered
```

## Python3

```python
from typing import List
import itertools

class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        m, n = len(matrix), len(matrix[0])
        row_masks = []
        for row in matrix:
            mask = 0
            for j, val in enumerate(row):
                if val:
                    mask |= 1 << j
            row_masks.append(mask)

        max_covered = 0
        cols_range = range(n)
        for combo in itertools.combinations(cols_range, numSelect):
            sel_mask = 0
            for c in combo:
                sel_mask |= 1 << c
            covered = 0
            not_sel = ~sel_mask
            for rm in row_masks:
                if rm & not_sel == 0:
                    covered += 1
            if covered > max_covered:
                max_covered = covered

        return max_covered
```

## C

```c
int maximumRows(int** matrix, int matrixSize, int* matrixColSize, int numSelect) {
    int m = matrixSize;
    if (m == 0) return 0;
    int n = matrixColSize[0];
    
    unsigned short rowMask[12]; // max rows = 12
    for (int i = 0; i < m; ++i) {
        unsigned short mask = 0;
        for (int j = 0; j < n; ++j) {
            if (matrix[i][j] == 1)
                mask |= (1 << j);
        }
        rowMask[i] = mask;
    }
    
    int maxRows = 0;
    int totalMasks = 1 << n;
    for (int sel = 0; sel < totalMasks; ++sel) {
        if (__builtin_popcount((unsigned)sel) != numSelect)
            continue;
        int covered = 0;
        unsigned notSel = ~sel;
        for (int i = 0; i < m; ++i) {
            if ((rowMask[i] & notSel) == 0)
                ++covered;
        }
        if (covered > maxRows)
            maxRows = covered;
    }
    
    return maxRows;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaximumRows(int[][] matrix, int numSelect)
    {
        int m = matrix.Length;
        int n = matrix[0].Length;
        int[] rowMasks = new int[m];
        for (int i = 0; i < m; i++)
        {
            int mask = 0;
            for (int j = 0; j < n; j++)
                if (matrix[i][j] == 1)
                    mask |= 1 << j;
            rowMasks[i] = mask;
        }

        int maxCovered = 0;
        int limit = 1 << n;
        for (int selMask = 0; selMask < limit; selMask++)
        {
            if (BitCount(selMask) != numSelect) continue;

            int covered = 0;
            foreach (int rowMask in rowMasks)
                if ((rowMask & ~selMask) == 0)
                    covered++;

            if (covered > maxCovered) maxCovered = covered;
        }

        return maxCovered;
    }

    private int BitCount(int x)
    {
        int cnt = 0;
        while (x != 0)
        {
            x &= x - 1;
            cnt++;
        }
        return cnt;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} matrix
 * @param {number} numSelect
 * @return {number}
 */
var maximumRows = function(matrix, numSelect) {
    const m = matrix.length;
    const n = matrix[0].length;
    const rowMasks = new Array(m);
    for (let i = 0; i < m; ++i) {
        let mask = 0;
        for (let j = 0; j < n; ++j) {
            if (matrix[i][j] === 1) mask |= (1 << j);
        }
        rowMasks[i] = mask;
    }

    const totalMask = 1 << n;
    let maxCovered = 0;

    const popcnt = x => {
        let cnt = 0;
        while (x) {
            x &= x - 1;
            ++cnt;
        }
        return cnt;
    };

    for (let mask = 0; mask < totalMask; ++mask) {
        if (popcnt(mask) !== numSelect) continue;
        let covered = 0;
        const notMask = ~mask;
        for (let i = 0; i < m; ++i) {
            if ((rowMasks[i] & notMask) === 0) ++covered;
        }
        if (covered > maxCovered) {
            maxCovered = covered;
            if (maxCovered === m) break; // cannot do better
        }
    }

    return maxCovered;
};
```

## Typescript

```typescript
function maximumRows(matrix: number[][], numSelect: number): number {
    const m = matrix.length;
    const n = matrix[0].length;
    const rowMasks: number[] = new Array(m);
    for (let i = 0; i < m; i++) {
        let mask = 0;
        for (let j = 0; j < n; j++) {
            if (matrix[i][j] === 1) mask |= 1 << j;
        }
        rowMasks[i] = mask;
    }

    const limit = 1 << n;
    let best = 0;

    for (let s = 0; s < limit; s++) {
        if (popcnt(s) !== numSelect) continue;
        let cnt = 0;
        for (let i = 0; i < m; i++) {
            if ((rowMasks[i] & ~s) === 0) cnt++;
        }
        if (cnt > best) best = cnt;
    }

    return best;

    function popcnt(x: number): number {
        let c = 0;
        while (x) {
            x &= x - 1;
            c++;
        }
        return c;
    }
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $matrix
     * @param Integer $numSelect
     * @return Integer
     */
    function maximumRows($matrix, $numSelect) {
        $m = count($matrix);
        if ($m == 0) return 0;
        $n = count($matrix[0]);

        // Precompute bitmask for each row
        $rowMasks = [];
        for ($i = 0; $i < $m; $i++) {
            $mask = 0;
            for ($j = 0; $j < $n; $j++) {
                if ($matrix[$i][$j] == 1) {
                    $mask |= (1 << $j);
                }
            }
            $rowMasks[] = $mask;
        }

        $maxCovered = 0;
        $limit = 1 << $n;

        for ($mask = 0; $mask < $limit; $mask++) {
            if ($this->popcount($mask) !== $numSelect) continue;

            $covered = 0;
            foreach ($rowMasks as $rm) {
                // row is covered if all its 1-bits are within selected columns
                if (($rm & (~$mask)) == 0) {
                    $covered++;
                }
            }
            if ($covered > $maxCovered) {
                $maxCovered = $covered;
            }
        }

        return $maxCovered;
    }

    private function popcount(int $x): int {
        $cnt = 0;
        while ($x) {
            $cnt += $x & 1;
            $x >>= 1;
        }
        return $cnt;
    }
}
```

## Swift

```swift
class Solution {
    func maximumRows(_ matrix: [[Int]], _ numSelect: Int) -> Int {
        let m = matrix.count
        guard m > 0 else { return 0 }
        let n = matrix[0].count
        var rowMasks = [Int]()
        for i in 0..<m {
            var mask = 0
            for j in 0..<n where matrix[i][j] == 1 {
                mask |= (1 << j)
            }
            rowMasks.append(mask)
        }
        let limit = 1 << n
        var best = 0
        for subset in 0..<limit {
            if subset.nonzeroBitCount != numSelect { continue }
            var covered = 0
            for rm in rowMasks where (rm & ~subset) == 0 {
                covered += 1
            }
            if covered > best { best = covered }
        }
        return best
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumRows(matrix: Array<IntArray>, numSelect: Int): Int {
        val m = matrix.size
        if (m == 0) return 0
        val n = matrix[0].size
        val rowMasks = IntArray(m)
        for (i in 0 until m) {
            var mask = 0
            for (j in 0 until n) {
                if (matrix[i][j] == 1) {
                    mask = mask or (1 shl j)
                }
            }
            rowMasks[i] = mask
        }
        var best = 0
        val limit = 1 shl n
        for (mask in 0 until limit) {
            if (Integer.bitCount(mask) != numSelect) continue
            var covered = 0
            for (rowMask in rowMasks) {
                if ((rowMask and mask) == rowMask) {
                    covered++
                }
            }
            if (covered > best) best = covered
        }
        return best
    }
}
```

## Dart

```dart
class Solution {
  int maximumRows(List<List<int>> matrix, int numSelect) {
    int m = matrix.length;
    int n = matrix[0].length;
    List<int> rowMasks = List.filled(m, 0);
    for (int i = 0; i < m; i++) {
      int mask = 0;
      for (int j = 0; j < n; j++) {
        if (matrix[i][j] == 1) {
          mask |= (1 << j);
        }
      }
      rowMasks[i] = mask;
    }

    int maxRows = 0;
    int totalMask = 1 << n;

    for (int mask = 0; mask < totalMask; mask++) {
      if (_popCount(mask) != numSelect) continue;
      int covered = 0;
      int notSelected = ~mask;
      for (int rowMask in rowMasks) {
        if ((rowMask & notSelected) == 0) {
          covered++;
        }
      }
      if (covered > maxRows) maxRows = covered;
    }

    return maxRows;
  }

  int _popCount(int x) {
    int count = 0;
    while (x != 0) {
      count += x & 1;
      x >>= 1;
    }
    return count;
  }
}
```

## Golang

```go
import "math/bits"

func maximumRows(matrix [][]int, numSelect int) int {
	m := len(matrix)
	if m == 0 {
		return 0
	}
	n := len(matrix[0])

	rowMasks := make([]int, m)
	for i := 0; i < m; i++ {
		mask := 0
		for j := 0; j < n; j++ {
			if matrix[i][j] == 1 {
				mask |= 1 << j
			}
		}
		rowMasks[i] = mask
	}

	maxCovered := 0
	limit := 1 << n
	for subset := 0; subset < limit; subset++ {
		if bits.OnesCount(uint(subset)) != numSelect {
			continue
		}
		covered := 0
		invSubset := ^subset
		for _, rm := range rowMasks {
			if rm&invSubset == 0 {
				covered++
			}
		}
		if covered > maxCovered {
			maxCovered = covered
		}
	}
	return maxCovered
}
```

## Ruby

```ruby
def maximum_rows(matrix, num_select)
  n = matrix[0].size
  row_masks = matrix.map do |row|
    mask = 0
    row.each_with_index { |v, i| mask |= (1 << i) if v == 1 }
    mask
  end

  max_covered = 0
  (0...n).to_a.combination(num_select) do |cols|
    selected_mask = 0
    cols.each { |c| selected_mask |= (1 << c) }

    covered = 0
    row_masks.each do |rm|
      covered += 1 if (rm & ~selected_mask).zero?
    end

    max_covered = covered if covered > max_covered
  end

  max_covered
end
```

## Scala

```scala
object Solution {
    def maximumRows(matrix: Array[Array[Int]], numSelect: Int): Int = {
        val m = matrix.length
        if (m == 0) return 0
        val n = matrix(0).length
        val rowMasks = new Array[Int](m)
        for (i <- 0 until m) {
            var mask = 0
            for (j <- 0 until n) {
                if (matrix(i)(j) == 1) mask |= (1 << j)
            }
            rowMasks(i) = mask
        }

        var best = 0
        val limit = 1 << n
        for (mask <- 0 until limit) {
            if (Integer.bitCount(mask) == numSelect) {
                var cnt = 0
                var r = 0
                while (r < m) {
                    if ((rowMasks(r) & ~mask) == 0) cnt += 1
                    r += 1
                }
                if (cnt > best) best = cnt
            }
        }
        best
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_rows(matrix: Vec<Vec<i32>>, num_select: i32) -> i32 {
        let m = matrix.len();
        if m == 0 {
            return 0;
        }
        let n = matrix[0].len();

        // Encode each row as a bitmask of columns containing 1
        let mut rows: Vec<u16> = Vec::with_capacity(m);
        for r in &matrix {
            let mut mask: u16 = 0;
            for (j, &v) in r.iter().enumerate() {
                if v == 1 {
                    mask |= 1 << j;
                }
            }
            rows.push(mask);
        }

        let k = num_select as usize;
        let limit = 1usize << n;
        let mut best = 0i32;

        for subset in 0..limit {
            if subset.count_ones() as usize != k {
                continue;
            }
            let sub_mask = subset as u16;
            let mut cnt = 0i32;
            for &row_mask in &rows {
                // Row is covered if all its 1-bits are inside the selected columns
                if row_mask & (!sub_mask) == 0 {
                    cnt += 1;
                }
            }
            if cnt > best {
                best = cnt;
            }
        }

        best
    }
}
```

## Racket

```racket
(define/contract (maximum-rows matrix numSelect)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ((m (length matrix))
         (n (if (= m 0) 0 (length (first matrix))))
         (row-masks
          (map (lambda (row)
                 (let loop ((i 0) (mask 0) (lst row))
                   (if (null? lst)
                       mask
                       (loop (+ i 1)
                             (if (= (car lst) 1)
                                 (bitwise-ior mask (arithmetic-shift 1 i))
                                 mask)
                             (cdr lst)))))
               matrix))
         (allMask (sub1 (arithmetic-shift 1 n))))
    (let loop ((mask 0) (maxRows 0))
      (if (> mask allMask)
          maxRows
          (if (= (bitwise-bit-count mask) numSelect)
              (let ((covered
                     (for/sum ([rm row-masks])
                       (if (= (bitwise-and rm (bitwise-and (bitwise-not mask) allMask)) 0)
                           1
                           0))))
                (loop (+ mask 1) (max maxRows covered)))
              (loop (+ mask 1) maxRows))))))
```

## Erlang

```erlang
-module(solution).
-export([maximum_rows/2]).

-spec maximum_rows(Matrix :: [[integer()]], NumSelect :: integer()) -> integer().
maximum_rows(Matrix, NumSelect) ->
    N = length(hd(Matrix)),
    RowMasks = [row_mask(Row, 0) || Row <- Matrix],
    MaxMask = (1 bsl N) - 1,
    max_covered(0, 0, MaxMask, NumSelect, RowMasks).

row_mask([], _Idx) -> 0;
row_mask([Bit|Rest], Idx) ->
    RestMask = row_mask(Rest, Idx + 1),
    case Bit of
        1 -> (1 bsl Idx) bor RestMask;
        _ -> RestMask
    end.

popcount(0) -> 0;
popcount(X) -> 1 + popcount(X band (X - 1)).

count_covered(RowMasks, SelMask) ->
    lists:foldl(fun(RM, Acc) ->
        if (RM band SelMask) =:= RM -> Acc + 1; true -> Acc end
    end, 0, RowMasks).

max_covered(CurrentMax, Mask, MaxMask, NumSelect, RowMasks) when Mask > MaxMask ->
    CurrentMax;
max_covered(CurrentMax, Mask, MaxMask, NumSelect, RowMasks) ->
    case popcount(Mask) of
        NumSelect ->
            Covered = count_covered(RowMasks, Mask),
            NewMax = if Covered > CurrentMax -> Covered; true -> CurrentMax end,
            max_covered(NewMax, Mask + 1, MaxMask, NumSelect, RowMasks);
        _ ->
            max_covered(CurrentMax, Mask + 1, MaxMask, NumSelect, RowMasks)
    end.
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec maximum_rows(matrix :: [[integer]], num_select :: integer) :: integer
  def maximum_rows(matrix, num_select) do
    n = length(List.first(matrix))

    row_masks =
      Enum.map(matrix, fn row ->
        Enum.with_index(row)
        |> Enum.reduce(0, fn {val, idx}, acc ->
          if val == 1, do: acc ||| (1 <<< idx), else: acc
        end)
      end)

    0..((1 <<< n) - 1)
    |> Enum.filter(fn mask -> :erlang.popcount(mask) == num_select end)
    |> Enum.reduce(0, fn mask, best ->
      covered =
        Enum.count(row_masks, fn rm ->
          (rm &&& bnot(mask)) == 0
        end)

      if covered > best, do: covered, else: best
    end)
  end
end
```
