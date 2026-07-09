# 3504. Longest Palindrome After Substring Concatenation II

## Cpp

```cpp
class Solution {
public:
    int longestPalindrome(string s, string t) {
        int n = s.size(), m = t.size();
        // palindrome tables
        vector<vector<char>> palS(n, vector<char>(n, 0));
        for (int i = n - 1; i >= 0; --i) {
            for (int j = i; j < n; ++j) {
                if (s[i] == s[j] && (j - i < 2 || palS[i + 1][j - 1]))
                    palS[i][j] = 1;
            }
        }
        vector<vector<char>> palT(m, vector<char>(m, 0));
        for (int i = m - 1; i >= 0; --i) {
            for (int j = i; j < m; ++j) {
                if (t[i] == t[j] && (j - i < 2 || palT[i + 1][j - 1]))
                    palT[i][j] = 1;
            }
        }
        // p[i]: longest palindrome starting at i in s
        vector<int> p(n, 0);
        for (int i = 0; i < n; ++i) {
            for (int r = n - 1; r >= i; --r) {
                if (palS[i][r]) { p[i] = r - i + 1; break; }
            }
        }
        // q[j]: longest palindrome ending at j in t
        vector<int> q(m, 0);
        for (int j = 0; j < m; ++j) {
            for (int l = 0; l <= j; ++l) {
                if (palT[l][j]) q[j] = max(q[j], j - l + 1);
            }
        }
        // dp[i][j]: longest palindrome using s[i...] as leftmost and t[...j] as rightmost
        vector<vector<int>> dp(n, vector<int>(m, 0));
        int ans = 0;
        for (int i = n - 1; i >= 0; --i) {
            for (int j = 0; j < m; ++j) {
                int best = max(p[i], q[j]);
                if (s[i] == t[j]) {
                    int inner = 0;
                    if (i + 1 < n && j - 1 >= 0) inner = dp[i + 1][j - 1];
                    best = max(best, 2 + inner);
                }
                dp[i][j] = best;
                ans = max(ans, best);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int longestPalindrome(String s, String t) {
        int n = s.length();
        int m = t.length();

        // Palindrome table for s
        boolean[][] palS = new boolean[n][n];
        for (int i = n - 1; i >= 0; --i) {
            for (int j = i; j < n; ++j) {
                if (s.charAt(i) == s.charAt(j) && (j - i < 2 || palS[i + 1][j - 1])) {
                    palS[i][j] = true;
                }
            }
        }

        // Palindrome table for t
        boolean[][] palT = new boolean[m][m];
        for (int i = m - 1; i >= 0; --i) {
            for (int j = i; j < m; ++j) {
                if (t.charAt(i) == t.charAt(j) && (j - i < 2 || palT[i + 1][j - 1])) {
                    palT[i][j] = true;
                }
            }
        }

        // p[i]: longest palindrome starting at i in s
        int[] p = new int[n];
        for (int i = 0; i < n; ++i) {
            int best = 0;
            for (int r = i; r < n; ++r) {
                if (palS[i][r]) {
                    best = Math.max(best, r - i + 1);
                }
            }
            p[i] = best;
        }

        // q[j]: longest palindrome ending at j in t
        int[] q = new int[m];
        for (int j = 0; j < m; ++j) {
            int best = 0;
            for (int l = 0; l <= j; ++l) {
                if (palT[l][j]) {
                    best = Math.max(best, j - l + 1);
                }
            }
            q[j] = best;
        }

        int[][] dp = new int[n][m];
        int ans = 0;

        for (int i = n - 1; i >= 0; --i) {
            for (int j = 0; j < m; ++j) {
                int val = Math.max(p[i], q[j]);
                if (s.charAt(i) == t.charAt(j)) {
                    int inner = 0;
                    if (i + 1 < n && j - 1 >= 0) {
                        inner = dp[i + 1][j - 1];
                    }
                    val = Math.max(val, 2 + inner);
                }
                dp[i][j] = val;
                ans = Math.max(ans, val);
            }
        }

        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def longestPalindrome(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n = len(s)
        m = len(t)

        # palindrome table for s
        pal_s = [[False] * n for _ in range(n)]
        p = [0] * n  # longest palindrome starting at i in s
        for i in range(n - 1, -1, -1):
            pal_s[i][i] = True
            max_len = 1
            for j in range(i + 1, n):
                if s[i] == s[j] and (j - i < 2 or pal_s[i + 1][j - 1]):
                    pal_s[i][j] = True
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
            p[i] = max_len

        # palindrome table for t
        pal_t = [[False] * m for _ in range(m)]
        q = [0] * m  # longest palindrome ending at j in t
        for i in range(m - 1, -1, -1):
            pal_t[i][i] = True
            max_len = 1
            for j in range(i + 1, m):
                if t[i] == t[j] and (j - i < 2 or pal_t[i + 1][j - 1]):
                    pal_t[i][j] = True
                    cur_len = j - i + 1
                    # update ending position j's max length
                    if cur_len > q[j]:
                        q[j] = cur_len
                # also keep track of max palindrome starting at i (not needed further)
            # ensure single character palindrome for start i contributes to some end
            if q[i] < 1:
                q[i] = 1

        # dp[i][j]: longest palindrome when using s[i...] as leftmost and t[...j] as rightmost
        dp = [[0] * m for _ in range(n)]
        ans = 1  # at least one character exists
        for i in range(n - 1, -1, -1):
            for j in range(m):
                best = p[i]
                if q[j] > best:
                    best = q[j]
                if s[i] == t[j]:
                    if i + 1 < n and j - 1 >= 0:
                        cand = 2 + dp[i + 1][j - 1]
                    else:
                        cand = 2
                    if cand > best:
                        best = cand
                dp[i][j] = best
                if best > ans:
                    ans = best

        return ans
```

