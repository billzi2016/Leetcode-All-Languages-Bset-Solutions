# 1606. Find Servers That Handled Most Number of Requests

## Cpp

```cpp
class Solution {
public:
    vector<int> busiestServers(int k, vector<int>& arrival, vector<int>& load) {
        int n = arrival.size();
        vector<int> cnt(k, 0);
        std::set<int> available;
        for (int i = 0; i < k; ++i) available.insert(i);
        
        using P = pair<long long,int>; // end time, server id
        priority_queue<P, vector<P>, greater<P>> busy;
        
        for (int i = 0; i < n; ++i) {
            long long curTime = arrival[i];
            // release servers that have finished by curTime
            while (!busy.empty() && busy.top().first <= curTime) {
                int sid = busy.top().second;
                busy.pop();
                available.insert(sid);
            }
            if (available.empty()) continue; // drop request
            
            int target = i % k;
            auto it = available.lower_bound(target);
            if (it == available.end()) it = available.begin(); // wrap around
            int sid = *it;
            
            // assign request to server sid
            cnt[sid]++;
            busy.emplace(curTime + load[i], sid);
            available.erase(it);
        }
        
        int mx = 0;
        for (int c : cnt) mx = max(mx, c);
        vector<int> res;
        for (int i = 0; i < k; ++i) {
            if (cnt[i] == mx) res.push_back(i);
        }
        return res;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<Integer> busiestServers(int k, int[] arrival, int[] load) {
        TreeSet<Integer> free = new TreeSet<>();
        for (int i = 0; i < k; i++) free.add(i);

        PriorityQueue<long[]> busy = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));
        int n = arrival.length;
        int[] cnt = new int[k];
        int max = 0;

        for (int i = 0; i < n; i++) {
            int curTime = arrival[i];

            while (!busy.isEmpty() && busy.peek()[0] <= curTime) {
                long[] finished = busy.poll();
                free.add((int) finished[1]);
            }

            if (free.isEmpty()) continue;

            int target = i % k;
            Integer server = free.ceiling(target);
            if (server == null) server = free.first();

            free.remove(server);
            cnt[server]++;
            max = Math.max(max, cnt[server]);

            long endTime = (long) curTime + load[i];
            busy.offer(new long[]{endTime, server});
        }

        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            if (cnt[i] == max) result.add(i);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def busiestServers(self, k, arrival, load):
        """
        :type k: int
        :type arrival: List[int]
        :type load: List[int]
        :rtype: List[int]
        """
        import bisect, heapq

        available = list(range(k))          # sorted list of free servers
        busy = []                           # min-heap of (finish_time, server_id)
        cnt = [0] * k                       # handled request count per server

        for i, (t, d) in enumerate(zip(arrival, load)):
            # release servers that have finished by current arrival time
            while busy and busy[0][0] <= t:
                ft, sid = heapq.heappop(busy)
                bisect.insort(available, sid)

            if not available:
                continue  # all servers are busy, drop request

            target = i % k
            idx = bisect.bisect_left(available, target)
            if idx == len(available):
                idx = 0   # wrap around to the smallest id

            server = available.pop(idx)
            cnt[server] += 1
            heapq.heappush(busy, (t + d, server))

        max_cnt = max(cnt)
        return [i for i, c in enumerate(cnt) if c == max_cnt]
```

## Python3

```python
import heapq
import bisect
from typing import List

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available = list(range(k))          # sorted list of free servers
        busy = []                           # min-heap of (finish_time, server_id)
        cnt = [0] * k

        for i, (t, l) in enumerate(zip(arrival, load)):
            # release servers that have finished by current arrival time
            while busy and busy[0][0] <= t:
                ft, sid = heapq.heappop(busy)
                bisect.insort_left(available, sid)

            if not available:
                continue

            target = i % k
            idx = bisect.bisect_left(available, target)
            if idx == len(available):
                idx = 0   # wrap around

            server = available.pop(idx)
            cnt[server] += 1
            heapq.heappush(busy, (t + l, server))

        max_cnt = max(cnt)
        return [i for i, c in enumerate(cnt) if c == max_cnt]
```

## C

