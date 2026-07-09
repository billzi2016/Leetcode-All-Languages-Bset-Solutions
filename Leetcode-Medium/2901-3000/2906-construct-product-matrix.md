# 2906. Construct Product Matrix

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> constructProductMatrix(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        int total = n * m;
        vector<long long> pref(total + 1, 1), suff(total + 1, 1);
        // flatten indices row-major
        for (int i = 0; i < total; ++i) {
            int r = i / m;
            int c = i % m;
            pref[i + 1] = pref[i] * grid[r][c];
        }
        for (int i = total - 1; i >= 0; --i) {
            int r = i / m;
            int c = i % m;
            suff[i] = suff[i + 1] * grid[r][c];
        }
        vector<vector<int>> ans(n, vector<int>(m));
        for (int i = 0; i < total; ++i) {
            long long prod = pref[i] * suff[i + 1];
            int r = i / m;
            int c = i % m;
            ans[r][c] = static_cast<int>(prod);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[][] constructProductMatrix(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        int total = n * m;
        long[] prefix = new long[total + 1];
        prefix[0] = 1L;
        for (int idx = 0; idx < total; idx++) {
            int val = grid[idx / m][idx % m];
            prefix[idx + 1] = prefix[idx] * val;
        }
        long[] suffix = new long[total + 1];
        suffix[total] = 1L;
        for (int idx = total - 1; idx >= 0; idx--) {
            int val = grid[idx / m][idx % m];
            suffix[idx] = suffix[idx + 1] * val;
        }
        int[][] result = new int[n][m];
        for (int idx = 0; idx < total; idx++) {
            long prod = prefix[idx] * suffix[idx + 1];
            result[idx / m][idx % m] = (int) prod;
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def constructProductMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        m = len(grid[0])
        total = n * m
        flat = []
        for row in grid:
            flat.extend(row)

        # prefix products
        pref = [1] * (total + 1)
        for i in range(total):
            pref[i + 1] = pref[i] * flat[i]

        # suffix products
        suff = [1] * (total + 1)
        for i in range(total - 1, -1, -1):
            suff[i] = suff[i + 1] * flat[i]

        res = [[0] * m for _ in range(n)]
        for idx in range(total):
            prod = pref[idx] * suff[idx + 1]
            i = idx // m
            j = idx % m
            res[i][j] = prod

        return res
```

## Python3

```python
class Solution:
    def constructProductMatrix(self, grid):
        n = len(grid)
        m = len(grid[0])
        total = n * m
        flat = [0] * total
        idx = 0
        for i in range(n):
            row = grid[i]
            for j in range(m):
                flat[idx] = row[j]
                idx += 1

        prefix = [1] * total
        suffix = [1] * total

        prod = 1
        for i in range(total):
            prod *= flat[i]
            prefix[i] = prod

        prod = 1
        for i in range(total - 1, -1, -1):
            prod *= flat[i]
            suffix[i] = prod

        res = [[0] * m for _ in range(n)]
        idx = 0
        for i in range(n):
            for j in range(m):
                left = prefix[idx - 1] if idx > 0 else 1
                right = suffix[idx + 1] if idx < total - 1 else 1
                res[i][j] = left * right
                idx += 1

        return res
```

## C

```c
/****
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced,
 *       assume caller calls free().
 */
int** constructProductMatrix(int** grid, int gridSize, int* gridColSize,
                             int* returnSize, int*** returnColumnSizes) {
    int rows = gridSize;
    int cols = gridColSize[0];
    long long total = (long long)rows * cols;

    // Allocate prefix and suffix product arrays
    unsigned long long *pref = (unsigned long long *)malloc((total + 1) * sizeof(unsigned long long));
    unsigned long long *suff = (unsigned long long *)malloc((total + 1) * sizeof(unsigned long long));

    pref[0] = 1ULL;
    for (long long i = 0; i < total; ++i) {
        int r = i / cols;
        int c = i % cols;
        unsigned long long val = (unsigned long long)grid[r][c];
        pref[i + 1] = pref[i] * val;
    }

    suff[total] = 1ULL;
    for (long long i = total - 1; i >= 0; --i) {
        int r = i / cols;
        int c = i % cols;
        unsigned long long val = (unsigned long long)grid[r][c];
        suff[i] = suff[i + 1] * val;
    }

    // Prepare return structures
    *returnSize = rows;
    *returnColumnSizes = (int **)malloc(rows * sizeof(int *));
    int **ans = (int **)malloc(rows * sizeof(int *));
    for (int i = 0; i < rows; ++i) {
        (*returnColumnSizes)[i] = cols;
        ans[i] = (int *)malloc(cols * sizeof(int));
    }

    // Fill answer matrix: product of all elements except the current one
    for (long long idx = 0; idx < total; ++idx) {
        unsigned long long prod = pref[idx] * suff[idx + 1];
        int r = idx / cols;
        int c = idx % cols;
        ans[r][c] = (int)prod;   // assumes result fits into 32‑bit signed integer
    }

    free(pref);
    free(suff);
    return ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int[][] ConstructProductMatrix(int[][] grid) {
        int n = grid.Length;
        int m = grid[0].Length;
        long total = 1L;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                total *= grid[i][j];
            }
        }

        int[][] result = new int[n][];
        for (int i = 0; i < n; i++) {
            result[i] = new int[m];
            for (int j = 0; j < m; j++) {
                result[i][j] = (int)(total / grid[i][j]);
            }
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number[][]}
 */
var constructProductMatrix = function(grid) {
    const n = grid.length;
    const m = grid[0].length;
    let total = 1n;
    for (let i = 0; i < n; ++i) {
        for (let j = 0; j < m; ++j) {
            total *= BigInt(grid[i][j]);
        }
    }
    const ans = new Array(n);
    for (let i = 0; i < n; ++i) {
        ans[i] = new Array(m);
        for (let j = 0; j < m; ++j) {
            const val = total / BigInt(grid[i][j]);
            ans[i][j] = Number(val);
        }
    }
    return ans;
};
```

## Typescript

```typescript
function constructProductMatrix(grid: number[][]): number[][] {
    const n = grid.length;
    const m = grid[0].length;
    let zeroCount = 0;
    let totalProd = 1n;

    for (let i = 0; i < n; ++i) {
        for (let j = 0; j < m; ++j) {
            const val = grid[i][j];
            if (val === 0) {
                zeroCount++;
            } else {
                totalProd *= BigInt(val);
            }
        }
    }

    const result: number[][] = Array.from({ length: n }, () => new Array(m).fill(0));

    for (let i = 0; i < n; ++i) {
        for (let j = 0; j < m; ++j) {
            const val = grid[i][j];
            let cellProd: bigint;
            if (zeroCount === 0) {
                // no zeros, safe to divide
                cellProd = totalProd / BigInt(val);
            } else if (zeroCount > 1) {
                // at least two zeros -> every product contains a zero
                cellProd = 0n;
            } else { // exactly one zero in the whole matrix
                if (val === 0) {
                    // current position is the only zero, product of all non‑zero elements
                    cellProd = totalProd;
                } else {
                    // other positions include the zero -> result is zero
                    cellProd = 0n;
                }
            }
            result[i][j] = Number(cellProd);
        }
    }

    return result;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer[][]
     */
    function constructProductMatrix($grid) {
        $MOD = 1000000007;
        $n = count($grid);
        $m = count($grid[0]);
        $len = $n * $m;

        // Flatten the grid
        $flat = [];
        foreach ($grid as $row) {
            foreach ($row as $val) {
                $flat[] = $val % $MOD;
            }
        }

        // Prefix products
        $pref = array_fill(0, $len + 1, 1);
        for ($i = 0; $i < $len; ++$i) {
            $pref[$i + 1] = (int)(($pref[$i] * $flat[$i]) % $MOD);
        }

        // Suffix products
        $suf = array_fill(0, $len + 1, 1);
        for ($i = $len - 1; $i >= 0; --$i) {
            $suf[$i] = (int)(($suf[$i + 1] * $flat[$i]) % $MOD);
        }

        // Build result matrix
        $result = array_fill(0, $n, []);
        $idx = 0;
        for ($i = 0; $i < $n; ++$i) {
            $rowRes = [];
            for ($j = 0; $j < $m; ++$j) {
                $prod = (int)(($pref[$idx] * $suf[$idx + 1]) % $MOD);
                $rowRes[] = $prod;
                ++$idx;
            }
            $result[$i] = $rowRes;
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func constructProductMatrix(_ grid: [[Int]]) -> [[Int]] {
        let MOD = 1_000_000_007
        let n = grid.count
        let m = grid[0].count
        var flat = [Int]()
        flat.reserveCapacity(n * m)
        for row in grid {
            flat.append(contentsOf: row)
        }
        let total = flat.count
        var prefix = [Int](repeating: 1, count: total + 1)
        for i in 0..<total {
            let val = flat[i] % MOD
            prefix[i + 1] = Int((Int64(prefix[i]) * Int64(val)) % Int64(MOD))
        }
        var suffix = [Int](repeating: 1, count: total + 1)
        if total > 0 {
            for i in stride(from: total - 1, through: 0, by: -1) {
                let val = flat[i] % MOD
                suffix[i] = Int((Int64(suffix[i + 1]) * Int64(val)) % Int64(MOD))
            }
        }
        var result = Array(repeating: Array(repeating: 0, count: m), count: n)
        for idx in 0..<total {
            let prod = Int((Int64(prefix[idx]) * Int64(suffix[idx + 1])) % Int64(MOD))
            let r = idx / m
            let c = idx % m
            result[r][c] = prod
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun constructProductMatrix(grid: Array<IntArray>): Array<IntArray> {
        val n = grid.size
        val m = grid[0].size
        val total = n * m
        val mod = 1_000_000_007L

        // Flatten the grid into a 1‑D array of longs modulo MOD
        val vals = LongArray(total)
        var idx = 0
        for (i in 0 until n) {
            for (j in 0 until m) {
                vals[idx++] = (grid[i][j].toLong() % mod)
            }
        }

        // Prefix products
        val pref = LongArray(total + 1)
        pref[0] = 1L
        for (i in 0 until total) {
            pref[i + 1] = (pref[i] * vals[i]) % mod
        }

        // Suffix products
        val suff = LongArray(total + 1)
        suff[total] = 1L
        for (i in total - 1 downTo 0) {
            suff[i] = (vals[i] * suff[i + 1]) % mod
        }

        // Build answer matrix: product of all elements except the current one
        val ans = Array(n) { IntArray(m) }
        idx = 0
        for (i in 0 until n) {
            for (j in 0 until m) {
                val prod = (pref[idx] * suff[idx + 1]) % mod
                ans[i][j] = prod.toInt()
                idx++
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> constructProductMatrix(List<List<int>> grid) {
    int n = grid.length;
    int m = grid[0].length;

    // Compute the total product of all elements.
    int total = 1;
    for (var row in grid) {
      for (int val in row) {
        total *= val;
      }
    }

    // Build the result matrix where each cell is total / current element.
    List<List<int>> res = List.generate(n, (_) => List.filled(m, 0));
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        res[i][j] = total ~/ grid[i][j];
      }
    }

    return res;
  }
}
```

## Golang

```go
func constructProductMatrix(grid [][]int) [][]int {
    n := len(grid)
    if n == 0 {
        return nil
    }
    m := len(grid[0])

    // Compute total product using big integers to avoid overflow.
    total := new(big.Int).SetInt64(1)
    for i := 0; i < n; i++ {
        for j := 0; j < m; j++ {
            total.Mul(total, big.NewInt(int64(grid[i][j])))
        }
    }

    // Build result matrix.
    res := make([][]int, n)
    for i := 0; i < n; i++ {
        row := make([]int, m)
        for j := 0; j < m; j++ {
            div := new(big.Int).Div(total, big.NewInt(int64(grid[i][j])))
            // Assuming the final value fits into int.
            row[j] = int(div.Int64())
        }
        res[i] = row
    }
    return res
}
```

## Ruby

```ruby
def construct_product_matrix(grid)
  n = grid.length
  m = grid[0].length
  total = n * m

  flat = Array.new(total)
  idx = 0
  grid.each do |row|
    row.each do |val|
      flat[idx] = val
      idx += 1
    end
  end

  pref = Array.new(total + 1, 1)
  (0...total).each do |i|
    pref[i + 1] = pref[i] * flat[i]
  end

  suff = Array.new(total + 1, 1)
  (total - 1).downto(0) do |i|
    suff[i] = suff[i + 1] * flat[i]
  end

  res = Array.new(n) { Array.new(m) }
  idx = 0
  n.times do |i|
    m.times do |j|
      res[i][j] = pref[idx] * suff[idx + 1]
      idx += 1
    end
  end

  res
end
```

## Scala

```scala
object Solution {
    def constructProductMatrix(grid: Array[Array[Int]]): Array[Array[Int]] = {
        val n = grid.length
        if (n == 0) return Array.empty
        val m = grid(0).length
        var total = BigInt(1)
        for (i <- 0 until n; j <- 0 until m) {
            total *= BigInt(grid(i)(j))
        }
        val result = Array.ofDim[Int](n, m)
        for (i <- 0 until n; j <- 0 until m) {
            result(i)(j) = (total / BigInt(grid(i)(j))).toInt
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn construct_product_matrix(grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        const MOD: i64 = 1_000_000_007;
        let n = grid.len();
        let m = grid[0].len();

        // compute total product modulo MOD
        let mut total: i64 = 1;
        for row in &grid {
            for &val in row {
                total = (total * (val as i64 % MOD)) % MOD;
            }
        }

        // fast exponentiation for modular inverse (MOD is prime)
        fn mod_pow(mut base: i64, mut exp: i64, modu: i64) -> i64 {
            let mut res: i64 = 1;
            base %= modu;
            while exp > 0 {
                if exp & 1 == 1 {
                    res = (res * base) % modu;
                }
                base = (base * base) % modu;
                exp >>= 1;
            }
            res
        }

        let mut ans: Vec<Vec<i32>> = vec![vec![0; m]; n];
        for i in 0..n {
            for j in 0..m {
                let inv = mod_pow(grid[i][j] as i64 % MOD, MOD - 2, MOD);
                let val = (total * inv) % MOD;
                ans[i][j] = val as i32;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (construct-product-matrix grid)
  (-> (listof (listof exact-integer?))
      (listof (listof exact-integer?)))
  (let-values ([(zero-count total-prod)
                (for/fold ([zc 0] [tp 1]) ([row grid])
                  (for/fold ([zc2 zc] [tp2 tp]) ([val row])
                    (if (= val 0)
                        (values (+ zc2 1) tp2)
                        (values zc2 (* tp2 val)))) )])
    (map (lambda (row)
           (map (lambda (val)
                  (cond
                    [(> zero-count 1) 0]
                    [(= zero-count 1)
                     (if (= val 0) total-prod 0)]
                    [else (/ total-prod val)]))
                row))
         grid)))
```

## Erlang

```erlang
-spec construct_product_matrix(Grid :: [[integer()]]) -> [[integer()]].
construct_product_matrix(Grid) ->
    case Grid of
        [] -> [];
        _ ->
            M = length(hd(Grid)),
            Flat = [Elem || Row <- Grid, Elem <- Row],
            % Prefix products: product of elements before each position
            {_, PrefixRev} = lists:foldl(
                fun(Elem, {AccProd, AccList}) ->
                    NewProd = AccProd * Elem,
                    {NewProd, [AccProd | AccList]}
                end,
                {1, []},
                Flat),
            Prefix = lists:reverse(PrefixRev),
            % Compute results using suffix traversal
            ResFlat = compute_rev(lists:reverse(Flat), lists:reverse(Prefix), 1, []),
            chunk(ResFlat, M)
    end.

% Helper to compute results while traversing from the end.
compute_rev([], [], _Suffix, Acc) ->
    Acc;
compute_rev([E|Es], [P|Ps], Suffix, Acc) ->
    Res = P * Suffix,
    NewSuffix = Suffix * E,
    compute_rev(Es, Ps, NewSuffix, [Res | Acc]).

% Split flat list into rows of length M.
chunk([], _M) -> [];
chunk(List, M) ->
    {Row, Rest} = lists:split(M, List),
    [Row | chunk(Rest, M)].
```

## Elixir

```elixir
defmodule Solution do
  @spec construct_product_matrix(grid :: [[integer]]) :: [[integer]]
  def construct_product_matrix(grid) do
    total = grid |> List.flatten() |> Enum.reduce(1, &*/2)
    Enum.map(grid, fn row ->
      Enum.map(row, fn v -> div(total, v) end)
    end)
  end
end
```
