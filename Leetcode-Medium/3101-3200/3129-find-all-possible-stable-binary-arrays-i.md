# 3129. Find All Possible Stable Binary Arrays I

## Cpp

```cpp
class Solution {
public:
    int numberOfStableArrays(int zero, int one, int limit) {
        const int MOD = 1000000007;
        static int dp[201][201][2][201];
        memset(dp, 0, sizeof(dp));
        if (zero > 0) dp[1][0][0][1] = 1;
        if (one > 0) dp[0][1][1][1] = 1;
        for (int z = 0; z <= zero; ++z) {
            for (int o = 0; o <= one; ++o) {
                for (int last = 0; last < 2; ++last) {
                    for (int len = 1; len <= limit; ++len) {
                        int cur = dp[z][o][last][len];
                        if (!cur) continue;
                        // add same element
                        if (len < limit) {
                            if (last == 0 && z + 1 <= zero) {
                                int &ref = dp[z + 1][o][0][len + 1];
                                ref += cur;
                                if (ref >= MOD) ref -= MOD;
                            }
                            if (last == 1 && o + 1 <= one) {
                                int &ref = dp[z][o + 1][1][len + 1];
                                ref += cur;
                                if (ref >= MOD) ref -= MOD;
                            }
                        }
                        // add opposite element
                        if (last == 0) {
                            if (o + 1 <= one) {
                                int &ref = dp[z][o + 1][1][1];
                                ref += cur;
                                if (ref >= MOD) ref -= MOD;
                            }
                        } else {
                            if (z + 1 <= zero) {
                                int &ref = dp[z + 1][o][0][1];
                                ref += cur;
                                if (ref >= MOD) ref -= MOD;
                            }
                        }
                    }
                }
            }
        }
        long long ans = 0;
        for (int last = 0; last < 2; ++last)
            for (int len = 1; len <= limit; ++len) {
                ans += dp[zero][one][last][len];
                if (ans >= MOD) ans -= MOD;
            }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    public int numberOfStableArrays(int zero, int one, int limit) {
        int[][][][] dp = new int[zero + 1][one + 1][2][limit + 1];
        if (zero > 0) dp[1][0][0][1] = 1;
        if (one > 0) dp[0][1][1][1] = 1;

        for (int z = 0; z <= zero; ++z) {
            for (int o = 0; o <= one; ++o) {
                for (int last = 0; last < 2; ++last) {
                    for (int len = 1; len <= limit; ++len) {
                        int cur = dp[z][o][last][len];
                        if (cur == 0) continue;
                        if (last == 0) { // ending with 0
                            // add another 0
                            if (z + 1 <= zero && len < limit) {
                                int v = dp[z + 1][o][0][len + 1] + cur;
                                if (v >= MOD) v -= MOD;
                                dp[z + 1][o][0][len + 1] = v;
                            }
                            // add a 1
                            if (o + 1 <= one) {
                                int v = dp[z][o + 1][1][1] + cur;
                                if (v >= MOD) v -= MOD;
                                dp[z][o + 1][1][1] = v;
                            }
                        } else { // ending with 1
                            // add another 1
                            if (o + 1 <= one && len < limit) {
                                int v = dp[z][o + 1][1][len + 1] + cur;
                                if (v >= MOD) v -= MOD;
                                dp[z][o + 1][1][len + 1] = v;
                            }
                            // add a 0
                            if (z + 1 <= zero) {
                                int v = dp[z + 1][o][0][1] + cur;
                                if (v >= MOD) v -= MOD;
                                dp[z + 1][o][0][1] = v;
                            }
                        }
                    }
                }
            }
        }

        long ans = 0;
        for (int last = 0; last < 2; ++last) {
            for (int len = 1; len <= limit; ++len) {
                ans += dp[zero][one][last][len];
                if (ans >= MOD) ans -= MOD;
            }
        }
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
        # dp0[a][b][l]: ends with l consecutive zeros (last element is 0)
        # dp1[a][b][l]: ends with l consecutive ones (last element is 1)
        dp0 = [[[0] * (limit + 1) for _ in range(one + 1)] for __ in range(zero + 1)]
        dp1 = [[[0] * (limit + 1) for _ in range(one + 1)] for __ in range(zero + 1)]

        if zero > 0:
            dp0[1][0][1] = 1
        if one > 0:
            dp1[0][1][1] = 1

        for a in range(zero + 1):
            for b in range(one + 1):
                # transitions from states ending with 0
                for l in range(1, limit + 1):
                    val = dp0[a][b][l]
                    if not val:
                        continue
                    # add another 0
                    if a < zero and l < limit:
                        dp0[a + 1][b][l + 1] = (dp0[a + 1][b][l + 1] + val) % MOD
                    # add a 1
                    if b < one:
                        dp1[a][b + 1][1] = (dp1[a][b + 1][1] + val) % MOD

                # transitions from states ending with 1
                for l in range(1, limit + 1):
                    val = dp1[a][b][l]
                    if not val:
                        continue
                    # add another 1
                    if b < one and l < limit:
                        dp1[a][b + 1][l + 1] = (dp1[a][b + 1][l + 1] + val) % MOD
                    # add a 0
                    if a < zero:
                        dp0[a + 1][b][1] = (dp0[a + 1][b][1] + val) % MOD

        ans = 0
        for l in range(1, limit + 1):
            ans = (ans + dp0[zero][one][l]) % MOD
            ans = (ans + dp1[zero][one][l]) % MOD
        return ans
```

