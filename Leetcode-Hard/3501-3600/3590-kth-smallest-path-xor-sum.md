# 3590. Kth Smallest Path XOR Sum

## Cpp

```cpp
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
using namespace std;
using namespace __gnu_pbds;

using ordered_set = tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update>;

class Solution {
public:
    vector<int> kthSmallest(vector<int>& par, vector<int>& vals, vector<vector<int>>& queries) {
        int n = par.size();
        vector<vector<int>> children(n);
        for (int i = 1; i < n; ++i) {
            children[par[i]].push_back(i);
        }
        // compute prefix xor
        vector<int> pref(n);
        function<void(int)> dfsPref = [&](int u){
            if (par[u] != -1) pref[u] = pref[par[u]] ^ vals[u];
            else pref[u] = vals[u];
            for (int v : children[u]) dfsPref(v);
        };
        dfsPref(0);
        
        // store queries per node
        vector<vector<pair<int,int>>> qAt(n);
        int m = queries.size();
        for (int i = 0; i < m; ++i) {
            int u = queries[i][0];
            int k = queries[i][1];
            qAt[u].push_back({k, i});
        }
        vector<int> ans(m, -1);
        
        function<ordered_set*(int)> dfs = [&](int u)->ordered_set*{
            ordered_set* cur = new ordered_set();
            cur->insert(pref[u]);
            for (int v : children[u]) {
                ordered_set* childSet = dfs(v);
                if (cur->size() < childSet->size()) swap(cur, childSet);
                for (int x : *childSet) cur->insert(x);
                delete childSet;
            }
            for (auto [k, idx] : qAt[u]) {
                if ((int)cur->size() >= k) ans[idx] = *cur->find_by_order(k-1);
                else ans[idx] = -1;
            }
            return cur;
        };
        
        ordered_set* rootSet = dfs(0);
        delete rootSet;
        return ans;
    }
};
```

## Java

```java
import java.util.*;
class Solution {
    static class Query {
        int k, idx;
        Query(int k, int idx) { this.k = k; this.idx = idx; }
    }
    static class Fenwick {
        int n;
        int[] bit;
        Fenwick(int n) { this.n = n; bit = new int[n + 2]; }
        void add(int i, int delta) {
            for (; i <= n; i += i & -i) bit[i] += delta;
        }
        int sum(int i) {
            int s = 0;
            for (; i > 0; i -= i & -i) s += bit[i];
            return s;
        }
        int total() { return sum(n); }
        // find smallest index such that prefix sum >= k (k is 1‑based)
        int kth(int k) {
            int idx = 0;
            int mask = Integer.highestOneBit(n);
            for (int d = mask; d != 0; d >>= 1) {
                int next = idx + d;
                if (next <= n && bit[next] < k) {
                    idx = next;
                    k -= bit[next];
                }
            }
            return idx + 1;
        }
    }

    int[] xorVal, start, end, euler, compIdx;
    List<Integer>[] tree;
    List<Query>[] qlist;
    int[] ans;
    Fenwick fenwick;
    int[] freq;
    int[] rev; // index -> original xor value

    public int[] kthSmallest(int[] par, int[] vals, int[][] queries) {
        int n = par.length;
        tree = new ArrayList[n];
        for (int i = 0; i < n; ++i) tree[i] = new ArrayList<>();
        for (int i = 1; i < n; ++i) tree[par[i]].add(i);

        xorVal = new int[n];
        xorVal[0] = vals[0];
        // preorder to compute xor values and order
        int[] order = new int[n];
        int ordPtr = 0;
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(0);
        while (!stack.isEmpty()) {
            int u = stack.pop();
            order[ordPtr++] = u;
            for (int v : tree[u]) {
                xorVal[v] = xorVal[u] ^ vals[v];
                stack.push(v);
            }
        }

        // subtree sizes and heavy child
        int[] sz = new int[n];
        int[] heavy = new int[n];
        Arrays.fill(heavy, -1);
        for (int i = n - 1; i >= 0; --i) {
            int u = order[i];
            sz[u] = 1;
            int maxSize = 0;
            for (int v : tree[u]) {
                sz[u] += sz[v];
                if (sz[v] > maxSize) {
                    maxSize = sz[v];
                    heavy[u] = v;
                }
            }
        }

        // euler tour
        start = new int[n];
        end = new int[n];
        euler = new int[n];
        int timer = 0;
        Deque<int[]> st = new ArrayDeque<>();
        st.push(new int[]{0, 0}); // node, next child index (0 means entry)
        while (!st.isEmpty()) {
            int[] cur = st.pop();
            int u = cur[0];
            int idx = cur[1];
            if (idx == 0) { // entry
                start[u] = timer;
                euler[timer++] = u;
            }
            if (idx < tree[u].size()) {
                int v = tree[u].get(idx);
                st.push(new int[]{u, idx + 1});
                st.push(new int[]{v, 0});
            } else {
                end[u] = timer - 1;
            }
        }

        // compress xor values
        int[] all = xorVal.clone();
        Arrays.sort(all);
        int m = 0;
        for (int i = 0; i < n; ++i) if (i == 0 || all[i] != all[i - 1]) all[m++] = all[i];
        rev = new int[m + 1];
        HashMap<Integer, Integer> map = new HashMap<>(m * 2);
        for (int i = 1; i <= m; ++i) {
            rev[i] = all[i - 1];
            map.put(rev[i], i);
        }
        compIdx = new int[n];
        for (int i = 0; i < n; ++i) compIdx[i] = map.get(xorVal[i]);

        // queries per node
        qlist = new ArrayList[n];
        ans = new int[queries.length];
        for (int i = 0; i < queries.length; ++i) {
            int u = queries[i][0];
            int k = queries[i][1];
            if (qlist[u] == null) qlist[u] = new ArrayList<>();
            qlist[u].add(new Query(k, i));
        }

        fenwick = new Fenwick(m);
        freq = new int[m + 2];

        dfs(0, true);

        return ans;
    }

    private void addNode(int u) {
        int id = compIdx[u];
        if (freq[id] == 0) fenwick.add(id, 1);
        freq[id]++;
    }

    private void removeNode(int u) {
        int id = compIdx[u];
        freq[id]--;
        if (freq[id] == 0) fenwick.add(id, -1);
    }

    private void addSubtree(int v) {
        for (int i = start[v]; i <= end[v]; ++i) addNode(euler[i]);
    }

    private void removeSubtree(int u) {
        for (int i = start[u]; i <= end[u]; ++i) removeNode(euler[i]);
    }

    private void dfs(int u, boolean keep) {
        // process light children
        for (int v : tree[u]) {
            if (v == heavyChild(u)) continue;
            dfs(v, false);
        }
        // heavy child
        int hc = heavyChild(u);
        if (hc != -1) dfs(hc, true);

        // merge light children's data
        for (int v : tree[u]) {
            if (v == hc) continue;
            addSubtree(v);
        }

        // add self
        addNode(u);

        // answer queries at u
        if (qlist[u] != null) {
            int total = fenwick.total();
            for (Query q : qlist[u]) {
                if (q.k > total) ans[q.idx] = -1;
                else {
                    int idx = fenwick.kth(q.k);
                    ans[q.idx] = rev[idx];
                }
            }
        }

        // clean up if not keep
        if (!keep) {
            removeSubtree(u);
        }
    }

    private int heavyChild(int u) {
        // heavy child stored in heavy array computed earlier
        // need access; store as field
        return heavy[u];
    }

    // fields needed for heavy array reference
    private int[] heavy;
}
```

## Python

```python
import math, sys

class Solution(object):
    def kthSmallest(self, par, vals, queries):
        """
        :type par: List[int]
        :type vals: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        sys.setrecursionlimit(1 << 25)
        n = len(vals)

        # build tree
        g = [[] for _ in range(n)]
        for i in range(1, n):
            p = par[i]
            g[p].append(i)

        tin = [0] * n
        tout = [0] * n
        order = [0] * n
        xor_path = [0] * n
        timer = 0

        def dfs(u, cur):
            nonlocal timer
            cur ^= vals[u]
            xor_path[u] = cur
            tin[u] = timer
            order[timer] = u
            timer += 1
            for v in g[u]:
                dfs(v, cur)
            tout[u] = timer - 1

        dfs(0, 0)

        arr = [xor_path[order[i]] for i in range(n)]

        # prepare queries as intervals
        qlist = []
        for idx, (u, k) in enumerate(queries):
            L = tin[u]
            R = tout[u]
            qlist.append((L, R, k, idx))

        block = int(math.sqrt(n)) + 1

        def mo_key(q):
            L, R = q[0], q[1]
            b = L // block
            return (b, R if b % 2 == 0 else -R)

        qlist.sort(key=mo_key)

        # value domain size (max possible xor)
        MAXV = 1 << 17          # 131072, covers all possible XORs (vals[i] <= 1e5)
        bucket_size = int(math.sqrt(MAXV)) + 1
        nbuckets = (MAXV + bucket_size - 1) // bucket_size

        cnt = [0] * MAXV
        bucket_cnt = [0] * nbuckets
        distinct = 0

        def add(pos):
            nonlocal distinct
            v = arr[pos]
            if cnt[v] == 0:
                distinct += 1
                bucket_cnt[v // bucket_size] += 1
            cnt[v] += 1

        def remove(pos):
            nonlocal distinct
            v = arr[pos]
            cnt[v] -= 1
            if cnt[v] == 0:
                distinct -= 1
                bucket_cnt[v // bucket_size] -= 1

        curL, curR = 0, -1
        ans = [-1] * len(queries)

        for L, R, k, idx in qlist:
            while curL > L:
                curL -= 1
                add(curL)
            while curR < R:
                curR += 1
                add(curR)
            while curL < L:
                remove(curL)
                curL += 1
            while curR > R:
                remove(curR)
                curR -= 1

            if k > distinct:
                ans[idx] = -1
                continue

            kk = k
            b = 0
            while kk > bucket_cnt[b]:
                kk -= bucket_cnt[b]
                b += 1
            start = b * bucket_size
            end = min(start + bucket_size, MAXV)
            for v in range(start, end):
                if cnt[v]:
                    kk -= 1
                    if kk == 0:
                        ans[idx] = v
                        break

        return ans
```

