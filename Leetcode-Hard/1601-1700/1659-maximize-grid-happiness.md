# 1659. Maximize Grid Happiness

## Cpp

```cpp
class Solution {
public:
    int getMaxGridHappiness(int m, int n, int introvertsCount, int extrovertsCount) {
        vector<int> pow3(n+1,1);
        for(int i=1;i<=n;i++) pow3[i]=pow3[i-1]*3;
        const int MAXMASK = pow3[n];
        unordered_map<long long,int> memo;
        function<int(int,int,int,int,int)> dfs = [&](int pos,int prevMask,int curMask,int iRem,int eRem)->int{
            if(pos==m*n) return 0;
            long long key = (((((long long)pos*MAXMASK)+prevMask)*MAXMASK + curMask)*(7LL)+(iRem))*7LL + eRem;
            auto it=memo.find(key);
            if(it!=memo.end()) return it->second;
            int r=pos/n, c=pos%n;
            int up = (prevMask/pow3[c])%3; // state of cell above
            int left = (c==0?0: (curMask/pow3[c-1])%3); // state of left cell in current row
            int best=0;
            // option 0: leave empty
            {
                int nPrevMask = prevMask;
                int nCurMask = curMask; // set digit to 0 (already zero)
                if(c==n-1){
                    nPrevMask = nCurMask;
                    nCurMask = 0;
                }
                best = max(best, dfs(pos+1,nPrevMask,nCurMask,iRem,eRem));
            }
            // introvert
            if(iRem>0){
                int add=120;
                int neighborCnt = (up?1:0)+(left?1:0);
                add += -30*neighborCnt;
                if(up) add += (up==1?-30:20);
                if(left) add += (left==1?-30:20);
                int nPrevMask=prevMask;
                int nCurMask = curMask + (1)*pow3[c]; // set digit to 1
                if(c==n-1){
                    nPrevMask = nCurMask;
                    nCurMask = 0;
                }
                best = max(best, add + dfs(pos+1,nPrevMask,nCurMask,iRem-1,eRem));
            }
            // extrovert
            if(eRem>0){
                int add=40;
                int neighborCnt = (up?1:0)+(left?1:0);
                add += 20*neighborCnt;
                if(up) add += (up==1?-30:20);
                if(left) add += (left==1?-30:20);
                int nPrevMask=prevMask;
                int nCurMask = curMask + (2)*pow3[c]; // set digit to 2
                if(c==n-1){
                    nPrevMask = nCurMask;
                    nCurMask = 0;
                }
                best = max(best, add + dfs(pos+1,nPrevMask,nCurMask,iRem,eRem-1));
            }
            memo[key]=best;
            return best;
        };
        return dfs(0,0,0,introvertsCount,extrovertsCount);
    }
};
```

## Java

```java
class Solution {
    public int getMaxGridHappiness(int m, int n, int introvertsCount, int extrovertsCount) {
        int totalMasks = (int) Math.pow(3, n);
        int[] pow3 = new int[n + 1];
        pow3[0] = 1;
        for (int i = 1; i <= n; ++i) pow3[i] = pow3[i - 1] * 3;

        // decode masks
        int[][] maskTypes = new int[totalMasks][n];
        int[] introMaskCnt = new int[totalMasks];
        int[] extroMaskCnt = new int[totalMasks];
        int[] rowScore = new int[totalMasks];

        // pair score matrix
        int[][] pair = new int[3][3];
        for (int a = 0; a < 3; ++a) {
            for (int b = 0; b < 3; ++b) {
                if (a == 0 || b == 0) {
                    pair[a][b] = 0;
                } else {
                    int deltaA = (a == 1) ? -30 : 20;
                    int deltaB = (b == 1) ? -30 : 20;
                    pair[a][b] = deltaA + deltaB;
                }
            }
        }

        for (int mask = 0; mask < totalMasks; ++mask) {
            int x = mask;
            int base = 0;
            for (int col = 0; col < n; ++col) {
                int t = x % 3;
                maskTypes[mask][col] = t;
                if (t == 1) {
                    introMaskCnt[mask]++;
                    base += 120;
                } else if (t == 2) {
                    extroMaskCnt[mask]++;
                    base += 40;
                }
                x /= 3;
            }
            int leftRight = 0;
            for (int col = 0; col < n - 1; ++col) {
                leftRight += pair[maskTypes[mask][col]][maskTypes[mask][col + 1]];
            }
            rowScore[mask] = base + leftRight;
        }

        // up-down adjacency scores between masks
        int[][] upScore = new int[totalMasks][totalMasks];
        for (int pm = 0; pm < totalMasks; ++pm) {
            for (int cm = 0; cm < totalMasks; ++cm) {
                int sum = 0;
                for (int col = 0; col < n; ++col) {
                    sum += pair[maskTypes[pm][col]][maskTypes[cm][col]];
                }
                upScore[pm][cm] = sum;
            }
        }

        final int NEG = -1_000_000_000;
        int[][][] dpPrev = new int[totalMasks][introvertsCount + 1][extrovertsCount + 1];
        int[][][] dpCurr = new int[totalMasks][introvertsCount + 1][extrovertsCount + 1];

        for (int i = 0; i < totalMasks; ++i) {
            for (int a = 0; a <= introvertsCount; ++a) {
                for (int b = 0; b <= extrovertsCount; ++b) {
                    dpPrev[i][a][b] = NEG;
                }
            }
        }
        dpPrev[0][introvertsCount][extrovertsCount] = 0;

        for (int row = 0; row < m; ++row) {
            // reset dpCurr
            for (int i = 0; i < totalMasks; ++i) {
                for (int a = 0; a <= introvertsCount; ++a) {
                    for (int b = 0; b <= extrovertsCount; ++b) {
                        dpCurr[i][a][b] = NEG;
                    }
                }
            }

            for (int prevMask = 0; prevMask < totalMasks; ++prevMask) {
                for (int iLeft = 0; iLeft <= introvertsCount; ++iLeft) {
                    for (int eLeft = 0; eLeft <= extrovertsCount; ++eLeft) {
                        int curVal = dpPrev[prevMask][iLeft][eLeft];
                        if (curVal == NEG) continue;
                        for (int curMask = 0; curMask < totalMasks; ++curMask) {
                            int ic = introMaskCnt[curMask];
                            int ec = extroMaskCnt[curMask];
                            if (ic > iLeft || ec > eLeft) continue;
                            int newI = iLeft - ic;
                            int newE = eLeft - ec;
                            int val = curVal + rowScore[curMask] + upScore[prevMask][curMask];
                            if (val > dpCurr[curMask][newI][newE]) {
                                dpCurr[curMask][newI][newE] = val;
                            }
                        }
                    }
                }
            }

            // swap
            int[][][] tmp = dpPrev;
            dpPrev = dpCurr;
            dpCurr = tmp;
        }

        int ans = 0;
        for (int mask = 0; mask < totalMasks; ++mask) {
            for (int i = 0; i <= introvertsCount; ++i) {
                for (int e = 0; e <= extrovertsCount; ++e) {
                    ans = Math.max(ans, dpPrev[mask][i][e]);
                }
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def getMaxGridHappiness(self, m, n, introvertsCount, extrovertsCount):
        """
        :type m: int
        :type n: int
        :type introvertsCount: int
        :type extrovertsCount: int
        :rtype: int
        """
        maxMask = 3 ** n
        delta = [0, -30, 20]  # effect per neighbor for each type (0 empty)
        base_hap = [0] * maxMask          # sum of individual happiness
        intro_cnt = [0] * maxMask
        extro_cnt = [0] * maxMask
        intra_row = [0] * maxMask         # happiness from left-right adjacencies within the row
        types = [[0] * n for _ in range(maxMask)]

        for mask in range(maxMask):
            tmp = mask
            cnt_i = cnt_e = 0
            hap = 0
            arr = []
            for col in range(n):
                t = tmp % 3
                tmp //= 3
                arr.append(t)
                if t == 1:
                    cnt_i += 1
                    hap += 120
                elif t == 2:
                    cnt_e += 1
                    hap += 40
            types[mask] = arr
            intro_cnt[mask] = cnt_i
            extro_cnt[mask] = cnt_e
            base_hap[mask] = hap

            # intra-row adjacency
            adj = 0
            for col in range(n - 1):
                a, b = arr[col], arr[col + 1]
                if a:
                    adj += delta[a]
                if b:
                    adj += delta[b]
            intra_row[mask] = adj

        # precompute vertical adjacency between two masks
        vert_adj = [[0] * maxMask for _ in range(maxMask)]
        for prev in range(maxMask):
            tp = types[prev]
            for cur in range(maxMask):
                tc = types[cur]
                add = 0
                for col in range(n):
                    a, b = tp[col], tc[col]
                    if a:
                        add += delta[a]
                    if b:
                        add += delta[b]
                vert_adj[prev][cur] = add

        # DP: state -> max happiness
        # key: (prevMask, remainingIntroverts, remainingExtroverts)
        dp = {(0, introvertsCount, extrovertsCount): 0}
        for _ in range(m):
            ndp = {}
            for (prevMask, iRem, eRem), val in dp.items():
                for curMask in range(maxMask):
                    ic = intro_cnt[curMask]
                    ec = extro_cnt[curMask]
                    if ic > iRem or ec > eRem:
                        continue
                    new_i = iRem - ic
                    new_e = eRem - ec
                    added = base_hap[curMask] + intra_row[curMask] + vert_adj[prevMask][curMask]
                    new_val = val + added
                    key = (curMask, new_i, new_e)
                    if key not in ndp or ndp[key] < new_val:
                        ndp[key] = new_val
            dp = ndp

        return max(dp.values())
```

