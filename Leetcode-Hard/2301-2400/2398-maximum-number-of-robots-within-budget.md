# 2398. Maximum Number of Robots Within Budget

## Cpp

```cpp
class Solution {
public:
    int maximumRobots(vector<int>& chargeTimes, vector<int>& runningCosts, long long budget) {
        int n = chargeTimes.size();
        deque<int> dq; // indices with decreasing chargeTimes
        long long sumRun = 0;
        int left = 0, ans = 0;
        for (int right = 0; right < n; ++right) {
            sumRun += runningCosts[right];
            while (!dq.empty() && chargeTimes[dq.back()] <= chargeTimes[right])
                dq.pop_back();
            dq.push_back(right);
            while (left <= right) {
                long long maxCharge = chargeTimes[dq.front()];
                long long cost = maxCharge + 1LL * (right - left + 1) * sumRun;
                if (cost <= budget) break;
                // shrink window
                sumRun -= runningCosts[left];
                if (!dq.empty() && dq.front() == left) dq.pop_front();
                ++left;
            }
            ans = max(ans, right - left + 1);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maximumRobots(int[] chargeTimes, int[] runningCosts, long budget) {
        int n = chargeTimes.length;
        Deque<Integer> deque = new ArrayDeque<>();
        long sumRunning = 0;
        int left = 0;
        int maxLen = 0;

        for (int right = 0; right < n; ++right) {
            sumRunning += runningCosts[right];
            while (!deque.isEmpty() && chargeTimes[deque.peekLast()] <= chargeTimes[right]) {
                deque.pollLast();
            }
            deque.offerLast(right);

            while (left <= right) {
                long maxCharge = chargeTimes[deque.peekFirst()];
                long cost = maxCharge + (long) (right - left + 1) * sumRunning;
                if (cost <= budget) {
                    break;
                }
                sumRunning -= runningCosts[left];
                if (!deque.isEmpty() && deque.peekFirst() == left) {
                    deque.pollFirst();
                }
                left++;
            }

            maxLen = Math.max(maxLen, right - left + 1);
        }

        return maxLen;
    }
}
```

## Python

```python
class Solution(object):
    def maximumRobots(self, chargeTimes, runningCosts, budget):
        """
        :type chargeTimes: List[int]
        :type runningCosts: List[int]
        :type budget: int
        :rtype: int
        """
        from collections import deque

        n = len(chargeTimes)
        dq = deque()          # stores indices with decreasing chargeTimes
        left = 0
        sum_run = 0
        best = 0

        for right in range(n):
            sum_run += runningCosts[right]

            while dq and chargeTimes[dq[-1]] <= chargeTimes[right]:
                dq.pop()
            dq.append(right)

            # shrink window until cost within budget
            while left <= right:
                max_charge = chargeTimes[dq[0]]
                total_cost = max_charge + (right - left + 1) * sum_run
                if total_cost <= budget:
                    break
                # move left pointer forward
                sum_run -= runningCosts[left]
                if dq[0] == left:
                    dq.popleft()
                left += 1

            best = max(best, right - left + 1)

        return best
```

## Python3

```python
import collections
from typing import List

class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        left = 0
        sum_run = 0
        max_len = 0
        dq = collections.deque()  # stores indices with decreasing chargeTimes
        
        for right in range(n):
            sum_run += runningCosts[right]
            while dq and chargeTimes[dq[-1]] <= chargeTimes[right]:
                dq.pop()
            dq.append(right)
            
            while left <= right:
                max_charge = chargeTimes[dq[0]]
                total_cost = max_charge + (right - left + 1) * sum_run
                if total_cost <= budget:
                    break
                # shrink window from left
                sum_run -= runningCosts[left]
                if dq[0] == left:
                    dq.popleft()
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len
```

## C