## Python3

```python
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        n, m = len(s), len(t)

        # p[i]: longest palindrome substring in s that starts at i
        p = [0] * n
        pal_s = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or pal_s[i + 1][j - 1]):
                    pal_s[i][j] = True
                    length = j - i + 1
                    if length > p[i]:
                        p[i] = length

        # q[j]: longest palindrome substring in t that ends at j
        q = [0] * m
        pal_t = [[False] * m for _ in range(m)]
        for i in range(m):
            for j in range(i, m):
                if t[i] == t[j] and (j - i < 2 or pal_t[i + 1][j - 1]):
                    pal_t[i][j] = True
                    length = j - i + 1
                    if length > q[j]:
                        q[j] = length

        # dp[i][j]: longest palindrome using s[i...] as leftmost and t[...j] as rightmost
        dp = [[0] * m for _ in range(n)]
        ans = 0
        if p:
            ans = max(ans, max(p))
        if q:
            ans = max(ans, max(q))

        for i in range(n - 1, -1, -1):
            for j in range(m):
                if s[i] == t[j]:
                    inner = dp[i + 1][j - 1] if (i + 1 < n and j - 1 >= 0) else 0
                    val = max(p[i], q[j], 2 + inner)
                else:
                    val = max(p[i], q[j])
                dp[i][j] = val
                if val > ans:
                    ans = val

        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

int longestPalindrome(char* s, char* t) {
    int n = strlen(s);
    int m = strlen(t);

    // p[i]: longest palindrome starting at i in s
    int *p = (int*)calloc(n, sizeof(int));
    // q[j]: longest palindrome ending at j in t
    int *q = (int*)calloc(m, sizeof(int));

    // Process string s for p[]
    for (int center = 0; center < n; ++center) {
        // odd length palindromes
        int l = center, r = center;
        while (l >= 0 && r < n && s[l] == s[r]) {
            int len = r - l + 1;
            if (len > p[l]) p[l] = len;
            --l; ++r;
        }
        // even length palindromes
        l = center; r = center + 1;
        while (l >= 0 && r < n && s[l] == s[r]) {
            int len = r - l + 1;
            if (len > p[l]) p[l] = len;
            --l; ++r;
        }
    }

    // Process string t for q[]
    for (int center = 0; center < m; ++center) {
        // odd length
        int l = center, r = center;
        while (l >= 0 && r < m && t[l] == t[r]) {
            int len = r - l + 1;
            if (len > q[r]) q[r] = len;
            --l; ++r;
        }
        // even length
        l = center; r = center + 1;
        while (l >= 0 && r < m && t[l] == t[r]) {
            int len = r - l + 1;
            if (len > q[r]) q[r] = len;
            --l; ++r;
        }
    }

    // dp[i][j+1]: longest palindrome using s starting at i and t ending at j
    int **dp = (int**)malloc((n + 1) * sizeof(int*));
    for (int i = 0; i <= n; ++i) {
        dp[i] = (int*)calloc(m + 2, sizeof(int));
    }

    int ans = 0;
    // consider palindromes wholly inside s or t
    for (int i = 0; i < n; ++i) if (p[i] > ans) ans = p[i];
    for (int j = 0; j < m; ++j) if (q[j] > ans) ans = q[j];

    for (int i = n - 1; i >= 0; --i) {
        for (int j = 0; j < m; ++j) {
            int cur = p[i];
            if (q[j] > cur) cur = q[j];
            if (s[i] == t[j]) {
                int inner = dp[i + 1][j]; // corresponds to dp[i+1][j-1] in original indices
                int cand = 2 + inner;
                if (cand > cur) cur = cand;
            }
            dp[i][j + 1] = cur;
            if (cur > ans) ans = cur;
        }
    }

    // free memory
    for (int i = 0; i <= n; ++i) free(dp[i]);
    free(dp);
    free(p);
    free(q);

    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int LongestPalindrome(string s, string t) {
        int n = s.Length;
        int m = t.Length;

        // Palindromes in s
        bool[,] palS = new bool[n, n];
        for (int i = n - 1; i >= 0; --i) {
            for (int j = i; j < n; ++j) {
                if (s[i] == s[j] && (j - i < 2 || palS[i + 1, j - 1])) {
                    palS[i, j] = true;
                }
            }
        }

        int[] p = new int[n];
        int maxPalS = 0;
        for (int i = 0; i < n; ++i) {
            for (int r = n - 1; r >= i; --r) {
                if (palS[i, r]) {
                    int len = r - i + 1;
                    p[i] = len;
                    if (len > maxPalS) maxPalS = len;
                    break;
                }
            }
        }

        // Palindromes in t
        bool[,] palT = new bool[m, m];
        for (int i = m - 1; i >= 0; --i) {
            for (int j = i; j < m; ++j) {
                if (t[i] == t[j] && (j - i < 2 || palT[i + 1, j - 1])) {
                    palT[i, j] = true;
                }
            }
        }

        int[] q = new int[m];
        int maxPalT = 0;
        for (int j = 0; j < m; ++j) {
            int best = 0;
            for (int l = 0; l <= j; ++l) {
                if (palT[l, j]) {
                    int len = j - l + 1;
                    if (len > best) best = len;
                }
            }
            q[j] = best;
            if (best > maxPalT) maxPalT = best;
        }

        // DP combining substrings from s and t
        int[,] dp = new int[n + 1, m];
        int ans = Math.Max(maxPalS, maxPalT);

        for (int i = n - 1; i >= 0; --i) {
            for (int j = 0; j < m; ++j) {
                int val = p[i] > q[j] ? p[i] : q[j];
                if (s[i] == t[j]) {
                    int inner = 0;
                    if (i + 1 < n && j - 1 >= 0) inner = dp[i + 1, j - 1];
                    int cand = 2 + inner;
                    if (cand > val) val = cand;
                }
                dp[i, j] = val;
                if (val > ans) ans = val;
            }
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var longestPalindrome = function(s, t) {
    const n = s.length;
    const m = t.length;

    // p[i]: longest palindrome starting at i in s
    const p = new Array(n).fill(0);
    const palS = Array.from({ length: n }, () => new Array(n).fill(false));
    for (let i = n - 1; i >= 0; --i) {
        for (let j = i; j < n; ++j) {
            if (s[i] === s[j] && (j - i < 2 || palS[i + 1][j - 1])) {
                palS[i][j] = true;
                const len = j - i + 1;
                if (len > p[i]) p[i] = len;
            }
        }
    }

    // q[j]: longest palindrome ending at j in t
    const q = new Array(m).fill(0);
    const palT = Array.from({ length: m }, () => new Array(m).fill(false));
    for (let i = m - 1; i >= 0; --i) {
        for (let j = i; j < m; ++j) {
            if (t[i] === t[j] && (j - i < 2 || palT[i + 1][j - 1])) {
                palT[i][j] = true;
                const len = j - i + 1;
                if (len > q[j]) q[j] = len;
            }
        }
    }

    let ans = 0;
    for (let i = 0; i < n; ++i) ans = Math.max(ans, p[i]);
    for (let j = 0; j < m; ++j) ans = Math.max(ans, q[j]);

    // dp[i][j]: longest palindrome when using s[i] as leftmost and t[j] as rightmost
    const dp = Array.from({ length: n + 1 }, () => new Array(m).fill(0));

    for (let i = n - 1; i >= 0; --i) {
        for (let j = 0; j < m; ++j) {
            let best = Math.max(p[i], q[j]);
            if (s[i] === t[j]) {
                const inner = (i + 1 < n && j - 1 >= 0) ? dp[i + 1][j - 1] : 0;
                best = Math.max(best, 2 + inner);
            }
            dp[i][j] = best;
            if (best > ans) ans = best;
        }
    }

    return ans;
};
```

