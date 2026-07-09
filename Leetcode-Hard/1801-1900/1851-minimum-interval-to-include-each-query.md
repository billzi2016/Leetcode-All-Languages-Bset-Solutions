# 1851. Minimum Interval to Include Each Query

## Cpp

```cpp
class Solution {
public:
    vector<int> minInterval(vector<vector<int>>& intervals, vector<int>& queries) {
        sort(intervals.begin(), intervals.end(),
             [](const vector<int>& a, const vector<int>& b){ return a[0] < b[0]; });
        
        int m = queries.size();
        vector<pair<int,int>> q(m);
        for (int i = 0; i < m; ++i) q[i] = {queries[i], i};
        sort(q.begin(), q.end());
        
        vector<int> ans(m, -1);
        using P = pair<int,int>; // {size, right}
        priority_queue<P, vector<P>, greater<P>> pq;
        size_t idx = 0;
        for (auto [val, pos] : q) {
            while (idx < intervals.size() && intervals[idx][0] <= val) {
                int l = intervals[idx][0];
                int r = intervals[idx][1];
                pq.emplace(r - l + 1, r);
                ++idx;
            }
            while (!pq.empty() && pq.top().second < val) {
                pq.pop();
            }
            if (!pq.empty()) ans[pos] = pq.top().first;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] minInterval(int[][] intervals, int[] queries) {
        int n = intervals.length;
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        
        int m = queries.length;
        Integer[] order = new Integer[m];
        for (int i = 0; i < m; i++) order[i] = i;
        Arrays.sort(order, (i, j) -> Integer.compare(queries[i], queries[j]));
        
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
            int sizeA = a[1] - a[0] + 1;
            int sizeB = b[1] - b[0] + 1;
            if (sizeA != sizeB) return Integer.compare(sizeA, sizeB);
            return Integer.compare(a[1], b[1]); // tie‑breaker
        });
        
        int[] ans = new int[m];
        int idx = 0; // pointer for intervals
        
        for (int qIdx : order) {
            int q = queries[qIdx];
            
            while (idx < n && intervals[idx][0] <= q) {
                pq.offer(intervals[idx]);
                idx++;
            }
            while (!pq.isEmpty() && pq.peek()[1] < q) {
                pq.poll();
            }
            if (pq.isEmpty()) {
                ans[qIdx] = -1;
            } else {
                int[] iv = pq.peek();
                ans[qIdx] = iv[1] - iv[0] + 1;
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def minInterval(self, intervals, queries):
        """
        :type intervals: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        import heapq

        # Sort intervals by left endpoint
        intervals.sort(key=lambda x: x[0])
        # Pair each query with its original index and sort by value
        q_with_idx = sorted([(val, idx) for idx, val in enumerate(queries)])

        res = [-1] * len(queries)
        heap = []  # elements are (size, right)

        i = 0  # pointer over intervals
        n = len(intervals)

        for q_val, q_idx in q_with_idx:
            # Add all intervals whose left <= current query
            while i < n and intervals[i][0] <= q_val:
                l, r = intervals[i]
                size = r - l + 1
                heapq.heappush(heap, (size, r))
                i += 1

            # Remove intervals that end before the query point
            while heap and heap[0][1] < q_val:
                heapq.heappop(heap)

            if heap:
                res[q_idx] = heap[0][0]
            else:
                res[q_idx] = -1

        return res
```

## Python3

```python
import heapq
from typing import List

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        sorted_q = sorted((q, i) for i, q in enumerate(queries))
        ans = [-1] * len(queries)
        heap = []  # (size, right)
        i = 0
        n = len(intervals)

        for q, idx in sorted_q:
            while i < n and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(heap, (r - l + 1, r))
                i += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            if heap:
                ans[idx] = heap[0][0]

        return ans
```

## C

