# 0799. Champagne Tower

## Cpp

```cpp
class Solution {
public:
    double champagneTower(int poured, int query_row, int query_glass) {
        const int MAX_ROWS = 101;
        vector<vector<double>> dp(MAX_ROWS, vector<double>(MAX_ROWS, 0.0));
        dp[0][0] = poured;
        for (int r = 0; r < query_row; ++r) {
            for (int c = 0; c <= r; ++c) {
                if (dp[r][c] > 1.0) {
                    double excess = (dp[r][c] - 1.0) / 2.0;
                    dp[r + 1][c] += excess;
                    dp[r + 1][c + 1] += excess;
                }
            }
        }
        return min(1.0, dp[query_row][query_glass]);
    }
};
```

## Java

```java
class Solution {
    public double champagneTower(int poured, int query_row, int query_glass) {
        double[][] dp = new double[query_row + 2][query_row + 2];
        dp[0][0] = poured;
        for (int i = 0; i <= query_row; i++) {
            for (int j = 0; j <= i; j++) {
                if (dp[i][j] > 1.0) {
                    double excess = (dp[i][j] - 1.0) / 2.0;
                    dp[i + 1][j] += excess;
                    dp[i + 1][j + 1] += excess;
                }
            }
        }
        return Math.min(1.0, dp[query_row][query_glass]);
    }
}
```

## Python

```python
class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        # DP table for flow-through amounts
        dp = [[0.0] * (i + 1) for i in range(query_row + 2)]
        dp[0][0] = float(poured)
        for r in range(query_row + 1):
            for c in range(r + 1):
                if dp[r][c] > 1.0:
                    excess = (dp[r][c] - 1.0) / 2.0
                    dp[r + 1][c] += excess
                    dp[r + 1][c + 1] += excess
        return min(1.0, dp[query_row][query_glass])
```

## Python3

```python
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0.0] * (i + 1) for i in range(query_row + 2)]
        dp[0][0] = float(poured)
        for r in range(query_row + 1):
            for c in range(r + 1):
                excess = max(0.0, dp[r][c] - 1.0)
                if excess > 0:
                    dp[r + 1][c] += excess / 2.0
                    dp[r + 1][c + 1] += excess / 2.0
        return min(1.0, dp[query_row][query_glass])
```

## C

```c
#include <stddef.h>

double champagneTower(int poured, int query_row, int query_glass){
    double dp[101][101] = {{0}};
    dp[0][0] = (double)poured;
    for (int i = 0; i < query_row; ++i) {
        for (int j = 0; j <= i; ++j) {
            if (dp[i][j] > 1.0) {
                double excess = (dp[i][j] - 1.0) / 2.0;
                dp[i + 1][j] += excess;
                dp[i + 1][j + 1] += excess;
            }
        }
    }
    double res = dp[query_row][query_glass];
    return res > 1.0 ? 1.0 : res;
}
```

## Csharp

```csharp
public class Solution
{
    public double ChampagneTower(int poured, int query_row, int query_glass)
    {
        double[][] dp = new double[101][];
        for (int i = 0; i < dp.Length; i++)
            dp[i] = new double[i + 1];

        dp[0][0] = poured;

        for (int r = 0; r < query_row; r++)
        {
            for (int c = 0; c <= r; c++)
            {
                if (dp[r][c] > 1.0)
                {
                    double overflow = (dp[r][c] - 1.0) / 2.0;
                    dp[r + 1][c] += overflow;
                    dp[r + 1][c + 1] += overflow;
                }
            }
        }

        return Math.Min(1.0, dp[query_row][query_glass]);
    }
}
```

## Javascript

```javascript
/**
 * @param {number} poured
 * @param {number} query_row
 * @param {number} query_glass
 * @return {number}
 */
var champagneTower = function(poured, query_row, query_glass) {
    // Initialize DP table with zeros
    const dp = Array.from({ length: query_row + 2 }, (_, i) => new Float64Array(i + 1));
    dp[0][0] = poured;
    
    for (let r = 0; r <= query_row; ++r) {
        for (let c = 0; c <= r; ++c) {
            if (dp[r][c] > 1) {
                const overflow = (dp[r][c] - 1) / 2;
                dp[r + 1][c] += overflow;
                dp[r + 1][c + 1] += overflow;
                dp[r][c] = 1; // cap current glass, not strictly needed for answer
            }
        }
    }
    
    return Math.min(1, dp[query_row][query_glass]);
};
```

## Typescript

