# 1793. Maximum Score of a Good Subarray

## Cpp

```cpp
class Solution {
public:
    int maximumScore(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> left(n), right(n);
        // previous smaller element
        stack<int> st;
        for (int i = 0; i < n; ++i) {
            while (!st.empty() && nums[st.top()] >= nums[i]) st.pop();
            left[i] = st.empty() ? -1 : st.top();
            st.push(i);
        }
        // next smaller element
        while (!st.empty()) st.pop();
        for (int i = n - 1; i >= 0; --i) {
            while (!st.empty() && nums[st.top()] >= nums[i]) st.pop();
            right[i] = st.empty() ? n : st.top();
            st.push(i);
        }
        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            if (left[i] < k && right[i] > k) {
                long long cur = 1LL * nums[i] * (right[i] - left[i] - 1);
                if (cur > ans) ans = cur;
            }
        }
        return (int)ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int maximumScore(int[] nums, int k) {
        int n = nums.length;
        int[] left = new int[n];
        int[] right = new int[n];
        Arrays.fill(left, -1);
        Arrays.fill(right, n);
        
        Deque<Integer> stack = new ArrayDeque<>();
        // previous smaller element
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && nums[stack.peek()] >= nums[i]) {
                stack.pop();
            }
            left[i] = stack.isEmpty() ? -1 : stack.peek();
            stack.push(i);
        }
        
        stack.clear();
        // next smaller element
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && nums[stack.peek()] >= nums[i]) {
                stack.pop();
            }
            right[i] = stack.isEmpty() ? n : stack.peek();
            stack.push(i);
        }
        
        long ans = 0;
        for (int i = 0; i < n; i++) {
            if (left[i] < k && right[i] > k) {
                long score = (long) nums[i] * (right[i] - left[i] - 1);
                if (score > ans) ans = score;
            }
        }
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        left = [-1] * n
        stack = []
        # previous smaller element (strictly less)
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        right = [n] * n
        stack.clear()
        # next smaller element (strictly less)
        for i in range(n):
            while stack and nums[i] < nums[stack[-1]]:
                idx = stack.pop()
                right[idx] = i
            stack.append(i)

        ans = 0
        for i in range(n):
            if left[i] < k and right[i] > k:
                length = right[i] - left[i] - 1
                score = nums[i] * length
                if score > ans:
                    ans = score
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = [-1] * n
        right = [n] * n
        stack = []

        # previous smaller element (strictly less)
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack.clear()
        # next smaller element (strictly less)
        for i in range(n):
            while stack and nums[i] < nums[stack[-1]]:
                idx = stack.pop()
                right[idx] = i
            stack.append(i)

        ans = 0
        for i in range(n):
            if left[i] < k < right[i]:
                area = (right[i] - left[i] - 1) * nums[i]
                if area > ans:
                    ans = area
        return ans
```

## C

