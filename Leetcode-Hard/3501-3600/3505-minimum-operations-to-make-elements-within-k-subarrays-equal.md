# 3505. Minimum Operations to Make Elements Within K Subarrays Equal

## Cpp

```cpp
class Solution {
public:
    long long minOperations(vector<int>& nums, int x, int k) {
        int n = nums.size();
        int m = n - x + 1; // number of windows
        vector<long long> cost(m);
        
        multiset<int> low, high;
        long long sumLow = 0, sumHigh = 0;
        int need = (x + 1) / 2; // size of low
        
        auto rebalance = [&]() {
            if (!low.empty() && !high.empty() && *low.rbegin() > *high.begin()) {
                auto itLow = prev(low.end());
                int vLow = *itLow;
                low.erase(itLow);
                sumLow -= vLow;
                
                auto itHigh = high.begin();
                int vHigh = *itHigh;
                high.erase(itHigh);
                sumHigh -= vHigh;
                
                low.insert(vHigh);
                sumLow += vHigh;
                high.insert(vLow);
                sumHigh += vLow;
            }
            while ((int)low.size() > need) {
                auto it = prev(low.end());
                int v = *it;
                low.erase(it);
                sumLow -= v;
                high.insert(v);
                sumHigh += v;
            }
            while ((int)low.size() < need && !high.empty()) {
                auto it = high.begin();
                int v = *it;
                high.erase(it);
                sumHigh -= v;
                low.insert(v);
                sumLow += v;
            }
        };
        
        // initial window
        for (int i = 0; i < x; ++i) {
            int val = nums[i];
            if (low.empty() || val <= *low.rbegin()) {
                low.insert(val);
                sumLow += val;
            } else {
                high.insert(val);
                sumHigh += val;
            }
            rebalance();
        }
        auto computeCost = [&]() -> long long {
            int median = *low.rbegin();
            long long szLow = (long long)low.size();
            long long szHigh = (long long)high.size();
            return (long long)median * szLow - sumLow + sumHigh - (long long)median * szHigh;
        };
        cost[0] = computeCost();
        
        // slide windows
        for (int i = x; i < n; ++i) {
            int outVal = nums[i - x];
            if (low.find(outVal) != low.end()) {
                low.erase(low.find(outVal));
                sumLow -= outVal;
            } else {
                high.erase(high.find(outVal));
                sumHigh -= outVal;
            }
            
            int inVal = nums[i];
            if (!low.empty() && inVal <= *low.rbegin()) {
                low.insert(inVal);
                sumLow += inVal;
            } else {
                high.insert(inVal);
                sumHigh += inVal;
            }
            rebalance();
            cost[i - x + 1] = computeCost();
        }
        
        const long long INF = (1LL << 60);
        vector<vector<long long>> dp(m + 1, vector<long long>(k + 1, INF));
        dp[0][0] = 0;
        for (int t = 1; t <= m; ++t) {
            // not taking window starting at t-1
            for (int j = 0; j <= k; ++j) dp[t][j] = dp[t - 1][j];
            int s = t - 1;
            for (int j = 1; j <= k; ++j) {
                int prevIdx = max(0, t - x);
                if (dp[prevIdx][j - 1] != INF) {
                    long long cand = dp[prevIdx][j - 1] + cost[s];
                    if (cand < dp[t][j]) dp[t][j] = cand;
                }
            }
        }
        return dp[m][k];
    }
};
```

## Java

```java
class Solution {
    public long minOperations(int[] nums, int x, int k) {
        int n = nums.length;
        int m = n - x + 1; // number of possible windows
        long[] cost = new long[m];
        DualHeap dh = new DualHeap();
        for (int i = 0; i < x; ++i) dh.add(nums[i]);
        cost[0] = dh.getCost();
        for (int start = 1; start < m; ++start) {
            dh.remove(nums[start - 1]);
            dh.add(nums[start + x - 1]);
            cost[start] = dh.getCost();
        }

        long INF = Long.MAX_VALUE / 4;
        long[][] dp = new long[k + 1][n + 1];
        for (int t = 0; t <= k; ++t) {
            java.util.Arrays.fill(dp[t], INF);
        }
        // zero windows cost zero
        for (int i = 0; i <= n; ++i) dp[0][i] = 0;

        for (int t = 1; t <= k; ++t) {
            for (int pos = 1; pos <= n; ++pos) {
                // not take a window ending at pos
                dp[t][pos] = dp[t][pos - 1];
                if (pos >= x) {
                    int startIdx = pos - x; // start index of the window in nums, also cost index
                    long cand = dp[t - 1][pos - x] + cost[startIdx];
                    if (cand < dp[t][pos]) dp[t][pos] = cand;
                }
            }
        }
        return dp[k][n];
    }

    private static class DualHeap {
        private final java.util.TreeMap<Integer, Integer> low;   // max-heap behavior
        private final java.util.TreeMap<Integer, Integer> high;  // min-heap behavior
        private int sizeLow = 0, sizeHigh = 0;
        private long sumLow = 0, sumHigh = 0;

        DualHeap() {
            low = new java.util.TreeMap<>(java.util.Collections.reverseOrder());
            high = new java.util.TreeMap<>();
        }

        void add(int num) {
            if (sizeLow == 0 || num <= low.firstKey()) {
                insert(low, num);
                sizeLow++;
                sumLow += num;
            } else {
                insert(high, num);
                sizeHigh++;
                sumHigh += num;
            }
            balance();
        }

        void remove(int num) {
            if (low.containsKey(num)) {
                delete(low, num);
                sizeLow--;
                sumLow -= num;
            } else {
                delete(high, num);
                sizeHigh--;
                sumHigh -= num;
            }
            balance();
        }

        long getCost() {
            int median = low.firstKey(); // current median (lower median for even length)
            long left = (long) median * sizeLow - sumLow;
            long right = sumHigh - (long) median * sizeHigh;
            return left + right;
        }

        private void insert(java.util.TreeMap<Integer, Integer> map, int val) {
            map.put(val, map.getOrDefault(val, 0) + 1);
        }

        private void delete(java.util.TreeMap<Integer, Integer> map, int val) {
            int cnt = map.get(val);
            if (cnt == 1) map.remove(val);
            else map.put(val, cnt - 1);
        }

        private void balance() {
            // Ensure sizeLow >= sizeHigh and difference at most 1
            while (sizeLow > sizeHigh + 1) {
                int key = low.firstKey();
                delete(low, key);
                sizeLow--;
                sumLow -= key;
                insert(high, key);
                sizeHigh++;
                sumHigh += key;
            }
            while (sizeLow < sizeHigh) {
                int key = high.firstKey();
                delete(high, key);
                sizeHigh--;
                sumHigh -= key;
                insert(low, key);
                sizeLow++;
                sumLow += key;
            }
        }
    }
}
```

## Python

```python
class Solution(object):
    def minOperations(self, nums, x, k):
        """
        :type nums: List[int]
        :type x: int
        :type k: int
        :rtype: int
        """
        import heapq

        n = len(nums)
        m = n - x + 1  # number of possible windows

        # ---------- sliding window median with cost ----------
        low = []   # max-heap (store negative)
        high = []  # min-heap
        del_low = {}
        del_high = {}
        len_low = len_high = 0
        sum_low = sum_high = 0

        def prune(heap):
            if heap is low:
                while heap and del_low.get(-heap[0], 0):
                    val = -heapq.heappop(low)
                    cnt = del_low[val]
                    if cnt == 1:
                        del del_low[val]
                    else:
                        del_low[val] = cnt - 1
            else:  # high
                while heap and del_high.get(heap[0], 0):
                    val = heapq.heappop(high)
                    cnt = del_high[val]
                    if cnt == 1:
                        del del_high[val]
                    else:
                        del_high[val] = cnt - 1

        def rebalance():
            nonlocal len_low, len_high, sum_low, sum_high
            # ensure len_low >= len_high and difference <= 1
            if len_low > len_high + 1:
                prune(low)
                val = -heapq.heappop(low)
                sum_low -= val
                len_low -= 1
                heapq.heappush(high, val)
                sum_high += val
                len_high += 1
            elif len_low < len_high:
                prune(high)
                val = heapq.heappop(high)
                sum_high -= val
                len_high -= 1
                heapq.heappush(low, -val)
                sum_low += val
                len_low += 1

        def add(num):
            nonlocal len_low, len_high, sum_low, sum_high
            if not low or num <= -low[0]:
                heapq.heappush(low, -num)
                sum_low += num
                len_low += 1
            else:
                heapq.heappush(high, num)
                sum_high += num
                len_high += 1
            rebalance()

        def remove(num):
            nonlocal len_low, len_high, sum_low, sum_high
            if low and num <= -low[0]:
                del_low[num] = del_low.get(num, 0) + 1
                sum_low -= num
                len_low -= 1
                if low and -low[0] == num:
                    prune(low)
            else:
                del_high[num] = del_high.get(num, 0) + 1
                sum_high -= num
                len_high -= 1
                if high and high[0] == num:
                    prune(high)
            rebalance()

        costs = [0] * m
        # initial window
        for i in range(x):
            add(nums[i])
        median = -low[0]
        costs[0] = median * len_low - sum_low + sum_high - median * len_high

        for start in range(1, m):
            remove(nums[start - 1])
            add(nums[start + x - 1])
            median = -low[0]
            costs[start] = median * len_low - sum_low + sum_high - median * len_high

        # ---------- DP to pick k non‑overlapping windows ----------
        INF = 10 ** 18
        dp = [[INF] * (k + 1) for _ in range(m + 1)]
        dp[0][0] = 0

        for i in range(1, m + 1):
            # not taking window starting at i-1
            prev = dp[i - 1]
            cur = dp[i]
            for j in range(k + 1):
                cur[j] = prev[j]

            if i >= x:
                base = dp[i - x]
                cost_i = costs[i - 1]
                for j in range(1, k + 1):
                    val = base[j - 1] + cost_i
                    if val < cur[j]:
                        cur[j] = val

        return dp[m][k]
```

