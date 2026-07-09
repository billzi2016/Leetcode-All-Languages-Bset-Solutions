# 3478. Choose K Elements With Maximum Sum

## Cpp

```cpp
class Solution {
public:
    vector<long long> findMaxSum(vector<int>& nums1, vector<int>& nums2, int k) {
        int n = nums1.size();
        vector<int> idx(n);
        iota(idx.begin(), idx.end(), 0);
        sort(idx.begin(), idx.end(), [&](int a, int b){
            return nums1[a] < nums1[b];
        });
        
        vector<long long> ans(n, 0);
        priority_queue<int, vector<int>, greater<int>> minHeap;
        long long curSum = 0;
        
        int i = 0;
        while (i < n) {
            int start = i;
            int val = nums1[idx[i]];
            // all indices with the same nums1 value get current sum
            while (i < n && nums1[idx[i]] == val) {
                ans[idx[i]] = curSum;
                ++i;
            }
            // now insert their nums2 values into the heap for future groups
            for (int j = start; j < i; ++j) {
                int v = nums2[idx[j]];
                if ((int)minHeap.size() < k) {
                    minHeap.push(v);
                    curSum += v;
                } else if (k > 0 && v > minHeap.top()) {
                    curSum -= minHeap.top();
                    minHeap.pop();
                    minHeap.push(v);
                    curSum += v;
                }
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
    public long[] findMaxSum(int[] nums1, int[] nums2, int k) {
        int n = nums1.length;
        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        Arrays.sort(idx, Comparator.comparingInt(i -> nums1[i]));

        long[] ans = new long[n];
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        long sum = 0L;

        int i = 0;
        while (i < n) {
            int curVal = nums1[idx[i]];
            int j = i;
            // find range with same nums1 value
            while (j < n && nums1[idx[j]] == curVal) j++;

            // compute answers for this group using current heap state
            for (int t = i; t < j; t++) {
                ans[idx[t]] = sum;
            }

            // add this group's nums2 values to the heap
            for (int t = i; t < j; t++) {
                int val = nums2[idx[t]];
                minHeap.offer(val);
                sum += val;
                if (minHeap.size() > k) {
                    sum -= minHeap.poll();
                }
            }

            i = j;
        }

        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def findMaxSum(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        import heapq
        n = len(nums1)
        items = [(nums1[i], nums2[i], i) for i in range(n)]
        items.sort(key=lambda x: x[0])
        ans = [0] * n
        minheap = []
        cur_sum = 0
        i = 0
        while i < n:
            j = i
            # find group with same nums1 value
            while j < n and items[j][0] == items[i][0]:
                j += 1
            # set answers for this group based on previous smaller elements
            for t in range(i, j):
                idx = items[t][2]
                ans[idx] = cur_sum
            # add current group's nums2 into heap
            for t in range(i, j):
                val = items[t][1]
                if len(minheap) < k:
                    heapq.heappush(minheap, val)
                    cur_sum += val
                else:
                    if k > 0 and val > minheap[0]:
                        cur_sum -= heapq.heapreplace(minheap, val)
                        cur_sum += val
            i = j
        return ans
```

## Python3

