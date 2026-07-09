# 0739. Daily Temperatures

## Cpp

```cpp
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> answer(n, 0);
        std::stack<int> stk; // indices of days with unresolved warmer temperature
        for (int i = 0; i < n; ++i) {
            while (!stk.empty() && temperatures[i] > temperatures[stk.top()]) {
                int idx = stk.top();
                stk.pop();
                answer[idx] = i - idx;
            }
            stk.push(i);
        }
        return answer;
    }
};
```

## Java

```java
class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] answer = new int[n];
        java.util.ArrayDeque<Integer> stack = new java.util.ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]) {
                int idx = stack.pop();
                answer[idx] = i - idx;
            }
            stack.push(i);
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        answer = [0] * n
        stack = []  # indices with decreasing temperatures
        
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                idx = stack.pop()
                answer[idx] = i - idx
            stack.append(i)
        
        return answer
```

## Python3

```python
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []  # indices with decreasing temperatures
        
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                idx = stack.pop()
                answer[idx] = i - idx
            stack.append(i)
        
        return answer
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* dailyTemperatures(int* temperatures, int temperaturesSize, int* returnSize) {
    int *answer = (int*)malloc(sizeof(int) * temperaturesSize);
    if (!answer) {
        *returnSize = 0;
        return NULL;
    }
    for (int i = 0; i < temperaturesSize; ++i) answer[i] = 0;

    int *stack = (int*)malloc(sizeof(int) * temperaturesSize); // store indices
    int top = -1; // empty stack

    for (int i = 0; i < temperaturesSize; ++i) {
        while (top >= 0 && temperatures[i] > temperatures[stack[top]]) {
            int idx = stack[top--];
            answer[idx] = i - idx;
        }
        stack[++top] = i;
    }

    free(stack);
    *returnSize = temperaturesSize;
    return answer;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int[] DailyTemperatures(int[] temperatures) {
        int n = temperatures.Length;
        int[] answer = new int[n];
        Stack<int> stack = new Stack<int>(); // stores indices
        
        for (int i = 0; i < n; i++) {
            while (stack.Count > 0 && temperatures[i] > temperatures[stack.Peek()]) {
                int idx = stack.Pop();
                answer[idx] = i - idx;
            }
            stack.Push(i);
        }
        
        // remaining indices already have default 0
        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function(temperatures) {
    const n = temperatures.length;
    const answer = new Array(n).fill(0);
    const stack = []; // stores indices with decreasing temps
    
    for (let i = n - 1; i >= 0; i--) {
        while (stack.length && temperatures[stack[stack.length - 1]] <= temperatures[i]) {
            stack.pop();
        }
        if (stack.length) {
            answer[i] = stack[stack.length - 1] - i;
        }
        stack.push(i);
    }
    
    return answer;
};
```

## Typescript

```typescript
function dailyTemperatures(temperatures: number[]): number[] {
    const n = temperatures.length;
    const answer = new Array<number>(n).fill(0);
    const stack: number[] = []; // indices of days with decreasing temps

    for (let i = 0; i < n; i++) {
        while (stack.length && temperatures[i] > temperatures[stack[stack.length - 1]]) {
            const idx = stack.pop()!;
            answer[idx] = i - idx;
        }
        stack.push(i);
    }

    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $temperatures
     * @return Integer[]
     */
    function dailyTemperatures($temperatures) {
        $n = count($temperatures);
        $answer = array_fill(0, $n, 0);
        $stack = []; // stack of indices with decreasing temperatures

        for ($i = 0; $i < $n; $i++) {
            while (!empty($stack) && $temperatures[$i] > $temperatures[$stack[count($stack) - 1]]) {
                $prevIdx = array_pop($stack);
                $answer[$prevIdx] = $i - $prevIdx;
            }
            $stack[] = $i;
        }

        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func dailyTemperatures(_ temperatures: [Int]) -> [Int] {
        let n = temperatures.count
        var answer = Array(repeating: 0, count: n)
        var stack = [Int]() // indices with decreasing temperatures
        
        for i in 0..<n {
            while let last = stack.last, temperatures[i] > temperatures[last] {
                let idx = stack.removeLast()
                answer[idx] = i - idx
            }
            stack.append(i)
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun dailyTemperatures(temperatures: IntArray): IntArray {
        val n = temperatures.size
        val answer = IntArray(n)
        val stack = java.util.ArrayDeque<Int>()
        for (i in 0 until n) {
            while (!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]) {
                val idx = stack.pop()
                answer[idx] = i - idx
            }
            stack.push(i)
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  List<int> dailyTemperatures(List<int> temperatures) {
    int n = temperatures.length;
    List<int> answer = List.filled(n, 0);
    List<int> stack = []; // stores indices

    for (int i = 0; i < n; i++) {
      while (stack.isNotEmpty && temperatures[i] > temperatures[stack.last]) {
        int idx = stack.removeLast();
        answer[idx] = i - idx;
      }
      stack.add(i);
    }

    return answer;
  }
}
```

