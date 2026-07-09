# 0174. Dungeon Game

## Cpp

```cpp
class Solution {
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon) {
        int m = dungeon.size();
        int n = dungeon[0].size();
        const int INF = 1e9;
        vector<int> dp(n, INF);
        for (int i = m - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                if (i == m - 1 && j == n - 1) {
                    dp[j] = max(1, 1 - dungeon[i][j]);
                } else {
                    int down = (i + 1 < m) ? dp[j] : INF;
                    int right = (j + 1 < n) ? dp[j + 1] : INF;
                    int need = min(down, right) - dungeon[i][j];
                    dp[j] = max(1, need);
                }
            }
        }
        return dp[0];
    }
};
```

## Java

```java
class Solution {
    public int calculateMinimumHP(int[][] dungeon) {
        int m = dungeon.length;
        int n = dungeon[0].length;
        int INF = Integer.MAX_VALUE / 2;
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 0; i <= m; i++) {
            java.util.Arrays.fill(dp[i], INF);
        }
        dp[m][n - 1] = 1;
        dp[m - 1][n] = 1;
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                int need = Math.min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j];
                dp[i][j] = Math.max(need, 1);
            }
        }
        return dp[0][0];
    }
}
```

## Python

```python
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])
        INF = float('inf')
        dp = [[INF] * (n + 1) for _ in range(m + 1)]
        dp[m][n - 1] = dp[m - 1][n] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                need = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                dp[i][j] = max(need, 1)
        return dp[0][0]
```

## Python3

```python
from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        dp[m][n - 1] = dp[m - 1][n] = 1  # sentinel cells beyond bottom/right

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                need = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                dp[i][j] = max(need, 1)

        return dp[0][0]
```

## C

```c
#include <stdlib.h>
#include <limits.h>

int calculateMinimumHP(int** dungeon, int dungeonSize, int* dungeonColSize) {
    int m = dungeonSize;
    int n = dungeonColSize[0];
    
    // Allocate dp array with extra row and column for sentinel values
    int **dp = (int **)malloc((m + 1) * sizeof(int *));
    for (int i = 0; i <= m; ++i) {
        dp[i] = (int *)malloc((n + 1) * sizeof(int));
        for (int j = 0; j <= n; ++j) {
            dp[i][j] = INT_MAX;
        }
    }
    
    // Set sentinel cells just beyond the bottom-right corner to 1
    dp[m][n - 1] = 1;
    dp[m - 1][n] = 1;
    
    for (int i = m - 1; i >= 0; --i) {
        for (int j = n - 1; j >= 0; --j) {
            int min_next = dp[i + 1][j] < dp[i][j + 1] ? dp[i + 1][j] : dp[i][j + 1];
            int need = min_next - dungeon[i][j];
            if (need <= 0) need = 1;
            dp[i][j] = need;
        }
    }
    
    int result = dp[0][0];
    
    // Free allocated memory
    for (int i = 0; i <= m; ++i) {
        free(dp[i]);
    }
    free(dp);
    
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int CalculateMinimumHP(int[][] dungeon)
    {
        int m = dungeon.Length;
        int n = dungeon[0].Length;
        int[,] dp = new int[m + 1, n + 1];
        const int INF = int.MaxValue / 2;

        for (int i = 0; i <= m; i++)
            for (int j = 0; j <= n; j++)
                dp[i, j] = INF;

        dp[m, n - 1] = 1;
        dp[m - 1, n] = 1;

        for (int i = m - 1; i >= 0; i--)
        {
            for (int j = n - 1; j >= 0; j--)
            {
                int need = Math.Min(dp[i + 1, j], dp[i, j + 1]) - dungeon[i][j];
                dp[i, j] = need <= 0 ? 1 : need;
            }
        }

        return dp[0, 0];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} dungeon
 * @return {number}
 */
var calculateMinimumHP = function(dungeon) {
    const m = dungeon.length;
    const n = dungeon[0].length;
    const dp = Array.from({ length: m + 1 }, () => Array(n + 1).fill(Infinity));
    dp[m][n - 1] = 1;
    dp[m - 1][n] = 1;

    for (let i = m - 1; i >= 0; i--) {
        for (let j = n - 1; j >= 0; j--) {
            const need = Math.min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j];
            dp[i][j] = need <= 0 ? 1 : need;
        }
    }

    return dp[0][0];
};
```