```c
int maximumRobots(int* chargeTimes, int chargeTimesSize, int* runningCosts, int runningCostsSize, long long budget) {
    int n = chargeTimesSize;
    int *dq = (int*)malloc(n * sizeof(int));
    int head = 0, tail = 0; // deque for indices with decreasing chargeTimes
    long long sumRunning = 0;
    int left = 0;
    int maxLen = 0;

    for (int right = 0; right < n; ++right) {
        sumRunning += runningCosts[right];
        while (tail > head && chargeTimes[dq[tail - 1]] <= chargeTimes[right]) {
            --tail;
        }
        dq[tail++] = right;

        // shrink window until cost within budget
        while (left <= right) {
            long long maxCharge = chargeTimes[dq[head]];
            int len = right - left + 1;
            long long cost = maxCharge + (long long)len * sumRunning;
            if (cost <= budget) break;

            // move left forward
            if (dq[head] == left) {
                ++head;
            }
            sumRunning -= runningCosts[left];
            ++left;
        }

        int currentLen = right - left + 1;
        if (currentLen > maxLen) maxLen = currentLen;
    }

    free(dq);
    return maxLen;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int MaximumRobots(int[] chargeTimes, int[] runningCosts, long budget) {
        int n = chargeTimes.Length;
        var maxDeque = new LinkedList<int>(); // stores indices with decreasing chargeTimes
        long sumRunning = 0;
        int left = 0;
        int best = 0;

        for (int right = 0; right < n; right++) {
            sumRunning += runningCosts[right];

            while (maxDeque.Count > 0 && chargeTimes[maxDeque.Last.Value] <= chargeTimes[right]) {
                maxDeque.RemoveLast();
            }
            maxDeque.AddLast(right);

            // shrink window until cost fits budget
            while (left <= right) {
                long currentMax = chargeTimes[maxDeque.First.Value];
                long cost = currentMax + (long)(right - left + 1) * sumRunning;
                if (cost <= budget) break;

                if (maxDeque.First != null && maxDeque.First.Value == left) {
                    maxDeque.RemoveFirst();
                }
                sumRunning -= runningCosts[left];
                left++;
            }

            int length = right - left + 1;
            if (length > best) best = length;
        }

        return best;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} chargeTimes
 * @param {number[]} runningCosts
 * @param {number} budget
 * @return {number}
 */
var maximumRobots = function(chargeTimes, runningCosts, budget) {
    const n = chargeTimes.length;
    let left = 0;
    let sumRunning = 0;
    let ans = 0;
    const deque = []; // indices with decreasing chargeTimes

    for (let right = 0; right < n; ++right) {
        sumRunning += runningCosts[right];
        while (deque.length && chargeTimes[deque[deque.length - 1]] <= chargeTimes[right]) {
            deque.pop();
        }
        deque.push(right);

        // shrink window until cost fits budget
        while (left <= right) {
            const maxCharge = chargeTimes[deque[0]];
            const len = right - left + 1;
            const cost = maxCharge + len * sumRunning;
            if (cost <= budget) break;

            if (deque[0] === left) deque.shift();
            sumRunning -= runningCosts[left];
            left++;
        }

        ans = Math.max(ans, right - left + 1);
    }
    return ans;
};
```

## Typescript

```typescript
function maximumRobots(chargeTimes: number[], runningCosts: number[], budget: number): number {
    const n = chargeTimes.length;
    const can = (k: number): boolean => {
        if (k === 0) return true;
        let sum = 0;
        const deque: number[] = [];
        for (let i = 0; i < n; i++) {
            sum += runningCosts[i];
            while (deque.length && chargeTimes[deque[deque.length - 1]] <= chargeTimes[i]) {
                deque.pop();
            }
            deque.push(i);
            if (i >= k - 1) {
                const maxCharge = chargeTimes[deque[0]];
                const cost = maxCharge + k * sum;
                if (cost <= budget) return true;
                const leftIdx = i - k + 1;
                sum -= runningCosts[leftIdx];
                if (deque[0] === leftIdx) deque.shift();
            }
        }
        return false;
    };
    let low = 0, high = n;
    while (low < high) {
        const mid = Math.floor((low + high + 1) / 2);
        if (can(mid)) low = mid; else high = mid - 1;
    }
    return low;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $chargeTimes
     * @param Integer[] $runningCosts
     * @param Integer $budget
     * @return Integer
     */
    function maximumRobots($chargeTimes, $runningCosts, $budget) {
        $n = count($chargeTimes);
        $left = 0;
        $sumRunning = 0;
        $maxLen = 0;

        $deque = [];   // stores indices with decreasing chargeTimes
        $head = 0;     // logical front pointer

        for ($right = 0; $right < $n; ++$right) {
            $sumRunning += $runningCosts[$right];

            // maintain decreasing deque for max charge time
            while (count($deque) > $head && $chargeTimes[end($deque)] <= $chargeTimes[$right]) {
                array_pop($deque);
            }
            $deque[] = $right;

            // shrink window until cost within budget
            while ($left <= $right) {
                $maxCharge = $chargeTimes[$deque[$head]];
                $cost = $maxCharge + ($right - $left + 1) * $sumRunning;
                if ($cost <= $budget) {
                    break;
                }
                // remove left element
                $sumRunning -= $runningCosts[$left];
                if ($deque[$head] == $left) {
                    ++$head; // pop front logically
                }
                ++$left;
            }

            $maxLen = max($maxLen, $right - $left + 1);
        }

        return $maxLen;
    }
}
```

