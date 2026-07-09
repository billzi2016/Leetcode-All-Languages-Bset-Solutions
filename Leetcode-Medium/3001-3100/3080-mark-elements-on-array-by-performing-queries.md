# 3080. Mark Elements on Array by Performing Queries

## Cpp

```cpp
class Solution {
public:
    vector<long long> unmarkedSumArray(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        long long total = 0;
        for (int v : nums) total += v;
        vector<char> marked(n, false);
        using P = pair<int,int>;
        priority_queue<P, vector<P>, greater<P>> pq;
        for (int i = 0; i < n; ++i) {
            pq.emplace(nums[i], i);
        }
        vector<long long> ans;
        for (auto& q : queries) {
            int idx = q[0];
            int k = q[1];
            if (!marked[idx]) {
                marked[idx] = true;
                total -= nums[idx];
            }
            for (int cnt = 0; cnt < k; ++cnt) {
                while (!pq.empty() && marked[pq.top().second]) pq.pop();
                if (pq.empty()) break;
                auto [val, id] = pq.top(); pq.pop();
                marked[id] = true;
                total -= val;
            }
            ans.push_back(total);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    private static class Node {
        int val;
        int idx;
        Node(int v, int i) { val = v; idx = i; }
    }

    public long[] unmarkedSumArray(int[] nums, int[][] queries) {
        int n = nums.length;
        boolean[] marked = new boolean[n];
        java.util.PriorityQueue<Node> pq = new java.util.PriorityQueue<>(
            (a, b) -> a.val != b.val ? Integer.compare(a.val, b.val) : Integer.compare(a.idx, b.idx)
        );
        long sum = 0L;
        for (int i = 0; i < n; ++i) {
            sum += nums[i];
            pq.offer(new Node(nums[i], i));
        }

        int m = queries.length;
        long[] ans = new long[m];

        for (int q = 0; q < m; ++q) {
            int index = queries[q][0];
            int k = queries[q][1];

            if (!marked[index]) {
                marked[index] = true;
                sum -= nums[index];
            }

            for (int cnt = 0; cnt < k; ++cnt) {
                while (!pq.isEmpty() && marked[pq.peek().idx]) {
                    pq.poll();
                }
                if (pq.isEmpty()) break;
                Node node = pq.poll();
                marked[node.idx] = true;
                sum -= node.val;
            }

            ans[q] = sum;
        }

        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def unmarkedSumArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        import heapq
        n = len(nums)
        marked = [False] * n
        total = sum(nums)
        heap = [(nums[i], i) for i in range(n)]
        heapq.heapify(heap)

        ans = []
        for idx, k in queries:
            if not marked[idx]:
                marked[idx] = True
                total -= nums[idx]
            cnt = 0
            while cnt < k and heap:
                val, i = heap[0]
                if marked[i]:
                    heapq.heappop(heap)
                    continue
                heapq.heappop(heap)
                marked[i] = True
                total -= val
                cnt += 1
            ans.append(total)
        return ans
```

## Python3

