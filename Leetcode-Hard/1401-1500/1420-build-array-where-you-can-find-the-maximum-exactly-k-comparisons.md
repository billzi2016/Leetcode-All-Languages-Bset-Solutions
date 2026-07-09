# 1420. Build Array Where You Can Find The Maximum Exactly K Comparisons

## Cpp

```cpp
class Solution {
public:
    int numOfArrays(int n, int m, int k) {
        const int MOD = 1000000007;
        // dp[i][j][c]: length i, current max j, exactly c comparisons
        vector<vector<vector<int>>> dp(n + 1,
            vector<vector<int>>(m + 1, vector<int>(k + 1, 0)));
        for (int j = 1; j <= m; ++j) {
            if (k >= 1) dp[1][j][1] = 1;
        }
        for (int i = 2; i <= n; ++i) {
            for (int c = 1; c <= k; ++c) {
                long long prefix = 0; // sum of dp[i-1][p][c-1] for p < j
                for (int j = 1; j <= m; ++j) {
                    long long stay = (long long)dp[i - 1][j][c] * j % MOD;
                    long long inc = prefix; // transition from smaller max to j
                    dp[i][j][c] = (stay + inc) % MOD;
                    // update prefix for next j
                    prefix += dp[i - 1][j][c - 1];
                    if (prefix >= MOD) prefix -= MOD;
                }
            }
        }
        long long ans = 0;
        for (int j = 1; j <= m; ++j) {
            ans += dp[n][j][k];
            if (ans >= MOD) ans -= MOD;
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int numOfArrays(int n, int m, int k) {
        final int MOD = 1_000_000_007;
        long[][][] dp = new long[n + 1][m + 1][k + 2];
        if (k == 0) return 0;
        for (int v = 1; v <= m; v++) {
            dp[1][v][1] = 1;
        }
        for (int i = 1; i < n; i++) {
            for (int curMax = 1; curMax <= m; curMax++) {
                for (int cost = 1; cost <= k; cost++) {
                    long ways = dp[i][curMax][cost];
                    if (ways == 0) continue;
                    // keep current maximum
                    dp[i + 1][curMax][cost] = (dp[i + 1][curMax][cost] + ways * curMax) % MOD;
                    // increase maximum to a larger value
                    if (cost + 1 <= k) {
                        for (int newMax = curMax + 1; newMax <= m; newMax++) {
                            dp[i + 1][newMax][cost + 1] = (dp[i + 1][newMax][cost + 1] + ways) % MOD;
                        }
                    }
                }
            }
        }
        long ans = 0;
        for (int maxVal = 1; maxVal <= m; maxVal++) {
            ans = (ans + dp[n][maxVal][k]) % MOD;
        }
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def numOfArrays(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        if k == 0 or k > n:
            return 0
        # dp[i][c][v] = ways for length i, exactly c comparisons, current max = v
        dp = [[[0] * (m + 1) for _ in range(k + 2)] for __ in range(n + 1)]
        for v in range(1, m + 1):
            dp[1][1][v] = 1  # first element sets max to v, one comparison
        for i in range(2, n + 1):
            max_c = min(i, k)
            for c in range(1, max_c + 1):
                # prefix sums of dp[i-1][c-1][*] for quick sum of prev < v
                pref = [0] * (m + 2)
                cur = 0
                for v in range(1, m + 1):
                    cur = (cur + dp[i - 1][c - 1][v]) % MOD
                    pref[v] = cur
                for v in range(1, m + 1):
                    stay = dp[i - 1][c][v] * v % MOD          # choose any value <= current max v
                    inc = pref[v - 1]                         # increase to new max v from smaller previous max
                    dp[i][c][v] = (stay + inc) % MOD
        ans = sum(dp[n][k][v] for v in range(1, m + 1)) % MOD
        return ans
```

## Python3

