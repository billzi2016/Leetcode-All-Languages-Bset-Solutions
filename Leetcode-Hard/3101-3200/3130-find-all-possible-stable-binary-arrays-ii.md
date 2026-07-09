# 3130. Find All Possible Stable Binary Arrays II

## Cpp

```cpp
class Solution {
public:
    int numberOfStableArrays(int zero, int one, int limit) {
        const int MOD = 1000000007;
        vector<vector<int>> dp0(zero + 1, vector<int>(one + 1, 0));
        vector<vector<int>> dp1(zero + 1, vector<int>(one + 1, 0));
        vector<vector<int>> sum0(zero + 1, vector<int>(one + 1, 0)); // prefix over j for fixed i
        vector<vector<int>> sum1(zero + 1, vector<int>(one + 1, 0)); // prefix over i for fixed j

        for (int i = 0; i <= zero; ++i) {
            for (int j = 0; j <= one; ++j) {
                if (i == 0 && j == 0) {
                    sum0[i][j] = sum1[i][j] = 0;
                    continue;
                }
                // compute dp0[i][j]: ends with 0
                if (i > 0) {
                    if (j == 0) { // only zeros
                        dp0[i][j] = (i <= limit) ? 1 : 0;
                    } else {
                        int left = max(0, i - limit);
                        long long val = sum1[i - 1][j];
                        if (left - 1 >= 0) val = (val - sum1[left - 1][j] + MOD) % MOD;
                        dp0[i][j] = (int)val;
                    }
                }
                // compute dp1[i][j]: ends with 1
                if (j > 0) {
                    if (i == 0) { // only ones
                        dp1[i][j] = (j <= limit) ? 1 : 0;
                    } else {
                        int leftj = max(0, j - limit);
                        long long val = sum0[i][j - 1];
                        if (leftj - 1 >= 0) val = (val - sum0[i][leftj - 1] + MOD) % MOD;
                        dp1[i][j] = (int)val;
                    }
                }
                // update prefix sums
                sum0[i][j] = ((j > 0 ? sum0[i][j - 1] : 0) + dp0[i][j]) % MOD;
                sum1[i][j] = ((i > 0 ? sum1[i - 1][j] : 0) + dp1[i][j]) % MOD;
            }
        }
        int ans = (dp0[zero][one] + dp1[zero][one]) % MOD;
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static final int MOD = 1_000_000_007;
    public int numberOfStableArrays(int zero, int one, int limit) {
        int Z = zero, O = one, L = limit;
        long[][] dp0 = new long[Z + 1][O + 1];
        long[][] dp1 = new long[Z + 1][O + 1];
        long[][] pref0 = new long[Z + 1][O + 1];
        long[][] pref1 = new long[Z + 1][O + 1];

        for (int x = 0; x <= Z; x++) {
            for (int y = 0; y <= O; y++) {
                if (x == 0 && y == 0) continue; // empty array not counted

                long v0 = 0, v1 = 0;

                // compute dp ending with 0
                if (x > 0) {
                    int left = Math.max(0, x - L);
                    long sum = pref1[x - 1][y];
                    if (left > 0) {
                        sum -= pref1[left - 1][y];
                        if (sum < 0) sum += MOD;
                    }
                    v0 = sum % MOD;
                }

                // compute dp ending with 1
                if (y > 0) {
                    int leftY = Math.max(0, y - L);
                    long sum = pref0[x][y - 1];
                    if (leftY > 0) {
                        sum -= pref0[x][leftY - 1];
                        if (sum < 0) sum += MOD;
                    }
                    v1 = sum % MOD;
                }

                // base cases: single block arrays
                if (y == 0 && x <= L) v0 = 1;
                if (x == 0 && y <= L) v1 = 1;

                dp0[x][y] = v0;
                dp1[x][y] = v1;

                // update prefix sums over x dimension
                long p0 = ((x > 0 ? pref0[x - 1][y] : 0) + dp0[x][y]) % MOD;
                long p1 = ((x > 0 ? pref1[x - 1][y] : 0) + dp1[x][y]) % MOD;
                pref0[x][y] = p0;
                pref1[x][y] = p1;
            }
        }

        long ans = (dp0[Z][O] + dp1[Z][O]) % MOD;
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfStableArrays(self, zero, one, limit):
        """
        :type zero: int
        :type one: int
        :type limit: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]  # ends with 0
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]  # ends with 1
        pre0 = [[0] * (one + 1) for _ in range(zero + 1)]  # prefix over j for dp0
        pre1 = [[0] * (one + 1) for _ in range(zero + 1)]  # prefix over i for dp1

        # base cases: single group of zeros or ones
        for i in range(1, min(limit, zero) + 1):
            dp0[i][0] = 1
        for j in range(1, min(limit, one) + 1):
            dp1[0][j] = 1

        # fill prefix arrays for the base rows/cols
        for i in range(zero + 1):
            pre0[i][0] = dp0[i][0]
        for j in range(one + 1):
            pre1[0][j] = dp1[0][j]

        for i in range(zero + 1):
            for j in range(one + 1):
                if i == 0 and j == 0:
                    continue

                # compute dp0[i][j] (ending with 0)
                if i > 0:
                    left = i - 1
                    right = i - limit - 1
                    val = pre1[left][j]
                    if right >= 0:
                        val = (val - pre1[right][j]) % MOD
                    dp0[i][j] = (dp0[i][j] + val) % MOD

                # compute dp1[i][j] (ending with 1)
                if j > 0:
                    left = j - 1
                    right = j - limit - 1
                    val = pre0[i][left]
                    if right >= 0:
                        val = (val - pre0[i][right]) % MOD
                    dp1[i][j] = (dp1[i][j] + val) % MOD

                # update prefix sums
                if j > 0:
                    pre0[i][j] = (pre0[i][j-1] + dp0[i][j]) % MOD
                else:
                    pre0[i][j] = dp0[i][j] % MOD

                if i > 0:
                    pre1[i][j] = (pre1[i-1][j] + dp1[i][j]) % MOD
                else:
                    pre1[i][j] = dp1[i][j] % MOD

        return (dp0[zero][one] + dp1[zero][one]) % MOD
```