```python
import heapq
from typing import List

class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        total = sum(nums)
        marked = [False] * n
        heap = [(nums[i], i) for i in range(n)]
        heapq.heapify(heap)

        ans = []
        for idx, k in queries:
            if not marked[idx]:
                marked[idx] = True
                total -= nums[idx]
            cnt = 0
            while cnt < k and heap:
                val, i = heap[0]
                if marked[i]:
                    heapq.heappop(heap)
                    continue
                heapq.heappop(heap)
                marked[i] = True
                total -= val
                cnt += 1
            ans.append(total)
        return ans
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int val;
    int idx;
} Node;

static void heapifyDown(Node *heap, int size, int i) {
    while (1) {
        int left = 2 * i + 1;
        int right = left + 1;
        int smallest = i;
        if (left < size && (heap[left].val < heap[smallest].val ||
            (heap[left].val == heap[smallest].val && heap[left].idx < heap[smallest].idx))) {
            smallest = left;
        }
        if (right < size && (heap[right].val < heap[smallest].val ||
            (heap[right].val == heap[smallest].val && heap[right].idx < heap[smallest].idx))) {
            smallest = right;
        }
        if (smallest != i) {
            Node tmp = heap[i];
            heap[i] = heap[smallest];
            heap[smallest] = tmp;
            i = smallest;
        } else {
            break;
        }
    }
}

static Node heapPop(Node *heap, int *size) {
    Node top = heap[0];
    heap[0] = heap[*size - 1];
    (*size)--;
    if (*size > 0) heapifyDown(heap, *size, 0);
    return top;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* unmarkedSumArray(int* nums, int numsSize, int** queries, int queriesSize,
                            int* queriesColSize, int* returnSize) {
    *returnSize = queriesSize;
    long long *ans = (long long *)malloc(sizeof(long long) * queriesSize);
    bool *marked = (bool *)calloc(numsSize, sizeof(bool));

    long long total = 0;
    for (int i = 0; i < numsSize; ++i) total += nums[i];

    Node *heap = (Node *)malloc(sizeof(Node) * numsSize);
    int heapSize = numsSize;
    for (int i = 0; i < numsSize; ++i) {
        heap[i].val = nums[i];
        heap[i].idx = i;
    }
    for (int i = heapSize / 2 - 1; i >= 0; --i)
        heapifyDown(heap, heapSize, i);

    for (int q = 0; q < queriesSize; ++q) {
        int index = queries[q][0];
        int k = queries[q][1];

        if (!marked[index]) {
            marked[index] = true;
            total -= nums[index];
        }

        while (k > 0 && heapSize > 0) {
            Node top = heap[0];
            if (marked[top.idx]) {
                heapPop(heap, &heapSize);
                continue;
            }
            marked[top.idx] = true;
            total -= top.val;
            heapPop(heap, &heapSize);
            --k;
        }

        ans[q] = total;
    }

    free(marked);
    free(heap);
    return ans;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public long[] UnmarkedSumArray(int[] nums, int[][] queries) {
        int n = nums.Length;
        bool[] marked = new bool[n];
        var pq = new PriorityQueue<int, long>();
        for (int i = 0; i < n; i++) {
            long priority = ((long)nums[i] << 32) | (uint)i; // value first, then index
            pq.Enqueue(i, priority);
        }

        long sum = 0;
        foreach (var v in nums) sum += v;

        int m = queries.Length;
        long[] ans = new long[m];

        for (int q = 0; q < m; q++) {
            int idx = queries[q][0];
            int k = queries[q][1];

            if (!marked[idx]) {
                marked[idx] = true;
                sum -= nums[idx];
            }

            int cnt = 0;
            while (cnt < k && pq.Count > 0) {
                int cur = pq.Dequeue();
                if (marked[cur]) continue;
                marked[cur] = true;
                sum -= nums[cur];
                cnt++;
            }

            ans[q] = sum;
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {number[]}
 */
var unmarkedSumArray = function(nums, queries) {
    const n = nums.length;
    // Min-heap implementation
    class MinHeap {
        constructor() {
            this.heap = [];
        }
        size() {
            return this.heap.length;
        }
        peek() {
            return this.heap[0];
        }
        push(node) {
            const h = this.heap;
            h.push(node);
            let i = h.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (h[p].value <= h[i].value) break;
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
                    let l = i * 2 + 1;
                    let r = i * 2 + 2;
                    let smallest = i;
                    if (l < h.length && h[l].value < h[smallest].value) smallest = l;
                    if (r < h.length && h[r].value < h[smallest].value) smallest = r;
                    if (smallest === i) break;
                    [h[i], h[smallest]] = [h[smallest], h[i]];
                    i = smallest;
                }
            }
            return top;
        }
    }

    const heap = new MinHeap();
    for (let i = 0; i < n; ++i) {
        heap.push({value: nums[i], index: i});
    }

    const marked = new Array(n).fill(false);
    let sum = 0;
    for (const v of nums) sum += v;

    const ans = [];

    for (const [idx, k] of queries) {
        // mark the given index if not already
        if (!marked[idx]) {
            marked[idx] = true;
            sum -= nums[idx];
        }

        let need = k;
        while (need > 0) {
            // discard already marked elements at heap top
            while (heap.size() && marked[heap.peek().index]) {
                heap.pop();
            }
            if (!heap.size()) break;
            const node = heap.pop(); // smallest unmarked
            marked[node.index] = true;
            sum -= node.value;
            need--;
        }

        ans.push(sum);
    }

    return ans;
};
```

