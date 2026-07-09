# 1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows

## Cpp

```cpp
class Solution {
public:
    int kthSmallest(vector<vector<int>>& mat, int k) {
        vector<int> cur = mat[0];
        if ((int)cur.size() > k) cur.resize(k);
        for (size_t r = 1; r < mat.size(); ++r) {
            const vector<int>& row = mat[r];
            int limitRow = min((int)row.size(), k);
            using T = tuple<int,int,int>; // sum, idx in cur, idx in row
            priority_queue<T, vector<T>, greater<T>> pq;
            for (int i = 0; i < (int)cur.size(); ++i) {
                pq.emplace(cur[i] + row[0], i, 0);
            }
            vector<int> nxt;
            while (!pq.empty() && (int)nxt.size() < k) {
                auto [s, i, j] = pq.top();
                pq.pop();
                nxt.push_back(s);
                if (j + 1 < limitRow) {
                    pq.emplace(cur[i] + row[j + 1], i, j + 1);
                }
            }
            cur.swap(nxt);
        }
        return cur[k - 1];
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int kthSmallest(int[][] mat, int k) {
        int m = mat.length;
        // Initialize with the first row's smallest elements
        List<Integer> cur = new ArrayList<>();
        for (int j = 0; j < Math.min(k, mat[0].length); ++j) {
            cur.add(mat[0][j]);
        }

        // Process each subsequent row
        for (int i = 1; i < m; ++i) {
            int[] row = mat[i];
            PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
            int curSize = cur.size();

            // Seed the heap with sums using the first element of the current row
            for (int idx = 0; idx < curSize; ++idx) {
                int sum = cur.get(idx) + row[0];
                pq.offer(new int[]{sum, idx, 0}); // {totalSum, indexInCur, indexInRow}
            }

            List<Integer> next = new ArrayList<>();
            while (next.size() < k && !pq.isEmpty()) {
                int[] top = pq.poll();
                int total = top[0];
                int idxCur = top[1];
                int idxRow = top[2];

                next.add(total);

                // Push the next candidate from the same cur sum with next element in row
                if (idxRow + 1 < row.length) {
                    int newSum = cur.get(idxCur) + row[idxRow + 1];
                    pq.offer(new int[]{newSum, idxCur, idxRow + 1});
                }
            }

            cur = next;
        }

        return cur.get(k - 1);
    }
}
```

## Python

```python
class Solution(object):
    def kthSmallest(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: int
        """
        import heapq

        # start with the first row's smallest elements (up to k)
        cur = mat[0][:k]

        for idx in range(1, len(mat)):
            row = mat[idx]
            # heap will store tuples: (sum, i, j) where sum = cur[i] + row[j]
            heap = []
            limit_i = min(k, len(cur))
            for i in range(limit_i):
                heapq.heappush(heap, (cur[i] + row[0], i, 0))

            new_cur = []
            while heap and len(new_cur) < k:
                s, i, j = heapq.heappop(heap)
                new_cur.append(s)
                if j + 1 < len(row):
                    heapq.heappush(heap, (cur[i] + row[j + 1], i, j + 1))
            cur = new_cur

        return cur[k - 1]
```

## Python3

```python
from typing import List
import heapq

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        # start with the first row (already sorted)
        cur = mat[0][:k]
        for row in mat[1:]:
            heap = []
            visited = set()
            # initial pair (0,0)
            heapq.heappush(heap, (cur[0] + row[0], 0, 0))
            visited.add((0, 0))
            nxt = []
            while len(nxt) < k and heap:
                s, i, j = heapq.heappop(heap)
                nxt.append(s)
                if i + 1 < len(cur):
                    ni = (i + 1, j)
                    if ni not in visited:
                        heapq.heappush(heap, (cur[i + 1] + row[j], i + 1, j))
                        visited.add(ni)
                if j + 1 < len(row):
                    nj = (i, j + 1)
                    if nj not in visited:
                        heapq.heappush(heap, (cur[i] + row[j + 1], i, j + 1))
                        visited.add(nj)
            cur = nxt
        return cur[k - 1]
```

## C

