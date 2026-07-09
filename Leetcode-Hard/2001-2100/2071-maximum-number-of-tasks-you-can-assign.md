# 2071. Maximum Number of Tasks You Can Assign

## Cpp

```cpp
class Solution {
public:
    int maxTaskAssign(vector<int>& tasks, vector<int>& workers, int pills, int strength) {
        sort(tasks.begin(), tasks.end());
        sort(workers.begin(), workers.end());
        int n = tasks.size();
        int m = workers.size();
        auto can = [&](int k)->bool{
            if (k == 0) return true;
            int remainingPills = pills;
            multiset<int> avail;
            // take the largest k workers
            for (int i = m - k; i < m; ++i) {
                avail.insert(workers[i]);
            }
            // assign tasks from hardest to easiest among the smallest k tasks
            for (int i = k - 1; i >= 0; --i) {
                int t = tasks[i];
                auto itStrong = prev(avail.end());
                if (*itStrong >= t) {
                    avail.erase(itStrong);
                    continue;
                }
                if (remainingPills == 0) return false;
                int need = t - strength;
                auto itWeak = avail.lower_bound(need);
                if (itWeak == avail.end()) return false;
                avail.erase(itWeak);
                --remainingPills;
            }
            return true;
        };
        
        int lo = 0, hi = min(n, m);
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (can(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
};
```

## Java

```java
class Solution {
    public int maxTaskAssign(int[] tasks, int[] workers, int pills, int strength) {
        java.util.Arrays.sort(tasks);
        java.util.Arrays.sort(workers);
        int n = tasks.length;
        int m = workers.length;
        int lo = 0, hi = Math.min(n, m);
        while (lo < hi) {
            int mid = (lo + hi + 1) >>> 1;
            if (canAssign(mid, tasks, workers, pills, strength)) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        return lo;
    }

    private boolean canAssign(int k, int[] tasks, int[] workers, int pills, int strength) {
        java.util.TreeMap<Integer, Integer> map = new java.util.TreeMap<>();
        int m = workers.length;
        for (int i = m - k; i < m; ++i) {
            map.merge(workers[i], 1, Integer::sum);
        }
        for (int i = k - 1; i >= 0; --i) {
            int t = tasks[i];
            Integer maxKey = map.lastKey();
            if (maxKey != null && maxKey >= t) {
                decrement(map, maxKey);
                continue;
            }
            if (pills == 0) return false;
            int need = t - strength;
            Integer cand = map.ceilingKey(need);
            if (cand == null) return false;
            decrement(map, cand);
            pills--;
        }
        return true;
    }

    private void decrement(java.util.TreeMap<Integer, Integer> map, int key) {
        int cnt = map.get(key);
        if (cnt == 1) map.remove(key);
        else map.put(key, cnt - 1);
    }
}
```

## Python

```python
class Solution(object):
    def maxTaskAssign(self, tasks, workers, pills, strength):
        """
        :type tasks: List[int]
        :type workers: List[int]
        :type pills: int
        :type strength: int
        :rtype: int
        """
        import heapq

        tasks.sort()
        workers.sort()
        n, m = len(tasks), len(workers)
        max_k = min(n, m)

        def can(k):
            if k == 0:
                return True
            # smallest k tasks
            tks = tasks[:k]               # ascending
            # largest k workers
            wks = workers[-k:]             # ascending
            used = [False] * k

            # max-heap for strongest available worker (no pill)
            max_heap = [(-wks[i], i) for i in range(k)]
            heapq.heapify(max_heap)

            min_heap = []  # eligible workers for pill, (strength, idx)
            # pointer to add newly eligible workers from the end (strongest to weakest)
            ptr = k - 1

            pills_left = pills

            # process tasks from hardest to easiest
            for t in reversed(tks):
                need = t - strength
                if need < 0:
                    need = 0
                # add all workers whose strength >= need (they become eligible)
                while ptr >= 0 and wks[ptr] >= need:
                    heapq.heappush(min_heap, (wks[ptr], ptr))
                    ptr -= 1

                # try to assign without pill using strongest available worker
                while max_heap and used[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap and -max_heap[0][0] >= t:
                    _, idx = heapq.heappop(max_heap)
                    used[idx] = True
                    continue

                # need to use a pill
                if pills_left == 0:
                    return False
                while min_heap and used[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if not min_heap:
                    return False
                _, idx = heapq.heappop(min_heap)
                used[idx] = True
                pills_left -= 1

            return True

        lo, hi = 0, max_k + 1  # hi is exclusive
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if can(mid):
                lo = mid
            else:
                hi = mid
        return lo
```

## Python3

