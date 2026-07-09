# 2104. Sum of Subarray Ranges

## Cpp

```cpp
class Solution {
public:
    long long subArrayRanges(vector<int>& nums) {
        int n = nums.size();
        auto calc = [&](bool isMin) -> long long {
            long long total = 0;
            vector<int> st;
            for (int i = 0; i <= n; ++i) {
                while (!st.empty() && (i == n ||
                       (isMin ? nums[st.back()] > nums[i] : nums[st.back()] < nums[i]))) {
                    int mid = st.back();
                    st.pop_back();
                    int left = st.empty() ? -1 : st.back();
                    long long right = i;
                    long long cnt = 1LL * (mid - left) * (right - mid);
                    total += cnt * (long long)nums[mid];
                }
                if (i < n) st.push_back(i);
            }
            return total;
        };
        long long sumMax = calc(false);
        long long sumMin = calc(true);
        return sumMax - sumMin;
    }
};
```

## Java

```java
class Solution {
    public long subArrayRanges(int[] nums) {
        int n = nums.length;
        long sumMin = 0L;
        long sumMax = 0L;
        java.util.Deque<Integer> stack = new java.util.ArrayDeque<>();

        // Sum of minimums
        for (int i = 0; i <= n; i++) {
            while (!stack.isEmpty() && (i == n || nums[stack.peekLast()] >= nums[i])) {
                int mid = stack.removeLast();
                int left = stack.isEmpty() ? -1 : stack.peekLast();
                int right = i;
                long cnt = (long) (mid - left) * (right - mid);
                sumMin += cnt * nums[mid];
            }
            if (i < n) {
                stack.addLast(i);
            }
        }

        // Sum of maximums
        stack.clear();
        for (int i = 0; i <= n; i++) {
            while (!stack.isEmpty() && (i == n || nums[stack.peekLast()] <= nums[i])) {
                int mid = stack.removeLast();
                int left = stack.isEmpty() ? -1 : stack.peekLast();
                int right = i;
                long cnt = (long) (mid - left) * (right - mid);
                sumMax += cnt * nums[mid];
            }
            if (i < n) {
                stack.addLast(i);
            }
        }

        return sumMax - sumMin;
    }
}
```

## Python

```python
class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        # Sum of minimums
        sum_min = 0
        stack = []
        for i in range(n + 1):
            cur = nums[i] if i < n else -float('inf')
            while stack and (i == n or cur <= nums[stack[-1]]):
                mid = stack.pop()
                left = stack[-1] if stack else -1
                right = i
                sum_min += nums[mid] * (mid - left) * (right - mid)

        # Sum of maximums
        sum_max = 0
        stack = []
        for i in range(n + 1):
            cur = nums[i] if i < n else float('inf')
            while stack and (i == n or cur >= nums[stack[-1]]):
                mid = stack.pop()
                left = stack[-1] if stack else -1
                right = i
                sum_max += nums[mid] * (mid - left) * (right - mid)

        return sum_max - sum_min
```

## Python3

```python
class Solution:
    def subArrayRanges(self, nums):
        n = len(nums)
        total_max = 0
        stack = []
        for i in range(n + 1):
            cur = float('inf') if i == n else nums[i]
            while stack and (i == n or nums[stack[-1]] < cur):
                mid = stack.pop()
                left = stack[-1] if stack else -1
                right = i
                total_max += nums[mid] * (mid - left) * (right - mid)
            stack.append(i)

        total_min = 0
        stack.clear()
        for i in range(n + 1):
            cur = -float('inf') if i == n else nums[i]
            while stack and (i == n or nums[stack[-1]] > cur):
                mid = stack.pop()
                left = stack[-1] if stack else -1
                right = i
                total_min += nums[mid] * (mid - left) * (right - mid)
            stack.append(i)

        return total_max - total_min
```

## C

