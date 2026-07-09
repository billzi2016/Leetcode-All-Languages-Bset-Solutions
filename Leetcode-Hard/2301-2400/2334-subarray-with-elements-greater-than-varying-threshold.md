# 2334. Subarray With Elements Greater Than Varying Threshold

## Cpp

```cpp
class Solution {
public:
    int validSubarraySize(vector<int>& nums, int threshold) {
        int n = nums.size();
        vector<int> left(n), right(n);
        stack<int> st;
        // previous smaller (strict)
        for (int i = 0; i < n; ++i) {
            while (!st.empty() && nums[st.top()] >= nums[i]) st.pop();
            left[i] = st.empty() ? -1 : st.top();
            st.push(i);
        }
        while (!st.empty()) st.pop();
        // next smaller (strict)
        for (int i = n - 1; i >= 0; --i) {
            while (!st.empty() && nums[st.top()] >= nums[i]) st.pop();
            right[i] = st.empty() ? n : st.top();
            st.push(i);
        }
        for (int i = 0; i < n; ++i) {
            long long len = (long long)right[i] - left[i] - 1;
            if ((long long)nums[i] * len > threshold) return (int)len;
        }
        return -1;
    }
};
```

## Java

```java
class Solution {
    public int validSubarraySize(int[] nums, int threshold) {
        int n = nums.length;
        int[] left = new int[n];
        int[] right = new int[n];
        java.util.ArrayDeque<Integer> stack = new java.util.ArrayDeque<>();

        // previous smaller element index
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && nums[stack.peek()] >= nums[i]) {
                stack.pop();
            }
            left[i] = stack.isEmpty() ? -1 : stack.peek();
            stack.push(i);
        }

        stack.clear();

        // next smaller element index
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && nums[stack.peek()] >= nums[i]) {
                stack.pop();
            }
            right[i] = stack.isEmpty() ? n : stack.peek();
            stack.push(i);
        }

        for (int i = 0; i < n; i++) {
            int len = right[i] - left[i] - 1;
            if ((long) nums[i] * len > threshold) {
                return len;
            }
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def validSubarraySize(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        n = len(nums)
        left = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        right = [n] * n
        stack.clear()
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        for i in range(n):
            max_len = right[i] - left[i] - 1
            req = threshold // nums[i] + 1
            if req <= max_len:
                return req
        return -1
```

## Python3

```python
from typing import List

class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        left = [-1] * n
        right = [n] * n

        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack.clear()
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        ans = float('inf')
        for i in range(n):
            max_len = right[i] - left[i] - 1
            need = threshold // nums[i] + 1
            if need <= max_len and need < ans:
                ans = need

        return ans if ans != float('inf') else -1
```

## C

```c
#include <stdlib.h>

int validSubarraySize(int* nums, int numsSize, int threshold) {
    if (numsSize == 0) return -1;
    
    int *left = (int*)malloc(numsSize * sizeof(int));
    int *right = (int*)malloc(numsSize * sizeof(int));
    int *stack = (int*)malloc(numsSize * sizeof(int));
    int top = -1;

    // previous smaller element (strictly)
    for (int i = 0; i < numsSize; ++i) {
        while (top >= 0 && nums[stack[top]] >= nums[i]) {
            --top;
        }
        left[i] = (top >= 0) ? stack[top] : -1;
        stack[++top] = i;
    }

    // next smaller element (strictly)
    top = -1;
    for (int i = numsSize - 1; i >= 0; --i) {
        while (top >= 0 && nums[stack[top]] >= nums[i]) {
            --top;
        }
        right[i] = (top >= 0) ? stack[top] : numsSize;
        stack[++top] = i;
    }

    int answer = -1;
    for (int i = 0; i < numsSize; ++i) {
        long long len = (long long)right[i] - left[i] - 1; // maximal length where nums[i] is minimum
        long long required = (long long)threshold / nums[i] + 1; // smallest k such that nums[i]*k > threshold
        if (required <= len) {
            answer = (int)required;
            break;
        }
    }

    free(left);
    free(right);
    free(stack);
    return answer;
}
```

## Csharp

