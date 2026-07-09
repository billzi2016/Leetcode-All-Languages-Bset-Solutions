# 1046. Last Stone Weight

## Cpp

```cpp
class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> pq(stones.begin(), stones.end());
        while (pq.size() > 1) {
            int y = pq.top(); pq.pop();
            int x = pq.top(); pq.pop();
            if (x != y) pq.push(y - x);
        }
        return pq.empty() ? 0 : pq.top();
    }
};
```

## Java

```java
class Solution {
    public int lastStoneWeight(int[] stones) {
        java.util.PriorityQueue<Integer> maxHeap = new java.util.PriorityQueue<>(java.util.Collections.reverseOrder());
        for (int stone : stones) {
            maxHeap.offer(stone);
        }
        while (maxHeap.size() > 1) {
            int y = maxHeap.poll();
            int x = maxHeap.poll();
            if (x != y) {
                maxHeap.offer(y - x);
            }
        }
        return maxHeap.isEmpty() ? 0 : maxHeap.peek();
    }
}
```

## Python

```python
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        import heapq
        # Use a max-heap by inserting negative values
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            y = -heapq.heappop(max_heap)  # heaviest
            x = -heapq.heappop(max_heap)  # second heaviest
            if x != y:
                heapq.heappush(max_heap, -(y - x))
        return -max_heap[0] if max_heap else 0
```

## Python3

```python
from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Use a max-heap by storing negative values
        heap = [-s for s in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            y = -heapq.heappop(heap)  # heaviest
            x = -heapq.heappop(heap)  # second heaviest
            if y != x:
                heapq.heappush(heap, -(y - x))
        
        return -heap[0] if heap else 0
```

## C

```c
int lastStoneWeight(int* stones, int stonesSize) {
    if (stonesSize == 0) return 0;
    // heap array uses the same buffer as stones
    int heapSize = stonesSize;

    // Build max-heap
    for (int i = (heapSize / 2) - 1; i >= 0; --i) {
        int idx = i;
        while (1) {
            int left = 2 * idx + 1;
            int right = left + 1;
            int largest = idx;
            if (left < heapSize && stones[left] > stones[largest]) largest = left;
            if (right < heapSize && stones[right] > stones[largest]) largest = right;
            if (largest == idx) break;
            int tmp = stones[idx];
            stones[idx] = stones[largest];
            stones[largest] = tmp;
            idx = largest;
        }
    }

    // Helper lambdas as static functions
    void siftUp(int *heap, int size, int i) {
        while (i > 0) {
            int p = (i - 1) / 2;
            if (heap[p] >= heap[i]) break;
            int tmp = heap[p];
            heap[p] = heap[i];
            heap[i] = tmp;
            i = p;
        }
    }

    void siftDown(int *heap, int size, int i) {
        while (1) {
            int left = 2 * i + 1;
            int right = left + 1;
            int largest = i;
            if (left < size && heap[left] > heap[largest]) largest = left;
            if (right < size && heap[right] > heap[largest]) largest = right;
            if (largest == i) break;
            int tmp = heap[i];
            heap[i] = heap[largest];
            heap[largest] = tmp;
            i = largest;
        }
    }

    // Pop max
    int popMax(int *heap, int *size) {
        int top = heap[0];
        (*size)--;
        if (*size > 0) {
            heap[0] = heap[*size];
            siftDown(heap, *size, 0);
        }
        return top;
    }

    // Push value
    void push(int *heap, int *size, int val) {
        heap[*size] = val;
        (*size)++;
        siftUp(heap, *size, *size - 1);
    }

    while (heapSize > 1) {
        int y = popMax(stones, &heapSize); // heaviest
        int x = popMax(stones, &heapSize); // second heaviest
        if (x != y) {
            push(stones, &heapSize, y - x);
        }
    }

    return heapSize == 1 ? stones[0] : 0;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int LastStoneWeight(int[] stones) {
        var pq = new PriorityQueue<int, int>();
        foreach (var s in stones) {
            pq.Enqueue(s, -s);
        }
        while (pq.Count > 1) {
            int y = pq.Dequeue(); // heaviest
            int x = pq.Dequeue(); // second heaviest
            if (x != y) {
                int diff = y - x;
                pq.Enqueue(diff, -diff);
            }
        }
        return pq.Count == 0 ? 0 : pq.Peek();
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} stones
 * @return {number}
 */
var lastStoneWeight = function(stones) {
    while (stones.length > 1) {
        stones.sort((a, b) => a - b);
        const y = stones.pop();
        const x = stones.pop();
        if (y !== x) {
            stones.push(y - x);
        }
    }
    return stones[0] || 0;
};
```

## Typescript

```typescript
function lastStoneWeight(stones: number[]): number {
    while (stones.length > 1) {
        stones.sort((a, b) => b - a);
        const y = stones.shift()!; // heaviest
        const x = stones.shift()!; // second heaviest
        if (x !== y) {
            stones.push(y - x);
        }
    }
    return stones.length === 0 ? 0 : stones[0];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $stones
     * @return Integer
     */
    function lastStoneWeight($stones) {
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        foreach ($stones as $s) {
            $pq->insert($s, $s);
        }
        while ($pq->count() > 1) {
            $y = $pq->extract(); // heaviest
            $x = $pq->extract(); // second heaviest
            if ($y != $x) {
                $diff = $y - $x;
                $pq->insert($diff, $diff);
            }
        }
        return $pq->count() === 1 ? $pq->extract() : 0;
    }
}
```

