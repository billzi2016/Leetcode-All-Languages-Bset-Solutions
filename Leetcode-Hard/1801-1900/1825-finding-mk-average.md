# 1825. Finding MK Average

## Cpp

```cpp
class MKAverage {
public:
    MKAverage(int m, int k) : m(m), k(k) {}
    
    void addElement(int num) {
        q.push(num);
        // Insert into appropriate set
        if (!low.empty() && num <= *prev(low.end())) {
            low.insert(num);
        } else if (!high.empty() && num >= *high.begin()) {
            high.insert(num);
        } else {
            mid.insert(num);
            sumMid += num;
        }
        rebalance();
        
        if ((int)q.size() > m) {
            int old = q.front(); q.pop();
            auto itLow = low.find(old);
            if (itLow != low.end()) {
                low.erase(itLow);
            } else {
                auto itHigh = high.find(old);
                if (itHigh != high.end()) {
                    high.erase(itHigh);
                } else {
                    auto itMid = mid.find(old);
                    if (itMid != mid.end()) {
                        sumMid -= old;
                        mid.erase(itMid);
                    }
                }
            }
            rebalance();
        }
    }
    
    int calculateMKAverage() {
        if ((int)q.size() < m) return -1;
        return (int)(sumMid / (m - 2 * k));
    }

private:
    int m, k;
    std::queue<int> q;
    std::multiset<int> low, mid, high;
    long long sumMid = 0;
    
    void rebalance() {
        // Ensure low size <= k
        while ((int)low.size() > k) {
            auto it = prev(low.end());
            int val = *it;
            low.erase(it);
            mid.insert(val);
            sumMid += val;
        }
        // Ensure high size <= k
        while ((int)high.size() > k) {
            auto it = high.begin();
            int val = *it;
            high.erase(it);
            mid.insert(val);
            sumMid += val;
        }
        // Fill low up to k
        while ((int)low.size() < k && !mid.empty()) {
            auto it = mid.begin(); // smallest in mid
            int val = *it;
            mid.erase(it);
            sumMid -= val;
            low.insert(val);
        }
        // Fill high up to k
        while ((int)high.size() < k && !mid.empty()) {
            auto it = prev(mid.end()); // largest in mid
            int val = *it;
            mid.erase(it);
            sumMid -= val;
            high.insert(val);
        }
    }
};

/**
 * Your MKAverage object will be instantiated and called as such:
 * MKAverage* obj = new MKAverage(m, k);
 * obj->addElement(num);
 * int param_2 = obj->calculateMKAverage();
 */
```

## Java

```java
class MKAverage {
    private static class BIT {
        int n;
        long[] tree;
        BIT(int n) {
            this.n = n;
            tree = new long[n + 2];
        }
        void add(int idx, long delta) {
            while (idx <= n) {
                tree[idx] += delta;
                idx += idx & -idx;
            }
        }
        long query(int idx) {
            long res = 0;
            while (idx > 0) {
                res += tree[idx];
                idx -= idx & -idx;
            }
            return res;
        }
        // find smallest index such that prefix sum >= k (k >= 1)
        int findKth(long k) {
            int idx = 0;
            int bit = Integer.highestOneBit(n);
            for (int step = bit; step != 0; step >>= 1) {
                int next = idx + step;
                if (next <= n && tree[next] < k) {
                    idx = next;
                    k -= tree[next];
                }
            }
            return idx + 1;
        }
    }

    private final int m, k;
    private final java.util.ArrayDeque<Integer> queue;
    private final BIT bitCount;
    private final BIT bitSum;
    private static final int MAXV = 100000; // given constraint for num

    public MKAverage(int m, int k) {
        this.m = m;
        this.k = k;
        this.queue = new java.util.ArrayDeque<>();
        this.bitCount = new BIT(MAXV);
        this.bitSum = new BIT(MAXV);
    }

    public void addElement(int num) {
        queue.addLast(num);
        bitCount.add(num, 1);
        bitSum.add(num, num);
        if (queue.size() > m) {
            int old = queue.pollFirst();
            bitCount.add(old, -1);
            bitSum.add(old, -old);
        }
    }

    public int calculateMKAverage() {
        if (queue.size() < m) return -1;
        long sumSmallK = getSumOfSmallest(k);
        long sumSmallMMinusK = getSumOfSmallest(m - k);
        long middleSum = sumSmallMMinusK - sumSmallK;
        int divisor = m - 2 * k;
        return (int) (middleSum / divisor);
    }

    private long getSumOfSmallest(int cnt) {
        if (cnt <= 0) return 0L;
        int idx = bitCount.findKth(cnt);
        long countBefore = bitCount.query(idx - 1);
        long sumBefore = bitSum.query(idx - 1);
        long need = cnt - countBefore; // number of elements needed from value idx
        return sumBefore + need * idx;
    }
}

/**
 * Your MKAverage object will be instantiated and called as such:
 * MKAverage obj = new MKAverage(m, k);
 * obj.addElement(num);
 * int param_2 = obj.calculateMKAverage();
 */
```

## Python

```python
import random
from collections import deque

class _Node:
    __slots__ = ('val', 'prio', 'cnt', 'size', 'sum', 'left', 'right')
    def __init__(self, val):
        self.val = val
        self.prio = random.randint(1, 1 << 30)
        self.cnt = 1
        self.size = 1
        self.sum = val
        self.left = None
        self.right = None

def _update(node):
    if not node:
        return
    left = node.left
    right = node.right
    node.size = (left.size if left else 0) + (right.size if right else 0) + node.cnt
    node.sum = (left.sum if left else 0) + (right.sum if right else 0) + node.val * node.cnt

def _rotate_right(p):
    q = p.left
    p.left = q.right
    q.right = p
    _update(p)
    _update(q)
    return q

def _rotate_left(p):
    q = p.right
    p.right = q.left
    q.left = p
    _update(p)
    _update(q)
    return q

def _insert(node, val):
    if not node:
        return _Node(val)
    if val == node.val:
        node.cnt += 1
    elif val < node.val:
        node.left = _insert(node.left, val)
        if node.left.prio > node.prio:
            node = _rotate_right(node)
    else:
        node.right = _insert(node.right, val)
        if node.right.prio > node.prio:
            node = _rotate_left(node)
    _update(node)
    return node

def _merge(a, b):
    if not a or not b:
        return a or b
    if a.prio > b.prio:
        a.right = _merge(a.right, b)
        _update(a)
        return a
    else:
        b.left = _merge(a, b.left)
        _update(b)
        return b

def _erase(node, val):
    if not node:
        return None
    if val == node.val:
        if node.cnt > 1:
            node.cnt -= 1
            _update(node)
            return node
        else:
            return _merge(node.left, node.right)
    elif val < node.val:
        node.left = _erase(node.left, val)
    else:
        node.right = _erase(node.right, val)
    if node:
        _update(node)
    return node

def _prefix_sum(node, k):
    # sum of smallest k elements
    if not node or k <= 0:
        return 0
    left = node.left
    left_sz = left.size if left else 0
    if k <= left_sz:
        return _prefix_sum(left, k)
    elif k <= left_sz + node.cnt:
        left_sum = left.sum if left else 0
        need = k - left_sz
        return left_sum + need * node.val
    else:
        left_sum = left.sum if left else 0
        cur_sum = node.cnt * node.val
        return left_sum + cur_sum + _prefix_sum(node.right, k - left_sz - node.cnt)

class MKAverage(object):

    def __init__(self, m, k):
        """
        :type m: int
        :type k: int
        """
        self.m = m
        self.k = k
        self.window = deque()
        self.root = None

    def addElement(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.window.append(num)
        self.root = _insert(self.root, num)
        if len(self.window) > self.m:
            old = self.window.popleft()
            self.root = _erase(self.root, old)

    def calculateMKAverage(self):
        """
        :rtype: int
        """
        if len(self.window) < self.m:
            return -1
        total_mid_cnt = self.m - 2 * self.k
        sum_low_k = _prefix_sum(self.root, self.k)
        sum_up_to_mk = _prefix_sum(self.root, self.m - self.k)
        mid_sum = sum_up_to_mk - sum_low_k
        return mid_sum // total_mid_cnt
```

## Python3