## Typescript

```typescript
function calculateMinimumHP(dungeon: number[][]): number {
    const m = dungeon.length;
    const n = dungeon[0].length;
    const dp: number[][] = Array.from({ length: m }, () => new Array(n).fill(0));

    for (let i = m - 1; i >= 0; i--) {
        for (let j = n - 1; j >= 0; j--) {
            if (i === m - 1 && j === n - 1) {
                dp[i][j] = Math.max(1 - dungeon[i][j], 1);
            } else if (i === m - 1) {
                dp[i][j] = Math.max(dp[i][j + 1] - dungeon[i][j], 1);
            } else if (j === n - 1) {
                dp[i][j] = Math.max(dp[i + 1][j] - dungeon[i][j], 1);
            } else {
                const needNext = Math.min(dp[i + 1][j], dp[i][j + 1]);
                dp[i][j] = Math.max(needNext - dungeon[i][j], 1);
            }
        }
    }

    return dp[0][0];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $dungeon
     * @return Integer
     */
    function calculateMinimumHP($dungeon) {
        $m = count($dungeon);
        $n = count($dungeon[0]);
        // dp array with extra row and column filled with max int
        $dp = array_fill(0, $m + 1, array_fill(0, $n + 1, PHP_INT_MAX));
        // Set the cells beyond the princess's cell to 1 (minimum health needed)
        $dp[$m][$n - 1] = 1;
        $dp[$m - 1][$n] = 1;

        for ($i = $m - 1; $i >= 0; $i--) {
            for ($j = $n - 1; $j >= 0; $j--) {
                $minHealthOnExit = min($dp[$i + 1][$j], $dp[$i][$j + 1]);
                $need = $minHealthOnExit - $dungeon[$i][$j];
                if ($need <= 0) {
                    $need = 1;
                }
                $dp[$i][$j] = $need;
            }
        }

        return $dp[0][0];
    }
}
```

## Swift

```swift
class Solution {
    func calculateMinimumHP(_ dungeon: [[Int]]) -> Int {
        let m = dungeon.count
        let n = dungeon[0].count
        var dp = Array(repeating: Array(repeating: 0, count: n), count: m)
        
        for i in stride(from: m - 1, through: 0, by: -1) {
            for j in stride(from: n - 1, through: 0, by: -1) {
                if i == m - 1 && j == n - 1 {
                    dp[i][j] = max(1, 1 - dungeon[i][j])
                } else {
                    var minHealthOnExit = Int.max
                    if i + 1 < m { minHealthOnExit = min(minHealthOnExit, dp[i + 1][j]) }
                    if j + 1 < n { minHealthOnExit = min(minHealthOnExit, dp[i][j + 1]) }
                    dp[i][j] = max(1, minHealthOnExit - dungeon[i][j])
                }
            }
        }
        
        return dp[0][0]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun calculateMinimumHP(dungeon: Array<IntArray>): Int {
        val m = dungeon.size
        val n = dungeon[0].size
        val dp = Array(m + 1) { IntArray(n + 1) { Int.MAX_VALUE } }
        dp[m][n - 1] = 1
        dp[m - 1][n] = 1

        for (i in m - 1 downTo 0) {
            for (j in n - 1 downTo 0) {
                val need = kotlin.math.min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                dp[i][j] = if (need <= 0) 1 else need
            }
        }
        return dp[0][0]
    }
}
```

## Dart