```c
#include <stdlib.h>

struct Interval {
    int left;
    int right;
    int len;
};

struct Query {
    int val;
    int idx;
};

struct HeapNode {
    int len;
    int right;
};

/* Min-heap based on interval length */
static void heapPush(struct HeapNode *heap, int *size, struct HeapNode node) {
    int i = (*size)++;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (heap[p].len <= node.len) break;
        heap[i] = heap[p];
        i = p;
    }
    heap[i] = node;
}

static void heapPop(struct HeapNode *heap, int *size) {
    int n = --(*size);
    if (n == 0) return;
    struct HeapNode last = heap[n];
    int i = 0;
    while (1) {
        int l = (i << 1) + 1;
        if (l >= n) break;
        int r = l + 1;
        int smallest = l;
        if (r < n && heap[r].len < heap[l].len) smallest = r;
        if (heap[smallest].len >= last.len) break;
        heap[i] = heap[smallest];
        i = smallest;
    }
    heap[i] = last;
}

/* Comparators for qsort */
static int cmpInterval(const void *a, const void *b) {
    const struct Interval *ia = (const struct Interval *)a;
    const struct Interval *ib = (const struct Interval *)b;
    return ia->left - ib->left;
}

static int cmpQuery(const void *a, const void *b) {
    const struct Query *qa = (const struct Query *)a;
    const struct Query *qb = (const struct Query *)b;
    return qa->val - qb->val;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* minInterval(int** intervals, int intervalsSize, int* intervalsColSize,
                 int* queries, int queriesSize, int* returnSize) {
    struct Interval *ints = (struct Interval *)malloc(sizeof(struct Interval) * intervalsSize);
    for (int i = 0; i < intervalsSize; ++i) {
        ints[i].left = intervals[i][0];
        ints[i].right = intervals[i][1];
        ints[i].len = ints[i].right - ints[i].left + 1;
    }
    qsort(ints, intervalsSize, sizeof(struct Interval), cmpInterval);

    struct Query *qs = (struct Query *)malloc(sizeof(struct Query) * queriesSize);
    for (int i = 0; i < queriesSize; ++i) {
        qs[i].val = queries[i];
        qs[i].idx = i;
    }
    qsort(qs, queriesSize, sizeof(struct Query), cmpQuery);

    struct HeapNode *heap = (struct HeapNode *)malloc(sizeof(struct HeapNode) * intervalsSize);
    int heapSize = 0;

    int *ans = (int *)malloc(sizeof(int) * queriesSize);
    int intPtr = 0;  // pointer in sorted intervals

    for (int i = 0; i < queriesSize; ++i) {
        int qval = qs[i].val;
        while (intPtr < intervalsSize && ints[intPtr].left <= qval) {
            struct HeapNode node;
            node.len = ints[intPtr].len;
            node.right = ints[intPtr].right;
            heapPush(heap, &heapSize, node);
            ++intPtr;
        }
        while (heapSize > 0 && heap[0].right < qval) {
            heapPop(heap, &heapSize);
        }
        if (heapSize == 0)
            ans[qs[i].idx] = -1;
        else
            ans[qs[i].idx] = heap[0].len;
    }

    free(ints);
    free(qs);
    free(heap);

    *returnSize = queriesSize;
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] MinInterval(int[][] intervals, int[] queries) {
        // Sort intervals by left endpoint
        var sortedIntervals = intervals.OrderBy(iv => iv[0]).ToArray();
        int n = sortedIntervals.Length;
        
        int m = queries.Length;
        // indices of queries sorted by query value
        var order = Enumerable.Range(0, m).OrderBy(i => queries[i]).ToArray();
        int[] answer = new int[m];
        
        // Min-heap where priority is interval size (right-left+1)
        var pq = new PriorityQueue<int[], int>(); // element: [right, size], priority: size
        
        int idx = 0; // pointer in sortedIntervals
        foreach (int qIdx in order) {
            int q = queries[qIdx];
            
            // Add all intervals whose left <= q
            while (idx < n && sortedIntervals[idx][0] <= q) {
                int l = sortedIntervals[idx][0];
                int r = sortedIntervals[idx][1];
                int size = r - l + 1;
                pq.Enqueue(new int[] { r, size }, size);
                idx++;
            }
            
            // Remove intervals that end before q
            while (pq.Count > 0) {
                pq.TryPeek(out var top, out _);
                if (top[0] < q) {
                    pq.Dequeue();
                } else {
                    break;
                }
            }
            
            if (pq.Count == 0) {
                answer[qIdx] = -1;
            } else {
                pq.TryPeek(out _, out int minSize);
                answer[qIdx] = minSize;
            }
        }
        
        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} intervals
 * @param {number[]} queries
 * @return {number[]}
 */
var minInterval = function(intervals, queries) {
    // sort intervals by left endpoint
    intervals.sort((a, b) => a[0] - b[0]);

    // pair each query with its original index and sort by query value
    const qWithIdx = queries.map((v, i) => [v, i]).sort((a, b) => a[0] - b[0]);
    const ans = new Array(queries.length).fill(-1);

    class MinHeap {
        constructor() { this.heap = []; }
        size() { return this.heap.length; }
        peek() { return this.heap[0]; }
        push(item) {
            const h = this.heap;
            h.push(item);
            let i = h.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (h[p][0] <= item[0]) break; // compare by size
                h[i] = h[p];
                i = p;
            }
            h[i] = item;
        }
        pop() {
            const h = this.heap;
            if (h.length === 0) return undefined;
            const top = h[0];
            const last = h.pop();
            if (h.length > 0) {
                let i = 0;
                while (true) {
                    const l = i * 2 + 1;
                    if (l >= h.length) break;
                    const r = l + 1;
                    const smallest = (r < h.length && h[r][0] < h[l][0]) ? r : l;
                    if (last[0] <= h[smallest][0]) break;
                    h[i] = h[smallest];
                    i = smallest;
                }
                h[i] = last;
            }
            return top;
        }
    }

    const heap = new MinHeap();
    let idx = 0; // pointer for intervals

    for (const [q, originalIdx] of qWithIdx) {
        // add all intervals whose left <= current query
        while (idx < intervals.length && intervals[idx][0] <= q) {
            const l = intervals[idx][0];
            const r = intervals[idx][1];
            heap.push([r - l + 1, r]); // [size, right]
            idx++;
        }
        // remove intervals that no longer cover the query
        while (heap.size() > 0 && heap.peek()[1] < q) {
            heap.pop();
        }
        if (heap.size() > 0) ans[originalIdx] = heap.peek()[0];
    }

    return ans;
};
```

