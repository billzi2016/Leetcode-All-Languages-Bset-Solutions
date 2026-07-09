# 3348. Smallest Divisible Digit Product II

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string smallestNumber(string num, long long t) {
        // prime factors only 2,3,5,7
        const int P = 4;
        vector<int> req(P,0); // 0:2,1:3,2:5,3:7
        long long tmp=t;
        while (tmp%2==0){req[0]++;tmp/=2;}
        while (tmp%3==0){req[1]++;tmp/=3;}
        while (tmp%5==0){req[2]++;tmp/=5;}
        while (tmp%7==0){req[3]++;tmp/=7;}
        if (tmp!=1) return "-1";
        // digit contributions
        int expd[10][4]={0};
        auto add=[&](int d,int p,int e){expd[d][p]=e;};
        for(int d=1;d<=9;++d){
            int x=d;
            while(x%2==0){expd[d][0]++;x/=2;}
            while(x%3==0){expd[d][1]++;x/=3;}
            while(x%5==0){expd[d][2]++;x/=5;}
            while(x%7==0){expd[d][3]++;x/=7;}
        }
        // DP for minimal digits to achieve any exponent vector up to req
        int E2=req[0],E3=req[1],E5=req[2],E7=req[3];
        long long totalStates=1LL*(E2+1)*(E3+1)*(E5+1)*(E7+1);
        const int INF = 1e9;
        vector<int> dp(totalStates, INF);
        auto encode=[&](int a,int b,int c,int d)->int{
            return ((a*(E3+1)+b)*(E5+1)+c)*(E7+1)+d;
        };
        dp[0]=0;
        queue<int> q;
        q.push(0);
        while(!q.empty()){
            int idx=q.front();q.pop();
            int cur=dp[idx];
            // decode
            int d4 = idx % (E7+1);
            int tmp = idx / (E7+1);
            int d3 = tmp % (E5+1);
            tmp /= (E5+1);
            int d2 = tmp % (E3+1);
            int d1 = tmp / (E3+1);
            for(int dig=1;dig<=9;++dig){
                int na=min(E2, d1 + expd[dig][0]);
                int nb=min(E3, d2 + expd[dig][1]);
                int nc=min(E5, d3 + expd[dig][2]);
                int nd=min(E7, d4 + expd[dig][3]);
                int nidx=encode(na,nb,nc,nd);
                if(dp[nidx]>cur+1){
                    dp[nidx]=cur+1;
                    q.push(nidx);
                }
            }
        }
        int targetIdx = encode(E2,E3,E5,E7);
        int minLenNeeded = dp[targetIdx];
        if(minLenNeeded==INF) return "-1";
        // helper to build number
        auto build=[&](int L, const string &bound, bool useBound)->string{
            vector<int> rem=req;
            bool tight=true;
            string res; res.reserve(L);
            for(int i=0;i<L;++i){
                int low=1;
                if(tight && useBound && i<(int)bound.size()){
                    low = max(bound[i]-'0', 1);
                }
                bool placed=false;
                for(int d=low;d<=9;++d){
                    vector<int> nrem(4);
                    for(int p=0;p<4;++p){
                        nrem[p]=max(0, rem[p]-expd[d][p]);
                    }
                    int k = L - i - 1;
                    int idx = encode(nrem[0],nrem[1],nrem[2],nrem[3]);
                    if(dp[idx]<=k){
                        res.push_back('0'+d);
                        rem.swap(nrem);
                        if(tight && useBound && i<(int)bound.size()){
                            if(d > bound[i]-'0') tight=false;
                        }else{
                            tight=false;
                        }
                        placed=true;
                        break;
                    }
                }
                if(!placed) return "";
            }
            return res;
        };
        // try length = num.size()
        string ans = build((int)num.size(), num, true);
        if(!ans.empty()) return ans;
        // need longer length
        int L = max((int)num.size()+1, minLenNeeded);
        ans = build(L, string(), false);
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static final int[][] DIGIT_EXP = new int[10][4];
    static {
        // primes: 2,3,5,7
        for (int d = 0; d <= 9; d++) {
            int x = d;
            for (int p = 0; p < 4; p++) {
                int prime = (p == 0) ? 2 : (p == 1) ? 3 : (p == 2) ? 5 : 7;
                while (x % prime == 0 && x > 0) {
                    DIGIT_EXP[d][p]++;
                    x /= prime;
                }
            }
        }
    }

    public String smallestNumber(String num, long t) {
        int[] req = factorize(t);
        if (req == null) return "-1";

        // quick check if original number already satisfies
        if (isZeroFree(num)) {
            int[] curExp = getExp(num);
            if (covers(curExp, req)) return num;
        }

        int n = num.length();
        int[][] prefExp = new int[n + 1][4];
        boolean[] validPref = new boolean[n + 1];
        validPref[0] = true;
        for (int i = 0; i < n; i++) {
            char c = num.charAt(i);
            int d = c - '0';
            System.arraycopy(prefExp[i], 0, prefExp[i + 1], 0, 4);
            if (d == 0) {
                validPref[i + 1] = false;
            } else {
                for (int p = 0; p < 4; p++) prefExp[i + 1][p] += DIGIT_EXP[d][p];
                validPref[i + 1] = validPref[i];
            }
        }

        // try to modify within same length
        for (int i = n - 1; i >= 0; i--) {
            if (!validPref[i]) continue; // prefix up to i-1 must be zero‑free
            int curDigit = num.charAt(i) - '0';
            int start = Math.max(curDigit + 1, 1);
            for (int d = start; d <= 9; d++) {
                int[] acc = new int[4];
                System.arraycopy(prefExp[i], 0, acc, 0, 4);
                for (int p = 0; p < 4; p++) acc[p] += DIGIT_EXP[d][p];

                int remLen = n - i - 1;
                int[] need = needed(req, acc);
                if (!feasible(need, remLen)) continue;

                // construct answer
                char[] ans = new char[n];
                for (int k = 0; k < i; k++) ans[k] = num.charAt(k);
                ans[i] = (char) ('0' + d);
                int[] curNeed = need;
                for (int pos = i + 1; pos < n; pos++) {
                    int remaining = n - pos - 1;
                    for (int nd = 1; nd <= 9; nd++) {
                        int[] after = new int[4];
                        for (int p = 0; p < 4; p++) {
                            after[p] = Math.max(0, curNeed[p] - DIGIT_EXP[nd][p]);
                        }
                        if (feasible(after, remaining)) {
                            ans[pos] = (char) ('0' + nd);
                            curNeed = after;
                            break;
                        }
                    }
                }
                return new String(ans);
            }
        }

        // need longer length
        int minDigitsNeeded = Math.max(
                Math.max(ceilDiv(req[0], 3), ceilDiv(req[1], 2)),
                Math.max(req[2], req[3])
        );
        int len = Math.max(n + 1, Math.max(minDigitsNeeded, 1));
        String res = buildMinimal(len, req);
        return res == null ? "-1" : res;
    }

    private int[] factorize(long t) {
        int[] need = new int[4];
        long[] primes = {2, 3, 5, 7};
        for (int i = 0; i < 4; i++) {
            while (t % primes[i] == 0) {
                need[i]++;
                t /= primes[i];
            }
        }
        return t == 1 ? need : null;
    }

    private boolean isZeroFree(String s) {
        for (int i = 0; i < s.length(); i++) if (s.charAt(i) == '0') return false;
        return true;
    }

    private int[] getExp(String s) {
        int[] e = new int[4];
        for (int i = 0; i < s.length(); i++) {
            int d = s.charAt(i) - '0';
            for (int p = 0; p < 4; p++) e[p] += DIGIT_EXP[d][p];
        }
        return e;
    }

    private boolean covers(int[] have, int[] need) {
        for (int i = 0; i < 4; i++) if (have[i] < need[i]) return false;
        return true;
    }

    private int[] needed(int[] req, int[] acc) {
        int[] nd = new int[4];
        for (int i = 0; i < 4; i++) nd[i] = Math.max(0, req[i] - acc[i]);
        return nd;
    }

    private boolean feasible(int[] need, int len) {
        if (need[0] > 3 * len) return false;
        if (need[1] > 2 * len) return false;
        if (need[2] > len) return false;
        if (need[3] > len) return false;
        return true;
    }

    private int ceilDiv(int a, int b) {
        return (a + b - 1) / b;
    }

    private String buildMinimal(int len, int[] req) {
        char[] ans = new char[len];
        int[] need = Arrays.copyOf(req, 4);
        for (int pos = 0; pos < len; pos++) {
            int remaining = len - pos - 1;
            boolean placed = false;
            for (int d = 1; d <= 9; d++) {
                int[] after = new int[4];
                for (int p = 0; p < 4; p++) after[p] = Math.max(0, need[p] - DIGIT_EXP[d][p]);
                if (feasible(after, remaining)) {
                    ans[pos] = (char) ('0' + d);
                    need = after;
                    placed = true;
                    break;
                }
            }
            if (!placed) return null; // should not happen
        }
        return new String(ans);
    }
}
```

## Python

```python
class Solution(object):
    def smallestNumber(self, num, t):
        """
        :type num: str
        :type t: int
        :rtype: str
        """
        # factorize t into 2,3,5,7 only
        need = [0, 0, 0, 0]  # exponents for 2,3,5,7
        orig_t = t
        for idx, p in enumerate([2, 3, 5, 7]):
            while t % p == 0:
                need[idx] += 1
                t //= p
        if t != 1:  # contains other prime factor -> impossible
            return "-1"

        # exponent contribution of each digit 0-9 (we will never use 0)
        exp = [
            (0, 0, 0, 0),  # 0 placeholder
            (0, 0, 0, 0),  # 1
            (1, 0, 0, 0),  # 2
            (0, 1, 0, 0),  # 3
            (2, 0, 0, 0),  # 4
            (0, 0, 1, 0),  # 5
            (1, 1, 0, 0),  # 6
            (0, 0, 0, 1),  # 7
            (3, 0, 0, 0),  # 8
            (0, 2, 0, 0)   # 9
        ]

        max_per_digit = [3, 2, 1, 1]  # per slot maximum exponents for 2,3,5,7

        def feasible(need_vec, slots):
            return (need_vec[0] <= max_per_digit[0] * slots and
                    need_vec[1] <= max_per_digit[1] * slots and
                    need_vec[2] <= max_per_digit[2] * slots and
                    need_vec[3] <= max_per_digit[3] * slots)

        def build_min(length, need_vec):
            """greedy smallest lexicographic string of given length satisfying need_vec"""
            res = []
            cur_need = list(need_vec)
            for pos in range(length):
                slots_left = length - pos - 1
                for d in range(1, 10):
                    e = exp[d]
                    new_need = [
                        max(cur_need[0] - e[0], 0),
                        max(cur_need[1] - e[1], 0),
                        max(cur_need[2] - e[2], 0),
                        max(cur_need[3] - e[3], 0)
                    ]
                    if feasible(new_need, slots_left):
                        res.append(str(d))
                        cur_need = new_need
                        break
            return ''.join(res)

        n = len(num)

        # helper to compute exponents of a string (assumes no zeros)
        def exps_of_string(s):
            e2=e3=e5=e7=0
            for ch in s:
                d=int(ch)
                ee=exp[d]
                e2+=ee[0]; e3+=ee[1]; e5+=ee[2]; e7+=ee[3]
            return [e2,e3,e5,e7]

        # check if num itself is valid
        if '0' not in num:
            cur = exps_of_string(num)
            if (cur[0] >= need[0] and cur[1] >= need[1] and
                cur[2] >= need[2] and cur[3] >= need[3]):
                return num

        # attempt to find answer with same length
        prefix_need = [0, 0, 0, 0]
        for i in range(n):
            orig_digit = int(num[i])
            if orig_digit == 0:
                # cannot keep zero, must increase earlier; stop trying equal prefix beyond this point
                break
            # try to increase at position i
            for d in range(orig_digit + 1, 10):
                e = exp[d]
                new_need = [
                    max(need[0] - (prefix_need[0] + e[0]), 0),
                    max(need[1] - (prefix_need[1] + e[1]), 0),
                    max(need[2] - (prefix_need[2] + e[2]), 0),
                    max(need[3] - (prefix_need[3] + e[3]), 0)
                ]
                slots = n - i - 1
                if feasible(new_need, slots):
                    suffix = build_min(slots, new_need)
                    return num[:i] + str(d) + suffix
            # keep the same digit and continue prefix accumulation
            e_orig = exp[orig_digit]
            prefix_need[0] += e_orig[0]
            prefix_need[1] += e_orig[1]
            prefix_need[2] += e_orig[2]
            prefix_need[3] += e_orig[3]
        # if loop completed without break, all digits were non-zero but no solution found (num itself invalid)
        # otherwise we hit a zero earlier and couldn't fix; need longer length

        # compute minimal required length based on needed exponents
        min_len_needed = 0
        for idx, mx in enumerate(max_per_digit):
            if need[idx] > 0:
                req = (need[idx] + mx - 1) // mx
                if req > min_len_needed:
                    min_len_needed = req

        L = max(n + 1, min_len_needed)
        # ensure feasibility; it always will be because we can use enough digits
        while True:
            if feasible(need, L):
                return build_min(L, need)
            L += 1  # safety, though should not happen

        # unreachable
        return "-1"
