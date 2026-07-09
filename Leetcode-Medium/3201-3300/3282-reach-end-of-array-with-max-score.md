# 3282. Reach End of Array With Max Score

## Cpp

```cpp
class Solution {
public:
    long long findMaximumScore(std::vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return 0LL;
        std::vector<int> nge(n);
        std::stack<int> st;
        for (int i = 0; i < n; ++i) {
            while (!st.empty() && nums[i] > nums[st.top()]) {
                nge[st.top()] = i;
                st.pop();
            }
            st.push(i);
        }
        while (!st.empty()) {
            nge[st.top()] = n - 1;
            st.pop();
        }
        long long ans = 0;
        int cur = 0;
        while (cur < n - 1) {
            int nxt = nge[cur];
            ans += static_cast<long long>(nxt - cur) * nums[cur];
            cur = nxt;
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public long findMaximumScore(List<Integer> nums) {
        int n = nums.size();
        if (n <= 1) return 0L;
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = nums.get(i);
        int[] nge = new int[n];
        int[] stack = new int[n];
        int top = -1;
        for (int i = n - 1; i >= 0; --i) {
            while (top >= 0 && a[stack[top]] <= a[i]) top--;
            nge[i] = (top >= 0) ? stack[top] : -1;
            stack[++top] = i;
        }
        long ans = 0L;
        int i = 0;
        while (i < n - 1) {
            int j = nge[i];
            if (j == -1) {
                ans += (long) (n - 1 - i) * a[i];
                break;
            } else {
                ans += (long) (j - i) * a[i];
                i = j;
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def findMaximumScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return 0

        # nearest greater element to the right for each index
        nge = [-1] * n
        stack = []  # monotonic decreasing stack of indices

        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            if stack:
                nge[i] = stack[-1]
            stack.append(i)

        total = 0
        i = 0
        while i < n - 1:
            j = nge[i] if nge[i] != -1 else n - 1
            total += (j - i) * nums[i]
            i = j

        return total
```

## Python3

```python
from typing import List

class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        nxt = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            nxt[i] = stack[-1] if stack else n - 1
            stack.append(i)
        ans = 0
        i = 0
        while i < n - 1:
            j = nxt[i]
            ans += (j - i) * nums[i]
            i = j
        return ans
```

## C

```c
#include <stdlib.h>

long long findMaximumScore(int* nums, int numsSize) {
    if (numsSize <= 1) return 0LL;

    int *next = (int *)malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; ++i) next[i] = -1;

    int *stack = (int *)malloc(numsSize * sizeof(int));
    int top = -1;
    for (int i = 0; i < numsSize; ++i) {
        while (top >= 0 && nums[i] > nums[stack[top]]) {
            next[stack[top]] = i;
            --top;
        }
        stack[++top] = i;
    }
    free(stack);

    long long ans = 0;
    int idx = 0;
    while (idx < numsSize - 1) {
        int j = (next[idx] == -1) ? (numsSize - 1) : next[idx];
        ans += (long long)(j - idx) * nums[idx];
        idx = j;
    }

    free(next);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public long FindMaximumScore(IList<int> nums) {
        int n = nums.Count;
        int[] nextGreater = new int[n];
        for (int i = 0; i < n; i++) nextGreater[i] = n - 1;

        var stack = new System.Collections.Generic.Stack<int>();
        for (int i = 0; i < n; i++) {
            while (stack.Count > 0 && nums[i] > nums[stack.Peek()]) {
                int idx = stack.Pop();
                nextGreater[idx] = i;
            }
            stack.Push(i);
        }

        long total = 0;
        int cur = 0;
        while (cur < n - 1) {
            int nxt = nextGreater[cur];
            total += ((long)(nxt - cur)) * nums[cur];
            cur = nxt;
        }
        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaximumScore = function(nums) {
    const n = nums.length;
    if (n <= 1) return 0;
    const next = new Array(n).fill(-1);
    const stack = [];
    for (let i = 0; i < n; i++) {
        while (stack.length && nums[i] > nums[stack[stack.length - 1]]) {
            const idx = stack.pop();
            next[idx] = i;
        }
        stack.push(i);
    }
    let ans = 0;
    let i = 0;
    while (i < n - 1) {
        const j = next[i] !== -1 ? next[i] : n - 1;
        ans += (j - i) * nums[i];
        i = j;
    }
    return ans;
};
```

## Typescript