```c
#include <stdlib.h>

long long subArrayRanges(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    int *stack = (int*)malloc(numsSize * sizeof(int));
    int top = -1;
    long long sumMin = 0, sumMax = 0;

    // Contribution as minimum
    for (int i = 0; i <= numsSize; ++i) {
        while (top >= 0 && (i == numsSize || nums[stack[top]] > nums[i])) {
            int mid = stack[top--];
            int left = (top >= 0) ? stack[top] : -1;
            long long right = i;
            sumMin += (long long)nums[mid] * (mid - left) * (right - mid);
        }
        if (i < numsSize) {
            stack[++top] = i;
        }
    }

    // Contribution as maximum
    top = -1;
    for (int i = 0; i <= numsSize; ++i) {
        while (top >= 0 && (i == numsSize || nums[stack[top]] < nums[i])) {
            int mid = stack[top--];
            int left = (top >= 0) ? stack[top] : -1;
            long long right = i;
            sumMax += (long long)nums[mid] * (mid - left) * (right - mid);
        }
        if (i < numsSize) {
            stack[++top] = i;
        }
    }

    free(stack);
    return sumMax - sumMin;
}
```

## Csharp

```csharp
public class Solution {
    public long SubArrayRanges(int[] nums) {
        int n = nums.Length;
        long sumMax = 0, sumMin = 0;
        var stack = new System.Collections.Generic.Stack<int>();

        // Contributions as maximum
        for (int i = 0; i <= n; i++) {
            while (stack.Count > 0 && (i == n || nums[i] >= nums[stack.Peek()])) {
                int mid = stack.Pop();
                int left = stack.Count == 0 ? -1 : stack.Peek();
                long cntLeft = mid - left;
                long cntRight = i - mid;
                sumMax += cntLeft * cntRight * (long)nums[mid];
            }
            if (i < n) stack.Push(i);
        }

        // Contributions as minimum
        stack.Clear();
        for (int i = 0; i <= n; i++) {
            while (stack.Count > 0 && (i == n || nums[i] <= nums[stack.Peek()])) {
                int mid = stack.Pop();
                int left = stack.Count == 0 ? -1 : stack.Peek();
                long cntLeft = mid - left;
                long cntRight = i - mid;
                sumMin += cntLeft * cntRight * (long)nums[mid];
            }
            if (i < n) stack.Push(i);
        }

        return sumMax - sumMin;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var subArrayRanges = function(nums) {
    const n = nums.length;
    let sumMax = 0, sumMin = 0;

    // Contribution as maximum
    let stack = [];
    for (let i = 0; i <= n; i++) {
        while (stack.length && (i === n || nums[stack[stack.length - 1]] <= nums[i])) {
            const mid = stack.pop();
            const left = stack.length ? stack[stack.length - 1] : -1;
            const right = i;
            sumMax += nums[mid] * (mid - left) * (right - mid);
        }
        if (i < n) stack.push(i);
    }

    // Contribution as minimum
    stack = [];
    for (let i = 0; i <= n; i++) {
        while (stack.length && (i === n || nums[stack[stack.length - 1]] >= nums[i])) {
            const mid = stack.pop();
            const left = stack.length ? stack[stack.length - 1] : -1;
            const right = i;
            sumMin += nums[mid] * (mid - left) * (right - mid);
        }
        if (i < n) stack.push(i);
    }

    return sumMax - sumMin;
};
```

## Typescript