```c
#include <stdlib.h>

typedef struct {
    long long end;
    int server;
} Node;

/* Fenwick Tree (BIT) */
static void bit_add(int *bit, int n, int idx, int delta) { // idx: 0-based
    for (int i = idx + 1; i <= n; i += i & -i)
        bit[i] += delta;
}
static int bit_sum(int *bit, int n, int idx) { // sum [0..idx], idx: 0-based
    int res = 0;
    for (int i = idx + 1; i > 0; i -= i & -i)
        res += bit[i];
    return res;
}
static int bit_range_sum(int *bit, int n, int l, int r) { // inclusive, 0-based
    if (l > r) return 0;
    int sumR = bit_sum(bit, n, r);
    int sumL = (l == 0) ? 0 : bit_sum(bit, n, l - 1);
    return sumR - sumL;
}
static int bit_find_kth(int *bit, int n, int k) { // 1 <= k <= total sum, returns 0-based index
    int idx = 0;
    int mask = 1;
    while ((mask << 1) <= n) mask <<= 1;          // highest power of two <= n
    for (int step = mask; step > 0; step >>= 1) {
        int next = idx + step;
        if (next <= n && bit[next] < k) {
            idx = next;
            k -= bit[next];
        }
    }
    return idx; // 0-based index of the found position
}

/* Min-heap for busy servers */
static void heap_swap(Node *a, Node *b) {
    Node t = *a;
    *a = *b;
    *b = t;
}
static void heapify_up(Node *heap, int idx) {
    while (idx > 0) {
        int parent = (idx - 1) >> 1;
        if (heap[parent].end <= heap[idx].end) break;
        heap_swap(&heap[parent], &heap[idx]);
        idx = parent;
    }
}
static void heapify_down(Node *heap, int size, int idx) {
    while (1) {
        int left = (idx << 1) + 1;
        int right = left + 1;
        int smallest = idx;
        if (left < size && heap[left].end < heap[smallest].end)
            smallest = left;
        if (right < size && heap[right].end < heap[smallest].end)
            smallest = right;
        if (smallest == idx) break;
        heap_swap(&heap[idx], &heap[smallest]);
        idx = smallest;
    }
}
static void heap_push(Node *heap, int *size, Node node) {
    int idx = *size;
    heap[idx] = node;
    (*size)++;
    heapify_up(heap, idx);
}
static Node heap_pop(Node *heap, int *size) {
    Node top = heap[0];
    heap[0] = heap[*size - 1];
    (*size)--;
    if (*size > 0)
        heapify_down(heap, *size, 0);
    return top;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* busiestServers(int k, int* arrival, int arrivalSize, int* load, int loadSize, int* returnSize) {
    (void)loadSize; // unused
    int *cnt = calloc(k, sizeof(int));
    int *bit = calloc(k + 1, sizeof(int));          // BIT is 1-indexed
    for (int i = 0; i < k; ++i)
        bit_add(bit, k, i, 1);                      // all servers initially free

    Node *heap = malloc(arrivalSize * sizeof(Node));
    int hsize = 0;

    for (int i = 0; i < arrivalSize; ++i) {
        long long curArr = arrival[i];

        /* Release servers that have finished by current arrival time */
        while (hsize > 0 && heap[0].end <= curArr) {
            Node freed = heap_pop(heap, &hsize);
            bit_add(bit, k, freed.server, 1);       // make server free
        }

        int target = i % k;
        int afterFree = bit_range_sum(bit, k, target, k - 1);
        int idx = -1;

        if (afterFree > 0) {
            int prefBefore = (target == 0) ? 0 : bit_sum(bit, k, target - 1);
            idx = bit_find_kth(bit, k, prefBefore + 1);
        } else {
            int totalFree = bit_sum(bit, k, k - 1);
            if (totalFree == 0)
                continue;                           // request dropped
            idx = bit_find_kth(bit, k, 1);          // first free from start
        }

        /* Assign request to server idx */
        cnt[idx]++;
        bit_add(bit, k, idx, -1);                   // mark as busy

        Node node;
        node.end = curArr + load[i];
        node.server = idx;
        heap_push(heap, &hsize, node);
    }

    int maxc = 0;
    for (int i = 0; i < k; ++i)
        if (cnt[i] > maxc) maxc = cnt[i];

    int rc = 0;
    for (int i = 0; i < k; ++i)
        if (cnt[i] == maxc) rc++;

    int *res = malloc(rc * sizeof(int));
    int pos = 0;
    for (int i = 0; i < k; ++i)
        if (cnt[i] == maxc) res[pos++] = i;

    *returnSize = rc;

    free(cnt);
    free(bit);
    free(heap);
    return res;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<int> BusiestServers(int k, int[] arrival, int[] load) {
        var available = new SortedSet<int>();
        for (int i = 0; i < k; i++) available.Add(i);
        
        var busy = new PriorityQueue<int, long>(); // server id, end time
        var handled = new int[k];
        int n = arrival.Length;
        
        for (int i = 0; i < n; i++) {
            long curTime = arrival[i];
            
            while (busy.Count > 0 && busy.TryPeek(out int srv, out long end) && end <= curTime) {
                busy.Dequeue();
                available.Add(srv);
            }
            
            if (available.Count == 0) continue;
            
            int target = i % k;
            int server;
            var view = available.GetViewBetween(target, k - 1);
            if (view.Count > 0) {
                server = view.Min;
            } else {
                server = available.Min; // wrap around
            }
            
            available.Remove(server);
            busy.Enqueue(server, curTime + load[i]);
            handled[server]++;
        }
        
        int max = handled.Max();
        var result = new List<int>();
        for (int i = 0; i < k; i++) {
            if (handled[i] == max) result.Add(i);
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} k
 * @param {number[]} arrival
 * @param {number[]} load
 * @return {number[]}
 */
var busiestServers = function(k, arrival, load) {
    // Fenwick Tree (Binary Indexed Tree)
    class BIT {
        constructor(n) {
            this.n = n;
            this.tree = new Array(n + 1).fill(0);
        }
        add(idx, delta) { // idx: 0‑based
            for (let i = idx + 1; i <= this.n; i += i & -i) {
                this.tree[i] += delta;
            }
        }
        sum(idx) { // prefix sum [0..idx], idx 0‑based
            let res = 0;
            for (let i = idx + 1; i > 0; i -= i & -i) {
                res += this.tree[i];
            }
            return res;
        }
        rangeSum(l, r) { // inclusive, 0‑based
            if (l > r) return 0;
            return this.sum(r) - (l ? this.sum(l - 1) : 0);
        }
        // smallest index such that prefix sum >= k (k is 1‑based)
        findKth(k) {
            let idx = 0;
            // largest power of two <= n
            let bitMask = 1;
            while ((bitMask << 1) <= this.n) bitMask <<= 1;
            for (let d = bitMask; d > 0; d >>= 1) {
                const next = idx + d;
                if (next <= this.n && this.tree[next] < k) {
                    idx = next;
                    k -= this.tree[next];
                }
            }
            return idx; // 0‑based index
        }
    }

    // Min‑heap for busy servers: [endTime, serverId]
    class MinHeap {
        constructor() { this.heap = []; }
        size() { return this.heap.length; }
        peek() { return this.heap[0]; }
        push(val) {
            const h = this.heap;
            h.push(val);
            let i = h.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (h[p][0] <= h[i][0]) break;
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
                    let l = i * 2 + 1, r = i * 2 + 2, smallest = i;
                    if (l < h.length && h[l][0] < h[smallest][0]) smallest = l;
                    if (r < h.length && h[r][0] < h[smallest][0]) smallest = r;
                    if (smallest === i) break;
                    [h[i], h[smallest]] = [h[smallest], h[i]];
                    i = smallest;
                }
            }
            return top;
        }
    }

    const n = arrival.length;
    const bit = new BIT(k);
    for (let i = 0; i < k; ++i) bit.add(i, 1); // all servers free

    const busy = new MinHeap();
    const cnt = new Array(k).fill(0);

    for (let i = 0; i < n; ++i) {
        const t = arrival[i];
        // release finished servers
        while (busy.size() && busy.peek()[0] <= t) {
            const [, sid] = busy.pop();
            bit.add(sid, 1); // make server available again
        }

        const start = i % k;
        let sid = -1;

        // try to find free server in [start, k-1]
        if (bit.rangeSum(start, k - 1) > 0) {
            const before = start ? bit.sum(start - 1) : 0;
            sid = bit.findKth(before + 1);
        } else if (bit.rangeSum(0, start - 1) > 0) { // wrap around
            sid = bit.findKth(1);
        }

        if (sid !== -1) {
            cnt[sid] += 1;
            bit.add(sid, -1); // occupy
            busy.push([t + load[i], sid]);
        }
    }

    const maxCnt = Math.max(...cnt);
    const res = [];
    for (let i = 0; i < k; ++i) {
        if (cnt[i] === maxCnt) res.push(i);
    }
    return res;
};
```

