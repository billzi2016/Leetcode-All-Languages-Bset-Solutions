# 2983. Palindrome Rearrangement Queries

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<bool> canMakePalindromeQueries(string s, vector<vector<int>>& queries) {
        int n = s.size();
        int half = n / 2;
        // prefix counts
        vector<array<int,26>> pref(n + 1);
        for (int i = 0; i < n; ++i) {
            pref[i+1] = pref[i];
            pref[i+1][s[i]-'a']++;
        }
        auto getFreq = [&](int l, int r)->array<int,26>{
            array<int,26> res{};
            if (l > r) return res;
            for (int c=0;c<26;++c) res[c] = pref[r+1][c] - pref[l][c];
            return res;
        };
        // mismatch prefix on left half
        vector<int> mismPref(half + 1, 0);
        for (int i = 0; i < half; ++i) {
            mismPref[i+1] = mismPref[i] + (s[i] != s[n-1-i]);
        }
        int totalMism = mismPref[half];
        vector<bool> ans;
        ans.reserve(queries.size());
        for (auto &q: queries) {
            int a=q[0], b=q[1], c=q[2], d=q[3];
            // uncovered mismatches
            int cntLeftIn = mismPref[b+1] - mismPref[a];
            int LrStart = n-1-d, LrEnd = n-1-c; // left indices whose counterpart in right interval
            int cntRightIn = 0;
            if (LrStart <= LrEnd)
                cntRightIn = mismPref[LrEnd+1] - mismPref[LrStart];
            int overlapLStart = max(a, LrStart);
            int overlapLEnd   = min(b, LrEnd);
            int cntBoth = 0;
            if (overlapLStart <= overlapLEnd)
                cntBoth = mismPref[overlapLEnd+1] - mismPref[overlapLStart];
            int uncovered = totalMism - cntLeftIn - cntRightIn + cntBoth;
            if (uncovered > 0) {
                ans.push_back(false);
                continue;
            }
            // frequency checks
            array<int,26> freqL = getFreq(a,b);
            array<int,26> freqR = getFreq(c,d);
            // overlap frequencies
            array<int,26> freqOverlapL{};
            array<int,26> freqOverlapR{};
            bool hasOverlap = (overlapLStart <= overlapLEnd);
            if (hasOverlap) {
                freqOverlapL = getFreq(overlapLStart, overlapLEnd);
                int ovRStart = n-1 - overlapLEnd;
                int ovREnd   = n-1 - overlapLStart;
                freqOverlapR = getFreq(ovRStart, ovREnd);
            }
            // needFromL : characters on right side whose counterpart left is in [a,b] but not overlapped
            array<int,26> freqJA = getFreq(n-1-b, n-1-a); // right indices symmetric to left interval
            array<int,26> needFromL{};
            for (int i=0;i<26;++i) needFromL[i] = freqJA[i] - (hasOverlap ? freqOverlapR[i] : 0);
            bool ok=true;
            for (int i=0;i<26 && ok;++i){
                if (needFromL[i] > freqL[i]) ok=false;
            }
            if (!ok){ ans.push_back(false); continue; }
            // needFromR
            array<int,26> freqIB = getFreq(n-1-d, n-1-c); // left indices symmetric to right interval
            array<int,26> needFromR{};
            for (int i=0;i<26;++i) needFromR[i] = freqIB[i] - (hasOverlap ? freqOverlapL[i] : 0);
            for (int i=0;i<26 && ok;++i){
                if (needFromR[i] > freqR[i]) ok=false;
            }
            if (!ok){ ans.push_back(false); continue; }
            // remaining frequencies must match
            array<int,26> remL{}, remR{};
            for (int i=0;i<26;++i){
                remL[i] = freqL[i] - needFromL[i];
                remR[i] = freqR[i] - needFromR[i];
                if (remL[i]!=remR[i]) ok=false;
            }
            ans.push_back(ok);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public boolean[] canMakePalindromeQueries(String s, int[][] queries) {
        int n = s.length();
        int half = n / 2;
        // prefix counts for whole string
        int[][] pref = new int[26][n + 1];
        for (int i = 0; i < n; i++) {
            int ch = s.charAt(i) - 'a';
            for (int c = 0; c < 26; c++) {
                pref[c][i + 1] = pref[c][i];
            }
            pref[ch][i + 1]++;
        }
        // mirror characters for left half positions
        int[][] prefMirror = new int[26][half + 1];
        for (int i = 0; i < half; i++) {
            int ch = s.charAt(n - 1 - i) - 'a';
            for (int c = 0; c < 26; c++) {
                prefMirror[c][i + 1] = prefMirror[c][i];
            }
            prefMirror[ch][i + 1]++;
        }
        // mismatch prefix for left half
        int[] mismPref = new int[half + 1];
        for (int i = 0; i < half; i++) {
            mismPref[i + 1] = mismPref[i] + (s.charAt(i) == s.charAt(n - 1 - i) ? 0 : 1);
        }
        boolean[] ans = new boolean[queries.length];
        for (int qi = 0; qi < queries.length; qi++) {
            int a = queries[qi][0];
            int b = queries[qi][1];
            int c = queries[qi][2];
            int d = queries[qi][3];
            // mirrored interval of [c,d] on left side
            int mrStart = n - 1 - d;
            int mrEnd = n - 1 - c;
            // intersection of L and MR
            int interL = Math.max(a, mrStart);
            int interR = Math.min(b, mrEnd);
            boolean hasInter = interL <= interR;

            // mismatches outside union
            int totalMism = mismPref[half];
            int mismInL = rangeSum(mismPref, a, b);
            int mismInMR = rangeSum(mismPref, mrStart, mrEnd);
            int mismInInter = hasInter ? rangeSum(mismPref, interL, interR) : 0;
            int mismOutside = totalMism - (mismInL + mismInMR - mismInInter);
            if (mismOutside > 0) {
                ans[qi] = false;
                continue;
            }

            boolean ok = true;
            for (int ch = 0; ch < 26; ch++) {
                int freqL = rangeSum(pref[ch], a, b);
                int freqR = rangeSum(pref[ch], c, d);

                int totalMirrorInL = rangeSum(prefMirror[ch], a, b);
                int mirrorInInter = hasInter ? rangeSum(prefMirror[ch], interL, interR) : 0;
                int requiredL = totalMirrorInL - mirrorInInter;

                int totalLeftInMR = rangeSum(pref[ch], mrStart, mrEnd);
                int leftInInter = hasInter ? rangeSum(pref[ch], interL, interR) : 0;
                int requiredR = totalLeftInMR - leftInInter;

                if (requiredL > freqL || requiredR > freqR) {
                    ok = false;
                    break;
                }
                int remaining = (freqL - requiredL) + (freqR - requiredR);
                if ((remaining & 1) == 1) {
                    ok = false;
                    break;
                }
            }
            ans[qi] = ok;
        }
        return ans;
    }

    private int rangeSum(int[] pref, int l, int r) { // inclusive
        if (l > r) return 0;
        return pref[r + 1] - pref[l];
    }
}
```

## Python

```python
class Solution(object):
    def canMakePalindromeQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        n = len(s)
        half = n // 2
        # prefix sums for character counts
        pref = [[0] * 26]
        for ch in s:
            cnt = pref[-1][:]
            cnt[ord(ch) - 97] += 1
            pref.append(cnt)

        # mismatch array for left half positions
        mism = [0] * half
        for i in range(half):
            if s[i] != s[n - 1 - i]:
                mism[i] = 1
        pref_mis = [0]
        for v in mism:
            pref_mis.append(pref_mis[-1] + v)
        total_mis = pref_mis[half]

        def get_counts(l, r):
            """inclusive l,r"""
            if l > r:
                return [0] * 26
            res = [pref[r + 1][k] - pref[l][k] for k in range(26)]
            return res

        def sum_mis(l, r):
            if l > r:
                return 0
            return pref_mis[r + 1] - pref_mis[l]

        ans = []
        for a, b, c, d in queries:
            # mismatch check
            mis_L = sum_mis(a, b)
            mirrorR_l = n - 1 - d
            mirrorR_r = n - 1 - c
            mis_mirrorR = sum_mis(mirrorR_l, mirrorR_r)

            interL_l = max(a, mirrorR_l)
            interL_r = min(b, mirrorR_r)
            mis_inter = sum_mis(interL_l, interL_r) if interL_l <= interL_r else 0

            covered = mis_L + mis_mirrorR - mis_inter
            if total_mis - covered > 0:
                ans.append(False)
                continue

            # character counts
            cntL = get_counts(a, b)
            cntR = get_counts(c, d)

            mirrorL_l = n - 1 - b
            mirrorL_r = n - 1 - a
            cntMirrorL = get_counts(mirrorL_l, mirrorL_r)

            cntMirrorR = get_counts(mirrorR_l, mirrorR_r)

            # intersections for flexible both sides
            interRL_l = max(c, mirrorL_l)
            interRL_r = min(d, mirrorL_r)
            cntInterRL = get_counts(interRL_l, interRL_r) if interRL_l <= interRL_r else [0]*26

            interLR_l = interL_l
            interLR_r = interL_r
            cntInterLR = get_counts(interLR_l, interLR_r) if interLR_l <= interLR_r else [0]*26

            neededFromL = [cntMirrorL[i] - cntInterRL[i] for i in range(26)]
            neededFromR = [cntMirrorR[i] - cntInterLR[i] for i in range(26)]

            possible = True
            for i in range(26):
                left_rem = cntL[i] - neededFromL[i]
                right_rem = cntR[i] - neededFromR[i]
                if left_rem < 0 or right_rem < 0 or left_rem != right_rem:
                    possible = False
                    break
            ans.append(possible)
        return ans
```

## Python3

```python
import sys
from typing import List

class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        half = n // 2

        # prefix counts for each character
        pref = [[0] * (n + 1) for _ in range(26)]
        for i, ch in enumerate(s):
            idx = ord(ch) - 97
            for c in range(26):
                pref[c][i + 1] = pref[c][i]
            pref[idx][i + 1] += 1

        def get_counts(l: int, r: int) -> List[int]:
            # assume l <= r and within [0, n-1]
            return [pref[c][r + 1] - pref[c][l] for c in range(26)]

        # diff array for left half
        diff = [0] * half
        for i in range(half):
            diff[i] = 1 if s[i] != s[n - 1 - i] else 0
        diff_ps = [0] * (half + 1)
        for i in range(half):
            diff_ps[i + 1] = diff_ps[i] + diff[i]

        def sum_diff(l: int, r: int) -> int:
            if l > r:
                return 0
            return diff_ps[r + 1] - diff_ps[l]

        total_mismatch = diff_ps[half]
        ans = []

        for a, b, c, d in queries:
            # mirrored range of right interval on left side
            mr_start = n - 1 - d
            mr_end = n - 1 - c

            sumLdiff = sum_diff(a, b)
            sumRdiff = sum_diff(mr_start, mr_end)

            ov_l = max(a, mr_start)
            ov_r = min(b, mr_end)
            if ov_l <= ov_r:
                sumBothDiff = sum_diff(ov_l, ov_r)
            else:
                sumBothDiff = 0

            # mismatches that must already match
            if total_mismatch - (sumLdiff + sumRdiff - sumBothDiff) != 0:
                ans.append(False)
                continue

            freqL = get_counts(a, b)
            freqR = get_counts(c, d)

            needL = [0] * 26
            needR = [0] * 26

            # left-only intervals (mutable on left, fixed on right)
            if ov_l <= ov_r:
                if a <= ov_l - 1:
                    l1, r1 = a, ov_l - 1
                    ml, mr = n - 1 - r1, n - 1 - l1
                    cnt = get_counts(ml, mr)
                    for k in range(26):
                        needL[k] += cnt[k]
                if ov_r + 1 <= b:
                    l2, r2 = ov_r + 1, b
                    ml, mr = n - 1 - r2, n - 1 - l2
                    cnt = get_counts(ml, mr)
                    for k in range(26):
                        needL[k] += cnt[k]
            else:
                ml, mr = n - 1 - b, n - 1 - a
                cnt = get_counts(ml, mr)
                for k in range(26):
                    needL[k] += cnt[k]

            # right-only intervals (mutable on right, fixed on left)
            if ov_l <= ov_r:
                j_start = n - 1 - ov_r
                j_end = n - 1 - ov_l
                if c <= j_start - 1:
                    l, r = c, j_start - 1
                    ml, mr = n - 1 - r, n - 1 - l
                    cnt = get_counts(ml, mr)
                    for k in range(26):
                        needR[k] += cnt[k]
                if j_end + 1 <= d:
                    l, r = j_end + 1, d
                    ml, mr = n - 1 - r, n - 1 - l
                    cnt = get_counts(ml, mr)
                    for k in range(26):
                        needR[k] += cnt[k]
            else:
                ml, mr = n - 1 - d, n - 1 - c
                cnt = get_counts(ml, mr)
                for k in range(26):
                    needR[k] += cnt[k]

            possible = True
            for k in range(26):
                if needL[k] > freqL[k] or needR[k] > freqR[k]:
                    possible = False
                    break
                remL = freqL[k] - needL[k]
                remR = freqR[k] - needR[k]
                if remL != remR:
                    possible = False
                    break

            ans.append(possible)

        return ans
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool* canMakePalindromeQueries(char* s, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    int n = (int)strlen(s);
    int m = n / 2;                     // left half size

    // prefix sums for character frequencies
    int (*pref)[26] = malloc((n + 1) * sizeof(int[26]));
    for (int c = 0; c < 26; ++c) pref[0][c] = 0;
    for (int i = 0; i < n; ++i) {
        for (int c = 0; c < 26; ++c) pref[i + 1][c] = pref[i][c];
        pref[i + 1][s[i] - 'a']++;
    }

    // diff prefix on left half: mismatched symmetric pairs
    int *diffPref = malloc((m + 1) * sizeof(int));
    diffPref[0] = 0;
    for (int i = 0; i < m; ++i) {
        diffPref[i + 1] = diffPref[i] + (s[i] != s[n - 1 - i]);
    }
    int totalDiff = diffPref[m];

    bool *ans = malloc(sizeof(bool) * queriesSize);
    *returnSize = queriesSize;

    for (int qi = 0; qi < queriesSize; ++qi) {
        int a = queries[qi][0];
        int b = queries[qi][1];
        int c = queries[qi][2];
        int d = queries[qi][3];

        // ----- check immutable mismatches -----
        int diffL = diffPref[b + 1] - diffPref[a];                     // in [a,b]
        int i_start = n - 1 - d;
        int i_end   = n - 1 - c;                                      // symmetric of right interval
        int diffI = diffPref[i_end + 1] - diffPref[i_start];          // in [i_start,i_end]

        int interL = a > i_start ? a : i_start;
        int interR = b < i_end   ? b : i_end;
        int diffOverlap = 0;
        if (interL <= interR) diffOverlap = diffPref[interR + 1] - diffPref[interL];

        int diffUnion = diffL + diffI - diffOverlap;
        if (totalDiff - diffUnion > 0) {
            ans[qi] = false;
            continue;
        }

        // ----- character counts in intervals -----
        int cntL[26], cntR[26];
        for (int ch = 0; ch < 26; ++ch) {
            cntL[ch] = pref[b + 1][ch] - pref[a][ch];
            cntR[ch] = pref[d + 1][ch] - pref[c][ch];
        }

        // ----- required matches from left interval (J_excl) -----
        int j_start = n - 1 - b;
        int j_end   = n - 1 - a;                                      // symmetric of [a,b]
        // overlap between J and R
        int ov_s = j_start > c ? j_start : c;
        int ov_e = j_end < d ? j_end : d;
        int cntOverlapJ[26] = {0};
        if (ov_s <= ov_e) {
            for (int ch = 0; ch < 26; ++ch)
                cntOverlapJ[ch] = pref[ov_e + 1][ch] - pref[ov_s][ch];
        }
        // total J counts
        int cntJ[26];
        for (int ch = 0; ch < 26; ++ch)
            cntJ[ch] = pref[j_end + 1][ch] - pref[j_start][ch];

        // characters that left interval must provide
        bool ok = true;
        for (int ch = 0; ch < 26; ++ch) {
            int need = cntJ[ch] - cntOverlapJ[ch];
            cntL[ch] -= need;
            if (cntL[ch] < 0) { ok = false; break; }
        }
        if (!ok) { ans[qi] = false; continue; }

        // ----- required matches from right interval (I_excl) -----
        int i_start2 = n - 1 - d;
        int i_end2   = n - 1 - c;                                      // same as i_start,i_end
        // overlap between I and L
        int ov2_s = i_start2 > a ? i_start2 : a;
        int ov2_e = i_end2 < b ? i_end2 : b;
        int cntOverlapI[26] = {0};
        if (ov2_s <= ov2_e) {
            for (int ch = 0; ch < 26; ++ch)
                cntOverlapI[ch] = pref[ov2_e + 1][ch] - pref[ov2_s][ch];
        }
        // total I counts
        int cntI[26];
        for (int ch = 0; ch < 26; ++ch)
            cntI[ch] = pref[i_end2 + 1][ch] - pref[i_start2][ch];

        // characters that right interval must provide
        for (int ch = 0; ch < 26; ++ch) {
            int need = cntI[ch] - cntOverlapI[ch];
            cntR[ch] -= need;
            if (cntR[ch] < 0) { ok = false; break; }
        }
        if (!ok) { ans[qi] = false; continue; }

        // ----- remaining counts must be equal -----
        for (int ch = 0; ch < 26; ++ch) {
            if (cntL[ch] != cntR[ch]) { ok = false; break; }
        }
        ans[qi] = ok;
    }

    free(pref);
    free(diffPref);
    return ans;
}
```

## Csharp

```csharp
using System;
public class Solution {
    public bool[] CanMakePalindromeQueries(string s, int[][] queries) {
        int n = s.Length;
        int half = n / 2;
        // prefix counts for each character
        int[][] pref = new int[26][];
        for (int c = 0; c < 26; ++c) pref[c] = new int[n + 1];
        for (int i = 0; i < n; ++i) {
            int ch = s[i] - 'a';
            for (int c = 0; c < 26; ++c) {
                pref[c][i + 1] = pref[c][i];
            }
            pref[ch][i + 1]++;
        }
        // mismatch prefix on left half
        int[] mismPref = new int[half + 1];
        for (int i = 0; i < half; ++i) {
            mismPref[i + 1] = mismPref[i] + (s[i] != s[n - 1 - i] ? 1 : 0);
        }
        int totalMism = mismPref[half];
        bool[] ans = new bool[queries.Length];
        for (int qi = 0; qi < queries.Length; ++qi) {
            int a = queries[qi][0], b = queries[qi][1];
            int c = queries[qi][2], d = queries[qi][3];
            // count chars in intervals
            int[] cntL = new int[26];
            int[] cntR = new int[26];
            for (int ch = 0; ch < 26; ++ch) {
                cntL[ch] = pref[ch][b + 1] - pref[ch][a];
                cntR[ch] = pref[ch][d + 1] - pref[ch][c];
            }
            // mismatch check outside flexible positions
            int mismInL = mismPref[b + 1] - mismPref[a];
            int symRStart = n - 1 - d;
            int symREnd = n - 1 - c;
            int mismInSymR = 0;
            if (symRStart <= symREnd) mismInSymR = mismPref[symREnd + 1] - mismPref[symRStart];
            int interStart = Math.Max(a, symRStart);
            int interEnd = Math.Min(b, symREnd);
            int mismInIntersection = 0;
            if (interStart <= interEnd) mismInIntersection = mismPref[interEnd + 1] - mismPref[interStart];
            int mismInUnion = mismInL + mismInSymR - mismInIntersection;
            if (totalMism - mismInUnion > 0) {
                ans[qi] = false;
                continue;
            }
            bool ok = true;
            // needed chars from left interval (symL \ R)
            int symLStart = n - 1 - b;
            int symLEnd = n - 1 - a;
            int overlapRStart = Math.Max(c, symLStart);
            int overlapREnd = Math.Min(d, symLEnd);
            bool hasOverlapRL = overlapRStart <= overlapREnd;
            for (int ch = 0; ch < 26; ++ch) {
                int need = pref[ch][symLEnd + 1] - pref[ch][symLStart];
                if (hasOverlapRL) need -= pref[ch][overlapREnd + 1] - pref[ch][overlapRStart];
                cntL[ch] -= need;
                if (cntL[ch] < 0) { ok = false; break; }
            }
            if (!ok) {
                ans[qi] = false;
                continue;
            }
            // needed chars from right interval (symR \ L)
            int symRStart2 = n - 1 - d;
            int symREnd2 = n - 1 - c;
            int overlapLStart = Math.Max(a, symRStart2);
            int overlapLEnd = Math.Min(b, symREnd2);
            bool hasOverlapLR = overlapLStart <= overlapLEnd;
            for (int ch = 0; ch < 26; ++ch) {
                int need = pref[ch][symREnd2 + 1] - pref[ch][symRStart2];
                if (hasOverlapLR) need -= pref[ch][overlapLEnd + 1] - pref[ch][overlapLStart];
                cntR[ch] -= need;
                if (cntR[ch] < 0) { ok = false; break; }
            }
            if (!ok) {
                ans[qi] = false;
                continue;
            }
            // compare remaining counts
            for (int ch = 0; ch < 26; ++ch) {
                if (cntL[ch] != cntR[ch]) { ok = false; break; }
            }
            ans[qi] = ok;
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number[][]} queries
 * @return {boolean[]}
 */
var canMakePalindromeQueries = function(s, queries) {
    const n = s.length;
    const half = n >> 1; // n is even

    // prefix mismatch for left side indices [0, half-1]
    const mism = new Uint8Array(half);
    for (let i = 0; i < half; ++i) {
        mism[i] = s.charCodeAt(i) === s.charCodeAt(n - 1 - i) ? 0 : 1;
    }
    const prefM = new Uint32Array(half + 1);
    for (let i = 0; i < half; ++i) {
        prefM[i + 1] = prefM[i] + mism[i];
    }

    // prefix counts for each character
    const pref = Array.from({ length: 26 }, () => new Uint32Array(n + 1));
    for (let i = 0; i < n; ++i) {
        const ch = s.charCodeAt(i) - 97;
        for (let c = 0; c < 26; ++c) {
            pref[c][i + 1] = pref[c][i];
        }
        pref[ch][i + 1]++;
    }

    // helper to get counts of chars in [l, r] inclusive
    const getCounts = (l, r) => {
        const cnt = new Uint32Array(26);
        if (l > r) return cnt;
        for (let c = 0; c < 26; ++c) {
            cnt[c] = pref[c][r + 1] - pref[c][l];
        }
        return cnt;
    };

    const totalMismatch = prefM[half];
    const ans = new Array(queries.length);

    for (let qi = 0; qi < queries.length; ++qi) {
        const [a, b, c, d] = queries[qi];

        // mismatch condition
        const mismL = prefM[b + 1] - prefM[a];
        const sStart = n - 1 - d;
        const sEnd   = n - 1 - c; // interval of left indices whose symmetric is in [c,d]
        const mismS = prefM[sEnd + 1] - prefM[sStart];

        const overlapL = Math.max(a, sStart);
        const overlapR = Math.min(b, sEnd);
        let overlapMis = 0;
        if (overlapL <= overlapR) {
            overlapMis = prefM[overlapR + 1] - prefM[overlapL];
        }

        const remainingMismatch = totalMismatch - mismL - mismS + overlapMis;
        if (remainingMismatch !== 0) {
            ans[qi] = false;
            continue;
        }

        // character count checks
        const freqL = getCounts(a, b);
        const freqR = getCounts(c, d);

        // symmetric interval of L in right half
        const symLStart = n - 1 - b;
        const symLEnd   = n - 1 - a;
        const freqS = getCounts(symLStart, symLEnd);

        let freqOverlapLeft = new Uint32Array(26);
        let freqOverlapRight = new Uint32Array(26);
        if (overlapL <= overlapR) {
            freqOverlapLeft = getCounts(overlapL, overlapR);
            const rOverlapStart = n - 1 - overlapR;
            const rOverlapEnd   = n - 1 - overlapL;
            freqOverlapRight = getCounts(rOverlapStart, rOverlapEnd);
        }

        // needed from L to match fixed right side
        let possible = true;
        const remL = new Uint32Array(26);
        for (let cIdx = 0; cIdx < 26; ++cIdx) {
            const needFromL = freqS[cIdx] - freqOverlapRight[cIdx];
            if (needFromL > freqL[cIdx]) { possible = false; break; }
            remL[cIdx] = freqL[cIdx] - needFromL;
        }
        if (!possible) { ans[qi] = false; continue; }

        // needed from R to match fixed left side
        const remR = new Uint32Array(26);
        for (let cIdx = 0; cIdx < 26; ++cIdx) {
            const needFromR = freqR[cIdx] - freqOverlapLeft[cIdx];
            if (needFromR > freqR[cIdx]) { possible = false; break; } // redundant but keep
            if (needFromR > freqR[cIdx]) { possible = false; break; }
            if (needFromR > freqR[cIdx]) { possible = false; break; }
            if (needFromR > freqR[cIdx]) { possible = false; break; }
            // actually need to ensure needFromR <= freqR, which always true because subtraction
            // but also need not exceed available after consumption; we compute remaining:
            remR[cIdx] = freqR[cIdx] - needFromR;
        }
        if (!possible) { ans[qi] = false; continue; }

        // finally, remaining multisets must be equal
        for (let cIdx = 0; cIdx < 26; ++cIdx) {
            if (remL[cIdx] !== remR[cIdx]) { possible = false; break; }
        }
        ans[qi] = possible;
    }

    return ans;
};
```

## Typescript

```typescript
function canMakePalindromeQueries(s: string, queries: number[][]): boolean[] {
    const n = s.length;
    const mid = n >> 1;

    // prefix sums for character counts
    const pref: Uint32Array[] = [];
    for (let c = 0; c < 26; ++c) pref.push(new Uint32Array(n + 1));
    for (let i = 0; i < n; ++i) {
        const ch = s.charCodeAt(i) - 97;
        for (let c = 0; c < 26; ++c) {
            pref[c][i + 1] = pref[c][i];
        }
        pref[ch][i + 1]++;
    }

    // diff array for mismatched pairs on left half
    const diff = new Uint8Array(mid);
    for (let i = 0; i < mid; ++i) {
        diff[i] = s.charCodeAt(i) === s.charCodeAt(n - 1 - i) ? 0 : 1;
    }
    const diffPref = new Uint32Array(mid + 1);
    for (let i = 0; i < mid; ++i) diffPref[i + 1] = diffPref[i] + diff[i];
    const totalDiff = diffPref[mid];

    const ans: boolean[] = [];

    // helper to fill frequency array for range [l, r] inclusive
    const fillFreq = (arr: Uint32Array, l: number, r: number) => {
        for (let c = 0; c < 26; ++c) {
            arr[c] = pref[c][r + 1] - pref[c][l];
        }
    };

    for (const q of queries) {
        const a = q[0], b = q[1], cIdx = q[2], d = q[3];

        // mismatch coverage check
        const countL = diffPref[b + 1] - diffPref[a];
        const L2 = n - 1 - d;
        const R2 = n - 1 - cIdx;
        const countR = diffPref[R2 + 1] - diffPref[L2];
        const interLeft = Math.max(a, L2);
        const interRight = Math.min(b, R2);
        const countBoth = (interLeft <= interRight) ? (diffPref[interRight + 1] - diffPref[interLeft]) : 0;
        const covered = countL + countR - countBoth;
        if (totalDiff > covered) {
            ans.push(false);
            continue;
        }

        // frequency arrays
        const freqL = new Uint32Array(26);
        const freqR = new Uint32Array(26);
        fillFreq(freqL, a, b);
        fillFreq(freqR, cIdx, d);

        // right side corresponding to left interval
        const rl = n - 1 - b;
        const rr = n - 1 - a;
        const freqRCor = new Uint32Array(26);
        fillFreq(freqRCor, rl, rr);
        const interRL = Math.max(rl, cIdx);
        const interRR = Math.min(rr, d);
        const needFromRightFixed = new Uint32Array(26);
        if (interRL <= interRR) {
            const freqIntersectR = new Uint32Array(26);
            fillFreq(freqIntersectR, interRL, interRR);
            for (let ch = 0; ch < 26; ++ch) needFromRightFixed[ch] = freqRCor[ch] - freqIntersectR[ch];
        } else {
            for (let ch = 0; ch < 26; ++ch) needFromRightFixed[ch] = freqRCor[ch];
        }

        // left side corresponding to right interval
        const ll = n - 1 - d;
        const lr = n - 1 - cIdx;
        const freqLCor = new Uint32Array(26);
        fillFreq(freqLCor, ll, lr);
        const interLL = Math.max(ll, a);
        const interLR = Math.min(lr, b);
        const needFromLeftFixed = new Uint32Array(26);
        if (interLL <= interLR) {
            const freqIntersectL = new Uint32Array(26);
            fillFreq(freqIntersectL, interLL, interLR);
            for (let ch = 0; ch < 26; ++ch) needFromLeftFixed[ch] = freqLCor[ch] - freqIntersectL[ch];
        } else {
            for (let ch = 0; ch < 26; ++ch) needFromLeftFixed[ch] = freqLCor[ch];
        }

        // verify remaining multisets are equal and non‑negative
        let ok = true;
        for (let ch = 0; ch < 26; ++ch) {
            const remL = freqL[ch] - needFromRightFixed[ch];
            const remR = freqR[ch] - needFromLeftFixed[ch];
            if (remL < 0 || remR < 0 || remL !== remR) {
                ok = false;
                break;
            }
        }
        ans.push(ok);
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param Integer[][] $queries
     * @return Boolean[]
     */
    function canMakePalindromeQueries($s, $queries) {
        $n = strlen($s);
        $half = intdiv($n, 2);

        // prefix sums for original string
        $pref = array_fill(0, 26, array_fill(0, $n + 1, 0));
        for ($i = 0; $i < $n; ++$i) {
            $ch = ord($s[$i]) - 97;
            for ($c = 0; $c < 26; ++$c) {
                $pref[$c][$i + 1] = $pref[$c][$i];
            }
            $pref[$ch][$i + 1]++;
        }

        // reversed string prefix sums (only first half indices are needed but we build for whole length)
        $rev = strrev($s);
        $prefRev = array_fill(0, 26, array_fill(0, $n + 1, 0));
        for ($i = 0; $i < $n; ++$i) {
            $ch = ord($rev[$i]) - 97;
            for ($c = 0; $c < 26; ++$c) {
                $prefRev[$c][$i + 1] = $prefRev[$c][$i];
            }
            $prefRev[$ch][$i + 1]++;
        }

        // mismatch array for first half
        $mis = [];
        for ($i = 0; $i < $half; ++$i) {
            $mis[$i] = ($s[$i] !== $s[$n - 1 - $i]) ? 1 : 0;
        }
        // prefix sum of mismatches
        $misPref = array_fill(0, $half + 1, 0);
        for ($i = 0; $i < $half; ++$i) {
            $misPref[$i + 1] = $misPref[$i] + $mis[$i];
        }

        $ans = [];

        foreach ($queries as $q) {
            [$a, $b, $c, $d] = $q;

            // ----- mismatch check -----
            $totalMis = $misPref[$half];

            $cntLmis = $misPref[$b + 1] - $misPref[$a];

            $mirrorStart = $n - 1 - $d;
            $mirrorEnd   = $n - 1 - $c; // inclusive, lies in [0, half-1]

            $cntRmirMis = 0;
            if ($mirrorStart <= $mirrorEnd) {
                $cntRmirMis = $misPref[$mirrorEnd + 1] - $misPref[$mirrorStart];
            }

            $interStart = max($a, $mirrorStart);
            $interEnd   = min($b, $mirrorEnd);
            $cntBoth = 0;
            if ($interStart <= $interEnd) {
                $cntBoth = $misPref[$interEnd + 1] - $misPref[$interStart];
            }

            $covered = $cntLmis + $cntRmirMis - $cntBoth;
            $uncovered = $totalMis - $covered;

            if ($uncovered > 0) {
                $ans[] = false;
                continue;
            }

            // ----- character counts -----
            // helper closure to get counts from a prefix array
            $getCounts = function($prefArr, $l, $r) {
                $cnt = [];
                for ($c = 0; $c < 26; ++$c) {
                    $cnt[$c] = $prefArr[$c][$r + 1] - $prefArr[$c][$l];
                }
                return $cnt;
            };

            // counts in mutable intervals
            $cntL = $getCounts($pref, $a, $b);
            $cntR = $getCounts($pref, $c, $d);

            // left-only: indices i in L but not in mirrorR -> need chars from rev side
            $leftAll = $getCounts($prefRev, $a, $b);
            if ($interStart <= $interEnd) {
                $leftInter = $getCounts($prefRev, $interStart, $interEnd);
                for ($c = 0; $c < 26; ++$c) {
                    $leftAll[$c] -= $leftInter[$c];
                }
            }
            // subtract from cntL
            $possible = true;
            for ($c = 0; $c < 26; ++$c) {
                $cntL[$c] -= $leftAll[$c];
                if ($cntL[$c] < 0) {
                    $possible = false;
                    break;
                }
            }
            if (!$possible) {
                $ans[] = false;
                continue;
            }

            // right-only: indices i in mirrorR but not in L -> need chars from original side
            $rightAll = $getCounts($pref, $mirrorStart, $mirrorEnd);
            if ($interStart <= $interEnd) {
                $rightInter = $getCounts($pref, $interStart, $interEnd);
                for ($c = 0; $c < 26; ++$c) {
                    $rightAll[$c] -= $rightInter[$c];
                }
            }
            // subtract from cntR
            for ($c = 0; $c < 26; ++$c) {
                $cntR[$c] -= $rightAll[$c];
                if ($cntR[$c] < 0) {
                    $possible = false;
                    break;
                }
            }
            if (!$possible) {
                $ans[] = false;
                continue;
            }

            // final check: remaining counts must match
            for ($c = 0; $c < 26; ++$c) {
                if ($cntL[$c] !== $cntR[$c]) {
                    $possible = false;
                    break;
                }
            }
            $ans[] = $possible;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func canMakePalindromeQueries(_ s: String, _ queries: [[Int]]) -> [Bool] {
        let n = s.count
        let half = n / 2
        let bytes = Array(s.utf8)
        // prefix sums for each character
        var pref = Array(repeating: Array(repeating: 0, count: n + 1), count: 26)
        for i in 0..<n {
            let chIdx = Int(bytes[i] - 97)
            for c in 0..<26 {
                pref[c][i + 1] = pref[c][i]
            }
            pref[chIdx][i + 1] += 1
        }
        // mismatched pairs on left half
        var diff = [Int](repeating: 0, count: half)
        for i in 0..<half {
            if bytes[i] != bytes[n - 1 - i] {
                diff[i] = 1
            }
        }
        var prefDiff = [Int](repeating: 0, count: half + 1)
        for i in 0..<half {
            prefDiff[i + 1] = prefDiff[i] + diff[i]
        }
        let totalDiff = prefDiff[half]
        
        func rangeCount(_ ch: Int, _ l: Int, _ r: Int) -> Int {
            if l > r { return 0 }
            return pref[ch][r + 1] - pref[ch][l]
        }
        func diffCount(_ l: Int, _ r: Int) -> Int {
            if l > r { return 0 }
            return prefDiff[r + 1] - prefDiff[l]
        }
        
        var result = [Bool]()
        for q in queries {
            let a = q[0], b = q[1], c = q[2], d = q[3]
            
            // check uncovered mismatches
            let diffInL = diffCount(a, b)
            let mirrorStart = max(0, n - 1 - d)
            let mirrorEnd = min(half - 1, n - 1 - c)
            let diffInMirrorR = diffCount(mirrorStart, mirrorEnd)
            let bothStart = max(a, n - 1 - d)
            let bothEnd = min(b, n - 1 - c)
            let diffInBoth = diffCount(bothStart, bothEnd)
            let uncovered = totalDiff - diffInL - diffInMirrorR + diffInBoth
            if uncovered > 0 {
                result.append(false)
                continue
            }
            
            // intervals for overlapping flexible pairs
            let leftOverlapL = max(a, n - 1 - d)
            let leftOverlapR = min(b, n - 1 - c)
            let rightOverlapL = max(c, n - 1 - b)
            let rightOverlapR = min(d, n - 1 - a)
            
            var possible = true
            for ch in 0..<26 {
                let cntL = rangeCount(ch, a, b)
                let cntR = rangeCount(ch, c, d)
                let overlapL = rangeCount(ch, leftOverlapL, leftOverlapR)
                let overlapR = rangeCount(ch, rightOverlapL, rightOverlapR)
                if cntL - overlapL != cntR - overlapR {
                    possible = false
                    break
                }
            }
            result.append(possible)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canMakePalindromeQueries(s: String, queries: Array<IntArray>): BooleanArray {
        val n = s.length
        val half = n / 2

        // Prefix sums for character frequencies
        val pref = Array(n + 1) { IntArray(26) }
        for (i in 0 until n) {
            val chIdx = s[i] - 'a'
            for (c in 0 until 26) {
                pref[i + 1][c] = pref[i][c]
            }
            pref[i + 1][chIdx]++
        }

        // Prefix sums for mismatches on the left half
        val prefMism = IntArray(half + 1)
        var totalMismatch = 0
        for (i in 0 until half) {
            if (s[i] != s[n - 1 - i]) totalMismatch++
            prefMism[i + 1] = totalMismatch
        }

        fun sumMism(l: Int, r: Int): Int {
            if (l > r) return 0
            return prefMism[r + 1] - prefMism[l]
        }

        fun getFreq(l: Int, r: Int): IntArray {
            val res = IntArray(26)
            if (l > r) return res
            for (c in 0 until 26) {
                res[c] = pref[r + 1][c] - pref[l][c]
            }
            return res
        }

        val ans = BooleanArray(queries.size)

        for (idx in queries.indices) {
            val q = queries[idx]
            val a = q[0]; val b = q[1]; val c = q[2]; val d = q[3]

            // Corresponding left indices of the right interval
            val rl = n - 1 - d
            val rr = n - 1 - c

            // Check fixed mismatches
            var unionMism = sumMism(a, b) + sumMism(rl, rr)
            val interL = maxOf(a, rl)
            val interR = minOf(b, rr)
            if (interL <= interR) {
                unionMism -= sumMism(interL, interR)
            }
            if (totalMismatch - unionMism != 0) {
                ans[idx] = false
                continue
            }

            // Frequencies in the two mutable intervals
            val freqL = getFreq(a, b)
            val freqR = getFreq(c, d)

            // Demand from left interval: characters needed from fixed right side positions
            val rightFromLStart = n - 1 - b
            val rightFromLEnd = n - 1 - a
            val freqRightFromL = getFreq(rightFromLStart, rightFromLEnd)
            val overlapStart = maxOf(rightFromLStart, c)
            val overlapEnd = minOf(rightFromLEnd, d)
            val overlapCounts = if (overlapStart <= overlapEnd) getFreq(overlapStart, overlapEnd) else IntArray(26)

            val demandL = IntArray(26)
            for (ch in 0 until 26) {
                demandL[ch] = freqRightFromL[ch] - overlapCounts[ch]
            }

            // Demand from right interval: characters needed from fixed left side positions
            val freqRevR = getFreq(rl, rr)   // chars on left whose counterpart is inside R
            val interCounts = if (interL <= interR) getFreq(interL, interR) else IntArray(26)
            val demandR = IntArray(26)
            for (ch in 0 until 26) {
                demandR[ch] = freqRevR[ch] - interCounts[ch]
            }

            // Remaining characters after satisfying demands
            var possible = true
            val remL = IntArray(26)
            val remR = IntArray(26)
            for (ch in 0 until 26) {
                val rL = freqL[ch] - demandL[ch]
                val rR = freqR[ch] - demandR[ch]
                if (rL < 0 || rR < 0) {
                    possible = false
                    break
                }
                remL[ch] = rL
                remR[ch] = rR
            }
            if (!possible) {
                ans[idx] = false
                continue
            }

            // The leftover characters must be pairable across the two intervals
            for (ch in 0 until 26) {
                if ((remL[ch] + remR[ch]) % 2 != 0) {
                    possible = false
                    break
                }
            }
            ans[idx] = possible
        }

        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<bool> canMakePalindromeQueries(String s, List<List<int>> queries) {
    int n = s.length;
    int half = n ~/ 2;

    // Prefix sums for character counts
    List<List<int>> pref = List.generate(26, (_) => List.filled(n + 1, 0));
    for (int i = 0; i < n; i++) {
      int ch = s.codeUnitAt(i) - 97;
      for (int c = 0; c < 26; c++) {
        pref[c][i + 1] = pref[c][i];
      }
      pref[ch][i + 1]++;
    }

    // Prefix sums for mismatches in pairs
    List<int> misPref = List.filled(half + 1, 0);
    for (int i = 0; i < half; i++) {
      int mism = s[i] == s[n - 1 - i] ? 0 : 1;
      misPref[i + 1] = misPref[i] + mism;
    }
    int totalMismatch = misPref[half];

    List<bool> ans = [];

    for (var q in queries) {
      int a = q[0], b = q[1], c = q[2], d = q[3];
      // intervals
      int irStart = n - 1 - d;
      int irEnd = n - 1 - c;

      // mismatches outside mutable intervals
      int mismatchInL = misPref[b + 1] - misPref[a];
      int mismatchInIR = (irStart <= irEnd)
          ? (misPref[irEnd + 1] - misPref[irStart])
          : 0;
      int interL = a > irStart ? a : irStart;
      int interR = b < irEnd ? b : irEnd;
      int mismatchInInter = 0;
      if (interL <= interR) {
        mismatchInInter = misPref[interR + 1] - misPref[interL];
      }
      int mismatchUnion = mismatchInL + mismatchInIR - mismatchInInter;
      int mismatchOutside = totalMismatch - mismatchUnion;

      bool possible = true;
      if (mismatchOutside > 0) {
        possible = false;
        ans.add(false);
        continue;
      }

      // character counts
      List<int> freqL = List.filled(26, 0);
      List<int> freqR = List.filled(26, 0);
      List<int> cntIR = List.filled(26, 0);
      List<int> interCnt = List.filled(26, 0);

      for (int ch = 0; ch < 26; ch++) {
        freqL[ch] = pref[ch][b + 1] - pref[ch][a];
        freqR[ch] = pref[ch][d + 1] - pref[ch][c];
        cntIR[ch] = pref[ch][irEnd + 1] - pref[ch][irStart];
        if (interL <= interR) {
          interCnt[ch] = pref[ch][interR + 1] - pref[ch][interL];
        }
      }

      // need from R to match fixed left side
      for (int ch = 0; ch < 26; ch++) {
        int needFromR = cntIR[ch] - interCnt[ch];
        if (needFromR > freqR[ch]) {
          possible = false;
          break;
        }
      }

      if (!possible) {
        ans.add(false);
        continue;
      }

      // remaining characters after satisfying fixed sides
      for (int ch = 0; ch < 26; ch++) {
        int remL = interCnt[ch];
        int needFromR = cntIR[ch] - interCnt[ch];
        int remR = freqR[ch] - needFromR;
        if (remL != remR) {
          possible = false;
          break;
        }
      }

      ans.add(possible);
    }

    return ans;
  }
}
```

## Golang

```go
func canMakePalindromeQueries(s string, queries [][]int) []bool {
	n := len(s)
	half := n / 2

	// prefix counts for characters
	pref := make([][26]int, n+1)
	for i := 0; i < n; i++ {
		copy(pref[i+1][:], pref[i][:])
		idx := s[i] - 'a'
		pref[i+1][idx]++
	}

	// diff array for left half vs mirrored right
	diff := make([]int, half)
	for i := 0; i < half; i++ {
		if s[i] != s[n-1-i] {
			diff[i] = 1
		}
	}
	// prefix sum of diff
	diffPref := make([]int, half+1)
	for i := 0; i < half; i++ {
		diffPref[i+1] = diffPref[i] + diff[i]
	}
	countDiff := func(l, r int) int { // inclusive
		if l > r {
			return 0
		}
		return diffPref[r+1] - diffPref[l]
	}

	getFreq := func(l, r int, out *[26]int) {
		for c := 0; c < 26; c++ {
			out[c] = pref[r+1][c] - pref[l][c]
		}
	}

	addRangeFreq := func(l, r int, dst *[26]int) {
		if l > r {
			return
		}
		for c := 0; c < 26; c++ {
			dst[c] += pref[r+1][c] - pref[l][c]
		}
	}

	ans := make([]bool, len(queries))
	for qi, q := range queries {
		a, b, c, d := q[0], q[1], q[2], q[3]

		var freqL, freqR [26]int
		getFreq(a, b, &freqL)
		getFreq(c, d, &freqR)

		// needed characters from L to match fixed right side
		var needL [26]int
		jLStart := n - 1 - b
		jLEnd := n - 1 - a

		if c > half { // complement part [half, c-1]
			l := jLStart
			if l < half {
				l = half
			}
			r := jLEnd
			if r > c-1 {
				r = c - 1
			}
			addRangeFreq(l, r, &needL)
		}
		if d < n-1 { // complement part [d+1, n-1]
			l := jLStart
			if l < d+1 {
				l = d + 1
			}
			r := jLEnd
			if r > n-1 {
				r = n - 1
			}
			addRangeFreq(l, r, &needL)
		}

		// needed characters from R to match fixed left side
		var needR [26]int
		iRStart := n - 1 - d
		iREnd := n - 1 - c

		if a > 0 { // complement left part [0, a-1]
			l := iRStart
			if l < 0 {
				l = 0
			}
			r := iREnd
			if r > a-1 {
				r = a - 1
			}
			addRangeFreq(l, r, &needR)
		}
		if b < half-1 { // complement left part [b+1, half-1]
			l := iRStart
			if l < b+1 {
				l = b + 1
			}
			r := iREnd
			if r > half-1 {
				r = half - 1
			}
			addRangeFreq(l, r, &needR)
		}

		// check availability and compute remaining counts
		var remL, remR [26]int
		ok := true
		for ch := 0; ch < 26; ch++ {
			if needL[ch] > freqL[ch] {
				ok = false
				break
			}
			remL[ch] = freqL[ch] - needL[ch]
			if needR[ch] > freqR[ch] {
				ok = false
				break
			}
			remR[ch] = freqR[ch] - needR[ch]
		}
		if !ok {
			ans[qi] = false
			continue
		}

		// remaining multisets must be identical
		for ch := 0; ch < 26 && ok; ch++ {
			if remL[ch] != remR[ch] {
				ok = false
			}
		}
		if !ok {
			ans[qi] = false
			continue
		}

		// check immutable mismatched pairs (both sides fixed)
		totalImm := 0
		leftRange1End := n - d - 2
		if leftRange1End >= 0 {
			totalImm += countDiff(0, leftRange1End)
		}
		leftRange2Start := n - c
		if leftRange2Start <= half-1 {
			totalImm += countDiff(leftRange2Start, half-1)
		}

		mutInL := 0
		if a <= b {
			if leftRange1End >= 0 {
				l := a
				if l < 0 {
					l = 0
				}
				r := b
				if r > leftRange1End {
					r = leftRange1End
				}
				if l <= r {
					mutInL += countDiff(l, r)
				}
			}
			if leftRange2Start <= half-1 {
				l := a
				if l < leftRange2Start {
					l = leftRange2Start
				}
				r := b
				if r > half-1 {
					r = half - 1
				}
				if l <= r {
					mutInL += countDiff(l, r)
				}
			}
		}
		if totalImm-mutInL > 0 {
			ans[qi] = false
			continue
		}

		ans[qi] = true
	}
	return ans
}
```

## Ruby

```ruby
def can_make_palindrome_queries(s, queries)
  n = s.length
  half = n / 2
  total_mismatch = 0

  # Prefix sums for left half characters
  pref_l = Array.new(26) { Array.new(half + 1, 0) }
  # Prefix sums for mirrored right-half characters (mapped to left indices)
  pref_r = Array.new(26) { Array.new(half + 1, 0) }
  # Prefix sums for whole string (for right interval counts)
  pref_all = Array.new(26) { Array.new(n + 1, 0) }
  # Mismatch prefix
  pref_mis = Array.new(half + 1, 0)

  half.times do |i|
    ch_l = s.getbyte(i) - 97
    ch_r = s.getbyte(n - 1 - i) - 97

    26.times do |c|
      pref_l[c][i + 1] = pref_l[c][i]
      pref_r[c][i + 1] = pref_r[c][i]
    end
    pref_l[ch_l][i + 1] += 1
    pref_r[ch_r][i + 1] += 1

    pref_mis[i + 1] = pref_mis[i] + (ch_l == ch_r ? 0 : 1)
  end

  n.times do |i|
    ch = s.getbyte(i) - 97
    26.times { |c| pref_all[c][i + 1] = pref_all[c][i] }
    pref_all[ch][i + 1] += 1
  end

  total_mismatch = pref_mis[half]

  answers = []

  queries.each do |a, b, c, d|
    # Map right interval to left indices
    l_left = n - 1 - d
    l_right = n - 1 - c

    # Overlap of [a,b] and [l_left,l_right]
    over_start = [a, l_left].max
    over_end   = [b, l_right].min
    has_overlap = over_start <= over_end

    demand_l = Array.new(26, 0)
    demand_r = Array.new(26, 0)

    # Demand from left interval (need chars from right side)
    if has_overlap
      if a < over_start
        l = a
        r = over_start - 1
        26.times { |ch| demand_l[ch] += pref_r[ch][r + 1] - pref_r[ch][l] }
      end
      if over_end < b
        l = over_end + 1
        r = b
        26.times { |ch| demand_l[ch] += pref_r[ch][r + 1] - pref_r[ch][l] }
      end
    else
      l = a
      r = b
      26.times { |ch| demand_l[ch] += pref_r[ch][r + 1] - pref_r[ch][l] }
    end

    # Demand from right interval (need chars from left side)
    if has_overlap
      if l_left < over_start
        l = l_left
        r = over_start - 1
        26.times { |ch| demand_r[ch] += pref_l[ch][r + 1] - pref_l[ch][l] }
      end
      if over_end < l_right
        l = over_end + 1
        r = l_right
        26.times { |ch| demand_r[ch] += pref_l[ch][r + 1] - pref_l[ch][l] }
      end
    else
      l = l_left
      r = l_right
      26.times { |ch| demand_r[ch] += pref_l[ch][r + 1] - pref_l[ch][l] }
    end

    # Frequencies in intervals
    freq_l = Array.new(26, 0)
    freq_r = Array.new(26, 0)
    26.times do |ch|
      freq_l[ch] = pref_l[ch][b + 1] - pref_l[ch][a]
      freq_r[ch] = pref_all[ch][d + 1] - pref_all[ch][c]
    end

    valid = true
    26.times do |ch|
      if demand_l[ch] > freq_l[ch] || demand_r[ch] > freq_r[ch]
        valid = false
        break
      end
    end

    if valid
      26.times do |ch|
        if (freq_l[ch] - demand_l[ch]) != (freq_r[ch] - demand_r[ch])
          valid = false
          break
        end
      end
    end

    # Mismatch check for uncovered pairs
    mis_a = pref_mis[b + 1] - pref_mis[a]
    mis_b = pref_mis[l_right + 1] - pref_mis[l_left]
    mis_overlap = has_overlap ? (pref_mis[over_end + 1] - pref_mis[over_start]) : 0
    covered_mis = mis_a + mis_b - mis_overlap
    uncovered_mis = total_mismatch - covered_mis
    valid &&= (uncovered_mis == 0)

    answers << valid
  end

  answers
end
```

## Scala

```scala
object Solution {
    def canMakePalindromeQueries(s: String, queries: Array[Array[Int]]): Array[Boolean] = {
        val n = s.length
        val half = n / 2

        // prefix frequencies for each character
        val pref = Array.ofDim[Int](26, n + 1)
        var i = 0
        while (i < n) {
            val chIdx = s.charAt(i) - 'a'
            var c = 0
            while (c < 26) {
                pref(c)(i + 1) = pref(c)(i)
                c += 1
            }
            pref(chIdx)(i + 1) += 1
            i += 1
        }

        // prefix sum of mismatches on the left half
        val misPref = new Array[Int](half + 1)
        var idx = 0
        while (idx < half) {
            misPref(idx + 1) = misPref(idx) + (if (s.charAt(idx) != s.charAt(n - 1 - idx)) 1 else 0)
            idx += 1
        }
        val totalMis = misPref(half)

        def getFreq(l: Int, r: Int, out: Array[Int]): Unit = {
            var c = 0
            while (c < 26) {
                out(c) = pref(c)(r + 1) - pref(c)(l)
                c += 1
            }
        }

        def rangeMis(l: Int, r: Int): Int =
            if (l > r) 0 else misPref(r + 1) - misPref(l)

        val ans = new Array[Boolean](queries.length)
        var qIdx = 0
        while (qIdx < queries.length) {
            val q = queries(qIdx)
            val a = q(0)
            val b = q(1)
            val cIdx = q(2)
            val dIdx = q(3)

            // frequencies of left interval and its counterpart range
            val cntL = new Array[Int](26)
            getFreq(a, b, cntL)

            val cl = n - 1 - b
            val cr = n - 1 - a
            val freqC = new Array[Int](26)
            getFreq(cl, cr, freqC)

            var ok = true
            var ch = 0
            while (ch < 26 && ok) {
                if (cntL(ch) != freqC(ch)) ok = false
                ch += 1
            }

            if (ok) {
                // check uncovered mismatches
                val nl = n - 1 - dIdx
                val nr = n - 1 - cIdx

                val misAB = rangeMis(a, b)
                val misNR = rangeMis(nl, nr)

                val interL = Math.max(a, nl)
                val interR = Math.min(b, nr)
                val misInter = if (interL <= interR) rangeMis(interL, interR) else 0

                val unionMis = misAB + misNR - misInter
                val uncovered = totalMis - unionMis
                if (uncovered > 0) ok = false
            }

            ans(qIdx) = ok
            qIdx += 1
        }
        ans
    }
}
```

## Rust

```rust
use std::cmp::{max, min};

impl Solution {
    pub fn can_make_palindrome_queries(s: String, queries: Vec<Vec<i32>>) -> Vec<bool> {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let half = n / 2;

        // prefix sums of character counts
        let mut pref: Vec<[i32; 26]> = vec![[0; 26]; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i];
            let idx = (bytes[i] - b'a') as usize;
            pref[i + 1][idx] += 1;
        }

        // diff array for left half: whether s[i] != s[n-1-i]
        let mut diff_pref: Vec<i32> = vec![0; half + 1];
        for i in 0..half {
            let d = if bytes[i] != bytes[n - 1 - i] { 1 } else { 0 };
            diff_pref[i + 1] = diff_pref[i] + d;
        }

        // helper to get char counts in [l, r] inclusive
        let get_counts = |l: usize, r: usize, pref: &Vec<[i32; 26]>| -> [i32; 26] {
            if l > r {
                return [0; 26];
            }
            let mut res = [0i32; 26];
            for c in 0..26 {
                res[c] = pref[r + 1][c] - pref[l][c];
            }
            res
        };

        // helper to get diff sum in [l, r]
        let get_diff = |l: usize, r: usize, diff_pref: &Vec<i32>| -> i32 {
            if l > r {
                return 0;
            }
            diff_pref[r + 1] - diff_pref[l]
        };

        let total_mismatch = diff_pref[half];
        let mut ans: Vec<bool> = Vec::with_capacity(queries.len());

        for q in queries.iter() {
            let a = q[0] as usize;
            let b = q[1] as usize;
            let c = q[2] as usize;
            let d = q[3] as usize;

            // mirror interval of [c,d] on the left half
            let ml = n - 1 - d; // left index inclusive
            let mr = n - 1 - c; // left index inclusive

            // intersection of L and mirrorR
            let int_l = max(a, ml);
            let int_r = min(b, mr);
            let has_inter = int_l <= int_r;

            // fixed mismatches check
            let mismatch_L = get_diff(a, b, &diff_pref);
            let mismatch_mirror = get_diff(ml, mr, &diff_pref);
            let mismatch_int = if has_inter {
                get_diff(int_l, int_r, &diff_pref)
            } else {
                0
            };
            let mutable_mismatch = mismatch_L + mismatch_mirror - mismatch_int;
            if total_mismatch - mutable_mismatch > 0 {
                ans.push(false);
                continue;
            }

            // character counts
            let freqL = get_counts(a, b, &pref);
            let freqR = get_counts(c, d, &pref);
            let cntMirrorLeft = get_counts(ml, mr, &pref); // left side positions whose mirrors are in [c,d]

            let cntIntersect = if has_inter {
                get_counts(int_l, int_r, &pref)
            } else {
                [0; 26]
            };

            // overlap on right side (mirror of intersect)
            let cntOverlapR = if has_inter {
                let rl = n - 1 - int_r;
                let rr = n - 1 - int_l;
                get_counts(rl, rr, &pref)
            } else {
                [0; 26]
            };

            // requirements
            let mut req_from_L = freqR; // need chars from L to match fixed right side
            for i in 0..26 {
                req_from_L[i] -= cntOverlapR[i];
            }

            let mut req_from_R = cntMirrorLeft;
            for i in 0..26 {
                req_from_R[i] -= cntIntersect[i];
            }

            // check availability and compute remaining
            let mut ok = true;
            let mut remL = [0i32; 26];
            let mut remR = [0i32; 26];
            for i in 0..26 {
                if req_from_L[i] > freqL[i] || req_from_R[i] > freqR[i] {
                    ok = false;
                    break;
                }
                remL[i] = freqL[i] - req_from_L[i];
                remR[i] = freqR[i] - req_from_R[i];
            }

            if !ok {
                ans.push(false);
                continue;
            }

            // remaining multisets must be equal
            for i in 0..26 {
                if remL[i] != remR[i] {
                    ok = false;
                    break;
                }
            }
            ans.push(ok);
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (can-make-palindrome-queries s queries)
  (-> string? (listof (listof exact-integer?)) (listof boolean?))
  (let* ((n (string-length s))
         (half (/ n 2))
         ;; prefix counts for each character
         (pref (let ((arr (make-vector 26)))
                 (for ([c (in-range 26)])
                   (vector-set! arr c (make-vector (+ n 1) 0)))
                 arr))
         ;; build prefix sums
         (_ (let loop ((i 0))
              (when (< i n)
                (let* ((ch (- (char->integer (string-ref s i))
                              (char->integer #\a))))
                  (for ([c (in-range 26)])
                    (let* ((v (vector-ref pref c))
                           (prev (vector-ref v i))
                           (new (+ prev (if (= c ch) 1 0))))
                      (vector-set! v (+ i 1) new)))
                  (loop (+ i 1))))))
         ;; mismatch prefix over left half
         (mismatch-pref (let ((v (make-vector (+ half 1) 0)))
                          (let loop ((i 0))
                            (if (= i half)
                                v
                                (let* ((mis (if (char=? (string-ref s i)
                                                (string-ref s (- n 1 i))) 0 1))
                                       (prev (vector-ref v i))
                                       (new (+ prev mis)))
                                  (vector-set! v (+ i 1) new)
                                  (loop (+ i 1)))))))
         (total-mism (vector-ref mismatch-pref half)))
    (map
     (lambda (qr)
       (let* ((a (list-ref qr 0))
              (b (list-ref qr 1))
              (c (list-ref qr 2))
              (d (list-ref qr 3))
              ;; mismatches covered by mutable sides
              (cntL-mism (- (vector-ref mismatch-pref (+ b 1))
                            (vector-ref mismatch-pref a)))
              (ls (- n 1 d))          ; left index corresponding to right end
              (le (- n 1 c))          ; left index corresponding to right start
              (cntR-mism (- (vector-ref mismatch-pref (+ le 1))
                            (vector-ref mismatch-pref ls)))
              (ovl (max a ls))
              (ovr (min b le))
              (hasOverlap (<= ovl ovr))
              (cntOverlap-mism (if hasOverlap
                                   (- (vector-ref mismatch-pref (+ ovr 1))
                                      (vector-ref mismatch-pref ovl))
                                   0))
              (covered (if hasOverlap
                           (- (+ cntL-mism cntR-mism) cntOverlap-mism)
                           (+ cntL-mism cntR-mism))))
         (if (not (= covered total-mism))
             #f
             ;; character count feasibility
             (let* ((mirStart (- n 1 b))   ; mirror of left interval start
                    (mirEnd   (- n 1 a)))  ; mirror of left interval end
               (let loop ((ch 0) (ok #t))
                 (if (or (not ok) (= ch 26))
                     ok
                     (let* ((v (vector-ref pref ch))
                            ;; counts in mutable intervals
                            (cntL (- (vector-ref v (+ b 1)) (vector-ref v a)))
                            (cntR (- (vector-ref v (+ d 1)) (vector-ref v c)))
                            ;; total chars in mirror of L
                            (cntMirror (- (vector-ref v (+ mirEnd 1))
                                          (vector-ref v mirStart)))
                            ;; overlap part between mirrorL and R
                            (cntOverlapRight (if hasOverlap
                                                 (let ((or-start (- n 1 ovr))
                                                       (or-end   (- n 1 ovl)))
                                                   (- (vector-ref v (+ or-end 1))
                                                      (vector-ref v or-start)))
                                                 0))
                            (demandL (- cntMirror cntOverlapRight))
                            ;; chars in I_R (left side corresponding to right interval)
                            (cntIR (- (vector-ref v (+ le 1)) (vector-ref v ls)))
                            (cntOverlapLeft (if hasOverlap
                                                (- (vector-ref v (+ ovr 1))
                                                   (vector-ref v ovl))
                                                0))
                            (demandR (- cntIR cntOverlapLeft))
                            (remL (- cntL demandL))
                            (remR (- cntR demandR)))
                       (loop (+ ch 1)
                             (and ok
                                  (= remL remR)
                                  (>= cntL demandL)
                                  (>= cntR demandR)))))))))))
     queries)))
```

## Erlang

```erlang
-spec can_make_palindrome_queries(S :: unicode:unicode_binary(), Queries :: [[integer()]]) -> [boolean()].
can_make_palindrome_queries(S, Queries) ->
    N = byte_size(S),
    M = N div 2,
    ZeroTuple = erlang:make_tuple(26, 0),

    %% Build prefix arrays for left half, right half and mismatch prefix
    {LeftPref, RightPref, MisPref} = build_prefixes(S, N, M, ZeroTuple),

    TotalMis = array:get(M, MisPref),

    lists:map(
      fun([A, B, C, D]) ->
          %% frequency vectors for intervals
          FreqL = range_counts(LeftPref, A, B),
          RcStart = C - M,
          RcEnd   = D - M,
          FreqR = range_counts(RightPref, RcStart, RcEnd),

          %% Right side positions whose left counterpart lies in [A,B]
          RaAbsL = max(N - 1 - B, M),
          RaAbsR = min(N - 1 - A, N - 1),
          {FreqRA, OverlapRA} =
              if RaAbsL =< RaAbsR ->
                     RAStart = RaAbsL - M,
                     RAEnd   = RaAbsR - M,
                     Freq = range_counts(RightPref, RAStart, RAEnd),
                     OvL = max(RaAbsL, C) - M,
                     OvR = min(RaAbsR, D) - M,
                     Overlap = if OvL =< OvR -> range_counts(RightPref, OvL, OvR); true -> zero_tuple() end,
                     {Freq, Overlap};
                 true ->
                     {zero_tuple(), zero_tuple()}
              end,
          RequiredLeft = tuple_sub(FreqRA, OverlapRA),

          %% Left side positions whose right counterpart lies in [C,D]
          LcAbsL = max(N - 1 - D, 0),
          LcAbsR = min(N - 1 - C, M - 1),
          {FreqLC, OverlapLC} =
              if LcAbsL =< LcAbsR ->
                     LCStart = LcAbsL,
                     LCEnd   = LcAbsR,
                     Freq = range_counts(LeftPref, LCStart, LCEnd),
                     OvL = max(LcAbsL, A),
                     OvR = min(LcAbsR, B),
                     Overlap = if OvL =< OvR -> range_counts(LeftPref, OvL, OvR); true -> zero_tuple() end,
                     {Freq, Overlap};
                 true ->
                     {zero_tuple(), zero_tuple()}
              end,
          RequiredRight = tuple_sub(FreqLC, OverlapLC),

          %% Check character feasibility
          case check_vectors(FreqL, FreqR, RequiredLeft, RequiredRight) of
              false -> false;
              true ->
                  %% Mismatch checks
                  MisA = range_mis(MisPref, A, B),
                  MisC = if LcAbsL =< LcAbsR -> range_mis(MisPref, LcAbsL, LcAbsR); true -> 0 end,
                  BothL = max(A, LcAbsL),
                  BothR = min(B, LcAbsR),
                  MisBoth = if BothL =< BothR -> range_mis(MisPref, BothL, BothR); true -> 0 end,
                  RemainingMis = TotalMis - (MisA + MisC - MisBoth),
                  RemainingMis == 0
          end
      end,
      Queries).

%% Build prefix arrays for left half, right half and mismatch prefix
build_prefixes(S, N, M, ZeroTuple) ->
    LeftPref0 = array:new(M+1, {default, ZeroTuple}),
    RightPref0 = array:new(M+1, {default, ZeroTuple}),
    MisPref0   = array:new(M+1, {default, 0}),
    build_prefixes_loop(0, N, M, S, LeftPref0, RightPref0, MisPref0).

build_prefixes_loop(I, N, M, S, LPref, RPref, MPref) when I == M ->
    {LPref, RPref, MPref};
build_prefixes_loop(I, N, M, S, LPref, RPref, MPref) ->
    CharL = binary:at(S, I),
    PrevL = array:get(I, LPref),
    NewL  = inc_tuple(PrevL, CharL - $a),
    LPref1 = array:set(I+1, NewL, LPref),

    J = M + I,
    CharR = binary:at(S, J),
    PrevR = array:get(I, RPref),
    NewR  = inc_tuple(PrevR, CharR - $a),
    RPref1 = array:set(I+1, NewR, RPref),

    MirrorIdx = N - 1 - I,
    CharM = binary:at(S, MirrorIdx),
    Mis = if CharL == CharM -> 0; true -> 1 end,
    PrevMis = array:get(I, MPref),
    MPref1 = array:set(I+1, PrevMis + Mis, MPref),

    build_prefixes_loop(I+1, N, M, S, LPref1, RPref1, MPref1).

%% Increment count of character at index Idx (0..25) in tuple
inc_tuple(Tuple, Idx) ->
    Pos = Idx + 1,
    Old = element(Pos, Tuple),
    setelement(Pos, Tuple, Old + 1).

zero_tuple() -> erlang:make_tuple(26, 0).

%% Get frequency vector for range [L,R] inclusive from prefix array
range_counts(Pref, L, R) when L =< R ->
    Upper = array:get(R+1, Pref),
    Lower = array:get(L, Pref),
    tuple_sub(Upper, Lower);
range_counts(_, _, _) -> zero_tuple().

%% Subtract two tuples elementwise (A - B)
tuple_sub(A, B) ->
    list_to_tuple(
      [element(I, A) - element(I, B) || I <- lists:seq(1, 26)]
    ).

list_to_tuple(L) -> erlang:list_to_tuple(L).

%% Check character feasibility
check_vectors(FreqL, FreqR, ReqL, ReqR) ->
    check_vectors_loop(1, FreqL, FreqR, ReqL, ReqR).

check_vectors_loop(I, FL, FR, RL, RR) when I =< 26 ->
    Lc = element(I, FL),
    Rc = element(I, FR),
    Rl = element(I, RL),
    Rr = element(I, RR),
    if Rl > Lc orelse Rr > Rc -> false;
       true ->
           RemL = Lc - Rl,
           RemR = Rc - Rr,
           if RemL =/= RemR -> false; true -> check_vectors_loop(I+1, FL, FR, RL, RR) end
    end;
check_vectors_loop(_, _, _, _, _) -> true.

%% Mismatch prefix sum for range [L,R]
range_mis(MisPref, L, R) when L =< R ->
    array:get(R+1, MisPref) - array:get(L, MisPref);
range_mis(_, _, _) -> 0.
```

## Elixir

```elixir
defmodule Solution do
  @spec can_make_palindrome_queries(s :: String.t(), queries :: [[integer]]) :: [boolean]
  def can_make_palindrome_queries(s, queries) do
    chars = :binary.bin_to_list(s)
    n = length(chars)
    half = div(n, 2)

    # prefix sums for each character (26 arrays of size n+1)
    pref_arrays = build_prefix(chars, n)

    # mismatch array and its prefix sum for left half
    {mismatch_pref, total_mismatches} = build_mismatch_prefix(chars, half)

    Enum.map(queries, fn [a, b, c, d] ->
      ir_l = n - 1 - d
      ir_r = n - 1 - c

      # check uncovered mismatches
      m_in_L = range_sum(mismatch_pref, a, b)
      m_in_R = range_sum(mismatch_pref, ir_l, ir_r)

      overlap_l = max(a, ir_l)
      overlap_r = min(b, ir_r)

      m_both =
        if overlap_l <= overlap_r do
          range_sum(mismatch_pref, overlap_l, overlap_r)
        else
          0
        end

      uncovered = total_mismatches - m_in_L - m_in_R + m_both

      if uncovered > 0 do
        false
      else
        # get counts for L and R intervals
        l_counts = get_counts(pref_arrays, a, b)
        r_counts = get_counts(pref_arrays, c, d)

        # left-only intervals (L \ I_R)
        {l_counts, ok1} =
          adjust_left_only(l_counts, pref_arrays, a, b, ir_l, ir_r, n)

        if not ok1 do
          false
        else
          # right-only intervals (R \ I_L)
          {r_counts, ok2} =
            adjust_right_only(r_counts, pref_arrays, a, b, ir_l, ir_r, n)

          if not ok2 do
            false
          else
            l_counts == r_counts
          end
        end
      end
    end)
  end

  # Build prefix arrays for each character
  defp build_prefix(chars, n) do
    base = Enum.map(0..25, fn _ -> :array.new(n + 1, default: 0) end)

    Enum.reduce(Enum.with_index(chars), base, fn {code, i}, acc ->
      c = code - ?a

      Enum.map(Enum.with_index(acc), fn {arr, ch} ->
        prev = :array.get(i, arr)
        new = prev + if ch == c, do: 1, else: 0
        :array.set(i + 1, new, arr)
      end)
    end)
  end

  # Build mismatch prefix array for left half and total mismatches
  defp build_mismatch_prefix(chars, half) do
    n = length(chars)

    mismatches =
      for i <- 0..(half - 1) do
        if Enum.at(chars, i) != Enum.at(chars, n - 1 - i), do: 1, else: 0
      end

    pref = :array.new(half + 1, default: 0)

    {pref_final, _} =
      Enum.reduce(Enum.with_index(mismatches), {pref, 0}, fn {val, idx},
                                                          {arr, _} ->
        prev = :array.get(idx, arr)
        new_arr = :array.set(idx + 1, prev + val, arr)
        {new_arr, idx + 1}
      end)

    total = Enum.sum(mismatches)
    {pref_final, total}
  end

  # Range sum using prefix array (inclusive)
  defp range_sum(pref, l, r) when l <= r do
    :array.get(r + 1, pref) - :array.get(l, pref)
  end

  defp range_sum(_pref, _l, _r), do: 0

  # Get counts of each character in interval [l,r]
  defp get_counts(pref_arrays, l, r) when l <= r do
    Enum.map(Enum.with_index(pref_arrays), fn {arr, ch} ->
      :array.get(r + 1, arr) - :array.get(l, arr)
    end)
  end

  defp get_counts(_pref_arrays, _l, _r), do: List.duplicate(0, 26)

  # Adjust left-only intervals: subtract needed chars from L counts
  defp adjust_left_only(l_counts, pref_arrays, a, b, ir_l, ir_r, n) do
    intervals = []

    intervals =
      if a <= ir_l - 1 do
        [{a, min(b, ir_l - 1)} | intervals]
      else
        intervals
      end

    intervals =
      if b >= ir_r + 1 do
        [{max(a, ir_r + 1), b} | intervals]
      else
        intervals
      end

    Enum.reduce_while(intervals, {l_counts, true}, fn {l, r},
                                                    {counts, _ok} ->
      # counterpart interval on right side
      j_l = n - 1 - r
      j_r = n - 1 - l

      need = get_counts(pref_arrays, j_l, j_r)

      new_counts =
        Enum.zip_with([counts, need], fn cnt, nd -> cnt - nd end)

      if Enum.any?(new_counts, &(&1 < 0)) do
        {:halt, {new_counts, false}}
      else
        {:cont, {new_counts, true}}
      end
    end)
  end

  # Adjust right-only intervals: subtract needed chars from R counts
  defp adjust_right_only(r_counts, pref_arrays, a, b, ir_l, ir_r, _n) do
    intervals = []

    intervals =
      if ir_l <= a - 1 do
        [{ir_l, min(ir_r, a - 1)} | intervals]
      else
        intervals
      end

    intervals =
      if ir_r >= b + 1 do
        [{max(ir_l, b + 1), ir_r} | intervals]
      else
        intervals
      end

    Enum.reduce_while(intervals, {r_counts, true}, fn {l, r},
                                                    {counts, _ok} ->
      need = get_counts(pref_arrays, l, r)

      new_counts =
        Enum.zip_with([counts, need], fn cnt, nd -> cnt - nd end)

      if Enum.any?(new_counts, &(&1 < 0)) do
        {:halt, {new_counts, false}}
      else
        {:cont, {new_counts, true}}
      end
    end)
  end
end
```
