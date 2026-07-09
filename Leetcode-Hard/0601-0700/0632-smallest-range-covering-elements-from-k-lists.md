# 0632. Smallest Range Covering Elements from K Lists

## Cpp

```cpp
class Solution {
public:
    vector<int> smallestRange(vector<vector<int>>& nums) {
        using T = pair<int, pair<int,int>>; // {value, {row, col}}
        priority_queue<T, vector<T>, greater<T>> minHeap;
        int currentMax = INT_MIN;
        for (int i = 0; i < nums.size(); ++i) {
            int val = nums[i][0];
            minHeap.push({val, {i, 0}});
            currentMax = max(currentMax, val);
        }
        int bestStart = -100000, bestEnd = 100000;
        while (minHeap.size() == nums.size()) {
            auto top = minHeap.top();
            minHeap.pop();
            int curMin = top.first;
            int row = top.second.first;
            int col = top.second.second;
            if (currentMax - curMin < bestEnd - bestStart ||
                (currentMax - curMin == bestEnd - bestStart && curMin < bestStart)) {
                bestStart = curMin;
                bestEnd = currentMax;
            }
            if (col + 1 == nums[row].size()) break;
            int nextVal = nums[row][col + 1];
            minHeap.push({nextVal, {row, col + 1}});
            if (nextVal > currentMax) currentMax = nextVal;
        }
        return {bestStart, bestEnd};
    }
};
```

## Java

```java
class Solution {
    public int[] smallestRange(List<List<Integer>> nums) {
        int k = nums.size();
        PriorityQueue<int[]> minHeap = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        int maxVal = Integer.MIN_VALUE;
        for (int i = 0; i < k; i++) {
            int val = nums.get(i).get(0);
            minHeap.offer(new int[]{val, i, 0});
            if (val > maxVal) {
                maxVal = val;
            }
        }

        int rangeStart = 0;
        int rangeEnd = Integer.MAX_VALUE;

        while (minHeap.size() == k) {
            int[] cur = minHeap.poll();
            int minVal = cur[0];
            int listIdx = cur[1];
            int elemIdx = cur[2];

            if ((maxVal - minVal < rangeEnd - rangeStart) ||
                (maxVal - minVal == rangeEnd - rangeStart && minVal < rangeStart)) {
                rangeStart = minVal;
                rangeEnd = maxVal;
            }

            elemIdx++;
            if (elemIdx < nums.get(listIdx).size()) {
                int nextVal = nums.get(listIdx).get(elemIdx);
                minHeap.offer(new int[]{nextVal, listIdx, elemIdx});
                if (nextVal > maxVal) {
                    maxVal = nextVal;
                }
            } else {
                break; // one list is exhausted
            }
        }

        return new int[]{rangeStart, rangeEnd};
    }
}
```

## Python

```python
import heapq
import sys

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        k = len(nums)
        heap = []
        cur_max = -sys.maxsize
        for i in range(k):
            val = nums[i][0]
            heap.append((val, i, 0))
            if val > cur_max:
                cur_max = val
        heapq.heapify(heap)

        best_start, best_end = 0, sys.maxsize
        best_len = best_end - best_start

        while True:
            cur_min, list_idx, elem_idx = heap[0]

            cur_len = cur_max - cur_min
            if cur_len < best_len or (cur_len == best_len and cur_min < best_start):
                best_start, best_end = cur_min, cur_max
                best_len = cur_len

            if elem_idx + 1 == len(nums[list_idx]):
                break

            next_val = nums[list_idx][elem_idx + 1]
            heapq.heapreplace(heap, (next_val, list_idx, elem_idx + 1))
            if next_val > cur_max:
                cur_max = next_val

        return [best_start, best_end]
```

## Python3

