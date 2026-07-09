# 0239. Sliding Window Maximum

## Cpp

```cpp
#include <vector>
#include <deque>
using namespace std;

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> ans;
        deque<int> dq; // stores indices of potential max elements
        for (int i = 0; i < n; ++i) {
            if (!dq.empty() && dq.front() <= i - k)
                dq.pop_front();
            while (!dq.empty() && nums[i] >= nums[dq.back()])
                dq.pop_back();
            dq.push_back(i);
            if (i >= k - 1)
                ans.push_back(nums[dq.front()]);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums == null || k <= 0) return new int[0];
        int n = nums.length;
        int[] result = new int[n - k + 1];
        Deque<Integer> deque = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            // Remove indices of elements not in the current window
            while (!deque.isEmpty() && deque.peekFirst() <= i - k) {
                deque.pollFirst();
            }
            // Maintain decreasing order in deque
            while (!deque.isEmpty() && nums[deque.peekLast()] < nums[i]) {
                deque.pollLast();
            }
            deque.offerLast(i);
            // Record the max for windows that have fully formed
            if (i >= k - 1) {
                result[i - k + 1] = nums[deque.peekFirst()];
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque
        n = len(nums)
        if n * k == 0:
            return []
        dq = deque()
        res = []
        for i in range(n):
            # remove indices out of the current window
            while dq and dq[0] <= i - k:
                dq.popleft()
            # maintain decreasing order in deque
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            # start adding results after first window is formed
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res
```

## Python3

```python
from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k == 0 or n == 0:
            return []
        dq = deque()
        res = []
        for i in range(n):
            # Remove indices that are out of the current window
            while dq and dq[0] < i - k + 1:
                dq.popleft()
            # Maintain decreasing order in deque
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            # Append max for windows that have reached size k
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maxSlidingWindow(int* nums, int numsSize, int k, int* returnSize) {
    if (numsSize == 0 || k == 0) {
        *returnSize = 0;
        return NULL;
    }
    
    int outSize = numsSize - k + 1;
    int* result = (int*)malloc(outSize * sizeof(int));
    int* dq = (int*)malloc(numsSize * sizeof(int)); // store indices
    int front = 0, back = -1; // empty deque
    
    for (int i = 0; i < numsSize; ++i) {
        // Remove indices that are out of the current window
        if (front <= back && dq[front] <= i - k)
            ++front;
        
        // Maintain decreasing order in deque
        while (front <= back && nums[dq[back]] < nums[i])
            --back;
        
        dq[++back] = i; // push current index
        
        // Record result when the first window is complete
        if (i >= k - 1) {
            result[i - k + 1] = nums[dq[front]];
        }
    }
    
    *returnSize = outSize;
    free(dq);
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int[] MaxSlidingWindow(int[] nums, int k) {
        if (nums == null || nums.Length == 0) return new int[0];
        int n = nums.Length;
        int[] result = new int[n - k + 1];
        var deque = new LinkedList<int>(); // stores indices

        for (int i = 0; i < n; i++) {
            if (deque.Count > 0 && deque.First.Value <= i - k) {
                deque.RemoveFirst();
            }
            while (deque.Count > 0 && nums[deque.Last.Value] < nums[i]) {
                deque.RemoveLast();
            }
            deque.AddLast(i);
            if (i >= k - 1) {
                result[i - k + 1] = nums[deque.First.Value];
            }
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSlidingWindow = function(nums, k) {
    const n = nums.length;
    if (k === 1) return nums.slice();
    const deque = []; // store indices, decreasing values
    const result = [];
    
    for (let i = 0; i < n; i++) {
        // Remove indices out of the current window
        while (deque.length && deque[0] <= i - k) {
            deque.shift();
        }
        // Maintain decreasing order in deque
        while (deque.length && nums[deque[deque.length - 1]] < nums[i]) {
            deque.pop();
        }
        deque.push(i);
        // Append max for windows that have reached size k
        if (i >= k - 1) {
            result.push(nums[deque[0]]);
        }
    }
    
    return result;
};
```

## Typescript

```typescript
function maxSlidingWindow(nums: number[], k: number): number[] {
    const n = nums.length;
    if (k === 1) return nums.slice();

    const deque: number[] = []; // stores indices
    const result: number[] = [];

    for (let i = 0; i < n; i++) {
        // Remove indices whose corresponding values are less than current value
        while (deque.length && nums[deque[deque.length - 1]] <= nums[i]) {
            deque.pop();
        }
        deque.push(i);

        // Remove the index that is out of the current window
        if (deque[0] <= i - k) {
            deque.shift();
        }

        // Record max for windows that have reached size k
        if (i >= k - 1) {
            result.push(nums[deque[0]]);
        }
    }

    return result;
}
```

## Php

