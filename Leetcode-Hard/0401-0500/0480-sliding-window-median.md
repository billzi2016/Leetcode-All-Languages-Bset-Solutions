# 0480. Sliding Window Median

## Cpp

```cpp
class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        multiset<int> lo, hi; // lo: max side, hi: min side
        
        auto add = [&](int x) {
            if (lo.empty() || x <= *prev(lo.end())) lo.insert(x);
            else hi.insert(x);
        };
        
        auto remove = [&](int x) {
            auto it = lo.find(x);
            if (it != lo.end()) lo.erase(it);
            else {
                it = hi.find(x);
                if (it != hi.end()) hi.erase(it);
            }
        };
        
        auto rebalance = [&]() {
            int target = (k + 1) / 2; // desired size of lo
            while ((int)lo.size() > target) {
                auto it = prev(lo.end());
                hi.insert(*it);
                lo.erase(it);
            }
            while ((int)lo.size() < target) {
                auto it = hi.begin();
                lo.insert(*it);
                hi.erase(it);
            }
            // ensure ordering: max(lo) <= min(hi)
            if (!lo.empty() && !hi.empty()) {
                while (*prev(lo.end()) > *hi.begin()) {
                    int a = *prev(lo.end());
                    int b = *hi.begin();
                    lo.erase(prev(lo.end()));
                    hi.erase(hi.begin());
                    lo.insert(b);
                    hi.insert(a);
                }
            }
        };
        
        auto getMedian = [&]() -> double {
            if (k % 2) return (double)*prev(lo.end());
            return ((double)*prev(lo.end()) + *hi.begin()) / 2.0;
        };
        
        vector<double> ans;
        for (int i = 0; i < (int)nums.size(); ++i) {
            add(nums[i]);
            rebalance();
            if (i >= k - 1) {
                ans.push_back(getMedian());
                int out = nums[i - k + 1];
                remove(out);
                rebalance();
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
    private PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
    private PriorityQueue<Integer> minHeap = new PriorityQueue<>();
    private Map<Integer, Integer> delayed = new HashMap<>();
    private int lowerSize = 0; // size of maxHeap (valid elements)
    private int higherSize = 0; // size of minHeap (valid elements)

    public double[] medianSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        double[] res = new double[n - k + 1];
        int idx = 0;

        for (int i = 0; i < n; i++) {
            addNum(nums[i]);
            if (i >= k) {
                removeNum(nums[i - k]);
            }
            rebalance();
            if (i >= k - 1) {
                res[idx++] = getMedian(k);
            }
        }
        return res;
    }

    private void addNum(int num) {
        if (maxHeap.isEmpty() || num <= maxHeap.peek()) {
            maxHeap.offer(num);
            lowerSize++;
        } else {
            minHeap.offer(num);
            higherSize++;
        }
    }

    private void removeNum(int num) {
        delayed.put(num, delayed.getOrDefault(num, 0) + 1);
        if (!maxHeap.isEmpty() && num <= maxHeap.peek()) {
            lowerSize--;
            if (num == maxHeap.peek()) {
                prune(maxHeap);
            }
        } else {
            higherSize--;
            if (!minHeap.isEmpty() && num == minHeap.peek()) {
                prune(minHeap);
            }
        }
    }

    private void rebalance() {
        // Ensure lowerSize >= higherSize and difference <= 1
        if (lowerSize > higherSize + 1) {
            int moved = maxHeap.poll();
            lowerSize--;
            minHeap.offer(moved);
            higherSize++;
            prune(maxHeap);
        } else if (lowerSize < higherSize) {
            int moved = minHeap.poll();
            higherSize--;
            maxHeap.offer(moved);
            lowerSize++;
            prune(minHeap);
        }
    }

    private void prune(PriorityQueue<Integer> heap) {
        while (!heap.isEmpty()) {
            int num = heap.peek();
            Integer cnt = delayed.get(num);
            if (cnt != null && cnt > 0) {
                if (cnt == 1) {
                    delayed.remove(num);
                } else {
                    delayed.put(num, cnt - 1);
                }
                heap.poll();
            } else {
                break;
            }
        }
    }

    private double getMedian(int k) {
        if ((k & 1) == 1) { // odd
            return (double) maxHeap.peek();
        } else {
            return ((double) maxHeap.peek() + minHeap.peek()) / 2.0;
        }
    }
}
```

## Python

```python
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        import heapq
        from collections import defaultdict

        small = []  # max-heap (store negatives)
        large = []  # min-heap
        delayed = defaultdict(int)  # value -> count to be removed lazily
        smallSize = 0  # effective sizes excluding delayed elements
        largeSize = 0
        res = []

        def prune(heap):
            while heap:
                num = -heap[0] if heap is small else heap[0]
                if delayed.get(num, 0):
                    heapq.heappop(heap)
                    delayed[num] -= 1
                    if delayed[num] == 0:
                        del delayed[num]
                else:
                    break

        def makeBalance():
            nonlocal smallSize, largeSize
            # Ensure size property: smallSize >= largeSize and diff <= 1
            if smallSize > largeSize + 1:
                val = -heapq.heappop(small)
                smallSize -= 1
                heapq.heappush(large, val)
                largeSize += 1
                prune(small)
            elif smallSize < largeSize:
                val = heapq.heappop(large)
                largeSize -= 1
                heapq.heappush(small, -val)
                smallSize += 1
                prune(large)

        def addNum(num):
            nonlocal smallSize, largeSize
            if not small or num <= -small[0]:
                heapq.heappush(small, -num)
                smallSize += 1
            else:
                heapq.heappush(large, num)
                largeSize += 1
            makeBalance()

        def removeNum(num):
            nonlocal smallSize, largeSize
            delayed[num] += 1
            if num <= -small[0]:
                smallSize -= 1
                if num == -small[0]:
                    prune(small)
            else:
                largeSize -= 1
                if large and num == large[0]:
                    prune(large)
            makeBalance()

        def getMedian():
            if k % 2:  # odd
                return float(-small[0])
            else:
                return (-small[0] + large[0]) / 2.0

        for i, num in enumerate(nums):
            addNum(num)
            if i >= k - 1:
                res.append(getMedian())
                removeNum(nums[i - k + 1])

        return res
```

## Python3

