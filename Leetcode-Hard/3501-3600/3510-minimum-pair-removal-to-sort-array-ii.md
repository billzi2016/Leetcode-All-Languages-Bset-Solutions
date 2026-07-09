# 3510. Minimum Pair Removal to Sort Array II

## Cpp

```cpp
class Solution {
public:
    int minimumPairRemoval(vector<int>& nums) {
        int n = nums.size();
        if (n < 2) return 0;
        vector<int> left(n), right(n);
        for (int i = 0; i < n; ++i) {
            left[i] = i - 1;
            right[i] = (i + 1 < n) ? i + 1 : -1;
        }
        std::set<int> bad;
        for (int i = 0; i + 1 < n; ++i) {
            if (nums[i] > nums[i + 1]) bad.insert(i);
        }
        int ops = 0;
        while (!bad.empty()) {
            int i = *bad.begin();          // smallest index with inversion
            int j = right[i];              // its right neighbor, guaranteed to exist
            // remove pair (i, j)
            ++ops;
            int li = left[i];
            int rj = right[j];
            // erase affected entries from set
            if (li != -1) bad.erase(li);
            bad.erase(i);
            bad.erase(j);
            // reconnect the list
            if (li != -1) right[li] = rj;
            if (rj != -1) left[rj] = li;
            // check new adjacency for inversion
            if (li != -1 && rj != -1 && nums[li] > nums[rj]) {
                bad.insert(li);
            }
        }
        return ops;
    }
};
```

## Java

```java
class Solution {
    public int minimumPairRemoval(int[] nums) {
        int n = nums.length;
        int[] tails = new int[n];
        int size = 0;
        for (int x : nums) {
            int l = 0, r = size;
            while (l < r) {
                int m = (l + r) >>> 1;
                if (tails[m] <= x) {
                    l = m + 1;
                } else {
                    r = m;
                }
            }
            if (l == size) {
                tails[size++] = x;
            } else {
                tails[l] = x;
            }
        }
        return n - size;
    }
}
```

## Python

```python
class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import bisect
        tails = []
        for x in nums:
            # find position to insert x to keep non-decreasing order
            idx = bisect.bisect_right(tails, x)
            if idx == len(tails):
                tails.append(x)
            else:
                tails[idx] = x
        return len(nums) - len(tails)
```

## Python3

```python
from typing import List
import heapq

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        prev = [-1] * n
        nxt = [-1] * n
        for i in range(n):
            if i > 0:
                prev[i] = i - 1
            if i + 1 < n:
                nxt[i] = i + 1

        heap = []
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                heapq.heappush(heap, i)

        removed = [False] * n
        ops = 0

        while heap:
            i = heapq.heappop(heap)
            if removed[i]:
                continue
            j = nxt[i]
            if j == -1 or removed[j]:
                continue
            if nums[i] <= nums[j]:
                continue

            # remove pair (i, j)
            ops += 1
            removed[i] = removed[j] = True

            l = prev[i]
            r = nxt[j]

            if l != -1:
                nxt[l] = r
            if r != -1:
                prev[r] = l

            if l != -1 and r != -1 and not removed[l] and not removed[r]:
                if nums[l] > nums[r]:
                    heapq.heappush(heap, l)

        return ops
```

## C

