# 0730. Count Different Palindromic Subsequences

## Cpp

```cpp
class Solution {
public:
    int countPalindromicSubsequences(string s) {
        const int MOD = 1000000007;
        int n = s.size();
        vector<vector<int>> dp(n, vector<int>(n, 0));
        // next occurrence
        vector<array<int,4>> nxt(n);
        array<int,4> last;
        last.fill(-1);
        for (int i = n - 1; i >= 0; --i) {
            last[s[i] - 'a'] = i;
            nxt[i] = last;
        }
        // previous occurrence
        vector<array<int,4>> prv(n);
        array<int,4> prev;
        prev.fill(-1);
        for (int i = 0; i < n; ++i) {
            prev[s[i] - 'a'] = i;
            prv[i] = prev;
        }
        // base case length 1
        for (int i = 0; i < n; ++i) dp[i][i] = 1;
        // lengths >=2
        for (int len = 2; len <= n; ++len) {
            for (int i = 0; i + len - 1 < n; ++i) {
                int j = i + len - 1;
                if (s[i] == s[j]) {
                    int c = s[i] - 'a';
                    long long inner = (i + 1 <= j - 1) ? dp[i+1][j-1] : 0;
                    int l = (i + 1 < n) ? nxt[i+1][c] : -1;
                    int r = (j - 1 >= 0) ? prv[j-1][c] : -1;
                    if (l == -1 || r == -1 || l > r) {
                        dp[i][j] = (int)((2LL * inner + 2) % MOD);
                    } else if (l == r) {
                        dp[i][j] = (int)((2LL * inner + 1) % MOD);
                    } else {
                        int sub = dp[l+1][r-1];
                        long long val = (2LL * inner - sub) % MOD;
                        if (val < 0) val += MOD;
                        dp[i][j] = (int)val;
                    }
                } else {
                    long long val = ((long long)dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]) % MOD;
                    if (val < 0) val += MOD;
                    dp[i][j] = (int)val;
                }
            }
        }
        return dp[0][n-1];
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    public int countPalindromicSubsequences(String s) {
        int n = s.length();
        if (n == 0) return 0;
        // next[i][c]: first occurrence of char c ('a'..'d') at or after i
        int[][] next = new int[n][4];
        // prev[i][c]: last occurrence of char c at or before i
        int[][] prev = new int[n][4];

        int[] nxt = new int[4];
        for (int i = 0; i < 4; i++) nxt[i] = -1;
        for (int i = n - 1; i >= 0; --i) {
            nxt[s.charAt(i) - 'a'] = i;
            for (int c = 0; c < 4; ++c) next[i][c] = nxt[c];
        }

        int[] prv = new int[4];
        for (int i = 0; i < 4; ++i) prv[i] = -1;
        for (int i = 0; i < n; ++i) {
            prv[s.charAt(i) - 'a'] = i;
            for (int c = 0; c < 4; ++c) prev[i][c] = prv[c];
        }

        int[][] dp = new int[n][n];
        for (int i = 0; i < n; ++i) dp[i][i] = 1;

        for (int len = 2; len <= n; ++len) {
            for (int i = 0; i + len - 1 < n; ++i) {
                int j = i + len - 1;
                if (s.charAt(i) == s.charAt(j)) {
                    int c = s.charAt(i) - 'a';
                    int low = (i + 1 <= j - 1) ? next[i + 1][c] : -1;
                    int high = (i + 1 <= j - 1) ? prev[j - 1][c] : -1;

                    if (low == -1 || low > j - 1) { // no same char inside
                        dp[i][j] = (int)((2L * dp[i + 1][j - 1] + 2) % MOD);
                    } else if (low == high) { // exactly one same char inside
                        dp[i][j] = (int)((2L * dp[i + 1][j - 1] + 1) % MOD);
                    } else {
                        int inner = (low + 1 <= high - 1) ? dp[low + 1][high - 1] : 0;
                        long val = 2L * dp[i + 1][j - 1] - inner;
                        val %= MOD;
                        if (val < 0) val += MOD;
                        dp[i][j] = (int) val;
                    }
                } else {
                    long val = (dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]) % MOD;
                    if (val < 0) val += MOD;
                    dp[i][j] = (int) val;
                }
            }
        }

        return dp[0][n - 1];
    }
}
```

## Python

```python
class Solution(object):
    def countPalindromicSubsequences(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(s)
        if n == 0:
            return 0

        # dp[i][j] = number of distinct palindromic subsequences in s[i..j]
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1  # single character

        # precompute next and previous occurrence indices for each character a-d
        nxt = [[-1] * 4 for _ in range(n)]
        prv = [[-1] * 4 for _ in range(n)]

        last = [-1] * 4
        for i, ch in enumerate(s):
            idx = ord(ch) - 97
            last[idx] = i
            for k in range(4):
                prv[i][k] = last[k]

        next_occ = [-1] * 4
        for i in range(n - 1, -1, -1):
            idx = ord(s[i]) - 97
            next_occ[idx] = i
            for k in range(4):
                nxt[i][k] = next_occ[k]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    c = ord(s[i]) - 97
                    lo = nxt[i + 1][c]   # first occurrence of c after i
                    hi = prv[j - 1][c]   # last occurrence of c before j
                    if lo == -1 or lo > j - 1:
                        dp[i][j] = (2 * dp[i + 1][j - 1] + 2) % MOD
                    elif lo == hi:
                        dp[i][j] = (2 * dp[i + 1][j - 1] + 1) % MOD
                    else:
                        dp[i][j] = (2 * dp[i + 1][j - 1] - dp[lo + 1][hi - 1]) % MOD
                else:
                    dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]) % MOD

        return dp[0][n - 1] % MOD
```