```php
<?php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer[]
     */
    function maxSlidingWindow($nums, $k) {
        $n = count($nums);
        if ($n == 0) return [];

        $deque = new SplDoublyLinkedList();
        $deque->setIteratorMode(SplDoublyLinkedList::IT_MODE_FIFO);
        $result = [];

        for ($i = 0; $i < $n; $i++) {
            // Remove indices that are out of the current window
            if (!$deque->isEmpty()) {
                $frontIdx = $deque->bottom();
                if ($frontIdx <= $i - $k) {
                    $deque->shift();
                }
            }

            // Maintain decreasing order in deque
            while (!$deque->isEmpty() && $nums[$i] >= $nums[$deque->top()]) {
                $deque->pop();
            }

            // Add current index
            $deque->push($i);

            // Record the maximum for the window
            if ($i >= $k - 1) {
                $result[] = $nums[$deque->bottom()];
            }
        }

        return $result;
    }
}
?>
```

## Swift

```swift
class Solution {
    func maxSlidingWindow(_ nums: [Int], _ k: Int) -> [Int] {
        var result = [Int]()
        var deque = [Int]()          // stores indices
        var front = 0                // points to the current front
        
        for i in 0..<nums.count {
            // Remove indices that are out of the current window
            if front < deque.count && deque[front] <= i - k {
                front += 1
            }
            
            // Maintain decreasing order in deque
            while deque.count > front && nums[deque.last!] < nums[i] {
                deque.removeLast()
            }
            
            deque.append(i)
            
            // Append max for windows that have reached size k
            if i >= k - 1 {
                result.append(nums[deque[front]])
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxSlidingWindow(nums: IntArray, k: Int): IntArray {
        val n = nums.size
        if (k == 0) return intArrayOf()
        val result = IntArray(n - k + 1)
        val deque: java.util.ArrayDeque<Int> = java.util.ArrayDeque()
        var idx = 0
        for (i in 0 until n) {
            // Remove indices that are out of the current window
            if (!deque.isEmpty() && deque.peekFirst() <= i - k) {
                deque.pollFirst()
            }
            // Maintain decreasing order in deque
            while (!deque.isEmpty() && nums[deque.peekLast()] < nums[i]) {
                deque.pollLast()
            }
            deque.addLast(i)
            // Record the max for windows that have reached size k
            if (i >= k - 1) {
                result[idx++] = nums[deque.peekFirst()]
            }
        }
        return result
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  List<int> maxSlidingWindow(List<int> nums, int k) {
    final n = nums.length;
    if (n == 0 || k == 0) return [];
    final result = <int>[];
    final deque = Queue<int>(); // stores indices

    for (int i = 0; i < n; ++i) {
      // Remove indices that are out of the current window
      if (deque.isNotEmpty && deque.first <= i - k) {
        deque.removeFirst();
      }
      // Maintain decreasing order in deque
      while (deque.isNotEmpty && nums[deque.last] < nums[i]) {
        deque.removeLast();
      }
      deque.addLast(i);
      // Record the max for windows that have reached size k
      if (i >= k - 1) {
        result.add(nums[deque.first]);
      }
    }

    return result;
  }
}
```

## Golang

```go
func maxSlidingWindow(nums []int, k int) []int {
    n := len(nums)
    if n == 0 || k == 0 {
        return []int{}
    }
    deque := make([]int, 0, k)
    res := make([]int, 0, n-k+1)

    for i := 0; i < n; i++ {
        // Remove indices whose corresponding values are less than nums[i]
        for len(deque) > 0 && nums[deque[len(deque)-1]] <= nums[i] {
            deque = deque[:len(deque)-1]
        }
        // Add current index
        deque = append(deque, i)

        // Remove the front if it's out of the window
        if deque[0] <= i-k {
            deque = deque[1:]
        }

        // Record result when first window is complete
        if i >= k-1 {
            res = append(res, nums[deque[0]])
        }
    }
    return res
}
```

## Ruby

```ruby
def max_sliding_window(nums, k)
  n = nums.length
  return [] if n == 0 || k == 0

  deque = []
  res = []

  nums.each_with_index do |num, i|
    while !deque.empty? && nums[deque[-1]] <= num
      deque.pop
    end
    deque << i

    if !deque.empty? && deque[0] <= i - k
      deque.shift
    end

    if i >= k - 1
      res << nums[deque[0]]
    end
  end

  res
end
```

## Scala