## Python3

```python
import heapq
from typing import List

class DualHeap:
    def __init__(self, k: int):
        self.k = k
        self.small = []          # max-heap (store negatives)
        self.large = []          # min-heap
        self.delayed = {}
        self.smallSize = 0
        self.largeSize = 0
        self.sumSmall = 0
        self.sumLarge = 0

    def _prune(self, heap):
        while heap:
            num = -heap[0] if heap is self.small else heap[0]
            if self.delayed.get(num, 0):
                self.delayed[num] -= 1
                if self.delayed[num] == 0:
                    del self.delayed[num]
                heapq.heappop(heap)
            else:
                break

    def _makeBalance(self):
        # target size for small (lower half) is (k+1)//2
        target = (self.k + 1) // 2
        if self.smallSize > target:
            val = -heapq.heappop(self.small)
            self.sumSmall -= val
            self.smallSize -= 1
            heapq.heappush(self.large, val)
            self.sumLarge += val
            self.largeSize += 1
        elif self.smallSize < target:
            if self.large:
                val = heapq.heappop(self.large)
                self.sumLarge -= val
                self.largeSize -= 1
                heapq.heappush(self.small, -val)
                self.sumSmall += val
                self.smallSize += 1

        self._prune(self.small)
        self._prune(self.large)

    def insert(self, num: int):
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.sumSmall += num
            self.smallSize += 1
        else:
            heapq.heappush(self.large, num)
            self.sumLarge += num
            self.largeSize += 1
        self._makeBalance()

    def erase(self, num: int):
        self.delayed[num] = self.delayed.get(num, 0) + 1
        if num <= -self.small[0]:
            self.sumSmall -= num
            self.smallSize -= 1
            if num == -self.small[0]:
                self._prune(self.small)
        else:
            self.sumLarge -= num
            self.largeSize -= 1
            if self.large and num == self.large[0]:
                self._prune(self.large)
        self._makeBalance()

    def median(self) -> int:
        return -self.small[0]

    def cost(self) -> int:
        m = self.median()
        left = m * self.smallSize - self.sumSmall
        right = self.sumLarge - m * self.largeSize
        return left + right


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        m = n - x + 1                     # number of possible windows
        costs = [0] * m

        dh = DualHeap(x)
        for i in range(x):
            dh.insert(nums[i])
        costs[0] = dh.cost()

        for start in range(1, m):
            dh.erase(nums[start - 1])
            dh.insert(nums[start + x - 1])
            costs[start] = dh.cost()

        INF = 10 ** 18
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            # inherit previous state (skip position i-1)
            for j in range(k + 1):
                dp[i][j] = dp[i - 1][j]

            if i >= x:
                w_start = i - x
                c = costs[w_start]
                for j in range(1, k + 1):
                    prev = dp[w_start][j - 1] + c
                    if prev < dp[i][j]:
                        dp[i][j] = prev

        return dp[n][k]
```

## C

```c
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define OFFSET 1000001               // value -1e6 maps to index 1
#define MAXV   2000005              // enough for values up to 1e6 + offset

static int bitCnt[MAXV];
static long long bitSum[MAXV];

static void bitAdd(int idx, int delta) {
    int v = idx - OFFSET;               // original value
    while (idx < MAXV) {
        bitCnt[idx] += delta;
        bitSum[idx] += (long long)v * delta;
        idx += idx & -idx;
    }
}

static int queryCnt(int idx) {
    int res = 0;
    while (idx > 0) {
        res += bitCnt[idx];
        idx -= idx & -idx;
    }
    return res;
}

static long long querySum(int idx) {
    long long res = 0;
    while (idx > 0) {
        res += bitSum[idx];
        idx -= idx & -idx;
    }
    return res;
}

/* find smallest index such that prefix count >= k (k is 1‑based) */
static int findKth(int k) {
    int idx = 0;
    int mask = 1;
    while (mask < MAXV) mask <<= 1;
    for (mask >>= 1; mask; mask >>= 1) {
        int next = idx + mask;
        if (next < MAXV && bitCnt[next] < k) {
            idx = next;
            k -= bitCnt[next];
        }
    }
    return idx + 1;
}

long long minOperations(int* nums, int numsSize, int x, int k) {
    int n = numsSize;
    int m = n - x + 1;                     // number of possible windows
    long long *cost = (long long *)malloc(sizeof(long long) * m);
    
    /* sliding window to compute cost for each start */
    long long sumWindow = 0;
    for (int i = 0; i < n; ++i) {
        int idxAdd = nums[i] + OFFSET;
        bitAdd(idxAdd, 1);
        sumWindow += nums[i];
        
        if (i >= x) {
            int idxRem = nums[i - x] + OFFSET;
            bitAdd(idxRem, -1);
            sumWindow -= nums[i - x];
        }
        if (i >= x - 1) {
            int start = i - x + 1;
            int medianPos = (x + 1) / 2;               // lower median
            int medIdx = findKth(medianPos);
            int medianVal = medIdx - OFFSET;
            
            int cntLow = queryCnt(medIdx);
            long long sumLow = querySum(medIdx);
            
            long long leftCost = (long long)medianVal * cntLow - sumLow;
            long long rightCost = (sumWindow - sumLow) -
                                  (long long)medianVal * (x - cntLow);
            cost[start] = leftCost + rightCost;
        }
    }
    
    /* DP: dp[t][i] = min cost using t windows among first i possible starts */
    const long long INF = LLONG_MAX / 4;
    int rows = k + 1;
    int cols = m + 1;
    long long *dp = (long long *)malloc(sizeof(long long) * rows * cols);
    
    #define DP(t,i) dp[(t)*(cols)+(i)]
    
    for (int i = 0; i <= m; ++i) DP(0,i) = 0;
    for (int t = 1; t <= k; ++t) DP(t,0) = INF;
    
    for (int t = 1; t <= k; ++t) {
        for (int i = 1; i <= m; ++i) {
            long long best = DP(t,i-1);               // skip current start
            int s = i - 1;                            // window starting at s
            int prevIdx = (s >= x) ? (s - x + 1) : 0;
            if (DP(t-1,prevIdx) != INF) {
                long long cand = DP(t-1,prevIdx) + cost[s];
                if (cand < best) best = cand;
            }
            DP(t,i) = best;
        }
    }
    
    long long answer = DP(k,m);
    free(cost);
    free(dp);
    return answer;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public long MinOperations(int[] nums, int x, int k) {
        int n = nums.Length;
        int m = n - x + 1;
        long[] cost = new long[m];

        // Heaps for sliding window median
        var maxHeap = new PriorityQueue<int, int>(Comparer<int>.Create((a, b) => b.CompareTo(a))); // max-heap
        var minHeap = new PriorityQueue<int, int>(); // min-heap

        var delayedLow = new Dictionary<int, int>();
        var delayedHigh = new Dictionary<int, int>();

        long sumLow = 0, sumHigh = 0;
        int sizeLow = 0, sizeHigh = 0;

        void CleanTop(PriorityQueue<int, int> heap, Dictionary<int, int> del) {
            while (heap.Count > 0) {
                heap.TryPeek(out int top, out _);
                if (del.TryGetValue(top, out int cnt)) {
                    heap.Dequeue();
                    if (cnt == 1) del.Remove(top);
                    else del[top] = cnt - 1;
                } else break;
            }
        }

        void Balance() {
            // Ensure sizeLow >= sizeHigh and sizeLow - sizeHigh <= 1
            while (sizeLow > sizeHigh + 1) {
                CleanTop(maxHeap, delayedLow);
                maxHeap.TryPeek(out int move, out _);
                maxHeap.Dequeue();
                sumLow -= move;
                sizeLow--;

                minHeap.Enqueue(move, move);
                sumHigh += move;
                sizeHigh++;
            }
            while (sizeLow < sizeHigh) {
                CleanTop(minHeap, delayedHigh);
                minHeap.TryPeek(out int move, out _);
                minHeap.Dequeue();
                sumHigh -= move;
                sizeHigh--;

                maxHeap.Enqueue(move, move);
                sumLow += move;
                sizeLow++;
            }
        }

        void Add(int num) {
            if (maxHeap.Count == 0) {
                maxHeap.Enqueue(num, num);
                sumLow += num;
                sizeLow++;
            } else {
                CleanTop(maxHeap, delayedLow);
                maxHeap.TryPeek(out int median, out _);
                if (num <= median) {
                    maxHeap.Enqueue(num, num);
                    sumLow += num;
                    sizeLow++;
                } else {
                    minHeap.Enqueue(num, num);
                    sumHigh += num;
                    sizeHigh++;
                }
            }
            Balance();
        }

        void Remove(int num) {
            // Determine which heap the number belongs to using current median
            CleanTop(maxHeap, delayedLow);
            int median = maxHeap.Count > 0 ? (maxHeap.TryPeek(out int med, out _) ? med : 0) : 0;
            if (num <= median) {
                if (delayedLow.ContainsKey(num)) delayedLow[num]++; else delayedLow[num] = 1;
                sumLow -= num;
                sizeLow--;
            } else {
                if (delayedHigh.ContainsKey(num)) delayedHigh[num]++; else delayedHigh[num] = 1;
                sumHigh -= num;
                sizeHigh--;
            }
            CleanTop(maxHeap, delayedLow);
            CleanTop(minHeap, delayedHigh);
            Balance();
        }

        // Compute cost for each window
        for (int i = 0; i < n; ++i) {
            Add(nums[i]);
            if (i >= x) Remove(nums[i - x]);
            if (i >= x - 1) {
                CleanTop(maxHeap, delayedLow);
                int median = maxHeap.TryPeek(out int med, out _) ? med : 0;
                long c = (long)median * sizeLow - sumLow + sumHigh - (long)median * sizeHigh;
                cost[i - x + 1] = c;
            }
        }

        const long INF = long.MaxValue / 4;
        long[,] dp = new long[n + 1, k + 1];
        for (int i = 0; i <= n; ++i)
            for (int j = 0; j <= k; ++j)
                dp[i, j] = INF;
        dp[0, 0] = 0;

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j <= k; ++j) {
                long cur = dp[i, j];
                if (cur == INF) continue;

                // Skip current element
                if (dp[i + 1, j] > cur) dp[i + 1, j] = cur;

                // Take window starting at i
                if (j < k && i <= n - x) {
                    long nd = cur + cost[i];
                    int end = i + x;
                    if (dp[end, j + 1] > nd) dp[end, j + 1] = nd;
                }
            }
        }

        long ans = INF;
        for (int i = 0; i <= n; ++i)
            if (dp[i, k] < ans) ans = dp[i, k];

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} x
 * @param {number} k
 * @return {number}
 */
var minOperations = function(nums, x, k) {
    const n = nums.length;
    const m = n - x + 1; // number of windows
    const costs = new Array(m);
    
    // Heap implementation
    class Heap {
        constructor(compare) {
            this.data = [];
            this.compare = compare; // returns true if a should be before b
        }
        size() { return this.data.length; }
        peek() { return this.data[0]; }
        push(val) {
            const arr = this.data;
            arr.push(val);
            let i = arr.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (this.compare(arr[p], arr[i])) break;
                [arr[p], arr[i]] = [arr[i], arr[p]];
                i = p;
            }
        }
        pop() {
            const arr = this.data;
            if (arr.length === 0) return undefined;
            const top = arr[0];
            const last = arr.pop();
            if (arr.length > 0) {
                arr[0] = last;
                let i = 0;
                while (true) {
                    let l = i * 2 + 1, r = l + 1, best = i;
                    if (l < arr.length && !this.compare(arr[best], arr[l])) best = l;
                    if (r < arr.length && !this.compare(arr[best], arr[r])) best = r;
                    if (best === i) break;
                    [arr[i], arr[best]] = [arr[best], arr[i]];
                    i = best;
                }
            }
            return top;
        }
    }

    const low = new Heap((a, b) => a > b);   // max-heap
    const high = new Heap((a, b) => a < b);  // min-heap
    const delLow = new Map();
    const delHigh = new Map();

    let sizeLow = 0, sizeHigh = 0;
    let sumLow = 0, sumHigh = 0;

    function prune(heap, delMap) {
        while (heap.size() > 0) {
            const val = heap.peek();
            const cnt = delMap.get(val);
            if (cnt != null && cnt > 0) {
                heap.pop();
                if (cnt === 1) delMap.delete(val);
                else delMap.set(val, cnt - 1);
            } else break;
        }
    }

    function rebalance() {
        // ensure sizeLow >= sizeHigh and difference <= 1
        if (sizeLow > sizeHigh + 1) {
            prune(low, delLow);
            const val = low.pop();
            sumLow -= val;
            sizeLow--;
            high.push(val);
            sumHigh += val;
            sizeHigh++;
        } else if (sizeLow < sizeHigh) {
            prune(high, delHigh);
            const val = high.pop();
            sumHigh -= val;
            sizeHigh--;
            low.push(val);
            sumLow += val;
            sizeLow++;
        }
    }

    function add(num) {
        if (sizeLow === 0 || num <= low.peek()) {
            low.push(num);
            sumLow += num;
            sizeLow++;
        } else {
            high.push(num);
            sumHigh += num;
            sizeHigh++;
        }
        rebalance();
    }

    function remove(num) {
        prune(low, delLow);
        prune(high, delHigh);
        const median = low.peek(); // after pruning
        if (num <= median) {
            sumLow -= num;
            sizeLow--;
            delLow.set(num, (delLow.get(num) || 0) + 1);
        } else {
            sumHigh -= num;
            sizeHigh--;
            delHigh.set(num, (delHigh.get(num) || 0) + 1);
        }
        prune(low, delLow);
        prune(high, delHigh);
        rebalance();
    }

    // sliding window to compute costs
    for (let i = 0; i < n; ++i) {
        add(nums[i]);
        if (i >= x) remove(nums[i - x]);
        if (i >= x - 1) {
            prune(low, delLow);
            const median = low.peek();
            const cost = median * sizeLow - sumLow + sumHigh - median * sizeHigh;
            costs[i - x + 1] = cost;
        }
    }

    // DP: dp[pos][cnt]
    const INF = Number.MAX_SAFE_INTEGER;
    const dp = Array.from({ length: n + 1 }, () => new Array(k + 1).fill(INF));
    dp[0][0] = 0;

    for (let i = 1; i <= n; ++i) {
        // skip current position
        for (let cnt = 0; cnt <= k; ++cnt) {
            dp[i][cnt] = dp[i - 1][cnt];
        }
        if (i >= x) {
            const cost = costs[i - x];
            for (let cnt = 1; cnt <= k; ++cnt) {
                const prev = dp[i - x][cnt - 1];
                if (prev !== INF) {
                    const val = prev + cost;
                    if (val < dp[i][cnt]) dp[i][cnt] = val;
                }
            }
        }
    }

    return dp[n][k];
};
```