```python
import heapq
from typing import List

class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n = len(nums1)
        order = sorted(range(n), key=lambda i: nums1[i])
        ans = [0] * n
        heap = []
        cur_sum = 0

        i = 0
        while i < n:
            j = i
            # group with same nums1 value
            while j < n and nums1[order[j]] == nums1[order[i]]:
                j += 1
            # set answers for this group using current heap state
            for t in range(i, j):
                idx = order[t]
                ans[idx] = cur_sum
            # add this group's nums2 values to the heap
            for t in range(i, j):
                val = nums2[order[t]]
                if len(heap) < k:
                    heapq.heappush(heap, val)
                    cur_sum += val
                else:
                    if k > 0 and val > heap[0]:
                        cur_sum += val - heap[0]
                        heapq.heapreplace(heap, val)
            i = j

        return ans
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdlib.h>

typedef struct {
    int a;
    int b;
    int idx;
} Item;

static int cmpItem(const void *p1, const void *p2) {
    const Item *x = (const Item *)p1;
    const Item *y = (const Item *)p2;
    if (x->a < y->a) return -1;
    if (x->a > y->a) return 1;
    return 0;
}

/* min-heap functions for integers */
static void heapSwap(int *h, int i, int j) {
    int tmp = h[i];
    h[i] = h[j];
    h[j] = tmp;
}

static void siftUp(int *h, int idx) {
    while (idx > 0) {
        int parent = (idx - 1) >> 1;
        if (h[parent] <= h[idx]) break;
        heapSwap(h, parent, idx);
        idx = parent;
    }
}

static void siftDown(int *h, int idx, int size) {
    while (1) {
        int left = (idx << 1) + 1;
        int right = left + 1;
        int smallest = idx;
        if (left < size && h[left] < h[smallest]) smallest = left;
        if (right < size && h[right] < h[smallest]) smallest = right;
        if (smallest == idx) break;
        heapSwap(h, idx, smallest);
        idx = smallest;
    }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* findMaxSum(int* nums1, int nums1Size, int* nums2, int nums2Size,
                      int k, int* returnSize) {
    int n = nums1Size;
    Item *items = (Item *)malloc(n * sizeof(Item));
    for (int i = 0; i < n; ++i) {
        items[i].a = nums1[i];
        items[i].b = nums2[i];
        items[i].idx = i;
    }
    qsort(items, n, sizeof(Item), cmpItem);

    long long *ans = (long long *)malloc(n * sizeof(long long));
    int *heap = (int *)malloc(k * sizeof(int));  // min-heap of size at most k
    int heapSize = 0;
    long long sum = 0;

    for (int i = 0; i < n; ++i) {
        ans[items[i].idx] = sum;   // current best sum from smaller a's

        int val = items[i].b;
        if (heapSize < k) {
            heap[heapSize] = val;
            siftUp(heap, heapSize);
            sum += val;
            ++heapSize;
        } else if (k > 0 && val > heap[0]) {
            sum -= heap[0];
            heap[0] = val;
            sum += val;
            siftDown(heap, 0, heapSize);
        }
    }

    free(items);
    free(heap);
    *returnSize = n;
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public long[] FindMaxSum(int[] nums1, int[] nums2, int k) {
        int n = nums1.Length;
        var pairs = new (int num1, int num2, int idx)[n];
        for (int i = 0; i < n; i++) {
            pairs[i] = (nums1[i], nums2[i], i);
        }
        Array.Sort(pairs, (a, b) => a.num1.CompareTo(b.num1));

        long[] answer = new long[n];
        var minHeap = new PriorityQueue<int, int>(); // stores nums2 values with min-heap order
        long sum = 0;

        int i = 0;
        while (i < n) {
            int j = i;
            while (j < n && pairs[j].num1 == pairs[i].num1) j++;

            // Compute answers for current batch using the heap built from strictly smaller nums1
            for (int t = i; t < j; ++t) {
                answer[pairs[t].idx] = sum;
            }

            // Insert current batch's nums2 into the heap
            for (int t = i; t < j; ++t) {
                int val = pairs[t].num2;
                if (minHeap.Count < k) {
                    minHeap.Enqueue(val, val);
                    sum += val;
                } else if (k > 0 && val > minHeap.Peek()) {
                    int removed = minHeap.Dequeue();
                    sum -= removed;
                    minHeap.Enqueue(val, val);
                    sum += val;
                }
            }

            i = j;
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} k
 * @return {number[]}
 */
var findMaxSum = function(nums1, nums2, k) {
    const n = nums1.length;
    const items = new Array(n);
    for (let i = 0; i < n; ++i) {
        items[i] = {val: nums1[i], idx: i, w: nums2[i]};
    }
    items.sort((a, b) => a.val - b.val);

    class MinHeap {
        constructor() {
            this.heap = [];
        }
        size() {
            return this.heap.length;
        }
        push(val) {
            const h = this.heap;
            h.push(val);
            let i = h.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (h[p] <= h[i]) break;
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
                    if (l < h.length && h[l] < h[smallest]) smallest = l;
                    if (r < h.length && h[r] < h[smallest]) smallest = r;
                    if (smallest === i) break;
                    [h[i], h[smallest]] = [h[smallest], h[i]];
                    i = smallest;
                }
            }
            return top;
        }
    }

    const heap = new MinHeap();
    let sum = 0;
    const ans = new Array(n).fill(0);

    for (let i = 0; i < n;) {
        let j = i;
        while (j < n && items[j].val === items[i].val) j++;

        // compute answers for current group using previous heap state
        for (let t = i; t < j; ++t) {
            ans[items[t].idx] = sum;
        }

        // insert current group's nums2 values into heap
        for (let t = i; t < j; ++t) {
            const w = items[t].w;
            heap.push(w);
            sum += w;
            if (heap.size() > k) {
                sum -= heap.pop(); // remove smallest to keep largest k
            }
        }

        i = j;
    }

    return ans;
};
```

