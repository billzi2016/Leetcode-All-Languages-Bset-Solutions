# 2386. Find the K-Sum of an Array

## Cpp

```cpp
class Solution {
public:
    long long kSum(vector<int>& nums, int k) {
        long long total = 0;
        vector<long long> a;
        a.reserve(nums.size());
        for (int x : nums) {
            if (x >= 0) total += x;
            a.push_back(std::llabs((long long)x));
        }
        sort(a.begin(), a.end());
        using P = pair<long long,int>;
        priority_queue<P, vector<P>, greater<P>> pq;
        int n = a.size();
        if (n > 0) pq.emplace(a[0], 0);
        vector<long long> sums;
        sums.reserve(k);
        sums.push_back(0); // empty subset
        while ((int)sums.size() < k) {
            auto [s, i] = pq.top(); pq.pop();
            sums.push_back(s);
            if (i + 1 < n) {
                pq.emplace(s + a[i+1], i+1);
                pq.emplace(s - a[i] + a[i+1], i+1);
            }
        }
        long long kth_smallest = sums[k-1];
        return total - kth_smallest;
    }
};
```

## Java

```java
class Solution {
    public long kSum(int[] nums, int k) {
        long base = 0;
        int n = nums.length;
        long[] absVals = new long[n];
        for (int i = 0; i < n; i++) {
            if (nums[i] > 0) base += nums[i];
            absVals[i] = Math.abs((long) nums[i]);
        }
        java.util.Arrays.sort(absVals);
        // list of smallest subset sums (including empty set)
        java.util.ArrayList<Long> smallest = new java.util.ArrayList<>(k);
        smallest.add(0L); // empty subset
        if (k == 1) return base; // only the largest sum needed

        class Node {
            long sum;
            int idx;
            Node(long s, int i) { sum = s; idx = i; }
        }

        java.util.PriorityQueue<Node> pq = new java.util.PriorityQueue<>(
                (a, b) -> Long.compare(a.sum, b.sum)
        );

        if (n > 0) {
            pq.offer(new Node(absVals[0], 0));
        }

        while (smallest.size() < k && !pq.isEmpty()) {
            Node cur = pq.poll();
            smallest.add(cur.sum);
            int i = cur.idx;
            if (i + 1 < n) {
                // replace current element with the next one
                long sumReplace = cur.sum - absVals[i] + absVals[i + 1];
                pq.offer(new Node(sumReplace, i + 1));
                // add the next element in addition to current subset
                long sumAdd = cur.sum + absVals[i + 1];
                pq.offer(new Node(sumAdd, i + 1));
            }
        }

        long kthSmallestSubsetSum = smallest.get(k - 1);
        return base - kthSmallestSubsetSum;
    }
}
```

## Python

```python
class Solution(object):
    def kSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        base = sum(x for x in nums if x > 0)
        costs = [abs(x) for x in nums]
        costs.sort()
        import heapq
        n = len(costs)
        heap = []
        if n:
            heapq.heappush(heap, (costs[0], 0))
        res = [0]  # smallest subset sum is 0
        while len(res) < k:
            s, i = heapq.heappop(heap)
            res.append(s)
            if i + 1 < n:
                # replace costs[i] with costs[i+1]
                heapq.heappush(heap, (s - costs[i] + costs[i + 1], i + 1))
                # add costs[i+1] additionally
                heapq.heappush(heap, (s + costs[i + 1], i + 1))
        return base - res[k - 1]
```

## Python3

```python
import heapq
from typing import List

class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        base = sum(x for x in nums if x > 0)
        w = [abs(x) for x in nums]
        w.sort()
        n = len(w)

        # generate the k smallest subset sums of w (including empty subset)
        smallest = [0]  # empty subset sum
        heap = []
        if n:
            heapq.heappush(heap, (w[0], 0))

        while len(smallest) < k and heap:
            s, i = heapq.heappop(heap)
            smallest.append(s)
            if i + 1 < n:
                # replace w[i] with w[i+1]
                heapq.heappush(heap, (s - w[i] + w[i + 1], i + 1))
                # add w[i+1] additionally
                heapq.heappush(heap, (s + w[i + 1], i + 1))

        return base - smallest[k - 1]
```

