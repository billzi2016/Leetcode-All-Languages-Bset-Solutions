# 2462. Total Cost to Hire K Workers

## Cpp

```cpp
class Solution {
public:
    struct Node {
        int cost;
        int idx;
    };
    struct Compare {
        bool operator()(const Node& a, const Node& b) const {
            if (a.cost != b.cost) return a.cost > b.cost; // min-heap by cost
            return a.idx > b.idx; // tie-breaker by smaller index
        }
    };
    
    long long totalCost(vector<int>& costs, int k, int candidates) {
        int n = costs.size();
        if (k == 0) return 0LL;
        
        int leftEnd = min(candidates, n) - 1;                 // last index included in left heap
        int rightStart = max(n - candidates, leftEnd + 1);    // first index included in right heap
        
        priority_queue<Node, vector<Node>, Compare> leftHeap, rightHeap;
        
        for (int i = 0; i <= leftEnd; ++i) {
            leftHeap.push({costs[i], i});
        }
        for (int i = rightStart; i < n; ++i) {
            rightHeap.push({costs[i], i});
        }
        
        int nextLeft = leftEnd + 1;      // next index to possibly add from the left side
        int nextRight = rightStart - 1;  // next index to possibly add from the right side
        
        long long total = 0;
        for (int hired = 0; hired < k; ++hired) {
            bool takeLeft;
            if (leftHeap.empty()) {
                takeLeft = false;
            } else if (rightHeap.empty()) {
                takeLeft = true;
            } else {
                const Node& l = leftHeap.top();
                const Node& r = rightHeap.top();
                if (l.cost < r.cost) takeLeft = true;
                else if (l.cost > r.cost) takeLeft = false;
                else takeLeft = l.idx < r.idx; // tie-breaker by index, left side always smaller
            }
            
            if (takeLeft) {
                Node cur = leftHeap.top(); leftHeap.pop();
                total += cur.cost;
                if (nextLeft <= nextRight) {
                    leftHeap.push({costs[nextLeft], nextLeft});
                    ++nextLeft;
                }
            } else {
                Node cur = rightHeap.top(); rightHeap.pop();
                total += cur.cost;
                if (nextLeft <= nextRight) {
                    rightHeap.push({costs[nextRight], nextRight});
                    --nextRight;
                }
            }
        }
        return total;
    }
};
```

## Java

```java
class Solution {
    public long totalCost(int[] costs, int k, int candidates) {
        int n = costs.length;
        // Min-heap: first by cost, then by index
        java.util.PriorityQueue<int[]> left = new java.util.PriorityQueue<>(
            (a, b) -> a[0] != b[0] ? Integer.compare(a[0], b[0]) : Integer.compare(a[1], b[1])
        );
        java.util.PriorityQueue<int[]> right = new java.util.PriorityQueue<>(
            (a, b) -> a[0] != b[0] ? Integer.compare(a[0], b[0]) : Integer.compare(a[1], b[1])
        );

        int i = 0, j = n - 1;
        // Fill left candidates
        for (int cnt = 0; cnt < candidates && i <= j; cnt++) {
            left.offer(new int[]{costs[i], i});
            i++;
        }
        // Fill right candidates
        for (int cnt = 0; cnt < candidates && i <= j; cnt++) {
            right.offer(new int[]{costs[j], j});
            j--;
        }

        long total = 0L;
        for (int hired = 0; hired < k; hired++) {
            if (right.isEmpty() || (!left.isEmpty() && left.peek()[0] <= right.peek()[0])) {
                int[] cur = left.poll();
                total += cur[0];
                if (i <= j) {
                    left.offer(new int[]{costs[i], i});
                    i++;
                }
            } else {
                int[] cur = right.poll();
                total += cur[0];
                if (i <= j) {
                    right.offer(new int[]{costs[j], j});
                    j--;
                }
            }
        }

        return total;
    }
}
```

## Python

```python
import heapq

class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """
        n = len(costs)
        left_heap = []
        right_heap = []
        l, r = 0, n - 1

        # initialize left candidates
        for _ in range(candidates):
            if l > r:
                break
            heapq.heappush(left_heap, (costs[l], l))
            l += 1

        # initialize right candidates
        for _ in range(candidates):
            if l > r:
                break
            heapq.heappush(right_heap, (costs[r], r))
            r -= 1

        total = 0
        for _ in range(k):
            if not left_heap:
                cost, idx = heapq.heappop(right_heap)
                total += cost
                if l <= r:
                    heapq.heappush(right_heap, (costs[r], r))
                    r -= 1
            elif not right_heap:
                cost, idx = heapq.heappop(left_heap)
                total += cost
                if l <= r:
                    heapq.heappush(left_heap, (costs[l], l))
                    l += 1
            else:
                left_top = left_heap[0][0]
                right_top = right_heap[0][0]
                if left_top < right_top:
                    cost, idx = heapq.heappop(left_heap)
                    total += cost
                    if l <= r:
                        heapq.heappush(left_heap, (costs[l], l))
                        l += 1
                elif left_top > right_top:
                    cost, idx = heapq.heappop(right_heap)
                    total += cost
                    if l <= r:
                        heapq.heappush(right_heap, (costs[r], r))
                        r -= 1
                else:  # equal costs, choose smaller index -> left side
                    cost, idx = heapq.heappop(left_heap)
                    total += cost
                    if l <= r:
                        heapq.heappush(left_heap, (costs[l], l))
                        l += 1

        return total
```

## Python3