```python
import heapq
from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # Initialize min-heap with first element from each list
        heap = []
        current_max = -10**9  # smaller than any possible value
        for i, lst in enumerate(nums):
            val = lst[0]
            heap.append((val, i, 0))
            if val > current_max:
                current_max = val
        heapq.heapify(heap)

        best_start, best_end = -10**9, 10**9

        while True:
            current_min, list_idx, elem_idx = heapq.heappop(heap)

            # Update best range if needed
            if (current_max - current_min < best_end - best_start) or \
               (current_max - current_min == best_end - best_start and current_min < best_start):
                best_start, best_end = current_min, current_max

            # Move to next element in the same list
            if elem_idx + 1 == len(nums[list_idx]):
                break  # cannot cover all lists anymore
            next_val = nums[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
            if next_val > current_max:
                current_max = next_val

        return [best_start, best_end]
```

## C

```c
#include <stdlib.h>
#include <limits.h>

typedef struct {
    int val;
    int row;
    int col;
} Node;

int* smallestRange(int** nums, int numsSize, int* numsColSize, int* returnSize) {
    int k = numsSize;
    if (k == 0) {
        *returnSize = 0;
        return NULL;
    }

    Node *heap = (Node *)malloc(sizeof(Node) * k);
    int heapSize = 0;
    int maxVal = INT_MIN;

    // Build initial heap with first element of each list
    for (int i = 0; i < k; ++i) {
        Node node;
        node.val = nums[i][0];
        node.row = i;
        node.col = 0;
        heap[heapSize] = node;

        // up-heap
        int cur = heapSize;
        while (cur > 0) {
            int parent = (cur - 1) >> 1;
            if (heap[parent].val <= heap[cur].val) break;
            Node tmp = heap[parent];
            heap[parent] = heap[cur];
            heap[cur] = tmp;
            cur = parent;
        }
        ++heapSize;

        if (node.val > maxVal) maxVal = node.val;
    }

    int bestStart = 0, bestEnd = 0;
    int bestDiff = INT_MAX;

    while (heapSize == k) {
        Node minNode = heap[0];
        int curDiff = maxVal - minNode.val;
        if (curDiff < bestDiff || (curDiff == bestDiff && minNode.val < bestStart)) {
            bestDiff = curDiff;
            bestStart = minNode.val;
            bestEnd = maxVal;
        }

        int r = minNode.row;
        int c = minNode.col + 1;
        if (c >= numsColSize[r]) break; // one list exhausted

        Node newNode;
        newNode.val = nums[r][c];
        newNode.row = r;
        newNode.col = c;

        // replace root with new node and down-heap
        heap[0] = newNode;
        int idx = 0;
        while (1) {
            int left = (idx << 1) + 1;
            int right = left + 1;
            int smallest = idx;
            if (left < heapSize && heap[left].val < heap[smallest].val) smallest = left;
            if (right < heapSize && heap[right].val < heap[smallest].val) smallest = right;
            if (smallest == idx) break;
            Node tmp = heap[idx];
            heap[idx] = heap[smallest];
            heap[smallest] = tmp;
            idx = smallest;
        }

        if (newNode.val > maxVal) maxVal = newNode.val;
    }

    int *ans = (int *)malloc(sizeof(int) * 2);
    ans[0] = bestStart;
    ans[1] = bestEnd;
    *returnSize = 2;

    free(heap);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int[] SmallestRange(IList<IList<int>> nums) {
        int k = nums.Count;
        var pq = new PriorityQueue<(int val, int listIdx, int elemIdx), int>();
        int currentMax = int.MinValue;

        for (int i = 0; i < k; i++) {
            int val = nums[i][0];
            pq.Enqueue((val, i, 0), val);
            if (val > currentMax) currentMax = val;
        }

        int bestStart = 0;
        int bestEnd = int.MaxValue;

        while (pq.Count == k) {
            var (minVal, listIdx, elemIdx) = pq.Dequeue();

            // Update best range
            if (currentMax - minVal < bestEnd - bestStart ||
                (currentMax - minVal == bestEnd - bestStart && minVal < bestStart)) {
                bestStart = minVal;
                bestEnd = currentMax;
            }

            // Move to next element in the same list
            if (elemIdx + 1 < nums[listIdx].Count) {
                int nextVal = nums[listIdx][elemIdx + 1];
                pq.Enqueue((nextVal, listIdx, elemIdx + 1), nextVal);
                if (nextVal > currentMax) currentMax = nextVal;
            } else {
                // One of the lists is exhausted
                break;
            }
        }

        return new int[] { bestStart, bestEnd };
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} nums
 * @return {number[]}
 */
var smallestRange = function(nums) {
    class MinHeap {
        constructor(compare) {
            this.heap = [];
            this.compare = compare;
        }
        size() {
            return this.heap.length;
        }
        push(item) {
            const h = this.heap;
            h.push(item);
            let i = h.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (this.compare(h[i], h[p]) < 0) {
                    [h[i], h[p]] = [h[p], h[i]];
                    i = p;
                } else break;
            }
        }
        pop() {
            const h = this.heap;
            if (h.length === 1) return h.pop();
            const top = h[0];
            const last = h.pop();
            h[0] = last;
            let i = 0;
            while (true) {
                let l = i * 2 + 1,
                    r = l + 1,
                    smallest = i;
                if (l < h.length && this.compare(h[l], h[smallest]) < 0) smallest = l;
                if (r < h.length && this.compare(h[r], h[smallest]) < 0) smallest = r;
                if (smallest !== i) {
                    [h[i], h[smallest]] = [h[smallest], h[i]];
                    i = smallest;
                } else break;
            }
            return top;
        }
    }

    const k = nums.length;
    const heap = new MinHeap((a, b) => a[0] - b[0]); // compare by value
    let maxVal = -Infinity;

    for (let i = 0; i < k; ++i) {
        const val = nums[i][0];
        heap.push([val, i, 0]);
        if (val > maxVal) maxVal = val;
    }

    let bestStart = 0,
        bestEnd = Infinity;

    while (heap.size() === k) {
        const [minVal, listIdx, elemIdx] = heap.pop();

        // Update answer if better
        if (
            maxVal - minVal < bestEnd - bestStart ||
            (maxVal - minVal === bestEnd - bestStart && minVal < bestStart)
        ) {
            bestStart = minVal;
            bestEnd = maxVal;
        }

        // Move to next element in the same list
        if (elemIdx + 1 < nums[listIdx].length) {
            const nextVal = nums[listIdx][elemIdx + 1];
            heap.push([nextVal, listIdx, elemIdx + 1]);
            if (nextVal > maxVal) maxVal = nextVal;
        } else {
            break; // one list is exhausted
        }
    }

    return [bestStart, bestEnd];
};
```