## Swift

```swift
class Solution {
    func maximumRobots(_ chargeTimes: [Int], _ runningCosts: [Int], _ budget: Int) -> Int {
        let n = chargeTimes.count
        var maxDeque = [Int]()          // stores indices, decreasing chargeTimes
        var front = 0                  // logical front pointer
        var left = 0
        var sumRunning: Int64 = 0
        let budgetVal = Int64(budget)
        var answer = 0

        for right in 0..<n {
            sumRunning += Int64(runningCosts[right])
            while maxDeque.count > front && chargeTimes[maxDeque.last!] <= chargeTimes[right] {
                maxDeque.removeLast()
            }
            maxDeque.append(right)

            // shrink window until cost fits budget
            while left <= right {
                if front >= maxDeque.count { break }   // empty deque, window is empty
                let currentMax = chargeTimes[maxDeque[front]]
                let cost = Int64(currentMax) + Int64(right - left + 1) * sumRunning
                if cost <= budgetVal { break }
                if maxDeque[front] == left {
                    front += 1
                }
                sumRunning -= Int64(runningCosts[left])
                left += 1
            }

            answer = max(answer, right - left + 1)
        }

        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumRobots(chargeTimes: IntArray, runningCosts: IntArray, budget: Long): Int {
        val n = chargeTimes.size
        var left = 0
        var sumRunning = 0L
        var maxLen = 0
        val deque = java.util.ArrayDeque<Int>()
        for (right in 0 until n) {
            sumRunning += runningCosts[right].toLong()
            while (!deque.isEmpty() && chargeTimes[deque.peekLast()] <= chargeTimes[right]) {
                deque.pollLast()
            }
            deque.offerLast(right)
            while (left <= right) {
                val maxCharge = chargeTimes[deque.peekFirst()]
                val windowSize = right - left + 1
                val totalCost = maxCharge.toLong() + windowSize.toLong() * sumRunning
                if (totalCost <= budget) break
                if (deque.peekFirst() == left) deque.pollFirst()
                sumRunning -= runningCosts[left].toLong()
                left++
            }
            maxLen = kotlin.math.max(maxLen, right - left + 1)
        }
        return maxLen
    }
}
```

## Dart

```dart
class Solution {
  int maximumRobots(List<int> chargeTimes, List<int> runningCosts, int budget) {
    int n = chargeTimes.length;
    int left = 0;
    int sumRunning = 0;
    List<int> dq = []; // stores indices with decreasing chargeTimes
    int head = 0; // logical front of deque
    int ans = 0;

    for (int right = 0; right < n; ++right) {
      sumRunning += runningCosts[right];

      while (dq.isNotEmpty && chargeTimes[dq.last] <= chargeTimes[right]) {
        dq.removeLast();
      }
      dq.add(right);

      // shrink window until cost fits budget
      while (left <= right) {
        int maxCharge = chargeTimes[dq[head]];
        int len = right - left + 1;
        int cost = maxCharge + len * sumRunning;
        if (cost <= budget) break;

        if (dq[head] == left) {
          head++;
          // occasional cleanup to avoid unbounded growth
          if (head > 100 && head * 2 > dq.length) {
            dq = dq.sublist(head);
            head = 0;
          }
        }
        sumRunning -= runningCosts[left];
        left++;
      }

      int len = right - left + 1;
      if (len > ans) ans = len;
    }

    return ans;
  }
}
```

