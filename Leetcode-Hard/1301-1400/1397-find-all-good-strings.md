# 1397. Find All Good Strings

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findGoodStrings(int n, string s1, string s2, string evil) {
        const int MOD = 1000000007;
        int m = (int)evil.size();
        
        // KMP failure function
        vector<int> lps(m,0);
        for (int i=1;i<m;i++) {
            int len = lps[i-1];
            while (len>0 && evil[i]!=evil[len]) len = lps[len-1];
            if (evil[i]==evil[len]) ++len;
            lps[i]=len;
        }
        
        // automaton transitions
        vector<array<int,26>> nxt(m+1);
        for (int state=0; state<=m; ++state) {
            for (int ch=0; ch<26; ++ch) {
                if (state==m) { // once matched, stay in forbidden state
                    nxt[state][ch]=m;
                    continue;
                }
                int ns = state;
                char c = 'a'+ch;
                while (ns>0 && evil[ns]!=c) ns = lps[ns-1];
                if (evil[ns]==c) ++ns;
                nxt[state][ch] = ns;
            }
        }
        
        static long long dp[501][51][2][2];
        memset(dp, 0, sizeof(dp));
        dp[0][0][1][1] = 1;
        
        for (int pos=0; pos<n; ++pos) {
            for (int state=0; state<m; ++state) {
                for (int low=0; low<2; ++low) {
                    for (int high=0; high<2; ++high) {
                        long long cur = dp[pos][state][low][high];
                        if (!cur) continue;
                        char loChar = low ? s1[pos] : 'a';
                        char hiChar = high ? s2[pos] : 'z';
                        for (char c=loChar; c<=hiChar; ++c) {
                            int ns = nxt[state][c-'a'];
                            if (ns == m) continue; // contains evil
                            int nlow  = low && (c==s1[pos]);
                            int nhigh = high && (c==s2[pos]);
                            dp[pos+1][ns][nlow][nhigh] += cur;
                            if (dp[pos+1][ns][nlow][nhigh] >= MOD) dp[pos+1][ns][nlow][nhigh] -= MOD;
                        }
                    }
                }
            }
        }
        
        long long ans = 0;
        for (int state=0; state<m; ++state)
            for (int low=0; low<2; ++low)
                for (int high=0; high<2; ++high) {
                    ans += dp[n][state][low][high];
                    if (ans >= MOD) ans -= MOD;
                }
        return (int)(ans % MOD);
    }
};
```

## Java

```java
class Solution {
    public int findGoodStrings(int n, String s1, String s2, String evil) {
        final int MOD = 1_000_000_007;
        int m = evil.length();

        // Build KMP failure function
        int[] lps = new int[m];
        for (int i = 1; i < m; i++) {
            int len = lps[i - 1];
            while (len > 0 && evil.charAt(i) != evil.charAt(len)) {
                len = lps[len - 1];
            }
            if (evil.charAt(i) == evil.charAt(len)) {
                len++;
            }
            lps[i] = len;
        }

        // Precompute transitions for automaton
        int[][] trans = new int[m + 1][26];
        for (int state = 0; state <= m; state++) {
            for (int c = 0; c < 26; c++) {
                if (state == m) { // absorbing, not used
                    trans[state][c] = m;
                    continue;
                }
                char ch = (char) ('a' + c);
                int ns = state;
                while (ns > 0 && evil.charAt(ns) != ch) {
                    ns = lps[ns - 1];
                }
                if (evil.charAt(ns) == ch) {
                    ns++;
                }
                trans[state][c] = ns;
            }
        }

        // DP[pos][state][tightLow][tightHigh]
        long[][][] cur = new long[m][2][2];
        cur[0][1][1] = 1; // start with empty prefix, both bounds tight

        for (int pos = 0; pos < n; pos++) {
            long[][][] nxt = new long[m][2][2];
            char lowChar = s1.charAt(pos);
            char highChar = s2.charAt(pos);

            for (int state = 0; state < m; state++) {
                for (int lowFlag = 0; lowFlag < 2; lowFlag++) {
                    for (int highFlag = 0; highFlag < 2; highFlag++) {
                        long val = cur[state][lowFlag][highFlag];
                        if (val == 0) continue;

                        char lo = lowFlag == 1 ? lowChar : 'a';
                        char hi = highFlag == 1 ? highChar : 'z';

                        for (char ch = lo; ch <= hi; ch++) {
                            int ns = trans[state][ch - 'a'];
                            if (ns == m) continue; // contains evil, skip

                            int nLow = (lowFlag == 1 && ch == lowChar) ? 1 : 0;
                            int nHigh = (highFlag == 1 && ch == highChar) ? 1 : 0;

                            long sum = nxt[ns][nLow][nHigh] + val;
                            if (sum >= MOD) sum -= MOD;
                            nxt[ns][nLow][nHigh] = sum;
                        }
                    }
                }
            }
            cur = nxt;
        }

        long ans = 0;
        for (int state = 0; state < m; state++) {
            for (int lowFlag = 0; lowFlag < 2; lowFlag++) {
                for (int highFlag = 0; highFlag < 2; highFlag++) {
                    ans += cur[state][lowFlag][highFlag];
                    if (ans >= MOD) ans -= MOD;
                }
            }
        }
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def findGoodStrings(self, n, s1, s2, evil):
        """
        :type n: int
        :type s1: str
        :type s2: str
        :type evil: str
        :rtype: int
        """
        MOD = 10**9 + 7
        m = len(evil)

        # build KMP failure function
        fail = [0] * m
        for i in range(1, m):
            j = fail[i - 1]
            while j > 0 and evil[i] != evil[j]:
                j = fail[j - 1]
            if evil[i] == evil[j]:
                j += 1
            fail[i] = j

        # build transition table for automaton
        trans = [[0] * 26 for _ in range(m + 1)]
        for state in range(m + 1):
            for c in range(26):
                ch = chr(ord('a') + c)
                if state == m:
                    trans[state][c] = m
                    continue
                ns = state
                while ns > 0 and ch != evil[ns]:
                    ns = fail[ns - 1]
                if ch == evil[ns]:
                    ns += 1
                trans[state][c] = ns

        # dp[pos][state][tightLow][tightHigh]
        cur = [[[0, 0] for _ in range(2)] for __ in range(m)]
        cur[0][1][1] = 1  # state=0, tightLow=True, tightHigh=True

        for i in range(n):
            nxt = [[[0, 0] for _ in range(2)] for __ in range(m)]
            low_char = s1[i]
            high_char = s2[i]
            lo_ord = ord(low_char)
            hi_ord = ord(high_char)
            for state in range(m):
                for tl in (0, 1):
                    for th in (0, 1):
                        cnt = cur[state][tl][th]
                        if not cnt:
                            continue
                        low_bound = lo_ord if tl else ord('a')
                        high_bound = hi_ord if th else ord('z')
                        for code in range(low_bound, high_bound + 1):
                            ns = trans[state][code - 97]
                            if ns == m:  # contains evil, skip
                                continue
                            ntl = tl and (code == lo_ord)
                            nth = th and (code == hi_ord)
                            nxt[ns][ntl][nth] = (nxt[ns][ntl][nth] + cnt) % MOD
            cur = nxt

        ans = 0
        for state in range(m):
            for tl in (0, 1):
                for th in (0, 1):
                    ans = (ans + cur[state][tl][th]) % MOD
        return ans
```

## Python3

```python
class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        MOD = 10**9 + 7
        m = len(evil)

        # build KMP failure function for evil
        lps = [0] * m
        for i in range(1, m):
            j = lps[i - 1]
            while j > 0 and evil[i] != evil[j]:
                j = lps[j - 1]
            if evil[i] == evil[j]:
                j += 1
            lps[i] = j

        # transition table: nxt[state][char] -> next matched length
        nxt = [[0] * 26 for _ in range(m + 1)]
        for state in range(m + 1):
            for c in range(26):
                ch = chr(ord('a') + c)
                if state == m:
                    nxt[state][c] = m
                    continue
                j = state
                while j > 0 and evil[j] != ch:
                    j = lps[j - 1]
                if evil[j] == ch:
                    j += 1
                nxt[state][c] = j

        from functools import lru_cache

        @lru_cache(None)
        def dfs(pos: int, state: int, low_eq: bool, high_eq: bool) -> int:
            if state == m:          # already contains evil (should not be counted)
                return 0
            if pos == n:
                return 1

            lo_char = ord(s1[pos]) - 97 if low_eq else 0
            hi_char = ord(s2[pos]) - 97 if high_eq else 25

            total = 0
            for c in range(lo_char, hi_char + 1):
                ns = nxt[state][c]
                if ns == m:
                    continue
                n_low_eq = low_eq and (c == ord(s1[pos]) - 97)
                n_high_eq = high_eq and (c == ord(s2[pos]) - 97)
                total += dfs(pos + 1, ns, n_low_eq, n_high_eq)
                if total >= MOD:
                    total -= MOD
            return total

        return dfs(0, 0, True, True) % MOD
```

## C

```c
#include <string.h>

#define MOD 1000000007LL

int findGoodStrings(int n, char* s1, char* s2, char* evil) {
    int m = strlen(evil);
    int fail[55] = {0};
    for (int i = 1; i < m; ++i) {
        int j = fail[i - 1];
        while (j > 0 && evil[i] != evil[j]) j = fail[j - 1];
        if (evil[i] == evil[j]) ++j;
        fail[i] = j;
    }

    int trans[55][26];
    for (int st = 0; st <= m; ++st) {
        for (int c = 0; c < 26; ++c) {
            if (st == m) {
                trans[st][c] = m;
                continue;
            }
            int ns = st;
            char ch = 'a' + c;
            while (ns > 0 && evil[ns] != ch) ns = fail[ns - 1];
            if (evil[ns] == ch) ++ns;
            trans[st][c] = ns;
        }
    }

    static long long dp[2][55][2][2];
    memset(dp, 0, sizeof(dp));
    int cur = 0, nxt = 1;
    dp[cur][0][1][1] = 1;

    for (int pos = 0; pos < n; ++pos) {
        memset(dp[nxt], 0, sizeof(dp[nxt]));
        for (int st = 0; st < m; ++st) {
            for (int tl = 0; tl <= 1; ++tl) {
                for (int th = 0; th <= 1; ++th) {
                    long long val = dp[cur][st][tl][th];
                    if (!val) continue;
                    char lowc = tl ? s1[pos] : 'a';
                    char highc = th ? s2[pos] : 'z';
                    for (char ch = lowc; ch <= highc; ++ch) {
                        int ns = trans[st][ch - 'a'];
                        if (ns == m) continue; // contains evil
                        int ntl = tl && (ch == s1[pos]);
                        int nth = th && (ch == s2[pos]);
                        dp[nxt][ns][ntl][nth] += val;
                        if (dp[nxt][ns][ntl][nth] >= MOD) dp[nxt][ns][ntl][nth] -= MOD;
                    }
                }
            }
        }
        cur ^= 1;
        nxt ^= 1;
    }

    long long ans = 0;
    for (int st = 0; st < m; ++st)
        for (int tl = 0; tl <= 1; ++tl)
            for (int th = 0; th <= 1; ++th) {
                ans += dp[cur][st][tl][th];
                if (ans >= MOD) ans -= MOD;
            }

    return (int)(ans % MOD);
}
```

## Csharp

```csharp
using System;

public class Solution {
    private const int MOD = 1000000007;
    public int FindGoodStrings(int n, string s1, string s2, string evil) {
        int m = evil.Length;
        // Build KMP failure function
        int[] lps = new int[m];
        for (int i = 1; i < m; i++) {
            int j = lps[i - 1];
            while (j > 0 && evil[i] != evil[j]) j = lps[j - 1];
            if (evil[i] == evil[j]) j++;
            lps[i] = j;
        }
        // Build transition table
        int[,] trans = new int[m + 1, 26];
        for (int state = 0; state <= m; state++) {
            for (int c = 0; c < 26; c++) {
                if (state == m) {
                    trans[state, c] = m;
                    continue;
                }
                int ns = state;
                char ch = (char)('a' + c);
                while (ns > 0 && evil[ns] != ch) ns = lps[ns - 1];
                if (evil[ns] == ch) ns++;
                trans[state, c] = ns;
            }
        }

        long[,,,] dp = new long[n + 1, m + 1, 2, 2];
        dp[0, 0, 1, 1] = 1;

        for (int pos = 0; pos < n; pos++) {
            for (int state = 0; state < m; state++) {
                for (int low = 0; low <= 1; low++) {
                    for (int high = 0; high <= 1; high++) {
                        long cur = dp[pos, state, low, high];
                        if (cur == 0) continue;
                        int lo = low == 1 ? s1[pos] - 'a' : 0;
                        int hi = high == 1 ? s2[pos] - 'a' : 25;
                        for (int c = lo; c <= hi; c++) {
                            int ns = trans[state, c];
                            if (ns == m) continue; // contains evil
                            int nLow = (low == 1 && c == lo) ? 1 : 0;
                            int nHigh = (high == 1 && c == hi) ? 1 : 0;
                            dp[pos + 1, ns, nLow, nHigh] = (dp[pos + 1, ns, nLow, nHigh] + cur) % MOD;
                        }
                    }
                }
            }
        }

        long ans = 0;
        for (int state = 0; state < m; state++) {
            for (int low = 0; low <= 1; low++) {
                for (int high = 0; high <= 1; high++) {
                    ans += dp[n, state, low, high];
                }
            }
        }
        ans %= MOD;
        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {string} s1
 * @param {string} s2
 * @param {string} evil
 * @return {number}
 */
var findGoodStrings = function(n, s1, s2, evil) {
    const MOD = 1000000007;
    const m = evil.length;

    // Build KMP failure (lps) array for evil
    const lps = new Array(m).fill(0);
    for (let i = 1; i < m; ++i) {
        let len = lps[i - 1];
        while (len > 0 && evil[i] !== evil[len]) {
            len = lps[len - 1];
        }
        if (evil[i] === evil[len]) len++;
        lps[i] = len;
    }

    // Build transition table: next[state][ch] -> new state length
    const trans = Array.from({ length: m }, () => new Array(26).fill(0));
    for (let state = 0; state < m; ++state) {
        for (let c = 0; c < 26; ++c) {
            const ch = String.fromCharCode(97 + c);
            if (ch === evil[state]) {
                trans[state][c] = state + 1;
            } else {
                let len = state;
                while (len > 0 && ch !== evil[len]) {
                    len = lps[len - 1];
                }
                if (ch === evil[len]) len++;
                trans[state][c] = len;
            }
        }
    }

    // dp[state][tightLow][tightHigh]
    let dp = Array.from({ length: m }, () => [
        [0, 0],
        [0, 0]
    ]);
    dp[0][1][1] = 1;

    for (let pos = 0; pos < n; ++pos) {
        const ndp = Array.from({ length: m }, () => [
            [0, 0],
            [0, 0]
        ]);

        for (let state = 0; state < m; ++state) {
            for (let lowFlag = 0; lowFlag <= 1; ++lowFlag) {
                for (let highFlag = 0; highFlag <= 1; ++highFlag) {
                    const cur = dp[state][lowFlag][highFlag];
                    if (cur === 0) continue;

                    const lo = lowFlag ? s1.charCodeAt(pos) - 97 : 0;
                    const hi = highFlag ? s2.charCodeAt(pos) - 97 : 25;

                    for (let c = lo; c <= hi; ++c) {
                        const ns = trans[state][c];
                        if (ns === m) continue; // contains evil, skip
                        const nLow = lowFlag && (c === lo);
                        const nHigh = highFlag && (c === hi);
                        let val = ndp[ns][nLow ? 1 : 0][nHigh ? 1 : 0] + cur;
                        if (val >= MOD) val -= MOD;
                        ndp[ns][nLow ? 1 : 0][nHigh ? 1 : 0] = val;
                    }
                }
            }
        }

        dp = ndp;
    }

    let ans = 0;
    for (let state = 0; state < m; ++state) {
        for (let lowFlag = 0; lowFlag <= 1; ++lowFlag) {
            for (let highFlag = 0; highFlag <= 1; ++highFlag) {
                ans += dp[state][lowFlag][highFlag];
                if (ans >= MOD) ans -= MOD;
            }
        }
    }
    return ans % MOD;
};
```

## Typescript

```typescript
function findGoodStrings(n: number, s1: string, s2: string, evil: string): number {
    const MOD = 1000000007;
    const m = evil.length;

    // KMP failure function
    const lps = new Array(m).fill(0);
    for (let i = 1; i < m; ++i) {
        let len = lps[i - 1];
        while (len > 0 && evil[i] !== evil[len]) {
            len = lps[len - 1];
        }
        if (evil[i] === evil[len]) ++len;
        lps[i] = len;
    }

    // transition table for automaton
    const trans: number[][] = Array.from({ length: m }, () => new Array(26).fill(0));
    for (let state = 0; state < m; ++state) {
        for (let c = 0; c < 26; ++c) {
            const ch = String.fromCharCode(97 + c);
            let ns = state;
            while (ns > 0 && evil[ns] !== ch) {
                ns = lps[ns - 1];
            }
            if (evil[ns] === ch) ++ns;
            trans[state][c] = ns;
        }
    }

    const memo = new Map<string, number>();

    function dfs(pos: number, state: number, lowTight: boolean, highTight: boolean): number {
        if (state === m) return 0; // contains evil
        if (pos === n) return 1;
        const key = pos + '|' + state + '|' + (lowTight ? 1 : 0) + '|' + (highTight ? 1 : 0);
        const cached = memo.get(key);
        if (cached !== undefined) return cached;

        const lo = lowTight ? s1.charCodeAt(pos) - 97 : 0;
        const hi = highTight ? s2.charCodeAt(pos) - 97 : 25;

        let ans = 0;
        for (let c = lo; c <= hi; ++c) {
            const ns = trans[state][c];
            if (ns === m) continue; // would create evil substring
            const nLow = lowTight && c === (s1.charCodeAt(pos) - 97);
            const nHigh = highTight && c === (s2.charCodeAt(pos) - 97);
            ans += dfs(pos + 1, ns, nLow, nHigh);
            if (ans >= MOD) ans -= MOD;
        }

        memo.set(key, ans);
        return ans;
    }

    return dfs(0, 0, true, true) % MOD;
}
```

## Php

```php
class Solution {
    private $n;
    private $s1;
    private $s2;
    private $evil;
    private $m;
    private $mod = 1000000007;
    private $next = [];
    private $dp = [];

    /**
     * @param Integer $n
     * @param String $s1
     * @param String $s2
     * @param String $evil
     * @return Integer
     */
    function findGoodStrings($n, $s1, $s2, $evil) {
        $this->n = $n;
        $this->s1 = $s1;
        $this->s2 = $s2;
        $this->evil = $evil;
        $this->m = strlen($evil);
        $this->buildAutomaton();
        $this->dp = [];
        return $this->dfs(0, 0, true, true) % $this->mod;
    }

    private function buildAutomaton() {
        $m = $this->m;
        $evil = $this->evil;
        // failure function
        $fail = array_fill(0, $m, 0);
        for ($i = 1; $i < $m; $i++) {
            $j = $fail[$i - 1];
            while ($j > 0 && $evil[$i] !== $evil[$j]) {
                $j = $fail[$j - 1];
            }
            if ($evil[$i] === $evil[$j]) {
                $j++;
            }
            $fail[$i] = $j;
        }

        // transition table
        $this->next = array_fill(0, $m + 1, array_fill(0, 26, 0));
        for ($len = 0; $len <= $m; $len++) {
            for ($ch = 0; $ch < 26; $ch++) {
                if ($len == $m) {
                    $this->next[$len][$ch] = $m;
                    continue;
                }
                $c = chr(ord('a') + $ch);
                $j = $len;
                while ($j > 0 && $c !== $evil[$j]) {
                    $j = $fail[$j - 1];
                }
                if ($c === $evil[$j]) {
                    $j++;
                }
                $this->next[$len][$ch] = $j;
            }
        }
    }

    private function dfs($pos, $len, $tightLow, $tightHigh) {
        if ($pos == $this->n) {
            return 1;
        }
        $key = $pos . '|' . $len . '|' . ($tightLow ? 1 : 0) . '|' . ($tightHigh ? 1 : 0);
        if (isset($this->dp[$key])) {
            return $this->dp[$key];
        }

        $lowChar = $tightLow ? $this->s1[$pos] : 'a';
        $highChar = $tightHigh ? $this->s2[$pos] : 'z';

        $res = 0;
        for ($cOrd = ord($lowChar); $cOrd <= ord($highChar); $cOrd++) {
            $chIdx = $cOrd - 97; // index 0..25
            $newLen = $this->next[$len][$chIdx];
            if ($newLen == $this->m) {
                continue; // contains evil, skip
            }
            $newTightLow = $tightLow && ($cOrd == ord($this->s1[$pos]));
            $newTightHigh = $tightHigh && ($cOrd == ord($this->s2[$pos]));
            $res += $this->dfs($pos + 1, $newLen, $newTightLow, $newTightHigh);
            if ($res >= $this->mod) {
                $res -= $this->mod;
            }
        }

        $this->dp[$key] = $res % $this->mod;
        return $this->dp[$key];
    }
}
```

## Swift

```swift
class Solution {
    func findGoodStrings(_ n: Int, _ s1: String, _ s2: String, _ evil: String) -> Int {
        let MOD = 1_000_000_007
        // Convert strings to integer arrays (0..25)
        let aVal = UInt8(ascii: "a")
        let s1Arr = s1.utf8.map { Int($0 - aVal) }
        let s2Arr = s2.utf8.map { Int($0 - aVal) }
        let evilArr = evil.utf8.map { Int($0 - aVal) }
        let m = evilArr.count
        
        // Build KMP failure function
        var fail = Array(repeating: 0, count: m)
        for i in 1..<m {
            var j = fail[i - 1]
            while j > 0 && evilArr[i] != evilArr[j] {
                j = fail[j - 1]
            }
            if evilArr[i] == evilArr[j] { j += 1 }
            fail[i] = j
        }
        
        // Build transition table nextState[state][char] -> new state length
        var nextState = Array(repeating: Array(repeating: 0, count: 26), count: m + 1)
        for state in 0...m {
            for ch in 0..<26 {
                if state == m {
                    nextState[state][ch] = m
                    continue
                }
                var k = state
                while k > 0 && evilArr[k] != ch {
                    k = fail[k - 1]
                }
                if k < m && evilArr[k] == ch { k += 1 }
                nextState[state][ch] = k
            }
        }
        
        // DP memo: dp[pos][state][lowFlag][highFlag] = result or -1 if uncomputed
        var dp = Array(
            repeating: Array(
                repeating: Array(
                    repeating: Array(repeating: -1, count: 2),
                    count: 2),
                count: m + 1),
            count: n + 1)
        
        func dfs(_ pos: Int, _ state: Int, _ lowFlag: Int, _ highFlag: Int) -> Int {
            if state == m { return 0 } // evil already matched, invalid
            if pos == n { return 1 }
            if dp[pos][state][lowFlag][highFlag] != -1 {
                return dp[pos][state][lowFlag][highFlag]
            }
            var res = 0
            let lo = lowFlag == 1 ? s1Arr[pos] : 0
            let hi = highFlag == 1 ? s2Arr[pos] : 25
            if lo <= hi {
                for ch in lo...hi {
                    let nextLow = (lowFlag == 1 && ch == s1Arr[pos]) ? 1 : 0
                    let nextHigh = (highFlag == 1 && ch == s2Arr[pos]) ? 1 : 0
                    let ns = nextState[state][ch]
                    if ns == m { continue } // would contain evil
                    let sub = dfs(pos + 1, ns, nextLow, nextHigh)
                    res += sub
                    if res >= MOD { res -= MOD }
                }
            }
            dp[pos][state][lowFlag][highFlag] = res
            return res
        }
        
        return dfs(0, 0, 1, 1)
    }
}
```

## Kotlin

```kotlin
import java.util.*

class Solution {
    private val MOD = 1_000_000_007L

    fun findGoodStrings(n: Int, s1: String, s2: String, evil: String): Int {
        val m = evil.length
        // build lps array for KMP
        val lps = IntArray(m)
        var len = 0
        var i = 1
        while (i < m) {
            if (evil[i] == evil[len]) {
                len++
                lps[i] = len
                i++
            } else {
                if (len != 0) {
                    len = lps[len - 1]
                } else {
                    lps[i] = 0
                    i++
                }
            }
        }

        // build transition table nxt[state][charIdx]
        val nxt = Array(m + 1) { IntArray(26) }
        for (state in 0..m) {
            for (cIdx in 0 until 26) {
                var k = state
                if (k == m) {
                    // once full match reached, stay at m (invalid)
                    nxt[state][cIdx] = m
                    continue
                }
                val ch = ('a'.code + cIdx).toChar()
                while (k > 0 && evil[k] != ch) {
                    k = lps[k - 1]
                }
                if (evil[k] == ch) {
                    k++
                }
                nxt[state][cIdx] = k
            }
        }

        var dp = Array(m) { Array(2) { LongArray(2) } }
        dp[0][1][1] = 1L

        for (pos in 0 until n) {
            val ndp = Array(m) { Array(2) { LongArray(2) } }
            for (state in 0 until m) {
                for (lowFlag in 0..1) {
                    for (highFlag in 0..1) {
                        val cur = dp[state][lowFlag][highFlag]
                        if (cur == 0L) continue
                        val lowChar = if (lowFlag == 1) s1[pos] else 'a'
                        val highChar = if (highFlag == 1) s2[pos] else 'z'
                        var c = lowChar
                        while (c <= highChar) {
                            val cIdx = c - 'a'
                            val ns = nxt[state][cIdx]
                            if (ns != m) { // not containing evil
                                val nLow = if (lowFlag == 1 && c == s1[pos]) 1 else 0
                                val nHigh = if (highFlag == 1 && c == s2[pos]) 1 else 0
                                ndp[ns][nLow][nHigh] =
                                    (ndp[ns][nLow][nHigh] + cur) % MOD
                            }
                            c++
                        }
                    }
                }
            }
            dp = ndp
        }

        var ans = 0L
        for (state in 0 until m) {
            for (lowFlag in 0..1) {
                for (highFlag in 0..1) {
                    ans = (ans + dp[state][lowFlag][highFlag]) % MOD
                }
            }
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _MOD = 1000000007;

  int findGoodStrings(int n, String s1, String s2, String evil) {
    int m = evil.length;
    // Build prefix function for KMP
    List<int> pi = List.filled(m, 0);
    for (int i = 1; i < m; i++) {
      int j = pi[i - 1];
      while (j > 0 && evil.codeUnitAt(i) != evil.codeUnitAt(j)) {
        j = pi[j - 1];
      }
      if (evil.codeUnitAt(i) == evil.codeUnitAt(j)) j++;
      pi[i] = j;
    }

    // Build transition table for automaton
    int aCode = 'a'.codeUnitAt(0);
    List<List<int>> trans = List.generate(m + 1, (_) => List.filled(26, 0));
    for (int state = 0; state <= m; state++) {
      for (int c = 0; c < 26; c++) {
        if (state == m) {
          trans[state][c] = m;
          continue;
        }
        int ns = state;
        int chCode = aCode + c;
        while (ns > 0 && evil.codeUnitAt(ns) != chCode) {
          ns = pi[ns - 1];
        }
        if (evil.codeUnitAt(ns) == chCode) ns++;
        trans[state][c] = ns;
      }
    }

    // DP: cur[state][mask], mask = lowFlag<<1 | highFlag
    List<List<int>> cur = List.generate(m, (_) => List.filled(4, 0));
    cur[0][3] = 1; // both tight to s1 and s2 at start

    for (int pos = 0; pos < n; pos++) {
      List<List<int>> nxt = List.generate(m, (_) => List.filled(4, 0));
      int lowChar = s1.codeUnitAt(pos);
      int highChar = s2.codeUnitAt(pos);
      for (int state = 0; state < m; state++) {
        for (int mask = 0; mask < 4; mask++) {
          int val = cur[state][mask];
          if (val == 0) continue;
          int lowFlag = (mask >> 1) & 1;
          int highFlag = mask & 1;
          int lo = lowFlag == 1 ? lowChar : aCode;
          int hi = highFlag == 1 ? highChar : aCode + 25; // 'z'
          for (int ch = lo; ch <= hi; ch++) {
            int nextLow = (lowFlag == 1 && ch == lowChar) ? 1 : 0;
            int nextHigh = (highFlag == 1 && ch == highChar) ? 1 : 0;
            int ns = trans[state][ch - aCode];
            if (ns == m) continue; // contains evil, skip
            int nmask = (nextLow << 1) | nextHigh;
            int newVal = nxt[ns][nmask] + val;
            if (newVal >= _MOD) newVal -= _MOD;
            nxt[ns][nmask] = newVal;
          }
        }
      }
      cur = nxt;
    }

    int ans = 0;
    for (int state = 0; state < m; state++) {
      for (int mask = 0; mask < 4; mask++) {
        ans += cur[state][mask];
        if (ans >= _MOD) ans -= _MOD;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func findGoodStrings(n int, s1 string, s2 string, evil string) int {
	const MOD = 1000000007
	m := len(evil)

	// KMP failure function for evil
	fail := make([]int, m)
	for i := 1; i < m; i++ {
		j := fail[i-1]
		for j > 0 && evil[i] != evil[j] {
			j = fail[j-1]
		}
		if evil[i] == evil[j] {
			j++
		}
		fail[i] = j
	}

	// transition table: state (matched prefix length) x next character -> new matched length
	trans := make([][26]int, m+1)
	for st := 0; st <= m; st++ {
		for c := 0; c < 26; c++ {
			if st == m {
				trans[st][c] = m
				continue
			}
			ch := byte('a' + c)
			ns := st
			for ns > 0 && evil[ns] != ch {
				ns = fail[ns-1]
			}
			if evil[ns] == ch {
				ns++
			}
			trans[st][c] = ns
		}
	}

	// dp[pos parity][state][tightLow][tightHigh]
	dp := make([][][][]int, 2)
	for i := 0; i < 2; i++ {
		dp[i] = make([][][]int, m)
		for j := 0; j < m; j++ {
			dp[i][j] = make([][]int, 2)
			for k := 0; k < 2; k++ {
				dp[i][j][k] = make([]int, 2)
			}
		}
	}

	cur := 0
	dp[cur][0][1][1] = 1

	for pos := 0; pos < n; pos++ {
		nxt := 1 - cur
		// reset next layer
		for st := 0; st < m; st++ {
			for tl := 0; tl < 2; tl++ {
				for th := 0; th < 2; th++ {
					dp[nxt][st][tl][th] = 0
				}
			}
		}

		lowChar := s1[pos]
		highChar := s2[pos]

		for st := 0; st < m; st++ {
			for tl := 0; tl < 2; tl++ {
				for th := 0; th < 2; th++ {
					val := dp[cur][st][tl][th]
					if val == 0 {
						continue
					}
					lo := byte('a')
					hi := byte('z')
					if tl == 1 {
						lo = lowChar
					}
					if th == 1 {
						hi = highChar
					}
					for c := lo; c <= hi; c++ {
						ns := trans[st][c-'a']
						if ns == m { // contains evil, skip
							continue
						}
						ntl := tl
						nth := th
						if tl == 1 && c != lowChar {
							ntl = 0
						}
						if th == 1 && c != highChar {
							nth = 0
						}
						dp[nxt][ns][ntl][nth] = (dp[nxt][ns][ntl][nth] + val) % MOD
					}
				}
			}
		}
		cur = nxt
	}

	ans := 0
	for st := 0; st < m; st++ {
		for tl := 0; tl < 2; tl++ {
			for th := 0; th < 2; th++ {
				ans = (ans + dp[cur][st][tl][th]) % MOD
			}
		}
	}
	return ans
}
```

## Ruby

```ruby
def find_good_strings(n, s1, s2, evil)
  mod = 1_000_000_007
  m = evil.length

  # KMP prefix function
  pi = Array.new(m, 0)
  (1...m).each do |i|
    j = pi[i - 1]
    while j > 0 && evil[i] != evil[j]
      j = pi[j - 1]
    end
    j += 1 if evil[i] == evil[j]
    pi[i] = j
  end

  # Transition table for automaton
  trans = Array.new(m) { Array.new(26, 0) }
  (0...m).each do |state|
    26.times do |c|
      ch = (97 + c).chr
      if state < m && ch == evil[state]
        trans[state][c] = state + 1
      else
        j = state
        while j > 0 && ch != evil[j]
          j = pi[j - 1]
        end
        trans[state][c] = (ch == evil[j]) ? j + 1 : 0
      end
    end
  end

  # dp[state][lowFlag][highFlag]
  dp = Array.new(m) { Array.new(2) { Array.new(2, 0) } }
  dp[0][1][1] = 1

  (0...n).each do |pos|
    ndp = Array.new(m) { Array.new(2) { Array.new(2, 0) } }
    s1_c = s1[pos].ord - 97
    s2_c = s2[pos].ord - 97
    (0...m).each do |state|
      (0..1).each do |low|
        (0..1).each do |high|
          cur = dp[state][low][high]
          next if cur == 0
          min_c = low == 1 ? s1_c : 0
          max_c = high == 1 ? s2_c : 25
          (min_c..max_c).each do |c|
            new_low = (low == 1 && c == s1_c) ? 1 : 0
            new_high = (high == 1 && c == s2_c) ? 1 : 0
            ns = trans[state][c]
            next if ns == m # evil substring matched
            ndp[ns][new_low][new_high] = (ndp[ns][new_low][new_high] + cur) % mod
          end
        end
      end
    end
    dp = ndp
  end

  ans = 0
  (0...m).each do |state|
    (0..1).each do |low|
      (0..1).each do |high|
        ans = (ans + dp[state][low][high]) % mod
      end
    end
  end
  ans
end
```

## Scala

```scala
object Solution {
    def findGoodStrings(n: Int, s1: String, s2: String, evil: String): Int = {
        val MOD = 1000000007L
        val m = evil.length

        // Build LPS array for KMP
        val lps = new Array[Int](m)
        var len = 0
        var i = 1
        while (i < m) {
            if (evil.charAt(i) == evil.charAt(len)) {
                len += 1
                lps(i) = len
                i += 1
            } else {
                if (len != 0) {
                    len = lps(len - 1)
                } else {
                    lps(i) = 0
                    i += 1
                }
            }
        }

        // Build transition table: state x char -> nextState
        val trans = Array.ofDim[Int](m, 26)
        for (state <- 0 until m) {
            for (cIdx <- 0 until 26) {
                val ch = ('a' + cIdx).toChar
                var cur = state
                while (cur > 0 && evil.charAt(cur) != ch) {
                    cur = lps(cur - 1)
                }
                if (evil.charAt(cur) == ch) trans(state)(cIdx) = cur + 1
                else trans(state)(cIdx) = cur
            }
        }

        // DP[pos][state][tightLow][tightHigh]
        val dp = Array.ofDim[Long](n + 1, m, 2, 2)
        dp(0)(0)(1)(1) = 1L

        for (pos <- 0 until n) {
            for (state <- 0 until m) {
                for (tightLow <- 0 to 1) {
                    for (tightHigh <- 0 to 1) {
                        val curVal = dp(pos)(state)(tightLow)(tightHigh)
                        if (curVal == 0L) continue
                        val lowChar = if (tightLow == 1) s1.charAt(pos) else 'a'
                        val highChar = if (tightHigh == 1) s2.charAt(pos) else 'z'
                        val loIdx = lowChar - 'a'
                        val hiIdx = highChar - 'a'
                        var cIdx = loIdx
                        while (cIdx <= hiIdx) {
                            val newTightLow = if (tightLow == 1 && cIdx == loIdx) 1 else 0
                            val newTightHigh = if (tightHigh == 1 && cIdx == hiIdx) 1 else 0
                            val nextState = trans(state)(cIdx)
                            if (nextState < m) {
                                var add = dp(pos + 1)(nextState)(newTightLow)(newTightHigh) + curVal
                                if (add >= MOD) add -= MOD
                                dp(pos + 1)(nextState)(newTightLow)(newTightHigh) = add
                            }
                            cIdx += 1
                        }
                    }
                }
            }
        }

        var ans = 0L
        for (state <- 0 until m) {
            for (tightLow <- 0 to 1) {
                for (tightHigh <- 0 to 1) {
                    ans += dp(n)(state)(tightLow)(tightHigh)
                    if (ans >= MOD) ans -= MOD
                }
            }
        }
        (ans % MOD).toInt
    }

    // Helper to emulate continue in while loops
    private def continue: Unit = {}
}
```

## Rust

```rust
use std::cmp::{max, min};

const MOD: i64 = 1_000_000_007;

fn dfs(
    pos: usize,
    state: usize,
    low: bool,
    high: bool,
    n: usize,
    s1: &[u8],
    s2: &[u8],
    m: usize,
    trans: &Vec<Vec<usize>>,
    dp: &mut Vec<i64>,
) -> i64 {
    if pos == n {
        return 1;
    }
    let idx = (((pos * m + state) << 2) | ((low as usize) << 1) | (high as usize));
    if dp[idx] != -1 {
        return dp[idx];
    }
    let lo = if low { s1[pos] } else { b'a' };
    let hi = if high { s2[pos] } else { b'z' };
    let mut ans: i64 = 0;
    for ch in lo..=hi {
        let new_low = low && (ch == s1[pos]);
        let new_high = high && (ch == s2[pos]);
        let next_state = trans[state][(ch - b'a') as usize];
        if next_state == m {
            continue;
        }
        ans += dfs(
            pos + 1,
            next_state,
            new_low,
            new_high,
            n,
            s1,
            s2,
            m,
            trans,
            dp,
        );
        if ans >= MOD {
            ans -= MOD;
        }
    }
    dp[idx] = ans % MOD;
    dp[idx]
}

impl Solution {
    pub fn find_good_strings(n: i32, s1: String, s2: String, evil: String) -> i32 {
        let n_usize = n as usize;
        let s1_bytes = s1.as_bytes();
        let s2_bytes = s2.as_bytes();
        let evil_bytes = evil.as_bytes();
        let m = evil_bytes.len();

        // build lps (failure function)
        let mut lps = vec![0usize; m];
        for i in 1..m {
            let mut len = lps[i - 1];
            while len > 0 && evil_bytes[i] != evil_bytes[len] {
                len = lps[len - 1];
            }
            if evil_bytes[i] == evil_bytes[len] {
                len += 1;
            }
            lps[i] = len;
        }

        // build transition table
        let mut trans = vec![vec![0usize; 26]; m];
        for state in 0..m {
            for c in 0..26 {
                let ch = b'a' + c as u8;
                let mut k = state;
                while k > 0 && evil_bytes[k] != ch {
                    k = lps[k - 1];
                }
                if evil_bytes[k] == ch {
                    k += 1;
                }
                trans[state][c] = k;
            }
        }

        // dp array: size (n * m * 4)
        let total_states = n_usize * m * 4;
        let mut dp = vec![-1i64; total_states];

        let result = dfs(
            0,
            0,
            true,
            true,
            n_usize,
            s1_bytes,
            s2_bytes,
            m,
            &trans,
            &mut dp,
        );
        (result % MOD) as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define (find-good-strings n s1 s2 evil)
  (let* ((m (string-length evil))
         ;; build failure function for KMP
         (fail (make-vector m 0))
         (build-fail
          (let loop ((i 1) (j 0))
            (when (< i m)
              (begin
                (while (and (> j 0)
                            (not (char=? (string-ref evil i)
                                         (string-ref evil j))))
                  (set! j (vector-ref fail (- j 1))))
                (when (char=? (string-ref evil i) (string-ref evil j))
                  (set! j (+ j 1)))
                (vector-set! fail i j)
                (loop (+ i 1) j)))))
         ;; build transition table
         (trans (let ((tbl (make-vector (+ m 1) #f)))
                  (for ([state (in-range (+ m 1))])
                    (define row (make-vector 26 0))
                    (vector-set! tbl state row)
                    (for ([ci (in-range 26)])
                      (define ch (integer->char (+ (char->integer #\a) ci)))
                      (if (= state m)
                          (vector-set! row ci m) ; stay in forbidden state
                          (let loop ((k state))
                            (cond
                              [(and (< k m) (char=? ch (string-ref evil k)))
                               (vector-set! row ci (+ k 1))]
                              [(> k 0)
                               (loop (vector-ref fail (- k 1)))]
                              [else
                               (vector-set! row ci 0)])))))
                  tbl))
         ;; memoization hash
         (memo (make-hash))
         ;; recursive DP
         (dfs
          (letrec ((proc (lambda (pos state low high)
                           (if (= pos n)
                               1
                               (let ((key (list pos state low high)))
                                 (or (hash-ref memo key #f)
                                     (let* ((lowChar (if low
                                                        (char->integer (string-ref s1 pos))
                                                        (char->integer #\a)))
                                            (highChar (if high
                                                         (char->integer (string-ref s2 pos))
                                                         (char->integer #\z))))
                                       (define sum 0)
                                       (for ([c (in-range lowChar (+ highChar 1))])
                                         (let* ((nextState (vector-ref (vector-ref trans state) (- c (char->integer #\a)))))
                                           (when (< nextState m)
                                             (define newLow (and low (= c lowChar)))
                                             (define newHigh (and high (= c highChar)))
                                             (set! sum (+ sum (proc (+ pos 1) nextState newLow newHigh))))))
                                       (set! sum (modulo sum MOD))
                                       (hash-set! memo key sum)
                                       sum)))))))
            proc)))
    (dfs 0 0 #t #t)))
```

## Erlang

```erlang
-module(solution).
-export([find_good_strings/4]).

-define(MOD, 1000000007).

find_good_strings(N, S1, S2, Evil) ->
    Mod = ?MOD,
    Pat = binary_to_list(Evil),
    M = length(Pat),
    NextTable = build_next(Pat),
    S1List = binary_to_list(S1),
    S2List = binary_to_list(S2),
    InitialMap = #{ {0, true, true} => 1 },
    FinalMap = dp_loop(0, N, Pat, M, NextTable, S1List, S2List, Mod, InitialMap),
    sum_map(FinalMap, Mod).

%% Build transition table: for each state j (matched prefix length) and character c,
%% give new matched length.
build_next(Pat) ->
    M = length(Pat),
    lists:map(
        fun(J) ->
            lists:map(
                fun(Offset) ->
                    C = $a + Offset,
                    compute_next_state(J, C, Pat)
                end,
                lists:seq(0, 25)
            )
        end,
        lists:seq(0, M - 1)
    ).

compute_next_state(J, C, Pat) ->
    Prefix = lists:sublist(Pat, J) ++ [C],
    MaxK = min(length(Prefix), length(Pat)),
    find_k(MaxK, Prefix, Pat).

find_k(0, _Prefix, _Pat) -> 0;
find_k(K, Prefix, Pat) ->
    LenPref = length(Prefix),
    Start = LenPref - K + 1,
    Suffix = lists:sublist(Prefix, Start, K),
    PatPref = lists:sublist(Pat, 1, K),
    case Suffix == PatPref of
        true -> K;
        false -> find_k(K - 1, Prefix, Pat)
    end.

dp_loop(Pos, N, _Pat, _M, _NextTable, _S1List, _S2List, _Mod, CurrMap) when Pos =:= N ->
    CurrMap;
dp_loop(Pos, N, Pat, M, NextTable, S1List, S2List, Mod, CurrMap) ->
    S1Char = lists:nth(Pos + 1, S1List),
    S2Char = lists:nth(Pos + 1, S2List),
    NextMap = maps:fold(
        fun({J, TL, TH}, Count, Acc) ->
            Low = if TL -> S1Char; true -> $a end,
            High = if TH -> S2Char; true -> $z end,
            lists:foldl(
                fun(C, InnerAcc) ->
                    NewTL = TL andalso (C =:= S1Char),
                    NewTH = TH andalso (C =:= S2Char),
                    NextJ = get_next(J, C, NextTable),
                    case NextJ of
                        M -> InnerAcc; % evil substring formed, discard
                        _ ->
                            Key = {NextJ, NewTL, NewTH},
                            Prev = maps:get(Key, InnerAcc, 0),
                            Updated = (Prev + Count) rem Mod,
                            maps:put(Key, Updated, InnerAcc)
                    end
                end,
                Acc,
                lists:seq(Low, High)
            )
        end,
        #{},
        CurrMap
    ),
    dp_loop(Pos + 1, N, Pat, M, NextTable, S1List, S2List, Mod, NextMap).

get_next(J, C, NextTable) ->
    Row = lists:nth(J + 1, NextTable),
    Offset = C - $a,
    lists:nth(Offset + 1, Row).

sum_map(Map, Mod) ->
    maps:fold(
        fun(_Key, Val, Acc) -> (Acc + Val) rem Mod end,
        0,
        Map
    ).
```

## Elixir

```elixir
defmodule Solution do
  @modulus 1_000_000_007

  @spec find_good_strings(integer, String.t(), String.t(), String.t()) :: integer
  def find_good_strings(n, s1, s2, evil) do
    pat = String.to_charlist(evil) |> Enum.map(&(&1 - ?a))
    m = length(pat)
    pi = compute_pi(pat)

    trans =
      Enum.map(0..m, fn state ->
        inner = Enum.map(0..25, fn ch -> next_state(state, ch, pat, pi) end)
        List.to_tuple(inner)
      end)
      |> List.to_tuple()

    s1_arr = String.to_charlist(s1) |> Enum.map(&(&1 - ?a))
    s2_arr = String.to_charlist(s2) |> Enum.map(&(&1 - ?a))

    dp_initial = %{{0, true, true} => 1}

    dp_final =
      Enum.reduce(0..(n - 1), dp_initial, fn pos, cur_dp ->
        new_dp = %{}
        Enum.each(cur_dp, fn {{state, low_eq, high_eq}, cnt} ->
          low_c = if low_eq, do: Enum.at(s1_arr, pos), else: 0
          high_c = if high_eq, do: Enum.at(s2_arr, pos), else: 25

          for ch <- low_c..high_c do
            new_low = low_eq && (ch == Enum.at(s1_arr, pos))
            new_high = high_eq && (ch == Enum.at(s2_arr, pos))
            ns = elem(elem(trans, state), ch)

            if ns != m do
              key = {ns, new_low, new_high}
              prev = Map.get(new_dp, key, 0)
              new_val = rem(prev + cnt, @modulus)
              new_dp = Map.put(new_dp, key, new_val)
            end
          end
        end)

        new_dp
      end)

    Enum.reduce(dp_final, 0, fn {_k, v}, acc -> rem(acc + v, @modulus) end)
  end

  # Compute prefix function (KMP pi array) for pattern pat
  defp compute_pi(pat) do
    m = length(pat)
    pi = List.duplicate(0, m)

    {pi, _} =
      Enum.reduce(1..(m - 1), {pi, 0}, fn i, {list, j} ->
        pj = Enum.at(pat, i)

        j2 =
          if j > 0 && pj != Enum.at(pat, j) do
            fallback(j, pj, pat, list)
          else
            j
          end

        j3 = if pj == Enum.at(pat, j2), do: j2 + 1, else: j2
        list = List.replace_at(list, i, j3)
        {list, j3}
      end)

    pi
  end

  # Recursive fallback using previously computed pi values
  defp fallback(j, ch, pat, pi_list) do
    if j == 0 do
      0
    else
      if Enum.at(pat, j) == ch do
        j
      else
        fallback(Enum.at(pi_list, j - 1), ch, pat, pi_list)
      end
    end
  end

  # Transition function using KMP automaton logic
  defp next_state(state, ch, pat, pi) do
    m = length(pat)

    cond do
      state < m && Enum.at(pat, state) == ch ->
        state + 1

      state == 0 ->
        0

      true ->
        next_state(Enum.at(pi, state - 1), ch, pat, pi)
    end
  end
end
```