## Python3

```python
import sys
from typing import List

class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, idx, delta):
        while idx <= self.n:
            self.bit[idx] += delta
            idx += idx & -idx

    def sum(self, idx):
        s = 0
        while idx > 0:
            s += self.bit[idx]
            idx -= idx & -idx
        return s

    # find smallest index such that prefix sum >= k (1-indexed)
    def kth(self, k):
        idx = 0
        bitmask = 1 << (self.n.bit_length() - 1)
        while bitmask:
            nxt = idx + bitmask
            if nxt <= self.n and self.bit[nxt] < k:
                k -= self.bit[nxt]
                idx = nxt
            bitmask >>= 1
        return idx + 1

class Solution:
    def kthSmallest(self, par: List[int], vals: List[int], queries: List[List[int]]) -> List[int]:
        sys.setrecursionlimit(1000000)
        n = len(vals)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            p = par[i]
            children[p].append(i)

        path_xor = [0] * n
        sz = [0] * n
        heavy = [-1] * n
        tin = [0] * n
        tout = [0] * n
        order = [0] * n
        timer = 0

        def dfs1(u):
            nonlocal timer
            sz[u] = 1
            max_sz = 0
            tin[u] = timer
            order[timer] = u
            timer += 1
            for v in children[u]:
                path_xor[v] = path_xor[u] ^ vals[v]
                dfs1(v)
                sz[u] += sz[v]
                if sz[v] > max_sz:
                    max_sz = sz[v]
                    heavy[u] = v
            tout[u] = timer - 1

        path_xor[0] = vals[0]
        dfs1(0)

        # bucket queries per node
        q_per_node = [[] for _ in range(n)]
        for idx, (u, k) in enumerate(queries):
            q_per_node[u].append((k, idx))

        max_val = max(path_xor)
        size_bit = 1
        while size_bit <= max_val:
            size_bit <<= 1
        bit = BIT(size_bit + 2)   # extra space
        freq = [0] * (size_bit + 2)

        ans = [-1] * len(queries)

        def add_node(u):
            v = path_xor[u]
            if freq[v] == 0:
                bit.add(v + 1, 1)
            freq[v] += 1

        def remove_node(u):
            v = path_xor[u]
            freq[v] -= 1
            if freq[v] == 0:
                bit.add(v + 1, -1)

        def add_subtree(v):
            for i in range(tin[v], tout[v] + 1):
                add_node(order[i])

        def remove_subtree(u):
            for i in range(tin[u], tout[u] + 1):
                remove_node(order[i])

        def dfs2(u, keep):
            for v in children[u]:
                if v == heavy[u]:
                    continue
                dfs2(v, False)
            if heavy[u] != -1:
                dfs2(heavy[u], True)

            for v in children[u]:
                if v == heavy[u]:
                    continue
                add_subtree(v)

            add_node(u)

            # answer queries at u
            total = bit.sum(bit.n)
            for k, idx in q_per_node[u]:
                if k > total:
                    ans[idx] = -1
                else:
                    pos = bit.kth(k)  # 1-indexed position in BIT
                    ans[idx] = pos - 1

            if not keep:
                remove_subtree(u)

        dfs2(0, True)
        return ans
```

## C

```c
#include <stdlib.h>

typedef struct Treap {
    int key;
    unsigned pri;
    int sz;
    struct Treap *l, *r;
} Treap;

static unsigned rng_state = 2463534242u;
static inline unsigned rand_uint() {
    rng_state ^= rng_state << 13;
    rng_state ^= rng_state >> 17;
    rng_state ^= rng_state << 5;
    return rng_state;
}
static inline int treap_size(Treap *t) { return t ? t->sz : 0; }
static inline void upd(Treap *t) {
    if (t) t->sz = 1 + treap_size(t->l) + treap_size(t->r);
}
static Treap* new_node(int key) {
    Treap *n = (Treap*)malloc(sizeof(Treap));
    n->key = key;
    n->pri = rand_uint();
    n->sz = 1;
    n->l = n->r = NULL;
    return n;
}
static Treap* rotate_right(Treap *y) {
    Treap *x = y->l;
    y->l = x->r;
    x->r = y;
    upd(y);
    upd(x);
    return x;
}
static Treap* rotate_left(Treap *x) {
    Treap *y = x->r;
    x->r = y->l;
    y->l = x;
    upd(x);
    upd(y);
    return y;
}
static Treap* treap_insert(Treap *root, int key) {
    if (!root) return new_node(key);
    if (key == root->key) return root;               // already present
    if (key < root->key) {
        root->l = treap_insert(root->l, key);
        if (root->l->pri > root->pri) root = rotate_right(root);
    } else {
        root->r = treap_insert(root->r, key);
        if (root->r->pri > root->pri) root = rotate_left(root);
    }
    upd(root);
    return root;
}
static int treap_kth(Treap *root, int k) { // 1‑based
    while (root) {
        int left = treap_size(root->l);
        if (k == left + 1) return root->key;
        if (k <= left) root = root->l;
        else {
            k -= left + 1;
            root = root->r;
        }
    }
    return -1; // should not happen
}
static void merge_into(Treap *src, Treap **dest) {
    if (!src) return;
    *dest = treap_insert(*dest, src->key);
    merge_into(src->l, dest);
    merge_into(src->r, dest);
}

/* query linked list */
typedef struct QNode {
    int k;
    int idx;
    struct QNode *next;
} QNode;

/* global containers for DFS */
static int n;
static int *vals;
static int *head;
static int *to;
static int *nxtEdge;
static QNode **qHead;
static int *answers;

/* DFS returning treap of subtree */
static Treap* dfs(int u, int curXor) {
    Treap *root = NULL;
    root = treap_insert(root, curXor);
    for (int e = head[u]; e != -1; e = nxtEdge[e]) {
        int v = to[e];
        Treap *childRoot = dfs(v, curXor ^ vals[v]);
        if (treap_size(childRoot) > treap_size(root)) {
            Treap *tmp = root;
            root = childRoot;
            childRoot = tmp;
        }
        merge_into(childRoot, &root);
    }
    for (QNode *qn = qHead[u]; qn; qn = qn->next) {
        if (qn->k <= treap_size(root))
            answers[qn->idx] = treap_kth(root, qn->k);
        else
            answers[qn->idx] = -1;
    }
    return root;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* kthSmallest(int* par, int parSize, int* _vals, int valsSize,
                 int** queries, int queriesSize, int* queriesColSize,
                 int* returnSize) {
    n = valsSize;
    vals = _vals;

    /* build children adjacency list */
    head = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < n; ++i) head[i] = -1;
    to = (int*)malloc((n - 1) * sizeof(int));
    nxtEdge = (int*)malloc((n - 1) * sizeof(int));
    int ecnt = 0;
    for (int i = 1; i < n; ++i) {
        int p = par[i];
        to[ecnt] = i;
        nxtEdge[ecnt] = head[p];
        head[p] = ecnt;
        ++ecnt;
    }

    /* store queries per node */
    qHead = (QNode**)calloc(n, sizeof(QNode*));
    answers = (int*)malloc(queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; ++i) {
        int u = queries[i][0];
        int k = queries[i][1];
        QNode *node = (QNode*)malloc(sizeof(QNode));
        node->k = k;
        node->idx = i;
        node->next = qHead[u];
        qHead[u] = node;
    }

    /* run DFS from root (0) */
    dfs(0, vals[0]);

    *returnSize = queriesSize;

    /* free auxiliary structures (optional for LeetCode) */
    free(head);
    free(to);
    free(nxtEdge);
    for (int i = 0; i < n; ++i) {
        QNode *cur = qHead[i];
        while (cur) {
            QNode *tmp = cur;
            cur = cur->next;
            free(tmp);
        }
    }
    free(qHead);

    return answers;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private int n;
    private List<int>[] graph;
    private int[] vals;
    private int[] xorFromRoot;
    private int[] sz;
    private int[] heavy;
    private int[] tin, tout, euler;
    private int timer;
    private const int MAXBIT = 1 << 17; // 131072, enough for values up to 100000
    private int[] cnt = new int[MAXBIT];
    private BIT bit = new BIT(MAXBIT + 2);
    private int distinctCount = 0;

    private List<(int k, int idx)>[] queriesByNode;
    private int[] answers;

    public int[] KthSmallest(int[] par, int[] valsInput, int[][] queries) {
        n = par.Length;
        vals = valsInput;
        graph = new List<int>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<int>();
        for (int i = 1; i < n; i++) {
            int p = par[i];
            graph[p].Add(i);
        }

        xorFromRoot = new int[n];
        sz = new int[n];
        heavy = new int[n];
        Array.Fill(heavy, -1);
        tin = new int[n];
        tout = new int[n];
        euler = new int[n];
        timer = 0;

        // first dfs: compute xorFromRoot, sizes, heavy child, euler order
        DfsInit(0, 0);

        // organize queries per node
        queriesByNode = new List<(int k, int idx)>[n];
        for (int i = 0; i < n; i++) queriesByNode[i] = new List<(int k, int idx)>();
        answers = new int[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            int u = queries[i][0];
            int k = queries[i][1];
            queriesByNode[u].Add((k, i));
        }

        // DSU on tree
        DfsDSU(0, true);

        return answers;
    }

    private void DfsInit(int v, int curXor) {
        xorFromRoot[v] = curXor ^ vals[v];
        tin[v] = timer;
        euler[timer++] = v;
        sz[v] = 1;
        int maxSize = -1;
        foreach (int to in graph[v]) {
            DfsInit(to, xorFromRoot[v]);
            sz[v] += sz[to];
            if (sz[to] > maxSize) {
                maxSize = sz[to];
                heavy[v] = to;
            }
        }
        tout[v] = timer - 1;
    }

    private void AddNode(int v) {
        int x = xorFromRoot[v];
        if (++cnt[x] == 1) {
            bit.Add(x + 1, 1);
            distinctCount++;
        }
    }

    private void RemoveNode(int v) {
        int x = xorFromRoot[v];
        if (--cnt[x] == 0) {
            bit.Add(x + 1, -1);
            distinctCount--;
        }
    }

    private void AddSubtree(int v) {
        for (int i = tin[v]; i <= tout[v]; i++) {
            AddNode(euler[i]);
        }
    }

    private void RemoveSubtree(int v) {
        for (int i = tin[v]; i <= tout[v]; i++) {
            RemoveNode(euler[i]);
        }
    }

    private void DfsDSU(int v, bool keep) {
        // process light children
        foreach (int to in graph[v]) {
            if (to == heavy[v]) continue;
            DfsDSU(to, false);
        }
        // heavy child
        if (heavy[v] != -1) {
            DfsDSU(heavy[v], true);
        }

        // add light children's contributions
        foreach (int to in graph[v]) {
            if (to == heavy[v]) continue;
            AddSubtree(to);
        }

        // add current node
        AddNode(v);

        // answer queries for v
        foreach (var (k, idx) in queriesByNode[v]) {
            if (distinctCount < k) {
                answers[idx] = -1;
            } else {
                int val = bit.FindKth(k);
                answers[idx] = val - 1; // remove offset
            }
        }

        if (!keep) {
            RemoveSubtree(v);
        }
    }

    private class BIT {
        private int[] tree;
        private int size;

        public BIT(int n) {
            size = n;
            tree = new int[n];
        }

        public void Add(int idx, int delta) {
            for (int i = idx; i < size; i += i & -i) {
                tree[i] += delta;
            }
        }

        // find smallest index such that prefix sum >= k (1-indexed)
        public int FindKth(int k) {
            int idx = 0;
            int bitMask = 1;
            while (bitMask < size) bitMask <<= 1;
            for (int step = bitMask; step > 0; step >>= 1) {
                int next = idx + step;
                if (next < size && tree[next] < k) {
                    idx = next;
                    k -= tree[next];
                }
            }
            return idx + 1;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} par
 * @param {number[]} vals
 * @param {number[][]} queries
 * @return {number[]}
 */
var kthSmallest = function(par, vals, queries) {
    const n = vals.length;
    const children = Array.from({length: n}, () => []);
    for (let i = 1; i < n; ++i) {
        children[par[i]].push(i);
    }

    // constants
    const MAXV = 1 << 17; // 131072, enough for all possible XOR values

    // Fenwick Tree for order statistics on distinct values
    class BIT {
        constructor(size) {
            this.n = size;
            this.bit = new Int32Array(size + 2);
        }
        add(idx, delta) {
            for (let i = idx; i <= this.n; i += i & -i) {
                this.bit[i] += delta;
            }
        }
        // find smallest index such that prefix sum >= k (k is 1‑based)
        kth(k) {
            let idx = 0;
            // highest power of two >= n
            let bitMask = 1 << 17; // since MAXV <= 2^17
            while (bitMask !== 0) {
                const next = idx + bitMask;
                if (next <= this.n && this.bit[next] < k) {
                    idx = next;
                    k -= this.bit[next];
                }
                bitMask >>= 1;
            }
            return idx + 1; // 1‑based index
        }
    }

    const bit = new BIT(MAXV + 2);
    const cnt = new Int32Array(MAXV + 2);
    let distinctCount = 0;

    function addValue(v) {
        if (cnt[v] === 0) {
            bit.add(v + 1, 1);
            ++distinctCount;
        }
        ++cnt[v];
    }
    function removeValue(v) {
        --cnt[v];
        if (cnt[v] === 0) {
            bit.add(v + 1, -1);
            --distinctCount;
        }
    }

    // arrays for DFS
    const size = new Int32Array(n);
    const heavy = new Int32Array(n).fill(-1);
    const tin = new Int32Array(n);
    const tout = new Int32Array(n);
    const euler = new Int32Array(n);
    const pathXor = new Int32Array(n);

    let timer = 0;
    // first DFS: sizes, heavy child, euler order, path xor
    function dfs1(u) {
        size[u] = 1;
        tin[u] = timer;
        euler[timer++] = u;

        for (const v of children[u]) {
            pathXor[v] = pathXor[u] ^ vals[v];
            dfs1(v);
            if (heavy[u] === -1 || size[v] > size[heavy[u]]) heavy[u] = v;
            size[u] += size[v];
        }
        tout[u] = timer - 1;
    }

    pathXor[0] = vals[0];
    dfs1(0);

    // organize queries per node
    const qByNode = Array.from({length: n}, () => []);
    for (let i = 0; i < queries.length; ++i) {
        const [u, k] = queries[i];
        qByNode[u].push([k, i]);
    }
    const ans = new Int32Array(queries.length).fill(-1);

    // helper to add whole subtree using euler range
    function addSubtree(v) {
        for (let t = tin[v]; t <= tout[v]; ++t) {
            addValue(pathXor[euler[t]]);
        }
    }
    function removeSubtree(v) {
        for (let t = tin[v]; t <= tout[v]; ++t) {
            removeValue(pathXor[euler[t]]);
        }
    }

    // second DFS: DSU on tree
    function dfs2(u, keep) {
        // process light children
        for (const v of children[u]) {
            if (v === heavy[u]) continue;
            dfs2(v, false);
        }
        // heavy child
        if (heavy[u] !== -1) {
            dfs2(heavy[u], true);
        }

        // merge light children's data into current set
        for (const v of children[u]) {
            if (v === heavy[u]) continue;
            addSubtree(v);
        }
        // add self
        addValue(pathXor[u]);

        // answer queries at u
        for (const [k, idx] of qByNode[u]) {
            if (distinctCount < k) {
                ans[idx] = -1;
            } else {
                const valIdx = bit.kth(k); // 1‑based index in BIT
                ans[idx] = valIdx - 1; // convert back to value
            }
        }

        // clean up if not keeping
        if (!keep) {
            removeSubtree(u);
        }
    }

    dfs2(0, true);

    return Array.from(ans);
};
```

