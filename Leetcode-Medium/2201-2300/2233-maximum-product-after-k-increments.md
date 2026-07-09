# 2233. Maximum Product After K Increments

## Cpp

```cpp
class Solution {
public:
    int maximumProduct(vector<int>& nums, int k) {
        const long long MOD = 1000000007LL;
        priority_queue<long long, vector<long long>, greater<long long>> pq(nums.begin(), nums.end());
        while (k-- > 0) {
            long long x = pq.top();
            pq.pop();
            ++x;
            pq.push(x);
        }
        long long result = 1;
        while (!pq.empty()) {
            result = (result * (pq.top() % MOD)) % MOD;
            pq.pop();
        }
        return static_cast<int>(result);
    }
};
```

## Java

```java
class Solution {
    public int maximumProduct(int[] nums, int k) {
        final long MOD = 1_000_000_007L;
        java.util.PriorityQueue<Integer> pq = new java.util.PriorityQueue<>();
        for (int num : nums) {
            pq.offer(num);
        }
        for (int i = 0; i < k; i++) {
            int x = pq.poll();
            pq.offer(x + 1);
        }
        long result = 1L;
        while (!pq.isEmpty()) {
            result = (result * pq.poll()) % MOD;
        }
        return (int) result;
    }
}
```

## Python

```python
class Solution(object):
    def maximumProduct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        MOD = 10**9 + 7

        heap = list(nums)
        heapq.heapify(heap)

        for _ in range(k):
            x = heapq.heappop(heap)
            heapq.heappush(heap, x + 1)

        prod = 1
        while heap:
            prod = (prod * heapq.heappop(heap)) % MOD

        return prod
```

## Python3

```python
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        import heapq
        MOD = 10**9 + 7
        heap = nums[:]
        heapq.heapify(heap)
        for _ in range(k):
            x = heapq.heappop(heap)
            heapq.heappush(heap, x + 1)
        prod = 1
        while heap:
            prod = (prod * heapq.heappop(heap)) % MOD
        return prod
```

## C

```c
#include <stdlib.h>

#define MOD 1000000007LL

static void heapifyDown(int *heap, int n, int i) {
    while (1) {
        int left = 2 * i + 1;
        int right = left + 1;
        int smallest = i;
        if (left < n && heap[left] < heap[smallest]) smallest = left;
        if (right < n && heap[right] < heap[smallest]) smallest = right;
        if (smallest == i) break;
        int tmp = heap[i];
        heap[i] = heap[smallest];
        heap[smallest] = tmp;
        i = smallest;
    }
}

int maximumProduct(int* nums, int numsSize, int k) {
    int *heap = (int *)malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; ++i) heap[i] = nums[i];
    
    // Build min-heap
    for (int i = numsSize / 2 - 1; i >= 0; --i)
        heapifyDown(heap, numsSize, i);
    
    // Perform k increments on the smallest element each time
    for (int i = 0; i < k; ++i) {
        heap[0] += 1;
        heapifyDown(heap, numsSize, 0);
    }
    
    long long prod = 1LL;
    for (int i = 0; i < numsSize; ++i) {
        prod = (prod * (heap[i] % MOD)) % MOD;
    }
    
    free(heap);
    return (int)prod;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    private const long MOD = 1000000007L;
    public int MaximumProduct(int[] nums, int k) {
        var pq = new PriorityQueue<long, long>();
        foreach (var num in nums) {
            pq.Enqueue(num, num);
        }
        for (int i = 0; i < k; i++) {
            long x = pq.Dequeue();
            pq.Enqueue(x + 1, x + 1);
        }
        long product = 1;
        while (pq.Count > 0) {
            long val = pq.Dequeue() % MOD;
            product = (product * val) % MOD;
        }
        return (int)product;
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
var maximumProduct = function(nums, k) {
    const MOD = 1000000007n;
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
            const min = h[0];
            const last = h.pop();
            if (h.length > 0) {
                h[0] = last;
                let i = 0;
                while (true) {
                    let l = i * 2 + 1;
                    let r = l + 1;
                    let smallest = i;
                    if (l < h.length && h[l] < h[smallest]) smallest = l;
                    if (r < h.length && h[r] < h[smallest]) smallest = r;
                    if (smallest === i) break;
                    [h[i], h[smallest]] = [h[smallest], h[i]];
                    i = smallest;
                }
            }
            return min;
        }
    }

    const heap = new MinHeap();
    for (const v of nums) heap.push(v);

    for (let i = 0; i < k; ++i) {
        const x = heap.pop();
        heap.push(x + 1);
    }

    let result = 1n;
    while (heap.size() > 0) {
        result = (result * BigInt(heap.pop())) % MOD;
    }
    return Number(result);
};
```

