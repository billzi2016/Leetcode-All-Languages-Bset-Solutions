# 3165. Maximum Sum of Subsequence With Non-adjacent Elements

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
    static const long long INF_NEG = (long long)-4e18;
    struct Node{
        long long a[2][2];
        Node(long long val=0){
            for(int i=0;i<2;i++)for(int j=0;j<2;j++)a[i][j]=INF_NEG;
            // leaf initialization
            a[0][0]=0;          // previous not taken, current not taken
            a[0][1]=val;        // previous not taken, take current
            a[1][0]=0;          // previous taken, cannot take current
            // a[1][1] stays -inf (impossible)
        }
    };
    
    int n;
    vector<Node> seg;
    
    Node merge(const Node& L, const Node& R){
        Node res;
        for(int i=0;i<2;i++)for(int k=0;k<2;k++)res.a[i][k]=INF_NEG;
        for(int i=0;i<2;i++){
            for(int j=0;j<2;j++){
                if(L.a[i][j]==INF_NEG) continue;
                for(int k=0;k<2;k++){
                    if(R.a[j][k]==INF_NEG) continue;
                    res.a[i][k]=max(res.a[i][k], L.a[i][j]+R.a[j][k]);
                }
            }
        }
        return res;
    }
    
    void build(int idx,int l,int r,const vector<int>& nums){
        if(l==r){
            seg[idx]=Node(nums[l]);
            return;
        }
        int mid=(l+r)/2;
        build(idx*2,l,mid,nums);
        build(idx*2+1,mid+1,r,nums);
        seg[idx]=merge(seg[idx*2],seg[idx*2+1]);
    }
    
    void update(int idx,int l,int r,int pos,int val){
        if(l==r){
            seg[idx]=Node(val);
            return;
        }
        int mid=(l+r)/2;
        if(pos<=mid) update(idx*2,l,mid,pos,val);
        else update(idx*2+1,mid+1,r,pos,val);
        seg[idx]=merge(seg[idx*2],seg[idx*2+1]);
    }
    