```python
class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        import heapq
        tasks.sort()
        workers.sort()
        n, m = len(tasks), len(workers)
        max_k = min(n, m)

        def can(k):
            if k == 0:
                return True
            sel_tasks = tasks[:k]               # smallest k tasks (ascending)
            sel_workers = workers[m - k:]       # largest k workers (ascending)
            left, right = 0, k - 1
            max_heap = []
            remaining_pills = pills

            # process tasks from hardest to easiest
            for t in reversed(sel_tasks):
                # add all workers that can do this task without a pill
                while right >= left and sel_workers[right] >= t:
                    heapq.heappush(max_heap, -sel_workers[right])
                    right -= 1

                if max_heap:
                    heapq.heappop(max_heap)   # assign strongest worker, no pill used
                    continue

                # need to use a pill
                if remaining_pills == 0:
                    return False

                # find the weakest worker that can do it with a pill
                needed = t - strength
                while left <= right and sel_workers[left] < needed:
                    left += 1
                if left > right:
                    return False
                # use this worker with a pill
                left += 1
                remaining_pills -= 1

            return True

        lo, hi = 0, max_k
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int cmp_int(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    return (x > y) - (x < y);
}

/* Binary Indexed Tree */
typedef struct {
    int n;
    int *tree;
} BIT;

static void bit_init(BIT *bit, int n, int *buffer) {
    bit->n = n;
    bit->tree = buffer;
    for (int i = 1; i <= n; ++i) bit->tree[i] = 0;
    for (int i = 1; i <= n; ++i) {
        bit->tree[i] += 1;                     // initial value 1 at each position
        int j = i + (i & -i);
        if (j <= n) bit->tree[j] += bit->tree[i];
    }
}

static void bit_add(BIT *bit, int idx, int delta) {
    for (; idx <= bit->n; idx += idx & -idx)
        bit->tree[idx] += delta;
}

static int bit_sum(BIT *bit, int idx) {   // sum[1..idx]
    int res = 0;
    for (; idx > 0; idx -= idx & -idx)
        res += bit->tree[idx];
    return res;
}

/* find smallest index such that prefix sum >= k (k>=1) */
static int bit_findKth(BIT *bit, int k) {
    int idx = 0;
    int mask = 1 << (31 - __builtin_clz(bit->n));
    for (; mask; mask >>= 1) {
        int next = idx + mask;
        if (next <= bit->n && bit->tree[next] < k) {
            idx = next;
            k -= bit->tree[next];
        }
    }
    return idx + 1;   // 1‑based index
}

/* feasibility check for given k */
static int can_assign(int k, const int *tasksSorted, const int *workersSorted,
                      int workersSize, int pills, int strength) {
    if (k == 0) return 1;

    const int *taskPtr = tasksSorted;                 // first k smallest tasks
    const int *workerPtr = workersSorted + workersSize - k; // k strongest workers

    static int bitBuf[50005];   // enough for max n,m (5e4)
    BIT bit;
    bit_init(&bit, k, bitBuf);

    int remainingPills = pills;
    int totalRemaining = k;

    int maxIdx = k - 1;   // zero‑based index of current strongest worker

    for (int ti = k - 1; ti >= 0; --ti) {
        int t = taskPtr[ti];

        while (maxIdx >= 0 && bit_sum(&bit, maxIdx + 1) - bit_sum(&bit, maxIdx) == 0)
            --maxIdx;

        if (maxIdx >= 0 && workerPtr[maxIdx] >= t) {
            /* assign without pill */
            bit_add(&bit, maxIdx + 1, -1);
            --totalRemaining;
            continue;
        }

        if (remainingPills == 0) return 0;

        long long need = (long long)t - strength;
        if (need < 0) need = 0;
        int lo = (int)(lower_bound(workerPtr, workerPtr + k, (int)need) - workerPtr);

        int before = bit_sum(&bit, lo);   // workers with index < lo
        if (totalRemaining - before == 0) return 0;   // no eligible worker

        int idx = bit_findKth(&bit, before + 1) - 1;   // zero‑based position
        bit_add(&bit, idx + 1, -1);
        --remainingPills;
        --totalRemaining;
    }
    return 1;
}

/* lower_bound implementation for int arrays */
static const int *lower_bound(const int *first, const int *last, int value) {
    while (first < last) {
        const int *mid = first + (last - first) / 2;
        if (*mid < value)
            first = mid + 1;
        else
            last = mid;
    }
    return first;
}

int maxTaskAssign(int* tasks, int tasksSize, int* workers, int workersSize, int pills, int strength) {
    qsort(tasks, tasksSize, sizeof(int), cmp_int);
    qsort(workers, workersSize, sizeof(int), cmp_int);

    int lo = 0, hi = tasksSize < workersSize ? tasksSize : workersSize;
    while (lo < hi) {
        int mid = (lo + hi + 1) >> 1;
        if (can_assign(mid, tasks, workers, workersSize, pills, strength))
            lo = mid;
        else
            hi = mid - 1;
    }
    return lo;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int MaxTaskAssign(int[] tasks, int[] workers, int pills, int strength) {
        Array.Sort(tasks);
        Array.Sort(workers);
        int n = tasks.Length;
        int m = workers.Length;
        int low = 0, high = Math.Min(n, m);
        while (low < high) {
            int mid = (low + high + 1) >> 1;
            if (CanAssign(mid, tasks, workers, pills, strength))
                low = mid;
            else
                high = mid - 1;
        }
        return low;
    }

    private bool CanAssign(int k, int[] tasks, int[] workers, int pills, int strength) {
        // take k smallest tasks (already sorted ascending)
        // take k largest workers
        var comparer = Comparer<(int val, int id)>.Create((a, b) => {
            int cmp = a.val.CompareTo(b.val);
            return cmp != 0 ? cmp : a.id.CompareTo(b.id);
        });
        var set = new SortedSet<(int val, int id)>(comparer);

        int wStart = workers.Length - k;
        for (int i = wStart; i < workers.Length; ++i) {
            set.Add((workers[i], i));
        }

        int remainingPills = pills;
        for (int ti = k - 1; ti >= 0; --ti) {
            int task = tasks[ti];
            // strongest available worker
            var maxWorker = set.Max;
            if (maxWorker.val >= task) {
                set.Remove(maxWorker);
                continue;
            }
            if (remainingPills == 0) return false;

            int need = task - strength;
            // find smallest worker with val >= need
            var lowerBound = (need, int.MinValue);
            var view = set.GetViewBetween(lowerBound, (int.MaxValue, int.MaxValue));
            if (view.Count == 0) return false;
            var chosen = view.Min;
            set.Remove(chosen);
            remainingPills--;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} tasks
 * @param {number[]} workers
 * @param {number} pills
 * @param {number} strength
 * @return {number}
 */
var maxTaskAssign = function(tasks, workers, pills, strength) {
    // sort tasks ascending and workers ascending
    tasks.sort((a, b) => a - b);
    workers.sort((a, b) => a - b);
    
    const n = tasks.length;
    const m = workers.length;
    const maxK = Math.min(n, m);
    
    // binary search on answer
    let lo = 0, hi = maxK;
    while (lo < hi) {
        const mid = Math.floor((lo + hi + 1) / 2);
        if (canAssign(mid)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
    
    // helper: lower bound in a sorted array
    function lowerBound(arr, target) {
        let l = 0, r = arr.length;
        while (l < r) {
            const mid = (l + r) >> 1;
            if (arr[mid] < target) l = mid + 1;
            else r = mid;
        }
        return l;
    }
    
    // Fenwick Tree (Binary Indexed Tree)
    class BIT {
        constructor(size) {
            this.n = size;
            this.bit = new Array(size + 1).fill(0);
        }
        add(idx, delta) { // idx: 0‑based
            for (let i = idx + 1; i <= this.n; i += i & -i) {
                this.bit[i] += delta;
            }
        }
        sum(idx) { // sum of first idx elements [0, idx)
            let res = 0;
            for (let i = idx; i > 0; i -= i & -i) {
                res += this.bit[i];
            }
            return res;
        }
        // find smallest index such that prefix sum >= k (k is 1‑based)
        kth(k) {
            let idx = 0;
            // highest power of two >= n
            let bitMask = 1;
            while (bitMask <= this.n) bitMask <<= 1;
            for (let d = bitMask; d > 0; d >>= 1) {
                const next = idx + d;
                if (next <= this.n && this.bit[next] < k) {
                    idx = next;
                    k -= this.bit[next];
                }
            }
            return idx; // 0‑based index
        }
    }
    
    function canAssign(k) {
        // take k smallest tasks
        const taskSlice = tasks.slice(0, k);
        // take k strongest workers (they are at the end of sorted workers)
        const startIdx = workers.length - k;
        const selectedWorkers = workers.slice(startIdx); // ascending order, length k
        
        const bit = new BIT(k);
        for (let i = 0; i < k; ++i) bit.add(i, 1);
        let remaining = k;
        let remainingPills = pills;
        
        // process tasks from hardest to easiest
        for (let ti = k - 1; ti >= 0; --ti) {
            const t = taskSlice[ti];
            if (remaining === 0) return false;
            
            // strongest available worker
            const maxIdx = bit.kth(remaining);
            const maxStrength = selectedWorkers[maxIdx];
            if (maxStrength >= t) {
                // assign without pill
                bit.add(maxIdx, -1);
                --remaining;
                continue;
            }
            
            // need a pill
            if (remainingPills === 0) return false;
            const needed = t - strength; // minimal base strength required after using a pill
            const pos = lowerBound(selectedWorkers, Math.max(needed, 0));
            const beforePos = bit.sum(pos); // workers strictly before pos still present
            if (remaining - beforePos === 0) return false; // no worker can satisfy even with pill
            
            // pick the weakest suitable worker (first after pos)
            const idx = bit.kth(beforePos + 1);
            bit.add(idx, -1);
            --remaining;
            --remainingPills;
        }
        return true;
    }
};
```