## Python3

```python
class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        if n == 0:
            return 0

        # map characters to indices 0..3
        mp = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
        # next_pos[i][c] = first occurrence of char c at or after i, else -1
        next_pos = [[-1] * 4 for _ in range(n + 1)]
        for c in range(4):
            next_pos[n][c] = -1
        for i in range(n - 1, -1, -1):
            for c in range(4):
                next_pos[i][c] = next_pos[i + 1][c]
            idx = mp[s[i]]
            next_pos[i][idx] = i

        # prev_pos[i][c] = last occurrence of char c at or before i, else -1
        prev_pos = [[-1] * 4 for _ in range(n)]
        last = [-1] * 4
        for i in range(n):
            for c in range(4):
                prev_pos[i][c] = last[c]
            idx = mp[s[i]]
            last[idx] = i

        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1  # single character palindrome

        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    idx = mp[s[i]]
                    lo = next_pos[i + 1][idx]   # first same char inside
                    hi = prev_pos[j - 1][idx]   # last same char inside
                    inner = dp[i + 1][j - 1] if i + 1 <= j - 1 else 0
                    if lo == -1 or lo > j - 1:          # no same char inside
                        val = (2 * inner + 2) % MOD
                    elif lo == hi:                       # exactly one same char inside
                        val = (2 * inner + 1) % MOD
                    else:                                 # at least two same chars inside
                        sub = dp[lo + 1][hi - 1] if lo + 1 <= hi - 1 else 0
                        val = (2 * inner - sub) % MOD
                else:
                    val = (dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]) % MOD
                dp[i][j] = val if val >= 0 else val + MOD

        return dp[0][n - 1] % MOD
```

## C

```c
#include <string.h>
#include <stdlib.h>

int countPalindromicSubsequences(char* s) {
    const int MOD = 1000000007;
    int n = strlen(s);
    int *dp = (int*)calloc(n * n, sizeof(int));
    #define DP(i,j) dp[(i) * n + (j)]

    for (int i = 0; i < n; ++i) DP(i,i) = 1;

    for (int len = 2; len <= n; ++len) {
        for (int i = 0; i + len - 1 < n; ++i) {
            int j = i + len - 1;
            if (s[i] == s[j]) {
                char c = s[i];
                int l = i + 1;
                while (l <= j && s[l] != c) ++l;
                int r = j - 1;
                while (r >= i && s[r] != c) --r;

                long long inner = (i + 1 <= j - 1) ? DP(i+1, j-1) : 0;
                long long val;
                if (l > r) {
                    val = 2 * inner + 2;
                } else if (l == r) {
                    val = 2 * inner + 1;
                } else {
                    long long inner2 = (l + 1 <= r - 1) ? DP(l+1, r-1) : 0;
                    val = 2 * inner - inner2;
                }
                val %= MOD;
                if (val < 0) val += MOD;
                DP(i,j) = (int)val;
            } else {
                long long val = (long long)DP(i+1, j) + DP(i, j-1) - DP(i+1, j-1);
                val %= MOD;
                if (val < 0) val += MOD;
                DP(i,j) = (int)val;
            }
        }
    }

    int result = DP(0, n-1);
    free(dp);
    #undef DP
    return result;
}
```

## Csharp

