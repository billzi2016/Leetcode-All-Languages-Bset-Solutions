# 2801. Count Stepping Numbers in Range

## Cpp

```cpp
class Solution {
public:
    static const int MOD = 1000000007;
    long long memo[105][11][2][2];
    string bound;
    int n;

    long long dfs(int pos, int prev, bool tight, bool started) {
        if (pos == n) return started ? 1 : 0;
        int idxPrev = started ? prev : 10; // 10 denotes undefined
        long long &res = memo[pos][idxPrev][tight][started];
        if (res != -1) return res;
        res = 0;
        int limit = tight ? bound[pos] - '0' : 9;
        for (int d = 0; d <= limit; ++d) {
            bool ntight = tight && (d == limit);
            if (!started && d == 0) {
                // still leading zeros, number not started
                res += dfs(pos + 1, 0, ntight, false);
            } else {
                if (!started) {
                    // first non‑zero digit, no previous constraint
                    res += dfs(pos + 1, d, ntight, true);
                } else {
                    if (abs(d - prev) == 1) {
                        res += dfs(pos + 1, d, ntight, true);
                    }
                }
            }
            if (res >= MOD) res -= MOD;
        }
        return res % MOD;
    }

    int countUpTo(const string &s) {
        bound = s;
        n = bound.size();
        memset(memo, -1, sizeof(memo));
        return (int)(dfs(0, 0, true, false) % MOD);
    }

    string decOne(string s) {
        int i = (int)s.size() - 1;
        while (i >= 0 && s[i] == '0') {
            s[i] = '9';
            --i;
        }
        if (i >= 0) {
            s[i]--;
        }
        // strip leading zeros, keep at least one digit
        int pos = 0;
        while (pos + 1 < (int)s.size() && s[pos] == '0') ++pos;
        return s.substr(pos);
    }

    int countSteppingNumbers(string low, string high) {
        int cntHigh = countUpTo(high);
        string lowMinusOne = decOne(low);
        int cntLow = countUpTo(lowMinusOne); // works even when lowMinusOne == "0"
        int ans = (cntHigh - cntLow) % MOD;
        if (ans < 0) ans += MOD;
        return ans;
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    private String bound;
    private int len;
    private long[][][][] dp;

    public int countSteppingNumbers(String low, String high) {
        int cntHigh = countUpTo(high);
        String lowMinusOne = subtractOne(low);
        int cntLow = countUpTo(lowMinusOne);
        return (int) ((cntHigh - cntLow + MOD) % MOD);
    }

    private int countUpTo(String num) {
        if (num.equals("0")) return 0;
        this.bound = num;
        this.len = bound.length();
        dp = new long[len + 1][11][2][2];
        for (int i = 0; i <= len; i++) {
            for (int j = 0; j < 11; j++) {
                for (int k = 0; k < 2; k++) {
                    java.util.Arrays.fill(dp[i][j][k], -1L);
                }
            }
        }
        long res = dfs(0, -1, true, false);
        return (int) (res % MOD);
    }

    private long dfs(int pos, int prev, boolean tight, boolean started) {
        if (pos == len) {
            return started ? 1 : 0;
        }
        int pIdx = prev + 1; // -1 -> 0
        int tIdx = tight ? 1 : 0;
        int sIdx = started ? 1 : 0;
        if (dp[pos][pIdx][tIdx][sIdx] != -1) {
            return dp[pos][pIdx][tIdx][sIdx];
        }
        int limit = tight ? bound.charAt(pos) - '0' : 9;
        long ans = 0;
        for (int d = 0; d <= limit; d++) {
            boolean nextTight = tight && d == limit;
            if (!started && d == 0) {
                // still leading zeros
                ans += dfs(pos + 1, -1, nextTight, false);
            } else {
                if (!started) { // first non‑zero digit
                    ans += dfs(pos + 1, d, nextTight, true);
                } else {
                    if (Math.abs(d - prev) == 1) {
                        ans += dfs(pos + 1, d, nextTight, true);
                    }
                }
            }
            if (ans >= MOD) ans -= MOD;
        }
        dp[pos][pIdx][tIdx][sIdx] = ans % MOD;
        return dp[pos][pIdx][tIdx][sIdx];
    }

    private String subtractOne(String s) {
        char[] ch = s.toCharArray();
        int i = ch.length - 1;
        while (i >= 0 && ch[i] == '0') {
            ch[i] = '9';
            i--;
        }
        if (i >= 0) {
            ch[i]--;
        }
        int start = 0;
        while (start < ch.length - 1 && ch[start] == '0') start++;
        return new String(ch, start, ch.length - start);
    }
}
```

## Python

```python
class Solution(object):
    def countSteppingNumbers(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        MOD = 10**9 + 7

        def dec_str(s):
            if s == "0":
                return "0"
            lst = list(s)
            i = len(lst) - 1
            while i >= 0 and lst[i] == '0':
                lst[i] = '9'
                i -= 1
            lst[i] = str(int(lst[i]) - 1)
            res = ''.join(lst).lstrip('0')
            return res if res else "0"

        def count(bound):
            if bound == "0":
                return 0
            n = len(bound)
            from functools import lru_cache

            @lru_cache(None)
            def dfs(pos, prev, tight, started):
                if pos == n:
                    return 1 if started else 0
                limit = int(bound[pos]) if tight else 9
                total = 0
                for d in range(limit + 1):
                    ntight = tight and (d == limit)
                    if not started:
                        if d == 0:
                            total += dfs(pos + 1, -1, ntight, False)
                        else:
                            total += dfs(pos + 1, d, ntight, True)
                    else:
                        if abs(d - prev) == 1:
                            total += dfs(pos + 1, d, ntight, True)
                return total % MOD

            return dfs(0, -1, True, False)

        low_minus_one = dec_str(low)
        ans = (count(high) - count(low_minus_one)) % MOD
        return ans
```

## Python3

