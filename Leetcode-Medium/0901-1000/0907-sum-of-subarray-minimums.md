# 0907. Sum of Subarray Minimums

## Cpp

```cpp
class Solution {
public:
    int sumSubarrayMins(vector<int>& arr) {
        const int MOD = 1'000'000'007;
        int n = arr.size();
        vector<int> ple(n), nle(n);
        stack<int> st;
        // previous less element (strictly less)
        for (int i = 0; i < n; ++i) {
            while (!st.empty() && arr[st.top()] > arr[i]) st.pop();
            ple[i] = st.empty() ? -1 : st.top();
            st.push(i);
        }
        while (!st.empty()) st.pop();
        // next less or equal element
        for (int i = n - 1; i >= 0; --i) {
            while (!st.empty() && arr[st.top()] >= arr[i]) st.pop();
            nle[i] = st.empty() ? n : st.top();
            st.push(i);
        }
        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            long long left = i - ple[i];
            long long right = nle[i] - i;
            ans = (ans + (long long)arr[i] * left % MOD * right) % MOD;
        }
        return (int)ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int sumSubarrayMins(int[] arr) {
        int n = arr.length;
        int MOD = 1_000_000_007;
        int[] left = new int[n];
        int[] right = new int[n];
        Deque<Integer> stack = new ArrayDeque<>();

        // previous less element (strictly less)
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && arr[stack.peek()] > arr[i]) {
                stack.pop();
            }
            int prev = stack.isEmpty() ? -1 : stack.peek();
            left[i] = i - prev;
            stack.push(i);
        }

        stack.clear();

        // next less-or-equal element
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && arr[stack.peek()] >= arr[i]) {
                stack.pop();
            }
            int nxt = stack.isEmpty() ? n : stack.peek();
            right[i] = nxt - i;
            stack.push(i);
        }

        long ans = 0;
        for (int i = 0; i < n; i++) {
            long contrib = ((long) arr[i] * left[i]) % MOD;
            contrib = (contrib * right[i]) % MOD;
            ans = (ans + contrib) % MOD;
        }
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(arr)
        left = [0] * n
        right = [0] * n

        # distance to previous less element (strictly less)
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if not stack:
                left[i] = i + 1
            else:
                left[i] = i - stack[-1]
            stack.append(i)

        # distance to next less-or-equal element
        stack.clear()
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if not stack:
                right[i] = n - i
            else:
                right[i] = stack[-1] - i
            stack.append(i)

        ans = 0
        for i in range(n):
            ans = (ans + arr[i] * left[i] * right[i]) % MOD
        return ans
```

## Python3

```python
class Solution:
    def sumSubarrayMins(self, arr):
        MOD = 10**9 + 7
        n = len(arr)
        left = [0] * n
        right = [0] * n

        # previous less element (strictly less)
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            prev = stack[-1] if stack else -1
            left[i] = i - prev
            stack.append(i)

        # next less-or-equal element
        stack.clear()
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            nxt = stack[-1] if stack else n
            right[i] = nxt - i
            stack.append(i)

        ans = 0
        for i in range(n):
            ans = (ans + arr[i] * left[i] * right[i]) % MOD
        return ans
```

## C

