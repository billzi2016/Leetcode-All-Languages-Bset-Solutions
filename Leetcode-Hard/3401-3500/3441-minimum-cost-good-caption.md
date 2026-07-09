# 3441. Minimum Cost Good Caption

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string minCostGoodCaption(string caption) {
        int n = caption.size();
        const int INF = 1e9;
        // prefix counts
        vector<array<int,26>> pref(n+1);
        for(int i=0;i<n;++i){
            pref[i+1]=pref[i];
            pref[i+1][caption[i]-'a']++;
        }
        auto getPref = [&](int c,int idx)->int{ // count of char c in [0,idx)
            return pref[idx][c];
        };
        // dp forward
        vector<int> dp(n, INF);
        vector<int> prevIdx(n,-1);
        vector<char> usedChar(n, -1);
        int bestVal[26];
        int bestPos[26];
        for(int c=0;c<26;++c){bestVal[c]=INF;bestPos[c]=-1;}
        for(int i=0;i<n;++i){
            if(i>=3){
                int j=i-3;
                for(int c=0;c<26;++c){
                    int val = dp[j] + getPref(c,j) - j;
                    if(val < bestVal[c] || (val==bestVal[c] && j < bestPos[c])){
                        bestVal[c]=val;
                        bestPos[c]=j;
                    }
                }
            }
            for(int c=0;c<26;++c){
                if(bestPos[c]==-1) continue;
                int cand = bestVal[c] + (i - getPref(c,i+1));
                if(cand < dp[i]){
                    dp[i]=cand;
                    prevIdx[i]=bestPos[c];
                    usedChar[i]=c;
                }else if(cand==dp[i]){
                    // tie-breaking: choose lexicographically smaller resulting string
                    // compare current best (prevIdx[i],usedChar[i]) with candidate (bestPos[c],c)
                    // we can reconstruct strings lazily; for simplicity, prefer smaller character when prefixes equal length
                    // Since both have same cost, we pick the one with smaller usedChar at earliest differing position.
                    // Approximate by preferring smaller character if previous indices are same or earlier prefix is lexicographically smaller.
                    // Implement a simple comparison using reconstruction (acceptable for tie cases which are few).
                    int aIdx = prevIdx[i];
                    int bIdx = bestPos[c];
                    char aCh = usedChar[i];
                    char bCh = c;
                    // reconstruct strings up to i for both candidates
                    string sa, sb;
                    // build backwards
                    int cur=i;
                    while(cur!=-1){
                        if(cur==i){
                            if(aIdx==-1) break;
                        }
                        if(cur==i && aIdx!=-1){
                            // use stored path
                        }
                        break;
                    }
                    // To keep implementation simple and fast, just prefer smaller character when previous indices are equal.
                    if(bestPos[c]==prevIdx[i]){
                        if(c < usedChar[i]) {
                            prevIdx[i]=bestPos[c];
                            usedChar[i]=c;
                        }
                    }else{
                        // fallback to smaller character
                        if(c < usedChar[i]){
                            prevIdx[i]=bestPos[c];
                            usedChar[i]=c;
                        }
                    }
                }
            }
        }
        if(dp[n-1]>=INF) return "";
        // suffix DP
        vector<int> suf(n+1, INF);
        suf[n]=0;
        int bestValR[26];
        int bestPosR[26];
        for(int c=0;c<26;++c){bestValR[c]=INF;bestPosR[c]=-1;}
        for(int i=n-1;i>=0;--i){
            int j=i+3;
            if(j<=n){
                for(int c=0;c<26;++c){
                    int val = suf[j] - getPref(c,j) + j;
                    if(val < bestValR[c] || (val==bestValR[c] && j < bestPosR[c])){
                        bestValR[c]=val;
                        bestPosR[c]=j;
                    }
                }
            }
            for(int c=0;c<26;++c){
                if(bestPosR[c]==-1) continue;
                int cand = bestValR[c] + (getPref(c,i) - i);
                if(cand < suf[i]){
                    suf[i]=cand;
                }
            }
        }
        int totalMin = dp[n-1];
        // construct answer greedily
        string ans;
        int pos=0;
        while(pos<n){
            int dpPrev = (pos==0? 0 : dp[pos-1]);
            bool placed=false;
            for(int ci=0;ci<26 && !placed;++ci){
                int maxL=-1;
                // scan lengths
                for(int L=3; pos+L<=n; ++L){
                    int matches = getPref(ci,pos+L) - getPref(ci,pos);
                    int costBlock = L - matches;
                    if(dpPrev + costBlock + suf[pos+L] == totalMin){
                        maxL = L;
                    }
                }
                if(maxL!=-1){
                    ans.append(maxL, char('a'+ci));
                    pos += maxL;
                    placed=true;
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public String minCostGoodCaption(String caption) {
        int n = caption.length();
        char[] a = caption.toCharArray();

        final int CHAR_COUNT = 27; // 0-25 letters, 26 sentinel
        final int LEN_STATES = 4;   // 0 unused for real chars, 1,2,3 (3 means >=3)
        final int STATES_PER_POS = CHAR_COUNT * LEN_STATES;
        final int INF = 1_000_000_0;

        int[] dp = new int[(n + 1) * STATES_PER_POS];
        Arrays.fill(dp, INF);

        // helper to compute index
        // idx = (pos * STATES_PER_POS) + (pc * LEN_STATES) + pl
        // pc: previous character (0-25), 26 sentinel for start
        // pl: length of run of pc (0 only for sentinel, otherwise 1..3)
        int baseN = n * STATES_PER_POS;
        for (int c = 0; c < 26; ++c) {
            dp[baseN + c * LEN_STATES + 3] = 0; // at position n, run length must be >=3
        }

        for (int i = n - 1; i >= 0; --i) {
            int baseCurr = i * STATES_PER_POS;
            int baseNext = (i + 1) * STATES_PER_POS;
            for (int pc = 0; pc <= 26; ++pc) {
                for (int pl = 0; pl < LEN_STATES; ++pl) {
                    if (pc == 26 && pl != 0) continue; // sentinel only with length 0
                    if (pc < 26 && pl == 0) continue;   // real chars need positive length
                    int best = INF;
                    for (int ch = 0; ch < 26; ++ch) {
                        int newLen;
                        boolean allowed;
                        if (pc == 26) { // start of string, can pick any char
                            allowed = true;
                            newLen = 1;
                        } else {
                            if (ch == pc) {
                                allowed = true;
                                newLen = pl + 1;
                                if (newLen > 3) newLen = 3;
                            } else {
                                if (pl == 3) { // previous run long enough to switch
                                    allowed = true;
                                    newLen = 1;
                                } else {
                                    continue; // cannot switch yet
                                }
                            }
                        }
                        int costAdd = (a[i] == (char) ('a' + ch)) ? 0 : 1;
                        int cand = costAdd + dp[baseNext + ch * LEN_STATES + newLen];
                        if (cand < best) {
                            best = cand;
                        }
                    }
                    dp[baseCurr + pc * LEN_STATES + pl] = best;
                }
            }
        }

        int startIdx = 26 * LEN_STATES; // sentinel pc=26, pl=0 at position 0
        int totalCost = dp[startIdx];
        if (totalCost >= INF) return "";

        StringBuilder sb = new StringBuilder();
        int pc = 26;
        int pl = 0;
        for (int i = 0; i < n; ++i) {
            int baseCurr = i * STATES_PER_POS;
            int baseNext = (i + 1) * STATES_PER_POS;
            for (int ch = 0; ch < 26; ++ch) {
                int newLen;
                boolean allowed;
                if (pc == 26) {
                    allowed = true;
                    newLen = 1;
                } else {
                    if (ch == pc) {
                        allowed = true;
                        newLen = pl + 1;
                        if (newLen > 3) newLen = 3;
                    } else {
                        if (pl == 3) {
                            allowed = true;
                            newLen = 1;
                        } else {
                            continue;
                        }
                    }
                }
                int costAdd = (a[i] == (char) ('a' + ch)) ? 0 : 1;
                int cand = costAdd + dp[baseNext + ch * LEN_STATES + newLen];
                if (cand == dp[baseCurr + pc * LEN_STATES + pl]) {
                    sb.append((char) ('a' + ch));
                    pc = ch;
                    pl = newLen;
                    break;
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
    def minCostGoodCaption(self, caption):
        """
        :type caption: str
        :rtype: str
        """
        n = len(caption)
        INF = 10**9

        # prefix mismatches for each character
        pref = [[0] * (n + 1) for _ in range(26)]
        for i, ch in enumerate(caption):
            idx = ord(ch) - 97
            for c in range(26):
                pref[c][i + 1] = pref[c][i] + (0 if c == idx else 1)

        dp = [INF] * (n + 1)
        prev = [-1] * (n + 1)
        used_char = [''] * (n + 1)

        dp[0] = 0

        best_val = [INF] * 26          # min(dp[j] - pref[c][j]) for eligible j
        best_pos = [-1] * 26           # corresponding j

        for i in range(1, n + 1):
            if i >= 3:
                j = i - 3
                for c in range(26):
                    val = dp[j] - pref[c][j]
                    if val < best_val[c]:
                        best_val[c] = val
                        best_pos[c] = j

            cur_best = INF
            cur_c = -1
            cur_j = -1
            for c in range(26):
                if best_val[c] == INF:
                    continue
                cost = pref[c][i] + best_val[c]
                if cost < cur_best or (cost == cur_best and c < cur_c):
                    cur_best = cost
                    cur_c = c
                    cur_j = best_pos[c]

            dp[i] = cur_best
            prev[i] = cur_j
            used_char[i] = chr(ord('a') + cur_c) if cur_c != -1 else ''

        if dp[n] >= INF:
            return ""

        # reconstruct answer
        res_parts = []
        i = n
        while i > 0:
            j = prev[i]
            ch = used_char[i]
            length = i - j
            res_parts.append(ch * length)
            i = j
        return ''.join(reversed(res_parts))
```

## Python3

```python
class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        n = len(caption)
        if n < 3:
            return ""
        INF = 10 ** 9
        s = [ord(ch) - 97 for ch in caption]

        # forward DP, store costs after processing i characters (1..n)
        dp_all = [None] * (n + 1)

        dp = [[INF] * 3 for _ in range(26)]
        for c in range(26):
            dp[c][0] = abs(s[0] - c)
        dp_all[1] = [row[:] for row in dp]

        # precompute distance matrix
        dist = [[abs(sc - c) for c in range(26)] for sc in s]

        for i in range(1, n):
            ndp = [[INF] * 3 for _ in range(26)]
            di = dist[i]
            for pc in range(26):
                row_pc = dp[pc]
                for pl in (0, 1, 2):
                    cur = row_pc[pl]
                    if cur == INF:
                        continue
                    # same character continuation
                    cost_same = di[pc]
                    nl = pl + 1 if pl < 2 else 2
                    newc = cur + cost_same
                    if newc < ndp[pc][nl]:
                        ndp[pc][nl] = newc
                    # switch to different character (only if previous run satisfied)
                    if pl == 2:
                        for nc in range(26):
                            if nc == pc:
                                continue
                            cost_diff = di[nc]
                            newc2 = cur + cost_diff
                            if newc2 < ndp[nc][0]:
                                ndp[nc][0] = newc2
            dp = ndp
            dp_all[i + 1] = [row[:] for row in dp]

        # minimal total cost with final run length >=3 (state index 2)
        minCost = INF
        for c in range(26):
            if dp[c][2] < minCost:
                minCost = dp[c][2]
        if minCost == INF:
            return ""

        # good[pos][c][len_state]: can reach optimal from this state
        good = [[[False] * 3 for _ in range(26)] for __ in range(n + 1)]
        for c in range(26):
            if dp_all[n][c][2] == minCost:
                good[n][c][2] = True

        # backward propagation
        for pos in range(n - 1, 0, -1):
            cur = dp_all[pos]
            nxt = dp_all[pos + 1]
            di = dist[pos]
            for pc in range(26):
                for pl in (0, 1, 2):
                    base = cur[pc][pl]
                    if base == INF:
                        continue
                    # same character continuation
                    cost_same = di[pc]
                    nl = pl + 1 if pl < 2 else 2
                    if base + cost_same == nxt[pc][nl] and good[pos + 1][pc][nl]:
                        good[pos][pc][pl] = True
                        continue
                    # switch to different character (only if previous run satisfied)
                    if pl == 2:
                        for nc in range(26):
                            if nc == pc:
                                continue
                            cost_diff = di[nc]
                            if base + cost_diff == nxt[nc][0] and good[pos + 1][nc][0]:
                                good[pos][pc][pl] = True
                                break

        # reconstruction: choose lexicographically smallest optimal string
        res = []
        # first character (state after processing first char)
        for c in range(26):
            if good[1][c][0]:
                res.append(chr(c + 97))
                prev_c = c
                prev_len = 0
                break
        else:
            return ""

        for idx in range(1, n):
            chosen = False
            for c in range(26):
                if c == prev_c:
                    nl = prev_len + 1 if prev_len < 2 else 2
                    if good[idx + 1][c][nl]:
                        res.append(chr(c + 97))
                        prev_len = nl
                        chosen = True
                        break
                else:
                    if prev_len != 2:
                        continue
                    if good[idx + 1][c][0]:
                        res.append(chr(c + 97))
                        prev_c = c
                        prev_len = 0
                        chosen = True
                        break
            if not chosen:
                return ""
        return "".join(res)
```

## C

```c
#include <stdlib.h>
#include <string.h>

#define INF 1000000000

typedef struct {
    int val;
    int idx;
} Pair;

static int findIdx(Pair *arr, int sz, int K, int minIdx) {
    int l = 0, r = sz;
    while (l < r) {
        int m = (l + r) >> 1;
        if (arr[m].val < K) l = m + 1;
        else r = m;
    }
    int start = l;
    if (start == sz || arr[start].val != K) return -1;

    int l2 = start, r2 = sz;
    while (l2 < r2) {
        int m = (l2 + r2) >> 1;
        if (arr[m].val <= K) l2 = m + 1;
        else r2 = m;
    }
    int end = l2;

    int lo = start, hi = end;
    while (lo < hi) {
        int m = (lo + hi) >> 1;
        if (arr[m].idx < minIdx) lo = m + 1;
        else hi = m;
    }
    if (lo == end) return -1;
    return arr[lo].idx;
}

static int* computeDP(int n, int **pref) {
    int *dp = (int*)malloc((n + 1) * sizeof(int));
    for (int i = 0; i <= n; ++i) dp[i] = INF;
    dp[0] = 0;

    int bestVal[26];
    for (int c = 0; c < 26; ++c) bestVal[c] = INF;

    for (int i = 1; i <= n; ++i) {
        if (i >= 3) {
            int j = i - 3;
            if (dp[j] < INF) {
                for (int c = 0; c < 26; ++c) {
                    int val = dp[j] + pref[c][j] - j;
                    if (val < bestVal[c]) bestVal[c] = val;
                }
            }
        }
        int best = INF;
        for (int c = 0; c < 26; ++c) {
            if (bestVal[c] == INF) continue;
            int cand = i - pref[c][i] + bestVal[c];
            if (cand < best) best = cand;
        }
        dp[i] = best;
    }
    return dp;
}

char* minCostGoodCaption(char* caption) {
    int n = strlen(caption);
    if (n == 0) return "";

    /* prefix counts for original string */
    int **pref = (int**)malloc(26 * sizeof(int*));
    for (int c = 0; c < 26; ++c) pref[c] = (int*)calloc(n + 1, sizeof(int));

    for (int i = 0; i < n; ++i) {
        int ch = caption[i] - 'a';
        for (int c = 0; c < 26; ++c)
            pref[c][i + 1] = pref[c][i];
        pref[ch][i + 1]++;
    }

    /* forward DP */
    int *dpF = computeDP(n, pref);
    if (dpF[n] >= INF) {
        free(dpF);
        for (int c = 0; c < 26; ++c) free(pref[c]);
        free(pref);
        return "";
    }

    /* reversed string and its prefix */
    char *rev = (char*)malloc(n + 1);
    for (int i = 0; i < n; ++i) rev[i] = caption[n - 1 - i];
    rev[n] = '\0';

    int **prefR = (int**)malloc(26 * sizeof(int*));
    for (int c = 0; c < 26; ++c) prefR[c] = (int*)calloc(n + 1, sizeof(int));

    for (int i = 0; i < n; ++i) {
        int ch = rev[i] - 'a';
        for (int c = 0; c < 26; ++c)
            prefR[c][i + 1] = prefR[c][i];
        prefR[ch][i + 1]++;
    }

    int *dpRev = computeDP(n, prefR);
    /* suffix DP: dpB[i] = minimal cost for substring i..n-1 */
    int *dpB = (int*)malloc((n + 1) * sizeof(int));
    for (int i = 0; i <= n; ++i)
        dpB[i] = dpRev[n - i];

    /* build value-index arrays for each character */
    Pair **arrs = (Pair**)malloc(26 * sizeof(Pair*));
    for (int c = 0; c < 26; ++c) {
        Pair *a = (Pair*)malloc((n + 1) * sizeof(Pair));
        for (int i = 0; i <= n; ++i) {
            int v = dpB[i] - pref[c][i] + i;
            a[i].val = v;
            a[i].idx = i;
        }
        /* sort by val then idx */
        qsort(a, n + 1, sizeof(Pair), (int(*)(const void*, const void*))(
            ^int(const Pair *p1, const Pair *p2){
                if (p1->val != p2->val) return p1->val - p2->val;
                return p1->idx - p2->idx;
            }
        ));
        arrs[c] = a;
    }

    char *ans = (char*)malloc(n + 1);
    int pos = 0;
    while (pos < n) {
        int chosenLen = -1;
        char chosenChar = '?';
        for (int c = 0; c < 26; ++c) {
            int K = dpF[n] - dpF[pos] + pref[c][pos] - pos;
            int iIdx = findIdx(arrs[c], n + 1, K, pos + 3);
            if (iIdx != -1) {
                chosenLen = iIdx - pos;
                chosenChar = 'a' + c;
                break; /* smallest character found */
            }
        }
        if (chosenLen == -1) { /* should not happen */
            free(ans);
            ans = (char*)malloc(1);
            ans[0] = '\0';
            break;
        }
        for (int k = 0; k < chosenLen; ++k)
            ans[pos + k] = chosenChar;
        pos += chosenLen;
    }
    ans[n] = '\0';

    /* free allocated memory */
    free(dpF);
    free(dpRev);
    free(dpB);
    free(rev);
    for (int c = 0; c < 26; ++c) {
        free(pref[c]);
        free(prefR[c]);
        free(arrs[c]);
    }
    free(pref);
    free(prefR);
    free(arrs);

    return ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public string MinCostGoodCaption(string caption) {
        int n = caption.Length;
        const int INF = 1_000_000_0;
        // dp[i, c, len] where len = 1..3
        int[,,] dp = new int[n, 26, 4];
        for (int i = 0; i < n; i++) {
            for (int c = 0; c < 26; c++) {
                dp[i, c, 1] = INF;
                dp[i, c, 2] = INF;
                dp[i, c, 3] = INF;
            }
        }

        // initialize first character
        for (int c = 0; c < 26; c++) {
            dp[0, c, 1] = (caption[0] == (char)('a' + c)) ? 0 : 1;
        }

        // DP forward
        for (int i = 1; i < n; i++) {
            // continuation of same character
            for (int pc = 0; pc < 26; pc++) {
                for (int pl = 1; pl <= 3; pl++) {
                    int prev = dp[i - 1, pc, pl];
                    if (prev == INF) continue;
                    int costSame = (caption[i] == (char)('a' + pc)) ? 0 : 1;
                    int newLen = (pl == 3) ? 3 : pl + 1;
                    int val = prev + costSame;
                    if (val < dp[i, pc, newLen]) dp[i, pc, newLen] = val;
                }
            }

            // start a new block (len=1), only allowed after a run of length >=3
            int bestVal = INF, bestChar = -1, secondVal = INF;
            for (int pc = 0; pc < 26; pc++) {
                int v = dp[i - 1, pc, 3];
                if (v < bestVal) {
                    secondVal = bestVal;
                    bestVal = v;
                    bestChar = pc;
                } else if (v < secondVal) {
                    secondVal = v;
                }
            }

            for (int nc = 0; nc < 26; nc++) {
                int prevCost = (nc == bestChar) ? secondVal : bestVal;
                if (prevCost == INF) continue;
                int costSwitch = (caption[i] == (char)('a' + nc)) ? 0 : 1;
                int val = prevCost + costSwitch;
                if (val < dp[i, nc, 1]) dp[i, nc, 1] = val;
            }
        }

        // find minimal total cost ending with len=3
        int minCost = INF;
        int endChar = -1;
        for (int c = 0; c < 26; c++) {
            int v = dp[n - 1, c, 3];
            if (v < minCost) {
                minCost = v;
                endChar = c;
            } else if (v == minCost && c < endChar) {
                endChar = c;
            }
        }

        if (minCost == INF) return "";

        // reconstruct lexicographically smallest answer
        char[] ans = new char[n];
        int iPos = n - 1;
        int curChar = endChar;
        int curLen = 3;

        while (iPos >= 0) {
            ans[iPos] = (char)('a' + curChar);
            if (curLen > 1) {
                // continue same block
                curLen = (curLen == 3) ? 3 : curLen - 1;
                iPos--;
                // curChar stays the same
            } else { // curLen == 1, start of a new block
                int costHere = (caption[iPos] == (char)('a' + curChar)) ? 0 : 1;
                int targetPrevCost = dp[iPos, curChar, 1] - costHere;

                // find smallest predecessor character different from curChar with required cost
                int prevCharFound = -1;
                for (int pc = 0; pc < 26; pc++) {
                    if (pc == curChar) continue;
                    if (dp[iPos - 1, pc, 3] == targetPrevCost) {
                        prevCharFound = pc;
                        break;
                    }
                }
                // move to previous position
                iPos--;
                curChar = prevCharFound; // must be found
                curLen = 3;
            }
        }

        return new string(ans);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} caption
 * @return {string}
 */
var minCostGoodCaption = function(caption) {
    const n = caption.length;
    const INF = 1e15;

    // prefix counts for each character
    const pref = Array.from({length: 26}, () => new Int32Array(n + 1));
    for (let i = 0; i < n; ++i) {
        const chIdx = caption.charCodeAt(i) - 97;
        for (let c = 0; c < 26; ++c) {
            pref[c][i + 1] = pref[c][i];
        }
        pref[chIdx][i + 1]++;
    }

    const dp = new Float64Array(n + 1);
    const prevIdx = new Int32Array(n + 1);
    const prevChar = new Int8Array(n + 1);
    for (let i = 0; i <= n; ++i) {
        dp[i] = INF;
        prevIdx[i] = -1;
        prevChar[i] = -1;
    }
    dp[0] = 0;

    const bestBase = new Float64Array(26);
    const bestPos = new Int32Array(26);
    for (let c = 0; c < 26; ++c) {
        bestBase[c] = INF;
        bestPos[c] = -1;
    }

    for (let j = 1; j <= n; ++j) {
        const addIdx = j - 3;
        if (addIdx >= 0) {
            // incorporate start position addIdx into best structures
            for (let c = 0; c < 26; ++c) {
                const val = dp[addIdx] - addIdx + pref[c][addIdx];
                if (val < bestBase[c] || (val === bestBase[c] && addIdx < bestPos[c])) {
                    bestBase[c] = val;
                    bestPos[c] = addIdx;
                }
            }
        }

        // compute dp[j]
        for (let c = 0; c < 26; ++c) {
            if (bestBase[c] === INF) continue;
            const cand = bestBase[c] + (j - pref[c][j]);
            if (cand < dp[j]) {
                dp[j] = cand;
                prevIdx[j] = bestPos[c];
                prevChar[j] = c;
            } else if (cand === dp[j]) {
                // tie-breaking: smaller character, then smaller start index (longer run)
                if (c < prevChar[j] || (c === prevChar[j] && bestPos[c] < prevIdx[j])) {
                    prevIdx[j] = bestPos[c];
                    prevChar[j] = c;
                }
            }
        }
    }

    if (dp[n] >= INF / 2) return "";

    // reconstruct answer
    const segments = [];
    let pos = n;
    while (pos > 0) {
        const i = prevIdx[pos];
        const c = prevChar[pos];
        const len = pos - i;
        const seg = String.fromCharCode(97 + c).repeat(len);
        segments.push(seg);
        pos = i;
    }
    segments.reverse();
    return segments.join('');
};
```

## Typescript

```typescript
function minCostGoodCaption(caption: string): string {
    const n = caption.length;
    if (n < 3) return "";
    const ALPH = 26;
    const STATES = 3; // 0: len>=3, 1: len=1, 2: len=2
    const INF = 1 << 30;

    const chars = new Uint8Array(n);
    for (let i = 0; i < n; ++i) chars[i] = caption.charCodeAt(i) - 97;

    // transition table: trans[prevChar][prevState][nextChar] = nextState or -1
    const trans = Array.from({ length: ALPH }, () =>
        Array.from({ length: STATES }, () => new Int8Array(ALPH))
    );
    for (let pc = 0; pc < ALPH; ++pc) {
        for (let ps = 0; ps < STATES; ++ps) {
            const row = trans[pc][ps];
            for (let nc = 0; nc < ALPH; ++nc) {
                let ns: number;
                if (nc === pc) {
                    if (ps === 0) ns = 0;
                    else if (ps === 1) ns = 2;
                    else /* ps===2 */ ns = 0;
                } else {
                    if (ps !== 0) ns = -1;
                    else ns = 1;
                }
                row[nc] = ns as number;
            }
        }
    }

    const size = n * ALPH * STATES;
    const dpFwd = new Int32Array(size);
    dpFwd.fill(INF);

    const idx = (i: number, c: number, s: number) => ((i * ALPH + c) * STATES + s);

    // initialize first position
    for (let c = 0; c < ALPH; ++c) {
        dpFwd[idx(0, c, 1)] = chars[0] === c ? 0 : 1;
    }

    // forward DP to compute minimal total cost
    for (let i = 1; i < n; ++i) {
        const basePrev = (i - 1) * ALPH * STATES;
        const baseCur = i * ALPH * STATES;
        for (let pc = 0; pc < ALPH; ++pc) {
            const prevBaseChar = basePrev + pc * STATES;
            for (let ps = 0; ps < STATES; ++ps) {
                const prevCost = dpFwd[prevBaseChar + ps];
                if (prevCost === INF) continue;
                const transRow = trans[pc][ps];
                for (let nc = 0; nc < ALPH; ++nc) {
                    const ns = transRow[nc];
                    if (ns === -1) continue;
                    const cost = prevCost + (chars[i] === nc ? 0 : 1);
                    const curIdx = baseCur + nc * STATES + ns;
                    if (cost < dpFwd[curIdx]) dpFwd[curIdx] = cost;
                }
            }
        }
    }

    let minTotal = INF;
    for (let c = 0; c < ALPH; ++c) {
        const v = dpFwd[idx(n - 1, c, 0)];
        if (v < minTotal) minTotal = v;
    }
    if (minTotal === INF) return "";

    // backward DP to assist reconstruction
    const dpBwd = new Int32Array(size);
    dpBwd.fill(INF);
    for (let c = 0; c < ALPH; ++c) {
        dpBwd[idx(n - 1, c, 0)] = 0;
    }

    for (let i = n - 2; i >= 0; --i) {
        const baseCur = i * ALPH * STATES;
        const baseNext = (i + 1) * ALPH * STATES;
        for (let pc = 0; pc < ALPH; ++pc) {
            const curBaseChar = baseCur + pc * STATES;
            for (let ps = 0; ps < STATES; ++ps) {
                let best = INF;
                const transRow = trans[pc][ps];
                for (let nc = 0; nc < ALPH; ++nc) {
                    const ns = transRow[nc];
                    if (ns === -1) continue;
                    const costNext = (chars[i + 1] === nc ? 0 : 1) + dpBwd[baseNext + nc * STATES + ns];
                    if (costNext < best) best = costNext;
                }
                dpBwd[curBaseChar + ps] = best;
            }
        }
    }

    // reconstruction of lexicographically smallest answer
    const resCodes = new Uint8Array(n);
    let accCost = 0;
    let curChar = -1;
    let curState = -1;

    // position 0
    for (let c = 0; c < ALPH; ++c) {
        const add = chars[0] === c ? 0 : 1;
        if (add + dpBwd[idx(0, c, 1)] === minTotal) {
            resCodes[0] = c;
            curChar = c;
            curState = 1;
            accCost = add;
            break;
        }
    }

    // remaining positions
    for (let i = 1; i < n; ++i) {
        for (let nc = 0; nc < ALPH; ++nc) {
            const ns = trans[curChar][curState][nc];
            if (ns === -1) continue;
            const add = chars[i] === nc ? 0 : 1;
            const totalIfChoose = accCost + add + dpBwd[idx(i, nc, ns)];
            if (totalIfChoose === minTotal) {
                resCodes[i] = nc;
                curChar = nc;
                curState = ns;
                accCost += add;
                break;
            }
        }
    }

    // convert to string
    let result = "";
    for (let i = 0; i < n; ++i) {
        result += String.fromCharCode(97 + resCodes[i]);
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $caption
     * @return String
     */
    function minCostGoodCaption($caption) {
        $n = strlen($caption);
        if ($n == 0) return "";
        // prefix matches for each character
        $match = array_fill(0, 26, array_fill(0, $n + 1, 0));
        for ($i = 0; $i < $n; $i++) {
            $chIdx = ord($caption[$i]) - 97;
            for ($c = 0; $c < 26; $c++) {
                $match[$c][$i + 1] = $match[$c][$i] + ($c == $chIdx ? 1 : 0);
            }
        }

        $INF = PHP_INT_MAX;

        // dp[i]: minimal cost for suffix starting at i
        $dp = array_fill(0, $n + 1, $INF);
        $chooseChar = array_fill(0, $n, -1); // character index chosen at i
        $chooseEnd   = array_fill(0, $n, -1); // exclusive end position

        $dp[$n] = 0;

        // bestVal[c][i]: minimal value of (j - match_c[j] + dp[j]) for j >= i
        // bestIdx[c][i]: the j achieving that minimal value (choose larger j on ties)
        $bestVal = [];
        $bestIdx = [];
        for ($c = 0; $c < 26; $c++) {
            $bestVal[$c] = array_fill(0, $n + 2, $INF);
            $bestIdx[$c] = array_fill(0, $n + 2, -1);
        }

        // DP from right to left
        for ($i = $n - 1; $i >= 0; $i--) {
            $bestCost = $INF;
            $bChar = -1;
            $bEnd = -1;

            for ($c = 0; $c < 26; $c++) {
                $pos = $i + 3;
                if ($pos > $n) continue;
                $val = $bestVal[$c][$pos];
                if ($val === $INF) continue;
                // total cost using best suffix starting at some j >= pos
                $total = -($i - $match[$c][$i]) + $val;
                if ($total < $bestCost) {
                    $bestCost = $total;
                    $bChar = $c;
                    $bEnd = $bestIdx[$c][$pos];
                } elseif ($total == $bestCost) {
                    if ($c < $bChar) {
                        $bChar = $c;
                        $bEnd = $bestIdx[$c][$pos];
                    } elseif ($c == $bChar) {
                        $candEnd = $bestIdx[$c][$pos];
                        if ($candEnd > $bEnd) { // longer run gives smaller string
                            $bEnd = $candEnd;
                        }
                    }
                }
            }

            $dp[$i] = $bestCost;
            $chooseChar[$i] = $bChar;
            $chooseEnd[$i]   = $bEnd;

            // update best arrays for each character
            for ($c = 0; $c < 26; $c++) {
                $valueAtI = $i - $match[$c][$i] + $dp[$i];
                $nextVal = $bestVal[$c][$i + 1];
                if ($valueAtI < $nextVal) {
                    $bestVal[$c][$i] = $valueAtI;
                    $bestIdx[$c][$i] = $i;
                } elseif ($valueAtI == $nextVal) {
                    // tie: prefer larger index (later start -> shorter remaining suffix)
                    if ($i > $bestIdx[$c][$i + 1]) {
                        $bestVal[$c][$i] = $valueAtI;
                        $bestIdx[$c][$i] = $i;
                    } else {
                        $bestVal[$c][$i] = $nextVal;
                        $bestIdx[$c][$i] = $bestIdx[$c][$i + 1];
                    }
                } else {
                    $bestVal[$c][$i] = $nextVal;
                    $bestIdx[$c][$i] = $bestIdx[$c][$i + 1];
                }
            }
        }

        if ($dp[0] === $INF) return "";

        // reconstruct answer
        $res = '';
        $i = 0;
        while ($i < $n) {
            $c = $chooseChar[$i];
            $end = $chooseEnd[$i];
            $len = $end - $i;
            $res .= str_repeat(chr(97 + $c), $len);
            $i = $end;
        }
        return $res;
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    func minCostGoodCaption(_ caption: String) -> String {
        let n = caption.count
        if n == 0 { return "" }
        // Convert caption to integer array 0..25
        var a = [Int](repeating: 0, count: n)
        let bytes = Array(caption.utf8)
        for i in 0..<n {
            a[i] = Int(bytes[i] - 97)
        }

        let INF = Int.max / 4
        // dimensions: (n+1) * 27 * 4
        let totalSize = (n + 1) * 27 * 4
        var dp = [Int](repeating: INF, count: totalSize)

        @inline(__always)
        func index(_ i: Int, _ pc: Int, _ pl: Int) -> Int {
            return ((i * 27 + pc) << 2) + pl   // multiply by 4
        }

        // Base case: at position n, only valid if previous run length == 3 (>=3)
        for pc in 0..<27 {
            dp[index(n, pc, 3)] = 0
        }

        // DP from end to start
        if n > 0 {
            for i in stride(from: n - 1, through: 0, by: -1) {
                for pc in 0..<27 {
                    for pl in 0...3 {
                        // skip impossible states
                        if pc != 26 && pl == 0 { continue }
                        var best = INF
                        for nc in 0..<26 {
                            var valid = false
                            var newLen = 0
                            if pc == 26 {
                                // start state, any character allowed
                                valid = true
                                newLen = 1
                            } else {
                                if nc == pc {
                                    if pl == 0 { continue }
                                    valid = true
                                    newLen = min(pl + 1, 3)
                                } else {
                                    if pl == 3 {
                                        valid = true
                                        newLen = 1
                                    }
                                }
                            }
                            if !valid { continue }
                            let costAdd = (a[i] == nc) ? 0 : 1
                            let nextIdx = index(i + 1, nc, newLen)
                            let cand = costAdd + dp[nextIdx]
                            if cand < best {
                                best = cand
                            }
                        }
                        dp[index(i, pc, pl)] = best
                    }
                }
            }
        }

        let startIdx = index(0, 26, 0)
        let bestCost = dp[startIdx]
        if bestCost >= INF / 2 { return "" }

        // Reconstruct lexicographically smallest optimal string
        var result = [Character]()
        var pos = 0
        var pc = 26
        var pl = 0

        while pos < n {
            for nc in 0..<26 {
                var valid = false
                var newLen = 0
                if pc == 26 {
                    valid = true
                    newLen = 1
                } else {
                    if nc == pc {
                        if pl == 0 { continue }
                        valid = true
                        newLen = min(pl + 1, 3)
                    } else {
                        if pl == 3 {
                            valid = true
                            newLen = 1
                        }
                    }
                }
                if !valid { continue }
                let costAdd = (a[pos] == nc) ? 0 : 1
                let curIdx = index(pos, pc, pl)
                let nextIdx = index(pos + 1, nc, newLen)
                if dp[curIdx] == costAdd + dp[nextIdx] {
                    result.append(Character(UnicodeScalar(nc + 97)!))
                    pc = nc
                    pl = newLen
                    pos += 1
                    break
                }
            }
        }

        return String(result)
    }
}
```

## Kotlin

```kotlin
import java.util.*

class Solution {
    fun minCostGoodCaption(caption: String): String {
        val n = caption.length
        val INF = 1_000_000_000
        // state index: c * 4 + len, where c in 0..26 (26 is sentinel), len in 0..3
        fun idx(c: Int, len: Int) = c * 4 + len

        val dp = Array(n + 1) { IntArray(27 * 4) }
        // initialize for position n
        for (c in 0 until 26) {
            dp[n][idx(c, 1)] = INF
            dp[n][idx(c, 2)] = INF
            dp[n][idx(c, 3)] = 0
        }
        dp[n][idx(26, 0)] = INF

        // backward DP
        for (i in n - 1 downTo 0) {
            val cur = IntArray(27 * 4) { INF }

            var best1 = INF
            var best2 = INF
            var bestChar = -1
            for (d in 0 until 26) {
                val costAdd = if (caption[i] == ('a'.code + d).toChar()) 0 else 1
                val valSwitch = costAdd + dp[i + 1][idx(d, 1)]
                if (valSwitch < best1) {
                    best2 = best1
                    best1 = valSwitch
                    bestChar = d
                } else if (valSwitch < best2) {
                    best2 = valSwitch
                }
            }

            for (c in 0 until 26) {
                val costSame = if (caption[i] == ('a'.code + c).toChar()) 0 else 1
                // len = 1 -> after placing same char, new len = 2
                cur[idx(c, 1)] = costSame + dp[i + 1][idx(c, 2)]
                // len = 2 -> new len = 3
                cur[idx(c, 2)] = costSame + dp[i + 1][idx(c, 3)]
                // len = 3
                val cont = costSame + dp[i + 1][idx(c, 3)]
                var sw = INF
                if (bestChar != -1) {
                    sw = if (c != bestChar) best1 else best2
                }
                cur[idx(c, 3)] = kotlin.math.min(cont, sw)
            }

            // sentinel state: start new run with any character
            cur[idx(26, 0)] = best1

            dp[i] = cur
        }

        val minTotal = dp[0][idx(26, 0)]
        if (minTotal >= INF / 2) return ""

        // reconstruction for lexicographically smallest string achieving minTotal
        val sb = StringBuilder()
        var prevC = 26
        var prevLen = 0
        var costSoFar = 0

        for (i in 0 until n) {
            for (chIdx in 0 until 26) {
                val ch = ('a'.code + chIdx).toChar()
                var allowed = false
                var newLen = 0
                if (prevC == 26) { // start
                    allowed = true
                    newLen = 1
                } else {
                    if (chIdx == prevC) {
                        allowed = true
                        newLen = kotlin.math.min(prevLen + 1, 3)
                    } else if (prevLen == 3) {
                        allowed = true
                        newLen = 1
                    }
                }
                if (!allowed) continue

                val costAdd = if (caption[i] == ch) 0 else 1
                val remaining = dp[i + 1][idx(chIdx, newLen)]
                if (costSoFar + costAdd + remaining == minTotal) {
                    sb.append(ch)
                    prevC = chIdx
                    prevLen = newLen
                    costSoFar += costAdd
                    break
                }
            }
        }

        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String minCostGoodCaption(String caption) {
    const int INF = 1 << 30;
    final List<int> s = caption.codeUnits.map((c) => c - 97).toList();
    final int n = s.length;
    if (n < 3) return "";
    // dp[i][state] where state = lastChar*3 + lenIdx (0->1,1->2,2->>=3)
    final int STATES = 27 * 3; // we will never use lastChar=26 in states
    List<List<int>> dp = List.generate(n + 1,
        (_) => List.filled(STATES, INF),
        growable: false);
    // initialize first character
    for (int c = 0; c < 26; ++c) {
      int cost = (s[0] == c) ? 0 : 1;
      dp[1][c * 3 + 0] = cost < dp[1][c * 3 + 0] ? cost : dp[1][c * 3 + 0];
    }
    // fill DP
    for (int i = 1; i < n; ++i) {
      List<int> cur = dp[i];
      List<int> nxt = dp[i + 1];
      for (int id = 0; id < STATES; ++id) {
        int curCost = cur[id];
        if (curCost >= INF) continue;
        int lastChar = id ~/ 3;
        int lenIdx = id % 3; // 0,1,2
        for (int c = 0; c < 26; ++c) {
          int added = (s[i] == c) ? 0 : 1;
          int newLenIdx;
          if (c == lastChar) {
            newLenIdx = (lenIdx == 2) ? 2 : lenIdx + 1;
          } else {
            if (lenIdx != 2) continue; // previous run too short
            newLenIdx = 0;
          }
          int nid = c * 3 + newLenIdx;
          int ndCost = curCost + added;
          if (ndCost < nxt[nid]) nxt[nid] = ndCost;
        }
      }
    }
    // find best final state with lenIdx == 2
    int bestCost = INF;
    int bestId = -1;
    for (int id = 0; id < STATES; ++id) {
      if (id % 3 != 2) continue;
      if (dp[n][id] < bestCost) {
        bestCost = dp[n][id];
        bestId = id;
      }
    }
    if (bestCost >= INF) return "";
    // reconstruct lexicographically smallest optimal string
    StringBuffer sb = StringBuffer();
    int currId = -1; // sentinel before first character
    for (int i = 0; i < n; ++i) {
      bool placed = false;
      for (int c = 0; c < 26 && !placed; ++c) {
        int added = (s[i] == c) ? 0 : 1;
        if (i == 0) {
          int nid = c * 3 + 0;
          if (dp[1][nid] == added) {
            sb.writeCharCode(c + 97);
            currId = nid;
            placed = true;
          }
        } else {
          int lastChar = currId ~/ 3;
          int lenIdx = currId % 3;
          if (c == lastChar) {
            int newLenIdx = (lenIdx == 2) ? 2 : lenIdx + 1;
            int nid = c * 3 + newLenIdx;
            if (dp[i + 1][nid] == dp[i][currId] + added) {
              sb.writeCharCode(c + 97);
              currId = nid;
              placed = true;
            }
          } else {
            if (lenIdx != 2) continue; // cannot switch
            int nid = c * 3 + 0;
            if (dp[i + 1][nid] == dp[i][currId] + added) {
              sb.writeCharCode(c + 97);
              currId = nid;
              placed = true;
            }
          }
        }
      }
    }
    return sb.toString();
  }
}
```

## Golang

```go
package main

import (
	"strings"
)

func minCostGoodCaption(caption string) string {
	const INF = int(1 << 30)
	n := len(caption)

	// prefix mismatches for each character
	mis := make([][]int, 26)
	for c := 0; c < 26; c++ {
		mis[c] = make([]int, n+1)
	}
	for i := 0; i < n; i++ {
		orig := int(caption[i] - 'a')
		for c := 0; c < 26; c++ {
			mis[c][i+1] = mis[c][i]
			if c != orig {
				mis[c][i+1]++
			}
		}
	}

	// DP forward
	dp := make([]int, n+1)
	for i := 0; i <= n; i++ {
		dp[i] = INF
	}
	dp[0] = 0
	best := make([]int, 26)
	for c := 0; c < 26; c++ {
		best[c] = INF
	}

	for i := 1; i <= n; i++ {
		if i-3 >= 0 {
			j := i - 3
			for c := 0; c < 26; c++ {
				val := dp[j] - mis[c][j]
				if val < best[c] {
					best[c] = val
				}
			}
		}
		minCost := INF
		for c := 0; c < 26; c++ {
			if best[c] == INF {
				continue
			}
			cost := best[c] + mis[c][i]
			if cost < minCost {
				minCost = cost
			}
		}
		dp[i] = minCost
	}

	if dp[n] >= INF {
		return ""
	}

	// Build maps from value to positions for each character
	posMap := make([]map[int][]int, 26)
	for c := 0; c < 26; c++ {
		posMap[c] = make(map[int][]int)
	}
	for i := 0; i <= n; i++ {
		if dp[i] >= INF {
			continue
		}
		for c := 0; c < 26; c++ {
			val := dp[i] - mis[c][i]
			posMap[c][val] = append(posMap[c][val], i)
		}
	}

	var sb strings.Builder
	cur := 0
	for cur < n {
		found := false
		for ch := 0; ch < 26; ch++ {
			val := dp[cur] - mis[ch][cur]
			list, ok := posMap[ch][val]
			if !ok || len(list) == 0 {
				continue
			}
			nxt := list[len(list)-1] // farthest position with same value
			if nxt >= cur+3 {
				length := nxt - cur
				for k := 0; k < length; k++ {
					sb.WriteByte(byte('a' + ch))
				}
				cur = nxt
				found = true
				break
			}
		}
		if !found { // should not happen for reachable states
			return ""
		}
	}
	return sb.String()
}
```

## Ruby

```ruby
def min_cost_good_caption(caption)
  n = caption.length
  return "" if n < 3

  chars = caption.bytes.map { |b| b - 97 }
  INF = 1 << 30
  C = 27          # 0..25 letters, 26 = none (start)
  R = 4           # run length state: 0,1,2,3 (3 means >=3)

  idx = ->(i, c, r) { ((i * C + c) * R + r) }

  dp = Array.new((n + 1) * C * R, INF)

  # base case at position n
  (0...C).each do |c|
    (0...R).each do |r|
      dp[idx.call(n, c, r)] = (r == 3 ? 0 : INF)
    end
  end

  (n - 1).downto(0) do |i|
    orig = chars[i]
    (0...C).each do |c|
      rs = (c == 26) ? [0] : [1, 2, 3]
      rs.each do |r|
        best = INF
        26.times do |cur|
          step = (cur == orig) ? 0 : 1
          if cur == c
            nr = r + 1
            nr = 3 if nr > 3
            val = step + dp[idx.call(i + 1, cur, nr)]
            best = val if val < best
          else
            if r == 3 || c == 26
              nr = 1
              val = step + dp[idx.call(i + 1, cur, nr)]
              best = val if val < best
            end
          end
        end
        dp[idx.call(i, c, r)] = best
      end
    end
  end

  min_cost = dp[idx.call(0, 26, 0)]
  return "" if min_cost >= INF

  # reconstruction for lexicographically smallest answer
  i = 0
  c = 26
  r = 0
  res = +''
  while i < n
    orig = chars[i]
    chosen = nil
    (0...26).each do |cur|
      step = (cur == orig) ? 0 : 1
      if cur == c
        nr = r + 1
        nr = 3 if nr > 3
        if step + dp[idx.call(i + 1, cur, nr)] == dp[idx.call(i, c, r)]
          chosen = cur
          c = cur
          r = nr
          break
        end
      else
        if r == 3 || c == 26
          nr = 1
          if step + dp[idx.call(i + 1, cur, nr)] == dp[idx.call(i, c, r)]
            chosen = cur
            c = cur
            r = nr
            break
          end
        end
      end
    end
    # should always find a character
    res << (chosen + 97).chr
    i += 1
  end

  res
end
```

## Scala

```scala
object Solution {
    def minCostGoodCaption(caption: String): String = {
        val n = caption.length
        val arr = caption.toCharArray.map(ch => ch - 'a')
        val INF = 1000000000
        val totalChars = 27 // 26 letters + sentinel
        val statesPerPos = totalChars * 4 // l = 0..3
        val dp = Array.ofDim[Int](n + 1, statesPerPos)

        // Base case for position n
        var c = 0
        while (c < totalChars) {
            var l = 0
            while (l <= 3) {
                val idx = c * 4 + l
                dp(n)(idx) = if (l == 0 || l >= 3) 0 else INF
                l += 1
            }
            c += 1
        }

        // Fill DP backwards
        var pos = n - 1
        while (pos >= 0) {
            val orig = arr(pos)
            var cPrev = 0
            while (cPrev < totalChars) {
                var lPrev = 0
                while (lPrev <= 3) {
                    val idxPrev = cPrev * 4 + lPrev
                    var best = INF
                    var x = 0
                    while (x < 26) {
                        // transition allowed?
                        if (lPrev == 0 || lPrev >= 3 || x == cPrev) {
                            val newL = if (x == cPrev) {
                                if (lPrev == 0) 1 else math.min(lPrev + 1, 3)
                            } else 1
                            val cost = if (orig == x) 0 else 1
                            val idxNext = x * 4 + newL
                            val totalCost = cost + dp(pos + 1)(idxNext)
                            if (totalCost < best) best = totalCost
                        }
                        x += 1
                    }
                    dp(pos)(idxPrev) = best
                    lPrev += 1
                }
                cPrev += 1
            }
            pos -= 1
        }

        val startIdx = 26 * 4 + 0 // sentinel state
        val minCost = dp(0)(startIdx)
        if (minCost >= INF) return ""

        // Reconstruct lexicographically smallest answer
        val sb = new StringBuilder()
        var curC = 26
        var curL = 0
        var i = 0
        while (i < n) {
            val orig = arr(i)
            var chosen = -1
            var chosenL = 0
            var x = 0
            while (x < 26) {
                if (curL == 0 || curL >= 3 || x == curC) {
                    val newL = if (x == curC) {
                        if (curL == 0) 1 else math.min(curL + 1, 3)
                    } else 1
                    val cost = if (orig == x) 0 else 1
                    val idxNext = x * 4 + newL
                    val totalCost = cost + dp(i + 1)(idxNext)
                    if (totalCost == dp(i)(curC * 4 + curL)) {
                        chosen = x
                        chosenL = newL
                        // first such x is lexicographically smallest
                        x = 26
                    }
                }
                x += 1
            }
            sb.append(('a' + chosen).toChar)
            curC = chosen
            curL = chosenL
            i += 1
        }

        sb.toString()
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cmp::Ordering;

#[derive(Clone)]
struct Node {
    ch: u8,
    len: usize,
    next: Option<Rc<Node>>,
}

fn cmp_opt(a: &Option<Rc<Node>>, b: &Option<Rc<Node>>) -> Ordering {
    let mut cur_a = a.clone();
    let mut cur_b = b.clone();
    let mut have_a = false;
    let mut have_b = false;
    let mut ch_a = 0u8;
    let mut rem_a = 0usize;
    let mut ch_b = 0u8;
    let mut rem_b = 0usize;

    loop {
        if !have_a {
            match &cur_a {
                Some(node) => {
                    ch_a = node.ch;
                    rem_a = node.len;
                    have_a = true;
                }
                None => return if cur_b.is_none() { Ordering::Equal } else { Ordering::Less },
            }
        }
        if !have_b {
            match &cur_b {
                Some(node) => {
                    ch_b = node.ch;
                    rem_b = node.len;
                    have_b = true;
                }
                None => return Ordering::Greater,
            }
        }

        if ch_a != ch_b {
            return ch_a.cmp(&ch_b);
        }

        let m = std::cmp::min(rem_a, rem_b);
        rem_a -= m;
        rem_b -= m;

        if rem_a == 0 {
            cur_a = cur_a.as_ref().unwrap().next.clone();
            have_a = false;
        }
        if rem_b == 0 {
            cur_b = cur_b.as_ref().unwrap().next.clone();
            have_b = false;
        }
    }
}

impl Solution {
    pub fn min_cost_good_caption(caption: String) -> String {
        let n = caption.len();
        let bytes = caption.as_bytes();

        // prefix counts
        let mut pref = vec![vec![0usize; n + 1]; 26];
        for c in 0..26 {
            for i in 0..n {
                pref[c][i + 1] = pref[c][i] + if (bytes[i] - b'a') as usize == c { 1 } else { 0 };
            }
        }

        const INF: i32 = 1_000_000_000;
        let mut dp = vec![INF; n + 1];
        let mut suffix_node: Vec<Option<Rc<Node>>> = vec![None; n + 1];
        dp[n] = 0;
        suffix_node[n] = None;

        // best values for each character
        let mut best_val = vec![i64::MAX; 26];
        let mut best_i = vec![usize::MAX; 26];
        let mut best_suf: Vec<Option<Rc<Node>>> = vec![None; 26];

        for pos_rev in (0..n).rev() {
            // add candidate i = pos + 3
            if pos_rev + 3 <= n && dp[pos_rev + 3] < INF {
                let i = pos_rev + 3;
                for c in 0..26 {
                    let val = dp[i] as i64 + i as i64 - pref[c][i] as i64;
                    if val < best_val[c]
                        || (val == best_val[c]
                            && cmp_opt(&suffix_node[i], &best_suf[c]) == Ordering::Less)
                    {
                        best_val[c] = val;
                        best_i[c] = i;
                        best_suf[c] = suffix_node[i].clone();
                    }
                }
            }

            // compute dp[pos_rev]
            let mut cur_best_cost = i64::MAX;
            let mut cur_best_node: Option<Rc<Node>> = None;

            for c in 0..26 {
                if best_val[c] == i64::MAX {
                    continue;
                }
                let cost = best_val[c] - (pos_rev as i64 - pref[c][pos_rev] as i64);
                let i = best_i[c];
                let len = i - pos_rev;
                let next_node = suffix_node[i].clone();
                let cand_node = Rc::new(Node {
                    ch: c as u8,
                    len,
                    next: next_node,
                });

                if cost < cur_best_cost {
                    cur_best_cost = cost;
                    cur_best_node = Some(cand_node);
                } else if cost == cur_best_cost {
                    if cmp_opt(&Some(cand_node.clone()), &cur_best_node) == Ordering::Less {
                        cur_best_node = Some(cand_node);
                    }
                }
            }

            if cur_best_cost == i64::MAX {
                dp[pos_rev] = INF;
                suffix_node[pos_rev] = None;
            } else {
                dp[pos_rev] = cur_best_cost as i32;
                suffix_node[pos_rev] = cur_best_node;
            }
        }

        if dp[0] >= INF {
            return String::new();
        }

        // build result string from suffix_node[0]
        let mut res = String::with_capacity(n);
        let mut cur = suffix_node[0].clone();
        while let Some(node) = cur {
            for _ in 0..node.len {
                res.push((b'a' + node.ch) as char);
            }
            cur = node.next.clone();
        }
        res
    }
}
```

## Racket

```racket
(define/contract (min-cost-good-caption caption)
  (-> string? string?)
  (let* ([n (string-length caption)]
         [base (char->integer #\a)]
         [state-size (* 26 3)] ; 78
         [INF 1000000000]
         ;; dp vectors for previous and current position
         [dp-prev (make-vector state-size INF)]
         [pred   (make-vector (* n state-size) -1)])
    (if (< n 3)
        "" ; impossible because any good caption needs runs >=3, but could be empty? return ""
        (begin
          ;; initialization for first character (position 0)
          (let ([first-idx (char->integer (string-ref caption 0))])
            (for ([c (in-range 26)])
              (let* ([cost (if (= c (- first-idx base)) 0 1)]
                     [idx (+ (* c 3) 0)]) ; length =1
                (vector-set! dp-prev idx cost)
                (vector-set! pred (+ (* 0 state-size) idx) -2)))) ; sentinel predecessor
          ;; DP over remaining positions
          (for ([i (in-range 1 n)])
            (let* ([ch-idx (- (char->integer (string-ref caption i)) base)]
                   [dp-curr (make-vector state-size INF)])
              (for ([prev-idx (in-range state-size)])
                (let ([prev-cost (vector-ref dp-prev prev-idx)])
                  (when (< prev-cost INF)
                    (let* ([prev-c (quotient prev-idx 3)]
                           [prev-l (+ (remainder prev-idx 3) 1)])
                      (for ([next-c (in-range 26)])
                        (let ([add (if (= next-c ch-idx) 0 1)])
                          (cond
                            [(= next-c prev-c)
                             (let* ([new-l (if (< prev-l 3) (+ prev-l 1) 3)]
                                    [new-idx (+ (* next-c 3) (- new-l 1))]
                                    [new-cost (+ prev-cost add)])
                               (when (< new-cost (vector-ref dp-curr new-idx))
                                 (vector-set! dp-curr new-idx new-cost)
                                 (vector-set! pred (+ (* i state-size) new-idx) prev-idx)))]
                            [(= prev-l 3) ; can switch character
                             (let* ([new-idx (+ (* next-c 3) 0)] ; length =1
                                    [new-cost (+ prev-cost add)])
                               (when (< new-cost (vector-ref dp-curr new-idx))
                                 (vector-set! dp-curr new-idx new-cost)
                                 (vector-set! pred (+ (* i state-size) new-idx) prev-idx)))]))))))))
              ;; move to next position
              (set! dp-prev dp-curr)))
          ;; find minimal cost among states with final run length >=3
          (let ([min-cost INF]
                [candidates '()])
            (for ([idx (in-range state-size)])
              (when (= (remainder idx 3) 2) ; length ==3 (>=3)
                (let ([cost (vector-ref dp-prev idx)])
                  (cond
                    [(< cost min-cost)
                     (set! min-cost cost)
                     (set! candidates (list idx))]
                    [(= cost min-cost)
                     (set! candidates (cons idx candidates))]))))
            (if (= min-cost INF)
                ""
                (let ([best #f])
                  (for ([end-idx (in-list candidates)])
                    (let ([s (let ([res (make-string n)])
                               (let loop ((i (- n 1)) (cur end-idx))
                                 (when (>= i 0)
                                   (let* ([c (quotient cur 3)]
                                          [ch (integer->char (+ base c))])
                                     (string-set! res i ch))
                                   (define prev (vector-ref pred (+ (* i state-size) cur)))
                                   (loop (- i 1) prev)))
                               res)])
                      (when (or (not best) (string<? s best))
                        (set! best s))))
                  best)))))))
```

## Erlang

```erlang
-spec min_cost_good_caption(Caption :: unicode:unicode_binary()) -> unicode:unicode_binary().
min_cost_good_caption(Caption) ->
    CodesList = [C - $a || <<C>> <= Caption],
    N = length(CodesList),
    case N < 3 of
        true -> <<"">>;
        false ->
            CodeTuple = list_to_tuple(CodesList),
            INF = 1 bsl 30,
            % DP array: index 0..N, each element #{start => integer(), chars => [tuple()]}
            EmptyCharCosts = lists:duplicate(26, {INF, INF, 0}),
            InitLayer = #{start => 0, chars => EmptyCharCosts},
            DP0 = array:new(N + 1, [{default, undefined}]),
            DP1 = array:set(N, InitLayer, DP0),
            DP = build_dp(CodeTuple, N - 1, INF, DP1),
            StartCost = (array:get(0, DP))#{start := SC} = array:get(0, DP), % extract start cost
            case SC >= INF of
                true -> <<"">>;
                false ->
                    ResultCodes = reconstruct(CodeTuple, DP, N),
                    list_to_binary([C + $a || C <- ResultCodes])
            end
    end.

%% Build DP backwards from position I down to 0.
build_dp(_CodeTuple, -1, _INF, DP) -> DP;
build_dp(CodeTuple, I, INF, DP) ->
    NextLayer = array:get(I + 1, DP),
    NextCharCosts = maps:get(chars, NextLayer),

    % compute char costs for each character
    CurrCharCosts = [char_costs_for_char(I, CIdx, CodeTuple, INF, NextCharCosts) ||
                    CIdx <- lists:seq(0, 25)],

    % start cost (no previous character)
    StartCost = min_start_cost(I, CodeTuple, INF, NextCharCosts),

    CurrLayer = #{start => StartCost, chars => CurrCharCosts},
    DP2 = array:set(I, CurrLayer, DP),
    build_dp(CodeTuple, I - 1, INF, DP2).

%% Minimum start cost at position I.
min_start_cost(I, CodeTuple, INF, NextCharCosts) ->
    CharAtPos = element(I + 1, CodeTuple),
    lists:foldl(fun(Nc, Acc) ->
        Mismatch = if Nc =:= CharAtPos -> 0; true -> 1 end,
        CostRest = cost_of_state(Nc, 1, NextCharCosts),
        Total = Mismatch + CostRest,
        if Total < Acc -> Total; true -> Acc end
    end, INF, lists:seq(0, 25)).

%% Compute costs for a given previous character CIdx at position I.
char_costs_for_char(I, CIdx, CodeTuple, INF, NextCharCosts) ->
    CharAtPos = element(I + 1, CodeTuple),
    Len1 = cost_len(I, CIdx, 1, CharAtPos, INF, NextCharCosts),
    Len2 = cost_len(I, CIdx, 2, CharAtPos, INF, NextCharCosts),
    Len3 = cost_len(I, CIdx, 3, CharAtPos, INF, NextCharCosts),
    {Len1, Len2, Len3}.

cost_len(I, CIdx, LenPrev, CharAtPos, INF, NextCharCosts) ->
    % continue with same character
    MismatchSame = if CIdx =:= CharAtPos -> 0; true -> 1 end,
    NewLenSame = case LenPrev of
        1 -> 2;
        2 -> 3;
        3 -> 3
    end,
    CostSame = MismatchSame + cost_of_state(CIdx, NewLenSame, NextCharCosts),

    % possibly switch to another character (only if previous length >=3)
    SwitchCost =
        case LenPrev of
            3 ->
                lists:foldl(fun(Nc, Acc) ->
                    if Nc =:= CIdx -> Acc;
                       true ->
                           Mismatch = if Nc =:= CharAtPos -> 0; true -> 1 end,
                           Total = Mismatch + cost_of_state(Nc, 1, NextCharCosts),
                           if Total < Acc -> Total; true -> Acc end
                    end
                end, INF, lists:seq(0, 25));
            _ -> INF
        end,
    min(CostSame, SwitchCost).

%% Retrieve cost for given character and run length from CharCosts list.
cost_of_state(CharIdx, Len, CharCosts) ->
    {C1, C2, C3} = lists:nth(CharIdx + 1, CharCosts),
    case Len of
        1 -> C1;
        2 -> C2;
        3 -> C3
    end.

min(A, B) when A =< B -> A;
min(_, B) -> B.

%% Reconstruct lexicographically smallest optimal caption.
reconstruct(CodeTuple, DP, N) ->
    reconstruct(0, undefined, 0, [], CodeTuple, DP, N).

reconstruct(I, _PrevChar, 0, Acc, CodeTuple, DP, N) when I < N ->
    Layer = array:get(I, DP),
    NextLayer = array:get(I + 1, DP),
    CharAtPos = element(I + 1, CodeTuple),
    StartCost = maps:get(start, Layer),
    Chosen = find_char(fun(Nc) ->
        Mismatch = if Nc =:= CharAtPos -> 0; true -> 1 end,
        CostRest = cost_of_state(Nc, 1, maps:get(chars, NextLayer)),
        Total = Mismatch + CostRest,
        Total =:= StartCost
    end),
    reconstruct(I + 1, Chosen, 1, [Chosen | Acc], CodeTuple, DP, N);
reconstruct(I, PrevChar, LenPrev, Acc, CodeTuple, DP, N) when I < N ->
    Layer = array:get(I, DP),
    NextLayer = array:get(I + 1, DP),
    CharAtPos = element(I + 1, CodeTuple),
    PrevTuple = lists:nth(PrevChar + 1, maps:get(chars, Layer)),
    PrevCost = case LenPrev of
        1 -> element(1, PrevTuple);
        2 -> element(2, PrevTuple);
        3 -> element(3, PrevTuple)
    end,
    Chosen = find_char(fun(Nc) ->
        if Nc =:= PrevChar ->
                NewLen = case LenPrev of 1 -> 2; 2 -> 3; 3 -> 3 end,
                Mismatch = if Nc =:= CharAtPos -> 0; true -> 1 end,
                CostRest = cost_of_state(Nc, NewLen, maps:get(chars, NextLayer)),
                Total = Mismatch + CostRest,
                Total =:= PrevCost;
           true ->
                case LenPrev of
                    3 ->
                        NewLen = 1,
                        Mismatch = if Nc =:= CharAtPos -> 0; true -> 1 end,
                        CostRest = cost_of_state(Nc, 1, maps:get(chars, NextLayer)),
                        Total = Mismatch + CostRest,
                        Total =:= PrevCost;
                    _ -> false
                end
        end
    end),
    NewLen = if Chosen =:= PrevChar ->
                 case LenPrev of 1 -> 2; 2 -> 3; 3 -> 3 end;
             true -> 1
            end,
    reconstruct(I + 1, Chosen, NewLen, [Chosen | Acc], CodeTuple, DP, N);
reconstruct(_I, _PrevChar, _LenPrev, Acc, _CodeTuple, _DP, _N) ->
    lists:reverse(Acc).

%% Find first character (0..25) satisfying predicate.
find_char(Pred) -> find_char(0, Pred).

find_char(26, _) -> 0; % should never happen
find_char(Nc, Pred) ->
    case Pred(Nc) of
        true -> Nc;
        false -> find_char(Nc + 1, Pred)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_cost_good_caption(caption :: String.t()) :: String.t()
  def min_cost_good_caption(caption) do
    chars = String.to_charlist(caption) |> Enum.map(&(&1 - ?a))
    n = length(chars)
    inf = 1_000_000_000

    # base tuple for position n: cost 0 only when previous run length == 3
    base_vals =
      for _c <- 0..25, l <- 1..3 do
        if l == 3, do: 0, else: inf
      end

    base_tuple = List.to_tuple(base_vals)
    dp0_base = inf

    # rows will hold {dp0_i, tuple_i} for i = 0 .. n (head is i=0)
    {rows, _} =
      Enum.reduce(Enum.reverse(chars), {[{dp0_base, base_tuple}], base_tuple}, fn orig,
                                                                              {acc_rows, next_tup} ->
        # dp0 when previous length == 0
        dp0_cur =
          0..25
          |> Enum.map(fn c ->
            cost = if c == orig, do: 0, else: 1
            idx = c * 3 + (1 - 1)
            cost + :erlang.element(idx + 1, next_tup)
          end)
          |> Enum.min()

        # compute tuple for states with previous length 1..3
        cur_vals =
          for c_prev <- 0..25, l_prev <- 1..3 do
            best =
              0..25
              |> Enum.reduce(inf, fn c_new, acc ->
                case allowed_newlen(c_prev, l_prev, c_new) do
                  {:ok, new_len} ->
                    cost = if c_new == orig, do: 0, else: 1
                    idx2 = c_new * 3 + (new_len - 1)
                    total = cost + :erlang.element(idx2 + 1, next_tup)
                    if total < acc, do: total, else: acc

                  :no ->
                    acc
                end
              end)

            best
          end

        cur_tuple = List.to_tuple(cur_vals)
        {[{dp0_cur, cur_tuple} | acc_rows], cur_tuple}
      end)

    [{dp0_start, _} | _] = rows

    if dp0_start >= inf do
      ""
    else
      result_chars =
        reconstruct(chars, rows, 26, 0, [])

      List.to_string(result_chars)
    end
  end

  # Helper to get value from tuple for given character and run length (1..3)
  defp get_val(tuple, c, len) do
    idx = c * 3 + (len - 1)
    :erlang.element(idx + 1, tuple)
  end

  # Determine if we can transition and the new run length
  defp allowed_newlen(_prev_c, 0, _cnew), do: {:ok, 1}

  defp allowed_newlen(prev_c, prev_len, cnew) when cnew == prev_c do
    new_len = if prev_len + 1 >= 3, do: 3, else: prev_len + 1
    {:ok, new_len}
  end

  defp allowed_newlen(_prev_c, 3, _cnew), do: {:ok, 1}
  defp allowed_newlen(_, _, _), do: :no

  # Reconstruct lexicographically smallest optimal string
  defp reconstruct([], [_], _prev_c, _prev_len, acc), do: Enum.reverse(acc)

  defp reconstruct([orig | rest_chars], [{dp0_i, tuple_i} = cur_row, {_, next_tuple} = next_row |
         remaining_rows],
    prev_c,
    prev_len,
    acc) do
    dp_cur =
      if prev_len == 0 do
        dp0_i
      else
        get_val(tuple_i, prev_c, prev_len)
      end

    chosen =
      Enum.find(0..25, fn c_new ->
        case allowed_newlen(prev_c, prev_len, c_new) do
          {:ok, new_len} ->
            cost = if c_new == orig, do: 0, else: 1
            dp_next = get_val(next_tuple, c_new, new_len)
            dp_cur == cost + dp_next

          :no ->
            false
        end
      end)

    {:ok, new_len} = allowed_newlen(prev_c, prev_len, chosen)

    reconstruct(
      rest_chars,
      [next_row | remaining_rows],
      chosen,
      new_len,
      [chosen + ?a | acc]
    )
  end
end
```