```python
from typing import List
import heapq
from collections import defaultdict

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        low = []   # max-heap (store negatives)
        high = []  # min-heap
        delayed = defaultdict(int)

        len_low = len_high = 0  # effective sizes excluding delayed elements

        def prune(heap):
            while heap:
                num = -heap[0] if heap is low else heap[0]
                if delayed[num]:
                    heapq.heappop(heap)
                    delayed[num] -= 1
                    if delayed[num] == 0:
                        del delayed[num]
                else:
                    break

        def balance():
            nonlocal len_low, len_high
            # ensure len_low >= len_high and difference <= 1
            if len_low > len_high + 1:
                # move top from low to high
                prune(low)
                val = -heapq.heappop(low)
                len_low -= 1
                heapq.heappush(high, val)
                len_high += 1
                prune(low)
            elif len_low < len_high:
                prune(high)
                val = heapq.heappop(high)
                len_high -= 1
                heapq.heappush(low, -val)
                len_low += 1
                prune(high)

        # initialize first window
        for i in range(k):
            num = nums[i]
            if not low or num <= -low[0]:
                heapq.heappush(low, -num)
                len_low += 1
            else:
                heapq.heappush(high, num)
                len_high += 1
            balance()
        prune(low); prune(high)

        res = []
        median = (-low[0]) if k % 2 == 1 else ((-low[0] + high[0]) / 2.0)
        res.append(float(median))

        # slide the window
        for i in range(k, len(nums)):
            out_num = nums[i - k]
            in_num = nums[i]

            # mark outgoing number for delayed removal
            delayed[out_num] += 1
            if out_num <= -low[0]:
                len_low -= 1
                if out_num == -low[0]:
                    prune(low)
            else:
                len_high -= 1
                if high and out_num == high[0]:
                    prune(high)

            # add incoming number
            if in_num <= -low[0]:
                heapq.heappush(low, -in_num)
                len_low += 1
            else:
                heapq.heappush(high, in_num)
                len_high += 1

            balance()
            prune(low); prune(high)

            median = (-low[0]) if k % 2 == 1 else ((-low[0] + high[0]) / 2.0)
            res.append(float(median))

        return res
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

/* Binary search: returns 1‑based index in compressed array */
static int get_index(int *arr, int size, int val) {
    int l = 0, r = size - 1;
    while (l <= r) {
        int m = (l + r) >> 1;
        if (arr[m] == val) return m + 1;          /* 1‑based for BIT */
        else if (arr[m] < val) l = m + 1;
        else r = m - 1;
    }
    return -1;   /* should never happen */
}

/* Fenwick Tree */
static void bit_add(int *bit, int n, int idx, int delta) {
    while (idx <= n) {
        bit[idx] += delta;
        idx += idx & -idx;
    }
}

/* Find smallest index such that prefix sum >= k (k is 1‑based rank) */
static int bit_find_kth(int *bit, int n, int k) {
    int idx = 0;
    int mask = 1;
    while (mask << 1 <= n) mask <<= 1;   /* highest power of two ≤ n */
    for (; mask; mask >>= 1) {
        int next = idx + mask;
        if (next <= n && bit[next] < k) {
            idx = next;
            k -= bit[next];
        }
    }
    return idx + 1;   /* 1‑based index */
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
double* medianSlidingWindow(int* nums, int numsSize, int k, int* returnSize) {
    if (numsSize == 0 || k == 0) {
        *returnSize = 0;
        return NULL;
    }

    /* coordinate compression */
    int *sorted = malloc(sizeof(int) * numsSize);
    memcpy(sorted, nums, sizeof(int) * numsSize);
    qsort(sorted, numsSize, sizeof(int), cmp_int);
    int uniqCount = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (i == 0 || sorted[i] != sorted[i - 1])
            sorted[uniqCount++] = sorted[i];
    }

    /* Fenwick tree */
    int *bit = calloc(uniqCount + 2, sizeof(int));

    int resLen = numsSize - k + 1;
    double *res = malloc(sizeof(double) * resLen);
    *returnSize = resLen;

    for (int i = 0; i < numsSize; ++i) {
        int idxAdd = get_index(sorted, uniqCount, nums[i]);
        bit_add(bit, uniqCount, idxAdd, 1);

        if (i >= k) {
            int idxRem = get_index(sorted, uniqCount, nums[i - k]);
            bit_add(bit, uniqCount, idxRem, -1);
        }

        if (i >= k - 1) {
            if (k & 1) {   /* odd */
                int rank = (k + 1) / 2;
                int pos = bit_find_kth(bit, uniqCount, rank);
                res[i - k + 1] = (double)sorted[pos - 1];
            } else {       /* even */
                int rank1 = k / 2;
                int rank2 = rank1 + 1;
                int pos1 = bit_find_kth(bit, uniqCount, rank1);
                int pos2 = bit_find_kth(bit, uniqCount, rank2);
                res[i - k + 1] = ((double)sorted[pos1 - 1] + (double)sorted[pos2 - 1]) / 2.0;
            }
        }
    }

    free(sorted);
    free(bit);
    return res;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private class Heap {
        private List<int> data;
        private Comparison<int> comp;
        public Heap(Comparison<int> comparison) {
            comp = comparison;
            data = new List<int>();
        }
        public int Count => data.Count;
        public void Push(int val) {
            data.Add(val);
            int i = data.Count - 1;
            while (i > 0) {
                int p = (i - 1) >> 1;
                if (comp(data[i], data[p]) < 0) {
                    int tmp = data[i];
                    data[i] = data[p];
                    data[p] = tmp;
                    i = p;
                } else break;
            }
        }
        public int Peek() => data[0];
        public int Pop() {
            int ret = data[0];
            int last = data[data.Count - 1];
            data.RemoveAt(data.Count - 1);
            if (data.Count > 0) {
                data[0] = last;
                Heapify(0);
            }
            return ret;
        }
        private void Heapify(int i) {
            int n = data.Count;
            while (true) {
                int l = (i << 1) + 1;
                int r = l + 1;
                int smallest = i;
                if (l < n && comp(data[l], data[smallest]) < 0) smallest = l;
                if (r < n && comp(data[r], data[smallest]) < 0) smallest = r;
                if (smallest != i) {
                    int tmp = data[i];
                    data[i] = data[smallest];
                    data[smallest] = tmp;
                    i = smallest;
                } else break;
            }
        }
    }

    private Heap small; // max-heap
    private Heap large; // min-heap
    private Dictionary<int, int> delayed;
    private int smallSize;
    private int largeSize;

    public double[] MedianSlidingWindow(int[] nums, int k) {
        int n = nums.Length;
        double[] result = new double[n - k + 1];
        small = new Heap((a, b) => b.CompareTo(a)); // max-heap
        large = new Heap((a, b) => a.CompareTo(b)); // min-heap
        delayed = new Dictionary<int, int>();
        smallSize = 0;
        largeSize = 0;

        for (int i = 0; i < n; ++i) {
            AddNum(nums[i]);
            if (i >= k - 1) {
                result[i - k + 1] = GetMedian(k);
                int outNum = nums[i - k + 1];
                RemoveNum(outNum);
            }
        }
        return result;
    }

    private void AddNum(int num) {
        if (small.Count == 0 || num <= small.Peek()) {
            small.Push(num);
            ++smallSize;
        } else {
            large.Push(num);
            ++largeSize;
        }
        BalanceHeaps();
    }

    private void RemoveNum(int num) {
        // lazy removal
        if (!delayed.ContainsKey(num)) delayed[num] = 0;
        delayed[num]++;

        if (small.Count > 0 && num <= small.Peek()) {
            --smallSize;
            if (num == small.Peek()) Prune(small);
        } else {
            --largeSize;
            if (large.Count > 0 && num == large.Peek()) Prune(large);
        }
        BalanceHeaps();
    }

    private void BalanceHeaps() {
        // Ensure small has >= large and size difference at most 1
        if (smallSize > largeSize + 1) {
            // move top from small to large
            int moved = small.Pop();
            --smallSize;
            large.Push(moved);
            ++largeSize;
            Prune(small);
        } else if (smallSize < largeSize) {
            int moved = large.Pop();
            --largeSize;
            small.Push(moved);
            ++smallSize;
            Prune(large);
        }
    }

    private void Prune(Heap heap) {
        while (heap.Count > 0) {
            int top = heap.Peek();
            if (delayed.TryGetValue(top, out int cnt) && cnt > 0) {
                // remove it
                delayed[top] = cnt - 1;
                if (delayed[top] == 0) delayed.Remove(top);
                heap.Pop();
            } else break;
        }
    }

    private double GetMedian(int k) {
        if ((k & 1) == 1) {
            return (double)small.Peek();
        } else {
            return ((double)small.Peek() + large.Peek()) / 2.0;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var medianSlidingWindow = function(nums, k) {
    class Heap {
        constructor(comp) {
            this.data = [];
            this.comp = comp; // returns negative if a should be before b
        }
        size() { return this.data.length; }
        peek() { return this.data[0]; }
        push(val) {
            const arr = this.data;
            arr.push(val);
            let idx = arr.length - 1;
            while (idx > 0) {
                const parent = (idx - 1) >> 1;
                if (this.comp(arr[parent], arr[idx]) <= 0) break;
                [arr[parent], arr[idx]] = [arr[idx], arr[parent]];
                idx = parent;
            }
        }
        pop() {
            const arr = this.data;
            if (arr.length === 0) return undefined;
            const top = arr[0];
            const last = arr.pop();
            if (arr.length > 0) {
                arr[0] = last;
                this._siftDown(0);
            }
            return top;
        }
        _siftDown(idx) {
            const arr = this.data;
            const n = arr.length;
            while (true) {
                let left = idx * 2 + 1;
                let right = left + 1;
                let best = idx;
                if (left < n && this.comp(arr[left], arr[best]) < 0) best = left;
                if (right < n && this.comp(arr[right], arr[best]) < 0) best = right;
                if (best === idx) break;
                [arr[idx], arr[best]] = [arr[best], arr[idx]];
                idx = best;
            }
        }
    }

    const maxHeap = new Heap((a, b) => b - a); // lower half
    const minHeap = new Heap((a, b) => a - b); // upper half
    const delayed = new Map(); // value -> count to delete lazily

    let smallSize = 0; // effective size of maxHeap
    let largeSize = 0; // effective size of minHeap

    const prune = (heap) => {
        while (heap.size() > 0) {
            const num = heap.peek();
            if (delayed.has(num)) {
                const cnt = delayed.get(num);
                if (cnt === 1) delayed.delete(num);
                else delayed.set(num, cnt - 1);
                heap.pop();
            } else break;
        }
    };

    const balance = () => {
        // Ensure smallSize >= largeSize and difference <= 1
        if (smallSize > largeSize + 1) {
            // move top from maxHeap to minHeap
            const val = maxHeap.pop();
            smallSize--;
            minHeap.push(val);
            largeSize++;
            prune(maxHeap);
        } else if (smallSize < largeSize) {
            const val = minHeap.pop();
            largeSize--;
            maxHeap.push(val);
            smallSize++;
            prune(minHeap);
        }
    };

    const addNum = (num) => {
        if (maxHeap.size() === 0 || num <= maxHeap.peek()) {
            maxHeap.push(num);
            smallSize++;
        } else {
            minHeap.push(num);
            largeSize++;
        }
        balance();
    };

    const removeNum = (num) => {
        delayed.set(num, (delayed.get(num) || 0) + 1);
        if (num <= maxHeap.peek()) {
            smallSize--;
            if (num === maxHeap.peek()) prune(maxHeap);
        } else {
            largeSize--;
            if (minHeap.size() > 0 && num === minHeap.peek()) prune(minHeap);
        }
        balance();
    };

    const getMedian = () => {
        if (k % 2 === 1) return maxHeap.peek();
        return (maxHeap.peek() + minHeap.peek()) / 2;
    };

    const result = [];
    for (let i = 0; i < nums.length; ++i) {
        addNum(nums[i]);
        if (i >= k - 1) {
            result.push(getMedian());
            removeNum(nums[i - k + 1]);
        }
    }
    return result;
};
```