## Typescript

```typescript
function longestPalindrome(s: string, t: string): number {
    const n = s.length, m = t.length;

    // p[i]: longest palindrome substring in s that starts at i
    const p = new Array(n).fill(0);
    for (let c = 0; c < n; ++c) {
        // odd length
        let l = c, r = c;
        while (l >= 0 && r < n && s[l] === s[r]) {
            const len = r - l + 1;
            if (len > p[l]) p[l] = len;
            --l; ++r;
        }
        // even length
        l = c; r = c + 1;
        while (l >= 0 && r < n && s[l] === s[r]) {
            const len = r - l + 1;
            if (len > p[l]) p[l] = len;
            --l; ++r;
        }
    }

    // q[j]: longest palindrome substring in t that ends at j
    const q = new Array(m).fill(0);
    for (let c = 0; c < m; ++c) {
        // odd length
        let l = c, r = c;
        while (l >= 0 && r < m && t[l] === t[r]) {
            const len = r - l + 1;
            if (len > q[r]) q[r] = len;
            --l; ++r;
        }
        // even length
        l = c; r = c + 1;
        while (l >= 0 && r < m && t[l] === t[r]) {
            const len = r - l + 1;
            if (len > q[r]) q[r] = len;
            --l; ++r;
        }
    }

    // dp[i][j]: longest palindrome where leftmost char is s[i], rightmost char is t[j]
    const dp: number[][] = Array.from({ length: n }, () => new Array(m).fill(0));
    let ans = 0;

    for (let i = n - 1; i >= 0; --i) {
        for (let j = 0; j < m; ++j) {
            let best = p[i];
            if (q[j] > best) best = q[j];

            if (s[i] === t[j]) {
                const inner = (i + 1 < n && j - 1 >= 0) ? dp[i + 1][j - 1] : 0;
                const cand = 2 + inner;
                if (cand > best) best = cand;
            }

            dp[i][j] = best;
            if (best > ans) ans = best;
        }
    }

    // Ensure single-side palindromes are considered
    for (let i = 0; i < n; ++i) if (p[i] > ans) ans = p[i];
    for (let j = 0; j < m; ++j) if (q[j] > ans) ans = q[j];

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @return Integer
     */
    function longestPalindrome($s, $t) {
        $n = strlen($s);
        $m = strlen($t);

        // Palindrome table for s
        $isPalS = array_fill(0, $n, array_fill(0, $n, false));
        for ($i = $n - 1; $i >= 0; --$i) {
            $isPalS[$i][$i] = true;
            for ($j = $i + 1; $j < $n; ++$j) {
                if ($s[$i] === $s[$j]) {
                    if ($j - $i == 1 || $isPalS[$i + 1][$j - 1]) {
                        $isPalS[$i][$j] = true;
                    }
                }
            }
        }

        // p[i]: longest palindrome starting at i in s
        $p = array_fill(0, $n, 0);
        for ($i = $n - 1; $i >= 0; --$i) {
            $maxLen = 1;
            for ($j = $n - 1; $j >= $i; --$j) {
                if ($isPalS[$i][$j]) {
                    $len = $j - $i + 1;
                    if ($len > $maxLen) $maxLen = $len;
                }
            }
            $p[$i] = $maxLen;
        }

        // Palindrome table for t
        $isPalT = array_fill(0, $m, array_fill(0, $m, false));
        for ($i = $m - 1; $i >= 0; --$i) {
            $isPalT[$i][$i] = true;
            for ($j = $i + 1; $j < $m; ++$j) {
                if ($t[$i] === $t[$j]) {
                    if ($j - $i == 1 || $isPalT[$i + 1][$j - 1]) {
                        $isPalT[$i][$j] = true;
                    }
                }
            }
        }

        // q[j]: longest palindrome ending at j in t
        $q = array_fill(0, $m, 0);
        for ($j = 0; $j < $m; ++$j) {
            $maxLen = 1;
            for ($i = $j; $i >= 0; --$i) {
                if ($isPalT[$i][$j]) {
                    $len = $j - $i + 1;
                    if ($len > $maxLen) $maxLen = $len;
                }
            }
            $q[$j] = $maxLen;
        }

        // DP for combined substrings
        $dp = array_fill(0, $n, array_fill(0, $m, 0));
        $ans = 1; // at least one character

        for ($i = $n - 1; $i >= 0; --$i) {
            for ($j = 0; $j < $m; ++$j) {
                $best = max($p[$i], $q[$j]);
                if ($s[$i] === $t[$j]) {
                    $inner = 0;
                    if ($i + 1 < $n && $j - 1 >= 0) {
                        $inner = $dp[$i + 1][$j - 1];
                    }
                    $candidate = 2 + $inner;
                    if ($candidate > $best) $best = $candidate;
                }
                $dp[$i][$j] = $best;
                if ($best > $ans) $ans = $best;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func longestPalindrome(_ s: String, _ t: String) -> Int {
        let sArr = Array(s)
        let tArr = Array(t)
        let n = sArr.count
        let m = tArr.count
        
        // Preprocess longest palindrome starting at each index in s
        var isPalS = Array(repeating: Array(repeating: false, count: n), count: n)
        var startLen = Array(repeating: 1, count: n)   // at least single char
        if n > 0 {
            for i in stride(from: n - 1, through: 0, by: -1) {
                for j in i..<n {
                    if sArr[i] == sArr[j] && (j - i < 2 || isPalS[i + 1][j - 1]) {
                        isPalS[i][j] = true
                        let len = j - i + 1
                        if len > startLen[i] { startLen[i] = len }
                    }
                }
            }
        }
        
        // Preprocess longest palindrome ending at each index in t
        var isPalT = Array(repeating: Array(repeating: false, count: m), count: m)
        var endLen = Array(repeating: 1, count: m)   // at least single char
        if m > 0 {
            for i in stride(from: m - 1, through: 0, by: -1) {
                for j in i..<m {
                    if tArr[i] == tArr[j] && (j - i < 2 || isPalT[i + 1][j - 1]) {
                        isPalT[i][j] = true
                    }
                }
            }
            for j in 0..<m {
                var best = 1
                for i in 0...j {
                    if isPalT[i][j] {
                        let len = j - i + 1
                        if len > best { best = len }
                    }
                }
                endLen[j] = best
            }
        }
        
        // DP over starting index in s and ending index in t
        var dp = Array(repeating: Array(repeating: 0, count: m), count: n)
        var answer = 1   // at least one character palindrome exists
        
        if n > 0 && m > 0 {
            for i in stride(from: n - 1, through: 0, by: -1) {
                for j in 0..<m {
                    var best = max(startLen[i], endLen[j])
                    if sArr[i] == tArr[j] {
                        let inner = (i + 1 < n && j > 0) ? dp[i + 1][j - 1] : 0
                        best = max(best, 2 + inner)
                    }
                    dp[i][j] = best
                    if best > answer { answer = best }
                }
            }
        } else {
            // If one string is empty, answer is the longest palindrome within the other
            if n == 0 && m > 0 {
                answer = endLen.max() ?? 0
            } else if m == 0 && n > 0 {
                answer = startLen.max() ?? 0
            }
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestPalindrome(s: String, t: String): Int {
        val n = s.length
        val m = t.length
        // Palindrome table for s
        val palS = Array(n) { BooleanArray(n) }
        for (i in n - 1 downTo 0) {
            for (j in i until n) {
                if (s[i] == s[j] && (j - i < 2 || palS[i + 1][j - 1])) {
                    palS[i][j] = true
                }
            }
        }
        // Palindrome table for t
        val palT = Array(m) { BooleanArray(m) }
        for (i in m - 1 downTo 0) {
            for (j in i until m) {
                if (t[i] == t[j] && (j - i < 2 || palT[i + 1][j - 1])) {
                    palT[i][j] = true
                }
            }
        }
        // p[i]: longest palindrome starting at i in s
        val p = IntArray(n)
        for (i in 0 until n) {
            var best = 0
            for (r in i until n) {
                if (palS[i][r]) {
                    best = maxOf(best, r - i + 1)
                }
            }
            p[i] = best
        }
        // q[j]: longest palindrome ending at j in t
        val q = IntArray(m)
        for (j in 0 until m) {
            var best = 0
            for (l in 0..j) {
                if (palT[l][j]) {
                    best = maxOf(best, j - l + 1)
                }
            }
            q[j] = best
        }
        // dp[i][j]: longest palindrome using s[i] as first char and t[j] as last char
        val dp = Array(n) { IntArray(m) }
        var answer = 1 // at least one character exists
        for (i in n - 1 downTo 0) {
            for (j in 0 until m) {
                var best = maxOf(p[i], q[j])
                if (s[i] == t[j]) {
                    val inner = if (i + 1 < n && j - 1 >= 0) dp[i + 1][j - 1] else 0
                    best = maxOf(best, 2 + inner)
                }
                dp[i][j] = best
                answer = maxOf(answer, best)
            }
        }
        return answer
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int longestPalindrome(String s, String t) {
    int ns = s.length;
    int nt = t.length;

    // Palindrome tables for s and t
    List<List<bool>> palS = List.generate(ns, (_) => List.filled(ns, false));
    for (int i = 0; i < ns; ++i) palS[i][i] = true;
    for (int len = 2; len <= ns; ++len) {
      for (int i = 0; i + len - 1 < ns; ++i) {
        int j = i + len - 1;
        if (s[i] == s[j]) {
          if (len == 2 || palS[i + 1][j - 1]) {
            palS[i][j] = true;
          }
        }
      }
    }

    List<List<bool>> palT = List.generate(nt, (_) => List.filled(nt, false));
    for (int i = 0; i < nt; ++i) palT[i][i] = true;
    for (int len = 2; len <= nt; ++len) {
      for (int i = 0; i + len - 1 < nt; ++i) {
        int j = i + len - 1;
        if (t[i] == t[j]) {
          if (len == 2 || palT[i + 1][j - 1]) {
            palT[i][j] = true;
          }
        }
      }
    }

    // p[i]: longest palindrome starting at i in s
    List<int> p = List.filled(ns, 0);
    for (int i = 0; i < ns; ++i) {
      int best = 0;
      for (int j = ns - 1; j >= i; --j) {
        if (palS[i][j]) {
          best = max(best, j - i + 1);
        }
      }
      p[i] = best;
    }

    // q[j]: longest palindrome ending at j in t
    List<int> q = List.filled(nt, 0);
    for (int j = 0; j < nt; ++j) {
      int best = 0;
      for (int i = 0; i <= j; ++i) {
        if (palT[i][j]) {
          best = max(best, j - i + 1);
        }
      }
      q[j] = best;
    }

    // DP combining substrings from s and t
    List<List<int>> dp = List.generate(ns, (_) => List.filled(nt, 0));
    int ans = 0;

    for (int i = ns - 1; i >= 0; --i) {
      for (int j = 0; j < nt; ++j) {
        if (s[i] == t[j]) {
          int inner = 0;
          if (i + 1 < ns && j - 1 >= 0) inner = dp[i + 1][j - 1];
          int cand = 2 + inner;
          dp[i][j] = max(cand, max(p[i], q[j]));
        } else {
          dp[i][j] = max(p[i], q[j]);
        }
        ans = max(ans, dp[i][j]);
      }
    }

    return ans;
  }
}
```

