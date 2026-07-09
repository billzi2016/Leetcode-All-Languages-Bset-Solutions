# 3569. Maximize Count of Distinct Primes After Split

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class SegTree {
    int n;
    vector<int> tree, lazy;
public:
    SegTree(int sz = 0) { init(sz); }
    void init(int sz) {
        n = max(1, sz);
        tree.assign(4 * n, 0);
        lazy.assign(4 * n, 0);
    }
    void rangeAdd(int l, int r, int val) { if (l <= r) add(1, 0, n - 1, l, r, val); }
    int queryMax() const { return tree[1]; }

private:
    void push(int node) {
        if (lazy[node] != 0) {
            for (int child : {node << 1, node << 1 | 1}) {
                tree[child] += lazy[node];
                lazy[child] += lazy[node];
            }
            lazy[node] = 0;
        }
    }
    void add(int node, int nl, int nr, int l, int r, int val) {
        if (l > nr || r < nl) return;
        if (l <= nl && nr <= r) {
            tree[node] += val;
            lazy[node] += val;
            return;
        }
        push(node);
        int mid = (nl + nr) >> 1;
        add(node << 1, nl, mid, l, r, val);
        add(node << 1 | 1, mid + 1, nr, l, r, val);
        tree[node] = max(tree[node << 1], tree[node << 1 | 1]);
    }
};

class Solution {
public:
    vector<int> maximumCount(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        const int MAXV = 100000;
        vector<bool> isPrime(MAXV + 1, true);
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i * i <= MAXV; ++i) if (isPrime[i])
            for (int j = i * i; j <= MAXV; j += i) isPrime[j] = false;

        vector< set<int> > pos(MAXV + 1);
        int distinctPrimes = 0;
        for (int i = 0; i < n; ++i) {
            int v = nums[i];
            if (!isPrime[v]) continue;
            auto &s = pos[v];
            s.insert(i);
        }
        for (int p = 2; p <= MAXV; ++p) if (isPrime[p] && !pos[p].empty()) distinctPrimes++;

        SegTree seg(max(n - 1));
        // add intervals for primes with >=2 occurrences
        for (int p = 2; p <= MAXV; ++p) if (isPrime[p]) {
            auto &s = pos[p];
            if ((int)s.size() >= 2) {
                int first = *s.begin();
                int last = *s.rbegin();
                seg.rangeAdd(first, last - 1, 1);
            }
        }

        vector<int> ans;
        for (auto &qr : queries) {
            int idx = qr[0];
            int val = qr[1];
            int oldVal = nums[idx];
            if (oldVal != val) {
                // remove old value contribution
                if (isPrime[oldVal]) {
                    auto &s = pos[oldVal];
                    int sz = s.size();
                    if (sz >= 2) {
                        int first = *s.begin();
                        int last = *s.rbegin();
                        seg.rangeAdd(first, last - 1, -1);
                    }
                    s.erase(idx);
                    int nsz = s.size();
                    if (nsz >= 2) {
                        int first = *s.begin();
                        int last = *s.rbegin();
                        seg.rangeAdd(first, last - 1, +1);
                    }
                    if (sz == 1 && nsz == 0) distinctPrimes--;
                }

                // add new value contribution
                if (isPrime[val]) {
                    auto &s = pos[val];
                    int sz = s.size();
                    if (sz >= 2) {
                        int first = *s.begin();
                        int last = *s.rbegin();
                        seg.rangeAdd(first, last - 1, -1);
                    }
                    s.insert(idx);
                    int nsz = s.size();
                    if (nsz >= 2) {
                        int first = *s.begin();
                        int last = *s.rbegin();
                        seg.rangeAdd(first, last - 1, +1);
                    }
                    if (sz == 0 && nsz == 1) distinctPrimes++;
                }

                nums[idx] = val;
            }
            int maxCover = seg.queryMax(); // may be zero
            ans.push_back(distinctPrimes + maxCover);
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static class SegTree {
        int n;
        int[] max, lazy;
        SegTree(int size) {
            this.n = size;
            max = new int[4 * n];
            lazy = new int[4 * n];
        }
        void push(int node) {
            if (lazy[node] != 0) {
                int lz = lazy[node];
                int left = node << 1, right = left | 1;
                max[left] += lz;
                lazy[left] += lz;
                max[right] += lz;
                lazy[right] += lz;
                lazy[node] = 0;
            }
        }
        void add(int node, int l, int r, int ql, int qr, int val) {
            if (ql > r || qr < l) return;
            if (ql <= l && r <= qr) {
                max[node] += val;
                lazy[node] += val;
                return;
            }
            push(node);
            int mid = (l + r) >>> 1;
            add(node << 1, l, mid, ql, qr, val);
            add(node << 1 | 1, mid + 1, r, ql, qr, val);
            max[node] = Math.max(max[node << 1], max[node << 1 | 1]);
        }
        void add(int l, int r, int val) {
            if (l > r) return;
            add(1, 0, n - 1, l, r, val);
        }
        int queryMax() {
            return n == 0 ? 0 : max[1];
        }
    }

    public int[] maximumCount(int[] nums, int[][] queries) {
        int n = nums.length;
        boolean[] isPrime = sieve(100000);
        if (n == 1) { // no split possible
            int[] ans = new int[queries.length];
            Arrays.fill(ans, 0);
            return ans;
        }
        SegTree seg = new SegTree(n - 1);
        Map<Integer, TreeSet<Integer>> map = new HashMap<>();

        for (int i = 0; i < n; i++) {
            int v = nums[i];
            if (v <= 100000 && isPrime[v]) {
                map.computeIfAbsent(v, k -> new TreeSet<>()).add(i);
            }
        }

        // initial contributions
        for (Map.Entry<Integer, TreeSet<Integer>> e : map.entrySet()) {
            TreeSet<Integer> set = e.getValue();
            if (set.size() >= 2) {
                int first = set.first();
                int last = set.last();
                seg.add(first, last - 1, 1);
            }
        }

        int[] res = new int[queries.length];
        for (int qi = 0; qi < queries.length; qi++) {
            int idx = queries[qi][0];
            int val = queries[qi][1];
            int old = nums[idx];

            // remove old prime contribution if needed
            if (old <= 100000 && isPrime[old]) {
                TreeSet<Integer> set = map.get(old);
                if (set != null) {
                    if (set.size() >= 2) {
                        seg.add(set.first(), set.last() - 1, -1);
                    }
                    set.remove(idx);
                    if (set.isEmpty()) {
                        map.remove(old);
                    } else if (set.size() >= 2) {
                        seg.add(set.first(), set.last() - 1, 1);
                    }
                }
            }

            // add new prime contribution if needed
            nums[idx] = val;
            if (val <= 100000 && isPrime[val]) {
                TreeSet<Integer> set = map.computeIfAbsent(val, k -> new TreeSet<>());
                if (set.size() >= 2) {
                    seg.add(set.first(), set.last() - 1, -1);
                }
                set.add(idx);
                if (set.size() >= 2) {
                    seg.add(set.first(), set.last() - 1, 1);
                }
            }

            res[qi] = seg.queryMax();
        }
        return res;
    }

    private boolean[] sieve(int limit) {
        boolean[] isPrime = new boolean[limit + 1];
        Arrays.fill(isPrime, true);
        if (limit >= 0) isPrime[0] = false;
        if (limit >= 1) isPrime[1] = false;
        for (int i = 2; i * i <= limit; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= limit; j += i) {
                    isPrime[j] = false;
                }
            }
        }
        return isPrime;
    }
}
```

## Python

```python
import heapq

class SegmentTree:
    def __init__(self, n):
        self.N = 1
        while self.N < n:
            self.N <<= 1
        size = self.N << 1
        self.maxv = [0] * size
        self.lazy = [0] * size

    def _push(self, node):
        if self.lazy[node]:
            val = self.lazy[node]
            left = node << 1
            right = left | 1
            self.maxv[left] += val
            self.lazy[left] += val
            self.maxv[right] += val
            self.lazy[right] += val
            self.lazy[node] = 0

    def _add(self, l, r, val, node, nl, nr):
        if r < nl or nr < l:
            return
        if l <= nl and nr <= r:
            self.maxv[node] += val
            self.lazy[node] += val
            return
        self._push(node)
        mid = (nl + nr) >> 1
        self._add(l, r, val, node << 1, nl, mid)
        self._add(l, r, val, node << 1 | 1, mid + 1, nr)
        self.maxv[node] = max(self.maxv[node << 1], self.maxv[node << 1 | 1])

    def add(self, l, r, val):
        if l > r:
            return
        self._add(l, r, val, 1, 0, self.N - 1)

    def query_max(self):
        return self.maxv[1]