```csharp
using System;

public class Solution {
    private const int MOD = 1000000007;
    public int CountPalindromicSubsequences(string s) {
        int n = s.Length;
        if (n == 0) return 0;
        int[,] dp = new int[n, n];

        // next[i,c] = first index >= i where character c appears, -1 if none
        int[,] next = new int[n, 4];
        int[] nxtPos = new int[4];
        for (int c = 0; c < 4; c++) nxtPos[c] = -1;
        for (int i = n - 1; i >= 0; i--) {
            nxtPos[s[i] - 'a'] = i;
            for (int c = 0; c < 4; c++) next[i, c] = nxtPos[c];
        }

        // prev[i,c] = last index <= i where character c appears, -1 if none
        int[,] prev = new int[n, 4];
        int[] prvPos = new int[4];
        for (int c = 0; c < 4; c++) prvPos[c] = -1;
        for (int i = 0; i < n; i++) {
            prvPos[s[i] - 'a'] = i;
            for (int c = 0; c < 4; c++) prev[i, c] = prvPos[c];
        }

        // base case: length 1
        for (int i = 0; i < n; i++) dp[i, i] = 1;

        for (int len = 2; len <= n; len++) {
            for (int i = 0; i + len - 1 < n; i++) {
                int j = i + len - 1;
                long val;
                if (s[i] == s[j]) {
                    int ch = s[i] - 'a';
                    int low = (i + 1 < n) ? next[i + 1, ch] : -1;   // first same char after i
                    int high = (j - 1 >= 0) ? prev[j - 1, ch] : -1; // last same char before j

                    long inner = (i + 1 <= j - 1) ? dp[i + 1, j - 1] : 0;

                    if (low == -1 || low > j - 1) {
                        // no same character inside
                        val = (2L * inner + 2) % MOD;
                    } else if (low == high) {
                        // exactly one same character inside
                        val = (2L * inner + 1) % MOD;
                    } else {
                        // at least two same characters inside
                        long sub = (low + 1 <= high - 1) ? dp[low + 1, high - 1] : 0;
                        val = (2L * inner - sub) % MOD;
                    }
                } else {
                    long a = dp[i + 1, j];
                    long b = dp[i, j - 1];
                    long c = dp[i + 1, j - 1];
                    val = (a + b - c) % MOD;
                }

                if (val < 0) val += MOD;
                dp[i, j] = (int)val;
            }
        }

        return dp[0, n - 1];
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var countPalindromicSubsequences = function(s) {
    const MOD = 1000000007;
    const n = s.length;
    if (n === 0) return 0;

    // next[i][c] = first occurrence of char c ('a'..'d') at or after i
    const next = Array.from({ length: n }, () => Array(4).fill(-1));
    // prev[i][c] = last occurrence of char c at or before i
    const prev = Array.from({ length: n }, () => Array(4).fill(-1));

    for (let i = n - 1; i >= 0; --i) {
        if (i < n - 1) {
            for (let k = 0; k < 4; ++k) next[i][k] = next[i + 1][k];
        }
        const idx = s.charCodeAt(i) - 97; // 'a' -> 0
        next[i][idx] = i;
    }

    for (let i = 0; i < n; ++i) {
        if (i > 0) {
            for (let k = 0; k < 4; ++k) prev[i][k] = prev[i - 1][k];
        }
        const idx = s.charCodeAt(i) - 97;
        prev[i][idx] = i;
    }

    // dp[i][j]: number of distinct non‑empty palindromic subsequences in s[i..j]
    const dp = Array.from({ length: n }, () => Array(n).fill(0));

    for (let len = 1; len <= n; ++len) {
        for (let i = 0; i + len - 1 < n; ++i) {
            const j = i + len - 1;
            if (len === 1) {
                dp[i][j] = 1; // single character
                continue;
            }
            let total = 0;
            for (let k = 0; k < 4; ++k) {
                const l = next[i][k];
                const r = prev[j][k];
                if (l === -1 || l > j) continue; // character not present in range
                if (l === r) {
                    total = (total + 1) % MOD; // only one occurrence -> single char palindrome
                } else {
                    const inner = (l + 1 <= r - 1) ? dp[l + 1][r - 1] : 0;
                    total = (total + 2 + inner) % MOD; // "c", "cc" plus extensions
                }
            }
            dp[i][j] = total;
        }
    }

    return dp[0][n - 1] % MOD;
};
```

## Typescript