## Golang

```go
func longestPalindrome(s string, t string) int {
    n := len(s)
    m := len(t)

    // Preprocess longest palindrome starting at each index in s
    p := make([]int, n)
    if n > 0 {
        palS := make([][]bool, n)
        for i := 0; i < n; i++ {
            palS[i] = make([]bool, n)
        }
        for i := 0; i < n; i++ {
            palS[i][i] = true
            p[i] = 1
        }
        for length := 2; length <= n; length++ {
            for i := 0; i+length-1 < n; i++ {
                j := i + length - 1
                if s[i] == s[j] && (length == 2 || palS[i+1][j-1]) {
                    palS[i][j] = true
                    if length > p[i] {
                        p[i] = length
                    }
                }
            }
        }
    }

    // Preprocess longest palindrome ending at each index in t
    q := make([]int, m)
    if m > 0 {
        palT := make([][]bool, m)
        for i := 0; i < m; i++ {
            palT[i] = make([]bool, m)
        }
        for i := 0; i < m; i++ {
            palT[i][i] = true
            q[i] = 1
        }
        for length := 2; length <= m; length++ {
            for l := 0; l+length-1 < m; l++ {
                r := l + length - 1
                if t[l] == t[r] && (length == 2 || palT[l+1][r-1]) {
                    palT[l][r] = true
                    if length > q[r] {
                        q[r] = length
                    }
                }
            }
        }
    }

    ans := 0
    for _, v := range p {
        if v > ans {
            ans = v
        }
    }
    for _, v := range q {
        if v > ans {
            ans = v
        }
    }

    // DP for mixed substrings
    dp := make([][]int, n)
    for i := 0; i < n; i++ {
        dp[i] = make([]int, m)
    }

    for i := n - 1; i >= 0; i-- {
        for j := 0; j < m; j++ {
            best := p[i]
            if q[j] > best {
                best = q[j]
            }
            if s[i] == t[j] {
                inner := 0
                if i+1 < n && j-1 >= 0 {
                    inner = dp[i+1][j-1]
                }
                cand := 2 + inner
                if cand > best {
                    best = cand
                }
            }
            dp[i][j] = best
            if best > ans {
                ans = best
            }
        }
    }

    return ans
}
```