## Typescript

```typescript
function medianSlidingWindow(nums: number[], k: number): number[] {
    class Heap {
        data: number[];
        cmp: (a: number, b: number) => boolean;
        constructor(cmp: (a: number, b: number) => boolean) {
            this.data = [];
            this.cmp = cmp;
        }
        size(): number { return this.data.length; }
        peek(): number | undefined { return this.data[0]; }
        push(val: number): void {
            this.data.push(val);
            this.bubbleUp(this.size() - 1);
        }
        pop(): number | undefined {
            if (this.size() === 0) return undefined;
            const top = this.data[0];
            const last = this.data.pop()!;
            if (this.size() > 0) {
                this.data[0] = last;
                this.bubbleDown(0);
            }
            return top;
        }
        private bubbleUp(idx: number): void {
            while (idx > 0) {
                const parent = (idx - 1) >> 1;
                if (this.cmp(this.data[parent], this.data[idx])) break;
                [this.data[parent], this.data[idx]] = [this.data[idx], this.data[parent]];
                idx = parent;
            }
        }
        private bubbleDown(idx: number): void {
            const n = this.size();
            while (true) {
                let left = idx * 2 + 1;
                let right = left + 1;
                let best = idx;
                if (left < n && !this.cmp(this.data[best], this.data[left])) best = left;
                if (right < n && !this.cmp(this.data[best], this.data[right])) best = right;
                if (best === idx) break;
                [this.data[idx], this.data[best]] = [this.data[best], this.data[idx]];
                idx = best;
            }
        }
    }

    const maxHeap = new Heap((a, b) => a >= b); // lower half
    const minHeap = new Heap((a, b) => a <= b); // upper half
    const delayed = new Map<number, number>();
    let loSize = 0; // effective size of maxHeap
    let hiSize = 0; // effective size of minHeap

    const prune = (heap: Heap): void => {
        while (heap.size() > 0) {
            const num = heap.peek()!;
            const cnt = delayed.get(num);
            if (cnt !== undefined && cnt > 0) {
                heap.pop();
                if (cnt === 1) delayed.delete(num);
                else delayed.set(num, cnt - 1);
            } else break;
        }
    };

    const balance = (): void => {
        // ensure loSize >= hiSize and difference <= 1
        if (loSize > hiSize + 1) {
            const val = maxHeap.pop()!;
            minHeap.push(val);
            loSize--;
            hiSize++;
            prune(maxHeap);
        } else if (loSize < hiSize) {
            const val = minHeap.pop()!;
            maxHeap.push(val);
            hiSize--;
            loSize++;
            prune(minHeap);
        }
    };

    const getMedian = (): number => {
        if (k % 2 === 1) return maxHeap.peek()!;
        return (maxHeap.peek()! + minHeap.peek()!) / 2;
    };

    const result: number[] = [];

    for (let i = 0; i < nums.length; ++i) {
        const num = nums[i];
        if (maxHeap.size() === 0 || num <= maxHeap.peek()!) {
            maxHeap.push(num);
            loSize++;
        } else {
            minHeap.push(num);
            hiSize++;
        }
        balance();

        if (i >= k - 1) {
            result.push(getMedian());

            const out = nums[i - k + 1];
            delayed.set(out, (delayed.get(out) ?? 0) + 1);

            if (out <= maxHeap.peek()!) {
                loSize--;
                if (out === maxHeap.peek()) prune(maxHeap);
            } else {
                hiSize--;
                if (out === minHeap.peek()) prune(minHeap);
            }
            balance();
        }
    }

    return result;
}
```