```typescript
function countPalindromicSubsequences(s: string): number {
    const MOD = 1_000_000_007;
    const n = s.length;
    if (n === 0) return 0;

    // dp[i][j]: number of distinct palindromic subsequences in s[i..j]
    const dp: number[][] = Array.from({ length: n }, () => new Array<number>(n).fill(0));
    for (let i = 0; i < n; ++i) dp[i][i] = 1;

    // nextPos[i][c]: smallest index >= i where character c appears, or n if none
    const nextPos: number[][] = Array.from({ length: n }, () => new Array<number>(4).fill(n));
    const nxtTmp = [n, n, n, n];
    for (let i = n - 1; i >= 0; --i) {
        nxtTmp[s.charCodeAt(i) - 97] = i;
        for (let k = 0; k < 4; ++k) nextPos[i][k] = nxtTmp[k];
    }

    // prevPos[i][c]: largest index <= i where character c appears, or -1 if none
    const prevPos: number[][] = Array.from({ length: n }, () => new Array<number>(4).fill(-1));
    const prvTmp = [-1, -1, -1, -1];
    for (let i = 0; i < n; ++i) {
        prvTmp[s.charCodeAt(i) - 97] = i;
        for (let k = 0; k < 4; ++k) prevPos[i][k] = prvTmp[k];
    }

    for (let len = 2; len <= n; ++len) {
        for (let i = 0; i + len - 1 < n; ++i) {
            const j = i + len - 1;
            if (s[i] === s[j]) {
                const cIdx = s.charCodeAt(i) - 97;
                const ni = nextPos[i + 1][cIdx];
                const pj = prevPos[j - 1][cIdx];
                if (ni > pj) {
                    // no same character inside
                    dp[i][j] = (2 * dp[i + 1][j - 1] + 2) % MOD;
                } else if (ni === pj) {
                    // exactly one same character inside
                    dp[i][j] = (2 * dp[i + 1][j - 1] + 1) % MOD;
                } else {
                    // at least two same characters inside
                    const sub = dp[ni + 1][pj - 1];
                    dp[i][j] = ((2 * dp[i + 1][j - 1] - sub) % MOD + MOD) % MOD;
                }
            } else {
                dp[i][j] = ((dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]) % MOD + MOD) % MOD;
            }
        }
    }

    return dp[0][n - 1];
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function countPalindromicSubsequences($s) {
        $MOD = 1000000007;
        $n = strlen($s);
        if ($n == 0) return 0;

        // dp[i][j] number of distinct non‑empty palindromic subsequences in s[i..j]
        $dp = array_fill(0, $n, array_fill(0, $n, 0));

        // base case: single characters
        for ($i = 0; $i < $n; $i++) {
            $dp[$i][$i] = 1;
        }

        // precompute next and prev occurrence for each character (a,b,c,d)
        $next = array_fill(0, $n, array_fill(0, 4, -1));
        $prev = array_fill(0, $n, array_fill(0, 4, -1));

        $last = array_fill(0, 4, -1);
        for ($i = $n - 1; $i >= 0; $i--) {
            $cIdx = ord($s[$i]) - 97;
            for ($k = 0; $k < 4; $k++) {
                $next[$i][$k] = $last[$k];
            }
            $last[$cIdx] = $i;
        }

        $last = array_fill(0, 4, -1);
        for ($i = 0; $i < $n; $i++) {
            $cIdx = ord($s[$i]) - 97;
            for ($k = 0; $k < 4; $k++) {
                $prev[$i][$k] = $last[$k];
            }
            $last[$cIdx] = $i;
        }

        // DP over lengths
        for ($len = 2; $len <= $n; $len++) {
            for ($i = 0; $i + $len - 1 < $n; $i++) {
                $j = $i + $len - 1;

                if ($s[$i] === $s[$j]) {
                    $cIdx = ord($s[$i]) - 97;
                    $l = $next[$i][$cIdx];   // first same char after i
                    $r = $prev[$j][$cIdx];   // last same char before j

                    $inner = ($i + 1 <= $j - 1) ? $dp[$i + 1][$j - 1] : 0;

                    if ($l == -1 || $l > $r) {
                        // no same character inside
                        $val = (2 * $inner + 2) % $MOD;
                    } elseif ($l == $r) {
                        // exactly one same character inside
                        $val = (2 * $inner + 1) % $MOD;
                    } else {
                        // at least two same characters inside
                        $mid = ($l + 1 <= $r - 1) ? $dp[$l + 1][$r - 1] : 0;
                        $val = (2 * $inner - $mid) % $MOD;
                        if ($val < 0) $val += $MOD;
                    }
                } else {
                    $a = ($i + 1 <= $j) ? $dp[$i + 1][$j] : 0;
                    $b = ($i <= $j - 1) ? $dp[$i][$j - 1] : 0;
                    $c = ($i + 1 <= $j - 1) ? $dp[$i + 1][$j - 1] : 0;
                    $val = ($a + $b - $c) % $MOD;
                    if ($val < 0) $val += $MOD;
                }

                $dp[$i][$j] = $val;
            }
        }

        return $dp[0][$n - 1];
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    private let MOD = 1_000_000_007
    
    func countPalindromicSubsequences(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        if n == 0 { return 0 }
        
        // map character to index 0..3
        func idx(_ c: Character) -> Int {
            return Int(c.unicodeScalars.first!.value - UnicodeScalar("a").value)
        }
        
        // next[i][k]: smallest position >= i with char k, else -1
        var next = Array(repeating: Array(repeating: -1, count: 4), count: n)
        var last = Array(repeating: -1, count: 4)
        for i in stride(from: n - 1, through: 0, by: -1) {
            let cIdx = idx(chars[i])
            last[cIdx] = i
            for k in 0..<4 { next[i][k] = last[k] }
        }
        
        // prev[i][k]: largest position <= i with char k, else -1
        var prev = Array(repeating: Array(repeating: -1, count: 4), count: n)
        var lastPrev = Array(repeating: -1, count: 4)
        for i in 0..<n {
            let cIdx = idx(chars[i])
            lastPrev[cIdx] = i
            for k in 0..<4 { prev[i][k] = lastPrev[k] }
        }
        
        var dp = Array(repeating: Array(repeating: 0, count: n), count: n)
        // length 1 substrings
        for i in 0..<n {
            dp[i][i] = 1
        }
        
        if n >= 2 {
            for len in 2...n {
                for i in 0...(n - len) {
                    let j = i + len - 1
                    if chars[i] == chars[j] {
                        let cIdx = idx(chars[i])
                        var left = -1
                        if i + 1 < n { left = next[i + 1][cIdx] }
                        var right = -1
                        if j - 1 >= 0 { right = prev[j - 1][cIdx] }
                        
                        let inner = (i + 1 <= j - 1) ? dp[i + 1][j - 1] : 0
                        
                        if left == -1 || left > right {
                            // no same char inside
                            var val = (inner * 2 + 2) % MOD
                            dp[i][j] = val
                        } else if left == right {
                            var val = (inner * 2 + 1) % MOD
                            dp[i][j] = val
                        } else {
                            let sub = dp[left + 1][right - 1]
                            var val = (inner * 2 - sub) % MOD
                            if val < 0 { val += MOD }
                            dp[i][j] = val
                        }
                    } else {
                        var val = (dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]) % MOD
                        if val < 0 { val += MOD }
                        dp[i][j] = val
                    }
                }
            }
        }
        
        return dp[0][n - 1] % MOD
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countPalindromicSubsequences(s: String): Int {
        val n = s.length
        val MOD = 1_000_000_007L
        if (n == 0) return 0

        // dp[i][j] = number of distinct palindromic subsequences in s[i..j]
        val dp = Array(n) { LongArray(n) }

        // next[c][i]: the first occurrence index >= i of character c ('a'..'d'), -1 if none
        // prev[c][i]: the last occurrence index <= i of character c, -1 if none
        val next = Array(4) { IntArray(n) { -1 } }
        val prev = Array(4) { IntArray(n) { -1 } }

        for (c in 0..3) {
            var nxt = -1
            for (i in n - 1 downTo 0) {
                if (s[i] == ('a' + c)) nxt = i
                next[c][i] = nxt
            }
            var prv = -1
            for (i in 0 until n) {
                if (s[i] == ('a' + c)) prv = i
                prev[c][i] = prv
            }
        }

        // base case: single characters
        for (i in 0 until n) dp[i][i] = 1L

        for (len in 2..n) {
            for (i in 0..n - len) {
                val j = i + len - 1
                if (s[i] == s[j]) {
                    val chIdx = s[i] - 'a'
                    val low = if (i + 1 < n) next[chIdx][i + 1] else -1
                    val high = if (j - 1 >= 0) prev[chIdx][j - 1] else -1
                    val innerSub = if (i + 1 <= j - 1) dp[i + 1][j - 1] else 0L
                    var value: Long
                    if (low == -1 || low > j - 1) {
                        // no same character inside
                        value = (2 * innerSub + 2) % MOD
                    } else if (low == high) {
                        // exactly one same character inside
                        value = (2 * innerSub + 1) % MOD
                    } else {
                        val inner = if (low + 1 <= high - 1) dp[low + 1][high - 1] else 0L
                        value = (2 * innerSub - inner) % MOD
                    }
                    if (value < 0) value += MOD
                    dp[i][j] = value
                } else {
                    var value = (dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]) % MOD
                    if (value < 0) value += MOD
                    dp[i][j] = value
                }
            }
        }

        return dp[0][n - 1].toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int countPalindromicSubsequences(String s) {
    int n = s.length;
    if (n == 0) return 0;

    // Precompute next occurrence indices
    List<List<int>> next = List.generate(n, (_) => List.filled(4, -1));
    List<int> last = List.filled(4, -1);
    for (int i = n - 1; i >= 0; --i) {
      int idx = s.codeUnitAt(i) - 97; // 'a' -> 0
      last[idx] = i;
      for (int c = 0; c < 4; ++c) {
        next[i][c] = last[c];
      }
    }

    // Precompute previous occurrence indices
    List<List<int>> prev = List.generate(n, (_) => List.filled(4, -1));
    List<int> first = List.filled(4, -1);
    for (int i = 0; i < n; ++i) {
      int idx = s.codeUnitAt(i) - 97;
      first[idx] = i;
      for (int c = 0; c < 4; ++c) {
        prev[i][c] = first[c];
      }
    }

    // DP table
    List<List<int>> dp = List.generate(n, (_) => List.filled(n, 0));
    for (int i = 0; i < n; ++i) {
      dp[i][i] = 1;
    }

    for (int len = 2; len <= n; ++len) {
      for (int i = 0; i + len - 1 < n; ++i) {
        int j = i + len - 1;
        if (s.codeUnitAt(i) != s.codeUnitAt(j)) {
          dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]) % _mod;
        } else {
          int cIdx = s.codeUnitAt(i) - 97;
          int low = next[i + 1][cIdx];
          int high = prev[j - 1][cIdx];
          int inner = (i + 1 <= j - 1) ? dp[i + 1][j - 1] : 0;

          if (low == -1 || high == -1 || low > high) {
            // No same character inside
            dp[i][j] = (2 * inner + 2) % _mod;
          } else if (low == high) {
            // Exactly one same character inside
            dp[i][j] = (2 * inner + 1) % _mod;
          } else {
            int sub = (low + 1 <= high - 1) ? dp[low + 1][high - 1] : 0;
            dp[i][j] = ((2 * inner - sub) % _mod);
          }
        }

        if (dp[i][j] < 0) dp[i][j] += _mod;
      }
    }

    return dp[0][n - 1];
  }
}
```