## Ruby

```ruby
def longest_palindrome(s, t)
  n = s.length
  m = t.length

  # p[i]: longest palindrome starting at i in s
  p = Array.new(n, 0)
  (0...n).each do |c|
    l = c
    r = c
    while l >= 0 && r < n && s[l] == s[r]
      len = r - l + 1
      p[l] = len if len > p[l]
      l -= 1
      r += 1
    end
  end
  (0...n-1).each do |c|
    l = c
    r = c + 1
    while l >= 0 && r < n && s[l] == s[r]
      len = r - l + 1
      p[l] = len if len > p[l]
      l -= 1
      r += 1
    end
  end

  # q[j]: longest palindrome ending at j in t
  q = Array.new(m, 0)
  (0...m).each do |c|
    l = c
    r = c
    while l >= 0 && r < m && t[l] == t[r]
      len = r - l + 1
      q[r] = len if len > q[r]
      l -= 1
      r += 1
    end
  end
  (0...m-1).each do |c|
    l = c
    r = c + 1
    while l >= 0 && r < m && t[l] == t[r]
      len = r - l + 1
      q[r] = len if len > q[r]
      l -= 1
      r += 1
    end
  end

  # dp[i][j]: longest palindrome when starting with s[i] and ending with t[j]
  dp = Array.new(n) { Array.new(m, 0) }
  ans = 1
  p.each { |v| ans = v if v > ans }
  q.each { |v| ans = v if v > ans }

  (n-1).downto(0) do |i|
    (0...m).each do |j|
      if s[i] == t[j]
        val = 2
        if i + 1 < n && j - 1 >= 0
          val += dp[i + 1][j - 1]
        end
        cur = [p[i], q[j], val].max
      else
        cur = [p[i], q[j]].max
      end
      dp[i][j] = cur
      ans = cur if cur > ans
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def longestPalindrome(s: String, t: String): Int = {
        val n = s.length
        val m = t.length

        // p[i]: longest palindrome starting at i in s
        val p = Array.fill[Int](n)(0)
        for (center <- 0 until n) {
            var l = center
            var r = center
            while (l >= 0 && r < n && s.charAt(l) == s.charAt(r)) {
                val len = r - l + 1
                if (len > p(l)) p(l) = len
                l -= 1
                r += 1
            }
            l = center
            r = center + 1
            while (l >= 0 && r < n && s.charAt(l) == s.charAt(r)) {
                val len = r - l + 1
                if (len > p(l)) p(l) = len
                l -= 1
                r += 1
            }
        }

        // q[j]: longest palindrome ending at j in t
        val q = Array.fill[Int](m)(0)
        for (center <- 0 until m) {
            var l = center
            var r = center
            while (l >= 0 && r < m && t.charAt(l) == t.charAt(r)) {
                val len = r - l + 1
                if (len > q(r)) q(r) = len
                l -= 1
                r += 1
            }
            l = center
            r = center + 1
            while (l >= 0 && r < m && t.charAt(l) == t.charAt(r)) {
                val len = r - l + 1
                if (len > q(r)) q(r) = len
                l -= 1
                r += 1
            }
        }

        var ans = 0
        for (i <- 0 until n) if (p(i) > ans) ans = p(i)
        for (j <- 0 until m) if (q(j) > ans) ans = q(j)

        val dp = Array.ofDim[Int](n, m)
        for (i <- (n - 1) to 0 by -1) {
            for (j <- 0 until m) {
                var best = math.max(p(i), q(j))
                if (s.charAt(i) == t.charAt(j)) {
                    val inner = if (i + 1 < n && j - 1 >= 0) dp(i + 1)(j - 1) else 0
                    val cand = 2 + inner
                    if (cand > best) best = cand
                }
                dp(i)(j) = best
                if (best > ans) ans = best
            }
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_palindrome(s: String, t: String) -> i32 {
        let s_bytes = s.as_bytes();
        let t_bytes = t.as_bytes();
        let n = s_bytes.len();
        let m = t_bytes.len();

        // p[i]: longest palindrome starting at i in s
        let mut p = vec![0usize; n];
        if n > 0 {
            let mut dp_s = vec![vec![false; n]; n];
            for i in (0..n).rev() {
                for j in i..n {
                    if s_bytes[i] == s_bytes[j]
                        && (j - i < 2 || dp_s[i + 1][j - 1])
                    {
                        dp_s[i][j] = true;
                        let len = j - i + 1;
                        if p[i] < len {
                            p[i] = len;
                        }
                    }
                }
            }
        }

        // q[j]: longest palindrome ending at j in t
        let mut q = vec![0usize; m];
        if m > 0 {
            let mut dp_t = vec![vec![false; m]; m];
            for i in (0..m).rev() {
                for j in i..m {
                    if t_bytes[i] == t_bytes[j]
                        && (j - i < 2 || dp_t[i + 1][j - 1])
                    {
                        dp_t[i][j] = true;
                        let len = j - i + 1;
                        if q[j] < len {
                            q[j] = len;
                        }
                    }
                }
            }
        }

        // DP over starting index in s and ending index in t
        let mut dp = vec![vec![0usize; m]; n];
        let mut ans = 0usize;

        for i in (0..n).rev() {
            for j in 0..m {
                let mut best = std::cmp::max(p[i], q[j]);
                if s_bytes[i] == t_bytes[j] {
                    let inner = if i + 1 < n && j >= 1 { dp[i + 1][j - 1] } else { 0 };
                    best = std::cmp::max(best, 2 + inner);
                }
                dp[i][j] = best;
                if ans < best {
                    ans = best;
                }
            }
        }

        // Also consider palindromes that lie completely inside one string
        for &len in &p {
            if ans < len { ans = len; }
        }
        for &len in &q {
            if ans < len { ans = len; }
        }

        ans as i32
    }
}
```

