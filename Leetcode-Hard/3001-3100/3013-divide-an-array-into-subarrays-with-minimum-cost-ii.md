# 3013. Divide an Array Into Subarrays With Minimum Cost II

## Cpp

```cpp
class Solution {
public:
    long long minimumCost(vector<int>& nums, int k, int dist) {
        int n = nums.size();
        int m = k - 2; // number of additional starts needed after i1
        if (m == 0) return (long long)nums[0];
        
        multiset<int> small; // holds up to m smallest elements
        multiset<int> large;
        long long sumSmall = 0;
        
        auto add = [&](int x) {
            if ((int)small.size() < m) {
                small.insert(x);
                sumSmall += x;
            } else {
                auto itMaxSmall = prev(small.end());
                if (x < *itMaxSmall) {
                    int y = *itMaxSmall;
                    small.erase(itMaxSmall);
                    sumSmall -= y;
                    large.insert(y);
                    small.insert(x);
                    sumSmall += x;
                } else {
                    large.insert(x);
                }
            }
        };
        
        auto remove = [&](int x) {
            auto itS = small.find(x);
            if (itS != small.end()) {
                small.erase(itS);
                sumSmall -= x;
                if (!large.empty()) {
                    auto itL = large.begin(); // smallest in large
                    int y = *itL;
                    large.erase(itL);
                    small.insert(y);
                    sumSmall += y;
                }
            } else {
                auto itL = large.find(x);
                if (itL != large.end())
                    large.erase(itL);
            }
        };
        
        long long ans = LLONG_MAX;
        int r = 1; // rightmost index currently added to the window
        
        for (int i = 1; i < n; ++i) {
            int newR = min(i + dist, n - 1);
            while (r < newR) {
                ++r;
                add(nums[r]);
            }
            if (i > 1) {
                remove(nums[i]); // index i leaves the window
            }
            int windowSize = newR - i; // number of elements in [i+1, newR]
            if (windowSize >= m && (int)small.size() == m) {
                long long total = (long long)nums[0] + nums[i] + sumSmall;
                ans = min(ans, total);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    private java.util.TreeMap<Integer, Integer> small;
    private java.util.TreeMap<Integer, Integer> large;
    private int need;
    private int sizeSmall;
    private long sumSmall;

    public long minimumCost(int[] nums, int k, int dist) {
        int n = nums.length;
        need = k - 1;                     // number of starts after the first element
        small = new java.util.TreeMap<>();
        large = new java.util.TreeMap<>();
        sizeSmall = 0;
        sumSmall = 0L;

        long ans = Long.MAX_VALUE;
        int maxL = n - need;               // last possible start index for second subarray
        int R = 0;                         // right end of current window (inclusive)

        for (int L = 1; L <= maxL; ++L) {
            int maxR = Math.min(L + dist, n - 1);
            while (R < maxR) {             // expand window to the farthest allowed position
                ++R;
                add(nums[R]);
            }
            if (sizeSmall == need) {       // we have enough candidates in the window
                long candidate = (long) nums[0] + sumSmall;
                if (candidate < ans) ans = candidate;
            }
            remove(nums[L]);               // slide left border for next iteration
        }
        return ans;
    }

    private void add(int x) {
        if (sizeSmall < need) {                     // still need more smallest elements
            small.put(x, small.getOrDefault(x, 0) + 1);
            sizeSmall++;
            sumSmall += x;
        } else {
            int maxSmall = small.lastKey();         // largest among the selected smallest
            if (x < maxSmall) {
                decrement(small, maxSmall);
                sizeSmall--;
                sumSmall -= maxSmall;
                large.put(maxSmall, large.getOrDefault(maxSmall, 0) + 1);

                small.put(x, small.getOrDefault(x, 0) + 1);
                sizeSmall++;
                sumSmall += x;
            } else {
                large.put(x, large.getOrDefault(x, 0) + 1);
            }
        }
    }

    private void remove(int y) {
        if (small.containsKey(y)) {
            decrement(small, y);
            sizeSmall--;
            sumSmall -= y;
        } else {
            decrement(large, y);
        }
        // rebalance to keep exactly 'need' elements in small when possible
        while (sizeSmall < need && !large.isEmpty()) {
            int minLarge = large.firstKey();
            decrement(large, minLarge);
            small.put(minLarge, small.getOrDefault(minLarge, 0) + 1);
            sizeSmall++;
            sumSmall += minLarge;
        }
    }

    private void decrement(java.util.TreeMap<Integer, Integer> map, int key) {
        int cnt = map.get(key);
        if (cnt == 1) {
            map.remove(key);
        } else {
            map.put(key, cnt - 1);
        }
    }
}
```

## Python

```python
class Solution(object):
    def minimumCost(self, nums, k, dist):
        """
        :type nums: List[int]
        :type k: int
        :type dist: int
        :rtype: int
        """
        import heapq

        n = len(nums)
        m = k - 2  # number of additional starts needed besides nums[0] and i1
        INF = 10 ** 30
        ans = INF

        # dual heap structures
        small = []          # max-heap (store negative values) -> holds the m smallest elements
        large = []          # min-heap -> holds the rest
        delayed = {}        # value -> count of lazy deletions
        sum_small = 0       # sum of elements in 'small'
        small_size = 0      # effective size (excluding delayed)
        large_size = 0

        def prune(heap, is_small):
            while heap:
                val = -heap[0] if is_small else heap[0]
                cnt = delayed.get(val, 0)
                if cnt:
                    heapq.heappop(heap)
                    if cnt == 1:
                        del delayed[val]
                    else:
                        delayed[val] = cnt - 1
                else:
                    break

        def balance():
            nonlocal sum_small, small_size, large_size
            # ensure small holds exactly m elements (window always has at least m)
            while small_size > m:
                prune(small, True)
                val = -heapq.heappop(small)
                sum_small -= val
                small_size -= 1
                heapq.heappush(large, val)
                large_size += 1
                prune(small, True)

            while small_size < m:
                prune(large, False)
                if not large:
                    break
                val = heapq.heappop(large)
                large_size -= 1
                heapq.heappush(small, -val)
                sum_small += val
                small_size += 1
                prune(large, False)

        def add(val):
            nonlocal sum_small, small_size, large_size
            if small_size and val <= -small[0]:
                heapq.heappush(small, -val)
                sum_small += val
                small_size += 1
            else:
                heapq.heappush(large, val)
                large_size += 1
            balance()

        def remove(val):
            nonlocal sum_small, small_size, large_size
            delayed[val] = delayed.get(val, 0) + 1
            if small_size and val <= -small[0]:
                sum_small -= val
                small_size -= 1
                if -small[0] == val:
                    prune(small, True)
            else:
                large_size -= 1
                if large and large[0] == val:
                    prune(large, False)
            balance()

        # initialize window for i1 = 1
        i1_start = 1
        left = i1_start + 1
        right = min(i1_start + dist, n - 1)
        for idx in range(left, right + 1):
            add(nums[idx])

        max_i1 = n - (k - 1)  # inclusive upper bound for i1
        for i1 in range(1, max_i1 + 1):
            # compute cost with current window
            total = nums[0] + nums[i1] + sum_small
            if total < ans:
                ans = total

            # slide window to next i1
            if i1 == max_i1:
                break
            out_idx = i1 + 1
            remove(nums[out_idx])
            new_right = i1 + dist + 1
            if new_right <= n - 1:
                add(nums[new_right])

        return ans
```

## Python3

