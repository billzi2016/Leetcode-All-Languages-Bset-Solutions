# 3410. Maximize Subarray Sum After Removing All Occurrences of One Element

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    struct Node {
        long long sum, pref, suff, best;
        Node(long long v = 0) : sum(v), pref(v), suff(v), best(v) {}
    };
    
    vector<Node> seg;
    int n;
    vector<int> arr;
    
    Node merge(const Node& L, const Node& R) {
        Node res;
        res.sum = L.sum + R.sum;
        res.pref = max(L.pref, L.sum + R.pref);
        res.suff = max(R.suff, R.sum + L.suff);
        res.best = max({L.best, R.best, L.suff + R.pref});
        return res;
    }
    
    void build(int idx, int l, int r) {
        if (l == r) {
            seg[idx] = Node(arr[l]);
            return;
        }
        int mid = (l + r) >> 1;
        build(idx<<1, l, mid);
        build(idx<<1|1, mid+1, r);
        seg[idx] = merge(seg[idx<<1], seg[idx<<1|1]);
    }
    
    void pointUpdate(int idx, int l, int r, int pos, long long val) {
        if (l == r) {
            seg[idx] = Node(val);
            return;
        }
        int mid = (l + r) >> 1;
        if (pos <= mid) pointUpdate(idx<<1, l, mid, pos, val);
        else pointUpdate(idx<<1|1, mid+1, r, pos, val);
        seg[idx] = merge(seg[idx<<1], seg[idx<<1|1]);
    }
    
    long long maxSubarraySum(vector<int>& nums) {
        arr = nums;
        n = (int)arr.size();
        seg.assign(4*n + 5, Node());
        build(1,0,n-1);
        
        // map value -> positions
        unordered_map<int, vector<int>> pos;
        pos.reserve(n*2);
        for (int i=0;i<n;++i) pos[nums[i]].push_back(i);
        
        // global max and second max
        long long max1 = LLONG_MIN, max2 = LLONG_MIN;
        int cntMax1 = 0;
        for (int v: nums) {
            if (v > max1) {
                max2 = max1;
                max1 = v;
                cntMax1 = 1;
            } else if (v == max1) {
                ++cntMax1;
            } else if (v > max2) {
                max2 = v;
            }
        }
        
        long long answer = seg[1].best; // no operation
        
        for (auto &kv : pos) {
            int val = kv.first;
            const vector<int>& idxs = kv.second;
            
            // set all occurrences to 0
            for (int id: idxs) pointUpdate(1,0,n-1,id,0);
            long long cand = seg[1].best;
            
            // compute max element not equal to val
            long long maxNonDel = LLONG_MIN;
            if (val != max1) {
                maxNonDel = max1;
            } else {
                if (cntMax1 > 1) maxNonDel = max1;
                else maxNonDel = max2; // may stay LLONG_MIN if no other element
            }
            
            if (cand == 0 && maxNonDel < 0 && maxNonDel != LLONG_MIN) cand = maxNonDel;
            answer = max(answer, cand);
            
            // revert updates
            for (int id: idxs) pointUpdate(1,0,n-1,id,nums[id]);
        }
        
        return answer;
    }
};
```

## Java

```java
class Solution {
    private int n;
    private long[] total, pref, suff, best;
    private int[] arr;

    public long maxSubarraySum(int[] nums) {
        this.n = nums.length;
        this.arr = nums.clone();
        int size = 4 * n + 5;
        total = new long[size];
        pref = new long[size];
        suff = new long[size];
        best = new long[size];
        build(1, 0, n - 1);

        long answer = best[1]; // no operation

        java.util.HashMap<Integer, java.util.ArrayList<Integer>> map = new java.util.HashMap<>();
        for (int i = 0; i < n; i++) {
            map.computeIfAbsent(nums[i], k -> new java.util.ArrayList<>()).add(i);
        }

        for (java.util.Map.Entry<Integer, java.util.ArrayList<Integer>> entry : map.entrySet()) {
            java.util.ArrayList<Integer> idxs = entry.getValue();
            // set these positions to 0
            for (int idx : idxs) {
                update(1, 0, n - 1, idx, 0L);
            }
            answer = Math.max(answer, best[1]);
            // revert back to original values
            for (int idx : idxs) {
                update(1, 0, n - 1, idx, arr[idx]);
            }
        }

        return answer;
    }

    private void build(int node, int l, int r) {
        if (l == r) {
            long val = arr[l];
            total[node] = val;
            pref[node] = val;
            suff[node] = val;
            best[node] = val;
            return;
        }
        int mid = (l + r) >>> 1;
        build(node << 1, l, mid);
        build(node << 1 | 1, mid + 1, r);
        pull(node);
    }

    private void update(int node, int l, int r, int pos, long val) {
        if (l == r) {
            total[node] = val;
            pref[node] = val;
            suff[node] = val;
            best[node] = val;
            return;
        }
        int mid = (l + r) >>> 1;
        if (pos <= mid) update(node << 1, l, mid, pos, val);
        else update(node << 1 | 1, mid + 1, r, pos, val);
        pull(node);
    }

    private void pull(int node) {
        int left = node << 1;
        int right = node << 1 | 1;

        total[node] = total[left] + total[right];
        pref[node] = Math.max(pref[left], total[left] + pref[right]);
        suff[node] = Math.max(suff[right], total[right] + suff[left]);
        best[node] = Math.max(Math.max(best[left], best[right]), suff[left] + pref[right]);
    }
}
```

## Python

```python
class Solution(object):
    def maxSubarraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        size = 4 * n
        seg_sum = [0] * size
        pref = [0] * size
        suf = [0] * size
        best = [0] * size

        def build(node, l, r):
            if l == r:
                val = nums[l]
                seg_sum[node] = val
                pref[node] = val
                suf[node] = val
                best[node] = val
                return
            mid = (l + r) // 2
            left = node * 2
            right = left + 1
            build(left, l, mid)
            build(right, mid + 1, r)
            pull(node)

        def pull(node):
            left = node * 2
            right = left + 1
            seg_sum[node] = seg_sum[left] + seg_sum[right]
            pref[node] = max(pref[left], seg_sum[left] + pref[right])
            suf[node] = max(suf[right], seg_sum[right] + suf[left])
            best[node] = max(best[left], best[right], suf[left] + pref[right])

        def update(node, l, r, idx, val):
            if l == r:
                seg_sum[node] = val
                pref[node] = val
                suf[node] = val
                best[node] = val
                return
            mid = (l + r) // 2
            left = node * 2
            right = left + 1
            if idx <= mid:
                update(left, l, mid, idx, val)
            else:
                update(right, mid + 1, r, idx, val)
            pull(node)

        build(1, 0, n - 1)
        answer = best[1]  # no removal case

        # map value to its indices
        pos = {}
        for i, v in enumerate(nums):
            pos.setdefault(v, []).append(i)

        for v, idxs in pos.items():
            # set all occurrences of v to 0
            for i in idxs:
                update(1, 0, n - 1, i, 0)
            answer = max(answer, best[1])
            # revert back to original values
            for i in idxs:
                update(1, 0, n - 1, i, nums[i])

        return answer