## C

```c
#include <stdlib.h>
#include <stddef.h>

typedef struct {
    long long sum;
    int idx;
} Node;

static void heapSwap(Node *a, Node *b) {
    Node t = *a; *a = *b; *b = t;
}

static void heapPush(Node *h, int *sz, Node v) {
    int i = (*sz)++;
    h[i] = v;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (h[p].sum <= h[i].sum) break;
        heapSwap(&h[p], &h[i]);
        i = p;
    }
}

static Node heapPop(Node *h, int *sz) {
    Node ret = h[0];
    (*sz)--;
    h[0] = h[*sz];
    int i = 0;
    while (1) {
        int l = i * 2 + 1, r = l + 1, s = i;
        if (l < *sz && h[l].sum < h[s].sum) s = l;
        if (r < *sz && h[r].sum < h[s].sum) s = r;
        if (s == i) break;
        heapSwap(&h[i], &h[s]);
        i = s;
    }
    return ret;
}

static int cmp_ll(const void *a, const void *b) {
    long long x = *(const long long *)a;
    long long y = *(const long long *)b;
    if (x < y) return -1;
    if (x > y) return 1;
    return 0;
}

long long kSum(int* nums, int numsSize, int k) {
    long long base = 0;
    long long *costs = (long long *)malloc(sizeof(long long) * (size_t)numsSize);
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] > 0) base += nums[i];
        costs[i] = llabs((long long)nums[i]);
    }
    qsort(costs, (size_t)numsSize, sizeof(long long), cmp_ll);

    int heapCap = (k + 5) * 2 + 5;
    Node *heap = (Node *)malloc(sizeof(Node) * (size_t)heapCap);
    int heapSize = 0;

    if (numsSize > 0) {
        heapPush(heap, &heapSize, (Node){costs[0], 0});
    }

    long long answer = base;          // k == 1 case
    if (k == 1) {
        free(costs);
        free(heap);
        return answer;
    }

    int cnt = 1;                      // counted the empty subset sum (0)
    while (cnt < k && heapSize > 0) {
        Node cur = heapPop(heap, &heapSize);
        long long s = cur.sum;
        int i = cur.idx;

        ++cnt;
        if (cnt == k) {
            answer = base - s;
            break;
        }

        if (i + 1 < numsSize) {
            heapPush(heap, &heapSize, (Node){s + costs[i + 1], i + 1});
            heapPush(heap, &heapSize, (Node){s - costs[i] + costs[i + 1], i + 1});
        }
    }

    free(costs);
    free(heap);
    return answer;
}
```

## Csharp