## Python3

```python
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]  # end with 0
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]  # end with 1

        # base cases: only zeros or only ones
        for i in range(1, min(zero, limit) + 1):
            dp0[i][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp1[0][j] = 1

        # window sums of dp1 over last 'limit' rows for each column (ones count)
        window_sum1 = [dp1[0][j] % MOD for j in range(one + 1)]

        for i in range(1, zero + 1):
            # compute dp0[i][*] using current window sums
            for j in range(one + 1):
                dp0[i][j] = window_sum1[j]
            # enforce base case for column 0 (all zeros)
            if i <= limit:
                dp0[i][0] = 1
            else:
                dp0[i][0] = 0

            # compute dp1[i][*] using sliding window over j (ones count)
            win0 = 0
            for j in range(1, one + 1):
                win0 = (win0 + dp0[i][j - 1]) % MOD
                if j - limit - 1 >= 0:
                    win0 = (win0 - dp0[i][j - limit - 1]) % MOD
                dp1[i][j] = win0

            # update window_sum1 for next iteration (i+1)
            for j in range(one + 1):
                val = window_sum1[j] + dp1[i][j]
                if i - limit >= 0:
                    val -= dp1[i - limit][j]
                window_sum1[j] = val % MOD

        return (dp0[zero][one] + dp1[zero][one]) % MOD
```

## C

```c
int numberOfStableArrays(int zero, int one, int limit) {
    const int MOD = 1000000007;
    static int dp0[1001][1001];
    static int dp1[1001][1001];
    int *win0 = (int*)calloc(one + 1, sizeof(int));
    for (int x = 0; x <= zero; ++x) {
        // compute dp0[x][*]
        for (int y = 0; y <= one; ++y) {
            if (x == 0 && y == 0) {
                dp0[0][0] = 0;
            } else if (y == 0) {
                dp0[x][0] = (x >= 1 && x <= limit) ? 1 : 0;
            } else {
                dp0[x][y] = win0[y];
            }
        }
        // compute dp1[x][*]
        long long winSum = 0;
        for (int y = 0; y <= one; ++y) {
            if (x == 0 && y == 0) {
                dp1[0][0] = 0;
            } else if (x == 0) {
                dp1[0][y] = (y >= 1 && y <= limit) ? 1 : 0;
            } else {
                dp1[x][y] = (int)(winSum % MOD);
            }
            winSum += dp0[x][y];
            if (winSum >= MOD) winSum -= MOD;
            if (y - limit + 1 >= 0) {
                winSum -= dp0[x][y - limit + 1];
                if (winSum < 0) winSum += MOD;
            }
        }
        // update sliding window for next x
        for (int y = 0; y <= one; ++y) {
            int val = dp1[x][y];
            int newWin = win0[y] + val;
            if (newWin >= MOD) newWin -= MOD;
            if (x - limit >= 0) {
                newWin -= dp1[x - limit][y];
                if (newWin < 0) newWin += MOD;
            }
            win0[y] = newWin;
        }
    }
    int ans = dp0[zero][one] + dp1[zero][one];
    if (ans >= MOD) ans -= MOD;
    free(win0);
    return ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int NumberOfStableArrays(int zero, int one, int limit) {
        const int MOD = 1000000007;
        int[,] dp0 = new int[zero + 1, one + 1]; // ends with 0
        int[,] dp1 = new int[zero + 1, one + 1]; // ends with 1
        int[,] pre0O = new int[zero + 1, one + 1]; // prefix over ones for dp0 (same zero)
        int[,] pre1Z = new int[zero + 1, one + 1]; // prefix over zeros for dp1 (same one)

        for (int z = 0; z <= zero; ++z) {
            for (int o = 0; o <= one; ++o) {
                if (z == 0 && o == 0) continue;

                // compute dp0[z,o]
                if (o == 0) {
                    dp0[z, o] = (z >= 1 && z <= limit) ? 1 : 0;
                } else if (z > 0) {
                    int leftZ = Math.Max(z - limit, 0);
                    long sum = pre1Z[z - 1, o];
                    if (leftZ > 0) {
                        sum = (sum - pre1Z[leftZ - 1, o] + MOD) % MOD;
                    }
                    dp0[z, o] = (int)sum;
                } else {
                    dp0[z, o] = 0;
                }

                // compute dp1[z,o]
                if (z == 0) {
                    dp1[z, o] = (o >= 1 && o <= limit) ? 1 : 0;
                } else if (o > 0) {
                    int leftO = Math.Max(o - limit, 0);
                    long sum = pre0O[z, o - 1];
                    if (leftO > 0) {
                        sum = (sum - pre0O[z, leftO - 1] + MOD) % MOD;
                    }
                    dp1[z, o] = (int)sum;
                } else {
                    dp1[z, o] = 0;
                }

                // update prefixes
                int upPre1 = (z > 0) ? pre1Z[z - 1, o] : 0;
                pre1Z[z, o] = (upPre1 + dp1[z, o]) % MOD;

                int leftPre0 = (o > 0) ? pre0O[z, o - 1] : 0;
                pre0O[z, o] = (leftPre0 + dp0[z, o]) % MOD;
            }
        }

        long ans = ((long)dp0[zero, one] + dp1[zero, one]) % MOD;
        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} zero
 * @param {number} one
 * @param {number} limit
 * @return {number}
 */
var numberOfStableArrays = function(zero, one, limit) {
    const MOD = 1000000007;
    // dp0[x][y]: ends with 0, dp1[x][y]: ends with 1
    const dp0 = Array.from({length: zero + 1}, () => new Array(one + 1).fill(0));
    const dp1 = Array.from({length: zero + 1}, () => new Array(one + 1).fill(0));
    // prefix sums over x for dp1 (pref1[y][x]) and over y for dp0 (pref0[x][y])
    const pref0 = Array.from({length: zero + 1}, () => new Array(one + 1).fill(0));
    const pref1 = Array.from({length: one + 1}, () => new Array(zero + 1).fill(0));

    // base cases: single block arrays
    for (let x = 1; x <= zero && x <= limit; ++x) dp0[x][0] = 1;
    for (let y = 1; y <= one && y <= limit; ++y) dp1[0][y] = 1;

    for (let x = 0; x <= zero; ++x) {
        for (let y = 0; y <= one; ++y) {
            if (x === 0 && y === 0) continue;

            // compute dp0[x][y] when y > 0 and x > 0
            if (y > 0 && x > 0) {
                const left = Math.max(0, x - limit);
                let total = pref1[y][x - 1];
                if (left > 0) {
                    total = (total - pref1[y][left - 1] + MOD) % MOD;
                }
                dp0[x][y] = total;
            }

            // compute dp1[x][y] when x > 0 and y > 0
            if (x > 0 && y > 0) {
                const top = Math.max(0, y - limit);
                let total = pref0[x][y - 1];
                if (top > 0) {
                    total = (total - pref0[x][top - 1] + MOD) % MOD;
                }
                dp1[x][y] = total;
            }

            // update prefix sums
            const prevPref0 = y > 0 ? pref0[x][y - 1] : 0;
            pref0[x][y] = (prevPref0 + dp0[x][y]) % MOD;

            const prevPref1 = x > 0 ? pref1[y][x - 1] : 0;
            pref1[y][x] = (prevPref1 + dp1[x][y]) % MOD;
        }
    }

    return (dp0[zero][one] + dp1[zero][one]) % MOD;
};
```

