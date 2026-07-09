# 2931. Maximum Spending After Buying Items

## Cpp

```cpp
class Solution {
public:
    long long maxSpending(vector<vector<int>>& values) {
        struct Node {
            int val;
            int shop;
            int idx;
        };
        auto cmp = [](const Node& a, const Node& b){ return a.val > b.val; };
        priority_queue<Node, vector<Node>, decltype(cmp)> pq(cmp);
        
        for (int i = 0; i < (int)values.size(); ++i) {
            int idx = (int)values[i].size() - 1;
            if (idx >= 0) {
                pq.push({values[i][idx], i, idx});
            }
        }
        
        long long total = 0;
        long long day = 1;
        while (!pq.empty()) {
            Node cur = pq.top(); pq.pop();
            total += (long long)cur.val * day;
            ++day;
            if (cur.idx > 0) {
                int newIdx = cur.idx - 1;
                pq.push({values[cur.shop][newIdx], cur.shop, newIdx});
            }
        }
        return total;
    }
};
```

## Java

```java
class Solution {
    private static class Node {
        int shop;
        int idx; // current index of the smallest remaining item in this shop
        int val;
        Node(int shop, int idx, int val) {
            this.shop = shop;
            this.idx = idx;
            this.val = val;
        }
    }

    public long maxSpending(int[][] values) {
        int m = values.length;
        int n = values[0].length;
        PriorityQueue<Node> pq = new PriorityQueue<>((a, b) -> Integer.compare(a.val, b.val));
        for (int i = 0; i < m; i++) {
            int idx = n - 1;
            pq.offer(new Node(i, idx, values[i][idx]));
        }

        long total = 0L;
        int day = 1;
        while (!pq.isEmpty()) {
            Node cur = pq.poll();
            total += (long) cur.val * day;
            day++;
            if (cur.idx > 0) {
                int newIdx = cur.idx - 1;
                pq.offer(new Node(cur.shop, newIdx, values[cur.shop][newIdx]));
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
    def maxSpending(self, values):
        """
        :type values: List[List[int]]
        :rtype: int
        """
        m = len(values)
        # pointers to the last (smallest) unbought item in each shop
        idx = [len(row) - 1 for row in values]
        heap = []
        for i in range(m):
            if idx[i] >= 0:
                heapq.heappush(heap, (values[i][idx[i]], i))
        day = 1
        total = 0
        while heap:
            val, shop = heapq.heappop(heap)
            total += val * day
            day += 1
            idx[shop] -= 1
            if idx[shop] >= 0:
                heapq.heappush(heap, (values[shop][idx[shop]], shop))
        return total
```

## Python3

```python
import heapq
from typing import List

class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        m = len(values)
        n = len(values[0]) if m else 0
        heap = []
        for i in range(m):
            # push the smallest (last) element of each shop
            heap.append((values[i][n - 1], i, n - 1))
        heapq.heapify(heap)

        total = 0
        day = 1
        while heap:
            val, shop, idx = heapq.heappop(heap)
            total += val * day
            day += 1
            if idx > 0:
                new_idx = idx - 1
                heapq.heappush(heap, (values[shop][new_idx], shop, new_idx))
        return total
```

## C

```c
#include <limits.h>
#include <stdlib.h>

long long maxSpending(int** values, int valuesSize, int* valuesColSize) {
    int m = valuesSize;
    if (m == 0) return 0LL;

    int *idx = (int *)malloc(m * sizeof(int));
    for (int i = 0; i < m; ++i) {
        idx[i] = valuesColSize[i] - 1;   // point to the smallest remaining item in each shop
    }

    long long ans = 0;
    int totalItems = 0;
    for (int i = 0; i < m; ++i) totalItems += valuesColSize[i];

    for (int day = 1; day <= totalItems; ++day) {
        int minVal = INT_MAX;
        int shop = -1;
        for (int i = 0; i < m; ++i) {
            if (idx[i] >= 0 && values[i][idx[i]] < minVal) {
                minVal = values[i][idx[i]];
                shop = i;
            }
        }
        ans += (long long)minVal * day;
        idx[shop]--;
    }

    free(idx);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public long MaxSpending(int[][] values) {
        int m = values.Length;
        var pq = new PriorityQueue<(int val, int shop, int idx), int>();
        for (int i = 0; i < m; i++) {
            int idx = values[i].Length - 1;
            int v = values[i][idx];
            pq.Enqueue((v, i, idx), v);
        }
        long total = 0;
        int day = 1;
        while (pq.Count > 0) {
            var cur = pq.Dequeue();
            long v = cur.val;
            total += v * day;
            day++;
            int shop = cur.shop;
            int nextIdx = cur.idx - 1;
            if (nextIdx >= 0) {
                int nextVal = values[shop][nextIdx];
                pq.Enqueue((nextVal, shop, nextIdx), nextVal);
            }
        }
        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} values
 * @return {number}
 */
var maxSpending = function(values) {
    class MinHeap {
        constructor() { this.heap = []; }
        size() { return this.heap.length; }
        push(node) {
            const h = this.heap;
            h.push(node);
            let i = h.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (h[p].val <= h[i].val) break;
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
                    let l = i * 2 + 1,
                        r = l + 1,
                        smallest = i;
                    if (l < h.length && h[l].val < h[smallest].val) smallest = l;
                    if (r < h.length && h[r].val < h[smallest].val) smallest = r;
                    if (smallest === i) break;
                    [h[i], h[smallest]] = [h[smallest], h[i]];
                    i = smallest;
                }
            }
            return top;
        }
    }

    const m = values.length;
    const idx = new Array(m);
    const heap = new MinHeap();
    let totalItems = 0;

    for (let i = 0; i < m; ++i) {
        const len = values[i].length;
        totalItems += len;
        idx[i] = len - 1;
        if (len > 0) {
            heap.push({ val: values[i][idx[i]], shop: i });
        }
    }

    let day = 1;
    let ans = 0;

    while (heap.size() > 0) {
        const node = heap.pop();
        ans += node.val * day;
        const s = node.shop;
        idx[s]--;
        if (idx[s] >= 0) {
            heap.push({ val: values[s][idx[s]], shop: s });
        }
        day++;
    }

    return ans;
};
```