## Typescript

```typescript
function unmarkedSumArray(nums: number[], queries: number[][]): number[] {
    const n = nums.length;
    let maxVal = 0;
    for (const v of nums) if (v > maxVal) maxVal = v;

    class BIT {
        n: number;
        tree: number[];
        constructor(n: number) {
            this.n = n;
            this.tree = new Array(n + 2).fill(0);
        }
        add(i: number, delta: number): void {
            for (let x = i; x <= this.n; x += x & -x) this.tree[x] += delta;
        }
        sum(i: number): number {
            let res = 0;
            for (let x = i; x > 0; x -= x & -x) res += this.tree[x];
            return res;
        }
        // smallest index such that prefix sum >= target (target >=1)
        lowerBound(target: number): number {
            let idx = 0;
            let bitMask = 1 << (Math.floor(Math.log2(this.n)) + 1);
            for (let k = bitMask; k !== 0; k >>= 1) {
                const next = idx + k;
                if (next <= this.n && this.tree[next] < target) {
                    idx = next;
                    target -= this.tree[next];
                }
            }
            return idx + 1;
        }
    }

    const bit = new BIT(maxVal + 2);
    const freq: number[] = new Array(maxVal + 2).fill(0);
    let totalSum = 0;
    for (const v of nums) {
        freq[v]++;
        bit.add(v, 1);
        totalSum += v;
    }

    const marked = new Array(n).fill(false);
    const ans: number[] = [];

    for (const [idx, kRaw] of queries) {
        let k = kRaw;
        if (!marked[idx]) {
            const val = nums[idx];
            // count of unmarked elements with value < val
            const cntLess = bit.sum(val - 1);
            // remove the indexed element
            marked[idx] = true;
            freq[val]--;
            bit.add(val, -1);
            totalSum -= val;

            const extra = cntLess < k ? k - 1 : k;
            let need = extra;
            while (need > 0 && bit.sum(maxVal) > 0) {
                const v = bit.lowerBound(1);
                const avail = freq[v];
                const take = Math.min(avail, need);
                freq[v] -= take;
                bit.add(v, -take);
                totalSum -= v * take;
                need -= take;
            }
        } else {
            // index already marked: just remove k smallest unmarked elements
            let need = k;
            while (need > 0 && bit.sum(maxVal) > 0) {
                const v = bit.lowerBound(1);
                const avail = freq[v];
                const take = Math.min(avail, need);
                freq[v] -= take;
                bit.add(v, -take);
                totalSum -= v * take;
                need -= take;
            }
        }
        ans.push(totalSum);
    }

    return ans;
}
```

## Php

```php
class MinHeap extends SplHeap {
    protected function compare($a, $b) {
        // a and b are arrays [value, index]
        if ($a[0] === $b[0]) {
            return 0;
        }
        // smaller value should be extracted first
        return ($a[0] < $b[0]) ? 1 : -1;
    }
}

class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function unmarkedSumArray($nums, $queries) {
        $n = count($nums);
        $total = array_sum($nums);
        $marked = array_fill(0, $n, false);

        $heap = new MinHeap();
        for ($i = 0; $i < $n; $i++) {
            $heap->insert([$nums[$i], $i]);
        }

        $ans = [];
        foreach ($queries as $q) {
            [$idx, $k] = $q;
            if (!$marked[$idx]) {
                $total -= $nums[$idx];
                $marked[$idx] = true;
            }
            while (!$heap->isEmpty()) {
                $top = $heap->top(); // peek
                if ($top[0] <= $k) {
                    $heap->extract();
                    $pos = $top[1];
                    if (!$marked[$pos]) {
                        $total -= $nums[$pos];
                        $marked[$pos] = true;
                    }
                } else {
                    break;
                }
            }
            $ans[] = $total;
        }

        return $ans;
    }
}
```