## Typescript

```typescript
function busiestServers(k: number, arrival: number[], load: number[]): number[] {
    class BIT {
        n: number;
        tree: number[];
        constructor(n: number) {
            this.n = n;
            this.tree = new Array(n + 1).fill(0);
        }
        add(idx: number, delta: number): void {
            idx++; // to 1‑based
            while (idx <= this.n) {
                this.tree[idx] += delta;
                idx += idx & -idx;
            }
        }
        sum(idx: number): number {
            if (idx < 0) return 0;
            idx++;
            let res = 0;
            while (idx > 0) {
                res += this.tree[idx];
                idx -= idx & -idx;
            }
            return res;
        }
        total(): number {
            return this.sum(this.n - 1);
        }
    }

    class MinHeap {
        data: [number, number][] = [];
        get size(): number { return this.data.length; }
        peek(): [number, number] | undefined { return this.data[0]; }
        push(item: [number, number]): void {
            const a = this.data;
            a.push(item);
            let i = a.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (a[p][0] <= a[i][0]) break;
                [a[p], a[i]] = [a[i], a[p]];
                i = p;
            }
        }
        pop(): [number, number] | undefined {
            const a = this.data;
            if (a.length === 0) return undefined;
            const top = a[0];
            const last = a.pop()!;
            if (a.length > 0) {
                a[0] = last;
                let i = 0;
                while (true) {
                    let l = i * 2 + 1, r = i * 2 + 2, smallest = i;
                    if (l < a.length && a[l][0] < a[smallest][0]) smallest = l;
                    if (r < a.length && a[r][0] < a[smallest][0]) smallest = r;
                    if (smallest === i) break;
                    [a[i], a[smallest]] = [a[smallest], a[i]];
                    i = smallest;
                }
            }
            return top;
        }
    }

    const bit = new BIT(k);
    for (let i = 0; i < k; ++i) bit.add(i, 1); // all servers free

    const busy = new MinHeap();
    const cnt = new Array(k).fill(0);

    function findNext(start: number): number {
        const totalFree = bit.total();
        if (totalFree === 0) return -1;
        const before = start > 0 ? bit.sum(start - 1) : 0;
        if (totalFree - before === 0) return -1; // none from start to end
        let l = start, r = k - 1, ans = -1;
        while (l <= r) {
            const m = (l + r) >> 1;
            if (bit.sum(m) > before) {
                ans = m;
                r = m - 1;
            } else {
                l = m + 1;
            }
        }
        return ans;
    }

    for (let i = 0; i < arrival.length; ++i) {
        const t = arrival[i];
        // release finished servers
        while (busy.size && busy.peek()![0] <= t) {
            const [, sid] = busy.pop()!;
            bit.add(sid, 1);
        }
        if (bit.total() === 0) continue; // drop request

        const target = i % k;
        let sid = findNext(target);
        if (sid === -1) sid = findNext(0); // wrap around
        // assign request to sid
        bit.add(sid, -1);
        cnt[sid]++;
        busy.push([t + load[i], sid]);
    }

    const maxCnt = Math.max(...cnt);
    const res: number[] = [];
    for (let i = 0; i < k; ++i) {
        if (cnt[i] === maxCnt) res.push(i);
    }
    return res;
}
```

## Php

