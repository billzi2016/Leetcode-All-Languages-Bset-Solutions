# 3534. Path Existence Queries in a Graph II

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> pathExistenceQueries(int n, vector<int>& nums, int maxDiff, vector<vector<int>>& queries) {
        // sort indices by value
        vector<int> order(n);
        iota(order.begin(), order.end(), 0);
        sort(order.begin(), order.end(), [&](int a, int b){ return nums[a] < nums[b]; });
        
        vector<int> sortedVal(n), posInSorted(n);
        for (int i = 0; i < n; ++i) {
            sortedVal[i] = nums[order[i]];
            posInSorted[order[i]] = i;
        }
        
        // component ids
        vector<int> comp(n);
        int cid = 0;
        comp[0] = cid;
        for (int i = 1; i < n; ++i) {
            if (sortedVal[i] - sortedVal[i-1] > maxDiff) ++cid;
            comp[i] = cid;
        }
        
        // farthest reachable to the right in one step
        vector<int> nxtR(n);
        int j = 0;
        for (int i = 0; i < n; ++i) {
            while (j < n && sortedVal[j] - sortedVal[i] <= maxDiff) ++j;
            nxtR[i] = j - 1; // at least i
        }
        
        const int LOG = 18; // since 2^17 > 1e5
        vector<array<int, LOG>> up(n);
        for (int i = 0; i < n; ++i) up[i][0] = nxtR[i];
        for (int k = 1; k < LOG; ++k) {
            for (int i = 0; i < n; ++i) {
                up[i][k] = up[ up[i][k-1] ][k-1];
            }
        }
        
        vector<int> ans;
        ans.reserve(queries.size());
        for (auto &qr : queries) {
            int u = qr[0], v = qr[1];
            if (u == v) { ans.push_back(0); continue; }
            int pu = posInSorted[u];
            int pv = posInSorted[v];
            if (pu > pv) swap(pu, pv);
            if (comp[pu] != comp[pv]) {
                ans.push_back(-1);
                continue;
            }
            int cur = pu;
            int steps = 0;
            for (int k = LOG - 1; k >= 0; --k) {
                int nxt = up[cur][k];
                if (nxt < pv) {
                    cur = nxt;
                    steps += 1 << k;
                }
            }
            if (cur == pv) ans.push_back(steps);
            else ans.push_back(steps + 1);
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[] pathExistenceQueries(int n, int[] nums, int maxDiff, int[][] queries) {
        Integer[] order = new Integer[n];
        for (int i = 0; i < n; i++) order[i] = i;
        Arrays.sort(order, Comparator.comparingInt(i -> nums[i]));

        int[] sortedVals = new int[n];
        int[] origToSorted = new int[n];
        for (int idx = 0; idx < n; idx++) {
            int node = order[idx];
            sortedVals[idx] = nums[node];
            origToSorted[node] = idx;
        }

        // rightReach
        int[] rightReach = new int[n];
        int r = 0;
        for (int i = 0; i < n; i++) {
            while (r < n && sortedVals[r] - sortedVals[i] <= maxDiff) r++;
            rightReach[i] = r - 1;
        }

        // leftReach
        int[] leftReach = new int[n];
        int l = 0;
        for (int i = 0; i < n; i++) {
            while (sortedVals[i] - sortedVals[l] > maxDiff) l++;
            leftReach[i] = l;
        }

        // segment tree for max rightReach
        int size = 1;
        while (size < n) size <<= 1;
        int[] segMax = new int[2 * size];
        Arrays.fill(segMax, -1);
        for (int i = 0; i < n; i++) segMax[size + i] = rightReach[i];
        for (int i = size - 1; i > 0; i--) segMax[i] = Math.max(segMax[2 * i], segMax[2 * i + 1]);

        // segment tree for min leftReach
        int[] segMin = new int[2 * size];
        Arrays.fill(segMin, Integer.MAX_VALUE);
        for (int i = 0; i < n; i++) segMin[size + i] = leftReach[i];
        for (int i = size - 1; i > 0; i--) segMin[i] = Math.min(segMin[2 * i], segMin[2 * i + 1]);

        // helper lambdas
        java.util.function.BiFunction<Integer, Integer, Integer> rangeMax = (L, R) -> {
            int res = -1;
            int lq = L + size, rq = R + size;
            while (lq <= rq) {
                if ((lq & 1) == 1) { res = Math.max(res, segMax[lq]); lq++; }
                if ((rq & 1) == 0) { res = Math.max(res, segMax[rq]); rq--; }
                lq >>= 1; rq >>= 1;
            }
            return res;
        };
        java.util.function.BiFunction<Integer, Integer, Integer> rangeMin = (L, R) -> {
            int res = Integer.MAX_VALUE;
            int lq = L + size, rq = R + size;
            while (lq <= rq) {
                if ((lq & 1) == 1) { res = Math.min(res, segMin[lq]); lq++; }
                if ((rq & 1) == 0) { res = Math.min(res, segMin[rq]); rq--; }
                lq >>= 1; rq >>= 1;
            }
            return res;
        };

        int[] farRight = new int[n];
        int[] farLeft = new int[n];
        for (int i = 0; i < n; i++) {
            farRight[i] = rangeMax.apply(i, rightReach[i]);
            farLeft[i] = rangeMin.apply(leftReach[i], i);
        }

        // binary lifting tables
        int LOG = 1;
        while ((1 << LOG) <= n) LOG++;
        int[][] upR = new int[LOG][n];
        int[][] upL = new int[LOG][n];
        for (int i = 0; i < n; i++) {
            upR[0][i] = farRight[i];
            upL[0][i] = farLeft[i];
        }
        for (int k = 1; k < LOG; k++) {
            for (int i = 0; i < n; i++) {
                upR[k][i] = upR[k - 1][upR[k - 1][i]];
                upL[k][i] = upL[k - 1][upL[k - 1][i]];
            }
        }

        int m = queries.length;
        int[] ans = new int[m];
        for (int qi = 0; qi < m; qi++) {
            int u = queries[qi][0];
            int v = queries[qi][1];
            int su = origToSorted[u];
            int sv = origToSorted[v];
            if (su == sv) {
                ans[qi] = 0;
                continue;
            }
            if (su < sv) { // move right
                int cur = su;
                int steps = 0;
                for (int k = LOG - 1; k >= 0; k--) {
                    int nxt = upR[k][cur];
                    if (nxt < sv) {
                        cur = nxt;
                        steps += 1 << k;
                    }
                }
                if (upR[0][cur] < sv) ans[qi] = -1;
                else ans[qi] = steps + 1;
            } else { // move left
                int cur = su;
                int steps = 0;
                for (int k = LOG - 1; k >= 0; k--) {
                    int nxt = upL[k][cur];
                    if (nxt > sv) {
                        cur = nxt;
                        steps += 1 << k;
                    }
                }
                if (upL[0][cur] > sv) ans[qi] = -1;
                else ans[qi] = steps + 1;
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # sort nodes by value
        sorted_nodes = sorted([(val, idx) for idx, val in enumerate(nums)])
        values = [v for v, _ in sorted_nodes]
        pos_of_original = [0] * n
        for i, (_, orig) in enumerate(sorted_nodes):
            pos_of_original[orig] = i

        # compute immediate reachable interval [L[i], R[i]]
        L = [0] * n
        R = [0] * n
        l = 0
        for i in range(n):
            while values[i] - values[l] > maxDiff:
                l += 1
            L[i] = l

        r = 0
        for i in range(n):
            if r < i:
                r = i
            while r + 1 < n and values[r + 1] - values[i] <= maxDiff:
                r += 1
            R[i] = r

        # component ids (contiguous blocks where consecutive diff <= maxDiff)
        comp = [0] * n
        cid = 0
        for i in range(1, n):
            if values[i] - values[i - 1] > maxDiff:
                cid += 1
            comp[i] = cid

        LOG = (n).bit_length()
        left = [L]
        right = [R]

        for p in range(1, LOG):
            prev_left = left[p - 1]
            prev_right = right[p - 1]
            cur_left = [0] * n
            cur_right = [0] * n
            for i in range(n):
                cur_left[i] = prev_left[prev_left[i]]
                cur_right[i] = prev_right[prev_right[i]]
            left.append(cur_left)
            right.append(cur_right)

        ans = []
        for u, v in queries:
            iu = pos_of_original[u]
            iv = pos_of_original[v]
            if comp[iu] != comp[iv]:
                ans.append(-1)
                continue
            if iu == iv:
                ans.append(0)
                continue

            curL = iu
            curR = iu
            steps = 0
            for p in range(LOG - 1, -1, -1):
                nL = left[p][curL]
                nR = right[p][curR]
                if not (nL <= iv <= nR):
                    curL = nL
                    curR = nR
                    steps += 1 << p
            ans.append(steps + 1)
        return ans
```

## Python3

```python
class Solution:
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        from math import ceil, log2

        # sort nodes by value
        order = sorted(range(n), key=lambda i: nums[i])
        pos_in_sorted = [0] * n
        for idx, node in enumerate(order):
            pos_in_sorted[node] = idx
        vals = [nums[i] for i in order]

        # compute farthest reachable index in one step (forward)
        r = [0] * n
        j = 0
        for i in range(n):
            while j + 1 < n and vals[j + 1] - vals[i] <= maxDiff:
                j += 1
            r[i] = j

        # component ids (contiguous blocks where adjacent diff <= maxDiff)
        comp = [0] * n
        cid = 0
        for i in range(1, n):
            if vals[i] - vals[i - 1] > maxDiff:
                cid += 1
            comp[i] = cid

        LOG = ceil(log2(n)) + 1
        up = [[0] * n for _ in range(LOG)]
        up[0] = r[:]
        for k in range(1, LOG):
            prev = up[k - 1]
            cur = up[k]
            for i in range(n):
                cur[i] = prev[prev[i]]

        def min_steps(su, sv):
            if su == sv:
                return 0
            # greedy binary lifting
            cur = su
            steps = 0
            for k in range(LOG - 1, -1, -1):
                nxt = up[k][cur]
                if nxt < sv:
                    cur = nxt
                    steps += 1 << k
            return steps + 1

        ans = []
        for u, v in queries:
            su, sv = pos_in_sorted[u], pos_in_sorted[v]
            if comp[su] != comp[sv]:
                ans.append(-1)
                continue
            if su > sv:
                su, sv = sv, su
            ans.append(min_steps(su, sv))
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    int val;
    int idx;
} Node;

static int cmpNode(const void *a, const void *b) {
    int va = ((Node *)a)->val;
    int vb = ((Node *)b)->val;
    if (va != vb) return va - vb;
    return ((Node *)a)->idx - ((Node *)b)->idx;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* pathExistenceQueries(int n, int* nums, int numsSize, int maxDiff,
                          int** queries, int queriesSize, int* queriesColSize,
                          int* returnSize) {
    // Sort nodes by value
    Node *nodes = (Node *)malloc(n * sizeof(Node));
    for (int i = 0; i < n; ++i) {
        nodes[i].val = nums[i];
        nodes[i].idx = i;
    }
    qsort(nodes, n, sizeof(Node), cmpNode);
    
    // position mapping: original index -> sorted position
    int *pos = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) {
        pos[nodes[i].idx] = i;
    }
    
    // compute farthest reachable to the right within one step
    int *r = (int *)malloc(n * sizeof(int));
    int j = 0;
    for (int i = 0; i < n; ++i) {
        if (j < i) j = i;
        while (j + 1 < n && nodes[j + 1].val - nodes[i].val <= maxDiff) {
            ++j;
        }
        r[i] = j;
    }
    
    // binary lifting table
    const int MAXK = 18; // since 2^17 > 1e5
    int **up = (int **)malloc(MAXK * sizeof(int *));
    for (int k = 0; k < MAXK; ++k) {
        up[k] = (int *)malloc(n * sizeof(int));
    }
    memcpy(up[0], r, n * sizeof(int));
    for (int k = 1; k < MAXK; ++k) {
        for (int i = 0; i < n; ++i) {
            int mid = up[k - 1][i];
            up[k][i] = up[k - 1][mid];
        }
    }
    
    // answer queries
    int *ans = (int *)malloc(queriesSize * sizeof(int));
    for (int qi = 0; qi < queriesSize; ++qi) {
        int u = queries[qi][0];
        int v = queries[qi][1];
        if (u == v) {
            ans[qi] = 0;
            continue;
        }
        int su = pos[u];
        int sv = pos[v];
        if (su > sv) {
            int tmp = su; su = sv; sv = tmp;
        }
        // greedy binary lifting
        int cur = su;
        int steps = 0;
        for (int k = MAXK - 1; k >= 0; --k) {
            int nxt = up[k][cur];
            if (nxt < sv) {
                cur = nxt;
                steps += 1 << k;
            }
        }
        if (up[0][cur] >= sv) {
            ans[qi] = steps + 1;
        } else {
            ans[qi] = -1;
        }
    }
    
    // clean up
    for (int k = 0; k < MAXK; ++k) free(up[k]);
    free(up);
    free(r);
    free(pos);
    free(nodes);
    
    *returnSize = queriesSize;
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[] PathExistenceQueries(int n, int[] nums, int maxDiff, int[][] queries) {
        // Pair values with original indices
        var pairs = new (int val, int idx)[n];
        for (int i = 0; i < n; i++) pairs[i] = (nums[i], i);
        Array.Sort(pairs, (a, b) => a.val.CompareTo(b.val));

        // Sorted values and position mapping
        var sortedVals = new int[n];
        var posOfOrig = new int[n];
        for (int i = 0; i < n; i++) {
            sortedVals[i] = pairs[i].val;
            posOfOrig[pairs[i].idx] = i;
        }

        // Compute farthest reachable index to the right within maxDiff
        var far = new int[n];
        int j = 0;
        for (int i = 0; i < n; i++) {
            if (j < i) j = i;
            while (j + 1 < n && sortedVals[j + 1] - sortedVals[i] <= maxDiff) j++;
            far[i] = j;
        }

        // Component ids (contiguous segments where consecutive diff <= maxDiff)
        var comp = new int[n];
        int curComp = 0;
        comp[0] = 0;
        for (int i = 1; i < n; i++) {
            if (sortedVals[i] - sortedVals[i - 1] > maxDiff) curComp++;
            comp[i] = curComp;
        }

        // Binary lifting table
        int LOG = 0;
        while ((1 << LOG) <= n) LOG++;
        var jump = new int[LOG][];
        for (int k = 0; k < LOG; k++) jump[k] = new int[n];

        for (int i = 0; i < n; i++) jump[0][i] = far[i];
        for (int k = 1; k < LOG; k++) {
            var prev = jump[k - 1];
            var cur = jump[k];
            for (int i = 0; i < n; i++) {
                cur[i] = prev[prev[i]];
            }
        }

        int qlen = queries.Length;
        var answer = new int[qlen];

        for (int qi = 0; qi < qlen; qi++) {
            int uOrig = queries[qi][0];
            int vOrig = queries[qi][1];
            int pu = posOfOrig[uOrig];
            int pv = posOfOrig[vOrig];

            if (pu == pv) {
                answer[qi] = 0;
                continue;
            }

            int left = pu, right = pv;
            if (left > right) { int tmp = left; left = right; right = tmp; }

            if (comp[left] != comp[right]) {
                answer[qi] = -1;
                continue;
            }

            int curPos = left;
            int steps = 0;
            for (int k = LOG - 1; k >= 0; k--) {
                int nxt = jump[k][curPos];
                if (nxt < right) {
                    curPos = nxt;
                    steps += 1 << k;
                }
            }
            // One final hop reaches or passes 'right'
            answer[qi] = steps + 1;
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[]} nums
 * @param {number} maxDiff
 * @param {number[][]} queries
 * @return {number[]}
 */
var pathExistenceQueries = function(n, nums, maxDiff, queries) {
    // sort nodes by value
    const idx = Array.from({length: n}, (_, i) => i);
    idx.sort((a, b) => nums[a] - nums[b]);
    const pos = new Array(n);
    for (let i = 0; i < n; ++i) pos[idx[i]] = i;

    // compute farthest reachable to the right within maxDiff
    const nextRight = new Uint32Array(n);
    let r = 0;
    for (let l = 0; l < n; ++l) {
        while (r + 1 < n && nums[idx[r + 1]] - nums[idx[l]] <= maxDiff) r++;
        nextRight[l] = r;
        if (r === l) r = l; // keep window valid
    }

    // binary lifting table
    let LOG = 0;
    while ((1 << LOG) <= n) LOG++;
    const up = new Array(LOG);
    up[0] = nextRight.slice();
    for (let k = 1; k < LOG; ++k) {
        const prev = up[k - 1];
        const cur = new Uint32Array(n);
        for (let i = 0; i < n; ++i) {
            cur[i] = prev[prev[i]];
        }
        up[k] = cur;
    }

    const ans = new Array(queries.length);
    for (let qi = 0; qi < queries.length; ++qi) {
        let [u, v] = queries[qi];
        let pu = pos[u], pv = pos[v];
        if (pu > pv) { const t = pu; pu = pv; pv = t; }
        if (pu === pv) {
            ans[qi] = 0;
            continue;
        }
        if (nextRight[pu] === pu) {
            ans[qi] = -1;
            continue;
        }
        let cur = pu;
        let jumps = 0;
        for (let k = LOG - 1; k >= 0; --k) {
            const nxt = up[k][cur];
            if (nxt < pv) {
                cur = nxt;
                jumps += 1 << k;
            }
        }
        ans[qi] = (up[0][cur] >= pv) ? jumps + 1 : -1;
    }
    return ans;
};
```

## Typescript

```typescript
function pathExistenceQueries(n: number, nums: number[], maxDiff: number, queries: number[][]): number[] {
    // Sort indices by nums value
    const idx = Array.from({ length: n }, (_, i) => i);
    idx.sort((a, b) => nums[a] - nums[b]);

    const posInSorted = new Uint32Array(n);
    const sortedVals = new Uint32Array(n);
    for (let i = 0; i < n; i++) {
        const original = idx[i];
        posInSorted[original] = i;
        sortedVals[i] = nums[original];
    }

    // Compute L and R intervals
    const L = new Uint32Array(n);
    const R = new Uint32Array(n);
    let l = 0, r = 0;
    for (let i = 0; i < n; i++) {
        while (sortedVals[i] - sortedVals[l] > maxDiff) l++;
        L[i] = l;
        while (r + 1 < n && sortedVals[r + 1] - sortedVals[i] <= maxDiff) r++;
        R[i] = r;
    }

    // Component ids
    const comp = new Uint32Array(n);
    let curComp = 0;
    comp[0] = curComp;
    for (let i = 1; i < n; i++) {
        if (sortedVals[i] - sortedVals[i - 1] > maxDiff) curComp++;
        comp[i] = curComp;
    }

    // Binary lifting table
    const LOG = Math.ceil(Math.log2(n)) + 1;
    const up: Uint32Array[] = new Array(LOG);
    up[0] = R.slice(); // copy
    for (let k = 1; k < LOG; k++) {
        const prev = up[k - 1];
        const curArr = new Uint32Array(n);
        for (let i = 0; i < n; i++) {
            curArr[i] = prev[prev[i]];
        }
        up[k] = curArr;
    }

    const answers: number[] = new Array(queries.length);
    for (let qi = 0; qi < queries.length; qi++) {
        let [u, v] = queries[qi];
        let pu = posInSorted[u];
        let pv = posInSorted[v];
        if (pu === pv) {
            answers[qi] = 0;
            continue;
        }
        // Ensure pu <= pv
        if (pu > pv) {
            const tmp = pu; pu = pv; pv = tmp;
        }
        if (comp[pu] !== comp[pv]) {
            answers[qi] = -1;
            continue;
        }
        let cur = pu;
        let steps = 0;
        for (let k = LOG - 1; k >= 0; k--) {
            const nxt = up[k][cur];
            if (nxt < pv) {
                cur = nxt;
                steps += 1 << k;
            }
        }
        answers[qi] = steps + 1;
    }

    return answers;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[] $nums
     * @param Integer $maxDiff
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function pathExistenceQueries($n, $nums, $maxDiff, $queries) {
        // sort indices by nums value
        $order = range(0, $n - 1);
        usort($order, function($a, $b) use ($nums) {
            if ($nums[$a] == $nums[$b]) return 0;
            return ($nums[$a] < $nums[$b]) ? -1 : 1;
        });

        $sortedVals = [];
        $pos = array_fill(0, $n, 0); // original index -> position in sorted order
        for ($i = 0; $i < $n; ++$i) {
            $idx = $order[$i];
            $sortedVals[$i] = $nums[$idx];
            $pos[$idx] = $i;
        }

        // component ids based on gaps > maxDiff
        $comp = array_fill(0, $n, 0);
        $cid = 0;
        for ($i = 1; $i < $n; ++$i) {
            if ($sortedVals[$i] - $sortedVals[$i - 1] > $maxDiff) {
                ++$cid;
            }
            $comp[$i] = $cid;
        }

        // furthest reachable index to the right in one hop
        $farthest = array_fill(0, $n, 0);
        $r = 0;
        for ($i = 0; $i < $n; ++$i) {
            if ($r < $i) $r = $i;
            while ($r + 1 < $n && $sortedVals[$r + 1] - $sortedVals[$i] <= $maxDiff) {
                ++$r;
            }
            $farthest[$i] = $r;
        }

        // binary lifting table
        $LOG = 0;
        while ((1 << $LOG) <= $n) ++$LOG;
        $up = array_fill(0, $LOG, []);
        for ($k = 0; $k < $LOG; ++$k) {
            $up[$k] = array_fill(0, $n, 0);
        }
        for ($i = 0; $i < $n; ++$i) {
            $up[0][$i] = $farthest[$i];
        }
        for ($k = 1; $k < $LOG; ++$k) {
            for ($i = 0; $i < $n; ++$i) {
                $mid = $up[$k - 1][$i];
                $up[$k][$i] = $up[$k - 1][$mid];
            }
        }

        $answers = [];
        foreach ($queries as $qr) {
            [$u, $v] = $qr;
            $pu = $pos[$u];
            $pv = $pos[$v];

            if ($comp[$pu] !== $comp[$pv]) {
                $answers[] = -1;
                continue;
            }
            if ($pu == $pv) {
                $answers[] = 0;
                continue;
            }

            // ensure pu < pv
            if ($pu > $pv) {
                $tmp = $pu; $pu = $pv; $pv = $tmp;
            }

            $cur = $pu;
            $steps = 0;
            for ($k = $LOG - 1; $k >= 0; --$k) {
                $next = $up[$k][$cur];
                if ($next < $pv) {
                    $cur = $next;
                    $steps += (1 << $k);
                }
            }
            // one final jump reaches or passes pv
            $answers[] = $steps + 1;
        }

        return $answers;
    }
}
```

## Swift

```swift
class Solution {
    func pathExistenceQueries(_ n: Int, _ nums: [Int], _ maxDiff: Int, _ queries: [[Int]]) -> [Int] {
        // Pair values with original indices and sort by value
        var pairs = [(value: Int, idx: Int)]()
        pairs.reserveCapacity(n)
        for i in 0..<n {
            pairs.append((nums[i], i))
        }
        pairs.sort { $0.value < $1.value }
        
        // Sorted values and position mapping
        var sortedVals = [Int](repeating: 0, count: n)
        var pos = [Int](repeating: 0, count: n)
        for (i, p) in pairs.enumerated() {
            sortedVals[i] = p.value
            pos[p.idx] = i
        }
        
        // Component ids based on gaps larger than maxDiff
        var comp = [Int](repeating: 0, count: n)
        var curComp = 0
        comp[0] = curComp
        if n > 1 {
            for i in 1..<n {
                if sortedVals[i] - sortedVals[i - 1] > maxDiff {
                    curComp += 1
                }
                comp[i] = curComp
            }
        }
        
        // Rightmost reachable index from each position using maxDiff
        var right = [Int](repeating: 0, count: n)
        var j = 0
        for i in 0..<n {
            while j + 1 < n && sortedVals[j + 1] - sortedVals[i] <= maxDiff {
                j += 1
            }
            right[i] = j
        }
        
        // Binary lifting table
        var maxLog = 0
        while (1 << maxLog) <= n { maxLog += 1 }
        maxLog -= 1   // highest power of two not exceeding n
        
        var jump = Array(repeating: [Int](repeating: 0, count: n), count: maxLog + 1)
        jump[0] = right
        if maxLog >= 1 {
            for k in 1...maxLog {
                let prev = jump[k - 1]
                var curArr = [Int](repeating: 0, count: n)
                for i in 0..<n {
                    let mid = prev[i]
                    curArr[i] = prev[mid]
                }
                jump[k] = curArr
            }
        }
        
        // Answer queries
        var answer = [Int]()
        answer.reserveCapacity(queries.count)
        for q in queries {
            let u = q[0]
            let v = q[1]
            if u == v {
                answer.append(0)
                continue
            }
            var a = pos[u]
            var b = pos[v]
            if comp[a] != comp[b] {
                answer.append(-1)
                continue
            }
            if a > b { swap(&a, &b) }
            var cur = a
            var steps = 0
            for k in stride(from: maxLog, through: 0, by: -1) {
                let nxt = jump[k][cur]
                if nxt < b {
                    cur = nxt
                    steps += (1 << k)
                }
            }
            // One final jump reaches or passes b
            steps += 1
            answer.append(steps)
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun pathExistenceQueries(n: Int, nums: IntArray, maxDiff: Int, queries: Array<IntArray>): IntArray {
        // Pair values with original indices and sort
        val nodes = Array(n) { i -> Pair(nums[i], i) }
        nodes.sortBy { it.first }
        val sortedVals = IntArray(n)
        val pos = IntArray(n) // original index -> sorted position
        for (i in 0 until n) {
            sortedVals[i] = nodes[i].first
            pos[nodes[i].second] = i
        }

        // Compute farthest reachable index from each position within one edge
        val far = IntArray(n)
        var r = 0
        for (l in 0 until n) {
            while (r + 1 < n && sortedVals[r + 1] - sortedVals[l] <= maxDiff) {
                r++
            }
            far[l] = r
            if (r == l) {
                // ensure window moves forward for next l
                r = l
            }
        }

        // Component ids based on gaps larger than maxDiff
        val compId = IntArray(n)
        var curComp = 0
        compId[0] = 0
        for (i in 1 until n) {
            if (sortedVals[i] - sortedVals[i - 1] > maxDiff) curComp++
            compId[i] = curComp
        }

        // Binary lifting table
        val LOG = 17 // since 2^17 = 131072 > 1e5
        val up = Array(LOG + 1) { IntArray(n) }
        for (i in 0 until n) {
            up[0][i] = far[i]
        }
        for (k in 1..LOG) {
            val prev = up[k - 1]
            val cur = up[k]
            for (i in 0 until n) {
                cur[i] = prev[prev[i]]
            }
        }

        // Answer queries
        val ans = IntArray(queries.size)
        for (idx in queries.indices) {
            val uOrig = queries[idx][0]
            val vOrig = queries[idx][1]
            if (uOrig == vOrig) {
                ans[idx] = 0
                continue
            }
            var pu = pos[uOrig]
            var pv = pos[vOrig]
            // ensure pu < pv for forward processing
            if (pu > pv) {
                val tmp = pu; pu = pv; pv = tmp
            }
            if (compId[pu] != compId[pv]) {
                ans[idx] = -1
                continue
            }
            var curPos = pu
            var steps = 0
            for (k in LOG downTo 0) {
                val nxt = up[k][curPos]
                if (nxt < pv) {
                    curPos = nxt
                    steps += 1 shl k
                }
            }
            // one final jump reaches or passes pv
            ans[idx] = steps + 1
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> pathExistenceQueries(int n, List<int> nums, int maxDiff, List<List<int>> queries) {
    // Sort nodes by their values
    List<int> order = List.generate(n, (i) => i);
    order.sort((a, b) => nums[a].compareTo(nums[b]));
    List<int> sortedVals = List.filled(n, 0);
    List<int> posInSorted = List.filled(n, 0);
    for (int i = 0; i < n; ++i) {
      int idx = order[i];
      sortedVals[i] = nums[idx];
      posInSorted[idx] = i;
    }

    // Compute nxt[i]: farthest index reachable from i in one step
    List<int> nxt = List.filled(n, 0);
    int r = 0;
    for (int i = 0; i < n; ++i) {
      if (r < i) r = i;
      while (r + 1 < n && sortedVals[r + 1] - sortedVals[i] <= maxDiff) {
        r++;
      }
      nxt[i] = r;
    }

    // Compute component ids
    List<int> comp = List.filled(n, 0);
    for (int i = 1; i < n; ++i) {
      if (sortedVals[i] - sortedVals[i - 1] > maxDiff) {
        comp[i] = comp[i - 1] + 1;
      } else {
        comp[i] = comp[i - 1];
      }
    }

    // Binary lifting table
    int LOG = 0;
    while ((1 << LOG) <= n) LOG++;
    LOG--; // highest power such that 2^LOG <= n
    List<List<int>> up = List.generate(LOG + 1, (_) => List.filled(n, 0));
    up[0] = nxt;
    for (int k = 1; k <= LOG; ++k) {
      List<int> prev = up[k - 1];
      List<int> cur = up[k];
      for (int i = 0; i < n; ++i) {
        cur[i] = prev[prev[i]];
      }
    }

    // Answer queries
    List<int> ans = List.filled(queries.length, 0);
    for (int qi = 0; qi < queries.length; ++qi) {
      int u = queries[qi][0];
      int v = queries[qi][1];
      if (u == v) {
        ans[qi] = 0;
        continue;
      }
      int pu = posInSorted[u];
      int pv = posInSorted[v];
      if (pu > pv) {
        int tmp = pu;
        pu = pv;
        pv = tmp;
      }
      if (comp[pu] != comp[pv]) {
        ans[qi] = -1;
        continue;
      }
      int cur = pu;
      int steps = 0;
      for (int k = LOG; k >= 0; --k) {
        int nxtIdx = up[k][cur];
        if (nxtIdx < pv) {
          cur = nxtIdx;
          steps += 1 << k;
        }
      }
      // One final jump reaches or passes target
      ans[qi] = steps + 1;
    }

    return ans;
  }
}
```

## Golang

```go
func pathExistenceQueries(n int, nums []int, maxDiff int, queries [][]int) []int {
	type node struct {
		val int
		idx int
	}
	nodes := make([]node, n)
	for i, v := range nums {
		nodes[i] = node{val: v, idx: i}
	}
	// sort by value
	sort.Slice(nodes, func(i, j int) bool { return nodes[i].val < nodes[j].val })
	pos := make([]int, n)      // original index -> sorted position
	vals := make([]int, n)     // sorted values
	for i, nd := range nodes {
		pos[nd.idx] = i
		vals[i] = nd.val
	}
	// component ids based on gaps > maxDiff
	comp := make([]int, n)
	for i := 1; i < n; i++ {
		if vals[i]-vals[i-1] > maxDiff {
			comp[i] = comp[i-1] + 1
		} else {
			comp[i] = comp[i-1]
		}
	}
	// next[i]: farthest index reachable from i in one edge (forward)
	next := make([]int, n)
	r := 0
	for i := 0; i < n; i++ {
		if r < i {
			r = i
		}
		for r+1 < n && vals[r+1]-vals[i] <= maxDiff {
			r++
		}
		next[i] = r
	}
	// binary lifting table
	maxLog := 0
	for (1 << maxLog) <= n {
		maxLog++
	}
	up := make([][]int, maxLog)
	up[0] = make([]int, n)
	copy(up[0], next)
	for k := 1; k < maxLog; k++ {
		up[k] = make([]int, n)
		for i := 0; i < n; i++ {
			mid := up[k-1][i]
			up[k][i] = up[k-1][mid]
		}
	}
	ans := make([]int, len(queries))
	for qi, q := range queries {
		u, v := q[0], q[1]
		if u == v {
			ans[qi] = 0
			continue
		}
		pu, pv := pos[u], pos[v]
		if comp[pu] != comp[pv] {
			ans[qi] = -1
			continue
		}
		if pu > pv {
			pu, pv = pv, pu
		}
		cur := pu
		steps := 0
		for k := maxLog - 1; k >= 0; k-- {
			nxt := up[k][cur]
			if nxt < pv {
				cur = nxt
				steps += 1 << k
			}
		}
		ans[qi] = steps + 1
	}
	return ans
}

import "sort"
```

## Ruby

```ruby
def path_existence_queries(n, nums, max_diff, queries)
  # sort nodes by value
  pairs = (0...n).map { |i| [nums[i], i] }
  pairs.sort_by! { |a| a[0] }
  sorted_vals = pairs.map { |p| p[0] }
  pos_of_original = Array.new(n)
  pairs.each_with_index { |(_, orig), idx| pos_of_original[orig] = idx }

  # farthest reachable index from each position (inclusive)
  r = 0
  furthest = Array.new(n, 0)
  n.times do |l|
    while r + 1 < n && sorted_vals[r + 1] - sorted_vals[l] <= max_diff
      r += 1
    end
    furthest[l] = r
    # ensure window moves forward
    r = l if r < l
  end

  # component ids (contiguous blocks where adjacent diff <= max_diff)
  comp = Array.new(n, 0)
  cid = 0
  comp[0] = cid
  (1...n).each do |i|
    if sorted_vals[i] - sorted_vals[i - 1] > max_diff
      cid += 1
    end
    comp[i] = cid
  end

  # binary lifting tables
  log = 1
  log += 1 while (1 << log) <= n
  jump = Array.new(log) { Array.new(n, 0) }
  jump[0] = furthest.dup
  (1...log).each do |k|
    prev = jump[k - 1]
    cur = jump[k]
    n.times do |i|
      cur[i] = prev[prev[i]]
    end
  end

  answers = []
  queries.each do |u, v|
    pu = pos_of_original[u]
    pv = pos_of_original[v]

    if pu == pv
      answers << 0
      next
    end

    # ensure pu < pv
    if pu > pv
      pu, pv = pv, pu
    end

    if comp[pu] != comp[pv]
      answers << -1
      next
    end

    cur = pu
    steps = 0
    (log - 1).downto(0) do |k|
      nxt = jump[k][cur]
      if nxt < pv
        cur = nxt
        steps += 1 << k
      end
    end
    steps += 1
    answers << steps
  end

  answers
end
```

## Scala

```scala
object Solution {
    def pathExistenceQueries(n: Int, nums: Array[Int], maxDiff: Int, queries: Array[Array[Int]]): Array[Int] = {
        // Pair values with original indices and sort by value
        val pairs = (0 until n).map(i => (nums(i), i)).toArray.sortBy(_._1)
        val sortedVals = new Array[Int](n)
        val posOfOrig = new Array[Int](n) // map original index -> position in sorted order
        var i = 0
        while (i < n) {
            sortedVals(i) = pairs(i)._1
            posOfOrig(pairs(i)._2) = i
            i += 1
        }

        // Compute rightmost reachable index from each position within maxDiff
        val right = new Array[Int](n)
        var r = 0
        i = 0
        while (i < n) {
            if (r < i) r = i
            while (r + 1 < n && sortedVals(r + 1) - sortedVals(i) <= maxDiff) {
                r += 1
            }
            right(i) = r
            i += 1
        }

        // Compute leftmost reachable index from each position within maxDiff
        val left = new Array[Int](n)
        var l = 0
        i = 0
        while (i < n) {
            while (sortedVals(i) - sortedVals(l) > maxDiff) {
                l += 1
            }
            left(i) = l
            i += 1
        }

        // Determine needed log size
        var LOG = 0
        while ((1 << LOG) <= n) LOG += 1

        // Binary lifting tables for forward (right) and backward (left) jumps
        val jumpF = Array.ofDim[Int](LOG, n)
        val jumpB = Array.ofDim[Int](LOG, n)

        i = 0
        while (i < n) {
            jumpF(0)(i) = right(i)
            jumpB(0)(i) = left(i)
            i += 1
        }

        var k = 1
        while (k < LOG) {
            i = 0
            while (i < n) {
                val midF = jumpF(k - 1)(i)
                jumpF(k)(i) = if (midF == i) i else jumpF(k - 1)(midF)

                val midB = jumpB(k - 1)(i)
                jumpB(k)(i) = if (midB == i) i else jumpB(k - 1)(midB)

                i += 1
            }
            k += 1
        }

        // Answer queries
        val ans = new Array[Int](queries.length)
        var qIdx = 0
        while (qIdx < queries.length) {
            val uOrig = queries(qIdx)(0)
            val vOrig = queries(qIdx)(1)
            var pu = posOfOrig(uOrig)
            var pv = posOfOrig(vOrig)

            if (pu == pv) {
                ans(qIdx) = 0
            } else if (pu < pv) { // move forward
                var cur = pu
                var steps = 0
                k = LOG - 1
                while (k >= 0) {
                    val nxt = jumpF(k)(cur)
                    if (nxt < pv) {
                        cur = nxt
                        steps += 1 << k
                    }
                    k -= 1
                }
                if (right(cur) >= pv) ans(qIdx) = steps + 1 else ans(qIdx) = -1
            } else { // pu > pv, move backward
                var cur = pu
                var steps = 0
                k = LOG - 1
                while (k >= 0) {
                    val nxt = jumpB(k)(cur)
                    if (nxt > pv) {
                        cur = nxt
                        steps += 1 << k
                    }
                    k -= 1
                }
                if (left(cur) <= pv) ans(qIdx) = steps + 1 else ans(qIdx) = -1
            }

            qIdx += 1
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn path_existence_queries(
        n: i32,
        nums: Vec<i32>,
        max_diff: i32,
        queries: Vec<Vec<i32>>,
    ) -> Vec<i32> {
        let n = n as usize;
        // sort nodes by value, keep original indices
        let mut pairs: Vec<(i32, usize)> = (0..n).map(|i| (nums[i], i)).collect();
        pairs.sort_by_key(|k| k.0);
        let mut sorted_vals = vec![0i32; n];
        let mut pos_in_sorted = vec![0usize; n];
        for (idx, &(val, orig)) in pairs.iter().enumerate() {
            sorted_vals[idx] = val;
            pos_in_sorted[orig] = idx;
        }

        // next[i]: farthest index reachable from i with one edge
        let mut next = vec![0usize; n];
        let mut j = 0usize;
        for i in 0..n {
            if j < i {
                j = i;
            }
            while j + 1 < n && (sorted_vals[j + 1] - sorted_vals[i]).abs() <= max_diff {
                j += 1;
            }
            next[i] = j;
        }

        // component ids based on gaps > max_diff
        let mut comp = vec![0usize; n];
        for i in 1..n {
            if (sorted_vals[i] - sorted_vals[i - 1]).abs() > max_diff {
                comp[i] = comp[i - 1] + 1;
            } else {
                comp[i] = comp[i - 1];
            }
        }

        // binary lifting table
        let mut log = 0usize;
        while (1usize << log) <= n {
            log += 1;
        }
        let mut up: Vec<Vec<usize>> = vec![vec![0usize; n]; log];
        for i in 0..n {
            up[0][i] = next[i];
        }
        for k in 1..log {
            for i in 0..n {
                let mid = up[k - 1][i];
                up[k][i] = up[k - 1][mid];
            }
        }

        // answer queries
        let mut ans = Vec::with_capacity(queries.len());
        for q in queries.iter() {
            let u = q[0] as usize;
            let v = q[1] as usize;
            if u == v {
                ans.push(0);
                continue;
            }
            let pu = pos_in_sorted[u];
            let pv = pos_in_sorted[v];
            if comp[pu] != comp[pv] {
                ans.push(-1);
                continue;
            }
            let (mut l, r) = if pu < pv { (pu, pv) } else { (pv, pu) };
            // greedy jumps using binary lifting
            let mut steps: usize = 0;
            for k in (0..log).rev() {
                let nxt = up[k][l];
                if nxt < r {
                    l = nxt;
                    steps += 1usize << k;
                }
            }
            steps += 1; // final jump reaches or passes r
            ans.push(steps as i32);
        }

        ans
    }
}
```

## Racket

```racket
(define (path-existence-queries n nums maxDiff queries)
  (let* ((indices (range 0 n))
         (sorted-idx (sort indices < #:key (lambda (i) (list-ref nums i))))
         (sorted-vals (list->vector (map (lambda (i) (list-ref nums i)) sorted-idx)))
         (pos (make-vector n)))
    ;; position of each original node in the sorted order
    (for ([p (in-range n)])
      (vector-set! pos (list-ref sorted-idx p) p))
    ;; compute rightmost reachable index for each position
    (define right (make-vector n))
    (let ((j 0))
      (for ([i (in-range n)])
        (when (< j i) (set! j i))
        (let loop ()
          (when (and (< j n)
                     (<= (- (vector-ref sorted-vals j)
                            (vector-ref sorted-vals i))
                         maxDiff))
            (set! j (+ j 1))
            (loop)))
        (vector-set! right i (- j 1))))
    ;; component ids
    (define comp (make-vector n))
    (let ((cid -1) (prev-val #f))
      (for ([i (in-range n)])
        (let ((val (vector-ref sorted-vals i)))
          (if (or (not prev-val)
                  (> (- val prev-val) maxDiff))
              (set! cid (+ cid 1)))
          (vector-set! comp i cid)
          (set! prev-val val))))
    ;; binary lifting table
    (let ((LOG 0) (pow 1))
      (while (<= pow n)
        (set! LOG (+ LOG 1))
        (set! pow (* pow 2)))
      (define up (make-vector LOG))
      (vector-set! up 0 right)
      (for ([k (in-range 1 LOG)])
        (define prev (vector-ref up (- k 1)))
        (define cur (make-vector n))
        (for ([i (in-range n)])
          (let ((mid (vector-ref prev i)))
            (vector-set! cur i (vector-ref prev mid))))
        (vector-set! up k cur))
      ;; answer queries
      (let loop ((qs queries) (acc '()))
        (if (null? qs)
            (reverse acc)
            (let* ((q (car qs))
                   (u (list-ref q 0))
                   (v (list-ref q 1)))
              (define ans
                (cond
                  [(= u v) 0]
                  [else
                   (let ((pu (vector-ref pos u))
                         (pv (vector-ref pos v)))
                     (if (not (= (vector-ref comp pu)
                                 (vector-ref comp pv)))
                         -1
                         (let* ((pa (min pu pv)) (pb (max pu pv)))
                           (if (= pa pb) 0
                               (let ((cur pa) (steps 0))
                                 (for ([k (in-range (- LOG 1) -1 -1)])
                                   (let ((nextIdx (vector-ref (vector-ref up k) cur)))
                                     (when (< nextIdx pb)
                                       (set! cur nextIdx)
                                       (set! steps (+ steps (expt 2 k))))))
                                 (if (= cur pb) steps
                                     (+ steps 1)))))))]))
              (loop (cdr qs) (cons ans acc))))))))
```

## Erlang

```erlang
-module(solution).
-export([path_existence_queries/4]).

-spec path_existence_queries(N :: integer(), Nums :: [integer()], MaxDiff :: integer(), Queries :: [[integer()]]) -> [integer()].
path_existence_queries(_N, Nums, MaxDiff, Queries) ->
    % Build sorted list of {Value, OriginalIndex}
    Indexed = lists:zip(Nums, lists:seq(0, length(Nums)-1)),
    Sorted = lists:keysort(1, Indexed),
    % Extract sorted values and position map (original index -> position in sorted order)
    {SortedVals, PosMapList} = extract_vals_and_pos(Sorted, 0, [], []),
    ValuesArr = list_to_array(SortedVals),
    PosArr = build_pos_array(PosMapList, length(Nums)),
    % Build next array using two‑pointer technique
    NextList = build_next(0, 0, length(Nums), ValuesArr, MaxDiff, []),
    NextArr = list_to_array(NextList),
    % Binary lifting tables
    Log = ceil_log2(length(Nums)) + 1,
    UpList = build_up_arrays(length(Nums), Log, NextArr),
    % Answer queries
    Answers = [answer_query(U, V, PosArr, NextArr, UpList, Log) || [U,V] <- Queries],
    Answers.

%% ------------------------------------------------------------------
%% Helpers
%% ------------------------------------------------------------------

extract_vals_and_pos([], _Pos, AccValsRev, AccPosRev) ->
    {lists:reverse(AccValsRev), lists:reverse(AccPosRev)};
extract_vals_and_pos([{Val, OrigIdx}|Rest], Pos, AccVals, AccPos) ->
    extract_vals_and_pos(Rest, Pos+1,
                         [Val|AccVals],
                         [{OrigIdx, Pos}|AccPos]).

build_pos_array(PosPairs, N) ->
    Arr0 = array:new(N, [{default, -1}]),
    build_pos_array(PosPairs, 1, Arr0).

build_pos_array([], _I, Arr) -> Arr;
build_pos_array([{OrigIdx, Pos}|Rest], I, Arr) ->
    NewArr = array:set(OrigIdx+1, Pos, Arr),
    build_pos_array(Rest, I+1, NewArr).

list_to_array(List) ->
    N = length(List),
    A0 = array:new(N, [{default, 0}]),
    list_to_array(List, 1, A0).

list_to_array([], _Idx, Arr) -> Arr;
list_to_array([H|T], Idx, Arr) ->
    NewArr = array:set(Idx, H, Arr),
    list_to_array(T, Idx+1, NewArr).

build_next(I, Right, N, ValuesArr, MaxDiff, Acc) when I == N ->
    lists:reverse(Acc);
build_next(I, Right, N, ValuesArr, MaxDiff, Acc) ->
    NewRight = advance(Right, I, N, ValuesArr, MaxDiff),
    build_next(I+1, NewRight, N, ValuesArr, MaxDiff, [NewRight|Acc]).

advance(R, I, N, ValuesArr, MaxDiff) when R + 1 < N,
    (array:get(R+2, ValuesArr) - array:get(I+1, ValuesArr)) =< MaxDiff ->
        advance(R+1, I, N, ValuesArr, MaxDiff);
advance(R, _I, _N, _ValuesArr, _MaxDiff) -> R.

%% Build binary lifting tables: Up[0] = Next, Up[k][i] = Up[k-1][ Up[k-1][i] ]
build_up_arrays(N, Log, NextArr) ->
    build_up_arrays(1, Log, NextArr, [NextArr], N).

build_up_arrays(Level, Log, PrevArr, Acc, N) when Level == Log ->
    lists:reverse(Acc);
build_up_arrays(Level, Log, PrevArr, Acc, N) ->
    NewArr = compose_arr(N, PrevArr),
    build_up_arrays(Level+1, Log, NewArr, [NewArr|Acc], N).

compose_arr(N, Arr) ->
    A0 = array:new(N, [{default, 0}]),
    compose_arr(0, N, Arr, A0).

compose_arr(I, N, Arr, Acc) when I == N -> Acc;
compose_arr(I, N, Arr, Acc) ->
    MidIdx = array:get(I+1, Arr),
    DestIdx = array:get(MidIdx+1, Arr),
    NewAcc = array:set(I+1, DestIdx, Acc),
    compose_arr(I+1, N, Arr, NewAcc).

ceil_log2(N) when N =< 0 -> 0;
ceil_log2(N) ->
    ceil_log2(N, 0).

ceil_log2(1, Acc) -> Acc;
ceil_log2(N, Acc) ->
    ceil_log2((N+1) bsr 1, Acc+1).

answer_query(U, V, PosArr, NextArr, UpList, Log) ->
    if U =:= V -> 0;
       true ->
            PU = array:get(U+1, PosArr),
            PV = array:get(V+1, PosArr),
            {Start, Target} = if PU =< PV -> {PU, PV}; true -> {PV, PU} end,
            if Start == Target -> 0;
               true ->
                    NextStart = array:get(Start+1, NextArr),
                    if NextStart == Start -> -1;
                       true ->
                            Cur = Start,
                            Ans0 = 0,
                            {Cur2, Ans1} = jump_forward(Cur, Target, UpList, Log-1, Ans0),
                            FinalIdx = array:get(Cur2+1, NextArr),
                            AnsFinal = Ans1 + 1,
                            if FinalIdx >= Target -> AnsFinal; true -> -1 end
                    end
            end
    end.

jump_forward(Cur, Target, _UpList, K, Acc) when K < 0 ->
    {Cur, Acc};
jump_forward(Cur, Target, UpList, K, Acc) ->
    UpArr = lists:nth(K+2, UpList), % level K array (0‑based)
    JumpIdx = array:get(Cur+1, UpArr),
    if JumpIdx < Target andalso JumpIdx > Cur ->
            jump_forward(JumpIdx, Target, UpList, K-1, Acc + (1 bsl K));
       true ->
            jump_forward(Cur, Target, UpList, K-1, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec path_existence_queries(
          n :: integer,
          nums :: [integer],
          max_diff :: integer,
          queries :: [[integer]]
        ) :: [integer]
  def path_existence_queries(n, nums, max_diff, queries) do
    # sort nodes by value
    sorted = Enum.sort_by(Enum.with_index(nums), fn {v, _i} -> v end)
    vals_list = Enum.map(sorted, fn {v, _i} -> v end)
    idx_list = Enum.map(sorted, fn {_v, i} -> i end)

    vals = List.to_tuple(vals_list)

    # position of original index in sorted order
    pos_map =
      Enum.with_index(idx_list)
      |> Enum.reduce(%{}, fn {orig, pos}, acc -> Map.put(acc, orig, pos) end)

    # component id for each position (break when gap > max_diff)
    {comp_list_rev, _} =
      Enum.reduce(0..(n - 1), {[], -1}, fn i, {list, comp_id} ->
        cur_val = elem(vals, i)

        cond do
          i == 0 ->
            {[comp_id + 1 | list], comp_id + 1}

          cur_val - elem(vals, i - 1) > max_diff ->
            new_comp = comp_id + 1
            {[new_comp | list], new_comp}

          true ->
            {[comp_id | list], comp_id}
        end
      end)

    comp_by_pos = List.to_tuple(Enum.reverse(comp_list_rev))

    # next and prev reachable positions using sliding window
    next_tuple = build_next(vals, max_diff)
    prev_tuple = build_prev(vals, max_diff)

    log = :math.ceil(:math.log2(n)) |> trunc

    up_levels = build_up_tables(next_tuple, log)
    down_levels = build_up_tables(prev_tuple, log)

    Enum.map(queries, fn [u, v] ->
      if u == v do
        0
      else
        pu = Map.get(pos_map, u)
        pv = Map.get(pos_map, v)

        comp_u = elem(comp_by_pos, pu)
        comp_v = elem(comp_by_pos, pv)

        if comp_u != comp_v do
          -1
        else
          if pu < pv do
            min_steps_forward(pu, pv, up_levels)
          else
            min_steps_backward(pu, pv, down_levels)
          end
        end
      end
    end)
  end

  # build next array: farthest index j >= i with vals[j] - vals[i] <= max_diff
  defp build_next(vals, max_diff) do
    n = tuple_size(vals)

    {list_rev, _} =
      Enum.reduce(0..(n - 1), {[], 0}, fn i, {acc, j} ->
        j = advance_forward(j, i, n, vals, max_diff)
        {[j | acc], j}
      end)

    List.to_tuple(Enum.reverse(list_rev))
  end

  defp advance_forward(j, i, n, vals, max_diff) do
    if j + 1 < n and elem(vals, j + 1) - elem(vals, i) <= max_diff do
      advance_forward(j + 1, i, n, vals, max_diff)
    else
      j
    end
  end

  # build prev array: leftmost index l <= i with vals[i] - vals[l] <= max_diff
  defp build_prev(vals, max_diff) do
    n = tuple_size(vals)

    {list_rev, _} =
      Enum.reduce(0..(n - 1), {[], 0}, fn i, {acc, l} ->
        l = advance_left(l, i, vals, max_diff)
        {[l | acc], l}
      end)

    List.to_tuple(Enum.reverse(list_rev))
  end

  defp advance_left(l, i, vals, max_diff) do
    if elem(vals, i) - elem(vals, l) > max_diff do
      advance_left(l + 1, i, vals, max_diff)
    else
      l
    end
  end

  # binary lifting tables for a base tuple (next or prev)
  defp build_up_tables(base_tuple, log) do
    n = tuple_size(base_tuple)

    Enum.reduce(1..log, [base_tuple], fn _k, levels ->
      prev = List.last(levels)

      cur =
        for i <- 0..(n - 1), into: Tuple.new() do
          mid = elem(prev, i)
          elem(prev, mid)
        end

      levels ++ [cur]
    end)
  end

  defp min_steps_forward(start, target, up_levels) do
    log = length(up_levels) - 1

    {steps, _cur} =
      Enum.reduce(Enum.reverse(0..log), {0, start}, fn k, {st, cur} ->
        nxt = elem(Enum.at(up_levels, k), cur)

        if nxt < target do
          {st + (1 <<< k), nxt}
        else
          {st, cur}
        end
      end)

    steps + 1
  end

  defp min_steps_backward(start, target, down_levels) do
    log = length(down_levels) - 1

    {steps, _cur} =
      Enum.reduce(Enum.reverse(0..log), {0, start}, fn k, {st, cur} ->
        nxt = elem(Enum.at(down_levels, k), cur)

        if nxt > target do
          {st + (1 <<< k), nxt}
        else
          {st, cur}
        end
      end)

    steps + 1
  end
end
```