## Typescript

```typescript
function numberOfStableArrays(zero: number, one: number, limit: number): number {
    const MOD = 1000000007;
    const dp0: number[][] = Array.from({ length: zero + 1 }, () => new Array(one + 1).fill(0));
    const dp1: number[][] = Array.from({ length: zero + 1 }, () => new Array(one + 1).fill(0));
    const pref0: number[][] = Array.from({ length: zero + 1 }, () => new Array(one + 1).fill(0)); // row prefix of dp0
    const pref1: number[][] = Array.from({ length: zero + 1 }, () => new Array(one + 1).fill(0)); // column prefix of dp1

    for (let z = 0; z <= zero; ++z) {
        for (let o = 0; o <= one; ++o) {
            // compute dp0[z][o]
            if (z === 0) {
                dp0[z][o] = 0;
            } else if (o === 0 && z <= limit) {
                dp0[z][o] = 1;
            } else {
                const left = pref1[z - 1][o];
                const subIdx = z - limit - 1;
                const sub = subIdx >= 0 ? pref1[subIdx][o] : 0;
                let val = left - sub;
                if (val < 0) val += MOD;
                dp0[z][o] = val;
            }
            // update row prefix for dp0
            pref0[z][o] = ((o > 0 ? pref0[z][o - 1] : 0) + dp0[z][o]) % MOD;

            // compute dp1[z][o]
            if (o === 0) {
                dp1[z][o] = 0;
            } else if (z === 0 && o <= limit) {
                dp1[z][o] = 1;
            } else {
                const leftRow = pref0[z][o - 1];
                const subIdx2 = o - limit - 1;
                const sub2 = subIdx2 >= 0 ? pref0[z][subIdx2] : 0;
                let val2 = leftRow - sub2;
                if (val2 < 0) val2 += MOD;
                dp1[z][o] = val2;
            }
            // update column prefix for dp1
            pref1[z][o] = ((z > 0 ? pref1[z - 1][o] : 0) + dp1[z][o]) % MOD;
        }
    }

    const result = (dp0[zero][one] + dp1[zero][one]) % MOD;
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $zero
     * @param Integer $one
     * @param Integer $limit
     * @return Integer
     */
    function numberOfStableArrays($zero, $one, $limit) {
        $mod = 1000000007;
        // initialize DP and prefix arrays
        $dp0   = array_fill(0, $zero + 1, array_fill(0, $one + 1, 0));
        $dp1   = array_fill(0, $zero + 1, array_fill(0, $one + 1, 0));
        $pref0 = array_fill(0, $zero + 1, array_fill(0, $one + 1, 0));
        $pref1 = array_fill(0, $zero + 1, array_fill(0, $one + 1, 0));

        // base cases: only zeros or only ones (run length must not exceed limit)
        for ($x = 1; $x <= $zero && $x <= $limit; $x++) {
            $dp0[$x][0] = 1;
        }
        for ($y = 1; $y <= $one && $y <= $limit; $y++) {
            $dp1[0][$y] = 1;
        }

        // DP computation
        for ($x = 0; $x <= $zero; $x++) {
            for ($y = 0; $y <= $one; $y++) {
                if ($x == 0 && $y == 0) {
                    $pref0[0][0] = 0;
                    $pref1[0][0] = 0;
                    continue;
                }

                // compute dp0[x][y] (ending with 0), need y > 0
                if ($y > 0) {
                    $maxK = min($limit, $x);
                    if ($maxK > 0) {
                        $leftIdx = $x - 1;
                        $sum = $pref1[$leftIdx][$y];
                        $rightIdx = $x - $maxK - 1;
                        if ($rightIdx >= 0) {
                            $sum -= $pref1[$rightIdx][$y];
                            if ($sum < 0) $sum += $mod;
                        }
                        $dp0[$x][$y] = $sum % $mod;
                    } else {
                        $dp0[$x][$y] = 0;
                    }
                }

                // update pref0 (cumulative over y for fixed x)
                $prevPref0 = ($y > 0) ? $pref0[$x][$y - 1] : 0;
                $pref0[$x][$y] = ($prevPref0 + $dp0[$x][$y]) % $mod;

                // compute dp1[x][y] (ending with 1), need x > 0
                if ($x > 0) {
                    $maxK = min($limit, $y);
                    if ($maxK > 0) {
                        $leftIdx = $y - 1;
                        $sum = $pref0[$x][$leftIdx];
                        $rightIdx = $y - $maxK - 1;
                        if ($rightIdx >= 0) {
                            $sum -= $pref0[$x][$rightIdx];
                            if ($sum < 0) $sum += $mod;
                        }
                        $dp1[$x][$y] = $sum % $mod;
                    } else {
                        $dp1[$x][$y] = 0;
                    }
                }

                // update pref1 (cumulative over x for fixed y)
                $prevPref1 = ($x > 0) ? $pref1[$x - 1][$y] : 0;
                $pref1[$x][$y] = ($prevPref1 + $dp1[$x][$y]) % $mod;
            }
        }

        $ans = ($dp0[$zero][$one] + $dp1[$zero][$one]) % $mod;
        return $ans;
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    private let MOD = 1_000_000_007
    
    func numberOfStableArrays(_ zero: Int, _ one: Int, _ limit: Int) -> Int {
        let rows = zero + 1
        let cols = one + 1
        
        var dp0 = Array(repeating: Array(repeating: 0, count: cols), count: rows)
        var dp1 = Array(repeating: Array(repeating: 0, count: cols), count: rows)
        var pref0 = Array(repeating: Array(repeating: 0, count: cols), count: rows) // prefix over columns for dp0
        var pref1 = Array(repeating: Array(repeating: 0, count: cols), count: rows) // prefix over rows for dp1
        
        // base cases: only zeros or only ones (single block)
        if limit > 0 {
            let maxZeroBlock = min(limit, zero)
            if maxZeroBlock >= 1 {
                for k in 1...maxZeroBlock {
                    dp0[k][0] = 1
                }
            }
            let maxOneBlock = min(limit, one)
            if maxOneBlock >= 1 {
                for k in 1...maxOneBlock {
                    dp1[0][k] = 1
                }
            }
        }
        
        // iterate by total length
        let maxTotal = zero + one
        for total in 0...maxTotal {
            let iStart = max(0, total - one)
            let iEnd = min(zero, total)
            if iStart > iEnd { continue }
            for i in iStart...iEnd {
                let j = total - i
                
                // compute dp0[i][j] when both counts are positive
                if i > 0 && j > 0 {
                    let low = max(0, i - limit)
                    var sum = pref1[i - 1][j]
                    if low > 0 {
                        sum -= pref1[low - 1][j]
                        if sum < 0 { sum += MOD }
                    }
                    dp0[i][j] = sum % MOD
                }
                
                // compute dp1[i][j] when both counts are positive
                if i > 0 && j > 0 {
                    let lowJ = max(0, j - limit)
                    var sum = pref0[i][j - 1]
                    if lowJ > 0 {
                        sum -= pref0[i][lowJ - 1]
                        if sum < 0 { sum += MOD }
                    }
                    dp1[i][j] = sum % MOD
                }
                
                // update prefix sums
                let prevPref0 = (j > 0) ? pref0[i][j - 1] : 0
                var curPref0 = prevPref0 + dp0[i][j]
                if curPref0 >= MOD { curPref0 -= MOD }
                pref0[i][j] = curPref0
                
                let prevPref1 = (i > 0) ? pref1[i - 1][j] : 0
                var curPref1 = prevPref1 + dp1[i][j]
                if curPref1 >= MOD { curPref1 -= MOD }
                pref1[i][j] = curPref1
            }
        }
        
        let result = (dp0[zero][one] + dp1[zero][one]) % MOD
        return result
    }
}
```

