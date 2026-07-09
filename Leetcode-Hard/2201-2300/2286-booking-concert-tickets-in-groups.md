# 2286. Booking Concert Tickets in Groups

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class BookMyShow {
    int n;
    long long m;
    vector<long long> segMax, segSum;
    vector<long long> remain;

    void build(int node, int l, int r) {
        if (l == r) {
            segMax[node] = m;
            segSum[node] = m;
            return;
        }
        int mid = (l + r) >> 1;
        build(node << 1, l, mid);
        build(node << 1 | 1, mid + 1, r);
        segMax[node] = max(segMax[node << 1], segMax[node << 1 | 1]);
        segSum[node] = segSum[node << 1] + segSum[node << 1 | 1];
    }

    void pointUpdate(int node, int l, int r, int idx, long long val) {
        if (l == r) {
            segMax[node] = val;
            segSum[node] = val;
            return;
        }
        int mid = (l + r) >> 1;
        if (idx <= mid) pointUpdate(node << 1, l, mid, idx, val);
        else pointUpdate(node << 1 | 1, mid + 1, r, idx, val);
        segMax[node] = max(segMax[node << 1], segMax[node << 1 | 1]);
        segSum[node] = segSum[node << 1] + segSum[node << 1 | 1];
    }

    long long querySum(int node, int l, int r, int ql, int qr) {
        if (qr < l || ql > r) return 0;
        if (ql <= l && r <= qr) return segSum[node];
        int mid = (l + r) >> 1;
        return querySum(node << 1, l, mid, ql, qr) +
               querySum(node << 1 | 1, mid + 1, r, ql, qr);
    }

    // find first index in [ql,qr] with remaining >= need
    int findFirstGE(int node, int l, int r, int ql, int qr, long long need) {
        if (qr < l || ql > r || segMax[node] < need) return -1;
        if (l == r) return l;
        int mid = (l + r) >> 1;
        int left = findFirstGE(node << 1, l, mid, ql, qr, need);
        if (left != -1) return left;
        return findFirstGE(node << 1 | 1, mid + 1, r, ql, qr, need);
    }

public:
    BookMyShow(int n_, int m_) : n(n_), m(m_) {
        segMax.assign(4 * n, 0);
        segSum.assign(4 * n, 0);
        remain.assign(n, m);
        build(1, 0, n - 1);
    }

    vector<int> gather(int k, int maxRow) {
        if (segMax[1] < k) return {};
        int row = findFirstGE(1, 0, n - 1, 0, maxRow, k);
        if (row == -1) return {};
        long long seatStart = m - remain[row];
        remain[row] -= k;
        pointUpdate(1, 0, n - 1, row, remain[row]);
        return {row, (int)seatStart};
    }

    bool scatter(int k, int maxRow) {
        long long total = querySum(1, 0, n - 1, 0, maxRow);
        if (total < k) return false;
        while (k > 0) {
            int row = findFirstGE(1, 0, n - 1, 0, maxRow, 1);
            long long canTake = min(remain[row], (long long)k);
            remain[row] -= canTake;
            pointUpdate(1, 0, n - 1, row, remain[row]);
            k -= (int)canTake;
        }
        return true;
    }
};

/**
 * Your BookMyShow object will be instantiated and called as such:
 * BookMyShow* obj = new BookMyShow(n, m);
 * vector<int> param_1 = obj->gather(k,maxRow);
 * bool param_2 = obj->scatter(k,maxRow);
 */
```

## Java

```java
class BookMyShow {
    private final int n;
    private final long m;
    private final long[] next;          // next free seat in each row
    private final long[] segSum;        // segment tree sum of remaining seats
    private final long[] segMax;        // segment tree max of remaining seats

    public BookMyShow(int n, int m) {
        this.n = n;
        this.m = m;
        this.next = new long[n];
        this.segSum = new long[4 * n];
        this.segMax = new long[4 * n];
        build(1, 0, n - 1);
    }

    private void build(int node, int l, int r) {
        if (l == r) {
            segSum[node] = m;
            segMax[node] = m;
        } else {
            int mid = (l + r) >>> 1;
            build(node << 1, l, mid);
            build(node << 1 | 1, mid + 1, r);
            segSum[node] = segSum[node << 1] + segSum[node << 1 | 1];
            segMax[node] = Math.max(segMax[node << 1], segMax[node << 1 | 1]);
        }
    }

    private void update(int idx, int node, int l, int r) {
        if (l == r) {
            long rem = m - next[idx];
            segSum[node] = rem;
            segMax[node] = rem;
        } else {
            int mid = (l + r) >>> 1;
            if (idx <= mid) {
                update(idx, node << 1, l, mid);
            } else {
                update(idx, node << 1 | 1, mid + 1, r);
            }
            segSum[node] = segSum[node << 1] + segSum[node << 1 | 1];
            segMax[node] = Math.max(segMax[node << 1], segMax[node << 1 | 1]);
        }
    }

    private long querySum(int ql, int qr, int node, int l, int r) {
        if (ql > r || qr < l) return 0;
        if (ql <= l && r <= qr) return segSum[node];
        int mid = (l + r) >>> 1;
        return querySum(ql, qr, node << 1, l, mid) +
               querySum(ql, qr, node << 1 | 1, mid + 1, r);
    }

    // find first row <= maxRow with remaining seats >= need (need can be 1)
    private int findFirst(int maxRow, long need, int node, int l, int r) {
        if (l > maxRow || segMax[node] < need) return -1;
        if (l == r) return l;
        int mid = (l + r) >>> 1;
        int left = findFirst(maxRow, need, node << 1, l, mid);
        if (left != -1) return left;
        return findFirst(maxRow, need, node << 1 | 1, mid + 1, r);
    }

    public int[] gather(int k, int maxRow) {
        int row = findFirst(maxRow, k, 1, 0, n - 1);
        if (row == -1) return new int[0];
        long startSeat = next[row];
        next[row] += k;
        update(row, 1, 0, n - 1);
        return new int[]{row, (int) startSeat};
    }

    public boolean scatter(int k, int maxRow) {
        long total = querySum(0, maxRow, 1, 0, n - 1);
        if (total < k) return false;
        while (k > 0) {
            int row = findFirst(maxRow, 1, 1, 0, n - 1);
            long avail = m - next[row];
            long take = Math.min(avail, k);
            next[row] += take;
            update(row, 1, 0, n - 1);
            k -= take;
        }
        return true;
    }
}

/**
 * Your BookMyShow object will be instantiated and called as such:
 * BookMyShow obj = new BookMyShow(n, m);
 * int[] param_1 = obj.gather(k,maxRow);
 * boolean param_2 = obj.scatter(k,maxRow);
 */
```

## Python

```python
class BookMyShow(object):
    def __init__(self, n, m):
        """
        :type n: int
        :type m: int
        """
        self.n = n
        self.m = m
        size = 4 * n
        self.minPos = [0] * size          # minimum next empty seat index in the interval
        self.sumRem = [0] * size          # total remaining seats in the interval
        self.pos = [0] * n                # next empty seat for each row
        self._build(1, 0, n - 1)

    def _build(self, node, l, r):
        if l == r:
            self.minPos[node] = 0
            self.sumRem[node] = self.m
        else:
            mid = (l + r) // 2
            self._build(node * 2, l, mid)
            self._build(node * 2 + 1, mid + 1, r)
            self.minPos[node] = 0
            self.sumRem[node] = (r - l + 1) * self.m

    def _update(self, node, l, r, idx, newPos):
        if l == r:
            self.minPos[node] = newPos
            self.sumRem[node] = self.m - newPos
        else:
            mid = (l + r) // 2
            if idx <= mid:
                self._update(node * 2, l, mid, idx, newPos)
            else:
                self._update(node * 2 + 1, mid + 1, r, idx, newPos)
            left = node * 2
            right = node * 2 + 1
            self.minPos[node] = min(self.minPos[left], self.minPos[right])
            self.sumRem[node] = self.sumRem[left] + self.sumRem[right]

    def _query_min(self, node, l, r, ql, qr):
        if ql > r or qr < l:
            return float('inf')
        if ql <= l and r <= qr:
            return self.minPos[node]
        mid = (l + r) // 2
        return min(self._query_min(node * 2, l, mid, ql, qr),
                   self._query_min(node * 2 + 1, mid + 1, r, ql, qr))

    def _query_sum(self, node, l, r, ql, qr):
        if ql > r or qr < l:
            return 0
        if ql <= l and r <= qr:
            return self.sumRem[node]
        mid = (l + r) // 2
        return (self._query_sum(node * 2, l, mid, ql, qr) +
                self._query_sum(node * 2 + 1, mid + 1, r, ql, qr))

    def _find_first_le(self, node, l, r, ql, qr, limit):
        """return leftmost index in [ql,qr] with minPos <= limit, or -1"""
        if ql > r or qr < l or self.minPos[node] > limit:
            return -1
        if l == r:
            return l
        mid = (l + r) // 2
        left_res = self._find_first_le(node * 2, l, mid, ql, qr, limit)
        if left_res != -1:
            return left_res
        return self._find_first_le(node * 2 + 1, mid + 1, r, ql, qr, limit)

    def _find_first_available(self, node, l, r, ql, qr):
        """return leftmost index in [ql,qr] with pos < m (i.e., minPos <= m-1)"""
        if ql > r or qr < l or self.minPos[node] >= self.m:
            return -1
        if l == r:
            return l
        mid = (l + r) // 2
        left_res = self._find_first_available(node * 2, l, mid, ql, qr)
        if left_res != -1:
            return left_res
        return self._find_first_available(node * 2 + 1, mid + 1, r, ql, qr)

    def gather(self, k, maxRow):
        """
        :type k: int
        :type maxRow: int
        :rtype: List[int]
        """
        limit = self.m - k
        if limit < 0:
            return []
        min_in_range = self._query_min(1, 0, self.n - 1, 0, maxRow)
        if min_in_range > limit:
            return []
        row = self._find_first_le(1, 0, self.n - 1, 0, maxRow, limit)
        start_seat = self.pos[row]
        newPos = start_seat + k
        self.pos[row] = newPos
        self._update(1, 0, self.n - 1, row, newPos)
        return [row, start_seat]

    def scatter(self, k, maxRow):
        """
        :type k: int
        :type maxRow: int
        :rtype: bool
        """
        total_available = self._query_sum(1, 0, self.n - 1, 0, maxRow)
        if total_available < k:
            return False
        while k > 0:
            row = self._find_first_available(1, 0, self.n - 1, 0, maxRow)
            # row must exist because we have enough seats overall
            avail = self.m - self.pos[row]
            take = min(avail, k)
            newPos = self.pos[row] + take
            self.pos[row] = newPos
            self._update(1, 0, self.n - 1, row, newPos)
            k -= take
        return True