```python
import heapq
from typing import List

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        t = k - 2  # number of additional elements needed besides i1 and i_k-1
        
        if t == 0:  # k == 2 (not in constraints but handle)
            return nums[0] + min(nums[1:])
        
        # heaps and auxiliary structures
        small = []          # max‑heap for the t smallest values (store (-val, idx))
        large = []          # min‑heap for the rest (store (val, idx))
        loc = {}            # idx -> 'small' or 'large'
        removed = set()     # indices lazily deleted from heaps
        
        small_cnt = 0
        large_cnt = 0
        sum_small = 0       # sum of values inside 'small'

        def prune(heap):
            while heap and heap[0][1] in removed:
                heapq.heappop(heap)

        def balance():
            nonlocal small_cnt, large_cnt, sum_small
            # ensure size constraints
            while small_cnt > t:
                prune(small)
                if not small: break
                v, i = heapq.heappop(small)
                v = -v
                sum_small -= v
                small_cnt -= 1
                heapq.heappush(large, (v, i))
                loc[i] = 'large'
                large_cnt += 1

            while small_cnt < t and large_cnt > 0:
                prune(large)
                if not large: break
                v, i = heapq.heappop(large)
                large_cnt -= 1
                heapq.heappush(small, (-v, i))
                loc[i] = 'small'
                small_cnt += 1
                sum_small += v

            # maintain ordering property
            while small_cnt > 0 and large_cnt > 0:
                prune(small)
                prune(large)
                if not small or not large: break
                max_small = -small[0][0]
                min_large = large[0][0]
                if max_small <= min_large:
                    break
                # swap tops
                v_s, i_s = heapq.heappop(small)
                v_s = -v_s
                sum_small -= v_s
                small_cnt -= 1

                v_l, i_l = heapq.heappop(large)
                large_cnt -= 1

                heapq.heappush(small, (-v_l, i_l))
                loc[i_l] = 'small'
                small_cnt += 1
                sum_small += v_l

                heapq.heappush(large, (v_s, i_s))
                loc[i_s] = 'large'
                large_cnt += 1

        def insert(idx):
            nonlocal small_cnt, large_cnt, sum_small
            val = nums[idx]
            heapq.heappush(large, (val, idx))
            loc[idx] = 'large'
            large_cnt += 1
            balance()

        def erase(idx):
            nonlocal small_cnt, large_cnt, sum_small
            if idx not in loc:
                return
            typ = loc.pop(idx)
            removed.add(idx)
            if typ == 'small':
                small_cnt -= 1
                sum_small -= nums[idx]
            else:
                large_cnt -= 1
            balance()

        # initialize window for i1 = 1
        cur_left = 2
        cur_right = min(1 + dist, n - 1)
        if cur_left <= cur_right:
            for i in range(cur_left, cur_right + 1):
                insert(i)

        INF = 10**20
        ans = INF

        for s in range(1, n):
            # window size
            win_size = max(0, cur_right - cur_left + 1) if cur_left <= cur_right else 0
            if win_size >= t:
                cand = nums[0] + nums[s] + sum_small
                if cand < ans:
                    ans = cand

            if s == n - 1:
                break

            # slide window: remove index s+1 (old left bound)
            idx_remove = s + 1
            if cur_left <= cur_right and cur_left == idx_remove:
                erase(idx_remove)
                cur_left += 1
            else:
                # even if not present, just move left pointer
                cur_left = max(cur_left, idx_remove + 1)

            # add new right index if any
            new_r = min(s + 1 + dist, n - 1)
            while cur_right < new_r:
                cur_right += 1
                insert(cur_right)

        return ans if ans != INF else -1
```

## C