## Swift

```swift
class Solution {
    func lastStoneWeight(_ stones: [Int]) -> Int {
        var heap = stones
        while heap.count > 1 {
            heap.sort(by: >)
            let y = heap.removeFirst()
            let x = heap.removeFirst()
            if x != y {
                heap.append(y - x)
            }
        }
        return heap.first ?? 0
    }
}
```

## Kotlin

```kotlin
import java.util.PriorityQueue
import java.util.Collections

class Solution {
    fun lastStoneWeight(stones: IntArray): Int {
        val pq = PriorityQueue<Int>(Collections.reverseOrder())
        for (s in stones) {
            pq.add(s)
        }
        while (pq.size > 1) {
            val y = pq.poll()
            val x = pq.poll()
            if (x != y) {
                pq.add(y - x)
            }
        }
        return if (pq.isEmpty()) 0 else pq.peek()
    }
}
```

## Dart

```dart
class Solution {
  int lastStoneWeight(List<int> stones) {
    while (stones.length > 1) {
      stones.sort((a, b) => b - a);
      int y = stones[0];
      int x = stones[1];
      stones.removeRange(0, 2);
      if (y != x) {
        stones.add(y - x);
      }
    }
    return stones.isEmpty ? 0 : stones[0];
  }
}
```

## Golang

```go
import (
	"container/heap"
)

type maxHeap []int

func (h maxHeap) Len() int           { return len(h) }
func (h maxHeap) Less(i, j int) bool { return h[i] > h[j] } // max-heap
func (h maxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *maxHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *maxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func lastStoneWeight(stones []int) int {
	h := &maxHeap{}
	heap.Init(h)
	for _, s := range stones {
		heap.Push(h, s)
	}
	for h.Len() > 1 {
		y := heap.Pop(h).(int) // heaviest
		x := heap.Pop(h).(int) // second heaviest
		if x != y {
			heap.Push(h, y-x)
		}
	}
	if h.Len() == 0 {
		return 0
	}
	return (*h)[0]
}
```

## Ruby

```ruby
# @param {Integer[]} stones
# @return {Integer}
def last_stone_weight(stones)
  while stones.size > 1
    stones.sort!
    y = stones.pop
    x = stones.pop
    stones << (y - x) if x != y
  end
  stones.empty? ? 0 : stones[0]
end
```

## Scala

```scala
import java.util.PriorityQueue
import java.util.Collections

object Solution {
  def lastStoneWeight(stones: Array[Int]): Int = {
    val pq = new PriorityQueue[Int](Collections.reverseOrder[Int]())
    stones.foreach(pq.add)
    while (pq.size() > 1) {
      val y = pq.poll()
      val x = pq.poll()
      if (y != x) pq.add(y - x)
    }
    if (pq.isEmpty) 0 else pq.peek()
  }
}
```

## Rust

```rust
impl Solution {
    pub fn last_stone_weight(stones: Vec<i32>) -> i32 {
        use std::collections::BinaryHeap;
        let mut heap = BinaryHeap::from(stones);
        while heap.len() > 1 {
            let y = heap.pop().unwrap();
            let x = heap.pop().unwrap();
            if y != x {
                heap.push(y - x);
            }
        }
        heap.pop().unwrap_or(0)
    }
}
```

## Racket

```racket
(define/contract (last-stone-weight stones)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((lst stones))
    (cond
      [(null? lst) 0]
      [(null? (cdr lst)) (car lst)]
      [else
       (define sorted (sort lst >))
       (define y (first sorted))
       (define x (second sorted))
       (define rest (cddr sorted))
       (if (= x y)
           (loop rest)
           (loop (cons (- y x) rest)))])))
```

## Erlang

```erlang
-spec last_stone_weight(Stones :: [integer()]) -> integer().
last_stone_weight([]) ->
    0;
last_stone_weight([X]) ->
    X;
last_stone_weight(Stones) ->
    Sorted = lists:sort(Stones),
    case lists:reverse(Sorted) of
        [Y, X | Rest] ->
            Diff = Y - X,
            NewList = if Diff == 0 -> Rest; true -> [Diff | Rest] end,
            last_stone_weight(NewList);
        _ ->
            %% This case occurs when there is only one element after sorting.
            case Sorted of
                [] -> 0;
                [Only] -> Only
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec last_stone_weight(stones :: [integer]) :: integer
  def last_stone_weight(stones) do
    stones
    |> Enum.sort(&>=/2)
    |> reduce()
  end

  defp reduce([]), do: 0
  defp reduce([x]), do: x
  defp reduce([x, y | rest]) do
    if x == y do
      reduce(Enum.sort(rest, &>=/2))
    else
      diff = x - y
      reduce(Enum.sort([diff | rest], &>=/2))
    end
  end
end
```