## Typescript

```typescript
function minInterval(intervals: number[][], queries: number[]): number[] {
    // Sort intervals by left endpoint
    intervals.sort((a, b) => a[0] - b[0]);

    // Pair each query with its original index and sort by query value
    const qWithIdx = queries.map((v, i) => [v, i] as [number, number]);
    qWithIdx.sort((a, b) => a[0] - b[0]);

    const ans: number[] = new Array(queries.length).fill(-1);
    let intPtr = 0;

    // Min-heap storing [size, right]
    class MinHeap {
        private heap: [number, number][] = [];

        private compare(a: [number, number], b: [number, number]): number {
            if (a[0] !== b[0]) return a[0] - b[0];
            return a[1] - b[1];
        }

        push(item: [number, number]): void {
            this.heap.push(item);
            let idx = this.heap.length - 1;
            while (idx > 0) {
                const parent = (idx - 1) >> 1;
                if (this.compare(this.heap[parent], this.heap[idx]) <= 0) break;
                [this.heap[parent], this.heap[idx]] = [this.heap[idx], this.heap[parent]];
                idx = parent;
            }
        }

        peek(): [number, number] | undefined {
            return this.heap[0];
        }

        pop(): [number, number] | undefined {
            if (this.heap.length === 0) return undefined;
            const top = this.heap[0];
            const last = this.heap.pop()!;
            if (this.heap.length > 0) {
                this.heap[0] = last;
                let idx = 0;
                while (true) {
                    const left = idx * 2 + 1;
                    const right = left + 1;
                    let smallest = idx;

                    if (left < this.heap.length && this.compare(this.heap[left], this.heap[smallest]) < 0) {
                        smallest = left;
                    }
                    if (right < this.heap.length && this.compare(this.heap[right], this.heap[smallest]) < 0) {
                        smallest = right;
                    }
                    if (smallest === idx) break;
                    [this.heap[idx], this.heap[smallest]] = [this.heap[smallest], this.heap[idx]];
                    idx = smallest;
                }
            }
            return top;
        }

        isEmpty(): boolean {
            return this.heap.length === 0;
        }
    }

    const heap = new MinHeap();

    for (const [q, originalIdx] of qWithIdx) {
        // Add all intervals whose left <= q
        while (intPtr < intervals.length && intervals[intPtr][0] <= q) {
            const l = intervals[intPtr][0];
            const r = intervals[intPtr][1];
            heap.push([r - l + 1, r]);
            intPtr++;
        }

        // Remove intervals that end before q
        while (!heap.isEmpty() && (heap.peek()![1] < q)) {
            heap.pop();
        }

        if (!heap.isEmpty()) {
            ans[originalIdx] = heap.peek()![0];
        } else {
            ans[originalIdx] = -1;
        }
    }

    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $intervals
     * @param Integer[] $queries
     * @return Integer[]
     */
    function minInterval($intervals, $queries) {
        // sort intervals by left endpoint
        usort($intervals, fn($a, $b) => $a[0] <=> $b[0]);

        // pair queries with original indices and sort by query value
        $qList = [];
        foreach ($queries as $idx => $val) {
            $qList[] = [$val, $idx];
        }
        usort($qList, fn($a, $b) => $a[0] <=> $b[0]);

        $ans = array_fill(0, count($queries), -1);
        $heap = []; // min-heap based on interval size
        $i = 0;
        $n = count($intervals);

        foreach ($qList as $pair) {
            [$q, $origIdx] = $pair;

            // add all intervals whose left <= q
            while ($i < $n && $intervals[$i][0] <= $q) {
                $size = $intervals[$i][1] - $intervals[$i][0] + 1;
                $this->heapPush($heap, ['size' => $size, 'right' => $intervals[$i][1]]);
                $i++;
            }

            // remove intervals that end before q
            while (!empty($heap) && $heap[0]['right'] < $q) {
                $this->heapPop($heap);
            }

            if (!empty($heap)) {
                $ans[$origIdx] = $heap[0]['size'];
            } else {
                $ans[$origIdx] = -1;
            }
        }

        return $ans;
    }

    private function heapPush(&$heap, $node) {
        $heap[] = $node;
        $idx = count($heap) - 1;
        while ($idx > 0) {
            $parent = intdiv($idx - 1, 2);
            if ($heap[$parent]['size'] <= $heap[$idx]['size']) {
                break;
            }
            $tmp = $heap[$parent];
            $heap[$parent] = $heap[$idx];
            $heap[$idx] = $tmp;
            $idx = $parent;
        }
    }

    private function heapPop(&$heap) {
        $n = count($heap);
        if ($n === 0) return null;
        $top = $heap[0];
        $last = array_pop($heap);
        if ($n > 1) {
            $heap[0] = $last;
            $idx = 0;
            $len = count($heap);
            while (true) {
                $left = $idx * 2 + 1;
                $right = $idx * 2 + 2;
                if ($left >= $len) break;
                $smallest = $left;
                if ($right < $len && $heap[$right]['size'] < $heap[$left]['size']) {
                    $smallest = $right;
                }
                if ($heap[$idx]['size'] <= $heap[$smallest]['size']) break;
                $tmp = $heap[$idx];
                $heap[$idx] = $heap[$smallest];
                $heap[$smallest] = $tmp;
                $idx = $smallest;
            }
        }
        return $top;
    }
}
```