## Php

```php
class DualHeap {
    public $small;
    public $large;
    public $delayed = [];
    public $k;
    public $smallSize = 0;
    public $largeSize = 0;

    public function __construct($k) {
        $this->k = $k;
        $this->small = new SplMaxHeap(); // max-heap for lower half
        $this->large = new SplMinHeap(); // min-heap for upper half
    }

    public function insert($num) {
        if ($this->small->isEmpty() || $num <= $this->small->top()) {
            $this->small->insert($num);
            $this->smallSize++;
        } else {
            $this->large->insert($num);
            $this->largeSize++;
        }
        $this->makeBalance();
    }

    public function erase($num) {
        if (!isset($this->delayed[$num])) {
            $this->delayed[$num] = 0;
        }
        $this->delayed[$num]++;

        if (!$this->small->isEmpty() && $num <= $this->small->top()) {
            $this->smallSize--;
            if ($num == $this->small->top()) {
                $this->prune($this->small);
            }
        } else {
            $this->largeSize--;
            if (!$this->large->isEmpty() && $num == $this->large->top()) {
                $this->prune($this->large);
            }
        }
        $this->makeBalance();
    }

    public function getMedian() {
        if ($this->k % 2 == 1) {
            return (float)$this->small->top();
        } else {
            return ((float)$this->small->top() + (float)$this->large->top()) / 2.0;
        }
    }

    private function makeBalance() {
        if ($this->smallSize > $this->largeSize + 1) {
            $val = $this->small->extract();
            $this->smallSize--;
            $this->large->insert($val);
            $this->largeSize++;
            $this->prune($this->small);
        } elseif ($this->smallSize < $this->largeSize) {
            $val = $this->large->extract();
            $this->largeSize--;
            $this->small->insert($val);
            $this->smallSize++;
            $this->prune($this->large);
        }
    }

    private function prune($heap) {
        while (!$heap->isEmpty()) {
            $num = $heap->top();
            if (isset($this->delayed[$num])) {
                $this->delayed[$num]--;
                if ($this->delayed[$num] == 0) {
                    unset($this->delayed[$num]);
                }
                $heap->extract();
            } else {
                break;
            }
        }
    }
}

class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Float[]
     */
    function medianSlidingWindow($nums, $k) {
        $dh = new DualHeap($k);
        $n = count($nums);
        $res = [];
        for ($i = 0; $i < $n; $i++) {
            $dh->insert($nums[$i]);
            if ($i >= $k - 1) {
                $res[] = $dh->getMedian();
                $dh->erase($nums[$i - $k + 1]);
            }
        }
        return $res;
    }
}
```

## Swift

```swift
import Foundation

struct Heap<T> {
    var elements: [T] = []
    let areSorted: (T, T) -> Bool
    
    init(_ sort: @escaping (T, T) -> Bool) {
        self.areSorted = sort
    }
    
    func peek() -> T? {
        return elements.first
    }
    
    mutating func push(_ value: T) {
        elements.append(value)
        siftUp(elements.count - 1)
    }
    
    mutating func pop() -> T? {
        guard !elements.isEmpty else { return nil }
        if elements.count == 1 {
            return elements.removeLast()
        } else {
            let top = elements[0]
            elements[0] = elements.removeLast()
            siftDown(0)
            return top
        }
    }
    
    private mutating func siftUp(_ index: Int) {
        var child = index
        var parent = (child - 1) / 2
        while child > 0 && areSorted(elements[child], elements[parent]) {
            elements.swapAt(child, parent)
            child = parent
            parent = (child - 1) / 2
        }
    }
    
    private mutating func siftDown(_ index: Int) {
        var parent = index
        while true {
            let left = parent * 2 + 1
            let right = left + 1
            var candidate = parent
            if left < elements.count && areSorted(elements[left], elements[candidate]) {
                candidate = left
            }
            if right < elements.count && areSorted(elements[right], elements[candidate]) {
                candidate = right
            }
            if candidate == parent { return }
            elements.swapAt(parent, candidate)
            parent = candidate
        }
    }
}

class Solution {
    func medianSlidingWindow(_ nums: [Int], _ k: Int) -> [Double] {
        var small = Heap<Int>(>)   // max-heap
        var large = Heap<Int>(<)   // min-heap
        var delayed = [Int: Int]()
        var result = [Double]()
        
        var smallSize = 0
        var largeSize = 0
        
        func prune(_ heap: inout Heap<Int>) {
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
            // Ensure smallSize >= largeSize and difference <= 1
            if smallSize > largeSize + 1 {
                if let moved = small.pop() {
                    large.push(moved)
                    smallSize -= 1
                    largeSize += 1
                    prune(&small)
                }
            } else if smallSize < largeSize {
                if let moved = large.pop() {
                    small.push(moved)
                    largeSize -= 1
                    smallSize += 1
                    prune(&large)
                }
            }
        }
        
        for i in 0..<nums.count {
            let num = nums[i]
            if let top = small.peek(), num <= top {
                small.push(num)
                smallSize += 1
            } else {
                large.push(num)
                largeSize += 1
            }
            balance()
            
            if i >= k - 1 {
                // Get median
                if k % 2 == 1 {
                    result.append(Double(small.peek()!))
                } else {
                    let median = (Double(small.peek()!) + Double(large.peek()!)) / 2.0
                    result.append(median)
                }
                
                // Remove outgoing element
                let outNum = nums[i - k + 1]
                delayed[outNum, default: 0] += 1
                if let top = small.peek(), outNum <= top {
                    smallSize -= 1
                    if outNum == top { prune(&small) }
                } else {
                    largeSize -= 1
                    if outNum == large.peek() { prune(&large) }
                }
                balance()
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun medianSlidingWindow(nums: IntArray, k: Int): DoubleArray {
        val n = nums.size
        if (n == 0) return doubleArrayOf()
        val result = DoubleArray(n - k + 1)
        val dh = DualHeap(k)

        for (i in 0 until n) {
            dh.add(nums[i])
            if (i >= k - 1) {
                result[i - k + 1] = dh.getMedian()
                dh.remove(nums[i - k + 1])
            }
        }
        return result
    }

    private class DualHeap(private val k: Int) {
        // max-heap for the smaller half
        private val small = java.util.PriorityQueue<Int>(Comparator { a, b -> b.compareTo(a) })
        // min-heap for the larger half
        private val large = java.util.PriorityQueue<Int>()
        // map for delayed deletions
        private val delayed = HashMap<Int, Int>()

        private var smallSize = 0   // effective size excluding delayed elements
        private var largeSize = 0

        fun getMedian(): Double {
            return if (k % 2 == 1) {
                small.peek().toDouble()
            } else {
                (small.peek() + large.peek()) / 2.0
            }
        }

        fun add(num: Int) {
            if (small.isEmpty() || num <= small.peek()) {
                small.offer(num)
                smallSize++
            } else {
                large.offer(num)
                largeSize++
            }
            makeBalance()
        }

        fun remove(num: Int) {
            delayed[num] = delayed.getOrDefault(num, 0) + 1
            if (num <= small.peek()) {
                smallSize--
                if (num == small.peek()) prune(small)
            } else {
                largeSize--
                if (large.isNotEmpty() && num == large.peek()) prune(large)
            }
            makeBalance()
        }

        private fun prune(heap: java.util.PriorityQueue<Int>) {
            while (!heap.isEmpty()) {
                val top = heap.peek()
                val cnt = delayed[top]
                if (cnt != null) {
                    // remove the top element lazily
                    heap.poll()
                    if (cnt == 1) {
                        delayed.remove(top)
                    } else {
                        delayed[top] = cnt - 1
                    }
                } else {
                    break
                }
            }
        }

        private fun makeBalance() {
            // Ensure small has the same size as large or one more element
            if (smallSize > largeSize + 1) {
                val moved = small.poll()
                large.offer(moved)
                smallSize--
                largeSize++
                prune(small)
            } else if (smallSize < largeSize) {
                val moved = large.poll()
                small.offer(moved)
                largeSize--
                smallSize++
                prune(large)
            }
        }
    }
}
```