## Typescript

```typescript
function smallestRange(nums: number[][]): number[] {
    const k = nums.length;
    // Min-heap implementation
    interface Node {
        val: number;
        row: number;
        col: number;
    }
    const heap: Node[] = [];

    function heapPush(node: Node): void {
        heap.push(node);
        let idx = heap.length - 1;
        while (idx > 0) {
            const parent = (idx - 1) >> 1;
            if (heap[parent].val <= heap[idx].val) break;
            [heap[parent], heap[idx]] = [heap[idx], heap[parent]];
            idx = parent;
        }
    }

    function heapPop(): Node {
        const top = heap[0];
        const last = heap.pop()!;
        if (heap.length > 0) {
            heap[0] = last;
            let idx = 0;
            const n = heap.length;
            while (true) {
                let left = idx * 2 + 1;
                let right = left + 1;
                let smallest = idx;
                if (left < n && heap[left].val < heap[smallest].val) smallest = left;
                if (right < n && heap[right].val < heap[smallest].val) smallest = right;
                if (smallest === idx) break;
                [heap[idx], heap[smallest]] = [heap[smallest], heap[idx]];
                idx = smallest;
            }
        }
        return top;
    }

    let maxVal = -Infinity;
    for (let i = 0; i < k; ++i) {
        const val = nums[i][0];
        heapPush({ val, row: i, col: 0 });
        if (val > maxVal) maxVal = val;
    }

    let bestStart = 0;
    let bestEnd = Number.MAX_SAFE_INTEGER;

    while (heap.length === k) {
        const node = heapPop();
        const minVal = node.val;

        // Update best range
        const curDiff = maxVal - minVal;
        const bestDiff = bestEnd - bestStart;
        if (
            curDiff < bestDiff ||
            (curDiff === bestDiff && minVal < bestStart)
        ) {
            bestStart = minVal;
            bestEnd = maxVal;
        }

        // Move to next element in the same list
        const nextCol = node.col + 1;
        if (nextCol < nums[node.row].length) {
            const nextVal = nums[node.row][nextCol];
            heapPush({ val: nextVal, row: node.row, col: nextCol });
            if (nextVal > maxVal) maxVal = nextVal;
        } else {
            break; // one list is exhausted
        }
    }

    return [bestStart, bestEnd];
}
```

