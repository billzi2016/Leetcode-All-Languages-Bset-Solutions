# 3414. Maximum Score of Non-overlapping Intervals

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    struct State {
        long long w;
        int sz;
        int idx[4];
        State(long long _w = -(1LL<<60), int _sz = 0) : w(_w), sz(_sz) {}
    };
    
    // return true if a is better than b
    static bool better(const State& a, const State& b){
        if (a.w != b.w) return a.w > b.w;
        int m = min(a.sz, b.sz);
        for (int i = 0; i < m; ++i){
            if (a.idx[i] != b.idx[i]) return a.idx[i] < b.idx[i];
        }
        return a.sz < b.sz; // shorter is lexicographically smaller
    }
    
    vector<int> maximumWeight(vector<vector<int>>& intervals) {
        int n = intervals.size();
        struct Interval{
            long long l,r,w;
            int id;
        };
        vector<Interval> iv(n);
        for (int i=0;i<n;++i){
            iv[i] = {intervals[i][0], intervals[i][1], intervals[i][2], i};
        }
        sort(iv.begin(), iv.end(), [](const Interval& a, const Interval& b){
            if (a.r != b.r) return a.r < b.r;
            return a.l < b.l;
        });
        // 1-indexed
        vector<long long> ends(n+1);
        for (int i=1;i<=n;++i) ends[i]=iv[i-1].r;
        vector<int> prevIdx(n+1,0);
        for (int i=1;i<=n;++i){
            long long L = iv[i-1].l;
            auto it = lower_bound(ends.begin()+1, ends.begin()+i, L);
            int pos = (int)(it - ends.begin()) - 1; // last with r < L
            prevIdx[i] = max(pos,0);
        }
        const long long NEG = -(1LL<<60);
        const int K = 4;
        vector<vector<State>> dp(K+1, vector<State>(n+1));
        for (int i=0;i<=n;++i){
            dp[0][i] = State(0,0); // weight 0 with empty set
        }
        for (int t=1;t<=K;++t){
            for (int i=0;i<=n;++i){
                dp[t][i] = State(NEG,0);
            }
        }
        // DP
        for (int i=1;i<=n;++i){
            for (int t=0;t<=K;++t){
                // option 1: skip interval i
                State best = dp[t][i-1];
                
                if (t>0){
                    int p = prevIdx[i];
                    const State& pre = dp[t-1][p];
                    if (pre.w != NEG){
                        State cand = pre;
                        cand.w += iv[i-1].w;
                        // insert original index maintaining sorted order
                        int newId = iv[i-1].id;
                        int pos = 0;
                        while (pos < cand.sz && cand.idx[pos] < newId) ++pos;
                        for (int j=cand.sz; j>pos; --j) cand.idx[j]=cand.idx[j-1];
                        cand.idx[pos]=newId;
                        cand.sz++;
                        if (better(cand, best)) best = cand;
                    }
                }
                dp[t][i] = best;
            }
        }
        // choose best among t=0..4 at i=n
        State ans = dp[0][n];
        for (int t=1;t<=K;++t){
            if (better(dp[t][n], ans)) ans = dp[t][n];
        }
        vector<int> res;
        for (int i=0;i<ans.sz;++i) res.push_back(ans.idx[i]);
        return res;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[] maximumWeight(List<List<Integer>> intervals) {
        int n = intervals.size();
        class Node {
            int l, r;
            long w;
            int idx;
        }
        Node[] arr = new Node[n];
        for (int i = 0; i < n; i++) {
            List<Integer> cur = intervals.get(i);
            Node node = new Node();
            node.l = cur.get(0);
            node.r = cur.get(1);
            node.w = cur.get(2);
            node.idx = i;
            arr[i] = node;
        }
        Arrays.sort(arr, (a, b) -> {
            if (a.r != b.r) return Integer.compare(a.r, b.r);
            return Integer.compare(a.l, b.l);
        });
        int[] L = new int[n];
        int[] R = new int[n];
        long[] W = new long[n];
        int[] Idx = new int[n];
        for (int i = 0; i < n; i++) {
            L[i] = arr[i].l;
            R[i] = arr[i].r;
            W[i] = arr[i].w;
            Idx[i] = arr[i].idx;
        }
        int[] prev = new int[n];
        for (int i = 0; i < n; i++) {
            int lo = 0, hi = i - 1, ans = -1;
            while (lo <= hi) {
                int mid = (lo + hi) >>> 1;
                if (R[mid] < L[i]) {
                    ans = mid;
                    lo = mid + 1;
                } else {
                    hi = mid - 1;
                }
            }
            prev[i] = ans;
        }

        final int K = 4;
        long[][] dp = new long[K + 1][n];
        int[][][] seq = new int[K + 1][n][K];
        for (int k = 0; k <= K; k++) {
            Arrays.fill(dp[k], Long.MIN_VALUE);
        }

        for (int i = 0; i < n; i++) {
            for (int k = 1; k <= K; k++) {
                long bestWeight = (i > 0) ? dp[k][i - 1] : Long.MIN_VALUE;
                int[] bestSeq = null;
                if (i > 0 && dp[k][i - 1] != Long.MIN_VALUE) {
                    bestSeq = seq[k][i - 1];
                }

                long prevWeight;
                int[] prevSeq = null;
                if (k == 1) {
                    prevWeight = 0;
                    prevSeq = new int[K];
                } else {
                    int pj = prev[i];
                    if (pj == -1) {
                        prevWeight = Long.MIN_VALUE;
                    } else {
                        prevWeight = dp[k - 1][pj];
                        if (prevWeight != Long.MIN_VALUE) {
                            prevSeq = seq[k - 1][pj];
                        }
                    }
                }

                long takeWeight = (prevWeight == Long.MIN_VALUE) ? Long.MIN_VALUE : W[i] + prevWeight;
                int[] takeSeq = null;
                if (takeWeight != Long.MIN_VALUE) {
                    takeSeq = new int[K];
                    if (k > 1 && prevSeq != null) {
                        System.arraycopy(prevSeq, 0, takeSeq, 0, k - 1);
                    }
                    takeSeq[k - 1] = Idx[i];
                }

                long chosenWeight;
                int[] chosenSeq;
                if (takeWeight > bestWeight) {
                    chosenWeight = takeWeight;
                    chosenSeq = takeSeq;
                } else if (takeWeight < bestWeight) {
                    chosenWeight = bestWeight;
                    chosenSeq = bestSeq;
                } else { // equal
                    if (bestWeight == Long.MIN_VALUE) {
                        chosenWeight = Long.MIN_VALUE;
                        chosenSeq = null;
                    } else {
                        int cmp = compareLex(takeSeq, bestSeq, k);
                        if (cmp < 0) {
                            chosenWeight = takeWeight;
                            chosenSeq = takeSeq;
                        } else {
                            chosenWeight = bestWeight;
                            chosenSeq = bestSeq;
                        }
                    }
                }

                dp[k][i] = chosenWeight;
                seq[k][i] = chosenSeq;
            }
        }

        long bestW = 0;
        int bestLen = 0;
        int[] bestSeq = new int[0];
        for (int k = 1; k <= K; k++) {
            long w = dp[k][n - 1];
            if (w == Long.MIN_VALUE) continue;
            if (w > bestW) {
                bestW = w;
                bestLen = k;
                bestSeq = seq[k][n - 1];
            } else if (w == bestW) {
                int cmp = compareSeq(bestSeq, bestLen, seq[k][n - 1], k);
                if (cmp > 0) { // current sequence is lexicographically smaller
                    bestLen = k;
                    bestSeq = seq[k][n - 1];
                }
            }
        }

        int[] res = new int[bestLen];
        for (int i = 0; i < bestLen; i++) {
            res[i] = bestSeq[i];
        }
        return res;
    }

    private static int compareLex(int[] a, int[] b, int len) {
        for (int i = 0; i < len; i++) {
            if (a[i] != b[i]) return Integer.compare(a[i], b[i]);
        }
        return 0;
    }

    private static int compareSeq(int[] a, int lenA, int[] b, int lenB) {
        int m = Math.min(lenA, lenB);
        for (int i = 0; i < m; i++) {
            if (a[i] != b[i]) return Integer.compare(a[i], b[i]);
        }
        return Integer.compare(lenA, lenB);
    }
}
```

## Python

```python
class Solution(object):
    def maximumWeight(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        import bisect

        n = len(intervals)
        # attach original indices
        iv = [(l, r, w, idx) for idx, (l, r, w) in enumerate(intervals)]
        # sort by right endpoint
        iv.sort(key=lambda x: x[1])
        ends = [r for (_, r, _, _) in iv]

        # p[i] = largest index j < i such that iv[j].right < iv[i].left
        p = [-1] * n
        for i, (l, _, _, _) in enumerate(iv):
            pos = bisect.bisect_left(ends, l)
            p[i] = pos - 1

        # dp_weight[k][i]: max weight using exactly k intervals from first i intervals
        # dp_list[k][i]: corresponding tuple of original indices (lexicographically minimal for that weight)
        K = 4
        dp_weight = [[0] * (n + 1) for _ in range(K + 1)]
        dp_list = [[() for _ in range(n + 1)] for _ in range(K + 1)]

        # k = 0 already initialized to zeros and empty tuples

        for k in range(1, K + 1):
            for i in range(1, n + 1):
                # option 1: skip interval i-1
                w_skip = dp_weight[k][i - 1]
                lst_skip = dp_list[k][i - 1]

                # option 2: take interval i-1
                l_i, r_i, w_i, orig_i = iv[i - 1]
                prev_idx = p[i - 1]          # may be -1
                idx = prev_idx + 1           # dp index for prefix up to prev_idx
                w_take = w_i + dp_weight[k - 1][idx]
                lst_take = dp_list[k - 1][idx] + (orig_i,)

                if w_take > w_skip:
                    best_w, best_lst = w_take, lst_take
                elif w_take < w_skip:
                    best_w, best_lst = w_skip, lst_skip
                else:  # equal weight, choose lexicographically smaller list
                    if lst_take < lst_skip:
                        best_w, best_lst = w_take, lst_take
                    else:
                        best_w, best_lst = w_skip, lst_skip

                dp_weight[k][i] = best_w
                dp_list[k][i] = best_lst

        # choose the overall best among k = 0..4 at i = n
        best_w = -1
        best_lst = ()
        for k in range(K + 1):
            w = dp_weight[k][n]
            lst = dp_list[k][n]
            if w > best_w or (w == best_w and lst < best_lst):
                best_w, best_lst = w, lst

        return list(best_lst)
```

## Python3

```python
import bisect
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        K = 4
        n = len(intervals)
        # attach original indices and sort by right endpoint
        sorted_intervals = [(l, r, w, idx) for idx, (l, r, w) in enumerate(intervals)]
        sorted_intervals.sort(key=lambda x: x[1])  # sort by r

        ends = [r for (_, r, _, _) in sorted_intervals]
        prev = [-1] * n
        for i, (l, _, _, _) in enumerate(sorted_intervals):
            j = bisect.bisect_left(ends, l) - 1
            prev[i] = j

        # dp_weights[k][i], dp_lists[k][i] for exactly k intervals using first i+1 sorted intervals
        dp_weights = [[float('-inf')] * n for _ in range(K + 1)]
        dp_lists = [[None] * n for _ in range(K + 1)]

        # base case: 0 intervals -> weight 0, empty list
        for i in range(n):
            dp_weights[0][i] = 0
            dp_lists[0][i] = ()

        for k in range(1, K + 1):
            for i in range(n):
                # option 1: skip interval i
                if i > 0:
                    w_not = dp_weights[k][i - 1]
                    l_not = dp_lists[k][i - 1]
                else:
                    w_not = float('-inf')
                    l_not = None

                # option 2: take interval i
                _, _, w_i, idx_i = sorted_intervals[i]
                j = prev[i]
                if j != -1:
                    w_prev = dp_weights[k - 1][j]
                    l_prev = dp_lists[k - 1][j]
                else:
                    if k - 1 == 0:
                        w_prev = 0
                        l_prev = ()
                    else:
                        w_prev = float('-inf')
                        l_prev = None

                if w_prev != float('-inf'):
                    w_take = w_i + w_prev
                    new_list = tuple(sorted(l_prev + (idx_i,)))
                else:
                    w_take = float('-inf')
                    new_list = None

                # choose better option
                if w_not > w_take:
                    dp_weights[k][i] = w_not
                    dp_lists[k][i] = l_not
                elif w_take > w_not:
                    dp_weights[k][i] = w_take
                    dp_lists[k][i] = new_list
                else:  # equal weight (could be -inf)
                    if l_not is None:
                        chosen = new_list
                    elif new_list is None:
                        chosen = l_not
                    else:
                        chosen = l_not if l_not < new_list else new_list
                    dp_weights[k][i] = w_not
                    dp_lists[k][i] = chosen

        # pick the best among 0..K intervals
        best_weight = -1
        best_list = ()
        for k in range(K + 1):
            w = dp_weights[k][n - 1]
            l = dp_lists[k][n - 1]
            if w > best_weight:
                best_weight = w
                best_list = l
            elif w == best_weight and l is not None and l < best_list:
                best_list = l

        return list(best_list)
```

## C

```c
#include <stdlib.h>

typedef struct {
    int l;
    int r;
    long long w;
    int idx;
} Interval;

typedef struct {
    long long w;
    int len;
    int idx[4];
} State;

static int cmpInterval(const void *a, const void *b) {
    const Interval *ia = (const Interval *)a;
    const Interval *ib = (const Interval *)b;
    if (ia->r != ib->r) return ia->r - ib->r;
    return ia->l - ib->l;
}

static int better(const State *a, const State *b) {
    if (a->w != b->w) return a->w > b->w;
    int minlen = a->len < b->len ? a->len : b->len;
    for (int i = 0; i < minlen; ++i) {
        if (a->idx[i] != b->idx[i]) return a->idx[i] < b->idx[i];
    }
    return a->len < b->len;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maximumWeight(int** intervals, int intervalsSize, int* intervalsColSize, int* returnSize) {
    if (intervalsSize == 0) {
        *returnSize = 0;
        return NULL;
    }

    Interval *arr = (Interval *)malloc(sizeof(Interval) * intervalsSize);
    for (int i = 0; i < intervalsSize; ++i) {
        arr[i].l = intervals[i][0];
        arr[i].r = intervals[i][1];
        arr[i].w = intervals[i][2];
        arr[i].idx = i;
    }

    qsort(arr, intervalsSize, sizeof(Interval), cmpInterval);

    int *prev = (int *)malloc(sizeof(int) * intervalsSize);
    for (int i = 0; i < intervalsSize; ++i) {
        int lo = 0, hi = i - 1, ans = -1;
        while (lo <= hi) {
            int mid = (lo + hi) >> 1;
            if (arr[mid].r < arr[i].l) {
                ans = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        prev[i] = ans;
    }

    int n = intervalsSize;
    State **dp = (State **)malloc(5 * sizeof(State *));
    for (int k = 0; k <= 4; ++k) {
        dp[k] = (State *)calloc(n + 1, sizeof(State));
    }
    // dp[0][*] already zero-initialized

    for (int i = 1; i <= n; ++i) {
        dp[0][i].w = 0;
        dp[0][i].len = 0;
        for (int k = 1; k <= 4; ++k) {
            State best = dp[k][i - 1]; // not taking i-th interval
            int p = prev[i - 1];
            State base = (p == -1) ? dp[k - 1][0] : dp[k - 1][p + 1];

            State cand = base;
            cand.w += arr[i - 1].w;

            // insert original index maintaining sorted order
            int val = arr[i - 1].idx;
            int pos = 0;
            while (pos < cand.len && cand.idx[pos] < val) ++pos;
            for (int t = cand.len; t > pos; --t) {
                cand.idx[t] = cand.idx[t - 1];
            }
            cand.idx[pos] = val;
            cand.len++;

            if (better(&cand, &best)) {
                best = cand;
            }
            dp[k][i] = best;
        }
    }

    State ans = dp[0][n];
    for (int k = 1; k <= 4; ++k) {
        if (better(&dp[k][n], &ans)) {
            ans = dp[k][n];
        }
    }

    int *res = NULL;
    if (ans.len > 0) {
        res = (int *)malloc(sizeof(int) * ans.len);
        for (int i = 0; i < ans.len; ++i) {
            res[i] = ans.idx[i];
        }
    } else {
        res = (int *)malloc(0);
    }

    *returnSize = ans.len;

    free(arr);
    free(prev);
    for (int k = 0; k <= 4; ++k) free(dp[k]);
    free(dp);

    return res;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution
{
    private struct Interval
    {
        public long l, r, w;
        public int idx;
    }

    private class State
    {
        public long weight;
        public int[] seq;
        public State(long w, int[] s)
        {
            weight = w;
            seq = s;
        }
    }

    private static int CompareSeq(int[] a, int[] b)
    {
        int len = Math.Min(a.Length, b.Length);
        for (int i = 0; i < len; i++)
        {
            if (a[i] != b[i]) return a[i] - b[i];
        }
        return a.Length - b.Length;
    }

    public int[] MaximumWeight(IList<IList<int>> intervals)
    {
        int n = intervals.Count;
        var arr = new Interval[n];
        for (int i = 0; i < n; i++)
        {
            var iv = intervals[i];
            arr[i] = new Interval { l = iv[0], r = iv[1], w = iv[2], idx = i };
        }
        Array.Sort(arr, (a, b) =>
        {
            int cmp = a.r.CompareTo(b.r);
            return cmp != 0 ? cmp : a.l.CompareTo(b.l);
        });

        long[] L = new long[n];
        long[] R = new long[n];
        long[] W = new long[n];
        int[] Orig = new int[n];
        for (int i = 0; i < n; i++)
        {
            L[i] = arr[i].l;
            R[i] = arr[i].r;
            W[i] = arr[i].w;
            Orig[i] = arr[i].idx;
        }

        int[] prev = new int[n];
        for (int i = 0; i < n; i++)
        {
            int lo = 0, hi = i - 1, ans = -1;
            while (lo <= hi)
            {
                int mid = (lo + hi) >> 1;
                if (R[mid] < L[i])
                {
                    ans = mid;
                    lo = mid + 1;
                }
                else
                {
                    hi = mid - 1;
                }
            }
            prev[i] = ans;
        }

        State[,] dp = new State[5, n];
        for (int i = 0; i < n; i++)
        {
            dp[0, i] = new State(0, new int[0]);
        }

        for (int i = 0; i < n; i++)
        {
            for (int t = 1; t <= 4; t++)
            {
                State best = i > 0 ? dp[t, i - 1] : null;

                bool canTake = true;
                long prevWeight = 0;
                int[] prevSeq = new int[0];

                if (t == 1)
                {
                    // no previous interval needed
                }
                else
                {
                    int pj = prev[i];
                    if (pj >= 0 && dp[t - 1, pj] != null)
                    {
                        prevWeight = dp[t - 1, pj].weight;
                        prevSeq = dp[t - 1, pj].seq;
                    }
                    else
                    {
                        canTake = false;
                    }
                }

                if (canTake)
                {
                    long candWeight = W[i] + (t == 1 ? 0 : prevWeight);
                    int[] candSeq = new int[prevSeq.Length + 1];
                    if (prevSeq.Length > 0) Array.Copy(prevSeq, 0, candSeq, 0, prevSeq.Length);
                    candSeq[candSeq.Length - 1] = Orig[i];

                    if (best == null)
                    {
                        best = new State(candWeight, candSeq);
                    }
                    else
                    {
                        if (candWeight > best.weight)
                        {
                            best = new State(candWeight, candSeq);
                        }
                        else if (candWeight == best.weight)
                        {
                            int cmp = CompareSeq(candSeq, best.seq);
                            if (cmp < 0) best = new State(candWeight, candSeq);
                        }
                    }
                }

                dp[t, i] = best;
            }
        }

        State answer = new State(0, new int[0]);
        for (int t = 1; t <= 4; t++)
        {
            State cur = dp[t, n - 1];
            if (cur == null) continue;
            if (cur.weight > answer.weight)
            {
                answer = cur;
            }
            else if (cur.weight == answer.weight)
            {
                int cmp = CompareSeq(cur.seq, answer.seq);
                if (cmp < 0) answer = cur;
            }
        }

        return answer.seq;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} intervals
 * @return {number[]}
 */
var maximumWeight = function(intervals) {
    const n = intervals.length;
    // attach original index
    const arr = intervals.map((v, i) => ({ l: v[0], r: v[1], w: v[2], idx: i }));
    // sort by right endpoint
    arr.sort((a, b) => a.r - b.r || a.l - b.l);
    const sortedR = arr.map(o => o.r);
    // prev index for each interval (largest j with r_j < l_i)
    const prevIdx = new Array(n).fill(-1);
    for (let i = 0; i < n; ++i) {
        let lo = 0, hi = i - 1, ans = -1;
        const target = arr[i].l;
        while (lo <= hi) {
            const mid = (lo + hi) >> 1;
            if (sortedR[mid] < target) {
                ans = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        prevIdx[i] = ans;
    }

    // dpWeight[c][i], dpSeq[c][i]
    const K = 4;
    const dpWeight = Array.from({ length: K + 1 }, () => new Array(n).fill(0));
    const dpSeq = Array.from({ length: K + 1 }, () => new Array(n));

    // helper for lexicographic compare
    const isLexSmaller = (a, b) => {
        if (!b) return true;
        const len = Math.min(a.length, b.length);
        for (let i = 0; i < len; ++i) {
            if (a[i] < b[i]) return true;
            if (a[i] > b[i]) return false;
        }
        return a.length < b.length;
    };

    for (let i = 0; i < n; ++i) {
        const { w, idx } = arr[i];
        const prev = prevIdx[i];

        // inherit previous bests (not taking interval i)
        for (let c = 0; c <= K; ++c) {
            if (i === 0) {
                dpWeight[c][i] = 0;
                dpSeq[c][i] = c === 0 ? [] : null;
            } else {
                dpWeight[c][i] = dpWeight[c][i - 1];
                dpSeq[c][i] = dpSeq[c][i - 1];
            }
        }

        // consider taking interval i
        for (let c = 1; c <= K; ++c) {
            let prevWeight, prevSeq;
            if (c === 1) {
                prevWeight = 0;
                prevSeq = [];
            } else {
                if (prev >= 0 && dpSeq[c - 1][prev] !== null) {
                    prevWeight = dpWeight[c - 1][prev];
                    prevSeq = dpSeq[c - 1][prev];
                } else {
                    prevWeight = 0;
                    prevSeq = [];
                }
            }

            const candWeight = w + prevWeight;
            const candSeq = (prevSeq || []).concat(idx);

            if (candWeight > dpWeight[c][i]) {
                dpWeight[c][i] = candWeight;
                dpSeq[c][i] = candSeq;
            } else if (candWeight === dpWeight[c][i]) {
                const curSeq = dpSeq[c][i];
                if (curSeq && isLexSmaller(candSeq, curSeq)) {
                    dpSeq[c][i] = candSeq;
                }
            }
        }
    }

    // choose best among 0..4 intervals
    let bestWeight = 0;
    let bestSeq = [];
    for (let c = 1; c <= K; ++c) {
        const wgt = dpWeight[c][n - 1];
        const seq = dpSeq[c][n - 1];
        if (!seq) continue;
        if (wgt > bestWeight) {
            bestWeight = wgt;
            bestSeq = seq;
        } else if (wgt === bestWeight && isLexSmaller(seq, bestSeq)) {
            bestSeq = seq;
        }
    }
    return bestSeq;
};
```

## Typescript

```typescript
function maximumWeight(intervals: number[][]): number[] {
    const n = intervals.length;
    type Interval = { l: number; r: number; w: number; idx: number };
    const sorted: Interval[] = intervals.map((v, i) => ({ l: v[0], r: v[1], w: v[2], idx: i }))
        .sort((a, b) => a.r - b.r);

    const ends = sorted.map(it => it.r);
    const prevIdx: number[] = new Array(n).fill(-1);
    for (let i = 0; i < n; ++i) {
        let lo = 0, hi = i - 1, res = -1;
        while (lo <= hi) {
            const mid = (lo + hi) >> 1;
            if (ends[mid] < sorted[i].l) {
                res = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        prevIdx[i] = res;
    }

    const maxK = 4;
    const exactWeight: number[][] = Array.from({ length: maxK + 1 }, () => Array(n).fill(-Infinity));
    const exactList: (number[] | null)[][] = Array.from({ length: maxK + 1 }, () => Array(n).fill(null));

    // k = 1
    for (let i = 0; i < n; ++i) {
        exactWeight[1][i] = sorted[i].w;
        exactList[1][i] = [sorted[i].idx];
    }

    const prefBestWeight: number[][] = Array.from({ length: maxK + 1 }, () => Array(n).fill(-Infinity));
    const prefBestList: (number[] | null)[][] = Array.from({ length: maxK + 1 }, () => Array(n).fill(null));

    function isLexSmaller(a: number[], b: number[]): boolean {
        for (let i = 0; i < a.length && i < b.length; ++i) {
            if (a[i] < b[i]) return true;
            if (a[i] > b[i]) return false;
        }
        return a.length < b.length;
    }

    // build prefix for k=1
    for (let i = 0; i < n; ++i) {
        if (i === 0) {
            prefBestWeight[1][i] = exactWeight[1][i];
            prefBestList[1][i] = exactList[1][i];
        } else {
            const wPrev = prefBestWeight[1][i - 1];
            const wCurr = exactWeight[1][i];
            if (wCurr > wPrev) {
                prefBestWeight[1][i] = wCurr;
                prefBestList[1][i] = exactList[1][i];
            } else if (wCurr < wPrev) {
                prefBestWeight[1][i] = wPrev;
                prefBestList[1][i] = prefBestList[1][i - 1];
            } else { // equal weight
                const listPrev = prefBestList[1][i - 1]!;
                const listCurr = exactList[1][i]!;
                if (isLexSmaller(listCurr, listPrev)) {
                    prefBestWeight[1][i] = wCurr;
                    prefBestList[1][i] = listCurr;
                } else {
                    prefBestWeight[1][i] = wPrev;
                    prefBestList[1][i] = listPrev;
                }
            }
        }
    }

    // k = 2..4
    for (let k = 2; k <= maxK; ++k) {
        for (let i = 0; i < n; ++i) {
            const pj = prevIdx[i];
            let bestW = -Infinity;
            let bestL: number[] | null = null;
            if (pj !== -1) {
                const wPrev = prefBestWeight[k - 1][pj];
                if (wPrev > -Infinity) {
                    const candW = sorted[i].w + wPrev;
                    const listPrev = prefBestList[k - 1][pj]!;
                    const candL = [...listPrev, sorted[i].idx];
                    candL.sort((a, b) => a - b);
                    bestW = candW;
                    bestL = candL;
                }
            }
            exactWeight[k][i] = bestW;
            exactList[k][i] = bestL;
        }

        // build prefix for this k
        for (let i = 0; i < n; ++i) {
            if (i === 0) {
                prefBestWeight[k][i] = exactWeight[k][i];
                prefBestList[k][i] = exactList[k][i];
            } else {
                const wPrev = prefBestWeight[k][i - 1];
                const wCurr = exactWeight[k][i];
                if (wCurr > wPrev) {
                    prefBestWeight[k][i] = wCurr;
                    prefBestList[k][i] = exactList[k][i];
                } else if (wCurr < wPrev) {
                    prefBestWeight[k][i] = wPrev;
                    prefBestList[k][i] = prefBestList[k][i - 1];
                } else { // equal weight
                    const listPrev = prefBestList[k][i - 1];
                    const listCurr = exactList[k][i];
                    if (listCurr === null) {
                        prefBestWeight[k][i] = wPrev;
                        prefBestList[k][i] = listPrev;
                    } else if (listPrev === null) {
                        prefBestWeight[k][i] = wCurr;
                        prefBestList[k][i] = listCurr;
                    } else {
                        if (isLexSmaller(listCurr, listPrev!)) {
                            prefBestWeight[k][i] = wCurr;
                            prefBestList[k][i] = listCurr;
                        } else {
                            prefBestWeight[k][i] = wPrev;
                            prefBestList[k][i] = listPrev;
                        }
                    }
                }
            }
        }
    }

    let ansWeight = 0;
    let ansList: number[] = [];

    for (let k = 1; k <= maxK; ++k) {
        const w = prefBestWeight[k][n - 1];
        if (w > ansWeight) {
            ansWeight = w;
            ansList = prefBestList[k][n - 1]!.slice();
        } else if (w === ansWeight && w > 0) {
            const cand = prefBestList[k][n - 1]!;
            if (isLexSmaller(cand, ansList)) {
                ansList = cand.slice();
            }
        }
    }

    return ansList;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $intervals
     * @return Integer[]
     */
    function maximumWeight($intervals) {
        $n = count($intervals);
        if ($n == 0) return [];

        // attach original index
        $arr = [];
        foreach ($intervals as $idx => $it) {
            $arr[] = ['l' => $it[0], 'r' => $it[1], 'w' => $it[2], 'idx' => $idx];
        }

        // sort by right endpoint
        usort($arr, function ($a, $b) {
            if ($a['r'] == $b['r']) return $a['l'] <=> $b['l'];
            return $a['r'] <=> $b['r'];
        });

        // ends array for binary search
        $ends = [];
        foreach ($arr as $it) $ends[] = $it['r'];

        // prev index: largest j with end < start_i
        $prevIdx = array_fill(0, $n, -1);
        for ($i = 0; $i < $n; ++$i) {
            $l = $arr[$i]['l'];
            $low = 0;
            $high = $i - 1;
            $ans = -1;
            while ($low <= $high) {
                $mid = intdiv($low + $high, 2);
                if ($ends[$mid] < $l) {
                    $ans = $mid;
                    $low = $mid + 1;
                } else {
                    $high = $mid - 1;
                }
            }
            $prevIdx[$i] = $ans;
        }

        $NEG_INF = PHP_INT_MIN;

        // dpWeight[k][i], dpList[k][i]
        $dpWeight = [];
        $dpList   = [];
        for ($k = 0; $k <= 4; ++$k) {
            $dpWeight[$k] = array_fill(0, $n, $NEG_INF);
            $dpList[$k]   = array_fill(0, $n, []);
        }

        // base: zero intervals weight 0
        for ($i = 0; $i < $n; ++$i) {
            $dpWeight[0][$i] = 0;
            $dpList[0][$i]   = [];
        }

        // DP
        for ($i = 0; $i < $n; ++$i) {
            for ($k = 1; $k <= 4; ++$k) {
                // option1: inherit from i-1
                if ($i > 0) {
                    $bestWeight = $dpWeight[$k][$i - 1];
                    $bestList   = $dpList[$k][$i - 1];
                } else {
                    $bestWeight = $NEG_INF;
                    $bestList   = [];
                }

                // option2: take interval i
                $candWeight = $NEG_INF;
                $candList   = [];

                if ($k == 1) {
                    $candWeight = $arr[$i]['w'];
                    $candList   = [$arr[$i]['idx']];
                } else {
                    $prev = $prevIdx[$i];
                    if ($prev != -1 && $dpWeight[$k - 1][$prev] != $NEG_INF) {
                        $candWeight = $arr[$i]['w'] + $dpWeight[$k - 1][$prev];
                        $candList   = $dpList[$k - 1][$prev];
                        $candList[] = $arr[$i]['idx'];
                        sort($candList, SORT_NUMERIC);
                    }
                }

                // choose better
                if ($candWeight > $bestWeight) {
                    $dpWeight[$k][$i] = $candWeight;
                    $dpList[$k][$i]   = $candList;
                } elseif ($candWeight == $bestWeight && $candWeight != $NEG_INF) {
                    if (self::lexCompare($candList, $bestList) < 0) {
                        $dpWeight[$k][$i] = $candWeight;
                        $dpList[$k][$i]   = $candList;
                    } else {
                        $dpWeight[$k][$i] = $bestWeight;
                        $dpList[$k][$i]   = $bestList;
                    }
                } else {
                    $dpWeight[$k][$i] = $bestWeight;
                    $dpList[$k][$i]   = $bestList;
                }
            }
        }

        // find best among k=1..4
        $ansWeight = -1;
        $ansList   = [];
        for ($k = 1; $k <= 4; ++$k) {
            $w = $dpWeight[$k][$n - 1];
            if ($w > $ansWeight) {
                $ansWeight = $w;
                $ansList   = $dpList[$k][$n - 1];
            } elseif ($w == $ansWeight && $w != $NEG_INF) {
                if (self::lexCompare($dpList[$k][$n - 1], $ansList) < 0) {
                    $ansList = $dpList[$k][$n - 1];
                }
            }
        }

        return $ansList;
    }

    private static function lexCompare($a, $b) {
        $lenA = count($a);
        $lenB = count($b);
        $min  = min($lenA, $lenB);
        for ($i = 0; $i < $min; ++$i) {
            if ($a[$i] < $b[$i]) return -1;
            if ($a[$i] > $b[$i]) return 1;
        }
        if ($lenA == $lenB) return 0;
        return ($lenA < $lenB) ? -1 : 1;
    }
}
```

## Swift

```swift
class Solution {
    func maximumWeight(_ intervals: [[Int]]) -> [Int] {
        let n = intervals.count
        if n == 0 { return [] }
        struct Item {
            var l: Int
            var r: Int
            var w: Int
            var idx: Int
        }
        var items = [Item]()
        items.reserveCapacity(n)
        for (i, arr) in intervals.enumerated() {
            items.append(Item(l: arr[0], r: arr[1], w: arr[2], idx: i))
        }
        items.sort { $0.r < $1.r }
        var L = [Int](repeating: 0, count: n + 1)
        var R = [Int](repeating: 0, count: n + 1)
        var W = [Int](repeating: 0, count: n + 1)
        var origIdx = [Int](repeating: 0, count: n + 1)
        for i in 1...n {
            let it = items[i - 1]
            L[i] = it.l
            R[i] = it.r
            W[i] = it.w
            origIdx[i] = it.idx
        }
        var P = [Int](repeating: 0, count: n + 1)
        for i in 1...n {
            var lo = 1, hi = i - 1, ans = 0
            while lo <= hi {
                let mid = (lo + hi) >> 1
                if R[mid] < L[i] {
                    ans = mid
                    lo = mid + 1
                } else {
                    hi = mid - 1
                }
            }
            P[i] = ans
        }
        struct State {
            var weight: Int64
            var indices: [Int]
        }
        func isLexSmaller(_ a: [Int], _ b: [Int]) -> Bool {
            let m = min(a.count, b.count)
            for i in 0..<m {
                if a[i] != b[i] { return a[i] < b[i] }
            }
            return a.count < b.count
        }
        var dp = Array(repeating: Array(repeating: State(weight: 0, indices: []), count: n + 1), count: 5)
        for t in 1...4 {
            for i in 1...n {
                let opt1 = dp[t][i - 1]
                let prevIdx = P[i]
                var opt2Weight = Int64(W[i]) + dp[t - 1][prevIdx].weight
                var opt2Indices = dp[t - 1][prevIdx].indices
                opt2Indices.append(origIdx[i])
                opt2Indices.sort()
                let opt2 = State(weight: opt2Weight, indices: opt2Indices)
                if opt2.weight > opt1.weight {
                    dp[t][i] = opt2
                } else if opt2.weight < opt1.weight {
                    dp[t][i] = opt1
                } else {
                    dp[t][i] = isLexSmaller(opt2.indices, opt1.indices) ? opt2 : opt1
                }
            }
        }
        var best = State(weight: 0, indices: [])
        for t in 1...4 {
            let cand = dp[t][n]
            if cand.weight > best.weight || (cand.weight == best.weight && isLexSmaller(cand.indices, best.indices)) {
                best = cand
            }
        }
        return best.indices
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayList
import java.util.Collections

class Solution {
    data class Interval(val l: Int, val r: Int, val w: Long, val idx: Int)

    private fun lexLess(a: List<Int>, b: List<Int>): Boolean {
        val n = kotlin.math.min(a.size, b.size)
        for (i in 0 until n) {
            if (a[i] != b[i]) return a[i] < b[i]
        }
        return a.size < b.size
    }

    fun maximumWeight(intervals: List<List<Int>>): IntArray {
        val n = intervals.size
        val sorted = ArrayList<Interval>(n)
        for ((i, it) in intervals.withIndex()) {
            sorted.add(Interval(it[0], it[1], it[2].toLong(), i))
        }
        sorted.sortWith(compareBy<Interval> { it.r }.thenBy { it.l })

        val ends = IntArray(n)
        for (i in 0 until n) ends[i] = sorted[i].r

        // prev[i]: largest index j (1‑based) such that intervals[j-1].r < intervals[i-1].l
        val prev = IntArray(n + 1)
        for (i in 1..n) {
            val l = sorted[i - 1].l
            var lo = 0
            var hi = n - 1
            var ans = -1
            while (lo <= hi) {
                val mid = (lo + hi) ushr 1
                if (ends[mid] < l) {
                    ans = mid
                    lo = mid + 1
                } else {
                    hi = mid - 1
                }
            }
            prev[i] = ans + 1 // convert to 1‑based, 0 means none
        }

        val K = 4
        val dpWeight = Array(K + 1) { LongArray(n + 1) }
        val dpList = Array(K + 1) { Array<List<Int>>(n + 1) { emptyList() } }

        // base: t = 0 already zero weight and empty list

        for (i in 1..n) {
            for (t in 0..K) {
                var bestW = dpWeight[t][i - 1]
                var bestL = dpList[t][i - 1]

                if (t > 0) {
                    val p = prev[i]
                    val wTake = sorted[i - 1].w + dpWeight[t - 1][p]
                    if (wTake > bestW) {
                        bestW = wTake
                        val lst = ArrayList<Int>(dpList[t - 1][p])
                        lst.add(sorted[i - 1].idx)
                        Collections.sort(lst)
                        bestL = lst
                    } else if (wTake == bestW) {
                        val lstTmp = ArrayList<Int>(dpList[t - 1][p])
                        lstTmp.add(sorted[i - 1].idx)
                        Collections.sort(lstTmp)
                        if (lexLess(lstTmp, bestL)) {
                            bestL = lstTmp
                        }
                    }
                }

                dpWeight[t][i] = bestW
                dpList[t][i] = bestL
            }
        }

        var finalWeight = -1L
        var answer: List<Int> = emptyList()
        for (t in 1..K) {
            val w = dpWeight[t][n]
            val lst = dpList[t][n]
            if (w > finalWeight) {
                finalWeight = w
                answer = lst
            } else if (w == finalWeight && w != -1L) {
                if (lexLess(lst, answer)) {
                    answer = lst
                }
            }
        }

        return answer.toIntArray()
    }
}
```

## Dart

```dart
class Solution {
  List<int> maximumWeight(List<List<int>> intervals) {
    int n = intervals.length;
    // Build list with original indices
    List<List<int>> arr = [];
    for (int i = 0; i < n; i++) {
      var iv = intervals[i];
      arr.add([iv[0], iv[1], iv[2], i]); // l, r, w, idx
    }
    // Sort by right endpoint
    arr.sort((a, b) => a[1].compareTo(b[1]));

    // Precompute prev indices (dp index base 0..n)
    List<int> ends = List.generate(n, (i) => arr[i][1]);
    List<int> prev = List.filled(n + 1, 0);
    for (int i = 1; i <= n; i++) {
      int l = arr[i - 1][0];
      int lo = 0, hi = n - 1, ans = -1;
      while (lo <= hi) {
        int mid = (lo + hi) >> 1;
        if (ends[mid] < l) {
          ans = mid;
          lo = mid + 1;
        } else {
          hi = mid - 1;
        }
      }
      prev[i] = ans + 1; // dp index, 0 means none
    }

    const int K = 4;
    List<List<int>> dpWeight = List.generate(K + 1, (_) => List.filled(n + 1, 0));
    List<List<List<int>?>> dpSeq =
        List.generate(K + 1, (_) => List.filled(n + 1, null));

    // Initialize cnt=0 sequences
    for (int i = 0; i <= n; i++) {
      dpSeq[0][i] = [];
    }

    bool isLexSmaller(List<int> a, List<int> b) {
      int len = a.length < b.length ? a.length : b.length;
      for (int i = 0; i < len; i++) {
        if (a[i] != b[i]) return a[i] < b[i];
      }
      return a.length < b.length;
    }

    for (int i = 1; i <= n; i++) {
      // copy not-take case
      for (int cnt = 0; cnt <= K; cnt++) {
        dpWeight[cnt][i] = dpWeight[cnt][i - 1];
        dpSeq[cnt][i] = dpSeq[cnt][i - 1];
      }
      // consider taking interval i-1
      for (int cnt = 1; cnt <= K; cnt++) {
        int prevIdx = prev[i];
        if (prevIdx < 0) continue;
        List<int>? prevSeq = dpSeq[cnt - 1][prevIdx];
        if (cnt > 1 && prevSeq == null) continue;
        int takeWeight = arr[i - 1][2] + dpWeight[cnt - 1][prevIdx];
        List<int> candidateSeq = List.from(prevSeq ?? []);
        candidateSeq.add(arr[i - 1][3]);
        candidateSeq.sort();
        int curWeight = dpWeight[cnt][i];
        List<int>? curSeq = dpSeq[cnt][i];
        if (takeWeight > curWeight) {
          dpWeight[cnt][i] = takeWeight;
          dpSeq[cnt][i] = candidateSeq;
        } else if (takeWeight == curWeight && curSeq != null) {
          if (isLexSmaller(candidateSeq, curSeq)) {
            dpWeight[cnt][i] = takeWeight;
            dpSeq[cnt][i] = candidateSeq;
          }
        }
      }
    }

    int bestWeight = -1;
    List<int> bestSeq = [];
    for (int cnt = 0; cnt <= K; cnt++) {
      int w = dpWeight[cnt][n];
      List<int>? seq = dpSeq[cnt][n];
      if (seq == null) continue;
      if (w > bestWeight) {
        bestWeight = w;
        bestSeq = seq;
      } else if (w == bestWeight && isLexSmaller(seq, bestSeq)) {
        bestSeq = seq;
      }
    }
    return bestSeq;
  }
}
```

## Golang

```go
package main

import (
	"sort"
)

type interval struct {
	l, r int
	w    int64
	idx  int
}

type state struct {
	score int64
	seq   [4]int
	len   int
}

// compare if a is lexicographically smaller than b
func less(aSeq [4]int, aLen int, bSeq [4]int, bLen int) bool {
	minL := aLen
	if bLen < minL {
		minL = bLen
	}
	for i := 0; i < minL; i++ {
		if aSeq[i] < bSeq[i] {
			return true
		}
		if aSeq[i] > bSeq[i] {
			return false
		}
	}
	return aLen < bLen
}

func maximumWeight(intervals [][]int) []int {
	n := len(intervals)
	itv := make([]interval, n)
	for i, v := range intervals {
		itv[i] = interval{
			l:   v[0],
			r:   v[1],
			w:   int64(v[2]),
			idx: i,
		}
	}
	sort.Slice(itv, func(i, j int) bool {
		if itv[i].r == itv[j].r {
			return itv[i].l < itv[j].l
		}
		return itv[i].r < itv[j].r
	})

	ends := make([]int, n)
	for i := 0; i < n; i++ {
		ends[i] = itv[i].r
	}

	// dp[k][i]: best state using at most k intervals from first i+1 intervals (sorted)
	dp := make([][]state, 5)
	for k := 0; k <= 4; k++ {
		dp[k] = make([]state, n)
	}
	zeroState := state{score: 0, len: 0}

	// dp[0][*] stays zeroState (already zero-valued)

	for i := 0; i < n; i++ {
		// find largest j with ends[j] < itv[i].l
		l := itv[i].l
		pos := -1
		lo, hi := 0, i-1
		for lo <= hi {
			mid := (lo + hi) >> 1
			if ends[mid] < l {
				pos = mid
				lo = mid + 1
			} else {
				hi = mid - 1
			}
		}
		for k := 1; k <= 4; k++ {
			var best state
			if i > 0 {
				best = dp[k][i-1]
			} else {
				best = zeroState
			}

			var prev state
			if pos >= 0 {
				prev = dp[k-1][pos]
			} else {
				prev = zeroState
			}
			candScore := itv[i].w + prev.score

			// build candidate sequence (sorted)
			var candSeq [4]int
			candLen := prev.len
			for t := 0; t < candLen; t++ {
				candSeq[t] = prev.seq[t]
			}
			candSeq[candLen] = itv[i].idx
			candLen++

			// insertion sort for up to 4 elements
			for a := candLen - 1; a > 0 && candSeq[a] < candSeq[a-1]; a-- {
				candSeq[a], candSeq[a-1] = candSeq[a-1], candSeq[a]
			}

			take := false
			if candScore > best.score {
				take = true
			} else if candScore == best.score {
				if less(candSeq, candLen, best.seq, best.len) {
					take = true
				}
			}
			if take {
				dp[k][i] = state{score: candScore, seq: candSeq, len: candLen}
			} else {
				dp[k][i] = best
			}
		}
	}

	ans := zeroState
	for k := 1; k <= 4; k++ {
		st := dp[k][n-1]
		if st.score > ans.score || (st.score == ans.score && less(st.seq, st.len, ans.seq, ans.len)) {
			ans = st
		}
	}

	res := make([]int, ans.len)
	for i := 0; i < ans.len; i++ {
		res[i] = ans.seq[i]
	}
	return res
}
```

## Ruby

```ruby
def maximum_weight(intervals)
  n = intervals.size
  # attach original indices
  arr = intervals.each_with_index.map do |(l, r, w), idx|
    { l: l, r: r, w: w, idx: idx }
  end

  # sort by right endpoint
  arr.sort_by! { |it| it[:r] }

  ends = arr.map { |it| it[:r] }

  # compute prev index for each interval
  prev = Array.new(n, -1)
  (0...n).each do |i|
    l = arr[i][:l]
    lo = 0
    hi = i - 1
    ans = -1
    while lo <= hi
      mid = (lo + hi) / 2
      if ends[mid] < l
        ans = mid
        lo = mid + 1
      else
        hi = mid - 1
      end
    end
    prev[i] = ans
  end

  neg_inf = -(1 << 60)

  # dp_weight[t][i]: max weight using exactly t intervals among first i+1 sorted intervals
  dp_weight = Array.new(5) { Array.new(n, neg_inf) }
  dp_seq = Array.new(5) { Array.new(n) }

  # base for t=0: weight 0, empty sequence
  (0...n).each do |i|
    dp_weight[0][i] = 0
    dp_seq[0][i] = []
  end

  (0...n).each do |i|
    cur = arr[i]
    cur_idx = cur[:idx]

    (1..4).each do |t|
      # option: not take current interval
      if i > 0 && dp_weight[t][i - 1] != neg_inf
        w_not = dp_weight[t][i - 1]
        seq_not = dp_seq[t][i - 1]
      else
        w_not = neg_inf
        seq_not = nil
      end

      # option: take current interval
      if t == 1
        w_take = cur[:w]
        seq_take = [cur_idx]
      else
        p = prev[i]
        if p >= 0 && dp_weight[t - 1][p] != neg_inf
          w_take = cur[:w] + dp_weight[t - 1][p]
          seq_take = (dp_seq[t - 1][p] + [cur_idx]).sort
        else
          w_take = neg_inf
          seq_take = nil
        end
      end

      # choose better option
      if w_take > w_not
        dp_weight[t][i] = w_take
        dp_seq[t][i] = seq_take
      elsif w_take < w_not
        dp_weight[t][i] = w_not
        dp_seq[t][i] = seq_not
      else # equal weight
        if w_take == neg_inf
          dp_weight[t][i] = neg_inf
          dp_seq[t][i] = nil
        else
          # both sequences exist, pick lexicographically smaller
          best_seq = (seq_take <=> seq_not) == -1 ? seq_take : seq_not
          dp_weight[t][i] = w_take
          dp_seq[t][i] = best_seq
        end
      end
    end
  end

  # find overall best among t=0..4 at the last index
  best_weight = 0
  best_seq = []
  (1..4).each do |t|
    w = dp_weight[t][n - 1]
    next if w == neg_inf
    seq = dp_seq[t][n - 1]
    if w > best_weight
      best_weight = w
      best_seq = seq
    elsif w == best_weight && (seq <=> best_seq) == -1
      best_seq = seq
    end
  end

  best_seq
end
```

## Scala

```scala
object Solution {
    case class State(score: Long, indices: List[Int])

    private val NEG: Long = Long.MinValue / 4

    private def better(a: State, b: State): Boolean = {
        if (a.score != b.score) a.score > b.score
        else {
            val la = a.indices
            val lb = b.indices
            val len = math.min(la.length, lb.length)
            var i = 0
            while (i < len) {
                if (la(i) != lb(i)) return la(i) < lb(i)
                i += 1
            }
            la.length < lb.length
        }
    }

    def maximumWeight(intervals: List[List[Int]]): Array[Int] = {
        val n = intervals.length
        // (l, r, w, originalIndex)
        val withIdx = intervals.zipWithIndex.map { case (lst, idx) =>
            (lst(0), lst(1), lst(2).toLong, idx)
        }
        val sorted = withIdx.sortBy(_._2) // sort by right endpoint
        val best = Array.ofDim[State](5, n)

        // initialize all states to negative infinity
        for (c <- 0 to 4; i <- 0 until n) {
            best(c)(i) = State(NEG, Nil)
        }
        // count 0: score 0 with empty list
        for (i <- 0 until n) best(0)(i) = State(0L, Nil)

        for (i <- 0 until n) {
            val (l, r, w, origIdx) = sorted(i)
            // binary search for the last interval ending before l
            var lo = 0
            var hi = i - 1
            var prev = -1
            while (lo <= hi) {
                val mid = (lo + hi) >>> 1
                if (sorted(mid)._2 < l) {
                    prev = mid
                    lo = mid + 1
                } else {
                    hi = mid - 1
                }
            }

            for (cnt <- 1 to 4) {
                var cand = State(NEG, Nil)

                if (cnt == 1) {
                    // take this interval alone
                    cand = State(w, List(origIdx))
                } else if (prev >= 0) {
                    val prevState = best(cnt - 1)(prev)
                    if (prevState.score != NEG) {
                        val newScore = prevState.score + w
                        val combined = (prevState.indices :+ origIdx).sorted
                        cand = State(newScore, combined)
                    }
                }

                val prevBest = if (i > 0) best(cnt)(i - 1) else State(NEG, Nil)

                best(cnt)(i) = if (better(cand, prevBest)) cand else prevBest
            }
        }

        var answer = State(NEG, Nil)
        for (cnt <- 1 to 4) {
            val st = best(cnt)(n - 1)
            if (better(st, answer)) answer = st
        }
        if (answer.score == NEG) return Array.emptyIntArray
        answer.indices.toArray
    }
}
```

## Rust

```rust
use std::cmp::Ordering;

#[derive(Clone)]
struct State {
    weight: i64,
    indices: Vec<i32>,
}

fn lex_smaller(a: &Vec<i32>, b: &Vec<i32>) -> bool {
    let m = a.len().min(b.len());
    for i in 0..m {
        if a[i] != b[i] {
            return a[i] < b[i];
        }
    }
    a.len() < b.len()
}

impl Solution {
    pub fn maximum_weight(intervals: Vec<Vec<i32>>) -> Vec<i32> {
        let n = intervals.len();
        if n == 0 {
            return vec![];
        }

        // Convert and keep original index
        let mut ivals: Vec<(i64, i64, i64, i32)> = intervals
            .into_iter()
            .enumerate()
            .map(|(idx, v)| (v[0] as i64, v[1] as i64, v[2] as i64, idx as i32))
            .collect();

        // Sort by right endpoint, then left, then original index for determinism
        ivals.sort_by(|a, b| {
            if a.1 != b.1 {
                a.1.cmp(&b.1)
            } else if a.0 != b.0 {
                a.0.cmp(&b.0)
            } else {
                a.3.cmp(&b.3)
            }
        });

        // Precompute previous non‑overlapping index for each interval
        let mut rights: Vec<i64> = ivals.iter().map(|x| x.1).collect();
        let mut prev: Vec<isize> = vec![-1; n];
        for i in 0..n {
            let l = ivals[i].0;
            // binary search for last right < l
            let mut lo = 0usize;
            let mut hi = i;
            while lo < hi {
                let mid = (lo + hi) / 2;
                if rights[mid] < l {
                    lo = mid + 1;
                } else {
                    hi = mid;
                }
            }
            prev[i] = if lo == 0 { -1 } else { (lo - 1) as isize };
        }

        const NEG_INF: i64 = i64::MIN / 4;

        // dp[count][i] = best state using up to interval i (inclusive)
        let mut dp: Vec<Vec<State>> = vec![
            vec![
                State {
                    weight: 0,
                    indices: Vec::new()
                };
                n
            ];
            5
        ];

        // Initialize counts >0 with negative infinity
        for c in 1..=4 {
            for i in 0..n {
                dp[c][i] = State {
                    weight: NEG_INF,
                    indices: Vec::new(),
                };
            }
        }

        for i in 0..n {
            // propagate previous bests
            if i > 0 {
                for c in 0..=4 {
                    dp[c][i] = dp[c][i - 1].clone();
                }
            } else {
                // i == 0, dp[0][0] already set to weight 0
                dp[0][0] = State {
                    weight: 0,
                    indices: Vec::new(),
                };
            }

            for c in 1..=4 {
                // candidate taking interval i
                let cand_state_opt = if prev[i] >= 0 {
                    let prev_state = &dp[c - 1][prev[i] as usize];
                    if prev_state.weight > NEG_INF {
                        Some((
                            prev_state.weight + ivals[i].2,
                            {
                                let mut v = prev_state.indices.clone();
                                v.push(ivals[i].3);
                                v
                            },
                        ))
                    } else {
                        None
                    }
                } else {
                    // No previous interval, can only take if c == 1 (since we need exactly one interval)
                    if c == 1 {
                        Some((ivals[i].2, vec![ivals[i].3]))
                    } else {
                        None
                    }
                };

                if let Some((cand_weight, cand_indices)) = cand_state_opt {
                    let cur = &dp[c][i];
                    if cand_weight > cur.weight
                        || (cand_weight == cur.weight && lex_smaller(&cand_indices, &cur.indices))
                    {
                        dp[c][i] = State {
                            weight: cand_weight,
                            indices: cand_indices,
                        };
                    }
                }
            }
        }

        // Choose best among counts 0..4 at the last position
        let mut best_state = State {
            weight: NEG_INF,
            indices: Vec::new(),
        };
        for c in 0..=4 {
            let state = &dp[c][n - 1];
            if state.weight > best_state.weight
                || (state.weight == best_state.weight && lex_smaller(&state.indices, &best_state.indices))
            {
                best_state = state.clone();
            }
        }

        best_state.indices
    }
}
```

## Racket

```racket
(define/contract (maximum-weight intervals)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ((n (length intervals))
         ;; attach original index
         (with-idx
          (for/list ([pair intervals] [i (in-naturals)])
            (list (first pair) (second pair) (third pair) i)))
         ;; sort by right endpoint
         (sorted
          (sort with-idx (lambda (a b) (< (cadr a) (cadr b)))))
         (L (make-vector (+ n 1) 0))
         (R (make-vector (+ n 1) 0))
         (W (make-vector (+ n 1) 0))
         (Idx (make-vector (+ n 1) 0)))
    ;; fill vectors (1‑based)
    (for ([i (in-range 1 (+ n 1))]
          [it sorted])
      (vector-set! L i (list-ref it 0))
      (vector-set! R i (list-ref it 1))
      (vector-set! W i (list-ref it 2))
      (vector-set! Idx i (list-ref it 3)))
    ;; compute predecessor p[i]
    (define p (make-vector (+ n 1) 0))
    (for ([i (in-range 1 (+ n 1))])
      (let* ((li (vector-ref L i))
             (low 1)
             (high (- i 1))
             (ans 0))
        (let loop ()
          (when (<= low high)
            (define mid (quotient (+ low high) 2))
            (if (< (vector-ref R mid) li)
                (begin (set! ans mid) (set! low (+ mid 1)))
                (set! high (- mid 1)))
            (loop)))
        (vector-set! p i ans)))
    ;; DP tables: dpW[k][i] = max weight, dpL[k][i] = list of indices
    (define dpW (for/list ([k (in-range 5)]) (make-vector (+ n 1) 0)))
    (define dpL (for/list ([k (in-range 5)]) (make-vector (+ n 1) '())))
    ;; lexicographic comparison
    (define (lex-less? a b)
      (cond [(null? a) (and (not (null? b)) #t)]
            [(null? b) #f]
            [else (let ((ah (car a)) (bh (car b)))
                    (if (< ah bh) #t
                        (if (> ah bh) #f
                            (lex-less? (cdr a) (cdr b)))))]))
    ;; DP iteration
    (for ([i (in-range 1 (+ n 1))])
      (for ([k (in-range 1 5)])
        (define wPrev (vector-ref (list-ref dpW k) (- i 1)))
        (define lstPrev (vector-ref (list-ref dpL k) (- i 1)))
        (define wTake
          (+ (vector-ref W i)
             (vector-ref (list-ref dpW (- k 1)) (vector-ref p i))))
        (define baseLst
          (vector-ref (list-ref dpL (- k 1)) (vector-ref p i)))
        (define lstTake (sort (append baseLst (list (vector-ref Idx i))) <))
        (cond [(> wTake wPrev)
               (vector-set! (list-ref dpW k) i wTake)
               (vector-set! (list-ref dpL k) i lstTake)]
              [(< wTake wPrev)
               (vector-set! (list-ref dpW k) i wPrev)
               (vector-set! (list-ref dpL k) i lstPrev)]
              [else ; equal weight, tie‑break lexicographically
               (if (lex-less? lstTake lstPrev)
                   (begin
                     (vector-set! (list-ref dpW k) i wTake)
                     (vector-set! (list-ref dpL k) i lstTake))
                   (begin
                     (vector-set! (list-ref dpW k) i wPrev)
                     (vector-set! (list-ref dpL k) i lstPrev)))])))
    ;; choose best among 0..4 intervals at position n
    (let loop ((k 0) (bestW -1) (bestLst '()))
      (if (> k 4)
          bestLst
          (let* ((w (vector-ref (list-ref dpW k) n))
                 (lst (vector-ref (list-ref dpL k) n)))
            (cond [(> w bestW) (loop (+ k 1) w lst)]
                  [(< w bestW) (loop (+ k 1) bestW bestLst)]
                  [else (if (lex-less? lst bestLst)
                            (loop (+ k 1) w lst)
                            (loop (+ k 1) bestW bestLst))]))))))
```

## Erlang

```erlang
-module(solution).
-export([maximum_weight/1]).

-spec maximum_weight(Intervals :: [[integer()]]) -> [integer()].
maximum_weight(Intervals) ->
    Indexed = lists:zipwith(fun(I, [L,R,W]) -> {L,R,W,I-1} end,
                            lists:seq(0, length(Intervals)-1),
                            Intervals),
    Sorted = lists:sort(fun(A,B) -> element(2,A) < element(2,B) end, Indexed),

    LsList = [element(1,T) || T <- Sorted],
    RsList = [element(2,T) || T <- Sorted],
    WsList = [element(3,T) || T <- Sorted],
    IdxList = [element(4,T) || T <- Sorted],

    EndsTuple = list_to_tuple(RsList),
    LTuple = list_to_tuple(LsList),
    WsTuple = list_to_tuple(WsList),
    IdxTuple = list_to_tuple(IdxList),

    N = length(Sorted),
    Ptuple = compute_p(N, LTuple, EndsTuple),

    Map0 = #{0 => {0, []}},
    MapsInit = [{0,Map0},{1,#{}},{2,#{}},{3,#{}},{4,#{}}],
    FinalMaps = dp_loop(1, N, WsTuple, IdxTuple, Ptuple, MapsInit),
    find_best(FinalMaps, N).

%% compute predecessor indices
-spec compute_p(integer(), tuple(), tuple()) -> tuple().
compute_p(N, LTuple, EndsTuple) ->
    compute_p(1, N, LTuple, EndsTuple, []).

-spec compute_p(integer(), integer(), tuple(), tuple(), [integer()]) -> tuple().
compute_p(I, N, _LTuple, _EndsTuple, Acc) when I > N ->
    list_to_tuple(lists:reverse(Acc));
compute_p(I, N, LTuple, EndsTuple, Acc) ->
    Li = element(I, LTuple),
    PrevIdx = find_prev(Li, EndsTuple, I-1),
    compute_p(I+1, N, LTuple, EndsTuple, [PrevIdx|Acc]).

%% binary search for largest j < High with Ends[j] < L
-spec find_prev(integer(), tuple(), integer()) -> integer().
find_prev(_L, _EndsTuple, 0) -> 0;
find_prev(L, EndsTuple, High) ->
    find_prev(L, EndsTuple, 1, High, 0).

-spec find_prev(integer(), tuple(), integer(), integer(), integer()) -> integer().
find_prev(_L, _EndsTuple, Low, High, Ans) when Low > High -> Ans;
find_prev(L, EndsTuple, Low, High, Ans) ->
    Mid = (Low + High) div 2,
    MidVal = element(Mid, EndsTuple),
    if
        MidVal < L ->
            find_prev(L, EndsTuple, Mid+1, High, Mid);
        true ->
            find_prev(L, EndsTuple, Low, Mid-1, Ans)
    end.

%% DP iteration
-spec dp_loop(integer(), integer(), tuple(), tuple(), tuple(),
              [{integer(), map()}]) -> [{integer(), map()}].
dp_loop(I, N, _WsTuple, _IdxTuple, _Ptuple, Maps) when I > N ->
    Maps;
dp_loop(I, N, WsTuple, IdxTuple, Ptuple,
        [{0,Map0},{1,Map1},{2,Map2},{3,Map3},{4,Map4}]=Maps) ->

    Wi = element(I, WsTuple),
    Ori = element(I, IdxTuple),
    PrevIdx = element(I, Ptuple),

    Opt1_1 = maps:get(I-1, Map1, {0, []}),
    Opt1_2 = maps:get(I-1, Map2, {0, []}),
    Opt1_3 = maps:get(I-1, Map3, {0, []}),
    Opt1_4 = maps:get(I-1, Map4, {0, []}),

    PrevState0 = maps:get(PrevIdx, Map0, {0, []}),
    PrevState1 = maps:get(PrevIdx, Map1, {0, []}),
    PrevState2 = maps:get(PrevIdx, Map2, {0, []}),
    PrevState3 = maps:get(PrevIdx, Map3, {0, []}),

    % k = 1
    Opt2Score1 = Wi + element(1, PrevState0),
    Opt2Seq1 = element(2, PrevState0) ++ [Ori],
    Best1 = better({Opt2Score1, Opt2Seq1}, Opt1_1),
    NewMap1 = maps:put(I, Best1, Map1),

    % k = 2
    Opt2Score2 = Wi + element(1, PrevState1),
    Opt2Seq2 = element(2, PrevState1) ++ [Ori],
    Best2 = better({Opt2Score2, Opt2Seq2}, Opt1_2),
    NewMap2 = maps:put(I, Best2, Map2),

    % k = 3
    Opt2Score3 = Wi + element(1, PrevState2),
    Opt2Seq3 = element(2, PrevState2) ++ [Ori],
    Best3 = better({Opt2Score3, Opt2Seq3}, Opt1_3),
    NewMap3 = maps:put(I, Best3, Map3),

    % k = 4
    Opt2Score4 = Wi + element(1, PrevState3),
    Opt2Seq4 = element(2, PrevState3) ++ [Ori],
    Best4 = better({Opt2Score4, Opt2Seq4}, Opt1_4),
    NewMap4 = maps:put(I, Best4, Map4),

    dp_loop(I+1, N, WsTuple, IdxTuple, Ptuple,
            [{0,Map0},{1,NewMap1},{2,NewMap2},{3,NewMap3},{4,NewMap4}]).

%% choose better of two states
-spec better({integer(), [integer()]}, {integer(), [integer()]}) -> {integer(), [integer()]}.
better({S1, Seq1} = A, {S2, Seq2} = B) ->
    if
        S1 > S2 -> A;
        S1 < S2 -> B;
        true ->
            case less_seq(Seq1, Seq2) of
                true -> A;
                false -> B
            end
    end.

%% lexicographic comparison: returns true if A < B
-spec less_seq([integer()], [integer()]) -> boolean().
less_seq([], []) -> false;
less_seq([], _) -> true;
less_seq(_, []) -> false;
less_seq([H1|T1], [H2|T2]) ->
    if
        H1 < H2 -> true;
        H1 > H2 -> false;
        true -> less_seq(T1, T2)
    end.

%% retrieve final best sequence among k=0..4 at position N
-spec find_best([{integer(), map()}], integer()) -> [integer()].
find_best(Maps, N) ->
    {_M0, M1, M2, M3, M4} = {maps:get(0, Maps), maps:get(1, Maps),
                               maps:get(2, Maps), maps:get(3, Maps),
                               maps:get(4, Maps)},
    Best0 = {0, []},
    Best1 = better(maps:get(N, M1, {0, []}), Best0),
    Best2 = better(maps:get(N, M2, {0, []}), Best1),
    Best3 = better(maps:get(N, M3, {0, []}), Best2),
    Best4 = better(maps:get(N, M4, {0, []}), Best3),
    element(2, Best4).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_weight(intervals :: [[integer]]) :: [integer]
  def maximum_weight(intervals) do
    # Attach original indices and sort by right endpoint
    sorted =
      intervals
      |> Enum.with_index()
      |> Enum.map(fn {[l, r, w], idx} -> %{l: l, r: r, w: w, idx: idx} end)
      |> Enum.sort_by(& &1.r)

    m = length(sorted)
    ends = Enum.map(sorted, & &1.r)

    # Precompute prev array: largest index j (< i) with intervals[j].r < intervals[i].l
    prev_arr =
      :array.new(m + 1, 0)
      |> compute_prev(ends, sorted, 1)

    # Initialize DP arrays for t = 0..4
    dp_arrays =
      for _ <- 0..4 do
        :array.new(m + 1, {0, []})
      end

    # DP iteration over intervals
    final_dp =
      Enum.reduce(1..m, dp_arrays, fn i, dps ->
        interval = Enum.at(sorted, i - 1)
        prev_idx = :array.get(i, prev_arr)

        # Update dp[0] at position i (always zero weight)
        dp0 = :array.set(i, {0, []}, Enum.at(dps, 0))
        dps = List.replace_at(dps, 0, dp0)

        # Process t = 1..4
        Enum.reduce(1..4, dps, fn t, acc ->
          dp_t = Enum.at(acc, t)
          dp_prev = Enum.at(acc, t - 1)

          {prev_w, prev_l} = :array.get(prev_idx, dp_prev)
          cand_w = interval.w + prev_w
          cand_l = prev_l ++ [interval.idx]

          {cur_w, cur_l} = :array.get(i - 1, dp_t)

          better =
            if cand_w > cur_w do
              true
            else
              cand_w == cur_w and lex_less?(cand_l, cur_l)
            end

          new_tuple = if better, do: {cand_w, cand_l}, else: {cur_w, cur_l}
          dp_t_new = :array.set(i, new_tuple, dp_t)
          List.replace_at(acc, t, dp_t_new)
        end)
      end)

    # Choose best among t = 1..4 at position m
    {best_w, best_list} =
      Enum.reduce(1..4, {0, []}, fn t, {bw, bl} ->
        {w, l} = :array.get(m, Enum.at(final_dp, t))

        cond do
          w > bw -> {w, l}
          w == bw and lex_less?(l, bl) -> {w, l}
          true -> {bw, bl}
        end
      end)

    best_list
  end

  # Compute prev array recursively for each i
  defp compute_prev(prev_arr, ends, sorted, i) when i > length(sorted), do: prev_arr

  defp compute_prev(prev_arr, ends, sorted, i) do
    li = (Enum.at(sorted, i - 1)).l
    ans = binary_search(ends, li, 1, i - 1, 0)
    new_prev = :array.set(i, ans, prev_arr)
    compute_prev(new_prev, ends, sorted, i + 1)
  end

  # Binary search for largest index j with ends[j-1] < target
  defp binary_search(_ends, _target, lo, hi, ans) when lo > hi, do: ans

  defp binary_search(ends, target, lo, hi, ans) do
    mid = div(lo + hi, 2)

    if Enum.at(ends, mid - 1) < target do
      binary_search(ends, target, mid + 1, hi, mid)
    else
      binary_search(ends, target, lo, mid - 1, ans)
    end
  end

  # Lexicographic comparison of two lists of integers
  defp lex_less?(a, b) do
    case Enum.zip(a, b) |> Enum.find(fn {x, y} -> x != y end) do
      nil ->
        length(a) < length(b)

      {x, _y} when x < elem({x, _y}, 1) ->
        true

      _ ->
        false
    end
  end
end
```