```csharp
public class Solution {
    public long KSum(int[] nums, int k) {
        long baseSum = 0;
        List<long> penaltiesVals = new List<long>();
        foreach (int x in nums) {
            if (x > 0) {
                baseSum += x;
                penaltiesVals.Add(x);
            } else {
                penaltiesVals.Add(-(long)x);
            }
        }

        penaltiesVals.Sort();
        int n = penaltiesVals.Count;

        var pq = new PriorityQueue<(long sum, int idx), long>();
        List<long> smallestPenalties = new List<long>(k);
        smallestPenalties.Add(0);

        if (n > 0) {
            pq.Enqueue((penaltiesVals[0], 0), penaltiesVals[0]);
        }

        while (smallestPenalties.Count < k && pq.Count > 0) {
            var cur = pq.Dequeue();
            long s = cur.sum;
            int i = cur.idx;
            smallestPenalties.Add(s);

            if (i + 1 < n) {
                long includeNext = s + penaltiesVals[i + 1];
                pq.Enqueue((includeNext, i + 1), includeNext);
                long replaceCurrent = s - penaltiesVals[i] + penaltiesVals[i + 1];
                pq.Enqueue((replaceCurrent, i + 1), replaceCurrent);
            }
        }

        long kthPenalty = smallestPenalties[k - 1];
        return baseSum - kthPenalty;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var kSum = function(nums, k) {
    let base = 0;
    const w = [];
    for (const x of nums) {
        if (x > 0) base += x;
        w.push(Math.abs(x));
    }
    w.sort((a, b) => a - b);
    
    // The largest subsequence sum is the sum of all positive numbers.
    if (k === 1) return base;
    
    const target = k - 1; // we need the (k-1)-th smallest subset sum of w
    
    class MinHeap {
        constructor() { this.heap = []; }
        size() { return this.heap.length; }
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
            if (h.length === 0) return null;
            const top = h[0];
            const last = h.pop();
            if (h.length > 0) {
                h[0] = last;
                let i = 0;
                while (true) {
                    let l = i * 2 + 1, r = l + 1, smallest = i;
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
    
    const heap = new MinHeap();
    if (w.length > 0) heap.push([w[0], 0]);
    
    let cnt = 0;
    let curSum = 0;
    while (cnt < target) {
        const node = heap.pop();
        if (!node) break; // safety, should not happen
        const [sum, idx] = node;
        curSum = sum;
        cnt++;
        if (idx + 1 < w.length) {
            heap.push([sum + w[idx + 1], idx + 1]);               // add next element
            heap.push([sum - w[idx] + w[idx + 1], idx + 1]);      // replace current with next
        }
    }
    
    return base - curSum;
};
```

## Typescript

```typescript
function kSum(nums: number[], k: number): number {
    // Sum of all positive numbers gives the maximum possible subsequence sum
    const base = nums.reduce((s, v) => s + (v > 0 ? v : 0), 0);
    // Work with absolute values; any subset sum can be expressed as base - sum_of_selected_abs
    const absVals = nums.map(v => Math.abs(v));
    absVals.sort((a, b) => a - b);
    const n = absVals.length;

    class MinHeap {
        private heap: [number, number][] = [];
        push(item: [number, number]): void {
            this.heap.push(item);
            this.bubbleUp(this.heap.length - 1);
        }
        pop(): [number, number] | undefined {
            if (this.heap.length === 0) return undefined;
            const top = this.heap[0];
            const last = this.heap.pop()!;
            if (this.heap.length > 0) {
                this.heap[0] = last;
                this.bubbleDown(0);
            }
            return top;
        }
        get size(): number {
            return this.heap.length;
        }
        private bubbleUp(idx: number): void {
            while (idx > 0) {
                const parent = (idx - 1) >> 1;
                if (this.heap[parent][0] <= this.heap[idx][0]) break;
                [this.heap[parent], this.heap[idx]] = [this.heap[idx], this.heap[parent]];
                idx = parent;
            }
        }
        private bubbleDown(idx: number): void {
            const len = this.heap.length;
            while (true) {
                let left = idx * 2 + 1;
                let right = left + 1;
                let smallest = idx;
                if (left < len && this.heap[left][0] < \`\${this.heap[smallest][0]}\`) smallest = left;
                if (right < len && this.heap[right][0] < this.heap[smallest][0]) smallest = right;
                if (smallest === idx) break;
                [this.heap[smallest], this.heap[idx]] = [this.heap[idx], this.heap[smallest]];
                idx = smallest;
            }
        }
    }

    const heap = new MinHeap();
    if (n > 0) heap.push([absVals[0], 0]);

    const smallestSums: number[] = [0]; // S = sum of selected absolute values, start with empty set
    while (smallestSums.length < k && heap.size > 0) {
        const [curSum, idx] = heap.pop()!;
        smallestSums.push(curSum);
        if (idx + 1 < n) {
            // take the next element in addition to current selection
            heap.push([curSum + absVals[idx + 1], idx + 1]);
            // replace current element with the next one
            heap.push([curSum - absVals[idx] + absVals[idx + 1], idx + 1]);
        }
    }

    const kthSmallest = smallestSums[k - 1];
    return base - kthSmallest;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function kSum($nums, $k) {
        $base = 0;
        $absVals = [];
        foreach ($nums as $v) {
            if ($v > 0) {
                $base += $v;
            }
            $absVals[] = abs($v);
        }

        sort($absVals); // ascending
        $n = count($absVals);

        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        if ($n > 0) {
            $firstSum = $absVals[0];
            $pq->insert([$firstSum, 0], -$firstSum); // min-heap via negative priority
        }

        $reductions = [0]; // empty subset sum

        while (count($reductions) < $k) {
            $node = $pq->extract();
            [$currSum, $idx] = $node;
            $reductions[] = $currSum;

            if ($idx + 1 < $n) {
                // add next element
                $newSum = $currSum + $absVals[$idx + 1];
                $pq->insert([$newSum, $idx + 1], -$newSum);
                // replace current element with next one
                $newSum2 = $currSum - $absVals[$idx] + $absVals[$idx + 1];
                $pq->insert([$newSum2, $idx + 1], -$newSum2);
            }
        }

        return $base - $reductions[$k - 1];
    }
}
```