```typescript
function subArrayRanges(nums: number[]): number {
    const n = nums.length;
    let sumMin = 0;
    let sumMax = 0;

    // contribution as minimums
    const stackMin: number[] = [];
    for (let i = 0; i <= n; i++) {
        while (
            stackMin.length &&
            (i === n || nums[stackMin[stackMin.length - 1]] >= (i < n ? nums[i] : undefined))
        ) {
            const mid = stackMin.pop() as number;
            const left = stackMin.length ? stackMin[stackMin.length - 1] : -1;
            const right = i;
            sumMin += nums[mid] * (mid - left) * (right - mid);
        }
        if (i < n) stackMin.push(i);
    }

    // contribution as maximums
    const stackMax: number[] = [];
    for (let i = 0; i <= n; i++) {
        while (
            stackMax.length &&
            (i === n || nums[stackMax[stackMax.length - 1]] <= (i < n ? nums[i] : undefined))
        ) {
            const mid = stackMax.pop() as number;
            const left = stackMax.length ? stackMax[stackMax.length - 1] : -1;
            const right = i;
            sumMax += nums[mid] * (mid - left) * (right - mid);
        }
        if (i < n) stackMax.push(i);
    }

    return sumMax - sumMin;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function subArrayRanges($nums) {
        $n = count($nums);
        // Sum of maximums
        $stack = [];
        $sumMax = 0;
        for ($i = 0; $i <= $n; $i++) {
            while (!empty($stack) && ($i == $n || $nums[end($stack)] <= $nums[$i])) {
                $mid = array_pop($stack);
                $left = empty($stack) ? -1 : end($stack);
                $right = $i;
                $count = ($mid - $left) * ($right - $mid);
                $sumMax += $nums[$mid] * $count;
            }
            $stack[] = $i;
        }

        // Sum of minimums
        $stack = [];
        $sumMin = 0;
        for ($i = 0; $i <= $n; $i++) {
            while (!empty($stack) && ($i == $n || $nums[end($stack)] >= $nums[$i])) {
                $mid = array_pop($stack);
                $left = empty($stack) ? -1 : end($stack);
                $right = $i;
                $count = ($mid - $left) * ($right - $mid);
                $sumMin += $nums[$mid] * $count;
            }
            $stack[] = $i;
        }

        return $sumMax - $sumMin;
    }
}
```

## Swift

```swift
class Solution {
    func subArrayRanges(_ nums: [Int]) -> Int {
        let n = nums.count
        var sumMin: Int64 = 0
        var stack = [Int]()
        
        // Calculate contribution as minimum
        for i in 0...n {
            while let last = stack.last, (i == n || nums[last] >= nums[i]) {
                let mid = stack.removeLast()
                let left = stack.last ?? -1
                let right = i
                let count = Int64(right - mid) * Int64(mid - left)
                sumMin += count * Int64(nums[mid])
            }
            if i < n { stack.append(i) }
        }
        
        var sumMax: Int64 = 0
        stack.removeAll()
        
        // Calculate contribution as maximum
        for i in 0...n {
            while let last = stack.last, (i == n || nums[last] <= nums[i]) {
                let mid = stack.removeLast()
                let left = stack.last ?? -1
                let right = i
                let count = Int64(right - mid) * Int64(mid - left)
                sumMax += count * Int64(nums[mid])
            }
            if i < n { stack.append(i) }
        }
        
        return Int(sumMax - sumMin)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun subArrayRanges(nums: IntArray): Long {
        val n = nums.size
        var sumMax = 0L
        var sumMin = 0L

        // Max contributions
        val stackMax = java.util.ArrayDeque<Int>()
        for (i in 0..n) {
            while (!stackMax.isEmpty() && (i == n || nums[stackMax.peek()] <= nums[i])) {
                val mid = stackMax.pop()
                val left = if (stackMax.isEmpty()) -1 else stackMax.peek()
                val right = i
                sumMax += (mid - left).toLong() * (right - mid) * nums[mid].toLong()
            }
            if (i < n) stackMax.push(i)
        }

        // Min contributions
        val stackMin = java.util.ArrayDeque<Int>()
        for (i in 0..n) {
            while (!stackMin.isEmpty() && (i == n || nums[stackMin.peek()] >= nums[i])) {
                val mid = stackMin.pop()
                val left = if (stackMin.isEmpty()) -1 else stackMin.peek()
                val right = i
                sumMin += (mid - left).toLong() * (right - mid) * nums[mid].toLong()
            }
            if (i < n) stackMin.push(i)
        }

        return sumMax - sumMin
    }
}
```

## Dart