## Typescript

```typescript
function minOperations(nums: number[], x: number, k: number): number {
    const n = nums.length;
    const m = n - x + 1;

    // coordinate compression
    const uniq = Array.from(new Set(nums)).sort((a, b) => a - b);
    const idMap = new Map<number, number>();
    for (let i = 0; i < uniq.length; i++) idMap.set(uniq[i], i);
    const sz = uniq.length;

    class BIT {
        n: number;
        tree: number[];
        constructor(n: number) {
            this.n = n;
            this.tree = new Array(n + 2).fill(0);
        }
        add(i: number, delta: number): void {
            for (let x = i + 1; x <= this.n; x += x & -x) this.tree[x] += delta;
        }
        sumPrefix(i: number): number { // [0,i)
            let res = 0;
            for (let x = i; x > 0; x -= x & -x) res += this.tree[x];
            return res;
        }
        query(i: number): number { // up to i inclusive, 0‑based
            return this.sumPrefix(i + 1);
        }
        kth(k: number): number { // smallest idx with prefix sum >= k (k>=1)
            let idx = 0;
            let bit = 1;
            while ((bit << 1) <= this.n) bit <<= 1;
            for (let d = bit; d > 0; d >>= 1) {
                const nxt = idx + d;
                if (nxt <= this.n && this.tree[nxt] < k) {
                    idx = nxt;
                    k -= this.tree[nxt];
                }
            }
            return idx; // 0‑based
        }
    }

    const cntBIT = new BIT(sz);
    const sumBIT = new BIT(sz);
    let totalSum = 0;

    for (let i = 0; i < x; i++) {
        const v = nums[i];
        const id = idMap.get(v)!;
        cntBIT.add(id, 1);
        sumBIT.add(id, v);
        totalSum += v;
    }

    const cost: number[] = new Array(m);
    for (let start = 0; start < m; start++) {
        const target = (x + 1) >> 1; // ceil(x/2)
        const medIdx = cntBIT.kth(target);
        const medVal = uniq[medIdx];
        const cntLeft = cntBIT.query(medIdx);
        const sumLeft = sumBIT.query(medIdx);
        const cntRight = x - cntLeft;
        const sumRight = totalSum - sumLeft;
        cost[start] =
            medVal * cntLeft - sumLeft + sumRight - medVal * cntRight;

        if (start + x < n) {
            const outV = nums[start];
            const outId = idMap.get(outV)!;
            cntBIT.add(outId, -1);
            sumBIT.add(outId, -outV);
            totalSum -= outV;

            const inV = nums[start + x];
            const inId = idMap.get(inV)!;
            cntBIT.add(inId, 1);
            sumBIT.add(inId, inV);
            totalSum += inV;
        }
    }

    const INF = Number.MAX_SAFE_INTEGER;
    const dp: number[][] = Array.from({ length: n + 1 }, () => new Array(k + 1).fill(INF));
    for (let c = 0; c <= k; c++) dp[n][c] = c === 0 ? 0 : INF;

    for (let i = n - 1; i >= 0; i--) {
        for (let c = 0; c <= k; c++) {
            let best = dp[i + 1][c];
            if (i + x <= n && c + 1 <= k) {
                const cand = cost[i] + dp[i + x][c + 1];
                if (cand < best) best = cand;
            }
            dp[i][c] = best;
        }
    }

    return dp[0][k];
}
```

## Php

