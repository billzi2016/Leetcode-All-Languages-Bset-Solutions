# 3519. Count Numbers with Non-Decreasing Digits

## Cpp

```cpp
class Solution {
public:
    static const int MOD = 1000000007;
    string bound;
    int base, n;
    long long dp[105][11][2][2];
    bool vis[105][11][2][2];

    long long dfs(int pos, int last, bool tight, bool started) {
        if (pos == n) return 1; // count the formed number (including zero)
        int li = (last == -1 ? base : last);
        int ti = tight ? 1 : 0;
        int si = started ? 1 : 0;
        if (vis[pos][li][ti][si]) return dp[pos][li][ti][si];
        vis[pos][li][ti][si] = true;
        long long res = 0;
        int limit = tight ? bound[pos] - '0' : base - 1;
        for (int d = 0; d <= limit; ++d) {
            bool ntight = tight && (d == limit);
            if (!started && d == 0) {
                res += dfs(pos + 1, -1, ntight, false);
            } else if (!started) { // first non‑zero digit
                res += dfs(pos + 1, d, ntight, true);
            } else {
                if (d < last) continue;
                res += dfs(pos + 1, d, ntight, true);
            }
            if (res >= MOD) res -= MOD;
        }
        dp[pos][li][ti][si] = res % MOD;
        return dp[pos][li][ti][si];
    }

    long long countUpTo(const string& s) {
        bound = s;
        n = s.size();
        memset(vis, 0, sizeof(vis));
        return dfs(0, -1, true, false) % MOD;
    }

    string decOne(string s) { // s > 0 in base 'base'
        int i = (int)s.size() - 1;
        while (i >= 0 && s[i] == '0') {
            s[i] = char('0' + (base - 1));
            --i;
        }
        if (i < 0) return "0";
        s[i] = char(s[i] - 1);
        int pos = 0;
        while (pos + 1 < (int)s.size() && s[pos] == '0') ++pos;
        if (pos > 0) s = s.substr(pos);
        return s;
    }

    int countNumbers(string l, string r, int b) {
        base = b;
        long long cntR = countUpTo(r);
        string lMinusOne = decOne(l);
        long long cntL = countUpTo(lMinusOne);
        long long ans = (cntR - cntL) % MOD;
        if (ans < 0) ans += MOD;
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    private static final long MOD = 1_000_000_007L;
    private int base;
    private java.util.List<Integer> digits;
    private Long[][][][] memo;

    private long dfs(int pos, int prevIdx, int tight, int started) {
        if (pos == digits.size()) {
            return 1; // a valid number (including zero)
        }
        Long cached = memo[pos][prevIdx][tight][started];
        if (cached != null) return cached;
        int limit = tight == 1 ? digits.get(pos) : base - 1;
        long res = 0;
        for (int d = 0; d <= limit; ++d) {
            int nextTight = (tight == 1 && d == limit) ? 1 : 0;
            if (started == 0 && d == 0) {
                // still leading zeros
                res += dfs(pos + 1, 0, nextTight, 0);
            } else {
                int prevDigit = (prevIdx == 0) ? -1 : prevIdx - 1;
                if (started == 0 || d >= prevDigit) {
                    res += dfs(pos + 1, d + 1, nextTight, 1);
                }
            }
            if (res >= MOD) res -= MOD;
        }
        memo[pos][prevIdx][tight][started] = res % MOD;
        return memo[pos][prevIdx][tight][started];
    }

    private java.util.List<Integer> toBaseDigits(java.math.BigInteger value) {
        if (value.equals(java.math.BigInteger.ZERO)) {
            return java.util.Collections.singletonList(0);
        }
        java.util.ArrayList<Integer> list = new java.util.ArrayList<>();
        java.math.BigInteger b = java.math.BigInteger.valueOf(base);
        while (value.compareTo(java.math.BigInteger.ZERO) > 0) {
            java.math.BigInteger[] dr = value.divideAndRemainder(b);
            list.add(dr[1].intValue());
            value = dr[0];
        }
        java.util.Collections.reverse(list);
        return list;
    }

    private long countUpTo(String s) {
        java.math.BigInteger val = new java.math.BigInteger(s);
        digits = toBaseDigits(val);
        int n = digits.size();
        memo = new Long[n][base + 1][2][2];
        return dfs(0, 0, 1, 0) % MOD;
    }

    public int countNumbers(String l, String r, int b) {
        this.base = b;
        long cntR = countUpTo(r);
        java.math.BigInteger lv = new java.math.BigInteger(l);
        long cntLMinus1;
        if (lv.equals(java.math.BigInteger.ZERO)) {
            cntLMinus1 = 0;
        } else {
            String lMinusOne = lv.subtract(java.math.BigInteger.ONE).toString();
            cntLMinus1 = countUpTo(lMinusOne);
        }
        long ans = (cntR - cntLMinus1) % MOD;
        if (ans < 0) ans += MOD;
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def countNumbers(self, l, r, b):
        """
        :type l: str
        :type r: str
        :type b: int
        :rtype: int
        """
        MOD = 10**9 + 7

        def to_base_digits(num_str):
            n = int(num_str)
            if n == 0:
                return [0]
            digs = []
            while n:
                digs.append(n % b)
                n //= b
            digs.reverse()
            return digs

        from functools import lru_cache

        def count_up_to(num_str):
            n_int = int(num_str)
            if n_int == 0:
                return 0
            digits = to_base_digits(num_str)
            m = len(digits)

            @lru_cache(None)
            def dp(pos, prev, tight, started):
                if pos == m:
                    return 1 if started else 0
                limit = digits[pos] if tight else b - 1
                total = 0
                for d in range(limit + 1):
                    ntight = tight and (d == limit)
                    nstarted = started or d != 0
                    if not nstarted:
                        # still leading zeros, prev irrelevant
                        total += dp(pos + 1, 0, ntight, False)
                    else:
                        if not started:
                            # first non‑zero digit, no previous constraint
                            total += dp(pos + 1, d, ntight, True)
                        else:
                            if d >= prev:
                                total += dp(pos + 1, d, ntight, True)
                return total % MOD

            return dp(0, 0, True, False)

        # compute l-1
        l_int = int(l)
        l_minus_one = str(l_int - 1) if l_int > 0 else "0"

        ans = (count_up_to(r) - count_up_to(l_minus_one)) % MOD
        return ans
```

## Python3