```c
#include <limits.h>
#include <stdlib.h>

typedef struct {
    long long val;
    int idx;
} Node;

typedef struct {
    Node *a;
    int sz;
    int isMax;   // 1 for max-heap, 0 for min-heap
} Heap;

static inline int cmp(Heap *h, Node x, Node y) {
    if (x.val != y.val)
        return h->isMax ? (x.val > y.val) : (x.val < y.val);
    return h->isMax ? (x.idx > y.idx) : (x.idx < y.idx);
}

static void heapSwap(Heap *h, int i, int j) {
    Node t = h->a[i];
    h->a[i] = h->a[j];
    h->a[j] = t;
}

static void heapPush(Heap *h, Node nd) {
    int i = ++h->sz;
    h->a[i] = nd;
    while (i > 1 && cmp(h, h->a[i], h->a[i >> 1])) {
        heapSwap(h, i, i >> 1);
        i >>= 1;
    }
}

static Node heapTop(Heap *h) { return h->a[1]; }

static void heapPop(Heap *h) {
    if (h->sz == 0) return;
    h->a[1] = h->a[h->sz];
    h->sz--;
    int i = 1;
    while (1) {
        int l = i << 1, r = l + 1, best = i;
        if (l <= h->sz && cmp(h, h->a[l], h->a[best])) best = l;
        if (r <= h->sz && cmp(h, h->a[r], h->a[best])) best = r;
        if (best == i) break;
        heapSwap(h, i, best);
        i = best;
    }
}

/* Remove invalid nodes from top */
static void heapClean(Heap *h, const char *inWindow) {
    while (h->sz && !inWindow[h->a[1].idx]) heapPop(h);
}

long long minimumCost(int* nums, int numsSize, int k, int dist) {
    int n = numsSize;
    int m = k - 2;                     // number of additional starts after i1
    if (m == 0) {                      // only first and second subarray needed
        long long best = LLONG_MAX;
        for (int i = 1; i < n; ++i) {
            long long cand = (long long)nums[0] + nums[i];
            if (cand < best) best = cand;
        }
        return best;
    }

    char *inWindow = calloc(n, sizeof(char));   // 0/1 flag
    char *belong   = calloc(n, sizeof(char));   // 0 none, 1 small, 2 large

    Heap small, large;
    small.sz = large.sz = 0;
    small.isMax = 1;               // max-heap for selected smallest values
    large.isMax = 0;               // min-heap for the rest
    small.a = malloc((n + 5) * sizeof(Node));
    large.a = malloc((n + 5) * sizeof(Node));

    long long sumSmall = 0;
    int cntSmall = 0;              // number of valid elements currently in 'small'

    /* initial window for i1 = 1 */
    int curL = 2;                  // first possible start after second subarray
    int curR = dist + 1;
    if (curR >= n) curR = n - 1;

    for (int idx = curL; idx <= curR; ++idx) {
        inWindow[idx] = 1;
        Node nd = { (long long)nums[idx], idx };
        if (cntSmall < m) {
            heapPush(&small, nd);
            belong[idx] = 1;
            sumSmall += nd.val;
            cntSmall++;
        } else {
            heapClean(&small, inWindow);
            long long topVal = (small.sz ? small.a[1].val : LLONG_MAX);
            if (nd.val <= topVal) {
                Node move = heapTop(&small);
                heapPop(&small);
                belong[move.idx] = 2;
                sumSmall -= move.val;
                cntSmall--;
                heapPush(&large, move);

                heapPush(&small, nd);
                belong[idx] = 1;
                sumSmall += nd.val;
                cntSmall++;
            } else {
                heapPush(&large, nd);
                belong[idx] = 2;
            }
        }
    }

    long long answer = LLONG_MAX;

    for (int i1 = 1; i1 < n - 1; ++i1) {
        int L = i1 + 1;
        int R = i1 + dist;
        if (R >= n) R = n - 1;

        /* remove indices that left the window */
        while (curL < L) {
            if (curL <= curR && inWindow[curL]) {
                if (belong[curL] == 1) {
                    sumSmall -= nums[curL];
                    cntSmall--;
                }
                inWindow[curL] = 0;
                belong[curL] = 0;
            }
            ++curL;
        }

        /* add new indices entering the window */
        while (curR < R) {
            ++curR;
            inWindow[curR] = 1;
            Node nd = { (long long)nums[curR], curR };
            if (cntSmall < m) {
                heapPush(&small, nd);
                belong[curR] = 1;
                sumSmall += nd.val;
                cntSmall++;
            } else {
                heapClean(&small, inWindow);
                long long topVal = (small.sz ? small.a[1].val : LLONG_MAX);
                if (nd.val <= topVal) {
                    Node move = heapTop(&small);
                    heapPop(&small);
                    belong[move.idx] = 2;
                    sumSmall -= move.val;
                    cntSmall--;
                    heapPush(&large, move);

                    heapPush(&small, nd);
                    belong[curR] = 1;
                    sumSmall += nd.val;
                    cntSmall++;
                } else {
                    heapPush(&large, nd);
                    belong[curR] = 2;
                }
            }
        }

        /* clean tops */
        heapClean(&small, inWindow);
        heapClean(&large, inWindow);

        /* rebalance to have exactly m valid elements in small if possible */
        while (cntSmall < m && large.sz) {
            heapClean(&large, inWindow);
            if (!large.sz) break;
            Node nd = heapTop(&large);
            heapPop(&large);
            belong[nd.idx] = 1;
            heapPush(&small, nd);
            sumSmall += nd.val;
            cntSmall++;
        }
        while (cntSmall > m) {
            heapClean(&small, inWindow);
            Node nd = heapTop(&small);
            heapPop(&small);
            belong[nd.idx] = 2;
            sumSmall -= nd.val;
            cntSmall--;
            heapPush(&large, nd);
        }

        int windowSize = (R >= L) ? (R - L + 1) : 0;
        if (windowSize >= m && cntSmall == m) {
            long long cand = (long long)nums[0] + nums[i1] + sumSmall;
            if (cand < answer) answer = cand;
        }
    }

    free(inWindow);
    free(belong);
    free(small.a);
    free(large.a);
    return answer;
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
        public int N;
        public long[] Tree;
        public Fenwick(int n)
        {
            N = n;
            Tree = new long[n + 2];
        }
        public void Add(int idx, long delta)
        {
            for (int i = idx; i <= N; i += i & -i)
                Tree[i] += delta;
        }
        public long PrefixSum(int idx)
        {
            long res = 0;
            for (int i = idx; i > 0; i -= i & -i)
                res += Tree[i];
            return res;
        }
    }

    private static int FindByOrder(Fenwick bit, int k)
    {
        int idx = 0;
        int mask = 1;
        while ((mask << 1) <= bit.N) mask <<= 1;
        for (; mask > 0; mask >>= 1)
        {
            int next = idx + mask;
            if (next <= bit.N && bit.Tree[next] < k)
            {
                idx = next;
                k -= (int)bit.Tree[next];
            }
        }
        return idx + 1; // 1‑based index where cumulative count >= original k
    }

    public long MinimumCost(int[] nums, int k, int dist)
    {
        int n = nums.Length;
        int need = k - 2; // number of additional starts after the second subarray

        // coordinate compression
        int[] sortedVals = (int[])nums.Clone();
        Array.Sort(sortedVals);
        int uniqCount = 1;
        for (int i = 1; i < n; ++i)
            if (sortedVals[i] != sortedVals[uniqCount - 1])
                sortedVals[uniqCount++] = sortedVals[i];
        Array.Resize(ref sortedVals, uniqCount);

        // map each value to its compressed index (1‑based for Fenwick)
        int[] compIdx = new int[n];
        var dict = new Dictionary<int, int>(uniqCount);
        for (int i = 0; i < uniqCount; ++i)
            dict[sortedVals[i]] = i + 1;
        for (int i = 0; i < n; ++i)
            compIdx[i] = dict[nums[i]];

        Fenwick cntBIT = new Fenwick(uniqCount);
        Fenwick sumBIT = new Fenwick(uniqCount);

        void AddVal(int pos)
        {
            int idx = compIdx[pos];
            cntBIT.Add(idx, 1);
            sumBIT.Add(idx, nums[pos]);
        }
        void RemoveVal(int pos)
        {
            int idx = compIdx[pos];
            cntBIT.Add(idx, -1);
            sumBIT.Add(idx, -nums[pos]);
        }

        long GetSmallestSum(int needCount)
        {
            if (needCount <= 0) return 0;
            int pos = FindByOrder(cntBIT, needCount); // 1‑based compressed index
            long cntBefore = cntBIT.PrefixSum(pos - 1);
            long sumBefore = sumBIT.PrefixSum(pos - 1);
            int remaining = needCount - (int)cntBefore;
            long val = sortedVals[pos - 1];
            return sumBefore + remaining * val;
        }

        // initial window for i = 1
        int left = 2; // first index inside the window
        int right = Math.Min(1 + dist, n - 1);
        for (int p = left; p <= right; ++p) AddVal(p);

        long answer = long.MaxValue;

        for (int i = 1; i <= n - 2; ++i)
        {
            int windowSize = right - left + 1;
            if (windowSize >= need)
            {
                long sumSmallest = GetSmallestSum(need);
                long total = (long)nums[0] + nums[i] + sumSmallest;
                if (total < answer) answer = total;
            }

            // slide window for next i
            if (left <= right)
            {
                RemoveVal(left);
                left++;
            }
            int newRight = Math.Min(i + 1 + dist, n - 1);
            while (right < newRight)
            {
                ++right;
                AddVal(right);
            }
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number} dist
 * @return {number}
 */
var minimumCost = function(nums, k, dist) {
    const n = nums.length;
    const m = k - 2; // number of additional starts needed after i1

    // coordinate compression for all values except the first (index 0)
    const vals = [];
    for (let i = 1; i < n; ++i) vals.push(nums[i]);
    const uniq = Array.from(new Set(vals)).sort((a, b) => a - b);
    const idxMap = new Map();
    for (let i = 0; i < uniq.length; ++i) idxMap.set(uniq[i], i + 1); // 1‑based

    class BIT {
        constructor(size, values) {
            this.n = size;
            this.cnt = new Array(size + 2).fill(0);
            this.sum = new Array(size + 2).fill(0);
            this.vals = values; // 0‑based array of original numbers
        }
        add(pos, deltaCnt, deltaSum) {
            for (let i = pos; i <= this.n; i += i & -i) {
                this.cnt[i] += deltaCnt;
                this.sum[i] += deltaSum;
            }
        }
        prefixCount(pos) {
            let res = 0;
            for (let i = pos; i > 0; i -= i & -i) res += this.cnt[i];
            return res;
        }
        prefixSum(pos) {
            let res = 0;
            for (let i = pos; i > 0; i -= i & -i) res += this.sum[i];
            return res;
        }
        totalCount() {
            return this.prefixCount(this.n);
        }
        // sum of smallest k elements currently stored
        sumSmallest(k) {
            if (k <= 0) return 0;
            let idx = 0;
            let bitMask = 1 << Math.floor(Math.log2(this.n));
            let cntSoFar = 0;
            for (let step = bitMask; step > 0; step >>= 1) {
                const next = idx + step;
                if (next <= this.n && cntSoFar + this.cnt[next] < k) {
                    idx = next;
                    cntSoFar += this.cnt[next];
                }
            }
            // idx now has cumulative count < k, position idx+1 reaches >=k
            const sumBefore = this.prefixSum(idx);
            const need = k - cntSoFar; // how many from value at idx+1 we need
            const value = this.vals[idx]; // because vals is 0‑based and idx is count of elements before
            return sumBefore + need * value;
        }
    }

    const bit = new BIT(uniq.length, uniq);
    let ans = Infinity;

    // initial window for i = 1
    let i = 1;
    let R = Math.min(i + dist, n - 1);
    for (let p = i + 1; p <= R; ++p) {
        const id = idxMap.get(nums[p]);
        bit.add(id, 1, nums[p]);
    }

    for (; i <= n - 2; ++i) {
        if (bit.totalCount() >= m) {
            const cur = nums[0] + nums[i] + bit.sumSmallest(m);
            if (cur < ans) ans = cur;
        }
        // slide window: remove leftmost element of current window
        const leftRemove = i + 1;
        if (leftRemove <= R) {
            const idRem = idxMap.get(nums[leftRemove]);
            bit.add(idRem, -1, -nums[leftRemove]);
        }
        // compute new right bound for next i
        const nextR = Math.min(i + 1 + dist, n - 1);
        if (nextR > R) {
            const idAdd = idxMap.get(nums[nextR]);
            bit.add(idAdd, 1, nums[nextR]);
        }
        R = nextR;
    }

    return ans;
};
```

## Typescript

```typescript
function minimumCost(nums: number[], k: number, dist: number): number {
    const n = nums.length;
    const need = k - 3; // number of interior selections needed
    // coordinate compression
    const uniq = Array.from(new Set(nums)).sort((a, b) => a - b);
    const idxMap = new Map<number, number>();
    for (let i = 0; i < uniq.length; i++) idxMap.set(uniq[i], i + 1); // 1-indexed
    const comp: number[] = new Array(n);
    for (let i = 0; i < n; i++) comp[i] = idxMap.get(nums[i])!;

    class Fenwick {
        n: number;
        treeCnt: number[];
        treeSum: number[];
        vals: number[];
        constructor(vals: number[]) {
            this.vals = vals;
            this.n = vals.length;
            this.treeCnt = new Array(this.n + 2).fill(0);
            this.treeSum = new Array(this.n + 2).fill(0);
        }
        add(pos: number, deltaCnt: number, deltaVal: number): void {
            for (let i = pos; i <= this.n; i += i & -i) {
                this.treeCnt[i] += deltaCnt;
                this.treeSum[i] += deltaVal;
            }
        }
        prefixCount(pos: number): number {
            let res = 0;
            for (let i = pos; i > 0; i -= i & -i) res += this.treeCnt[i];
            return res;
        }
        prefixSum(pos: number): number {
            let res = 0;
            for (let i = pos; i > 0; i -= i & -i) res += this.treeSum[i];
            return res;
        }
        kth(k: number): number { // smallest index with cumulative count >= k
            let idx = 0;
            let bitMask = 1 << Math.floor(Math.log2(this.n));
            while (bitMask !== 0) {
                const next = idx + bitMask;
                if (next <= this.n && this.treeCnt[next] < k) {
                    k -= this.treeCnt[next];
                    idx = next;
                }
                bitMask >>= 1;
            }
            return idx + 1; // 1-indexed
        }
        sumSmallest(t: number): number {
            if (t <= 0) return 0;
            const total = this.prefixCount(this.n);
            if (total < t) return Number.MAX_SAFE_INTEGER;
            const idx = this.kth(t);
            const cntPrev = this.prefixCount(idx - 1);
            const sumPrev = this.prefixSum(idx - 1);
            const needCnt = t - cntPrev;
            const val = this.vals[idx - 1];
            return sumPrev + needCnt * val;
        }
    }

    const bit = new Fenwick(uniq);
    let ans = Number.MAX_SAFE_INTEGER;
    let curJ = 0; // current right endpoint candidate

    for (let i = 1; i <= n - 2; i++) {
        const maxJ = Math.min(i + dist, n - 1);
        if (curJ < i + 1) curJ = i + 1;

        // evaluate current curJ
        if (curJ <= maxJ && (need === 0 || curJ - i - 1 >= need)) {
            const sumSmall = need === 0 ? 0 : bit.sumSmallest(need);
            const cost = nums[0] + nums[i] + nums[curJ] + sumSmall;
            if (cost < ans) ans = cost;
        }

        while (curJ < maxJ) {
            curJ++;
            // add new interior element at index curJ-1
            if (need > 0) {
                const idxAdd = curJ - 1;
                bit.add(comp[idxAdd], 1, nums[idxAdd]);
            }
            if (need === 0 || curJ - i - 1 >= need) {
                const sumSmall = need === 0 ? 0 : bit.sumSmallest(need);
                const cost = nums[0] + nums[i] + nums[curJ] + sumSmall;
                if (cost < ans) ans = cost;
            }
        }

        // remove element that leaves the interior window for next i
        if (need > 0) {
            const outIdx = i + 1;
            if (outIdx < n) {
                bit.add(comp[outIdx], -1, -nums[outIdx]);
            }
        }
    }

    return ans;
}
```

