# 3003. Maximize the Number of Partitions After Operations

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxPartitionsAfterOperations(string s, int k) {
        int n = s.size();
        // prefix counts for each letter
        vector<array<int,26>> pref(n+1);
        pref[0].fill(0);
        for (int i=0;i<n;++i){
            pref[i+1]=pref[i];
            ++pref[i+1][s[i]-'a'];
        }
        // original greedy partitions: part_start per index and prefPartitions
        vector<int> partStart(n);
        vector<int> prefPart(n);
        vector<pair<int,int>> parts;
        int pos=0, totalOrig=0;
        while(pos<n){
            int st=pos;
            array<int,26> cnt{};
            cnt.fill(0);
            int distinct=0;
            while(pos<n){
                int ch=s[pos]-'a';
                if(cnt[ch]==0 && distinct==k) break;
                if(cnt[ch]==0) ++distinct;
                ++cnt[ch];
                ++pos;
            }
            ++totalOrig;
            for(int i=st;i<pos;++i){
                partStart[i]=st;
                prefPart[i]=totalOrig;
            }
            parts.emplace_back(st,pos-1);
        }
        // compute e[i]: farthest right index from i with <=k distinct (no changes)
        vector<int> e(n);
        array<int,26> winCnt{};
        winCnt.fill(0);
        int distinct=0, r=-1;
        for(int l=0;l<n;++l){
            while(r+1<n){
                int nxt = s[r+1]-'a';
                if(winCnt[nxt]==0 && distinct==k) break;
                ++r;
                if(winCnt[nxt]==0) ++distinct;
                ++winCnt[nxt];
            }
            e[l]=r;
            // move left pointer
            int ch=s[l]-'a';
            --winCnt[ch];
            if(winCnt[ch]==0) --distinct;
        }
        // suff[i]: partitions count for substring s[i..n-1] (fresh start)
        vector<int> suff(n+1,0);
        for(int i=n-1;i>=0;--i){
            suff[i]=1 + suff[e[i]+1];
        }

        auto distinctAfterChange = [&](int L,int R,int idx,int newIdx)->int{
            int oldIdx = s[idx]-'a';
            int cntDistinct=0;
            for(int c=0;c<26;++c){
                int cnt = pref[R+1][c] - pref[L][c];
                if(c==oldIdx && idx>=L && idx<=R) --cnt;
                if(c==newIdx && idx>=L && idx<=R) ++cnt;
                if(cnt>0) ++cntDistinct;
            }
            return cntDistinct;
        };

        auto ok = [&](int L,int R,int idx,int newIdx)->bool{
            return distinctAfterChange(L,R,idx,newIdx) <= k;
        };

        auto maxRight = [&](int start,int idx,int newIdx)->int{
            int lo=start-1, hi=n-1;
            while(lo<hi){
                int mid=(lo+hi+1)/2;
                if(ok(start,mid,idx,newIdx)) lo=mid;
                else hi=mid-1;
            }
            return lo;
        };

        int answer = totalOrig; // no change case
        for(int i=0;i<n;++i){
            int L = partStart[i];
            int prefBefore = (L==0?0:prefPart[L-1]);
            for(int nc=0;nc<26;++nc){
                if(nc == s[i]-'a') continue;
                int r1 = maxRight(L,i,nc);
                if(r1>=i){
                    int total = 1 + prefBefore + (r1+1<n ? suff[r1+1] : 0);
                    answer = max(answer,total);
                }else{
                    int start2 = r1+1;
                    int r2 = maxRight(start2,i,nc);
                    int total = 2 + prefBefore + (r2+1<n ? suff[r2+1] : 0);
                    answer = max(answer,total);
                }
            }
        }
        return answer;
    }
};
```

## Java

```java
class Solution {
    public int maxPartitionsAfterOperations(String s, int k) {
        int n = s.length();
        // prefix counts
        int[][] pre = new int[n + 1][26];
        for (int i = 0; i < n; i++) {
            System.arraycopy(pre[i], 0, pre[i + 1], 0, 26);
            pre[i + 1][s.charAt(i) - 'a']++;
        }

        // compute next cut positions using two pointers
        int[] next = new int[n];
        int[] freq = new int[26];
        int distinct = 0;
        int r = 0;
        for (int l = 0; l < n; l++) {
            while (r < n) {
                int c = s.charAt(r) - 'a';
                if (freq[c] == 0 && distinct == k) break;
                if (freq[c] == 0) distinct++;
                freq[c]++;
                r++;
            }
            next[l] = r; // exclusive
            int cl = s.charAt(l) - 'a';
            freq[cl]--;
            if (freq[cl] == 0) distinct--;
        }

        // suffix partitions count using DP on next[]
        int[] suff = new int[n + 1];
        suff[n] = 0;
        for (int i = n - 1; i >= 0; i--) {
            suff[i] = 1 + suff[next[i]];
        }

        // pref array and partition start
        int[] pref = new int[n];
        int[] partStart = new int[n];
        int cnt = 0;
        int idx = 0;
        while (idx < n) {
            int end = next[idx] - 1; // inclusive
            for (int j = idx; j <= end; j++) {
                pref[j] = cnt + 1;
                partStart[j] = idx;
            }
            cnt++;
            idx = next[idx];
        }

        int answer = suff[0]; // no change case

        // helper lambda for distinct count after replacement
        java.util.function.IntBinaryOperator distinctAfter = (l, rPos) -> {
            return 0; // placeholder not used
        };

        for (int i = 0; i < n; i++) {
            int L = partStart[i];
            int prefBefore = (L == 0) ? 0 : pref[L - 1];
            int oldIdx = s.charAt(i) - 'a';
            for (int newIdx = 0; newIdx < 26; newIdx++) {
                if (newIdx == oldIdx) continue;

                // binary search rightmost r such that distinct in [L, r] <= k after replacement
                int lo = L, hi = n - 1, best = L - 1;
                while (lo <= hi) {
                    int mid = (lo + hi) >>> 1;
                    if (distinctInRange(pre, L, mid, i, oldIdx, newIdx) <= k) {
                        best = mid;
                        lo = mid + 1;
                    } else {
                        hi = mid - 1;
                    }
                }
                int rPos = best;
                if (rPos >= i) {
                    int total = 1 + prefBefore + suff[rPos + 1];
                    if (total > answer) answer = total;
                } else {
                    // need second partition starting at i
                    lo = i; hi = n - 1; best = i - 1;
                    while (lo <= hi) {
                        int mid = (lo + hi) >>> 1;
                        if (distinctInRange(pre, i, mid, i, oldIdx, newIdx) <= k) {
                            best = mid;
                            lo = mid + 1;
                        } else {
                            hi = mid - 1;
                        }
                    }
                    int r2 = best;
                    int total = 2 + prefBefore + suff[r2 + 1];
                    if (total > answer) answer = total;
                }
            }
        }

        return answer;
    }

