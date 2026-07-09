# 1981. Minimize the Difference Between Target and Chosen Elements

## Cpp

```cpp
class Solution {
public:
    int minimizeTheDifference(vector<vector<int>>& mat, int target) {
        int m = mat.size();
        int maxSum = m * 70; // maximum possible sum
        vector<char> dp(maxSum + 1, false);
        dp[0] = true;
        for (const auto& row : mat) {
            vector<char> ndp(maxSum + 1, false);
            for (int s = 0; s <= maxSum; ++s) {
                if (!dp[s]) continue;
                for (int v : row) {
                    int ns = s + v;
                    if (ns <= maxSum) ndp[ns] = true;
                }
            }
            dp.swap(ndp);
        }
        int ans = INT_MAX;
        for (int s = 0; s <= maxSum; ++s) {
            if (dp[s]) {
                ans = min(ans, abs(s - target));
                if (ans == 0) break;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minimizeTheDifference(int[][] mat, int target) {
        int m = mat.length;
        int maxSum = m * 70; // maximum possible sum
        boolean[] dp = new boolean[maxSum + 1];
        for (int v : mat[0]) {
            if (v <= maxSum) dp[v] = true;
        }
        for (int i = 1; i < m; i++) {
            boolean[] ndp = new boolean[maxSum + 1];
            for (int s = 0; s <= maxSum; s++) {
                if (!dp[s]) continue;
                for (int v : mat[i]) {
                    int ns = s + v;
                    if (ns <= maxSum) ndp[ns] = true;
                }
            }
            dp = ndp;
        }
        int ans = Integer.MAX_VALUE;
        for (int s = 0; s <= maxSum; s++) {
            if (dp[s]) {
                int diff = Math.abs(target - s);
                if (diff < ans) ans = diff;
                if (ans == 0) break;
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def minimizeTheDifference(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: int
        :rtype: int
        """
        m = len(mat)
        max_sum = m * 70  # maximum possible sum given constraints
        dp = 1  # bitmask with only sum 0 reachable

        for row in mat:
            new_dp = 0
            for v in row:
                new_dp |= dp << v
            dp = new_dp

        # Find minimal absolute difference
        for diff in range(max_sum + 1):
            low = target - diff
            high = target + diff
            if low >= 0 and ((dp >> low) & 1):
                return diff
            if high <= max_sum and ((dp >> high) & 1):
                return diff
        # Should never reach here because at least one sum is reachable
        return -1
```

## Python3

```python
from typing import List

class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        max_sum = sum(max(row) for row in mat)
        dp = 1  # bitmask with only sum 0 possible
        mask_limit = (1 << (max_sum + 1)) - 1

        for row in mat:
            ndp = 0
            for v in row:
                ndp |= dp << v
            dp = ndp & mask_limit

        ans = float('inf')
        for s in range(max_sum + 1):
            if (dp >> s) & 1:
                diff = target - s
                if diff < 0:
                    diff = -diff
                if diff < ans:
                    ans = diff
                    if ans == 0:
                        return 0
        return ans
```

## C