```python
import sys
from functools import lru_cache

MOD = 10**9 + 7

class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        def to_base_digits(x: int):
            if x == 0:
                return [0]
            digs = []
            while x:
                digs.append(x % b)
                x //= b
            return digs[::-1]

        def count_upto(num_str: str) -> int:
            x = int(num_str)
            if x < 0:
                return 0
            digits = to_base_digits(x)
            n = len(digits)

            @lru_cache(None)
            def dfs(pos: int, prev: int, tight: bool, started: bool) -> int:
                if pos == n:
                    # reached end, count this number (including zero when not started)
                    return 1
                limit = digits[pos] if tight else b - 1
                total = 0
                for d in range(limit + 1):
                    ntight = tight and (d == limit)
                    if not started:
                        if d == 0:
                            total += dfs(pos + 1, 0, ntight, False)
                        else:
                            total += dfs(pos + 1, d, ntight, True)
                    else:
                        if d >= prev:
                            total += dfs(pos + 1, d, ntight, True)
                return total % MOD

            return dfs(0, 0, True, False)

        # compute answer = f(r) - f(l-1)
        l_int = int(l)
        ans = (count_upto(r) - count_upto(str(l_int - 1))) % MOD
        return ans
```

## C

```c
#include <stdio.h>
#include <string.h>

#define MAXLEN 350
#define MOD 1000000007LL

static int B;
static int gDigits[MAXLEN];
static int gLen;
static long long memo[MAXLEN][11][2];

static long long dfs(int pos, int prev, int started, int tight) {
    if (pos == gLen) {
        return 1; // count the constructed number (zero included)
    }
    if (!tight && memo[pos][prev][started] != -1LL) {
        return memo[pos][prev][started];
    }
    int maxDigit = tight ? gDigits[pos] : B - 1;
    long long ans = 0;
    for (int d = 0; d <= maxDigit; ++d) {
        int nextTight = tight && (d == maxDigit);
        if (!started && d == 0) {
            ans += dfs(pos + 1, prev, 0, nextTight);
        } else if (!started) { // start now with non‑zero digit
            ans += dfs(pos + 1, d, 1, nextTight);
        } else {
            if (d >= prev) {
                ans += dfs(pos + 1, d, 1, nextTight);
            }
        }
        if (ans >= MOD) ans -= MOD;
    }
    if (!tight) memo[pos][prev][started] = ans;
    return ans;
}

/* convert decimal string to base B digits (most significant first) */
static void toBase(const char *s) {
    int dec[200];
    int decLen = strlen(s);
    for (int i = 0; i < decLen; ++i) dec[i] = s[i] - '0';

    if (decLen == 1 && dec[0] == 0) { // zero
        gLen = 1;
        gDigits[0] = 0;
        return;
    }

    int baseDigits[MAXLEN];
    int baseLen = 0;

    while (decLen > 0) {
        int newDec[200];
        int newLen = 0;
        int carry = 0;
        for (int i = 0; i < decLen; ++i) {
            int cur = carry * 10 + dec[i];
            int q = cur / B;
            carry = cur % B;
            if (newLen > 0 || q > 0) newDec[newLen++] = q;
        }
        baseDigits[baseLen++] = carry; // remainder
        memcpy(dec, newDec, newLen * sizeof(int));
        decLen = newLen;
    }

    gLen = baseLen;
    for (int i = 0; i < baseLen; ++i) {
        gDigits[i] = baseDigits[baseLen - 1 - i];
    }
}

/* count numbers in [0, N] satisfying condition */
static long long countUpTo(const char *N) {
    toBase(N);
    for (int i = 0; i < gLen; ++i)
        for (int p = 0; p <= B; ++p)
            memo[i][p][0] = memo[i][p][1] = -1LL;
    return dfs(0, 0, 0, 1) % MOD;
}

/* compute s-1 where s > "0", result stored in out (no leading zeros unless zero) */
static void decMinusOne(const char *s, char *out) {
    int n = strlen(s);
    char tmp[105];
    strcpy(tmp, s);
    int i = n - 1;
    while (i >= 0 && tmp[i] == '0') {
        tmp[i] = '9';
        --i;
    }
    if (i >= 0) {
        tmp[i]--;
    }
    int start = 0;
    while (start < n - 1 && tmp[start] == '0') ++start;
    strcpy(out, tmp + start);
}

/* main entry */
int countNumbers(char* l, char* r, int b) {
    B = b;
    long long cntR = countUpTo(r);

    if (strcmp(l, "0") == 0) {
        return (int)(cntR % MOD);
    }

    char lminus[105];
    decMinusOne(l, lminus);
    long long cntL = countUpTo(lminus);

    long long ans = cntR - cntL;
    ans %= MOD;
    if (ans < 0) ans += MOD;
    return (int)ans;
}
```

## Csharp