class Solution(object):
    def maximumCount(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        max_val = 100000
        is_prime = [True] * (max_val + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(max_val ** 0.5) + 1):
            if is_prime[i]:
                step = i
                start = i * i
                for j in range(start, max_val + 1, step):
                    is_prime[j] = False

        # structures per prime
        data = {}   # p -> dict with cnt,set,minh,maxh,first,last
        D = 0       # number of distinct primes present

        seg = SegmentTree(n - 1) if n > 1 else SegmentTree(1)

        for idx, val in enumerate(nums):
            if not is_prime[val]:
                continue
            p = val
            if p not in data:
                data[p] = {
                    'cnt': 0,
                    'set': set(),
                    'minh': [],
                    'maxh': [],
                    'first': None,
                    'last': None
                }
                D += 1
            d = data[p]
            d['cnt'] += 1
            d['set'].add(idx)
            heapq.heappush(d['minh'], idx)
            heapq.heappush(d['maxh'], -idx)

        # finalize first/last and initial intervals
        for p, d in data.items():
            while d['minh'][0] not in d['set']:
                heapq.heappop(d['minh'])
            while -d['maxh'][0] not in d['set']:
                heapq.heappop(d['maxh'])
            d['first'] = d['minh'][0]
            d['last'] = -d['maxh'][0]
            if d['cnt'] >= 2:
                seg.add(d['first'], d['last'] - 1, 1)

        res = []
        for idx, val in queries:
            old = nums[idx]
            if old != val:
                # remove old prime contribution
                if is_prime[old]:
                    p = old
                    d = data[p]
                    cnt_before = d['cnt']
                    if cnt_before >= 2:
                        seg.add(d['first'], d['last'] - 1, -1)
                    # update structures
                    d['cnt'] -= 1
                    d['set'].remove(idx)
                    if d['cnt'] == 0:
                        D -= 1
                        del data[p]
                    else:
                        while d['minh'][0] not in d['set']:
                            heapq.heappop(d['minh'])
                        while -d['maxh'][0] not in d['set']:
                            heapq.heappop(d['maxh'])
                        d['first'] = d['minh'][0]
                        d['last'] = -d['maxh'][0]
                        if d['cnt'] >= 2:
                            seg.add(d['first'], d['last'] - 1, 1)

                # add new prime contribution
                if is_prime[val]:
                    p = val
                    if p not in data:
                        data[p] = {
                            'cnt': 0,
                            'set': set(),
                            'minh': [],
                            'maxh': [],
                            'first': None,
                            'last': None
                        }
                        D += 1
                    d = data[p]
                    cnt_before = d['cnt']
                    if cnt_before >= 2:
                        seg.add(d['first'], d['last'] - 1, -1)
                    d['cnt'] += 1
                    d['set'].add(idx)
                    heapq.heappush(d['minh'], idx)
                    heapq.heappush(d['maxh'], -idx)

                    while d['minh'][0] not in d['set']:
                        heapq.heappop(d['minh'])
                    while -d['maxh'][0] not in d['set']:
                        heapq.heappop(d['maxh'])
                    d['first'] = d['minh'][0]
                    d['last'] = -d['maxh'][0]
                    if d['cnt'] >= 2:
                        seg.add(d['first'], d['last'] - 1, 1)

                nums[idx] = val

            ans = D + seg.query_max()
            res.append(ans)
        return res
```

## Python3

```python
import heapq
from typing import List

class SegmentTree:
    def __init__(self, n):
        self.n = n
        size = 4 * n
        self.maxv = [0] * size
        self.lazy = [0] * size

    def _push(self, node):
        if self.lazy[node]:
            val = self.lazy[node]
            left = node << 1
            right = left | 1
            self.maxv[left] += val
            self.lazy[left] += val
            self.maxv[right] += val
            self.lazy[right] += val
            self.lazy[node] = 0

    def _add(self, node, l, r, ql, qr, val):
        if ql > r or qr < l:
            return
        if ql <= l and r <= qr:
            self.maxv[node] += val
            self.lazy[node] += val
            return
        self._push(node)
        mid = (l + r) >> 1
        self._add(node << 1, l, mid, ql, qr, val)
        self._add((node << 1) | 1, mid + 1, r, ql, qr, val)
        self.maxv[node] = max(self.maxv[node << 1], self.maxv[(node << 1) | 1])

    def add(self, l, r, val):
        if l > r:
            return
        self._add(1, 0, self.n - 1, l, r, val)

    def query_max(self):
        return self.maxv[1] if self.n > 0 else 0


class Solution:
    def maximumCount(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        max_val = 100000
        is_prime = [True] * (max_val + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(max_val ** 0.5) + 1):
            if is_prime[i]:
                step = i * i
                while step <= max_val:
                    is_prime[step] = False
                    step += i

        n = len(nums)
        split_cnt = n - 1
        seg = SegmentTree(split_cnt)

        # data per prime: cnt, set of indices, minHeap, maxHeap
        prime_info = {}

        def get_first(p):
            info = prime_info[p]
            while info['minHeap']:
                idx = info['minHeap'][0]
                if idx in info['set']:
                    return idx
                heapq.heappop(info['minHeap'])
            return None

        def get_last(p):
            info = prime_info[p]
            while info['maxHeap']:
                idx = -info['maxHeap'][0]
                if idx in info['set']:
                    return idx
                heapq.heappop(info['maxHeap'])
            return None

        def apply_interval(p, delta):
            """delta = +1 to add interval, -1 to remove"""
            cnt = prime_info[p]['cnt']
            if cnt >= 2:
                f = get_first(p)
                l = get_last(p)
                seg.add(f, l - 1, delta)

        def adjust(p, idx, delta):
            """delta = +1 for insertion, -1 for deletion"""
            if p not in prime_info:
                prime_info[p] = {'cnt': 0, 'set': set(),
                                'minHeap': [], 'maxHeap': []}
            info = prime_info[p]

            # remove old interval if existed
            apply_interval(p, -1)

            if delta == 1:
                info['cnt'] += 1
                info['set'].add(idx)
                heapq.heappush(info['minHeap'], idx)
                heapq.heappush(info['maxHeap'], -idx)
            else:  # deletion
                info['cnt'] -= 1
                info['set'].remove(idx)

            # add new interval if now valid
            apply_interval(p, +1)

        # initial population
        for i, v in enumerate(nums):
            if is_prime[v]:
                adjust(v, i, 1)

        res = []
        for idx, val in queries:
            old = nums[idx]
            if is_prime[old]:
                adjust(old, idx, -1)
            nums[idx] = val
            if is_prime[val]:
                adjust(val, idx, 1)
            res.append(seg.query_max())
        return res
```

## C

```c
#include <stdlib.h>
#include <string.h>

#define MAXV 100000
#define MAXN 50005
#define MAXNODE 200005

/* prime sieve */
static int isPrime[MAXV + 1];

/* treap node pool */
typedef struct {
    int key;
    unsigned pri;
    int l, r;
} Node;

static Node nodes[MAXNODE];
static int nodeCnt = 0;

/* roots and counts per prime */
static int roots[MAXV + 1];
static int cntPrime[MAXV + 1];

/* segment tree for positions 0 .. n-2 */
typedef struct {
    int add;
    int mx;
} SegNode;

static SegNode *seg;
static int segSize;   /* number of leaves = n-1 */

/* ---------- treap utilities ---------- */
static int newNode(int key) {
    ++nodeCnt;
    nodes[nodeCnt].key = key;
    nodes[nodeCnt].pri = ((unsigned)rand() << 16) ^ (unsigned)rand();
    nodes[nodeCnt].l = nodes[nodeCnt].r = 0;
    return nodeCnt;
}

static void split(int cur, int key, int *left, int *right) {
    if (cur == 0) {
        *left = *right = 0;
        return;
    }
    if (key < nodes[cur].key) {
        split(nodes[cur].l, key, left, &nodes[cur].l);
        *right = cur;
    } else {
        split(nodes[cur].r, key, &nodes[cur].r, right);
        *left = cur;
    }
}

static int merge(int a, int b) {
    if (!a || !b) return a ? a : b;
    if (nodes[a].pri > nodes[b].pri) {
        nodes[a].r = merge(nodes[a].r, b);
        return a;
    } else {
        nodes[b].l = merge(a, nodes[b].l);
        return b;
    }
}

static int insertNode(int root, int key) {
    int l, r;
    split(root, key, &l, &r);
    int nd = newNode(key);
    return merge(merge(l, nd), r);
}

static int eraseNode(int root, int key) {
    if (!root) return 0;
    if (nodes[root].key == key) {
        return merge(nodes[root].l, nodes[root].r);
    } else if (key < nodes[root].key) {
        nodes[root].l = eraseNode(nodes[root].l, key);
    } else {
        nodes[root].r = eraseNode(nodes[root].r, key);
    }
    return root;
}

static int getMin(int root) {
    while (root && nodes[root].l) root = nodes[root].l;
    return root ? nodes[root].key : -1;
}
static int getMax(int root) {
    while (root && nodes[root].r) root = nodes[root].r;
    return root ? nodes[root].key : -1;
}

/* ---------- segment tree utilities ---------- */
static void segPush(int idx) {
    if (seg[idx].add != 0) {
        int v = seg[idx].add;
        seg[idx << 1].add += v;
        seg[idx << 1].mx += v;
        seg[(idx << 1) | 1].add += v;
        seg[(idx << 1) | 1].mx += v;
        seg[idx].add = 0;
    }
}
static void segAdd(int idx, int l, int r, int ql, int qr, int val) {
    if (ql > r || qr < l) return;
    if (ql <= l && r <= qr) {
        seg[idx].add += val;
        seg[idx].mx += val;
        return;
    }
    segPush(idx);
    int mid = (l + r) >> 1;
    segAdd(idx << 1, l, mid, ql, qr, val);
    segAdd((idx << 1) | 1, mid + 1, r, ql, qr, val);
    seg[idx].mx = seg[idx << 1].mx > seg[(idx << 1) | 1].mx ? seg[idx << 1].mx : seg[(idx << 1) | 1].mx;
}

/* ---------- main solution ---------- */
int* maximumCount(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize){
    /* sieve */
    memset(isPrime, 1, sizeof(isPrime));
    isPrime[0] = isPrime[1] = 0;
    for (int i = 2; i * i <= MAXV; ++i) if (isPrime[i]) {
        for (int j = i * i; j <= MAXV; j += i) isPrime[j] = 0;
    }

    /* initialize structures */
    memset(roots, 0, sizeof(roots));
    memset(cntPrime, 0, sizeof(cntPrime));
    nodeCnt = 0;
    srand(0);

    int n = numsSize;
    segSize = n - 1;               /* positions between elements */
    seg = (SegNode*)calloc((segSize * 4 + 5), sizeof(SegNode));

    /* insert initial primes */
    for (int i = 0; i < n; ++i) {
        int v = nums[i];
        if (!isPrime[v]) continue;
        cntPrime[v]++;
        roots[v] = insertNode(roots[v], i);
    }

    /* add intervals for primes with count >=2 */
    for (int p = 2; p <= MAXV; ++p) {
        if (!isPrime[p] || cntPrime[p] < 2) continue;
        int first = getMin(roots[p]);
        int last  = getMax(roots[p]);
        if (first < last) {
            segAdd(1, 0, segSize - 1, first, last - 1, 1);
        }
    }

    int *ansArr = (int*)malloc(sizeof(int) * queriesSize);
    for (int qi = 0; qi < queriesSize; ++qi) {
        int idx = queries[qi][0];
        int newVal = queries[qi][1];
        int oldVal = nums[idx];
        if (oldVal != newVal) {
            /* remove old value contribution */
            if (isPrime[oldVal]) {
                int p = oldVal;
                if (cntPrime[p] >= 2) {
                    int first = getMin(roots[p]);
                    int last  = getMax(roots[p]);
                    segAdd(1, 0, segSize - 1, first, last - 1, -1);
                }
                roots[p] = eraseNode(roots[p], idx);
                cntPrime[p]--;
                if (cntPrime[p] >= 2) {
                    int first = getMin(roots[p]);
                    int last  = getMax(roots[p]);
                    segAdd(1, 0, segSize - 1, first, last - 1, 1);
                }
            }

            /* add new value contribution */
            if (isPrime[newVal]) {
                int p = newVal;
                if (cntPrime[p] >= 2) {
                    int first = getMin(roots[p]);
                    int last  = getMax(roots[p]);
                    segAdd(1, 0, segSize - 1, first, last - 1, -1);
                }
                roots[p] = insertNode(roots[p], idx);
                cntPrime[p]++;
                if (cntPrime[p] >= 2) {
                    int first = getMin(roots[p]);
                    int last  = getMax(roots[p]);
                    segAdd(1, 0, segSize - 1, first, last - 1, 1);
                }
            }

            nums[idx] = newVal;
        }
        ansArr[qi] = (segSize > 0) ? seg[1].mx : 0;
    }

    *returnSize = queriesSize;
    free(seg);
    return ansArr;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private bool[] isPrime;
    private SortedSet<int>[] positions;
    private SegTree seg;
    private int totalDistinct;
    private int nMinusOne;

    public int[] MaximumCount(int[] nums, int[][] queries) {
        int maxVal = 100000;
        PrecomputePrimes(maxVal);
        int n = nums.Length;
        nMinusOne = n - 1;
        seg = new SegTree(nMinusOne > 0 ? nMinusOne : 1);
        positions = new SortedSet<int>[maxVal + 1];
        totalDistinct = 0;

        for (int i = 0; i < n; i++) {
            AddPrime(nums[i], i);
        }

        int q = queries.Length;
        int[] ans = new int[q];
        for (int i = 0; i < q; i++) {
            int idx = queries[i][0];
            int val = queries[i][1];
            if (nums[idx] != val) {
                RemovePrime(nums[idx], idx);
                AddPrime(val, idx);
                nums[idx] = val;
            }
            ans[i] = totalDistinct + (nMinusOne > 0 ? (int)seg.Max() : 0);
        }
        return ans;
    }

    private void PrecomputePrimes(int limit) {
        isPrime = new bool[limit + 1];
        for (int i = 2; i <= limit; i++) isPrime[i] = true;
        for (int p = 2; p * p <= limit; p++) {
            if (isPrime[p]) {
                for (int multiple = p * p; multiple <= limit; multiple += p)
                    isPrime[multiple] = false;
            }
        }
    }

    private void AddPrime(int value, int idx) {
        if (value < 0 || value >= isPrime.Length || !isPrime[value]) return;

        var set = positions[value];
        bool hadAny = set != null && set.Count > 0;
        int oldFirst = -1, oldLast = -1;
        if (hadAny && set.Count >= 2) {
            oldFirst = set.Min;
            oldLast = set.Max;
        }

        if (set == null) {
            set = new SortedSet<int>();
            positions[value] = set;
        }
        set.Add(idx);

        bool nowAny = set.Count > 0;
        int newFirst = -1, newLast = -1;
        if (set.Count >= 2) {
            newFirst = set.Min;
            newLast = set.Max;
        }

        if (!hadAny && nowAny) totalDistinct++;

        if (oldFirst != -1) seg.Add(oldFirst, oldLast - 1, -1);
        if (newFirst != -1) seg.Add(newFirst, newLast - 1, +1);
    }

    private void RemovePrime(int value, int idx) {
        if (value < 0 || value >= isPrime.Length || !isPrime[value]) return;

        var set = positions[value];
        if (set == null) return; // should not happen

        int oldFirst = -1, oldLast = -1;
        if (set.Count >= 2) {
            oldFirst = set.Min;
            oldLast = set.Max;
        }
        bool hadAny = set.Count > 0;

        set.Remove(idx);

        bool nowAny = set.Count > 0;
        int newFirst = -1, newLast = -1;
        if (set.Count >= 2) {
            newFirst = set.Min;
            newLast = set.Max;
        }

        if (hadAny && !nowAny) totalDistinct--;

        if (oldFirst != -1) seg.Add(oldFirst, oldLast - 1, -1);
        if (newFirst != -1) seg.Add(newFirst, newLast - 1, +1);

        if (!nowAny) positions[value] = null;
    }

    private class SegTree {
        private readonly int size;
        private readonly long[] max;
        private readonly long[] lazy;

        public SegTree(int n) {
            size = 1;
            while (size < n) size <<= 1;
            max = new long[size << 1];
            lazy = new long[size << 1];
        }

        private void Apply(int node, long val) {
            max[node] += val;
            lazy[node] += val;
        }

        private void Push(int node) {
            if (lazy[node] != 0) {
                Apply(node << 1, lazy[node]);
                Apply((node << 1) | 1, lazy[node]);
                lazy[node] = 0;
            }
        }

        public void Add(int l, int r, long val) {
            if (l > r) return;
            Add(l, r, val, 1, 0, size - 1);
        }

        private void Add(int l, int r, long val, int node, int nl, int nr) {
            if (r < nl || nr < l) return;
            if (l <= nl && nr <= r) {
                Apply(node, val);
                return;
            }
            Push(node);
            int mid = (nl + nr) >> 1;
            Add(l, r, val, node << 1, nl, mid);
            Add(l, r, val, (node << 1) | 1, mid + 1, nr);
            max[node] = Math.Max(max[node << 1], max[(node << 1) | 1]);
        }

        public long Max() => max[1];
    }
}
```

## Javascript

```javascript
/****
* @param {number[]} nums
* @param {number[][]} queries
* @return {number[]}
*/
var maximumCount = function(nums, queries) {
    const MAXV = 100000;
    // sieve for primes
    const isPrime = new Uint8Array(MAXV + 1);
    for (let i = 2; i <= MAXV; ++i) isPrime[i] = 1;
    for (let p = 2; p * p <= MAXV; ++p) {
        if (isPrime[p]) {
            for (let x = p * p; x <= MAXV; x += p) isPrime[x] = 0;
        }
    }

    // Treap implementation
    function newNode(key) {
        return {key, prio: Math.random(), left: null, right: null, sz: 1};
    }
    function getSize(node) { return node ? node.sz : 0; }
    function upd(node) {
        if (node) node.sz = 1 + getSize(node.left) + getSize(node.right);
    }
    function rotateRight(p) {
        const q = p.left;
        p.left = q.right;
        q.right = p;
        upd(p); upd(q);
        return q;
    }
    function rotateLeft(p) {
        const q = p.right;
        p.right = q.left;
        q.left = p;
        upd(p); upd(q);
        return q;
    }
    function treapInsert(root, key) {
        if (!root) return newNode(key);
        if (key < root.key) {
            root.left = treapInsert(root.left, key);
            if (root.left.prio < root.prio) root = rotateRight(root);
        } else {
            root.right = treapInsert(root.right, key);
            if (root.right.prio < root.prio) root = rotateLeft(root);
        }
        upd(root);
        return root;
    }
    function treapDelete(root, key) {
        if (!root) return null;
        if (key === root.key) {
            // remove this node
            if (!root.left && !root.right) return null;
            if (!root.left) {
                root = rotateLeft(root);
                root.left = treapDelete(root.left, key);
            } else if (!root.right) {
                root = rotateRight(root);
                root.right = treapDelete(root.right, key);
            } else {
                // rotate the child with smaller priority
                if (root.left.prio < root.right.prio) {
                    root = rotateRight(root);
                    root.right = treapDelete(root.right, key);
                } else {
                    root = rotateLeft(root);
                    root.left = treapDelete(root.left, key);
                }
            }
        } else if (key < root.key) {
            root.left = treapDelete(root.left, key);
        } else {
            root.right = treapDelete(root.right, key);
        }
        upd(root);
        return root;
    }
    function getMin(node) {
        while (node && node.left) node = node.left;
        return node ? node.key : null;
    }
    function getMax(node) {
        while (node && node.right) node = node.right;
        return node ? node.key : null;
    }

    // Segment tree for range add / max query
    class SegTree {
        constructor(n) {
            this.n = n;
            const size = 4 * Math.max(1, n);
            this.mx = new Int32Array(size);
            this.add = new Int32Array(size);
        }
        _push(v) {
            const a = this.add[v];
            if (a !== 0) {
                const l = v << 1, r = l | 1;
                this.mx[l] += a; this.add[l] += a;
                this.mx[r] += a; this.add[r] += a;
                this.add[v] = 0;
            }
        }
        _update(l, r, val, v, tl, tr) {
            if (l > r) return;
            if (l === tl && r === tr) {
                this.mx[v] += val;
                this.add[v] += val;
                return;
            }
            this._push(v);
            const tm = (tl + tr) >> 1;
            if (r <= tm) this._update(l, r, val, v << 1, tl, tm);
            else if (l > tm) this._update(l, r, val, (v << 1) | 1, tm + 1, tr);
            else {
                this._update(l, tm, val, v << 1, tl, tm);
                this._update(tm + 1, r, val, (v << 1) | 1, tm + 1, tr);
            }
            const left = this.mx[v << 1], right = this.mx[(v << 1) | 1];
            this.mx[v] = left > right ? left : right;
        }
        update(l, r, val) {
            if (this.n === 0 || l > r) return;
            this._update(l, r, val, 1, 0, this.n - 1);
        }
        queryMax() {
            return this.n === 0 ? 0 : this.mx[1];
        }
    }

    const n = nums.length;
    const splitCount = Math.max(0, n - 1);
    const seg = new SegTree(splitCount);

    // map prime value -> treap root
    const roots = new Map();
    let distinctPrimeCnt = 0;

    // initial insertion
    for (let i = 0; i < n; ++i) {
        const v = nums[i];
        if (!isPrime[v]) continue;
        let root = roots.get(v) || null;
        const beforeSize = getSize(root);
        root = treapInsert(root, i);
        roots.set(v, root);
        const afterSize = getSize(root);
        if (beforeSize === 0 && afterSize > 0) distinctPrimeCnt++;
    }

    // add intervals for primes with >=2 occurrences
    for (const [p, root] of roots.entries()) {
        if (getSize(root) >= 2) {
            const l = getMin(root);
            const r = getMax(root);
            seg.update(l, r - 1, 1);
        }
    }

    const answers = [];

    for (const [idx, val] of queries) {
        const oldVal = nums[idx];
        if (oldVal !== val) {
            // remove old prime occurrence
            if (isPrime[oldVal]) {
                let root = roots.get(oldVal);
                const szBefore = getSize(root);
                if (szBefore >= 2) {
                    const l = getMin(root);
                    const r = getMax(root);
                    seg.update(l, r - 1, -1);
                }
                root = treapDelete(root, idx);
                if (root) roots.set(oldVal, root);
                else roots.delete(oldVal);
                const szAfter = getSize(root);
                if (szBefore > 0 && szAfter === 0) distinctPrimeCnt--;
                if (szBefore >= 2 && szAfter >= 2) {
                    const l = getMin(root);
                    const r = getMax(root);
                    seg.update(l, r - 1, 1);
                }
            }

            // add new prime occurrence
            if (isPrime[val]) {
                let root = roots.get(val) || null;
                const szBefore = getSize(root);
                if (szBefore >= 2) {
                    const l = getMin(root);
                    const r = getMax(root);
                    seg.update(l, r - 1, -1);
                }
                root = treapInsert(root, idx);
                roots.set(val, root);
                const szAfter = getSize(root);
                if (szBefore === 0 && szAfter > 0) distinctPrimeCnt++;
                if (szAfter >= 2) {
                    const l = getMin(root);
                    const r = getMax(root);
                    seg.update(l, r - 1, 1);
                }
            }

            nums[idx] = val;
        }
        answers.push(distinctPrimeCnt + seg.queryMax());
    }

    return answers;
};
```

## Typescript

```typescript
function maximumCount(nums: number[], queries: number[][]): number[] {
    const maxVal = 100000;
    const isPrime = new Uint8Array(maxVal + 1);
    for (let i = 2; i <= maxVal; ++i) isPrime[i] = 1;
    for (let p = 2; p * p <= maxVal; ++p) {
        if (isPrime[p]) {
            for (let x = p * p; x <= maxVal; x += p) isPrime[x] = 0;
        }
    }

    const n = nums.length;
    const segSize = n - 1;
    class SegTree {
        n: number;
        max: Int32Array;
        lazy: Int32Array;
        constructor(size: number) {
            this.n = size;
            const sz = size * 4 + 5;
            this.max = new Int32Array(sz);
            this.lazy = new Int32Array(sz);
        }
        private push(node: number, l: number, r: number): void {
            const val = this.lazy[node];
            if (val !== 0 && l !== r) {
                const left = node << 1;
                const right = left | 1;
                this.max[left] += val;
                this.lazy[left] += val;
                this.max[right] += val;
                this.lazy[right] += val;
                this.lazy[node] = 0;
            }
        }
        private rangeAdd(node: number, l: number, r: number, ql: number, qr: number, v: number): void {
            if (ql > r || qr < l) return;
            if (ql <= l && r <= qr) {
                this.max[node] += v;
                this.lazy[node] += v;
                return;
            }
            this.push(node, l, r);
            const mid = (l + r) >> 1;
            this.rangeAdd(node << 1, l, mid, ql, qr, v);
            this.rangeAdd((node << 1) | 1, mid + 1, r, ql, qr, v);
            this.max[node] = Math.max(this.max[node << 1], this.max[(node << 1) | 1]);
        }
        add(l: number, r: number, v: number): void {
            if (l > r) return;
            this.rangeAdd(1, 0, this.n - 1, l, r, v);
        }
        queryMax(): number {
            return this.max[1];
        }
    }

    type TreapNode = {
        key: number;
        prio: number;
        left: TreapNode | null;
        right: TreapNode | null;
        size: number;
    };

    function nodeSize(t: TreapNode | null): number {
        return t ? t.size : 0;
    }
    function update(t: TreapNode): void {
        t.size = 1 + nodeSize(t.left) + nodeSize(t.right);
    }
    function rotateRight(y: TreapNode): TreapNode {
        const x = y.left!;
        y.left = x.right;
        x.right = y;
        update(y);
        update(x);
        return x;
    }
    function rotateLeft(x: TreapNode): TreapNode {
        const y = x.right!;
        x.right = y.left;
        y.left = x;
        update(x);
        update(y);
        return y;
    }
    function treapInsert(root: TreapNode | null, key: number): TreapNode {
        if (!root) return { key, prio: Math.random(), left: null, right: null, size: 1 };
        if (key < root.key) {
            root.left = treapInsert(root.left, key);
            if (root.left.prio < root.prio) root = rotateRight(root);
        } else {
            root.right = treapInsert(root.right, key);
            if (root.right.prio < root.prio) root = rotateLeft(root);
        }
        update(root);
        return root;
    }
    function merge(a: TreapNode | null, b: TreapNode | null): TreapNode | null {
        if (!a) return b;
        if (!b) return a;
        if (a.prio < b.prio) {
            a.right = merge(a.right, b);
            update(a);
            return a;
        } else {
            b.left = merge(a, b.left);
            update(b);
            return b;
        }
    }
    function treapErase(root: TreapNode | null, key: number): TreapNode | null {
        if (!root) return null;
        if (key === root.key) {
            return merge(root.left, root.right);
        } else if (key < root.key) {
            root.left = treapErase(root.left, key);
            update(root);
            return root;
        } else {
            root.right = treapErase(root.right, key);
            update(root);
            return root;
        }
    }
    function treapGetMin(root: TreapNode | null): number | undefined {
        if (!root) return undefined;
        while (root.left) root = root.left;
        return root.key;
    }
    function treapGetMax(root: TreapNode | null): number | undefined {
        if (!root) return undefined;
        while (root.right) root = root.right;
        return root.key;
    }

    const seg = new SegTree(segSize);
    const primeMap = new Map<number, TreapNode | null>();

    // initial insertion
    for (let i = 0; i < n; ++i) {
        const v = nums[i];
        if (isPrime[v]) {
            const root = primeMap.get(v) || null;
            primeMap.set(v, treapInsert(root, i));
        }
    }

    // add initial segments
    for (const [p, root] of primeMap.entries()) {
        if (root && nodeSize(root) >= 2) {
            const first = treapGetMin(root)!;
            const last = treapGetMax(root)!;
            seg.add(first, last - 1, 1);
        }
    }

    const ans: number[] = [];
    for (const [idxRaw, valRaw] of queries) {
        const idx = idxRaw;
        const val = valRaw;
        const old = nums[idx];
        if (old !== val) {
            // remove old prime contribution
            if (isPrime[old]) {
                let root = primeMap.get(old)!;
                const szBefore = nodeSize(root);
                if (szBefore >= 2) {
                    const f = treapGetMin(root)!;
                    const l = treapGetMax(root)!;
                    seg.add(f, l - 1, -1);
                }
                root = treapErase(root, idx);
                primeMap.set(old, root);
                const szAfter = nodeSize(root);
                if (szAfter >= 2) {
                    const f = treapGetMin(root)!;
                    const l = treapGetMax(root)!;
                    seg.add(f, l - 1, 1);
                }
            }

            // add new prime contribution
            if (isPrime[val]) {
                let root = primeMap.get(val) || null;
                const szBefore = nodeSize(root);
                if (szBefore >= 2) {
                    const f = treapGetMin(root)!;
                    const l = treapGetMax(root)!;
                    seg.add(f, l - 1, -1);
                }
                root = treapInsert(root, idx);
                primeMap.set(val, root);
                const szAfter = nodeSize(root);
                if (szAfter >= 2) {
                    const f = treapGetMin(root)!;
                    const l = treapGetMax(root)!;
                    seg.add(f, l - 1, 1);
                }
            }

            nums[idx] = val;
        }
        ans.push(seg.queryMax());
    }
    return ans;
}
```

## Php

```php
class Solution {
    private $isPrime = [];
    private $tree = [];
    private $lazy = [];
    private $nSplits;
    private $nums = [];
    private $pos = []; // prime => sorted list of indices
    private $distinctPrimeCount = 0;

    /**
     * @param Integer[] $nums
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function maximumCount($nums, $queries) {
        $this->initPrimes(100000);
        $n = count($nums);
        $this->nSplits = $n - 1;
        $size = 4 * max(1, $this->nSplits);
        $this->tree = array_fill(0, $size, 0);
        $this->lazy = array_fill(0, $size, 0);
        $this->nums = $nums;

        // build positions for each prime
        foreach ($nums as $idx => $val) {
            if (!$this->isPrime[$val]) continue;
            if (!isset($this->pos[$val])) $this->pos[$val] = [];
            $this->pos[$val][] = $idx;
        }

        // sort positions and initialize distinct count & segment contributions
        foreach ($this->pos as $p => &$list) {
            sort($list, SORT_NUMERIC);
            $cnt = count($list);
            if ($cnt > 0) $this->distinctPrimeCount++;
            if ($cnt >= 2) {
                $first = $list[0];
                $last = $list[$cnt - 1];
                $this->rangeAdd(1, 0, $this->nSplits - 1, $first, $last - 1, 1);
            }
        }
        unset($list);

        $ans = [];
        foreach ($queries as $q) {
            [$idx, $val] = $q;
            $old = $this->nums[$idx];
            if ($old !== $val) {
                // remove old value contribution
                if ($this->isPrime[$old]) {
                    $list =& $this->pos[$old];
                    $posIdx = $this->binarySearch($list, $idx);
                    $cnt = count($list);
                    if ($cnt >= 2) {
                        $first = $list[0];
                        $last = $list[$cnt - 1];
                        $this->rangeAdd(1, 0, $this->nSplits - 1, $first, $last - 1, -1);
                    }
                    // remove index
                    array_splice($list, $posIdx, 1);
                    $newCnt = count($list);
                    if ($newCnt == 0) {
                        unset($this->pos[$old]);
                        $this->distinctPrimeCount--;
                    } elseif ($newCnt >= 2) {
                        $first = $list[0];
                        $last = $list[$newCnt - 1];
                        $this->rangeAdd(1, 0, $this->nSplits - 1, $first, $last - 1, 1);
                    }
                }

                // add new value contribution
                if ($this->isPrime[$val]) {
                    if (!isset($this->pos[$val])) {
                        $this->pos[$val] = [];
                        $this->distinctPrimeCount++;
                    }
                    $list =& $this->pos[$val];
                    $cnt = count($list);
                    if ($cnt >= 2) {
                        $first = $list[0];
                        $last = $list[$cnt - 1];
                        $this->rangeAdd(1, 0, $this->nSplits - 1, $first, $last - 1, -1);
                    }
                    // insert index keeping sorted order
                    $insertPos = $this->findInsertPosition($list, $idx);
                    array_splice($list, $insertPos, 0, [$idx]);
                    $newCnt = count($list);
                    if ($newCnt >= 2) {
                        $first = $list[0];
                        $last = $list[$newCnt - 1];
                        $this->rangeAdd(1, 0, $this->nSplits - 1, $first, $last - 1, 1);
                    }
                }

                $this->nums[$idx] = $val;
            }

            $maxOverlap = ($this->nSplits > 0) ? $this->tree[1] : 0;
            $ans[] = $this->distinctPrimeCount + $maxOverlap;
        }

        return $ans;
    }

    private function initPrimes($limit) {
        $this->isPrime = array_fill(0, $limit + 1, true);
        $this->isPrime[0] = $this->isPrime[1] = false;
        for ($i = 2; $i * $i <= $limit; $i++) {
            if ($this->isPrime[$i]) {
                for ($j = $i * $i; $j <= $limit; $j += $i) {
                    $this->isPrime[$j] = false;
                }
            }
        }
    }

    private function rangeAdd($node, $l, $r, $ql, $qr, $val) {
        if ($ql > $r || $qr < $l) return;
        if ($ql <= $l && $r <= $qr) {
            $this->tree[$node] += $val;
            $this->lazy[$node] += $val;
            return;
        }
        $mid = intdiv($l + $r, 2);
        $this->push($node);
        $this->rangeAdd($node * 2, $l, $mid, $ql, $qr, $val);
        $this->rangeAdd($node * 2 + 1, $mid + 1, $r, $ql, $qr, $val);
        $this->tree[$node] = max($this->tree[$node * 2], $this->tree[$node * 2 + 1]);
    }

    private function push($node) {
        if ($this->lazy[$node] != 0) {
            $add = $this->lazy[$node];
            $left = $node * 2;
            $right = $node * 2 + 1;
            $this->tree[$left] += $add;
            $this->lazy[$left] += $add;
            $this->tree[$right] += $add;
            $this->lazy[$right] += $add;
            $this->lazy[$node] = 0;
        }
    }

    // binary search to find exact index position in sorted list
    private function binarySearch(&$arr, $target) {
        $low = 0;
        $high = count($arr) - 1;
        while ($low <= $high) {
            $mid = intdiv($low + $high, 2);
            if ($arr[$mid] == $target) return $mid;
            elseif ($arr[$mid] < $target) $low = $mid + 1;
            else $high = $mid - 1;
        }
        return -1; // should not happen
    }

    // find position to insert while keeping sorted order
    private function findInsertPosition(&$arr, $value) {
        $low = 0;
        $high = count($arr);
        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            if ($arr[$mid] < $value) $low = $mid + 1;
            else $high = $mid;
        }
        return $low;
    }
}
```

## Swift

```swift
import Foundation

class TreapNode {
    var key: Int
    var priority: UInt32
    var left: TreapNode?
    var right: TreapNode?
    init(_ key: Int) {
        self.key = key
        self.priority = arc4random()
    }
}

class SegmentTree {
    private let size: Int
    private var maxArr: [Int]
    private var lazy: [Int]

    init(_ n: Int) {
        self.size = n
        let sz = 4 * (n + 5)
        self.maxArr = Array(repeating: 0, count: sz)
        self.lazy = Array(repeating: 0, count: sz)
    }

    func rangeAdd(_ l: Int, _ r: Int, _ val: Int) {
        if l > r { return }
        rangeAdd(1, 0, size, l, r, val)
    }

    private func rangeAdd(_ idx: Int, _ left: Int, _ right: Int, _ ql: Int, _ qr: Int, _ val: Int) {
        if ql <= left && right <= qr {
            maxArr[idx] += val
            lazy[idx] += val
            return
        }
        push(idx)
        let mid = (left + right) >> 1
        if ql <= mid {
            rangeAdd(idx << 1, left, mid, ql, qr, val)
        }
        if qr > mid {
            rangeAdd(idx << 1 | 1, mid + 1, right, ql, qr, val)
        }
        maxArr[idx] = max(maxArr[idx << 1], maxArr[idx << 1 | 1])
    }

    private func push(_ idx: Int) {
        let v = lazy[idx]
        if v != 0 {
            let lIdx = idx << 1
            let rIdx = lIdx | 1
            maxArr[lIdx] += v; lazy[lIdx] += v
            maxArr[rIdx] += v; lazy[rIdx] += v
            lazy[idx] = 0
        }
    }

    func queryMax() -> Int {
        return maxArr[1]
    }
}

class Solution {
    private var isPrime: [Bool] = []
    private var roots: [TreapNode?] = []
    private var cnt: [Int] = []
    private var seg: SegmentTree!
    private var distinctPrimes = 0
    private let maxValue = 100000

    func maximumCount(_ nums: [Int], _ queries: [[Int]]) -> [Int] {
        let n = nums.count
        buildSieve(upTo: maxValue)
        roots = Array(repeating: nil, count: maxValue + 1)
        cnt = Array(repeating: 0, count: maxValue + 1)

        var arr = nums

        // initial insertion
        for i in 0..<n {
            let v = arr[i]
            if isPrime[v] {
                roots[v] = treapInsert(roots[v], i)
                cnt[v] += 1
            }
        }

        distinctPrimes = 0
        for p in 2...maxValue where isPrime[p] && cnt[p] > 0 {
            distinctPrimes += 1
        }

        seg = SegmentTree(n) // indices 0..n

        // add intervals for primes with at least two occurrences
        for p in 2...maxValue where isPrime[p] && cnt[p] >= 2 {
            if let first = treapMin(roots[p]), let last = treapMax(roots[p]) {
                seg.rangeAdd(first + 1, last, 1)
            }
        }

        var result: [Int] = []
        for q in queries {
            let idx = q[0]
            let newVal = q[1]
            let oldVal = arr[idx]

            if oldVal != newVal {
                // remove old prime contribution
                if isPrime[oldVal] {
                    if cnt[oldVal] >= 2, let first = treapMin(roots[oldVal]), let last = treapMax(roots[oldVal]) {
                        seg.rangeAdd(first + 1, last, -1)
                    }
                    roots[oldVal] = treapDelete(roots[oldVal], idx)
                    cnt[oldVal] -= 1
                    if cnt[oldVal] == 0 {
                        distinctPrimes -= 1
                    } else if cnt[oldVal] >= 2, let first = treapMin(roots[oldVal]), let last = treapMax(roots[oldVal]) {
                        seg.rangeAdd(first + 1, last, 1)
                    }
                }

                // add new prime contribution
                if isPrime[newVal] {
                    if cnt[newVal] >= 2, let first = treapMin(roots[newVal]), let last = treapMax(roots[newVal]) {
                        seg.rangeAdd(first + 1, last, -1)
                    } else if cnt[newVal] == 0 {
                        distinctPrimes += 1
                    }
                    roots[newVal] = treapInsert(roots[newVal], idx)
                    cnt[newVal] += 1
                    if cnt[newVal] >= 2, let first = treapMin(roots[newVal]), let last = treapMax(roots[newVal]) {
                        seg.rangeAdd(first + 1, last, 1)
                    }
                }

                arr[idx] = newVal
            }

            let ans = distinctPrimes + seg.queryMax()
            result.append(ans)
        }

        return result
    }

    // MARK: - Sieve

    private func buildSieve(upTo limit: Int) {
        isPrime = Array(repeating: true, count: limit + 1)
        if limit >= 0 { isPrime[0] = false }
        if limit >= 1 { isPrime[1] = false }
        var p = 2
        while p * p <= limit {
            if isPrime[p] {
                var multiple = p * p
                while multiple <= limit {
                    isPrime[multiple] = false
                    multiple += p
                }
            }
            p += 1
        }
    }

    // MARK: - Treap Operations

    private func rotateRight(_ y: TreapNode) -> TreapNode {
        let x = y.left!
        y.left = x.right
        x.right = y
        return x
    }

    private func rotateLeft(_ x: TreapNode) -> TreapNode {
        let y = x.right!
        x.right = y.left
        y.left = x
        return y
    }

    private func treapInsert(_ root: TreapNode?, _ key: Int) -> TreapNode {
        guard let node = root else { return TreapNode(key) }
        if key < node.key {
            node.left = treapInsert(node.left, key)
            if node.left!.priority < node.priority {
                return rotateRight(node)
            }
        } else {
            node.right = treapInsert(node.right, key)
            if node.right!.priority < node.priority {
                return rotateLeft(node)
            }
        }
        return node
    }

    private func treapDelete(_ root: TreapNode?, _ key: Int) -> TreapNode? {
        guard let node = root else { return nil }
        if key < node.key {
            node.left = treapDelete(node.left, key)
            return node
        } else if key > node.key {
            node.right = treapDelete(node.right, key)
            return node
        } else {
            // node to delete
            if node.left == nil { return node.right }
            if node.right == nil { return node.left }
            if node.left!.priority < node.right!.priority {
                let newRoot = rotateRight(node)
                newRoot.right = treapDelete(newRoot.right, key)
                return newRoot
            } else {
                let newRoot = rotateLeft(node)
                newRoot.left = treapDelete(newRoot.left, key)
                return newRoot
            }
        }
    }

    private func treapMin(_ root: TreapNode?) -> Int? {
        var cur = root
        while let left = cur?.left {
            cur = left
        }
        return cur?.key
    }

    private func treapMax(_ root: TreapNode?) -> Int? {
        var cur = root
        while let right = cur?.right {
            cur = right
        }
        return cur?.key
    }
}
```

## Kotlin

```kotlin
import java.util.TreeSet
import kotlin.math.max

class Solution {
    private val MAXV = 100000
    private lateinit var isPrime: BooleanArray
    private fun sieve() {
        isPrime = BooleanArray(MAXV + 1) { true }
        isPrime[0] = false
        isPrime[1] = false
        var p = 2
        while (p * p <= MAXV) {
            if (isPrime[p]) {
                var multiple = p * p
                while (multiple <= MAXV) {
                    isPrime[multiple] = false
                    multiple += p
                }
            }
            p++
        }
    }

    private class SegTree(val n: Int) {
        private val maxVal = IntArray(4 * n)
        private val lazy = IntArray(4 * n)

        private fun push(node: Int) {
            if (lazy[node] != 0) {
                val v = lazy[node]
                val left = node shl 1
                val right = left + 1
                maxVal[left] += v
                lazy[left] += v
                maxVal[right] += v
                lazy[right] += v
                lazy[node] = 0
            }
        }

        fun add(l: Int, r: Int, delta: Int) {
            if (l > r) return
            add(1, 0, n - 1, l, r, delta)
        }

        private fun add(node: Int, nl: Int, nr: Int, l: Int, r: Int, delta: Int) {
            if (l > nr || r < nl) return
            if (l <= nl && nr <= r) {
                maxVal[node] += delta
                lazy[node] += delta
                return
            }
            push(node)
            val mid = (nl + nr) ushr 1
            add(node shl 1, nl, mid, l, r, delta)
            add(node shl 1 or 1, mid + 1, nr, l, r, delta)
            maxVal[node] = max(maxVal[node shl 1], maxVal[node shl 1 or 1])
        }

        fun queryMax(): Int = if (n > 0) maxVal[1] else 0
    }

    fun maximumCount(nums: IntArray, queries: Array<IntArray>): IntArray {
        sieve()
        val n = nums.size
        val splitCnt = n - 1
        val seg = SegTree(splitCnt)
        val primePos = HashMap<Int, TreeSet<Int>>()
        var distinctPrimes = 0

        // initial population
        for (i in nums.indices) {
            val v = nums[i]
            if (v <= MAXV && isPrime[v]) {
                val set = primePos.getOrPut(v) { TreeSet() }
                set.add(i)
            }
        }

        // compute initial distinct count and segment contributions
        for ((p, set) in primePos) {
            if (set.isNotEmpty()) distinctPrimes++
            if (set.size >= 2) {
                val first = set.first()
                val last = set.last()
                seg.add(first, last - 1, 1)
            }
        }

        val res = IntArray(queries.size)
        for (qi in queries.indices) {
            val idx = queries[qi][0]
            val newVal = queries[qi][1]
            val oldVal = nums[idx]
            if (oldVal != newVal) {
                // handle removal of old value if prime
                if (oldVal <= MAXV && isPrime[oldVal]) {
                    val setOld = primePos[oldVal]!!
                    if (setOld.size >= 2) {
                        val first = setOld.first()
                        val last = setOld.last()
                        seg.add(first, last - 1, -1)
                    }
                    setOld.remove(idx)
                    if (setOld.isEmpty()) {
                        primePos.remove(oldVal)
                        distinctPrimes--
                    } else {
                        if (setOld.size >= 2) {
                            val first = setOld.first()
                            val last = setOld.last()
                            seg.add(first, last - 1, 1)
                        }
                    }
                }

                // handle addition of new value if prime
                if (newVal <= MAXV && isPrime[newVal]) {
                    val setNew = primePos.getOrPut(newVal) { TreeSet() }
                    if (setNew.size >= 2) {
                        val first = setNew.first()
                        val last = setNew.last()
                        seg.add(first, last - 1, -1)
                    } else if (setNew.isEmpty()) {
                        distinctPrimes++
                    }
                    setNew.add(idx)
                    if (setNew.size >= 2) {
                        val first = setNew.first()
                        val last = setNew.last()
                        seg.add(first, last - 1, 1)
                    }
                }

                nums[idx] = newVal
            }
            res[qi] = distinctPrimes + seg.queryMax()
        }
        return res
    }
}
```

## Dart

```dart
import 'dart:math';

class TreapNode {
  int key;
  int priority;
  TreapNode? left;
  TreapNode? right;
  int size = 1;
  TreapNode(this.key, this.priority);
}

class Treap {
  TreapNode? root;
  final Random _rand = Random();

  int get count => _size(root);

  void insert(int key) {
    root = _insert(root, TreapNode(key, _rand.nextInt(1 << 30)));
  }

  void erase(int key) {
    root = _erase(root, key);
  }

  int? first() {
    if (root == null) return null;
    var cur = root!;
    while (cur.left != null) cur = cur.left!;
    return cur.key;
  }

  int? last() {
    if (root == null) return null;
    var cur = root!;
    while (cur.right != null) cur = cur.right!;
    return cur.key;
  }

  // internal helpers
  int _size(TreapNode? node) => node?.size ?? 0;

  void _update(TreapNode node) {
    node.size = 1 + _size(node.left) + _size(node.right);
  }

  TreapNode _merge(TreapNode? a, TreapNode? b) {
    if (a == null) return b!;
    if (b == null) return a;
    if (a.priority > b.priority) {
      a.right = _merge(a.right, b);
      _update(a);
      return a;
    } else {
      b.left = _merge(a, b.left);
      _update(b);
      return b;
    }
  }

  TreapNode _insert(TreapNode? root, TreapNode node) {
    if (root == null) return node;
    if (node.key < root.key) {
      root.left = _insert(root.left, node);
      if (root.left!.priority > root.priority) {
        root = _rotateRight(root);
      }
    } else {
      root.right = _insert(root.right, node);
      if (root.right!.priority > root.priority) {
        root = _rotateLeft(root);
      }
    }
    _update(root);
    return root;
  }

  TreapNode? _erase(TreapNode? root, int key) {
    if (root == null) return null;
    if (key == root.key) {
      return _merge(root.left, root.right);
    } else if (key < root.key) {
      root.left = _erase(root.left, key);
    } else {
      root.right = _erase(root.right, key);
    }
    if (root != null) _update(root);
    return root;
  }

  TreapNode _rotateRight(TreapNode y) {
    var x = y.left!;
    y.left = x.right;
    x.right = y;
    _update(y);
    _update(x);
    return x;
  }

  TreapNode _rotateLeft(TreapNode x) {
    var y = x.right!;
    x.right = y.left;
    y.left = x;
    _update(x);
    _update(y);
    return y;
  }
}

class SegTree {
  final int n;
  final List<int> maxv;
  final List<int> lazy;

  SegTree(this.n)
      : maxv = List.filled(4 * (n > 0 ? n : 1), 0),
        lazy = List.filled(4 * (n > 0 ? n : 1), 0);

  void _push(int node) {
    if (lazy[node] != 0) {
      int v = lazy[node];
      maxv[node << 1] += v;
      lazy[node << 1] += v;
      maxv[(node << 1) | 1] += v;
      lazy[(node << 1) | 1] += v;
      lazy[node] = 0;
    }
  }

  void _add(int node, int l, int r, int ql, int qr, int val) {
    if (ql <= l && r <= qr) {
      maxv[node] += val;
      lazy[node] += val;
      return;
    }
    _push(node);
    int mid = (l + r) >> 1;
    if (ql <= mid) _add(node << 1, l, mid, ql, qr, val);
    if (qr > mid) _add((node << 1) | 1, mid + 1, r, ql, qr, val);
    maxv[node] = max(maxv[node << 1], maxv[(node << 1) | 1]);
  }

  void addRange(int l, int r, int val) {
    if (n == 0 || l > r) return;
    _add(1, 0, n - 1, l, r, val);
  }

  int queryMax() => n == 0 ? 0 : maxv[1];
}

class Solution {
  List<int> maximumCount(List<int> nums, List<List<int>> queries) {
    final int n = nums.length;
    final int splitCnt = n - 1; // number of possible split positions
    // sieve for primes up to 100000 (max value per constraints)
    const int MAXV = 100000;
    List<bool> isPrime = List.filled(MAXV + 1, true);
    isPrime[0] = isPrime[1] = false;
    for (int i = 2; i * i <= MAXV; ++i) {
      if (isPrime[i]) {
        for (int j = i * i; j <= MAXV; j += i) isPrime[j] = false;
      }
    }

    // map prime value -> treap of indices
    final Map<int, Treap> primeMap = {};
    int distinctPrimes = 0;

    // build initial structures
    for (int i = 0; i < n; ++i) {
      int val = nums[i];
      if (!isPrime[val]) continue;
      var treap = primeMap.putIfAbsent(val, () => Treap());
      treap.insert(i);
    }

    // count distinct primes
    distinctPrimes = primeMap.length;

    // segment tree for overlap counts
    final SegTree seg = SegTree(splitCnt);

    // add initial contributions
    primeMap.forEach((p, treap) {
      if (treap.count >= 2) {
        int l = treap.first()!;
        int r = treap.last()!;
        seg.addRange(l, r - 1, 1);
      }
    });

    List<int> ans = [];

    for (var q in queries) {
      int idx = q[0];
      int newVal = q[1];
      int oldVal = nums[idx];

      if (oldVal != newVal) {
        // remove old prime contribution
        if (isPrime[oldVal]) {
          var treap = primeMap[oldVal]!;
          if (treap.count >= 2) {
            int l = treap.first()!;
            int r = treap.last()!;
            seg.addRange(l, r - 1, -1);
          }
          treap.erase(idx);
          if (treap.count == 0) {
            primeMap.remove(oldVal);
            distinctPrimes--;
          } else if (treap.count >= 2) {
            int l = treap.first()!;
            int r = treap.last()!;
            seg.addRange(l, r - 1, 1);
          }
        }

        // add new prime contribution
        if (isPrime[newVal]) {
          var treap = primeMap.putIfAbsent(newVal, () => Treap());
          if (treap.count >= 2) {
            int l = treap.first()!;
            int r = treap.last()!;
            seg.addRange(l, r - 1, -1);
          }
          bool wasEmpty = treap.count == 0;
          treap.insert(idx);
          if (wasEmpty) distinctPrimes++;
          if (treap.count >= 2) {
            int l = treap.first()!;
            int r = treap.last()!;
            seg.addRange(l, r - 1, 1);
          }
        }

        nums[idx] = newVal;
      }

      int currentMaxOverlap = seg.queryMax();
      ans.add(distinctPrimes + currentMaxOverlap);
    }

    return ans;
  }
}
```

## Golang

```go
package main

import (
	"container/heap"
)

type MinHeap []int

func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h MinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *MinHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}
func (h *MinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

type MaxHeap []int

func (h MaxHeap) Len() int           { return len(h) }
func (h MaxHeap) Less(i, j int) bool { return h[i] > h[j] } // reverse
func (h MaxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *MaxHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}
func (h *MaxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

type PrimeInfo struct {
	cnt     int
	present map[int]bool
	minH    *MinHeap
	maxH    *MaxHeap
}

func (p *PrimeInfo) first() int {
	for p.minH.Len() > 0 {
		v := (*p.minH)[0]
		if p.present[v] {
			return v
		}
		heap.Pop(p.minH)
	}
	return -1
}
func (p *PrimeInfo) last() int {
	for p.maxH.Len() > 0 {
		v := (*p.maxH)[0]
		if p.present[v] {
			return v
		}
		heap.Pop(p.maxH)
	}
	return -1
}
func (p *PrimeInfo) insert(idx int) {
	if p.present == nil {
		p.present = make(map[int]bool)
	}
	p.present[idx] = true
	p.cnt++
	heap.Push(p.minH, idx)
	heap.Push(p.maxH, idx)
}
func (p *PrimeInfo) remove(idx int) {
	if !p.present[idx] {
		return
	}
	delete(p.present, idx)
	p.cnt--
}

type SegTree struct {
	n    int
	max  []int
	lazy []int
}

func NewSegTree(size int) *SegTree {
	n := 1
	for n < size {
		n <<= 1
	}
	return &SegTree{
		n:    n,
		max:  make([]int, 2*n),
		lazy: make([]int, 2*n),
	}
}
func (st *SegTree) apply(node, val int) {
	st.max[node] += val
	st.lazy[node] += val
}
func (st *SegTree) push(node int) {
	if st.lazy[node] != 0 {
		st.apply(node*2, st.lazy[node])
		st.apply(node*2+1, st.lazy[node])
		st.lazy[node] = 0
	}
}
func (st *SegTree) rangeAdd(l, r, val int) {
	if l > r {
		return
	}
	st.rangeAddRec(1, 0, st.n-1, l, r, val)
}
func (st *SegTree) rangeAddRec(node, nl, nr, l, r, val int) {
	if l > nr || r < nl {
		return
	}
	if l <= nl && nr <= r {
		st.apply(node, val)
		return
	}
	st.push(node)
	mid := (nl + nr) >> 1
	st.rangeAddRec(node*2, nl, mid, l, r, val)
	st.rangeAddRec(node*2+1, mid+1, nr, l, r, val)
	if st.max[node*2] > st.max[node*2+1] {
		st.max[node] = st.max[node*2]
	} else {
		st.max[node] = st.max[node*2+1]
	}
}
func (st *SegTree) queryMax() int {
	return st.max[1]
}

func maximumCount(nums []int, queries [][]int) []int {
	const maxV = 100000
	isPrime := make([]bool, maxV+1)
	for i := 2; i <= maxV; i++ {
		isPrime[i] = true
	}
	for p := 2; p*p <= maxV; p++ {
		if isPrime[p] {
			for multiple := p * p; multiple <= maxV; multiple += p {
				isPrime[multiple] = false
			}
		}
	}

	n := len(nums)
	var seg *SegTree
	if n > 1 {
		seg = NewSegTree(n - 1)
	}
	infos := make([]*PrimeInfo, maxV+1)

	D := 0 // distinct primes count

	// initial insertion
	for idx, v := range nums {
		if !isPrime[v] {
			continue
		}
		pi := infos[v]
		if pi == nil {
			minH := &MinHeap{}
			maxH := &MaxHeap{}
			heap.Init(minH)
			heap.Init(maxH)
			pi = &PrimeInfo{present: make(map[int]bool), minH: minH, maxH: maxH}
			infos[v] = pi
		}
		if pi.cnt == 0 {
			D++
		}
		pi.insert(idx)
	}

	// add intervals for primes with >=2 occurrences
	if n > 1 {
		for v := 2; v <= maxV; v++ {
			if !isPrime[v] {
				continue
			}
			pi := infos[v]
			if pi != nil && pi.cnt >= 2 {
				l := pi.first()
				r := pi.last() - 1
				if l <= r {
					seg.rangeAdd(l, r, 1)
				}
			}
		}
	}

	ans := make([]int, len(queries))
	for qi, q := range queries {
		idx, val := q[0], q[1]
		old := nums[idx]
		if old != val {
			// remove old prime contribution
			if isPrime[old] {
				pi := infos[old]
				if pi.cnt >= 2 && n > 1 {
					l := pi.first()
					r := pi.last() - 1
					if l <= r {
						seg.rangeAdd(l, r, -1)
					}
				}
				pi.remove(idx)
				if pi.cnt >= 2 && n > 1 {
					l := pi.first()
					r := pi.last() - 1
					if l <= r {
						seg.rangeAdd(l, r, 1)
					}
				} else if pi.cnt == 0 {
					D--
				}
			}
			// add new prime contribution
			if isPrime[val] {
				pi := infos[val]
				if pi == nil {
					minH := &MinHeap{}
					maxH := &MaxHeap{}
					heap.Init(minH)
					heap.Init(maxH)
					pi = &PrimeInfo{present: make(map[int]bool), minH: minH, maxH: maxH}
					infos[val] = pi
				}
				if pi.cnt >= 2 && n > 1 {
					l := pi.first()
					r := pi.last() - 1
					if l <= r {
						seg.rangeAdd(l, r, -1)
					}
				}
				if pi.cnt == 0 {
					D++
				}
				pi.insert(idx)
				if pi.cnt >= 2 && n > 1 {
					l := pi.first()
					r := pi.last() - 1
					if l <= r {
						seg.rangeAdd(l, r, 1)
					}
				}
			}
			nums[idx] = val
		}
		maxOverlap := 0
		if n > 1 {
			maxOverlap = seg.queryMax()
		}
		ans[qi] = D + maxOverlap
	}
	return ans
}
```

## Ruby

```ruby
require 'set'

# Sieve of Eratosthenes for primality up to 1e5
MAX_VAL = 100_000
is_prime = Array.new(MAX_VAL + 1, true)
is_prime[0] = is_prime[1] = false
(2..Math.sqrt(MAX_VAL).to_i).each do |i|
  next unless is_prime[i]
  (i*i).step(MAX_VAL, i) { |j| is_prime[j] = false }
end

class SegTree
  def initialize(n)
    @n = n
    size = 4 * (n + 5)
    @max = Array.new(size, 0)
    @lazy = Array.new(size, 0)
  end

  def range_add(l, r, val)
    return if l > r
    add(1, 0, @n, l, r, val)
  end

  def query_max
    @max[1]
  end

  private

  def push(node)
    v = @lazy[node]
    return if v == 0
    left = node * 2
    right = left + 1
    @max[left] += v
    @lazy[left] += v
    @max[right] += v
    @lazy[right] += v
    @lazy[node] = 0
  end

  def add(node, nl, nr, l, r, val)
    if l <= nl && nr <= r
      @max[node] += val
      @lazy[node] += val
      return
    end
    push(node)
    mid = (nl + nr) / 2
    if l <= mid
      add(node * 2, nl, mid, l, r, val)
    end
    if r > mid
      add(node * 2 + 1, mid + 1, nr, l, r, val)
    end
    @max[node] = [@max[node * 2], @max[node * 2 + 1]].max
  end
end

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer[]}
def maximum_count(nums, queries)
  n = nums.length
  seg = SegTree.new(n)               # split positions 0..n
  prime_sets = Hash.new { |h, k| h[k] = SortedSet.new }
  distinct_primes = 0

  # build initial sets and intervals
  nums.each_with_index do |v, i|
    next unless is_prime[v]
    set = prime_sets[v]
    set.add(i)
  end

  prime_sets.each do |p, set|
    if set.size > 0
      distinct_primes += 1
    end
    if set.size >= 2
      l = set.first
      r = set.last
      seg.range_add(l + 1, r, 1)
    end
  end

  answers = []

  queries.each do |idx, val|
    old = nums[idx]

    # handle removal of old value if prime
    if is_prime[old]
      s = prime_sets[old]
      if s.size >= 2
        l = s.first
        r = s.last
        seg.range_add(l + 1, r, -1)
      end
      s.delete(idx)

      if s.empty?
        distinct_primes -= 1
        prime_sets.delete(old)
      else
        if s.size >= 2
          l = s.first
          r = s.last
          seg.range_add(l + 1, r, 1)
        end
      end
    end

    nums[idx] = val

    # handle insertion of new value if prime
    if is_prime[val]
      s = (prime_sets[val] ||= SortedSet.new)

      if s.size >= 2
        l = s.first
        r = s.last
        seg.range_add(l + 1, r, -1)
      end

      before_empty = s.empty?
      s.add(idx)

      distinct_primes += 1 if before_empty
      if s.size >= 2
        l = s.first
        r = s.last
        seg.range_add(l + 1, r, 1)
      end
    end

    answers << (distinct_primes + seg.query_max)
  end

  answers
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable
  import java.util.{TreeSet => JTreeSet}

  private class SegTree(val n: Int) {
    private val size: Int = {
      var s = 1
      while (s < n) s <<= 1
      s
    }
    private val maxArr = new Array[Int](size << 1)
    private val lazy = new Array[Int](size << 1)

    private def apply(node: Int, v: Int): Unit = {
      maxArr(node) += v
      lazy(node) += v
    }

    private def push(node: Int): Unit = {
      if (lazy(node) != 0) {
        apply(node << 1, lazy(node))
        apply(node << 1 | 1, lazy(node))
        lazy(node) = 0
      }
    }

    private def pull(node: Int): Unit = {
      maxArr(node) = math.max(maxArr(node << 1), maxArr(node << 1 | 1))
    }

    // add v to range [l, r] inclusive
    def add(l: Int, r: Int, v: Int): Unit = {
      if (l > r || n == 0) return
      add(1, 0, size - 1, l, r, v)
    }

    private def add(node: Int, nl: Int, nr: Int, l: Int, r: Int, v: Int): Unit = {
      if (l <= nl && nr <= r) {
        apply(node, v)
        return
      }
      push(node)
      val mid = (nl + nr) >> 1
      if (l <= mid) add(node << 1, nl, mid, l, r, v)
      if (r > mid) add(node << 1 | 1, mid + 1, nr, l, r, v)
      pull(node)
    }

    def queryMax(): Int = {
      if (n == 0) 0 else maxArr(1)
    }
  }

  def maximumCount(nums: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
    val n = nums.length
    if (n <= 1) return Array.fill(queries.length)(0)

    // sieve for primes up to 100000
    val limit = 100000
    val isPrime = new Array[Boolean](limit + 1)
    java.util.Arrays.fill(isPrime, true)
    isPrime(0) = false
    isPrime(1) = false
    var p = 2
    while (p * p <= limit) {
      if (isPrime(p)) {
        var mul = p * p
        while (mul <= limit) {
          isPrime(mul) = false
          mul += p
        }
      }
      p += 1
    }

    // map prime -> positions set
    val posMap = mutable.HashMap[Int, JTreeSet[Int]]()
    for (i <- nums.indices) {
      val v = nums(i)
      if (isPrime(v)) {
        val set = posMap.getOrElseUpdate(v, new JTreeSet[Int]())
        set.add(i)
      }
    }

    var distinctPrimeCnt = posMap.size
    val seg = new SegTree(n - 1)

    // initial intervals for primes appearing at least twice
    for ((prime, set) <- posMap) {
      if (set.size() >= 2) {
        seg.add(set.first(), set.last() - 1, 1)
      }
    }

    val res = new Array[Int](queries.length)
    val arr = nums.clone()

    for (qi <- queries.indices) {
      val idx = queries(qi)(0)
      val vNew = queries(qi)(1)
      val vOld = arr(idx)

      if (vOld != vNew) {
        // remove old value contribution
        if (isPrime(vOld)) {
          val set = posMap(vOld)
          if (set.size() >= 2) {
            seg.add(set.first(), set.last() - 1, -1)
          }
          set.remove(idx)
          if (set.isEmpty) {
            posMap -= vOld
            distinctPrimeCnt -= 1
          } else {
            if (set.size() >= 2) {
              seg.add(set.first(), set.last() - 1, 1)
            }
          }
        }

        // add new value contribution
        if (isPrime(vNew)) {
          val set = posMap.getOrElseUpdate(vNew, new JTreeSet[Int]())
          if (set.size() >= 2) {
            seg.add(set.first(), set.last() - 1, -1)
          }
          val wasEmpty = set.isEmpty
          set.add(idx)
          if (wasEmpty) distinctPrimeCnt += 1
          if (set.size() >= 2) {
            seg.add(set.first(), set.last() - 1, 1)
          }
        }

        arr(idx) = vNew
      }

      res(qi) = distinctPrimeCnt + seg.queryMax()
    }

    res
  }
}
```

## Rust

```rust
use std::collections::{BTreeSet, HashMap};

pub struct SegTree {
    n: usize,
    max: Vec<i32>,
    lazy: Vec<i32>,
}

impl SegTree {
    fn new(size: usize) -> Self {
        let n = size.next_power_of_two().max(1);
        SegTree {
            n,
            max: vec![0; 2 * n],
            lazy: vec![0; 2 * n],
        }
    }

    fn push(&mut self, idx: usize) {
        let val = self.lazy[idx];
        if val != 0 {
            let left = idx << 1;
            let right = left | 1;
            self.max[left] += val;
            self.max[right] += val;
            self.lazy[left] += val;
            self.lazy[right] += val;
            self.lazy[idx] = 0;
        }
    }

    fn add_rec(&mut self, idx: usize, l: usize, r: usize, ql: usize, qr: usize, val: i32) {
        if ql > r || qr < l {
            return;
        }
        if ql <= l && r <= qr {
            self.max[idx] += val;
            self.lazy[idx] += val;
            return;
        }
        self.push(idx);
        let mid = (l + r) >> 1;
        self.add_rec(idx << 1, l, mid, ql, qr, val);
        self.add_rec((idx << 1) | 1, mid + 1, r, ql, qr, val);
        self.max[idx] = self.max[idx << 1].max(self.max[(idx << 1) | 1]);
    }

    fn add(&mut self, l: usize, r: usize, val: i32) {
        if l > r || self.n == 0 {
            return;
        }
        let size = self.n;
        self.add_rec(1, 0, size - 1, l, r, val);
    }

    fn query_max(&self) -> i32 {
        if self.n == 0 {
            0
        } else {
            self.max[1]
        }
    }
}

impl Solution {
    pub fn maximum_count(mut nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = nums.len();
        if n < 2 {
            return vec![0; queries.len()];
        }

        // sieve for primes up to 100000
        const MAXV: usize = 100_000;
        let mut is_prime = vec![true; MAXV + 1];
        is_prime[0] = false;
        is_prime[1] = false;
        for i in 2..=MAXV {
            if is_prime[i] {
                let mut j = i * i;
                while j <= MAXV {
                    is_prime[j] = false;
                    j += i;
                }
            }
        }

        // map prime value -> ordered set of indices
        let mut pos_map: Vec<Option<BTreeSet<usize>>> = vec![None; MAXV + 1];

        for (i, &v) in nums.iter().enumerate() {
            let v_usize = v as usize;
            if is_prime[v_usize] {
                let entry = pos_map[v_usize].get_or_insert_with(BTreeSet::new);
                entry.insert(i);
            }
        }

        // segment tree over split positions [0, n-2]
        let mut seg = SegTree::new(n - 1);

        // initial intervals
        for v in 2..=MAXV {
            if is_prime[v] {
                if let Some(set) = &pos_map[v] {
                    if set.len() >= 2 {
                        let first = *set.iter().next().unwrap();
                        let last = *set.iter().next_back().unwrap();
                        seg.add(first, last - 1, 1);
                    }
                }
            }
        }

        let mut ans = Vec::with_capacity(queries.len());

        for q in queries {
            let idx = q[0] as usize;
            let new_val = q[1];
            let old_val = nums[idx];
            if old_val != new_val {
                // remove contribution of old prime (if any)
                let old_usize = old_val as usize;
                if is_prime[old_usize] {
                    if let Some(set) = &mut pos_map[old_usize] {
                        if set.len() >= 2 {
                            let first = *set.iter().next().unwrap();
                            let last = *set.iter().next_back().unwrap();
                            seg.add(first, last - 1, -1);
                        }
                        set.remove(&idx);
                        if set.len() >= 2 {
                            let first = *set.iter().next().unwrap();
                            let last = *set.iter().next_back().unwrap();
                            seg.add(first, last - 1, 1);
                        }
                    }
                }

                // add contribution of new prime (if any)
                let new_usize = new_val as usize;
                if is_prime[new_usize] {
                    let entry = pos_map[new_usize].get_or_insert_with(BTreeSet::new);
                    if entry.len() >= 2 {
                        let first = *entry.iter().next().unwrap();
                        let last = *entry.iter().next_back().unwrap();
                        seg.add(first, last - 1, -1);
                    }
                    entry.insert(idx);
                    if entry.len() >= 2 {
                        let first = *entry.iter().next().unwrap();
                        let last = *entry.iter().next_back().unwrap();
                        seg.add(first, last - 1, 1);
                    }
                }

                nums[idx] = new_val;
            }

            ans.push(seg.query_max());
        }

        ans
    }
}
```

## Racket

```racket
(require racket/vector)
(require racket/list)
(require data/ordered-set)

;; Sieve of Eratosthenes up to 100000
(define max-val 100000)
(define is-prime (make-vector (+ max-val 1) #t))
(vector-set! is-prime 0 #f)
(vector-set! is-prime 1 #f)
(for ([i (in-range 2 (add1 (sqrt max-val)))])
  (when (vector-ref is-prime i)
    (for ([j (in-range (* i i) (+ max-val 1) i)])
      (vector-set! is-prime j #f))))

;; Segment tree with lazy propagation for range add and global max query
(struct seg-node (l r max lazy left right) #:mutable)

(define (build-seg l r)
  (if (= l r)
      (seg-node l r 0 0 #f #f)
      (let* ([mid (quotient (+ l r) 2)]
             [left (build-seg l mid)]
             [right (build-seg (add1 mid) r)])
        (seg-node l r 0 0 left right))))

(define (push node)
  (when (and (seg-node-left node) (> (seg-node-lazy node) 0))
    (for-each
     (lambda (child)
       (set-seg-node-max! child (+ (seg-node-max child) (seg-node-lazy node)))
       (set-seg-node-lazy! child (+ (seg-node-lazy child) (seg-node-lazy node))))
     (list (seg-node-left node) (seg-node-right node)))
    (set-seg-node-lazy! node 0)))

(define (pull node)
  (let ([lmax (seg-node-max (seg-node-left node))]
        [rmax (seg-node-max (seg-node-right node))])
    (set-seg-node-max! node (max lmax rmax))))

(define (range-add! node ql qr delta)
  (let ([l (seg-node-l node)] [r (seg-node-r node)])
    (cond
      [(> ql r) (void)]
      [(< qr l) (void)]
      [(<= ql l) (when (>= r qr)
                   (set-seg-node-max! node (+ (seg-node-max node) delta))
                   (set-seg-node-lazy! node (+ (seg-node-lazy node) delta)))]
      [else
       (push node)
       (range-add! (seg-node-left node) ql qr delta)
       (range-add! (seg-node-right node) ql qr delta)
       (pull node)])))

(define (global-max node)
  (seg-node-max node))

;; Main function
(define/contract (maximum-count nums queries)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ([n (length nums)]
         [vec (list->vector nums)]
         [prime-pos (make-hash)] ; prime -> ordered-set of indices
         ;; build initial sets
         (for ([i (in-range n)])
           (let ([v (vector-ref vec i)])
             (when (and (<= 0 v) (< v (vector-length is-prime)) (vector-ref is-prime v))
               (define s (hash-ref prime-pos v (lambda () (let ((ns (make-ordered-set <))) (hash-set! prime-pos v ns) ns))))
               (ordered-set-add! s i)))))
         ;; segment tree over split positions 0 .. n-2
         [seg-root (if (> n 1) (build-seg 0 (sub1 n)) (void))]
         ;; add contributions of existing primes
         (for ([kv (in-hash prime-pos)])
           (define s (cdr kv))
           (when (>= (ordered-set-size s) 2)
             (define first (ordered-set-min s))
             (define last (ordered-set-max s))
             (range-add! seg-root first (sub1 last) 1)))
         ;; process queries
         [answers (let loop ([qs queries] [acc '()])
                    (if (null? qs)
                        (reverse acc)
                        (let* ([q (car qs)]
                               [idx (list-ref q 0)]
                               [newval (list-ref q 1)]
                               [oldval (vector-ref vec idx)])
                          ;; remove old value contribution
                          (when (and (<= 0 oldval) (< oldval (vector-length is-prime)) (vector-ref is-prime oldval))
                            (define s (hash-ref prime-pos oldval))
                            (when (>= (ordered-set-size s) 2)
                              (range-add! seg-root (ordered-set-min s) (sub1 (ordered-set-max s)) -1))
                            (ordered-set-remove! s idx)
                            (if (ordered-set-empty? s)
                                (hash-remove! prime-pos oldval)
                                (when (>= (ordered-set-size s) 2)
                                  (range-add! seg-root (ordered-set-min s) (sub1 (ordered-set-max s)) 1)))))
                          ;; add new value contribution
                          (when (and (<= 0 newval) (< newval (vector-length is-prime)) (vector-ref is-prime newval))
                            (define s (hash-ref prime-pos newval (lambda () (let ((ns (make-ordered-set <))) (hash-set! prime-pos newval ns) ns))))
                            (when (>= (ordered-set-size s) 2)
                              (range-add! seg-root (ordered-set-min s) (sub1 (ordered-set-max s)) -1))
                            (ordered-set-add! s idx)
                            (when (>= (ordered-set-size s) 2)
                              (range-add! seg-root (ordered-set-min s) (sub1 (ordered-set-max s)) 1)))
                          ;; update array
                          (vector-set! vec idx newval)
                          ;; current answer
                          (define cur-ans (if (> n 1) (global-max seg-root) 0))
                          (loop (cdr qs) (cons cur-ans acc)))) )])
    answers))
```

## Erlang

```erlang
-spec maximum_count(Nums :: [integer()], Queries :: [[integer()]]) -> [integer()].
maximum_count(Nums, Queries) ->
    MaxVal = max_list([lists:max(Nums) | [V || [_Idx, V] <- Queries]]),
    PrimeSet = sieve(MaxVal),
    N = length(Nums),
    Arr0 = array:from_list(Nums),
    % Build prime occurrence map
    {PrimeMap0, Distinct0} = build_prime_map(Nums, 0, PrimeSet, #{}),
    % Build segment tree over positions 0..N-2 (if N>=2)
    Seg0 = case N > 1 of
        true -> build_seg(1, 0, N - 2, #{});
        false -> #{}
    end,
    % Add initial intervals to segment tree
    Seg1 = add_all_intervals(PrimeMap0, Seg0),
    % Process queries
    {AnsRev, _ArrFinal, _PrimeMapFinal, _DistinctFinal, _SegFinal} =
        lists:foldl(fun([Idx, Val], {Acc, Arr, PrimeMap, Distinct, Seg}) ->
            OldVal = array:get(Idx, Arr),
            {Seg1, PrimeMap1, Distinct1} = 
                if OldVal =:= Val -> {Seg, PrimeMap, Distinct};
                   true ->
                       {SegA, PrimeMapA, DistinctA} = maybe_remove(OldVal, Idx, Seg, PrimeMap, Distinct, PrimeSet),
                       {SegB, PrimeMapB, DistinctB} = maybe_add(Val, Idx, SegA, PrimeMapA, DistinctA, PrimeSet),
                       {SegB, PrimeMapB, DistinctB}
                end,
            Arr1 = array:set(Idx, Val, Arr),
            RootNode = maps:get(1, Seg1, #{max=>0}),
            MaxOverlap = maps:get(max, RootNode, 0),
            Answer = Distinct1 + MaxOverlap,
            {[Answer | Acc], Arr1, PrimeMap1, Distinct1, Seg1}
        end, {[], Arr0, PrimeMap0, Distinct0, Seg1}, Queries),
    lists:reverse(AnsRev).

%% Build prime set using sieve
sieve(Limit) ->
    IsPrime = lists:foldl(fun(I, Acc) -> maps:put(I, true, Acc) end, #{2 => true}, lists:seq(3, Limit)),
    SieveFun = fun(F, P, Max) when P * P =< Max ->
        case maps:get(P, IsPrime, false) of
            true ->
                NewAcc = mark_multiples(IsPrime, P*P, P, Max),
                F(F, P+1, Max);
            false -> F(F, P+1, Max)
        end;
        (_, _, _) -> IsPrime
    end,
    SieveFun(SieveFun, 2, Limit).

mark_multiples(Map, Start, Step, Max) when Start =< Max ->
    NewMap = maps:remove(Start, Map),
    mark_multiples(NewMap, Start+Step, Step, Max);
mark_multiples(Map, _Start, _Step, _Max) -> Map.

max_list([H|T]) -> lists:max([H|T]).

%% Build initial prime occurrence map and distinct count
build_prime_map([], Index, _PrimeSet, AccMap) ->
    {AccMap, maps:size(AccMap)};
build_prime_map([Val|Rest], Index, PrimeSet, AccMap) ->
    NewMap = case maps:get(Val, PrimeSet, false) of
        true ->
            Tree0 = maps:get(Val, AccMap, gb_trees:empty()),
            Tree1 = gb_trees:enter(Index, true, Tree0),
            maps:put(Val, Tree1, AccMap);
        false -> AccMap
    end,
    build_prime_map(Rest, Index+1, PrimeSet, NewMap).

%% Build segment tree recursively
build_seg(Node, L, R, Seg) when L =:= R ->
    NodeMap = #{l=>L, r=>R, max=>0, lazy=>0},
    maps:put(Node, NodeMap, Seg);
build_seg(Node, L, R, Seg) ->
    Mid = (L + R) div 2,
    Seg1 = build_seg(Node*2, L, Mid, Seg),
    Seg2 = build_seg(Node*2+1, Mid+1, R, Seg1),
    NodeMap = #{l=>L, r=>R, max=>0, lazy=>0},
    maps:put(Node, NodeMap, Seg2).

%% Add all intervals from prime map to segment tree
add_all_intervals(PrimeMap, Seg) ->
    maps:fold(fun(_P, Tree, AccSeg) ->
        case gb_trees:size(Tree) >= 2 of
            true ->
                {First,_} = gb_trees:smallest(Tree),
                {Last,_} = gb_trees:largest(Tree),
                range_add(AccSeg, 1, First, Last-1, 1);
            false -> AccSeg
        end
    end, Seg, PrimeMap).

%% Remove old prime contribution if needed
maybe_remove(Val, Idx, Seg, PrimeMap, Distinct, PrimeSet) ->
    case maps:get(Val, PrimeSet, false) of
        true ->
            Tree0 = maps:get(Val, PrimeMap),
            % remove previous interval
            Seg1 = case gb_trees:size(Tree0) >= 2 of
                true ->
                    {F,_} = gb_trees:smallest(Tree0),
                    {L,_} = gb_trees:largest(Tree0),
                    range_add(Seg, 1, F, L-1, -1);
                false -> Seg
            end,
            Tree1 = gb_trees:delete_any(Idx, Tree0),
            {Seg2, PrimeMap2, Distinct2} =
                case gb_trees:size(Tree1) of
                    0 ->
                        {Seg1, maps:remove(Val, PrimeMap), Distinct-1};
                    _ ->
                        % add new interval if still >=2
                        SegNew = case gb_trees:size(Tree1) >= 2 of
                            true ->
                                {F2,_} = gb_trees:smallest(Tree1),
                                {L2,_} = gb_trees:largest(Tree1),
                                range_add(Seg1, 1, F2, L2-1, 1);
                            false -> Seg1
                        end,
                        {SegNew, maps:put(Val, Tree1, PrimeMap), Distinct}
                end,
            {Seg2, PrimeMap2, Distinct2};
        false -> {Seg, PrimeMap, Distinct}
    end.

%% Add new prime contribution if needed
maybe_add(Val, Idx, Seg, PrimeMap, Distinct, PrimeSet) ->
    case maps:get(Val, PrimeSet, false) of
        true ->
            Tree0 = maps:get(Val, PrimeMap, gb_trees:empty()),
            % remove old interval if existed
            Seg1 = case gb_trees:size(Tree0) >= 2 of
                true ->
                    {F,_} = gb_trees:smallest(Tree0),
                    {L,_} = gb_trees:largest(Tree0),
                    range_add(Seg, 1, F, L-1, -1);
                false -> Seg
            end,
            Tree1 = gb_trees:enter(Idx, true, Tree0),
            Distinct1 = case gb_trees:size(Tree0) of
                0 -> Distinct + 1;
                _ -> Distinct
            end,
            % add new interval if now >=2
            Seg2 = case gb_trees:size(Tree1) >= 2 of
                true ->
                    {F2,_} = gb_trees:smallest(Tree1),
                    {L2,_} = gb_trees:largest(Tree1),
                    range_add(Seg1, 1, F2, L2-1, 1);
                false -> Seg1
            end,
            PrimeMap2 = maps:put(Val, Tree1, PrimeMap),
            {Seg2, PrimeMap2, Distinct1};
        false -> {Seg, PrimeMap, Distinct}
    end.

%% Range add with lazy propagation
range_add(Seg, Node, L, R, Delta) when L > R ->
    Seg;
range_add(Seg, Node, QL, QR, Delta) ->
    NodeMap = maps:get(Node, Seg),
    L = maps:get(l, NodeMap),
    R = maps:get(r, NodeMap),
    case (QL =< L) andalso (R =< QR) of
        true ->
            NewMax = maps:get(max, NodeMap) + Delta,
            NewLazy = maps:get(lazy, NodeMap) + Delta,
            NewNodeMap = NodeMap#{max=>NewMax, lazy=>NewLazy},
            maps:put(Node, NewNodeMap, Seg);
        false ->
            % push lazy to children if any
            Seg1 = case maps:get(lazy, NodeMap) of
                0 -> Seg;
                LazyVal ->
                    LeftId = Node*2,
                    RightId = Node*2+1,
                    LChild = maps:get(LeftId, Seg),
                    RChild = maps:get(RightId, Seg),
                    NewLChild = LChild#{max=>maps:get(max, LChild)+LazyVal,
                                        lazy=>maps:get(lazy, LChild)+LazyVal},
                    NewRChild = RChild#{max=>maps:get(max, RChild)+LazyVal,
                                        lazy=>maps:get(lazy, RChild)+LazyVal},
                    SegTmp1 = maps:put(LeftId, NewLChild, Seg),
                    SegTmp2 = maps:put(RightId, NewRChild, SegTmp1),
                    maps:put(Node, NodeMap#{lazy=>0}, SegTmp2)
            end,
            Mid = (L + R) div 2,
            SegLeft = if QL =< Mid -> range_add(Seg1, Node*2, QL, QR, Delta) else Seg1 end,
            SegBoth = if QR > Mid -> range_add(SegLeft, Node*2+1, QL, QR, Delta) else SegLeft end,
            LeftNode = maps:get(Node*2, SegBoth),
            RightNode = maps:get(Node*2+1, SegBoth),
            NewMax = erlang:max(maps:get(max, LeftNode), maps:get(max, RightNode)),
            UpdatedNodeMap = NodeMap#{max=>NewMax},
            maps:put(Node, UpdatedNodeMap, SegBoth)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_count(nums :: [integer], queries :: [[integer]]) :: [integer]
  def maximum_count(nums, queries) do
    max_val = 100_000
    spf = build_spf(max_val)

    n = length(nums)
    arr = :array.from_list(nums)
    size_k = n - 1
    seg = SegTree.new(size_k)

    # Build prime occurrence map
    {prime_map, _} =
      Enum.reduce(Enum.with_index(nums), {%{}, nil}, fn {val, idx}, {pm, _} ->
        primes = prime_factors(val, spf)

        pm =
          Enum.reduce(primes, pm, fn p, acc ->
            tree = Map.get(acc, p, :gb_trees.empty())
            tree = :gb_trees.enter(idx, true, tree)
            Map.put(acc, p, tree)
          end)

        {pm, nil}
      end)

    distinct_cnt = map_size(prime_map)

    # Initialize segment tree with existing overlapping primes
    seg =
      Enum.reduce(prime_map, seg, fn {_p, tree}, acc ->
        cnt = :gb_trees.size(tree)

        if cnt >= 2 do
          {first, _} = :gb_trees.smallest(tree)
          {last, _} = :gb_trees.largest(tree)
          SegTree.update(acc, first, last - 1, 1)
        else
          acc
        end
      end)

    # Process queries
    {_final_arr, _final_map, _final_distinct, _final_seg, rev_res} =
      Enum.reduce(queries, {arr, prime_map, distinct_cnt, seg, []}, fn [idx, val],
                                                                      {a,
                                                                       m,
                                                                       dcnt,
                                                                       st,
                                                                       res} ->
        old = :array.get(idx, a)

        if old == val do
          max_overlap = SegTree.max(st)
          {a, m, dcnt, st, [dcnt + max_overlap | res]}
        else
          old_primes = MapSet.new(prime_factors(old, spf))
          new_primes = MapSet.new(prime_factors(val, spf))
          affected = MapSet.union(old_primes, new_primes)

          {m2, dcnt2, st2} =
            Enum.reduce(affected, {m, dcnt, st}, fn p,
                                                   {mp, dc, sst} ->
              tree = Map.get(mp, p, :gb_trees.empty())
              cnt_before = :gb_trees.size(tree)

              {first_before, _} =
                if cnt_before > 0 do
                  :gb_trees.smallest(tree)
                else
                  {nil, nil}
                end

              {last_before, _} =
                if cnt_before > 0 do
                  :gb_trees.largest(tree)
                else
                  {nil, nil}
                end

              tree =
                if MapSet.member?(old_primes, p) do
                  :gb_trees.delete(idx, tree)
                else
                  tree
                end

              tree =
                if MapSet.member?(new_primes, p) do
                  :gb_trees.enter(idx, true, tree)
                else
                  tree
                end

              cnt_after = :gb_trees.size(tree)

              {first_after, _} =
                if cnt_after > 0 do
                  :gb_trees.smallest(tree)
                else
                  {nil, nil}
                end

              {last_after, _} =
                if cnt_after > 0 do
                  :gb_trees.largest(tree)
                else
                  {nil, nil}
                end

              sst =
                if cnt_before >= 2 do
                  SegTree.update(sst, first_before, last_before - 1, -1)
                else
                  sst
                end

              sst =
                if cnt_after >= 2 do
                  SegTree.update(sst, first_after, last_after - 1, 1)
                else
                  sst
                end

              dc =
                cond do
                  cnt_before == 0 and cnt_after > 0 -> dc + 1
                  cnt_before > 0 and cnt_after == 0 -> dc - 1
                  true -> dc
                end

              mp2 =
                if cnt_after == 0 do
                  Map.delete(mp, p)
                else
                  Map.put(mp, p, tree)
                end

              {mp2, dc, sst}
            end)

          a2 = :array.set(idx, val, a)
          max_overlap = SegTree.max(st2)
          {a2, m2, dcnt2, st2, [dcnt2 + max_overlap | res]}
        end
      end)

    Enum.reverse(rev_res)
  end

  # Build smallest prime factor array up to limit
  defp build_spf(limit) do
    spf = :array.new(limit + 1, default: 0)

    spf =
      Enum.reduce(2..limit, spf, fn i, arr ->
        if :array.get(i, arr) == 0 do
          # i is prime
          Enum.reduce(i..limit//i, arr, fn j, a2 ->
            if rem(j, i) == 0 and :array.get(j, a2) == 0 do
              :array.set(j, i, a2)
            else
              a2
            end
          end)
        else
          arr
        end
      end)

    spf
  end

  # Return distinct prime factors of x using spf array
  defp prime_factors(1, _), do: []

  defp prime_factors(x, spf) do
    p = :array.get(x, spf)
    rest = divide_out(x, p)
    [p | prime_factors(rest, spf)]
  end

  defp divide_out(x, p) do
    if rem(x, p) == 0 do
      divide_out(div(x, p), p)
    else
      x
    end
  end

  # Segment tree with range add and global max query
  defmodule SegTree do
    defstruct n: 0, max: nil, lazy: nil

    def new(0), do: %SegTree{n: 0, max: :array.new(1, default: 0), lazy: :array.new(1, default: 0)}
    def new(n) when n > 0 do
      size = 4 * n
      %SegTree{
        n: n,
        max: :array.new(size + 2, default: 0),
        lazy: :array.new(size + 2, default: 0)
      }
    end

    def update(tree, l, r, _val) when l > r or tree.n == 0, do: tree
    def update(tree, l, r, val), do: do_update(tree, 1, 0, tree.n - 1, l, r, val)

    defp do_update(tree, node, nl, nr, l, r, val) do
      cond do
        r < nl or nr < l ->
          tree

        l <= nl and nr <= r ->
          apply_lazy(tree, node, val)

        true ->
          tree = push(tree, node)
          mid = div(nl + nr, 2)
          tree = do_update(tree, node * 2, nl, mid, l, r, val)
          tree = do_update(tree, node * 2 + 1, mid + 1, nr, l, r, val)

          left_max = :array.get(node * 2, tree.max)
          right_max = :array.get(node * 2 + 1, tree.max)
          max_val = if left_max > right_max, do: left_max, else: right_max

          %{tree | max: :array.set(node, max_val, tree.max)}
      end
    end

    defp apply_lazy(tree, node, val) do
      new_max = :array.get(node, tree.max) + val
      new_lazy = :array.get(node, tree.lazy) + val
      %{tree |
        max: :array.set(node, new_max, tree.max),
        lazy: :array.set(node, new_lazy, tree.lazy)}
    end

    defp push(tree, node) do
      lazy = :array.get(node, tree.lazy)

      if lazy != 0 do
        tree = apply_lazy(tree, node * 2, lazy)
        tree = apply_lazy(tree, node * 2 + 1, lazy)
        %{tree | lazy: :array.set(node, 0, tree.lazy)}
      else
        tree
      end
    end

    def max(%SegTree{max: max_arr}), do: :array.get(1, max_arr)
  end
end
```