## Typescript

```typescript
function maxTaskAssign(tasks: number[], workers: number[], pills: number, strength: number): number {
    tasks.sort((a, b) => a - b);
    workers.sort((a, b) => a - b);
    const n = tasks.length;
    const m = workers.length;
    const maxK = Math.min(n, m);

    class TreapNode {
        key: number;
        priority: number;
        cnt: number;
        left: TreapNode | null = null;
        right: TreapNode | null = null;
        constructor(key: number) {
            this.key = key;
            this.priority = Math.random();
            this.cnt = 1;
        }
    }

    class Treap {
        root: TreapNode | null = null;

        private rotateRight(y: TreapNode): TreapNode {
            const x = y.left!;
            y.left = x.right;
            x.right = y;
            return x;
        }

        private rotateLeft(x: TreapNode): TreapNode {
            const y = x.right!;
            x.right = y.left;
            y.left = x;
            return y;
        }

        insert(key: number) {
            this.root = this._insert(this.root, key);
        }

        private _insert(node: TreapNode | null, key: number): TreapNode {
            if (!node) return new TreapNode(key);
            if (key === node.key) {
                node.cnt++;
                return node;
            }
            if (key < node.key) {
                node.left = this._insert(node.left, key);
                if (node.left!.priority < node.priority) {
                    node = this.rotateRight(node);
                }
            } else {
                node.right = this._insert(node.right, key);
                if (node.right!.priority < node.priority) {
                    node = this.rotateLeft(node);
                }
            }
            return node;
        }

        erase(key: number) {
            this.root = this._erase(this.root, key);
        }

        private _erase(node: TreapNode | null, key: number): TreapNode | null {
            if (!node) return null;
            if (key === node.key) {
                if (node.cnt > 1) {
                    node.cnt--;
                    return node;
                }
                // merge children
                return this._merge(node.left, node.right);
            } else if (key < node.key) {
                node.left = this._erase(node.left, key);
            } else {
                node.right = _erase(node.right, key);
            }
            return node;

            function _erase(n: TreapNode | null, k: number): TreapNode | null {
                if (!n) return null;
                if (k === n.key) {
                    if (n.cnt > 1) {
                        n.cnt--;
                        return n;
                    }
                    return merge(n.left, n.right);
                } else if (k < n.key) {
                    n.left = _erase(n.left, k);
                } else {
                    n.right = _erase(n.right, k);
                }
                return n;
            }

            function merge(a: TreapNode | null, b: TreapNode | null): TreapNode | null {
                if (!a) return b;
                if (!b) return a;
                if (a.priority < b.priority) {
                    a.right = merge(a.right, b);
                    return a;
                } else {
                    b.left = merge(a, b.left);
                    return b;
                }
            }
        }

        lowerBound(key: number): number | null {
            let node = this.root;
            let ans: number | null = null;
            while (node) {
                if (node.key >= key) {
                    ans = node.key;
                    node = node.left;
                } else {
                    node = node.right;
                }
            }
            return ans;
        }

        getMax(): number | null {
            let node = this.root;
            if (!node) return null;
            while (node.right) node = node.right;
            return node.key;
        }
    }

    function can(k: number): boolean {
        if (k === 0) return true;
        const treap = new Treap();
        // insert k strongest workers
        for (let i = m - k; i < m; ++i) {
            treap.insert(workers[i]);
        }
        let remainingPills = pills;
        for (let i = k - 1; i >= 0; --i) {
            const task = tasks[i];
            const maxWorker = treap.getMax();
            if (maxWorker !== null && maxWorker >= task) {
                treap.erase(maxWorker);
            } else {
                if (remainingPills === 0) return false;
                const need = task - strength;
                const cand = treap.lowerBound(need);
                if (cand === null) return false;
                treap.erase(cand);
                remainingPills--;
            }
        }
        return true;
    }

    let lo = 0, hi = maxK + 1;
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (can(mid)) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    return lo - 1;
}
```