## Swift

```swift
class Solution {
    struct Node {
        var size: Int
        var right: Int
    }
    
    struct MinHeap {
        private var data: [Node] = []
        
        var isEmpty: Bool { data.isEmpty }
        func peek() -> Node? { data.first }
        
        mutating func push(_ node: Node) {
            data.append(node)
            siftUp(data.count - 1)
        }
        
        mutating func pop() -> Node? {
            guard !data.isEmpty else { return nil }
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
                if data[child].size < data[parent].size {
                    data.swapAt(child, parent)
                    child = parent
                } else {
                    break
                }
            }
        }
        
        private mutating func siftDown(_ index: Int) {
            var parent = index
            while true {
                let left = parent * 2 + 1
                let right = left + 1
                var smallest = parent
                if left < data.count && data[left].size < data[smallest].size {
                    smallest = left
                }
                if right < data.count && data[right].size < data[smallest].size {
                    smallest = right
                }
                if smallest == parent { break }
                data.swapAt(parent, smallest)
                parent = smallest
            }
        }
    }
    
    func minInterval(_ intervals: [[Int]], _ queries: [Int]) -> [Int] {
        let sortedIntervals = intervals.sorted { $0[0] < $1[0] }
        var queryPairs: [(value: Int, idx: Int)] = []
        for (i, q) in queries.enumerated() {
            queryPairs.append((q, i))
        }
        queryPairs.sort { $0.value < $1.value }
        
        var answers = Array(repeating: -1, count: queries.count)
        var heap = MinHeap()
        var intervalIdx = 0
        
        for qp in queryPairs {
            let q = qp.value
            while intervalIdx < sortedIntervals.count && sortedIntervals[intervalIdx][0] <= q {
                let l = sortedIntervals[intervalIdx][0]
                let r = sortedIntervals[intervalIdx][1]
                let size = r - l + 1
                heap.push(Node(size: size, right: r))
                intervalIdx += 1
            }
            while let top = heap.peek(), top.right < q {
                _ = heap.pop()
            }
            if let top = heap.peek() {
                answers[qp.idx] = top.size
            } else {
                answers[qp.idx] = -1
            }
        }
        
        return answers
    }
}
```