```dart
class Solution {
  int subArrayRanges(List<int> nums) {
    int n = nums.length;
    List<int> left = List.filled(n, 0);
    List<int> right = List.filled(n, 0);
    List<int> stack = [];

    // Contributions as minimums
    // left distances: previous less element (strict)
    for (int i = 0; i < n; i++) {
      while (stack.isNotEmpty && nums[stack.last] >= nums[i]) {
        stack.removeLast();
      }
      int prev = stack.isEmpty ? -1 : stack.last;
      left[i] = i - prev;
      stack.add(i);
    }

    // right distances: next less-or-equal element
    stack.clear();
    for (int i = n - 1; i >= 0; i--) {
      while (stack.isNotEmpty && nums[stack.last] > nums[i]) {
        stack.removeLast();
      }
      int nxt = stack.isEmpty ? n : stack.last;
      right[i] = nxt - i;
      stack.add(i);
    }

    int sumMin = 0;
    for (int i = 0; i < n; i++) {
      sumMin += nums[i] * left[i] * right[i];
    }

    // Contributions as maximums
    // reuse left and right arrays
    // left distances: previous greater element (strict)
    stack.clear();
    for (int i = 0; i < n; i++) {
      while (stack.isNotEmpty && nums[stack.last] <= nums[i]) {
        stack.removeLast();
      }
      int prev = stack.isEmpty ? -1 : stack.last;
      left[i] = i - prev;
      stack.add(i);
    }

    // right distances: next greater-or-equal element
    stack.clear();
    for (int i = n - 1; i >= 0; i--) {
      while (stack.isNotEmpty && nums[stack.last] < nums[i]) {
        stack.removeLast();
      }
      int nxt = stack.isEmpty ? n : stack.last;
      right[i] = nxt - i;
      stack.add(i);
    }

    int sumMax = 0;
    for (int i = 0; i < n; i++) {
      sumMax += nums[i] * left[i] * right[i];
    }

    return sumMax - sumMin;
  }
}
```

## Golang

```go
func subArrayRanges(nums []int) int64 {
    n := len(nums)
    // helper to calculate total contribution as min or max
    calc := func(isMin bool) int64 {
        var stack []int
        var total int64
        for i := 0; i <= n; i++ {
            var cur int
            if i < n {
                cur = nums[i]
            }
            // pop while condition holds
            for len(stack) > 0 && (i == n ||
                (isMin && nums[stack[len(stack)-1]] >= cur) ||
                (!isMin && nums[stack[len(stack)-1]] <= cur)) {
                mid := stack[len(stack)-1]
                stack = stack[:len(stack)-1]
                left := -1
                if len(stack) > 0 {
                    left = stack[len(stack)-1]
                }
                right := i
                cnt := int64(mid-left) * int64(right-mid)
                total += cnt * int64(nums[mid])
            }
            if i < n {
                stack = append(stack, i)
            }
        }
        return total
    }

    sumMax := calc(false)
    sumMin := calc(true)
    return sumMax - sumMin
}
```

## Ruby

```ruby
def sub_array_ranges(nums)
  n = nums.length

  # Sum of maximums
  max_sum = 0
  stack = []
  (0..n).each do |i|
    cur = i < n ? nums[i] : Float::INFINITY
    while !stack.empty? && cur > nums[stack[-1]]
      mid = stack.pop
      left = stack.empty? ? -1 : stack[-1]
      right = i
      max_sum += nums[mid] * (mid - left) * (right - mid)
    end
    stack << i if i < n
  end

  # Sum of minimums
  min_sum = 0
  stack.clear
  (0..n).each do |i|
    cur = i < n ? nums[i] : -Float::INFINITY
    while !stack.empty? && cur < nums[stack[-1]]
      mid = stack.pop
      left = stack.empty? ? -1 : stack[-1]
      right = i
      min_sum += nums[mid] * (mid - left) * (right - mid)
    end
    stack << i if i < n
  end

  max_sum - min_sum
end
```

## Scala