```c
int maximumScore(int* nums, int numsSize, int k) {
    int n = numsSize;
    int *left = (int*)malloc(n * sizeof(int));
    int *right = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) left[i] = -1;
    for (int i = 0; i < n; ++i) right[i] = n;

    int *stack = (int*)malloc(n * sizeof(int));
    int top = -1;

    // compute left boundaries
    for (int i = n - 1; i >= 0; --i) {
        while (top >= 0 && nums[stack[top]] > nums[i]) {
            left[stack[top]] = i;
            --top;
        }
        stack[++top] = i;
    }

    // compute right boundaries
    top = -1;
    for (int i = 0; i < n; ++i) {
        while (top >= 0 && nums[stack[top]] > nums[i]) {
            right[stack[top]] = i;
            --top;
        }
        stack[++top] = i;
    }

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        if (left[i] < k && right[i] > k) {
            long long cur = (long long)nums[i] * (right[i] - left[i] - 1);
            if (cur > ans) ans = cur;
        }
    }

    free(left);
    free(right);
    free(stack);
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaximumScore(int[] nums, int k) {
        int n = nums.Length;
        int[] left = new int[n];
        int[] right = new int[n];
        for (int i = 0; i < n; i++) left[i] = -1;
        for (int i = 0; i < n; i++) right[i] = n;

        var stack = new System.Collections.Generic.Stack<int>();

        // nearest smaller to the left
        for (int i = 0; i < n; i++) {
            while (stack.Count > 0 && nums[stack.Peek()] >= nums[i]) {
                stack.Pop();
            }
            left[i] = stack.Count == 0 ? -1 : stack.Peek();
            stack.Push(i);
        }

        // nearest smaller to the right
        stack.Clear();
        for (int i = n - 1; i >= 0; i--) {
            while (stack.Count > 0 && nums[stack.Peek()] >= nums[i]) {
                stack.Pop();
            }
            right[i] = stack.Count == 0 ? n : stack.Peek();
            stack.Push(i);
        }

        long ans = 0;
        for (int i = 0; i < n; i++) {
            if (left[i] < k && right[i] > k) {
                long len = right[i] - left[i] - 1;
                long score = (long)nums[i] * len;
                if (score > ans) ans = score;
            }
        }

        return (int)ans;
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
var maximumScore = function(nums, k) {
    const n = nums.length;
    const left = new Array(n).fill(-1);
    const right = new Array(n).fill(n);
    let stack = [];

    // nearest smaller element on the left (strictly smaller)
    for (let i = 0; i < n; ++i) {
        while (stack.length && nums[stack[stack.length - 1]] >= nums[i]) {
            stack.pop();
        }
        left[i] = stack.length ? stack[stack.length - 1] : -1;
        stack.push(i);
    }

    // nearest smaller element on the right (strictly smaller)
    stack = [];
    for (let i = 0; i < n; ++i) {
        while (stack.length && nums[stack[stack.length - 1]] > nums[i]) {
            const idx = stack.pop();
            right[idx] = i;
        }
        stack.push(i);
    }

    let ans = 0;
    for (let i = 0; i < n; ++i) {
        if (left[i] < k && right[i] > k) {
            const size = right[i] - left[i] - 1;
            const score = nums[i] * size;
            if (score > ans) ans = score;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function maximumScore(nums: number[], k: number): number {
    const n = nums.length;
    const left = new Array<number>(n);
    const right = new Array<number>(n).fill(n);

    // previous smaller element indices
    const stackL: number[] = [];
    for (let i = 0; i < n; ++i) {
        while (stackL.length && nums[stackL[stackL.length - 1]] >= nums[i]) {
            stackL.pop();
        }
        left[i] = stackL.length ? stackL[stackL.length - 1] : -1;
        stackL.push(i);
    }

    // next smaller element indices
    const stackR: number[] = [];
    for (let i = 0; i < n; ++i) {
        while (stackR.length && nums[i] < nums[stackR[stackR.length - 1]]) {
            const idx = stackR.pop()!;
            right[idx] = i;
        }
        stackR.push(i);
    }

    let ans = 0;
    for (let i = 0; i < n; ++i) {
        if (left[i] < k && right[i] > k) {
            const len = right[i] - left[i] - 1;
            const score = nums[i] * len;
            if (score > ans) ans = score;
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
    function maximumScore($nums, $k) {
        $n = count($nums);
        $left = array_fill(0, $n, -1);
        $right = array_fill(0, $n, $n);

        // previous smaller element indices
        $stack = [];
        for ($i = 0; $i < $n; $i++) {
            while (!empty($stack) && $nums[end($stack)] >= $nums[$i]) {
                array_pop($stack);
            }
            if (!empty($stack)) {
                $left[$i] = end($stack);
            } else {
                $left[$i] = -1;
            }
            $stack[] = $i;
        }

        // next smaller element indices
        $stack = [];
        for ($i = $n - 1; $i >= 0; $i--) {
            while (!empty($stack) && $nums[end($stack)] >= $nums[$i]) {
                array_pop($stack);
            }
            if (!empty($stack)) {
                $right[$i] = end($stack);
            } else {
                $right[$i] = $n;
            }
            $stack[] = $i;
        }

        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($left[$i] < $k && $right[$i] > $k) {
                $len = $right[$i] - $left[$i] - 1;
                $score = $nums[$i] * $len;
                if ($score > $ans) {
                    $ans = $score;
                }
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maximumScore(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var left = Array(repeating: -1, count: n)
        var right = Array(repeating: n, count: n)
        var stack = [Int]()
        
        // previous smaller element (strictly less)
        for i in 0..<n {
            while let last = stack.last, nums[last] >= nums[i] {
                stack.removeLast()
            }
            left[i] = stack.last ?? -1
            stack.append(i)
        }
        
        stack.removeAll()
        // next smaller element to the right (strictly less)
        for i in stride(from: n - 1, through: 0, by: -1) {
            while let last = stack.last, nums[last] >= nums[i] {
                stack.removeLast()
            }
            right[i] = stack.last ?? n
            stack.append(i)
        }
        
        var ans = 0
        for i in 0..<n {
            if left[i] < k && right[i] > k {
                let length = right[i] - left[i] - 1
                let score = nums[i] * length
                if score > ans { ans = score }
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumScore(nums: IntArray, k: Int): Int {
        val n = nums.size
        val left = IntArray(n) { -1 }
        val right = IntArray(n) { n }
        val stack = java.util.ArrayDeque<Int>()

        // previous smaller element to the left
        for (i in n - 1 downTo 0) {
            while (!stack.isEmpty() && nums[stack.peek()] > nums[i]) {
                val idx = stack.pop()
                left[idx] = i
            }
            stack.push(i)
        }

        stack.clear()

        // next smaller element to the right
        for (i in 0 until n) {
            while (!stack.isEmpty() && nums[stack.peek()] > nums[i]) {
                val idx = stack.pop()
                right[idx] = i
            }
            stack.push(i)
        }

        var ans = 0L
        for (i in 0 until n) {
            if (left[i] < k && right[i] > k) {
                val length = right[i] - left[i] - 1
                val score = nums[i].toLong() * length.toLong()
                if (score > ans) ans = score
            }
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int maximumScore(List<int> nums, int k) {
    int n = nums.length;
    List<int> left = List.filled(n, -1);
    List<int> right = List.filled(n, n);
    List<int> stack = [];

    // Compute previous smaller element indices (strictly less)
    for (int i = 0; i < n; i++) {
      while (stack.isNotEmpty && nums[stack.last] >= nums[i]) {
        stack.removeLast();
      }
      left[i] = stack.isNotEmpty ? stack.last : -1;
      stack.add(i);
    }

    // Compute next smaller element indices (strictly less)
    stack.clear();
    for (int i = n - 1; i >= 0; i--) {
      while (stack.isNotEmpty && nums[stack.last] > nums[i]) {
        int idx = stack.removeLast();
        right[idx] = i;
      }
      stack.add(i);
    }

    int ans = 0;
    for (int i = 0; i < n; i++) {
      if (left[i] < k && right[i] > k) {
        int length = right[i] - left[i] - 1;
        int score = nums[i] * length;
        if (score > ans) ans = score;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func maximumScore(nums []int, k int) int {
    n := len(nums)
    left := make([]int, n)
    right := make([]int, n)

    // previous smaller element indices
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

    // next smaller element indices
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

    ans := 0
    for i := 0; i < n; i++ {
        if left[i] < k && right[i] > k {
            length := right[i] - left[i] - 1
            score := nums[i] * length
            if score > ans {
                ans = score
            }
        }
    }
    return ans
}
```