## Racket

```racket
(define/contract (longest-palindrome s t)
  (-> string? string? exact-integer?)
  (let* ((n (string-length s))
         (m (string-length t))
         (p (make-vector n 0))
         (q (make-vector m 0))
         ;; palindrome tables for s and t
         (palS (make-vector n))
         (palT (make-vector m)))
    ;; initialise inner vectors
    (for ([i n]) (vector-set! palS i (make-vector n #f)))
    (for ([j m]) (vector-set! palT j (make-vector m #f)))
    ;; fill palindrome table for s
    (for ([len (in-range 1 (+ n 1))])
      (for ([i (in-range 0 (+ 1 (- n len)))])
        (let ((j (+ i len -1)))
          (if (= i j)
              (vector-set! (vector-ref palS i) j #t)
              (when (and (char=? (string-ref s i) (string-ref s j))
                         (or (< (- j i) 2)
                             (vector-ref (vector-ref palS (+ i 1)) (- j 1))))
                (vector-set! (vector-ref palS i) j #t))))))
    ;; compute p[i]: longest palindrome starting at i in s
    (for ([i n])
      (let ((maxlen 0))
        (for ([j (in-range i n)])
          (when (vector-ref (vector-ref palS i) j)
            (set! maxlen (max maxlen (+ 1 (- j i))))))
        (vector-set! p i maxlen)))
    ;; fill palindrome table for t
    (for ([len (in-range 1 (+ m 1))])
      (for ([i (in-range 0 (+ 1 (- m len)))])
        (let ((j (+ i len -1)))
          (if (= i j)
              (vector-set! (vector-ref palT i) j #t)
              (when (and (char=? (string-ref t i) (string-ref t j))
                         (or (< (- j i) 2)
                             (vector-ref (vector-ref palT (+ i 1)) (- j 1))))
                (vector-set! (vector-ref palT i) j #t))))))
    ;; compute q[j]: longest palindrome ending at j in t
    (for ([j m])
      (let ((maxlen 0))
        (for ([i (in-range 0 (+ j 1))])
          (when (vector-ref (vector-ref palT i) j)
            (set! maxlen (max maxlen (+ 1 (- j i))))))
        (vector-set! q j maxlen)))
    ;; initial answer from single‑string palindromes
    (let ((ans 0))
      (for ([i n]) (set! ans (max ans (vector-ref p i))))
      (for ([j m]) (set! ans (max ans (vector-ref q j))))
      ;; dp[i][j] table
      (define dp (make-vector n))
      (for ([i n]) (vector-set! dp i (make-vector m 0)))
      (for ([i (in-range (sub1 n) -1 -1)])   ; from n-1 down to 0
        (for ([j (in-range m)])
          (let* ((si (string-ref s i))
                 (tj (string-ref t j))
                 (pi (vector-ref p i))
                 (qj (vector-ref q j))
                 (val (if (char=? si tj)
                          (let ((inner (if (and (< i (sub1 n)) (> j 0))
                                           (vector-ref (vector-ref dp (+ i 1)) (- j 1))
                                           0)))
                            (max pi qj (+ 2 inner)))
                          (max pi qj))))
            (vector-set! (vector-ref dp i) j val)
            (set! ans (max ans val)))))
      ans)))
```