## Php

```php
<?php
class MinHeap extends SplHeap {
    public function compare($a, $b) {
        // $a and $b are arrays: [value, listIdx, elemIdx]
        // For a min-heap we want smaller value to have higher priority,
        // so we reverse the comparison.
        return $b[0] <=> $a[0];
    }
}

class Solution {

    /**
     * @param Integer[][] $nums
     * @return Integer[]
     */
    function smallestRange($nums) {
        $k = count($nums);
        $heap = new MinHeap();
        $currentMax = PHP_INT_MIN;

        // Initialize heap with first element of each list
        foreach ($nums as $listIdx => $list) {
            $val = $list[0];
            $heap->insert([$val, $listIdx, 0]);
            if ($val > $currentMax) {
                $currentMax = $val;
            }
        }

        $bestStart = 0;
        $bestEnd   = PHP_INT_MAX;

        while ($heap->count() == $k) {
            [$minVal, $listIdx, $elemIdx] = $heap->extract();

            // Update best range if needed
            $currRange = $currentMax - $minVal;
            $bestRange = $bestEnd - $bestStart;
            if ($currRange < $bestRange || ($currRange == $bestRange && $minVal < $bestStart)) {
                $bestStart = $minVal;
                $bestEnd   = $currentMax;
            }

            // Move to next element in the same list
            $nextIdx = $elemIdx + 1;
            if ($nextIdx < count($nums[$listIdx])) {
                $nextVal = $nums[$listIdx][$nextIdx];
                $heap->insert([$nextVal, $listIdx, $nextIdx]);
                if ($nextVal > $currentMax) {
                    $currentMax = $nextVal;
                }
            } else {
                // One list is exhausted; cannot find further complete ranges
                break;
            }
        }

        return [$bestStart, $bestEnd];
    }
}
?>
```

## Swift

