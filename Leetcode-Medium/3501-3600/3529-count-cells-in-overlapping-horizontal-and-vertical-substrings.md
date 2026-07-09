# 3529. Count Cells in Overlapping Horizontal and Vertical Substrings

## Cpp

```cpp
class Solution {
public:
    using ull = unsigned long long;
    
    vector<int> getMatches(const string& text, const string& pat, const vector<ull>& powBase) {
        int n = text.size();
        int m = pat.size();
        if (m > n) return {};
        const ull base = 91138233ULL;
        // prefix hashes
        vector<ull> pref(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            pref[i + 1] = pref[i] * base + (ull)(text[i]);
        }
        // pattern hash
        ull patHash = 0;
        for (char c : pat) patHash = patHash * base + (ull)c;
        
        vector<int> starts;
        for (int i = m; i <= n; ++i) {
            int l = i - m;
            ull cur = pref[i] - pref[l] * powBase[m];
            if (cur == patHash) starts.push_back(l);
        }
        return starts;
    }
    
    int countCells(vector<vector<char>>& grid, string pattern) {
        int mRows = grid.size();
        int nCols = grid[0].size();
        long long N = 1LL * mRows * nCols;
        int L = pattern.size();
        
        // Build row-major string S
        string S;
        S.reserve(N);
        for (int i = 0; i < mRows; ++i)
            for (int j = 0; j < nCols; ++j)
                S.push_back(grid[i][j]);
        // Build column-major string T
        string T;
        T.reserve(N);
        for (int j = 0; j < nCols; ++j)
            for (int i = 0; i < mRows; ++i)
                T.push_back(grid[i][j]);
        
        // Precompute powers up to max(N, L)
        int maxLen = (int)N;
        const ull base = 91138233ULL;
        vector<ull> powBase(maxLen + 1);
        powBase[0] = 1;
        for (int i = 1; i <= maxLen; ++i) powBase[i] = powBase[i - 1] * base;
        
        // Find matches
        vector<int> horizStarts = getMatches(S, pattern, powBase);
        vector<int> vertStarts = getMatches(T, pattern, powBase);
        
        // Difference arrays for coverage
        vector<int> diffH(N + 1, 0), diffV(N + 1, 0);
        for (int s : horizStarts) {
            diffH[s] += 1;
            diffH[s + L] -= 1;
        }
        for (int s : vertStarts) {
            diffV[s] += 1;
            diffV[s + L] -= 1;
        }
        
        // Prefix sums to get boolean coverage
        vector<char> coverH(N, 0), coverV(N, 0);
        int cur = 0;
        for (long long i = 0; i < N; ++i) {
            cur += diffH[i];
            if (cur > 0) coverH[i] = 1;
        }
        cur = 0;
        for (long long i = 0; i < N; ++i) {
            cur += diffV[i];
            if (cur > 0) coverV[i] = 1;
        }
        
        // Count cells covered by both
        int ans = 0;
        for (int i = 0; i < mRows; ++i) {
            for (int j = 0; j < nCols; ++j) {
                long long idxH = 1LL * i * nCols + j;
                long long idxV = 1LL * j * mRows + i;
                if (coverH[idxH] && coverV[idxV]) ++ans;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    private static final long MOD1 = 1_000_000_007L;
    private static final long MOD2 = 1_000_000_009L;
    private static final long BASE = 91138233L;

    public int countCells(char[][] grid, String pattern) {
        int m = grid.length;
        int n = grid[0].length;
        int total = m * n;
        int L = pattern.length();
        if (L > total) return 0;

        // Build row-major and column-major character arrays
        char[] rowStr = new char[total];
        char[] colStr = new char[total];
        int idx = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                rowStr[idx++] = grid[i][j];
            }
        }
        idx = 0;
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < m; i++) {
                colStr[idx++] = grid[i][j];
            }
        }

        // Precompute powers
        long[] pow1 = new long[L + 1];
        long[] pow2 = new long[L + 1];
        pow1[0] = 1;
        pow2[0] = 1;
        for (int i = 1; i <= L; i++) {
            pow1[i] = (pow1[i - 1] * BASE) % MOD1;
            pow2[i] = (pow2[i - 1] * BASE) % MOD2;
        }

        // Pattern hash
        long patHash1 = 0, patHash2 = 0;
        for (int i = 0; i < L; i++) {
            int v = pattern.charAt(i);
            patHash1 = (patHash1 * BASE + v) % MOD1;
            patHash2 = (patHash2 * BASE + v) % MOD2;
        }

        // Difference arrays for coverage
        int[] diffH = new int[total + 1];
        int[] diffV = new int[total + 1];

        // Process horizontal (row-major)
        process(text(rowStr), total, L, pow1, pow2, patHash1, patHash2, diffH);

        // Process vertical (column-major)
        process(text(colStr), total, L, pow1, pow2, patHash1, patHash2, diffV);

        // Prefix sums to get coverage counts
        int[] coverH = new int[total];
        int cur = 0;
        for (int i = 0; i < total; i++) {
            cur += diffH[i];
            coverH[i] = cur;
        }
        int[] coverV = new int[total];
        cur = 0;
        for (int i = 0; i < total; i++) {
            cur += diffV[i];
            coverV[i] = cur;
        }

        // Count cells that are covered by both
        int result = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int idxR = i * n + j;      // row-major index
                int idxC = j * m + i;      // column-major index
                if (coverH[idxR] > 0 && coverV[idxC] > 0) {
                    result++;
                }
            }
        }
        return result;
    }

    private void process(char[] text, int total, int L,
                         long[] pow1, long[] pow2,
                         long patHash1, long patHash2,
                         int[] diff) {
        if (L > total) return;
        long[] pre1 = new long[total + 1];
        long[] pre2 = new long[total + 1];
        for (int i = 0; i < total; i++) {
            int v = text[i];
            pre1[i + 1] = (pre1[i] * BASE + v) % MOD1;
            pre2[i + 1] = (pre2[i] * BASE + v) % MOD2;
        }
        for (int start = 0; start <= total - L; start++) {
            long cur1 = (pre1[start + L] - (pre1[start] * pow1[L]) % MOD1 + MOD1) % MOD1;
            long cur2 = (pre2[start + L] - (pre2[start] * pow2[L]) % MOD2 + MOD2) % MOD2;
            if (cur1 == patHash1 && cur2 == patHash2) {
                diff[start] += 1;
                diff[start + L] -= 1;
            }
        }
    }

    // Helper to avoid varargs warning
    private char[] text(char[] arr) { return arr; }
}
```

## Python

```python
class Solution(object):
    def countCells(self, grid, pattern):
        """
        :type grid: List[List[str]]
        :type pattern: str
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        N = m * n
        L = len(pattern)

        # KMP prefix function
        def build_lps(p):
            lps = [0] * len(p)
            length = 0
            i = 1
            while i < len(p):
                if p[i] == p[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        # KMP search, returns list of start indices (including overlapping)
        def kmp_search(text, pat):
            if not pat or len(pat) > len(text):
                return []
            lps = build_lps(pat)
            res = []
            i = j = 0
            while i < len(text):
                if text[i] == pat[j]:
                    i += 1
                    j += 1
                    if j == len(pat):
                        res.append(i - j)
                        j = lps[j - 1]
                else:
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        i += 1
            return res

        # Horizontal linearization (row-major)
        row_strings = [''.join(row) for row in grid]
        S_h = ''.join(row_strings)

        horiz_occurs = kmp_search(S_h, pattern)
        diff_h = [0] * (N + 1)
        for s in horiz_occurs:
            diff_h[s] += 1
            e = s + L
            if e <= N:
                diff_h[e] -= 1

        horiz_cov = [False] * N
        cur = 0
        for i in range(N):
            cur += diff_h[i]
            horiz_cov[i] = cur > 0

        # Vertical linearization (column-major)
        col_parts = []
        for c in range(n):
            col_chars = [grid[r][c] for r in range(m)]
            col_parts.append(''.join(col_chars))
        S_v = ''.join(col_parts)

        vert_occurs = kmp_search(S_v, pattern)
        diff_v = [0] * (N + 1)
        for s in vert_occurs:
            diff_v[s] += 1
            e = s + L
            if e <= N:
                diff_v[e] -= 1

        ans = 0
        cur = 0
        for i in range(N):
            cur += diff_v[i]
            if cur > 0 and horiz_cov[i]:
                ans += 1

        return ans
```