## Php

```php
class Solution {
    private function bitAdd(&$bit, $idx, $delta) {
        $n = count($bit);
        while ($idx < $n) {
            $bit[$idx] += $delta;
            $idx += $idx & -$idx;
        }
    }

    private function bitSum(&$bit, $idx) {
        $res = 0;
        while ($idx > 0) {
            $res += $bit[$idx];
            $idx -= $idx & -$idx;
        }
        return $res;
    }

    // sum of smallest $k$ values in the current multiset
    private function smallestKSum(&$cntBIT, &$sumBIT, $values, $k) {
        $n = count($cntBIT) - 1; // last valid index
        $idx = 0;
        $cnt = 0;

        // highest power of two <= n
        $bitMask = 1;
        while (($bitMask << 1) <= $n) {
            $bitMask <<= 1;
        }

        for ($d = $bitMask; $d > 0; $d >>= 1) {
            $next = $idx + $d;
            if ($next <= $n && $cnt + $cntBIT[$next] < $k) {
                $idx = $next;
                $cnt += $cntBIT[$next];
            }
        }

        $pos = $idx + 1;                 // first index where cumulative count >= k
        $countPrev = $cnt;               // counts before $pos
        $sumPrev = $this->bitSum($sumBIT, $idx);
        $need = $k - $countPrev;         // how many from value at $pos we need
        $valueAtPos = $values[$pos - 1]; // values array is 0-indexed

        return $sumPrev + $need * $valueAtPos;
    }

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @param Integer $dist
     * @return Integer
     */
    function minimumCost($nums, $k, $dist) {
        $n = count($nums);
        $need = $k - 1; // number of starts after the first element

        // coordinate compression for nums[1..n-1]
        $vals = array_slice($nums, 1);
        $sorted = $vals;
        sort($sorted, SORT_NUMERIC);
        $sorted = array_values(array_unique($sorted));
        $m = count($sorted);

        $comp = [];
        foreach ($sorted as $i => $v) {
            $comp[$v] = $i + 1; // 1‑based index for BIT
        }

        $cntBIT = array_fill(0, $m + 2, 0);
        $sumBIT = array_fill(0, $m + 2, 0);

        $ans = PHP_INT_MAX;
        $L = 1; // left bound of the sliding window (inclusive)

        for ($R = 1; $R < $n; $R++) {
            $val = $nums[$R];
            $idxComp = $comp[$val];
            $this->bitAdd($cntBIT, $idxComp, 1);
            $this->bitAdd($sumBIT, $idxComp, $val);

            // shrink window to keep size <= dist+1 (i.e., indices difference <= dist)
            while ($L < $R - $dist) {
                $oldVal = $nums[$L];
                $oldIdx = $comp[$oldVal];
                $this->bitAdd($cntBIT, $oldIdx, -1);
                $this->bitAdd($sumBIT, $oldIdx, -$oldVal);
                $L++;
            }

            $windowSize = $R - $L + 1;
            if ($windowSize >= $need) {
                $smallSum = $this->smallestKSum($cntBIT, $sumBIT, $sorted, $need);
                $candidate = $nums[0] + $smallSum;
                if ($candidate < $ans) {
                    $ans = $candidate;
                }
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    struct Elem {
        var value: Int
        var idx: Int
    }
    
    class Heap {
        private var data: [Elem] = []
        private let cmp: (Elem, Elem) -> Bool
        
        init(_ comparator: @escaping (Elem, Elem) -> Bool) {
            self.cmp = comparator
        }
        
        var count: Int { data.count }
        
        func peek() -> Elem? {
            return data.first
        }
        
        func push(_ element: Elem) {
            data.append(element)
            siftUp(data.count - 1)
        }
        
        @discardableResult
        func pop() -> Elem? {
            guard !data.isEmpty else { return nil }
            let top = data[0]
            let last = data.removeLast()
            if !data.isEmpty {
                data[0] = last
                siftDown(0)
            }
            return top
        }
        
        private func siftUp(_ index: Int) {
            var child = index
            while child > 0 {
                let parent = (child - 1) >> 1
                if cmp(data[child], data[parent]) {
                    data.swapAt(child, parent)
                    child = parent
                } else { break }
            }
        }
        
        private func siftDown(_ index: Int) {
            var parent = index
            while true {
                let left = parent * 2 + 1
                let right = left + 1
                var candidate = parent
                if left < data.count && cmp(data[left], data[candidate]) {
                    candidate = left
                }
                if right < data.count && cmp(data[right], data[candidate]) {
                    candidate = right
                }
                if candidate == parent { break }
                data.swapAt(parent, candidate)
                parent = candidate
            }
        }
    }
    
    func minimumCost(_ nums: [Int], _ k: Int, _ dist: Int) -> Int {
        let n = nums.count
        let need = k - 2   // number of additional starts after the second subarray
        
        if need == 0 { // not expected per constraints but handle safely
            var ans = Int.max
            for i in 1..<n {
                ans = min(ans, nums[0] + nums[i])
            }
            return ans
        }
        
        var removed = [Bool](repeating: false, count: n)
        var inSelected = [Bool](repeating: false, count: n)
        var sumSelected = 0
        
        let selectedHeap = Heap { (a: Elem, b: Elem) -> Bool in
            if a.value == b.value { return a.idx > b.idx } // max-heap
            return a.value > b.value
        }
        let otherHeap = Heap { (a: Elem, b: Elem) -> Bool in
            if a.value == b.value { return a.idx < b.idx } // min-heap
            return a.value < b.value
        }
        
        func cleanTop(_ heap: Heap) {
            while let top = heap.peek(), removed[top.idx] {
                _ = heap.pop()
            }
        }
        
        func add(_ val: Int, _ idx: Int) {
            let elem = Elem(value: val, idx: idx)
            if selectedHeap.count < need {
                selectedHeap.push(elem)
                inSelected[idx] = true
                sumSelected += val
            } else {
                cleanTop(selectedHeap)
                if let top = selectedHeap.peek(), val < top.value {
                    // move top to other heap
                    _ = selectedHeap.pop()
                    sumSelected -= top.value
                    inSelected[top.idx] = false
                    otherHeap.push(top)
                    
                    // insert new element into selected
                    selectedHeap.push(elem)
                    inSelected[idx] = true
                    sumSelected += val
                } else {
                    otherHeap.push(elem)
                }
            }
        }
        
        func remove(_ idx: Int) {
            if removed[idx] { return }
            removed[idx] = true
            if inSelected[idx] {
                sumSelected -= nums[idx]
                inSelected[idx] = false
            }
        }
        
        func rebalance() {
            cleanTop(selectedHeap)
            cleanTop(otherHeap)
            while selectedHeap.count > need {
                if let top = selectedHeap.pop() {
                    sumSelected -= top.value
                    inSelected[top.idx] = false
                    otherHeap.push(top)
                }
                cleanTop(selectedHeap)
            }
            while selectedHeap.count < need {
                cleanTop(otherHeap)
                guard let elem = otherHeap.pop() else { break }
                selectedHeap.push(elem)
                inSelected[elem.idx] = true
                sumSelected += elem.value
            }
        }
        
        var answer = Int.max
        
        // initial i = 1
        if n <= 1 { return answer }
        let firstI = 1
        let startL = firstI + 1
        let endR = min(firstI + dist, n - 1)
        if startL <= endR {
            for idx in startL...endR {
                add(nums[idx], idx)
            }
        }
        rebalance()
        if selectedHeap.count == need {
            answer = min(answer, nums[0] + nums[firstI] + sumSelected)
        }
        
        // iterate i from 2 to n-1-need
        if n - 1 - need >= 2 {
            for i in 2...n - 1 - need {
                // remove previous left index (i)
                let removeIdx = i
                remove(removeIdx)
                
                // add new right index if within bounds
                let newR = i + dist
                if newR <= n - 1 {
                    add(nums[newR], newR)
                }
                
                rebalance()
                if selectedHeap.count == need {
                    let cost = nums[0] + nums[i] + sumSelected
                    if cost < answer { answer = cost }
                }
            }
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
import java.util.TreeMap

class Solution {
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
        fun first(): Int = map.firstKey()
        fun last(): Int = map.lastKey()
        fun isEmpty(): Boolean = map.isEmpty()
    }

    fun minimumCost(nums: IntArray, k: Int, dist: Int): Long {
        val n = nums.size
        val need = k - 2 // number of additional starts after the second subarray
        if (need == 0) {
            var minVal = Int.MAX_VALUE
            for (i in 1 until n) {
                if (nums[i] < minVal) minVal = nums[i]
            }
            return nums[0].toLong() + minVal
        }

        val small = MultiSet() // holds the need smallest values
        val large = MultiSet()
        var sumSmall = 0L

        fun addValue(v: Int) {
            if (small.size < need) {
                small.add(v)
                sumSmall += v
            } else {
                val maxSmall = small.last()
                if (v < maxSmall) {
                    // move the current largest of small to large
                    small.remove(maxSmall)
                    sumSmall -= maxSmall
                    large.add(maxSmall)

                    small.add(v)
                    sumSmall += v
                } else {
                    large.add(v)
                }
            }
        }

        fun removeValue(v: Int) {
            if (small.map.containsKey(v)) {
                small.remove(v)
                sumSmall -= v
                // rebalance if needed
                if (!large.isEmpty()) {
                    val minLarge = large.first()
                    large.remove(minLarge)
                    small.add(minLarge)
                    sumSmall += minLarge
                }
            } else {
                large.remove(v)
            }
        }

        var leftIdx = 2
        var rightIdx = kotlin.math.min(1 + dist, n - 1)
        if (leftIdx <= rightIdx) {
            for (idx in leftIdx..rightIdx) addValue(nums[idx])
        }

        var answer = Long.MAX_VALUE

        for (i in 1 until n - 1) { // i is the start index of the second subarray
            val windowSize = if (rightIdx >= leftIdx) rightIdx - leftIdx + 1 else 0
            if (windowSize >= need) {
                val total = nums[0].toLong() + nums[i].toLong() + sumSmall
                if (total < answer) answer = total
            }
            if (i == n - 2) break

            // slide window: remove element at i+1 (old left)
            val remIdx = i + 1
            if (remIdx >= leftIdx && remIdx <= rightIdx) {
                removeValue(nums[remIdx])
                leftIdx++
            }

            // possibly extend right side
            val newRight = kotlin.math.min(i + 1 + dist, n - 1)
            if (newRight > rightIdx) {
                for (idx in (rightIdx + 1)..newRight) addValue(nums[idx])
                rightIdx = newRight
            }
        }

        return answer
    }
}
```