```

## Python3

```python
class BookMyShow:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.cur = [0] * n
        size = 1
        while size < n:
            size <<= 1
        self.N = size
        INF = 10 ** 18
        self.min_cur = [INF] * (2 * size)
        self.sum_remain = [0] * (2 * size)
        for i in range(n):
            self.min_cur[size + i] = 0
            self.sum_remain[size + i] = m
        for i in range(size - 1, 0, -1):
            self.min_cur[i] = min(self.min_cur[2 * i], self.min_cur[2 * i + 1])
            self.sum_remain[i] = self.sum_remain[2 * i] + self.sum_remain[2 * i + 1]

    def _update(self, idx: int):
        pos = self.N + idx
        self.min_cur[pos] = self.cur[idx]
        self.sum_remain[pos] = self.m - self.cur[idx]
        pos //= 2
        while pos:
            left = pos * 2
            right = left + 1
            self.min_cur[pos] = min(self.min_cur[left], self.min_cur[right])
            self.sum_remain[pos] = self.sum_remain[left] + self.sum_remain[right]
            pos //= 2

    def _query_sum(self, l: int, r: int) -> int:
        l += self.N
        r += self.N
        res = 0
        while l <= r:
            if l & 1:
                res += self.sum_remain[l]
                l += 1
            if not (r & 1):
                res += self.sum_remain[r]
                r -= 1
            l //= 2
            r //= 2
        return res

    def _find_first(self, node: int, nl: int, nr: int, limit: int, maxRow: int) -> int:
        if nl > maxRow or self.min_cur[node] > limit:
            return -1
        if nl == nr:
            return nl
        mid = (nl + nr) // 2
        left = node * 2
        right = left + 1
        res = self._find_first(left, nl, mid, limit, maxRow)
        if res != -1:
            return res
        return self._find_first(right, mid + 1, nr, limit, maxRow)

    def gather(self, k: int, maxRow: int):
        limit = self.m - k
        if limit < 0:
            return []
        row = self._find_first(1, 0, self.N - 1, limit, maxRow)
        if row == -1 or row >= self.n:
            return []
        start = self.cur[row]
        self.cur[row] += k
        self._update(row)
        return [row, start]

    def scatter(self, k: int, maxRow: int) -> bool:
        if self._query_sum(0, maxRow) < k:
            return False
        while k > 0:
            row = self._find_first(1, 0, self.N - 1, self.m - 1, maxRow)
            available = self.m - self.cur[row]
            take = min(available, k)
            self.cur[row] += take
            self._update(row)
            k -= take
        return True
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int n;
    long long m;
    long long *rem;      // remaining seats per row
    long long *segMax;   // segment tree max
    long long *segSum;   // segment tree sum
} BookMyShow;

static void build(BookMyShow *obj, int node, int l, int r) {
    if (l == r) {
        obj->rem[l] = obj->m;
        obj->segMax[node] = obj->m;
        obj->segSum[node] = obj->m;
        return;
    }
    int mid = (l + r) >> 1;
    build(obj, node << 1, l, mid);
    build(obj, node << 1 | 1, mid + 1, r);
    obj->segMax[node] = obj->m; // all leaves equal
    obj->segSum[node] = (long long)(r - l + 1) * obj->m;
}

static void update(BookMyShow *obj, int idx, long long val, int node, int l, int r) {
    if (l == r) {
        obj->segMax[node] = val;
        obj->segSum[node] = val;
        return;
    }
    int mid = (l + r) >> 1;
    if (idx <= mid)
        update(obj, idx, val, node << 1, l, mid);
    else
        update(obj, idx, val, node << 1 | 1, mid + 1, r);
    long long leftMax = obj->segMax[node << 1];
    long long rightMax = obj->segMax[node << 1 | 1];
    obj->segMax[node] = leftMax > rightMax ? leftMax : rightMax;
    obj->segSum[node] = obj->segSum[node << 1] + obj->segSum[node << 1 | 1];
}

static long long querySum(BookMyShow *obj, int ql, int qr, int node, int l, int r) {
    if (ql > r || qr < l) return 0;
    if (ql <= l && r <= qr) return obj->segSum[node];
    int mid = (l + r) >> 1;
    return querySum(obj, ql, qr, node << 1, l, mid) +
           querySum(obj, ql, qr, node << 1 | 1, mid + 1, r);
}

static int findGather(BookMyShow *obj, int k, int maxRow, int node, int l, int r) {
    if (l > maxRow || obj->segMax[node] < k) return -1;
    if (l == r) return l;
    int mid = (l + r) >> 1;
    int leftRes = findGather(obj, k, maxRow, node << 1, l, mid);
    if (leftRes != -1) return leftRes;
    return findGather(obj, k, maxRow, node << 1 | 1, mid + 1, r);
}

static int findFirstPositive(BookMyShow *obj, int maxRow, int node, int l, int r) {
    if (l > maxRow || obj->segMax[node] == 0) return -1;
    if (l == r) return l;
    int mid = (l + r) >> 1;
    int leftRes = findFirstPositive(obj, maxRow, node << 1, l, mid);
    if (leftRes != -1) return leftRes;
    return findFirstPositive(obj, maxRow, node << 1 | 1, mid + 1, r);
}

/** Initialize your data structure here. */
BookMyShow* bookMyShowCreate(int n, int m) {
    BookMyShow *obj = (BookMyShow *)malloc(sizeof(BookMyShow));
    obj->n = n;
    obj->m = m;
    obj->rem = (long long *)calloc(n, sizeof(long long));
    obj->segMax = (long long *)calloc(4 * n + 5, sizeof(long long));
    obj->segSum = (long long *)calloc(4 * n + 5, sizeof(long long));
    build(obj, 1, 0, n - 1);
    return obj;
}

/** Gather k seats in the same row <= maxRow. */
int* bookMyShowGather(BookMyShow* obj, int k, int maxRow, int* retSize) {
    int row = findGather(obj, k, maxRow, 1, 0, obj->n - 1);
    if (row == -1) {
        *retSize = 0;
        return NULL;
    }
    long long startSeat = obj->m - obj->rem[row];
    obj->rem[row] -= k;
    update(obj, row, obj->rem[row], 1, 0, obj->n - 1);
    int *res = (int *)malloc(2 * sizeof(int));
    res[0] = row;
    res[1] = (int)startSeat;
    *retSize = 2;
    return res;
}

/** Scatter k seats across rows <= maxRow. */
bool bookMyShowScatter(BookMyShow* obj, int k, int maxRow) {
    long long total = querySum(obj, 0, maxRow, 1, 0, obj->n - 1);
    if (total < k) return false;
    while (k > 0) {
        int row = findFirstPositive(obj, maxRow, 1, 0, obj->n - 1);
        long long take = obj->rem[row];
        if (take > k) take = k;
        obj->rem[row] -= take;
        update(obj, row, obj->rem[row], 1, 0, obj->n - 1);
        k -= (int)take;
    }
    return true;
}

void bookMyShowFree(BookMyShow* obj) {
    if (!obj) return;
    free(obj->rem);
    free(obj->segMax);
    free(obj->segSum);
    free(obj);
}

/**
 * Your BookMyShow struct will be instantiated and called as such:
 * BookMyShow* obj = bookMyShowCreate(n, m);
 * int* param_1 = bookMyShowGather(obj, k, maxRow, retSize);
 *
 * bool param_2 = bookMyShowScatter(obj, k, maxRow);
 *
 * bookMyShowFree(obj);
 */
```

## Csharp

```csharp
using System;

public class BookMyShow
{
    private readonly int n;
    private readonly int m;
    private readonly int[] remaining;
    private readonly int[] segMax;
    private readonly long[] segSum;

    public BookMyShow(int n, int m)
    {
        this.n = n;
        this.m = m;
        remaining = new int[n];
        for (int i = 0; i < n; i++) remaining[i] = m;
        segMax = new int[4 * n];
        segSum = new long[4 * n];
        Build(1, 0, n - 1);
    }

    private void Build(int node, int l, int r)
    {
        if (l == r)
        {
            segMax[node] = m;
            segSum[node] = m;
        }
        else
        {
            int mid = (l + r) >> 1;
            Build(node << 1, l, mid);
            Build(node << 1 | 1, mid + 1, r);
            Pull(node);
        }
    }

    private void Pull(int node)
    {
        segMax[node] = Math.Max(segMax[node << 1], segMax[node << 1 | 1]);
        segSum[node] = segSum[node << 1] + segSum[node << 1 | 1];
    }

    private void Update(int idx, int delta) // delta is negative when seats are taken
    {
        Update(1, 0, n - 1, idx, delta);
    }

    private void Update(int node, int l, int r, int idx, int delta)
    {
        if (l == r)
        {
            remaining[idx] += delta;
            segMax[node] = remaining[idx];
            segSum[node] = remaining[idx];
        }
        else
        {
            int mid = (l + r) >> 1;
            if (idx <= mid) Update(node << 1, l, mid, idx, delta);
            else Update(node << 1 | 1, mid + 1, r, idx, delta);
            Pull(node);
        }
    }

    private int FindFirst(int node, int l, int r, int maxRow, int need)
    {
        if (l > maxRow || segMax[node] < need) return -1;
        if (l == r) return l;
        int mid = (l + r) >> 1;
        int leftRes = FindFirst(node << 1, l, mid, maxRow, need);
        if (leftRes != -1) return leftRes;
        return FindFirst(node << 1 | 1, mid + 1, r, maxRow, need);
    }