## Swift

```swift
class Solution {
    func kSum(_ nums: [Int], _ k: Int) -> Int {
        var base = 0
        var costs = [Int]()
        for v in nums {
            if v > 0 { base += v }
            costs.append(abs(v))
        }
        costs.sort()
        
        // Min-heap for (sum, index)
        struct Heap<Element> {
            var elements: [Element] = []
            let priorityFunction: (Element, Element) -> Bool
            init(sort: @escaping (Element, Element) -> Bool) { self.priorityFunction = sort }
            var isEmpty: Bool { elements.isEmpty }
            mutating func insert(_ value: Element) {
                elements.append(value)
                siftUp(elements.count - 1)
            }
            mutating func remove() -> Element? {
                guard !elements.isEmpty else { return nil }
                if elements.count == 1 { return elements.removeLast() }
                let value = elements[0]
                elements[0] = elements.removeLast()
                siftDown(0)
                return value
            }
            mutating private func siftUp(_ index: Int) {
                var child = index
                var parent = (child - 1) / 2
                while child > 0 && priorityFunction(elements[child], elements[parent]) {
                    elements.swapAt(child, parent)
                    child = parent
                    parent = (child - 1) / 2
                }
            }
            mutating private func siftDown(_ index: Int) {
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
        
        var heap = Heap<(sum: Int, idx: Int)>(sort: { $0.sum < $1.sum })
        if !costs.isEmpty {
            heap.insert((costs[0], 0))
        }
        
        // The empty subset sum (0) is the smallest
        if k == 1 { return base }   // base - 0
        
        var count = 1   // already counted sum = 0
        while let node = heap.remove() {
            let s = node.sum
            let i = node.idx
            count += 1
            if count == k {
                return base - s
            }
            if i + 1 < costs.count {
                heap.insert((s + costs[i + 1], i + 1))
                heap.insert((s - costs[i] + costs[i + 1], i + 1))
            }
        }
        // Fallback (should not reach here given constraints)
        return base
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun kSum(nums: IntArray, k: Int): Long {
        var base = 0L
        val absList = ArrayList<Long>(nums.size)
        for (v in nums) {
            if (v > 0) base += v.toLong()
            absList.add(kotlin.math.abs(v).toLong())
        }
        absList.sort()
        if (k == 1) return base
        val n = absList.size
        val pq = java.util.PriorityQueue<Pair<Long, Int>>(compareBy { it.first })
        var count = 1 // sum 0 already counted
        if (n > 0) {
            pq.add(Pair(absList[0], 0))
        }
        while (count < k) {
            val (curSum, idx) = pq.poll()
            count++
            if (count == k) {
                return base - curSum
            }
            if (idx + 1 < n) {
                // add next element to current subset
                pq.add(Pair(curSum + absList[idx + 1], idx + 1))
                // replace current last element with the next one
                pq.add(Pair(curSum - absList[idx] + absList[idx + 1], idx + 1))
            }
        }
        return base
    }
}
```

## Dart