```php
class DualHeap {
    private $small; // max heap
    private $large; // min heap
    private $delSmall = [];
    private $delLarge = [];
    public $smallSize = 0;
    public $largeSize = 0;
    public $smallSum = 0;
    public $largeSum = 0;

    public function __construct() {
        $this->small = new SplMaxHeap();
        $this->large = new SplMinHeap();
    }

    private function prune(&$heap, &$delMap) {
        while (!$heap->isEmpty()) {
            $top = $heap->current();
            if (isset($delMap[$top]) && $delMap[$top] > 0) {
                $heap->extract();
                $delMap[$top]--;
                if ($delMap[$top] == 0) {
                    unset($delMap[$top]);
                }
            } else {
                break;
            }
        }
    }

    private function makeBalance() {
        // ensure smallSize >= largeSize and difference <=1
        if ($this->smallSize > $this->largeSize + 1) {
            $value = $this->small->extract();
            $this->smallSum -= $value;
            $this->smallSize--;
            $this->large->insert($value);
            $this->largeSum += $value;
            $this->largeSize++;
            $this->prune($this->small, $this->delSmall);
        } elseif ($this->smallSize < $this->largeSize) {
            $value = $this->large->extract();
            $this->largeSum -= $value;
            $this->largeSize--;
            $this->small->insert($value);
            $this->smallSum += $value;
            $this->smallSize++;
            $this->prune($this->large, $this->delLarge);
        }
    }

    public function insert($num) {
        if ($this->small->isEmpty() || $num <= $this->small->current()) {
            $this->small->insert($num);
            $this->smallSum += $num;
            $this->smallSize++;
        } else {
            $this->large->insert($num);
            $this->largeSum += $num;
            $this->largeSize++;
        }
        $this->makeBalance();
    }

    public function erase($num) {
        if (!$this->small->isEmpty() && $num <= $this->small->current()) {
            $this->delSmall[$num] = ($this->delSmall[$num] ?? 0) + 1;
            $this->smallSum -= $num;
            $this->smallSize--;
        } else {
            $this->delLarge[$num] = ($this->delLarge[$num] ?? 0) + 1;
            $this->largeSum -= $num;
            $this->largeSize--;
        }
        $this->prune($this->small, $this->delSmall);
        $this->prune($this->large, $this->delLarge);
        $this->makeBalance();
    }

    public function getMedian() {
        return $this->small->current();
    }

    public function getCost() {
        $median = $this->getMedian();
        $cost = $median * $this->smallSize - $this->smallSum + $this->largeSum - $median * $this->largeSize;
        return $cost;
    }
}

class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $x
     * @param Integer $k
     * @return Integer
     */
    function minOperations($nums, $x, $k) {
        $n = count($nums);
        $m = $n - $x + 1; // number of possible windows
        $costs = array_fill(0, $m, 0);

        $dh = new DualHeap();
        for ($i = 0; $i < $x; $i++) {
            $dh->insert($nums[$i]);
        }
        $costs[0] = $dh->getCost();

        for ($i = $x; $i < $n; $i++) {
            $dh->insert($nums[$i]);
            $dh->erase($nums[$i - $x]);
            $start = $i - $x + 1;
            $costs[$start] = $dh->getCost();
        }

        $INF = 10**18;
        $dpPrev = array_fill(0, $m, $INF);

        for ($t = 1; $t <= $k; $t++) {
            $dpCurr = array_fill(0, $m, $INF);
            for ($s = 0; $s < $m; $s++) {
                // not take this window
                if ($s > 0 && $dpCurr[$s - 1] < $dpCurr[$s]) {
                    $dpCurr[$s] = $dpCurr[$s - 1];
                }
                // take this window
                if ($t == 1) {
                    $candidate = $costs[$s];
                } else {
                    $prevIdx = $s - $x;
                    if ($prevIdx >= 0 && $dpPrev[$prevIdx] < $INF) {
                        $candidate = $dpPrev[$prevIdx] + $costs[$s];
                    } else {
                        $candidate = $INF;
                    }
                }
                if ($candidate < $dpCurr[$s]) {
                    $dpCurr[$s] = $candidate;
                }
            }
            $dpPrev = $dpCurr;
        }

        return (int)$dpPrev[$m - 1];
    }
}
```

## Swift

```swift
class Solution {
    func minOperations(_ nums: [Int], _ x: Int, _ k: Int) -> Int {
        let n = nums.count
        let m = n - x + 1
        var costs = [Int64](repeating: 0, count: m)
        
        // Heap implementation
        final class Heap {
            var elements: [Int] = []
            let priorityFunction: (Int, Int) -> Bool   // true if a has higher priority than b
            
            init(_ priorityFunction: @escaping (Int, Int) -> Bool) {
                self.priorityFunction = priorityFunction
            }
            
            var isEmpty: Bool { elements.isEmpty }
            func peek() -> Int? { elements.first }
            
            func push(_ value: Int) {
                elements.append(value)
                siftUp(from: elements.count - 1)
            }
            
            func pop() -> Int? {
                guard !elements.isEmpty else { return nil }
                if elements.count == 1 {
                    return elements.removeLast()
                } else {
                    let value = elements[0]
                    elements[0] = elements.removeLast()
                    siftDown(from: 0)
                    return value
                }
            }
            
            private func parentIndex(of index: Int) -> Int { (index - 1) / 2 }
            private func leftChildIndex(of index: Int) -> Int { 2 * index + 1 }
            private func rightChildIndex(of index: Int) -> Int { 2 * index + 2 }
            
            private func siftUp(from index: Int) {
                var child = index
                var parent = parentIndex(of: child)
                while child > 0 && priorityFunction(elements[child], elements[parent]) {
                    elements.swapAt(child, parent)
                    child = parent
                    parent = parentIndex(of: child)
                }
            }
            
            private func siftDown(from index: Int) {
                var parent = index
                while true {
                    let left = leftChildIndex(of: parent)
                    let right = rightChildIndex(of: parent)
                    var candidate = parent
                    if left < elements.count && priorityFunction(elements[left], elements[candidate]) {
                        candidate = left
                    }
                    if right < elements.count && priorityFunction(elements[right], elements[candidate]) {
                        candidate = right
                    }
                    if candidate == parent { return }
                    elements.swapAt(parent, candidate)
                    parent = candidate
                }
            }
        }
        
        // Sliding window median with lazy deletions
        let low = Heap({ $0 > $1 })   // max-heap for lower half
        let high = Heap({ $0 < $1 })  // min-heap for upper half
        var delayed: [Int:Int] = [:]
        var sumLow: Int64 = 0
        var sumHigh: Int64 = 0
        var sizeLow = 0
        var sizeHigh = 0
        
        func prune(_ heap: Heap) {
            while let top = heap.peek(), let cnt = delayed[top], cnt > 0 {
                _ = heap.pop()
                if cnt == 1 {
                    delayed.removeValue(forKey: top)
                } else {
                    delayed[top] = cnt - 1
                }
            }
        }
        
        func balance() {
            // Ensure sizeLow >= sizeHigh and difference <= 1
            if sizeLow > sizeHigh + 1 {
                if let val = low.pop() {
                    sumLow -= Int64(val)
                    sizeLow -= 1
                    high.push(val)
                    sumHigh += Int64(val)
                    sizeHigh += 1
                }
            } else if sizeLow < sizeHigh {
                if let val = high.pop() {
                    sumHigh -= Int64(val)
                    sizeHigh -= 1
                    low.push(val)
                    sumLow += Int64(val)
                    sizeLow += 1
                }
            }
        }
        
        for i in 0..<n {
            let num = nums[i]
            if let median = low.peek(), num <= median {
                low.push(num)
                sumLow += Int64(num)
                sizeLow += 1
            } else {
                high.push(num)
                sumHigh += Int64(num)
                sizeHigh += 1
            }
            balance()
            prune(low)
            prune(high)
            
            if i >= x {
                let out = nums[i - x]
                // Determine current median for classification
                guard let curMedian = low.peek() else { continue }
                if out <= curMedian {
                    sizeLow -= 1
                    sumLow -= Int64(out)
                } else {
                    sizeHigh -= 1
                    sumHigh -= Int64(out)
                }
                delayed[out, default: 0] += 1
                prune(low)
                prune(high)
                balance()
            }
            
            if i >= x - 1 {
                let start = i - x + 1
                guard let median = low.peek() else { continue }
                let leftSize = Int64(sizeLow)
                let rightSize = Int64(sizeHigh)
                let medVal = Int64(median)
                let cost = medVal * leftSize - sumLow + sumHigh - medVal * rightSize
                costs[start] = cost
            }
        }
        
        // DP over prefix length
        let INF: Int64 = 9_000_000_000_000_000_000
        var dp = [[Int64]](repeating: [Int64](repeating: INF, count: k + 1), count: n + 1)
        dp[0][0] = 0
        
        for i in 1...n {
            for j in 0...k {
                // Skip current position
                var best = dp[i - 1][j]
                if i >= x && j > 0 {
                    let cand = dp[i - x][j - 1] + costs[i - x]
                    if cand < best { best = cand }
                }
                dp[i][j] = best
            }
        }
        
        return Int(dp[n][k])
    }
}
```

## Kotlin