## Dart

```dart
class Heap {
  final List<int> _data = [];
  final bool _isMin;
  Heap(this._isMin);
  int get size => _data.length;
  bool get isEmpty => _data.isEmpty;
  int top() => _data[0];
  void push(int val) {
    _data.add(val);
    _siftUp(_data.length - 1);
  }

  int pop() {
    final int res = _data[0];
    final int last = _data.removeLast();
    if (_data.isNotEmpty) {
      _data[0] = last;
      _siftDown(0);
    }
    return res;
  }

  void _siftUp(int idx) {
    while (idx > 0) {
      final int parent = (idx - 1) >> 1;
      if (_compare(_data[idx], _data[parent]) < 0) {
        _swap(idx, parent);
        idx = parent;
      } else {
        break;
      }
    }
  }

  void _siftDown(int idx) {
    final int n = _data.length;
    while (true) {
      int left = idx * 2 + 1;
      int right = left + 1;
      int best = idx;
      if (left < n && _compare(_data[left], _data[best]) < 0) best = left;
      if (right < n && _compare(_data[right], _data[best]) < 0) best = right;
      if (best != idx) {
        _swap(idx, best);
        idx = best;
      } else {
        break;
      }
    }
  }

  int _compare(int a, int b) => _isMin ? a.compareTo(b) : b.compareTo(a);

  void _swap(int i, int j) {
    final int tmp = _data[i];
    _data[i] = _data[j];
    _data[j] = tmp;
  }
}

class Solution {
  List<double> medianSlidingWindow(List<int> nums, int k) {
    final int n = nums.length;
    final List<double> result = [];

    final Heap lower = Heap(false); // max-heap
    final Heap higher = Heap(true); // min-heap
    final Map<int, int> delayed = {};

    int lowerSize = 0;
    int higherSize = 0;

    void prune(Heap heap) {
      while (!heap.isEmpty) {
        final int val = heap.top();
        if (delayed.containsKey(val)) {
          int cnt = delayed[val]!;
          if (cnt > 0) {
            heap.pop();
            if (cnt == 1) {
              delayed.remove(val);
            } else {
              delayed[val] = cnt - 1;
            }
          } else {
            break;
          }
        } else {
          break;
        }
      }
    }

    void balance() {
      // Ensure lowerSize >= higherSize and difference <= 1
      if (lowerSize > higherSize + 1) {
        int val = lower.pop();
        lowerSize--;
        higher.push(val);
        higherSize++;
        prune(lower);
      } else if (lowerSize < higherSize) {
        int val = higher.pop();
        higherSize--;
        lower.push(val);
        lowerSize++;
        prune(higher);
      }
    }

    for (int i = 0; i < n; ++i) {
      int num = nums[i];
      // Insert
      if (!lower.isEmpty && num <= lower.top()) {
        lower.push(num);
        lowerSize++;
      } else {
        higher.push(num);
        higherSize++;
      }
      balance();

      if (i >= k - 1) {
        prune(lower);
        prune(higher);

        double median;
        if (k % 2 == 1) {
          median = lower.top().toDouble();
        } else {
          median = (lower.top() + higher.top()) / 2.0;
        }
        result.add(median);

        // Remove outgoing element
        int out = nums[i - k + 1];
        delayed[out] = (delayed[out] ?? 0) + 1;
        if (out <= lower.top()) {
          lowerSize--;
        } else {
          higherSize--;
        }

        prune(lower);
        prune(higher);
        balance();
      }
    }

    return result;
  }
}
```

## Golang

```go
import "container/heap"

type MaxHeap []int

func (h MaxHeap) Len() int            { return len(h) }
func (h MaxHeap) Less(i, j int) bool  { return h[i] > h[j] } // max‑heap
func (h MaxHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *MaxHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *MaxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

type MinHeap []int

func (h MinHeap) Len() int            { return len(h) }
func (h MinHeap) Less(i, j int) bool  { return h[i] < h[j] } // min‑heap
func (h MinHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *MinHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *MinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func medianSlidingWindow(nums []int, k int) []float64 {
	if k == 0 {
		return []float64{}
	}
	small := &MaxHeap{} // lower half
	large := &MinHeap{} // upper half
	heap.Init(small)
	heap.Init(large)

	delayed := make(map[int]int) // value -> count to delete later
	var smallSize, largeSize int

	prune := func(h heap.Interface) {
		for h.Len() > 0 {
			var top int
			switch hp := h.(type) {
			case *MaxHeap:
				top = (*hp)[0]
			case *MinHeap:
				top = (*hp)[0]
			}
			if cnt, ok := delayed[top]; ok && cnt > 0 {
				heap.Pop(h)
				if cnt == 1 {
					delete(delayed, top)
				} else {
					delayed[top] = cnt - 1
				}
			} else {
				break
			}
		}
	}

	rebalance := func() {
		// ensure smallSize >= largeSize and diff <= 1
		if smallSize > largeSize+1 {
			val := heap.Pop(small).(int)
			smallSize--
			heap.Push(large, val)
			largeSize++
			prune(small)
		} else if smallSize < largeSize {
			val := heap.Pop(large).(int)
			largeSize--
			heap.Push(small, val)
			smallSize++
			prune(large)
		}
	}

	addNum := func(num int) {
		if small.Len() == 0 || num <= (*small)[0] {
			heap.Push(small, num)
			smallSize++
		} else {
			heap.Push(large, num)
			largeSize++
		}
		rebalance()
	}

	removeNum := func(num int) {
		delayed[num]++
		if num <= (*small)[0] {
			smallSize--
			if num == (*small)[0] {
				prune(small)
			}
		} else {
			largeSize--
			if large.Len() > 0 && num == (*large)[0] {
				prune(large)
			}
		}
		rebalance()
	}

	// build initial window
	for i := 0; i < k; i++ {
		addNum(nums[i])
	}

	getMedian := func() float64 {
		if k%2 == 1 {
			return float64((*small)[0])
		}
		return (float64((*small)[0]) + float64((*large)[0])) / 2.0
	}

	res := make([]float64, 0, len(nums)-k+1)
	res = append(res, getMedian())

	for i := k; i < len(nums); i++ {
		addNum(nums[i])
		removeNum(nums[i-k])
		res = append(res, getMedian())
	}
	return res
}
```