```c
#include <stdlib.h>
#include <string.h>

struct HeapNode {
    int sum;
    int i;
    int j;
};

typedef struct {
    struct HeapNode *data;
    int size;
    int capacity;
} MinHeap;

static void heapSwap(struct HeapNode *a, struct HeapNode *b) {
    struct HeapNode tmp = *a;
    *a = *b;
    *b = tmp;
}

static void heapPush(MinHeap *h, struct HeapNode node) {
    if (h->size == h->capacity) {
        h->capacity = h->capacity ? h->capacity * 2 : 4;
        h->data = realloc(h->data, h->capacity * sizeof(struct HeapNode));
    }
    int idx = h->size++;
    h->data[idx] = node;
    while (idx > 0) {
        int parent = (idx - 1) / 2;
        if (h->data[parent].sum <= h->data[idx].sum) break;
        heapSwap(&h->data[parent], &h->data[idx]);
        idx = parent;
    }
}

static struct HeapNode heapPop(MinHeap *h) {
    struct HeapNode top = h->data[0];
    h->data[0] = h->data[--h->size];
    int idx = 0;
    while (1) {
        int left = idx * 2 + 1, right = left + 1, smallest = idx;
        if (left < h->size && h->data[left].sum < h->data[smallest].sum) smallest = left;
        if (right < h->size && h->data[right].sum < h->data[smallest].sum) smallest = right;
        if (smallest == idx) break;
        heapSwap(&h->data[idx], &h->data[smallest]);
        idx = smallest;
    }
    return top;
}

int kthSmallest(int** mat, int matSize, int* matColSize, int k) {
    int m = matSize;
    int n = matColSize[0];
    int maxK = k;

    int *sums = (int *)malloc(maxK * sizeof(int));
    int curSize = n < k ? n : k;
    for (int i = 0; i < curSize; ++i) sums[i] = mat[0][i];

    for (int r = 1; r < m; ++r) {
        int *newSums = (int *)malloc(maxK * sizeof(int));
        int newSize = 0;

        MinHeap heap = {NULL, 0, 0};

        static char visited[205][45];
        memset(visited, 0, sizeof(visited));

        for (int i = 0; i < curSize && i < maxK; ++i) {
            struct HeapNode node;
            node.sum = sums[i] + mat[r][0];
            node.i = i;
            node.j = 0;
            heapPush(&heap, node);
            visited[i][0] = 1;
        }

        while (newSize < maxK && heap.size > 0) {
            struct HeapNode cur = heapPop(&heap);
            newSums[newSize++] = cur.sum;

            int iIdx = cur.i, jIdx = cur.j;
            if (jIdx + 1 < n && !visited[iIdx][jIdx + 1]) {
                struct HeapNode nxt;
                nxt.sum = sums[iIdx] + mat[r][jIdx + 1];
                nxt.i = iIdx;
                nxt.j = jIdx + 1;
                heapPush(&heap, nxt);
                visited[iIdx][jIdx + 1] = 1;
            }
        }

        free(sums);
        free(heap.data);
        sums = newSums;
        curSize = newSize;
    }

    int ans = sums[k - 1];
    free(sums);
    return ans;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int KthSmallest(int[][] mat, int k) {
        List<int> cur = new List<int>(mat[0]);
        if (cur.Count > k) cur = cur.GetRange(0, k);
        for (int r = 1; r < mat.Length; ++r) {
            int[] row = mat[r];
            var pq = new PriorityQueue<(int sum, int i, int j), int>();
            var visited = new HashSet<(int, int)>();
            pq.Enqueue((cur[0] + row[0], 0, 0), cur[0] + row[0]);
            visited.Add((0, 0));
            List<int> next = new List<int>();
            while (next.Count < k && pq.Count > 0) {
                var node = pq.Dequeue();
                int sum = node.sum;
                int iIdx = node.i;
                int jIdx = node.j;
                next.Add(sum);
                if (jIdx + 1 < row.Length && !visited.Contains((iIdx, jIdx + 1))) {
                    pq.Enqueue((cur[iIdx] + row[jIdx + 1], iIdx, jIdx + 1), cur[iIdx] + row[jIdx + 1]);
                    visited.Add((iIdx, jIdx + 1));
                }
                if (jIdx == 0 && iIdx + 1 < cur.Count && !visited.Contains((iIdx + 1, 0))) {
                    pq.Enqueue((cur[iIdx + 1] + row[0], iIdx + 1, 0), cur[iIdx + 1] + row[0]);
                    visited.Add((iIdx + 1, 0));
                }
            }
            cur = next;
        }
        return cur[k - 1];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} mat
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function(mat, k) {
    // Min-heap implementation
    class MinHeap {
        constructor() {
            this.heap = [];
        }
        push(node) {
            const h = this.heap;
            h.push(node);
            let i = h.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (h[p].sum <= h[i].sum) break;
                [h[p], h[i]] = [h[i], h[p]];
                i = p;
            }
        }
        pop() {
            const h = this.heap;
            if (h.length === 0) return null;
            const root = h[0];
            const last = h.pop();
            if (h.length > 0) {
                h[0] = last;
                let i = 0;
                while (true) {
                    let l = i * 2 + 1,
                        r = l + 1,
                        smallest = i;
                    if (l < h.length && h[l].sum < h[smallest].sum) smallest = l;
                    if (r < h.length && h[r].sum < h[smallest].sum) smallest = r;
                    if (smallest === i) break;
                    [h[i], h[smallest]] = [h[smallest], h[i]];
                    i = smallest;
                }
            }
            return root;
        }
        size() {
            return this.heap.length;
        }
    }

    // start with the first row's smallest k elements
    let sums = mat[0].slice(0, Math.min(k, mat[0].length));

    for (let rowIdx = 1; rowIdx < mat.length; ++rowIdx) {
        const row = mat[rowIdx];
        const heap = new MinHeap();
        const limitA = Math.min(k, sums.length);
        // initialize heap with pairing each sum with the first element of current row
        for (let i = 0; i < limitA; ++i) {
            heap.push({ sum: sums[i] + row[0], i: i, j: 0 });
        }
        const nextSums = [];
        while (nextSums.length < k && heap.size() > 0) {
            const cur = heap.pop();
            nextSums.push(cur.sum);
            if (cur.j + 1 < row.length) {
                heap.push({
                    sum: sums[cur.i] + row[cur.j + 1],
                    i: cur.i,
                    j: cur.j + 1
                });
            }
        }
        sums = nextSums;
    }

    return sums[k - 1];
};
```