    private long QuerySum(int node, int l, int r, int ql, int qr)
    {
        if (ql > r || qr < l) return 0;
        if (ql <= l && r <= qr) return segSum[node];
        int mid = (l + r) >> 1;
        return QuerySum(node << 1, l, mid, ql, qr) + QuerySum(node << 1 | 1, mid + 1, r, ql, qr);
    }

    public int[] Gather(int k, int maxRow)
    {
        int row = FindFirst(1, 0, n - 1, maxRow, k);
        if (row == -1) return new int[0];
        int startSeat = m - remaining[row];
        Update(row, -k);
        return new int[] { row, startSeat };
    }

    public bool Scatter(int k, int maxRow)
    {
        long total = QuerySum(1, 0, n - 1, 0, maxRow);
        if (total < k) return false;

        while (k > 0)
        {
            int row = FindFirst(1, 0, n - 1, maxRow, 1); // first row with at least one seat
            int take = Math.Min(k, remaining[row]);
            Update(row, -take);
            k -= take;
        }
        return true;
    }
}

/**
 * Your BookMyShow object will be instantiated and called as such:
 * BookMyShow obj = new BookMyShow(n, m);
 * int[] param_1 = obj.Gather(k,maxRow);
 * bool param_2 = obj.Scatter(k,maxRow);
 */
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} m
 */
var BookMyShow = function(n, m) {
    this.n = n;
    this.m = m;
    // segment tree size (next power of two)
    this.size = 1;
    while (this.size < n) this.size <<= 1;

    const sz = this.size << 1;
    this.sum = new Array(sz).fill(0);
    this.max = new Array(sz).fill(0);

    // initialize leaves
    for (let i = 0; i < n; ++i) {
        const pos = i + this.size;
        this.sum[pos] = m;
        this.max[pos] = m;
    }
    // build internal nodes
    for (let i = this.size - 1; i > 0; --i) {
        this.sum[i] = this.sum[i << 1] + this.sum[(i << 1) | 1];
        this.max[i] = Math.max(this.max[i << 1], this.max[(i << 1) | 1]);
    }

    // next empty seat index per row
    this.nextSeat = new Array(n).fill(0);
};

/** internal: update leaf idx with remaining seats */
BookMyShow.prototype._update = function(idx, val) {
    let i = idx + this.size;
    this.sum[i] = val;
    this.max[i] = val;
    i >>= 1;
    while (i > 0) {
        this.sum[i] = this.sum[i << 1] + this.sum[(i << 1) | 1];
        this.max[i] = Math.max(this.max[i << 1], this.max[(i << 1) | 1]);
        i >>= 1;
    }
};

/** internal: query max in [l, r] inclusive */
BookMyShow.prototype._queryMax = function(l, r) {
    let res = 0;
    l += this.size;
    r += this.size;
    while (l <= r) {
        if ((l & 1) === 1) {
            res = Math.max(res, this.max[l]);
            ++l;
        }
        if ((r & 1) === 0) {
            res = Math.max(res, this.max[r]);
            --r;
        }
        l >>= 1;
        r >>= 1;
    }
    return res;
};

/** internal: query sum in [l, r] inclusive */
BookMyShow.prototype._querySum = function(l, r) {
    let res = 0;
    l += this.size;
    r += this.size;
    while (l <= r) {
        if ((l & 1) === 1) {
            res += this.sum[l];
            ++l;
        }
        if ((r & 1) === 0) {
            res += this.sum[r];
            --r;
        }
        l >>= 1;
        r >>= 1;
    }
    return res;
};

/** internal: find leftmost index in [nodeL,nodeR] with max >= k and <= limitRow */
BookMyShow.prototype._findFirstGE = function(node, nodeL, nodeR, k, limitRow) {
    if (nodeL > limitRow || this.max[node] < k) return -1;
    if (nodeL === nodeR) return nodeL;
    const mid = (nodeL + nodeR) >> 1;
    const leftRes = this._findFirstGE(node << 1, nodeL, mid, k, limitRow);
    if (leftRes !== -1) return leftRes;
    return this._findFirstGE((node << 1) | 1, mid + 1, nodeR, k, limitRow);
};

/** internal: find leftmost index with remaining > 0 */
BookMyShow.prototype._findFirstPos = function(node, nodeL, nodeR, limitRow) {
    if (nodeL > limitRow || this.max[node] === 0) return -1;
    if (nodeL === nodeR) return nodeL;
    const mid = (nodeL + nodeR) >> 1;
    const leftRes = this._findFirstPos(node << 1, nodeL, mid, limitRow);
    if (leftRes !== -1) return leftRes;
    return this._findFirstPos((node << 1) | 1, mid + 1, nodeR, limitRow);
};

/** 
 * @param {number} k 
 * @param {number} maxRow
 * @return {number[]}
 */
BookMyShow.prototype.gather = function(k, maxRow) {
    if (this._queryMax(0, maxRow) < k) return [];
    const row = this._findFirstGE(1, 0, this.size - 1, k, maxRow);
    const seat = this.nextSeat[row];
    this.nextSeat[row] += k;
    const remaining = this.m - this.nextSeat[row];
    this._update(row, remaining);
    return [row, seat];
};

/** 
 * @param {number} k 
 * @param {number} maxRow
 * @return {boolean}
 */
BookMyShow.prototype.scatter = function(k, maxRow) {
    if (this._querySum(0, maxRow) < k) return false;
    while (k > 0) {
        const row = this._findFirstPos(1, 0, this.size - 1, maxRow);
        // guaranteed to exist
        const avail = this.m - this.nextSeat[row];
        if (avail > k) {
            this.nextSeat[row] += k;
            this._update(row, this.m - this.nextSeat[row]);
            k = 0;
        } else {
            this.nextSeat[row] = this.m;
            this._update(row, 0);
            k -= avail;
        }
    }
    return true;
};

/** 
 * Your BookMyShow object will be instantiated and called as such:
 * var obj = new BookMyShow(n, m)
 * var param_1 = obj.gather(k,maxRow)
 * var param_2 = obj.scatter(k,maxRow)
 */
```

## Typescript

```typescript
class Fenwick {
    private n: number;
    private tree: number[];
    constructor(n: number) {
        this.n = n;
        this.tree = new Array(n + 1).fill(0);
    }
    add(idx: number, delta: number): void {
        for (let i = idx + 1; i <= this.n; i += i & -i) {
            this.tree[i] += delta;
        }
    }
    sum(idx: number): number {
        let res = 0;
        for (let i = idx + 1; i > 0; i -= i & -i) {
            res += this.tree[i];
        }
        return res;
    }
    rangeSum(l: number, r: number): number {
        if (r < l) return 0;
        return this.sum(r) - (l > 0 ? this.sum(l - 1) : 0);
    }
}

class BookMyShow {
    private n: number;
    private m: number;
    private nextSeat: number[];
    private segMax: number[];
    private fenwick: Fenwick;

    constructor(n: number, m: number) {
        this.n = n;
        this.m = m;
        this.nextSeat = new Array(n).fill(0);
        this.segMax = new Array(4 * n).fill(m);
        this.build(1, 0, n - 1);
        this.fenwick = new Fenwick(n);
        for (let i = 0; i < n; ++i) this.fenwick.add(i, m);
    }

    private build(node: number, l: number, r: number): void {
        if (l === r) {
            this.segMax[node] = this.m;
            return;
        }
        const mid = (l + r) >> 1;
        this.build(node << 1, l, mid);
        this.build((node << 1) | 1, mid + 1, r);
        this.segMax[node] = Math.max(this.segMax[node << 1], this.segMax[(node << 1) | 1]);
    }

    private update(node: number, l: number, r: number, idx: number, val: number): void {
        if (l === r) {
            this.segMax[node] = val;
            return;
        }
        const mid = (l + r) >> 1;
        if (idx <= mid) this.update(node << 1, l, mid, idx, val);
        else this.update((node << 1) | 1, mid + 1, r, idx, val);
        this.segMax[node] = Math.max(this.segMax[node << 1], this.segMax[(node << 1) | 1]);
    }

    // find first index in [ql,qr] whose remaining seats >= k
    private findFirst(node: number, l: number, r: number, ql: number, qr: number, k: number): number {
        if (l > qr || r < ql || this.segMax[node] < k) return -1;
        if (l === r) return l;
        const mid = (l + r) >> 1;
        const left = this.findFirst(node << 1, l, mid, ql, qr, k);
        if (left !== -1) return left;
        return this.findFirst((node << 1) | 1, mid + 1, r, ql, qr, k);
    }

    gather(k: number, maxRow: number): number[] {
        const row = this.findFirst(1, 0, this.n - 1, 0, maxRow, k);
        if (row === -1) return [];
        const seatStart = this.nextSeat[row];
        this.nextSeat[row] += k;
        const remaining = this.m - this.nextSeat[row];
        this.update(1, 0, this.n - 1, row, remaining);
        this.fenwick.add(row, -k);
        return [row, seatStart];
    }

    scatter(k: number, maxRow: number): boolean {
        const total = this.fenwick.rangeSum(0, maxRow);
        if (total < k) return false;
        while (k > 0) {
            const row = this.findFirst(1, 0, this.n - 1, 0, maxRow, 1);
            // row is guaranteed to exist
            const avail = this.m - this.nextSeat[row];
            const take = Math.min(avail, k);
            this.nextSeat[row] += take;
            const remaining = this.m - this.nextSeat[row];
            this.update(1, 0, this.n - 1, row, remaining);
            this.fenwick.add(row, -take);
            k -= take;
        }
        return true;
    }
}

/**
 * Your BookMyShow object will be instantiated and called as such:
 * var obj = new BookMyShow(n, m)
 * var param_1 = obj.gather(k,maxRow)
 * var param_2 = obj.scatter(k,maxRow)
 */