```csharp
using System;
using System.Numerics;
using System.Collections.Generic;

public class Solution {
    private const long MOD = 1000000007L;
    
    public int CountNumbers(string l, string r, int b) {
        BigInteger L = BigInteger.Parse(l);
        BigInteger R = BigInteger.Parse(r);
        long ansR = CountUpTo(R, b);
        long ansL = 0;
        if (L > 0) {
            ansL = CountUpTo(L - 1, b);
        }
        long res = (ansR - ansL) % MOD;
        if (res < 0) res += MOD;
        return (int)res;
    }
    
    private long CountUpTo(BigInteger N, int baseB) {
        // digits of N in baseB, most significant first
        List<int> digList = new List<int>();
        if (N.IsZero) {
            digList.Add(0);
        } else {
            while (!N.IsZero) {
                BigInteger[] divRem = BigInteger.DivRem(N, baseB, out BigInteger rem);
                digList.Add((int)rem);
                N = divRem;
            }
            digList.Reverse();
        }
        int len = digList.Count;
        int[] digits = digList.ToArray(); // most significant to least
        
        // dp[pos][prevIdx][started] where prevIdx: 0..baseB-1 actual digit, baseB means no previous (not started)
        long[,,] memo = new long[len, baseB + 1, 2];
        for (int i = 0; i < len; i++)
            for (int j = 0; j <= baseB; j++)
                for (int k = 0; k < 2; k++)
                    memo[i, j, k] = -1;
        
        long Dfs(int pos, int prevIdx, bool tight, bool started) {
            if (pos == len) {
                // reached end, count this number (including zero when not started)
                return 1L;
            }
            if (!tight && memo[pos, prevIdx, started ? 1 : 0] != -1) {
                return memo[pos, prevIdx, started ? 1 : 0];
            }
            int limit = tight ? digits[pos] : baseB - 1;
            long total = 0L;
            for (int d = 0; d <= limit; d++) {
                bool ntight = tight && (d == limit);
                if (!started) {
                    if (d == 0) {
                        // still leading zeros
                        total += Dfs(pos + 1, baseB, ntight, false);
                    } else {
                        // start now, no previous constraint
                        total += Dfs(pos + 1, d, ntight, true);
                    }
                } else {
                    if (d >= prevIdx) {
                        total += Dfs(pos + 1, d, ntight, true);
                    }
                }
                if (total >= MOD) total -= MOD;
            }
            if (!tight) {
                memo[pos, prevIdx, started ? 1 : 0] = total;
            }
            return total;
        }
        
        long result = Dfs(0, baseB, true, false) % MOD;
        // subtract the count of numbers > N? No, Dfs counts numbers <= N already.
        // It also includes zero; that's intended.
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} l
 * @param {string} r
 * @param {number} b
 * @return {number}
 */
var countNumbers = function(l, r, b) {
    const MOD = 1000000007;

    // subtract 1 from a decimal string (assumes s > "0")
    function decOne(s) {
        let arr = s.split('');
        let i = arr.length - 1;
        while (i >= 0 && arr[i] === '0') {
            arr[i] = '9';
            i--;
        }
        if (i >= 0) {
            arr[i] = String.fromCharCode(arr[i].charCodeAt(0) - 1);
        }
        // remove leading zeros
        while (arr.length > 1 && arr[0] === '0') arr.shift();
        return arr.join('');
    }

    // convert decimal string to array of base-b digits (most significant first)
    function toBaseDigits(s) {
        if (s === "0") return [0];
        let digits = [];
        let cur = s;
        while (cur !== "0") {
            let carry = 0;
            let next = '';
            for (let ch of cur) {
                const num = carry * 10 + (ch.charCodeAt(0) - 48);
                const q = Math.floor(num / b);
                const r = num % b;
                if (!(next === '' && q === 0)) next += String.fromCharCode(q + 48);
                carry = r;
            }
            digits.push(carry); // remainder
            cur = next === '' ? '0' : next;
        }
        digits.reverse();
        return digits;
    }

    function countUpTo(numStr) {
        if (numStr == null) return 0;
        const digits = toBaseDigits(numStr);
        const n = digits.length;
        const memo = new Map();

        function dfs(pos, last, started, tight) {
            if (pos === n) return 1; // valid number
            const key = pos + '|' + (last + 1) + '|' + (started ? 1 : 0) + '|' + (tight ? 1 : 0);
            if (!tight && memo.has(key)) return memo.get(key);
            let limit = tight ? digits[pos] : b - 1;
            let res = 0;
            for (let d = 0; d <= limit; d++) {
                const newStarted = started || d !== 0;
                let newLast = last;
                if (!newStarted) {
                    // still leading zeros, last irrelevant
                    newLast = -1;
                } else {
                    if (!started) {
                        // first non‑zero digit
                        newLast = d;
                    } else {
                        if (d < last) continue; // violates non‑decreasing
                        newLast = d;
                    }
                }
                const newTight = tight && (d === limit);
                res += dfs(pos + 1, newLast, newStarted, newTight);
                if (res >= MOD) res -= MOD;
            }
            if (!tight) memo.set(key, res);
            return res;
        }

        return dfs(0, -1, false, true);
    }

    const lMinus = (l === "0") ? null : decOne(l);
    let ans = countUpTo(r) - (lMinus === null ? 0 : countUpTo(lMinus));
    ans %= MOD;
    if (ans < 0) ans += MOD;
    return ans;
};
```

## Typescript

```typescript
function countNumbers(l: string, r: string, b: number): number {
    const MOD = 1000000007;

    function decStrMinusOne(s: string): string {
        if (s === "0") return "-1";
        const arr = s.split('').map(ch => ch.charCodeAt(0) - 48);
        let i = arr.length - 1;
        while (i >= 0 && arr[i] === 0) {
            arr[i] = 9;
            i--;
        }
        if (i >= 0) arr[i]--;
        let start = 0;
        while (start < arr.length && arr[start] === 0) start++;
        return start === arr.length ? "0" : arr.slice(start).join('');
    }

    function decStrToBaseDigits(s: string, base: number): number[] {
        if (s === "0") return [0];
        const res: number[] = [];
        let cur = s;
        while (cur !== "0") {
            let carry = 0;
            let next = "";
            for (let i = 0; i < cur.length; i++) {
                const num = carry * 10 + (cur.charCodeAt(i) - 48);
                const q = Math.floor(num / base);
                carry = num % base;
                if (!(next === "" && q === 0)) next += String.fromCharCode(48 + q);
            }
            res.push(carry);
            cur = next === "" ? "0" : next;
        }
        res.reverse();
        return res;
    }

    function countUpTo(bound: string): number {
        const digits = decStrToBaseDigits(bound, b);
        const n = digits.length;
        // dp[pos][prev][started] = value when tight == false
        const dp: number[][][] = Array.from({ length: n + 1 }, () =>
            Array.from({ length: b }, () => Array(2).fill(-1))
        );

        function dfs(pos: number, prev: number, started: number, tight: boolean): number {
            if (pos === n) return 1; // valid number (including zero)
            if (!tight && dp[pos][prev][started] !== -1) return dp[pos][prev][started];

            const limit = tight ? digits[pos] : b - 1;
            let total = 0;

            for (let d = 0; d <= limit; d++) {
                const nextTight = tight && d === limit;
                if (!started && d === 0) {
                    // still leading zeros
                    total += dfs(pos + 1, 0, 0, nextTight);
                } else if (!started) {
                    // first non‑zero digit
                    total += dfs(pos + 1, d, 1, nextTight);
                } else {
                    // already started, enforce non‑decreasing
                    if (d < prev) continue;
                    total += dfs(pos + 1, d, 1, nextTight);
                }
                if (total >= MOD) total -= MOD;
            }

            if (!tight) dp[pos][prev][started] = total;
            return total;
        }

        return dfs(0, 0, 0, true) % MOD;
    }

    const cntR = countUpTo(r);
    let cntL = 0;
    if (l !== "0") {
        const lMinusOne = decStrMinusOne(l);
        cntL = countUpTo(lMinusOne);
    }
    let ans = cntR - cntL;
    ans %= MOD;
    if (ans < 0) ans += MOD;
    return ans;
}
```

## Php