## Typescript

```typescript
function kthSmallest(mat: number[][], k: number): number {
    class MinHeap<T> {
        private data: T[] = [];
        constructor(private compare: (a: T, b: T) => boolean) {}
        size(): number { return this.data.length; }
        push(item: T): void {
            this.data.push(item);
            let idx = this.data.length - 1;
            while (idx > 0) {
                const parent = (idx - 1) >> 1;
                if (!this.compare(this.data[idx], this.data[parent])) break;
                [this.data[idx], this.data[parent]] = [this.data[parent], this.data[idx]];
                idx = parent;
            }
        }
        pop(): T | undefined {
            if (this.data.length === 0) return undefined;
            const top = this.data[0];
            const last = this.data.pop()!;
            if (this.data.length > 0) {
                this.data[0] = last;
                let idx = 0;
                const n = this.data.length;
                while (true) {
                    let left = idx * 2 + 1;
                    let right = left + 1;
                    let smallest = idx;
                    if (left < n && this.compare(this.data[left], this.data[smallest])) smallest = left;
                    if (right < n && this.compare(this.data[right], this.data[smallest])) smallest = right;
                    if (smallest === idx) break;
                    [this.data[idx], this.data[smallest]] = [this.data[smallest], this.data[idx]];
                    idx = smallest;
                }
            }
            return top;
        }
    }

    // start with the first row, keep only up to k smallest elements
    let cur: number[] = mat[0].slice(0, Math.min(k, mat[0].length));

    for (let r = 1; r < mat.length; ++r) {
        const row = mat[r];
        const heap = new MinHeap<{ sum: number; i: number; j: number }>((a, b) => a.sum < b.sum);
        const limitA = Math.min(cur.length, k);
        for (let i = 0; i < limitA; ++i) {
            heap.push({ sum: cur[i] + row[0], i, j: 0 });
        }
        const next: number[] = [];
        while (next.length < k && heap.size() > 0) {
            const { sum, i, j } = heap.pop()!;
            next.push(sum);
            if (j + 1 < row.length) {
                heap.push({ sum: cur[i] + row[j + 1], i, j: j + 1 });
            }
        }
        cur = next;
    }

    return cur[k - 1];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $mat
     * @param Integer $k
     * @return Integer
     */
    function kthSmallest($mat, $k) {
        // start with the first row sorted and trimmed to k elements
        $cur = $mat[0];
        sort($cur);
        if (count($cur) > $k) {
            $cur = array_slice($cur, 0, $k);
        }

        $rows = count($mat);
        for ($i = 1; $i < $rows; $i++) {
            $row = $mat[$i];
            sort($row);
            if (count($row) > $k) {
                $row = array_slice($row, 0, $k);
            }
            $cur = $this->mergeKSmallest($cur, $row, $k);
        }

        return $cur[$k - 1];
    }

    /**
     * Merge two sorted arrays to get the k smallest sums.
     *
     * @param array $a
     * @param array $b
     * @param int   $k
     * @return array
     */
    private function mergeKSmallest($a, $b, $k) {
        $m = count($a);
        $n = count($b);

        $heap = new SplPriorityQueue();
        // we only need the data when extracting
        $heap->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        $visited = [];

        // initial pair (0,0)
        $sum = $a[0] + $b[0];
        $heap->insert([$sum, 0, 0], -$sum);
        $visited["0#0"] = true;

        $res = [];
        while (count($res) < $k && !$heap->isEmpty()) {
            [$s, $i, $j] = $heap->extract();
            $res[] = $s;

            if ($i + 1 < $m) {
                $key = ($i + 1) . '#' . $j;
                if (!isset($visited[$key])) {
                    $newSum = $a[$i + 1] + $b[$j];
                    $heap->insert([$newSum, $i + 1, $j], -$newSum);
                    $visited[$key] = true;
                }
            }

            if ($j + 1 < $n) {
                $key = $i . '#' . ($j + 1);
                if (!isset($visited[$key])) {
                    $newSum = $a[$i] + $b[$j + 1];
                    $heap->insert([$newSum, $i, $j + 1], -$newSum);
                    $visited[$key] = true;
                }
            }
        }

        return $res;
    }
}
```

