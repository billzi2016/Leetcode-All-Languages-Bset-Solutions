# 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

## Cpp

```cpp
class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        deque<int> maxDeque, minDeque;
        int left = 0, best = 0;
        for (int right = 0; right < (int)nums.size(); ++right) {
            while (!maxDeque.empty() && maxDeque.back() < nums[right])
                maxDeque.pop_back();
            maxDeque.push_back(nums[right]);
            
            while (!minDeque.empty() && minDeque.back() > nums[right])
                minDeque.pop_back();
            minDeque.push_back(nums[right]);
            
            while (!maxDeque.empty() && !minDeque.empty() &&
                   maxDeque.front() - minDeque.front() > limit) {
                if (maxDeque.front() == nums[left]) maxDeque.pop_front();
                if (minDeque.front() == nums[left]) minDeque.pop_front();
                ++left;
            }
            
            best = max(best, right - left + 1);
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public int longestSubarray(int[] nums, int limit) {
        java.util.Deque<Integer> maxDeque = new java.util.ArrayDeque<>();
        java.util.Deque<Integer> minDeque = new java.util.ArrayDeque<>();
        int left = 0;
        int best = 0;
        for (int right = 0; right < nums.length; right++) {
            int val = nums[right];
            while (!maxDeque.isEmpty() && maxDeque.peekLast() < val) {
                maxDeque.pollLast();
            }
            maxDeque.addLast(val);
            while (!minDeque.isEmpty() && minDeque.peekLast() > val) {
                minDeque.pollLast();
            }
            minDeque.addLast(val);
            while (maxDeque.peekFirst() - minDeque.peekFirst() > limit) {
                if (nums[left] == maxDeque.peekFirst()) {
                    maxDeque.pollFirst();
                }
                if (nums[left] == minDeque.peekFirst()) {
                    minDeque.pollFirst();
                }
                left++;
            }
            best = Math.max(best, right - left + 1);
        }
        return best;
    }
}
```

## Python

```python
class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        from collections import deque

        max_deque = deque()  # decreasing
        min_deque = deque()  # increasing
        left = 0
        best = 0

        for right, val in enumerate(nums):
            while max_deque and max_deque[-1] < val:
                max_deque.pop()
            max_deque.append(val)

            while min_deque and min_deque[-1] > val:
                min_deque.pop()
            min_deque.append(val)

            # shrink window if invalid
            while max_deque[0] - min_deque[0] > limit:
                if nums[left] == max_deque[0]:
                    max_deque.popleft()
                if nums[left] == min_deque[0]:
                    min_deque.popleft()
                left += 1

            best = max(best, right - left + 1)

        return best
```

## Python3

```python
from collections import deque
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque()  # decreasing
        min_deque = deque()  # increasing
        left = 0
        result = 0

        for right, value in enumerate(nums):
            while max_deque and max_deque[-1] < value:
                max_deque.pop()
            max_deque.append(value)

            while min_deque and min_deque[-1] > value:
                min_deque.pop()
            min_deque.append(value)

            while max_deque[0] - min_deque[0] > limit:
                if nums[left] == max_deque[0]:
                    max_deque.popleft()
                if nums[left] == min_deque[0]:
                    min_deque.popleft()
                left += 1

            result = max(result, right - left + 1)

        return result
```

## C

