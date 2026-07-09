# 3395. Subsequences with a Unique Middle Mode I

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    static const int MOD = 1000000007;
    long long C2(long long x){
        if(x<2) return 0;
        return (x*(x-1)/2)%MOD;
    }
    long long C1(long long x){ return x%MOD; }
    long long C0(){ return 1; }
    
    int subsequencesWithMiddleMode(vector<int>& nums) {
        int n = nums.size();
        long long ans = 0;
        for(int i=0;i<n;++i){
            int mid = nums[i];
            unordered_map<int,int> lcnt, rcnt;
            int Lmid=0,Rmid=0;
            for(int j=0;j<i;++j){
                if(nums[j]==mid) ++Lmid;
                else ++lcnt[nums[j]];
            }
            for(int j=i+1;j<n;++j){
                if(nums[j]==mid) ++Rmid;
                else ++rcnt[nums[j]];
            }
            int Lnon = i - Lmid;
            int Rnon = (n-i-1) - Rmid;
            
            // precompute sums for distinct pairs
            long long sumC_l2=0, sumC_r2=0;
            for(auto &p:lcnt){
                long long c=p.second;
                sumC_l2 = (sumC_l2 + C2(c))%MOD;
            }
            for(auto &p:rcnt){
                long long c=p.second;
                sumC_r2 = (sumC_r2 + C2(c))%MOD;
            }
            long long diffL = (C2(Lnon) - sumC_l2)%MOD; if(diffL<0) diffL+=MOD;
            long long diffR = (C2(Rnon) - sumC_r2)%MOD; if(diffR<0) diffR+=MOD;
            
            // k=4
            if(Lmid>=2 && Rmid>=2){
                ans = (ans + C2(Lmid)*C2(Rmid))%MOD;
            }
            // k=3
            if(Lmid>=1 && Lnon>=1 && Rmid>=2){
                ans = (ans + C1(Lmid)*C1(Lnon)%MOD * C2(Rmid))%MOD;
            }
            if(Rmid>=1 && Rnon>=1 && Lmid>=2){
                ans = (ans + C1(Rmid)*C1(Rnon)%MOD * C2(Lmid))%MOD;
            }
            // k=2
            for(int a=0;a<=2;++a){
                int b=2-a;
                if(Lmid>=a && Lnon>=2-a && Rmid>=b && Rnon>=a){
                    long long ways = C1(Lmid)*C2(Lmid- (Lmid-a))%MOD; // placeholder not used
                    long long term = 1;
                    // compute combinations directly
                    auto comb = [&](int n,int k)->long long{
                        if(k<0||k>n) return 0LL;
                        if(k==0) return 1LL;
                        if(k==1) return C1(n);
                        if(k==2) return C2(n);
                        return 0LL;
                    };
                    term = comb(Lmid,a)*comb(Lnon,2-a)%MOD *
                           comb(Rmid,b)%MOD * comb(Rnon,a)%MOD;
                    ans = (ans + term)%MOD;
                }
            }
            // k=1 left extra mid
            if(Lmid>=1 && Lnon>=1 && Rnon>=2){
                long long sum = 0;
                for(auto &p:lcnt){
                    int v=p.first;
                    long long lc=p.second;
                    long long rv = rcnt.count(v)?rcnt[v]:0;
                    long long validR = (diffR - (rv * (long long)(Rnon - rv))%MOD)%MOD;
                    if(validR<0) validR+=MOD;
                    sum = (sum + lc%MOD * validR)%MOD;
                }
                ans = (ans + C1(Lmid)*sum)%MOD;
            }
            // k=1 right extra mid
            if(Rmid>=1 && Rnon>=1 && Lnon>=2){
                long long sum = 0;
                for(auto &p:rcnt){
                    int v=p.first;
                    long long rc=p.second;
                    long long lc = lcnt.count(v)?lcnt[v]:0;
                    long long validL = (diffL - (lc * (long long)(Lnon - lc))%MOD)%MOD;
                    if(validL<0) validL+=MOD;
                    sum = (sum + rc%MOD * validL)%MOD;
                }
                ans = (ans + C1(Rmid)*sum)%MOD;
            }
        }
        return (int)(ans%MOD);
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    private static long comb2(long x) {
        return x * (x - 1) / 2;
    }
    public int subsequencesWithMiddleMode(int[] nums) {
        int n = nums.length;
        // compress values
        java.util.HashMap<Integer, Integer> map = new java.util.HashMap<>();
        int idCnt = 0;
        int[] ids = new int[n];
        for (int i = 0; i < n; i++) {
            Integer v = map.get(nums[i]);
            if (v == null) {
                v = idCnt++;
                map.put(nums[i], v);
            }
            ids[i] = v;
        }
        int m = idCnt;
        int[][] pref = new int[m][n + 1];
        for (int i = 0; i < n; i++) {
            int cur = ids[i];
            for (int j = 0; j < m; j++) {
                pref[j][i + 1] = pref[j][i];
            }
            pref[cur][i + 1]++;
        }

        long answer = 0;
        for (int i = 0; i < n; i++) {
            int leftSize = i;
            int rightSize = n - i - 1;
            if (leftSize < 2 || rightSize < 2) continue;

            int vId = ids[i];
            long Lv = pref[vId][i];
            long Rv = pref[vId][n] - pref[vId][i + 1];

            long leftNonV = leftSize - Lv;
            long rightNonV = rightSize - Rv;

            // ways to pick pairs on each side
            long left0 = comb2(leftNonV);
            long left1 = Lv * leftNonV;
            long left2 = comb2(Lv);

            long right0 = comb2(rightNonV);
            long right1 = Rv * rightNonV;
            long right2 = comb2(Rv);

            long totalLeftPairs = comb2(leftSize);
            long totalRightPairs = comb2(rightSize);

            // case k >= 2
            long cntKge2 = (totalLeftPairs % MOD) * (totalRightPairs % MOD) % MOD;
            cntKge2 = (cntKge2 - (left0 % MOD) * (right0 % MOD) % MOD + MOD) % MOD;
            cntKge2 = (cntKge2 - (left1 % MOD) * (right0 % MOD) % MOD + MOD) % MOD;
            cntKge2 = (cntKge2 - (left0 % MOD) * (right1 % MOD) % MOD + MOD) % MOD;

            // distinct-value pairs on each side
            long sumSameRight = 0;
            for (int id = 0; id < m; id++) {
                if (id == vId) continue;
                long cnt = pref[id][n] - pref[id][i + 1];
                sumSameRight += comb2(cnt);
            }
            long totalDistinctRight = comb2(rightNonV) - sumSameRight;

            long sumSameLeft = 0;
            for (int id = 0; id < m; id++) {
                if (id == vId) continue;
                long cnt = pref[id][i];
                sumSameLeft += comb2(cnt);
            }
            long totalDistinctLeft = comb2(leftNonV) - sumSameLeft;

            // case a=1,b=0 with distinct non-v values
            long contribA1B0 = 0;
            for (int id = 0; id < m; id++) {
                if (id == vId) continue;
                long Lx = pref[id][i];
                if (Lx == 0) continue;
                long Rx = pref[id][n] - pref[id][i + 1];
                long term = totalDistinctRight - Rx * (rightNonV - Rx);
                term %= MOD;
                if (term < 0) term += MOD;
                contribA1B0 = (contribA1B0 + (Lx % MOD) * term) % MOD;
            }
            contribA1B0 = (contribA1B0 * (Lv % MOD)) % MOD;

            // case a=0,b=1 with distinct non-v values
            long contribA0B1 = 0;
            for (int id = 0; id < m; id++) {
                if (id == vId) continue;
                long Ry = pref[id][n] - pref[id][i + 1];
                if (Ry == 0) continue;
                long Ly = pref[id][i];
                long term = totalDistinctLeft - Ly * (leftNonV - Ly);
                term %= MOD;
                if (term < 0) term += MOD;
                contribA0B1 = (contribA0B1 + (Ry % MOD) * term) % MOD;
            }
            contribA0B1 = (contribA0B1 * (Rv % MOD)) % MOD;

            long totalForI = (cntKge2 + contribA1B0 + contribA0B1) % MOD;
            answer = (answer + totalForI) % MOD;
        }
        return (int) answer;
    }
}
```

## Python

```python
class Solution(object):
    def subsequencesWithMiddleMode(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        # factorials for combinations
        maxN = n
        fact = [1] * (maxN + 1)
        invfact = [1] * (maxN + 1)
        for i in range(1, maxN + 1):
            fact[i] = fact[i-1] * i % MOD
        invfact[maxN] = pow(fact[maxN], MOD-2, MOD)
        for i in range(maxN, 0, -1):
            invfact[i-1] = invfact[i] * i % MOD

        def C(nn, kk):
            if kk < 0 or kk > nn:
                return 0
            return fact[nn] * invfact[kk] % MOD * invfact[nn-kk] % MOD

        # total frequency of each value
        total_cnt = {}
        for v in nums:
            total_cnt[v] = total_cnt.get(v, 0) + 1

        left_cnt = {}  # frequencies to the left of current index
        ans = 0

        for i, m in enumerate(nums):
            L_total = i
            R_total = n - i - 1
            L_eq = left_cnt.get(m, 0)
            R_eq = total_cnt[m] - L_eq - 1

            L_neq = L_total - L_eq
            R_neq = R_total - R_eq

            # precompute sums needed for k=2 cases
            sum_left_pair = 0      # Σ C(cnt_left[v],2) for v!=m
            sum_right_pair = 0     # Σ C(cnt_right[v],2) for v!=m
            cross_L = 0            # Σ cnt_left[v]*cnt_right[v]*(L_neq - cnt_left[v])
            cross_R = 0            # Σ cnt_left[v]*cnt_right[v]*(R_neq - cnt_right[v])

            for val, tot in total_cnt.items():
                if val == m:
                    continue
                cl = left_cnt.get(val, 0)
                cr = tot - cl  # right count (current index is not this value)

                if cl >= 2:
                    sum_left_pair = (sum_left_pair + C(cl, 2)) % MOD
                if cr >= 2:
                    sum_right_pair = (sum_right_pair + C(cr, 2)) % MOD

                cross_L = (cross_L + cl * cr * (L_neq - cl)) % MOD
                cross_R = (cross_R + cl * cr * (R_neq - cr)) % MOD

            # iterate over possible a,b (number of equal elements taken from left/right)
            for a in range(0, 3):
                if a > L_eq or 2 - a > L_neq:
                    continue
                for b in range(0, 3):
                    if b > R_eq or 2 - b > R_neq:
                        continue
                    k = 1 + a + b
                    if k < 2:
                        continue

                    # special handling when k == 2 (a+b == 1)
                    if k == 2:
                        if a == 0 and b == 1:
                            total = C(L_neq, 2) * R_eq % MOD * R_neq % MOD
                            Lpair = sum_left_pair * R_neq % MOD
                            distinct = (total - (Lpair + cross_L)) % MOD
                            ans = (ans + distinct) % MOD
                        elif a == 1 and b == 0:
                            total = L_eq * C(L_neq, 1) % MOD * C(R_neq, 2) % MOD
                            Rpair = sum_right_pair * L_neq % MOD
                            distinct = (total - (Rpair + cross_R)) % MOD
                            ans = (ans + distinct) % MOD
                        # other combos with a+b==1 are covered above; no need else
                    else:
                        ways = C(L_eq, a) * C(L_neq, 2 - a) % MOD
                        ways = ways * C(R_eq, b) % MOD
                        ways = ways * C(R_neq, 2 - b) % MOD
                        ans = (ans + ways) % MOD

            # update left_cnt with current element for next iteration
            left_cnt[m] = left_cnt.get(m, 0) + 1

        return ans % MOD
```

## Python3

```python
import sys
from collections import Counter

class Solution:
    def subsequencesWithMiddleMode(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        total_cnt = Counter(nums)

        left_cnt = Counter()
        ans = 0

        def C2(x):
            return x * (x - 1) // 2 if x >= 2 else 0

        for m in range(2, n - 2 + 1):
            v = nums[m]

            L = left_cnt.get(v, 0)
            R_raw = total_cnt[v] - L          # includes the middle element
            R = R_raw - 1                      # exclude the middle itself

            left_notv_total = m - L
            right_notv_total = (n - 1 - m) - R

            # ----- case A : k=5 -----
            if L >= 2 and R >= 2:
                ans += C2(L) * C2(R)

            # ----- case B : k=4 -----
            ans += C2(L) * R * right_notv_total
            ans += L * C2(R) * left_notv_total

            # ----- case C : k=3 -----
            ans += C2(left_notv_total) * C2(R)
            ans += L * left_notv_total * R * right_notv_total
            ans += C2(L) * C2(right_notv_total)

            # prepare sums for distinct pairs on each side
            sum_same_left = 0
            for val, cnt in left_cnt.items():
                if val != v:
                    sum_same_left += C2(cnt)
            total_pairs_left = C2(left_notv_total)
            distinct_pairs_left = total_pairs_left - sum_same_left

            sum_same_right = 0
            # compute right counts (excluding middle) on the fly
            for val, tot in total_cnt.items():
                cnt_right_raw = tot - left_cnt.get(val, 0)
                if val != v:
                    sum_same_right += C2(cnt_right_raw)
            total_pairs_right = C2(right_notv_total)
            distinct_pairs_right = total_pairs_right - sum_same_right

            # ----- case D : k=2 -----
            # option a: extra v on left
            if L >= 1 and left_notv_total >= 1 and right_notv_total >= 2:
                s = 0
                for val, cnt_left in left_cnt.items():
                    if val == v:
                        continue
                    r = total_cnt.get(val, 0) - left_cnt.get(val, 0)   # right count of this value (middle not this value)
                    excl = r * (right_notv_total - r)
                    s += cnt_left * (distinct_pairs_right - excl)
                ans += L * s

            # option b: extra v on right
            if R >= 1 and right_notv_total >= 1 and left_notv_total >= 2:
                s = 0
                for val, tot in total_cnt.items():
                    cnt_right_raw = tot - left_cnt.get(val, 0)
                    if val == v or cnt_right_raw == 0:
                        continue
                    l = left_cnt.get(val, 0)
                    excl = l * (left_notv_total - l)
                    s += cnt_right_raw * (distinct_pairs_left - excl)
                ans += R * s

            ans %= MOD

            # move current element to left side for next iteration
            left_cnt[v] += 1

        return ans % MOD
```

## C

```c
#include <stdio.h>
#include <stdlib.h>

#define MOD 1000000007LL
static const long long INV2 = 500000004LL; // modular inverse of 2 modulo MOD

int subsequencesWithMiddleMode(int* nums, int numsSize) {
    int n = numsSize;
    // coordinate compression
    int *vals = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) vals[i] = nums[i];
    qsort(vals, n, sizeof(int), (int (*)(const void*, const void*))strcmp);
    int m = 0;
    for (int i = 0; i < n; ++i) {
        if (i == 0 || vals[i] != vals[i-1]) vals[m++] = vals[i];
    }
    // map original to compressed index
    int *comp = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) {
        int lo = 0, hi = m-1;
        while (lo <= hi) {
            int mid = (lo+hi)/2;
            if (vals[mid] == nums[i]) { comp[i]=mid; break;}
            else if (vals[mid] < nums[i]) lo=mid+1;
            else hi=mid-1;
        }
    }

    // total counts per value
    int *total = (int*)calloc(m, sizeof(int));
    for (int i = 0; i < n; ++i) total[comp[i]]++;

    // prefix counts: pref[i][v] = count of v in nums[0..i-1]
    int **pref = (int**)malloc((n+1) * sizeof(int*));
    pref[0] = (int*)calloc(m, sizeof(int));
    for (int i = 1; i <= n; ++i) {
        pref[i] = (int*)malloc(m * sizeof(int));
        memcpy(pref[i], pref[i-1], m * sizeof(int));
        pref[i][comp[i-1]]++;
    }

    long long answer = 0;

    for (int i = 0; i < n; ++i) {
        int mid = comp[i];
        long long L_eq = pref[i][mid];
        long long R_eq = total[mid] - pref[i+1][mid];
        long long L_total = i;
        long long R_total = n - i - 1;
        long long S1L = L_total - L_eq; // left non-m
        long long Rn   = R_total - R_eq; // right non-m

        // aggregates over values != mid
        long long sumSqL = 0, sumSqR = 0;
        long long crossSum = 0, sumL2R = 0, sumLR2 = 0;

        for (int v = 0; v < m; ++v) {
            if (v == mid) continue;
            long long cntL = pref[i][v];
            long long cntR = total[v] - pref[i+1][v];
            sumSqL += (cntL * cntL) % MOD; if (sumSqL >= MOD) sumSqL -= MOD;
            sumSqR += (cntR * cntR) % MOD; if (sumSqR >= MOD) sumSqR -= MOD;
            crossSum = (crossSum + (cntL * cntR) % MOD) % MOD;
            sumL2R = (sumL2R + ((cntL * cntL) % MOD) * cntR) % MOD;
            sumLR2 = (sumLR2 + (cntL * ((cntR * cntR) % MOD)) ) % MOD;
        }

        // distinct pairs
        long long distinctPairsLeft = 0, distinctPairsRight = 0;
        if (S1L >= 2) {
            long long tmp = ((S1L % MOD) * (S1L % MOD)) % MOD;
            tmp = (tmp - sumSqL + MOD) % MOD;
            distinctPairsLeft = (tmp * INV2) % MOD;
        }
        if (Rn >= 2) {
            long long tmp = ((Rn % MOD) * (Rn % MOD)) % MOD;
            tmp = (tmp - sumSqR + MOD) % MOD;
            distinctPairsRight = (tmp * INV2) % MOD;
        }

        // helper for C(x,2)
        auto comb2 = [&](long long x)->long long{
            if (x < 2) return 0LL;
            return ((x % MOD) * ((x-1) % MOD) % MOD) * INV2 % MOD;
        };

        // a=4
        long long contrib4 = comb2(L_eq) * comb2(R_eq) % MOD;

        // a=3
        long long term31 = (L_eq % MOD) * ((L_total - L_eq) % MOD) % MOD * comb2(R_eq) % MOD;
        long long term32 = comb2(L_eq) * (R_eq % MOD) % MOD * ((R_total - R_eq) % MOD) % MOD;
        long long contrib3 = (term31 + term32) % MOD;

        // a=2
        long long term0 = comb2(S1L) * comb2(R_eq) % MOD;
        long long term1 = (L_eq % MOD) * (R_eq % MOD) % MOD *
                         ((L_total - L_eq) % MOD) % MOD *
                         ((R_total - R_eq) % MOD) % MOD;
        long long term2 = comb2(L_eq) * comb2(Rn) % MOD;
        long long contrib2 = (term0 + term1 + term2) % MOD;

        // a=1
        // case A: extra m on right
        long long termA = (Rn % MOD) * distinctPairsLeft % MOD;
        long long subA = ((S1L % MOD) * (crossSum % MOD)) % MOD;
        subA = (subA - sumL2R + MOD) % MOD;
        termA = (termA - subA + MOD) % MOD;
        long long contribA = (R_eq % MOD) * termA % MOD;

        // case B: extra m on left
        long long termB = (S1L % MOD) * distinctPairsRight % MOD;
        long long subB = ((Rn % MOD) * (crossSum % MOD)) % MOD;
        subB = (subB - sumLR2 + MOD) % MOD;
        termB = (termB - subB + MOD) % MOD;
        long long contribB = (L_eq % MOD) * termB % MOD;

        long long contrib1 = (contribA + contribB) % MOD;

        long long total_i = (contrib1 + contrib2 + contrib3 + contrib4) % MOD;
        answer += total_i;
        if (answer >= MOD) answer -= MOD;
    }

    // free memory
    for (int i = 0; i <= n; ++i) free(pref[i]);
    free(pref);
    free(total);
    free(comp);
    free(vals);

    return (int)(answer % MOD);
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    const int MOD = 1000000007;
    public int SubsequencesWithMiddleMode(int[] nums) {
        int n = nums.Length;
        // Coordinate compression
        var dict = new Dictionary<int, int>();
        int idx = 0;
        foreach (var v in nums) {
            if (!dict.ContainsKey(v)) dict[v] = idx++;
        }
        int m = idx; // number of distinct values
        int[] comp = new int[n];
        for (int i = 0; i < n; i++) comp[i] = dict[nums[i]];
        // total counts per value
        int[] totalCnt = new int[m];
        foreach (var id in comp) totalCnt[id]++;
        // prefix counts: pref[i][id] = count of id in first i elements (0..i-1)
        int[,] pref = new int[n + 1, m];
        for (int i = 0; i < n; i++) {
            for (int v = 0; v < m; v++) {
                pref[i + 1, v] = pref[i, v];
            }
            pref[i + 1, comp[i]]++;
        }
        // factorials
        long[] fact = new long[n + 1];
        long[] invFact = new long[n + 1];
        fact[0] = 1;
        for (int i = 1; i <= n; i++) fact[i] = fact[i - 1] * i % MOD;
        invFact[n] = ModPow(fact[n], MOD - 2);
        for (int i = n; i > 0; i--) invFact[i - 1] = invFact[i] * i % MOD;

        long answer = 0;
        for (int i = 0; i < n; i++) {
            int midId = comp[i];
            int Ltotal = i;
            int Rtotal = n - i - 1;
            int Lm = pref[i, midId];
            int Rm = totalCnt[midId] - pref[i + 1, midId];
            int Lnon = Ltotal - Lm;
            int Rnon = Rtotal - Rm;

            long curAns = 0;

            // x = 4 (total m count =5)
            if (Lm >= 2 && Rm >= 2) {
                curAns = (curAns + Comb(Lm, 2, fact, invFact) * Comb(Rm, 2, fact, invFact)) % MOD;
            }

            // x = 3 (total m count =4)
            if (Lm >= 2 && Rnon > 0) {
                long ways = Comb(Lm, 2, fact, invFact);
                ways = ways * Rm % MOD;
                ways = ways * Rnon % MOD;
                curAns = (curAns + ways) % MOD;
            }
            if (Rm >= 2 && Lnon > 0) {
                long ways = Comb(Rm, 2, fact, invFact);
                ways = ways * Lm % MOD;
                ways = ways * Lnon % MOD;
                curAns = (curAns + ways) % MOD;
            }

            // x = 2 (total m count =3)
            for (int a = 0; a <= 2; a++) {
                int b = 2 - a; // left non-m
                int c = 2 - a; // right m count
                int d = a;     // right non-m
                if (Lm >= a && Rm >= c && Lnon >= b && Rnon >= d) {
                    long ways = Comb(Lm, a, fact, invFact);
                    ways = ways * Comb(Lnon, b, fact, invFact) % MOD;
                    ways = ways * Comb(Rm, c, fact, invFact) % MOD;
                    ways = ways * Comb(Rnon, d, fact, invFact) % MOD;
                    curAns = (curAns + ways) % MOD;
                }
            }

            // x = 1 (total m count =2)
            long[,] dp = new long[3, 4];
            dp[0, 0] = 1;
            for (int vid = 0; vid < m; vid++) {
                if (vid == midId) continue;
                int Lv = pref[i, vid];
                int Rv = totalCnt[vid] - pref[i + 1, vid];
                if (Lv == 0 && Rv == 0) continue;
                long[,] nxt = (long[,])dp.Clone();
                for (int pl = 0; pl <= 2; pl++) {
                    for (int qr = 0; qr <= 3; qr++) {
                        long val = dp[pl, qr];
                        if (val == 0) continue;
                        if (Lv > 0 && pl + 1 <= 2) {
                            nxt[pl + 1, qr] = (nxt[pl + 1, qr] + val * Lv) % MOD;
                        }
                        if (Rv > 0 && qr + 1 <= 3) {
                            nxt[pl, qr + 1] = (nxt[pl, qr + 1] + val * Rv) % MOD;
                        }
                    }
                }
                dp = nxt;
            }
            long term1 = ((long)Rm * dp[2, 1]) % MOD; // extra m on right
            long term2 = ((long)Lm * dp[1, 2]) % MOD; // extra m on left
            curAns = (curAns + term1 + term2) % MOD;

            answer = (answer + curAns) % MOD;
        }

        return (int)answer;
    }

    private static long Comb(int n, int k, long[] fact, long[] invFact) {
        if (k < 0 || k > n) return 0;
        return fact[n] * invFact[k] % MOD * invFact[n - k] % MOD;
    }

    private static long ModPow(long a, long e) {
        long res = 1;
        while (e > 0) {
            if ((e & 1) == 1) res = res * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return res;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var subsequencesWithMiddleMode = function(nums) {
    const MOD = 1_000_000_007;
    const n = nums.length;

    // frequency maps for left and right sides
    const leftMap = new Map();
    const rightMap = new Map();

    // initialize right map with all elements
    for (const x of nums) {
        rightMap.set(x, (rightMap.get(x) || 0) + 1);
    }

    let leftSize = 0;
    let rightSize = n;

    // sum of C(cnt,2) over all values in each side
    let leftSamePairsAll = 0; // initially empty
    let rightSamePairsAll = 0;
    for (const cnt of rightMap.values()) {
        rightSamePairsAll += cnt * (cnt - 1) / 2;
    }

    const comb2 = (x) => x * (x - 1) / 2;

    let ans = 0;

    for (let m = 0; m < n; ++m) {
        const v = nums[m];

        // remove current element from right side
        let cntRv = rightMap.get(v);
        rightSamePairsAll -= comb2(cntRv);
        cntRv--;
        if (cntRv === 0) rightMap.delete(v);
        else rightMap.set(v, cntRv);
        rightSamePairsAll += comb2(cntRv);
        rightSize--;

        const lsize = leftSize;
        const rsize = rightSize;

        const lv = leftMap.get(v) || 0;
        const rv = rightMap.get(v) || 0;

        // counts of pairs on each side
        const L2 = comb2(lv);
        const L1 = lv * (lsize - lv);
        const L0 = comb2(lsize - lv);

        const R2 = comb2(rv);
        const R1 = rv * (rsize - rv);
        const R0 = comb2(rsize - rv);

        // total pairs where k >= 2
        const totalPairs = (L0 + L1 + L2) * (R0 + R1 + R2);
        let base = totalPairs - L0 * R0 - L0 * R1 - L1 * R0;
        base %= MOD;
        if (base < 0) base += MOD;

        // ----- handle i=1, j=0 case -----
        const totalRightNonV = rsize - rv;
        const sameRv = comb2(rv);
        const distinctPairsRight = comb2(totalRightNonV) - (rightSamePairsAll - sameRv);

        let add_i1j0 = 0;
        if (lv > 0 && totalRightNonV >= 2) {
            for (const [x, cntLx] of leftMap.entries()) {
                if (x === v) continue;
                const cntRx = rightMap.get(x) || 0;
                // pairs on right with distinct values and none equal to x
                const invalidWithX = cntRx * (totalRightNonV - cntRx);
                let validRight = distinctPairsRight - invalidWithX;
                if (validRight < 0) validRight = 0;
                const waysLeft = lv * cntLx; // pick one v and one x on left
                add_i1j0 = (add_i1j0 + waysLeft * validRight) % MOD;
            }
        }

        // ----- handle i=0, j=1 case -----
        const totalLeftNonV = lsize - lv;
        const sameLv = comb2(lv);
        const distinctPairsLeft = comb2(totalLeftNonV) - (leftSamePairsAll - sameLv);

        let add_i0j1 = 0;
        if (rv > 0 && totalLeftNonV >= 2) {
            for (const [x, cntRx] of rightMap.entries()) {
                if (x === v) continue;
                const cntLx = leftMap.get(x) || 0;
                const invalidWithX = cntLx * (totalLeftNonV - cntLx);
                let validLeft = distinctPairsLeft - invalidWithX;
                if (validLeft < 0) validLeft = 0;
                const waysRight = rv * cntRx; // pick one v and one x on right
                add_i0j1 = (add_i0j1 + waysRight * validLeft) % MOD;
            }
        }

        ans = (ans + base + add_i1j0 + add_i0j1) % MOD;

        // add current element to left side for next iteration
        let cntLv = leftMap.get(v) || 0;
        leftSamePairsAll -= comb2(cntLv);
        cntLv++;
        leftMap.set(v, cntLv);
        leftSamePairsAll += comb2(cntLv);
        leftSize++;
    }

    return ans % MOD;
};
```

## Typescript

```typescript
function subsequencesWithMiddleMode(nums: number[]): number {
    const MOD = 1000000007;
    const n = nums.length;

    // helper for C(x,2)
    const comb2 = (x: number): number => {
        if (x < 2) return 0;
        return ((x * (x - 1)) / 2) % MOD;
    };

    // build right frequency map
    const rightMap = new Map<number, number>();
    for (const v of nums) {
        rightMap.set(v, (rightMap.get(v) ?? 0) + 1);
    }

    // collect all distinct values for iteration
    const distinctVals: number[] = Array.from(new Set(nums));

    const leftMap = new Map<number, number>();
    let answer = 0;

    for (let i = 0; i < n; ++i) {
        const m = nums[i];

        // remove current element from right side
        const cntR = rightMap.get(m)!;
        if (cntR === 1) rightMap.delete(m);
        else rightMap.set(m, cntR - 1);

        const L = i;
        const R = n - 1 - i;

        const leftM = leftMap.get(m) ?? 0;
        const rightM = rightMap.get(m) ?? 0;

        const leftNonM = L - leftM;
        const rightNonM = R - rightM;

        if (L < 2 || R < 2) {
            // cannot pick two on either side
            // add current to left and continue
            leftMap.set(m, (leftMap.get(m) ?? 0) + 1);
            continue;
        }

        const total = comb2(L) * comb2(R) % MOD;
        const ways0m = comb2(leftNonM) * comb2(rightNonM) % MOD;

        // exactly one extra m
        const ways1m_left = (leftM * leftNonM % MOD) * comb2(rightNonM) % MOD;
        const ways1m_right = comb2(leftNonM) * (rightM * rightNonM % MOD) % MOD;
        const waysExactly1m = (ways1m_left + ways1m_right) % MOD;

        // count invalid selections among those with exactly one extra m
        let invalidDup = 0;

        for (const v of distinctVals) {
            if (v === m) continue;
            const lc = leftMap.get(v) ?? 0;
            const rc = rightMap.get(v) ?? 0;

            // extra m from left side
            if (leftM > 0) {
                // duplicate pair: left non-m v with right non-m v
                const term1 = leftM * lc % MOD * rc % MOD * ((rightNonM - rc) % MOD) % MOD;
                // duplicate pair both from right side
                const term2 = leftM *
                    ((leftNonM - lc) % MOD) % MOD *
                    (rc * (rc - 1) / 2 % MOD) % MOD;
                invalidDup = (invalidDup + term1 + term2) % MOD;
            }

            // extra m from right side
            if (rightM > 0) {
                // duplicate pair both from left side
                const term3 = rightM *
                    (lc * (lc - 1) / 2 % MOD) % MOD *
                    ((rightNonM - rc) % MOD) % MOD;
                // duplicate across left and right
                const term4 = rightM *
                    lc % MOD *
                    ((leftNonM - lc) % MOD) % MOD *
                    rc % MOD;
                invalidDup = (invalidDup + term3 + term4) % MOD;
            }
        }

        // ensure positive modulo for intermediate subtraction
        let valid = (total - ways0m - waysExactly1m) % MOD;
        if (valid < 0) valid += MOD;
        valid = (valid + invalidDup) % MOD;

        answer += valid;
        if (answer >= MOD) answer -= MOD;

        // add current element to left side for next iteration
        leftMap.set(m, (leftMap.get(m) ?? 0) + 1);
    }

    return answer % MOD;
}
```

## Php

```php
<?php
class Solution {
    const MOD = 1000000007;

    private function modPow($a, $e) {
        $mod = self::MOD;
        $res = 1;
        $a %= $mod;
        while ($e > 0) {
            if ($e & 1) $res = ($res * $a) % $mod;
            $a = ($a * $a) % $mod;
            $e >>= 1;
        }
        return $res;
    }

    private function prepareComb($n) {
        $mod = self::MOD;
        $fact = array_fill(0, $n + 1, 1);
        for ($i = 1; $i <= $n; ++$i) {
            $fact[$i] = ($fact[$i - 1] * $i) % $mod;
        }
        $invFact = array_fill(0, $n + 1, 1);
        $invFact[$n] = $this->modPow($fact[$n], $mod - 2);
        for ($i = $n; $i > 0; --$i) {
            $invFact[$i - 1] = ($invFact[$i] * $i) % $mod;
        }
        return [$fact, $invFact];
    }

    private function comb($n, $k, $fact, $invFact) {
        if ($k < 0 || $k > $n) return 0;
        $mod = self::MOD;
        return ((($fact[$n] * $invFact[$k]) % $mod) * $invFact[$n - $k]) % $mod;
    }

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function subsequencesWithMiddleMode($nums) {
        $n = count($nums);
        [$fact, $invFact] = $this->prepareComb($n);

        // total frequency map
        $totalCounts = [];
        foreach ($nums as $val) {
            if (!isset($totalCounts[$val])) $totalCounts[$val] = 0;
            $totalCounts[$val]++;
        }

        $leftCounts = []; // frequencies before current index
        $ans = 0;
        for ($j = 0; $j < $n; ++$j) {
            $v = $nums[$j];
            $L = $leftCounts[$v] ?? 0;
            $R = $totalCounts[$v] - $L - 1;

            $leftNonV = $j - $L;
            $rightNonV = ($n - $j - 1) - $R;

            // build right frequency map for this j
            $rightCounts = [];
            foreach ($totalCounts as $val => $tot) {
                $left = $leftCounts[$val] ?? 0;
                $sub = ($val == $v) ? 1 : 0;
                $cnt = $tot - $left - $sub;
                if ($cnt > 0) $rightCounts[$val] = $cnt;
            }

            // precompute distinct pairs counts
            $totalLeftPairsDistinct = $this->comb($leftNonV, 2, $fact, $invFact);
            foreach ($leftCounts as $val => $cnt) {
                if ($val == $v) continue;
                $totalLeftPairsDistinct = ($totalLeftPairsDistinct - $this->comb($cnt, 2, $fact, $invFact)) % self::MOD;
            }
            if ($totalLeftPairsDistinct < 0) $totalLeftPairsDistinct += self::MOD;

            $totalRightPairsDistinct = $this->comb($rightNonV, 2, $fact, $invFact);
            foreach ($rightCounts as $val => $cnt) {
                if ($val == $v) continue;
                $totalRightPairsDistinct = ($totalRightPairsDistinct - $this->comb($cnt, 2, $fact, $invFact)) % self::MOD;
            }
            if ($totalRightPairsDistinct < 0) $totalRightPairsDistinct += self::MOD;

            // c = 1 cases (extra v on left)
            if ($L >= 1 && $leftNonV >= 1 && $rightNonV >= 2) {
                $ways_v = $L; // C(L,1)
                $sum = 0;
                foreach ($leftCounts as $val => $cntL) {
                    if ($val == $v) continue;
                    $freqLx = $cntL;
                    $freqRx = $rightCounts[$val] ?? 0;
                    $bad = ($freqRx * ($rightNonV - $freqRx)) % self::MOD;
                    $good = $totalRightPairsDistinct - $bad;
                    $good %= self::MOD;
                    if ($good < 0) $good += self::MOD;
                    $sum = ($sum + ($freqLx * $good) % self::MOD) % self::MOD;
                }
                $ans = ($ans + ($ways_v * $sum) % self::MOD) % self::MOD;
            }

            // c = 1 cases (extra v on right)
            if ($R >= 1 && $rightNonV >= 1 && $leftNonV >= 2) {
                $ways_v = $R; // C(R,1)
                $sum = 0;
                foreach ($rightCounts as $val => $cntR) {
                    if ($val == $v) continue;
                    $freqRy = $cntR;
                    $freqLx = $leftCounts[$val] ?? 0;
                    $bad = ($freqLx * ($leftNonV - $freqLx)) % self::MOD;
                    $good = $totalLeftPairsDistinct - $bad;
                    $good %= self::MOD;
                    if ($good < 0) $good += self::MOD;
                    $sum = ($sum + ($freqRy * $good) % self::MOD) % self::MOD;
                }
                $ans = ($ans + ($ways_v * $sum) % self::MOD) % self::MOD;
            }

            // c >= 2 cases
            for ($c = 2; $c <= 4; ++$c) {
                for ($cl = 0; $cl <= 2; ++$cl) {
                    $cr = $c - $cl;
                    if ($cr < 0 || $cr > 2) continue;
                    if ($L < $cl || $R < $cr) continue;
                    $leftRemain = 2 - $cl;
                    $rightRemain = 2 - $cr;
                    if ($leftNonV < $leftRemain || $rightNonV < $rightRemain) continue;

                    $ways_v = ($this->comb($L, $cl, $fact, $invFact) *
                               $this->comb($R, $cr, $fact, $invFact)) % self::MOD;
                    $ways_nonv = ($this->comb($leftNonV, $leftRemain, $fact, $invFact) *
                                  $this->comb($rightNonV, $rightRemain, $fact, $invFact)) % self::MOD;
                    $ans = ($ans + ($ways_v * $ways_nonv) % self::MOD) % self::MOD;
                }
            }

            // update leftCounts with current element for next iteration
            if (!isset($leftCounts[$v])) $leftCounts[$v] = 0;
            $leftCounts[$v]++;
        }

        return ($ans % self::MOD + self::MOD) % self::MOD;
    }
}
?>
```

## Swift

```swift
class Solution {
    private let MOD: Int64 = 1_000_000_007

    private func comb(_ n: Int, _ k: Int) -> Int64 {
        if k < 0 || k > n { return 0 }
        switch k {
        case 0:
            return 1
        case 1:
            return Int64(n)
        case 2:
            return Int64(n) * Int64(n - 1) / 2
        default:
            return 0
        }
    }

    func subsequencesWithMiddleMode(_ nums: [Int]) -> Int {
        let n = nums.count
        var totalFreq = [Int: Int]()
        for v in nums {
            totalFreq[v, default: 0] += 1
        }

        var prefix = [Int: Int]()
        var ans: Int64 = 0

        for j in 0..<n {
            let v = nums[j]
            let leftCountV = prefix[v] ?? 0
            let rightCountV = totalFreq[v]! - leftCountV - 1

            let leftNon = j - leftCountV
            let rightNon = (n - 1 - j) - rightCountV

            for l in 0...2 {
                if l > leftCountV { continue }
                let needLeftNon = 2 - l
                if needLeftNon < 0 || needLeftNon > leftNon { continue }

                let waysLeftV = comb(leftCountV, l)
                let waysLeftNon = comb(leftNon, needLeftNon)
                let waysLeft = (waysLeftV * waysLeftNon) % MOD

                for r in 0...2 {
                    if r > rightCountV { continue }
                    let needRightNon = 2 - r
                    if needRightNon < 0 || needRightNon > rightNon { continue }
                    if l + r < 2 { continue }

                    let waysRightV = comb(rightCountV, r)
                    let waysRightNon = comb(rightNon, needRightNon)
                    let waysRight = (waysRightV * waysRightNon) % MOD

                    ans += (waysLeft * waysRight) % MOD
                    if ans >= MOD { ans -= MOD }
                }
            }

            prefix[v, default: 0] += 1
        }

        return Int(ans % MOD)
    }
}
```

## Kotlin

```kotlin
import java.util.HashMap

class Solution {
    private val MOD = 1_000_000_007L
    private lateinit var fact: LongArray
    private lateinit var invFact: LongArray
    private fun modPow(a: Long, e: Long): Long {
        var base = a % MOD
        var exp = e
        var res = 1L
        while (exp > 0) {
            if ((exp and 1L) == 1L) res = res * base % MOD
            base = base * base % MOD
            exp = exp shr 1
        }
        return res
    }
    private fun comb(n: Int, k: Int): Long {
        if (k < 0 || k > n) return 0L
        return fact[n] * invFact[k] % MOD * invFact[n - k] % MOD
    }

    fun subsequencesWithMiddleMode(nums: IntArray): Int {
        val n = nums.size
        fact = LongArray(n + 5)
        invFact = LongArray(n + 5)
        fact[0] = 1L
        for (i in 1 until fact.size) fact[i] = fact[i - 1] * i % MOD
        invFact[fact.size - 1] = modPow(fact[fact.size - 1], MOD - 2)
        for (i in fact.size - 2 downTo 0) invFact[i] = invFact[i + 1] * (i + 1) % MOD

        val suffixMap = HashMap<Int, Int>()
        for (v in nums) {
            suffixMap[v] = suffixMap.getOrDefault(v, 0) + 1
        }
        val prefixMap = HashMap<Int, Int>()

        var answer = 0L
        val inv2 = (MOD + 1) / 2

        for (m in 0 until n) {
            val cur = nums[m]
            // remove current from suffix
            suffixMap[cur] = suffixMap[cur]!! - 1
            if (suffixMap[cur] == 0) suffixMap.remove(cur)

            val a = prefixMap.getOrDefault(cur, 0)
            val b = suffixMap.getOrDefault(cur, 0)

            val totalPrefix = m
            val totalSuffix = n - 1 - m

            val nonVPref = totalPrefix - a
            val nonVSuf = totalSuffix - b

            // aggregates for distinctness handling (k=1)
            var sumL2 = 0L
            var sumR2 = 0L
            var sumLR = 0L
            var sumL2R = 0L
            var sumL_Rx2 = 0L

            for ((value, cntPref) in prefixMap) {
                if (value == cur) continue
                val L = cntPref.toLong()
                val R = suffixMap.getOrDefault(value, 0).toLong()
                sumL2 = (sumL2 + L * L) % MOD
                sumLR = (sumLR + L * R) % MOD
                sumL2R = (sumL2R + (L * L % MOD) * R) % MOD
                sumL_Rx2 = (sumL_Rx2 + L * (R * R % MOD)) % MOD
            }
            for ((value, cntSuf) in suffixMap) {
                if (value == cur) continue
                val R = cntSuf.toLong()
                sumR2 = (sumR2 + R * R) % MOD
            }

            var totalWays = 0L

            // k=1 split: kl=0, kr=1
            if (b >= 1 && nonVPref >= 2 && nonVSuf >= 1) {
                val A = nonVPref.toLong() % MOD
                val B = sumL2
                val CtotalR = nonVSuf.toLong() % MOD

                var T = (A * sumLR % MOD - sumL2R + MOD) % MOD
                var distinctWays = CtotalR *
                        (( (A * A % MOD - B + MOD) % MOD) * inv2 % MOD) % MOD
                distinctWays = (distinctWays - 2L * T % MOD + MOD) % MOD

                val contrib = (b.toLong() % MOD) * distinctWays % MOD
                totalWays = (totalWays + contrib) % MOD
            }

            // k=1 split: kl=1, kr=0
            if (a >= 1 && nonVPref >= 1 && nonVSuf >= 2) {
                val A = nonVPref.toLong() % MOD
                val Ccnt = nonVSuf.toLong() % MOD

                val totalPairsRDistinct = ((Ccnt * Ccnt % MOD - sumR2 + MOD) % MOD) * inv2 % MOD
                var term = (Ccnt * sumLR % MOD - sumL_Rx2 + MOD) % MOD
                var distinctWays = (A * totalPairsRDistinct % MOD - term + MOD) % MOD

                val contrib = (a.toLong() % MOD) * distinctWays % MOD
                totalWays = (totalWays + contrib) % MOD
            }

            // k = 2,3,4 generic handling
            for (c in 3..5) {
                val k = c - 1
                if (k == 1) continue
                for (kl in 0..2) {
                    val kr = k - kl
                    if (kr < 0 || kr > 2) continue
                    if (a < kl || b < kr) continue
                    val leftNeed = 2 - kl
                    val rightNeed = 2 - kr
                    if (nonVPref < leftNeed || nonVSuf < rightNeed) continue

                    val waysLeft = comb(a, kl) * comb(nonVPref, leftNeed) % MOD
                    val waysRight = comb(b, kr) * comb(nonVSuf, rightNeed) % MOD
                    totalWays = (totalWays + waysLeft * waysRight % MOD) % MOD
                }
            }

            answer = (answer + totalWays) % MOD

            // add current to prefix
            prefixMap[cur] = prefixMap.getOrDefault(cur, 0) + 1
        }

        return (answer % MOD).toInt()
    }
}
```

## Dart

```dart
import 'dart:collection';
class Solution {
  static const int MOD = 1000000007;
  late List<int> _fact;
  late List<int> _invFact;

  int _modPow(int a, int e) {
    long res = 1;
    long base = a % MOD;
    while (e > 0) {
      if ((e & 1) == 1) res = (res * base) % MOD;
      base = (base * base) % MOD;
      e >>= 1;
    }
    return res.toInt();
  }

  int _comb(int n, int k) {
    if (k < 0 || k > n) return 0;
    return (((_fact[n] * _invFact[k]) % MOD) * _invFact[n - k]) % MOD;
  }

  int subsequencesWithMiddleMode(List<int> nums) {
    int n = nums.length;
    _fact = List.filled(n + 5, 1);
    for (int i = 1; i < _fact.length; ++i) {
      _fact[i] = (_fact[i - 1] * i) % MOD;
    }
    _invFact = List.filled(_fact.length, 1);
    _invFact[_fact.length - 1] = _modPow(_fact[_fact.length - 1], MOD - 2);
    for (int i = _fact.length - 2; i >= 0; --i) {
      _invFact[i] = (_invFact[i + 1] * (i + 1)) % MOD;
    }

    int answer = 0;

    for (int i = 0; i < n; ++i) {
      int v = nums[i];

      // left side
      int leftEq = 0;
      Map<int, int> leftFreq = HashMap();
      for (int j = 0; j < i; ++j) {
        if (nums[j] == v) {
          leftEq++;
        } else {
          leftFreq[nums[j]] = (leftFreq[nums[j]] ?? 0) + 1;
        }
      }
      int leftNeqTotal = i - leftEq;

      // right side
      int rightEq = 0;
      Map<int, int> rightFreq = HashMap();
      for (int j = i + 1; j < n; ++j) {
        if (nums[j] == v) {
          rightEq++;
        } else {
          rightFreq[nums[j]] = (rightFreq[nums[j]] ?? 0) + 1;
        }
      }
      int rightNeqTotal = (n - i - 1) - rightEq;

      // precompute distinct pair counts for non‑v elements
      int sumSameLeft = 0;
      leftFreq.values.forEach((cnt) {
        if (cnt >= 2) sumSameLeft = (sumSameLeft + _comb(cnt, 2)) % MOD;
      });
      int totalDistinctPairsLeft =
          (_comb(leftNeqTotal, 2) - sumSameLeft) % MOD;
      if (totalDistinctPairsLeft < 0) totalDistinctPairsLeft += MOD;

      int sumSameRight = 0;
      rightFreq.values.forEach((cnt) {
        if (cnt >= 2) sumSameRight = (sumSameRight + _comb(cnt, 2)) % MOD;
      });
      int totalDistinctPairsRight =
          (_comb(rightNeqTotal, 2) - sumSameRight) % MOD;
      if (totalDistinctPairsRight < 0) totalDistinctPairsRight += MOD;

      int ansI = 0;

      // k >= 2
      for (int k = 2; k <= 4; ++k) {
        for (int lEq = 0; lEq <= 2 && lEq <= leftEq; ++lEq) {
          int rEq = k - lEq;
          if (rEq < 0 || rEq > 2 || rEq > rightEq) continue;
          int lRem = 2 - lEq;
          int rRem = 2 - rEq;
          int ways = _comb(leftEq, lEq);
          ways = (ways * _comb(rightEq, rEq)) % MOD;
          ways = (ways * _comb(leftNeqTotal, lRem)) % MOD;
          ways = (ways * _comb(rightNeqTotal, rRem)) % MOD;
          ansI += ways;
          if (ansI >= MOD) ansI -= MOD;
        }
      }

      // k == 1, case lEq=1, rEq=0
      if (leftEq >= 1 && rightNeqTotal >= 2) {
        leftFreq.forEach((val, cntL) {
          int cntR = rightFreq[val] ?? 0;
          int pairsWithValInRight =
              (cntR * (rightNeqTotal - cntR)) % MOD;
          int validRightPairs = totalDistinctPairsRight - pairsWithValInRight;
          if (validRightPairs < 0) validRightPairs += MOD;
          int ways = (cntL % MOD) * validRightPairs % MOD;
          ansI += ways;
          if (ansI >= MOD) ansI -= MOD;
        });
      }

      // k == 1, case lEq=0, rEq=1
      if (rightEq >= 1 && leftNeqTotal >= 2) {
        rightFreq.forEach((val, cntR) {
          int cntL = leftFreq[val] ?? 0;
          int pairsWithValInLeft =
              (cntL * (leftNeqTotal - cntL)) % MOD;
          int validLeftPairs = totalDistinctPairsLeft - pairsWithValInLeft;
          if (validLeftPairs < 0) validLeftPairs += MOD;
          int ways = (cntR % MOD) * validLeftPairs % MOD;
          ansI += ways;
          if (ansI >= MOD) ansI -= MOD;
        });
      }

      answer += ansI;
      if (answer >= MOD) answer -= MOD;
    }

    return answer;
  }
}
```

## Golang

```go
func subsequencesWithMiddleMode(nums []int) int {
	const MOD int64 = 1000000007
	n := len(nums)
	// coordinate compression
	idMap := make(map[int]int)
	ids := make([]int, n)
	nextID := 0
	for i, v := range nums {
		if _, ok := idMap[v]; !ok {
			idMap[v] = nextID
			nextID++
		}
		ids[i] = idMap[v]
	}
	m := nextID
	totalCnt := make([]int, m)
	for _, id := range ids {
		totalCnt[id]++
	}
	// factorials for combinations
	fact := make([]int64, n+1)
	ifact := make([]int64, n+1)
	fact[0] = 1
	for i := 1; i <= n; i++ {
		fact[i] = fact[i-1] * int64(i) % MOD
	}
	// modular inverse using Fermat
	modPow := func(a, e int64) int64 {
		res := int64(1)
		base := a % MOD
		for e > 0 {
			if e&1 == 1 {
				res = res * base % MOD
			}
			base = base * base % MOD
			e >>= 1
		}
		return res
	}
	ifact[n] = modPow(fact[n], MOD-2)
	for i := n; i >= 1; i-- {
		ifact[i-1] = ifact[i] * int64(i) % MOD
	}
	comb := func(nn, kk int) int64 {
		if kk < 0 || kk > nn {
			return 0
		}
		return fact[nn] * ifact[kk] % MOD * ifact[nn-kk] % MOD
	}

	prefixCnt := make([]int, m)
	var ans int64 = 0

	for i := 0; i < n; i++ {
		midID := ids[i]
		L_eq := prefixCnt[midID]
		R_eq := totalCnt[midID] - (prefixCnt[midID] + 1)

		L_total := i
		R_total := n - 1 - i
		L_neq := L_total - L_eq
		R_neq := R_total - R_eq

		// contributions where number of matches >=2
		for a := 0; a <= 2; a++ {
			if a > L_eq || 2-a > L_neq {
				continue
			}
			leftWays := comb(L_eq, a) * comb(L_neq, 2-a) % MOD
			for b := 0; b <= 2; b++ {
				matches := a + b
				if matches < 2 {
					continue
				}
				if b > R_eq || 2-b > R_neq {
					continue
				}
				rightWays := comb(R_eq, b) * comb(R_neq, 2-b) % MOD
				ans = (ans + leftWays*rightWays) % MOD
			}
		}

		// precompute duplicate pair counts for distinctness case
		var dupLeft, dupRight int64 = 0, 0
		for v := 0; v < m; v++ {
			if v == midID {
				continue
			}
			lc := prefixCnt[v]
			rc := totalCnt[v] - prefixCnt[v]
			dupLeft = (dupLeft + comb(lc, 2)) % MOD
			dupRight = (dupRight + comb(rc, 2)) % MOD
		}
		totalPairsLeft := comb(L_neq, 2)
		totalPairsRight := comb(R_neq, 2)
		distinctLeft := (totalPairsLeft - dupLeft + MOD) % MOD
		distinctRight := (totalPairsRight - dupRight + MOD) % MOD

		// case: exactly one match on left side
		if L_eq >= 1 && R_neq >= 2 {
			var sum int64 = 0
			for v := 0; v < m; v++ {
				if v == midID {
					continue
				}
				lc := prefixCnt[v]
				if lc == 0 {
					continue
				}
				rc := totalCnt[v] - prefixCnt[v]
				pairsWithX := int64(rc) * int64(R_neq-rc) % MOD
				valid := (distinctRight - pairsWithX + MOD) % MOD
				sum = (sum + int64(lc)*valid) % MOD
			}
			ans = (ans + int64(L_eq)%MOD*sum) % MOD
		}

		// case: exactly one match on right side
		if R_eq >= 1 && L_neq >= 2 {
			var sum int64 = 0
			for v := 0; v < m; v++ {
				if v == midID {
					continue
				}
				rc := totalCnt[v] - prefixCnt[v]
				if rc == 0 {
					continue
				}
				lc := prefixCnt[v]
				pairsWithX := int64(lc) * int64(L_neq-lc) % MOD
				valid := (distinctLeft - pairsWithX + MOD) % MOD
				sum = (sum + int64(rc)*valid) % MOD
			}
			ans = (ans + int64(R_eq)%MOD*sum) % MOD
		}

		prefixCnt[midID]++
	}
	return int(ans % MOD)
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def mod_pow(a, e)
  res = 1
  a %= MOD
  while e > 0
    res = res * a % MOD if (e & 1) == 1
    a = a * a % MOD
    e >>= 1
  end
  res
end

def prepare_combinations(n)
  fact = Array.new(n + 1, 1)
  (1..n).each { |i| fact[i] = fact[i - 1] * i % MOD }
  inv_fact = Array.new(n + 1, 1)
  inv_fact[n] = mod_pow(fact[n], MOD - 2)
  (n - 1).downto(0) { |i| inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD }
  [fact, inv_fact]
end

def comb(n, k, fact, inv_fact)
  return 0 if n < k || k < 0
  fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD
end

def subsequences_with_middle_mode(nums)
  n = nums.length
  fact, inv_fact = prepare_combinations(n)

  # right side counts initially whole array
  right_counts = Hash.new(0)
  nums.each { |v| right_counts[v] += 1 }
  right_total = n
  right_sumC_all = 0
  right_counts.each_value { |c| right_sumC_all += c * (c - 1) / 2 }

  left_counts = Hash.new(0)
  left_total = 0
  left_sumC_all = 0

  ans = 0

  nums.each_with_index do |v, i|
    # remove current element from right side
    cnt_old = right_counts[v]
    right_sumC_all -= cnt_old * (cnt_old - 1) / 2
    cnt_new = cnt_old - 1
    right_sumC_all += cnt_new * (cnt_new - 1) / 2
    right_counts[v] = cnt_new
    right_total -= 1

    left_eq = left_counts[v]
    right_eq = right_counts[v]

    left_nonv = left_total - left_eq
    right_nonv = right_total - right_eq

    # k = 5
    if left_eq >= 2 && right_eq >= 2
      ans = (ans + comb(left_eq, 2, fact, inv_fact) * comb(right_eq, 2, fact, inv_fact)) % MOD
    end

    # k = 4
    if left_eq >= 2 && right_eq >= 1 && right_nonv >= 1
      ans = (ans + comb(left_eq, 2, fact, inv_fact) * right_eq % MOD * right_nonv) % MOD
    end
    if left_eq >= 1 && left_nonv >= 1 && right_eq >= 2
      ans = (ans + left_eq * left_nonv % MOD * comb(right_eq, 2, fact, inv_fact)) % MOD
    end

    # k = 3
    if left_eq >= 2 && right_nonv >= 2
      ans = (ans + comb(left_eq, 2, fact, inv_fact) * comb(right_nonv, 2, fact, inv_fact)) % MOD
    end
    if left_nonv >= 2 && right_eq >= 2
      ans = (ans + comb(right_eq, 2, fact, inv_fact) * comb(left_nonv, 2, fact, inv_fact)) % MOD
    end
    if left_eq >= 1 && left_nonv >= 1 && right_eq >= 1 && right_nonv >= 1
      ans = (ans + left_eq * left_nonv % MOD * right_eq % MOD * right_nonv) % MOD
    end

    # k = 2
    # subcase: extra v on left side
    if left_eq >= 1 && left_nonv >= 1 && right_nonv >= 3
      right_sumC_nonv = right_sumC_all - comb(right_eq, 2, fact, inv_fact)
      left_counts.each do |a, cntL|
        next if a == v || cntL == 0
        rcnt_a = right_counts[a] || 0
        total_pairs = comb(right_nonv - rcnt_a, 2, fact, inv_fact)
        dup_pairs = (right_sumC_nonv - comb(rcnt_a, 2, fact, inv_fact))
        distinct_pairs = total_pairs - dup_pairs
        next if distinct_pairs <= 0
        term = cntL * distinct_pairs % MOD
        ans = (ans + left_eq * term) % MOD
      end
    end

    # subcase: extra v on right side
    if right_eq >= 1 && right_nonv >= 1 && left_nonv >= 3
      left_sumC_nonv = left_sumC_all - comb(left_eq, 2, fact, inv_fact)
      right_counts.each do |a, cntR|
        next if a == v || cntR == 0
        lcnt_a = left_counts[a] || 0
        total_pairs = comb(left_nonv - lcnt_a, 2, fact, inv_fact)
        dup_pairs = (left_sumC_nonv - comb(lcnt_a, 2, fact, inv_fact))
        distinct_pairs = total_pairs - dup_pairs
        next if distinct_pairs <= 0
        term = cntR * distinct_pairs % MOD
        ans = (ans + right_eq * term) % MOD
      end
    end

    # add current element to left side for next iteration
    cnt_old_left = left_counts[v]
    left_sumC_all -= cnt_old_left * (cnt_old_left - 1) / 2
    cnt_new_left = cnt_old_left + 1
    left_sumC_all += cnt_new_left * (cnt_new_left - 1) / 2
    left_counts[v] = cnt_new_left
    left_total += 1
  end

  ans % MOD
end
```

## Scala

```scala
object Solution {
  def subsequencesWithMiddleMode(nums: Array[Int]): Int = {
    val MOD = 1000000007L
    val n = nums.length

    // total frequency map
    val totalFreq = scala.collection.mutable.Map[Int, Int]()
    for (v <- nums) {
      totalFreq(v) = totalFreq.getOrElse(v, 0) + 1
    }

    // mutable maps for left and right side frequencies
    val leftMap = scala.collection.mutable.Map[Int, Int]()
    val rightMap = totalFreq.clone() // includes all elements initially

    var answer = 0L

    def comb2(x: Long): Long = {
      if (x < 2) 0L else ((x % MOD) * ((x - 1) % MOD) / 2) % MOD
    }

    for (i <- 0 until n) {
      val v = nums(i)

      // remove current element from right side
      val cntRightVNow = rightMap(v)
      if (cntRightVNow == 1) rightMap -= v else rightMap(v) = cntRightVNow - 1

      val Ltotal = i.toLong
      val Rtotal = (n - i - 1).toLong

      val LcntV = leftMap.getOrElse(v, 0)
      val RcntV = rightMap.getOrElse(v, 0)

      val LeftNonVTotal = Ltotal - LcntV
      val RightNonVTotal = Rtotal - RcntV

      // sums for non-v values
      var sumCombL = 0L          // Σ C(cnt,2) for left non-v
      var sumCombR = 0L          // Σ C(cnt,2) for right non-v
      var sumSqLNonV = 0L        // Σ cnt^2 for left non-v (may be unused)
      var sumSqRNonV = 0L

      var sumProdLRTimesRight = 0L   // Σ lc*rc*(RightNonVTotal - rc) over non-v
      var sumProdLRTimesLeft = 0L    // Σ lc*rc*(LeftNonVTotal - lc) over non-v

      for ((key, lc) <- leftMap) {
        if (key != v) {
          val cntSq = lc.toLong * lc
          sumSqLNonV += cntSq
          sumCombL += comb2(lc)
          // right count
          val rc = rightMap.getOrElse(key, 0)
          sumProdLRTimesRight += lc.toLong * rc.toLong % MOD * ((RightNonVTotal - rc).toLong % MOD) % MOD
          sumProdLRTimesLeft  += lc.toLong * rc.toLong % MOD * ((LeftNonVTotal - lc).toLong % MOD) % MOD
        }
      }

      for ((key, rc) <- rightMap) {
        if (key != v) {
          sumSqRNonV += rc.toLong * rc
          sumCombR += comb2(rc)
        }
      }

      // total distinct pairs on each side (both non-v values must be different)
      val totalDistinctPairsLeft = ((comb2(LeftNonVTotal) - sumCombL) % MOD + MOD) % MOD
      val totalDistinctPairsRight = ((comb2(RightNonVTotal) - sumCombR) % MOD + MOD) % MOD

      // ----- cnt = 5 -----
      if (LcntV >= 2 && RcntV >= 2) {
        answer = (answer + comb2(LcntV) * comb2(RcntV) % MOD) % MOD
      }

      // ----- cnt = 4 -----
      // a=2 left, b=1 right
      if (LcntV >= 2 && RcntV >= 1 && RightNonVTotal >= 1) {
        val leftWays = comb2(LcntV)
        val rightWays = (RcntV.toLong % MOD) * (RightNonVTotal % MOD) % MOD
        answer = (answer + leftWays * rightWays % MOD) % MOD
      }
      // a=1 left, b=2 right
      if (LcntV >= 1 && RcntV >= 2 && LeftNonVTotal >= 1) {
        val leftWays = (LcntV.toLong % MOD) * (LeftNonVTotal % MOD) % MOD
        val rightWays = comb2(RcntV)
        answer = (answer + leftWays * rightWays % MOD) % MOD
      }

      // ----- cnt = 3 -----
      // a=2,b=0
      if (LcntV >= 2) {
        val leftWays = comb2(LcntV)
        val rightWays = comb2(Rtotal)
        answer = (answer + leftWays * rightWays % MOD) % MOD
      }
      // a=0,b=2
      if (RcntV >= 2) {
        val leftWays = comb2(Ltotal)
        val rightWays = comb2(RcntV)
        answer = (answer + leftWays * rightWays % MOD) % MOD
      }
      // a=1,b=1
      if (LcntV >= 1 && RcntV >= 1 && LeftNonVTotal >= 1 && RightNonVTotal >= 1) {
        val ways = (LcntV.toLong % MOD) * (LeftNonVTotal % MOD) % MOD *
          ((RcntV.toLong % MOD) * (RightNonVTotal % MOD) % MOD) % MOD
        answer = (answer + ways) % MOD
      }

      // ----- cnt = 2 -----
      // a=1 left, b=0 right
      if (LcntV >= 1 && LeftNonVTotal >= 1 && RightNonVTotal >= 2) {
        val term1 = (LeftNonVTotal % MOD) * totalDistinctPairsRight % MOD
        val term2 = sumProdLRTimesRight % MOD
        var contrib = (term1 - term2) % MOD
        if (contrib < 0) contrib += MOD
        contrib = (LcntV.toLong % MOD) * contrib % MOD
        answer = (answer + contrib) % MOD
      }
      // a=0 left, b=1 right
      if (RcntV >= 1 && RightNonVTotal >= 1 && LeftNonVTotal >= 2) {
        val term1 = (RightNonVTotal % MOD) * totalDistinctPairsLeft % MOD
        val term2 = sumProdLRTimesLeft % MOD
        var contrib = (term1 - term2) % MOD
        if (contrib < 0) contrib += MOD
        contrib = (RcntV.toLong % MOD) * contrib % MOD
        answer = (answer + contrib) % MOD
      }

      // add current element to left map for next iteration
      leftMap(v) = leftMap.getOrElse(v, 0) + 1
    }

    ((answer % MOD) + MOD).toInt
  }
}
```

## Rust

```rust
use std::collections::HashMap;

const MOD: i64 = 1_000_000_007;

fn mod_pow(mut a: i64, mut e: i64) -> i64 {
    let mut res = 1i64;
    while e > 0 {
        if e & 1 == 1 {
            res = res * a % MOD;
        }
        a = a * a % MOD;
        e >>= 1;
    }
    res
}

fn comb(n: usize, k: usize, fact: &[i64], inv_fact: &[i64]) -> i64 {
    if k > n {
        return 0;
    }
    fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD
}

impl Solution {
    pub fn subsequences_with_middle_mode(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        // factorials for combinations up to n
        let mut fact = vec![1i64; n + 1];
        for i in 1..=n {
            fact[i] = fact[i - 1] * (i as i64) % MOD;
        }
        let mut inv_fact = vec![1i64; n + 1];
        inv_fact[n] = mod_pow(fact[n], MOD - 2);
        for i in (1..=n).rev() {
            inv_fact[i - 1] = inv_fact[i] * (i as i64) % MOD;
        }

        let mut answer: i64 = 0;

        for m in 0..n {
            let mid_val = nums[m];

            // left side counts
            let mut left_eq: usize = 0;
            let mut left_map: HashMap<i32, usize> = HashMap::new();
            for i in 0..m {
                if nums[i] == mid_val {
                    left_eq += 1;
                } else {
                    *left_map.entry(nums[i]).or_insert(0) += 1;
                }
            }

            // right side counts
            let mut right_eq: usize = 0;
            let mut right_map: HashMap<i32, usize> = HashMap::new();
            for i in (m + 1)..n {
                if nums[i] == mid_val {
                    right_eq += 1;
                } else {
                    *right_map.entry(nums[i]).or_insert(0) += 1;
                }
            }

            // collect (L,R) for each distinct non-mid value
            let mut lr_vec: Vec<(i64, i64)> = Vec::new();
            for (&val, &lc) in left_map.iter() {
                let rc = *right_map.get(&val).unwrap_or(&0);
                lr_vec.push((lc as i64, rc as i64));
            }
            for (&val, &rc) in right_map.iter() {
                if !left_map.contains_key(&val) {
                    lr_vec.push((0i64, rc as i64));
                }
            }

            // dp[l][r]: ways to pick l distinct values from left side and r from right side (disjoint)
            let mut dp = vec![vec![0i64; 3]; 3];
            dp[0][0] = 1;
            for &(lcnt, rcnt) in lr_vec.iter() {
                for l in (0..=2).rev() {
                    for r in (0..=2).rev() {
                        let cur = dp[l][r];
                        if cur == 0 {
                            continue;
                        }
                        if l + 1 <= 2 && lcnt > 0 {
                            dp[l + 1][r] = (dp[l + 1][r] + cur * (lcnt % MOD)) % MOD;
                        }
                        if r + 1 <= 2 && rcnt > 0 {
                            dp[l][r + 1] = (dp[l][r + 1] + cur * (rcnt % MOD)) % MOD;
                        }
                    }
                }
            }

            // enumerate how many extra mid values are taken from left/right
            for a in 0..=2usize {
                if a > left_eq { continue; }
                for b in 0..=2usize {
                    if b > right_eq { continue; }
                    let k = 1 + a + b;
                    if k < 2 { continue; } // need at least two occurrences of mid value
                    let l_needed = 2 - a;
                    let r_needed = 2 - b;
                    if l_needed > 2 || r_needed > 2 {
                        continue;
                    }
                    let ways_mid = comb(left_eq, a, &fact, &inv_fact)
                        * comb(right_eq, b, &fact, &inv_fact) % MOD;
                    let ways_others = dp[l_needed][r_needed];
                    let add = ways_mid * ways_others % MOD;
                    answer += add;
                    if answer >= MOD {
                        answer -= MOD;
                    }
                }
            }
        }

        (answer % MOD) as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

;; n choose k for k = 0,1,2
(define (C n k)
  (cond [(or (< k 0) (> k n)) 0]
        [(= k 0) 1]
        [(= k 1) n]
        [(= k 2) (/ (* n (- n 1)) 2)]
        [else 0]))

(define (mod-add a b)
  (let ((s (+ a b)))
    (if (>= s MOD) (- s MOD) s)))

(define (mod-sub a b)
  (let ((d (- a b)))
    (if (< d 0) (+ d MOD) d)))

(define (mod-mul a b)
  (modulo (* a b) MOD))

(define (subsequences-with-middle-mode nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         ;; total counts of each value
         (right-counts (make-hash)))
    (for ([v nums])
      (hash-set! right-counts v (+ (hash-ref right-counts v 0) 1)))
    (define left-counts (make-hash))
    (define answer 0)
    (let loop ((i 0) (nums-list nums))
      (when (< i n)
        (define val (list-ref nums i))
        ;; remove current element from right side
        (define rc (hash-ref right-counts val))
        (if (= rc 1)
            (hash-remove! right-counts val)
            (hash-set! right-counts val (- rc 1)))
        (define left-total i)
        (define right-total (- n i 1))
        (define left-eq (hash-ref left-counts val 0))
        (define right-eq (hash-ref right-counts val 0))
        (define left-neq (- left-total left-eq))
        (define right-neq (- right-total right-eq))

        ;; contribution where extra equal count >=2
        (define contrib-ge2 0)
        (for ([a (in-range 0 3)])
          (when (and (<= a left-eq) (>= (- 2 a) 0) (<= (- 2 a) left-neq))
            (define comb-left (mod-mul (C left-eq a) (C left-neq (- 2 a))))
            (for ([b (in-range 0 3)])
              (when (and (>= (+ a b) 2)
                         (<= b right-eq)
                         (>= (- 2 b) 0)
                         (<= (- 2 b) right-neq))
                (define comb-right (mod-mul (C right-eq b) (C right-neq (- 2 b))))
                (set! contrib-ge2
                      (mod-add contrib-ge2 (mod-mul comb-left comb-right)))))))
        ;; precompute sums for distinct pairs on each side
        (define total-pairs-right (C right-neq 2))
        (define sum-dup-right 0)
        (for ([kv (hash->list right-counts)])
          (define v (car kv))
          (when (not (= v val))
            (set! sum-dup-right (+ sum-dup-right (C (cdr kv) 2)))))
        (define distinct-pairs-right (mod-sub total-pairs-right sum-dup-right))

        (define total-pairs-left (C left-neq 2))
        (define sum-dup-left 0)
        (for ([kv (hash->list left-counts)])
          (define v (car kv))
          (when (not (= v val))
            (set! sum-dup-left (+ sum-dup-left (C (cdr kv) 2)))))
        (define distinct-pairs-left (mod-sub total-pairs-left sum-dup-left))

        ;; case A: left provides the extra equal element
        (define good-A 0)
        (when (and (> left-eq 0) (>= left-neq 1) (>= right-neq 2))
          (define sum-good 0)
          (for ([kv (hash->list right-counts)])
            (define v (car kv))
            (when (not (= v val))
              (define Rv (cdr kv))
              (define Lv (hash-ref left-counts v 0))
              (define term (mod-sub distinct-pairs-right
                                    (mod-mul Rv (- right-neq Rv))))
              (set! sum-good (mod-add sum-good (mod-mul Lv term)))))
          (set! good-A (mod-mul left-eq sum-good)))

        ;; case B: right provides the extra equal element
        (define good-B 0)
        (when (and (> right-eq 0) (>= right-neq 1) (>= left-neq 2))
          (define sum-good 0)
          (for ([kv (hash->list left-counts)])
            (define v (car kv))
            (when (not (= v val))
              (define Lv (cdr kv))
              (define Rv (hash-ref right-counts v 0))
              (define term (mod-sub distinct-pairs-left
                                    (mod-mul Lv (- left-neq Lv))))
              (set! sum-good (mod-add sum-good (mod-mul Rv term)))))
          (set! good-B (mod-mul right-eq sum-good)))

        (set! answer (mod-add answer (mod-add contrib-ge2 (mod-add good-A good-B))))

        ;; add current element to left side
        (hash-set! left-counts val (+ (hash-ref left-counts val 0) 1))
        (loop (+ i 1) nums-list))))
    answer))
```

## Erlang

```erlang
-module(solution).
-export([subsequences_with_middle_mode/1]).

-define(MOD, 1000000007).
-define(INV2, 500000004). % modular inverse of 2 modulo MOD

%% Public API
-spec subsequences_with_middle_mode(Nums :: [integer()]) -> integer().
subsequences_with_middle_mode(Nums) ->
    N = length(Nums),
    Right0 = build_freq_map(Nums),
    process(0, N, NumList = Nums, #{}, Right0, 0).

%% Build frequency map of a list
build_freq_map(List) ->
    lists:foldl(fun(X, Acc) ->
        case maps:get(X, Acc, 0) of
            C -> maps:put(X, C + 1, Acc)
        end
    end, #{}, List).

%% Main loop over positions
process(_Idx, _N, [], _LeftMap, _RightMap, Ans) ->
    Ans rem ?MOD;
process(Idx, N, [Val | Rest], LeftMap0, RightMap0, Ans) ->
    % remove current element from right map (it is the middle)
    RightMap = dec_map(RightMap0, Val),

    % compute contributions for this middle
    MidCnt = count_for_middle(Idx, N, Val, LeftMap0, RightMap),

    NewAns = (Ans + MidCnt) rem ?MOD,

    % add current element to left map for next iterations
    LeftMap1 = inc_map(LeftMap0, Val),

    process(Idx + 1, N, Rest, LeftMap1, RightMap, NewAns).

%% Decrement count in map, remove key if zero
dec_map(Map, Key) ->
    case maps:get(Key, Map, 0) of
        0 -> Map;
        1 -> maps:remove(Key, Map);
        C -> maps:put(Key, C - 1, Map)
    end.

%% Increment count in map
inc_map(Map, Key) ->
    case maps:get(Key, Map, 0) of
        C -> maps:put(Key, C + 1, Map)
    end.

%% Compute contributions for a fixed middle position
count_for_middle(Idx, N, Val, LeftMap, RightMap) ->
    LeftEq = maps:get(Val, LeftMap, 0),
    RightEq = maps:get(Val, RightMap, 0),

    SL = Idx - LeftEq,
    SR = (N - Idx - 1) - RightEq,

    % sum of squares on each side (excluding Val)
    SumLSq = sum_sq_excluding(LeftMap, Val),
    SumRSq = sum_sq_excluding(RightMap, Val),

    % cross aggregates
    {SumLR, SumLRCntSq, SumRLCntSq, SumLSqRSq} =
        cross_aggregates(LeftMap, RightMap, Val),

    Mod = ?MOD,
    Inv2 = ?INV2,

    %% Helper for modular multiplication
    Mul(A,B) -> ((A rem Mod) * (B rem Mod)) rem Mod end,
    Add(A,B) -> (A + B) rem Mod,
    Sub(A,B) -> ((A - B) rem Mod + Mod) rem Mod,

    %% Combination nC2 modulo MOD
    Comb2(N) when N < 2 -> 0;
    Comb2(N) ->
        Mul(Mul(N rem Mod, ((N-1) rem Mod)), Inv2),

    %% left/right distinct pairs total (choose two positions with different values)
    LeftPairs = Sub(Mul(SL rem Mod, SL rem Mod), SumLSq),
    LeftPairsTot = Mul(LeftPairs, Inv2),

    RightPairs = Sub(Mul(SR rem Mod, SR rem Mod), SumRSq),
    RightPairsTot = Mul(RightPairs, Inv2),

    %% ----- k = 1 (t=0) -----
    Term1 = Mul(LeftPairsTot, RightPairsTot),

    % second term: sum over v of L*R*(SR-R)*(SL-L)
    SecondSum = maps:fold(fun(_Key, _ValCnt, Acc) -> Acc end, 0, #{}), % placeholder
    SecondTerm = compute_second_term(LeftMap, RightMap, Val, SL, SR),

    % third term: ((sum_lr)^2 - sum_lsq_rsq)/2
    DiffLR = Sub(Mul(SumLR rem Mod, SumLR rem Mod), SumLSqRSq),
    ThirdTerm = Mul(DiffLR, Inv2),

    CountK1 = Sub(Add(Term1, ThirdTerm), SecondTerm),

    %% ----- k = 2 (t=1) -----
    % left side extra equal
    PartL = Sub(Mul(RightPairsTot, SL rem Mod),
                Sub(Mul(SR rem Mod, SumLR rem Mod), SumLRCntSq)),
    LeftExtra = Mul(LeftEq rem Mod, PartL),

    % right side extra equal
    PartR = Sub(Mul(LeftPairsTot, SR rem Mod),
                Sub(Mul(SL rem Mod, SumLR rem Mod), SumRLCntSq)),
    RightExtra = Mul(RightEq rem Mod, PartR),

    CountK2 = Add(LeftExtra, RightExtra),

    %% ----- k = 3 (t=2) -----
    CLeq2 = Comb2(LeftEq),
    CReq2 = Comb2(RightEq),

    TermA = Mul(CLeq2, Comb2(SR)),
    TermB = Mul(CReq2, Comb2(SL)),
    TermC = Mul(Mul(LeftEq rem Mod, RightEq rem Mod), Mul(SL rem Mod, SR rem Mod)),

    CountK3 = Add(Add(TermA, TermB), TermC),

    %% ----- k = 4 (t=3) -----
    TermD = Mul(CLeq2, Mul(RightEq rem Mod, SR rem Mod)),
    TermE = Mul(LeftEq rem Mod, Mul(CReq2, SL rem Mod)),

    CountK4 = Add(TermD, TermE),

    %% ----- k = 5 (t=4) -----
    CountK5 = Mul(CLeq2, CReq2),

    Total = (((((CountK1 + CountK2) rem Mod + CountK3) rem Mod
               + CountK4) rem Mod + CountK5) rem Mod),
    Total.

%% Sum of squares of counts excluding a specific value
sum_sq_excluding(Map, Excl) ->
    maps:fold(fun(Key, Cnt, Acc) ->
        if Key =:= Excl -> Acc;
           true -> (Acc + Cnt*Cnt) end
    end, 0, Map).

%% Compute cross aggregates needed for formulas
cross_aggregates(LeftMap, RightMap, Excl) ->
    maps:fold(fun(Key, Lcnt, {SumLR, SumLRCntSq, SumRLCntSq, SumLSqRSq}) ->
        if Key =:= Excl -> {SumLR, SumLRCntSq, SumRLCntSq, SumLSqRSq};
           true ->
               Rcnt = maps:get(Key, RightMap, 0),
               NewSumLR = SumLR + Lcnt * Rcnt,
               NewSumLRCntSq = SumLRCntSq + Lcnt * (Rcnt*Rcnt),
               NewSumRLCntSq = SumRLCntSq + Rcnt * (Lcnt*Lcnt),
               NewSumLSqRSq = SumLSqRSq + (Lcnt*Lcnt) * (Rcnt*Rcnt),
               {NewSumLR, NewSumLRCntSq, NewSumRLCntSq, NewSumLSqRSq}
        end
    end, {0,0,0,0}, LeftMap).

%% Compute second term for k=1: sum over v L*R*(SR-R)*(SL-L)
compute_second_term(LeftMap, RightMap, Excl, SL, SR) ->
    Mod = ?MOD,
    Mul(A,B) -> ((A rem Mod) * (B rem Mod)) rem Mod end,
    Add(A,B) -> (A + B) rem Mod,
    FoldFun = fun(Key, Lcnt, Acc) ->
        if Key =:= Excl -> Acc;
           true ->
               Rcnt = maps:get(Key, RightMap, 0),
               Term = Mul(Mul(Lcnt, Rcnt), Mul(SR - Rcnt, SL - Lcnt)),
               Add(Acc, Term)
        end
    end,
    maps:fold(FoldFun, 0, LeftMap).

%% Combination helper (public for internal use)
Comb2(N) when N < 2 -> 0;
Comb2(N) ->
    Mod = ?MOD,
    Inv2 = ?INV2,
    ((N rem Mod) * ((N-1) rem Mod) rem Mod) * Inv2 rem Mod.
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @mod 1_000_000_007

  defp c2(n) when n < 2, do: 0
  defp c2(n), do: rem(div(n * (n - 1), 2), @mod)

  def subsequences_with_middle_mode(nums) do
    n = length(nums)
    # build right counts
    {right_counts, _} =
      Enum.reduce(nums, {%{}, 0}, fn v, {cnts, _} ->
        Map.update(cnts, v, 1, &(&1 + 1))
      end)

    right_total = n

    # total same-pair count on the right (including all values)
    right_same_pairs =
      Enum.reduce(right_counts, 0, fn {_v, c}, acc -> rem(acc + c2(c), @mod) end)

    left_counts = %{}
    left_total = 0
    left_same_pairs = 0

    ans = 0

    Enum.with_index(nums)
    |> Enum.reduce({ans, left_counts, left_total, left_same_pairs,
                    right_counts, right_total, right_same_pairs},
      fn {v, idx}, {ans_acc,
                     l_cnts, l_tot, l_same,
                     r_cnts, r_tot, r_same} ->

        # remove current element from right side (it becomes the middle)
        cnt_r_v = Map.get(r_cnts, v)
        r_same = rem(r_same - c2(cnt_r_v) + @mod, @mod)
        cnt_r_v = cnt_r_v - 1
        r_cnts = Map.put(r_cnts, v, cnt_r_v)
        r_tot = r_tot - 1
        r_same = rem(r_same + c2(cnt_r_v), @mod)

        l_cnt_v = Map.get(l_cnts, v, 0)

        total_left = l_tot
        total_right = r_tot

        left_nonv = total_left - l_cnt_v
        right_nonv = total_right - cnt_r_v

        # precomputed combos
        c2L = c2(l_cnt_v)
        c2R = c2(cnt_r_v)

        cn2_left_nonv = c2(left_nonv)
        cn2_right_nonv = c2(right_nonv)

        # case count(v)=5
        case5 = rem(c2L * c2R, @mod)

        # case count(v)=4
        term1 = rem(rem(c2L * cnt_r_v, @mod) * right_nonv, @mod)
        term2 = rem(rem(l_cnt_v * c2R, @mod) * left_nonv, @mod)
        case4 = rem(term1 + term2, @mod)

        # case count(v)=3
        t1 = rem(c2L * cn2_right_nonv, @mod)
        t2 = rem(c2R * cn2_left_nonv, @mod)
        t3 = rem(rem(l_cnt_v * cnt_r_v, @mod) * left_nonv, @mod)
        t3 = rem(t3 * right_nonv, @mod)
        case3 = rem(t1 + t2 + t3, @mod)

        # same-pair counts excluding v
        same_nonv_R = rem(r_same - c2(cnt_r_v) + @mod, @mod)
        same_nonv_L = rem(l_same - c2(l_cnt_v) + @mod, @mod)

        # case count(v)=2 : extra v on left side
        case2_leftV =
          Enum.reduce(l_cnts, 0, fn {x, cntLx}, acc ->
            if x != v do
              cntRx = Map.get(r_cnts, x, 0)
              nr_prime = right_nonv - cntRx
              term_a = c2(nr_prime)

              sub_same = rem(same_nonv_R - c2(cntRx) + @mod, @mod)
              f = rem(term_a - sub_same + @mod, @mod)
              rem(acc + rem(cntLx * f, @mod), @mod)
            else
              acc
            end
          end)

        # extra v on right side
        case2_rightV =
          Enum.reduce(r_cnts, 0, fn {x, cntRx}, acc ->
            if x != v do
              cntLx = Map.get(l_cnts, x, 0)
              nl_prime = left_nonv - cntLx
              term_a = c2(nl_prime)

              sub_same = rem(same_nonv_L - c2(cntLx) + @mod, @mod)
              f = rem(term_a - sub_same + @mod, @mod)
              rem(acc + rem(cntRx * f, @mod), @mod)
            else
              acc
            end
          end)

        case2 = rem(case2_leftV + case2_rightV, @mod)

        ans_new = rem(ans_acc + case5 + case4 + case3 + case2, @mod)

        # add current element to left side for next iteration
        cnt_l_v = Map.get(l_cnts, v, 0)
        l_same = rem(l_same - c2(cnt_l_v) + @mod, @mod)
        cnt_l_v = cnt_l_v + 1
        l_cnts = Map.put(l_cnts, v, cnt_l_v)
        l_tot = l_tot + 1
        l_same = rem(l_same + c2(cnt_l_v), @mod)

        {ans_new,
         l_cnts, l_tot, l_same,
         r_cnts, r_tot, r_same}
      end)
    |> elem(0)
  end
end
```