## Python3

```python
class Solution:
    def countCells(self, grid, pattern):
        m = len(grid)
        n = len(grid[0])
        N = m * n
        L = len(pattern)
        if L > N:
            return 0

        # Build row-major string
        row_str = ''.join(''.join(row) for row in grid)

        # Build column-major string
        cols = []
        for j in range(n):
            for i in range(m):
                cols.append(grid[i][j])
        col_str = ''.join(cols)

        def kmp(text, pat):
            lps = [0] * len(pat)
            length = 0
            i = 1
            while i < len(pat):
                if pat[i] == pat[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            res = []
            i = j = 0
            while i < len(text):
                if text[i] == pat[j]:
                    i += 1
                    j += 1
                    if j == len(pat):
                        res.append(i - j)
                        j = lps[j - 1]
                else:
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        i += 1
            return res

        horiz_starts = kmp(row_str, pattern)
        vert_starts = kmp(col_str, pattern)

        diff_h = [0] * (N + 1)
        for s in horiz_starts:
            diff_h[s] += 1
            end = s + L
            if end <= N:
                diff_h[end] -= 1

        diff_v = [0] * (N + 1)
        for s in vert_starts:
            diff_v[s] += 1
            end = s + L
            if end <= N:
                diff_v[end] -= 1

        horiz_cov = [False] * N
        cur = 0
        for i in range(N):
            cur += diff_h[i]
            horiz_cov[i] = cur > 0

        vert_cov = [False] * N
        cur = 0
        for i in range(N):
            cur += diff_v[i]
            vert_cov[i] = cur > 0

        count = 0
        for i in range(m):
            base_row = i * n
            for j in range(n):
                idx_r = base_row + j          # row-major index
                idx_c = j * m + i             # column-major index
                if horiz_cov[idx_r] and vert_cov[idx_c]:
                    count += 1
        return count
```

## C

```c
int countCells(char** grid, int gridSize, int* gridColSize, char* pattern) {
    int m = gridSize;
    long long total = 0;
    for (int i = 0; i < m; ++i) total += gridColSize[i];
    int N = (int)total;

    int L = 0;
    while (pattern[L] != '\0') ++L;
    if (L == 0 || L > N) return 0;

    char *S = (char *)malloc(N);
    char *T = (char *)malloc(N);
    int idx = 0;
    for (int i = 0; i < m; ++i) {
        int cols = gridColSize[i];
        for (int j = 0; j < cols; ++j) S[idx++] = grid[i][j];
    }
    idx = 0;
    int n = gridColSize[0]; // uniform per constraints
    for (int j = 0; j < n; ++j)
        for (int i = 0; i < m; ++i) T[idx++] = grid[i][j];

    int *pi = (int *)malloc(L * sizeof(int));
    pi[0] = 0;
    for (int i = 1; i < L; ++i) {
        int k = pi[i - 1];
        while (k > 0 && pattern[k] != pattern[i]) k = pi[k - 1];
        if (pattern[k] == pattern[i]) ++k;
        pi[i] = k;
    }

    int *hDiff = (int *)calloc(N + 1, sizeof(int));
    int *vDiff = (int *)calloc(N + 1, sizeof(int));

    // KMP on horizontal linearization
    int q = 0;
    for (int i = 0; i < N; ++i) {
        while (q > 0 && pattern[q] != S[i]) q = pi[q - 1];
        if (pattern[q] == S[i]) ++q;
        if (q == L) {
            int start = i - L + 1;
            hDiff[start] += 1;
            hDiff[start + L] -= 1;
            q = pi[q - 1];
        }
    }

    // KMP on vertical linearization
    q = 0;
    for (int i = 0; i < N; ++i) {
        while (q > 0 && pattern[q] != T[i]) q = pi[q - 1];
        if (pattern[q] == T[i]) ++q;
        if (q == L) {
            int start = i - L + 1;
            vDiff[start] += 1;
            vDiff[start + L] -= 1;
            q = pi[q - 1];
        }
    }

    int ans = 0, curH = 0, curV = 0;
    for (int i = 0; i < N; ++i) {
        curH += hDiff[i];
        curV += vDiff[i];
        if (curH > 0 && curV > 0) ++ans;
    }

    free(S);
    free(T);
    free(pi);
    free(hDiff);
    free(vDiff);
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    private const long MOD1 = 1000000007L;
    private const long MOD2 = 1000000009L;
    private const long BASE = 91138233L;

    public int CountCells(char[][] grid, string pattern)
    {
        int m = grid.Length;
        int n = grid[0].Length;
        int total = m * n;
        int L = pattern.Length;

        // Build row-major string S
        char[] S = new char[total];
        int pos = 0;
        for (int r = 0; r < m; r++)
            for (int c = 0; c < n; c++)
                S[pos++] = grid[r][c];

        // Build column-major string V
        char[] V = new char[total];
        pos = 0;
        for (int c = 0; c < n; c++)
            for (int r = 0; r < m; r++)
                V[pos++] = grid[r][c];

        // Precompute powers
        long[] pow1 = new long[total + 1];
        long[] pow2 = new long[total + 1];
        pow1[0] = pow2[0] = 1;
        for (int i = 1; i <= total; i++)
        {
            pow1[i] = (pow1[i - 1] * BASE) % MOD1;
            pow2[i] = (pow2[i - 1] * BASE) % MOD2;
        }

        // Prefix hashes for S
        long[] preS1 = new long[total + 1];
        long[] preS2 = new long[total + 1];
        for (int i = 0; i < total; i++)
        {
            preS1[i + 1] = (preS1[i] * BASE + S[i]) % MOD1;
            preS2[i + 1] = (preS2[i] * BASE + S[i]) % MOD2;
        }

        // Prefix hashes for V
        long[] preV1 = new long[total + 1];
        long[] preV2 = new long[total + 1];
        for (int i = 0; i < total; i++)
        {
            preV1[i + 1] = (preV1[i] * BASE + V[i]) % MOD1;
            preV2[i + 1] = (preV2[i] * BASE + V[i]) % MOD2;
        }

        // Pattern hash
        long patHash1 = 0, patHash2 = 0;
        foreach (char ch in pattern)
        {
            patHash1 = (patHash1 * BASE + ch) % MOD1;
            patHash2 = (patHash2 * BASE + ch) % MOD2;
        }

        // Difference arrays for coverage
        int[] diffH = new int[total + 1];
        int[] diffV = new int[total + 1];

        // Horizontal matches
        for (int i = 0; i + L <= total; i++)
        {
            long cur1 = (preS1[i + L] - preS1[i] * pow1[L]) % MOD1;
            if (cur1 < 0) cur1 += MOD1;
            long cur2 = (preS2[i + L] - preS2[i] * pow2[L]) % MOD2;
            if (cur2 < 0) cur2 += MOD2;

            if (cur1 == patHash1 && cur2 == patHash2)
            {
                diffH[i] ++;
                diffH[i + L] --;
            }
        }

        // Vertical matches
        for (int i = 0; i + L <= total; i++)
        {
            long cur1 = (preV1[i + L] - preV1[i] * pow1[L]) % MOD1;
            if (cur1 < 0) cur1 += MOD1;
            long cur2 = (preV2[i + L] - preV2[i] * pow2[L]) % MOD2;
            if (cur2 < 0) cur2 += MOD2;

            if (cur1 == patHash1 && cur2 == patHash2)
            {
                diffV[i] ++;
                diffV[i + L] --;
            }
        }

        // Build coverage boolean arrays
        bool[] horiz = new bool[total];
        bool[] vert = new bool[total];

        int acc = 0;
        for (int i = 0; i < total; i++)
        {
            acc += diffH[i];
            if (acc > 0) horiz[i] = true;
        }

        acc = 0;
        for (int i = 0; i < total; i++)
        {
            acc += diffV[i];
            if (acc > 0) vert[i] = true;
        }

        // Count cells covered by both
        int result = 0;
        for (int i = 0; i < total; i++)
            if (horiz[i] && vert[i]) result++;

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {character[][]} grid
 * @param {string} pattern
 * @return {number}
 */
var countCells = function(grid, pattern) {
    const m = grid.length;
    const n = grid[0].length;
    const total = m * n;
    const L = pattern.length;

    // Build row-major character array
    const rowArr = new Array(total);
    for (let r = 0; r < m; ++r) {
        for (let c = 0; c < n; ++c) {
            rowArr[r * n + c] = grid[r][c];
        }
    }

    // Build column-major character array
    const colArr = new Array(total);
    for (let c = 0; c < n; ++c) {
        for (let r = 0; r < m; ++r) {
            colArr[c * m + r] = grid[r][c];
        }
    }

    // Convert pattern to array
    const patArr = Array.from(pattern);

    // KMP preprocessing: compute lps array
    function buildLPS(p) {
        const lps = new Int32Array(p.length);
        let len = 0;
        for (let i = 1; i < p.length; ++i) {
            while (len > 0 && p[i] !== p[len]) {
                len = lps[len - 1];
            }
            if (p[i] === p[len]) {
                ++len;
                lps[i] = len;
            }
        }
        return lps;
    }

    const lps = buildLPS(patArr);

    // KMP search returning start indices where pattern fits completely
    function kmpSearch(text) {
        const starts = [];
        let j = 0; // index in pattern
        for (let i = 0; i < text.length; ++i) {
            while (j > 0 && text[i] !== patArr[j]) {
                j = lps[j - 1];
            }
            if (text[i] === patArr[j]) {
                ++j;
                if (j === L) {
                    const startIdx = i - L + 1;
                    // ensure the match does not exceed total length (always true here)
                    starts.push(startIdx);
                    j = lps[j - 1];
                }
            }
        }
        return starts;
    }

    // Process horizontal matches
    const diffH = new Int32Array(total + 1);
    const horizStarts = kmpSearch(rowArr);
    for (const s of horizStarts) {
        if (s + L <= total) { // safety, though always true
            diffH[s] += 1;
            diffH[s + L] -= 1;
        }
    }

    // Process vertical matches
    const diffV = new Int32Array(total + 1);
    const vertStarts = kmpSearch(colArr);
    for (const s of vertStarts) {
        if (s + L <= total) {
            diffV[s] += 1;
            diffV[s + L] -= 1;
        }
    }

    // Build coverage boolean arrays
    const horizCover = new Uint8Array(total);
    const vertCover = new Uint8Array(total);

    let cur = 0;
    for (let i = 0; i < total; ++i) {
        cur += diffH[i];
        horizCover[i] = cur > 0 ? 1 : 0;
    }
    cur = 0;
    for (let i = 0; i < total; ++i) {
        cur += diffV[i];
        vertCover[i] = cur > 0 ? 1 : 0;
    }

    // Count cells covered by both
    let ans = 0;
    for (let r = 0; r < m; ++r) {
        for (let c = 0; c < n; ++c) {
            const idxH = r * n + c;
            const idxV = c * m + r;
            if (horizCover[idxH] && vertCover[idxV]) ans++;
        }
    }

    return ans;
};
```