## Typescript

```typescript
function maxSpending(values: number[][]): number {
    const m = values.length;
    const n = values[0].length;

    // pointer to the current smallest (last) element index for each shop
    const ptr = new Array(m);
    for (let i = 0; i < m; i++) ptr[i] = n - 1;

    class MinHeap {
        private heap: { val: number; shop: number }[] = [];

        push(node: { val: number; shop: number }): void {
            const h = this.heap;
            h.push(node);
            let i = h.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (h[p].val <= h[i].val) break;
                [h[p], h[i]] = [h[i], h[p]];
                i = p;
            }
        }

        pop(): { val: number; shop: number } | undefined {
            const h = this.heap;
            if (h.length === 0) return undefined;
            const top = h[0];
            const last = h.pop()!;
            if (h.length > 0) {
                h[0] = last;
                let i = 0;
                while (true) {
                    let l = i * 2 + 1,
                        r = l + 1,
                        smallest = i;
                    if (l < h.length && h[l].val < h[smallest].val) smallest = l;
                    if (r < h.length && h[r].val < h[smallest].val) smallest = r;
                    if (smallest === i) break;
                    [h[i], h[smallest]] = [h[smallest], h[i]];
                    i = smallest;
                }
            }
            return top;
        }
    }

    const heap = new MinHeap();
    // initialize heap with the smallest item from each shop
    for (let i = 0; i < m; i++) {
        heap.push({ val: values[i][ptr[i]], shop: i });
        ptr[i]--;
    }

    let total = 0;
    const totalItems = m * n;

    for (let day = 1; day <= totalItems; day++) {
        const node = heap.pop()!;
        total += node.val * day;
        const s = node.shop;
        if (ptr[s] >= 0) {
            heap.push({ val: values[s][ptr[s]], shop: s });
            ptr[s]--;
        }
    }

    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $values
     * @return Integer
     */
    function maxSpending($values) {
        $m = count($values);
        // pointers to the current last index for each shop
        $ptr = [];
        foreach ($values as $i => $arr) {
            $ptr[$i] = count($arr) - 1;
        }

        // min-heap using SplPriorityQueue (store negative priority)
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);

        foreach ($values as $i => $arr) {
            if (!empty($arr)) {
                $val = $arr[$ptr[$i]];
                $pq->insert([$i, $val], -$val);
            }
        }

        $total = 0;
        $day = 1;

        while (!$pq->isEmpty()) {
            [$shop, $value] = $pq->extract();
            $total += $value * $day;
            $day++;

            $ptr[$shop]--;
            if ($ptr[$shop] >= 0) {
                $newVal = $values[$shop][$ptr[$shop]];
                $pq->insert([$shop, $newVal], -$newVal);
            }
        }

        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func maxSpending(_ values: [[Int]]) -> Int {
        struct HeapNode {
            var val: Int
            var shop: Int
        }
        struct MinHeap {
            private var data = [HeapNode]()
            var isEmpty: Bool { data.isEmpty }
            mutating func push(_ node: HeapNode) {
                data.append(node)
                siftUp(data.count - 1)
            }
            mutating func pop() -> HeapNode {
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

        let m = values.count
        var idx = Array(repeating: -1, count: m)   // current last index for each shop
        var heap = MinHeap()
        for i in 0..<m {
            let n = values[i].count
            if n > 0 {
                idx[i] = n - 1
                heap.push(HeapNode(val: values[i][idx[i]], shop: i))
            }
        }

        var day = 1
        var total: Int64 = 0
        while !heap.isEmpty {
            let node = heap.pop()
            total += Int64(node.val) * Int64(day)
            idx[node.shop] -= 1
            if idx[node.shop] >= 0 {
                heap.push(HeapNode(val: values[node.shop][idx[node.shop]], shop: node.shop))
            }
            day += 1
        }
        return Int(total)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxSpending(values: Array<IntArray>): Long {
        val m = values.size
        if (m == 0) return 0L
        val n = values[0].size
        val idx = IntArray(m) { n - 1 }

        data class Node(val value: Int, val shop: Int)

        val pq = java.util.PriorityQueue<Node>(compareBy { it.value })
        for (i in 0 until m) {
            pq.add(Node(values[i][idx[i]], i))
        }

        var day = 1L
        var total = 0L

        while (pq.isNotEmpty()) {
            val cur = pq.poll()
            total += cur.value.toLong() * day
            idx[cur.shop]--
            if (idx[cur.shop] >= 0) {
                pq.add(Node(values[cur.shop][idx[cur.shop]], cur.shop))
            }
            day++
        }

        return total
    }
}
```

