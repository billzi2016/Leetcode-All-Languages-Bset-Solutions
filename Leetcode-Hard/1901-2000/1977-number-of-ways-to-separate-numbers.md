# 1977. Number of Ways to Separate Numbers

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numberOfCombinations(string num) {
        const int MOD = 1'000'000'007;
        int n = (int)num.size();
        // LCP array
        vector<vector<int>> lcp(n + 1, vector<int>(n + 1, 0));
        for (int i = n - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                if (num[i] == num[j]) lcp[i][j] = 1 + lcp[i + 1][j + 1];
                else lcp[i][j] = 0;
            }
        }

        // dp[i][len]: ways for suffix starting at i with first number length len
        vector<vector<int>> dp(n, vector<int>(n + 2, 0));
        // sum[i][len]: suffix sums of dp[i][*] from len to end
        vector<vector<int>> sum(n, vector<int>(n + 3, 0));

        for (int i = n - 1; i >= 0; --i) {
            if (num[i] == '0') continue; // all dp[i][*] stay zero
            int maxLen = n - i;
            for (int len = 1; len <= maxLen; ++len) {
                int j = i + len;
                if (j == n) {
                    dp[i][len] = 1;
                } else {
                    long long val = 0;
                    // longer next numbers are always larger
                    if (len + 1 <= n - j) val += sum[j][len + 1];
                    // equal length case: need current <= next
                    bool leq = false;
                    int common = lcp[i][j];
                    if (common >= len) {
                        leq = true; // identical substrings
                    } else {
                        if (num[i + common] < num[j + common]) leq = true;
                    }
                    if (leq) val += dp[j][len];
                    dp[i][len] = (int)(val % MOD);
                }
            }
            // compute suffix sums for position i
            sum[i][maxLen + 1] = 0;
            for (int len = maxLen; len >= 1; --len) {
                int cur = dp[i][len];
                int nxt = sum[i][len + 1];
                int s = cur + nxt;
                if (s >= MOD) s -= MOD;
                sum[i][len] = s;
            }
        }

        return sum[0][1] % MOD;
    }
};
```

## Java

```java
class Solution {
    public int numberOfCombinations(String num) {
        final int MOD = 1_000_000_007;
        int n = num.length();
        char[] s = num.toCharArray();

        // LCP array
        int[][] lcp = new int[n + 1][n + 1];
        for (int i = n - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                if (s[i] == s[j]) {
                    lcp[i][j] = lcp[i + 1][j + 1] + 1;
                }
            }
        }

        int[][] dp = new int[n + 1][n + 1];
        int[][] pref = new int[n + 1][n + 1]; // prefix sums of dp for each position

        for (int pos = 1; pos <= n; ++pos) {
            for (int len = 1; len <= pos; ++len) {
                int start = pos - len;
                if (s[start] == '0') continue; // leading zero not allowed
                if (start == 0) {
                    dp[pos][len] = 1; // whole prefix is a single number
                } else {
                    long ways = pref[start][Math.min(len - 1, start)];
                    // case when previous number has the same length
                    if (len <= start) {
                        int prevStart = start - len;
                        int common = lcp[prevStart][start];
                        boolean le;
                        if (common >= len) {
                            le = true; // equal
                        } else {
                            char a = s[prevStart + common];
                            char b = s[start + common];
                            le = a < b;
                        }
                        if (le) {
                            ways += dp[start][len];
                        }
                    }
                    dp[pos][len] = (int) (ways % MOD);
                }
            }
            // build prefix sums for current position
            int sum = 0;
            for (int len = 1; len <= pos; ++len) {
                sum += dp[pos][len];
                if (sum >= MOD) sum -= MOD;
                pref[pos][len] = sum;
            }
        }

        return pref[n][n] % MOD;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfCombinations(self, num):
        """
        :type num: str
        :rtype: int
        """
        MOD = 10**9 + 7
        s = num
        n = len(s)
        from array import array