## Php

```php
class BIT {
    public int $n;
    public array $tree;

    public function __construct(int $size) {
        $this->n = $size;
        $this->tree = array_fill(0, $size + 1, 0);
    }

    // index is 0‑based
    public function add(int $idx, int $delta): void {
        $i = $idx + 1;
        while ($i <= $this->n) {
            $this->tree[$i] += $delta;
            $i += $i & (-$i);
        }
    }

    // prefix sum [0..idx], idx can be -1
    public function sum(int $idx): int {
        if ($idx < 0) return 0;
        $res = 0;
        $i = $idx + 1;
        while ($i > 0) {
            $res += $this->tree[$i];
            $i -= $i & (-$i);
        }
        return $res;
    }

    // find smallest index such that prefix sum >= k (k is 1‑based)
    public function kth(int $k): int {
        $idx = 0;
        $bitMask = 1;
        while ($bitMask << 1 <= $this->n) $bitMask <<= 1;
        for (; $bitMask > 0; $bitMask >>= 1) {
            $next = $idx + $bitMask;
            if ($next <= $this->n && $this->tree[$next] < $k) {
                $idx = $next;
                $k -= $this->tree[$next];
            }
        }
        return $idx; // 0‑based index
    }
}

class Solution {

    /**
     * @param Integer[] $tasks
     * @param Integer[] $workers
     * @param Integer $pills
     * @param Integer $strength
     * @return Integer
     */
    function maxTaskAssign($tasks, $workers, $pills, $strength) {
        sort($tasks);
        sort($workers);
        $n = count($tasks);
        $m = count($workers);
        $low = 0;
        $high = min($n, $m);
        while ($low < $high) {
            $mid = intdiv($low + $high + 1, 2);
            if ($this->canAssign($tasks, $workers, $pills, $strength, $mid)) {
                $low = $mid;
            } else {
                $high = $mid - 1;
            }
        }
        return $low;
    }

    private function canAssign($tasks, $workers, $pills, $strength, $k): bool {
        if ($k == 0) return true;
        $taskSubset = array_slice($tasks, 0, $k); // smallest k tasks (already sorted asc)
        $workerStart = count($workers) - $k;      // index of first among strongest k workers
        $bit = new BIT($k);
        for ($i = 0; $i < $k; ++$i) {
            $bit->add($i, 1); // all workers initially available
        }
        $highIdx = $k - 1;
        $remainingPills = $pills;

        for ($ti = $k - 1; $ti >= 0; --$ti) { // process tasks from hardest to easiest
            $t = $taskSubset[$ti];

            // move highIdx to the next available worker if needed
            while ($highIdx >= 0 && $bit->sum($highIdx) - $bit->sum($highIdx - 1) == 0) {
                --$highIdx;
            }

            if ($highIdx >= 0 && $workers[$workerStart + $highIdx] >= $t) {
                // assign without pill
                $bit->add($highIdx, -1);
                --$highIdx;
                continue;
            }

            // need a pill
            if ($remainingPills == 0) return false;

            $need = $t - $strength;
            // find first position with strength >= need
            $pos = $this->lowerBound($workers, $workerStart, $k, $need);
            if ($pos == $k) return false; // no worker can reach even with pill

            $availableBeforePos = ($pos > 0) ? $bit->sum($pos - 1) : 0;
            $totalAvailable = $bit->sum($k - 1);
            if ($totalAvailable - $availableBeforePos <= 0) return false; // none left after pos

            // smallest available index >= pos
            $idx = $bit->kth($availableBeforePos + 1);
            $bit->add($idx, -1);
            --$remainingPills;

            if ($idx == $highIdx) {
                while ($highIdx >= 0 && $bit->sum($highIdx) - $bit->sum($highIdx - 1) == 0) {
                    --$highIdx;
                }
            }
        }

        return true;
    }

    // lower bound on subarray workers[start .. start+len-1] for value >= target
    private function lowerBound($arr, $start, $len, $target): int {
        $lo = 0;
        $hi = $len; // exclusive
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($arr[$start + $mid] >= $target) {
                $hi = $mid;
            } else {
                $lo = $mid + 1;
            }
        }
        return $lo; // may be $len
    }
}
```

## Swift