## Ruby

```ruby
def maximum_score(nums, k)
  n = nums.length
  left = Array.new(n, -1)
  right = Array.new(n, n)

  stack = []
  (0...n).each do |i|
    while !stack.empty? && nums[stack[-1]] >= nums[i]
      stack.pop
    end
    left[i] = stack.empty? ? -1 : stack[-1]
    stack << i
  end

  stack.clear
  (n - 1).downto(0) do |i|
    while !stack.empty? && nums[stack[-1]] >= nums[i]
      stack.pop
    end
    right[i] = stack.empty? ? n : stack[-1]
    stack << i
  end

  ans = 0
  (0...n).each do |i|
    if left[i] < k && right[i] > k
      length = right[i] - left[i] - 1
      score = nums[i] * length
      ans = score if score > ans
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def maximumScore(nums: Array[Int], k: Int): Int = {
        val n = nums.length
        val left = Array.fill(n)(-1)
        val right = Array.fill(n)(n)

        // previous smaller element indices
        val stack = new scala.collection.mutable.ArrayStack[Int]()
        for (i <- 0 until n) {
            while (stack.nonEmpty && nums(stack.top) >= nums(i)) {
                stack.pop()
            }
            if (stack.nonEmpty) left(i) = stack.top
            stack.push(i)
        }

        // next smaller element indices
        stack.clear()
        for (i <- (n - 1) to 0 by -1) {
            while (stack.nonEmpty && nums(stack.top) >= nums(i)) {
                stack.pop()
            }
            if (stack.nonEmpty) right(i) = stack.top
            stack.push(i)
        }

        var ans: Long = 0L
        for (i <- 0 until n) {
            if (left(i) < k && right(i) > k) {
                val len = right(i) - left(i) - 1
                val score = nums(i).toLong * len
                if (score > ans) ans = score
            }
        }

        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_score(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let k_usize = k as usize;
        // left[i]: index of first smaller element to the left, -1 if none
        let mut left = vec![-1i32; n];
        let mut stack: Vec<usize> = Vec::new();

        // Compute left using a monotonic increasing stack (process from right to left)
        for i in (0..n).rev() {
            while let Some(&top) = stack.last() {
                if nums[top] > nums[i] {
                    left[top] = i as i32;
                    stack.pop();
                } else {
                    break;
                }
            }
            stack.push(i);
        }

        // right[i]: index of first smaller element to the right, n if none
        let mut right = vec![n as i32; n];
        stack.clear();

        for i in 0..n {
            while let Some(&top) = stack.last() {
                if nums[top] > nums[i] {
                    right[top] = i as i32;
                    stack.pop();
                } else {
                    break;
                }
            }
            stack.push(i);
        }

        // Evaluate each position as the minimum of a subarray containing k
        let mut ans: i64 = 0;
        for i in 0..n {
            if left[i] < k && right[i] > k {
                let length = (right[i] - left[i] - 1) as i64;
                let score = nums[i] as i64 * length;
                if score > ans {
                    ans = score;
                }
            }
        }

        ans as i32
    }
}
```

