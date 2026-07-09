# 1690. Stone Game VII

## Cpp

```cpp
class Solution {
public:
    int stoneGameVII(vector<int>& stones) {
        int n = stones.size();
        vector<long long> pref(n + 1, 0);
        for (int i = 0; i < n; ++i) pref[i + 1] = pref[i] + stones[i];
        auto rangeSum = [&](int l, int r) -> int {
            return static_cast<int>(pref[r + 1] - pref[l]);
        };
        vector<vector<int>> dp(n, vector<int>(n, 0));
        for (int len = 2; len <= n; ++len) {
            for (int l = 0; l + len - 1 < n; ++l) {
                int r = l + len - 1;
                int removeLeft = rangeSum(l + 1, r) - dp[l + 1][r];
                int removeRight = rangeSum(l, r - 1) - dp[l][r - 1];
                dp[l][r] = max(removeLeft, removeRight);
            }
        }
        return dp[0][n - 1];
    }
};
```

## Java

```java
class Solution {
    public int stoneGameVII(int[] stones) {
        int n = stones.length;
        int[] prefix = new int[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + stones[i];
        }
        int[][] dp = new int[n][n];
        for (int len = 2; len <= n; len++) {
            for (int i = 0; i + len - 1 < n; i++) {
                int j = i + len - 1;
                int removeLeft = (prefix[j + 1] - prefix[i + 1]) - dp[i + 1][j];
                int removeRight = (prefix[j] - prefix[i]) - dp[i][j - 1];
                dp[i][j] = Math.max(removeLeft, removeRight);
            }
        }
        return dp[0][n - 1];
    }
}
```

## Python

```python
class Solution(object):
    def stoneGameVII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        dp = [[0] * n for _ in range(n)]

        # length from 2 to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                total = prefix[j + 1] - prefix[i]
                remove_left = total - stones[i] - dp[i + 1][j]
                remove_right = total - stones[j] - dp[i][j - 1]
                dp[i][j] = max(remove_left, remove_right)

        return dp[0][n - 1]
```

## Python3

```python
from typing import List

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        def sub_sum(l: int, r: int) -> int:
            return prefix[r + 1] - prefix[l]

        dp = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                total = sub_sum(i, j)
                take_left = total - stones[i] - dp[i + 1][j]
                take_right = total - stones[j] - dp[i][j - 1]
                dp[i][j] = max(take_left, take_right)

        return dp[0][n - 1]
```

## C

```c
#include <stdlib.h>

int stoneGameVII(int* stones, int stonesSize) {
    int n = stonesSize;
    int *pref = (int *)malloc((n + 1) * sizeof(int));
    pref[0] = 0;
    for (int i = 0; i < n; ++i) {
        pref[i + 1] = pref[i] + stones[i];
    }

    int *dp = (int *)calloc(n * n, sizeof(int)); // dp[l*n + r]

    for (int len = 2; len <= n; ++len) {
        for (int l = 0; l + len - 1 < n; ++l) {
            int r = l + len - 1;
            int sumLR = pref[r + 1] - pref[l];
            int leftGain = sumLR - stones[l];
            int rightGain = sumLR - stones[r];

            int valLeft = leftGain - dp[(l + 1) * n + r];
            int valRight = rightGain - dp[l * n + (r - 1)];
            dp[l * n + r] = (valLeft > valRight) ? valLeft : valRight;
        }
    }

    int result = dp[n - 1]; // dp[0*n + (n-1)]
    free(pref);
    free(dp);
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int StoneGameVII(int[] stones) {
        int n = stones.Length;
        int[] prefix = new int[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + stones[i];
        }

        int[,] dp = new int[n, n];

        // dp[i][i] is already 0 by default
        for (int len = 2; len <= n; len++) {
            for (int i = 0; i + len - 1 < n; i++) {
                int j = i + len - 1;
                int total = prefix[j + 1] - prefix[i];
                int removeLeft = total - stones[i] - dp[i + 1, j];
                int removeRight = total - stones[j] - dp[i, j - 1];
                dp[i, j] = Math.Max(removeLeft, removeRight);
            }
        }

        return dp[0, n - 1];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} stones
 * @return {number}
 */
var stoneGameVII = function(stones) {
    const n = stones.length;
    const prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; ++i) {
        prefix[i + 1] = prefix[i] + stones[i];
    }
    const dp = Array.from({ length: n }, () => new Array(n).fill(0));
    for (let len = 2; len <= n; ++len) {
        for (let i = 0; i + len - 1 < n; ++i) {
            const j = i + len - 1;
            const sumLeft = prefix[j + 1] - prefix[i + 1]; // remove leftmost
            const sumRight = prefix[j] - prefix[i];       // remove rightmost
            dp[i][j] = Math.max(sumLeft - dp[i + 1][j], sumRight - dp[i][j - 1]);
        }
    }
    return dp[0][n - 1];
};
```