## Swift

```swift
class Solution {
    struct Node {
        var sum: Int
        var i: Int
        var j: Int
    }
    struct MinHeap {
        private var heap = [Node]()
        var isEmpty: Bool { heap.isEmpty }
        mutating func push(_ node: Node) {
            heap.append(node)
            siftUp(heap.count - 1)
        }
        mutating func pop() -> Node? {
            guard !heap.isEmpty else { return nil }
            let top = heap[0]
            let last = heap.removeLast()
            if !heap.isEmpty {
                heap[0] = last
                siftDown(0)
            }
            return top
        }
        private mutating func siftUp(_ index: Int) {
            var child = index
            while child > 0 {
                let parent = (child - 1) >> 1
                if heap[child].sum < heap[parent].sum {
                    heap.swapAt(child, parent)
                    child = parent
                } else { break }
            }
        }
        private mutating func siftDown(_ index: Int) {
            var parent = index
            while true {
                let left = parent * 2 + 1
                let right = left + 1
                var smallest = parent
                if left < heap.count && heap[left].sum < heap[smallest].sum {
                    smallest = left
                }
                if right < heap.count && heap[right].sum < heap[smallest].sum {
                    smallest = right
                }
                if smallest == parent { break }
                heap.swapAt(parent, smallest)
                parent = smallest
            }
        }
    }

    func kthSmallest(_ mat: [[Int]], _ k: Int) -> Int {
        var cur = Array(mat[0].prefix(min(k, mat[0].count)))
        for r in 1..<mat.count {
            let row = mat[r]
            var heap = MinHeap()
            for i in 0..<cur.count {
                heap.push(Node(sum: cur[i] + row[0], i: i, j: 0))
            }
            var next = [Int]()
            while next.count < k && !heap.isEmpty {
                let node = heap.pop()!
                next.append(node.sum)
                if node.j + 1 < row.count {
                    heap.push(Node(sum: cur[node.i] + row[node.j + 1], i: node.i, j: node.j + 1))
                }
            }
            cur = next
        }
        return cur[k - 1]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun kthSmallest(mat: Array<IntArray>, k: Int): Int {
        var sums = mat[0].take(k).toMutableList()
        for (rowIdx in 1 until mat.size) {
            val row = mat[rowIdx]
            val pq = java.util.PriorityQueue<Node>(compareBy { it.sum })
            val limit = minOf(k, sums.size)
            for (i in 0 until limit) {
                pq.offer(Node(sums[i] + row[0], i, 0))
            }
            val newSums = mutableListOf<Int>()
            while (newSums.size < k && pq.isNotEmpty()) {
                val cur = pq.poll()
                newSums.add(cur.sum)
                if (cur.j + 1 < row.size) {
                    pq.offer(Node(sums[cur.i] + row[cur.j + 1], cur.i, cur.j + 1))
                }
            }
            sums = newSums
        }
        return sums[k - 1]
    }

    private data class Node(val sum: Int, val i: Int, val j: Int)
}
```