## Python3

```python
class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        # mapping of pair happiness (total change for both persons)
        def pair_hap(a: int, b: int) -> int:
            if a == 0 or b == 0:
                return 0
            if a == 1 and b == 1:      # introvert-introvert
                return -60
            if (a == 1 and b == 2) or (a == 2 and b == 1):  # introvert-extrovert
                return -10
            # both extroverts
            return 40

        total_masks = 3 ** n
        types_per_mask = [None] * total_masks
        intro_cnt = [0] * total_masks
        extro_cnt = [0] * total_masks
        internal_hap = [0] * total_masks

        # precompute mask details
        for mask in range(total_masks):
            cur = mask
            lst = []
            ic = ec = 0
            base = 0
            for _ in range(n):
                t = cur % 3
                lst.append(t)
                if t == 1:
                    ic += 1
                    base += 120
                elif t == 2:
                    ec += 1
                    base += 40
                cur //= 3
            types_per_mask[mask] = lst
            intro_cnt[mask] = ic
            extro_cnt[mask] = ec

            # left-right interactions within the row
            intra = 0
            for j in range(1, n):
                intra += pair_hap(lst[j], lst[j - 1])
            internal_hap[mask] = base + intra

        # precompute vertical interactions between rows
        vert = [[0] * total_masks for _ in range(total_masks)]
        for prev in range(total_masks):
            p_lst = types_per_mask[prev]
            for cur in range(total_masks):
                c_lst = types_per_mask[cur]
                v = 0
                for j in range(n):
                    v += pair_hap(c_lst[j], p_lst[j])
                vert[prev][cur] = v

        # DP: state -> max happiness
        dp = {(0, 0, 0): 0}   # (prev_mask, used_introverts, used_extroverts)
        for _ in range(m):
            ndp = {}
            for (pmask, i_used, e_used), val in dp.items():
                for cmask in range(total_masks):
                    ic = intro_cnt[cmask]
                    ec = extro_cnt[cmask]
                    ni = i_used + ic
                    ne = e_used + ec
                    if ni > introvertsCount or ne > extrovertsCount:
                        continue
                    new_val = val + internal_hap[cmask] + vert[pmask][cmask]
                    key = (cmask, ni, ne)
                    if key not in ndp or new_val > ndp[key]:
                        ndp[key] = new_val
            dp = ndp

        return max(dp.values())
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

inline int pairContribution(int a, int b) {
    int cur = (a == 1) ? -30 : (a == 2 ? 20 : 0);
    int nb  = (b == 1) ? -30 : (b == 2 ? 20 : 0);
    return cur + nb;
}

int getMaxGridHappiness(int m, int n, int introvertsCount, int extrovertsCount) {
    int maxMask = 1;
    for (int i = 0; i < n; ++i) maxMask *= 3;          // 3^n
    const int INF_NEG = -1e9;

    vector<int> cntI(maxMask), cntE(maxMask), baseHap(maxMask), internalAdd(maxMask);
    for (int mask = 0; mask < maxMask; ++mask) {
        int tmp = mask, prev = 0;
        int ci = 0, ce = 0, bh = 0, add = 0;
        for (int col = 0; col < n; ++col) {
            int cur = tmp % 3;
            tmp /= 3;
            if (cur == 1) { ++ci; bh += 120; }
            else if (cur == 2) { ++ce; bh += 40; }

            if (col > 0 && prev != 0 && cur != 0)
                add += pairContribution(prev, cur);
            prev = cur;
        }
        cntI[mask] = ci;
        cntE[mask] = ce;
        baseHap[mask] = bh;
        internalAdd[mask] = add;
    }

    vector<vector<int>> upAdj(maxMask, vector<int>(maxMask, 0));
    for (int prevMask = 0; prevMask < maxMask; ++prevMask) {
        int tmpPrev = prevMask;
        int upTypes[5];
        for (int col = 0; col < n; ++col) { upTypes[col] = tmpPrev % 3; tmpPrev /= 3; }
        for (int curMask = 0; curMask < maxMask; ++curMask) {
            int tmpCur = curMask, add = 0;
            for (int col = 0; col < n; ++col) {
                int cur = tmpCur % 3;
                tmpCur /= 3;
                int up = upTypes[col];
                if (cur != 0 && up != 0) add += pairContribution(cur, up);
            }
            upAdj[prevMask][curMask] = add;
        }
    }

    static int dpPrev[243][7][7];
    static int dpCurr[243][7][7];
    for (int mask = 0; mask < maxMask; ++mask)
        for (int i = 0; i <= introvertsCount; ++i)
            for (int e = 0; e <= extrovertsCount; ++e) {
                dpPrev[mask][i][e] = INF_NEG;
                dpCurr[mask][i][e] = INF_NEG;
            }
    dpPrev[0][0][0] = 0;

    for (int row = 0; row < m; ++row) {
        for (int mask = 0; mask < maxMask; ++mask)
            for (int i = 0; i <= introvertsCount; ++i)
                for (int e = 0; e <= extrovertsCount; ++e)
                    dpCurr[mask][i][e] = INF_NEG;

        for (int prevMask = 0; prevMask < maxMask; ++prevMask) {
            for (int i = 0; i <= introvertsCount; ++i) {
                for (int e = 0; e <= extrovertsCount; ++e) {
                    int curVal = dpPrev[prevMask][i][e];
                    if (curVal == INF_NEG) continue;
                    for (int curMask = 0; curMask < maxMask; ++curMask) {
                        int ni = i + cntI[curMask];
                        int ne = e + cntE[curMask];
                        if (ni > introvertsCount || ne > extrovertsCount) continue;
                        int added = baseHap[curMask] + internalAdd[curMask] + upAdj[prevMask][curMask];
                        int &ref = dpCurr[curMask][ni][ne];
                        int cand = curVal + added;
                        if (cand > ref) ref = cand;
                    }
                }
            }
        }

        for (int mask = 0; mask < maxMask; ++mask)
            for (int i = 0; i <= introvertsCount; ++i)
                for (int e = 0; e <= extrovertsCount; ++e)
                    dpPrev[mask][i][e] = dpCurr[mask][i][e];
    }

    int ans = 0;
    for (int mask = 0; mask < maxMask; ++mask)
        for (int i = 0; i <= introvertsCount; ++i)
            for (int e = 0; e <= extrovertsCount; ++e)
                ans = max(ans, dpPrev[mask][i][e]);
    return ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int GetMaxGridHappiness(int m, int n, int introvertsCount, int extrovertsCount) {
        int maxMask = (int)Math.Pow(3, n);
        int[][] state = new int[maxMask][];
        int[] introCnt = new int[maxMask];
        int[] extroCnt = new int[maxMask];
        int[] internalHap = new int[maxMask];

        // base happiness
        int[] baseHap = new int[3];
        baseHap[1] = 120; // introvert
        baseHap[2] = 40;  // extrovert

        // delta when a person of type a has neighbor of type b (effect on a)
        int[,] delta = new int[3, 3];
        delta[1, 1] = -30;
        delta[1, 2] = -30;
        delta[2, 1] = 20;
        delta[2, 2] = 20;

        // pair effect (both sides)
        int[,] pairEffect = new int[3, 3];
        for (int a = 0; a <= 2; a++) {
            for (int b = 0; b <= 2; b++) {
                if (a == 0 || b == 0) continue;
                pairEffect[a, b] = delta[a, b] + delta[b, a];
            }
        }

        // precompute state arrays and internal happiness
        for (int mask = 0; mask < maxMask; mask++) {
            int[] arr = new int[n];
            int tmp = mask;
            for (int col = 0; col < n; col++) {
                arr[col] = tmp % 3;
                tmp /= 3;
            }
            state[mask] = arr;

            int prev = 0;
            int internal = 0;
            int ic = 0, ec = 0;
            for (int col = 0; col < n; col++) {
                int cur = arr[col];
                if (cur == 1) ic++;
                else if (cur == 2) ec++;

                if (cur != 0) {
                    internal += baseHap[cur];
                    if (prev != 0) internal += pairEffect[cur, prev];
                }
                prev = cur;
            }
            introCnt[mask] = ic;
            extroCnt[mask] = ec;
            internalHap[mask] = internal;
        }

        // precompute cross happiness between rows
        int[,] cross = new int[maxMask, maxMask];
        for (int pm = 0; pm < maxMask; pm++) {
            int[] pArr = state[pm];
            for (int cm = 0; cm < maxMask; cm++) {
                int[] cArr = state[cm];
                int sum = 0;
                for (int col = 0; col < n; col++) {
                    int up = pArr[col];
                    int cur = cArr[col];
                    if (up != 0 && cur != 0) {
                        sum += pairEffect[cur, up];
                    }
                }
                cross[pm, cm] = sum;
            }
        }

        const int NEG_INF = -1000000000;
        int iMax = introvertsCount;
        int eMax = extrovertsCount;

        int[,,] dpPrev = new int[maxMask, iMax + 1, eMax + 1];
        for (int mask = 0; mask < maxMask; mask++)
            for (int i = 0; i <= iMax; i++)
                for (int e = 0; e <= eMax; e++)
                    dpPrev[mask, i, e] = NEG_INF;

        dpPrev[0, introvertsCount, extrovertsCount] = 0;

        for (int row = 0; row < m; row++) {
            int[,,] dpNext = new int[maxMask, iMax + 1, eMax + 1];
            for (int mask = 0; mask < maxMask; mask++)
                for (int i = 0; i <= iMax; i++)
                    for (int e = 0; e <= eMax; e++)
                        dpNext[mask, i, e] = NEG_INF;

            for (int prevMask = 0; prevMask < maxMask; prevMask++) {
                for (int iLeft = 0; iLeft <= iMax; iLeft++) {
                    for (int eLeft = 0; eLeft <= eMax; eLeft++) {
                        int curVal = dpPrev[prevMask, iLeft, eLeft];
                        if (curVal == NEG_INF) continue;
                        for (int curMask = 0; curMask < maxMask; curMask++) {
                            int ic = introCnt[curMask];
                            int ec = extroCnt[curMask];
                            if (ic > iLeft || ec > eLeft) continue;
                            int newVal = curVal + internalHap[curMask] + cross[prevMask, curMask];
                            int ni = iLeft - ic;
                            int ne = eLeft - ec;
                            if (newVal > dpNext[curMask, ni, ne]) {
                                dpNext[curMask, ni, ne] = newVal;
                            }
                        }
                    }
                }
            }

            dpPrev = dpNext;
        }

        int answer = 0;
        for (int mask = 0; mask < maxMask; mask++) {
            for (int i = 0; i <= iMax; i++) {
                for (int e = 0; e <= eMax; e++) {
                    if (dpPrev[mask, i, e] > answer) answer = dpPrev[mask, i, e];
                }
            }
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} m
 * @param {number} n
 * @param {number} introvertsCount
 * @param {number} extrovertsCount
 * @return {number}
 */
var getMaxGridHappiness = function(m, n, introvertsCount, extrovertsCount) {
    const totalMasks = Math.pow(3, n);
    const pow3 = new Array(n);
    pow3[0] = 1;
    for (let i = 1; i < n; ++i) pow3[i] = pow3[i - 1] * 3;

    const base = [0, 120, 40];
    const effect = [0, -30, 20]; // introvert loses 30 per neighbor, extrovert gains 20

    const cntI = new Array(totalMasks).fill(0);
    const cntE = new Array(totalMasks).fill(0);
    const intra = new Array(totalMasks).fill(0);
    const statesCache = new Array(totalMasks);

    // decode masks and precompute counts & intra-row happiness
    for (let mask = 0; mask < totalMasks; ++mask) {
        let arr = new Array(n);
        let tmp = mask;
        let iCnt = 0, eCnt = 0, val = 0;
        for (let col = 0; col < n; ++col) {
            const s = tmp % 3;
            arr[col] = s;
            if (s === 1) iCnt++;
            else if (s === 2) eCnt++;
            val += base[s];
            tmp = Math.floor(tmp / 3);
        }
        // horizontal neighbor contributions
        for (let col = 1; col < n; ++col) {
            const left = arr[col - 1], right = arr[col];
            if (left !== 0 && right !== 0) {
                val += effect[left] + effect[right];
            }
        }
        cntI[mask] = iCnt;
        cntE[mask] = eCnt;
        intra[mask] = val;
        statesCache[mask] = arr; // keep for vertical calc later
    }

    // precompute vertical contributions between any two masks
    const vert = Array.from({ length: totalMasks }, () => new Array(totalMasks).fill(0));
    for (let up = 0; up < totalMasks; ++up) {
        const upArr = statesCache[up];
        for (let down = 0; down < totalMasks; ++down) {
            const downArr = statesCache[down];
            let add = 0;
            for (let col = 0; col < n; ++col) {
                const a = upArr[col], b = downArr[col];
                if (a !== 0 && b !== 0) {
                    add += effect[a] + effect[b];
                }
            }
            vert[up][down] = add;
        }
    }

    const INF_NEG = -1e9;

    // dpPrev[mask][i][e]
    let dpPrev = Array.from({ length: totalMasks }, () =>
        Array.from({ length: introvertsCount + 1 }, () => new Array(extrovertsCount + 1).fill(INF_NEG))
    );

    // first row initialization
    for (let mask = 0; mask < totalMasks; ++mask) {
        const iCnt = cntI[mask];
        const eCnt = cntE[mask];
        if (iCnt <= introvertsCount && eCnt <= extrovertsCount) {
            dpPrev[mask][iCnt][eCnt] = intra[mask];
        }
    }

    // process remaining rows
    for (let row = 1; row < m; ++row) {
        let dpCurr = Array.from({ length: totalMasks }, () =>
            Array.from({ length: introvertsCount + 1 }, () => new Array(extrovertsCount + 1).fill(INF_NEG))
        );

        for (let upMask = 0; upMask < totalMasks; ++upMask) {
            const dpUpMask = dpPrev[upMask];
            for (let iUsed = 0; iUsed <= introvertsCount; ++iUsed) {
                const dpRowI = dpUpMask[iUsed];
                for (let eUsed = 0; eUsed <= extrovertsCount; ++eUsed) {
                    const curVal = dpRowI[eUsed];
                    if (curVal === INF_NEG) continue;
                    for (let downMask = 0; downMask < totalMasks; ++downMask) {
                        const newI = iUsed + cntI[downMask];
                        const newE = eUsed + cntE[downMask];
                        if (newI > introvertsCount || newE > extrovertsCount) continue;
                        const val = curVal + intra[downMask] + vert[upMask][downMask];
                        if (val > dpCurr[downMask][newI][newE]) {
                            dpCurr[downMask][newI][newE] = val;
                        }
                    }
                }
            }
        }

        dpPrev = dpCurr;
    }

    // answer: max over all masks and used counts
    let ans = 0;
    for (let mask = 0; mask < totalMasks; ++mask) {
        const dpMask = dpPrev[mask];
        for (let i = 0; i <= introvertsCount; ++i) {
            for (let e = 0; e <= extrovertsCount; ++e) {
                if (dpMask[i][e] > ans) ans = dpMask[i][e];
            }
        }
    }
    return ans;
};
```