## Swift

```swift
class MinHeap {
    private var heap: [(Int, Int)] = [] // (value, index)
    
    private func less(_ a: (Int, Int), _ b: (Int, Int)) -> Bool {
        if a.0 != b.0 { return a.0 < b.0 }
        return a.1 < b.1
    }
    
    var isEmpty: Bool { heap.isEmpty }
    var peek: (Int, Int)? { heap.first }
    
    func push(_ element: (Int, Int)) {
        heap.append(element)
        siftUp(heap.count - 1)
    }
    
    func pop() -> (Int, Int)? {
        guard !heap.isEmpty else { return nil }
        if heap.count == 1 {
            return heap.removeLast()
        }
        let top = heap[0]
        heap[0] = heap.removeLast()
        siftDown(0)
        return top
    }
    
    private func siftUp(_ index: Int) {
        var child = index
        while child > 0 {
            let parent = (child - 1) >> 1
            if less(heap[child], heap[parent]) {
                heap.swapAt(child, parent)
                child = parent
            } else { break }
        }
    }
    
    private func siftDown(_ index: Int) {
        var parent = index
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
}

class Solution {
    func unmarkedSumArray(_ nums: [Int], _ queries: [[Int]]) -> [Int] {
        let n = nums.count
        var marked = Array(repeating: false, count: n)
        var total = 0
        for v in nums { total += v }
        
        var heap = MinHeap()
        for i in 0..<n {
            heap.push((nums[i], i))
        }
        
        var answer: [Int] = []
        for q in queries {
            let idx = q[0]
            var k = q[1]
            
            if !marked[idx] {
                marked[idx] = true
                total -= nums[idx]
            }
            
            while k > 0 {
                // discard already marked elements at heap top
                while let top = heap.peek, marked[top.1] {
                    _ = heap.pop()
                }
                guard let node = heap.pop() else { break }
                if !marked[node.1] {
                    marked[node.1] = true
                    total -= node.0
                    k -= 1
                }
            }
            
            answer.append(total)
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun unmarkedSumArray(nums: IntArray, queries: Array<IntArray>): LongArray {
        val n = nums.size
        var sum = 0L
        for (v in nums) sum += v.toLong()
        val marked = BooleanArray(n)
        val pq = java.util.PriorityQueue<Pair<Int, Int>>(compareBy<Pair<Int, Int>> { it.first }.thenBy { it.second })
        for (i in 0 until n) {
            pq.add(Pair(nums[i], i))
        }
        val ans = LongArray(queries.size)
        var idx = 0
        for (q in queries) {
            val index = q[0]
            var k = q[1]
            while (k > 0 && pq.isNotEmpty()) {
                val (value, i) = pq.poll()
                if (marked[i]) continue
                marked[i] = true
                sum -= value.toLong()
                k--
            }
            if (!marked[index]) {
                marked[index] = true
                sum -= nums[index].toLong()
            }
            ans[idx++] = sum
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> unmarkedSumArray(List<int> nums, List<List<int>> queries) {
    int n = nums.length;
    List<bool> marked = List.filled(n, false);
    int sum = 0;
    for (int v in nums) sum += v;

    MinHeap heap = MinHeap();
    for (int i = 0; i < n; ++i) {
      heap.push(_Node(nums[i], i));
    }

    List<int> ans = [];

    for (var q in queries) {
      int idx = q[0];
      int k = q[1];

      if (!marked[idx]) {
        sum -= nums[idx];
        marked[idx] = true;
      }

      for (int cnt = 0; cnt < k; ++cnt) {
        while (!heap.isEmpty && marked[heap.peek().idx]) {
          heap.pop();
        }
        if (heap.isEmpty) break;
        _Node node = heap.pop();
        if (!marked[node.idx]) {
          sum -= node.val;
          marked[node.idx] = true;
        }
      }

      ans.add(sum);
    }

    return ans;
  }
}

class _Node {
  int val;
  int idx;
  _Node(this.val, this.idx);
}

class MinHeap {
  final List<_Node> _data = [];

  bool get isEmpty => _data.isEmpty;

  _Node peek() => _data[0];

  void push(_Node node) {
    _data.add(node);
    _siftUp(_data.length - 1);
  }

  _Node pop() {
    var root = _data[0];
    var last = _data.removeLast();
    if (_data.isNotEmpty) {
      _data[0] = last;
      _siftDown(0);
    }
    return root;
  }

  void _siftUp(int i) {
    while (i > 0) {
      int p = (i - 1) >> 1;
      if (_compare(_data[i], _data[p]) < 0) {
        var tmp = _data[i];
        _data[i] = _data[p];
        _data[p] = tmp;
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
      int r = l + 1;
      int smallest = i;
      if (l < n && _compare(_data[l], _data[smallest]) < 0) smallest = l;
      if (r < n && _compare(_data[r], _data[smallest]) < 0) smallest = r;
      if (smallest == i) break;
      var tmp = _data[i];
      _data[i] = _data[smallest];
      _data[smallest] = tmp;
      i = smallest;
    }
  }

  int _compare(_Node a, _Node b) {
    if (a.val != b.val) return a.val - b.val;
    return a.idx - b.idx;
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
	val int
	idx int
}
type minHeap []item

func (h minHeap) Len() int            { return len(h) }
func (h minHeap) Less(i, j int) bool  { return h[i].val < h[j].val }
func (h minHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *minHeap) Push(x interface{}) { *h = append(*h, x.(item)) }
func (h *minHeap) Pop() interface{} {
	old := *h
	n := len(old)
	it := old[n-1]
	*h = old[:n-1]
	return it
}

func unmarkedSumArray(nums []int, queries [][]int) []int64 {
	n := len(nums)
	marked := make([]bool, n)

	h := &minHeap{}
	for i, v := range nums {
		heap.Push(h, item{val: v, idx: i})
	}
	heap.Init(h)

	var total int64
	for _, v := range nums {
		total += int64(v)
	}

	ans := make([]int64, len(queries))

	for qi, q := range queries {
		idx := q[0]
		k := q[1]

		if !marked[idx] {
			marked[idx] = true
			total -= int64(nums[idx])
		}
		for i := 0; i < k; i++ {
			// find next unmarked smallest element
			for h.Len() > 0 && marked[(*h)[0].idx] {
				heap.Pop(h)
			}
			if h.Len() == 0 {
				break
			}
			it := heap.Pop(h).(item)
			marked[it.idx] = true
			total -= int64(it.val)
		}
		ans[qi] = total
	}
	return ans
}
```