```swift
class Solution {
    var tasksSorted: [Int] = []
    var workersSorted: [Int] = []
    var strength: Int = 0
    var pillsTotal: Int = 0

    func maxTaskAssign(_ tasks: [Int], _ workers: [Int], _ pills: Int, _ strength: Int) -> Int {
        self.tasksSorted = tasks.sorted()
        self.workersSorted = workers.sorted()
        self.strength = strength
        self.pillsTotal = pills

        var low = 0
        var high = min(tasks.count, workers.count)
        while low < high {
            let mid = (low + high + 1) / 2
            if canAssign(mid) {
                low = mid
            } else {
                high = mid - 1
            }
        }
        return low
    }

    private func lowerBound(_ arr: [Int], _ target: Int) -> Int {
        var l = 0, r = arr.count
        while l < r {
            let m = (l + r) >> 1
            if arr[m] >= target { r = m } else { l = m + 1 }
        }
        return l
    }

    private func canAssign(_ k: Int) -> Bool {
        if k == 0 { return true }

        // strongest k workers
        let startIdx = workersSorted.count - k
        var selectedWorkers = [Int]()
        selectedWorkers.reserveCapacity(k)
        for i in startIdx..<workersSorted.count {
            selectedWorkers.append(workersSorted[i])
        }

        // distinct strengths
        var vals = [Int]()
        vals.reserveCapacity(selectedWorkers.count)
        for w in selectedWorkers {
            if vals.isEmpty || vals.last! != w { vals.append(w) }
        }
        let size = vals.count

        // BIT for frequencies
        let bit = BIT(size)
        var valueToIdx = [Int: Int](minimumCapacity: size)
        for (i, v) in vals.enumerated() {
            valueToIdx[v] = i
        }
        for w in selectedWorkers {
            if let idx = valueToIdx[w] {
                bit.add(idx, 1)
            }
        }

        var maxIdx = size - 1
        while maxIdx >= 0 && bit.rangeSum(maxIdx, maxIdx) == 0 { maxIdx -= 1 }

        var remainingPills = pillsTotal

        // assign tasks from hardest to easiest (among first k smallest tasks)
        for i in stride(from: k - 1, through: 0, by: -1) {
            let t = tasksSorted[i]

            if maxIdx >= 0 && vals[maxIdx] >= t {
                // use strongest worker without pill
                bit.add(maxIdx, -1)
                while maxIdx >= 0 && bit.rangeSum(maxIdx, maxIdx) == 0 { maxIdx -= 1 }
            } else {
                // need a pill
                if remainingPills == 0 { return false }
                let need = t - strength
                var idx: Int

                if need <= 0 {
                    // any worker works with pill; pick weakest available
                    idx = bit.kth(1)
                } else {
                    let pos = lowerBound(vals, need)
                    if pos == size { return false }
                    if bit.rangeSum(pos, size - 1) == 0 { return false }
                    let prefix = pos > 0 ? bit.sum(pos - 1) : 0
                    idx = bit.kth(prefix + 1)
                }

                bit.add(idx, -1)
                remainingPills -= 1
                while maxIdx >= 0 && bit.rangeSum(maxIdx, maxIdx) == 0 { maxIdx -= 1 }
            }
        }
        return true
    }
}

// Fenwick Tree (Binary Indexed Tree)
final class BIT {
    private let n: Int
    private var tree: [Int]

    init(_ n: Int) {
        self.n = n
        self.tree = Array(repeating: 0, count: n + 1)
    }

    func add(_ idx: Int, _ delta: Int) {
        var i = idx + 1
        while i <= n {
            tree[i] += delta
            i += i & -i
        }
    }

    func sum(_ idx: Int) -> Int {
        var res = 0
        var i = idx + 1
        while i > 0 {
            res += tree[i]
            i -= i & -i
        }
        return res
    }

    func rangeSum(_ l: Int, _ r: Int) -> Int {
        if r < l { return 0 }
        let right = sum(r)
        let left = l > 0 ? sum(l - 1) : 0
        return right - left
    }

    // smallest index with prefix sum >= k (k is 1‑based)
    func kth(_ k: Int) -> Int {
        var idx = 0
        var bitMask = 1
        while (bitMask << 1) <= n { bitMask <<= 1 }
        var curIdx = 0
        var curSum = 0
        var mask = bitMask
        while mask != 0 {
            let next = curIdx + mask
            if next <= n && curSum + tree[next] < k {
                curIdx = next
                curSum += tree[next]
            }
            mask >>= 1
        }
        return curIdx   // zero‑based index
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxTaskAssign(tasks: IntArray, workers: IntArray, pills: Int, strength: Int): Int {
        java.util.Arrays.sort(tasks)
        java.util.Arrays.sort(workers)
        val n = tasks.size
        val m = workers.size
        var low = 0
        var high = kotlin.math.min(n, m)

        fun can(k: Int): Boolean {
            if (k == 0) return true
            val map = java.util.TreeMap<Int, Int>()
            for (i in m - k until m) {
                val w = workers[i]
                map[w] = (map[w] ?: 0) + 1
            }
            var pillsLeft = pills
            for (idx in k - 1 downTo 0) {
                val task = tasks[idx]
                // Try without a pill: use the strongest available worker
                if (!map.isEmpty()) {
                    val maxWorker = map.lastKey()
                    if (maxWorker >= task) {
                        val cnt = map[maxWorker]!!
                        if (cnt == 1) map.remove(maxWorker) else map[maxWorker] = cnt - 1
                        continue
                    }
                }
                // Need a pill
                if (pillsLeft == 0) return false
                val needed = task - strength
                val key = map.ceilingKey(needed)
                if (key == null) return false
                val cnt = map[key]!!
                if (cnt == 1) map.remove(key) else map[key] = cnt - 1
                pillsLeft--
            }
            return true
        }

        while (low < high) {
            val mid = (low + high + 1) / 2
            if (can(mid)) low = mid else high = mid - 1
        }
        return low
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  int maxTaskAssign(List<int> tasks, List<int> workers, int pills, int strength) {
    tasks.sort();
    workers.sort();
    int n = tasks.length;
    int m = workers.length;
    int lo = 0, hi = n < m ? n : m;
    while (lo < hi) {
      int mid = (lo + hi + 1) >> 1;
      if (_canAssign(mid, tasks, workers, pills, strength)) {
        lo = mid;
      } else {
        hi = mid - 1;
      }
    }
    return lo;
  }

  bool _canAssign(int k, List<int> tasks, List<int> workers, int pills,
      int strength) {
    if (k == 0) return true;

    // smallest k tasks
    List<int> subTasks = tasks.sublist(0, k);

    // multiset of largest k workers
    SplayTreeMap<int, int> ms = SplayTreeMap<int, int>();
    int startIdx = workers.length - k;
    for (int i = startIdx; i < workers.length; ++i) {
      int w = workers[i];
      ms.update(w, (cnt) => cnt + 1, ifAbsent: () => 1);
    }

    int remainingPills = pills;

    // assign tasks from hardest to easiest
    for (int idx = k - 1; idx >= 0; --idx) {
      int t = subTasks[idx];

      if (ms.isNotEmpty && ms.lastKey! >= t) {
        // use strongest worker without pill
        int w = ms.lastKey!;
        int cnt = ms[w]!;
        if (cnt == 1) {
          ms.remove(w);
        } else {
          ms[w] = cnt - 1;
        }
      } else {
        // need a pill
        if (remainingPills == 0) return false;

        int needed = t - strength;
        if (needed <= 0) {
          // any worker works with pill, take the weakest
          if (ms.isEmpty) return false;
          int w = ms.firstKey!;
          int cnt = ms[w]!;
          if (cnt == 1) {
            ms.remove(w);
          } else {
            ms[w] = cnt - 1;
          }
        } else {
          // find smallest worker >= needed
          int? candidate;
          if (ms.containsKey(needed)) {
            candidate = needed;
          } else {
            candidate = ms.higherKey(needed);
          }
          if (candidate == null) return false;
          int cnt = ms[candidate]!;
          if (cnt == 1) {
            ms.remove(candidate);
          } else {
            ms[candidate] = cnt - 1;
          }
        }

        remainingPills--;
      }
    }

    return true;
  }
}
```