```python
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        if n == 1:
            return m % MOD if k == 0 else 0

        cur = [[0] * (k + 1) for _ in range(m + 1)]
        nxt = [[0] * (k + 1) for _ in range(m + 1)]

        for v in range(1, m + 1):
            cur[v][0] = 1

        for _ in range(1, n):
            # reset nxt
            for i in range(1, m + 1):
                row = nxt[i]
                for j in range(k + 1):
                    row[j] = 0

            # keep the same maximum
            for max_val in range(1, m + 1):
                cur_row = cur[max_val]
                nxt_row = nxt[max_val]
                mul = max_val
                for comp in range(k + 1):
                    val = cur_row[comp]
                    if val:
                        nxt_row[comp] = (nxt_row[comp] + val * mul) % MOD

            # increase maximum (new comparison)
            for comp in range(k):
                pref = 0
                for new_max in range(1, m + 1):
                    nxt[new_max][comp + 1] = (nxt[new_max][comp + 1] + pref) % MOD
                    pref = (pref + cur[new_max][comp]) % MOD

            cur, nxt = nxt, cur

        ans = 0
        for max_val in range(1, m + 1):
            ans = (ans + cur[max_val][k]) % MOD
        return ans
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numOfArrays(int n, int m, int k) {
        if (k == 0 || k > n) return 0;
        const int MOD = 1000000007;
        vector<vector<vector<int>>> dp(n + 1,
            vector<vector<int>>(m + 1, vector<int>(k + 1, 0)));
        for (int j = 1; j <= m; ++j) dp[1][j][1] = 1;
        for (int i = 2; i <= n; ++i) {
            for (int c = 1; c <= k; ++c) {
                vector<int> pref(m + 1, 0);
                for (int p = 1; p <= m; ++p) {
                    pref[p] = (pref[p - 1] + dp[i - 1][p][c - 1]) % MOD;
                }
                for (int j = 1; j <= m; ++j) {
                    long long val = (long long)dp[i - 1][j][c] * j % MOD;
                    int sumLess = pref[j - 1];
                    val = (val + sumLess) % MOD;
                    dp[i][j][c] = (int)val;
                }
            }
        }
        long long ans = 0;
        for (int j = 1; j <= m; ++j) {
            ans += dp[n][j][k];
            if (ans >= MOD) ans -= MOD;
        }
        return (int)ans;
    }
};
```

## Csharp

```csharp
using System;

public class Solution {
    private const int MOD = 1000000007;
    public int NumOfArrays(int n, int m, int k) {
        // dp[i, maxVal, comps] = number of ways for first i elements,
        // current maximum is maxVal, and exactly comps comparisons have been made.
        int[,,] dp = new int[n + 1, m + 1, k + 1];

        // Initialize first element: any value v (1..m) sets max=v with 0 comparisons.
        for (int v = 1; v <= m; v++) {
            dp[1, v, 0] = 1;
        }

        for (int i = 1; i < n; i++) {
            for (int maxVal = 1; maxVal <= m; maxVal++) {
                for (int comp = 0; comp <= k; comp++) {
                    int cur = dp[i, maxVal, comp];
                    if (cur == 0) continue;

                    // Choose a value <= current max: stays same max, same comparisons.
                    long addSame = (long)cur * maxVal % MOD;
                    dp[i + 1, maxVal, comp] = (int)((dp[i + 1, maxVal, comp] + addSame) % MOD);

                    // Choose a value > current max: each possible new max v gets one way,
                    // comparisons increase by 1.
                    if (comp + 1 <= k) {
                        for (int newMax = maxVal + 1; newMax <= m; newMax++) {
                            dp[i + 1, newMax, comp + 1] += cur;
                            if (dp[i + 1, newMax, comp + 1] >= MOD)
                                dp[i + 1, newMax, comp + 1] -= MOD;
                        }
                    }
                }
            }
        }

        int result = 0;
        for (int maxVal = 1; maxVal <= m; maxVal++) {
            result += dp[n, maxVal, k];
            if (result >= MOD) result -= MOD;
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} m
 * @param {number} k
 * @return {number}
 */
var numOfArrays = function(n, m, k) {
    const MOD = 1000000007;
    // dp[max][cost] for current length
    let dp = Array.from({length: m + 1}, () => new Array(k + 1).fill(0));
    // initialize first element
    if (k >= 1) {
        for (let max = 1; max <= m; ++max) {
            dp[max][1] = 1;
        }
    }
    for (let len = 2; len <= n; ++len) {
        const ndp = Array.from({length: m + 1}, () => new Array(k + 1).fill(0));
        for (let curMax = 1; curMax <= m; ++curMax) {
            for (let cost = 1; cost <= k; ++cost) {
                const ways = dp[curMax][cost];
                if (!ways) continue;
                // choose a value <= curMax, max stays the same
                ndp[curMax][cost] = (ndp[curMax][cost] + ways * curMax) % MOD;
                // choose a value > curMax, max increases, cost+1
                if (cost + 1 <= k) {
                    const add = ways; // each specific new value contributes one way
                    for (let newMax = curMax + 1; newMax <= m; ++newMax) {
                        ndp[newMax][cost + 1] = (ndp[newMax][cost + 1] + add) % MOD;
                    }
                }
            }
        }
        dp = ndp;
    }
    let ans = 0;
    for (let max = 1; max <= m; ++max) {
        ans = (ans + dp[max][k]) % MOD;
    }
    return ans;
};
```