```csharp
public class Solution {
    public int ValidSubarraySize(int[] nums, int threshold) {
        int n = nums.Length;
        int[] left = new int[n];
        int[] right = new int[n];
        var stack = new Stack<int>();

        // previous smaller element index
        for (int i = 0; i < n; i++) {
            while (stack.Count > 0 && nums[stack.Peek()] >= nums[i]) {
                stack.Pop();
            }
            left[i] = stack.Count == 0 ? -1 : stack.Peek();
            stack.Push(i);
        }

        stack.Clear();

        // next smaller element index
        for (int i = n - 1; i >= 0; i--) {
            while (stack.Count > 0 && nums[stack.Peek()] >= nums[i]) {
                stack.Pop();
            }
            right[i] = stack.Count == 0 ? n : stack.Peek();
            stack.Push(i);
        }

        long th = threshold;
        for (int i = 0; i < n; i++) {
            int len = right[i] - left[i] - 1;
            if ((long)nums[i] * len > th) {
                return len;
            }
        }
        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} threshold
 * @return {number}
 */
var validSubarraySize = function(nums, threshold) {
    const n = nums.length;
    const left = new Array(n).fill(-1);
    const right = new Array(n).fill(n);
    
    // previous smaller element index
    let stack = [];
    for (let i = 0; i < n; i++) {
        while (stack.length && nums[stack[stack.length - 1]] >= nums[i]) {
            stack.pop();
        }
        left[i] = stack.length ? stack[stack.length - 1] : -1;
        stack.push(i);
    }
    
    // next smaller element index
    stack = [];
    for (let i = n - 1; i >= 0; i--) {
        while (stack.length && nums[stack[stack.length - 1]] >= nums[i]) {
            stack.pop();
        }
        right[i] = stack.length ? stack[stack.length - 1] : n;
        stack.push(i);
    }
    
    for (let i = 0; i < n; i++) {
        const maxLen = right[i] - left[i] - 1;
        const need = Math.floor(threshold / nums[i]) + 1;
        if (maxLen >= need) return need;
    }
    return -1;
};
```

## Typescript

```typescript
function validSubarraySize(nums: number[], threshold: number): number {
    const n = nums.length;
    const left = new Array<number>(n);
    const right = new Array<number>(n);
    const stack: number[] = [];

    // previous smaller element (strictly less)
    for (let i = 0; i < n; i++) {
        while (stack.length && nums[stack[stack.length - 1]] >= nums[i]) {
            stack.pop();
        }
        const prev = stack.length ? stack[stack.length - 1] : -1;
        left[i] = i - prev - 1;
        stack.push(i);
    }

    // next smaller element (strictly less)
    stack.length = 0;
    for (let i = n - 1; i >= 0; i--) {
        while (stack.length && nums[stack[stack.length - 1]] >= nums[i]) {
            stack.pop();
        }
        const nxt = stack.length ? stack[stack.length - 1] : n;
        right[i] = nxt - i - 1;
        stack.push(i);
    }

    for (let i = 0; i < n; i++) {
        const maxLen = left[i] + right[i] + 1;
        if (maxLen * nums[i] > threshold) {
            const need = Math.floor(threshold / nums[i]) + 1;
            return need <= maxLen ? need : maxLen;
        }
    }

    return -1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $threshold
     * @return Integer
     */
    function validSubarraySize($nums, $threshold) {
        $n = count($nums);
        $left = array_fill(0, $n, -1);
        $right = array_fill(0, $n, $n);

        // previous smaller element indices
        $stack = [];
        for ($i = 0; $i < $n; ++$i) {
            while (!empty($stack) && $nums[end($stack)] >= $nums[$i]) {
                array_pop($stack);
            }
            $left[$i] = empty($stack) ? -1 : end($stack);
            $stack[] = $i;
        }

        // next smaller element indices
        $stack = [];
        for ($i = $n - 1; $i >= 0; --$i) {
            while (!empty($stack) && $nums[end($stack)] >= $nums[$i]) {
                array_pop($stack);
            }
            $right[$i] = empty($stack) ? $n : end($stack);
            $stack[] = $i;
        }

        for ($i = 0; $i < $n; ++$i) {
            $maxLen = $right[$i] - $left[$i] - 1;
            // minimal length needed so that nums[i] * len > threshold
            $need = intdiv($threshold, $nums[$i]) + 1;
            if ($need <= $maxLen) {
                return $need;
            }
        }

        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func validSubarraySize(_ nums: [Int], _ threshold: Int) -> Int {
        let n = nums.count
        if n == 0 { return -1 }
        var left = Array(repeating: -1, count: n)
        var right = Array(repeating: n, count: n)
        var stack = [Int]()
        
        // previous smaller element
        for i in 0..<n {
            while let last = stack.last, nums[last] >= nums[i] {
                stack.removeLast()
            }
            left[i] = stack.last ?? -1
            stack.append(i)
        }
        
        stack.removeAll()
        // next smaller element
        for i in stride(from: n - 1, through: 0, by: -1) {
            while let last = stack.last, nums[last] >= nums[i] {
                stack.removeLast()
            }
            right[i] = stack.last ?? n
            stack.append(i)
        }
        
        let t64 = Int64(threshold)
        for i in 0..<n {
            let length = right[i] - left[i] - 1
            if Int64(nums[i]) * Int64(length) > t64 {
                return length
            }
        }
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun validSubarraySize(nums: IntArray, threshold: Int): Int {
        val n = nums.size
        val left = IntArray(n)
        val right = IntArray(n)

        // previous smaller element index
        val stack = java.util.ArrayDeque<Int>()
        for (i in 0 until n) {
            while (!stack.isEmpty() && nums[stack.peek()] >= nums[i]) {
                stack.pop()
            }
            left[i] = if (stack.isEmpty()) -1 else stack.peek()
            stack.push(i)
        }

        // next smaller element index
        stack.clear()
        for (i in n - 1 downTo 0) {
            while (!stack.isEmpty() && nums[stack.peek()] >= nums[i]) {
                stack.pop()
            }
            right[i] = if (stack.isEmpty()) n else stack.peek()
            stack.push(i)
        }

        for (i in 0 until n) {
            val span = right[i] - left[i] - 1
            val required = threshold / nums[i] + 1
            if (required <= span) return required
        }
        return -1
    }
}
```

