# 0373. Find K Pairs with Smallest Sums

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        vector<vector<int>> result;
        if (nums1.empty() || nums2.empty() || k == 0) return result;
        struct Node {
            long long sum;
            int i, j;
            bool operator>(const Node& other) const { return sum > other.sum; }
        };
        priority_queue<Node, vector<Node>, greater<Node>> minHeap;
        unordered_set<long long> visited;
        auto encode = [&](int i, int j)->long long {
            return (static_cast<long long>(i) << 32) | static_cast<unsigned int>(j);
        };
        minHeap.push({static_cast<long long>(nums1[0]) + nums2[0], 0, 0});
        visited.insert(encode(0, 0));
        while (k-- > 0 && !minHeap.empty()) {
            Node cur = minHeap.top();
            minHeap.pop();
            result.push_back({nums1[cur.i], nums2[cur.j]});
            if (cur.i + 1 < (int)nums1.size()) {
                long long key = encode(cur.i + 1, cur.j);
                if (!visited.count(key)) {
                    visited.insert(key);
                    minHeap.push({static_cast<long long>(nums1[cur.i + 1]) + nums2[cur.j], cur.i + 1, cur.j});
                }
            }
            if (cur.j + 1 < (int)nums2.size()) {
                long long key = encode(cur.i, cur.j + 1);
                if (!visited.count(key)) {
                    visited.insert(key);
                    minHeap.push({static_cast<long long>(nums1[cur.i]) + nums2[cur.j + 1], cur.i, cur.j + 1});
                }
            }
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        List<List<Integer>> result = new ArrayList<>();
        if (nums1 == null || nums2 == null || nums1.length == 0 || nums2.length == 0 || k <= 0) {
            return result;
        }
        PriorityQueue<Node> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a.sum));
        int limit = Math.min(nums1.length, k);
        for (int i = 0; i < limit; i++) {
            pq.offer(new Node(nums1[i] + nums2[0], i, 0));
        }
        while (k > 0 && !pq.isEmpty()) {
            Node cur = pq.poll();
            List<Integer> pair = new ArrayList<>(2);
            pair.add(nums1[cur.i]);
            pair.add(nums2[cur.j]);
            result.add(pair);
            k--;
            if (cur.j + 1 < nums2.length) {
                pq.offer(new Node(nums1[cur.i] + nums2[cur.j + 1], cur.i, cur.j + 1));
            }
        }
        return result;
    }

    private static class Node {
        int sum;
        int i;
        int j;

        Node(int sum, int i, int j) {
            this.sum = sum;
            this.i = i;
            this.j = j;
        }
    }
}
```

## Python

```python
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2 or k == 0:
            return []
        import heapq
        m, n = len(nums1), len(nums2)
        heap = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, m))]
        heapq.heapify(heap)
        res = []
        while heap and k > 0:
            s, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < n:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
            k -= 1
        return res
```

## Python3

```python
class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        import heapq
        if not nums1 or not nums2 or k == 0:
            return []
        m, n = len(nums1), len(nums2)
        heap = [(nums1[0] + nums2[0], 0, 0)]
        visited = {(0, 0)}
        ans = []
        while heap and len(ans) < k:
            s, i, j = heapq.heappop(heap)
            ans.append([nums1[i], nums2[j]])
            if i + 1 < m and (i + 1, j) not in visited:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))
            if j + 1 < n and (i, j + 1) not in visited:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))
        return ans
```

## C

```c
#include <stdlib.h>
#include <limits.h>

typedef struct {
    long sum;
    int i;
    int j;
} HeapNode;

/* Min-heap utilities */
static void heapSwap(HeapNode *a, HeapNode *b) {
    HeapNode tmp = *a;
    *a = *b;
    *b = tmp;
}

static void heapPush(HeapNode *heap, int *size, HeapNode node) {
    int idx = (*size)++;
    heap[idx] = node;
    while (idx > 0) {
        int parent = (idx - 1) >> 1;
        if (heap[parent].sum <= heap[idx].sum) break;
        heapSwap(&heap[parent], &heap[idx]);
        idx = parent;
    }
}

