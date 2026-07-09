# 3264. Final Array State After K Multiplication Operations I

## Cpp

```cpp
class Solution {
public:
    vector<int> getFinalState(vector<int>& nums, int k, int multiplier) {
        using P = pair<long long,int>;
        priority_queue<P, vector<P>, greater<P>> pq;
        for (int i = 0; i < (int)nums.size(); ++i) {
            pq.emplace(nums[i], i);
        }
        while (k--) {
            auto [val, idx] = pq.top();
            pq.pop();
            val *= multiplier;
            nums[idx] = static_cast<int>(val);
            pq.emplace(val, idx);
        }
        return nums;
    }
};
```

## Java

```java
class Solution {
    public int[] getFinalState(int[] nums, int k, int multiplier) {
        java.util.PriorityQueue<int[]> pq = new java.util.PriorityQueue<>(
            (a, b) -> a[0] != b[0] ? Integer.compare(a[0], b[0]) : Integer.compare(a[1], b[1])
        );
        for (int i = 0; i < nums.length; i++) {
            pq.offer(new int[]{nums[i], i});
        }
        while (k-- > 0) {
            int[] cur = pq.poll();
            int idx = cur[1];
            nums[idx] *= multiplier;
            pq.offer(new int[]{nums[idx], idx});
        }
        return nums;
    }
}
```

## Python

```python
class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        import heapq
        # Build a min-heap of (value, index) to break ties by smallest index
        heap = [(nums[i], i) for i in range(len(nums))]
        heapq.heapify(heap)

        for _ in range(k):
            val, idx = heapq.heappop(heap)
            new_val = val * multiplier
            nums[idx] = new_val
            heapq.heappush(heap, (new_val, idx))

        return nums
```

## Python3

```python
from typing import List
import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(nums[i], i) for i in range(len(nums))]
        heapq.heapify(heap)
        for _ in range(k):
            val, idx = heapq.heappop(heap)
            new_val = val * multiplier
            nums[idx] = new_val
            heapq.heappush(heap, (new_val, idx))
        return nums
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getFinalState(int* nums, int numsSize, int k, int multiplier, int* returnSize) {
    int *res = (int*)malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; ++i) {
        res[i] = nums[i];
    }
    
    for (int op = 0; op < k; ++op) {
        int minIdx = 0;
        for (int i = 1; i < numsSize; ++i) {
            if (res[i] < res[minIdx]) {
                minIdx = i;
            }
        }
        long long prod = (long long)res[minIdx] * multiplier;
        res[minIdx] = (int)prod;
    }
    
    *returnSize = numsSize;
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public int[] GetFinalState(int[] nums, int k, int multiplier) {
        int n = nums.Length;
        for (int op = 0; op < k; ++op) {
            int minIdx = 0;
            for (int i = 1; i < n; ++i) {
                if (nums[i] < nums[minIdx]) {
                    minIdx = i;
                }
            }
            long newVal = (long)nums[minIdx] * multiplier;
            nums[minIdx] = (int)newVal;
        }
        return nums;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number} multiplier
 * @return {number[]}
 */
var getFinalState = function(nums, k, multiplier) {
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
            this.heap.push(node);
            this._siftUp(this.heap.length - 1);
        }
        pop() {
            if (this.heap.length === 0) return null;
            const min = this.heap[0];
            const last = this.heap.pop();
            if (this.heap.length > 0) {
                this.heap[0] = last;
                this._siftDown(0);
            }
            return min;
        }
        _compare(a, b) {
            // true if a should be above b
            if (a.val !== b.val) return a.val < b.val;
            return a.idx < b.idx;
        }
        _siftUp(i) {
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (!this._compare(this.heap[i], this.heap[p])) break;
                [this.heap[i], this.heap[p]] = [this.heap[p], this.heap[i]];
                i = p;
            }
        }
        _siftDown(i) {
            const n = this.heap.length;
            while (true) {
                let left = i * 2 + 1;
                let right = i * 2 + 2;
                let smallest = i;

                if (left < n && this._compare(this.heap[left], this.heap[smallest])) {
                    smallest = left;
                }
                if (right < n && this._compare(this.heap[right], this.heap[smallest])) {
                    smallest = right;
                }
                if (smallest === i) break;
                [this.heap[i], this.heap[smallest]] = [this.heap[smallest], this.heap[i]];
                i = smallest;
            }
        }
    }

    const heap = new MinHeap();
    for (let i = 0; i < nums.length; ++i) {
        heap.push({ val: nums[i], idx: i });
    }

    for (let op = 0; op < k; ++op) {
        const node = heap.pop(); // smallest
        const newVal = node.val * multiplier;
        nums[node.idx] = newVal;
        heap.push({ val: newVal, idx: node.idx });
    }

    return nums;
};
```

