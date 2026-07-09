# 3575. Maximum Good Subtree Score

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    static const int MOD = 1000000007;
    vector<vector<int>> children;
    vector<long long> maxScore;
    vector<int> nodeMask;
    vector<int> vals;
    
    // compute digit mask, return -1 if duplicate digits within the number
    int getMask(int x) {
        int mask = 0;
        while (x > 0) {
            int d = x % 10;
            if (mask & (1 << d)) return -1; // duplicate digit
            mask |= 1 << d;
            x /= 10;
        }
        return mask;
    }
    
    vector<long long> dfs(int u) {
        const long long NEG = -(1LL<<60);
        vector<long long> dp(1<<10, NEG);
        dp[0] = 0; // empty set
        
        for (int v : children[u]) {
            vector<long long> childDP = dfs(v);
            vector<long long> ndp = dp;
            for (int m1 = 0; m1 < (1<<10); ++m1) if (dp[m1] != NEG) {
                for (int m2 = 0; m2 < (1<<10); ++m2) if (childDP[m2] != NEG && !(m1 & m2)) {
                    int nm = m1 | m2;
                    ndp[nm] = max(ndp[nm], dp[m1] + childDP[m2]);
                }
            }
            dp.swap(ndp);
        }
        
        // consider taking the current node itself
        int ownMask = nodeMask[u];
        if (ownMask != -1) {
            vector<long long> ndp = dp;
            for (int m = 0; m < (1<<10); ++m) if (dp[m] != NEG && !(m & ownMask)) {
                int nm = m | ownMask;
                ndp[nm] = max(ndp[nm], dp[m] + vals[u]);
            }
            dp.swap(ndp);
        }
        
        long long best = 0;
        for (long long v : dp) if (v > best) best = v;
        maxScore[u] = best;
        return dp;
    }
    
    int goodSubtreeSum(vector<int>& vals_, vector<int>& par) {
        vals = vals_;
        int n = vals.size();
        children.assign(n, {});
        for (int i = 1; i < n; ++i) {
            children[par[i]].push_back(i);
        }
        nodeMask.resize(n);
        for (int i = 0; i < n; ++i) nodeMask[i] = getMask(vals[i]);
        maxScore.assign(n, 0);
        dfs(0);
        long long ans = 0;
        for (long long v : maxScore) {
            ans += v;
            if (ans >= MOD) ans %= MOD;
        }
        return int(ans % MOD);
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static final int DIGIT_COUNT = 10;
    private static final int MASK_SIZE = 1 << DIGIT_COUNT;
    private static final long NEG = -1L;
    private List<Integer>[] children;
    private long[] maxScore;
    private int[] vals;

    public int goodSubtreeSum(int[] vals, int[] par) {
        int n = vals.length;
        this.vals = vals;
        children = new ArrayList[n];
        for (int i = 0; i < n; i++) children[i] = new ArrayList<>();
        for (int i = 1; i < n; i++) {
            children[par[i]].add(i);
        }
        maxScore = new long[n];
        dfs(0);
        long mod = 1_000_000_007L;
        long ans = 0;
        for (long v : maxScore) {
            ans += v;
            if (ans >= mod) ans -= mod;
        }
        return (int)(ans % mod);
    }

    private long[] dfs(int u) {
        long[] dp = new long[MASK_SIZE];
        Arrays.fill(dp, NEG);
        dp[0] = 0L;

        for (int v : children[u]) {
            long[] childDP = dfs(v);
            long[] ndp = new long[MASK_SIZE];
            Arrays.fill(ndp, NEG);
            for (int m1 = 0; m1 < MASK_SIZE; m1++) {
                if (dp[m1] == NEG) continue;
                for (int m2 = 0; m2 < MASK_SIZE; m2++) {
                    if (childDP[m2] == NEG) continue;
                    if ((m1 & m2) != 0) continue;
                    int nm = m1 | m2;
                    long val = dp[m1] + childDP[m2];
                    if (val > ndp[nm]) ndp[nm] = val;
                }
            }
            dp = ndp;
        }

        int nodeMask = digitMask(vals[u]);
        if (nodeMask != -1) {
            long[] ndp = dp.clone();
            for (int m = 0; m < MASK_SIZE; m++) {
                if (dp[m] == NEG) continue;
                if ((m & nodeMask) != 0) continue;
                int nm = m | nodeMask;
                long val = dp[m] + vals[u];
                if (val > ndp[nm]) ndp[nm] = val;
            }
            dp = ndp;
        }

        long best = 0L;
        for (long v : dp) {
            if (v > best) best = v;
        }
        maxScore[u] = best;
        return dp;
    }

    private int digitMask(int x) {
        int mask = 0;
        while (x > 0) {
            int d = x % 10;
            int bit = 1 << d;
            if ((mask & bit) != 0) return -1; // duplicate digit in the same number
            mask |= bit;
            x /= 10;
        }
        return mask;
    }
}
```

## Python

```python
class Solution(object):
    def goodSubtreeSum(self, vals, par):
        """
        :type vals: List[int]
        :type par: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(vals)
        # build children list
        children = [[] for _ in range(n)]
        for i in range(1, n):
            p = par[i]
            children[p].append(i)

        # precompute digit mask; -1 if value has repeated digit
        masks = []
        for v in vals:
            seen = 0
            ok = True
            x = v
            while x > 0:
                d = x % 10
                bit = 1 << d
                if seen & bit:
                    ok = False
                    break
                seen |= bit
                x //= 10
            # handle value 0 (digit 0)
            if v == 0:
                if seen & 1:
                    ok = False
                else:
                    seen = 1
            masks.append(seen if ok else -1)

        maxScore = [0] * n

        def dfs(u):
            dp = [-1] * 1024
            dp[0] = 0
            for v in children[u]:
                child_dp = dfs(v)
                # merge dp with child_dp
                newdp = dp[:]  # keep existing selections (skip child)
                masks_a = [i for i, val in enumerate(dp) if val >= 0]
                masks_b = [i for i, val in enumerate(child_dp) if val >= 0]
                for a in masks_a:
                    sum_a = dp[a]
                    for b in masks_b:
                        if a & b:
                            continue
                        newmask = a | b
                        cand = sum_a + child_dp[b]
                        if cand > newdp[newmask]:
                            newdp[newmask] = cand
                dp = newdp

            # try to include current node itself if its value has unique digits
            mask_self = masks[u]
            if mask_self != -1:
                cur_masks = [i for i, val in enumerate(dp) if val >= 0]
                for a in cur_masks:
                    if a & mask_self:
                        continue
                    newmask = a | mask_self
                    cand = dp[a] + vals[u]
                    if cand > dp[newmask]:
                        dp[newmask] = cand

            maxScore[u] = max(dp)
            return dp

        dfs(0)

        total = sum(maxScore) % MOD
        return total
```

## Python3

```python
import sys
sys.setrecursionlimit(10000)
from typing import List

MOD = 10**9 + 7
FULL_MASK = 1 << 10  # 1024

class Solution:
    def goodSubtreeSum(self, vals: List[int], par: List[int]) -> int:
        n = len(vals)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            p = par[i]
            children[p].append(i)

        # precompute digit masks; -1 means value has duplicate digits and cannot be used
        node_mask = []
        for v in vals:
            mask = 0
            ok = True
            x = v
            while x:
                d = x % 10
                bit = 1 << d
                if mask & bit:
                    ok = False
                    break
                mask |= bit
                x //= 10
            node_mask.append(mask if ok else -1)

        max_scores = [0] * n

        def dfs(u: int):
            # dp[mask] = best sum for this subtree with used digits = mask
            dp = [-1] * FULL_MASK
            dp[0] = 0  # empty set

            # option to take the node itself if possible
            m = node_mask[u]
            if m != -1:
                dp[m] = max(dp[m], vals[u])

            for v in children[u]:
                child_dp = dfs(v)
                newdp = [-1] * FULL_MASK
                for mask1 in range(FULL_MASK):
                    if dp[mask1] < 0:
                        continue
                    # keep current combination without taking anything from child
                    if dp[mask1] > newdp[mask1]:
                        newdp[mask1] = dp[mask1]
                    for mask2 in range(FULL_MASK):
                        if child_dp[mask2] < 0:
                            continue
                        if mask1 & mask2:
                            continue
                        nm = mask1 | mask2
                        val_sum = dp[mask1] + child_dp[mask2]
                        if val_sum > newdp[nm]:
                            newdp[nm] = val_sum
                dp = newdp

            max_scores[u] = max(dp)
            return dp

        dfs(0)

        total = sum(max_scores) % MOD
        return total
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <limits.h>

typedef long long ll;
static const int MOD = 1000000007;
static const int MASK_SIZE = 1 << 10;          // 1024
static const ll NEG_INF = -(1LL<<60);

int goodSubtreeSum(int* vals, int valsSize, int* par, int parSize) {
    int n = valsSize;

    /* build children adjacency list */
    int *head = (int*)malloc(n * sizeof(int));
    int *next = (int*)malloc((n - 1) * sizeof(int));
    int *to   = (int*)malloc((n - 1) * sizeof(int));
    for (int i = 0; i < n; ++i) head[i] = -1;
    for (int i = 1, e = 0; i < n; ++i, ++e) {
        int p = par[i];
        to[e] = i;
        next[e] = head[p];
        head[p] = e;
    }

    /* compute digit masks and validity */
    int *mask = (int*)malloc(n * sizeof(int));
    char *valid = (char*)malloc(n * sizeof(char));
    for (int i = 0; i < n; ++i) {
        int v = vals[i];
        int m = 0;
        char ok = 1;
        if (v == 0) {
            m |= 1 << 0;
        } else {
            while (v > 0) {
                int d = v % 10;
                if (m & (1 << d)) { ok = 0; break; }
                m |= 1 << d;
                v /= 10;
            }
        }
        mask[i] = m;
        valid[i] = ok;
    }

    ll *maxScore = (ll*)malloc(n * sizeof(ll));
    for (int i = 0; i < n; ++i) maxScore[i] = 0;

    /* recursive DFS returning DP array */
    ll* dfs(int u) {
        ll *dp = (ll*)malloc(MASK_SIZE * sizeof(ll));
        for (int i = 0; i < MASK_SIZE; ++i) dp[i] = NEG_INF;
        dp[0] = 0;

        for (int e = head[u]; e != -1; e = next[e]) {
            int v = to[e];
            ll *childdp = dfs(v);
            ll *newdp = (ll*)malloc(MASK_SIZE * sizeof(ll));
            for (int i = 0; i < MASK_SIZE; ++i) newdp[i] = NEG_INF;

            for (int a = 0; a < MASK_SIZE; ++a) if (dp[a] > NEG_INF/2) {
                for (int b = 0; b < MASK_SIZE; ++b) if (childdp[b] > NEG_INF/2) {
                    if ((a & b) == 0) {
                        int nb = a | b;
                        ll val = dp[a] + childdp[b];
                        if (val > newdp[nb]) newdp[nb] = val;
                    }
                }
            }

            free(dp);
            free(childdp);
            dp = newdp;
        }

        if (valid[u]) {
            int m = mask[u];
            ll *newdp = (ll*)malloc(MASK_SIZE * sizeof(ll));
            memcpy(newdp, dp, MASK_SIZE * sizeof(ll));

            for (int a = 0; a < MASK_SIZE; ++a) if (dp[a] > NEG_INF/2) {
                if ((a & m) == 0) {
                    int nb = a | m;
                    ll val = dp[a] + (ll)vals[u];
                    if (val > newdp[nb]) newdp[nb] = val;
                }
            }

            free(dp);
            dp = newdp;
        }

        ll best = 0;
        for (int i = 0; i < MASK_SIZE; ++i)
            if (dp[i] > best) best = dp[i];
        maxScore[u] = best;

        return dp;
    }

    ll *rootdp = dfs(0);
    free(rootdp);

    ll total = 0;
    for (int i = 0; i < n; ++i) {
        total += maxScore[i] % MOD;
        if (total >= MOD) total -= MOD;
    }

    free(head);
    free(next);
    free(to);
    free(mask);
    free(valid);
    free(maxScore);

    return (int)(total % MOD);
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    const long MOD = 1000000007L;
    const int MASK_SIZE = 1 << 10;
    int[] vals;
    List<int>[] children;
    long[] maxScore;
    long negInf = long.MinValue / 4;

    public int GoodSubtreeSum(int[] vals, int[] par) {
        this.vals = vals;
        int n = vals.Length;
        children = new List<int>[n];
        for (int i = 0; i < n; i++) children[i] = new List<int>();
        for (int i = 1; i < n; i++) children[par[i]].Add(i);
        maxScore = new long[n];
        Dfs(0);
        long total = 0;
        foreach (var v in maxScore) {
            total += v;
            if (total >= MOD) total -= MOD;
        }
        return (int)(total % MOD);
    }

    private long[] Dfs(int u) {
        long[] dp = new long[MASK_SIZE];
        for (int i = 0; i < MASK_SIZE; i++) dp[i] = negInf;
        dp[0] = 0;

        foreach (int v in children[u]) {
            long[] childDp = Dfs(v);
            long[] ndp = new long[MASK_SIZE];
            Array.Copy(dp, ndp, MASK_SIZE); // keep existing without taking from child
            for (int m1 = 0; m1 < MASK_SIZE; m1++) {
                if (dp[m1] == negInf) continue;
                for (int m2 = 0; m2 < MASK_SIZE; m2++) {
                    if (childDp[m2] == negInf) continue;
                    if ((m1 & m2) != 0) continue;
                    int nm = m1 | m2;
                    long val = dp[m1] + childDp[m2];
                    if (val > ndp[nm]) ndp[nm] = val;
                }
            }
            dp = ndp;
        }

        int nodeMask = GetMask(vals[u]);
        if (nodeMask != -1) {
            long[] ndp = new long[MASK_SIZE];
            Array.Copy(dp, ndp, MASK_SIZE); // not taking the node
            for (int m = 0; m < MASK_SIZE; m++) {
                if (dp[m] == negInf) continue;
                if ((m & nodeMask) != 0) continue;
                int nm = m | nodeMask;
                long val = dp[m] + vals[u];
                if (val > ndp[nm]) ndp[nm] = val;
            }
            dp = ndp;
        }

        long best = 0;
        foreach (long v in dp) if (v > best) best = v;
        maxScore[u] = best;
        return dp;
    }

    private int GetMask(int x) {
        int mask = 0;
        while (x > 0) {
            int d = x % 10;
            int bit = 1 << d;
            if ((mask & bit) != 0) return -1; // duplicate digit
            mask |= bit;
            x /= 10;
        }
        return mask;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} vals
 * @param {number[]} par
 * @return {number}
 */
var goodSubtreeSum = function(vals, par) {
    const MOD = 1000000007;
    const n = vals.length;
    const children = Array.from({length: n}, () => []);
    for (let i = 1; i < n; ++i) {
        const p = par[i];
        children[p].push(i);
    }

    // compute digit mask for each value, -1 if a digit repeats inside the number
    const nodeMask = new Array(n);
    for (let i = 0; i < n; ++i) {
        let v = vals[i];
        let seen = 0;
        let ok = true;
        while (v > 0) {
            const d = v % 10;
            if ((seen >> d) & 1) { ok = false; break; }
            seen |= (1 << d);
            v = Math.floor(v / 10);
        }
        nodeMask[i] = ok ? seen : -1;
    }

    const maxScore = new Array(n).fill(0);

    function dfs(u) {
        // dp[mask] = max sum achievable in subtree u using exactly 'mask' digits
        let dp = new Array(1024).fill(-1);
        dp[0] = 0;

        for (const v of children[u]) {
            const childDP = dfs(v);
            const ndp = new Array(1024).fill(-1);
            for (let m1 = 0; m1 < 1024; ++m1) if (dp[m1] >= 0) {
                for (let m2 = 0; m2 < 1024; ++m2) if (childDP[m2] >= 0) {
                    if ((m1 & m2) === 0) {
                        const nm = m1 | m2;
                        const ns = dp[m1] + childDP[m2];
                        if (ns > ndp[nm]) ndp[nm] = ns;
                    }
                }
            }
            dp = ndp;
        }

        const maskU = nodeMask[u];
        if (maskU !== -1) {
            const old = dp.slice(); // snapshot before adding u
            for (let m = 0; m < 1024; ++m) if (old[m] >= 0 && (m & maskU) === 0) {
                const nm = m | maskU;
                const ns = old[m] + vals[u];
                if (ns > dp[nm]) dp[nm] = ns;
            }
        }

        let best = 0;
        for (let s of dp) if (s > best) best = s;
        maxScore[u] = best;
        return dp;
    }

    dfs(0);

    let total = 0;
    for (let v of maxScore) {
        total = (total + v) % MOD;
    }
    return total;
};
```

## Typescript

```typescript
function goodSubtreeSum(vals: number[], par: number[]): number {
    const MOD = 1_000_000_007;
    const n = vals.length;
    const children: number[][] = Array.from({ length: n }, () => []);
    for (let i = 1; i < n; ++i) {
        const p = par[i];
        children[p].push(i);
    }

    // compute digit masks, -1 if value has duplicate digits
    const nodeMask: number[] = new Array(n);
    for (let i = 0; i < n; ++i) {
        let v = vals[i];
        let mask = 0;
        let ok = true;
        while (v > 0) {
            const d = v % 10;
            if ((mask >> d) & 1) { ok = false; break; }
            mask |= 1 << d;
            v = Math.floor(v / 10);
        }
        nodeMask[i] = ok ? mask : -1;
    }

    const maxScore: number[] = new Array(n).fill(0);

    function dfs(u: number): number[] {
        let dp = new Array(1024).fill(-Infinity);
        dp[0] = 0;
        const m = nodeMask[u];
        if (m !== -1) {
            dp[m] = Math.max(dp[m], vals[u]);
        }

        for (const v of children[u]) {
            const childDP = dfs(v);
            const newDP = dp.slice(); // start with current possibilities (skip child)
            for (let mask1 = 0; mask1 < 1024; ++mask1) {
                const sum1 = dp[mask1];
                if (sum1 === -Infinity) continue;
                for (let mask2 = 0; mask2 < 1024; ++mask2) {
                    const sum2 = childDP[mask2];
                    if (sum2 === -Infinity) continue;
                    if ((mask1 & mask2) !== 0) continue;
                    const combinedMask = mask1 | mask2;
                    const candidate = sum1 + sum2;
                    if (candidate > newDP[combinedMask]) {
                        newDP[combinedMask] = candidate;
                    }
                }
            }
            dp = newDP;
        }

        let best = 0;
        for (let mask = 0; mask < 1024; ++mask) {
            if (dp[mask] > best) best = dp[mask];
        }
        maxScore[u] = best;
        return dp;
    }

    dfs(0);

    let total = 0;
    for (const v of maxScore) {
        total = (total + v) % MOD;
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $vals
     * @param Integer[] $par
     * @return Integer
     */
    function goodSubtreeSum($vals, $par) {
        $n = count($vals);
        $children = array_fill(0, $n, []);
        for ($i = 1; $i < $n; ++$i) {
            $p = $par[$i];
            $children[$p][] = $i;
        }

        $maxScore = array_fill(0, $n, 0);
        $MOD = 1000000007;

        // precompute mask and validity for each node
        $nodeMask = [];
        $nodeValid = [];
        foreach ($vals as $idx => $v) {
            [$mask, $valid] = $this->valueMask($v);
            $nodeMask[$idx] = $mask;
            $nodeValid[$idx] = $valid;
        }

        // DFS returns dp array mask=>max sum for subtree rooted at $u
        $dfs = function($u) use (&$dfs, &$children, &$vals, &$nodeMask, &$nodeValid, &$maxScore) {
            // start with empty set
            $dp = [0 => 0];

            foreach ($children[$u] as $v) {
                $childDp = $dfs($v);
                $newDp = [];
                foreach ($dp as $mask1 => $sum1) {
                    foreach ($childDp as $mask2 => $sum2) {
                        if (($mask1 & $mask2) === 0) {
                            $nm = $mask1 | $mask2;
                            $ns = $sum1 + $sum2;
                            if (!isset($newDp[$nm]) || $newDp[$nm] < $ns) {
                                $newDp[$nm] = $ns;
                            }
                        }
                    }
                }
                $dp = $newDp;
            }

            // consider taking node u itself
            if ($nodeValid[$u]) {
                $valMask = $nodeMask[$u];
                $val = $vals[$u];
                $newDp = $dp; // copy existing (not taking)
                foreach ($dp as $mask => $sum) {
                    if (($mask & $valMask) === 0) {
                        $nm = $mask | $valMask;
                        $ns = $sum + $val;
                        if (!isset($newDp[$nm]) || $newDp[$nm] < $ns) {
                            $newDp[$nm] = $ns;
                        }
                    }
                }
                $dp = $newDp;
            }

            // store max score for this node
            $max = 0;
            foreach ($dp as $s) {
                if ($s > $max) $max = $s;
            }
            $maxScore[$u] = $max;

            return $dp;
        };

        $dfs(0);

        $total = 0;
        foreach ($maxScore as $v) {
            $total = ($total + $v) % $MOD;
        }
        return $total;
    }

    // returns [mask, valid] where mask is bitmask of digits used in $val,
    // and valid indicates no repeated digit inside the number.
    private function valueMask($val) {
        $mask = 0;
        while ($val > 0) {
            $d = $val % 10;
            if (($mask >> $d) & 1) {
                return [0, false];
            }
            $mask |= (1 << $d);
            $val = intdiv($val, 10);
        }
        // handle value 0 case (though vals[i] >= 1 per constraints)
        if ($mask == 0) { // means original val was 0
            $mask = 1; // digit 0 used
        }
        return [$mask, true];
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    private let MOD = 1_000_000_007
    private var vals: [Int] = []
    private var nodeMask: [Int] = []
    private var nodeValid: [Bool] = []
    private var children: [[Int]] = []
    private var maxScore: [Int] = []

    func goodSubtreeSum(_ vals: [Int], _ par: [Int]) -> Int {
        let n = vals.count
        self.vals = vals
        nodeMask = Array(repeating: 0, count: n)
        nodeValid = Array(repeating: false, count: n)
        children = Array(repeating: [], count: n)
        maxScore = Array(repeating: 0, count: n)

        // build tree
        for i in 1..<n {
            let p = par[i]
            children[p].append(i)
        }

        // compute mask and validity for each node
        for i in 0..<n {
            let (mask, valid) = digitMask(vals[i])
            nodeMask[i] = mask
            nodeValid[i] = valid
        }

        _ = dfs(0)

        var total: Int64 = 0
        for v in maxScore {
            total += Int64(v)
        }
        return Int(total % Int64(MOD))
    }

    private func digitMask(_ x: Int) -> (Int, Bool) {
        var seen = 0
        var num = x
        if num == 0 {
            return (1 << 0, true)
        }
        while num > 0 {
            let d = num % 10
            let bit = 1 << d
            if (seen & bit) != 0 {
                return (0, false)
            }
            seen |= bit
            num /= 10
        }
        return (seen, true)
    }

    private func dfs(_ u: Int) -> [Int] {
        var dp = Array(repeating: -1, count: 1024)
        dp[0] = 0

        for v in children[u] {
            let childDP = dfs(v)
            var newDP = dp
            for mask1 in 0..<1024 where dp[mask1] >= 0 {
                let val1 = dp[mask1]
                for mask2 in 0..<1024 where childDP[mask2] >= 0 && (mask1 & mask2) == 0 {
                    let combined = mask1 | mask2
                    let sum = val1 + childDP[mask2]
                    if sum > newDP[combined] {
                        newDP[combined] = sum
                    }
                }
            }
            dp = newDP
        }

        // consider taking the node itself
        if nodeValid[u] {
            let m = nodeMask[u]
            var newDP = dp
            for mask in 0..<1024 where dp[mask] >= 0 && (mask & m) == 0 {
                let combined = mask | m
                let sum = dp[mask] + vals[u]
                if sum > newDP[combined] {
                    newDP[combined] = sum
                }
            }
            dp = newDP
        }

        var best = 0
        for val in dp where val > best {
            best = val
        }
        maxScore[u] = best
        return dp
    }
}
```

## Kotlin

```kotlin
import java.util.*

class Solution {
    private val MOD = 1_000_000_007L
    private lateinit var vals: IntArray
    private lateinit var masks: IntArray
    private lateinit var children: Array<MutableList<Int>>
    private lateinit var maxScore: LongArray

    fun goodSubtreeSum(vals: IntArray, par: IntArray): Int {
        val n = vals.size
        this.vals = vals
        masks = IntArray(n)
        for (i in 0 until n) {
            masks[i] = digitMask(vals[i])
        }
        children = Array(n) { mutableListOf<Int>() }
        for (i in 1 until n) {
            val p = par[i]
            children[p].add(i)
        }
        maxScore = LongArray(n)

        dfs(0)

        var ans = 0L
        for (v in maxScore) {
            ans = (ans + (v % MOD + MOD) % MOD) % MOD
        }
        return ans.toInt()
    }

    private fun digitMask(v: Int): Int {
        var x = v
        var mask = 0
        while (x > 0) {
            val d = x % 10
            val bit = 1 shl d
            if ((mask and bit) != 0) return -1
            mask = mask or bit
            x /= 10
        }
        return mask
    }

    private fun dfs(u: Int): LongArray {
        var dp = LongArray(1024) { Long.MIN_VALUE }
        dp[0] = 0L

        for (v in children[u]) {
            val childDp = dfs(v)
            val ndp = LongArray(1024) { Long.MIN_VALUE }
            for (m1 in 0 until 1024) {
                val sum1 = dp[m1]
                if (sum1 == Long.MIN_VALUE) continue
                for (m2 in 0 until 1024) {
                    val sum2 = childDp[m2]
                    if (sum2 == Long.MIN_VALUE) continue
                    if ((m1 and m2) == 0) {
                        val nm = m1 or m2
                        val ns = sum1 + sum2
                        if (ns > ndp[nm]) ndp[nm] = ns
                    }
                }
            }
            dp = ndp
        }

        val nodeMask = masks[u]
        if (nodeMask != -1) {
            val ndp = LongArray(1024) { Long.MIN_VALUE }
            for (m in 0 until 1024) {
                val sum = dp[m]
                if (sum == Long.MIN_VALUE) continue
                // not take u
                if (sum > ndp[m]) ndp[m] = sum
                // take u
                if ((m and nodeMask) == 0) {
                    val nm = m or nodeMask
                    val ns = sum + vals[u].toLong()
                    if (ns > ndp[nm]) ndp[nm] = ns
                }
            }
            dp = ndp
        }

        var best = 0L
        for (s in dp) {
            if (s > best) best = s
        }
        maxScore[u] = best
        return dp
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  static const int MOD = 1000000007;
  static const int INF_NEG = -1 << 60;

  List<List<int>> children = [];
  List<int> vals = [];
  List<int> maxScore = [];

  int goodSubtreeSum(List<int> valsInput, List<int> par) {
    int n = valsInput.length;
    vals = valsInput;
    children = List.generate(n, (_) => []);
    for (int i = 1; i < n; ++i) {
      children[par[i]].add(i);
    }
    maxScore = List.filled(n, 0);
    _dfs(0);
    int total = 0;
    for (int v in maxScore) {
      total += v;
      if (total >= MOD) total -= MOD;
    }
    return total % MOD;
  }

  List<int> _dfs(int u) {
    // dp[mask] = maximum sum achievable in subtree u with digit mask exactly 'mask'
    List<int> dp = List.filled(1 << 10, INF_NEG);
    dp[0] = 0;

    for (int v in children[u]) {
      List<int> childDp = _dfs(v);
      List<int> newDp = List.filled(1 << 10, INF_NEG);
      for (int m1 = 0; m1 < (1 << 10); ++m1) {
        if (dp[m1] == INF_NEG) continue;
        int sum1 = dp[m1];
        for (int m2 = 0; m2 < (1 << 10); ++m2) {
          if (childDp[m2] == INF_NEG) continue;
          if ((m1 & m2) != 0) continue;
          int newMask = m1 | m2;
          int newSum = sum1 + childDp[m2];
          if (newSum > newDp[newMask]) newDp[newMask] = newSum;
        }
      }
      dp = newDp;
    }

    int nodeMask = _valueMask(vals[u]);
    if (nodeMask != -1) {
      for (int m = 0; m < (1 << 10); ++m) {
        if (dp[m] == INF_NEG) continue;
        if ((m & nodeMask) != 0) continue;
        int newMask = m | nodeMask;
        int newSum = dp[m] + vals[u];
        if (newSum > dp[newMask]) dp[newMask] = newSum;
      }
    }

    int best = 0;
    for (int s in dp) {
      if (s > best) best = s;
    }
    maxScore[u] = best;
    return dp;
  }

  // Returns bitmask of digits used by val, or -1 if any digit repeats within the number.
  int _valueMask(int val) {
    int mask = 0;
    while (val > 0) {
      int d = val % 10;
      if ((mask >> d & 1) == 1) return -1; // duplicate digit inside this value
      mask |= (1 << d);
      val ~/= 10;
    }
    return mask;
  }
}
```

## Golang

```go
func goodSubtreeSum(vals []int, par []int) int {
	const MOD = 1000000007
	n := len(vals)
	children := make([][]int, n)
	for i := 1; i < n; i++ {
		p := par[i]
		children[p] = append(children[p], i)
	}
	var total int64

	digitMask := func(v int) (int, bool) {
		mask := 0
		if v == 0 { // not needed per constraints but handle safely
			return 1 << 0, true
		}
		for v > 0 {
			d := v % 10
			bit := 1 << d
			if mask&bit != 0 {
				return 0, false
			}
			mask |= bit
			v /= 10
		}
		return mask, true
	}

	var dfs func(int) []int
	dfs = func(u int) []int {
		dp := make([]int, 1024)
		for i := 0; i < 1024; i++ {
			dp[i] = -1
		}
		dp[0] = 0

		for _, v := range children[u] {
			childDP := dfs(v)
			newDP := make([]int, 1024)
			for i := 0; i < 1024; i++ {
				newDP[i] = -1
			}
			for m1 := 0; m1 < 1024; m1++ {
				if dp[m1] == -1 {
					continue
				}
				for m2 := 0; m2 < 1024; m2++ {
					if childDP[m2] == -1 {
						continue
					}
					if (m1 & m2) != 0 {
						continue
					}
					nm := m1 | m2
					sum := dp[m1] + childDP[m2]
					if sum > newDP[nm] {
						newDP[nm] = sum
					}
				}
			}
			dp = newDP
		}

		if mask, ok := digitMask(vals[u]); ok {
			for m := 0; m < 1024; m++ {
				if dp[m] == -1 || (m&mask) != 0 {
					continue
				}
				nm := m | mask
				sum := dp[m] + vals[u]
				if sum > dp[nm] {
					dp[nm] = sum
				}
			}
		}

		best := 0
		for _, v := range dp {
			if v > best {
				best = v
			}
		}
		total += int64(best)
		return dp
	}

	dfs(0)
	return int(total % MOD)
}
```

## Ruby

```ruby
def good_subtree_sum(vals, par)
  mod = 1_000_000_007
  n = vals.length

  # build children list
  children = Array.new(n) { [] }
  par.each_with_index do |p, i|
    next if p == -1
    children[p] << i
  end

  # compute digit mask for each value; nil if a digit repeats inside the number
  def digit_mask(val)
    mask = 0
    while val > 0
      d = val % 10
      bit = 1 << d
      return nil if (mask & bit) != 0
      mask |= bit
      val /= 10
    end
    mask
  end

  masks = vals.map { |v| digit_mask(v) }

  max_scores = Array.new(n, 0)

  dfs = nil
  dfs = ->(u) do
    dp = { 0 => 0 } # mask => best sum

    children[u].each do |v|
      child_dp = dfs.call(v)
      new_dp = dp.dup
      dp.each do |m1, s1|
        child_dp.each do |m2, s2|
          next if (m1 & m2) != 0
          ns = m1 | m2
          ns_sum = s1 + s2
          cur = new_dp[ns]
          new_dp[ns] = ns_sum if cur.nil? || cur < ns_sum
        end
      end
      dp = new_dp
    end

    dmask = masks[u]
    if dmask
      new_dp = dp.dup
      dp.each do |m, s|
        next if (m & dmask) != 0
        ns = m | dmask
        ns_sum = s + vals[u]
        cur = new_dp[ns]
        new_dp[ns] = ns_sum if cur.nil? || cur < ns_sum
      end
      dp = new_dp
    end

    max_scores[u] = dp.values.max
    dp
  end

  dfs.call(0)

  total = max_scores.sum % mod
  total
end
```

## Scala

```scala
object Solution {
  def goodSubtreeSum(vals: Array[Int], par: Array[Int]): Int = {
    val n = vals.length
    val children = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (i <- 1 until n) {
      children(par(i)).append(i)
    }

    val MOD = 1000000007L
    val maxScore = new Array[Long](n)

    def digitMask(v: Int): Option[Int] = {
      var x = v
      var mask = 0
      while (x > 0) {
        val d = x % 10
        val bit = 1 << d
        if ((mask & bit) != 0) return None
        mask |= bit
        x /= 10
      }
      Some(mask)
    }

    def dfs(u: Int): Array[Long] = {
      val cur = Array.fill[Long](1024)(-1L)
      cur(0) = 0L
      digitMask(vals(u)) match {
        case Some(m) => cur(m) = math.max(cur(m), vals(u).toLong)
        case None    =>
      }

      for (v <- children(u)) {
        val childDp = dfs(v)
        val next = Array.fill[Long](1024)(-1L)
        var maskA = 0
        while (maskA < 1024) {
          val sumA = cur(maskA)
          if (sumA >= 0) {
            var maskB = 0
            while (maskB < 1024) {
              val sumB = childDp(maskB)
              if (sumB >= 0 && (maskA & maskB) == 0) {
                val newMask = maskA | maskB
                val newSum = sumA + sumB
                if (newSum > next(newMask)) next(newMask) = newSum
              }
              maskB += 1
            }
          }
          maskA += 1
        }
        Array.copy(next, 0, cur, 0, 1024)
      }

      var best = 0L
      var m = 0
      while (m < 1024) {
        if (cur(m) > best) best = cur(m)
        m += 1
      }
      maxScore(u) = best
      cur
    }

    dfs(0)

    var ans = 0L
    var i = 0
    while (i < n) {
      ans = (ans + (maxScore(i) % MOD)) % MOD
      i += 1
    }
    ((ans % MOD) + MOD).toInt
  }
}
```

## Rust

```rust
use std::cmp::max;

const NEG_INF: i64 = -9_000_000_000_000_000_000;
const MOD_I64: i64 = 1_000_000_007;

fn digit_mask(mut x: i32) -> Option<u16> {
    let mut mask: u16 = 0;
    while x > 0 {
        let d = (x % 10) as u16;
        let bit = 1 << d;
        if mask & bit != 0 {
            return None;
        }
        mask |= bit;
        x /= 10;
    }
    Some(mask)
}

fn dfs(u: usize, children: &Vec<Vec<usize>>, vals: &Vec<i32>, total: &mut i64) -> Vec<i64> {
    let mut dp = vec![NEG_INF; 1024];
    dp[0] = 0;
    for &v in &children[u] {
        let child_dp = dfs(v, children, vals, total);
        let mut ndp = vec![NEG_INF; 1024];
        for ma in 0..1024 {
            if dp[ma] == NEG_INF { continue; }
            for mb in 0..1024 {
                if child_dp[mb] == NEG_INF { continue; }
                if (ma & mb) != 0 { continue; }
                let m = ma | mb;
                let val = dp[ma] + child_dp[mb];
                if val > ndp[m] {
                    ndp[m] = val;
                }
            }
        }
        dp = ndp;
    }

    // consider taking the current node
    let mut final_dp = dp.clone();
    if let Some(node_mask) = digit_mask(vals[u]) {
        for m in 0..1024 {
            if dp[m] == NEG_INF { continue; }
            if (m & node_mask as usize) != 0 { continue; }
            let nm = m | node_mask as usize;
            let val = dp[m] + vals[u] as i64;
            if val > final_dp[nm] {
                final_dp[nm] = val;
            }
        }
    }

    // best score for this subtree
    let mut best = NEG_INF;
    for &v in &final_dp {
        if v > best { best = v; }
    }
    *total = (*total + (best % MOD_I64 + MOD_I64) % MOD_I64) % MOD_I64;

    final_dp
}

impl Solution {
    pub fn good_subtree_sum(vals: Vec<i32>, par: Vec<i32>) -> i32 {
        let n = vals.len();
        let mut children = vec![Vec::new(); n];
        for i in 1..n {
            let p = par[i] as usize;
            children[p].push(i);
        }
        let mut total: i64 = 0;
        dfs(0, &children, &vals, &mut total);
        (total % MOD_I64) as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)
(define INF -1000000000000)

;; compute digit mask, return -1 if any digit repeats within the number
(define (digit-mask v)
  (let loop ((x v) (mask 0))
    (if (= x 0)
        mask
        (let* ((d (remainder x 10))
               (bit (arithmetic-shift 1 d)))
          (if (> (bitwise-and mask bit) 0)
              -1
              (loop (quotient x 10) (bitwise-ior mask bit)))))))

(define/contract (good-subtree-sum vals par)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((n (length vals))
         (val-vec (list->vector vals))
         ;; build children adjacency list
         (children (make-vector n '()))
         (masks (make-vector n 0)))
    ;; fill masks
    (for ([i (in-range n)])
      (vector-set! masks i (digit-mask (vector-ref val-vec i))))
    ;; build tree edges
    (for ([i (in-range 1 n)])
      (let ((p (list-ref par i)))
        (vector-set! children p (cons i (vector-ref children p)))))
    (define scores (make-vector n 0))
    ;; depth‑first DP
    (define (dfs u)
      (let ((dp (make-vector 1024 INF)))
        (vector-set! dp 0 0)
        (let ((node-mask (vector-ref masks u)))
          (when (>= node-mask 0)
            (let ((cur (vector-ref dp node-mask))
                  (val (vector-ref val-vec u)))
              (when (> val cur) (vector-set! dp node-mask val)))))
        ;; merge children
        (for ([v (in-list (vector-ref children u))])
          (let ((child-dp (dfs v))
                (newdp (make-vector 1024 INF)))
            (for ([maskA (in-range 1024)])
              (define valA (vector-ref dp maskA))
              (when (>= valA 0)
                (for ([maskB (in-range 1024)])
                  (define valB (vector-ref child-dp maskB))
                  (when (>= valB 0)
                    (when (= 0 (bitwise-and maskA maskB))
                      (let* ((newMask (bitwise-ior maskA maskB))
                             (cand (+ valA valB))
                             (cur (vector-ref newdp newMask)))
                        (when (> cand cur) (vector-set! newdp newMask cand))))))))
            (set! dp newdp)))
        ;; compute maxScore for u
        (let ((best 0))
          (for ([mask (in-range 1024)])
            (define v (vector-ref dp mask))
            (when (> v best) (set! best v)))
          (vector-set! scores u best))
        dp))
    (dfs 0)
    ;; sum all maxScores modulo MOD
    (let ((total 0))
      (for ([i (in-range n)])
        (set! total (+ total (vector-ref scores i))))
      (modulo total MOD))))
```

## Erlang

```erlang
-module(solution).
-export([good_subtree_sum/2]).

-define(MOD, 1000000007).

good_subtree_sum(Vals, Par) ->
    ChildrenMap = build_children_map(Par),
    ValsTuple = list_to_tuple(Vals),
    {_, _, Total} = dfs(0, ValsTuple, ChildrenMap),
    Total rem ?MOD.

%% Build map Parent -> [Children]
build_children_map(Par) ->
    N = length(Par),
    Indices = lists:seq(0, N-1),
    Pairs = lists:zip(Indices, Par),
    lists:foldl(fun({Idx, P}, Acc) ->
        if
            P == -1 -> Acc;
            true ->
                Prev = maps:get(P, Acc, []),
                maps:put(P, [Idx|Prev], Acc)
        end
    end, #{}, Pairs).

%% Depth‑first search returning {DPMap, MaxScoreNode, SumSubtree}
dfs(Node, ValsTuple, ChildrenMap) ->
    Val = element(Node+1, ValsTuple),
    BaseDP0 = #{0 => 0},
    {BaseDP, _} =
        case digit_mask(Val) of
            {ok, Mask} -> {maps:put(Mask, Val, BaseDP0), true};
            error -> {BaseDP0, false}
        end,
    Children = maps:get(Node, ChildrenMap, []),
    {FinalDP, SumChildren} =
        lists:foldl(fun(Child, {CurDP, AccSum}) ->
            {ChildDP, _ChildMax, ChildSum} = dfs(Child, ValsTuple, ChildrenMap),
            NewDP = merge_dp(CurDP, ChildDP),
            {NewDP, AccSum + ChildSum}
        end, {BaseDP, 0}, Children),
    MaxScoreNode = lists:max(maps:values(FinalDP)),
    TotalSum = MaxScoreNode + SumChildren,
    {FinalDP, MaxScoreNode, TotalSum}.

%% Merge two DP maps respecting digit masks
merge_dp(DP1, DP2) ->
    Base = DP1,
    List1 = maps:to_list(DP1),
    List2 = maps:to_list(DP2),
    lists:foldl(fun({Mask1, Sum1}, Acc) ->
        lists:foldl(fun({Mask2, Sum2}, AccInner) ->
            case (Mask1 band Mask2) of
                0 ->
                    NewMask = Mask1 bor Mask2,
                    NewSum = Sum1 + Sum2,
                    Prev = maps:get(NewMask, AccInner, -1),
                    if NewSum > Prev -> maps:put(NewMask, NewSum, AccInner);
                       true -> AccInner
                    end;
                _ -> AccInner
            end
        end, Acc, List2)
    end, Base, List1).

%% Compute digit mask; fail if a digit repeats within the number
digit_mask(Val) when Val > 0 ->
    digit_mask(Val, 0);
digit_mask(_Val) -> {ok, 0}.   % not used (Vals[i] >= 1)

digit_mask(0, Mask) -> {ok, Mask};
digit_mask(N, Mask) ->
    D = N rem 10,
    Bit = 1 bsl D,
    case (Mask band Bit) of
        0 ->
            NewMask = Mask bor Bit,
            digit_mask(N div 10, NewMask);
        _ -> error
    end.
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @mod 1_000_000_007

  @spec good_subtree_sum(vals :: [integer], par :: [integer]) :: integer
  def good_subtree_sum(vals, par) do
    n = length(vals)

    children =
      List.duplicate([], n)
      |> Enum.reduce(1..(n - 1), fn i, acc ->
        p = Enum.at(par, i)
        List.update_at(acc, p, fn lst -> [i | lst] end)
      end)

    masks = Enum.map(vals, &node_mask/1)

    {_dp, total} = dfs(0, vals, masks, children)
    rem(total, @mod)
  end

  defp node_mask(val) do
    case compute_mask(val, 0) do
      {:ok, mask} -> mask
      :error -> nil
    end
  end

  defp compute_mask(0, mask), do: {:ok, mask}
  defp compute_mask(v, mask) do
    d = rem(v, 10)
    bit = 1 <<< d
    if (mask &&& bit) != 0 do
      :error
    else
      compute_mask(div(v, 10), mask ||| bit)
    end
  end

  defp dfs(u, vals, masks, children) do
    dp = %{0 => 0}
    total = 0

    {dp, total} =
      Enum.reduce(Enum.at(children, u), {dp, total}, fn v, {cur_dp, cur_total} ->
        {child_dp, child_total} = dfs(v, vals, masks, children)
        new_dp = merge_maps(cur_dp, child_dp)
        {new_dp, cur_total + child_total}
      end)

    self_dp =
      case Enum.at(masks, u) do
        nil -> %{0 => 0}
        own_mask -> %{0 => 0, own_mask => Enum.at(vals, u)}
      end

    dp = merge_maps(dp, self_dp)
    max_score_u = dp |> Map.values() |> Enum.max()
    total = total + max_score_u
    {dp, total}
  end

  defp merge_maps(map1, map2) do
    Enum.reduce(map1, %{}, fn {mask1, sum1}, acc ->
      Enum.reduce(map2, acc, fn {mask2, sum2}, acc2 ->
        if (mask1 &&& mask2) == 0 do
          m = mask1 ||| mask2
          s = sum1 + sum2
          prev = Map.get(acc2, m, -1)
          if s > prev, do: Map.put(acc2, m, s), else: acc2
        else
          acc2
        end
      end)
    end)
  end
end
```