## Typescript

```typescript
function kthSmallest(par: number[], vals: number[], queries: number[][]): number[] {
    const n = par.length;
    const children: number[][] = Array.from({ length: n }, () => []);
    for (let i = 1; i < n; i++) {
        children[par[i]].push(i);
    }

    const xorArr = new Uint32Array(n);
    const sz = new Uint32Array(n);
    const heavy = new Int32Array(n).fill(-1);
    const tin = new Uint32Array(n);
    const tout = new Uint32Array(n);
    const euler: number[] = new Array(n);
    let timer = 0;

    function dfs1(u: number): void {
        tin[u] = timer;
        euler[timer] = u;
        timer++;
        sz[u] = 1;
        for (const v of children[u]) {
            xorArr[v] = xorArr[u] ^ vals[v];
            dfs1(v);
            if (heavy[u] === -1 || sz[v] > sz[heavy[u]]) heavy[u] = v;
            sz[u] += sz[v];
        }
        tout[u] = timer - 1;
    }

    xorArr[0] = vals[0];
    dfs1(0);

    const qPerNode: number[][] = Array.from({ length: n }, () => []);
    for (let i = 0; i < queries.length; i++) {
        const u = queries[i][0];
        qPerNode[u].push(i);
    }

    const MAXV = 1 << 17; // 131072, enough for xor values up to 2^17-1
    const cnt = new Uint32Array(MAXV);

    class BIT {
        n: number;
        tree: Int32Array;
        constructor(n: number) {
            this.n = n;
            this.tree = new Int32Array(n + 2);
        }
        add(i: number, delta: number): void {
            for (let x = i; x <= this.n; x += x & -x) this.tree[x] += delta;
        }
        sum(i: number): number {
            let s = 0;
            for (let x = i; x > 0; x -= x & -x) s += this.tree[x];
            return s;
        }
        kth(k: number): number { // returns BIT index (1‑based)
            if (k <= 0) return -1;
            let idx = 0;
            let bit = 1 << 18; // power of two > n
            while (bit) {
                const next = idx + bit;
                if (next <= this.n && this.tree[next] < k) {
                    k -= this.tree[next];
                    idx = next;
                }
                bit >>= 1;
            }
            return idx + 1; // 1‑based index where prefix sum >= original k
        }
    }

    const bit = new BIT(MAXV);

    function addValue(val: number, delta: number): void {
        const old = cnt[val];
        cnt[val] = old + delta;
        if (old === 0 && cnt[val] > 0) {
            bit.add(val + 1, 1);
        } else if (old > 0 && cnt[val] === 0) {
            bit.add(val + 1, -1);
        }
    }

    function addSubtree(v: number, delta: number): void {
        for (let i = tin[v]; i <= tout[v]; i++) {
            const node = euler[i];
            addValue(xorArr[node], delta);
        }
    }

    const ans: number[] = new Array(queries.length).fill(-1);

    function dfs2(u: number, keep: boolean): void {
        for (const v of children[u]) {
            if (v === heavy[u]) continue;
            dfs2(v, false);
        }
        if (heavy[u] !== -1) dfs2(heavy[u], true);
        for (const v of children[u]) {
            if (v === heavy[u]) continue;
            addSubtree(v, 1);
        }
        addValue(xorArr[u], 1);

        const totalDistinct = bit.sum(MAXV);
        for (const qi of qPerNode[u]) {
            const k = queries[qi][1];
            if (totalDistinct < k) {
                ans[qi] = -1;
            } else {
                const pos = bit.kth(k); // BIT index (1‑based)
                ans[qi] = pos - 1;      // actual xor value
            }
        }

        if (!keep) addSubtree(u, -1);
    }

    dfs2(0, true);
    return ans;
}
```