## Golang

```go
package main

import (
	"math/rand"
	"sort"
	"time"
)

type node struct {
	key        int
	priority   uint32
	cnt        int
	left, right *node
}

type treap struct {
	root *node
}

func newTreap() *treap { return &treap{} }

func (t *treap) rotateRight(p *node) *node {
	q := p.left
	p.left = q.right
	q.right = p
	return q
}

func (t *treap) rotateLeft(p *node) *node {
	q := p.right
	p.right = q.left
	q.left = p
	return q
}

func (t *treap) insertRec(cur *node, key int) *node {
	if cur == nil {
		return &node{key: key, priority: rand.Uint32(), cnt: 1}
	}
	if key == cur.key {
		cur.cnt++
		return cur
	}
	if key < cur.key {
		cur.left = t.insertRec(cur.left, key)
		if cur.left.priority > cur.priority {
			cur = t.rotateRight(cur)
		}
	} else {
		cur.right = t.insertRec(cur.right, key)
		if cur.right.priority > cur.priority {
			cur = t.rotateLeft(cur)
		}
	}
	return cur
}

func (t *treap) Insert(key int) {
	t.root = t.insertRec(t.root, key)
}

func (t *treap) merge(a, b *node) *node {
	if a == nil {
		return b
	}
	if b == nil {
		return a
	}
	if a.priority > b.priority {
		a.right = t.merge(a.right, b)
		return a
	}
	b.left = t.merge(a, b.left)
	return b
}

func (t *treap) eraseRec(cur *node, key int) *node {
	if cur == nil {
		return nil
	}
	if key == cur.key {
		cur.cnt--
		if cur.cnt == 0 {
			return t.merge(cur.left, cur.right)
		}
		return cur
	}
	if key < cur.key {
		cur.left = t.eraseRec(cur.left, key)
	} else {
		cur.right = t.eraseRec(cur.right, key)
	}
	return cur
}

func (t *treap) Erase(key int) {
	t.root = t.eraseRec(t.root, key)
}

// lower bound: smallest key >= x, -1 if none
func (t *treap) lowerBound(x int) int {
	cur := t.root
	ans := -1
	for cur != nil {
		if cur.key >= x {
			ans = cur.key
			cur = cur.left
		} else {
			cur = cur.right
		}
	}
	return ans
}

// max key in treap, -1 if empty
func (t *treap) Max() int {
	if t.root == nil {
		return -1
	}
	cur := t.root
	for cur.right != nil {
		cur = cur.right
	}
	return cur.key
}

func maxTaskAssign(tasks []int, workers []int, pills int, strength int) int {
	rand.Seed(time.Now().UnixNano())
	sort.Ints(tasks)
	sort.Ints(workers)

	n := len(tasks)
	m := len(workers)
	limit := n
	if m < limit {
		limit = m
	}

	can := func(k int) bool {
		if k == 0 {
			return true
		}
		ts := tasks[:k] // smallest k tasks, already sorted asc
		ws := workers[m-k:] // largest k workers, sorted asc

		tr := newTreap()
		for _, w := range ws {
			tr.Insert(w)
		}

		remainingPills := pills
		// process tasks from hardest to easiest
		for i := k - 1; i >= 0; i-- {
			tval := ts[i]
			maxW := tr.Max()
			if maxW >= tval {
				tr.Erase(maxW)
				continue
			}
			if remainingPills == 0 {
				return false
			}
			need := tval - strength
			if need < 0 {
				need = 0
			}
			w := tr.lowerBound(need)
			if w == -1 {
				return false
			}
			tr.Erase(w)
			remainingPills--
		}
		return true
	}

	lo, hi := 0, limit
	for lo < hi {
		mid := (lo + hi + 1) / 2
		if can(mid) {
			lo = mid
		} else {
			hi = mid - 1
		}
	}
	return lo
}
```

## Ruby

```ruby
class BIT
  def initialize(n)
    @n = n
    @bit = Array.new(n + 2, 0)
    @max_pow = 1
    while @max_pow <= n
      @max_pow <<= 1
    end
  end

  def add(idx, delta) # idx: 0-based
    i = idx + 1
    while i <= @n
      @bit[i] += delta
      i += i & -i
    end
  end

  def sum(idx) # prefix sum up to idx inclusive; idx < 0 => 0
    return 0 if idx < 0
    i = idx + 1
    res = 0
    while i > 0
      res += @bit[i]
      i -= i & -i
    end
    res
  end

  def total
    sum(@n - 1)
  end

  # smallest index such that prefix sum >= k (k >= 1), returns 0‑based index
  def kth(k)
    idx = 0
    bitmask = @max_pow
    while bitmask > 0
      t = idx + bitmask
      if t <= @n && @bit[t] < k
        idx = t
        k -= @bit[t]
      end
      bitmask >>= 1
    end
    idx # 0‑based index where prefix sum >= original k
  end
end

# @param {Integer[]} tasks
# @param {Integer[]} workers
# @param {Integer} pills
# @param {Integer} strength
# @return {Integer}
def max_task_assign(tasks, workers, pills, strength)
  tasks.sort!
  workers.sort!
  n = tasks.length
  m = workers.length

  vals = workers.uniq
  idx_map = {}
  vals.each_with_index { |v, i| idx_map[v] = i }

  feasible = lambda do |k|
    return true if k == 0
    sub_tasks = tasks[0, k]

    bit = BIT.new(vals.length)
    workers.each { |w| bit.add(idx_map[w], 1) }

    remaining_workers = m
    remaining_pills = pills

    sub_tasks.reverse_each do |t|
      return false if remaining_workers == 0

      idx_max = bit.kth(remaining_workers)
      max_strength = vals[idx_max]

      if max_strength >= t
        bit.add(idx_max, -1)
        remaining_workers -= 1
      else
        return false if remaining_pills == 0
        need = t - strength
        lb = vals.bsearch_index { |v| v >= need }
        return false if lb.nil?

        count_before = bit.sum(lb - 1)
        if remaining_workers - count_before <= 0
          return false
        end

        idx_use = bit.kth(count_before + 1)
        bit.add(idx_use, -1)
        remaining_workers -= 1
        remaining_pills -= 1
      end
    end
    true
  end

  low = 0
  high = [n, m].min
  while low < high
    mid = (low + high + 1) / 2
    if feasible.call(mid)
      low = mid
    else
      high = mid - 1
    end
  end
  low
end
```