## Typescript

```typescript
function stoneGameVII(stones: number[]): number {
    const n = stones.length;
    const prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        prefix[i + 1] = prefix[i] + stones[i];
    }
    const rangeSum = (l: number, r: number): number => prefix[r + 1] - prefix[l];

    const dp: number[][] = Array.from({ length: n }, () => new Array(n).fill(0));

    for (let len = 2; len <= n; len++) {
        for (let l = 0; l + len - 1 < n; l++) {
            const r = l + len - 1;
            const removeLeftScore = rangeSum(l + 1, r) - dp[l + 1][r];
            const removeRightScore = rangeSum(l, r - 1) - dp[l][r - 1];
            dp[l][r] = Math.max(removeLeftScore, removeRightScore);
        }
    }

    return dp[0][n - 1];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $stones
     * @return Integer
     */
    function stoneGameVII($stones) {
        $n = count($stones);
        $prefix = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            $prefix[$i + 1] = $prefix[$i] + $stones[$i];
        }

        // dp[l][r] stores the maximum score difference the current player can achieve
        $dp = array_fill(0, $n, array_fill(0, $n, 0));

        for ($len = 2; $len <= $n; $len++) {
            for ($l = 0; $l + $len - 1 < $n; $l++) {
                $r = $l + $len - 1;
                // Remove left stone
                $sumLeft = $prefix[$r + 1] - $prefix[$l + 1];
                // Remove right stone
                $sumRight = $prefix[$r] - $prefix[$l];

                $dp[$l][$r] = max($sumLeft - $dp[$l + 1][$r], $sumRight - $dp[$l][$r - 1]);
            }
        }

        return $dp[0][$n - 1];
    }
}
```

## Swift

```swift
class Solution {
    func stoneGameVII(_ stones: [Int]) -> Int {
        let n = stones.count
        var prefix = [Int](repeating: 0, count: n + 1)
        for i in 0..<n {
            prefix[i + 1] = prefix[i] + stones[i]
        }
        func rangeSum(_ l: Int, _ r: Int) -> Int {
            return prefix[r + 1] - prefix[l]
        }
        var dp = Array(repeating: Array(repeating: 0, count: n), count: n)
        if n == 0 { return 0 }
        for len in 2...n {
            for i in 0...(n - len) {
                let j = i + len - 1
                let sumLeft = rangeSum(i + 1, j)
                let diffLeft = sumLeft - dp[i + 1][j]
                let sumRight = rangeSum(i, j - 1)
                let diffRight = sumRight - dp[i][j - 1]
                dp[i][j] = max(diffLeft, diffRight)
            }
        }
        return dp[0][n - 1]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun stoneGameVII(stones: IntArray): Int {
        val n = stones.size
        val prefix = LongArray(n + 1)
        for (i in 0 until n) {
            prefix[i + 1] = prefix[i] + stones[i]
        }
        fun rangeSum(l: Int, r: Int): Long = prefix[r + 1] - prefix[l]

        val dp = Array(n) { LongArray(n) }
        for (len in 2..n) {
            for (l in 0..n - len) {
                val r = l + len - 1
                val gainLeft = rangeSum(l + 1, r)
                val gainRight = rangeSum(l, r - 1)
                val diffLeft = gainLeft - dp[l + 1][r]
                val diffRight = gainRight - dp[l][r - 1]
                dp[l][r] = if (diffLeft > diffRight) diffLeft else diffRight
            }
        }
        return dp[0][n - 1].toInt()
    }
}
```