## Kotlin

```kotlin
import java.util.PriorityQueue

class Solution {
    data class Node(val size: Int, val right: Int)

    fun minInterval(intervals: Array<IntArray>, queries: IntArray): IntArray {
        // Sort intervals by left endpoint
        val sortedIntervals = intervals.sortedBy { it[0] }
        val n = sortedIntervals.size

        // Pair each query with its original index and sort by query value
        val qWithIdx = Array(queries.size) { i -> intArrayOf(queries[i], i) }
        qWithIdx.sortWith(compareBy<IntArray> { it[0] })

        val ans = IntArray(queries.size) { -1 }
        val pq = PriorityQueue<Node>(compareBy { it.size })
        var idx = 0

        for (pair in qWithIdx) {
            val q = pair[0]

            // Add all intervals whose left <= q
            while (idx < n && sortedIntervals[idx][0] <= q) {
                val l = sortedIntervals[idx][0]
                val r = sortedIntervals[idx][1]
                pq.add(Node(r - l + 1, r))
                idx++
            }

            // Remove intervals that end before q
            while (pq.isNotEmpty() && pq.peek().right < q) {
                pq.poll()
            }

            if (pq.isNotEmpty()) {
                ans[pair[1]] = pq.peek().size
            }
        }

        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> minInterval(List<List<int>> intervals, List<int> queries) {
    // Sort intervals by their left endpoint
    intervals.sort((a, b) => a[0].compareTo(b[0]));
    int n = intervals.length;
    int m = queries.length;

    // Pair each query with its original index and sort by query value
    List<_Query> qlist =
        List.generate(m, (i) => _Query(queries[i], i));
    qlist.sort((a, b) => a.val.compareTo(b.val));

    MinHeap heap = MinHeap();
    List<int> ans = List.filled(m, -1);
    int idx = 0; // pointer for intervals

    for (var q in qlist) {
      // Add all intervals whose left <= current query
      while (idx < n && intervals[idx][0] <= q.val) {
        int left = intervals[idx][0];
        int right = intervals[idx][1];
        int size = right - left + 1;
        heap.push(Node(size, right));
        idx++;
      }
      // Remove intervals that end before the query
      while (!heap.isEmpty && heap.peek().right < q.val) {
        heap.pop();
      }
      if (!heap.isEmpty) ans[q.idx] = heap.peek().size;
    }

    return ans;
  }
}

class _Query {
  int val;
  int idx;
  _Query(this.val, this.idx);
}

class Node {
  int size;
  int right;
  Node(this.size, this.right);
}

class MinHeap {
  final List<Node> _data = [];

  bool get isEmpty => _data.isEmpty;

  Node peek() => _data[0];

  void push(Node node) {
    _data.add(node);
    _siftUp(_data.length - 1);
  }

  Node pop() {
    Node top = _data[0];
    Node last = _data.removeLast();
    if (_data.isNotEmpty) {
      _data[0] = last;
      _siftDown(0);
    }
    return top;
  }

  void _siftUp(int i) {
    while (i > 0) {
      int p = (i - 1) >> 1;
      if (_compare(_data[i], _data[p]) < 0) {
        _swap(i, p);
        i = p;
      } else {
        break;
      }
    }
  }

  void _siftDown(int i) {
    int n = _data.length;
    while (true) {
      int l = i * 2 + 1;
      int r = i * 2 + 2;
      int smallest = i;

      if (l < n && _compare(_data[l], _data[smallest]) < 0) smallest = l;
      if (r < n && _compare(_data[r], _data[smallest]) < 0) smallest = r;

      if (smallest != i) {
        _swap(i, smallest);
        i = smallest;
      } else {
        break;
      }
    }
  }

  int _compare(Node a, Node b) {
    // Primary by size, secondary by right endpoint
    if (a.size != b.size) return a.size - b.size;
    return a.right - b.right;
  }

  void _swap(int i, int j) {
    Node tmp = _data[i];
    _data[i] = _data[j];
    _data[j] = tmp;
  }
}
```