## Typescript

```typescript
function numOfArrays(n: number, m: number, k: number): number {
    const MOD = 1000000007;
    if (k === 0) return 0; // impossible for n > 0
    // dp[i][c][mx] : first i elements, exactly c search costs, current max = mx
    const dp: number[][][] = Array.from({ length: n + 1 }, () =>
        Array.from({ length: k + 1 }, () => new Array(m + 1).fill(0))
    );

    for (let v = 1; v <= m; ++v) {
        dp[1][1][v] = 1;
    }

    for (let i = 1; i < n; ++i) {
        for (let c = 1; c <= k; ++c) {
            for (let mx = 1; mx <= m; ++mx) {
                const cur = dp[i][c][mx];
                if (!cur) continue;
                // choose a value ≤ current max, cost unchanged
                dp[i + 1][c][mx] = (dp[i + 1][c][mx] + cur * mx) % MOD;

                // choose a value > current max, cost increases by 1
                if (c + 1 <= k) {
                    const add = cur;
                    for (let newMx = mx + 1; newMx <= m; ++newMx) {
                        dp[i + 1][c + 1][newMx] = (dp[i + 1][c + 1][newMx] + add) % MOD;
                    }
                }
            }
        }
    }

    let ans = 0;
    for (let mx = 1; mx <= m; ++mx) {
        ans = (ans + dp[n][k][mx]) % MOD;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $m
     * @param Integer $k
     * @return Integer
     */
    function numOfArrays($n, $m, $k) {
        $MOD = 1000000007;
        // dp[i][j][v]: first i elements, cost j, current max v
        $dp = array_fill(0, $n + 1, null);
        for ($i = 0; $i <= $n; $i++) {
            $dp[$i] = array_fill(0, $k + 2, null);
            for ($j = 0; $j <= $k; $j++) {
                $dp[$i][$j] = array_fill(0, $m + 1, 0);
            }
        }

        // base case: first element sets max and costs 1
        for ($v = 1; $v <= $m; $v++) {
            $dp[1][1][$v] = 1;
        }

        for ($i = 1; $i < $n; $i++) {
            for ($j = 1; $j <= $k; $j++) {
                for ($v = 1; $v <= $m; $v++) {
                    $cur = $dp[$i][$j][$v];
                    if ($cur == 0) continue;

                    // choose next element <= current max (cost unchanged)
                    $add = ($cur * $v) % $MOD;
                    $dp[$i + 1][$j][$v] = ($dp[$i + 1][$j][$v] + $add) % $MOD;

                    // choose next element > current max (cost increases by 1)
                    if ($j + 1 <= $k) {
                        for ($w = $v + 1; $w <= $m; $w++) {
                            $dp[$i + 1][$j + 1][$w] = ($dp[$i + 1][$j + 1][$w] + $cur) % $MOD;
                        }
                    }
                }
            }
        }

        $ans = 0;
        for ($v = 1; $v <= $m; $v++) {
            $ans = ($ans + $dp[$n][$k][$v]) % $MOD;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func numOfArrays(_ n: Int, _ m: Int, _ k: Int) -> Int {
        let MOD = 1_000_000_007
        if k > n { return 0 }
        var prev = Array(repeating: Array(repeating: 0, count: k + 1), count: m + 1)
        for maxVal in 1...m {
            prev[maxVal][0] = 1
        }
        if n == 1 {
            return k == 0 ? (m % MOD) : 0
        }
        for _ in 2...n {
            var curr = Array(repeating: Array(repeating: 0, count: k + 1), count: m + 1)
            for comp in 0...k {
                var prefix = Array(repeating: 0, count: m + 1) // prefix[0] = 0
                for maxVal in 1...m {
                    let val = prev[maxVal][comp]
                    if val != 0 {
                        let addSame = (Int64(val) * Int64(maxVal)) % Int64(MOD)
                        curr[maxVal][comp] = (curr[maxVal][comp] + Int(addSame)) % MOD
                    }
                    prefix[maxVal] = (prefix[maxVal - 1] + val) % MOD
                }
                if comp + 1 <= k {
                    for newMax in 2...m {
                        let inc = prefix[newMax - 1]
                        if inc != 0 {
                            curr[newMax][comp + 1] = (curr[newMax][comp + 1] + inc) % MOD
                        }
                    }
                }
            }
            prev = curr
        }
        var ans = 0
        for maxVal in 1...m {
            ans = (ans + prev[maxVal][k]) % MOD
        }
        return ans
    }
}
```