```c
int sumSubarrayMins(int* arr, int arrSize) {
    const int MOD = 1000000007;
    int *ple = (int*)malloc(arrSize * sizeof(int));
    int *nle = (int*)malloc(arrSize * sizeof(int));
    int *stack = (int*)malloc(arrSize * sizeof(int));
    int top = -1;

    // previous less element (strict)
    for (int i = 0; i < arrSize; ++i) {
        while (top >= 0 && arr[stack[top]] >= arr[i]) {
            --top;
        }
        ple[i] = (top == -1) ? -1 : stack[top];
        stack[++top] = i;
    }

    // next less-or-equal element
    top = -1;
    for (int i = arrSize - 1; i >= 0; --i) {
        while (top >= 0 && arr[stack[top]] > arr[i]) {
            --top;
        }
        nle[i] = (top == -1) ? arrSize : stack[top];
        stack[++top] = i;
    }

    long long ans = 0;
    for (int i = 0; i < arrSize; ++i) {
        long long left = i - ple[i];
        long long right = nle[i] - i;
        long long contrib = (left * right) % MOD;
        contrib = (contrib * arr[i]) % MOD;
        ans += contrib;
        if (ans >= MOD) ans -= MOD;
    }

    free(ple);
    free(nle);
    free(stack);
    return (int)(ans % MOD);
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int SumSubarrayMins(int[] arr) {
        const int MOD = 1000000007;
        int n = arr.Length;
        long[] left = new long[n];
        long[] right = new long[n];
        var stack = new Stack<int>();

        // distance to previous less element (strict)
        for (int i = 0; i < n; i++) {
            while (stack.Count > 0 && arr[stack.Peek()] > arr[i]) {
                stack.Pop();
            }
            left[i] = stack.Count == 0 ? i + 1 : i - stack.Peek();
            stack.Push(i);
        }

        stack.Clear();

        // distance to next less-or-equal element
        for (int i = n - 1; i >= 0; i--) {
            while (stack.Count > 0 && arr[stack.Peek()] >= arr[i]) {
                stack.Pop();
            }
            right[i] = stack.Count == 0 ? n - i : stack.Peek() - i;
            stack.Push(i);
        }

        long ans = 0;
        for (int i = 0; i < n; i++) {
            long contrib = ((long)arr[i] * left[i]) % MOD;
            contrib = (contrib * right[i]) % MOD;
            ans = (ans + contrib) % MOD;
        }

        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var sumSubarrayMins = function(arr) {
    const MOD = 1e9 + 7;
    const n = arr.length;
    const left = new Array(n);
    const right = new Array(n);
    let stack = [];

    // distance to previous less element (strict)
    for (let i = 0; i < n; i++) {
        while (stack.length && arr[stack[stack.length - 1]] > arr[i]) {
            stack.pop();
        }
        const prev = stack.length ? stack[stack.length - 1] : -1;
        left[i] = i - prev;
        stack.push(i);
    }

    // distance to next less-or-equal element
    stack = [];
    for (let i = n - 1; i >= 0; i--) {
        while (stack.length && arr[stack[stack.length - 1]] >= arr[i]) {
            stack.pop();
        }
        const nxt = stack.length ? stack[stack.length - 1] : n;
        right[i] = nxt - i;
        stack.push(i);
    }

    let ans = 0;
    for (let i = 0; i < n; i++) {
        ans = (ans + arr[i] * left[i] % MOD * right[i]) % MOD;
    }
    return ans;
};
```

## Typescript

```typescript
function sumSubarrayMins(arr: number[]): number {
    const n = arr.length;
    const MOD = 1_000_000_007;
    const left = new Array<number>(n);
    const right = new Array<number>(n);
    const stack: number[] = [];

    // distance to previous less element (strict)
    for (let i = 0; i < n; i++) {
        while (stack.length && arr[stack[stack.length - 1]] > arr[i]) {
            stack.pop();
        }
        const prev = stack.length ? stack[stack.length - 1] : -1;
        left[i] = i - prev;
        stack.push(i);
    }

    // distance to next less-or-equal element
    stack.length = 0;
    for (let i = n - 1; i >= 0; i--) {
        while (stack.length && arr[stack[stack.length - 1]] >= arr[i]) {
            stack.pop();
        }
        const nxt = stack.length ? stack[stack.length - 1] : n;
        right[i] = nxt - i;
        stack.push(i);
    }

    let ans = 0;
    for (let i = 0; i < n; i++) {
        const contrib = ((arr[i] * left[i]) % MOD) * right[i] % MOD;
        ans = (ans + contrib) % MOD;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function sumSubarrayMins($arr) {
        $mod = 1000000007;
        $n = count($arr);
        $left = array_fill(0, $n, 0);
        $right = array_fill(0, $n, 0);
        $stack = [];

        // previous less (strict)
        for ($i = 0; $i < $n; $i++) {
            while (!empty($stack) && $arr[end($stack)] > $arr[$i]) {
                array_pop($stack);
            }
            $prev = empty($stack) ? -1 : end($stack);
            $left[$i] = $i - $prev;
            $stack[] = $i;
        }

        // next less-or-equal
        $stack = [];
        for ($i = $n - 1; $i >= 0; $i--) {
            while (!empty($stack) && $arr[end($stack)] >= $arr[$i]) {
                array_pop($stack);
            }
            $next = empty($stack) ? $n : end($stack);
            $right[$i] = $next - $i;
            $stack[] = $i;
        }

        $result = 0;
        for ($i = 0; $i < $n; $i++) {
            $contrib = ($arr[$i] * $left[$i]) % $mod;
            $contrib = ($contrib * $right[$i]) % $mod;
            $result = ($result + $contrib) % $mod;
        }

        return (int)$result;
    }
}
```

## Swift

