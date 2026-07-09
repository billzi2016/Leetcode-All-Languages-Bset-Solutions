# 2454. Next Greater Element IV

## Cpp

```cpp
class Solution {
public:
    vector<int> secondGreaterElement(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n, -1);
        stack<int> st; // indices waiting for first greater
        using P = pair<int,int>;
        priority_queue<P, vector<P>, greater<P>> pq; // (value, index) waiting for second greater
        
        for (int i = 0; i < n; ++i) {
            int cur = nums[i];
            
            // Resolve second greater candidates
            while (!pq.empty() && pq.top().first < cur) {
                auto [val, idx] = pq.top();
                pq.pop();
                ans[idx] = cur;
            }
            
            // Find first greater for indices in stack
            vector<int> moved;
            while (!st.empty() && nums[st.top()] < cur) {
                moved.push_back(st.top());
                st.pop();
            }
            // Those indices now wait for their second greater
            for (int idx : moved) {
                pq.emplace(nums[idx], idx);
            }
            
            // Current index may serve as first greater for future elements
            st.push(i);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] secondGreaterElement(int[] nums) {
        int n = nums.length;
        int[] answer = new int[n];
        java.util.Arrays.fill(answer, -1);
        java.util.Deque<Integer> firstStack = new java.util.ArrayDeque<>();
        java.util.Deque<Integer> secondStack = new java.util.ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            // Resolve second greater elements
            while (!secondStack.isEmpty() && nums[i] > nums[secondStack.peekLast()]) {
                answer[secondStack.pollLast()] = nums[i];
            }

            // Move indices that have found their first greater to second stack
            java.util.List<Integer> moved = new java.util.ArrayList<>();
            while (!firstStack.isEmpty() && nums[i] > nums[firstStack.peekLast()]) {
                moved.add(firstStack.pollLast());
            }
            for (int j = moved.size() - 1; j >= 0; --j) {
                secondStack.addLast(moved.get(j));
            }

            // Current index waits for its first greater
            firstStack.addLast(i);
        }
        return answer;
    }
}
```

## Python

```python
import heapq

class Solution(object):
    def secondGreaterElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [-1] * n
        stack = []          # indices waiting for first greater
        heap = []           # (original value, index) waiting for second greater

        for i, val in enumerate(nums):
            # Resolve second greater elements
            while heap and val > heap[0][0]:
                _, idx = heapq.heappop(heap)
                answer[idx] = val

            # Resolve first greater elements
            while stack and val > nums[stack[-1]]:
                idx = stack.pop()
                heapq.heappush(heap, (nums[idx], idx))

            stack.append(i)

        return answer
```

## Python3