## Golang

```go
func dailyTemperatures(temperatures []int) []int {
	n := len(temperatures)
	ans := make([]int, n)
	stack := make([]int, 0, n) // store indices with decreasing temperatures

	for i, t := range temperatures {
		for len(stack) > 0 && t > temperatures[stack[len(stack)-1]] {
			idx := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			ans[idx] = i - idx
		}
		stack = append(stack, i)
	}
	return ans
}
```

## Ruby

```ruby
# @param {Integer[]} temperatures
# @return {Integer[]}
def daily_temperatures(temperatures)
  n = temperatures.length
  answer = Array.new(n, 0)
  stack = [] # stores indices with decreasing temps

  temperatures.each_with_index do |temp, i|
    while !stack.empty? && temp > temperatures[stack[-1]]
      idx = stack.pop
      answer[idx] = i - idx
    end
    stack << i
  end

  answer
end
```

## Scala

```scala
object Solution {
  def dailyTemperatures(temperatures: Array[Int]): Array[Int] = {
    val n = temperatures.length
    val ans = new Array[Int](n)
    val stack = new java.util.ArrayDeque[Int]()
    var i = 0
    while (i < n) {
      while (!stack.isEmpty && temperatures(i) > temperatures(stack.peek())) {
        val idx = stack.pop()
        ans(idx) = i - idx
      }
      stack.push(i)
      i += 1
    }
    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
        let n = temperatures.len();
        let mut answer = vec![0i32; n];
        let mut stack: Vec<usize> = Vec::new(); // indices with strictly higher future temps

        for i in (0..n).rev() {
            while let Some(&top) = stack.last() {
                if temperatures[top] <= temperatures[i] {
                    stack.pop();
                } else {
                    break;
                }
            }
            if let Some(&top) = stack.last() {
                answer[i] = (top - i) as i32;
            }
            stack.push(i);
        }

        answer
    }
}
```

## Racket

```racket
(define/contract (daily-temperatures temperatures)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ([temps-v (list->vector temperatures)]
         [n (vector-length temps-v)]
         [ans (make-vector n 0)]
         [stack '()]) ; stack of indices, monotonic decreasing temperatures
    (for ([i (in-range n)])
      (let ([t (vector-ref temps-v i)])
        (let recur ()
          (when (and (not (null? stack))
                     (> t (vector-ref temps-v (car stack))))
            (define idx (car stack))
            (set! stack (cdr stack))
            (vector-set! ans idx (- i idx))
            (recur)))))
      (set! stack (cons i stack)))
    (vector->list ans)))
```

## Erlang

```erlang
-export([daily_temperatures/1]).

-spec daily_temperatures([integer()]) -> [integer()].
daily_temperatures(Temperatures) ->
    Len = length(Temperatures),
    Res0 = array:new(Len, {default, 0}),
    FinalRes = process(0, Temperatures, [], Res0),
    array:to_list(FinalRes).

process(_Idx, [], _Stack, Res) -> 
    Res;
process(Idx, [Temp | Rest], Stack, Res) ->
    {NewStack, NewRes} = pop_and_set(Stack, Temp, Idx, Res),
    process(Idx + 1, Rest, [{Idx, Temp} | NewStack], NewRes).

pop_and_set([], _Temp, _CurrIdx, Res) -> 
    {[], Res};
pop_and_set([{PrevIdx, PrevTemp} = Top | Rest], Temp, CurrIdx, Res) when Temp > PrevTemp ->
    Days = CurrIdx - PrevIdx,
    NewRes = array:set(PrevIdx, Days, Res),
    pop_and_set(Rest, Temp, CurrIdx, NewRes);
pop_and_set(Stack, _Temp, _CurrIdx, Res) -> 
    {Stack, Res}.
```

## Elixir

```elixir
defmodule Solution do
  @spec daily_temperatures(temperatures :: [integer]) :: [integer]
  def daily_temperatures(temperatures) do
    temps = List.to_tuple(temperatures)
    n = tuple_size(temps)

    process(n - 1, [], [], temps)
    |> Enum.reverse()
  end

  defp process(-1, _stack, acc, _temps), do: acc

  defp process(i, stack, acc, temps) do
    cur = elem(temps, i)
    new_stack = pop(stack, cur, temps)

    days =
      case new_stack do
        [] -> 0
        [next_idx | _] -> next_idx - i
      end

    process(i - 1, [i | new_stack], [days | acc], temps)
  end

  defp pop([], _cur, _temps), do: []

  defp pop([top | rest] = stack, cur, temps) do
    if elem(temps, top) <= cur do
      pop(rest, cur, temps)
    else
      stack
    end
  end
end
```