```c
int longestSubarray(int* nums, int numsSize, int limit) {
    if (numsSize == 0) return 0;
    int *maxDeque = (int *)malloc(numsSize * sizeof(int));
    int *minDeque = (int *)malloc(numsSize * sizeof(int));
    int maxHead = 0, maxTail = 0; // indices in maxDeque[ maxHead .. maxTail-1 ]
    int minHead = 0, minTail = 0;
    int left = 0, best = 0;

    for (int right = 0; right < numsSize; ++right) {
        while (maxTail > maxHead && nums[maxDeque[maxTail - 1]] < nums[right])
            --maxTail;
        maxDeque[maxTail++] = right;

        while (minTail > minHead && nums[minDeque[minTail - 1]] > nums[right])
            --minTail;
        minDeque[minTail++] = right;

        while (nums[maxDeque[maxHead]] - nums[minDeque[minHead]] > limit) {
            if (maxDeque[maxHead] == left) ++maxHead;
            if (minDeque[minHead] == left) ++minHead;
            ++left;
        }

        int len = right - left + 1;
        if (len > best) best = len;
    }

    free(maxDeque);
    free(minDeque);
    return best;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int LongestSubarray(int[] nums, int limit) {
        var maxDeque = new LinkedList<int>();
        var minDeque = new LinkedList<int>();
        int left = 0, best = 0;
        for (int right = 0; right < nums.Length; ++right) {
            int val = nums[right];
            while (maxDeque.Count > 0 && maxDeque.Last.Value < val)
                maxDeque.RemoveLast();
            maxDeque.AddLast(val);
            while (minDeque.Count > 0 && minDeque.Last.Value > val)
                minDeque.RemoveLast();
            minDeque.AddLast(val);
            while (maxDeque.First.Value - minDeque.First.Value > limit) {
                if (maxDeque.First.Value == nums[left])
                    maxDeque.RemoveFirst();
                if (minDeque.First.Value == nums[left])
                    minDeque.RemoveFirst();
                left++;
            }
            best = Math.Max(best, right - left + 1);
        }
        return best;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} limit
 * @return {number}
 */
var longestSubarray = function(nums, limit) {
    const maxDeque = []; // stores indices in decreasing order of values
    const minDeque = []; // stores indices in increasing order of values
    let maxHead = 0;
    let minHead = 0;
    let left = 0;
    let best = 0;

    for (let right = 0; right < nums.length; ++right) {
        while (maxDeque.length > maxHead && nums[maxDeque[maxDeque.length - 1]] < nums[right]) {
            maxDeque.pop();
        }
        maxDeque.push(right);

        while (minDeque.length > minHead && nums[minDeque[minDeque.length - 1]] > nums[right]) {
            minDeque.pop();
        }
        minDeque.push(right);

        while (nums[maxDeque[maxHead]] - nums[minDeque[minHead]] > limit) {
            if (maxDeque[maxHead] === left) maxHead++;
            if (minDeque[minHead] === left) minHead++;
            ++left;
        }

        best = Math.max(best, right - left + 1);
    }

    return best;
};
```

## Typescript