```c
#include <stddef.h>
#include <stdlib.h>

static void heapSwap(int *a, int *b) {
    int t = *a;
    *a = *b;
    *b = t;
}

static void heapPush(int *heap, int *size, int val) {
    int i = (*size)++;
    heap[i] = val;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (heap[p] <= heap[i]) break;
        heapSwap(&heap[p], &heap[i]);
        i = p;
    }
}

static int heapTop(int *heap, int size) {
    return heap[0];
}

static void heapPop(int *heap, int *size) {
    if (*size == 0) return;
    heap[0] = heap[--(*size)];
    int i = 0;
    while (1) {
        int l = i * 2 + 1;
        int r = l + 1;
        if (l >= *size) break;
        int smallest = l;
        if (r < *size && heap[r] < heap[l]) smallest = r;
        if (heap[i] <= heap[smallest]) break;
        heapSwap(&heap[i], &heap[smallest]);
        i = smallest;
    }
}

int minimumPairRemoval(int* nums, int numsSize) {
    if (numsSize <= 1) return 0;

    int *prev = (int *)malloc(numsSize * sizeof(int));
    int *next = (int *)malloc(numsSize * sizeof(int));
    char *removed = (char *)calloc(numsSize, sizeof(char));

    for (int i = 0; i < numsSize; ++i) {
        prev[i] = i - 1;
        next[i] = (i + 1 < numsSize) ? i + 1 : -1;
    }

    int heapCap = numsSize * 2 + 5;
    int *heap = (int *)malloc(heapCap * sizeof(int));
    int heapSize = 0;

    for (int i = 0; i + 1 < numsSize; ++i) {
        if (nums[i] > nums[i + 1]) {
            heapPush(heap, &heapSize, i);
        }
    }

    int ops = 0;
    while (1) {
        // discard invalid entries
        while (heapSize > 0) {
            int idx = heapTop(heap, heapSize);
            int jdx = next[idx];
            if (idx == -1 || jdx == -1 ||
                removed[idx] || removed[jdx] ||
                nums[idx] <= nums[jdx]) {
                heapPop(heap, &heapSize);
            } else break;
        }
        if (heapSize == 0) break;

        int i = heapTop(heap, heapSize);
        heapPop(heap, &heapSize);
        int j = next[i];
        // perform removal of pair (i, j)
        ops++;
        removed[i] = removed[j] = 1;
        int p = prev[i];
        int s = next[j];

        if (p != -1) next[p] = s;
        if (s != -1) prev[s] = p;

        // check new adjacent pair (p, s)
        if (p != -1 && s != -1 && !removed[p] && !removed[s] && nums[p] > nums[s]) {
            heapPush(heap, &heapSize, p);
        }
    }

    free(prev);
    free(next);
    free(removed);
    free(heap);
    return ops;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumPairRemoval(int[] nums) {
        int n = nums.Length;
        int ops = 0;
        int i = 0;
        while (i < n - 1) {
            if (nums[i] > nums[i + 1]) {
                ops++;
                i += 2; // remove both elements
            } else {
                i++;
            }
        }
        return ops;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumPairRemoval = function(nums) {
    let ops = 0;
    const n = nums.length;
    let i = 0;
    while (i < n - 1) {
        if (nums[i] > nums[i + 1]) {
            // start of a decreasing segment
            let len = 0;
            while (i < n - 1 && nums[i] > nums[i + 1]) {
                len++;
                i++;
            }
            ops += Math.ceil(len / 2);
        } else {
            i++;
        }
    }
    return ops;
};
```

## Typescript

```typescript
function minimumPairRemoval(nums: number[]): number {
    const n = nums.length;
    if (n < 2) return 0;

    // doubly linked list
    const left = new Int32Array(n);
    const right = new Int32Array(n);
    for (let i = 0; i < n; i++) {
        left[i] = i - 1;
        right[i] = i + 1 < n ? i + 1 : -1;
    }
    const removed = new Uint8Array(n);

    // min-heap implementation
    class MinHeap {
        heap: { sum: number; idx: number }[] = [];
        push(node: { sum: number; idx: number }) {
            this.heap.push(node);
            this.bubbleUp(this.heap.length - 1);
        }
        bubbleUp(pos: number) {
            const heap = this.heap;
            while (pos > 0) {
                const parent = (pos - 1) >> 1;
                if (heap[parent].sum <= heap[pos].sum) break;
                [heap[parent], heap[pos]] = [heap[pos], heap[parent]];
                pos = parent;
            }
        }
        pop(): { sum: number; idx: number } | undefined {
            const heap = this.heap;
            if (heap.length === 0) return undefined;
            const top = heap[0];
            const last = heap.pop()!;
            if (heap.length > 0) {
                heap[0] = last;
                this.bubbleDown(0);
            }
            return top;
        }
        bubbleDown(pos: number) {
            const heap = this.heap;
            const len = heap.length;
            while (true) {
                let leftIdx = pos * 2 + 1;
                let rightIdx = leftIdx + 1;
                let smallest = pos;

                if (leftIdx < len && heap[leftIdx].sum < heap[smallest].sum) smallest = leftIdx;
                if (rightIdx < len && heap[rightIdx].sum < heap[smallest].sum) smallest = rightIdx;

                if (smallest === pos) break;
                [heap[pos], heap[smallest]] = [heap[smallest], heap[pos]];
                pos = smallest;
            }
        }
        isEmpty(): boolean {
            return this.heap.length === 0;
        }
    }

    const pq = new MinHeap();

    // initialize bad pairs
    for (let i = 0; i < n - 1; i++) {
        if (nums[i] > nums[i + 1]) {
            pq.push({ sum: nums[i] + nums[i + 1], idx: i });
        }
    }

    let ops = 0;

    while (!pq.isEmpty()) {
        const node = pq.pop()!;
        const i = node.idx;
        const j = right[i];
        // validate current pair
        if (i === -1 || j === -1) continue;
        if (removed[i] || removed[j]) continue;
        if (right[i] !== j) continue; // not adjacent anymore
        if (nums[i] <= nums[j]) continue; // no longer a bad pair

        // remove both i and j
        removed[i] = 1;
        removed[j] = 1;
        ops++;

        const li = left[i];
        const rj = right[j];

        if (li !== -1) right[li] = rj;
        if (rj !== -1) left[rj] = li;

        // check new adjacent pair formed by li and rj
        if (li !== -1 && rj !== -1 && nums[li] > nums[rj]) {
            pq.push({ sum: nums[li] + nums[rj], idx: li });
        }
    }

    return ops;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumPairRemoval($nums) {
        $n = count($nums);
        $ans = 0;
        $i = 0;
        while ($i < $n - 1) {
            if ($nums[$i] > $nums[$i + 1]) {
                $ans++;
                $i += 2; // remove this decreasing pair
            } else {
                $i++;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minimumPairRemoval(_ nums: [Int]) -> Int {
        var tails = [Int]()
        for v in nums {
            var left = 0
            var right = tails.count
            while left < right {
                let mid = (left + right) >> 1
                if tails[mid] <= v {
                    left = mid + 1
                } else {
                    right = mid
                }
            }
            if left == tails.count {
                tails.append(v)
            } else {
                tails[left] = v
            }
        }
        return nums.count - tails.count
    }
}
```