```python
class MKAverage:
    from collections import deque
    import bisect

    class _SortedList:
        __slots__ = ('_B', 'blocks', 'sums')

        def __init__(self):
            self._B = 350  # block size, sqrt(1e5) ~ 316
            self.blocks = []   # list of sorted blocks
            self.sums = []     # sum of each block

        def _build(self, a=None):
            if a is None:
                a = []
            B = self._B
            self.blocks = [a[i:i + B] for i in range(0, len(a), B)]
            self.sums = [sum(block) for block in self.blocks]

        def __len__(self):
            return sum(len(b) for b in self.blocks)

        def add(self, x: int):
            import bisect
            if not self.blocks:
                self.blocks.append([x])
                self.sums.append(x)
                return

            # locate block
            lo, hi = 0, len(self.blocks)
            while lo < hi:
                mid = (lo + hi) // 2
                if self.blocks[mid][-1] < x:
                    lo = mid + 1
                else:
                    hi = mid
            if lo == len(self.blocks):
                b_idx = len(self.blocks) - 1
                inner = len(self.blocks[b_idx])
            else:
                b_idx = lo
                block = self.blocks[b_idx]
                inner = bisect.bisect_left(block, x)

            self.blocks[b_idx].insert(inner, x)
            self.sums[b_idx] += x

            if len(self.blocks[b_idx]) > 2 * self._B:
                # split block
                new_block = self.blocks[b_idx][self._B:]
                self.blocks[b_idx] = self.blocks[b_idx][:self._B]
                self.sums[b_idx] = sum(self.blocks[b_idx])
                self.blocks.insert(b_idx + 1, new_block)
                self.sums.insert(b_idx + 1, sum(new_block))

        def discard(self, x: int):
            import bisect
            if not self.blocks:
                return False

            lo, hi = 0, len(self.blocks)
            while lo < hi:
                mid = (lo + hi) // 2
                if self.blocks[mid][-1] < x:
                    lo = mid + 1
                else:
                    hi = mid
            if lo == len(self.blocks):
                return False

            b_idx = lo
            block = self.blocks[b_idx]
            i = bisect.bisect_left(block, x)
            if i == len(block) or block[i] != x:
                return False

            val = block.pop(i)
            self.sums[b_idx] -= val

            # clean empty block
            if not block:
                self.blocks.pop(b_idx)
                self.sums.pop(b_idx)
            else:
                # merge with neighbor if too small
                if len(block) < self._B // 2 and len(self.blocks) > 1:
                    if b_idx > 0:
                        left = self.blocks[b_idx - 1]
                        if len(left) + len(block) <= 2 * self._B:
                            left.extend(block)
                            self.sums[b_idx - 1] += self.sums[b_idx]
                            self.blocks.pop(b_idx)
                            self.sums.pop(b_idx)
                    elif b_idx + 1 < len(self.blocks):
                        right = self.blocks[b_idx + 1]
                        if len(right) + len(block) <= 2 * self._B:
                            block.extend(right)
                            self.sums[b_idx] = sum(block)
                            self.blocks.pop(b_idx + 1)
                            self.sums.pop(b_idx + 1)
            return True

        def range_sum(self, left: int, right: int):
            """sum of elements with indices [left, right)"""
            if left >= right:
                return 0
            res = 0
            i = 0
            # skip whole blocks before 'left'
            while i < len(self.blocks) and left >= len(self.blocks[i]):
                left -= len(self.blocks[i])
                right -= len(self.blocks[i])
                i += 1

            while i < len(self.blocks) and left < right:
                block = self.blocks[i]
                take = min(len(block) - left, right - left)
                # sum slice
                res += sum(block[left:left + take])
                right -= take
                i += 1
                left = 0
            return res

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.q = self.deque()
        self.sl = self._SortedList()

    def addElement(self, num: int) -> None:
        self.q.append(num)
        self.sl.add(num)
        if len(self.q) > self.m:
            old = self.q.popleft()
            self.sl.discard(old)

    def calculateMKAverage(self) -> int:
        if len(self.q) < self.m:
            return -1
        total_len = len(self.sl)
        left = self.k
        right = total_len - self.k
        sum_mid = self.sl.range_sum(left, right)
        cnt = total_len - 2 * self.k
        return sum_mid // cnt
```

## C

```c
typedef struct {
    int m;
    int k;
    int *arr;
    int head;
    int sz;
    long long totalSum;
    int maxVal;
    long long *cntTree;
    long long *sumTree;
} MKAverage;

static void bitUpdate(MKAverage* obj, int val, int delta) {
    for (int i = val; i <= obj->maxVal; i += i & -i) {
        obj->cntTree[i] += delta;
        obj->sumTree[i] += (long long)delta * val;
    }
}

static long long queryCnt(MKAverage* obj, int idx) {
    long long res = 0;
    for (int i = idx; i > 0; i -= i & -i)
        res += obj->cntTree[i];
    return res;
}

static long long querySum(MKAverage* obj, int idx) {
    long long res = 0;
    for (int i = idx; i > 0; i -= i & -i)
        res += obj->sumTree[i];
    return res;
}

/* find smallest value v such that prefix count >= k */
static int findKth(MKAverage* obj, int k) {
    int idx = 0;
    int bitMask = 1;
    while (bitMask <= obj->maxVal) bitMask <<= 1;
    for (int step = bitMask; step > 0; step >>= 1) {
        int next = idx + step;
        if (next <= obj->maxVal && obj->cntTree[next] < k) {
            idx = next;
            k -= (int)obj->cntTree[next];
        }
    }
    return idx + 1;
}

/* sum of first k smallest elements */
static long long sumFirstK(MKAverage* obj, int k) {
    if (k <= 0) return 0;
    int pos = findKth(obj, k);
    long long cntPrev = queryCnt(obj, pos - 1);
    long long sumPrev = querySum(obj, pos - 1);
    long long remain = k - cntPrev;          // number of elements equal to 'pos' taken
    return sumPrev + remain * (long long)pos;
}

/* Create */
MKAverage* mKAverageCreate(int m, int k) {
    MKAverage* obj = (MKAverage*)malloc(sizeof(MKAverage));
    obj->m = m;
    obj->k = k;
    obj->arr = (int*)malloc(sizeof(int) * m);
    obj->head = 0;
    obj->sz = 0;
    obj->totalSum = 0;
    obj->maxVal = 100000;                     // per constraints
    obj->cntTree = (long long*)calloc(obj->maxVal + 2, sizeof(long long));
    obj->sumTree = (long long*)calloc(obj->maxVal + 2, sizeof(long long));
    return obj;
}

/* Add element */
void mKAverageAddElement(MKAverage* obj, int num) {
    if (obj->sz == obj->m) {                  // need to evict oldest
        int old = obj->arr[obj->head];
        bitUpdate(obj, old, -1);
        obj->totalSum -= old;
        obj->head = (obj->head + 1) % obj->m;
        obj->sz--;
    }
    int idx = (obj->head + obj->sz) % obj->m;
    obj->arr[idx] = num;
    bitUpdate(obj, num, 1);
    obj->totalSum += num;
    obj->sz++;
}

/* Calculate MKAverage */
int mKAverageCalculateMKAverage(MKAverage* obj) {
    if (obj->sz < obj->m)
        return -1;
    long long sumSmall = sumFirstK(obj, obj->k);
    long long sumFirstMMinusK = sumFirstK(obj, obj->m - obj->k);
    long long sumLarge = obj->totalSum - sumFirstMMinusK;   // sum of largest k
    long long midSum = obj->totalSum - sumSmall - sumLarge;
    int denom = obj->m - 2 * obj->k;
    return (int)(midSum / denom);
}

/* Free */
void mKAverageFree(MKAverage* obj) {
    if (!obj) return;
    free(obj->arr);
    free(obj->cntTree);
    free(obj->sumTree);
    free(obj);
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class MKAverage {
    private readonly int m;
    private readonly int k;
    private readonly Queue<(int val, long id)> window;
    private readonly SortedSet<(int val, long id)> low;
    private readonly SortedSet<(int val, long id)> mid;
    private readonly SortedSet<(int val, long id)> high;
    private long sumMid;
    private long idx;

    public MKAverage(int m, int k) {
        this.m = m;
        this.k = k;
        window = new Queue<(int, long)>();
        var comp = new PairComparer();
        low = new SortedSet<(int, long)>(comp);
        mid = new SortedSet<(int, long)>(comp);
        high = new SortedSet<(int, long)>(comp);
        sumMid = 0;
        idx = 0;
    }

    public void AddElement(int num) {
        var node = (num, idx++);
        // Insert into appropriate set
        if (low.Count > 0 && compCompare(node, low.Max) <= 0) {
            low.Add(node);
        } else if (high.Count > 0 && compCompare(node, high.Min) >= 0) {
            high.Add(node);
        } else {
            mid.Add(node);
            sumMid += num;
        }

        window.Enqueue(node);
        Balance();

        if (window.Count > m) {
            var old = window.Dequeue();
            if (!low.Remove(old)) {
                if (!high.Remove(old)) {
                    // must be in mid
                    mid.Remove(old);
                    sumMid -= old.val;
                }
            }
            Balance();
        }
    }

    public int CalculateMKAverage() {
        if (window.Count < m) return -1;
        long divisor = m - 2L * k;
        return (int)(sumMid / divisor);
    }

    private void Balance() {
        // Ensure low size <= k
        while (low.Count > k) {
            var node = low.Max;
            low.Remove(node);
            mid.Add(node);
            sumMid += node.val;
        }
        // Ensure high size <= k
        while (high.Count > k) {
            var node = high.Min;
            high.Remove(node);
            mid.Add(node);
            sumMid += node.val;
        }
        // Fill low up to k
        while (low.Count < k && mid.Count > 0) {
            var node = mid.Min;
            mid.Remove(node);
            sumMid -= node.val;
            low.Add(node);
        }
        // Fill high up to k
        while (high.Count < k && mid.Count > 0) {
            var node = mid.Max;
            mid.Remove(node);
            sumMid -= node.val;
            high.Add(node);
        }
    }

    private static int compCompare((int val, long id) a, (int val, long id) b) {
        int cmp = a.val.CompareTo(b.val);
        if (cmp != 0) return cmp;
        return a.id.CompareTo(b.id);
    }

    private class PairComparer : IComparer<(int val, long id)> {
        public int Compare((int val, long id) a, (int val, long id) b) {
            int cmp = a.val.CompareTo(b.val);
            if (cmp != 0) return cmp;
            return a.id.CompareTo(b.id);
        }
    }
}

/**
 * Your MKAverage object will be instantiated and called as such:
 * MKAverage obj = new MKAverage(m, k);
 * obj.AddElement(num);
 * int param_2 = obj.CalculateMKAverage();
 */
```