```dart
class Solution {
  int kSum(List<int> nums, int k) {
    // Sum of all positive numbers
    int base = 0;
    List<int> w = List.filled(nums.length, 0);
    for (int i = 0; i < nums.length; ++i) {
      int val = nums[i];
      if (val > 0) base += val;
      w[i] = val.abs();
    }
    // Sort absolute values in descending order
    w.sort((a, b) => b.compareTo(a));

    // Max-heap implementation
    final List<_Node> heap = [];

    void push(_Node node) {
      heap.add(node);
      int i = heap.length - 1;
      while (i > 0) {
        int p = (i - 1) >> 1;
        if (heap[p].sum >= heap[i].sum) break;
        final tmp = heap[p];
        heap[p] = heap[i];
        heap[i] = tmp;
        i = p;
      }
    }

    _Node pop() {
      final top = heap[0];
      final last = heap.removeLast();
      if (heap.isNotEmpty) {
        heap[0] = last;
        int i = 0;
        while (true) {
          int left = i * 2 + 1;
          int right = left + 1;
          if (left >= heap.length) break;
          int largest = left;
          if (right < heap.length && heap[right].sum > heap[left].sum) {
            largest = right;
          }
          if (heap[i].sum >= heap[largest].sum) break;
          final tmp = heap[i];
          heap[i] = heap[largest];
          heap[largest] = tmp;
          i = largest;
        }
      }
      return top;
    }

    // Initialize heap with the maximum possible sum
    push(_Node(base, 0));

    int answer = 0;
    for (int cnt = 0; cnt < k; ++cnt) {
      final cur = pop();
      answer = cur.sum;
      int idx = cur.idx;
      if (idx < w.length) {
        // Exclude current absolute value
        push(_Node(cur.sum - w[idx], idx + 1));
        // Replace it with the next one, if exists
        if (idx + 1 < w.length) {
          push(_Node(cur.sum - w[idx] + w[idx + 1], idx + 1));
        }
      }
    }
    return answer;
  }
}

class _Node {
  int sum;
  int idx;
  _Node(this.sum, this.idx);
}
```

## Golang

```go
import (
	"container/heap"
	"sort"
)

type item struct {
	sum int64
	idx int
}

type minHeap []item

func (h minHeap) Len() int            { return len(h) }
func (h minHeap) Less(i, j int) bool  { return h[i].sum < h[j].sum }
func (h minHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *minHeap) Push(x interface{}) { *h = append(*h, x.(item)) }
func (h *minHeap) Pop() interface{} {
	old := *h
	n := len(old)
	it := old[n-1]
	*h = old[:n-1]
	return it
}

func kSum(nums []int, k int) int64 {
	var base int64
	b := make([]int64, len(nums))
	for i, v := range nums {
		if v > 0 {
			base += int64(v)
		}
		if v < 0 {
			b[i] = int64(-v)
		} else {
			b[i] = int64(v)
		}
	}
	sort.Slice(b, func(i, j int) bool { return b[i] < b[j] })
	n := len(b)

	h := &minHeap{}
	heap.Init(h)
	if n > 0 {
		heap.Push(h, item{sum: b[0], idx: 0})
	}

	count := 1 // empty subset sum = 0
	var cur int64 = 0
	if k == 1 {
		return base
	}
	for count < k {
		it := heap.Pop(h).(item)
		cur = it.sum
		count++
		i := it.idx
		if i+1 < n {
			heap.Push(h, item{sum: cur + b[i+1], idx: i + 1})
			heap.Push(h, item{sum: cur - b[i] + b[i+1], idx: i + 1})
		}
	}
	return base - cur
}
```

## Ruby