```swift
class Solution {
    func sumSubarrayMins(_ arr: [Int]) -> Int {
        let n = arr.count
        let MOD: Int64 = 1_000_000_007
        var left = Array(repeating: 0, count: n)
        var right = Array(repeating: 0, count: n)
        var stack = [Int]()
        
        // Compute distances to previous less element (strictly less)
        for i in 0..<n {
            while let last = stack.last, arr[last] > arr[i] {
                stack.removeLast()
            }
            let prevLess = stack.last ?? -1
            left[i] = i - prevLess
            stack.append(i)
        }
        
        stack.removeAll()
        // Compute distances to next less-or-equal element
        for i in stride(from: n - 1, through: 0, by: -1) {
            while let last = stack.last, arr[last] >= arr[i] {
                stack.removeLast()
            }
            let nextLess = stack.last ?? n
            right[i] = nextLess - i
            stack.append(i)
        }
        
        var result: Int64 = 0
        for i in 0..<n {
            let contrib = (Int64(arr[i]) * Int64(left[i]) % MOD) * Int64(right[i]) % MOD
            result = (result + contrib) % MOD
        }
        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sumSubarrayMins(arr: IntArray): Int {
        val n = arr.size
        val left = IntArray(n)
        val right = IntArray(n)
        val stack = java.util.ArrayDeque<Int>()

        // previous less (strict)
        for (i in 0 until n) {
            while (!stack.isEmpty() && arr[stack.peek()] >= arr[i]) {
                stack.pop()
            }
            left[i] = i - if (stack.isEmpty()) -1 else stack.peek()
            stack.push(i)
        }

        stack.clear()

        // next less-or-equal
        for (i in n - 1 downTo 0) {
            while (!stack.isEmpty() && arr[stack.peek()] > arr[i]) {
                stack.pop()
            }
            right[i] = if (stack.isEmpty()) n else stack.peek()
            right[i] -= i
            stack.push(i)
        }

        val MOD = 1_000_000_007L
        var ans = 0L
        for (i in 0 until n) {
            val contrib = arr[i].toLong() * left[i].toLong() % MOD * right[i].toLong() % MOD
            ans += contrib
            if (ans >= MOD) ans -= MOD
        }
        return (ans % MOD).toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int sumSubarrayMins(List<int> arr) {
    final n = arr.length;
    final left = List.filled(n, 0);
    final right = List.filled(n, 0);
    final stack = <int>[];

    // distances to previous less element (strict)
    for (var i = 0; i < n; i++) {
      while (stack.isNotEmpty && arr[stack.last] >= arr[i]) {
        stack.removeLast();
      }
      final prev = stack.isEmpty ? -1 : stack.last;
      left[i] = i - prev;
      stack.add(i);
    }

    // distances to next less-or-equal element
    stack.clear();
    for (var i = n - 1; i >= 0; i--) {
      while (stack.isNotEmpty && arr[stack.last] > arr[i]) {
        stack.removeLast();
      }
      final nxt = stack.isEmpty ? n : stack.last;
      right[i] = nxt - i;
      stack.add(i);
    }

    var ans = 0;
    for (var i = 0; i < n; i++) {
      final contrib = ((arr[i] * left[i]) % _mod) * right[i] % _mod;
      ans += contrib;
      if (ans >= _mod) ans -= _mod;
    }
    return ans;
  }
}
```

## Golang

```go
func sumSubarrayMins(arr []int) int {
	const mod = 1000000007
	n := len(arr)
	left := make([]int, n)
	right := make([]int, n)

	// previous less element (strictly less)
	stack := make([]int, 0, n)
	for i := 0; i < n; i++ {
		for len(stack) > 0 && arr[stack[len(stack)-1]] > arr[i] {
			stack = stack[:len(stack)-1]
		}
		if len(stack) == 0 {
			left[i] = i + 1
		} else {
			left[i] = i - stack[len(stack)-1]
		}
		stack = append(stack, i)
	}

	// next less-or-equal element
	stack = stack[:0]
	for i := n - 1; i >= 0; i-- {
		for len(stack) > 0 && arr[stack[len(stack)-1]] >= arr[i] {
			stack = stack[:len(stack)-1]
		}
		if len(stack) == 0 {
			right[i] = n - i
		} else {
			right[i] = stack[len(stack)-1] - i
		}
		stack = append(stack, i)
	}

	var result int64 = 0
	for i := 0; i < n; i++ {
		contrib := (int64(arr[i]) * int64(left[i]) % mod) * int64(right[i]) % mod
		result += contrib
		if result >= mod {
			result -= mod
		}
	}
	return int(result % mod)
}
```

## Ruby

