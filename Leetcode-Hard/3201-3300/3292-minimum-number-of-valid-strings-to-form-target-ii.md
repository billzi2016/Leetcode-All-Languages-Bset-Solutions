# 3292. Minimum Number of Valid Strings to Form Target II

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class SegTree {
    const int INF = 1e9;
    int n;
    vector<int> seg, lazy;
    void push(int node) {
        if (lazy[node] == INF) return;
        for (int child : {node << 1, node << 1 | 1}) {
            seg[child] = min(seg[child], lazy[node]);
            lazy[child] = min(lazy[child], lazy[node]);
        }
        lazy[node] = INF;
    }
    void range_chmin(int node, int nl, int nr, int l, int r, int val) {
        if (r < nl || nr < l) return;
        if (l <= nl && nr <= r) {
            seg[node] = min(seg[node], val);
            lazy[node] = min(lazy[node], val);
            return;
        }
        push(node);
        int mid = (nl + nr) >> 1;
        range_chmin(node << 1, nl, mid, l, r, val);
        range_chmin(node << 1 | 1, mid + 1, nr, l, r, val);
        seg[node] = min(seg[node << 1], seg[node << 1 | 1]);
    }
    int point_query(int node, int nl, int nr, int idx) {
        if (nl == nr) return seg[node];
        push(node);
        int mid = (nl + nr) >> 1;
        if (idx <= mid) return point_query(node << 1, nl, mid, idx);
        else return point_query(node << 1 | 1, mid + 1, nr, idx);
    }
public:
    SegTree(int _n): n(_n) {
        seg.assign(4 * n, INF);
        lazy.assign(4 * n, INF);
    }
    void range_chmin(int l, int r, int val) { if (l <= r) range_chmin(1, 0, n - 1, l, r, val); }
    int point_query(int idx) { return point_query(1, 0, n - 1, idx); }
};

class Solution {
public:
    int minValidStrings(vector<string>& words, string target) {
        using ull = unsigned long long;
        const ull BASE = 91138233ULL;

        // collect all prefix hashes grouped by length
        size_t maxWordLen = 0;
        for (auto &w : words) maxWordLen = max(maxWordLen, w.size());
        vector<unordered_set<ull>> prefByLen(maxWordLen + 1);
        for (const string& w : words) {
            ull h = 0;
            for (size_t i = 0; i < w.size(); ++i) {
                h = h * BASE + (ull)(w[i] - 'a' + 1);
                prefByLen[i + 1].insert(h);
            }
        }

        int n = target.size();
        // rolling hash for target
        vector<ull> powBase(n + 1, 1), preHash(n + 1, 0);
        for (int i = 1; i <= n; ++i) {
            powBase[i] = powBase[i - 1] * BASE;
            preHash[i] = preHash[i - 1] * BASE + (ull)(target[i - 1] - 'a' + 1);
        }
        auto getHash = [&](int l, int len) -> ull {
            // substring target[l .. l+len-1]
            return preHash[l + len] - preHash[l] * powBase[len];
        };

        vector<int> maxReach(n, 0); // exclusive index
        for (int i = 0; i < n; ++i) {
            int low = 0, high = min<int>(maxWordLen, n - i);
            while (low < high) {
                int mid = (low + high + 1) >> 1;
                ull h = getHash(i, mid);
                if (!prefByLen[mid].empty() && prefByLen[mid].count(h)) low = mid;
                else high = mid - 1;
            }
            maxReach[i] = i + low; // position after the longest valid substring
        }

        SegTree st(n + 1);
        st.range_chmin(0, 0, 0); // dp[0]=0

        const int INF = 1e9;
        for (int i = 0; i < n; ++i) {
            int cur = st.point_query(i);
            if (cur == INF) continue;
            int r = maxReach[i];
            if (r > i) st.range_chmin(i + 1, r, cur + 1);
        }
        int ans = st.point_query(n);
        return ans >= INF ? -1 : ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static final long BASE = 91138233L;
    private static final int INF = 1_000_000_000;

    public int minValidStrings(String[] words, String target) {
        int n = target.length();
        // map length -> set of prefix hashes
        Map<Integer, HashSet<Long>> hashMap = new HashMap<>();
        int maxWordLen = 0;
        for (String w : words) {
            long h = 0L;
            for (int i = 0; i < w.length(); i++) {
                h = h * BASE + (w.charAt(i) - 'a' + 1);
                int len = i + 1;
                hashMap.computeIfAbsent(len, k -> new HashSet<>()).add(h);
                if (len > maxWordLen) maxWordLen = len;
            }
        }

        // precompute powers
        long[] pow = new long[n + 1];
        pow[0] = 1L;
        for (int i = 1; i <= n; i++) {
            pow[i] = pow[i - 1] * BASE;
        }

        // prefix hash of target
        long[] pref = new long[n + 1];
        pref[0] = 0L;
        for (int i = 0; i < n; i++) {
            pref[i + 1] = pref[i] * BASE + (target.charAt(i) - 'a' + 1);
        }

        SegTree seg = new SegTree(n + 1);
        seg.pointSet(0, 0);

        for (int i = 0; i < n; i++) {
            int cur = seg.queryPoint(i);
            if (cur == INF) continue;

            int low = 1;
            int high = Math.min(maxWordLen, n - i);
            int best = 0;
            while (low <= high) {
                int mid = (low + high) >>> 1;
                long subHash = pref[i + mid] - pref[i] * pow[mid];
                HashSet<Long> set = hashMap.get(mid);
                if (set != null && set.contains(subHash)) {
                    best = mid;
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }

            if (best > 0) {
                int l = i + 1;
                int r = Math.min(n, i + best);
                seg.rangeChmin(l, r, cur + 1);
            }
        }

        int ans = seg.queryPoint(n);
        return ans == INF ? -1 : ans;
    }

    // Segment tree supporting range chmin and point query
    private static class SegTree {
        int size;          // power of two >= n
        int[] tree;
        int[] lazy;

        SegTree(int n) {
            size = 1;
            while (size < n) size <<= 1;
            tree = new int[size << 1];
            lazy = new int[size << 1];
            Arrays.fill(tree, INF);
            Arrays.fill(lazy, INF);
        }

        private void apply(int node, int val) {
            if (val < tree[node]) {
                tree[node] = val;
                lazy[node] = Math.min(lazy[node], val);
            }
        }

        private void push(int node) {
            if (lazy[node] != INF) {
                apply(node << 1, lazy[node]);
                apply(node << 1 | 1, lazy[node]);
                lazy[node] = INF;
            }
        }

        // range [l, r] inclusive
        void rangeChmin(int l, int r, int val) {
            rangeChmin(l, r, val, 1, 0, size - 1);
        }

        private void rangeChmin(int l, int r, int val, int node, int nl, int nr) {
            if (l > nr || r < nl) return;
            if (l <= nl && nr <= r) {
                apply(node, val);
                return;
            }
            push(node);
            int mid = (nl + nr) >>> 1;
            rangeChmin(l, r, val, node << 1, nl, mid);
            rangeChmin(l, r, val, node << 1 | 1, mid + 1, nr);
            tree[node] = Math.min(tree[node << 1], tree[node << 1 | 1]);
        }

        int queryPoint(int idx) {
            return queryPoint(idx, 1, 0, size - 1);
        }

        private int queryPoint(int idx, int node, int nl, int nr) {
            if (nl == nr) return tree[node];
            push(node);
            int mid = (nl + nr) >>> 1;
            if (idx <= mid) return queryPoint(idx, node << 1, nl, mid);
            else return queryPoint(idx, node << 1 | 1, mid + 1, nr);
        }

        // set a single point to a specific value (used for dp[0]=0)
        void pointSet(int idx, int val) {
            int node = idx + size;
            tree[node] = Math.min(tree[node], val);
            while ((node >>= 1) > 0) {
                tree[node] = Math.min(tree[node << 1], tree[node << 1 | 1]);
            }
        }
    }
}
```

## Python

```python
class Solution(object):
    def minValidStrings(self, words, target):
        """
        :type words: List[str]
        :type target: str
        :rtype: int
        """
        MOD = 1000000007
        BASE = 91138233

        from collections import defaultdict, deque

        # store hashes of all prefixes grouped by length
        pref_hashes = defaultdict(set)
        max_word_len = 0
        for w in words:
            h = 0
            for i, ch in enumerate(w):
                h = (h * BASE + ord(ch)) % MOD
                l = i + 1
                pref_hashes[l].add(h)
            if len(w) > max_word_len:
                max_word_len = len(w)

        n = len(target)
        # precompute powers
        pow_arr = [1] * (max(n, max_word_len) + 2)
        for i in range(1, len(pow_arr)):
            pow_arr[i] = (pow_arr[i - 1] * BASE) % MOD

        # prefix hash of target
        H = [0] * (n + 1)
        for i, ch in enumerate(target):
            H[i + 1] = (H[i] * BASE + ord(ch)) % MOD

        def get_hash(l, r):  # substring [l, r)
            return (H[r] - H[l] * pow_arr[r - l]) % MOD

        INF = 10 ** 9
        dp = [INF] * (n + 1)
        dp[0] = 0

        # DSU for next unvisited index
        parent = list(range(n + 2))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        q = deque([0])

        while q:
            i = q.popleft()
            cur = dp[i]

            # binary search longest valid length starting at i
            low, high = 1, min(max_word_len, n - i)
            best = 0
            while low <= high:
                mid = (low + high) // 2
                hsub = get_hash(i, i + mid)
                if hsub in pref_hashes.get(mid, ()):
                    best = mid
                    low = mid + 1
                else:
                    high = mid - 1

            if best == 0:
                continue

            l = i + 1
            r = i + best
            j = find(l)
            while j <= r:
                dp[j] = cur + 1
                q.append(j)
                # mark visited
                parent[j] = find(j + 1)
                j = find(j)

        return dp[n] if dp[n] != INF else -1
```

## Python3

```python
from typing import List

class SegTree:
    def __init__(self, n):
        self.N = 1
        while self.N < n:
            self.N <<= 1
        self.val = [float('inf')] * (2 * self.N)
        self.lazy = [float('inf')] * (2 * self.N)

    def _apply(self, idx, v):
        if v < self.val[idx]:
            self.val[idx] = v
        if v < self.lazy[idx]:
            self.lazy[idx] = v

    def _push(self, idx):
        if self.lazy[idx] != float('inf'):
            self._apply(idx << 1, self.lazy[idx])
            self._apply(idx << 1 | 1, self.lazy[idx])
            self.lazy[idx] = float('inf')

    def update(self, l, r, v, idx=1, left=0, right=None):
        if right is None:
            right = self.N - 1
        if r < left or l > right:
            return
        if l <= left and right <= r:
            self._apply(idx, v)
            return
        self._push(idx)
        mid = (left + right) >> 1
        self.update(l, r, v, idx << 1, left, mid)
        self.update(l, r, v, idx << 1 | 1, mid + 1, right)
        self.val[idx] = min(self.val[idx << 1], self.val[idx << 1 | 1])

    def query(self, pos, idx=1, left=0, right=None):
        if right is None:
            right = self.N - 1
        if left == right:
            return self.val[idx]
        self._push(idx)
        mid = (left + right) >> 1
        if pos <= mid:
            return self.query(pos, idx << 1, left, mid)
        else:
            return self.query(pos, idx << 1 | 1, mid + 1, right)


class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)
        max_word_len = max(len(w) for w in words)