## Php

```php
class TreapNode {
    public int $key;
    public int $prio;
    public ?TreapNode $left = null;
    public ?TreapNode $right = null;
    public int $size = 1;

    public function __construct(int $key) {
        $this->key = $key;
        $this->prio = mt_rand();
    }
}

class Solution {

    /**
     * @param Integer[] $par
     * @param Integer[] $vals
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function kthSmallest($par, $vals, $queries) {
        $n = count($vals);
        // build children list
        $children = array_fill(0, $n, []);
        for ($i = 1; $i < $n; $i++) {
            $p = $par[$i];
            $children[$p][] = $i;
        }

        // group queries by node
        $queriesByNode = array_fill(0, $n, []);
        foreach ($queries as $idx => $q) {
            $u = $q[0];
            $k = $q[1];
            $queriesByNode[$u][] = [$k, $idx];
        }

        $answers = array_fill(0, count($queries), -1);
        $pathXor = array_fill(0, $n, 0);

        // iterative DFS to compute path XORs and obtain processing order
        $stack = [[0, 0]];
        $order = [];
        while ($stack) {
            [$u, $xor] = array_pop($stack);
            $curXor = $xor ^ $vals[$u];
            $pathXor[$u] = $curXor;
            $order[] = $u; // preorder
            foreach ($children[$u] as $v) {
                $stack[] = [$v, $curXor];
            }
        }

        // set root for each node's treap
        $setRoot = array_fill(0, $n, null);

        // process nodes in postorder (reverse preorder)
        foreach (array_reverse($order) as $u) {
            $big = null;
            foreach ($children[$u] as $v) {
                $childSet = $setRoot[$v];
                if ($big === null) {
                    $big = $childSet;
                } else {
                    if ($childSet !== null && $childSet->size > $big->size) {
                        $tmp = $big;
                        $big = $childSet;
                        $big = $this->mergeSets($big, $tmp);
                    } else {
                        $big = $this->mergeSets($big, $childSet);
                    }
                }
            }
            // insert own xor value
            $big = $this->treapInsertIfNotExists($big, $pathXor[$u]);

            // answer queries for this node
            foreach ($queriesByNode[$u] as $q) {
                [$k, $idx] = $q;
                if ($big !== null && $big->size >= $k) {
                    $answers[$idx] = $this->treapKth($big, $k);
                } else {
                    $answers[$idx] = -1;
                }
            }

            $setRoot[$u] = $big;
        }

        return $answers;
    }

    private function updateSize(?TreapNode $node): void {
        if ($node === null) return;
        $l = $node->left ? $node->left->size : 0;
        $r = $node->right ? $node->right->size : 0;
        $node->size = $l + $r + 1;
    }

    private function split(?TreapNode $root, int $key): array {
        if ($root === null) return [null, null];
        if ($key < $root->key) {
            [$l, $r] = $this->split($root->left, $key);
            $root->left = $r;
            $this->updateSize($root);
            return [$l, $root];
        } else {
            [$l, $r] = $this->split($root->right, $key);
            $root->right = $l;
            $this->updateSize($root);
            return [$root, $r];
        }
    }

    private function insertNode(?TreapNode $root, TreapNode $node): ?TreapNode {
        if ($root === null) return $node;
        if ($node->prio > $root->prio) {
            [$l, $r] = $this->split($root, $node->key);
            $node->left = $l;
            $node->right = $r;
            $this->updateSize($node);
            return $node;
        } elseif ($node->key < $root->key) {
            $root->left = $this->insertNode($root->left, $node);
            $this->updateSize($root);
            return $root;
        } elseif ($node->key > $root->key) {
            $root->right = $this->insertNode($root->right, $node);
            $this->updateSize($root);
            return $root;
        } else {
            // duplicate key, discard new node
            return $root;
        }
    }

    private function treapInsertIfNotExists(?TreapNode $root, int $key): ?TreapNode {
        $node = new TreapNode($key);
        return $this->insertNode($root, $node);
    }

    private function treapKth(?TreapNode $root, int $k): ?int {
        if ($root === null) return null;
        $leftSize = $root->left ? $root->left->size : 0;
        if ($k == $leftSize + 1) {
            return $root->key;
        } elseif ($k <= $leftSize) {
            return $this->treapKth($root->left, $k);
        } else {
            return $this->treapKth($root->right, $k - $leftSize - 1);
        }
    }

    private function mergeSets(?TreapNode $big, ?TreapNode $small): ?TreapNode {
        if ($small === null) return $big;
        // inorder traversal of small set
        $stack = [];
        $node = $small;
        while ($node !== null || $stack) {
            while ($node !== null) {
                $stack[] = $node;
                $node = $node->left;
            }
            $node = array_pop($stack);
            $big = $this->treapInsertIfNotExists($big, $node->key);
            $node = $node->right;
        }
        return $big;
    }
}
```

## Swift

```swift
class Solution {
    private class TrieNode {
        var child: [Int] = [-1, -1]
        var cnt: Int = 0
    }
    
    private class XorSet {
        static let MAXBIT = 20   // enough for values up to 2^20
        
        var values: Set<Int>
        var nodes: [TrieNode]
        let root = 0
        
        init() {
            self.values = Set<Int>()
            self.nodes = [TrieNode()]   // root node
        }
        
        func insert(_ x: Int) {
            if values.contains(x) { return }
            values.insert(x)
            var node = root
            for b in stride(from: XorSet.MAXBIT - 1, through: 0, by: -1) {
                let bit = (x >> b) & 1
                if nodes[node].child[bit] == -1 {
                    nodes.append(TrieNode())
                    nodes[node].child[bit] = nodes.count - 1
                }
                node = nodes[node].child[bit]
                nodes[node].cnt += 1
            }
        }
        
        func kth(_ k: Int) -> Int? {
            if values.count < k { return nil }
            var node = root
            var ans = 0
            var kk = k
            for b in stride(from: XorSet.MAXBIT - 1, through: 0, by: -1) {
                let leftIdx = nodes[node].child[0]
                let leftCnt = (leftIdx == -1) ? 0 : nodes[leftIdx].cnt
                if kk <= leftCnt {
                    node = leftIdx
                } else {
                    kk -= leftCnt
                    ans |= (1 << b)
                    let rightIdx = nodes[node].child[1]
                    node = rightIdx   // guaranteed to exist
                }
            }
            return ans
        }
    }
    
    private var children: [[Int]] = []
    private var pathXor: [Int] = []
    private var queriesAtNode: [[(k: Int, idx: Int)]] = []
    private var answers: [Int] = []
    
    func kthSmallest(_ par: [Int], _ vals: [Int], _ queries: [[Int]]) -> [Int] {
        let n = par.count
        children = Array(repeating: [], count: n)
        if n > 1 {
            for i in 1..<n {
                let p = par[i]
                children[p].append(i)
            }
        }
        pathXor = Array(repeating: 0, count: n)
        dfsPath(0, 0, vals)
        
        queriesAtNode = Array(repeating: [], count: n)
        answers = Array(repeating: -1, count: queries.count)
        for (idx, q) in queries.enumerated() {
            let u = q[0]
            let k = q[1]
            queriesAtNode[u].append((k: k, idx: idx))
        }
        
        _ = dfs(0)
        return answers
    }
    
    private func dfsPath(_ u: Int, _ curXor: Int, _ vals: [Int]) {
        let newXor = curXor ^ vals[u]
        pathXor[u] = newXor
        for v in children[u] {
            dfsPath(v, newXor, vals)
        }
    }
    
    private func dfs(_ u: Int) -> XorSet {
        var childSets: [XorSet] = []
        for v in children[u] {
            let setV = dfs(v)
            childSets.append(setV)
        }
        
        var bigSet: XorSet
        if childSets.isEmpty {
            bigSet = XorSet()
        } else {
            var maxIdx = 0
            for i in 1..<childSets.count {
                if childSets[i].values.count > childSets[maxIdx].values.count {
                    maxIdx = i
                }
            }
            bigSet = childSets[maxIdx]
            for i in 0..<childSets.count where i != maxIdx {
                let small = childSets[i]
                for val in small.values {
                    bigSet.insert(val)
                }
            }
        }
        
        // insert current node's path xor
        bigSet.insert(pathXor[u])
        
        // answer queries at this node
        for q in queriesAtNode[u] {
            if let ans = bigSet.kth(q.k) {
                answers[q.idx] = ans
            } else {
                answers[q.idx] = -1
            }
        }
        return bigSet
    }
}
```

## Kotlin