## Golang

```go
package main

import (
	"container/heap"
	"sort"
)

type intervalItem struct {
	size  int
	right int
}

// MinHeap implements heap.Interface based on interval size.
type MinHeap []intervalItem

func (h MinHeap) Len() int { return len(h) }
func (h MinHeap) Less(i, j int) bool {
	return h[i].size < h[j].size
}
func (h MinHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *MinHeap) Push(x interface{}) {
	*h = append(*h, x.(intervalItem))
}

func (h *MinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	it := old[n-1]
	*h = old[:n-1]
	return it
}

type query struct {
	val int
	idx int
}

func minInterval(intervals [][]int, queries []int) []int {
	// Sort intervals by left endpoint.
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})

	// Prepare and sort queries while keeping original indices.
	qList := make([]query, len(queries))
	for i, v := range queries {
		qList[i] = query{val: v, idx: i}
	}
	sort.Slice(qList, func(i, j int) bool {
		return qList[i].val < qList[j].val
	})

	ans := make([]int, len(queries))
	h := &MinHeap{}
	heap.Init(h)

	intIdx := 0
	for _, q := range qList {
		// Add all intervals whose left <= current query value.
		for intIdx < len(intervals) && intervals[intIdx][0] <= q.val {
			left, right := intervals[intIdx][0], intervals[intIdx][1]
			size := right - left + 1
			heap.Push(h, intervalItem{size: size, right: right})
			intIdx++
		}
		// Remove intervals that do not cover the query.
		for h.Len() > 0 && (*h)[0].right < q.val {
			heap.Pop(h)
		}
		if h.Len() == 0 {
			ans[q.idx] = -1
		} else {
			ans[q.idx] = (*h)[0].size
		}
	}

	return ans
}
```

## Ruby

```ruby
def min_interval(intervals, queries)
  intervals.sort_by! { |l, r| l }
  q_with_idx = queries.each_with_index.map { |q, i| [q, i] }.sort_by { |pair| pair[0] }

  heap = MinHeap.new
  ans = Array.new(queries.size)

  i = 0
  n = intervals.length

  q_with_idx.each do |q, idx|
    while i < n && intervals[i][0] <= q
      l, r = intervals[i]
      size = r - l + 1
      heap.push([size, r])
      i += 1
    end

    while !heap.empty? && heap.top[1] < q
      heap.pop
    end

    ans[idx] = heap.empty? ? -1 : heap.top[0]
  end

  ans
end

class MinHeap
  def initialize
    @data = []
  end

  def push(val)
    @data << val
    sift_up(@data.size - 1)
  end

  def pop
    return nil if @data.empty?
    min = @data[0]
    last = @data.pop
    unless @data.empty?
      @data[0] = last
      sift_down(0)
    end
    min
  end

  def top
    @data[0]
  end

  def empty?
    @data.empty?
  end

  private

  def sift_up(idx)
    while idx > 0
      parent = (idx - 1) / 2
      break if @data[parent][0] <= @data[idx][0]
      @data[parent], @data[idx] = @data[idx], @data[parent]
      idx = parent
    end
  end

  def sift_down(idx)
    n = @data.size
    loop do
      left = idx * 2 + 1
      right = left + 1
      smallest = idx
      if left < n && @data[left][0] < @data[smallest][0]
        smallest = left
      end
      if right < n && @data[right][0] < @data[smallest][0]
        smallest = right
      end
      break if smallest == idx
      @data[smallest], @data[idx] = @data[idx], @data[smallest]
      idx = smallest
    end
  end
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable.PriorityQueue

  def minInterval(intervals: Array[Array[Int]], queries: Array[Int]): Array[Int] = {
    // Sort intervals by left endpoint
    val sortedIntervals = intervals.sortBy(_(0))
    // Pair each query with its original index and sort by query value
    val indexedQueries = queries.zipWithIndex.sortBy(_._1)

    // Min-heap based on interval size (right - left + 1)
    implicit val ord: Ordering[(Int, Int)] = Ordering.by[(Int, Int), Int](_._1).reverse
    val heap = PriorityQueue.empty[(Int, Int)]

    val ans = Array.fill(queries.length)(-1)
    var i = 0 // pointer for intervals

    for ((q, idx) <- indexedQueries) {
      // Add all intervals whose left <= q
      while (i < sortedIntervals.length && sortedIntervals(i)(0) <= q) {
        val left = sortedIntervals(i)(0)
        val right = sortedIntervals(i)(1)
        heap.enqueue((right - left + 1, right))
        i += 1
      }
      // Remove intervals that end before q
      while (heap.nonEmpty && heap.head._2 < q) {
        heap.dequeue()
      }
      if (heap.nonEmpty) ans(idx) = heap.head._1
    }

    ans
  }
}
```