## Typescript

```typescript
function countCells(grid: string[][], pattern: string): number {
    const m = grid.length;
    const n = grid[0].length;
    const total = m * n;
    const L = pattern.length;
    if (L > total) return 0;

    // Build horizontal linearized string (row‑major)
    const horizChars: string[] = new Array(total);
    let idx = 0;
    for (let r = 0; r < m; ++r) {
        for (let c = 0; c < n; ++c) {
            horizChars[idx++] = grid[r][c];
        }
    }
    const horizStr = horizChars.join('');

    // Build vertical linearized string (column‑major)
    const vertChars: string[] = new Array(total);
    idx = 0;
    for (let c = 0; c < n; ++c) {
        for (let r = 0; r < m; ++r) {
            vertChars[idx++] = grid[r][c];
        }
    }
    const vertStr = vertChars.join('');

    // KMP to find all start positions of pattern in a text
    function kmpSearch(text: string, pat: string): number[] {
        const n = text.length;
        const m = pat.length;
        if (m === 0) return [];
        const lps = new Int32Array(m);
        // build LPS array
        for (let i = 1, len = 0; i < m;) {
            if (pat.charAt(i) === pat.charAt(len)) {
                ++len;
                lps[i] = len;
                ++i;
            } else {
                if (len !== 0) {
                    len = lps[len - 1];
                } else {
                    lps[i] = 0;
                    ++i;
                }
            }
        }
        const res: number[] = [];
        for (let i = 0, j = 0; i < n;) {
            if (text.charAt(i) === pat.charAt(j)) {
                ++i; ++j;
                if (j === m) {
                    res.push(i - j);
                    j = lps[j - 1];
                }
            } else {
                if (j !== 0) {
                    j = lps[j - 1];
                } else {
                    ++i;
                }
            }
        }
        return res;
    }

    const horizStarts = kmpSearch(horizStr, pattern);
    const vertStarts = kmpSearch(vertStr, pattern);

    // Mark coverage using difference array (intervals)
    function buildMark(starts: number[], lenPat: number, tot: number): Uint8Array {
        const diff = new Int32Array(tot + 1);
        for (const s of starts) {
            diff[s] += 1;
            if (s + lenPat <= tot) diff[s + lenPat] -= 1;
        }
        const mark = new Uint8Array(tot);
        let cur = 0;
        for (let i = 0; i < tot; ++i) {
            cur += diff[i];
            if (cur > 0) mark[i] = 1;
        }
        return mark;
    }

    const horizMark = buildMark(horizStarts, L, total);          // row‑major order
    const vertMarkColMajor = buildMark(vertStarts, L, total);   // column‑major order

    // Convert vertical marks to row‑major indexing
    const vertMark = new Uint8Array(total);
    for (let c = 0; c < n; ++c) {
        for (let r = 0; r < m; ++r) {
            const idxV = c * m + r;
            if (vertMarkColMajor[idxV]) {
                const idxRow = r * n + c;
                vertMark[idxRow] = 1;
            }
        }
    }

    // Count cells covered by both
    let ans = 0;
    for (let i = 0; i < total; ++i) {
        if (horizMark[i] && vertMark[i]) ++ans;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String[][] $grid
     * @param String $pattern
     * @return Integer
     */
    function countCells($grid, $pattern) {
        $m = count($grid);
        $n = count($grid[0]);
        $N = $m * $n;
        $L = strlen($pattern);
        if ($L > $N) return 0;

        // Build row-major string
        $rowStr = '';
        foreach ($grid as $row) {
            $rowStr .= implode('', $row);
        }

        // Build column-major string
        $colStr = '';
        for ($c = 0; $c < $n; ++$c) {
            for ($r = 0; $r < $m; ++$r) {
                $colStr .= $grid[$r][$c];
            }
        }

        // KMP to find all occurrences
        $horPos = $this->kmpSearch($rowStr, $pattern);
        $verPos = $this->kmpSearch($colStr, $pattern);

        // Difference arrays for coverage
        $diffH = array_fill(0, $N + 1, 0);
        foreach ($horPos as $st) {
            $diffH[$st] += 1;
            $end = $st + $L;
            if ($end <= $N) $diffH[$end] -= 1;
        }

        $diffV = array_fill(0, $N + 1, 0);
        foreach ($verPos as $st) {
            $diffV[$st] += 1;
            $end = $st + $L;
            if ($end <= $N) $diffV[$end] -= 1;
        }

        // Prefix sums to get coverage flags
        $coverH = array_fill(0, $N, false);
        $cur = 0;
        for ($i = 0; $i < $N; ++$i) {
            $cur += $diffH[$i];
            $coverH[$i] = $cur > 0;
        }

        $coverV = array_fill(0, $N, false);
        $cur = 0;
        for ($i = 0; $i < $N; ++$i) {
            $cur += $diffV[$i];
            $coverV[$i] = $cur > 0;
        }

        // Count cells covered by both
        $ans = 0;
        for ($pos = 0; $pos < $N; ++$pos) {
            if (!$coverH[$pos]) continue;
            $row = intdiv($pos, $n);
            $col = $pos % $n;
            $vPos = $col * $m + $row; // column-major index
            if ($coverV[$vPos]) ++$ans;
        }

        return $ans;
    }

    private function kmpSearch(string $text, string $pat): array {
        $n = strlen($text);
        $m = strlen($pat);
        if ($m == 0) return [];

        // Build LPS (longest proper prefix which is also suffix) array
        $lps = array_fill(0, $m, 0);
        $len = 0;
        for ($i = 1; $i < $m; ++$i) {
            while ($len > 0 && $pat[$i] !== $pat[$len]) {
                $len = $lps[$len - 1];
            }
            if ($pat[$i] === $pat[$len]) {
                ++$len;
                $lps[$i] = $len;
            } else {
                $lps[$i] = 0;
            }
        }

        // Search
        $res = [];
        $j = 0;
        for ($i = 0; $i < $n; ++$i) {
            while ($j > 0 && $text[$i] !== $pat[$j]) {
                $j = $lps[$j - 1];
            }
            if ($text[$i] === $pat[$j]) {
                ++$j;
                if ($j == $m) {
                    $res[] = $i - $m + 1;
                    $j = $lps[$j - 1];
                }
            }
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func countCells(_ grid: [[Character]], _ pattern: String) -> Int {
        let m = grid.count
        guard m > 0 else { return 0 }
        let n = grid[0].count
        let total = m * n
        let patArr = Array(pattern)
        let L = patArr.count
        if L == 0 || L > total { return 0 }

        // Build row-major string
        var rowMajor = [Character]()
        rowMajor.reserveCapacity(total)
        for r in 0..<m {
            rowMajor.append(contentsOf: grid[r])
        }

        // Build column-major string
        var colMajor = [Character]()
        colMajor.reserveCapacity(total)
        for c in 0..<n {
            for r in 0..<m {
                colMajor.append(grid[r][c])
            }
        }

        // KMP prefix function
        func computePrefix(_ pattern: [Character]) -> [Int] {
            var pi = [Int](repeating: 0, count: pattern.count)
            for i in 1..<pattern.count {
                var j = pi[i - 1]
                while j > 0 && pattern[i] != pattern[j] {
                    j = pi[j - 1]
                }
                if pattern[i] == pattern[j] { j += 1 }
                pi[i] = j
            }
            return pi
        }

        let pi = computePrefix(patArr)

        // Find match start positions using KMP
        func findStarts(in text: [Character]) -> [Int] {
            var starts = [Int]()
            var j = 0
            for i in 0..<text.count {
                while j > 0 && text[i] != patArr[j] {
                    j = pi[j - 1]
                }
                if text[i] == patArr[j] { j += 1 }
                if j == L {
                    starts.append(i - L + 1)
                    j = pi[j - 1]
                }
            }
            return starts
        }

        let horizStarts = findStarts(in: rowMajor)
        let vertStarts = findStarts(in: colMajor)

        // Difference arrays for coverage
        var diffHor = [Int](repeating: 0, count: total + 1)
        for s in horizStarts {
            diffHor[s] += 1
            let e = s + L
            if e <= total { diffHor[e] -= 1 }
        }

        var diffVert = [Int](repeating: 0, count: total + 1)
        for s in vertStarts {
            diffVert[s] += 1
            let e = s + L
            if e <= total { diffVert[e] -= 1 }
        }

        // Compute covered boolean arrays
        var horCovered = [Bool](repeating: false, count: total)
        var cur = 0
        for i in 0..<total {
            cur += diffHor[i]
            if cur > 0 { horCovered[i] = true }
        }

        var vertCovered = [Bool](repeating: false, count: total)
        cur = 0
        for i in 0..<total {
            cur += diffVert[i]
            if cur > 0 { vertCovered[i] = true }
        }

        // Count cells covered by both
        var result = 0
        for r in 0..<m {
            for c in 0..<n {
                let idxRow = r * n + c          // row-major index
                let idxCol = c * m + r          // column-major index
                if horCovered[idxRow] && vertCovered[idxCol] {
                    result += 1
                }
            }
        }

        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countCells(grid: Array<CharArray>, pattern: String): Int {
        val m = grid.size
        val n = grid[0].size
        val total = m * n
        val patArr = pattern.toCharArray()
        val L = patArr.size

        // Build row-major string
        val rowStr = CharArray(total)
        var idx = 0
        for (i in 0 until m) {
            for (j in 0 until n) {
                rowStr[idx++] = grid[i][j]
            }
        }

        // Build column-major string
        val colStr = CharArray(total)
        idx = 0
        for (j in 0 until n) {
            for (i in 0 until m) {
                colStr[idx++] = grid[i][j]
            }
        }

        // Find occurrences using KMP
        val horizStarts = kmpSearch(rowStr, patArr)
        val vertStarts = kmpSearch(colStr, patArr)

        // Difference arrays for range marking
        val diffH = IntArray(total + 1)
        for (s in horizStarts) {
            diffH[s]++
            diffH[s + L]--
        }
        val diffV = IntArray(total + 1)
        for (s in vertStarts) {
            diffV[s]++
            diffV[s + L]--
        }

        // Prefix sums to get coverage
        val horizCovered = BooleanArray(total)
        var cur = 0
        for (i in 0 until total) {
            cur += diffH[i]
            if (cur > 0) horizCovered[i] = true
        }
        val vertCovered = BooleanArray(total)
        cur = 0
        for (i in 0 until total) {
            cur += diffV[i]
            if (cur > 0) vertCovered[i] = true
        }

        // Count cells covered by both
        var ans = 0
        for (r in 0 until m) {
            for (c in 0 until n) {
                val idxH = r * n + c          // index in row-major string
                val idxV = c * m + r          // index in column-major string
                if (horizCovered[idxH] && vertCovered[idxV]) ans++
            }
        }
        return ans
    }

    private fun kmpSearch(text: CharArray, pat: CharArray): IntArray {
        val n = text.size
        val m = pat.size
        if (m == 0) return IntArray(0)

        // Build LPS array
        val lps = IntArray(m)
        var len = 0
        var i = 1
        while (i < m) {
            if (pat[i] == pat[len]) {
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

        // Search
        val occ = ArrayList<Int>()
        var j = 0
        for (k in 0 until n) {
            while (j > 0 && text[k] != pat[j]) {
                j = lps[j - 1]
            }
            if (text[k] == pat[j]) {
                j++
            }
            if (j == m) {
                occ.add(k - m + 1)
                j = lps[j - 1]
            }
        }
        return occ.toIntArray()
    }
}
```