```python
class Solution:
    MOD = 10**9 + 7
    MAX_LEN = 105

    # precompute dp_len[l][d]: number of l-digit stepping numbers ending with digit d (no leading zero)
    dp_len = [[0] * 10 for _ in range(MAX_LEN)]
    total_len = [0] * MAX_LEN
    prefix_sum = [0] * MAX_LEN

    for d in range(1, 10):
        dp_len[1][d] = 1
    total_len[1] = 9
    prefix_sum[1] = 9
    for l in range(2, MAX_LEN):
        s = 0
        for d in range(10):
            val = 0
            if d - 1 >= 0:
                val += dp_len[l - 1][d - 1]
            if d + 1 <= 9:
                val += dp_len[l - 1][d + 1]
            dp_len[l][d] = val % MOD
            s += dp_len[l][d]
        total_len[l] = s % Solution.MOD
        prefix_sum[l] = (prefix_sum[l - 1] + total_len[l]) % Solution.MOD

    def countSteppingNumbers(self, low: str, high: str) -> int:
        def dec_str(s: str) -> str:
            if s == "0":
                return "0"
            lst = list(s)
            i = len(lst) - 1
            while i >= 0 and lst[i] == '0':
                lst[i] = '9'
                i -= 1
            if i < 0:
                return "0"
            lst[i] = chr(ord(lst[i]) - 1)
            res = ''.join(lst).lstrip('0')
            return res if res else "0"

        def count_up_to(s: str) -> int:
            if s == "0":
                return 0
            n = len(s)

            # numbers with length < n
            total = self.prefix_sum[n - 1]

            from functools import lru_cache

            @lru_cache(None)
            def dfs(idx: int, prev: int, tight: bool) -> int:
                if idx == n:
                    return 1
                limit = ord(s[idx]) - 48 if tight else 9
                ans = 0
                if idx == 0:
                    for d in range(1, limit + 1):
                        ans += dfs(idx + 1, d, tight and d == limit)
                else:
                    for nd in (prev - 1, prev + 1):
                        if 0 <= nd <= 9 and nd <= limit:
                            ans += dfs(idx + 1, nd, tight and nd == limit)
                return ans % self.MOD

            total = (total + dfs(0, -1, True)) % self.MOD
            return total

        high_cnt = count_up_to(high)
        low_minus_one = dec_str(low)
        low_cnt = count_up_to(low_minus_one)
        return (high_cnt - low_cnt) % self.MOD
```

## C

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

static const int MOD = 1000000007;

static int digits[105];
static int len;
static long long dp[105][10][2][2];
static char vis[105][10][2][2];

static long long dfs(int pos, int prev, int tight, int started) {
    if (pos == len) return started ? 1 : 0;
    if (vis[pos][prev][tight][started]) return dp[pos][prev][tight][started];
    long long res = 0;
    int limit = tight ? digits[pos] : 9;
    for (int d = 0; d <= limit; ++d) {
        int ntight = (tight && d == limit);
        if (!started) {
            if (d == 0) {
                res += dfs(pos + 1, 0, ntight, 0);
            } else {
                res += dfs(pos + 1, d, ntight, 1);
            }
        } else {
            if (abs(d - prev) == 1) {
                res += dfs(pos + 1, d, ntight, 1);
            }
        }
        if (res >= (1LL << 60)) res %= MOD;
    }
    res %= MOD;
    vis[pos][prev][tight][started] = 1;
    dp[pos][prev][tight][started] = res;
    return res;
}

static int countUpTo(const char *s) {
    len = strlen(s);
    for (int i = 0; i < len; ++i) digits[i] = s[i] - '0';
    memset(vis, 0, sizeof(vis));
    long long ans = dfs(0, 0, 1, 0);
    return (int)(ans % MOD);
}

static void decString(const char *s, char *out) {
    int n = strlen(s);
    char buf[105];
    strcpy(buf, s);
    int i = n - 1;
    while (i >= 0 && buf[i] == '0') {
        buf[i] = '9';
        --i;
    }
    if (i >= 0) {
        buf[i]--;
    }
    int start = 0;
    while (start < n - 1 && buf[start] == '0') ++start;
    int j = 0;
    for (int k = start; k < n; ++k) out[j++] = buf[k];
    out[j] = '\0';
}