    private int distinctInRange(int[][] pre, int l, int r, int pos, int oldIdx, int newIdx) {
        int distinct = 0;
        for (int c = 0; c < 26; c++) {
            int cnt = pre[r + 1][c] - pre[l][c];
            if (c == oldIdx) cnt--;
            if (c == newIdx) cnt++;
            if (cnt > 0) distinct++;
        }
        return distinct;
    }
}
```

## Python

```python
class Solution(object):
    def maxPartitionsAfterOperations(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        s_int = [ord(c) - 97 for c in s]

        # prefix counts for each letter
        pref_cnt = [[0] * (n + 1) for _ in range(26)]
        for i, ch in enumerate(s_int):
            for c in range(26):
                pref_cnt[c][i + 1] = pref_cnt[c][i]
            pref_cnt[ch][i + 1] += 1

        # maxR[l]: exclusive right bound of longest prefix starting at l with <=k distinct chars
        maxR = [0] * n
        cnt = [0] * 26
        distinct = 0
        r = 0
        for l in range(n):
            while r < n:
                ch = s_int[r]
                if cnt[ch] == 0 and distinct + 1 > k:
                    break
                if cnt[ch] == 0:
                    distinct += 1
                cnt[ch] += 1
                r += 1
            maxR[l] = r
            # move left pointer
            ch_left = s_int[l]
            cnt[ch_left] -= 1
            if cnt[ch_left] == 0:
                distinct -= 1

        # partition_start, pref (partitions up to each index)
        partition_start = [0] * n
        pref = [0] * n
        part_cnt = 0
        pos = 0
        while pos < n:
            start = pos
            end = maxR[start]
            part_cnt += 1
            for idx in range(start, end):
                partition_start[idx] = start
                pref[idx] = part_cnt
            pos = end

        # suff[i]: number of partitions from i to end (i is start index)
        suff = [0] * (n + 1)   # suff[n]=0
        for i in range(n - 1, -1, -1):
            suff[i] = 1 + suff[maxR[i]]

        def distinct_original(l, r):
            cntd = 0
            for c in range(26):
                if pref_cnt[c][r + 1] - pref_cnt[c][l] > 0:
                    cntd += 1
            return cntd

        def distinct_modified(l, r, idx, new_ord):
            # original distinct count
            d = distinct_original(l, r)
            if not (l <= idx <= r):
                return d
            old_ord = s_int[idx]
            if old_ord == new_ord:
                return d
            # removal of old character if it was unique in interval
            if pref_cnt[old_ord][r + 1] - pref_cnt[old_ord][l] == 1:
                d -= 1
            # addition of new character if absent in interval
            if pref_cnt[new_ord][r + 1] - pref_cnt[new_ord][l] == 0:
                d += 1
            return d

        best = pref[-1]  # no change case

        for i in range(n):
            L = partition_start[i]
            left_partitions = pref[L - 1] if L > 0 else 0
            old_ord = s_int[i]
            for new_ord in range(26):
                if new_ord == old_ord:
                    continue
                # first segment binary search
                lo, hi = L, n - 1
                r_best = L - 1
                while lo <= hi:
                    mid = (lo + hi) // 2
                    d = distinct_modified(L, mid, i, new_ord)
                    if d <= k:
                        r_best = mid
                        lo = mid + 1
                    else:
                        hi = mid - 1
                r = r_best
                if r >= i:
                    total = left_partitions + 1 + suff[r + 1]
                else:
                    # second segment starts at r+1 (contains i)
                    start2 = r + 1
                    lo, hi = start2, n - 1
                    r2_best = start2 - 1
                    while lo <= hi:
                        mid = (lo + hi) // 2
                        d = distinct_modified(start2, mid, i, new_ord)
                        if d <= k:
                            r2_best = mid
                            lo = mid + 1
                        else:
                            hi = mid - 1
                    total = left_partitions + 2 + suff[r2_best + 1]
                if total > best:
                    best = total

        return best
```

## Python3

```python
class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        # prefix counts for each letter
        pref_cnt = [[0] * (n + 1) for _ in range(26)]
        for i, ch in enumerate(s):
            idx = ord(ch) - 97
            for c in range(26):
                pref_cnt[c][i + 1] = pref_cnt[c][i]
            pref_cnt[idx][i + 1] += 1

        # helper to count distinct letters in [l, r] (inclusive)
        def distinct(l: int, r: int, change_idx: int = -1, new_idx: int = -1) -> int:
            cnt = 0
            for c in range(26):
                occ = pref_cnt[c][r + 1] - pref_cnt[c][l]
                if change_idx != -1 and l <= change_idx <= r:
                    old_c = ord(s[change_idx]) - 97
                    if c == old_c:
                        occ -= 1
                    if c == new_idx:
                        occ += 1
                if occ > 0:
                    cnt += 1
                    if cnt > k:
                        break
            return cnt

        # check without any change
        def ok_no_change(l: int, r: int) -> bool:
            return distinct(l, r) <= k

        # binary search max right index for given left (no change)
        def max_right_no_change(l: int) -> int:
            lo, hi = l - 1, n - 1
            while lo + 1 < hi:
                mid = (lo + hi) // 2
                if ok_no_change(l, mid):
                    lo = mid
                else:
                    hi = mid
            if ok_no_change(l, hi):
                return hi
            return lo

        # build partitions for original string
        starts = []
        ends = {}
        part_start_of_idx = [0] * n
        start = 0
        while start < n:
            end_excl = max_right_no_change(start) + 1
            starts.append(start)
            ends[start] = end_excl
            for i in range(start, end_excl):
                part_start_of_idx[i] = start
            start = end_excl

        # prefix partitions count up to each position (exclusive)
        pref = [0] * (n + 1)
        cnt = 0
        for st in starts:
            cnt += 1
            en = ends[st]
            for p in range(st + 1, en + 1):
                pref[p] = cnt

        # suffix partitions count from each start position
        suff = [0] * (n + 1)
        for st in reversed(starts):
            en = ends[st]
            suff[st] = 1 + suff[en]

        ans = pref[n]  # no change case

        # binary search helper with a possible change
        def max_right_with_change(l: int, change_idx: int, new_idx: int) -> int:
            lo, hi = l - 1, n - 1
            while lo + 1 < hi:
                mid = (lo + hi) // 2
                if distinct(l, mid, change_idx, new_idx) <= k:
                    lo = mid
                else:
                    hi = mid
            if distinct(l, hi, change_idx, new_idx) <= k:
                return hi
            return lo

        # try changing each position to every other letter
        for i in range(n):
            L = part_start_of_idx[i]
            pre_cnt = pref[L]  # partitions before this start
            old_idx = ord(s[i]) - 97
            for new_c in range(26):
                if new_c == old_idx:
                    continue
                r = max_right_with_change(L, i, new_c)
                if r >= i:
                    total = 1 + pre_cnt + suff[r + 1]
                else:
                    # first partition ends before i, need a second one starting at i
                    r2 = max_right_with_change(i, i, new_c)
                    total = 2 + pre_cnt + suff[r2 + 1]
                if total > ans:
                    ans = total

        return ans
```

## C

```c
#include <string.h>
#include <stdbool.h>

int maxPartitionsAfterOperations(char* s, int k) {
    int n = strlen(s);
    const int MAXN = 10005;
    static int freq[26][MAXN];
    for (int c = 0; c < 26; ++c) freq[c][0] = 0;
    for (int i = 0; i < n; ++i) {
        int ch = s[i] - 'a';
        for (int c = 0; c < 26; ++c) {
            freq[c][i + 1] = freq[c][i] + (c == ch);
        }
    }

    // nxt[i]: exclusive end of maximal segment starting at i with <=k distinct chars
    static int nxt[MAXN];
    int cnt[26] = {0};
    int distinct = 0;
    int r = 0;
    for (int l = 0; l < n; ++l) {
        while (r < n) {
            int ch = s[r] - 'a';
            if (cnt[ch] == 0 && distinct + 1 > k) break;
            if (cnt[ch] == 0) distinct++;
            cnt[ch]++;
            r++;
        }
        nxt[l] = r; // exclusive
        int chL = s[l] - 'a';
        cnt[chL]--;
        if (cnt[chL] == 0) distinct--;
    }

    // pref[i]: number of partitions covering s[0..i-1]
    static int pref[MAXN];
    static int partStart[MAXN];
    pref[0] = 0;
    int pos = 0;
    while (pos < n) {
        int end = nxt[pos];
        for (int i = pos; i < end; ++i) {
            partStart[i] = pos;
            pref[i + 1] = pref[pos] + 1;
        }
        pos = end;
    }

    // suff[i]: number of partitions from i to end
    static int suff[MAXN];
    suff[n] = 0;
    for (int i = n - 1; i >= 0; --i) {
        suff[i] = 1 + suff[nxt[i]];
    }

    int answer = pref[n]; // no change

    // helper to check distinct count after replacement in [l, r] inclusive
    auto ok = [&](int l, int r, int idx, char newc)->bool{
        int orig = s[idx] - 'a';
        int nc = newc - 'a';
        int d = 0;
        for (int c = 0; c < 26; ++c) {
            int cntc = freq[c][r + 1] - freq[c][l];
            if (idx >= l && idx <= r) {
                if (c == orig) cntc--;
                else if (c == nc) cntc++;
            }
            if (cntc > 0) {
                d++;
                if (d > k) return false;
            }
        }
        return true;
    };

    for (int i = 0; i < n; ++i) {
        int L = partStart[i];
        char origChar = s[i];
        for (char ch = 'a'; ch <= 'z'; ++ch) {
            if (ch == origChar) continue;
            // binary search maximal r >= i such that [L, r] is valid
            int low = i, high = n - 1, best = i - 1;
            while (low <= high) {
                int mid = (low + high) >> 1;
                if (ok(L, mid, i, ch)) {
                    best = mid;
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
            if (best >= i) {
                // first partition ends at best
                int total = 1 + pref[L] + suff[best + 1];
                if (total > answer) answer = total;
            } else {
                // first partition ends before i, need second partition
                int r1 = best; // could be L-1 when best < L
                int start2 = r1 + 1;
                low = i;
                high = n - 1;
                int best2 = i - 1;
                while (low <= high) {
                    int mid = (low + high) >> 1;
                    if (ok(start2, mid, i, ch)) {
                        best2 = mid;
                        low = mid + 1;
                    } else {
                        high = mid - 1;
                    }
                }
                int total = 2 + pref[L] + suff[best2 + 1];
                if (total > answer) answer = total;
            }
        }
    }

    return answer;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MaxPartitionsAfterOperations(string s, int k) {
        int n = s.Length;
        // Prefix counts for each character
        int[,] prefCnt = new int[26, n + 1];
        for (int i = 0; i < n; i++) {
            int ch = s[i] - 'a';
            for (int c = 0; c < 26; c++) {
                prefCnt[c, i + 1] = prefCnt[c, i];
            }
            prefCnt[ch, i + 1]++;
        }

        // Greedy partitions on original string
        int[] partStart = new int[n];
        int[] partEnd = new int[n];
        List<int> starts = new List<int>();
        int idx = 0;
        while (idx < n) {
            int[] cntTmp = new int[26];
            int distinct = 0;
            int j = idx;
            while (j < n) {
                int c = s[j] - 'a';
                if (cntTmp[c] == 0 && distinct == k) break;
                if (cntTmp[c] == 0) distinct++;
                cntTmp[c]++;
                j++;
            }
            for (int p = idx; p < j; p++) {
                partStart[p] = idx;
                partEnd[p] = j - 1;
            }
            starts.Add(idx);
            idx = j;
        }

        // pref[i]: partitions covering s[0..i]
        int[] pref = new int[n];
        int partsSoFar = 0;
        foreach (int st in starts) {
            int ed = partEnd[st];
            for (int p = st; p <= ed; p++) pref[p] = partsSoFar + 1;
            partsSoFar++;
        }

        // suff[i]: partitions from i to end, suff[n]=0
        int[] suff = new int[n + 1];
        suff[n] = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (i == partStart[i]) {
                int ed = partEnd[i];
                suff[i] = 1 + suff[ed + 1];
            } else {
                suff[i] = suff[i + 1];
            }
        }

        int bestAns = pref[n - 1]; // without any change

        // Helper to compute distinct count after a single character change
        bool DistinctWithinK(int l, int r, int pos, int oldc, int newc) {
            int distinct = 0;
            for (int c = 0; c < 26; c++) {
                int cnt = prefCnt[c, r + 1] - prefCnt[c, l];
                if (c == oldc && l <= pos && pos <= r) cnt--;
                if (c == newc && l <= pos && pos <= r) cnt++;
                if (cnt > 0) {
                    distinct++;
                    if (distinct > k) return false;
                }
            }
            return true;
        }

        for (int i = 0; i < n; i++) {
            int oldc = s[i] - 'a';
            int L = partStart[i];
            for (int newc = 0; newc < 26; newc++) {
                if (newc == oldc) continue;

                // Find maximal r >= L such that [L, r] satisfies condition
                int low = L, high = n - 1, bestR = L - 1;
                while (low <= high) {
                    int mid = (low + high) >> 1;
                    if (DistinctWithinK(L, mid, i, oldc, newc)) {
                        bestR = mid;
                        low = mid + 1;
                    } else {
                        high = mid - 1;
                    }
                }
                int r = bestR;
                int leftPartitions = (L > 0) ? pref[L - 1] : 0;

                if (r >= i) {
                    int total = 1 + leftPartitions + suff[r + 1];
                    if (total > bestAns) bestAns = total;
                } else {
                    // Need a second partition starting at r+1
                    int start2 = r + 1;
                    low = start2; high = n - 1; bestR = start2 - 1;
                    while (low <= high) {
                        int mid = (low + high) >> 1;
                        if (DistinctWithinK(start2, mid, i, oldc, newc)) {
                            bestR = mid;
                            low = mid + 1;
                        } else {
                            high = mid - 1;
                        }
                    }
                    int r2 = bestR;
                    int total = 2 + leftPartitions + suff[r2 + 1];
                    if (total > bestAns) bestAns = total;
                }
            }
        }

        return bestAns;
    }
}
```

## Javascript

```javascript
/ **
 * @param {string} s
 * @param {number} k
 * @return {number}
 * /
var maxPartitionsAfterOperations = function(s, k) {
    const n = s.length;
    const aCode = 97;

    // prefix counts for each letter
    const pref = Array.from({length:26}, () => new Uint16Array(n+1));
    for (let i = 0; i < n; ++i) {
        const ch = s.charCodeAt(i) - aCode;
        for (let c = 0; c < 26; ++c) pref[c][i + 1] = pref[c][i];
        pref[ch][i + 1]++;
    }

    // nextEnd[i]: exclusive right bound of longest prefix starting at i with <=k distinct letters
    const nextEnd = new Uint16Array(n);
    const freq = new Uint16Array(26);
    let distinct = 0, r = 0;
    for (let l = 0; l < n; ++l) {
        while (r < n) {
            const idx = s.charCodeAt(r) - aCode;
            if (freq[idx] === 0 && distinct + 1 > k) break;
            if (freq[idx] === 0) distinct++;
            freq[idx]++;
            r++;
        }
        nextEnd[l] = r; // exclusive
        const leftIdx = s.charCodeAt(l) - aCode;
        freq[leftIdx]--;
        if (freq[leftIdx] === 0) distinct--;
    }

    // partStart[i]: start index of the partition containing i in original greedy
    const partStart = new Uint16Array(n);
    const leftCntBefore = new Uint16Array(n); // partitions before this start
    let order = 0;
    for (let i = 0; i < n;) {
        const st = i;
        const en = nextEnd[i];
        for (let j = st; j < en; ++j) partStart[j] = st;
        leftCntBefore[st] = order;
        i = en;
        order++;
    }
    const totalPartitions = order;

    // suff[i]: number of partitions from i to end using original string
    const suff = new Uint16Array(n + 1);
    suff[n] = 0;
    for (let i = n - 1; i >= 0; --i) {
        suff[i] = 1 + suff[nextEnd[i]];
    }

    // helper: distinct count in [l, r] after changing position pos from oldIdx to newIdx
    function distinctCount(l, r, pos, oldIdx, newIdx) {
        let cnt = 0;
        const needAdjust = (pos >= l && pos <= r);
        for (let c = 0; c < 26; ++c) {
            let occ = pref[c][r + 1] - pref[c][l];
            if (needAdjust) {
                if (c === oldIdx) occ--;
                if (c === newIdx) occ++;
            }
            if (occ > 0) {
                cnt++;
                if (cnt > k) return k + 1; // early exit
            }
        }
        return cnt;
    }

    // binary search maximal r >= start such that distinctCount <= k
    function maxRight(start, pos, oldIdx, newIdx) {
        let low = start, high = n - 1, ans = start - 1;
        while (low <= high) {
            const mid = (low + high) >> 1;
            if (distinctCount(start, mid, pos, oldIdx, newIdx) <= k) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return ans; // will be >= start
    }

    let best = totalPartitions; // case of no change

    for (let i = 0; i < n; ++i) {
        const oldIdx = s.charCodeAt(i) - aCode;
        const origStart = partStart[i];
        const leftCnt = leftCntBefore[origStart];

        for (let newIdx = 0; newIdx < 26; ++newIdx) {
            if (newIdx === oldIdx) continue;

            // first partition after change starting at origStart
            const r1 = maxRight(origStart, i, oldIdx, newIdx);
            if (r1 >= i) {
                const total = leftCnt + 1 + suff[r1 + 1];
                if (total > best) best = total;
            } else {
                // need a second partition starting at i
                const r2 = maxRight(i, i, oldIdx, newIdx);
                const total = leftCnt + 2 + suff[r2 + 1];
                if (total > best) best = total;
            }
        }
    }

    return best;
};
```

## Typescript

```typescript
function maxPartitionsAfterOperations(s: string, k: number): number {
    const n = s.length;
    const aCode = 'a'.charCodeAt(0);
    // prefix counts
    const pref: number[][] = Array.from({ length: n + 1 }, () => new Array(26).fill(0));
    for (let i = 0; i < n; ++i) {
        const idx = s.charCodeAt(i) - aCode;
        for (let c = 0; c < 26; ++c) pref[i + 1][c] = pref[i][c];
        pref[i + 1][idx]++;
    }

    // original greedy partitions
    const partStartIdx = new Array(n);
    const starts: number[] = [];
    const ends: number[] = [];

    let i = 0;
    while (i < n) {
        const freq = new Array(26).fill(0);
        let distinct = 0;
        let j = i;
        for (; j < n; ++j) {
            const idx = s.charCodeAt(j) - aCode;
            if (freq[idx] === 0) distinct++;
            freq[idx]++;
            if (distinct > k) break;
        }
        const end = j - 1;
        starts.push(i);
        ends.push(end);
        for (let p = i; p <= end; ++p) partStartIdx[p] = i;
        i = j;
    }

    const totalParts = starts.length;
    // map start index -> its order (number of partitions before it)
    const orderOfStart: Map<number, number> = new Map();
    for (let idx = 0; idx < starts.length; ++idx) {
        orderOfStart.set(starts[idx], idx);
    }

    // suffix count from any position
    const suffixCnt = new Array(n + 1).fill(0); // suffixCnt[pos] = partitions for s[pos..]
    for (let pos = 0; pos < n; ++pos) {
        const st = partStartIdx[pos];
        const before = orderOfStart.get(st)!;
        suffixCnt[pos] = totalParts - before;
    }
    suffixCnt[n] = 0;

    // helper to compute distinct count in [l,r] after replacing s[i] with newChar
    function distinctAfterReplace(l: number, r: number, iPos: number, newIdx: number): number {
        const oldIdx = s.charCodeAt(iPos) - aCode;
        let cnt = 0;
        for (let c = 0; c < 26; ++c) {
            let cur = pref[r + 1][c] - pref[l][c];
            if (c === oldIdx) {
                if (cur > 0) cur--; // remove old char at iPos
            }
            if (c === newIdx) {
                cur++; // add new char
            }
            if (cur > 0) cnt++;
        }
        return cnt;
    }

    let answer = totalParts; // case of no change

    for (let pos = 0; pos < n; ++pos) {
        const start = partStartIdx[pos];
        const beforePartitions = orderOfStart.get(start)!;

        const oldIdx = s.charCodeAt(pos) - aCode;
        for (let newIdx = 0; newIdx < 26; ++newIdx) {
            if (newIdx === oldIdx) continue;

            // binary search max r where distinct(start, r) <= k after replacement
            let lo = start, hi = n - 1, best = start - 1;
            while (lo <= hi) {
                const mid = (lo + hi) >> 1;
                if (distinctAfterReplace(start, mid, pos, newIdx) <= k) {
                    best = mid;
                    lo = mid + 1;
                } else {
                    hi = mid - 1;
                }
            }

            if (best >= pos) {
                const after = best + 1 <= n ? suffixCnt[best + 1] : 0;
                answer = Math.max(answer, 1 + beforePartitions + after);
            } else {
                // need an extra partition before position
                let lo2 = pos, hi2 = n - 1, best2 = pos - 1;
                while (lo2 <= hi2) {
                    const mid = (lo2 + hi2) >> 1;
                    if (distinctAfterReplace(pos, mid, pos, newIdx) <= k) {
                        best2 = mid;
                        lo2 = mid + 1;
                    } else {
                        hi2 = mid - 1;
                    }
                }
                const after2 = best2 + 1 <= n ? suffixCnt[best2 + 1] : 0;
                answer = Math.max(answer, 2 + beforePartitions + after2);
            }
        }
    }

    return answer;
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function maxPartitionsAfterOperations($s, $k) {
        $n = strlen($s);
        // prefix counts for each character
        $prefCnt = array_fill(0, 26, array_fill(0, $n + 1, 0));
        for ($i = 0; $i < $n; $i++) {
            $chIdx = ord($s[$i]) - 97;
            for ($c = 0; $c < 26; $c++) {
                $prefCnt[$c][$i + 1] = $prefCnt[$c][$i];
            }
            $prefCnt[$chIdx][$i + 1]++;
        }

        // greedy partitions on original string
        $partStart = array_fill(0, $n, 0);
        $prefPart = array_fill(0, $n, 0);
        $partitionCount = 0;
        $l = 0;
        while ($l < $n) {
            $freq = array_fill(0, 26, 0);
            $distinct = 0;
            $r = $l;
            while ($r < $n) {
                $cIdx = ord($s[$r]) - 97;
                if ($freq[$cIdx] == 0 && $distinct == $k) break;
                $freq[$cIdx]++;
                if ($freq[$cIdx] == 1) $distinct++;
                $r++;
            }
            $partitionCount++;
            for ($i = $l; $i < $r; $i++) {
                $partStart[$i] = $l;
                $prefPart[$i] = $partitionCount;
            }
            $l = $r;
        }

        // greedy partitions on reversed string to obtain suffix info
        $rev = strrev($s);
        $prefRev = array_fill(0, $n, 0);
        $partitionCount = 0;
        $l = 0;
        while ($l < $n) {
            $freq = array_fill(0, 26, 0);
            $distinct = 0;
            $r = $l;
            while ($r < $n) {
                $cIdx = ord($rev[$r]) - 97;
                if ($freq[$cIdx] == 0 && $distinct == $k) break;
                $freq[$cIdx]++;
                if ($freq[$cIdx] == 1) $distinct++;
                $r++;
            }
            $partitionCount++;
            for ($i = $l; $i < $r; $i++) {
                $prefRev[$i] = $partitionCount;
            }
            $l = $r;
        }

        // suffix partitions array
        $suff = array_fill(0, $n + 1, 0); // suff[n]=0
        for ($i = 0; $i < $n; $i++) {
            $suff[$i] = $prefRev[$n - 1 - $i];
        }

        $ans = $prefPart[$n - 1]; // no change case

        // helper to compute distinct count after a change in range [l, r]
        $distinctAfterChange = function($l, $r, $oldIdx, $newIdx) use ($prefCnt) {
            $origDistinct = 0;
            for ($c = 0; $c < 26; $c++) {
                if ($prefCnt[$c][$r + 1] - $prefCnt[$c][$l] > 0) $origDistinct++;
            }
            $cntOld = $prefCnt[$oldIdx][$r + 1] - $prefCnt[$oldIdx][$l];
            $cntNew = $prefCnt[$newIdx][$r + 1] - $prefCnt[$newIdx][$l];
            $distinct = $origDistinct;
            if ($cntOld == 1) $distinct--;
            if ($cntNew == 0) $distinct++;
            return $distinct;
        };

        // binary search for maximal r where condition holds
        $findMaxR = function($start, $pos, $oldIdx, $newIdx) use ($n, $k, $prefCnt, $distinctAfterChange) {
            $low = $start;
            $high = $n - 1;
            $best = $start - 1; // no valid range yet
            while ($low <= $high) {
                $mid = intdiv($low + $high, 2);
                $d = $distinctAfterChange($start, $mid, $oldIdx, $newIdx);
                if ($d <= $k) {
                    $best = $mid;
                    $low = $mid + 1;
                } else {
                    $high = $mid - 1;
                }
            }
            return $best;
        };

        for ($i = 0; $i < $n; $i++) {
            $origStart = $partStart[$i];
            $oldIdx = ord($s[$i]) - 97;
            for ($newIdx = 0; $newIdx < 26; $newIdx++) {
                if ($newIdx == $oldIdx) continue;

                // first try to extend from origStart
                $r = $findMaxR($origStart, $i, $oldIdx, $newIdx);
                if ($r >= $i) {
                    $left = ($origStart > 0) ? $prefPart[$origStart - 1] : 0;
                    $right = ($r + 1 < $n) ? $suff[$r + 1] : 0;
                    $cand = 1 + $left + $right;
                } else {
                    // partition ends before i, need second partition starting at i
                    $r2 = $findMaxR($i, $i, $oldIdx, $newIdx);
                    $left = ($origStart > 0) ? $prefPart[$origStart - 1] : 0;
                    $right = ($r2 + 1 < $n) ? $suff[$r2 + 1] : 0;
                    $cand = 2 + $left + $right;
                }
                if ($cand > $ans) $ans = $cand;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxPartitionsAfterOperations(_ s: String, _ k: Int) -> Int {
        let n = s.count
        if n == 0 { return 0 }
        // convert to int array 0..25
        var chars = [Int]()
        chars.reserveCapacity(n)
        for ch in s.utf8 {
            chars.append(Int(ch - 97))
        }
        // prefix counts for each character
        var prefCnt = Array(repeating: Array(repeating: 0, count: n + 1), count: 26)
        for i in 0..<n {
            let c = chars[i]
            for ch in 0..<26 {
                prefCnt[ch][i + 1] = prefCnt[ch][i] + (ch == c ? 1 : 0)
            }
        }
        // compute partition start for each index and prefix partitions count
        var partStart = Array(repeating: 0, count: n)
        var prefPartitions = Array(repeating: 0, count: n)
        var freq = Array(repeating: 0, count: 26)
        var distinct = 0
        var start = 0
        var partitions = 0
        for i in 0..<n {
            let c = chars[i]
            if freq[c] == 0 { distinct += 1 }
            freq[c] += 1
            if distinct > k {
                partitions += 1
                for idx in start..<i {
                    prefPartitions[idx] = partitions
                    partStart[idx] = start
                }
                // reset
                freq = Array(repeating: 0, count: 26)
                distinct = 0
                start = i
                freq[c] = 1
                distinct = 1
            }
        }
        partitions += 1
        for idx in start..<n {
            prefPartitions[idx] = partitions
            partStart[idx] = start
        }
        // farthest right index with <=k distinct for each left using sliding window
        var farthestR = Array(repeating: 0, count: n)
        var freq2 = Array(repeating: 0, count: 26)
        var distinct2 = 0
        var right = 0
        for left in 0..<n {
            while right < n && (distinct2 + (freq2[chars[right]] == 0 ? 1 : 0)) <= k {
                if freq2[chars[right]] == 0 { distinct2 += 1 }
                freq2[chars[right]] += 1
                right += 1
            }
            farthestR[left] = right - 1
            // move left forward
            let cl = chars[left]
            freq2[cl] -= 1
            if freq2[cl] == 0 { distinct2 -= 1 }
        }
        // suffix partitions from each index using DP
        var suff = Array(repeating: 0, count: n + 1) // suff[n]=0
        for i in stride(from: n - 1, through: 0, by: -1) {
            let r = farthestR[i]
            suff[i] = 1 + suff[r + 1]
        }
        var answer = prefPartitions[n - 1] // no change case
        
        // helper to count distinct in [l,r]
        @inline(__always) func distinctCount(_ l: Int, _ r: Int) -> Int {
            var cnt = 0
            for ch in 0..<26 {
                if prefCnt[ch][r + 1] - prefCnt[ch][l] > 0 { cnt += 1 }
            }
            return cnt
        }
        
        // iterate each position and possible replacement
        for i in 0..<n {
            let orig = chars[i]
            let L = partStart[i]
            let prefBefore = (L > 0) ? prefPartitions[L - 1] : 0
            for newChar in 0..<26 where newChar != orig {
                // binary search max r >= i such that after change [L, r] has <=k distinct
                var low = i
                var high = n - 1
                var bestR = i - 1
                while low <= high {
                    let mid = (low + high) >> 1
                    var d = distinctCount(L, mid)
                    let cntOrig = prefCnt[orig][mid + 1] - prefCnt[orig][L]
                    let cntNew = prefCnt[newChar][mid + 1] - prefCnt[newChar][L]
                    if cntOrig == 1 { d -= 1 }
                    if cntNew == 0 { d += 1 }
                    if d <= k {
                        bestR = mid
                        low = mid + 1
                    } else {
                        high = mid - 1
                    }
                }
                if bestR >= i {
                    let total = 1 + prefBefore + suff[bestR + 1]
                    if total > answer { answer = total }
                } else {
                    // first partition ends before i, need second partition starting at i
                    var low2 = i
                    var high2 = n - 1
                    var bestR2 = i - 1
                    while low2 <= high2 {
                        let mid = (low2 + high2) >> 1
                        var d2 = distinctCount(i, mid)
                        let cntOrig2 = prefCnt[orig][mid + 1] - prefCnt[orig][i]
                        let cntNew2 = prefCnt[newChar][mid + 1] - prefCnt[newChar][i]
                        if cntOrig2 == 1 { d2 -= 1 }
                        if cntNew2 == 0 { d2 += 1 }
                        if d2 <= k {
                            bestR2 = mid
                            low2 = mid + 1
                        } else {
                            high2 = mid - 1
                        }
                    }
                    let total = 2 + prefBefore + suff[bestR2 + 1]
                    if total > answer { answer = total }
                }
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxPartitionsAfterOperations(s: String, k: Int): Int {
        val n = s.length
        val chars = s.toCharArray()
        // prefix counts for each letter
        val pref = Array(26) { IntArray(n + 1) }
        for (i in 0 until n) {
            val idx = chars[i] - 'a'
            for (c in 0 until 26) {
                pref[c][i + 1] = pref[c][i]
            }
            pref[idx][i + 1]++
        }

        // compute maxRight for each start using sliding window
        val maxRight = IntArray(n)
        var right = -1
        val freq = IntArray(26)
        var distinct = 0
        for (left in 0 until n) {
            if (left > 0) {
                val remIdx = chars[left - 1] - 'a'
                freq[remIdx]--
                if (freq[remIdx] == 0) distinct--
            }
            while (right + 1 < n) {
                val nxtIdx = chars[right + 1] - 'a'
                val addDistinct = if (freq[nxtIdx] == 0) 1 else 0
                if (distinct + addDistinct > k) break
                right++
                freq[nxtIdx]++
                if (addDistinct == 1) distinct++
            }
            maxRight[left] = right
        }

        // next index after each partition and dpFrom suffix partitions count
        val nextIdxArr = IntArray(n)
        for (i in 0 until n) {
            nextIdxArr[i] = maxRight[i] + 1
        }
        val dpFrom = IntArray(n + 1)
        dpFrom[n] = 0
        for (i in n - 1 downTo 0) {
            dpFrom[i] = 1 + dpFrom[nextIdxArr[i]]
        }
        val total = dpFrom[0]

        // partStart: start index of partition containing each position
        val partStart = IntArray(n)
        var st = 0
        while (st < n) {
            val ed = maxRight[st]
            for (i in st..ed) partStart[i] = st
            st = ed + 1
        }

        var answer = total // case of no change

        fun distinctAfter(l: Int, r: Int, pos: Int, oldIdx: Int, newIdx: Int): Int {
            var cnt = 0
            for (c in 0 until 26) {
                if (pref[c][r + 1] - pref[c][l] > 0) cnt++
            }
            if (oldIdx == newIdx) return cnt
            if (pos < l || pos > r) return cnt
            val oldInRange = pref[oldIdx][r + 1] - pref[oldIdx][l]
            if (oldInRange == 1) cnt--          // becomes zero after removal
            val newInRange = pref[newIdx][r + 1] - pref[newIdx][l]
            if (newInRange == 0) cnt++           // becomes non‑zero after addition
            return cnt
        }

        for (pos in 0 until n) {
            val oldIdx = chars[pos] - 'a'
            for (newIdx in 0 until 26) {
                if (newIdx == oldIdx) continue
                val startPart = partStart[pos]

                // first binary search: farthest r from startPart
                var lo = startPart - 1
                var hi = n - 1
                while (lo < hi) {
                    val mid = (lo + hi + 1) ushr 1
                    if (distinctAfter(startPart, mid, pos, oldIdx, newIdx) <= k) {
                        lo = mid
                    } else {
                        hi = mid - 1
                    }
                }
                val r = lo
                val prefBefore = total - dpFrom[startPart]
                var cur: Int
                if (r >= pos) {
                    cur = prefBefore + 1 + dpFrom[r + 1]
                } else {
                    // need a second partition starting at r+1
                    val start2 = r + 1
                    var lo2 = start2 - 1
                    var hi2 = n - 1
                    while (lo2 < hi2) {
                        val mid = (lo2 + hi2 + 1) ushr 1
                        if (distinctAfter(start2, mid, pos, oldIdx, newIdx) <= k) {
                            lo2 = mid
                        } else {
                            hi2 = mid - 1
                        }
                    }
                    val r2 = lo2
                    cur = prefBefore + 2 + dpFrom[r2 + 1]
                }
                if (cur > answer) answer = cur
            }
        }

        return answer
    }
}
```

## Dart

```dart
class Solution {
  int maxPartitionsAfterOperations(String s, int k) {
    int n = s.length;
    // Prefix counts for each character
    List<List<int>> prefCnt =
        List.generate(26, (_) => List.filled(n + 1, 0));
    for (int i = 0; i < n; ++i) {
      int ch = s.codeUnitAt(i) - 97;
      for (int c = 0; c < 26; ++c) {
        prefCnt[c][i + 1] = prefCnt[c][i];
      }
      prefCnt[ch][i + 1]++;
    }

    // Helper to count distinct chars in [l, r] after changing position pos to newCh
    int distinctCount(int l, int r, int pos, int newCh) {
      int cnt = 0;
      for (int c = 0; c < 26; ++c) {
        int occ = prefCnt[c][r + 1] - prefCnt[c][l];
        if (pos >= l && pos <= r) {
          int oldCh = s.codeUnitAt(pos) - 97;
          if (c == oldCh) occ--;
          if (c == newCh) occ++;
        }
        if (occ > 0) cnt++;
      }
      return cnt;
    }

    // Compute pref partitions and partition start indices for original string
    List<int> pref = List.filled(n, 0);
    List<int> partStart = List.filled(n, 0);
    int partitions = 0;
    int idx = 0;
    while (idx < n) {
      int start = idx;
      List<int> freq = List.filled(26, 0);
      int distinct = 0;
      while (idx < n) {
        int ch = s.codeUnitAt(idx) - 97;
        if (freq[ch] == 0 && distinct + 1 > k) break;
        if (freq[ch] == 0) distinct++;
        freq[ch]++;
        idx++;
      }
      for (int j = start; j < idx; ++j) {
        pref[j] = partitions + 1;
        partStart[j] = start;
      }
      partitions++;
    }

    // Compute suffix partitions using reversed string
    String rev = s.split('').reversed.join();
    List<int> prefRev = List.filled(n, 0);
    int idxR = 0;
    int partsR = 0;
    while (idxR < n) {
      int start = idxR;
      List<int> freq = List.filled(26, 0);
      int distinct = 0;
      while (idxR < n) {
        int ch = rev.codeUnitAt(idxR) - 97;
        if (freq[ch] == 0 && distinct + 1 > k) break;
        if (freq[ch] == 0) distinct++;
        freq[ch]++;
        idxR++;
      }
      for (int j = start; j < idxR; ++j) {
        prefRev[j] = partsR + 1;
      }
      partsR++;
    }
    List<int> suff = List.filled(n, 0);
    for (int i = 0; i < n; ++i) {
      suff[i] = prefRev[n - 1 - i];
    }

    int answer = pref[n - 1]; // no change case

    for (int pos = 0; pos < n; ++pos) {
      int L = partStart[pos];
      int preCnt = (L > 0) ? pref[L - 1] : 0;
      int oldCh = s.codeUnitAt(pos) - 97;

      for (int newCh = 0; newCh < 26; ++newCh) {
        if (newCh == oldCh) continue;

        // Find farthest r >= L with distinct <= k after change
        int low = L, high = n - 1, bestR = L - 1;
        while (low <= high) {
          int mid = (low + high) >> 1;
          if (distinctCount(L, mid, pos, newCh) <= k) {
            bestR = mid;
            low = mid + 1;
          } else {
            high = mid - 1;
          }
        }

        int total;
        if (bestR >= pos) {
          int suffix = (bestR + 1 < n) ? suff[bestR + 1] : 0;
          total = 1 + preCnt + suffix;
        } else {
          // Need a second partition
          int start2 = bestR + 1;
          low = start2;
          high = n - 1;
          int bestR2 = start2 - 1;
          while (low <= high) {
            int mid = (low + high) >> 1;
            if (distinctCount(start2, mid, pos, newCh) <= k) {
              bestR2 = mid;
              low = mid + 1;
            } else {
              high = mid - 1;
            }
          }
          int suffix = (bestR2 + 1 < n) ? suff[bestR2 + 1] : 0;
          total = 2 + preCnt + suffix;
        }

        if (total > answer) answer = total;
      }
    }

    return answer;
  }
}
```

## Golang

```go
func maxPartitionsAfterOperations(s string, k int) int {
    n := len(s)
    // prefix counts for each character
    prefCnt := make([][]int, 26)
    for c := 0; c < 26; c++ {
        prefCnt[c] = make([]int, n+1)
    }
    for i := 0; i < n; i++ {
        idx := int(s[i] - 'a')
        for c := 0; c < 26; c++ {
            prefCnt[c][i+1] = prefCnt[c][i]
        }
        prefCnt[idx][i+1]++
    }

    // greedy partitioning of original string
    type seg struct{ l, r int }
    segments := []seg{}
    freq := [26]int{}
    distinct := 0
    segStart := 0
    for i := 0; i < n; i++ {
        idx := int(s[i] - 'a')
        if freq[idx] == 0 {
            distinct++
        }
        freq[idx]++
        if distinct > k {
            segments = append(segments, seg{segStart, i - 1})
            for j := 0; j < 26; j++ {
                freq[j] = 0
            }
            distinct = 0
            segStart = i
            freq[idx] = 1
            distinct = 1
        }
    }
    segments = append(segments, seg{segStart, n - 1})

    // partStart for each position and prefBefore (partitions before index)
    partStart := make([]int, n)
    prefBefore := make([]int, n+1) // partitions before i
    cnt := 0
    curPos := 0
    for _, sg := range segments {
        for ; curPos < sg.l; curPos++ {
            prefBefore[curPos] = cnt
        }
        for j := sg.l; j <= sg.r; j++ {
            partStart[j] = sg.l
        }
        cnt++
        curPos = sg.r + 1
    }
    for ; curPos <= n; curPos++ {
        prefBefore[curPos] = cnt
    }

    // suffixCount[i]: partitions from i to end (including segment containing i)
    suffixCount := make([]int, n+1) // suffixCount[n]=0
    cnt = 0
    cur := n
    for idx := len(segments) - 1; idx >= 0; idx-- {
        sg := segments[idx]
        for i := sg.r + 1; i < cur; i++ {
            suffixCount[i] = cnt
        }
        cnt++
        for i := sg.l; i <= sg.r; i++ {
            suffixCount[i] = cnt
        }
        cur = sg.l
    }
    for i := 0; i < cur; i++ {
        suffixCount[i] = cnt
    }

    // helper to count distinct chars in [L,R] after changing position i from origIdx to newIdx
    distinctCount := func(L, R, i, origIdx, newIdx int) int {
        d := 0
        for c := 0; c < 26; c++ {
            cntc := prefCnt[c][R+1] - prefCnt[c][L]
            if L <= i && i <= R {
                if c == origIdx {
                    cntc--
                }
                if c == newIdx {
                    cntc++
                }
            }
            if cntc > 0 {
                d++
            }
        }
        return d
    }

    // binary search maximal right index starting from L satisfying distinct <= k
    maxRight := func(L, i, origIdx, newIdx int) int {
        low := L - 1
        high := n - 1
        for low < high {
            mid := (low + high + 1) >> 1
            if distinctCount(L, mid, i, origIdx, newIdx) <= k {
                low = mid
            } else {
                high = mid - 1
            }
        }
        return low
    }

    ans := len(segments) // no change case

    for i := 0; i < n; i++ {
        origIdx := int(s[i] - 'a')
        L := partStart[i]
        for newIdx := 0; newIdx < 26; newIdx++ {
            if newIdx == origIdx {
                continue
            }
            r := maxRight(L, i, origIdx, newIdx)
            if r >= i {
                total := 1 + prefBefore[L] + suffixCount[r+1]
                if total > ans {
                    ans = total
                }
            } else {
                start2 := r + 1
                r2 := maxRight(start2, i, origIdx, newIdx)
                total := 2 + prefBefore[L] + suffixCount[r2+1]
                if total > ans {
                    ans = total
                }
            }
        }
    }

    return ans
}
```

## Ruby

```ruby
def max_partitions_after_operations(s, k)
  n = s.length
  a = s.bytes.map { |b| b - 97 } # 0..25

  # prefix counts for each character
  pref_cnt = Array.new(26) { Array.new(n + 1, 0) }
  (0...n).each do |i|
    ch = a[i]
    26.times do |c|
      pref_cnt[c][i + 1] = pref_cnt[c][i] + (c == ch ? 1 : 0)
    end
  end

  # distinct count in [l, r] with optional modification at position pos
  distinct = lambda do |l, r, pos = nil, orig_idx = nil, new_idx = nil|
    cnt = 0
    26.times do |c|
      occ = pref_cnt[c][r + 1] - pref_cnt[c][l]
      if pos && l <= pos && pos <= r
        if c == orig_idx
          occ -= 1
        elsif c == new_idx
          occ += 1
        end
      end
      cnt += 1 if occ > 0
      return k + 1 if cnt > k
    end
    cnt
  end

  # max right endpoint for each left using original string
  max_r = Array.new(n, 0)
  (0...n).each do |l|
    low = l
    high = n - 1
    ans = l - 1
    while low <= high
      mid = (low + high) / 2
      if distinct.call(l, mid) <= k
        ans = mid
        low = mid + 1
      else
        high = mid - 1
      end
    end
    max_r[l] = ans
  end

  # pref partitions count up to each index and start of partition for each position
  pref_part = Array.new(n, 0)
  start_arr = Array.new(n, 0)
  i = 0
  part_cnt = 0
  while i < n
    l = i
    r = max_r[l]
    part_cnt += 1
    (l..r).each do |idx|
      pref_part[idx] = part_cnt
      start_arr[idx] = l
    end
    i = r + 1
  end

  # suff partitions count from each index using DP
  suff_part = Array.new(n + 1, 0) # suff_part[n] = 0
  (n - 1).downto(0) do |idx|
    r = max_r[idx]
    suff_part[idx] = 1 + suff_part[r + 1]
  end

  best = pref_part[n - 1] # no change case

  (0...n).each do |pos|
    orig_idx = a[pos]
    l0 = start_arr[pos]
    pref_before = l0 > 0 ? pref_part[l0 - 1] : 0

    26.times do |new_idx|
      next if new_idx == orig_idx

      # first partition after change starting at l0
      low = l0
      high = n - 1
      ans = l0 - 1
      while low <= high
        mid = (low + high) / 2
        if distinct.call(l0, mid, pos, orig_idx, new_idx) <= k
          ans = mid
          low = mid + 1
        else
          high = mid - 1
        end
      end
      r_prime = ans

      if r_prime >= pos
        total = 1 + pref_before + suff_part[r_prime + 1]
        best = total if total > best
      else
        # need a second partition starting at pos
        low2 = pos
        high2 = n - 1
        ans2 = pos - 1
        while low2 <= high2
          mid = (low2 + high2) / 2
          if distinct.call(pos, mid, pos, orig_idx, new_idx) <= k
            ans2 = mid
            low2 = mid + 1
          else
            high2 = mid - 1
          end
        end
        r2 = ans2
        total = 2 + pref_before + suff_part[r2 + 1]
        best = total if total > best
      end
    end
  end

  best
end
```

## Scala

```scala
object Solution {
  def maxPartitionsAfterOperations(s: String, k: Int): Int = {
    val n = s.length
    // prefix counts for each character
    val prefCnt = Array.ofDim[Int](26, n + 1)
    for (i <- 0 until n) {
      val chIdx = s.charAt(i) - 'a'
      var c = 0
      while (c < 26) {
        prefCnt(c)(i + 1) = prefCnt(c)(i)
        c += 1
      }
      prefCnt(chIdx)(i + 1) += 1
    }

    // maxEnd[left] = exclusive right index of longest segment starting at left with <=k distinct chars (original string)
    val maxEnd = new Array[Int](n)
    var right = 0
    val cnt = new Array[Int](26)
    var distinct = 0
    for (left <- 0 until n) {
      while (right < n) {
        val idx = s.charAt(right) - 'a'
        if (cnt(idx) == 0 && distinct + 1 > k) {
          // would exceed, break
          ()
        } else {
          if (cnt(idx) == 0) distinct += 1
          cnt(idx) += 1
          right += 1
          // continue loop
          // note: we need to re-evaluate condition after adding; handled by while condition next iteration
          // break only when would exceed, which we already prevented
        }
        if (right <= n && (cnt(s.charAt(right - 1) - 'a') == 0 || distinct > k)) {
          // not needed
        }
        if (right < n && cnt(s.charAt(right) - 'a') == 0 && distinct + 1 > k) {
          // stop expanding
          ()
        }
        if (right < n && !(cnt(s.charAt(right) - 'a') == 0 && distinct + 1 > k)) {
          // continue loop
        } else {
          // break condition met
          // but while will check again; we just let it exit naturally
        }
      }
      maxEnd(left) = right
      val lIdx = s.charAt(left) - 'a'
      cnt(lIdx) -= 1
      if (cnt(lIdx) == 0) distinct -= 1
    }

    // prefPartitions and partStart for each index
    val prefParts = new Array[Int](n)
    val partStartArr = new Array[Int](n)
    var start = 0
    var partNum = 0
    while (start < n) {
      val endExclusive = maxEnd(start)
      val end = endExclusive - 1
      partNum += 1
      var idx = start
      while (idx <= end) {
        prefParts(idx) = partNum
        partStartArr(idx) = start
        idx += 1
      }
      start = end + 1
    }

    // suffix partitions count from each position
    val suffFrom = new Array[Int](n + 1)
    suffFrom(n) = 0
    var i = n - 1
    while (i >= 0) {
      val endExclusive = maxEnd(i)
      suffFrom(i) = 1 + suffFrom(endExclusive)
      i -= 1
    }

    // helper to compute distinct count in [l, r] after replacement at pos with newCharIdx
    def distinctAfterReplace(l: Int, r: Int, pos: Int, origIdx: Int, newIdx: Int): Int = {
      var d = 0
      var c = 0
      while (c < 26) {
        val cntInRange = prefCnt(c)(r + 1) - prefCnt(c)(l)
        if (cntInRange > 0) d += 1
        c += 1
      }
      val origCount = prefCnt(origIdx)(r + 1) - prefCnt(origIdx)(l)
      var dAdj = d
      if (origCount == 1) dAdj -= 1
      val newCount = prefCnt(newIdx)(r + 1) - prefCnt(newIdx)(l)
      if (newCount == 0) dAdj += 1
      dAdj
    }

    var answer = prefParts(n - 1) // no change case

    for (pos <- 0 until n) {
      val L = partStartArr(pos)
      val prefBefore = if (L > 0) prefParts(L - 1) else 0
      val origIdx = s.charAt(pos) - 'a'
      var newIdx = 0
      while (newIdx < 26) {
        if (newIdx != origIdx) {
          // binary search for r in [L, n-1] maximal where condition holds
          var lo = L - 1
          var hi = n - 1
          while (lo < hi) {
            val mid = (lo + hi + 1) >>> 1
            if (distinctAfterReplace(L, mid, pos, origIdx, newIdx) <= k) lo = mid
            else hi = mid - 1
          }
          val r = lo
          if (r >= pos) {
            val after = 1 + prefBefore + suffFrom(r + 1)
            if (after > answer) answer = after
          } else {
            // need second partition starting at pos
            var lo2 = pos - 1
            var hi2 = n - 1
            while (lo2 < hi2) {
              val mid = (lo2 + hi2 + 1) >>> 1
              if (distinctAfterReplace(pos, mid, pos, origIdx, newIdx) <= k) lo2 = mid
              else hi2 = mid - 1
            }
            val r2 = lo2
            val after = 2 + prefBefore + suffFrom(r2 + 1)
            if (after > answer) answer = after
          }
        }
        newIdx += 1
      }
    }

    answer
  }
}
```

## Rust

```rust
use std::cmp::max;

impl Solution {
    pub fn max_partitions_after_operations(s: String, k: i32) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        if n == 0 {
            return 0;
        }
        // prefix counts for each character
        let mut pref_cnt = vec![vec![0usize; n + 1]; 26];
        for i in 0..n {
            let ch = (bytes[i] - b'a') as usize;
            for c in 0..26 {
                pref_cnt[c][i + 1] = pref_cnt[c][i];
            }
            pref_cnt[ch][i + 1] += 1;
        }

        // max_right[l]: farthest r such that [l, r] has at most k distinct chars
        let mut max_right = vec![0usize; n];
        let mut cnt = [0usize; 26];
        let mut distinct = 0usize;
        let mut r: isize = -1;
        for l in 0..n {
            while (r + 1) < n as isize {
                let nxt = (r + 1) as usize;
                let ch = (bytes[nxt] - b'a') as usize;
                let new_distinct = if cnt[ch] == 0 { distinct + 1 } else { distinct };
                if new_distinct <= k as usize {
                    r += 1;
                    cnt[ch] += 1;
                    distinct = new_distinct;
                } else {
                    break;
                }
            }
            max_right[l] = r as usize; // r >= l always because k>=1
            let ch_l = (bytes[l] - b'a') as usize;
            cnt[ch_l] -= 1;
            if cnt[ch_l] == 0 {
                distinct -= 1;
            }
        }

        // pref partitions and partition start for each index
        let mut pref_part = vec![0i32; n];
        let mut part_start_of_idx = vec![0usize; n];
        let mut start = 0usize;
        let mut cnt_parts = 0i32;
        while start < n {
            let end = max_right[start];
            cnt_parts += 1;
            for idx in start..=end {
                pref_part[idx] = cnt_parts;
                part_start_of_idx[idx] = start;
            }
            start = end + 1;
        }

        // suffix partitions using DP: suff[i] = number of partitions from i to end
        let mut suff = vec![0i32; n + 1];
        for i in (0..n).rev() {
            let end = max_right[i];
            let next = if end + 1 < n { suff[end + 1] } else { 0 };
            suff[i] = 1 + next;
        }
        // answer without any change
        let mut answer = pref_part[n - 1];

        // helper closure to compute distinct count with a replacement
        let distinct_le_k = |l: usize,
                             r: usize,
                             pos: usize,
                             orig_c: usize,
                             new_c: usize,
                             pref_cnt: &Vec<Vec<usize>>,
                             k: i32|
         -> bool {
            let mut distinct_now = 0usize;
            for c in 0..26 {
                let mut cnt = pref_cnt[c][r + 1] - pref_cnt[c][l];
                if pos >= l && pos <= r {
                    if c == orig_c {
                        if cnt > 0 {
                            cnt -= 1;
                        }
                    }
                    if c == new_c {
                        cnt += 1;
                    }
                }
                if cnt > 0 {
                    distinct_now += 1;
                    if distinct_now > k as usize {
                        return false;
                    }
                }
            }
            true
        };

        for i in 0..n {
            let orig_c = (bytes[i] - b'a') as usize;
            let left_start = part_start_of_idx[i];
            let left_pref = if left_start == 0 { 0 } else { pref_part[left_start - 1] };
            for new_c in 0..26 {
                if new_c == orig_c {
                    continue;
                }
                // binary search for farthest r >= left_start
                let mut lo: isize = left_start as isize - 1; // may be -1
                let mut hi: isize = n as isize - 1;
                while lo < hi {
                    let mid = ((lo + hi + 1) / 2) as usize;
                    if distinct_le_k(
                        left_start,
                        mid,
                        i,
                        orig_c,
                        new_c,
                        &pref_cnt,
                        k,
                    ) {
                        lo = (mid as isize);
                    } else {
                        hi = (mid as isize) - 1;
                    }
                }
                let r = lo as usize; // maximal index satisfying condition
                if r >= i {
                    let total = 1 + left_pref + suff[r + 1];
                    answer = max(answer, total);
                } else {
                    // need second partition starting at i
                    let mut lo2: isize = i as isize - 1;
                    let mut hi2: isize = n as isize - 1;
                    while lo2 < hi2 {
                        let mid = ((lo2 + hi2 + 1) / 2) as usize;
                        if distinct_le_k(
                            i,
                            mid,
                            i,
                            orig_c,
                            new_c,
                            &pref_cnt,
                            k,
                        ) {
                            lo2 = (mid as isize);
                        } else {
                            hi2 = (mid as isize) - 1;
                        }
                    }
                    let r2 = lo2 as usize;
                    let total = 2 + left_pref + suff[r2 + 1];
                    answer = max(answer, total);
                }
            }
        }

        answer
    }
}
```

## Racket

```racket
(define (max-partitions-after-operations s k)
  (define n (string-length s))
  ;; prefix counts
  (define pref-counts (make-vector (+ n 1)))
  (vector-set! pref-counts 0 (make-vector 26 0))
  (for ([i (in-range n)])
    (define prev (vector-ref pref-counts i))
    (define cur (make-vector 26))
    (for ([j (in-range 26)]) (vector-set! cur j (vector-ref prev j)))
    (define idx (- (char->integer (string-ref s i)) (char->integer #\a)))
    (vector-set! cur idx (+ 1 (vector-ref cur idx)))
    (vector-set! pref-counts (+ i 1) cur))
  ;; compute partition start and prefix-partition counts
  (define part-start (make-vector n -1))
  (define pref-parts (make-vector (+ n 1) 0))
  (let loop ((i 0) (cnt 0))
    (when (< i n)
      (define freq (make-vector 26 0))
      (define distinct 0)
      (define j i)
      (let inner ()
        (when (< j n)
          (define idx (- (char->integer (string-ref s j)) (char->integer #\a)))
          (when (= (vector-ref freq idx) 0) (set! distinct (+ distinct 1)))
          (vector-set! freq idx (+ 1 (vector-ref freq idx)))
          (if (> distinct k)
              (void)
              (begin
                (set! j (+ j 1))
                (inner))))))
      ;; set start for indices in this partition
      (for ([p (in-range i j)]) (vector-set! part-start p i))
      (define newcnt (+ cnt 1))
      (vector-set! pref-parts j newcnt)
      (loop j newcnt)))
  ;; compute suffix partitions via reversed string
  (define rev-s (list->string (reverse (string->list s))))
  (define (compute-pref-parts str)
    (define len (string-length str))
    (define freq (make-vector 26 0))
    (define distinct 0)
    (define cnt 0)
    (define pref (make-vector (+ len 1) 0))
    (let loop ((i 0) (cnt cnt))
      (when (< i len)
        (define local-freq (make-vector 26 0))
        (define local-distinct 0)
        (define j i)
        (let inner ()
          (when (< j len)
            (define idx (- (char->integer (string-ref str j)) (char->integer #\a)))
            (when (= (vector-ref local-freq idx) 0) (set! local-distinct (+ local-distinct 1)))
            (vector-set! local-freq idx (+ 1 (vector-ref local-freq idx)))
            (if (> local-distinct k)
                (void)
                (begin
                  (set! j (+ j 1))
                  (inner))))))
        (set! cnt (+ cnt 1))
        (vector-set! pref j cnt)
        (loop j cnt)))
    pref)
  (define pref-rev-parts (compute-pref-parts rev-s))
  (define suff (make-vector (+ n 1) 0))
  (for ([i (in-range (+ n 1))])
    (vector-set! suff i (vector-ref pref-rev-parts (- n i))))
  ;; answer start with no change
  (define ans (vector-ref pref-parts n))
  ;; helper to compute distinct after replacement in range [l,r]
  (define (distinct-after l r old-idx new-idx)
    (define orig-dist 0)
    (for ([c (in-range 26)])
      (when (> (- (vector-ref (vector-ref pref-counts (+ r 1)) c)
                 (vector-ref (vector-ref pref-counts l) c))
               0)
        (set! orig-dist (+ orig-dist 1))))
    (define cnt-old (- (vector-ref (vector-ref pref-counts (+ r 1)) old-idx)
                       (vector-ref (vector-ref pref-counts l) old-idx)))
    (define cnt-new (- (vector-ref (vector-ref pref-counts (+ r 1)) new-idx)
                       (vector-ref (vector-ref pref-counts l) new-idx)))
    (when (not (= old-idx new-idx))
      (when (= cnt-old 1) (set! orig-dist (- orig-dist 1)))
      (when (= cnt-new 0) (set! orig-dist (+ orig-dist 1))))
    orig-dist)
  ;; iterate each position and possible replacement
  (for ([i (in-range n)])
    (define ps (vector-ref part-start i))
    (define pre-parts (vector-ref pref-parts ps))
    (define old-idx (- (char->integer (string-ref s i)) (char->integer #\a)))
    (for ([new-idx (in-range 26)] #:when (not (= new-idx old-idx)))
      ;; binary search for farthest r >= ps with distinct <= k
      (define best (- ps 1))
      (let loop ((l ps) (h (- n 1)) (b best))
        (if (> l h)
            (set! best b)
            (let* ((mid (quotient (+ l h) 2))
                   (new-dist (distinct-after ps mid old-idx new-idx)))
              (if (<= new-dist k)
                  (loop (+ mid 1) h mid)
                  (loop l (- mid 1) b)))))
      (define r best)
      (cond
        [(>= r i)
         (define total (+ 1 pre-parts (vector-ref suff (+ r 1))))
         (when (> total ans) (set! ans total))]
        [else
         ;; need second partition starting at i
         (define best2 (- i 1))
         (let loop2 ((l i) (h (- n 1)) (b best2))
           (if (> l h)
               (set! best2 b)
               (let* ((mid (quotient (+ l h) 2))
                      (new-dist (distinct-after i mid old-idx new-idx)))
                 (if (<= new-dist k)
                     (loop2 (+ mid 1) h mid)
                     (loop2 l (- mid 1) b)))))
         (define r2 best2)
         (define total (+ 2 pre-parts (vector-ref suff (+ r2 1))))
         (when (> total ans) (set! ans total)))])))
  ans)
```

## Erlang

```erlang
-spec max_partitions_after_operations(S :: unicode:unicode_binary(), K :: integer()) -> integer().
max_partitions_after_operations(S, K) ->
    CharList = binary:bin_to_list(S),
    N = length(CharList),
    % convert chars to 0..25
    Chars = [C - $a || C <- CharList],
    CharArr = array:from_list(Chars),

    %% build prefix counts for each character (26 arrays of size N+1)
    Prefs0 = lists:foldl(fun(_, Acc) -> [array:new(N + 1, {default, 0}) | Acc] end,
                         [], lists:seq(1, 26)),
    Prefs = lists:reverse(Prefs0),
    Prefs1 = build_prefix_counts(Chars, N, Prefs),

    %% sliding window to compute maxR for each start
    MaxRList = compute_max_r(Chars, N, K),
    MaxRArr = array:from_list(MaxRList),

    %% dp suffix (number of partitions starting at i)
    DP = compute_dp(N, MaxRArr),

    %% partition start for each index and index of partition start
    {PartStartArr, PartIdxStartArr} = build_partition_info(N, MaxRArr),

    %% answer without any change
    Answer0 = array:get(0, DP),

    %% main enumeration over positions and possible new characters
    Answer = enumerate_changes(N, K, CharArr, Prefs1,
                               MaxRArr, DP,
                               PartStartArr, PartIdxStartArr,
                               Answer0),
    Answer.

%% Build prefix counts: Prefs is list of 26 arrays (each size N+1)
build_prefix_counts(_Chars, _N, []) -> [];
build_prefix_counts(Chars, N, [Arr|Rest]) ->
    CharIdx = length(Rest), % because we are building in reverse order
    UpdatedArr = build_single_prefix(Chars, N, CharIdx, Arr),
    [UpdatedArr | build_prefix_counts(Chars, N, Rest)].

build_single_prefix([], _N, _Cidx, Arr) -> Arr;
build_single_prefix([Ch|Rest], N, Cidx, Arr) ->
    Prev = array:get(N - length(Rest) - 1, Arr),
    NewVal = if Ch =:= Cidx -> Prev + 1; true -> Prev end,
    Arr2 = array:set(N - length(Rest), NewVal, Arr),
    build_single_prefix(Rest, N, Cidx, Arr2).

%% Sliding window to compute maximal right index for each left where distinct <= K
compute_max_r(Chars, N, K) ->
    Freq0 = lists:duplicate(26, 0),
    compute_max_r_loop(0, -1, 0, Freq0, Chars, N, K, []).

compute_max_r_loop(L, R, Distinct, _Freq, _Chars, N, _K, Acc) when L >= N ->
    lists:reverse(Acc);
compute_max_r_loop(L, R, Distinct, Freq, Chars, N, K, Acc) ->
    {R2, Dist2, Freq2} = expand_right(R, Distinct, Freq, Chars, N, K),
    MaxR = R2,
    % remove left char
    CharL = lists:nth(L + 1, Chars),
    CountL = lists:nth(CharL + 1, Freq2) - 1,
    NewFreq = set_nth(Freq2, CharL, CountL),
    NewDistinct = if CountL =:= 0 -> Dist2 - 1; true -> Dist2 end,
    compute_max_r_loop(L + 1, R2, NewDistinct, NewFreq, Chars, N, K, [MaxR | Acc]).

expand_right(R, Distinct, Freq, Chars, N, K) ->
    case R + 1 < N of
        true ->
            Char = lists:nth(R + 2, Chars),
            Count = lists:nth(Char + 1, Freq),
            NewDistinct = if Count =:= 0 -> Distinct + 1; true -> Distinct end,
            if NewDistinct =< K ->
                    NewFreq = set_nth(Freq, Char, Count + 1),
                    expand_right(R + 1, NewDistinct, NewFreq, Chars, N, K);
               true ->
                    {R, Distinct, Freq}
            end;
        false -> {R, Distinct, Freq}
    end.

set_nth(List, Index, Value) ->
    Prefix = lists:sublist(List, Index),
    Suffix = lists:nthtail(Index + 1, List),
    Prefix ++ [Value] ++ Suffix.

%% Compute DP suffix array
compute_dp(N, MaxRArr) ->
    DP0 = array:new(N + 1, {default, 0}),
    compute_dp_loop(N - 1, DP0, MaxRArr).

compute_dp_loop(-1, DP, _MaxRArr) -> DP;
compute_dp_loop(I, DP, MaxRArr) ->
    MaxR = array:get(I, MaxRArr),
    Next = MaxR + 1,
    Val = 1 + array:get(Next, DP),
    DP2 = array:set(I, Val, DP),
    compute_dp_loop(I - 1, DP2, MaxRArr).

%% Build partition start for each index and partition index start
build_partition_info(N, MaxRArr) ->
    PartStart0 = array:new(N, {default, 0}),
    PartIdxStart0 = array:new(N, {default, 0}),
    build_part_loop(0, 0, PartStart0, PartIdxStart0, MaxRArr).

build_part_loop(Cur, Idx, PS, PI, _MaxRArr) when Cur >= array:size(PS) ->
    {PS, PI};
build_part_loop(Cur, Idx, PS, PI, MaxRArr) ->
    MaxR = array:get(Cur, MaxRArr),
    % set start index for all positions in this partition
    PS2 = fill_range(PS, Cur, MaxR, Cur),
    PI2 = array:set(Cur, Idx, PI),
    build_part_loop(MaxR + 1, Idx + 1, PS2, PI2, MaxRArr).

fill_range(Arr, L, R, Val) when L > R -> Arr;
fill_range(Arr, L, R, Val) ->
    Arr2 = array:set(L, Val, Arr),
    fill_range(Arr2, L + 1, R, Val).

%% Enumerate all possible changes and compute best answer
enumerate_changes(N, K, CharArr, Prefs,
                  MaxRArr, DP,
                  PartStartArr, PartIdxStartArr,
                  Best) ->
    enumerate_i(0, N, K, CharArr, Prefs,
                MaxRArr, DP,
                PartStartArr, PartIdxStartArr,
                Best).

enumerate_i(I, N, _K, _CharArr, _Prefs,
            _MaxRArr, _DP,
            _PartStartArr, _PartIdxStartArr,
            Best) when I >= N ->
    Best;
enumerate_i(I, N, K, CharArr, Prefs,
            MaxRArr, DP,
            PartStartArr, PartIdxStartArr,
            Best) ->
    Orig = array:get(I, CharArr),
    L = array:get(I, PartStartArr),
    PrefBefore = array:get(L, PartIdxStartArr),
    Best1 = enumerate_newc(0, 25, I, Orig, L, PrefBefore,
                           K, CharArr, Prefs,
                           MaxRArr, DP,
                           PartStartArr, PartIdxStartArr,
                           Best),
    enumerate_i(I + 1, N, K, CharArr, Prefs,
                MaxRArr, DP,
                PartStartArr, PartIdxStartArr,
                Best1).

enumerate_newc(C, _MaxC, _I, _Orig, _L, _PrefBefore,
               _K, _CharArr, _Prefs,
               _MaxRArr, _DP,
               _PartStartArr, _PartIdxStartArr,
               Best) when C > _MaxC ->
    Best;
enumerate_newc(C, MaxC, I, Orig, L, PrefBefore,
               K, CharArr, Prefs,
               MaxRArr, DP,
               PartStartArr, PartIdxStartArr,
               Best) ->
    if C =:= Orig -> enumerate_newc(C + 1, MaxC, I, Orig, L, PrefBefore,
                                    K, CharArr, Prefs,
                                    MaxRArr, DP,
                                    PartStartArr, PartIdxStartArr,
                                    Best);
       true ->
            % binary search for maximal r >= I
            R = max_r_binary(I, N - 1, I, L, Orig, C, K, Prefs),
            Total =
                if R >= I ->
                        1 + PrefBefore + array:get(R + 1, DP);
                   true ->
                        % need second partition start at I
                        R2 = max_r_binary(I, N - 1, I, I, Orig, C, K, Prefs),
                        2 + PrefBefore + array:get(R2 + 1, DP)
                end,
            NewBest = if Total > Best -> Total; true -> Best end,
            enumerate_newc(C + 1, MaxC, I, Orig, L, PrefBefore,
                           K, CharArr, Prefs,
                           MaxRArr, DP,
                           PartStartArr, PartIdxStartArr,
                           NewBest)
    end.

max_r_binary(Low, High, I, Start, Orig, NewC, K, Prefs) ->
    max_r_binary_loop(Low, High, -1, I, Start, Orig, NewC, K, Prefs).

max_r_binary_loop(Low, High, Best, I, Start, Orig, NewC, K, Prefs) when Low > High ->
    Best;
max_r_binary_loop(Low, High, Best, I, Start, Orig, NewC, K, Prefs) ->
    Mid = (Low + High) div 2,
    Distinct = distinct_in_range(Start, Mid, I, Orig, NewC, Prefs),
    if Distinct =< K ->
            max_r_binary_loop(Mid + 1, High, Mid, I, Start, Orig, NewC, K, Prefs);
       true ->
            max_r_binary_loop(Low, Mid - 1, Best, I, Start, Orig, NewC, K, Prefs)
    end.

distinct_in_range(L, R, I, Orig, NewC, Prefs) ->
    distinct_in_range_loop(0, 26, L, R, I, Orig, NewC, Prefs, 0).

distinct_in_range_loop(C, MaxC, _L, _R, _I, _Orig, _NewC, _Prefs, Acc) when C >= MaxC ->
    Acc;
distinct_in_range_loop(C, MaxC, L, R, I, Orig, NewC, Prefs, Acc) ->
    Arr = lists:nth(C + 1, Prefs),
    CountR = array:get(R + 1, Arr),
    CountL = array:get(L, Arr),
    Cnt = CountR - CountL,
    Cnt2 =
        if I >= L andalso I =< R ->
                Adjusted = case C of
                              Orig -> Cnt - 1;
                              NewC -> Cnt + 1;
                              _ -> Cnt
                          end,
                Adjusted;
           true -> Cnt
        end,
    Acc2 = if Cnt2 > 0 -> Acc + 1; true -> Acc end,
    distinct_in_range_loop(C + 1, MaxC, L, R, I, Orig, NewC, Prefs, Acc2).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_partitions_after_operations(s :: String.t(), k :: integer) :: integer
  def max_partitions_after_operations(s, k) do
    n = String.length(s)
    chars = for <<c <- s>>, do: c - ?a

    # prefix counts for each letter (26 arrays of size n+1)
    pref_counts =
      Enum.reduce(0..25, [], fn _l, acc ->
        [:array.new(n + 1, default: 0) | acc]
      end)
      |> Enum.reverse()

    {pref_counts, _} =
      Enum.reduce(0..(n - 1), {pref_counts, 0}, fn i, {cnts, _} ->
        ch = Enum.at(chars, i)

        new_cnts =
          Enum.map(0..25, fn l ->
            arr = Enum.at(cnts, l)
            prev = :array.get(i, arr)
            val = if l == ch, do: prev + 1, else: prev
            :array.set(i + 1, val, arr)
          end)

        {new_cnts, i}
      end)

    # compute greedy partitions, also fill partition_start and pref_partitions arrays
    partition_start = :array.new(n, default: 0)
    pref_parts = :array.new(n, default: 0)

    total_parts =
      greedy_partition(chars, k, n, partition_start, pref_parts, 0, 0, [])

    # helper to get number of partitions up to index i (inclusive)
    get_pref = fn idx ->
      if idx < 0, do: 0, else: :array.get(idx, pref_parts)
    end

    # suffix partitions count from i
    get_suff = fn idx ->
      if idx >= n, do: 0, else: total_parts - get_pref.(idx - 1)
    end

    # initial answer without any change
    ans = total_parts

    # iterate each position and try all other letters
    Enum.each(0..(n - 1), fn i ->
      old_ch = Enum.at(chars, i)
      l = :array.get(i, partition_start)

      Enum.each(0..25, fn new_ch ->
        if new_ch != old_ch do
          # find maximal r >= i such that distinct in [l, r] <= k after change
          r = max_right(l, i, old_ch, new_ch, n, pref_counts, k)

          total =
            cond do
              r >= i ->
                1 + get_pref.(l - 1) + get_suff.(r + 1)

              true ->
                # need second partition starting at i
                r2 = max_right(i, i, old_ch, new_ch, n, pref_counts, k)
                2 + get_pref.(l - 1) + get_suff.(r2 + 1)
            end

          if total > ans, do: ans = total
        end
      end)
    end)

    ans
  end

  # Greedy partitioning to fill arrays; returns total number of partitions
  defp greedy_partition(chars, k, n, part_start_arr, pref_arr, idx, parts_cnt, _acc) when idx >= n do
    parts_cnt
  end

  defp greedy_partition(chars, k, n, part_start_arr, pref_arr, idx, parts_cnt, acc) do
    # expand r as far as possible with at most k distinct chars
    {r, _freq, _dist} = expand(idx, chars, k, n, %{}, 0)

    # fill arrays for this segment [idx, r]
    Enum.each(idx..r, fn pos ->
      part_start_arr = :array.set(pos, idx, part_start_arr)
      pref_arr = :array.set(pos, parts_cnt + 1, pref_arr)
    end)

    greedy_partition(chars, k, n, part_start_arr, pref_arr, r + 1, parts_cnt + 1, acc)
  end

  # expand window from start idx
  defp expand(start_idx, chars, k, n, freq, distinct) do
    if start_idx >= n do
      {start_idx - 1, freq, distinct}
    else
      expand_loop(start_idx, start_idx - 1, chars, k, n, freq, distinct)
    end
  end

  defp expand_loop(_l, r, _chars, _k, _n, freq, distinct) when r + 1 >= length(_chars) do
    {r, freq, distinct}
  end

  defp expand_loop(l, r, chars, k, n, freq, distinct) do
    next = r + 1
    if next >= n do
      {r, freq, distinct}
    else
      ch = Enum.at(chars, next)
      cnt = Map.get(freq, ch, 0)
      new_distinct = if cnt == 0, do: distinct + 1, else: distinct

      if new_distinct <= k do
        new_freq = Map.put(freq, ch, cnt + 1)
        expand_loop(l, next, chars, k, n, new_freq, new_distinct)
      else
        {r, freq, distinct}
      end
    end
  end

  # binary search for maximal right index where distinct <= k after change
  defp max_right(l, start_idx, old_ch, new_ch, n, pref_counts, k) do
    low = start_idx
    high = n - 1
    ans = start_idx - 1

    while low <= high do
      mid = div(low + high, 2)

      distinct =
        distinct_with_change(l, mid, old_ch, new_ch, pref_counts)

      if distinct <= k do
        ans = mid
        low = mid + 1
      else
        high = mid - 1
      end
    end

    ans
  end

  defp distinct_with_change(l, r, old_ch, new_ch, pref_counts) do
    # original distinct count in [l, r]
    orig_distinct =
      Enum.reduce(0..25, 0, fn letter, acc ->
        arr = Enum.at(pref_counts, letter)
        cnt = :array.get(r + 1, arr) - :array.get(l, arr)
        if cnt > 0, do: acc + 1, else: acc
      end)

    # adjust for old character removal
    arr_old = Enum.at(pref_counts, old_ch)
    cnt_old_total = :array.get(r + 1, arr_old) - :array.get(l, arr_old)
    delta =
      if cnt_old_total == 1 do
        -1
      else
        0
      end

    # adjust for new character addition
    arr_new = Enum.at(pref_counts, new_ch)
    cnt_new_total = :array.get(r + 1, arr_new) - :array.get(l, arr_new)

    delta =
      if cnt_new_total == 0 do
        delta + 1
      else
        delta
      end

    orig_distinct + delta
  end
end
```