```typescript
function longestSubarray(nums: number[], limit: number): number {
    const maxDeque: number[] = []; // stores indices, values in decreasing order
    const minDeque: number[] = []; // stores indices, values in increasing order
    let left = 0;
    let best = 0;

    for (let right = 0; right < nums.length; ++right) {
        while (maxDeque.length && nums[maxDeque[maxDeque.length - 1]] < nums[right]) {
            maxDeque.pop();
        }
        maxDeque.push(right);

        while (minDeque.length && nums[minDeque[minDeque.length - 1]] > nums[right]) {
            minDeque.pop();
        }
        minDeque.push(right);

        while (nums[maxDeque[0]] - nums[minDeque[0]] > limit) {
            if (maxDeque[0] === left) maxDeque.shift();
            if (minDeque[0] === left) minDeque.shift();
            left++;
        }

        best = Math.max(best, right - left + 1);
    }

    return best;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $limit
     * @return Integer
     */
    function longestSubarray($nums, $limit) {
        $maxDeque = new SplDoublyLinkedList(); // decreasing order
        $minDeque = new SplDoublyLinkedList(); // increasing order

        $left = 0;
        $result = 0;
        $n = count($nums);

        for ($right = 0; $right < $n; $right++) {
            $num = $nums[$right];

            while (!$maxDeque->isEmpty() && $maxDeque->top() < $num) {
                $maxDeque->pop();
            }
            $maxDeque->push($num);

            while (!$minDeque->isEmpty() && $minDeque->top() > $num) {
                $minDeque->pop();
            }
            $minDeque->push($num);

            while ($maxDeque->bottom() - $minDeque->bottom() > $limit) {
                if ($maxDeque->bottom() == $nums[$left]) {
                    $maxDeque->shift();
                }
                if ($minDeque->bottom() == $nums[$left]) {
                    $minDeque->shift();
                }
                $left++;
            }

            $result = max($result, $right - $left + 1);
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func longestSubarray(_ nums: [Int], _ limit: Int) -> Int {
        var maxDeque = [Int]()   // stores indices, decreasing values
        var minDeque = [Int]()   // stores indices, increasing values
        var maxHead = 0
        var minHead = 0
        
        var left = 0
        var best = 0
        
        for right in 0..<nums.count {
            // maintain decreasing maxDeque
            while maxHead < maxDeque.count && nums[maxDeque.last!] < nums[right] {
                maxDeque.removeLast()
            }
            maxDeque.append(right)
            
            // maintain increasing minDeque
            while minHead < minDeque.count && nums[minDeque.last!] > nums[right] {
                minDeque.removeLast()
            }
            minDeque.append(right)
            
            // shrink window if diff exceeds limit
            while maxHead < maxDeque.count &&
                  minHead < minDeque.count &&
                  nums[maxDeque[maxHead]] - nums[minDeque[minHead]] > limit {
                
                if maxDeque[maxHead] == left { maxHead += 1 }
                if minDeque[minHead] == left { minHead += 1 }
                left += 1
            }
            
            // optional cleanup to avoid large unused prefix
            if maxHead > 1000 && maxHead * 2 > maxDeque.count {
                maxDeque.removeFirst(maxHead)
                maxHead = 0
            }
            if minHead > 1000 && minHead * 2 > minDeque.count {
                minDeque.removeFirst(minHead)
                minHead = 0
            }
            
            best = max(best, right - left + 1)
        }
        
        return best
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestSubarray(nums: IntArray, limit: Int): Int {
        val maxDeque = java.util.ArrayDeque<Int>()
        val minDeque = java.util.ArrayDeque<Int>()
        var left = 0
        var best = 0
        for (right in nums.indices) {
            val cur = nums[right]
            while (!maxDeque.isEmpty() && maxDeque.peekLast() < cur) {
                maxDeque.pollLast()
            }
            maxDeque.addLast(cur)
            while (!minDeque.isEmpty() && minDeque.peekLast() > cur) {
                minDeque.pollLast()
            }
            minDeque.addLast(cur)

            while (maxDeque.peekFirst() - minDeque.peekFirst() > limit) {
                if (maxDeque.peekFirst() == nums[left]) maxDeque.pollFirst()
                if (minDeque.peekFirst() == nums[left]) minDeque.pollFirst()
                left++
            }

            best = kotlin.math.max(best, right - left + 1)
        }
        return best
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  int longestSubarray(List<int> nums, int limit) {
    final maxDeque = DoubleLinkedQueue<int>();
    final minDeque = DoubleLinkedQueue<int>();
    int left = 0;
    int best = 0;

    for (int right = 0; right < nums.length; ++right) {
      int cur = nums[right];

      while (maxDeque.isNotEmpty && maxDeque.last < cur) {
        maxDeque.removeLast();
      }
      maxDeque.addLast(cur);

      while (minDeque.isNotEmpty && minDeque.last > cur) {
        minDeque.removeLast();
      }
      minDeque.addLast(cur);

      while (maxDeque.first - minDeque.first > limit) {
        if (maxDeque.first == nums[left]) {
          maxDeque.removeFirst();
        }
        if (minDeque.first == nums[left]) {
          minDeque.removeFirst();
        }
        left++;
      }

      int len = right - left + 1;
      if (len > best) best = len;
    }

    return best;
  }
}
```

## Golang

```go
func longestSubarray(nums []int, limit int) int {
    maxDeque := make([]int, 0)
    minDeque := make([]int, 0)
    left, ans := 0, 0

    for right, v := range nums {
        // maintain decreasing max deque
        for len(maxDeque) > 0 && nums[maxDeque[len(maxDeque)-1]] < v {
            maxDeque = maxDeque[:len(maxDeque)-1]
        }
        maxDeque = append(maxDeque, right)

        // maintain increasing min deque
        for len(minDeque) > 0 && nums[minDeque[len(minDeque)-1]] > v {
            minDeque = minDeque[:len(minDeque)-1]
        }
        minDeque = append(minDeque, right)

        // shrink window while invalid
        for len(maxDeque) > 0 && len(minDeque) > 0 && nums[maxDeque[0]]-nums[minDeque[0]] > limit {
            if maxDeque[0] == left {
                maxDeque = maxDeque[1:]
            }
            if minDeque[0] == left {
                minDeque = minDeque[1:]
            }
            left++
        }

        if cur := right - left + 1; cur > ans {
            ans = cur
        }
    }
    return ans
}
```

## Ruby