## Golang

```go
func countPalindromicSubsequences(s string) int {
	const MOD = 1000000007
	n := len(s)
	if n == 0 {
		return 0
	}
	b := []byte(s)

	nextPos := make([][4]int, n)
	prevPos := make([][4]int, n)

	last := [4]int{-1, -1, -1, -1}
	for i := n - 1; i >= 0; i-- {
		for c := 0; c < 4; c++ {
			nextPos[i][c] = last[c]
		}
		idx := b[i] - 'a'
		last[idx] = i
	}

	last = [4]int{-1, -1, -1, -1}
	for i := 0; i < n; i++ {
		for c := 0; c < 4; c++ {
			prevPos[i][c] = last[c]
		}
		idx := b[i] - 'a'
		last[idx] = i
	}

	dp := make([][]int, n)
	for i := 0; i < n; i++ {
		dp[i] = make([]int, n)
		dp[i][i] = 1
	}

	for length := 2; length <= n; length++ {
		for i := 0; i+length-1 < n; i++ {
			j := i + length - 1
			if b[i] == b[j] {
				cIdx := b[i] - 'a'
				l := nextPos[i][cIdx]
				r := prevPos[j][cIdx]

				if l == -1 || l > j-1 { // no same char inside
					dp[i][j] = (2*dp[i+1][j-1] + 2) % MOD
				} else if l == r {
					dp[i][j] = (2*dp[i+1][j-1] + 1) % MOD
				} else {
					sub := 0
					if l+1 <= r-1 {
						sub = dp[l+1][r-1]
					}
					val := (2*dp[i+1][j-1] - sub) % MOD
					if val < 0 {
						val += MOD
					}
					dp[i][j] = val
				}
			} else {
				val := (dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]) % MOD
				if val < 0 {
					val += MOD
				}
				dp[i][j] = val
			}
		}
	}

	return dp[0][n-1] % MOD
}
```