## Dart

```dart
class Solution {
  int maxSpending(List<List<int>> values) {
    int m = values.length;
    List<int> pos = List.filled(m, -1);
    int total = 0;
    for (int i = 0; i < m; ++i) {
      pos[i] = values[i].length - 1;
      total += values[i].length;
    }

    int day = 1;
    int ans = 0;

    while (day <= total) {
      int minVal = 1 << 60;
      int minIdx = -1;
      for (int i = 0; i < m; ++i) {
        if (pos[i] >= 0) {
          int v = values[i][pos[i]];
          if (v < minVal) {
            minVal = v;
            minIdx = i;
          }
        }
      }
      ans += minVal * day;
      pos[minIdx]--;
      day++;
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

type item struct {
	val  int
	shop int
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

func maxSpending(values [][]int) int64 {
	m := len(values)
	if m == 0 {
		return 0
	}
	n := len(values[0])
	totalItems := m * n

	// current index of smallest remaining item for each shop
	idx := make([]int, m)
	h := &minHeap{}
	for i := 0; i < m; i++ {
		idx[i] = len(values[i]) - 1
		if idx[i] >= 0 {
			heap.Push(h, item{val: values[i][idx[i]], shop: i})
			idx[i]--
		}
	}

	var result int64
	for day := 1; day <= totalItems; day++ {
		it := heap.Pop(h).(item)
		result += int64(it.val) * int64(day)

		s := it.shop
		if idx[s] >= 0 {
			heap.Push(h, item{val: values[s][idx[s]], shop: s})
			idx[s]--
		}
	}

	return result
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
    i = @data.size - 1
    while i > 0
      p = (i - 1) / 2
      break if @data[p][0] <= @data[i][0]
      @data[i], @data[p] = @data[p], @data[i]
      i = p
    end
  end

  def pop
    top = @data[0]
    last = @data.pop
    unless @data.empty?
      @data[0] = last
      i = 0
      size = @data.size
      loop do
        l = i * 2 + 1
        r = i * 2 + 2
        smallest = i
        smallest = l if l < size && @data[l][0] < @data[smallest][0]
        smallest = r if r < size && @data[r][0] < @data[smallest][0]
        break if smallest == i
        @data[i], @data[smallest] = @data[smallest], @data[i]
        i = smallest
      end
    end
    top
  end

  def empty?
    @data.empty?
  end
end

def max_spending(values)
  m = values.size
  heap = MinHeap.new
  idx = Array.new(m)

  m.times do |i|
    idx[i] = values[i].length - 1
    heap.push([values[i][idx[i]], i])
  end

  total = 0
  day = 1
  until heap.empty?
    val, shop = heap.pop
    total += val * day
    idx[shop] -= 1
    if idx[shop] >= 0
      heap.push([values[shop][idx[shop]], shop])
    end
    day += 1
  end

  total
end
```

## Scala