```typescript
function findMaximumScore(nums: number[]): number {
    const n = nums.length;
    if (n <= 1) return 0;

    const nextGreater = new Array<number>(n).fill(-1);
    const stack: number[] = [];

    for (let i = n - 1; i >= 0; --i) {
        while (stack.length && nums[stack[stack.length - 1]] <= nums[i]) {
            stack.pop();
        }
        if (stack.length) nextGreater[i] = stack[stack.length - 1];
        stack.push(i);
    }

    let score = 0;
    let i = 0;
    while (i < n - 1) {
        const j = nextGreater[i];
        if (j !== -1) {
            score += (j - i) * nums[i];
            i = j;
        } else {
            score += (n - 1 - i) * nums[i];
            break;
        }
    }

    return score;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findMaximumScore($nums) {
        $n = count($nums);
        if ($n <= 1) {
            return 0;
        }
        $next = array_fill(0, $n, -1);
        $stack = [];

        for ($i = 0; $i < $n; $i++) {
            while (!empty($stack) && $nums[$i] > $nums[$stack[count($stack) - 1]]) {
                $idx = array_pop($stack);
                $next[$idx] = $i;
            }
            $stack[] = $i;
        }

        $score = 0;
        $i = 0;
        while ($i < $n - 1) {
            $j = $next[$i];
            if ($j == -1) {
                $j = $n - 1;
            }
            $score += ($j - $i) * $nums[$i];
            $i = $j;
        }

        return $score;
    }
}
```

## Swift

```swift
class Solution {
    func findMaximumScore(_ nums: [Int]) -> Int {
        let n = nums.count
        if n <= 1 { return 0 }
        var nextGreater = Array(repeating: -1, count: n)
        var stack = [Int]() // indices with decreasing values
        
        for i in stride(from: n - 1, through: 0, by: -1) {
            while let last = stack.last, nums[last] <= nums[i] {
                stack.removeLast()
            }
            if let last = stack.last {
                nextGreater[i] = last
            } else {
                nextGreater[i] = -1
            }
            stack.append(i)
        }
        
        var cur = 0
        var ans = 0
        while cur < n - 1 {
            let nxt = nextGreater[cur]
            if nxt != -1 {
                ans += (nxt - cur) * nums[cur]
                cur = nxt
            } else {
                ans += (n - 1 - cur) * nums[cur]
                break
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findMaximumScore(nums: List<Int>): Long {
        val n = nums.size
        if (n <= 1) return 0L
        val next = IntArray(n) { n - 1 }
        val stack = java.util.ArrayDeque<Int>()
        for (i in 0 until n) {
            while (!stack.isEmpty() && nums[i] > nums[stack.peek()]) {
                val idx = stack.pop()
                next[idx] = i
            }
            stack.push(i)
        }
        var ans = 0L
        var i = 0
        while (i < n - 1) {
            val j = next[i]
            ans += ((j - i).toLong()) * nums[i].toLong()
            i = j
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int findMaximumScore(List<int> nums) {
    int n = nums.length;
    List<int> nge = List.filled(n, n - 1);
    List<int> stack = [];

    for (int i = n - 1; i >= 0; i--) {
      while (stack.isNotEmpty && nums[stack.last] <= nums[i]) {
        stack.removeLast();
      }
      if (stack.isNotEmpty) {
        nge[i] = stack.last;
      } else {
        nge[i] = n - 1;
      }
      stack.add(i);
    }

    int cur = 0;
    int ans = 0;
    while (cur < n - 1) {
      int nxt = nge[cur];
      ans += (nxt - cur) * nums[cur];
      cur = nxt;
    }
    return ans;
  }
}
```

## Golang

```go
func findMaximumScore(nums []int) int64 {
    n := len(nums)
    if n <= 1 {
        return 0
    }
    next := make([]int, n)
    for i := range next {
        next[i] = -1
    }
    stack := make([]int, 0)
    for i := n - 1; i >= 0; i-- {
        for len(stack) > 0 && nums[stack[len(stack)-1]] <= nums[i] {
            stack = stack[:len(stack)-1]
        }
        if len(stack) > 0 {
            next[i] = stack[len(stack)-1]
        }
        stack = append(stack, i)
    }

    var total int64
    i := 0
    for i < n-1 {
        if next[i] == -1 {
            total += int64(n-1-i) * int64(nums[i])
            break
        }
        j := next[i]
        total += int64(j-i) * int64(nums[i])
        i = j
    }
    return total
}
```

## Ruby

```ruby
def find_maximum_score(nums)
  n = nums.length
  next_greater = Array.new(n, -1)
  stack = []

  (n - 1).downto(0) do |i|
    while !stack.empty? && nums[stack[-1]] <= nums[i]
      stack.pop
    end
    next_greater[i] = stack.empty? ? -1 : stack[-1]
    stack << i
  end

  dp = Array.new(n, 0)
  (n - 1).downto(0) do |i|
    if next_greater[i] == -1
      dp[i] = (n - 1 - i) * nums[i]
    else
      dp[i] = (next_greater[i] - i) * nums[i] + dp[next_greater[i]]
    end
  end

  dp[0]
end
```

## Scala

