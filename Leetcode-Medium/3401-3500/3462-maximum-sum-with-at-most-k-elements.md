# 3462. Maximum Sum With at Most K Elements

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long maxSum(vector<vector<int>>& grid, vector<int>& limits, int k) {
        vector<int> candidates;
        int n = grid.size();
        for (int i = 0; i < n; ++i) {
            int take = min(limits[i], (int)grid[i].size());
            if (take == 0) continue;
            vector<int> row = grid[i];
            nth_element(row.begin(), row.begin() + take, row.end(), greater<int>());
            // Now first 'take' elements are the largest but unsorted; we can push them directly.
            for (int j = 0; j < take; ++j) candidates.push_back(row[j]);
        }
        if (candidates.empty() || k == 0) return 0;
        int need = min(k, (int)candidates.size());
        nth_element(candidates.begin(), candidates.begin() + need, candidates.end(), greater<int>());
        long long ans = 0;
        for (int i = 0; i < need; ++i) ans += candidates[i];
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long maxSum(int[][] grid, int[] limits, int k) {
        java.util.List<Integer> candidates = new java.util.ArrayList<>();
        for (int i = 0; i < grid.length; i++) {
            int[] row = grid[i];
            java.util.Arrays.sort(row);
            int cnt = Math.min(limits[i], row.length);
            for (int j = row.length - 1; j >= row.length - cnt; j--) {
                candidates.add(row[j]);
            }
        }
        candidates.sort(java.util.Collections.reverseOrder());
        long sum = 0;
        int pick = Math.min(k, candidates.size());
        for (int i = 0; i < pick; i++) {
            sum += candidates.get(i);
        }
        return sum;
    }
}
```

## Python

```python
class Solution(object):
    def maxSum(self, grid, limits, k):
        """
        :type grid: List[List[int]]
        :type limits: List[int]
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 0
        candidates = []
        for row, lim in zip(grid, limits):
            if lim > 0:
                # take the largest 'lim' elements from this row
                row_sorted = sorted(row, reverse=True)
                candidates.extend(row_sorted[:lim])
        if not candidates:
            return 0
        if len(candidates) <= k:
            return sum(candidates)
        candidates.sort(reverse=True)
        return sum(candidates[:k])
```

## Python3

```python
import heapq
from typing import List

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        candidates = []
        for row, lim in zip(grid, limits):
            if lim > 0:
                # take the largest 'lim' elements from this row
                top_vals = heapq.nlargest(lim, row)
                candidates.extend(top_vals)
        if k == 0:
            return 0
        return sum(heapq.nlargest(k, candidates))
```

## C

```c
#include <stdlib.h>

typedef struct {
    int val;
    int row;
    int idx;
} Node;

static void heapSwap(Node *a, Node *b) {
    Node tmp = *a;
    *a = *b;
    *b = tmp;
}

static void heapPush(Node *heap, int *size, Node node) {
    int i = (*size)++;
    heap[i] = node;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (heap[p].val >= heap[i].val) break;
        heapSwap(&heap[p], &heap[i]);
        i = p;
    }
}

static void heapPop(Node *heap, int *size, Node *out) {
    *out = heap[0];
    heap[0] = heap[--(*size)];
    int i = 0, n = *size;
    while (1) {
        int l = i * 2 + 1;
        int r = l + 1;
        if (l >= n) break;
        int largest = l;
        if (r < n && heap[r].val > heap[l].val) largest = r;
        if (heap[i].val >= heap[largest].val) break;
        heapSwap(&heap[i], &heap[largest]);
        i = largest;
    }
}

static int cmpDesc(const void *a, const void *b) {
    return *(int *)b - *(int *)a;
}

long long maxSum(int** grid, int gridSize, int* gridColSize, int* limits, int limitsSize, int k) {
    if (k == 0) return 0LL;

    int n = gridSize;
    int cap = n + k + 5;
    Node *heap = (Node *)malloc(sizeof(Node) * cap);
    int heapSize = 0;

    for (int i = 0; i < n; ++i) {
        if (limits[i] > 0 && gridColSize[i] > 0) {
            qsort(grid[i], gridColSize[i], sizeof(int), cmpDesc);
            Node node = {grid[i][0], i, 0};
            heapPush(heap, &heapSize, node);
        }
    }

    long long sum = 0;
    int taken = 0;
    while (taken < k && heapSize > 0) {
        Node cur;
        heapPop(heap, &heapSize, &cur);
        sum += cur.val;
        ++taken;

        int row = cur.row;
        int nextIdx = cur.idx + 1;
        if (nextIdx < limits[row] && nextIdx < gridColSize[row]) {
            Node nxt = {grid[row][nextIdx], row, nextIdx};
            heapPush(heap, &heapSize, nxt);
        }
    }

    free(heap);
    return sum;
}
```

## Csharp

```csharp
public class Solution {
    public long MaxSum(int[][] grid, int[] limits, int k) {
        List<int> candidates = new List<int>();
        int n = grid.Length;
        for (int i = 0; i < n; i++) {
            int limit = limits[i];
            if (limit <= 0) continue;
            int[] row = grid[i];
            Array.Sort(row); // ascending
            int cnt = Math.Min(limit, row.Length);
            for (int j = 1; j <= cnt; j++) {
                candidates.Add(row[row.Length - j]); // take largest elements
            }
        }

        if (k == 0 || candidates.Count == 0) return 0L;

        candidates.Sort((a, b) => b.CompareTo(a)); // descending

        long sum = 0;
        int take = Math.Min(k, candidates.Count);
        for (int i = 0; i < take; i++) {
            sum += candidates[i];
        }
        return sum;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @param {number[]} limits
 * @param {number} k
 * @return {number}
 */
var maxSum = function(grid, limits, k) {
    const candidates = [];
    for (let i = 0; i < grid.length; ++i) {
        const row = grid[i];
        row.sort((a, b) => b - a);
        const cnt = Math.min(limits[i], row.length);
        for (let j = 0; j < cnt; ++j) {
            candidates.push(row[j]);
        }
    }
    if (k === 0) return 0;
    candidates.sort((a, b) => b - a);
    let sum = 0;
    const take = Math.min(k, candidates.length);
    for (let i = 0; i < take; ++i) {
        sum += candidates[i];
    }
    return sum;
};
```

## Typescript

```typescript
function maxSum(grid: number[][], limits: number[], k: number): number {
    const candidates: number[] = [];
    for (let i = 0; i < grid.length; i++) {
        const row = grid[i];
        const limit = Math.min(limits[i], row.length);
        if (limit === 0) continue;
        const sorted = row.slice().sort((a, b) => b - a);
        for (let j = 0; j < limit; j++) {
            candidates.push(sorted[j]);
        }
    }
    if (k === 0 || candidates.length === 0) return 0;
    candidates.sort((a, b) => b - a);
    const take = Math.min(k, candidates.length);
    let sum = 0;
    for (let i = 0; i < take; i++) {
        sum += candidates[i];
    }
    return sum;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @param Integer[] $limits
     * @param Integer $k
     * @return Integer
     */
    function maxSum($grid, $limits, $k) {
        $candidates = [];
        $n = count($grid);
        for ($i = 0; $i < $n; $i++) {
            $row = $grid[$i];
            rsort($row); // descending order
            $limit = $limits[$i];
            $cnt = min($limit, count($row));
            for ($j = 0; $j < $cnt; $j++) {
                $candidates[] = $row[$j];
            }
        }

        if ($k == 0 || empty($candidates)) {
            return 0;
        }

        rsort($candidates);
        $take = min($k, count($candidates));
        $sum = 0;
        for ($i = 0; $i < $take; $i++) {
            $sum += $candidates[$i];
        }
        return $sum;
    }
}
```

## Swift

```swift
class Solution {
    func maxSum(_ grid: [[Int]], _ limits: [Int], _ k: Int) -> Int {
        var heap = MaxHeap()
        let n = grid.count
        for i in 0..<n {
            var row = grid[i]
            row.sort(by: >)
            let cnt = min(limits[i], row.count)
            if cnt > 0 {
                for j in 0..<cnt {
                    heap.push(row[j])
                }
            }
        }
        var remaining = k
        var result = 0
        while remaining > 0, let val = heap.pop() {
            result += val
            remaining -= 1
        }
        return result
    }
}

struct MaxHeap {
    private var data: [Int] = []
    
    mutating func push(_ x: Int) {
        data.append(x)
        siftUp(data.count - 1)
    }
    
    mutating func pop() -> Int? {
        guard !data.isEmpty else { return nil }
        if data.count == 1 {
            return data.removeLast()
        }
        let top = data[0]
        data[0] = data.removeLast()
        siftDown(0)
        return top
    }
    
    private mutating func siftUp(_ index: Int) {
        var child = index
        while child > 0 {
            let parent = (child - 1) / 2
            if data[parent] < data[child] {
                data.swapAt(parent, child)
                child = parent
            } else { break }
        }
    }
    
    private mutating func siftDown(_ index: Int) {
        var parent = index
        while true {
            let left = parent * 2 + 1
            let right = left + 1
            var largest = parent
            if left < data.count && data[left] > data[largest] { largest = left }
            if right < data.count && data[right] > data[largest] { largest = right }
            if largest == parent { break }
            data.swapAt(parent, largest)
            parent = largest
        }
    }
}
```

## Kotlin

```kotlin
import java.util.PriorityQueue
import java.util.Arrays

class Solution {
    fun maxSum(grid: Array<IntArray>, limits: IntArray, k: Int): Long {
        val n = grid.size
        // Store for each row the sorted descending list of selectable elements (up to its limit)
        val rows = Array(n) { IntArray(0) }
        for (i in 0 until n) {
            val limit = limits[i].coerceAtMost(grid[i].size)
            if (limit == 0) continue
            val copy = grid[i].clone()
            Arrays.sort(copy) // ascending
            val selected = IntArray(limit)
            var idx = copy.size - 1
            for (j in 0 until limit) {
                selected[j] = copy[idx--]
            }
            rows[i] = selected
        }

        data class Node(val value: Int, val row: Int, val idx: Int)

        val pq = PriorityQueue<Node>(compareByDescending { it.value })
        for (i in 0 until n) {
            if (rows[i].isNotEmpty()) {
                pq.offer(Node(rows[i][0], i, 0))
            }
        }

        var remaining = k
        var sum = 0L
        while (remaining > 0 && pq.isNotEmpty()) {
            val cur = pq.poll()
            sum += cur.value.toLong()
            remaining--
            val nextIdx = cur.idx + 1
            if (nextIdx < rows[cur.row].size) {
                pq.offer(Node(rows[cur.row][nextIdx], cur.row, nextIdx))
            }
        }
        return sum
    }
}
```

## Dart

```dart
class Solution {
  int maxSum(List<List<int>> grid, List<int> limits, int k) {
    List<int> candidates = [];

    for (int i = 0; i < grid.length; i++) {
      int limit = limits[i];
      if (limit == 0) continue;

      List<int> row = List.from(grid[i]);
      row.sort((a, b) => b.compareTo(a));

      int take = limit < row.length ? limit : row.length;
      for (int j = 0; j < take; j++) {
        candidates.add(row[j]);
      }
    }

    if (candidates.isEmpty || k == 0) return 0;

    candidates.sort((a, b) => b.compareTo(a));

    int takeK = k < candidates.length ? k : candidates.length;
    int sum = 0;
    for (int i = 0; i < takeK; i++) {
      sum += candidates[i];
    }
    return sum;
  }
}
```

## Golang

```go
func maxSum(grid [][]int, limits []int, k int) int64 {
    candidates := make([]int, 0)
    for i, row := range grid {
        sort.Slice(row, func(a, b int) bool { return row[a] > row[b] })
        limit := limits[i]
        if limit > len(row) {
            limit = len(row)
        }
        for j := 0; j < limit && j < len(row); j++ {
            candidates = append(candidates, row[j])
        }
    }
    sort.Slice(candidates, func(i, j int) bool { return candidates[i] > candidates[j] })
    if k > len(candidates) {
        k = len(candidates)
    }
    var sum int64
    for i := 0; i < k; i++ {
        sum += int64(candidates[i])
    }
    return sum
}
```

## Ruby

```ruby
def max_sum(grid, limits, k)
  candidates = []
  grid.each_with_index do |row, i|
    limit = limits[i]
    next if limit <= 0
    sorted = row.sort.reverse
    take = [limit, sorted.length].min
    candidates.concat(sorted[0, take])
  end
  candidates.sort!.reverse!
  cnt = [k, candidates.size].min
  sum = 0
  cnt.times { |idx| sum += candidates[idx] }
  sum
end
```

## Scala

```scala
object Solution {
    def maxSum(grid: Array[Array[Int]], limits: Array[Int], k: Int): Long = {
        val n = grid.length
        val candidates = scala.collection.mutable.ArrayBuffer.empty[Int]

        var i = 0
        while (i < n) {
            val limit = limits(i)
            if (limit > 0) {
                // sort row in descending order
                val sortedRow = grid(i).sorted(Ordering.Int.reverse)
                val cnt = math.min(limit, sortedRow.length)
                var j = 0
                while (j < cnt) {
                    candidates += sortedRow(j)
                    j += 1
                }
            }
            i += 1
        }

        if (k == 0 || candidates.isEmpty) return 0L

        val take = math.min(k, candidates.size)
        val topK = candidates.sorted(Ordering.Int.reverse).take(take)

        var sum: Long = 0L
        var idx = 0
        while (idx < topK.length) {
            sum += topK(idx).toLong
            idx += 1
        }
        sum
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_sum(grid: Vec<Vec<i32>>, limits: Vec<i32>, k: i32) -> i64 {
        let mut candidates: Vec<i32> = Vec::new();
        for (row, &lim_i) in grid.iter().zip(limits.iter()) {
            let lim = lim_i as usize;
            if lim == 0 {
                continue;
            }
            let mut sorted_row = row.clone();
            sorted_row.sort_unstable_by(|a, b| b.cmp(a));
            let take = std::cmp::min(lim, sorted_row.len());
            candidates.extend_from_slice(&sorted_row[..take]);
        }

        let k_usize = k as usize;
        if k_usize == 0 || candidates.is_empty() {
            return 0;
        }

        candidates.sort_unstable_by(|a, b| b.cmp(a));
        let take = std::cmp::min(k_usize, candidates.len());
        candidates.iter().take(take).map(|&x| x as i64).sum()
    }
}
```

## Racket

```racket
(define/contract (max-sum grid limits k)
  (-> (listof (listof exact-integer?)) (listof exact-integer?) exact-integer? exact-integer?)
  (letrec ((take
            (lambda (lst n)
              (if (or (zero? n) (null? lst))
                  '()
                  (cons (car lst) (take (cdr lst) (- n 1)))))))
    (let* ((selected
            (apply append
                   (map (lambda (row limit)
                          (let ((sorted (sort row >)))
                            (if (> limit (length sorted))
                                sorted
                                (take sorted limit))))
                        grid limits)))
           (sorted-all (sort selected >))
           (to-take (min k (length sorted-all))))
      (foldl + 0 (take sorted-all to-take)))))
```

## Erlang

```erlang
-module(solution).
-export([max_sum/3]).

-spec max_sum(Grid :: [[integer()]], Limits :: [integer()], K :: integer()) -> integer().
max_sum(Grid, Limits, K) ->
    Selected = [Val ||
                {Row, Lim} <- lists:zip(Grid, Limits),
                Val <- lists:sublist(lists:reverse(lists:sort(Row)), Lim)],
    Sorted = lists:reverse(lists:sort(Selected)),
    sum_first_k(Sorted, K).

sum_first_k(_, 0) -> 0;
sum_first_k([], _) -> 0;
sum_first_k([H|T], N) when N > 0 ->
    H + sum_first_k(T, N - 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_sum(grid :: [[integer]], limits :: [integer], k :: integer) :: integer
  def max_sum(grid, limits, k) do
    candidates =
      Enum.with_index(grid)
      |> Enum.flat_map(fn {row, i} ->
        limit = Enum.at(limits, i, 0)

        row
        |> Enum.sort(&>=/2)
        |> Enum.take(limit)
      end)

    sorted = Enum.sort(candidates, &>=/2)
    take = min(k, length(sorted))
    sorted
    |> Enum.take(take)
    |> Enum.sum()
  end
end
```
