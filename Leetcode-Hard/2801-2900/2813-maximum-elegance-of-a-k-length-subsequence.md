# 2813. Maximum Elegance of a K-Length Subsequence

## Cpp

```cpp
class Solution {
public:
    long long findMaximumElegance(std::vector<std::vector<int>>& items, int k) {
        struct Item { long long profit; int cat; };
        std::vector<Item> v;
        v.reserve(items.size());
        for (auto& it : items) v.push_back({it[0], it[1]});
        std::sort(v.begin(), v.end(), [](const Item& a, const Item& b){
            return a.profit > b.profit;
        });
        
        long long sum = 0;
        int distinct = 0;
        std::unordered_map<int,int> cnt;
        std::priority_queue<long long, std::vector<long long>, std::greater<long long>> dupHeap;
        
        for (int i = 0; i < k; ++i) {
            sum += v[i].profit;
            int c = v[i].cat;
            if (++cnt[c] == 1) {
                ++distinct;
            } else {
                dupHeap.push(v[i].profit);
            }
        }
        
        long long best = sum + 1LL * distinct * distinct;
        
        for (int i = k; i < (int)v.size(); ++i) {
            int c = v[i].cat;
            if (cnt[c] == 0 && !dupHeap.empty()) {
                long long removed = dupHeap.top();
                dupHeap.pop();
                sum = sum - removed + v[i].profit;
                cnt[c] = 1;
                ++distinct;
                best = std::max(best, sum + 1LL * distinct * distinct);
            }
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public long findMaximumElegance(int[][] items, int k) {
        java.util.Arrays.sort(items, (a, b) -> Integer.compare(b[0], a[0])); // descending profit
        java.util.Map<Integer, Integer> freq = new java.util.HashMap<>();
        java.util.PriorityQueue<Integer> dupHeap = new java.util.PriorityQueue<>(); // min-heap of duplicate profits
        
        long sum = 0;
        for (int i = 0; i < k; i++) {
            int profit = items[i][0];
            int cat = items[i][1];
            sum += profit;
            int cnt = freq.getOrDefault(cat, 0) + 1;
            freq.put(cat, cnt);
            if (cnt >= 2) {
                dupHeap.offer(profit);
            }
        }
        
        long distinct = freq.size();
        long best = sum + distinct * distinct;
        
        for (int i = k; i < items.length; i++) {
            int profit = items[i][0];
            int cat = items[i][1];
            if (freq.containsKey(cat)) continue; // not a new category
            if (dupHeap.isEmpty()) break; // no duplicate to replace
            
            int removed = dupHeap.poll(); // remove least profitable duplicate
            sum = sum - removed + profit;
            freq.put(cat, 1);
            distinct++;
            
            long elegance = sum + distinct * distinct;
            if (elegance > best) best = elegance;
        }
        
        return best;
    }
}
```

## Python

```python
import heapq

class Solution(object):
    def findMaximumElegance(self, items, k):
        """
        :type items: List[List[int]]
        :type k: int
        :rtype: int
        """
        # Sort items by profit descending
        items.sort(key=lambda x: -x[0])
        
        total_profit = 0
        distinct_cnt = 0
        freq = {}
        dup_heap = []  # min-heap of profits that are duplicates
        
        # Pick first k items
        for i in range(k):
            profit, cat = items[i]
            total_profit += profit
            if cat not in freq:
                freq[cat] = 1
                distinct_cnt += 1
            else:
                freq[cat] += 1
                heapq.heappush(dup_heap, profit)
        
        best = total_profit + distinct_cnt * distinct_cnt
        
        # Try to replace duplicates with new categories from the rest
        for i in range(k, len(items)):
            profit, cat = items[i]
            if cat in freq:
                continue  # already have this category, no benefit in adding it
            if not dup_heap:
                break  # cannot replace any more items
            removed_profit = heapq.heappop(dup_heap)
            total_profit = total_profit - removed_profit + profit
            distinct_cnt += 1
            freq[cat] = 1
            best = max(best, total_profit + distinct_cnt * distinct_cnt)
        
        return best
```