## Dart

```dart
class Solution {
  int countCells(List<List<String>> grid, String pattern) {
    int m = grid.length;
    int n = grid[0].length;
    int total = m * n;
    int L = pattern.length;

    // pattern as integer list
    List<int> pat = List.filled(L, 0);
    for (int i = 0; i < L; ++i) {
      pat[i] = pattern.codeUnitAt(i);
    }

    // horizontal linearization
    List<int> horiz = List.filled(total, 0);
    int idx = 0;
    for (int r = 0; r < m; ++r) {
      for (int c = 0; c < n; ++c) {
        horiz[idx++] = grid[r][c].codeUnitAt(0);
      }
    }

    // vertical linearization
    List<int> vert = List.filled(total, 0);
    idx = 0;
    for (int c = 0; c < n; ++c) {
      for (int r = 0; r < m; ++r) {
        vert[idx++] = grid[r][c].codeUnitAt(0);
      }
    }

    List<int> _computePi(List<int> p) {
      int mlen = p.length;
      List<int> pi = List.filled(mlen, 0);
      for (int i = 1; i < mlen; ++i) {
        int j = pi[i - 1];
        while (j > 0 && p[i] != p[j]) {
          j = pi[j - 1];
        }
        if (p[i] == p[j]) ++j;
        pi[i] = j;
      }
      return pi;
    }

    List<int> _kmpSearch(List<int> text, List<int> pat) {
      int nlen = text.length;
      int plen = pat.length;
      List<int> pi = _computePi(pat);
      List<int> res = [];
      int j = 0;
      for (int i = 0; i < nlen; ++i) {
        while (j > 0 && text[i] != pat[j]) {
          j = pi[j - 1];
        }
        if (text[i] == pat[j]) ++j;
        if (j == plen) {
          res.add(i - plen + 1);
          j = pi[j - 1];
        }
      }
      return res;
    }

    List<int> startsH = _kmpSearch(horiz, pat);
    List<int> startsV = _kmpSearch(vert, pat);

    // horizontal coverage using difference array
    List<int> diffH = List.filled(total + 1, 0);
    for (int s in startsH) {
      diffH[s] += 1;
      int e = s + L;
      if (e <= total) diffH[e] -= 1;
    }
    List<bool> coverH = List.filled(total, false);
    int cur = 0;
    for (int i = 0; i < total; ++i) {
      cur += diffH[i];
      coverH[i] = cur > 0;
    }

    // vertical coverage using difference array
    List<int> diffV = List.filled(total + 1, 0);
    for (int s in startsV) {
      diffV[s] += 1;
      int e = s + L;
      if (e <= total) diffV[e] -= 1;
    }
    List<bool> coverV = List.filled(total, false);
    cur = 0;
    for (int i = 0; i < total; ++i) {
      cur += diffV[i];
      coverV[i] = cur > 0;
    }

    int ans = 0;
    for (int r = 0; r < m; ++r) {
      for (int c = 0; c < n; ++c) {
        int idxH = r * n + c;
        int idxV = c * m + r;
        if (coverH[idxH] && coverV[idxV]) ++ans;
      }
    }

    return ans;
  }
}
```

