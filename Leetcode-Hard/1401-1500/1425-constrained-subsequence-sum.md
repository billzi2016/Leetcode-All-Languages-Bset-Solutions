# 1425. Constrained Subsequence Sum

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int constrainedSubsetSum(vector<int>& nums, int k) {
        int n = nums.size();
        vector<long long> dp(n);
        deque<int> dq;
        long long ans = LLONG_MIN;
        for (int i = 0; i < n; ++i) {
            while (!dq.empty() && dq.front() < i - k) dq.pop_front();
            long long best = dq.empty() ? 0 : dp[dq.front()];
            dp[i] = nums[i] + max(0LL, best);
            ans = max(ans, dp[i]);
            while (!dq.empty() && dp[dq.back()] <= dp[i]) dq.pop_back();
            if (dp[i] > 0) dq.push_back(i);
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    public int constrainedSubsetSum(int[] nums, int k) {
        int n = nums.length;
        int[] dp = new int[n];
        java.util.ArrayDeque<Integer> deque = new java.util.ArrayDeque<>();
        int ans = Integer.MIN_VALUE;

        for (int i = 0; i < n; i++) {
            // Remove indices out of the window [i-k, i-1]
            while (!deque.isEmpty() && i - deque.peekFirst() > k) {
                deque.pollFirst();
            }

            int bestPrev = deque.isEmpty() ? 0 : dp[deque.peekFirst()];
            if (bestPrev < 0) bestPrev = 0; // safety, though deque stores only positive dp

            dp[i] = nums[i] + bestPrev;
            ans = Math.max(ans, dp[i]);

            // Maintain decreasing order of dp values in the deque
            while (!deque.isEmpty() && dp[deque.peekLast()] <= dp[i]) {
                deque.pollLast();
            }

            if (dp[i] > 0) {
                deque.addLast(i);
            }
        }

        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import deque

        n = len(nums)
        dp = [0] * n
        dq = deque()
        ans = -10**9  # initialize with very small number

        for i in range(n):
            # Remove indices out of the window [i-k, i-1]
            while dq and i - dq[0] > k:
                dq.popleft()

            # Best previous sum within distance k
            best = dp[dq[0]] if dq else 0

            dp[i] = nums[i] + (best if best > 0 else 0)

            ans = max(ans, dp[i])

            # Maintain deque decreasing by dp value
            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()

            if dp[i] > 0:
                dq.append(i)

        return ans
```

## Python3

```python
from collections import deque
from typing import List

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dq = deque()
        ans = nums[0]

        for i in range(n):
            # Remove indices out of the window
            while dq and i - dq[0] > k:
                dq.popleft()

            best = dp[dq[0]] if dq else 0
            dp[i] = nums[i] + (best if best > 0 else 0)

            ans = max(ans, dp[i])

            # Maintain decreasing order of dp values in deque
            while dq and dp[i] >= dp[dq[-1]]:
                dq.pop()
            if dp[i] > 0:
                dq.append(i)

        return ans
```

## C

```c
#include <stdlib.h>

int constrainedSubsetSum(int* nums, int numsSize, int k) {
    if (numsSize == 0) return 0;
    
    long long *dp = (long long *)malloc(sizeof(long long) * numsSize);
    int *dq = (int *)malloc(sizeof(int) * numsSize);   // monotonic deque storing indices
    int head = 0, tail = -1;                           // empty deque
    
    dp[0] = nums[0];
    long long ans = dp[0];
    if (dp[0] > 0) {
        dq[++tail] = 0;
    }
    
    for (int i = 1; i < numsSize; ++i) {
        // Remove indices out of the window [i-k, i-1]
        while (head <= tail && i - dq[head] > k) head++;
        
        long long bestPrev = 0;
        if (head <= tail && dp[dq[head]] > 0) {
            bestPrev = dp[dq[head]];
        }
        dp[i] = nums[i] + bestPrev;
        if (dp[i] > ans) ans = dp[i];
        
        // Maintain decreasing order of dp values in deque
        while (head <= tail && dp[dq[tail]] < dp[i]) tail--;
        if (dp[i] > 0) {
            dq[++tail] = i;
        }
    }
    
    free(dp);
    free(dq);
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int ConstrainedSubsetSum(int[] nums, int k) {
        int n = nums.Length;
        long[] dp = new long[n];
        var deque = new LinkedList<int>();
        long answer = nums[0];

        for (int i = 0; i < n; i++) {
            // Remove indices that are out of the window [i-k, i-1]
            while (deque.First != null && i - deque.First.Value > k) {
                deque.RemoveFirst();
            }

            long bestPrev = deque.First != null ? dp[deque.First.Value] : 0;
            if (bestPrev < 0) bestPrev = 0;

            dp[i] = nums[i] + bestPrev;
            if (dp[i] > answer) answer = dp[i];

            // Maintain decreasing order of dp values in deque
            while (deque.Last != null && dp[deque.Last.Value] <= dp[i]) {
                deque.RemoveLast();
            }

            if (dp[i] > 0) {
                deque.AddLast(i);
            }
        }

        return (int)answer;
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
var constrainedSubsetSum = function(nums, k) {
    const n = nums.length;
    const dp = new Array(n);
    const dq = new Array(n); // store indices with decreasing dp values
    let front = 0, back = -1; // deque boundaries
    let ans = -Infinity;

    for (let i = 0; i < n; ++i) {
        // Remove indices out of the window [i-k, i-1]
        while (front <= back && dq[front] < i - k) {
            front++;
        }

        const best = (front <= back) ? Math.max(0, dp[dq[front]]) : 0;
        dp[i] = nums[i] + best;
        if (dp[i] > ans) ans = dp[i];

        // Maintain decreasing order of dp values in deque
        while (front <= back && dp[dq[back]] <= dp[i]) {
            back--;
        }

        // Only positive dp can help future elements
        if (dp[i] > 0) {
            dq[++back] = i;
        }
    }

    return ans;
};
```

## Typescript

```typescript
function constrainedSubsetSum(nums: number[], k: number): number {
    const n = nums.length;
    const dp = new Array<number>(n);
    const deque: number[] = [];
    let ans = -Infinity;

    for (let i = 0; i < n; ++i) {
        while (deque.length && i - deque[0] > k) {
            deque.shift();
        }
        const bestPrev = deque.length ? dp[deque[0]] : 0;
        dp[i] = nums[i] + Math.max(0, bestPrev);
        ans = Math.max(ans, dp[i]);

        while (deque.length && dp[deque[deque.length - 1]] <= dp[i]) {
            deque.pop();
        }
        if (dp[i] > 0) {
            deque.push(i);
        }
    }

    return ans;
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
    function constrainedSubsetSum($nums, $k) {
        $n = count($nums);
        if ($n == 0) return 0;

        $dp = array_fill(0, $n, 0);
        $deque = new SplDoublyLinkedList(); // stores indices, monotonic decreasing by dp value
        $ans = PHP_INT_MIN;

        for ($i = 0; $i < $n; $i++) {
            // Remove indices out of the window [i-k, i-1]
            while (!$deque->isEmpty()) {
                $frontIdx = $deque->bottom();
                if ($i - $frontIdx > $k) {
                    $deque->shift(); // pop from front
                } else {
                    break;
                }
            }

            $maxPrev = 0;
            if (!$deque->isEmpty()) {
                $maxPrev = $dp[$deque->bottom()];
            }

            $dp[$i] = $nums[$i] + $maxPrev; // maxPrev is >=0 because we only keep positive dp in deque
            if ($dp[$i] > $ans) {
                $ans = $dp[$i];
            }

            // Maintain decreasing order of dp values in deque
            while (!$deque->isEmpty()) {
                $backIdx = $deque->top();
                if ($dp[$backIdx] <= $dp[$i]) {
                    $deque->pop(); // remove smaller or equal value
                } else {
                    break;
                }
            }

            // Only keep positive dp values for future extensions
            if ($dp[$i] > 0) {
                $deque->push($i);
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func constrainedSubsetSum(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var dp = Array(repeating: 0, count: n)
        var deque = [Int]()
        var ans = Int.min

        for i in 0..<n {
            if let first = deque.first, i - first > k {
                deque.removeFirst()
            }
            let maxPrev = deque.isEmpty ? 0 : dp[deque.first!]
            dp[i] = nums[i] + max(0, maxPrev)
            ans = max(ans, dp[i])

            while let last = deque.last, dp[last] <= dp[i] {
                deque.removeLast()
            }
            if dp[i] > 0 {
                deque.append(i)
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun constrainedSubsetSum(nums: IntArray, k: Int): Int {
        val n = nums.size
        val dp = IntArray(n)
        var answer = nums[0]
        val deque = ArrayDeque<Int>()
        for (i in 0 until n) {
            if (i > 0) {
                while (!deque.isEmpty() && i - deque.first > k) {
                    deque.removeFirst()
                }
                val maxPrev = if (deque.isEmpty()) 0 else dp[deque.first]
                dp[i] = nums[i] + maxPrev
            } else {
                dp[i] = nums[i]
            }
            answer = kotlin.math.max(answer, dp[i])
            while (!deque.isEmpty() && dp[deque.last] <= dp[i]) {
                deque.removeLast()
            }
            if (dp[i] > 0) {
                deque.addLast(i)
            }
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int constrainedSubsetSum(List<int> nums, int k) {
    int n = nums.length;
    List<int> dp = List.filled(n, 0);
    List<int> deque = [];
    int front = 0;
    int ans = -(1 << 60); // sufficiently small

    for (int i = 0; i < n; i++) {
      while (deque.isNotEmpty && i - deque[front] > k) {
        front++;
      }

      int maxPrev = (deque.length > front) ? dp[deque[front]] : 0;
      if (maxPrev < 0) maxPrev = 0;

      dp[i] = nums[i] + maxPrev;

      while (deque.length > front && dp[deque.last] < dp[i]) {
        deque.removeLast();
      }

      if (dp[i] > 0) {
        deque.add(i);
      }

      if (dp[i] > ans) ans = dp[i];
    }

    return ans;
  }
}
```

## Golang

```go
func constrainedSubsetSum(nums []int, k int) int {
	n := len(nums)
	if n == 0 {
		return 0
	}
	dp := make([]int, n)
	ans := nums[0]
	deque := make([]int, 0)

	for i := 0; i < n; i++ {
		// Remove indices out of the window [i-k, i-1]
		if len(deque) > 0 && deque[0] < i-k {
			deque = deque[1:]
		}
		maxPrev := 0
		if len(deque) > 0 && dp[deque[0]] > 0 {
			maxPrev = dp[deque[0]]
		}
		dp[i] = nums[i] + maxPrev
		if dp[i] > ans {
			ans = dp[i]
		}
		// Maintain deque in decreasing order of dp values
		for len(deque) > 0 && dp[deque[len(deque)-1]] <= dp[i] {
			deque = deque[:len(deque)-1]
		}
		if dp[i] > 0 {
			deque = append(deque, i)
		}
	}
	return ans
}
```

## Ruby

```ruby
def constrained_subset_sum(nums, k)
  n = nums.length
  dp = Array.new(n, 0)

  queue = []   # stores indices, decreasing dp values
  head = 0     # logical front of the deque

  ans = -Float::INFINITY

  (0...n).each do |i|
    # Remove out-of-range indices from the front
    while head < queue.size && queue[head] < i - k
      head += 1
    end

    max_prev = if head >= queue.size
                 0
               else
                 dp[queue[head]]
               end
    max_prev = 0 if max_prev < 0

    dp[i] = nums[i] + max_prev
    ans = dp[i] if dp[i] > ans

    # Maintain decreasing order in deque (by dp value)
    while queue.size > head && dp[queue[-1]] <= dp[i]
      queue.pop
    end

    # Only keep positive dp values for future extensions
    queue << i if dp[i] > 0
  end

  ans.to_i
end
```

## Scala

```scala
object Solution {
  def constrainedSubsetSum(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    val dp = new Array[Long](n)
    val deque = new java.util.ArrayDeque[Int]()
    var ans: Long = Long.MinValue

    var i = 0
    while (i < n) {
      // Remove indices that are out of the window [i-k, i-1]
      while (!deque.isEmpty && i - deque.peekFirst > k) {
        deque.pollFirst()
      }

      val maxPrev = if (deque.isEmpty) 0L else dp(deque.peekFirst)
      dp(i) = nums(i).toLong + math.max(0L, maxPrev)

      if (dp(i) > ans) ans = dp(i)

      // Maintain decreasing order of dp values in deque
      while (!deque.isEmpty && dp(deque.peekLast) <= dp(i)) {
        deque.pollLast()
      }

      // Only keep positive dp values for future extensions
      if (dp(i) > 0) {
        deque.offerLast(i)
      }

      i += 1
    }

    ans.toInt
  }
}
```

## Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn constrained_subset_sum(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        let k_usize = k as usize;
        let mut dp: Vec<i64> = vec![0; n];
        let mut deque: VecDeque<usize> = VecDeque::new();
        let mut ans: i64 = i64::MIN;

        for i in 0..n {
            // Remove indices out of the window [i-k, i-1]
            while let Some(&front) = deque.front() {
                if i - front > k_usize {
                    deque.pop_front();
                } else {
                    break;
                }
            }

            let max_prev = if let Some(&front) = deque.front() {
                dp[front]
            } else {
                0
            };

            dp[i] = nums[i] as i64 + std::cmp::max(0, max_prev);
            ans = ans.max(dp[i]);

            // Maintain decreasing order in deque
            while let Some(&back) = deque.back() {
                if dp[back] <= dp[i] {
                    deque.pop_back();
                } else {
                    break;
                }
            }

            if dp[i] > 0 {
                deque.push_back(i);
            }
        }

        ans as i32
    }
}
```

## Racket

```racket
(define/contract (constrained-subset-sum nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length nums))
         (nums-vec (list->vector nums))
         (dp (make-vector n 0))
         (deque (make-vector n 0)) ; stores indices
         (head 0)
         (tail -1)
         (ans 0))
    ;; initialize first element
    (vector-set! dp 0 (vector-ref nums-vec 0))
    (set! ans (vector-ref dp 0))
    (when (> (vector-ref dp 0) 0)
      (set! tail (+ tail 1))
      (vector-set! deque tail 0))
    ;; process remaining elements
    (do ((i 1 (+ i 1)))
        ((= i n) ans)
      ;; discard indices out of the k‑window
      (let loop ()
        (when (and (<= head tail)
                   (> (- i (vector-ref deque head)) k))
          (set! head (+ head 1))
          (loop)))
      ;; compute dp[i]
      (let* ((maxPrev (if (< head (add1 tail))
                         (vector-ref dp (vector-ref deque head))
                         0))
             (usePrev (if (> maxPrev 0) maxPrev 0))
             (curr (+ (vector-ref nums-vec i) usePrev)))
        (vector-set! dp i curr)
        (when (> curr ans) (set! ans curr))
        ;; maintain monotonic decreasing deque
        (when (> curr 0)
          (let loop2 ()
            (when (and (<= head tail)
                       (< (vector-ref dp (vector-ref deque tail)) curr))
              (set! tail (- tail 1))
              (loop2)))
          (set! tail (+ tail 1))
          (vector-set! deque tail i)))))))
```

## Erlang

```erlang
-module(solution).
-export([constrained_subset_sum/2]).

-spec constrained_subset_sum(Nums :: [integer()], K :: integer()) -> integer().
constrained_subset_sum(Nums, K) ->
    loop(Nums, K, 0, -10000000000, queue:new()).

%% Loop over the list with current index I, current maximum answer MaxAns,
%% and a monotonic deque storing {Idx, Dp} in decreasing Dp order.
loop([], _K, _I, MaxAns, _Deque) ->
    MaxAns;
loop([V | Rest], K, I, MaxAns, Deque0) ->
    %% Remove elements out of the window from the front
    Deque1 = remove_out_of_range(Deque0, I, K),

    %% Best previous dp within window (0 if none)
    PrevDp =
        case queue:peek(Deque1) of
            empty -> 0;
            {{_, Dp}, _} -> Dp
        end,

    Cur = V + PrevDp,
    NewMaxAns = erlang:max(MaxAns, Cur),

    %% Maintain monotonic decreasing order by removing smaller dp from back
    Deque2 = clean_back(Deque1, Cur),

    %% Insert current dp if positive
    Deque3 =
        if Cur > 0 ->
                queue:in({I, Cur}, Deque2);
           true ->
                Deque2
        end,

    loop(Rest, K, I + 1, NewMaxAns, Deque3).

%% Remove elements whose index is farther than K from the current index.
remove_out_of_range(Deque, I, K) ->
    case queue:peek(Deque) of
        empty -> Deque;
        {{Idx, _}, _} when I - Idx > K ->
            {_, Q2} = queue:out(Deque),
            remove_out_of_range(Q2, I, K);
        _ -> Deque
    end.

%% Remove elements from the back while their dp is <= Cur.
clean_back(Deque, Cur) ->
    case queue:peek_r(Deque) of
        empty -> Deque;
        {{_, Dp}, _} when Dp =< Cur ->
            {_, Q2} = queue:out_r(Deque),
            clean_back(Q2, Cur);
        _ -> Deque
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec constrained_subset_sum(nums :: [integer], k :: integer) :: integer
  def constrained_subset_sum(nums, k) do
    {ans, _} =
      Enum.with_index(nums)
      |> Enum.reduce({-1_000_000_000, :gb_trees.empty()}, fn {num, i}, {cur_ans, tree} ->
        tree = clean_tree(tree, i, k)

        best =
          if :gb_trees.is_empty(tree) do
            0
          else
            {{max_dp, _idx}, _val} = :gb_trees.max(tree)
            if max_dp > 0, do: max_dp, else: 0
          end

        dp_i = num + best
        new_ans = if dp_i > cur_ans, do: dp_i, else: cur_ans
        tree2 = :gb_trees.insert({dp_i, i}, true, tree)
        {new_ans, tree2}
      end)

    ans
  end

  defp clean_tree(tree, i, k) do
    if :gb_trees.is_empty(tree) do
      tree
    else
      {{max_dp, idx}, _val} = :gb_trees.max(tree)
      if i - idx > k do
        clean_tree(:gb_trees.delete({max_dp, idx}, tree), i, k)
      else
        tree
      end
    end
  end
end
```