```swift
class Solution {
    struct Node {
        let val: Int
        let listIdx: Int
        let elemIdx: Int
    }
    
    struct MinHeap {
        private var data: [Node] = []
        
        var count: Int { data.count }
        
        mutating func push(_ node: Node) {
            data.append(node)
            siftUp(data.count - 1)
        }
        
        mutating func pop() -> Node? {
            guard !data.isEmpty else { return nil }
            let top = data[0]
            let last = data.removeLast()
            if !data.isEmpty {
                data[0] = last
                siftDown(0)
            }
            return top
        }
        
        private mutating func siftUp(_ index: Int) {
            var child = index
            while child > 0 {
                let parent = (child - 1) / 2
                if data[child].val < data[parent].val {
                    data.swapAt(child, parent)
                    child = parent
                } else { break }
            }
        }
        
        private mutating func siftDown(_ index: Int) {
            var parent = index
            while true {
                let left = 2 * parent + 1
                let right = left + 1
                var smallest = parent
                if left < data.count && data[left].val < data[smallest].val { smallest = left }
                if right < data.count && data[right].val < data[smallest].val { smallest = right }
                if smallest == parent { break }
                data.swapAt(parent, smallest)
                parent = smallest
            }
        }
    }
    
    func smallestRange(_ nums: [[Int]]) -> [Int] {
        var heap = MinHeap()
        var currentMax = Int.min
        
        for i in 0..<nums.count {
            let val = nums[i][0]
            heap.push(Node(val: val, listIdx: i, elemIdx: 0))
            if val > currentMax { currentMax = val }
        }
        
        var bestRange = [0, 0]
        var minSize = Int.max
        
        while heap.count == nums.count {
            guard let node = heap.pop() else { break }
            let curMin = node.val
            if currentMax - curMin < minSize || (currentMax - curMin == minSize && curMin < bestRange[0]) {
                bestRange[0] = curMin
                bestRange[1] = currentMax
                minSize = currentMax - curMin
            }
            
            let nextIdx = node.elemIdx + 1
            if nextIdx < nums[node.listIdx].count {
                let nextVal = nums[node.listIdx][nextIdx]
                heap.push(Node(val: nextVal, listIdx: node.listIdx, elemIdx: nextIdx))
                if nextVal > currentMax { currentMax = nextVal }
            } else {
                break
            }
        }
        
        return bestRange
    }
}
```

## Kotlin

```kotlin
import java.util.PriorityQueue

class Solution {
    data class Node(val value: Int, val row: Int, val col: Int)

    fun smallestRange(nums: List<List<Int>>): IntArray {
        val k = nums.size
        val pq = PriorityQueue<Node>(compareBy { it.value })
        var currentMax = Int.MIN_VALUE

        for (i in 0 until k) {
            val v = nums[i][0]
            pq.offer(Node(v, i, 0))
            if (v > currentMax) currentMax = v
        }

        var bestStart = 0
        var bestEnd = Int.MAX_VALUE

        while (true) {
            val minNode = pq.poll() ?: break
            val curMin = minNode.value

            if (currentMax - curMin < bestEnd - bestStart ||
                (currentMax - curMin == bestEnd - bestStart && curMin < bestStart)
            ) {
                bestStart = curMin
                bestEnd = currentMax
            }

            val nextCol = minNode.col + 1
            if (nextCol >= nums[minNode.row].size) {
                break
            }
            val nextVal = nums[minNode.row][nextCol]
            pq.offer(Node(nextVal, minNode.row, nextCol))
            if (nextVal > currentMax) currentMax = nextVal
        }

        return intArrayOf(bestStart, bestEnd)
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  List<int> smallestRange(List<List<int>> nums) {
    int k = nums.length;
    var heap = HeapPriorityQueue<List<int>>((a, b) => a[0].compareTo(b[0]));
    int currentMax = -1000000000;

    for (int i = 0; i < k; i++) {
      int val = nums[i][0];
      heap.add([val, i, 0]);
      if (val > currentMax) currentMax = val;
    }

    int bestStart = 0;
    int bestEnd = 2000000000;

    while (heap.length == k) {
      var smallest = heap.removeFirst();
      int curMin = smallest[0];
      int listIdx = smallest[1];
      int elemIdx = smallest[2];

      if ((currentMax - curMin) < (bestEnd - bestStart) ||
          ((currentMax - curMin) == (bestEnd - bestStart) && curMin < bestStart)) {
        bestStart = curMin;
        bestEnd = currentMax;
      }

      if (elemIdx + 1 < nums[listIdx].length) {
        int nextVal = nums[listIdx][elemIdx + 1];
        heap.add([nextVal, listIdx, elemIdx + 1]);
        if (nextVal > currentMax) currentMax = nextVal;
      } else {
        break;
      }
    }

    return [bestStart, bestEnd];
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
	row int
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
	*h = old[0 : n-1]
	return it
}

func smallestRange(nums [][]int) []int {
	if len(nums) == 0 {
		return []int{}
	}
	k := len(nums)
	h := &minHeap{}
	heap.Init(h)

	maxVal := -int(^uint(0)>>1) - 1 // MinInt
	for i, arr := range nums {
		val := arr[0]
		heap.Push(h, item{val: val, row: i, idx: 0})
		if val > maxVal {
			maxVal = val
		}
	}

	minInt := int(^uint(0) >> 1)
	bestStart, bestEnd := minInt, -minInt

	for h.Len() == k {
		it := heap.Pop(h).(item)

		if maxVal-it.val < bestEnd-bestStart || (maxVal-it.val == bestEnd-bestStart && it.val < bestStart) {
			bestStart = it.val
			bestEnd = maxVal
		}

		if it.idx+1 < len(nums[it.row]) {
			nextIdx := it.idx + 1
			nextVal := nums[it.row][nextIdx]
			heap.Push(h, item{val: nextVal, row: it.row, idx: nextIdx})
			if nextVal > maxVal {
				maxVal = nextVal
			}
		} else {
			break
		}
	}

	return []int{bestStart, bestEnd}
}
```