## Ruby

```ruby
def count_palindromic_subsequences(s)
  mod = 1_000_000_007
  n = s.length
  return 0 if n == 0

  dp = Array.new(n) { Array.new(n, 0) }

  # prev[i][c] = last occurrence of character c (0..3) at or before i
  prev = Array.new(n) { Array.new(4, -1) }
  last = [-1, -1, -1, -1]
  (0...n).each do |i|
    idx = s.getbyte(i) - 97
    last[idx] = i
    4.times { |c| prev[i][c] = last[c] }
  end

  # nxt[i][c] = next occurrence of character c at or after i
  nxt = Array.new(n) { Array.new(4, -1) }
  last = [-1, -1, -1, -1]
  (n - 1).downto(0) do |i|
    idx = s.getbyte(i) - 97
    last[idx] = i
    4.times { |c| nxt[i][c] = last[c] }
  end

  n.times { |i| dp[i][i] = 1 }

  (2..n).each do |len|
    (0..(n - len)).each do |i|
      j = i + len - 1
      if s.getbyte(i) == s.getbyte(j)
        c_idx = s.getbyte(i) - 97
        low = nxt[i + 1][c_idx]          # first occurrence of c after i
        high = prev[j - 1][c_idx]         # last occurrence of c before j
        inner = (i + 1 <= j - 1) ? dp[i + 1][j - 1] : 0

        if low == -1 || low > j - 1
          val = (2 * inner + 2) % mod
        elsif low == high
          val = (2 * inner + 1) % mod
        else
          sub = (low + 1 <= high - 1) ? dp[low + 1][high - 1] : 0
          val = (2 * inner - sub) % mod
        end
      else
        val = (dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]) % mod
      end
      val += mod if val < 0
      dp[i][j] = val
    end
  end

  dp[0][n - 1] % mod
end
```

## Scala