## Kotlin

```kotlin
import java.util.*

class Solution {
    private val MOD = 1_000_000_007L

    fun numOfArrays(n: Int, m: Int, k: Int): Int {
        // dp[i][maxVal][cost]
        val dp = Array(n + 1) { Array(m + 1) { LongArray(k + 1) } }
        dp[0][0][0] = 1L

        for (i in 0 until n) {
            for (maxVal in 0..m) {
                for (cost in 0..k) {
                    val cur = dp[i][maxVal][cost]
                    if (cur == 0L) continue
                    // Choose a value <= current max, cost unchanged
                    if (maxVal > 0) {
                        val add = (cur * maxVal) % MOD
                        dp[i + 1][maxVal][cost] = (dp[i + 1][maxVal][cost] + add) % MOD
                    }
                    // Choose a value that becomes new maximum, cost+1
                    if (cost + 1 <= k) {
                        for (newMax in maxVal + 1..m) {
                            dp[i + 1][newMax][cost + 1] = (dp[i + 1][newMax][cost + 1] + cur) % MOD
                        }
                    }
                }
            }
        }

        var ans = 0L
        for (maxVal in 1..m) {
            ans = (ans + dp[n][maxVal][k]) % MOD
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _MOD = 1000000007;

  int numOfArrays(int n, int m, int k) {
    // dp[i][j][c]: number of ways for first i elements,
    // current maximum is j, and exactly c comparisons (new maxima) have been made.
    List<List<List<int>>> dp = List.generate(
        n + 1, (_) => List.generate(m + 1, (_) => List.filled(k + 2, 0)));

    // Initialize first element: it sets the max and costs 1 comparison.
    for (int j = 1; j <= m; ++j) {
      dp[1][j][1] = 1;
    }

    for (int i = 1; i < n; ++i) {
      for (int c = 1; c <= k; ++c) {
        // Prefix sums of dp[i][*][c] to handle transitions where max increases.
        List<int> pref = List.filled(m + 1, 0);
        for (int j = 1; j <= m; ++j) {
          pref[j] = (pref[j - 1] + dp[i][j][c]) % _MOD;
        }

        for (int newMax = 1; newMax <= m; ++newMax) {
          int curVal = dp[i][newMax][c];
          if (curVal != 0) {
            // Next element ≤ current max: stays same max, choose any of 'newMax' values.
            dp[i + 1][newMax][c] =
                (dp[i + 1][newMax][c] + (curVal * newMax) % _MOD) % _MOD;
          }
          if (c + 1 <= k) {
            // Next element > current max: becomes new maximum.
            int inc = pref[newMax - 1]; // sum of dp[i][j][c] for j < newMax
            if (inc != 0) {
              dp[i + 1][newMax][c + 1] =
                  (dp[i + 1][newMax][c + 1] + inc) % _MOD;
            }
          }
        }
      }
    }

    int ans = 0;
    for (int j = 1; j <= m; ++j) {
      ans = (ans + dp[n][j][k]) % _MOD;
    }
    return ans;
  }
}
```