## Dart

```dart
class Solution {
  int minimumCost(List<int> nums, int k, int dist) {
    int n = nums.length;
    int need = k - 2; // number of additional starts after the second one
    if (need == 0) {
      int minVal = nums[1];
      for (int i = 2; i < n; ++i) {
        if (nums[i] < minVal) minVal = nums[i];
      }
      return nums[0] + minVal;
    }

    // two multisets: small holds the need smallest values, large holds the rest
    var small = SplayTreeMap<int, int>();
    var large = SplayTreeMap<int, int>();
    int smallSize = 0;
    int largeSize = 0;
    int sumSmall = 0;

    void addToMap(SplayTreeMap<int, int> map, int v) {
      map[v] = (map[v] ?? 0) + 1;
    }

    void removeFromMap(SplayTreeMap<int, int> map, int v) {
      int cnt = map[v]!;
      if (cnt == 1) {
        map.remove(v);
      } else {
        map[v] = cnt - 1;
      }
    }

    void rebalance() {
      // ensure smallSize == need
      while (smallSize > need) {
        int maxSmall = small.lastKey()!;
        removeFromMap(small, maxSmall);
        smallSize--;
        sumSmall -= maxSmall;
        addToMap(large, maxSmall);
        largeSize++;
      }
      while (smallSize < need && largeSize > 0) {
        int minLarge = large.firstKey()!;
        removeFromMap(large, minLarge);
        largeSize--;
        addToMap(small, minLarge);
        smallSize++;
        sumSmall += minLarge;
      }
    }

    void insertVal(int v) {
      if (smallSize < need) {
        addToMap(small, v);
        smallSize++;
        sumSmall += v;
      } else {
        int maxSmall = small.lastKey()!;
        if (v < maxSmall) {
          // move maxSmall to large
          removeFromMap(small, maxSmall);
          smallSize--;
          sumSmall -= maxSmall;
          addToMap(large, maxSmall);
          largeSize++;

          // insert v into small
          addToMap(small, v);
          smallSize++;
          sumSmall += v;
        } else {
          addToMap(large, v);
          largeSize++;
        }
      }
    }

    void eraseVal(int v) {
      if (small.containsKey(v)) {
        removeFromMap(small, v);
        smallSize--;
        sumSmall -= v;
        rebalance();
      } else {
        // must be in large
        removeFromMap(large, v);
        largeSize--;
        rebalance();
      }
    }

    // initialize window for i = 1 (second subarray starts at index 1)
    int initRight = (dist < n - 1) ? dist : n - 1;
    for (int idx = 2; idx <= initRight; ++idx) {
      insertVal(nums[idx]);
    }

    int answer = 1 << 60;

    for (int i = 1; i < n; ++i) {
      int right = i + dist;
      if (right > n - 1) right = n - 1;
      int totalCandidates = right - i; // number of indices after i within window
      if (totalCandidates >= need) {
        int cost = nums[0] + nums[i] + sumSmall;
        if (cost < answer) answer = cost;
      }

      // prepare for next i
      int leftIdx = i + 1;
      if (leftIdx <= right) {
        eraseVal(nums[leftIdx]);
      }
      int newRight = i + 1 + dist;
      if (newRight > n - 1) newRight = n - 1;
      if (newRight > right) {
        insertVal(nums[newRight]);
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
	"math"
	"sort"
)

type BIT struct {
	n   int
	cnt []int
	sum []int64
}

func NewBIT(n int) *BIT {
	return &BIT{
		n:   n,
		cnt: make([]int, n+2),
		sum: make([]int64, n+2),
	}
}

func (b *BIT) add(idx int, deltaCnt int, deltaSum int64) {
	for i := idx; i <= b.n; i += i & -i {
		b.cnt[i] += deltaCnt
		b.sum[i] += deltaSum
	}
}

func (b *BIT) prefixCount(idx int) int {
	res := 0
	for i := idx; i > 0; i -= i & -i {
		res += b.cnt[i]
	}
	return res
}

func (b *BIT) prefixSum(idx int) int64 {
	var res int64 = 0
	for i := idx; i > 0; i -= i & -i {
		res += b.sum[i]
	}
	return res
}

// sum of smallest t elements, assumes total count >= t
func (b *BIT) sumSmallest(t int, uniq []int) int64 {
	if t == 0 {
		return 0
	}
	lo, hi := 1, b.n
	for lo < hi {
		mid := (lo + hi) >> 1
		if b.prefixCount(mid) >= t {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	idx := lo
	cntBefore := b.prefixCount(idx - 1)
	sumBefore := b.prefixSum(idx - 1)
	need := t - cntBefore
	val := uniq[idx-1]
	return sumBefore + int64(need)*int64(val)
}

func minimumCost(nums []int, k int, dist int) int64 {
	n := len(nums)
	if k == 1 {
		return int64(nums[0])
	}
	need := k - 2 // number of interior starts needed

	// coordinate compression
	vals := make([]int, n)
	copy(vals, nums)
	sort.Ints(vals)
	uniq := []int{}
	for _, v := range vals {
		if len(uniq) == 0 || uniq[len(uniq)-1] != v {
			uniq = append(uniq, v)
		}
	}
	m := len(uniq)
	idxMap := make(map[int]int, m)
	for i, v := range uniq {
		idxMap[v] = i + 1 // BIT is 1-indexed
	}

	bit := NewBIT(m)

	// initial window for i = 1 (second subarray starts at index 1)
	left := 2
	right := dist + 1
	if right > n-1 {
		right = n - 1
	}
	for pos := left; pos <= right; pos++ {
		bit.add(idxMap[nums[pos]], 1, int64(nums[pos]))
	}

	ans := int64(math.MaxInt64)

	// iterate i from 1 to n-2 (i is start of second subarray)
	for i := 1; i <= n-2; i++ {
		totalCnt := bit.prefixCount(m)
		if totalCnt >= need {
			sumSmall := bit.sumSmallest(need, uniq)
			cand := int64(nums[0]) + int64(nums[i]) + sumSmall
			if cand < ans {
				ans = cand
			}
		}
		// slide window for next i
		// remove element at position i+1 (leaving the window)
		if i+1 <= n-1 {
			bit.add(idxMap[nums[i+1]], -1, -int64(nums[i+1]))
		}
		newRight := i + dist + 1
		if newRight > n-1 {
			newRight = n - 1
		}
		for pos := right + 1; pos <= newRight; pos++ {
			bit.add(idxMap[nums[pos]], 1, int64(nums[pos]))
		}
		right = newRight
	}

	return ans
}
```