## Kotlin

```kotlin
class Solution {
    private class BIT(size: Int) {
        private val n = size
        private val tree = IntArray(n + 2)
        fun update(idx: Int, value: Int) {
            var i = idx
            while (i <= n) {
                if (value > tree[i]) tree[i] = value
                i += i and -i
            }
        }

        fun query(idx: Int): Int {
            var res = 0
            var i = idx
            while (i > 0) {
                if (tree[i] > res) res = tree[i]
                i -= i and -i
            }
            return res
        }
    }

    fun minimumPairRemoval(nums: IntArray): Int {
        val n = nums.size
        // coordinate compression
        val sortedVals = nums.distinct().sorted()
        val comp = HashMap<Int, Int>(sortedVals.size * 2)
        for (i in sortedVals.indices) {
            comp[sortedVals[i]] = i + 1   // 1‑based index for BIT
        }
        val m = sortedVals.size
        val bits = Array(2) { BIT(m) }    // bits[0] for even positions, bits[1] for odd

        var bestLen = if (n % 2 == 0) 0 else Int.MIN_VALUE

        for (i in nums.indices) {
            val idx = comp[nums[i]]!!
            val parity = i and 1
            val opposite = parity xor 1

            var cur = Int.MIN_VALUE
            // start a new subsequence if prefix length is even (i must be even)
            if (parity == 0) cur = 1

            val prev = bits[opposite].query(idx)
            if (prev > 0) {
                cur = maxOf(cur, prev + 1)
            }

            if (cur > 0) {
                bits[parity].update(idx, cur)
                // suffix after i must be removable => length even
                if ((n - 1 - i) % 2 == 0) {
                    bestLen = maxOf(bestLen, cur)
                }
            }
        }

        if (bestLen < 0) {
            // odd n and no valid subsequence found; keep any single element at even index
            bestLen = 1
        }

        return (n - bestLen) / 2
    }
}
```

## Dart

