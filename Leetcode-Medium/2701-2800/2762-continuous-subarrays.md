# 2762. Continuous Subarrays

## Cpp

```cpp
class Solution {
public:
    long long continuousSubarrays(vector<int>& nums) {
        deque<int> maxQ, minQ;
        long long ans = 0;
        int left = 0;
        for (int right = 0; right < (int)nums.size(); ++right) {
            while (!maxQ.empty() && nums[maxQ.back()] < nums[right]) maxQ.pop_back();
            maxQ.push_back(right);
            while (!minQ.empty() && nums[minQ.back()] > nums[right]) minQ.pop_back();
            minQ.push_back(right);
            while (!maxQ.empty() && !minQ.empty() && nums[maxQ.front()] - nums[minQ.front()] > 2) {
                if (maxQ.front() == left) maxQ.pop_front();
                if (minQ.front() == left) minQ.pop_front();
                ++left;
            }
            ans += right - left + 1;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long continuousSubarrays(int[] nums) {
        int n = nums.length;
        ArrayDeque<Integer> maxQ = new ArrayDeque<>();
        ArrayDeque<Integer> minQ = new ArrayDeque<>();
        int left = 0;
        long ans = 0L;
        for (int right = 0; right < n; ++right) {
            while (!maxQ.isEmpty() && nums[maxQ.peekLast()] < nums[right]) {
                maxQ.pollLast();
            }
            maxQ.addLast(right);
            while (!minQ.isEmpty() && nums[minQ.peekLast()] > nums[right]) {
                minQ.pollLast();
            }
            minQ.addLast(right);
            while (nums[maxQ.peekFirst()] - nums[minQ.peekFirst()] > 2) {
                if (maxQ.peekFirst() == left) maxQ.pollFirst();
                if (minQ.peekFirst() == left) minQ.pollFirst();
                left++;
            }
            ans += right - left + 1;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def continuousSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import deque

        max_q = deque()  # stores indices, values decreasing
        min_q = deque()  # stores indices, values increasing
        left = 0
        total = 0

        for right, val in enumerate(nums):
            while max_q and nums[max_q[-1]] < val:
                max_q.pop()
            max_q.append(right)

            while min_q and nums[min_q[-1]] > val:
                min_q.pop()
            min_q.append(right)

            # shrink window until condition satisfied
            while nums[max_q[0]] - nums[min_q[0]] > 2:
                if max_q[0] < min_q[0]:
                    left = max_q[0] + 1
                    max_q.popleft()
                else:
                    left = min_q[0] + 1
                    min_q.popleft()
                # discard any stale indices
                while max_q and max_q[0] < left:
                    max_q.popleft()
                while min_q and min_q[0] < left:
                    min_q.popleft()

            total += right - left + 1

        return total
```

## Python3

```python
import collections
from typing import List

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        maxdq = collections.deque()
        mindq = collections.deque()
        left = 0
        ans = 0
        for right, val in enumerate(nums):
            while maxdq and nums[maxdq[-1]] < val:
                maxdq.pop()
            maxdq.append(right)
            while mindq and nums[mindq[-1]] > val:
                mindq.pop()
            mindq.append(right)

            while nums[maxdq[0]] - nums[mindq[0]] > 2:
                left += 1
                if maxdq[0] < left:
                    maxdq.popleft()
                if mindq[0] < left:
                    mindq.popleft()

            ans += right - left + 1
        return ans
```

## C