## Rust

```rust
use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn min_interval(intervals: Vec<Vec<i32>>, queries: Vec<i32>) -> Vec<i32> {
        // Convert intervals to (left, right) tuples and sort by left endpoint
        let mut ivals: Vec<(i32, i32)> = intervals.into_iter().map(|v| (v[0], v[1])).collect();
        ivals.sort_by_key(|&(l, _)| l);

        // Pair each query with its original index and sort by query value
        let mut q_with_idx: Vec<(i32, usize)> = queries
            .iter()
            .cloned()
            .enumerate()
            .map(|(i, q)| (q, i))
            .collect();
        q_with_idx.sort_by_key(|&(q, _)| q);

        // Min-heap ordered by interval size; store (size, right)
        let mut heap: BinaryHeap<Reverse<(i32, i32)>> = BinaryHeap::new();

        let mut ans = vec![-1; queries.len()];
        let mut i = 0usize;

        for &(q, idx) in &q_with_idx {
            // Add all intervals whose left <= current query
            while i < ivals.len() && ivals[i].0 <= q {
                let (l, r) = ivals[i];
                let size = r - l + 1;
                heap.push(Reverse((size, r)));
                i += 1;
            }

            // Remove intervals that end before the query
            while let Some(&Reverse((_size, r))) = heap.peek() {
                if r < q {
                    heap.pop();
                } else {
                    break;
                }
            }

            // The smallest valid interval (if any) is at the top of the heap
            if let Some(&Reverse((size, _))) = heap.peek() {
                ans[idx] = size;
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (min-interval intervals queries)
  (-> (listof (listof exact-integer?)) (listof exact-integer?) (listof exact-integer?))
  (begin
    (require racket/heap)

    ;; sort intervals by left endpoint
    (define sorted-ints
      (sort intervals (lambda (a b) (< (first a) (first b)))))
    (define n (length sorted-ints))
    (define int-vec (list->vector sorted-ints))

    ;; pair each query with its original index and sort by query value
    (define indexed-queries
      (let loop ((qs queries) (idx 0) (acc '()))
        (if (null? qs)
            (reverse acc)
            (loop (cdr qs) (+ idx 1)
                  (cons (list (car qs) idx) acc)))))
    (define sorted-q
      (sort indexed-queries (lambda (a b) (< (first a) (first b)))))

    ;; min‑heap ordered by interval size, then by right endpoint
    (define heap
      (make-heap
       (lambda (x y)
         (let ((sx (first x)) (sy (first y)))
           (if (= sx sy)
               (< (second x) (second y))
               (< sx sy))))))

    ;; answer vector, default -1
    (define ans (make-vector (length queries) -1))

    ;; mutable index into intervals vector
    (define i-box (box 0))

    ;; process each query in increasing order
    (for-each
     (lambda (qr)
       (define qval (first qr))
       (define qidx (second qr))

       ;; add all intervals whose left <= qval
       (let loop ((i (unbox i-box)))
         (if (and (< i n) (<= (first (vector-ref int-vec i)) qval))
             (begin
               (define iv (vector-ref int-vec i))
               (define size (+ (- (second iv) (first iv)) 1))
               (heap-insert! heap (list size (second iv)))
               (loop (+ i 1)))
             (box-set! i-box i)))

       ;; discard intervals that end before qval
       (let clean ()
         (when (and (not (heap-empty? heap))
                    (< (second (heap-min heap)) qval))
           (heap-remove-min! heap)
           (clean)))

       ;; record answer
       (if (heap-empty? heap)
           (vector-set! ans qidx -1)
           (vector-set! ans qidx (first (heap-min heap)))))
     sorted-q)

    (vector->list ans)))
```