## Dart

```dart
class Solution {
  int validSubarraySize(List<int> nums, int threshold) {
    int n = nums.length;
    List<int> left = List.filled(n, -1);
    List<int> right = List.filled(n, n);
    List<int> stack = [];

    // previous smaller element (strict)
    for (int i = 0; i < n; i++) {
      while (stack.isNotEmpty && nums[stack.last] >= nums[i]) {
        stack.removeLast();
      }
      left[i] = stack.isEmpty ? -1 : stack.last;
      stack.add(i);
    }

    stack.clear();

    // next smaller element (strict)
    for (int i = n - 1; i >= 0; i--) {
      while (stack.isNotEmpty && nums[stack.last] >= nums[i]) {
        stack.removeLast();
      }
      right[i] = stack.isEmpty ? n : stack.last;
      stack.add(i);
    }

    for (int i = 0; i < n; i++) {
      int maxLen = right[i] - left[i] - 1;
      int need = threshold ~/ nums[i]; // floor division
      if (maxLen > need) {
        return need + 1;
      }
    }
    return -1;
  }
}
```

## Golang

```go
func validSubarraySize(nums []int, threshold int) int {
    n := len(nums)
    left := make([]int, n)
    right := make([]int, n)

    // previous smaller element (strictly less)
    stack := []int{}
    for i := 0; i < n; i++ {
        for len(stack) > 0 && nums[stack[len(stack)-1]] >= nums[i] {
            stack = stack[:len(stack)-1]
        }
        if len(stack) == 0 {
            left[i] = -1
        } else {
            left[i] = stack[len(stack)-1]
        }
        stack = append(stack, i)
    }

    // next smaller element (strictly less)
    stack = []int{}
    for i := n - 1; i >= 0; i-- {
        for len(stack) > 0 && nums[stack[len(stack)-1]] >= nums[i] {
            stack = stack[:len(stack)-1]
        }
        if len(stack) == 0 {
            right[i] = n
        } else {
            right[i] = stack[len(stack)-1]
        }
        stack = append(stack, i)
    }

    for i := 0; i < n; i++ {
        maxLen := right[i] - left[i] - 1
        kMin := threshold/nums[i] + 1 // smallest length satisfying nums[i] > threshold/k
        if kMin <= maxLen {
            return kMin
        }
    }
    return -1
}
```

## Ruby

```ruby
def valid_subarray_size(nums, threshold)
  n = nums.length
  prev = Array.new(n, -1)
  stack = []

  (0...n).each do |i|
    while !stack.empty? && nums[stack[-1]] >= nums[i]
      stack.pop
    end
    prev[i] = stack.empty? ? -1 : stack[-1]
    stack << i
  end

  nxt = Array.new(n, n)
  stack.clear

  (n - 1).downto(0) do |i|
    while !stack.empty? && nums[stack[-1]] >= nums[i]
      stack.pop
    end
    nxt[i] = stack.empty? ? n : stack[-1]
    stack << i
  end

  (0...n).each do |i|
    max_len = nxt[i] - prev[i] - 1
    need = threshold / nums[i] + 1
    return need if need <= max_len
  end

  -1
end
```

