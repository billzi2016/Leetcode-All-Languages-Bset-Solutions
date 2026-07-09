# 3638. Maximum Balanced Shipments

## Cpp

```cpp
class Solution {
public:
    int maxBalancedShipments(vector<int>& weight) {
        int n = weight.size();
        if (n == 0) return 0;
        vector<int> best(n, 0);
        std::vector<int> st; // monotonic decreasing stack of indices
        for (int i = 0; i < n; ++i) {
            while (!st.empty() && weight[st.back()] <= weight[i]) {
                st.pop_back();
            }
            int cur = 0;
            if (!st.empty()) {
                int j = st.back();          // previous greater element
                cur = best[j] + 1;           // form a shipment ending at i
            }
            best[i] = (i > 0 ? std::max(best[i - 1], cur) : cur);
            st.push_back(i);
        }
        return best[n - 1];
    }
};
```

## Java

```java
class Solution {
    public int maxBalancedShipments(int[] weight) {
        int n = weight.length;
        int[] dp = new int[n];
        int[] best = new int[n];
        java.util.ArrayDeque<Integer> stack = new java.util.ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && weight[stack.peek()] <= weight[i]) {
                stack.pop();
            }
            int j = stack.isEmpty() ? -1 : stack.peek(); // nearest greater to the left
            if (j != -1) {
                dp[i] = (j == 0 ? 0 : best[j - 1]) + 1;
            } else {
                dp[i] = 0; // cannot form a balanced shipment ending at i
            }
            best[i] = Math.max(i > 0 ? best[i - 1] : 0, dp[i]);
            stack.push(i);
        }
        return best[n - 1];
    }
}
```

## Python

```python
class Solution(object):
    def maxBalancedShipments(self, weight):
        """
        :type weight: List[int]
        :rtype: int
        """
        n = len(weight)
        best = [0] * n  # best[i]: max shipments using prefix up to i
        stack = []  # monotonic decreasing stack of indices (weights strictly decreasing)

        for i in range(n):
            # find nearest previous greater element
            while stack and weight[stack[-1]] <= weight[i]:
                stack.pop()
            if stack:
                j = stack[-1]  # index of nearest previous greater
                prev_best = best[j - 1] if j > 0 else 0
                dp_i = prev_best + 1
                best[i] = max(best[i - 1] if i > 0 else 0, dp_i)
            else:
                # cannot end a balanced shipment at i
                best[i] = best[i - 1] if i > 0 else 0
            stack.append(i)

        return best[-1] if n else 0
```

## Python3

```python
from typing import List

class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        n = len(weight)
        best = [0] * n          # best[i]: max shipments using prefix up to i
        stack = []              # monotonic decreasing stack of indices (weights strictly decreasing)

        for i, w in enumerate(weight):
            while stack and weight[stack[-1]] <= w:
                stack.pop()
            if stack:
                j = stack[-1]
                dp_i = best[j] + 1
            else:
                dp_i = 0
            best[i] = max(best[i - 1] if i > 0 else 0, dp_i)
            stack.append(i)

        return best[-1] if n else 0
```

## C

```c
#include <stdlib.h>

int maxBalancedShipments(int* weight, int weightSize) {
    if (weightSize == 0) return 0;
    int *best = (int *)malloc(sizeof(int) * weightSize);
    int *stack = (int *)malloc(sizeof(int) * weightSize);
    int top = -1;

    for (int i = 0; i < weightSize; ++i) {
        while (top >= 0 && weight[stack[top]] <= weight[i]) {
            --top;
        }
        int j = (top >= 0) ? stack[top] : -1;
        int dp_i = 0;
        if (j != -1) {
            dp_i = best[j] + 1;
        }
        if (i == 0) {
            best[i] = dp_i;
        } else {
            best[i] = best[i - 1] > dp_i ? best[i - 1] : dp_i;
        }
        stack[++top] = i;
    }

    int ans = best[weightSize - 1];
    free(best);
    free(stack);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxBalancedShipments(int[] weight) {
        int n = weight.Length;
        int[] dp = new int[n];
        int[] best = new int[n];
        var stack = new System.Collections.Generic.Stack<int>(); // indices with decreasing weights

        for (int i = 0; i < n; i++) {
            while (stack.Count > 0 && weight[stack.Peek()] <= weight[i]) {
                stack.Pop();
            }

            int j = stack.Count > 0 ? stack.Peek() : -1;
            dp[i] = (j == -1) ? 0 : best[j] + 1;

            best[i] = i == 0 ? dp[i] : System.Math.Max(best[i - 1], dp[i]);

            stack.Push(i);
        }

        return best[n - 1];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} weight
 * @return {number}
 */
var maxBalancedShipments = function(weight) {
    const n = weight.length;
    if (n === 0) return 0;
    const best = new Array(n).fill(0);
    const stack = []; // monotonic decreasing stack of indices
    
    for (let i = 0; i < n; i++) {
        while (stack.length && weight[stack[stack.length - 1]] <= weight[i]) {
            stack.pop();
        }
        const j = stack.length ? stack[stack.length - 1] : -1;
        let dp = 0;
        if (j !== -1) {
            dp = best[j] + 1;
        }
        best[i] = i > 0 ? Math.max(best[i - 1], dp) : dp;
        stack.push(i);
    }
    
    return best[n - 1];
};
```