## Typescript

```typescript
function findMaxSum(nums1: number[], nums2: number[], k: number): number[] {
    const n = nums1.length;
    const items = new Array(n);
    for (let i = 0; i < n; i++) {
        items[i] = { v1: nums1[i], v2: nums2[i], idx: i };
    }
    items.sort((a, b) => a.v1 - b.v1);

    class MinHeap {
        private data: number[] = [];
        size(): number { return this.data.length; }
        peek(): number { return this.data[0]; }
        push(val: number): void {
            const a = this.data;
            a.push(val);
            let i = a.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (a[p] <= a[i]) break;
                [a[p], a[i]] = [a[i], a[p]];
                i = p;
            }
        }
        pop(): number {
            const a = this.data;
            const root = a[0];
            const last = a.pop()!;
            if (a.length > 0) {
                a[0] = last;
                let i = 0;
                while (true) {
                    let l = i * 2 + 1,
                        r = l + 1,
                        smallest = i;
                    if (l < a.length && a[l] < a[smallest]) smallest = l;
                    if (r < a.length && a[r] < a[smallest]) smallest = r;
                    if (smallest === i) break;
                    [a[i], a[smallest]] = [a[smallest], a[i]];
                    i = smallest;
                }
            }
            return root;
        }
    }

    const heap = new MinHeap();
    let sum = 0;
    const ans: number[] = new Array(n).fill(0);

    for (let i = 0; i < n;) {
        let j = i;
        while (j < n && items[j].v1 === items[i].v1) j++;

        // compute answers for this group
        for (let t = i; t < j; t++) {
            ans[items[t].idx] = sum;
        }

        // add current group's nums2 to heap
        for (let t = i; t < j; t++) {
            const val = items[t].v2;
            if (heap.size() < k) {
                heap.push(val);
                sum += val;
            } else if (k > 0 && val > heap.peek()) {
                sum -= heap.pop();
                heap.push(val);
                sum += val;
            }
        }

        i = j;
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @param Integer $k
     * @return Integer[]
     */
    function findMaxSum($nums1, $nums2, $k) {
        $n = count($nums1);
        $indices = range(0, $n - 1);
        usort($indices, function ($a, $b) use ($nums1) {
            if ($nums1[$a] == $nums1[$b]) return 0;
            return ($nums1[$a] < $nums1[$b]) ? -1 : 1;
        });

        $ans = array_fill(0, $n, 0);
        $heap = new SplMinHeap(); // stores the current top k nums2 values
        $sum = 0;

        $i = 0;
        while ($i < $n) {
            $currentVal = $nums1[$indices[$i]];
            $j = $i;
            // compute answers for all indices with this nums1 value
            while ($j < $n && $nums1[$indices[$j]] == $currentVal) {
                $idx = $indices[$j];
                $ans[$idx] = $sum; // sum of up to k largest nums2 from smaller nums1
                $j++;
            }
            // add their nums2 values into the structure for future indices
            for ($p = $i; $p < $j; $p++) {
                $idx = $indices[$p];
                $heap->insert($nums2[$idx]);
                $sum += $nums2[$idx];
                if ($heap->count() > $k) {
                    $removed = $heap->extract(); // remove smallest among the top k
                    $sum -= $removed;
                }
            }
            $i = $j;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    struct Heap<T> {
        var elements: [T] = []
        let priorityFunction: (T, T) -> Bool
        
        init(sort: @escaping (T, T) -> Bool) {
            self.priorityFunction = sort
        }
        
        var isEmpty: Bool { elements.isEmpty }
        var count: Int { elements.count }
        func peek() -> T? { elements.first }
        
        mutating func insert(_ value: T) {
            elements.append(value)
            siftUp(from: elements.count - 1)
        }
        
        mutating func remove() -> T {
            let value = elements[0]
            if elements.count == 1 {
                elements.removeLast()
            } else {
                elements[0] = elements.removeLast()
                siftDown(from: 0)
            }
            return value
        }
        
        private mutating func siftUp(from index: Int) {
            var child = index
            var parent = (child - 1) / 2
            while child > 0 && priorityFunction(elements[child], elements[parent]) {
                elements.swapAt(child, parent)
                child = parent
                parent = (child - 1) / 2
            }
        }
        
        private mutating func siftDown(from index: Int) {
            var parent = index
            while true {
                let left = parent * 2 + 1
                let right = left + 1
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
    
    func findMaxSum(_ nums1: [Int], _ nums2: [Int], _ k: Int) -> [Int] {
        let n = nums1.count
        var combined: [(v1: Int, v2: Int, idx: Int)] = []
        combined.reserveCapacity(n)
        for i in 0..<n {
            combined.append((nums1[i], nums2[i], i))
        }
        combined.sort { $0.v1 < $1.v1 }
        
        var answer = Array(repeating: 0, count: n)
        var minHeap = Heap<Int>(sort: <)   // keeps the current top k largest values
        var sumTopK: Int64 = 0
        
        var i = 0
        while i < n {
            var j = i
            while j < n && combined[j].v1 == combined[i].v1 { j += 1 }
            
            // compute answers for this group using current heap (values from smaller nums1)
            for t in i..<j {
                answer[combined[t].idx] = Int(sumTopK)
            }
            
            // add this group's nums2 values into the structure
            for t in i..<j {
                let val = combined[t].v2
                if minHeap.count < k {
                    minHeap.insert(val)
                    sumTopK += Int64(val)
                } else if k > 0 && val > (minHeap.peek() ?? Int.max) {
                    let removed = minHeap.remove()
                    sumTopK -= Int64(removed)
                    minHeap.insert(val)
                    sumTopK += Int64(val)
                }
            }
            
            i = j
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findMaxSum(nums1: IntArray, nums2: IntArray, k: Int): LongArray {
        val n = nums1.size
        data class Node(val a: Int, val b: Int, val idx: Int)
        val nodes = Array(n) { i -> Node(nums1[i], nums2[i], i) }
        nodes.sortWith(compareBy<Node> { it.a })
        val heap = java.util.PriorityQueue<Int>() // min-heap for top k values
        var sum = 0L
        val ans = LongArray(n)
        var i = 0
        while (i < n) {
            var j = i
            while (j < n && nodes[j].a == nodes[i].a) j++
            // compute answers for this group using current heap state
            for (t in i until j) {
                ans[nodes[t].idx] = sum
            }
            // add this group's nums2 values into the heap
            for (t in i until j) {
                val v = nodes[t].b
                if (heap.size < k) {
                    heap.add(v)
                    sum += v.toLong()
                } else if (k > 0 && v > heap.peek()) {
                    val removed = heap.poll()
                    sum -= removed.toLong()
                    heap.add(v)
                    sum += v.toLong()
                }
            }
            i = j
        }
        return ans
    }
}
```