## Golang

```go
package main

import (
	"math"
)

const MOD int64 = 1000000007

func numOfArrays(n int, m int, k int) int {
	if k == 0 {
		return 0
	}
	// dpPrev[max][cost]
	dpPrev := make([][]int64, m+1)
	for i := 0; i <= m; i++ {
		dpPrev[i] = make([]int64, k+1)
	}
	// base: first element sets max and costs 1
	if k >= 1 {
		for v := 1; v <= m; v++ {
			dpPrev[v][1] = 1
		}
	}

	for i := 2; i <= n; i++ {
		dpCurr := make([][]int64, m+1)
		for idx := 0; idx <= m; idx++ {
			dpCurr[idx] = make([]int64, k+1)
		}
		for cost := 1; cost <= k; cost++ {
			// prefix sums of dpPrev[*][cost-1]
			pref := make([]int64, m+1)
			var sum int64 = 0
			if cost > 1 { // when cost==1, dpPrev[*][0] are all zero
				for j := 1; j <= m; j++ {
					sum += dpPrev[j][cost-1]
					if sum >= MOD {
						sum -= MOD
					}
					pref[j] = sum
				}
			}
			for maxVal := 1; maxVal <= m; maxVal++ {
				// stay with same max
				val := dpPrev[maxVal][cost] * int64(maxVal) % MOD
				// become new max maxVal from a smaller previous max
				if cost > 1 && maxVal > 1 {
					val += pref[maxVal-1]
					if val >= MOD {
						val -= MOD
					}
				}
				dpCurr[maxVal][cost] = val
			}
		}
		dpPrev = dpCurr
	}

	var ans int64 = 0
	for v := 1; v <= m; v++ {
		ans += dpPrev[v][k]
		if ans >= MOD {
			ans -= MOD
		}
	}
	return int(ans)
}

// The following is only to avoid "imported and not used" error in some environments.
var _ = math.MaxInt64
```

## Ruby

```ruby
def num_of_arrays(n, m, k)
  mod = 1_000_000_007
  return 0 if k == 0 && n > 0
  return 0 if k > n

  dp = Array.new(n + 1) { Array.new(k + 1) { Array.new(m + 1, 0) } }

  if n >= 1 && k >= 1
    (1..m).each { |x| dp[1][1][x] = 1 }
  end

  (2..n).each do |i|
    (1..k).each do |j|
      prefix = Array.new(m + 1, 0)
      sum = 0
      (1..m).each do |x|
        sum += dp[i - 1][j - 1][x]
        sum -= mod if sum >= mod
        prefix[x] = sum
      end

      (1..m).each do |x|
        same = (dp[i - 1][j][x] * x) % mod
        new_max = prefix[x - 1]
        dp[i][j][x] = (same + new_max) % mod
      end
    end
  end

  ans = 0
  (1..m).each do |x|
    ans += dp[n][k][x]
    ans -= mod if ans >= mod
  end
  ans % mod
end
```

## Scala