```scala
object Solution {
    def subArrayRanges(nums: Array[Int]): Long = {
        val n = nums.length

        def total(isMin: Boolean): Long = {
            val stack = new java.util.ArrayDeque[Int]()
            var sum: Long = 0L
            var i = 0
            while (i <= n) {
                while (!stack.isEmpty && (i == n || (if (isMin) nums(stack.peek()) >= nums(i) else nums(stack.peek()) <= nums(i)))) {
                    val idx = stack.pop()
                    val left = if (stack.isEmpty) -1 else stack.peek()
                    val right = i
                    val cnt = (idx - left).toLong * (right - idx)
                    sum += cnt * nums(idx).toLong
                }
                if (i < n) {
                    stack.push(i)
                }
                i += 1
            }
            sum
        }

        total(false) - total(true)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sub_array_ranges(nums: Vec<i32>) -> i64 {
        let n = nums.len();

        // Sum of contributions as minimums
        let mut min_sum: i64 = 0;
        let mut stack: Vec<usize> = Vec::new();
        for i in 0..=n {
            while let Some(&mid) = stack.last() {
                if i == n || (i < n && nums[i] <= nums[mid]) {
                    stack.pop();
                    let left = if let Some(&l) = stack.last() { l as i64 } else { -1 };
                    let right = i as i64;
                    let cnt = (mid as i64 - left) * (right - mid as i64);
                    min_sum += cnt * nums[mid] as i64;
                } else {
                    break;
                }
            }
            if i < n {
                stack.push(i);
            }
        }

        // Sum of contributions as maximums
        let mut max_sum: i64 = 0;
        let mut stack: Vec<usize> = Vec::new();
        for i in 0..=n {
            while let Some(&mid) = stack.last() {
                if i == n || (i < n && nums[i] >= nums[mid]) {
                    stack.pop();
                    let left = if let Some(&l) = stack.last() { l as i64 } else { -1 };
                    let right = i as i64;
                    let cnt = (mid as i64 - left) * (right - mid as i64);
                    max_sum += cnt * nums[mid] as i64;
                } else {
                    break;
                }
            }
            if i < n {
                stack.push(i);
            }
        }

        max_sum - min_sum
    }
}
```

## Racket

```racket
(define/contract (sub-array-ranges nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((v (list->vector nums))
         (n (vector-length v)))
    (define (calc-sum cmp)
      (let ((stack (make-vector (+ n 1) -1))
            (top -1)
            (total 0))
        (for ([i (in-range 0 (+ n 1))])
          (define cur (if (< i n) (vector-ref v i) #f))
          ;; pop while the condition for contribution holds
          (let loop ()
            (when (and (> top -1)
                       (or (= i n)
                           (cmp cur (vector-ref v (vector-ref stack top)))))
              (define mid (vector-ref stack top))
              (set! top (- top 1))
              (define left (if (> top -1) (vector-ref stack top) -1))
              (define right i)
              (define cnt (* (- mid left) (- right mid)))
              (set! total (+ total (* cnt (vector-ref v mid))))
              (loop)))
          ;; push current index if still within array bounds
          (when (< i n)
            (set! top (+ top 1))
            (vector-set! stack top i)))
        total))
    (let ((sum-max (calc-sum (lambda (a b) (>= a b))))
          (sum-min (calc-sum (lambda (a b) (<= a b)))))
      (- sum-max sum-min))))
```

## Erlang

