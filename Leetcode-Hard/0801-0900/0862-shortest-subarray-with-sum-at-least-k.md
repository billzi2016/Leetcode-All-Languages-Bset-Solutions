# 0862. Shortest Subarray with Sum at Least K

## Cpp

```cpp
class Solution {
public:
    int shortestSubarray(std::vector<int>& nums, int k) {
        int n = nums.size();
        std::vector<long long> prefix(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            prefix[i + 1] = prefix[i] + nums[i];
        }
        const long long K = k;
        int ans = n + 1;
        std::deque<int> dq;
        for (int i = 0; i <= n; ++i) {
            while (!dq.empty() && prefix[i] - prefix[dq.front()] >= K) {
                ans = std::min(ans, i - dq.front());
                dq.pop_front();
            }
            while (!dq.empty() && prefix[i] <= prefix[dq.back()]) {
                dq.pop_back();
            }
            dq.push_back(i);
        }
        return (ans == n + 1) ? -1 : ans;
    }
};
```

## Java

```java
class Solution {
    public int shortestSubarray(int[] nums, int k) {
        int n = nums.length;
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + nums[i];
        }
        int ans = n + 1;
        java.util.ArrayDeque<Integer> deque = new java.util.ArrayDeque<>();
        for (int i = 0; i <= n; i++) {
            while (!deque.isEmpty() && prefix[i] - prefix[deque.peekFirst()] >= k) {
                ans = Math.min(ans, i - deque.pollFirst());
            }
            while (!deque.isEmpty() && prefix[i] <= prefix[deque.peekLast()]) {
                deque.pollLast();
            }
            deque.addLast(i);
        }
        return ans == n + 1 ? -1 : ans;
    }
}
```

## Python

```python
class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        from collections import deque
        dq = deque()
        ans = n + 1

        for i in range(n + 1):
            while dq and prefix[i] - prefix[dq[0]] >= k:
                ans = min(ans, i - dq.popleft())
            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()
            dq.append(i)

        return ans if ans <= n else -1
```

## Python3

```python
from collections import deque
from typing import List

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        dq = deque()
        ans = n + 1

        for i in range(n + 1):
            # Check if any subarray ending at i meets the requirement
            while dq and prefix[i] - prefix[dq[0]] >= k:
                ans = min(ans, i - dq.popleft())
            # Maintain increasing order of prefix sums in deque
            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()
            dq.append(i)

        return ans if ans <= n else -1
```

## C

```c
#include <stdlib.h>
#include <limits.h>

int shortestSubarray(int* nums, int numsSize, int k) {
    int n = numsSize;
    long long *pre = (long long *)malloc((n + 1) * sizeof(long long));
    if (!pre) return -1; // allocation failure safeguard
    pre[0] = 0;
    for (int i = 1; i <= n; ++i) {
        pre[i] = pre[i - 1] + (long long)nums[i - 1];
    }

    int *dq = (int *)malloc((n + 1) * sizeof(int));
    if (!dq) {
        free(pre);
        return -1;
    }
    int head = 0, tail = 0; // deque stores indices
    int ans = n + 1;

    for (int i = 0; i <= n; ++i) {
        while (head < tail && pre[i] - pre[dq[head]] >= (long long)k) {
            int len = i - dq[head];
            if (len < ans) ans = len;
            head++;
        }
        while (head < tail && pre[i] <= pre[dq[tail - 1]]) {
            tail--;
        }
        dq[tail++] = i;
    }

    free(pre);
    free(dq);

    return (ans == n + 1) ? -1 : ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int ShortestSubarray(int[] nums, int k)
    {
        int n = nums.Length;
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++)
            prefix[i + 1] = prefix[i] + nums[i];

        int[] deque = new int[n + 1];
        int head = 0, tail = 0;
        int best = n + 1;
        long target = k;

        for (int i = 0; i <= n; i++)
        {
            while (head < tail && prefix[i] - prefix[deque[head]] >= target)
            {
                best = Math.Min(best, i - deque[head]);
                head++;
            }

            while (head < tail && prefix[i] <= prefix[deque[tail - 1]])
            {
                tail--;
            }

            deque[tail++] = i;
        }

        return best == n + 1 ? -1 : best;
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
var shortestSubarray = function(nums, k) {
    const n = nums.length;
    const prefix = new Array(n + 1);
    prefix[0] = 0;
    for (let i = 0; i < n; i++) {
        prefix[i + 1] = prefix[i] + nums[i];
    }

    // deque implemented with a plain array and two pointers
    const dq = new Array(n + 1);
    let head = 0, tail = 0;
    let ans = Infinity;

    for (let i = 0; i <= n; i++) {
        // Try to find valid subarrays ending at i
        while (head < tail && prefix[i] - prefix[dq[head]] >= k) {
            ans = Math.min(ans, i - dq[head]);
            head++;
        }
        // Maintain increasing order of prefix sums in deque
        while (head < tail && prefix[i] <= prefix[dq[tail - 1]]) {
            tail--;
        }
        dq[tail++] = i;
    }

    return ans === Infinity ? -1 : ans;
};
```