```c
#include <stdlib.h>

long long continuousSubarrays(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    int *maxDeque = (int *)malloc(numsSize * sizeof(int));
    int *minDeque = (int *)malloc(numsSize * sizeof(int));
    int maxHead = 0, maxTail = -1;
    int minHead = 0, minTail = -1;
    int left = 0;
    long long ans = 0;

    for (int right = 0; right < numsSize; ++right) {
        while (maxTail >= maxHead && nums[maxDeque[maxTail]] < nums[right])
            --maxTail;
        maxDeque[++maxTail] = right;

        while (minTail >= minHead && nums[minDeque[minTail]] > nums[right])
            --minTail;
        minDeque[++minTail] = right;

        while (maxHead <= maxTail && minHead <= minTail &&
               (long long)nums[maxDeque[maxHead]] - (long long)nums[minDeque[minHead]] > 2) {
            if (maxDeque[maxHead] < minDeque[minHead]) {
                left = maxDeque[maxHead] + 1;
                ++maxHead;
            } else {
                left = minDeque[minHead] + 1;
                ++minHead;
            }
            while (maxHead <= maxTail && maxDeque[maxHead] < left) ++maxHead;
            while (minHead <= minTail && minDeque[minHead] < left) ++minHead;
        }

        ans += (long long)(right - left + 1);
    }

    free(maxDeque);
    free(minDeque);
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public long ContinuousSubarrays(int[] nums)
    {
        int n = nums.Length;
        var maxDeque = new System.Collections.Generic.LinkedList<int>();
        var minDeque = new System.Collections.Generic.LinkedList<int>();
        long ans = 0;
        int left = 0;

        for (int right = 0; right < n; ++right)
        {
            while (maxDeque.Count > 0 && nums[maxDeque.Last.Value] < nums[right])
                maxDeque.RemoveLast();
            maxDeque.AddLast(right);

            while (minDeque.Count > 0 && nums[minDeque.Last.Value] > nums[right])
                minDeque.RemoveLast();
            minDeque.AddLast(right);

            while (nums[maxDeque.First.Value] - nums[minDeque.First.Value] > 2)
            {
                if (maxDeque.First.Value == left) maxDeque.RemoveFirst();
                if (minDeque.First.Value == left) minDeque.RemoveFirst();
                left++;
            }

            ans += right - left + 1;
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var continuousSubarrays = function(nums) {
    const n = nums.length;
    let left = 0;
    let ans = 0;
    
    const maxDeque = []; // decreasing values, store indices
    const minDeque = []; // increasing values, store indices
    let maxHead = 0;
    let minHead = 0;
    
    for (let right = 0; right < n; ++right) {
        const val = nums[right];
        
        while (maxDeque.length > maxHead && nums[maxDeque[maxDeque.length - 1]] < val) {
            maxDeque.pop();
        }
        maxDeque.push(right);
        
        while (minDeque.length > minHead && nums[minDeque[minDeque.length - 1]] > val) {
            minDeque.pop();
        }
        minDeque.push(right);
        
        // shrink window until condition satisfied
        while (nums[maxDeque[maxHead]] - nums[minDeque[minHead]] > 2) {
            if (maxDeque[maxHead] === left) maxHead++;
            if (minDeque[minHead] === left) minHead++;
            left++;
        }
        
        ans += right - left + 1;
    }
    
    return ans;
};
```

## Typescript

```typescript
function continuousSubarrays(nums: number[]): number {
    const n = nums.length;
    const maxDeque: number[] = [];
    const minDeque: number[] = [];
    let maxHead = 0, minHead = 0;
    let left = 0;
    let ans = 0;

    for (let right = 0; right < n; ++right) {
        while (maxDeque.length > maxHead && nums[maxDeque[maxDeque.length - 1]] < nums[right]) {
            maxDeque.pop();
        }
        maxDeque.push(right);

        while (minDeque.length > minHead && nums[minDeque[minDeque.length - 1]] > nums[right]) {
            minDeque.pop();
        }
        minDeque.push(right);

        while (nums[maxDeque[maxHead]] - nums[minDeque[minHead]] > 2) {
            if (maxDeque[maxHead] === left) maxHead++;
            if (minDeque[minHead] === left) minHead++;
            left++;
        }

        ans += right - left + 1;
    }
    return ans;
}
```

## Php

```php
<?php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function continuousSubarrays($nums) {
        $n = count($nums);
        $maxDeque = new SplDoublyLinkedList(); // decreasing values
        $minDeque = new SplDoublyLinkedList(); // increasing values
        $left = 0;
        $count = 0;

        for ($right = 0; $right < $n; $right++) {
            // maintain max deque (decreasing)
            while (!$maxDeque->isEmpty() && $nums[$maxDeque->top()] < $nums[$right]) {
                $maxDeque->pop();
            }
            $maxDeque->push($right);

            // maintain min deque (increasing)
            while (!$minDeque->isEmpty() && $nums[$minDeque->top()] > $nums[$right]) {
                $minDeque->pop();
            }
            $minDeque->push($right);

            // shrink window until condition satisfied
            while ($nums[$maxDeque->bottom()] - $nums[$minDeque->bottom()] > 2) {
                $left++;
                while (!$maxDeque->isEmpty() && $maxDeque->bottom() < $left) {
                    $maxDeque->shift();
                }
                while (!$minDeque->isEmpty() && $minDeque->bottom() < $left) {
                    $minDeque->shift();
                }
            }

            $count += $right - $left + 1;
        }

        return $count;
    }
}
?>
```

## Swift