## Typescript

```typescript
function getFinalState(nums: number[], k: number, multiplier: number): number[] {
    class MinHeap {
        private data: { val: number; idx: number }[] = [];
        private swap(i: number, j: number) {
            const tmp = this.data[i];
            this.data[i] = this.data[j];
            this.data[j] = tmp;
        }
        private less(a: { val: number; idx: number }, b: { val: number; idx: number }) {
            if (a.val !== b.val) return a.val < b.val;
            return a.idx < b.idx;
        }
        push(item: { val: number; idx: number }) {
            this.data.push(item);
            let i = this.data.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (this.less(this.data[i], this.data[p])) {
                    this.swap(i, p);
                    i = p;
                } else break;
            }
        }
        pop(): { val: number; idx: number } {
            const top = this.data[0];
            const last = this.data.pop()!;
            if (this.data.length) {
                this.data[0] = last;
                let i = 0;
                while (true) {
                    let l = i * 2 + 1,
                        r = l + 1,
                        smallest = i;
                    if (l < this.data.length && this.less(this.data[l], this.data[smallest])) smallest = l;
                    if (r < this.data.length && this.less(this.data[r], this.data[smallest])) smallest = r;
                    if (smallest !== i) {
                        this.swap(i, smallest);
                        i = smallest;
                    } else break;
                }
            }
            return top;
        }
    }

    const heap = new MinHeap();
    for (let i = 0; i < nums.length; ++i) heap.push({ val: nums[i], idx: i });

    for (let op = 0; op < k; ++op) {
        const node = heap.pop();
        const newVal = node.val * multiplier;
        nums[node.idx] = newVal;
        heap.push({ val: newVal, idx: node.idx });
    }
    return nums;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @param Integer $multiplier
     * @return Integer[]
     */
    function getFinalState($nums, $k, $multiplier) {
        $n = count($nums);
        for ($op = 0; $op < $k; $op++) {
            $minIdx = 0;
            for ($i = 1; $i < $n; $i++) {
                if ($nums[$i] < $nums[$minIdx]) {
                    $minIdx = $i;
                }
            }
            $nums[$minIdx] *= $multiplier;
        }
        return $nums;
    }
}
```

## Swift

```swift
class Solution {
    func getFinalState(_ nums: [Int], _ k: Int, _ multiplier: Int) -> [Int] {
        var arr = nums
        let n = arr.count
        for _ in 0..<k {
            var minIdx = 0
            for i in 1..<n {
                if arr[i] < arr[minIdx] {
                    minIdx = i
                }
            }
            arr[minIdx] *= multiplier
        }
        return arr
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getFinalState(nums: IntArray, k: Int, multiplier: Int): IntArray {
        val pq = java.util.PriorityQueue<Pair<Int, Int>>(compareBy<Pair<Int, Int>> { it.first }.thenBy { it.second })
        for (i in nums.indices) {
            pq.offer(Pair(nums[i], i))
        }
        repeat(k) {
            var cur = pq.poll()
            while (cur.first != nums[cur.second]) {
                cur = pq.poll()
            }
            val newVal = cur.first * multiplier
            nums[cur.second] = newVal
            pq.offer(Pair(newVal, cur.second))
        }
        return nums
    }
}
```

## Dart

```dart
class Solution {
  List<int> getFinalState(List<int> nums, int k, int multiplier) {
    for (int op = 0; op < k; ++op) {
      int minIdx = 0;
      for (int i = 1; i < nums.length; ++i) {
        if (nums[i] < nums[minIdx]) {
          minIdx = i;
        }
      }
      nums[minIdx] *= multiplier;
    }
    return nums;
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

func (h minHeap) Len() int { return len(h) }
func (h minHeap) Less(i, j int) bool {
	if h[i].val == h[j].val {
		return h[i].idx < h[j].idx
	}
	return h[i].val < h[j].val
}
func (h minHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *minHeap) Push(x interface{}) {
	*h = append(*h, x.(item))
}

func (h *minHeap) Pop() interface{} {
	old := *h
	n := len(old)
	it := old[n-1]
	*h = old[:n-1]
	return it
}

func getFinalState(nums []int, k int, multiplier int) []int {
	h := make(minHeap, len(nums))
	for i, v := range nums {
		h[i] = item{val: v, idx: i}
	}
	heap.Init(&h)

	for i := 0; i < k; i++ {
		it := heap.Pop(&h).(item)
		newVal := it.val * multiplier
		nums[it.idx] = newVal
		it.val = newVal
		heap.Push(&h, it)
	}
	return nums
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} multiplier
# @return {Integer[]}
def get_final_state(nums, k, multiplier)
  k.times do
    min_idx = 0
    min_val = nums[0]
    nums.each_with_index do |val, idx|
      if val < min_val
        min_val = val
        min_idx = idx
      end
    end
    nums[min_idx] *= multiplier
  end
  nums
end
```