## Python3

```python
from typing import List
import heapq

class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        # Sort items by profit descending
        items.sort(key=lambda x: -x[0])
        
        total = 0
        distinct = 0
        seen = set()
        dup_heap = []  # min-heap of profits that are duplicates in current selection
        
        # Initial selection of first k items
        for i in range(k):
            profit, cat = items[i]
            total += profit
            if cat not in seen:
                seen.add(cat)
                distinct += 1
            else:
                heapq.heappush(dup_heap, profit)
        
        best = total + distinct * distinct
        
        # Try to replace duplicates with new categories from the remaining items
        for i in range(k, len(items)):
            profit, cat = items[i]
            if cat in seen:
                continue  # does not increase distinct categories
            if not dup_heap:
                break  # no duplicate to replace, cannot improve further
            removed = heapq.heappop(dup_heap)
            total = total - removed + profit
            seen.add(cat)
            distinct += 1
            best = max(best, total + distinct * distinct)
        
        return best
```

## C

```c
#include <stdlib.h>

typedef struct {
    int profit;
    int cat;
} Item;

static int cmpDesc(const void *a, const void *b) {
    const Item *ia = (const Item *)a;
    const Item *ib = (const Item *)b;
    return ib->profit - ia->profit;
}

static void heapPush(int *heap, int *size, int val) {
    int i = (*size)++;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (heap[p] <= val) break;
        heap[i] = heap[p];
        i = p;
    }
    heap[i] = val;
}

static int heapPop(int *heap, int *size) {
    int ret = heap[0];
    int val = heap[--(*size)];
    int i = 0;
    while (1) {
        int l = (i << 1) + 1;
        if (l >= *size) break;
        int r = l + 1;
        int child = (r < *size && heap[r] < heap[l]) ? r : l;
        if (heap[child] >= val) break;
        heap[i] = heap[child];
        i = child;
    }
    heap[i] = val;
    return ret;
}

long long findMaximumElegance(int** items, int itemsSize, int* itemsColSize, int k) {
    (void)itemsColSize; // unused
    Item *arr = (Item *)malloc(sizeof(Item) * itemsSize);
    for (int i = 0; i < itemsSize; ++i) {
        arr[i].profit = items[i][0];
        arr[i].cat = items[i][1];
    }
    qsort(arr, itemsSize, sizeof(Item), cmpDesc);

    int maxCat = itemsSize + 5;
    int *cnt = (int *)calloc(maxCat, sizeof(int));

    long long sum = 0;
    int distinct = 0;

    int *heap = (int *)malloc(sizeof(int) * itemsSize);
    int heapSize = 0;

    for (int i = 0; i < k; ++i) {
        sum += arr[i].profit;
        if (cnt[arr[i].cat] == 0) distinct++;
        cnt[arr[i].cat]++;
        if (cnt[arr[i].cat] > 1) {
            heapPush(heap, &heapSize, arr[i].profit);
        }
    }

    long long ans = sum + (long long)distinct * distinct;

    for (int i = k; i < itemsSize && heapSize > 0; ++i) {
        if (cnt[arr[i].cat] > 0) continue; // category already present
        int removed = heapPop(heap, &heapSize);
        sum = sum - removed + arr[i].profit;
        distinct++;
        cnt[arr[i].cat] = 1;
        long long cur = sum + (long long)distinct * distinct;
        if (cur > ans) ans = cur;
    }

    free(arr);
    free(cnt);
    free(heap);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public long FindMaximumElegance(int[][] items, int k) {
        // Sort items by profit descending
        System.Array.Sort(items, (a, b) => b[0].CompareTo(a[0]));
        
        var duplicateHeap = new PriorityQueue<long, long>(); // min-heap of profits that are duplicates
        var seenCategories = new HashSet<int>();
        long sumProfit = 0;
        
        // Take first k items
        for (int i = 0; i < k; i++) {
            int profit = items[i][0];
            int cat = items[i][1];
            sumProfit += profit;
            if (!seenCategories.Add(cat)) {
                duplicateHeap.Enqueue(profit, profit);
            }
        }
        
        long distinct = seenCategories.Count;
        long best = sumProfit + distinct * distinct;
        
        // Try to replace duplicates with new categories
        for (int i = k; i < items.Length; i++) {
            int profit = items[i][0];
            int cat = items[i][1];
            
            if (seenCategories.Contains(cat)) continue; // not a new category
            
            if (duplicateHeap.Count == 0) break; // no duplicate to replace
            
            long removedProfit = duplicateHeap.Dequeue();
            sumProfit = sumProfit - removedProfit + profit;
            seenCategories.Add(cat);
            distinct++;
            
            long elegance = sumProfit + distinct * distinct;
            if (elegance > best) best = elegance;
        }
        
        return best;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} items
 * @param {number} k
 * @return {number}
 */
var findMaximumElegance = function(items, k) {
    // sort by profit descending
    items.sort((a, b) => b[0] - a[0]);

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

    const freq = new Map();
    let sum = 0;
    let distinct = 0;
    const dupHeap = new MinHeap();

    // initial selection of first k items
    for (let i = 0; i < k; ++i) {
        const [profit, cat] = items[i];
        sum += profit;
        if (!freq.has(cat)) {
            freq.set(cat, 1);
            distinct++;
        } else {
            freq.set(cat, freq.get(cat) + 1);
            dupHeap.push(profit); // duplicate profit can be swapped out later
        }
    }

    let best = sum + distinct * distinct;

    // try to replace duplicates with new categories
    for (let i = k; i < items.length; ++i) {
        const [profit, cat] = items[i];
        if (freq.has(cat)) continue; // already have this category
        if (dupHeap.size() === 0) break; // no duplicate to replace

        const removedProfit = dupHeap.pop();
        sum = sum - removedProfit + profit;
        distinct += 1;
        freq.set(cat, 1);
        best = Math.max(best, sum + distinct * distinct);
    }

    return best;
};
```