## Typescript

```typescript
function getMaxGridHappiness(m: number, n: number, introvertsCount: number, extrovertsCount: number): number {
    const total = m * n;
    const pow3 = new Array(n).fill(0);
    pow3[0] = 1;
    for (let i = 1; i < n; ++i) pow3[i] = pow3[i - 1] * 3;
    const maxMask = Math.pow(3, n);

    const base = [0, 120, 40];
    const pairScore = [
        [0, 0, 0],
        [0, -60, -10],
        [0, -10, 40],
    ]; // index by type (0 empty)

    const memo = new Map<number, number>();

    function dfs(pos: number, mask: number, iLeft: number, eLeft: number, left: number): number {
        if (pos === total) return 0;
        const key = (((((pos * maxMask + mask) * 7 + iLeft) * 7 + eLeft) * 3) + left);
        if (memo.has(key)) return memo.get(key)!;

        const col = pos % n;
        const up = Math.floor(mask / pow3[col]) % 3;

        let best = dfs(pos + 1, mask - up * pow3[col], iLeft, eLeft, col === n - 1 ? 0 : left); // place empty

        for (let cur = 1; cur <= 2; ++cur) {
            if (cur === 1 && iLeft === 0) continue;
            if (cur === 2 && eLeft === 0) continue;

            const newMask = mask - up * pow3[col] + cur * pow3[col];
            let delta = base[cur];
            if (up !== 0) delta += pairScore[cur][up];
            if (left !== 0) delta += pairScore[cur][left];

            const nextLeft = (col === n - 1) ? 0 : cur;
            const cand = delta + dfs(pos + 1, newMask,
                iLeft - (cur === 1 ? 1 : 0),
                eLeft - (cur === 2 ? 1 : 0),
                nextLeft);
            if (cand > best) best = cand;
        }

        memo.set(key, best);
        return best;
    }

    // start with empty mask
    const initMask = 0;
    return dfs(0, initMask, introvertsCount, extrovertsCount, 0);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $m
     * @param Integer $n
     * @param Integer $introvertsCount
     * @param Integer $extrovertsCount
     * @return Integer
     */
    function getMaxGridHappiness($m, $n, $introvertsCount, $extrovertsCount) {
        $totalStates = 1;
        for ($i = 0; $i < $n; $i++) $totalStates *= 3; // 3^n

        // precompute state info
        $stateRows = [];
        $cntIntro = array_fill(0, $totalStates, 0);
        $cntExtro = array_fill(0, $totalStates, 0);
        $rowScore = array_fill(0, $totalStates, 0);

        $baseH = [0 => 0, 1 => 120, 2 => 40];
        $effect = [0 => 0, 1 => -30, 2 => 20];

        for ($s = 0; $s < $totalStates; $s++) {
            $tmp = $s;
            $row = [];
            $score = 0;
            $intro = 0;
            $extro = 0;
            for ($c = 0; $c < $n; $c++) {
                $cell = $tmp % 3;
                $tmp = intdiv($tmp, 3);
                $row[$c] = $cell;
                if ($cell != 0) {
                    $score += $baseH[$cell];
                    if ($cell == 1) $intro++;
                    else $extro++;
                }
            }
            // left neighbor interactions
            for ($c = 1; $c < $n; $c++) {
                $a = $row[$c - 1];
                $b = $row[$c];
                if ($a != 0 && $b != 0) {
                    $score += $effect[$a] + $effect[$b];
                }
            }
            $stateRows[$s] = $row;
            $cntIntro[$s] = $intro;
            $cntExtro[$s] = $extro;
            $rowScore[$s] = $score;
        }

        // precompute up interactions between two rows
        $upScore = array_fill(0, $totalStates, array_fill(0, $totalStates, 0));
        for ($p = 0; $p < $totalStates; $p++) {
            $prevRow = $stateRows[$p];
            for ($c = 0; $c < $totalStates; $c++) {
                $curRow = $stateRows[$c];
                $add = 0;
                for ($col = 0; $col < $n; $col++) {
                    $a = $prevRow[$col];
                    $b = $curRow[$col];
                    if ($a != 0 && $b != 0) {
                        $add += $effect[$a] + $effect[$b];
                    }
                }
                $upScore[$p][$c] = $add;
            }
        }

        // DP initialization
        $dpPrev = [];
        $dpPrev[0][$introvertsCount][$extrovertsCount] = 0;

        for ($rowIdx = 0; $rowIdx < $m; $rowIdx++) {
            $dpNext = [];
            foreach ($dpPrev as $prevState => $iMap) {
                foreach ($iMap as $iRem => $eMap) {
                    foreach ($eMap as $eRem => $val) {
                        for ($curState = 0; $curState < $totalStates; $curState++) {
                            $needI = $cntIntro[$curState];
                            $needE = $cntExtro[$curState];
                            if ($needI > $iRem || $needE > $eRem) continue;
                            $newVal = $val + $rowScore[$curState] + $upScore[$prevState][$curState];
                            $ni = $iRem - $needI;
                            $ne = $eRem - $needE;
                            if (!isset($dpNext[$curState][$ni][$ne]) || $dpNext[$curState][$ni][$ne] < $newVal) {
                                $dpNext[$curState][$ni][$ne] = $newVal;
                            }
                        }
                    }
                }
            }
            $dpPrev = $dpNext;
        }

        $ans = 0;
        foreach ($dpPrev as $iMap) {
            foreach ($iMap as $eMap) {
                foreach ($eMap as $val) {
                    if ($val > $ans) $ans = $val;
                }
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    func getMaxGridHappiness(_ m: Int, _ n: Int, _ introvertsCount: Int, _ extrovertsCount: Int) -> Int {
        let maxI = introvertsCount
        let maxE = extrovertsCount
        
        // Precompute powers of 3 and total mask count
        var pow3 = 1
        for _ in 0..<n { pow3 *= 3 }
        let maskCount = pow3
        
        // Helper to compute pair effect
        func pairEffect(_ a: Int, _ b: Int) -> Int {
            if a == 0 || b == 0 { return 0 }
            if a == 1 && b == 1 { return -60 }   // introvert-introvert
            if a == 2 && b == 2 { return 40 }    // extrovert-extrovert
            return -10                           // introvert-extrovert or vice versa
        }
        
        // Precompute per mask: counts, intra-row happiness, and cell types
        var cntI = [Int](repeating: 0, count: maskCount)
        var cntE = [Int](repeating: 0, count: maskCount)
        var intraRow = [Int](repeating: 0, count: maskCount)
        var types = [[Int]](repeating: [], count: maskCount) // each is length n
        
        for mask in 0..<maskCount {
            var temp = mask
            var arr = [Int]()
            var cI = 0, cE = 0, base = 0, horiz = 0
            for _ in 0..<n {
                let d = temp % 3
                arr.append(d)
                if d == 1 { cI += 1; base += 120 }
                else if d == 2 { cE += 1; base += 40 }
                temp /= 3
            }
            for j in 1..<n {
                horiz += pairEffect(arr[j], arr[j-1])
            }
            cntI[mask] = cI
            cntE[mask] = cE
            intraRow[mask] = base + horiz
            types[mask] = arr
        }
        
        // DP arrays: dpPrev[mask][i][e]
        let INF = -1_000_000_000
        var dpPrev = Array(repeating: Array(repeating: Array(repeating: INF, count: maxE+1), count: maxI+1), count: maskCount)
        dpPrev[0][0][0] = 0
        
        // Iterate over rows
        for _ in 0..<m {
            var dpNext = Array(repeating: Array(repeating: Array(repeating: INF, count: maxE+1), count: maxI+1), count: maskCount)
            for prevMask in 0..<maskCount {
                let prevTypes = types[prevMask]
                for iUsed in 0...maxI {
                    for eUsed in 0...maxE {
                        let curVal = dpPrev[prevMask][iUsed][eUsed]
                        if curVal == INF { continue }
                        // Try all current row masks
                        for curMask in 0..<maskCount {
                            let addI = cntI[curMask]
                            let addE = cntE[curMask]
                            let newI = iUsed + addI
                            let newE = eUsed + addE
                            if newI > maxI || newE > maxE { continue }
                            
                            // vertical contribution with previous row
                            var vert = 0
                            let curTypes = types[curMask]
                            for col in 0..<n {
                                vert += pairEffect(curTypes[col], prevTypes[col])
                            }
                            
                            let added = intraRow[curMask] + vert
                            let newVal = curVal + added
                            if newVal > dpNext[curMask][newI][newE] {
                                dpNext[curMask][newI][newE] = newVal
                            }
                        }
                    }
                }
            }
            dpPrev = dpNext
        }
        
        // Find maximum over all states
        var answer = 0
        for mask in 0..<maskCount {
            for i in 0...maxI {
                for e in 0...maxE {
                    let val = dpPrev[mask][i][e]
                    if val > answer { answer = val }
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
    fun getMaxGridHappiness(m: Int, n: Int, introvertsCount: Int, extrovertsCount: Int): Int {
        var states = 1
        repeat(n) { states *= 3 } // 3^n possible masks per row

        val types = Array(states) { IntArray(n) }
        val introCnt = IntArray(states)
        val extroCnt = IntArray(states)
        val rowScore = IntArray(states)
        val effect = intArrayOf(0, -30, 20)

        for (mask in 0 until states) {
            var tmp = mask
            var base = 0
            var intro = 0
            var extro = 0
            for (c in 0 until n) {
                val t = tmp % 3
                types[mask][c] = t
                when (t) {
                    1 -> { base += 120; intro++ }
                    2 -> { base += 40; extro++ }
                }
                tmp /= 3
            }
            var internal = 0
            for (c in 0 until n - 1) {
                val a = types[mask][c]
                val b = types[mask][c + 1]
                if (a != 0 && b != 0) {
                    internal += effect[a] + effect[b]
                }
            }
            introCnt[mask] = intro
            extroCnt[mask] = extro
            rowScore[mask] = base + internal
        }

        // vertical adjacency contributions between two consecutive rows
        val vert = Array(states) { IntArray(states) }
        for (prev in 0 until states) {
            for (cur in 0 until states) {
                var sum = 0
                for (c in 0 until n) {
                    val p = types[prev][c]
                    val q = types[cur][c]
                    if (p != 0 && q != 0) {
                        sum += effect[p] + effect[q]
                    }
                }
                vert[prev][cur] = sum
            }
        }

        val NEG = -1_000_000_000
        var dpPrev = Array(introvertsCount + 1) { Array(extrovertsCount + 1) { IntArray(states) { NEG } } }
        dpPrev[0][0][0] = 0

        repeat(m) {
            val dpNext = Array(introvertsCount + 1) { Array(extrovertsCount + 1) { IntArray(states) { NEG } } }
            for (i in 0..introvertsCount) {
                for (e in 0..extrovertsCount) {
                    for (prevMask in 0 until states) {
                        val curVal = dpPrev[i][e][prevMask]
                        if (curVal == NEG) continue
                        for (curMask in 0 until states) {
                            val ic = introCnt[curMask]
                            val ec = extroCnt[curMask]
                            val ni = i + ic
                            val ne = e + ec
                            if (ni > introvertsCount || ne > extrovertsCount) continue
                            val added = rowScore[curMask] + vert[prevMask][curMask]
                            val newVal = curVal + added
                            if (newVal > dpNext[ni][ne][curMask]) {
                                dpNext[ni][ne][curMask] = newVal
                            }
                        }
                    }
                }
            }
            dpPrev = dpNext
        }

        var ans = 0
        for (i in 0..introvertsCount) {
            for (e in 0..extrovertsCount) {
                for (mask in 0 until states) {
                    val v = dpPrev[i][e][mask]
                    if (v > ans) ans = v
                }
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int getMaxGridHappiness(int m, int n, int introvertsCount, int extrovertsCount) {
    const int INF = -1000000000;
    // Precompute powers of 3
    List<int> pow3 = List.filled(n + 1, 1);
    for (int i = 1; i <= n; ++i) pow3[i] = pow3[i - 1] * 3;
    int maxMask = pow3[n]; // 3^n

    // Base happiness and effect per neighbor
    List<int> base = [0, 120, 40];
    List<List<int>> effect = [
      [0, 0, 0],
      [0, -30, -30], // introvert affected by any neighbor: -30
      [0, 20, 20]   // extrovert affected by any neighbor: +20
    ];

    // Count introverts and extroverts in each mask
    List<int> cntIntro = List.filled(maxMask, 0);
    List<int> cntExtro = List.filled(maxMask, 0);
    for (int mask = 0; mask < maxMask; ++mask) {
      int tmp = mask;
      int ci = 0, ce = 0;
      for (int col = 0; col < n; ++col) {
        int d = tmp % 3;
        if (d == 1) ++ci;
        else if (d == 2) ++ce;
        tmp ~/= 3;
      }
      cntIntro[mask] = ci;
      cntExtro[mask] = ce;
    }

    // Precompute added happiness when transitioning from prevMask to curMask
    List<List<int>> add = List.generate(maxMask, (_) => List.filled(maxMask, 0));
    for (int prev = 0; prev < maxMask; ++prev) {
      for (int cur = 0; cur < maxMask; ++cur) {
        int added = 0;
        for (int col = 0; col < n; ++col) {
          int t = (cur ~/ pow3[col]) % 3;
          if (t == 0) continue;
          int north = (prev ~/ pow3[col]) % 3;
          int west = (col > 0) ? ((cur ~/ pow3[col - 1]) % 3) : 0;

          added += base[t];
          if (north != 0) {
            added += effect[t][north] + effect[north][t];
          }
          if (west != 0) {
            added += effect[t][west] + effect[west][t];
          }
        }
        add[prev][cur] = added;
      }
    }

    // DP dimensions: mask x remaining introverts x remaining extroverts
    int Imax = introvertsCount, Emax = extrovertsCount;
    List<List<List<int>>> dpPrev = List.generate(
        maxMask,
        (_) => List.generate(Imax + 1, (_) => List.filled(Emax + 1, INF)));
    dpPrev[0][Imax][Emax] = 0;

    for (int row = 0; row < m; ++row) {
      List<List<List<int>>> dpNext = List.generate(
          maxMask,
          (_) => List.generate(Imax + 1, (_) => List.filled(Emax + 1, INF)));
      for (int prevMask = 0; prevMask < maxMask; ++prevMask) {
        for (int iRem = 0; iRem <= Imax; ++iRem) {
          for (int eRem = 0; eRem <= Emax; ++eRem) {
            int curVal = dpPrev[prevMask][iRem][eRem];
            if (curVal == INF) continue;
            for (int curMask = 0; curMask < maxMask; ++curMask) {
              int needI = cntIntro[curMask];
              int needE = cntExtro[curMask];
              if (needI > iRem || needE > eRem) continue;
              int added = add[prevMask][curMask];
              int ni = iRem - needI;
              int ne = eRem - needE;
              int newVal = curVal + added;
              if (newVal > dpNext[curMask][ni][ne]) {
                dpNext[curMask][ni][ne] = newVal;
              }
            }
          }
        }
      }
      dpPrev = dpNext;
    }

    int ans = 0;
    for (int mask = 0; mask < maxMask; ++mask) {
      for (int i = 0; i <= Imax; ++i) {
        for (int e = 0; e <= Emax; ++e) {
          if (dpPrev[mask][i][e] > ans) ans = dpPrev[mask][i][e];
        }
      }
    }
    return ans;
  }
}
```