## Typescript

```typescript
function shortestSubarray(nums: number[], k: number): number {
    const n = nums.length;
    const prefix = new Array<number>(n + 1);
    prefix[0] = 0;
    for (let i = 0; i < n; i++) {
        prefix[i + 1] = prefix[i] + nums[i];
    }

    const dq = new Array<number>(n + 1);
    let head = 0, tail = 0;
    let ans = Number.MAX_SAFE_INTEGER;

    for (let i = 0; i <= n; i++) {
        while (head < tail && prefix[i] - prefix[dq[head]] >= k) {
            ans = Math.min(ans, i - dq[head]);
            head++;
        }
        while (head < tail && prefix[i] <= prefix[dq[tail - 1]]) {
            tail--;
        }
        dq[tail++] = i;
    }

    return ans === Number.MAX_SAFE_INTEGER ? -1 : ans;
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
    function shortestSubarray($nums, $k) {
        $n = count($nums);
        $prefix = array_fill(0, $n + 1, 0);
        for ($i = 1; $i <= $n; $i++) {
            $prefix[$i] = $prefix[$i - 1] + $nums[$i - 1];
        }

        $deque = new SplDoublyLinkedList();
        $deque->setIteratorMode(SplDoublyLinkedList::IT_MODE_FIFO);
        $ans = $n + 1;
        $deque->push(0);

        for ($i = 1; $i <= $n; $i++) {
            while (!$deque->isEmpty() && $prefix[$i] - $prefix[$deque->bottom()] >= $k) {
                $len = $i - $deque->bottom();
                if ($len < $ans) {
                    $ans = $len;
                }
                $deque->shift(); // remove from front
            }

            while (!$deque->isEmpty() && $prefix[$i] <= $prefix[$deque->top()]) {
                $deque->pop(); // remove from back
            }

            $deque->push($i);
        }

        return $ans == $n + 1 ? -1 : $ans;
    }
}
```

## Swift

```swift
class Solution {
    func shortestSubarray(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var prefix = [Int64](repeating: 0, count: n + 1)
        for i in 0..<n {
            prefix[i + 1] = prefix[i] + Int64(nums[i])
        }
        var deque = [Int]()
        var front = 0
        let target = Int64(k)
        var ans = n + 1
        
        for i in 0...n {
            while front < deque.count && prefix[i] - prefix[deque[front]] >= target {
                ans = min(ans, i - deque[front])
                front += 1
            }
            while deque.count > front && prefix[i] <= prefix[deque.last!] {
                deque.removeLast()
            }
            deque.append(i)
        }
        return ans == n + 1 ? -1 : ans
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque
import kotlin.math.min

class Solution {
    fun shortestSubarray(nums: IntArray, k: Int): Int {
        val n = nums.size
        val prefix = LongArray(n + 1)
        for (i in 0 until n) {
            prefix[i + 1] = prefix[i] + nums[i].toLong()
        }
        val deque: ArrayDeque<Int> = ArrayDeque()
        var ans = Int.MAX_VALUE
        val target = k.toLong()
        for (i in 0..n) {
            while (!deque.isEmpty() && prefix[i] - prefix[deque.peekFirst()] >= target) {
                ans = min(ans, i - deque.pollFirst())
            }
            while (!deque.isEmpty() && prefix[i] <= prefix[deque.peekLast()]) {
                deque.pollLast()
            }
            deque.addLast(i)
        }
        return if (ans == Int.MAX_VALUE) -1 else ans
    }
}
```

## Dart