## Dart

```dart
class HeapNode {
  int sum;
  int i;
  int j;
  HeapNode(this.sum, this.i, this.j);
}

class MinHeap {
  final List<HeapNode> _data = [];

  bool get isEmpty => _data.isEmpty;

  void push(HeapNode node) {
    _data.add(node);
    _siftUp(_data.length - 1);
  }

  HeapNode pop() {
    var res = _data[0];
    var last = _data.removeLast();
    if (_data.isNotEmpty) {
      _data[0] = last;
      _siftDown(0);
    }
    return res;
  }

  void _siftUp(int idx) {
    while (idx > 0) {
      int parent = (idx - 1) >> 1;
      if (_data[parent].sum <= _data[idx].sum) break;
      var tmp = _data[parent];
      _data[parent] = _data[idx];
      _data[idx] = tmp;
      idx = parent;
    }
  }

  void _siftDown(int idx) {
    int n = _data.length;
    while (true) {
      int left = idx * 2 + 1;
      int right = left + 1;
      int smallest = idx;
      if (left < n && _data[left].sum < _data[smallest].sum) smallest = left;
      if (right < n && _data[right].sum < _data[smallest].sum) smallest = right;
      if (smallest == idx) break;
      var tmp = _data[idx];
      _data[idx] = _data[smallest];
      _data[smallest] = tmp;
      idx = smallest;
    }
  }
}

class Solution {
  List<int> _combine(List<int> a, List<int> b, int k) {
    int lenA = a.length;
    int lenB = b.length;
    int limitA = lenA < k ? lenA : k;

    var heap = MinHeap();
    var visited = <int>{};

    for (int i = 0; i < limitA; ++i) {
      heap.push(HeapNode(a[i] + b[0], i, 0));
      visited.add(i * lenB);
    }

    var res = <int>[];
    while (res.length < k && !heap.isEmpty) {
      var node = heap.pop();
      res.add(node.sum);
      int i = node.i;
      int j = node.j;
      if (j + 1 < lenB) {
        int key = i * lenB + (j + 1);
        if (!visited.contains(key)) {
          heap.push(HeapNode(a[i] + b[j + 1], i, j + 1));
          visited.add(key);
        }
      }
    }
    return res;
  }

  int kthSmallest(List<List<int>> mat, int k) {
    List<int> cur = List.from(mat[0]);
    cur.sort();
    for (int r = 1; r < mat.length; ++r) {
      var row = List.from(mat[r]);
      row.sort();
      cur = _combine(cur, row, k);
    }
    return cur[k - 1];
  }
}
```

## Golang