## Typescript

```typescript
function maxBalancedShipments(weight: number[]): number {
    const n = weight.length;
    if (n === 0) return 0;
    const best: number[] = new Array(n).fill(0);
    const stack: number[] = []; // indices with strictly decreasing weights

    for (let i = 0; i < n; i++) {
        while (stack.length && weight[stack[stack.length - 1]] <= weight[i]) {
            stack.pop();
        }

        let dp = 0;
        if (stack.length) {
            const j = stack[stack.length - 1];
            dp = best[j] + 1;
        }
        best[i] = i > 0 ? Math.max(best[i - 1], dp) : dp;

        stack.push(i);
    }

    return best[n - 1];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $weight
     * @return Integer
     */
    function maxBalancedShipments($weight) {
        $n = count($weight);
        if ($n == 0) return 0;
        $best = array_fill(0, $n, 0);
        $stack = [];

        for ($i = 0; $i < $n; ++$i) {
            while (!empty($stack) && $weight[end($stack)] <= $weight[$i]) {
                array_pop($stack);
            }

            if (empty($stack)) {
                $dp = 0;
            } else {
                $j = end($stack);          // nearest previous greater index
                $dp = $best[$j] + 1;       // form a new balanced shipment ending at i
            }

            if ($i == 0) {
                $best[$i] = $dp;
            } else {
                $best[$i] = max($best[$i - 1], $dp);
            }

            $stack[] = $i; // push current index onto monotonic stack
        }

        return $best[$n - 1];
    }
}
```

## Swift

```swift
class Solution {
    func maxBalancedShipments(_ weight: [Int]) -> Int {
        let n = weight.count
        if n == 0 { return 0 }
        var best = Array(repeating: 0, count: n)
        var stack = [Int]() // indices with decreasing weights
        
        for i in 0..<n {
            while let last = stack.last, weight[last] <= weight[i] {
                stack.removeLast()
            }
            
            var dp = 0
            if let j = stack.last {
                let prevBest = (j > 0) ? best[j - 1] : 0
                dp = prevBest + 1
            }
            
            if i == 0 {
                best[i] = dp
            } else {
                best[i] = max(best[i - 1], dp)
            }
            
            stack.append(i)
        }
        
        return best[n - 1]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxBalancedShipments(weight: IntArray): Int {
        val n = weight.size
        if (n == 0) return 0
        val best = IntArray(n)
        val stack = java.util.ArrayDeque<Int>()
        for (i in 0 until n) {
            while (!stack.isEmpty() && weight[stack.peek()] <= weight[i]) {
                stack.pop()
            }
            val j = if (stack.isEmpty()) -1 else stack.peek()
            var dp = 0
            if (j != -1) {
                val prevBest = if (j - 1 >= 0) best[j - 1] else 0
                dp = prevBest + 1
            }
            val without = if (i > 0) best[i - 1] else 0
            best[i] = kotlin.math.max(without, dp)
            stack.push(i)
        }
        return best[n - 1]
    }
}
```

## Dart

```dart
class Solution {
  int maxBalancedShipments(List<int> weight) {
    int n = weight.length;
    List<int> best = List.filled(n, 0);
    List<int> stack = [];
    for (int i = 0; i < n; i++) {
      while (stack.isNotEmpty && weight[stack.last] <= weight[i]) {
        stack.removeLast();
      }
      int dp = 0;
      if (stack.isNotEmpty) {
        int j = stack.last;
        dp = best[j] + 1;
      }
      int prevBest = i > 0 ? best[i - 1] : 0;
      best[i] = dp > prevBest ? dp : prevBest;
      stack.add(i);
    }
    return best[n - 1];
  }
}
```

## Golang

```go
func maxBalancedShipments(weight []int) int {
	n := len(weight)
	if n == 0 {
		return 0
	}
	best := make([]int, n)
	stack := make([]int, 0, n)

	for i := 0; i < n; i++ {
		for len(stack) > 0 && weight[stack[len(stack)-1]] <= weight[i] {
			stack = stack[:len(stack)-1]
		}
		cur := 0
		if len(stack) > 0 {
			j := stack[len(stack)-1]
			prevBest := 0
			if j > 0 {
				prevBest = best[j-1]
			}
			cur = prevBest + 1
		}
		if i == 0 {
			best[i] = cur
		} else if cur > best[i-1] {
			best[i] = cur
		} else {
			best[i] = best[i-1]
		}
		stack = append(stack, i)
	}
	return best[n-1]
}
```

## Ruby

```ruby
def max_balanced_shipments(weight)
  n = weight.length
  best = Array.new(n, 0)
  stack = []

  weight.each_with_index do |w, i|
    while !stack.empty? && weight[stack[-1]] <= w
      stack.pop
    end

    cur_dp = if stack.empty?
               0
             else
               j = stack[-1]
               best[j] + 1
             end

    best[i] = i.zero? ? cur_dp : [best[i - 1], cur_dp].max
    stack << i
  end

  best[n - 1]
end
```