## Kotlin

```kotlin
import java.util.*

class Solution {
    private val MOD = 1_000_000_007L

    fun numberOfStableArrays(zero: Int, one: Int, limit: Int): Int {
        val dp0 = Array(zero + 1) { LongArray(one + 1) }
        val dp1 = Array(zero + 1) { LongArray(one + 1) }
        val pref0 = Array(zero + 1) { LongArray(one + 1) } // prefix over columns (j)
        val pref1 = Array(zero + 1) { LongArray(one + 1) } // prefix over rows (i)

        fun modSub(a: Long, b: Long): Long {
            var res = a - b
            if (res < 0) res += MOD
            return res
        }

        for (i in 0..zero) {
            for (j in 0..one) {
                // compute dp0[i][j] : ending with 0
                var cur0 = 0L
                if (i > 0 && j == 0) {
                    cur0 = if (i <= limit) 1L else 0L
                } else if (i > 0) {
                    val left = maxOf(0, i - limit)
                    var sum = pref1[i - 1][j]
                    if (left > 0) {
                        sum = modSub(sum, pref1[left - 1][j])
                    }
                    cur0 = sum
                }
                dp0[i][j] = cur0
                // update prefix over columns for dp0
                val p0 = ((if (j > 0) pref0[i][j - 1] else 0L) + cur0) % MOD
                pref0[i][j] = p0

                // compute dp1[i][j] : ending with 1
                var cur1 = 0L
                if (j > 0 && i == 0) {
                    cur1 = if (j <= limit) 1L else 0L
                } else if (j > 0) {
                    val leftJ = maxOf(0, j - limit)
                    var sum = pref0[i][j - 1]
                    if (leftJ > 0) {
                        sum = modSub(sum, pref0[i][leftJ - 1])
                    }
                    cur1 = sum
                }
                dp1[i][j] = cur1
                // update prefix over rows for dp1
                val p1 = ((if (i > 0) pref1[i - 1][j] else 0L) + cur1) % MOD
                pref1[i][j] = p1
            }
        }

        val ans = (dp0[zero][one] + dp1[zero][one]) % MOD
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _MOD = 1000000007;

  int numberOfStableArrays(int zero, int one, int limit) {
    // dp0[x][y]: ends with 0, dp1[x][y]: ends with 1
    List<List<int>> dp0 = List.generate(zero + 1, (_) => List.filled(one + 1, 0));
    List<List<int>> dp1 = List.generate(zero + 1, (_) => List.filled(one + 1, 0));

    // prefix sums: pref0[x][y] = sum_{j=0..y} dp0[x][j]
    //               pref1[y][x] = sum_{i=0..x} dp1[i][y]
    List<List<int>> pref0 = List.generate(zero + 1, (_) => List.filled(one + 1, 0));
    List<List<int>> pref1 = List.generate(one + 1, (_) => List.filled(zero + 1, 0));

    for (int x = 0; x <= zero; ++x) {
      for (int y = 0; y <= one; ++y) {
        if (x == 0 && y == 0) continue; // empty array not counted

        int val0 = 0;
        int val1 = 0;

        if (y == 0) {
          // only zeros
          if (x >= 1 && x <= limit) val0 = 1;
        } else if (x == 0) {
          // only ones
          if (y >= 1 && y <= limit) val1 = 1;
        } else {
          // both types present, use prefix sums
          int leftX = x - limit;
          if (leftX < 0) leftX = 0;
          int total0 = pref1[y][x - 1];
          int sub0 = leftX > 0 ? pref1[y][leftX - 1] : 0;
          val0 = total0 - sub0;
          if (val0 < 0) val0 += _MOD;

          int leftY = y - limit;
          if (leftY < 0) leftY = 0;
          int total1 = pref0[x][y - 1];
          int sub1 = leftY > 0 ? pref0[x][leftY - 1] : 0;
          val1 = total1 - sub1;
          if (val1 < 0) val1 += _MOD;
        }

        dp0[x][y] = val0 % _MOD;
        dp1[x][y] = val1 % _MOD;

        // update prefix sums
        int prevPref0 = y > 0 ? pref0[x][y - 1] : 0;
        pref0[x][y] = (prevPref0 + dp0[x][y]) % _MOD;

        int prevPref1 = x > 0 ? pref1[y][x - 1] : 0;
        pref1[y][x] = (prevPref1 + dp1[x][y]) % _MOD;
      }
    }

    return (dp0[zero][one] + dp1[zero][one]) % _MOD;
  }
}
```