```dart
class Solution {
  int calculateMinimumHP(List<List<int>> dungeon) {
    int m = dungeon.length;
    int n = dungeon[0].length;
    const int INF = 1 << 30;
    List<List<int>> dp = List.generate(m + 1, (_) => List.filled(n + 1, INF));
    dp[m][n - 1] = 1;
    dp[m - 1][n] = 1;

    for (int i = m - 1; i >= 0; i--) {
      for (int j = n - 1; j >= 0; j--) {
        int minNext = dp[i + 1][j] < dp[i][j + 1] ? dp[i + 1][j] : dp[i][j + 1];
        int need = minNext - dungeon[i][j];
        if (need <= 0) need = 1;
        dp[i][j] = need;
      }
    }

    return dp[0][0];
  }
}
```

## Golang

```go
func calculateMinimumHP(dungeon [][]int) int {
	m := len(dungeon)
	n := len(dungeon[0])
	const INF = int(^uint(0) >> 1) // max int
	// dp with extra row and column filled with INF
	dp := make([][]int, m+1)
	for i := range dp {
		dp[i] = make([]int, n+1)
		for j := range dp[i] {
			dp[i][j] = INF
		}
	}
	// The princess cell needs at least 1 HP after leaving it
	dp[m][n-1] = 1
	dp[m-1][n] = 1

	for i := m - 1; i >= 0; i-- {
		for j := n - 1; j >= 0; j-- {
			minNext := dp[i+1][j]
			if dp[i][j+1] < minNext {
				minNext = dp[i][j+1]
			}
			need := minNext - dungeon[i][j]
			if need <= 0 {
				need = 1
			}
			dp[i][j] = need
		}
	}
	return dp[0][0]
}
```

## Ruby

```ruby
def calculate_minimum_hp(dungeon)
  m = dungeon.size
  n = dungeon[0].size
  inf = 1 << 60
  dp = Array.new(m + 1) { Array.new(n + 1, inf) }
  dp[m][n - 1] = dp[m - 1][n] = 1

  (m - 1).downto(0) do |i|
    (n - 1).downto(0) do |j|
      need = [dp[i + 1][j], dp[i][j + 1]].min - dungeon[i][j]
      dp[i][j] = need <= 0 ? 1 : need
    end
  end

  dp[0][0]
end
```

## Scala

```scala
object Solution {
  def calculateMinimumHP(dungeon: Array[Array[Int]]): Int = {
    val m = dungeon.length
    val n = dungeon(0).length
    val dp = Array.ofDim[Int](m + 1, n + 1)
    for (i <- 0 to m) java.util.Arrays.fill(dp(i), Int.MaxValue)
    dp(m)(n - 1) = 1
    dp(m - 1)(n) = 1

    for (i <- (m - 1) to 0 by -1) {
      for (j <- (n - 1) to 0 by -1) {
        val need = Math.min(dp(i + 1)(j), dp(i)(j + 1)) - dungeon(i)(j)
        dp(i)(j) = if (need <= 0) 1 else need
      }
    }
    dp(0)(0)
  }
}
```

## Rust

```rust
impl Solution {
    pub fn calculate_minimum_hp(dungeon: Vec<Vec<i32>>) -> i32 {
        let m = dungeon.len();
        let n = dungeon[0].len();
        // dp with extra row and column filled with a large value.
        let mut dp = vec![vec![i32::MAX; n + 1]; m + 1];
        dp[m][n - 1] = 1;
        dp[m - 1][n] = 1;

        for i in (0..m).rev() {
            for j in (0..n).rev() {
                let min_next = std::cmp::min(dp[i + 1][j], dp[i][j + 1]);
                let need = min_next - dungeon[i][j];
                dp[i][j] = if need <= 0 { 1 } else { need };
            }
        }

        dp[0][0]
    }
}
```

## Racket