## Ruby

```ruby
def smallest_range(nums)
  k = nums.size
  heap = []
  max_val = -Float::INFINITY

  # Heap helper methods
  push = lambda do |item|
    heap << item
    idx = heap.size - 1
    while idx > 0
      parent = (idx - 1) / 2
      break if heap[parent][0] <= heap[idx][0]
      heap[parent], heap[idx] = heap[idx], heap[parent]
      idx = parent
    end
  end

  pop_min = lambda do
    top = heap[0]
    last = heap.pop
    unless heap.empty?
      heap[0] = last
      idx = 0
      size = heap.size
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

  # Initialize heap with first element of each list
  nums.each_with_index do |list, i|
    val = list[0]
    push.call([val, i, 0])
    max_val = val if val > max_val
  end

  best_start = 0
  best_end = (1 << 60)

  while heap.size == k
    min_val, list_idx, elem_idx = pop_min.call
    # Update best range if needed
    if (max_val - min_val < best_end - best_start) ||
       ((max_val - min_val == best_end - best_start) && (min_val < best_start))
      best_start = min_val
      best_end = max_val
    end

    # Move to next element in the same list
    if elem_idx + 1 < nums[list_idx].size
      next_val = nums[list_idx][elem_idx + 1]
      push.call([next_val, list_idx, elem_idx + 1])
      max_val = next_val if next_val > max_val
    else
      break
    end
  end

  [best_start, best_end]
end
```

## Scala

```scala
object Solution {
  import java.util.PriorityQueue

  def smallestRange(nums: List[List[Int]]): Array[Int] = {
    val k = nums.length
    val pq = new PriorityQueue[(Int, Int, Int)](
      (a: (Int, Int, Int), b: (Int, Int, Int)) => Integer.compare(a._1, b._1)
    )
    var maxVal = Int.MinValue

    for (i <- 0 until k) {
      val v = nums(i)(0)
      pq.offer((v, i, 0))
      if (v > maxVal) maxVal = v
    }

    var bestStart = 0
    var bestEnd = Int.MaxValue

    while (true) {
      val cur = pq.poll()
      val minVal = cur._1
      val row = cur._2
      val col = cur._3

      if ((maxVal - minVal < bestEnd - bestStart) ||
          (maxVal - minVal == bestEnd - bestStart && minVal < bestStart)) {
        bestStart = minVal
        bestEnd = maxVal
      }

      if (col + 1 >= nums(row).length) {
        return Array(bestStart, bestEnd)
      } else {
        val nextVal = nums(row)(col + 1)
        pq.offer((nextVal, row, col + 1))
        if (nextVal > maxVal) maxVal = nextVal
      }
    }

    Array(bestStart, bestEnd) // unreachable
  }
}
```