```go
package main

import (
	"container/heap"
)

type node struct {
	sum int
	i   int // index in cur slice
	j   int // index in current row
}

type minHeap []node

func (h minHeap) Len() int            { return len(h) }
func (h minHeap) Less(a, b int) bool  { return h[a].sum < h[b].sum }
func (h minHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *minHeap) Push(x interface{}) { *h = append(*h, x.(node)) }
func (h *minHeap) Pop() interface{} {
	old := *h
	n := len(old)
	it := old[n-1]
	*h = old[:n-1]
	return it
}

func kthSmallest(mat [][]int, k int) int {
	if len(mat) == 0 {
		return 0
	}
	// initialize cur with first row (up to k elements)
	curLen := len(mat[0])
	if curLen > k {
		curLen = k
	}
	cur := make([]int, curLen)
	copy(cur, mat[0][:curLen])

	for r := 1; r < len(mat); r++ {
		row := mat[r]
		h := &minHeap{}
		heap.Init(h)

		// push initial pairs (each element from cur with row[0])
		for i := 0; i < len(cur); i++ {
			heap.Push(h, node{sum: cur[i] + row[0], i: i, j: 0})
		}

		newCur := make([]int, 0, k)
		for len(newCur) < k && h.Len() > 0 {
			it := heap.Pop(h).(node)
			newCur = append(newCur, it.sum)

			if it.j+1 < len(row) {
				heap.Push(h, node{sum: cur[it.i] + row[it.j+1], i: it.i, j: it.j + 1})
			}
		}
		cur = newCur
	}

	return cur[k-1]
}
```

## Ruby

```ruby
class MinHeap
  def initialize
    @data = []
  end

  def push(item)
    @data << item
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

# @param {Integer[][]} mat
# @param {Integer} k
# @return {Integer}
def kth_smallest(mat, k)
  cur = mat[0][0...k] # initial sums from first row (already sorted)

  (1...mat.size).each do |row_idx|
    row = mat[row_idx]
    heap = MinHeap.new

    cur.each_with_index do |s, i|
      heap.push([s + row[0], i, 0])
    end

    next_cur = []
    while next_cur.size < k && !heap.empty?
      sum, i, j = heap.pop
      next_cur << sum
      if j + 1 < row.size
        new_sum = cur[i] + row[j + 1]
        heap.push([new_sum, i, j + 1])
      end
    end

    cur = next_cur
  end

  cur[k - 1]
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable
  import java.util.PriorityQueue

  def kthSmallest(mat: Array[Array[Int]], k: Int): Int = {
    var sums: Array[Int] = mat(0).take(k)
    for (rowIdx <- 1 until mat.length) {
      val row = mat(rowIdx)
      val pq = new PriorityQueue[(Int, Int, Int)](
        (a: (Int, Int, Int), b: (Int, Int, Int)) => Integer.compare(a._1, b._1)
      )
      val visited = mutable.HashSet[(Int, Int)]()
      val limitPrev = math.min(sums.length, k)
      for (i <- 0 until limitPrev) {
        pq.offer((sums(i) + row(0), i, 0))
        visited.add((i, 0))
      }
      val newSums = mutable.ArrayBuffer[Int]()
      while (newSums.size < k && !pq.isEmpty) {
        val cur = pq.poll()
        val curSum = cur._1
        val i = cur._2
        val j = cur._3
        newSums += curSum
        if (j + 1 < row.length) {
          val key = (i, j + 1)
          if (!visited.contains(key)) {
            pq.offer((sums(i) + row(j + 1), i, j + 1))
            visited.add(key)
          }
        }
      }
      sums = newSums.toArray
    }
    sums(k - 1)
  }
}
```

## Rust

```rust
impl Solution {
    pub fn kth_smallest(mat: Vec<Vec<i32>>, k: i32) -> i32 {
        use std::cmp::Reverse;
        use std::collections::BinaryHeap;

        let mut cur = mat[0].clone();
        let k_usize = k as usize;
        if cur.len() > k_usize {
            cur.truncate(k_usize);
        }

        for row in mat.iter().skip(1) {
            let mut heap: BinaryHeap<Reverse<(i32, usize, usize)>> = BinaryHeap::new();
            let limit_cur = cur.len();

            for i in 0..limit_cur {
                heap.push(Reverse((cur[i] + row[0], i, 0)));
            }

            let mut next: Vec<i32> = Vec::with_capacity(k_usize);
            while next.len() < k_usize && !heap.is_empty() {
                if let Reverse((sum, i_idx, j_idx)) = heap.pop().unwrap() {
                    next.push(sum);
                    if j_idx + 1 < row.len() {
                        heap.push(Reverse((cur[i_idx] + row[j_idx + 1], i_idx, j_idx + 1)));
                    }
                }
            }

            cur = next;
        }

        cur[k_usize - 1]
    }
}
```

## Racket