## Golang

```go
func getMaxGridHappiness(m int, n int, introvertsCount int, extrovertsCount int) int {
	const NEG = -1 << 60

	// precompute powers of 3
	pow3 := make([]int, n+1)
	pow3[0] = 1
	for i := 1; i <= n; i++ {
		pow3[i] = pow3[i-1] * 3
	}
	totalMasks := pow3[n]

	introCnt := make([]int, totalMasks)
	extroCnt := make([]int, totalMasks)
	rowScore := make([]int, totalMasks)

	// compute per-mask data and internal row score
	for mask := 0; mask < totalMasks; mask++ {
		tmp := mask
		cells := make([]int, n)
		score := 0
		iCnt, eCnt := 0, 0
		for j := 0; j < n; j++ {
			v := tmp % 3
			cells[j] = v
			if v == 1 {
				iCnt++
				score += 120
			} else if v == 2 {
				eCnt++
				score += 40
			}
			tmp /= 3
		}
		// left-right neighbor contributions within the row
		for j := 1; j < n; j++ {
			a, b := cells[j-1], cells[j]
			if a != 0 && b != 0 {
				if a == 1 {
					score -= 30
				} else if a == 2 {
					score += 20
				}
				if b == 1 {
					score -= 30
				} else if b == 2 {
					score += 20
				}
			}
		}
		introCnt[mask] = iCnt
		extroCnt[mask] = eCnt
		rowScore[mask] = score
	}

	// precompute vertical interaction between two masks
	vertical := make([][]int, totalMasks)
	for i := 0; i < totalMasks; i++ {
		vertical[i] = make([]int, totalMasks)
	}
	for pm := 0; pm < totalMasks; pm++ {
		for cm := 0; cm < totalMasks; cm++ {
			score := 0
			tmpP, tmpC := pm, cm
			for j := 0; j < n; j++ {
				a := tmpP % 3
				b := tmpC % 3
				if a != 0 && b != 0 {
					if a == 1 {
						score -= 30
					} else if a == 2 {
						score += 20
					}
					if b == 1 {
						score -= 30
					} else if b == 2 {
						score += 20
					}
				}
				tmpP /= 3
				tmpC /= 3
			}
			vertical[pm][cm] = score
		}
	}

	// DP arrays: dpPrev[mask][i][e]
	dpPrev := make([][][]int, totalMasks)
	for i := 0; i < totalMasks; i++ {
		dpPrev[i] = make([][]int, introvertsCount+1)
		for ii := 0; ii <= introvertsCount; ii++ {
			dpPrev[i][ii] = make([]int, extrovertsCount+1)
			for ee := 0; ee <= extrovertsCount; ee++ {
				dpPrev[i][ii][ee] = NEG
			}
		}
	}
	dpPrev[0][0][0] = 0

	// iterate over rows
	for r := 0; r < m; r++ {
		// initialize dpCurr with NEG
		dpCurr := make([][][]int, totalMasks)
		for i := 0; i < totalMasks; i++ {
			dpCurr[i] = make([][]int, introvertsCount+1)
			for ii := 0; ii <= introvertsCount; ii++ {
				dpCurr[i][ii] = make([]int, extrovertsCount+1)
				for ee := 0; ee <= extrovertsCount; ee++ {
					dpCurr[i][ii][ee] = NEG
				}
			}
		}

		for prevMask := 0; prevMask < totalMasks; prevMask++ {
			for usedI := 0; usedI <= introvertsCount; usedI++ {
				for usedE := 0; usedE <= extrovertsCount; usedE++ {
					baseVal := dpPrev[prevMask][usedI][usedE]
					if baseVal == NEG {
						continue
					}
					for curMask := 0; curMask < totalMasks; curMask++ {
						addI := introCnt[curMask]
						addE := extroCnt[curMask]
						newI := usedI + addI
						newE := usedE + addE
						if newI > introvertsCount || newE > extrovertsCount {
							continue
						}
						val := baseVal + rowScore[curMask] + vertical[prevMask][curMask]
						if val > dpCurr[curMask][newI][newE] {
							dpCurr[curMask][newI][newE] = val
						}
					}
				}
			}
		}
		dpPrev = dpCurr
	}

	ans := 0
	for mask := 0; mask < totalMasks; mask++ {
		for i := 0; i <= introvertsCount; i++ {
			for e := 0; e <= extrovertsCount; e++ {
				if dpPrev[mask][i][e] > ans {
					ans = dpPrev[mask][i][e]
				}
			}
		}
	}
	return ans
}
```