```

## Php

```php
class BookMyShow {
    private int $n;
    private int $m;
    /** @var int[] */
    private array $next;
    /** @var int[] */
    private array $maxTree;
    /** @var int[] */
    private array $sumTree;

    /**
     * @param Integer $n
     * @param Integer $m
     */
    function __construct($n, $m) {
        $this->n = $n;
        $this->m = $m;
        $size = 4 * $n + 5;
        $this->maxTree = array_fill(0, $size, 0);
        $this->sumTree = array_fill(0, $size, 0);
        $this->next = array_fill(0, $n, 0);
        $this->build(1, 0, $n - 1);
    }

    private function build(int $idx, int $l, int $r): void {
        if ($l == $r) {
            $this->maxTree[$idx] = $this->m;
            $this->sumTree[$idx] = $this->m;
            return;
        }
        $mid = intdiv($l + $r, 2);
        $this->build($idx * 2, $l, $mid);
        $this->build($idx * 2 + 1, $mid + 1, $r);
        $this->pull($idx);
    }

    private function pull(int $idx): void {
        $this->maxTree[$idx] = max($this->maxTree[$idx * 2], $this->maxTree[$idx * 2 + 1]);
        $this->sumTree[$idx] = $this->sumTree[$idx * 2] + $this->sumTree[$idx * 2 + 1];
    }

    private function updateNode(int $idx, int $l, int $r, int $pos): void {
        if ($l == $r) {
            $remaining = $this->m - $this->next[$pos];
            $this->maxTree[$idx] = $remaining;
            $this->sumTree[$idx] = $remaining;
            return;
        }
        $mid = intdiv($l + $r, 2);
        if ($pos <= $mid) {
            $this->updateNode($idx * 2, $l, $mid, $pos);
        } else {
            $this->updateNode($idx * 2 + 1, $mid + 1, $r, $pos);
        }
        $this->pull($idx);
    }

    private function queryMax(int $idx, int $l, int $r, int $ql, int $qr): int {
        if ($ql > $r || $qr < $l) return -1;
        if ($ql <= $l && $r <= $qr) return $this->maxTree[$idx];
        $mid = intdiv($l + $r, 2);
        $left = $this->queryMax($idx * 2, $l, $mid, $ql, $qr);
        $right = $this->queryMax($idx * 2 + 1, $mid + 1, $r, $ql, $qr);
        return max($left, $right);
    }

    private function querySum(int $idx, int $l, int $r, int $ql, int $qr): int {
        if ($ql > $r || $qr < $l) return 0;
        if ($ql <= $l && $r <= $qr) return $this->sumTree[$idx];
        $mid = intdiv($l + $r, 2);
        $left = $this->querySum($idx * 2, $l, $mid, $ql, $qr);
        $right = $this->querySum($idx * 2 + 1, $mid + 1, $r, $ql, $qr);
        return $left + $right;
    }

    private function findRow(int $idx, int $l, int $r, int $ql, int $qr, int $k): int {
        if ($ql > $r || $qr < $l || $this->maxTree[$idx] < $k) return -1;
        if ($l == $r) return $l;
        $mid = intdiv($l + $r, 2);
        $leftRes = $this->findRow($idx * 2, $l, $mid, $ql, $qr, $k);
        if ($leftRes != -1) return $leftRes;
        return $this->findRow($idx * 2 + 1, $mid + 1, $r, $ql, $qr, $k);
    }

    /**
     * @param Integer $k
     * @param Integer $maxRow
     * @return Integer[]
     */
    function gather($k, $maxRow) {
        if ($this->queryMax(1, 0, $this->n - 1, 0, $maxRow) < $k) {
            return [];
        }
        $row = $this->findRow(1, 0, $this->n - 1, 0, $maxRow, $k);
        $seat = $this->next[$row];
        $this->next[$row] += $k;
        $this->updateNode(1, 0, $this->n - 1, $row);
        return [$row, $seat];
    }

    /**
     * @param Integer $k
     * @param Integer $maxRow
     * @return Boolean
     */
    function scatter($k, $maxRow) {
        if ($this->querySum(1, 0, $this->n - 1, 0, $maxRow) < $k) {
            return false;
        }
        while ($k > 0) {
            $row = $this->findRow(1, 0, $this->n - 1, 0, $maxRow, 1);
            // $row is guaranteed to exist
            $available = $this->m - $this->next[$row];
            $take = min($available, $k);
            $this->next[$row] += $take;
            $this->updateNode(1, 0, $this->n - 1, $row);
            $k -= $take;
        }
        return true;
    }
}

/**
 * Your BookMyShow object will be instantiated and called as such:
 * $obj = new BookMyShow($n, $m);
 * $ret_1 = $obj->gather($k, $maxRow);
 * $ret_2 = $obj->scatter($k, $maxRow);
 */
```

## Swift

```swift
class BookMyShow {
    private var n: Int
    private var m: Int
    private var nextSeat: [Int]
    private var bit: [Int64]
    private var segMax: [Int]
    private var cur: Int = 0

    init(_ n: Int, _ m: Int) {
        self.n = n
        self.m = m
        self.nextSeat = Array(repeating: 0, count: n)
        self.bit = Array(repeating: 0, count: n + 2)
        self.segMax = Array(repeating: 0, count: 4 * n)
        build(1, 0, n - 1)
        for i in 0..<n {
            bitAdd(i, Int64(m))
        }
    }

    private func build(_ node: Int, _ l: Int, _ r: Int) {
        if l == r {
            segMax[node] = m
        } else {
            let mid = (l + r) >> 1
            build(node << 1, l, mid)
            build(node << 1 | 1, mid + 1, r)
            segMax[node] = max(segMax[node << 1], segMax[node << 1 | 1])
        }
    }

    private func bitAdd(_ idx: Int, _ delta: Int64) {
        var i = idx + 1
        while i <= n {
            bit[i] += delta
            i += i & -i
        }
    }

    private func bitSum(_ idx: Int) -> Int64 {
        if idx < 0 { return 0 }
        var res: Int64 = 0
        var i = idx + 1
        while i > 0 {
            res += bit[i]
            i -= i & -i
        }
        return res
    }

    private func segUpdate(_ node: Int, _ l: Int, _ r: Int, _ idx: Int, _ value: Int) {
        if l == r {
            segMax[node] = value
        } else {
            let mid = (l + r) >> 1
            if idx <= mid {
                segUpdate(node << 1, l, mid, idx, value)
            } else {
                segUpdate(node << 1 | 1, mid + 1, r, idx, value)
            }
            segMax[node] = max(segMax[node << 1], segMax[node << 1 | 1])
        }
    }

    private func segQuery(_ node: Int, _ l: Int, _ r: Int, _ ql: Int, _ qr: Int) -> Int {
        if ql > r || qr < l { return -1 }
        if ql <= l && r <= qr { return segMax[node] }
        let mid = (l + r) >> 1
        let left = segQuery(node << 1, l, mid, ql, qr)
        let right = segQuery(node << 1 | 1, mid + 1, r, ql, qr)
        return max(left, right)
    }

    private func findFirst(_ node: Int, _ l: Int, _ r: Int, _ limit: Int, _ k: Int) -> Int? {
        if l > limit || segMax[node] < k { return nil }
        if l == r { return l }
        let mid = (l + r) >> 1
        if let leftRes = findFirst(node << 1, l, mid, limit, k) {
            return leftRes
        } else {
            return findFirst(node << 1 | 1, mid + 1, r, limit, k)
        }
    }

    func gather(_ k: Int, _ maxRow: Int) -> [Int] {
        if maxRow < 0 { return [] }
        let maxAvail = segQuery(1, 0, n - 1, 0, maxRow)
        if maxAvail < k { return [] }
        guard let row = findFirst(1, 0, n - 1, maxRow, k) else { return [] }
        let seatStart = nextSeat[row]
        nextSeat[row] += k
        let remaining = m - nextSeat[row]
        segUpdate(1, 0, n - 1, row, remaining)
        bitAdd(row, Int64(-k))
        if row == cur && remaining == 0 {
            while cur < n && (m - nextSeat[cur]) == 0 { cur += 1 }
        }
        return [row, seatStart]
    }

    func scatter(_ k: Int, _ maxRow: Int) -> Bool {
        let total = bitSum(maxRow)
        if total < Int64(k) { return false }
        var remainingK = k
        while remainingK > 0 {
            while cur < n && (m - nextSeat[cur]) == 0 { cur += 1 }
            if cur > maxRow { break }
            let avail = m - nextSeat[cur]
            let take = min(avail, remainingK)
            nextSeat[cur] += take
            let newRem = m - nextSeat[cur]
            segUpdate(1, 0, n - 1, cur, newRem)
            bitAdd(cur, Int64(-take))
            remainingK -= take
            if newRem == 0 { cur += 1 }
        }
        return true
    }
}

/**
 * Your BookMyShow object will be instantiated and called as such:
 * let obj = BookMyShow(n, m)
 * let ret_1: [Int] = obj.gather(k, maxRow)
 * let ret_2: Bool = obj.scatter(k, maxRow)
 */
```

## Kotlin

```kotlin
import kotlin.math.max
import kotlin.math.min

class BookMyShow(n: Int, m: Int) {
    private val rows = n
    private val seatsPerRow = m
    private val seg = SegmentTree(rows, seatsPerRow)

    fun gather(k: Int, maxRow: Int): IntArray {
        val row = seg.findFirst(maxRow, k)
        if (row == -1) return intArrayOf()
        val curAvail = seg.getAvail(row)
        val startSeat = seatsPerRow - curAvail
        seg.add(row, k)
        return intArrayOf(row, startSeat)
    }

    fun scatter(k: Int, maxRow: Int): Boolean {
        if (seg.querySum(0, maxRow) < k.toLong()) return false
        var remaining = k
        while (remaining > 0) {
            val row = seg.findFirst(maxRow, 1)
            val avail = seg.getAvail(row)
            val take = min(avail, remaining)
            seg.add(row, take)
            remaining -= take
        }
        return true
    }

    private class SegmentTree(private val n: Int, private val m: Int) {
        private val maxArr = IntArray(4 * n)
        private val sumArr = LongArray(4 * n)