## Python3

```python
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        # dp0[a][b][l]: ends with 0, run length l
        dp0 = [[[0] * (limit + 1) for _ in range(one + 1)] for __ in range(zero + 1)]
        # dp1[a][b][l]: ends with 1, run length l
        dp1 = [[[0] * (limit + 1) for _ in range(one + 1)] for __ in range(zero + 1)]

        if zero > 0:
            dp0[1][0][1] = 1
        if one > 0:
            dp1[0][1][1] = 1

        for a in range(zero + 1):
            for b in range(one + 1):
                # transitions from ending with 0
                cur0 = dp0[a][b]
                for l in range(1, limit + 1):
                    val = cur0[l]
                    if not val:
                        continue
                    # add another 0
                    if a < zero and l + 1 <= limit:
                        dp0[a + 1][b][l + 1] = (dp0[a + 1][b][l + 1] + val) % MOD
                    # add a 1, start new run length 1
                    if b < one:
                        dp1[a][b + 1][1] = (dp1[a][b + 1][1] + val) % MOD

                # transitions from ending with 1
                cur1 = dp1[a][b]
                for l in range(1, limit + 1):
                    val = cur1[l]
                    if not val:
                        continue
                    # add another 1
                    if b < one and l + 1 <= limit:
                        dp1[a][b + 1][l + 1] = (dp1[a][b + 1][l + 1] + val) % MOD
                    # add a 0, start new run length 1
                    if a < zero:
                        dp0[a + 1][b][1] = (dp0[a + 1][b][1] + val) % MOD

        ans = 0
        for l in range(1, limit + 1):
            ans = (ans + dp0[zero][one][l]) % MOD
            ans = (ans + dp1[zero][one][l]) % MOD
        return ans
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

const int MOD = 1000000007;

int numberOfStableArrays(int zero, int one, int limit) {
    static int dp[201][201][2][201];
    memset(dp, 0, sizeof(dp));
    if (zero > 0) dp[1][0][0][1] = 1;
    if (one > 0) dp[0][1][1][1] = 1;

    for (int z = 0; z <= zero; ++z) {
        for (int o = 0; o <= one; ++o) {
            for (int last = 0; last < 2; ++last) {
                for (int len = 1; len <= limit; ++len) {
                    int cur = dp[z][o][last][len];
                    if (!cur) continue;
                    // add same value
                    if (last == 0) {
                        if (z < zero && len < limit) {
                            int &ref = dp[z + 1][o][0][len + 1];
                            ref += cur;
                            if (ref >= MOD) ref -= MOD;
                        }
                        // add opposite value
                        if (o < one) {
                            int &ref = dp[z][o + 1][1][1];
                            ref += cur;
                            if (ref >= MOD) ref -= MOD;
                        }
                    } else { // last == 1
                        if (o < one && len < limit) {
                            int &ref = dp[z][o + 1][1][len + 1];
                            ref += cur;
                            if (ref >= MOD) ref -= MOD;
                        }
                        if (z < zero) {
                            int &ref = dp[z + 1][o][0][1];
                            ref += cur;
                            if (ref >= MOD) ref -= MOD;
                        }
                    }
                }
            }
        }
    }

    long long ans = 0;
    for (int last = 0; last < 2; ++last)
        for (int len = 1; len <= limit; ++len)
            ans = (ans + dp[zero][one][last][len]) % MOD;

    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int NumberOfStableArrays(int zero, int one, int limit) {
        const int MOD = 1000000007;
        var dp = new int[zero + 1, one + 1, 2, limit + 1];

        if (zero > 0) dp[1, 0, 0, 1] = 1;
        if (one > 0) dp[0, 1, 1, 1] = 1;

        for (int z = 0; z <= zero; ++z) {
            for (int o = 0; o <= one; ++o) {
                for (int last = 0; last < 2; ++last) {
                    for (int len = 1; len <= limit; ++len) {
                        int cur = dp[z, o, last, len];
                        if (cur == 0) continue;

                        if (last == 0) {
                            // add another 0
                            if (z < zero && len < limit) {
                                int val = dp[z + 1, o, 0, len + 1] + cur;
                                if (val >= MOD) val -= MOD;
                                dp[z + 1, o, 0, len + 1] = val;
                            }
                            // add a 1
                            if (o < one) {
                                int val = dp[z, o + 1, 1, 1] + cur;
                                if (val >= MOD) val -= MOD;
                                dp[z, o + 1, 1, 1] = val;
                            }
                        } else { // last == 1
                            // add another 1
                            if (o < one && len < limit) {
                                int val = dp[z, o + 1, 1, len + 1] + cur;
                                if (val >= MOD) val -= MOD;
                                dp[z, o + 1, 1, len + 1] = val;
                            }
                            // add a 0
                            if (z < zero) {
                                int val = dp[z + 1, o, 0, 1] + cur;
                                if (val >= MOD) val -= MOD;
                                dp[z + 1, o, 0, 1] = val;
                            }
                        }
                    }
                }
            }
        }

        long ans = 0;
        for (int last = 0; last < 2; ++last) {
            for (int len = 1; len <= limit; ++len) {
                ans += dp[zero, one, last, len];
            }
        }
        return (int)(ans % MOD);
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
    // dp[z][o][last] -> Uint32Array of length limit+1 (index by run length)
    const dp = Array.from({length: zero + 1}, () =>
        Array.from({length: one + 1}, () => [new Uint32Array(limit + 1), new Uint32Array(limit + 1)])
    );

    if (zero > 0) dp[1][0][0][1] = 1;
    if (one > 0) dp[0][1][1][1] = 1;

    for (let z = 0; z <= zero; ++z) {
        for (let o = 0; o <= one; ++o) {
            const arrZero = dp[z][o][0];
            const arrOne  = dp[z][o][1];
            for (let len = 1; len <= limit; ++len) {
                let val = arrZero[len];
                if (val) {
                    // add another 0
                    if (z < zero && len + 1 <= limit) {
                        const nxt = dp[z + 1][o][0];
                        nxt[len + 1] = (nxt[len + 1] + val) % MOD;
                    }
                    // switch to 1
                    if (o < one) {
                        const nxt = dp[z][o + 1][1];
                        nxt[1] = (nxt[1] + val) % MOD;
                    }
                }
                val = arrOne[len];
                if (val) {
                    // add another 1
                    if (o < one && len + 1 <= limit) {
                        const nxt = dp[z][o + 1][1];
                        nxt[len + 1] = (nxt[len + 1] + val) % MOD;
                    }
                    // switch to 0
                    if (z < zero) {
                        const nxt = dp[z + 1][o][0];
                        nxt[1] = (nxt[1] + val) % MOD;
                    }
                }
            }
        }
    }

    let ans = 0;
    for (let last = 0; last < 2; ++last) {
        const arr = dp[zero][one][last];
        for (let len = 1; len <= limit; ++len) {
            ans += arr[len];
            if (ans >= MOD) ans -= MOD;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function numberOfStableArrays(zero: number, one: number, limit: number): number {
    const MOD = 1_000_000_007;
    // dp[a][b][c][len] : c=0 ends with 0, c=1 ends with 1, len is current run length (1..limit)
    const dp: number[][][] = Array.from({ length: zero + 1 }, () =>
        Array.from({ length: one + 1 }, () => [
            new Array(limit + 1).fill(0), // ending with 0
            new Array(limit + 1).fill(0)  // ending with 1
        ])
    );

    if (zero > 0) dp[1][0][0][1] = 1;
    if (one > 0) dp[0][1][1][1] = 1;

    for (let a = 0; a <= zero; ++a) {
        for (let b = 0; b <= one; ++b) {
            // end with 0
            const arr0 = dp[a][b][0];
            for (let len = 1; len <= limit; ++len) {
                const val = arr0[len];
                if (!val) continue;
                // add another 0
                if (a + 1 <= zero && len + 1 <= limit) {
                    dp[a + 1][b][0][len + 1] = (dp[a + 1][b][0][len + 1] + val) % MOD;
                }
                // add a 1
                if (b + 1 <= one) {
                    dp[a][b + 1][1][1] = (dp[a][b + 1][1][1] + val) % MOD;
                }
            }
            // end with 1
            const arr1 = dp[a][b][1];
            for (let len = 1; len <= limit; ++len) {
                const val = arr1[len];
                if (!val) continue;
                // add another 1
                if (b + 1 <= one && len + 1 <= limit) {
                    dp[a][b + 1][1][len + 1] = (dp[a][b + 1][1][len + 1] + val) % MOD;
                }
                // add a 0
                if (a + 1 <= zero) {
                    dp[a + 1][b][0][1] = (dp[a + 1][b][0][1] + val) % MOD;
                }
            }
        }
    }

    let ans = 0;
    for (let c = 0; c < 2; ++c) {
        const arr = dp[zero][one][c];
        for (let len = 1; len <= limit; ++len) {
            ans += arr[len];
            if (ans >= MOD) ans -= MOD;
        }
    }
    return ans % MOD;
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
        $MOD = 1000000007;

        // previous layer for a-1 (zeros used)
        $dp0PrevZero = array_fill(0, $one + 1, null);
        $tot0PrevZero = array_fill(0, $one + 1, 0);
        $tot1PrevZero = array_fill(0, $one + 1, 0);
        for ($b = 0; $b <= $one; $b++) {
            $dp0PrevZero[$b] = array_fill(0, $limit + 1, 0);
        }

        // iterate over number of zeros used
        for ($a = 0; $a <= $zero; $a++) {
            $dp0Curr = array_fill(0, $one + 1, null);
            $dp1Curr = array_fill(0, $one + 1, null);
            $tot0Curr = array_fill(0, $one + 1, 0);
            $tot1Curr = array_fill(0, $one + 1, 0);

            for ($b = 0; $b <= $one; $b++) {
                if ($a == 0 && $b == 0) {
                    $dp0Curr[$b] = array_fill(0, $limit + 1, 0);
                    $dp1Curr[$b] = array_fill(0, $limit + 1, 0);
                    continue;
                }

                // dp for ending with 0
                $arr0 = array_fill(0, $limit + 1, 0);
                if ($a > 0) {
                    $prevArr0 = $dp0PrevZero[$b];
                    for ($k = 2; $k <= $limit; $k++) {
                        $arr0[$k] = $prevArr0[$k - 1];
                    }
                    $arr0[1] = $tot1PrevZero[$b];
                    if ($a == 1 && $b == 0) {
                        $arr0[1] = ($arr0[1] + 1) % $MOD;
                    }
                }

                // dp for ending with 1
                $arr1 = array_fill(0, $limit + 1, 0);
                if ($b > 0) {
                    $prevArr1 = $dp1Curr[$b - 1];
                    for ($k = 2; $k <= $limit; $k++) {
                        $arr1[$k] = $prevArr1[$k - 1];
                    }
                    $arr1[1] = $tot0Curr[$b - 1];
                    if ($a == 0 && $b == 1) {
                        $arr1[1] = ($arr1[1] + 1) % $MOD;
                    }
                }

                $dp0Curr[$b] = $arr0;
                $dp1Curr[$b] = $arr1;

                // compute totals for this (a,b)
                $sum0 = 0;
                $sum1 = 0;
                for ($k = 1; $k <= $limit; $k++) {
                    $sum0 += $arr0[$k];
                    if ($sum0 >= $MOD) $sum0 -= $MOD;
                    $sum1 += $arr1[$k];
                    if ($sum1 >= $MOD) $sum1 -= $MOD;
                }
                $tot0Curr[$b] = $sum0 % $MOD;
                $tot1Curr[$b] = $sum1 % $MOD;
            }

            // prepare for next a
            $dp0PrevZero = $dp0Curr;
            $tot0PrevZero = $tot0Curr;
            $tot1PrevZero = $tot1Curr;
        }

        return ($tot0Curr[$one] + $tot1Curr[$one]) % $MOD;
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    private let MOD = 1_000_000_007
    
    func numberOfStableArrays(_ zero: Int, _ one: Int, _ limit: Int) -> Int {
        if zero == 0 && one == 0 { return 0 }
        // dp[last][a][b][run]
        var dp0 = Array(repeating: Array(repeating: Array(repeating: 0, count: limit + 1), count: one + 1), count: zero + 1)
        var dp1 = Array(repeating: Array(repeating: Array(repeating: 0, count: limit + 1), count: one + 1), count: zero + 1)
        
        if zero > 0 { dp0[1][0][1] = 1 }
        if one > 0 { dp1[0][1][1] = 1 }
        
        for a in 0...zero {
            for b in 0...one {
                // last = 0
                if a <= zero && b <= one {
                    for run in 1...limit {
                        let val = dp0[a][b][run]
                        if val == 0 { continue }
                        // add another 0
                        if a < zero && run < limit {
                            var newVal = dp0[a + 1][b][run + 1] + val
                            if newVal >= MOD { newVal -= MOD }
                            dp0[a + 1][b][run + 1] = newVal
                        }
                        // add a 1
                        if b < one {
                            var newVal = dp1[a][b + 1][1] + val
                            if newVal >= MOD { newVal -= MOD }
                            dp1[a][b + 1][1] = newVal
                        }
                    }
                }
                
                // last = 1
                for run in 1...limit {
                    let val = dp1[a][b][run]
                    if val == 0 { continue }
                    // add another 1
                    if b < one && run < limit {
                        var newVal = dp1[a][b + 1][run + 1] + val
                        if newVal >= MOD { newVal -= MOD }
                        dp1[a][b + 1][run + 1] = newVal
                    }
                    // add a 0
                    if a < zero {
                        var newVal = dp0[a + 1][b][1] + val
                        if newVal >= MOD { newVal -= MOD }
                        dp0[a + 1][b][1] = newVal
                    }
                }
            }
        }
        
        var ans = 0
        for run in 1...limit {
            ans += dp0[zero][one][run]
            if ans >= MOD { ans -= MOD }
            ans += dp1[zero][one][run]
            if ans >= MOD { ans -= MOD }
        }
        return ans % MOD
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfStableArrays(zero: Int, one: Int, limit: Int): Int {
        val MOD = 1_000_000_007
        val sizeA = zero + 1
        val sizeB = one + 1
        val sizeC = 2
        val sizeLen = limit + 1
        val totalSize = sizeA * sizeB * sizeC * sizeLen
        val dp = IntArray(totalSize)

        fun idx(a: Int, b: Int, c: Int, len: Int): Int {
            return (((a * sizeB) + b) * sizeC + c) * sizeLen + len
        }

        if (zero > 0) dp[idx(1, 0, 0, 1)] = 1
        if (one > 0) dp[idx(0, 1, 1, 1)] = 1

        for (a in 0..zero) {
            for (b in 0..one) {
                for (c in 0..1) {
                    for (len in 1..limit) {
                        val cur = dp[idx(a, b, c, len)]
                        if (cur == 0) continue
                        if (c == 0) {
                            // add another 0
                            if (len < limit && a + 1 <= zero) {
                                val ni = idx(a + 1, b, 0, len + 1)
                                var v = dp[ni] + cur
                                if (v >= MOD) v -= MOD
                                dp[ni] = v
                            }
                            // switch to 1
                            if (b + 1 <= one) {
                                val ni = idx(a, b + 1, 1, 1)
                                var v = dp[ni] + cur
                                if (v >= MOD) v -= MOD
                                dp[ni] = v
                            }
                        } else { // c == 1
                            // add another 1
                            if (len < limit && b + 1 <= one) {
                                val ni = idx(a, b + 1, 1, len + 1)
                                var v = dp[ni] + cur
                                if (v >= MOD) v -= MOD
                                dp[ni] = v
                            }
                            // switch to 0
                            if (a + 1 <= zero) {
                                val ni = idx(a + 1, b, 0, 1)
                                var v = dp[ni] + cur
                                if (v >= MOD) v -= MOD
                                dp[ni] = v
                            }
                        }
                    }
                }
            }
        }

        var ans = 0L
        for (c in 0..1) {
            for (len in 1..limit) {
                ans += dp[idx(zero, one, c, len)]
                if (ans >= MOD) ans -= MOD
            }
        }
        return (ans % MOD).toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int numberOfStableArrays(int zero, int one, int limit) {
    // dp[a][b][c][len] where c:0->last is 0, 1->last is 1, len: current run length (1..limit)
    List<List<List<List<int>>>> dp = List.generate(
        zero + 1,
        (_) => List.generate(
            one + 1,
            (_) => List.generate(2, (_) => List.filled(limit + 1, 0))));

    if (zero > 0) dp[1][0][0][1] = 1;
    if (one > 0) dp[0][1][1][1] = 1;

    for (int a = 0; a <= zero; ++a) {
      for (int b = 0; b <= one; ++b) {
        for (int c = 0; c < 2; ++c) {
          for (int len = 1; len <= limit; ++len) {
            int cur = dp[a][b][c][len];
            if (cur == 0) continue;

            // Append opposite value
            if (c == 0 && b < one) {
              int nb = b + 1;
              dp[a][nb][1][1] = (dp[a][nb][1][1] + cur) % _mod;
            } else if (c == 1 && a < zero) {
              int na = a + 1;
              dp[na][b][0][1] = (dp[na][b][0][1] + cur) % _mod;
            }

            // Append same value if run length permits
            if (len < limit) {
              if (c == 0 && a < zero) {
                int na = a + 1;
                dp[na][b][0][len + 1] =
                    (dp[na][b][0][len + 1] + cur) % _mod;
              } else if (c == 1 && b < one) {
                int nb = b + 1;
                dp[a][nb][1][len + 1] =
                    (dp[a][nb][1][len + 1] + cur) % _mod;
              }
            }
          }
        }
      }
    }

    int ans = 0;
    for (int c = 0; c < 2; ++c) {
      for (int len = 1; len <= limit; ++len) {
        ans = (ans + dp[zero][one][c][len]) % _mod;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func numberOfStableArrays(zero int, one int, limit int) int {
	const MOD = 1000000007
	// dp0[a][b][l]: ends with 0, using a zeros, b ones, current run length l (1..limit)
	// dp1 similar for ending with 1
	dp0 := make([][][]int, zero+1)
	dp1 := make([][][]int, zero+1)
	for i := 0; i <= zero; i++ {
		dp0[i] = make([][]int, one+1)
		dp1[i] = make([][]int, one+1)
		for j := 0; j <= one; j++ {
			dp0[i][j] = make([]int, limit+1)
			dp1[i][j] = make([]int, limit+1)
		}
	}
	if zero > 0 {
		dp0[1][0][1] = 1
	}
	if one > 0 {
		dp1[0][1][1] = 1
	}

	for a := 0; a <= zero; a++ {
		for b := 0; b <= one; b++ {
			// transitions from states ending with 0
			for l := 1; l <= limit; l++ {
				val := dp0[a][b][l]
				if val == 0 {
					continue
				}
				// add another 0 if run length permits and zeros remain
				if a+1 <= zero && l < limit {
					dp0[a+1][b][l+1] = (dp0[a+1][b][l+1] + val) % MOD
				}
				// switch to 1
				if b+1 <= one {
					dp1[a][b+1][1] = (dp1[a][b+1][1] + val) % MOD
				}
			}
			// transitions from states ending with 1
			for l := 1; l <= limit; l++ {
				val := dp1[a][b][l]
				if val == 0 {
					continue
				}
				// add another 1 if run length permits and ones remain
				if b+1 <= one && l < limit {
					dp1[a][b+1][l+1] = (dp1[a][b+1][l+1] + val) % MOD
				}
				// switch to 0
				if a+1 <= zero {
					dp0[a+1][b][1] = (dp0[a+1][b][1] + val) % MOD
				}
			}
		}
	}

	ans := 0
	for l := 1; l <= limit; l++ {
		ans = (ans + dp0[zero][one][l]) % MOD
		ans = (ans + dp1[zero][one][l]) % MOD
	}
	return ans
}
```