## Ruby

```ruby
def minimum_cost(nums, k, dist)
  n = nums.length
  m = k - 2
  return Float::INFINITY if m < 0

  # Simple heap implementation (min-heap)
  class MinHeap
    def initialize
      @a = []
    end

    def push(val)
      @a << val
      i = @a.size - 1
      while i > 0
        p = (i - 1) / 2
        break if @a[p] <= @a[i]
        @a[p], @a[i] = @a[i], @a[p]
        i = p
      end
    end

    def top
      @a[0]
    end

    def pop
      return nil if @a.empty?
      root = @a[0]
      last = @a.pop
      unless @a.empty?
        @a[0] = last
        i = 0
        n = @a.size
        loop do
          l = i * 2 + 1
          r = i * 2 + 2
          smallest = i
          smallest = l if l < n && @a[l] < @a[smallest]
          smallest = r if r < n && @a[r] < @a[smallest]
          break if smallest == i
          @a[i], @a[smallest] = @a[smallest], @a[i]
          i = smallest
        end
      end
      root
    end

    def empty?
      @a.empty?
    end

    def size
      @a.size
    end
  end

  # Heaps for the two groups
  small = MinHeap.new   # max-heap via storing negative values
  large = MinHeap.new   # normal min-heap

  del_small = Hash.new(0)
  del_large = Hash.new(0)

  sum_small = 0
  sz_small = 0
  sz_large = 0

  # helpers to clean lazy deletions
  clean_small = lambda do
    while !small.empty?
      val = -small.top
      if del_small[val] > 0
        del_small[val] -= 1
        small.pop
      else
        break
      end
    end
  end

  clean_large = lambda do
    while !large.empty? && del_large[large.top] > 0
      val = large.top
      del_large[val] -= 1
      large.pop
    end
  end

  # add a value into the sliding window structure
  add_val = lambda do |x|
    clean_small.call
    if sz_small < m
      small.push(-x)
      sum_small += x
      sz_small += 1
    else
      max_small = -small.top
      if x < max_small
        # move current largest of small to large
        small.pop
        sum_small -= max_small
        sz_small -= 1
        large.push(max_small)
        sz_large += 1

        # insert new value into small
        small.push(-x)
        sum_small += x
        sz_small += 1
      else
        large.push(x)
        sz_large += 1
      end
    end
  end

  # remove a value that leaves the window
  remove_val = lambda do |x|
    clean_small.call
    if !small.empty? && x <= -small.top
      del_small[x] += 1
      sum_small -= x
      sz_small -= 1
    else
      del_large[x] += 1
      sz_large -= 1
    end

    # rebalance to ensure small has m elements if possible
    clean_small.call
    clean_large.call
    while sz_small < m && !large.empty?
      val = large.pop
      sz_large -= 1
      del_large[val] -= 0 # just to keep hash entry, no effect
      small.push(-val)
      sum_small += val
      sz_small += 1
      clean_large.call
    end
  end

  ans = (1 << 62)

  i = 1
  r = [i + dist, n - 1].min
  # initialize window for i = 1 (indices i+1 .. r)
  ((i + 1)..r).each { |idx| add_val.call(nums[idx]) }

  while i <= n - 2
    if (r - i) >= m && sz_small == m
      cur = nums[0] + nums[i] + sum_small
      ans = cur if cur < ans
    end

    break if i == n - 2

    # slide window: remove leftmost element of current window
    left_idx = i + 1
    if left_idx <= r
      remove_val.call(nums[left_idx])
    end

    i += 1
    new_r = [i + dist, n - 1].min
    if new_r > r
      add_val.call(nums[new_r])
    end
    r = new_r
  end

  ans
end
```

## Scala

```scala
object Solution {
  import java.util.PriorityQueue
  case class Entry(value: Int, idx: Int)

  def minimumCost(nums: Array[Int], k: Int, dist: Int): Long = {
    val n = nums.length
    val need = k - 2 // number of additional starts needed besides i1

    // Heaps
    val selected = new PriorityQueue[Entry]((a: Entry, b: Entry) => Integer.compare(b.value, a.value)) // max-heap
    val other = new PriorityQueue[Entry]((a: Entry, b: Entry) => Integer.compare(a.value, b.value))   // min-heap

    // Lazy deletion flags
    val delSel = Array.fill[Boolean](n)(false)
    val delOther = Array.fill[Boolean](n)(false)

    // State of each index: 0=not in window,1=in selected,2=in other
    val state = Array.fill[Int](n)(0)

    var sumSelected: Long = 0L
    var selCount = 0

    def cleanSel(): Unit = {
      while (!selected.isEmpty && delSel(selected.peek().idx)) {
        val e = selected.poll()
        delSel(e.idx) = false
      }
    }

    def cleanOther(): Unit = {
      while (!other.isEmpty && delOther(other.peek().idx)) {
        val e = other.poll()
        delOther(e.idx) = false
      }
    }

    def addIdx(idx: Int): Unit = {
      if (need == 0) return
      val v = nums(idx)
      cleanSel()
      if (selCount < need) {
        selected.offer(Entry(v, idx))
        sumSelected += v
        selCount += 1
        state(idx) = 1
      } else {
        // compare with current max in selected
        val top = selected.peek()
        if (v < top.value) {
          // move top to other
          cleanSel()
          val moved = selected.poll()
          sumSelected -= moved.value
          selCount -= 1
          state(moved.idx) = 2
          other.offer(moved)

          // insert new into selected
          selected.offer(Entry(v, idx))
          sumSelected += v
          selCount += 1
          state(idx) = 1
        } else {
          other.offer(Entry(v, idx))
          state(idx) = 2
        }
      }
    }

    def removeIdx(idx: Int): Unit = {
      val st = state(idx)
      if (st == 1) {
        delSel(idx) = true
        sumSelected -= nums(idx)
        selCount -= 1
      } else if (st == 2) {
        delOther(idx) = true
      }
      state(idx) = 0

      // rebalance: fill selected up to need
      cleanSel()
      while (selCount < need && !other.isEmpty) {
        cleanOther()
        if (other.isEmpty) return
        val e = other.poll()
        // ensure not lazily deleted
        if (delOther(e.idx)) {
          delOther(e.idx) = false
        } else {
          selected.offer(e)
          sumSelected += e.value
          selCount += 1
          state(e.idx) = 1
        }
      }
    }

    // Initialize window for i1 = 1
    var i1 = 1
    val leftInit = i1 + 1
    var right = math.min(i1 + dist, n - 1)
    var idx = leftInit
    while (idx <= right) {
      addIdx(idx)
      idx += 1
    }

    var answer: Long = Long.MaxValue

    // Iterate over possible i1 positions
    while (i1 <= n - 2) {
      val leftIdx = i1 + 1
      val windowSize = right - leftIdx + 1
      if (windowSize >= need && selCount == need) {
        val total = nums(i1).toLong + sumSelected
        if (total < answer) answer = total
      }

      // slide window for next i1
      removeIdx(leftIdx)

      i1 += 1
      val newRight = math.min(i1 + dist, n - 1)
      if (newRight > right) {
        addIdx(newRight)
      }
      right = newRight
    }

    nums(0).toLong + answer
  }
}
```