```dart
class Solution {
  int shortestSubarray(List<int> nums, int k) {
    int n = nums.length;
    List<int> prefix = List.filled(n + 1, 0);
    for (int i = 0; i < n; ++i) {
      prefix[i + 1] = prefix[i] + nums[i];
    }

    List<int> deque = [];
    int head = 0;
    int ans = n + 1;

    for (int i = 0; i <= n; ++i) {
      // Check if any subarray ending at i satisfies the condition
      while (deque.length > head && prefix[i] - prefix[deque[head]] >= k) {
        ans = ans < (i - deque[head]) ? ans : (i - deque[head]);
        head++;
      }

      // Maintain monotonic increasing order of prefix sums in deque
      while (deque.length > head && prefix[i] <= prefix[deque.last]) {
        deque.removeLast();
      }

      deque.add(i);
    }

    return ans == n + 1 ? -1 : ans;
  }
}
```

## Golang

```go
func shortestSubarray(nums []int, k int) int {
	n := len(nums)
	prefix := make([]int64, n+1)
	for i := 0; i < n; i++ {
		prefix[i+1] = prefix[i] + int64(nums[i])
	}

	deq := make([]int, n+1)
	l, r := 0, 0
	ans := n + 1
	target := int64(k)

	for i := 0; i <= n; i++ {
		// Check if any subarray ending at i meets the requirement
		for l < r && prefix[i]-prefix[deq[l]] >= target {
			if length := i - deq[l]; length < ans {
				ans = length
			}
			l++
		}
		// Maintain monotonicity of prefix sums in deque
		for l < r && prefix[i] <= prefix[deq[r-1]] {
			r--
		}
		deq[r] = i
		r++
	}

	if ans == n+1 {
		return -1
	}
	return ans
}
```

## Ruby

```ruby
def shortest_subarray(nums, k)
  n = nums.length
  prefix = Array.new(n + 1, 0)
  (0...n).each do |i|
    prefix[i + 1] = prefix[i] + nums[i]
  end

  deque = []
  head = 0
  ans = n + 1

  (0..n).each do |i|
    while head < deque.length && prefix[i] - prefix[deque[head]] >= k
      length = i - deque[head]
      ans = length if length < ans
      head += 1
    end

    while deque.length > head && prefix[i] <= prefix[deque[-1]]
      deque.pop
    end

    deque << i
  end

  ans == n + 1 ? -1 : ans
end
```

## Scala

```scala
object Solution {
  import java.util.ArrayDeque

  def shortestSubarray(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    val pre = new Array[Long](n + 1)
    var i = 0
    while (i < n) {
      pre(i + 1) = pre(i) + nums(i).toLong
      i += 1
    }

    val deque = new ArrayDeque[Int]()
    var ans = Int.MaxValue
    var idx = 0
    while (idx <= n) {
      while (!deque.isEmpty && pre(idx) - pre(deque.peekFirst()) >= k.toLong) {
        val length = idx - deque.pollFirst()
        if (length < ans) ans = length
      }
      while (!deque.isEmpty && pre(idx) <= pre(deque.peekLast())) {
        deque.pollLast()
      }
      deque.addLast(idx)
      idx += 1
    }

    if (ans == Int.MaxValue) -1 else ans
  }
}
```

## Rust

```rust
use std::collections::VecDeque;

pub struct Solution;

impl Solution {
    pub fn shortest_subarray(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let mut prefix = vec![0i64; n + 1];
        for i in 0..n {
            prefix[i + 1] = prefix[i] + nums[i] as i64;
        }
        let mut deque: VecDeque<usize> = VecDeque::new();
        let mut ans = n + 1;
        let target = k as i64;

        for i in 0..=n {
            while let Some(&front) = deque.front() {
                if prefix[i] - prefix[front] >= target {
                    ans = ans.min(i - front);
                    deque.pop_front();
                } else {
                    break;
                }
            }
            while let Some(&back) = deque.back() {
                if prefix[i] <= prefix[back] {
                    deque.pop_back();
                } else {
                    break;
                }
            }
            deque.push_back(i);
        }

        if ans == n + 1 { -1 } else { ans as i32 }
    }
}
```

## Racket