## Erlang

```erlang
-module(solution).
-export([min_interval/2]).

-spec min_interval(Intervals :: [[integer()]], Queries :: [integer()]) -> [integer()].
min_interval(Intervals, Queries) ->
    Tree0 = gb_trees:empty(),
    IndexedQueries = lists:zip(Queries, lists:seq(0, length(Queries) - 1)),
    QueryTree = build_tree(IndexedQueries, Tree0),
    Size = length(Queries),
    AnsArray0 = array:new(Size, [{default, -1}]),
    SortedIntervals = lists:keysort(
        1,
        [ {R - L + 1, L, R} || [L, R] <- Intervals ]
    ),
    {_FinalTree, FinalAnsArray} = process_intervals(SortedIntervals, QueryTree, AnsArray0),
    array:to_list(FinalAnsArray).

build_tree([], Tree) -> Tree;
build_tree([{Q, Idx} | Rest], Tree) ->
    case gb_trees:lookup(Q, Tree) of
        none ->
            NewTree = gb_trees:insert(Q, [Idx], Tree);
        {value, Ls} ->
            NewTree = gb_trees:update(Q, [Idx | Ls], Tree)
    end,
    build_tree(Rest, NewTree).

process_intervals([], Tree, Ans) -> {Tree, Ans};
process_intervals([{Len, L, R} | Rest], Tree, Ans) ->
    {NewTree, NewAns} = process_interval(Len, L, R, Tree, Ans),
    process_intervals(Rest, NewTree, NewAns).

process_interval(_Len, _L, _R, Tree, Ans) when Tree == gb_trees:empty() -> {Tree, Ans};
process_interval(Len, L, R, Tree, Ans) ->
    case gb_trees:iterator_from(L, Tree) of
        none -> {Tree, Ans};
        Iter ->
            case gb_trees:next(Iter) of
                none -> {Tree, Ans};
                {Key, IdxList, _} when Key =< R ->
                    UpdatedAns = assign_answers(IdxList, Len, Ans),
                    NewTree = gb_trees:delete(Key, Tree),
                    process_interval(Len, L, R, NewTree, UpdatedAns);
                {_Key, _IdxList, _} ->
                    {Tree, Ans}
            end
    end.

assign_answers([], _Len, Ans) -> Ans;
assign_answers([Idx | Rest], Len, Ans) ->
    NewAns = array:set(Idx, Len, Ans),
    assign_answers(Rest, Len, NewAns).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_interval(intervals :: [[integer]], queries :: [integer]) :: [integer]
  def min_interval(intervals, queries) do
    sorted_intervals = Enum.sort_by(intervals, fn [l, _r] -> l end)

    indexed_queries =
      queries
      |> Enum.with_index()
      |> Enum.sort_by(fn {q, _i} -> q end)

    {answers_rev, _tree, _remaining, _uid} =
      Enum.reduce(indexed_queries, {[], :gb_trees.empty(), sorted_intervals, 0}, fn {q, idx},
                                                                              {acc, tree, rem_ints, uid} ->
        {tree2, rem2, uid2} = add_until(rem_ints, q, tree, uid)
        {ans, tree3} = query_answer(tree2, q)
        {[{idx, ans} | acc], tree3, rem2, uid2}
      end)

    answers_rev
    |> Enum.sort_by(fn {i, _a} -> i end)
    |> Enum.map(fn {_i, a} -> a end)
  end

  # Insert all intervals whose left <= q into the tree.
  defp add_until([], _q, tree, uid), do: {tree, [], uid}

  defp add_until([[l, r] | rest] = list, q, tree, uid) when l <= q do
    size = r - l + 1
    key = {size, uid}
    new_tree = :gb_trees.insert(key, r, tree)
    add_until(rest, q, new_tree, uid + 1)
  end

  defp add_until(list, _q, tree, uid), do: {tree, list, uid}

  # Retrieve the smallest interval covering q, cleaning up expired ones.
  defp query_answer(tree, q) do
    if :gb_trees.is_empty(tree) do
      {-1, tree}
    else
      {{size, uid}, r} = :gb_trees.smallest(tree)

      if r < q do
        new_tree = :gb_trees.delete_any({size, uid}, tree)
        query_answer(new_tree, q)
      else
        {size, tree}
      end
    end
  end
end
```