## Rust

```rust
use std::cmp::{max, Reverse};
use std::collections::BinaryHeap;

impl Solution {
    pub fn smallest_range(nums: Vec<Vec<i32>>) -> Vec<i32> {
        let k = nums.len();
        let mut heap: BinaryHeap<Reverse<(i32, usize, usize)>> = BinaryHeap::with_capacity(k);
        let mut current_max = i32::MIN;

        for (i, list) in nums.iter().enumerate() {
            let val = list[0];
            heap.push(Reverse((val, i, 0)));
            current_max = max(current_max, val);
        }

        let mut best_start = 0;
        let mut best_end = i32::MAX;

        while heap.len() == k {
            let Reverse((min_val, list_idx, elem_idx)) = heap.pop().unwrap();

            // Update best range if needed
            if current_max - min_val < best_end - best_start
                || (current_max - min_val == best_end - best_start && min_val < best_start)
            {
                best_start = min_val;
                best_end = current_max;
            }

            // Move to next element in the same list
            if elem_idx + 1 < nums[list_idx].len() {
                let next_idx = elem_idx + 1;
                let next_val = nums[list_idx][next_idx];
                heap.push(Reverse((next_val, list_idx, next_idx)));
                current_max = max(current_max, next_val);
            } else {
                break; // one list is exhausted
            }
        }

        vec![best_start, best_end]
    }
}
```

## Racket

```racket
(require racket/priority-queue)

(define/contract (smallest-range nums)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ([k (length nums)]
         [less? (lambda (a b) (< (first a) (first b)))]
         [pq (make-pq less?)])
    ;; insert first element of each list and compute initial max
    (define maxVal
      (apply max (map (lambda (lst) (first lst)) nums)))
    (for ([i (in-range k)])
      (let* ([lst (list-ref nums i)]
             [val (first lst)])
        (pq-add! pq (list val i 0))))
    ;; initialize best range using current min
    (define cur-min (first (pq-peek pq)))
    (define best-start cur-min)
    (define best-end maxVal)

    (let loop ()
      (when (= (pq-size pq) k)
        (define min-item (pq-pop! pq))
        (define min-val (first min-item))
        (define list-idx (second min-item))
        (define elem-idx (third min-item))

        ;; update best range if better
        (let* ([cur-len (- maxVal min-val)]
               [best-len (- best-end best-start)])
          (when (or (< cur-len best-len)
                    (and (= cur-len best-len) (< min-val best-start)))
            (set! best-start min-val)
            (set! best-end maxVal)))

        ;; advance in the list that provided the current minimum
        (let* ([lst (list-ref nums list-idx)]
               [next-idx (+ elem-idx 1)])
          (if (< next-idx (length lst))
              (begin
                (define next-val (list-ref lst next-idx))
                (pq-add! pq (list next-val list-idx next-idx))
                (when (> next-val maxVal) (set! maxVal next-val))
                (loop))
              ;; one list exhausted, stop looping
              (void)))))
    (list best-start best-end)))
```

## Erlang