```python
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        import heapq
        n = len(costs)
        left_heap = []
        right_heap = []
        i, j = 0, n - 1

        # initial fill for left side
        for _ in range(candidates):
            if i > j:
                break
            heapq.heappush(left_heap, (costs[i], i))
            i += 1
        # initial fill for right side
        for _ in range(candidates):
            if i > j:
                break
            heapq.heappush(right_heap, (costs[j], j))
            j -= 1

        total = 0
        for _ in range(k):
            if left_heap and right_heap:
                # compare by cost then index (tuple ordering)
                if left_heap[0] <= right_heap[0]:
                    cost, _ = heapq.heappop(left_heap)
                    total += cost
                    if i <= j:
                        heapq.heappush(left_heap, (costs[i], i))
                        i += 1
                else:
                    cost, _ = heapq.heappop(right_heap)
                    total += cost
                    if i <= j:
                        heapq.heappush(right_heap, (costs[j], j))
                        j -= 1
            elif left_heap:
                cost, _ = heapq.heappop(left_heap)
                total += cost
                if i <= j:
                    heapq.heappush(left_heap, (costs[i], i))
                    i += 1
            else:  # only right heap has elements
                cost, _ = heapq.heappop(right_heap)
                total += cost
                if i <= j:
                    heapq.heappush(right_heap, (costs[j], j))
                    j -= 1

        return total
```

## C

```c
#include <stdlib.h>
#include <limits.h>

typedef struct {
    int cost;
    int idx;
} Node;

typedef struct {
    Node *a;
    int size;
    int cap;
} Heap;

/* compare two nodes: return 1 if n1 has higher priority (smaller) than n2 */
static int better(const Node *n1, const Node *n2) {
    if (n1->cost != n2->cost) return n1->cost < n2->cost;
    return n1->idx < n2->idx;
}

static Heap* heapCreate(int cap) {
    Heap *h = (Heap*)malloc(sizeof(Heap));
    h->a = (Node*)malloc(sizeof(Node) * cap);
    h->size = 0;
    h->cap = cap;
    return h;
}

static void heapSwap(Node *x, Node *y) {
    Node t = *x; *x = *y; *y = t;
}

static void heapPush(Heap *h, Node v) {
    int i = h->size++;
    h->a[i] = v;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (better(&h->a[p], &h->a[i])) break;
        heapSwap(&h->a[p], &h->a[i]);
        i = p;
    }
}

static Node heapTop(const Heap *h) {
    return h->a[0];
}

static void heapPop(Heap *h) {
    if (h->size == 0) return;
    h->a[0] = h->a[--h->size];
    int i = 0;
    while (1) {
        int l = i * 2 + 1, r = l + 1, smallest = i;
        if (l < h->size && !better(&h->a[smallest], &h->a[l])) smallest = l;
        if (r < h->size && !better(&h->a[smallest], &h->a[r])) smallest = r;
        if (smallest == i) break;
        heapSwap(&h->a[i], &h->a[smallest]);
        i = smallest;
    }
}

/* main function */
long long totalCost(int* costs, int costsSize, int k, int candidates) {
    int n = costsSize;
    Heap *leftHeap = heapCreate(n);
    Heap *rightHeap = heapCreate(n);

    int leftPtr = 0, rightPtr = n - 1;

    /* initial fill */
    for (int i = 0; i < candidates && leftPtr <= rightPtr; ++i) {
        Node nd = {costs[leftPtr], leftPtr};
        heapPush(leftHeap, nd);
        ++leftPtr;
    }
    for (int i = 0; i < candidates && leftPtr <= rightPtr; ++i) {
        Node nd = {costs[rightPtr], rightPtr};
        heapPush(rightHeap, nd);
        --rightPtr;
    }

    long long total = 0;

    for (int hired = 0; hired < k; ++hired) {
        int takeLeft = 0; /* 1 if we take from leftHeap */
        if (leftHeap->size == 0) {
            takeLeft = 0;
        } else if (rightHeap->size == 0) {
            takeLeft = 1;
        } else {
            Node ltop = heapTop(leftHeap);
            Node rtop = heapTop(rightHeap);
            if (ltop.cost < rtop.cost) takeLeft = 1;
            else if (ltop.cost > rtop.cost) takeLeft = 0;
            else { /* equal cost, tie by smaller index -> left side has smaller indices */
                takeLeft = 1;
            }
        }

        if (takeLeft) {
            Node cur = heapTop(leftHeap);
            total += cur.cost;
            heapPop(leftHeap);
            if (leftPtr <= rightPtr) {
                Node nd = {costs[leftPtr], leftPtr};
                heapPush(leftHeap, nd);
                ++leftPtr;
            }
        } else {
            Node cur = heapTop(rightHeap);
            total += cur.cost;
            heapPop(rightHeap);
            if (leftPtr <= rightPtr) {
                Node nd = {costs[rightPtr], rightPtr};
                heapPush(rightHeap, nd);
                --rightPtr;
            }
        }
    }

    free(leftHeap->a);
    free(rightHeap->a);
    free(leftHeap);
    free(rightHeap);
    return total;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public long TotalCost(int[] costs, int k, int candidates) {
        int n = costs.Length;
        int leftPtr = 0;
        int rightPtr = n - 1;

        var leftHeap = new PriorityQueue<int, long>();
        var rightHeap = new PriorityQueue<int, long>();

        // Initialize left heap
        for (int i = 0; i < candidates && leftPtr <= rightPtr; ++i) {
            leftHeap.Enqueue(leftPtr, ((long)costs[leftPtr] << 32) | (uint)leftPtr);
            leftPtr++;
        }
        // Initialize right heap
        for (int i = 0; i < candidates && leftPtr <= rightPtr; ++i) {
            rightHeap.Enqueue(rightPtr, ((long)costs[rightPtr] << 32) | (uint)rightPtr);
            rightPtr--;
        }

        long total = 0L;
        for (int hired = 0; hired < k; ++hired) {
            bool takeLeft;
            if (leftHeap.Count == 0) {
                takeLeft = false;
            } else if (rightHeap.Count == 0) {
                takeLeft = true;
            } else {
                int leftIdx = leftHeap.Peek();
                int rightIdx = rightHeap.Peek();
                if (costs[leftIdx] < costs[rightIdx]) {
                    takeLeft = true;
                } else if (costs[leftIdx] > costs[rightIdx]) {
                    takeLeft = false;
                } else {
                    // tie by smaller index
                    takeLeft = leftIdx < rightIdx;
                }
            }

            if (takeLeft) {
                int idx = leftHeap.Dequeue();
                total += costs[idx];
                if (leftPtr <= rightPtr) {
                    leftHeap.Enqueue(leftPtr, ((long)costs[leftPtr] << 32) | (uint)leftPtr);
                    leftPtr++;
                }
            } else {
                int idx = rightHeap.Dequeue();
                total += costs[idx];
                if (leftPtr <= rightPtr) {
                    rightHeap.Enqueue(rightPtr, ((long)costs[rightPtr] << 32) | (uint)rightPtr);
                    rightPtr--;
                }
            }
        }

        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} costs
 * @param {number} k
 * @param {number} candidates
 * @return {number}
 */
var totalCost = function(costs, k, candidates) {
    class MinHeap {
        constructor(compare) {
            this.data = [];
            this.compare = compare || ((a, b) => a - b);
        }
        size() { return this.data.length; }
        peek() { return this.data[0]; }
        push(item) {
            const d = this.data;
            d.push(item);
            this._siftUp(d.length - 1);
        }
        pop() {
            const d = this.data;
            if (d.length === 0) return undefined;
            const top = d[0];
            const last = d.pop();
            if (d.length > 0) {
                d[0] = last;
                this._siftDown(0);
            }
            return top;
        }
        _siftUp(i) {
            const d = this.data, cmp = this.compare;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (cmp(d[i], d[p]) < 0) {
                    [d[i], d[p]] = [d[p], d[i]];
                    i = p;
                } else break;
            }
        }
        _siftDown(i) {
            const d = this.data, cmp = this.compare;
            const n = d.length;
            while (true) {
                let l = i * 2 + 1;
                let r = l + 1;
                let smallest = i;
                if (l < n && cmp(d[l], d[smallest]) < 0) smallest = l;
                if (r < n && cmp(d[r], d[smallest]) < 0) smallest = r;
                if (smallest !== i) {
                    [d[i], d[smallest]] = [d[smallest], d[i]];
                    i = smallest;
                } else break;
            }
        }
    }

    const n = costs.length;
    let left = 0, right = n - 1;

    const leftHeap = new MinHeap((a, b) => a[0] - b[0]);   // [cost, index]
    const rightHeap = new MinHeap((a, b) => a[0] - b[0]);

    // Fill initial candidates from the left side
    for (let cnt = 0; cnt < candidates && left <= right; cnt++) {
        leftHeap.push([costs[left], left]);
        left++;
    }
    // Fill initial candidates from the right side
    for (let cnt = 0; cnt < candidates && left <= right; cnt++) {
        rightHeap.push([costs[right], right]);
        right--;
    }

    let total = 0;
    for (let hired = 0; hired < k; hired++) {
        // Decide from which heap to take
        if (rightHeap.size() === 0 ||
            (leftHeap.size() > 0 && leftHeap.peek()[0] <= rightHeap.peek()[0])) {
            const [c, idx] = leftHeap.pop();
            total += c;
            if (left <= right) {
                leftHeap.push([costs[left], left]);
                left++;
            }
        } else {
            const [c, idx] = rightHeap.pop();
            total += c;
            if (left <= right) {
                rightHeap.push([costs[right], right]);
                right--;
            }
        }
    }

    return total;
};
```