## Golang

```go
func stoneGameVII(stones []int) int {
	n := len(stones)
	if n == 0 {
		return 0
	}
	prefix := make([]int, n+1)
	for i, v := range stones {
		prefix[i+1] = prefix[i] + v
	}
	sum := func(i, j int) int { // inclusive indices
		return prefix[j+1] - prefix[i]
	}

	dp := make([][]int, n)
	for i := 0; i < n; i++ {
		dp[i] = make([]int, n)
	}

	for length := 2; length <= n; length++ {
		for i := 0; i+length-1 < n; i++ {
			j := i + length - 1
			total := sum(i, j)

			// remove left stone
			leftScore := total - stones[i] // sum of remaining stones after removing left
			diffLeft := leftScore - dp[i+1][j]

			// remove right stone
			rightScore := total - stones[j] // sum of remaining stones after removing right
			diffRight := rightScore - dp[i][j-1]

			if diffLeft > diffRight {
				dp[i][j] = diffLeft
			} else {
				dp[i][j] = diffRight
			}
		}
	}
	return dp[0][n-1]
}
```

## Ruby

```ruby
def stone_game_vii(stones)
  n = stones.length
  prefix = Array.new(n + 1, 0)
  (0...n).each { |i| prefix[i + 1] = prefix[i] + stones[i] }

  dp = Array.new(n) { Array.new(n, 0) }

  (2..n).each do |len|
    (0..n - len).each do |l|
      r = l + len - 1
      total = prefix[r + 1] - prefix[l]

      left_gain = total - stones[l]
      option_left = left_gain - dp[l + 1][r]

      right_gain = total - stones[r]
      option_right = right_gain - dp[l][r - 1]

      dp[l][r] = option_left > option_right ? option_left : option_right
    end
  end

  dp[0][n - 1]
end
```

## Scala

```scala
object Solution {
    def stoneGameVII(stones: Array[Int]): Int = {
        val n = stones.length
        val prefix = new Array[Int](n + 1)
        var i = 0
        while (i < n) {
            prefix(i + 1) = prefix(i) + stones(i)
            i += 1
        }
        def sum(l: Int, r: Int): Int = prefix(r + 1) - prefix(l)

        val dp = Array.ofDim[Int](n, n) // default 0, dp[l][l] = 0

        var len = 2
        while (len <= n) {
            var l = 0
            while (l + len - 1 < n) {
                val r = l + len - 1
                val total = sum(l, r)
                val leftGain = total - stones(l)
                val rightGain = total - stones(r)
                val best = Math.max(leftGain - dp(l + 1)(r), rightGain - dp(l)(r - 1))
                dp(l)(r) = best
                l += 1
            }
            len += 1
        }

        dp(0)(n - 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn stone_game_vii(stones: Vec<i32>) -> i32 {
        let n = stones.len();
        // prefix sums
        let mut pref = vec![0i32; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + stones[i];
        }

        // dp[l][r]: max difference current player can achieve on subarray [l, r]
        let mut dp = vec![vec![0i32; n]; n];

        // length from 2 to n
        for len in 2..=n {
            for l in 0..=n - len {
                let r = l + len - 1;
                // remove left stone
                let sum_left = pref[r + 1] - pref[l + 1]; // sum of stones[l+1..=r]
                let left_gain = sum_left - dp[l + 1][r];
                // remove right stone
                let sum_right = pref[r] - pref[l]; // sum of stones[l..=r-1]
                let right_gain = sum_right - dp[l][r - 1];
                dp[l][r] = if left_gain > right_gain { left_gain } else { right_gain };
            }
        }

        dp[0][n - 1]
    }
}
```