## Javascript

```javascript
/**
 * Binary Indexed Tree (Fenwick) for sum queries.
 */
class BIT {
    constructor(size) {
        this.n = size + 2; // 1-indexed, extra space
        this.tree = new Array(this.n).fill(0);
    }
    add(idx, delta) {
        for (let i = idx; i < this.n; i += i & -i) {
            this.tree[i] += delta;
        }
    }
    sum(idx) {
        let res = 0;
        for (let i = idx; i > 0; i -= i & -i) {
            res += this.tree[i];
        }
        return res;
    }
    // smallest index such that prefix sum >= target (target > 0)
    lowerBound(target) {
        let idx = 0;
        // highest power of two <= n
        let bit = 1;
        while ((bit << 1) < this.n) bit <<= 1;
        for (; bit > 0; bit >>= 1) {
            const next = idx + bit;
            if (next < this.n && this.tree[next] < target) {
                idx = next;
                target -= this.tree[next];
            }
        }
        return idx + 1; // 1-indexed position
    }
}

/**
 * @param {number} m
 * @param {number} k
 */
var MKAverage = function(m, k) {
    this.m = m;
    this.k = k;
    this.maxVal = 100000; // per constraints
    this.cntBIT = new BIT(this.maxVal);
    this.sumBIT = new BIT(this.maxVal);
    this.queue = [];
    this.start = 0;   // index of the first valid element in queue
    this.size = 0;    // current window size (<= m)
    this.totalSum = 0;
};

/**
 * internal helper to update both BITs
 */
MKAverage.prototype._add = function(num, delta) {
    this.cntBIT.add(num, delta);
    this.sumBIT.add(num, delta * num);
};

/**
 * sum of the smallest k elements in current window
 */
MKAverage.prototype._prefixSumK = function(k) {
    if (k <= 0) return 0;
    const pos = this.cntBIT.lowerBound(k); // value where kth element lies
    const cntBefore = this.cntBIT.sum(pos - 1);
    const sumBefore = this.sumBIT.sum(pos - 1);
    const need = k - cntBefore; // how many of 'pos' we need
    return sumBefore + need * pos;
};

/** 
 * @param {number} num
 * @return {void}
 */
MKAverage.prototype.addElement = function(num) {
    this.queue.push(num);
    this._add(num, 1);
    this.totalSum += num;
    this.size++;

    if (this.size > this.m) {
        const oldNum = this.queue[this.start];
        this.start++;
        this._add(oldNum, -1);
        this.totalSum -= oldNum;
        this.size--;
    }
};

/**
 * @return {number}
 */
MKAverage.prototype.calculateMKAverage = function() {
    if (this.size < this.m) return -1;

    const sumSmallestK = this._prefixSumK(this.k);

    // sum of smallest (m - k) elements = total - sumLargestK
    const sumSmallestRest = this._prefixSumK(this.m - this.k);
    const sumLargestK = this.totalSum - sumSmallestRest;

    const middleSum = this.totalSum - sumSmallestK - sumLargestK;
    return Math.floor(middleSum / (this.m - 2 * this.k));
};
```

## Typescript

```typescript
class BIT {
    n: number;
    treeCount: number[];
    treeSum: number[];

    constructor(n: number) {
        this.n = n;
        this.treeCount = new Array(n + 2).fill(0);
        this.treeSum = new Array(n + 2).fill(0);
    }

    add(idx: number, deltaCnt: number, deltaSum: number): void {
        for (let i = idx; i <= this.n; i += i & -i) {
            this.treeCount[i] += deltaCnt;
            this.treeSum[i] += deltaSum;
        }
    }

    prefixCount(idx: number): number {
        let res = 0;
        for (let i = idx; i > 0; i -= i & -i) {
            res += this.treeCount[i];
        }
        return res;
    }

    prefixSum(idx: number): number {
        let res = 0;
        for (let i = idx; i > 0; i -= i & -i) {
            res += this.treeSum[i];
        }
        return res;
    }

    // smallest index such that cumulative count >= k (1-indexed values)
    kth(k: number): number {
        let idx = 0;
        let bitMask = 1 << Math.floor(Math.log2(this.n));
        while (bitMask !== 0) {
            const next = idx + bitMask;
            if (next <= this.n && this.treeCount[next] < k) {
                k -= this.treeCount[next];
                idx = next;
            }
            bitMask >>= 1;
        }
        return idx + 1;
    }
}

class MKAverage {
    private m: number;
    private k: number;
    private queue: number[];
    private head: number;
    private size: number;
    private totalSum: number;
    private bit: BIT;

    constructor(m: number, k: number) {
        this.m = m;
        this.k = k;
        this.queue = [];
        this.head = 0;
        this.size = 0;
        this.totalSum = 0;
        // nums are in [1, 100000]
        this.bit = new BIT(100000);
    }

    addElement(num: number): void {
        this.queue.push(num);
        this.bit.add(num, 1, num);
        this.totalSum += num;
        this.size++;

        if (this.size > this.m) {
            const old = this.queue[this.head];
            this.head++;
            this.bit.add(old, -1, -old);
            this.totalSum -= old;
            this.size--;
        }
    }

    calculateMKAverage(): number {
        if (this.size < this.m) return -1;

        const sumSmallK = this.getSumSmallest(this.k);
        const sumSmallMMinusK = this.getSumSmallest(this.m - this.k);
        const middleSum = sumSmallMMinusK - sumSmallK;
        const divisor = this.m - 2 * this.k;
        return Math.floor(middleSum / divisor);
    }

    private getSumSmallest(x: number): number {
        if (x <= 0) return 0;
        const idx = this.bit.kth(x);
        const cntBefore = this.bit.prefixCount(idx - 1);
        const sumBefore = this.bit.prefixSum(idx - 1);
        const need = x - cntBefore;
        return sumBefore + need * idx;
    }
}

/**
 * Your MKAverage object will be instantiated and called as such:
 * var obj = new MKAverage(m, k)
 * obj.addElement(num)
 * var param_2 = obj.calculateMKAverage()
 */
```

## Php