        base = 91138233
        mod1 = 1000000007
        mod2 = 1000000009

        pref_sets = {}
        for w in words:
            h1 = h2 = 0
            for i, ch in enumerate(w):
                o = ord(ch) - 96
                h1 = (h1 * base + o) % mod1
                h2 = (h2 * base + o) % mod2
                l = i + 1
                pref_sets.setdefault(l, set()).add((h1, h2))

        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow1[i] = pow1[i - 1] * base % mod1
            pow2[i] = pow2[i - 1] * base % mod2

        pre1 = [0] * (n + 1)
        pre2 = [0] * (n + 1)
        for i, ch in enumerate(target, 1):
            o = ord(ch) - 96
            pre1[i] = (pre1[i - 1] * base + o) % mod1
            pre2[i] = (pre2[i - 1] * base + o) % mod2

        def get_hash(l, r):  # [l, r)
            h1 = (pre1[r] - pre1[l] * pow1[r - l]) % mod1
            h2 = (pre2[r] - pre2[l] * pow2[r - l]) % mod2
            return h1, h2

        max_len_arr = [0] * n
        for i in range(n):
            lo, hi = 0, min(max_word_len, n - i)
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if mid not in pref_sets:
                    hi = mid - 1
                    continue
                if get_hash(i, i + mid) in pref_sets[mid]:
                    lo = mid
                else:
                    hi = mid - 1
            max_len_arr[i] = lo

        seg = SegTree(n + 1)
        seg.update(0, 0, 0)

        for i in range(n):
            cur = seg.query(i)
            if cur == float('inf'):
                continue
            L = max_len_arr[i]
            if L:
                seg.update(i + 1, i + L, cur + 1)