        # LCP matrix using unsigned short (max length <= 3500)
        lcp = [array('H', [0]) * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            row_i = lcp[i]
            row_ip1 = lcp[i + 1]
            si = s[i]
            for j in range(n - 1, -1, -1):
                if si == s[j]:
                    row_i[j] = 1 + lcp[i + 1][j + 1]
                else:
                    row_i[j] = 0

        def leq(a, b, length):
            """return True if s[a:a+length] <= s[b:b+length]"""
            common = lcp[a][b]
            if common >= length:
                return True
            return s[a + common] < s[b + common]

        # dp[end][len] = ways for prefix of length end with last number length len
        dp = [array('I', [0]) * (n + 1) for _ in range(n + 1)]

        if n > 0 and s[0] != '0':
            for l in range(1, n + 1):
                dp[l][l] = 1

        for i in range(1, n):
            cur = dp[i]
            # prefix sums of cur
            pref = [0] * (n + 2)
            acc = 0
            for k in range(1, n + 1):
                acc += cur[k]
                if acc >= MOD:
                    acc -= MOD
                pref[k] = acc

            if s[i] == '0':
                continue
            max_len = n - i
            for l in range(1, max_len + 1):
                add = pref[l - 1]
                if i >= l:
                    val_eq = cur[l]
                    if val_eq and leq(i - l, i, l):
                        add += val_eq
                        if add >= MOD:
                            add -= MOD
                nxt = i + l
                dp[nxt][l] = (dp[nxt][l] + add) % MOD

        ans = 0
        for l in range(1, n + 1):
            ans += dp[n][l]
            if ans >= MOD:
                ans -= MOD
        return ans
```

## Python3

```python
import sys
from array import array

class Solution:
    def numberOfCombinations(self, num: str) -> int:
        MOD = 10**9 + 7
        n = len(num)
        # LCP using unsigned short (max length 3500 fits in 16 bits)
        lcp = [array('H', [0] * (n + 1)) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            row_i = lcp[i]
            row_ip1 = lcp[i + 1] if i + 1 < n else None
            for j in range(n - 1, -1, -1):
                if num[i] == num[j]:
                    nxt = row_ip1[j + 1] if (i + 1 < n and j + 1 < n) else 0
                    row_i[j] = nxt + 1

        # DP arrays: f[i][len] ways where last number has length len ending at i-1
        f = [array('I', [0] * (n + 1)) for _ in range(n + 1)]
        pref = [array('I', [0] * (n + 1)) for _ in range(n + 1)]

        for i in range(1, n + 1):
            cum = 0
            for d in range(1, i + 1):
                start = i - d
                if num[start] == '0':
                    # invalid number due to leading zero
                    val = 0
                else:
                    if start == 0:
                        val = 1
                    else:
                        total = pref[start][d - 1]  # previous lengths < d
                        extra = 0
                        if start - d >= 0:
                            a = start - d
                            b = start
                            common = lcp[a][b]
                            if common >= d or (common < d and num[a + common] < num[b + common]):
                                extra = f[start][d]
                        val = (total + extra) % MOD
                f[i][d] = val
                cum = (cum + val) % MOD
                pref[i][d] = cum

        return int(pref[n][n] % MOD)
```

## C

```c
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

int numberOfCombinations(char* num) {
    const int MOD = 1000000007;
    int n = (int)strlen(num);
    int N = n + 1;                         // size for LCP matrix

    // LCP[i][j] = longest common prefix of suffixes starting at i and j
    unsigned short *lcp = (unsigned short*)calloc(N * N, sizeof(unsigned short));
    for (int i = n - 1; i >= 0; --i) {
        for (int j = n - 1; j >= 0; --j) {
            if (num[i] == num[j]) {
                lcp[i * N + j] = (unsigned short)(1 + lcp[(i + 1) * N + (j + 1)]);
            } else {
                lcp[i * N + j] = 0;
            }
        }
    }

    // dp[i][len]: ways for substring starting at i with first number length len
    int **dp = (int**)malloc((n + 1) * sizeof(int*));
    int **suf = (int**)malloc((n + 1) * sizeof(int*));
    for (int i = 0; i <= n; ++i) {
        int sz = n - i;
        dp[i] = (int*)calloc(sz + 2, sizeof(int));   // index by len (1..sz)
        suf[i] = (int*)calloc(sz + 3, sizeof(int));  // suffix sums
    }

    for (int i = n - 1; i >= 0; --i) {
        int maxLen = n - i;
        for (int len = 1; len <= maxLen; ++len) {
            if (num[i] == '0') {          // leading zero not allowed
                dp[i][len] = 0;
                continue;
            }
            int j = i + len;              // start of next number
            if (j == n) {
                dp[i][len] = 1;           // last number
            } else {
                long long res = suf[j][len + 1];   // next number longer than current
                unsigned short common = lcp[i * N + j];
                bool le;
                if (common >= len) {               // equal strings
                    le = true;
                } else {
                    char c1 = num[i + common];
                    char c2 = num[j + common];
                    le = c1 < c2;                  // current <= next ?
                }
                if (le) {
                    res += dp[j][len];             // equal length and valid
                }
                dp[i][len] = (int)(res % MOD);
            }
        }
        // compute suffix sums for position i
        suf[i][maxLen + 1] = 0;
        for (int len = maxLen; len >= 1; --len) {
            int val = dp[i][len] + suf[i][len + 1];
            if (val >= MOD) val -= MOD;
            suf[i][len] = val;
        }
    }

    int answer = suf[0][1] % MOD;

    // clean up
    for (int i = 0; i <= n; ++i) {
        free(dp[i]);
        free(suf[i]);
    }
    free(dp);
    free(suf);
    free(lcp);

    return answer;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int NumberOfCombinations(string num) {
        const int MOD = 1000000007;
        int n = num.Length;
        // LCP array
        int[,] lcp = new int[n + 1, n + 1];
        for (int i = n - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                if (num[i] == num[j]) {
                    lcp[i, j] = 1 + lcp[i + 1, j + 1];
                } else {
                    lcp[i, j] = 0;
                }
            }
        }

        int[,] dp = new int[n + 1, n + 1];   // dp[end, len]
        int[,] pref = new int[n + 1, n + 1]; // prefix sums of dp for each end

        for (int end = 1; end <= n; ++end) {
            for (int curLen = 1; curLen <= end; ++curLen) {
                int start = end - curLen;
                if (num[start] == '0') continue; // leading zero not allowed

                long ways = 0;
                if (start == 0) {
                    ways = 1; // first number
                } else {
                    // previous length < current length -> always valid
                    int maxPrevLen = Math.Min(curLen - 1, start);
                    if (maxPrevLen > 0) {
                        ways += pref[start, maxPrevLen];
                    }

                    // previous length == current length -> need comparison
                    if (curLen <= start) {
                        int prevStart = start - curLen;
                        int common = lcp[prevStart, start];
                        bool leq;
                        if (common >= curLen) {
                            leq = true; // equal numbers
                        } else {
                            char cPrev = num[prevStart + common];
                            char cCurr = num[start + common];
                            leq = cPrev < cCurr;
                        }
                        if (leq) {
                            ways += dp[start, curLen];
                        }
                    }
                }

                dp[end, curLen] = (int)(ways % MOD);
            }

            // build prefix sums for this end position
            long cum = 0;
            for (int l = 1; l <= end; ++l) {
                cum += dp[end, l];
                if (cum >= MOD) cum -= MOD;
                pref[end, l] = (int)cum;
            }
        }

        return pref[n, n];
    }
}
```

## Javascript

```javascript
/**
 * @param {string} num
 * @return {number}
 */
var numberOfCombinations = function(num) {
    const MOD = 1000000007;
    const n = num.length;

    // LCP array: lcp[i][j] = longest common prefix length of suffixes starting at i and j
    const lcp = new Array(n + 1);
    lcp[n] = new Uint16Array(n + 1); // all zeros

    for (let i = n - 1; i >= 0; --i) {
        const row = new Uint16Array(n + 1);
        for (let j = n - 1; j >= 0; --j) {
            if (num[i] === num[j]) {
                row[j] = 1 + lcp[i + 1][j + 1];
            } // else remains 0
        }
        lcp[i] = row;
    }

    // dp[i][len]: ways for prefix of length i, last number has length len (i is exclusive)
    const dp = Array.from({ length: n + 1 }, () => new Uint32Array(n + 1));
    // pref[i][len]: cumulative sum of dp[i][1..len]
    const pref = Array.from({ length: n + 1 }, () => new Uint32Array(n + 1));

    for (let i = 1; i <= n; ++i) {
        for (let len = 1; len <= i; ++len) {
            const start = i - len;
            if (num[start] === '0') continue; // leading zero not allowed

            let val;
            if (start === 0) {
                // whole prefix is a single number
                val = 1;
            } else {
                // sum of ways where previous number length < len
                val = pref[start][len - 1];

                // equal length case
                if (start >= len) {
                    const prevStart = start - len;
                    const common = lcp[prevStart][start];
                    let leq;
                    if (common >= len) {
                        leq = true; // identical strings
                    } else {
                        leq = num.charCodeAt(prevStart + common) < num.charCodeAt(start + common);
                    }
                    if (leq) {
                        val += dp[start][len];
                        if (val >= MOD) val -= MOD;
                    }
                }
            }

            dp[i][len] = val % MOD;
            const cum = pref[i][len - 1] + dp[i][len];
            pref[i][len] = cum >= MOD ? cum - MOD : cum;
        }
    }

    return pref[n][n] % MOD;
};
```

## Typescript

```typescript
function numberOfCombinations(num: string): number {
    const MOD = 1_000_000_007;
    const n = num.length;
    const s = num;

    // LCP array
    const lcp: Uint16Array[] = new Array(n + 1);
    for (let i = 0; i <= n; i++) lcp[i] = new Uint16Array(n + 1);
    for (let i = n - 1; i >= 0; i--) {
        const ci = s.charCodeAt(i);
        for (let j = n - 1; j >= 0; j--) {
            if (ci === s.charCodeAt(j)) {
                lcp[i][j] = (lcp[i + 1][j + 1] + 1) as unknown as Uint16Array;
            } else {
                lcp[i][j] = 0;
            }
        }
    }

    // dp and prefix sums
    const f: number[][] = new Array(n);
    const cum: number[][] = new Array(n);
    for (let i = 0; i < n; i++) {
        f[i] = new Array(i + 2).fill(0);   // index by length
        cum[i] = new Array(i + 2).fill(0);
    }

    for (let i = 0; i < n; i++) {
        for (let len = 1; len <= i + 1; len++) {
            const start = i - len + 1;
            if (s.charCodeAt(start) === 48) continue; // leading zero not allowed

            if (start === 0) {
                f[i][len] = 1;
            } else {
                let ways = 0;
                const prevIdx = start - 1;

                // previous number shorter than current
                const maxPrevLen = Math.min(len - 1, start);
                if (maxPrevLen > 0) {
                    ways += cum[prevIdx][maxPrevLen];
                }

                // previous number same length
                if (len <= start) {
                    const prevStart = start - len;
                    const common = lcp[prevStart][start];
                    if (
                        common >= len ||
                        (common < len && s.charCodeAt(prevStart + common) < s.charCodeAt(start + common))
                    ) {
                        ways += f[prevIdx][len];
                    }
                }

                f[i][len] = ways % MOD;
            }
        }

        // build prefix sums for position i
        let running = 0;
        for (let l = 1; l <= i + 1; l++) {
            running = (running + f[i][l]) % MOD;
            cum[i][l] = running;
        }
    }

    return cum[n - 1][n] % MOD;
}
```

## Php

```php
class Solution {
    /**
     * @param String $num
     * @return Integer
     */
    function numberOfCombinations($num) {
        $MOD = 1000000007;
        $n = strlen($num);
        if ($n == 0) return 0;

        // hash parameters
        $base = 91138233;
        $mod1 = 1000000007;
        $mod2 = 1000000009;

        // prefix hashes and powers
        $h1 = array_fill(0, $n + 1, 0);
        $h2 = array_fill(0, $n + 1, 0);
        $pow1 = array_fill(0, $n + 1, 1);
        $pow2 = array_fill(0, $n + 1, 1);

        for ($i = 0; $i < $n; $i++) {
            $c = ord($num[$i]) - 48; // digit value
            $h1[$i + 1] = (int)(($h1[$i] * $base + $c) % $mod1);
            $h2[$i + 1] = (int)(($h2[$i] * $base + $c) % $mod2);
            $pow1[$i + 1] = (int)(($pow1[$i] * $base) % $mod1);
            $pow2[$i + 1] = (int)(($pow2[$i] * $base) % $mod2);
        }

        // helper to get hash of substring [l, r)
        $getHash = function($l, $r, $h, $pow, $mod) {
            $res = ($h[$r] - ($h[$l] * $pow[$r - $l]) % $mod);
            if ($res < 0) $res += $mod;
            return $res;
        };

        // LCP using binary search on hashes
        $lcpFunc = function($i, $j) use (&$num, $n, &$h1, &$h2, &$pow1, &$pow2, $mod1, $mod2, $getHash) {
            $maxLen = min($n - $i, $n - $j);
            $low = 0;
            $high = $maxLen;
            while ($low < $high) {
                $mid = intdiv($low + $high + 1, 2);
                $hash1_i = $getHash($i, $i + $mid, $h1, $pow1, $mod1);
                $hash1_j = $getHash($j, $j + $mid, $h1, $pow1, $mod1);
                if ($hash1_i !== $hash1_j) {
                    $high = $mid - 1;
                    continue;
                }
                $hash2_i = $getHash($i, $i + $mid, $h2, $pow2, $mod2);
                $hash2_j = $getHash($j, $j + $mid, $h2, $pow2, $mod2);
                if ($hash2_i === $hash2_j) {
                    $low = $mid;
                } else {
                    $high = $mid - 1;
                }
            }
            return $low;
        };

        // dp and prefix sums
        $dp = array_fill(0, $n + 1, 0);
        $pref = array_fill(0, $n + 2, 0); // pref[i] = sum_{k=0}^{i-1} dp[k]
        $dp[0] = 1;
        $pref[1] = 1;

        for ($i = 1; $i <= $n; $i++) {
            $total = 0;
            for ($L = 1; $L <= $i; $L++) {
                $j = $i - $L; // start index of current number
                if ($num[$j] === '0') continue; // leading zero not allowed

                if ($j == 0) {
                    // whole prefix as a single number
                    $total++;
                    if ($total >= $MOD) $total -= $MOD;
                    continue;
                }

                // sum of dp[k] where previous length < L
                $lowK = max(0, $j - $L + 1);
                if ($lowK <= $j - 1) {
                    $sumLess = $pref[$j] - $pref[$lowK];
                    $sumLess %= $MOD;
                    if ($sumLess < 0) $sumLess += $MOD;
                    $total += $sumLess;
                    if ($total >= $MOD) $total -= $MOD;
                }

                // previous length == L
                $k = $j - $L;
                if ($k >= 0 && $num[$k] !== '0') {
                    $lcpLen = $lcpFunc($k, $j);
                    $ok = false;
                    if ($lcpLen >= $L) {
                        $ok = true; // equal
                    } else {
                        $c1 = $num[$k + $lcpLen];
                        $c2 = $num[$j + $lcpLen];
                        if ($c1 <= $c2) $ok = true;
                    }
                    if ($ok) {
                        $total += $dp[$k];
                        if ($total >= $MOD) $total -= $MOD;
                    }
                }
            }
            $dp[$i] = $total % $MOD;
            $pref[$i + 1] = $pref[$i] + $dp[$i];
            if ($pref[$i + 1] >= $MOD) $pref[$i + 1] -= $MOD;
        }

        return $dp[$n] % $MOD;
    }
}
```

## Swift

```swift
class Solution {
    func numberOfCombinations(_ num: String) -> Int {
        let MOD = 1_000_000_007
        let chars = Array(num.utf8)
        let n = chars.count
        if n == 0 { return 0 }
        
        // lcp[i][j] = longest common prefix of suffixes starting at i and j
        var lcp = Array(repeating: Array(repeating: 0, count: n + 1), count: n + 1)
        if n > 0 {
            for i in stride(from: n - 1, through: 0, by: -1) {
                for j in stride(from: n - 1, through: 0, by: -1) {
                    if chars[i] == chars[j] {
                        lcp[i][j] = lcp[i + 1][j + 1] + 1
                    }
                }
            }
        }
        
        // pref[pos][len] = sum_{k=1..len} dp[pos][k]
        var pref = Array(repeating: Array(repeating: 0, count: n + 1), count: n + 1)
        
        func lessOrEqual(_ a: Int, _ b: Int, _ len: Int) -> Bool {
            let common = lcp[a][b]
            if common >= len { return true }
            return chars[a + common] < chars[b + common]
        }
        
        for i in 1...n {
            // pref[i][0] is already 0
            for l in 1...i {
                let start = i - l
                if chars[start] == 48 { // leading zero not allowed
                    pref[i][l] = pref[i][l - 1]
                    continue
                }
                
                var ways: Int
                if start == 0 {
                    // first number in the sequence
                    ways = 1
                } else {
                    // sum of dp[start][lenPrev] where lenPrev < l
                    var val = pref[start][l - 1]
                    
                    // equal length case
                    if start >= l {
                        let prevStart = start - l
                        if lessOrEqual(prevStart, start, l) {
                            var eq = pref[start][l] - pref[start][l - 1]
                            if eq < 0 { eq += MOD }
                            val += eq
                            if val >= MOD { val -= MOD }
                        }
                    }
                    ways = val % MOD
                }
                
                var cumulative = pref[i][l - 1] + ways
                if cumulative >= MOD { cumulative -= MOD }
                pref[i][l] = cumulative
            }
        }
        
        return pref[n][n]
    }
}
```

## Kotlin

```kotlin
import java.util.*

class Solution {
    private val MOD = 1_000_000_007

    fun numberOfCombinations(num: String): Int {
        val n = num.length
        if (n == 0) return 0
        val s = num.toCharArray()
        // LCP matrix
        val lcp = Array(n + 1) { IntArray(n + 1) }
        for (i in n - 1 downTo 0) {
            for (j in n - 1 downTo 0) {
                if (s[i] == s[j]) {
                    lcp[i][j] = lcp[i + 1][j + 1] + 1
                }
            }
        }

        val dp = Array(n + 1) { IntArray(0) }
        val pref = Array(n + 1) { IntArray(0) }

        for (i in 1..n) {
            val maxLen = i
            val curDp = IntArray(maxLen + 1)
            val curPref = IntArray(maxLen + 1)

            for (len in 1..maxLen) {
                val start = i - len
                if (s[start] == '0') continue

                var ways = 0L
                if (start == 0) {
                    ways = 1L
                } else {
                    // previous number shorter than current
                    if (len > 1) {
                        ways += pref[start][len - 1]
                    }
                    // previous number same length
                    if (len <= start) {
                        val prevStart = start - len
                        var le = false
                        val common = lcp[prevStart][start]
                        if (common >= len) {
                            le = true   // equal strings
                        } else {
                            if (s[prevStart + common] < s[start + common]) le = true
                        }
                        if (le) {
                            ways += dp[start][len]
                        }
                    }
                }

                val wMod = (ways % MOD).toInt()
                curDp[len] = wMod

                var sum = wMod.toLong() + (if (len > 0) curPref[len - 1].toLong() else 0L)
                if (sum >= MOD) sum -= MOD
                curPref[len] = sum.toInt()
            }

            dp[i] = curDp
            pref[i] = curPref
        }

        return pref[n][n]
    }
}
```

## Dart

```dart
class Solution {
  static const int MOD = 1000000007;

  int numberOfCombinations(String num) {
    int n = num.length;
    // Precompute LCP
    List<List<int>> lcp = List.generate(n + 1, (_) => List.filled(n + 1, 0));
    for (int i = n - 1; i >= 0; --i) {
      for (int j = n - 1; j >= 0; --j) {
        if (num.codeUnitAt(i) == num.codeUnitAt(j)) {
          lcp[i][j] = 1 + lcp[i + 1][j + 1];
        }
      }
    }

    // dp[i][len]: ways where a number starts at i with length len
    List<List<int>> dp = List.generate(n, (_) => List.filled(n + 1, 0));
    // prefRaw[e][len] stores raw dp values for segments ending at e with length len
    List<List<int>> prefRaw = List.generate(n, (_) => List.filled(n + 2, 0));
    // prefCum[e][len] will hold cumulative sums up to len (computed when needed)
    List<List<int>> prefCum = List.generate(n, (_) => List.filled(n + 2, 0));
    List<bool> cumReady = List.filled(n, false);

    for (int i = 0; i < n; ++i) {
      // Ensure cumulative sums for end i-1 are ready
      if (i > 0 && !cumReady[i - 1]) {
        int cum = 0;
        for (int len = 1; len <= i; ++len) {
          cum += prefRaw[i - 1][len];
          if (cum >= MOD) cum -= MOD;
          prefCum[i - 1][len] = cum;
        }
        cumReady[i - 1] = true;
      }

      if (num.codeUnitAt(i) == 48) continue; // leading zero not allowed

      for (int len = 1; i + len - 1 < n; ++len) {
        int e = i + len - 1;
        int ways;
        if (i == 0) {
          ways = 1;
        } else {
          // sum of previous lengths less than current length
          int limit = len - 1;
          if (limit > i) limit = i;
          int total = prefCum[i - 1][limit];

          // equal length case
          if (len <= i) {
            int common = lcp[i - len][i];
            bool leq;
            if (common >= len) {
              leq = true; // equal strings
            } else {
              leq = num.codeUnitAt(i - len + common) < num.codeUnitAt(i + common);
            }
            if (leq) {
              total += prefRaw[i - 1][len];
              if (total >= MOD) total -= MOD;
            }
          }
          ways = total % MOD;
        }

        dp[i][len] = ways;
        // store raw value for future equal-length checks
        int cur = prefRaw[e][len] + ways;
        if (cur >= MOD) cur -= MOD;
        prefRaw[e][len] = cur;
      }
    }

    // Final answer: sum of ways where the last number ends at n-1
    int ans = 0;
    for (int i = 0; i < n; ++i) {
      int len = n - i;
      ans += dp[i][len];
      if (ans >= MOD) ans -= MOD;
    }
    return ans % MOD;
  }
}
```

## Golang

```go
func numberOfCombinations(num string) int {
	const MOD = 1000000007
	n := len(num)

	// lcp[i][j] = longest common prefix length of suffixes starting at i and j
	lcp := make([][]int, n+1)
	for i := 0; i <= n; i++ {
		lcp[i] = make([]int, n+1)
	}
	for i := n - 1; i >= 0; i-- {
		for j := n - 1; j >= 0; j-- {
			if num[i] == num[j] {
				lcp[i][j] = lcp[i+1][j+1] + 1
			}
		}
	}

	// dp[i][len] = ways to split first i characters, last number has length len
	dp := make([][]int, n+1)
	pref := make([][]int, n+1) // prefix sums of dp[i][*]
	for i := 0; i <= n; i++ {
		dp[i] = make([]int, n+1)
		pref[i] = make([]int, n+1)
	}

	for i := 1; i <= n; i++ {
		for length := 1; length <= i; length++ {
			start := i - length
			if num[start] == '0' { // leading zero not allowed
				dp[i][length] = 0
			} else if start == 0 {
				dp[i][length] = 1
			} else {
				// sum of ways where previous number has fewer digits
				maxPrev := start
				limit := length - 1
				if limit > maxPrev {
					limit = maxPrev
				}
				sum := pref[start][limit]

				// case: previous number has same length
				if length <= start {
					a := start - length // start index of previous number
					b := start          // start index of current number
					common := lcp[a][b]
					if common >= length || (common < length && num[a+common] < num[b+common]) {
						sum += dp[start][length]
						if sum >= MOD {
							sum -= MOD
						}
					}
				}
				dp[i][length] = sum % MOD
			}
			// update prefix sums for position i
			pref[i][length] = pref[i][length-1] + dp[i][length]
			if pref[i][length] >= MOD {
				pref[i][length] -= MOD
			}
		}
	}

	ans := 0
	for length := 1; length <= n; length++ {
		ans += dp[n][length]
		if ans >= MOD {
			ans -= MOD
		}
	}
	return ans
}
```

## Ruby

```ruby
MOD = 1_000_000_007
BASE = 91138233
MODH1 = 1_000_000_007
MODH2 = 1_000_000_009

def number_of_combinations(num)
  n = num.length
  bytes = num.bytes

  # prefix hashes
  h1 = Array.new(n + 1, 0)
  h2 = Array.new(n + 1, 0)
  p1 = Array.new(n + 1, 1)
  p2 = Array.new(n + 1, 1)

  (0...n).each do |i|
    d = bytes[i]
    h1[i + 1] = (h1[i] * BASE + d) % MODH1
    h2[i + 1] = (h2[i] * BASE + d) % MODH2
    p1[i + 1] = (p1[i] * BASE) % MODH1
    p2[i + 1] = (p2[i] * BASE) % MODH2
  end

  get_hash = lambda do |l, r|
    x1 = (h1[r] - h1[l] * p1[r - l]) % MODH1
    x1 += MODH1 if x1 < 0
    x2 = (h2[r] - h2[l] * p2[r - l]) % MODH2
    x2 += MODH2 if x2 < 0
    [x1, x2]
  end

  leq = lambda do |a, b, len|
    return true if a == b
    low = 0
    high = len
    while low < high
      mid = (low + high + 1) >> 1
      if get_hash.call(a, a + mid) == get_hash.call(b, b + mid)
        low = mid
      else
        high = mid - 1
      end
    end
    return true if low == len # equal strings
    bytes[a + low] < bytes[b + low]
  end

  dp   = Array.new(n + 1) { Array.new(n + 1, 0) }
  pref = Array.new(n + 1) { Array.new(n + 1, 0) }

  # base case: empty prefix has one way (no last number)
  pref[0][0] = 1

  (1..n).each do |i|
    (1..i).each do |len|
      start_idx = i - len
      next if bytes[start_idx] == 48 # '0'

      total = pref[start_idx][len - 1]

      if start_idx >= len && bytes[start_idx - len] != 48
        if leq.call(start_idx - len, start_idx, len)
          total += dp[start_idx][len]
          total -= MOD if total >= MOD
        end
      end

      dp[i][len] = total
    end

    sum = 0
    (1..i).each do |len|
      sum += dp[i][len]
      sum -= MOD if sum >= MOD
      pref[i][len] = sum
    end
  end

  pref[n][n] % MOD
end
```

## Scala

```scala
object Solution {
  def numberOfCombinations(num: String): Int = {
    val MOD = 1000000007
    val n = num.length
    // Precompute LCP array
    val lcp = Array.ofDim[Int](n + 1, n + 1)
    var i = n - 1
    while (i >= 0) {
      var j = n - 1
      while (j >= 0) {
        if (num.charAt(i) == num.charAt(j)) {
          lcp(i)(j) = 1 + lcp(i + 1)(j + 1)
        } else {
          lcp(i)(j) = 0
        }
        j -= 1
      }
      i -= 1
    }

    // dp[pos][len] : ways for prefix of length pos, last number has length len
    val dp = Array.ofDim[Int](n + 1, n + 1)

    if (num.charAt(0) != '0') {
      var l = 1
      while (l <= n) {
        dp(l)(l) = 1
        l += 1
      }
    }

    var start = 1
    while (start < n) {
      // prefix sums of dp[start][*]
      val pre = new Array[Int](start + 2)
      var sum = 0
      var lenPrev = 1
      while (lenPrev <= start) {
        sum += dp(start)(lenPrev)
        if (sum >= MOD) sum -= MOD
        pre(lenPrev) = sum
        lenPrev += 1
      }

      if (num.charAt(start) != '0') {
        var curLen = 1
        while (start + curLen <= n) {
          val endPos = start + curLen

          // add contributions from shorter previous lengths
          val limit = if (curLen - 1 < start) curLen - 1 else start
          var add = if (limit >= 0) pre(limit) else 0

          // equal length case
          if (start - curLen >= 0) {
            var leq = false
            val common = lcp(start - curLen)(start)
            if (common >= curLen) {
              leq = true
            } else {
              if (num.charAt(start - curLen + common) < num.charAt(start + common)) leq = true
            }
            if (leq) {
              add += dp(start)(curLen)
              if (add >= MOD) add -= MOD
            }
          }

          var newVal = dp(endPos)(curLen) + add
          if (newVal >= MOD) newVal -= MOD
          dp(endPos)(curLen) = newVal

          curLen += 1
        }
      }
      start += 1
    }

    // sum all ways for full length
    var ans = 0
    var l = 1
    while (l <= n) {
      ans += dp(n)(l)
      if (ans >= MOD) ans -= MOD
      l += 1
    }
    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_combinations(num: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let bytes = num.as_bytes();
        let n = bytes.len();

        // lcp[i][j] = longest common prefix of suffixes starting at i and j
        let mut lcp = vec![vec![0usize; n + 1]; n + 1];
        for i in (0..n).rev() {
            for j in (0..n).rev() {
                if bytes[i] == bytes[j] {
                    lcp[i][j] = lcp[i + 1][j + 1] + 1;
                }
            }
        }

        // dp[i][len]: ways to split prefix of length i, last number has length len
        let mut dp = vec![vec![0i64; n + 1]; n + 1];
        // pref[i][len]: prefix sums of dp[i][*] for quick range sum
        let mut pref = vec![vec![0i64; n + 1]; n + 1];

        for i in 1..=n {
            for len in 1..=i {
                let start = i - len;
                if bytes[start] == b'0' {
                    continue; // leading zero not allowed
                }
                if start == 0 {
                    dp[i][len] = 1;
                } else {
                    // sum of previous lengths < current length
                    let mut val = pref[start][len - 1];
                    // same length case
                    if len <= start && bytes[start - len] != b'0' {
                        let prev_start = start - len;
                        let common = lcp[prev_start][start];
                        if common >= len || bytes[prev_start + common] < bytes[start + common] {
                            val += dp[start][len];
                        }
                    }
                    dp[i][len] = val % MOD;
                }
                pref[i][len] = (pref[i][len - 1] + dp[i][len]) % MOD;
            }
        }

        pref[n][n] as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define (add-mod a b)
  (let ((c (+ a b)))
    (if (>= c MOD) (- c MOD) c)))

(define/contract (number-of-combinations num)
  (-> string? exact-integer?)
  (let* ((n (string-length num))
         ;; lcp matrix (n+1) x (n+1)
         (lcp (make-vector (+ n 1)))
         (_ (for ([i (in-range (+ n 1))])
              (vector-set! lcp i (make-vector (+ n 1) 0))))
         ;; compute LCP
         (_ (for ([i (in-range (sub1 n) -1 -1)])
              (let ((row-i (vector-ref lcp i))
                    (row-ip1 (vector-ref lcp (+ i 1))))
                (for ([j (in-range (sub1 n) -1 -1)])
                  (if (char=? (string-ref num i) (string-ref num j))
                      (vector-set! row-i j
                                   (+ 1 (vector-ref row-ip1 (+ j 1))))
                      (vector-set! row-i j 0))))))
         ;; dp and prefix sum tables
         (dp (make-vector n))
         (pref (make-vector n)))
    ;; initialize rows
    (for ([i (in-range n)])
      (vector-set! dp i (make-vector (+ n 1) 0))
      (vector-set! pref i (make-vector (+ n 1) 0)))
    ;; main DP
    (for ([i (in-range n)])
      (let ((dp-row (vector-ref dp i))
            (pref-row (vector-ref pref i)))
        (for ([len (in-range 1 (add1 i))])
          (let* ((start (- i len -1)) ; start index of current number
                 (first-char (string-ref num start)))
            (when (not (char=? first-char #\0))
              (if (= start 0)
                  ;; whole prefix is one number
                  (vector-set! dp-row len 1)
                  (let* ((j (- start 1)) ; end index of previous segment
                         (total0 0)
                         (limit (min (- len 1) (+ j 1)))
                         (total1 (if (> limit 0)
                                     (vector-ref (vector-ref pref j) limit)
                                     0))
                         (total2
                          (let ((prev-start (- start len)))
                            (if (>= prev-start 0)
                                (let* ((common (vector-ref (vector-ref lcp prev-start) start))
                                       (cond-ok (or (= common len)
                                                    (char<=? (string-ref num (+ prev-start common))
                                                             (string-ref num (+ start common))))))
                                  (if cond-ok
                                      (add-mod 0 (vector-ref (vector-ref dp j) len))
                                      0))
                                0)))
                         (total (add-mod total1 total2)))
                    (vector-set! dp-row len total)))))
          )
        ;; compute prefix sums for this i
        (let ((cum 0))
          (for ([len (in-range 1 (add1 i))])
            (set! cum (add-mod cum (vector-ref dp-row len)))
            (vector-set! pref-row len cum))))
      )
    (if (= n 0)
        0
        (vector-ref (vector-ref pref (sub1 n)) n))))
```

## Erlang

```erlang
-spec number_of_combinations(Num :: unicode:unicode_binary()) -> integer().
number_of_combinations(Num) ->
    Mod = 1000000007,
    Base = 91138233,
    Mod1 = 1000000007,
    Mod2 = 1000000009,

    % convert to list of digit integers (0..9)
    DigitsList = [C - $0 || <<C>> <= Num],
    N = length(DigitsList),

    % build tuples for digits, powers and prefix hashes
    DigitsTuple = list_to_tuple(DigitsList),

    {Pow1, Pow2, H1, H2} =
        build_arrays(DigitsList, Base, Mod1, Mod2),

    % ETS tables for dp and prefix sums
    DPTab = ets:new(dp_tab, [set, public]),
    PrefTab = ets:new(pref_tab, [set, public]),

    % main DP
    lists:foreach(
      fun(I) ->
          AccPref0 = 0,
          loop_len(I, I, DigitsTuple, Pow1, Pow2, H1, H2, Mod, Mod1, Mod2,
                   DPTab, PrefTab, AccPref0)
      end,
      lists:seq(1, N)),

    % answer is prefix sum for position N and length N
    case ets:lookup(PrefTab, {N, N}) of
        [{_, Ans}] -> Ans;
        [] -> 0
    end.

%% Build power and hash tuples (index 0 stored at position 1)
build_arrays(Digits, Base, Mod1, Mod2) ->
    % start with pow[0]=1, h[0]=0
    {Pow1Rev, Pow2Rev, H1Rev, H2Rev} =
        lists:foldl(
          fun(Digit,
              {P1Acc, P2Acc, H1Acc, H2Acc}) ->
                PrevPow1 = hd(P1Acc),
                NewPow1 = (PrevPow1 * Base) rem Mod1,
                PrevPow2 = hd(P2Acc),
                NewPow2 = (PrevPow2 * Base) rem Mod2,
                PrevH1 = hd(H1Acc),
                NewH1 = (PrevH1 * Base + Digit) rem Mod1,
                PrevH2 = hd(H2Acc),
                NewH2 = (PrevH2 * Base + Digit) rem Mod2,
                {[NewPow1|P1Acc],
                 [NewPow2|P2Acc],
                 [NewH1|H1Acc],
                 [NewH2|H2Acc]}
          end,
          {[1], [1], [0], [0]},
          Digits),
    Pow1 = list_to_tuple(lists:reverse(Pow1Rev)),
    Pow2 = list_to_tuple(lists:reverse(Pow2Rev)),
    H1   = list_to_tuple(lists:reverse(H1Rev)),
    H2   = list_to_tuple(lists:reverse(H2Rev)),
    {Pow1, Pow2, H1, H2}.

%% Loop over possible lengths for a fixed end position I
loop_len(I, Len, _DigitsTuple, _Pow1, _Pow2, _H1, _H2,
         _Mod, _Mod1, _Mod2, _DPTab, _PrefTab, AccPref) when Len < 1 ->
    ok;
loop_len(I, Len, DigitsTuple, Pow1, Pow2, H1, H2,
         Mod, Mod1, Mod2, DPTab, PrefTab, AccPrev) ->
    Start = I - Len + 1,
    CharAtStart = element(Start, DigitsTuple),
    Value =
        if
            CharAtStart =:= 0 -> 0;
            true ->
                PrevEnd = Start - 1,
                case PrevEnd of
                    0 -> 1;
                    _ ->
                        SumLess =
                            if Len > 1 ->
                                    get_pref(PrefTab, PrevEnd, Len-1);
                               true -> 0
                            end,
                        EqualPart = 
                            case Start - Len of
                                PrevStart when PrevStart >= 1 ->
                                    case le_substring(PrevStart, Start, Len,
                                                      DigitsTuple, Pow1, Pow2,
                                                      H1, H2, Mod1, Mod2) of
                                        true -> get_dp(DPTab, PrevEnd, Len);
                                        false -> 0
                                    end;
                                _ -> 0
                            end,
                        (SumLess + EqualPart) rem Mod
                end
        end,
    ets:insert(DPTab, {{I, Len}, Value}),
    AccCurr = (AccPrev + Value) rem Mod,
    ets:insert(PrefTab, {{I, Len}, AccCurr}),
    loop_len(I, Len-1, DigitsTuple, Pow1, Pow2, H1, H2,
             Mod, Mod1, Mod2, DPTab, PrefTab, AccCurr).

%% Retrieve dp value
get_dp(DPTab, Pos, Len) ->
    case ets:lookup(DPTab, {Pos, Len}) of
        [{_, V}] -> V;
        [] -> 0
    end.

%% Retrieve prefix sum up to Len at position Pos
get_pref(PrefTab, Pos, Len) ->
    case ets:lookup(PrefTab, {Pos, Len}) of
        [{_, V}] -> V;
        [] -> 0
    end.

%% Compare two substrings of equal length: return true if first <= second
le_substring(A, B, Len,
             DigitsTuple, Pow1, Pow2, H1, H2, Mod1, Mod2) ->
    Lcp = lcp(A, B, Len, Pow1, Pow2, H1, H2, Mod1, Mod2),
    if
        Lcp >= Len -> true;
        true ->
            CharA = element(A + Lcp, DigitsTuple),
            CharB = element(B + Lcp, DigitsTuple),
            CharA =< CharB
    end.

%% Compute longest common prefix length (max up to MaxLen)
lcp(A, B, MaxLen, Pow1, Pow2, H1, H2, Mod1, Mod2) ->
    lcp_binsearch(0, MaxLen, A, B, Pow1, Pow2, H1, H2, Mod1, Mod2).

lcp_binsearch(Low, High, A, B,
              Pow1, Pow2, H1, H2, Mod1, Mod2) when Low < High ->
    Mid = (Low + High + 1) div 2,
    case equal_sub(A, B, Mid, Pow1, Pow2, H1, H2, Mod1, Mod2) of
        true -> lcp_binsearch(Mid, High, A, B, Pow1, Pow2, H1, H2, Mod1, Mod2);
        false -> lcp_binsearch(Low, Mid-1, A, B, Pow1, Pow2, H1, H2, Mod1, Mod2)
    end;
lcp_binsearch(Len, _High, _A, _B, _Pow1, _Pow2, _H1, _H2, _Mod1, _Mod2) ->
    Len.

%% Check equality of substrings of length Len starting at A and B
equal_sub(A, B, Len,
          Pow1, Pow2, H1, H2, Mod1, Mod2) when Len =:= 0 ->
    true;
equal_sub(A, B, Len,
          Pow1, Pow2, H1, H2, Mod1, Mod2) ->
    HashA1 = get_hash(H1, Pow1, A, A+Len-1, Mod1),
    HashB1 = get_hash(H1, Pow1, B, B+Len-1, Mod1),
    if
        HashA1 =/= HashB1 -> false;
        true ->
            HashA2 = get_hash(H2, Pow2, A, A+Len-1, Mod2),
            HashB2 = get_hash(H2, Pow2, B, B+Len-1, Mod2),
            HashA2 =:= HashB2
    end.

%% Get hash of substring [L,R] (1‑based indices) using prefix hashes
get_hash(H, Pow, L, R, Mod) ->
    HR = element(R + 1, H),
    HL_1 = element(L, H),          % because L-1 +1 = L
    Len = R - L + 1,
    PowLen = element(Len + 1, Pow),
    ((HR - (HL_1 * PowLen) rem Mod) + Mod) rem Mod.
```

## Elixir

```elixir
defmodule Solution do
  @mod 1_000_000_007

  @spec number_of_combinations(String.t()) :: integer
  def number_of_combinations(num) do
    n = String.length(num)
    chars = :array.from_list(String.to_charlist(num))

    # precompute LCP for each offset d (distance between substrings)
    offset_arr = build_lcp_offsets(n, chars)

    stride = n + 1
    total_size = stride * (n + 1)
    dp = :array.new(total_size, default: 0)
    dp = :array.set(idx(0, 0, stride), 1, dp)

    dp =
      Enum.reduce(0..(n - 1), dp, fn i, dp_acc ->
        if :array.get(i, chars) == ?0 do
          dp_acc
        else
          max_l = n - i

          {dp_new, _cum} =
            Enum.reduce(1..max_l, {dp_acc, 0}, fn l, {dp_inner, cum} ->
              total = cum

              if l <= i do
                # equality check between previous and current number of length l
                offset_tuple = :array.get(l, offset_arr)
                common = :erlang.element(i - l + 1, offset_tuple)

                eq_ok =
                  if common >= l do
                    true
                  else
                    c1 = :array.get(i - l + common, chars)
                    c2 = :array.get(i + common, chars)
                    c1 < c2
                  end

                if eq_ok do
                  dp_i_l = :array.get(idx(i, l, stride), dp_inner)
                  total = rem(total + dp_i_l, @mod)
                else
                  total = total
                end
              end

              # add to state (i+l, l)
              next_idx = idx(i + l, l, stride)
              prev_val = :array.get(next_idx, dp_inner)
              new_val = rem(prev_val + total, @mod)
              dp_updated = :array.set(next_idx, new_val, dp_inner)

              # update cumulative sum for next length
              cum_new =
                if l <= i do
                  dp_i_l = :array.get(idx(i, l, stride), dp_inner)
                  rem(cum + dp_i_l, @mod)
                else
                  cum
                end

              {dp_updated, cum_new}
            end)

          dp_new
        end
      end)

    # sum all ways that finish at position n
    Enum.reduce(0..n, 0, fn len, acc ->
      val = :array.get(idx(n, len, stride), dp)
      rem(acc + val, @mod)
    end)
  end

  defp idx(i, len, stride), do: i * stride + len

  defp build_lcp_offsets(n, chars) do
    offset_arr = :array.new(n + 1, default: nil)

    Enum.reduce((n - 1)..1, offset_arr, fn d, arr ->
      len = n - d

      {list_rev, _} =
        Enum.reduce(0..(len - 1), {[], 0}, fn rev_i, {acc, next_val} ->
          i = len - 1 - rev_i
          c1 = :array.get(i, chars)
          c2 = :array.get(i + d, chars)

          val = if c1 == c2, do: 1 + next_val, else: 0
          {[val | acc], val}
        end)

      tuple = List.to_tuple(list_rev ++ [0])
      :array.set(d, tuple, arr)
    end)
  end
end
```