```php
class MKAverage {
    private int $m;
    private int $k;
    private SplQueue $queue;
    private array $cntBIT;
    private array $sumBIT;
    private int $size = 100001; // max value (1e5) + 1
    private int $totalSum = 0;

    public function __construct(int $m, int $k) {
        $this->m = $m;
        $this->k = $k;
        $this->queue = new SplQueue();
        $this->cntBIT = array_fill(0, $this->size + 2, 0);
        $this->sumBIT = array_fill(0, $this->size + 2, 0);
    }

    private function addCount(int $idx, int $delta): void {
        for ($i = $idx; $i <= $this->size; $i += $i & (-$i)) {
            $this->cntBIT[$i] += $delta;
        }
    }

    private function addSum(int $idx, int $delta): void {
        for ($i = $idx; $i <= $this->size; $i += $i & (-$i)) {
            $this->sumBIT[$i] += $delta;
        }
    }

    private function queryCount(int $idx): int {
        $res = 0;
        for ($i = $idx; $i > 0; $i -= $i & (-$i)) {
            $res += $this->cntBIT[$i];
        }
        return $res;
    }

    private function querySum(int $idx): int {
        $res = 0;
        for ($i = $idx; $i > 0; $i -= $i & (-$i)) {
            $res += $this->sumBIT[$i];
        }
        return $res;
    }

    // find smallest index such that prefix count >= k (k >=1)
    private function findKth(int $k): int {
        $idx = 0;
        $bitMask = 1;
        while ($bitMask <= $this->size) {
            $bitMask <<= 1;
        }
        $bitMask >>= 1; // highest power of two <= size
        for (; $bitMask > 0; $bitMask >>= 1) {
            $next = $idx + $bitMask;
            if ($next <= $this->size && $this->cntBIT[$next] < $k) {
                $k -= $this->cntBIT[$next];
                $idx = $next;
            }
        }
        return $idx + 1;
    }

    private function sumSmallest(int $k): int {
        if ($k <= 0) {
            return 0;
        }
        $idx = $this->findKth($k);
        $cntPrev = $this->queryCount($idx - 1);
        $sumPrev = $this->querySum($idx - 1);
        $need = $k - $cntPrev; // number of elements equal to $idx needed
        return $sumPrev + $need * $idx;
    }

    public function addElement(int $num): void {
        $this->queue->enqueue($num);
        $this->addCount($num, 1);
        $this->addSum($num, $num);
        $this->totalSum += $num;

        if ($this->queue->count() > $this->m) {
            $old = $this->queue->dequeue();
            $this->addCount($old, -1);
            $this->addSum($old, -$old);
            $this->totalSum -= $old;
        }
    }

    public function calculateMKAverage(): int {
        if ($this->queue->count() < $this->m) {
            return -1;
        }
        // sum of smallest k elements
        $sumSmallK = $this->sumSmallest($this->k);
        // sum of largest k elements = totalSum - sum of smallest (m - k) elements
        $sumSmallRest = $this->sumSmallest($this->m - $this->k);
        $sumLargeK = $this->totalSum - $sumSmallRest;

        $midSum = $this->totalSum - $sumSmallK - $sumLargeK;
        $denom = $this->m - 2 * $this->k;
        return intdiv($midSum, $denom);
    }
}
```

## Swift

```swift
class Fenwick {
    let n: Int
    var cnt: [Int]
    var sum: [Int64]

    init(_ n: Int) {
        self.n = n
        cnt = Array(repeating: 0, count: n + 2)
        sum = Array(repeating: 0, count: n + 2)
    }

    func update(_ index: Int, _ deltaCnt: Int, _ deltaVal: Int) {
        var i = index
        while i <= n {
            cnt[i] += deltaCnt
            sum[i] += Int64(deltaVal)
            i += i & -i
        }
    }

    func queryCount(_ index: Int) -> Int {
        var res = 0
        var i = index
        while i > 0 {
            res += cnt[i]
            i -= i & -i
        }
        return res
    }

    func querySum(_ index: Int) -> Int64 {
        var res: Int64 = 0
        var i = index
        while i > 0 {
            res += sum[i]
            i -= i & -i
        }
        return res
    }
}

class MKAverage {

    private let m: Int
    private let k: Int
    private let maxVal = 100000
    private var fenwick: Fenwick
    private var data: [Int] = []
    private var head: Int = 0
    private var totalSum: Int64 = 0

    init(_ m: Int, _ k: Int) {
        self.m = m
        self.k = k
        fenwick = Fenwick(maxVal)
    }

    func addElement(_ num: Int) {
        data.append(num)
        fenwick.update(num, 1, num)
        totalSum += Int64(num)

        if data.count - head > m {
            let old = data[head]
            head += 1
            fenwick.update(old, -1, -old)
            totalSum -= Int64(old)
        }
    }

    private func sumOfSmallest(_ cnt: Int) -> Int64 {
        if cnt <= 0 { return 0 }
        var left = 1
        var right = maxVal
        while left < right {
            let mid = (left + right) >> 1
            if fenwick.queryCount(mid) >= cnt {
                right = mid
            } else {
                left = mid + 1
            }
        }
        let v = left
        let lessCnt = fenwick.queryCount(v - 1)
        let sumLess = fenwick.querySum(v - 1)
        let need = cnt - lessCnt
        return sumLess + Int64(need) * Int64(v)
    }

    func calculateMKAverage() -> Int {
        if data.count - head < m { return -1 }
        let sumSmallK = sumOfSmallest(k)
        let sumSmallMMinusK = sumOfSmallest(m - k)
        let sumLargeK = totalSum - sumSmallMMinusK
        let middleSum = totalSum - sumSmallK - sumLargeK
        let divisor = m - 2 * k
        return Int(middleSum / Int64(divisor))
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque
import java.util.TreeMap

class MKAverage(private val m: Int, private val k: Int) {

    private class MultiSet {
        val map = TreeMap<Int, Int>()
        var size = 0

        fun add(x: Int) {
            map[x] = (map[x] ?: 0) + 1
            size++
        }

        fun remove(x: Int) {
            val cnt = map[x] ?: return
            if (cnt == 1) map.remove(x) else map[x] = cnt - 1
            size--
        }

        fun firstKey(): Int = map.firstKey()
        fun lastKey(): Int = map.lastKey()

        fun pollFirst(): Int {
            val key = map.firstKey()
            remove(key)
            return key
        }

        fun pollLast(): Int {
            val key = map.lastKey()
            remove(key)
            return key
        }

        fun contains(x: Int): Boolean = map.containsKey(x)
    }

    private val low = MultiSet()   // k smallest
    private val mid = MultiSet()   // middle elements
    private val high = MultiSet()  // k largest
    private var sumMid: Long = 0L
    private val queue = ArrayDeque<Int>()

    fun addElement(num: Int) {
        queue.addLast(num)

        // Insert into appropriate set based on current boundaries
        when {
            low.size > 0 && num <= low.lastKey() -> low.add(num)
            high.size > 0 && num >= high.firstKey() -> high.add(num)
            else -> {
                mid.add(num)
                sumMid += num.toLong()
            }
        }

        balanceAfterInsert()

        if (queue.size > m) {
            val old = queue.removeFirst()
            when {
                low.contains(old) -> low.remove(old)
                high.contains(old) -> high.remove(old)
                else -> {
                    mid.remove(old)
                    sumMid -= old.toLong()
                }
            }
            balanceAfterRemove()
        }
    }

    fun calculateMKAverage(): Int {
        if (queue.size < m) return -1
        val cnt = m - 2 * k
        return (sumMid / cnt).toInt()
    }

    private fun balanceAfterInsert() {
        // Ensure low and high do not exceed size k
        while (low.size > k) {
            val moved = low.pollLast()
            mid.add(moved)
            sumMid += moved.toLong()
        }
        while (high.size > k) {
            val moved = high.pollFirst()
            mid.add(moved)
            sumMid += moved.toLong()
        }
        // Fill low and high up to size k from mid if possible
        while (low.size < k && mid.size > 0) {
            val moved = mid.pollFirst()   // smallest in mid
            low.add(moved)
            sumMid -= moved.toLong()
        }
        while (high.size < k && mid.size > 0) {
            val moved = mid.pollLast()    // largest in mid
            high.add(moved)
            sumMid -= moved.toLong()
        }
    }

    private fun balanceAfterRemove() {
        // After removal, low/high might be too small; move from mid if possible
        while (low.size > k) {
            val moved = low.pollLast()
            mid.add(moved)
            sumMid += moved.toLong()
        }
        while (high.size > k) {
            val moved = high.pollFirst()
            mid.add(moved)
            sumMid += moved.toLong()
        }
        while (low.size < k && mid.size > 0) {
            val moved = mid.pollFirst()
            low.add(moved)
            sumMid -= moved.toLong()
        }
        while (high.size < k && mid.size > 0) {
            val moved = mid.pollLast()
            high.add(moved)
            sumMid -= moved.toLong()
        }
    }
}

/**
 * Your MKAverage object will be instantiated and called as such:
 * var obj = MKAverage(m, k)
 * obj.addElement(num)
 * var param_2 = obj.calculateMKAverage()
 */
```