```python
import heapq
from typing import List

class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []          # monotonic decreasing stack of indices waiting for first greater
        wait = []           # min-heap of (original value, index) waiting for second greater

        for i, x in enumerate(nums):
            # Resolve second greater candidates
            while wait and x > wait[0][0]:
                _, idx = heapq.heappop(wait)
                ans[idx] = x

            # Find first greater for indices in stack
            while stack and x > nums[stack[-1]]:
                idx = stack.pop()
                heapq.heappush(wait, (nums[idx], idx))

            stack.append(i)

        return ans
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* secondGreaterElement(int* nums, int numsSize, int* returnSize) {
    int *ans = (int *)malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; ++i) ans[i] = -1;
    *returnSize = numsSize;

    int *stack1 = (int *)malloc(numsSize * sizeof(int));
    int top1 = 0;
    int *stack2 = (int *)malloc(numsSize * sizeof(int));
    int top2 = 0;

    for (int i = 0; i < numsSize; ++i) {
        while (top2 > 0 && nums[i] > nums[stack2[top2 - 1]]) {
            int idx = stack2[--top2];
            ans[idx] = nums[i];
        }
        while (top1 > 0 && nums[i] > nums[stack1[top1 - 1]]) {
            int idx = stack1[--top1];
            stack2[top2++] = idx;
        }
        stack1[top1++] = i;
    }

    free(stack1);
    free(stack2);
    return ans;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int[] SecondGreaterElement(int[] nums) {
        int n = nums.Length;
        int[] answer = new int[n];
        for (int i = 0; i < n; i++) answer[i] = -1;

        Stack<int> firstStack = new Stack<int>();
        var secondHeap = new PriorityQueue<int, int>(); // element: index, priority: nums[index]

        for (int i = 0; i < n; i++) {
            while (secondHeap.Count > 0 && nums[secondHeap.Peek()] < nums[i]) {
                int idx = secondHeap.Dequeue();
                answer[idx] = nums[i];
            }

            while (firstStack.Count > 0 && nums[firstStack.Peek()] < nums[i]) {
                int idx = firstStack.Pop();
                secondHeap.Enqueue(idx, nums[idx]);
            }

            firstStack.Push(i);
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var secondGreaterElement = function(nums) {
    const n = nums.length;
    const ans = new Array(n).fill(-1);
    const firstStack = []; // indices waiting for first greater (decreasing by value)
    const secondStack = []; // indices waiting for second greater (decreasing by original value)

    for (let i = 0; i < n; ++i) {
        // Resolve second greater for those already in secondStack
        while (secondStack.length && nums[i] > nums[secondStack[secondStack.length - 1]]) {
            const idx = secondStack.pop();
            ans[idx] = nums[i];
        }

        // Find first greater for indices in firstStack
        const moved = [];
        while (firstStack.length && nums[i] > nums[firstStack[firstStack.length - 1]]) {
            moved.push(firstStack.pop());
        }
        // Move them to secondStack preserving decreasing order (smallest on top)
        for (let j = moved.length - 1; j >= 0; --j) {
            secondStack.push(moved[j]);
        }

        // Current index may serve as first greater for future elements
        firstStack.push(i);
    }
    return ans;
};
```

## Typescript