## Typescript

```typescript
function totalCost(costs: number[], k: number, candidates: number): number {
    const n = costs.length;

    class Heap {
        private data: [number, number][] = [];
        constructor(private cmp: (a: [number, number], b: [number, number]) => boolean) {}
        size(): number { return this.data.length; }
        peek(): [number, number] | undefined { return this.data[0]; }
        push(item: [number, number]): void {
            const a = this.data;
            a.push(item);
            let i = a.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (this.cmp(a[p], a[i])) break; // parent has higher priority
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
                    let l = i * 2 + 1,
                        r = l + 1,
                        best = i;
                    if (l < a.length && !this.cmp(a[best], a[l])) best = l;
                    if (r < a.length && !this.cmp(a[best], a[r])) best = r;
                    if (best === i) break;
                    [a[i], a[best]] = [a[best], a[i]];
                    i = best;
                }
            }
            return top;
        }
    }

    const cmp = (a: [number, number], b: [number, number]): boolean => {
        if (a[0] !== b[0]) return a[0] < b[0];
        return a[1] < b[1];
    };

    const leftHeap = new Heap(cmp);
    const rightHeap = new Heap(cmp);

    let leftPtr = 0;
    let rightPtr = n - 1;

    // initial candidates from the left side
    for (let i = 0; i < candidates && leftPtr <= rightPtr; ++i) {
        leftHeap.push([costs[leftPtr], leftPtr]);
        ++leftPtr;
    }
    // initial candidates from the right side
    for (let i = 0; i < candidates && leftPtr <= rightPtr; ++i) {
        rightHeap.push([costs[rightPtr], rightPtr]);
        --rightPtr;
    }

    let total = 0;

    for (let hired = 0; hired < k; ++hired) {
        let takeFromLeft: boolean;
        if (leftHeap.size() === 0) {
            takeFromLeft = false;
        } else if (rightHeap.size() === 0) {
            takeFromLeft = true;
        } else {
            const leftTop = leftHeap.peek()!;
            const rightTop = rightHeap.peek()!;
            if (leftTop[0] < rightTop[0]) takeFromLeft = true;
            else if (leftTop[0] > rightTop[0]) takeFromLeft = false;
            else takeFromLeft = true; // tie -> smaller index, which is in left heap
        }

        const node = takeFromLeft ? leftHeap.pop()! : rightHeap.pop()!;
        total += node[0];

        if (leftPtr <= rightPtr) {
            if (takeFromLeft) {
                leftHeap.push([costs[leftPtr], leftPtr]);
                ++leftPtr;
            } else {
                rightHeap.push([costs[rightPtr], rightPtr]);
                --rightPtr;
            }
        }
    }

    return total;
}
```