## Ruby

```ruby
def get_max_grid_happiness(m, n, introverts_count, extroverts_count)
  pow3 = Array.new(n + 1, 1)
  (1..n).each { |i| pow3[i] = pow3[i - 1] * 3 }

  base   = [0, 120, 40]
  effect = [0, -30, 20]

  dp = {}
  dp[[0, introverts_count, extroverts_count]] = 0

  m.times do
    new_dp = {}

    dp.each do |(mask, i_left, e_left), cur_val|
      dfs = nil
      dfs = lambda do |col, cur_mask, i_rem, e_rem, acc|
        if col == n
          key = [cur_mask, i_rem, e_rem]
          prev = new_dp[key]
          new_dp[key] = prev.nil? || acc > prev ? acc : prev
          return
        end

        up_type   = (mask / pow3[col]) % 3
        left_type = col.zero? ? 0 : ((cur_mask / pow3[col - 1]) % 3)

        # empty
        dfs.call(col + 1, cur_mask, i_rem, e_rem, acc)

        if i_rem > 0
          add = base[1]
          nb = left_type
          add += effect[1] + effect[nb] if nb != 0
          nb = up_type
          add += effect[1] + effect[nb] if nb != 0
          new_mask = cur_mask + pow3[col] * 1
          dfs.call(col + 1, new_mask, i_rem - 1, e_rem, acc + add)
        end

        if e_rem > 0
          add = base[2]
          nb = left_type
          add += effect[2] + effect[nb] if nb != 0
          nb = up_type
          add += effect[2] + effect[nb] if nb != 0
          new_mask = cur_mask + pow3[col] * 2
          dfs.call(col + 1, new_mask, i_rem, e_rem - 1, acc + add)
        end
      end

      dfs.call(0, 0, i_left, e_left, cur_val)
    end

    dp = new_dp
  end

  dp.values.max || 0
end
```