## Dart

```dart
class MinHeap {
  final List<int> _data = [];

  int get size => _data.length;

  int top() => _data[0];

  void push(int x) {
    _data.add(x);
    _siftUp(_data.length - 1);
  }

  int pop() {
    int res = _data[0];
    int last = _data.removeLast();
    if (_data.isNotEmpty) {
      _data[0] = last;
      _siftDown(0);
    }
    return res;
  }

  void _siftUp(int idx) {
    while (idx > 0) {
      int parent = (idx - 1) >> 1;
      if (_data[parent] <= _data[idx]) break;
      int tmp = _data[parent];
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
      if (left < n && _data[left] < _data[smallest]) smallest = left;
      if (right < n && _data[right] < _data[smallest]) smallest = right;
      if (smallest == idx) break;
      int tmp = _data[idx];
      _data[idx] = _data[smallest];
      _data[smallest] = tmp;
      idx = smallest;
    }
  }
}

class Solution {
  List<int> findMaxSum(List<int> nums1, List<int> nums2, int k) {
    int n = nums1.length;
    var items = <List<int>>[];
    for (int i = 0; i < n; ++i) {
      items.add([nums1[i], nums2[i], i]);
    }
    items.sort((a, b) => a[0].compareTo(b[0]));

    List<int> ans = List.filled(n, 0);
    MinHeap heap = MinHeap();
    int sum = 0;

    int i = 0;
    while (i < n) {
      int j = i;
      while (j < n && items[j][0] == items[i][0]) ++j;

      // compute answers for this group
      for (int t = i; t < j; ++t) {
        ans[items[t][2]] = sum;
      }

      // add current group's nums2 to the heap
      for (int t = i; t < j; ++t) {
        int val = items[t][1];
        if (heap.size < k) {
          heap.push(val);
          sum += val;
        } else if (val > heap.top()) {
          sum -= heap.pop();
          heap.push(val);
          sum += val;
        }
      }

      i = j;
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

type pair struct {
	val1 int
	val2 int
	idx  int
}

// MinHeap for nums2 values
type IntMinHeap []int

func (h IntMinHeap) Len() int           { return len(h) }
func (h IntMinHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntMinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntMinHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *IntMinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func findMaxSum(nums1 []int, nums2 []int, k int) []int64 {
	n := len(nums1)
	pairs := make([]pair, n)
	for i := 0; i < n; i++ {
		pairs[i] = pair{val1: nums1[i], val2: nums2[i], idx: i}
	}
	// sort by val1 ascending
	sort.Slice(pairs, func(i, j int) bool {
		if pairs[i].val1 == pairs[j].val1 {
			return pairs[i].idx < pairs[j].idx
		}
		return pairs[i].val1 < pairs[j].val1
	})

	ans := make([]int64, n)
	h := &IntMinHeap{}
	heap.Init(h)
	var sum int64 = 0

	i := 0
	for i < n {
		j := i
		// find range with same val1
		for j < n && pairs[j].val1 == pairs[i].val1 {
			j++
		}
		// compute answers for this group using current heap (elements with smaller val1)
		for t := i; t < j; t++ {
			ans[pairs[t].idx] = sum
		}
		// now add this group's nums2 into heap
		for t := i; t < j; t++ {
			heap.Push(h, pairs[t].val2)
			sum += int64(pairs[t].val2)
			if h.Len() > k {
				minVal := heap.Pop(h).(int)
				sum -= int64(minVal)
			}
		}
		i = j
	}
	return ans
}

// needed import for sort
import "sort"
```