```php
<?php
class Solution {
    const MOD = 1000000007;

    /**
     * @param String $l
     * @param String $r
     * @param Integer $b
     * @return Integer
     */
    function countNumbers($l, $r, $b) {
        $mod = self::MOD;
        // helper: decimal string minus one
        $decMinusOne = function(string $s): string {
            if ($s === "0") return "0";
            $i = strlen($s) - 1;
            while ($i >= 0 && $s[$i] === '0') {
                $s[$i] = '9';
                $i--;
            }
            if ($i < 0) return "0";
            $s[$i] = chr(ord($s[$i]) - 1);
            $s = ltrim($s, '0');
            return $s === '' ? '0' : $s;
        };

        // helper: convert decimal string to base-b digits (most significant first)
        $toBaseDigits = function(string $s) use ($b): array {
            if ($s === "0") return [0];
            $digits = [];
            $num = $s;
            while ($num !== "0") {
                $carry = 0;
                $new = '';
                $len = strlen($num);
                for ($i = 0; $i < $len; $i++) {
                    $cur = $carry * 10 + (int)$num[$i];
                    $quot = intdiv($cur, $b);
                    $rem = $cur % $b;
                    if (!($new === '' && $quot == 0)) {
                        $new .= chr(ord('0') + $quot);
                    }
                    $carry = $rem;
                }
                $digits[] = $carry; // remainder is least significant digit
                $num = $new === '' ? '0' : $new;
            }
            return array_reverse($digits);
        };

        // DP to count numbers <= bound with non-decreasing base-b digits
        $countUpTo = function(array $digits) use ($b, $mod): int {
            $n = count($digits);
            $memo = [];

            $dfs = function(int $pos, int $prev, bool $tight, bool $started) use (&$dfs, &$memo, $digits, $n, $b, $mod): int {
                if ($pos === $n) {
                    // reached end; count this number (including zero)
                    return 1;
                }
                $key = $pos . '|' . $prev . '|' . ($tight ? 1 : 0) . '|' . ($started ? 1 : 0);
                if (!$tight && isset($memo[$key])) {
                    return $memo[$key];
                }

                $limit = $tight ? $digits[$pos] : ($b - 1);
                $res = 0;
                for ($d = 0; $d <= $limit; $d++) {
                    $nextStarted = $started || $d != 0;
                    if (!$nextStarted) {
                        // still leading zeros, prev unchanged
                        $res += $dfs($pos + 1, $prev, $tight && $d == $limit, false);
                    } else {
                        if ($started) {
                            if ($d < $prev) continue; // must be non-decreasing
                        }
                        $newPrev = $d;
                        $res += $dfs($pos + 1, $newPrev, $tight && $d == $limit, true);
                    }
                    if ($res >= $mod) $res -= $mod;
                }

                if (!$tight) {
                    $memo[$key] = $res;
                }
                return $res % $mod;
            };

            return $dfs(0, -1, true, false) % $mod;
        };

        $rDigits = $toBaseDigits($r);
        $cntR = $countUpTo($rDigits);

        $lMinusOne = $decMinusOne($l);
        $lDigits = $toBaseDigits($lMinusOne);
        $cntL = $countUpTo($lDigits);

        $ans = ($cntR - $cntL) % $mod;
        if ($ans < 0) $ans += $mod;
        return $ans;
    }
}
?>
```

## Swift

```swift
class Solution {
    func countNumbers(_ l: String, _ r: String, _ b: Int) -> Int {
        let MOD = 1_000_000_007

        func toBase(_ s: String, _ base: Int) -> [Int] {
            var digits = s.map { Int(String($0))! }
            if digits.count == 1 && digits[0] == 0 { return [0] }
            var res: [Int] = []
            while !(digits.isEmpty || (digits.count == 1 && digits[0] == 0)) {
                var carry = 0
                var newDigits: [Int] = []
                var started = false
                for d in digits {
                    let cur = carry * 10 + d
                    let q = cur / base
                    let r = cur % base
                    if q != 0 || started {
                        newDigits.append(q)
                        started = true
                    }
                    carry = r
                }
                res.append(carry)
                digits = newDigits
            }
            if res.isEmpty { res.append(0) }
            return res.reversed()
        }

        func decOne(_ s: String) -> String? {
            var chars = Array(s)
            var i = chars.count - 1
            while i >= 0 && chars[i] == "0" {
                chars[i] = "9"
                i -= 1
            }
            if i < 0 { return nil } // underflow, original was "0"
            let digit = Int(String(chars[i]))! - 1
            chars[i] = Character(String(digit))
            var start = 0
            while start < chars.count - 1 && chars[start] == "0" {
                start += 1
            }
            return String(chars[start...])
        }

        func countUpTo(_ s: String) -> Int {
            let digits = toBase(s, b)
            let n = digits.count

            struct Key: Hashable {
                let pos: Int
                let prev: Int
                let started: Int
            }
            var cache = [Key: Int]()

            func dfs(_ pos: Int, _ prev: Int, _ tight: Bool, _ started: Bool) -> Int {
                if pos == n { return 1 } // count this number (including zero)
                if !tight {
                    let key = Key(pos: pos, prev: prev, started: started ? 1 : 0)
                    if let val = cache[key] { return val }
                }
                let maxDigit = tight ? digits[pos] : b - 1
                var res = 0
                for d in 0...maxDigit {
                    let ntight = tight && (d == digits[pos])
                    if !started && d == 0 {
                        let v = dfs(pos + 1, 0, ntight, false)
                        res += v
                        if res >= MOD { res -= MOD }
                    } else {
                        if !started {
                            // first non‑zero digit
                            let v = dfs(pos + 1, d, ntight, true)
                            res += v
                            if res >= MOD { res -= MOD }
                        } else {
                            if d >= prev {
                                let v = dfs(pos + 1, d, ntight, true)
                                res += v
                                if res >= MOD { res -= MOD }
                            }
                        }
                    }
                }
                if !tight {
                    let key = Key(pos: pos, prev: prev, started: started ? 1 : 0)
                    cache[key] = res
                }
                return res
            }

            return dfs(0, 0, true, false) % MOD
        }

        let cntR = countUpTo(r)
        var cntLMinus = 0
        if let lMinus = decOne(l) {
            cntLMinus = countUpTo(lMinus)
        }
        var ans = cntR - cntLMinus
        ans %= MOD
        if ans < 0 { ans += MOD }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val MOD = 1_000_000_007

    fun countNumbers(l: String, r: String, b: Int): Int {
        val cntR = countUpTo(r, b)
        val lMinusOne = java.math.BigInteger(l).subtract(java.math.BigInteger.ONE)
        val cntL = if (lMinusOne.signum() < 0) 0 else countUpTo(lMinusOne.toString(), b)
        var ans = cntR - cntL
        if (ans < 0) ans += MOD
        return ans % MOD
    }

    private fun countUpTo(s: String, b: Int): Int {
        val big = java.math.BigInteger(s)
        if (big.signum() < 0) return 0
        val digitsStr = big.toString(b)               // base‑b representation
        val n = digitsStr.length
        val digits = IntArray(n) { digitsStr[it] - '0' }

        // memo[pos][tight][started][prevIdx]; prevIdx == b means “no previous digit”
        val memo = Array(n + 1) { Array(2) { Array(2) { IntArray(b + 1) { -1 } } } }

        fun dfs(pos: Int, tight: Int, started: Int, prevIdx: Int): Int {
            if (pos == n) return 1
            var cached = memo[pos][tight][started][prevIdx]
            if (cached != -1) return cached

            val limit = if (tight == 1) digits[pos] else b - 1
            var ans = 0L
            for (d in 0..limit) {
                val newTight = if (tight == 1 && d == limit) 1 else 0
                val newStarted = if (started == 1 || d != 0) 1 else 0
                if (newStarted == 1) {
                    if (started == 0) {                     // first non‑zero digit
                        ans = (ans + dfs(pos + 1, newTight, 1, d)) % MOD
                    } else {
                        val prev = prevIdx
                        if (d >= prev) {
                            ans = (ans + dfs(pos + 1, newTight, 1, d)) % MOD
                        }
                    }
                } else {                                    // still leading zeros
                    ans = (ans + dfs(pos + 1, newTight, 0, b)) % MOD
                }
            }
            cached = ans.toInt()
            memo[pos][tight][started][prevIdx] = cached
            return cached
        }

        return dfs(0, 1, 0, b)
    }
}
```