## Ruby

```ruby
def median_sliding_window(nums, k)
  low = []   # max-heap (store negatives)
  high = []  # min-heap
  delayed = Hash.new(0)
  low_size = 0
  high_size = 0

  heap_push = lambda do |heap, val|
    heap << val
    i = heap.size - 1
    while i > 0
      p = (i - 1) / 2
      break if heap[p] <= heap[i]
      heap[p], heap[i] = heap[i], heap[p]
      i = p
    end
  end

  heap_pop = lambda do |heap|
    top = heap[0]
    last = heap.pop
    unless heap.empty?
      heap[0] = last
      i = 0
      n = heap.size
      loop do
        l = i * 2 + 1
        r = l + 1
        break if l >= n
        smallest = (r < n && heap[r] < heap[l]) ? r : l
        break if heap[i] <= heap[smallest]
        heap[i], heap[smallest] = heap[smallest], heap[i]
        i = smallest
      end
    end
    top
  end

  prune = lambda do |heap|
    loop do
      break if heap.empty?
      val = (heap.equal?(low) ? -heap[0] : heap[0])
      if delayed[val] && delayed[val] > 0
        delayed[val] -= 1
        heap_pop.call(heap)
      else
        break
      end
    end
  end

  balance = lambda do
    if low_size > high_size + 1
      val = -heap_pop.call(low)
      low_size -= 1
      heap_push.call(high, val)
      high_size += 1
      prune.call(low)
    elsif low_size < high_size
      val = heap_pop.call(high)
      high_size -= 1
      heap_push.call(low, -val)
      low_size += 1
      prune.call(high)
    end
  end

  add_num = lambda do |num|
    if low.empty? || num <= -low[0]
      heap_push.call(low, -num)
      low_size += 1
    else
      heap_push.call(high, num)
      high_size += 1
    end
    balance.call
  end

  remove_num = lambda do |num|
    delayed[num] += 1
    if !low.empty? && num <= -low[0]
      low_size -= 1
      prune.call(low) if num == -low[0]
    else
      high_size -= 1
      prune.call(high) if !high.empty? && num == high[0]
    end
    balance.call
  end

  result = []
  nums.each_with_index do |num, i|
    add_num.call(num)
    if i >= k - 1
      median = if k.odd?
                 -low[0].to_f
               else
                 ((-low[0]) + high[0]) / 2.0
               end
      result << median
      remove_num.call(nums[i - k + 1])
    end
  end
  result
end
```

## Scala

```scala
import scala.collection.mutable

object Solution {
  def medianSlidingWindow(nums: Array[Int], k: Int): Array[Double] = {
    val low = mutable.PriorityQueue.empty[Int](Ordering.Int)          // max-heap
    val high = mutable.PriorityQueue.empty[Int](Ordering.Int.reverse) // min-heap
    val delayed = mutable.Map.empty[Int, Int]

    var sizeLow = 0
    var sizeHigh = 0

    def prune(heap: mutable.PriorityQueue[Int]): Unit = {
      while (heap.nonEmpty) {
        val num = heap.head
        delayed.get(num) match {
          case Some(cnt) if cnt > 0 =>
            heap.dequeue()
            if (cnt == 1) delayed -= num else delayed.update(num, cnt - 1)
          case _ => return
        }
      }
    }

    def balance(): Unit = {
      // ensure sizeLow >= sizeHigh and sizeLow <= sizeHigh + 1
      if (sizeLow > sizeHigh + 1) {
        val moved = low.dequeue()
        sizeLow -= 1
        high.enqueue(moved)
        sizeHigh += 1
        prune(low)
      } else if (sizeLow < sizeHigh) {
        val moved = high.dequeue()
        sizeHigh -= 1
        low.enqueue(moved)
        sizeLow += 1
        prune(high)
      }
    }

    def addNum(num: Int): Unit = {
      if (low.isEmpty || num <= low.head) {
        low.enqueue(num)
        sizeLow += 1
      } else {
        high.enqueue(num)
        sizeHigh += 1
      }
      balance()
    }

    def removeNum(num: Int): Unit = {
      delayed.update(num, delayed.getOrElse(num, 0) + 1)
      if (num <= low.head) {
        sizeLow -= 1
        if (num == low.head) prune(low)
      } else {
        sizeHigh -= 1
        if (high.nonEmpty && num == high.head) prune(high)
      }
      balance()
    }

    def getMedian(): Double = {
      if (k % 2 == 1) low.head.toDouble
      else (low.head.toLong + high.head.toLong).toDouble / 2.0
    }

    val n = nums.length
    val result = new Array[Double](n - k + 1)

    // initialize first window
    for (i <- 0 until k) addNum(nums(i))
    result(0) = getMedian()

    var idx = 1
    while (idx <= n - k) {
      removeNum(nums(idx - 1))
      addNum(nums(idx + k - 1))
      result(idx) = getMedian()
      idx += 1
    }

    result
  }
}
```

## Rust