```kotlin
import java.util.Random
import kotlin.math.max

class Solution {
    private lateinit var xorTo: IntArray
    private lateinit var children: Array<MutableList<Int>>
    private lateinit var queryByNode: Array<MutableList<Int>>
    private lateinit var queries: Array<IntArray>
    private lateinit var answer: IntArray

    fun kthSmallest(par: IntArray, vals: IntArray, queriesInput: Array<IntArray>): IntArray {
        val n = vals.size
        this.queries = queriesInput
        answer = IntArray(queriesInput.size)

        // build tree
        children = Array(n) { mutableListOf() }
        for (i in 1 until n) {
            val p = par[i]
            children[p].add(i)
        }

        // compute xor from root to each node
        xorTo = IntArray(n)
        val stack = java.util.ArrayDeque<Int>()
        stack.add(0)
        while (!stack.isEmpty()) {
            val u = stack.removeLast()
            for (v in children[u]) {
                xorTo[v] = xorTo[u] xor vals[v]
                stack.add(v)
            }
        }

        // group queries by node
        queryByNode = Array(n) { mutableListOf() }
        for (i in queriesInput.indices) {
            val u = queriesInput[i][0]
            queryByNode[u].add(i)
        }

        dfs(0)

        return answer
    }

    private fun dfs(u: Int): XorSet {
        var cur = XorSet()
        cur.add(xorTo[u])
        for (v in children[u]) {
            var childSet = dfs(v)
            if (cur.size() < childSet.size()) {
                val tmp = cur
                cur = childSet
                childSet = tmp
            }
            cur.merge(childSet)
        }
        for (qid in queryByNode[u]) {
            val k = queries[qid][1]
            answer[qid] = cur.kth(k)
        }
        return cur
    }

    // ---------- XorSet ----------
    private class XorSet {
        private var root: TreapNode? = null
        private val elems = IntList()
        private val rand = Random()

        fun size(): Int = root?.sz ?: 0

        fun add(x: Int) {
            if (!contains(x)) {
                root = insert(root, x, rand.nextInt())
                elems.add(x)
            }
        }

        private fun contains(key: Int): Boolean {
            var cur = root
            while (cur != null) {
                when {
                    key == cur.key -> return true
                    key < cur.key -> cur = cur.left
                    else -> cur = cur.right
                }
            }
            return false
        }

        fun merge(other: XorSet) {
            for (i in 0 until other.elems.size) {
                add(other.elems[i])
            }
        }

        fun kth(k: Int): Int {
            val sz = size()
            if (k > sz) return -1
            var cur = root!!
            var kk = k
            while (true) {
                val leftSize = cur.left?.sz ?: 0
                when {
                    kk == leftSize + 1 -> return cur.key
                    kk <= leftSize -> cur = cur.left!!
                    else -> {
                        kk -= leftSize + 1
                        cur = cur.right!!
                    }
                }
            }
        }

        // treap operations
        private fun insert(node: TreapNode?, key: Int, priority: Int): TreapNode? {
            if (node == null) return TreapNode(key, priority)
            if (key == node.key) return node
            if (key < node.key) {
                node.left = insert(node.left, key, priority)
                if ((node.left?.priority ?: Int.MIN_VALUE) > node.priority) {
                    return rotateRight(node)
                }
            } else {
                node.right = insert(node.right, key, priority)
                if ((node.right?.priority ?: Int.MIN_VALUE) > node.priority) {
                    return rotateLeft(node)
                }
            }
            update(node)
            return node
        }

        private fun rotateRight(y: TreapNode): TreapNode {
            val x = y.left!!
            y.left = x.right
            x.right = y
            update(y)
            update(x)
            return x
        }

        private fun rotateLeft(x: TreapNode): TreapNode {
            val y = x.right!!
            x.right = y.left
            y.left = x
            update(x)
            update(y)
            return y
        }

        private fun update(node: TreapNode) {
            node.sz = 1 + (node.left?.sz ?: 0) + (node.right?.sz ?: 0)
        }
    }

    // ---------- Treap Node ----------
    private class TreapNode(val key: Int, var priority: Int) {
        var left: TreapNode? = null
        var right: TreapNode? = null
        var sz: Int = 1
    }

    // ---------- Simple int list ----------
    private class IntList(initialCap: Int = 8) {
        private var arr = IntArray(initialCap)
        var size = 0
            private set

        fun add(v: Int) {
            if (size == arr.size) {
                arr = arr.copyOf(arr.size shl 1)
            }
            arr[size++] = v
        }

        operator fun get(idx: Int): Int = arr[idx]
    }
}
```

## Dart

```dart
import 'dart:math';

class Fenwick {
  final List<int> _bit;
  final int n;
  Fenwick(this.n) : _bit = List.filled(n + 2, 0);

  void add(int idx, int delta) {
    for (int i = idx; i <= n; i += i & -i) {
      _bit[i] += delta;
    }
  }

  int sum(int idx) {
    int res = 0;
    for (int i = idx; i > 0; i -= i & -i) {
      res += _bit[i];
    }
    return res;
  }

  // returns smallest index such that prefix sum >= k (1‑based)
  int kth(int k) {
    int idx = 0;
    int mask = 1;
    while ((mask << 1) <= n) mask <<= 1;
    for (int d = mask; d > 0; d >>= 1) {
      int next = idx + d;
      if (next <= n && _bit[next] < k) {
        idx = next;
        k -= _bit[next];
      }
    }
    return idx + 1;
  }
}

class Solution {
  List<int> kthSmallest(List<int> par, List<int> vals, List<List<int>> queries) {
    final int n = vals.length;
    // build tree
    final List<List<int>> g = List.generate(n, (_) => []);
    for (int i = 1; i < n; ++i) {
      g[par[i]].add(i);
    }

    // path xor from root to each node
    final List<int> pathXor = List.filled(n, 0);
    void dfsPath(int u, int cur) {
      int now = cur ^ vals[u];
      pathXor[u] = now;
      for (int v in g[u]) {
        dfsPath(v, now);
      }
    }

    dfsPath(0, 0);

    // queries per node: each entry is [k, queryIndex]
    final List<List<List<int>>> qAt = List.generate(n, (_) => []);
    for (int i = 0; i < queries.length; ++i) {
      int u = queries[i][0];
      int k = queries[i][1];
      qAt[u].add([k, i]);
    }

    // subtree sizes and heavy child
    final List<int> sz = List.filled(n, 0);
    final List<int> heavy = List.filled(n, -1);
    final List<int> start = List.filled(n, 0);
    final List<int> endIdx = List.filled(n, 0);
    final List<int> euler = List.filled(n, 0);
    int timer = 0;

    void dfsSize(int u) {
      sz[u] = 1;
      start[u] = timer;
      euler[timer] = u;
      timer++;
      int maxSub = 0;
      for (int v in g[u]) {
        dfsSize(v);
        sz[u] += sz[v];
        if (sz[v] > maxSub) {
          maxSub = sz[v];
          heavy[u] = v;
        }
      }
      endIdx[u] = timer - 1;
    }

    dfsSize(0);

    // determine value range for BIT
    int maxVal = 0;
    for (int v in pathXor) if (v > maxVal) maxVal = v;
    final Fenwick fenwick = Fenwick(maxVal + 2);
    final List<int> cnt = List.filled(maxVal + 1, 0);
    int distinctCount = 0;

    void addNode(int u) {
      int val = pathXor[u];
      if (cnt[val] == 0) {
        fenwick.add(val + 1, 1);
        distinctCount++;
      }
      cnt[val]++;
    }

    void removeNode(int u) {
      int val = pathXor[u];
      cnt[val]--;
      if (cnt[val] == 0) {
        fenwick.add(val + 1, -1);
        distinctCount--;
      }
    }

    final List<int> ans = List.filled(queries.length, -1);

    void dfs(int u, bool keep) {
      // process light children
      for (int v in g[u]) {
        if (v == heavy[u]) continue;
        dfs(v, false);
      }
      // heavy child
      if (heavy[u] != -1) {
        dfs(heavy[u], true);
      }

      // add contributions of light subtrees
      for (int v in g[u]) {
        if (v == heavy[u]) continue;
        for (int i = start[v]; i <= endIdx[v]; ++i) {
          addNode(euler[i]);
        }
      }
      // add self
      addNode(u);

      // answer queries at u
      for (var qq in qAt[u]) {
        int k = qq[0];
        int idx = qq[1];
        if (distinctCount < k) {
          ans[idx] = -1;
        } else {
          int pos = fenwick.kth(k); // 1‑based index of value+1
          ans[idx] = pos - 1;
        }
      }

      if (!keep) {
        for (int i = start[u]; i <= endIdx[u]; ++i) {
          removeNode(euler[i]);
        }
      }
    }

    dfs(0, true);
    return ans;
  }
}
```

## Golang

```go
package main

import (
	"math/rand"
	"time"
)

type treap struct {
	key        int
	priority   uint32
	left, right *treap
	size       int
}

func sz(t *treap) int {
	if t == nil {
		return 0
	}
	return t.size
}

func upd(t *treap) {
	if t != nil {
		t.size = 1 + sz(t.left) + sz(t.right)
	}
}

func rotateRight(p *treap) *treap {
	q := p.left
	p.left = q.right
	q.right = p
	upd(p)
	upd(q)
	return q
}

func rotateLeft(p *treap) *treap {
	q := p.right
	p.right = q.left
	q.left = p
	upd(p)
	upd(q)
	return q
}

func insert(t *treap, key int) *treap {
	if t == nil {
		return &treap{key: key, priority: rand.Uint32(), size: 1}
	}
	if key == t.key {
		return t
	}
	if key < t.key {
		t.left = insert(t.left, key)
		if t.left.priority < t.priority {
			t = rotateRight(t)
		}
	} else {
		t.right = insert(t.right, key)
		if t.right.priority < t.priority {
			t = rotateLeft(t)
		}
	}
	upd(t)
	return t
}

func kth(t *treap, k int) int {
	leftSize := sz(t.left)
	if k <= leftSize {
		return kth(t.left, k)
	}
	if k == leftSize+1 {
		return t.key
	}
	return kth(t.right, k-leftSize-1)
}

// merge all keys from src into *dst (small into large)
func mergeSmallIntoLarge(src *treap, dst **treap) {
	if src == nil {
		return
	}
	mergeSmallIntoLarge(src.left, dst)
	*dst = insert(*dst, src.key)
	mergeSmallIntoLarge(src.right, dst)
}

type query struct {
	k   int
	idx int
}

func kthSmallest(par []int, vals []int, queries [][]int) []int {
	n := len(par)

	children := make([][]int, n)
	for i := 1; i < n; i++ {
		p := par[i]
		children[p] = append(children[p], i)
	}

	pathXor := make([]int, n)
	var dfsPath func(u int, cur int)
	dfsPath = func(u int, cur int) {
		cur ^= vals[u]
		pathXor[u] = cur
		for _, v := range children[u] {
			dfsPath(v, cur)
		}
	}
	dfsPath(0, 0)

	qByNode := make([][]query, n)
	ans := make([]int, len(queries))
	for i, q := range queries {
		u, k := q[0], q[1]
		qByNode[u] = append(qByNode[u], query{k: k, idx: i})
	}

	var dfsSet func(u int) *treap
	dfsSet = func(u int) *treap {
		var curSet *treap
		curSet = insert(curSet, pathXor[u])
		for _, v := range children[u] {
			childSet := dfsSet(v)
			if sz(childSet) > sz(curSet) {
				curSet, childSet = childSet, curSet
			}
			mergeSmallIntoLarge(childSet, &curSet)
		}
		for _, q := range qByNode[u] {
			if sz(curSet) < q.k {
				ans[q.idx] = -1
			} else {
				ans[q.idx] = kth(curSet, q.k)
			}
		}
		return curSet
	}

	rand.Seed(time.Now().UnixNano())
	dfsSet(0)

	return ans
}
```