## Typescript

```typescript
function findMaximumElegance(items: number[][], k: number): number {
    // sort items by profit descending
    items.sort((a, b) => b[0] - a[0]);

    const freq = new Map<number, number>();
    const dupHeap = new MinHeap();
    let sum = 0;

    for (let i = 0; i < k; ++i) {
        const [p, c] = items[i];
        sum += p;
        const cnt = (freq.get(c) ?? 0);
        freq.set(c, cnt + 1);
        if (cnt >= 1) { // this item is a duplicate of its category
            dupHeap.push(p);
        }
    }

    let distinct = freq.size;
    let best = sum + distinct * distinct;

    for (let i = k; i < items.length; ++i) {
        const [p, c] = items[i];
        if (freq.has(c)) continue; // category already present
        if (dupHeap.size() === 0) break; // no duplicate to replace

        const removed = dupHeap.pop()!;
        sum = sum - removed + p;
        freq.set(c, 1);
        distinct++;
        best = Math.max(best, sum + distinct * distinct);
    }

    return best;
}

class MinHeap {
    private heap: number[] = [];

    size(): number {
        return this.heap.length;
    }

    push(val: number): void {
        this.heap.push(val);
        this.bubbleUp(this.heap.length - 1);
    }

    pop(): number | undefined {
        if (this.heap.length === 0) return undefined;
        const top = this.heap[0];
        const end = this.heap.pop()!;
        if (this.heap.length > 0) {
            this.heap[0] = end;
            this.sinkDown(0);
        }
        return top;
    }

    private bubbleUp(idx: number): void {
        const element = this.heap[idx];
        while (idx > 0) {
            const parentIdx = Math.floor((idx - 1) / 2);
            const parent = this.heap[parentIdx];
            if (element >= parent) break;
            this.heap[parentIdx] = element;
            this.heap[idx] = parent;
            idx = parentIdx;
        }
    }

    private sinkDown(idx: number): void {
        const length = this.heap.length;
        const element = this.heap[idx];
        while (true) {
            let leftIdx = 2 * idx + 1;
            let rightIdx = 2 * idx + 2;
            let swapIdx = -1;

            if (leftIdx < length && this.heap[leftIdx] < element) {
                swapIdx = leftIdx;
            }
            if (rightIdx < length) {
                if (
                    (swapIdx === -1 && this.heap[rightIdx] < element) ||
                    (swapIdx !== -1 && this.heap[rightIdx] < this.heap[swapIdx])
                ) {
                    swapIdx = rightIdx;
                }
            }

            if (swapIdx === -1) break;

            this.heap[idx] = this.heap[swapIdx];
            this.heap[swapIdx] = element;
            idx = swapIdx;
        }
    }
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $items
     * @param Integer $k
     * @return Integer
     */
    function findMaximumElegance($items, $k) {
        // Sort items by profit descending
        usort($items, function($a, $b) {
            return $b[0] <=> $a[0];
        });

        $n = count($items);
        $sum = 0;
        $cnt = [];               // category => frequency in current selection
        $heap = new SplMinHeap(); // profits of removable duplicate items

        // Initial selection: first k items
        for ($i = 0; $i < $k; ++$i) {
            $profit   = $items[$i][0];
            $category = $items[$i][1];

            $sum += $profit;
            if (!isset($cnt[$category])) {
                $cnt[$category] = 0;
            }
            $cnt[$category]++;

            // If this category appears more than once, this item can be removed later
            if ($cnt[$category] > 1) {
                $heap->insert($profit);
            }
        }

        $distinct = count($cnt);
        $maxElegance = $sum + $distinct * $distinct;

        // Try to replace duplicates with items of new categories
        for ($i = $k; $i < $n; ++$i) {
            $profit   = $items[$i][0];
            $category = $items[$i][1];

            // Skip if category already present
            if (isset($cnt[$category])) {
                continue;
            }

            // No duplicate to replace -> cannot increase distinct count further
            if ($heap->isEmpty()) {
                break;
            }

            // Replace the smallest-profit duplicate with this new-category item
            $removedProfit = $heap->extract();
            $sum = $sum - $removedProfit + $profit;

            $cnt[$category] = 1;   // add new category
            $distinct++;

            $currentElegance = $sum + $distinct * $distinct;
            if ($currentElegance > $maxElegance) {
                $maxElegance = $currentElegance;
            }
        }

        return $maxElegance;
    }
}
```