```c
#include <stdlib.h>
#include <limits.h>

int minimizeTheDifference(int** mat, int matSize, int* matColSize, int target) {
    if (matSize == 0) return target;
    
    // Compute maximum possible sum (sum of max element in each row)
    int maxSum = 0;
    for (int i = 0; i < matSize; ++i) {
        int rowMax = 0;
        for (int j = 0; j < matColSize[i]; ++j) {
            if (mat[i][j] > rowMax) rowMax = mat[i][j];
        }
        maxSum += rowMax;
    }

    char *dp = (char *)calloc(maxSum + 1, sizeof(char));
    char *next = (char *)calloc(maxSum + 1, sizeof(char));

    // Initialize with first row
    for (int j = 0; j < matColSize[0]; ++j) {
        int val = mat[0][j];
        dp[val] = 1;
    }

    // Process remaining rows
    for (int i = 1; i < matSize; ++i) {
        // clear next
        for (int s = 0; s <= maxSum; ++s) next[s] = 0;

        for (int sum = 0; sum <= maxSum; ++sum) {
            if (!dp[sum]) continue;
            for (int j = 0; j < matColSize[i]; ++j) {
                int ns = sum + mat[i][j];
                if (ns <= maxSum) next[ns] = 1;
            }
        }

        // swap dp and next
        char *tmp = dp;
        dp = next;
        next = tmp;
    }

    int best = INT_MAX;
    for (int sum = 0; sum <= maxSum; ++sum) {
        if (!dp[sum]) continue;
        int diff = sum > target ? sum - target : target - sum;
        if (diff < best) best = diff;
        if (best == 0) break;
    }

    free(dp);
    free(next);
    return best;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimizeTheDifference(int[][] mat, int target) {
        int m = mat.Length;
        int totalMax = 0;
        foreach (var row in mat) {
            int maxRow = 0;
            foreach (int v in row) if (v > maxRow) maxRow = v;
            totalMax += maxRow;
        }

        bool[] dp = new bool[totalMax + 1];
        foreach (int v in mat[0]) {
            dp[v] = true;
        }

        for (int i = 1; i < m; i++) {
            bool[] ndp = new bool[totalMax + 1];
            var row = mat[i];
            for (int sum = 0; sum <= totalMax; sum++) {
                if (!dp[sum]) continue;
                foreach (int v in row) {
                    int ns = sum + v;
                    ndp[ns] = true;
                }
            }
            dp = ndp;
        }

        int ans = int.MaxValue;
        for (int s = 0; s <= totalMax; s++) {
            if (dp[s]) {
                int diff = Math.Abs(s - target);
                if (diff < ans) ans = diff;
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
 * @param {number} target
 * @return {number}
 */
var minimizeTheDifference = function(mat, target) {
    const m = mat.length;
    const maxSum = m * 70; // each element <=70
    let dp = new Uint8Array(maxSum + 1);
    dp[0] = 1;
    
    for (const row of mat) {
        const ndp = new Uint8Array(maxSum + 1);
        for (let s = 0; s <= maxSum; ++s) {
            if (dp[s]) {
                for (const v of row) {
                    const ns = s + v;
                    if (ns <= maxSum) ndp[ns] = 1;
                }
            }
        }
        dp = ndp;
    }
    
    let ans = Infinity;
    for (let s = 0; s <= maxSum; ++s) {
        if (dp[s]) {
            const diff = Math.abs(s - target);
            if (diff < ans) ans = diff;
            if (ans === 0) break;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function minimizeTheDifference(mat: number[][], target: number): number {
    const m = mat.length;
    let maxSum = 0;
    for (const row of mat) {
        let mx = 0;
        for (const v of row) if (v > mx) mx = v;
        maxSum += mx;
    }

    let dp = new Uint8Array(maxSum + 1);
    dp[0] = 1;

    for (const row of mat) {
        const ndp = new Uint8Array(maxSum + 1);
        for (let s = 0; s <= maxSum; ++s) {
            if (!dp[s]) continue;
            for (const v of row) {
                ndp[s + v] = 1;
            }
        }
        dp = ndp;
    }

    let ans = Number.MAX_SAFE_INTEGER;
    for (let s = 0; s <= maxSum; ++s) {
        if (dp[s]) {
            const diff = Math.abs(s - target);
            if (diff < ans) ans = diff;
            if (ans === 0) break;
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
     * @param Integer $target
     * @return Integer
     */
    function minimizeTheDifference($mat, $target) {
        $m = count($mat);
        $maxSum = $m * 70; // maximum possible sum

        $dp = array_fill(0, $maxSum + 1, false);
        $dp[0] = true;

        foreach ($mat as $row) {
            $new = array_fill(0, $maxSum + 1, false);
            foreach ($row as $val) {
                for ($s = 0; $s <= $maxSum - $val; $s++) {
                    if ($dp[$s]) {
                        $new[$s + $val] = true;
                    }
                }
            }
            $dp = $new;
        }

        $ans = PHP_INT_MAX;
        for ($s = 0; $s <= $maxSum; $s++) {
            if ($dp[$s]) {
                $diff = abs($target - $s);
                if ($diff < $ans) {
                    $ans = $diff;
                    if ($ans == 0) {
                        break;
                    }
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
    func minimizeTheDifference(_ mat: [[Int]], _ target: Int) -> Int {
        // Maximum possible sum using the largest element from each row
        let maxSum = mat.reduce(0) { $0 + ($1.max() ?? 0) }
        var dp = [Bool](repeating: false, count: maxSum + 1)
        dp[0] = true
        
        for row in mat {
            var next = [Bool](repeating: false, count: maxSum + 1)
            for s in 0...maxSum where dp[s] {
                for v in row {
                    let ns = s + v
                    if ns <= maxSum {
                        next[ns] = true
                    }
                }
            }
            dp = next
        }
        
        var answer = Int.max
        for s in 0...maxSum where dp[s] {
            let diff = abs(target - s)
            if diff < answer { answer = diff }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimizeTheDifference(mat: Array<IntArray>, target: Int): Int {
        val m = mat.size
        var maxSum = 0
        for (row in mat) {
            var rowMax = 0
            for (v in row) if (v > rowMax) rowMax = v
            maxSum += rowMax
        }
        var dp = BooleanArray(maxSum + 1)
        dp[0] = true
        var curMax = 0
        for (row in mat) {
            val next = BooleanArray(maxSum + 1)
            var newMax = 0
            for (s in 0..curMax) {
                if (!dp[s]) continue
                for (v in row) {
                    val ns = s + v
                    if (ns <= maxSum) {
                        next[ns] = true
                        if (ns > newMax) newMax = ns
                    }
                }
            }
            dp = next
            curMax = newMax
        }
        var ans = Int.MAX_VALUE
        for (s in 0..maxSum) {
            if (dp[s]) {
                val diff = kotlin.math.abs(target - s)
                if (diff < ans) ans = diff
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int minimizeTheDifference(List<List<int>> mat, int target) {
    int m = mat.length;
    // Upper bound for possible sum: each row contributes at most 70
    int maxSum = m * 70;

    List<bool> dp = List.filled(maxSum + 1, false);
    dp[0] = true;

    for (var row in mat) {
      List<bool> ndp = List.filled(maxSum + 1, false);
      for (int s = 0; s <= maxSum; ++s) {
        if (!dp[s]) continue;
        for (int val in row) {
          int ns = s + val;
          if (ns <= maxSum) ndp[ns] = true;
        }
      }
      dp = ndp;
    }

    int best = maxSum;
    for (int s = 0; s <= maxSum; ++s) {
      if (dp[s]) {
        int diff = (s - target).abs();
        if (diff < best) {
          best = diff;
          if (best == 0) break;
        }
      }
    }
    return best;
  }
}
```