## Ruby

```ruby
def kth_smallest(par, vals, queries)
  n = par.length
  # build children adjacency list
  children = Array.new(n) { [] }
  (1...n).each do |i|
    p = par[i]
    children[p] << i
  end

  # compute path xor for each node
  path_xor = Array.new(n, 0)
  path_xor[0] = vals[0]
  stack = [0]
  while (u = stack.pop)
    children[u].each do |v|
      path_xor[v] = path_xor[u] ^ vals[v]
      stack << v
    end
  end

  # subtree sizes and heavy child
  size = Array.new(n, 1)
  heavy = Array.new(n, -1)
  order = []
  stack = [0]
  while (u = stack.pop)
    order << u
    children[u].each { |v| stack << v }
  end
  order.reverse_each do |u|
    max_sz = 0
    children[u].each do |v|
      size[u] += size[v]
      if size[v] > max_sz
        max_sz = size[v]
        heavy[u] = v
      end
    end
  end

  # group queries by node
  q_by_node = Array.new(n) { [] }
  queries.each_with_index do |(u, k), idx|
    q_by_node[u] << [k, idx]
  end
  ans = Array.new(queries.length)

  max_val = path_xor.max || 0
  bit_size = max_val + 2

  class BIT
    def initialize(n)
      @n = n
      @tree = Array.new(n + 2, 0)
    end
    def add(i, delta)
      while i <= @n
        @tree[i] += delta
        i += i & -i
      end
    end
    def sum(i)
      s = 0
      while i > 0
        s += @tree[i]
        i -= i & -i
      end
      s
    end
    def total
      sum(@n)
    end
    def kth(k)
      idx = 0
      bitmask = 1 << (Math.log2(@n).floor)
      while bitmask > 0
        t = idx + bitmask
        if t <= @n && @tree[t] < k
          idx = t
          k -= @tree[t]
        end
        bitmask >>= 1
      end
      idx
    end
  end

  cnt = Array.new(max_val + 1, 0)
  bit = BIT.new(bit_size)

  bucket = Array.new(n) { [] }

  order.reverse_each do |u|
    cur_bucket = heavy[u] != -1 ? bucket[heavy[u]] : []
    # merge light children
    children[u].each do |v|
      next if v == heavy[u]
      bucket[v].each do |val|
        if cnt[val] == 0
          bit.add(val + 1, 1)
        end
        cnt[val] += 1
        cur_bucket << val
      end
    end
    # add own value
    x = path_xor[u]
    if cnt[x] == 0
      bit.add(x + 1, 1)
    end
    cnt[x] += 1
    cur_bucket << x

    bucket[u] = cur_bucket

    unless q_by_node[u].empty?
      total = bit.total
      q_by_node[u].each do |k, idx|
        if total < k
          ans[idx] = -1
        else
          ans[idx] = bit.kth(k)
        end
      end
    end

    # clear unless this node is heavy child of its parent
    p = par[u]
    keep = (p != -1 && heavy[p] == u)
    unless keep
      cur_bucket.each do |val|
        cnt[val] -= 1
        if cnt[val] == 0
          bit.add(val + 1, -1)
        end
      end
      bucket[u] = []
    end
  end

  ans
end
```

## Scala

```scala
import java.util.ArrayDeque
import java.util.ArrayList
import java.util.HashMap
import java.util.concurrent.ThreadLocalRandom

object Solution {
  private class TreapNode(var key: Int, var prio: Int) {
    var left: TreapNode = null
    var right: TreapNode = null
    var size: Int = 1
  }

  private def sz(t: TreapNode): Int = if (t == null) 0 else t.size

  private def upd(t: TreapNode): Unit = {
    if (t != null) t.size = 1 + sz(t.left) + sz(t.right)
  }

  private def rotateRight(y: TreapNode): TreapNode = {
    val x = y.left
    y.left = x.right
    x.right = y
    upd(y)
    upd(x)
    x
  }

  private def rotateLeft(x: TreapNode): TreapNode = {
    val y = x.right
    x.right = y.left
    y.left = x
    upd(x)
    upd(y)
    y
  }

  private def insert(t: TreapNode, key: Int): TreapNode = {
    if (t == null) return new TreapNode(key, ThreadLocalRandom.current().nextInt())
    if (key == t.key) return t
    if (key < t.key) {
      t.left = insert(t.left, key)
      if (t.left.prio > t.prio) return rotateRight(t)
    } else {
      t.right = insert(t.right, key)
      if (t.right.prio > t.prio) return rotateLeft(t)
    }
    upd(t)
    t
  }

  private def kth(t: TreapNode, k: Int): Int = {
    var node = t
    var kk = k
    while (node != null) {
      val leftSize = sz(node.left)
      if (kk < leftSize) {
        node = node.left
      } else if (kk == leftSize) {
        return node.key
      } else {
        kk -= leftSize + 1
        node = node.right
      }
    }
    -1 // should never reach here if k is valid
  }

  private def mergeInto(bigRoot: TreapNode, smallRoot: TreapNode): TreapNode = {
    var res = bigRoot
    if (smallRoot == null) return res
    val stack = new ArrayDeque[TreapNode]()
    stack.push(smallRoot)
    while (!stack.isEmpty) {
      val node = stack.pop()
      res = insert(res, node.key)
      if (node.left != null) stack.push(node.left)
      if (node.right != null) stack.push(node.right)
    }
    res
  }

  def kthSmallest(par: Array[Int], vals: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
    val n = par.length
    // build children list
    val children = Array.fill(n)(new ArrayList[Int]())
    for (i <- 1 until n) {
      children(par(i)).add(i)
    }

    // compute path xor using BFS/stack
    val pathXor = new Array[Int](n)
    val stackNode = new ArrayDeque[Int]()
    stackNode.push(0)
    pathXor(0) = vals(0)
    while (!stackNode.isEmpty) {
      val u = stackNode.pop()
      val it = children(u).iterator()
      while (it.hasNext) {
        val v = it.next()
        pathXor(v) = pathXor(u) ^ vals(v)
        stackNode.push(v)
      }
    }

    // store queries per node
    val qPerNode = Array.fill(n)(new ArrayList[Array[Int]]()) // each element: [k, idx]
    for (i <- queries.indices) {
      val u = queries(i)(0)
      val k = queries(i)(1)
      qPerNode(u).add(Array(k, i))
    }

    // postorder traversal order
    val order = new ArrayList[Int]()
    val stack = new ArrayDeque[(Int, Int)]() // (node, state) 0=enter,1=exit
    stack.push((0, 0))
    while (!stack.isEmpty) {
      val (u, st) = stack.pop()
      if (st == 0) {
        stack.push((u, 1))
        val it = children(u).iterator()
        while (it.hasNext) {
          stack.push((it.next(), 0))
        }
      } else {
        order.add(u)
      }
    }

    // treap per node
    val treaps = new Array[TreapNode](n)

    val ans = new Array[Int](queries.length)

    // process nodes in postorder
    for (idx <- 0 until order.size()) {
      val u = order.get(idx)

      // find biggest child treap
      var bigChild = -1
      var maxSize = -1
      val itc = children(u).iterator()
      while (itc.hasNext) {
        val v = itc.next()
        val szv = if (treaps(v) == null) 0 else treaps(v).size
        if (szv > maxSize) {
          maxSize = szv
          bigChild = v
        }
      }

      var cur: TreapNode = null
      if (bigChild != -1) cur = treaps(bigChild)

      val itc2 = children(u).iterator()
      while (itc2.hasNext) {
        val v = itc2.next()
        if (v != bigChild) {
          cur = mergeInto(cur, treaps(v))
        }
      }

      // insert own path xor
      cur = insert(cur, pathXor(u))
      treaps(u) = cur

      // answer queries for u
      val qlist = qPerNode(u)
      val itq = qlist.iterator()
      while (itq.hasNext) {
        val arr = itq.next()
        val k = arr(0)
        val qi = arr(1)
        if (cur == null || sz(cur) < k) ans(qi) = -1
        else ans(qi) = kth(cur, k - 1)
      }
    }

    ans
  }
}
```

## Rust