```ruby
def sum_subarray_mins(arr)
  mod = 1_000_000_007
  n = arr.length
  left = Array.new(n)
  right = Array.new(n)

  stack = []
  arr.each_with_index do |val, i|
    while !stack.empty? && arr[stack[-1]] > val
      stack.pop
    end
    left[i] = stack.empty? ? i + 1 : i - stack[-1]
    stack << i
  end

  stack.clear
  (n - 1).downto(0) do |i|
    val = arr[i]
    while !stack.empty? && arr[stack[-1]] >= val
      stack.pop
    end
    right[i] = stack.empty? ? n - i : stack[-1] - i
    stack << i
  end

  ans = 0
  n.times do |i|
    ans = (ans + arr[i] * left[i] % mod * right[i]) % mod
  end
  ans
end
```

## Scala

```scala
object Solution {
    def sumSubarrayMins(arr: Array[Int]): Int = {
        val MOD = 1000000007L
        val n = arr.length
        val left = new Array[Long](n)
        val right = new Array[Long](n)

        // previous less element (strictly)
        val stackPrev = new java.util.ArrayDeque[Int]()
        for (i <- 0 until n) {
            while (!stackPrev.isEmpty && arr(stackPrev.peek()) >= arr(i)) {
                stackPrev.pop()
            }
            val prev = if (stackPrev.isEmpty) -1 else stackPrev.peek()
            left(i) = (i - prev).toLong
            stackPrev.push(i)
        }

        // next less-or-equal element
        val stackNext = new java.util.ArrayDeque[Int]()
        for (i <- 0 until n) {
            while (!stackNext.isEmpty && arr(i) <= arr(stackNext.peek())) {
                val idx = stackNext.pop()
                right(idx) = (i - idx).toLong
            }
            stackNext.push(i)
        }
        while (!stackNext.isEmpty) {
            val idx = stackNext.pop()
            right(idx) = (n - idx).toLong
        }

        var ans = 0L
        for (i <- 0 until n) {
            ans = (ans + arr(i).toLong * left(i) % MOD * right(i) % MOD) % MOD
        }
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sum_subarray_mins(arr: Vec<i32>) -> i32 {
        let n = arr.len();
        let mut left = vec![0i64; n];
        let mut right = vec![0i64; n];
        let mut stack: Vec<usize> = Vec::new();

        // previous less (strict)
        for i in 0..n {
            while let Some(&idx) = stack.last() {
                if arr[idx] > arr[i] {
                    stack.pop();
                } else {
                    break;
                }
            }
            let prev = if let Some(&idx) = stack.last() { idx as i64 } else { -1 };
            left[i] = i as i64 - prev;
            stack.push(i);
        }

        stack.clear();

        // next less or equal
        for i in (0..n).rev() {
            while let Some(&idx) = stack.last() {
                if arr[idx] >= arr[i] {
                    stack.pop();
                } else {
                    break;
                }
            }
            let next = if let Some(&idx) = stack.last() { idx as i64 } else { n as i64 };
            right[i] = next - i as i64;
            stack.push(i);
        }

        const MOD: i64 = 1_000_000_007;
        let mut ans: i64 = 0;
        for i in 0..n {
            let val = arr[i] as i64 % MOD;
            let contrib = (val * left[i] % MOD) * right[i] % MOD;
            ans = (ans + contrib) % MOD;
        }
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (sum-subarray-mins arr)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((mod 1000000007)
         (v   (list->vector arr))
         (n   (vector-length v))
         (left  (make-vector n))
         (right (make-vector n))
         (stack '()))
    ;; distances to previous less element (strict)
    (for ([i (in-range n)])
      (let loop ()
        (when (and (not (null? stack))
                   (> (vector-ref v (car stack)) (vector-ref v i)))
          (set! stack (cdr stack))
          (loop)))
      (if (null? stack)
          (vector-set! left i (+ i 1))
          (vector-set! left i (- i (car stack))))
      (set! stack (cons i stack)))
    ;; distances to next less-or-equal element
    (set! stack '())
    (for ([i (in-range (sub1 n) -1 -1)])
      (let loop ()
        (when (and (not (null? stack))
                   (>= (vector-ref v (car stack)) (vector-ref v i)))
          (set! stack (cdr stack))
          (loop)))
      (if (null? stack)
          (vector-set! right i (- n i))
          (vector-set! right i (- (car stack) i)))
      (set! stack (cons i stack)))
    ;; accumulate answer
    (let ((ans 0))
      (for ([i (in-range n)])
        (set! ans (modulo (+ ans (* (vector-ref v i)
                                    (vector-ref left i)
                                    (vector-ref right i))) mod)))
      ans)))
```