```php
class BusyHeap extends SplHeap {
    public function compare($a, $b) {
        // a and b are arrays [endTime, serverId]
        if ($a[0] === $b[0]) {
            return $b[1] <=> $a[1]; // smaller id has higher priority when end times equal
        }
        return $b[0] <=> $a[0]; // earlier end time has higher priority
    }
}

class BIT {
    private int $n;
    private array $tree = [];
    private int $maxPow;

    public function __construct(int $size) {
        $this->n = $size;
        $this->tree = array_fill(0, $size + 2, 0);
        $this->maxPow = 1;
        while ($this->maxPow <= $size) {
            $this->maxPow <<= 1;
        }
    }

    // add delta at index idx (0‑based)
    public function add(int $idx, int $delta): void {
        for ($i = $idx + 1; $i <= $this->n; $i += $i & (-$i)) {
            $this->tree[$i] += $delta;
        }
    }

    // prefix sum [0..idx] inclusive, idx can be -1
    public function sum(int $idx): int {
        if ($idx < 0) return 0;
        $res = 0;
        for ($i = $idx + 1; $i > 0; $i -= $i & (-$i)) {
            $res += $this->tree[$i];
        }
        return $res;
    }

    // sum on [l..r] inclusive
    public function rangeSum(int $l, int $r): int {
        if ($l > $r) return 0;
        return $this->sum($r) - ($l > 0 ? $this->sum($l - 1) : 0);
    }

    // find smallest index such that prefix sum >= k (k is 1‑based)
    public function kth(int $k): int {
        $idx = 0;
        for ($bit = $this->maxPow; $bit > 0; $bit >>= 1) {
            $next = $idx + $bit;
            if ($next <= $this->n && $this->tree[$next] < $k) {
                $k -= $this->tree[$next];
                $idx = $next;
            }
        }
        // $idx is the largest index with prefix sum < original k, so answer is $idx (0‑based)
        return $idx;
    }
}

class Solution {

    /**
     * @param Integer $k
     * @param Integer[] $arrival
     * @param Integer[] $load
     * @return Integer[]
     */
    function busiestServers($k, $arrival, $load) {
        $n = count($arrival);
        $counts = array_fill(0, $k, 0);

        // BIT to maintain available servers (1 means free)
        $bit = new BIT($k);
        for ($i = 0; $i < $k; ++$i) {
            $bit->add($i, 1);
        }

        $busy = new BusyHeap();

        for ($i = 0; $i < $n; ++$i) {
            $time = $arrival[$i];
            $duration = $load[$i];

            // free servers whose tasks have finished
            while (!$busy->isEmpty()) {
                $top = $busy->current(); // [endTime, serverId]
                if ($top[0] <= $time) {
                    $busy->extract();
                    $sid = $top[1];
                    $bit->add($sid, 1); // mark as free
                } else {
                    break;
                }
            }

            $totalFree = $bit->sum($k - 1);
            if ($totalFree == 0) {
                continue; // drop request
            }

            $target = $i % $k;

            $freeAfterTarget = $bit->rangeSum($target, $k - 1);
            if ($freeAfterTarget > 0) {
                $order = ($target > 0 ? $bit->sum($target - 1) : 0) + 1;
                $sid = $bit->kth($order);
            } else {
                // wrap around to the smallest free server
                $sid = $bit->kth(1);
            }

            // assign request to server $sid
            $counts[$sid]++;

            // mark server as busy
            $bit->add($sid, -1);
            $busy->insert([$time + $duration, $sid]);
        }

        $max = max($counts);
        $result = [];
        for ($i = 0; $i < $k; ++$i) {
            if ($counts[$i] == $max) {
                $result[] = $i;
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    class SegmentTree {
        private let n: Int
        private var tree: [Int]
        
        init(_ size: Int) {
            self.n = size
            self.tree = Array(repeating: 0, count: 4 * size)
            build(1, 0, n - 1)
        }
        
        private func build(_ node: Int, _ l: Int, _ r: Int) {
            if l == r {
                tree[node] = 1
            } else {
                let mid = (l + r) >> 1
                build(node << 1, l, mid)
                build(node << 1 | 1, mid + 1, r)
                tree[node] = tree[node << 1] + tree[node << 1 | 1]
            }
        }
        
        func update(_ index: Int, _ value: Int) {
            update(1, 0, n - 1, index, value)
        }
        
        private func update(_ node: Int, _ l: Int, _ r: Int, _ idx: Int, _ val: Int) {
            if l == r {
                tree[node] = val
            } else {
                let mid = (l + r) >> 1
                if idx <= mid {
                    update(node << 1, l, mid, idx, val)
                } else {
                    update(node << 1 | 1, mid + 1, r, idx, val)
                }
                tree[node] = tree[node << 1] + tree[node << 1 | 1]
            }
        }
        
        // find first index with value 1 in [ql, qr]
        func queryFirst(_ ql: Int) -> Int? {
            return queryFirst(1, 0, n - 1, ql, n - 1)
        }
        
        private func queryFirst(_ node: Int, _ l: Int, _ r: Int, _ ql: Int, _ qr: Int) -> Int? {
            if ql > qr || tree[node] == 0 { return nil }
            if l == r {
                return l
            }
            let mid = (l + r) >> 1
            var res: Int? = nil
            if ql <= mid {
                res = queryFirst(node << 1, l, mid, ql, min(qr, mid))
                if res != nil { return res }
            }
            if qr > mid {
                res = queryFirst(node << 1 | 1, mid + 1, r, max(ql, mid + 1), qr)
            }
            return res
        }
    }
    
    struct HeapNode {
        var end: Int
        var server: Int
    }
    
    class MinHeap {
        private var data: [HeapNode] = []
        
        var isEmpty: Bool { data.isEmpty }
        func peek() -> HeapNode? { data.first }
        
        func push(_ node: HeapNode) {
            data.append(node)
            siftUp(data.count - 1)
        }
        
        func pop() -> HeapNode? {
            guard !data.isEmpty else { return nil }
            let root = data[0]
            let last = data.removeLast()
            if !data.isEmpty {
                data[0] = last
                siftDown(0)
            }
            return root
        }
        
        private func siftUp(_ idx: Int) {
            var child = idx
            while child > 0 {
                let parent = (child - 1) >> 1
                if data[child].end < data[parent].end {
                    data.swapAt(child, parent)
                    child = parent
                } else { break }
            }
        }
        
        private func siftDown(_ idx: Int) {
            var parent = idx
            while true {
                let left = parent * 2 + 1
                let right = left + 1
                var smallest = parent
                if left < data.count && data[left].end < data[smallest].end {
                    smallest = left
                }
                if right < data.count && data[right].end < data[smallest].end {
                    smallest = right
                }
                if smallest == parent { break }
                data.swapAt(parent, smallest)
                parent = smallest
            }
        }
    }
    
    func busiestServers(_ k: Int, _ arrival: [Int], _ load: [Int]) -> [Int] {
        let n = arrival.count
        var requestCount = Array(repeating: 0, count: k)
        let segTree = SegmentTree(k)
        let busyHeap = MinHeap()
        
        for i in 0..<n {
            let curTime = arrival[i]
            // free servers whose tasks have finished
            while let top = busyHeap.peek(), top.end <= curTime {
                _ = busyHeap.pop()
                segTree.update(top.server, 1)
            }
            
            var start = i % k
            var serverIdx: Int? = segTree.queryFirst(start)
            if serverIdx == nil {
                serverIdx = segTree.queryFirst(0)
            }
            guard let idx = serverIdx else { continue } // all servers busy, drop request
            
            // assign request to server idx
            requestCount[idx] += 1
            segTree.update(idx, 0) // mark as busy
            busyHeap.push(HeapNode(end: curTime + load[i], server: idx))
        }
        
        let maxHandled = requestCount.max() ?? 0
        var result: [Int] = []
        for i in 0..<k {
            if requestCount[i] == maxHandled {
                result.append(i)
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
import java.util.PriorityQueue
import java.util.TreeSet

class Solution {
    data class Busy(val end: Long, val id: Int)

    fun busiestServers(k: Int, arrival: IntArray, load: IntArray): List<Int> {
        val available = TreeSet<Int>()
        for (i in 0 until k) {
            available.add(i)
        }
        val busy = PriorityQueue<Busy>(compareBy<Busy> { it.end }.thenBy { it.id })
        val count = IntArray(k)

        for (i in arrival.indices) {
            val curTime = arrival[i].toLong()
            // free up servers that have finished by now
            while (busy.isNotEmpty() && busy.peek().end <= curTime) {
                val freed = busy.poll()
                available.add(freed.id)
            }
            if (available.isEmpty()) continue

            val target = i % k
            var serverId = available.ceiling(target)
            if (serverId == null) {
                serverId = available.first()
            }

            // assign request to serverId
            available.remove(serverId)
            count[serverId]++
            busy.add(Busy(curTime + load[i].toLong(), serverId))
        }

        var maxHandled = 0
        for (c in count) {
            if (c > maxHandled) maxHandled = c
        }
        val result = mutableListOf<Int>()
        for (i in 0 until k) {
            if (count[i] == maxHandled) result.add(i)
        }
        return result
    }
}
```

