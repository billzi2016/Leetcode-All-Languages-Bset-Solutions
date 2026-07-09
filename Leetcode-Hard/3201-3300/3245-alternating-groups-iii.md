# 3245. Alternating Groups III

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
    struct BIT{
        int N;
        vector<long long> t;
        BIT(int n=0){init(n);}
        void init(int n){
            N=n;
            t.assign(N+1,0);
        }
        void add(int idx,long long val){
            for(;idx<=N;idx+=idx&-idx) t[idx]+=val;
        }
        long long sumPrefix(int idx) const{
            long long r=0;
            for(;idx>0;idx-=idx&-idx) r+=t[idx];
            return r;
        }
    };
public:
    vector<int> numberOfAlternatingGroups(vector<int>& colors, vector<vector<int>>& queries) {
        int n = colors.size();
        BIT bitCnt(n), bitSum(n);
        vector<char> isBreakEdge(n,0);
        set<int> breaks; // indices i where edge i-(i+1)%n is a break (same color)

        auto dist=[&](int a,int b)->int{
            int d = b - a;
            if(d<=0) d+=n;
            return d;
        };

        // initial breaks
        for(int i=0;i<n;++i){
            if(colors[i]==colors[(i+1)%n]){
                isBreakEdge[i]=1;
                breaks.insert(i);
            }
        }

        // build BIT with run lengths
        if(!breaks.empty()){
            for(auto it=breaks.begin();it!=breaks.end();++it){
                auto nxtIt = next(it);
                if(nxtIt==breaks.end()) nxtIt=breaks.begin();
                int L = dist(*it,*nxtIt);
                bitCnt.add(L,1);
                bitSum.add(L,L);
            }
        }

        vector<int> ans;
        for(const auto& q: queries){
            if(q[0]==1){ // query count
                int k=q[1];
                long long res=0;
                if(breaks.empty()){
                    if(k<n) res=n;
                    else if(k==n) res=1;
                    else res=0;
                }else{
                    long long cnt_ge = bitCnt.sumPrefix(n) - bitCnt.sumPrefix(k-1);
                    long long sum_ge = bitSum.sumPrefix(n) - bitSum.sumPrefix(k-1);
                    res = sum_ge - (long long)(k-1)*cnt_ge;
                }
                ans.push_back((int)res);
            }else{ // update
                int idx=q[1];
                int col=q[2];
                if(colors[idx]==col) continue;

                int e1=(idx-1+n)%n;
                int e2=idx;
                bool old1=isBreakEdge[e1];
                bool old2=isBreakEdge[e2];

                colors[idx]=col;

                bool new1 = (colors[e1]==colors[(e1+1)%n]);
                bool new2 = (colors[e2]==colors[(e2+1)%n]);

                auto processChange=[&](int e,bool oldB,bool newB){
                    if(oldB==newB) return;
                    if(oldB && !newB){ // remove break
                        if(breaks.size()==1){
                            // only this break existed
                            bitCnt.add(n,-1);
                            bitSum.add(n,-n);
                            breaks.erase(e);
                        }else{
                            auto it=breaks.find(e);
                            auto nxtIt=next(it);
                            if(nxtIt==breaks.end()) nxtIt=breaks.begin();
                            int nxt=*nxtIt;
                            int prv;
                            if(it==breaks.begin()){
                                auto lastIt=breaks.end(); --lastIt;
                                prv=*lastIt;
                            }else{
                                auto prevIt=it; --prevIt;
                                prv=*prevIt;
                            }
                            int L1=dist(prv,e);
                            int L2=dist(e,nxt);
                            int L =dist(prv,nxt);
                            bitCnt.add(L1,-1); bitSum.add(L1,-L1);
                            bitCnt.add(L2,-1); bitSum.add(L2,-L2);
                            bitCnt.add(L,1);   bitSum.add(L,L);
                            breaks.erase(it);
                        }
                    }else if(!oldB && newB){ // add break
                        if(breaks.empty()){
                            // first break
                            bitCnt.add(n,1);
                            bitSum.add(n,n);
                            breaks.insert(e);
                        }else{
                            auto nxtIt=breaks.lower_bound(e);
                            int nxt;
                            if(nxtIt==breaks.end()) nxt=*breaks.begin();
                            else nxt=*nxtIt;
                            int prv;
                            if(nxtIt==breaks.begin()){
                                auto lastIt=breaks.end(); --lastIt;
                                prv=*lastIt;
                            }else{
                                auto prevIt=nxtIt; --prevIt;
                                prv=*prevIt;
                            }
                            int L =dist(prv,nxt);
                            int L1=dist(prv,e);
                            int L2=dist(e,nxt);
                            bitCnt.add(L,-1); bitSum.add(L,-L);
                            bitCnt.add(L1,1); bitSum.add(L1,L1);
                            bitCnt.add(L2,1); bitSum.add(L2,L2);
                            breaks.insert(e);
                        }
                    }
                };

                processChange(e1,old1,new1);
                processChange(e2,old2,new2);
                isBreakEdge[e1]=new1;
                isBreakEdge[e2]=new2;
            }
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static class Fenwick {
        int n;
        long[] bit;
        Fenwick(int n) { this.n = n; bit = new long[n + 2]; }
        void add(int idx, long delta) {
            for (int i = idx; i <= n; i += i & -i) bit[i] += delta;
        }
        long sum(int idx) {
            long res = 0;
            for (int i = idx; i > 0; i -= i & -i) res += bit[i];
            return res;
        }
    }

    private int n;
    private int[] colors;
    private boolean[] diff;
    private Fenwick cntBIT, sumBIT;
    private TreeMap<Integer, Integer> intervals; // start -> end (exclusive)
    private TreeMap<Integer, Integer> ends;      // end   -> start

    public List<Integer> numberOfAlternatingGroups(int[] colors, int[][] queries) {
        this.n = colors.length;
        this.colors = colors.clone();
        diff = new boolean[n];
        for (int i = 0; i < n; i++) diff[i] = this.colors[i] != this.colors[(i + 1) % n];

        cntBIT = new Fenwick(n);
        sumBIT = new Fenwick(n);
        intervals = new TreeMap<>();
        ends = new TreeMap<>();

        // build initial intervals of true diffs
        int i = 0;
        while (i < n) {
            if (!diff[i]) { i++; continue; }
            int start = i;
            while (i < n && diff[i]) i++;
            int end = i; // exclusive
            insertInterval(start, end);
        }

        List<Integer> ansList = new ArrayList<>();
        for (int[] q : queries) {
            if (q[0] == 1) { // query count
                int k = q[1];
                ansList.add(queryCount(k));
            } else { // update
                int idx = q[1];
                int col = q[2];
                if (colors[idx] != col) {
                    colors[idx] = col;
                    int left = (idx - 1 + n) % n;
                    int right = idx;
                    toggleEdge(left);
                    toggleEdge(right);
                }
            }
        }
        return ansList;
    }

    private void insertInterval(int l, int r) { // [l,r)
        intervals.put(l, r);
        ends.put(r, l);
        int len = r - l;
        cntBIT.add(len, 1);
        sumBIT.add(len, len);
    }

    private void deleteInterval(int l, int r) {
        intervals.remove(l);
        ends.remove(r);
        int len = r - l;
        cntBIT.add(len, -1);
        sumBIT.add(len, -len);
    }

    private void toggleEdge(int pos) { // flip diff[pos]
        boolean old = diff[pos];
        boolean now = colors[pos] != colors[(pos + 1) % n];
        if (old == now) return;
        diff[pos] = now;
        if (now) addEdge(pos);
        else removeEdge(pos);
    }

    private void addEdge(int p) { // diff[p] becomes true
        Integer leftStart = null;
        Map.Entry<Integer, Integer> leftEntry = intervals.floorEntry(p);
        if (leftEntry != null && leftEntry.getValue() == p) leftStart = leftEntry.getKey();

        Integer rightStart = null, rightEnd = null;
        if (intervals.containsKey(p + 1)) {
            rightStart = p + 1;
            rightEnd = intervals.get(rightStart);
        }

        if (leftStart != null && rightStart != null) { // merge three parts
            int leftLen = p - leftStart;          // not used directly
            int rightLen = rightEnd - rightStart;
            deleteInterval(leftStart, p);
            deleteInterval(rightStart, rightEnd);
            insertInterval(leftStart, rightEnd);
        } else if (leftStart != null) { // extend left interval
            deleteInterval(leftStart, p);
            insertInterval(leftStart, p + 1);
        } else if (rightStart != null) { // extend right interval backward
            deleteInterval(rightStart, rightEnd);
            insertInterval(p, rightEnd);
        } else { // new single edge interval
            insertInterval(p, p + 1);
        }
    }

    private void removeEdge(int p) { // diff[p] becomes false
        Map.Entry<Integer, Integer> entry = intervals.floorEntry(p);
        int s = entry.getKey();
        int e = entry.getValue(); // e > p
        deleteInterval(s, e);
        if (s < p) insertInterval(s, p);
        if (p + 1 < e) insertInterval(p + 1, e);
    }

    private int queryCount(int k) {
        int t = k - 1; // minimal edge length needed
        long totalCnt = cntBIT.sum(n);
        long totalSum = sumBIT.sum(n);
        long cntGe = totalCnt - (t > 0 ? cntBIT.sum(t - 1) : 0);
        long sumGe = totalSum - (t > 0 ? sumBIT.sum(t - 1) : 0);
        long ans = sumGe - (long) (k - 2) * cntGe;

        // handle wrap-around correction if needed
        if (!intervals.isEmpty()) {
            Integer startLenObj = intervals.get(0);
            Integer endStartKey = ends.get(n);
            boolean wholeRun = intervals.size() == 1 && startLenObj != null && startLenObj == n;
            if (startLenObj != null && endStartKey != null && !wholeRun) {
                int startLen = startLenObj;
                int endLen = n - endStartKey; // interval [endStartKey, n)
                long contribStart = Math.max(0L, startLen - t + 1);
                long contribEnd = Math.max(0L, endLen - t + 1);
                long mergedLen = startLen + endLen;
                long contribMerged = Math.max(0L, mergedLen - t + 1);
                ans = ans - contribStart - contribEnd + contribMerged;
            }
        }

        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfAlternatingGroups(self, colors, queries):
        """
        :type colors: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(colors)

        # Fenwick Tree for counts and sums of run lengths
        size = n
        cntBIT = [0] * (size + 2)
        sumBIT = [0] * (size + 2)

        def bit_add(bit, idx, delta):
            i = idx
            while i <= size:
                bit[i] += delta
                i += i & -i

        def bit_sum(bit, idx):
            s = 0
            i = idx
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        def add_run(L, delta):
            if L <= 0:
                return
            bit_add(cntBIT, L, delta)
            bit_add(sumBIT, L, delta * L)

        # Segment tree for good array (edges where colors differ)
        good = [1 if colors[i] != colors[(i + 1) % n] else 0 for i in range(n)]

        class Node:
            __slots__ = ('l', 'r', 'pref', 'suff', 'all')
            def __init__(self, l=0, r=0, pref=0, suff=0, all=False):
                self.l = l
                self.r = r
                self.pref = pref
                self.suff = suff
                self.all = all

        seg = [Node() for _ in range(4 * n)]

        def pull(idx):
            left = seg[idx << 1]
            right = seg[idx << 1 | 1]
            node = seg[idx]
            node.l = left.l + right.l
            node.pref = left.pref if not left.all else left.l + right.pref
            node.suff = right.suff if not right.all else right.l + left.suff
            node.all = left.all and right.all

        def build(idx, l, r):
            if l == r:
                val = good[l]
                seg[idx] = Node(1, 1, val, val, val == 1)
                return
            m = (l + r) >> 1
            build(idx << 1, l, m)
            build(idx << 1 | 1, m + 1, r)
            pull(idx)

        def update(idx, l, r, pos, val):
            if l == r:
                seg[idx] = Node(1, 1, val, val, val == 1)
                return
            m = (l + r) >> 1
            if pos <= m:
                update(idx << 1, l, m, pos, val)
            else:
                update(idx << 1 | 1, m + 1, r, pos, val)
            pull(idx)

        def query(idx, l, r, ql, qr):
            if ql <= l and r <= qr:
                return seg[idx]
            m = (l + r) >> 1
            if qr <= m:
                return query(idx << 1, l, m, ql, qr)
            if ql > m:
                return query(idx << 1 | 1, m + 1, r, ql, qr)
            left = query(idx << 1, l, m, ql, qr)
            right = query(idx << 1 | 1, m + 1, r, ql, qr)
            res = Node()
            res.l = left.l + right.l
            res.pref = left.pref if not left.all else left.l + right.pref
            res.suff = right.suff if not right.all else right.l + left.suff
            res.all = left.all and right.all
            return res

        build(1, 0, n - 1)

        # initialize runs from good array (circular)
        runs = []
        i = 0
        while i < n:
            if good[i] == 1:
                j = i
                while j + 1 < n and good[j + 1] == 1:
                    j += 1
                runs.append(j - i + 1)
                i = j + 1
            else:
                i += 1

        if runs and good[0] == 1 and good[-1] == 1:
            # merge first and last run
            merged = runs[0] + runs[-1]
            runs[0] = merged
            runs.pop()
        for L in runs:
            add_run(L, 1)

        total_cnt = bit_sum(cntBIT, size)
        total_sum = bit_sum(sumBIT, size)

        ans = []

        for q in queries:
            if q[0] == 1:
                k = q[1]
                t = k - 1
                if t <= 0 or t > n:
                    ans.append(0)
                    continue
                cnt_le = bit_sum(cntBIT, t - 1)
                sum_le = bit_sum(sumBIT, t - 1)
                cnt_ge = total_cnt - cnt_le
                sum_ge = total_sum - sum_le
                res = sum_ge - (t - 1) * cnt_ge
                ans.append(res)
            else:
                pos, newc = q[1], q[2]
                if colors[pos] == newc:
                    continue
                # edges affected: a = (pos-1)%n , b = pos
                for edge in ((pos - 1) % n, pos):
                    old = good[edge]
                    new = 1 if colors[(edge)] != colors[(edge + 1) % n] else 0
                    # after color change, recompute using tentative new colors
                    # we will compute new based on updated colors later
                # apply the color change first
                colors[pos] = newc
                # now process each edge
                for edge in ((pos - 1) % n, pos):
                    old = good[edge]
                    new = 1 if colors[edge] != colors[(edge + 1) % n] else 0
                    if old == new:
                        continue
                    # update segment tree and good array later after handling runs
                    # compute left_len and right_len based on current good (before change)
                    if edge == 0:
                        left_len = 0
                    else:
                        left_node = query(1, 0, n - 1, 0, edge - 1)
                        left_len = left_node.suff
                    if edge == n - 1:
                        right_len = 0
                    else:
                        right_node = query(1, 0, n - 1, edge + 1, n - 1)
                        right_len = right_node.pref

                    if old == 0 and new == 1:
                        # merging runs
                        if left_len > 0:
                            add_run(left_len, -1)
                            total_cnt -= 1
                            total_sum -= left_len
                        if right_len > 0:
                            add_run(right_len, -1)
                            total_cnt -= 1
                            total_sum -= right_len
                        merged = left_len + right_len + 1
                        add_run(merged, 1)
                        total_cnt += 1
                        total_sum += merged
                    else:  # old ==1 and new==0
                        # splitting run
                        orig = left_len + right_len + 1
                        add_run(orig, -1)
                        total_cnt -= 1
                        total_sum -= orig
                        if left_len > 0:
                            add_run(left_len, 1)
                            total_cnt += 1
                            total_sum += left_len
                        if right_len > 0:
                            add_run(right_len, 1)
                            total_cnt += 1
                            total_sum += right_len

                    # apply point update in segment tree and good array
                    good[edge] = new
                    update(1, 0, n - 1, edge, new)

        return ans
```

## Python3

```python
class Solution:
    def numberOfAlternatingGroups(self, colors, queries):
        n = len(colors)
        self.n = n

        class BIT:
            __slots__ = ("n", "bit")
            def __init__(self, n):
                self.n = n
                self.bit = [0] * (n + 2)

            def add(self, idx, delta):
                i = idx + 1
                while i <= self.n + 1:
                    self.bit[i] += delta
                    i += i & -i

            def sum(self, idx):
                if idx < 0:
                    return 0
                i = idx + 1
                s = 0
                while i > 0:
                    s += self.bit[i]
                    i -= i & -i
                return s

            def total(self):
                return self.sum(self.n - 1)

            # find smallest index such that prefix sum >= k (k>=1)
            def kth(self, k):
                idx = 0
                bitmask = 1 << (self.n.bit_length())
                while bitmask:
                    nxt = idx + bitmask
                    if nxt <= self.n and self.bit[nxt] < k:
                        idx = nxt
                        k -= self.bit[nxt]
                    bitmask >>= 1
                return idx  # zero‑based

        self.badBIT = BIT(n)          # marks bad edges
        self.cntBIT = BIT(n)          # frequency of run lengths
        self.lenBIT = BIT(n)          # sum of lengths (len * freq)

        # initial bad edges
        B = 0
        for i in range(n):
            if colors[i] == colors[(i + 1) % n]:
                self.badBIT.add(i, 1)
                B += 1
        self.B = B

        def add_run(L):
            self.cntBIT.add(L, 1)
            self.lenBIT.add(L, L)

        def remove_run(L):
            self.cntBIT.add(L, -1)
            self.lenBIT.add(L, -L)

        if B > 0:
            bads = [i for i in range(n) if colors[i] == colors[(i + 1) % n]]
            m = len(bads)
            for idx in range(m):
                p = bads[idx]
                q = bads[(idx + 1) % m]
                L = (q - p + n) % n
                add_run(L)

        def predecessor(e):
            cnt = self.badBIT.sum(e - 1)
            if cnt == 0:
                return self.badBIT.kth(self.B)   # last bad edge
            return self.badBIT.kth(cnt)

        def successor(e):
            cnt = self.badBIT.sum(e)
            if cnt == self.B:
                return self.badBIT.kth(1)       # first bad edge
            return self.badBIT.kth(cnt + 1)

        def edge_become_bad(e):
            if self.B == 0:
                self.badBIT.add(e, 1)
                self.B = 1
                add_run(self.n)
                return
            p = predecessor(e)   # previous bad edge (before insertion)
            q = successor(e)     # next bad edge (before insertion)
            if self.B == 1:
                L = self.n
            else:
                L = (q - p + self.n) % self.n
            L1 = (e - p + self.n) % self.n
            L2 = (q - e + self.n) % self.n
            remove_run(L)
            add_run(L1)
            add_run(L2)
            self.badBIT.add(e, 1)
            self.B += 1

        def edge_become_good(e):
            if self.B == 1:
                # removing the only bad edge -> all alternating
                remove_run(self.n)
                self.badBIT.add(e, -1)
                self.B = 0
                return
            # predecessor and successor while e is still present
            cnt_before = self.badBIT.sum(e - 1)
            if cnt_before == 0:
                p = self.badBIT.kth(self.B)   # last bad edge (wrap)
            else:
                p = self.badBIT.kth(cnt_before)

            cnt_up_to = self.badBIT.sum(e)
            if cnt_up_to == self.B:
                q = self.badBIT.kth(1)        # first bad edge
            else:
                q = self.badBIT.kth(cnt_up_to + 1)

            L1 = (e - p + self.n) % self.n
            L2 = (q - e + self.n) % self.n
            if self.B == 2:
                L = self.n
            else:
                L = (q - p + self.n) % self.n
            remove_run(L1)
            remove_run(L2)
            add_run(L)
            self.badBIT.add(e, -1)
            self.B -= 1

        ans = []
        for query in queries:
            if query[0] == 2:
                _, idx, col = query
                if colors[idx] != col:
                    affected = [(idx - 1) % n, idx]
                    old_status = {}
                    for e in affected:
                        a, b = e, (e + 1) % n
                        old_status[e] = (colors[a] == colors[b])
                    colors[idx] = col
                    for e in affected:
                        a, b = e, (e + 1) % n
                        new_bad = (colors[a] == colors[b])
                        if old_status[e] == new_bad:
                            continue
                        if not old_status[e] and new_bad:
                            edge_become_bad(e)
                        else:
                            edge_become_good(e)
            else:   # query type 1
                _, k = query
                if self.B == 0:
                    ans.append(self.n)
                else:
                    total_cnt = self.cntBIT.total()
                    cnt_lt_k = self.cntBIT.sum(k - 1) if k > 0 else 0
                    Ck = total_cnt - cnt_lt_k

                    total_len = self.lenBIT.total()
                    len_lt_k = self.lenBIT.sum(k - 1) if k > 0 else 0
                    Sk = total_len - len_lt_k

                    ans.append(Sk - (k - 1) * Ck)
        return ans
```

## C

```c
#include <stdlib.h>

typedef struct Node {
    int l, r;
    unsigned pri;
    struct Node *left, *right;
} Node;

static int N;                     // colors size
static int *diff;                 // diff array size N
static int zeroCount;             // number of zeros in diff
static int allOnesFlag;           // 1 if zeroCount == 0

// Fenwick trees
static long long *bitCnt, *bitSum;   // for lengths L (1..N)
static int *bitZero;                 // for zeros positions (1-indexed)

// ---------- Fenwick helpers ----------
static void bitAddCnt(int idx, int delta) {
    for (; idx <= N; idx += idx & -idx) bitCnt[idx] += delta;
}
static void bitAddSum(int idx, long long delta) {
    for (; idx <= N; idx += idx & -idx) bitSum[idx] += delta;
}
static void bitLenAdd(int L, int delta) {          // add/remove length contribution
    if (L <= 0) return;
    bitAddCnt(L, delta);
    bitAddSum(L, (long long)L * delta);
}
static long long bitQueryCnt(int idx) {
    long long res = 0;
    for (; idx > 0; idx -= idx & -idx) res += bitCnt[idx];
    return res;
}
static long long bitQuerySum(int idx) {
    long long res = 0;
    for (; idx > 0; idx -= idx & -idx) res += bitSum[idx];
    return res;
}
static void bitZeroAdd(int idx, int delta) {       // idx is 1-indexed
    for (; idx <= N; idx += idx & -idx) bitZero[idx] += delta;
}
static int bitZeroPrefix(int idx) {
    int res = 0;
    for (; idx > 0; idx -= idx & -idx) res += bitZero[idx];
    return res;
}
static int bitZeroTotal() { return bitZeroPrefix(N); }
static int findKthZero(int k) {                     // 1 <= k <= total zeros
    int idx = 0;
    int mask = 1;
    while ((mask << 1) <= N) mask <<= 1;
    for (int step = mask; step; step >>= 1) {
        int nxt = idx + step;
        if (nxt <= N && bitZero[nxt] < k) {
            k -= bitZero[nxt];
            idx = nxt;
        }
    }
    return idx + 1;   // 1-indexed position
}

// ---------- zero neighbor helpers ----------
static int getPrevZero(int pos) {   // pos is 0-indexed, assumes zeroCount>0
    int cntBefore = bitZeroPrefix(pos);          // zeros with index < pos
    if (cntBefore > 0)
        return findKthZero(cntBefore) - 1;
    else
        return findKthZero(zeroCount) - 1;      // wrap to last zero
}
static int getNextZero(int pos) {   // pos is 0-indexed, assumes zeroCount>0
    int cntUpTo = bitZeroPrefix(pos + 1);       // zeros with index <= pos
    if (cntUpTo < zeroCount)
        return findKthZero(cntUpTo + 1) - 1;
    else
        return findKthZero(1) - 1;               // wrap to first zero
}

// ---------- length handling ----------
static void addGap(int a, int b) {   // gap between zeros a and b (a -> b clockwise)
    int dist = (b - a - 1 + N) % N;
    if (dist > 0) bitLenAdd(dist + 1, +1);
}
static void removeGap(int a, int b) {
    int dist = (b - a - 1 + N) % N;
    if (dist > 0) bitLenAdd(dist + 1, -1);
}

// ---------- diff modification ----------
static void modifyDiff(int pos, int newVal) {   // pos: 0-indexed
    if (diff[pos] == newVal) return;
    int old = diff[pos];

    if (old == 0 && newVal == 1) {               // remove a zero
        // special case: this is the last zero
        if (zeroCount == 1) {
            // after removal, all ones
            bitZeroAdd(pos + 1, -1);
            zeroCount = 0;
            allOnesFlag = 1;
            diff[pos] = newVal;
            return;
        }
        int prev = getPrevZero(pos);
        int next = getNextZero(pos);

        removeGap(prev, pos);
        removeGap(pos, next);
        addGap(prev, next);

        bitZeroAdd(pos + 1, -1);
        zeroCount--;
        diff[pos] = newVal;
        if (zeroCount == 0) allOnesFlag = 1;
    } else {                                     // old==1 && newVal==0 : insert a zero
        if (zeroCount == 0) {
            // first zero in an all‑ones circle
            bitZeroAdd(pos + 1, +1);
            zeroCount = 1;
            allOnesFlag = 0;
            // the whole remaining part forms one gap of length N-1 -> L=N
            bitLenAdd(N, +1);
            diff[pos] = newVal;
            return;
        }
        int prev = getPrevZero(pos);
        int next = getNextZero(pos);

        removeGap(prev, next);
        addGap(prev, pos);
        addGap(pos, next);

        bitZeroAdd(pos + 1, +1);
        zeroCount++;
        diff[pos] = newVal;
        allOnesFlag = 0;
    }
}

// ---------- main solution ----------
int* numberOfAlternatingGroups(int* colors, int colorsSize, int** queries,
                               int queriesSize, int* queriesColSize, int* returnSize) {
    N = colorsSize;
    diff = (int*)malloc(N * sizeof(int));

    // allocate Fenwick trees
    bitCnt = (long long*)calloc(N + 2, sizeof(long long));
    bitSum = (long long*)calloc(N + 2, sizeof(long long));
    bitZero = (int*)calloc(N + 2, sizeof(int));

    // build diff array and zero set
    zeroCount = 0;
    for (int i = 0; i < N; ++i) {
        int nxt = (i + 1) % N;
        diff[i] = (colors[i] != colors[nxt]) ? 1 : 0;
        if (diff[i] == 0) {
            bitZeroAdd(i + 1, +1);
            zeroCount++;
        }
    }

    if (zeroCount == 0) {
        allOnesFlag = 1;
    } else {
        allOnesFlag = 0;
        // collect zeros in order
        int *zeros = (int*)malloc(zeroCount * sizeof(int));
        int idx = 0;
        for (int i = 0; i < N; ++i)
            if (diff[i] == 0) zeros[idx++] = i;
        for (int i = 0; i < zeroCount; ++i) {
            int a = zeros[i];
            int b = zeros[(i + 1) % zeroCount];
            addGap(a, b);
        }
        free(zeros);
    }

    // count type‑1 queries to allocate answer array
    int ansCap = 0;
    for (int i = 0; i < queriesSize; ++i)
        if (queries[i][0] == 1) ansCap++;
    int *answers = (int*)malloc(ansCap * sizeof(int));
    int ansIdx = 0;

    // process queries
    for (int qi = 0; qi < queriesSize; ++qi) {
        int type = queries[qi][0];
        if (type == 1) {                     // count query
            int k = queries[qi][1];
            long long res;
            if (allOnesFlag) {
                if (k > N) res = 0;
                else res = (long long)N - k + 1;
            } else {
                long long totalCnt = bitQueryCnt(N);
                long long totalSum = bitQuerySum(N);
                long long cntLe = (k - 1 >= 1) ? bitQueryCnt(k - 1) : 0;
                long long sumLe = (k - 1 >= 1) ? bitQuerySum(k - 1) : 0;
                long long cntGe = totalCnt - cntLe;
                long long sumGe = totalSum - sumLe;
                res = sumGe - (long long)(k - 1) * cntGe;
            }
            answers[ansIdx++] = (int)res;
        } else {                              // update query
            int idx = queries[qi][1];
            int newCol = queries[qi][2];
            if (colors[idx] == newCol) continue;
            colors[idx] = newCol;

            int leftPos = (idx - 1 + N) % N;
            int rightPos = idx;

            int newDiffLeft = (colors[leftPos] != newCol) ? 1 : 0;
            modifyDiff(leftPos, newDiffLeft);

            int newDiffRight = (newCol != colors[(idx + 1) % N]) ? 1 : 0;
            modifyDiff(rightPos, newDiffRight);
        }
    }

    *returnSize = ansIdx;
    // free auxiliary memory
    free(diff);
    free(bitCnt);
    free(bitSum);
    free(bitZero);
    return answers;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution
{
    private class Fenwick
    {
        private readonly long[] tree;
        private readonly int n;
        public Fenwick(int size)
        {
            n = size;
            tree = new long[n + 2];
        }
        public void Add(int idx, long delta)
        {
            for (int i = idx; i <= n; i += i & -i) tree[i] += delta;
        }
        public long Sum(int idx)
        {
            long res = 0;
            for (int i = idx; i > 0; i -= i & -i) res += tree[i];
            return res;
        }
    }

    private int n;
    private int[] diff;
    private SortedSet<int> zeros;
    private Fenwick bitCnt;
    private Fenwick bitSum;
    private long totalCnt;
    private long totalLen;

    private int Distance(int a, int b)
    {
        int d = b - a;
        if (d < 0) d += n;
        return d;
    }

    private void AddGap(int len)
    {
        if (len <= 0) return;
        totalCnt++;
        totalLen += len;
        bitCnt.Add(len, 1);
        bitSum.Add(len, len);
    }

    private void RemoveGap(int len)
    {
        if (len <= 0) return;
        totalCnt--;
        totalLen -= len;
        bitCnt.Add(len, -1);
        bitSum.Add(len, -len);
    }

    private int GetPrev(int x)
    {
        var view = zeros.GetViewBetween(int.MinValue, x - 1);
        if (view.Count == 0) return zeros.Max;
        return view.Max;
    }

    private int GetNext(int x)
    {
        var view = zeros.GetViewBetween(x + 1, int.MaxValue);
        if (view.Count == 0) return zeros.Min;
        return view.Min;
    }

    private void InsertZero(int pos)
    {
        if (zeros.Count == 0)
        {
            // remove whole-circle gap
            RemoveGap(n);
            AddGap(n - 1);
        }
        else
        {
            int prev = GetPrev(pos);
            int next = GetNext(pos);
            int oldLen = Distance(prev, next) - 1;
            if (oldLen > 0) RemoveGap(oldLen);

            int len1 = Distance(prev, pos) - 1;
            int len2 = Distance(pos, next) - 1;
            if (len1 > 0) AddGap(len1);
            if (len2 > 0) AddGap(len2);
        }
        zeros.Add(pos);
    }

    private void DeleteZero(int pos)
    {
        if (zeros.Count == 1)
        {
            // only this zero
            RemoveGap(n - 1);
            AddGap(n);
        }
        else
        {
            int prev = GetPrev(pos);
            int next = GetNext(pos);
            int len1 = Distance(prev, pos) - 1;
            int len2 = Distance(pos, next) - 1;
            if (len1 > 0) RemoveGap(len1);
            if (len2 > 0) RemoveGap(len2);

            int newLen = Distance(prev, next) - 1;
            if (newLen > 0) AddGap(newLen);
        }
        zeros.Remove(pos);
    }

    public IList<int> NumberOfAlternatingGroups(int[] colors, int[][] queries)
    {
        n = colors.Length;
        diff = new int[n];
        for (int i = 0; i < n; i++)
        {
            diff[i] = colors[i] == colors[(i + 1) % n] ? 0 : 1;
        }

        zeros = new SortedSet<int>();
        for (int i = 0; i < n; i++) if (diff[i] == 0) zeros.Add(i);

        bitCnt = new Fenwick(n);
        bitSum = new Fenwick(n);
        totalCnt = 0;
        totalLen = 0;

        if (zeros.Count == 0)
        {
            AddGap(n);
        }
        else
        {
            var arr = new int[zeros.Count];
            zeros.CopyTo(arr);
            int m = arr.Length;
            for (int i = 0; i < m; i++)
            {
                int a = arr[i];
                int b = arr[(i + 1) % m];
                int len = (b - a - 1 + n) % n;
                if (len > 0) AddGap(len);
            }
        }

        var result = new List<int>();
        foreach (var q in queries)
        {
            if (q[0] == 2)
            {
                int idx = q[1];
                int col = q[2];
                if (colors[idx] == col) continue;
                // update affected diffs
                int left = (idx - 1 + n) % n;
                int right = idx;

                // left diff
                int old = diff[left];
                int nw = colors[(left + 1) % n] != colors[left] ? 1 : 0; // after change, colors[left+1]=colors[idx]
                if (old != nw)
                {
                    if (nw == 0) InsertZero(left);
                    else DeleteZero(left);
                    diff[left] = nw;
                }

                // right diff
                old = diff[right];
                nw = colors[right] != colors[(right + 1) % n] ? 1 : 0; // after change, colors[right]=col
                if (old != nw)
                {
                    if (nw == 0) InsertZero(right);
                    else DeleteZero(right);
                    diff[right] = nw;
                }

                colors[idx] = col;
            }
            else // query type 1
            {
                int k = q[1];
                int t = k - 1; // required consecutive ones in diff
                if (t <= 0)
                {
                    result.Add(n);
                    continue;
                }
                long cntGe = totalCnt - bitCnt.Sum(t - 1);
                long lenGe = totalLen - bitSum.Sum(t - 1);
                long ans = lenGe - (long)(t - 1) * cntGe;
                result.Add((int)ans);
            }
        }

        return result;
    }
}
```

## Javascript

```javascript
/****
 * @param {number[]} colors
 * @param {number[][]} queries
 * @return {number[]}
 */
var numberOfAlternatingGroups = function(colors, queries) {
    const n = colors.length;

    // Fenwick Tree
    class Fenwick{
        constructor(n){
            this.n=n;
            this.bit=new Array(n+2).fill(0);
        }
        add(idx,val){
            for(let i=idx;i<=this.n;i+=i&-i) this.bit[i]+=val;
        }
        sum(idx){
            let s=0;
            for(let i=idx;i>0;i-=i&-i) s+=this.bit[i];
            return s;
        }
        rangeSum(l,r){
            if(l>r) return 0;
            return this.sum(r)-this.sum(l-1);
        }
    }

    const cntBIT = new Fenwick(n); // count of runs with given length
    const sumBIT = new Fenwick(n); // total lengths

    // Treap for zero positions
    class Node{
        constructor(key){
            this.key=key;
            this.pri=Math.random();
            this.left=null;
            this.right=null;
        }
    }
    let treapRoot=null;
    function rotateRight(y){
        const x=y.left;
        y.left=x.right;
        x.right=y;
        return x;
    }
    function rotateLeft(x){
        const y=x.right;
        x.right=y.left;
        y.left=x;
        return y;
    }
    function treapInsert(root,key){
        if(!root) return new Node(key);
        if(key<root.key){
            root.left=treapInsert(root.left,key);
            if(root.left.pri<root.pri) root=rotateRight(root);
        }else{
            root.right=treapInsert(root.right,key);
            if(root.right.pri<root.pri) root=rotateLeft(root);
        }
        return root;
    }
    function treapErase(root,key){
        if(!root) return null;
        if(key===root.key){
            // merge children
            if(!root.left) return root.right;
            if(!root.right) return root.left;
            if(root.left.pri<root.right.pri){
                root=rotateRight(root);
                root.right=treapErase(root.right,key);
            }else{
                root=rotateLeft(root);
                root.left=treapErase(root.left,key);
            }
        }else if(key<root.key){
            root.left=treapErase(root.left,key);
        }else{
            root.right=treapErase(root.right,key);
        }
        return root;
    }
    function findPrev(root,key){
        let cur=root, pred=null;
        while(cur){
            if(key>cur.key){
                pred=cur;
                cur=cur.right;
            }else{
                cur=cur.left;
            }
        }
        return pred?pred.key:null;
    }
    function findNext(root,key){
        let cur=root, succ=null;
        while(cur){
            if(key<cur.key){
                succ=cur;
                cur=cur.left;
            }else{
                cur=cur.right;
            }
        }
        return succ?succ.key:null;
    }
    function findMin(root){
        if(!root) return null;
        let cur=root;
        while(cur.left) cur=cur.left;
        return cur.key;
    }
    function findMax(root){
        if(!root) return null;
        let cur=root;
        while(cur.right) cur=cur.right;
        return cur.key;
    }

    // good array
    const good = new Array(n);
    for(let i=0;i<n;i++){
        const prev=(i-1+n)%n;
        good[i]= colors[i]!==colors[prev]?1:0;
        if(good[i]===0){
            treapRoot=treapInsert(treapRoot,i);
        }
    }
    let zeroCount = n - good.reduce((a,b)=>a+b,0);

    // initialize runs in BIT
    function addRun(len){
        if(len<=0) return;
        cntBIT.add(len,1);
        sumBIT.add(len,len);
    }
    function removeRun(len){
        if(len<=0) return;
        cntBIT.add(len,-1);
        sumBIT.add(len,-len);
    }
    if(zeroCount>0){
        // collect zeros in order
        const zeros=[];
        for(let i=0;i<n;i++) if(good[i]===0) zeros.push(i);
        const m=zeros.length;
        for(let i=0;i<m;i++){
            const cur=zeros[i];
            const nxt=zeros[(i+1)%m];
            const runLen = (nxt - cur - 1 + n)%n;
            addRun(runLen);
        }
    }

    // helper to get predecessor and successor with wrap
    function getPrev(p){
        let prev=findPrev(treapRoot,p);
        if(prev===null) prev=findMax(treapRoot);
        return prev;
    }
    function getNext(p){
        let nxt=findNext(treapRoot,p);
        if(nxt===null) nxt=findMin(treapRoot);
        return nxt;
    }

    // process change of good at position p from old to new
    function processChange(p,old,newVal){
        if(old===newVal) return;
        if(zeroCount===0){
            // currently all ones, so old must be 1 and new 0 (adding first zero)
            // add zero
            treapRoot=treapInsert(treapRoot,p);
            zeroCount=1;
            // remove whole run length n, add run length n-1
            removeRun(n);
            addRun(n-1);
            return;
        }
        if(old===0 && newVal===1){
            // remove a zero at p
            const prev=getPrev(p);
            const nxt=getNext(p);
            const left = (p - prev - 1 + n)%n;
            const right= (nxt - p - 1 + n)%n;
            if(left>0) removeRun(left);
            if(right>0) removeRun(right);
            treapRoot=treapErase(treapRoot,p);
            zeroCount--;
            if(zeroCount===0){
                // all ones now, no runs to add
                // clear any leftover (should be none)
            }else{
                const merged = left + 1 + right;
                addRun(merged);
            }
        }else if(old===1 && newVal===0){
            // add a zero at p
            const prev=getPrev(p);
            const nxt=getNext(p);
            const totalRun = (nxt - prev - 1 + n)%n;
            if(totalRun>0) removeRun(totalRun);
            const left = (p - prev - 1 + n)%n;
            const right= (nxt - p - 1 + n)%n;
            if(left>0) addRun(left);
            if(right>0) addRun(right);
            treapRoot=treapInsert(treapRoot,p);
            zeroCount++;
        }
    }

    // update good at position p after colors changed
    function recomputeGood(p){
        const prev=(p-1+n)%n;
        const newVal = colors[p]!==colors[prev]?1:0;
        if(good[p]!==newVal){
            processChange(p,good[p],newVal);
            good[p]=newVal;
        }
    }

    const ans=[];
    for(const q of queries){
        if(q[0]===1){
            const k=q[1];
            const L=k-1;
            if(L>n){ ans.push(0); continue; }
            if(zeroCount===0){
                ans.push(n);
            }else{
                const cntGe = cntBIT.rangeSum(L,n);
                if(cntGe===0){
                    ans.push(0);
                }else{
                    const sumGe = sumBIT.rangeSum(L,n);
                    const res = sumGe - (L-1)*cntGe;
                    ans.push(res);
                }
            }
        }else{ // type 2
            const idx=q[1];
            const col=q[2];
            if(colors[idx]===col) continue;
            colors[idx]=col;
            recomputeGood(idx);
            recomputeGood((idx+1)%n);
        }
    }
    return ans;
};
```

## Typescript

```typescript
function numberOfAlternatingGroups(colors: number[], queries: number[][]): number[] {
    const N = colors.length;

    // Edge bad array
    const edgeBad: boolean[] = new Array(N);
    for (let i = 0; i < N; ++i) {
        edgeBad[i] = colors[i] === colors[(i + 1) % N];
    }

    class BIT {
        n: number;
        tree: number[];
        constructor(n: number) {
            this.n = n;
            this.tree = new Array(n + 2).fill(0);
        }
        add(idx: number, delta: number): void {
            for (let i = idx; i <= this.n; i += i & -i) this.tree[i] += delta;
        }
        sum(idx: number): number {
            let res = 0;
            for (let i = idx; i > 0; i -= i & -i) res += this.tree[i];
            return res;
        }
    }

    const cntBIT = new BIT(N);
    const sumBIT = new BIT(N);

    function addLen(len: number, delta: number): void {
        if (len <= 0) return;
        cntBIT.add(len, delta);
        sumBIT.add(len, delta * len);
    }

    // Treap implementation
    class Node {
        key: number;
        prio: number;
        left: Node | null = null;
        right: Node | null = null;
        size: number = 1;
        constructor(key: number) {
            this.key = key;
            this.prio = Math.random();
        }
    }

    function upd(t: Node | null): void {
        if (t) t.size = 1 + (t.left?.size ?? 0) + (t.right?.size ?? 0);
    }

    function split(t: Node | null, key: number): [Node | null, Node | null] {
        if (!t) return [null, null];
        if (key <= t.key) {
            const [l, r] = split(t.left, key);
            t.left = r;
            upd(t);
            return [l, t];
        } else {
            const [l, r] = split(t.right, key);
            t.right = l;
            upd(t);
            return [t, r];
        }
    }

    function merge(a: Node | null, b: Node | null): Node | null {
        if (!a || !b) return a ? a : b;
        if (a.prio > b.prio) {
            a.right = merge(a.right, b);
            upd(a);
            return a;
        } else {
            b.left = merge(a, b.left);
            upd(b);
            return b;
        }
    }

    function insert(t: Node | null, key: number): Node {
        const [l, r] = split(t, key);
        const nd = new Node(key);
        return merge(merge(l, nd), r);
    }

    function erase(t: Node | null, key: number): Node | null {
        const [l, mid] = split(t, key);
        const [_mid, r] = split(mid, key + 1);
        // discard _mid
        return merge(l, r);
    }

    function getMin(t: Node | null): Node | null {
        while (t && t.left) t = t.left;
        return t;
    }
    function getMax(t: Node | null): Node | null {
        while (t && t.right) t = t.right;
        return t;
    }

    function findPrev(root: Node | null, key: number): number {
        let node = root;
        let pred: Node | null = null;
        while (node) {
            if (node.key < key) {
                pred = node;
                node = node.right;
            } else {
                node = node.left;
            }
        }
        if (pred) return pred.key;
        const mx = getMax(root);
        return mx ? mx.key : -1; // should not happen when set non‑empty
    }

    function findNext(root: Node | null, key: number): number {
        let node = root;
        let succ: Node | null = null;
        while (node) {
            if (node.key > key) {
                succ = node;
                node = node.left;
            } else {
                node = node.right;
            }
        }
        if (succ) return succ.key;
        const mn = getMin(root);
        return mn ? mn.key : -1;
    }

    function gapLen(a: number, b: number): number {
        let d = (b - a + N) % N;
        if (d === 0) d = N;
        return d;
    }

    // Initialize treap and BIT with initial bad edges
    let root: Node | null = null;
    let allAlt = true; // no bad edges
    const badPos: number[] = [];
    for (let i = 0; i < N; ++i) if (edgeBad[i]) badPos.push(i);
    if (badPos.length === 0) {
        allAlt = true;
    } else {
        allAlt = false;
        badPos.sort((a, b) => a - b);
        for (const p of badPos) root = insert(root, p);
        const m = badPos.length;
        for (let i = 0; i < m; ++i) {
            const cur = badPos[i];
            const nxt = badPos[(i + 1) % m];
            const len = gapLen(cur, nxt);
            addLen(len, 1);
        }
    }

    function handleInsert(p: number): void {
        if (allAlt) {
            // first bad edge
            root = insert(root, p);
            allAlt = false;
            addLen(N, 1); // whole circle as one gap
            return;
        }
        const prev = findPrev(root, p);
        const next = findNext(root, p);
        const oldGap = gapLen(prev, next);
        const g1 = gapLen(prev, p);
        const g2 = gapLen(p, next);
        addLen(oldGap, -1);
        addLen(g1, 1);
        addLen(g2, 1);
        root = insert(root, p);
    }

    function handleRemove(p: number): void {
        if (!root) return;
        const sz = root.size;
        if (sz === 1) {
            // removing the only bad edge
            addLen(N, -1);
            root = erase(root, p);
            allAlt = true;
            return;
        }
        const prev = findPrev(root, p);
        const next = findNext(root, p);
        const g1 = gapLen(prev, p);
        const g2 = gapLen(p, next);
        const newGap = gapLen(prev, next);
        addLen(g1, -1);
        addLen(g2, -1);
        addLen(newGap, 1);
        root = erase(root, p);
    }

    const ans: number[] = [];

    for (const q of queries) {
        if (q[0] === 1) {
            const k = q[1];
            let res: number;
            if (allAlt) {
                // every start works
                res = N;
            } else {
                if (k > N) {
                    res = 0;
                } else {
                    const cntGe = cntBIT.sum(N) - cntBIT.sum(k - 1);
                    const sumGe = sumBIT.sum(N) - sumBIT.sum(k - 1);
                    res = sumGe - (k - 1) * cntGe;
                }
            }
            ans.push(res);
        } else {
            const idx = q[1];
            const newCol = q[2];
            if (colors[idx] === newCol) continue;
            const affected = [(idx - 1 + N) % N, idx];
            const oldBadVals = affected.map(p => edgeBad[p]);
            // apply color change
            colors[idx] = newCol;
            for (let i = 0; i < affected.length; ++i) {
                const p = affected[i];
                const newBad = colors[p] === colors[(p + 1) % N];
                if (oldBadVals[i] === newBad) continue;
                edgeBad[p] = newBad;
                if (oldBadVals[i]) {
                    // was bad, now good
                    handleRemove(p);
                } else {
                    // was good, now bad
                    handleInsert(p);
                }
            }
        }
    }

    return ans;
}
```

## Php

```php
class Solution {
    private $n;
    private $colors = [];
    private $bad = [];          // 1 if colors[i]==colors[(i+1)%n]
    private $totalBadOnes = 0;  // sum of $bad
    private $root = null;       // treap root for zero runs
    private $bitCnt;            // BIT for counts of run lengths
    private $bitSum;            // BIT for sum of run lengths

    /** Node of treap */
    private class Node {
        public $key;   // start index
        public $len;   // length of zero run
        public $prio;
        public $left = null;
        public $right = null;
        function __construct($key, $len) {
            $this->key = $key;
            $this->len = $len;
            $this->prio = mt_rand();
        }
    }

    /** BIT (Fenwick) */
    private class BIT {
        public $n;
        public $tree;
        function __construct($n) {
            $this->n = $n;
            $this->tree = array_fill(0, $n + 2, 0);
        }
        function add($idx, $delta) {
            for ($i = $idx; $i <= $this->n; $i += $i & (-$i)) {
                $this->tree[$i] += $delta;
            }
        }
        function sum($idx) {
            $res = 0;
            for ($i = $idx; $i > 0; $i -= $i & (-$i)) {
                $res += $this->tree[$i];
            }
            return $res;
        }
        function rangeSum($l, $r) {
            if ($l > $r) return 0;
            return $this->sum($r) - $this->sum($l - 1);
        }
    }

    /** rotate right */
    private function rotateRight($y) {
        $x = $y->left;
        $y->left = $x->right;
        $x->right = $y;
        return $x;
    }

    /** rotate left */
    private function rotateLeft($x) {
        $y = $x->right;
        $x->right = $y->left;
        $y->left = $x;
        return $y;
    }

    /** insert node into treap */
    private function treapInsert($root, $node) {
        if ($root === null) return $node;
        if ($node->key < $root->key) {
            $root->left = $this->treapInsert($root->left, $node);
            if ($root->left->prio > $root->prio) {
                $root = $this->rotateRight($root);
            }
        } else {
            $root->right = $this->treapInsert($root->right, $node);
            if ($root->right->prio > $root->prio) {
                $root = $this->rotateLeft($root);
            }
        }
        return $root;
    }

    /** delete node with given key */
    private function treapDelete($root, $key) {
        if ($root === null) return null;
        if ($key < $root->key) {
            $root->left = $this->treapDelete($root->left, $key);
        } elseif ($key > $root->key) {
            $root->right = $this->treapDelete($root->right, $key);
        } else { // found
            if ($root->left === null) return $root->right;
            if ($root->right === null) return $root->left;
            if ($root->left->prio > $root->right->prio) {
                $root = $this->rotateRight($root);
                $root->right = $this->treapDelete($root->right, $key);
            } else {
                $root = $this->rotateLeft($root);
                $root->left = $this->treapDelete($root->left, $key);
            }
        }
        return $root;
    }

    /** find node with exact key */
    private function treapFindExact($root, $key) {
        while ($root !== null) {
            if ($key == $root->key) return $root;
            $root = ($key < $root->key) ? $root->left : $root->right;
        }
        return null;
    }

    /** find predecessor (max key <= given) */
    private function treapFindPrev($root, $key) {
        $res = null;
        while ($root !== null) {
            if ($root->key <= $key) {
                $res = $root;
                $root = $root->right;
            } else {
                $root = $root->left;
            }
        }
        return $res;
    }

    /** find node containing position pos */
    private function treapFindContaining($pos) {
        $node = $this->treapFindPrev($this->root, $pos);
        if ($node !== null && $pos < $node->key + $node->len) return $node;
        return null;
    }

    /** find minimum node (leftmost) */
    private function treapMin($root) {
        if ($root === null) return null;
        while ($root->left !== null) $root = $root->left;
        return $root;
    }

    /** find maximum node (rightmost) */
    private function treapMax($root) {
        if ($root === null) return null;
        while ($root->right !== null) $root = $root->right;
        return $root;
    }

    /** add a zero run of given start and length to structures */
    private function addRun($start, $len) {
        $node = new self::Node($start, $len);
        $this->root = $this->treapInsert($this->root, $node);
        $this->bitCnt->add($len, 1);
        $this->bitSum->add($len, $len);
    }

    /** remove a zero run node from structures */
    private function removeRunNode($node) {
        $this->root = $this->treapDelete($this->root, $node->key);
        $len = $node->len;
        $this->bitCnt->add($len, -1);
        $this->bitSum->add($len, -$len);
    }

    /** toggle bad[p] to newVal (0 or 1) */
    private function toggleBad($p, $newVal) {
        $old = $this->bad[$p];
        if ($old == $newVal) return;
        $this->bad[$p] = $newVal;
        if ($newVal == 1) { // remove zero at p
            $node = $this->treapFindContaining($p);
            if ($node === null) {
                // should not happen
                $this->totalBadOnes += 1;
                return;
            }
            $start = $node->key;
            $len   = $node->len;
            $leftLen  = $p - $start;
            $rightLen = $len - $leftLen - 1;

            $this->removeRunNode($node);
            if ($leftLen > 0) $this->addRun($start, $leftLen);
            if ($rightLen > 0) $this->addRun($p + 1, $rightLen);
        } else { // newVal == 0, add zero at p
            $n = $this->n;
            $leftZero  = $this->bad[($p - 1 + $n) % $n] == 0;
            $rightZero = $this->bad[($p + 1) % $n] == 0;

            if (!$leftZero && !$rightZero) {
                // isolated run length 1
                $this->addRun($p, 1);
            } elseif ($leftZero && !$rightZero) {
                // extend left run
                $node = $this->treapFindContaining(($p - 1 + $n) % $n);
                $oldLen = $node->len;
                $this->removeRunNode($node);
                $newLen = $oldLen + 1;
                $this->addRun($node->key, $newLen);
            } elseif (!$leftZero && $rightZero) {
                // extend right run (shift start left)
                $node = $this->treapFindContaining(($p + 1) % $n);
                $oldStart = $node->key;
                $oldLen   = $node->len;
                $this->removeRunNode($node);
                $newStart = $p;
                $newLen   = $oldLen + 1;
                $this->addRun($newStart, $newLen);
            } else { // both sides zero -> merge two runs and p
                $leftNode  = $this->treapFindContaining(($p - 1 + $n) % $n);
                $rightNode = $this->treapFindContaining(($p + 1) % $n);
                $lenL   = $leftNode->len;
                $lenR   = $rightNode->len;
                $startL = $leftNode->key;

                $this->removeRunNode($leftNode);
                $this->removeRunNode($rightNode);

                $newLen = $lenL + 1 + $lenR;
                $this->addRun($startL, $newLen);
            }
        }

        // update total bad count
        if ($newVal == 1) $this->totalBadOnes++; else $this->totalBadOnes--;
    }

    /** compute answer for query type 1 */
    private function countGroups($k) {
        if ($this->totalBadOnes == 0) return $this->n;
        $t = $k - 1; // needed consecutive zeros in bad array
        if ($t > $this->n) return 0;

        $cnt = $this->bitCnt->rangeSum($t, $this->n);
        $sum = $this->bitSum->rangeSum($t, $this->n);
        $base = $sum - ($t - 1) * $cnt;

        // correction for wrap (first run starting at 0 and last ending at n)
        $firstLen = 0;
        $lastLen  = 0;
        $minNode = $this->treapMin($this->root);
        if ($minNode !== null && $minNode->key == 0) $firstLen = $minNode->len;
        $maxNode = $this->treapMax($this->root);
        if ($maxNode !== null && $maxNode->key + $maxNode->len == $this->n) $lastLen = $maxNode->len;

        if ($firstLen > 0 && $lastLen > 0) {
            $combined = $firstLen + $lastLen;
            if ($combined >= $t) {
                $extra = $combined - $t + 1;
                $sub = 0;
                if ($firstLen >= $t) $sub += $firstLen - $t + 1;
                if ($lastLen  >= $t) $sub += $lastLen  - $t + 1;
                $extra -= $sub;
                $base += $extra;
            }
        }

        return $base;
    }

    /**
     * @param Integer[] $colors
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function numberOfAlternatingGroups($colors, $queries) {
        $this->n = count($colors);
        $this->colors = $colors;
        $this->bad = array_fill(0, $this->n, 0);
        $this->totalBadOnes = 0;

        for ($i = 0; $i < $this->n; $i++) {
            $next = ($i + 1) % $this->n;
            if ($colors[$i] == $colors[$next]) {
                $this->bad[$i] = 1;
                $this->totalBadOnes++;
            }
        }

        $this->bitCnt = new self::BIT($this->n);
        $this->bitSum = new self::BIT($this->n);

        // build zero runs
        $i = 0;
        while ($i < $this->n) {
            if ($this->bad[$i] == 1) { $i++; continue; }
            $start = $i;
            while ($i < $this->n && $this->bad[$i] == 0) $i++;
            $len = $i - $start;
            $this->addRun($start, $len);
        }

        $ans = [];
        foreach ($queries as $q) {
            if ($q[0] == 2) { // update
                $idx = $q[1];
                $col = $q[2];
                if ($this->colors[$idx] == $col) continue;
                $this->colors[$idx] = $col;

                $p1 = ($idx - 1 + $this->n) % $this->n;
                $newBad1 = ($this->colors[$p1] == $this->colors[($p1 + 1) % $this->n]) ? 1 : 0;
                $this->toggleBad($p1, $newBad1);

                $p2 = $idx;
                $newBad2 = ($this->colors[$p2] == $this->colors[($p2 + 1) % $this->n]) ? 1 : 0;
                $this->toggleBad($p2, $newBad2);
            } else { // query count
                $k = $q[1];
                $ans[] = $this->countGroups($k);
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func numberOfAlternatingGroups(_ colors: [Int], _ queries: [[Int]]) -> [Int] {
        let n = colors.count
        var col = colors
        var diff = [Int](repeating: 0, count: n)
        for i in 0..<n {
            diff[i] = (col[i] == col[(i + 1) % n]) ? 0 : 1
        }
        
        // Fenwick Tree for counts and sums of lengths of 1-blocks
        final class Fenwick {
            let size: Int
            var tree: [Int64]
            init(_ n: Int) {
                size = n
                tree = Array(repeating: 0, count: n + 2)
            }
            func add(_ idx: Int, _ delta: Int64) {
                var i = idx
                while i <= size {
                    tree[i] += delta
                    i += i & -i
                }
            }
            func sum(_ idx: Int) -> Int64 {
                var i = idx
                var res: Int64 = 0
                while i > 0 {
                    res += tree[i]
                    i -= i & -i
                }
                return res
            }
        }
        
        let bitCount = Fenwick(n)
        let bitSum = Fenwick(n)
        
        // Treap node
        final class Node {
            var key: Int          // start index
            var len: Int
            var val: Bool         // true if block of 1s
            var priority: UInt32
            var left: Node?
            var right: Node?
            init(key: Int, len: Int, val: Bool) {
                self.key = key
                self.len = len
                self.val = val
                self.priority = UInt32.random(in: 0...UInt32.max)
            }
        }
        
        // Helper to update BIT when inserting/removing a node of ones
        func bitUpdate(_ node: Node, _ delta: Int) {
            if node.val {
                let d = Int64(delta) * Int64(node.len)
                bitCount.add(node.len, Int64(delta))
                bitSum.add(node.len, d)
            }
        }
        
        // Treap operations
        func split(_ root: Node?, _ key: Int) -> (Node?, Node?) {
            guard let r = root else { return (nil, nil) }
            if r.key < key {
                let (l, rr) = split(r.right, key)
                r.right = l
                return (r, rr)
            } else {
                let (ll, r2) = split(r.left, key)
                r.left = r2
                return (ll, r)
            }
        }
        
        func merge(_ a: Node?, _ b: Node?) -> Node? {
            if a == nil { return b }
            if b == nil { return a }
            if a!.priority < b!.priority {
                a!.right = merge(a!.right, b)
                return a
            } else {
                b!.left = merge(a, b!.left)
                return b
            }
        }
        
        func insertNode(_ root: Node?, _ node: Node) -> Node? {
            if let r = root {
                if node.priority < r.priority {
                    let (l, rr) = split(r, node.key)
                    node.left = l
                    node.right = rr
                    bitUpdate(node, 1)
                    return node
                } else if node.key < r.key {
                    r.left = insertNode(r.left, node)
                    return r
                } else {
                    r.right = insertNode(r.right, node)
                    return r
                }
            } else {
                bitUpdate(node, 1)
                return node
            }
        }
        
        func erase(_ root: Node?, _ key: Int) -> Node? {
            guard let r = root else { return nil }
            if key == r.key {
                bitUpdate(r, -1)
                return merge(r.left, r.right)
            } else if key < r.key {
                r.left = erase(r.left, key)
                return r
            } else {
                r.right = erase(r.right, key)
                return r
            }
        }
        
        func predecessor(_ root: Node?, _ pos: Int) -> Node? {
            var cur = root
            var pred: Node? = nil
            while let c = cur {
                if pos >= c.key {
                    pred = c
                    cur = c.right
                } else {
                    cur = c.left
                }
            }
            return pred
        }
        
        func findNode(_ root: Node?, _ key: Int) -> Node? {
            var cur = root
            while let c = cur {
                if key == c.key { return c }
                if key < c.key { cur = c.left } else { cur = c.right }
            }
            return nil
        }
        
        func getLast(_ root: Node?) -> Node? {
            var cur = root
            var last: Node? = nil
            while let c = cur {
                last = c
                cur = c.right
            }
            return last
        }
        
        // Build initial blocks
        var root: Node? = nil
        var i = 0
        while i < n {
            let start = i
            let v = diff[i] == 1
            var j = i
            while j + 1 < n && diff[j + 1] == diff[i] { j += 1 }
            let len = j - start + 1
            let node = Node(key: start, len: len, val: v)
            root = insertNode(root, node)
            i = j + 1
        }
        
        // Flip function for a single diff index
        func flip(at idx: Int, to newVal: Int) {
            let old = diff[idx]
            if old == newVal { return }
            diff[idx] = newVal
            guard let curNode = predecessor(root, idx) else { return }
            // remove current block
            root = erase(root, curNode.key)
            let start = curNode.key
            let len = curNode.len
            let val = curNode.val
            let leftLen = idx - start
            let rightLen = start + len - 1 - idx
            if leftLen > 0 {
                let leftNode = Node(key: start, len: leftLen, val: val)
                root = insertNode(root, leftNode)
            }
            if rightLen > 0 {
                let rightNode = Node(key: idx + 1, len: rightLen, val: val)
                root = insertNode(root, rightNode)
            }
            // create/merge new 1 block at idx
            var newStart = idx
            var newLen = 1
            if idx != 0 {
                if let leftNeighbor = predecessor(root, idx - 1), leftNeighbor.val {
                    root = erase(root, leftNeighbor.key)
                    newStart = leftNeighbor.key
                    newLen += leftNeighbor.len
                }
            }
            if idx != n - 1 {
                if let rightNeighbor = predecessor(root, idx + 1), rightNeighbor.val && rightNeighbor.key == idx + 1 {
                    root = erase(root, rightNeighbor.key)
                    newLen += rightNeighbor.len
                }
            }
            let newNode = Node(key: newStart, len: newLen, val: true)
            root = insertNode(root, newNode)
        }
        
        var answers: [Int] = []
        for q in queries {
            if q[0] == 2 {
                let pos = q[1]
                let newColor = q[2]
                if col[pos] == newColor { continue }
                col[pos] = newColor
                let leftIdx = (pos - 1 + n) % n
                let rightIdx = pos
                let newLeft = (col[leftIdx] == col[(leftIdx + 1) % n]) ? 0 : 1
                flip(at: leftIdx, to: newLeft)
                let newRight = (col[rightIdx] == col[(rightIdx + 1) % n]) ? 0 : 1
                flip(at: rightIdx, to: newRight)
            } else { // query type 1
                let k = q[1]
                let w = k - 1
                if w == 0 {
                    answers.append(n)
                    continue
                }
                let totalCnt = bitCount.sum(n)
                let totalSum = bitSum.sum(n)
                let prefCnt = w > 1 ? bitCount.sum(w - 1) : 0
                let prefSum = w > 1 ? bitSum.sum(w - 1) : 0
                let cntGE = totalCnt - prefCnt
                let sumGE = totalSum - prefSum
                var ans = sumGE - Int64(w - 1) * cntGE
                // circular adjustment
                if let firstNode = findNode(root, 0), let lastNode = getLast(root), firstNode.val && lastNode.val {
                    let Lfirst = firstNode.len
                    let Llast = lastNode.len
                    let combined = Lfirst + Llast
                    let contribCombined = max(0, combined - w + 1)
                    let contribSeparate = max(0, Lfirst - w + 1) + max(0, Llast - w + 1)
                    ans += Int64(contribCombined - contribSeparate)
                }
                answers.append(Int(ans))
            }
        }
        return answers
    }
}
```

## Kotlin

```kotlin
import java.util.TreeMap
import java.util.Map

class Fenwick(private val n: Int) {
    private val bit = LongArray(n + 2)
    fun add(idx0: Int, delta: Long) {
        var idx = idx0
        var d = delta
        while (idx <= n) {
            bit[idx] += d
            idx += idx and -idx
        }
    }

    fun sum(idx0: Int): Long {
        var idx = idx0
        var res = 0L
        while (idx > 0) {
            res += bit[idx]
            idx -= idx and -idx
        }
        return res
    }

    fun rangeSum(l: Int, r: Int): Long {
        if (r < l) return 0L
        return sum(r) - sum(l - 1)
    }
}

class Solution {
    private lateinit var colors: IntArray
    private lateinit var good: IntArray
    private val runs = TreeMap<Int, Int>()
    private lateinit var freqBIT: Fenwick
    private lateinit var sumBIT: Fenwick
    private var n = 0

    private fun addRun(start: Int, len: Int) {
        if (len <= 0) return
        runs[start] = len
        freqBIT.add(len, 1)
        sumBIT.add(len, len.toLong())
    }

    private fun removeRun(start: Int) {
        val len = runs.remove(start) ?: return
        freqBIT.add(len, -1)
        sumBIT.add(len, -len.toLong())
    }

    private fun setGood(pos: Int, newVal: Int) {
        if (good[pos] == newVal) return
        if (newVal == 1) {
            // merging possible
            val leftIdx = (pos - 1 + n) % n
            var leftStart = -1
            var leftLen = 0
            if (good[leftIdx] == 1) {
                val entry = runs.floorEntry(leftIdx)!!
                leftStart = entry.key
                leftLen = entry.value
            }
            val rightIdx = (pos + 1) % n
            var rightStart = -1
            var rightLen = 0
            if (good[rightIdx] == 1) {
                val entry = runs.floorEntry(rightIdx)!!
                rightStart = entry.key
                rightLen = entry.value
            }
            when {
                leftLen > 0 && rightLen > 0 && leftStart != rightStart -> {
                    removeRun(leftStart)
                    removeRun(rightStart)
                    addRun(leftStart, leftLen + 1 + rightLen)
                }
                leftLen > 0 -> {
                    removeRun(leftStart)
                    addRun(leftStart, leftLen + 1)
                }
                rightLen > 0 -> {
                    removeRun(rightStart)
                    addRun(pos, rightLen + 1)
                }
                else -> {
                    addRun(pos, 1)
                }
            }
        } else { // newVal == 0
            val entry = runs.floorEntry(pos) ?: return
            val start = entry.key
            val len = entry.value
            if (pos < start || pos >= start + len) return // should not happen
            removeRun(start)
            val leftLen = pos - start
            if (leftLen > 0) addRun(start, leftLen)
            val rightLen = (start + len - 1) - pos
            if (rightLen > 0) addRun(pos + 1, rightLen)
        }
        good[pos] = newVal
    }

    private fun applyUpdate(p: Int, v: Int) {
        if (colors[p] == v) return
        colors[p] = v
        val leftIdx = (p - 1 + n) % n
        val newLeft = if (colors[(p - 1 + n) % n] != colors[p]) 1 else 0
        setGood(leftIdx, newLeft)
        val rightIdx = p
        val newRight = if (colors[p] != colors[(p + 1) % n]) 1 else 0
        setGood(rightIdx, newRight)
    }

    private fun countGroups(k: Int): Int {
        val L = k - 1
        var cnt = freqBIT.rangeSum(L, n)
        var sumLen = sumBIT.rangeSum(L, n)
        var ans = sumLen - (L - 1).toLong() * cnt

        if (good[n - 1] == 1) {
            val firstEntry: Map.Entry<Int, Int>? = runs.firstEntry()
            val lastEntry: Map.Entry<Int, Int>? = runs.lastEntry()
            if (firstEntry != null && firstEntry.key == 0 &&
                lastEntry != null && lastEntry.key + lastEntry.value == n &&
                firstEntry.key != lastEntry.key) {
                val preLen = firstEntry.value
                val sufLen = lastEntry.value
                fun contrib(len: Int): Long =
                    if (len >= L) (len - (L - 1)).toLong() else 0L
                ans -= contrib(preLen)
                ans -= contrib(sufLen)
                ans += contrib(preLen + sufLen)
            }
        }
        return ans.toInt()
    }

    fun numberOfAlternatingGroups(colorsInput: IntArray, queries: Array<IntArray>): List<Int> {
        colors = colorsInput.clone()
        n = colors.size
        good = IntArray(n)
        for (i in 0 until n) {
            good[i] = if (colors[i] != colors[(i + 1) % n]) 1 else 0
        }
        freqBIT = Fenwick(n)
        sumBIT = Fenwick(n)

        var i = 0
        while (i < n) {
            if (good[i] == 1) {
                val start = i
                while (i + 1 < n && good[i + 1] == 1) i++
                val len = i - start + 1
                addRun(start, len)
            }
            i++
        }

        val answer = ArrayList<Int>()
        for (q in queries) {
            if (q[0] == 1) {
                // count query
                answer.add(countGroups(q[1]))
            } else {
                // update query
                applyUpdate(q[1], q[2])
            }
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  List<int> numberOfAlternatingGroups(List<int> colors, List<List<int>> queries) {
    int n = colors.length;
    // diff[i] = 1 if colors[i] != colors[(i+1)%n]
    List<int> diff = List.filled(n, 0);
    for (int i = 0; i < n; ++i) {
      diff[i] = colors[i] == colors[(i + 1) % n] ? 0 : 1;
    }

    // Fenwick Trees
    class BIT {
      final List<int> tree;
      final int size;
      BIT(this.size) : tree = List.filled(size + 2, 0);
      void add(int idx, int delta) {
        for (int i = idx; i <= size; i += i & -i) {
          tree[i] += delta;
        }
      }

      int sum(int idx) {
        int res = 0;
        for (int i = idx; i > 0; i -= i & -i) {
          res += tree[i];
        }
        return res;
      }
    }

    BIT bitCnt = BIT(n);
    BIT bitSum = BIT(n); // stores cnt * (len + 2)

    // Treap for runs of ones in diff
    class Node {
      int key; // start index
      int len; // run length
      int prio;
      Node? left, right;
      Node(this.key, this.len) : prio = _rand.nextInt(1 << 30);
    }

    final _rand = Random();

    Node? root;

    Node _rotateRight(Node y) {
      Node x = y.left!;
      y.left = x.right;
      x.right = y;
      return x;
    }

    Node _rotateLeft(Node x) {
      Node y = x.right!;
      x.right = y.left;
      y.left = x;
      return y;
    }

    Node _insert(Node? node, int key, int len) {
      if (node == null) return Node(key, len);
      if (key < node.key) {
        node.left = _insert(node.left, key, len);
        if (node.left!.prio > node.prio) node = _rotateRight(node);
      } else {
        node.right = _insert(node.right, key, len);
        if (node.right!.prio > node.prio) node = _rotateLeft(node);
      }
      return node;
    }

    Node? _merge(Node? a, Node? b) {
      if (a == null) return b;
      if (b == null) return a;
      if (a.prio > b.prio) {
        a.right = _merge(a.right, b);
        return a;
      } else {
        b.left = _merge(a, b.left);
        return b;
      }
    }

    Node? _erase(Node? node, int key) {
      if (node == null) return null;
      if (key < node.key) {
        node.left = _erase(node.left, key);
        return node;
      } else if (key > node.key) {
        node.right = _erase(node.right, key);
        return node;
      } else {
        return _merge(node.left, node.right);
      }
    }

    Node? _find(Node? node, int key) {
      while (node != null) {
        if (key == node.key) return node;
        if (key < node.key) node = node.left;
        else node = node.right;
      }
      return null;
    }

    Node? _predecessor(int key) {
      Node? cur = root;
      Node? pred;
      while (cur != null) {
        if (cur.key <= key) {
          pred = cur;
          cur = cur.right;
        } else {
          cur = cur.left;
        }
      }
      return pred;
    }

    // initialize runs from diff
    int i = 0;
    while (i < n) {
      if (diff[i] == 1) {
        int start = i;
        while (i < n && diff[i] == 1) i++;
        int len = i - start;
        root = _insert(root, start, len);
        bitCnt.add(len, 1);
        bitSum.add(len, len + 2);
      } else {
        i++;
      }
    }

    void _addRun(int start, int len) {
      if (len <= 0) return;
      root = _insert(root, start, len);
      bitCnt.add(len, 1);
      bitSum.add(len, len + 2);
    }

    void _removeRun(Node node) {
      root = _erase(root, node.key);
      bitCnt.add(node.len, -1);
      bitSum.add(node.len, -(node.len + 2));
    }

    void _setDiff(int p, int newVal) {
      if (diff[p] == newVal) return;
      if (newVal == 1) {
        // merge possible left and right runs
        Node? leftNode;
        Node? pred = _predecessor(p - 1);
        if (pred != null && pred.key + pred.len == p) leftNode = pred;

        Node? rightNode = _find(root, p + 1);

        int newStart = leftNode?.key ?? p;
        int newLen = (leftNode?.len ?? 0) + (rightNode?.len ?? 0) + 1;

        if (leftNode != null) _removeRun(leftNode);
        if (rightNode != null) _removeRun(rightNode);

        _addRun(newStart, newLen);
      } else {
        // split existing run containing p
        Node? cur = _predecessor(p);
        if (cur == null || !(cur.key <= p && p < cur.key + cur.len)) {
          diff[p] = newVal;
          return;
        }
        int start = cur.key;
        int len = cur.len;
        _removeRun(cur);

        // left part
        if (p > start) {
          _addRun(start, p - start);
        }
        // right part
        if (p < start + len - 1) {
          _addRun(p + 1, start + len - (p + 1));
        }
      }
      diff[p] = newVal;
    }

    List<int> answer = [];

    for (List<int> q in queries) {
      if (q[0] == 2) {
        int idx = q[1];
        int col = q[2];
        if (colors[idx] == col) continue;
        colors[idx] = col;
        int p1 = (idx - 1 + n) % n;
        int p2 = idx;
        int newVal1 = colors[p1] == colors[(p1 + 1) % n] ? 0 : 1;
        int newVal2 = colors[p2] == colors[(p2 + 1) % n] ? 0 : 1;
        _setDiff(p1, newVal1);
        _setDiff(p2, newVal2);
      } else {
        int k = q[1];
        int t = k - 2;
        if (t < 0) t = 0;
        int totalCnt = bitCnt.sum(n) - (t > 0 ? bitCnt.sum(t - 1) : 0);
        int totalSum = bitSum.sum(n) - (t > 0 ? bitSum.sum(t - 1) : 0);
        int ans = totalSum - k * totalCnt;

        // adjustment for circular merge of first and last runs
        Node? firstNode = _find(root, 0);
        int firstLen = firstNode?.len ?? 0;
        Node? predLast = _predecessor(n - 1);
        int lastLen = 0;
        if (predLast != null && predLast.key + predLast.len == n) {
          lastLen = predLast.len;
        }

        bool needAdjust = false;
        // check if first and last are distinct runs
        if (firstLen > 0 && lastLen > 0) {
          if (!(firstNode != null && firstNode.key == 0 && firstNode.len == n)) {
            needAdjust = true;
          }
        }

        if (needAdjust) {
          int mergedLen = firstLen + lastLen;
          int contribMerged = mergedLen - k + 2;
          if (contribMerged < 0) contribMerged = 0;
          int contribFirst = firstLen - k + 2;
          if (contribFirst < 0) contribFirst = 0;
          int contribLast = lastLen - k + 2;
          if (contribLast < 0) contribLast = 0;
          ans += (contribMerged - contribFirst - contribLast);
        }

        answer.add(ans);
      }
    }

    return answer;
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

type BIT struct {
	n    int
	tree []int64
}

func newBIT(n int) *BIT {
	b := &BIT{n: n, tree: make([]int64, n+2)}
	return b
}
func (b *BIT) add(idx int, delta int64) {
	for i := idx + 1; i <= b.n; i += i & -i {
		b.tree[i] += delta
	}
}
func (b *BIT) sum(idx int) int64 {
	if idx < 0 {
		return 0
	}
	var res int64
	for i := idx + 1; i > 0; i -= i & -i {
		res += b.tree[i]
	}
	return res
}

type Node struct {
	key        int
	end        int
	pr         uint32
	left, right *Node
}

func rotateRight(y *Node) *Node {
	x := y.left
	y.left = x.right
	x.right = y
	return x
}
func rotateLeft(x *Node) *Node {
	y := x.right
	x.right = y.left
	y.left = x
	return y
}
func mergeTrees(a, b *Node) *Node {
	if a == nil {
		return b
	}
	if b == nil {
		return a
	}
	if a.pr < b.pr {
		a.right = mergeTrees(a.right, b)
		return a
	}
	b.left = mergeTrees(a, b.left)
	return b
}
func treapInsert(root, node *Node) *Node {
	if root == nil {
		return node
	}
	if node.key < root.key {
		root.left = treapInsert(root.left, node)
		if root.left.pr < root.pr {
			root = rotateRight(root)
		}
	} else {
		root.right = treapInsert(root.right, node)
		if root.right.pr < root.pr {
			root = rotateLeft(root)
		}
	}
	return root
}
func treapDelete(root *Node, key int) *Node {
	if root == nil {
		return nil
	}
	if key < root.key {
		root.left = treapDelete(root.left, key)
	} else if key > root.key {
		root.right = treapDelete(root.right, key)
	} else {
		return mergeTrees(root.left, root.right)
	}
	return root
}
func treapPrev(root *Node, key int) *Node {
	var res *Node
	for root != nil {
		if root.key <= key {
			res = root
			root = root.right
		} else {
			root = root.left
		}
	}
	return res
}

type Solver struct {
	n        int
	colors   []int
	diff     []int
	root     *Node
	mapStart map[int]int // start -> length
	mapEnd   map[int]int // end -> length
	bitCnt   *BIT
	bitSum   *BIT
}

func newSolver(colors []int) *Solver {
	s := &Solver{
		n:        len(colors),
		colors:   make([]int, len(colors)),
		diff:     make([]int, len(colors)),
		root:     nil,
		mapStart: make(map[int]int),
		mapEnd:   make(map[int]int),
		bitCnt:   newBIT(len(colors) + 2),
		bitSum:   newBIT(len(colors) + 2),
	}
	copy(s.colors, colors)
	n := s.n
	for i := 0; i < n; i++ {
		if s.colors[i] != s.colors[(i+1)%n] {
			s.diff[i] = 1
		} else {
			s.diff[i] = 0
		}
	}
	// build runs
	i := 0
	for i < n {
		if s.diff[i] == 1 {
			j := i
			for j+1 < n && s.diff[j+1] == 1 {
				j++
			}
			start := i
			length := j - i + 1
			s.insertRun(start, length)
			i = j + 1
		} else {
			i++
		}
	}
	return s
}

func (s *Solver) insertRun(start, length int) {
	end := start + length - 1
	node := &Node{key: start, end: end, pr: rand.Uint32()}
	s.root = treapInsert(s.root, node)
	s.mapStart[start] = length
	s.mapEnd[end] = length
	s.bitCnt.add(length, 1)
	s.bitSum.add(length, int64(length))
}

func (s *Solver) removeRun(start, length int) {
	end := start + length - 1
	s.root = treapDelete(s.root, start)
	delete(s.mapStart, start)
	delete(s.mapEnd, end)
	s.bitCnt.add(length, -1)
	s.bitSum.add(length, -int64(length))
}

func (s *Solver) getStartContaining(pos int) int {
	node := treapPrev(s.root, pos)
	if node != nil && node.end >= pos {
		return node.key
	}
	return -1 // should not happen
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func (s *Solver) query(k int) int {
	L := k - 1 // length in diff array
	totalCnt := s.bitCnt.sum(s.n)
	totalSum := s.bitSum.sum(s.n)

	var cntGe, sumGe int64
	prefixIdx := L - 2
	if prefixIdx >= 0 {
		cntGe = totalCnt - s.bitCnt.sum(prefixIdx)
		sumGe = totalSum - s.bitSum.sum(prefixIdx)
	} else {
		cntGe = totalCnt
		sumGe = totalSum
	}
	ans := sumGe - int64(L-1)*cntGe

	if s.diff[0] == 1 && s.diff[s.n-1] == 1 {
		firstLen, ok1 := s.mapStart[0]
		if !ok1 {
			firstLen = 0
		}
		lastLen, ok2 := s.mapEnd[s.n-1]
		if !ok2 {
			lastLen = 0
		}
		W := firstLen + lastLen
		cross := max(0, W-L+1) - max(0, firstLen-L+1) - max(0, lastLen-L+1)
		ans += int64(cross)
	}
	return int(ans)
}

func (s *Solver) update(idx, col int) {
	if s.colors[idx] == col {
		return
	}
	s.colors[idx] = col
	n := s.n
	posList := []int{(idx - 1 + n) % n, idx}
	for _, p := range posList {
		old := s.diff[p]
		newVal := 0
		if s.colors[p] != s.colors[(p+1)%n] {
			newVal = 1
		}
		if old == newVal {
			continue
		}
		if old == 0 && newVal == 1 {
			// turn on
			leftIdx := (p - 1 + n) % n
			rightIdx := (p + 1) % n
			leftAdj := s.diff[leftIdx] == 1
			rightAdj := s.diff[rightIdx] == 1
			if !leftAdj && !rightAdj {
				s.insertRun(p, 1)
			} else if leftAdj && !rightAdj {
				startL := s.getStartContaining(leftIdx)
				lenL := s.mapStart[startL]
				s.removeRun(startL, lenL)
				s.insertRun(startL, lenL+1)
			} else if !leftAdj && rightAdj {
				startR := s.getStartContaining(rightIdx)
				lenR := s.mapStart[startR]
				s.removeRun(startR, lenR)
				s.insertRun(p, lenR+1)
			} else { // both adjacent
				startL := s.getStartContaining(leftIdx)
				lenL := s.mapStart[startL]
				startR := s.getStartContaining(rightIdx)
				lenR := s.mapStart[startR]
				s.removeRun(startL, lenL)
				s.removeRun(startR, lenR)
				s.insertRun(startL, lenL+1+lenR)
			}
		} else if old == 1 && newVal == 0 {
			// turn off
			start := s.getStartContaining(p)
			lenRun := s.mapStart[start]
			if lenRun == 1 {
				s.removeRun(start, 1)
			} else if p == start {
				s.removeRun(start, lenRun)
				s.insertRun(start+1, lenRun-1)
			} else if p == start+lenRun-1 {
				s.removeRun(start, lenRun)
				s.insertRun(start, lenRun-1)
			} else {
				leftLen := p - start
				rightLen := start + lenRun - 1 - p
				s.removeRun(start, lenRun)
				s.insertRun(start, leftLen)
				s.insertRun(p+1, rightLen)
			}
		}
		s.diff[p] = newVal
	}
}

func numberOfAlternatingGroups(colors []int, queries [][]int) []int {
	rand.Seed(time.Now().UnixNano())
	solver := newSolver(colors)
	ans := make([]int, 0, len(queries))
	for _, q := range queries {
		if q[0] == 1 {
			k := q[1]
			ans = append(ans, solver.query(k))
		} else {
			idx := q[1]
			col := q[2]
			solver.update(idx, col)
		}
	}
	return ans
}
```

## Ruby

```ruby
class Fenwick
  def initialize(n)
    @n = n
    @bit = Array.new(n + 2, 0)
  end

  def add(idx, delta)
    i = idx + 1
    while i <= @n + 1
      @bit[i] += delta
      i += i & -i
    end
  end

  def sum(idx)
    res = 0
    i = idx + 1
    while i > 0
      res += @bit[i]
      i -= i & -i
    end
    res
  end

  def range_sum(l, r)
    return 0 if l > r
    sum(r) - (l == 0 ? 0 : sum(l - 1))
  end
end

class SegTree
  INF = (1 << 60)

  def initialize(arr)
    @n = arr.size
    @size = 1
    @size <<= 1 while @size < @n
    @left = Array.new(@size * 2, INF)
    @right = Array.new(@size * 2, -1)
    (0...@n).each do |i|
      if arr[i] == 0
        @left[@size + i] = i
        @right[@size + i] = i
      end
    end
    (@size - 1).downto(1) do |i|
      @left[i] = [@left[i * 2], @left[i * 2 + 1]].min
      @right[i] = [@right[i * 2], @right[i * 2 + 1]].max
    end
  end

  def update(pos, val)
    i = @size + pos
    if val == 0
      @left[i] = pos
      @right[i] = pos
    else
      @left[i] = INF
      @right[i] = -1
    end
    i >>= 1
    while i > 0
      @left[i] = [@left[i * 2], @left[i * 2 + 1]].min
      @right[i] = [@right[i * 2], @right[i * 2 + 1]].max
      i >>= 1
    end
  end

  def query_leftmost(l, r, node = 1, nl = 0, nr = nil)
    nr = @size - 1 if nr.nil?
    return INF if l > r || r < nl || nr < l
    if l <= nl && nr <= r
      return @left[node]
    end
    mid = (nl + nr) >> 1
    left_res = query_leftmost(l, r, node * 2, nl, mid)
    right_res = query_leftmost(l, r, node * 2 + 1, mid + 1, nr)
    left_res < right_res ? left_res : right_res
  end

  def query_rightmost(l, r, node = 1, nl = 0, nr = nil)
    nr = @size - 1 if nr.nil?
    return -1 if l > r || r < nl || nr < l
    if l <= nl && nr <= r
      return @right[node]
    end
    mid = (nl + nr) >> 1
    right_res = query_rightmost(l, r, node * 2 + 1, mid + 1, nr)
    left_res = query_rightmost(l, r, node * 2, nl, mid)
    right_res > left_res ? right_res : left_res
  end

  def any_zero?(l, r)
    return false if l > r
    query_leftmost(l, r) != INF
  end
end

def add_run(len, cnt_fen, sum_fen)
  cnt_fen.add(len, 1)
  sum_fen.add(len, len)
end

def remove_run(len, cnt_fen, sum_fen)
  cnt_fen.add(len, -1)
  sum_fen.add(len, -len)
end

def process_edge_change(pos, old_val, new_val, seg, zero_cnt_ref, cnt_fen, sum_fen, n)
  if old_val == 0 && new_val == 1
    # remove a zero
    zero_cnt_ref[0] -= 1
    if zero_cnt_ref[0] == 0
      # only this zero existed before removal
      remove_run(n - 1, cnt_fen, sum_fen) if n > 1
      add_run(n, cnt_fen, sum_fen)
    else
      prev = seg.query_rightmost(0, pos - 1)
      prev = seg.query_rightmost(pos + 1, n - 1) if prev == -1
      nxt = seg.query_leftmost(pos + 1, n - 1)
      nxt = seg.query_leftmost(0, pos - 1) if nxt == SegTree::INF
      len1 = (pos - prev - 1) % n
      len2 = (nxt - pos - 1) % n
      remove_run(len1, cnt_fen, sum_fen) if len1 > 0
      remove_run(len2, cnt_fen, sum_fen) if len2 > 0
      merged = len1 + 1 + len2
      add_run(merged, cnt_fen, sum_fen) if merged > 0
    end
    seg.update(pos, 1)
  elsif old_val == 1 && new_val == 0
    # add a zero
    zero_cnt_ref[0] += 1
    if zero_cnt_ref[0] == 1
      remove_run(n, cnt_fen, sum_fen)
      add_run(n - 1, cnt_fen, sum_fen) if n > 1
    else
      prev = seg.query_rightmost(0, pos - 1)
      prev = seg.query_rightmost(pos + 1, n - 1) if prev == -1
      nxt = seg.query_leftmost(pos + 1, n - 1)
      nxt = seg.query_leftmost(0, pos - 1) if nxt == SegTree::INF
      whole = (nxt - prev - 1) % n
      remove_run(whole, cnt_fen, sum_fen) if whole > 0
      left_len = (pos - prev - 1) % n
      right_len = (nxt - pos - 1) % n
      add_run(left_len, cnt_fen, sum_fen) if left_len > 0
      add_run(right_len, cnt_fen, sum_fen) if right_len > 0
    end
    seg.update(pos, 0)
  end
end

def number_of_alternating_groups(colors, queries)
  n = colors.length
  diff = Array.new(n)
  zero_cnt = 0
  (0...n).each do |i|
    diff[i] = (colors[i] != colors[(i + 1) % n]) ? 1 : 0
    zero_cnt += 1 if diff[i] == 0
  end

  seg = SegTree.new(diff)
  cnt_fen = Fenwick.new(n)
  sum_fen = Fenwick.new(n)

  if zero_cnt == 0
    add_run(n, cnt_fen, sum_fen)
  else
    zeros = []
    (0...n).each { |i| zeros << i if diff[i] == 0 }
    zlen = zeros.length
    (0...zlen).each do |i|
      a = zeros[i]
      b = zeros[(i + 1) % zlen]
      len = (b - a - 1) % n
      add_run(len, cnt_fen, sum_fen) if len > 0
    end
  end

  zero_cnt_ref = [zero_cnt]
  answers = []

  queries.each do |q|
    type = q[0]
    if type == 1
      k = q[1]
      w = k - 1
      cnt_ge = cnt_fen.range_sum(w, n)
      sum_ge = sum_fen.range_sum(w, n)
      ans = sum_ge - cnt_ge * (w - 1)
      answers << ans
    else
      idx = q[1]
      newc = q[2]
      next if colors[idx] == newc
      colors[idx] = newc
      pos1 = (idx - 1) % n
      pos2 = idx % n
      [pos1, pos2].each do |pos|
        old_val = diff[pos]
        new_val = (colors[pos] != colors[(pos + 1) % n]) ? 1 : 0
        if old_val != new_val
          process_edge_change(pos, old_val, new_val, seg, zero_cnt_ref, cnt_fen, sum_fen, n)
          diff[pos] = new_val
        end
      end
    end
  end

  answers
end
```

## Scala

```scala
import java.util.TreeMap
import scala.collection.mutable.{ArrayBuffer, ListBuffer}

object Solution {
  class Fenwick(size: Int) {
    private val tree = new Array[Long](size + 2)
    def add(idx: Int, delta: Long): Unit = {
      var i = idx
      while (i <= size) {
        tree(i) += delta
        i += i & -i
      }
    }
    def sum(idx: Int): Long = {
      var res = 0L
      var i = idx
      while (i > 0) {
        res += tree(i)
        i -= i & -i
      }
      res
    }
  }

  def numberOfAlternatingGroups(colors: Array[Int], queries: Array[Array[Int]]): List[Int] = {
    val n = colors.length
    val diff = new Array[Boolean](n) // edge i between i and (i+1)%n
    for (i <- 0 until n) {
      diff(i) = colors(i) != colors((i + 1) % n)
    }

    var totalOnes = 0L
    var prefixLen = 0          // run starting at 0, length >0
    var suffixStart = -1       // start index of suffix run (if any)
    var suffixLen = 0
    val runs = new TreeMap[Int, Int]() // internal runs: start -> len

    val maxSize = n
    val cntFenwick = new Fenwick(maxSize)
    val sumFenwick = new Fenwick(maxSize)

    def addRunInternal(len: Int): Unit = {
      if (len > 0) {
        cntFenwick.add(len, 1L)
        sumFenwick.add(len, len.toLong + 1L)
      }
    }

    def removeRunInternal(len: Int): Unit = {
      if (len > 0) {
        cntFenwick.add(len, -1L)
        sumFenwick.add(len, -(len.toLong + 1L))
      }
    }

    def addRun(start: Int, len: Int): Unit = {
      if (len <= 0) return
      totalOnes += len
      if (start == 0) {
        prefixLen = len
      } else if (start + len == n) {
        suffixStart = start
        suffixLen = len
      } else {
        runs.put(start, len)
        addRunInternal(len)
      }
    }

    def removeRun(start: Int, len: Int): Unit = {
      if (len <= 0) return
      totalOnes -= len
      if (start == 0) {
        prefixLen = 0
      } else if (start + len == n) {
        suffixStart = -1
        suffixLen = 0
      } else {
        runs.remove(start)
        removeRunInternal(len)
      }
    }

    def getRun(idx: Int): (Int, Int, Boolean) = { // returns (start,len,isEdge)
      if (prefixLen > 0 && idx < prefixLen) return (0, prefixLen, true)
      if (suffixLen > 0 && idx >= n - suffixLen) return (n - suffixLen, suffixLen, true)
      val entryKey = runs.floorKey(idx)
      if (entryKey != null) {
        val l = runs.get(entryKey)
        if (idx < entryKey + l) return (entryKey, l, false)
      }
      (-1, 0, false) // should not happen for idx where diff[idx]==true
    }

    def updateDiff(pos: Int, newVal: Boolean): Unit = {
      val old = diff(pos)
      if (old == newVal) return
      diff(pos) = newVal
      if (old) { // turning 1 -> 0, split run
        val (s, l, edge) = getRun(pos)
        removeRun(s, l)
        val leftLen = pos - s
        val rightLen = (s + l) - (pos + 1)
        if (leftLen > 0) addRun(s, leftLen)
        if (rightLen > 0) addRun(pos + 1, rightLen)
      } else { // turning 0 -> 1, merge with neighbours
        val leftIdx = (pos - 1 + n) % n
        val rightIdx = (pos + 1) % n
        var newStart = pos
        var newLen = 1

        if (diff(leftIdx)) {
          val (ls, ll, _) = getRun(leftIdx)
          removeRun(ls, ll)
          newStart = ls
          newLen += ll
        }
        if (diff(rightIdx)) {
          val (rs, rl, _) = getRun(rightIdx)
          removeRun(rs, rl)
          newLen += rl
        }
        addRun(newStart, newLen)
      }
    }

    // initial runs detection
    var i = 0
    while (i < n) {
      if (!diff(i)) { i += 1 }
      else {
        var j = i
        while (j < n && diff(j)) j += 1
        val len = j - i
        addRun(i, len)
        i = j
      }
    }

    val answers = ListBuffer[Int]()

    def query(k: Int): Int = {
      if (totalOnes == n) {
        // all edges are 1 -> every start works for any k <= n
        return n
      }
      val t = k - 1 // needed consecutive ones
      var ans = 0L

      // internal runs contribution via fenwick
      val totalCnt = cntFenwick.sum(maxSize)
      val prefCnt = if (t > 0) cntFenwick.sum(t) else 0L
      val cntGe = totalCnt - prefCnt
      val totalSum = sumFenwick.sum(maxSize)
      val prefSum = if (t > 0) sumFenwick.sum(t) else 0L
      val sumGe = totalSum - prefSum
      ans += sumGe - t.toLong * cntGe

      // wrap contribution (prefix + suffix) if both exist
      var wrapLen = 0
      if (prefixLen > 0 && suffixLen > 0) wrapLen = prefixLen + suffixLen
      if (wrapLen > 0) {
        val add = math.max(0, wrapLen - t + 1)
        ans += add
      }
      ans.toInt
    }

    for (q <- queries) {
      q(0) match {
        case 1 =>
          answers += query(q(1))
        case 2 =>
          val idx = q(1)
          val newCol = q(2)
          if (colors(idx) != newCol) {
            // update affected diffs
            val leftNeighbor = (idx - 1 + n) % n
            colors(idx) = newCol
            val newDiffLeft = colors(leftNeighbor) != colors(idx)
            updateDiff((idx - 1 + n) % n, newDiffLeft)
            val newDiffRight = colors(idx) != colors((idx + 1) % n)
            updateDiff(idx, newDiffRight)
          }
      }
    }

    answers.toList
  }
}
```

## Rust

```rust
use std::collections::BTreeSet;

struct BIT {
    n: usize,
    freq: Vec<i64>,
    sum: Vec<i64>, // stores (len+1) * count
}
impl BIT {
    fn new(n: usize) -> Self {
        Self { n, freq: vec![0; n + 2], sum: vec![0; n + 2] }
    }
    fn add(&mut self, mut idx: usize, df: i64, ds: i64) {
        // idx is 1..=n
        while idx <= self.n {
            self.freq[idx] += df;
            self.sum[idx] += ds;
            idx += idx & (!idx + 1);
        }
    }
    fn prefix(&self, mut idx: usize) -> (i64, i64) {
        let mut f = 0i64;
        let mut s = 0i64;
        while idx > 0 {
            f += self.freq[idx];
            s += self.sum[idx];
            idx &= idx - 1;
        }
        (f, s)
    }
}

impl Solution {
    pub fn number_of_alternating_groups(colors: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = colors.len();
        let mut col = colors.clone();
        // helper distance on circle
        let dist = |a: usize, b: usize| -> usize {
            if a == b { n } else { (b + n - a) % n }
        };
        // initialize break set
        let mut breaks: BTreeSet<usize> = BTreeSet::new();
        for i in 0..n {
            if col[i] == col[(i + 1) % n] {
                breaks.insert(i);
            }
        }
        let mut cnt_breaks = breaks.len();
        let mut bit = BIT::new(n);
        // function to add component length to BIT
        let mut add_len = |len: usize, delta: i64, bit: &mut BIT| {
            if len == 0 { return; }
            bit.add(len, delta, delta * (len as i64 + 1));
        };
        // initialize components in BIT when cnt_breaks > 0
        if cnt_breaks > 0 {
            let mut prev_opt = None;
            for &b in breaks.iter() {
                if let Some(prev) = prev_opt {
                    let len = dist(prev, b);
                    add_len(len, 1, &mut bit);
                }
                prev_opt = Some(b);
            }
            // last to first
            if let (Some(first), Some(last)) = (breaks.iter().next(), breaks.iter().next_back()) {
                let len = dist(*last, *first);
                add_len(len, 1, &mut bit);
            }
        }

        // helper to find neighbors in current break set (assumes set not empty)
        let mut get_neighbors = |e: usize, set: &BTreeSet<usize>| -> (usize, usize) {
            // previous
            let prev = match set.range(..e).next_back() {
                Some(&v) => v,
                None => *set.iter().next_back().unwrap(),
            };
            // next
            let next = match set.range((e + 1)..).next() {
                Some(&v) => v,
                None => *set.iter().next().unwrap(),
            };
            (prev, next)
        };

        // handlers for adding/removing a break edge
        let mut handle_add_break = |e: usize,
                                    breaks: &mut BTreeSet<usize>,
                                    cnt_breaks: &mut usize,
                                    bit: &mut BIT| {
            if *cnt_breaks == 0 {
                // transition from 0 to 1
                *cnt_breaks = 1;
                breaks.insert(e);
                add_len(n, 1, bit); // single linear component of length n
                return;
            }
            // find neighbors before insertion
            let (prev, next) = get_neighbors(e, &breaks);
            let old_len = if *cnt_breaks == 1 { n } else { dist(prev, next) };
            add_len(old_len, -1, bit);
            let len1 = dist(prev, e);
            let len2 = dist(e, next);
            add_len(len1, 1, bit);
            add_len(len2, 1, bit);
            breaks.insert(e);
            *cnt_breaks += 1;
        };

        let mut handle_remove_break = |e: usize,
                                       breaks: &mut BTreeSet<usize>,
                                       cnt_breaks: &mut usize,
                                       bit: &mut BIT| {
            if *cnt_breaks == 1 {
                // transition to zero breaks
                add_len(n, -1, bit);
                breaks.remove(&e);
                *cnt_breaks = 0;
                return;
            }
            // neighbors while e is still present
            let (prev, next) = get_neighbors(e, &breaks);
            let len1 = dist(prev, e);
            let len2 = dist(e, next);
            add_len(len1, -1, bit);
            add_len(len2, -1, bit);
            let merged_len = if *cnt_breaks == 2 { n } else { dist(prev, next) };
            add_len(merged_len, 1, bit);
            breaks.remove(&e);
            *cnt_breaks -= 1;
        };

        let mut answers: Vec<i32> = Vec::new();

        for q in queries {
            if q[0] == 2 {
                // update
                let pos = q[1] as usize;
                let val = q[2];
                if col[pos] == val {
                    continue;
                }
                // edges: (pos-1,pos) edge index (pos-1+n)%n, and (pos,pos+1) edge index pos
                let edges = [
                    (pos + n - 1) % n,
                    pos,
                ];
                for &e in edges.iter() {
                    let a = e;
                    let b = (e + 1) % n;
                    let before_break = col[a] == col[b];
                    // compute after colors
                    let after_break = if a == pos {
                        val == col[b]
                    } else if b == pos {
                        col[a] == val
                    } else {
                        false // unreachable
                    };
                    if before_break != after_break {
                        if after_break {
                            handle_add_break(e, &mut breaks, &mut cnt_breaks, &mut bit);
                        } else {
                            handle_remove_break(e, &mut breaks, &mut cnt_breaks, &mut bit);
                        }
                    }
                }
                col[pos] = val;
            } else {
                // query count for size k
                let k = q[1] as usize;
                if k > n {
                    answers.push(0);
                    continue;
                }
                let ans: i64 = if cnt_breaks == 0 {
                    n as i64
                } else {
                    let (total_freq, total_sum) = bit.prefix(n);
                    let (pref_freq, pref_sum) = if k > 1 { bit.prefix(k - 1) } else { (0, 0) };
                    let cnt_ge = total_freq - pref_freq;
                    let sum_ge = total_sum - pref_sum;
                    sum_ge - (k as i64) * cnt_ge
                };
                answers.push(ans as i32);
            }
        }

        answers
    }
}
```

## Racket

```racket
(define/contract (number-of-alternating-groups colors queries)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ((n (length colors))
         (vec-col (list->vector colors))
         (bad-vec (make-vector n #f))
         ;; Fenwick trees: index 1..n
         (bit-bad (make-vector (+ n 2) 0))
         (bit-cnt (make-vector (+ n 2) 0))
         (bit-sum (make-vector (+ n 2) 0))

         (add-bit!
           (lambda (bit idx delta)
             (let loop ((i idx))
               (when (<= i n)
                 (vector-set! bit i (+ (vector-ref bit i) delta))
                 (loop (+ i (bitwise-and i (- i))))))))

         (sum-bit
           (lambda (bit idx)
             (let loop ((i idx) (acc 0))
               (if (= i 0) acc
                   (loop (- i (bitwise-and i (- i))) (+ acc (vector-ref bit i)))))))

         (find-by-order
           (lambda (bit k)
             (let* ((size n)
                    (max-log (integer-length size)))
               (let loop ((idx 0) (mask (arithmetic-shift 1 (- max-log 1))))
                 (if (= mask 0) (+ idx 1)
                     (let ((next (+ idx mask)))
                       (if (and (<= next size) (< (vector-ref bit next) k))
                           (loop next (arithmetic-shift mask -1))
                           (loop idx (arithmetic-shift mask -1)))))))))

         (dist
           (lambda (a b)
             (let ((d (modulo (- b a) n)))
               (if (= d 0) n d))))

         (update-count!
           (lambda (len delta)
             (add-bit! bit-cnt len delta)
             (add-bit! bit-sum len (* delta len))))

         (total-bad
           (lambda () (sum-bit bit-bad n)))

         (prev-bad
           (lambda (pos) ; last bad <= pos, assumes at least one bad exists
             (let* ((cnt-before (sum-bit bit-bad (+ pos 1))) ; prefix up to pos
                    (total (total-bad)))
               (if (> cnt-before 0)
                   (let ((target cnt-before))
                     (- (find-by-order bit-bad target) 1))
                   (let ((target total))
                     (- (find-by-order bit-bad target) 1))))))

         (next-bad
           (lambda (pos) ; first bad > pos, assumes at least one bad exists
             (let* ((cnt-up-to (sum-bit bit-bad (+ pos 1))) ; up to pos inclusive
                    (total (total-bad))
                    (after (- total cnt-up-to)))
               (if (> after 0)
                   (let ((target (+ cnt-up-to 1)))
                     (- (find-by-order bit-bad target) 1))
                   (let ((target 1))
                     (- (find-by-order bit-bad target) 1))))))

         (prev-bad-excl
           (lambda (pos) ; previous bad not equal to pos, assumes at least two bads
             (let* ((cnt-before (sum-bit bit-bad (+ pos 1))) ; includes pos if bad
                    (total (total-bad)))
               (if (> cnt-before 1)
                   (let ((target (- cnt-before 1)))
                     (- (find-by-order bit-bad target) 1))
                   (let ((target total))
                     (- (find-by-order bit-bad target) 1))))))

         (next-bad-excl
           (lambda (pos) ; next bad not equal to pos, assumes at least two bads
             (let* ((cnt-up-to (sum-bit bit-bad (+ pos 1))) ; includes pos if bad
                    (total (total-bad))
                    (after (- total cnt-up-to)))
               (if (> after 0)
                   (let ((target (+ cnt-up-to 1)))
                     (- (find-by-order bit-bad target) 1))
                   (let ((target 1))
                     (- (find-by-order bit-bad target) 1))))))

         (add-bad
           (lambda (e)
             (let ((m (total-bad)))
               (if (= m 0)
                   ; first bad edge, counts stay the same (single arc length n)
                   (void)
                   (let* ((p (prev-bad e))
                          (nx (next-bad e))
                          (L (dist p nx))
                          (L1 (dist p e))
                          (L2 (dist e nx)))
                     (update-count! L -1)
                     (update-count! L1 1)
                     (update-count! L2 1))))
             (add-bit! bit-bad (+ e 1) 1)))

         (remove-bad
           (lambda (e)
             (let ((m (total-bad)))
               (if (= m 1)
                   ; removing the only bad edge, counts stay the same
                   (void)
                   (let* ((p (prev-bad-excl e))
                          (nx (next-bad-excl e))
                          (L1 (dist p e))
                          (L2 (dist e nx))
                          (L (dist p nx)))
                     (update-count! L1 -1)
                     (update-count! L2 -1)
                     (update-count! L 1))))
             (add-bit! bit-bad (+ e 1) -1)))

         ;; initialize bad edges and counts
         (init
           (let loop ((i 0))
             (when (< i n)
               (let* ((next (modulo (+ i 1) n))
                      (isbad (= (vector-ref vec-col i) (vector-ref vec-col next))))
                 (when isbad
                   (vector-set! bad-vec i #t)
                   (add-bit! bit-bad (+ i 1) 1)))
               (loop (+ i 1)))))
         (_ (init))

         ;; build initial arcs counts
         (build-initial-counts
           (let ((m (total-bad)))
             (if (= m 0)
                 (update-count! n 1)
                 (let* ((bad-indices
                         (let loop ((i 0) (acc '()))
                           (if (= i n) (reverse acc)
                               (loop (+ i 1) (if (vector-ref bad-vec i) (cons i acc) acc)))))
                        (len (length bad-indices)))
                   (let loop ((idx 0))
                     (when (< idx len)
                       (let* ((cur (list-ref bad-indices idx))
                              (next (list-ref bad-indices (modulo (+ idx 1) len)))
                              (L (dist cur next)))
                         (update-count! L 1))
                       (loop (+ idx 1))))))))

         (_ (build-initial-counts))

         (answers (make-vector 0)) ; will grow using vector-append
         (ans-list '()))

    ;; helper to push answer
    (define (push ans)
      (set! ans-list (cons ans ans-list)))

    ;; process queries
    (for ([q queries])
      (cond
        [(= (first q) 2)
         (let* ((idx (second q))
                (val (list-ref q 2)))
           (when (not (= (vector-ref vec-col idx) val))
             ;; update colors
             (vector-set! vec-col idx val)
             ;; left edge between (idx-1) and idx
             (let* ((left (modulo (- idx 1) n))
                    (right idx))
               (for ([e (list left right)])
                 (let* ((a e)
                        (b (modulo (+ e 1) n))
                        (newbad (= (vector-ref vec-col a) (vector-ref vec-col b)))
                        (oldbad (vector-ref bad-vec e)))
                   (when (not (= oldbad newbad))
                     (if newbad
                         (add-bad e)
                         (remove-bad e))
                     (vector-set! bad-vec e newbad)))))))]

        [(= (first q) 1)
         (let* ((k (second q))
                (m (total-bad)))
           (if (= m 0)
               (push n)
               (let* ((total-cnt (sum-bit bit-cnt n))
                      (pref-cnt (sum-bit bit-cnt (- k 1)))
                      (s0 (- total-cnt pref-cnt))
                      (total-sum (sum-bit bit-sum n))
                      (pref-sum (sum-bit bit-sum (- k 1)))
                      (s1 (- total-sum pref-sum))
                      (ans (- s1 (* (- k 1) s0))))
                 (push ans))))]))

    (reverse ans-list)))
```

## Erlang

```erlang
-spec number_of_alternating_groups(Colors :: [integer()], Queries :: [[integer()]]) -> [integer()].
number_of_alternating_groups(Colors, Queries) ->
    N = length(Colors),
    ColorArr = list_to_array(Colors),
    DiffList = build_diff_list(ColorArr, N),
    DiffArr0 = list_to_array(DiffList),
    Zeros0 = count_zeros(DiffList),

    % initial intervals and fenwick trees
    {Starts0, Ends0, CntFen0, SumFen0} = init_intervals(DiffList, N),

    State0 = {N, DiffArr0, Starts0, Ends0, CntFen0, SumFen0, Zeros0, ColorArr},
    AnswersRev = process_queries(Queries, State0, []),
    lists:reverse(AnswersRev).

%% --------------------------------------------------------------------
%% Helpers
list_to_array(L) ->
    array:from_list(L).

build_diff_list(ColorArr, N) ->
    build_diff_list(0, N, ColorArr, []).

build_diff_list(I, N, _ColorArr, Acc) when I =:= N -> lists:reverse(Acc);
build_diff_list(I, N, ColorArr, Acc) ->
    C1 = array:get(I, ColorArr),
    C2 = array:get((I + 1) rem N, ColorArr),
    D = if C1 =/= C2 -> 1; true -> 0 end,
    build_diff_list(I + 1, N, ColorArr, [D | Acc]).

count_zeros(List) ->
    count_zeros(List, 0).
count_zeros([], C) -> C;
count_zeros([0|T], C) -> count_zeros(T, C+1);
count_zeros([_|T], C) -> count_zeros(T, C).

%% Initialize intervals from diff list
init_intervals(DiffList, N) ->
    Starts = gb_trees:empty(),
    Ends   = gb_trees:empty(),
    CntFen0 = {N, array:new(N+1, {default,0})},
    SumFen0 = {N, array:new(N+1, {default,0})},
    init_intervals(0, DiffList, N, Starts, Ends, CntFen0, SumFen0).

init_intervals(_Idx, [], _N, Starts, Ends, CntFen, SumFen) ->
    {Starts, Ends, CntFen, SumFen};
init_intervals(Idx, [0|Rest], N, Starts, Ends, CntFen, SumFen) ->
    init_intervals(Idx+1, Rest, N, Starts, Ends, CntFen, SumFen);
init_intervals(Idx, List, N, Starts, Ends, CntFen, SumFen) ->
    {Len, NextIdx} = count_run(List, 0),
    Start = Idx,
    End   = Idx + Len - 1,
    {Starts2, Ends2, CntFen2, SumFen2} =
        add_interval(Start, End, Starts, Ends, CntFen, SumFen),
    Rest = lists:sublist(List, Len+1, length(List)-Len-1), % skip processed run and following zero
    init_intervals(NextIdx+1, Rest, N, Starts2, Ends2, CntFen2, SumFen2).

count_run([], Acc) -> {Acc, 0};
count_run([1|T], Acc) -> count_run(T, Acc+1);
count_run(_, Acc) -> {Acc, 0}.

%% Fenwick operations
fenwick_add({Size, Tree}, Index, Delta) ->
    NewTree = fenwick_add_loop(Index + 1, Size, Tree, Delta),
    {Size, NewTree}.

fenwick_add_loop(I, Size, Tree, _Delta) when I > Size -> Tree;
fenwick_add_loop(I, Size, Tree, Delta) ->
    Val = array:get(I, Tree),
    Tree2 = array:set(I, Val + Delta, Tree),
    fenwick_add_loop(I + (I band -I), Size, Tree2, Delta).

fenwick_sum({Size, Tree}, Index) when Index < 0 -> 0;
fenwick_sum({Size, Tree}, Index) ->
    fenwick_sum_loop(Index + 1, Tree, 0).

fenwick_sum_loop(0, _Tree, Acc) -> Acc;
fenwick_sum_loop(I, Tree, Acc) ->
    Val = array:get(I, Tree),
    fenwick_sum_loop(I - (I band -I), Tree, Acc + Val).

%% Interval add/remove with fenwick updates
add_interval(Start, End, Starts, Ends, CntFen, SumFen) ->
    Len = End - Start + 1,
    Starts2 = gb_trees:insert(Start, End, Starts),
    Ends2   = gb_trees:insert(End, Start, Ends),
    CntFen2 = fenwick_add(CntFen, Len, 1),
    SumFen2 = fenwick_add(SumFen, Len, Len),
    {Starts2, Ends2, CntFen2, SumFen2}.

remove_interval(Start, End, Starts, Ends, CntFen, SumFen) ->
    Len = End - Start + 1,
    Starts2 = gb_trees:delete(Start, Starts),
    Ends2   = gb_trees:delete(End, Ends),
    CntFen2 = fenwick_add(CntFen, Len, -1),
    SumFen2 = fenwick_add(SumFen, Len, -Len),
    {Starts2, Ends2, CntFen2, SumFen2}.

%% Process all queries
process_queries([], _State, Acc) -> Acc;
process_queries([Q|Rest], State, Acc) ->
    case Q of
        [2,Idx,Val] ->
            NewState = handle_update(Idx, Val, State),
            process_queries(Rest, NewState, Acc);
        [1,K] ->
            Answer = query_count(K, State),
            process_queries(Rest, State, [Answer|Acc])
    end.

%% Update colors and affected diffs
handle_update(Idx, NewColor, {N, DiffArr, Starts, Ends, CntFen, SumFen, Zeros, ColorArr}) ->
    OldColor = array:get(Idx, ColorArr),
    case OldColor of
        NewColor -> % no change
            {N, DiffArr, Starts, Ends, CntFen, SumFen, Zeros, ColorArr};
        _ ->
            ColorArr2 = array:set(Idx, NewColor, ColorArr),

            PrevPos = (Idx - 1 + N) rem N,
            NextPos = Idx,

            {DiffArr1, Starts1, Ends1, CntFen1, SumFen1, Zeros1} =
                toggle_diff(PrevPos, DiffArr, Starts, Ends, CntFen, SumFen, Zeros),

            {DiffArr2, Starts2, Ends2, CntFen2, SumFen2, Zeros2} =
                toggle_diff(NextPos, DiffArr1, Starts1, Ends1, CntFen1, SumFen1, Zeros1),

            {N, DiffArr2, Starts2, Ends2, CntFen2, SumFen2, Zeros2, ColorArr2}
    end.

%% Toggle a diff position
toggle_diff(Pos, DiffArr, Starts, Ends, CntFen, SumFen, Zeros) ->
    Old = array:get(Pos, DiffArr),
    New = 1 - Old,
    Zeros2 = if Old =:= 0 -> Zeros - 1; true -> Zeros + 1 end,
    DiffArr2 = array:set(Pos, New, DiffArr),

    case New of
        1 ->
            {Starts2, Ends2, CntFen2, SumFen2} =
                turn_on_diff(Pos, Starts, Ends, CntFen, SumFen),
            {DiffArr2, Starts2, Ends2, CntFen2, SumFen2, Zeros2};
        0 ->
            {Starts2, Ends2, CntFen2, SumFen2} =
                turn_off_diff(Pos, Starts, Ends, CntFen, SumFen),
            {DiffArr2, Starts2, Ends2, CntFen2, SumFen2, Zeros2}
    end.

turn_on_diff(Pos, Starts, Ends, CntFen, SumFen) ->
    N = array:size(Starts), % dummy to avoid unused warning
    LeftExists = if Pos > 0 -> case gb_trees:lookup(Pos-1, Ends) of {value,_} -> true; none -> false end; true -> false end,
    RightExists = if Pos < (array:size(DiffArr)-1) -> case gb_trees:lookup(Pos+1, Starts) of {value,_} -> true; none -> false end; true -> false end,
    case {LeftExists, RightExists} of
        {true,true} ->
            {value, LStart} = gb_trees:lookup(Pos-1, Ends),
            {value, REnd}   = gb_trees:lookup(Pos+1, Starts),
            {StartsA, EndsA, CntFenA, SumFenA} = remove_interval(LStart, Pos-1, Starts, Ends, CntFen, SumFen),
            {StartsB, EndsB, CntFenB, SumFenB} = remove_interval(Pos+1, REnd, StartsA, EndsA, CntFenA, SumFenA),
            add_interval(LStart, REnd, StartsB, EndsB, CntFenB, SumFenB);
        {true,false} ->
            {value, LStart} = gb_trees:lookup(Pos-1, Ends),
            {StartsA, EndsA, CntFenA, SumFenA} = remove_interval(LStart, Pos-1, Starts, Ends, CntFen, SumFen),
            add_interval(LStart, Pos, StartsA, EndsA, CntFenA, SumFenA);
        {false,true} ->
            {value, REnd} = gb_trees:lookup(Pos+1, Starts),
            {StartsA, EndsA, CntFenA, SumFenA} = remove_interval(Pos+1, REnd, Starts, Ends, CntFen, SumFen),
            add_interval(Pos, REnd, StartsA, EndsA, CntFenA, SumFenA);
        {false,false} ->
            add_interval(Pos, Pos, Starts, Ends, CntFen, SumFen)
    end.

turn_off_diff(Pos, Starts, Ends, CntFen, SumFen) ->
    case gb_trees:lookup(Pos, Starts) of
        {value, End} ->
            IntervalStart = Pos,
            IntervalEnd   = End;
        none ->
            Iter = gb_trees:iterator_from(Pos, Starts),
            Prev = gb_trees:prev(Iter),
            case Prev of
                none -> erlang:error(bad_state);
                {Start, End, _} when End >= Pos ->
                    IntervalStart = Start,
                    IntervalEnd   = End;
                _ -> erlang:error(bad_state)
            end
    end,
    {StartsA, EndsA, CntFenA, SumFenA} = remove_interval(IntervalStart, IntervalEnd, Starts, Ends, CntFen, SumFen),
    % left part
    {StartsB, EndsB, CntFenB, SumFenB} =
        if IntervalStart =< Pos-1 ->
                add_interval(IntervalStart, Pos-1, StartsA, EndsA, CntFenA, SumFenA);
           true -> {StartsA, EndsA, CntFenA, SumFenA}
        end,
    % right part
    {StartsC, EndsC, CntFenC, SumFenC} =
        if Pos+1 =< IntervalEnd ->
                add_interval(Pos+1, IntervalEnd, StartsB, EndsB, CntFenB, SumFenB);
           true -> {StartsB, EndsB, CntFenB, SumFenB}
        end,
    {StartsC, EndsC, CntFenC, SumFenC}.

%% Query count for size K
query_count(K, {N, _DiffArr, Starts, Ends, CntFen, SumFen, Zeros, _ColorArr}) ->
    if Zeros =:= 0 ->
            if K =< N -> N; true -> 0 end;
       true ->
            L = K - 1,
            if L > N-1 -> 0;
               true ->
                    TotalCntAll = fenwick_sum(CntFen, N),
                    CntLess = fenwick_sum(CntFen, L-1),
                    CntGe = TotalCntAll - CntLess,

                    SumAll = fenwick_sum(SumFen, N),
                    SumLess = fenwick_sum(SumFen, L-1),
                    SumGe = SumAll - SumLess,

                    Base = SumGe - (L-1) * CntGe,

                    FirstLen = case gb_trees:lookup(0, Starts) of
                                   {value, End} -> End + 1;
                                   none -> 0
                               end,
                    LastLen = case gb_trees:lookup(N-1, Ends) of
                                  {value, Start} -> N - Start;
                                  none -> 0
                              end,

                    Adjusted =
                        if FirstLen > 0, LastLen > 0, FirstLen + LastLen =/= N ->
                                ContribF = max(0, FirstLen - L + 1),
                                ContribL = max(0, LastLen - L + 1),
                                Combined = max(0, FirstLen + LastLen - L + 1),
                                Base - ContribF - ContribL + Combined;
                           true -> Base
                        end,
                    Adjusted
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_alternating_groups(colors :: [integer], queries :: [[integer]]) :: [integer]
  def number_of_alternating_groups(colors, queries) do
    n = length(colors)
    colors_arr = :array.from_list(colors)

    diff_list =
      for i <- 0..(n - 1) do
        a = Enum.at(colors, i)
        b = Enum.at(colors, rem(i + 1, n))
        if a != b, do: 1, else: 0
      end

    diff_arr = :array.from_list(diff_list)

    bit = BIT.new(n)
    intervals = :gb_trees.empty()
    {intervals, bit} = build_intervals(0, n, diff_arr, intervals, bit)

    # process queries
    {answers_rev, _, _, intervals, bit} =
      Enum.reduce(queries, {[], colors_arr, diff_arr, intervals, bit}, fn query,
                                                                          {ans_acc,
                                                                           col_arr,
                                                                           dif_arr,
                                                                           intv_tree,
                                                                           btree} ->
        [type | rest] = query

        cond do
          type == 2 ->
            [idx, newc] = rest
            oldc = :array.get(idx, col_arr)

            if oldc == newc do
              {ans_acc, col_arr, dif_arr, intv_tree, btree}
            else
              col_arr = :array.set(idx, newc, col_arr)
              left_pos = rem(idx - 1 + n, n)
              right_pos = idx

              {intv_tree, btree, dif_arr} =
                Enum.reduce([left_pos, right_pos], {intv_tree, btree, dif_arr}, fn pos,
                                                                                 {itree,
                                                                                  ibtree,
                                                                                  darray} ->
                  a = :array.get(pos, col_arr)
                  bcol = :array.get(rem(pos + 1, n), col_arr)
                  new_diff = if a != bcol, do: 1, else: 0
                  old_diff = :array.get(pos, darray)

                  if old_diff == new_diff do
                    {itree, ibtree, darray}
                  else
                    darray = :array.set(pos, new_diff, darray)

                    if new_diff == 1 do
                      {itree2, ibtree2} = add_one(pos, itree, ibtree, n, darray)
                      {itree2, ibtree2, darray}
                    else
                      {itree2, ibtree2} = remove_one(pos, itree, ibtree, n, darray)
                      {itree2, ibtree2, darray}
                    end
                  end
                end)

              {ans_acc, col_arr, dif_arr, intv_tree, btree}
            end

          type == 1 ->
            [k] = rest
            w = k - 1

            total_cnt = BIT.total_cnt(btree)
            total_sum = BIT.total_sum(btree)

            cnt_ge = total_cnt - BIT.prefix_cnt(btree, w - 1)
            sum_ge = total_sum - BIT.prefix_sum(btree, w - 1)

            base = sum_ge - w * cnt_ge

            first_info =
              case :gb_trees.lookup(0, intervals) do
                {:value, e} -> {e, e - 0 + 1}
                :none -> nil
              end

            last_info = get_last_interval(intervals, n)

            answer =
              if first_info != nil and last_info != nil do
                {first_end, first_len} = first_info
                {last_start, last_len} = last_info

                if first_end < n - 1 and last_start > 0 do
                  contrib_first = max(0, first_len - w + 1)
                  contrib_last = max(0, last_len - w + 1)
                  combined = max(0, (first_len + last_len) - w + 1)

                  base - contrib_first - contrib_last + combined
                else
                  base
                end
              else
                base
              end

            {[answer | ans_acc], col_arr, dif_arr, intervals, btree}
        end
      end)

    Enum.reverse(answers_rev)
  end

  # Build initial intervals and BIT
  defp build_intervals(i, n, diff_arr, intv_tree, bit) when i < n do
    if :array.get(i, diff_arr) == 1 do
      start = i
      j = i + 1

      while j < n && :array.get(j, diff_arr) == 1 do
        j = j + 1
      end

      finish = j - 1
      len = finish - start + 1
      intv_tree = :gb_trees.insert(start, finish, intv_tree)
      bit = BIT.add(bit, len, 1)
      build_intervals(j, n, diff_arr, intv_tree, bit)
    else
      build_intervals(i + 1, n, diff_arr, intv_tree, bit)
    end
  end

  defp build_intervals(_, _, _, intv_tree, bit), do: {intv_tree, bit}

  # Find interval containing position pos
  defp find_interval(tree, pos) do
    it = :gb_trees.iterator_from(pos)

    case :gb_trees.prev(it) do
      nil -> nil
      {l, r} -> if pos <= r, do: {l, r}, else: nil
    end
  end

  # Add a one at position pos (0->1)
  defp add_one(pos, intervals, bit, n, diff_arr) do
    left_interval =
      if :array.get(rem(pos - 1 + n, n), diff_arr) == 1,
        do: find_interval(intervals, rem(pos - 1 + n, n)),
        else: nil

    right_interval =
      if :array.get(rem(pos + 1, n), diff_arr) == 1,
        do: find_interval(intervals, rem(pos + 1, n)),
        else: nil

    cond do
      left_interval == nil and right_interval == nil ->
        intervals = :gb_trees.insert(pos, pos, intervals)
        bit = BIT.add(bit, 1, 1)
        {intervals, bit}

      left_interval != nil and right_interval == nil ->
        {l_start, l_end} = left_interval
        len_old = l_end - l_start + 1
        intervals = :gb_trees.delete(l_start, intervals)
        bit = BIT.add(bit, len_old, -1)

        new_len = pos - l_start + 1
        intervals = :gb_trees.insert(l_start, pos, intervals)
        bit = BIT.add(bit, new_len, 1)
        {intervals, bit}

      left_interval == nil and right_interval != nil ->
        {r_start, r_end} = right_interval
        len_old = r_end - r_start + 1
        intervals = :gb_trees.delete(r_start, intervals)
        bit = BIT.add(bit, len_old, -1)

        new_len = r_end - pos + 1
        intervals = :gb_trees.insert(pos, r_end, intervals)
        bit = BIT.add(bit, new_len, 1)
        {intervals, bit}

      true ->
        {l_start, l_end} = left_interval
        {r_start, r_end} = right_interval

        # if they are the edge intervals that wrap around, do not merge them linearly
        if l_end == n - 1 and r_start == 0 do
          # treat as separate; just extend both sides logically (no change in BIT needed)
          {intervals, bit}
        else
          len_left = l_end - l_start + 1
          len_right = r_end - r_start + 1

          intervals = :gb_trees.delete(l_start, intervals)
          intervals = :gb_trees.delete(r_start, intervals)

          bit = BIT.add(bit, len_left, -1)
          bit = BIT.add(bit, len_right, -1)

          new_len = len_left + 1 + len_right
          intervals = :gb_trees.insert(l_start, r_end, intervals)
          bit = BIT.add(bit, new_len, 1)
          {intervals, bit}
        end
    end
  end

  # Remove a one at position pos (1->0)
  defp remove_one(pos, intervals, bit, n, diff_arr) do
    interval = find_interval(intervals, pos)

    case interval do
      nil ->
        {intervals, bit}

      {l_start, l_end} ->
        len_old = l_end - l_start + 1
        intervals = :gb_trees.delete(l_start, intervals)
        bit = BIT.add(bit, len_old, -1)

        cond do
          l_start == l_end ->
            {intervals, bit}

          pos == l_start ->
            new_len = l_end - (l_start + 1) + 1
            intervals = :gb_trees.insert(l_start + 1, l_end, intervals)
            bit = BIT.add(bit, new_len, 1)
            {intervals, bit}

          pos == l_end ->
            new_len = (l_end - 1) - l_start + 1
            intervals = :gb_trees.insert(l_start, l_end - 1, intervals)
            bit = BIT.add(bit, new_len, 1)
            {intervals, bit}

          true ->
            left_len = pos - 1 - l_start + 1
            right_len = l_end - (pos + 1) + 1

            intervals = :gb_trees.insert(l_start, pos - 1, intervals)
            intervals = :gb_trees.insert(pos + 1, l_end, intervals)

            bit = BIT.add(bit, left_len, 1)
            bit = BIT.add(bit, right_len, 1)
            {intervals, bit}
        end
    end
  end

  # Get last interval that ends at n-1
  defp get_last_interval(tree, n) do
    it = :gb_trees.iterator_from(n)

    case :gb_trees.prev(it) do
      nil -> nil
      {start, finish} ->
        if finish == n - 1,
          do: {start, finish - start + 1},
          else: nil
    end
  end
end

defmodule BIT do
  def new(n), do: %{n: n, cnt: :array.new(n + 2, default: 0), sum: :array.new(n + 2, default: 0)}

  def add(bit, idx, delta) when idx > 0 do
    bit = update(bit, :cnt, idx, delta)
    bit = update(bit, :sum, idx, (idx + 1 - 1) * delta)
    bit
  end

  defp update(bit, field, i, delta) do
    n = bit.n
    arr = Map.get(bit, field)

    arr =
      upd(arr, i, delta, n)

    Map.put(bit, field, arr)
  end

  defp upd(arr, i, delta, n) when i <= n do
    val = :array.get(i, arr)
    arr = :array.set(i, val + delta, arr)
    upd(arr, i + (i &&& -i), delta, n)
  end

  defp upd(arr, _i, _delta, _n), do: arr

  def prefix_cnt(bit, idx), do: pref(bit.cnt, idx)

  def prefix_sum(bit, idx), do: pref(bit.sum, idx)

  defp pref(arr, i) when i > 0 do
    val = :array.get(i, arr)
    val + pref(arr, i - (i &&& -i))
  end

  defp pref(_arr, _i), do: 0

  def total_cnt(bit), do: prefix_cnt(bit, bit.n)

  def total_sum(bit), do: prefix_sum(bit, bit.n)
end
```
