# 2017. Grid Game

## Cpp

```cpp
class Solution {
public:
    long long gridGame(vector<vector<int>>& grid) {
        int n = grid[0].size();
        long long topSum = 0, bottomSum = 0;
        for (int i = 0; i < n; ++i) topSum += grid[0][i];
        long long ans = LLONG_MAX;
        for (int i = 0; i < n; ++i) {
            topSum -= grid[0][i];                 // cells to the right of column i
            long long cur = max(topSum, bottomSum);
            ans = min(ans, cur);
            bottomSum += grid[1][i];              // cells to the left of next column
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long gridGame(int[][] grid) {
        int n = grid[0].length;
        long topSum = 0;
        for (int i = 0; i < n; i++) {
            topSum += grid[0][i];
        }
        long bottomSum = 0;
        long answer = Long.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            topSum -= grid[0][i]; // points remaining in top row after column i
            long candidate = Math.max(topSum, bottomSum);
            if (candidate < answer) {
                answer = candidate;
            }
            bottomSum += grid[1][i]; // include current bottom cell for next iteration
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def gridGame(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid[0])
        top_remaining = sum(grid[0])
        bottom_collected = 0
        ans = float('inf')
        for i in range(n):
            top_remaining -= grid[0][i]
            ans = min(ans, max(top_remaining, bottom_collected))
            bottom_collected += grid[1][i]
        return int(ans)
```

## Python3

```python
class Solution:
    def gridGame(self, grid: list[list[int]]) -> int:
        top_sum = sum(grid[0])
        bottom_prefix = 0
        ans = float('inf')
        n = len(grid[0])
        for i in range(n):
            top_sum -= grid[0][i]
            cur = max(top_sum, bottom_prefix)
            if cur < ans:
                ans = cur
            bottom_prefix += grid[1][i]
        return ans
```

## C

```c
#include <limits.h>

long long gridGame(int** grid, int gridSize, int* gridColSize) {
    int n = gridColSize[0];
    long long sumTop = 0;
    for (int i = 0; i < n; ++i) {
        sumTop += grid[0][i];
    }
    long long sumBottom = 0;
    long long answer = LLONG_MAX;

    for (int i = 0; i < n; ++i) {
        sumTop -= grid[0][i];                 // points remaining on top row after column i
        long long cur = sumTop > sumBottom ? sumTop : sumBottom; // second robot's best gain
        if (cur < answer) answer = cur;
        sumBottom += grid[1][i];              // accumulate bottom row points up to column i
    }
    return answer;
}
```

## Csharp

```csharp
public class Solution {
    public long GridGame(int[][] grid) {
        int n = grid[0].Length;
        long topSum = 0;
        for (int i = 0; i < n; i++) {
            topSum += grid[0][i];
        }
        long bottomSum = 0;
        long answer = long.MaxValue;
        for (int col = 0; col < n; col++) {
            topSum -= grid[0][col];
            long current = topSum > bottomSum ? topSum : bottomSum;
            if (current < answer) answer = current;
            bottomSum += grid[1][col];
        }
        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var gridGame = function(grid) {
    const top = grid[0];
    const bottom = grid[1];
    let sumTop = 0;
    for (let v of top) sumTop += v;
    
    let sumBottom = 0;
    let answer = Infinity;
    
    const n = top.length;
    for (let i = 0; i < n; ++i) {
        // first robot takes top[i] before moving down
        sumTop -= top[i];
        // second robot's best possible gain after this turn
        const cur = Math.max(sumTop, sumBottom);
        if (cur < answer) answer = cur;
        // bottom cell becomes available for future turns
        sumBottom += bottom[i];
    }
    
    return answer;
};
```

## Typescript

```typescript
function gridGame(grid: number[][]): number {
    const n = grid[0].length;
    let topSum = 0;
    for (let i = 0; i < n; i++) {
        topSum += grid[0][i];
    }
    let bottomSum = 0;
    let answer = Number.MAX_SAFE_INTEGER;
    for (let i = 0; i < n; i++) {
        topSum -= grid[0][i];               // points remaining on top row after column i
        const cur = Math.max(topSum, bottomSum);
        if (cur < answer) answer = cur;
        bottomSum += grid[1][i];            // accumulate points on bottom row before column i+1
    }
    return answer;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function gridGame($grid) {
        $n = count($grid[0]);
        $topSum = 0;
        for ($i = 0; $i < $n; $i++) {
            $topSum += $grid[0][$i];
        }
        $bottomSum = 0;
        $ans = PHP_INT_MAX;
        for ($i = 0; $i < $n; $i++) {
            $topSum -= $grid[0][$i];               // points remaining on top row after column i
            $maxPoints = max($topSum, $bottomSum); // best second robot can achieve for this turn
            if ($maxPoints < $ans) {
                $ans = $maxPoints;
            }
            $bottomSum += $grid[1][$i];             // points accumulated on bottom row before column i+1
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func gridGame(_ grid: [[Int]]) -> Int {
        let n = grid[0].count
        var topSum = 0
        for val in grid[0] {
            topSum += val
        }
        var bottomPrefix = 0
        var answer = Int.max
        for i in 0..<n {
            topSum -= grid[0][i]
            let current = max(topSum, bottomPrefix)
            if current < answer {
                answer = current
            }
            bottomPrefix += grid[1][i]
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun gridGame(grid: Array<IntArray>): Long {
        val n = grid[0].size
        var topRemaining = 0L
        for (v in grid[0]) topRemaining += v.toLong()
        var bottomCollected = 0L
        var answer = Long.MAX_VALUE
        for (i in 0 until n) {
            topRemaining -= grid[0][i].toLong()
            val cur = if (topRemaining > bottomCollected) topRemaining else bottomCollected
            if (cur < answer) answer = cur
            bottomCollected += grid[1][i].toLong()
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int gridGame(List<List<int>> grid) {
    int n = grid[0].length;
    int topSum = 0;
    for (int v in grid[0]) topSum += v;

    int bottomSum = 0;
    int answer = 1 << 60; // large number

    for (int i = 0; i < n; i++) {
      topSum -= grid[0][i];
      int current = topSum > bottomSum ? topSum : bottomSum;
      if (current < answer) answer = current;
      bottomSum += grid[1][i];
    }
    return answer;
  }
}
```