## Scala

```scala
object Solution {
    def validSubarraySize(nums: Array[Int], threshold: Int): Int = {
        val n = nums.length
        val left = new Array[Int](n)
        val right = new Array[Int](n)

        // previous smaller element index (strictly less), -1 if none
        val stack = new java.util.ArrayDeque[Int]()
        for (i <- 0 until n) {
            while (!stack.isEmpty && nums(stack.peekLast()) >= nums(i)) {
                stack.pollLast()
            }
            left(i) = if (stack.isEmpty) -1 else stack.peekLast()
            stack.addLast(i)
        }

        // next smaller element index (strictly less), n if none
        stack.clear()
        for (i <- (n - 1) to 0 by -1) {
            while (!stack.isEmpty && nums(stack.peekLast()) >= nums(i)) {
                stack.pollLast()
            }
            right(i) = if (stack.isEmpty) n else stack.peekLast()
            stack.addLast(i)
        }

        for (i <- 0 until n) {
            val maxLen = right(i) - left(i) - 1
            // smallest k such that nums[i] > threshold / k  => k > threshold / nums[i]
            val kMin = threshold / nums(i) + 1
            if (kMin <= maxLen) return kMin
        }
        -1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn valid_subarray_size(nums: Vec<i32>, threshold: i32) -> i32 {
        let n = nums.len();
        if n == 0 {
            return -1;
        }
        let mut left = vec![-1i32; n];
        let mut right = vec![n as i32; n];
        let mut stack: Vec<usize> = Vec::new();

        // previous smaller element
        for i in 0..n {
            while let Some(&last) = stack.last() {
                if nums[last] >= nums[i] {
                    stack.pop();
                } else {
                    break;
                }
            }
            left[i] = if let Some(&last) = stack.last() { last as i32 } else { -1 };
            stack.push(i);
        }

        // next smaller element
        stack.clear();
        for i in (0..n).rev() {
            while let Some(&last) = stack.last() {
                if nums[last] >= nums[i] {
                    stack.pop();
                } else {
                    break;
                }
            }
            right[i] = if let Some(&last) = stack.last() { last as i32 } else { n as i32 };
            stack.push(i);
        }

        let thresh = threshold as i64;
        for i in 0..n {
            let len = (right[i] - left[i] - 1) as i64;
            let req = thresh / nums[i] as i64 + 1; // minimal k satisfying nums[i] > threshold/k
            if req <= len {
                return req as i32;
            }
        }
        -1
    }
}
```

## Racket

```racket
(define/contract (valid-subarray-size nums threshold)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((v (list->vector nums))
         (n (vector-length v))
         (left (make-vector n -1))
         (right (make-vector n n)))
    ;; compute previous smaller element indices
    (let loop-left ((i 0) (stk '()))
      (when (< i n)
        (define cur (vector-ref v i))
        (define new-stk
          (let pop ((s stk))
            (if (and (pair? s)
                     (>= (vector-ref v (car s)) cur))
                (pop (cdr s))
                s)))
        (vector-set! left i (if (null? new-stk) -1 (car new-stk)))
        (loop-left (+ i 1) (cons i new-stk))))
    ;; compute next smaller element indices
    (let loop-right ((i (- n 1)) (stk '()))
      (when (>= i 0)
        (define cur (vector-ref v i))
        (define new-stk
          (let pop ((s stk))
            (if (and (pair? s)
                     (>= (vector-ref v (car s)) cur))
                (pop (cdr s))
                s)))
        (vector-set! right i (if (null? new-stk) n (car new-stk)))
        (loop-right (- i 1) (cons i new-stk))))
    ;; search for a valid subarray size
    (let search ((i 0))
      (cond [(>= i n) -1]
            [else
             (define span (- (vector-ref right i)
                             (vector-ref left i) 1))
             (define req (+ (quotient threshold (vector-ref v i)) 1))
             (if (<= req span)
                 req
                 (search (+ i 1)))]))))
```

## Erlang