## Dart

```dart
class MinHeap {
  final List<List<int>> _data = [];

  bool get isEmpty => _data.isEmpty;
  List<int> get top => _data[0];

  void push(int endTime, int serverId) {
    _data.add([endTime, serverId]);
    _siftUp(_data.length - 1);
  }

  List<int> pop() {
    final res = _data[0];
    final last = _data.removeLast();
    if (_data.isNotEmpty) {
      _data[0] = last;
      _siftDown(0);
    }
    return res;
  }

  void _siftUp(int i) {
    while (i > 0) {
      final p = (i - 1) >> 1;
      if (_data[p][0] <= _data[i][0]) break;
      final tmp = _data[i];
      _data[i] = _data[p];
      _data[p] = tmp;
      i = p;
    }
  }

  void _siftDown(int i) {
    final n = _data.length;
    while (true) {
      int smallest = i;
      final l = i * 2 + 1;
      final r = l + 1;
      if (l < n && _data[l][0] < _data[smallest][0]) smallest = l;
      if (r < n && _data[r][0] < _data[smallest][0]) smallest = r;
      if (smallest == i) break;
      final tmp = _data[i];
      _data[i] = _data[smallest];
      _data[smallest] = tmp;
      i = smallest;
    }
  }
}

class SegmentTree {
  final List<int> _tree;
  final int n;

  SegmentTree(this.n) : _tree = List.filled(4 * n, 0) {
    _build(1, 0, n - 1);
  }

  void _build(int node, int l, int r) {
    if (l == r) {
      _tree[node] = 1;
      return;
    }
    final mid = (l + r) >> 1;
    _build(node << 1, l, mid);
    _build(node << 1 | 1, mid + 1, r);
    _tree[node] = _tree[node << 1] + _tree[node << 1 | 1];
  }

  void update(int idx, int val) => _update(1, 0, n - 1, idx, val);

  void _update(int node, int l, int r, int idx, int val) {
    if (l == r) {
      _tree[node] = val;
      return;
    }
    final mid = (l + r) >> 1;
    if (idx <= mid) {
      _update(node << 1, l, mid, idx, val);
    } else {
      _update(node << 1 | 1, mid + 1, r, idx, val);
    }
    _tree[node] = _tree[node << 1] + _tree[node << 1 | 1];
  }

  // returns first index with value 1 in [ql, qr], or -1 if none
  int queryFirst(int ql, int qr) => _queryFirst(1, 0, n - 1, ql, qr);

  int _queryFirst(int node, int l, int r, int ql, int qr) {
    if (_tree[node] == 0 || ql > r || qr < l) return -1;
    if (l == r) return l;
    final mid = (l + r) >> 1;
    final left = _queryFirst(node << 1, l, mid, ql, qr);
    if (left != -1) return left;
    return _queryFirst(node << 1 | 1, mid + 1, r, ql, qr);
  }

  bool get isEmpty => _tree[1] == 0;
}

class Solution {
  List<int> busiestServers(int k, List<int> arrival, List<int> load) {
    final n = arrival.length;
    final seg = SegmentTree(k);
    final heap = MinHeap();
    final cnt = List.filled(k, 0);

    for (int i = 0; i < n; ++i) {
      final curTime = arrival[i];
      // free servers whose tasks have finished
      while (!heap.isEmpty && heap.top[0] <= curTime) {
        final freed = heap.pop();
        seg.update(freed[1], 1);
      }

      if (seg.isEmpty) continue; // all busy, drop request

      final target = i % k;
      int idx = seg.queryFirst(target, k - 1);
      if (idx == -1) {
        idx = seg.queryFirst(0, target - 1);
      }
      // assign request to server idx
      cnt[idx]++;
      seg.update(idx, 0);
      heap.push(curTime + load[i], idx);
    }

    int maxCnt = 0;
    for (final c in cnt) {
      if (c > maxCnt) maxCnt = c;
    }
    final List<int> res = [];
    for (int i = 0; i < k; ++i) {
      if (cnt[i] == maxCnt) res.add(i);
    }
    return res;
  }
}
```

## Golang