## Ruby

```ruby
def number_of_stable_arrays(zero, one, limit)
  mod = 1_000_000_007
  dp0 = Array.new(zero + 1) { Array.new(one + 1) { Array.new(limit + 1, 0) } }
  dp1 = Array.new(zero + 1) { Array.new(one + 1) { Array.new(limit + 1, 0) } }

  dp0[1][0][1] = 1 if zero > 0
  dp1[0][1][1] = 1 if one > 0

  (0..zero).each do |a|
    (0..one).each do |b|
      (1..limit).each do |len|
        val = dp0[a][b][len]
        unless val.zero?
          # add another 0
          if a + 1 <= zero && len + 1 <= limit
            dp0[a + 1][b][len + 1] = (dp0[a + 1][b][len + 1] + val) % mod
          end
          # switch to 1
          if b + 1 <= one
            dp1[a][b + 1][1] = (dp1[a][b + 1][1] + val) % mod
          end
        end

        val = dp1[a][b][len]
        unless val.zero?
          # add another 1
          if b + 1 <= one && len + 1 <= limit
            dp1[a][b + 1][len + 1] = (dp1[a][b + 1][len + 1] + val) % mod
          end
          # switch to 0
          if a + 1 <= zero
            dp0[a + 1][b][1] = (dp0[a + 1][b][1] + val) % mod
          end
        end
      end
    end
  end

  ans = 0
  (1..limit).each do |len|
    ans = (ans + dp0[zero][one][len]) % mod
    ans = (ans + dp1[zero][one][len]) % mod
  end
  ans
end
```