```typescript
function secondGreaterElement(nums: number[]): number[] {
    const n = nums.length;
    const answer = new Array<number>(n).fill(-1);
    const stack1: number[] = []; // waiting for first greater
    const stack2: number[] = []; // waiting for second greater

    for (let i = 0; i < n; ++i) {
        // Resolve second greater candidates
        while (stack2.length && nums[i] > nums[stack2[stack2.length - 1]]) {
            const idx = stack2.pop()!;
            answer[idx] = nums[i];
        }

        // Find first greater for indices in stack1
        const moved: number[] = [];
        while (stack1.length && nums[i] > nums[stack1[stack1.length - 1]]) {
            moved.push(stack1.pop()!);
        }
        // Those indices now wait for their second greater; push onto stack2 preserving decreasing order
        for (let k = moved.length - 1; k >= 0; --k) {
            stack2.push(moved[k]);
        }

        // Current index may become first greater for future elements
        stack1.push(i);
    }

    return answer;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function secondGreaterElement($nums) {
        $n = count($nums);
        $ans = array_fill(0, $n, -1);
        $stack = []; // indices waiting for first greater

        $heap = new SplPriorityQueue(); // min-heap based on original value
        $heap->setExtractFlags(SplPriorityQueue::EXTR_BOTH);

        for ($i = 0; $i < $n; $i++) {
            $cur = $nums[$i];

            // Resolve second greater elements
            while (!$heap->isEmpty()) {
                $top = $heap->current();
                $val = -$top['priority']; // original value of the index
                if ($val < $cur) {
                    $idx = $top['data'];
                    $ans[$idx] = $cur;
                    $heap->extract();
                } else {
                    break;
                }
            }

            // Resolve first greater elements and move them to heap
            while (!empty($stack) && $nums[end($stack)] < $cur) {
                $idx = array_pop($stack);
                $heap->insert($idx, -$nums[$idx]); // negative for min-heap behavior
            }

            // Current index may serve as first greater for future elements
            $stack[] = $i;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func secondGreaterElement(_ nums: [Int]) -> [Int] {
        let n = nums.count
        var answer = Array(repeating: -1, count: n)
        var firstStack = [Int]()   // indices waiting for first greater
        var secondStack = [Int]()  // indices waiting for second greater
        
        for i in 0..<n {
            // Resolve second greater for candidates in secondStack
            while let lastIdx = secondStack.last, nums[i] > nums[lastIdx] {
                answer[secondStack.removeLast()] = nums[i]
            }
            
            // Move indices that found their first greater from firstStack to secondStack
            var moved = [Int]()
            while let lastIdx = firstStack.last, nums[i] > nums[lastIdx] {
                moved.append(firstStack.removeLast())
            }
            // Push onto secondStack in reverse order to maintain decreasing values
            for idx in moved.reversed() {
                secondStack.append(idx)
            }
            
            // Current index waits for its first greater
            firstStack.append(i)
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun secondGreaterElement(nums: IntArray): IntArray {
        val n = nums.size
        val answer = IntArray(n) { -1 }
        val firstStack = java.util.ArrayDeque<Int>()
        val heap = java.util.PriorityQueue<Pair<Int, Int>>(compareBy { it.first })
        for (i in 0 until n) {
            val cur = nums[i]
            while (!heap.isEmpty() && heap.peek().first < cur) {
                val idx = heap.poll().second
                answer[idx] = cur
            }
            while (!firstStack.isEmpty() && nums[firstStack.peekLast()] < cur) {
                val idx = firstStack.removeLast()
                heap.add(Pair(nums[idx], idx))
            }
            firstStack.addLast(i)
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  List<int> secondGreaterElement(List<int> nums) {
    int n = nums.length;
    List<int> ans = List.filled(n, -1);
    List<int> firstStack = []; // waiting for first greater
    List<int> secondStack = []; // waiting for second greater

    for (int i = 0; i < n; ++i) {
      // Resolve second greater elements
      while (secondStack.isNotEmpty && nums[i] > nums[secondStack.last]) {
        int idx = secondStack.removeLast();
        ans[idx] = nums[i];
      }

      // Find first greater elements
      List<int> moved = [];
      while (firstStack.isNotEmpty && nums[i] > nums[firstStack.last]) {
        moved.add(firstStack.removeLast());
      }
      // Those now wait for their second greater
      for (int idx in moved) {
        secondStack.add(idx);
      }

      // Current index waits for its first greater
      firstStack.add(i);
    }

    return ans;
  }
}
```

## Golang

```go
import "container/heap"

type item struct {
	val int
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
	*h = old[:n-1]
	return it
}

func secondGreaterElement(nums []int) []int {
	n := len(nums)
	ans := make([]int, n)
	for i := range ans {
		ans[i] = -1
	}
	stack := []int{} // indices with decreasing values
	h := &minHeap{}
	heap.Init(h)

	for i, v := range nums {
		// Resolve second greater elements
		for h.Len() > 0 && (*h)[0].val < v {
			it := heap.Pop(h).(item)
			ans[it.idx] = v
		}
		// Resolve first greater elements and move them to heap
		for len(stack) > 0 && nums[stack[len(stack)-1]] < v {
			idx := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			heap.Push(h, item{val: nums[idx], idx: idx})
		}
		// Current index may become first greater for future elements
		stack = append(stack, i)
	}
	return ans
}
```

## Ruby