## Dart

```dart
import 'dart:collection';

class MKAverage {
  final int m;
  final int k;
  final Queue<int> _queue = ListQueue<int>();
  final SplayTreeMap<int, int> _low = SplayTreeMap<int, int>();
  final SplayTreeMap<int, int> _mid = SplayTreeMap<int, int>();
  final SplayTreeMap<int, int> _high = SplayTreeMap<int, int>();

  int _lowSize = 0;
  int _midSize = 0;
  int _highSize = 0;
  int _midSum = 0;

  MKAverage(this.m, this.k);

  void addElement(int num) {
    _queue.add(num);
    _add(_low, num);
    _lowSize++;

    if (_lowSize > k) {
      int move = _low.lastKey!;
      _remove(_low, move);
      _lowSize--;
      _addMid(move);
    }

    if (_midSize > m - 2 * k) {
      int move = _mid.lastKey!;
      _removeMid(move);
      _add(_high, move);
      _highSize++;
    }

    if (_queue.length > m) {
      int old = _queue.removeFirst();
      if (_contains(_low, old)) {
        _remove(_low, old);
        _lowSize--;
        if (_lowSize < k && _midSize > 0) {
          int mv = _mid.firstKey!;
          _removeMid(mv);
          _add(_low, mv);
          _lowSize++;
        }
      } else if (_contains(_high, old)) {
        _remove(_high, old);
        _highSize--;
        if (_highSize < k && _midSize > 0) {
          int mv = _mid.lastKey!;
          _removeMid(mv);
          _add(_high, mv);
          _highSize++;
        }
      } else {
        _removeMid(old);
        if (_lowSize < k && _midSize > 0) {
          int mv = _mid.firstKey!;
          _removeMid(mv);
          _add(_low, mv);
          _lowSize++;
        }
        if (_highSize < k && _midSize > 0) {
          int mv = _mid.lastKey!;
          _removeMid(mv);
          _add(_high, mv);
          _highSize++;
        }
      }

      while (_lowSize > k) {
        int move = _low.lastKey!;
        _remove(_low, move);
        _lowSize--;
        _addMid(move);
      }
      while (_highSize > k) {
        int move = _high.firstKey!;
        _remove(_high, move);
        _highSize--;
        _addMid(move);
      }
      while (_lowSize < k && _midSize > 0) {
        int mv = _mid.firstKey!;
        _removeMid(mv);
        _add(_low, mv);
        _lowSize++;
      }
      while (_highSize < k && _midSize > 0) {
        int mv = _mid.lastKey!;
        _removeMid(mv);
        _add(_high, mv);
        _highSize++;
      }
    }
  }

  int calculateMKAverage() {
    if (_queue.length < m) return -1;
    return _midSum ~/ (m - 2 * k);
  }

  void _add(SplayTreeMap<int, int> map, int x) {
    map[x] = (map[x] ?? 0) + 1;
  }

  void _remove(SplayTreeMap<int, int> map, int x) {
    var cnt = map[x];
    if (cnt == null) return;
    if (cnt == 1) {
      map.remove(x);
    } else {
      map[x] = cnt - 1;
    }
  }

  bool _contains(SplayTreeMap<int, int> map, int x) => map.containsKey(x);

  void _addMid(int x) {
    _mid[x] = (_mid[x] ?? 0) + 1;
    _midSize++;
    _midSum += x;
  }

  void _removeMid(int x) {
    var cnt = _mid[x];
    if (cnt == null) return;
    if (cnt == 1) {
      _mid.remove(x);
    } else {
      _mid[x] = cnt - 1;
    }
    _midSize--;
    _midSum -= x;
  }
}

/**
 * Your MKAverage object will be instantiated and called as such:
 * MKAverage obj = MKAverage(m, k);
 * obj.addElement(num);
 * int param2 = obj.calculateMKAverage();
 */
```

## Golang

```go
type BIT struct {
	n    int
	tree []int
}

func NewBIT(n int) *BIT {
	return &BIT{
		n:    n,
		tree: make([]int, n+2),
	}
}

func (b *BIT) add(idx, delta int) {
	for i := idx; i <= b.n; i += i & -i {
		b.tree[i] += delta
	}
}

func (b *BIT) sum(idx int) int {
	res := 0
	for i := idx; i > 0; i -= i & -i {
		res += b.tree[i]
	}
	return res
}

// kth returns the smallest index such that prefix count >= k (1-indexed)
func (b *BIT) kth(k int) int {
	idx := 0
	bitMask := 1
	for bitMask <= b.n {
		bitMask <<= 1
	}
	bitMask >>= 1
	for bitMask != 0 {
		next := idx + bitMask
		if next <= b.n && b.tree[next] < k {
			k -= b.tree[next]
			idx = next
		}
		bitMask >>= 1
	}
	return idx + 1
}

type BIT64 struct {
	n    int
	tree []int64
}

func NewBIT64(n int) *BIT64 {
	return &BIT64{
		n:    n,
		tree: make([]int64, n+2),
	}
}

func (b *BIT64) add(idx int, delta int64) {
	for i := idx; i <= b.n; i += i & -i {
		b.tree[i] += delta
	}
}

func (b *BIT64) sum(idx int) int64 {
	var res int64 = 0
	for i := idx; i > 0; i -= i & -i {
		res += b.tree[i]
	}
	return res
}

type MKAverage struct {
	m, k      int
	size      int
	pos       int
	elements  []int
	cntBIT    *BIT
	sumBIT    *BIT64
	totalSum  int64
	maxVal    int
}

func Constructor(m int, k int) MKAverage {
	const maxNum = 100000
	return MKAverage{
		m:        m,
		k:        k,
		elements: make([]int, m),
		cntBIT:   NewBIT(maxNum + 2),
		sumBIT:   NewBIT64(maxNum + 2),
		maxVal:   maxNum + 2,
	}
}

func (this *MKAverage) AddElement(num int) {
	if this.size == this.m {
		old := this.elements[this.pos]
		this.cntBIT.add(old, -1)
		this.sumBIT.add(old, -int64(old))
		this.totalSum -= int64(old)
	} else {
		this.size++
	}
	this.elements[this.pos] = num
	this.pos = (this.pos + 1) % this.m

	this.cntBIT.add(num, 1)
	this.sumBIT.add(num, int64(num))
	this.totalSum += int64(num)
}

func (this *MKAverage) sumSmallest(x int) int64 {
	if x <= 0 {
		return 0
	}
	pos := this.cntBIT.kth(x)
	cntBefore := this.cntBIT.sum(pos - 1)
	sumBefore := this.sumBIT.sum(pos - 1)
	remain := x - cntBefore
	return sumBefore + int64(remain*pos)
}

func (this *MKAverage) CalculateMKAverage() int {
	if this.size < this.m {
		return -1
	}
	midCount := this.m - 2*this.k

	sumSmallK := this.sumSmallest(this.k)
	sumSmallMMinusK := this.sumSmallest(this.m - this.k)
	sumLargeK := this.totalSum - sumSmallMMinusK

	middleSum := this.totalSum - sumSmallK - sumLargeK
	return int(middleSum / int64(midCount))
}

/**
 * Your MKAverage object will be instantiated and called as such:
 * obj := Constructor(m, k);
 * obj.AddElement(num);
 * param_2 := obj.CalculateMKAverage();
 */
```

## Ruby