```

## Python3

```python
import sys
from collections import deque

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # factorize t into 2,3,5,7 only
        need = [0, 0, 0, 0]  # exponents for 2,3,5,7
        primes = [2, 3, 5, 7]
        tmp = t
        for idx, p in enumerate(primes):
            while tmp % p == 0:
                need[idx] += 1
                tmp //= p
        if tmp != 1:   # contains other prime factor
            return "-1"

        r2, r3, r5, r7 = need

        # digit contributions
        contrib = {}
        for d in range(1, 10):
            x = d
            c2 = c3 = c5 = c7 = 0
            while x % 2 == 0:
                c2 += 1
                x //= 2
            while x % 3 == 0:
                c3 += 1
                x //= 3
            while x % 5 == 0:
                c5 += 1
                x //= 5
            while x % 7 == 0:
                c7 += 1
                x //= 7
            contrib[d] = (c2, c3, c5, c7)

        # DP: minimal digits needed to reach at least each exponent vector
        INF = 10**9
        dp = [[[[INF] * (r7 + 1) for _ in range(r5 + 1)] for _ in range(r3 + 1)] for _ in range(r2 + 1)]
        dp[0][0][0][0] = 0
        q = deque()
        q.append((0, 0, 0, 0))
        while q:
            a, b, c, d = q.popleft()
            cur = dp[a][b][c][d]
            for da, db, dc, dd in contrib.values():
                na = min(r2, a + da)
                nb = min(r3, b + db)
                nc = min(r5, c + dc)
                nd = min(r7, d + dd)
                if dp[na][nb][nc][nd] > cur + 1:
                    dp[na][nb][nc][nd] = cur + 1
                    q.append((na, nb, nc, nd))

        min_needed = dp[r2][r3][r5][r7]
        if min_needed == INF:
            return "-1"

        n = len(num)
        num_digits = [int(ch) for ch in num]

        # attempt same length
        chosen = [0] * n
        pref2 = [0] * (n + 1)
        pref3 = [0] * (n + 1)
        pref5 = [0] * (n + 1)
        pref7 = [0] * (n + 1)
        tight_at = [False] * (n + 1)
        tight_at[0] = True

        i = 0
        while i >= 0 and i < n:
            low = num_digits[i] if tight_at[i] else 1
            start = chosen[i] + 1 if chosen[i] != 0 else max(low, 1)
            found = False
            for d in range(start, 10):
                c2, c3, c5, c7 = contrib[d]
                new2 = pref2[i] + c2
                new3 = pref3[i] + c3
                new5 = pref5[i] + c5
                new7 = pref7[i] + c7
                need2 = r2 - new2 if new2 < r2 else 0
                need3 = r3 - new3 if new3 < r3 else 0
                need5 = r5 - new5 if new5 < r5 else 0
                need7 = r7 - new7 if new7 < r7 else 0
                rem_len = n - i - 1
                if dp[need2][need3][need5][need7] <= rem_len:
                    chosen[i] = d
                    pref2[i + 1] = new2
                    pref3[i + 1] = new3
                    pref5[i + 1] = new5
                    pref7[i + 1] = new7
                    tight_at[i + 1] = tight_at[i] and (d == num_digits[i])
                    found = True
                    break
            if found:
                i += 1
            else:
                chosen[i] = 0
                i -= 1

        if i == n:   # success
            return ''.join(str(d) for d in chosen)

        # need longer length
        L = max(n + 1, min_needed)
        ans = []
        cur2 = cur3 = cur5 = cur7 = 0
        for pos in range(L):
            for d in range(1, 10):
                c2, c3, c5, c7 = contrib[d]
                new2 = cur2 + c2
                new3 = cur3 + c3
                new5 = cur5 + c5
                new7 = cur7 + c7
                need2 = r2 - new2 if new2 < r2 else 0
                need3 = r3 - new3 if new3 < r3 else 0
                need5 = r5 - new5 if new5 < r5 else 0
                need7 = r7 - new7 if new7 < r7 else 0
                rem_len = L - pos - 1
                if dp[need2][need3][need5][need7] <= rem_len:
                    ans.append(str(d))
                    cur2, cur3, cur5, cur7 = new2, new3, new5, new7
                    break
        return ''.join(ans)
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static const int contrib[10][4] = {
    {0,0,0,0}, //0 (unused)
    {0,0,0,0}, //1
    {1,0,0,0}, //2
    {0,1,0,0}, //3
    {2,0,0,0}, //4
    {0,0,1,0}, //5
    {1,1,0,0}, //6
    {0,0,0,1}, //7
    {3,0,0,0}, //8
    {0,2,0,0}  //9
};

static inline int can(int rem, const int need[4]) {
    return need[0] <= 3 * rem && need[1] <= 2 * rem &&
           need[2] <= rem && need[3] <= rem;
}