## Golang

```go
package main

import "fmt"

const MOD int64 = 1000000007

func numberOfStableArrays(zero int, one int, limit int) int {
	z := zero
	o := one
	// dp0[i][j]: ends with 0 using i zeros and j ones
	// dp1[i][j]: ends with 1 using i zeros and j ones
	dp0 := make([][]int64, z+1)
	dp1 := make([][]int64, z+1)
	pref0 := make([][]int64, z+1) // prefix over j for each i
	pref1 := make([][]int64, z+1) // prefix over i for each j
	for i := 0; i <= z; i++ {
		dp0[i] = make([]int64, o+1)
		dp1[i] = make([]int64, o+1)
		pref0[i] = make([]int64, o+1)
		pref1[i] = make([]int64, o+1)
	}
	// base cases: only zeros or only ones with length <= limit
	for i := 1; i <= z && i <= limit; i++ {
		dp0[i][0] = 1
	}
	for j := 1; j <= o && j <= limit; j++ {
		dp1[0][j] = 1
	}

	for i := 0; i <= z; i++ {
		for j := 0; j <= o; j++ {
			if i == 0 && j == 0 {
				// nothing to do, already zero
			} else if j == 0 { // only zeros, base already set
				// dp0[i][0] already initialized (or remains 0)
			} else if i == 0 { // only ones, base already set
				// dp1[0][j] already initialized (or remains 0)
			} else {
				// compute dp0[i][j]
				l := i - limit
				if l < 0 {
					l = 0
				}
				r := i - 1
				var sum int64 = 0
				if r >= 0 {
					sum = pref1[r][j]
					if l-1 >= 0 {
						sum = (sum - pref1[l-1][j] + MOD) % MOD
					}
				}
				dp0[i][j] = sum

				// compute dp1[i][j]
				l2 := j - limit
				if l2 < 0 {
					l2 = 0
				}
				r2 := j - 1
				sum = 0
				if r2 >= 0 {
					sum = pref0[i][r2]
					if l2-1 >= 0 {
						sum = (sum - pref0[i][l2-1] + MOD) % MOD
					}
				}
				dp1[i][j] = sum
			}

			// update prefix sums
			var val0 int64
			if j > 0 {
				val0 = pref0[i][j-1]
			} else {
				val0 = 0
			}
			val0 = (val0 + dp0[i][j]) % MOD
			pref0[i][j] = val0

			var val1 int64
			if i > 0 {
				val1 = pref1[i-1][j]
			} else {
				val1 = 0
			}
			val1 = (val1 + dp1[i][j]) % MOD
			pref1[i][j] = val1
		}
	}

	ans := (dp0[z][o] + dp1[z][o]) % MOD
	return int(ans)
}

// The following main function is only for local testing and will be ignored on LeetCode.
func main() {
	fmt.Println(numberOfStableArrays(1, 1, 2)) // 2
	fmt.Println(numberOfStableArrays(1, 2, 1)) // 1
	fmt.Println(numberOfStableArrays(3, 3, 2)) // 14
}
```

## Ruby