## Scala

```scala
object Solution {
    def getMaxGridHappiness(m: Int, n: Int, introvertsCount: Int, extrovertsCount: Int): Int = {
        val pow3 = new Array[Int](n + 1)
        pow3(0) = 1
        for (i <- 1 to n) pow3(i) = pow3(i - 1) * 3
        val totalStates = pow3(n)

        // digits[state][col]
        val digits = Array.ofDim[Int](totalStates, n)
        val introInState = new Array[Int](totalStates)
        val extroInState = new Array[Int](totalStates)
        val internalHap = new Array[Int](totalStates)

        for (s <- 0 until totalStates) {
            var tmp = s
            for (c <- 0 until n) {
                digits(s)(c) = tmp % 3
                tmp /= 3
            }
            var ic = 0
            var ec = 0
            var hap = 0
            for (c <- 0 until n) {
                val cur = digits(s)(c)
                if (cur == 1) ic += 1
                else if (cur == 2) ec += 1

                if (cur != 0) {
                    hap += (if (cur == 1) 120 else 40)
                    if (c > 0) {
                        val left = digits(s)(c - 1)
                        if (left != 0) {
                            hap += (if (cur == 1) -30 else 20) // self effect
                            hap += (if (left == 1) -30 else 20) // neighbor effect on left
                        }
                    }
                }
            }
            introInState(s) = ic
            extroInState(s) = ec
            internalHap(s) = hap
        }

        val cross = Array.ofDim[Int](totalStates, totalStates)
        for (prev <- 0 until totalStates) {
            for (cur <- 0 until totalStates) {
                var add = 0
                for (c <- 0 until n) {
                    val p = digits(prev)(c)
                    val curV = digits(cur)(c)
                    if (p != 0 && curV != 0) {
                        // effect on current person
                        add += (if (curV == 1) -30 else 20)
                        // effect on previous person
                        add += (if (p == 1) -30 else 20)
                    }
                }
                cross(prev)(cur) = add
            }
        }

        val maxI = introvertsCount
        val maxE = extrovertsCount
        val NEG = Int.MinValue / 2

        var dpPrev = Array.ofDim[Int](maxI + 1, maxE + 1, totalStates)
        for (i <- 0 to maxI; e <- 0 to maxE; s <- 0 until totalStates) dpPrev(i)(e)(s) = NEG
        dpPrev(maxI)(maxE)(0) = 0

        for (_row <- 0 until m) {
            val dpNext = Array.ofDim[Int](maxI + 1, maxE + 1, totalStates)
            for (i <- 0 to maxI; e <- 0 to maxE; prev <- 0 until totalStates) dpNext(i)(e)(prev) = NEG

            for (iRem <- 0 to maxI) {
                for (eRem <- 0 to maxE) {
                    for (prevState <- 0 until totalStates) {
                        val curVal = dpPrev(iRem)(eRem)(prevState)
                        if (curVal > NEG) {
                            var curState = 0
                            while (curState < totalStates) {
                                val ic = introInState(curState)
                                val ec = extroInState(curState)
                                if (ic <= iRem && ec <= eRem) {
                                    val newI = iRem - ic
                                    val newE = eRem - ec
                                    val newScore = curVal + internalHap(curState) + cross(prevState)(curState)
                                    if (newScore > dpNext(newI)(newE)(curState)) {
                                        dpNext(newI)(newE)(curState) = newScore
                                    }
                                }
                                curState += 1
                            }
                        }
                    }
                }
            }
            dpPrev = dpNext
        }

        var ans = 0
        for (i <- 0 to maxI; e <- 0 to maxE; s <- 0 until totalStates) {
            val v = dpPrev(i)(e)(s)
            if (v > ans) ans = v
        }
        ans
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn get_max_grid_happiness(
        m: i32,
        n: i32,
        introverts_count: i32,
        extroverts_count: i32,
    ) -> i32 {
        let m_us = m as usize;
        let n_us = n as usize;
        // powers of 3 for mask encoding
        let mut pow3 = vec![1i32; n_us + 1];
        for i in 1..=n_us {
            pow3[i] = pow3[i - 1] * 3;
        }

        const BASE: [i32; 3] = [0, 120, 40];
        // effect[t][neighbor] = total change (both persons) due to this adjacency
        const EFFECT: [[i32; 3]; 3] = [
            [0, 0, 0],
            [0, -60, -10], // introvert with introvert/extrovert
            [0, -10, 40],  // extrovert with introvert/extrovert
        ];

        fn get_digit(mask: i32, idx: usize, pow3: &Vec<i32>) -> i32 {
            (mask / pow3[idx]) % 3
        }

        fn set_digit(mask: i32, idx: usize, val: i32, pow3: &Vec<i32>) -> i32 {
            let old = get_digit(mask, idx, pow3);
            mask + (val - old) * pow3[idx]
        }

        fn dfs(
            pos: usize,
            prev_mask: i32,
            cur_mask: i32,
            i_left: i32,
            e_left: i32,
            m: usize,
            n: usize,
            pow3: &Vec<i32>,
            memo: &mut HashMap<u64, i32>,
        ) -> i32 {
            if pos == m * n {
                return 0;
            }
            let key: u64 = ((pos as u64) << 40)
                | ((prev_mask as u64) << 20)
                | ((cur_mask as u64) << 10)
                | ((i_left as u64) << 5)
                | (e_left as u64);
            if let Some(&v) = memo.get(&key) {
                return v;
            }

            let row = pos / n;
            let col = pos % n;

            let up = get_digit(prev_mask, col, pow3);
            let left = if col == 0 { 0 } else { get_digit(cur_mask, col - 1, pow3) };

            let mut best = 0i32; // we can always leave empty

            // option: empty
            {
                let next_cur = set_digit(cur_mask, col, 0, pow3);
                let (next_prev, reset_cur) = if col + 1 == n {
                    (next_cur, 0)
                } else {
                    (prev_mask, next_cur)
                };
                let val = dfs(
                    pos + 1,
                    next_prev,
                    reset_cur,
                    i_left,
                    e_left,
                    m,
                    n,
                    pow3,
                    memo,
                );
                if val > best {
                    best = val;
                }
            }

            // option: introvert
            if i_left > 0 {
                let t = 1;
                let mut add = BASE[t];
                if up != 0 {
                    add += EFFECT[t][up as usize];
                }
                if left != 0 {
                    add += EFFECT[t][left as usize];
                }
                let next_cur = set_digit(cur_mask, col, t, pow3);
                let (next_prev, reset_cur) = if col + 1 == n {
                    (next_cur, 0)
                } else {
                    (prev_mask, next_cur)
                };
                let val = add
                    + dfs(
                        pos + 1,
                        next_prev,
                        reset_cur,
                        i_left - 1,
                        e_left,
                        m,
                        n,
                        pow3,
                        memo,
                    );
                if val > best {
                    best = val;
                }
            }

            // option: extrovert
            if e_left > 0 {
                let t = 2;
                let mut add = BASE[t];
                if up != 0 {
                    add += EFFECT[t][up as usize];
                }
                if left != 0 {
                    add += EFFECT[t][left as usize];
                }
                let next_cur = set_digit(cur_mask, col, t, pow3);
                let (next_prev, reset_cur) = if col + 1 == n {
                    (next_cur, 0)
                } else {
                    (prev_mask, next_cur)
                };
                let val = add
                    + dfs(
                        pos + 1,
                        next_prev,
                        reset_cur,
                        i_left,
                        e_left - 1,
                        m,
                        n,
                        pow3,
                        memo,
                    );
                if val > best {
                    best = val;
                }
            }

            memo.insert(key, best);
            best
        }

        let mut memo: HashMap<u64, i32> = HashMap::new();
        dfs(
            0,
            0,
            0,
            introverts_count,
            extroverts_count,
            m_us,
            n_us,
            &pow3,
            &mut memo,
        )
    }
}
```