```typescript
function champagneTower(poured: number, query_row: number, query_glass: number): number {
    // dp[j] holds the amount of liquid that flows through glass (current row, j)
    let dp: number[] = new Array(query_row + 2).fill(0);
    dp[0] = poured;

    for (let row = 0; row < query_row; row++) {
        const next: number[] = new Array(query_row + 2).fill(0);
        for (let col = 0; col <= row; col++) {
            if (dp[col] > 1) {
                const excess = (dp[col] - 1) / 2;
                next[col] += excess;
                next[col + 1] += excess;
            }
        }
        dp = next;
    }

    return Math.min(1, dp[query_glass]);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $poured
     * @param Integer $query_row
     * @param Integer $query_glass
     * @return Float
     */
    function champagneTower($poured, $query_row, $query_glass) {
        // Initialize DP table up to query_row + 1 (extra row for overflow propagation)
        $dp = [];
        for ($i = 0; $i <= $query_row + 1; $i++) {
            $dp[$i] = array_fill(0, $i + 1, 0.0);
        }

        $dp[0][0] = (float)$poured;

        // Simulate the pouring process row by row
        for ($r = 0; $r <= $query_row; $r++) {
            for ($c = 0; $c <= $r; $c++) {
                if ($dp[$r][$c] > 1.0) {
                    $excess = ($dp[$r][$c] - 1.0) / 2.0;
                    $dp[$r + 1][$c]     += $excess;
                    $dp[$r + 1][$c + 1] += $excess;
                }
            }
        }

        // The amount in the target glass cannot exceed 1
        return min(1.0, $dp[$query_row][$query_glass]);
    }
}
```

## Swift

```swift
class Solution {
    func champagneTower(_ poured: Int, _ query_row: Int, _ query_glass: Int) -> Double {
        var dp = Array(repeating: Array(repeating: 0.0, count: query_row + 2), count: query_row + 2)
        dp[0][0] = Double(poured)
        for r in 0..<query_row {
            for c in 0...r {
                let amount = dp[r][c]
                if amount > 1.0 {
                    let excess = (amount - 1.0) / 2.0
                    dp[r + 1][c] += excess
                    dp[r + 1][c + 1] += excess
                }
            }
        }
        return min(1.0, dp[query_row][query_glass])
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun champagneTower(poured: Int, query_row: Int, query_glass: Int): Double {
        val dp = Array(101) { DoubleArray(101) }
        dp[0][0] = poured.toDouble()
        for (i in 0 until query_row) {
            for (j in 0..i) {
                if (dp[i][j] > 1.0) {
                    val overflow = (dp[i][j] - 1.0) / 2.0
                    dp[i + 1][j] += overflow
                    dp[i + 1][j + 1] += overflow
                }
            }
        }
        return kotlin.math.min(1.0, dp[query_row][query_glass])
    }
}
```

## Golang

```go
func champagneTower(poured int, query_row int, query_glass int) float64 {
	var dp [101][101]float64
	dp[0][0] = float64(poured)
	for r := 0; r < query_row; r++ {
		for c := 0; c <= r; c++ {
			excess := dp[r][c] - 1.0
			if excess > 0 {
				dp[r+1][c] += excess / 2.0
				dp[r+1][c+1] += excess / 2.0
			}
		}
	}
	if dp[query_row][query_glass] > 1.0 {
		return 1.0
	}
	return dp[query_row][query_glass]
}
```

## Ruby

```ruby
def champagne_tower(poured, query_row, query_glass)
  dp = Array.new(101) { Array.new(101, 0.0) }
  dp[0][0] = poured.to_f
  (0..query_row).each do |r|
    (0..r).each do |c|
      excess = (dp[r][c] - 1.0) / 2.0
      next if excess <= 0
      dp[r + 1][c] += excess
      dp[r + 1][c + 1] += excess
    end
  end
  [dp[query_row][query_glass], 1.0].min
end
```

## Scala

```scala
object Solution {
    def champagneTower(poured: Int, query_row: Int, query_glass: Int): Double = {
        val dp = Array.ofDim[Double](query_row + 2, query_row + 2)
        dp(0)(0) = poured.toDouble
        for (r <- 0 to query_row) {
            for (c <- 0 to r) {
                if (dp(r)(c) > 1.0) {
                    val excess = (dp(r)(c) - 1.0) / 2.0
                    dp(r + 1)(c) += excess
                    dp(r + 1)(c + 1) += excess
                }
            }
        }
        math.min(1.0, dp(query_row)(query_glass))
    }
}
```

## Rust

```rust
impl Solution {
    pub fn champagne_tower(poured: i32, query_row: i32, query_glass: i32) -> f64 {
        let n = query_row as usize;
        // Allocate enough space for row n+1 to avoid bounds checks when distributing excess
        let mut dp = vec![vec![0f64; n + 2]; n + 2];
        dp[0][0] = poured as f64;

        for r in 0..=n {
            for c in 0..=r {
                if dp[r][c] > 1.0 {
                    let excess = (dp[r][c] - 1.0) / 2.0;
                    dp[r + 1][c] += excess;
                    dp[r + 1][c + 1] += excess;
                }
            }
        }

        let ans = dp[n][query_glass as usize];
        if ans > 1.0 { 1.0 } else { ans }
    }
}
```