        init {
            build(1, 0, n - 1)
        }

        private fun build(node: Int, l: Int, r: Int) {
            if (l == r) {
                maxArr[node] = m
                sumArr[node] = m.toLong()
            } else {
                val mid = (l + r) ushr 1
                build(node shl 1, l, mid)
                build(node shl 1 or 1, mid + 1, r)
                pull(node)
            }
        }

        private fun pull(node: Int) {
            maxArr[node] = max(maxArr[node shl 1], maxArr[node shl 1 or 1])
            sumArr[node] = sumArr[node shl 1] + sumArr[node shl 1 or 1]
        }

        fun add(idx: Int, delta: Int) {
            update(1, 0, n - 1, idx, delta)
        }

        private fun update(node: Int, l: Int, r: Int, idx: Int, delta: Int) {
            if (l == r) {
                maxArr[node] -= delta
                sumArr[node] -= delta.toLong()
            } else {
                val mid = (l + r) ushr 1
                if (idx <= mid) update(node shl 1, l, mid, idx, delta)
                else update(node shl 1 or 1, mid + 1, r, idx, delta)
                pull(node)
            }
        }

        fun querySum(ql: Int, qr: Int): Long {
            return querySum(1, 0, n - 1, ql, qr)
        }

        private fun querySum(node: Int, l: Int, r: Int, ql: Int, qr: Int): Long {
            if (qr < l || ql > r) return 0L
            if (ql <= l && r <= qr) return sumArr[node]
            val mid = (l + r) ushr 1
            return querySum(node shl 1, l, mid, ql, qr) +
                    querySum(node shl 1 or 1, mid + 1, r, ql, qr)
        }

        fun getAvail(idx: Int): Int {
            return queryMax(1, 0, n - 1, idx, idx)
        }

        private fun queryMax(node: Int, l: Int, r: Int, ql: Int, qr: Int): Int {
            if (qr < l || ql > r) return -1
            if (ql <= l && r <= qr) return maxArr[node]
            val mid = (l + r) ushr 1
            val left = queryMax(node shl 1, l, mid, ql, qr)
            val right = queryMax(node shl 1 or 1, mid + 1, r, ql, qr)
            return max(left, right)
        }

        fun findFirst(limit: Int, need: Int): Int {
            return findFirst(1, 0, n - 1, limit, need)
        }

        private fun findFirst(node: Int, l: Int, r: Int, limit: Int, need: Int): Int {
            if (l > limit || maxArr[node] < need) return -1
            if (l == r) return l
            val mid = (l + r) ushr 1
            var res = findFirst(node shl 1, l, mid, limit, need)
            if (res == -1) {
                res = findFirst(node shl 1 or 1, mid + 1, r, limit, need)
            }
            return res
        }
    }
}

/**
 * Your BookMyShow object will be instantiated and called as such:
 * var obj = BookMyShow(n, m)
 * var param_1 = obj.gather(k,maxRow)
 * var param_2 = obj.scatter(k,maxRow)
 */
```

## Dart

```dart
class BookMyShow {
  late int n;
  late int m;
  late List<int> _rem;
  late List<int> _segMax;
  late List<int> _segSum;

  BookMyShow(int n, int m) {
    this.n = n;
    this.m = m;
    _rem = List.filled(n, m);
    _segMax = List.filled(4 * n, 0);
    _segSum = List.filled(4 * n, 0);
    _build(1, 0, n - 1);
  }

  void _build(int node, int l, int r) {
    if (l == r) {
      _segMax[node] = m;
      _segSum[node] = m;
    } else {
      int mid = (l + r) >> 1;
      _build(node << 1, l, mid);
      _build((node << 1) | 1, mid + 1, r);
      _segMax[node] = _segMax[node << 1] > _segMax[(node << 1) | 1]
          ? _segMax[node << 1]
          : _segMax[(node << 1) | 1];
      _segSum[node] = _segSum[node << 1] + _segSum[(node << 1) | 1];
    }
  }

  void _update(int node, int l, int r, int idx, int val) {
    if (l == r) {
      _segMax[node] = val;
      _segSum[node] = val;
    } else {
      int mid = (l + r) >> 1;
      if (idx <= mid) {
        _update(node << 1, l, mid, idx, val);
      } else {
        _update((node << 1) | 1, mid + 1, r, idx, val);
      }
      _segMax[node] = _segMax[node << 1] > _segMax[(node << 1) | 1]
          ? _segMax[node << 1]
          : _segMax[(node << 1) | 1];
      _segSum[node] = _segSum[node << 1] + _segSum[(node << 1) | 1];
    }
  }

  int _querySum(int node, int l, int r, int ql, int qr) {
    if (ql > r || qr < l) return 0;
    if (ql <= l && r <= qr) return _segSum[node];
    int mid = (l + r) >> 1;
    return _querySum(node << 1, l, mid, ql, qr) +
        _querySum((node << 1) | 1, mid + 1, r, ql, qr);
  }

  int _findFirstGE(int node, int l, int r, int maxRow, int k) {
    if (l > maxRow || _segMax[node] < k) return -1;
    if (l == r) return l;
    int mid = (l + r) >> 1;
    int left = _findFirstGE(node << 1, l, mid, maxRow, k);
    if (left != -1) return left;
    return _findFirstGE((node << 1) | 1, mid + 1, r, maxRow, k);
  }

  int _findFirstPos(int node, int l, int r, int maxRow) {
    if (l > maxRow || _segMax[node] == 0) return -1;
    if (l == r) return l;
    int mid = (l + r) >> 1;
    int left = _findFirstPos(node << 1, l, mid, maxRow);
    if (left != -1) return left;
    return _findFirstPos((node << 1) | 1, mid + 1, r, maxRow);
  }

  List<int> gather(int k, int maxRow) {
    int row = _findFirstGE(1, 0, n - 1, maxRow, k);
    if (row == -1) return [];
    int startSeat = m - _rem[row];
    _rem[row] -= k;
    _update(1, 0, n - 1, row, _rem[row]);
    return [row, startSeat];
  }

  bool scatter(int k, int maxRow) {
    int total = _querySum(1, 0, n - 1, 0, maxRow);
    if (total < k) return false;
    while (k > 0) {
      int row = _findFirstPos(1, 0, n - 1, maxRow);
      int take = k < _rem[row] ? k : _rem[row];
      _rem[row] -= take;
      _update(1, 0, n - 1, row, _rem[row]);
      k -= take;
    }
    return true;
  }
}

/**
 * Your BookMyShow object will be instantiated and called as such:
 * BookMyShow obj = BookMyShow(n, m);
 * List<int> param1 = obj.gather(k,maxRow);
 * bool param2 = obj.scatter(k,maxRow);
 */
```

## Golang

```go
type BookMyShow struct {
	n      int
	m      int64
	remain []int64
	seg    []int64
	bit    []int64
	parent []int
}

func Constructor(n int, m int) BookMyShow {
	b := BookMyShow{
		n:      n,
		m:      int64(m),
		remain: make([]int64, n),
		seg:    make([]int64, 4*n),
		bit:    make([]int64, n+2),
		parent: make([]int, n+1),
	}
	for i := 0; i < n; i++ {
		b.remain[i] = b.m
		b.addBIT(i, b.m)
	}
	b.build(1, 0, n-1)
	for i := 0; i <= n; i++ {
		b.parent[i] = i
	}
	return b
}

// segment tree build
func (b *BookMyShow) build(node, l, r int) {
	if l == r {
		b.seg[node] = b.remain[l]
		return
	}
	mid := (l + r) >> 1
	b.build(node<<1, l, mid)
	b.build(node<<1|1, mid+1, r)
	if b.seg[node<<1] > b.seg[node<<1|1] {
		b.seg[node] = b.seg[node<<1]
	} else {
		b.seg[node] = b.seg[node<<1|1]
	}
}

// segment tree point update
func (b *BookMyShow) updateSeg(node, l, r, idx int, val int64) {
	if l == r {
		b.seg[node] = val
		return
	}
	mid := (l + r) >> 1
	if idx <= mid {
		b.updateSeg(node<<1, l, mid, idx, val)
	} else {
		b.updateSeg(node<<1|1, mid+1, r, idx, val)
	}
	if b.seg[node<<1] > b.seg[node<<1|1] {
		b.seg[node] = b.seg[node<<1]
	} else {
		b.seg[node] = b.seg[node<<1|1]
	}
}

func (b *BookMyShow) update(idx int, val int64) {
	b.updateSeg(1, 0, b.n-1, idx, val)
}

// segment tree range max query
func (b *BookMyShow) queryMax(node, l, r, ql, qr int) int64 {
	if ql > r || qr < l {
		return -1
	}
	if ql <= l && r <= qr {
		return b.seg[node]
	}
	mid := (l + r) >> 1
	left := b.queryMax(node<<1, l, mid, ql, qr)
	right := b.queryMax(node<<1|1, mid+1, r, ql, qr)
	if left > right {
		return left
	}
	return right
}

// find first index with value >= k in [ql,qr]
func (b *BookMyShow) findFirst(node, l, r, ql, qr int, k int64) int {
	if ql > r || qr < l || b.seg[node] < k {
		return -1
	}
	if l == r {
		return l
	}
	mid := (l + r) >> 1
	res := b.findFirst(node<<1, l, mid, ql, qr, k)
	if res != -1 {
		return res
	}
	return b.findFirst(node<<1|1, mid+1, r, ql, qr, k)
}

// Fenwick tree add
func (b *BookMyShow) addBIT(idx int, delta int64) {
	i := idx + 1
	for i < len(b.bit) {
		b.bit[i] += delta
		i += i & -i
	}
}

// Fenwick prefix sum [0..idx]
func (b *BookMyShow) sumBIT(idx int) int64 {
	if idx < 0 {
		return 0
	}
	res := int64(0)
	i := idx + 1
	for i > 0 {
		res += b.bit[i]
		i -= i & -i
	}
	return res
}