```scala
object Solution {
    def countPalindromicSubsequences(s: String): Int = {
        val MOD = 1000000007L
        val n = s.length
        if (n == 0) return 0

        // dp[i][j] stores answer for substring s[i..j]
        val dp = Array.ofDim[Int](n, n)

        // nextIdx[pos][c] = smallest index >= pos where character c occurs, -1 if none
        val nextIdx = Array.ofDim[Int](n + 1, 4)
        for (c <- 0 until 4) nextIdx(n)(c) = -1
        for (i <- n - 1 to 0 by -1) {
            for (c <- 0 until 4) {
                nextIdx(i)(c) = nextIdx(i + 1)(c)
            }
            val idx = s.charAt(i) - 'a'
            nextIdx(i)(idx) = i
        }

        // prevIdx[pos][c] = largest index <= pos where character c occurs, -1 if none
        val prevIdx = Array.ofDim[Int](n, 4)
        for (i <- 0 until n) {
            if (i > 0) {
                for (c <- 0 until 4) {
                    prevIdx(i)(c) = prevIdx(i - 1)(c)
                }
            } else {
                for (c <- 0 until 4) {
                    prevIdx(i)(c) = -1
                }
            }
            val idx = s.charAt(i) - 'a'
            prevIdx(i)(idx) = i
        }

        // DP over lengths
        for (len <- 1 to n) {
            var i = 0
            while (i + len <= n) {
                val j = i + len - 1
                if (i == j) {
                    dp(i)(j) = 1
                } else {
                    val ci = s.charAt(i) - 'a'
                    val cj = s.charAt(j) - 'a'
                    if (ci == cj) {
                        val inner = if (i + 1 <= j - 1) dp(i + 1)(j - 1) else 0
                        var low = -1
                        if (i + 1 < n) low = nextIdx(i + 1)(ci)
                        var high = -1
                        if (j - 1 >= 0) high = prevIdx(j - 1)(ci)

                        if (low == -1 || low > j - 1) {
                            // No same character inside
                            val value = (2L * inner + 2) % MOD
                            dp(i)(j) = value.toInt
                        } else if (low == high) {
                            // Exactly one same character inside
                            val value = (2L * inner + 1) % MOD
                            dp(i)(j) = value.toInt
                        } else {
                            // At least two same characters inside
                            val sub = if (low + 1 <= high - 1) dp(low + 1)(high - 1) else 0
                            var value = (2L * inner - sub) % MOD
                            if (value < 0) value += MOD
                            dp(i)(j) = value.toInt
                        }
                    } else {
                        val left = dp(i + 1)(j)
                        val right = dp(i)(j - 1)
                        val both = dp(i + 1)(j - 1)
                        var value = (left.toLong + right - both) % MOD
                        if (value < 0) value += MOD
                        dp(i)(j) = value.toInt
                    }
                }
                i += 1
            }
        }

        dp(0)(n - 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_palindromic_subsequences(s: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let bytes = s.as_bytes();
        let n = bytes.len();
        if n == 0 {
            return 0;
        }

        // next_idx[i][c] = first occurrence of char c after position i
        let mut next_idx = vec![[n; 4]; n];
        let mut next = [n; 4];
        for i in (0..n).rev() {
            next_idx[i] = next;
            let c = (bytes[i] - b'a') as usize;
            next[c] = i;
        }

        // prev_idx[i][c] = last occurrence of char c before position i
        let mut prev_idx = vec![[n; 4]; n];
        let mut prev = [n; 4];
        for i in 0..n {
            prev_idx[i] = prev;
            let c = (bytes[i] - b'a') as usize;
            prev[c] = i;
        }

        // dp[l][r]: number of distinct palindromic subsequences in s[l..=r]
        let mut dp = vec![vec![0i64; n]; n];
        for i in 0..n {
            dp[i][i] = 1;
        }

        for len in 2..=n {
            for l in 0..=n - len {
                let r = l + len - 1;
                if bytes[l] == bytes[r] {
                    let c_idx = (bytes[l] - b'a') as usize;
                    let low = next_idx[l][c_idx];
                    let high = prev_idx[r][c_idx];
                    let inner = if l + 1 <= r.saturating_sub(1) {
                        dp[l + 1][r - 1]
                    } else {
                        0
                    };
                    let val = if low > high {
                        (2 * inner + 2) % MOD
                    } else if low == high {
                        (2 * inner + 1) % MOD
                    } else {
                        let sub = if low + 1 <= high.saturating_sub(1) {
                            dp[low + 1][high - 1]
                        } else {
                            0
                        };
                        ((2 * inner - sub) % MOD + MOD) % MOD
                    };
                    dp[l][r] = val;
                } else {
                    let val = (dp[l + 1][r] + dp[l][r - 1] - dp[l + 1][r - 1]) % MOD;
                    dp[l][r] = (val + MOD) % MOD;
                }
            }
        }

        dp[0][n - 1] as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define (char-index ch)
  (- (char->integer ch) (char->integer #\a))) ; 'a' -> 0, ..., 'd' -> 3

(define/contract (count-palindromic-subsequences s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         ;; next[i][c] = first position >= i where character c occurs, -1 if none
         (next (make-vector (+ n 1)))
         ;; prev[i][c] = last position <= i where character c occurs, -1 if none
         (prev (make-vector n))
         ;; dp[i][j] = number of distinct palindromic subsequences in s[i..j]
         (dp (make-vector n)))
    ;; initialise next vectors with -1
    (for ([i (in-range (+ n 1))])
      (vector-set! next i (make-vector 4 -1)))
    (let ((last (make-vector 4 -1)))
      (for ([i (in-range (sub1 n) -1 -1)]) ; from n-1 down to 0
        (let ((cidx (char-index (string-ref s i))))
          (vector-set! last cidx i))
        ;; copy current state of last into next[i]
        (let ((arr (make-vector 4)))
          (for ([k (in-range 4)])
            (vector-set! arr k (vector-ref last k)))
          (vector-set! next i arr))))
    ;; initialise prev vectors with -1
    (let ((last (make-vector 4 -1)))
      (for ([i (in-range n)])
        (let ((cidx (char-index (string-ref s i))))
          (vector-set! last cidx i))
        (let ((arr (make-vector 4)))
          (for ([k (in-range 4)])
            (vector-set! arr k (vector-ref last k)))
          (vector-set! prev i arr))))
    ;; initialise dp matrix
    (for ([i (in-range n)])
      (vector-set! dp i (make-vector n 0)))
    ;; DP over increasing substring lengths
    (for ([len (in-range 1 (add1 n))])
      (for ([i (in-range 0 (- n len))])
        (let* ((j (+ i (sub1 len)))
               (total
                (let loop ((c 0) (acc 0))
                  (if (= c 4)
                      acc
                      (let* ((l (vector-ref (vector-ref next i) c))
                             (r (vector-ref (vector-ref prev j) c)))
                        (cond
                          [(or (= l -1) (= r -1) (> l j) (< r i))
                           (loop (add1 c) acc)]
                          [(= l r)
                           (loop (add1 c) (+ acc 1))]
                          [else
                           (let ((inner (if (< (add1 l) (sub1 r))
                                            (vector-ref (vector-ref dp (add1 l)) (sub1 r))
                                            0)))
                             (loop (add1 c) (+ acc (+ 2 inner))))]))))))
          (vector-set! (vector-ref dp i) j (modulo total MOD)))))
    (if (= n 0)
        0
        (modulo (vector-ref (vector-ref dp 0) (sub1 n)) MOD))))
```

## Erlang