```kotlin
import java.util.PriorityQueue
import java.util.HashMap

class Solution {
    fun minOperations(nums: IntArray, x: Int, k: Int): Long {
        val n = nums.size
        val m = n - x + 1
        if (m <= 0) return 0L
        val cost = LongArray(m)

        // DualHeap to maintain median and sums
        class DualHeap(val windowSize: Int) {
            private val small = PriorityQueue<Int>(compareByDescending { it }) // max-heap
            private val large = PriorityQueue<Int>() // min-heap
            private val delayed = HashMap<Int, Int>()
            var smallSize = 0
            var largeSize = 0
            var sumSmall: Long = 0L
            var sumLarge: Long = 0L

            private fun prune(heap: PriorityQueue<Int>) {
                while (heap.isNotEmpty()) {
                    val num = heap.peek()
                    val cnt = delayed[num]
                    if (cnt != null && cnt > 0) {
                        if (cnt == 1) delayed.remove(num) else delayed[num] = cnt - 1
                        heap.poll()
                    } else break
                }
            }

            private fun makeBalance() {
                // target size for small: (windowSize + 1) / 2
                val targetSmall = (windowSize + 1) / 2
                if (smallSize > targetSmall) {
                    // move from small to large
                    prune(small)
                    val num = small.poll()
                    sumSmall -= num.toLong()
                    smallSize--
                    large.offer(num)
                    sumLarge += num.toLong()
                    largeSize++
                } else if (smallSize < targetSmall) {
                    prune(large)
                    val num = large.poll()
                    sumLarge -= num.toLong()
                    largeSize--
                    small.offer(num)
                    sumSmall += num.toLong()
                    smallSize++
                }
            }

            fun add(num: Int) {
                if (small.isEmpty() || num <= small.peek()) {
                    small.offer(num)
                    sumSmall += num.toLong()
                    smallSize++
                } else {
                    large.offer(num)
                    sumLarge += num.toLong()
                    largeSize++
                }
                makeBalance()
            }

            fun remove(num: Int) {
                delayed[num] = (delayed.getOrDefault(num, 0) + 1)
                if (!small.isEmpty() && num <= small.peek()) {
                    smallSize--
                    sumSmall -= num.toLong()
                } else {
                    largeSize--
                    sumLarge -= num.toLong()
                }
                prune(small)
                prune(large)
                makeBalance()
            }

            fun median(): Int = small.peek()

            fun cost(): Long {
                val med = median().toLong()
                val left = med * smallSize - sumSmall
                val right = sumLarge - med * largeSize
                return left + right
            }
        }

        val dh = DualHeap(x)
        for (i in 0 until x) dh.add(nums[i])
        cost[0] = dh.cost()
        for (start in 1 until m) {
            dh.remove(nums[start - 1])
            dh.add(nums[start + x - 1])
            cost[start] = dh.cost()
        }

        val INF = Long.MAX_VALUE / 4
        val dp = Array(k + 1) { LongArray(m + 1) { INF } }
        for (i in 0..m) dp[0][i] = 0L

        for (t in 1..k) {
            for (i in 1..m) {
                var best = dp[t][i - 1]
                val prevIdx = i - x
                if (prevIdx >= 0 && dp[t - 1][prevIdx] != INF) {
                    val cand = dp[t - 1][prevIdx] + cost[i - 1]
                    if (cand < best) best = cand
                }
                dp[t][i] = best
            }
        }

        return dp[k][m]
    }
}
```

## Dart

```dart
class Heap {
  List<int> _data;
  final bool _isMin;
  Heap(this._isMin) : _data = [];

  int get size => _data.length;

  void push(int val) {
    _data.add(val);
    _siftUp(_data.length - 1);
  }

  int peek() => _data[0];

  int pop() {
    int top = _data[0];
    int last = _data.removeLast();
    if (_data.isNotEmpty) {
      _data[0] = last;
      _siftDown(0);
    }
    return top;
  }

  void _siftUp(int idx) {
    while (idx > 0) {
      int parent = (idx - 1) >> 1;
      if (_compare(_data[idx], _data[parent])) {
        var tmp = _data[idx];
        _data[idx] = _data[parent];
        _data[parent] = tmp;
        idx = parent;
      } else {
        break;
      }
    }
  }

  void _siftDown(int idx) {
    int n = _data.length;
    while (true) {
      int left = idx * 2 + 1;
      int right = left + 1;
      int best = idx;
      if (left < n && _compare(_data[left], _data[best])) best = left;
      if (right < n && _compare(_data[right], _data[best])) best = right;
      if (best != idx) {
        var tmp = _data[idx];
        _data[idx] = _data[best];
        _data[best] = tmp;
        idx = best;
      } else {
        break;
      }
    }
  }

  bool _compare(int a, int b) => _isMin ? a < b : a > b;
}

class DualHeap {
  final int k;
  final Heap _small; // max-heap
  final Heap _large; // min-heap
  final Map<int, int> _delayed = {};
  int _smallSize = 0, _largeSize = 0;
  int _sumSmall = 0, _sumLarge = 0;

  DualHeap(this.k)
      : _small = Heap(false),
        _large = Heap(true);

  void _prune(Heap heap) {
    while (heap.size > 0) {
      int num = heap.peek();
      if (_delayed.containsKey(num)) {
        int cnt = _delayed[num]!;
        if (cnt == 1) {
          _delayed.remove(num);
        } else {
          _delayed[num] = cnt - 1;
        }
        heap.pop();
      } else {
        break;
      }
    }
  }

  void _makeBalance() {
    // ensure smallSize >= largeSize and diff <= 1
    if (_smallSize > _largeSize + 1) {
      int moved = _small.pop();
      _sumSmall -= moved;
      _smallSize--;
      _large.push(moved);
      _sumLarge += moved;
      _largeSize++;
      _prune(_small);
    } else if (_smallSize < _largeSize) {
      int moved = _large.pop();
      _sumLarge -= moved;
      _largeSize--;
      _small.push(moved);
      _sumSmall += moved;
      _smallSize++;
      _prune(_large);
    }
  }

  void insert(int num) {
    if (_small.size == 0 || num <= _small.peek()) {
      _small.push(num);
      _sumSmall += num;
      _smallSize++;
    } else {
      _large.push(num);
      _sumLarge += num;
      _largeSize++;
    }
    _makeBalance();
  }

  void erase(int num) {
    _delayed[num] = (_delayed[num] ?? 0) + 1;
    if (num <= _small.peek()) {
      _smallSize--;
      _sumSmall -= num;
      if (num == _small.peek()) _prune(_small);
    } else {
      _largeSize--;
      _sumLarge -= num;
      if (_large.size > 0 && num == _large.peek()) _prune(_large);
    }
    _makeBalance();
  }

  int getMedian() => _small.peek();

  int getCost() {
    int median = getMedian();
    int costLow = median * _smallSize - _sumSmall;
    int costHigh = _sumLarge - median * _largeSize;
    return costLow + costHigh;
  }
}

class Solution {
  int minOperations(List<int> nums, int x, int k) {
    int n = nums.length;
    int m = n - x + 1; // number of possible windows
    List<int> cost = List.filled(m, 0);
    DualHeap dh = DualHeap(x);
    for (int i = 0; i < x; ++i) dh.insert(nums[i]);
    cost[0] = dh.getCost();
    for (int start = 1; start < m; ++start) {
      dh.erase(nums[start - 1]);
      dh.insert(nums[start + x - 1]);
      cost[start] = dh.getCost();
    }

    const int INF = 1 << 60;
    List<List<int>> dp = List.generate(k + 1, (_) => List.filled(m + 1, INF));
    dp[0][0] = 0;

    for (int t = 0; t <= k; ++t) {
      for (int j = 0; j <= m; ++j) {
        int cur = dp[t][j];
        if (cur == INF) continue;
        // skip current window
        if (j < m && cur < dp[t][j + 1]) dp[t][j + 1] = cur;
        // take window starting at j
        if (t < k && j < m) {
          int nextIdx = j + x;
          if (nextIdx <= m) {
            int val = cur + cost[j];
            if (val < dp[t + 1][nextIdx]) dp[t + 1][nextIdx] = val;
          }
        }
      }
    }

    int ans = INF;
    for (int i = 0; i <= m; ++i) {
      if (dp[k][i] < ans) ans = dp[k][i];
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

type MaxHeap []int

func (h MaxHeap) Len() int           { return len(h) }
func (h MaxHeap) Less(i, j int) bool { return h[i] > h[j] } // max-heap
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
func (h MaxHeap) Top() int { return h[0] }

type MinHeap []int

func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i] < h[j] } // min-heap
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
func (h MinHeap) Top() int { return h[0] }

func pruneMax(h *MaxHeap, del map[int]int) {
	for h.Len() > 0 {
		v := (*h)[0]
		if cnt, ok := del[v]; ok && cnt > 0 {
			heap.Pop(h)
			if cnt == 1 {
				delete(del, v)
			} else {
				del[v] = cnt - 1
			}
		} else {
			break
		}
	}
}

func pruneMin(h *MinHeap, del map[int]int) {
	for h.Len() > 0 {
		v := (*h)[0]
		if cnt, ok := del[v]; ok && cnt > 0 {
			heap.Pop(h)
			if cnt == 1 {
				delete(del, v)
			} else {
				del[v] = cnt - 1
			}
		} else {
			break
		}
	}
}

func minOperations(nums []int, x int, k int) int64 {
	n := len(nums)
	if n == 0 || x == 0 || k == 0 {
		return 0
	}
	m := n - x + 1 // number of possible windows
	costs := make([]int64, m)

	var low MaxHeap
	var high MinHeap
	heap.Init(&low)
	heap.Init(&high)
	delLow := make(map[int]int)
	delHigh := make(map[int]int)

	var sumLow int64
	var sumHigh int64
	sizeLow := 0
	sizeHigh := 0

	add := func(val int) {
		if low.Len() == 0 || val <= low.Top() {
			heap.Push(&low, val)
			sumLow += int64(val)
			sizeLow++
		} else {
			heap.Push(&high, val)
			sumHigh += int64(val)
			sizeHigh++
		}
		// rebalance
		if sizeLow > sizeHigh+1 {
			pruneMax(&low, delLow)
			moved := heap.Pop(&low).(int)
			sumLow -= int64(moved)
			sizeLow--
			heap.Push(&high, moved)
			sumHigh += int64(moved)
			sizeHigh++
		} else if sizeLow < sizeHigh {
			pruneMin(&high, delHigh)
			moved := heap.Pop(&high).(int)
			sumHigh -= int64(moved)
			sizeHigh--
			heap.Push(&low, moved)
			sumLow += int64(moved)
			sizeLow++
		}
	}

	remove := func(val int) {
		pruneMax(&low, delLow)
		pruneMin(&high, delHigh)
		median := low.Top()
		if val <= median {
			delLow[val]++
			sumLow -= int64(val)
			sizeLow--
		} else {
			delHigh[val]++
			sumHigh -= int64(val)
			sizeHigh--
		}
		// clean tops
		pruneMax(&low, delLow)
		pruneMin(&high, delHigh)

		// rebalance after removal
		if sizeLow > sizeHigh+1 {
			pruneMax(&low, delLow)
			moved := heap.Pop(&low).(int)
			sumLow -= int64(moved)
			sizeLow--
			heap.Push(&high, moved)
			sumHigh += int64(moved)
			sizeHigh++
		} else if sizeLow < sizeHigh {
			pruneMin(&high, delHigh)
			moved := heap.Pop(&high).(int)
			sumHigh -= int64(moved)
			sizeHigh--
			heap.Push(&low, moved)
			sumLow += int64(moved)
			sizeLow++
		}
	}

	getCost := func() int64 {
		pruneMax(&low, delLow)
		median := low.Top()
		cost := int64(median)*int64(sizeLow) - sumLow + sumHigh - int64(median)*int64(sizeHigh)
		return cost
	}

	// initial window
	for i := 0; i < x; i++ {
		add(nums[i])
	}
	costs[0] = getCost()

	// slide windows
	for start := 1; start < m; start++ {
		remove(nums[start-1])
		add(nums[start+x-1])
		costs[start] = getCost()
	}

	const INF int64 = 1 << 60
	dpPrev := make([]int64, n+1)
	for i := range dpPrev {
		dpPrev[i] = 0 // zero windows cost zero
	}
	dpCurr := make([]int64, n+1)

	for t := 1; t <= k; t++ {
		for i := 0; i <= n; i++ {
			dpCurr[i] = INF
		}
		for i := 1; i <= n; i++ {
			// not taking a window ending at i
			if dpCurr[i-1] < dpCurr[i] {
				dpCurr[i] = dpCurr[i-1]
			}
			if i >= x {
				startIdx := i - x
				val := dpPrev[startIdx] + costs[startIdx]
				if val < dpCurr[i] {
					dpCurr[i] = val
				}
			}
		}
		// swap
		dpPrev, dpCurr = dpCurr, dpPrev
	}

	return dpPrev[n]
}
```