```ruby
def heap_push(heap, item)
  heap << item
  i = heap.size - 1
  while i > 0
    p = (i - 1) >> 1
    break if heap[p][0] <= item[0]
    heap[i] = heap[p]
    i = p
  end
  heap[i] = item
end

def heap_pop(heap)
  top = heap[0]
  last = heap.pop
  unless heap.empty?
    i = 0
    while (child = i * 2 + 1) < heap.size
      right = child + 1
      child = right if right < heap.size && heap[right][0] < heap[child][0]
      break if last[0] <= heap[child][0]
      heap[i] = heap[child]
      i = child
    end
    heap[i] = last
  end
  top
end

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def k_sum(nums, k)
  base = 0
  w = []
  nums.each do |x|
    if x >= 0
      base += x
      w << x
    else
      w << -x
    end
  end

  w.sort!
  heap = []
  heap_push(heap, [w[0], 0]) unless w.empty?

  sums = [0] # smallest subset sum (empty set)
  while sums.size < k && !heap.empty?
    s, i = heap_pop(heap)
    sums << s
    nxt = i + 1
    if nxt < w.length
      heap_push(heap, [s + w[nxt], nxt])
      heap_push(heap, [s - w[i] + w[nxt], nxt])
    end
  end

  base - sums[k - 1]
end
```

## Scala

```scala
object Solution {
    def kSum(nums: Array[Int], k: Int): Long = {
        val n = nums.length
        var base: Long = 0L
        val absVals = new Array[Long](n)
        var i = 0
        while (i < n) {
            val v = nums(i).toLong
            if (v > 0) base += v
            absVals(i) = if (v >= 0) v else -v
            i += 1
        }
        java.util.Arrays.sort(absVals) // sort ascending

        val pq = new java.util.PriorityQueue[(Long, Int)](
          new java.util.Comparator[(Long, Int)] {
            override def compare(a: (Long, Int), b: (Long, Int)): Int = {
              if (a._1 < b._1) -1
              else if (a._1 > b._1) 1
              else a._2 - b._2
            }
          }
        )

        if (n > 0) pq.offer((absVals(0), 0))

        var count = 0
        var answer: Long = base

        while (count < k) {
          if (count == 0) {
            answer = base
            count += 1
          } else {
            val cur = pq.poll()
            val curSum = cur._1
            val idx = cur._2
            answer = base - curSum
            count += 1

            if (idx + 1 < n) {
              // replace current element with the next one
              val sumReplace = curSum - absVals(idx) + absVals(idx + 1)
              pq.offer((sumReplace, idx + 1))
              // add the next element additionally
              val sumAdd = curSum + absVals(idx + 1)
              pq.offer((sumAdd, idx + 1))
            }
          }
        }

        answer
    }
}
```

## Rust

```rust
impl Solution {
    pub fn k_sum(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let mut base: i64 = 0;
        let mut abs_vals: Vec<i64> = Vec::with_capacity(n);
        for &x in &nums {
            if x > 0 {
                base += x as i64;
            }
            abs_vals.push((x.abs()) as i64);
        }
        abs_vals.sort(); // ascending

        use std::cmp::Reverse;
        use std::collections::BinaryHeap;

        let mut heap: BinaryHeap<Reverse<(i64, usize)>> = BinaryHeap::new();
        heap.push(Reverse((0_i64, 0_usize)));

        let target = k as usize;
        let mut count = 0usize;
        let mut kth_subset_sum = 0_i64;

        while let Some(Reverse((sum, idx))) = heap.pop() {
            count += 1;
            if count == target {
                kth_subset_sum = sum;
                break;
            }
            if idx < n {
                // include abs_vals[idx]
                heap.push(Reverse((sum + abs_vals[idx], idx + 1)));
                // exclude abs_vals[idx]
                heap.push(Reverse((sum, idx + 1)));
            }
        }

        base - kth_subset_sum
    }
}
```

## Racket

```racket
(require racket/priority-queue)

(define/contract (k-sum nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((base (apply + (filter positive? nums)))
         (abs-list (map abs nums))
         (sorted (sort abs-list <))
         (n (length sorted)))
    (if (= n 0)
        base
        (let ((pq (make-pq (lambda (a b) (< (first a) (first b))))))
          (pq-push! pq (list (list-ref sorted 0) 0))
          (define ans base)
          (let loop ((cnt 1))
            (if (= cnt k)
                ans
                (let* ((node (pq-pop! pq))
                       (s (first node))
                       (i (second node)))
                  (set! ans (- base s))
                  (when (< (+ i 1) n)
                    (define next-idx (+ i 1))
                    (define next-val (list-ref sorted next-idx))
                    (pq-push! pq (list (+ s next-val) next-idx))
                    (pq-push! pq (list (+ (- s (list-ref sorted i)) next-val) next-idx)))
                  (loop (+ cnt 1))))))))))
```