```

## Python3

```python
import sys
from typing import List

class Solution:
    def maxSubarraySum(self, nums: List[int]) -> int:
        n = len(nums)
        # Kadane for no operation
        cur = best = nums[0]
        for x in nums[1:]:
            cur = x if cur < 0 else cur + x
            if cur > best:
                best = cur

        # prefix sums
        pref = [0] * (n + 1)
        for i, v in enumerate(nums):
            pref[i + 1] = pref[i] + v

        # build log table
        import math
        LOG = [0] * (n + 2)
        for i in range(2, n + 2):
            LOG[i] = LOG[i // 2] + 1
        K = LOG[n + 1] + 1

        # sparse tables for min and max of prefix sums
        st_min = [[0] * (n + 1) for _ in range(K)]
        st_max = [[0] * (n + 1) for _ in range(K)]
        for i in range(n + 1):
            st_min[0][i] = pref[i]
            st_max[0][i] = pref[i]
        j = 1
        while (1 << j) <= n + 1:
            length = 1 << (j - 1)
            for i in range(n + 2 - (1 << j)):
                a = st_min[j - 1][i]
                b = st_min[j - 1][i + length]
                st_min[j][i] = a if a < b else b
                a = st_max[j - 1][i]
                b = st_max[j - 1][i + length]
                st_max[j][i] = a if a > b else b
            j += 1

        def query_min(l: int, r: int) -> int:
            """min of pref[l..r-1]"""
            k = LOG[r - l]
            a = st_min[k][l]
            b = st_min[k][r - (1 << k)]
            return a if a < b else b

        def query_max(l: int, r: int) -> int:
            """max of pref[l..r-1]"""
            k = LOG[r - l]
            a = st_max[k][l]
            b = st_max[k][r - (1 << k)]
            return a if a > b else b

        # map values to positions
        pos_map = {}
        for idx, val in enumerate(nums):
            pos_map.setdefault(val, []).append(idx)

        answer = best  # include case of no operation

        for v, positions in pos_map.items():
            cnt = 0
            start = 0
            min_S = None
            ans_v = -10**30

            for p in positions:
                if start < p:  # non‑empty segment before this occurrence
                    seg_min = query_min(start, p) - v * cnt
                    seg_max = query_max(start, p) - v * cnt

                    # internal interval within the segment
                    diff = seg_max - seg_min
                    if diff > ans_v:
                        ans_v = diff

                    # cross intervals using previous minima
                    if min_S is not None:
                        cross = seg_max - min_S
                        if cross > ans_v:
                            ans_v = cross

                    # update global minimum S seen so far
                    if min_S is None or seg_min < min_S:
                        min_S = seg_min

                # move past the occurrence
                start = p + 1
                cnt += 1

            # final segment after last occurrence
            if start <= n:
                seg_min = query_min(start, n) - v * cnt
                seg_max = query_max(start, n) - v * cnt

                diff = seg_max - seg_min
                if diff > ans_v:
                    ans_v = diff
                if min_S is not None:
                    cross = seg_max - min_S
                    if cross > ans_v:
                        ans_v = cross
                if min_S is None or seg_min < min_S:
                    min_S = seg_min

            if ans_v > answer:
                answer = ans_v

        return answer
```

## C

```c
#include <stddef.h>
#include <stdlib.h>

typedef long long ll;
const ll NEG_INF = -(1LL<<60);

typedef struct {
    ll sum;
    ll pref;
    ll suff;
    ll best;
    int has; // 0 or 1
} Node;

static inline Node make_node(ll val, int removed) {
    Node n;
    if (removed) {
        n.sum = 0;
        n.pref = n.suff = n.best = NEG_INF;
        n.has = 0;
    } else {
        n.sum = val;
        n.pref = n.suff = n.best = val;
        n.has = 1;
    }
    return n;
}

static inline Node combine(Node L, Node R) {
    Node res;
    res.sum = L.sum + R.sum;
    res.has = L.has || R.has;

    // prefix
    res.pref = L.pref;
    if (R.has) {
        ll cand = L.sum + R.pref;
        if (cand > res.pref) res.pref = cand;
    }

    // suffix
    res.suff = R.suff;
    if (L.has) {
        ll cand = L.suff + R.sum;
        if (cand > res.suff) res.suff = cand;
    }

    // best
    res.best = L.best > R.best ? L.best : R.best;
    if (L.has && R.has) {
        ll cand = L.suff + R.pref;
        if (cand > res.best) res.best = cand;
    }
    return res;
}

typedef struct {
    Node *tree;
    int n;
} SegTree;

static void seg_build(SegTree *st, ll *arr, int idx, int l, int r) {
    if (l == r) {
        st->tree[idx] = make_node(arr[l], 0);
        return;
    }
    int mid = (l + r) >> 1;
    seg_build(st, arr, idx<<1, l, mid);
    seg_build(st, arr, idx<<1|1, mid+1, r);
    st->tree[idx] = combine(st->tree[idx<<1], st->tree[idx<<1|1]);
}

static void seg_update(SegTree *st, int idx, int l, int r, int pos, ll val, int removed) {
    if (l == r) {
        st->tree[idx] = make_node(val, removed);
        return;
    }
    int mid = (l + r) >> 1;
    if (pos <= mid)
        seg_update(st, idx<<1, l, mid, pos, val, removed);
    else
        seg_update(st, idx<<1|1, mid+1, r, pos, val, removed);
    st->tree[idx] = combine(st->tree[idx<<1], st->tree[idx<<1|1]);
}

static Node seg_root(SegTree *st) {
    return st->tree[1];
}

/* Simple hash map for value -> dynamic array of positions */
typedef struct PosNode {
    int pos;
    struct PosNode *next;
} PosNode;

typedef struct {
    int key;
    PosNode *head;
    struct MapEntry *next;
} MapEntry;

typedef struct MapEntry {
    int key;
    PosNode *head;
    struct MapEntry *next;
} MapEntry;

#define MAP_SIZE 131071

static unsigned int hash_int(int x) {
    return ((unsigned int)x * 2654435761u);
}

static void map_insert(MapEntry **table, int key, int pos) {
    unsigned int h = hash_int(key) % MAP_SIZE;
    MapEntry *e = table[h];
    while (e) {
        if (e->key == key) break;
        e = e->next;
    }
    if (!e) {
        e = (MapEntry *)malloc(sizeof(MapEntry));
        e->key = key;
        e->head = NULL;
        e->next = table[h];
        table[h] = e;
    }
    PosNode *pn = (PosNode *)malloc(sizeof(PosNode));
    pn->pos = pos;
    pn->next = e->head;
    e->head = pn;
}

/* Retrieve entry */
static MapEntry* map_get(MapEntry **table, int key) {
    unsigned int h = hash_int(key) % MAP_SIZE;
    MapEntry *e = table[h];
    while (e) {
        if (e->key == key) return e;
        e = e->next;
    }
    return NULL;
}

/* Free map */
static void map_free(MapEntry **table) {
    for (int i=0;i<MAP_SIZE;++i){
        MapEntry *e = table[i];
        while(e){
            PosNode *pn=e->head;
            while(pn){PosNode*tmp=pn;pn=pn->next;free(tmp);}
            MapEntry*tmp=e;e=e->next;free(tmp);
        }
    }
}

long long maxSubarraySum(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    ll *arr = (ll*)malloc(sizeof(ll)*numsSize);
    for (int i=0;i<numsSize;++i) arr[i]=nums[i];

    SegTree st;
    st.n = numsSize;
    st.tree = (Node*)malloc(sizeof(Node)*(4*numsSize+5));
    seg_build(&st, arr, 1, 0, numsSize-1);
    ll answer = seg_root(&st).best;

    /* Build map of value -> positions */
    MapEntry **table = (MapEntry**)calloc(MAP_SIZE, sizeof(MapEntry*));
    for (int i=0;i<numsSize;++i) {
        map_insert(table, nums[i], i);
    }

    for (int bucket=0; bucket<MAP_SIZE; ++bucket) {
        MapEntry *e = table[bucket];
        while (e) {
            // apply removal
            PosNode *pn = e->head;
            while (pn) {
                seg_update(&st, 1, 0, numsSize-1, pn->pos, arr[pn->pos], 1);
                pn = pn->next;
            }
            Node root = seg_root(&st);
            if (root.has && root.best > answer) answer = root.best;

            // revert
            pn = e->head;
            while (pn) {
                seg_update(&st, 1, 0, numsSize-1, pn->pos, arr[pn->pos], 0);
                pn = pn->next;
            }
            e = e->next;
        }
    }

    free(arr);
    free(st.tree);
    map_free(table);
    free(table);
    return answer;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private struct Node {
        public long sum, pref, suff, ans;
    }

    private Node[] seg;
    private int n;

    private Node Combine(Node left, Node right) {
        Node res = new Node();
        res.sum = left.sum + right.sum;
        res.pref = Math.Max(left.pref, left.sum + right.pref);
        res.suff = Math.Max(right.suff, right.sum + left.suff);
        res.ans = Math.Max(Math.Max(left.ans, right.ans), left.suff + right.pref);
        return res;
    }

    private void Build(int idx, int l, int r, long[] arr) {
        if (l == r) {
            long val = arr[l];
            seg[idx].sum = val;
            seg[idx].pref = Math.Max(0L, val);
            seg[idx].suff = Math.Max(0L, val);
            seg[idx].ans  = Math.Max(0L, val);
            return;
        }
        int mid = (l + r) >> 1;
        Build(idx << 1, l, mid, arr);
        Build(idx << 1 | 1, mid + 1, r, arr);
        seg[idx] = Combine(seg[idx << 1], seg[idx << 1 | 1]);
    }

    private void Update(int idx, int l, int r, int pos, long val) {
        if (l == r) {
            seg[idx].sum = val;
            seg[idx].pref = Math.Max(0L, val);
            seg[idx].suff = Math.Max(0L, val);
            seg[idx].ans  = Math.Max(0L, val);
            return;
        }
        int mid = (l + r) >> 1;
        if (pos <= mid) Update(idx << 1, l, mid, pos, val);
        else Update(idx << 1 | 1, mid + 1, r, pos, val);
        seg[idx] = Combine(seg[idx << 1], seg[idx << 1 | 1]);
    }

    public long MaxSubarraySum(int[] nums) {
        n = nums.Length;
        long[] arr = new long[n];
        for (int i = 0; i < n; i++) arr[i] = nums[i];

        seg = new Node[4 * n];
        Build(1, 0, n - 1, arr);

        long best = seg[1].ans;

        // map value -> list of indices
        var dict = new Dictionary<int, List<int>>();
        for (int i = 0; i < n; i++) {
            if (!dict.TryGetValue(nums[i], out var list)) {
                list = new List<int>();
                dict[nums[i]] = list;
            }
            list.Add(i);
        }

        foreach (var kvp in dict) {
            int val = kvp.Key;
            var indices = kvp.Value;

            // set all occurrences to 0
            foreach (int idx in indices) {
                Update(1, 0, n - 1, idx, 0L);
            }
            best = Math.Max(best, seg[1].ans);

            // restore original values
            foreach (int idx in indices) {
                Update(1, 0, n - 1, idx, arr[idx]);
            }
        }

        return best;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubarraySum = function(nums) {
    const n = nums.length;
    // Build segment tree
    let size = 1;
    while (size < n) size <<= 1;
    const sum = new Array(2 * size).fill(0);
    const pref = new Array(2 * size).fill(-Infinity);
    const suff = new Array(2 * size).fill(-Infinity);
    const best = new Array(2 * size).fill(-Infinity);

    for (let i = 0; i < size; ++i) {
        if (i < n) {
            const v = nums[i];
            sum[size + i] = v;
            pref[size + i] = v;
            suff[size + i] = v;
            best[size + i] = v;
        } else {
            // dummy leaf
            sum[size + i] = 0;
            pref[size + i] = -Infinity;
            suff[size + i] = -Infinity;
            best[size + i] = -Infinity;
        }
    }

    const merge = (a, b) => {
        return {
            sum: a.sum + b.sum,
            pref: Math.max(a.pref, a.sum + b.pref),
            suff: Math.max(b.suff, b.sum + a.suff),
            best: Math.max(Math.max(a.best, b.best), a.suff + b.pref)
        };
    };

    for (let i = size - 1; i >= 1; --i) {
        const l = i << 1;
        const r = l | 1;
        sum[i] = sum[l] + sum[r];
        pref[i] = Math.max(pref[l], sum[l] + pref[r]);
        suff[i] = Math.max(suff[r], sum[r] + suff[l]);
        best[i] = Math.max(Math.max(best[l], best[r]), suff[l] + pref[r]);
    }

    const query = (l, r) => {
        l += size;
        r += size;
        let leftRes = null;
        let rightRes = null;
        while (l <= r) {
            if ((l & 1) === 1) {
                const node = { sum: sum[l], pref: pref[l], suff: suff[l], best: best[l] };
                leftRes = leftRes ? merge(leftRes, node) : node;
                ++l;
            }
            if ((r & 1) === 0) {
                const node = { sum: sum[r], pref: pref[r], suff: suff[r], best: best[r] };
                rightRes = rightRes ? merge(node, rightRes) : node;
                --r;
            }
            l >>= 1;
            r >>= 1;
        }
        if (!leftRes) return rightRes;
        if (!rightRes) return leftRes;
        return merge(leftRes, rightRes);
    };

    // overall best without any removal
    let answer = query(0, n - 1).best;

    // map value -> list of positions
    const posMap = new Map();
    for (let i = 0; i < n; ++i) {
        const v = nums[i];
        if (!posMap.has(v)) posMap.set(v, []);
        posMap.get(v).push(i);
    }

    // evaluate each distinct value as the one to remove
    for (const [val, positions] of posMap.entries()) {
        let maxForVal = -Infinity;
        let start = 0;
        for (let idx = 0; idx < positions.length; ++idx) {
            const p = positions[idx];
            if (start <= p - 1) {
                const curBest = query(start, p - 1).best;
                if (curBest > maxForVal) maxForVal = curBest;
            }
            start = p + 1;
        }
        if (start <= n - 1) {
            const curBest = query(start, n - 1).best;
            if (curBest > maxForVal) maxForVal = curBest;
        }
        // If all elements are removed, maxForVal stays -Infinity; ignore.
        if (maxForVal > answer) answer = maxForVal;
    }

    return answer;
};
```

## Typescript

```typescript
function maxSubarraySum(nums: number[]): number {
    const n = nums.length;
    const NEG_INF = -1e18;

    interface Node {
        sum: number;
        pref: number;
        suff: number;
        ans: number;
    }

    const tree: Node[] = new Array(4 * n);

    function makeNode(val: number): Node {
        return { sum: val, pref: val, suff: val, ans: val };
    }

    function combine(a: Node, b: Node): Node {
        const sum = a.sum + b.sum;
        const pref = Math.max(a.pref, a.sum + b.pref);
        const suff = Math.max(b.suff, b.sum + a.suff);
        const ans = Math.max(Math.max(a.ans, b.ans), a.suff + b.pref);
        return { sum, pref, suff, ans };
    }

    function build(idx: number, l: number, r: number): void {
        if (l === r) {
            tree[idx] = makeNode(nums[l]);
            return;
        }
        const mid = (l + r) >> 1;
        build(idx << 1, l, mid);
        build((idx << 1) | 1, mid + 1, r);
        tree[idx] = combine(tree[idx << 1], tree[(idx << 1) | 1]);
    }

    function update(idx: number, l: number, r: number, pos: number, val: number): void {
        if (l === r) {
            tree[idx] = makeNode(val);
            return;
        }
        const mid = (l + r) >> 1;
        if (pos <= mid) update(idx << 1, l, mid, pos, val);
        else update((idx << 1) | 1, mid + 1, r, pos, val);
        tree[idx] = combine(tree[idx << 1], tree[(idx << 1) | 1]);
    }

    build(1, 0, n - 1);

    // map value -> list of indices
    const posMap = new Map<number, number[]>();
    for (let i = 0; i < n; ++i) {
        const v = nums[i];
        if (!posMap.has(v)) posMap.set(v, []);
        posMap.get(v)!.push(i);
    }

    let answer = tree[1].ans; // no removal

    for (const [val, idxList] of posMap.entries()) {
        // remove all occurrences of val
        for (const idx of idxList) update(1, 0, n - 1, idx, NEG_INF);
        const curAns = tree[1].ans;
        if (curAns > answer) answer = curAns;
        // restore original values
        for (const idx of idxList) update(1, 0, n - 1, idx, nums[idx]);
    }

    return answer;
}
```

## Php

```php
class Solution {
    private $sum = [];
    private $pref = [];
    private $suff = [];
    private $best = [];
    private $nums = [];

    public function maxSubarraySum($nums) {
        $this->nums = $nums;
        $n = count($nums);
        $size = 4 * $n + 5;
        $this->sum = array_fill(0, $size, 0);
        $this->pref = array_fill(0, $size, 0);
        $this->suff = array_fill(0, $size, 0);
        $this->best = array_fill(0, $size, 0);

        $this->build(1, 0, $n - 1);
        $answer = $this->best[1]; // original max subarray sum

        // group positions by value
        $posMap = [];
        foreach ($nums as $i => $v) {
            if (!isset($posMap[$v])) {
                $posMap[$v] = [];
            }
            $posMap[$v][] = $i;
        }

        foreach ($posMap as $value => $indices) {
            // set all occurrences to 0
            foreach ($indices as $idx) {
                $this->update(1, 0, $n - 1, $idx, 0);
            }
            $answer = max($answer, $this->best[1]);
            // revert back to original values
            foreach ($indices as $idx) {
                $this->update(1, 0, $n - 1, $idx, $nums[$idx]);
            }
        }

        return $answer;
    }

    private function build($node, $l, $r) {
        if ($l == $r) {
            $val = $this->nums[$l];
            $this->sum[$node] = $val;
            $this->pref[$node] = $val;
            $this->suff[$node] = $val;
            $this->best[$node] = $val;
            return;
        }
        $mid = intdiv($l + $r, 2);
        $left = $node * 2;
        $right = $node * 2 + 1;
        $this->build($left, $l, $mid);
        $this->build($right, $mid + 1, $r);
        $this->pull($node, $left, $right);
    }

    private function update($node, $l, $r, $pos, $val) {
        if ($l == $r) {
            $this->sum[$node] = $val;
            $this->pref[$node] = $val;
            $this->suff[$node] = $val;
            $this->best[$node] = $val;
            return;
        }
        $mid = intdiv($l + $r, 2);
        $left = $node * 2;
        $right = $node * 2 + 1;
        if ($pos <= $mid) {
            $this->update($left, $l, $mid, $pos, $val);
        } else {
            $this->update($right, $mid + 1, $r, $pos, $val);
        }
        $this->pull($node, $left, $right);
    }

    private function pull($node, $left, $right) {
        $this->sum[$node] = $this->sum[$left] + $this->sum[$right];
        $this->pref[$node] = max($this->pref[$left], $this->sum[$left] + $this->pref[$right]);
        $this->suff[$node] = max($this->suff[$right], $this->sum[$right] + $this->suff[$left]);
        $this->best[$node] = max(
            max($this->best[$left], $this->best[$right]),
            $this->suff[$left] + $this->pref[$right]
        );
    }
}
```

## Swift

```swift
class Solution {
    func maxSubarraySum(_ nums: [Int]) -> Int {
        let n = nums.count
        var arr = nums.map { Int64($0) }
        if n == 0 { return 0 }
        let size = 4 * n
        var total = Array(repeating: Int64(0), count: size)
        var pref = Array(repeating: Int64(0), count: size)
        var suff = Array(repeating: Int64(0), count: size)
        var best = Array(repeating: Int64(0), count: size)

        func pull(_ idx: Int) {
            let l = idx << 1
            let r = l | 1
            total[idx] = total[l] + total[r]
            pref[idx] = max(pref[l], total[l] + pref[r])
            suff[idx] = max(suff[r], total[r] + suff[l])
            best[idx] = max(max(best[l], best[r]), suff[l] + pref[r])
        }

        func build(_ idx: Int, _ l: Int, _ r: Int) {
            if l == r {
                let v = arr[l]
                total[idx] = v
                pref[idx] = v
                suff[idx] = v
                best[idx] = v
                return
            }
            let mid = (l + r) >> 1
            build(idx << 1, l, mid)
            build((idx << 1) | 1, mid + 1, r)
            pull(idx)
        }

        func update(_ idx: Int, _ l: Int, _ r: Int, _ pos: Int, _ value: Int64) {
            if l == r {
                total[idx] = value
                pref[idx] = value
                suff[idx] = value
                best[idx] = value
                return
            }
            let mid = (l + r) >> 1
            if pos <= mid {
                update(idx << 1, l, mid, pos, value)
            } else {
                update((idx << 1) | 1, mid + 1, r, pos, value)
            }
            pull(idx)
        }

        build(1, 0, n - 1)

        var positionsByValue = [Int: [Int]]()
        for (i, v) in nums.enumerated() {
            positionsByValue[v, default: []].append(i)
        }

        let NEG_INF: Int64 = -1_000_000_000_000   // sufficiently small
        var answer = best[1]   // no operation

        for (_, indices) in positionsByValue {
            for i in indices {
                update(1, 0, n - 1, i, NEG_INF)
            }
            let cur = best[1]
            if cur > answer { answer = cur }
            for i in indices {
                update(1, 0, n - 1, i, arr[i])
            }
        }

        return Int(answer)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxSubarraySum(nums: IntArray): Long {
        val n = nums.size
        if (n == 0) return 0L
        val arr = LongArray(n) { nums[it].toLong() }

        // map each distinct value to its indices
        val posMap = HashMap<Int, MutableList<Int>>()
        for (i in 0 until n) {
            posMap.computeIfAbsent(nums[i]) { mutableListOf() }.add(i)
        }

        // persistent segment tree node
        class Node(
            val sum: Long,
            val pref: Long,
            val suff: Long,
            val ans: Long,
            val left: Node?,
            val right: Node?
        )

        fun merge(l: Node, r: Node): Node {
            val sum = l.sum + r.sum
            val pref = kotlin.math.max(l.pref, l.sum + r.pref)
            val suff = kotlin.math.max(r.suff, r.sum + l.suff)
            val ans = kotlin.math.max(kotlin.math.max(l.ans, r.ans), l.suff + r.pref)
            return Node(sum, pref, suff, ans, l, r)
        }

        fun build(l: Int, r: Int): Node {
            if (l == r) {
                val v = arr[l]
                return Node(v, v, v, v, null, null)
            }
            val m = (l + r) ushr 1
            val leftNode = build(l, m)
            val rightNode = build(m + 1, r)
            return merge(leftNode, rightNode)
        }

        fun update(node: Node, l: Int, r: Int, idx: Int, value: Long): Node {
            if (l == r) {
                return Node(value, value, value, value, null, null)
            }
            val m = (l + r) ushr 1
            return if (idx <= m) {
                val newLeft = update(node.left!!, l, m, idx, value)
                merge(newLeft, node.right!!)
            } else {
                val newRight = update(node.right!!, m + 1, r, idx, value)
                merge(node.left!!, newRight)
            }
        }

        val originalRoot = build(0, n - 1)
        var answer = originalRoot.ans

        for (indices in posMap.values) {
            var root = originalRoot
            for (idx in indices) {
                root = update(root, 0, n - 1, idx, 0L)
            }
            if (root.ans > answer) answer = root.ans
        }

        return answer
    }
}
```

## Dart

```dart
class Solution {
  static const int _negInf = -0x4000000000000000; // -(2^62)

  int maxSubarraySum(List<int> nums) {
    if (nums.isEmpty) return 0;
    final seg = _SegmentTree(nums);
    int answer = seg.tree[1].best;

    final Map<int, List<int>> posMap = {};
    for (int i = 0; i < nums.length; ++i) {
      posMap.putIfAbsent(nums[i], () => []).add(i);
    }

    for (final entry in posMap.entries) {
      final indices = entry.value;
      // remove all occurrences of this value
      for (final idx in indices) {
        seg.update(idx, _negInf);
      }
      int cand = seg.tree[1].best;
      if (cand > answer) answer = cand;
      // restore original values
      for (final idx in indices) {
        seg.update(idx, nums[idx]);
      }
    }

    return answer;
  }
}

class _Node {
  int sum;
  int pref;
  int suff;
  int best;
  _Node(this.sum, this.pref, this.suff, this.best);
}

class _SegmentTree {
  final List<_Node> tree;
  final List<int> data;

  _SegmentTree(this.data) : tree = List.filled(data.length * 4, _Node(0, 0, 0, 0)) {
    _build(1, 0, data.length - 1);
  }

  void _build(int node, int l, int r) {
    if (l == r) {
      final val = data[l];
      tree[node] = _Node(val, val, val, val);
      return;
    }
    final mid = (l + r) >> 1;
    _build(node << 1, l, mid);
    _build((node << 1) | 1, mid + 1, r);
    tree[node] = _combine(tree[node << 1], tree[(node << 1) | 1]);
  }

  void update(int idx, int value) {
    _update(1, 0, data.length - 1, idx, value);
  }

  void _update(int node, int l, int r, int idx, int value) {
    if (l == r) {
      tree[node] = _Node(value, value, value, value);
      return;
    }
    final mid = (l + r) >> 1;
    if (idx <= mid) {
      _update(node << 1, l, mid, idx, value);
    } else {
      _update((node << 1) | 1, mid + 1, r, idx, value);
    }
    tree[node] = _combine(tree[node << 1], tree[(node << 1) | 1]);
  }

  _Node _combine(_Node left, _Node right) {
    final sum = left.sum + right.sum;
    final pref = left.pref > left.sum + right.pref ? left.pref : left.sum + right.pref;
    final suff = right.suff > right.sum + left.suff ? right.suff : right.sum + left.suff;
    int best = left.best;
    if (right.best > best) best = right.best;
    final cross = left.suff + right.pref;
    if (cross > best) best = cross;
    return _Node(sum, pref, suff, best);
  }
}
```

## Golang

```go
package main

import (
	"math"
)

type node struct {
	sum   int64
	pref  int64
	suff  int64
	best  int64
}

const negInf int64 = math.MinInt64 / 4

func merge(a, b node) node {
	if a.best == negInf {
		return b
	}
	if b.best == negInf {
		return a
	}
	res := node{}
	res.sum = a.sum + b.sum
	res.pref = max(a.pref, a.sum+b.pref)
	res.suff = max(b.suff, b.sum+a.suff)
	res.best = max(max(a.best, b.best), a.suff+b.pref)
	return res
}

func build(arr []int64, seg []node, idx, l, r int) {
	if l == r {
		val := arr[l]
		seg[idx] = node{sum: val, pref: val, suff: val, best: val}
		return
	}
	mid := (l + r) / 2
	build(arr, seg, idx*2, l, mid)
	build(arr, seg, idx*2+1, mid+1, r)
	seg[idx] = merge(seg[idx*2], seg[idx*2+1])
}

func query(seg []node, idx, l, r, ql, qr int) node {
	if ql > r || qr < l {
		return node{sum: 0, pref: negInf, suff: negInf, best: negInf}
	}
	if ql <= l && r <= qr {
		return seg[idx]
	}
	mid := (l + r) / 2
	left := query(seg, idx*2, l, mid, ql, qr)
	right := query(seg, idx*2+1, mid+1, r, ql, qr)
	return merge(left, right)
}

func maxSubarraySum(nums []int) int64 {
	n := len(nums)
	if n == 0 {
		return 0
	}
	arr := make([]int64, n)
	for i, v := range nums {
		arr[i] = int64(v)
	}
	size := 4 * n
	seg := make([]node, size)
	build(arr, seg, 1, 0, n-1)

	ans := seg[1].best // no removal case

	posMap := make(map[int][]int)
	for i, v := range nums {
		posMap[v] = append(posMap[v], i)
	}

	for _, positions := range posMap {
		// add sentinels
		tmp := make([]int, 0, len(positions)+2)
		tmp = append(tmp, -1)
		tmp = append(tmp, positions...)
		tmp = append(tmp, n)
		for i := 0; i+1 < len(tmp); i++ {
			l := tmp[i] + 1
			r := tmp[i+1] - 1
			if l <= r {
				res := query(seg, 1, 0, n-1, l, r)
				if res.best > ans {
					ans = res.best
				}
			}
		}
	}

	return ans
}
```

## Ruby

```ruby
def max_subarray_sum(nums)
  class SegmentTree
    def initialize(arr)
      @n = arr.size
      size = 4 * @n
      @sum = Array.new(size, 0)
      @pref = Array.new(size, 0)
      @suff = Array.new(size, 0)
      @ans = Array.new(size, 0)
      build(1, 0, @n - 1, arr)
    end

    def max_subarray
      @ans[1]
    end

    def update(pos, val)
      _update(1, 0, @n - 1, pos, val)
    end

    private

    def build(node, l, r, arr)
      if l == r
        v = arr[l]
        @sum[node] = v
        @pref[node] = v
        @suff[node] = v
        @ans[node] = v
      else
        mid = (l + r) / 2
        build(node * 2, l, mid, arr)
        build(node * 2 + 1, mid + 1, r, arr)
        pull(node)
      end
    end

    def pull(node)
      left = node * 2
      right = left + 1
      @sum[node] = @sum[left] + @sum[right]
      @pref[node] = [@pref[left], @sum[left] + @pref[right]].max
      @suff[node] = [@suff[right], @sum[right] + @suff[left]].max
      @ans[node] = [@ans[left], @ans[right], @suff[left] + @pref[right]].max
    end

    def _update(node, l, r, pos, val)
      if l == r
        @sum[node] = val
        @pref[node] = val
        @suff[node] = val
        @ans[node] = val
      else
        mid = (l + r) / 2
        if pos <= mid
          _update(node * 2, l, mid, pos, val)
        else
          _update(node * 2 + 1, mid + 1, r, pos, val)
        end
        pull(node)
      end
    end
  end

  seg = SegmentTree.new(nums)
  best = seg.max_subarray

  groups = Hash.new { |h, k| h[k] = [] }
  nums.each_with_index { |v, i| groups[v] << i }

  groups.each do |val, idxs|
    idxs.each { |i| seg.update(i, 0) }
    cur = seg.max_subarray
    best = cur if cur > best
    idxs.each { |i| seg.update(i, nums[i]) }
  end

  best
end
```

## Scala

```scala
object Solution {
    def maxSubarraySum(nums: Array[Int]): Long = {
        val n = nums.length
        case class Node(sum: Long, pref: Long, suff: Long, best: Long)
        val tree = new Array[Node](4 * n)

        def combine(a: Node, b: Node): Node = {
            val sum = a.sum + b.sum
            val pref = math.max(a.pref, a.sum + b.pref)
            val suff = math.max(b.suff, b.sum + a.suff)
            val best = List(a.best, b.best, a.suff + b.pref).max
            Node(sum, pref, suff, best)
        }

        def build(node: Int, l: Int, r: Int): Unit = {
            if (l == r) {
                val v = nums(l).toLong
                tree(node) = Node(v, v, v, v)
            } else {
                val mid = (l + r) >> 1
                build(node << 1, l, mid)
                build(node << 1 | 1, mid + 1, r)
                tree(node) = combine(tree(node << 1), tree(node << 1 | 1))
            }
        }

        def update(node: Int, l: Int, r: Int, idx: Int, value: Long): Unit = {
            if (l == r) {
                tree(node) = Node(value, value, value, value)
            } else {
                val mid = (l + r) >> 1
                if (idx <= mid) update(node << 1, l, mid, idx, value)
                else update(node << 1 | 1, mid + 1, r, idx, value)
                tree(node) = combine(tree(node << 1), tree(node << 1 | 1))
            }
        }

        build(1, 0, n - 1)

        // map values to their positions
        val posMap = scala.collection.mutable.Map[Int, scala.collection.mutable.ArrayBuffer[Int]]()
        for (i <- nums.indices) {
            val v = nums(i)
            posMap.getOrElseUpdate(v, scala.collection.mutable.ArrayBuffer[Int]()) += i
        }

        // global max and second max values
        var max1 = Int.MinValue
        var cntMax1 = 0
        var max2 = Int.MinValue
        for (v <- nums) {
            if (v > max1) {
                max2 = max1
                max1 = v
                cntMax1 = 1
            } else if (v == max1) {
                cntMax1 += 1
            } else if (v > max2) {
                max2 = v
            }
        }

        var answer = tree(1).best

        for ((value, positions) <- posMap) {
            // set all occurrences to 0
            for (idx <- positions) update(1, 0, n - 1, idx, 0L)

            val candidate = tree(1).best

            // compute max kept element after removal of 'value'
            val maxKept: Long =
                if (value != max1) max1.toLong
                else {
                    if (max2 == Int.MinValue) Long.MinValue else max2.toLong
                }

            var effective = candidate
            if (effective == 0L && maxKept < 0L) effective = maxKept

            answer = math.max(answer, effective)

            // revert updates
            for (idx <- positions) update(1, 0, n - 1, idx, nums(idx).toLong)
        }

        answer
    }
}
```

## Rust

```rust
use std::collections::HashMap;

#[derive(Clone, Copy, Debug)]
struct Node {
    sum: i64,
    pref: i64,
    suff: i64,
    best: i64,
}

impl Node {
    fn from(val: i64) -> Self {
        Node { sum: val, pref: val, suff: val, best: val }
    }

    fn combine(left: &Node, right: &Node) -> Node {
        let sum = left.sum + right.sum;
        let pref = left.pref.max(left.sum + right.pref);
        let suff = right.suff.max(right.sum + left.suff);
        let best = left.best.max(right.best).max(left.suff + right.pref);
        Node { sum, pref, suff, best }
    }

    fn empty() -> Self {
        // neutral element (won't be used for real segments)
        Node {
            sum: 0,
            pref: i64::MIN / 4,
            suff: i64::MIN / 4,
            best: i64::MIN / 4,
        }
    }
}

struct SegTree {
    size: usize,
    data: Vec<Node>,
}

impl SegTree {
    fn new(arr: &[i32]) -> Self {
        let n = arr.len();
        let size = n.next_power_of_two();
        let mut data = vec![Node::empty(); 2 * size];
        for i in 0..n {
            data[size + i] = Node::from(arr[i] as i64);
        }
        for i in (1..size).rev() {
            data[i] = Node::combine(&data[2 * i], &data[2 * i + 1]);
        }
        SegTree { size, data }
    }

    fn update(&mut self, pos: usize, val: i64) {
        let mut idx = self.size + pos;
        self.data[idx] = Node::from(val);
        while idx > 1 {
            idx >>= 1;
            self.data[idx] = Node::combine(&self.data[2 * idx], &self.data[2 * idx + 1]);
        }
    }

    fn root(&self) -> &Node {
        &self.data[1]
    }
}

impl Solution {
    pub fn max_subarray_sum(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        // Build segment tree with original values
        let mut seg = SegTree::new(&nums);
        let mut answer = seg.root().best;

        // Group indices by value
        let mut groups: HashMap<i32, Vec<usize>> = HashMap::new();
        for (i, &v) in nums.iter().enumerate() {
            groups.entry(v).or_default().push(i);
        }

        // For each distinct value, set its positions to 0, query, then revert
        for (_val, idxs) in groups.iter() {
            // remove all occurrences (set to zero)
            for &idx in idxs {
                seg.update(idx, 0);
            }
            answer = answer.max(seg.root().best);
            // revert back to original values
            for &idx in idxs {
                seg.update(idx, nums[idx] as i64);
            }
        }

        answer
    }
}
```

## Racket

```racket
(define/contract (max-subarray-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((arr (list->vector nums))
         (n (vector-length arr))
         (size (* 4 n))
         (sumV (make-vector size 0))
         (prefV (make-vector size 0))
         (suffV (make-vector size 0))
         (bestV (make-vector size 0)))
    (define (combine node)
      (let* ((l (* node 2))
             (r (+ l 1))
             (lsum (vector-ref sumV l))
             (rsum (vector-ref sumV r))
             (lpref (vector-ref prefV l))
             (rpref (vector-ref prefV r))
             (lsuff (vector-ref suffV l))
             (rsuff (vector-ref suffV r))
             (lbest (vector-ref bestV l))
             (rbest (vector-ref bestV r)))
        (vector-set! sumV node (+ lsum rsum))
        (vector-set! prefV node (max lpref (+ lsum rpref)))
        (vector-set! suffV node (max rsuff (+ rsum lsuff)))
        (vector-set! bestV node (max (max lbest rbest) (+ lsuff rpref)))))
    (define (build node l r)
      (if (= l r)
          (let ((val (vector-ref arr l)))
            (vector-set! sumV node val)
            (vector-set! prefV node val)
            (vector-set! suffV node val)
            (vector-set! bestV node val))
          (let ((mid (quotient (+ l r) 2)))
            (build (* node 2) l mid)
            (build (+ (* node 2) 1) (+ mid 1) r)
            (combine node))))
    (define (update node l r idx newval)
      (if (= l r)
          (begin
            (vector-set! sumV node newval)
            (vector-set! prefV node newval)
            (vector-set! suffV node newval)
            (vector-set! bestV node newval))
          (let ((mid (quotient (+ l r) 2)))
            (if (<= idx mid)
                (update (* node 2) l mid idx newval)
                (update (+ (* node 2) 1) (+ mid 1) r idx newval))
            (combine node))))
    (build 1 0 (- n 1))
    (define ans (vector-ref bestV 1))
    ;; map each distinct value to list of its indices
    (let ((hash (make-hash)))
      (for ([i (in-range n)])
        (let* ((v (vector-ref arr i))
               (lst (hash-ref hash v '())))
          (hash-set! hash v (cons i lst))))
      (for ([val (in-hash-keys hash)])
        (define idxs (hash-ref hash val))
        ;; remove all occurrences of val (set to 0)
        (for ([i (in-list idxs)])
          (update 1 0 (- n 1) i 0))
        (let ((cur (vector-ref bestV 1)))
          (set! ans (max ans cur)))
        ;; restore original values
        (for ([i (in-list idxs)])
          (update 1 0 (- n 1) i (vector-ref arr i)))))
    ans))
```

## Erlang

```erlang
-spec max_subarray_sum(Nums :: [integer()]) -> integer().
max_subarray_sum(Nums) ->
    N = length(Nums),
    OriginalTree = build_tree(Nums, 1, N),
    BaseAns = maps:get(ans, OriginalTree),
    IndexMap = build_index_map(Nums, 1, #{}),
    MaxAfterRemoval = maps:fold(
        fun(_Val, IdxList, CurMax) ->
            ModifiedTree = lists:foldl(
                fun(Id, TreeAcc) -> update(TreeAcc, 1, N, Id, 0) end,
                OriginalTree,
                IdxList
            ),
            NewAns = maps:get(ans, ModifiedTree),
            if NewAns > CurMax -> NewAns; true -> CurMax end
        end,
        BaseAns,
        IndexMap
    ),
    max(MaxAfterRemoval, 0).

%% Build segment tree from array NumList (1‑based indices)
build_tree(NumList, L, R) when L =:= R ->
    Val = lists:nth(L, NumList),
    #{sum => Val, pref => Val, suff => Val, ans => Val};
build_tree(NumList, L, R) ->
    Mid = (L + R) div 2,
    Left = build_tree(NumList, L, Mid),
    Right = build_tree(NumList, Mid + 1, R),
    combine(Left, Right).

%% Update position Pos to NewVal, returning new tree
update(Node, L, R, Pos, NewVal) when L =:= R ->
    #{sum => NewVal, pref => NewVal, suff => NewVal, ans => NewVal};
update(Node, L, R, Pos, NewVal) ->
    Mid = (L + R) div 2,
    LeftChild = maps:get(left, Node),
    RightChild = maps:get(right, Node),
    if
        Pos =< Mid ->
            NewLeft = update(LeftChild, L, Mid, Pos, NewVal),
            combine(NewLeft, RightChild);
        true ->
            NewRight = update(RightChild, Mid + 1, R, Pos, NewVal),
            combine(LeftChild, NewRight)
    end.

%% Combine two child nodes into parent node
combine(Left, Right) ->
    LSum = maps:get(sum, Left),
    RSum = maps:get(sum, Right),
    Sum = LSum + RSum,
    LPref = maps:get(pref, Left),
    RPRef = maps:get(pref, Right),
    Pref = max(LPref, LSum + RPRef),
    LSuff = maps:get(suff, Left),
    RSuff = maps:get(suff, Right),
    Suff = max(RSuff, RSum + LSuff),
    LAns = maps:get(ans, Left),
    RAns = maps:get(ans, Right),
    Cross = LSuff + RPRef,
    Ans = max(max(LAns, RAns), Cross),
    #{sum => Sum, pref => Pref, suff => Suff, ans => Ans, left => Left, right => Right}.

%% Build map from value to list of its indices (1‑based)
build_index_map([], _Idx, Acc) -> Acc;
build_index_map([H|T], Idx, Acc) ->
    Prev = maps:get(H, Acc, []),
    NewAcc = maps:put(H, [Idx | Prev], Acc),
    build_index_map(T, Idx + 1, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  defstruct l: 0, r: 0, sum: 0, pref: 0, suff: 0, best: 0, left: nil, right: nil

  @spec max_subarray_sum(nums :: [integer]) :: integer
  def max_subarray_sum(nums) do
    n = length(nums)
    orig = List.to_tuple(nums)

    root = build(orig, 0, n - 1)

    groups =
      Enum.reduce(0..n - 1, %{}, fn i, acc ->
        v = elem(orig, i)
        Map.update(acc, v, [i], &[i | &1])
      end)

    neg_inf = -9_000_000_000_000

    {ans, _} =
      Enum.reduce(groups, {root.best, root}, fn {_val, idxs}, {cur_ans, cur_root} ->
        removed_root = Enum.reduce(idxs, cur_root, fn pos, tr -> update(tr, pos, neg_inf) end)
        new_ans = max(cur_ans, removed_root.best)

        restored_root =
          Enum.reduce(idxs, removed_root, fn pos, tr ->
            orig_val = elem(orig, pos)
            update(tr, pos, orig_val)
          end)

        {new_ans, restored_root}
      end)

    ans
  end

  defp build(arr, l, r) when l == r do
    v = elem(arr, l)

    %Solution{
      l: l,
      r: r,
      sum: v,
      pref: v,
      suff: v,
      best: v
    }
  end

  defp build(arr, l, r) do
    m = div(l + r, 2)
    left = build(arr, l, m)
    right = build(arr, m + 1, r)
    merge(left, right)
  end

  defp merge(left, right) do
    sum = left.sum + right.sum
    pref = max(left.pref, left.sum + right.pref)
    suff = max(right.suff, right.sum + left.suff)
    best = Enum.max([left.best, right.best, left.suff + right.pref])

    %Solution{
      l: left.l,
      r: right.r,
      sum: sum,
      pref: pref,
      suff: suff,
      best: best,
      left: left,
      right: right
    }
  end

  defp update(node, pos, val) do
    if node.l == node.r do
      %Solution{node | sum: val, pref: val, suff: val, best: val}
    else
      if pos <= node.left.r do
        left = update(node.left, pos, val)
        merge(left, node.right)
      else
        right = update(node.right, pos, val)
        merge(node.left, right)
      end
    end
  end
end
```