## Rust

```rust
use std::cmp::min;
use std::collections::HashMap;

struct Fenwick {
    n: usize,
    cnt: Vec<i32>,
    sum: Vec<i64>,
    vals: Vec<i64>, // 0‑based values for each index (1‑based in BIT)
}

impl Fenwick {
    fn new(vals: Vec<i64>) -> Self {
        let n = vals.len();
        Fenwick {
            n,
            cnt: vec![0; n + 2],
            sum: vec![0; n + 2],
            vals,
        }
    }

    fn add(&mut self, mut idx: usize, delta_cnt: i32, delta_sum: i64) {
        while idx <= self.n {
            self.cnt[idx] += delta_cnt;
            self.sum[idx] += delta_sum;
            idx += idx & (!idx + 1);
        }
    }

    fn prefix_cnt(&self, mut idx: usize) -> i32 {
        let mut res = 0;
        while idx > 0 {
            res += self.cnt[idx];
            idx &= idx - 1;
        }
        res
    }

    fn prefix_sum(&self, mut idx: usize) -> i64 {
        let mut res = 0i64;
        while idx > 0 {
            res += self.sum[idx];
            idx &= idx - 1;
        }
        res
    }

    fn total_cnt(&self) -> usize {
        self.prefix_cnt(self.n) as usize
    }

    // sum of smallest k elements currently stored (k <= total count)
    fn sum_smallest_k(&self, k: usize) -> i64 {
        if k == 0 {
            return 0;
        }
        let mut lo = 1usize;
        let mut hi = self.n;
        while lo < hi {
            let mid = (lo + hi) / 2;
            if self.prefix_cnt(mid) as usize >= k {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        let idx = lo; // first index where cumulative count >= k
        let cnt_before = if idx > 1 { self.prefix_cnt(idx - 1) as usize } else { 0 };
        let sum_before = if idx > 1 { self.prefix_sum(idx - 1) } else { 0 };
        let need = k - cnt_before; // number taken from value at idx
        let val = self.vals[idx - 1];
        sum_before + (need as i64) * val
    }
}

impl Solution {
    pub fn minimum_cost(nums: Vec<i32>, k: i32, dist: i32) -> i64 {
        let n = nums.len();
        if k == 2 {
            // not required by constraints but handle safely
            let mut min_val = i64::MAX;
            for i in 1..n {
                min_val = min(min_val, nums[i] as i64);
            }
            return nums[0] as i64 + min_val;
        }

        let m = (k - 2) as usize; // number of additional starts needed after the second one
        // coordinate compression
        let mut uniq: Vec<i64> = nums.iter().map(|&x| x as i64).collect();
        uniq.sort_unstable();
        uniq.dedup();

        let mut idx_map: HashMap<i64, usize> = HashMap::new();
        for (i, &v) in uniq.iter().enumerate() {
            idx_map.insert(v, i + 1); // 1‑based
        }

        let mut comp_idx = vec![0usize; n];
        for i in 0..n {
            comp_idx[i] = *idx_map.get(&(nums[i] as i64)).unwrap();
        }

        let mut bit = Fenwick::new(uniq);
        let mut ans = i64::MAX;
        let mut r: usize = 0; // current rightmost index included in the window

        for i in 1..n {
            // expand right bound to min(i+dist, n-1)
            let limit = min((i as i32 + dist) as usize, n - 1);
            while r < limit {
                r += 1;
                bit.add(comp_idx[r], 1, nums[r] as i64);
            }

            // current window should be [i+1 .. limit]
            let cnt = bit.total_cnt();
            if cnt >= m {
                let sum_smallest = bit.sum_smallest_k(m);
                let total = nums[0] as i64 + nums[i] as i64 + sum_smallest;
                if total < ans {
                    ans = total;
                }
            }

            // remove index i+1 for next iteration
            let leave = i + 1;
            if leave <= n - 1 {
                bit.add(comp_idx[leave], -1, -(nums[leave] as i64));
            }
        }

        ans
    }
}
```

## Racket

```racket
(require racket/priority-queue)

(define (minimum-cost nums k dist)
  (let* ([arr (list->vector nums)]
         [n (vector-length arr)]
         [small-pq (make-pq (lambda (a b) (< (first a) (first b))))]
         [large-pq (make-pq (lambda (a b) (< (first a) (first b))))]
         [status (make-vector n 'none)]
         [need (sub1 k)]                         ; k-1
         [INF (arithmetic-shift 1 62)]
         [ans (box INF)]
         [total 0]                               ; elements in current window
         [small-size 0]                          ; number of elems kept in small-pq
         [sum-small 0])                          ; sum of those elems

    (define (pq-empty? q) (not (pq-peek q)))

    (define (clean-small!)
      (let loop ()
        (when (and (not (pq-empty? small-pq))
                   (let* ([top (pq-peek small-pq)]
                          [idx (second top)])
                     (not (eq? (vector-ref status idx) 'small))))
          (pq-pop! small-pq)
          (loop))))

    (define (clean-large!)
      (let loop ()
        (when (and (not (pq-empty? large-pq))
                   (let* ([top (pq-peek large-pq)]
                          [idx (second top)])
                     (not (eq? (vector-ref status idx) 'large))))
          (pq-pop! large-pq)
          (loop))))

    (define (rebalance-after-removal)
      (clean-small!)
      (let loop ()
        (when (< small-size (min need total))
          (clean-large!)
          (unless (pq-empty? large-pq)
            (let* ([top (pq-pop! large-pq)]
                   [val (first top)]
                   [idx (second top)])
              (vector-set! status idx 'small)
              (set! sum-small (+ sum-small val))
              (set! small-size (+ small-size 1))
              (pq-insert! small-pq (list (- val) idx))))
          (loop))))

    (define (insert-idx idx)
      (let ([val (vector-ref arr idx)])
        (set! total (+ total 1))
        (if (< small-size need)
            (begin
              (pq-insert! small-pq (list (- val) idx))
              (vector-set! status idx 'small)
              (set! sum-small (+ sum-small val))
              (set! small-size (+ small-size 1)))
            (begin
              (clean-small!)
              (let* ([max-small-val (- (first (pq-peek small-pq)))])
                (if (< val max-small-val)
                    (begin
                      ;; move current largest of small to large
                      (let* ([pop (pq-pop! small-pq)]
                             [sval (- (first pop))]
                             [sidx (second pop)])
                        (vector-set! status sidx 'large)
                        (set! sum-small (- sum-small sval))
                        (set! small-size (- small-size 1))
                        (pq-insert! large-pq (list sval sidx)))
                      ;; insert new value into small
                      (pq-insert! small-pq (list (- val) idx))
                      (vector-set! status idx 'small)
                      (set! sum-small (+ sum-small val))
                      (set! small-size (+ small-size 1)))
                    (begin
                      (pq-insert! large-pq (list val idx))
                      (vector-set! status idx 'large)))))))))

    (define (remove-idx idx)
      (let ([st (vector-ref status idx)])
        (cond [(eq? st 'small)
               (set! sum-small (- sum-small (vector-ref arr idx)))
               (set! small-size (- small-size 1))
               (vector-set! status idx 'removed)]
              [(eq? st 'large)
               (vector-set! status idx 'removed)]
              [else (void)]))
      (set! total (- total 1))
      (rebalance-after-removal))

    ;; main sliding window
    (let loop ((L 1) (R -1))
      (when (<= L (- n 1))
        (let ([newR (min (+ L dist) (- n 1))])
          (let insert-loop ((i (+ R 1)))
            (when (<= i newR)
              (insert-idx i)
              (set! R i)
              (insert-loop (+ i 1)))))
        ;; evaluate answer
        (when (>= total need)
          (let ([candidate (+ (vector-ref arr 0) sum-small)])
            (when (< candidate (unbox ans))
              (set-box! ans candidate))))
        ;; slide left bound
        (remove-idx L)
        (loop (+ L 1) R)))
    (unbox ans)))
```

## Erlang