## Golang

```go
func maximumRobots(chargeTimes []int, runningCosts []int, budget int64) int {
    n := len(chargeTimes)
    left := 0
    var sumRunning int64 = 0
    maxLen := 0
    deque := make([]int, 0) // stores indices with decreasing chargeTimes

    for right := 0; right < n; right++ {
        sumRunning += int64(runningCosts[right])

        // maintain decreasing deque for chargeTimes
        for len(deque) > 0 && chargeTimes[deque[len(deque)-1]] <= chargeTimes[right] {
            deque = deque[:len(deque)-1]
        }
        deque = append(deque, right)

        // shrink window while cost exceeds budget
        for left <= right {
            maxCharge := chargeTimes[deque[0]]
            totalCost := int64(maxCharge) + int64(right-left+1)*sumRunning
            if totalCost <= budget {
                break
            }
            // remove leftmost element from window
            if deque[0] == left {
                deque = deque[1:]
            }
            sumRunning -= int64(runningCosts[left])
            left++
        }

        curLen := right - left + 1
        if curLen > maxLen {
            maxLen = curLen
        }
    }

    return maxLen
}
```

## Ruby

```ruby
def maximum_robots(charge_times, running_costs, budget)
  n = charge_times.length
  sum = 0
  max_len = 0
  left = 0
  deq = []
  head = 0

  (0...n).each do |right|
    sum += running_costs[right]

    while deq.length > head && charge_times[deq[-1]] <= charge_times[right]
      deq.pop
    end
    deq << right

    loop do
      break if left > right
      max_charge = charge_times[deq[head]]
      cost = max_charge + (right - left + 1) * sum
      break if cost <= budget

      sum -= running_costs[left]
      head += 1 if deq[head] == left
      left += 1
    end

    current_len = right - left + 1
    max_len = current_len if current_len > max_len
  end

  max_len
end
```

## Scala

```scala
object Solution {
  def maximumRobots(chargeTimes: Array[Int], runningCosts: Array[Int], budget: Long): Int = {
    val n = chargeTimes.length

    def can(k: Int): Boolean = {
      if (k == 0) return true
      import scala.collection.mutable.ArrayDeque
      val dq = new ArrayDeque[Int]()
      var sum: Long = 0L
      for (i <- 0 until n) {
        sum += runningCosts(i)
        while (dq.nonEmpty && chargeTimes(dq.last) <= chargeTimes(i)) dq.removeLast()
        dq.append(i)

        if (i >= k) {
          sum -= runningCosts(i - k)
          if (dq.head == i - k) dq.removeHead()
        }

        if (i >= k - 1) {
          val maxCharge = chargeTimes(dq.head).toLong
          val cost = maxCharge + k.toLong * sum
          if (cost <= budget) return true
        }
      }
      false
    }

    var left = 0
    var right = n
    while (left < right) {
      val mid = (left + right + 1) / 2
      if (can(mid)) left = mid else right = mid - 1
    }
    left
  }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_robots(charge_times: Vec<i32>, running_costs: Vec<i32>, budget: i64) -> i32 {
        let n = charge_times.len();

        fn can(len: usize, charge: &Vec<i32>, run: &Vec<i32>, budget: i64) -> bool {
            if len == 0 {
                return true;
            }
            use std::collections::VecDeque;
            let mut sum: i64 = 0;
            let mut dq: VecDeque<usize> = VecDeque::new();

            for i in 0..charge.len() {
                sum += run[i] as i64;

                while let Some(&back) = dq.back() {
                    if charge[back] <= charge[i] {
                        dq.pop_back();
                    } else {
                        break;
                    }
                }
                dq.push_back(i);

                if i + 1 > len {
                    let out = i - len;
                    sum -= run[out] as i64;
                    if let Some(&front) = dq.front() {
                        if front == out {
                            dq.pop_front();
                        }
                    }
                }

                if i + 1 >= len {
                    let max_charge = charge[*dq.front().unwrap()] as i64;
                    let cost = max_charge + (len as i64) * sum;
                    if cost <= budget {
                        return true;
                    }
                }
            }
            false
        }

        let mut lo: usize = 0;
        let mut hi: usize = n;
        while lo < hi {
            let mid = (lo + hi + 1) / 2;
            if can(mid, &charge_times, &running_costs, budget) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        lo as i32
    }
}
```