```scala
object Solution {
    def numOfArrays(n: Int, m: Int, k: Int): Int = {
        val MOD = 1000000007L
        if (k == 0) return 0
        val dp = Array.ofDim[Long](n + 1, m + 1, k + 1)
        for (v <- 1 to m) {
            if (k >= 1) dp(1)(v)(1) = 1L
        }
        for (i <- 2 to n) {
            for (c <- 1 to k) {
                var prefix = 0L
                for (v <- 1 to m) {
                    // keep the same maximum
                    val same = (dp(i - 1)(v)(c) * v) % MOD
                    dp(i)(v)(c) = (dp(i)(v)(c) + same) % MOD
                    // increase cost by introducing a new maximum
                    dp(i)(v)(c) = (dp(i)(v)(c) + prefix) % MOD
                    // update prefix sum for next v
                    prefix = (prefix + dp(i - 1)(v)(c - 1)) % MOD
                }
            }
        }
        var ans = 0L
        for (v <- 1 to m) {
            ans = (ans + dp(n)(v)(k)) % MOD
        }
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_of_arrays(n: i32, m: i32, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = n as usize;
        let m = m as usize;
        let k = k as usize;

        // dp[pos][cost][max] = number of ways
        let mut dp = vec![vec![vec![0i64; m + 1]; k + 1]; n + 1];
        dp[0][0][0] = 1;

        for pos in 0..n {
            for cost in 0..=k {
                for maxv in 0..=m {
                    let cur = dp[pos][cost][maxv];
                    if cur == 0 {
                        continue;
                    }
                    // Choose a value <= current max
                    if maxv > 0 {
                        let add = (cur * maxv as i64) % MOD;
                        dp[pos + 1][cost][maxv] =
                            (dp[pos + 1][cost][maxv] + add) % MOD;
                    }
                    // Choose a value > current max, which increases cost
                    if cost + 1 <= k && maxv < m {
                        for new_max in (maxv + 1)..=m {
                            dp[pos + 1][cost + 1][new_max] =
                                (dp[pos + 1][cost + 1][new_max] + cur) % MOD;
                        }
                    }
                }
            }
        }

        let mut ans: i64 = 0;
        for maxv in 1..=m {
            ans = (ans + dp[n][k][maxv]) % MOD;
        }
        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (num-of-arrays n m k)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  (if (= k 0)
      0
      (let ((dp-prev (make-vector (+ m 1) #f)))
        ;; initialise dpPrev rows
        (do ([i 0 (+ i 1)])
            ((> i m))
          (vector-set! dp-prev i (make-vector (+ k 1) 0)))
        ;; base case: length 1, each value creates one comparison
        (when (>= k 1)
          (do ([v 1 (+ v 1)])
              ((> v m))
            (vector-set! (vector-ref dp-prev v) 1 1)))
        ;; build for lengths 2..n
        (do ([len 2 (+ len 1)])
            ((> len n))
          (let ((dp-curr (make-vector (+ m 1) #f)))
            (do ([i 0 (+ i 1)])
                ((> i m))
              (vector-set! dp-curr i (make-vector (+ k 1) 0)))
            (do ([curMax 1 (+ curMax 1)])
                ((> curMax m))
              (let ((row-prev (vector-ref dp-prev curMax)))
                (do ([cost 1 (+ cost 1)])
                    ((> cost k))
                  (define val (vector-ref row-prev cost))
                  (when (> val 0)
                    ;; keep same maximum
                    (let* ((add (modulo (* val curMax) MOD))
                           (old (vector-ref (vector-ref dp-curr curMax) cost))
                           (new (modulo (+ old add) MOD)))
                      (vector-set! (vector-ref dp-curr curMax) cost new))
                    ;; increase to a larger maximum
                    (when (< cost k)
                      (do ([newMax (+ curMax 1) (+ newMax 1)])
                          ((> newMax m))
                        (let* ((old2 (vector-ref (vector-ref dp-curr newMax) (+ cost 1)))
                               (new2 (modulo (+ old2 val) MOD)))
                          (vector-set! (vector-ref dp-curr newMax) (+ cost 1) new2)))))))))
            (set! dp-prev dp-curr)))
        ;; sum over all possible final maximums
        (let ((ans 0))
          (do ([maxv 1 (+ maxv 1)])
              ((> maxv m))
            (set! ans (modulo (+ ans (vector-ref (vector-ref dp-prev maxv) k)) MOD)))
          ans))))
```

## Erlang