## Typescript

```typescript
function maximumProduct(nums: number[], k: number): number {
    const MOD = 1000000007n;

    class MinHeap {
        data: number[] = [];
        size(): number { return this.data.length; }
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
            if (a.length) {
                a[0] = last;
                let i = 0;
                while (true) {
                    let l = i * 2 + 1;
                    let r = l + 1;
                    let smallest = i;
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
    for (const v of nums) heap.push(v);

    for (let i = 0; i < k; ++i) {
        const x = heap.pop();
        heap.push(x + 1);
    }

    let ans = 1n;
    for (const v of heap.data) {
        ans = (ans * BigInt(v)) % MOD;
    }
    return Number(ans);
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
    function maximumProduct($nums, $k) {
        $mod = 1000000007;
        $heap = new SplMinHeap();
        foreach ($nums as $v) {
            $heap->insert((int)$v);
        }
        for ($i = 0; $i < $k; $i++) {
            $minVal = $heap->extract();
            $heap->insert($minVal + 1);
        }
        $result = 1;
        while (!$heap->isEmpty()) {
            $val = $heap->extract();
            $result = ($result * ($val % $mod)) % $mod;
        }
        return (int)$result;
    }
}
```

## Swift

```swift
class Solution {
    func maximumProduct(_ nums: [Int], _ k: Int) -> Int {
        let MOD = 1_000_000_007
        var heap = MinHeap<Int>()
        for num in nums {
            heap.push(num)
        }
        var remaining = k
        while remaining > 0 {
            if let minVal = heap.pop() {
                heap.push(minVal + 1)
            }
            remaining -= 1
        }
        var result: Int64 = 1
        while !heap.isEmpty {
            if let val = heap.pop() {
                result = (result * Int64(val)) % Int64(MOD)
            }
        }
        return Int(result)
    }
}

struct MinHeap<T: Comparable> {
    private var elements: [T] = []
    
    var isEmpty: Bool { elements.isEmpty }
    
    mutating func push(_ value: T) {
        elements.append(value)
        siftUp(from: elements.count - 1)
    }
    
    mutating func pop() -> T? {
        guard !elements.isEmpty else { return nil }
        let value = elements[0]
        let last = elements.removeLast()
        if !elements.isEmpty {
            elements[0] = last
            siftDown(from: 0)
        }
        return value
    }
    
    private mutating func siftUp(from index: Int) {
        var child = index
        while child > 0 {
            let parent = (child - 1) / 2
            if elements[child] < elements[parent] {
                elements.swapAt(child, parent)
                child = parent
            } else {
                break
            }
        }
    }
    
    private mutating func siftDown(from index: Int) {
        var parent = index
        while true {
            let left = 2 * parent + 1
            let right = left + 1
            var smallest = parent
            if left < elements.count && elements[left] < elements[smallest] {
                smallest = left
            }
            if right < elements.count && elements[right] < elements[smallest] {
                smallest = right
            }
            if smallest == parent { break }
            elements.swapAt(parent, smallest)
            parent = smallest
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumProduct(nums: IntArray, k: Int): Int {
        val MOD = 1_000_000_007L
        val pq = java.util.PriorityQueue<Long>()
        for (num in nums) {
            pq.offer(num.toLong())
        }
        repeat(k) {
            val x = pq.poll()
            pq.offer(x + 1)
        }
        var result = 1L
        while (pq.isNotEmpty()) {
            result = result * (pq.poll() % MOD) % MOD
        }
        return result.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _MOD = 1000000007;
  int maximumProduct(List<int> nums, int k) {
    var heap = _MinHeap();
    for (var v in nums) {
      heap.push(v);
    }
    for (int i = 0; i < k; i++) {
      int smallest = heap.pop()!;
      heap.push(smallest + 1);
    }
    int result = 1;
    for (var v in heap.heap) {
      result = (result * v) % _MOD;
    }
    return result;
  }
}

class _MinHeap {
  List<int> heap = [];
  void push(int val) {
    heap.add(val);
    _siftUp(heap.length - 1);
  }

  int? pop() {
    if (heap.isEmpty) return null;
    int root = heap[0];
    int last = heap.removeLast();
    if (heap.isNotEmpty) {
      heap[0] = last;
      _siftDown(0);
    }
    return root;
  }

  void _siftUp(int idx) {
    while (idx > 0) {
      int parent = (idx - 1) >> 1;
      if (heap[parent] <= heap[idx]) break;
      _swap(parent, idx);
      idx = parent;
    }
  }

  void _siftDown(int idx) {
    int n = heap.length;
    while (true) {
      int left = idx * 2 + 1;
      int right = left + 1;
      int smallest = idx;
      if (left < n && heap[left] < heap[smallest]) smallest = left;
      if (right < n && heap[right] < heap[smallest]) smallest = right;
      if (smallest == idx) break;
      _swap(idx, smallest);
      idx = smallest;
    }
  }

  void _swap(int i, int j) {
    int tmp = heap[i];
    heap[i] = heap[j];
    heap[j] = tmp;
  }
}
```