## Golang

```go
package main

func countCells(grid [][]byte, pattern string) int {
	m := len(grid)
	n := len(grid[0])
	N := m * n
	L := len(pattern)

	// Row-major flattening
	rowFlat := make([]byte, 0, N)
	for i := 0; i < m; i++ {
		rowFlat = append(rowFlat, grid[i]...)
	}
	horizCover := make([]bool, N)
	if L <= N {
		matches := getMatches(rowFlat, []byte(pattern))
		diff := make([]int, N+1)
		for _, s := range matches {
			diff[s]++
			end := s + L
			if end <= N {
				diff[end]--
			}
		}
		cur := 0
		for i := 0; i < N; i++ {
			cur += diff[i]
			if cur > 0 {
				horizCover[i] = true
			}
		}
	}

	// Column-major flattening
	colFlat := make([]byte, 0, N)
	for j := 0; j < n; j++ {
		for i := 0; i < m; i++ {
			colFlat = append(colFlat, grid[i][j])
		}
	}
	vertCover := make([]bool, N)
	if L <= N {
		matches := getMatches(colFlat, []byte(pattern))
		diff := make([]int, N+1)
		for _, s := range matches {
			diff[s]++
			end := s + L
			if end <= N {
				diff[end]--
			}
		}
		cur := 0
		for i := 0; i < N; i++ {
			cur += diff[i]
			if cur > 0 {
				vertCover[i] = true
			}
		}
	}

	// Count cells covered by both a horizontal and vertical occurrence
	ans := 0
	for i := 0; i < m; i++ {
		rowBase := i * n
		for j := 0; j < n; j++ {
			idxRow := rowBase + j          // index in row-major order
			idxCol := j*m + i              // index in column-major order
			if horizCover[idxRow] && vertCover[idxCol] {
				ans++
			}
		}
	}
	return ans
}

func getMatches(seq []byte, pat []byte) []int {
	n := len(seq)
	m := len(pat)
	if m > n {
		return nil
	}
	const base uint64 = 91138233
	pow := make([]uint64, m+1)
	pow[0] = 1
	for i := 1; i <= m; i++ {
		pow[i] = pow[i-1] * base
	}

	var patHash uint64 = 0
	for _, c := range pat {
		patHash = patHash*base + uint64(c)
	}
	pref := make([]uint64, n+1)
	for i := 0; i < n; i++ {
		pref[i+1] = pref[i]*base + uint64(seq[i])
	}

	res := make([]int, 0)
	for i := 0; i <= n-m; i++ {
		h := pref[i+m] - pref[i]*pow[m]
		if h == patHash {
			res = append(res, i)
		}
	}
	return res
}
```

## Ruby