## Php

```php
class MinHeap extends SplPriorityQueue {
    public function compare($p1, $p2) {
        // $p1 and $p2 are arrays [cost, index]
        if ($p1[0] === $p2[0]) {
            // smaller index has higher priority
            return $p2[1] <=> $p1[1];
        }
        // smaller cost has higher priority
        return $p2[0] <=> $p1[0];
    }
}

class Solution {

    /**
     * @param Integer[] $costs
     * @param Integer $k
     * @param Integer $candidates
     * @return Integer
     */
    function totalCost($costs, $k, $candidates) {
        $n = count($costs);
        $leftHeap = new MinHeap();
        $rightHeap = new MinHeap();
        $leftHeap->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        $rightHeap->setExtractFlags(SplPriorityQueue::EXTR_DATA);

        // initial fill for left side
        $leftCount = min($candidates, $n);
        for ($i = 0; $i < $leftCount; ++$i) {
            $item = [$costs[$i], $i];
            $leftHeap->insert($item, $item);
        }

        // initial fill for right side without overlapping
        $rightStart = max($n - $candidates, $leftCount);
        for ($i = $rightStart; $i < $n; ++$i) {
            $item = [$costs[$i], $i];
            $rightHeap->insert($item, $item);
        }

        $nextHead = $leftCount;
        $nextTail = $rightStart - 1;

        $total = 0;
        for ($hired = 0; $hired < $k; ++$hired) {
            if ($leftHeap->isEmpty()) {
                // take from right
                $chosen = $rightHeap->extract();
                $total += $chosen[0];
                if ($nextHead <= $nextTail) {
                    $item = [$costs[$nextTail], $nextTail];
                    $rightHeap->insert($item, $item);
                    --$nextTail;
                }
            } elseif ($rightHeap->isEmpty()) {
                // take from left
                $chosen = $leftHeap->extract();
                $total += $chosen[0];
                if ($nextHead <= $nextTail) {
                    $item = [$costs[$nextHead], $nextHead];
                    $leftHeap->insert($item, $item);
                    ++$nextHead;
                }
            } else {
                // both non‑empty, compare tops
                $leftTop = $leftHeap->top();   // does not extract
                $rightTop = $rightHeap->top();

                if ($leftTop[0] <= $rightTop[0]) { // left wins on tie as well
                    $chosen = $leftHeap->extract();
                    $total += $chosen[0];
                    if ($nextHead <= $nextTail) {
                        $item = [$costs[$nextHead], $nextHead];
                        $leftHeap->insert($item, $item);
                        ++$nextHead;
                    }
                } else {
                    $chosen = $rightHeap->extract();
                    $total += $chosen[0];
                    if ($nextHead <= $nextTail) {
                        $item = [$costs[$nextTail], $nextTail];
                        $rightHeap->insert($item, $item);
                        --$nextTail;
                    }
                }
            }
        }

        return $total;
    }
}
```

## Swift