## Golang

```go
func minimizeTheDifference(mat [][]int, target int) int {
	m := len(mat)
	// compute maximum possible sum
	maxSum := 0
	rowMaxVals := make([]int, m)
	for i, row := range mat {
		rowMax := 0
		for _, v := range row {
			if v > rowMax {
				rowMax = v
			}
		}
		rowMaxVals[i] = rowMax
		maxSum += rowMax
	}

	dp := make([]bool, maxSum+1)
	dp[0] = true
	curMax := 0

	for i, row := range mat {
		newDP := make([]bool, maxSum+1)
		for s := 0; s <= curMax; s++ {
			if !dp[s] {
				continue
			}
			for _, v := range row {
				ns := s + v
				newDP[ns] = true
			}
		}
		dp = newDP
		curMax += rowMaxVals[i]
	}

	ans := int(^uint(0) >> 1) // MaxInt
	for s, ok := range dp {
		if ok {
			diff := target - s
			if diff < 0 {
				diff = -diff
			}
			if diff < ans {
				ans = diff
				if ans == 0 {
					break
				}
			}
		}
	}
	return ans
}
```

## Ruby

```ruby
def minimize_the_difference(mat, target)
  max_sum = mat.map { |row| row.max }.sum
  reachable = Array.new(max_sum + 1, false)
  reachable[0] = true

  mat.each do |row|
    new_reachable = Array.new(max_sum + 1, false)
    (0..max_sum).each do |s|
      next unless reachable[s]
      row.each do |v|
        ns = s + v
        new_reachable[ns] = true if ns <= max_sum
      end
    end
    reachable = new_reachable
  end

  min_diff = Float::INFINITY
  (0..max_sum).each do |s|
    next unless reachable[s]
    diff = (s - target).abs
    min_diff = diff if diff < min_diff
    return 0 if min_diff == 0
  end
  min_diff.to_i
end
```