```dart
class Solution {
  int minimumPairRemoval(List<int> nums) {
    int n = nums.length;
    List<int> prev = List.filled(n, -1);
    List<int> next = List.filled(n, -1);
    for (int i = 0; i < n; ++i) {
      if (i > 0) prev[i] = i - 1;
      if (i + 1 < n) next[i] = i + 1;
    }
    List<bool> removed = List.filled(n, false);

    // binary min-heap for pairs
    class _Pair {
      int sum;
      int i;
      int j;
      _Pair(this.sum, this.i, this.j);
    }

    List<_Pair> heap = [];

    void heapPush(_Pair p) {
      heap.add(p);
      int idx = heap.length - 1;
      while (idx > 0) {
        int parent = (idx - 1) >> 1;
        if (heap[parent].sum < heap[idx].sum ||
            (heap[parent].sum == heap[idx].sum && heap[parent].i <= heap[idx].i)) break;
        var tmp = heap[parent];
        heap[parent] = heap[idx];
        heap[idx] = tmp;
        idx = parent;
      }
    }

    _Pair? heapPop() {
      if (heap.isEmpty) return null;
      var top = heap[0];
      var last = heap.removeLast();
      if (heap.isNotEmpty) {
        heap[0] = last;
        int idx = 0;
        while (true) {
          int left = idx * 2 + 1;
          int right = left + 1;
          if (left >= heap.length) break;
          int smallest = left;
          if (right < heap.length) {
            if (heap[right].sum < heap[left].sum ||
                (heap[right].sum == heap[left].sum && heap[right].i < heap[left].i)) {
              smallest = right;
            }
          }
          if (heap[smallest].sum < heap[idx].sum ||
              (heap[smallest].sum == heap[idx].sum && heap[smallest].i < heap[idx].i)) {
            var tmp = heap[smallest];
            heap[smallest] = heap[idx];
            heap[idx] = tmp;
            idx = smallest;
          } else {
            break;
          }
        }
      }
      return top;
    }

    // initial bad adjacent pairs
    for (int i = 0; i + 1 < n; ++i) {
      if (nums[i] > nums[i + 1]) {
        heapPush(_Pair(nums[i] + nums[i + 1], i, i + 1));
      }
    }

    int ops = 0;
    while (true) {
      var pair = heapPop();
      if (pair == null) break;
      int i = pair.i;
      int j = pair.j;
      if (removed[i] || removed[j]) continue;
      if (next[i] != j || prev[j] != i) continue; // not adjacent anymore
      // remove both
      removed[i] = true;
      removed[j] = true;
      ops++;

      int l = prev[i];
      int r = next[j];

      if (l != -1) next[l] = r;
      if (r != n) prev[r] = l;

      if (l != -1 && r != n && nums[l] > nums[r]) {
        heapPush(_Pair(nums[l] + nums[r], l, r));
      }
    }

    return ops;
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
	sum int64
	idx int // left index of the pair (right = right[idx])
}

type minHeap []pair

func (h minHeap) Len() int           { return len(h) }
func (h minHeap) Less(i, j int) bool { return h[i].sum < h[j].sum }
func (h minHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *minHeap) Push(x interface{}) {
	*h = append(*h, x.(pair))
}

func (h *minHeap) Pop() interface{} {
	old := *h
	n := len(old)
	it := old[n-1]
	*h = old[:n-1]
	return it
}

// minimumPairRemoval returns the minimal number of operations needed to make the array non‑decreasing.
// An operation removes a consecutive decreasing pair (i, i+1) where nums[i] > nums[i+1].
func minimumPairRemoval(nums []int) int {
	n := len(nums)
	if n < 2 {
		return 0
	}
	left := make([]int, n)
	right := make([]int, n)
	active := make([]bool, n)

	for i := 0; i < n; i++ {
		left[i] = i - 1
		if i+1 < n {
			right[i] = i + 1
		} else {
			right[i] = -1
		}
		active[i] = true
	}

	h := &minHeap{}
	heap.Init(h)

	for i := 0; i < n-1; i++ {
		if nums[i] > nums[i+1] {
			heap.Push(h, pair{int64(nums[i]) + int64(nums[i+1]), i})
		}
	}

	ops := 0
	for h.Len() > 0 {
		top := heap.Pop(h).(pair)
		i := top.idx
		if !active[i] {
			continue
		}
		j := right[i]
		if j == -1 || !active[j] {
			continue
		}
		if nums[i] <= nums[j] {
			continue
		}

		// remove both i and j
		active[i] = false
		active[j] = false
		ops++

		li := left[i]
		rj := right[j]

		if li != -1 {
			right[li] = rj
		}
		if rj != -1 {
			left[rj] = li
		}

		if li != -1 && rj != -1 && nums[li] > nums[rj] {
			heap.Push(h, pair{int64(nums[li]) + int64(nums[rj]), li})
		}
	}

	return ops
}
```

## Ruby