```ruby
def longest_subarray(nums, limit)
  max_deque = [] # stores indices of elements in decreasing order
  min_deque = [] # stores indices of elements in increasing order
  left = 0
  best = 0

  nums.each_with_index do |value, right|
    while !max_deque.empty? && nums[max_deque[-1]] < value
      max_deque.pop
    end
    max_deque << right

    while !min_deque.empty? && nums[min_deque[-1]] > value
      min_deque.pop
    end
    min_deque << right

    while nums[max_deque[0]] - nums[min_deque[0]] > limit
      left += 1
      max_deque.shift if max_deque[0] < left
      min_deque.shift if min_deque[0] < left
    end

    current_len = right - left + 1
    best = current_len if current_len > best
  end

  best
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable.ArrayDeque

  def longestSubarray(nums: Array[Int], limit: Int): Int = {
    val maxDeque = new ArrayDeque[Int]()
    val minDeque = new ArrayDeque[Int]()
    var left = 0
    var best = 0

    for (right <- nums.indices) {
      val v = nums(right)

      while (maxDeque.nonEmpty && maxDeque.last < v) maxDeque.removeLast()
      maxDeque.append(v)

      while (minDeque.nonEmpty && minDeque.last > v) minDeque.removeLast()
      minDeque.append(v)

      while (maxDeque.head - minDeque.head > limit) {
        if (maxDeque.head == nums(left)) maxDeque.removeHead()
        if (minDeque.head == nums(left)) minDeque.removeHead()
        left += 1
      }

      best = math.max(best, right - left + 1)
    }

    best
  }
}
```

## Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn longest_subarray(nums: Vec<i32>, limit: i32) -> i32 {
        let n = nums.len();
        let mut maxdq: VecDeque<usize> = VecDeque::new(); // decreasing values
        let mut mindq: VecDeque<usize> = VecDeque::new(); // increasing values
        let mut left = 0usize;
        let mut ans = 0usize;

        for right in 0..n {
            while let Some(&idx) = maxdq.back() {
                if nums[idx] < nums[right] {
                    maxdq.pop_back();
                } else {
                    break;
                }
            }
            maxdq.push_back(right);

            while let Some(&idx) = mindq.back() {
                if nums[idx] > nums[right] {
                    mindq.pop_back();
                } else {
                    break;
                }
            }
            mindq.push_back(right);

            while !maxdq.is_empty()
                && !mindq.is_empty()
                && (nums[*maxdq.front().unwrap()] - nums[*mindq.front().unwrap()]).abs() > limit
            {
                if *maxdq.front().unwrap() == left {
                    maxdq.pop_front();
                }
                if *mindq.front().unwrap() == left {
                    mindq.pop_front();
                }
                left += 1;
            }

            ans = ans.max(right - left + 1);
        }

        ans as i32
    }
}
```

## Racket

```racket
(require racket/deque)

(define/contract (longest-subarray nums limit)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([arr (list->vector nums)]
         [n   (vector-length arr)])
    (define maxdq (make-deque))
    (define mindq (make-deque))
    (define left 0)
    (define best 0)
    (for ([right (in-range n)])
      (define val (vector-ref arr right))
      ;; maintain decreasing max deque
      (let loop ()
        (when (and (not (deque-empty? maxdq))
                   (< (deque-last maxdq) val))
          (deque-remove-back! maxdq)
          (loop)))
      (deque-add-back! maxdq val)
      ;; maintain increasing min deque
      (let loop2 ()
        (when (and (not (deque-empty? mindq))
                   (> (deque-last mindq) val))
          (deque-remove-back! mindq)
          (loop2)))
      (deque-add-back! mindq val)
      ;; shrink window while invalid
      (let shrink ()
        (when (> (- (deque-first maxdq) (deque-first mindq)) limit)
          (define leftval (vector-ref arr left))
          (when (= leftval (deque-first maxdq))
            (deque-remove-front! maxdq))
          (when (= leftval (deque-first mindq))
            (deque-remove-front! mindq))
          (set! left (+ left 1))
          (shrink)))
      ;; update answer
      (set! best (max best (+ 1 (- right left)))))
    best))
```

## Erlang

```erlang
-module(solution).
-export([longest_subarray/2]).

-spec longest_subarray(Nums :: [integer()], Limit :: integer()) -> integer().
longest_subarray(Nums, Limit) ->
    process(Nums, 0, 0, 0, queue:new(), queue:new(), Limit).