## Dart

```dart
class Solution {
  static const int MOD = 1000000007;
  late List<int> _digits;
  late int _len;
  late int _base;
  late List<List<List<List<int>>>> _dp;

  int countNumbers(String l, String r, int b) {
    _base = b;
    int cntR = _countUpTo(r);
    if (l == "0") return cntR % MOD;
    BigInt lMinusOne = BigInt.parse(l) - BigInt.one;
    int cntL = _countUpTo(lMinusOne.toString());
    int ans = cntR - cntL;
    ans %= MOD;
    if (ans < 0) ans += MOD;
    return ans;
  }

  int _countUpTo(String s) {
    BigInt n = BigInt.parse(s);
    _digits = _toBase(n, _base);
    _len = _digits.length;
    _dp = List.generate(_len, (_) =>
        List.generate(2, (_) =>
            List.generate(2, (_) => List.filled(_base, -1))));
    return _dfs(0, 1, 0, 0);
  }

  List<int> _toBase(BigInt n, int base) {
    if (n == BigInt.zero) return [0];
    List<int> rev = [];
    BigInt bBig = BigInt.from(base);
    while (n > BigInt.zero) {
      rev.add((n % bBig).toInt());
      n ~/= bBig;
    }
    return rev.reversed.toList();
  }

  int _dfs(int pos, int tight, int started, int prev) {
    if (pos == _len) return 1;
    int cached = _dp[pos][tight][started][prev];
    if (cached != -1) return cached;
    int limit = tight == 1 ? _digits[pos] : _base - 1;
    int res = 0;
    for (int d = 0; d <= limit; ++d) {
      int newTight = (tight == 1 && d == limit) ? 1 : 0;
      if (started == 0 && d == 0) {
        res += _dfs(pos + 1, newTight, 0, 0);
      } else if (started == 0) {
        res += _dfs(pos + 1, newTight, 1, d);
      } else {
        if (d < prev) continue;
        res += _dfs(pos + 1, newTight, 1, d);
      }
      if (res >= MOD) res -= MOD;
    }
    _dp[pos][tight][started][prev] = res % MOD;
    return _dp[pos][tight][started][prev];
  }
}
```

## Golang

```go
package main

import (
	"math/big"
)

const MOD int64 = 1000000007

func countNumbers(l string, r string, b int) int {
	f := func(s string) int64 {
		if s == "" {
			return 0
		}
		digits := toBaseDigits(s, b)
		n := len(digits)

		// dp[pos][prev][tight][started] = count, -1 means uncomputed
		dp := make([][][][]int64, n)
		for i := 0; i < n; i++ {
			dp[i] = make([][][]int64, b)
			for p := 0; p < b; p++ {
				dp[i][p] = make([][]int64, 2)
				for t := 0; t < 2; t++ {
					dp[i][p][t] = make([]int64, 2)
					for s := 0; s < 2; s++ {
						dp[i][p][t][s] = -1
					}
				}
			}
		}

		var dfs func(pos int, prev int, tight int, started int) int64
		dfs = func(pos int, prev int, tight int, started int) int64 {
			if pos == n {
				return 1 // count this number (including zero)
			}
			if dp[pos][prev][tight][started] != -1 {
				return dp[pos][prev][tight][started]
			}
			maxDigit := b - 1
			if tight == 1 {
				maxDigit = digits[pos]
			}
			var res int64 = 0
			for d := 0; d <= maxDigit; d++ {
				nextTight := 0
				if tight == 1 && d == digits[pos] {
					nextTight = 1
				}
				nextStarted := started
				nextPrev := prev
				if started == 0 && d == 0 {
					// still not started, keep prev as is (any value)
				} else {
					if started == 1 && d < prev {
						continue // violates non‑decreasing property
					}
					nextStarted = 1
					nextPrev = d
				}
				res += dfs(pos+1, nextPrev, nextTight, nextStarted)
				if res >= MOD {
					res -= MOD
				}
			}
			dp[pos][prev][tight][started] = res % MOD
			return dp[pos][prev][tight][started]
		}

		return dfs(0, 0, 1, 0) % MOD
	}

	leftCount := int64(0)
	if l != "0" {
		lMinusOne := decMinusOne(l)
		leftCount = f(lMinusOne)
	}
	rightCount := f(r)

	ans := (rightCount - leftCount) % MOD
	if ans < 0 {
		ans += MOD
	}
	return int(ans)
}

// convert decimal string to slice of base‑b digits (most significant first)
func toBaseDigits(s string, b int) []int {
	n := new(big.Int)
	n.SetString(s, 10)

	if n.Sign() == 0 {
		return []int{0}
	}

	base := big.NewInt(int64(b))
	zero := big.NewInt(0)
	var rev []int
	for n.Cmp(zero) > 0 {
		mod := new(big.Int)
		n.DivMod(n, base, mod)
		rev = append(rev, int(mod.Int64()))
	}
	// reverse to most significant first
	digits := make([]int, len(rev))
	for i := 0; i < len(rev); i++ {
		digits[i] = rev[len(rev)-1-i]
	}
	return digits
}

// return decimal string of (s - 1), assumes s represents a non‑negative integer
func decMinusOne(s string) string {
	n := new(big.Int)
	n.SetString(s, 10)
	n.Sub(n, big.NewInt(1))
	if n.Sign() < 0 {
		return ""
	}
	return n.Text(10)
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def count_upto(num, b)
  return 0 if num < 0
  # convert to base‑b digits (most significant first)
  if num == 0
    digits = [0]
  else
    digits = []
    n = num
    while n > 0
      digits << (n % b)
      n /= b
    end
    digits.reverse!
  end

  len = digits.length
  memo = {}

  dfs = nil
  dfs = lambda do |pos, last, tight, started|
    if pos == len
      return 1
    end

    key = [pos, last, tight ? 1 : 0, started ? 1 : 0]
    unless tight
      cached = memo[key]
      return cached if cached
    end

    limit = tight ? digits[pos] : b - 1
    total = 0

    (0..limit).each do |d|
      ntight = tight && d == limit
      if !started && d == 0
        total += dfs.call(pos + 1, 0, ntight, false)
      else
        if !started
          # first non‑zero digit, any value allowed
          total += dfs.call(pos + 1, d, ntight, true)
        else
          next if d < last   # must be non‑decreasing
          total += dfs.call(pos + 1, d, ntight, true)
        end
      end
    end

    total %= MOD
    memo[key] = total unless tight
    total
  end

  dfs.call(0, 0, true, false) % MOD
end

def count_numbers(l, r, b)
  l_int = l.to_i
  r_int = r.to_i
  ans = (count_upto(r_int, b) - count_upto(l_int - 1, b)) % MOD
  ans += MOD if ans < 0
  ans
end
```