## Swift

```swift
class MinHeap {
    private var data: [Int] = []
    
    var isEmpty: Bool { data.isEmpty }
    
    func push(_ value: Int) {
        data.append(value)
        siftUp(data.count - 1)
    }
    
    func pop() -> Int? {
        guard !data.isEmpty else { return nil }
        let result = data[0]
        let last = data.removeLast()
        if !data.isEmpty {
            data[0] = last
            siftDown(0)
        }
        return result
    }
    
    private func siftUp(_ index: Int) {
        var child = index
        while child > 0 {
            let parent = (child - 1) >> 1
            if data[parent] <= data[child] { break }
            data.swapAt(parent, child)
            child = parent
        }
    }
    
    private func siftDown(_ index: Int) {
        var parent = index
        while true {
            let left = parent * 2 + 1
            let right = left + 1
            var smallest = parent
            if left < data.count && data[left] < data[smallest] { smallest = left }
            if right < data.count && data[right] < data[smallest] { smallest = right }
            if smallest == parent { break }
            data.swapAt(parent, smallest)
            parent = smallest
        }
    }
}

class Solution {
    func findMaximumElegance(_ items: [[Int]], _ k: Int) -> Int {
        let sortedItems = items.sorted { $0[0] > $1[0] }   // descending by profit
        
        var categoryCount = [Int:Int]()
        var sumProfit: Int64 = 0
        var heap = MinHeap()
        
        // initial selection of first k items
        for i in 0..<k {
            let profit = sortedItems[i][0]
            let cat = sortedItems[i][1]
            sumProfit += Int64(profit)
            categoryCount[cat, default: 0] += 1
            if categoryCount[cat]! > 1 {
                heap.push(profit)   // duplicate profit eligible for removal
            }
        }
        
        var distinct = categoryCount.count
        var best = sumProfit + Int64(distinct * distinct)
        
        // try to replace duplicates with new categories
        if k < sortedItems.count {
            for i in k..<sortedItems.count {
                let profit = sortedItems[i][0]
                let cat = sortedItems[i][1]
                
                // skip if category already present
                if categoryCount[cat] != nil { continue }
                // need a duplicate to replace
                guard !heap.isEmpty else { break }
                
                // perform replacement
                if let removedProfit = heap.pop() {
                    sumProfit = sumProfit - Int64(removedProfit) + Int64(profit)
                    distinct += 1
                    categoryCount[cat] = 1
                    best = max(best, sumProfit + Int64(distinct * distinct))
                }
            }
        }
        
        return Int(best)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findMaximumElegance(items: Array<IntArray>, k: Int): Long {
        val n = items.size
        val sorted = items.sortedWith(compareByDescending<IntArray> { it[0] })
        val cnt = IntArray(n + 2)
        var sum = 0L
        var distinct = 0
        val dupHeap = java.util.PriorityQueue<Pair<Long, Int>>(compareBy { it.first })

        for (i in 0 until k) {
            val profit = sorted[i][0].toLong()
            val cat = sorted[i][1]
            sum += profit
            if (cnt[cat] == 0) distinct++
            cnt[cat]++
            if (cnt[cat] > 1) {
                dupHeap.add(Pair(profit, cat))
            }
        }

        var maxElegance = sum + distinct.toLong() * distinct

        for (i in k until n) {
            val profit = sorted[i][0].toLong()
            val cat = sorted[i][1]
            if (cnt[cat] == 0 && dupHeap.isNotEmpty()) {
                val removed = dupHeap.poll()
                val removedProfit = removed.first
                val removedCat = removed.second

                sum = sum - removedProfit + profit
                cnt[removedCat]--
                cnt[cat] = 1
                distinct++

                val current = sum + distinct.toLong() * distinct
                if (current > maxElegance) {
                    maxElegance = current
                }
            }
        }

        return maxElegance
    }
}
```