```erlang
-spec smallest_range(Nums :: [[integer()]]) -> [integer()].
smallest_range(Nums) ->
    NumsTuple = list_to_tuple(Nums),
    K = tuple_size(NumsTuple),
    {InitTree, InitMax} = init_heap(K, NumsTuple, gb_trees:empty(), -2000000),
    {MinKey, _} = gb_trees:smallest(InitTree),
    MinVal = element(1, MinKey),
    loop(InitTree, InitMax, MinVal, InitMax, NumsTuple).

init_heap(0, _, Tree, Max) ->
    {Tree, Max};
init_heap(I, NumsTuple, TreeAcc, MaxAcc) ->
    List = element(I, NumsTuple),
    [First | _] = List,
    ListIdx = I - 1,
    NewTree = gb_trees:insert({First, ListIdx}, {ListIdx, 0}, TreeAcc),
    NewMax = erlang:max(MaxAcc, First),
    init_heap(I - 1, NumsTuple, NewTree, NewMax).

loop(Tree, MaxVal, BestStart, BestEnd, NumsTuple) ->
    case gb_trees:is_empty(Tree) of
        true -> [BestStart, BestEnd];
        false ->
            {MinKey, {ListIdx, ElemIdx}} = gb_trees:smallest(Tree),
            MinVal = element(1, MinKey),
            RangeLen = MaxVal - MinVal,
            BestLen = BestEnd - BestStart,
            {NewBestStart, NewBestEnd} =
                if
                    RangeLen < BestLen orelse (RangeLen == BestLen andalso MinVal < BestStart) ->
                        {MinVal, MaxVal};
                    true -> {BestStart, BestEnd}
                end,
            List = element(ListIdx + 1, NumsTuple),
            Len = length(List),
            NextIdx = ElemIdx + 1,
            if
                NextIdx >= Len ->
                    [NewBestStart, NewBestEnd];
                true ->
                    NextVal = lists:nth(NextIdx + 1, List),
                    NewMax = erlang:max(MaxVal, NextVal),
                    Tree2 = gb_trees:delete(MinKey, Tree),
                    Tree3 = gb_trees:insert({NextVal, ListIdx}, {ListIdx, NextIdx}, Tree2),
                    loop(Tree3, NewMax, NewBestStart, NewBestEnd, NumsTuple)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec smallest_range(nums :: [[integer]]) :: [integer]
  def smallest_range(nums) do
    k = length(nums)

    merged =
      Enum.flat_map(Enum.with_index(nums), fn {list, idx} ->
        Enum.map(list, fn v -> {v, idx} end)
      end)

    sorted = Enum.sort_by(merged, fn {v, _} -> v end)
    arr = :array.from_list(sorted)
    total = :array.size(arr)

    # start recursion
    {best_start, best_end, _left, _covered, _freq} =
      rec(0, 0, %{}, 0, nil, nil, arr, total, k)

    [best_start, best_end]
  end

  defp rec(right, left, freq, covered, best_start, best_end, arr, total, k) do
    if right < total do
      {val_r, idx_r} = :array.get(right, arr)
      cnt = Map.get(freq, idx_r, 0)
      freq = Map.put(freq, idx_r, cnt + 1)
      covered = if cnt == 0, do: covered + 1, else: covered

      {best_start, best_end, left, covered, freq} =
        shrink_window(arr, left, right, freq, covered, best_start, best_end, k)

      rec(right + 1, left, freq, covered, best_start, best_end, arr, total, k)
    else
      {best_start, best_end, left, covered, freq}
    end
  end

  defp shrink_window(arr, left, right, freq, covered, best_start, best_end, k) do
    if covered == k do
      {val_l, idx_l} = :array.get(left, arr)
      {val_r, _} = :array.get(right, arr)

      range_len = val_r - val_l

      {new_best_start, new_best_end} =
        cond do
          best_start == nil ->
            {val_l, val_r}

          range_len < (best_end - best_start) ->
            {val_l, val_r}

          range_len == (best_end - best_start) and val_l < best_start ->
            {val_l, val_r}

          true ->
            {best_start, best_end}
        end

      cnt_l = Map.get(freq, idx_l)
      freq =
        if cnt_l == 1 do
          Map.delete(freq, idx_l)
        else
          Map.put(freq, idx_l, cnt_l - 1)
        end

      covered = if cnt_l == 1, do: covered - 1, else: covered

      shrink_window(arr, left + 1, right, freq, covered, new_best_start, new_best_end, k)
    else
      {best_start, best_end, left, covered, freq}
    end
  end
end
```