```scala
object Solution {
  def findMaximumScore(nums: List[Int]): Long = {
    val n = nums.length
    if (n <= 1) return 0L
    val arr = nums.toArray
    val nextGreater = Array.fill[Int](n)(-1)
    val stack = new java.util.ArrayDeque[Int]()

    var i = 0
    while (i < n) {
      while (!stack.isEmpty && arr(i) > arr(stack.peek())) {
        val idx = stack.pop()
        nextGreater(idx) = i
      }
      stack.push(i)
      i += 1
    }

    val dp = Array.fill[Long](n)(0L)
    var idx = n - 2
    while (idx >= 0) {
      val ng = nextGreater(idx)
      if (ng == -1) {
        dp(idx) = (n - 1 - idx).toLong * arr(idx).toLong
      } else {
        dp(idx) = (ng - idx).toLong * arr(idx).toLong + dp(ng)
      }
      idx -= 1
    }

    dp(0)
  }
}
```

## Rust

```rust
impl Solution {
    pub fn find_maximum_score(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        if n <= 1 {
            return 0;
        }
        // nxt[i] = nearest index j > i with nums[j] > nums[i]; if none, n-1
        let mut nxt = vec![n - 1; n];
        let mut stack: Vec<usize> = Vec::new(); // monotonic decreasing values

        for i in (0..n).rev() {
            while let Some(&top) = stack.last() {
                if nums[top] <= nums[i] {
                    stack.pop();
                } else {
                    break;
                }
            }
            if let Some(&top) = stack.last() {
                nxt[i] = top;
            } else {
                nxt[i] = n - 1;
            }
            stack.push(i);
        }

        let mut idx = 0usize;
        let mut total: i64 = 0;
        while idx < n - 1 {
            let next = nxt[idx];
            total += ((next - idx) as i64) * (nums[idx] as i64);
            if next == idx {
                break; // safety, should not happen
            }
            idx = next;
        }
        total
    }
}
```

## Racket

```racket
(define/contract (find-maximum-score nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (arr (list->vector nums))
         (next (make-vector n -1))
         (stack '()))
    ;; compute next greater element for each index
    (for ([i (in-range n)])
      (let ((val (vector-ref arr i)))
        (let loop ()
          (when (and (not (null? stack))
                     (> val (vector-ref arr (car stack))))
            (let ((idx (car stack)))
              (vector-set! next idx i)
              (set! stack (cdr stack))
              (loop)))))
      (set! stack (cons i stack))) ; push current index onto stack
    ;; dynamic programming from the end backwards
    (let ((dp (make-vector n 0)))
      (for ([i (in-range (- n 2) -1 -1)])   ; i = n-2 .. 0
        (let* ((j (vector-ref next i))
               (dest (if (= j -1) (- n 1) j))
               (score (+ (* (- dest i) (vector-ref arr i))
                         (vector-ref dp dest))))
          (vector-set! dp i score)))
      (vector-ref dp 0))))
```

## Erlang

```erlang
-spec find_maximum_score(Nums :: [integer()]) -> integer().
find_maximum_score(Nums) ->
    N = length(Nums),
    NumT = list_to_tuple(Nums),
    {DPMap, _} =
        lists:foldl(
            fun(I, {Map, Stack}) ->
                Val = element(I, NumT),
                NewStack = pop_le(Stack, Val, NumT),
                Score =
                    case NewStack of
                        [] -> (N - I) * Val;
                        [J|_] -> (J - I) * Val + maps:get(J, Map)
                    end,
                {maps:put(I, Score, Map), [I | NewStack]}
            end,
            {maps:new(), []},
            lists:seq(N, 1, -1)),
    maps:get(1, DPMap).

pop_le([], _Val, _NumT) -> [];
pop_le([Idx|Rest] = Stack, Val, NumT) ->
    case element(Idx, NumT) =< Val of
        true -> pop_le(Rest, Val, NumT);
        false -> Stack
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_maximum_score(nums :: [integer]) :: integer
  def find_maximum_score(nums) do
    n = length(nums)

    if n <= 1 do
      0
    else
      vals_arr = :array.from_list(nums)
      default_nge = n - 1
      nge_arr = :array.new(n, default: default_nge)

      {final_nge, _stack} =
        Enum.reduce(Enum.with_index(nums), {nge_arr, []}, fn {val, idx},
                                                            {nge_acc, stack} ->
          {new_stack, new_nge} = pop_greater(stack, val, idx, nge_acc)
          {new_nge, [{idx, val} | new_stack]}
        end)

      compute_total(0, n, final_nge, vals_arr, 0)
    end
  end

  defp pop_greater([], _cur_val, _cur_idx, nge), do: {[], nge}

  defp pop_greater([{top_idx, top_val} | rest], cur_val, cur_idx, nge) when cur_val > top_val do
    new_nge = :array.set(top_idx, cur_idx, nge)
    pop_greater(rest, cur_val, cur_idx, new_nge)
  end

  defp pop_greater(stack, _cur_val, _cur_idx, nge), do: {stack, nge}

  defp compute_total(i, n, _nge_arr, _vals_arr, acc) when i >= n - 1, do: acc

  defp compute_total(i, n, nge_arr, vals_arr, acc) do
    j = :array.get(i, nge_arr)
    val_i = :array.get(i, vals_arr)
    compute_total(j, n, nge_arr, vals_arr, acc + (j - i) * val_i)
  end
end
```