```swift
struct MinHeap {
    private var data: [Int] = []
    
    var isEmpty: Bool { data.isEmpty }
    var count: Int { data.count }
    func peek() -> Int? { data.first }
    
    mutating func push(_ value: Int) {
        data.append(value)
        siftUp(data.count - 1)
    }
    
    mutating func pop() -> Int {
        let result = data[0]
        let last = data.removeLast()
        if !data.isEmpty {
            data[0] = last
            siftDown(0)
        }
        return result
    }
    
    private mutating func siftUp(_ index: Int) {
        var child = index
        while child > 0 {
            let parent = (child - 1) / 2
            if data[parent] <= data[child] { break }
            data.swapAt(parent, child)
            child = parent
        }
    }
    
    private mutating func siftDown(_ index: Int) {
        var parent = index
        while true {
            let left = parent * 2 + 1
            let right = left + 1
            var smallest = parent
            if left < data.count && data[left] < data[smallest] {
                smallest = left
            }
            if right < data.count && data[right] < data[smallest] {
                smallest = right
            }
            if smallest == parent { break }
            data.swapAt(parent, smallest)
            parent = smallest
        }
    }
}

class Solution {
    func totalCost(_ costs: [Int], _ k: Int, _ candidates: Int) -> Int {
        let n = costs.count
        var leftHeap = MinHeap()
        var rightHeap = MinHeap()
        
        var leftIdx = 0
        var rightIdx = n - 1
        
        // Fill initial candidates from the left side
        while leftIdx <= rightIdx && leftHeap.count < candidates {
            leftHeap.push(costs[leftIdx])
            leftIdx += 1
        }
        // Fill initial candidates from the right side
        while rightIdx >= leftIdx && rightHeap.count < candidates {
            rightHeap.push(costs[rightIdx])
            rightIdx -= 1
        }
        
        var total = 0
        var hired = 0
        
        while hired < k {
            let takeFromLeft: Bool
            if leftHeap.isEmpty {
                takeFromLeft = false
            } else if rightHeap.isEmpty {
                takeFromLeft = true
            } else {
                // Tie goes to the left side (smaller original index)
                if leftHeap.peek()! <= rightHeap.peek()! {
                    takeFromLeft = true
                } else {
                    takeFromLeft = false
                }
            }
            
            if takeFromLeft {
                total += leftHeap.pop()
                if leftIdx <= rightIdx {
                    leftHeap.push(costs[leftIdx])
                    leftIdx += 1
                }
            } else {
                total += rightHeap.pop()
                if leftIdx <= rightIdx {
                    rightHeap.push(costs[rightIdx])
                    rightIdx -= 1
                }
            }
            
            hired += 1
        }
        
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun totalCost(costs: IntArray, k: Int, candidates: Int): Long {
        val n = costs.size
        // If the candidate windows overlap, all workers are initially candidates.
        if (candidates * 2 >= n) {
            val pq = java.util.PriorityQueue<Int>()
            for (c in costs) pq.add(c)
            var total = 0L
            repeat(k) { total += pq.poll() }
            return total
        }

        data class Node(val cost: Int, val idx: Int)

        val leftHeap = java.util.PriorityQueue<Node>(compareBy { it.cost })
        val rightHeap = java.util.PriorityQueue<Node>(compareBy { it.cost })

        var leftPtr = 0
        var rightPtr = n - 1

        // Initialize left candidates
        repeat(candidates) {
            leftHeap.add(Node(costs[leftPtr], leftPtr))
            leftPtr++
        }
        // Initialize right candidates
        repeat(candidates) {
            rightHeap.add(Node(costs[rightPtr], rightPtr))
            rightPtr--
        }

        var total = 0L
        repeat(k) {
            val takeFromLeft = when {
                leftHeap.isEmpty() -> false
                rightHeap.isEmpty() -> true
                else -> leftHeap.peek().cost <= rightHeap.peek().cost
            }

            if (takeFromLeft) {
                val node = leftHeap.poll()
                total += node.cost.toLong()
                if (leftPtr <= rightPtr) {
                    leftHeap.add(Node(costs[leftPtr], leftPtr))
                    leftPtr++
                }
            } else {
                val node = rightHeap.poll()
                total += node.cost.toLong()
                if (leftPtr <= rightPtr) {
                    rightHeap.add(Node(costs[rightPtr], rightPtr))
                    rightPtr--
                }
            }
        }

        return total
    }
}
```

## Dart

```dart
class MinHeap {
  final List<List<int>> _heap = [];

  bool get isEmpty => _heap.isEmpty;

  void push(List<int> value) {
    _heap.add(value);
    _siftUp(_heap.length - 1);
  }

  List<int> pop() {
    if (_heap.isEmpty) {
      throw StateError('Heap is empty');
    }
    final top = _heap.first;
    final last = _heap.removeLast();
    if (_heap.isNotEmpty) {
      _heap[0] = last;
      _siftDown(0);
    }
    return top;
  }

  void _siftUp(int idx) {
    while (idx > 0) {
      final parent = (idx - 1) >> 1;
      if (_compare(_heap[idx], _heap[parent]) < 0) {
        _swap(idx, parent);
        idx = parent;
      } else {
        break;
      }
    }
  }

  void _siftDown(int idx) {
    final n = _heap.length;
    while (true) {
      int left = idx * 2 + 1;
      int right = left + 1;
      int smallest = idx;

      if (left < n && _compare(_heap[left], _heap[smallest]) < 0) {
        smallest = left;
      }
      if (right < n && _compare(_heap[right], _heap[smallest]) < 0) {
        smallest = right;
      }
      if (smallest != idx) {
        _swap(idx, smallest);
        idx = smallest;
      } else {
        break;
      }
    }
  }

  int _compare(List<int> a, List<int> b) {
    if (a[0] != b[0]) return a[0] - b[0];
    return a[1] - b[1]; // tie‑break by index (smaller index first)
  }

  void _swap(int i, int j) {
    final tmp = _heap[i];
    _heap[i] = _heap[j];
    _heap[j] = tmp;
  }
}

class Solution {
  int totalCost(List<int> costs, int k, int candidates) {
    final n = costs.length;
    int leftPtr = 0;
    int rightPtr = n - 1;

    final heap = MinHeap();

    // add initial candidates from the left side
    while (leftPtr < n && leftPtr < candidates) {
      heap.push([costs[leftPtr], leftPtr]);
      leftPtr++;
    }

    // add initial candidates from the right side, avoiding overlap
    while (rightPtr >= 0 && rightPtr >= n - candidates && rightPtr >= leftPtr) {
      heap.push([costs[rightPtr], rightPtr]);
      rightPtr--;
    }

    int total = 0;
    for (int hired = 0; hired < k; ++hired) {
      final node = heap.pop();
      final cost = node[0];
      final idx = node[1];
      total += cost;

      // replenish from the side we took a worker
      if (idx < leftPtr) {
        // came from left side
        if (leftPtr <= rightPtr) {
          heap.push([costs[leftPtr], leftPtr]);
          leftPtr++;
        }
      } else {
        // came from right side
        if (leftPtr <= rightPtr) {
          heap.push([costs[rightPtr], rightPtr]);
          rightPtr--;
        }
      }
    }

    return total;
  }
}
```

## Golang