## Ruby

```ruby
def heap_push(heap, val)
  heap << val
  idx = heap.size - 1
  while idx > 0
    parent = (idx - 1) / 2
    break if heap[parent] <= heap[idx]
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
      break if left >= size
      smallest = left
      smallest = right if right < size && heap[right] < heap[left]
      break if heap[idx] <= heap[smallest]
      heap[idx], heap[smallest] = heap[smallest], heap[idx]
      idx = smallest
    end
  end
  top
end

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer} k
# @return {Integer[]}
def find_max_sum(nums1, nums2, k)
  n = nums1.length
  idxs = (0...n).to_a.sort_by { |i| [nums1[i], i] }
  ans = Array.new(n, 0)

  selected = []          # min-heap of current top k nums2 values
  sum_selected = 0

  i = 0
  while i < n
    j = i
    while j < n && nums1[idxs[j]] == nums1[idxs[i]]
      j += 1
    end

    # compute answers for this group (strictly smaller values only)
    (i...j).each do |p|
      idx = idxs[p]
      ans[idx] = sum_selected
    end

    # insert current group's nums2 into the structure
    (i...j).each do |p|
      v = nums2[idxs[p]]
      if selected.size < k
        heap_push(selected, v)
        sum_selected += v
      elsif k > 0 && v > selected[0]
        removed = heap_pop(selected)
        sum_selected -= removed
        heap_push(selected, v)
        sum_selected += v
      end
    end

    i = j
  end

  ans
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable.PriorityQueue

  def findMaxSum(nums1: Array[Int], nums2: Array[Int], k: Int): Array[Long] = {
    val n = nums1.length
    // tuple: (value of nums1, value of nums2, original index)
    val sorted = (0 until n).map(i => (nums1(i), nums2(i), i)).toArray.sortBy(_._1)

    val answer = new Array[Long](n)
    // min-heap to keep the k largest nums2 values seen so far
    implicit val ord: Ordering[Int] = Ordering[Int].reverse // smallest on top
    val heap = PriorityQueue.empty[Int]
    var curSum: Long = 0L

    var pos = 0
    while (pos < n) {
      val currentVal = sorted(pos)._1
      var end = pos
      while (end < n && sorted(end)._1 == currentVal) end += 1

      // compute answers for this group using only previous groups
      var i = pos
      while (i < end) {
        if (heap.size >= k) answer(sorted(i)._3) = curSum else answer(sorted(i)._3) = 0L
        i += 1
      }

      // add current group's nums2 values into the heap
      i = pos
      while (i < end) {
        val v = sorted(i)._2
        heap.enqueue(v)
        curSum += v
        if (heap.size > k) {
          val removed = heap.dequeue()
          curSum -= removed
        }
        i += 1
      }

      pos = end
    }

    answer
  }
}
```