## Scala

```scala
object Solution {
  val MOD = 1000000007

  def countNumbers(l: String, r: String, b: Int): Int = {

    def decString(s: String): String = {
      // assumes s > "0"
      val sb = new StringBuilder
      var borrow = 1
      for (i <- s.length - 1 to 0 by -1) {
        var d = s.charAt(i) - '0' - borrow
        if (d < 0) {
          d += 10
          borrow = 1
        } else {
          borrow = 0
        }
        sb.append(('0' + d).toChar)
      }
      var res = sb.reverse.toString()
      var idx = 0
      while (idx < res.length - 1 && res.charAt(idx) == '0') idx += 1
      if (idx > 0) res = res.substring(idx)
      res
    }

    def toBaseDigits(num: String): Array[Int] = {
      if (num == "0") return Array(0)
      var s = num
      val buf = scala.collection.mutable.ArrayBuffer[Int]()
      while (s != "0") {
        var carry = 0
        val sb = new StringBuilder
        var startedQ = false
        for (ch <- s) {
          val cur = carry * 10 + (ch - '0')
          val q = cur / b
          val r = cur % b
          if (q != 0 || startedQ) {
            sb.append(('0' + q).toChar)
            startedQ = true
          } else if (startedQ) {
            sb.append('0')
          }
          carry = r
        }
        buf += carry
        s = if (!startedQ) "0" else sb.toString()
      }
      buf.reverse.toArray
    }

    def countUpTo(bound: String): Int = {
      val digits = toBaseDigits(bound)
      val n = digits.length
      val memo = Array.ofDim[Int](n + 1, 2, b + 1, 2)
      for {
        i <- 0 until n + 1
        t <- 0 until 2
        p <- 0 until b + 1
        sFlag <- 0 until 2
      } memo(i)(t)(p)(sFlag) = -1

      def dfs(pos: Int, tight: Int, prevIdx: Int, started: Int): Int = {
        if (pos == n) return 1
        val cached = memo(pos)(tight)(prevIdx)(started)
        if (cached != -1) return cached
        var res = 0L
        val maxDigit = if (tight == 1) digits[pos] else b - 1
        for (d <- 0 to maxDigit) {
          val nextTight = if (tight == 1 && d == maxDigit) 1 else 0
          if (started == 0 && d == 0) {
            res += dfs(pos + 1, nextTight, 0, 0)
          } else {
            val prev = if (started == 0) -1 else (prevIdx - 1)
            if (prev <= d) {
              val newPrevIdx = d + 1
              res += dfs(pos + 1, nextTight, newPrevIdx, 1)
            }
          }
        }
        val ans = (res % MOD).toInt
        memo(pos)(tight)(prevIdx)(started) = ans
        ans
      }

      dfs(0, 1, 0, 0)
    }

    if (l == "0") {
      countUpTo(r) % MOD
    } else {
      val lMinusOne = decString(l)
      var res = countUpTo(r) - countUpTo(lMinusOne)
      if (res < 0) res += MOD
      res
    }
  }
}
```

## Rust