```ruby
class BIT
  def initialize(n)
    @n = n
    @cnt = Array.new(n + 2, 0)
    @sum = Array.new(n + 2, 0)
  end

  def add(idx, delta)
    i = idx
    while i <= @n
      @cnt[i] += delta
      @sum[i] += delta * idx
      i += i & -i
    end
  end

  def prefix_cnt(idx)
    res = 0
    i = idx
    while i > 0
      res += @cnt[i]
      i -= i & -i
    end
    res
  end

  def prefix_sum(idx)
    res = 0
    i = idx
    while i > 0
      res += @sum[i]
      i -= i & -i
    end
    res
  end

  # sum of the smallest k elements currently stored
  def sum_smallest(k)
    return 0 if k <= 0
    pos = 0
    cnt_sofar = 0
    bit = 1
    while (bit << 1) <= @n
      bit <<= 1
    end
    while bit > 0
      nxt = pos + bit
      if nxt <= @n && cnt_sofar + @cnt[nxt] < k
        cnt_sofar += @cnt[nxt]
        pos = nxt
      end
      bit >>= 1
    end
    sum = prefix_sum(pos)
    remaining = k - cnt_sofar
    value = pos + 1
    sum + remaining * value
  end
end

class MKAverage
=begin
    :type m: Integer
    :type k: Integer
=end
  def initialize(m, k)
    @m = m
    @k = k
    @max_val = 100_000
    @bit = BIT.new(@max_val)
    @arr = []
    @head = 0
    @total_sum = 0
  end

=begin
    :type num: Integer
    :rtype: Void
=end
  def add_element(num)
    @arr << num
    @bit.add(num, 1)
    @total_sum += num
    if @arr.size - @head > @m
      old = @arr[@head]
      @head += 1
      @bit.add(old, -1)
      @total_sum -= old
    end
  end

=begin
    :rtype: Integer
=end
  def calculate_mk_average()
    cur_size = @arr.size - @head
    return -1 if cur_size < @m
    total = @total_sum
    small_k_sum = @bit.sum_smallest(@k)
    # sum of largest k = total - sum of smallest (m - k)
    large_k_sum = total - @bit.sum_smallest(@m - @k)
    middle_sum = total - small_k_sum - large_k_sum
    middle_sum / (@m - 2 * @k)
  end
end
```

## Scala

```scala
import java.util.{TreeMap, ArrayDeque}

class MKAverage(_m: Int, _k: Int) {
  private val m = _m
  private val k = _k

  private val low = new TreeMap[Int, Int]()
  private val mid = new TreeMap[Int, Int]()
  private val high = new TreeMap[Int, Int]()

  private var sizeLow = 0
  private var sizeMid = 0
  private var sizeHigh = 0
  private var sumMid: Long = 0L

  private val queue = new ArrayDeque[Int]()

  private def add(map: TreeMap[Int, Int], x: Int): Unit =
    map.put(x, map.getOrDefault(x, 0) + 1)

  private def remove(map: TreeMap[Int, Int], x: Int): Unit = {
    val cnt = map.get(x)
    if (cnt == 1) map.remove(x) else map.put(x, cnt - 1)
  }

  private def pollFirst(map: TreeMap[Int, Int]): Int = {
    val key = map.firstKey()
    remove(map, key)
    key
  }

  private def pollLast(map: TreeMap[Int, Int]): Int = {
    val key = map.lastKey()
    remove(map, key)
    key
  }

  private def insert(num: Int): Unit = {
    if (sizeLow > 0 && num <= low.lastKey()) {
      add(low, num); sizeLow += 1
    } else if (sizeHigh > 0 && num >= high.firstKey()) {
      add(high, num); sizeHigh += 1
    } else {
      add(mid, num); sumMid += num; sizeMid += 1
    }
  }

  private def delete(num: Int): Unit = {
    if (low.get(num) != null) {
      remove(low, num); sizeLow -= 1
    } else if (high.get(num) != null) {
      remove(high, num); sizeHigh -= 1
    } else {
      remove(mid, num); sumMid -= num; sizeMid -= 1
    }
  }

  private def balance(): Unit = {
    while (sizeLow > k) {
      val moved = pollLast(low)
      add(mid, moved); sumMid += moved
      sizeLow -= 1; sizeMid += 1
    }
    while (sizeLow < k && sizeMid > 0) {
      val moved = pollFirst(mid)
      add(low, moved); sumMid -= moved
      sizeLow += 1; sizeMid -= 1
    }
    while (sizeHigh > k) {
      val moved = pollFirst(high)
      add(mid, moved); sumMid += moved
      sizeHigh -= 1; sizeMid += 1
    }
    while (sizeHigh < k && sizeMid > 0) {
      val moved = pollLast(mid)
      add(high, moved); sumMid -= moved
      sizeHigh += 1; sizeMid -= 1
    }
  }

  def addElement(num: Int): Unit = {
    queue.addLast(num)
    if (queue.size() > m) {
      val old = queue.pollFirst()
      delete(old)
    }
    insert(num)
    balance()
  }

  def calculateMKAverage(): Int = {
    if (queue.size() < m) -1
    else {
      val denom = m - 2 * k
      (sumMid / denom).toInt
    }
  }
}
```

## Rust

```rust
use std::collections::{BTreeMap, VecDeque};

pub struct MKAverage {
    m: usize,
    k: usize,
    window: VecDeque<i32>,
    lo: BTreeMap<i32, usize>,
    mid: BTreeMap<i32, usize>,
    hi: BTreeMap<i32, usize>,
    lo_sz: usize,
    mid_sz: usize,
    hi_sz: usize,
    mid_sum: i64,
}

impl MKAverage {
    pub fn new(m: i32, k: i32) -> Self {
        MKAverage {
            m: m as usize,
            k: k as usize,
            window: VecDeque::new(),
            lo: BTreeMap::new(),
            mid: BTreeMap::new(),
            hi: BTreeMap::new(),
            lo_sz: 0,
            mid_sz: 0,
            hi_sz: 0,
            mid_sum: 0,
        }
    }

    fn add_to(&mut self, map: &mut BTreeMap<i32, usize>, val: i32) {
        *map.entry(val).or_insert(0) += 1;
    }

    fn remove_from(&mut self, map: &mut BTreeMap<i32, usize>, val: i32) {
        if let Some(cnt) = map.get_mut(&val) {
            if *cnt == 1 {
                map.remove(&val);
            } else {
                *cnt -= 1;
            }
        }
    }

    fn move_mid_to_lo(&mut self) {
        let v = *self.mid.iter().next().unwrap().0;
        self.remove_from(&mut self.mid, v);
        self.mid_sz -= 1;
        self.mid_sum -= v as i64;

        self.add_to(&mut self.lo, v);
        self.lo_sz += 1;
    }

    fn move_lo_to_mid(&mut self) {
        let v = *self.lo.iter().next_back().unwrap().0;
        self.remove_from(&mut self.lo, v);
        self.lo_sz -= 1;

        self.add_to(&mut self.mid, v);
        self.mid_sz += 1;
        self.mid_sum += v as i64;
    }

    fn move_mid_to_hi(&mut self) {
        let v = *self.mid.iter().next_back().unwrap().0;
        self.remove_from(&mut self.mid, v);
        self.mid_sz -= 1;
        self.mid_sum -= v as i64;

        self.add_to(&mut self.hi, v);
        self.hi_sz += 1;
    }

    fn move_hi_to_mid(&mut self) {
        let v = *self.hi.iter().next().unwrap().0;
        self.remove_from(&mut self.hi, v);
        self.hi_sz -= 1;

        self.add_to(&mut self.mid, v);
        self.mid_sz += 1;
        self.mid_sum += v as i64;
    }

    fn balance(&mut self) {
        let cur = self.window.len();
        let lo_target = std::cmp::min(self.k, cur);
        let hi_target = std::cmp::min(self.k, cur);

        while self.lo_sz > lo_target {
            self.move_lo_to_mid();
        }
        while self.lo_sz < lo_target {
            self.move_mid_to_lo();
        }

        while self.hi_sz > hi_target {
            self.move_hi_to_mid();
        }
        while self.hi_sz < hi_target {
            self.move_mid_to_hi();
        }

        loop {
            let mut changed = false;

            if self.lo_sz > 0 && self.mid_sz > 0 {
                let max_lo = *self.lo.iter().next_back().unwrap().0;
                let min_mid = *self.mid.iter().next().unwrap().0;
                if max_lo > min_mid {
                    // swap
                    self.remove_from(&mut self.lo, max_lo);
                    self.lo_sz -= 1;
                    self.add_to(&mut self.mid, max_lo);
                    self.mid_sz += 1;
                    self.mid_sum += max_lo as i64;

                    self.remove_from(&mut self.mid, min_mid);
                    self.mid_sz -= 1;
                    self.mid_sum -= min_mid as i64;
                    self.add_to(&mut self.lo, min_mid);
                    self.lo_sz += 1;

                    changed = true;
                }
            }

            if self.hi_sz > 0 && self.mid_sz > 0 {
                let min_hi = *self.hi.iter().next().unwrap().0;
                let max_mid = *self.mid.iter().next_back().unwrap().0;
                if min_hi < max_mid {
                    // swap
                    self.remove_from(&mut self.hi, min_hi);
                    self.hi_sz -= 1;
                    self.add_to(&mut self.mid, min_hi);
                    self.mid_sz += 1;
                    self.mid_sum += min_hi as i64;

                    self.remove_from(&mut self.mid, max_mid);
                    self.mid_sz -= 1;
                    self.mid_sum -= max_mid as i64;
                    self.add_to(&mut self.hi, max_mid);
                    self.hi_sz += 1;

                    changed = true;
                }
            }

            if !changed {
                break;
            }
        }
    }

    fn remove_old(&mut self, val: i32) {
        if self.lo.get(&val).is_some() {
            self.remove_from(&mut self.lo, val);
            self.lo_sz -= 1;
        } else if self.hi.get(&val).is_some() {
            self.remove_from(&mut self.hi, val);
            self.hi_sz -= 1;
        } else {
            self.remove_from(&mut self.mid, val);
            self.mid_sz -= 1;
            self.mid_sum -= val as i64;
        }
    }

    pub fn add_element(&mut self, num: i32) {
        self.window.push_back(num);
        self.add_to(&mut self.mid, num);
        self.mid_sz += 1;
        self.mid_sum += num as i64;

        self.balance();

        if self.window.len() > self.m {
            let old = self.window.pop_front().unwrap();
            self.remove_old(old);
            self.balance();
        }
    }

    pub fn calculate_mk_average(&self) -> i32 {
        if self.window.len() < self.m {
            return -1;
        }
        let cnt = (self.m - 2 * self.k) as i64;
        (self.mid_sum / cnt) as i32
    }
}

/**
 * Your MKAverage object will be instantiated and called as such:
 * let mut obj = MKAverage::new(m, k);
 * obj.add_element(num);
 * let ret_2: i32 = obj.calculate_mk_average();
 */
```