```ruby
def kmp_search(text_bytes, pat_bytes)
  n = text_bytes.length
  m = pat_bytes.length
  return [] if m == 0 || n < m

  pi = Array.new(m, 0)
  j = 0
  (1...m).each do |i|
    while j > 0 && pat_bytes[i] != pat_bytes[j]
      j = pi[j - 1]
    end
    if pat_bytes[i] == pat_bytes[j]
      j += 1
      pi[i] = j
    end
  end

  res = []
  j = 0
  (0...n).each do |i|
    while j > 0 && text_bytes[i] != pat_bytes[j]
      j = pi[j - 1]
    end
    if text_bytes[i] == pat_bytes[j]
      j += 1
      if j == m
        res << i - m + 1
        j = pi[j - 1]
      end
    end
  end
  res
end

# @param {Character[][]} grid
# @param {String} pattern
# @return {Integer}
def count_cells(grid, pattern)
  m = grid.length
  n = grid[0].length
  total = m * n
  l = pattern.length
  return 0 if l > total

  # row‑major linearization
  s_bytes = []
  grid.each do |row|
    row.each { |ch| s_bytes << ch.ord }
  end

  # column‑major linearization
  t_bytes = []
  n.times do |c|
    m.times do |r|
      t_bytes << grid[r][c].ord
    end
  end

  pat_bytes = pattern.bytes

  horiz_starts = kmp_search(s_bytes, pat_bytes)
  vert_starts  = kmp_search(t_bytes, pat_bytes)

  # horizontal coverage using difference array
  horiz_diff = Array.new(total + 1, 0)
  horiz_starts.each do |st|
    horiz_diff[st] += 1
    horiz_diff[st + l] -= 1
  end
  horiz_cov = Array.new(total, false)
  cur = 0
  total.times do |i|
    cur += horiz_diff[i]
    horiz_cov[i] = cur > 0
  end

  # vertical coverage using difference array
  vert_diff = Array.new(total + 1, 0)
  vert_starts.each do |st|
    vert_diff[st] += 1
    vert_diff[st + l] -= 1
  end
  vert_cov = Array.new(total, false)
  cur = 0
  total.times do |i|
    cur += vert_diff[i]
    vert_cov[i] = cur > 0
  end

  ans = 0
  total.times do |i|
    ans += 1 if horiz_cov[i] && vert_cov[i]
  end
  ans
end
```

## Scala

```scala
object Solution {
    def countCells(grid: Array[Array[Char]], pattern: String): Int = {
        val m = grid.length
        val n = grid(0).length
        val total = m * n
        val L = pattern.length

        // Build horizontal linearization
        val horiz = new Array[Char](total)
        var idx = 0
        var i = 0
        while (i < m) {
            var j = 0
            while (j < n) {
                horiz(idx) = grid(i)(j)
                idx += 1
                j += 1
            }
            i += 1
        }

        // Build vertical linearization
        val vert = new Array[Char](total)
        idx = 0
        var col = 0
        while (col < n) {
            var row = 0
            while (row < m) {
                vert(idx) = grid(row)(col)
                idx += 1
                row += 1
            }
            col += 1
        }

        // Rolling hash parameters
        val mod1 = 1000000007L
        val mod2 = 1000000009L
        val base = 91138233L

        // Precompute powers
        val pow1 = new Array[Long](total + 1)
        val pow2 = new Array[Long](total + 1)
        pow1(0) = 1L
        pow2(0) = 1L
        var k = 1
        while (k <= total) {
            pow1(k) = (pow1(k - 1) * base) % mod1
            pow2(k) = (pow2(k - 1) * base) % mod2
            k += 1
        }

        // Prefix hashes for horiz and vert
        val prefH1 = new Array[Long](total + 1)
        val prefH2 = new Array[Long](total + 1)
        i = 0
        while (i < total) {
            val v = (horiz(i) - 'a' + 1).toLong
            prefH1(i + 1) = (prefH1(i) * base + v) % mod1
            prefH2(i + 1) = (prefH2(i) * base + v) % mod2
            i += 1
        }

        val prefV1 = new Array[Long](total + 1)
        val prefV2 = new Array[Long](total + 1)
        i = 0
        while (i < total) {
            val v = (vert(i) - 'a' + 1).toLong
            prefV1(i + 1) = (prefV1(i) * base + v) % mod1
            prefV2(i + 1) = (prefV2(i) * base + v) % mod2
            i += 1
        }

        // Pattern hash
        var patH1 = 0L
        var patH2 = 0L
        i = 0
        while (i < L) {
            val v = (pattern.charAt(i) - 'a' + 1).toLong
            patH1 = (patH1 * base + v) % mod1
            patH2 = (patH2 * base + v) % mod2
            i += 1
        }

        // Difference arrays for coverage
        val diffH = new Array[Int](total + 1)
        val diffV = new Array[Int](total + 1)

        // Find horizontal matches
        var start = 0
        while (start <= total - L) {
            val cur1 = (prefH1(start + L) - (prefH1(start) * pow1(L)) % mod1 + mod1) % mod1
            val cur2 = (prefH2(start + L) - (prefH2(start) * pow2(L)) % mod2 + mod2) % mod2
            if (cur1 == patH1 && cur2 == patH2) {
                diffH(start) += 1
                diffH(start + L) -= 1
            }
            start += 1
        }

        // Find vertical matches
        start = 0
        while (start <= total - L) {
            val cur1 = (prefV1(start + L) - (prefV1(start) * pow1(L)) % mod1 + mod1) % mod1
            val cur2 = (prefV2(start + L) - (prefV2(start) * pow2(L)) % mod2 + mod2) % mod2
            if (cur1 == patH1 && cur2 == patH2) {
                diffV(start) += 1
                diffV(start + L) -= 1
            }
            start += 1
        }

        // Prefix sum to get coverage flags
        val coverH = new Array[Boolean](total)
        var acc = 0
        i = 0
        while (i < total) {
            acc += diffH(i)
            coverH(i) = acc > 0
            i += 1
        }

        val coverV = new Array[Boolean](total)
        acc = 0
        i = 0
        while (i < total) {
            acc += diffV(i)
            coverV(i) = acc > 0
            i += 1
        }

        // Count cells where both coverings are true
        var result = 0
        i = 0
        while (i < m) {
            var j = 0
            while (j < n) {
                val hIdx = i * n + j
                val vIdx = j * m + i
                if (coverH(hIdx) && coverV(vIdx)) result += 1
                j += 1
            }
            i += 1
        }

        result
    }
}
```

## Rust

```rust
use std::cmp::min;

fn kmp_find(text: &[char], pat: &[char]) -> Vec<usize> {
    let l = pat.len();
    if l == 0 || text.len() < l {
        return Vec::new();
    }
    // build longest proper prefix which is also suffix array
    let mut lps = vec![0usize; l];
    let mut len = 0usize;
    for i in 1..l {
        while len > 0 && pat[i] != pat[len] {
            len = lps[len - 1];
        }
        if pat[i] == pat[len] {
            len += 1;
            lps[i] = len;
        }
    }
    // search
    let mut res = Vec::new();
    let mut i = 0usize;
    let mut j = 0usize;
    while i < text.len() {
        while j > 0 && text[i] != pat[j] {
            j = lps[j - 1];
        }
        if text[i] == pat[j] {
            j += 1;
        }
        if j == l {
            res.push(i + 1 - l);
            j = lps[j - 1];
        }
        i += 1;
    }
    res
}

impl Solution {
    pub fn count_cells(grid: Vec<Vec<char>>, pattern: String) -> i32 {
        let m = grid.len();
        if m == 0 {
            return 0;
        }
        let n = grid[0].len();
        let total = m * n;
        let pat_vec: Vec<char> = pattern.chars().collect();
        let l = pat_vec.len();

        // Build linear string for horizontal scanning (row-major)
        let mut horiz_str = Vec::with_capacity(total);
        for row in &grid {
            for &ch in row.iter() {
                horiz_str.push(ch);
            }
        }

        // Horizontal occurrences
        let starts_h = kmp_find(&horiz_str, &pat_vec);
        let mut diff_h = vec![0i32; total + 1];
        for &st in &starts_h {
            diff_h[st] += 1;
            let end = st + l;
            if end <= total {
                diff_h[end] -= 1;
            }
        }
        let mut horiz_cover = vec![false; total];
        let mut cur = 0i32;
        for i in 0..total {
            cur += diff_h[i];
            horiz_cover[i] = cur > 0;
        }

        // Build linear string for vertical scanning (column-major)
        let mut vert_str = Vec::with_capacity(total);
        for col in 0..n {
            for row in 0..m {
                vert_str.push(grid[row][col]);
            }
        }

        // Vertical occurrences
        let starts_v = kmp_find(&vert_str, &pat_vec);
        let mut diff_v = vec![0i32; total + 1];
        for &st in &starts_v {
            diff_v[st] += 1;
            let end = st + l;
            if end <= total {
                diff_v[end] -= 1;
            }
        }
        let mut vert_cover = vec![false; total];
        cur = 0;
        for i in 0..total {
            cur += diff_v[i];
            vert_cover[i] = cur > 0;
        }

        // Count cells covered by both a horizontal and a vertical occurrence
        let mut ans = 0i32;
        for r in 0..m {
            for c in 0..n {
                let idx_h = r * n + c;      // index in row-major string
                let idx_v = c * m + r;      // index in column-major string
                if horiz_cover[idx_h] && vert_cover[idx_v] {
                    ans += 1;
                }
            }
        }
        ans
    }
}
```