```ruby
class MinHeap
  def initialize
    @data = []
  end

  def empty?
    @data.empty?
  end

  def top
    @data[0]
  end

  def push(item)
    @data << item
    sift_up(@data.size - 1)
  end

  def pop
    return nil if @data.empty?
    min = @data[0]
    last = @data.pop
    unless @data.empty?
      @data[0] = last
      sift_down(0)
    end
    min
  end

  private

  def sift_up(idx)
    while idx > 0
      parent = (idx - 1) / 2
      break if @data[parent][0] <= @data[idx][0]
      @data[parent], @data[idx] = @data[idx], @data[parent]
      idx = parent
    end
  end

  def sift_down(idx)
    n = @data.size
    loop do
      left = idx * 2 + 1
      right = left + 1
      smallest = idx
      if left < n && @data[left][0] < @data[smallest][0]
        smallest = left
      end
      if right < n && @data[right][0] < @data[smallest][0]
        smallest = right
      end
      break if smallest == idx
      @data[smallest], @data[idx] = @data[idx], @data[smallest]
      idx = smallest
    end
  end
end

# @param {Integer[]} nums
# @return {Integer[]}
def second_greater_element(nums)
  n = nums.length
  ans = Array.new(n, -1)
  stack = []          # indices waiting for first greater
  heap = MinHeap.new  # stores [value, index] awaiting second greater

  nums.each_with_index do |val, i|
    while !heap.empty? && val > heap.top[0]
      _, idx = heap.pop
      ans[idx] = val
    end

    while !stack.empty? && val > nums[stack[-1]]
      idx = stack.pop
      heap.push([nums[idx], idx])
    end

    stack << i
  end

  ans
end
```

## Scala

```scala
object Solution {
    def secondGreaterElement(nums: Array[Int]): Array[Int] = {
        val n = nums.length
        val ans = Array.fill(n)(-1)
        val first = new scala.collection.mutable.Stack[Int]()
        val second = new scala.collection.mutable.Stack[Int]()
        for (i <- 0 until n) {
            val cur = nums(i)
            while (second.nonEmpty && cur > nums(second.top)) {
                ans(second.pop()) = cur
            }
            val moved = scala.collection.mutable.ArrayBuffer[Int]()
            while (first.nonEmpty && cur > nums(first.top)) {
                moved += first.pop()
            }
            for (idx <- moved.reverse) {
                second.push(idx)
            }
            first.push(i)
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn second_greater_element(nums: Vec<i32>) -> Vec<i32> {
        use std::cmp::Reverse;
        use std::collections::BinaryHeap;

        let n = nums.len();
        let mut ans = vec![-1; n];
        let mut stack: Vec<usize> = Vec::new(); // indices waiting for first greater
        let mut heap: BinaryHeap<Reverse<(i32, usize)>> = BinaryHeap::new(); // (value, index) waiting for second greater

        for i in 0..n {
            // Resolve second greater candidates
            while let Some(&Reverse((val, idx))) = heap.peek() {
                if nums[i] > val {
                    ans[idx] = nums[i];
                    heap.pop();
                } else {
                    break;
                }
            }

            // Find first greater for pending indices
            while let Some(&last) = stack.last() {
                if nums[i] > nums[last] {
                    heap.push(Reverse((nums[last], last)));
                    stack.pop();
                } else {
                    break;
                }
            }

            // Current index becomes candidate for future first greater
            stack.push(i);
        }

        ans
    }
}
```

## Racket

```racket
(require racket/heap)

(define/contract (second-greater-element nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ((v (list->vector nums))
         (n (vector-length v))
         (ans (make-vector n -1))
         (stack '())
         (heap (make-heap (lambda (a b) (< (first a) (first b))))))
    (for ([i (in-range n)])
      (define cur (vector-ref v i))
      ;; Resolve second greater elements
      (let loop ()
        (when (and (not (heap-empty? heap))
                   (< (first (heap-min heap)) cur))
          (define pair (heap-remove-min! heap))
          (vector-set! ans (second pair) cur)
          (loop)))
      ;; Process first greater elements
      (let loop1 ()
        (when (and (not (null? stack))
                   (> cur (vector-ref v (car stack))))
          (define idx (car stack))
          (set! stack (cdr stack))
          (heap-add! heap (list (vector-ref v idx) idx))
          (loop1)))
      ;; Push current index onto the first-greater stack
      (set! stack (cons i stack)))
    (vector->list ans)))
```