```erlang
-spec valid_subarray_size(Nums :: [integer()], Threshold :: integer()) -> integer().
valid_subarray_size(Nums, Threshold) ->
    Tuple = list_to_tuple(Nums),
    LeftList = build_left(Tuple),
    RightList = build_right(Tuple),
    LeftTuple = list_to_tuple(LeftList),
    RightTuple = list_to_tuple(RightList),
    N = tuple_size(Tuple),
    find_answer(1, N, Threshold, Tuple, LeftTuple, RightTuple).

%% Build previous smaller index (0 if none)
build_left(Tuple) ->
    N = tuple_size(Tuple),
    build_left_loop(1, N, [], [], Tuple).

build_left_loop(I, N, Stack, Acc, Tuple) when I =< N ->
    Curr = element(I, Tuple),
    NewStack = pop_while(Stack, Curr, Tuple),
    LeftIdx = case NewStack of
        [] -> 0;
        [Top|_] -> Top
    end,
    build_left_loop(I + 1, N, [I | NewStack], [LeftIdx | Acc], Tuple);
build_left_loop(_, _, _, Acc, _) ->
    lists:reverse(Acc).

%% Build next smaller index (N+1 if none)
build_right(Tuple) ->
    N = tuple_size(Tuple),
    build_right_loop(N, N, [], [], Tuple).

build_right_loop(I, N, Stack, Acc, Tuple) when I >= 1 ->
    Curr = element(I, Tuple),
    NewStack = pop_while(Stack, Curr, Tuple),
    RightIdx = case NewStack of
        [] -> N + 1;
        [Top|_] -> Top
    end,
    build_right_loop(I - 1, N, [I | NewStack], [RightIdx | Acc], Tuple);
build_right_loop(_, _, _, Acc, _) ->
    lists:reverse(Acc).

%% Pop while top element >= current value
pop_while([], _Curr, _Tuple) -> [];
pop_while([H|T] = Stack, Curr, Tuple) ->
    case element(H, Tuple) >= Curr of
        true -> pop_while(T, Curr, Tuple);
        false -> Stack
    end.

%% Find any valid subarray length
find_answer(I, N, Threshold, NumTuple, LeftTuple, RightTuple) when I =< N ->
    Num = element(I, NumTuple),
    MaxLen = element(I, RightTuple) - element(I, LeftTuple) - 1,
    Required = (Threshold div Num) + 1,
    if
        Required =< MaxLen -> Required;
        true -> find_answer(I + 1, N, Threshold, NumTuple, LeftTuple, RightTuple)
    end;
find_answer(_, _, _, _, _, _) ->
    -1.
```

## Elixir

```elixir
defmodule Solution do
  @spec valid_subarray_size(nums :: [integer], threshold :: integer) :: integer
  def valid_subarray_size(nums, threshold) do
    n = length(nums)
    arr = List.to_tuple(nums)

    prev_arr = compute_prev(arr, n)
    next_arr = compute_next(arr, n)

    Enum.reduce_while(0..(n - 1), -1, fn i, _acc ->
      max_len = :array.get(i, next_arr) - :array.get(i, prev_arr) - 1
      needed = div(threshold, :erlang.element(i + 1, arr)) + 1

      if needed <= max_len do
        {:halt, needed}
      else
        {:cont, -1}
      end
    end)
  end

  defp compute_prev(arr, n) do
    {prev_arr, _stack} =
      Enum.reduce(0..(n - 1), {%array.new(n, default: -1), []}, fn i,
                                                                   {prev_acc, stack} ->
        val = :erlang.element(i + 1, arr)
        new_stack = pop_while_ge(stack, val, arr)

        prev_index =
          case new_stack do
            [] -> -1
            [top | _] -> top
          end

        prev_acc2 = :array.set(i, prev_index, prev_acc)
        {prev_acc2, [i | new_stack]}
      end)

    prev_arr
  end

  defp compute_next(arr, n) do
    seq = :lists.seq(n - 1, 0, -1)

    {next_arr, _stack} =
      Enum.reduce(seq, {%array.new(n, default: n), []}, fn i,
                                                          {next_acc, stack} ->
        val = :erlang.element(i + 1, arr)
        new_stack = pop_while_ge(stack, val, arr)

        next_index =
          case new_stack do
            [] -> n
            [top | _] -> top
          end

        next_acc2 = :array.set(i, next_index, next_acc)
        {next_acc2, [i | new_stack]}
      end)

    next_arr
  end

  defp pop_while_ge([], _val, _arr), do: []

  defp pop_while_ge([top | rest] = stack, val, arr) do
    if :erlang.element(top + 1, arr) >= val do
      pop_while_ge(rest, val, arr)
    else
      stack
    end
  end
end
```
