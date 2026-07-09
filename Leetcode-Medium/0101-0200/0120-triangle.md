# 0120. Triangle

## Cpp

```cpp
class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        if (triangle.empty()) return 0;
        vector<int> dp = triangle.back();
        for (int i = (int)triangle.size() - 2; i >= 0; --i) {
            for (int j = 0; j <= i; ++j) {
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1]);
            }
        }
        return dp[0];
    }
};
```

## Java

```java
class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int n = triangle.size();
        // dp will hold the minimum path sums for the current row
        int[] dp = new int[n];
        // Initialize dp with the last row of the triangle
        List<Integer> lastRow = triangle.get(n - 1);
        for (int i = 0; i < n; i++) {
            dp[i] = lastRow.get(i);
        }
        // Iterate from the second-last row up to the top
        for (int row = n - 2; row >= 0; row--) {
            List<Integer> current = triangle.get(row);
            for (int col = 0; col <= row; col++) {
                dp[col] = Math.min(dp[col], dp[col + 1]) + current.get(col);
            }
        }
        return dp[0];
    }
}
```

## Python

```python
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        # Initialize dp with the last row of the triangle
        dp = triangle[-1][:]
        # Iterate from the second-last row up to the top
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        return dp[0]
```

## Python3

```python
from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        dp = triangle[-1][:]
        for row in range(len(triangle) - 2, -1, -1):
            for i in range(row + 1):
                dp[i] = triangle[row][i] + min(dp[i], dp[i + 1])
        return dp[0]
```

## C

```c
#include <stdlib.h>

int minimumTotal(int** triangle, int triangleSize, int* triangleColSize) {
    if (triangleSize == 0) return 0;
    int n = triangleColSize[triangleSize - 1];
    int *dp = (int *)malloc(sizeof(int) * n);
    for (int j = 0; j < n; ++j) dp[j] = triangle[triangleSize - 1][j];
    for (int i = triangleSize - 2; i >= 0; --i) {
        int cols = triangleColSize[i];
        for (int j = 0; j < cols; ++j) {
            int left = dp[j], right = dp[j + 1];
            dp[j] = triangle[i][j] + (left < right ? left : right);
        }
    }
    int ans = dp[0];
    free(dp);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MinimumTotal(IList<IList<int>> triangle) {
        if (triangle == null || triangle.Count == 0) return 0;
        int n = triangle.Count;
        // dp will hold the minimum path sums for the current row
        int[] dp = new int[n];
        // Initialize dp with the last row of the triangle
        IList<int> lastRow = triangle[n - 1];
        for (int i = 0; i < n; i++) {
            dp[i] = lastRow[i];
        }
        // Iterate from the second-last row up to the top
        for (int row = n - 2; row >= 0; row--) {
            IList<int> current = triangle[row];
            for (int col = 0; col <= row; col++) {
                dp[col] = current[col] + Math.Min(dp[col], dp[col + 1]);
            }
        }
        return dp[0];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} triangle
 * @return {number}
 */
var minimumTotal = function(triangle) {
    if (!triangle || triangle.length === 0) return 0;
    const n = triangle.length;
    // Initialize dp with the last row of the triangle
    let dp = triangle[n - 1].slice();
    
    // Iterate from the second-last row up to the top
    for (let i = n - 2; i >= 0; i--) {
        for (let j = 0; j <= i; j++) {
            dp[j] = triangle[i][j] + Math.min(dp[j], dp[j + 1]);
        }
    }
    
    return dp[0];
};
```

## Typescript

```typescript
function minimumTotal(triangle: number[][]): number {
    const n = triangle.length;
    let dp = triangle[n - 1].slice();
    for (let i = n - 2; i >= 0; i--) {
        for (let j = 0; j <= i; j++) {
            dp[j] = Math.min(dp[j], dp[j + 1]) + triangle[i][j];
        }
    }
    return dp[0];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $triangle
     * @return Integer
     */
    function minimumTotal($triangle) {
        $n = count($triangle);
        if ($n == 0) return 0;
        // Initialize dp with the last row of the triangle
        $dp = $triangle[$n - 1];
        // Bottom-up DP
        for ($i = $n - 2; $i >= 0; $i--) {
            for ($j = 0; $j <= $i; $j++) {
                $dp[$j] = $triangle[$i][$j] + min($dp[$j], $dp[$j + 1]);
            }
        }
        return $dp[0];
    }
}
```

## Swift