## Golang

```go
package main

import (
	"container/heap"
)

const MOD int64 = 1000000007

type IntHeap []int64

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int64))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func maximumProduct(nums []int, k int) int {
	h := &IntHeap{}
	for _, v := range nums {
		*h = append(*h, int64(v))
	}
	heap.Init(h)

	for i := 0; i < k; i++ {
		x := heap.Pop(h).(int64)
		x++
		heap.Push(h, x)
	}

	var prod int64 = 1
	for h.Len() > 0 {
		val := heap.Pop(h).(int64) % MOD
		prod = (prod * val) % MOD
	}
	return int(prod)
}
```

## Ruby

```ruby
def sift_down(arr, i, n)
  loop do
    l = 2 * i + 1
    r = l + 1
    smallest = i
    if l < n && arr[l] < arr[smallest]
      smallest = l
    end
    if r < n && arr[r] < arr[smallest]
      smallest = r
    end
    break if smallest == i
    arr[i], arr[smallest] = arr[smallest], arr[i]
    i = smallest
  end
end

def maximum_product(nums, k)
  mod = 1_000_000_007
  heap = nums.dup
  n = heap.size

  # build min-heap
  i = (n / 2) - 1
  while i >= 0
    sift_down(heap, i, n)
    i -= 1
  end

  k.times do
    heap[0] += 1
    sift_down(heap, 0, n)
  end

  result = 1
  heap.each { |v| result = (result * v) % mod }
  result
end
```

## Scala

```scala
object Solution {
  private val MOD = 1000000007L
  def maximumProduct(nums: Array[Int], k: Int): Int = {
    import scala.collection.mutable.PriorityQueue
    val pq = PriorityQueue.empty[Int](Ordering[Int].reverse)
    nums.foreach(pq.enqueue(_))
    var ops = k
    while (ops > 0) {
      val x = pq.dequeue()
      pq.enqueue(x + 1)
      ops -= 1
    }
    var prod = 1L
    while (pq.nonEmpty) {
      val v = pq.dequeue()
      prod = (prod * (v % MOD)) % MOD
    }
    prod.toInt
  }
}
```

## Rust

```rust
use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn maximum_product(nums: Vec<i32>, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut heap: BinaryHeap<Reverse<i64>> = BinaryHeap::new();
        for &x in nums.iter() {
            heap.push(Reverse(x as i64));
        }
        let mut ops = k;
        while ops > 0 {
            if let Some(Reverse(mut smallest)) = heap.pop() {
                smallest += 1;
                heap.push(Reverse(smallest));
            }
            ops -= 1;
        }
        let mut prod: i64 = 1;
        while let Some(Reverse(val)) = heap.pop() {
            prod = ((prod as i128 * val as i128) % MOD as i128) as i64;
        }
        prod as i32
    }
}
```

## Racket