## Scala

```scala
object Solution {
  def numberOfStableArrays(zero: Int, one: Int, limit: Int): Int = {
    val MOD = 1000000007
    val maxZ = zero
    val maxO = one
    val L = limit

    // dp[z][o][last][len] : number of ways using z zeros, o ones,
    // ending with 'last' (0 or 1) having a current run length 'len'
    val dp = Array.ofDim[Int](maxZ + 1, maxO + 1, 2, L + 1)

    if (zero > 0) dp(1)(0)(0)(1) = 1
    if (one > 0) dp(0)(1)(1)(1) = 1

    for (z <- 0 to maxZ) {
      for (o <- 0 to maxO) {
        for (last <- 0 to 1) {
          var len = 1
          while (len <= L) {
            val cur = dp(z)(o)(last)(len)
            if (cur != 0) {
              if (last == 0) {
                // add another zero
                if (z < maxZ && len < L) {
                  var v = dp(z + 1)(o)(0)(len + 1).toLong + cur
                  if (v >= MOD) v -= MOD
                  dp(z + 1)(o)(0)(len + 1) = v.toInt
                }
                // add a one, start new run
                if (o < maxO) {
                  var v = dp(z)(o + 1)(1)(1).toLong + cur
                  if (v >= MOD) v -= MOD
                  dp(z)(o + 1)(1)(1) = v.toInt
                }
              } else { // last == 1
                // add another one
                if (o < maxO && len < L) {
                  var v = dp(z)(o + 1)(1)(len + 1).toLong + cur
                  if (v >= MOD) v -= MOD
                  dp(z)(o + 1)(1)(len + 1) = v.toInt
                }
                // add a zero, start new run
                if (z < maxZ) {
                  var v = dp(z + 1)(o)(0)(1).toLong + cur
                  if (v >= MOD) v -= MOD
                  dp(z + 1)(o)(0)(1) = v.toInt
                }
              }
            }
            len += 1
          }
        }
      }
    }

    var ans = 0L
    for (last <- 0 to 1) {
      var len = 1
      while (len <= L) {
        ans += dp(zero)(one)(last)(len)
        if (ans >= MOD) ans -= MOD
        len += 1
      }
    }
    ans.toInt
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
        let l = limit as usize;

        // total size: (z+1)*(o+1)*2*(l+1)
        let total = (z + 1) * (o + 1) * 2 * (l + 1);
        let mut dp = vec![0i64; total];

        // helper to compute flat index
        let idx = |a: usize, b: usize, c: usize, d: usize| -> usize {
            ((a * (o + 1) + b) * 2 + c) * (l + 1) + d
        };

        if z > 0 {
            dp[idx(1, 0, 0, 1)] = 1;
        }
        if o > 0 {
            dp[idx(0, 1, 1, 1)] = 1;
        }

        for a in 0..=z {
            for b in 0..=o {
                for c in 0..2 {
                    for d in 1..=l {
                        let cur = dp[idx(a, b, c, d)];
                        if cur == 0 {
                            continue;
                        }
                        if c == 0 {
                            // add another 0
                            if a < z && d + 1 <= l {
                                let na = a + 1;
                                let nd = d + 1;
                                let pos = idx(na, b, 0, nd);
                                dp[pos] = (dp[pos] + cur) % MOD;
                            }
                            // switch to 1
                            if b < o {
                                let nb = b + 1;
                                let pos = idx(a, nb, 1, 1);
                                dp[pos] = (dp[pos] + cur) % MOD;
                            }
                        } else {
                            // c == 1
                            // add another 1
                            if b < o && d + 1 <= l {
                                let nb = b + 1;
                                let nd = d + 1;
                                let pos = idx(a, nb, 1, nd);
                                dp[pos] = (dp[pos] + cur) % MOD;
                            }
                            // switch to 0
                            if a < z {
                                let na = a + 1;
                                let pos = idx(na, b, 0, 1);
                                dp[pos] = (dp[pos] + cur) % MOD;
                            }
                        }
                    }
                }
            }
        }

        let mut ans: i64 = 0;
        for c in 0..2 {
            for d in 1..=l {
                ans = (ans + dp[idx(z, o, c, d)]) % MOD;
            }
        }
        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

;; create a 3‑dimensional vector: [0..z] × [0..o] × [0..l] initialized to 0
(define (make-3d zmax omax lmax)
  (let ([v (make-vector (add1 zmax))])
    (for ([i (in-range (add1 zmax))])
      (let ([row (make-vector (add1 omax))])
        (vector-set! v i row)
        (for ([j (in-range (add1 omax))])
          (vector-set! row j (make-vector (add1 lmax) 0)))))
    v))

(define (add-mod! vec idx delta)
  (let ([new (+ (vector-ref vec idx) delta)])
    (when (>= new MOD) (set! new (- new MOD)))
    (vector-set! vec idx new)))

(define/contract (number-of-stable-arrays zero one limit)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  (let* ([dp0 (make-3d zero one limit)]
         [dp1 (make-3d zero one limit)])
    ;; base cases: start with a single 0 or 1
    (when (> zero 0)
      (let* ([row (vector-ref dp0 1)]
             [col (vector-ref row 0)])
        (vector-set! col 1 1)))
    (when (> one 0)
      (let* ([row (vector-ref dp1 0)]
             [col (vector-ref row 1)])
        (vector-set! col 1 1)))

    ;; DP transitions
    (for ([z (in-range (add1 zero))])
      (for ([o (in-range (add1 one))])
        (let* ([row0 (vector-ref dp0 z)]
               [row1 (vector-ref dp1 z)])
          (for ([len (in-range 1 (add1 limit))])
            ;; ending with 0
            (let* ([col0 (vector-ref row0 o)]
                   [val0 (vector-ref col0 len)])
              (when (> val0 0)
                ;; add another 0 if run length permits
                (when (and (< z zero) (< len limit))
                  (let* ([next-row (vector-ref dp0 (+ z 1))]
                         [next-col (vector-ref next-row o)]
                         [nlen (+ len 1)])
                    (add-mod! next-col nlen val0)))
                ;; add a 1, start new run
                (when (< o one)
                  (let* ([next-row (vector-ref dp1 z)]
                         [next-col (vector-ref next-row (+ o 1))])
                    (add-mod! next-col 1 val0)))))
            ;; ending with 1
            (let* ([col1 (vector-ref row1 o)]
                   [val1 (vector-ref col1 len)])
              (when (> val1 0)
                ;; add another 1 if run length permits
                (when (and (< o one) (< len limit))
                  (let* ([next-row (vector-ref dp1 z)]
                         [next-col (vector-ref next-row (+ o 1))]
                         [nlen (+ len 1)])
                    (add-mod! next-col nlen val1)))
                ;; add a 0, start new run
                (when (< z zero)
                  (let* ([next-row (vector-ref dp0 (+ z 1))]
                         [next-col (vector-ref next-row o)])
                    (add-mod! next-col 1 val1)))))))))

    ;; sum over all possible ending run lengths
    (let ([ans 0])
      (let ([row0 (vector-ref dp0 zero)]
            [row1 (vector-ref dp1 zero)])
        (for ([len (in-range 1 (add1 limit))])
          (set! ans (+ ans (vector-ref (vector-ref row0 one) len)))
          (when (>= ans MOD) (set! ans (- ans MOD)))
          (set! ans (+ ans (vector-ref (vector-ref row1 one) len)))
          (when (>= ans MOD) (set! ans (- ans MOD)))))
      ans)))
```