        ans = seg.query(n)
        return -1 if ans == float('inf') else ans
```

## C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef unsigned long long ULL;

static const ULL BASE = 91138233ULL;
static const int INF = 0x3f3f3f3f;

/* Disjoint Set Union to skip visited positions */
int *parentDSU;
int find_set(int x) {
    if (parentDSU[x] != x) parentDSU[x] = find_set(parentDSU[x]);
    return parentDSU[x];
}
void unite_set(int x, int y) { // make x point to y
    parentDSU[find_set(x)] = find_set(y);
}

/* Simple hash set for (len,hash) pairs */
typedef struct Node {
    ULL key;
    struct Node *next;
} Node;

#define HASH_SIZE 262144

static Node *hashTable[HASH_SIZE];

static unsigned int hash_func(ULL x) {
    return (unsigned int)(x ^ (x >> 32)) & (HASH_SIZE - 1);
}
static int set_contains(ULL key) {
    unsigned int h = hash_func(key);
    for (Node *p = hashTable[h]; p; p = p->next)
        if (p->key == key) return 1;
    return 0;
}
static void set_insert(ULL key) {
    if (set_contains(key)) return;
    unsigned int h = hash_func(key);
    Node *node = (Node *)malloc(sizeof(Node));
    node->key = key;
    node->next = hashTable[h];
    hashTable[h] = node;
}

/* Main function */
int minValidStrings(char** words, int wordsSize, char* target) {
    int n = strlen(target);
    int maxWordLen = 0;

    /* Build prefix hash set */
    for (int i = 0; i < wordsSize; ++i) {
        const char *w = words[i];
        ULL h = 0;
        for (int j = 0; w[j]; ++j) {
            h = h * BASE + (ULL)(w[j] - 'a' + 1);
            int len = j + 1;
            if (len > maxWordLen) maxWordLen = len;
            ULL key = ((ULL)len << 32) ^ h;
            set_insert(key);
        }
    }

    /* Precompute rolling hash for target */
    ULL *pref = (ULL *)malloc((n + 1) * sizeof(ULL));
    ULL *powb = (ULL *)malloc((n + 1) * sizeof(ULL));
    pref[0] = 0;
    powb[0] = 1;
    for (int i = 0; i < n; ++i) {
        pref[i + 1] = pref[i] * BASE + (ULL)(target[i] - 'a' + 1);
        powb[i + 1] = powb[i] * BASE;
    }

    /* Compute maxLen for each position using binary search */
    int *maxLen = (int *)malloc((n) * sizeof(int));
    for (int i = 0; i < n; ++i) {
        int low = 0, high = maxWordLen;
        if (high > n - i) high = n - i;
        while (low < high) {
            int mid = (low + high + 1) >> 1;
            ULL subHash = pref[i + mid] - pref[i] * powb[mid];
            ULL key = ((ULL)mid << 32) ^ subHash;
            if (set_contains(key))
                low = mid;
            else
                high = mid - 1;
        }
        maxLen[i] = low; // may be 0
    }

    /* BFS with DSU to propagate dp */
    int *dp = (int *)malloc((n + 1) * sizeof(int));
    for (int i = 0; i <= n; ++i) dp[i] = INF;
    dp[0] = 0;

    parentDSU = (int *)malloc((n + 2) * sizeof(int));
    for (int i = 0; i <= n + 1; ++i) parentDSU[i] = i;

    int *queue = (int *)malloc((n + 1) * sizeof(int));
    int qhead = 0, qtail = 0;
    queue[qtail++] = 0;
    unite_set(0, 1); // mark position 0 as visited

    while (qhead < qtail) {
        int pos = queue[qhead++];
        if (pos == n) break;
        int reach = maxLen[pos];
        if (reach == 0) continue;
        int l = pos + 1;
        int r = pos + reach;
        if (r > n) r = n;
        int cur = find_set(l);
        while (cur <= r) {
            dp[cur] = dp[pos] + 1;
            queue[qtail++] = cur;
            unite_set(cur, cur + 1); // mark visited
            cur = find_set(cur);
        }
    }

    int ans = (dp[n] == INF) ? -1 : dp[n];
    /* free memory */
    free(pref);
    free(powb);
    free(maxLen);
    free(dp);
    free(queue);
    free(parentDSU);
    for (int i = 0; i < HASH_SIZE; ++i) {
        Node *p = hashTable[i];
        while (p) {
            Node *tmp = p;
            p = p->next;
            free(tmp);
        }
    }

    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MinValidStrings(string[] words, string target) {
        const ulong BASE = 91138233UL;
        const int INF = 1_000_000_0;

        // Build hash sets for each prefix length
        var dict = new Dictionary<int, HashSet<ulong>>();
        int maxLen = 0;
        foreach (var w in words) {
            ulong h = 0;
            for (int i = 0; i < w.Length; i++) {
                h = unchecked(h * BASE + (ulong)(w[i] - 'a' + 1));
                int len = i + 1;
                if (!dict.TryGetValue(len, out var set)) {
                    set = new HashSet<ulong>();
                    dict[len] = set;
                }
                set.Add(h);
            }
            if (w.Length > maxLen) maxLen = w.Length;
        }

        int n = target.Length;
        // Precompute powers
        ulong[] pow = new ulong[n + 1];
        pow[0] = 1;
        for (int i = 1; i <= n; i++) {
            pow[i] = unchecked(pow[i - 1] * BASE);
        }
        // Prefix hashes of target
        ulong[] pref = new ulong[n + 1];
        pref[0] = 0;
        for (int i = 0; i < n; i++) {
            pref[i + 1] = unchecked(pref[i] * BASE + (ulong)(target[i] - 'a' + 1));
        }

        // Helper to get hash of substring [l, r]
        ulong GetHash(int l, int r) {
            int len = r - l + 1;
            return unchecked(pref[r + 1] - pref[l] * pow[len]);
        }

        var seg = new SegTree(n + 1, INF);
        seg.Update(0, 0, 0); // dp[0]=0

        for (int i = 0; i < n; i++) {
            int cur = seg.Query(i);
            if (cur == INF) continue;

            int limit = Math.Min(maxLen, n - i);
            int lo = 1, hi = limit, best = 0;
            while (lo <= hi) {
                int mid = (lo + hi) >> 1;
                ulong h = GetHash(i, i + mid - 1);
                if (dict.TryGetValue(mid, out var set) && set.Contains(h)) {
                    best = mid;
                    lo = mid + 1;
                } else {
                    hi = mid - 1;
                }
            }

            if (best > 0) {
                seg.Update(i + 1, i + best, cur + 1);
            }
        }

        int ans = seg.Query(n);
        return ans >= INF ? -1 : ans;
    }

    // Segment tree supporting range chmin updates and point queries
    private class SegTree {
        private readonly int n;
        private readonly int[] seg;
        private readonly int[] lazy;
        private readonly int INF;

        public SegTree(int size, int inf) {
            n = size;
            INF = inf;
            seg = new int[4 * n];
            lazy = new int[4 * n];
            for (int i = 0; i < lazy.Length; i++) lazy[i] = INF;
            Build(1, 0, n - 1);
        }

        private void Build(int node, int l, int r) {
            if (l == r) {
                seg[node] = INF;
                return;
            }
            int mid = (l + r) >> 1;
            Build(node << 1, l, mid);
            Build(node << 1 | 1, mid + 1, r);
            seg[node] = Math.Min(seg[node << 1], seg[node << 1 | 1]);
        }

        private void Apply(int node, int val) {
            if (val < seg[node]) seg[node] = val;
            if (val < lazy[node]) lazy[node] = val;
        }

        private void Push(int node) {
            if (lazy[node] != INF) {
                Apply(node << 1, lazy[node]);
                Apply(node << 1 | 1, lazy[node]);
                lazy[node] = INF;
            }
        }

        public void Update(int l, int r, int val) {
            Update(1, 0, n - 1, l, r, val);
        }

        private void Update(int node, int nl, int nr, int l, int r, int val) {
            if (l > nr || r < nl) return;
            if (l <= nl && nr <= r) {
                Apply(node, val);
                return;
            }
            Push(node);
            int mid = (nl + nr) >> 1;
            Update(node << 1, nl, mid, l, r, val);
            Update(node << 1 | 1, mid + 1, nr, l, r, val);
            seg[node] = Math.Min(seg[node << 1], seg[node << 1 | 1]);
        }

        public int Query(int idx) {
            return Query(1, 0, n - 1, idx);
        }

        private int Query(int node, int nl, int nr, int idx) {
            if (nl == nr) return seg[node];
            Push(node);
            int mid = (nl + nr) >> 1;
            if (idx <= mid) return Query(node << 1, nl, mid, idx);
            else return Query(node << 1 | 1, mid + 1, nr, idx);
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @param {string} target
 * @return {number}
 */
var minValidStrings = function(words, target) {
    const MOD1 = 1000000007;
    const MOD2 = 1000000009;
    const BASE = 91138233;
    const n = target.length;

    // map length -> Set of hash keys for prefixes of that length
    const prefMap = new Map();
    let maxWordLen = 0;
    for (const w of words) {
        let h1 = 0, h2 = 0;
        for (let i = 0; i < w.length; ++i) {
            const code = w.charCodeAt(i);
            h1 = (h1 * BASE + code) % MOD1;
            h2 = (h2 * BASE + code) % MOD2;
            const len = i + 1;
            maxWordLen = Math.max(maxWordLen, len);
            let set = prefMap.get(len);
            if (!set) {
                set = new Set();
                prefMap.set(len, set);
            }
            set.add(h1 + '#' + h2);
        }
    }

    // precompute powers
    const pow1 = new Array(n + 1).fill(0);
    const pow2 = new Array(n + 1).fill(0);
    pow1[0] = 1;
    pow2[0] = 1;
    for (let i = 1; i <= n; ++i) {
        pow1[i] = (pow1[i - 1] * BASE) % MOD1;
        pow2[i] = (pow2[i - 1] * BASE) % MOD2;
    }

    // prefix hashes of target
    const pre1 = new Array(n + 1).fill(0);
    const pre2 = new Array(n + 1).fill(0);
    for (let i = 0; i < n; ++i) {
        const code = target.charCodeAt(i);
        pre1[i + 1] = (pre1[i] * BASE + code) % MOD1;
        pre2[i + 1] = (pre2[i] * BASE + code) % MOD2;
    }

    function getHash(l, r) { // [l, r)
        let x1 = (pre1[r] - (pre1[l] * pow1[r - l]) % MOD1);
        if (x1 < 0) x1 += MOD1;
        let x2 = (pre2[r] - (pre2[l] * pow2[r - l]) % MOD2);
        if (x2 < 0) x2 += MOD2;
        return x1 + '#' + x2;
    }

    // compute longest match length for each start position
    const maxLenArr = new Array(n).fill(0);
    for (let i = 0; i < n; ++i) {
        let low = 1, high = Math.min(maxWordLen, n - i), best = 0;
        while (low <= high) {
            const mid = (low + high) >> 1;
            const key = getHash(i, i + mid);
            const set = prefMap.get(mid);
            if (set && set.has(key)) {
                best = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        maxLenArr[i] = best;
    }

    // segment tree for range chmin and point query
    const INF = 1e9;
    const size = n + 1; // positions 0..n
    const segSize = 4 * size;
    const tree = new Array(segSize).fill(INF);
    const lazy = new Array(segSize).fill(INF);

    function push(node) {
        if (lazy[node] !== INF) {
            const left = node << 1, right = left | 1;
            tree[left] = Math.min(tree[left], lazy[node]);
            lazy[left] = Math.min(lazy[left], lazy[node]);
            tree[right] = Math.min(tree[right], lazy[node]);
            lazy[right] = Math.min(lazy[right], lazy[node]);
            lazy[node] = INF;
        }
    }

    function rangeUpdate(node, l, r, ql, qr, val) {
        if (ql > r || qr < l) return;
        if (ql <= l && r <= qr) {
            tree[node] = Math.min(tree[node], val);
            lazy[node] = Math.min(lazy[node], val);
            return;
        }
        push(node);
        const mid = (l + r) >> 1;
        rangeUpdate(node << 1, l, mid, ql, qr, val);
        rangeUpdate((node << 1) | 1, mid + 1, r, ql, qr, val);
        tree[node] = Math.min(tree[node << 1], tree[(node << 1) | 1]);
    }

    function pointQuery(node, l, r, idx) {
        if (l === r) return tree[node];
        push(node);
        const mid = (l + r) >> 1;
        if (idx <= mid) return pointQuery(node << 1, l, mid, idx);
        else return pointQuery((node << 1) | 1, mid + 1, r, idx);
    }

    // initialize dp[0] = 0
    rangeUpdate(1, 0, n, 0, 0, 0);

    for (let i = 0; i < n; ++i) {
        const cur = pointQuery(1, 0, n, i);
        if (cur >= INF) continue;
        const len = maxLenArr[i];
        if (len > 0) {
            const l = i + 1;
            const r = i + len;
            rangeUpdate(1, 0, n, l, r, cur + 1);
        }
    }

    const ans = pointQuery(1, 0, n, n);
    return ans >= INF ? -1 : ans;
};
```

## Typescript

```typescript
function minValidStrings(words: string[], target: string): number {
    const MOD1 = 1000000007n;
    const MOD2 = 1000000009n;
    const BASE = 91138233n;
    const INF = 1e9;

    const maxWordLen = Math.max(...words.map(w => w.length));
    const n = target.length;
    const maxLen = Math.max(maxWordLen, n);

    // store hashes of all prefixes grouped by length
    const prefixSets: Array<Set<string>> = new Array(maxLen + 1);
    for (const w of words) {
        let h1 = 0n, h2 = 0n;
        for (let i = 0; i < w.length; ++i) {
            const c = BigInt(w.charCodeAt(i) - 96); // 'a' -> 1
            h1 = (h1 * BASE + c) % MOD1;
            h2 = (h2 * BASE + c) % MOD2;
            const len = i + 1;
            let set = prefixSets[len];
            if (!set) {
                set = new Set<string>();
                prefixSets[len] = set;
            }
            set.add(`${h1.toString()},${h2.toString()}`);
        }
    }

    // powers
    const pow1: bigint[] = new Array(n + 1);
    const pow2: bigint[] = new Array(n + 1);
    pow1[0] = 1n;
    pow2[0] = 1n;
    for (let i = 1; i <= n; ++i) {
        pow1[i] = (pow1[i - 1] * BASE) % MOD1;
        pow2[i] = (pow2[i - 1] * BASE) % MOD2;
    }

    // prefix hashes of target
    const pref1: bigint[] = new Array(n + 1);
    const pref2: bigint[] = new Array(n + 1);
    pref1[0] = 0n;
    pref2[0] = 0n;
    for (let i = 0; i < n; ++i) {
        const c = BigInt(target.charCodeAt(i) - 96);
        pref1[i + 1] = (pref1[i] * BASE + c) % MOD1;
        pref2[i + 1] = (pref2[i] * BASE + c) % MOD2;
    }

    function getHash(start: number, len: number): [bigint, bigint] {
        const end = start + len;
        let h1 = pref1[end] - (pref1[start] * pow1[len]) % MOD1;
        if (h1 < 0) h1 += MOD1;
        let h2 = pref2[end] - (pref2[start] * pow2[len]) % MOD2;
        if (h2 < 0) h2 += MOD2;
        return [h1, h2];
    }

    class SegTree {
        n: number;
        tree: number[];
        lazy: number[];
        constructor(n: number) {
            this.n = n;
            const size = 4 * n + 5;
            this.tree = new Array(size).fill(INF);
            this.lazy = new Array(size).fill(INF);
        }
        push(node: number): void {
            const lz = this.lazy[node];
            if (lz !== INF) {
                const left = node << 1, right = left | 1;
                this.tree[left] = Math.min(this.tree[left], lz);
                this.lazy[left] = Math.min(this.lazy[left], lz);
                this.tree[right] = Math.min(this.tree[right], lz);
                this.lazy[right] = Math.min(this.lazy[right], lz);
                this.lazy[node] = INF;
            }
        }
        rangeUpdate(node: number, l: number, r: number, ql: number, qr: number, val: number): void {
            if (ql > r || qr < l) return;
            if (ql <= l && r <= qr) {
                this.tree[node] = Math.min(this.tree[node], val);
                this.lazy[node] = Math.min(this.lazy[node], val);
                return;
            }
            this.push(node);
            const mid = (l + r) >> 1;
            this.rangeUpdate(node << 1, l, mid, ql, qr, val);
            this.rangeUpdate((node << 1) | 1, mid + 1, r, ql, qr, val);
            this.tree[node] = Math.min(this.tree[node << 1], this.tree[(node << 1) | 1]);
        }
        pointQuery(node: number, l: number, r: number, idx: number): number {
            if (l === r) return this.tree[node];
            this.push(node);
            const mid = (l + r) >> 1;
            if (idx <= mid) return this.pointQuery(node << 1, l, mid, idx);
            else return this.pointQuery((node << 1) | 1, mid + 1, r, idx);
        }
        update(l: number, r: number, val: number): void {
            this.rangeUpdate(1, 0, this.n, l, r, val);
        }
        query(idx: number): number {
            return this.pointQuery(1, 0, this.n, idx);
        }
    }

    const seg = new SegTree(n);
    seg.update(0, 0, 0); // dp[0] = 0

    for (let i = 0; i < n; ++i) {
        const cur = seg.query(i);
        if (cur === INF) continue;
        let low = 1, high = Math.min(maxWordLen, n - i), best = 0;
        while (low <= high) {
            const mid = (low + high) >> 1;
            const set = prefixSets[mid];
            if (set) {
                const [h1, h2] = getHash(i, mid);
                const key = `${h1.toString()},${h2.toString()}`;
                if (set.has(key)) {
                    best = mid;
                    low = mid + 1;
                    continue;
                }
            }
            high = mid - 1;
        }
        if (best > 0) {
            seg.update(i + 1, i + best, cur + 1);
        }
    }

    const ans = seg.query(n);
    return ans === INF ? -1 : ans;
}
```

## Php

```php
class Solution {
    /**
     * @param String[] $words
     * @param String $target
     * @return Integer
     */
    function minValidStrings($words, $target) {
        $mod = 1000000007;
        $base = 91138233;

        // Build hash sets of prefixes grouped by length
        $hashSet = [];
        $maxWordLen = 0;
        foreach ($words as $w) {
            $h = 0;
            $lenW = strlen($w);
            for ($i = 0; $i < $lenW; $i++) {
                $c = ord($w[$i]) - 96; // a -> 1
                $h = (int)(($h * $base + $c) % $mod);
                $l = $i + 1;
                if (!isset($hashSet[$l])) $hashSet[$l] = [];
                $hashSet[$l][$h] = true;
            }
            if ($lenW > $maxWordLen) $maxWordLen = $lenW;
        }

        $n = strlen($target);
        // Prefix hashes and powers for target
        $pref = array_fill(0, $n + 1, 0);
        $pow  = array_fill(0, $n + 1, 1);
        for ($i = 0; $i < $n; $i++) {
            $c = ord($target[$i]) - 96;
            $pref[$i + 1] = (int)(($pref[$i] * $base + $c) % $mod);
            $pow[$i + 1]  = (int)(($pow[$i] * $base) % $mod);
        }

        // DSU for unvisited positions
        $parent = [];
        for ($i = 0; $i <= $n + 1; $i++) $parent[$i] = $i;
        $find = function($x) use (&$parent, &$find) {
            if ($parent[$x] != $x) {
                $parent[$x] = $find($parent[$x]);
            }
            return $parent[$x];
        };

        // BFS
        $dist = array_fill(0, $n + 1, -1);
        $queue = new SplQueue();
        $dist[0] = 0;
        $queue->enqueue(0);
        // mark position 0 as visited in DSU
        $parent[0] = $find(1);

        while (!$queue->isEmpty()) {
            $i = $queue->dequeue();
            if ($i == $n) break;

            $maxLen = $maxWordLen;
            if ($maxLen > $n - $i) $maxLen = $n - $i;
            $low = 1;
            $high = $maxLen;
            $best = 0;
            while ($low <= $high) {
                $mid = intdiv($low + $high, 2);
                // hash of target[i .. i+mid-1]
                $h = $pref[$i + $mid] - (int)(($pref[$i] * $pow[$mid]) % $mod);
                if ($h < 0) $h += $mod;
                if (isset($hashSet[$mid]) && isset($hashSet[$mid][$h])) {
                    $best = $mid;
                    $low = $mid + 1;
                } else {
                    $high = $mid - 1;
                }
            }

            if ($best == 0) continue;

            $j = $find($i + 1);
            while ($j <= $i + $best) {
                $dist[$j] = $dist[$i] + 1;
                $queue->enqueue($j);
                // remove j from unvisited set
                $parent[$j] = $find($j + 1);
                $j = $find($j);
            }
        }

        return $dist[$n];
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    func minValidStrings(_ words: [String], _ target: String) -> Int {
        let base: UInt64 = 91138233
        let tBytes = Array(target.utf8)
        let n = tBytes.count
        
        // Precompute powers and prefix hashes for target
        var powBase = [UInt64](repeating: 0, count: n + 1)
        var preHash = [UInt64](repeating: 0, count: n + 1)
        powBase[0] = 1
        for i in 0..<n {
            powBase[i + 1] = powBase[i] &* base
            preHash[i + 1] = preHash[i] &* base &+ UInt64(tBytes[i])
        }
        func getHash(_ l: Int, _ r: Int) -> UInt64 { // [l, r)
            return preHash[r] &- (preHash[l] &* powBase[r - l])
        }
        
        // Store hashes of all prefixes grouped by length
        var prefixSets = [Int: Set<UInt64>]()
        var maxWordLen = 0
        for w in words {
            let wBytes = Array(w.utf8)
            var h: UInt64 = 0
            for i in 0..<wBytes.count {
                h = h &* base &+ UInt64(wBytes[i])
                let len = i + 1
                prefixSets[len, default: Set<UInt64>()].insert(h)
            }
            maxWordLen = max(maxWordLen, wBytes.count)
        }
        
        // Compute longest match length L_i for each position i in target
        var L = [Int](repeating: 0, count: n)
        if !prefixSets.isEmpty {
            for i in 0..<n {
                var low = 0
                var high = min(maxWordLen, n - i)
                while low < high {
                    let mid = (low + high + 1) >> 1
                    if let set = prefixSets[mid] {
                        let h = getHash(i, i + mid)
                        if set.contains(h) {
                            low = mid
                        } else {
                            high = mid - 1
                        }
                    } else {
                        high = mid - 1
                    }
                }
                L[i] = low
            }
        }
        
        // Dijkstra/BFS with range relaxation using DSU for unvisited positions
        var dist = [Int](repeating: Int.max, count: n + 1)
        dist[0] = 0
        
        struct Heap {
            var data: [(Int, Int)] = []
            mutating func push(_ item: (Int, Int)) {
                data.append(item)
                siftUp(data.count - 1)
            }
            mutating func pop() -> (Int, Int)? {
                guard !data.isEmpty else { return nil }
                let res = data[0]
                data[0] = data[data.count - 1]
                data.removeLast()
                siftDown(0)
                return res
            }
            var isEmpty: Bool { data.isEmpty }
            mutating private func siftUp(_ idx: Int) {
                var i = idx
                while i > 0 {
                    let p = (i - 1) >> 1
                    if data[p].0 <= data[i].0 { break }
                    data.swapAt(p, i)
                    i = p
                }
            }
            mutating private func siftDown(_ idx: Int) {
                var i = idx
                while true {
                    let l = i * 2 + 1
                    let r = l + 1
                    var smallest = i
                    if l < data.count && data[l].0 < data[smallest].0 { smallest = l }
                    if r < data.count && data[r].0 < data[smallest].0 { smallest = r }
                    if smallest == i { break }
                    data.swapAt(i, smallest)
                    i = smallest
                }
            }
        }
        
        var heap = Heap()
        heap.push((0, 0))
        
        // DSU "next" array to skip visited indices
        var parent = Array(0...n+1) // size n+2
        func find(_ x: Int) -> Int {
            var v = x
            while parent[v] != v {
                parent[v] = parent[parent[v]]
                v = parent[v]
            }
            return v
        }
        func erase(_ x: Int) {
            parent[x] = find(x + 1)
        }
        
        // Initially all positions 1..n are unvisited
        for i in 0...n { parent[i] = i }
        parent[n+1] = n+1
        
        while let (d, pos) = heap.pop() {
            if d != dist[pos] { continue }
            if pos == n { break }
            let reach = min(n, pos + L[pos])
            var j = find(pos + 1)
            while j <= reach {
                if dist[j] > d + 1 {
                    dist[j] = d + 1
                    heap.push((dist[j], j))
                }
                erase(j)
                j = find(j)
            }
        }
        
        return dist[n] == Int.max ? -1 : dist[n]
    }
}
```

## Kotlin

```kotlin
import java.util.PriorityQueue

class Solution {
    private const val MOD1 = 1_000_000_007L
    private const val MOD2 = 1_000_000_009L
    private const val BASE = 91138233L
    private const val INF = 1_000_000_000

    fun minValidStrings(words: Array<String>, target: String): Int {
        val n = target.length
        var maxWordLen = 0
        for (w in words) if (w.length > maxWordLen) maxWordLen = w.length

        // hash sets per length
        val prefixSets = Array(maxWordLen + 1) { HashSet<Long>() }
        for (w in words) {
            var h1 = 0L
            var h2 = 0L
            for (i in w.indices) {
                val c = (w[i] - 'a' + 1).toLong()
                h1 = (h1 * BASE + c) % MOD1
                h2 = (h2 * BASE + c) % MOD2
                val combined = (h1 shl 32) xor h2
                prefixSets[i + 1].add(combined)
            }
        }

        // precompute powers
        val pow1 = LongArray(n + 1)
        val pow2 = LongArray(n + 1)
        pow1[0] = 1L
        pow2[0] = 1L
        for (i in 1..n) {
            pow1[i] = (pow1[i - 1] * BASE) % MOD1
            pow2[i] = (pow2[i - 1] * BASE) % MOD2
        }

        // prefix hashes of target
        val pref1 = LongArray(n + 1)
        val pref2 = LongArray(n + 1)
        for (i in 0 until n) {
            val c = (target[i] - 'a' + 1).toLong()
            pref1[i + 1] = (pref1[i] * BASE + c) % MOD1
            pref2[i + 1] = (pref2[i] * BASE + c) % MOD2
        }

        fun getHash(l: Int, r: Int): Long {
            val len = r - l
            var h1 = pref1[r] - (pref1[l] * pow1[len] % MOD1)
            if (h1 < 0) h1 += MOD1
            var h2 = pref2[r] - (pref2[l] * pow2[len] % MOD2)
            if (h2 < 0) h2 += MOD2
            return (h1 shl 32) xor h2
        }

        // compute longest match length for each start position
        val maxLenFrom = IntArray(n)
        for (i in 0 until n) {
            var low = 1
            var high = kotlin.math.min(maxWordLen, n - i)
            var best = 0
            while (low <= high) {
                val mid = (low + high) ushr 1
                if (prefixSets[mid].isEmpty()) {
                    high = mid - 1
                    continue
                }
                val h = getHash(i, i + mid)
                if (prefixSets[mid].contains(h)) {
                    best = mid
                    low = mid + 1
                } else {
                    high = mid - 1
                }
            }
            maxLenFrom[i] = best
        }

        // DP with active range min using priority queue
        val dp = IntArray(n + 1) { INF }
        dp[0] = 0

        data class Node(val value: Int, val expire: Int)

        val pq = PriorityQueue<Node>(compareBy { it.value })
        // process positions
        for (i in 0 until n) {
            if (dp[i] < INF && maxLenFrom[i] > 0) {
                val cand = dp[i] + 1
                val expirePos = i + maxLenFrom[i]
                pq.offer(Node(cand, expirePos))
            }
            // remove expired contributions for position i+1
            while (pq.isNotEmpty() && pq.peek().expire < i + 1) {
                pq.poll()
            }
            if (pq.isNotEmpty()) {
                dp[i + 1] = kotlin.math.min(dp[i + 1], pq.peek().value)
            }
        }

        return if (dp[n] >= INF) -1 else dp[n]
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  static const int MOD1 = 1000000007;
  static const int MOD2 = 1000000009;
  static const int BASE = 91138233;
  static const int INF = 1 << 60;

  int minValidStrings(List<String> words, String target) {
    final int n = target.length;
    // precompute powers
    List<int> pow1 = List.filled(n + 1, 0);
    List<int> pow2 = List.filled(n + 1, 0);
    pow1[0] = 1;
    pow2[0] = 1;
    for (int i = 1; i <= n; ++i) {
      pow1[i] = (pow1[i - 1] * BASE) % MOD1;
      pow2[i] = (pow2[i - 1] * BASE) % MOD2;
    }
    // prefix hashes of target
    List<int> pref1 = List.filled(n + 1, 0);
    List<int> pref2 = List.filled(n + 1, 0);
    for (int i = 0; i < n; ++i) {
      int val = target.codeUnitAt(i) - 96;
      pref1[i + 1] = (pref1[i] * BASE + val) % MOD1;
      pref2[i + 1] = (pref2[i] * BASE + val) % MOD2;
    }

    // collect all prefix hashes from words
    final Set<int> validHashes = HashSet();
    for (String w in words) {
      int h1 = 0, h2 = 0;
      for (int i = 0; i < w.length; ++i) {
        int val = w.codeUnitAt(i) - 96;
        h1 = (h1 * BASE + val) % MOD1;
        h2 = (h2 * BASE + val) % MOD2;
        validHashes.add((h1 << 32) | h2);
      }
    }

    // helper to get combined hash of substring [l, l+len)
    int getHash(int l, int len) {
      int r = l + len;
      int h1 = pref1[r] - (pref1[l] * pow1[len]) % MOD1;
      if (h1 < 0) h1 += MOD1;
      int h2 = pref2[r] - (pref2[l] * pow2[len]) % MOD2;
      if (h2 < 0) h2 += MOD2;
      return (h1 << 32) | h2;
    }

    bool hasHash(int start, int len) {
      return validHashes.contains(getHash(start, len));
    }

    // segment tree for range chmin and point query
    final SegTree seg = SegTree(n + 1);
    seg.pointUpdate(0, 0);

    for (int i = 0; i < n; ++i) {
      int cur = seg.pointQuery(i);
      if (cur >= INF) continue;

      // binary search longest length starting at i
      int low = 0;
      int high = n - i;
      while (low < high) {
        int mid = (low + high + 1) >> 1;
        if (hasHash(i, mid)) {
          low = mid;
        } else {
          high = mid - 1;
        }
      }
      int maxLen = low;
      if (maxLen == 0) continue;

      int l = i + 1;
      int r = i + maxLen;
      seg.rangeChmin(l, r, cur + 1);
    }

    int ans = seg.pointQuery(n);
    return ans >= INF ? -1 : ans;
  }
}

class SegTree {
  final List<int> _min;
  final List<int> _lazy;
  final int _size;

  SegTree(int n)
      : _size = n,
        _min = List.filled(4 * n + 5, Solution.INF),
        _lazy = List.filled(4 * n + 5, Solution.INF);

  void _apply(int node, int val) {
    if (val < _min[node]) _min[node] = val;
    if (val < _lazy[node]) _lazy[node] = val;
  }

  void _push(int node) {
    if (_lazy[node] == Solution.INF) return;
    _apply(node << 1, _lazy[node]);
    _apply((node << 1) | 1, _lazy[node]);
    _lazy[node] = Solution.INF;
  }

  void rangeChmin(int l, int r, int val) {
    _rangeChmin(1, 0, _size - 1, l, r, val);
  }

  void _rangeChmin(int node, int nl, int nr, int ql, int qr, int val) {
    if (ql > nr || qr < nl) return;
    if (ql <= nl && nr <= qr) {
      _apply(node, val);
      return;
    }
    _push(node);
    int mid = (nl + nr) >> 1;
    _rangeChmin(node << 1, nl, mid, ql, qr, val);
    _rangeChmin((node << 1) | 1, mid + 1, nr, ql, qr, val);
    _min[node] = _min[node << 1] < _min[(node << 1) | 1]
        ? _min[node << 1]
        : _min[(node << 1) | 1];
  }

  void pointUpdate(int idx, int val) {
    rangeChmin(idx, idx, val);
  }

  int pointQuery(int idx) {
    return _pointQuery(1, 0, _size - 1, idx);
  }

  int _pointQuery(int node, int nl, int nr, int idx) {
    if (nl == nr) return _min[node];
    _push(node);
    int mid = (nl + nr) >> 1;
    if (idx <= mid) {
      return _pointQuery(node << 1, nl, mid, idx);
    } else {
      return _pointQuery((node << 1) | 1, mid + 1, nr, idx);
    }
  }
}
```

## Golang

```go
func minValidStrings(words []string, target string) int {
	const INF = int(1e9)
	n := len(target)

	// Find maximum word length
	maxW := 0
	for _, w := range words {
		if len(w) > maxW {
			maxW = len(w)
		}
	}

	// Rolling hash base (random odd)
	var base uint64 = 91138233

	// Precompute powers up to max(n, maxW)
	maxLen := n
	if maxW > maxLen {
		maxLen = maxW
	}
	pow := make([]uint64, maxLen+1)
	pow[0] = 1
	for i := 1; i <= maxLen; i++ {
		pow[i] = pow[i-1] * base
	}

	// Store all prefix hashes grouped by length
	prefixSets := make([]map[uint64]struct{}, maxW+1)
	for _, w := range words {
		var h uint64 = 0
		for i, ch := range w {
			h = h*base + uint64(ch-'a'+1)
			l := i + 1
			if prefixSets[l] == nil {
				prefixSets[l] = make(map[uint64]struct{})
			}
			prefixSets[l][h] = struct{}{}
		}
	}

	// Prefix hashes for target
	targetHash := make([]uint64, n+1)
	for i := 0; i < n; i++ {
		targetHash[i+1] = targetHash[i]*base + uint64(target[i]-'a'+1)
	}

	// Compute maxLenAtPos using binary search
	maxLenAtPos := make([]int, n)
	for i := 0; i < n; i++ {
		low, high := 0, maxW
		if remaining := n - i; high > remaining {
			high = remaining
		}
		for low < high {
			mid := (low + high + 1) >> 1
			if prefixSets[mid] == nil {
				high = mid - 1
				continue
			}
			hash := targetHash[i+mid] - targetHash[i]*pow[mid]
			if _, ok := prefixSets[mid][hash]; ok {
				low = mid
			} else {
				high = mid - 1
			}
		}
		maxLenAtPos[i] = low
	}

	// DP using min-heap of active intervals
	type item struct {
		val int // dp + 1
		end int // inclusive end position reachable
	}
	h := &minHeap{}
	heapInit(h)

	dp := make([]int, n+1)
	for i := range dp {
		dp[i] = INF
	}
	dp[0] = 0

	if maxLenAtPos[0] > 0 {
		heapPush(h, item{val: dp[0] + 1, end: 0 + maxLenAtPos[0]})
	}

	for pos := 1; pos <= n; pos++ {
		// discard intervals that cannot reach current position
		for h.Len() > 0 && (*h)[0].end < pos {
			heapPop(h)
		}
		if h.Len() > 0 {
			dp[pos] = (*h)[0].val
		}
		if pos < n && maxLenAtPos[pos] > 0 && dp[pos] < INF {
			heapPush(h, item{val: dp[pos] + 1, end: pos + maxLenAtPos[pos]})
		}
	}

	if dp[n] >= INF {
		return -1
	}
	return dp[n]
}

// ---------- min-heap implementation ----------
type minHeap []item

func heapInit(h *minHeap) { heap.Init(h) }
func heapPush(h *minHeap, it item) { heap.Push(h, it) }
func heapPop(h *minHeap) item { return heap.Pop(h).(item) }

func (h minHeap) Len() int           { return len(h) }
func (h minHeap) Less(i, j int) bool {
	if h[i].val == h[j].val {
		return h[i].end < h[j].end
	}
	return h[i].val < h[j].val
}
func (h minHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *minHeap) Push(x interface{}) { *h = append(*h, x.(item)) }
func (h *minHeap) Pop() interface{} {
	old := *h
	n := len(old)
	it := old[n-1]
	*h = old[:n-1]
	return it
}
import "container/heap"
```

## Ruby

```ruby
require 'set'

# @param {String[]} words
# @param {String} target
# @return {Integer}
def min_valid_strings(words, target)
  n = target.length
  max_len = 0
  words.each { |w| max_len = [max_len, w.length].max }

  mod1 = 1_000_000_007
  mod2 = 1_000_000_009
  base = 91138233

  # prefix hash sets for each length
  pref_hashes = Array.new(max_len + 1) { Set.new }

  words.each do |w|
    h1 = 0
    h2 = 0
    w.each_char.with_index(1) do |ch, idx|
      val = ch.ord - 96
      h1 = (h1 * base + val) % mod1
      h2 = (h2 * base + val) % mod2
      pref_hashes[idx] << ((h1 << 32) ^ h2)
    end
  end

  # rolling hash for target
  pow1 = Array.new(n + 1, 0)
  pow2 = Array.new(n + 1, 0)
  pow1[0] = 1
  pow2[0] = 1
  (1..n).each do |i|
    pow1[i] = (pow1[i - 1] * base) % mod1
    pow2[i] = (pow2[i - 1] * base) % mod2
  end

  pref1 = Array.new(n + 1, 0)
  pref2 = Array.new(n + 1, 0)
  target.each_char.with_index do |ch, i|
    val = ch.ord - 96
    pref1[i + 1] = (pref1[i] * base + val) % mod1
    pref2[i + 1] = (pref2[i] * base + val) % mod2
  end

  get_hash = lambda do |l, len|
    r = l + len
    h1 = (pref1[r] - (pref1[l] * pow1[len]) % mod1) % mod1
    h2 = (pref2[r] - (pref2[l] * pow2[len]) % mod2) % mod2
    ((h1 << 32) ^ h2)
  end

  # DSU for next unvisited index
  parent = Array.new(n + 2) { |i| i } # extra sentinel at n+1
  find = lambda do |x|
    while parent[x] != x
      parent[x] = parent[parent[x]]
      x = parent[x]
    end
    x
  end

  dist = Array.new(n + 1, -1)
  queue = []
  head = 0
  dist[0] = 0
  queue << 0
  parent[0] = find.call(1) # mark 0 as visited

  while head < queue.size
    i = queue[head]
    head += 1
    max_possible = [max_len, n - i].min
    low = 0
    high = max_possible
    while low < high
      mid = (low + high + 1) >> 1
      h = get_hash.call(i, mid)
      if pref_hashes[mid].include?(h)
        low = mid
      else
        high = mid - 1
      end
    end
    lmax = low
    next_idx = find.call(i + 1)
    while next_idx <= i + lmax && next_idx <= n
      dist[next_idx] = dist[i] + 1
      queue << next_idx
      parent[next_idx] = find.call(next_idx + 1) # mark visited
      next_idx = find.call(next_idx)
    end
  end

  dist[n]
end
```

## Scala

```scala
import scala.collection.mutable

object Solution {
  def minValidStrings(words: Array[String], target: String): Int = {
    val MOD1 = 1000000007
    val MOD2 = 1000000009
    val BASE = 91138233L

    val maxWordLen = words.map(_.length).maxOption.getOrElse(0)
    val n = target.length

    // hash sets for each length
    val sets = Array.fill(maxWordLen + 1)(mutable.HashSet[Long]())

    def combine(h1: Int, h2: Int): Long = {
      (h1.toLong << 32) | (h2 & 0xffffffffL)
    }

    // insert all prefixes of words
    for (w <- words) {
      var h1 = 0L
      var h2 = 0L
      var len = 0
      for (ch <- w) {
        val v = (ch - 'a' + 1).toLong
        h1 = (h1 * BASE + v) % MOD1
        h2 = (h2 * BASE + v) % MOD2
        len += 1
        sets(len).add(combine(h1.toInt, h2.toInt))
      }
    }

    // prefix hashes for target
    val pref1 = new Array[Int](n + 1)
    val pref2 = new Array[Int](n + 1)
    val pow1 = new Array[Int](n + 1)
    val pow2 = new Array[Int](n + 1)
    pow1(0) = 1
    pow2(0) = 1
    for (i <- 0 until n) {
      val v = (target.charAt(i) - 'a' + 1).toLong
      pref1(i + 1) = ((pref1(i).toLong * BASE + v) % MOD1).toInt
      pref2(i + 1) = ((pref2(i).toLong * BASE + v) % MOD2).toInt
      pow1(i + 1) = ((pow1(i).toLong * BASE) % MOD1).toInt
      pow2(i + 1) = ((pow2(i).toLong * BASE) % MOD2).toInt
    }

    def getHash(l: Int, r: Int): Long = {
      // substring [l, r)
      val len = r - l
      var h1 = pref1(r) - (pref1(l).toLong * pow1(len) % MOD1).toInt
      if (h1 < 0) h1 += MOD1
      var h2 = pref2(r) - (pref2(l).toLong * pow2(len) % MOD2).toInt
      if (h2 < 0) h2 += MOD2
      combine(h1, h2)
    }

    // farthest reachable index from each position
    val farthest = new Array[Int](n)
    for (i <- 0 until n) {
      var lo = 1
      var hi = math.min(maxWordLen, n - i)
      var best = 0
      while (lo <= hi) {
        val mid = (lo + hi) >>> 1
        if (sets(mid).contains(getHash(i, i + mid))) {
          best = mid
          lo = mid + 1
        } else {
          hi = mid - 1
        }
      }
      farthest(i) = i + best
    }

    // greedy jump game II
    var steps = 0
    var currentEnd = 0
    var furthestReach = 0
    for (i <- 0 until n) {
      if (i > furthestReach) return -1
      furthestReach = math.max(furthestReach, farthest(i))
      if (i == currentEnd) {
        steps += 1
        currentEnd = furthestReach
        if (currentEnd >= n) return steps
      }
    }
    if (currentEnd >= n) steps else -1
  }
}
```

## Rust

```rust
use std::collections::HashSet;

const INF: i32 = 1_000_000_000;
const BASE1: u64 = 91138233;
const BASE2: u64 = 97266353;

struct SegmentTree {
    size: usize,
    tree: Vec<i32>,
    lazy: Vec<i32>,
}

impl SegmentTree {
    fn new(n: usize) -> Self {
        let mut size = 1usize;
        while size < n {
            size <<= 1;
        }
        SegmentTree {
            size,
            tree: vec![INF; size * 2],
            lazy: vec![INF; size * 2],
        }
    }

    #[inline]
    fn apply(&mut self, node: usize, val: i32) {
        if self.tree[node] > val {
            self.tree[node] = val;
        }
        if self.lazy[node] > val {
            self.lazy[node] = val;
        }
    }

    #[inline]
    fn push(&mut self, node: usize) {
        let v = self.lazy[node];
        if v != INF {
            self.apply(node << 1, v);
            self.apply(node << 1 | 1, v);
            self.lazy[node] = INF;
        }
    }

    fn range_chmin_rec(
        &mut self,
        node: usize,
        l: usize,
        r: usize,
        ql: usize,
        qr: usize,
        val: i32,
    ) {
        if ql > r || qr < l {
            return;
        }
        if ql <= l && r <= qr {
            self.apply(node, val);
            return;
        }
        self.push(node);
        let mid = (l + r) >> 1;
        self.range_chmin_rec(node << 1, l, mid, ql, qr, val);
        self.range_chmin_rec(node << 1 | 1, mid + 1, r, ql, qr, val);
        self.tree[node] = self.tree[node << 1].min(self.tree[node << 1 | 1]);
    }

    fn range_chmin(&mut self, l: usize, r: usize, val: i32) {
        if l > r {
            return;
        }
        self.range_chmin_rec(1, 0, self.size - 1, l, r, val);
    }

    fn point_query_rec(&mut self, node: usize, l: usize, r: usize, idx: usize) -> i32 {
        if l == r {
            return self.tree[node];
        }
        self.push(node);
        let mid = (l + r) >> 1;
        if idx <= mid {
            self.point_query_rec(node << 1, l, mid, idx)
        } else {
            self.point_query_rec(node << 1 | 1, mid + 1, r, idx)
        }
    }

    fn point_query(&mut self, idx: usize) -> i32 {
        self.point_query_rec(1, 0, self.size - 1, idx)
    }
}

pub struct Solution;

impl Solution {
    pub fn min_valid_strings(words: Vec<String>, target: String) -> i32 {
        // collect all prefix hashes
        let mut set: HashSet<u128> = HashSet::new();
        for w in words.iter() {
            let bytes = w.as_bytes();
            let mut h1: u64 = 0;
            let mut h2: u64 = 0;
            for &c in bytes {
                let v = (c - b'a' + 1) as u64;
                h1 = h1.wrapping_mul(BASE1).wrapping_add(v);
                h2 = h2.wrapping_mul(BASE2).wrapping_add(v);
                let combined = ((h1 as u128) << 64) | (h2 as u128);
                set.insert(combined);
            }
        }

        let n = target.len();
        let tbytes = target.as_bytes();

        // prefix hashes for target
        let mut pref1 = vec![0u64; n + 1];
        let mut pref2 = vec![0u64; n + 1];
        for i in 0..n {
            let v = (tbytes[i] - b'a' + 1) as u64;
            pref1[i + 1] = pref1[i].wrapping_mul(BASE1).wrapping_add(v);
            pref2[i + 1] = pref2[i].wrapping_mul(BASE2).wrapping_add(v);
        }

        // powers
        let mut pow1 = vec![1u64; n + 1];
        let mut pow2 = vec![1u64; n + 1];
        for i in 1..=n {
            pow1[i] = pow1[i - 1].wrapping_mul(BASE1);
            pow2[i] = pow2[i - 1].wrapping_mul(BASE2);
        }

        // helper to get hash of substring [l, r)
        let get_hash = |l: usize, r: usize| -> u128 {
            let len = r - l;
            let mut h1 = pref1[r];
            let mul1 = pref1[l].wrapping_mul(pow1[len]);
            h1 = h1.wrapping_sub(mul1);
            let mut h2 = pref2[r];
            let mul2 = pref2[l].wrapping_mul(pow2[len]);
            h2 = h2.wrapping_sub(mul2);
            ((h1 as u128) << 64) | (h2 as u128)
        };

        // compute max valid length starting at each position
        let mut max_len = vec![0usize; n];
        for i in 0..n {
            let mut low = 0usize;
            let mut high = n - i;
            while low < high {
                let mid = (low + high + 1) >> 1;
                if set.contains(&get_hash(i, i + mid)) {
                    low = mid;
                } else {
                    high = mid - 1;
                }
            }
            max_len[i] = low;
        }

        // DP with segment tree
        let mut seg = SegmentTree::new(n + 1);
        seg.range_chmin(0, 0, 0);

        for i in 0..n {
            let cur = seg.point_query(i);
            if cur == INF {
                continue;
            }
            let len = max_len[i];
            if len == 0 {
                continue;
            }
            let l = i + 1;
            let r = std::cmp::min(n, i + len);
            seg.range_chmin(l, r, cur + 1);
        }

        let ans = seg.point_query(n);
        if ans >= INF / 2 { -1 } else { ans }
    }
}
```

## Racket

```racket
(define INF 1000000000)

;; rolling hash parameters
(define BASE 91138233)
(define MOD 1000000007)

;; compute integer code for a character ('a' -> 1, ... 'z' -> 26)
(define (char-code c)
  (+ (- (char->integer c) (char->integer #\a)) 1))

;; main function
(define/contract (min-valid-strings words target)
  (-> (listof string?) string? exact-integer?)
  (let* ((n (string-length target))
         ;; map length -> hash table of prefix hashes of that length
         (len-map (make-hash))
         (max-pref-len 0))

    ;; process all words, store every prefix hash
    (for ([w words])
      (let ((m (string-length w)))
        (set! max-pref-len (max max-pref-len m))
        (let loop ((i 0) (h 0))
          (when (< i m)
            (let* ((c (char-code (string-ref w i)))
                   (new-h (modulo (+ (* h BASE) c) MOD))
                   (len (+ i 1))
                   (set-hash (hash-ref len-map len
                                      (lambda ()
                                        (let ((s (make-hash)))
                                          (hash-set! len-map len s)
                                          s)))))
              (hash-set! set-hash new-h #t)
              (loop (+ i 1) new-h))))))

    ;; precompute powers of BASE modulo MOD
    (define pow (make-vector (+ n 1) 0))
    (vector-set! pow 0 1)
    (for ([i (in-range 1 (+ n 1))])
      (vector-set! pow i (modulo (* (vector-ref pow (- i 1)) BASE) MOD)))

    ;; prefix hashes of target
    (define pref (make-vector (+ n 1) 0))
    (for ([i (in-range n)])
      (let* ((c (char-code (string-ref target i)))
             (new-h (modulo (+ (* (vector-ref pref i) BASE) c) MOD)))
        (vector-set! pref (+ i 1) new-h)))

    ;; helper to get hash of substring [l, l+len)
    (define (subhash l len)
      (let* ((h1 (vector-ref pref (+ l len)))
             (h2 (vector-ref pref l))
             (val (- h1 (* h2 (vector-ref pow len)))))
        (modulo val MOD)))

    ;; segment tree for range chmin and point query
    (define size
      (let loop ((s 1))
        (if (>= s (+ n 1)) s (loop (* s 2)))))
    (define tree (make-vector (* 2 size) INF))
    (define lazy (make-vector (* 2 size) INF))

    (define (apply node val)
      (vector-set! tree node (min (vector-ref tree node) val))
      (vector-set! lazy node (min (vector-ref lazy node) val)))

    (define (push node)
      (let ((lz (vector-ref lazy node)))
        (when (< lz INF)
          (apply (* node 2) lz)
          (apply (+ (* node 2) 1) lz)
          (vector-set! lazy node INF))))

    (define (range-update l r val node nl nr)
      (cond
        [(or (> l nl) (< r nr)) ; no overlap
         (void)]
        [(and (<= l nl) (>= r nr)) ; total cover
         (apply node val)]
        [else
         (push node)
         (let ((mid (quotient (+ nl nr) 2)))
           (range-update l r val (* node 2) nl mid)
           (range-update l r val (+ (* node 2) 1) (+ mid 1) nr)
           (vector-set! tree node
                        (min (vector-ref tree (* node 2))
                             (vector-ref tree (+ (* node 2) 1)))))]))

    (define (point-query idx node nl nr)
      (if (= nl nr)
          (vector-ref tree node)
          (begin
            (push node)
            (let ((mid (quotient (+ nl nr) 2)))
              (if (<= idx mid)
                  (point-query idx (* node 2) nl mid)
                  (point-query idx (+ (* node 2) 1) (+ mid 1) nr))))))

    ;; set dp[0] = 0
    (range-update 0 0 0 1 0 (- size 1))

    ;; main DP loop
    (for ([i (in-range n)])
      (let ((cur (point-query i 1 0 (- size 1))))
        (when (< cur INF)
          (define max-possible (min max-pref-len (- n i)))
          ;; binary search longest length where prefix exists
          (let loop ((lo 0) (hi max-possible))
            (if (= lo hi)
                (let ((Lmax lo))
                  (when (> Lmax 0)
                    (range-update (+ i 1) (+ i Lmax) (+ cur 1) 1 0 (- size 1))))
                (let* ((mid (quotient (+ lo hi) 2))
                       (len (+ mid 1))) ; try length = mid+1
                  (if (> len max-possible)
                      (loop lo mid)
                      (let ((h (subhash i len))
                            (set-hash (hash-ref len-map len #f)))
                        (if (and set-hash (hash-has-key? set-hash h))
                            (loop (+ lo 1) hi) ; can go higher
                            (loop lo mid))))))))))
    (let ((ans (point-query n 1 0 (- size 1))))
      (if (< ans INF) ans -1)))
```

## Erlang

```erlang
-spec min_valid_strings(Words :: [unicode:unicode_binary()], Target :: unicode:unicode_binary()) -> integer().
min_valid_strings(Words, Target) ->
    Base = 91138233,
    Mod = 1000000007,

    %% Build prefix hash map and maximum word length
    {PrefixMap, MaxWordLen} = build_prefix_map(Words, Base, Mod, #{}, 0),

    N = byte_size(Target),

    %% Precompute powers up to MaxWordLen
    PowMap = build_pow_map(MaxWordLen, Base, Mod, #{0 => 1}),
    %% Prefix hashes of target (pref[0]=0)
    PrefMap = build_pref_hashes(binary_to_list(Target), Base, Mod, #{0 => 0}, 0),

    %% Compute maximal reachable length from each position
    LmaxList = [calc_max_len(Pos, N, MaxWordLen, PrefixMap, PowMap, PrefMap, Base, Mod) ||
                Pos <- lists:seq(0, N-1)],
    LmaxMap = maps:from_list(lists:zip(lists:seq(0, N-1), LmaxList)),

    %% BFS with DSU (union‑find) to skip visited indices
    Dist0 = #{0 => 0},
    Parent0 = init_parent(N + 1),
    Q0 = queue:new(),
    Q = queue:in(0, Q0),

    bfs(Q, Dist0, Parent0, LmaxMap, N, Base, Mod).

%% Build map Length -> Set of prefix hashes
build_prefix_map([], _Base, _Mod, Map, Max) ->
    {Map, Max};
build_prefix_map([W | Rest], Base, Mod, MapAcc, MaxAcc) ->
    Bytes = binary_to_list(W),
    {NewMap, NewMax} = add_word_prefixes(Bytes, 1, 0, Base, Mod, MapAcc, MaxAcc),
    build_prefix_map(Rest, Base, Mod, NewMap, NewMax).

add_word_prefixes([], _Len, _Hash, _Base, _Mod, Map, Max) ->
    {Map, Max};
add_word_prefixes([C | Cs], Len, PrevHash, Base, Mod, MapAcc, MaxAcc) ->
    Char = C - $a + 1,
    Hash = (PrevHash * Base + Char) rem Mod,
    Set0 = maps:get(Len, MapAcc, #{}),
    Set = maps:put(Hash, true, Set0),
    NewMap = maps:put(Len, Set, MapAcc),
    add_word_prefixes(Cs, Len + 1, Hash, Base, Mod, NewMap, max(MaxAcc, Len)).

%% Powers of base modulo Mod
build_pow_map(0, _Base, _Mod, Pow) -> Pow;
build_pow_map(N, Base, Mod, Pow) ->
    build_pow_map(1, N, Base, Mod, Pow).

build_pow_map(Cur, Max, Base, Mod, Map) when Cur =< Max ->
    Prev = maps:get(Cur - 1, Map),
    Val = (Prev * Base) rem Mod,
    NewMap = maps:put(Cur, Val, Map),
    build_pow_map(Cur + 1, Max, Base, Mod, NewMap);
build_pow_map(_, _, _, _, Map) -> Map.

%% Prefix hashes of target string
build_pref_hashes([], _Base, _Mod, Pref, _Idx) ->
    Pref;
build_pref_hashes([C | Cs], Base, Mod, PrefAcc, Idx) ->
    Char = C - $a + 1,
    PrevHash = maps:get(Idx, PrefAcc),
    NewHash = (PrevHash * Base + Char) rem Mod,
    NewPref = maps:put(Idx + 1, NewHash, PrefAcc),
    build_pref_hashes(Cs, Base, Mod, NewPref, Idx + 1).

%% Max length of a valid prefix starting at Pos
calc_max_len(Pos, N, MaxWordLen, PrefixMap, PowMap, PrefMap, Base, Mod) ->
    MaxPossible = min(MaxWordLen, N - Pos),
    binary_search(1, MaxPossible, 0, Pos, PrefixMap, PowMap, PrefMap, Mod).

binary_search(Low, High, Best, _Pos, _PMap, _Pow, _Pref, _Mod) when Low > High ->
    Best;
binary_search(Low, High, Best, Pos, PMap, Pow, Pref, Mod) ->
    Mid = (Low + High) div 2,
    Hash = substring_hash(Pos, Mid, Pow, Pref, Mod),
    case prefix_exists(Mid, Hash, PMap) of
        true -> binary_search(Mid + 1, High, Mid, Pos, PMap, Pow, Pref, Mod);
        false -> binary_search(Low, Mid - 1, Best, Pos, PMap, Pow, Pref, Mod)
    end.

substring_hash(Pos, Len, Pow, Pref, Mod) ->
    H1 = maps:get(Pos + Len, Pref),
    H0 = maps:get(Pos, Pref),
    PowLen = maps:get(Len, Pow),
    Raw = (H1 - (H0 * PowLen) rem Mod),
    if Raw < 0 -> Raw + Mod; true -> Raw end.

prefix_exists(Len, Hash, PMap) ->
    case maps:find(Len, PMap) of
        error -> false;
        {ok, Set} -> maps:is_key(Hash, Set)
    end.

%% Initialize union‑find parent map (each index points to itself)
init_parent(Upper) ->
    init_parent(0, Upper, #{}).

init_parent(I, Upper, Acc) when I =< Upper ->
    init_parent(I + 1, Upper, maps:put(I, I, Acc));
init_parent(_, _, Acc) -> Acc.

%% BFS using queue and DSU to skip already visited positions
bfs(Queue, DistMap, ParentMap, LmaxMap, N, Base, Mod) ->
    case queue:out(Queue) of
        {empty, _} ->
            case maps:get(N, DistMap, -1) of
                -1 -> -1;
                D -> D
            end;
        {{value, Pos}, QRest} ->
            CurDist = maps:get(Pos, DistMap),
            MaxReach = case maps:find(Pos, LmaxMap) of
                           error -> 0;
                           {ok, V} -> V
                       end,
            Limit = min(N, Pos + MaxReach),
            {NewParent, NewDist, NewQueue} =
                process_range(Pos + 1, Limit, CurDist + 1, DistMap, ParentMap, QRest),
            bfs(NewQueue, NewDist, NewParent, LmaxMap, N, Base, Mod)
    end.

process_range(CurIdx, Limit, NewDist, DistMap, ParentMap, Queue) when CurIdx =< Limit ->
    {Root, P1} = find(CurIdx, ParentMap),
    if Root > Limit ->
            {P1, DistMap, Queue};
       true ->
            D2 = maps:put(Root, NewDist, DistMap),
            Q2 = queue:in(Root, Queue),
            {NextRoot, P2} = find(Root + 1, P1),
            P3 = maps:put(Root, NextRoot, P2),
            process_range(CurIdx, Limit, NewDist, D2, P3, Q2)
    end;
process_range(_, _, _, DistMap, ParentMap, Queue) ->
    {ParentMap, DistMap, Queue}.

find(Index, ParentMap) ->
    Parent = maps:get(Index, ParentMap),
    if Parent == Index ->
            {Index, ParentMap};
       true ->
            {Root, NewMap} = find(Parent, ParentMap),
            Updated = maps:put(Index, Root, NewMap),
            {Root, Updated}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_valid_strings(words :: [String.t()], target :: String.t()) :: integer
  def min_valid_strings(words, target) do
    base = 91138233
    mod = 1_000_000_007

    # Build map: length => set of prefix hashes, and find max word length
    {len_map, max_word_len} = build_prefix_sets(words, base, mod)

    # Prepare target char list and its rolling hash + powers
    t_chars = String.to_charlist(target)
    n = length(t_chars)
    {pref_hash, pow} = compute_hashes(t_chars, base, mod)

    # Compute longest match length for each start position
    lens_arr =
      0..(n - 1)
      |> Enum.reduce(:array.new(n, default: 0), fn i, arr ->
        max_possible = min(max_word_len, n - i)

        l = longest_match(i, max_possible, pref_hash, pow, len_map, mod)
        :array.set(i, l, arr)
      end)

    # Initialize DSU parent array (next unvisited pointer)
    parent =
      0..(n + 1)
      |> Enum.reduce(:array.new(n + 2, default: 0), fn i, a -> :array.set(i, i, a) end)

    # Distance array, -1 means unreachable
    dist = :array.set(0, 0, :array.new(n + 1, default: -1))
    queue = :queue.in(0, :queue.new())

    {parent, dist, _queue} =
      bfs(queue, parent, dist, lens_arr, n, pref_hash, pow, len_map, base, mod)

    ans = :array.get(n, dist)
    if ans == -1, do: -1, else: ans
  end

  # Build prefix hash sets per length
  defp build_prefix_sets(words, base, mod) do
    Enum.reduce(words, {%{}, 0}, fn w, {map, max_len} ->
      chars = String.to_charlist(w)

      {new_map, _h, len} =
        Enum.reduce(chars, {map, 0, 0}, fn ch, {m, h, l} ->
          nh = rem(h * base + (ch - ?a + 1), mod)
          nl = l + 1
          m2 = Map.update(m, nl, MapSet.new([nh]), &MapSet.put(&1, nh))
          {m2, nh, nl}
        end)

      {new_map, max(max_len, length(chars))}
    end)
  end

  # Compute rolling hash and powers for a char list
  defp compute_hashes(chars, base, mod) do
    n = length(chars)

    pow =
      0..n
      |> Enum.reduce(:array.new(n + 1, default: 0), fn i, arr ->
        val = if i == 0, do: 1, else: rem(:array.get(i - 1, arr) * base, mod)
        :array.set(i, val, arr)
      end)

    pref_hash =
      chars
      |> Enum.with_index()
      |> Enum.reduce(:array.new(n + 1, default: 0), fn {ch, idx}, arr ->
        prev = :array.get(idx, arr)
        nh = rem(prev * base + (ch - ?a + 1), mod)
        :array.set(idx + 1, nh, arr)
      end)

    {pref_hash, pow}
  end

  # Substring hash [l, r) using precomputed arrays
  defp substring_hash(pref, pow, l, r, mod) do
    h_r = :array.get(r, pref)
    h_l = :array.get(l, pref)
    p = :array.get(r - l, pow)
    val = rem(h_r - rem(h_l * p, mod) + mod, mod)
    val
  end

  # Binary search longest matching length at position i
  defp longest_match(i, max_len, pref, pow, len_map, mod) do
    do_longest(i, 0, max_len, pref, pow, len_map, mod)
  end

  defp do_longest(_i, low, high, _pref, _pow, _len_map, _mod) when low >= high, do: low

  defp do_longest(i, low, high, pref, pow, len_map, mod) do
    mid = div(low + high + 1, 2)
    hash = substring_hash(pref, pow, i, i + mid, mod)

    exists =
      case Map.get(len_map, mid) do
        nil -> false
        set -> MapSet.member?(set, hash)
      end

    if exists,
      do: do_longest(i, mid, high, pref, pow, len_map, mod),
      else: do_longest(i, low, mid - 1, pref, pow, len_map, mod)
  end

  # DSU find with path compression (returns {root, updated_parent})
  defp dsu_find(parent, x) do
    px = :array.get(x, parent)

    if px == x do
      {x, parent}
    else
      {root, parent2} = dsu_find(parent, px)
      parent3 = :array.set(x, root, parent2)
      {root, parent3}
    end
  end

  # DSU union (sets parent of a to b) returns updated parent array
  defp dsu_union(parent, a, b) do
    {ra, parent1} = dsu_find(parent, a)
    {rb, parent2} = dsu_find(parent1, b)

    if ra != rb do
      :array.set(ra, rb, parent2)
    else
      parent2
    end
  end

  # BFS processing using queue, DSU and distance array
  defp bfs(queue, parent, dist, lens_arr, n, pref, pow, len_map, base, mod) do
    case :queue.out(queue) do
      {:empty, _} ->
        {parent, dist, queue}

      {{:value, i}, q2} ->
        d = :array.get(i, dist)
        max_len = if i < n, do: :array.get(i, lens_arr), else: 0

        {parent, dist, q2} =
          if max_len > 0 do
            limit = i + max_len
            {j, parent1} = dsu_find(parent, i + 1)

            process_range(j, limit, d + 1, parent1, dist, q2)
          else
            {parent, dist, q2}
          end

        bfs(q2, parent, dist, lens_arr, n, pref, pow, len_map, base, mod)
    end
  end

  # Process all unvisited positions in [cur, limit]
  defp process_range(cur, limit, new_dist, parent, dist, queue) do
    if cur > limit do
      {parent, dist, queue}
    else
      dist = :array.set(cur, new_dist, dist)
      queue = :queue.in(cur, queue)
      parent = dsu_union(parent, cur, cur + 1)
      {next_cur, parent} = dsu_find(parent, cur)
      process_range(next_cur, limit, new_dist, parent, dist, queue)
    end
  end
end
```