```rust
use std::cmp::Ordering;

pub struct BIT {
    n: usize,
    tree: Vec<i32>,
}
impl BIT {
    fn new(n: usize) -> Self {
        BIT { n, tree: vec![0; n + 2] }
    }
    fn add(&mut self, mut idx: usize, delta: i32) {
        while idx <= self.n {
            self.tree[idx] += delta;
            idx += idx & (!idx + 1);
        }
    }
    fn sum(&self, mut idx: usize) -> i32 {
        let mut res = 0;
        while idx > 0 {
            res += self.tree[idx];
            idx &= idx - 1;
        }
        res
    }
    // smallest index such that prefix sum >= k (k >= 1)
    fn kth(&self, mut k: i32) -> usize {
        let mut idx = 0usize;
        let mut bitmask = 1usize;
        while bitmask << 1 <= self.n {
            bitmask <<= 1;
        }
        while bitmask > 0 {
            let next = idx + bitmask;
            if next <= self.n && self.tree[next] < k {
                k -= self.tree[next];
                idx = next;
            }
            bitmask >>= 1;
        }
        idx + 1
    }
}

#[derive(Clone)]
struct Query {
    l: usize,
    r: usize,
    k: i32,
    idx: usize,
}

impl Solution {
    pub fn kth_smallest(par: Vec<i32>, vals: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = vals.len();
        // build children list
        let mut children: Vec<Vec<usize>> = vec![Vec::new(); n];
        for i in 1..n {
            let p = par[i] as usize;
            children[p].push(i);
        }
        // euler tour and path xor
        let mut tin = vec![0usize; n];
        let mut tout = vec![0usize; n];
        let mut euler = vec![0i32; n];
        fn dfs(
            u: usize,
            cur_xor: i32,
            children: &Vec<Vec<usize>>,
            vals: &Vec<i32>,
            tin: &mut Vec<usize>,
            tout: &mut Vec<usize>,
            euler: &mut Vec<i32>,
            timer: &mut usize,
        ) {
            tin[u] = *timer;
            let node_xor = cur_xor ^ vals[u];
            euler[*timer] = node_xor;
            *timer += 1;
            for &v in &children[u] {
                dfs(v, node_xor, children, vals, tin, tout, euler, timer);
            }
            tout[u] = *timer - 1;
        }
        let mut timer = 0usize;
        dfs(
            0,
            0,
            &children,
            &vals,
            &mut tin,
            &mut tout,
            &mut euler,
            &mut timer,
        );

        // prepare queries
        let qlen = queries.len();
        let mut qs: Vec<Query> = Vec::with_capacity(qlen);
        for (i, qu) in queries.iter().enumerate() {
            let u = qu[0] as usize;
            let k = qu[1];
            qs.push(Query {
                l: tin[u],
                r: tout[u],
                k,
                idx: i,
            });
        }

        // Mo's algorithm ordering
        let block = (n as f64).sqrt() as usize + 1;
        qs.sort_by(|a, b| {
            let ba = a.l / block;
            let bb = b.l / block;
            if ba != bb {
                return ba.cmp(&bb);
            }
            if ba % 2 == 0 {
                a.r.cmp(&b.r)
            } else {
                b.r.cmp(&a.r)
            }
        });

        // value domain size
        let mut max_val = 0i32;
        for &v in &euler {
            if v > max_val {
                max_val = v;
            }
        }
        let size = (max_val as usize) + 2; // plus one for offset, extra safety

        let mut cnt = vec![0i32; size];
        let mut bit = BIT::new(size);
        let mut cur_l: usize = 0;
        let mut cur_r: usize = 0; // current range is empty [cur_l, cur_r)
        let mut answers = vec![-1i32; qlen];

        let mut add = |pos: usize,
                       cnt: &mut Vec<i32>,
                       bit: &mut BIT|
         {
            let val = euler[pos] as usize;
            cnt[val] += 1;
            if cnt[val] == 1 {
                bit.add(val + 1, 1);
            }
        };
        let mut remove = |pos: usize,
                          cnt: &mut Vec<i32>,
                          bit: &mut BIT|
         {
            let val = euler[pos] as usize;
            cnt[val] -= 1;
            if cnt[val] == 0 {
                bit.add(val + 1, -1);
            }
        };

        for q in qs.iter() {
            while cur_l > q.l {
                cur_l -= 1;
                add(cur_l, &mut cnt, &mut bit);
            }
            while cur_r <= q.r {
                add(cur_r, &mut cnt, &mut bit);
                cur_r += 1;
            }
            while cur_l < q.l {
                remove(cur_l, &mut cnt, &mut bit);
                cur_l += 1;
            }
            while cur_r > q.r + 1 {
                cur_r -= 1;
                remove(cur_r, &mut cnt, &mut bit);
            }

            let total = bit.sum(size);
            if total < q.k {
                answers[q.idx] = -1;
            } else {
                let idx = bit.kth(q.k) as usize; // 1-indexed in BIT
                answers[q.idx] = (idx - 1) as i32;
            }
        }

        answers
    }
}
```

## Racket

```racket
(define/contract (kth-smallest par vals queries)
  (-> (listof exact-integer?) (listof exact-integer?) (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ((n (length vals))
         (parv (list->vector par))
         (valv (list->vector vals))
         ;; adjacency list of children
         (children (make-vector n '()))
         (size (make-vector n 0))
         (heavy (make-vector n -1))
         (tin (make-vector n 0))
         (tout (make-vector n 0))
         (pref (make-vector n 0))
         (euler (make-vector n 0))
         (cur-idx (box 0)))
    ;; build children lists
    (for ([i (in-range 1 n)])
      (let ((p (vector-ref parv i)))
        (vector-set! children p (cons i (vector-ref children p)))))
    ;; first dfs: compute sizes, heavy child, euler order and prefix xor
    (define (dfs1 u)
      (let* ((idx (unbox cur-idx))
             (_ (vector-set! tin u idx))
             (_ (vector-set! euler idx u))
             (_ (set-box! cur-idx (+ idx 1))))
        (vector-set! size u 1)
        (let loop ((maxsz 0) (h -1) (chs (vector-ref children u)))
          (if (null? chs)
              (begin
                (vector-set! heavy u h)
                (vector-set! tout u (- (unbox cur-idx) 1)))
              (let* ((v (car chs))
                     (_ (vector-set! pref v (bitwise-xor (vector-ref pref u) (vector-ref valv v)))))
                (dfs1 v)
                (let* ((szv (vector-ref size v))
                       (newsize (+ (vector-ref size u) szv)))
                  (vector-set! size u newsize)
                  (if (> szv maxsz)
                      (loop szv v (cdr chs))
                      (loop maxsz h (cdr chs)))))))))
    ;; init root prefix xor
    (vector-set! pref 0 (vector-ref valv 0))
    (dfs1 0)
    ;; determine maximum possible xor value for BIT size
    (define max-pref
      (let loop ((i 0) (mx 0))
        (if (= i n) mx
            (loop (+ i 1) (max mx (vector-ref pref i))))))
    (define bit-n (+ max-pref 2)) ; 1‑based BIT, index = value+1
    (define cnt (make-vector (+ max-pref 1) 0))
    (define bit (make-vector (+ bit-n 1) 0))
    ;; BIT helpers
    (define (bit-add idx delta)
      (let loop ((i idx))
        (when (<= i bit-n)
          (vector-set! bit i (+ (vector-ref bit i) delta))
          (loop (+ i (bitwise-and (- i) i))))))
    (define (bit-sum idx)
      (let loop ((i idx) (res 0))
        (if (= i 0) res
            (loop (- i (bitwise-and i (- i))) (+ res (vector-ref bit i))))))
    ;; find smallest index with prefix sum >= k (1‑based BIT)
    (define (bit-kth k)
      (let* ((size bit-n)
             (step (let loop ((p 1))
                     (if (> p size) (/ p 2) (loop (* p 2))))))
        (let loop ((idx 0) (step step) (kk k))
          (if (= step 0)
              (+ idx 1) ; return BIT index
              (let ((next (+ idx step)))
                (if (and (<= next size) (< (vector-ref bit next) kk))
                    (loop next (/ step 2) (- kk (vector-ref bit next)))
                    (loop idx (/ step 2) kk)))))))
    ;; add / remove a value
    (define (add-value v)
      (let ((c (vector-ref cnt v)))
        (when (= c 0) (bit-add (+ v 1) 1))
        (vector-set! cnt v (+ c 1))))
    (define (remove-value v)
      (let ((c (vector-ref cnt v)))
        (vector-set! cnt v (- c 1))
        (when (= (- c 1) 0) (bit-add (+ v 1) -1))))
    ;; add / remove whole subtree using euler interval
    (define (add-subtree u)
      (let ((l (vector-ref tin u)) (r (vector-ref tout u)))
        (for ([i (in-range l (+ r 1))])
          (add-value (vector-ref pref (vector-ref euler i))))))
    (define (remove-subtree u)
      (let ((l (vector-ref tin u)) (r (vector-ref tout u)))
        (for ([i (in-range l (+ r 1))])
          (remove-value (vector-ref pref (vector-ref euler i))))))
    ;; group queries by node
    (define qlen (length queries))
    (define qlist (make-vector n '()))
    (for* ([idx (in-range qlen)]
           [qr (list-ref queries idx)])
      (let ((u (first qr))
            (k (second qr)))
        (vector-set! qlist u (cons (list k idx) (vector-ref qlist u)))))
    (define ans (make-vector qlen 0))
    ;; DSU on tree
    (define (dfs2 u keep)
      (let ((h (vector-ref heavy u)))
        ;; process light children
        (for ([v (vector-ref children u)])
          (when (not (= v h)) (dfs2 v #f)))
        ;; heavy child
        (when (>= h 0) (dfs2 h #t))
        ;; add light children's contributions
        (for ([v (vector-ref children u)])
          (when (not (= v h)) (add-subtree v)))
        ;; add current node
        (add-value (vector-ref pref u))
        ;; answer queries at u
        (for ([qpair (vector-ref qlist u)])
          (let* ((k (first qpair))
                 (idx (second qpair))
                 (total (bit-sum bit-n)))
            (if (> k total)
                (vector-set! ans idx -1)
                (let ((val (bit-kth k))) ; BIT index = value+1
                  (vector-set! ans idx (- val 1))))))
        ;; clean up if not keep
        (unless keep
          (remove-subtree u))))
    (dfs2 0 #t)
    (let loop ((i 0) (res '()))
      (if (= i qlen) (reverse res)
          (loop (+ i 1) (cons (vector-ref ans i) res))))))
```

## Erlang