```rust
use std::collections::{BinaryHeap, HashMap};
use std::cmp::Reverse;

impl Solution {
    pub fn median_sliding_window(nums: Vec<i32>, k: i32) -> Vec<f64> {
        let n = nums.len();
        if n == 0 || k == 0 {
            return vec![];
        }
        let k_usize = k as usize;
        let mut lower: BinaryHeap<i32> = BinaryHeap::new(); // max-heap
        let mut upper: BinaryHeap<Reverse<i32>> = BinaryHeap::new(); // min-heap
        let mut delayed: HashMap<i32, i32> = HashMap::new();
        let mut lower_size: usize = 0;
        let mut upper_size: usize = 0;

        fn prune_lower(heap: &mut BinaryHeap<i32>, delayed: &mut HashMap<i32, i32>) {
            while let Some(&top) = heap.peek() {
                if let Some(cnt) = delayed.get(&top) {
                    if *cnt > 0 {
                        let entry = delayed.get_mut(&top).unwrap();
                        *entry -= 1;
                        if *entry == 0 {
                            delayed.remove(&top);
                        }
                        heap.pop();
                        continue;
                    }
                }
                break;
            }
        }

        fn prune_upper(heap: &mut BinaryHeap<Reverse<i32>>, delayed: &mut HashMap<i32, i32>) {
            while let Some(&Reverse(top)) = heap.peek() {
                if let Some(cnt) = delayed.get(&top) {
                    if *cnt > 0 {
                        let entry = delayed.get_mut(&top).unwrap();
                        *entry -= 1;
                        if *entry == 0 {
                            delayed.remove(&top);
                        }
                        heap.pop();
                        continue;
                    }
                }
                break;
            }
        }

        fn balance(
            lower: &mut BinaryHeap<i32>,
            upper: &mut BinaryHeap<Reverse<i32>>,
            delayed: &mut HashMap<i32, i32>,
            lower_size: &mut usize,
            upper_size: &mut usize,
        ) {
            // Ensure lower has at most one more element than upper
            if *lower_size > *upper_size + 1 {
                // move top from lower to upper
                let val = lower.pop().unwrap();
                *lower_size -= 1;
                upper.push(Reverse(val));
                *upper_size += 1;
                prune_lower(lower, delayed);
            } else if *lower_size < *upper_size {
                // move top from upper to lower
                let Reverse(val) = upper.pop().unwrap();
                *upper_size -= 1;
                lower.push(val);
                *lower_size += 1;
                prune_upper(upper, delayed);
            }
        }

        fn add_num(
            num: i32,
            lower: &mut BinaryHeap<i32>,
            upper: &mut BinaryHeap<Reverse<i32>>,
            delayed: &mut HashMap<i32, i32>,
            lower_size: &mut usize,
            upper_size: &mut usize,
        ) {
            if lower.peek().map_or(true, |&top| num <= top) {
                lower.push(num);
                *lower_size += 1;
            } else {
                upper.push(Reverse(num));
                *upper_size += 1;
            }
            balance(lower, upper, delayed, lower_size, upper_size);
        }

        fn remove_num(
            num: i32,
            lower: &mut BinaryHeap<i32>,
            upper: &mut BinaryHeap<Reverse<i32>>,
            delayed: &mut HashMap<i32, i32>,
            lower_size: &mut usize,
            upper_size: &mut usize,
        ) {
            *delayed.entry(num).or_insert(0) += 1;
            if let Some(&top) = lower.peek() {
                if num <= top {
                    *lower_size -= 1;
                    if num == top {
                        prune_lower(lower, delayed);
                    }
                } else {
                    *upper_size -= 1;
                    if let Some(&Reverse(top_up)) = upper.peek() {
                        if num == top_up {
                            prune_upper(upper, delayed);
                        }
                    }
                }
            } else {
                // lower empty shouldn't happen in normal flow
                *upper_size -= 1;
            }
            balance(lower, upper, delayed, lower_size, upper_size);
        }

        let mut result: Vec<f64> = Vec::with_capacity(n - k_usize + 1);

        for i in 0..n {
            add_num(
                nums[i],
                &mut lower,
                &mut upper,
                &mut delayed,
                &mut lower_size,
                &mut upper_size,
            );

            if i + 1 >= k_usize {
                // compute median
                let median = if k % 2 == 1 {
                    *lower.peek().unwrap() as f64
                } else {
                    let a = *lower.peek().unwrap() as f64;
                    let b = match upper.peek() {
                        Some(&Reverse(v)) => v as f64,
                        None => 0.0,
                    };
                    (a + b) / 2.0
                };
                result.push(median);

                // remove the element sliding out
                let out_num = nums[i + 1 - k_usize];
                remove_num(
                    out_num,
                    &mut lower,
                    &mut upper,
                    &mut delayed,
                    &mut lower_size,
                    &mut upper_size,
                );
            }
        }

        result
    }
}
```

## Racket

```racket
(require racket/heap)

(define (median-sliding-window nums k)
  (-> (listof exact-integer?) exact-integer? (listof flonum?))
  (let* ([lo (make-heap >)]               ; max‑heap for lower half
         [hi (make-heap <)]               ; min‑heap for upper half
         [del-lo (make-hash)]             ; delayed deletions from lo
         [del-hi (make-hash)]             ; delayed deletions from hi
         [lo-size 0]                      ; number of valid elems in lo
         [hi-size 0]                      ; number of valid elems in hi
         
         ;; prune invalid tops from a heap using its delayed map
         (define (prune! heap del)
           (let loop ()
             (when (and (not (heap-empty? heap))
                        (> (hash-ref del (heap-peek heap) 0) 0))
               (let* ([top (heap-pop! heap)]
                      [cnt (hash-ref del top)])
                 (if (= cnt 1)
                     (hash-remove! del top)
                     (hash-set! del top (- cnt 1))))
               (loop))))
         
         ;; rebalance so that lo has either same size as hi or one more
         (define (rebalance!)
           (cond
             [(> lo-size (+ hi-size 1))
              (let ([v (heap-pop! lo)])
                (set! lo-size (- lo-size 1))
                (heap-insert! hi v)
                (set! hi-size (+ hi-size 1))
                (prune! lo del-lo)
                (rebalance!))]
             [(< lo-size hi-size)
              (let ([v (heap-pop! hi)])
                (set! hi-size (- hi-size 1))
                (heap-insert! lo v)
                (set! lo-size (+ lo-size 1))
                (prune! hi del-hi)
                (rebalance!))]
             [else (void)])))
         
         ;; insert a new number
         (define (add-num x)
           (if (or (heap-empty? lo) (<= x (heap-peek lo)))
               (begin (heap-insert! lo x) (set! lo-size (+ lo-size 1)))
               (begin (heap-insert! hi x) (set! hi-size (+ hi-size 1)))))
         
         ;; schedule removal of a number leaving the window
         (define (remove-num x)
           (if (or (heap-empty? lo) (<= x (heap-peek lo)))
               (begin
                 (hash-set! del-lo x (+ (hash-ref del-lo x 0) 1))
                 (set! lo-size (- lo-size 1)))
               (begin
                 (hash-set! del-hi x (+ (hash-ref del-hi x 0) 1))
                 (set! hi-size (- hi-size 1)))))
         
         ;; compute current median as flonum
         (define (current-median)
           (if (odd? k)
               (exact->inexact (heap-peek lo))
               (/ (+ (exact->inexact (heap-peek lo))
                     (exact->inexact (heap-peek hi))) 2.0)))
         
         ;; result list accumulator
         (result '()))
    
    (for ([i (in-range (length nums))])
      (let ([x (list-ref nums i)])
        (add-num x)
        (when (>= i k)
          (remove-num (list-ref nums (- i k))))
        (prune! lo del-lo)
        (prune! hi del-hi)
        (rebalance!)
        (when (>= i (- k 1))
          (set! result (cons (current-median) result)))))
    
    (reverse result)))
```

## Erlang