## Ruby

```ruby
def unmarked_sum_array(nums, queries)
  n = nums.length
  marked = Array.new(n, false)
  total_unmarked = nums.sum

  heap = []
  nums.each_with_index { |val, i| heap << [val, i] }
  (heap.size / 2 - 1).downto(0) { |i| sift_down(heap, i) }

  result = []

  queries.each do |idx, k|
    unless marked[idx]
      marked[idx] = true
      total_unmarked -= nums[idx]
    end

    cnt = 0
    while cnt < k && !heap.empty?
      val, i = heap[0]
      if marked[i]
        heap_pop(heap)
        next
      else
        heap_pop(heap)
        marked[i] = true
        total_unmarked -= val
        cnt += 1
      end
    end

    result << total_unmarked
  end

  result
end

def sift_down(arr, i)
  n = arr.length
  loop do
    l = i * 2 + 1
    r = i * 2 + 2
    smallest = i
    if l < n && (arr[l][0] < arr[smallest][0] || (arr[l][0] == arr[smallest][0] && arr[l][1] < arr[smallest][1]))
      smallest = l
    end
    if r < n && (arr[r][0] < arr[smallest][0] || (arr[r][0] == arr[smallest][0] && arr[r][1] < arr[smallest][1]))
      smallest = r
    end
    break if smallest == i
    arr[i], arr[smallest] = arr[smallest], arr[i]
    i = smallest
  end
end

def heap_pop(arr)
  min = arr[0]
  last = arr.pop
  unless arr.empty?
    arr[0] = last
    sift_down(arr, 0)
  end
  min
end
```