```erlang
-module(solution).
-export([kth_smallest/3]).

-spec kth_smallest(Par :: [integer()], Vals :: [integer()], Queries :: [[integer()]]) -> [integer()].
kth_smallest(Par, Vals, Queries) ->
    N = length(Vals),
    MaxBit = 20,
    ChildrenMap = build_children(Par, 0, #{}),
    ValsMap = build_vals_map(Vals, 0, #{}),
    PathXorMap = dfs_path_xor(0, 0, ChildrenMap, ValsMap, #{}),
    QueriesMap = build_queries_map(Queries, 0, #{}),
    {_, AnswersMap} = dfs_process(0, ChildrenMap, PathXorMap, QueriesMap, MaxBit),
    QLen = length(Queries),
    [maps:get(I, AnswersMap) || I <- lists:seq(0, QLen-1)].

%% Build children adjacency map
build_children([], _Idx, Acc) -> Acc;
build_children([P|Rest], Idx, Acc) ->
    NewAcc = case P of
        -1 -> Acc;
        _Parent ->
            maps:update_with(P,
                fun(L) -> [Idx|L] end,
                [Idx],
                Acc)
    end,
    build_children(Rest, Idx+1, NewAcc).

%% Build vals map node->value
build_vals_map([], _Idx, Acc) -> Acc;
build_vals_map([V|Rest], Idx, Acc) ->
    build_vals_map(Rest, Idx+1, maps:put(Idx, V, Acc)).

%% Compute path xor for each node
dfs_path_xor(Node, CurXor, ChildrenMap, ValsMap, Acc) ->
    NewXor = CurXor bxor maps:get(Node, ValsMap),
    Acc1 = maps:put(Node, NewXor, Acc),
    ChildList = maps:get(Node, ChildrenMap, []),
    lists:foldl(fun(Child, A) -> dfs_path_xor(Child, NewXor, ChildrenMap, ValsMap, A) end,
                Acc1,
                ChildList).

%% Build queries map node -> [{K,Idx}]
build_queries_map([], _Idx, Acc) -> Acc;
build_queries_map([[U,K]|Rest], Idx, Acc) ->
    Entry = {K, Idx},
    NewAcc = maps:update_with(U,
                fun(L) -> [Entry|L] end,
                [Entry],
                Acc),
    build_queries_map(Rest, Idx+1, NewAcc).

%% Process DSU on tree and answer queries
dfs_process(Node, ChildrenMap, PathXorMap, QueriesMap, MaxBit) ->
    Val = maps:get(Node, PathXorMap),
    BaseTrie = insert(undefined, Val, MaxBit),
    ChildList = maps:get(Node, ChildrenMap, []),
    {MergedTrie, AnsMap} = lists:foldl(
        fun(Child, {AccTrie, AccAns}) ->
            {ChildTrie, ChildAns} = dfs_process(Child, ChildrenMap, PathXorMap, QueriesMap, MaxBit),
            NewTrie = case get_cnt(AccTrie) < get_cnt(ChildTrie) of
                true -> merge(ChildTrie, AccTrie);
                false -> merge(AccTrie, ChildTrie)
            end,
            {NewTrie, maps:merge(AccAns, ChildAns)}
        end,
        {BaseTrie, #{}},
        ChildList),
    Qs = maps:get(Node, QueriesMap, []),
    FinalAns = lists:foldl(
        fun({K,Idx}, AM) ->
            Answer = if K > get_cnt(MergedTrie) -> -1;
                        true -> kth_in_trie(MergedTrie, K-1, MaxBit)
                     end,
            maps:put(Idx, Answer, AM)
        end,
        AnsMap,
        Qs),
    {MergedTrie, FinalAns}.

%% Trie operations
get_cnt(undefined) -> 0;
get_cnt({Cnt,_,_}) -> Cnt.

insert(undefined, Val, BitPos) ->
    if BitPos < 0 ->
            {1, undefined, undefined};
       true ->
            Bit = (Val bsr BitPos) band 1,
            Child = insert(undefined, Val, BitPos-1),
            case Bit of
                0 -> NewL = Child, NewR = undefined;
                1 -> NewL = undefined, NewR = Child
            end,
            Cnt = get_cnt(NewL) + get_cnt(NewR),
            {Cnt, NewL, NewR}
    end;
insert({_,L,R}=Node, Val, BitPos) ->
    if BitPos < 0 ->
            {1, undefined, undefined};
       true ->
            Bit = (Val bsr BitPos) band 1,
            case Bit of
                0 -> NewL = insert(L, Val, BitPos-1), NewR = R;
                1 -> NewL = L, NewR = insert(R, Val, BitPos-1)
            end,
            Cnt = get_cnt(NewL) + get_cnt(NewR),
            {Cnt, NewL, NewR}
    end.

merge(undefined, T) -> T;
merge(T, undefined) -> T;
merge({_,L1,R1}, {_,L2,R2}) ->
    NL = merge(L1, L2),
    NR = merge(R1, R2),
    Cnt = get_cnt(NL) + get_cnt(NR),
    {Cnt, NL, NR}.

%% kth smallest in trie (0‑based)
kth_in_trie(_, _, -1) -> 0;
kth_in_trie({_,L,R}=Node, K, BitPos) ->
    Lcnt = get_cnt(L),
    if K < Lcnt ->
            kth_in_trie(L, K, BitPos-1);
       true ->
            Sub = kth_in_trie(R, K - Lcnt, BitPos-1),
            (1 bsl BitPos) bor Sub
    end.
```

## Elixir

```elixir
defmodule Treap do
  defstruct key: nil, prio: nil, left: nil, right: nil, size: 1

  def new(key) do
    %Treap{key: key, prio: :rand.uniform()}
  end

  def size(nil), do: 0
  def size(node), do: node.size

  defp update(%Treap{} = node) do
    %{node | size: 1 + size(node.left) + size(node.right)}
  end

  def split(nil, _key), do: {nil, nil}
  def split(%Treap{key: k, left: l, right: r}=node, key) do
    if k < key do
      {lt, rt} = split(r, key)
      {update(%{node | right: lt}), rt}
    else
      {lt, rt} = split(l, key)
      {lt, update(%{node | left: rt})}
    end
  end

  def merge(nil, b), do: b
  def merge(a, nil), do: a
  def merge(%Treap{prio: pa}=a, %Treap{prio: pb}=b) do
    if pa < pb do
      new_right = merge(a.right, b)
      update(%{a | right: new_right})
    else
      new_left = merge(a, b.left)
      update(%{b | left: new_left})
    end
  end

  def insert(nil, key), do: new(key)
  def insert(node=%Treap{key: k}=node0, key) do
    if key == k do
      node0
    else
      {l, r} = split(node0, key)
      merged = merge(l, new(key))
      merge(merged, r)
    end
  end

  def kth(nil, _idx), do: nil
  def kth(%Treap{key: k, left: l, right: r}=node, idx) do
    left_sz = size(l)
    cond do
      idx < left_sz -> kth(l, idx)
      idx == left_sz -> k
      true -> kth(r, idx - left_sz - 1)
    end
  end

  def to_list(node), do: to_list(node, [])
  defp to_list(nil, acc), do: acc
  defp to_list(%Treap{key: k, left: l, right: r}, acc) do
    acc = to_list(r, acc)
    acc = [k | acc]
    to_list(l, acc)
  end
end

defmodule Solution do
  require Bitwise

  @spec kth_smallest(par :: [integer], vals :: [integer], queries :: [[integer]]) :: [integer]
  def kth_smallest(par, vals, queries) do
    n = length(par)

    # build adjacency list
    adj = :array.new(n, default: [])
    adj =
      Enum.reduce(0..(n - 1), adj, fn i, acc ->
        p = Enum.at(par, i)
        if p != -1 do
          children = :array.get(p, acc)
          :array.set(p, [i | children], acc)
        else
          acc
        end
      end)

    # compute xor from root to each node
    xor_arr = :array.new(n, default: 0)
    {xor_arr, _} = dfs_xor(0, adj, vals, xor_arr, 0)

    # map queries per node
    query_map =
      Enum.with_index(queries)
      |> Enum.reduce(%{}, fn {{u, k}, idx}, acc ->
        Map.update(acc, u, [{k, idx}], fn list -> [{k, idx} | list] end)
      end)

    ans_map = %{}
    {_treap, final_ans} = dfs(0, adj, xor_arr, query_map, ans_map)

    Enum.map(0..(length(queries) - 1), fn i -> Map.get(final_ans, i) end)
  end

  defp dfs_xor(u, adj, vals, xor_arr, cur_xor) do
    node_val = Enum.at(vals, u)
    new_xor = Bitwise.bxor(cur_xor, node_val)
    xor_arr = :array.set(u, new_xor, xor_arr)

    children = :array.get(u, adj)

    Enum.reduce(children, {xor_arr, new_xor}, fn child, {arr, _} ->
      dfs_xor(child, adj, vals, arr, new_xor)
    end)
  end

  defp dfs(u, adj, xor_vals, query_map, ans) do
    my_xor = :array.get(u, xor_vals)
    treap = Treap.insert(nil, my_xor)

    children = :array.get(u, adj)

    {treap, ans} =
      Enum.reduce(children, {treap, ans}, fn child, {cur_treap, cur_ans} ->
        {child_treap, new_ans} = dfs(child, adj, xor_vals, query_map, cur_ans)

        # ensure cur_treap is the larger one
        if Treap.size(child_treap) > Treap.size(cur_treap) do
          {cur_treap, child_treap} = {child_treap, cur_treap}
        end

        merged =
          Enum.reduce(Treap.to_list(child_treap), cur_treap, fn key, acc ->
            Treap.insert(acc, key)
          end)

        {merged, new_ans}
      end)

    ans =
      case Map.get(query_map, u) do
        nil -> ans
        qlist ->
          Enum.reduce(qlist, ans, fn {k, idx}, a ->
            if k <= Treap.size(treap) do
              val = Treap.kth(treap, k - 1)
              Map.put(a, idx, val)
            else
              Map.put(a, idx, -1)
            end
          end)
      end

    {treap, ans}
  end
end
```