// DSU find next row with remaining seats
func (b *BookMyShow) find(x int) int {
	if x >= b.n {
		return b.n
	}
	if b.parent[x] != x {
		b.parent[x] = b.find(b.parent[x])
	}
	return b.parent[x]
}

func (b *BookMyShow) Gather(k int, maxRow int) []int {
	if maxRow >= b.n {
		maxRow = b.n - 1
	}
	if b.queryMax(1, 0, b.n-1, 0, maxRow) < int64(k) {
		return []int{}
	}
	idx := b.findFirst(1, 0, b.n-1, 0, maxRow, int64(k))
	startSeat := int(b.m - b.remain[idx])
	b.remain[idx] -= int64(k)
	b.update(idx, b.remain[idx])
	b.addBIT(idx, -int64(k))
	return []int{idx, startSeat}
}

func (b *BookMyShow) Scatter(k int, maxRow int) bool {
	if maxRow >= b.n {
		maxRow = b.n - 1
	}
	total := b.sumBIT(maxRow)
	if total < int64(k) {
		return false
	}
	remaining := int64(k)
	row := b.find(0)
	for remaining > 0 && row <= maxRow {
		avail := b.remain[row]
		if avail == 0 {
			row = b.find(row + 1)
			continue
		}
		take := remaining
		if take > avail {
			take = avail
		}
		b.remain[row] -= take
		b.update(row, b.remain[row])
		b.addBIT(row, -take)
		remaining -= take
		if b.remain[row] == 0 {
			b.parent[row] = b.find(row + 1)
		}
		row = b.find(row) // move to next candidate
	}
	return true
}

/**
 * Your BookMyShow object will be instantiated and called as such:
 * obj := Constructor(n, m);
 * param_1 := obj.Gather(k,maxRow);
 * param_2 := obj.Scatter(k,maxRow);
 */
```

## Ruby

```ruby
class SegmentTree
  def initialize(arr)
    @n = arr.length
    @size = 1
    while @size < @n
      @size <<= 1
    end
    @max = Array.new(@size * 2, 0)
    @sum = Array.new(@size * 2, 0)
    (0...@n).each do |i|
      @max[@size + i] = arr[i]
      @sum[@size + i] = arr[i]
    end
    (@size - 1).downto(1) do |i|
      @max[i] = [@max[i * 2], @max[i * 2 + 1]].max
      @sum[i] = @sum[i * 2] + @sum[i * 2 + 1]
    end
  end

  def update(idx, val)
    pos = @size + idx
    @max[pos] = val
    @sum[pos] = val
    pos >>= 1
    while pos >= 1
      @max[pos] = [@max[pos * 2], @max[pos * 2 + 1]].max
      @sum[pos] = @sum[pos * 2] + @sum[pos * 2 + 1]
      pos >>= 1
    end
  end

  def query_max(l, r)
    return 0 if l > r
    l += @size
    r += @size
    res = 0
    while l <= r
      if (l & 1) == 1
        res = [res, @max[l]].max
        l += 1
      end
      if (r & 1) == 0
        res = [res, @max[r]].max
        r -= 1
      end
      l >>= 1
      r >>= 1
    end
    res
  end

  def query_sum(l, r)
    return 0 if l > r
    l += @size
    r += @size
    res = 0
    while l <= r
      if (l & 1) == 1
        res += @sum[l]
        l += 1
      end
      if (r & 1) == 0
        res += @sum[r]
        r -= 1
      end
      l >>= 1
      r >>= 1
    end
    res
  end

  def find_first(k, ql, qr)
    return -1 if query_max(ql, qr) < k
    _find_first(1, 0, @size - 1, ql, qr, k)
  end

  private

  def _find_first(node, l, r, ql, qr, k)
    return -1 if r < ql || l > qr || @max[node] < k
    return l if l == r
    mid = (l + r) >> 1
    left = _find_first(node * 2, l, mid, ql, qr, k)
    return left unless left == -1
    _find_first(node * 2 + 1, mid + 1, r, ql, qr, k)
  end
end

class BookMyShow
  def initialize(n, m)
    @n = n
    @m = m
    @rem = Array.new(n, m)
    @seg = SegmentTree.new(@rem.dup)
    @cur_scatter_row = 0
  end

  def gather(k, max_row)
    row = @seg.find_first(k, 0, max_row)
    return [] if row == -1 || row >= @n
    seat = @m - @rem[row]
    @rem[row] -= k
    @seg.update(row, @rem[row])
    [row, seat]
  end

  def scatter(k, max_row)
    total = @seg.query_sum(0, max_row)
    return false if total < k
    while k > 0 && @cur_scatter_row <= max_row
      if @rem[@cur_scatter_row] == 0
        @cur_scatter_row += 1
        next
      end
      take = [@rem[@cur_scatter_row], k].min
      @rem[@cur_scatter_row] -= take
      @seg.update(@cur_scatter_row, @rem[@cur_scatter_row])
      k -= take
      @cur_scatter_row += 1 if @rem[@cur_scatter_row] == 0
    end
    true
  end
end
```

## Scala

```scala
class BookMyShow(_n: Int, _m: Int) {
  private val n = _n
  private val m = _m.toLong
  private val rem = Array.fill[Long](n)(m)

  private val maxTree = new Array[Long](4 * n)
  private val sumTree = new Array[Long](4 * n)

  build(1, 0, n - 1)

  private def build(node: Int, l: Int, r: Int): Unit = {
    if (l == r) {
      maxTree(node) = m
      sumTree(node) = m
    } else {
      val mid = (l + r) >>> 1
      build(node << 1, l, mid)
      build(node << 1 | 1, mid + 1, r)
      pull(node)
    }
  }

  private def pull(node: Int): Unit = {
    maxTree(node) = math.max(maxTree(node << 1), maxTree(node << 1 | 1))
    sumTree(node) = sumTree(node << 1) + sumTree(node << 1 | 1)
  }

  private def update(node: Int, l: Int, r: Int, idx: Int, value: Long): Unit = {
    if (l == r) {
      maxTree(node) = value
      sumTree(node) = value
    } else {
      val mid = (l + r) >>> 1
      if (idx <= mid) update(node << 1, l, mid, idx, value)
      else update(node << 1 | 1, mid + 1, r, idx, value)
      pull(node)
    }
  }

  private def queryMax(node: Int, l: Int, r: Int, ql: Int, qr: Int): Long = {
    if (ql > r || qr < l) return Long.MinValue
    if (ql <= l && r <= qr) return maxTree(node)
    val mid = (l + r) >>> 1
    math.max(
      queryMax(node << 1, l, mid, ql, qr),
      queryMax(node << 1 | 1, mid + 1, r, ql, qr)
    )
  }

  private def querySum(node: Int, l: Int, r: Int, ql: Int, qr: Int): Long = {
    if (ql > r || qr < l) return 0L
    if (ql <= l && r <= qr) return sumTree(node)
    val mid = (l + r) >>> 1
    querySum(node << 1, l, mid, ql, qr) + querySum(node << 1 | 1, mid + 1, r, ql, qr)
  }

  private def findFirstWithAtLeastK(node: Int, l: Int, r: Int, ql: Int, qr: Int, k: Long): Int = {
    if (ql > r || qr < l || maxTree(node) < k) return -1
    if (l == r) return l
    val mid = (l + r) >>> 1
    val leftRes = findFirstWithAtLeastK(node << 1, l, mid, ql, qr, k)
    if (leftRes != -1) leftRes else findFirstWithAtLeastK(node << 1 | 1, mid + 1, r, ql, qr, k)
  }

  private def findFirstPositive(node: Int, l: Int, r: Int, ql: Int, qr: Int): Int = {
    if (ql > r || qr < l || sumTree(node) == 0L) return -1
    if (l == r) return l
    val mid = (l + r) >>> 1
    val leftRes = findFirstPositive(node << 1, l, mid, ql, qr)
    if (leftRes != -1) leftRes else findFirstPositive(node << 1 | 1, mid + 1, r, ql, qr)
  }

  def gather(k: Int, maxRow: Int): Array[Int] = {
    val kk = k.toLong
    if (maxRow < 0) return Array.empty[Int]
    val maxAvail = queryMax(1, 0, n - 1, 0, maxRow)
    if (maxAvail < kk) return Array.empty[Int]

    val row = findFirstWithAtLeastK(1, 0, n - 1, 0, maxRow, kk)
    val startSeat = (m - rem(row)).toInt
    rem(row) -= kk
    update(1, 0, n - 1, row, rem(row))
    Array(row, startSeat)
  }

  def scatter(k: Int, maxRow: Int): Boolean = {
    val kk = k.toLong
    if (maxRow < 0) return false
    val totalAvail = querySum(1, 0, n - 1, 0, maxRow)
    if (totalAvail < kk) return false

    var remaining = kk
    var curL = 0
    while (remaining > 0) {
      val row = findFirstPositive(1, 0, n - 1, curL, maxRow)
      // row is guaranteed to exist
      val take = math.min(rem(row), remaining)
      rem(row) -= take
      update(1, 0, n - 1, row, rem(row))
      remaining -= take
      if (rem(row) == 0) curL = row + 1
    }
    true
  }
}

/**
 * Your BookMyShow object will be instantiated and called as such:
 * val obj = new BookMyShow(n, m)
 * val param_1 = obj.gather(k,maxRow)
 * val param_2 = obj.scatter(k,maxRow)
 */
```

## Rust

```rust
struct BookMyShow {
    n: usize,
    m: i64,
    seg_sum: Vec<i64>,
    seg_max: Vec<i64>,
    rem: Vec<i64>,
}

impl BookMyShow {
    fn new(n: i32, m: i32) -> Self {
        let n_usize = n as usize;
        let m_i64 = m as i64;
        let mut obj = BookMyShow {
            n: n_usize,
            m: m_i64,
            seg_sum: vec![0; 4 * n_usize],
            seg_max: vec![0; 4 * n_usize],
            rem: vec![m_i64; n_usize],
        };
        obj.build(1, 0, n_usize - 1);
        obj
    }