```rust
use std::cmp::min;

const MOD: i64 = 1_000_000_007;

pub struct Solution;

impl Solution {
    pub fn count_numbers(l: String, r: String, b: i32) -> i32 {
        let base = b as usize;
        // precompute factorials up to needed size
        let max_len = 350usize; // enough for given constraints
        let max_n = base + max_len;
        let (fac, ifac) = Self::precompute_fact(max_n);

        fn comb(n: usize, k: usize, fac: &Vec<i64>, ifac: &Vec<i64>) -> i64 {
            if k > n { return 0; }
            fac[n] * ifac[k] % MOD * ifac[n - k] % MOD
        }

        // count numbers <= s (decimal string) with non‑decreasing digits in base `base`
        fn count_up_to(s: &str, base: usize, fac: &Vec<i64>, ifac: &Vec<i64>) -> i64 {
            if s == "0" { return 0; }
            let digits = Self::to_base(s, base);
            let n = digits.len();

            // count numbers with length < n
            let mut total = 0i64;
            for len in 1..n {
                total = (total + comb(base + len - 2, len, fac, ifac)) % MOD;
            }

            // DP for exact length n with tight constraint
            // memo[pos][prev][tight]
            let mut memo: Vec<Vec<[[Option<i64>; 2]; 10]>> = vec![
                vec![[None; 2]; base];
                n + 1
            ];

            fn dfs(
                pos: usize,
                prev: usize,
                tight: usize,
                digits: &Vec<u8>,
                base: usize,
                memo: &mut Vec<Vec<[[Option<i64>; 2]; 10]>>,
            ) -> i64 {
                if pos == digits.len() {
                    return 1;
                }
                if let Some(v) = memo[pos][prev][tight] {
                    return v;
                }
                let limit = if tight == 1 { digits[pos] as usize } else { base - 1 };
                let mut res = 0i64;
                for d in prev..=limit {
                    let ntight = if tight == 1 && d == limit { 1 } else { 0 };
                    res = (res + dfs(pos + 1, d, ntight, digits, base, memo)) % MOD;
                }
                memo[pos][prev][tight] = Some(res);
                res
            }

            let first_limit = digits[0] as usize;
            for d in 1..=first_limit {
                let tight_next = if d == first_limit { 1 } else { 0 };
                total = (total + dfs(1, d, tight_next, &digits, base, &mut memo)) % MOD;
            }

            total
        }

        // decrement decimal string by one
        fn dec_one(s: &str) -> String {
            if s == "0" { return "0".to_string(); }
            let mut bytes: Vec<u8> = s.bytes().collect();
            let mut i = bytes.len() - 1;
            loop {
                if bytes[i] > b'0' {
                    bytes[i] -= 1;
                    break;
                } else {
                    bytes[i] = b'9';
                    if i == 0 { break; }
                    i -= 1;
                }
            }
            while bytes.len() > 1 && bytes[0] == b'0' {
                bytes.remove(0);
            }
            String::from_utf8(bytes).unwrap()
        }

        let left_minus_one = dec_one(&l);
        let cnt_r = count_up_to(&r, base, &fac, &ifac);
        let cnt_l = count_up_to(&left_minus_one, base, &fac, &ifac);
        ((cnt_r - cnt_l + MOD) % MOD) as i32
    }

    // convert decimal string to vector of digits in given base (most significant first)
    fn to_base(s: &str, base: usize) -> Vec<u8> {
        let mut num: Vec<u8> = s.bytes().map(|c| c - b'0').collect();
        if num.is_empty() { return vec![0]; }
        let mut res: Vec<u8> = Vec::new();
        while !num.is_empty() {
            let mut new_num: Vec<u8> = Vec::new();
            let mut carry: usize = 0;
            for &d in &num {
                let cur = carry * 10 + d as usize;
                let q = (cur / base) as u8;
                let r = (cur % base) as u8;
                if !new_num.is_empty() || q != 0 {
                    new_num.push(q);
                }
                carry = r as usize;
            }
            res.push(carry as u8);
            num = new_num;
        }
        res.reverse();
        res
    }

    fn precompute_fact(n: usize) -> (Vec<i64>, Vec<i64>) {
        let mut fac = vec![0i64; n + 1];
        let mut ifac = vec![0i64; n + 1];
        fac[0] = 1;
        for i in 1..=n {
            fac[i] = fac[i - 1] * (i as i64) % MOD;
        }
        ifac[n] = Self::mod_pow(fac[n], MOD - 2);
        for i in (0..n).rev() {
            ifac[i] = ifac[i + 1] * ((i + 1) as i64) % MOD;
        }
        (fac, ifac)
    }

    fn mod_pow(mut base: i64, mut exp: i64) -> i64 {
        let mut res = 1i64;
        while exp > 0 {
            if exp & 1 == 1 {
                res = res * base % MOD;
            }
            base = base * base % MOD;
            exp >>= 1;
        }
        res
    }
}
```

## Racket

```racket
(define MOD 1000000007)

;; convert a non‑negative integer to a list of its base‑b digits (most significant first)
(define (to-base n b)
  (if (= n 0)
      '(0)
      (let loop ((x n) (acc '()))
        (if (= x 0)
            acc
            (loop (quotient x b) (cons (remainder x b) acc))))))

;; count numbers ≤ the given digit list whose base‑b representation has non‑decreasing digits
(define (count-up-to digits b)
  (let* ((len (length digits))
         (memo (make-hash)))
    (define (key pos prev tight started)
      (list pos prev (if tight 1 0) (if started 1 0)))
    (define (dfs pos prev tight started)
      (cond
        [(= pos len) (if started 1 0)]
        [else
         (define k (key pos prev tight started))
         (if (hash-has-key? memo k)
             (hash-ref memo k)
             (let* ((limit (if tight (list-ref digits pos) (sub1 b)))
                    (ans
                     (let loop ((d 0) (sum 0))
                       (cond
                         [(> d limit) sum]
                         [else
                          (define next-tight (and tight (= d limit)))
                          (cond
                            ;; still skipping leading zeros
                            [(and (not started) (= d 0))
                             (loop (add1 d)
                                   (modulo (+ sum (dfs (add1 pos) -1 next-tight #f)) MOD))]
                            [else
                             (define can-start? (or started (> d 0)))
                             (if (not can-start?)
                                 (loop (add1 d) sum) ; cannot start with zero after having started
                                 (let ([ok (or (not started) (>= d prev))])
                                   (if ok
                                       (loop (add1 d)
                                             (modulo (+ sum (dfs (add1 pos) d next-tight #t)) MOD))
                                       (loop (add1 d) sum))))]))]))
               (hash-set! memo k ans)
               ans)])))
    (dfs 0 -1 #t #f)))

;; main entry point
(define/contract (count-numbers l r b)
  (-> string? string? exact-integer? exact-integer?)
  (let* ((bint (exact->inexact b)) ; ensure it's an integer
         (l-num (string->number l))
         (r-num (string->number r))
         (r-digits (to-base r-num b))
         (cnt-r (count-up-to r-digits b))
         (cnt-l
          (if (= l-num 0)
              0
              (let* ((l-1 (sub1 l-num))
                     (l-digits (to-base l-1 b)))
                (count-up-to l-digits b)))))
    (modulo (- cnt-r cnt-l) MOD)))
```

## Erlang