## Racket

```racket
(define/contract (maximum-robots chargeTimes runningCosts budget)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((ct (list->vector chargeTimes))
         (rc (list->vector runningCosts))
         (n (vector-length ct)))
    (let ((sum 0)
          (left 0)
          (maxlen 0)
          (dq (make-vector n))
          (head 0)
          (tail 0))
      (let loop ((right 0) (sum sum) (left left) (maxlen maxlen) (head head) (tail tail))
        (if (= right n)
            maxlen
            (begin
              ;; add new robot
              (set! sum (+ sum (vector-ref rc right)))
              ;; maintain decreasing deque for chargeTimes
              (let pop-back ()
                (when (and (< head tail)
                           (<= (vector-ref ct (vector-ref dq (- tail 1))) (vector-ref ct right)))
                  (set! tail (- tail 1))
                  (pop-back)))
              (vector-set! dq tail right)
              (set! tail (+ tail 1))
              ;; shrink window while cost exceeds budget
              (let shrink ()
                (when (and (<= left right)
                           (> (+ (vector-ref ct (vector-ref dq head))
                                 (* (+ (- right left) 1) sum)) budget))
                  (when (= (vector-ref dq head) left)
                    (set! head (+ head 1)))
                  (set! sum (- sum (vector-ref rc left)))
                  (set! left (+ left 1))
                  (shrink)))
              ;; update answer
              (let ((currlen (+ (- right left) 1)))
                (when (> currlen maxlen)
                  (set! maxlen currlen)))
              (loop (+ right 1) sum left maxlen head tail)))))))
```

## Erlang