## Erlang

```erlang
-module(solution).
-export([k_sum/2]).

-spec k_sum(Nums :: [integer()], K :: integer()) -> integer().
k_sum(Nums, K) ->
    Base = lists:foldl(fun(X, Acc) -> if X > 0 -> Acc + X; true -> Acc end end, 0, Nums),
    AbsList = [abs(X) || X <- Nums],
    SortedAbs = lists:sort(AbsList),
    AbsArr = array:from_list(SortedAbs),
    N = array:size(AbsArr),
    Heap0 =
        case N of
            0 -> [];
            _ -> [{array:get(0, AbsArr), 0}]
        end,
    Penalties = gen_penalties(K, [0], Heap0, AbsArr, N),
    PenaltyKMinus1 = lists:nth(K, Penalties),
    Base - PenaltyKMinus1.

gen_penalties(K, ResultRev, _Heap, _AbsArr, _N) when length(ResultRev) >= K ->
    lists:reverse(ResultRev);
gen_penalties(K, ResultRev, [], _AbsArr, _N) ->
    lists:reverse(ResultRev);
gen_penalties(K, ResultRev, [{Sum,Idx}|RestHeap], AbsArr, N) ->
    NewResultRev = [Sum | ResultRev],
    NewHeap0 = RestHeap,
    NewHeap =
        if Idx + 1 < N ->
                NextVal = array:get(Idx+1, AbsArr),
                H1 = push_heap(NewHeap0, {Sum + NextVal, Idx+1}),
                PrevVal = array:get(Idx, AbsArr),
                push_heap(H1, {Sum - PrevVal + NextVal, Idx+1});
           true -> NewHeap0
        end,
    gen_penalties(K, NewResultRev, NewHeap, AbsArr, N).

push_heap([], Elem) ->
    [Elem];
push_heap([H|T]=Heap, {S,_}=Elem) ->
    case H of
        {SH,_} when S =< SH -> [Elem | Heap];
        _ -> [H | push_heap(T, Elem)]
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec k_sum(nums :: [integer], k :: integer) :: integer
  def k_sum(nums, k) do
    pos_sum = Enum.reduce(nums, 0, fn x, acc -> if x > 0, do: acc + x, else: acc end)
    abs_vals = Enum.map(nums, &abs/1) |> Enum.sort()
    n = length(abs_vals)

    if k == 1 do
      pos_sum
    else
      first = pos_sum - hd(abs_vals)
      heap = heap_push(:gb_trees.empty(), first, 0)
      go(k, 2, heap, abs_vals, n)
    end
  end

  defp go(k, cnt, heap, abs_vals, n) do
    {cur, idx, new_heap} = heap_pop(heap)

    if cnt == k do
      cur
    else
      new_heap2 =
        if idx + 1 < n do
          a_i = Enum.at(abs_vals, idx)
          a_next = Enum.at(abs_vals, idx + 1)

          heap1 = heap_push(new_heap, cur - a_next, idx + 1)
          heap_push(heap1, cur + a_i - a_next, idx + 1)
        else
          new_heap
        end

      go(k, cnt + 1, new_heap2, abs_vals, n)
    end
  end

  defp heap_push(tree, sum, idx) do
    case :gb_trees.lookup(sum, tree) do
      :none -> :gb_trees.insert(sum, [idx], tree)
      {:value, lst} -> :gb_trees.update(sum, [idx | lst], tree)
    end
  end

  defp heap_pop(tree) do
    {{max_sum, idxs}, rest_tree} = :gb_trees.take_largest(tree)
    [idx | rest] = idxs

    new_tree =
      case rest do
        [] -> rest_tree
        _ -> :gb_trees.insert(max_sum, rest, rest_tree)
      end

    {max_sum, idx, new_tree}
  end
end
```