## Dart

```dart
class Solution {
  int findMaximumElegance(List<List<int>> items, int k) {
    // Sort items by profit descending
    items.sort((a, b) => b[0].compareTo(a[0]));

    Map<int, int> catCount = {};
    List<int> duplicateProfits = [];
    int totalProfit = 0;

    // Select first k items
    for (int i = 0; i < k; i++) {
      int profit = items[i][0];
      int category = items[i][1];
      totalProfit += profit;
      catCount[category] = (catCount[category] ?? 0) + 1;
      if (catCount[category]! > 1) {
        duplicateProfits.add(profit);
      }
    }

    // Sort duplicate profits ascending to remove smallest first
    duplicateProfits.sort();
    int distinct = catCount.length;
    int maxElegance = totalProfit + distinct * distinct;

    int dupIdx = 0; // pointer to next removable duplicate profit

    // Try to replace duplicates with new categories from the remaining items
    for (int i = k; i < items.length; i++) {
      int profit = items[i][0];
      int category = items[i][1];

      if (catCount.containsKey(category)) continue; // not a new category

      if (dupIdx >= duplicateProfits.length) break; // no duplicates left to replace

      int removedProfit = duplicateProfits[dupIdx];
      dupIdx++;

      totalProfit = totalProfit - removedProfit + profit;
      distinct += 1;
      catCount[category] = 1;

      int elegance = totalProfit + distinct * distinct;
      if (elegance > maxElegance) {
        maxElegance = elegance;
      }
    }

    return maxElegance;
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

type dupItem struct {
	profit   int
	category int
}

type minHeap []dupItem

func (h minHeap) Len() int            { return len(h) }
func (h minHeap) Less(i, j int) bool  { return h[i].profit < h[j].profit }
func (h minHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *minHeap) Push(x interface{}) { *h = append(*h, x.(dupItem)) }
func (h *minHeap) Pop() interface{} {
	old := *h
	n := len(old)
	it := old[n-1]
	*h = old[:n-1]
	return it
}

func findMaximumElegance(items [][]int, k int) int64 {
	// sort by profit descending
	sort.Slice(items, func(i, j int) bool {
		return items[i][0] > items[j][0]
	})

	catCount := make(map[int]int)
	var sum int64
	distinct := 0

	h := &minHeap{}
	heap.Init(h)

	// initial selection of first k items
	for i := 0; i < k; i++ {
		p := items[i][0]
		c := items[i][1]
		sum += int64(p)
		if catCount[c] == 0 {
			distinct++
		}
		catCount[c]++
		if catCount[c] >= 2 {
			heap.Push(h, dupItem{profit: p, category: c})
		}
	}

	best := sum + int64(distinct)*int64(distinct)

	// try to replace duplicates with new categories
	for i := k; i < len(items); i++ {
		p := items[i][0]
		c := items[i][1]

		if catCount[c] > 0 { // already have this category, skip
			continue
		}
		if h.Len() == 0 {
			break // no duplicate to replace
		}
		// remove the smallest profit duplicate
		rem := heap.Pop(h).(dupItem)
		sum = sum - int64(rem.profit) + int64(p)

		// update counts
		catCount[rem.category]--
		catCount[c] = 1
		distinct++

		// compute elegance
		current := sum + int64(distinct)*int64(distinct)
		if current > best {
			best = current
		}
	}

	return best
}
```

