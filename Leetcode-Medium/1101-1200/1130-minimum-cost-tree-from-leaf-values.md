# 1130. Minimum Cost Tree From Leaf Values

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int mctFromLeafValues(vector<int>& arr) {
        long long ans = 0;
        vector<int> st;
        st.push_back(INT_MAX); // sentinel
        
        for (int a : arr) {
            while (st.back() <= a) {
                int mid = st.back();
                st.pop_back();
                ans += 1LL * mid * min(st.back(), a);
            }
            st.push_back(a);
        }
        
        while (st.size() > 2) { // more than sentinel and one element
            int mid = st.back();
            st.pop_back();
            ans += 1LL * mid * st.back();
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    public int mctFromLeafValues(int[] arr) {
        java.util.Deque<Integer> stack = new java.util.ArrayDeque<>();
        stack.push(Integer.MAX_VALUE);
        int ans = 0;
        for (int a : arr) {
            while (stack.peek() <= a) {
                int mid = stack.pop();
                ans += mid * Math.min(stack.peek(), a);
            }
            stack.push(a);
        }
        while (stack.size() > 2) {
            int mid = stack.pop();
            ans += mid * stack.peek();
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        stack = [float('inf')]
        cost = 0
        for a in arr:
            while stack[-1] <= a:
                mid = stack.pop()
                cost += mid * min(stack[-1], a)
            stack.append(a)
        while len(stack) > 2:
            cost += stack.pop() * stack[-1]
        return cost
```

## Python3

```python
from typing import List

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = [float('inf')]
        cost = 0
        for a in arr:
            while stack[-1] <= a:
                mid = stack.pop()
                cost += mid * min(stack[-1], a)
            stack.append(a)
        while len(stack) > 2:
            cost += stack.pop() * stack[-1]
        return cost
```

## C

```c
#include <limits.h>

int mctFromLeafValues(int* arr, int arrSize) {
    int stack[45];
    int top = -1;
    stack[++top] = INT_MAX; // sentinel
    long long cost = 0;

    for (int i = 0; i < arrSize; ++i) {
        int cur = arr[i];
        while (stack[top] <= cur) {
            int mid = stack[top--];
            int left = stack[top];
            int minNeighbor = left < cur ? left : cur;
            cost += (long long)mid * minNeighbor;
        }
        stack[++top] = cur;
    }

    while (top > 1) { // more than sentinel and one element
        int mid = stack[top--];
        cost += (long long)mid * stack[top];
    }

    return (int)cost;
}
```

## Csharp

```csharp
public class Solution {
    public int MctFromLeafValues(int[] arr) {
        var stack = new System.Collections.Generic.List<int>();
        stack.Add(int.MaxValue); // sentinel
        int cost = 0;
        foreach (int a in arr) {
            while (stack[stack.Count - 1] <= a) {
                int mid = stack[stack.Count - 1];
                stack.RemoveAt(stack.Count - 1);
                int left = stack[stack.Count - 1];
                cost += mid * System.Math.Min(left, a);
            }
            stack.Add(a);
        }
        while (stack.Count > 2) {
            int mid = stack[stack.Count - 1];
            stack.RemoveAt(stack.Count - 1);
            int left = stack[stack.Count - 1];
            cost += mid * left;
        }
        return cost;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var mctFromLeafValues = function(arr) {
    const stack = [Infinity];
    let total = 0;
    for (const a of arr) {
        while (stack[stack.length - 1] <= a) {
            const mid = stack.pop();
            total += mid * Math.min(stack[stack.length - 1], a);
        }
        stack.push(a);
    }
    while (stack.length > 2) {
        const mid = stack.pop();
        total += mid * stack[stack.length - 1];
    }
    return total;
};
```

## Typescript

```typescript
function mctFromLeafValues(arr: number[]): number {
    const stack: number[] = [Number.MAX_SAFE_INTEGER];
    let result = 0;
    for (const x of arr) {
        while (stack[stack.length - 1] <= x) {
            const mid = stack.pop()!;
            result += mid * Math.min(stack[stack.length - 1], x);
        }
        stack.push(x);
    }
    while (stack.length > 2) {
        const mid = stack.pop()!;
        result += mid * stack[stack.length - 1];
    }
    return result;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function mctFromLeafValues($arr) {
        $stack = [PHP_INT_MAX];
        $res = 0;
        foreach ($arr as $a) {
            while (end($stack) <= $a) {
                $mid = array_pop($stack);
                $res += $mid * min(end($stack), $a);
            }
            $stack[] = $a;
        }
        while (count($stack) > 2) {
            $mid = array_pop($stack);
            $res += $mid * end($stack);
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func mctFromLeafValues(_ arr: [Int]) -> Int {
        var stack: [Int] = [Int.max]
        var result = 0
        
        for a in arr {
            while let last = stack.last, last <= a {
                let mid = stack.removeLast()
                if let top = stack.last {
                    result += mid * min(top, a)
                }
            }
            stack.append(a)
        }
        
        while stack.count > 2 {
            let mid = stack.removeLast()
            if let top = stack.last {
                result += mid * top
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun mctFromLeafValues(arr: IntArray): Int {
        val stack = java.util.ArrayDeque<Int>()
        stack.addFirst(Int.MAX_VALUE)
        var res = 0
        for (a in arr) {
            while (stack.peekFirst() <= a) {
                val mid = stack.removeFirst()
                val cost = mid * kotlin.math.min(stack.peekFirst(), a)
                res += cost
            }
            stack.addFirst(a)
        }
        while (stack.size > 2) {
            val mid = stack.removeFirst()
            res += mid * stack.peekFirst()
        }
        return res
    }
}
```

## Dart

```dart
class Solution {
  int mctFromLeafValues(List<int> arr) {
    const int INF = 1 << 30;
    List<int> stack = [INF];
    int res = 0;
    for (int a in arr) {
      while (stack.last <= a) {
        int mid = stack.removeLast();
        int cost = mid * (stack.last < a ? stack.last : a);
        res += cost;
      }
      stack.add(a);
    }
    while (stack.length > 2) {
      int mid = stack.removeLast();
      res += mid * stack.last;
    }
    return res;
  }
}
```

## Golang

```go
func mctFromLeafValues(arr []int) int {
	const INF = int(^uint(0) >> 1)
	stack := []int{INF}
	cost := 0
	for _, v := range arr {
		for stack[len(stack)-1] <= v {
			mid := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			if stack[len(stack)-1] < v {
				cost += mid * stack[len(stack)-1]
			} else {
				cost += mid * v
			}
		}
		stack = append(stack, v)
	}
	for len(stack) > 2 {
		mid := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		cost += mid * stack[len(stack)-1]
	}
	return cost
}
```

## Ruby

```ruby
def mct_from_leaf_values(arr)
  stack = [Float::INFINITY]
  cost = 0
  arr.each do |x|
    while stack[-1] <= x
      mid = stack.pop
      cost += mid * [stack[-1], x].min
    end
    stack << x
  end
  while stack.size > 2
    mid = stack.pop
    cost += mid * stack[-1]
  end
  cost
end
```

## Scala

```scala
object Solution {
  def mctFromLeafValues(arr: Array[Int]): Int = {
    import java.util.ArrayDeque
    val stack = new ArrayDeque[Int]()
    stack.push(Int.MaxValue) // sentinel
    var res = 0
    for (a <- arr) {
      while (stack.peek() <= a) {
        val mid = stack.pop()
        val cost = mid * Math.min(stack.peek(), a)
        res += cost
      }
      stack.push(a)
    }
    while (stack.size() > 2) {
      val mid = stack.pop()
      res += mid * stack.peek()
    }
    res
  }
}
```

## Rust

```rust
impl Solution {
    pub fn mct_from_leaf_values(arr: Vec<i32>) -> i32 {
        let mut stack: Vec<i32> = Vec::new();
        stack.push(i32::MAX);
        let mut total: i64 = 0;
        for &val in arr.iter() {
            while *stack.last().unwrap() <= val {
                let mid = stack.pop().unwrap();
                let cost = (mid as i64) * (std::cmp::min(*stack.last().unwrap(), val) as i64);
                total += cost;
            }
            stack.push(val);
        }
        while stack.len() > 2 {
            let mid = stack.pop().unwrap();
            let cost = (mid as i64) * (*stack.last().unwrap() as i64);
            total += cost;
        }
        total as i32
    }
}
```

## Racket

```racket
(define/contract (mct-from-leaf-values arr)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((v (list->vector arr))
         (n (vector-length v)))
    ;; precompute max for every subarray
    (define max-table (make-vector n))
    (for ([i (in-range n)])
      (let ((row (make-vector n)))
        (vector-set! max-table i row)
        (let loop ((j i) (cur (vector-ref v i)))
          (when (< j n)
            (define new-cur (max cur (vector-ref v j)))
            (vector-set! row j new-cur)
            (loop (+ j 1) new-cur)))))
    ;; dp table: dp[i][j] = minimal cost for subarray i..j
    (define dp-table (make-vector n))
    (for ([i (in-range n)])
      (let ((row (make-vector n)))
        (vector-set! dp-table i row)
        (vector-set! row i 0))) ; single leaf costs 0
    ;; fill DP for increasing lengths
    (for ([len (in-range 2 (add1 n))])
      (for ([i (in-range 0 (add1 (- n len)))])
        (define j (+ i len -1))
        (let loop ((k i) (best-so-far (arithmetic-shift 1 60)))
          (if (< k j)
              (let* ((left-max  (vector-ref (vector-ref max-table i) k))
                     (right-max (vector-ref (vector-ref max-table (+ k 1)) j))
                     (cost (+ (vector-ref (vector-ref dp-table i) k)
                              (vector-ref (vector-ref dp-table (+ k 1)) j)
                              (* left-max right-max)))
                     (new-best (if (< cost best-so-far) cost best-so-far)))
                (loop (+ k 1) new-best))
              (begin
                (vector-set! (vector-ref dp-table i) j best-so-far))))))

    (vector-ref (vector-ref dp-table 0) (- n 1))))
```

## Erlang

```erlang
-module(solution).
-export([mct_from_leaf_values/1]).

-spec mct_from_leaf_values(Arr :: [integer()]) -> integer().
mct_from_leaf_values(Arr) ->
    Inf = 1 bsl 31,
    {Stack, Cost} = process_elements(Arr, [Inf], 0),
    finalize(Stack, Cost).

process_elements([], Stack, Cost) ->
    {Stack, Cost};
process_elements([A|Rest], Stack, Cost) ->
    {NewStack, NewCost} = process_stack(A, Stack, Cost),
    UpdatedStack = [A | NewStack],
    process_elements(Rest, UpdatedStack, NewCost).

process_stack(A, [Top|Rest] = Stack, Cost) when Top =< A ->
    Next = case Rest of
        [] -> 0;
        [N|_] -> N
    end,
    NewCost = Cost + Top * erlang:min(A, Next),
    process_stack(A, Rest, NewCost);
process_stack(_A, Stack, Cost) ->
    {Stack, Cost}.

finalize([_Sentinel, _One], Cost) ->
    Cost;
finalize([Top, Next | Rest] = _Stack, Cost) when Rest =/= [] ->
    NewCost = Cost + Top * Next,
    finalize([Next | Rest], NewCost);
finalize(_, Cost) ->
    Cost.
```

## Elixir

```elixir
defmodule Solution do
  @spec mct_from_leaf_values(arr :: [integer]) :: integer
  def mct_from_leaf_values(arr) do
    sentinel = 1_000_000
    {cost, stack} =
      Enum.reduce(arr, {0, [sentinel]}, fn x, acc ->
        process_elem(x, acc)
      end)

    finalize(cost, stack)
  end

  # Process a single element x with current (cost, stack)
  defp process_elem(x, {cost, [top | rest] = stack}) when top <= x do
    mid = top
    case rest do
      [] ->
        # Should not happen because sentinel guarantees non‑empty rest
        {cost, [mid]}

      [new_top | _] ->
        add = mid * min(new_top, x)
        process_elem(x, {cost + add, rest})
    end
  end

  defp process_elem(x, {cost, stack}) do
    {cost, [x | stack]}
  end

  # Finalize remaining stack after all elements processed
  defp finalize(cost, [_sentinel] = _stack), do: cost

  defp finalize(cost, [_value, sentinel] = _stack) when sentinel != nil, do: cost

  defp finalize(cost, [a, b | rest]) do
    if rest == [] do
      # Only two elements left (a and sentinel); stop.
      cost
    else
      new_cost = cost + a * b
      finalize(new_cost, [b | rest])
    end
  end
end
```