## Scala

```scala
import java.util.TreeMap

object Solution {
  def maxTaskAssign(tasks: Array[Int], workers: Array[Int], pills: Int, strength: Int): Int = {
    val tasksSorted = tasks.sorted
    val workersSorted = workers.sorted
    val n = tasks.length
    val m = workers.length
    val maxK = Math.min(n, m)

    def decrement(map: TreeMap[Int, Int], key: Int): Unit = {
      val cnt = map.get(key)
      if (cnt == 1) map.remove(key) else map.put(key, cnt - 1)
    }

    def can(k: Int): Boolean = {
      var pillsLeft = pills
      val workerMap = new TreeMap[Int, Int]()
      var i = m - k
      while (i < m) {
        val w = workersSorted(i)
        workerMap.put(w, workerMap.getOrDefault(w, 0) + 1)
        i += 1
      }
      var idx = k - 1
      while (idx >= 0) {
        val t = tasksSorted(idx)
        if (!workerMap.isEmpty && workerMap.lastKey() >= t) {
          val w = workerMap.lastKey()
          decrement(workerMap, w)
        } else {
          if (pillsLeft == 0) return false
          val need = t - strength
          val keyObj: java.lang.Integer = workerMap.ceilingKey(need)
          if (keyObj == null) return false
          val key = keyObj.intValue()
          decrement(workerMap, key)
          pillsLeft -= 1
        }
        idx -= 1
      }
      true
    }

    var lo = 0
    var hi = maxK
    while (lo < hi) {
      val mid = (lo + hi + 1) >>> 1
      if (can(mid)) lo = mid else hi = mid - 1
    }
    lo
  }
}
```

## Rust

```rust
use std::collections::BTreeMap;

impl Solution {
    pub fn max_task_assign(tasks: Vec<i32>, workers: Vec<i32>, pills: i32, strength: i32) -> i32 {
        let mut tasks = tasks;
        let mut workers = workers;
        tasks.sort_unstable();
        workers.sort_unstable();

        let n = tasks.len();
        let m = workers.len();
        let max_possible = std::cmp::min(n, m);
        let mut lo: usize = 0;
        let mut hi: usize = max_possible;

        while lo < hi {
            let mid = (lo + hi + 1) / 2;
            if Self::can_assign(mid, &tasks, &workers, pills, strength) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }

        lo as i32
    }

    fn can_assign(k: usize, tasks: &[i32], workers: &[i32], pills: i32, strength: i32) -> bool {
        if k == 0 {
            return true;
        }
        // multiset of the k strongest workers
        let mut multiset: BTreeMap<i32, usize> = BTreeMap::new();
        for &w in workers.iter().rev().take(k) {
            *multiset.entry(w).or_insert(0) += 1;
        }

        let mut pills_left = pills;

        // process the k smallest tasks from hardest to easiest
        for i in (0..k).rev() {
            let t = tasks[i];
            // get current strongest worker
            if let Some((&max_worker, _)) = multiset.iter().next_back() {
                if max_worker >= t {
                    // assign without pill
                    Self::decrease(&mut multiset, max_worker);
                    continue;
                }
            }

            // need a pill
            if pills_left == 0 {
                return false;
            }
            let needed = t - strength; // may be negative
            // find the weakest worker that can do it with a pill
            if let Some((&candidate, _)) = multiset.range(needed..).next() {
                pills_left -= 1;
                Self::decrease(&mut multiset, candidate);
            } else {
                return false;
            }
        }

        true
    }

    fn decrease(map: &mut BTreeMap<i32, usize>, key: i32) {
        if let Some(cnt) = map.get_mut(&key) {
            *cnt -= 1;
            if *cnt == 0 {
                map.remove(&key);
            }
        }
    }
}
```

## Racket

```racket
(require racket/list)
(require racket/rbtree)

(define (max-task-assign tasks workers pills strength)
  (let* ([tasks-sorted (sort tasks <)]
         [workers-sorted (sort workers <)]
         [n (length tasks-sorted)]
         [m (length workers-sorted)])
    (define (can? k)
      (let* ([task-list (take tasks-sorted k)]
             [worker-list (drop workers-sorted (- m k))]
             [tree (make-rb-tree <)])
        ;; insert workers with counts
        (for ([w worker-list])
          (let ([cnt (rb-lookup tree w 0)])
            (rb-insert! tree w (+ cnt 1))))
        (define remaining-pills pills)
        (let loop ((i (- k 1)))
          (if (< i 0)
              #t
              (let* ([t (list-ref task-list i)]
                     [max-key (and (not (rb-empty? tree)) (rb-max-key tree))])
                (cond
                  [(and max-key (>= max-key t))
                   ;; use strongest worker without pill
                   (let ([cnt (rb-lookup tree max-key)])
                     (if (= cnt 1)
                         (rb-delete! tree max-key)
                         (rb-insert! tree max-key (- cnt 1))))
                   (loop (- i 1))]
                  [else
                   (if (zero? remaining-pills)
                       #f
                       (let* ([need (- t strength)]
                              [candidate (and (not (rb-empty? tree))
                                              (rb-least-greater-or-equal tree need))])
                         (if candidate
                             (begin
                               (let ([cnt (rb-lookup tree candidate)])
                                 (if (= cnt 1)
                                     (rb-delete! tree candidate)
                                     (rb-insert! tree candidate (- cnt 1))))
                               (set! remaining-pills (- remaining-pills 1))
                               (loop (- i 1)))
                             #f))))))))) )
    ;; binary search for maximum feasible k
    (let loop ((lo 0) (hi (min n m)))
      (if (= lo hi)
          lo
          (let* ([mid (+ lo (quotient (+ (- hi lo) 1) 2))])
            (if (can? mid)
                (loop mid hi)
                (loop lo (- mid 1))))))))
```