## Ruby

```ruby
def min_operations(nums, x, k)
  n = nums.length
  # coordinate compression
  vals = nums.uniq.sort
  idx_map = {}
  vals.each_with_index { |v, i| idx_map[v] = i + 1 }
  m = vals.size

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
    # smallest index with prefix sum >= k (k >= 1)
    def kth(k)
      idx = 0
      bitmask = 1 << (Math.log2(@n).to_i + 1)
      while bitmask > 0
        t = idx + bitmask
        if t <= @n && @tree[t] < k
          idx = t
          k -= @tree[t]
        end
        bitmask >>= 1
      end
      idx + 1
    end
  end

  freqBIT = BIT.new(m)
  sumBIT = BIT.new(m)

  costs = Array.new(n - x + 1, 0)

  window_sum = 0
  (0...x).each do |i|
    v = nums[i]
    id = idx_map[v]
    freqBIT.add(id, 1)
    sumBIT.add(id, v)
    window_sum += v
  end

  median_idx = freqBIT.kth((x + 1) / 2)
  median_val = vals[median_idx - 1]
  cnt_left = freqBIT.sum(median_idx)
  sum_left = sumBIT.sum(median_idx)
  cnt_right = x - cnt_left
  sum_right = window_sum - sum_left
  costs[0] = median_val * cnt_left - sum_left + sum_right - median_val * cnt_right

  (1..n - x).each do |start|
    out_v = nums[start - 1]
    out_id = idx_map[out_v]
    freqBIT.add(out_id, -1)
    sumBIT.add(out_id, -out_v)
    window_sum -= out_v

    in_v = nums[start + x - 1]
    in_id = idx_map[in_v]
    freqBIT.add(in_id, 1)
    sumBIT.add(in_id, in_v)
    window_sum += in_v

    median_idx = freqBIT.kth((x + 1) / 2)
    median_val = vals[median_idx - 1]
    cnt_left = freqBIT.sum(median_idx)
    sum_left = sumBIT.sum(median_idx)
    cnt_right = x - cnt_left
    sum_right = window_sum - sum_left
    costs[start] = median_val * cnt_left - sum_left + sum_right - median_val * cnt_right
  end

  mwin = n - x + 1
  inf = (1 << 60)
  dp = Array.new(mwin + 1) { Array.new(k + 1, inf) }
  dp[0][0] = 0

  (1..mwin).each do |i|
    (0..k).each do |j|
      # not take window ending at i-1
      val = dp[i - 1][j]
      dp[i][j] = val if val < dp[i][j]

      if i >= x && j > 0
        cand = dp[i - x][j - 1] + costs[i - x]
        dp[i][j] = cand if cand < dp[i][j]
      end
    end
  end

  dp[mwin][k]
end
```

## Scala

```scala
import java.util.{PriorityQueue, Comparator}
import scala.collection.mutable

object Solution {
  def minOperations(nums: Array[Int], x: Int, k: Int): Long = {
    val n = nums.length
    val m = n - x + 1
    val cost = new Array[Long](m)

    class DualHeap {
      private val small = new PriorityQueue[Int](Comparator.reverseOrder()) // max-heap
      private val large = new PriorityQueue[Int]()                           // min-heap
      private val delayed = mutable.Map.empty[Int, Int].withDefaultValue(0)
      private var smallSize = 0
      private var largeSize = 0
      private var sumSmall: Long = 0L
      private var sumLarge: Long = 0L

      private def prune(heap: PriorityQueue[Int]): Unit = {
        while (!heap.isEmpty) {
          val num = heap.peek()
          if (delayed(num) > 0) {
            delayed(num) -= 1
            if (delayed(num) == 0) delayed.remove(num)
            heap.poll()
          } else return
        }
      }

      private def makeBalance(): Unit = {
        // ensure smallSize >= largeSize and difference <= 1
        if (smallSize > largeSize + 1) {
          val num = small.poll()
          sumSmall -= num
          smallSize -= 1
          large.offer(num)
          sumLarge += num
          largeSize += 1
          prune(small)
        } else if (smallSize < largeSize) {
          val num = large.poll()
          sumLarge -= num
          largeSize -= 1
          small.offer(num)
          sumSmall += num
          smallSize += 1
          prune(large)
        }
      }

      def add(num: Int): Unit = {
        if (small.isEmpty || num <= small.peek()) {
          small.offer(num)
          sumSmall += num
          smallSize += 1
        } else {
          large.offer(num)
          sumLarge += num
          largeSize += 1
        }
        makeBalance()
      }

      def remove(num: Int): Unit = {
        delayed(num) += 1
        if (small.nonEmpty && num <= small.peek()) {
          smallSize -= 1
          sumSmall -= num
          if (num == small.peek()) prune(small)
        } else {
          largeSize -= 1
          sumLarge -= num
          if (large.nonEmpty && num == large.peek()) prune(large)
        }
        makeBalance()
      }

      def getCost: Long = {
        val median = small.peek()
        val left = median.toLong * smallSize - sumSmall
        val right = sumLarge - median.toLong * largeSize
        left + right
      }
    }

    // compute cost for each window
    val dh = new DualHeap
    var i = 0
    while (i < x) {
      dh.add(nums(i))
      i += 1
    }
    cost(0) = dh.getCost
    var start = 1
    while (start < m) {
      dh.remove(nums(start - 1))
      dh.add(nums(start + x - 1))
      cost(start) = dh.getCost
      start += 1
    }

    val INF: Long = Long.MaxValue / 4
    // dp[j][i] = min cost using first i elements and j windows
    val dp = Array.fill(k + 1, n + 1)(INF)
    dp(0)(0) = 0L

    var idx = 1
    while (idx <= n) {
      var j = 0
      while (j <= k) {
        // skip current position
        dp(j)(idx) = math.min(dp(j)(idx), dp(j)(idx - 1))
        j += 1
      }
      if (idx >= x) {
        val wIdx = idx - x // start index of window ending at idx-1
        val c = cost(wIdx)
        var jj = 1
        while (jj <= k) {
          if (dp(jj - 1)(idx - x) != INF) {
            dp(jj)(idx) = math.min(dp(jj)(idx), dp(jj - 1)(idx - x) + c)
          }
          jj += 1
        }
      }
      idx += 1
    }

    dp(k)(n)
  }
}
```

## Rust