```swift
class Solution {
    func minimumTotal(_ triangle: [[Int]]) -> Int {
        var dp = triangle.last!
        for i in stride(from: triangle.count - 2, through: 0, by: -1) {
            let row = triangle[i]
            for j in 0..<row.count {
                dp[j] = min(dp[j], dp[j + 1]) + row[j]
            }
        }
        return dp[0]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumTotal(triangle: List<List<Int>>): Int {
        if (triangle.isEmpty()) return 0
        val dp = triangle.last().toMutableList()
        for (i in triangle.size - 2 downTo 0) {
            val row = triangle[i]
            for (j in 0 until row.size) {
                dp[j] = row[j] + kotlin.math.min(dp[j], dp[j + 1])
            }
        }
        return dp[0]
    }
}
```

## Dart

```dart
class Solution {
  int minimumTotal(List<List<int>> triangle) {
    int n = triangle.length;
    List<int> dp = List.from(triangle[n - 1]);
    for (int i = n - 2; i >= 0; i--) {
      for (int j = 0; j <= i; j++) {
        dp[j] = triangle[i][j] + (dp[j] < dp[j + 1] ? dp[j] : dp[j + 1]);
      }
    }
    return dp[0];
  }
}
```

## Golang

```go
func minimumTotal(triangle [][]int) int {
	n := len(triangle)
	if n == 0 {
		return 0
	}
	dp := make([]int, n)
	copy(dp, triangle[n-1])
	for i := n - 2; i >= 0; i-- {
		for j := 0; j <= i; j++ {
			if dp[j] < dp[j+1] {
				dp[j] = triangle[i][j] + dp[j]
			} else {
				dp[j] = triangle[i][j] + dp[j+1]
			}
		}
	}
	return dp[0]
}
```

## Ruby

```ruby
# @param {Integer[][]} triangle
# @return {Integer}
def minimum_total(triangle)
  return 0 if triangle.empty?
  dp = triangle[-1].dup
  (triangle.size - 2).downto(0) do |i|
    row = triangle[i]
    (0...row.size).each do |j|
      dp[j] = row[j] + (dp[j] < dp[j + 1] ? dp[j] : dp[j + 1])
    end
  end
  dp[0]
end
```

## Scala

```scala
object Solution {
    def minimumTotal(triangle: List[List[Int]]): Int = {
        val n = triangle.length
        if (n == 0) return 0
        val dp = new Array[Int](n)
        // Initialize dp with the last row of the triangle
        for (j <- 0 until n) {
            dp(j) = triangle(n - 1)(j)
        }
        // Bottom-up DP
        for (i <- (n - 2) to 0 by -1) {
            val row = triangle(i)
            for (j <- 0 to i) {
                dp(j) = row(j) + math.min(dp(j), dp(j + 1))
            }
        }
        dp(0)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_total(triangle: Vec<Vec<i32>>) -> i32 {
        let n = triangle.len();
        if n == 0 {
            return 0;
        }
        let mut dp = triangle[n - 1].clone();
        for row in (0..n - 1).rev() {
            for i in 0..=row {
                dp[i] = triangle[row][i] + std::cmp::min(dp[i], dp[i + 1]);
            }
        }
        dp[0]
    }
}
```

## Racket

```racket
(define/contract (minimum-total triangle)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((rev (reverse triangle))
         (dp0 (car rev))
         (result
          (foldl (lambda (row acc)
                   (for/list ([i (in-range (length row))])
                     (+ (list-ref row i)
                        (min (list-ref acc i) (list-ref acc (add1 i))))))
                 dp0
                 (cdr rev))))
    (car result)))
```

## Erlang

```erlang
-module(solution).
-export([minimum_total/1]).

-spec minimum_total(Triangle :: [[integer()]]) -> integer().
minimum_total(Triangle) ->
    case Triangle of
        [] -> 0;
        _ ->
            Rev = lists:reverse(Triangle),
            [Last|Rest] = Rev,
            DP = lists:foldl(fun(Row, Acc) ->
                    compute_row(Row, Acc)
                end, Last, Rest),
            hd(DP)
    end.

compute_row([], _) -> [];
compute_row([Val|RestRow], [B1,B2|RestBelow]) ->
    NewVal = Val + erlang:min(B1, B2),
    [NewVal | compute_row(RestRow, [B2|RestBelow])].
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_total(triangle :: [[integer]]) :: integer
  def minimum_total(triangle) do
    [last_row | rest_rev] = Enum.reverse(triangle)

    dp =
      Enum.reduce(rest_rev, last_row, fn row, acc ->
        Enum.map(Enum.with_index(row), fn {val, idx} ->
          val + min(Enum.at(acc, idx), Enum.at(acc, idx + 1))
        end)
      end)

    hd(dp)
  end
end
```