## Erlang

```erlang
-module(solution).
-export([number_of_stable_arrays/3]).

-define(MOD, 1000000007).

number_of_stable_arrays(Zero, One, Limit) ->
    DPZ = build_dp(Zero, Limit),
    DPO = build_dp(One, Limit),
    lists:foldl(fun(Nz, Acc1) ->
        WaysZ = maps:get({Nz, Zero}, DPZ, 0),
        if WaysZ == 0 -> Acc1;
           true ->
               lists:foldl(fun(No, Acc2) ->
                   WaysO = maps:get({No, One}, DPO, 0),
                   case WaysO of
                       0 -> Acc2;
                       _ ->
                           Factor = factor(Nz, No),
                           Add = ((WaysZ * WaysO) rem ?MOD) * Factor rem ?MOD,
                           (Acc2 + Add) rem ?MOD
                   end
               end, Acc1, lists:seq(1, One))
        end
    end, 0, lists:seq(1, Zero)).

factor(Nz, No) when Nz == No -> 2;
factor(Nz, No) when Nz == No + 1 -> 1;
factor(Nz, No) when No == Nz + 1 -> 1;
factor(_, _) -> 0.

build_dp(Total, Limit) ->
    BaseMap = maps:put({0,0}, 1, maps:new()),
    build_dp_iter(1, Total, Limit, BaseMap).

build_dp_iter(N, Total, _Limit, Map) when N > Total ->
    Map;
build_dp_iter(N, Total, Limit, Map) ->
    NewMap = lists:foldl(fun(S, AccMap) ->
        Val = sum_len(N-1, S, Limit, AccMap),
        if Val == 0 -> AccMap; true -> maps:put({N,S}, Val, AccMap) end
    end, Map, lists:seq(0, Total)),
    build_dp_iter(N+1, Total, Limit, NewMap).

sum_len(PrevN, S, Limit, Map) ->
    MaxLen = min(Limit, S),
    sum_len_loop(1, MaxLen, PrevN, S, Map, 0).

sum_len_loop(Len, MaxLen, _PrevN, _S, _Map, Acc) when Len > MaxLen ->
    Acc;
sum_len_loop(Len, MaxLen, PrevN, S, Map, Acc) ->
    Val = maps:get({PrevN, S - Len}, Map, 0),
    NewAcc = (Acc + Val) rem ?MOD,
    sum_len_loop(Len + 1, MaxLen, PrevN, S, Map, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @spec number_of_stable_arrays(zero :: integer, one :: integer, limit :: integer) :: integer
  def number_of_stable_arrays(zero, one, limit) do
    mod = 1_000_000_007
    :ets.new(:dp_table, [:named_table, :public, read_concurrency: true])

    total =
      (if zero > 0, do: dfs(zero - 1, one, 0, 1, limit, mod), else: 0) +
        (if one > 0, do: dfs(zero, one - 1, 1, 1, limit, mod), else: 0)

    :ets.delete(:dp_table)
    rem(total, mod)
  end

  defp dfs(z, o, last, run, limit, mod) do
    case :ets.lookup(:dp_table, {z, o, last, run}) do
      [{_, val}] ->
        val

      [] ->
        val =
          if z == 0 and o == 0 do
            1
          else
            cond do
              last == 0 ->
                s1 = if z > 0 and run < limit, do: dfs(z - 1, o, 0, run + 1, limit, mod), else: 0
                s2 = if o > 0, do: dfs(z, o - 1, 1, 1, limit, mod), else: 0
                rem(s1 + s2, mod)

              true ->
                # last == 1
                s1 = if o > 0 and run < limit, do: dfs(z, o - 1, 1, run + 1, limit, mod), else: 0
                s2 = if z > 0, do: dfs(z - 1, o, 0, 1, limit, mod), else: 0
                rem(s1 + s2, mod)
            end
          end

        :ets.insert(:dp_table, {{z, o, last, run}, val})
        val
    end
  end
end
```