## Golang

```go
package main

import (
	"math"
)

func gridGame(grid [][]int) int64 {
	n := len(grid[0])
	var topSum int64
	for i := 0; i < n; i++ {
		topSum += int64(grid[0][i])
	}
	var bottomSum int64
	ans := int64(math.MaxInt64)

	for i := 0; i < n; i++ {
		topSum -= int64(grid[0][i]) // points remaining in top row to the right of column i
		if topSum > bottomSum {
			if topSum < ans {
				ans = topSum
			}
		} else {
			if bottomSum < ans {
				ans = bottomSum
			}
		}
		bottomSum += int64(grid[1][i]) // points in bottom row to the left of column i+1
	}
	return ans
}
```

## Ruby

```ruby
def grid_game(grid)
  top_sum = grid[0].sum
  bottom_sum = 0
  min_max = (1 << 62)

  n = grid[0].length
  (0...n).each do |i|
    top_sum -= grid[0][i]
    cur = top_sum > bottom_sum ? top_sum : bottom_sum
    min_max = cur if cur < min_max
    bottom_sum += grid[1][i]
  end

  min_max
end
```

## Scala

```scala
object Solution {
    def gridGame(grid: Array[Array[Int]]): Long = {
        val n = grid(0).length
        var topSum: Long = 0L
        for (c <- 0 until n) {
            topSum += grid(0)(c).toLong
        }
        var bottomSum: Long = 0L
        var answer: Long = Long.MaxValue

        for (i <- 0 until n) {
            topSum -= grid(0)(i).toLong          // sum of top row cells after column i
            val cur = math.max(topSum, bottomSum) // best second robot can achieve if first turns at i
            if (cur < answer) answer = cur
            bottomSum += grid(1)(i).toLong        // accumulate bottom row cells before next turn
        }
        answer
    }
}
```

## Rust

```rust
impl Solution {
    pub fn grid_game(grid: Vec<Vec<i32>>) -> i64 {
        let n = grid[0].len();
        let mut top_sum: i64 = grid[0].iter().map(|&v| v as i64).sum();
        let mut bottom_sum: i64 = 0;
        let mut ans: i64 = i64::MAX;
        for col in 0..n {
            top_sum -= grid[0][col] as i64;
            let candidate = if top_sum > bottom_sum { top_sum } else { bottom_sum };
            if candidate < ans {
                ans = candidate;
            }
            bottom_sum += grid[1][col] as i64;
        }
        ans
    }
}
```

## Racket

```racket
#lang racket

(define/contract (grid-game grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((top-row   (list-ref grid 0))
         (bottom-row (list-ref grid 1))
         (n (length top-row))
         (total-top (foldl + 0 top-row))
         (big (expt 2 62))) ; sufficiently large
    (let loop ((i 0) (top-rem total-top) (bottom-sum 0) (ans big))
      (if (= i n)
          ans
          (let* ((top-rem2 (- top-rem (list-ref top-row i)))
                 (candidate (max top-rem2 bottom-sum))
                 (ans2 (min ans candidate))
                 (bottom-sum2 (+ bottom-sum (list-ref bottom-row i))))
            (loop (+ i 1) top-rem2 bottom-sum2 ans2)))))
```

## Erlang

```erlang
-spec grid_game(Grid :: [[integer()]]) -> integer().
grid_game(Grid) ->
    [Top, Bottom] = Grid,
    TotalTop = lists:sum(Top),
    loop(Top, Bottom, TotalTop, 0, 1 bsl 60).

loop([], [], _RemTop, _AccBottom, Min) ->
    Min;
loop([Htop|RestTop], [Hbottom|RestBottom], RemTop, AccBottom, Min) ->
    NewRemTop = RemTop - Htop,
    MaxVal = erlang:max(NewRemTop, AccBottom),
    NewMin = if MaxVal < Min -> MaxVal; true -> Min end,
    loop(RestTop, RestBottom, NewRemTop, AccBottom + Hbottom, NewMin).
```

## Elixir

```elixir
defmodule Solution do
  @spec grid_game(grid :: [[integer]]) :: integer
  def grid_game(grid) do
    [top_row, bottom_row] = grid
    total_top = Enum.reduce(top_row, 0, &+/2)
    initial_best = 1 <<< 60

    iterate(top_row, bottom_row, total_top, 0, initial_best)
  end

  defp iterate([], [], _suffix_top, _prefix_bottom, best), do: best

  defp iterate([t_head | t_tail], [b_head | b_tail], suffix_top, prefix_bottom, best) do
    new_suffix = suffix_top - t_head
    max_val = if new_suffix > prefix_bottom, do: new_suffix, else: prefix_bottom
    new_best = if max_val < best, do: max_val, else: best
    new_prefix = prefix_bottom + b_head

    iterate(t_tail, b_tail, new_suffix, new_prefix, new_best)
  end
end
```