## Scala

```scala
import java.util.{Comparator, PriorityQueue}

object Solution {
  def getFinalState(nums: Array[Int], k: Int, multiplier: Int): Array[Int] = {
    val cmp = new Comparator[(Int, Int)] {
      override def compare(a: (Int, Int), b: (Int, Int)): Int = {
        if (a._1 != b._1) Integer.compare(a._1, b._1)
        else Integer.compare(a._2, b._2)
      }
    }
    val pq = new PriorityQueue[(Int, Int)](cmp)

    for (i <- nums.indices) {
      pq.offer((nums(i), i))
    }

    var remaining = k
    while (remaining > 0) {
      val (value, idx) = pq.poll()
      val newVal = value * multiplier
      nums(idx) = newVal
      pq.offer((newVal, idx))
      remaining -= 1
    }
    nums
  }
}
```

## Rust

```rust
use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn get_final_state(nums: Vec<i32>, k: i32, multiplier: i32) -> Vec<i32> {
        let mut arr = nums.clone();
        let n = arr.len();
        let mut heap: BinaryHeap<Reverse<(i32, usize)>> = BinaryHeap::with_capacity(n);
        for i in 0..n {
            heap.push(Reverse((arr[i], i)));
        }

        for _ in 0..k as usize {
            if let Some(Reverse((_val, idx))) = heap.pop() {
                let new_val = arr[idx] * multiplier;
                arr[idx] = new_val;
                heap.push(Reverse((new_val, idx)));
            }
        }

        arr
    }
}
```

## Racket

```racket
(require racket/list)

(define/contract (get-final-state nums k multiplier)
  (-> (listof exact-integer?) exact-integer? exact-integer? (listof exact-integer?))
  (let loop ((arr nums) (rem k))
    (if (= rem 0)
        arr
        (let* ((min-val (apply min arr))
               (idx (let find ((lst arr) (i 0))
                      (cond [(null? lst) -1]
                            [(= (car lst) min-val) i]
                            [else (find (cdr lst) (+ i 1))])))
               (new-arr (list-set arr idx (* min-val multiplier))))
          (loop new-arr (- rem 1))))))
```

## Erlang

```erlang
-spec get_final_state([integer()], integer(), integer()) -> [integer()].
get_final_state(Nums, K, Multiplier) ->
    loop(K, Nums, Multiplier).

loop(0, List, _) -> List;
loop(K, List, M) when K > 0 ->
    {Idx, MinVal} = find_min(List),
    NewVal = MinVal * M,
    Updated = replace_nth(Idx, NewVal, List),
    loop(K - 1, Updated, M).

replace_nth(1, New, [_|Tail]) -> [New | Tail];
replace_nth(N, New, [H|Tail]) when N > 1 ->
    [H | replace_nth(N - 1, New, Tail)].

find_min([H|T]) ->
    find_min(T, H, 1, 2).

find_min([], Min, Idx, _) -> {Idx, Min};
find_min([H|T], Min, Idx, Pos) ->
    if
        H < Min ->
            find_min(T, H, Pos, Pos + 1);
        true ->
            find_min(T, Min, Idx, Pos + 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec get_final_state(nums :: [integer], k :: integer, multiplier :: integer) :: [integer]
  def get_final_state(nums, k, multiplier) do
    apply_ops(nums, k, multiplier)
  end

  defp apply_ops(nums, 0, _multiplier), do: nums

  defp apply_ops(nums, k, multiplier) when k > 0 do
    {min_val, min_idx} =
      nums
      |> Enum.with_index()
      |> Enum.min_by(fn {val, idx} -> {val, idx} end)

    new_val = min_val * multiplier
    new_nums = List.replace_at(nums, min_idx, new_val)
    apply_ops(new_nums, k - 1, multiplier)
  end
end
```