## Ruby

```ruby
class MinHeap
  def initialize
    @data = []
  end

  def push(val)
    i = @data.size
    @data << val
    while i > 0
      parent = (i - 1) / 2
      break if @data[parent] <= @data[i]
      @data[parent], @data[i] = @data[i], @data[parent]
      i = parent
    end
  end

  def pop
    return nil if @data.empty?
    min = @data[0]
    last = @data.pop
    unless @data.empty?
      @data[0] = last
      i = 0
      size = @data.size
      loop do
        left = i * 2 + 1
        right = left + 1
        smallest = i
        smallest = left if left < size && @data[left] < @data[smallest]
        smallest = right if right < size && @data[right] < @data[smallest]
        break if smallest == i
        @data[i], @data[smallest] = @data[smallest], @data[i]
        i = smallest
      end
    end
    min
  end

  def empty?
    @data.empty?
  end
end

# @param {Integer[][]} items
# @param {Integer} k
# @return {Integer}
def find_maximum_elegance(items, k)
  items.sort_by! { |p, _c| -p }
  heap = MinHeap.new
  freq = Hash.new(0)
  sum = 0

  (0...k).each do |i|
    p, c = items[i]
    heap.push(p) if freq[c] > 0
    freq[c] += 1
    sum += p
  end

  distinct = freq.size
  max_elegance = sum + distinct * distinct

  (k...items.length).each do |i|
    p, c = items[i]
    next if freq.key?(c)
    break if heap.empty?
    removed = heap.pop
    sum = sum - removed + p
    freq[c] = 1
    distinct += 1
    current = sum + distinct * distinct
    max_elegance = current if current > max_elegance
  end

  max_elegance
end
```

## Scala