```erlang
-spec maximum_robots(ChargeTimes :: [integer()], RunningCosts :: [integer()], Budget :: integer()) -> integer().
maximum_robots(ChargeTimes, RunningCosts, Budget) ->
    N = length(ChargeTimes),
    Prefix = build_prefix(RunningCosts),
    SegTree = build_seg(ChargeTimes),
    binary_search(0, N, Prefix, SegTree, Budget, 0).

build_prefix(RCs) ->
    build_prefix_loop(RCs, 0, 0, array:new(length(RCs) + 1, {default, 0})).

build_prefix_loop([], _Idx, _Acc, Arr) -> Arr;
build_prefix_loop([H|T], Idx, Acc, Arr) ->
    NewAcc = Acc + H,
    NewArr = array:set(Idx + 1, NewAcc, Arr),
    build_prefix_loop(T, Idx + 1, NewAcc, NewArr).

build_seg(ChargeTimes) ->
    N = length(ChargeTimes),
    Size = next_power_of_two(N),
    TreeSize = 2 * Size,
    EmptyTree = array:new(TreeSize, {default, 0}),
    ChargeArr = array:from_list(ChargeTimes),
    TreeWithLeaves = fill_leaves(ChargeArr, EmptyTree, Size, 0, N),
    FullTree = build_internal(Size - 1, TreeWithLeaves),
    {Size, FullTree}.

next_power_of_two(N) -> next_pow(N, 1).
next_pow(N, P) when P >= N -> P;
next_pow(N, P) -> next_pow(N, P * 2).

fill_leaves(_ChargeArr, Tree, _Size, I, N) when I >= N -> Tree;
fill_leaves(ChargeArr, Tree, Size, I, N) ->
    Val = array:get(I + 1, ChargeArr),
    Index = Size + I,
    NewTree = array:set(Index, Val, Tree),
    fill_leaves(ChargeArr, NewTree, Size, I + 1, N).

build_internal(0, Tree) -> Tree;
build_internal(I, Tree) ->
    Left = array:get(2 * I, Tree),
    Right = array:get(2 * I + 1, Tree),
    MaxVal = erlang:max(Left, Right),
    NewTree = array:set(I, MaxVal, Tree),
    build_internal(I - 1, NewTree).

range_max({Size, Tree}, L0, R0) ->
    loop_range(L0 + Size, R0 + Size, Tree, 0).

loop_range(L, R, Tree, Max) when L =< R ->
    Max1 = case (L band 1) of
               1 -> erlang:max(Max, array:get(L, Tree));
               _ -> Max
           end,
    Max2 = case (R band 1) of
               0 -> erlang:max(Max1, array:get(R, Tree));
               _ -> Max1
           end,
    L1 = L bsr 1,
    R1 = R bsr 1,
    loop_range(L1, R1, Tree, Max2);
loop_range(_, _, _, Max) -> Max.

feasible(0, _Prefix, _SegTree, _Budget) -> true;
feasible(K, Prefix, SegTree, Budget) ->
    N = array:size(Prefix) - 1,
    MaxStart = N - K,
    feasible_loop(0, MaxStart, K, Prefix, SegTree, Budget).

feasible_loop(I, MaxI, _K, _Prefix, _SegTree, _Budget) when I > MaxI -> false;
feasible_loop(I, MaxI, K, Prefix, SegTree, Budget) ->
    SumRunning = array:get(I + K, Prefix) - array:get(I, Prefix),
    MaxCharge = range_max(SegTree, I, I + K - 1),
    Cost = MaxCharge + K * SumRunning,
    if
        Cost =< Budget -> true;
        true -> feasible_loop(I + 1, MaxI, K, Prefix, SegTree, Budget)
    end.

binary_search(Low, High, _Prefix, _SegTree, _Budget, Best) when Low > High ->
    Best;
binary_search(Low, High, Prefix, SegTree, Budget, _Best) ->
    Mid = (Low + High) div 2,
    case feasible(Mid, Prefix, SegTree, Budget) of
        true -> binary_search(Mid + 1, High, Prefix, SegTree, Budget, Mid);
        false -> binary_search(Low, Mid - 1, Prefix, SegTree, Budget, Best)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_robots(charge_times :: [integer], running_costs :: [integer], budget :: integer) :: integer
  def maximum_robots(charge_times, running_costs, budget) do
    n = length(charge_times)
    ct = List.to_tuple(charge_times)
    rc = List.to_tuple(running_costs)

    {_left, _sum_running, _deque, ans} =
      Enum.reduce(0..(n - 1), {0, 0, :queue.new(), 0}, fn right,
                                                       {left, sum_running, deque, ans} ->
        sum_running = sum_running + elem(rc, right)

        # maintain decreasing order of charge times in the deque
        deque = clean_back(deque, ct, elem(ct, right))
        deque = :queue.in(right, deque)

        {left, sum_running, deque} =
          shrink_window(left, sum_running, deque, ct, rc, budget, right)

        ans = if right - left + 1 > ans, do: right - left + 1, else: ans
        {left, sum_running, deque, ans}
      end)

    ans
  end

  defp clean_back(deque, ct, cur_val) do
    case :queue.peek_r(deque) do
      false ->
        deque

      {:value, idx_back} ->
        if cur_val >= elem(ct, idx_back) do
          {_out_elem, new_deque} = :queue.out_r(deque)
          clean_back(new_deque, ct, cur_val)
        else
          deque
        end
    end
  end

  defp shrink_window(left, sum_running, deque, ct, rc, budget, right) do
    case :queue.peek(deque) do
      false ->
        {left, sum_running, deque}

      {:value, max_idx} ->
        max_charge = elem(ct, max_idx)
        total_cost = max_charge + (right - left + 1) * sum_running

        if total_cost <= budget do
          {left, sum_running, deque}
        else
          # move left pointer forward
          sum_running = sum_running - elem(rc, left)

          deque =
            case :queue.peek(deque) do
              {:value, ^left} ->
                {_out_elem, new_deq} = :queue.out(deque)
                new_deq

              _ ->
                deque
            end

          shrink_window(left + 1, sum_running, deque, ct, rc, budget, right)
        end
    end
  end
end
```