## Racket

```racket
(define (count-cells grid pattern)
  (let* ((m (length grid))
         (n (if (= m 0) 0 (length (first grid))))
         (N (* m n))
         (L (string-length pattern)))
    (if (> L N)
        0
        (let ()
          ;; build row-major vector
          (define row-vec (make-vector N #\space))
          (let loop ((i 0) (rgrid grid))
            (when (< i N)
              (let ((row (car rgrid)))
                (let inner ((j 0) (cols row))
                  (when (< j n)
                    (vector-set! row-vec (+ i j) (car cols))
                    (inner (+ j 1) (cdr cols))))
                (loop (+ i n) (cdr rgrid)))))
          ;; build column-major vector
          (define col-vec (make-vector N #\space))
          (let loop ((c 0) (col-index 0))
            (when (< c n)
              (let inner ((r 0) (idx col-index))
                (when (< r m)
                  (vector-set! col-vec idx
                               (list-ref (list-ref grid r) c))
                  (inner (+ r 1) (+ idx 1))))
              (loop (+ c 1) (+ col-index m))))
          ;; KMP prefix function
          (define (build-lps pat)
            (let ((lps (make-vector L 0)))
              (let loop ((len 0) (i 1))
                (when (< i L)
                  (if (char=? (string-ref pat i) (string-ref pat len))
                      (begin
                        (set! len (+ len 1))
                        (vector-set! lps i len)
                        (loop len (+ i 1)))
                      (if (> len 0)
                          (begin
                            (set! len (vector-ref lps (- len 1)))
                            (loop len i))
                          (begin
                            (vector-set! lps i 0)
                            (loop len (+ i 1)))))))
              lps))
          ;; KMP search returning start positions
          (define (kmp-search text pat)
            (let ((lps (build-lps pat)))
              (let loop ((i 0) (j 0) (starts '()))
                (if (= i N)
                    (reverse starts)
                    (let ((ti (vector-ref text i))
                          (pj (string-ref pat j)))
                      (if (char=? ti pj)
                          (let ((i1 (+ i 1)) (j1 (+ j 1)))
                            (if (= j1 L)
                                (loop i1 (vector-ref lps (- j1 1))
                                      (cons (- i1 L) starts))
                                (loop i1 j1 starts)))
                          (if (> j 0)
                              (loop i (vector-ref lps (- j 1)) starts)
                              (loop (+ i 1) j starts))))))))
          ;; horizontal matches
          (define horiz-diff (make-vector (+ N 1) 0))
          (for ([s (in-list (kmp-search row-vec pattern))])
            (vector-set! horiz-diff s (+ (vector-ref horiz-diff s) 1))
            (let ((e (+ s L)))
              (when (<= e N)
                (vector-set! horiz-diff e (- (vector-ref horiz-diff e) 1)))))
          (define horiz (make-vector N #f))
          (let loop ((i 0) (cur 0))
            (when (< i N)
              (set! cur (+ cur (vector-ref horiz-diff i)))
              (vector-set! horiz i (> cur 0))
              (loop (+ i 1) cur)))
          ;; vertical matches
          (define vert-diff (make-vector (+ N 1) 0))
          (for ([s (in-list (kmp-search col-vec pattern))])
            (vector-set! vert-diff s (+ (vector-ref vert-diff s) 1))
            (let ((e (+ s L)))
              (when (<= e N)
                (vector-set! vert-diff e (- (vector-ref vert-diff e) 1)))))
          (define vert (make-vector N #f))
          (let loop ((j 0) (cur 0))
            (when (< j N)
              (set! cur (+ cur (vector-ref vert-diff j)))
              (when (> cur 0)
                (let* ((row (modulo j m))
                       (col (quotient j m))
                       (idx (+ (* row n) col)))
                  (vector-set! vert idx #t)))
              (loop (+ j 1) cur)))
          ;; count intersection
          (let loop ((i 0) (cnt 0))
            (if (= i N)
                cnt
                (loop (+ i 1)
                      (if (and (vector-ref horiz i) (vector-ref vert i))
                          (+ cnt 1)
                          cnt)))))))))
```

## Erlang