```ruby
def minimum_pair_removal(nums)
  n = nums.size
  return 0 if n <= 1

  prev = Array.new(n) { |i| i - 1 }
  nxt  = Array.new(n) { |i| i + 1 < n ? i + 1 : -1 }
  removed = Array.new(n, false)

  heap = []

  # min‑heap helpers
  define_singleton_method(:heap_push) do |h, item|
    h << item
    i = h.size - 1
    while i > 0
      p = (i - 1) / 2
      break if h[p][0] <= item[0]
      h[i] = h[p]
      i = p
    end
    h[i] = item
  end

  define_singleton_method(:heap_pop) do |h|
    top = h[0]
    last = h.pop
    unless h.empty?
      i = 0
      while (c = i * 2 + 1) < h.size
        r = c + 1
        c = r if r < h.size && h[r][0] < h[c][0]
        break if last[0] <= h[c][0]
        h[i] = h[c]
        i = c
      end
      h[i] = last
    end
    top
  end

  (0...n - 1).each do |i|
    heap_push(heap, [i + i + 1, i, i + 1]) if nums[i] > nums[i + 1]
  end

  ops = 0
  until heap.empty?
    sum, l, r = heap_pop(heap)
    next if removed[l] || removed[r]
    next unless nxt[l] == r && prev[r] == l   # still adjacent

    # remove both nodes
    removed[l] = true
    removed[r] = true
    left  = prev[l]
    right = nxt[r]

    nxt[left] = right if left != -1
    prev[right] = left if right != -1

    ops += 1

    # check new adjacency created by removal
    if left != -1 && right != -1 && nums[left] > nums[right]
      heap_push(heap, [left + right, left, right])
    end
  end

  ops
end
```

## Scala

```scala
object Solution {
    def minimumPairRemoval(nums: Array[Int]): Int = {
        // Compute length of longest non-decreasing subsequence (LNDS)
        val tails = new scala.collection.mutable.ArrayBuffer[Int]()
        for (x <- nums) {
            var l = 0
            var r = tails.length
            while (l < r) {
                val m = (l + r) >>> 1
                if (tails(m) <= x) l = m + 1 else r = m
            }
            if (l == tails.length) tails += x
            else tails(l) = x
        }
        val keep = tails.length
        // Each operation removes exactly two elements.
        ((nums.length - keep) + 1) / 2
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_pair_removal(nums: Vec<i32>) -> i32 {
        use std::cmp::Reverse;
        use std::collections::BinaryHeap;

        let n = nums.len();
        if n <= 1 {
            return 0;
        }

        // Doubly linked list representation
        let mut left: Vec<Option<usize>> = (0..n).map(|i| if i == 0 { None } else { Some(i - 1) }).collect();
        let mut right: Vec<Option<usize>> = (0..n).map(|i| if i + 1 >= n { None } else { Some(i + 1) }).collect();

        let mut removed = vec![false; n];
        let mut heap: BinaryHeap<Reverse<(i64, usize)>> = BinaryHeap::new();

        // Initialize heap with all decreasing adjacent pairs
        for i in 0..n - 1 {
            if nums[i] > nums[i + 1] {
                let sum = nums[i] as i64 + nums[i + 1] as i64;
                heap.push(Reverse((sum, i)));
            }
        }

        let mut ops: i32 = 0;

        while let Some(Reverse((_sum, l))) = heap.pop() {
            if removed[l] {
                continue;
            }
            let r_opt = right[l];
            if r_opt.is_none() {
                continue;
            }
            let r = r_opt.unwrap();
            if removed[r] {
                continue;
            }
            // ensure still adjacent and decreasing
            if right[l] != Some(r) || left[r] != Some(l) {
                continue;
            }
            if nums[l] <= nums[r] {
                continue;
            }

            // Perform removal of both l and r
            ops += 1;
            removed[l] = true;
            removed[r] = true;

            let ll = left[l];
            let rr = right[r];

            // Connect the remaining neighbors
            if let Some(ll_idx) = ll {
                right[ll_idx] = rr;
            }
            if let Some(rr_idx) = rr {
                left[rr_idx] = ll;
            }

            // Check new adjacent pair formed by ll and rr
            if let (Some(a), Some(b)) = (ll, rr) {
                if !removed[a] && !removed[b] && nums[a] > nums[b] {
                    let sum = nums[a] as i64 + nums[b] as i64;
                    heap.push(Reverse((sum, a)));
                }
            }
        }

        ops
    }
}
```