```racket
(require racket/heap)

(define (k-smallest-sums a b k)
  (let* ([lenA (vector-length a)]
         [lenB (vector-length b)]
         [heap (make-heap (lambda (x y) (< (first x) (first y))))]
         [visited (make-hash)])
    (when (and (> lenA 0) (> lenB 0))
      (let ([init (list (+ (vector-ref a 0) (vector-ref b 0)) 0 0)])
        (heap-add! heap init)
        (hash-set! visited (list 0 0) #t)))
    (let loop ((result '()))
      (if (or (= (length result) k) (heap-empty? heap))
          (reverse result)
          (let* ([node (heap-remove-min! heap)]
                 [sum (first node)] [i (second node)] [j (third node)])
            (define (push-if ii jj)
              (when (and (< ii lenA) (< jj lenB))
                (unless (hash-has-key? visited (list ii jj))
                  (let ([new-sum (+ (vector-ref a ii) (vector-ref b jj))])
                    (heap-add! heap (list new-sum ii jj))
                    (hash-set! visited (list ii jj) #t)))))
            (push-if (+ i 1) j)
            (push-if i (+ j 1))
            (loop (cons sum result))))))))

(define/contract (kth-smallest mat k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ([rows (map list->vector mat)]
         [m (length rows)])
    (if (= m 0)
        0
        (let loop ((idx 1)
                   (sums (vector->list (list-ref rows 0))))
          (if (>= idx m)
              (list-ref sums (- k 1))
              (let* ([row (list-ref rows idx)]
                     [new-sums (k-smallest-sums (list->vector sums) row
                                                (min k (* (length sums) (vector-length row))))])
                (loop (+ idx 1) new-sums)))))))
```

## Erlang

```erlang
-module(solution).
-export([kth_smallest/2]).

kth_smallest(Mat, K) ->
    [FirstRow | RestRows] = Mat,
    Sums0 = FirstRow,
    Sums = lists:foldl(fun(Row, Acc) -> combine(Acc, Row, K) end, Sums0, RestRows),
    lists:nth(K, Sums).

combine(Sums, Row, K) ->
    LenR = length(Row),
    Heap0 = init_heap(Sums, Row, 1),
    combine_loop(Heap0, Sums, Row, LenR, K, []).

init_heap(Sums, Row, J) ->
    Indexed = indexed_list(Sums, 1),
    lists:foldl(fun({SumI, I}, Acc) ->
        Total = SumI + lists:nth(J, Row),
        insert_sorted({Total, I, J}, Acc)
    end, [], Indexed).

indexed_list(List, Start) -> indexed_list(List, Start, []).

indexed_list([], _, Acc) -> lists:reverse(Acc);
indexed_list([H|T], I, Acc) -> indexed_list(T, I+1, [{H, I}|Acc]).

combine_loop(_, _, _, _, K, Result) when length(Result) =:= K ->
    lists:reverse(Result);
combine_loop([], _, _, _, _, Result) ->
    lists:reverse(Result);
combine_loop([MinTuple | RestHeap], Sums, Row, LenR, K, Result) ->
    {Total, I, J} = MinTuple,
    NewResult = [Total | Result],
    NewHeap =
        if J < LenR ->
                NextJ = J + 1,
                SumI = lists:nth(I, Sums),
                NewTotal = SumI + lists:nth(NextJ, Row),
                insert_sorted({NewTotal, I, NextJ}, RestHeap);
           true -> RestHeap
        end,
    combine_loop(NewHeap, Sums, Row, LenR, K, NewResult).

insert_sorted(Tuple, []) -> [Tuple];
insert_sorted({Total,_ ,_}=T, [H|Tail]=Heap) ->
    case Total =< element(1, H) of
        true -> [T | Heap];
        false -> [H | insert_sorted(T, Tail)]
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec kth_smallest(mat :: [[integer]], k :: integer) :: integer
  def kth_smallest([first_row | rest_rows], k) do
    # start with the smallest k elements from the first row (already sorted)
    init = Enum.take(first_row, k)

    final_sums =
      Enum.reduce(rest_rows, init, fn row, acc ->
        combined =
          for sum <- acc,
              val <- row do
            sum + val
          end

        combined
        |> Enum.sort()
        |> Enum.take(k)
      end)

    Enum.at(final_sums, k - 1)
  end
end
```