## Scala

```scala
object Solution {
    import scala.collection.mutable

    def unmarkedSumArray(nums: Array[Int], queries: Array[Array[Int]]): Array[Long] = {
        val n = nums.length
        val marked = new Array[Boolean](n)
        var totalSum: Long = 0L
        val countMap = mutable.TreeMap.empty[Int, Int]

        for (v <- nums) {
            totalSum += v.toLong
            countMap.update(v, countMap.getOrElse(v, 0) + 1)
        }

        val ans = new Array[Long](queries.length)

        var qIdx = 0
        while (qIdx < queries.length) {
            val idx = queries(qIdx)(0)
            var k = queries(qIdx)(1)

            if (!marked(idx)) {
                marked(idx) = true
                val v = nums(idx)
                totalSum -= v.toLong
                val cnt = countMap(v)
                if (cnt == 1) countMap.remove(v)
                else countMap.update(v, cnt - 1)
            }

            var remainingK = k
            while (remainingK > 0 && countMap.nonEmpty) {
                val (value, cnt) = countMap.head
                if (cnt <= remainingK) {
                    totalSum -= value.toLong * cnt
                    remainingK -= cnt
                    countMap.remove(value)
                } else {
                    totalSum -= value.toLong * remainingK
                    countMap.update(value, cnt - remainingK)
                    remainingK = 0
                }
            }

            ans(qIdx) = totalSum
            qIdx += 1
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
    pub fn unmarked_sum_array(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i64> {
        let n = nums.len();
        let mut marked = vec![false; n];
        let mut sum: i64 = nums.iter().map(|&x| x as i64).sum();

        // min-heap of (value, index)
        let mut heap: BinaryHeap<Reverse<(i32, usize)>> = BinaryHeap::with_capacity(n);
        for (i, &v) in nums.iter().enumerate() {
            heap.push(Reverse((v, i)));
        }

        let mut ans = Vec::with_capacity(queries.len());

        for q in queries.iter() {
            let idx = q[0] as usize;
            let mut k = q[1] as usize;

            // mark the specified index if not already
            if !marked[idx] {
                marked[idx] = true;
                sum -= nums[idx] as i64;
            }

            while k > 0 {
                // discard already marked elements at heap top
                while let Some(&Reverse((_, id))) = heap.peek() {
                    if marked[id] {
                        heap.pop();
                    } else {
                        break;
                    }
                }
                match heap.pop() {
                    Some(Reverse((val, id))) => {
                        marked[id] = true;
                        sum -= val as i64;
                        k -= 1;
                    }
                    None => break,
                }
            }

            ans.push(sum);
        }

        ans
    }
}
```

## Racket

```racket
(require racket/heap)

(define/contract (unmarked-sum-array nums queries)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ([n (length nums)]
         [nums-vec (list->vector nums)]
         [marked (make-vector n #f)]
         [total-sum (apply + nums)]
         [h (make-heap
              (lambda (a b) (< (first a) (first b))))])
    ;; initialize heap with all elements
    (for ([i (in-range n)])
      (heap-add! h (list (vector-ref nums-vec i) i)))
    (let loop ((qs queries) (answers '()))
      (if (null? qs)
          (reverse answers)
          (begin
            (define q (car qs))
            (define idx (first q))
            (define k (second q))
            ;; mark the given index if not already marked
            (unless (vector-ref marked idx)
              (set! total-sum (- total-sum (vector-ref nums-vec idx)))
              (vector-set! marked idx #t))
            ;; mark k smallest unmarked elements
            (let recur ((remaining k))
              (when (and (> remaining 0) (not (heap-empty? h)))
                (define pair (heap-peek h))
                (define val (first pair))
                (define i (second pair))
                (if (vector-ref marked i)
                    (begin
                      (heap-remove-min! h)
                      (recur remaining))
                    (begin
                      (heap-remove-min! h)
                      (set! total-sum (- total-sum val))
                      (vector-set! marked i #t)
                      (recur (- remaining 1)))))))
            (loop (cdr qs) (cons total-sum answers)))))))
```