char* smallestNumber(char* num, long long t) {
    int need[4] = {0,0,0,0};
    long long tmp = t;
    while (tmp % 2 == 0) { need[0]++; tmp /= 2; }
    while (tmp % 3 == 0) { need[1]++; tmp /= 3; }
    while (tmp % 5 == 0) { need[2]++; tmp /= 5; }
    while (tmp % 7 == 0) { need[3]++; tmp /= 7; }
    if (tmp != 1) return strdup("-1");

    int n = strlen(num);
    int (*pref)[4] = malloc((n + 1) * sizeof(int[4]));
    pref[0][0]=pref[0][1]=pref[0][2]=pref[0][3]=0;
    for (int i = 0; i < n; ++i) {
        int d = num[i] - '0';
        for (int p = 0; p < 4; ++p) pref[i+1][p] = pref[i][p];
        if (d != 0) {
            const int *c = contrib[d];
            for (int p = 0; p < 4; ++p) pref[i+1][p] += c[p];
        }
    }

    bool *hasZeroBefore = malloc((n + 1) * sizeof(bool));
    hasZeroBefore[0] = false;
    for (int i = 1; i <= n; ++i)
        hasZeroBefore[i] = hasZeroBefore[i-1] || (num[i-1]=='0');

    /* if original number already valid */
    if (!hasZeroBefore[n]) {
        int ok = 1;
        for (int p = 0; p < 4; ++p) {
            if (pref[n][p] < need[p]) { ok = 0; break; }
        }
        if (ok) {
            char *ans = strdup(num);
            free(pref); free(hasZeroBefore);
            return ans;
        }
    }

    /* try to keep same length */
    for (int i = n-1; i >= 0; --i) {
        if (hasZeroBefore[i]) continue;   // prefix would contain zero
        int curNeed[4];
        for (int p = 0; p < 4; ++p) {
            int diff = need[p] - pref[i][p];
            curNeed[p] = diff > 0 ? diff : 0;
        }
        int start = num[i]-'0' + 1;
        for (int d = start; d <= 9; ++d) {
            if (d == 0) continue;
            const int *cd = contrib[d];
            int newNeed[4];
            for (int p = 0; p < 4; ++p) {
                int diff = curNeed[p] - cd[p];
                newNeed[p] = diff > 0 ? diff : 0;
            }
            int rem = n - i - 1;
            if (!can(rem, newNeed)) continue;

            char *ans = malloc(n + 1);
            memcpy(ans, num, i);
            ans[i] = '0' + d;

            int needNow[4];
            for (int p = 0; p < 4; ++p) needNow[p] = newNeed[p];

            for (int j = i+1; j < n; ++j) {
                for (int nd = 1; nd <= 9; ++nd) {
                    const int *c2 = contrib[nd];
                    int after[4];
                    for (int p = 0; p < 4; ++p) {
                        int diff = needNow[p] - c2[p];
                        after[p] = diff > 0 ? diff : 0;
                    }
                    if (can(n - j - 1, after)) {
                        ans[j] = '0' + nd;
                        for (int p = 0; p < 4; ++p) needNow[p] = after[p];
                        break;
                    }
                }
            }
            ans[n] = '\0';
            free(pref); free(hasZeroBefore);
            return ans;
        }
    }

    /* need longer length */
    int Lmin = 0;
    if (need[0] > 0) {
        int v = (need[0] + 3 - 1) / 3;
        if (v > Lmin) Lmin = v;
    }
    if (need[1] > 0) {
        int v = (need[1] + 2 - 1) / 2;
        if (v > Lmin) Lmin = v;
    }
    if (need[2] > Lmin) Lmin = need[2];
    if (need[3] > Lmin) Lmin = need[3];

    int finalLen = n + 1;
    if (finalLen < Lmin) finalLen = Lmin;

    char *ans = malloc(finalLen + 1);
    int curNeed[4];
    for (int p = 0; p < 4; ++p) curNeed[p] = need[p];

    for (int idx = 0; idx < finalLen; ++idx) {
        for (int d = 1; d <= 9; ++d) {
            const int *cd = contrib[d];
            int after[4];
            for (int p = 0; p < 4; ++p) {
                int diff = curNeed[p] - cd[p];
                after[p] = diff > 0 ? diff : 0;
            }
            if (can(finalLen - idx - 1, after)) {
                ans[idx] = '0' + d;
                for (int p = 0; p < 4; ++p) curNeed[p] = after[p];
                break;
            }
        }
    }
    ans[finalLen] = '\0';
    free(pref); free(hasZeroBefore);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Text;

public class Solution {
    public string SmallestNumber(string num, long t) {
        // factorize t into 2,3,5,7
        int[] need = new int[4];
        foreach (var p in new int[]{2,3,5,7}) {
            while (t % p == 0) {
                if (p == 2) need[0]++;
                else if (p == 3) need[1]++;
                else if (p == 5) need[2]++;
                else need[3]++;
                t /= p;
            }
        }
        if (t != 1) return "-1";

        // digit exponents
        int[][] exp = new int[10][];
        for (int d = 0; d <= 9; d++) exp[d] = new int[4];
        for (int d = 1; d <= 9; d++) {
            int x = d;
            while (x % 2 == 0) { exp[d][0]++; x /= 2; }
            while (x % 3 == 0) { exp[d][1]++; x /= 3; }
            while (x % 5 == 0) { exp[d][2]++; x /= 5; }
            while (x % 7 == 0) { exp[d][3]++; x /= 7; }
        }

        int A = need[0], B = need[1], C = need[2], D = need[3];
        int size = (A + 1) * (B + 1) * (C + 1) * (D + 1);
        const int INF = 1_000_000_000;
        int[] minLen = new int[size];
        for (int i = 0; i < size; i++) minLen[i] = INF;

        Func<int,int,int,int,int,int> idx = (a,b,c,dv) => {
            return (((a)*(B+1)+b)*(C+1)+c)*(D+1)+dv;
        };

        Queue<int> q = new Queue<int>();
        int startIdx = idx(0,0,0,0);
        minLen[startIdx] = 0;
        q.Enqueue(startIdx);

        while (q.Count > 0) {
            int cur = q.Dequeue();
            int tmp = cur;
            int dv = tmp % (D+1); tmp /= (D+1);
            int c = tmp % (C+1); tmp /= (C+1);
            int b = tmp % (B+1); tmp /= (B+1);
            int a = tmp;

            foreach (int d in new int[]{1,2,3,4,5,6,7,8,9}) {
                int na = Math.Min(A, a + exp[d][0]);
                int nb = Math.Min(B, b + exp[d][1]);
                int nc = Math.Min(C, c + exp[d][2]);
                int nd = Math.Min(D, dv + exp[d][3]);
                int nIdx = idx(na, nb, nc, nd);
                if (minLen[nIdx] > minLen[cur] + 1) {
                    minLen[nIdx] = minLen[cur] + 1;
                    q.Enqueue(nIdx);
                }
            }
        }

        if (minLen[idx(A,B,C,D)] == INF) return "-1";

        // helper to get min length for a need vector
        int GetMinLen(int[] v) => minLen[idx(v[0],v[1],v[2],v[3])];

        // check original number
        bool zeroFree = true;
        int[] curExp = new int[4];
        foreach (char ch in num) {
            int d = ch - '0';
            if (d == 0) { zeroFree = false; break; }
            for (int i=0;i<4;i++) curExp[i] += exp[d][i];
        }
        bool ok = zeroFree && curExp[0]>=need[0] && curExp[1]>=need[1] && curExp[2]>=need[2] && curExp[3]>=need[3];
        if (ok) return num;

        int n = num.Length;
        // prefix exponent sums and zero flag
        int[][] pref = new int[n+1][];
        bool[] zeroPref = new bool[n+1];
        pref[0] = new int[4];
        zeroPref[0] = false;
        for (int i=0;i<n;i++) {
            int d = num[i]-'0';
            int[] arr = new int[4];
            Array.Copy(pref[i], arr, 4);
            if (d == 0) zeroPref[i+1] = true;
            else zeroPref[i+1] = zeroPref[i];
            if (d != 0) {
                for (int j=0;j<4;j++) arr[j] += exp[d][j];
            }
            pref[i+1] = arr;
        }

        // attempt same length
        for (int pos=n-1; pos>=0; pos--) {
            if (zeroPref[pos]) continue; // cannot keep prefix equal due to earlier zero
            int curDigit = num[pos]-'0';
            for (int d = Math.Max(curDigit+1,1); d<=9; d++) {
                int[] newExp = new int[4];
                for (int j=0;j<4;j++) newExp[j] = pref[pos][j] + exp[d][j];
                int[] remNeed = new int[4];
                for (int j=0;j<4;j++) remNeed[j] = Math.Max(need[j]-newExp[j], 0);
                int slots = n - pos - 1;
                if (GetMinLen(remNeed) <= slots) {
                    StringBuilder sb = new StringBuilder();
                    sb.Append(num.Substring(0,pos));
                    sb.Append((char)('0'+d));

                    int[] curNeed = remNeed;
                    for (int i=0;i<slots;i++) {
                        foreach (int nd in new int[]{1,2,3,4,5,6,7,8,9}) {
                            int[] after = new int[4];
                            for (int j=0;j<4;j++) after[j] = Math.Max(curNeed[j]-exp[nd][j], 0);
                            if (GetMinLen(after) <= slots - i - 1) {
                                sb.Append((char)('0'+nd));
                                curNeed = after;
                                break;
                            }
                        }
                    }
                    return sb.ToString();
                }
            }
        }

        // need longer length: construct minimal string of length minLen[need]
        int totalSlots = GetMinLen(need);
        StringBuilder finalSb = new StringBuilder();
        int[] curNeed2 = (int[])need.Clone();
        for (int i=0;i<totalSlots;i++) {
            foreach (int d in new int[]{1,2,3,4,5,6,7,8,9}) {
                int[] after = new int[4];
                for (int j=0;j<4;j++) after[j] = Math.Max(curNeed2[j]-exp[d][j], 0);
                if (GetMinLen(after) <= totalSlots - i - 1) {
                    finalSb.Append((char)('0'+d));
                    curNeed2 = after;
                    break;
                }
            }
        }
        return finalSb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} num
 * @param {number} t
 * @return {string}
 */
var smallestNumber = function(num, t) {
    // factorize t into 2,3,5,7 only
    const need = [0, 0, 0, 0]; // 2,3,5,7 exponents
    let tmp = t;
    const primes = [2, 3, 5, 7];
    for (let i = 0; i < 4; ++i) {
        const p = primes[i];
        while (tmp % p === 0) {
            need[i]++;
            tmp /= p;
        }
    }
    if (tmp !== 1) return "-1";

    // digit exponent table
    const exp = Array.from({ length: 10 }, () => [0, 0, 0, 0]);
    exp[2] = [1, 0, 0, 0];
    exp[3] = [0, 1, 0, 0];
    exp[4] = [2, 0, 0, 0];
    exp[5] = [0, 0, 1, 0];
    exp[6] = [1, 1, 0, 0];
    exp[7] = [0, 0, 0, 1];
    exp[8] = [3, 0, 0, 0];
    exp[9] = [0, 2, 0, 0];

    const maxPer = [3, 2, 1, 1]; // per digit maximum exponents for 2,3,5,7

    function feasible(c2, c3, c5, c7, rem) {
        return (
            c2 + rem * maxPer[0] >= need[0] &&
            c3 + rem * maxPer[1] >= need[1] &&
            c5 + rem * maxPer[2] >= need[2] &&
            c7 + rem * maxPer[3] >= need[3]
        );
    }

    const n = num.length;
    const ans = new Array(n);
    const snap2 = new Array(n), snap3 = new Array(n), snap5 = new Array(n), snap7 = new Array(n);

    let cur2 = 0, cur3 = 0, cur5 = 0, cur7 = 0;
    let pos = 0;

    while (pos >= 0 && pos < n) {
        let startDigit;
        if (ans[pos] === undefined) {
            startDigit = num.charCodeAt(pos) - 48; // original digit
        } else {
            startDigit = ans[pos] + 1; // try larger after backtrack
        }
        let found = false;
        for (let d = Math.max(startDigit, 1); d <= 9; ++d) { // skip zero
            const nd2 = cur2 + exp[d][0];
            const nd3 = cur3 + exp[d][1];
            const nd5 = cur5 + exp[d][2];
            const nd7 = cur7 + exp[d][3];
            if (feasible(nd2, nd3, nd5, nd7, n - pos - 1)) {
                ans[pos] = d;
                cur2 = nd2; cur3 = nd3; cur5 = nd5; cur7 = nd7;
                snap2[pos] = cur2; snap3[pos] = cur3; snap5[pos] = cur5; snap7[pos] = cur7;
                found = true;
                break;
            }
        }
        if (found) {
            ++pos;
        } else {
            // backtrack
            ans[pos] = undefined;
            --pos;
            if (pos >= 0) {
                cur2 = snap2[pos];
                cur3 = snap3[pos];
                cur5 = snap5[pos];
                cur7 = snap7[pos];
            }
        }
    }

    if (pos === n) {
        // built a valid number of same length
        return ans.join('');
    }

    // need longer length
    let minLen = 0;
    for (let i = 0; i < 4; ++i) {
        if (need[i] > 0) {
            const cur = Math.floor((need[i] + maxPer[i] - 1) / maxPer[i]);
            if (cur > minLen) minLen = cur;
        }
    }
    let L = Math.max(n + 1, minLen);
    while (!feasible(0, 0, 0, 0, L)) ++L;

    // greedy build minimal number of length L
    const res = new Array(L);
    let c2 = 0, c3 = 0, c5 = 0, c7 = 0;
    for (let i = 0; i < L; ++i) {
        for (let d = 1; d <= 9; ++d) {
            const nd2 = c2 + exp[d][0];
            const nd3 = c3 + exp[d][1];
            const nd5 = c5 + exp[d][2];
            const nd7 = c7 + exp[d][3];
            if (feasible(nd2, nd3, nd5, nd7, L - i - 1)) {
                res[i] = d;
                c2 = nd2; c3 = nd3; c5 = nd5; c7 = nd7;
                break;
            }
        }
    }
    return res.join('');
};
```

## Typescript

```typescript
function smallestNumber(num: string, t: number): string {
    // factorize t into 2,3,5,7
    const primes = [2, 3, 5, 7];
    const need = [0, 0, 0, 0]; // exponents for 2,3,5,7
    let tmp = t;
    for (let i = 0; i < 4; i++) {
        const p = primes[i];
        while (tmp % p === 0) {
            need[i]++;
            tmp /= p;
        }
    }
    if (tmp !== 1) return "-1";

    // digit exponent contributions
    const digExp: number[][] = Array.from({ length: 10 }, () => [0, 0, 0, 0]);
    const add = (d: number, e2: number, e3: number, e5: number, e7: number) => {
        digExp[d] = [e2, e3, e5, e7];
    };
    add(1, 0, 0, 0, 0);
    add(2, 1, 0, 0, 0);
    add(3, 0, 1, 0, 0);
    add(4, 2, 0, 0, 0);
    add(5, 0, 0, 1, 0);
    add(6, 1, 1, 0, 0);
    add(7, 0, 0, 0, 1);
    add(8, 3, 0, 0, 0);
    add(9, 0, 2, 0, 0);

    const maxE2 = need[0], maxE3 = need[1], maxE5 = need[2], maxE7 = need[3];
    const dim2 = maxE2 + 1, dim3 = maxE3 + 1, dim5 = maxE5 + 1, dim7 = maxE7 + 1;
    const totalSize = dim2 * dim3 * dim5 * dim7;

    const mul3 = dim7;
    const mul2 = dim5 * mul3;
    const mul1 = dim3 * mul2;

    const encode = (e2: number, e3: number, e5: number, e7: number): number => {
        return ((e2 * dim3 + e3) * dim5 + e5) * dim7 + e7;
    };

    const INF = 255;
    const dp = new Uint8Array(totalSize);
    dp.fill(INF);
    dp[0] = 0;

    // DP for minimal number of digits to satisfy at least given exponents
    for (let e2 = 0; e2 <= maxE2; e2++) {
        for (let e3 = 0; e3 <= maxE3; e3++) {
            for (let e5 = 0; e5 <= maxE5; e5++) {
                for (let e7 = 0; e7 <= maxE7; e7++) {
                    const idx = encode(e2, e3, e5, e7);
                    const cur = dp[idx];
                    if (cur === INF) continue;
                    for (let d = 2; d <= 9; d++) {
                        const de = digExp[d];
                        const ne2 = Math.min(maxE2, e2 + de[0]);
                        const ne3 = Math.min(maxE3, e3 + de[1]);
                        const ne5 = Math.min(maxE5, e5 + de[2]);
                        const ne7 = Math.min(maxE7, e7 + de[3]);
                        const nIdx = encode(ne2, ne3, ne5, ne7);
                        if (dp[nIdx] > cur + 1) dp[nIdx] = cur + 1;
                    }
                }
            }
        }
    }

    const targetIdx = encode(maxE2, maxE3, maxE5, maxE7);
    const minDigitsNeededOverall = dp[targetIdx];
    if (minDigitsNeededOverall === INF) return "-1";

    // Try to build answer with same length
    const n = num.length;
    const chosen: number[] = new Array(n);
    const preE2 = new Int16Array(n);
    const preE3 = new Int16Array(n);
    const preE5 = new Int16Array(n);
    const preE7 = new Int16Array(n);
    const preTight = new Uint8Array(n); // 0 or 1

    let curE2 = maxE2, curE3 = maxE3, curE5 = maxE5, curE7 = maxE7;
    let tight = 1; // true
    let i = 0;

    while (true) {
        if (i === n) {
            return chosen.join('');
        }
        const startDigit = tight ? Number(num[i]) : 1;
        const prevChosen = chosen[i] ?? -1;
        let dStart = Math.max(startDigit, prevChosen + 1);
        let found = false;
        for (let d = dStart; d <= 9; d++) {
            const de = digExp[d];
            const ne2 = Math.max(0, curE2 - de[0]);
            const ne3 = Math.max(0, curE3 - de[1]);
            const ne5 = Math.max(0, curE5 - de[2]);
            const ne7 = Math.max(0, curE7 - de[3]);
            const needIdx = encode(ne2, ne3, ne5, ne7);
            if (dp[needIdx] <= n - i - 1) {
                // store state for possible backtrack
                preE2[i] = curE2;
                preE3[i] = curE3;
                preE5[i] = curE5;
                preE7[i] = curE7;
                preTight[i] = tight;
                chosen[i] = d;
                curE2 = ne2; curE3 = ne3; curE5 = ne5; curE7 = ne7;
                tight = (tight && d === startDigit) ? 1 : 0;
                i++;
                found = true;
                break;
            }
        }
        if (!found) {
            // backtrack
            i--;
            if (i < 0) break; // cannot build same length
            curE2 = preE2[i];
            curE3 = preE3[i];
            curE5 = preE5[i];
            curE7 = preE7[i];
            tight = preTight[i];
        }
    }

    // Build answer with longer length
    const k = minDigitsNeededOverall; // minimal non‑1 digits required
    const L = Math.max(n + 1, k);
    let needE2 = maxE2, needE3 = maxE3, needE5 = maxE5, needE7 = maxE7;
    const suffix: number[] = [];
    while (needE2 > 0 || needE3 > 0 || needE5 > 0 || needE7 > 0) {
        for (let d = 2; d <= 9; d++) {
            const de = digExp[d];
            const ne2 = Math.max(0, needE2 - de[0]);
            const ne3 = Math.max(0, needE3 - de[1]);
            const ne5 = Math.max(0, needE5 - de[2]);
            const ne7 = Math.max(0, needE7 - de[3]);
            if (dp[encode(ne2, ne3, ne5, ne7)] === dp[encode(needE2, needE3, needE5, needE7)] - 1) {
                suffix.push(d);
                needE2 = ne2; needE3 = ne3; needE5 = ne5; needE7 = ne7;
                break;
            }
        }
    }
    suffix.sort((a, b) => a - b);
    const result = '1'.repeat(L - suffix.length) + suffix.join('');
    return result;
}
```

## Php

```php
class Solution {
    /**
     * @param String $num
     * @param Integer $t
     * @return String
     */
    function smallestNumber($num, $t) {
        // factor t into primes 2,3,5,7
        $req = [0,0,0,0]; // indices: 0->2,1->3,2->5,3->7
        foreach ([2,3,5,7] as $idx=>$p) {
            while ($t % $p == 0) {
                $req[$idx]++;
                $t /= $p;
            }
        }
        if ($t != 1) return "-1";

        // digit exponents
        $digitExp = [];
        for ($d=0;$d<=9;$d++) {
            $e2=$e3=$e5=$e7=0;
            $x=$d;
            while ($x % 2 == 0 && $x>0) {$e2++; $x/=2;}
            while ($x % 3 == 0 && $x>0) {$e3++; $x/=3;}
            while ($x % 5 == 0 && $x>0) {$e5++; $x/=5;}
            while ($x % 7 == 0 && $x>0) {$e7++; $x/=7;}
            $digitExp[$d]=[$e2,$e3,$e5,$e7];
        }

        // max exponents per position
        $maxPerPos = [3,2,1,1];

        $n = strlen($num);

        // helper: can achieve with given current exp and remaining slots
        $canAchieve = function($curExp, $rem) use ($req,$maxPerPos) {
            for ($i=0;$i<4;$i++) {
                if ($req[$i] > $curExp[$i] + $rem * $maxPerPos[$i]) return false;
            }
            return true;
        };

        // check if original num already valid
        $hasZero = false;
        $origExp = [0,0,0,0];
        for ($i=0;$i<$n;$i++) {
            $d = intval($num[$i]);
            if ($d==0) {$hasZero=true; break;}
            $e = $digitExp[$d];
            for ($j=0;$j<4;$j++) $origExp[$j]+=$e[$j];
        }
        if (!$hasZero) {
            $ok = true;
            for ($i=0;$i<4;$i++) if ($origExp[$i] < $req[$i]) {$ok=false;break;}
            if ($ok) return $num;
        }

        // prefix exponents and zero flag
        $prefixExp = array_fill(0,$n+1,[0,0,0,0]);
        $zeroPrefix = array_fill(0,$n+1,false);
        $cur = [0,0,0,0];
        $hasZeroSoFar = false;
        for ($i=0;$i<$n;$i++) {
            $d = intval($num[$i]);
            if ($d==0) $hasZeroSoFar = true;
            else {
                $e = $digitExp[$d];
                for ($j=0;$j<4;$j++) $cur[$j]+=$e[$j];
            }
            $prefixExp[$i+1]=$cur;
            $zeroPrefix[$i+1]=$hasZeroSoFar;
        }

        // attempt same length by increasing a position
        for ($i=$n-1;$i>=0;$i--) {
            if ($zeroPrefix[$i]) continue; // prefix contains zero, cannot keep it
            $curExp = $prefixExp[$i];
            $startDigit = intval($num[$i]) + 1;
            if ($startDigit < 1) $startDigit = 1;
            for ($d=$startDigit;$d<=9;$d++) {
                if ($d==0) continue;
                $newExp = $curExp;
                $e = $digitExp[$d];
                for ($j=0;$j<4;$j++) $newExp[$j]+=$e[$j];
                $rem = $n - $i - 1;
                if (!$canAchieve($newExp,$rem)) continue;

                // build answer
                $prefixStr = substr($num,0,$i);
                $ans = $prefixStr . strval($d);
                // needed remaining exponents
                $need = [];
                for ($j=0;$j<4;$j++) {
                    $need[$j] = max(0, $req[$j] - $newExp[$j]);
                }
                // construct suffix greedily
                $suffix = '';
                for ($pos=0;$pos<$rem;$pos++) {
                    for ($cand=1;$cand<=9;$cand++) {
                        $eCand = $digitExp[$cand];
                        $needAfter = [];
                        $possible = true;
                        for ($j=0;$j<4;$j++) {
                            $needAfter[$j] = max(0, $need[$j] - $eCand[$j]);
                            if ($needAfter[$j] > ($rem-$pos-1) * $maxPerPos[$j]) { $possible=false; break; }
                        }
                        if ($possible) {
                            $suffix .= strval($cand);
                            $need = $needAfter;
                            break;
                        }
                    }
                }
                return $ans . $suffix;
            }
        }

        // try longer lengths
        $minExtra = 0;
        // minimal length needed based on max per position (rough upper bound)
        $estLen = 0;
        for ($j=0;$j<4;$j++) {
            $need = $req[$j];
            if ($maxPerPos[$j]>0) {
                $estLen = max($estLen, intdiv($need + $maxPerPos[$j] - 1, $maxPerPos[$j]));
            }
        }
        $startLen = max($n+1, $estLen);
        $limitLen = $startLen + 200; // safe bound

        for ($L=$startLen;$L<=$limitLen;$L++) {
            $curExp = [0,0,0,0];
            $ans = '';
            $possibleOverall = true;
            for ($pos=0;$pos<$L;$pos++) {
                $found = false;
                for ($d=1;$d<=9;$d++) {
                    $e = $digitExp[$d];
                    $newExp = $curExp;
                    for ($j=0;$j<4;$j++) $newExp[$j]+=$e[$j];
                    $remSlots = $L - $pos - 1;
                    if ($canAchieve($newExp,$remSlots)) {
                        $ans .= strval($d);
                        $curExp = $newExp;
                        $found = true;
                        break;
                    }
                }
                if (!$found) { $possibleOverall=false; break; }
            }
            if ($possibleOverall) return $ans;
        }

        return "-1";
    }
}
```

## Swift

```swift
class Solution {
    func smallestNumber(_ num: String, _ t: Int) -> String {
        // Factorize t into 2,3,5,7 only
        var need = [0,0,0,0] // exponents for 2,3,5,7
        var temp = t
        let primes = [2,3,5,7]
        for (i,p) in primes.enumerated() {
            while temp % p == 0 {
                need[i] += 1
                temp /= p
            }
        }
        if temp != 1 { return "-1" } // other prime factor
        
        let maxE2 = need[0]
        let maxE3 = need[1]
        let maxE5 = need[2]
        let maxE7 = need[3]
        
        // digit exponent contributions
        var dExp = Array(repeating: (0,0,0,0), count: 10)
        func add(_ d:Int,_ a:Int,_ b:Int,_ c:Int,_ d7:Int){
            dExp[d] = (a,b,c,d7)
        }
        add(1,0,0,0,0)
        add(2,1,0,0,0)
        add(3,0,1,0,0)
        add(4,2,0,0,0)
        add(5,0,0,1,0)
        add(6,1,1,0,0)
        add(7,0,0,0,1)
        add(8,3,0,0,0)
        add(9,0,2,0,0)
        
        // DP over exponent states to get minimal sorted multiset string
        let strideE7 = 1
        let strideE5 = (maxE7 + 1) * strideE7
        let strideE3 = (maxE5 + 1) * strideE5
        let strideE2 = (maxE3 + 1) * strideE3
        let totalStates = (maxE2 + 1) * strideE2
        
        var dp = Array<String?>(repeating: nil, count: totalStates)
        func encode(_ e2:Int,_ e3:Int,_ e5:Int,_ e7:Int) -> Int {
            return ((e2 * strideE2) + (e3 * strideE3) + (e5 * strideE5) + e7)
        }
        dp[0] = ""
        var queue = [Int]()
        queue.append(0)
        var head = 0
        
        func insertSorted(_ s:String,_ ch:Character) -> String {
            var inserted = false
            var res = ""
            for c in s {
                if !inserted && ch < c {
                    res.append(ch)
                    inserted = true
                }
                res.append(c)
            }
            if !inserted { res.append(ch) }
            return res
        }
        
        while head < queue.count {
            let state = queue[head]; head += 1
            guard let curStr = dp[state] else { continue }
            // decode
            var rem = state
            let e7 = rem % (maxE7 + 1); rem /= (maxE7 + 1)
            let e5 = rem % (maxE5 + 1); rem /= (maxE5 + 1)
            let e3 = rem % (maxE3 + 1); rem /= (maxE3 + 1)
            let e2 = rem
            for d in 2...9 {
                let exp = dExp[d]
                var ne2 = e2 + exp.0; if ne2 > maxE2 { ne2 = maxE2 }
                var ne3 = e3 + exp.1; if ne3 > maxE3 { ne3 = maxE3 }
                var ne5 = e5 + exp.2; if ne5 > maxE5 { ne5 = maxE5 }
                var ne7 = e7 + exp.3; if ne7 > maxE7 { ne7 = maxE7 }
                let ns = encode(ne2, ne3, ne5, ne7)
                let newStr = insertSorted(curStr, Character(String(d)))
                if let existing = dp[ns] {
                    if newStr.count < existing.count || (newStr.count == existing.count && newStr < existing) {
                        dp[ns] = newStr
                        queue.append(ns)
                    }
                } else {
                    dp[ns] = newStr
                    queue.append(ns)
                }
            }
        }
        
        // Helper to get minimal suffix for needed exponents
        func minSuffix(_ need2:Int,_ need3:Int,_ need5:Int,_ need7:Int) -> String? {
            let e2 = min(need2, maxE2)
            let e3 = min(need3, maxE3)
            let e5 = min(need5, maxE5)
            let e7 = min(need7, maxE7)
            return dp[encode(e2,e3,e5,e7)]
        }
        
        // Prefix exponent sums and zero detection
        let n = num.count
        var prefE2 = Array(repeating: 0, count: n+1)
        var prefE3 = Array(repeating: 0, count: n+1)
        var prefE5 = Array(repeating: 0, count: n+1)
        var prefE7 = Array(repeating: 0, count: n+1)
        var zeroPrefix = Array(repeating: false, count: n+1) // true if any zero in first i chars
        let digitsArray = Array(num)
        for i in 0..<n {
            let ch = digitsArray[i]
            let d = Int(ch.unicodeScalars.first!.value - 48)
            zeroPrefix[i+1] = zeroPrefix[i] || (d == 0)
            prefE2[i+1] = prefE2[i]
            prefE3[i+1] = prefE3[i]
            prefE5[i+1] = prefE5[i]
            prefE7[i+1] = prefE7[i]
            if d != 0 {
                let exp = dExp[d]
                prefE2[i+1] += exp.0
                prefE3[i+1] += exp.1
                prefE5[i+1] += exp.2
                prefE7[i+1] += exp.3
            }
        }
        
        // Check if original number already valid (zero-free and product divisible)
        if !zeroPrefix[n] {
            let curNeed2 = max(0, need[0] - prefE2[n])
            let curNeed3 = max(0, need[1] - prefE3[n])
            let curNeed5 = max(0, need[2] - prefE5[n])
            let curNeed7 = max(0, need[3] - prefE7[n])
            if curNeed2 == 0 && curNeed3 == 0 && curNeed5 == 0 && curNeed7 == 0 {
                return num
            }
        }
        
        // Try to modify at position i
        for i in stride(from: n-1, through: 0, by: -1) {
            if zeroPrefix[i] { continue } // prefix contains zero -> cannot keep unchanged
            let origDigit = Int(digitsArray[i].unicodeScalars.first!.value - 48)
            for d in (origDigit+1)...9 {
                if d == 0 { continue }
                let exp = dExp[d]
                let ne2 = prefE2[i] + exp.0
                let ne3 = prefE3[i] + exp.1
                let ne5 = prefE5[i] + exp.2
                let ne7 = prefE7[i] + exp.3
                var need2 = need[0] - ne2; if need2 < 0 { need2 = 0 }
                var need3 = need[1] - ne3; if need3 < 0 { need3 = 0 }
                var need5 = need[2] - ne5; if need5 < 0 { need5 = 0 }
                var need7 = need[3] - ne7; if need7 < 0 { need7 = 0 }
                let remaining = n - i - 1
                if need2 > 3*remaining || need3 > 2*remaining || need5 > remaining || need7 > remaining {
                    continue
                }
                guard let suffix = minSuffix(need2, need3, need5, need7) else { continue }
                if suffix.count > remaining { continue }
                // Build result
                var res = ""
                if i > 0 { res += String(num.prefix(i)) }
                res.append(Character(String(d)))
                let onesCount = remaining - suffix.count
                if onesCount > 0 {
                    res += String(repeating: "1", count: onesCount)
                }
                res += suffix
                return res
            }
        }
        
        // Need longer length
        guard let fullSuffix = minSuffix(need[0], need[1], need[2], need[3]) else { return "-1" }
        let m = fullSuffix.count
        let L = max(m, n + 1)
        var result = ""
        if L > m {
            result += String(repeating: "1", count: L - m)
        }
        result += fullSuffix
        return result
    }
}
```

## Kotlin

```kotlin
import java.util.*

class Solution {
    private val contrib = Array(10) { intArrayOf(0, 0, 0, 0) }
    init {
        // digit contributions for primes 2,3,5,7
        val map = arrayOf(
            intArrayOf(0, 0, 0, 0), //0 not used
            intArrayOf(0, 0, 0, 0), //1
            intArrayOf(1, 0, 0, 0), //2
            intArrayOf(0, 1, 0, 0), //3
            intArrayOf(2, 0, 0, 0), //4
            intArrayOf(0, 0, 1, 0), //5
            intArrayOf(1, 1, 0, 0), //6
            intArrayOf(0, 0, 0, 1), //7
            intArrayOf(3, 0, 0, 0), //8
            intArrayOf(0, 2, 0, 0)  //9
        )
        for (d in 1..9) {
            contrib[d] = map[d]
        }
    }

    private fun feasible(need: IntArray, len: Int): Boolean {
        if (need[0] > 3 * len) return false
        if (need[1] > 2 * len) return false
        if (need[2] > len) return false
        if (need[3] > len) return false
        return true
    }

    private fun buildMin(len: Int, req: IntArray): String? {
        val ans = CharArray(len)
        var need = req.clone()
        for (i in 0 until len) {
            var placed = false
            for (d in 1..9) {
                val n2 = intArrayOf(
                    kotlin.math.max(0, need[0] - contrib[d][0]),
                    kotlin.math.max(0, need[1] - contrib[d][1]),
                    kotlin.math.max(0, need[2] - contrib[d][2]),
                    kotlin.math.max(0, need[3] - contrib[d][3])
                )
                if (feasible(n2, len - i - 1)) {
                    ans[i] = ('0'.code + d).toChar()
                    need = n2
                    placed = true
                    break
                }
            }
            if (!placed) return null
        }
        return String(ans)
    }

    private fun attemptSameLength(num: String, req: IntArray): String? {
        val L = num.length
        val ans = CharArray(L)
        val nextDigit = IntArray(L)

        // backtrack stacks
        val stackPos = IntArray(L)
        val stackTight = BooleanArray(L)
        val stackNext = IntArray(L)
        val stackNeed = Array(L) { IntArray(4) }
        var sp = 0

        var pos = 0
        var tight = true
        var need = req.clone()
        nextDigit[0] = if (tight) num[0] - '0' else 1

        while (true) {
            if (pos == L) return String(ans)

            var d = nextDigit[pos]
            var found = false
            val bound = if (tight) num[pos] - '0' else -1
            while (d <= 9) {
                if (d == 0) {
                    d++
                    continue
                }
                val n2 = intArrayOf(
                    kotlin.math.max(0, need[0] - contrib[d][0]),
                    kotlin.math.max(0, need[1] - contrib[d][1]),
                    kotlin.math.max(0, need[2] - contrib[d][2]),
                    kotlin.math.max(0, need[3] - contrib[d][3])
                )
                if (feasible(n2, L - pos - 1)) {
                    // choose d
                    ans[pos] = ('0'.code + d).toChar()
                    // push state for backtrack
                    stackPos[sp] = pos
                    stackTight[sp] = tight
                    stackNeed[sp] = need.clone()
                    stackNext[sp] = d + 1
                    sp++

                    need = n2
                    tight = tight && (d == bound)
                    pos++
                    if (pos < L) {
                        nextDigit[pos] = if (tight) num[pos] - '0' else 1
                    }
                    found = true
                    break
                }
                d++
            }

            if (!found) {
                // backtrack
                if (sp == 0) return null
                sp--
                pos = stackPos[sp]
                tight = stackTight[sp]
                need = stackNeed[sp]
                nextDigit[pos] = stackNext[sp]
            }
        }
    }

    fun smallestNumber(num: String, t: Long): String {
        var temp = t
        val primes = intArrayOf(2, 3, 5, 7)
        val req = IntArray(4)
        for (i in 0..3) {
            val p = primes[i]
            while (temp % p == 0L) {
                req[i]++
                temp /= p
            }
        }
        if (temp != 1L) return "-1"

        // minimal length needed based on exponents
        var minLenNeeded = 0
        if (req[0] > 0) minLenNeeded = kotlin.math.max(minLenNeeded, (req[0] + 2) / 3)
        if (req[1] > 0) minLenNeeded = kotlin.math.max(minLenNeeded, (req[1] + 1) / 2)
        minLenNeeded = kotlin.math.max(minLenNeeded, req[2])
        minLenNeeded = kotlin.math.max(minLenNeeded, req[3])

        if (num.length < minLenNeeded) {
            val res = buildMin(minLenNeeded, req)
            return res ?: "-1"
        }

        // try same length
        val same = attemptSameLength(num, req)
        if (same != null) return same

        // need longer length
        val newLen = kotlin.math.max(num.length + 1, minLenNeeded)
        val res = buildMin(newLen, req)
        return res ?: "-1"
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  String smallestNumber(String num, int t) {
    // factorize t into primes 2,3,5,7
    List<int> target = [0, 0, 0, 0]; // exponents for 2,3,5,7
    int tmp = t;
    const primes = [2, 3, 5, 7];
    for (int i = 0; i < 4; i++) {
      while (tmp % primes[i] == 0) {
        target[i]++;
        tmp ~/= primes[i];
      }
    }
    if (tmp != 1) return "-1";

    // digit exponent contributions
    List<List<int>> dExp = List.generate(10, (_) => List.filled(4, 0));
    for (int d = 2; d <= 9; d++) {
      int x = d;
      for (int i = 0; i < 4; i++) {
        while (x % primes[i] == 0) {
          dExp[d][i]++;
          x ~/= primes[i];
        }
      }
    }

    // DP: minimal count of non‑1 digits to achieve at least needed exponents
    int A = target[0], B = target[1], C = target[2], D = target[3];
    int sizeA = A + 1, sizeB = B + 1, sizeC = C + 1, sizeD = D + 1;
    int total = sizeA * sizeB * sizeC * sizeD;
    const INF = 1 << 30;
    List<int> dp = List.filled(total, INF);
    int idx(int a, int b, int c, int d) => ((a * sizeB + b) * sizeC + c) * sizeD + d;
    dp[0] = 0;

    for (int a = 0; a <= A; a++) {
      for (int b = 0; b <= B; b++) {
        for (int c = 0; c <= C; c++) {
          for (int d = 0; d <= D; d++) {
            int cur = dp[idx(a, b, c, d)];
            if (cur == INF) continue;
            for (int digit = 2; digit <= 9; digit++) {
              int na = a + dExp[digit][0];
              if (na > A) na = A;
              int nb = b + dExp[digit][1];
              if (nb > B) nb = B;
              int nc = c + dExp[digit][2];
              if (nc > C) nc = C;
              int nd = d + dExp[digit][3];
              if (nd > D) nd = D;
              int id2 = idx(na, nb, nc, nd);
              if (dp[id2] > cur + 1) dp[id2] = cur + 1;
            }
          }
        }
      }
    }

    int needDigits(List<int> need) => dp[idx(need[0], need[1], need[2], need[3])];

    // helper to attempt building number of length L
    String? tryBuild(int L, bool startTight) {
      List<int> need = target.toList();
      StringBuffer sb = StringBuffer();
      bool tight = startTight;
      for (int i = 0; i < L; i++) {
        int startDigit = tight ? (num.codeUnitAt(i) - 48) : 1;
        if (startDigit < 1) startDigit = 1; // zeros are not allowed
        bool placed = false;
        for (int d = startDigit; d <= 9; d++) {
          int a = need[0] - dExp[d][0];
          if (a < 0) a = 0;
          int b = need[1] - dExp[d][1];
          if (b < 0) b = 0;
          int c = need[2] - dExp[d][2];
          if (c < 0) c = 0;
          int e = need[3] - dExp[d][3];
          if (e < 0) e = 0;
          int rem = L - i - 1;
          if (dp[idx(a, b, c, e)] <= rem) {
            sb.writeCharCode(d + 48);
            need[0] = a;
            need[1] = b;
            need[2] = c;
            need[3] = e;
            if (tight && d != (num.codeUnitAt(i) - 48)) tight = false;
            placed = true;
            break;
          }
        }
        if (!placed) return null;
      }
      // all requirements satisfied automatically by feasibility checks
      return sb.toString();
    }

    int n = num.length;
    int minNeededDigits = needDigits(target);
    int maxLen = max(n, minNeededDigits) + 20; // safe upper bound

    for (int L = n; L <= maxLen; L++) {
      String? res;
      if (L == n) {
        res = tryBuild(L, true);
      } else {
        res = tryBuild(L, false);
      }
      if (res != null) return res;
    }
    return "-1";
  }
}
```

## Golang

```go
package main

func smallestNumber(num string, t int64) string {
	// prime factors limited to 2,3,5,7
	primes := []int{2, 3, 5, 7}
	var req [4]int
	tmp := t
	for i, p := range primes {
		for tmp%int64(p) == 0 {
			req[i]++
			tmp /= int64(p)
		}
	}
	if tmp != 1 {
		return "-1"
	}

	// digit contributions for primes 2,3,5,7
	var cnt [10][4]int
	factors := [][]int{
		{},               //0 unused
		{},               //1
		{1, 0, 0, 0},     //2 = 2^1
		{0, 1, 0, 0},     //3 = 3^1
		{2, 0, 0, 0},     //4 = 2^2
		{0, 0, 1, 0},     //5 = 5^1
		{1, 1, 0, 0},     //6 = 2*3
		{0, 0, 0, 1},     //7 = 7^1
		{3, 0, 0, 0},     //8 = 2^3
		{0, 2, 0, 0},     //9 = 3^2
	}
	for d := 1; d <= 9; d++ {
		for i := 0; i < 4; i++ {
			cnt[d][i] = factors[d][i]
		}
	}

	maxExp := [4]int{3, 2, 1, 1} // per digit max for 2,3,5,7

	satisfies := func(cur [4]int) bool {
		for i := 0; i < 4; i++ {
			if cur[i] < req[i] {
				return false
			}
		}
		return true
	}

	canSatisfy := func(cur [4]int, rem int) bool {
		for i := 0; i < 4; i++ {
			if cur[i]+rem*maxExp[i] < req[i] {
				return false
			}
		}
		return true
	}

	buildSuffix := func(rem int, cur [4]int) string {
		ans := make([]byte, rem)
		for pos := 0; pos < rem; pos++ {
			for d := 1; d <= 9; d++ {
				var nxt [4]int
				copy(nxt[:], cur[:])
				for k := 0; k < 4; k++ {
					nxt[k] += cnt[d][k]
				}
				if canSatisfy(nxt, rem-pos-1) {
					ans[pos] = byte('0' + d)
					cur = nxt
					break
				}
			}
		}
		return string(ans)
	}

	// check if original number itself works (must be zero‑free)
	zeroFree := true
	var curOrig [4]int
	for _, ch := range num {
		d := int(ch - '0')
		if d == 0 {
			zeroFree = false
			break
		}
		for k := 0; k < 4; k++ {
			curOrig[k] += cnt[d][k]
		}
	}
	if zeroFree && satisfies(curOrig) {
		return num
	}

	n := len(num)

	// prefix contributions and zero‑presence flag
	pref := make([][4]int, n+1)
	zeroPref := make([]bool, n+1)
	for i := 0; i < n; i++ {
		d := int(num[i] - '0')
		copy(pref[i+1][:], pref[i][:])
		if d == 0 {
			zeroPref[i+1] = true
		} else {
			for k := 0; k < 4; k++ {
				pref[i+1][k] = pref[i][k] + cnt[d][k]
			}
			zeroPref[i+1] = zeroPref[i]
		}
	}

	// try to increase at some position
	for i := n - 1; i >= 0; i-- {
		if zeroPref[i] { // prefix contains a zero, cannot keep it unchanged
			continue
		}
		curPref := pref[i]
		origDigit := int(num[i] - '0')
		start := origDigit + 1
		for d := start; d <= 9; d++ {
			if d == 0 {
				continue
			}
			var curNow [4]int
			copy(curNow[:], curPref[:])
			for k := 0; k < 4; k++ {
				curNow[k] += cnt[d][k]
			}
			rem := n - i - 1
			if canSatisfy(curNow, rem) {
				ans := make([]byte, n)
				copy(ans[:i], []byte(num[:i]))
				ans[i] = byte('0' + d)
				suffix := buildSuffix(rem, curNow)
				return string(append(ans[:i+1], []byte(suffix)...))
			}
		}
	}

	// need a longer length
	minLenNeeded := 0
	need2 := (req[0] + maxExp[0] - 1) / maxExp[0]
	if need2 > minLenNeeded {
		minLenNeeded = need2
	}
	need3 := (req[1] + maxExp[1] - 1) / maxExp[1]
	if need3 > minLenNeeded {
		minLenNeeded = need3
	}
	if req[2] > minLenNeeded {
		minLenNeeded = req[2]
	}
	if req[3] > minLenNeeded {
		minLenNeeded = req[3]
	}

	startLen := n + 1
	if startLen < minLenNeeded {
		startLen = minLenNeeded
	}
	for L := startLen; ; L++ {
		if !canSatisfy([4]int{}, L) {
			continue
		}
		curNow := [4]int{}
		ans := make([]byte, L)
		ok := true
		for pos := 0; pos < L; pos++ {
			placed := false
			for d := 1; d <= 9; d++ {
				var nxt [4]int
				copy(nxt[:], curNow[:])
				for k := 0; k < 4; k++ {
					nxt[k] += cnt[d][k]
				}
				if canSatisfy(nxt, L-pos-1) {
					ans[pos] = byte('0' + d)
					curNow = nxt
					placed = true
					break
				}
			}
			if !placed {
				ok = false
				break
			}
		}
		if ok && satisfies(curNow) {
			return string(ans)
		}
	}
}
```

## Ruby

```ruby
def smallest_number(num, t)
  # prime exponents required from t (only 2,3,5,7 allowed)
  req = [0, 0, 0, 0] # [e2,e3,e5,e7]
  primes = [2, 3, 5, 7]
  primes.each_with_index do |p, idx|
    while t % p == 0
      req[idx] += 1
      t /= p
    end
  end
  return "-1" if t != 1 # contains other prime factors

  # exponent contribution of each digit (index 0..9)
  exp = Array.new(10) { [0, 0, 0, 0] }
  exp[2] = [1, 0, 0, 0]
  exp[3] = [0, 1, 0, 0]
  exp[4] = [2, 0, 0, 0]
  exp[5] = [0, 0, 1, 0]
  exp[6] = [1, 1, 0, 0]
  exp[7] = [0, 0, 0, 1]
  exp[8] = [3, 0, 0, 0]
  exp[9] = [0, 2, 0, 0]

  max_per = [3, 2, 1, 1] # max exponent per slot for 2,3,5,7

  n = num.length
  digits = num.bytes.map { |b| b - 48 }

  # cumulative exponents and validity of prefix (no zero)
  cum_e2 = Array.new(n + 1, 0)
  cum_e3 = Array.new(n + 1, 0)
  cum_e5 = Array.new(n + 1, 0)
  cum_e7 = Array.new(n + 1, 0)
  valid_prefix = Array.new(n + 1, true)

  (0...n).each do |i|
    d = digits[i]
    if d == 0
      valid_prefix[i + 1] = false
    else
      cum_e2[i + 1] = cum_e2[i] + exp[d][0]
      cum_e3[i + 1] = cum_e3[i] + exp[d][1]
      cum_e5[i + 1] = cum_e5[i] + exp[d][2]
      cum_e7[i + 1] = cum_e7[i] + exp[d][3]
    end
    valid_prefix[i + 1] &&= valid_prefix[i]
  end

  # helper to check feasibility with remaining slots
  feasible = lambda do |e2, e3, e5, e7, slots|
    e2 + slots * max_per[0] >= req[0] &&
      e3 + slots * max_per[1] >= req[1] &&
      e5 + slots * max_per[2] >= req[2] &&
      e7 + slots * max_per[3] >= req[3]
  end

  # build the minimal suffix given current exponents and length
  build_suffix = lambda do |slots, cur_e|
    e2, e3, e5, e7 = cur_e
    res = +''
    slots.times do |pos|
      placed = false
      (1..9).each do |dig|
        ne2 = e2 + exp[dig][0]
        ne3 = e3 + exp[dig][1]
        ne5 = e5 + exp[dig][2]
        ne7 = e7 + exp[dig][3]
        if feasible.call(ne2, ne3, ne5, ne7, slots - pos - 1)
          res << dig.to_s
          e2, e3, e5, e7 = ne2, ne3, ne5, ne7
          placed = true
          break
        end
      end
      return nil unless placed
    end
    # final check (should hold)
    if e2 >= req[0] && e3 >= req[1] && e5 >= req[2] && e7 >= req[3]
      res
    else
      nil
    end
  end

  # try to modify within same length
  (n - 1).downto(0) do |i|
    next unless valid_prefix[i] # prefix up to i-1 must be zero‑free
    orig = digits[i]
    start_digit = orig == 0 ? 1 : orig + 1
    (start_digit..9).each do |new_dig|
      e2 = cum_e2[i] + exp[new_dig][0]
      e3 = cum_e3[i] + exp[new_dig][1]
      e5 = cum_e5[i] + exp[new_dig][2]
      e7 = cum_e7[i] + exp[new_dig][3]
      slots = n - i - 1
      next unless feasible.call(e2, e3, e5, e7, slots)
      suffix = build_suffix.call(slots, [e2, e3, e5, e7])
      if suffix
        prefix_str = num[0...i]
        return prefix_str + new_dig.to_s + suffix
      end
    end
  end

  # try longer lengths (up to a safe bound)
  max_extra = 20
  ((n + 1)..(n + max_extra)).each do |len|
    slots = len
    next unless feasible.call(0, 0, 0, 0, slots)
    suffix = build_suffix.call(slots, [0, 0, 0, 0])
    return suffix if suffix
  end

  "-1"
end
```

## Scala

```scala
object Solution {
  import java.util.ArrayDeque
  def smallestNumber(num: String, tInput: Long): String = {
    var t = tInput
    var r2 = 0; while (t % 2 == 0) { r2 += 1; t /= 2 }
    var r3 = 0; while (t % 3 == 0) { r3 += 1; t /= 3 }
    var r5 = 0; while (t % 5 == 0) { r5 += 1; t /= 5 }
    var r7 = 0; while (t % 7 == 0) { r7 += 1; t /= 7 }
    if (t != 1) return "-1"

    // contributions for digits 0..9
    val contrib = Array.ofDim[Int](10,4)
    def add(d:Int, p2:Int,p3:Int,p5:Int,p7:Int): Unit = {
      contrib(d)(0)=p2; contrib(d)(1)=p3; contrib(d)(2)=p5; contrib(d)(3)=p7
    }
    add(0,0,0,0,0)
    add(1,0,0,0,0)
    add(2,1,0,0,0)
    add(3,0,1,0,0)
    add(4,2,0,0,0)
    add(5,0,0,1,0)
    add(6,1,1,0,0)
    add(7,0,0,0,1)
    add(8,3,0,0,0)
    add(9,0,2,0,0)

    val max2 = r2; val max3 = r3; val max5 = r5; val max7 = r7
    val dim2 = max2 + 1
    val dim3 = max3 + 1
    val dim5 = max5 + 1
    val dim7 = max7 + 1
    val totalSize = dim2 * dim3 * dim5 * dim7

    def encode(a:Int,b:Int,c:Int,d:Int): Int = {
      ((a*dim3 + b)*dim5 + c)*dim7 + d
    }
    // DP for minimal number of non‑1 digits needed to satisfy each requirement
    val INF = Int.MaxValue/4
    val dp = Array.fill[Int](totalSize)(INF)
    val q = new ArrayDeque[Int]()
    val startEnc = encode(0,0,0,0)
    dp(startEnc) = 0
    q.add(startEnc)

    while (!q.isEmpty) {
      val cur = q.poll()
      val a = (cur / (dim3*dim5*dim7))
      val rem1 = cur % (dim3*dim5*dim7)
      val b = rem1 / (dim5*dim7)
      val rem2 = rem1 % (dim5*dim7)
      val c = rem2 / dim7
      val d = rem2 % dim7
      val curDist = dp(cur)
      var digit = 2
      while (digit <= 9) {
        val na = math.min(max2, a + contrib(digit)(0))
        val nb = math.min(max3, b + contrib(digit)(1))
        val nc = math.min(max5, c + contrib(digit)(2))
        val nd = math.min(max7, d + contrib(digit)(3))
        val nxt = encode(na,nb,nc,nd)
        if (dp(nxt) > curDist + 1) {
          dp(nxt) = curDist + 1
          q.add(nxt)
        }
        digit += 1
      }
    }

    def minNeeded(req2:Int, req3:Int, req5:Int, req7:Int): Int = {
      val enc = encode(req2,req3,req5,req7)
      dp(enc)
    }

    def sub(req:Array[Int], d:Int): Array[Int] = {
      val res = new Array[Int](4)
      var i=0
      while(i<4){
        val need=req(i)
        val have=contrib(d)(i)
        res(i)=if (need>have) need-have else 0
        i+=1
      }
      res
    }

    def buildSuffix(len:Int, req:Array[Int]): String = {
      val sb = new StringBuilder
      var curReq = req.clone()
      var pos = 0
      while (pos < len) {
        var d = 1
        var placed = false
        while (d <= 9 && !placed) {
          val nr = sub(curReq, d)
          if (minNeeded(nr(0),nr(1),nr(2),nr(3)) <= len - pos - 1) {
            sb.append(('0' + d).toChar)
            curReq = nr
            placed = true
          }
          d += 1
        }
        pos += 1
      }
      sb.toString()
    }

    val n = num.length
    var curReq = Array(r2, r3, r5, r7)

    // attempt same length
    val prefix = new StringBuilder
    var i = 0
    while (i < n) {
      val orig = num.charAt(i) - '0'
      var kept = false
      if (orig != 0) {
        val reqKeep = sub(curReq, orig)
        if (minNeeded(reqKeep(0),reqKeep(1),reqKeep(2),reqKeep(3)) <= n - i - 1) {
          prefix.append(num.charAt(i))
          curReq = reqKeep
          kept = true
        }
      }
      if (kept) { i += 1; continue }

      // need to increase at this position
      val startDigit = if (orig == 0) 1 else orig + 1
      var d = startDigit
      var found = false
      while (d <= 9 && !found) {
        val reqNew = sub(curReq, d)
        if (minNeeded(reqNew(0),reqNew(1),reqNew(2),reqNew(3)) <= n - i - 1) {
          prefix.append(('0' + d).toChar)
          val suffix = buildSuffix(n - i - 1, reqNew)
          return prefix.toString + suffix
        }
        d += 1
      }
      // cannot fix at this position -> no solution of same length
      i = n // break outer
    }

    // all digits kept, check if requirement already satisfied
    if (minNeeded(curReq(0),curReq(1),curReq(2),curReq(3)) == 0) {
      return num
    }

    // need longer length
    val minDigits = dp(startEnc) // minimal non‑1 digits needed for full requirement
    var L = math.max(n + 1, minDigits)
    while (true) {
      if (minNeeded(r2,r3,r5,r7) <= L) {
        return buildSuffix(L, Array(r2,r3,r5,r7))
      }
      L += 1 // should never loop many times
    }
    "-1"
  }
}
```

## Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn smallest_number(num: String, t: i64) -> String {
        // factor t into 2,3,5,7
        let mut tt = t;
        let mut need = [0usize; 4]; // 2,3,5,7
        for (i, p) in [2i64, 3, 5, 7].iter().enumerate() {
            while tt % *p == 0 {
                need[i] += 1;
                tt /= *p;
            }
        }
        if tt != 1 {
            return "-1".to_string();
        }
        let (e2, e3, e5, e7) = (need[0], need[1], need[2], need[3]);

        // digit contributions for digits 2..9
        let mut contrib = vec![(0usize, 0usize, 0usize, 0usize); 10];
        for d in 2..=9 {
            let (a, b, c, d7) = match d {
                2 => (1, 0, 0, 0),
                3 => (0, 1, 0, 0),
                4 => (2, 0, 0, 0),
                5 => (0, 0, 1, 0),
                6 => (1, 1, 0, 0),
                7 => (0, 0, 0, 1),
                8 => (3, 0, 0, 0),
                9 => (0, 2, 0, 0),
                _ => (0, 0, 0, 0),
            };
            contrib[d] = (a, b, c, d7);
        }

        // dimensions for state encoding
        let dim2 = e2 + 1;
        let dim3 = e3 + 1;
        let dim5 = e5 + 1;
        let dim7 = e7 + 1;
        let total_states = dim2 * dim3 * dim5 * dim7;

        // encode/decode helpers
        let encode = |a: usize, b: usize, c: usize, d: usize| -> usize {
            ((a * dim3 + b) * dim5 + c) * dim7 + d
        };

        // BFS to compute minimal number of non‑1 digits for each state
        let mut dist = vec![usize::MAX; total_states];
        let mut parent_digit = vec![0u8; total_states];
        let mut parent_state = vec![usize::MAX; total_states];

        let start_idx = encode(0, 0, 0, 0);
        dist[start_idx] = 0;
        let mut q = VecDeque::new();
        q.push_back(start_idx);

        while let Some(idx) = q.pop_front() {
            // decode
            let mut rem = idx;
            let d7_cur = rem % dim7; rem /= dim7;
            let c5_cur = rem % dim5; rem /= dim5;
            let b3_cur = rem % dim3; rem /= dim3;
            let a2_cur = rem;

            for digit in 2..=9 {
                let (da, db, dc, dd) = contrib[digit];
                let na = std::cmp::min(a2_cur + da, e2);
                let nb = std::cmp::min(b3_cur + db, e3);
                let nc = std::cmp::min(c5_cur + dc, e5);
                let nd = std::cmp::min(d7_cur + dd, e7);
                let nidx = encode(na, nb, nc, nd);
                if dist[nidx] == usize::MAX {
                    dist[nidx] = dist[idx] + 1;
                    parent_digit[nidx] = digit as u8;
                    parent_state[nidx] = idx;
                    q.push_back(nidx);
                }
            }
        }

        let target_idx = encode(e2, e3, e5, e7);
        if dist[target_idx] == usize::MAX {
            return "-1".to_string();
        }

        // Try to build answer with the same length as num
        let n = num.len();
        let bytes = num.as_bytes();
        let mut ans = String::with_capacity(n);
        let (mut cur2, mut cur3, mut cur5, mut cur7) = (0usize, 0usize, 0usize, 0usize);
        let mut prefix_equal = true;
        let mut possible_same_len = true;

        for i in 0..n {
            let orig_digit = (bytes[i] - b'0') as usize;
            let start_d = if prefix_equal { orig_digit } else { 1 };
            let mut chosen: Option<usize> = None;

            for d in start_d..=9 {
                if d == 0 {
                    continue;
                }
                let (da, db, dc, dd) = contrib[d];
                let na = std::cmp::min(cur2 + da, e2);
                let nb = std::cmp::min(cur3 + db, e3);
                let nc = std::cmp::min(cur5 + dc, e5);
                let nd = std::cmp::min(cur7 + dd, e7);

                // remaining needed exponents
                let re2 = if e2 > na { e2 - na } else { 0 };
                let re3 = if e3 > nb { e3 - nb } else { 0 };
                let re5 = if e5 > nc { e5 - nc } else { 0 };
                let re7 = if e7 > nd { e7 - nd } else { 0 };
                let deficit_idx = encode(re2, re3, re5, re7);
                let needed = dist[deficit_idx];
                if needed != usize::MAX && needed <= n - i - 1 {
                    chosen = Some(d);
                    cur2 = na;
                    cur3 = nb;
                    cur5 = nc;
                    cur7 = nd;
                    prefix_equal = prefix_equal && (d == orig_digit);
                    break;
                }
            }

            if let Some(d) = chosen {
                ans.push((b'0' + d as u8) as char);
            } else {
                possible_same_len = false;
                break;
            }
        }

        if possible_same_len {
            return ans;
        }

        // Need a longer length
        let k = dist[target_idx]; // minimal count of non‑1 digits
        let mut L = std::cmp::max(n + 1, k);
        // reconstruct one optimal multiset for the target state
        let mut mult: Vec<u8> = Vec::with_capacity(k);
        let mut cur_idx = target_idx;
        while cur_idx != start_idx {
            let d = parent_digit[cur_idx];
            mult.push(d);
            cur_idx = parent_state[cur_idx];
        }
        mult.sort();

        let mut result = String::with_capacity(L);
        for _ in 0..(L - k) {
            result.push('1');
        }
        for d in mult {
            result.push((b'0' + d) as char);
        }
        result
    }
}
```

## Racket

```racket
(define (smallest-number num t)
  (define max-exp '(3 2 1 1)) ; per digit max exponents for 2,3,5,7
  ;; factor t into counts of 2,3,5,7; return #f if other prime factors exist
  (define (factor-t x)
    (let ((cnts (make-vector 4 0)))
      (let loop ((y x))
        (cond [(= y 1) cnts]
              [(zero? (remainder y 2))
               (vector-set! cnts 0 (+ 1 (vector-ref cnts 0)))
               (loop (/ y 2))]
              [(zero? (remainder y 3))
               (vector-set! cnts 1 (+ 1 (vector-ref cnts 1)))
               (loop (/ y 3))]
              [(zero? (remainder y 5))
               (vector-set! cnts 2 (+ 1 (vector-ref cnts 2)))
               (loop (/ y 5))]
              [(zero? (remainder y 7))
               (vector-set! cnts 3 (+ 1 (vector-ref cnts 3)))
               (loop (/ y 7))]
              [else #f]))))
  ;; digit exponent vectors for digits 0..9
  (define digit-exp
    (let ((v (make-vector 10)))
      (for ([d (in-range 10)])
        (vector-set! v d (make-vector 4 0)))
      (define (setexp d e2 e3 e5 e7)
        (let ((vec (make-vector 4 0)))
          (vector-set! vec 0 e2)
          (vector-set! vec 1 e3)
          (vector-set! vec 2 e5)
          (vector-set! vec 3 e7)
          (vector-set! v d vec)))
      (setexp 1 0 0 0 0)
      (setexp 2 1 0 0 0)
      (setexp 3 0 1 0 0)
      (setexp 4 2 0 0 0)
      (setexp 5 0 0 1 0)
      (setexp 6 1 1 0 0)
      (setexp 7 0 0 0 1)
      (setexp 8 3 0 0 0)
      (setexp 9 0 2 0 0)
      v))
  ;; convert string to vector of digits
  (define (str->digits s)
    (let* ((len (string-length s))
           (vec (make-vector len)))
      (for ([i (in-range len)])
        (vector-set! vec i (- (char->integer (string-ref s i)) 48)))
      vec))
  ;; feasibility check for remaining positions
  (define (feasible? rem need)
    (let loop ((i 0))
      (if (= i 4) #t
          (and (<= (list-ref need i) (* rem (list-ref max-exp i)))
               (loop (+ i 1))))))
  ;; build candidate of length L with lower bound digits lb (vector)
  (define (build L lb req)
    (let* ((chosen (make-vector L 0))
           (nextdig (make-vector L -1))
           (eqpref (make-vector (+ L 1) #f))
           (cur (make-vector 4 0)))
      (vector-set! eqpref 0 #t)
      (let loop ((pos 0))
        (cond [(= pos L)
               ;; success, construct string
               (let ((out (make-string L)))
                 (for ([i (in-range L)])
                   (string-set! out i (integer->char (+ 48 (vector-ref chosen i)))))
                 out)]
              [else
               (define start
                 (if (vector-ref eqpref pos)
                     (max 1 (vector-ref lb pos))
                     1))
               (define nd (+ 1 (vector-ref nextdig pos)))
               (define cand (if (< nd start) start nd))
               (let try ((d cand) (found #f))
                 (cond [(> d 9)
                        ;; backtrack
                        (when (> pos 0)
                          (vector-set! nextdig pos -1)
                          (define prevd (vector-ref chosen (- pos 1)))
                          (let ((expvec (vector-ref digit-exp prevd)))
                            (for ([i (in-range 4)])
                              (vector-set! cur i (- (vector-ref cur i) (vector-ref expvec i)))))
                          (loop (- pos 1)))]
                       [else
                        (define expvec (vector-ref digit-exp d))
                        (define rem (- L pos 1))
                        ;; compute needed after picking d
                        (let ((ok #t))
                          (for ([i (in-range 4)])
                            (when ok
                              (define have (+ (vector-ref cur i) (vector-ref expvec i)))
                              (define need (- (vector-ref req i) have))
                              (when (< need 0) (set! need 0))
                              (when (> need (* rem (list-ref max-exp i))) (set! ok #f))))
                          (if ok
                              (begin
                                ;; accept d
                                (vector-set! chosen pos d)
                                (vector-set! nextdig pos d)
                                (for ([i (in-range 4)])
                                  (vector-set! cur i (+ (vector-ref cur i) (vector-ref expvec i))))
                                (define eqnext (and (vector-ref eqpref pos) (= d (vector-ref lb pos))))
                                (vector-set! eqpref (+ pos 1) eqnext)
                                (loop (+ pos 1)))
                              (try (+ d 1) #f)))])))))))
  ;; main logic
  (let ((req (factor-t t)))
    (if (not req) "-1"
        (let* ((num-digits (str->digits num))
               (n (vector-length num-digits))
               (sum-req (+ (vector-ref req 0)
                           (vector-ref req 1)
                           (vector-ref req 2)
                           (vector-ref req 3)))
               (minlen (max n
                            (max (ceiling (/ (vector-ref req 0) 3.0))
                                 (max (ceiling (/ (vector-ref req 1) 2.0))
                                      (max (vector-ref req 2) (vector-ref req 3))))))
               (maxlen (+ (max n minlen) sum-req 5)))
          (let loop ((L minlen))
            (if (> L maxlen)
                "-1"
                (let ((lb (if (= L n) num-digits
                              (let ((v (make-vector L 0)))
                                (for ([i (in-range L)]) (vector-set! v i 1))
                                v))))
                  (define res (build L lb req))
                  (if res
                      res
                      (loop (+ L 1)))))))))
```

## Erlang

```erlang
-module(solution).
-export([smallest_number/2]).

-define(MAX2, 3).
-define(MAX3, 2).
-define(MAX5, 1).
-define(MAX7, 1).

%% Public API
-spec smallest_number(Num :: unicode:unicode_binary(), T :: integer()) -> unicode:unicode_binary().
smallest_number(Num, T) ->
    Need = factor(T),
    Digits = [C - $0 || <<C>> <= Num],
    case find_answer(Num, Digits, Need) of
        {ok, Res} -> Res;
        not_found -> <<"-1">>
    end.

%% Factorization of t into exponents of 2,3,5,7
factor(N) ->
    {A, N1} = count_factor(N, 2, 0),
    {B, N2} = count_factor(N1, 3, 0),
    {C, N3} = count_factor(N2, 5, 0),
    {D, _ } = count_factor(N3, 7, 0),
    {A,B,C,D}.

count_factor(N, P, Acc) when N rem P =:= 0 ->
    count_factor(N div P, P, Acc + 1);
count_factor(N, _, Acc) -> {Acc, N}.

%% Main search
find_answer(NumBin, Digits, Need) ->
    Len = length(Digits),
    find_pos(0, Len, NumBin, Digits, Need, {0,0,0,0}).

find_pos(Index, Len, _NumBin, _Digits, _Need, _Cur) when Index > Len -> not_found;
find_pos(Index, Len, NumBin, Digits, Need, CurExps) ->
    Orig = if Index < Len -> lists:nth(Index + 1, Digits); true -> -1 end,
    case try_increase(Index, Orig, CurExps, Need, Len, NumBin) of
        {ok, Res} -> {ok, Res};
        not_found ->
            case Index == Len of
                true -> not_found;
                false ->
                    case Orig of
                        0 -> not_found; % cannot keep a zero digit
                        _ ->
                            NewCur = add_exps(CurExps, digit_exps(Orig)),
                            find_pos(Index + 1, Len, NumBin, Digits, Need, NewCur)
                    end
            end
    end.

%% Attempt to increase at position Index
try_increase(Index, Orig, CurExps, Need, Len, NumBin) ->
    Slots = if Index < Len -> Len - Index - 1; true -> 0 end,
    StartD = case Orig of
                -1 -> 1;
                0  -> 1;
                _  -> Orig + 1
            end,
    try_digit_loop(StartD, 9, Index, Slots, CurExps, Need, Len, NumBin).

try_digit_loop(D, Max, _Idx, _Slots, _Cur, _Need, _Len, _Num) when D > Max ->
    not_found;
try_digit_loop(D, Max, Idx, Slots, CurExps, Need, Len, NumBin) ->
    NewExps = add_exps(CurExps, digit_exps(D)),
    Deficit = deficit_subtract(Need, NewExps),
    case feasible(Deficit, Slots) of
        true ->
            {SuffixDigits, ok} = build_suffix(Deficit, Slots),
            case ok of
                true ->
                    PrefixBin = if Idx == 0 -> <<>>; true -> binary:part(NumBin, 0, Idx) end,
                    DigitChar = <<$0 + D>>,
                    OneCnt = Slots - length(SuffixDigits),
                    Ones = lists:duplicate(OneCnt, $1),
                    SufChars = [ $0 + X || X <- SuffixDigits ],
                    Res = iolist_to_binary([PrefixBin, DigitChar, Ones, SufChars]),
                    {ok, Res};
                false ->
                    try_digit_loop(D + 1, Max, Idx, Slots, CurExps, Need, Len, NumBin)
            end;
        false ->
            try_digit_loop(D + 1, Max, Idx, Slots, CurExps, Need, Len, NumBin)
    end.

%% Build minimal suffix (non‑'1' digits) satisfying deficit within given slots
build_suffix(Deficit, Slots) ->
    build_suffix_loop(Deficit, Slots, []).

build_suffix_loop(Def, _Slots, Acc) when all_zero(Def) ->
    {lists:sort(Acc), true};
build_suffix_loop(_Def, 0, _Acc) ->
    {[], false};
build_suffix_loop(Def, Slots, Acc) ->
    try_digit_for_suffix(2, Def, Slots, Acc).

try_digit_for_suffix(D, _Def, _Slots, _Acc) when D > 9 -> {[], false};
try_digit_for_suffix(D, Def, Slots, Acc) ->
    Contrib = digit_exps(D),
    NewDef = deficit_subtract(Def, Contrib),
    case feasible(NewDef, Slots - 1) of
        true ->
            build_suffix_loop(NewDef, Slots - 1, [D|Acc]);
        false ->
            try_digit_for_suffix(D + 1, Def, Slots, Acc)
    end.

%% Helpers
add_exps({A,B,C,D}, {E,F,G,H}) -> {A+E, B+F, C+G, D+H}.

deficit_subtract({A,B,C,D}, {E,F,G,H}) ->
    {max(A - E, 0), max(B - F, 0), max(C - G, 0), max(D - H, 0)}.

all_zero({A,B,C,D}) -> A =:= 0 andalso B =:= 0 andalso C =:= 0 andalso D =:= 0.

feasible({A,B,C,D}, Slots) ->
    A =< Slots * ?MAX2 andalso
    B =< Slots * ?MAX3 andalso
    C =< Slots * ?MAX5 andalso
    D =< Slots * ?MAX7.

digit_exps(0) -> {0,0,0,0};
digit_exps(1) -> {0,0,0,0};
digit_exps(2) -> {1,0,0,0};
digit_exps(3) -> {0,1,0,0};
digit_exps(4) -> {2,0,0,0};
digit_exps(5) -> {0,0,1,0};
digit_exps(6) -> {1,1,0,0};
digit_exps(7) -> {0,0,0,1};
digit_exps(8) -> {3,0,0,0};
digit_exps(9) -> {0,2,0,0}.
```

## Elixir

```elixir
defmodule Solution do
  @primes [2, 3, 5, 7]
  @max_per_digit %{2 => 3, 3 => 2, 5 => 1, 7 => 1}
  # precompute contributions for digits 0..9 as tuple {e2,e3,e5,e7}
  @contrib Tuple.from_list(
    Enum.map(0..9, fn d ->
      {c2, r} = count_factor(d, 2, 0)
      {c3, r} = count_factor(r, 3, c2)
      {c5, r} = count_factor(r, 5, c3)
      {c7, _r} = count_factor(r, 7, c5)
      {c2, c3, c5, c7}
    end)
  )

  @spec smallest_number(num :: String.t(), t :: integer) :: String.t()
  def smallest_number(num, t) do
    case factor_t(t) do
      :invalid ->
        "-1"

      need when is_tuple(need) ->
        digits = String.to_charlist(num) |> Enum.map(&(&1 - ?0))
        n = length(digits)

        case try_same_length(digits, need, n) do
          {:ok, ans} -> ans
          :none ->
            min_len_needed = minimal_length_needed(need)
            len = max(n + 1, min_len_needed)

            if can_fill(len, need) do
              fill_min(len, need) |> to_string()
            else
              "-1"
            end
        end
    end
  end

  # factor t into required exponents of 2,3,5,7; return :invalid if other primes exist
  defp factor_t(t) do
    {e2, r} = count_factor(t, 2, 0)
    {e3, r} = count_factor(r, 3, e2)
    {e5, r} = count_factor(r, 5, e3)
    {e7, r} = count_factor(r, 7, e5)

    if r != 1 do
      :invalid
    else
      {e2, e3, e5, e7}
    end
  end

  # count exponent of p in x, returning {count, remaining}
  defp count_factor(x, p, acc) when rem(x, p) == 0 do
    count_factor(div(x, p), p, acc + 1)
  end

  defp count_factor(x, _p, acc), do: {acc, x}

  # attempt to find answer with same length as original number
  defp try_same_length(digits, need, total_len) do
    do_try(digits, need, [], total_len)
  end

  defp do_try([], need, prefix_rev, _total_len) do
    if all_zero?(need) do
      {:ok,
       prefix_rev
       |> Enum.reverse()
       |> to_string()}
    else
      :none
    end
  end

  defp do_try([orig | rest], need, prefix_rev, remaining) do
    rem_len = remaining - 1
    inc_start = if orig == 0, do: 1, else: orig + 1

    case try_increase(inc_start, 9, need, prefix_rev, rem_len) do
      {:ok, ans} ->
        {:ok, ans}

      :none ->
        if orig == 0 do
          :none
        else
          new_need = sub_need(need, elem(@contrib, orig))
          do_try(rest, new_need, [orig | prefix_rev], rem_len)
        end
    end
  end

  # try to increase current digit to some d in [cur..max] that allows completion
  defp try_increase(cur, max, _need, _prefix_rev, _rem_len) when cur > max, do: :none

  defp try_increase(d, max, need, prefix_rev, rem_len) do
    new_need = sub_need(need, elem(@contrib, d))

    if can_fill(rem_len, new_need) do
      suffix = fill_min(rem_len, new_need)
      final_digits = Enum.reverse(prefix_rev) ++ [d] ++ suffix
      {:ok, to_string(final_digits)}
    else
      try_increase(d + 1, max, need, prefix_rev, rem_len)
    end
  end

  # construct minimal lexicographic number of given length satisfying need
  defp fill_min(len, need) do
    fill_iter(len, need, [])
  end

  defp fill_iter(0, _need, acc), do: Enum.reverse(acc)

  defp fill_iter(rem_len, need, acc) do
    d = find_digit(rem_len, need)
    new_need = sub_need(need, elem(@contrib, d))
    fill_iter(rem_len - 1, new_need, [d | acc])
  end

  # smallest digit that keeps possibility
  defp find_digit(rem_len, need) do
    Enum.find(1..9, fn d ->
      new_need = sub_need(need, elem(@contrib, d))
      can_fill(rem_len - 1, new_need)
    end)
  end

  # check if remaining length can satisfy needed exponents
  defp can_fill(len, {e2, e3, e5, e7}) do
    e2 <= len * @max_per_digit[2] and
      e3 <= len * @max_per_digit[3] and
      e5 <= len * @max_per_digit[5] and
      e7 <= len * @max_per_digit[7]
  end

  # subtract contributions, floor at zero
  defp sub_need({a, b, c, d}, {ea, eb, ec, ed}) do
    {
      max(a - ea, 0),
      max(b - eb, 0),
      max(c - ec, 0),
      max(d - ed, 0)
    }
  end

  defp all_zero?({a, b, c, d}), do: a == 0 and b == 0 and c == 0 and d == 0

  # minimal length needed to possibly satisfy need
  defp minimal_length_needed({e2, e3, e5, e7}) do
    ceil_div(e2, @max_per_digit[2])
    |> max(ceil_div(e3, @max_per_digit[3]))
    |> max(e5)
    |> max(e7)
  end

  defp ceil_div(a, b), do: div(a + b - 1, b)

  # convert list of digits to string
  defp to_string(digits) do
    digits
    |> Enum.map(&(&1 + ?0))
    |> List.to_string()
  end
end
```