```go
package main

import (
	"container/heap"
)

type Fenwick struct {
	n    int
	tree []int
}

func NewFenwick(n int) *Fenwick {
	return &Fenwick{n: n, tree: make([]int, n+1)}
}
func (f *Fenwick) Update(idx, delta int) {
	idx++ // to 1‑based
	for idx <= f.n {
		f.tree[idx] += delta
		idx += idx & -idx
	}
}
func (f *Fenwick) Query(idx int) int {
	if idx < 0 {
		return 0
	}
	idx++
	sum := 0
	for idx > 0 {
		sum += f.tree[idx]
		idx -= idx & -idx
	}
	return sum
}
// LowerBound returns the smallest index i (0‑based) such that prefix sum >= target.
// Assumes 1 <= target <= total sum.
func (f *Fenwick) LowerBound(target int) int {
	idx := 0
	bit := 1
	for bit<<1 <= f.n {
		bit <<= 1
	}
	for bit > 0 {
		next := idx + bit
		if next <= f.n && f.tree[next] < target {
			target -= f.tree[next]
			idx = next
		}
		bit >>= 1
	}
	return idx // zero‑based index
}

type Busy struct {
	end    int
	server int
}
type MinHeap []Busy

func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i].end < h[j].end }
func (h MinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MinHeap) Push(x interface{}) {
	*h = append(*h, x.(Busy))
}
func (h *MinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func busiestServers(k int, arrival []int, load []int) []int {
	if k == 0 {
		return []int{}
	}
	ft := NewFenwick(k)
	for i := 0; i < k; i++ {
		ft.Update(i, 1)
	}
	busyHeap := &MinHeap{}
	heap.Init(busyHeap)

	requestsHandled := make([]int, k)

	for i := 0; i < len(arrival); i++ {
		curArr := arrival[i]
		curLoad := load[i]

		// free servers whose tasks have finished
		for busyHeap.Len() > 0 && (*busyHeap)[0].end <= curArr {
			b := heap.Pop(busyHeap).(Busy)
			ft.Update(b.server, 1) // make server available again
		}

		if ft.Query(k-1) == 0 { // no servers free
			continue
		}

		target := i % k

		pre := ft.Query(target - 1)
		totalAfter := ft.Query(k-1) - pre
		var srv int
		if totalAfter > 0 {
			srv = ft.LowerBound(pre + 1)
		} else {
			srv = ft.LowerBound(1)
		}

		requestsHandled[srv]++
		ft.Update(srv, -1) // mark as busy
		heap.Push(busyHeap, Busy{end: curArr + curLoad, server: srv})
	}

	maxCnt := 0
	for _, cnt := range requestsHandled {
		if cnt > maxCnt {
			maxCnt = cnt
		}
	}
	var res []int
	for i, cnt := range requestsHandled {
		if cnt == maxCnt {
			res = append(res, i)
		}
	}
	return res
}
```

## Ruby

```ruby
class Fenwick
  def initialize(n)
    @tree = Array.new(n + 2, 0)
  end

  def add(i, delta)
    i += 1
    while i < @tree.size
      @tree[i] += delta
      i += i & -i
    end
  end

  def sum(i)
    return 0 if i < 0
    i += 1
    res = 0
    while i > 0
      res += @tree[i]
      i -= i & -i
    end
    res
  end

  def range_sum(l, r)
    return 0 if l > r
    sum(r) - (l == 0 ? 0 : sum(l - 1))
  end

  # returns smallest index such that prefix sum >= k (k is 1‑based)
  def find_kth(k)
    idx = 0
    bit = 1 << (@tree.size.bit_length - 1)
    while bit > 0
      nxt = idx + bit
      if nxt < @tree.size && @tree[nxt] < k
        k -= @tree[nxt]
        idx = nxt
      end
      bit >>= 1
    end
    idx
  end
end

module MinHeap
  def self.push(heap, item)
    heap << item
    i = heap.size - 1
    while i > 0
      p = (i - 1) / 2
      break if heap[p][0] <= heap[i][0]
      heap[p], heap[i] = heap[i], heap[p]
      i = p
    end
  end

  def self.pop(heap)
    top = heap[0]
    last = heap.pop
    unless heap.empty?
      heap[0] = last
      i = 0
      size = heap.size
      loop do
        l = i * 2 + 1
        r = l + 1
        smallest = i
        smallest = l if l < size && heap[l][0] < heap[smallest][0]
        smallest = r if r < size && heap[r][0] < heap[smallest][0]
        break if smallest == i
        heap[i], heap[smallest] = heap[smallest], heap[i]
        i = smallest
      end
    end
    top
  end

  def self.peek(heap)
    heap[0]
  end
end

# @param {Integer} k
# @param {Integer[]} arrival
# @param {Integer[]} load
# @return {Integer[]}
def busiest_servers(k, arrival, load)
  n = arrival.length
  counts = Array.new(k, 0)

  fenwick = Fenwick.new(k)
  (0...k).each { |i| fenwick.add(i, 1) }

  busy = [] # min‑heap of [end_time, server_id]

  i = 0
  while i < n
    t = arrival[i]
    dur = load[i]

    while !busy.empty? && MinHeap.peek(busy)[0] <= t
      _, sid = MinHeap.pop(busy)
      fenwick.add(sid, 1)
    end

    if fenwick.range_sum(0, k - 1) == 0
      i += 1
      next
    end

    target = i % k
    sid = nil
    if fenwick.range_sum(target, k - 1) > 0
      prefix = target.zero? ? 0 : fenwick.sum(target - 1)
      kth = prefix + 1
      sid = fenwick.find_kth(kth)
    else
      sid = fenwick.find_kth(1)
    end

    counts[sid] += 1
    fenwick.add(sid, -1)
    MinHeap.push(busy, [t + dur, sid])

    i += 1
  end

  max_cnt = counts.max
  res = []
  counts.each_with_index { |c, idx| res << idx if c == max_cnt }
  res
end
```

## Scala