int countSteppingNumbers(char* low, char* high) {
    int highCnt = countUpTo(high);
    if (strcmp(low, "1") == 0) return highCnt;
    char lowMinus[105];
    decString(low, lowMinus);
    int lowCnt = (strcmp(lowMinus, "0") == 0) ? 0 : countUpTo(lowMinus);
    long long ans = highCnt - lowCnt;
    if (ans < 0) ans += MOD;
    return (int)(ans % MOD);
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Text;

public class Solution {
    private const int MOD = 1000000007;
    private string boundStr;
    private int len;
    private Dictionary<(int,int,int,int), long> memo;

    private long Dfs(int pos, int prev, bool tight, bool started) {
        if (pos == len) return started ? 1L : 0L;
        var key = (pos, prev + 1, tight ? 1 : 0, started ? 1 : 0);
        if (!tight && memo.TryGetValue(key, out long cached)) return cached;

        int limit = tight ? boundStr[pos] - '0' : 9;
        long res = 0L;
        for (int d = 0; d <= limit; ++d) {
            bool nextTight = tight && d == limit;
            if (!started) {
                if (d == 0) {
                    res += Dfs(pos + 1, -1, nextTight, false);
                } else {
                    res += Dfs(pos + 1, d, nextTight, true);
                }
            } else {
                if (Math.Abs(d - prev) == 1) {
                    res += Dfs(pos + 1, d, nextTight, true);
                }
            }
            if (res >= MOD) res %= MOD;
        }

        if (!tight) memo[key] = res % MOD;
        return res % MOD;
    }

    private long CountUpTo(string s) {
        boundStr = s;
        len = s.Length;
        memo = new Dictionary<(int,int,int,int), long>();
        return Dfs(0, -1, true, false);
    }

    private string Decrement(string num) {
        var sb = new StringBuilder(num);
        int i = sb.Length - 1;
        while (i >= 0 && sb[i] == '0') {
            sb[i] = '9';
            i--;
        }
        if (i < 0) return "0";
        sb[i] = (char)(sb[i] - 1);
        int start = 0;
        while (start < sb.Length - 1 && sb[start] == '0') start++;
        return sb.ToString(start, sb.Length - start);
    }

    public int CountSteppingNumbers(string low, string high) {
        long highCount = CountUpTo(high);
        string lowMinusOne = Decrement(low);
        long lowCount = CountUpTo(lowMinusOne);
        long ans = (highCount - lowCount) % MOD;
        if (ans < 0) ans += MOD;
        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} low
 * @param {string} high
 * @return {number}
 */
var countSteppingNumbers = function(low, high) {
    const MOD = 1000000007n;
    const maxLen = Math.max(low.length, high.length);
    
    // dp[len][digit] = number of stepping numbers with exact length len ending with digit
    const dp = Array.from({length: maxLen + 1}, () => Array(10).fill(0n));
    const totalLen = Array(maxLen + 1).fill(0n);
    
    for (let d = 1; d <= 9; ++d) dp[1][d] = 1n;
    totalLen[1] = 9n;
    
    for (let len = 2; len <= maxLen; ++len) {
        let sum = 0n;
        for (let d = 0; d <= 9; ++d) {
            let val = 0n;
            if (d - 1 >= 0) val += dp[len - 1][d - 1];
            if (d + 1 <= 9) val += dp[len - 1][d + 1];
            dp[len][d] = val % MOD;
            sum = (sum + dp[len][d]) % MOD;
        }
        totalLen[len] = sum;
    }
    
    function countUpTo(s) {
        if (s === "0") return 0n;
        const n = s.length;
        let total = 0n;
        for (let len = 1; len < n; ++len) {
            total = (total + totalLen[len]) % MOD;
        }
        const memo = Array.from({length: n}, () => 
            Array(11).fill(null).map(() => [undefined, undefined])
        );
        function dfs(pos, prev, tight) {
            if (pos === n) return 1n;
            const prevIdx = prev === -1 ? 10 : prev;
            const tIdx = tight ? 1 : 0;
            const cached = memo[pos][prevIdx][tIdx];
            if (cached !== undefined) return cached;
            const limit = tight ? Number(s.charAt(pos)) : 9;
            let res = 0n;
            for (let d = 0; d <= limit; ++d) {
                if (pos === 0 && d === 0) continue; // no leading zero
                if (prev !== -1 && Math.abs(d - prev) !== 1) continue;
                const nextTight = tight && (d === limit);
                res = (res + dfs(pos + 1, d, nextTight)) % MOD;
            }
            memo[pos][prevIdx][tIdx] = res;
            return res;
        }
        total = (total + dfs(0, -1, true)) % MOD;
        return total;
    }
    
    function decOne(str) {
        if (str === "0") return "0";
        const arr = str.split('').map(ch => ch.charCodeAt(0) - 48);
        let i = arr.length - 1;
        while (i >= 0 && arr[i] === 0) {
            arr[i] = 9;
            i--;
        }
        if (i >= 0) arr[i]--;
        let start = 0;
        while (start < arr.length - 1 && arr[start] === 0) start++;
        return arr.slice(start).join('');
    }
    
    const highCount = countUpTo(high);
    const lowMinusOne = decOne(low);
    const lowCount = countUpTo(lowMinusOne);
    const ans = (highCount - lowCount + MOD) % MOD;
    return Number(ans);
};
```

## Typescript

```typescript
function countSteppingNumbers(low: string, high: string): number {
    const MOD = 1000000007n;

    function decString(s: string): string {
        if (s === "0") return "0";
        const arr = s.split('').map(ch => Number(ch));
        let i = arr.length - 1;
        while (i >= 0 && arr[i] === 0) {
            arr[i] = 9;
            i--;
        }
        if (i >= 0) arr[i]--;
        // remove leading zeros
        let idx = 0;
        while (idx < arr.length - 1 && arr[idx] === 0) idx++;
        return arr.slice(idx).join('') || '0';
    }

    function countUpTo(s: string): bigint {
        const n = s.length;
        const memo = new Map<string, bigint>();

        function dfs(pos: number, prev: number, tight: boolean, started: boolean): bigint {
            if (pos === n) return started ? 1n : 0n;
            const key = `${pos}|${prev}|${tight ? 1 : 0}|${started ? 1 : 0}`;
            if (memo.has(key)) return memo.get(key)!;

            const limit = tight ? Number(s[pos]) : 9;
            let total = 0n;

            for (let d = 0; d <= limit; d++) {
                const nextTight = tight && d === limit;
                if (!started) {
                    if (d === 0) {
                        total += dfs(pos + 1, 10, nextTight, false);
                    } else {
                        total += dfs(pos + 1, d, nextTight, true);
                    }
                } else {
                    if (Math.abs(d - prev) !== 1) continue;
                    total += dfs(pos + 1, d, nextTight, true);
                }
            }

            total %= MOD;
            memo.set(key, total);
            return total;
        }

        return dfs(0, 10, true, false);
    }

    const highCount = countUpTo(high);
    const lowMinusOne = decString(low);
    const lowCount = countUpTo(lowMinusOne);

    let ans = (highCount - lowCount) % MOD;
    if (ans < 0) ans += MOD;
    return Number(ans);
}
```

## Php

```php
class Solution {
    private const MOD = 1000000007;

    /**
     * @param String $low
     * @param String $high
     * @return Integer
     */
    function countSteppingNumbers($low, $high) {
        $cntHigh = $this->countUpTo($high);
        $lowMinusOne = $this->decrement($low);
        $cntLow = ($lowMinusOne === "0") ? 0 : $this->countUpTo($lowMinusOne);
        $ans = $cntHigh - $cntLow;
        $ans %= self::MOD;
        if ($ans < 0) {
            $ans += self::MOD;
        }
        return $ans;
    }

    private function countUpTo(string $s): int {
        if ($s === "0") {
            return 0;
        }
        $digits = array_map('intval', str_split($s));
        $n = count($digits);
        $memo = [];

        $dfs = function(int $pos, bool $tight, bool $started, int $prev) use (&$dfs, &$memo, $digits, $n): int {
            if ($pos === $n) {
                return $started ? 1 : 0;
            }
            if (!$tight) {
                $keyPrev = $started ? ($prev + 1) : 0;
                if (isset($memo[$pos][$started][$keyPrev])) {
                    return $memo[$pos][$started][$keyPrev];
                }
            }

            $limit = $tight ? $digits[$pos] : 9;
            $res = 0;
            for ($d = 0; $d <= $limit; ++$d) {
                $nextTight = $tight && ($d === $limit);
                if (!$started && $d === 0) {
                    $res = ($res + $dfs($pos + 1, $nextTight, false, 0)) % self::MOD;
                } else {
                    if (!$started) { // first non‑zero digit
                        $res = ($res + $dfs($pos + 1, $nextTight, true, $d)) % self::MOD;
                    } elseif (abs($d - $prev) === 1) {
                        $res = ($res + $dfs($pos + 1, $nextTight, true, $d)) % self::MOD;
                    }
                }
            }

            if (!$tight) {
                $keyPrev = $started ? ($prev + 1) : 0;
                $memo[$pos][$started][$keyPrev] = $res;
            }
            return $res;
        };

        return $dfs(0, true, false, 0);
    }

    private function decrement(string $s): string {
        if ($s === "0") {
            return "0";
        }
        $arr = str_split($s);
        $i = count($arr) - 1;
        while ($i >= 0) {
            if ($arr[$i] > '0') {
                $arr[$i] = chr(ord($arr[$i]) - 1);
                break;
            } else {
                $arr[$i] = '9';
                --$i;
            }
        }
        $result = ltrim(implode('', $arr), '0');
        return $result === '' ? '0' : $result;
    }
}
```

## Swift

```swift
class Solution {
    let MOD = 1_000_000_007

    func countSteppingNumbers(_ low: String, _ high: String) -> Int {
        func decrement(_ s: String) -> String {
            var chars = Array(s)
            var i = chars.count - 1
            while i >= 0 && chars[i] == "0" {
                chars[i] = "9"
                i -= 1
            }
            if i >= 0 {
                let digit = Int(String(chars[i]))!
                chars[i] = Character(String(digit - 1))
            }
            var start = 0
            while start < chars.count - 1 && chars[start] == "0" {
                start += 1
            }
            return String(chars[start...])
        }

        func count(_ s: String) -> Int {
            let digits = s.map { Int(String($0))! }
            let n = digits.count
            var memo = Array(repeating: Array(repeating: Array(repeating: -1, count: 2), count: 11), repeatCount: n + 1)

            func dfs(_ pos: Int, _ prev: Int, _ tight: Bool, _ started: Bool) -> Int {
                if pos == n {
                    return started ? 1 : 0
                }
                if !tight {
                    let pIdx = prev + 1
                    let sIdx = started ? 1 : 0
                    if memo[pos][pIdx][sIdx] != -1 {
                        return memo[pos][pIdx][sIdx]
                    }
                }

                let limit = tight ? digits[pos] : 9
                var res = 0
                for d in 0...limit {
                    let nextTight = tight && (d == limit)
                    if !started {
                        if d == 0 {
                            res = (res + dfs(pos + 1, -1, nextTight, false)) % MOD
                        } else {
                            res = (res + dfs(pos + 1, d, nextTight, true)) % MOD
                        }
                    } else {
                        if abs(d - prev) == 1 {
                            res = (res + dfs(pos + 1, d, nextTight, true)) % MOD
                        }
                    }
                }

                if !tight {
                    let pIdx = prev + 1
                    let sIdx = started ? 1 : 0
                    memo[pos][pIdx][sIdx] = res
                }
                return res
            }

            return dfs(0, -1, true, false)
        }

        let highCount = count(high)
        let lowMinusOne = decrement(low)
        let lowCount = (lowMinusOne == "0") ? 0 : count(lowMinusOne)

        var ans = highCount - lowCount
        if ans < 0 { ans += MOD }
        return ans % MOD
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val MOD = 1_000_000_007L

    fun countSteppingNumbers(low: String, high: String): Int {
        val highCount = countUpTo(high)
        val lowMinusOne = decString(low)
        val lowCount = if (lowMinusOne == "0") 0 else countUpTo(lowMinusOne)
        var ans = (highCount.toLong() - lowCount + MOD) % MOD
        return ans.toInt()
    }

    private fun countUpTo(s: String): Int {
        if (s == "0") return 0
        val n = s.length
        var total = 0L

        // Count stepping numbers with length shorter than n
        if (n > 1) {
            var dpPrev = LongArray(10)
            for (d in 1..9) dpPrev[d] = 1L
            var sumPrev = 9L
            total = (total + sumPrev) % MOD // length = 1
            for (len in 2 until n) {
                val dpCurr = LongArray(10)
                var sumCurr = 0L
                for (d in 0..9) {
                    var v = 0L
                    if (d > 0) v += dpPrev[d - 1]
                    if (d < 9) v += dpPrev[d + 1]
                    v %= MOD
                    dpCurr[d] = v
                    sumCurr = (sumCurr + v) % MOD
                }
                total = (total + sumCurr) % MOD
                dpPrev = dpCurr
            }
        }

        // DP for numbers with exact length n and <= s
        val memo = Array(n) { Array(11) { LongArray(2) { -1L } } }

        fun dfs(pos: Int, prev: Int, tight: Int): Long {
            if (pos == n) return 1L
            val idxPrev = if (prev == -1) 10 else prev
            var cached = memo[pos][idxPrev][tight]
            if (cached != -1L) return cached
            val limit = if (tight == 1) s[pos] - '0' else 9
            var ans = 0L
            if (prev == -1) {
                for (d in 1..limit) {
                    val nextTight = if (tight == 1 && d == limit) 1 else 0
                    ans += dfs(pos + 1, d, nextTight)
                    if (ans >= MOD) ans -= MOD
                }
            } else {
                val candidates = intArrayOf(prev - 1, prev + 1)
                for (d in candidates) {
                    if (d < 0 || d > 9) continue
                    if (d > limit) continue
                    val nextTight = if (tight == 1 && d == limit) 1 else 0
                    ans += dfs(pos + 1, d, nextTight)
                    if (ans >= MOD) ans -= MOD
                }
            }
            memo[pos][idxPrev][tight] = ans % MOD
            return ans % MOD
        }

        val exact = dfs(0, -1, 1)
        total = (total + exact) % MOD
        return total.toInt()
    }

    private fun decString(s: String): String {
        if (s == "0") return "0"
        val sb = StringBuilder(s)
        var i = sb.length - 1
        while (i >= 0 && sb[i] == '0') {
            sb.setCharAt(i, '9')
            i--
        }
        if (i >= 0) {
            sb.setCharAt(i, ((sb[i] - '0' - 1) + '0'.code).toChar())
        }
        var start = 0
        while (start < sb.length && sb[start] == '0') start++
        return if (start == sb.length) "0" else sb.substring(start)
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  String _decrement(String s) {
    List<int> chars = s.codeUnits;
    int i = chars.length - 1;
    while (i >= 0 && chars[i] == 48) { // '0'
      chars[i] = 57; // '9'
      i--;
    }
    if (i < 0) return "0";
    chars[i]--;
    int start = 0;
    while (start < chars.length - 1 && chars[start] == 48) start++;
    return String.fromCharCodes(chars.sublist(start));
  }

  int _countUpTo(String bound) {
    if (bound == "0") return 0;
    final List<int> digits = bound.codeUnits.map((c) => c - 48).toList();
    final int n = digits.length;

    // dp[pos][prev+1][started][tight] = value, -1 means uncomputed
    final List<List<List<List<int>>>> dp = List.generate(
        n + 1,
        (_) => List.generate(
            11,
            (_) => List.generate(2, (_) => List.filled(2, -1))));

    int dfs(int pos, int prev, int started, int tight) {
      if (pos == n) return started == 1 ? 1 : 0;
      int memo = dp[pos][prev + 1][started][tight];
      if (memo != -1) return memo;

      int limit = tight == 1 ? digits[pos] : 9;
      int ans = 0;
      for (int d = 0; d <= limit; ++d) {
        int nextTight = (tight == 1 && d == limit) ? 1 : 0;
        if (started == 0 && d == 0) {
          // still leading zeros, not started yet
          ans += dfs(pos + 1, -1, 0, nextTight);
        } else {
          if (started == 0) {
            // first non‑zero digit, no previous to compare
            ans += dfs(pos + 1, d, 1, nextTight);
          } else {
            if ((d - prev).abs() == 1) {
              ans += dfs(pos + 1, d, 1, nextTight);
            }
          }
        }
        if (ans >= _mod) ans -= _mod;
      }
      dp[pos][prev + 1][started][tight] = ans;
      return ans;
    }

    return dfs(0, -1, 0, 1);
  }

  int countSteppingNumbers(String low, String high) {
    String lowMinusOne = _decrement(low);
    int hi = _countUpTo(high);
    int lo = _countUpTo(lowMinusOne);
    int ans = hi - lo;
    ans %= _mod;
    if (ans < 0) ans += _mod;
    return ans;
  }
}
```

## Golang

```go
package main

import (
	"strconv"
)

const MOD int = 1000000007

func countSteppingNumbers(low string, high string) int {
	maxLen := len(high)
	if len(low) > maxLen {
		maxLen = len(low)
	}
	totalByLen := precomputeTotals(maxLen)

	fHigh := countUpTo(high, totalByLen)
	lowMinusOne := decString(low)
	fLowMinusOne := countUpTo(lowMinusOne, totalByLen)

	ans := fHigh - fLowMinusOne
	if ans < 0 {
		ans += MOD
	}
	return ans % MOD
}

func precomputeTotals(maxLen int) []int {
	total := make([]int, maxLen+1) // 1-indexed lengths
	prev := make([]int, 10)
	for d := 1; d <= 9; d++ {
		prev[d] = 1
	}
	sum := 0
	for d := 0; d <= 9; d++ {
		sum = (sum + prev[d]) % MOD
	}
	if maxLen >= 1 {
		total[1] = sum // should be 9
	}
	for l := 2; l <= maxLen; l++ {
		cur := make([]int, 10)
		for d := 0; d <= 9; d++ {
			val := 0
			if d-1 >= 0 {
				val = (val + prev[d-1]) % MOD
			}
			if d+1 <= 9 {
				val = (val + prev[d+1]) % MOD
			}
			cur[d] = val
		}
		sum = 0
		for d := 0; d <= 9; d++ {
			sum = (sum + cur[d]) % MOD
		}
		total[l] = sum
		prev = cur
	}
	return total
}

func countUpTo(s string, totalByLen []int) int {
	if s == "0" {
		return 0
	}
	n := len(s)
	ans := 0
	for l := 1; l < n; l++ {
		ans = (ans + totalByLen[l]) % MOD
	}
	ans = (ans + countSameLength(s)) % MOD
	return ans
}

func countSameLength(s string) int {
	n := len(s)
	type key struct {
		pos   int
		prev  int // -1 encoded as 10
		tight int // 0 or 1
	}
	memo := make(map[key]int)

	var dfs func(pos int, prev int, tight bool) int
	dfs = func(pos int, prev int, tight bool) int {
		if pos == n {
			return 1
		}
		k := key{pos, prev + 1, 0}
		if tight {
			k.tight = 1
		}
		if v, ok := memo[k]; ok {
			return v
		}
		limit := 9
		boundDigit := 0
		if tight {
			boundDigit = int(s[pos] - '0')
			limit = boundDigit
		}
		start := 0
		if pos == 0 {
			start = 1
		}
		total := 0
		for d := start; d <= limit; d++ {
			if prev != -1 && abs(d-prev) != 1 {
				continue
			}
			nextTight := tight && (d == boundDigit)
			total += dfs(pos+1, d, nextTight)
			if total >= MOD {
				total -= MOD
			}
		}
		memo[k] = total
		return total
	}
	return dfs(0, -1, true)
}

func decString(s string) string {
	if s == "0" {
		return "0"
	}
	b := []byte(s)
	i := len(b) - 1
	for i >= 0 && b[i] == '0' {
		b[i] = '9'
		i--
	}
	if i >= 0 {
		b[i]--
	}
	// trim leading zeros
	idx := 0
	for idx < len(b)-1 && b[idx] == '0' {
		idx++
	}
	return string(b[idx:])
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

// The following import is only to avoid unused import errors in the LeetCode environment.
var _ = strconv.Atoi("")
```

## Ruby

```ruby
MOD = 1_000_000_007

def precompute(max_len)
  dp = Array.new(max_len + 1) { Array.new(10, 0) }
  sum_len = Array.new(max_len + 1, 0)

  (1..9).each { |d| dp[1][d] = 1 }
  sum_len[1] = (1..9).sum % MOD

  (2..max_len).each do |l|
    (0..9).each do |d|
      val = 0
      val = (val + dp[l - 1][d - 1]) % MOD if d - 1 >= 0
      val = (val + dp[l - 1][d + 1]) % MOD if d + 1 <= 9
      dp[l][d] = val
    end
    sum_len[l] = dp[l].sum % MOD
  end

  [dp, sum_len]
end

def dec_str(s)
  bytes = s.bytes
  i = bytes.length - 1
  while i >= 0 && bytes[i] == 48 # '0'
    bytes[i] = 57 # '9'
    i -= 1
  end
  if i < 0
    return "0"
  else
    bytes[i] -= 1
    res = bytes.pack('C*').sub(/^0+/, '')
    res.empty? ? "0" : res
  end
end

def count_upto(s, sum_len)
  return 0 if s == "0"

  digits = s.chars.map(&:to_i)
  n = digits.length
  total = 0
  (1...n).each { |len| total = (total + sum_len[len]) % MOD }

  memo = Array.new(n) { Array.new(11) { Array.new(2, -1) } }

  dfs = nil
  dfs = lambda do |pos, prev, tight|
    return 1 if pos == n

    idx_prev = prev + 1
    t = tight ? 1 : 0
    cached = memo[pos][idx_prev][t]
    return cached unless cached == -1

    limit = tight ? digits[pos] : 9
    res = 0

    if prev == -1
      (1..limit).each do |d|
        next if d == 0
        new_tight = tight && (d == limit)
        res = (res + dfs.call(pos + 1, d, new_tight)) % MOD
      end
    else
      [prev - 1, prev + 1].each do |d|
        next if d < 0 || d > 9
        next if d > limit
        new_tight = tight && (d == limit)
        res = (res + dfs.call(pos + 1, d, new_tight)) % MOD
      end
    end

    memo[pos][idx_prev][t] = res
    res
  end

  total = (total + dfs.call(0, -1, true)) % MOD
  total
end

# @param {String} low
# @param {String} high
# @return {Integer}
def count_stepping_numbers(low, high)
  max_len = [low.length, high.length].max
  _, sum_len = precompute(max_len)

  low_minus_one = dec_str(low)
  cnt_high = count_upto(high, sum_len)
  cnt_low = count_upto(low_minus_one, sum_len)

  ans = (cnt_high - cnt_low) % MOD
  ans += MOD if ans < 0
  ans
end
```

## Scala

```scala
object Solution {
    val MOD = 1000000007L

    def countSteppingNumbers(low: String, high: String): Int = {

        def decOne(s: String): String = {
            if (s == "0") return "0"
            val sb = new StringBuilder(s)
            var i = sb.length - 1
            while (i >= 0 && sb.charAt(i) == '0') {
                sb.setCharAt(i, '9')
                i -= 1
            }
            if (i >= 0) {
                sb.setCharAt(i, ((sb.charAt(i) - '0' - 1 + '0').toChar))
            }
            var idx = 0
            while (idx < sb.length && sb.charAt(idx) == '0') idx += 1
            if (idx == sb.length) "0" else sb.substring(idx)
        }

        def count(bound: String): Int = {
            val n = bound.length
            val digits = bound.map(_.asDigit).toArray
            // dp[pos][prevIdx][tight][started]
            val dp = Array.ofDim[Long](n + 1, 11, 2, 2)
            val vis = Array.ofDim[Boolean](n + 1, 11, 2, 2)

            def dfs(pos: Int, prevIdx: Int, tight: Int, started: Int): Long = {
                if (pos == n) return if (started == 1) 1L else 0L
                if (vis(pos)(prevIdx)(tight)(started)) return dp(pos)(prevIdx)(tight)(started)

                var res = 0L
                val boundDigit = digits(pos)
                val limit = if (tight == 1) boundDigit else 9

                for (d <- 0 to limit) {
                    val nextTight = if (tight == 1 && d == boundDigit) 1 else 0
                    if (started == 0) {
                        if (d == 0) {
                            res += dfs(pos + 1, 10, nextTight, 0)
                        } else {
                            // start now, leading digit cannot be zero
                            res += dfs(pos + 1, d, nextTight, 1)
                        }
                    } else {
                        if (Math.abs(d - prevIdx) == 1) {
                            res += dfs(pos + 1, d, nextTight, 1)
                        }
                    }
                }

                res %= MOD
                vis(pos)(prevIdx)(tight)(started) = true
                dp(pos)(prevIdx)(tight)(started) = res
                res
            }

            dfs(0, 10, 1, 0).toInt
        }

        val lowMinusOne = decOne(low)
        val highCount = count(high)
        val lowCount = if (lowMinusOne == "0") 0 else count(lowMinusOne)

        ((highCount - lowCount) % MOD + MOD).toInt
    }
}
```

## Rust

```rust
use std::cmp::max;

const MOD: i64 = 1_000_000_007;

fn count_up_to(num: &String) -> i64 {
    let digits: Vec<u8> = num.bytes().map(|b| b - b'0').collect();
    let n = digits.len();
    // memo[pos][prev+1][tight][started]
    let mut memo = vec![vec![vec![vec![None; 2]; 2]; 11]; n + 1];

    fn dfs(
        pos: usize,
        prev: i32,
        tight: bool,
        started: bool,
        digits: &Vec<u8>,
        memo: &mut Vec<Vec<Vec<Vec<Option<i64>>>>>,
    ) -> i64 {
        if pos == digits.len() {
            return if started { 1 } else { 0 };
        }
        let prev_idx = (prev + 1) as usize;
        let ti = tight as usize;
        let si = started as usize;
        if let Some(v) = memo[pos][prev_idx][ti][si] {
            return v;
        }
        let limit = if tight { digits[pos] } else { 9 };
        let mut res: i64 = 0;
        for d in 0..=limit {
            let next_tight = tight && (d == limit);
            if !started {
                if d == 0 {
                    // still leading zeros
                    res += dfs(pos + 1, -1, next_tight, false, digits, memo);
                } else {
                    // start number with digit d
                    res += dfs(pos + 1, d as i32, next_tight, true, digits, memo);
                }
            } else {
                if (d as i32 - prev).abs() == 1 {
                    res += dfs(pos + 1, d as i32, next_tight, true, digits, memo);
                }
            }
        }
        res %= MOD;
        memo[pos][prev_idx][ti][si] = Some(res);
        res
    }

    dfs(0, -1, true, false, &digits, &mut memo)
}

fn dec_str(s: &String) -> String {
    let mut bytes: Vec<u8> = s.as_bytes().to_vec();
    let mut i: i32 = (bytes.len() as i32) - 1;
    while i >= 0 && bytes[i as usize] == b'0' {
        bytes[i as usize] = b'9';
        i -= 1;
    }
    if i >= 0 {
        bytes[i as usize] -= 1;
    }
    // strip leading zeros
    let mut start = 0usize;
    while start < bytes.len() && bytes[start] == b'0' {
        start += 1;
    }
    if start == bytes.len() {
        return "0".to_string();
    }
    String::from_utf8(bytes[start..].to_vec()).unwrap()
}

impl Solution {
    pub fn count_stepping_numbers(low: String, high: String) -> i32 {
        let high_cnt = count_up_to(&high);
        let low_minus_one = dec_str(&low);
        let low_cnt = count_up_to(&low_minus_one);
        ((high_cnt - low_cnt + MOD) % MOD) as i32
    }
}
```

## Racket

```racket
#lang racket

(define MOD 1000000007)

;; decrement a decimal string by one, assuming s > "0"
(define (dec-str s)
  (let* ([len (string-length s)]
         [chars (list->vector (for/list ([i (in-range len)]) (string-ref s i)))]
         [result (make-vector len #\0)])
    (let loop ([i (- len 1)] [borrow 1])
      (if (< i 0)
          (let* ([first-non-zero
                  (let find ([j 0])
                    (cond [(= j len) len]
                          [(char=? (vector-ref result j) #\0) (find (+ j 1))]
                          [else j]))]
                 [out (if (= first-non-zero len)
                          "0"
                          (list->string
                           (for/list ([k (in-range first-non-zero len)])
                             (vector-ref result k))))])
            out)
          (let* ([digit (- (char->integer (vector-ref chars i))
                           (char->integer #\0))]
                 [sub (- digit borrow)]
                 [new-borrow (if (< sub 0) 1 0)]
                 [final (if (< sub 0) (+ sub 10) sub)])
            (vector-set! result i
                         (integer->char (+ final (char->integer #\0))))
            (loop (- i 1) new-borrow))))))

;; count stepping numbers <= bound string s
(define (count-up-to s)
  (let* ([digits (map (λ (c) (- (char->integer c) (char->integer #\0)))
                      (string->list s))]
         [n (length digits)]
         [memo (make-hash)])
    (define (dp pos prev tight started)
      (if (= pos n)
          (if started 1 0)
          (let* ([key (vector pos prev (if tight 1 0) (if started 1 0))])
            (or (hash-ref memo key #f)
                (let* ([limit (if tight (list-ref digits pos) 9)]
                       [res
                        (let loop ([d 0] [acc 0])
                          (if (> d limit)
                              acc
                              (let* ([new-started (or started (not (= d 0)))]
                                     [valid?
                                      (cond [(not new-started) #t]
                                            [(not started) #t]
                                            [else (= (abs (- d prev)) 1)])]
                                     [new-prev (if new-started d prev)]
                                     [new-tight (and tight (= d limit))])
                                (if valid?
                                    (loop (+ d 1)
                                          (modulo (+ acc (dp (+ pos 1) new-prev new-tight new-started))
                                                  MOD))
                                    (loop (+ d 1) acc))))])])
                  (hash-set! memo key res)
                  res)))))
    (dp 0 10 #t #f))) ; prev=10 means undefined

;; main function with contract
(define/contract (count-stepping-numbers low high)
  (-> string? string? exact-integer?)
  (let* ([high-count (count-up-to high)]
         [low-minus-one (dec-str low)]
         [low-count (if (string=? low "0") 0 (count-up-to low-minus-one))]
         [ans (modulo (- high-count low-count) MOD)])
    ans))
```

## Erlang

```erlang
-define(MOD, 1000000007).

-spec count_stepping_numbers(Low :: unicode:unicode_binary(), High :: unicode:unicode_binary()) -> integer().
count_stepping_numbers(Low, High) ->
    HighCnt = count_up_to(High),
    LowMinusOne = dec_string(Low),
    LowCnt = count_up_to(LowMinusOne),
    Res = (HighCnt - LowCnt) rem ?MOD,
    if Res < 0 -> Res + ?MOD; true -> Res end.

%% count stepping numbers in [1, S]
count_up_to(<<"0">>) ->
    0;
count_up_to(S) ->
    Digits = [C - $0 || <<C>> <= S],
    InitMap = #{ {-1, 1, 0} => 1},
    FinalMap = lists:foldl(fun(Dig, Map) -> process_position(Dig, Map) end,
                           InitMap,
                           Digits),
    maps:fold(fun({_Prev, _Tight, Started}, Val, Acc) ->
                      case Started of
                          1 -> (Acc + Val) rem ?MOD;
                          _ -> Acc
                      end
              end, 0, FinalMap).

process_position(Digit, Map) ->
    maps:fold(
      fun({Prev, Tight, Started}, Count, AccMap) ->
          Limit = if Tight == 1 -> Digit; true -> 9 end,
          lists:foldl(
            fun(D, M) ->
                NewStarted = case {Started, D} of
                                 {0, 0} -> 0;
                                 _ -> 1
                             end,
                NewTight = if Tight == 1 andalso D == Limit -> 1 else 0 end,
                case NewStarted of
                    0 ->
                        add_to_map(M, {-1, NewTight, 0}, Count);
                    1 ->
                        case Started of
                            0 ->
                                add_to_map(M, {D, NewTight, 1}, Count);
                            1 ->
                                if erlang:abs(D - Prev) == 1 ->
                                       add_to_map(M, {D, NewTight, 1}, Count);
                                   true -> M
                                end
                        end
                end
            end,
            AccMap,
            lists:seq(0, Limit)
          )
      end,
      #{},
      Map).

add_to_map(Map, Key, Val) ->
    maps:update_with(Key,
                     fun(Old) -> (Old + Val) rem ?MOD end,
                     Val rem ?MOD,
                     Map).

dec_string(Bin) ->
    case erlang:list_to_integer(binary_to_list(Bin)) of
        0 -> <<"0">>;
        N -> integer_to_binary(N - 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @mod 1_000_000_007

  @spec count_stepping_numbers(low :: String.t(), high :: String.t()) :: integer
  def count_stepping_numbers(low, high) do
    max_len = max(String.length(low), String.length(high))
    dp_len = precompute(max_len)

    high_cnt = count_upto(high, dp_len)
    low_minus_one = dec_str(low)
    low_cnt = count_upto(low_minus_one, dp_len)

    ans = rem(high_cnt - low_cnt + @mod, @mod)
    ans
  end

  # Precompute dp[length][digit] : number of stepping numbers with given length ending with digit
  defp precompute(max_len) do
    base =
      for d <- 0..9, into: %{} do
        {d, if(d == 0, do: 0, else: 1)}
      end

    Enum.reduce(2..max_len, %{1 => base}, fn len, acc ->
      prev = Map.get(acc, len - 1)

      cur =
        for d <- 0..9, into: %{} do
          sum = 0

          if d - 1 >= 0 do
            sum = rem(sum + Map.get(prev, d - 1), @mod)
          end

          if d + 1 <= 9 do
            sum = rem(sum + Map.get(prev, d + 1), @mod)
          end

          {d, sum}
        end

      Map.put(acc, len, cur)
    end)
  end

  # Count stepping numbers in [1, s] (inclusive). Returns 0 for s == "0".
  defp count_upto("0", _dp_len), do: 0

  defp count_upto(s, dp_len) do
    n = String.length(s)

    short_total =
      Enum.reduce(1..(n - 1), 0, fn len, acc ->
        map = Map.get(dp_len, len)
        sum_len = Enum.reduce(map, 0, fn {_d, v}, a -> rem(a + v, @mod) end)
        rem(acc + sum_len, @mod)
      end)

    digits = s |> String.codepoints() |> Enum.map(&String.to_integer/1)
    same_total = count_same_length(digits, dp_len)

    rem(short_total + same_total, @mod)
  end

  # DP for numbers with the same length as bound
  defp count_same_length(digits, _dp_len) do
    n = length(digits)

    init_dp = %{{-1, true} => 1}

    final_dp =
      Enum.reduce(0..(n - 1), init_dp, fn pos, cur_dp ->
        limit_digit = Enum.at(digits, pos)

        Enum.reduce(cur_dp, %{}, fn {{prev, tight}, cnt}, ndp ->
          max_digit = if tight, do: limit_digit, else: 9
          min_digit = if pos == 0, do: 1, else: 0

          Enum.reduce(min_digit..max_digit, ndp, fn cur, acc2 ->
            cond_ok =
              prev == -1 or abs(prev - cur) == 1

            if cond_ok do
              new_tight = tight and (cur == limit_digit)
              key = {cur, new_tight}
              existing = Map.get(acc2, key, 0)
              Map.put(acc2, key, rem(existing + cnt, @mod))
            else
              acc2
            end
          end)
        end)
      end)

    Enum.reduce(final_dp, 0, fn {_k, v}, sum -> rem(sum + v, @mod) end)
  end

  # Decrement a numeric string by one.
  defp dec_str("0"), do: "0"

  defp dec_str(s) do
    chars = String.to_charlist(s)

    {new_chars_rev, _borrow} =
      Enum.reduce(Enum.reverse(chars), {[], 1}, fn ch, {acc, borrow} ->
        d = ch - ?0
        nd = d - borrow

        if nd < 0 do
          {[?0 + (nd + 10) | acc], 1}
        else
          {[?0 + nd | acc], 0}
        end
      end)

    trimmed = Enum.drop_while(new_chars_rev, &(&1 == ?0))

    case trimmed do
      [] -> "0"
      _ -> to_string(trimmed)
    end
  end
end
```