```swift
class Solution {
    func continuousSubarrays(_ nums: [Int]) -> Int {
        var maxDeque = [Int]()
        var minDeque = [Int]()
        var maxFront = 0
        var minFront = 0
        var left = 0
        var result: Int64 = 0
        let n = nums.count

        for right in 0..<n {
            let cur = nums[right]
            while maxDeque.count > maxFront && nums[maxDeque.last!] < cur {
                maxDeque.removeLast()
            }
            maxDeque.append(right)

            while minDeque.count > minFront && nums[minDeque.last!] > cur {
                minDeque.removeLast()
            }
            minDeque.append(right)

            while left <= right && (nums[maxDeque[maxFront]] - nums[minDeque[minFront]] > 2) {
                if maxDeque[maxFront] == left { maxFront += 1 }
                if minDeque[minFront] == left { minFront += 1 }
                left += 1
            }

            result += Int64(right - left + 1)

            if maxFront > 1000 {
                maxDeque.removeFirst(maxFront)
                maxFront = 0
            }
            if minFront > 1000 {
                minDeque.removeFirst(minFront)
                minFront = 0
            }
        }

        return Int(result)
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

class Solution {
    fun continuousSubarrays(nums: IntArray): Long {
        val n = nums.size
        val maxDeque = ArrayDeque<Int>()
        val minDeque = ArrayDeque<Int>()
        var left = 0
        var ans = 0L
        for (right in 0 until n) {
            while (!maxDeque.isEmpty() && nums[maxDeque.peekLast()] < nums[right]) {
                maxDeque.pollLast()
            }
            maxDeque.addLast(right)
            while (!minDeque.isEmpty() && nums[minDeque.peekLast()] > nums[right]) {
                minDeque.pollLast()
            }
            minDeque.addLast(right)

            while (nums[maxDeque.peekFirst()!!] - nums[minDeque.peekFirst()!!] > 2) {
                if (maxDeque.peekFirst() == left) maxDeque.pollFirst()
                if (minDeque.peekFirst() == left) minDeque.pollFirst()
                left++
            }
            ans += (right - left + 1).toLong()
        }
        return ans
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  int continuousSubarrays(List<int> nums) {
    var maxQ = Queue<int>();
    var minQ = Queue<int>();
    int left = 0;
    int count = 0;

    for (int right = 0; right < nums.length; ++right) {
      while (maxQ.isNotEmpty && nums[maxQ.last] < nums[right]) {
        maxQ.removeLast();
      }
      maxQ.addLast(right);

      while (minQ.isNotEmpty && nums[minQ.last] > nums[right]) {
        minQ.removeLast();
      }
      minQ.addLast(right);

      while (nums[maxQ.first] - nums[minQ.first] > 2) {
        left++;
        if (maxQ.isNotEmpty && maxQ.first < left) {
          maxQ.removeFirst();
        }
        if (minQ.isNotEmpty && minQ.first < left) {
          minQ.removeFirst();
        }
      }

      count += right - left + 1;
    }

    return count;
  }
}
```

## Golang

```go
func continuousSubarrays(nums []int) int64 {
    left := 0
    var ans int64 = 0
    minD := make([]int, 0)
    maxD := make([]int, 0)

    for right, v := range nums {
        // maintain decreasing max deque
        for len(maxD) > 0 && nums[maxD[len(maxD)-1]] < v {
            maxD = maxD[:len(maxD)-1]
        }
        maxD = append(maxD, right)

        // maintain increasing min deque
        for len(minD) > 0 && nums[minD[len(minD)-1]] > v {
            minD = minD[:len(minD)-1]
        }
        minD = append(minD, right)

        // shrink window while condition violated
        for len(maxD) > 0 && len(minD) > 0 && nums[maxD[0]]-nums[minD[0]] > 2 {
            left++
            if len(maxD) > 0 && maxD[0] < left {
                maxD = maxD[1:]
            }
            if len(minD) > 0 && minD[0] < left {
                minD = minD[1:]
            }
        }

        ans += int64(right - left + 1)
    }
    return ans
}
```

## Ruby

```ruby
def continuous_subarrays(nums)
  n = nums.length
  max_q = []
  min_q = []
  max_head = 0
  min_head = 0
  left = 0
  ans = 0

  (0...n).each do |right|
    val = nums[right]

    while max_q.length > max_head && nums[max_q[-1]] < val
      max_q.pop
    end
    max_q << right

    while min_q.length > min_head && nums[min_q[-1]] > val
      min_q.pop
    end
    min_q << right

    while left <= right && (nums[max_q[max_head]] - nums[min_q[min_head]] > 2)
      left += 1
      max_head += 1 while max_head < max_q.length && max_q[max_head] < left
      min_head += 1 while min_head < min_q.length && min_q[min_head] < left
    end

    ans += right - left + 1
  end

  ans
end
```