## Racket

```racket
(define/contract (get-max-grid-happiness m n introvertsCount extrovertsCount)
  (-> exact-integer? exact-integer? exact-integer? exact-integer? exact-integer?)
  (let* ([total-cells (* m n)]
         ;; precompute powers of 3 up to n
         [pow3 (let ([v (make-vector (+ n 1))])
                 (vector-set! v 0 1)
                 (for ([i (in-range 1 (+ n 1))])
                   (vector-set! v i (* 3 (vector-ref v (- i 1)))))
                 v)]
         ;; helpers to get/set digit in base‑3 mask
         [digit (lambda (mask idx)
                  (modulo (quotient mask (vector-ref pow3 idx)) 3))]
         [set-digit (lambda (mask idx val)
                      (+ mask (* (- val (digit mask idx))
                                 (vector-ref pow3 idx))))])
    (define memo (make-hash))

    (define (dfs pos mask i-left e-left left-type)
      (if (= pos total-cells)
          0
          (let* ([key (list pos mask i-left e-left left-type)])
            (or (hash-ref memo key #f)
                (let* ([row (quotient pos n)]
                       [col (remainder pos n)]
                       [up (digit mask col)]
                       [best -1000000])
                  ;; try empty
                  (let* ([new-mask (set-digit mask col 0)]
                         [next-left 0]
                         [val (+ (dfs (+ pos 1) new-mask i-left e-left next-left))])
                    (when (> val best) (set! best val)))
                  ;; try introvert
                  (when (> i-left 0)
                    (let* ([neighbors (list up left-type)]
                           [cnt (length (filter positive? neighbors))]
                           [add (+ 120 (* -30 cnt))]
                           [add (foldl (lambda (nt acc)
                                         (cond [(= nt 1) (+ acc -30)]
                                               [(= nt 2) (+ acc 20)]
                                               [else acc]))
                                       add
                                       neighbors)]
                           [new-mask (set-digit mask col 1)]
                           [next-left (if (= col (- n 1)) 0 1)]
                           [val (+ add (dfs (+ pos 1) new-mask (- i-left 1) e-left next-left))])
                      (when (> val best) (set! best val))))
                  ;; try extrovert
                  (when (> e-left 0)
                    (let* ([neighbors (list up left-type)]
                           [cnt (length (filter positive? neighbors))]
                           [add (+ 40 (* 20 cnt))]
                           [add (foldl (lambda (nt acc)
                                         (cond [(= nt 1) (+ acc -30)]
                                               [(= nt 2) (+ acc 20)]
                                               [else acc]))
                                       add
                                       neighbors)]
                           [new-mask (set-digit mask col 2)]
                           [next-left (if (= col (- n 1)) 0 2)]
                           [val (+ add (dfs (+ pos 1) new-mask i-left (- e-left 1) next-left))])
                      (when (> val best) (set! best val))))
                  (hash-set! memo key best)
                  best)))))

    (dfs 0 0 introvertsCount extrovertsCount 0)))
```

