# 3266. Final Array State After K Multiplication Operations II

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    static const int MOD = 1000000007;
    
    long long modPow(long long a, long long e) {
        long long res = 1 % MOD;
        a %= MOD;
        while (e > 0) {
            if (e & 1) res = (res * a) % MOD;
            a = (a * a) % MOD;
            e >>= 1;
        }
        return res;
    }
    
    vector<int> getFinalState(vector<int>& nums, int k, int multiplier) {
        int n = nums.size();
        if (multiplier == 1 || k == 0) {
            vector<int> ans(n);
            for (int i = 0; i < n; ++i) ans[i] = ((long long)nums[i]) % MOD;
            return ans;
        }
        
        vector<long long> curVals(nums.begin(), nums.end());
        vector<long long> cnt(n, 0);
        using P = pair<long long,int>;
        priority_queue<P, vector<P>, greater<P>> pq;
        long long maxVal = *max_element(curVals.begin(), curVals.end());
        for (int i = 0; i < n; ++i) pq.emplace(curVals[i], i);
        
        while (k > 0) {
            auto [val, idx] = pq.top(); pq.pop();
            __int128 prod = (__int128)val * multiplier;
            if (prod > maxVal) {
                // condition met, stop simulation
                pq.emplace(val, idx); // put back
                break;
            }
            long long newVal = (long long)prod; // safe within 64-bit for our constraints
            curVals[idx] = newVal;
            ++cnt[idx];
            --k;
            if (newVal > maxVal) maxVal = newVal;
            pq.emplace(newVal, idx);
        }
        
        if (k > 0) {
            vector<int> order(n);
            iota(order.begin(), order.end(), 0);
            sort(order.begin(), order.end(), [&](int a, int b){
                if (curVals[a] != curVals[b]) return curVals[a] < curVals[b];
                return a < b;
            });
            long long full = k / n;
            int rem = k % n;
            for (int idx : order) {
                cnt[idx] += full;
                if (rem > 0) {
                    ++cnt[idx];
                    --rem;
                }
            }
        }
        
        vector<int> res(n);
        for (int i = 0; i < n; ++i) {
            long long multPow = modPow(multiplier, cnt[i]);
            long long valMod = ((long long)nums[i] % MOD) * multPow % MOD;
            res[i] = (int)valMod;
        }
        return res;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static final int MOD = 1_000_000_007;

    private static class Node {
        long val;
        int idx;
        Node(long v, int i) { val = v; idx = i; }
    }

    public int[] getFinalState(int[] nums, int k, int multiplier) {
        int n = nums.length;
        long[] cnt = new long[n];
        PriorityQueue<Node> pq = new PriorityQueue<>(Comparator.comparingLong(a -> a.val));
        long maxVal = Long.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            long v = nums[i];
            pq.offer(new Node(v, i));
            if (v > maxVal) maxVal = v;
        }

        long ops = k;
        while (ops > 0) {
            Node minNode = pq.peek();
            // check condition: min * multiplier > max
            if (minNode.val > maxVal / multiplier) break;

            // perform operation
            pq.poll();
            cnt[minNode.idx]++;                     // one multiplication performed
            long newVal = minNode.val * multiplier; // safe from overflow as per analysis
            if (newVal > maxVal) maxVal = newVal;
            pq.offer(new Node(newVal, minNode.idx));
            ops--;
        }

        if (ops > 0) {
            long addAll = ops / n;
            int extra = (int)(ops % n);
            for (int i = 0; i < n; i++) cnt[i] += addAll;

            // give one more multiplication to the smallest 'extra' elements
            for (int i = 0; i < extra; i++) {
                Node nd = pq.poll();
                cnt[nd.idx]++;
                // no need to push back since we are done with distribution
            }
        }

        int[] res = new int[n];
        long multMod = multiplier % MOD;
        for (int i = 0; i < n; i++) {
            long base = nums[i] % MOD;
            long pow = modPow(multMod, cnt[i], MOD);
            res[i] = (int)((base * pow) % MOD);
        }
        return res;
    }

    private long modPow(long a, long e, int mod) {
        long result = 1L;
        long base = a % mod;
        while (e > 0) {
            if ((e & 1L) == 1L) result = (result * base) % mod;
            base = (base * base) % mod;
            e >>= 1;
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        n = len(nums)
        if k == 0 or multiplier == 1:
            return [x % MOD for x in nums]

        import heapq
        heap = [(nums[i], i) for i in range(n)]
        heapq.heapify(heap)
        cur_max = max(nums)

        while k > 0:
            v, idx = heap[0]  # peek smallest
            if v * multiplier > cur_max:
                break
            heapq.heappop(heap)
            new_v = v * multiplier
            k -= 1
            heapq.heappush(heap, (new_v, idx))
            if new_v > cur_max:
                cur_max = new_v

        # Distribute remaining operations in batch
        elems = [heapq.heappop(heap) for _ in range(n)]
        elems.sort(key=lambda x: (x[0], x[1]))  # sort by value then index

        base = k // n
        rem = k % n

        res = [0] * n
        pow_base = pow(multiplier, base, MOD) if base else 1

        for pos, (val, orig_idx) in enumerate(elems):
            times = base + (1 if pos < rem else 0)
            if times == 0:
                final_val = val % MOD
            else:
                final_val = (val % MOD) * pow(multiplier, times, MOD) % MOD
            res[orig_idx] = final_val

        return res
```

## Python3

```python
import heapq
from typing import List

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        MOD = 10**9 + 7
        n = len(nums)
        if multiplier == 1 or k == 0:
            return [x % MOD for x in nums]

        heap = [(val, idx) for idx, val in enumerate(nums)]
        heapq.heapify(heap)
        max_val = max(nums)

        # Simulate until condition holds or k exhausted
        while k > 0:
            min_val, _ = heap[0]
            if min_val * multiplier > max_val:
                break
            min_val, idx = heapq.heappop(heap)
            new_val = min_val * multiplier
            heapq.heappush(heap, (new_val, idx))
            k -= 1
            if new_val > max_val:
                max_val = new_val

        if k == 0:
            res = [0] * n
            for val, idx in heap:
                res[idx] = val % MOD
            return res

        # Distribute remaining operations greedily
        sorted_items = sorted(heap, key=lambda x: x[0])  # ascending by current value
        full_cycles = k // n
        remainder = k % n
        mult_full = pow(multiplier, full_cycles, MOD)

        res = [0] * n
        for pos, (val, idx) in enumerate(sorted_items):
            val_mod = (val % MOD) * mult_full % MOD
            if pos < remainder:
                val_mod = val_mod * multiplier % MOD
            res[idx] = val_mod

        return res
```

## C

```c
#include <stdlib.h>
#include <math.h>
#include <stdint.h>

typedef struct {
    unsigned long long val;
    int idx;
} SimNode;

typedef struct {
    SimNode *data;
    int size;
    int capacity;
} MinHeapSim;

static void simSwap(SimNode *a, SimNode *b) {
    SimNode t = *a; *a = *b; *b = t;
}
static void simPush(MinHeapSim *h, SimNode node) {
    int i = ++h->size;
    h->data[i] = node;
    while (i > 1 && h->data[i].val < h->data[i/2].val) {
        simSwap(&h->data[i], &h->data[i/2]);
        i >>= 1;
    }
}
static SimNode simTop(MinHeapSim *h) { return h->data[1]; }
static void simPop(MinHeapSim *h) {
    h->data[1] = h->data[h->size--];
    int i = 1;
    while (1) {
        int l = i<<1, r = l|1, s = i;
        if (l <= h->size && h->data[l].val < h->data[s].val) s = l;
        if (r <= h->size && h->data[r].val < h->data[s].val) s = r;
        if (s == i) break;
        simSwap(&h->data[i], &h->data[s]);
        i = s;
    }
}

/* Log heap for remaining remainder operations */
typedef struct {
    double key;
    int idx;
} LogNode;

typedef struct {
    LogNode *data;
    int size;
    int capacity;
} MinHeapLog;

static void logSwap(LogNode *a, LogNode *b) {
    LogNode t = *a; *a = *b; *b = t;
}
static void logPush(MinHeapLog *h, LogNode node) {
    int i = ++h->size;
    h->data[i] = node;
    while (i > 1 && h->data[i].key < h->data[i/2].key) {
        logSwap(&h->data[i], &h->data[i/2]);
        i >>= 1;
    }
}
static LogNode logTop(MinHeapLog *h) { return h->data[1]; }
static void logPop(MinHeapLog *h) {
    h->data[1] = h->data[h->size--];
    int i = 1;
    while (1) {
        int l = i<<1, r = l|1, s = i;
        if (l <= h->size && h->data[l].key < h->data[s].key) s = l;
        if (r <= h->size && h->data[r].key < h->data[s].key) s = r;
        if (s == i) break;
        logSwap(&h->data[i], &h->data[s]);
        i = s;
    }
}

/* modular exponentiation */
static long long modPow(long long base, long long exp, long long MOD) {
    long long res = 1 % MOD;
    base %= MOD;
    while (exp) {
        if (exp & 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return res;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getFinalState(int* nums, int numsSize, int k, int multiplier, int* returnSize) {
    const long long MOD = 1000000007LL;
    *returnSize = numsSize;
    int *result = (int*)malloc(sizeof(int) * numsSize);
    if (multiplier == 1) {
        for (int i = 0; i < numsSize; ++i)
            result[i] = ((long long)nums[i]) % MOD;
        return result;
    }

    long long *cnt = (long long*)calloc(numsSize, sizeof(long long));

    /* Simulation phase */
    MinHeapSim simHeap;
    simHeap.size = 0;
    simHeap.capacity = numsSize + 5;
    simHeap.data = (SimNode*)malloc(sizeof(SimNode) * simHeap.capacity);
    unsigned long long maxVal = 0;
    for (int i = 0; i < numsSize; ++i) {
        SimNode nd = { (unsigned long long)nums[i], i };
        simPush(&simHeap, nd);
        if (nd.val > maxVal) maxVal = nd.val;
    }

    long long remainingK = k;
    while (remainingK > 0) {
        SimNode cur = simTop(&simHeap);
        __uint128_t prod = (__uint128_t)cur.val * (unsigned long long)multiplier;
        if (prod > maxVal) break;               /* enter cycle phase */
        simPop(&simHeap);
        unsigned long long newVal = (unsigned long long)prod;
        cnt[cur.idx] += 1;
        SimNode nd = { newVal, cur.idx };
        simPush(&simHeap, nd);
        if (newVal > maxVal) maxVal = newVal;
        --remainingK;
    }

    /* Cycle phase */
    long long fullCycles = remainingK / numsSize;
    int rem = (int)(remainingK % numsSize);
    for (int i = 0; i < numsSize; ++i) cnt[i] += fullCycles;

    double logM = log((double)multiplier);
    MinHeapLog logHeap;
    logHeap.size = 0;
    logHeap.capacity = numsSize + 5;
    logHeap.data = (LogNode*)malloc(sizeof(LogNode) * logHeap.capacity);
    for (int i = 0; i < numsSize; ++i) {
        double key = log((double)nums[i]) + cnt[i] * logM;
        LogNode nd = { key, i };
        logPush(&logHeap, nd);
    }

    while (rem-- > 0) {
        LogNode cur = logTop(&logHeap);
        logPop(&logHeap);
        cnt[cur.idx] += 1;
        cur.key += logM;
        logPush(&logHeap, cur);
    }

    /* Build final result */
    for (int i = 0; i < numsSize; ++i) {
        long long mult = modPow(multiplier, cnt[i], MOD);
        long long val = ((long long)nums[i] % MOD) * mult % MOD;
        result[i] = (int)val;
    }

    free(cnt);
    free(simHeap.data);
    free(logHeap.data);
    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private const long MOD = 1000000007L;

    public int[] GetFinalState(int[] nums, int k, int multiplier) {
        int n = nums.Length;
        long[] vals = new long[n];
        for (int i = 0; i < n; i++) vals[i] = nums[i];

        var set = new SortedSet<Node>(new NodeComparer());
        long maxVal = long.MinValue;
        for (int i = 0; i < n; i++) {
            set.Add(new Node(vals[i], i));
            if (vals[i] > maxVal) maxVal = vals[i];
        }

        while (k > 0) {
            var minNode = set.Min;
            // check condition: min * multiplier > max
            // use checked multiplication with overflow guard
            bool willOverflow = minNode.val > long.MaxValue / multiplier;
            long prod = willOverflow ? long.MaxValue : minNode.val * (long)multiplier;
            if (!willOverflow && prod <= maxVal) {
                // perform operation
                set.Remove(minNode);
                vals[minNode.idx] = prod;
                set.Add(new Node(prod, minNode.idx));
                if (prod > maxVal) maxVal = prod;
                k--;
            } else {
                break; // enter cycle mode
            }
        }

        if (k == 0) {
            int[] ans = new int[n];
            for (int i = 0; i < n; i++) ans[i] = (int)(vals[i] % MOD);
            return ans;
        }

        // Cycle mode
        int startIdx = set.Min.idx; // index of current minimum
        long cycles = k / n;
        int extra = (int)(k % n);

        long powCycle = ModPow(multiplier, cycles);
        for (int i = 0; i < n; i++) {
            long cur = vals[i] % MOD;
            if (cycles > 0) cur = (cur * powCycle) % MOD;

            int offset = (i - startIdx + n) % n;
            if (offset < extra) {
                cur = (cur * multiplier) % MOD;
            }
            vals[i] = cur;
        }

        int[] result = new int[n];
        for (int i = 0; i < n; i++) result[i] = (int)(vals[i] % MOD);
        return result;
    }

    private long ModPow(long baseVal, long exp) {
        long res = 1L;
        long b = baseVal % MOD;
        while (exp > 0) {
            if ((exp & 1L) == 1L) res = (res * b) % MOD;
            b = (b * b) % MOD;
            exp >>= 1;
        }
        return res;
    }

    private class Node {
        public long val;
        public int idx;
        public Node(long v, int i) { val = v; idx = i; }
    }

    private class NodeComparer : IComparer<Node> {
        public int Compare(Node a, Node b) {
            if (a.val != b.val) return a.val < b.val ? -1 : 1;
            return a.idx.CompareTo(b.idx);
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number} multiplier
 * @return {number[]}
 */
var getFinalState = function(nums, k, multiplier) {
    const MOD = 1000000007n;
    if (multiplier === 1) {
        return nums.map(v => v % Number(MOD));
    }
    const n = nums.length;
    const multBig = BigInt(multiplier);
    
    // Min-heap implementation
    class MinHeap {
        constructor() { this.heap = []; }
        size() { return this.heap.length; }
        peek() { return this.heap[0]; }
        push(node) {
            const h = this.heap;
            h.push(node);
            let i = h.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (h[p].val <= h[i].val) break;
                [h[p], h[i]] = [h[i], h[p]];
                i = p;
            }
        }
        pop() {
            const h = this.heap;
            if (h.length === 0) return undefined;
            const top = h[0];
            const last = h.pop();
            if (h.length > 0) {
                h[0] = last;
                let i = 0;
                while (true) {
                    let l = i * 2 + 1, r = l + 1, smallest = i;
                    if (l < h.length && h[l].val < h[smallest].val) smallest = l;
                    if (r < h.length && h[r].val < h[smallest].val) smallest = r;
                    if (smallest === i) break;
                    [h[i], h[smallest]] = [h[smallest], h[i]];
                    i = smallest;
                }
            }
            return top;
        }
    }
    
    const heap = new MinHeap();
    let maxVal = 0n;
    for (let i = 0; i < n; ++i) {
        const v = BigInt(nums[i]);
        heap.push({val: v, idx: i});
        if (v > maxVal) maxVal = v;
    }
    
    // simulate until condition or k exhausted
    while (k > 0) {
        const node = heap.peek();
        const potential = node.val * multBig;
        if (potential > maxVal) break; // start of cycle
        heap.pop();
        const newVal = potential;
        if (newVal > maxVal) maxVal = newVal;
        heap.push({val: newVal, idx: node.idx});
        k--;
    }
    
    const result = new Array(n);
    
    if (k === 0) {
        while (heap.size()) {
            const node = heap.pop();
            result[node.idx] = Number(node.val % MOD);
        }
        return result;
    }
    
    // collect remaining nodes
    const nodes = [];
    while (heap.size()) {
        nodes.push(heap.pop());
    }
    nodes.sort((a, b) => (a.val < b.val ? -1 : a.val > b.val ? 1 : 0));
    
    const len = nodes.length;
    const base = Math.floor(k / len);
    const rem = k % len;
    
    // fast power modulo
    function powMod(baseBig, exp) {
        let result = 1n;
        let b = baseBig % MOD;
        let e = BigInt(exp);
        while (e > 0n) {
            if (e & 1n) result = (result * b) % MOD;
            b = (b * b) % MOD;
            e >>= 1n;
        }
        return result;
    }
    
    const powBase = powMod(multBig, base);
    const multPlusOne = (powBase * multBig) % MOD; // multiplier^(base+1)
    
    for (let i = 0; i < len; ++i) {
        const node = nodes[i];
        const valMod = node.val % MOD;
        const finalPow = i < rem ? multPlusOne : powBase;
        result[node.idx] = Number((valMod * finalPow) % MOD);
    }
    
    return result;
};
```

## Typescript

```typescript
function getFinalState(nums: number[], k: number, multiplier: number): number[] {
    const MOD = 1000000007n;
    if (multiplier === 1) {
        return nums.map(v => Number(BigInt(v) % MOD));
    }
    const n = nums.length;
    const multBig = BigInt(multiplier);
    const values: bigint[] = nums.map(v => BigInt(v));
    const exp = new Array<number>(n).fill(0);

    class MinHeap {
        data: { val: bigint; idx: number }[] = [];
        size(): number { return this.data.length; }
        peek() { return this.data[0]; }
        push(item: { val: bigint; idx: number }) {
            const a = this.data;
            a.push(item);
            let i = a.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (this.less(a[i], a[p])) {
                    [a[i], a[p]] = [a[p], a[i]];
                    i = p;
                } else break;
            }
        }
        pop(): { val: bigint; idx: number } | undefined {
            const a = this.data;
            if (a.length === 0) return undefined;
            const top = a[0];
            const last = a.pop()!;
            if (a.length > 0) {
                a[0] = last;
                this.heapify(0);
            }
            return top;
        }
        private heapify(i: number) {
            const a = this.data;
            const n = a.length;
            while (true) {
                let smallest = i;
                const l = i * 2 + 1;
                const r = i * 2 + 2;
                if (l < n && this.less(a[l], a[smallest])) smallest = l;
                if (r < n && this.less(a[r], a[smallest])) smallest = r;
                if (smallest !== i) {
                    [a[i], a[smallest]] = [a[smallest], a[i]];
                    i = smallest;
                } else break;
            }
        }
        private less(a: { val: bigint; idx: number }, b: { val: bigint; idx: number }): boolean {
            if (a.val < b.val) return true;
            if (a.val > b.val) return false;
            return a.idx < b.idx;
        }
    }

    const heap = new MinHeap();
    let currentMax = values[0];
    for (let i = 0; i < n; ++i) {
        heap.push({ val: values[i], idx: i });
        if (values[i] > currentMax) currentMax = values[i];
    }

    let remaining = k;
    while (remaining > 0) {
        const top = heap.peek()!;
        if (top.val * multBig > currentMax) break;
        heap.pop();
        const newVal = top.val * multBig;
        values[top.idx] = newVal;
        exp[top.idx] += 1;
        heap.push({ val: newVal, idx: top.idx });
        if (newVal > currentMax) currentMax = newVal;
        remaining--;
    }

    function modPow(base: bigint, exponent: bigint, mod: bigint): bigint {
        let result = 1n;
        let b = base % mod;
        let e = exponent;
        while (e > 0n) {
            if (e & 1n) result = (result * b) % mod;
            b = (b * b) % mod;
            e >>= 1n;
        }
        return result;
    }

    const res = new Array<number>(n);
    if (remaining === 0) {
        for (let i = 0; i < n; ++i) {
            const pow = modPow(multBig, BigInt(exp[i]), MOD);
            const valMod = (BigInt(nums[i]) % MOD) * pow % MOD;
            res[i] = Number(valMod);
        }
        return res;
    }

    // Extract and sort remaining items
    const items: { val: bigint; idx: number }[] = [];
    while (heap.size() > 0) {
        items.push(heap.pop()!);
    }
    items.sort((a, b) => {
        if (a.val < b.val) return -1;
        if (a.val > b.val) return 1;
        return a.idx - b.idx;
    });

    const cycles = Math.floor(remaining / n);
    const extra = remaining % n;

    for (let i = 0; i < n; ++i) {
        const idx = items[i].idx;
        const totalExp = exp[idx] + cycles + (i < extra ? 1 : 0);
        const pow = modPow(multBig, BigInt(totalExp), MOD);
        const valMod = (BigInt(nums[idx]) % MOD) * pow % MOD;
        res[idx] = Number(valMod);
    }
    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @param Integer $multiplier
     * @return Integer[]
     */
    function getFinalState($nums, $k, $multiplier) {
        $mod = 1000000007;
        $n = count($nums);

        // Simulate until the cycle condition is met or k runs out
        while ($k > 0) {
            $minVal = PHP_INT_MAX;
            $maxVal = 0;
            foreach ($nums as $v) {
                if ($v < $minVal) $minVal = $v;
                if ($v > $maxVal) $maxVal = $v;
            }
            // If min * multiplier > max, we are in the cycle region
            if ($minVal > intdiv($maxVal, $multiplier)) {
                break;
            }

            // Find index of a minimum element (first occurrence)
            foreach ($nums as $idx => $v) {
                if ($v == $minVal) {
                    $nums[$idx] = $v * $multiplier;
                    break;
                }
            }
            $k--;
        }

        if ($k == 0) {
            // Apply modulo and return
            foreach ($nums as &$v) {
                $v %= $mod;
            }
            unset($v);
            return $nums;
        }

        // Now we are in the cyclic phase
        $fullCycles = intdiv($k, $n);
        $remain = $k % $n;

        if ($fullCycles > 0) {
            $powCycle = $this->modPow($multiplier, $fullCycles, $mod);
            foreach ($nums as &$v) {
                $v = ($v % $mod) * $powCycle % $mod;
            }
            unset($v);
        }

        // Determine the smallest 'remain' elements based on actual values (before modulo)
        $indices = range(0, $n - 1);
        usort($indices, function($a, $b) use ($nums) {
            if ($nums[$a] == $nums[$b]) return 0;
            return ($nums[$a] < $nums[$b]) ? -1 : 1;
        });

        for ($i = 0; $i < $remain; $i++) {
            $idx = $indices[$i];
            $nums[$idx] = ($nums[$idx] % $mod) * $multiplier % $mod;
        }

        // Ensure all values are modulo'd
        foreach ($nums as &$v) {
            $v %= $mod;
        }
        unset($v);

        return $nums;
    }

    private function modPow($base, $exp, $mod) {
        $result = 1;
        $base %= $mod;
        while ($exp > 0) {
            if ($exp & 1) {
                $result = ($result * $base) % $mod;
            }
            $base = ($base * $base) % $mod;
            $exp >>= 1;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    private struct Node {
        var value: Int64
        var index: Int
    }
    
    private class MinHeap {
        private var heap: [Node] = []
        
        func peek() -> Node? {
            return heap.first
        }
        
        func push(_ node: Node) {
            heap.append(node)
            siftUp(heap.count - 1)
        }
        
        func pop() -> Node? {
            guard !heap.isEmpty else { return nil }
            let top = heap[0]
            let last = heap.removeLast()
            if !heap.isEmpty {
                heap[0] = last
                siftDown(0)
            }
            return top
        }
        
        func allElements() -> [Node] {
            return heap
        }
        
        private func siftUp(_ i: Int) {
            var child = i
            while child > 0 {
                let parent = (child - 1) >> 1
                if less(heap[child], heap[parent]) {
                    heap.swapAt(child, parent)
                    child = parent
                } else { break }
            }
        }
        
        private func siftDown(_ i: Int) {
            var parent = i
            while true {
                let left = parent * 2 + 1
                let right = left + 1
                var smallest = parent
                if left < heap.count && less(heap[left], heap[smallest]) {
                    smallest = left
                }
                if right < heap.count && less(heap[right], heap[smallest]) {
                    smallest = right
                }
                if smallest == parent { break }
                heap.swapAt(parent, smallest)
                parent = smallest
            }
        }
        
        private func less(_ a: Node, _ b: Node) -> Bool {
            if a.value != b.value { return a.value < b.value }
            return a.index < b.index
        }
    }
    
    private let MOD: Int64 = 1_000_000_007
    
    private func modPow(_ base: Int64, _ exp: Int64) -> Int64 {
        var result: Int64 = 1
        var b = base % MOD
        var e = exp
        while e > 0 {
            if (e & 1) == 1 {
                result = (result * b) % MOD
            }
            b = (b * b) % MOD
            e >>= 1
        }
        return result
    }
    
    func getFinalState(_ nums: [Int], _ k: Int, _ multiplier: Int) -> [Int] {
        let n = nums.count
        if multiplier == 1 || k == 0 {
            return nums.map { $0 % Int(MOD) }
        }
        
        var heap = MinHeap()
        var currentMax: Int64 = 0
        for (i, v) in nums.enumerated() {
            let val = Int64(v)
            heap.push(Node(value: val, index: i))
            if val > currentMax { currentMax = val }
        }
        
        var remaining = k
        while remaining > 0 {
            guard let top = heap.peek() else { break }
            // check without overflow: top.value * multiplier <= currentMax ?
            if top.value <= currentMax / Int64(multiplier) {
                _ = heap.pop()
                let newVal = top.value * Int64(multiplier)
                heap.push(Node(value: newVal, index: top.index))
                if newVal > currentMax { currentMax = newVal }
                remaining -= 1
            } else {
                break
            }
        }
        
        var nodes = heap.allElements()
        nodes.sort { $0.value < $1.value }
        
        let full = remaining / n
        let extra = remaining % n
        
        var result = Array(repeating: Int64(0), count: n)
        for (i, node) in nodes.enumerated() {
            var cnt = full
            if i < extra { cnt += 1 }
            let valMod = ((node.value % MOD) + MOD) % MOD
            let powMul = modPow(Int64(multiplier), Int64(cnt))
            result[node.index] = (valMod * powMul) % MOD
        }
        
        return result.map { Int($0) }
    }
}
```

## Kotlin

```kotlin
import java.util.PriorityQueue

class Solution {
    private val MOD = 1_000_000_007L

    private fun modPow(base: Long, exp: Long): Long {
        var b = base % MOD
        var e = exp
        var res = 1L
        while (e > 0) {
            if ((e and 1L) == 1L) res = (res * b) % MOD
            b = (b * b) % MOD
            e = e shr 1
        }
        return res
    }

    fun getFinalState(nums: IntArray, k: Int, multiplier: Int): IntArray {
        val n = nums.size
        if (multiplier == 1) {
            val ans = IntArray(n)
            for (i in 0 until n) ans[i] = nums[i]
            return ans
        }

        val mult = multiplier.toLong()
        val cur = LongArray(n) { nums[it].toLong() }
        var maxVal = cur.maxOrNull()!!

        val heap = PriorityQueue<Pair<Long, Int>>(compareBy { it.first })
        for (i in 0 until n) {
            heap.add(Pair(cur[i], i))
        }

        var opsDone = 0L
        val totalOps = k.toLong()
        while (opsDone < totalOps) {
            val (minVal, idx) = heap.peek()
            if (minVal > maxVal / mult) break   // min*mult > max
            heap.poll()
            val newVal = minVal * mult
            cur[idx] = newVal
            heap.add(Pair(newVal, idx))
            if (newVal > maxVal) maxVal = newVal
            opsDone++
        }

        var remaining = totalOps - opsDone
        if (remaining > 0) {
            val list = mutableListOf<Pair<Long, Int>>()
            while (heap.isNotEmpty()) {
                list.add(heap.poll())
            }
            // list is in ascending order of current values
            val addAll = remaining / n
            var extra = (remaining % n).toInt()

            val powBase = modPow(mult, addAll)
            val powExtra = (powBase * mult) % MOD

            for ((pos, pair) in list.withIndex()) {
                val idx = pair.second
                val factor = if (extra > 0) {
                    extra--
                    powExtra
                } else {
                    powBase
                }
                cur[idx] = (cur[idx] % MOD) * factor % MOD
            }
        } else {
            for (i in 0 until n) {
                cur[i] %= MOD
            }
        }

        val result = IntArray(n)
        for (i in 0 until n) {
            result[i] = ((cur[i] % MOD + MOD) % MOD).toInt()
        }
        return result
    }
}
```

## Dart

```dart
import 'dart:io';
import 'dart:math';

class _Node {
  int idx;
  int val;
  _Node(this.idx, this.val);
}

class MinHeap {
  final List<_Node> _data = [];

  bool get isEmpty => _data.isEmpty;

  void push(_Node node) {
    _data.add(node);
    _siftUp(_data.length - 1);
  }

  _Node pop() {
    final root = _data[0];
    final last = _data.removeLast();
    if (_data.isNotEmpty) {
      _data[0] = last;
      _siftDown(0);
    }
    return root;
  }

  _Node peek() => _data[0];

  void _siftUp(int idx) {
    while (idx > 0) {
      final parent = (idx - 1) >> 1;
      if (_compare(_data[idx], _data[parent]) < 0) {
        final tmp = _data[idx];
        _data[idx] = _data[parent];
        _data[parent] = tmp;
        idx = parent;
      } else {
        break;
      }
    }
  }

  void _siftDown(int idx) {
    final n = _data.length;
    while (true) {
      int left = idx * 2 + 1;
      int right = left + 1;
      int smallest = idx;

      if (left < n && _compare(_data[left], _data[smallest]) < 0) {
        smallest = left;
      }
      if (right < n && _compare(_data[right], _data[smallest]) < 0) {
        smallest = right;
      }
      if (smallest != idx) {
        final tmp = _data[idx];
        _data[idx] = _data[smallest];
        _data[smallest] = tmp;
        idx = smallest;
      } else {
        break;
      }
    }
  }

  int _compare(_Node a, _Node b) {
    if (a.val != b.val) return a.val.compareTo(b.val);
    return a.idx.compareTo(b.idx);
  }
}

class Solution {
  static const int MOD = 1000000007;

  List<int> getFinalState(List<int> nums, int k, int multiplier) {
    if (multiplier == 1 || k == 0) {
      return nums.map((v) => v % MOD).toList();
    }

    final heap = MinHeap();
    int maxVal = nums[0];
    for (int i = 0; i < nums.length; ++i) {
      heap.push(_Node(i, nums[i]));
      if (nums[i] > maxVal) maxVal = nums[i];
    }

    while (k > 0) {
      final minNode = heap.peek();
      // check condition: min * multiplier > max
      if (minNode.val * multiplier > maxVal) break;
      // perform operation
      heap.pop();
      int newVal = minNode.val * multiplier;
      heap.push(_Node(minNode.idx, newVal));
      if (newVal > maxVal) maxVal = newVal;
      k--;
    }

    List<int> result = List.filled(nums.length, 0);

    if (k == 0) {
      while (!heap.isEmpty) {
        final node = heap.pop();
        result[node.idx] = node.val % MOD;
      }
      return result;
    }

    // Extract remaining elements
    List<_Node> nodes = [];
    while (!heap.isEmpty) {
      nodes.add(heap.pop());
    }
    nodes.sort((a, b) {
      if (a.val != b.val) return a.val.compareTo(b.val);
      return a.idx.compareTo(b.idx);
    });

    int n = nums.length;
    int fullRounds = k ~/ n;
    int remainder = k % n;

    int powFull = _modPow(multiplier, fullRounds);

    for (int i = 0; i < nodes.length; ++i) {
      int valMod = nodes[i].val % MOD;
      int cur = (valMod * powFull) % MOD;
      if (i < remainder) {
        cur = (cur * multiplier) % MOD;
      }
      result[nodes[i].idx] = cur;
    }

    return result;
  }

  int _modPow(int base, int exp) {
    long res = 1;
    long b = base % MOD;
    while (exp > 0) {
      if ((exp & 1) == 1) {
        res = (res * b) % MOD;
      }
      b = (b * b) % MOD;
      exp >>= 1;
    }
    return res.toInt();
  }
}

// Helper type for intermediate large multiplication
class long {
  int _value;
  long(this._value);
  int get value => _value;

  static long operator *(long a, long b) => long(a._value * b._value);
  static long operator %(long a, int mod) => long(a._value % mod);
  static long operator +(long a, long b) => long(a._value + b._value);
  static long operator -(long a, long b) => long(a._value - b._value);
  static long operator /(long a, int d) => long(a._value ~/ d);
  static long operator &(long a, int mask) => long(a._value & mask);
  static long fromInt(int v) => long(v);
  int toInt() => _value;
}
```

## Golang

```go
package main

import (
	"container/heap"
	"sort"
)

const MOD int64 = 1000000007

type Item struct {
	val uint64
	idx int
}

// Min-heap implementation
type MinHeap []Item

func (h MinHeap) Len() int { return len(h) }
func (h MinHeap) Less(i, j int) bool {
	if h[i].val == h[j].val {
		return h[i].idx < h[j].idx
	}
	return h[i].val < h[j].val
}
func (h MinHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *MinHeap) Push(x interface{}) {
	*h = append(*h, x.(Item))
}
func (h *MinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	it := old[n-1]
	*h = old[:n-1]
	return it
}

// fast exponentiation modulo MOD
func modPow(base int64, exp int64) int64 {
	res := int64(1)
	b := base % MOD
	for exp > 0 {
		if exp&1 == 1 {
			res = (res * b) % MOD
		}
		b = (b * b) % MOD
		exp >>= 1
	}
	return res
}

func getFinalState(nums []int, k int, multiplier int) []int {
	if multiplier == 1 || k == 0 {
		res := make([]int, len(nums))
		for i, v := range nums {
			res[i] = int(int64(v) % MOD)
		}
		return res
	}

	n := len(nums)
	h := &MinHeap{}
	heap.Init(h)

	var maxVal uint64
	for i, v := range nums {
		val := uint64(v)
		if val > maxVal {
			maxVal = val
		}
		heap.Push(h, Item{val: val, idx: i})
	}

	remK := int64(k)
	mul := uint64(multiplier)

	for remK > 0 {
		minItem := (*h)[0]
		if uint64(minItem.val)*mul > maxVal && remK < int64(n) {
			// condition already true and remaining ops less than a full round,
			// we can break to handle them in batch.
			break
		}
		it := heap.Pop(h).(Item)
		newVal := it.val * mul
		if newVal > maxVal {
			maxVal = newVal
		}
		heap.Push(h, Item{val: newVal, idx: it.idx})
		remK--
		// after this operation check if condition holds for next step
		nextMin := (*h)[0]
		if uint64(nextMin.val)*mul > maxVal {
			break
		}
	}

	if remK == 0 {
		res := make([]int, n)
		for h.Len() > 0 {
			it := heap.Pop(h).(Item)
			res[it.idx] = int(int64(it.val) % MOD)
		}
		return res
	}

	// Extract remaining items
	items := make([]Item, n)
	for i := 0; i < n; i++ {
		items[i] = heap.Pop(h).(Item)
	}
	// Sort by current value then index to determine order of extra multiplications
	sort.Slice(items, func(i, j int) bool {
		if items[i].val == items[j].val {
			return items[i].idx < items[j].idx
		}
		return items[i].val < items[j].val
	})

	base := remK / int64(n)
	extra := remK % int64(n)

	powBase := modPow(int64(multiplier), base)
	mulMod := int64(multiplier) % MOD

	res := make([]int, n)
	for i, it := range items {
		valMod := int64(it.val%uint64(MOD)) * powBase % MOD
		if int64(i) < extra {
			valMod = valMod * mulMod % MOD
		}
		res[it.idx] = int(valMod)
	}
	return res
}
```

## Ruby

```ruby
class MinHeap
  def initialize
    @data = []
  end

  def push(item)
    data = @data
    data << item
    i = data.size - 1
    while i > 0
      p = (i - 1) / 2
      break if data[p][0] <= item[0]
      data[i] = data[p]
      i = p
    end
    data[i] = item
  end

  def pop
    data = @data
    top = data[0]
    last = data.pop
    unless data.empty?
      i = 0
      while (child = i * 2 + 1) < data.size
        right = child + 1
        child = right if right < data.size && data[right][0] < data[child][0]
        break if last[0] <= data[child][0]
        data[i] = data[child]
        i = child
      end
      data[i] = last
    end
    top
  end

  def empty?
    @data.empty?
  end
end

def get_final_state(nums, k, multiplier)
  mod = 1_000_000_007
  return nums.map { |x| x % mod } if multiplier == 1 || k == 0

  n = nums.length
  max_val = nums.max
  heap = MinHeap.new
  nums.each_with_index { |v, i| heap.push([v, i]) }

  while k > 0
    min_val, idx = heap.pop
    if min_val * multiplier > max_val
      heap.push([min_val, idx])
      break
    end
    new_val = min_val * multiplier
    nums[idx] = new_val
    k -= 1
    max_val = new_val if new_val > max_val
    heap.push([new_val, idx])
  end

  if k > 0
    cycle = k / n
    rem   = k % n
    factor_mod = multiplier.pow(cycle, mod)
    result = Array.new(n) { |i| (nums[i] % mod) * factor_mod % mod }
    if rem > 0
      sorted_idx = (0...n).to_a.sort_by { |i| nums[i] }
      rem.times do |j|
        idx = sorted_idx[j]
        result[idx] = (result[idx] * multiplier) % mod
      end
    end
    return result
  else
    return nums.map { |v| v % mod }
  end
end
```

## Scala

```scala
object Solution {
    private val MOD = 1000000007L

    def modPow(base: Long, exp: Long, mod: Long): Long = {
        var b = base % mod
        var e = exp
        var res = 1L
        while (e > 0) {
            if ((e & 1L) == 1L) res = (res * b) % mod
            b = (b * b) % mod
            e >>= 1
        }
        res
    }

    def getFinalState(nums: Array[Int], k: Int, multiplier: Int): Array[Int] = {
        if (multiplier == 1) {
            return nums.map(x => ((x % MOD).toInt))
        }

        val n = nums.length
        val pq = new java.util.PriorityQueue[(Long, Int)](
            new java.util.Comparator[(Long, Int)] {
                override def compare(a: (Long, Int), b: (Long, Int)): Int =
                    java.lang.Long.compare(a._1, b._1)
            }
        )

        var maxVal = Long.MinValue
        for (i <- 0 until n) {
            val v = nums(i).toLong
            pq.offer((v, i))
            if (v > maxVal) maxVal = v
        }

        var ops: Long = 0L
        val totalOps = k.toLong
        val mult = multiplier.toLong

        while (ops < totalOps) {
            val minElem = pq.peek()
            if (minElem._1 * mult > maxVal) {
                // condition met, break to batch processing
                break
            }
            // perform one operation
            pq.poll()
            val newVal = minElem._1 * mult
            pq.offer((newVal, minElem._2))
            if (newVal > maxVal) maxVal = newVal
            ops += 1
        }

        if (ops == totalOps) {
            // all operations simulated individually
            val result = new Array[Int](n)
            while (!pq.isEmpty) {
                val (v, idx) = pq.poll()
                result(idx) = ((v % MOD).toInt)
            }
            return result
        }

        // batch processing for remaining operations
        val remaining = totalOps - ops
        val fullCycles = remaining / n
        val extra = (remaining % n).toInt

        val arr = new Array[(Long, Int)](n)
        var idx = 0
        while (!pq.isEmpty) {
            arr(idx) = pq.poll()
            idx += 1
        }
        java.util.Arrays.sort(arr, new java.util.Comparator[(Long, Int)] {
            override def compare(a: (Long, Int), b: (Long, Int)): Int =
                java.lang.Long.compare(a._1, b._1)
        })

        val powFull = modPow(mult, fullCycles, MOD)
        val res = new Array[Long](n)

        for (elem <- arr) {
            val i = elem._2
            var v = ((elem._1 % MOD) * powFull) % MOD
            res(i) = v
        }

        for (i <- 0 until extra) {
            val index = arr(i)._2
            res(index) = (res(index) * mult) % MOD
        }

        res.map(v => (v % MOD).toInt)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_final_state(nums: Vec<i32>, k: i32, multiplier: i32) -> Vec<i32> {
        const MOD: i64 = 1_000_000_007;
        let n = nums.len();
        if n == 0 {
            return vec![];
        }
        // current values as u128 for safe arithmetic
        let mut cur_vals: Vec<u128> = nums.iter().map(|&x| x as u128).collect();

        use std::collections::BinaryHeap;
        use std::cmp::Reverse;

        let mut heap: BinaryHeap<Reverse<(u128, usize)>> = BinaryHeap::new();
        let mut max_val: u128 = 0;
        for (i, &v) in cur_vals.iter().enumerate() {
            heap.push(Reverse((v, i)));
            if v > max_val {
                max_val = v;
            }
        }

        let mut remaining: i64 = k as i64;
        let mult_u128 = multiplier as u128;

        // Simulate until condition holds or we run out of operations
        while remaining > 0 {
            let Reverse((min_val, idx)) = *heap.peek().unwrap();
            // if min*multiplier > max, break
            let prod = min_val.checked_mul(mult_u128).unwrap_or(u128::MAX);
            if prod > max_val {
                break;
            }
            heap.pop(); // remove the minimum
            let new_val = prod; // min_val * multiplier
            cur_vals[idx] = new_val;
            heap.push(Reverse((new_val, idx)));
            if new_val > max_val {
                max_val = new_val;
            }
            remaining -= 1;
        }

        // If no operations left, just return modulo values
        if remaining == 0 {
            return cur_vals.iter().map(|&v| (v % MOD as u128) as i32).collect();
        }

        // Bulk processing: each full round multiplies every element by multiplier
        let cycles = remaining / n as i64;
        let rem = (remaining % n as i64) as usize;

        fn mod_pow(mut base: i64, mut exp: i64, modu: i64) -> i64 {
            let mut result: i64 = 1;
            let mut b = ((base % modu) + modu) % modu;
            while exp > 0 {
                if exp & 1 == 1 {
                    result = (result as i128 * b as i128 % modu as i128) as i64;
                }
                b = (b as i128 * b as i128 % modu as i128) as i64;
                exp >>= 1;
            }
            result
        }

        let pow_cycle = mod_pow(multiplier as i64, cycles, MOD);

        // Apply the full cycles to each element
        let mut res: Vec<i64> = vec![0; n];
        for i in 0..n {
            let base_mod = (cur_vals[i] % MOD as u128) as i64;
            res[i] = (base_mod as i128 * pow_cycle as i128 % MOD as i128) as i64;
        }

        // Determine the smallest `rem` elements based on current values
        let mut idxs: Vec<usize> = (0..n).collect();
        idxs.sort_by_key(|&i| cur_vals[i]);

        for &i in idxs.iter().take(rem) {
            res[i] = (res[i] as i128 * multiplier as i128 % MOD as i128) as i64;
        }

        res.into_iter().map(|x| x as i32).collect()
    }
}
```

## Racket

```racket
(require data/heap)

(define MOD 1000000007)

(: pow-mod (Integer Integer -> Integer))
(define (pow-mod base exp)
  (let loop ((b (remainder base MOD)) (e exp) (res 1))
    (if (= e 0)
        res
        (loop (remainder (* b b) MOD)
              (quotient e 2)
              (if (odd? e) (remainder (* res b) MOD) res)))))

(: get-final-state (listof exact-integer? exact-integer? exact-integer? -> (listof exact-integer?)))
(define (get-final-state nums k multiplier)
  (let* ((n (length nums))
         (heap (make-heap <))
         (max-val (apply max nums)))
    ;; initialize heap with [value index]
    (for ([v nums] [i (in-naturals)])
      (heap-insert! heap (list v i)))
    (let loop ((remaining k) (max-so-far max-val))
      (if (or (= remaining 0)
              (let* ((min-pair (heap-min heap))
                     (min-val (first min-pair)))
                (> (* min-val multiplier) max-so-far)))
          (values remaining max-so-far)
          (begin
            (define min-pair (heap-remove-min! heap))
            (define min-val (first min-pair))
            (define idx (second min-pair))
            (define new-val (* min-val multiplier))
            (heap-insert! heap (list new-val idx))
            (loop (- remaining 1) (max max-so-far new-val))))))
    ;; after loop we have possibly remaining operations
    (let-values ([(remaining max-final) (values k max-val)]) ; placeholder, will be overwritten
      (define-values (remaining max-final)
        (call-with-values
            (lambda () (loop 0 max-val))
          values)))
    ;; extract current values and keep original order list for sorting
    (let* ((pairs '())
           (arr (make-vector n)))
      (let extract ()
        (when (> (heap-count heap) 0)
          (define p (heap-remove-min! heap))
          (set! pairs (cons p pairs))
          (vector-set! arr (second p) (first p))
          (extract)))
      (extract)
      (if (= remaining 0)
          ;; no more operations, just apply modulo
          (let result ()
            (map (lambda (v) (remainder v MOD)) (vector->list arr)))
          (begin
            (define cycles (quotient remaining n))
            (define rem    (remainder remaining n))
            (when (> cycles 0)
              (define mult-pow (pow-mod multiplier cycles))
              (for ([i (in-range n)])
                (vector-set! arr i (remainder (* (vector-ref arr i) mult-pow) MOD))))
            ;; sort pairs by original raw value to decide extra multiplications
            (define sorted-pairs (sort pairs (lambda (a b) (< (first a) (first b)))))
            (for ([i (in-range rem)])
              (define idx (second (list-ref sorted-pairs i)))
              (vector-set! arr idx (remainder (* (vector-ref arr idx) multiplier) MOD)))
            ;; final result list preserving original order
            (map (lambda (v) (remainder v MOD)) (vector->list arr)))))))
```

## Erlang

```erlang
-spec get_final_state(Nums :: [integer()], K :: integer(), Multiplier :: integer()) -> [integer()].
get_final_state(Nums, K, Multiplier) ->
    Mod = 1000000007,
    case Multiplier of
        1 ->
            [Num rem Mod || Num <- Nums];
        _ ->
            N = length(Nums),
            %% build array of values indexed from 0
            InitArray = lists:foldl(
                fun({Idx, Val}, Acc) -> array:set(Idx, Val, Acc) end,
                array:new(N, [{default,0}]),
                lists:zip(lists:seq(0, N-1), Nums)
            ),
            MaxVal0 = lists:max(Nums),
            {RemK, _MaxAfter, ArrAfterSim} = simulate(K, MaxVal0, Multiplier, InitArray, N),
            case RemK of
                0 ->
                    %% apply modulo and return in original order
                    [ (array:get(I, ArrAfterSim) rem Mod) || I <- lists:seq(0, N-1) ];
                _ ->
                    %% batch processing
                    ListVals = [{I, array:get(I, ArrAfterSim)} || I <- lists:seq(0, N-1)],
                    Sorted = lists:keysort(2, ListVals),
                    Extra = RemK div N,
                    Rem  = RemK rem N,
                    PowExtra = pow_mod(Multiplier, Extra, Mod),
                    %% build result array
                    ResultArray = batch_apply(Sorted, 0, Rem, PowExtra, Multiplier, Mod, array:new(N, [{default,0}])),
                    [ (array:get(I, ResultArray) rem Mod) || I <- lists:seq(0, N-1) ]
            end
    end.

%% simulate until condition breaks or K exhausted
simulate(0, MaxVal, _M, Arr, _N) ->
    {0, MaxVal, Arr};
simulate(K, MaxVal, M, Arr, N) ->
    {MinIdx, MinVal} = find_min(N, Arr),
    case MinVal * M =< MaxVal of
        true ->
            NewVal = MinVal * M,
            NewMax = max(MaxVal, NewVal),
            NewArr = array:set(MinIdx, NewVal, Arr),
            simulate(K-1, NewMax, M, NewArr, N);
        false ->
            {K, MaxVal, Arr}
    end.

%% find minimum value and its index
find_min(N, Arr) ->
    find_min(0, N-1, Arr, 0, array:get(0, Arr)).

find_min(CurIdx, EndIdx, Arr, MinIdx, MinVal) when CurIdx =< EndIdx ->
    Val = array:get(CurIdx, Arr),
    if
        Val < MinVal -> find_min(CurIdx+1, EndIdx, Arr, CurIdx, Val);
        true          -> find_min(CurIdx+1, EndIdx, Arr, MinIdx, MinVal)
    end;
find_min(_, _, _Arr, MinIdx, MinVal) ->
    {MinIdx, MinVal}.

%% batch apply remaining multiplications
batch_apply([], _Pos, _Rem, _PowExtra, _M, _Mod, ResArr) ->
    ResArr;
batch_apply([{Idx, Val}|Rest], Pos, Rem, PowExtra, M, Mod, ResArr) ->
    Factor = case Pos < Rem of
                 true -> (PowExtra * (M rem Mod)) rem Mod;
                 false -> PowExtra
             end,
    FinalVal = ((Val rem Mod) * Factor) rem Mod,
    NewResArr = array:set(Idx, FinalVal, ResArr),
    batch_apply(Rest, Pos+1, Rem, PowExtra, M, Mod, NewResArr).

%% fast modular exponentiation
pow_mod(_Base, 0, _Mod) -> 1;
pow_mod(Base, Exp, Mod) when Exp band 1 =:= 1 ->
    (Base rem Mod) * pow_mod((Base*Base) rem Mod, Exp bsr 1, Mod) rem Mod;
pow_mod(Base, Exp, Mod) ->
    pow_mod((Base*Base) rem Mod, Exp bsr 1, Mod).
```

## Elixir

```elixir
defmodule Solution do
  @mod 1_000_000_007

  @spec get_final_state(nums :: [integer], k :: integer, multiplier :: integer) :: [integer]
  def get_final_state(nums, k, multiplier) do
    if multiplier == 1 do
      Enum.map(nums, &rem(&1, @mod))
    else
      n = length(nums)

      tree =
        Enum.with_index(nums)
        |> Enum.reduce(:gb_trees.empty(), fn {val, idx}, acc ->
          :gb_trees.insert({val, idx}, val, acc)
        end)

      max_val = Enum.max(nums)

      {tree, _max_val, k_rem} = simulate(tree, max_val, k, multiplier)

      sorted =
        :gb_trees.fold(fn {{val, idx}, _v, acc} -> [{val, idx} | acc] end, [], tree)
        |> Enum.reverse()

      extra = div(k_rem, n)
      rem_ops = rem(k_rem, n)

      pow_extra = mod_pow(multiplier, extra, @mod)

      result = List.duplicate(0, n)

      {final_res, _} =
        Enum.reduce(Enum.with_index(sorted), {result, 0}, fn {{val, idx}, i},
                                                             {res, _} ->
          base_mod = rem(val, @mod)
          val_mod = rem(base_mod * pow_extra, @mod)

          val_mod =
            if i < rem_ops do
              rem(val_mod * multiplier, @mod)
            else
              val_mod
            end

          {List.replace_at(res, idx, val_mod), 0}
        end)

      final_res
    end
  end

  defp simulate(tree, max_val, k, mult) when k > 0 do
    case :gb_trees.smallest(tree) do
      {{min_val, min_idx}, _} ->
        if min_val * mult <= max_val do
          {_, _, tree2} = :gb_trees.take_smallest(tree)
          new_val = min_val * mult
          new_max = if new_val > max_val, do: new_val, else: max_val
          new_tree = :gb_trees.insert({new_val, min_idx}, new_val, tree2)
          simulate(new_tree, new_max, k - 1, mult)
        else
          {tree, max_val, k}
        end
    end
  end

  defp simulate(tree, max_val, 0, _mult), do: {tree, max_val, 0}

  defp mod_pow(_base, 0, _mod), do: 1

  defp mod_pow(base, exp, mod) do
    pow_mod(rem(base, mod), exp, 1, mod)
  end

  defp pow_mod(_base, 0, acc, _mod), do: acc

  defp pow_mod(base, exp, acc, mod) do
    acc = if rem(exp, 2) == 1, do: rem(acc * base, mod), else: acc
    base = rem(base * base, mod)
    pow_mod(base, div(exp, 2), acc, mod)
  end
end
```