## Scala

```scala
import java.util.ArrayDeque

object Solution {
  def continuousSubarrays(nums: Array[Int]): Long = {
    val n = nums.length
    val maxQ = new ArrayDeque[Int]()
    val minQ = new ArrayDeque[Int]()
    var left = 0
    var ans: Long = 0L

    for (right <- 0 until n) {
      // maintain decreasing max deque
      while (!maxQ.isEmpty && nums(maxQ.peekLast) < nums(right)) {
        maxQ.pollLast()
      }
      maxQ.addLast(right)

      // maintain increasing min deque
      while (!minQ.isEmpty && nums(minQ.peekLast) > nums(right)) {
        minQ.pollLast()
      }
      minQ.addLast(right)

      // shrink window until condition satisfied
      while (!maxQ.isEmpty && !minQ.isEmpty && (nums(maxQ.peekFirst) - nums(minQ.peekFirst) > 2)) {
        if (maxQ.peekFirst == left) maxQ.pollFirst()
        if (minQ.peekFirst == left) minQ.pollFirst()
        left += 1
      }

      ans += (right - left + 1).toLong
    }

    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn continuous_subarrays(nums: Vec<i32>) -> i64 {
        use std::collections::VecDeque;
        let n = nums.len();
        let mut max_q: VecDeque<usize> = VecDeque::new(); // decreasing values
        let mut min_q: VecDeque<usize> = VecDeque::new(); // increasing values
        let mut left = 0usize;
        let mut ans: i64 = 0;

        for right in 0..n {
            while let Some(&idx) = max_q.back() {
                if nums[idx] <= nums[right] {
                    max_q.pop_back();
                } else {
                    break;
                }
            }
            max_q.push_back(right);

            while let Some(&idx) = min_q.back() {
                if nums[idx] >= nums[right] {
                    min_q.pop_back();
                } else {
                    break;
                }
            }
            min_q.push_back(right);

            loop {
                let max_val = nums[*max_q.front().unwrap()];
                let min_val = nums[*min_q.front().unwrap()];
                if max_val - min_val <= 2 {
                    break;
                }
                if *max_q.front().unwrap() == left {
                    max_q.pop_front();
                }
                if *min_q.front().unwrap() == left {
                    min_q.pop_front();
                }
                left += 1;
            }

            ans += (right - left + 1) as i64;
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (continuous-subarrays nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (vec (list->vector nums)))
    (if (= n 0)
        0
        (let ((maxQ (make-vector n 0))
              (minQ (make-vector n 0)))
          (let loop ((right 0) (left 0)
                     (maxHead 0) (maxTail 0)
                     (minHead 0) (minTail 0)
                     (ans 0))
            (if (= right n)
                ans
                (let* ((val (vector-ref vec right))
                       ;; maintain max deque (decreasing)
                       (newMaxTail
                        (let recur ((mt maxTail))
                          (if (and (> mt maxHead)
                                   (< (vector-ref vec (vector-ref maxQ (- mt 1))) val))
                              (recur (- mt 1))
                              mt)))
                       (maxTailAfterPush newMaxTail)
                       ;; push current index
                       (begin
                         (vector-set! maxQ newMaxTail right)
                         (set! newMaxTail (+ newMaxTail 1))))
                       ;; maintain min deque (increasing)
                       (newMinTail
                        (let recur ((mt minTail))
                          (if (and (> mt minHead)
                                   (> (vector-ref vec (vector-ref minQ (- mt 1))) val))
                              (recur (- mt 1))
                              mt)))
                       (minTailAfterPush newMinTail)
                       (begin
                         (vector-set! minQ newMinTail right)
                         (set! newMinTail (+ newMinTail 1))))
                       ;; shrink window while invalid
                       (let shrink ((l left) (mh maxHead) (mt newMaxTail) (nh minHead) (nt newMinTail))
                         (if (> (- (vector-ref vec (vector-ref maxQ mh))
                                   (vector-ref vec (vector-ref minQ nh))) 2)
                             (let* ((mh2 (if (= (vector-ref maxQ mh) l) (+ mh 1) mh))
                                    (nh2 (if (= (vector-ref minQ nh) l) (+ nh 1) nh)))
                               (shrink (+ l 1) mh2 mt nh2 nt))
                             (let ((newAns (+ ans (+ (- right l) 1))))
                               (loop (+ right 1) l mh mt nh nt newAns)))))))))))
```