## Erlang

```erlang
-spec longest_palindrome(S :: unicode:unicode_binary(), T :: unicode:unicode_binary()) -> integer().
longest_palindrome(S, T) ->
    SList = binary:bin_to_list(S),
    TList = binary:bin_to_list(T),
    SArr = list_to_tuple(SList),
    TArr = list_to_tuple(TList),
    N = tuple_size(SArr),
    M = tuple_size(TArr),

    % longest palindrome starting at each position in S
    P0 = erlang:make_tuple(N, 0),
    P = compute_start_pal(SArr, N, P0),

    % longest palindrome ending at each position in T
    Q0 = erlang:make_tuple(M, 0),
    Q = compute_end_pal(TArr, M, Q0),

    % initial answer from single-side palindromes
    InitAns1 = max_in_tuple(P, N),
    InitAns2 = max_in_tuple(Q, M),
    InitAns = if InitAns1 > InitAns2 -> InitAns1; true -> InitAns2 end,

    % DP over i descending and j ascending
    FinalAns = dp_compute(N, M, SArr, TArr, P, Q, InitAns),

    FinalAns.

%% compute longest palindrome starting at each index of S
compute_start_pal(_SArr, 0, P) -> P;
compute_start_pal(SArr, N, P) ->
    compute_center(0, SArr, N, P).

compute_center(I, _SArr, N, P) when I >= N -> P;
compute_center(I, SArr, N, P) ->
    P1 = expand_odd(I, I, SArr, N, P),
    P2 = expand_even(I, I + 1, SArr, N, P1),
    compute_center(I + 1, SArr, N, P2).

expand_odd(L, R, SArr, N, P) ->
    case (L >= 0 andalso R < N andalso element(L + 1, SArr) =:= element(R + 1, SArr)) of
        true ->
            Len = R - L + 1,
            Cur = element(L + 1, P),
            NewP = if Len > Cur -> setelement(L + 1, P, Len); true -> P end,
            expand_odd(L - 1, R + 1, SArr, N, NewP);
        false -> P
    end.

expand_even(L, R, _SArr, N, P) when L >= N; R >= N -> P;
expand_even(L, R, SArr, N, P) ->
    case (L >= 0 andalso R < N andalso element(L + 1, SArr) =:= element(R + 1, SArr)) of
        true ->
            Len = R - L + 1,
            Cur = element(L + 1, P),
            NewP = if Len > Cur -> setelement(L + 1, P, Len); true -> P end,
            expand_even(L - 1, R + 1, SArr, N, NewP);
        false -> P
    end.

%% compute longest palindrome ending at each index of T
compute_end_pal(_TArr, 0, Q) -> Q;
compute_end_pal(TArr, M, Q) ->
    compute_center_t(0, TArr, M, Q).

compute_center_t(I, _TArr, M, Q) when I >= M -> Q;
compute_center_t(I, TArr, M, Q) ->
    Q1 = expand_odd_t(I, I, TArr, M, Q),
    Q2 = expand_even_t(I, I + 1, TArr, M, Q1),
    compute_center_t(I + 1, TArr, M, Q2).

expand_odd_t(L, R, TArr, M, Q) ->
    case (L >= 0 andalso R < M andalso element(L + 1, TArr) =:= element(R + 1, TArr)) of
        true ->
            Len = R - L + 1,
            Cur = element(R + 1, Q),
            NewQ = if Len > Cur -> setelement(R + 1, Q, Len); true -> Q end,
            expand_odd_t(L - 1, R + 1, TArr, M, NewQ);
        false -> Q
    end.

expand_even_t(L, R, _TArr, M, Q) when L >= M; R >= M -> Q;
expand_even_t(L, R, TArr, M, Q) ->
    case (L >= 0 andalso R < M andalso element(L + 1, TArr) =:= element(R + 1, TArr)) of
        true ->
            Len = R - L + 1,
            Cur = element(R + 1, Q),
            NewQ = if Len > Cur -> setelement(R + 1, Q, Len); true -> Q end,
            expand_even_t(L - 1, R + 1, TArr, M, NewQ);
        false -> Q
    end.

%% maximum value inside a tuple (size N)
max_in_tuple(Tup, Size) ->
    max_in_tuple(0, 1, Size, Tup).

max_in_tuple(Max, I, Size, _Tup) when I > Size -> Max;
max_in_tuple(Max, I, Size, Tup) ->
    Val = element(I, Tup),
    NewMax = if Val > Max -> Val; true -> Max end,
    max_in_tuple(NewMax, I + 1, Size, Tup).

%% DP computation
dp_compute(N, M, SArr, TArr, P, Q, InitAns) ->
    dp_loop(N - 1, erlang:make_tuple(M, 0), N, M, SArr, TArr, P, Q, InitAns).

dp_loop(-1, _PrevRow, _N, _M, _SArr, _TArr, _P, _Q, Ans) -> Ans;
dp_loop(I, PrevRow, N, M, SArr, TArr, P, Q, Ans) ->
    {CurrRow, RowMax} = build_row(0, I, PrevRow, N, M, SArr, TArr, P, Q, erlang:make_tuple(M, 0), 0),
    NewAns = if RowMax > Ans -> RowMax; true -> Ans end,
    dp_loop(I - 1, CurrRow, N, M, SArr, TArr, P, Q, NewAns).

build_row(J, _I, _PrevRow, _N, M, _SArr, _TArr, _P, _Q, RowAcc, MaxSoFar) when J >= M ->
    {RowAcc, MaxSoFar};
build_row(J, I, PrevRow, N, M, SArr, TArr, P, Q, RowAcc, MaxSoFar) ->
    Pi = element(I + 1, P),
    Qj = element(J + 1, Q),
    MaxPQ = if Pi > Qj -> Pi; true -> Qj end,
    Val =
        case element(I + 1, SArr) =:= element(J + 1, TArr) of
            true ->
                Inner = 
                    if (I + 1 < N) andalso (J - 1 >= 0) ->
                        element((J - 1) + 1, PrevRow);
                       true -> 0
                    end,
                Ext = 2 + Inner,
                if Ext > MaxPQ -> Ext; true -> MaxPQ end;
            false -> MaxPQ
        end,
    NewRowAcc = setelement(J + 1, RowAcc, Val),
    NewMax = if Val > MaxSoFar -> Val; true -> MaxSoFar end,
    build_row(J + 1, I, PrevRow, N, M, SArr, TArr, P, Q, NewRowAcc, NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_palindrome(s :: String.t(), t :: String.t()) :: integer
  def longest_palindrome(s, t) do
    s_arr = :array.from_list(String.to_charlist(s))
    t_arr = :array.from_list(String.to_charlist(t))

    n = String.length(s)
    m = String.length(t)

    {p, max_s} = compute_start(s_arr, n)
    {q, max_t} = compute_end(t_arr, m)

    init_best = if max_s > max_t, do: max_s, else: max_t

    # DP over i (s) descending and j (t) ascending
    {_final_best, _} =
      Enum.reduce(Enum.reverse(0..(n - 1)), {init_best, Tuple.duplicate(0, m)}, fn i,
                                                                               {best, prev_row} ->
        p_i = elem(p, i)

        cur_list =
          Enum.map(0..(m - 1), fn j ->
            q_j = elem(q, j)
            base = if p_i > q_j, do: p_i, else: q_j

            if :array.get(i, s_arr) == :array.get(j, t_arr) do
              inner =
                if i + 1 < n and j - 1 >= 0,
                  do: elem(prev_row, j - 1),
                  else: 0

              cand = 2 + inner
              if cand > base, do: cand, else: base
            else
              base
            end
          end)

        cur_tuple = List.to_tuple(cur_list)
        new_best = Enum.max([best | cur_list])
        {new_best, cur_tuple}
      end)

    # The reduce returns the final best as first element of tuple
    elem({_final_best, _}, 0)
  end

  defp compute_start(arr, n) do
    p = Tuple.duplicate(0, n)

    p =
      Enum.reduce(0..(n - 1), p, fn center, acc ->
        acc = expand_start(acc, center, center, n, arr)

        if center + 1 < n,
          do: expand_start(acc, center, center + 1, n, arr),
          else: acc
      end)

    {p, Enum.max(Tuple.to_list(p))}
  end

  defp compute_end(arr, n) do
    q = Tuple.duplicate(0, n)

    q =
      Enum.reduce(0..(n - 1), q, fn center, acc ->
        acc = expand_end(acc, center, center, n, arr)

        if center + 1 < n,
          do: expand_end(acc, center, center + 1, n, arr),
          else: acc
      end)

    {q, Enum.max(Tuple.to_list(q))}
  end

  defp expand_start(p, l, r, n, arr) when l >= 0 and r < n do
    if :array.get(l, arr) == :array.get(r, arr) do
      len = r - l + 1
      cur = elem(p, l)

      p2 =
        if len > cur,
          do: put_elem(p, l, len),
          else: p

      expand_start(p2, l - 1, r + 1, n, arr)
    else
      p
    end
  end

  defp expand_start(p, _l, _r, _n, _arr), do: p

  defp expand_end(q, l, r, n, arr) when l >= 0 and r < n do
    if :array.get(l, arr) == :array.get(r, arr) do
      len = r - l + 1
      cur = elem(q, r)

      q2 =
        if len > cur,
          do: put_elem(q, r, len),
          else: q

      expand_end(q2, l - 1, r + 1, n, arr)
    else
      q
    end
  end

  defp expand_end(q, _l, _r, _n, _arr), do: q
end
```