## Erlang

```erlang
-spec unmarked_sum_array(Nums :: [integer()], Queries :: [[integer()]]) -> [integer()].
unmarked_sum_array(Nums, Queries) ->
    NumTuple = list_to_tuple(Nums),
    Sum0 = lists:sum(Nums),
    Set0 = build_set(Nums, 0, gb_sets:new()),
    process_queries(Queries, Set0, #{}, Sum0, [], NumTuple).

build_set([], _Idx, Set) -> Set;
build_set([V|Rest], Idx, Set) ->
    NewSet = gb_sets:add({V, Idx}, Set),
    build_set(Rest, Idx + 1, NewSet).

process_queries([], _Set, _Map, _Sum, Acc, _NumTuple) ->
    lists:reverse(Acc);
process_queries([[Idx, K] | Rest], Set, Map, Sum, Acc, NumTuple) ->
    %% mark the element at given index if not already marked
    case maps:is_key(Idx, Map) of
        true ->
            Set1 = Set,
            Map1 = Map,
            Sum1 = Sum;
        false ->
            Val = element(Idx + 1, NumTuple),
            Set1 = Set,
            Map1 = maps:put(Idx, true, Map),
            Sum1 = Sum - Val
    end,
    {Set2, Map2, Sum2} = mark_k_smallest(K, Set1, Map1, Sum1),
    process_queries(Rest, Set2, Map2, Sum2, [Sum2 | Acc], NumTuple).

mark_k_smallest(0, Set, Map, Sum) ->
    {Set, Map, Sum};
mark_k_smallest(K, Set, Map, Sum) when K > 0 ->
    case gb_sets:is_empty(Set) of
        true ->
            {Set, Map, Sum};
        false ->
            Small = gb_sets:smallest(Set),
            Set1 = gb_sets:delete(Small, Set),
            {Val, Idx} = Small,
            case maps:is_key(Idx, Map) of
                true ->
                    %% already marked, do not consume K
                    mark_k_smallest(K, Set1, Map, Sum);
                false ->
                    NewMap = maps:put(Idx, true, Map),
                    NewSum = Sum - Val,
                    mark_k_smallest(K - 1, Set1, NewMap, NewSum)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec unmarked_sum_array(nums :: [integer], queries :: [[integer]]) :: [integer]
  def unmarked_sum_array(nums, queries) do
    n = length(nums)
    total_initial = Enum.sum(nums)

    nums_tuple = List.to_tuple(nums)

    indexed = Enum.with_index(nums) |> Enum.map(fn {v, i} -> {v, i} end)
    sorted_list = Enum.sort_by(indexed, fn {v, _i} -> v end)
    sorted_tuple = List.to_tuple(sorted_list)

    {results_rev, _ptr, _marked, _total} =
      Enum.reduce(queries, {[], 0, MapSet.new(), total_initial}, fn [idx, k],
                                                                   {res, ptr, marked, total} ->
        {marked1, total1} =
          if MapSet.member?(marked, idx) do
            {marked, total}
          else
            {MapSet.put(marked, idx), total - elem(nums_tuple, idx)}
          end

        {ptr2, marked2, total2} = mark_k_smallest(k, ptr, sorted_tuple, n, marked1, total1)

        {[total2 | res], ptr2, marked2, total2}
      end)

    Enum.reverse(results_rev)
  end

  defp mark_k_smallest(0, ptr, _sorted, _n, marked, total), do: {ptr, marked, total}

  defp mark_k_smallest(k, ptr, sorted, n, marked, total) when k > 0 do
    if ptr >= n do
      {ptr, marked, total}
    else
      {val, idx} = elem(sorted, ptr)

      if MapSet.member?(marked, idx) do
        mark_k_smallest(k, ptr + 1, sorted, n, marked, total)
      else
        new_marked = MapSet.put(marked, idx)
        new_total = total - val
        mark_k_smallest(k - 1, ptr + 1, sorted, n, new_marked, new_total)
      end
    end
  end
end
```