static HeapNode heapPop(HeapNode *heap, int *size) {
    HeapNode top = heap[0];
    heap[0] = heap[--(*size)];
    int idx = 0;
    while (1) {
        int left = (idx << 1) + 1;
        int right = left + 1;
        if (left >= *size) break;
        int smallest = left;
        if (right < *size && heap[right].sum < heap[left].sum)
            smallest = right;
        if (heap[idx].sum <= heap[smallest].sum) break;
        heapSwap(&heap[idx], &heap[smallest]);
        idx = smallest;
    }
    return top;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** kSmallestPairs(int* nums1, int nums1Size, int* nums2, int nums2Size,
                     int k, int* returnSize, int*** returnColumnSizes) {
    (void)returnColumnSizes; // suppress unused warning if not needed
    *returnSize = 0;
    if (nums1Size == 0 || nums2Size == 0 || k == 0) {
        return NULL;
    }

    long totalPairs = (long)nums1Size * (long)nums2Size;
    int limit = k < totalPairs ? k : (int)totalPairs;

    int **result = (int **)malloc(limit * sizeof(int *));
    int *colSizes = (int *)malloc(limit * sizeof(int));

    /* Heap capacity: at most min(nums1Size, k) initial elements plus pushes */
    int heapCap = (nums1Size < k ? nums1Size : k) + limit;
    HeapNode *heap = (HeapNode *)malloc(heapCap * sizeof(HeapNode));
    int heapSize = 0;

    int init = nums1Size < k ? nums1Size : k;
    for (int i = 0; i < init; ++i) {
        HeapNode node;
        node.sum = (long)nums1[i] + (long)nums2[0];
        node.i = i;
        node.j = 0;
        heapPush(heap, &heapSize, node);
    }

    int count = 0;
    while (count < limit && heapSize > 0) {
        HeapNode cur = heapPop(heap, &heapSize);
        int *pair = (int *)malloc(2 * sizeof(int));
        pair[0] = nums1[cur.i];
        pair[1] = nums2[cur.j];
        result[count] = pair;
        colSizes[count] = 2;
        ++count;

        if (cur.j + 1 < nums2Size) {
            HeapNode nxt;
            nxt.sum = (long)nums1[cur.i] + (long)nums2[cur.j + 1];
            nxt.i = cur.i;
            nxt.j = cur.j + 1;
            heapPush(heap, &heapSize, nxt);
        }
    }

    free(heap);
    *returnSize = count;
    *returnColumnSizes = &colSizes;
    return result;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<IList<int>> KSmallestPairs(int[] nums1, int[] nums2, int k) {
        var result = new List<IList<int>>();
        if (nums1.Length == 0 || nums2.Length == 0 || k == 0)
            return result;

        var visited = new HashSet<(int, int)>();
        var pq = new PriorityQueue<(int i, int j), long>();

        pq.Enqueue((0, 0), (long)nums1[0] + nums2[0]);
        visited.Add((0, 0));

        while (pq.Count > 0 && result.Count < k) {
            var (i, j) = pq.Dequeue();
            result.Add(new List<int> { nums1[i], nums2[j] });

            if (i + 1 < nums1.Length && !visited.Contains((i + 1, j))) {
                visited.Add((i + 1, j));
                pq.Enqueue((i + 1, j), (long)nums1[i + 1] + nums2[j]);
            }
            if (j + 1 < nums2.Length && !visited.Contains((i, j + 1))) {
                visited.Add((i, j + 1));
                pq.Enqueue((i, j + 1), (long)nums1[i] + nums2[j + 1]);
            }
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} k
 * @return {number[][]}
 */
var kSmallestPairs = function(nums1, nums2, k) {
    const m = nums1.length, n = nums2.length;
    if (m === 0 || n === 0 || k === 0) return [];

    class MinHeap {
        constructor() { this.heap = []; }
        push(node) {
            this.heap.push(node);
            this._up(this.heap.length - 1);
        }
        pop() {
            if (!this.heap.length) return null;
            const top = this.heap[0];
            const end = this.heap.pop();
            if (this.heap.length) {
                this.heap[0] = end;
                this._down(0);
            }
            return top;
        }
        size() { return this.heap.length; }
        _up(idx) {
            while (idx > 0) {
                const parent = (idx - 1) >> 1;
                if (this.heap[parent][0] <= this.heap[idx][0]) break;
                [this.heap[parent], this.heap[idx]] = [this.heap[idx], this.heap[parent]];
                idx = parent;
            }
        }
        _down(idx) {
            const len = this.heap.length;
            while (true) {
                let left = idx * 2 + 1,
                    right = left + 1,
                    smallest = idx;
                if (left < len && this.heap[left][0] < this.heap[smallest][0]) smallest = left;
                if (right < len && this.heap[right][0] < this.heap[smallest][0]) smallest = right;
                if (smallest === idx) break;
                [this.heap[idx], this.heap[smallest]] = [this.heap[smallest], this.heap[idx]];
                idx = smallest;
            }
        }
    }

    const heap = new MinHeap();
    const visited = new Set();

    heap.push([nums1[0] + nums2[0], 0, 0]);
    visited.add('0,0');

    const result = [];
    while (result.length < k && heap.size() > 0) {
        const [_, i, j] = heap.pop();
        result.push([nums1[i], nums2[j]]);

        if (i + 1 < m) {
            const key = `${i + 1},${j}`;
            if (!visited.has(key)) {
                visited.add(key);
                heap.push([nums1[i + 1] + nums2[j], i + 1, j]);
            }
        }
        if (j + 1 < n) {
            const key = `${i},${j + 1}`;
            if (!visited.has(key)) {
                visited.add(key);
                heap.push([nums1[i] + nums2[j + 1], i, j + 1]);
            }
        }
    }

    return result;
};
```

## Typescript

```typescript
function kSmallestPairs(nums1: number[], nums2: number[], k: number): number[][] {
    const m = nums1.length;
    const n = nums2.length;
    if (m === 0 || n === 0 || k === 0) return [];

    interface Node {
        sum: number;
        i: number;
        j: number;
    }

    class MinHeap {
        private data: Node[] = [];
        push(node: Node): void {
            this.data.push(node);
            this.bubbleUp(this.data.length - 1);
        }
        pop(): Node | undefined {
            if (this.data.length === 0) return undefined;
            const top = this.data[0];
            const end = this.data.pop()!;
            if (this.data.length > 0) {
                this.data[0] = end;
                this.sinkDown(0);
            }
            return top;
        }
        size(): number {
            return this.data.length;
        }
        private bubbleUp(idx: number): void {
            const element = this.data[idx];
            while (idx > 0) {
                const parentIdx = Math.floor((idx - 1) / 2);
                const parent = this.data[parentIdx];
                if (element.sum >= parent.sum) break;
                this.data[parentIdx] = element;
                this.data[idx] = parent;
                idx = parentIdx;
            }
        }
        private sinkDown(idx: number): void {
            const length = this.data.length;
            const element = this.data[idx];
            while (true) {
                let leftIdx = 2 * idx + 1;
                let rightIdx = 2 * idx + 2;
                let swapIdx: number | null = null;

                if (leftIdx < length) {
                    if (this.data[leftIdx].sum < element.sum) {
                        swapIdx = leftIdx;
                    }
                }

                if (rightIdx < length) {
                    if (
                        (swapIdx === null && this.data[rightIdx].sum < element.sum) ||
                        (swapIdx !== null && this.data[rightIdx].sum < this.data[leftIdx].sum)
                    ) {
                        swapIdx = rightIdx;
                    }
                }

                if (swapIdx === null) break;

                this.data[idx] = this.data[swapIdx];
                this.data[swapIdx] = element;
                idx = swapIdx;
            }
        }
    }

    const heap = new MinHeap();
    const visited = new Set<string>();
    heap.push({ sum: nums1[0] + nums2[0], i: 0, j: 0 });
    visited.add('0,0');

    const result: number[][] = [];

    while (result.length < k && heap.size() > 0) {
        const node = heap.pop()!;
        const i = node.i;
        const j = node.j;
        result.push([nums1[i], nums2[j]]);

        if (i + 1 < m) {
            const key = `${i + 1},${j}`;
            if (!visited.has(key)) {
                visited.add(key);
                heap.push({ sum: nums1[i + 1] + nums2[j], i: i + 1, j });
            }
        }

        if (j + 1 < n) {
            const key = `${i},${j + 1}`;
            if (!visited.has(key)) {
                visited.add(key);
                heap.push({ sum: nums1[i] + nums2[j + 1], i, j: j + 1 });
            }
        }
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @param Integer $k
     * @return Integer[][]
     */
    function kSmallestPairs($nums1, $nums2, $k) {
        $m = count($nums1);
        $n = count($nums2);
        if ($m == 0 || $n == 0 || $k == 0) {
            return [];
        }

        $heap = new SplPriorityQueue();
        // we want to extract the data (indices) only
        $heap->setExtractFlags(SplPriorityQueue::EXTR_DATA);

        $visited = [];

        // push first pair (0,0)
        $sum = $nums1[0] + $nums2[0];
        $heap->insert([0, 0], -$sum);   // negative sum to simulate min-heap
        $visited["0,0"] = true;

        $result = [];

        while (!$heap->isEmpty() && count($result) < $k) {
            [$i, $j] = $heap->extract();
            $result[] = [$nums1[$i], $nums2[$j]];

            // next pair with i+1
            if ($i + 1 < $m) {
                $key = ($i + 1) . ',' . $j;
                if (!isset($visited[$key])) {
                    $newSum = $nums1[$i + 1] + $nums2[$j];
                    $heap->insert([$i + 1, $j], -$newSum);
                    $visited[$key] = true;
                }
            }

            // next pair with j+1
            if ($j + 1 < $n) {
                $key = $i . ',' . ($j + 1);
                if (!isset($visited[$key])) {
                    $newSum = $nums1[$i] + $nums2[$j + 1];
                    $heap->insert([$i, $j + 1], -$newSum);
                    $visited[$key] = true;
                }
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func kSmallestPairs(_ nums1: [Int], _ nums2: [Int], _ k: Int) -> [[Int]] {
        guard !nums1.isEmpty, !nums2.isEmpty, k > 0 else { return [] }
        var heap = [(sum: Int, i: Int, j: Int)]()
        var visited = Set<Int64>()
        
        func encode(_ i: Int, _ j: Int) -> Int64 {
            return (Int64(i) << 32) | Int64(j)
        }
        
        func heapPush(_ node: (sum: Int, i: Int, j: Int)) {
            heap.append(node)
            var idx = heap.count - 1
            while idx > 0 {
                let parent = (idx - 1) >> 1
                if heap[parent].sum <= heap[idx].sum { break }
                heap.swapAt(parent, idx)
                idx = parent
            }
        }
        
        func heapPop() -> (sum: Int, i: Int, j: Int)? {
            guard !heap.isEmpty else { return nil }
            let top = heap[0]
            let last = heap.removeLast()
            if !heap.isEmpty {
                heap[0] = last
                var idx = 0
                while true {
                    let left = idx * 2 + 1
                    let right = left + 1
                    var smallest = idx
                    if left < heap.count && heap[left].sum < heap[smallest].sum {
                        smallest = left
                    }
                    if right < heap.count && heap[right].sum < heap[smallest].sum {
                        smallest = right
                    }
                    if smallest == idx { break }
                    heap.swapAt(idx, smallest)
                    idx = smallest
                }
            }
            return top
        }
        
        heapPush((nums1[0] + nums2[0], 0, 0))
        visited.insert(encode(0, 0))
        
        var result: [[Int]] = []
        while result.count < k, let node = heapPop() {
            let i = node.i
            let j = node.j
            result.append([nums1[i], nums2[j]])
            
            if i + 1 < nums1.count {
                let code = encode(i + 1, j)
                if !visited.contains(code) {
                    heapPush((nums1[i + 1] + nums2[j], i + 1, j))
                    visited.insert(code)
                }
            }
            if j + 1 < nums2.count {
                let code = encode(i, j + 1)
                if !visited.contains(code) {
                    heapPush((nums1[i] + nums2[j + 1], i, j + 1))
                    visited.insert(code)
                }
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun kSmallestPairs(nums1: IntArray, nums2: IntArray, k: Int): List<List<Int>> {
        if (nums1.isEmpty() || nums2.isEmpty() || k == 0) return emptyList()
        val m = nums1.size
        val n = nums2.size

        data class Node(val sum: Long, val i: Int, val j: Int)

        val pq = java.util.PriorityQueue<Node>(compareBy { it.sum })
        val visited = HashSet<Long>()
        fun encode(i: Int, j: Int): Long = i.toLong() * n + j

        pq.add(Node(nums1[0].toLong() + nums2[0], 0, 0))
        visited.add(encode(0, 0))

        val result = mutableListOf<List<Int>>()
        while (result.size < k && pq.isNotEmpty()) {
            val cur = pq.poll()
            val i = cur.i
            val j = cur.j
            result.add(listOf(nums1[i], nums2[j]))

            if (i + 1 < m) {
                val code = encode(i + 1, j)
                if (visited.add(code)) {
                    pq.add(Node(nums1[i + 1].toLong() + nums2[j], i + 1, j))
                }
            }
            if (j + 1 < n) {
                val code = encode(i, j + 1)
                if (visited.add(code)) {
                    pq.add(Node(nums1[i].toLong() + nums2[j + 1], i, j + 1))
                }
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> kSmallestPairs(List<int> nums1, List<int> nums2, int k) {
    if (nums1.isEmpty || nums2.isEmpty || k == 0) return [];

    final int m = nums1.length;
    final int n = nums2.length;

    // Min-heap implementation
    final _MinHeap heap = _MinHeap();
    final Set<int> visited = {};

    // Encode pair (i, j) as i * n + j
    int encode(int i, int j) => i * n + j;

    heap.push(_Node(nums1[0] + nums2[0], 0, 0));
    visited.add(encode(0, 0));

    final List<List<int>> result = [];

    while (result.length < k && !heap.isEmpty) {
      final _Node cur = heap.pop()!;
      result.add([nums1[cur.i], nums2[cur.j]]);

      if (cur.i + 1 < m) {
        int key = encode(cur.i + 1, cur.j);
        if (!visited.contains(key)) {
          visited.add(key);
          heap.push(_Node(nums1[cur.i + 1] + nums2[cur.j], cur.i + 1, cur.j));
        }
      }

      if (cur.j + 1 < n) {
        int key = encode(cur.i, cur.j + 1);
        if (!visited.contains(key)) {
          visited.add(key);
          heap.push(_Node(nums1[cur.i] + nums2[cur.j + 1], cur.i, cur.j + 1));
        }
      }
    }

    return result;
  }
}

class _Node {
  final int sum;
  final int i;
  final int j;
  _Node(this.sum, this.i, this.j);
}

class _MinHeap {
  final List<_Node> _data = [];

  bool get isEmpty => _data.isEmpty;

  void push(_Node node) {
    _data.add(node);
    _siftUp(_data.length - 1);
  }

  _Node? pop() {
    if (_data.isEmpty) return null;
    final root = _data[0];
    final last = _data.removeLast();
    if (_data.isNotEmpty) {
      _data[0] = last;
      _siftDown(0);
    }
    return root;
  }

  void _siftUp(int idx) {
    while (idx > 0) {
      int parent = (idx - 1) >> 1;
      if (_compare(_data[idx], _data[parent]) < 0) {
        _swap(idx, parent);
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
      int smallest = idx;

      if (left < n && _compare(_data[left], _data[smallest]) < 0) {
        smallest = left;
      }
      if (right < n && _compare(_data[right], _data[smallest]) < 0) {
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

  int _compare(_Node a, _Node b) {
    if (a.sum != b.sum) return a.sum - b.sum;
    if (a.i != b.i) return a.i - b.i;
    return a.j - b.j;
  }

  void _swap(int i, int j) {
    final tmp = _data[i];
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
)

type pairItem struct {
	sum int
	i   int
	j   int
}

type minHeap []pairItem

func (h minHeap) Len() int { return len(h) }
func (h minHeap) Less(a, b int) bool {
	return h[a].sum < h[b].sum
}
func (h minHeap) Swap(a, b int) { h[a], h[b] = h[b], h[a] }

func (h *minHeap) Push(x interface{}) {
	*h = append(*h, x.(pairItem))
}

func (h *minHeap) Pop() interface{} {
	old := *h
	n := len(old)
	it := old[n-1]
	*h = old[:n-1]
	return it
}

func kSmallestPairs(nums1 []int, nums2 []int, k int) [][]int {
	if len(nums1) == 0 || len(nums2) == 0 || k == 0 {
		return [][]int{}
	}
	h := &minHeap{}
	heap.Init(h)

	limit := len(nums1)
	if limit > k {
		limit = k
	}
	for i := 0; i < limit; i++ {
		heap.Push(h, pairItem{sum: nums1[i] + nums2[0], i: i, j: 0})
	}

	res := make([][]int, 0, k)
	for len(res) < k && h.Len() > 0 {
		it := heap.Pop(h).(pairItem)
		res = append(res, []int{nums1[it.i], nums2[it.j]})
		if it.j+1 < len(nums2) {
			heap.Push(h, pairItem{sum: nums1[it.i] + nums2[it.j+1], i: it.i, j: it.j + 1})
		}
	}
	return res
}
```

## Ruby

```ruby
require 'set'

def heap_push(heap, item)
  heap << item
  idx = heap.size - 1
  while idx > 0
    parent = (idx - 1) / 2
    break if heap[parent][0] <= heap[idx][0]
    heap[parent], heap[idx] = heap[idx], heap[parent]
    idx = parent
  end
end

def heap_pop(heap)
  top = heap[0]
  last = heap.pop
  unless heap.empty?
    heap[0] = last
    size = heap.size
    idx = 0
    loop do
      left = idx * 2 + 1
      right = left + 1
      smallest = idx
      smallest = left if left < size && heap[left][0] < heap[smallest][0]
      smallest = right if right < size && heap[right][0] < heap[smallest][0]
      break if smallest == idx
      heap[idx], heap[smallest] = heap[smallest], heap[idx]
      idx = smallest
    end
  end
  top
end

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer} k
# @return {Integer[][]}
def k_smallest_pairs(nums1, nums2, k)
  return [] if nums1.empty? || nums2.empty? || k <= 0

  m = nums1.size
  n = nums2.size
  heap = []
  visited = Set.new

  heap_push(heap, [nums1[0] + nums2[0], 0, 0])
  visited.add([0, 0])

  result = []

  while result.size < k && !heap.empty?
    _, i, j = heap_pop(heap)
    result << [nums1[i], nums2[j]]

    if i + 1 < m && !visited.include?([i + 1, j])
      heap_push(heap, [nums1[i + 1] + nums2[j], i + 1, j])
      visited.add([i + 1, j])
    end

    if j + 1 < n && !visited.include?([i, j + 1])
      heap_push(heap, [nums1[i] + nums2[j + 1], i, j + 1])
      visited.add([i, j + 1])
    end
  end

  result
end
```

## Scala

```scala
object Solution {
  import java.util.PriorityQueue
  import scala.collection.mutable.{HashSet, ListBuffer}

  case class Node(i: Int, j: Int, sum: Long)

  def kSmallestPairs(nums1: Array[Int], nums2: Array[Int], k: Int): List[List[Int]] = {
    if (nums1.isEmpty || nums2.isEmpty || k == 0) return Nil

    val m = nums1.length
    val n = nums2.length

    val cmp = new java.util.Comparator[Node] {
      override def compare(a: Node, b: Node): Int =
        java.lang.Long.compare(a.sum, b.sum)
    }
    val pq = new PriorityQueue[Node](cmp)

    val visited = HashSet[(Int, Int)]()
    pq.offer(Node(0, 0, nums1(0).toLong + nums2(0)))
    visited.add((0, 0))

    val res = ListBuffer[List[Int]]()

    while (res.size < k && !pq.isEmpty) {
      val cur = pq.poll()
      res += List(nums1(cur.i), nums2(cur.j))

      if (cur.i + 1 < m && !visited.contains((cur.i + 1, cur.j))) {
        visited.add((cur.i + 1, cur.j))
        pq.offer(Node(cur.i + 1, cur.j, nums1(cur.i + 1).toLong + nums2(cur.j)))
      }
      if (cur.j + 1 < n && !visited.contains((cur.i, cur.j + 1))) {
        visited.add((cur.i, cur.j + 1))
        pq.offer(Node(cur.i, cur.j + 1, nums1(cur.i).toLong + nums2(cur.j + 1)))
      }
    }

    res.toList
  }
}
```

## Rust

```rust
use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashSet};

impl Solution {
    pub fn k_smallest_pairs(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> Vec<Vec<i32>> {
        let m = nums1.len();
        let n = nums2.len();
        if m == 0 || n == 0 || k == 0 {
            return Vec::new();
        }

        let mut heap: BinaryHeap<Reverse<(i64, usize, usize)>> = BinaryHeap::new();
        let mut visited: HashSet<(usize, usize)> = HashSet::new();

        // start with (0,0)
        heap.push(Reverse((nums1[0] as i64 + nums2[0] as i64, 0usize, 0usize)));
        visited.insert((0usize, 0usize));

        let mut result: Vec<Vec<i32>> = Vec::new();
        let limit = k as usize;

        while result.len() < limit {
            if let Some(Reverse((_sum, i, j))) = heap.pop() {
                result.push(vec![nums1[i], nums2[j]]);

                // push (i+1, j)
                if i + 1 < m && !visited.contains(&(i + 1, j)) {
                    heap.push(Reverse((
                        nums1[i + 1] as i64 + nums2[j] as i64,
                        i + 1,
                        j,
                    )));
                    visited.insert((i + 1, j));
                }
                // push (i, j+1)
                if j + 1 < n && !visited.contains(&(i, j + 1)) {
                    heap.push(Reverse((
                        nums1[i] as i64 + nums2[j + 1] as i64,
                        i,
                        j + 1,
                    )));
                    visited.insert((i, j + 1));
                }
            } else {
                break;
            }
        }

        result
    }
}
```

## Racket

```racket
#lang racket
(require data/heap)

(define/contract (k-smallest-pairs nums1 nums2 k)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? (listof (listof exact-integer?)))
  (let* ((m (length nums1))
         (n (length nums2))
         (result '())
         (cnt 0)
         (visited (make-hash))
         (heap (make-heap (lambda (a b) (< (first a) (first b))))))
    (when (and (> m 0) (> n 0) (> k 0))
      (define sum0 (+ (list-ref nums1 0) (list-ref nums2 0)))
      (heap-push! heap (list sum0 0 0))
      (hash-set! visited (cons 0 0) #t))
    (let loop ()
      (when (and (< cnt k) (not (heap-empty? heap)))
        (define top (heap-pop! heap))
        (define i (list-ref top 1))
        (define j (list-ref top 2))
        (set! result (cons (list (list-ref nums1 i) (list-ref nums2 j)) result))
        (set! cnt (+ cnt 1))
        ;; push (i+1, j)
        (when (< (+ i 1) m)
          (define key (cons (+ i 1) j))
          (unless (hash-has-key? visited key)
            (define sum (+ (list-ref nums1 (+ i 1)) (list-ref nums2 j)))
            (heap-push! heap (list sum (+ i 1) j))
            (hash-set! visited key #t)))
        ;; push (i, j+1)
        (when (< (+ j 1) n)
          (define key (cons i (+ j 1)))
          (unless (hash-has-key? visited key)
            (define sum (+ (list-ref nums1 i) (list-ref nums2 (+ j 1))))
            (heap-push! heap (list sum i (+ j 1)))
            (hash-set! visited key #t)))
        (loop)))
    (reverse result)))
```

## Erlang

```erlang
-spec k_smallest_pairs(Nums1 :: [integer()], Nums2 :: [integer()], K :: integer()) -> [[integer()]].
k_smallest_pairs(Nums1, Nums2, K) ->
    Num1Arr = array:from_list(Nums1),
    Num2Arr = array:from_list(Nums2),
    M = length(Nums1),
    N = length(Nums2),
    Limit = erlang:min(K, M),
    Tree0 = init_heap(Limit, Num1Arr, Num2Arr, gb_trees:empty()),
    collect_pairs(Tree0, Num1Arr, Num2Arr, K, [], N).

%% Initialize heap with pairs (i,0) for i = 0 .. Limit-1
-spec init_heap(integer(), array:array(integer()), array:array(integer()), gb_trees:tree()) -> gb_trees:tree().
init_heap(0, _Num1Arr, _Num2Arr, Tree) ->
    Tree;
init_heap(Cnt, Num1Arr, Num2Arr, Tree) ->
    I = Cnt - 1,
    Sum = array:get(I, Num1Arr) + array:get(0, Num2Arr),
    NewTree = gb_trees:insert({Sum, I, 0}, {I, 0}, Tree),
    init_heap(Cnt - 1, Num1Arr, Num2Arr, NewTree).

%% Collect up to K smallest pairs
-spec collect_pairs(gb_trees:tree(), array:array(integer()), array:array(integer()), integer(), [[integer()]], integer()) -> [[integer()]].
collect_pairs(_Tree, _Num1Arr, _Num2Arr, 0, Acc, _N) ->
    lists:reverse(Acc);
collect_pairs(Tree, Num1Arr, Num2Arr, K, Acc, N) when K > 0 ->
    case gb_trees:is_empty(Tree) of
        true ->
            lists:reverse(Acc);
        false ->
            {{_Sum, I, J}, {I, J}} = gb_trees:smallest(Tree),
            Tree1 = gb_trees:delete_min(Tree),
            Pair = [array:get(I, Num1Arr), array:get(J, Num2Arr)],
            NewTree =
                if
                    J + 1 < N ->
                        NewSum = array:get(I, Num1Arr) + array:get(J + 1, Num2Arr),
                        gb_trees:insert({NewSum, I, J + 1}, {I, J + 1}, Tree1);
                    true ->
                        Tree1
                end,
            collect_pairs(NewTree, Num1Arr, Num2Arr, K - 1, [Pair | Acc], N)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec k_smallest_pairs(nums1 :: [integer], nums2 :: [integer], k :: integer) :: [[integer]]
  def k_smallest_pairs(nums1, nums2, k) do
    m = length(nums1)
    n = length(nums2)

    limit_i = min(k, m)

    arr1 = :array.from_list(nums1)
    arr2 = :array.from_list(nums2)

    initial_tree =
      Enum.reduce(0..limit_i - 1, :gb_trees.empty(), fn i, tree ->
        sum = :array.get(i, arr1) + :array.get(0, arr2)
        insert_pair(tree, sum, {i, 0})
      end)

    collect(initial_tree, arr1, arr2, n, k, [])
  end

  defp collect(_, _, _, _, 0, acc), do: Enum.reverse(acc)

  defp collect(tree, arr1, arr2, n, remaining, acc) do
    if :gb_trees.is_empty(tree) do
      Enum.reverse(acc)
    else
      {{sum, list}, tree1} = :gb_trees.take_smallest(tree)
      [{i, j} | rest] = list

      new_acc = [[:array.get(i, arr1), :array.get(j, arr2)] | acc]

      tree2 =
        if rest == [] do
          tree1
        else
          :gb_trees.insert(sum, rest, tree1)
        end

      tree3 =
        if j + 1 < n do
          new_sum = :array.get(i, arr1) + :array.get(j + 1, arr2)
          insert_pair(tree2, new_sum, {i, j + 1})
        else
          tree2
        end

      collect(tree3, arr1, arr2, n, remaining - 1, new_acc)
    end
  end

  defp insert_pair(tree, sum, pair) do
    case :gb_trees.lookup(sum, tree) do
      {:value, list} -> :gb_trees.update(sum, [pair | list], tree)
      :none -> :gb_trees.insert(sum, [pair], tree)
    end
  end
end
```