## Scala

```scala
object Solution {
    def maxBalancedShipments(weight: Array[Int]): Int = {
        val n = weight.length
        if (n == 0) return 0
        val best = new Array[Int](n)
        val stack = new java.util.ArrayDeque[Int]()
        for (i <- 0 until n) {
            while (!stack.isEmpty && weight(stack.peekLast()) <= weight(i)) {
                stack.pollLast()
            }
            val j = if (!stack.isEmpty) stack.peekLast() else -1
            var dp = 0
            if (j != -1) {
                val prevBest = if (j - 1 >= 0) best(j - 1) else 0
                dp = prevBest + 1
            }
            val prevOverall = if (i > 0) best(i - 1) else 0
            best(i) = Math.max(prevOverall, dp)
            stack.addLast(i)
        }
        best(n - 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_balanced_shipments(weight: Vec<i32>) -> i32 {
        let n = weight.len();
        if n == 0 {
            return 0;
        }
        let mut stack: Vec<usize> = Vec::new(); // indices with decreasing weights
        let mut best: Vec<i32> = vec![0; n];
        for i in 0..n {
            while let Some(&top) = stack.last() {
                if weight[top] <= weight[i] {
                    stack.pop();
                } else {
                    break;
                }
            }
            let dp_i = if let Some(&j) = stack.last() {
                best[j] + 1
            } else {
                0
            };
            if i == 0 {
                best[i] = dp_i;
            } else {
                best[i] = std::cmp::max(best[i - 1], dp_i);
            }
            stack.push(i);
        }
        *best.last().unwrap()
    }
}
```

## Racket

```racket
(define/contract (max-balanced-shipments weight)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length weight))
         (arr (list->vector weight))
         (best (make-vector n -1000000000))
         (stack '()))
    (for ([i (in-range n)])
      (define w (vector-ref arr i))
      ;; maintain decreasing stack of indices
      (let loop ()
        (when (and (not (null? stack))
                   (<= (vector-ref arr (car stack)) w))
          (set! stack (cdr stack))
          (loop)))
      (define j (if (null? stack) -1 (car stack)))
      (define dp
        (if (= j -1)
            -1000000000
            (+ (if (= j -1) 0 (vector-ref best j)) 1)))
      (define prev-best (if (= i 0) 0 (vector-ref best (- i 1))))
      (vector-set! best i (max prev-best dp))
      (set! stack (cons i stack)))
    (if (= n 0) 0 (vector-ref best (- n 1)))))
```

## Erlang

```erlang
-module(solution).
-export([max_balanced_shipments/1]).

-spec max_balanced_shipments(Weight :: [integer()]) -> integer().
max_balanced_shipments(Weight) ->
    process(0, Weight, [], #{}, 0).

process(_Idx, [], _Stack, _BestMap, BestPrev) ->
    BestPrev;
process(Idx, [W|Tail], Stack, BestMap, BestPrev) ->
    NewStack = pop_while(Stack, W),
    J = case NewStack of
            [] -> -1;
            [{JIdx,_}|_] -> JIdx
        end,
    DP = case J of
            -1 -> 0;
            0 -> 1; % shipment from index 0 to Idx
            _ ->
                PrevBest = maps:get(J-1, BestMap),
                PrevBest + 1
         end,
    BestCurr = if BestPrev >= DP -> BestPrev; true -> DP end,
    NewBestMap = maps:put(Idx, BestCurr, BestMap),
    UpdatedStack = [{Idx,W}|NewStack],
    process(Idx+1, Tail, UpdatedStack, NewBestMap, BestCurr).

pop_while([], _W) ->
    [];
pop_while([{_,Val}=Top|Rest], W) when Val =< W ->
    pop_while(Rest, W);
pop_while(Stack, _W) ->
    Stack.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_balanced_shipments(weight :: [integer]) :: integer
  def max_balanced_shipments(weight) do
    n = length(weight)
    wt = List.to_tuple(weight)

    {_stack, best_arr, _} =
      0..(n - 1)
      |> Enum.reduce({[], :array.new(0, default: 0), 0}, fn i, {stack, best_arr, _prev_best} ->
        w = elem(wt, i)
        new_stack = pop_until_greater(stack, w, wt)

        j =
          case new_stack do
            [] -> -1
            [top | _] -> top
          end

        dp_i =
          if j == -1 do
            0
          else
            :array.get(j, best_arr) + 1
          end

        prev_best = if i == 0, do: 0, else: :array.get(i - 1, best_arr)
        best_i = max(prev_best, dp_i)

        new_best_arr = :array.set(i, best_i, best_arr)
        {[i | new_stack], new_best_arr, best_i}
      end)

    if n == 0 do
      0
    else
      :array.get(n - 1, best_arr)
    end
  end

  defp pop_until_greater([], _w, _wt), do: []

  defp pop_until_greater([h | t] = stack, w, wt) do
    if elem(wt, h) <= w do
      pop_until_greater(t, w, wt)
    else
      stack
    end
  end
end
```