public:
    int maximumSumSubsequence(vector<int>& nums, vector<vector<int>>& queries) {
        const long long MOD = 1000000007LL;
        n = nums.size();
        seg.assign(4*n, Node());
        build(1,0,n-1,nums);
        long long total=0;
        for(const auto& q:queries){
            int pos=q[0];
            int x=q[1];
            update(1,0,n-1,pos,x);
            long long cur = max(seg[1].a[0][0], seg[1].a[0][1]);
            total = (total + (cur%MOD+MOD)%MOD) % MOD;
        }
        return (int)total;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static final long NEG = Long.MIN_VALUE / 4;
    private static final int MOD = 1_000_000_007;

    private static class Node {
        long[][] dp = new long[2][2];
        Node() {
            for (int i = 0; i < 2; i++)
                Arrays.fill(dp[i], NEG);
        }
    }

    private final int n;
    private final Node[] seg;

    public Solution(int[] nums) {
        this.n = nums.length;
        seg = new Node[4 * n];
        build(1, 0, n - 1, nums);
    }

    private void build(int idx, int l, int r, int[] arr) {
        if (l == r) {
            seg[idx] = leaf(arr[l]);
            return;
        }
        int mid = (l + r) >>> 1;
        build(idx << 1, l, mid, arr);
        build(idx << 1 | 1, mid + 1, r, arr);
        seg[idx] = merge(seg[idx << 1], seg[idx << 1 | 1]);
    }

    private Node leaf(int val) {
        Node node = new Node();
        node.dp[0][0] = 0;          // not take the element
        node.dp[1][1] = val;        // take the element
        return node;
    }

    private Node merge(Node left, Node right) {
        Node res = new Node();
        for (int a = 0; a < 2; a++) {          // leftmost selected?
            for (int d = 0; d < 2; d++) {      // rightmost selected?
                long best = NEG;
                for (int b = 0; b < 2; b++) {  // left.rightmost
                    if (left.dp[a][b] == NEG) continue;
                    for (int c = 0; c < 2; c++) { // right.leftmost
                        if (right.dp[c][d] == NEG) continue;
                        if (b == 1 && c == 1) continue; // adjacent selected not allowed
                        long cand = left.dp[a][b] + right.dp[c][d];
                        if (cand > best) best = cand;
                    }
                }
                res.dp[a][d] = best;
            }
        }
        return res;
    }

    private void update(int idx, int l, int r, int pos, int val) {
        if (l == r) {
            seg[idx] = leaf(val);
            return;
        }
        int mid = (l + r) >>> 1;
        if (pos <= mid) update(idx << 1, l, mid, pos, val);
        else update(idx << 1 | 1, mid + 1, r, pos, val);
        seg[idx] = merge(seg[idx << 1], seg[idx << 1 | 1]);
    }

    private long queryRootBest() {
        Node root = seg[1];
        long best = NEG;
        for (int a = 0; a < 2; a++) {
            for (int d = 0; d < 2; d++) {
                if (root.dp[a][d] > best) best = root.dp[a][d];
            }
        }
        return Math.max(best, 0); // empty subsequence allowed
    }

    public int maximumSumSubsequence(int[] nums, int[][] queries) {
        Solution solver = new Solution(nums);
        long total = 0;
        for (int[] q : queries) {
            int pos = q[0];
            int val = q[1];
            solver.update(1, 0, solver.n - 1, pos, val);
            total += solver.queryRootBest();
            if (total >= MOD) total %= MOD;
        }
        return (int)(total % MOD);
    }
}
```

## Python

```python
class Solution(object):
    def maximumSumSubsequence(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        INF_NEG = -10**18

        n = len(nums)
        size = 4 * n
        tree = [None] * size

        def leaf_matrix(v):
            return [[0, 0],
                    [v, INF_NEG]]

        def merge(left, right):
            # left segment first, then right segment
            res = [[INF_NEG, INF_NEG], [INF_NEG, INF_NEG]]
            for i in range(2):          # output state of right segment
                for k in range(2):      # input state of left segment
                    best = INF_NEG
                    for j in range(2):  # intermediate state between segments
                        val = right[i][j] + left[j][k]
                        if val > best:
                            best = val
                    res[i][k] = best
            return res

        def build(node, l, r):
            if l == r:
                tree[node] = leaf_matrix(nums[l])
                return
            mid = (l + r) // 2
            left = node * 2
            right = left + 1
            build(left, l, mid)
            build(right, mid + 1, r)
            tree[node] = merge(tree[left], tree[right])

        def update(node, l, r, idx, val):
            if l == r:
                tree[node] = leaf_matrix(val)
                return
            mid = (l + r) // 2
            left = node * 2
            right = left + 1
            if idx <= mid:
                update(left, l, mid, idx, val)
            else:
                update(right, mid + 1, r, idx, val)
            tree[node] = merge(tree[left], tree[right])

        build(1, 0, n - 1)

        total = 0
        for pos, x in queries:
            update(1, 0, n - 1, pos, x)
            root = tree[1]
            ans = max(root[0][0], root[1][0])
            total = (total + ans) % MOD

        return total
```

## Python3

```python
import sys
from typing import List

INF_NEG = -10**18
MOD = 10**9 + 7

def combine(left, right):
    res = [[INF_NEG, INF_NEG], [INF_NEG, INF_NEG]]
    for i in range(2):
        for j in range(2):
            best = INF_NEG
            for a in range(2):
                for b in range(2):
                    if a == 1 and b == 1:
                        continue
                    val = left[i][a] + right[b][j]
                    if val > best:
                        best = val
            res[i][j] = best
    return res

class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        size = 1
        while size < n:
            size <<= 1
        seg = [ [[0, INF_NEG],[INF_NEG, 0]] for _ in range(2 * size) ]  # placeholder

        # build leaves
        for i in range(n):
            x = nums[i]
            seg[size + i] = [
                [0, INF_NEG],
                [INF_NEG, x]
            ]
        for i in range(n, size):
            seg[size + i] = [
                [0, INF_NEG],
                [INF_NEG, 0]
            ]

        # build internal nodes
        for idx in range(size - 1, 0, -1):
            seg[idx] = combine(seg[2 * idx], seg[2 * idx + 1])

        total = 0
        for pos, val in queries:
            idx = size + pos
            seg[idx] = [
                [0, INF_NEG],
                [INF_NEG, val]
            ]
            idx >>= 1
            while idx:
                seg[idx] = combine(seg[2 * idx], seg[2 * idx + 1])
                idx >>= 1
            root = seg[1]
            cur = max(root[0][0], root[0][1], root[1][0], root[1][1])
            total = (total + cur) % MOD

        return total
```

## C

```c
#include <stdlib.h>
#include <limits.h>

#define MOD 1000000007LL
#define NEG_INF (-4LL<<60)

typedef struct {
    long long v[2][2];
} Node;

static Node *tree;
static int N;

static void combine(Node *res, const Node *left, const Node *right) {
    for (int i = 0; i < 2; ++i) {
        for (int j = 0; j < 2; ++j) {
            long long best = NEG_INF;
            for (int k = 0; k < 2; ++k) {
                if (right->v[i][k] == NEG_INF || left->v[k][j] == NEG_INF) continue;
                long long cand = right->v[i][k] + left->v[k][j];
                if (cand > best) best = cand;
            }
            res->v[i][j] = best;
        }
    }
}

static void build(int idx, int l, int r, const int *arr) {
    if (l == r) {
        long long val = arr[l];
        tree[idx].v[0][0] = 0;
        tree[idx].v[0][1] = 0;
        tree[idx].v[1][0] = val;
        tree[idx].v[1][1] = NEG_INF;
        return;
    }
    int mid = (l + r) >> 1;
    build(idx<<1, l, mid, arr);
    build(idx<<1|1, mid+1, r, arr);
    combine(&tree[idx], &tree[idx<<1], &tree[idx<<1|1]);
}

static void update(int idx, int l, int r, int pos, long long val) {
    if (l == r) {
        tree[idx].v[0][0] = 0;
        tree[idx].v[0][1] = 0;
        tree[idx].v[1][0] = val;
        tree[idx].v[1][1] = NEG_INF;
        return;
    }
    int mid = (l + r) >> 1;
    if (pos <= mid) update(idx<<1, l, mid, pos, val);
    else update(idx<<1|1, mid+1, r, pos, val);
    combine(&tree[idx], &tree[idx<<1], &tree[idx<<1|1]);
}

int maximumSumSubsequence(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize) {
    N = numsSize;
    tree = (Node*)malloc(sizeof(Node) * 4 * N);
    build(1, 0, N-1, nums);

    long long total = 0;
    for (int i = 0; i < queriesSize; ++i) {
        int pos = queries[i][0];
        int x   = queries[i][1];
        update(1, 0, N-1, pos, (long long)x);
        long long ans = tree[1].v[0][0];
        if (tree[1].v[1][0] > ans) ans = tree[1].v[1][0];
        if (ans < 0) ans = 0;
        total += ans;
        if (total >= MOD) total %= MOD;
    }
    free(tree);
    return (int)(total % MOD);
}
```

## Csharp

```csharp
using System;

public class Solution {
    private const long MOD = 1000000007L;
    private const long NEG = -(1L << 60);

    private struct Node {
        public long a00, a01, a10, a11; // dp[0,0], dp[0,1], dp[1,0], dp[1,1]

        public long Get(int i, int j) {
            if (i == 0 && j == 0) return a00;
            if (i == 0 && j == 1) return a01;
            if (i == 1 && j == 0) return a10;
            return a11;
        }

        public void Set(int i, int j, long v) {
            if (i == 0 && j == 0) a00 = v;
            else if (i == 0 && j == 1) a01 = v;
            else if (i == 1 && j == 0) a10 = v;
            else a11 = v;
        }
    }

    private int n;
    private Node[] seg;

    public int MaximumSumSubsequence(int[] nums, int[][] queries) {
        n = nums.Length;
        seg = new Node[4 * n];
        Build(1, 0, n - 1, nums);
        long answer = 0;
        foreach (var q in queries) {
            int pos = q[0];
            int val = q[1];
            Update(1, 0, n - 1, pos, val);
            Node root = seg[1];
            long best = Math.Max(Math.Max(root.a00, root.a01), Math.Max(root.a10, root.a11));
            if (best < 0) best = 0;
            answer += best % MOD;
            if (answer >= MOD) answer -= MOD;
        }
        return (int)(answer % MOD);
    }

    private void Build(int idx, int l, int r, int[] nums) {
        if (l == r) {
            SetLeaf(ref seg[idx], nums[l]);
            return;
        }
        int mid = (l + r) >> 1;
        Build(idx << 1, l, mid, nums);
        Build(idx << 1 | 1, mid + 1, r, nums);
        seg[idx] = Merge(seg[idx << 1], seg[idx << 1 | 1]);
    }

    private void Update(int idx, int l, int r, int pos, int val) {
        if (l == r) {
            SetLeaf(ref seg[idx], val);
            return;
        }
        int mid = (l + r) >> 1;
        if (pos <= mid) Update(idx << 1, l, mid, pos, val);
        else Update(idx << 1 | 1, mid + 1, r, pos, val);
        seg[idx] = Merge(seg[idx << 1], seg[idx << 1 | 1]);
    }

    private void SetLeaf(ref Node node, long v) {
        node.a00 = 0;
        node.a01 = NEG;
        node.a10 = NEG;
        node.a11 = v;
    }

    private Node Merge(Node left, Node right) {
        Node res = new Node { a00 = NEG, a01 = NEG, a10 = NEG, a11 = NEG };
        for (int cl = 0; cl < 2; ++cl) {
            for (int cr = 0; cr < 2; ++cr) {
                long best = NEG;
                for (int alr = 0; alr < 2; ++alr) {
                    for (int bfl = 0; bfl < 2; ++bfl) {
                        if (alr == 1 && bfl == 1) continue; // adjacent taken
                        long lv = left.Get(cl, alr);
                        long rv = right.Get(bfl, cr);
                        if (lv == NEG || rv == NEG) continue;
                        long cand = lv + rv;
                        if (cand > best) best = cand;
                    }
                }
                res.Set(cl, cr, best);
            }
        }
        return res;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {number}
 */
var maximumSumSubsequence = function(nums, queries) {
    const MOD = 1_000_000_007;
    const n = nums.length;
    const INF_NEG = -1e18;

    // segment tree storing flattened 2x2 matrix for each node
    const seg = new Array(4 * n);

    const makeLeaf = (v) => {
        const m = new Array(4);
        m[0] = 0;          // prev not taken, last not taken
        m[1] = v;          // prev not taken, last taken
        m[2] = 0;          // prev taken, last not taken
        m[3] = INF_NEG;    // prev taken, last taken (invalid)
        return m;
    };

    const merge = (L, R) => {
        const res = new Array(4);
        for (let a = 0; a < 2; ++a) {
            for (let c = 0; c < 2; ++c) {
                let best = INF_NEG;
                for (let b = 0; b < 2; ++b) {
                    const val = L[a * 2 + b] + R[b * 2 + c];
                    if (val > best) best = val;
                }
                res[a * 2 + c] = best;
            }
        }
        return res;
    };

    const build = (idx, l, r) => {
        if (l === r) {
            seg[idx] = makeLeaf(nums[l]);
            return;
        }
        const mid = (l + r) >> 1;
        build(idx << 1, l, mid);
        build(idx << 1 | 1, mid + 1, r);
        seg[idx] = merge(seg[idx << 1], seg[idx << 1 | 1]);
    };

    const update = (idx, l, r, pos, val) => {
        if (l === r) {
            seg[idx] = makeLeaf(val);
            return;
        }
        const mid = (l + r) >> 1;
        if (pos <= mid) update(idx << 1, l, mid, pos, val);
        else update(idx << 1 | 1, mid + 1, r, pos, val);
        seg[idx] = merge(seg[idx << 1], seg[idx << 1 | 1]);
    };

    build(1, 0, n - 1);

    let total = 0;
    for (const [pos, x] of queries) {
        update(1, 0, n - 1, pos, x);
        const root = seg[1];
        const ans = Math.max(root[0], root[1]); // start with prev not taken
        total += ans % MOD;
        if (total >= MOD) total -= MOD;
    }
    return total % MOD;
};
```

## Typescript

```typescript
function maximumSumSubsequence(nums: number[], queries: number[][]): number {
    const MOD = 1_000_000_007;
    const n = nums.length;

    // each matrix is a flat array of length 4:
    // index = leftState * 2 + rightState, where state 0 = not taken, 1 = taken
    type Mat = number[];

    const seg: Mat[] = new Array(4 * n);

    function leaf(v: number): Mat {
        const INF_NEG = -Infinity;
        return [
            0,          // 00 : both ends not taken
            INF_NEG,    // 01 : impossible for length 1
            INF_NEG,    // 10 : impossible for length 1
            v           // 11 : element taken (may be negative)
        ];
    }

    function merge(a: Mat, b: Mat): Mat {
        const res: Mat = [-Infinity, -Infinity, -Infinity, -Infinity];
        for (let left = 0; left < 2; ++left) {
            for (let rightA = 0; rightA < 2; ++rightA) {
                const av = a[left * 2 + rightA];
                if (av === -Infinity) continue;
                for (let leftB = 0; leftB < 2; ++leftB) {
                    // adjacency constraint between rightA and leftB
                    if (rightA === 1 && leftB === 1) continue;
                    for (let right = 0; right < 2; ++right) {
                        const bv = b[leftB * 2 + right];
                        if (bv === -Infinity) continue;
                        const idx = left * 2 + right;
                        const val = av + bv;
                        if (val > res[idx]) res[idx] = val;
                    }
                }
            }
        }
        return res;
    }

    function build(node: number, l: number, r: number): void {
        if (l === r) {
            seg[node] = leaf(nums[l]);
            return;
        }
        const mid = (l + r) >> 1;
        build(node << 1, l, mid);
        build(node << 1 | 1, mid + 1, r);
        seg[node] = merge(seg[node << 1], seg[node << 1 | 1]);
    }

    function update(node: number, l: number, r: number, idx: number, val: number): void {
        if (l === r) {
            seg[node] = leaf(val);
            return;
        }
        const mid = (l + r) >> 1;
        if (idx <= mid) update(node << 1, l, mid, idx, val);
        else update(node << 1 | 1, mid + 1, r, idx, val);
        seg[node] = merge(seg[node << 1], seg[node << 1 | 1]);
    }

    build(1, 0, n - 1);

    let total = 0;
    for (const [pos, x] of queries) {
        update(1, 0, n - 1, pos, x);
        const root = seg[1];
        const best = Math.max(root[0], root[1], root[2], root[3]);
        total = (total + ((best % MOD) + MOD) % MOD) % MOD;
    }
    return total;
}
```

## Php

```php
class Solution {
    const MOD = 1000000007;
    private $tree = [];
    private $n;

    /**
     * @param Integer[] $nums
     * @param Integer[][] $queries
     * @return Integer
     */
    function maximumSumSubsequence($nums, $queries) {
        $this->n = count($nums);
        $size = 4 * $this->n;
        $this->tree = array_fill(0, $size, [ -1e18, -1e18, -1e18, -1e18 ]);
        $this->build(1, 0, $this->n - 1, $nums);

        $total = 0;
        foreach ($queries as $q) {
            [$pos, $val] = $q;
            $this->update(1, 0, $this->n - 1, $pos, $val);
            $root = $this->tree[1];
            $ans = max($root);
            $total = ($total + $ans) % self::MOD;
        }
        return $total;
    }

    private function build($idx, $l, $r, &$arr) {
        if ($l == $r) {
            $v = $arr[$l];
            // matrix: [00, 01, 10, 11]
            $this->tree[$idx] = [0, -1e18, -1e18, $v];
            return;
        }
        $mid = intdiv($l + $r, 2);
        $this->build($idx * 2, $l, $mid, $arr);
        $this->build($idx * 2 + 1, $mid + 1, $r, $arr);
        $this->tree[$idx] = $this->merge($this->tree[$idx * 2], $this->tree[$idx * 2 + 1]);
    }

    private function update($idx, $l, $r, $pos, $val) {
        if ($l == $r) {
            $this->tree[$idx] = [0, -1e18, -1e18, $val];
            return;
        }
        $mid = intdiv($l + $r, 2);
        if ($pos <= $mid) {
            $this->update($idx * 2, $l, $mid, $pos, $val);
        } else {
            $this->update($idx * 2 + 1, $mid + 1, $r, $pos, $val);
        }
        $this->tree[$idx] = $this->merge($this->tree[$idx * 2], $this->tree[$idx * 2 + 1]);
    }

    private function merge($left, $right) {
        $neg = -1e18;
        $res = [$neg, $neg, $neg, $neg];
        for ($i = 0; $i < 2; ++$i) {          // leftmost state of left segment
            for ($p = 0; $p < 2; ++$p) {      // rightmost state of left segment
                $a = $left[$i * 2 + $p];
                if ($a <= $neg / 2) continue;
                for ($q = 0; $q < 2; ++$q) {  // leftmost state of right segment
                    if ($p == 1 && $q == 1) continue; // adjacent taken not allowed
                    for ($j = 0; $j < 2; ++$j) { // rightmost state of right segment
                        $b = $right[$q * 2 + $j];
                        if ($b <= $neg / 2) continue;
                        $idx = $i * 2 + $j;
                        $val = $a + $b;
                        if ($val > $res[$idx]) {
                            $res[$idx] = $val;
                        }
                    }
                }
            }
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    private let MOD: Int64 = 1_000_000_007
    private var n: Int = 0
    private var seg: [Node] = []
    private let NEG_INF: Int64 = -9_000_000_000_000_000_000

    func maximumSumSubsequence(_ nums: [Int], _ queries: [[Int]]) -> Int {
        n = nums.count
        seg = Array(repeating: Node(dp: Array(repeating: 0, count: 4)), count: 4 * n)
        build(nums, 1, 0, n - 1)

        var total: Int64 = 0
        for q in queries {
            let pos = q[0]
            let x = q[1]
            update(1, 0, n - 1, pos, x)
            let root = seg[1]
            var best: Int64 = 0
            for v in root.dp where v > best { best = v }
            total = (total + best) % MOD
        }
        return Int(total)
    }

    private func build(_ nums: [Int], _ idx: Int, _ l: Int, _ r: Int) {
        if l == r {
            seg[idx] = leaf(nums[l])
            return
        }
        let mid = (l + r) >> 1
        build(nums, idx << 1, l, mid)
        build(nums, idx << 1 | 1, mid + 1, r)
        seg[idx] = merge(seg[idx << 1], seg[idx << 1 | 1])
    }

    private func update(_ idx: Int, _ l: Int, _ r: Int, _ pos: Int, _ val: Int) {
        if l == r {
            seg[idx] = leaf(val)
            return
        }
        let mid = (l + r) >> 1
        if pos <= mid {
            update(idx << 1, l, mid, pos, val)
        } else {
            update(idx << 1 | 1, mid + 1, r, pos, val)
        }
        seg[idx] = merge(seg[idx << 1], seg[idx << 1 | 1])
    }

    private func leaf(_ v: Int) -> Node {
        var dp = Array(repeating: NEG_INF, count: 4)
        dp[0] = 0                     // not take the only element
        dp[3] = Int64(v)              // take it (left and right are both taken)
        return Node(dp: dp)
    }

    private func merge(_ left: Node, _ right: Node) -> Node {
        var dp = Array(repeating: NEG_INF, count: 4)
        for l in 0...1 {
            for r in 0...1 {
                var best = NEG_INF
                for aR in 0...1 {          // state of left segment's rightmost
                    for bL in 0...1 {      // state of right segment's leftmost
                        if !(aR == 1 && bL == 1) {
                            let lv = left.dp[l * 2 + aR]
                            let rv = right.dp[bL * 2 + r]
                            if lv > NEG_INF / 2 && rv > NEG_INF / 2 {
                                best = max(best, lv + rv)
                            }
                        }
                    }
                }
                dp[l * 2 + r] = best
            }
        }
        return Node(dp: dp)
    }

    private struct Node {
        var dp: [Int64]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumSumSubsequence(nums: IntArray, queries: Array<IntArray>): Int {
        val n = nums.size
        val size = 4 * n
        val a00 = LongArray(size)
        val a01 = LongArray(size)
        val b00 = LongArray(size)
        val b01 = LongArray(size)
        val NEG = Long.MIN_VALUE / 4

        fun pull(idx: Int) {
            val left = idx shl 1
            val right = left + 1
            val la00 = a00[left]
            val la01 = a01[left]
            val lb00 = b00[left]
            val lb01 = b01[left]

            val ra00 = a00[right]
            val rb00 = b00[right]
            val rb01 = b01[right]

            a00[idx] = kotlin.math.max(ra00 + la00, rb00 + lb00)
            a01[idx] = kotlin.math.max(ra00 + la01, rb00 + lb01)
            b00[idx] = kotlin.math.max(rb00 + la00, rb01 + lb00)
            b01[idx] = kotlin.math.max(rb00 + la01, rb01 + lb01)
        }

        fun build(idx: Int, l: Int, r: Int) {
            if (l == r) {
                a00[idx] = 0L
                a01[idx] = 0L
                b00[idx] = nums[l].toLong()
                b01[idx] = NEG
                return
            }
            val mid = (l + r) ushr 1
            build(idx shl 1, l, mid)
            build((idx shl 1) + 1, mid + 1, r)
            pull(idx)
        }

        fun update(idx: Int, l: Int, r: Int, pos: Int, value: Long) {
            if (l == r) {
                a00[idx] = 0L
                a01[idx] = 0L
                b00[idx] = value
                b01[idx] = NEG
                return
            }
            val mid = (l + r) ushr 1
            if (pos <= mid) update(idx shl 1, l, mid, pos, value)
            else update((idx shl 1) + 1, mid + 1, r, pos, value)
            pull(idx)
        }

        build(1, 0, n - 1)

        val MOD = 1_000_000_007L
        var total = 0L

        for (q in queries) {
            val pos = q[0]
            val x = q[1].toLong()
            update(1, 0, n - 1, pos, x)
            val ans = kotlin.math.max(a00[1], b00[1])
            total += ans
            if (total >= MOD) total %= MOD
        }
        return (total % MOD).toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;
  static const int _negInf = -9000000000000000000; // sufficiently small

  late List<List<List<int>>> _seg;

  int maximumSumSubsequence(List<int> nums, List<List<int>> queries) {
    final n = nums.length;
    _seg = List.filled(4 * n, [], growable: false);
    _build(1, 0, n - 1, nums);

    int total = 0;
    for (final q in queries) {
      final pos = q[0];
      final x = q[1];
      _update(1, 0, n - 1, pos, x);
      final root = _seg[1];
      int cur = _negInf;
      for (int i = 0; i < 2; ++i) {
        for (int j = 0; j < 2; ++j) {
          if (root[i][j] > cur) cur = root[i][j];
        }
      }
      total = (total + (cur % _mod)) % _mod;
    }
    return total;
  }

  void _build(int node, int l, int r, List<int> nums) {
    if (l == r) {
      final v = nums[l];
      _seg[node] = [
        [0, _negInf],
        [_negInf, v]
      ];
      return;
    }
    final mid = (l + r) >> 1;
    _build(node << 1, l, mid, nums);
    _build((node << 1) | 1, mid + 1, r, nums);
    _seg[node] = _merge(_seg[node << 1], _seg[(node << 1) | 1]);
  }

  void _update(int node, int l, int r, int idx, int val) {
    if (l == r) {
      _seg[node] = [
        [0, _negInf],
        [_negInf, val]
      ];
      return;
    }
    final mid = (l + r) >> 1;
    if (idx <= mid) {
      _update(node << 1, l, mid, idx, val);
    } else {
      _update((node << 1) | 1, mid + 1, r, idx, val);
    }
    _seg[node] = _merge(_seg[node << 1], _seg[(node << 1) | 1]);
  }

  List<List<int>> _merge(List<List<int>> left, List<List<int>> right) {
    final res = List.generate(2, (_) => List.filled(2, _negInf));
    for (int lf = 0; lf < 2; ++lf) {
      for (int ll = 0; ll < 2; ++ll) {
        final lv = left[lf][ll];
        if (lv == _negInf) continue;
        for (int rf = 0; rf < 2; ++rf) {
          for (int rl = 0; rl < 2; ++rl) {
            final rv = right[rf][rl];
            if (rv == _negInf) continue;
            if (ll == 1 && rf == 1) continue; // adjacent conflict
            final nf = lf;
            final nl = rl;
            final sum = lv + rv;
            if (sum > res[nf][nl]) res[nf][nl] = sum;
          }
        }
      }
    }
    return res;
  }
}
```

## Golang

```go
func maximumSumSubsequence(nums []int, queries [][]int) int {
	const INF int64 = -1 << 60
	const MOD int64 = 1000000007

	n := len(nums)
	seg := make([][2][2]int64, 4*n)

	var merge func(a, b [2][2]int64) [2][2]int64
	merge = func(a, b [2][2]int64) [2][2]int64 {
		var res [2][2]int64
		for i := 0; i < 2; i++ {
			for j := 0; j < 2; j++ {
				best := INF
				for x := 0; x < 2; x++ { // right state of left interval
					for y := 0; y < 2; y++ { // left state of right interval
						if x == 1 && y == 1 {
							continue // adjacent selected not allowed
						}
						if a[i][x] == INF || b[y][j] == INF {
							continue
						}
						val := a[i][x] + b[y][j]
						if val > best {
							best = val
						}
					}
				}
				res[i][j] = best
			}
		}
		return res
	}

	var build func(idx, l, r int)
	build = func(idx, l, r int) {
		if l == r {
			for i := 0; i < 2; i++ {
				for j := 0; j < 2; j++ {
					seg[idx][i][j] = INF
				}
			}
			seg[idx][0][0] = 0
			seg[idx][1][1] = int64(nums[l])
			return
		}
		mid := (l + r) / 2
		build(idx*2, l, mid)
		build(idx*2+1, mid+1, r)
		seg[idx] = merge(seg[idx*2], seg[idx*2+1])
	}

	var update func(idx, l, r, pos int, val int64)
	update = func(idx, l, r, pos int, val int64) {
		if l == r {
			for i := 0; i < 2; i++ {
				for j := 0; j < 2; j++ {
					seg[idx][i][j] = INF
				}
			}
			seg[idx][0][0] = 0
			seg[idx][1][1] = val
			return
		}
		mid := (l + r) / 2
		if pos <= mid {
			update(idx*2, l, mid, pos, val)
		} else {
			update(idx*2+1, mid+1, r, pos, val)
		}
		seg[idx] = merge(seg[idx*2], seg[idx*2+1])
	}

	build(1, 0, n-1)

	var ans int64
	for _, q := range queries {
		pos, x := q[0], int64(q[1])
		update(1, 0, n-1, pos, x)
		root := seg[1]
		maxVal := INF
		for i := 0; i < 2; i++ {
			for j := 0; j < 2; j++ {
				if root[i][j] > maxVal {
					maxVal = root[i][j]
				}
			}
		}
		ans = (ans + ((maxVal%MOD)+MOD)%MOD) % MOD
	}
	return int(ans)
}
```

## Ruby

```ruby
def maximum_sum_subsequence(nums, queries)
  mod = 1_000_000_007
  inf = -(1 << 60)

  n = nums.length
  size = 1
  size <<= 1 while size < n

  tree = Array.new(2 * size) { Array.new(4, inf) }

  build_leaf = ->(val) {
    leaf = Array.new(4, inf)
    leaf[0] = 0          # both ends not selected
    leaf[3] = val        # single element selected
    leaf
  }

  n.times do |i|
    tree[size + i] = build_leaf.call(nums[i])
  end

  merge = ->(left, right) {
    res = Array.new(4, inf)
    2.times do |l|
      2.times do |r|
        best = inf
        2.times do |le|
          2.times do |rs|
            next if le == 1 && rs == 1
            val = left[l * 2 + le] + right[rs * 2 + r]
            best = val if val > best
          end
        end
        res[l * 2 + r] = best
      end
    end
    res
  }

  (size - 1).downto(1) do |i|
    tree[i] = merge.call(tree[i << 1], tree[(i << 1) + 1])
  end

  total = 0
  queries.each do |pos, x|
    idx = size + pos
    tree[idx] = build_leaf.call(x)
    while idx > 1
      idx >>= 1
      tree[idx] = merge.call(tree[idx << 1], tree[(idx << 1) + 1])
    end
    total += tree[1].max
    total %= mod
  end

  total % mod
end
```

## Scala

```scala
object Solution {
    def maximumSumSubsequence(nums: Array[Int], queries: Array[Array[Int]]): Int = {
        val MOD = 1000000007L
        val INF_NEG = -9_000_000_000_000_000_000L

        def combine(left: Array[Array[Long]], right: Array[Array[Long]]): Array[Array[Long]] = {
            val res = Array.ofDim[Long](2, 2)
            for (i <- 0 to 1) {
                for (j <- 0 to 1) {
                    var best = INF_NEG
                    for (m <- 0 to 1) {
                        for (n <- 0 to 1) {
                            if (!(m == 1 && n == 1)) {
                                val a = left(i)(m)
                                val b = right(n)(j)
                                if (a != INF_NEG && b != INF_NEG) {
                                    val sum = a + b
                                    if (sum > best) best = sum
                                }
                            }
                        }
                    }
                    res(i)(j) = best
                }
            }
            res
        }

        class SegTree(val size: Int) {
            private val tree = new Array[Array[Array[Long]]](4 * size)

            def build(node: Int, l: Int, r: Int): Unit = {
                if (l == r) {
                    val dp = Array.ofDim[Long](2, 2)
                    for (i <- 0 to 1; j <- 0 to 1) dp(i)(j) = INF_NEG
                    dp(0)(0) = 0L
                    dp(1)(1) = nums(l).toLong
                    tree(node) = dp
                } else {
                    val mid = (l + r) >>> 1
                    build(node << 1, l, mid)
                    build((node << 1) | 1, mid + 1, r)
                    tree(node) = combine(tree(node << 1), tree((node << 1) | 1))
                }
            }

            def update(node: Int, l: Int, r: Int, pos: Int, value: Long): Unit = {
                if (l == r) {
                    val dp = Array.ofDim[Long](2, 2)
                    for (i <- 0 to 1; j <- 0 to 1) dp(i)(j) = INF_NEG
                    dp(0)(0) = 0L
                    dp(1)(1) = value
                    tree(node) = dp
                } else {
                    val mid = (l + r) >>> 1
                    if (pos <= mid) update(node << 1, l, mid, pos, value)
                    else update((node << 1) | 1, mid + 1, r, pos, value)
                    tree(node) = combine(tree(node << 1), tree((node << 1) | 1))
                }
            }

            def rootMax(): Long = {
                val dp = tree(1)
                var best = 0L
                for (i <- 0 to 1; j <- 0 to 1) {
                    if (dp(i)(j) > best) best = dp(i)(j)
                }
                best
            }
        }

        val seg = new SegTree(nums.length)
        seg.build(1, 0, nums.length - 1)

        var total: Long = 0L
        for (q <- queries) {
            val pos = q(0)
            val x = q(1).toLong
            seg.update(1, 0, nums.length - 1, pos, x)
            val cur = seg.rootMax()
            total += cur % MOD
            if (total >= MOD) total -= MOD
        }
        ((total % MOD) + MOD).toInt
    }
}
```

## Rust

```rust
use std::cmp::max;

const MOD: i64 = 1_000_000_007;
const NEG_INF: i64 = -(1_i64 << 60);

struct SegTree {
    n: usize,
    data: Vec<[[i64; 2]; 2]>,
}

impl SegTree {
    fn new(nums: &[i32]) -> Self {
        let n = nums.len();
        let mut st = SegTree {
            n,
            data: vec![[[NEG_INF; 2]; 2]; 4 * n],
        };
        st.build(1, 0, n - 1, nums);
        st
    }

    fn leaf_matrix(val: i32) -> [[i64; 2]; 2] {
        let mut m = [[NEG_INF; 2]; 2];
        m[0][0] = 0;
        m[1][1] = val as i64;
        m
    }

    fn build(&mut self, idx: usize, l: usize, r: usize, nums: &[i32]) {
        if l == r {
            self.data[idx] = Self::leaf_matrix(nums[l]);
            return;
        }
        let mid = (l + r) / 2;
        self.build(idx * 2, l, mid, nums);
        self.build(idx * 2 + 1, mid + 1, r, nums);
        self.data[idx] = Self::merge(&self.data[idx * 2], &self.data[idx * 2 + 1]);
    }

    fn merge(left: &[[i64; 2]; 2], right: &[[i64; 2]; 2]) -> [[i64; 2]; 2] {
        let mut res = [[NEG_INF; 2]; 2];
        for a in 0..2 {
            for d in 0..2 {
                let mut best = NEG_INF;
                for b in 0..2 {
                    for c in 0..2 {
                        if !(b == 1 && c == 1) {
                            let lv = left[a][b];
                            let rv = right[c][d];
                            if lv > NEG_INF / 2 && rv > NEG_INF / 2 {
                                best = max(best, lv + rv);
                            }
                        }
                    }
                }
                res[a][d] = best;
            }
        }
        res
    }

    fn update(&mut self, pos: usize, val: i32) {
        self.update_rec(1, 0, self.n - 1, pos, val);
    }

    fn update_rec(&mut self, idx: usize, l: usize, r: usize, pos: usize, val: i32) {
        if l == r {
            self.data[idx] = Self::leaf_matrix(val);
            return;
        }
        let mid = (l + r) / 2;
        if pos <= mid {
            self.update_rec(idx * 2, l, mid, pos, val);
        } else {
            self.update_rec(idx * 2 + 1, mid + 1, r, pos, val);
        }
        self.data[idx] = Self::merge(&self.data[idx * 2], &self.data[idx * 2 + 1]);
    }

    fn root_max(&self) -> i64 {
        let mat = &self.data[1];
        let mut ans = 0i64; // empty subsequence
        for a in 0..2 {
            for b in 0..2 {
                ans = max(ans, mat[a][b]);
            }
        }
        ans
    }
}

impl Solution {
    pub fn maximum_sum_subsequence(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> i32 {
        let mut seg = SegTree::new(&nums);
        let mut total: i64 = 0;
        for q in queries.iter() {
            let pos = q[0] as usize;
            let val = q[1];
            seg.update(pos, val);
            total += seg.root_max();
            if total >= MOD {
                total %= MOD;
            }
        }
        (total % MOD) as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)
(define INF (expt 2 60))
(define NEG-INF (- INF))

;; matrix for a single element value v
(define (leaf-matrix v)
  (vector 0 v 0 NEG-INF)) ; [0][0]=0, [0][1]=v, [1][0]=0, [1][1]=-inf

;; combine two matrices using max‑plus multiplication
(define (combine left right)
  (let* ((a00 (vector-ref left 0))
         (a01 (vector-ref left 1))
         (a10 (vector-ref left 2))
         (a11 (vector-ref left 3))
         (b00 (vector-ref right 0))
         (b01 (vector-ref right 1))
         (b10 (vector-ref right 2))
         (b11 (vector-ref right 3)))
    (vector
     (max (+ a00 b00) (+ a01 b10)) ; c00
     (max (+ a00 b01) (+ a01 b11)) ; c01
     (max (+ a10 b00) (+ a11 b10)) ; c10
     (max (+ a10 b01) (+ a11 b11))))) ; c11

;; build segment tree from vector of numbers
(define (make-segtree nums-vec)
  (let* ((n (vector-length nums-vec))
         (size (* 4 n))
         (seg (make-vector size #f)))
    (define (build idx l r)
      (if (= l r)
          (vector-set! seg idx (leaf-matrix (vector-ref nums-vec l)))
          (let ((mid (quotient (+ l r) 2)))
            (build (+ (* idx 2) 1) l mid)
            (build (+ (* idx 2) 2) (+ mid 1) r)
            (vector-set! seg idx
                         (combine (vector-ref seg (+ (* idx 2) 1))
                                  (vector-ref seg (+ (* idx 2) 2)))))))
    (build 0 0 (- n 1))
    (values seg n)))

;; point update
(define (update! seg n pos val)
  (define (upd idx l r)
    (if (= l r)
        (vector-set! seg idx (leaf-matrix val))
        (let ((mid (quotient (+ l r) 2)))
          (if (<= pos mid)
              (upd (+ (* idx 2) 1) l mid)
              (upd (+ (* idx 2) 2) (+ mid 1) r))
          (vector-set! seg idx
                       (combine (vector-ref seg (+ (* idx 2) 1))
                                (vector-ref seg (+ (* idx 2) 2)))))))
  (upd 0 0 (- n 1)))

;; modular addition handling negatives
(define (mod-add a b)
  (let ((s (+ a b)))
    (if (>= s MOD) (- s MOD) s)))

(define (maximum-sum-subsequence nums queries)
  (let* ((nums-vec (list->vector nums))
         (values (make-segtree nums-vec))
         (seg (car values))
         (n (cadr values)))
    (foldl
     (lambda (q acc)
       (define pos (first q))
       (define val (second q))
       (update! seg n pos val)
       (let* ((root (vector-ref seg 0))
              (ans (max (vector-ref root 0) (vector-ref root 1))))
         (mod-add acc ans)))
     0
     queries)))
```

## Erlang

```erlang
-module(solution).
-export([maximum_sum_subsequence/2]).

-define(MOD, 1000000007).
-define(NEG_INF, -1152921504606846976). % -(2^60)

%% Public API
-spec maximum_sum_subsequence(Nums :: [integer()], Queries :: [[integer()]]) -> integer().
maximum_sum_subsequence(Nums, Queries) ->
    N = length(Nums),
    NumTuple = list_to_tuple(Nums),
    {Tree0, _} = build(NumTuple, 1, N, 1, #{}),
    process_queries(Queries, Tree0, N, 0).

%% Process all queries, accumulating answer modulo MOD
process_queries([], _Tree, _N, Acc) ->
    Acc rem ?MOD;
process_queries([[Pos, X] | Rest], Tree, N, Acc) ->
    Index = Pos + 1, % convert to 1‑based
    {NewTree, _} = update(Index, X, 1, N, 1, Tree),
    Root = maps:get(1, NewTree),
    {A00, A01, _, _} = Root,
    CurAns = max(A00, A01),
    NewAcc = (Acc + CurAns) rem ?MOD,
    process_queries(Rest, NewTree, N, NewAcc).

%% Build segment tree recursively
-spec build(tuple(), integer(), integer(), integer(), map()) -> {map(), integer()}.
build(_NumTuple, L, R, Idx, Map) when L =:= R ->
    V = element(L, _NumTuple),
    Leaf = leaf(V),
    {maps:put(Idx, Leaf, Map), Idx};
build(NumTuple, L, R, Idx, Map) ->
    Mid = (L + R) div 2,
    {Map1, _} = build(NumTuple, L, Mid, Idx * 2, Map),
    {Map2, _} = build(NumTuple, Mid + 1, R, Idx * 2 + 1, Map1),
    LeftM  = maps:get(Idx * 2, Map2),
    RightM = maps:get(Idx * 2 + 1, Map2),
    Combined = combine(LeftM, RightM),
    {maps:put(Idx, Combined, Map2), Idx}.

%% Update a single position
-spec update(integer(), integer(), integer(), integer(), integer(), map()) -> {map(), integer()}.
update(Index, Val, L, R, Idx, Map) when L =:= R ->
    NewLeaf = leaf(Val),
    {maps:put(Idx, NewLeaf, Map), Idx};
update(Index, Val, L, R, Idx, Map) ->
    Mid = (L + R) div 2,
    if
        Index =< Mid ->
            {UpdMap, _} = update(Index, Val, L, Mid, Idx * 2, Map);
        true ->
            {UpdMap, _} = update(Index, Val, Mid + 1, R, Idx * 2 + 1, Map)
    end,
    LeftM  = maps:get(Idx * 2, UpdMap),
    RightM = maps:get(Idx * 2 + 1, UpdMap),
    Combined = combine(LeftM, RightM),
    {maps:put(Idx, Combined, UpdMap), Idx}.

%% Leaf matrix for a single element value V
-spec leaf(integer()) -> {integer(), integer(), integer(), integer()}.
leaf(V) ->
    {?NEG_INF, V, 0, ?NEG_INF}. % stored as {A00,A01,A10,A11}
    % Actually A00 = 0 (skip when prev not taken)
    % A01 = V (take when prev not taken)
    % A10 = 0 (must skip when prev taken)
    % A11 = -inf (invalid)

%% Combine two matrices using max‑plus multiplication
-spec combine({integer(), integer(), integer(), integer()},
              {integer(), integer(), integer(), integer()}) ->
                 {integer(), integer(), integer(), integer()}.
combine({A00, A01, A10, A11}, {B00, B01, B10, B11}) ->
    C00 = max(A00 + B00, A01 + B10),
    C01 = max(A00 + B01, A01 + B11),
    C10 = max(A10 + B00, A11 + B10),
    C11 = max(A10 + B01, A11 + B11),
    {C00, C01, C10, C11}.

%% Simple max for two integers
-spec max(integer(), integer()) -> integer().
max(X, Y) when X >= Y -> X;
max(_, Y) -> Y.
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false

  @neg_inf -10_000_000_000_000_000_000
  @mod 1_000_000_007

  defstruct l: 0, r: 0, left: nil, right: nil, mat: nil

  # matrix stored as {a00,a01,a10,a11}
  defp leaf_matrix(v) do
    {0, 0, v, @neg_inf}
  end

  defp merge({l00, l01, l10, l11}, {r00, r01, r10, r11}) do
    c00 = max(r00 + l00, r01 + l10)
    c01 = max(r00 + l01, r01 + l11)
    c10 = max(r10 + l00, r11 + l10)
    c11 = max(r10 + l01, r11 + l11)
    {c00, c01, c10, c11}
  end

  defp build(arr, l, r) do
    if l == r do
      %__MODULE__{
        l: l,
        r: r,
        mat: leaf_matrix(:array.get(l, arr))
      }
    else
      m = div(l + r, 2)
      left = build(arr, l, m)
      right = build(arr, m + 1, r)
      %__MODULE__{
        l: l,
        r: r,
        left: left,
        right: right,
        mat: merge(left.mat, right.mat)
      }
    end
  end

  defp update(node, pos, val) do
    if node.l == node.r do
      %__MODULE__{node | mat: leaf_matrix(val)}
    else
      if pos <= node.left.r do
        new_left = update(node.left, pos, val)
        %__MODULE__{
          node |
          left: new_left,
          mat: merge(new_left.mat, node.right.mat)
        }
      else
        new_right = update(node.right, pos, val)
        %__MODULE__{
          node |
          right: new_right,
          mat: merge(node.left.mat, new_right.mat)
        }
      end
    end
  end

  defp answer(node) do
    {a00, _a01, a10, _a11} = node.mat
    max(a00, a10)
  end

  @spec maximum_sum_subsequence(nums :: [integer], queries :: [[integer]]) :: integer
  def maximum_sum_subsequence(nums, queries) do
    n = length(nums)
    arr = :array.from_list(nums)
    root = build(arr, 0, n - 1)

    {total, _} =
      Enum.reduce(queries, {0, root}, fn [pos, x], {acc, cur_root} ->
        new_root = update(cur_root, pos, x)
        ans = answer(new_root)
        {(rem(acc + ans, @mod)), new_root}
      end)

    total
  end
end
```