```erlang
-module(solution).
-export([num_of_arrays/3]).

-define(MOD, 1000000007).

-spec num_of_arrays(N :: integer(), M :: integer(), K :: integer()) -> integer().
num_of_arrays(N, M, K) ->
    InitList = lists:duplicate(K + 1, 0),
    InitTuple0 = list_to_tuple(InitList),
    Prev0 = setelement(1, InitTuple0, 1), % dp[0][0] = 1
    Final = loop(1, N, M, K, Prev0),
    element(K + 1, Final) rem ?MOD.

loop(I, N, _M, _K, Prev) when I > N ->
    Prev;
loop(I, N, M, K, Prev) ->
    MaxJ = erlang:min(I, K),
    CurVals = [calc(J, MaxJ, M, Prev) || J <- lists:seq(0, K)],
    CurTuple = list_to_tuple(CurVals),
    loop(I + 1, N, M, K, CurTuple).

calc(0, _MaxJ, _M, _Prev) ->
    0;
calc(J, MaxJ, _M, _Prev) when J > MaxJ ->
    0;
calc(J, _MaxJ, M, Prev) ->
    PrevJ = element(J + 1, Prev),
    PrevJMinus1 = element(J, Prev),
    Part1 = (PrevJ * J) rem ?MOD,
    Part2 = (PrevJMinus1 * (M - J + 1)) rem ?MOD,
    (Part1 + Part2) rem ?MOD.
```

## Elixir

```elixir
defmodule Solution do
  @mod 1_000_000_007

  @spec num_of_arrays(n :: integer, m :: integer, k :: integer) :: integer
  def num_of_arrays(n, m, k) do
    cond do
      k == 0 -> 0
      n == 0 -> 0
      true ->
        # initialize dp for i = 1
        dp_prev =
          Enum.reduce(0..m, :array.new(m + 1, default: nil), fn idx, acc ->
            inner =
              if idx == 0 do
                :array.new(k + 1, default: 0)
              else
                arr = :array.new(k + 1, default: 0)
                :array.set(1, 1, arr)
              end

            :array.set(idx, inner, acc)
          end)

        dp_prev =
          if n == 1 do
            dp_prev
          else
            Enum.reduce(2..n, dp_prev, fn _i, dp_prev_acc ->
              # create empty dp_curr
              dp_curr =
                Enum.reduce(0..m, :array.new(m + 1, default: nil), fn idx, acc ->
                  :array.set(idx, :array.new(k + 1, default: 0), acc)
                end)

              # stay with same maximum
              dp_curr =
                Enum.reduce(1..m, dp_curr, fn j, cur_acc ->
                  row_prev = :array.get(j, dp_prev_acc)

                  Enum.reduce(1..k, cur_acc, fn c, inner_acc ->
                    val = :array.get(c, row_prev)

                    if val != 0 do
                      add = rem(val * j, @mod)
                      row_curr = :array.get(j, inner_acc)
                      old = :array.get(c, row_curr)
                      new_row = :array.set(c, rem(old + add, @mod), row_curr)
                      :array.set(j, new_row, inner_acc)
                    else
                      inner_acc
                    end
                  end)
                end)

              # transition to a larger maximum using prefix sums
              dp_curr =
                Enum.reduce(1..(k - 1), dp_curr, fn c, cur_acc ->
                  pref = 0

                  Enum.reduce(1..m, {cur_acc, pref}, fn new_max, {acc_mat, pref_sum} ->
                    # add prefix sum to dp_curr[new_max][c+1]
                    acc_mat =
                      if pref_sum != 0 do
                        row_curr = :array.get(new_max, acc_mat)
                        old = :array.get(c + 1, row_curr)
                        new_row = :array.set(c + 1, rem(old + pref_sum, @mod), row_curr)
                        :array.set(new_max, new_row, acc_mat)
                      else
                        acc_mat
                      end

                    # update prefix sum with dp_prev[new_max][c]
                    row_prev = :array.get(new_max, dp_prev_acc)
                    val_prev = :array.get(c, row_prev)
                    new_pref = rem(pref_sum + val_prev, @mod)

                    {acc_mat, new_pref}
                  end)
                  |> elem(0)
                end)

              dp_curr
            end)
          end

        # sum over all possible maximum values for exact k comparisons
        Enum.reduce(1..m, 0, fn j, acc ->
          row = :array.get(j, dp_prev)
          val = :array.get(k, row)
          rem(acc + val, @mod)
        end)
    end
  end
end
```