process([], _Right, MaxLen, _Left, _MaxQ, _MinQ, _Limit) ->
    MaxLen;
process([V|Rest], Right, MaxLen, Left, MaxQ0, MinQ0, Limit) ->
    I = Right,
    MaxQ1 = clean_back_max(MaxQ0, V),
    MaxQ2 = queue:in({V, I}, MaxQ1),

    MinQ1 = clean_back_min(MinQ0, V),
    MinQ2 = queue:in({V, I}, MinQ1),

    {NewLeft, NewMaxQ, NewMinQ} = shrink_window(Left, Limit, MaxQ2, MinQ2),

    NewLen = erlang:max(MaxLen, I - NewLeft + 1),
    process(Rest, Right + 1, NewLen, NewLeft, NewMaxQ, NewMinQ, Limit).

clean_back_max(Q, V) ->
    case queue:peek_r(Q) of
        {value, {Val, _}} when Val < V ->
            {_, Q1} = queue:out_r(Q),
            clean_back_max(Q1, V);
        _ -> Q
    end.

clean_back_min(Q, V) ->
    case queue:peek_r(Q) of
        {value, {Val, _}} when Val > V ->
            {_, Q1} = queue:out_r(Q),
            clean_back_min(Q1, V);
        _ -> Q
    end.

shrink_window(Left, Limit, MaxQ, MinQ) ->
    case {queue:peek(MaxQ), queue:peek(MinQ)} of
        {{value, {MaxVal, _}}, {value, {MinVal, _}}}
            when MaxVal - MinVal =< Limit ->
                {Left, MaxQ, MinQ};
        {{value, {MaxVal, _}}, {value, {MinVal, _}}} ->
            NewLeft = Left + 1,
            MaxQ1 = case queue:peek(MaxQ) of
                        {value, {_, Idx}} when Idx < NewLeft ->
                            {_, QRest} = queue:out(MaxQ),
                            QRest;
                        _ -> MaxQ
                    end,
            MinQ1 = case queue:peek(MinQ) of
                        {value, {_, Idx}} when Idx < NewLeft ->
                            {_, QRest} = queue:out(MinQ),
                            QRest;
                        _ -> MinQ
                    end,
            shrink_window(NewLeft, Limit, MaxQ1, MinQ1);
        _ ->
            {Left, MaxQ, MinQ}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_subarray(nums :: [integer], limit :: integer) :: integer
  def longest_subarray(nums, limit) do
    {max_len, _, _} =
      Enum.with_index(nums)
      |> Enum.reduce({0, 0, {:queue.new(), :queue.new()}}, fn {val, i},
            {curr_max, left, {max_q, min_q}} ->
        # maintain decreasing max deque
        max_q = pop_back_while(max_q, fn {v, _} -> v < val end)
        max_q = :queue.in({val, i}, max_q)

        # maintain increasing min deque
        min_q = pop_back_while(min_q, fn {v, _} -> v > val end)
        min_q = :queue.in({val, i}, min_q)

        {max_q, min_q, left} = shrink(max_q, min_q, left, limit)

        new_max = max(curr_max, i - left + 1)
        {new_max, left, {max_q, min_q}}
      end)

    max_len
  end

  defp pop_back_while(q, fun) do
    case :queue.out_r(q) do
      {:empty, _} ->
        q

      {{v, i} = elem, rest} ->
        if fun.(elem) do
          pop_back_while(rest, fun)
        else
          :queue.in_r(elem, rest)
        end
    end
  end

  defp shrink(max_q, min_q, left, limit) do
    case {:queue.peek(max_q), :queue.peek(min_q)} do
      {{:value, {max_val, _max_idx}}, {:value, {min_val, _min_idx}}} ->
        if max_val - min_val > limit do
          new_left = left + 1
          max_q = maybe_pop_front(max_q, new_left)
          min_q = maybe_pop_front(min_q, new_left)
          shrink(max_q, min_q, new_left, limit)
        else
          {max_q, min_q, left}
        end

      _ ->
        {max_q, min_q, left}
    end
  end

  defp maybe_pop_front(q, left) do
    case :queue.peek(q) do
      {:value, {_v, idx}} when idx < left ->
        {{_v, _i}, new_q} = :queue.out(q)
        maybe_pop_front(new_q, left)

      _ ->
        q
    end
  end
end
```