```erlang
-module(solution).
-export([median_sliding_window/2]).

-spec median_sliding_window(Nums :: [integer()], K :: integer()) -> [float()].
median_sliding_window(Nums, K) ->
    FirstK = lists:sublist(Nums, K),
    Rest = lists:nthtail(K, Nums),
    {Low0, High0, SizeL0, SizeH0} = init_window(FirstK, gb_trees:empty(), gb_trees:empty(), 0, 0),
    {Low1, High1, SizeL1, SizeH1} = rebalance(Low0, High0, SizeL0, SizeH0),
    Med0 = median(K, Low1, High1),
    Queue0 = {FirstK, []},
    Acc0 = [Med0],
    ResultRev = slide(Rest, Queue0, Low1, High1, SizeL1, SizeH1, Acc0, K),
    lists:reverse(ResultRev).

%% Initialize the first window
init_window([], Low, High, SizeL, SizeH) ->
    {Low, High, SizeL, SizeH};
init_window([X|Xs], Low, High, SizeL, SizeH) ->
    {Low1, High1, SizeL1, SizeH1} = insert(X, Low, High, SizeL, SizeH),
    init_window(Xs, Low1, High1, SizeL1, SizeH1).

%% Insert a number into appropriate heap
insert(Num, Low, High, SizeL, SizeH) ->
    case gb_trees:is_empty(Low) of
        true ->
            {add_one(Low, Num), High, SizeL + 1, SizeH};
        false ->
            {MaxLow,_} = gb_trees:largest(Low),
            if Num =< MaxLow ->
                    {add_one(Low, Num), High, SizeL + 1, SizeH};
               true ->
                    {Low, add_one(High, Num), SizeL, SizeH + 1}
            end
    end.

%% Remove a number from appropriate heap
remove(Num, Low, High, SizeL, SizeH) ->
    case gb_trees:is_empty(Low) of
        true ->
            {Low, High, SizeL, SizeH};
        false ->
            {MaxLow,_} = gb_trees:largest(Low),
            if Num =< MaxLow ->
                    {remove_one(Low, Num), High, SizeL - 1, SizeH};
               true ->
                    {Low, remove_one(High, Num), SizeL, SizeH - 1}
            end
    end.

%% Rebalance the two heaps to maintain size properties
rebalance(Low, High, SizeL, SizeH) ->
    Diff = SizeL - SizeH,
    if Diff > 1 ->
            {Key,_} = gb_trees:largest(Low),
            Low1 = remove_one(Low, Key),
            High1 = add_one(High, Key),
            rebalance(Low1, High1, SizeL - 1, SizeH + 1);
       Diff < 0 ->
            {Key,_} = gb_trees:smallest(High),
            High1 = remove_one(High, Key),
            Low1 = add_one(Low, Key),
            rebalance(Low1, High1, SizeL + 1, SizeH - 1);
       true ->
            {Low, High, SizeL, SizeH}
    end.

%% Compute median from the two heaps
median(K, Low, _High) when K rem 2 =:= 1 ->
    {MaxLow,_} = gb_trees:largest(Low),
    float(MaxLow);
median(_K, Low, High) ->
    {MaxLow,_} = gb_trees:largest(Low),
    {MinHigh,_} = gb_trees:smallest(High),
    (float(MaxLow) + float(MinHigh)) / 2.0.

%% Slide the window across remaining elements
slide([], _Queue, _Low, _High, _SizeL, _SizeH, Acc, _K) ->
    Acc;
slide([In|Rest], Queue, Low, High, SizeL, SizeH, Acc, K) ->
    {Out, Q1} = pop_queue(Queue),
    {Low1, High1, SizeL1, SizeH1} = remove(Out, Low, High, SizeL, SizeH),
    {Low2, High2, SizeL2, SizeH2} = insert(In, Low1, High1, SizeL1, SizeH1),
    {Low3, High3, SizeL3, SizeH3} = rebalance(Low2, High2, SizeL2, SizeH2),
    Med = median(K, Low3, High3),
    Q2 = push(In, Q1),
    slide(Rest, Q2, Low3, High3, SizeL3, SizeH3, [Med|Acc], K).

%% Queue operations (functional queue with two lists)
push(In, {F,B}) -> {F, [In|B]}.

pop_queue({[H|T], B}) ->
    {H, {T, B}};
pop_queue({[], B}) when B =/= [] ->
    NewFront = lists:reverse(B),
    pop_queue({NewFront, []});
pop_queue({[], []}) ->
    erlang:error(empty_queue).

%% Helper to add one occurrence in gb_tree
add_one(Tree, Key) ->
    case gb_trees:lookup(Key, Tree) of
        {value, Count} -> gb_trees:update(Key, Count + 1, Tree);
        none -> gb_trees:insert(Key, 1, Tree)
    end.

%% Helper to remove one occurrence in gb_tree
remove_one(Tree, Key) ->
    case gb_trees:lookup(Key, Tree) of
        {value, Count} when Count > 1 -> gb_trees:update(Key, Count - 1, Tree);
        {value, 1} -> gb_trees:delete(Key, Tree);
        none -> Tree
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec median_sliding_window(nums :: [integer], k :: integer) :: [float]
  def median_sliding_window(nums, k) do
    arr = :array.from_list(nums)
    n = length(nums)

    {result_rev, _left, _right, _lsz, _rsz} =
      Enum.reduce(0..(n - 1), {[], :gb_trees.empty(), :gb_trees.empty(), 0, 0}, fn i,
                                                                               {res_rev, left, right,
                                                                                lsz, rsz} ->
        val = :array.get(i, arr)

        # insert new value
        {left, right, lsz, rsz} =
          if lsz == 0 do
            {insert(left, val), right, lsz + 1, rsz}
          else
            max_left = max_key(left)

            if val <= max_left do
              {insert(left, val), right, lsz + 1, rsz}
            else
              {left, insert(right, val), lsz, rsz + 1}
            end
          end

        # rebalance after insertion
        {left, right, lsz, rsz} = rebalance(left, right, lsz, rsz)

        if i >= k - 1 do
          median =
            if rem(k, 2) == 1 do
              max_key(left) * 1.0
            else
              (max_key(left) + min_key(right)) / 2.0
            end

          res_rev = [median | res_rev]

          out = :array.get(i - k + 1, arr)

          # remove outgoing value
          {left, right, lsz, rsz} =
            if out <= max_key(left) do
              {delete(left, out), right, lsz - 1, rsz}
            else
              {left, delete(right, out), lsz, rsz - 1}
            end

          # rebalance after removal
          {left, right, lsz, rsz} = rebalance(left, right, lsz, rsz)

          {res_rev, left, right, lsz, rsz}
        else
          {res_rev, left, right, lsz, rsz}
        end
      end)

    Enum.reverse(result_rev)
  end

  # Helper functions for multiset using :gb_trees

  defp insert(tree, val) do
    case :gb_trees.lookup(val, tree) do
      {:value, cnt} -> :gb_trees.update(val, cnt + 1, tree)
      :none -> :gb_trees.insert(val, 1, tree)
    end
  end

  defp delete(tree, val) do
    case :gb_trees.lookup(val, tree) do
      {:value, 1} -> :gb_trees.delete(val, tree)
      {:value, cnt} -> :gb_trees.update(val, cnt - 1, tree)
      :none -> tree
    end
  end

  defp max_key(tree) do
    {key, _cnt} = :gb_trees.max(tree)
    key
  end

  defp min_key(tree) do
    {key, _cnt} = :gb_trees.smallest(tree)
    key
  end

  defp rebalance(left, right, lsz, rsz) do
    cond do
      lsz > rsz + 1 ->
        max_val = max_key(left)
        left = delete(left, max_val)
        right = insert(right, max_val)
        rebalance(left, right, lsz - 1, rsz + 1)

      lsz < rsz ->
        min_val = min_key(right)
        right = delete(right, min_val)
        left = insert(left, min_val)
        rebalance(left, right, lsz + 1, rsz - 1)

      true ->
        {left, right, lsz, rsz}
    end
  end
end
```