## Erlang

```erlang
-module(solution).
-export([get_max_grid_happiness/4]).

%% Entry point
-spec get_max_grid_happiness(integer(), integer(), integer(), integer()) -> integer().
get_max_grid_happiness(M, N, IntrovertsCount, ExtrovertsCount) ->
    MaxMask = trunc(math:pow(3, N)),
    %% Precompute mask info: {CntI, CntE, Internal}
    MaskInfo = precompute_masks(N, MaxMask),
    %% Initialize DP map with key {IUsed, EUsed, PrevMask} -> Value
    InitDP = maps:from_list([{{0, 0, 0}, 0}]),
    FinalDP = dp_rows(1, M, N, IntrovertsCount, ExtrovertsCount, MaxMask, MaskInfo, InitDP),
    %% Find maximum value in final DP map
    lists:max(maps:values(FinalDP)).

%% Precompute mask information for all masks
precompute_masks(N, MaxMask) ->
    lists:foldl(fun(Mask, Acc) ->
        {CntI, CntE, Internal} = calc_mask(N, Mask),
        maps:put(Mask, {CntI, CntE, Internal}, Acc)
    end, #{}, lists:seq(0, MaxMask - 1)).

%% DP over rows
dp_rows(Row, M, _N, _ICap, _ECap, _MaxMask, _MaskInfo, DP) when Row > M ->
    DP;
dp_rows(Row, M, N, ICap, ECap, MaxMask, MaskInfo, DP) ->
    NewDP = maps:fold(fun({IUsed, EUsed, PrevMask}, Val, Acc) ->
        lists:foldl(fun(CurMask, InnerAcc) ->
            {CntI, CntE, Internal} = maps:get(CurMask, MaskInfo),
            I2 = IUsed + CntI,
            E2 = EUsed + CntE,
            if
                I2 =< ICap, E2 =< ECap ->
                    Add = Internal + vertical_contrib(N, PrevMask, CurMask),
                    NewVal = Val + Add,
                    Key = {I2, E2, CurMask},
                    case maps:find(Key, InnerAcc) of
                        {ok, Existing} when Existing >= NewVal -> InnerAcc;
                        _ -> maps:put(Key, NewVal, InnerAcc)
                    end;
                true ->
                    InnerAcc
            end
        end, Acc, lists:seq(0, MaxMask - 1))
    end, #{}, DP),
    dp_rows(Row + 1, M, N, ICap, ECap, MaxMask, MaskInfo, NewDP).

%% Calculate mask internal happiness and counts
calc_mask(N, Mask) ->
    calc_mask(0, N, Mask, 0, 0, 0).

calc_mask(Pos, N, _Mask, CntI, CntE, Sum) when Pos == N ->
    {CntI, CntE, Sum};
calc_mask(Pos, N, Mask, CntI, CntE, Sum) ->
    Digit = (Mask div pow3(Pos)) rem 3,
    case Digit of
        0 ->
            calc_mask(Pos + 1, N, Mask, CntI, CntE, Sum);
        1 -> % introvert
            Base = 120,
            LeftDigit = if Pos == 0 -> 0; true -> (Mask div pow3(Pos - 1)) rem 3 end,
            PairAdd = pair_contrib(1, LeftDigit),
            calc_mask(Pos + 1, N, Mask, CntI + 1, CntE, Sum + Base + PairAdd);
        2 -> % extrovert
            Base = 40,
            LeftDigit = if Pos == 0 -> 0; true -> (Mask div pow3(Pos - 1)) rem 3 end,
            PairAdd = pair_contrib(2, LeftDigit),
            calc_mask(Pos + 1, N, Mask, CntI, CntE + 1, Sum + Base + PairAdd)
    end.

%% Vertical contribution between two masks
vertical_contrib(N, PrevMask, CurMask) ->
    vertical_contrib(0, N, PrevMask, CurMask, 0).

vertical_contrib(Pos, N, _Prev, _Cur, Sum) when Pos == N ->
    Sum;
vertical_contrib(Pos, N, PrevMask, CurMask, Sum) ->
    T1 = (PrevMask div pow3(Pos)) rem 3,
    T2 = (CurMask div pow3(Pos)) rem 3,
    Add = pair_contrib(T1, T2),
    vertical_contrib(Pos + 1, N, PrevMask, CurMask, Sum + Add).

%% Pair contribution for adjacency
pair_contrib(0, _) -> 0;
pair_contrib(_, 0) -> 0;
pair_contrib(1, 1) -> -60;
pair_contrib(2, 2) -> 40;
pair_contrib(_, _) -> -10.

%% Power of three helper (pos >= 0)
pow3(0) -> 1;
pow3(Pos) when Pos > 0 ->
    pow3(Pos - 1) * 3.
```

## Elixir

```elixir
defmodule Solution do
  @spec get_max_grid_happiness(integer, integer, integer, integer) :: integer
  def get_max_grid_happiness(m, n, introverts_count, extroverts_count) do
    total = m * n

    pow3 =
      for i <- 0..(n - 1) do
        trunc(:math.pow(3, i))
      end

    base = %{0 => 0, 1 => 120, 2 => 40}
    delta = %{0 => 0, 1 => -30, 2 => 20}

    init_state = %{{introverts_count, extroverts_count, 0, 0} => 0}

    final_dp =
      Enum.reduce(0..total - 1, init_state, fn idx, cur_dp ->
        col = rem(idx, n)

        Enum.reduce(cur_dp, %{}, fn {{i_left, e_left, mask, left}, val}, acc ->
          up_type = get_digit(mask, col, pow3)

          # option: leave empty
          new_mask0 = set_digit(mask, col, 0, pow3)
          next_left0 = if col == n - 1, do: 0, else: 0
          acc = update_max(acc, {i_left, e_left, new_mask0, next_left0}, val)

          # option: place introvert
          acc =
            if i_left > 0 do
              added = base[1] + interaction(1, up_type, delta) + interaction(1, left, delta)
              new_mask1 = set_digit(mask, col, 1, pow3)
              next_left1 = if col == n - 1, do: 0, else: 1
              update_max(acc, {i_left - 1, e_left, new_mask1, next_left1}, val + added)
            else
              acc
            end

          # option: place extrovert
          acc =
            if e_left > 0 do
              added = base[2] + interaction(2, up_type, delta) + interaction(2, left, delta)
              new_mask2 = set_digit(mask, col, 2, pow3)
              next_left2 = if col == n - 1, do: 0, else: 2
              update_max(acc, {i_left, e_left - 1, new_mask2, next_left2}, val + added)
            else
              acc
            end

          acc
        end)
      end)

    final_dp
    |> Map.values()
    |> Enum.max(fn -> 0 end)
  end

  defp get_digit(mask, pos, pow3) do
    p = Enum.at(pow3, pos)
    div(mask, p) |> rem(3)
  end

  defp set_digit(mask, pos, val, pow3) do
    p = Enum.at(pow3, pos)
    old = div(mask, p) |> rem(3)
    mask - old * p + val * p
  end

  defp interaction(_t, 0, _delta), do: 0

  defp interaction(t, neighbor, delta) do
    delta[t] + delta[neighbor]
  end

  defp update_max(map, key, new_val) do
    case Map.get(map, key) do
      nil -> Map.put(map, key, new_val)
      existing when existing < new_val -> Map.put(map, key, new_val)
      _ -> map
    end
  end
end
```