```racket
(define/contract (shortest-subarray nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length nums))
         (pref (make-vector (+ n 1) 0)))
    ;; compute prefix sums
    (let loop ((i 0) (acc 0) (lst nums))
      (if (null? lst)
          (void)
          (begin
            (set! acc (+ acc (car lst)))
            (vector-set! pref (+ i 1) acc)
            (loop (+ i 1) acc (cdr lst)))))
    (let ((deque (make-vector (+ n 1) -1))
          (head 0)
          (tail 0)
          (ans (+ n 1))) ; sentinel larger than any possible answer
      (define (push-back idx)
        (vector-set! deque tail idx)
        (set! tail (+ tail 1)))
      (define (pop-front)
        (set! head (+ head 1)))
      (define (front) (vector-ref deque head))
      (define (back) (vector-ref deque (- tail 1)))
      (define (pop-back)
        (set! tail (- tail 1)))
      (for ([i (in-range (+ n 1))])
        (let ((cur (vector-ref pref i)))
          ;; Try to find valid subarrays ending at i
          (let loop1 ()
            (when (and (< head tail)
                       (>= (- cur (vector-ref pref (front))) k))
              (set! ans (min ans (- i (front))))
              (pop-front)
              (loop1)))
          ;; Maintain increasing order of prefix sums in deque
          (let loop2 ()
            (when (and (< head tail)
                       (<= cur (vector-ref pref (back))))
              (pop-back)
              (loop2)))
          (push-back i)))
      (if (= ans (+ n 1)) -1 ans))))
```

## Erlang

```erlang
-spec shortest_subarray(Nums :: [integer()], K :: integer()) -> integer().
shortest_subarray(Nums, K) ->
    N = length(Nums),
    MaxAns = N + 1,
    Deque0 = queue:new(),
    Deque1 = queue:in({0, 0}, Deque0),          % (index, prefix sum)
    Ans = proc(Nums, 1, 0, MaxAns, Deque1, K),
    if
        Ans =< N -> Ans;
        true     -> -1
    end.

proc([], _Idx, _Sum, Ans, _Deque, _K) ->
    Ans;
proc([H|T], Idx, CumSum, Ans, Deque, K) ->
    NewSum = CumSum + H,
    {DequeF, AnsF} = pop_front(Idx, NewSum, Deque, K, Ans),
    DequeB = pop_back(Idx, NewSum, DequeF),
    DequeNew = queue:in({Idx, NewSum}, DequeB),
    proc(T, Idx + 1, NewSum, AnsF, DequeNew, K).

pop_front(_Idx, _Sum, Deque, _K, Ans) when Deque == queue:new() ->
    {Deque, Ans};
pop_front(Idx, Sum, Deque, K, Ans) ->
    case queue:peek(Deque) of
        empty ->
            {Deque, Ans};
        {value, {FIdx, FSum}} ->
            if
                Sum - FSum >= K ->
                    {{value, _}, Deq1} = queue:out(Deque),
                    NewAns = erlang:min(Ans, Idx - FIdx),
                    pop_front(Idx, Sum, Deq1, K, NewAns);
                true ->
                    {Deque, Ans}
            end
    end.

pop_back(_Idx, _Sum, Deque) when Deque == queue:new() ->
    Deque;
pop_back(Idx, Sum, Deque) ->
    case queue:peek_r(Deque) of
        empty ->
            Deque;
        {value, {_BIdx, BSum}} ->
            if
                Sum =< BSum ->
                    {{value, _}, Deq1} = queue:out_r(Deque),
                    pop_back(Idx, Sum, Deq1);
                true ->
                    Deque
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec shortest_subarray(nums :: [integer], k :: integer) :: integer
  def shortest_subarray(nums, k) do
    n = length(nums)
    init_queue = :queue.in({0, -1}, :queue.new())

    {_, best, _} =
      Enum.reduce(Enum.with_index(nums), {init_queue, n + 1, 0},
        fn {num, i}, {q, best, sum} ->
          sum = sum + num

          {q, best} = pop_front(q, sum, k, i, best)
          q = pop_back(q, sum)

          q = :queue.in({sum, i}, q)
          {q, best, sum}
        end)

    if best <= n, do: best, else: -1
  end

  defp pop_front(q, sum, k, i, best) do
    case :queue.peek(q) do
      {:value, {pref, idx}} when sum - pref >= k ->
        new_best = Kernel.min(best, i - idx)
        {{:value, _elem}, q2} = :queue.out(q)
        pop_front(q2, sum, k, i, new_best)

      _ ->
        {q, best}
    end
  end

  defp pop_back(q, sum) do
    case :queue.peek_r(q) do
      {:value, {pref, _idx}} when sum <= pref ->
        {{:value, _elem}, q2} = :queue.out_r(q)
        pop_back(q2, sum)

      _ ->
        q
    end
  end
end
```