## Scala

```scala
object Solution {
    def minimizeTheDifference(mat: Array[Array[Int]], target: Int): Int = {
        val maxSum = mat.map(_.max).sum
        var dp = new Array[Boolean](maxSum + 1)
        dp(0) = true

        for (row <- mat) {
            val next = new Array[Boolean](maxSum + 1)
            var s = 0
            while (s <= maxSum) {
                if (dp(s)) {
                    var i = 0
                    while (i < row.length) {
                        val ns = s + row(i)
                        if (ns <= maxSum) next(ns) = true
                        i += 1
                    }
                }
                s += 1
            }
            dp = next
        }

        var ans = Int.MaxValue
        var sum = 0
        while (sum <= maxSum) {
            if (dp(sum)) {
                val diff = math.abs(target - sum)
                if (diff < ans) ans = diff
            }
            sum += 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimize_the_difference(mat: Vec<Vec<i32>>, target: i32) -> i32 {
        let m = mat.len();
        let max_sum = m * 70; // maximum possible sum (since each element <= 70)
        let mut dp = vec![false; max_sum + 1];
        dp[0] = true;
        for row in mat.iter() {
            let mut next = vec![false; max_sum + 1];
            for (sum, &possible) in dp.iter().enumerate() {
                if possible {
                    for &val in row.iter() {
                        let new_sum = sum + val as usize;
                        if new_sum <= max_sum {
                            next[new_sum] = true;
                        }
                    }
                }
            }
            dp = next;
        }
        let mut ans = i32::MAX;
        for (sum, &possible) in dp.iter().enumerate() {
            if possible {
                let diff = (target - sum as i32).abs();
                if diff < ans {
                    ans = diff;
                }
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (minimize-the-difference mat target)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ((row-maxes (map (lambda (row) (apply max row)) mat))
         (sum-max   (apply + row-maxes)))
    (define dp (make-vector (+ sum-max 1) #f))
    (vector-set! dp 0 #t)
    (for ([row mat])
      (define new-dp (make-vector (+ sum-max 1) #f))
      (for ([s (in-range 0 (+ sum-max 1))] #:when (vector-ref dp s))
        (for ([val row])
          (let ((ns (+ s val)))
            (when (<= ns sum-max)
              (vector-set! new-dp ns #t)))))
      (set! dp new-dp))
    (let loop ((s 0) (best (+ target sum-max))) ; initial large diff
      (if (> s sum-max)
          best
          (if (vector-ref dp s)
              (let ((diff (abs (- s target))))
                (loop (+ s 1) (if (< diff best) diff best)))
              (loop (+ s 1) best))))))
```

## Erlang

```erlang
-module(solution).
-export([minimize_the_difference/2]).

-spec minimize_the_difference(Mat :: [[integer()]], Target :: integer()) -> integer().
minimize_the_difference(Mat, Target) ->
    MaxSum = length(Mat) * 70,
    Initial = #{0 => true},
    Reachable = lists:foldl(
        fun(Row, AccMap) ->
            Keys = maps:keys(AccMap),
            NewMap = lists:foldl(
                fun(Sum, M) ->
                    lists:foldl(
                        fun(Val, M2) ->
                            NewSum = Sum + Val,
                            if
                                NewSum =< MaxSum -> maps:put(NewSum, true, M2);
                                true -> M2
                            end
                        end,
                        M,
                        Row)
                end,
                #{},
                Keys),
            NewMap
        end,
        Initial,
        Mat),
    Sums = maps:keys(Reachable),
    lists:min([erlang:abs(Target - Sum) || Sum <- Sums]).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimize_the_difference(mat :: [[integer]], target :: integer) :: integer
  def minimize_the_difference(mat, target) do
    reachable =
      Enum.reduce(mat, MapSet.new([0]), fn row, acc ->
        Enum.reduce(row, MapSet.new(), fn v, set ->
          Enum.reduce(acc, set, fn s, st -> MapSet.put(st, s + v) end)
        end)
      end)

    reachable
    |> Enum.map(&abs(&1 - target))
    |> Enum.min()
  end
end
```