```rust
use std::collections::BTreeMap;

struct MultiSet {
    map: BTreeMap<i32, i32>,
    size: usize,
    sum: i64,
}

impl MultiSet {
    fn new() -> Self {
        MultiSet {
            map: BTreeMap::new(),
            size: 0,
            sum: 0,
        }
    }
    fn insert(&mut self, v: i32) {
        *self.map.entry(v).or_insert(0) += 1;
        self.size += 1;
        self.sum += v as i64;
    }
    fn erase(&mut self, v: i32) {
        if let Some(cnt) = self.map.get_mut(&v) {
            *cnt -= 1;
            if *cnt == 0 {
                self.map.remove(&v);
            }
            self.size -= 1;
            self.sum -= v as i64;
        }
    }
    fn max(&self) -> Option<i32> {
        self.map.iter().next_back().map(|(&k, _)| k)
    }
    fn min(&self) -> Option<i32> {
        self.map.iter().next().map(|(&k, _)| k)
    }
}

fn rebalance(low: &mut MultiSet, high: &mut MultiSet) {
    // ensure low.size >= high.size and difference <= 1
    while low.size > high.size + 1 {
        let val = low.max().unwrap();
        low.erase(val);
        high.insert(val);
    }
    while low.size < high.size {
        let val = high.min().unwrap();
        high.erase(val);
        low.insert(val);
    }
}

fn insert_val(v: i32, low: &mut MultiSet, high: &mut MultiSet) {
    if low.size == 0 {
        low.insert(v);
    } else {
        let max_low = low.max().unwrap();
        if v <= max_low {
            low.insert(v);
        } else {
            high.insert(v);
        }
    }
    rebalance(low, high);
}

fn erase_val(v: i32, low: &mut MultiSet, high: &mut MultiSet) {
    // decide where the value resides based on current median
    if low.size > 0 && v <= low.max().unwrap() {
        low.erase(v);
    } else {
        high.erase(v);
    }
    rebalance(low, high);
}

impl Solution {
    pub fn min_operations(nums: Vec<i32>, x: i32, k: i32) -> i64 {
        let n = nums.len();
        let m = x as usize;
        let w = n - m + 1;
        let mut costs = vec![0i64; w];

        let mut low = MultiSet::new();
        let mut high = MultiSet::new();

        for i in 0..n {
            insert_val(nums[i], &mut low, &mut high);
            if i >= m {
                erase_val(nums[i - m], &mut low, &mut high);
            }
            if i + 1 >= m {
                let start = i + 1 - m;
                let median = low.max().unwrap();
                let left = median as i64 * (low.size as i64) - low.sum;
                let right = high.sum - median as i64 * (high.size as i64);
                costs[start] = left + right;
            }
        }

        const INF: i64 = 4_000_000_000_000_000_000;
        let kk = k as usize;
        let mut dp = vec![vec![INF; kk + 1]; n + 1];
        dp[0][0] = 0;

        for i in 1..=n {
            for j in 0..=kk {
                dp[i][j] = dp[i - 1][j];
            }
            if i >= m {
                let start = i - m;
                let cost = costs[start];
                for j in 1..=kk {
                    let prev = dp[start][j - 1];
                    if prev + cost < dp[i][j] {
                        dp[i][j] = prev + cost;
                    }
                }
            }
        }

        dp[n][kk]
    }
}
```

## Racket

```racket
(require racket/heap)

(define (min-operations nums x k)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (let* ([n (length nums)]
         [arr (list->vector nums)]
         [m (- n x -1)] ; number of possible windows
         [costs (make-vector m 0)]
         ;; heaps and auxiliary data for sliding median
         [lower (make-heap >)]   ; max‑heap
         [upper (make-heap <)]   ; min‑heap
         [delL (make-hash)]      ; lazy deletions for lower
         [delU (make-hash)]      ; lazy deletions for upper
         [sizeL 0] [sizeU 0]
         [sumL 0] [sumU 0]
         [targetL (quotient (+ x 1) 2)]
         
         ;; helpers
         (define (hash-inc! h key)
           (hash-set! h key (+ (hash-ref h key 0) 1)))
         (define (prune! heap del)
           (let loop ()
             (define top (heap-peek heap))
             (when top
               (define cnt (hash-ref del top 0))
               (if (> cnt 0)
                   (begin
                     (heap-pop! heap)
                     (hash-set! del top (- cnt 1))
                     (loop))
                   (void)))))
         (define (clean-peek! heap del)
           (prune! heap del)
           (heap-peek heap))
         
         ;; insertion
         (define (add! v)
           (let ([med (clean-peek! lower delL)])
             (if (or (not med) (<= v med))
                 (begin
                   (heap-push! lower v)
                   (set! sumL (+ sumL v))
                   (set! sizeL (+ sizeL 1)))
                 (begin
                   (heap-push! upper v)
                   (set! sumU (+ sumU v))
                   (set! sizeU (+ sizeU 1))))))
         
         ;; removal (lazy)
         (define (remove! v)
           (let ([med (clean-peek! lower delL)])
             (if (and med (<= v med))
                 (begin
                   (hash-inc! delL v)
                   (set! sumL (- sumL v))
                   (set! sizeL (- sizeL 1)))
                 (begin
                   (hash-inc! delU v)
                   (set! sumU (- sumU v))
                   (set! sizeU (- sizeU 1))))))
         
         ;; rebalance to keep lower size = targetL
         (define (rebalance!)
           (let loop ()
             (cond [(> sizeL targetL)
                    (prune! lower delL)
                    (define val (heap-pop! lower))
                    (set! sumL (- sumL val))
                    (set! sizeL (- sizeL 1))
                    (heap-push! upper val)
                    (set! sumU (+ sumU val))
                    (set! sizeU (+ sizeU 1))
                    (loop)]
                   [(< sizeL targetL)
                    (prune! upper delU)
                    (define val (heap-pop! upper))
                    (set! sumU (- sumU val))
                    (set! sizeU (- sizeU 1))
                    (heap-push! lower val)
                    (set! sumL (+ sumL val))
                    (set! sizeL (+ sizeL 1))
                    (loop)]
                   [else (void)]))
           ;; final clean
           (prune! lower delL)
           (prune! upper delU)))
         
         ;; compute cost from current state
         (define (current-cost)
           (let ([med (clean-peek! lower delL)])
             (- (+ (* med sizeL) (- sumL) (* med sizeU) (- sumU))
                0))) ; placeholder to force integer arithmetic
         )
    
    ;; build first window
    (for ([i (in-range x)])
      (add! (vector-ref arr i)))
    (rebalance!)
    (let ([med (clean-peek! lower delL)])
      (vector-set! costs 0 (- (+ (* med sizeL) (- sumL)) (+ (* med sizeU) (- sumU)))))
    
    ;; slide windows
    (for ([i (in-range x n)])
      (remove! (vector-ref arr (- i x)))
      (add! (vector-ref arr i))
      (rebalance!)
      (let* ([start (- i x +1)]
             [med (clean-peek! lower delL)]
             [cst (- (+ (* med sizeL) (- sumL)) (+ (* med sizeU) (- sumU)))])
        (when (< start m)
          (vector-set! costs start cst))))
    
    ;; DP: dp[cnt][pos] minimal cost using first pos elements, cnt windows
    (define INF 1000000000000000000)
    (define dp (make-vector (add1 k)))
    (let ([v0 (make-vector (add1 n) 0)])
      (vector-set! dp 0 v0))
    (for ([cnt (in-range 1 (add1 k))])
      (vector-set! dp cnt (make-vector (add1 n) INF)))
    
    (for ([cnt (in-range 1 (add1 k))])
      (define cur (vector-ref dp cnt))
      (define prev (vector-ref dp (- cnt 1)))
      (for ([pos (in-range 1 (add1 n))])
        (define best (vector-ref cur (- pos 1))) ; skip current position
        (when (>= pos x)
          (define start (- pos x))
          (define cand (+ (vector-ref prev start) (vector-ref costs start)))
          (when (< cand best) (set! best cand)))
        (vector-set! cur pos best)))
    
    (vector-ref (vector-ref dp k) n)))
```

## Erlang