## Racket

```racket
(define/contract (minimum-pair-removal nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((arr (list->vector nums))
         (n (vector-length arr))
         (tails (make-vector n 0))
         (len 0))
    (define (upper-bound x)
      (let loop ((l 0) (r len))
        (if (= l r)
            l
            (let* ((mid (quotient (+ l r) 2))
                   (midval (vector-ref tails mid)))
              (if (> midval x)
                  (loop l mid)
                  (loop (+ mid 1) r))))))
    (for ([i (in-range n)])
      (let ((x (vector-ref arr i)))
        (let ((pos (upper-bound x)))
          (vector-set! tails pos x)
          (when (= pos len)
            (set! len (+ len 1))))))
    (- n len)))
```

## Erlang

```erlang
-spec minimum_pair_removal(Nums :: [integer()]) -> integer().
minimum_pair_removal(Nums) ->
    N = length(Nums),
    Sorted = lists:usort(Nums),
    M = length(Sorted),
    IndexMap = maps:from_list(lists:zip(Sorted, lists:seq(1, M))),
    {Best, _EvenBIT, _OddBIT} =
        lists:foldl(
            fun({Num, Pos}, {CurBest, EvenBIT, OddBIT}) ->
                Par = Pos rem 2,
                CompIdx = maps:get(Num, IndexMap),
                OppPar = 1 - Par,
                PrevMax = case OppPar of
                    0 -> bit_query(EvenBIT, CompIdx);
                    1 -> bit_query(OddBIT, CompIdx)
                end,
                DPStart = if Par == 0 -> 1; true -> 0 end,
                DP = case PrevMax of
                    0 -> DPStart;
                    _ -> max(PrevMax + 1, DPStart)
                end,
                {NewEvenBIT, NewOddBIT} =
                    if Par == 0 ->
                            {bit_update(EvenBIT, M, CompIdx, DP), OddBIT};
                       true ->
                            {EvenBIT, bit_update(OddBIT, M, CompIdx, DP)}
                    end,
                LastPar = (N - 1) rem 2,
                NewBest = if Par == LastPar -> max(CurBest, DP); true -> CurBest end,
                {NewBest, NewEvenBIT, NewOddBIT}
            end,
            {0, #{}, #{}},
            lists:zip(Nums, lists:seq(0, N - 1))
        ),
    (N - Best) div 2.

%% BIT query for maximum in prefix [1..Idx]
-spec bit_query(map(), integer()) -> integer().
bit_query(Map, Idx) ->
    bit_query(Map, Idx, 0).

-spec bit_query(map(), integer(), integer()) -> integer().
bit_query(_Map, 0, Acc) -> Acc;
bit_query(Map, Idx, Acc) ->
    Val = maps:get(Idx, Map, 0),
    NewAcc = if Val > Acc -> Val; true -> Acc end,
    bit_query(Map, Idx - (Idx band -Idx), NewAcc).

%% BIT update: set position Idx to max(old, Value)
-spec bit_update(map(), integer(), integer(), integer()) -> map().
bit_update(Map, Size, Idx, Value) when Idx =< Size ->
    Old = maps:get(Idx, Map, 0),
    UpdatedMap = if Value > Old -> maps:put(Idx, Value, Map); true -> Map end,
    bit_update(UpdatedMap, Size, Idx + (Idx band -Idx), Value);
bit_update(Map, _Size, Idx, _Value) when Idx > _Size ->
    Map.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_pair_removal(nums :: [integer]) :: integer
  def minimum_pair_removal(nums) do
    {len, _arr} =
      Enum.reduce(nums, {0, :array.from_list([])}, fn x, {len, arr} ->
        cond do
          len == 0 ->
            {1, :array.set(0, x, arr)}

          true ->
            idx = find_first_greater(arr, 0, len - 1, x)

            if idx == len do
              {len + 1, :array.set(len, x, arr)}
            else
              {len, :array.set(idx, x, arr)}
            end
        end
      end)

    length(nums) - len
  end

  defp find_first_greater(_arr, low, high, _x) when low > high, do: low

  defp find_first_greater(arr, low, high, x) do
    mid = div(low + high, 2)
    val = :array.get(mid, arr)

    if val > x do
      find_first_greater(arr, low, mid - 1, x)
    else
      find_first_greater(arr, mid + 1, high, x)
    end
  end
end
```