```go
package main

import (
	"container/heap"
)

type item struct {
	cost int
	idx  int
}

// minHeap implements heap.Interface based on cost then index.
type minHeap []item

func (h minHeap) Len() int { return len(h) }
func (h minHeap) Less(i, j int) bool {
	if h[i].cost == h[j].cost {
		return h[i].idx < h[j].idx
	}
	return h[i].cost < h[j].cost
}
func (h minHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *minHeap) Push(x interface{}) {
	*h = append(*h, x.(item))
}

func (h *minHeap) Pop() interface{} {
	old := *h
	n := len(old)
	it := old[n-1]
	*h = old[:n-1]
	return it
}

// totalCost returns the minimum total cost to hire k workers.
func totalCost(costs []int, k int, candidates int) int64 {
	n := len(costs)
	if k == 0 {
		return 0
	}

	leftPtr, rightPtr := 0, n-1
	lh := &minHeap{}
	rh := &minHeap{}
	heap.Init(lh)
	heap.Init(rh)

	// Fill initial candidates from the left side.
	for i := 0; i < candidates && leftPtr <= rightPtr; i++ {
		heap.Push(lh, item{costs[leftPtr], leftPtr})
		leftPtr++
	}
	// Fill initial candidates from the right side.
	for i := 0; i < candidates && leftPtr <= rightPtr; i++ {
		heap.Push(rh, item{costs[rightPtr], rightPtr})
		rightPtr--
	}

	var total int64
	for hired := 0; hired < k; hired++ {
		var chosen item
		// Decide which heap to pop from.
		if lh.Len() > 0 && (rh.Len() == 0 ||
			lh.Peek().cost < rh.Peek().cost ||
			(lh.Peek().cost == rh.Peek().cost && lh.Peek().idx < rh.Peek().idx)) {
			chosen = heap.Pop(lh).(item)
			if leftPtr <= rightPtr {
				heap.Push(lh, item{costs[leftPtr], leftPtr})
				leftPtr++
			}
		} else {
			chosen = heap.Pop(rh).(item)
			if leftPtr <= rightPtr {
				heap.Push(rh, item{costs[rightPtr], rightPtr})
				rightPtr--
			}
		}
		total += int64(chosen.cost)
	}
	return total
}

// Peek returns the top element without removing it.
func (h minHeap) Peek() item { return h[0] }
```

## Ruby

```ruby
class MinHeap
  def initialize
    @data = []
  end

  def push(val)
    @data << val
    i = @data.size - 1
    while i > 0
      p = (i - 1) / 2
      break if compare(@data[p], @data[i]) <= 0
      @data[p], @data[i] = @data[i], @data[p]
      i = p
    end
  end

  def pop
    top = @data[0]
    last = @data.pop
    unless @data.empty?
      @data[0] = last
      i = 0
      n = @data.size
      loop do
        l = i * 2 + 1
        r = l + 1
        smallest = i
        if l < n && compare(@data[l], @data[smallest]) < 0
          smallest = l
        end
        if r < n && compare(@data[r], @data[smallest]) < 0
          smallest = r
        end
        break if smallest == i
        @data[i], @data[smallest] = @data[smallest], @data[i]
        i = smallest
      end
    end
    top
  end

  def peek
    @data[0]
  end

  def empty?
    @data.empty?
  end

  private

  def compare(a, b)
    if a[0] != b[0]
      a[0] <=> b[0]
    else
      a[1] <=> b[1]
    end
  end
end

# @param {Integer[]} costs
# @param {Integer} k
# @param {Integer} candidates
# @return {Integer}
def total_cost(costs, k, candidates)
  n = costs.length
  left = MinHeap.new
  right = MinHeap.new

  i = 0
  while i < candidates && i < n
    left.push([costs[i], i])
    i += 1
  end

  j = n - 1
  while j >= n - candidates && j >= i
    right.push([costs[j], j])
    j -= 1
  end

  next_left = i
  next_right = j
  total = 0

  k.times do
    if left.empty?
      cost, idx = right.pop
      from_left = false
    elsif right.empty?
      cost, idx = left.pop
      from_left = true
    else
      ltop = left.peek
      rtop = right.peek
      if ltop[0] < rtop[0] || (ltop[0] == rtop[0] && ltop[1] < rtop[1])
        cost, idx = left.pop
        from_left = true
      else
        cost, idx = right.pop
        from_left = false
      end
    end

    total += cost

    if from_left
      if next_left <= next_right
        left.push([costs[next_left], next_left])
        next_left += 1
      end
    else
      if next_left <= next_right
        right.push([costs[next_right], next_right])
        next_right -= 1
      end
    end
  end

  total
end
```

## Scala

```scala
object Solution {
    def totalCost(costs: Array[Int], k: Int, candidates: Int): Long = {
        val n = costs.length
        val left = new java.util.PriorityQueue[(Int, Int)](new java.util.Comparator[(Int, Int)] {
            override def compare(a: (Int, Int), b: (Int, Int)): Int = {
                if (a._1 != b._1) a._1 - b._1 else a._2 - b._2
            }
        })
        val right = new java.util.PriorityQueue[(Int, Int)](new java.util.Comparator[(Int, Int)] {
            override def compare(a: (Int, Int), b: (Int, Int)): Int = {
                if (a._1 != b._1) a._1 - b._1 else a._2 - b._2
            }
        })

        // Initialize left heap with first candidates workers
        var i = 0
        while (i < candidates && i < n) {
            left.add((costs(i), i))
            i += 1
        }

        // Initialize right heap with last candidates workers, avoiding overlap
        var startRight = Math.max(candidates, n - candidates)
        while (startRight < n) {
            right.add((costs(startRight), startRight))
            startRight += 1
        }

        var nextHead = candidates
        var nextTail = n - candidates - 1

        var total: Long = 0L
        var hired = 0
        while (hired < k) {
            if (left.isEmpty) {
                val elem = right.poll()
                total += elem._1
                if (nextHead <= nextTail) {
                    right.add((costs(nextTail), nextTail))
                    nextTail -= 1
                }
            } else if (right.isEmpty) {
                val elem = left.poll()
                total += elem._1
                if (nextHead <= nextTail) {
                    left.add((costs(nextHead), nextHead))
                    nextHead += 1
                }
            } else {
                val leftTop = left.peek()
                val rightTop = right.peek()
                if (leftTop._1 <= rightTop._1) {
                    val elem = left.poll()
                    total += elem._1
                    if (nextHead <= nextTail) {
                        left.add((costs(nextHead), nextHead))
                        nextHead += 1
                    }
                } else {
                    val elem = right.poll()
                    total += elem._1
                    if (nextHead <= nextTail) {
                        right.add((costs(nextTail), nextTail))
                        nextTail -= 1
                    }
                }
            }
            hired += 1
        }

        total
    }
}
```