## Racket

```racket
(require racket/queue)

(define mk-average%
  (class object%
    (super-new)
    (init-field m k)

    (define max-val 100000)
    (define count-bit (make-vector (+ max-val 2) 0))
    (define sum-bit   (make-vector (+ max-val 2) 0))

    (define q (make-queue))
    (define cur-size 0)
    (define total-sum 0)

    ;; BIT update
    (define (bit-update! bit idx delta)
      (let ((n max-val))
        (let loop ((i idx))
          (when (<= i n)
            (vector-set! bit i (+ (vector-ref bit i) delta))
            (loop (+ i (bitwise-and i (- i))))))))

    ;; BIT prefix sum
    (define (bit-query bit idx)
      (let loop ((i idx) (res 0))
        (if (= i 0)
            res
            (loop (bitwise-and i (- i)) (+ res (vector-ref bit i))))))

    ;; Find smallest index such that cumulative count >= k
    (define (bit-find-kth k)
      (let ((idx 0)
            (mask (let loop ((p 1))
                    (if (> (* p 2) max-val) p (loop (* p 2))))))
        (let loop ()
          (when (> mask 0)
            (let ((next (+ idx mask)))
              (when (and (<= next max-val)
                         (< (vector-ref count-bit next) k))
                (set! idx next)
                (set! k (- k (vector-ref count-bit next)))))
            (set! mask (arithmetic-shift mask -1))
            (loop))))
        (+ idx 1))

    ;; Update both BITs and total sum
    (define (add-to-structures num delta) ; delta = +1 or -1
      (bit-update! count-bit num (* delta 1))
      (bit-update! sum-bit   num (* delta num))
      (set! total-sum (+ total-sum (* delta num))))

    (define/public (add-element num)
      (enqueue! q num)
      (add-to-structures num 1)
      (set! cur-size (+ cur-size 1))
      (when (> cur-size m)
        (define old (dequeue! q))
        (add-to-structures old -1)
        (set! cur-size (- cur-size 1))))

    ;; Sum of smallest k elements in current window
    (define (sum-first-k k)
      (if (= k 0)
          0
          (let* ((val (bit-find-kth k))
                 (cnt-before (bit-query count-bit (- val 1)))
                 (need (- k cnt-before))
                 (sum-before (bit-query sum-bit (- val 1))))
            (+ sum-before (* need val)))))

    (define/public (calculate-mk-average)
      (if (< cur-size m)
          -1
          (let* ((sum-small (sum-first-k k))
                 (sum-first-mk (sum-first-k (- m k)))
                 (sum-large (- total-sum sum-first-mk))
                 (mid-sum (- total-sum (+ sum-small sum-large)))
                 (denom (- m (* 2 k))))
            (quotient mid-sum denom))))))
```

## Erlang

```erlang
-spec mk_average_init_(M :: integer(), K :: integer()) -> any().
mk_average_init_(M, K) ->
    State = #{
        m => M,
        k => K,
        cnt => 0,
        queue => queue:new(),
        low => empty_set(),
        mid => empty_set(),
        high => empty_set(),
        sum_mid => 0
    },
    put(mk_state, State),
    ok.

-spec mk_average_add_element(Num :: integer()) -> any().
mk_average_add_element(Num) ->
    State = get(mk_state),
    M = maps:get(m, State),
    K = maps:get(k, State),

    %% add to queue and count
    Q1 = queue:in(Num, maps:get(queue, State)),
    Cnt1 = maps:get(cnt, State) + 1,

    %% insert and rebalance
    {Low1, Mid1, High1, SumMid1} =
        add_and_rebalance(maps:get(low, State), maps:get(mid, State),
                          maps:get(high, State), maps:get(sum_mid, State),
                          Num, K),

    %% if exceed window size, remove oldest
    {FinalState, FinalCnt, FinalQ} =
        case Cnt1 > M of
            true ->
                {{value, Old}, Q2} = queue:out(Q1),
                {Low2, Mid2, High2, SumMid2} =
                    remove_and_rebalance(Low1, Mid1, High1, SumMid1, Old, K),
                {maps:put(cnt, Cnt1 - 1,
                         maps:put(queue, Q2,
                                  maps:put(low, Low2,
                                           maps:put(mid, Mid2,
                                                    maps:put(high, High2,
                                                             maps:put(sum_mid, SumMid2,
                                                                      State))))),
                 Cnt1 - 1, Q2};
            false ->
                {maps:put(cnt, Cnt1,
                         maps:put(queue, Q1,
                                  maps:put(low, Low1,
                                           maps:put(mid, Mid1,
                                                    maps:put(high, High1,
                                                             maps:put(sum_mid, SumMid1,
                                                                      State))))),
                 Cnt1, Q1}
        end,

    put(mk_state, FinalState),
    ok.

-spec mk_average_calculate_mk_average() -> integer().
mk_average_calculate_mk_average() ->
    State = get(mk_state),
    M = maps:get(m, State),
    K = maps:get(k, State),
    Cnt = maps:get(cnt, State),
    case Cnt < M of
        true -> -1;
        false ->
            SumMid = maps:get(sum_mid, State),
            Divisor = M - 2 * K,
            SumMid div Divisor
    end.

%% ---------- Helper functions ----------
empty_set() ->
    #{tree => gb_trees:empty(), size => 0}.

set_size(Set) -> maps:get(size, Set).

insert(Set, Num) ->
    Tree = maps:get(tree, Set),
    Size = maps:get(size, Set),
    case gb_trees:lookup(Num, Tree) of
        {value, C} ->
            NewTree = gb_trees:update(Num, C + 1, Tree),
            #{tree => NewTree, size => Size};
        none ->
            NewTree = gb_trees:insert(Num, 1, Tree),
            #{tree => NewTree, size => Size + 1}
    end.

delete(Set, Num) ->
    Tree = maps:get(tree, Set),
    Size = maps:get(size, Set),
    case gb_trees:lookup(Num, Tree) of
        {value, C} when C > 1 ->
            NewTree = gb_trees:update(Num, C - 1, Tree),
            #{tree => NewTree, size => Size};
        {value, _} ->
            NewTree = gb_trees:delete(Num, Tree),
            #{tree => NewTree, size => Size - 1};
        none ->
            Set
    end.

extract_max(Set) ->
    Tree = maps:get(tree, Set),
    {Key, Count} = gb_trees:largest(Tree),
    case Count > 1 of
        true ->
            NewTree = gb_trees:update(Key, Count - 1, Tree),
            NewSet = #{tree => NewTree, size => maps:get(size, Set)},
            {Key, NewSet};
        false ->
            NewTree = gb_trees:delete(Key, Tree),
            NewSet = #{tree => NewTree, size => maps:get(size, Set) - 1},
            {Key, NewSet}
    end.

extract_min(Set) ->
    Tree = maps:get(tree, Set),
    {Key, Count} = gb_trees:smallest(Tree),
    case Count > 1 of
        true ->
            NewTree = gb_trees:update(Key, Count - 1, Tree),
            NewSet = #{tree => NewTree, size => maps:get(size, Set)},
            {Key, NewSet};
        false ->
            NewTree = gb_trees:delete(Key, Tree),
            NewSet = #{tree => NewTree, size => maps:get(size, Set) - 1},
            {Key, NewSet}
    end.

add_and_rebalance(Low, Mid, High, SumMid, Num, K) ->
    %% Insert into low first
    Low0 = insert(Low, Num),

    %% Move excess from low to mid if needed
    {Low1, Mid1, SumMid1} =
        case set_size(Low0) > K of
            true ->
                {MaxVal, LowTmp} = extract_max(Low0),
                MidTmp = insert(Mid, MaxVal),
                {LowTmp, MidTmp, SumMid + MaxVal};
            false -> {Low0, Mid, SumMid}
        end,

    %% Ensure high has K elements by moving from mid
    case set_size(High) < K of
        true when set_size(Mid1) > 0 ->
            {MinVal, MidTmp} = extract_min(Mid1),
            HighTmp = insert(High, MinVal),
            {Low1, MidTmp, HighTmp, SumMid1 - MinVal};
        _ -> {Low1, Mid1, High, SumMid1}
    end.

remove_and_rebalance(Low, Mid, High, SumMid, Old, K) ->
    case gb_trees:lookup(Old, maps:get(tree, Low)) of
        {value, _} ->
            Low0 = delete(Low, Old),
            rebalance_after_removal(Low0, Mid, High, SumMid, K);
        none ->
            case gb_trees:lookup(Old, maps:get(tree, High)) of
                {value, _} ->
                    High0 = delete(High, Old),
                    rebalance_after_removal(Low, Mid, High0, SumMid, K);
                none ->
                    Mid0 = delete(Mid, Old),
                    rebalance_after_removal(Low, Mid0, High, SumMid - Old, K)
            end
    end.

rebalance_after_removal(Low, Mid, High, SumMid, K) ->
    %% Low may be too small
    {Low1, Mid1, SumMid1} =
        case set_size(Low) < K of
            true when set_size(Mid) > 0 ->
                {MinVal, MidTmp} = extract_min(Mid),
                LowTmp = insert(Low, MinVal),
                {LowTmp, MidTmp, SumMid + MinVal};
            _ -> {Low, Mid, SumMid}
        end,

    %% High may be too small
    {Low2, Mid2, High1, SumMid2} =
        case set_size(High) < K of
            true when set_size(Mid1) > 0 ->
                {MaxVal, MidTmp} = extract_max(Mid1),
                HighTmp = insert(High, MaxVal),
                {Low1, MidTmp, HighTmp, SumMid1 - MaxVal};
            _ -> {Low1, Mid1, High, SumMid1}
        end,

    %% Low may be too big
    {Low3, Mid3, SumMid3} =
        case set_size(Low2) > K of
            true ->
                {MaxVal, LowTmp} = extract_max(Low2),
                MidTmp = insert(Mid2, MaxVal),
                {LowTmp, MidTmp, SumMid2 + MaxVal};
            false -> {Low2, Mid2, SumMid2}
        end,

    %% High may be too big
    case set_size(High1) > K of
        true ->
            {MinVal, HighTmp} = extract_min(High1),
            MidTmp = insert(Mid3, MinVal),
            {Low3, MidTmp, HighTmp, SumMid3 - MinVal};
        false -> {Low3, Mid3, High1, SumMid3}
    end.
```