## Erlang

```erlang
-define(MOD, 1000000007).

-export([sum_subarray_mins/1]).

-spec sum_subarray_mins(Arr :: [integer()]) -> integer().
sum_subarray_mins(Arr) ->
    N = length(Arr),
    Indexed = lists:zip(lists:seq(0, N - 1), Arr),
    LeftDist = left_dist(Indexed, [], []),
    RevIndexed = lists:reverse(Indexed),
    RightDistRev = right_dist_rev(RevIndexed, [], N, []),
    RightDist = lists:reverse(RightDistRev),
    compute_sum(Arr, LeftDist, RightDist).

left_dist([], _Stack, Acc) ->
    lists:reverse(Acc);
left_dist([{I, V} | Rest], Stack, Acc) ->
    NewStack = pop_while_gte(Stack, V),
    PrevIdx = case NewStack of
        [] -> -1;
        [{_, PrevI} | _] -> PrevI
    end,
    Dist = I - PrevIdx,
    left_dist(Rest, [{V, I} | NewStack], [Dist | Acc]).

pop_while_gte([], _V) ->
    [];
pop_while_gte([{TopV, _} = Top | Rest], V) when TopV >= V ->
    pop_while_gte(Rest, V);
pop_while_gte(Stack, _V) ->
    Stack.

right_dist_rev([], _Stack, _N, Acc) ->
    Acc;
right_dist_rev([{I, V} | Rest], Stack, N, Acc) ->
    NewStack = pop_while_gt(Stack, V),
    NextIdx = case NewStack of
        [] -> N;
        [{_, NextI} | _] -> NextI
    end,
    Dist = NextIdx - I,
    right_dist_rev(Rest, [{V, I} | NewStack], N, [Dist | Acc]).

pop_while_gt([], _V) ->
    [];
pop_while_gt([{TopV, _} = Top | Rest], V) when TopV > V ->
    pop_while_gt(Rest, V);
pop_while_gt(Stack, _V) ->
    Stack.

compute_sum(Arr, Left, Right) ->
    lists:foldl(
        fun({Val, L, R}, Acc) ->
            Contribution = ((Val rem ?MOD) * (L rem ?MOD) rem ?MOD) *
                           (R rem ?MOD) rem ?MOD,
            (Acc + Contribution) rem ?MOD
        end,
        0,
        lists:zip3(Arr, Left, Right)
    ).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @spec sum_subarray_mins(arr :: [integer]) :: integer
  def sum_subarray_mins(arr) do
    mod = 1_000_000_007
    n = length(arr)
    arr_arr = :array.from_list(arr)

    left = compute_left(0, n, arr_arr, :array.new(n, default: 0), [])
    right = compute_right(n - 1, n, arr_arr, :array.new(n, default: 0), [])

    Enum.reduce(0..n - 1, 0, fn i, acc ->
      l = :array.get(i, left)
      r = :array.get(i, right)
      v = :array.get(i, arr_arr)
      contrib = rem(v * l * r, mod)
      rem(acc + contrib, mod)
    end)
  end

  defp compute_left(i, n, arr_arr, left, stack) when i < n do
    val = :array.get(i, arr_arr)

    new_stack = trim_stack(stack, arr_arr, val, fn a, b -> a > b end)

    prev_idx =
      case new_stack do
        [] -> -1
        [top | _] -> top
      end

    dist = i - prev_idx
    left2 = :array.set(i, dist, left)
    compute_left(i + 1, n, arr_arr, left2, [i | new_stack])
  end

  defp compute_left(_, _, _, left, _), do: left

  defp compute_right(i, n, arr_arr, right, stack) when i >= 0 do
    val = :array.get(i, arr_arr)

    new_stack = trim_stack(stack, arr_arr, val, fn a, b -> a >= b end)

    next_idx =
      case new_stack do
        [] -> n
        [top | _] -> top
      end

    dist = next_idx - i
    right2 = :array.set(i, dist, right)
    compute_right(i - 1, n, arr_arr, right2, [i | new_stack])
  end

  defp compute_right(_, _, _, right, _), do: right

  defp trim_stack([], _arr_arr, _val, _comp), do: []

  defp trim_stack([top | rest] = stack, arr_arr, val, comp) do
    top_val = :array.get(top, arr_arr)

    if comp.(top_val, val) do
      trim_stack(rest, arr_arr, val, comp)
    else
      stack
    end
  end
end
```