## Rust

```rust
use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn total_cost(costs: Vec<i32>, k: i32, candidates: i32) -> i64 {
        let n = costs.len();
        let mut left_heap: BinaryHeap<Reverse<(i32, usize)>> = BinaryHeap::new();
        let mut right_heap: BinaryHeap<Reverse<(i32, usize)>> = BinaryHeap::new();

        let mut l: usize = 0;
        let mut r: usize = n.saturating_sub(1);
        let cand = candidates as usize;

        // fill left side
        for _ in 0..cand {
            if l > r { break; }
            left_heap.push(Reverse((costs[l], l)));
            l += 1;
        }

        // fill right side
        for _ in 0..cand {
            if l > r { break; }
            right_heap.push(Reverse((costs[r], r)));
            if r == 0 { break; } // avoid underflow
            r -= 1;
        }

        let mut total: i64 = 0;
        for _ in 0..k as usize {
            let take_left = if left_heap.is_empty() {
                false
            } else if right_heap.is_empty() {
                true
            } else {
                let left_cost = left_heap.peek().unwrap().0 .0;
                let right_cost = right_heap.peek().unwrap().0 .0;
                left_cost <= right_cost
            };

            if take_left {
                let Reverse((cost, _idx)) = left_heap.pop().unwrap();
                total += cost as i64;
                if l <= r {
                    left_heap.push(Reverse((costs[l], l)));
                    l += 1;
                }
            } else {
                let Reverse((cost, _idx)) = right_heap.pop().unwrap();
                total += cost as i64;
                if l <= r {
                    right_heap.push(Reverse((costs[r], r)));
                    if r == 0 { break; }
                    r -= 1;
                }
            }
        }

        total
    }
}
```

## Racket

```racket
(require racket/heap)

(define/contract (total-cost costs k candidates)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (let* ((v (list->vector costs))
         (n (vector-length v))
         (m candidates)
         (cmp (lambda (a b)
                (or (< (car a) (car b))
                    (and (= (car a) (car b)) (< (cadr a) (cadr b))))))
         (left (make-heap cmp))
         (right (make-heap cmp)))
    ;; initialize left heap with first m workers
    (let ((limit (min m n)))
      (for ([i (in-range limit)])
        (heap-add! left (list (vector-ref v i) i))))
    ;; initialize right heap with last m workers, avoiding overlap
    (let ((start (max m (- n m))))
      (when (< start n)
        (for ([i (in-range start n)])
          (heap-add! right (list (vector-ref v i) i)))))
    (define next-head m)
    (define next-tail (- n m 1))
    (define total 0)
    (let loop ((remaining k) (total total) (next-head next-head) (next-tail next-tail))
      (if (= remaining 0)
          total
          (begin
            (define choose-left
              (cond [(heap-empty? left) #f]
                    [(heap-empty? right) #t]
                    [else (cmp (heap-peek left) (heap-peek right))]))
            (if choose-left
                (let* ((item (heap-pop! left))
                       (cost (car item)))
                  (set! total (+ total cost))
                  (when (<= next-head next-tail)
                    (heap-add! left (list (vector-ref v next-head) next-head))
                    (set! next-head (+ next-head 1))))
                (let* ((item (heap-pop! right))
                       (cost (car item)))
                  (set! total (+ total cost))
                  (when (<= next-head next-tail)
                    (heap-add! right (list (vector-ref v next-tail) next-tail))
                    (set! next-tail (- next-tail 1)))))
            (loop (- remaining 1) total next-head next-tail))))))
```

## Erlang

```erlang
-module(solution).
-export([total_cost/3]).
-spec total_cost(Costs :: [integer()], K :: integer(), Candidates :: integer()) -> integer().
total_cost(Costs, K, Candidates) ->
    N = length(Costs),
    M = Candidates,
    Tree0 = build_initial_tree(Costs, N, M),
    NextHead = min(M, N),
    NextTail = N - M - 1,
    hire(K, Tree0, NextHead, NextTail, Costs, 0).

build_initial_tree(Costs, N, M) ->
    LeftIndices = lists:seq(0, erlang:min(M - 1, N - 1)),
    TreeLeft = lists:foldl(
        fun(I, Acc) ->
            C = element_at(I, Costs),
            gb_trees:insert({C, I}, 0, Acc)
        end,
        gb_trees:empty(),
        LeftIndices
    ),
    StartRight = erlang:max(N - M, 0),
    RightIndices = lists:seq(StartRight, N - 1),
    lists:foldl(
        fun(J, Acc) ->
            if J < M -> Acc; % already added from left side
               true ->
                   C = element_at(J, Costs),
                   gb_trees:insert({C, J}, 1, Acc)
            end
        end,
        TreeLeft,
        RightIndices
    ).

hire(0, _Tree, _NH, _NT, _Costs, Total) ->
    Total;
hire(K, Tree, NH, NT, Costs, Total) ->
    {Key, Side, Rest} = gb_trees:take_smallest(Tree),
    {Cost, _Idx} = Key,
    NewTotal = Total + Cost,
    case Side of
        0 -> % came from left side
            if NH =< NT ->
                    C = element_at(NH, Costs),
                    NewTree = gb_trees:insert({C, NH}, 0, Rest),
                    hire(K - 1, NewTree, NH + 1, NT, Costs, NewTotal);
               true ->
                    hire(K - 1, Rest, NH, NT, Costs, NewTotal)
            end;
        1 -> % came from right side
            if NH =< NT ->
                    C = element_at(NT, Costs),
                    NewTree = gb_trees:insert({C, NT}, 1, Rest),
                    hire(K - 1, NewTree, NH, NT - 1, Costs, NewTotal);
               true ->
                    hire(K - 1, Rest, NH, NT, Costs, NewTotal)
            end
    end.

element_at(Index, List) ->
    lists:nth(Index + 1, List).
```