## Erlang

```erlang
-spec second_greater_element(Nums :: [integer()]) -> [integer()].
second_greater_element(Nums) ->
    Len = length(Nums),
    NumsT = list_to_tuple(Nums),
    Answer0 = array:new(Len, {default, -1}),
    FinalArr = process(0, Len, NumsT, [], [], Answer0),
    array:to_list(FinalArr).

process(Index, Len, _NumsT, _S1, _S2, Ans) when Index == Len ->
    Ans;
process(Index, Len, NumsT, S1, S2, Ans) ->
    CurVal = element(Index + 1, NumsT),
    {NewS2, NewAns} = pop_second_greater(S2, CurVal, Ans, NumsT),
    {NewS1, UpdatedS2} = move_first_to_second(S1, NewS2, CurVal, NumsT),
    process(Index + 1, Len, NumsT, [Index | NewS1], UpdatedS2, NewAns).

pop_second_greater([], _CurVal, Ans, _NumsT) ->
    {[], Ans};
pop_second_greater([Top|Rest] = Stack, CurVal, Ans, NumsT) ->
    TopVal = element(Top + 1, NumsT),
    case TopVal < CurVal of
        true ->
            UpdatedAns = array:set(Top, CurVal, Ans),
            pop_second_greater(Rest, CurVal, UpdatedAns, NumsT);
        false ->
            {Stack, Ans}
    end.

move_first_to_second([], S2, _CurVal, _NumsT) ->
    {[], S2};
move_first_to_second([Top|Rest] = Stack1, S2, CurVal, NumsT) ->
    TopVal = element(Top + 1, NumsT),
    case TopVal < CurVal of
        true ->
            move_first_to_second(Rest, [Top | S2], CurVal, NumsT);
        false ->
            {Stack1, S2}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec second_greater_element(nums :: [integer]) :: [integer]
  def second_greater_element(nums) do
    n = length(nums)
    nums_arr = :array.from_list(nums)
    ans_arr = :array.new(n, default: -1)

    {_, _, final_ans} =
      Enum.with_index(nums)
      |> Enum.reduce({[], :gb_trees.empty(), ans_arr}, fn {cur, i},
                                                          {stack, pending, arr} ->
        # Process pending indices waiting for second greater
        {less, _maybe, greater} = :gb_trees.split(cur, pending)

        arr1 = assign_less(less, arr, cur)

        # Process stack for first greater
        {new_stack, new_pending} = pop_first_greater(stack, cur, nums_arr, greater)

        # Push current index onto stack
        {[i | new_stack], new_pending, arr1}
      end)

    :array.to_list(final_ans)
  end

  defp assign_less(tree, arr, cur) do
    if :gb_trees.is_empty(tree) do
      arr
    else
      {{_key, idxs}, rest} = :gb_trees.take_smallest(tree)

      arr1 =
        Enum.reduce(idxs, arr, fn idx, a ->
          :array.set(idx, cur, a)
        end)

      assign_less(rest, arr1, cur)
    end
  end

  defp pop_first_greater([], _cur, _nums_arr, pending), do: {[], pending}

  defp pop_first_greater([top | rest] = stack, cur, nums_arr, pending) do
    top_val = :array.get(top, nums_arr)

    if cur > top_val do
      # Move index to pending tree keyed by its value (first greater waiting)
      updated_pending =
        case :gb_trees.lookup(top_val, pending) do
          :none -> :gb_trees.insert(top_val, [top], pending)
          {:value, lst} -> :gb_trees.update(top_val, [top | lst], pending)
        end

      pop_first_greater(rest, cur, nums_arr, updated_pending)
    else
      {stack, pending}
    end
  end
end
```