```erlang
-spec min_operations(Nums :: [integer()], X :: integer(), K :: integer()) -> integer().
min_operations(Nums, X, K) ->
    INF = 1000000000000000000,
    N = length(Nums),
    %% convert nums to tuple for O(1) access
    NumT = list_to_tuple(Nums),

    %% coordinate compression
    Sorted = lists:usort(Nums),
    ValT = list_to_tuple(Sorted),
    M = tuple_size(ValT),
    IndexMap = maps:from_list(lists:zip(Sorted, lists:seq(1, M))),

    %% BIT arrays for frequencies and sums
    Freq0 = array:new(M, [{default, 0}]),
    Sum0  = array:new(M, [{default, 0}]),

    %% build initial window [0, X-1]
    {Freq1, Sum1, TotalSum} = init_window(0, X - 1, NumT, IndexMap, Freq0, Sum0, 0),

    %% compute costs for each possible start
    CostsRev = compute_costs(0, N - X, NumT, IndexMap, ValT, M, X,
                             Freq1, Sum1, TotalSum, []),
    Costs = lists:reverse(CostsRev),   % list indexed from 0

    %% DP over positions 0..N
    ZeroTuple = make_tuple(K + 1, INF),
    ZeroTuple2 = setelement(1, ZeroTuple, 0),
    DPA0 = array:new(N + 1, [{default, undefined}]),
    DPA1 = array:set(0, ZeroTuple2, DPA0),

    DPFinal = dp_loop(0, N - 1, X, K, INF, Costs, DPA1),
    ResultTuple = array:get(N, DPFinal),
    element(K + 1, ResultTuple).

%% initialize BITs with elements from L..R (inclusive)
init_window(L, R, NumT, IndexMap, FreqA, SumA, Tot) when L =< R ->
    Val = element(L + 1, NumT),
    Idx = maps:get(Val, IndexMap),
    FreqB = bit_add(Idx, 1, FreqA),
    SumB  = bit_add(Idx, Val, SumA),
    init_window(L + 1, R, NumT, IndexMap, FreqB, SumB, Tot + Val);
init_window(_, _, _, _, FreqA, SumA, Tot) ->
    {FreqA, SumA, Tot}.

%% compute costs for each start position, accumulating in reverse order list
compute_costs(Start, MaxStart, NumT, IndexMap, ValT, M, X,
              FreqA, SumA, TotalSum, Acc) when Start =< MaxStart ->
    MedianIdx = find_kth((X + 1) div 2, M, FreqA),
    MedianVal = element(MedianIdx, ValT),

    LeftCnt = bit_sum(MedianIdx, FreqA),
    LeftSum = bit_sum(MedianIdx, SumA),

    RightCnt = X - LeftCnt,
    RightSum = TotalSum - LeftSum,

    Cost = MedianVal * LeftCnt - LeftSum + RightSum - MedianVal * RightCnt,

    %% slide window
    OutVal = element(Start + 1, NumT),
    OutIdx = maps:get(OutVal, IndexMap),
    FreqB = bit_add(OutIdx, -1, FreqA),
    SumB  = bit_add(OutIdx, -OutVal, SumA),
    NewTotal = TotalSum - OutVal,

    InPos = Start + X,
    InVal = element(InPos + 1, NumT),
    InIdx = maps:get(InVal, IndexMap),
    FreqC = bit_add(InIdx, 1, FreqB),
    SumC  = bit_add(InIdx, InVal, SumB),
    NewTotal2 = NewTotal + InVal,

    compute_costs(Start + 1, MaxStart, NumT, IndexMap, ValT, M, X,
                  FreqC, SumC, NewTotal2, [Cost | Acc]);
compute_costs(_, _, _, _, _, _, _, _, _, _, Acc) ->
    Acc.

%% DP loop over positions
dp_loop(I, NMinus1, X, K, INF, Costs, DPA) when I =< NMinus1 ->
    Prev = array:get(I, DPA),
    Updated0 = Prev,
    Updated =
        if I >= X - 1 ->
                StartIdx = I - X + 1,
                CostStart = lists:nth(StartIdx + 1, Costs),
                Base = array:get(StartIdx, DPA),
                dp_update(0, K - 1, Base, Updated0, CostStart, INF)
        ; true -> Updated0
        end,
    DPA2 = array:set(I + 1, Updated, DPA),
    dp_loop(I + 1, NMinus1, X, K, INF, Costs, DPA2);
dp_loop(_, _, _, _, _, _, DPA) ->
    DPA.

%% update DP tuple for taking a window starting at current position
dp_update(Cur, MaxC, Base, CurTuple, CostStart, INF) when Cur =< MaxC ->
    PrevVal = element(Cur + 1, Base),
    NewTuple =
        if PrevVal < INF ->
                NewCost = PrevVal + CostStart,
                Existing = element(Cur + 2, CurTuple),
                MinCost = if NewCost < Existing -> NewCost; true -> Existing end,
                setelement(Cur + 2, CurTuple, MinCost)
           ; true -> CurTuple
        end,
    dp_update(Cur + 1, MaxC, Base, NewTuple, CostStart, INF);
dp_update(_, _, _, Tuple, _, _) ->
    Tuple.

%% create a tuple of Size elements all set to Val
make_tuple(Size, Val) ->
    list_to_tuple(lists:duplicate(Size, Val)).

%% BIT add (point update)
bit_add(Index, Delta, Arr) ->
    Size = array:size(Arr),
    bit_add_loop(Index, Delta, Arr, Size).

bit_add_loop(I, Delta, Arr, Size) when I =< Size ->
    Cur = case array:get(I, Arr) of undefined -> 0; V -> V end,
    NewArr = array:set(I, Cur + Delta, Arr),
    NextI = I + (I band -I),
    bit_add_loop(NextI, Delta, NewArr, Size);
bit_add_loop(_, _, Arr, _) ->
    Arr.

%% BIT prefix sum
bit_sum(Index, Arr) -> bit_sum_loop(Index, Arr, 0).

bit_sum_loop(I, Arr, Acc) when I > 0 ->
    Cur = case array:get(I, Arr) of undefined -> 0; V -> V end,
    bit_sum_loop(I - (I band -I), Arr, Acc + Cur);
bit_sum_loop(_, _, Acc) -> Acc.

%% find smallest index such that prefix sum >= Kth
find_kth(Kth, MaxIdx, FreqArr) ->
    find_kth_bin(1, MaxIdx, Kth, FreqArr).

find_kth_bin(Low, High, Kth, Arr) when Low < High ->
    Mid = (Low + High) div 2,
    SumMid = bit_sum(Mid, Arr),
    if SumMid >= Kth -> find_kth_bin(Low, Mid, Kth, Arr);
       true -> find_kth_bin(Mid + 1, High, Kth, Arr)
    end;
find_kth_bin(Low, _, _, _) -> Low.
```

## Elixir

```elixir
defmodule BIT do
  @spec new(non_neg_integer()) :: :array.array(integer())
  def new(size) do
    :array.new(size + 2, default: 0)
  end

  @spec update(:array.array(integer()), pos_integer(), integer()) :: :array.array(integer())
  def update(bit, idx, delta) when idx > 0 do
    size = :array.size(bit) - 1
    do_update(bit, idx, delta, size)
  end

  defp do_update(bit, idx, _delta, size) when idx > size, do: bit

  defp do_update(bit, idx, delta, size) do
    val = :array.get(idx, bit) + delta
    bit = :array.set(idx, val, bit)
    next = idx + (idx &&& -idx)
    do_update(bit, next, delta, size)
  end

  @spec query(:array.array(integer()), non_neg_integer()) :: integer()
  def query(_bit, 0), do: 0
  def query(bit, idx) when idx > 0 do
    do_query(bit, idx, 0)
  end

  defp do_query(_bit, 0, acc), do: acc

  defp do_query(bit, idx, acc) do
    val = :array.get(idx, bit)
    next = idx - (idx &&& -idx)
    do_query(bit, next, acc + val)
  end

  @spec kth(:array.array(integer()), pos_integer()) :: pos_integer()
  def kth(bit, k) when k > 0 do
    size = :array.size(bit) - 1
    max_pow = highest_one_bit(size)
    find_kth(bit, k, 0, max_pow, size)
  end

  defp highest_one_bit(n) do
    1 <<< (Float.floor(:math.log2(n)) |> trunc)
  end

  defp find_kth(_bit, _k, idx, 0, _size), do: idx + 1

  defp find_kth(bit, k, idx, step, size) do
    next = idx + step
    if next <= size and :array.get(next, bit) < k do
      find_kth(bit, k - :array.get(next, bit), next, div(step, 2), size)
    else
      find_kth(bit, k, idx, div(step, 2), size)
    end
  end
end

defmodule Solution do
  @spec min_operations(nums :: [integer], x :: integer, k :: integer) :: integer
  def min_operations(nums, x, k) do
    n = length(nums)
    offset = 1_000_001
    size = 2_000_002

    # initial BITs
    cnt_bit = BIT.new(size)
    sum_bit = BIT.new(size)

    total_sum =
      Enum.reduce(0..(x - 1), {cnt_bit, sum_bit, 0}, fn i, {cbit, sbit, acc} ->
        v = Enum.at(nums, i)
        idx = v + offset
        cbit = BIT.update(cbit, idx, 1)
        sbit = BIT.update(sbit, idx, v)
        {cbit, sbit, acc + v}
      end)

    {cnt_bit, sum_bit, total_sum} = total_sum

    median_idx = BIT.kth(cnt_bit, div(x + 1, 2))
    median_val = median_idx - offset
    left_cnt = BIT.query(cnt_bit, median_idx)
    left_sum = BIT.query(sum_bit, median_idx)
    right_cnt = x - left_cnt
    right_sum = total_sum - left_sum

    cost0 =
      median_val * left_cnt - left_sum + right_sum - median_val * right_cnt

    # compute costs for all windows
    {_, _, _, rev_costs} =
      Enum.reduce(1..(n - x), {cnt_bit, sum_bit, total_sum, [cost0]}, fn start,
                                                                      {cbit, sbit, tsum, acc} ->
        out_v = Enum.at(nums, start - 1)
        in_v = Enum.at(nums, start + x - 1)

        out_idx = out_v + offset
        in_idx = in_v + offset

        cbit = BIT.update(cbit, out_idx, -1)
        sbit = BIT.update(sbit, out_idx, -out_v)
        tsum = tsum - out_v

        cbit = BIT.update(cbit, in_idx, 1)
        sbit = BIT.update(sbit, in_idx, in_v)
        tsum = tsum + in_v

        median_idx = BIT.kth(cbit, div(x + 1, 2))
        median_val = median_idx - offset
        left_cnt = BIT.query(cbit, median_idx)
        left_sum = BIT.query(sbit, median_idx)
        right_cnt = x - left_cnt
        right_sum = tsum - left_sum

        cost =
          median_val * left_cnt - left_sum + right_sum - median_val * right_cnt

        {cbit, sbit, tsum, [cost | acc]}
      end)

    costs = Enum.reverse(rev_costs) # length n - x + 1

    inf = 1 <<< 60
    dp0_row = List.duplicate(inf, k + 1) |> List.replace_at(0, 0)
    dp_arr = :array.new(n + 1, default: nil) |> :array.set(0, dp0_row)

    dp_arr =
      Enum.reduce(1..n, dp_arr, fn i, dparray ->
        prev = :array.get(i - 1, dparray)
        cur = List.to_tuple(prev) |> Tuple.to_list() # copy

        if i >= x do
          base = :array.get(i - x, dparray)
          cost_i = Enum.at(costs, i - x)

          cur =
            Enum.reduce(1..k, cur, fn j, acc_cur ->
              cand = Enum.at(base, j - 1) + cost_i
              if cand < Enum.at(acc_cur, j) do
                List.replace_at(acc_cur, j, cand)
              else
                acc_cur
              end
            end)

          :array.set(i, cur, dparray)
        else
          :array.set(i, cur, dparray)
        end
      end)

    final_row = :array.get(n, dp_arr)
    Enum.at(final_row, k)
  end
end
```