    fn build(&mut self, node: usize, l: usize, r: usize) {
        if l == r {
            self.seg_sum[node] = self.m;
            self.seg_max[node] = self.m;
        } else {
            let mid = (l + r) / 2;
            self.build(node * 2, l, mid);
            self.build(node * 2 + 1, mid + 1, r);
            self.pull(node);
        }
    }

    fn pull(&mut self, node: usize) {
        self.seg_sum[node] = self.seg_sum[node * 2] + self.seg_sum[node * 2 + 1];
        self.seg_max[node] = self.seg_max[node * 2].max(self.seg_max[node * 2 + 1]);
    }

    fn update(&mut self, idx: usize, val: i64) {
        self._update(1, 0, self.n - 1, idx, val);
    }

    fn _update(&mut self, node: usize, l: usize, r: usize, idx: usize, val: i64) {
        if l == r {
            self.seg_sum[node] = val;
            self.seg_max[node] = val;
        } else {
            let mid = (l + r) / 2;
            if idx <= mid {
                self._update(node * 2, l, mid, idx, val);
            } else {
                self._update(node * 2 + 1, mid + 1, r, idx, val);
            }
            self.pull(node);
        }
    }

    fn query_sum(&self, ql: usize, qr: usize) -> i64 {
        self._query_sum(1, 0, self.n - 1, ql, qr)
    }

    fn _query_sum(&self, node: usize, l: usize, r: usize, ql: usize, qr: usize) -> i64 {
        if ql > r || qr < l {
            return 0;
        }
        if ql <= l && r <= qr {
            return self.seg_sum[node];
        }
        let mid = (l + r) / 2;
        self._query_sum(node * 2, l, mid, ql, qr)
            + self._query_sum(node * 2 + 1, mid + 1, r, ql, qr)
    }

    fn find_first_ge(&self, need: i64, max_row: usize) -> Option<usize> {
        self._find_first_ge(1, 0, self.n - 1, need, max_row)
    }

    fn _find_first_ge(
        &self,
        node: usize,
        l: usize,
        r: usize,
        need: i64,
        max_row: usize,
    ) -> Option<usize> {
        if l > max_row || self.seg_max[node] < need {
            return None;
        }
        if l == r {
            return Some(l);
        }
        let mid = (l + r) / 2;
        if let Some(res) = self._find_first_ge(node * 2, l, mid, need, max_row) {
            return Some(res);
        }
        self._find_first_ge(node * 2 + 1, mid + 1, r, need, max_row)
    }

    fn gather(&mut self, k: i32, max_row: i32) -> Vec<i32> {
        let need = k as i64;
        let max_usize = max_row as usize;
        if let Some(row) = self.find_first_ge(need, max_usize) {
            let start_seat = (self.m - self.rem[row]) as i32;
            self.rem[row] -= need;
            self.update(row, self.rem[row]);
            vec![row as i32, start_seat]
        } else {
            Vec::new()
        }
    }

    fn scatter(&mut self, k: i32, max_row: i32) -> bool {
        let mut need = k as i64;
        let max_usize = max_row as usize;
        if self.query_sum(0, max_usize) < need {
            return false;
        }
        while need > 0 {
            // find first row with at least one seat left
            let row_opt = self.find_first_ge(1, max_usize);
            match row_opt {
                Some(row) => {
                    let take = if self.rem[row] >= need { need } else { self.rem[row] };
                    self.rem[row] -= take;
                    self.update(row, self.rem[row]);
                    need -= take;
                }
                None => break,
            }
        }
        true
    }
}

/**
 * Your BookMyShow object will be instantiated and called as such:
 * let obj = BookMyShow::new(n, m);
 * let ret_1: Vec<i32> = obj.gather(k, maxRow);
 * let ret_2: bool = obj.scatter(k, maxRow);
 */