```scala
object Solution {
    def maxSpending(values: Array[Array[Int]]): Long = {
        val m = values.length
        if (m == 0) return 0L
        val n = values(0).length
        val idx = Array.fill(m)(n - 1)

        import java.util.PriorityQueue

        val pq = new PriorityQueue[(Int, Int)](
            (a: (Int, Int), b: (Int, Int)) => Integer.compare(a._1, b._1)
        )

        for (i <- 0 until m) {
            if (idx(i) >= 0) {
                pq.offer((values(i)(idx(i)), i))
            }
        }

        var day = 1L
        var total: Long = 0L

        while (!pq.isEmpty) {
            val (v, shop) = pq.poll()
            total += v.toLong * day
            idx(shop) -= 1
            if (idx(shop) >= 0) {
                pq.offer((values(shop)(idx(shop)), shop))
            }
            day += 1
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
    pub fn max_spending(values: Vec<Vec<i32>>) -> i64 {
        let m = values.len();
        if m == 0 {
            return 0;
        }
        // total number of items
        let total_items = values.iter().map(|row| row.len()).sum::<usize>() as i64;

        // current index (pointing to the smallest remaining item) for each shop
        let mut idx: Vec<usize> = vec![0; m];
        let mut heap: BinaryHeap<Reverse<(i32, usize)>> = BinaryHeap::new();

        for i in 0..m {
            if !values[i].is_empty() {
                let last = values[i].len() - 1;
                idx[i] = last;
                heap.push(Reverse((values[i][last], i)));
            }
        }

        let mut ans: i64 = 0;
        for day in 1..=total_items {
            if let Some(Reverse((val, shop))) = heap.pop() {
                ans += (val as i64) * (day as i64);
                if idx[shop] > 0 {
                    idx[shop] -= 1;
                    let new_pos = idx[shop];
                    heap.push(Reverse((values[shop][new_pos], shop)));
                }
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (max-spending values)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ([all (apply append values)]
         [sorted (sort all <)])
    (let loop ((lst sorted) (day 1) (acc 0))
      (if (null? lst)
          acc
          (loop (cdr lst) (+ day 1) (+ acc (* (car lst) day)))))))
```

## Erlang

```erlang
-spec max_spending(Values :: [[integer()]]) -> integer().
max_spending(Values) ->
    ShopLists = [lists:reverse(Row) || Row <- Values],
    TotalItems = length(Values) * (case Values of [] -> 0; [Row|_] -> length(Row) end),
    loop(ShopLists, 1, TotalItems, 0).

loop(_, Day, MaxDay, Acc) when Day > MaxDay ->
    Acc;
loop(ShopLists, Day, MaxDay, Acc) ->
    {MinVal, MinIdx} = find_min_head(ShopLists),
    UpdatedShopLists = update_at_index(ShopLists, MinIdx,
        fun(L) -> tl(L) end),
    loop(UpdatedShopLists, Day + 1, MaxDay, Acc + MinVal * Day).

find_min_head(ShopLists) ->
    find_min_head(ShopLists, 0, undefined, -1).

find_min_head([], _Idx, MinVal, MinIdx) ->
    {MinVal, MinIdx};
find_min_head([L|Rest], Idx, undefined, _) ->
    case L of
        [] -> find_min_head(Rest, Idx + 1, undefined, -1);
        [H|_] -> find_min_head(Rest, Idx + 1, H, Idx)
    end;
find_min_head([L|Rest], Idx, MinVal, MinIdx) ->
    case L of
        [] -> find_min_head(Rest, Idx + 1, MinVal, MinIdx);
        [H|_] ->
            if H < MinVal ->
                find_min_head(Rest, Idx + 1, H, Idx);
               true ->
                find_min_head(Rest, Idx + 1, MinVal, MinIdx)
            end
    end.

update_at_index([], _Idx, _Fun) -> [];
update_at_index([L|Rest], 0, Fun) ->
    [Fun(L) | Rest];
update_at_index([L|Rest], Idx, Fun) when Idx > 0 ->
    [L | update_at_index(Rest, Idx - 1, Fun)].
```

## Elixir

```elixir
defmodule Solution do
  @spec max_spending(values :: [[integer]]) :: integer
  def max_spending(values) do
    m = length(values)

    if m == 0 do
      0
    else
      n = length(List.first(values))
      total_days = m * n

      # Reverse each row so the smallest element is at the head.
      lists = Enum.map(values, &Enum.reverse/1)
      max_int = 1 <<< 60

      {ans, _} =
        1..total_days
        |> Enum.reduce({0, lists}, fn day, {sum, cur_lists} ->
          {min_val, min_idx} =
            cur_lists
            |> Enum.with_index()
            |> Enum.reduce({max_int, -1}, fn
              {[], _i}, acc -> acc
              {[h | _t], i}, {cur_min, cur_idx} ->
                if h < cur_min, do: {h, i}, else: {cur_min, cur_idx}
            end)

          new_sum = sum + min_val * day

          updated_lists =
            List.update_at(cur_lists, min_idx, fn [_head | tail] -> tail end)

          {new_sum, updated_lists}
        end)

      ans
    end
  end
end
```