```erlang
-module(solution).
-export([count_numbers/3]).

-define(MOD, 1000000007).

-spec count_numbers(L :: unicode:unicode_binary(), R :: unicode:unicode_binary(), B :: integer()) -> integer().
count_numbers(L, R, B) ->
    CountR = count_upto(R, B),
    CountLMinus1 =
        case is_zero(L) of
            true -> 0;
            false ->
                L1 = dec_sub_one(L),
                count_upto(L1, B)
        end,
    ((CountR - CountLMinus1) rem ?MOD + ?MOD) rem ?MOD.

%% ---------- Helper for counting numbers <= N ----------
count_upto(NBin, B) ->
    case is_zero(NBin) of
        true -> 1; % only zero itself
        false ->
            Digits = dec_str_to_base(NBin, B),
            DigitsTup = list_to_tuple(Digits),
            Len = tuple_size(DigitsTup),
            {Res, _} = dp(0, 0, true, false, DigitsTup, Len, B, #{}),
            Res
    end.

%% DP with memoization: returns {Count, NewMemo}
dp(Pos, Prev, Tight, Started, DigitsTup, Len, B, Memo) ->
    Key = {Pos, Prev, Tight, Started},
    case maps:get(Key, Memo, undefined) of
        Value when Value =/= undefined -> {Value, Memo};
        _ ->
            Result =
                if Pos == Len ->
                        1; % reached end, count this number
                   true ->
                        MaxDigit = if Tight -> element(Pos + 1, DigitsTup); true -> B - 1 end,
                        dp_iter(0, MaxDigit, Pos, Prev, Tight, Started, DigitsTup, Len, B, Memo, 0)
                end,
            {Count, NewMemo} = Result,
            UpdatedMemo = maps:put(Key, Count, NewMemo),
            {Count, UpdatedMemo}
    end.

%% Iterate over possible digit D at current position
dp_iter(D, Max, Pos, Prev, Tight, Started, DigitsTup, Len, B, Memo, Acc) when D > Max ->
    {Acc rem ?MOD, Memo};
dp_iter(D, Max, Pos, Prev, Tight, Started, DigitsTup, Len, B, Memo, Acc) ->
    NewTight = Tight andalso (D == Max),
    case Started of
        false ->
            if D == 0 ->
                    {SubCnt, Memo1} = dp(Pos + 1, 0, NewTight, false, DigitsTup, Len, B, Memo),
                    NewAcc = (Acc + SubCnt) rem ?MOD,
                    dp_iter(D + 1, Max, Pos, Prev, Tight, Started, DigitsTup, Len, B, Memo1, NewAcc);
               true ->
                    {SubCnt, Memo1} = dp(Pos + 1, D, NewTight, true, DigitsTup, Len, B, Memo),
                    NewAcc = (Acc + SubCnt) rem ?MOD,
                    dp_iter(D + 1, Max, Pos, Prev, Tight, Started, DigitsTup, Len, B, Memo1, NewAcc)
            end;
        true ->
            if D < Prev ->
                    dp_iter(D + 1, Max, Pos, Prev, Tight, Started, DigitsTup, Len, B, Memo, Acc);
               true ->
                    {SubCnt, Memo1} = dp(Pos + 1, D, NewTight, true, DigitsTup, Len, B, Memo),
                    NewAcc = (Acc + SubCnt) rem ?MOD,
                    dp_iter(D + 1, Max, Pos, Prev, Tight, Started, DigitsTup, Len, B, Memo1, NewAcc)
            end
    end.

%% ---------- Decimal string to base B digits ----------
dec_str_to_base(DecBin, B) ->
    DecList = binary:bin_to_list(DecBin),
    DigitsRev = dec_to_base_rev(normalize_decimal(DecList), B, []),
    case DigitsRev of
        [] -> [0];
        _  -> lists:reverse(DigitsRev)
    end.

dec_to_base_rev([ $0 ], _B, Acc) -> Acc;
dec_to_base_rev(NumStr, B, Acc) ->
    {QuotStr, Rem} = divide_by_int(NumStr, B),
    dec_to_base_rev(normalize_decimal(QuotStr), B, [Rem | Acc]).

%% Divide decimal string (list of chars) by integer B
divide_by_int(Str, B) -> divide_by_int(Str, B, [], false, 0).

divide_by_int([], _B, Acc, _Started, Rem) ->
    Quot = case Acc of
        [] -> "0";
        _  -> lists:reverse(Acc)
    end,
    {Quot, Rem};
divide_by_int([C|Rest], B, Acc, Started, Carry) ->
    Digit = C - $0,
    Val = Carry * 10 + Digit,
    QDigit = Val div B,
    NewCarry = Val rem B,
    NewStarted = Started orelse (QDigit =/= 0),
    NewAcc = if NewStarted -> [QDigit+$0 | Acc]; true -> Acc end,
    divide_by_int(Rest, B, NewAcc, NewStarted, NewCarry).

%% ---------- Subtract one from decimal string ----------
dec_sub_one(DecBin) ->
    List = binary:bin_to_list(DecBin),
    Rev = lists:reverse(List),
    {ResRev, _} = dec_sub_one_rev(Rev, 1, []),
    normalize_decimal(lists:reverse(ResRev)).

dec_sub_one_rev([], Borrow, Acc) when Borrow == 0 -> {Acc, 0};
dec_sub_one_rev([], Borrow, Acc) -> {Acc, Borrow}; % should not happen for valid input
dec_sub_one_rev([C|Rest], Borrow, Acc) ->
    Digit = C - $0,
    NewDigit = Digit - Borrow,
    if NewDigit < 0 ->
            dec_sub_one_rev(Rest, 1, [$0+10 | Acc]);
       true ->
            dec_sub_one_rev(Rest, 0, [NewDigit+$0 | Acc])
    end.

%% ---------- Utility ----------
is_zero(Bin) ->
    case binary:bin_to_list(Bin) of
        [] -> true;
        List -> normalize_decimal(List) =:= "0"
    end.

normalize_decimal(List) ->
    Trimmed = trim_leading_zeros(List),
    case Trimmed of
        [] -> "0";
        _  -> Trimmed
    end.

trim_leading_zeros([ $0 | Rest]) -> trim_leading_zeros(Rest);
trim_leading_zeros(L) -> L.
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @mod 1_000_000_007

  @spec count_numbers(l :: String.t(), r :: String.t(), b :: integer) :: integer
  def count_numbers(l, r, b) do
    l_int = String.to_integer(l)
    r_int = String.to_integer(r)

    left =
      if l_int == 0 do
        0
      else
        count_up_to(l_int - 1, b)
      end

    right = count_up_to(r_int, b)
    ans = rem(right - left, @mod)
    if ans < 0, do: ans + @mod, else: ans
  end

  # Count numbers in [0, num] with non‑decreasing digits in base b
  defp count_up_to(num, b) do
    digits = to_base_digits(num, b)
    {res, _} = dfs(0, 0, false, true, digits, b, %{})
    res
  end

  # Convert integer to list of base‑b digits (most significant first)
  defp to_base_digits(0, _b), do: [0]

  defp to_base_digits(n, b) do
    build_digits(n, b, [])
  end

  defp build_digits(0, _b, acc), do: acc

  defp build_digits(num, b, acc) do
    {q, r} = Integer.div_rem(num, b)
    build_digits(q, b, [r | acc])
  end

  # Digit DP with memoization
  defp dfs(pos, prev, started, tight, digits, b, memo) do
    len = length(digits)

    if pos == len do
      {1, memo}
    else
      key = {pos, prev, started, tight}

      case Map.fetch(memo, key) do
        {:ok, val} ->
          {val, memo}

        :error ->
          limit = if tight, do: Enum.at(digits, pos), else: b - 1

          {sum, memo2} =
            Enum.reduce(0..limit, {0, memo}, fn d, {acc, m} ->
              new_started = started or d != 0

              cond do
                new_started and started and d < prev ->
                  {acc, m}

                true ->
                  new_prev = if new_started, do: d, else: prev
                  new_tight = tight && d == limit
                  {cnt, m2} = dfs(pos + 1, new_prev, new_started, new_tight, digits, b, m)
                  {(acc + cnt) |> rem(@mod), m2}
              end
            end)

          memo3 = Map.put(memo2, key, sum)
          {sum, memo3}
      end
    end
  end
end
```