```racket
#lang racket

(define/contract (calculate-minimum-hp dungeon)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((vd (list->vector (map list->vector dungeon)))
         (m (vector-length vd))
         (n (if (= m 0) 0 (vector-length (vector-ref vd 0))))
         (dp (make-vector m)))
    (for ([i (in-range m)])
      (vector-set! dp i (make-vector n 0)))
    (define big 1000000000)
    (for ([i (in-range (sub1 m) -1 -1)])
      (for ([j (in-range (sub1 n) -1 -1)])
        (let* ((cell (vector-ref (vector-ref vd i) j))
               (needed
                 (if (and (= i (sub1 m)) (= j (sub1 n)))
                     (max 1 (- 1 cell))
                     (let* ((down (if (< (add1 i) m)
                                      (vector-ref (vector-ref dp (add1 i)) j)
                                      big))
                            (right (if (< (add1 j) n)
                                       (vector-ref (vector-ref dp i) (add1 j))
                                       big))
                            (min-next (min down right)))
                       (max 1 (- min-next cell))))))
          (vector-set! (vector-ref dp i) j needed))))
    (vector-ref (vector-ref dp 0) 0)))
```

## Erlang

```erlang
-spec calculate_minimum_hp(Dungeon :: [[integer()]]) -> integer().
calculate_minimum_hp(Dungeon) ->
    M = length(Dungeon),
    [FirstRow|_] = Dungeon,
    N = length(FirstRow),
    DRowsTuples = [list_to_tuple(Row) || Row <- Dungeon],
    D = list_to_tuple(DRowsTuples),
    RowsBottomUp = build_rows(M - 1, D, M, N, undefined),
    DP_Tuple = list_to_tuple(lists:reverse(RowsBottomUp)),
    element(1, element(1, DP_Tuple)).

build_rows(-1, _D, _M, _N, _NextRow) ->
    [];
build_rows(I, D, M, N, NextRowDp) ->
    RowTuple = element(I + 1, D),
    CurRowList = build_row(N - 1, RowTuple, I, M, N, NextRowDp, [], undefined),
    CurRowTuple = list_to_tuple(CurRowList),
    [CurRowTuple | build_rows(I - 1, D, M, N, CurRowTuple)].

build_row(-1, _RowTuple, _I, _M, _N, _NextRowDp, AccRev, _RightNeeded) ->
    lists:reverse(AccRev);
build_row(J, RowTuple, I, M, N, NextRowDp, AccRev, RightNeeded) ->
    Cell = element(J + 1, RowTuple),
    DownNeeded =
        case I == M - 1 of
            true -> undefined;
            false -> element(J + 1, NextRowDp)
        end,
    MinNext =
        case {I == M - 1, J == N - 1} of
            {true, true} ->
                1;
            {true, false} ->
                RightNeeded;
            {false, true} ->
                DownNeeded;
            {false, false} ->
                erlang:min(RightNeeded, DownNeeded)
        end,
    Needed = erlang:max(1, MinNext - Cell),
    build_row(J - 1, RowTuple, I, M, N, NextRowDp, [Needed | AccRev], Needed).
```

## Elixir

```elixir
defmodule Solution do
  @spec calculate_minimum_hp(dungeon :: [[integer]]) :: integer
  def calculate_minimum_hp(dungeon) do
    m = length(dungeon)
    n = dungeon |> List.first() |> length()
    inf = 1_000_000_000

    # health tuple indices: 1..n+1, where index n+1 is the sentinel (right of last column)
    health =
      :erlang.make_tuple(n + 1, inf)
      |> put_elem(n + 1, 1)

    Enum.reduce(Enum.reverse(dungeon), health, fn row, acc_health ->
      process_row(row, acc_health, n)
    end)
    |> elem(1)
  end

  defp process_row(row, health, n) do
    indices = Enum.to_list(0..(n - 1)) |> Enum.reverse()

    Enum.reduce(indices, health, fn j, acc ->
      cell = Enum.at(row, j)

      need =
        min(elem(acc, j + 1), elem(acc, j + 2)) - cell

      new_val = if need < 1, do: 1, else: need
      put_elem(acc, j + 1, new_val)
    end)
  end
end
```