```

## Racket

```racket
(define book-my-show%
  (class object%
    (init-field n m)
    (super-new)

    ;; state
    (define used (make-vector n 0))
    (define seg-max (make-vector (* 4 n) 0))
    (define seg-sum (make-vector (* 4 n) 0))

    ;; point update: set remaining seats of row pos to val
    (define (update idx l r pos val)
      (if (= l r)
          (begin
            (vector-set! seg-max idx val)
            (vector-set! seg-sum idx val))
          (let* ((mid (quotient (+ l r) 2)))
            (if (<= pos mid)
                (update (* idx 2) l mid pos val)
                (update (+ idx 1) (+ mid 1) r pos val))
            (vector-set! seg-max idx
                         (max (vector-ref seg-max (* idx 2))
                              (vector-ref seg-max (+ idx 1))))
            (vector-set! seg-sum idx
                         (+ (vector-ref seg-sum (* idx 2))
                            (vector-ref seg-sum (+ idx 1)))))))

    ;; build initial tree (all rows have m seats free)
    (for ([i (in-range n)])
      (update 1 0 (- n 1) i m))

    ;; range max query
    (define (query-max idx l r ql qr)
      (if (or (> ql r) (< qr l))
          -1
          (if (and (<= ql l) (>= qr r))
              (vector-ref seg-max idx)
              (let* ((mid (quotient (+ l r) 2))
                     (left (query-max (* idx 2) l mid ql qr))
                     (right (query-max (+ idx 1) (+ mid 1) r ql qr)))
                (max left right)))))

    ;; range sum query
    (define (query-sum idx l r ql qr)
      (if (or (> ql r) (< qr l))
          0
          (if (and (<= ql l) (>= qr r))
              (vector-ref seg-sum idx)
              (let* ((mid (quotient (+ l r) 2))
                     (left (query-sum (* idx 2) l mid ql qr))
                     (right (query-sum (+ idx 1) (+ mid 1) r ql qr)))
                (+ left right)))))

    ;; find first row <= maxRow with remaining >= k
    (define (find-first idx l r maxRow k)
      (if (> l maxRow)
          -1
          (let ((mx (vector-ref seg-max idx)))
            (if (< mx k)
                -1
                (if (= l r)
                    l
                    (let* ((mid (quotient (+ l r) 2))
                           (leftRes (find-first (* idx 2) l mid maxRow k)))
                      (if (>= leftRes 0)
                          leftRes
                          (find-first (+ idx 1) (+ mid 1) r maxRow k))))))))

    ;; public methods
    (define/public (gather k max-row)
      (let ((row (find-first 1 0 (- n 1) max-row k)))
        (if (= row -1)
            '()
            (let* ((start (vector-ref used row))
                   (new-used (+ start k))
                   (remaining (- m new-used)))
              (vector-set! used row new-used)
              (update 1 0 (- n 1) row remaining)
              (list row start)))))

    (define/public (scatter k max-row)
      (let ((total (query-sum 1 0 (- n 1) 0 max-row)))
        (if (< total k)
            #f
            (let loop ((remaining k))
              (if (= remaining 0)
                  #t
                  (let* ((row (find-first 1 0 (- n 1) max-row 1))
                         (avail (- m (vector-ref used row)))
                         (take (if (< avail remaining) avail remaining))
                         (new-used (+ (vector-ref used row) take))
                         (rem-after (- m new-used)))
                    (vector-set! used row new-used)
                    (update 1 0 (- n 1) row rem-after)
                    (loop (- remaining take)))))))))
```

## Erlang

```erlang
-module(book_my_show).
-export([book_my_show_init_/2,
         book_my_show_gather/2,
         book_my_show_scatter/2]).

%% Initialization
-spec book_my_show_init_(N :: integer(), M :: integer()) -> any().
book_my_show_init_(N, M) ->
    put(n, N),
    put(m, M),
    put(cur_scatter, 0),

    %% Clean previous tables if they exist
    (case ets:info(used_tab) of undefined -> ok; _ -> ets:delete(used_tab) end),
    UsedTab = ets:new(used_tab, [named_table, public, set]),

    (case ets:info(seg_sum) of undefined -> ok; _ -> ets:delete(seg_sum) end),
    SegSum = ets:new(seg_sum, [named_table, public, set]),

    (case ets:info(seg_max) of undefined -> ok; _ -> ets:delete(seg_max) end),
    SegMax = ets:new(seg_max, [named_table, public, set]),

    build(1, 0, N - 1, M),
    ok.

%% Gather operation
-spec book_my_show_gather(K :: integer(), MaxRow :: integer()) -> [integer()].
book_my_show_gather(K, MaxRow) ->
    N = get(n),
    MaxInRange = query_max(1, 0, N - 1, 0, MaxRow),
    if MaxInRange < K ->
            [];
       true ->
            Row = find_first(1, 0, N - 1, K, MaxRow),
            Used = get_used(Row),
            StartSeat = Used,
            NewUsed = Used + K,
            NewFree = get(m) - NewUsed,
            ets:insert(used_tab, {Row, NewUsed}),
            update_row(Row, NewFree),
            [Row, StartSeat]
    end.

%% Scatter operation
-spec book_my_show_scatter(K :: integer(), MaxRow :: integer()) -> boolean().
book_my_show_scatter(K, MaxRow) ->
    N = get(n),
    SumInRange = query_sum(1, 0, N - 1, 0, MaxRow),
    if SumInRange < K ->
            false;
       true ->
            Cur = get(cur_scatter),
            case scatter_allocate(K, MaxRow, Cur) of
                {true, NewCur} ->
                    put(cur_scatter, NewCur),
                    true;
                false -> false
            end
    end.

%% ---------- Helper Functions ----------
build(_Idx, L, R, _M) when L > R -> ok;
build(Idx, L, R, M) ->
    if L == R ->
            ets:insert(seg_sum, {Idx, M}),
            ets:insert(seg_max, {Idx, M});
       true ->
            Mid = (L + R) div 2,
            Left = Idx * 2,
            Right = Idx * 2 + 1,
            build(Left, L, Mid, M),
            build(Right, Mid + 1, R, M),

            {_, SumL} = hd(ets:lookup(seg_sum, Left)),
            {_, SumR} = hd(ets:lookup(seg_sum, Right)),
            ets:insert(seg_sum, {Idx, SumL + SumR}),

            {_, MaxL} = hd(ets:lookup(seg_max, Left)),
            {_, MaxR} = hd(ets:lookup(seg_max, Right)),
            ets:insert(seg_max, {Idx, erlang:max(MaxL, MaxR)})
    end.

update_row(Row, NewFree) ->
    N = get(n),
    update(1, 0, N - 1, Row, NewFree).

update(_Idx, L, R, Pos, _NewFree) when L > R -> ok;
update(Idx, L, R, Pos, NewFree) ->
    if L == R ->
            ets:insert(seg_sum, {Idx, NewFree}),
            ets:insert(seg_max, {Idx, NewFree});
       true ->
            Mid = (L + R) div 2,
            Left = Idx * 2,
            Right = Idx * 2 + 1,
            if Pos =< Mid -> update(Left, L, Mid, Pos, NewFree);
               true -> update(Right, Mid + 1, R, Pos, NewFree)
            end,

            {_, SumL} = hd(ets:lookup(seg_sum, Left)),
            {_, SumR} = hd(ets:lookup(seg_sum, Right)),
            ets:insert(seg_sum, {Idx, SumL + SumR}),

            {_, MaxL} = hd(ets:lookup(seg_max, Left)),
            {_, MaxR} = hd(ets:lookup(seg_max, Right)),
            ets:insert(seg_max, {Idx, erlang:max(MaxL, MaxR)})
    end.

query_sum(_Idx, L, R, Ql, _Qr) when Ql > R -> 0;
query_sum(_Idx, L, R, _Ql, Qr) when Qr < L -> 0;
query_sum(Idx, L, R, Ql, Qr) ->
    if Ql =< L, R =< Qr ->
            {_, Val} = hd(ets:lookup(seg_sum, Idx)),
            Val;
       true ->
            Mid = (L + R) div 2,
            SumLeft = query_sum(Idx * 2, L, Mid, Ql, Qr),
            SumRight = query_sum(Idx * 2 + 1, Mid + 1, R, Ql, Qr),
            SumLeft + SumRight
    end.

query_max(_Idx, L, R, Ql, _Qr) when Ql > R -> -1;
query_max(_Idx, L, R, _Ql, Qr) when Qr < L -> -1;
query_max(Idx, L, R, Ql, Qr) ->
    if Ql =< L, R =< Qr ->
            {_, Val} = hd(ets:lookup(seg_max, Idx)),
            Val;
       true ->
            Mid = (L + R) div 2,
            MaxLeft = query_max(Idx * 2, L, Mid, Ql, Qr),
            MaxRight = query_max(Idx * 2 + 1, Mid + 1, R, Ql, Qr),
            erlang:max(MaxLeft, MaxRight)
    end.

find_first(_Idx, L, _R, _K, MaxRow) when L > MaxRow -> undefined;
find_first(Idx, L, R, K, MaxRow) ->
    {_, NodeMax} = hd(ets:lookup(seg_max, Idx)),
    if NodeMax < K ->
            undefined;
       true ->
            if L == R -> L;
               true ->
                    Mid = (L + R) div 2,
                    LeftRes = find_first(Idx * 2, L, Mid, K, MaxRow),
                    case LeftRes of
                        undefined -> find_first(Idx * 2 + 1, Mid + 1, R, K, MaxRow);
                        _ -> LeftRes
                    end
            end
    end.

get_used(Row) ->
    case ets:lookup(used_tab, Row) of
        [{Row, U}] -> U;
        [] -> 0
    end.

get_free(Row) ->
    get(m) - get_used(Row).

advance_to_free(Cur, MaxRow) when Cur > MaxRow -> Cur;
advance_to_free(Cur, MaxRow) ->
    case get_free(Cur) of
        0 -> advance_to_free(Cur + 1, MaxRow);
        _ -> Cur
    end.

scatter_allocate(0, _MaxRow, Cur) -> {true, Cur};
scatter_allocate(K, MaxRow, Cur) ->
    Row = advance_to_free(Cur, MaxRow),
    if Row > MaxRow ->
            false;
       true ->
            Free = get_free(Row),
            Take = erlang:min(K, Free),
            Used = get_used(Row),
            NewUsed = Used + Take,
            NewFree = Free - Take,
            ets:insert(used_tab, {Row, NewUsed}),
            update_row(Row, NewFree),
            NextCur = if NewFree == 0 -> Row + 1; true -> Row end,
            scatter_allocate(K - Take, MaxRow, NextCur)
    end.
```

## Elixir

```elixir
defmodule BookMyShow do
  @spec init_(n :: integer, m :: integer) :: any
  def init_(n, m) do
    # Initialize arrays for next seat index per row, segment tree sum and max
    next_seat = :array.new(n, default: 0)
    size = 4 * n
    sum_tree = :array.new(size, default: 0)
    max_tree = :array.new(size, default: 0)

    state = %{
      n: n,
      m: m,
      next_seat: next_seat,
      sum_tree: sum_tree,
      max_tree: max_tree
    }

    # Build segment tree where each leaf has value m (remaining seats)
    state = build(state, 1, 0, n - 1)

    Process.put(:bms_state, state)
    :ok
  end

  @spec gather(k :: integer, max_row :: integer) :: [integer]
  def gather(k, max_row) do
    state = Process.get(:bms_state)

    case find_row(state, 1, 0, state.n - 1, max_row, k) do
      nil ->
        []

      row ->
        seat_start = :array.get(row, state.next_seat)
        new_next = seat_start + k

        next_seat = :array.set(row, new_next, state.next_seat)

        remaining = state.m - new_next
        state = %{state | next_seat: next_seat}
        state = update(state, 1, 0, state.n - 1, row, remaining)

        Process.put(:bms_state, state)
        [row, seat_start]
    end
  end

  @spec scatter(k :: integer, max_row :: integer) :: boolean
  def scatter(k, max_row) do
    state = Process.get(:bms_state)

    total = query_sum(state, 1, 0, state.n - 1, 0, max_row)

    if total < k do
      false
    else
      {state, _remaining} = allocate_scatter(state, k, max_row)
      Process.put(:bms_state, state)
      true
    end
  end

  # ---------- Helper Functions ----------
  defp build(state, node, l, r) do
    if l == r do
      sum_tree = :array.set(node, state.m, state.sum_tree)
      max_tree = :array.set(node, state.m, state.max_tree)
      %{state | sum_tree: sum_tree, max_tree: max_tree}
    else
      mid = div(l + r, 2)

      state = build(state, node * 2, l, mid)
      state = build(state, node * 2 + 1, mid + 1, r)

      left_sum = :array.get(node * 2, state.sum_tree)
      right_sum = :array.get(node * 2 + 1, state.sum_tree)
      sum_val = left_sum + right_sum

      left_max = :array.get(node * 2, state.max_tree)
      right_max = :array.get(node * 2 + 1, state.max_tree)
      max_val = if left_max > right_max, do: left_max, else: right_max

      sum_tree = :array.set(node, sum_val, state.sum_tree)
      max_tree = :array.set(node, max_val, state.max_tree)

      %{state | sum_tree: sum_tree, max_tree: max_tree}
    end
  end

  defp query_sum(state, node, l, r, ql, qr) do
    cond do
      ql > r or qr < l ->
        0

      ql <= l and r <= qr ->
        :array.get(node, state.sum_tree)

      true ->
        mid = div(l + r, 2)
        left = query_sum(state, node * 2, l, mid, ql, qr)
        right = query_sum(state, node * 2 + 1, mid + 1, r, ql, qr)
        left + right
    end
  end

  defp find_row(state, node, l, r, max_row, k) do
    cond do
      l > max_row or :array.get(node, state.max_tree) < k ->
        nil

      l == r ->
        l

      true ->
        mid = div(l + r, 2)

        left_res =
          if l <= max_row do
            find_row(state, node * 2, l, mid, max_row, k)
          else
            nil
          end

        case left_res do
          nil -> find_row(state, node * 2 + 1, mid + 1, r, max_row, k)
          _ -> left_res
        end
    end
  end

  defp find_first_positive(state, node, l, r, max_row) do
    cond do
      l > max_row or :array.get(node, state.max_tree) == 0 ->
        nil

      l == r ->
        l

      true ->
        mid = div(l + r, 2)

        left_res =
          if l <= max_row do
            find_first_positive(state, node * 2, l, mid, max_row)
          else
            nil
          end

        case left_res do
          nil -> find_first_positive(state, node * 2 + 1, mid + 1, r, max_row)
          _ -> left_res
        end
    end
  end

  defp update(state, node, l, r, idx, new_val) do
    if l == r do
      sum_tree = :array.set(node, new_val, state.sum_tree)
      max_tree = :array.set(node, new_val, state.max_tree)
      %{state | sum_tree: sum_tree, max_tree: max_tree}
    else
      mid = div(l + r, 2)

      state =
        if idx <= mid do
          update(state, node * 2, l, mid, idx, new_val)
        else
          update(state, node * 2 + 1, mid + 1, r, idx, new_val)
        end

      left_sum = :array.get(node * 2, state.sum_tree)
      right_sum = :array.get(node * 2 + 1, state.sum_tree)
      sum_val = left_sum + right_sum

      left_max = :array.get(node * 2, state.max_tree)
      right_max = :array.get(node * 2 + 1, state.max_tree)
      max_val = if left_max > right_max, do: left_max, else: right_max

      sum_tree = :array.set(node, sum_val, state.sum_tree)
      max_tree = :array.set(node, max_val, state.max_tree)

      %{state | sum_tree: sum_tree, max_tree: max_tree}
    end
  end

  defp allocate_scatter(state, k, max_row) do
    if k == 0 do
      {state, 0}
    else
      row = find_first_positive(state, 1, 0, state.n - 1, max_row)

      seat_start = :array.get(row, state.next_seat)
      avail = state.m - seat_start
      take = if k < avail, do: k, else: avail

      new_next = seat_start + take
      next_seat = :array.set(row, new_next, state.next_seat)

      remaining = state.m - new_next
      state = %{state | next_seat: next_seat}
      state = update(state, 1, 0, state.n - 1, row, remaining)

      allocate_scatter(state, k - take, max_row)
    end
  end
end
```
