# 1074. Number of Submatrices That Sum to Target

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        int n = matrix[0].size();
        long long ans = 0;
        for (int top = 0; top < m; ++top) {
            vector<int> colSums(n, 0);
            for (int bottom = top; bottom < m; ++bottom) {
                for (int c = 0; c < n; ++c)
                    colSums[c] += matrix[bottom][c];
                
                unordered_map<long long, int> cnt;
                cnt.reserve(n * 2);
                cnt[0] = 1;
                long long cur = 0;
                for (int c = 0; c < n; ++c) {
                    cur += colSums[c];
                    ans += cnt[cur - target];
                    ++cnt[cur];
                }
            }
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    public int numSubmatrixSumTarget(int[][] matrix, int target) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        int result = 0;

        for (int top = 0; top < rows; ++top) {
            int[] colSums = new int[cols];
            for (int bottom = top; bottom < rows; ++bottom) {
                for (int c = 0; c < cols; ++c) {
                    colSums[c] += matrix[bottom][c];
                }

                java.util.Map<Integer, Integer> prefixCount = new java.util.HashMap<>();
                prefixCount.put(0, 1);
                int curSum = 0;
                for (int sum : colSums) {
                    curSum += sum;
                    result += prefixCount.getOrDefault(curSum - target, 0);
                    prefixCount.put(curSum, prefixCount.getOrDefault(curSum, 0) + 1);
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
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        rows = len(matrix)
        cols = len(matrix[0])
        ans = 0
        for top in range(rows):
            col_sums = [0] * cols
            for bottom in range(top, rows):
                for c in range(cols):
                    col_sums[c] += matrix[bottom][c]
                counter = {0: 1}
                cur = 0
                for s in col_sums:
                    cur += s
                    ans += counter.get(cur - target, 0)
                    counter[cur] = counter.get(cur, 0) + 1
        return ans
```

## Python3

```python
class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        from collections import defaultdict
        m, n = len(matrix), len(matrix[0])
        ans = 0
        for top in range(m):
            col_sums = [0] * n
            for bottom in range(top, m):
                row = matrix[bottom]
                for c in range(n):
                    col_sums[c] += row[c]
                cur_sum = 0
                counter = defaultdict(int)
                counter[0] = 1
                for val in col_sums:
                    cur_sum += val
                    ans += counter.get(cur_sum - target, 0)
                    counter[cur_sum] += 1
        return ans
```

## C

```c
int numSubmatrixSumTarget(int** matrix, int matrixSize, int* matrixColSize, int target) {
    int m = matrixSize;
    int n = matrixColSize[0];
    long long ans = 0;
    
    for (int top = 0; top < m; ++top) {
        int colSums[101] = {0};
        for (int bottom = top; bottom < m; ++bottom) {
            for (int c = 0; c < n; ++c) {
                colSums[c] += matrix[bottom][c];
            }
            for (int left = 0; left < n; ++left) {
                int sum = 0;
                for (int right = left; right < n; ++right) {
                    sum += colSums[right];
                    if (sum == target) {
                        ++ans;
                    }
                }
            }
        }
    }
    
    return (int)ans;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int NumSubmatrixSumTarget(int[][] matrix, int target) {
        int rows = matrix.Length;
        int cols = matrix[0].Length;
        int result = 0;

        for (int top = 0; top < rows; ++top) {
            int[] colSums = new int[cols];
            for (int bottom = top; bottom < rows; ++bottom) {
                for (int c = 0; c < cols; ++c) {
                    colSums[c] += matrix[bottom][c];
                }

                var prefixCount = new Dictionary<int, int>();
                prefixCount[0] = 1;
                int curSum = 0;

                for (int c = 0; c < cols; ++c) {
                    curSum += colSums[c];
                    if (prefixCount.TryGetValue(curSum - target, out int cnt)) {
                        result += cnt;
                    }
                    if (prefixCount.ContainsKey(curSum))
                        prefixCount[curSum]++;
                    else
                        prefixCount[curSum] = 1;
                }
            }
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {number}
 */
var numSubmatrixSumTarget = function(matrix, target) {
    const rows = matrix.length;
    const cols = matrix[0].length;
    let count = 0;

    for (let top = 0; top < rows; ++top) {
        const colSums = new Array(cols).fill(0);
        for (let bottom = top; bottom < rows; ++bottom) {
            for (let c = 0; c < cols; ++c) {
                colSums[c] += matrix[bottom][c];
            }
            const prefixMap = new Map();
            prefixMap.set(0, 1);
            let curSum = 0;
            for (const sum of colSums) {
                curSum += sum;
                if (prefixMap.has(curSum - target)) {
                    count += prefixMap.get(curSum - target);
                }
                prefixMap.set(curSum, (prefixMap.get(curSum) || 0) + 1);
            }
        }
    }

    return count;
};
```

## Typescript

```typescript
function numSubmatrixSumTarget(matrix: number[][], target: number): number {
    const m = matrix.length;
    const n = matrix[0].length;
    let result = 0;

    if (m <= n) {
        // Iterate over pairs of rows
        for (let top = 0; top < m; ++top) {
            const colSums = new Array(n).fill(0);
            for (let bottom = top; bottom < m; ++bottom) {
                for (let c = 0; c < n; ++c) {
                    colSums[c] += matrix[bottom][c];
                }
                // Count subarrays in colSums that sum to target
                const prefixMap = new Map<number, number>();
                prefixMap.set(0, 1);
                let curSum = 0;
                for (const val of colSums) {
                    curSum += val;
                    const need = curSum - target;
                    if (prefixMap.has(need)) {
                        result += prefixMap.get(need)!;
                    }
                    prefixMap.set(curSum, (prefixMap.get(curSum) ?? 0) + 1);
                }
            }
        }
    } else {
        // Iterate over pairs of columns (transpose logic)
        for (let left = 0; left < n; ++left) {
            const rowSums = new Array(m).fill(0);
            for (let right = left; right < n; ++right) {
                for (let r = 0; r < m; ++r) {
                    rowSums[r] += matrix[r][right];
                }
                // Count subarrays in rowSums that sum to target
                const prefixMap = new Map<number, number>();
                prefixMap.set(0, 1);
                let curSum = 0;
                for (const val of rowSums) {
                    curSum += val;
                    const need = curSum - target;
                    if (prefixMap.has(need)) {
                        result += prefixMap.get(need)!;
                    }
                    prefixMap.set(curSum, (prefixMap.get(curSum) ?? 0) + 1);
                }
            }
        }
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $matrix
     * @param Integer $target
     * @return Integer
     */
    function numSubmatrixSumTarget($matrix, $target) {
        $rows = count($matrix);
        $cols = count($matrix[0]);
        $result = 0;

        for ($top = 0; $top < $rows; $top++) {
            $colSums = array_fill(0, $cols, 0);
            for ($bottom = $top; $bottom < $rows; $bottom++) {
                // accumulate sums for each column between top and bottom rows
                for ($c = 0; $c < $cols; $c++) {
                    $colSums[$c] += $matrix[$bottom][$c];
                }

                // count subarrays in colSums that sum to target
                $prefixCount = [];
                $prefixCount[0] = 1;
                $currSum = 0;

                foreach ($colSums as $val) {
                    $currSum += $val;
                    $need = $currSum - $target;
                    if (isset($prefixCount[$need])) {
                        $result += $prefixCount[$need];
                    }
                    if (!isset($prefixCount[$currSum])) {
                        $prefixCount[$currSum] = 0;
                    }
                    $prefixCount[$currSum]++;
                }
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func numSubmatrixSumTarget(_ matrix: [[Int]], _ target: Int) -> Int {
        let rows = matrix.count
        guard rows > 0 else { return 0 }
        let cols = matrix[0].count
        var result = 0
        
        for top in 0..<rows {
            var colSums = [Int](repeating: 0, count: cols)
            for bottom in top..<rows {
                for c in 0..<cols {
                    colSums[c] += matrix[bottom][c]
                }
                
                var prefixCount = [Int: Int]()
                prefixCount[0] = 1
                var currentSum = 0
                for sum in colSums {
                    currentSum += sum
                    if let cnt = prefixCount[currentSum - target] {
                        result += cnt
                    }
                    prefixCount[currentSum, default: 0] += 1
                }
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numSubmatrixSumTarget(matrix: Array<IntArray>, target: Int): Int {
        val rows = matrix.size
        val cols = matrix[0].size
        var result = 0L
        for (top in 0 until rows) {
            val colSums = IntArray(cols)
            for (bottom in top until rows) {
                for (c in 0 until cols) {
                    colSums[c] += matrix[bottom][c]
                }
                val map = HashMap<Int, Int>()
                map[0] = 1
                var cur = 0
                for (sum in colSums) {
                    cur += sum
                    result += map.getOrDefault(cur - target, 0)
                    map[cur] = map.getOrDefault(cur, 0) + 1
                }
            }
        }
        return result.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int numSubmatrixSumTarget(List<List<int>> matrix, int target) {
    int m = matrix.length;
    int n = matrix[0].length;
    int result = 0;

    for (int top = 0; top < m; ++top) {
      List<int> colSums = List.filled(n, 0);
      for (int bottom = top; bottom < m; ++bottom) {
        for (int c = 0; c < n; ++c) {
          colSums[c] += matrix[bottom][c];
        }

        Map<int, int> prefixCount = {0: 1};
        int curSum = 0;
        for (int sum in colSums) {
          curSum += sum;
          result += prefixCount[curSum - target] ?? 0;
          prefixCount[curSum] = (prefixCount[curSum] ?? 0) + 1;
        }
      }
    }

    return result;
  }
}
```

## Golang

```go
func numSubmatrixSumTarget(matrix [][]int, target int) int {
    rows := len(matrix)
    cols := len(matrix[0])
    ans := 0

    for top := 0; top < rows; top++ {
        colSums := make([]int, cols)
        for bottom := top; bottom < rows; bottom++ {
            for c := 0; c < cols; c++ {
                colSums[c] += matrix[bottom][c]
            }
            prefixCount := map[int]int{0: 1}
            curSum := 0
            for _, v := range colSums {
                curSum += v
                if cnt, ok := prefixCount[curSum-target]; ok {
                    ans += cnt
                }
                prefixCount[curSum]++
            }
        }
    }

    return ans
}
```

## Ruby

```ruby
def num_submatrix_sum_target(matrix, target)
  m = matrix.size
  n = matrix[0].size
  ans = 0

  (0...m).each do |top|
    col_sums = Array.new(n, 0)
    (top...m).each do |bottom|
      n.times { |c| col_sums[c] += matrix[bottom][c] }

      counts = Hash.new(0)
      counts[0] = 1
      cur = 0
      col_sums.each do |v|
        cur += v
        ans += counts[cur - target]
        counts[cur] += 1
      end
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def numSubmatrixSumTarget(matrix: Array[Array[Int]], target: Int): Int = {
        val m = matrix.length
        val n = matrix(0).length
        var result: Long = 0L

        for (top <- 0 until m) {
            val colSums = new Array[Int](n)
            for (bottom <- top until m) {
                var c = 0
                while (c < n) {
                    colSums(c) += matrix(bottom)(c)
                    c += 1
                }

                val prefixCount = scala.collection.mutable.Map[Int, Int]()
                prefixCount.put(0, 1)

                var prefix = 0
                for (v <- colSums) {
                    prefix += v
                    val need = prefix - target
                    if (prefixCount.contains(need)) {
                        result += prefixCount(need)
                    }
                    prefixCount.put(prefix, prefixCount.getOrElse(prefix, 0) + 1)
                }
            }
        }

        result.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_submatrix_sum_target(matrix: Vec<Vec<i32>>, target: i32) -> i32 {
        let m = matrix.len();
        let n = matrix[0].len();
        let mut ans: i32 = 0;
        for top in 0..m {
            let mut col_sums = vec![0i32; n];
            for bottom in top..m {
                for c in 0..n {
                    col_sums[c] += matrix[bottom][c];
                }
                use std::collections::HashMap;
                let mut map: HashMap<i32, i32> = HashMap::new();
                map.insert(0, 1);
                let mut cur = 0i32;
                for &val in &col_sums {
                    cur += val;
                    if let Some(cnt) = map.get(&(cur - target)) {
                        ans += *cnt;
                    }
                    *map.entry(cur).or_insert(0) += 1;
                }
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (num-submatrix-sum-target matrix target)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ([rows (list->vector (map list->vector matrix))]
         [m (vector-length rows)]
         [n (if (= m 0) 0 (vector-length (vector-ref rows 0)))])
    (define total 0)
    (for ([top (in-range m)])
      (define col-sums (make-vector n 0))
      (for ([bottom (in-range top m)])
        ;; update column sums for the new bottom row
        (let ([row-bot (vector-ref rows bottom)])
          (for ([c (in-range n)])
            (vector-set! col-sums c (+ (vector-ref col-sums c)
                                      (vector-ref row-bot c)))))
        ;; count subarrays in col-sums that sum to target
        (define prefix-count (make-hash))
        (hash-set! prefix-count 0 1)
        (let ([cur 0])
          (for ([c (in-range n)])
            (set! cur (+ cur (vector-ref col-sums c)))
            (define need (- cur target))
            (set! total (+ total (hash-ref prefix-count need 0)))
            (hash-set! prefix-count cur (+ 1 (hash-ref prefix-count cur 0))))))))
    total))
```

## Erlang

```erlang
-module(solution).
-export([num_submatrix_sum_target/2]).

-spec num_submatrix_sum_target(Matrix :: [[integer()]], Target :: integer()) -> integer().
num_submatrix_sum_target(Matrix, Target) ->
    Rows = length(Matrix),
    case Matrix of
        [] -> 0;
        _ ->
            Cols = length(hd(Matrix)),
            TopIndices = lists:seq(0, Rows - 1),
            lists:foldl(
                fun(Top, Acc) ->
                    ZeroSums = lists:duplicate(Cols, 0),
                    {_, SubTotal} = lists:foldl(
                        fun(Bottom, {ColSums, Count}) ->
                            Row = lists:nth(Bottom + 1, Matrix),
                            NewColSums = add_rows(ColSums, Row),
                            Add = count_subarrays(Target, NewColSums),
                            {NewColSums, Count + Add}
                        end,
                        {ZeroSums, 0},
                        lists:seq(Top, Rows - 1)
                    ),
                    Acc + SubTotal
                end,
                0,
                TopIndices
            )
    end.

add_rows([], []) -> [];
add_rows([H|T], [R|Rest]) -> [(H + R) | add_rows(T, Rest)].

-spec count_subarrays(Target :: integer(), List :: [integer()]) -> integer().
count_subarrays(Target, List) ->
    {_, _, Result} = lists:foldl(
        fun(X, {Cum, Map, Ans}) ->
            NewCum = Cum + X,
            Add = maps:get(NewCum - Target, Map, 0),
            NewAns = Ans + Add,
            NewCount = maps:get(NewCum, Map, 0) + 1,
            NewMap = Map#{NewCum => NewCount},
            {NewCum, NewMap, NewAns}
        end,
        {0, #{0 => 1}, 0},
        List),
    Result.
```

## Elixir

```elixir
defmodule Solution do
  @spec num_submatrix_sum_target(matrix :: [[integer]], target :: integer) :: integer
  def num_submatrix_sum_target(matrix, target) do
    m = length(matrix)
    n = matrix |> hd() |> length()

    Enum.reduce(0..(m - 1), 0, fn r1, total ->
      {_, cnt} =
        Enum.reduce(r1..(m - 1), {List.duplicate(0, n), 0}, fn r2, {col_sums, acc_cnt} ->
          row = Enum.at(matrix, r2)

          new_col_sums =
            Enum.map(Enum.with_index(col_sums), fn {sum, idx} ->
              sum + Enum.at(row, idx)
            end)

          added = count_subarrays(new_col_sums, target)
          {new_col_sums, acc_cnt + added}
        end)

      total + cnt
    end)
  end

  defp count_subarrays(arr, target) do
    {_pref, _map, cnt} =
      Enum.reduce(arr, {0, %{0 => 1}, 0}, fn x, {pref, map, cnt} ->
        new_pref = pref + x
        add = Map.get(map, new_pref - target, 0)
        new_map = Map.update(map, new_pref, 1, &(&1 + 1))
        {new_pref, new_map, cnt + add}
      end)

    cnt
  end
end
```