## Racket

```racket
(define/contract (maximum-score nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((v (list->vector nums))
         (n (vector-length v))
         (left (make-vector n -1))
         (right (make-vector n n)))
    ;; compute left limits using monotonic increasing stack
    (let loop-left ((i (- n 1)) (stack '()))
      (when (>= i 0)
        (let* ((curr i)
               (new-stack
                (let rec ((stk stack))
                  (cond [(null? stk) '()]
                        [(> (vector-ref v (car stk)) (vector-ref v curr))
                         (begin
                           (vector-set! left (car stk) curr)
                           (rec (cdr stk)))]
                        [else stk]))))
          (loop-left (- i 1) (cons curr new-stack)))))
    ;; compute right limits using monotonic increasing stack
    (let loop-right ((i 0) (stack '()))
      (when (< i n)
        (let* ((curr i)
               (new-stack
                (let rec ((stk stack))
                  (cond [(null? stk) '()]
                        [(> (vector-ref v (car stk)) (vector-ref v curr))
                         (begin
                           (vector-set! right (car stk) curr)
                           (rec (cdr stk)))]
                        [else stk]))))
          (loop-right (+ i 1) (cons curr new-stack)))))
    ;; evaluate maximum score
    (let ((ans 0))
      (for ([i (in-range n)])
        (when (and (< (vector-ref left i) k)
                   (> (vector-ref right i) k))
          (let* ((len (- (vector-ref right i)
                         (vector-ref left i) 1))
                 (score (* (vector-ref v i) len)))
            (when (> score ans)
              (set! ans score)))))
      ans)))
```

## Erlang