```erlang
-module(solution).
-export([count_palindromic_subsequences/1]).

-spec count_palindromic_subsequences(S :: unicode:unicode_binary()) -> integer().
count_palindromic_subsequences(S) ->
    CharList = [char_to_idx(C) || <<C>> <= S],
    N = length(CharList),
    M = 1000000007,
    NextArray = build_next_array(CharList, N),
    PrevArray = build_prev_array(CharList, N),

    DP0 = #{},
    DP = dp_fill(1, N, NextArray, PrevArray, M, DP0),
    maps:get({0, N-1}, DP).

char_to_idx($a) -> 0;
char_to_idx($b) -> 1;
char_to_idx($c) -> 2;
char_to_idx($d) -> 3.

build_next_array(CharList, N) ->
    Indices = lists:seq(N-1, 0, -1),
    {List, _} = lists:foldl(
        fun(I, {Acc, Last}) ->
            C = lists:nth(I+1, CharList),
            NewLast = setelement(C+1, Last, I),
            {[NewLast | Acc], NewLast}
        end,
        {[], {-1,-1,-1,-1}},
        Indices),
    array:from_list(List).

build_prev_array(CharList, N) ->
    Indices = lists:seq(0, N-1),
    {Rev, _} = lists:foldl(
        fun(I, {Acc, Last}) ->
            C = lists:nth(I+1, CharList),
            NewLast = setelement(C+1, Last, I),
            {[NewLast | Acc], NewLast}
        end,
        {[], {-1,-1,-1,-1}},
        Indices),
    List = lists:reverse(Rev),
    array:from_list(List).

dp_fill(Len, N, _NextArray, _PrevArray, _M, DP) when Len > N ->
    DP;
dp_fill(Len, N, NextArray, PrevArray, M, DP) ->
    MaxI = N - Len,
    DP1 = fill_i(0, MaxI, Len, NextArray, PrevArray, M, DP),
    dp_fill(Len + 1, N, NextArray, PrevArray, M, DP1).

fill_i(I, MaxI, _Len, _NextArray, _PrevArray, _M, DP) when I > MaxI ->
    DP;
fill_i(I, MaxI, Len, NextArray, PrevArray, M, DP) ->
    J = I + Len - 1,
    Sum = compute_sum(I, J, NextArray, PrevArray, M, DP),
    NewDP = maps:put({I, J}, Sum, DP),
    fill_i(I + 1, MaxI, Len, NextArray, PrevArray, M, NewDP).

compute_sum(I, J, NextArray, PrevArray, M, DP) ->
    compute_char(0, I, J, NextArray, PrevArray, M, DP, 0).

compute_char(C, _I, _J, _NextArray, _PrevArray, _M, _DP, Acc) when C > 3 ->
    Acc;
compute_char(C, I, J, NextArray, PrevArray, M, DP, Acc) ->
    NextTuple = array:get(I, NextArray),
    L = element(C+1, NextTuple),
    PrevTuple = array:get(J, PrevArray),
    R = element(C+1, PrevTuple),
    Add =
        if
            L == -1 orelse L > J -> 0;
            L == R -> 1;
            true ->
                Inner = maps:get({L+1, R-1}, DP, 0),
                (2 + Inner) rem M
        end,
    NewAcc = (Acc + Add) rem M,
    compute_char(C + 1, I, J, NextArray, PrevArray, M, DP, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false

  @spec count_palindromic_subsequences(s :: String.t()) :: integer
  def count_palindromic_subsequences(s) do
    mod = 1_000_000_007
    chars = for <<c <- s>>, do: c - ?a
    n = length(chars)

    s_arr = :array.from_list(chars)

    next_arr = build_next(s_arr, n, n)
    prev_arr = build_prev(s_arr, n, -1)

    dp =
      Enum.reduce(1..n, %{}, fn len, acc ->
        Enum.reduce(0..(n - len), acc, fn i, acc2 ->
          j = i + len - 1

          val =
            if len == 1 do
              1
            else
              ci = :array.get(i, s_arr)
              cj = :array.get(j, s_arr)

              if ci == cj do
                # low: first occurrence of ci after i
                low =
                  if i + 1 <= j do
                    elem(:array.get(i + 1, next_arr), ci)
                  else
                    n
                  end

                # high: last occurrence of ci before j
                high =
                  if i <= j - 1 do
                    elem(:array.get(j - 1, prev_arr), ci)
                  else
                    -1
                  end

                inner = get_dp(acc2, i + 1, j - 1)

                cond do
                  low > high ->
                    (2 * inner + 2) |> rem(mod)

                  low == high ->
                    (2 * inner + 1) |> rem(mod)

                  true ->
                    middle = get_dp(acc2, low + 1, high - 1)
                    ((2 * inner - middle) |> mod_fix(mod))
                end
              else
                a = get_dp(acc2, i + 1, j)
                b = get_dp(acc2, i, j - 1)
                cval = get_dp(acc2, i + 1, j - 1)
                ((a + b - cval) |> mod_fix(mod))
              end
            end

          Map.put(acc2, {i, j}, val)
        end)
      end)

    Map.get(dp, {0, n - 1})
  end

  defp get_dp(map, i, j) when i > j, do: 0
  defp get_dp(map, i, j), do: Map.get(map, {i, j}, 0)

  defp mod_fix(x, mod) do
    r = rem(x, mod)
    if r < 0, do: r + mod, else: r
  end

  defp build_next(s_arr, n, sentinel) do
    init_tuple = {sentinel, sentinel, sentinel, sentinel}
    arr = :array.new(n, default: init_tuple)

    next_seen = [sentinel, sentinel, sentinel, sentinel]

    {_final_arr, _} =
      Enum.reduce((n - 1)..0, {arr, next_seen}, fn i, {a, ns} ->
        c = :array.get(i, s_arr)
        ns2 = List.replace_at(ns, c, i)
        tuple = List.to_tuple(ns2)
        a2 = :array.set(i, tuple, a)
        {a2, ns2}
      end)

    elem({arr, next_seen}, 0)
  end

  defp build_prev(s_arr, n, sentinel) do
    init_tuple = {sentinel, sentinel, sentinel, sentinel}
    arr = :array.new(n, default: init_tuple)

    prev_seen = [sentinel, sentinel, sentinel, sentinel]

    {_final_arr, _} =
      Enum.reduce(0..(n - 1), {arr, prev_seen}, fn i, {a, ps} ->
        c = :array.get(i, s_arr)
        ps2 = List.replace_at(ps, c, i)
        tuple = List.to_tuple(ps2)
        a2 = :array.set(i, tuple, a)
        {a2, ps2}
      end)

    elem({arr, prev_seen}, 0)
  end
end
```