## Erlang

```erlang
-spec max_task_assign(Tasks :: [integer()], Workers :: [integer()], Pills :: integer(), Strength :: integer()) -> integer().
max_task_assign(Tasks, Workers, Pills, Strength) ->
    TasksSorted = lists:sort(Tasks),
    WorkersSorted = lists:sort(Workers),
    MaxK = min(length(TasksSorted), length(WorkersSorted)),
    binary_search(0, MaxK, TasksSorted, WorkersSorted, Pills, Strength).

binary_search(Low, High, _TS, _WS, _P, _S) when Low >= High ->
    Low;
binary_search(Low, High, TS, WS, P, S) ->
    Mid = (Low + High + 1) div 2,
    case feasible_k(Mid, TS, WS, P, S) of
        true -> binary_search(Mid, High, TS, WS, P, S);
        false -> binary_search(Low, Mid - 1, TS, WS, P, S)
    end.

feasible_k(0, _TS, _WS, _P, _S) ->
    true;
feasible_k(K, TasksSorted, WorkersSorted, Pills, Strength) ->
    TasksK = lists:sublist(TasksSorted, K),
    TasksDesc = lists:reverse(TasksK),

    LenW = length(WorkersSorted),
    WorkersK = lists:nthtail(LenW - K, WorkersSorted),

    Tree0 = build_tree(WorkersK),
    feasible_tasks(TasksDesc, Tree0, Pills, Strength).

build_tree(Workers) ->
    lists:foldl(fun(W, Acc) -> add_worker(Acc, W) end, gb_trees:empty(), Workers).

add_worker(Tree, W) ->
    case gb_trees:lookup(W, Tree) of
        {value, C} -> gb_trees:update(W, C + 1, Tree);
        none -> gb_trees:insert(W, 1, Tree)
    end.

remove_worker(Tree, W) ->
    case gb_trees:lookup(W, Tree) of
        {value, 1} -> gb_trees:delete(W, Tree);
        {value, C} -> gb_trees:update(W, C - 1, Tree)
    end.

feasible_tasks([], _Tree, _Pills, _Strength) ->
    true;
feasible_tasks([T | Rest], Tree, Pills, Strength) ->
    case gb_trees:is_empty(Tree) of
        true -> false;
        false ->
            {MaxW, _} = gb_trees:largest(Tree),
            if MaxW >= T ->
                    NewTree = remove_worker(Tree, MaxW),
                    feasible_tasks(Rest, NewTree, Pills, Strength);
               true ->
                    Needed = T - Strength,
                    case Pills > 0 of
                        false -> false;
                        true ->
                            Need = if Needed < 0 -> 0; true -> Needed end,
                            Iterator = gb_trees:iterator_from(Need, Tree),
                            case gb_trees:next(Iterator) of
                                none -> false;
                                {W, _, _} ->
                                    NewTree = remove_worker(Tree, W),
                                    feasible_tasks(Rest, NewTree, Pills - 1, Strength)
                            end
                    end
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_task_assign(tasks :: [integer], workers :: [integer], pills :: integer, strength :: integer) :: integer
  def max_task_assign(tasks, workers, pills, strength) do
    tasks_sorted = Enum.sort(tasks)
    workers_sorted = Enum.sort(workers)

    max_k = min(length(tasks_sorted), length(workers_sorted))
    binary_search(0, max_k, tasks_sorted, workers_sorted, pills, strength)
  end

  defp binary_search(l, r, _tasks, _workers, _pills, _strength) when l >= r, do: l

  defp binary_search(l, r, tasks, workers, pills, strength) do
    mid = div(l + r + 1, 2)

    if feasible?(tasks, workers, mid, pills, strength) do
      binary_search(mid, r, tasks, workers, pills, strength)
    else
      binary_search(l, mid - 1, tasks, workers, pills, strength)
    end
  end

  defp feasible?(tasks_sorted, workers_sorted, k, pills, strength) do
    # take k smallest tasks and process them from hardest to easiest
    tasks = tasks_sorted |> Enum.take(k) |> Enum.reverse()

    # take k strongest workers
    start_idx = length(workers_sorted) - k
    selected_workers = Enum.slice(workers_sorted, start_idx, k)

    tree = Enum.reduce(selected_workers, :gb_trees.empty(), fn w, acc -> insert(acc, w) end)
    assign_tasks(tasks, tree, pills, strength)
  end

  defp assign_tasks([], _tree, _pills_left, _strength), do: true

  defp assign_tasks([t | rest], tree, pills_left, strength) do
    if :gb_trees.is_empty(tree) do
      false
    else
      {max_key, _cnt} = :gb_trees.max(tree)

      cond do
        max_key >= t ->
          tree2 = delete_one(tree, max_key)
          assign_tasks(rest, tree2, pills_left, strength)

        true ->
          if pills_left == 0 do
            false
          else
            needed = t - strength
            needed = if needed < 0, do: 0, else: needed

            iter = :gb_trees.iterator_from(needed, tree)

            case :gb_trees.next(iter) do
              {key, _cnt2, _next} ->
                tree2 = delete_one(tree, key)
                assign_tasks(rest, tree2, pills_left - 1, strength)

              :none ->
                false
            end
          end
      end
    end
  end

  defp insert(tree, val) do
    case :gb_trees.lookup(val, tree) do
      :none -> :gb_trees.insert(val, 1, tree)
      {:value, cnt} -> :gb_trees.update(val, cnt + 1, tree)
    end
  end

  defp delete_one(tree, key) do
    case :gb_trees.lookup(key, tree) do
      {:value, 1} -> :gb_trees.delete(key, tree)
      {:value, cnt} -> :gb_trees.update(key, cnt - 1, tree)
      :none -> tree
    end
  end
end
```