```erlang
-module(solution).
-export([minimum_cost/3]).

-define(INF, 1 bsl 62).

minimum_cost(Nums, K, Dist) ->
    Tuple = list_to_tuple(Nums),
    N = tuple_size(Tuple),
    KMinus2 = K - 2,
    MaxI = N - (K - 1),
    loop(1, MaxI, Dist, N, Tuple, gb_sets:new(), gb_sets:new(),
         0, 0, ?INF, KMinus2).

%% Main iteration over possible i (first cut index)
loop(I, MaxI, _Dist, _N, _Tuple, Small, Large, SumSmall, Right, Ans, _KMinus2) when I > MaxI ->
    Ans;
loop(I, MaxI, Dist, N, Tuple, Small, Large, SumSmall, Right, Ans, KMinus2) ->
    %% Remove element that leaves the window
    {Small1, Large1, Sum1} =
        if I > 1 ->
                RemIdx = I,
                ValRem = element(RemIdx + 1, Tuple),
                remove_elem(RemIdx, ValRem, Small, Large, SumSmall, KMinus2);
           true -> {Small, Large, SumSmall}
        end,

    NewRight = erlang:min(I + Dist, N - 1),

    %% Expand window to the new right bound
    {FinalRight, Small2, Large2, Sum2} =
        expand(Right, NewRight, Tuple, Small1, Large1, Sum1, KMinus2),

    %% Compute answer if we have enough elements in small set
    Ans1 = case gb_sets:size(Small2) == KMinus2 of
               true ->
                   Total = element(1, Tuple) + element(I + 1, Tuple) + Sum2,
                   erlang:min(Ans, Total);
               false -> Ans
           end,

    loop(I + 1, MaxI, Dist, N, Tuple, Small2, Large2, Sum2, FinalRight, Ans1, KMinus2).

%% Expand the right side of the sliding window
expand(Right, Target, _Tuple, Small, Large, SumSmall, _KMinus2) when Right == Target ->
    {Right, Small, Large, SumSmall};
expand(Right, Target, Tuple, Small, Large, SumSmall, KMinus2) ->
    Next = Right + 1,
    Val = element(Next + 1, Tuple),
    {S1, L1, Sum1} = add_elem(Next, Val, Small, Large, SumSmall, KMinus2),
    expand(Next, Target, Tuple, S1, L1, Sum1, KMinus2).

%% Insert a new element into the two-set structure
add_elem(Index, Value, Small, Large, SumSmall, KMinus2) ->
    case gb_sets:size(Small) < KMinus2 of
        true ->
            {gb_sets:add({Value, Index}, Small), Large, SumSmall + Value};
        false ->
            Largest = gb_sets:largest(Small),
            case Value < element(1, Largest) of
                true ->
                    SmallTmp = gb_sets:delete_any(Largest, Small),
                    LargeTmp = gb_sets:add(Largest, Large),
                    SumTmp = SumSmall - element(1, Largest),
                    {gb_sets:add({Value, Index}, SmallTmp), LargeTmp, SumTmp + Value};
                false ->
                    {Small, gb_sets:add({Value, Index}, Large), SumSmall}
            end
    end.

%% Remove an element that leaves the sliding window
remove_elem(Index, Value, Small, Large, SumSmall, KMinus2) ->
    Elem = {Value, Index},
    case gb_sets:is_member(Elem, Small) of
        true ->
            Small1 = gb_sets:delete_any(Elem, Small),
            Sum1 = SumSmall - Value,
            case {gb_sets:size(Small1) < KMinus2, gb_sets:is_empty(Large)} of
                {true, false} ->
                    MinElem = gb_sets:smallest(Large),
                    Large1 = gb_sets:delete_any(MinElem, Large),
                    Small2 = gb_sets:add(MinElem, Small1),
                    Sum2 = Sum1 + element(1, MinElem),
                    {Small2, Large1, Sum2};
                _ ->
                    {Small1, Large, Sum1}
            end;
        false ->
            case gb_sets:is_member(Elem, Large) of
                true -> {Small, gb_sets:delete_any(Elem, Large), SumSmall};
                false -> {Small, Large, SumSmall} % should not happen
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  defmodule BIT do
    defstruct cnt: nil, sum: nil, size: 0, values: []

    def new(values) do
      m = length(values)
      %BIT{
        cnt: :array.new(m + 2, default: 0),
        sum: :array.new(m + 2, default: 0),
        size: m,
        values: values
      }
    end

    def add(bit, idx, delta) do
      val = Enum.at(bit.values, idx - 1)
      {new_cnt, new_sum} = add_loop(bit.cnt, bit.sum, idx, delta, val, bit.size)
      %BIT{bit | cnt: new_cnt, sum: new_sum}
    end

    defp add_loop(cnt_arr, sum_arr, idx, delta, val, size) do
      if idx > size do
        {cnt_arr, sum_arr}
      else
        cur_cnt = :array.get(idx, cnt_arr)
        cur_sum = :array.get(idx, sum_arr)
        cnt_arr2 = :array.set(idx, cur_cnt + delta, cnt_arr)
        sum_arr2 = :array.set(idx, cur_sum + delta * val, sum_arr)
        add_loop(cnt_arr2, sum_arr2, idx + lowbit(idx), delta, val, size)
      end
    end

    defp lowbit(x), do: band(x, -x)

    def prefix(bit, idx) do
      prefix_loop(bit.cnt, bit.sum, idx, 0, 0)
    end

    defp prefix_loop(_cnt_arr, _sum_arr, idx, acc_cnt, acc_sum) when idx <= 0,
      do: {acc_cnt, acc_sum}

    defp prefix_loop(cnt_arr, sum_arr, idx, acc_cnt, acc_sum) do
      cnt = :array.get(idx, cnt_arr)
      sum = :array.get(idx, sum_arr)
      prefix_loop(cnt_arr, sum_arr, band(idx, idx - 1), acc_cnt + cnt, acc_sum + sum)
    end

    def find_kth(bit, k) do
      mask = highest_one_bit(bit.size)
      find_kth_loop(bit.cnt, k, 0, mask, bit.size)
    end

    defp highest_one_bit(n) do
      p = 1
      while p * 2 <= n do
        p = p * 2
      end
      p
    end

    defp find_kth_loop(_cnt_arr, _k, idx, 0, _size), do: idx + 1

    defp find_kth_loop(cnt_arr, k, idx, mask, size) do
      nxt = idx + mask
      if nxt <= size and (:array.get(nxt, cnt_arr) < k) do
        new_k = k - :array.get(nxt, cnt_arr)
        find_kth_loop(cnt_arr, new_k, nxt, mask >>> 1, size)
      else
        find_kth_loop(cnt_arr, k, idx, mask >>> 1, size)
      end
    end

    def sum_of_smallest(bit, k) when k <= 0, do: 0

    def sum_of_smallest(bit, k) do
      idx = find_kth(bit, k)
      {cnt_before, sum_before} = prefix(bit, idx - 1)
      remaining = k - cnt_before
      val = Enum.at(bit.values, idx - 1)
      sum_before + remaining * val
    end
  end

  @spec minimum_cost(nums :: [integer], k :: integer, dist :: integer) :: integer
  def minimum_cost(nums, k, dist) do
    n = length(nums)

    # coordinate compression
    uniq_vals = nums |> Enum.uniq() |> Enum.sort()
    comp_map = for {v, i} <- Enum.with_index(uniq_vals), into: %{}, do: {v, i + 1}
    comp_list = Enum.map(nums, &Map.fetch!(comp_map, &1))

    nums_arr = :array.from_list(nums)
    comp_arr = :array.from_list(comp_list)

    bit = BIT.new(uniq_vals)

    left = 1
    right = min(dist, n - 1)

    bit =
      Enum.reduce(left..right, bit, fn idx, acc ->
        BIT.add(acc, :array.get(idx, comp_arr), 1)
      end)

    total_needed = k - 2
    max_i1 = n - 2
    inf = 1 <<< 60

    iter(0, max_i1, left, right, bit, total_needed, nums_arr, comp_arr, inf, dist)
  end

  defp iter(i1, max_i1, left, right, bit, need, nums_arr, comp_arr, best, dist) when i1 > max_i1,
    do: best

  defp iter(i1, max_i1, left, right, bit, need, nums_arr, comp_arr, best, dist) do
    window_size = right - left + 1

    best =
      if window_size >= need do
        sum_smallest = BIT.sum_of_smallest(bit, need)
        cost = :array.get(0, nums_arr) + :array.get(i1, nums_arr) + sum_smallest
        if cost < best, do: cost, else: best
      else
        best
      end

    # slide window
    bit =
      if left <= right do
        BIT.add(bit, :array.get(left, comp_arr), -1)
      else
        bit
      end

    new_left = left + 1
    new_right_candidate = i1 + dist + 1

    {bit, new_right} =
      if new_right_candidate < :array.size(comp_arr) do
        {BIT.add(bit, :array.get(new_right_candidate, comp_arr), 1), new_right_candidate}
      else
        {bit, right}
      end

    iter(i1 + 1, max_i1, new_left, new_right, bit, need, nums_arr, comp_arr, best, dist)
  end
end
```