```scala
object Solution {
    def maxSlidingWindow(nums: Array[Int], k: Int): Array[Int] = {
        val n = nums.length
        if (k == 0) return Array.emptyIntArray
        val result = scala.collection.mutable.ArrayBuffer[Int]()
        val dq = new java.util.ArrayDeque[Int]() // stores indices

        for (i <- 0 until n) {
            while (!dq.isEmpty && nums(dq.peekLast()) <= nums(i)) {
                dq.pollLast()
            }
            dq.addLast(i)

            if (dq.peekFirst() <= i - k) {
                dq.pollFirst()
            }

            if (i >= k - 1) {
                result += nums(dq.peekFirst())
            }
        }
        result.toArray
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_sliding_window(nums: Vec<i32>, k: i32) -> Vec<i32> {
        use std::collections::VecDeque;
        let n = nums.len();
        if n == 0 {
            return vec![];
        }
        let k = k as usize;
        let mut deq: VecDeque<usize> = VecDeque::new();
        let mut res = Vec::with_capacity(n - k + 1);
        for i in 0..n {
            // Remove indices that are out of the current window
            if let Some(&front) = deq.front() {
                if front + k <= i {
                    deq.pop_front();
                }
            }
            // Maintain decreasing order of values in deque
            while let Some(&back) = deq.back() {
                if nums[back] < nums[i] {
                    deq.pop_back();
                } else {
                    break;
                }
            }
            deq.push_back(i);
            // Record the maximum for windows that have reached size k
            if i + 1 >= k {
                if let Some(&front) = deq.front() {
                    res.push(nums[front]);
                }
            }
        }
        res
    }
}
```

## Racket

```racket
(require racket/deque)

(define/contract (max-sliding-window nums k)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let* ((v (list->vector nums))
         (n (vector-length v))
         (dq (make-deque))
         (result '()))
    (for ([i (in-range n)])
      ;; maintain decreasing deque
      (let loop ()
        (unless (deque-empty? dq)
          (define last-idx (deque-last dq))
          (when (<= (vector-ref v last-idx) (vector-ref v i))
            (deque-remove-back! dq)
            (loop))))
      (deque-add-back! dq i)
      ;; remove indices that are out of the current window
      (let ((threshold (+ (- i k) 1))) ; i - k + 1
        (when (and (not (deque-empty? dq))
                   (< (deque-first dq) threshold))
          (deque-remove-front! dq)))
      ;; record max when the first full window is formed
      (when (>= i (- k 1))
        (set! result (cons (vector-ref v (deque-first dq)) result))))
    (reverse result)))
```

## Erlang

```erlang
-spec max_sliding_window(Nums :: [integer()], K :: integer()) -> [integer()].
max_sliding_window(Nums, K) ->
    Deque = queue:new(),
    ResultRev = process(Nums, 0, Deque, [], K),
    lists:reverse(ResultRev).

process([], _Idx, _Deque, Acc, _K) ->
    Acc;
process([H|T], I, Deq, Acc, K) ->
    Deq1 = remove_back_smaller(Deq, H),
    Deq2 = queue:in({I, H}, Deq1),
    Deq3 = remove_front_out_of_window(Deq2, I, K),
    case I >= K - 1 of
        true ->
            {value, {_IdxMax, MaxVal}} = queue:peek(Deque3),
            process(T, I + 1, Deq3, [MaxVal | Acc], K);
        false ->
            process(T, I + 1, Deq3, Acc, K)
    end.

remove_back_smaller(Deque, X) ->
    case queue:peek_r(Deque) of
        empty -> Deque;
        {value, {_Idx, V}} when V =< X ->
            {value, _Elem, D1} = queue:out_r(Deque),
            remove_back_smaller(D1, X);
        {value, _} -> Deque
    end.

remove_front_out_of_window(Deque, I, K) ->
    case queue:peek(Deque) of
        empty -> Deque;
        {value, {Idx, _}} when Idx =< I - K ->
            {value, _Elem, D1} = queue:out(Deque),
            remove_front_out_of_window(D1, I, K);
        {value, _} -> Deque
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_sliding_window(nums :: [integer], k :: integer) :: [integer]
  def max_sliding_window(nums, k) do
    n = length(nums)
    arr = :array.from_list(nums)
    dq = :queue.new()
    loop(0, n, k, arr, dq, [])
  end

  defp loop(i, n, _k, _arr, _dq, acc) when i == n do
    Enum.reverse(acc)
  end

  defp loop(i, n, k, arr, dq, acc) do
    # Remove indices that are out of the current window
    dq =
      case :queue.peek(dq) do
        {:value, idx} when idx <= i - k ->
          {{:value, _}, new_dq} = :queue.out(dq)
          new_dq

        _ ->
          dq
      end

    # Remove indices from the back whose values are less than or equal to nums[i]
    dq = clean_back(i, arr, dq)

    # Add current index to the deque
    dq = :queue.in(i, dq)

    acc =
      if i >= k - 1 do
        max_val =
          case :queue.peek(dq) do
            {:value, idx} -> :array.get(idx, arr)
          end

        [max_val | acc]
      else
        acc
      end

    loop(i + 1, n, k, arr, dq, acc)
  end

  defp clean_back(i, arr, dq) do
    case :queue.peek_r(dq) do
      {:value, idx} ->
        if :array.get(idx, arr) <= :array.get(i, arr) do
          {{:value, _}, new_dq} = :queue.out_r(dq)
          clean_back(i, arr, new_dq)
        else
          dq
        end

      _ ->
        dq
    end
  end
end
```