```erlang
-module(solution).
-export([sub_array_ranges/1]).

-spec sub_array_ranges(Nums :: [integer()]) -> integer().
sub_array_ranges(Nums) ->
    MaxSum = contribution(Nums, true),
    MinSum = contribution(Nums, false),
    MaxSum - MinSum.

%% Compute total contribution of each element being max (IsMax=true) or min (IsMax=false)
-spec contribution([integer()], boolean()) -> integer().
contribution(Nums, IsMax) ->
    PopCond =
        case IsMax of
            true  -> fun(A, B) -> A =< B end;   % for maximums: pop while top <= current
            false -> fun(A, B) -> A >= B end    % for minimums: pop while top >= current
        end,
    N = length(Nums),
    {StackAfterLoop, Acc1} = loop(0, Nums, [], 0, PopCond),
    finalize(StackAfterLoop, N, Acc1).

%% Process the array left to right
-spec loop(integer(), [integer()], [{integer(), integer()}], integer(),
          fun((integer(), integer()) -> boolean())) ->
          {[{integer(), integer()}], integer()}.
loop(_Idx, [], Stack, Acc, _PopCond) ->
    {Stack, Acc};
loop(Idx, [Val | Rest], Stack, Acc, PopCond) ->
    {NewStack, NewAcc} = pop_while(Idx, Val, Stack, Acc, PopCond),
    loop(Idx + 1, Rest, [{Idx, Val} | NewStack], NewAcc, PopCond).

%% Pop elements that satisfy the condition and accumulate their contributions
-spec pop_while(integer(), integer(),
               [{integer(), integer()}], integer(),
               fun((integer(), integer()) -> boolean())) ->
               {[{integer(), integer()}], integer()}.
pop_while(_Idx, _Val, [], Acc, _PopCond) ->
    {[], Acc};
pop_while(Idx, Val, [{MidIdx, MidVal} = Top | RestStack] = Stack, Acc, PopCond) ->
    case PopCond(MidVal, Val) of
        true ->
            LeftIdx =
                case RestStack of
                    [] -> -1;
                    [{LIdx, _} | _] -> LIdx
                end,
            Contribution = (Idx - MidIdx) * (MidIdx - LeftIdx) * MidVal,
            pop_while(Idx, Val, RestStack, Acc + Contribution, PopCond);
        false ->
            {Stack, Acc}
    end.

%% After traversal, pop remaining elements using right boundary = N
-spec finalize([{integer(), integer()}], integer(), integer()) -> integer().
finalize([], _Right, Acc) ->
    Acc;
finalize([{MidIdx, MidVal} | RestStack] = Stack, Right, Acc) ->
    LeftIdx =
        case RestStack of
            [] -> -1;
            [{LIdx, _} | _] -> LIdx
        end,
    Contribution = (Right - MidIdx) * (MidIdx - LeftIdx) * MidVal,
    finalize(RestStack, Right, Acc + Contribution).
```

## Elixir

```elixir
defmodule Solution do
  @spec sub_array_ranges(nums :: [integer]) :: integer
  def sub_array_ranges(nums) do
    min_sum = sum_contrib(nums, fn a, b -> a >= b end)
    max_sum = sum_contrib(nums, fn a, b -> a <= b end)
    max_sum - min_sum
  end

  defp sum_contrib(nums, cmp) do
    n = length(nums)
    arr = :array.from_list(nums)

    {stack, acc} =
      Enum.reduce(0..(n - 1), {[], 0}, fn i, {stack, acc} ->
        cur = :array.get(arr, i)
        {new_stack, new_acc} = pop_while(stack, i, cur, arr, cmp, acc)
        {[i | new_stack], new_acc}
      end)

    finalize(stack, n, arr, acc)
  end

  defp pop_while([], _i, _cur, _arr, _cmp, acc), do: {[], acc}

  defp pop_while([mid | rest] = stack, i, cur, arr, cmp, acc) do
    mid_val = :array.get(arr, mid)

    if cmp.(mid_val, cur) do
      left = if rest == [], do: -1, else: hd(rest)
      cnt = (mid - left) * (i - mid)
      acc2 = acc + cnt * mid_val
      pop_while(rest, i, cur, arr, cmp, acc2)
    else
      {stack, acc}
    end
  end

  defp finalize([], _right, _arr, acc), do: acc

  defp finalize([mid | rest] = stack, right, arr, acc) do
    left = if rest == [], do: -1, else: hd(rest)
    cnt = (mid - left) * (right - mid)
    val = :array.get(arr, mid)
    finalize(rest, right, arr, acc + cnt * val)
  end
end
```