```scala
object Solution {
  def findMaximumElegance(items: Array[Array[Int]], k: Int): Long = {
    import java.util.PriorityQueue

    val sorted = items.map { arr => (arr(0).toLong, arr(1)) }
      .sortBy(item => -item._1)

    var sum: Long = 0L
    val seen = scala.collection.mutable.HashSet[Int]()
    val dupHeap = new PriorityQueue[Long]() // min-heap for duplicate profits

    for (i <- 0 until k) {
      val (p, c) = sorted(i)
      sum += p
      if (seen.contains(c)) {
        dupHeap.offer(p)
      } else {
        seen.add(c)
      }
    }

    var distinct = seen.size
    var ans: Long = sum + distinct.toLong * distinct

    for (i <- k until items.length) {
      val (p, c) = sorted(i)
      if (!seen.contains(c) && !dupHeap.isEmpty) {
        val removed = dupHeap.poll()
        sum = sum - removed + p
        seen.add(c)
        distinct += 1
        ans = math.max(ans, sum + distinct.toLong * distinct)
      }
    }

    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn find_maximum_elegance(items: Vec<Vec<i32>>, k: i32) -> i64 {
        use std::collections::{HashMap, BinaryHeap};
        use std::cmp::Reverse;

        let mut v: Vec<(i64, i32)> = items
            .into_iter()
            .map(|it| (it[0] as i64, it[1]))
            .collect();
        v.sort_by(|a, b| b.0.cmp(&a.0)); // descending profit

        let k_usize = k as usize;
        let n = v.len();

        let mut freq: HashMap<i32, i32> = HashMap::new();
        let mut dup_heap: BinaryHeap<Reverse<i64>> = BinaryHeap::new();
        let mut sum: i64 = 0;

        for i in 0..k_usize {
            let (p, c) = v[i];
            sum += p;
            let cnt = freq.entry(c).or_insert(0);
            *cnt += 1;
            if *cnt > 1 {
                dup_heap.push(Reverse(p));
            }
        }

        let mut distinct = freq.len() as i64;
        let mut best = sum + distinct * distinct;

        for i in k_usize..n {
            let (p, c) = v[i];
            if freq.contains_key(&c) {
                continue; // category already present
            }
            if let Some(Reverse(rem)) = dup_heap.pop() {
                // replace a duplicate with this new category item
                sum = sum - rem + p;
                distinct += 1;
                freq.insert(c, 1);
                let cur = sum + distinct * distinct;
                if cur > best {
                    best = cur;
                }
            } else {
                break; // no more duplicates to replace
            }
        }

        best
    }
}
```

## Racket

```racket
(require racket/list)
(require racket/hash)

(define/contract (find-maximum-elegance items k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ((sorted-items (sort items
                             (lambda (a b) (> (first a) (first b)))))
         (selected (take sorted-items k))
         (remaining (drop sorted-items k))
         (ht (make-hash))
         (sum-profit
           (for/fold ([s 0]) ([it selected])
             (let* ((p (first it))
                    (c (second it)))
               (hash-set! ht c (+ 1 (hash-ref ht c 0)))
               (+ s p))))
         (distinct (hash-count ht))
         (dup-list
           (let ((lst '()))
             (for ([it selected])
               (define cat (second it))
               (when (> (hash-ref ht cat) 1)
                 (set! lst (cons (first it) lst))))
             (sort lst <))) ; ascending profits of duplicates
         (dup-vec (list->vector dup-list))
         (dup-count (vector-length dup-vec))
         (max-elegance (+ sum-profit (* distinct distinct))))
    (let loop ((rem remaining)
               (sum sum-profit)
               (dist distinct)
               (idx 0)
               (best max-elegance))
      (if (null? rem)
          best
          (let* ((item (car rem))
                 (p (first item))
                 (c (second item)))
            (if (or (hash-has-key? ht c) (>= idx dup-count))
                (loop (cdr rem) sum dist idx best)
                (let* ((removed (vector-ref dup-vec idx))
                       (new-sum (+ (- sum removed) p))
                       (new-dist (+ dist 1)))
                  (hash-set! ht c 1)
                  (define new-best (max best (+ new-sum (* new-dist new-dist))))
                  (loop (cdr rem) new-sum new-dist (+ idx 1) new-best))))))))
```

## Erlang