```racket
#lang racket
(require racket/heap)

(define MOD 1000000007)

(define/contract (maximum-product nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([h (make-heap <)])
    ;; insert initial numbers into the min‑heap
    (for ([n nums])
      (heap-insert! h n))
    ;; perform k increments, always on the smallest element
    (for ([i (in-range k)])
      (define min-val (heap-min h))
      (heap-remove-min! h)
      (heap-insert! h (+ min-val 1)))
    ;; compute the product modulo MOD
    (let loop ((prod 1))
      (if (heap-empty? h)
          prod
          (let ([val (heap-min h)])
            (heap-remove-min! h)
            (loop (modulo (* prod val) MOD)))))))
```

## Erlang

```erlang
-spec maximum_product(Nums :: [integer()], K :: integer()) -> integer().
maximum_product(Nums, K) ->
    Mod = 1000000007,
    Tree0 = build_tree(Nums),
    FinalTree = apply_increments(Tree0, K),
    product_mod(FinalTree, Mod).

build_tree(Nums) ->
    lists:foldl(fun(N, Acc) -> inc_key(Acc, N) end, gb_trees:new(), Nums).

apply_increments(Tree, 0) ->
    Tree;
apply_increments(Tree, K) ->
    {MinV, C} = gb_trees:smallest(Tree),
    Tree1 = case C of
        1 -> gb_trees:delete(MinV, Tree);
        _ -> gb_trees:update(MinV, C - 1, Tree)
    end,
    NewKey = MinV + 1,
    Tree2 = inc_key(Tree1, NewKey),
    apply_increments(Tree2, K - 1).

inc_key(Tree, Key) ->
    case gb_trees:lookup(Key, Tree) of
        {value, V} -> gb_trees:update(Key, V + 1, Tree);
        none -> gb_trees:insert(Key, 1, Tree)
    end.

product_mod(Tree, Mod) ->
    gb_trees:fold(fun(Key, Count, Acc) ->
        (Acc * pow_mod(Key rem Mod, Count, Mod)) rem Mod
    end, 1, Tree).

pow_mod(_, 0, _) -> 1;
pow_mod(Base, Exp, Mod) when Exp band 1 =:= 1 ->
    (Base * pow_mod((Base * Base) rem Mod, Exp bsr 1, Mod)) rem Mod;
pow_mod(Base, Exp, Mod) ->
    pow_mod((Base * Base) rem Mod, Exp bsr 1, Mod).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_product(nums :: [integer], k :: integer) :: integer
  def maximum_product(nums, k) do
    mod = 1_000_000_007

    tree =
      Enum.reduce(nums, :gb_trees.empty(), fn x, acc ->
        case :gb_trees.lookup(x, acc) do
          {:value, cnt} -> :gb_trees.update(x, cnt + 1, acc)
          :none -> :gb_trees.insert(x, 1, acc)
        end
      end)

    final_tree =
      Enum.reduce(1..k, tree, fn _, acc ->
        {min_key, cnt} = :gb_trees.smallest(acc)

        acc2 =
          if cnt == 1 do
            :gb_trees.delete(min_key, acc)
          else
            :gb_trees.update(min_key, cnt - 1, acc)
          end

        new_val = min_key + 1

        case :gb_trees.lookup(new_val, acc2) do
          {:value, c} -> :gb_trees.update(new_val, c + 1, acc2)
          :none -> :gb_trees.insert(new_val, 1, acc2)
        end
      end)

    :gb_trees.fold(
      fn key, cnt, prod ->
        rem(prod * pow_mod(key, cnt, mod), mod)
      end,
      1,
      final_tree
    )
  end

  defp pow_mod(_base, 0, _mod), do: 1

  defp pow_mod(base, exp, mod) do
    base = rem(base, mod)
    do_pow(base, exp, mod, 1)
  end

  defp do_pow(_base, 0, _mod, acc), do: acc

  defp do_pow(base, exp, mod, acc) when rem(exp, 2) == 1 do
    new_acc = rem(acc * base, mod)
    new_base = rem(base * base, mod)
    do_pow(new_base, div(exp, 2), mod, new_acc)
  end

  defp do_pow(base, exp, mod, acc) do
    new_base = rem(base * base, mod)
    do_pow(new_base, div(exp, 2), mod, acc)
  end
end
```