## Elixir

```elixir
defmodule MKAverage do
  @spec init_(m :: integer, k :: integer) :: any
  def init_(m, k) do
    state = %{
      m: m,
      k: k,
      queue: :queue.new(),
      low: :gb_trees.empty(),
      mid: :gb_trees.empty(),
      high: :gb_trees.empty(),
      size_low: 0,
      size_mid: 0,
      size_high: 0,
      sum_mid: 0
    }

    Process.put(:mk_state, state)
    nil
  end

  @spec add_element(num :: integer) :: any
  def add_element(num) do
    state = Process.get(:mk_state)

    # enqueue new element
    {:ok, queue} = :queue.in_r(num, state.queue) |> then(&{:ok, &1})
    state = %{state | queue: queue}
    k = state.k

    # insert into appropriate set
    cond do
      state.size_low < k ->
        low = insert(state.low, num)
        state = %{state | low: low, size_low: state.size_low + 1}

      true ->
        max_low = get_max(state.low)

        if num <= max_low do
          # put into low then move its max to mid
          low = insert(state.low, num)
          {low, moved} = delete_one_and_get(low, max_low)
          mid = insert(state.mid, moved)

          state = %{
            state |
            low: low,
            mid: mid,
            size_mid: state.size_mid + 1,
            sum_mid: state.sum_mid + moved
          }
        else
          cond do
            state.size_high < k ->
              high = insert(state.high, num)
              state = %{state | high: high, size_high: state.size_high + 1}

            true ->
              min_high = get_min(state.high)

              if num >= min_high do
                # put into high then move its min to mid
                high = insert(state.high, num)
                {high, moved} = delete_one_and_get(high, min_high)
                mid = insert(state.mid, moved)

                state = %{
                  state |
                  high: high,
                  mid: mid,
                  size_mid: state.size_mid + 1,
                  sum_mid: state.sum_mid + moved
                }
              else
                # goes to mid directly
                mid = insert(state.mid, num)
                state = %{state | mid: mid, size_mid: state.size_mid + 1, sum_mid: state.sum_mid + num}
              end
          end
        end
    end

    # if window exceeds m, remove oldest element and rebalance
    if :queue.len(state.queue) > state.m do
      {{:value, old}, new_queue} = :queue.out_r(state.queue)
      state = %{state | queue: new_queue}

      cond do
        contains?(state.low, old) ->
          low = delete_one(state.low, old)
          state = %{state | low: low, size_low: state.size_low - 1}

        contains?(state.high, old) ->
          high = delete_one(state.high, old)
          state = %{state | high: high, size_high: state.size_high - 1}

        true ->
          mid = delete_one(state.mid, old)
          state = %{
            state |
            mid: mid,
            size_mid: state.size_mid - 1,
            sum_mid: state.sum_mid - old
          }
      end

      # rebalance low side if needed
      if state.size_low < k do
        moved = get_min(state.mid)
        mid = delete_one(state.mid, moved)
        low = insert(state.low, moved)

        state = %{
          state |
          low: low,
          mid: mid,
          size_low: state.size_low + 1,
          size_mid: state.size_mid - 1,
          sum_mid: state.sum_mid - moved
        }
      end

      # rebalance high side if needed
      if state.size_high < k do
        moved = get_max(state.mid)
        mid = delete_one(state.mid, moved)
        high = insert(state.high, moved)

        state = %{
          state |
          high: high,
          mid: mid,
          size_high: state.size_high + 1,
          size_mid: state.size_mid - 1,
          sum_mid: state.sum_mid - moved
        }
      end
    end

    Process.put(:mk_state, state)
    nil
  end

  @spec calculate_mk_average() :: integer
  def calculate_mk_average do
    state = Process.get(:mk_state)

    if :queue.len(state.queue) < state.m do
      -1
    else
      div(state.sum_mid, state.m - 2 * state.k)
    end
  end

  # ----- helper functions -----
  defp insert(tree, val) do
    case :gb_trees.lookup(val, tree) do
      {:value, cnt} -> :gb_trees.update(val, cnt + 1, tree)
      :none -> :gb_trees.insert(val, 1, tree)
    end
  end

  defp delete_one(tree, val) do
    case :gb_trees.lookup(val, tree) do
      {:value, 1} -> :gb_trees.delete(val, tree)
      {:value, cnt} -> :gb_trees.update(val, cnt - 1, tree)
      :none -> tree
    end
  end

  defp delete_one_and_get(tree, val) do
    {delete_one(tree, val), val}
  end

  defp contains?(tree, val) do
    case :gb_trees.lookup(val, tree) do
      :none -> false
      _ -> true
    end
  end

  defp get_min(tree) do
    {key, _} = :gb_trees.smallest(tree)
    key
  end

  defp get_max(tree) do
    {key, _} = :gb_trees.largest(tree)
    key
  end
end
```