```erlang
-module(solution).
-export([find_maximum_elegance/2]).

-spec find_maximum_elegance(Items :: [[integer()]], K :: integer()) -> integer().
find_maximum_elegance(Items, K) ->
    Sorted = lists:sort(fun(A, B) -> element(1, A) > element(1, B) end, Items),
    {FirstK, Rest} = lists:split(K, Sorted),
    {Total0, Distinct0, CatMap0, RemovableSorted} = init_selection(FirstK),
    Best0 = Total0 + Distinct0 * Distinct0,
    loop(Rest, Total0, Distinct0, CatMap0, RemovableSorted, Best0).

init_selection(Selected) ->
    {Total, CatMap} =
        lists:foldl(
            fun([P, C], {AccT, AccM}) ->
                NewT = AccT + P,
                Count = maps:get(C, AccM, 0),
                NewM = maps:put(C, Count + 1, AccM),
                {NewT, NewM}
            end,
            {0, #{}},
            Selected
        ),
    Distinct = map_size(CatMap),
    Removable = collect_removables(Selected, #{}, []),
    RemovableSorted = lists:sort(Removable), % ascending order
    {Total, Distinct, CatMap, RemovableSorted}.

collect_removables([], _Seen, Acc) ->
    Acc;
collect_removables([[P, C] | Rest], Seen, Acc) ->
    CountSeen = maps:get(C, Seen, 0),
    NewAcc = if CountSeen >= 1 -> [P | Acc]; true -> Acc end,
    NewSeen = maps:put(C, CountSeen + 1, Seen),
    collect_removables(Rest, NewSeen, NewAcc).

loop([], _Total, _Distinct, _CatMap, _Removables, Best) ->
    Best;
loop([[P, C] | Rest], Total, Distinct, CatMap, Removables, Best) ->
    case maps:is_key(C, CatMap) of
        true ->
            loop(Rest, Total, Distinct, CatMap, Removables, Best);
        false ->
            case Removables of
                [] -> Best;
                [MinRem | Tail] ->
                    NewTotal = Total - MinRem + P,
                    NewDistinct = Distinct + 1,
                    NewCatMap = maps:put(C, 1, CatMap),
                    NewBest = erlang:max(Best, NewTotal + NewDistinct * NewDistinct),
                    loop(Rest, NewTotal, NewDistinct, NewCatMap, Tail, NewBest)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_maximum_elegance(items :: [[integer]], k :: integer) :: integer
  def find_maximum_elegance(items, k) do
    # Sort items by profit descending
    sorted = Enum.sort_by(items, fn [p, _c] -> -p end)

    {first_k, rest} = Enum.split(sorted, k)

    total_profit =
      Enum.reduce(first_k, 0, fn [p, _c], acc -> acc + p end)

    # Count categories in the first k items
    counts =
      Enum.reduce(first_k, %{}, fn [_p, c], acc ->
        Map.update(acc, c, 1, &(&1 + 1))
      end)

    distinct = map_size(counts)

    # Collect profits of duplicate-category items (removable candidates)
    dup_profits =
      first_k
      |> Enum.filter(fn [_p, c] -> counts[c] > 1 end)
      |> Enum.map(fn [p, _c] -> p end)
      |> Enum.sort()   # ascending, smallest first

    # Set of categories already selected
    cat_set = Map.keys(counts) |> MapSet.new()

    initial_elegance = total_profit + distinct * distinct
    process(rest, dup_profits, total_profit, distinct, initial_elegance, cat_set)
  end

  defp process(_rest, [], _total, _distinct, ans, _set), do: ans

  defp process([], _dup, _total, _distinct, ans, _set), do: ans

  defp process([[profit, cat] | tail], dup, total, distinct, ans, set) do
    cond do
      MapSet.member?(set, cat) ->
        # Category already present, cannot increase distinct count
        process(tail, dup, total, distinct, ans, set)

      true ->
        # Use the smallest removable duplicate profit to replace
        [smallest | rest_dup] = dup
        new_total = total - smallest + profit
        new_distinct = distinct + 1
        new_ans = max(ans, new_total + new_distinct * new_distinct)
        new_set = MapSet.put(set, cat)
        process(tail, rest_dup, new_total, new_distinct, new_ans, new_set)
    end
  end
end
```