```scala
object Solution {
  import java.util.{TreeSet, PriorityQueue}
  import scala.collection.mutable.ListBuffer

  def busiestServers(k: Int, arrival: Array[Int], load: Array[Int]): List[Int] = {
    val available = new TreeSet[Integer]()
    var i = 0
    while (i < k) { available.add(i); i += 1 }

    // busy queue stores [endTime, serverId]
    val busy = new PriorityQueue[Array[Long]](new java.util.Comparator[Array[Long]] {
      override def compare(a: Array[Long], b: Array[Long]): Int =
        java.lang.Long.compare(a(0), b(0))
    })

    val cnt = new Array[Int](k)
    val n = arrival.length
    var idx = 0

    while (idx < n) {
      val curTime = arrival(idx).toLong

      // release servers that have finished by curTime
      while (!busy.isEmpty && busy.peek()(0) <= curTime) {
        val arr = busy.poll()
        available.add(arr(1).toInt)
      }

      if (available.isEmpty) {
        idx += 1 // request dropped
      } else {
        val target = idx % k
        var sidObj: Integer = available.ceiling(target)
        var sid: Int = -1
        if (sidObj != null) {
          sid = sidObj.intValue()
        } else {
          sid = available.first().intValue() // wrap around
        }

        // assign request to server sid
        available.remove(sid)
        cnt(sid) += 1
        val endTime = curTime + load(idx).toLong
        busy.add(Array(endTime, sid.toLong))

        idx += 1
      }
    }

    var maxCnt = 0
    i = 0
    while (i < k) {
      if (cnt(i) > maxCnt) maxCnt = cnt(i)
      i += 1
    }

    val res = ListBuffer[Int]()
    i = 0
    while (i < k) {
      if (cnt(i) == maxCnt) res += i
      i += 1
    }
    res.toList
  }
}
```

## Rust

```rust
use std::collections::{BTreeSet, BinaryHeap};
use std::cmp::Reverse;

impl Solution {
    pub fn busiest_servers(k: i32, arrival: Vec<i32>, load: Vec<i32>) -> Vec<i32> {
        let k_usize = k as usize;
        let n = arrival.len();
        let mut available: BTreeSet<usize> = (0..k_usize).collect();
        let mut busy: BinaryHeap<Reverse<(i64, usize)>> = BinaryHeap::new();
        let mut cnt = vec![0usize; k_usize];

        for i in 0..n {
            let cur_time = arrival[i] as i64;
            let finish_time = cur_time + load[i] as i64;

            // release servers that have finished by cur_time
            while let Some(&Reverse((end, sid))) = busy.peek() {
                if end <= cur_time {
                    busy.pop();
                    available.insert(sid);
                } else {
                    break;
                }
            }

            if available.is_empty() {
                continue; // request dropped
            }

            let target = i % k_usize;

            // find smallest server >= target, otherwise wrap around
            let server_opt = available.range(target..).next().cloned()
                .or_else(|| available.iter().next().cloned());

            if let Some(server) = server_opt {
                available.remove(&server);
                cnt[server] += 1;
                busy.push(Reverse((finish_time, server)));
            }
        }

        // find max count
        let max_cnt = *cnt.iter().max().unwrap_or(&0);
        let mut result = Vec::new();
        for (i, &c) in cnt.iter().enumerate() {
            if c == max_cnt {
                result.push(i as i32);
            }
        }
        result
    }
}
```

## Racket

```racket
(require racket/priority-queue)

(define/contract (busiest-servers k arrival load)
  (-> exact-integer? (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  (let* ((n (length arrival))
         (bit (make-vector (+ k 1) 0))          ; 1‑indexed BIT
         (counts (make-vector k 0))
         (pq (make-pq <)))                     ; min‑heap keyed by finish time

    ;; BIT helpers -------------------------------------------------
    (define (bit-add! idx delta)
      (let ((i (+ idx 1)))
        (let loop ((i i))
          (when (<= i k)
            (vector-set! bit i (+ (vector-ref bit i) delta))
            (loop (+ i (bitwise-and i (- i))))))))

    (define (bit-sum idx)
      (let loop ((i (+ idx 1)) (s 0))
        (if (= i 0) s
            (loop (bitwise-and i (- i)) (+ s (vector-ref bit i))))))

    (define (bit-find-first target)
      (let* ((max-log (integer-length k))
             (mask (arithmetic-shift 1 (- max-log 1))))
        (let loop ((mask mask) (idx 0) (t target))
          (if (= mask 0)
              idx
              (let ((next (+ idx mask)))
                (if (and (<= next k) (< (vector-ref bit next) t))
                    (loop (arithmetic-shift mask -1) next (- t (vector-ref bit next)))
                    (loop (arithmetic-shift mask -1) idx t)))))))

    ;; initially all servers are free
    (for ([i (in-range k)]) (bit-add! i 1))

    ;; process each request -----------------------------------------
    (for ([i (in-range n)])
      (define t (list-ref arrival i))
      (define load-i (list-ref load i))

      ;; release finished servers
      (let loop ()
        (when (and (not (pq-empty? pq)) (<= (pq-peek-key pq) t))
          (define srv (pq-peek-value pq))
          (pq-pop! pq)
          (bit-add! srv 1)
          (loop)))

      (define start (remainder i k))
      (define total-avail (bit-sum (- k 1)))
      (when (> total-avail 0)
        (define sum-before (if (> start 0) (bit-sum (- start 1)) 0))
        (define target
          (if (> (- total-avail sum-before) 0)
              (+ sum-before 1)
              1))
        (define srv (bit-find-first target))

        ;; assign request to server srv
        (bit-add! srv -1)
        (pq-add! pq (+ t load-i) srv)
        (vector-set! counts srv (+ (vector-ref counts srv) 1))))

    ;; find maximum handled count ------------------------------------
    (define maxc
      (let loop ((i 0) (mx 0))
        (if (= i k) mx
            (loop (+ i 1) (max mx (vector-ref counts i))))))

    ;; collect all busiest servers -----------------------------------
    (for/list ([i (in-range k)] #:when (= (vector-ref counts i) maxc)) i)))
```

## Erlang