```erlang
-module(solution).
-export([maximum_score/2]).

-spec maximum_score(Nums :: [integer()], K :: integer()) -> integer().
maximum_score(Nums, K) ->
    Tuple = list_to_tuple(Nums),
    N = tuple_size(Tuple),

    LeftArr0 = array:new(N, [{default, -1}]),
    {LeftArr, _} = left_pass(0, N, Tuple, [], LeftArr0),

    RightArr0 = array:new(N, [{default, N}]),
    {RightArr, _} = right_pass(N - 1, -1, Tuple, [], RightArr0),

    compute_ans(0, N, K, Tuple, LeftArr, RightArr, 0).

%% left pass: compute previous smaller index for each position
left_pass(Index, N, Tuple, Stack, LeftArr) when Index == N ->
    {LeftArr, Stack};
left_pass(Index, N, Tuple, Stack, LeftArr) ->
    Val = element(Index + 1, Tuple),
    NewStack = pop_greater(Stack, Val, Tuple),
    LeftIdx = case NewStack of
                  [] -> -1;
                  [Top | _] -> Top
              end,
    UpdatedLeftArr = array:set(Index, LeftIdx, LeftArr),
    left_pass(Index + 1, N, Tuple, [Index | NewStack], UpdatedLeftArr).

%% right pass: compute next smaller index for each position
right_pass(Index, _Stop, _Tuple, Stack, RightArr) when Index < 0 ->
    {RightArr, Stack};
right_pass(Index, Stop, Tuple, Stack, RightArr) ->
    Val = element(Index + 1, Tuple),
    NewStack = pop_greater(Stack, Val, Tuple),
    RightIdx = case NewStack of
                   [] -> Stop + 1; % when no smaller to the right, use N (Stop is -1)
                   [Top | _] -> Top
               end,
    UpdatedRightArr = array:set(Index, RightIdx, RightArr),
    right_pass(Index - 1, Stop, Tuple, [Index | NewStack], UpdatedRightArr).

%% pop elements from stack while they are >= current value
pop_greater([], _Val, _Tuple) ->
    [];
pop_greater([Top | Rest] = Stack, Val, Tuple) ->
    TopVal = element(Top + 1, Tuple),
    if
        TopVal >= Val -> pop_greater(Rest, Val, Tuple);
        true -> Stack
    end.

%% compute final answer using left and right arrays
compute_ans(I, N, K, Tuple, LeftArr, RightArr, Ans) when I == N ->
    Ans;
compute_ans(I, N, K, Tuple, LeftArr, RightArr, Ans) ->
    L = array:get(I, LeftArr),
    R = array:get(I, RightArr),
    NewAns =
        if
            L < K andalso R > K ->
                Len = R - L - 1,
                Score = Len * element(I + 1, Tuple),
                max(Ans, Score);
            true -> Ans
        end,
    compute_ans(I + 1, N, K, Tuple, LeftArr, RightArr, NewAns).

max(A, B) when A >= B -> A;
max(_A, B) -> B.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_score(nums :: [integer], k :: integer) :: integer
  def maximum_score(nums, k) do
    n = length(nums)
    nums_t = List.to_tuple(nums)

    left_arr = compute_left(nums_t, n)
    right_arr = compute_right(nums_t, n)

    Enum.reduce(0..(n - 1), 0, fn i, acc ->
      left_i = :array.get(i, left_arr)
      right_i = :array.get(i, right_arr)

      if left_i < k and right_i > k do
        len = right_i - left_i - 1
        score = elem(nums_t, i) * len
        max(acc, score)
      else
        acc
      end
    end)
  end

  defp compute_left(nums_t, n) do
    init_left = :array.new(n, default: -1)

    {left_arr, _stack} =
      Enum.reduce(Enum.to_list(0..(n - 1)) |> Enum.reverse(), {init_left, []}, fn i,
                                                                               {arr, stack} ->
        val_i = elem(nums_t, i)
        {arr2, stack2} = pop_left(i, val_i, nums_t, arr, stack)
        {arr2, [i | stack2]}
      end)

    left_arr
  end

  defp compute_right(nums_t, n) do
    init_right = :array.new(n, default: n)

    {right_arr, _stack} =
      Enum.reduce(0..(n - 1), {init_right, []}, fn i, {arr, stack} ->
        val_i = elem(nums_t, i)
        {arr2, stack2} = pop_right(i, val_i, nums_t, arr, stack)
        {arr2, [i | stack2]}
      end)

    right_arr
  end

  defp pop_left(_i, _val_i, _nums_t, arr, []), do: {arr, []}

  defp pop_left(i, val_i, nums_t, arr, [top | rest]) do
    if elem(nums_t, top) > val_i do
      arr2 = :array.set(top, i, arr)
      pop_left(i, val_i, nums_t, arr2, rest)
    else
      {arr, [top | rest]}
    end
  end

  defp pop_right(_i, _val_i, _nums_t, arr, []), do: {arr, []}

  defp pop_right(i, val_i, nums_t, arr, [top | rest]) do
    if elem(nums_t, top) > val_i do
      arr2 = :array.set(top, i, arr)
      pop_right(i, val_i, nums_t, arr2, rest)
    else
      {arr, [top | rest]}
    end
  end
end
```