## Elixir

```elixir
defmodule Solution do
  @spec total_cost(costs :: [integer], k :: integer, candidates :: integer) :: integer
  def total_cost(costs, k, candidates) do
    n = length(costs)
    arr = List.to_tuple(costs)

    {left_heap, right_heap, next_head, next_tail} = init_heaps(arr, n, candidates)
    hire(k, left_heap, right_heap, next_head, next_tail, arr, 0)
  end

  # Initialize the two heaps and pointers
  defp init_heaps(arr, n, cand) do
    left_cnt = min(cand, n)

    {left_heap, nh} = fill_left(arr, 0, left_cnt, :gb_trees.empty())
    remaining = n - nh
    right_cnt = min(cand, remaining)

    {right_heap, nt, _} = fill_right(arr, n - 1, right_cnt, nh, :gb_trees.empty())
    {left_heap, right_heap, nh, nt}
  end

  # Fill left heap with first `cnt` elements starting at index `idx`
  defp fill_left(_arr, idx, 0, heap), do: {heap, idx}

  defp fill_left(arr, idx, cnt, heap) when cnt > 0 do
    cost = elem(arr, idx)
    key = {cost, idx}
    heap2 = :gb_trees.insert(key, true, heap)
    fill_left(arr, idx + 1, cnt - 1, heap2)
  end

  # Fill right heap with up to `cnt` elements from the end, not crossing `limit_idx`
  defp fill_right(_arr, idx, _cnt, limit_idx, heap) when idx < limit_idx do
    {heap, idx, nil}
  end

  defp fill_right(_arr, _idx, 0, _limit_idx, heap), do: {heap, -1, nil}

  defp fill_right(arr, idx, cnt, limit_idx, heap) when cnt > 0 and idx >= limit_idx do
    cost = elem(arr, idx)
    key = {cost, idx}
    heap2 = :gb_trees.insert(key, true, heap)
    fill_right(arr, idx - 1, cnt - 1, limit_idx, heap2)
  end

  # Hiring process
  defp hire(0, _lh, _rh, _nh, _nt, _arr, total), do: total

  defp hire(remain, left_heap, right_heap, nh, nt, arr, total) do
    cond do
      :gb_trees.is_empty(left_heap) ->
        # take from right heap
        {{{cost, _idx}, _}, rh1} = :gb_trees.take_smallest(right_heap)
        total2 = total + cost

        {rh2, nh2, nt2} =
          if nh <= nt do
            c = elem(arr, nt)
            k = {c, nt}
            {:gb_trees.insert(k, true, rh1), nh, nt - 1}
          else
            {rh1, nh, nt}
          end

        hire(remain - 1, left_heap, rh2, nh2, nt2, arr, total2)

      :gb_trees.is_empty(right_heap) ->
        # take from left heap
        {{{cost, _idx}, _}, lh1} = :gb_trees.take_smallest(left_heap)
        total2 = total + cost

        {lh2, nh2, nt2} =
          if nh <= nt do
            c = elem(arr, nh)
            k = {c, nh}
            {:gb_trees.insert(k, true, lh1), nh + 1, nt}
          else
            {lh1, nh, nt}
          end

        hire(remain - 1, lh2, right_heap, nh2, nt2, arr, total2)

      true ->
        # both heaps non-empty, compare minima
        left_min_key = :gb_trees.smallest(left_heap) |> elem(0)
        right_min_key = :gb_trees.smallest(right_heap) |> elem(0)

        left_cost = elem(left_min_key, 0)
        right_cost = elem(right_min_key, 0)

        if left_cost <= right_cost do
          # take from left heap
          {{{cost, _idx}, _}, lh1} = :gb_trees.take_smallest(left_heap)
          total2 = total + cost

          {lh2, nh2, nt2} =
            if nh <= nt do
              c = elem(arr, nh)
              k = {c, nh}
              {:gb_trees.insert(k, true, lh1), nh + 1, nt}
            else
              {lh1, nh, nt}
            end

          hire(remain - 1, lh2, right_heap, nh2, nt2, arr, total2)
        else
          # take from right heap
          {{{cost, _idx}, _}, rh1} = :gb_trees.take_smallest(right_heap)
          total2 = total + cost

          {rh2, nh2, nt2} =
            if nh <= nt do
              c = elem(arr, nt)
              k = {c, nt}
              {:gb_trees.insert(k, true, rh1), nh, nt - 1}
            else
              {rh1, nh, nt}
            end

          hire(remain - 1, left_heap, rh2, nh2, nt2, arr, total2)
        end
    end
  end
end
```