## Erlang

```erlang
-module(solution).
-export([continuous_subarrays/1]).

-spec continuous_subarrays(Nums :: [integer()]) -> integer().
continuous_subarrays(Nums) ->
    Tuple = list_to_tuple(Nums),
    Len = tuple_size(Tuple),
    loop(Tuple, 0, 0, gb_trees:empty(), 0, Len).

loop(_Tuple, RightIdx, _LeftIdx, _Tree, Count, Len) when RightIdx == Len ->
    Count;
loop(Tuple, RightIdx, LeftIdx, Tree, Count, Len) ->
    Val = element(RightIdx + 1, Tuple),
    Tree1 = insert_or_increment(Tree, Val),
    {NewLeft, NewTree} = shrink_window(Tuple, LeftIdx, RightIdx, Tree1),
    NewCount = Count + (RightIdx - NewLeft + 1),
    loop(Tuple, RightIdx + 1, NewLeft, NewTree, NewCount, Len).

shrink_window(Tuple, LeftIdx, _RightIdx, Tree) ->
    case diff_ok(Tree) of
        true -> {LeftIdx, Tree};
        false ->
            Val = element(LeftIdx + 1, Tuple),
            NewTree = decrement_or_remove(Tree, Val),
            shrink_window(Tuple, LeftIdx + 1, _RightIdx, NewTree)
    end.

diff_ok(Tree) ->
    case gb_trees:is_empty(Tree) of
        true -> true;
        false ->
            {Min, _} = gb_trees:smallest(Tree),
            {Max, _} = gb_trees:largest(Tree),
            Max - Min =< 2
    end.

insert_or_increment(Tree, Val) ->
    case gb_trees:lookup(Val, Tree) of
        none -> gb_trees:insert(Val, 1, Tree);
        {value, C} -> gb_trees:update(Val, C + 1, Tree)
    end.

decrement_or_remove(Tree, Val) ->
    case gb_trees:lookup(Val, Tree) of
        {value, 1} -> gb_trees:delete(Val, Tree);
        {value, C} -> gb_trees:update(Val, C - 1, Tree)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec continuous_subarrays(nums :: [integer]) :: integer
  def continuous_subarrays(nums) do
    arr = :array.from_list(nums)
    n = length(nums)

    {_, _, _, ans} =
      Enum.reduce(0..(n - 1), {:queue.new(), :queue.new(), 0, 0}, fn i,
                                                                    {min_q, max_q, left, acc} ->
        min_q = push_min(min_q, arr, i)
        max_q = push_max(max_q, arr, i)

        {new_left, new_min_q, new_max_q} = shrink_window(left, min_q, max_q, arr)

        new_acc = acc + (i - new_left + 1)
        {new_min_q, new_max_q, new_left, new_acc}
      end)

    ans
  end

  defp push_min(q, arr, idx) do
    v = :array.get(idx, arr)

    case :queue.peek_r(q) do
      {:value, last_idx} ->
        if :array.get(last_idx, arr) > v do
          {_pop_val, q2} = :queue.out_r(q)
          push_min(q2, arr, idx)
        else
          :queue.in(idx, q)
        end

      :empty ->
        :queue.in(idx, q)
    end
  end

  defp push_max(q, arr, idx) do
    v = :array.get(idx, arr)

    case :queue.peek_r(q) do
      {:value, last_idx} ->
        if :array.get(last_idx, arr) < v do
          {_pop_val, q2} = :queue.out_r(q)
          push_max(q2, arr, idx)
        else
          :queue.in(idx, q)
        end

      :empty ->
        :queue.in(idx, q)
    end
  end

  defp shrink_window(left, min_q, max_q, arr) do
    case {:queue.peek(min_q), :queue.peek(max_q)} do
      {{:value, min_idx}, {:value, max_idx}} ->
        min_val = :array.get(min_idx, arr)
        max_val = :array.get(max_idx, arr)

        if max_val - min_val > 2 do
          new_left = left + 1
          new_min_q = drop_front(min_q, new_left)
          new_max_q = drop_front(max_q, new_left)
          shrink_window(new_left, new_min_q, new_max_q, arr)
        else
          {left, min_q, max_q}
        end

      _ ->
        {left, min_q, max_q}
    end
  end

  defp drop_front(q, left) do
    case :queue.peek(q) do
      {:value, idx} when idx < left ->
        {_val, q2} = :queue.out(q)
        drop_front(q2, left)

      _ ->
        q
    end
  end
end
```