```ruby
def number_of_stable_arrays(zero, one, limit)
  mod = 1_000_000_007
  dp0 = Array.new(zero + 1) { Array.new(one + 1, 0) }
  dp1 = Array.new(zero + 1) { Array.new(one + 1, 0) }
  pref0 = Array.new(zero + 1) { Array.new(one + 1, 0) } # sum over y for fixed x
  pref1 = Array.new(zero + 1) { Array.new(one + 1, 0) } # sum over x for fixed y

  maxz = [limit, zero].min
  (1..maxz).each { |k| dp0[k][0] = 1 }
  maxo = [limit, one].min
  (1..maxo).each { |k| dp1[0][k] = 1 }

  (0..zero).each do |x|
    (0..one).each do |y|
      # compute dp0[x][y]: end with 0, previous block is 1
      if y > 0 && x > 0
        low = x - limit
        low = 0 if low < 0
        total = pref1[x - 1][y]
        sub = low > 0 ? pref1[low - 1][y] : 0
        val = total - sub
        val += mod if val < 0
        dp0[x][y] = (dp0[x][y] + val) % mod
      end

      # compute dp1[x][y]: end with 1, previous block is 0
      if x > 0 && y > 0
        low = y - limit
        low = 0 if low < 0
        total = pref0[x][y - 1]
        sub = low > 0 ? pref0[x][low - 1] : 0
        val = total - sub
        val += mod if val < 0
        dp1[x][y] = (dp1[x][y] + val) % mod
      end

      # update prefix sums
      pref0[x][y] = ((y > 0 ? pref0[x][y - 1] : 0) + dp0[x][y]) % mod
      pref1[x][y] = ((x > 0 ? pref1[x - 1][y] : 0) + dp1[x][y]) % mod
    end
  end

  (dp0[zero][one] + dp1[zero][one]) % mod
end
```

## Scala

```scala
object Solution {
    def numberOfStableArrays(zero: Int, one: Int, limit: Int): Int = {
        val MOD = 1000000007L
        val dp0 = Array.ofDim[Long](zero + 1, one + 1)
        val dp1 = Array.ofDim[Long](zero + 1, one + 1)

        // base cases: single group of zeros or ones
        val maxZeroBase = math.min(limit, zero)
        var i = 1
        while (i <= maxZeroBase) {
            dp0(i)(0) = 1L
            i += 1
        }
        val maxOneBase = math.min(limit, one)
        i = 1
        while (i <= maxOneBase) {
            dp1(0)(i) = 1L
            i += 1
        }

        // sliding window sums of last 'limit' rows of dp1 for each column (y)
        val winSumZero = Array.ofDim[Long](one + 1)

        var x = 0
        while (x <= zero) {
            // add contributions from previous dp1 rows (stored in winSumZero) to dp0[x][*]
            var y = 0
            while (y <= one) {
                val added = winSumZero(y)
                if (added != 0) {
                    dp0(x)(y) = (dp0(x)(y) + added) % MOD
                }
                y += 1
            }

            // compute dp1[x][*] using sliding window over y of dp0[x][*]
            var sumY = 0L
            y = 0
            while (y <= one) {
                if (y - 1 >= 0) {
                    sumY += dp0(x)(y - 1)
                    if (sumY >= MOD) sumY -= MOD
                }
                if (y - limit - 1 >= 0) {
                    sumY -= dp0(x)(y - limit - 1)
                    if (sumY < 0) sumY += MOD
                }
                val added = sumY
                if (added != 0) {
                    dp1(x)(y) = (dp1(x)(y) + added) % MOD
                }
                y += 1
            }

            // update winSumZero for next x (add current row, remove row that slides out)
            if (x < zero) { // no need after last iteration
                y = 0
                while (y <= one) {
                    var v = winSumZero(y) + dp1(x)(y)
                    if (v >= MOD) v -= MOD
                    if (x - limit >= 0) {
                        v -= dp1(x - limit)(y)
                        if (v < 0) v += MOD
                    }
                    winSumZero(y) = v
                    y += 1
                }
            }

            x += 1
        }

        ((dp0(zero)(one) + dp1(zero)(one)) % MOD).toInt
    }
}
```

## Rust