## Rust

```rust
impl Solution {
    pub fn find_max_sum(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> Vec<i64> {
        use std::cmp::Reverse;
        use std::collections::BinaryHeap;

        let n = nums1.len();
        let mut order: Vec<usize> = (0..n).collect();
        order.sort_by_key(|&i| nums1[i]);

        let mut heap: BinaryHeap<Reverse<i32>> = BinaryHeap::new(); // min-heap via Reverse
        let mut sum: i64 = 0;
        let mut ans = vec![0i64; n];
        let k_usize = k as usize;

        for &idx in order.iter() {
            ans[idx] = sum;
            let val = nums2[idx];
            if heap.len() < k_usize {
                heap.push(Reverse(val));
                sum += val as i64;
            } else if k_usize > 0 {
                if let Some(&Reverse(smallest)) = heap.peek() {
                    if val > smallest {
                        heap.pop();
                        sum -= smallest as i64;
                        heap.push(Reverse(val));
                        sum += val as i64;
                    }
                }
            }
        }

        ans
    }
}
```

## Racket

```racket
(require data/heap)

(define/contract (find-max-sum nums1 nums2 k)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let* ((n (length nums1))
         (pairs (for/list ([i (in-range n)])
                  (list (list-ref nums1 i) (list-ref nums2 i) i)))
         (sorted (sort pairs (lambda (a b) (< (first a) (first b)))))
         (heap (make-heap <)) ; min‑heap for the k largest nums2 values
         (sum 0)
         (ans (make-vector n 0)))
    (let loop ((i 0))
      (when (< i n)
        (define cur-val (first (list-ref sorted i)))
        ;; find end of group with same nums1 value
        (define j i)
        (let inner ()
          (when (and (< j n) (= (first (list-ref sorted j)) cur-val))
            (set! j (+ j 1))
            (inner)))
        ;; set answer for each index in the group using current sum
        (for ([idx (in-range i j)])
          (define orig-idx (third (list-ref sorted idx)))
          (vector-set! ans orig-idx sum))
        ;; insert this group's nums2 values into heap
        (for ([idx (in-range i j)])
          (define val (second (list-ref sorted idx)))
          (heap-insert! heap val)
          (set! sum (+ sum val))
          (when (> (heap-size heap) k)
            (define smallest (heap-pop! heap))
            (set! sum (- sum smallest))))
        (loop j)))
    (vector->list ans)))
```

## Erlang

