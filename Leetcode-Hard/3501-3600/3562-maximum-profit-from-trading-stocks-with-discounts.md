# 3562. Maximum Profit from Trading Stocks with Discounts

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxProfit(int n, vector<int>& present, vector<int>& future,
                  vector<vector<int>>& hierarchy, int budget) {
        // 1-index arrays
        present.insert(present.begin(), 0);
        future.insert(future.begin(), 0);
        vector<vector<int>> children(n + 1);
        for (auto &e : hierarchy) {
            int u = e[0], v = e[1];
            children[u].push_back(v);
        }
        const int NEG = -1e9;
        function<pair<vector<int>, vector<int>>(int)> dfs = [&](int u)
            -> pair<vector<int>, vector<int>> {
            // agg0: children profit when u is NOT bought (use child dp0)
            // agg1: children profit when u IS bought (use child dp1)
            vector<int> agg0(budget + 1, NEG), agg1(budget + 1, NEG);
            agg0[0] = agg1[0] = 0;
            for (int v : children[u]) {
                auto childDP = dfs(v);
                const vector<int>& dp0 = childDP.first;   // parent not bought
                const vector<int>& dp1 = childDP.second;  // parent bought

                // combine for agg0 using child's dp0
                vector<int> newAgg0(budget + 1, NEG);
                for (int i = 0; i <= budget; ++i) if (agg0[i] != NEG) {
                    for (int j = 0; j + i <= budget; ++j) if (dp0[j] != NEG) {
                        newAgg0[i + j] = max(newAgg0[i + j], agg0[i] + dp0[j]);
                    }
                }
                agg0.swap(newAgg0);

                // combine for agg1 using child's dp1
                vector<int> newAgg1(budget + 1, NEG);
                for (int i = 0; i <= budget; ++i) if (agg1[i] != NEG) {
                    for (int j = 0; j + i <= budget; ++j) if (dp1[j] != NEG) {
                        newAgg1[i + j] = max(newAgg1[i + j], agg1[i] + dp1[j]);
                    }
                }
                agg1.swap(newAgg1);
            }

            vector<int> res0(budget + 1, NEG), res1(budget + 1, NEG);

            // Case: u not bought (both parent states)
            for (int c = 0; c <= budget; ++c) if (agg0[c] != NEG) {
                res0[c] = max(res0[c], agg0[c]);
                res1[c] = max(res1[c], agg0[c]); // parent bought but u not bought
            }

            // Case: u bought, parent NOT bought -> normal cost, children get discount (agg1)
            int costNorm = present[u];
            int profitNorm = future[u] - costNorm;
            if (costNorm <= budget) {
                for (int c = 0; c + costNorm <= budget; ++c) if (agg1[c] != NEG) {
                    res0[c + costNorm] = max(res0[c + costNorm], agg1[c] + profitNorm);
                }
            }

            // Case: u bought, parent bought -> discounted cost, children get discount (agg1)
            int costDisc = present[u] / 2;
            int profitDisc = future[u] - costDisc;
            if (costDisc <= budget) {
                for (int c = 0; c + costDisc <= budget; ++c) if (agg1[c] != NEG) {
                    res1[c + costDisc] = max(res1[c + costDisc], agg1[c] + profitDisc);
                }
            }

            return {res0, res1};
        };

        auto rootDP = dfs(1);
        const vector<int>& dpRoot = rootDP.first; // parent of root is considered not bought
        int ans = 0;
        for (int c = 0; c <= budget; ++c) {
            if (dpRoot[c] > ans) ans = dpRoot[c];
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static final int NEG_INF = -1_000_000_000;

    public int maxProfit(int n, int[] present, int[] future, int[][] hierarchy, int budget) {
        List<Integer>[] children = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) children[i] = new ArrayList<>();
        for (int[] e : hierarchy) {
            children[e[0]].add(e[1]);
        }
        DP rootDP = dfs(1, children, present, future, budget);
        int ans = 0;
        for (int c = 0; c <= budget; c++) {
            ans = Math.max(ans, rootDP.noParent[c]);
        }
        return ans;
    }

    private static class DP {
        int[] noParent;   // parent did NOT buy
        int[] parentBought; // parent DID buy

        DP(int[] np, int[] pb) {
            this.noParent = np;
            this.parentBought = pb;
        }
    }

    private DP dfs(int u, List<Integer>[] children, int[] present, int[] future, int B) {
        List<DP> childDPs = new ArrayList<>();
        for (int v : children[u]) {
            childDPs.add(dfs(v, children, present, future, B));
        }

        // Base arrays for "not buying u"
        int[] baseNoBuy = new int[B + 1];
        Arrays.fill(baseNoBuy, NEG_INF);
        baseNoBuy[0] = 0;
        for (DP cd : childDPs) {
            baseNoBuy = combine(baseNoBuy, cd.noParent, B);
        }

        // dp when parent did NOT buy
        int[] dp0 = new int[B + 1];
        Arrays.fill(dp0, NEG_INF);
        // not buying u
        for (int c = 0; c <= B; c++) {
            if (baseNoBuy[c] != NEG_INF) dp0[c] = Math.max(dp0[c], baseNoBuy[c]);
        }
        // buying u at full price
        int costFull = present[u - 1];
        int profitFull = future[u - 1] - costFull;
        if (costFull <= B) {
            int[] cur = new int[B + 1];
            Arrays.fill(cur, NEG_INF);
            cur[costFull] = profitFull;
            for (DP cd : childDPs) {
                cur = combine(cur, cd.parentBought, B);
            }
            for (int c = 0; c <= B; c++) {
                if (cur[c] != NEG_INF) dp0[c] = Math.max(dp0[c], cur[c]);
            }
        }

        // dp when parent DID buy
        int[] dp1 = new int[B + 1];
        Arrays.fill(dp1, NEG_INF);
        // not buying u (same as baseNoBuy)
        for (int c = 0; c <= B; c++) {
            if (baseNoBuy[c] != NEG_INF) dp1[c] = Math.max(dp1[c], baseNoBuy[c]);
        }
        // buying u at discounted price
        int costDisc = present[u - 1] / 2;
        int profitDisc = future[u - 1] - costDisc;
        if (costDisc <= B) {
            int[] cur = new int[B + 1];
            Arrays.fill(cur, NEG_INF);
            cur[costDisc] = profitDisc;
            for (DP cd : childDPs) {
                cur = combine(cur, cd.parentBought, B);
            }
            for (int c = 0; c <= B; c++) {
                if (cur[c] != NEG_INF) dp1[c] = Math.max(dp1[c], cur[c]);
            }
        }

        return new DP(dp0, dp1);
    }

    private int[] combine(int[] a, int[] b, int B) {
        int[] res = new int[B + 1];
        Arrays.fill(res, NEG_INF);
        for (int i = 0; i <= B; i++) {
            if (a[i] == NEG_INF) continue;
            for (int j = 0; j + i <= B; j++) {
                if (b[j] == NEG_INF) continue;
                int val = a[i] + b[j];
                if (val > res[i + j]) res[i + j] = val;
            }
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def maxProfit(self, n, present, future, hierarchy, budget):
        """
        :type n: int
        :type present: List[int]
        :type future: List[int]
        :type hierarchy: List[List[int]]
        :type budget: int
        :rtype: int
        """
        B = budget
        g = [[] for _ in range(n)]
        for u, v in hierarchy:
            g[u - 1].append(v - 1)

        INF_NEG = -10 ** 9

        def dfs(u):
            # gather children's dp tables first
            child_infos = []
            for v in g[u]:
                dp0_child, dp1_child = dfs(v)
                child_infos.append((dp0_child, dp1_child))

            # ---------- not buying u ----------
            # parent not bought -> children see parent not bought (use dp0)
            cur0 = [INF_NEG] * (B + 1)
            cur0[0] = 0
            for dp0c, _ in child_infos:
                nxt = [INF_NEG] * (B + 1)
                for i in range(B + 1):
                    if cur0[i] == INF_NEG:
                        continue
                    vi = cur0[i]
                    limit = B - i
                    for j in range(limit + 1):
                        val = dp0c[j]
                        if val == INF_NEG:
                            continue
                        nv = vi + val
                        if nv > nxt[i + j]:
                            nxt[i + j] = nv
                cur0 = nxt
            notBuy0 = cur0

            # parent bought -> u not bought, children still see parent not bought (dp0)
            cur1 = [INF_NEG] * (B + 1)
            cur1[0] = 0
            for dp0c, _ in child_infos:
                nxt = [INF_NEG] * (B + 1)
                for i in range(B + 1):
                    if cur1[i] == INF_NEG:
                        continue
                    vi = cur1[i]
                    limit = B - i
                    for j in range(limit + 1):
                        val = dp0c[j]
                        if val == INF_NEG:
                            continue
                        nv = vi + val
                        if nv > nxt[i + j]:
                            nxt[i + j] = nv
                cur1 = nxt
            notBuy1 = cur1

            # ---------- buying u ----------
            # price when parent not bought (full)
            price_full = present[u]
            profit_full = future[u] - price_full
            buy0 = [INF_NEG] * (B + 1)
            if price_full <= B:
                buy0[price_full] = profit_full
                cur = buy0[:]
                for _, dp1c in child_infos:
                    nxt = [INF_NEG] * (B + 1)
                    for i in range(B + 1):
                        if cur[i] == INF_NEG:
                            continue
                        vi = cur[i]
                        limit = B - i
                        for j in range(limit + 1):
                            val = dp1c[j]
                            if val == INF_NEG:
                                continue
                            nv = vi + val
                            if nv > nxt[i + j]:
                                nxt[i + j] = nv
                    cur = nxt
                buy0 = cur

            # price when parent bought (discount)
            price_disc = present[u] // 2
            profit_disc = future[u] - price_disc
            buy1 = [INF_NEG] * (B + 1)
            if price_disc <= B:
                buy1[price_disc] = profit_disc
                cur = buy1[:]
                for _, dp1c in child_infos:
                    nxt = [INF_NEG] * (B + 1)
                    for i in range(B + 1):
                        if cur[i] == INF_NEG:
                            continue
                        vi = cur[i]
                        limit = B - i
                        for j in range(limit + 1):
                            val = dp1c[j]
                            if val == INF_NEG:
                                continue
                            nv = vi + val
                            if nv > nxt[i + j]:
                                nxt[i + j] = nv
                    cur = nxt
                buy1 = cur

            # combine results for each state
            dp0 = [max(notBuy0[c], buy0[c]) for c in range(B + 1)]
            dp1 = [max(notBuy1[c], buy1[c]) for c in range(B + 1)]
            return dp0, dp1

        dp_root, _ = dfs(0)
        return max(dp_root)
```

## Python3

```python
import sys
from typing import List

sys.setrecursionlimit(10000)

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int],
                  hierarchy: List[List[int]], budget: int) -> int:
        # build tree
        children = [[] for _ in range(n)]
        for u, v in hierarchy:
            children[u - 1].append(v - 1)

        INF_NEG = -10**9

        def dfs(u: int):
            # start with empty contributions
            skip_dp = [INF_NEG] * (budget + 1)
            skip_dp[0] = 0
            buy_child_dp = [INF_NEG] * (budget + 1)
            buy_child_dp[0] = 0

            for v in children[u]:
                child_dp0, child_dp1 = dfs(v)

                # merge into skip_dp using child's dp0 (u not bought)
                new_skip = [INF_NEG] * (budget + 1)
                for i in range(budget + 1):
                    if skip_dp[i] == INF_NEG:
                        continue
                    max_j = budget - i
                    child_arr = child_dp0
                    for j in range(max_j + 1):
                        val = child_arr[j]
                        if val == INF_NEG:
                            continue
                        nb = i + j
                        cur = skip_dp[i] + val
                        if cur > new_skip[nb]:
                            new_skip[nb] = cur
                skip_dp = new_skip

                # merge into buy_child_dp using child's dp1 (u bought)
                new_buy = [INF_NEG] * (budget + 1)
                for i in range(budget + 1):
                    if buy_child_dp[i] == INF_NEG:
                        continue
                    max_j = budget - i
                    child_arr = child_dp1
                    for j in range(max_j + 1):
                        val = child_arr[j]
                        if val == INF_NEG:
                            continue
                        nb = i + j
                        cur = buy_child_dp[i] + val
                        if cur > new_buy[nb]:
                            new_buy[nb] = cur
                buy_child_dp = new_buy

            # now construct dp0 (parent not bought) and dp1 (parent bought)
            dp0 = [INF_NEG] * (budget + 1)
            dp1 = [INF_NEG] * (budget + 1)

            # skip buying u
            for b in range(budget + 1):
                if skip_dp[b] != INF_NEG:
                    dp0[b] = max(dp0[b], skip_dp[b])
                    dp1[b] = max(dp1[b], skip_dp[b])

            # buy u without discount (parent not bought)
            cost0 = present[u]
            profit0 = future[u] - cost0
            for b in range(budget + 1):
                if buy_child_dp[b] == INF_NEG:
                    continue
                nb = b + cost0
                if nb <= budget:
                    val = buy_child_dp[b] + profit0
                    if val > dp0[nb]:
                        dp0[nb] = val

            # buy u with discount (parent bought)
            cost1 = present[u] // 2
            profit1 = future[u] - cost1
            for b in range(budget + 1):
                if buy_child_dp[b] == INF_NEG:
                    continue
                nb = b + cost1
                if nb <= budget:
                    val = buy_child_dp[b] + profit1
                    if val > dp1[nb]:
                        dp1[nb] = val

            return dp0, dp1

        root_dp0, _ = dfs(0)
        return max(root_dp0)
```

## C

```c
#include <stddef.h>

#define MAXN 165
#define MAXB 165
#define NEG_INF (-1000000000)

static int children[MAXN][MAXN];
static int childCnt[MAXN];
static int dp0[MAXN][MAXB];
static int dp1[MAXN][MAXB];

static void dfs(int u, int budget, const int *present, const int *future) {
    static int notBuy[MAXB];
    static int buyChild[MAXB];
    static int tmp[MAXB];
    for (int i = 0; i <= budget; ++i) {
        notBuy[i] = NEG_INF;
        buyChild[i] = NEG_INF;
    }
    notBuy[0] = 0;
    buyChild[0] = 0;

    for (int idx = 0; idx < childCnt[u]; ++idx) {
        int v = children[u][idx];
        dfs(v, budget, present, future);

        /* merge dp0[v] into notBuy */
        for (int i = 0; i <= budget; ++i) tmp[i] = NEG_INF;
        for (int c1 = 0; c1 <= budget; ++c1) {
            if (notBuy[c1] == NEG_INF) continue;
            for (int c2 = 0; c1 + c2 <= budget; ++c2) {
                if (dp0[v][c2] == NEG_INF) continue;
                int val = notBuy[c1] + dp0[v][c2];
                if (val > tmp[c1 + c2]) tmp[c1 + c2] = val;
            }
        }
        for (int i = 0; i <= budget; ++i) notBuy[i] = tmp[i];

        /* merge dp1[v] into buyChild */
        for (int i = 0; i <= budget; ++i) tmp[i] = NEG_INF;
        for (int c1 = 0; c1 <= budget; ++c1) {
            if (buyChild[c1] == NEG_INF) continue;
            for (int c2 = 0; c1 + c2 <= budget; ++c2) {
                if (dp1[v][c2] == NEG_INF) continue;
                int val = buyChild[c1] + dp1[v][c2];
                if (val > tmp[c1 + c2]) tmp[c1 + c2] = val;
            }
        }
        for (int i = 0; i <= budget; ++i) buyChild[i] = tmp[i];
    }

    for (int i = 0; i <= budget; ++i) {
        dp0[u][i] = NEG_INF;
        dp1[u][i] = NEG_INF;
    }

    /* not buying u */
    for (int c = 0; c <= budget; ++c) {
        if (notBuy[c] != NEG_INF) {
            if (notBuy[c] > dp0[u][c]) dp0[u][c] = notBuy[c];
            if (notBuy[c] > dp1[u][c]) dp1[u][c] = notBuy[c];
        }
    }

    int pu = present[u - 1];
    int fu = future[u - 1];
    int profitFull = fu - pu;

    /* buying u with full price (parent did NOT buy) */
    if (pu <= budget) {
        for (int c = pu; c <= budget; ++c) {
            int childCost = c - pu;
            if (buyChild[childCost] != NEG_INF) {
                int val = profitFull + buyChild[childCost];
                if (val > dp0[u][c]) dp0[u][c] = val;
            }
        }
    }

    int disc = pu / 2;
    int profitDisc = fu - disc;

    /* buying u with discounted price (parent DID buy) */
    if (disc <= budget) {
        for (int c = disc; c <= budget; ++c) {
            int childCost = c - disc;
            if (buyChild[childCost] != NEG_INF) {
                int val = profitDisc + buyChild[childCost];
                if (val > dp1[u][c]) dp1[u][c] = val;
            }
        }
    }
}

int maxProfit(int n, int* present, int presentSize, int* future, int futureSize,
              int** hierarchy, int hierarchySize, int* hierarchyColSize, int budget) {
    for (int i = 1; i <= n; ++i) childCnt[i] = 0;
    for (int i = 0; i < hierarchySize; ++i) {
        int u = hierarchy[i][0];
        int v = hierarchy[i][1];
        children[u][childCnt[u]++] = v;
    }

    dfs(1, budget, present, future);

    int ans = 0;
    for (int c = 0; c <= budget; ++c) {
        if (dp0[1][c] > ans) ans = dp0[1][c];
    }
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private int n, B;
    private int[] present, future;
    private List<int>[] children;
    private const int NEG = -1000000000;
    private int[][] dp0; // parent did not buy
    private int[][] dp1; // parent bought

    public int MaxProfit(int n, int[] present, int[] future, int[][] hierarchy, int budget) {
        this.n = n;
        this.B = budget;
        this.present = present;
        this.future = future;
        children = new List<int>[n];
        for (int i = 0; i < n; i++) children[i] = new List<int>();
        foreach (var e in hierarchy) {
            int u = e[0] - 1;
            int v = e[1] - 1;
            children[u].Add(v);
        }
        dp0 = new int[n][];
        dp1 = new int[n][];
        Dfs(0);
        int ans = 0;
        for (int c = 0; c <= B; c++) {
            ans = Math.Max(ans, dp0[0][c]);
        }
        return ans;
    }

    private void Dfs(int u) {
        foreach (var v in children[u]) Dfs(v);

        // compute dp for state where parent did NOT buy
        int[] notBuy = ComputeState(u, false);
        // compute dp for state where parent DID buy
        int[] boughtParent = ComputeState(u, true);

        dp0[u] = notBuy;
        dp1[u] = boughtParent;
    }

    private int[] ComputeState(int u, bool parentBought) {
        // Not buying u
        int[] curNot = new int[B + 1];
        for (int i = 0; i <= B; i++) curNot[i] = NEG;
        curNot[0] = 0;
        foreach (var v in children[u]) {
            curNot = Merge(curNot, dp0[v]); // children see parent not bought
        }

        // Buying u
        int costBuy = parentBought ? present[u] / 2 : present[u];
        int profitGain = future[u] - costBuy;
        int[] curBuy = new int[B + 1];
        for (int i = 0; i <= B; i++) curBuy[i] = NEG;
        if (costBuy <= B) {
            curBuy[costBuy] = profitGain;
            foreach (var v in children[u]) {
                curBuy = Merge(curBuy, dp1[v]); // children see parent bought
            }
        }

        int[] result = new int[B + 1];
        for (int i = 0; i <= B; i++) {
            result[i] = Math.Max(curNot[i], curBuy[i]);
        }
        return result;
    }

    private int[] Merge(int[] a, int[] b) {
        int[] res = new int[B + 1];
        for (int i = 0; i <= B; i++) res[i] = NEG;
        for (int i = 0; i <= B; i++) {
            if (a[i] == NEG) continue;
            for (int j = 0; j + i <= B; j++) {
                if (b[j] == NEG) continue;
                int val = a[i] + b[j];
                if (val > res[i + j]) res[i + j] = val;
            }
        }
        return res;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[]} present
 * @param {number[]} future
 * @param {number[][]} hierarchy
 * @param {number} budget
 * @return {number}
 */
var maxProfit = function(n, present, future, hierarchy, budget) {
    const B = budget;
    const INF_NEG = -1e15;

    // build children list
    const children = Array.from({length: n + 1}, () => []);
    for (const [u, v] of hierarchy) {
        children[u].push(v);
    }

    // dp0[node][c] : max profit in subtree when parent didn't buy
    // dp1[node][c] : max profit in subtree when parent bought
    const dp0 = Array(n + 1);
    const dp1 = Array(n + 1);

    function knapMerge(base, child) {
        const res = Array(B + 1).fill(INF_NEG);
        for (let i = 0; i <= B; ++i) {
            if (base[i] === INF_NEG) continue;
            for (let j = 0; j <= B - i; ++j) {
                if (child[j] === INF_NEG) continue;
                const val = base[i] + child[j];
                if (val > res[i + j]) res[i + j] = val;
            }
        }
        return res;
    }

    function dfs(u) {
        // process children first
        for (const v of children[u]) dfs(v);

        // merge children's dp0 and dp1 separately
        let merge0 = Array(B + 1).fill(INF_NEG);
        merge0[0] = 0;
        let merge1 = Array(B + 1).fill(INF_NEG);
        merge1[0] = 0;

        for (const v of children[u]) {
            merge0 = knapMerge(merge0, dp0[v]);
            merge1 = knapMerge(merge1, dp1[v]);
        }

        const priceFull = present[u - 1];
        const priceDisc = Math.floor(present[u - 1] / 2);
        const profitFull = future[u - 1] - priceFull;
        const profitDisc = future[u - 1] - priceDisc;

        // dp0 for node u (parent didn't buy)
        const cur0 = Array(B + 1).fill(INF_NEG);
        // option: not buying u
        for (let c = 0; c <= B; ++c) {
            if (merge0[c] !== INF_NEG) cur0[c] = Math.max(cur0[c], merge0[c]);
        }
        // option: buying u at full price, children see parent bought -> use merge1
        if (priceFull <= B) {
            for (let cChild = 0; cChild + priceFull <= B; ++cChild) {
                if (merge1[cChild] === INF_NEG) continue;
                const total = priceFull + cChild;
                const val = profitFull + merge1[cChild];
                if (val > cur0[total]) cur0[total] = val;
            }
        }

        // dp1 for node u (parent bought)
        const cur1 = Array(B + 1).fill(INF_NEG);
        // option: not buying u (children see parent not bought)
        for (let c = 0; c <= B; ++c) {
            if (merge0[c] !== INF_NEG) cur1[c] = Math.max(cur1[c], merge0[c]);
        }
        // option: buying u at discounted price, children see parent bought -> use merge1
        if (priceDisc <= B) {
            for (let cChild = 0; cChild + priceDisc <= B; ++cChild) {
                if (merge1[cChild] === INF_NEG) continue;
                const total = priceDisc + cChild;
                const val = profitDisc + merge1[cChild];
                if (val > cur1[total]) cur1[total] = val;
            }
        }

        dp0[u] = cur0;
        dp1[u] = cur1;
    }

    dfs(1);

    let ans = 0;
    for (let c = 0; c <= B; ++c) {
        if (dp0[1][c] > ans) ans = dp0[1][c];
    }
    return ans;
};
```

## Typescript

```typescript
function maxProfit(n: number, present: number[], future: number[], hierarchy: number[][], budget: number): number {
    const INF_NEG = -1e15;
    const children: number[][] = Array.from({ length: n + 1 }, () => []);
    for (const [u, v] of hierarchy) {
        children[u].push(v);
    }

    const dp0: number[][] = Array.from({ length: n + 1 }, () => new Array(budget + 1).fill(INF_NEG));
    const dp1: number[][] = Array.from({ length: n + 1 }, () => new Array(budget + 1).fill(INF_NEG));

    function merge(a: number[], b: number[]): number[] {
        const res = new Array(budget + 1).fill(INF_NEG);
        for (let i = 0; i <= budget; ++i) {
            if (a[i] <= INF_NEG / 2) continue;
            for (let j = 0; j + i <= budget; ++j) {
                if (b[j] <= INF_NEG / 2) continue;
                const val = a[i] + b[j];
                if (val > res[i + j]) res[i + j] = val;
            }
        }
        return res;
    }

    function dfs(u: number): void {
        for (const v of children[u]) dfs(v);

        // ----- parent NOT bought (dp0) -----
        // not buying u
        let curNotBuy = new Array(budget + 1).fill(INF_NEG);
        curNotBuy[0] = 0;
        for (const v of children[u]) {
            curNotBuy = merge(curNotBuy, dp0[v]);
        }

        // buying u at full price
        const costFull = present[u - 1];
        let curBuy = new Array(budget + 1).fill(INF_NEG);
        if (costFull <= budget) {
            curBuy[costFull] = future[u - 1] - costFull;
        }
        for (const v of children[u]) {
            curBuy = merge(curBuy, dp1[v]);
        }

        const dp0u = new Array(budget + 1).fill(INF_NEG);
        for (let c = 0; c <= budget; ++c) {
            dp0u[c] = Math.max(curNotBuy[c], curBuy[c]);
        }
        dp0[u] = dp0u;

        // ----- parent bought (dp1) -----
        // not buying u
        let curNotBuy1 = new Array(budget + 1).fill(INF_NEG);
        curNotBuy1[0] = 0;
        for (const v of children[u]) {
            curNotBuy1 = merge(curNotBuy1, dp0[v]);
        }

        // buying u at discounted price
        const costDisc = Math.floor(present[u - 1] / 2);
        let curBuy1 = new Array(budget + 1).fill(INF_NEG);
        if (costDisc <= budget) {
            curBuy1[costDisc] = future[u - 1] - costDisc;
        }
        for (const v of children[u]) {
            curBuy1 = merge(curBuy1, dp1[v]);
        }

        const dp1u = new Array(budget + 1).fill(INF_NEG);
        for (let c = 0; c <= budget; ++c) {
            dp1u[c] = Math.max(curNotBuy1[c], curBuy1[c]);
        }
        dp1[u] = dp1u;
    }

    dfs(1);

    let ans = 0;
    for (let c = 0; c <= budget; ++c) {
        if (dp0[1][c] > ans) ans = dp0[1][c];
    }
    return ans;
}
```

## Php

```php
class Solution {
    private $present;
    private $future;
    private $budget;
    private $children;
    private const NEG_INF = -1000000000;

    /**
     * @param Integer $n
     * @param Integer[] $present
     * @param Integer[] $future
     * @param Integer[][] $hierarchy
     * @param Integer $budget
     * @return Integer
     */
    function maxProfit($n, $present, $future, $hierarchy, $budget) {
        $this->present = $present;
        $this->future  = $future;
        $this->budget  = $budget;
        $this->children = array_fill(0, $n + 1, []);
        foreach ($hierarchy as $edge) {
            $parent = $edge[0];
            $child  = $edge[1];
            $this->children[$parent][] = $child;
        }
        list($dpRoot, $_) = $this->dfs(1);
        $ans = 0;
        for ($c = 0; $c <= $budget; $c++) {
            if ($dpRoot[$c] > $ans) {
                $ans = $dpRoot[$c];
            }
        }
        return $ans;
    }

    private function dfs($u) {
        $B = $this->budget;

        // not buying u
        $not = array_fill(0, $B + 1, self::NEG_INF);
        $not[0] = 0;

        // buying u with full price (parent did NOT buy)
        $buyFull = array_fill(0, $B + 1, self::NEG_INF);
        $priceFull = $this->present[$u - 1];
        if ($priceFull <= $B) {
            $profitFull = $this->future[$u - 1] - $priceFull;
            $buyFull[$priceFull] = max($buyFull[$priceFull], $profitFull);
        }

        // buying u with discounted price (parent DID buy)
        $buyDisc = array_fill(0, $B + 1, self::NEG_INF);
        $priceDisc = intdiv($this->present[$u - 1], 2);
        if ($priceDisc <= $B) {
            $profitDisc = $this->future[$u - 1] - $priceDisc;
            $buyDisc[$priceDisc] = max($buyDisc[$priceDisc], $profitDisc);
        }

        foreach ($this->children[$u] as $v) {
            list($dp0Child, $dp1Child) = $this->dfs($v);

            // merge for not buying u (children see parent NOT bought)
            $not = $this->merge($not, $dp0Child);

            // merge for buying u with full price (children see parent BOUGHT)
            $buyFull = $this->merge($buyFull, $dp1Child);

            // merge for buying u with discounted price (children also see parent BOUGHT)
            $buyDisc = $this->merge($buyDisc, $dp1Child);
        }

        // combine scenarios
        $dp0 = array_fill(0, $B + 1, self::NEG_INF); // parent of u did NOT buy
        $dp1 = array_fill(0, $B + 1, self::NEG_INF); // parent of u DID buy

        for ($c = 0; $c <= $B; $c++) {
            $dp0[$c] = max($not[$c], $buyFull[$c]);
            $dp1[$c] = max($not[$c], $buyDisc[$c]);
        }

        return [$dp0, $dp1];
    }

    private function merge($base, $child) {
        $B = $this->budget;
        $new = array_fill(0, $B + 1, self::NEG_INF);
        for ($i = 0; $i <= $B; $i++) {
            if ($base[$i] == self::NEG_INF) continue;
            $maxJ = $B - $i;
            for ($j = 0; $j <= $maxJ; $j++) {
                if ($child[$j] == self::NEG_INF) continue;
                $val = $base[$i] + $child[$j];
                $idx = $i + $j;
                if ($val > $new[$idx]) {
                    $new[$idx] = $val;
                }
            }
        }
        return $new;
    }
}
```

## Swift

```swift
class Solution {
    var present: [Int] = []
    var future: [Int] = []
    var budget: Int = 0
    var children: [[Int]] = []
    let NEG = -1_000_000

    func merge(_ a: [Int], _ b: [Int]) -> [Int] {
        var res = Array(repeating: NEG, count: budget + 1)
        for i in 0...budget where a[i] > NEG / 2 {
            let av = a[i]
            let maxJ = budget - i
            if maxJ < 0 { continue }
            for j in 0...maxJ where b[j] > NEG / 2 {
                let val = av + b[j]
                if val > res[i + j] {
                    res[i + j] = val
                }
            }
        }
        return res
    }

    func dfs(_ u: Int) -> (dp0: [Int], dp1: [Int]) {
        var childDPs: [(dp0: [Int], dp1: [Int])] = []
        for v in children[u] {
            childDPs.append(dfs(v))
        }

        // Not buying u
        var notBuy0 = Array(repeating: NEG, count: budget + 1)
        var notBuy1 = Array(repeating: NEG, count: budget + 1)
        notBuy0[0] = 0
        notBuy1[0] = 0

        for child in childDPs {
            notBuy0 = merge(notBuy0, child.dp0)   // parent of child didn't buy
            notBuy1 = merge(notBuy1, child.dp0)   // u not bought, so children see no purchase
        }

        // Buying u when parent didn't buy (full price)
        var buy0 = Array(repeating: NEG, count: budget + 1)
        let costFull = present[u - 1]
        if costFull <= budget {
            let profitU = future[u - 1] - costFull
            buy0[costFull] = profitU
            var cur = buy0
            for child in childDPs {
                cur = merge(cur, child.dp1)       // children get discount because u bought
            }
            buy0 = cur
        }

        // Buying u when parent bought (discount)
        var buy1 = Array(repeating: NEG, count: budget + 1)
        let costDisc = present[u - 1] / 2
        if costDisc <= budget {
            let profitU = future[u - 1] - costDisc
            buy1[costDisc] = profitU
            var cur = buy1
            for child in childDPs {
                cur = merge(cur, child.dp1)
            }
            buy1 = cur
        }

        // Final dp arrays
        var dp0 = Array(repeating: NEG, count: budget + 1)
        var dp1 = Array(repeating: NEG, count: budget + 1)

        for c in 0...budget {
            dp0[c] = max(notBuy0[c], buy0[c])
            dp1[c] = max(notBuy1[c], buy1[c])
        }

        return (dp0, dp1)
    }

    func maxProfit(_ n: Int, _ present: [Int], _ future: [Int], _ hierarchy: [[Int]], _ budget: Int) -> Int {
        self.present = present
        self.future = future
        self.budget = budget
        children = Array(repeating: [], count: n + 1)
        for edge in hierarchy {
            let u = edge[0]
            let v = edge[1]
            children[u].append(v)
        }
        let (dpRoot, _) = dfs(1)
        var ans = 0
        for c in 0...budget {
            if dpRoot[c] > ans { ans = dpRoot[c] }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxProfit(n: Int, present: IntArray, future: IntArray, hierarchy: Array<IntArray>, budget: Int): Int {
        val children = Array(n + 1) { mutableListOf<Int>() }
        for (edge in hierarchy) {
            val u = edge[0]
            val v = edge[1]
            children[u].add(v)
        }
        val INF_NEG = -1_000_000_0
        val dp0 = Array(n + 1) { IntArray(budget + 1) { INF_NEG } }
        val dp1 = Array(n + 1) { IntArray(budget + 1) { INF_NEG } }

        fun dfs(u: Int) {
            // Option A: not buying u, children see parent not bought -> use dp0 of child
            var curA = IntArray(budget + 1) { INF_NEG }
            curA[0] = 0
            for (v in children[u]) {
                dfs(v)
                val childDP0 = dp0[v]
                val newA = IntArray(budget + 1) { INF_NEG }
                for (i in 0..budget) {
                    if (curA[i] == INF_NEG) continue
                    for (j in 0..budget - i) {
                        val cv = childDP0[j]
                        if (cv == INF_NEG) continue
                        val nv = curA[i] + cv
                        if (nv > newA[i + j]) newA[i + j] = nv
                    }
                }
                curA = newA
            }

            // Option B: buying u without discount, children see parent bought -> use dp1 of child
            var curB = IntArray(budget + 1) { INF_NEG }
            val costFull = present[u - 1]
            if (costFull <= budget) {
                curB[costFull] = future[u - 1] - costFull
            }
            for (v in children[u]) {
                val childDP1 = dp1[v]
                val newB = IntArray(budget + 1) { INF_NEG }
                for (i in 0..budget) {
                    if (curB[i] == INF_NEG) continue
                    for (j in 0..budget - i) {
                        val cv = childDP1[j]
                        if (cv == INF_NEG) continue
                        val nv = curB[i] + cv
                        if (nv > newB[i + j]) newB[i + j] = nv
                    }
                }
                curB = newB
            }

            // dp0[u]: parent not bought, choose best of A and B
            for (b in 0..budget) {
                var best = curA[b]
                if (curB[b] > best) best = curB[b]
                dp0[u][b] = best
            }

            // Option B with discount when parent bought
            var curB1 = IntArray(budget + 1) { INF_NEG }
            val costDisc = present[u - 1] / 2
            if (costDisc <= budget) {
                curB1[costDisc] = future[u - 1] - costDisc
            }
            for (v in children[u]) {
                val childDP1 = dp1[v]
                val newB1 = IntArray(budget + 1) { INF_NEG }
                for (i in 0..budget) {
                    if (curB1[i] == INF_NEG) continue
                    for (j in 0..budget - i) {
                        val cv = childDP1[j]
                        if (cv == INF_NEG) continue
                        val nv = curB1[i] + cv
                        if (nv > newB1[i + j]) newB1[i + j] = nv
                    }
                }
                curB1 = newB1
            }

            // dp1[u]: parent bought, choose best of not buying (curA) and buying with discount (curB1)
            for (b in 0..budget) {
                var best = curA[b]
                if (curB1[b] > best) best = curB1[b]
                dp1[u][b] = best
            }
        }

        dfs(1)

        var ans = 0
        for (b in 0..budget) {
            val v = dp0[1][b]
            if (v > ans) ans = v
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maxProfit(int n, List<int> present, List<int> future,
      List<List<int>> hierarchy, int budget) {
    // Build adjacency list for the tree (parent -> children)
    List<List<int>> children = List.generate(n + 1, (_) => []);
    for (var edge in hierarchy) {
      int u = edge[0];
      int v = edge[1];
      children[u].add(v);
    }

    const int NEG_INF = -1000000000;

    // Returns a pair [dp0, dp1] where:
    // dp0[c] = max profit in subtree when parent of this node did NOT buy
    // dp1[c] = max profit in subtree when parent of this node DID buy
    List<List<int>> dfs(int u) {
      // Process all children first
      List<List<int>> childDPs = [];
      for (int v in children[u]) {
        childDPs.add(dfs(v));
      }

      // Combine children's dp0 when current node is NOT bought (skip case)
      List<int> skip = List.filled(budget + 1, NEG_INF);
      skip[0] = 0;
      for (var pair in childDPs) {
        List<int> dp0c = pair[0];
        List<int> newSkip = List.filled(budget + 1, NEG_INF);
        for (int i = 0; i <= budget; ++i) {
          if (skip[i] == NEG_INF) continue;
          for (int j = 0; j + i <= budget; ++j) {
            if (dp0c[j] == NEG_INF) continue;
            int val = skip[i] + dp0c[j];
            if (val > newSkip[i + j]) newSkip[i + j] = val;
          }
        }
        skip = newSkip;
      }

      // Combine children's dp1 when current node IS bought (discounted children)
      List<int> childBuy = List.filled(budget + 1, NEG_INF);
      childBuy[0] = 0;
      for (var pair in childDPs) {
        List<int> dp1c = pair[1];
        List<int> newChildBuy = List.filled(budget + 1, NEG_INF);
        for (int i = 0; i <= budget; ++i) {
          if (childBuy[i] == NEG_INF) continue;
          for (int j = 0; j + i <= budget; ++j) {
            if (dp1c[j] == NEG_INF) continue;
            int val = childBuy[i] + dp1c[j];
            if (val > newChildBuy[i + j]) newChildBuy[i + j] = val;
          }
        }
        childBuy = newChildBuy;
      }

      // Initialize dp0 and dp1 with the skip scenario (not buying current node)
      List<int> dp0 = List.from(skip);
      List<int> dp1 = List.from(skip);

      // Buying current node when parent did NOT buy
      int priceFull = present[u - 1];
      int profitFull = future[u - 1] - priceFull;
      for (int c = 0; c + priceFull <= budget; ++c) {
        if (childBuy[c] == NEG_INF) continue;
        int totalCost = c + priceFull;
        int val = profitFull + childBuy[c];
        if (val > dp0[totalCost]) dp0[totalCost] = val;
      }

      // Buying current node when parent DID buy (discounted price)
      int priceDisc = present[u - 1] ~/ 2;
      int profitDisc = future[u - 1] - priceDisc;
      for (int c = 0; c + priceDisc <= budget; ++c) {
        if (childBuy[c] == NEG_INF) continue;
        int totalCost = c + priceDisc;
        int val = profitDisc + childBuy[c];
        if (val > dp1[totalCost]) dp1[totalCost] = val;
      }

      return [dp0, dp1];
    }

    List<int> rootDP0 = dfs(1)[0];
    int answer = 0;
    for (int c = 0; c <= budget; ++c) {
      if (rootDP0[c] > answer) answer = rootDP0[c];
    }
    return answer;
  }
}
```

## Golang

```go
var (
	B          int
	tree       [][]int
	presentArr []int
	futureArr  []int
)

const INF = -1 << 60

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func dfs(u int) ([]int, []int) {
	// curNot: u not bought
	curNot := make([]int, B+1)
	for i := 0; i <= B; i++ {
		curNot[i] = INF
	}
	curNot[0] = 0

	// curBuyFull: u bought with full price (parent didn't buy)
	costFull := presentArr[u-1]
	profitFull := futureArr[u-1] - costFull
	curBuyFull := make([]int, B+1)
	for i := 0; i <= B; i++ {
		curBuyFull[i] = INF
	}
	if costFull <= B {
		curBuyFull[costFull] = profitFull
	}

	// curBuyDisc: u bought with discounted price (parent bought)
	costDisc := presentArr[u-1] / 2
	profitDisc := futureArr[u-1] - costDisc
	curBuyDisc := make([]int, B+1)
	for i := 0; i <= B; i++ {
		curBuyDisc[i] = INF
	}
	if costDisc <= B {
		curBuyDisc[costDisc] = profitDisc
	}

	for _, v := range tree[u] {
		child0, child1 := dfs(v)

		// merge for curNot using child's dp0 (parent not bought, u not bought)
		nxtNot := make([]int, B+1)
		for i := 0; i <= B; i++ {
			nxtNot[i] = INF
		}
		for c := 0; c <= B; c++ {
			if curNot[c] == INF {
				continue
			}
			for k := 0; k+c <= B; k++ {
				val := child0[k]
				if val == INF {
					continue
				}
				nc := c + k
				profit := curNot[c] + val
				if profit > nxtNot[nc] {
					nxtNot[nc] = profit
				}
			}
		}
		curNot = nxtNot

		// merge for curBuyFull using child's dp1 (u bought)
		nxtBuyFull := make([]int, B+1)
		for i := 0; i <= B; i++ {
			nxtBuyFull[i] = INF
		}
		for c := 0; c <= B; c++ {
			if curBuyFull[c] == INF {
				continue
			}
			for k := 0; k+c <= B; k++ {
				val := child1[k]
				if val == INF {
					continue
				}
				nc := c + k
				profit := curBuyFull[c] + val
				if profit > nxtBuyFull[nc] {
					nxtBuyFull[nc] = profit
				}
			}
		}
		curBuyFull = nxtBuyFull

		// merge for curBuyDisc using child's dp1 (u bought with discount)
		nxtBuyDisc := make([]int, B+1)
		for i := 0; i <= B; i++ {
			nxtBuyDisc[i] = INF
		}
		for c := 0; c <= B; c++ {
			if curBuyDisc[c] == INF {
				continue
			}
			for k := 0; k+c <= B; k++ {
				val := child1[k]
				if val == INF {
					continue
				}
				nc := c + k
				profit := curBuyDisc[c] + val
				if profit > nxtBuyDisc[nc] {
					nxtBuyDisc[nc] = profit
				}
			}
		}
		curBuyDisc = nxtBuyDisc
	}

	dp0 := make([]int, B+1)
	for i := 0; i <= B; i++ {
		dp0[i] = max(curNot[i], curBuyFull[i])
	}
	dp1 := make([]int, B+1)
	for i := 0; i <= B; i++ {
		dp1[i] = max(curNot[i], curBuyDisc[i])
	}
	return dp0, dp1
}

func maxProfit(n int, present []int, future []int, hierarchy [][]int, budget int) int {
	B = budget
	presentArr = present
	futureArr = future
	tree = make([][]int, n+1)
	for _, e := range hierarchy {
		u, v := e[0], e[1]
		tree[u] = append(tree[u], v)
	}
	dpRoot, _ := dfs(1)
	ans := 0
	for i := 0; i <= budget; i++ {
		if dpRoot[i] > ans {
			ans = dpRoot[i]
		}
	}
	return ans
}
```

## Ruby

```ruby
def max_profit(n, present, future, hierarchy, budget)
  adj = Array.new(n) { [] }
  hierarchy.each do |u, v|
    adj[u - 1] << (v - 1)
  end

  INF_NEG = -10**9

  dfs = lambda do |u|
    child_results = []
    adj[u].each do |v|
      dp0_child, dp1_child = dfs.call(v)
      child_results << [dp0_child, dp1_child]
    end

    # Scenario: not buying u (children see parent not bought)
    cur_not_buy = Array.new(budget + 1, INF_NEG)
    cur_not_buy[0] = 0
    child_results.each do |dp0_child, _|
      new_cur = Array.new(budget + 1, INF_NEG)
      (0..budget).each do |i|
        next if cur_not_buy[i] == INF_NEG
        max_j = budget - i
        (0..max_j).each do |j|
          val = dp0_child[j]
          next if val == INF_NEG
          nv = cur_not_buy[i] + val
          new_cur[i + j] = nv if nv > new_cur[i + j]
        end
      end
      cur_not_buy = new_cur
    end

    # Scenario: buying u when parent has NOT bought (full price)
    cost_full = present[u]
    profit_full = future[u] - cost_full
    cur_buy_no_parent = Array.new(budget + 1, INF_NEG)
    if cost_full <= budget
      cur_buy_no_parent[cost_full] = profit_full
      child_results.each do |_, dp1_child|
        new_cur = Array.new(budget + 1, INF_NEG)
        (0..budget).each do |i|
          next if cur_buy_no_parent[i] == INF_NEG
          max_j = budget - i
          (0..max_j).each do |j|
            val = dp1_child[j]
            next if val == INF_NEG
            nv = cur_buy_no_parent[i] + val
            new_cur[i + j] = nv if nv > new_cur[i + j]
          end
        end
        cur_buy_no_parent = new_cur
      end
    end

    dp0 = Array.new(budget + 1, INF_NEG)
    (0..budget).each do |k|
      best = cur_not_buy[k]
      b2 = cur_buy_no_parent[k]
      best = b2 if b2 > best
      dp0[k] = best
    end

    # Scenario: buying u when parent HAS bought (discounted price)
    cost_disc = present[u] / 2
    profit_disc = future[u] - cost_disc
    cur_buy_parent = Array.new(budget + 1, INF_NEG)
    if cost_disc <= budget
      cur_buy_parent[cost_disc] = profit_disc
      child_results.each do |_, dp1_child|
        new_cur = Array.new(budget + 1, INF_NEG)
        (0..budget).each do |i|
          next if cur_buy_parent[i] == INF_NEG
          max_j = budget - i
          (0..max_j).each do |j|
            val = dp1_child[j]
            next if val == INF_NEG
            nv = cur_buy_parent[i] + val
            new_cur[i + j] = nv if nv > new_cur[i + j]
          end
        end
        cur_buy_parent = new_cur
      end
    end

    dp1 = Array.new(budget + 1, INF_NEG)
    (0..budget).each do |k|
      best = cur_not_buy[k]
      b2 = cur_buy_parent[k]
      best = b2 if b2 > best
      dp1[k] = best
    end

    [dp0, dp1]
  end

  dp_root0, _ = dfs.call(0)
  ans = 0
  (0..budget).each do |c|
    val = dp_root0[c]
    ans = val if val > ans
  end
  ans
end
```

## Scala

```scala
object Solution {
  def maxProfit(n: Int, present: Array[Int], future: Array[Int],
                hierarchy: Array[Array[Int]], budget: Int): Int = {

    val INF_NEG = -100000000
    val B = budget

    // build tree adjacency list (children)
    val children = Array.fill(n + 1)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (edge <- hierarchy) {
      val u = edge(0)
      val v = edge(1)
      children(u) += v
    }

    def combine(a: Array[Int], b: Array[Int]): Array[Int] = {
      val res = Array.fill(B + 1)(INF_NEG)
      var i = 0
      while (i <= B) {
        if (a(i) > INF_NEG) {
          var j = 0
          while (j <= B - i) {
            if (b(j) > INF_NEG) {
              val v = a(i) + b(j)
              if (v > res(i + j)) res(i + j) = v
            }
            j += 1
          }
        }
        i += 1
      }
      res
    }

    def dfs(u: Int): (Array[Int], Array[Int]) = {
      // not buying u, children see parent not bought -> use dp0 of child
      var notBuyDP = Array.fill(B + 1)(INF_NEG)
      notBuyDP(0) = 0

      val childResults = scala.collection.mutable.ArrayBuffer.empty[(Array[Int], Array[Int])]

      for (v <- children(u)) {
        val res = dfs(v)
        childResults += res
        notBuyDP = combine(notBuyDP, res._1) // use child's dp0
      }

      // buying u at full price (parent hasn't bought)
      var buyFullDP = Array.fill(B + 1)(INF_NEG)
      val costFull = present(u - 1)
      if (costFull <= B) {
        buyFullDP(costFull) = future(u - 1) - costFull
      }
      for ((c0, c1) <- childResults) {
        buyFullDP = combine(buyFullDP, c1) // children see u bought
      }

      val dp0 = Array.fill(B + 1)(INF_NEG)
      var i = 0
      while (i <= B) {
        var best = notBuyDP(i)
        if (buyFullDP(i) > best) best = buyFullDP(i)
        dp0(i) = best
        i += 1
      }

      // buying u at discounted price (parent has bought)
      var buyDiscDP = Array.fill(B + 1)(INF_NEG)
      val costDisc = present(u - 1) / 2
      if (costDisc <= B) {
        buyDiscDP(costDisc) = future(u - 1) - costDisc
      }
      for ((c0, c1) <- childResults) {
        buyDiscDP = combine(buyDiscDP, c1)
      }

      val dp1 = Array.fill(B + 1)(INF_NEG)
      i = 0
      while (i <= B) {
        var best = notBuyDP(i) // same not-buy scenario
        if (buyDiscDP(i) > best) best = buyDiscDP(i)
        dp1(i) = best
        i += 1
      }

      (dp0, dp1)
    }

    val (rootDP0, _) = dfs(1)

    var answer = 0
    var k = 0
    while (k <= B) {
      if (rootDP0(k) > answer) answer = rootDP0(k)
      k += 1
    }
    answer
  }
}
```

## Rust

```rust
use std::cmp::max;

pub struct Solution;

impl Solution {
    pub fn max_profit(
        n: i32,
        present: Vec<i32>,
        future: Vec<i32>,
        hierarchy: Vec<Vec<i32>>,
        budget: i32,
    ) -> i32 {
        let n_usize = n as usize;
        let bud = budget as usize;
        let mut children: Vec<Vec<usize>> = vec![Vec::new(); n_usize];
        for edge in hierarchy.iter() {
            let u = (edge[0] - 1) as usize;
            let v = (edge[1] - 1) as usize;
            children[u].push(v);
        }
        const NEG_INF: i32 = -1_000_000;

        fn dfs(
            u: usize,
            children: &Vec<Vec<usize>>,
            present: &Vec<i32>,
            future: &Vec<i32>,
            bud: usize,
        ) -> (Vec<i32>, Vec<i32>) {
            const NEG_INF: i32 = -1_000_000;
            // gather children's dp results
            let mut child_infos: Vec<(Vec<i32>, Vec<i32>)> = Vec::new();
            for &v in &children[u] {
                child_infos.push(dfs(v, children, present, future, bud));
            }

            // not buying u -> children use dp0
            let mut not_buy = vec![NEG_INF; bud + 1];
            not_buy[0] = 0;
            for (dp0_child, _) in &child_infos {
                let mut new_nb = vec![NEG_INF; bud + 1];
                for i in 0..=bud {
                    if not_buy[i] == NEG_INF {
                        continue;
                    }
                    for j in 0..=bud - i {
                        let val_c = dp0_child[j];
                        if val_c == NEG_INF {
                            continue;
                        }
                        let cand = not_buy[i] + val_c;
                        if cand > new_nb[i + j] {
                            new_nb[i + j] = cand;
                        }
                    }
                }
                not_buy = new_nb;
            }

            // buying u -> children use dp1
            let mut buy_children = vec![NEG_INF; bud + 1];
            buy_children[0] = 0;
            for (_, dp1_child) in &child_infos {
                let mut new_bc = vec![NEG_INF; bud + 1];
                for i in 0..=bud {
                    if buy_children[i] == NEG_INF {
                        continue;
                    }
                    for j in 0..=bud - i {
                        let val_c = dp1_child[j];
                        if val_c == NEG_INF {
                            continue;
                        }
                        let cand = buy_children[i] + val_c;
                        if cand > new_bc[i + j] {
                            new_bc[i + j] = cand;
                        }
                    }
                }
                buy_children = new_bc;
            }

            // initialize dp0 and dp1 with not buying case
            let mut dp0_u = not_buy.clone();
            let mut dp1_u = not_buy.clone();

            // buying u without discount (parent didn't buy)
            let price_full = present[u] as usize;
            let profit_full = future[u] - present[u];
            if price_full <= bud {
                for total in price_full..=bud {
                    let rem = total - price_full;
                    if buy_children[rem] != NEG_INF {
                        let cand = profit_full + buy_children[rem];
                        dp0_u[total] = max(dp0_u[total], cand);
                    }
                }
            }

            // buying u with discount (parent bought)
            let price_disc = (present[u] / 2) as usize;
            let profit_disc = future[u] - (present[u] / 2);
            if price_disc <= bud {
                for total in price_disc..=bud {
                    let rem = total - price_disc;
                    if buy_children[rem] != NEG_INF {
                        let cand = profit_disc + buy_children[rem];
                        dp1_u[total] = max(dp1_u[total], cand);
                    }
                }
            }

            (dp0_u, dp1_u)
        }

        let (dp0_root, _) = dfs(0, &children, &present, &future, bud);
        let mut ans = 0;
        for cost in 0..=bud {
            if dp0_root[cost] > ans {
                ans = dp0_root[cost];
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (max-profit n present future hierarchy budget)
  (-> exact-integer?
      (listof exact-integer?)
      (listof exact-integer?)
      (listof (listof exact-integer?))
      exact-integer?
      exact-integer?)

  (let* ((INF -1000000000)

         ;; build adjacency list
         (adj (let ((v (make-vector (+ n 1) '())))
                (for ([e hierarchy])
                  (let ((u (first e)) (v-child (second e)))
                    (vector-set! v u (cons v-child (vector-ref v u)))))
                v))

         ;; merge two DP vectors under budget constraint
         (define (merge dp1 dp2)
           (let ((new (make-vector (+ budget 1) INF)))
             (for ([i (in-range 0 (+ budget 1))])
               (let ((val-i (vector-ref dp1 i)))
                 (when (> val-i INF)
                   (for ([j (in-range 0 (- (+ budget 1) i))])
                     (let ((val-j (vector-ref dp2 j)))
                       (when (> val-j INF)
                         (let* ((idx (+ i j))
                                (cand (+ val-i val-j)))
                           (when (> cand (vector-ref new idx))
                             (vector-set! new idx cand)))))))))
             new))

         ;; depth‑first search returning two DP tables:
         ;; dp0 – parent didn't buy, dp1 – parent bought
         (define (dfs u)
           (let* ((children (vector-ref adj u))
                  (child-dps (map dfs children))   ; list of (dp0 dp1) pairs

                  ;; ---------- case: parent did NOT buy ----------
                  ;; 1) do NOT buy u, children use their dp0
                  (dp-notbuy (let ((dp (make-vector (+ budget 1) INF)))
                               (vector-set! dp 0 0)
                               (for ([pair child-dps])
                                 (let-values ([(c0 c1) pair])
                                   (set! dp (merge dp c0))))
                               dp))

                  ;; 2) buy u at full price, children use their dp1
                  (price-full (list-ref present (- u 1)))
                  (profit-full (- (list-ref future (- u 1)) price-full))
                  (dp-buyfull (let ((dp (make-vector (+ budget 1) INF)))
                                (when (<= price-full budget)
                                  (vector-set! dp price-full profit-full))
                                (for ([pair child-dps])
                                  (let-values ([(c0 c1) pair])
                                    (set! dp (merge dp c1))))
                                dp))

                  ;; combine both possibilities for dp0
                  (dp0 (make-vector (+ budget 1) INF))
                  (_ (for ([i (in-range 0 (+ budget 1))])
                       (vector-set! dp0 i
                                    (max (vector-ref dp-notbuy i)
                                         (vector-ref dp-buyfull i)))))

                  ;; ---------- case: parent DID buy ----------
                  ;; 1) do NOT buy u, children see parent not bought -> use dp0
                  (dp-nobuy-parent (let ((dp (make-vector (+ budget 1) INF)))
                                     (vector-set! dp 0 0)
                                     (for ([pair child-dps])
                                       (let-values ([(c0 c1) pair])
                                         (set! dp (merge dp c0))))
                                     dp))

                  ;; 2) buy u at discounted price, children use dp1
                  (price-disc (quotient price-full 2))
                  (profit-disc (- (list-ref future (- u 1)) price-disc))
                  (dp-buydisc (let ((dp (make-vector (+ budget 1) INF)))
                                (when (<= price-disc budget)
                                  (vector-set! dp price-disc profit-disc))
                                (for ([pair child-dps])
                                  (let-values ([(c0 c1) pair])
                                    (set! dp (merge dp c1))))
                                dp))

                  ;; combine both possibilities for dp1
                  (dp1 (make-vector (+ budget 1) INF))
                  (_ (for ([i (in-range 0 (+ budget 1))])
                       (vector-set! dp1 i
                                    (max (vector-ref dp-nobuy-parent i)
                                         (vector-ref dp-buydisc i))))))
             (values dp0 dp1)))

         ;; compute DP for the CEO (node 1); its parent is considered NOT bought
         (define-values (root0 root1) (dfs 1))

         ;; answer: best profit with total cost ≤ budget from root0
         (ans (let ((best -INF))
                (for ([c (in-range 0 (+ budget 1))])
                  (let ((p (vector-ref root0 c)))
                    (when (> p best) (set! best p))))
                best)))
    ans))
```

## Erlang

```erlang
-define(NEG_INF, -1000000000).

-spec max_profit(N :: integer(), Present :: [integer()], Future :: [integer()], Hierarchy :: [[integer()]], Budget :: integer()) -> integer().
max_profit(_N, PresentList, FutureList, Hierarchy, B) ->
    Present = list_to_tuple([0 | PresentList]),
    Future  = list_to_tuple([0 | FutureList]),
    Adj = build_adj(Hierarchy, #{}),
    {F0Root, _} = dfs(1, Adj, Present, Future, B),
    max_over_budget(F0Root, B).

%% Build adjacency map: parent -> [children]
build_adj([], Adj) -> Adj;
build_adj([[U,V]|Rest], Adj) ->
    Children = maps:get(U, Adj, []),
    NewAdj = maps:put(U, [V|Children], Adj),
    build_adj(Rest, NewAdj).

%% Depth‑first DP
dfs(Node, Adj, Present, Future, B) ->
    Children = maps:get(Node, Adj, []),

    %% Combine children's DP tables
    {ChildNoBuy0, ChildIfParentBought0} =
        lists:foldl(
            fun(Ch, {Acc0, Acc1}) ->
                {F0C, F1C} = dfs(Ch, Adj, Present, Future, B),
                NewAcc0 = combine_tuples(Acc0, F0C, B),
                NewAcc1 = combine_tuples(Acc1, F1C, B),
                {NewAcc0, NewAcc1}
            end,
            {make_base(B), make_base(B)},
            Children),

    CostFull = element(Node, Present),
    CostDisc = CostFull div 2,
    ProfitFull = element(Node, Future) - CostFull,
    ProfitDisc = element(Node, Future) - CostDisc,

    F0 = compute_state(ChildNoBuy0, ChildIfParentBought0, B, CostFull, ProfitFull),
    F1 = compute_state(ChildNoBuy0, ChildIfParentBought0, B, CostDisc, ProfitDisc),

    {F0, F1}.

%% Compute DP for a node given child tables and purchase cost/profit
compute_state(ChildNoBuy, ChildIfParentBought, B, Cost, Profit) ->
    List = [ 
        NotBuy = element(Budget+1, ChildNoBuy),
        Buy =
            case Budget >= Cost of
                true ->
                    ChildPart = element((Budget - Cost)+1, ChildIfParentBought),
                    if ChildPart =:= ?NEG_INF -> ?NEG_INF;
                       true -> Profit + ChildPart
                    end;
                false -> ?NEG_INF
            end,
        if Buy > NotBuy -> Buy; true -> NotBuy end
     || Budget <- lists:seq(0, B)
    ],
    list_to_tuple(List).

%% Combine two DP tables (knapsack convolution)
combine_tuples(Old, Child, B) ->
    List = [ max_split(Total, Old, Child) || Total <- lists:seq(0, B) ],
    list_to_tuple(List).

max_split(Total, Old, Child) ->
    max_split_k(0, Total, Old, Child, ?NEG_INF).

max_split_k(K, Total, _Old, _Child, Max) when K > Total -> Max;
max_split_k(K, Total, Old, Child, Max) ->
    ValOld   = element((Total - K)+1, Old),
    ValChild = element(K+1, Child),
    NewMax =
        if ValOld =:= ?NEG_INF orelse ValChild =:= ?NEG_INF -> Max;
           true ->
               Cand = ValOld + ValChild,
               if Cand > Max -> Cand; true -> Max end
        end,
    max_split_k(K+1, Total, Old, Child, NewMax).

%% Base DP table: profit 0 with 0 cost, otherwise -inf
make_base(B) ->
    list_to_tuple([0 | lists:duplicate(B, ?NEG_INF)]).

%% Maximum profit achievable within budget B
max_over_budget(Tuple, B) ->
    lists:max([element(I+1, Tuple) || I <- lists:seq(0, B)]).
```

## Elixir

```elixir
defmodule Solution do
  @inf_neg -1_000_000

  @spec max_profit(n :: integer, present :: [integer], future :: [integer], hierarchy :: [[integer]], budget :: integer) :: integer
  def max_profit(n, present, future, hierarchy, budget) do
    adj =
      Enum.reduce(1..n, %{}, fn i, acc -> Map.put(acc, i, []) end)
      |> Enum.reduce(hierarchy, fn [u, v], acc ->
        Map.update!(acc, u, fn lst -> [v | lst] end)
      end)

    {dp0_root, _dp1_root} = dfs(1, adj, present, future, budget)

    0..budget
    |> Enum.map(fn c -> elem(dp0_root, c + 1) end)
    |> Enum.max()
  end

  defp init_dp(budget), do: :erlang.make_tuple(budget + 1, @inf_neg)

  defp combine(acc, child, budget) do
    Enum.reduce(0..budget, init_dp(budget), fn i, new_acc ->
      a = elem(acc, i + 1)

      if a > @inf_neg do
        max_j = budget - i

        Enum.reduce(0..max_j, new_acc, fn j, inner_acc ->
          b = elem(child, j + 1)

          if b > @inf_neg do
            idx = i + j
            cur = elem(inner_acc, idx + 1)
            val = a + b

            if val > cur,
              do: put_elem(inner_acc, idx + 1, val),
              else: inner_acc
          else
            inner_acc
          end
        end)
      else
        new_acc
      end
    end)
  end

  defp add_purchase(base_dp, child_dp, price, profit_gain, budget) do
    if price > budget do
      base_dp
    else
      Enum.reduce(0..(budget - price), base_dp, fn c, acc ->
        child_profit = elem(child_dp, c + 1)

        if child_profit > @inf_neg do
          total_cost = c + price
          cur = elem(acc, total_cost + 1)
          val = child_profit + profit_gain

          if val > cur,
            do: put_elem(acc, total_cost + 1, val),
            else: acc
        else
          acc
        end
      end)
    end
  end

  defp dfs(u, adj, present, future, budget) do
    children = Map.get(adj, u, [])

    {children_no_buy, children_parent_bought} =
      Enum.reduce(children, {init_dp(budget) |> put_elem(1, 0), init_dp(budget) |> put_elem(1, 0)}, fn v,
                                                                                                         {cur0, cur1} ->
        {child0, child1} = dfs(v, adj, present, future, budget)
        new0 = combine(cur0, child0, budget)
        new1 = combine(cur1, child1, budget)
        {new0, new1}
      end)

    price = Enum.at(present, u - 1)
    profit_gain = Enum.at(future, u - 1) - price

    dp0 =
      children_no_buy
      |> add_purchase(children_parent_bought, price, profit_gain, budget)

    disc_price = div(price, 2)
    profit_gain_disc = Enum.at(future, u - 1) - disc_price

    dp1 =
      children_no_buy
      |> add_purchase(children_parent_bought, disc_price, profit_gain_disc, budget)

    {dp0, dp1}
  end
end
```