```rust
use std::cmp::min;

impl Solution {
    pub fn number_of_stable_arrays(zero: i32, one: i32, limit: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let z = zero as usize;
        let o = one as usize;
        let lim = limit as usize;

        // dp0[i][j]: ends with 0, uses i zeros and j ones
        // dp1[i][j]: ends with 1
        let mut dp0 = vec![vec![0i64; o + 1]; z + 1];
        let mut dp1 = vec![vec![0i64; o + 1]; z + 1];

        // pref0_j[i][j] = sum_{t=0..j} dp0[i][t]
        let mut pref0_j = vec![vec![0i64; o + 1]; z + 1];
        // pref1_i[i][j] = sum_{t=0..i} dp1[t][j]
        let mut pref1_i = vec![vec![0i64; o + 1]; z + 1];

        for i in 0..=z {
            for j in 0..=o {
                // compute dp0[i][j]
                let mut val0 = 0i64;
                if i > 0 {
                    let left = if i > lim { i - lim } else { 0 };
                    let sum = (pref1_i[i - 1][j] + MOD
                        - if left > 0 { pref1_i[left - 1][j] } else { 0 })
                        % MOD;
                    val0 = sum;
                }
                // base case: only zeros, single block
                if j == 0 && i > 0 && i <= lim {
                    val0 = 1;
                }
                dp0[i][j] = val0;

                // update pref0_j for this row
                let prev_row = if j > 0 { pref0_j[i][j - 1] } else { 0 };
                pref0_j[i][j] = (prev_row + val0) % MOD;

                // compute dp1[i][j]
                let mut val1 = 0i64;
                if j > 0 {
                    let left = if j > lim { j - lim } else { 0 };
                    let sum = (pref0_j[i][j - 1] + MOD
                        - if left > 0 { pref0_j[i][left - 1] } else { 0 })
                        % MOD;
                    val1 = sum;
                }
                // base case: only ones, single block
                if i == 0 && j > 0 && j <= lim {
                    val1 = 1;
                }
                dp1[i][j] = val1;

                // update pref1_i for this column
                let prev_col = if i > 0 { pref1_i[i - 1][j] } else { 0 };
                pref1_i[i][j] = (prev_col + val1) % MOD;
            }
        }

        ((dp0[z][o] + dp1[z][o]) % MOD) as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define (mod-add a b)
  (let ((c (+ a b)))
    (if (>= c MOD) (- c MOD) c)))

(define (mod-sub a b)
  (let ((c (- a b)))
    (if (< c 0) (+ c MOD) c)))

(define/contract (number-of-stable-arrays zero one limit)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  (let* ((z (add1 zero))
         (o (add1 one))
         (dp0 (make-vector z))
         (dp1 (make-vector z))
         (pref0 (make-vector z))
         (pref1 (make-vector z)))
    ;; initialize inner vectors
    (for ([i (in-range z)])
      (vector-set! dp0 i (make-vector o 0))
      (vector-set! dp1 i (make-vector o 0))
      (vector-set! pref0 i (make-vector o 0))
      (vector-set! pref1 i (make-vector o 0)))
    ;; base cases: single group of zeros or ones
    (for ([x (in-range 1 (add1 (min zero limit)))])
      (vector-set! (vector-ref dp0 x) 0 1))
    (for ([y (in-range 1 (add1 (min one limit)))])
      (vector-set! (vector-ref dp1 0) y 1))
    ;; DP computation
    (for ([x (in-range z)])
      (for ([y (in-range o)])
        (cond
          [(and (= x 0) (= y 0)) (void)]
          [else
           ;; compute dp0[x][y] when possible
           (when (> x 0)
             (if (= y 0)
                 (void) ; base already set
                 (let* ((low (max 0 (- x limit)))
                        (high (sub1 x))
                        (sum (mod-sub (vector-ref (vector-ref pref1 high) y)
                                      (if (> low 0)
                                          (vector-ref (vector-ref pref1 (sub1 low)) y)
                                          0))))
                   (vector-set! (vector-ref dp0 x) y sum))))
           ;; compute dp1[x][y] when possible
           (when (> y 0)
             (if (= x 0)
                 (void) ; base already set
                 (let* ((low (max 0 (- y limit)))
                        (high (sub1 y))
                        (sum (mod-sub (vector-ref (vector-ref pref0 x) high)
                                      (if (> low 0)
                                          (vector-ref (vector-ref pref0 x) (sub1 low))
                                          0))))
                   (vector-set! (vector-ref dp1 x) y sum))))
           ;; update prefix sums
           (let* ((dp0xy (vector-ref (vector-ref dp0 x) y))
                  (dp1xy (vector-ref (vector-ref dp1 x) y))
                  (pref0prev (if (> y 0)
                                 (vector-ref (vector-ref pref0 x) (sub1 y))
                                 0))
                  (pref1prev (if (> x 0)
                                 (vector-ref (vector-ref pref1 (sub1 x)) y)
                                 0)))
             (vector-set! (vector-ref pref0 x) y (mod-add dp0xy pref0prev))
             (vector-set! (vector-ref pref1 x) y (mod-add dp1xy pref1prev))))]))
    ;; final answer
    (let ((ans0 (vector-ref (vector-ref dp0 zero) one))
          (ans1 (vector-ref (vector-ref dp1 zero) one)))
      (mod-add ans0 ans1)))
```

## Erlang

```erlang
-define(MOD, 1000000007).

-spec number_of_stable_arrays(Zero :: integer(), One :: integer(), Limit :: integer()) -> integer().
number_of_stable_arrays(Zero, One, Limit) ->
    Mod = ?MOD,
    DP0 = ets:new(dp0, [named_table, public]),
    DP1 = ets:new(dp1, [named_table, public]),

    MaxBaseZ = min(Limit, Zero),
    lists:foreach(fun(Z) -> ets:insert(DP0, {idx(Z, 0, One), 1}) end,
                  lists:seq(1, MaxBaseZ)),

    MaxBaseO = min(Limit, One),
    lists:foreach(fun(O) -> ets:insert(DP1, {idx(0, O, One), 1}) end,
                  lists:seq(1, MaxBaseO)),

    Sums0 = [ if O =< MaxBaseO -> 1; true -> 0 end || O <- lists:seq(0, One) ],

    _FinalSums = loop_z(1, Zero, One, Limit, Mod, DP0, DP1, Sums0),

    KeyAns = idx(Zero, One, One),
    V0 = case ets:lookup(DP0, KeyAns) of [{_, V}] -> V; [] -> 0 end,
    V1 = case ets:lookup(DP1, KeyAns) of [{_, V}] -> V; [] -> 0 end,
    (V0 + V1) rem Mod.

loop_z(Z, Zero, _One, _Limit, _Mod, _DP0, _DP1, Sums0) when Z > Zero ->
    Sums0;
loop_z(Z, Zero, One, Limit, Mod, DP0, DP1, Sums0) ->
    RowDP0 = build_dp0_row(Z, One, Limit, Sums0),
    maps:fold(fun(O, Val, _) -> ets:insert(DP0, {idx(Z, O, One), Val}) end,
              ok, RowDP0),

    RowDP1 = build_dp1_row(One, Limit, Mod, RowDP0),
    maps:fold(fun(O, Val, _) -> ets:insert(DP1, {idx(Z, O, One), Val}) end,
              ok, RowDP1),

    NewSums0 = update_sums0(Sums0, RowDP1, Z, Limit, Mod, DP1, One),
    loop_z(Z + 1, Zero, One, Limit, Mod, DP0, DP1, NewSums0).

build_dp0_row(Z, One, Limit, Sums0) ->
    build_dp0_row(0, Z, One, Limit, Sums0, #{}).
build_dp0_row(O, Z, One, _Limit, Sums0, Acc) when O =< One ->
    Val = if
        O == 0 -> (if Z =< Limit -> 1 else 0 end);
        true   -> lists:nth(O + 1, Sums0)
    end,
    NewAcc = maps:put(O, Val, Acc),
    build_dp0_row(O + 1, Z, One, _Limit, Sums0, NewAcc);
build_dp0_row(_, _, _, _, _, Acc) ->
    Acc.

build_dp1_row(One, Limit, Mod, RowDP0) ->
    build_dp1_row(0, One, Limit, Mod, RowDP0, 0, #{}).
build_dp1_row(O, One, _Limit, _Mod, _RowDP0, Win, Acc) when O > One ->
    Acc;
build_dp1_row(0, One, Limit, Mod, RowDP0, _Win, Acc) ->
    NewAcc = maps:put(0, 0, Acc),
    build_dp1_row(1, One, Limit, Mod, RowDP0, 0, NewAcc);
build_dp1_row(O, One, Limit, Mod, RowDP0, Win, Acc) ->
    Add = maps:get(O - 1, RowDP0),
    Win1 = (Win + Add) rem Mod,
    Win2 = if
        O - Limit - 1 >= 0 ->
            Sub = maps:get(O - Limit - 1, RowDP0),
            (Win1 - Sub + Mod) rem Mod;
        true -> Win1
    end,
    NewAcc = maps:put(O, Win2, Acc),
    build_dp1_row(O + 1, One, Limit, Mod, RowDP0, Win2, NewAcc).

update_sums0(Sums0, RowDP1, Z, Limit, Mod, DP1, One) ->
    [ begin
          OldSum = lists:nth(O + 1, Sums0),
          Val = maps:get(O, RowDP1),
          Sum1 = (OldSum + Val) rem Mod,
          Sum2 = if
              Z - Limit >= 0 ->
                  OldKey = idx(Z - Limit, O, One),
                  case ets:lookup(DP1, OldKey) of
                      [{_, OldVal}] -> (Sum1 - OldVal + Mod) rem Mod;
                      [] -> Sum1
                  end;
              true -> Sum1
          end,
          Sum2
      end || O <- lists:seq(0, One) ].

idx(Z, O, One) ->
    Z * (One + 1) + O.
```