```erlang
-module(solution).
-export([find_max_sum/3]).

-spec find_max_sum(Nums1 :: [integer()], Nums2 :: [integer()], K :: integer()) -> [integer()].
find_max_sum(Nums1, Nums2, K) ->
    % Build list of {Num1, Num2, Index}
    Indexed = build_indexed(lists:zip3(Nums1, Nums2, lists:seq(0, length(Nums1) - 1))),
    % Sort by Num1 ascending
    Sorted = lists:keysort(1, Indexed),
    % Process groups
    AnswersMap = process(Sorted, K, gb_trees:empty(), 0, 0, 0, #{}),
    % Assemble result in original order
    N = length(Nums1),
    [maps:get(I, AnswersMap) || I <- lists:seq(0, N - 1)].

build_indexed([]) -> [];
build_indexed([{N1, N2, Id} | Rest]) ->
    [{N1, N2, Id} | build_indexed(Rest)].

process([], _K, _Tree, _Size, _Sum, _Id, AnswersMap) ->
    AnswersMap;
process([{Num1, _, _}=First | Rest], K, Tree, Size, Sum, Id, AnswersMap) ->
    {Group, Remaining} = take_same(Num1, [First | Rest]),
    % Record answers for current group
    AnswersMap1 = lists:foldl(fun({_N1, _N2, Index}, Acc) ->
        maps:put(Index, Sum, Acc)
    end, AnswersMap, Group),
    % Insert group's Num2 values into the heap
    {Tree2, Size2, Sum2, Id2} = insert_group(Group, K, Tree, Size, Sum, Id),
    process(Remaining, K, Tree2, Size2, Sum2, Id2, AnswersMap1).

take_same(_Num1, []) -> {[], []};
take_same(Num1, [{N1, N2, I} = Elem | Rest]) when N1 =:= Num1 ->
    {GroupTail, Remaining} = take_same(Num1, Rest),
    {[Elem | GroupTail], Remaining};
take_same(_Num1, List) -> {[], List}.

insert_group([], _K, Tree, Size, Sum, Id) ->
    {Tree, Size, Sum, Id};
insert_group([{_N1, N2, _Idx} = Elem | Rest], K, Tree, Size, Sum, Id) ->
    Key = {N2, Id},
    Tree1 = gb_trees:insert(Key, true, Tree),
    Size1 = Size + 1,
    Sum1 = Sum + N2,
    {Tree2, Size2, Sum2} =
        if
            Size1 > K ->
                {SmallKey, _} = gb_trees:smallest(Tree1),
                {SmallN2, _} = SmallKey,
                TreeTmp = gb_trees:delete(SmallKey, Tree1),
                {TreeTmp, Size1 - 1, Sum1 - SmallN2};
            true ->
                {Tree1, Size1, Sum1}
        end,
    insert_group(Rest, K, Tree2, Size2, Sum2, Id + 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_max_sum(nums1 :: [integer], nums2 :: [integer], k :: integer) :: [integer]
  def find_max_sum(nums1, nums2, k) do
    n = length(nums1)

    sorted =
      Enum.with_index(nums1)
      |> Enum.map(fn {v1, idx} -> {v1, Enum.at(nums2, idx), idx} end)
      |> Enum.sort_by(fn {v1, _, _} -> v1 end)

    ans_array = :array.new(n, default: 0)

    final_ans =
      process(sorted, k, :gb_trees.empty(), 0, 0, ans_array)

    Enum.map(0..n - 1, fn i -> :array.get(i, final_ans) end)
  end

  defp process([], _k, _heap, _size, _sum, ans), do: ans

  defp process([head | tail] = list, k, heap, size, sum, ans) do
    {group, rest} = split_group(list, elem(head, 0), [])

    # set answers for current group using the current sum
    ans =
      Enum.reduce(group, ans, fn {_v1, _v2, idx}, acc ->
        :array.set(idx, sum, acc)
      end)

    # insert each element's nums2 into the heap maintaining top k largest values
    {heap, size, sum} =
      Enum.reduce(group, {heap, size, sum}, fn {_v1, val2, _idx}, {h, sz, s} ->
        cond do
          sz < k ->
            {insert_val(h, val2), sz + 1, s + val2}

          true ->
            {min_key, _cnt} = :gb_trees.smallest(h)

            if val2 > min_key do
              h = delete_one(h, min_key)
              s = s - min_key
              sz = sz - 1
              {insert_val(h, val2), sz + 1, s + val2}
            else
              {h, sz, s}
            end
        end
      end)

    process(rest, k, heap, size, sum, ans)
  end

  # Splits the list into a group of consecutive elements having the same first component (nums1 value)
  defp split_group([], _value, acc), do: {Enum.reverse(acc), []}

  defp split_group([h = {v, _, _} | t], value, acc) when v == value,
    do: split_group(t, value, [h | acc])

  defp split_group(list, _value, acc), do: {Enum.reverse(acc), list}

  # Insert a value into the multiset represented by a gb_tree
  defp insert_val(tree, val) do
    case :gb_trees.lookup(val, tree) do
      :none -> :gb_trees.insert(val, 1, tree)
      {:value, cnt} -> :gb_trees.update(val, cnt + 1, tree)
    end
  end

  # Delete one occurrence of a value from the multiset
  defp delete_one(tree, val) do
    case :gb_trees.lookup(val, tree) do
      {:value, cnt} when cnt > 1 -> :gb_trees.update(val, cnt - 1, tree)
      {:value, 1} -> :gb_trees.delete(val, tree)
    end
  end
end
```