```erlang
-module(solution).
-export([busiest_servers/3]).

-spec busiest_servers(K :: integer(), Arrival :: [integer()], Load :: [integer()]) -> [integer()].
busiest_servers(K, Arrival, Load) ->
    Counts0 = array:new(K, {default, 0}),
    Avail0 = gb_sets:from_list(lists:seq(0, K - 1)),
    Busy0 = gb_trees:empty(),
    {_AvailF, _BusyF, CountsF} = process(0, Arrival, Load, Avail0, Busy0, Counts0, K),
    find_max(K, CountsF, -1, []).

%% Process each request recursively
process(_Idx, [], [], Avail, Busy, Counts, _K) ->
    {Avail, Busy, Counts};
process(Idx, [A|As], [L|Ls], Avail, Busy, Counts, K) ->
    {Busy1, Avail1} = free_servers(A, Busy, Avail),
    Target = Idx rem K,
    case assign_server(Target, Avail1) of
        none ->
            process(Idx + 1, As, Ls, Avail1, Busy1, Counts, K);
        {Sid, Avail2} ->
            Count = array:get(Sid, Counts),
            Counts1 = array:set(Sid, Count + 1, Counts),
            Finish = A + L,
            Busy2 = add_busy(Finish, Sid, Busy1),
            process(Idx + 1, As, Ls, Avail2, Busy2, Counts1, K)
    end.

%% Free servers whose tasks have finished by current arrival time
free_servers(Time, Busy, Avail) ->
    case gb_trees:is_empty(Busy) of
        true -> {Busy, Avail};
        false ->
            {Key, Val} = gb_trees:smallest(Busy),
            if Key =< Time ->
                    Busy1 = gb_trees:delete(Key, Busy),
                    Avail1 = lists:foldl(fun(Sid, Acc) -> gb_sets:add(Sid, Acc) end, Avail, Val),
                    free_servers(Time, Busy1, Avail1);
               true ->
                    {Busy, Avail}
            end
    end.

%% Assign the appropriate server if available
assign_server(Target, AvailSet) ->
    case gb_sets:is_empty(AvailSet) of
        true -> none;
        false ->
            Iter = gb_sets:iterator_from(Target, AvailSet),
            case gb_sets:next(Iter) of
                none ->
                    % wrap around to the smallest server id
                    WrapIter = gb_sets:iterator(AvailSet),
                    {Sid, _} = gb_sets:next(WrapIter),
                    {Sid, gb_sets:delete(Sid, AvailSet)};
                {Sid, _} ->
                    {Sid, gb_sets:delete(Sid, AvailSet)}
            end
    end.

%% Insert a busy server entry into the tree
add_busy(FinishTime, Sid, BusyTree) ->
    case gb_trees:lookup(FinishTime, BusyTree) of
        {value, List} -> NewList = [Sid | List];
        none -> NewList = [Sid]
    end,
    gb_trees:enter(FinishTime, NewList, BusyTree).

%% Find servers with maximum handled requests
find_max(K, Counts, MaxSoFar, Acc) ->
    find_max(0, K, Counts, MaxSoFar, Acc).

find_max(I, K, _Counts, Max, Acc) when I == K ->
    lists:reverse(Acc);
find_max(I, K, Counts, Max, Acc) ->
    C = array:get(I, Counts),
    case C > Max of
        true -> find_max(I + 1, K, Counts, C, [I]);
        false ->
            case C == Max of
                true -> find_max(I + 1, K, Counts, Max, [I | Acc]);
                false -> find_max(I + 1, K, Counts, Max, Acc)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec busiest_servers(k :: integer, arrival :: [integer], load :: [integer]) :: [integer]
  def busiest_servers(k, arrival, load) do
    avail = :gb_sets.from_list(Enum.to_list(0..k - 1))
    busy = :gb_trees.empty()
    counts = %{}

    {final_avail, final_busy, final_counts} =
      Enum.zip(arrival, load)
      |> Enum.with_index()
      |> Enum.reduce({avail, busy, counts}, fn {{time, ld}, idx},
                                               {avail_set, busy_tree, cnts} ->
        # free servers that have completed by current arrival time
        {avail_set2, busy_tree2} = free_servers(time, avail_set, busy_tree)

        if :gb_sets.is_empty(avail_set2) do
          # request is dropped
          {avail_set2, busy_tree2, cnts}
        else
          target = rem(idx, k)
          it = :gb_sets.iterator_from(avail_set2, target)

          case :gb_sets.next(it) do
            {server_id, _} ->
              assign(server_id, time, ld, avail_set2, busy_tree2, cnts)

            :none ->
              {wrap_server, _} = :gb_sets.smallest(avail_set2)
              assign(wrap_server, time, ld, avail_set2, busy_tree2, cnts)
          end
        end
      end)

    max_cnt =
      case Map.values(final_counts) do
        [] -> 0
        vals -> Enum.max(vals)
      end

    final_counts
    |> Enum.filter(fn {_id, c} -> c == max_cnt end)
    |> Enum.map(fn {id, _c} -> id end)
    |> Enum.sort()
  end

  defp free_servers(current_time, avail_set, busy_tree) do
    if :gb_trees.is_empty(busy_tree) do
      {avail_set, busy_tree}
    else
      case :gb_trees.smallest(busy_tree) do
        {ft, ids} when ft <= current_time ->
          busy_tree2 = :gb_trees.delete_min(busy_tree)

          avail_set2 =
            Enum.reduce(ids, avail_set, fn sid, acc -> :gb_sets.add(sid, acc) end)

          free_servers(current_time, avail_set2, busy_tree2)

        {_ft, _ids} ->
          {avail_set, busy_tree}
      end
    end
  end

  defp assign(server_id, start_time, load_i, avail_set, busy_tree, cnts) do
    # remove from available set
    avail_set2 = :gb_sets.delete(server_id, avail_set)

    ft = start_time + load_i

    busy_tree2 =
      case :gb_trees.lookup(ft, busy_tree) do
        {:value, list} -> :gb_trees.insert(ft, [server_id | list], busy_tree)
        :none -> :gb_trees.insert(ft, [server_id], busy_tree)
      end

    cnts2 = Map.update(cnts, server_id, 1, &(&1 + 1))
    {avail_set2, busy_tree2, cnts2}
  end
end
```