## Elixir

```elixir
defmodule Solution do
  @mod 1_000_000_007

  @spec number_of_stable_arrays(zero :: integer, one :: integer, limit :: integer) :: integer
  def number_of_stable_arrays(zero, one, limit) do
    cols = one + 1
    rows = zero + 1
    size = rows * cols

    idx = fn z, o -> z * cols + o end

    # dp0 and dp1 stored in Erlang arrays for fast random access
    dp0 = :array.new(size, default: 0)
    dp1 = :array.new(size, default: 0)

    # base cases: only ones (no zeros) and only zeros (no ones)
    dp1 =
      Enum.reduce(1..one, dp1, fn o, acc ->
        if o <= limit do
          :array.set(idx.(0, o), 1, acc)
        else
          acc
        end
      end)

    dp0 =
      Enum.reduce(1..zero, dp0, fn z, acc ->
        if z <= limit do
          :array.set(idx.(z, 0), 1, acc)
        else
          acc
        end
      end)

    # column sliding sums of dp1 for the last `limit` rows
    col_sum = :array.new(cols, default: 0)

    {final_dp0, final_dp1, _} =
      Enum.reduce(0..zero, {dp0, dp1, col_sum}, fn z, {cur_dp0, cur_dp1, cur_col_sum} ->
        # inner loop over columns (number of ones)
        {new_dp0, new_dp1, updated_col_sum, _row_sum} =
          Enum.reduce(0..one, {cur_dp0, cur_dp1, cur_col_sum, 0}, fn o,
                                                                   {d0, d1, csum, row_sum} ->
            # dp0 value: sum of dp1 in the same column over previous up to `limit` rows
            dp0_val =
              if z == 0 do
                0
              else
                :array.get(o, csum)
              end

            dp0_val =
              if o == 0 and z >= 1 and z <= limit do
                1
              else
                dp0_val
              end

            d0 = :array.set(idx.(z, o), dp0_val, d0)

            # update rolling sum over ones for dp1 computation
            new_row_sum = row_sum + dp0_val
            if new_row_sum >= @mod, do: new_row_sum = new_row_sum - @mod end

            if o >= limit do
              prev_dp0 = :array.get(idx.(z, o - limit), d0)
              new_row_sum = new_row_sum - prev_dp0
              if new_row_sum < 0, do: new_row_sum = new_row_sum + @mod end
            end

            # dp1 value: sum of dp0 over last `limit` columns (ones)
            dp1_val =
              if o == 0 do
                0
              else
                new_row_sum
              end

            dp1_val =
              if z == 0 and o >= 1 and o <= limit do
                1
              else
                dp1_val
              end

            d1 = :array.set(idx.(z, o), dp1_val, d1)

            {d0, d1, csum, new_row_sum}
          end)

        # after processing the whole row, update column sliding sums with dp1 of this row
        updated_col_sum =
          Enum.reduce(0..one, updated_col_sum, fn o, csum2 ->
            val = :array.get(idx.(z, o), new_dp1)
            cur = :array.get(o, csum2) + val
            if cur >= @mod, do: cur = cur - @mod end

            if z >= limit do
              old = :array.get(idx.(z - limit, o), new_dp1)
              cur = cur - old
              if cur < 0, do: cur = cur + @mod end
            end

            :array.set(o, cur, csum2)
          end)

        {new_dp0, new_dp1, updated_col_sum}
      end)

    ans0 = :array.get(idx.(zero, one), final_dp0)
    ans1 = :array.get(idx.(zero, one), final_dp1)
    rem(ans0 + ans1, @mod)
  end
end
```
