# 3474. Lexicographically Smallest Generated String

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string generateString(string str1, string str2) {
        int n = (int)str1.size();
        int m = (int)str2.size();
        int L = n + m - 1;
        vector<int> fix(L, -1); // -1 means free
        
        // Apply forced characters from 'T' positions
        for (int i = 0; i < n; ++i) {
            if (str1[i] == 'T') {
                for (int j = 0; j < m; ++j) {
                    int pos = i + j;
                    int ch = str2[j];
                    if (fix[pos] == -1) fix[pos] = ch;
                    else if (fix[pos] != ch) return "";
                }
            }
        }
        
        // Build prefix function for str2
        vector<int> pi(m, 0);
        for (int i = 1; i < m; ++i) {
            int j = pi[i - 1];
            while (j > 0 && str2[i] != str2[j]) j = pi[j - 1];
            if (str2[i] == str2[j]) ++j;
            pi[i] = j;
        }
        
        // Build automaton nxt[state][c]
        vector<array<int,26>> nxt(m + 1);
        for (int state = 0; state <= m; ++state) {
            for (int ci = 0; ci < 26; ++ci) {
                char c = 'a' + ci;
                int t = state;
                while (t > 0 && (t == m || str2[t] != c)) t = pi[t - 1];
                if (t < m && str2[t] == c) ++t;
                nxt[state][ci] = t;
            }
        }
        
        // DP: dp[pos][state] = can finish from this configuration
        vector<vector<char>> dp(L + 1, vector<char>(m + 1, 0));
        for (int st = 0; st <= m; ++st) dp[L][st] = 1;
        
        for (int pos = L - 1; pos >= 0; --pos) {
            for (int st = 0; st <= m; ++st) {
                bool ok = false;
                if (fix[pos] != -1) {
                    int ci = fix[pos] - 'a';
                    int ns = nxt[st][ci];
                    if (ns == m) {
                        int i = pos - m + 1;
                        if (i >= 0 && str1[i] == 'T' && dp[pos + 1][ns]) ok = true;
                    } else {
                        if (dp[pos + 1][ns]) ok = true;
                    }
                } else {
                    for (int ci = 0; ci < 26; ++ci) {
                        int ns = nxt[st][ci];
                        if (ns == m) {
                            int i = pos - m + 1;
                            if (i >= 0 && str1[i] != 'T') continue;
                        }
                        if (dp[pos + 1][ns]) { ok = true; break; }
                    }
                }
                dp[pos][st] = ok;
            }
        }
        
        if (!dp[0][0]) return "";
        
        // Construct lexicographically smallest answer
        string ans(L, 'a');
        int st = 0;
        for (int pos = 0; pos < L; ++pos) {
            if (fix[pos] != -1) {
                char c = fix[pos];
                ans[pos] = c;
                st = nxt[st][c - 'a'];
                continue;
            }
            for (int ci = 0; ci < 26; ++ci) {
                int ns = nxt[st][ci];
                if (ns == m) {
                    int i = pos - m + 1;
                    if (i >= 0 && str1[i] != 'T') continue;
                }
                if (dp[pos + 1][ns]) {
                    ans[pos] = char('a' + ci);
                    st = ns;
                    break;
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public String generateString(String str1, String str2) {
        int n = str1.length();
        int m = str2.length();
        int L = n + m - 1;
        char[] fixed = new char[L];
        // Apply forced characters from 'T' positions
        for (int i = 0; i < n; i++) {
            if (str1.charAt(i) == 'T') {
                for (int j = 0; j < m; j++) {
                    int pos = i + j;
                    char c = str2.charAt(j);
                    if (fixed[pos] != 0 && fixed[pos] != c) {
                        return "";
                    }
                    fixed[pos] = c;
                }
            }
        }

        // Build KMP prefix function for pattern str2
        int[] pi = new int[m];
        for (int i = 1; i < m; i++) {
            int j = pi[i - 1];
            while (j > 0 && str2.charAt(i) != str2.charAt(j)) {
                j = pi[j - 1];
            }
            if (str2.charAt(i) == str2.charAt(j)) {
                j++;
            }
            pi[i] = j;
        }

        // Precompute transition table nxt[state][ch]
        int[][] nxt = new int[m + 1][26];
        for (int state = 0; state <= m; state++) {
            for (int ch = 0; ch < 26; ch++) {
                char c = (char) ('a' + ch);
                int k = state;
                while (k > 0 && (k == m || str2.charAt(k) != c)) {
                    k = pi[k - 1];
                }
                if (k < m && str2.charAt(k) == c) {
                    k++;
                }
                nxt[state][ch] = k;
            }
        }

        // Helper to check constraint at position pos with resulting nextState
        java.util.function.BiPredicate<Integer, Integer> okConstraint = (pos, nextState) -> {
            int start = pos - m + 1;
            if (start >= 0 && start < n) {
                char t = str1.charAt(start);
                if (t == 'T') return nextState == m;
                else return nextState != m;
            }
            return true;
        };

        boolean[][] dp = new boolean[L + 1][m + 1];
        // Base: any state at position L is acceptable
        for (int s = 0; s <= m; s++) {
            dp[L][s] = true;
        }

        // Fill DP backwards
        for (int pos = L - 1; pos >= 0; pos--) {
            char forced = fixed[pos];
            for (int state = 0; state <= m; state++) {
                boolean possible = false;
                if (forced != 0) {
                    int ns = nxt[state][forced - 'a'];
                    if (okConstraint.test(pos, ns) && dp[pos + 1][ns]) {
                        possible = true;
                    }
                } else {
                    for (int ch = 0; ch < 26; ch++) {
                        int ns = nxt[state][ch];
                        if (okConstraint.test(pos, ns) && dp[pos + 1][ns]) {
                            possible = true;
                            break;
                        }
                    }
                }
                dp[pos][state] = possible;
            }
        }

        if (!dp[0][0]) return "";

        // Reconstruct lexicographically smallest string
        StringBuilder sb = new StringBuilder();
        int state = 0;
        for (int pos = 0; pos < L; pos++) {
            char forced = fixed[pos];
            if (forced != 0) {
                sb.append(forced);
                state = nxt[state][forced - 'a'];
            } else {
                for (int ch = 0; ch < 26; ch++) {
                    int ns = nxt[state][ch];
                    if (okConstraint.test(pos, ns) && dp[pos + 1][ns]) {
                        sb.append((char) ('a' + ch));
                        state = ns;
                        break;
                    }
                }
            }
        }

        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def generateString(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        n = len(str1)
        m = len(str2)
        L = n + m - 1

        # forced characters from 'T' windows
        forced = [None] * L
        for i, ch in enumerate(str1):
            if ch == 'T':
                start = i
                for j in range(m):
                    pos = start + j
                    c = str2[j]
                    if forced[pos] is not None and forced[pos] != c:
                        return ""
                    forced[pos] = c

        # KMP prefix function for pattern str2
        pi = [0] * m
        for i in range(1, m):
            j = pi[i - 1]
            while j > 0 and str2[i] != str2[j]:
                j = pi[j - 1]
            if str2[i] == str2[j]:
                j += 1
            pi[i] = j

        # transition table for automaton (states 0..m)
        trans = [[0] * 26 for _ in range(m + 1)]
        for s in range(m + 1):
            for ci in range(26):
                c = chr(ord('a') + ci)
                if s < m and c == str2[s]:
                    trans[s][ci] = s + 1
                else:
                    if s == 0:
                        trans[s][ci] = 0
                    else:
                        trans[s][ci] = trans[pi[s - 1]][ci]

        # forward DP: dp[pos][state] reachable?
        dp = [bytearray(m + 1) for _ in range(L + 1)]
        dp[0][0] = 1

        for pos in range(L):
            cur = dp[pos]
            nxt = dp[pos + 1]
            forced_c = forced[pos]
            if forced_c is not None:
                ci = ord(forced_c) - 97
                for s in range(m + 1):
                    if not cur[s]:
                        continue
                    ns = trans[s][ci]
                    i_win = pos - m + 1
                    if 0 <= i_win < n:
                        f = str1[i_win]
                        if (f == 'T' and ns != m) or (f == 'F' and ns == m):
                            continue
                    nxt[ns] = 1
            else:
                for s in range(m + 1):
                    if not cur[s]:
                        continue
                    base_row = trans[s]
                    for ci in range(26):
                        ns = base_row[ci]
                        i_win = pos - m + 1
                        if 0 <= i_win < n:
                            f = str1[i_win]
                            if (f == 'T' and ns != m) or (f == 'F' and ns == m):
                                continue
                        nxt[ns] = 1

        # check any reachable end state
        if not any(dp[L][s] for s in range(m + 1)):
            return ""

        # backward reachability to ensure a suffix exists
        reach = [bytearray(m + 1) for _ in range(L + 1)]
        for s in range(m + 1):
            if dp[L][s]:
                reach[L][s] = 1

        for pos in range(L - 1, -1, -1):
            cur_dp = dp[pos]
            nxt_reach = reach[pos + 1]
            cur_reach = reach[pos]
            forced_c = forced[pos]
            if forced_c is not None:
                ci = ord(forced_c) - 97
                for s in range(m + 1):
                    if not cur_dp[s]:
                        continue
                    ns = trans[s][ci]
                    i_win = pos - m + 1
                    if 0 <= i_win < n:
                        f = str1[i_win]
                        if (f == 'T' and ns != m) or (f == 'F' and ns == m):
                            continue
                    if nxt_reach[ns]:
                        cur_reach[s] = 1
            else:
                for s in range(m + 1):
                    if not cur_dp[s]:
                        continue
                    base_row = trans[s]
                    for ci in range(26):
                        ns = base_row[ci]
                        i_win = pos - m + 1
                        if 0 <= i_win < n:
                            f = str1[i_win]
                            if (f == 'T' and ns != m) or (f == 'F' and ns == m):
                                continue
                        if nxt_reach[ns]:
                            cur_reach[s] = 1
                            break

        if not reach[0][0]:
            return ""

        # construct lexicographically smallest string
        ans = []
        state = 0
        for pos in range(L):
            forced_c = forced[pos]
            candidates = [forced_c] if forced_c is not None else [chr(ord('a') + i) for i in range(26)]
            chosen = None
            for c in candidates:
                ci = ord(c) - 97
                ns = trans[state][ci]
                i_win = pos - m + 1
                if 0 <= i_win < n:
                    f = str1[i_win]
                    if (f == 'T' and ns != m) or (f == 'F' and ns == m):
                        continue
                if reach[pos + 1][ns]:
                    chosen = c
                    state = ns
                    break
            if chosen is None:
                return ""
            ans.append(chosen)

        return "".join(ans)
```

## Python3

```python
class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        L = n + m - 1

        # build failure function for KMP
        fail = [0] * m
        for i in range(1, m):
            j = fail[i - 1]
            while j > 0 and str2[i] != str2[j]:
                j = fail[j - 1]
            if str2[i] == str2[j]:
                j += 1
            fail[i] = j

        # build automaton transitions
        nxt = [[0] * 26 for _ in range(m + 1)]
        for s in range(m + 1):
            for ci in range(26):
                c = chr(ord('a') + ci)
                j = s
                if j == m:
                    j = fail[m - 1]
                while j > 0 and str2[j] != c:
                    j = fail[j - 1]
                if j < m and str2[j] == c:
                    j += 1
                nxt[s][ci] = j

        # dp[pos][state] -> can we finish from pos with current automaton state = state
        dp = [[False] * (m + 1) for _ in range(L + 1)]
        for s in range(m + 1):
            dp[L][s] = True

        for pos in range(L - 1, -1, -1):
            start_idx = pos - (m - 1)
            need_check = 0 <= start_idx < n
            required_T = str1[start_idx] == 'T' if need_check else False
            for s in range(m + 1):
                ok = False
                for ci in range(26):
                    ns = nxt[s][ci]
                    if need_check:
                        if required_T and ns != m:
                            continue
                        if not required_T and ns == m:
                            continue
                    if dp[pos + 1][ns]:
                        ok = True
                        break
                dp[pos][s] = ok

        if not dp[0][0]:
            return ""

        res = []
        s = 0
        for pos in range(L):
            start_idx = pos - (m - 1)
            need_check = 0 <= start_idx < n
            required_T = str1[start_idx] == 'T' if need_check else False
            for ci in range(26):
                ns = nxt[s][ci]
                if need_check:
                    if required_T and ns != m:
                        continue
                    if not required_T and ns == m:
                        continue
                if dp[pos + 1][ns]:
                    res.append(chr(ord('a') + ci))
                    s = ns
                    break

        return ''.join(res)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* generateString(char* str1, char* str2) {
    int n = strlen(str1);
    int m = strlen(str2);
    int L = n + m - 1;

    // Allocate answer buffer
    char *ans = (char*)malloc(L + 1);
    if (!ans) return NULL;
    ans[L] = '\0';

    // Fixed positions from 'T' windows
    char *fixedChar = (char*)malloc(L);
    int *isFixed = (int*)calloc(L, sizeof(int));
    if (!fixedChar || !isFixed) {
        free(ans); free(fixedChar); free(isFixed);
        return NULL;
    }

    // Initialize answer with placeholder '?'
    for (int i = 0; i < L; ++i) ans[i] = '?';

    // Process 'T' constraints
    for (int i = 0; i < n; ++i) {
        if (str1[i] != 'T') continue;
        for (int k = 0; k < m; ++k) {
            int pos = i + k;
            char ch = str2[k];
            if (isFixed[pos]) {
                if (fixedChar[pos] != ch) { // conflict
                    ans[0] = '\0';
                    free(fixedChar); free(isFixed);
                    return ans;
                }
            } else {
                isFixed[pos] = 1;
                fixedChar[pos] = ch;
                ans[pos] = ch;
            }
        }
    }

    // Process 'F' windows greedily
    for (int i = 0; i < n; ++i) {
        if (str1[i] != 'F') continue;

        int satisfied = 0;
        for (int k = 0; k < m; ++k) {
            int pos = i + k;
            if (ans[pos] != '?' && ans[pos] != str2[k]) {
                satisfied = 1;
                break;
            }
        }

        if (!satisfied) {
            // find rightmost free position in the window
            int p = -1;
            for (int pos = i + m - 1; pos >= i; --pos) {
                if (ans[pos] == '?') { p = pos; break; }
            }
            if (p == -1) { // impossible
                ans[0] = '\0';
                free(fixedChar); free(isFixed);
                return ans;
            }
            int offset = p - i;
            char need = str2[offset];
            char c = 'a';
            while (c == need) ++c; // choose smallest different character
            ans[p] = c;
        }
    }

    // Fill remaining unknown positions with 'a'
    for (int i = 0; i < L; ++i) {
        if (ans[i] == '?') ans[i] = 'a';
    }

    free(fixedChar);
    free(isFixed);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Text;

public class Solution {
    public string GenerateString(string str1, string str2) {
        int n = str1.Length;
        int m = str2.Length;
        int L = n + m - 1;
        char[] pat = str2.ToCharArray();

        // prefix function
        int[] pi = new int[m];
        for (int i = 1; i < m; i++) {
            int j = pi[i - 1];
            while (j > 0 && pat[i] != pat[j]) j = pi[j - 1];
            if (pat[i] == pat[j]) j++;
            pi[i] = j;
        }

        // transition table
        int[,] nxt = new int[m + 1, 26];
        for (int s = 0; s <= m; s++) {
            for (int ci = 0; ci < 26; ci++) {
                char c = (char)('a' + ci);
                int t = s;
                if (t == m) t = pi[m - 1];
                while (t > 0 && pat[t] != c) t = pi[t - 1];
                if (pat[t] == c) t++;
                nxt[s, ci] = t;
            }
        }

        // dp[pos, state] where state in [0,m-1]
        bool[,] dp = new bool[L + 1, m];
        for (int s = 0; s < m; s++) dp[L, s] = true;

        for (int pos = L - 1; pos >= 0; pos--) {
            for (int state = 0; state < m; state++) {
                bool ok = false;
                for (int ci = 0; ci < 26; ci++) {
                    int t = nxt[state, ci];
                    // constraint at this position after reading char
                    if (pos >= m - 1) {
                        int start = pos - m + 1;
                        char flag = str1[start];
                        if (flag == 'T' && t != m) continue;
                        if (flag == 'F' && t == m) continue;
                    }
                    int nextState = (t == m) ? pi[m - 1] : t;
                    if (dp[pos + 1, nextState]) {
                        ok = true;
                        break;
                    }
                }
                dp[pos, state] = ok;
            }
        }

        if (!dp[0, 0]) return "";

        StringBuilder sb = new StringBuilder(L);
        int curState = 0;
        for (int pos = 0; pos < L; pos++) {
            for (int ci = 0; ci < 26; ci++) {
                int t = nxt[curState, ci];
                if (pos >= m - 1) {
                    int start = pos - m + 1;
                    char flag = str1[start];
                    if (flag == 'T' && t != m) continue;
                    if (flag == 'F' && t == m) continue;
                }
                int nextState = (t == m) ? pi[m - 1] : t;
                if (dp[pos + 1, nextState]) {
                    sb.Append((char)('a' + ci));
                    curState = nextState;
                    break;
                }
            }
        }

        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
var generateString = function(str1, str2) {
    const n = str1.length;
    const m = str2.length;
    const L = n + m - 1;
    // s[pos] = character or '' if not set yet
    const s = new Array(L).fill('');
    // Apply T constraints
    for (let i = 0; i < n; ++i) {
        if (str1[i] === 'T') {
            for (let j = 0; j < m; ++j) {
                const pos = i + j;
                const c = str2[j];
                if (s[pos] !== '' && s[pos] !== c) return "";
                s[pos] = c;
            }
        }
    }
    // Prepare windows for F positions
    const windowInfo = new Array(n); // only used when str1[i]=='F'
    const endsAt = Array.from({length: L}, () => []);
    for (let i = 0; i < n; ++i) {
        if (str1[i] === 'F') {
            const end = i + m - 1;
            windowInfo[i] = {mismatched: false};
            endsAt[end].push(i);
        }
    }
    // Initial mismatched flags based on already fixed characters
    for (let i = 0; i < n; ++i) {
        if (str1[i] === 'F') {
            let mis = false;
            for (let j = 0; j < m; ++j) {
                const pos = i + j;
                if (s[pos] !== '' && s[pos] !== str2[j]) { mis = true; break; }
            }
            windowInfo[i].mismatched = mis;
        }
    }
    // Helper to update mismatched status for windows covering position pos
    const propagate = (pos) => {
        const ch = s[pos];
        for (let offset = 0; offset < m; ++offset) {
            const start = pos - offset;
            if (start < 0 || start >= n) continue;
            if (str1[start] !== 'F') continue;
            const win = windowInfo[start];
            if (!win.mismatched && ch !== str2[offset]) {
                win.mismatched = true;
            }
        }
    };
    // Main construction
    for (let pos = 0; pos < L; ++pos) {
        // Determine if any ending F-window is still unsatisfied
        let needMismatch = false;
        const forbid = new Set();
        for (const start of endsAt[pos]) {
            const win = windowInfo[start];
            if (!win.mismatched) {
                needMismatch = true;
                const offset = pos - start; // 0..m-1
                forbid.add(str2[offset]);
            }
        }
        if (needMismatch) {
            if (s[pos] !== '') {
                // already fixed, must be mismatching for all unsatisfied windows
                let ok = true;
                for (const start of endsAt[pos]) {
                    const win = windowInfo[start];
                    if (!win.mismatched) {
                        const offset = pos - start;
                        if (s[pos] === str2[offset]) { ok = false; break; }
                    }
                }
                if (!ok) return "";
            } else {
                // choose smallest char not in forbid
                let chosen = '';
                for (let code = 97; code <= 122; ++code) {
                    const ch = String.fromCharCode(code);
                    if (!forbid.has(ch)) { chosen = ch; break; }
                }
                if (chosen === '') return ""; // no possible character
                s[pos] = chosen;
            }
        } else {
            if (s[pos] === '') s[pos] = 'a';
        }
        propagate(pos);
    }
    // Final verification
    for (let i = 0; i < n; ++i) {
        if (str1[i] === 'F' && !windowInfo[i].mismatched) return "";
    }
    return s.join('');
};
```

## Typescript

```typescript
function generateString(str1: string, str2: string): string {
    const n = str1.length;
    const m = str2.length;
    const L = n + m - 1;

    // Step 1: apply forced characters from 'T' windows
    const fixed: (string | undefined)[] = new Array(L);
    for (let i = 0; i < n; ++i) {
        if (str1[i] === 'T') {
            for (let j = 0; j < m; ++j) {
                const pos = i + j;
                const ch = str2[j];
                if (fixed[pos] !== undefined && fixed[pos] !== ch) return "";
                fixed[pos] = ch;
            }
        }
    }

    // Step 2: build KMP prefix function for pattern str2
    const pi = new Array(m).fill(0);
    for (let i = 1; i < m; ++i) {
        let k = pi[i - 1];
        while (k > 0 && str2[i] !== str2[k]) k = pi[k - 1];
        if (str2[i] === str2[k]) ++k;
        pi[i] = k;
    }

    // Step 3: build transition table trans[state][charIdx]
    const trans: number[][] = Array.from({ length: m }, () => new Array(26).fill(0));
    for (let state = 0; state < m; ++state) {
        for (let c = 0; c < 26; ++c) {
            const ch = String.fromCharCode(97 + c);
            let k = state;
            while (k > 0 && ch !== str2[k]) k = pi[k - 1];
            if (ch === str2[k]) ++k;
            trans[state][c] = k; // may be m
        }
    }

    // Step 4: DP from end to start, dp[pos][state] stored in flat Uint8Array
    const dp = new Uint8Array((L + 1) * m);
    for (let s = 0; s < m; ++s) dp[L * m + s] = 1; // base: any state is acceptable at the end

    for (let pos = L - 1; pos >= 0; --pos) {
        const forcedChar = fixed[pos];
        for (let state = 0; state < m; ++state) {
            let ok = false;
            if (forcedChar !== undefined) {
                const cIdx = forcedChar.charCodeAt(0) - 97;
                let ns = trans[state][cIdx];
                if (ns === m) {
                    const start = pos - m + 1;
                    if (start >= 0 && str1[start] === 'T') {
                        ns = pi[m - 1];
                        if (dp[(pos + 1) * m + ns]) ok = true;
                    }
                } else {
                    if (dp[(pos + 1) * m + ns]) ok = true;
                }
            } else {
                for (let cIdx = 0; cIdx < 26; ++cIdx) {
                    let ns = trans[state][cIdx];
                    if (ns === m) {
                        const start = pos - m + 1;
                        if (start >= 0 && str1[start] === 'T') {
                            ns = pi[m - 1];
                        } else continue;
                    }
                    if (dp[(pos + 1) * m + ns]) { ok = true; break; }
                }
            }
            dp[pos * m + state] = ok ? 1 : 0;
        }
    }

    if (!dp[0]) return "";

    // Step 5: reconstruct lexicographically smallest string
    const result: string[] = new Array(L);
    let curState = 0;
    for (let pos = 0; pos < L; ++pos) {
        const forcedChar = fixed[pos];
        let chosen = '';
        if (forcedChar !== undefined) {
            chosen = forcedChar;
        } else {
            for (let cIdx = 0; cIdx < 26; ++cIdx) {
                let ns = trans[curState][cIdx];
                if (ns === m) {
                    const start = pos - m + 1;
                    if (start >= 0 && str1[start] === 'T') {
                        ns = pi[m - 1];
                    } else continue;
                }
                if (dp[(pos + 1) * m + ns]) {
                    chosen = String.fromCharCode(97 + cIdx);
                    break;
                }
            }
        }
        result[pos] = chosen;
        // update state for next position
        let ns = trans[curState][chosen.charCodeAt(0) - 97];
        if (ns === m) {
            const start = pos - m + 1;
            // this must be a valid 'T' window; we already ensured it.
            ns = pi[m - 1];
        }
        curState = ns;
    }

    return result.join('');
}
```

## Php

```php
class Solution {
    /**
     * @param String $str1
     * @param String $str2
     * @return String
     */
    function generateString($str1, $str2) {
        $n = strlen($str1);
        $m = strlen($str2);
        $L = $n + $m - 1;
        // build failure function for str2
        $fail = array_fill(0, $m, 0);
        for ($i = 1; $i < $m; $i++) {
            $j = $fail[$i - 1];
            while ($j > 0 && $str2[$i] !== $str2[$j]) {
                $j = $fail[$j - 1];
            }
            if ($str2[$i] === $str2[$j]) $j++;
            $fail[$i] = $j;
        }
        // build transition table
        $next = array_fill(0, $m + 1, []);
        for ($state = 0; $state <= $m; $state++) {
            for ($ci = 0; $ci < 26; $ci++) {
                $c = chr(ord('a') + $ci);
                if ($state == $m) {
                    $k = $fail[$m - 1];
                } else {
                    $k = $state;
                }
                while ($k > 0 && $c !== $str2[$k]) {
                    $k = $fail[$k - 1];
                }
                if ($k < $m && $c === $str2[$k]) $k++;
                $next[$state][$ci] = $k;
            }
        }
        // constraints on ending positions
        $needEqual = [];
        for ($i = 0; $i < $n; $i++) {
            $end = $i + $m - 1;
            $needEqual[$end] = ($str1[$i] === 'T');
        }
        // forward DP: reachable states after each position
        $dp = array_fill(0, $L, []);
        $prev = [0 => true];
        for ($pos = 0; $pos < $L; $pos++) {
            $curr = [];
            foreach ($prev as $state => $_) {
                for ($ci = 0; $ci < 26; $ci++) {
                    $t = $next[$state][$ci];
                    if (isset($needEqual[$pos])) {
                        if ($needEqual[$pos]) {
                            if ($t != $m) continue;
                        } else {
                            if ($t == $m) continue;
                        }
                    }
                    $curr[$t] = true;
                }
            }
            $dp[$pos] = $curr;
            $prev = $curr;
            if (empty($prev)) return "";
        }
        // backward DP: states after position that can lead to a solution
        $back = array_fill(0, $L, []);
        $back[$L - 1] = $dp[$L - 1];
        for ($pos = $L - 2; $pos >= 0; $pos--) {
            $set = [];
            foreach ($dp[$pos] as $s => $_) {
                for ($ci = 0; $ci < 26; $ci++) {
                    $t = $next[$s][$ci];
                    $np = $pos + 1;
                    if (isset($needEqual[$np])) {
                        if ($needEqual[$np]) {
                            if ($t != $m) continue;
                        } else {
                            if ($t == $m) continue;
                        }
                    }
                    if (isset($back[$np][$t])) {
                        $set[$s] = true;
                        break;
                    }
                }
            }
            $back[$pos] = $set;
        }
        // construct lexicographically smallest string
        $state = 0;
        $result = '';
        for ($pos = 0; $pos < $L; $pos++) {
            for ($ci = 0; $ci < 26; $ci++) {
                $t = $next[$state][$ci];
                if (isset($needEqual[$pos])) {
                    if ($needEqual[$pos]) {
                        if ($t != $m) continue;
                    } else {
                        if ($t == $m) continue;
                    }
                }
                if (!isset($back[$pos][$t])) continue;
                $result .= chr(ord('a') + $ci);
                $state = $t;
                break;
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func generateString(_ str1: String, _ str2: String) -> String {
        let n = str1.count
        let m = str2.count
        let L = n + m - 1
        var s1 = Array(str1)
        var s2 = Array(str2)
        var word = [Character?](repeating: nil, count: L)

        // Apply T constraints
        for i in 0..<n where s1[i] == "T" {
            for j in 0..<m {
                let pos = i + j
                let c = s2[j]
                if let existing = word[pos], existing != c {
                    return ""
                }
                word[pos] = c
            }
        }

        // Intervals for F positions
        struct Interval { var start: Int; var end: Int }
        var intervals = [Interval]()
        var intervalIndexForPos = [[Int]](repeating: [], count: L)

        for i in 0..<n where s1[i] == "F" {
            let st = i
            let en = i + m - 1
            let idx = intervals.count
            intervals.append(Interval(start: st, end: en))
            if st <= en && en < L {
                for p in st...en {
                    intervalIndexForPos[p].append(idx)
                }
            }
        }

        let fCount = intervals.count
        var satisfied = [Bool](repeating: false, count: fCount)
        var availCnt = [Int](repeating: 0, count: fCount)

        // Initialize satisfied and available counts
        for idx in 0..<fCount {
            let iv = intervals[idx]
            var sat = false
            var cnt = 0
            for p in iv.start...iv.end {
                if let ch = word[p] {
                    if ch != s2[p - iv.start] {
                        sat = true
                        break
                    }
                } else {
                    cnt += 1
                }
            }
            satisfied[idx] = sat
            availCnt[idx] = cnt
        }

        let letters = Array("abcdefghijklmnopqrstuvwxyz")
        // Build the word greedily
        for pos in 0..<L {
            if word[pos] != nil { continue }

            var forcedForbidden = Set<Character>()
            var mustMismatch = false

            for idx in intervalIndexForPos[pos] {
                if satisfied[idx] { continue }
                if availCnt[idx] == 1 {
                    let forb = s2[pos - intervals[idx].start]
                    forcedForbidden.insert(forb)
                    mustMismatch = true
                }
            }

            var chosen: Character? = nil
            if mustMismatch {
                for ch in letters {
                    if !forcedForbidden.contains(ch) {
                        chosen = ch
                        break
                    }
                }
                if chosen == nil { return "" } // impossible
            } else {
                chosen = "a"
            }

            let c = chosen!
            word[pos] = c

            // Update intervals covering this position
            for idx in intervalIndexForPos[pos] {
                if satisfied[idx] { continue }
                let forb = s2[pos - intervals[idx].start]
                if c != forb {
                    satisfied[idx] = true
                } else {
                    availCnt[idx] -= 1
                }
            }
        }

        // Verify all F intervals are satisfied
        for i in 0..<fCount where !satisfied[i] {
            return ""
        }

        // Fill any remaining nil (should not happen) with 'a'
        var resultChars = [Character]()
        resultChars.reserveCapacity(L)
        for chOpt in word {
            resultChars.append(chOpt ?? "a")
        }
        return String(resultChars)
    }
}
```

## Kotlin

```kotlin
import java.util.*

class Solution {
    fun generateString(str1: String, str2: String): String {
        val n = str1.length
        val m = str2.length
        val L = n + m - 1
        val forced = CharArray(L) { '\u0000' }

        // Apply T constraints
        for (i in 0 until n) {
            if (str1[i] == 'T') {
                for (j in 0 until m) {
                    val pos = i + j
                    val ch = str2[j]
                    val cur = forced[pos]
                    if (cur != '\u0000' && cur != ch) return ""
                    forced[pos] = ch
                }
            }
        }

        // Prepare windows for F constraints
        data class Window(var start: Int, var mismatched: Boolean, var potential: Int)

        val windows = mutableListOf<Window>()
        val cover = Array(L) { mutableListOf<Int>() }

        for (i in 0 until n) {
            if (str1[i] == 'F') {
                var mismatched = false
                // check if any forced char already causes mismatch
                loop@ for (j in 0 until m) {
                    val pos = i + j
                    val f = forced[pos]
                    val pat = str2[j]
                    if (f != '\u0000' && f != pat) {
                        mismatched = true
                        break@loop
                    }
                }
                var potential = 0
                if (!mismatched) {
                    for (j in 0 until m) {
                        val pos = i + j
                        if (forced[pos] == '\u0000') potential++
                    }
                    if (potential == 0) return ""
                }
                val idx = windows.size
                windows.add(Window(i, mismatched, potential))
                for (j in 0 until m) {
                    cover[i + j].add(idx)
                }
            }
        }

        val ans = CharArray(L)

        // Helper to apply character to windows, returns false if impossible
        fun apply(pos: Int, c: Char): Boolean {
            for (wIdx in cover[pos]) {
                val win = windows[wIdx]
                if (win.mismatched) continue
                val offset = pos - win.start
                if (c != str2[offset]) {
                    win.mismatched = true
                } else {
                    win.potential--
                    if (win.potential == 0) return false
                }
            }
            return true
        }

        for (pos in 0 until L) {
            val forcedChar = forced[pos]
            if (forcedChar != '\u0000') {
                if (!apply(pos, forcedChar)) return ""
                ans[pos] = forcedChar
            } else {
                // Determine forbidden letters due to windows that need mismatch now
                val forbid = BooleanArray(26)
                for (wIdx in cover[pos]) {
                    val win = windows[wIdx]
                    if (win.mismatched) continue
                    if (win.potential == 1) {
                        val offset = pos - win.start
                        val patChar = str2[offset]
                        forbid[patChar - 'a'] = true
                    }
                }
                var chosen = 'a'
                while (chosen <= 'z' && forbid[chosen - 'a']) chosen++
                if (chosen > 'z') return ""
                if (!apply(pos, chosen)) return ""
                ans[pos] = chosen
            }
        }

        // Final verification (optional)
        for (win in windows) {
            if (!win.mismatched) return ""
        }

        return String(ans)
    }
}
```

## Dart

```dart
class Solution {
  String generateString(String str1, String str2) {
    int n = str1.length;
    int m = str2.length;
    int L = n + m - 1;

    // forced characters from 'T' windows
    List<String?> forced = List.filled(L, null);
    for (int i = 0; i < n; ++i) {
      if (str1.codeUnitAt(i) == 84) { // 'T'
        for (int j = 0; j < m; ++j) {
          int pos = i + j;
          String need = String.fromCharCode(str2.codeUnitAt(j));
          if (forced[pos] != null && forced[pos] != need) return "";
          forced[pos] = need;
        }
      }
    }

    // collect 'F' windows
    List<int> fStart = [];
    List<bool> sat = [];   // already has a mismatch
    List<int> flex = [];   // remaining flexible positions (only for unsatisfied)
    for (int i = 0; i < n; ++i) {
      if (str1.codeUnitAt(i) == 70) { // 'F'
        bool satisfied = false;
        int cntFlex = 0;
        for (int j = 0; j < m; ++j) {
          int pos = i + j;
          String? fch = forced[pos];
          String need = String.fromCharCode(str2.codeUnitAt(j));
          if (fch != null && fch != need) {
            satisfied = true;
            break;
          }
        }
        if (!satisfied) {
          for (int j = 0; j < m; ++j) {
            int pos = i + j;
            if (forced[pos] == null) cntFlex++;
          }
        }
        fStart.add(i);
        sat.add(satisfied);
        flex.add(cntFlex);
      }
    }

    StringBuffer sb = StringBuffer();

    for (int p = 0; p < L; ++p) {
      String ch;
      if (forced[p] != null) {
        ch = forced[p]!;
      } else {
        // Determine mandatory mismatches
        Set<int> mustDiff = {};
        bool needDiff = false;
        for (int idx = 0; idx < fStart.length; ++idx) {
          int start = fStart[idx];
          int end = start + m - 1;
          if (p < start || p > end) continue;
          if (sat[idx]) continue;
          int remaining = flex[idx];
          if (remaining == 0) return "";
          if (remaining == 1) {
            needDiff = true;
            mustDiff.add(str2.codeUnitAt(p - start));
          }
        }

        if (needDiff) {
          // pick smallest letter not in mustDiff
          int chosen = 97; // 'a'
          for (int code = 97; code <= 122; ++code) {
            if (!mustDiff.contains(code)) {
              chosen = code;
              break;
            }
          }
          ch = String.fromCharCode(chosen);
        } else {
          ch = 'a';
        }
      }

      sb.write(ch);

      // Update windows covering position p
      for (int idx = 0; idx < fStart.length; ++idx) {
        int start = fStart[idx];
        int end = start + m - 1;
        if (p < start || p > end) continue;
        if (sat[idx]) continue;

        int offset = p - start;
        String need = String.fromCharCode(str2.codeUnitAt(offset));
        if (ch != need) {
          sat[idx] = true;
        } else {
          // matched, reduce flexibility only if this position was not forced
          if (forced[p] == null) {
            flex[idx]--;
            if (flex[idx] == 0) return "";
          }
        }
      }
    }

    // All constraints satisfied by construction
    return sb.toString();
  }
}
```

## Golang

```go
func generateString(str1 string, str2 string) string {
    n := len(str1)
    m := len(str2)
    L := n + m - 1
    chars := make([]byte, L)
    fixed := make([]bool, L)

    // Apply 'T' constraints
    for i := 0; i < n; i++ {
        if str1[i] == 'T' {
            for j := 0; j < m; j++ {
                pos := i + j
                c := str2[j]
                if fixed[pos] && chars[pos] != c {
                    return ""
                }
                chars[pos] = c
                fixed[pos] = true
            }
        }
    }

    // Fill remaining positions with 'a'
    for p := 0; p < L; p++ {
        if !fixed[p] {
            chars[p] = 'a'
        }
    }

    // Process 'F' constraints
    for i := 0; i < n; i++ {
        if str1[i] != 'F' {
            continue
        }
        broken := false
        for j := 0; j < m; j++ {
            pos := i + j
            if chars[pos] != str2[j] {
                broken = true
                break
            }
        }
        if broken {
            continue
        }

        // Need to introduce a mismatch: pick rightmost mutable position
        found := -1
        offset := 0
        for j := m - 1; j >= 0; j-- {
            pos := i + j
            if fixed[pos] {
                continue
            }
            found = pos
            offset = j
            break
        }
        if found == -1 {
            return ""
        }

        needChar := str2[offset]
        newc := byte('a')
        if needChar == 'a' {
            newc = 'b'
        }
        chars[found] = newc
    }

    return string(chars)
}
```

## Ruby

```ruby
def generate_string(str1, str2)
  n = str1.length
  m = str2.length
  l = n + m - 1
  word = Array.new(l)

  # Apply 'T' constraints
  (0...n).each do |i|
    next unless str1[i] == 'T'
    (0...m).each do |k|
      pos = i + k
      ch = str2[k]
      if word[pos] && word[pos] != ch
        return ""
      end
      word[pos] = ch
    end
  end

  # Collect starts of 'F' windows
  f_starts = []
  (0...n).each { |i| f_starts << i if str1[i] == 'F' }
  f_cnt = f_starts.size

  windows = Array.new(f_cnt) { { remaining: 0, mismatch: false } }
  pos_to_windows = Array.new(l) { [] }

  # Initialize windows
  f_starts.each_with_index do |start, idx|
    remaining = 0
    mismatch = false
    (0...m).each do |k|
      pos = start + k
      c = word[pos]
      if c.nil?
        remaining += 1
      else
        if c != str2[k]
          mismatch = true
          break
        end
      end
    end

    if mismatch
      windows[idx][:mismatch] = true
      next
    end

    return "" if remaining == 0

    windows[idx][:remaining] = remaining
    (0...m).each do |k|
      pos = start + k
      pos_to_windows[pos] << idx if word[pos].nil?
    end
  end

  # Fill remaining positions greedily
  (0...l).each do |pos|
    next if word[pos]

    assigned = nil
    ('a'..'z').each do |ch|
      ok = true
      pos_to_windows[pos].each do |w_idx|
        win = windows[w_idx]
        next if win[:mismatch]
        offset = pos - f_starts[w_idx]
        required = str2[offset]
        if ch == required
          ok = false if win[:remaining] - 1 == 0
        end
        break unless ok
      end

      if ok
        assigned = ch
        word[pos] = ch
        pos_to_windows[pos].each do |w_idx|
          win = windows[w_idx]
          next if win[:mismatch]
          offset = pos - f_starts[w_idx]
          required = str2[offset]
          win[:remaining] -= 1
          win[:mismatch] = true if ch != required
        end
        break
      end
    end

    return "" unless assigned
  end

  word.join
end
```

## Scala

```scala
object Solution {
  def generateString(str1: String, str2: String): String = {
    val n = str1.length
    val m = str2.length
    val L = n + m - 1
    val res = Array.fill[Char](L)('?')

    // Apply 'T' constraints
    var i = 0
    while (i < n) {
      if (str1.charAt(i) == 'T') {
        var j = 0
        while (j < m) {
          val pos = i + j
          val ch = str2.charAt(j)
          if (res(pos) == '?') res(pos) = ch
          else if (res(pos) != ch) return ""
          j += 1
        }
      }
      i += 1
    }

    // Collect 'F' intervals
    val fStarts = new scala.collection.mutable.ArrayBuffer[Int]()
    i = 0
    while (i < n) {
      if (str1.charAt(i) == 'F') fStarts += i
      i += 1
    }
    val intervalCount = fStarts.length
    val broken = Array.fill[Boolean](intervalCount)(false)

    // Map positions to intervals that cover them
    val posIntervals = Array.fill[L](new scala.collection.mutable.ArrayBuffer[Int]())
    var idx = 0
    while (idx < intervalCount) {
      val start = fStarts(idx)
      var j = 0
      while (j < m) {
        val pos = start + j
        posIntervals(pos).append(idx)
        j += 1
      }
      idx += 1
    }

    // Build the result string left to right
    var pos = 0
    while (pos < L) {
      if (res(pos) == '?') {
        // Determine forbidden letters for intervals ending here that are still unbroken
        val forbid = new Array[Boolean](26)
        val it = posIntervals(pos).iterator
        while (it.hasNext) {
          val id = it.next()
          if (!broken(id) && fStarts(id) + m - 1 == pos) {
            val offset = pos - fStarts(id)
            forbid(str2.charAt(offset) - 'a') = true
          }
        }
        var chosen: Char = 0
        var c = 0
        while (c < 26 && chosen == 0) {
          if (!forbid(c)) chosen = ('a' + c).toChar
          c += 1
        }
        if (chosen == 0) return ""
        res(pos) = chosen
      } else {
        // Verify that a fixed character does not violate the last‑position requirement
        val cur = res(pos)
        val it = posIntervals(pos).iterator
        while (it.hasNext) {
          val id = it.next()
          if (!broken(id) && fStarts(id) + m - 1 == pos) {
            val offset = pos - fStarts(id)
            if (cur == str2.charAt(offset)) return ""
          }
        }
      }

      // Update broken status for intervals covering this position
      val ch = res(pos)
      val it2 = posIntervals(pos).iterator
      while (it2.hasNext) {
        val id = it2.next()
        if (!broken(id)) {
          val offset = pos - fStarts(id)
          if (ch != str2.charAt(offset)) broken(id) = true
        }
      }

      pos += 1
    }

    // Ensure all 'F' intervals are satisfied
    idx = 0
    while (idx < intervalCount) {
      if (!broken(idx)) return ""
      idx += 1
    }

    new String(res)
  }
}
```

## Rust

```rust
use std::cmp::{min, max};

impl Solution {
    pub fn generate_string(str1: String, str2: String) -> String {
        let s1 = str1.as_bytes();
        let s2 = str2.as_bytes();
        let n = s1.len();
        let m = s2.len();
        if n == 0 || m == 0 {
            return "".to_string();
        }
        let l = n + m - 1;
        // word positions, None means not fixed yet
        let mut word: Vec<Option<u8>> = vec![None; l];
        // apply T constraints
        for i in 0..n {
            if s1[i] == b'T' {
                for j in 0..m {
                    let pos = i + j;
                    let ch = s2[j];
                    match word[pos] {
                        Some(existing) => {
                            if existing != ch {
                                return "".to_string();
                            }
                        }
                        None => word[pos] = Some(ch),
                    }
                }
            }
        }

        // identify F starts
        let mut is_f: Vec<bool> = vec![false; n];
        for i in 0..n {
            if s1[i] == b'F' {
                is_f[i] = true;
            }
        }
        let mut mismatch: Vec<bool> = vec![false; n];

        // build the final string
        for p in 0..l {
            // range of start indices whose window covers position p
            let start_idx = if p + 1 >= m { p + 1 - m } else { 0 };
            let end_idx = min(p, n - 1);
            // forbidden characters because some F-window ending here still has no mismatch yet
            let mut forbid = [false; 26];
            for i in start_idx..=end_idx {
                if !is_f[i] {
                    continue;
                }
                let offset = p - i;
                if offset == m - 1 && !mismatch[i] {
                    let idx = (s2[offset] - b'a') as usize;
                    forbid[idx] = true;
                }
            }

            // decide character for this position
            let chosen: u8;
            if let Some(ch) = word[p] {
                let idx = (ch - b'a') as usize;
                if forbid[idx] {
                    return "".to_string();
                }
                chosen = ch;
            } else {
                // pick smallest allowed character
                let mut c_opt = None;
                for c in b'a'..=b'z' {
                    if !forbid[(c - b'a') as usize] {
                        c_opt = Some(c);
                        break;
                    }
                }
                match c_opt {
                    Some(c) => {
                        chosen = c;
                        word[p] = Some(c);
                    }
                    None => return "".to_string(),
                }
            }

            // update mismatch info for all active F-windows
            for i in start_idx..=end_idx {
                if !is_f[i] || mismatch[i] {
                    continue;
                }
                let offset = p - i;
                if chosen != s2[offset] {
                    mismatch[i] = true;
                }
            }
        }

        // final verification (optional)
        for i in 0..n {
            if is_f[i] && !mismatch[i] {
                return "".to_string();
            }
        }

        let result: String = word.iter().map(|&c| c.unwrap() as char).collect();
        result
    }
}
```

## Racket

```racket
(define/contract (generate-string str1 str2)
  (-> string? string? string?)
  (let* ([n (string-length str1)]
         [m (string-length str2)]
         [len (+ n m -1)]
         [vec (make-vector len #\?)])
    ;; apply T constraints
    (let loop-t ([i 0])
      (when (< i n)
        (when (char=? (string-ref str1 i) #\T)
          (let inner ([j 0])
            (when (< j m)
              (let* ([pos (+ i j)]
                     [need (string-ref str2 j)]
                     [cur (vector-ref vec pos)])
                (cond [(and (not (char=? cur #\?)) (not (char=? cur need)))
                       (begin
                         (set! vec #f) ; mark impossible
                         (return ""))]
                      [else (vector-set! vec pos need)])
                (inner (+ j 1)))))
          )
        (loop-t (+ i 1))))
    (when (eq? vec #f) (return ""))
    ;; process F intervals
    (let loop-f ([i 0])
      (when (< i n)
        (when (char=? (string-ref str1 i) #\F)
          (define l i)
          (define r (+ i m -1))
          ;; check if already satisfied
          (define satisfied? #f)
          (for ([pos (in-range l (+ r 1))])
            (let* ([cur (vector-ref vec pos)]
                   [pat (string-ref str2 (- pos l))])
              (when (and (not (char=? cur #\?))
                         (not (char=? cur pat)))
                (set! satisfied? #t)
                (break))))
          (unless satisfied?
            ;; find rightmost breakable position
            (define break-pos -1)
            (for ([pos (in-range r (- l 1) -1)])
              (when (char=? (vector-ref vec pos) #\?)
                (set! break-pos pos)
                (break)))
            (if (= break-pos -1)
                (return "")
                (let* ([pat (string-ref str2 (- break-pos l))]
                       [newch (if (char=? pat #\a) #\b #\a)])
                  (vector-set! vec break-pos newch)))))
        (loop-f (+ i 1))))
    ;; fill remaining '?' with 'a'
    (for ([idx (in-range len)])
      (when (char=? (vector-ref vec idx) #\?)
        (vector-set! vec idx #\a)))
    ;; build result string
    (list->string
     (for/list ([idx (in-range len)]) (vector-ref vec idx)))))
```

## Erlang

```erlang
-export([generate_string/2]).
-spec generate_string(Str1 :: unicode:unicode_binary(), Str2 :: unicode:unicode_binary()) -> unicode:unicode_binary().
generate_string(Str1, Str2) ->
    try
        S1 = binary_to_list(Str1),
        S2 = binary_to_list(Str2),
        N = length(S1),
        M = length(S2),
        L = N + M - 1,
        %% initial array with placeholder {$?, false}
        Arr0 = array:new(L, [{default, {$?, false}}]),
        %% apply all 'T' constraints
        Arr1 = apply_T_constraints(0, S1, S2, M, Arr0),
        %% fill unfixed positions with 'a'
        Arr2 = fill_defaults(0, L, Arr1),
        %% process 'F' constraints
        Arr3 = apply_F_constraints(0, S1, S2, M, Arr2),
        %% build result string
        list_to_binary(build_result(0, L, Arr3, []))
    catch
        throw:conflict -> <<>>
    end.

%% Apply all 'T' constraints
apply_T_constraints(_, [], _, _, Arr) ->
    Arr;
apply_T_constraints(Index, [C|Rest], S2, M, Arr) ->
    case C of
        $T ->
            Arr1 = apply_single_T(Index, 0, S2, Arr),
            apply_T_constraints(Index + 1, Rest, S2, M, Arr1);
        _ -> % 'F'
            apply_T_constraints(Index + 1, Rest, S2, M, Arr)
    end.

apply_single_T(_, _, [], Arr) ->
    Arr;
apply_single_T(I, J, [D|Ds], Arr) ->
    Pos = I + J,
    {CharPrev, FixedPrev} = get_elem(Pos, Arr),
    case FixedPrev of
        true when CharPrev =/= D -> throw(conflict);
        _ ->
            Arr1 = set_fixed_char(Pos, D, Arr),
            apply_single_T(I, J + 1, Ds, Arr1)
    end.

%% Fill unfixed positions with 'a'
fill_defaults(Index, L, Arr) when Index == L ->
    Arr;
fill_defaults(Index, L, Arr) ->
    {_, Fixed} = get_elem(Index, Arr),
    Arr1 = case Fixed of
        true -> Arr;
        false -> array:set(Index + 1, {$a, false}, Arr)
    end,
    fill_defaults(Index + 1, L, Arr1).

%% Apply all 'F' constraints
apply_F_constraints(_, [], _, _, Arr) ->
    Arr;
apply_F_constraints(Index, [C|Rest], S2, M, Arr) ->
    case C of
        $F ->
            case substring_equal(Index, 0, M, S2, Arr) of
                true -> % need to break this window
                    Arr1 = break_window(Index, M - 1, S2, Arr),
                    apply_F_constraints(Index + 1, Rest, S2, M, Arr1);
                false ->
                    apply_F_constraints(Index + 1, Rest, S2, M, Arr)
            end;
        _ -> % 'T'
            apply_F_constraints(Index + 1, Rest, S2, M, Arr)
    end.

%% Check if substring starting at I equals S2
substring_equal(_, J, M, _, _) when J == M ->
    true;
substring_equal(I, J, M, S2, Arr) ->
    Desired = lists:nth(J + 1, S2),
    Pos = I + J,
    {Char, _} = get_elem(Pos, Arr),
    if Char =:= Desired -> substring_equal(I, J + 1, M, S2, Arr);
       true -> false
    end.

%% Break a violating window by modifying the rightmost flexible position
break_window(I, Off, S2, Arr) when Off < 0 ->
    throw(conflict);
break_window(I, Off, S2, Arr) ->
    Pos = I + Off,
    {_, Fixed} = get_elem(Pos, Arr),
    case Fixed of
        false ->
            Desired = lists:nth(Off + 1, S2),
            NewChar = smallest_diff_char(Desired),
            set_fixed_char(Pos, NewChar, Arr);
        true ->
            break_window(I, Off - 1, S2, Arr)
    end.

%% Find the smallest lowercase letter different from D
smallest_diff_char(D) ->
    smallest_diff_char($a, D).

smallest_diff_char(C, D) when C =< $z ->
    if C =/= D -> C;
       true -> smallest_diff_char(C + 1, D)
    end.

%% Helpers for array access (0‑based index)
get_elem(Pos, Arr) ->
    array:get(Pos + 1, Arr).

set_fixed_char(Pos, Char, Arr) ->
    array:set(Pos + 1, {Char, true}, Arr).

%% Build final binary string
build_result(Index, L, _Arr, Acc) when Index == L ->
    lists:reverse(Acc);
build_result(Index, L, Arr, Acc) ->
    {Char, _} = get_elem(Index, Arr),
    build_result(Index + 1, L, Arr, [Char | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec generate_string(str1 :: String.t(), str2 :: String.t()) :: String.t()
  def generate_string(str1, str2) do
    s1 = String.to_charlist(str1)
    s2 = String.to_charlist(str2)
    n = length(s1)
    m = length(s2)
    l = n + m - 1

    # apply forced characters from 'T' positions
    forced = %{}
    forced =
      Enum.reduce(0..(n - 1), forced, fn i, acc ->
        if Enum.at(s1, i) == ?T do
          Enum.reduce(0..(m - 1), acc, fn j, a2 ->
            pos = i + j
            ch = Enum.at(s2, j)
            case Map.get(a2, pos) do
              nil -> Map.put(a2, pos, ch)
              ^ch -> a2
              _ -> :conflict
            end
          end)
        else
          acc
        end
      end)

    if forced == :conflict do
      ""
    else
      # build KMP failure function
      fail =
        Enum.reduce(1..(m - 1), List.duplicate(0, m), fn i, f ->
          j = Enum.at(f, i - 1)
          while j > 0 and Enum.at(s2, j) != Enum.at(s2, i) do
            j = Enum.at(f, j - 1)
          end
          if Enum.at(s2, j) == Enum.at(s2, i), do: List.replace_at(f, i, j + 1), else: f
        end)

      # transition table for states 0..m-1 and letters a..z
      trans =
        for state <- 0..(m - 1) do
          for code <- ?a..?z do
            ns = state
            ns =
              cond do
                ns == m -> ns
                true ->
                  while ns > 0 and Enum.at(s2, ns) != code do
                    ns = Enum.at(fail, ns - 1)
                  end

                  if Enum.at(s2, ns) == code, do: ns + 1, else: ns
              end

            ns
          end
          |> List.to_tuple()
        end
        |> List.to_tuple()

      # DP rows from position l down to 0
      dp_next = List.duplicate(true, m)
      rows_rev = []

      rows_rev =
        Enum.reduce((l - 1)..0, {dp_next, rows_rev}, fn pos, {next_row, acc_rows} ->
          row = List.duplicate(false, m)

          row =
            Enum.reduce(0..(m - 1), row, fn state, cur_row ->
              possible =
                if Map.has_key?(forced, pos) do
                  [Map.get(forced, pos)]
                else
                  ?a..?z |> Enum.to_list()
                end
                |> Enum.any?(fn c ->
                  ns = elem(elem(trans, state), c - ?a)

                  cond do
                    ns == m ->
                      start = pos - m + 1

                      if start >= 0 and start < n and Enum.at(s1, start) == ?T do
                        ns2 = Enum.at(fail, m - 1)
                        Enum.at(next_row, ns2)
                      else
                        false
                      end

                    true ->
                      Enum.at(next_row, ns)
                  end
                end)

              List.replace_at(cur_row, state, possible)
            end)

          {row, [row | acc_rows]}
        end)
        |> elem(1)

      rows = Enum.reverse(rows_rev)

      # construct answer greedily using DP table
      result =
        0..(l - 1)
        |> Enum.reduce({[], 0}, fn pos, {chars_acc, state} ->
          candidates =
            if Map.has_key?(forced, pos) do
              [Map.get(forced, pos)]
            else
              ?a..?z |> Enum.to_list()
            end

          chosen =
            Enum.find(candidates, fn c ->
              ns = elem(elem(trans, state), c - ?a)

              cond do
                ns == m ->
                  start = pos - m + 1

                  if start >= 0 and start < n and Enum.at(s1, start) == ?T do
                    ns2 = Enum.at(fail, m - 1)
                    Enum.at(Enum.at(rows, pos + 1), ns2)
                  else
                    false
                  end

                true ->
                  Enum.at(Enum.at(rows, pos + 1), ns)
              end
            end)

          if chosen == nil do
            throw(:impossible)
          else
            new_state =
              let ns = elem(elem(trans, state), chosen - ?a) in
                if ns == m, do: Enum.at(fail, m - 1), else: ns

            {[chosen | chars_acc], new_state}
          end
        end)

      case result do
        {chars_rev, _state} ->
          chars_rev |> Enum.reverse() |> to_string()
      catch
        :impossible -> ""
      end
    end
  end
end
```