```erlang
-module(solution).
-export([count_cells/2]).

-spec count_cells(Grid :: [[char()]], Pattern :: unicode:unicode_binary()) -> integer().
count_cells(Grid, Pattern) ->
    %% Convert each row to binary of chars
    RowBins = [list_to_binary([hd(Cell) || Cell <- Row]) || Row <- Grid],
    M = length(RowBins),
    N = case RowBins of
            [] -> 0;
            [First|_] -> byte_size(First)
        end,
    Total = M * N,
    %% Horizontal string: concatenate rows
    HBin = iolist_to_binary(RowBins),
    %% Vertical string: column-major order
    VList = [binary:at(RowBin, C) || C <- lists:seq(0, N-1), RowBin <- RowBins],
    VBin = list_to_binary(VList),
    PatBin = unicode:characters_to_binary(Pattern),
    L = byte_size(PatBin),
    case L > Total of
        true -> 0;
        false ->
            PiArray = build_pi(PatBin),
            HorStarts = kmp_search(HBin, PatBin, PiArray),
            VertStarts = kmp_search(VBin, PatBin, PiArray),

            %% Mark cells covered by horizontal matches (global index = row-major)
            HMap0 = #{},
            HMap = lists:foldl(fun(S, Acc) ->
                        mark_range(S, L, fun(Idx) -> maps:put(Idx, true, Acc) end)
                    end, HMap0, HorStarts),

            %% Mark cells covered by vertical matches (convert to global index)
            VMap0 = #{},
            VMap = lists:foldl(fun(T, Acc) ->
                        mark_vertical_range(T, L, M, N, fun(GlobalIdx) -> maps:put(GlobalIdx, true, Acc) end)
                    end, VMap0, VertStarts),

            %% Count intersection
            {Small, Large} = if maps:size(HMap) =< maps:size(VMap) ->
                                    {HMap, VMap};
                                true ->
                                    {VMap, HMap}
                              end,
            lists:foldl(fun({Key,_}, Cnt) ->
                        case maps:is_key(Key, Large) of
                            true -> Cnt + 1;
                            false -> Cnt
                        end
                    end, 0, maps:to_list(Small))
    end.

%% Mark indices from Start to Start+Len-1 using Fun(Index)
mark_range(Start, Len, Fun) ->
    mark_range_helper(0, Start, Len, Fun).

mark_range_helper(K, _Start, Len, _Fun) when K >= Len -> fun(X)->X end,
mark_range_helper(K, Start, Len, Fun) ->
    Idx = Start + K,
    NewFun = Fun(Idx),
    mark_range_helper(K+1, Start, Len, NewFun).

%% Mark vertical range converting to global row-major index
mark_vertical_range(Start, Len, M, N, Fun) ->
    mark_vertical_helper(0, Start, Len, M, N, Fun).

mark_vertical_helper(K, _Start, Len, _M, _N, _Fun) when K >= Len -> fun(X)->X end,
mark_vertical_helper(K, Start, Len, M, N, Fun) ->
    IdxV = Start + K,
    R = IdxV rem M,
    C = IdxV div M,
    GlobalIdx = R * N + C,
    NewFun = Fun(GlobalIdx),
    mark_vertical_helper(K+1, Start, Len, M, N, NewFun).

%% Build prefix function (pi array) for KMP
build_pi(PatBin) ->
    L = byte_size(PatBin),
    Pi0 = array:new(L, {default,0}),
    build_pi_loop(1, 0, L, PatBin, Pi0).

build_pi_loop(I, K, L, PatBin, PiArray) when I < L ->
    CharI = binary:at(PatBin, I),
    NewK = adjust_k(K, CharI, PatBin, PiArray),
    FinalK = if CharI == binary:at(PatBin, NewK) -> NewK + 1; true -> NewK end,
    PiArray2 = array:set(I, FinalK, PiArray),
    build_pi_loop(I+1, FinalK, L, PatBin, PiArray2);
build_pi_loop(_, _, _, _, PiArray) ->
    PiArray.

adjust_k(K, CharI, PatBin, PiArray) when K > 0 ->
    CharK = binary:at(PatBin, K),
    if CharI == CharK -> K;
       true -> adjust_k(array:get(K-1, PiArray), CharI, PatBin, PiArray)
    end;
adjust_k(0, _CharI, _, _) -> 0.

%% KMP search returning list of start indices
kmp_search(TextBin, PatBin, PiArray) ->
    N = byte_size(TextBin),
    L = byte_size(PatBin),
    kmp_search_loop(0, 0, N, L, TextBin, PatBin, PiArray, []).

kmp_search_loop(I, Q, N, L, TextBin, PatBin, PiArray, Acc) when I < N ->
    CharT = binary:at(TextBin, I),
    {Q1} =
        case Q of
            0 ->
                if CharT == binary:at(PatBin,0) -> {1}; true -> {0} end;
            _ ->
                CharP = binary:at(PatBin, Q),
                if CharT == CharP -> {Q+1};
                   true -> adjust_q(Q-1, CharT, PatBin, PiArray)
                end
        end,
    case Q1 of
        L when L == L ->
            Start = I - L + 1,
            NewQ = array:get(L-1, PiArray),
            kmp_search_loop(I+1, NewQ, N, L, TextBin, PatBin, PiArray, [Start|Acc]);
        _ ->
            kmp_search_loop(I+1, Q1, N, L, TextBin, PatBin, PiArray, Acc)
    end;
kmp_search_loop(_, _, _, _, _, _, _, Acc) -> lists:reverse(Acc).

adjust_q(K, CharT, PatBin, PiArray) when K > 0 ->
    CharK = binary:at(PatBin, K),
    if CharT == CharK -> {K+1};
       true -> adjust_q(array:get(K-1, PiArray), CharT, PatBin, PiArray)
    end;
adjust_q(0, CharT, PatBin, _) ->
    if CharT == binary:at(PatBin,0) -> {1}; true -> {0} end.
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false

  @spec count_cells(grid :: [[char]], pattern :: String.t()) :: integer()
  def count_cells(grid, pattern) do
    m = length(grid)
    n = length(hd(grid))
    total = m * n
    l_pat = String.length(pattern)

    # convert grid to list of integer char codes
    grid_int =
      Enum.map(grid, fn row ->
        Enum.map(row, fn ch -> hd(String.to_charlist(ch)) end)
      end)

    # row-major string
    row_major = List.flatten(grid_int)

    # column-major string
    col_major =
      for c <- 0..(n - 1), r <- 0..(m - 1) do
        Enum.at(Enum.at(grid_int, r), c)
      end

    pat_list = String.to_charlist(pattern)

    base = 91138233
    mod = 1_000_000_007

    # prefix hashes
    pref_h = build_prefix(row_major, base, mod)
    pref_v = build_prefix(col_major, base, mod)

    # pattern hash
    pat_hash = compute_hash(pat_list, base, mod)

    pow_l = fast_pow(base, l_pat, mod)

    horiz_cov = coverage_array(pref_h, total, l_pat, pat_hash, pow_l, mod)
    vert_cov = coverage_array(pref_v, total, l_pat, pat_hash, pow_l, mod)

    # count cells covered by both
    Enum.reduce(0..(m - 1), 0, fn r, acc ->
      Enum.reduce(0..(n - 1), acc, fn c, inner_acc ->
        idx_h = r * n + c
        idx_v = c * m + r

        if :array.get(idx_h, horiz_cov) and :array.get(idx_v, vert_cov) do
          inner_acc + 1
        else
          inner_acc
        end
      end)
    end)
  end

  # build prefix hash array (length+1)
  defp build_prefix(list, base, mod) do
    {pref_rev, _} =
      Enum.reduce(list, {[0], 0}, fn x, {acc, prev} ->
        new = rem(prev * base + x, mod)
        {[new | acc], new}
      end)

    Enum.reverse(pref_rev)
  end

  # compute hash of a list
  defp compute_hash(list, base, mod) do
    Enum.reduce(list, 0, fn x, h -> rem(h * base + x, mod) end)
  end

  # fast exponentiation for base^exp % mod
  defp fast_pow(_base, 0, _mod), do: 1

  defp fast_pow(base, exp, mod) when rem(exp, 2) == 0 do
    half = fast_pow(base, div(exp, 2), mod)
    rem(half * half, mod)
  end

  defp fast_pow(base, exp, mod) do
    rem(base * fast_pow(base, exp - 1, mod), mod)
  end

  # compute coverage boolean array using difference technique
  defp coverage_array(prefix, total, l_pat, pat_hash, pow_l, mod) do
    diff = :array.new(total + 1, default: 0)

    max_start = total - l_pat

    diff =
      Enum.reduce(0..max_start, diff, fn i, d ->
        subhash =
          rem(
            prefix |> :array.get(i + l_pat) -
              rem(:array.get(i, prefix) * pow_l, mod),
            mod
          )

        subhash = if subhash < 0, do: subhash + mod, else: subhash

        if subhash == pat_hash do
          d1 = :array.set(i, :array.get(i, d) + 1, d)
          d2 =
            if i + l_pat <= total do
              :array.set(i + l_pat, :array.get(i + l_pat, d1) - 1, d1)
            else
              d1
            end

          d2
        else
          d
        end
      end)

    # build coverage array from diff
    {cov_arr, _} =
      Enum.reduce(0..(total - 1), {:array.new(total, default: false), 0}, fn idx,
                                                                              {arr, cur} ->
        cur = cur + :array.get(idx, diff)
        arr = if cur > 0, do: :array.set(idx, true, arr), else: arr
        {arr, cur}
      end)

    cov_arr
  end
end
```
