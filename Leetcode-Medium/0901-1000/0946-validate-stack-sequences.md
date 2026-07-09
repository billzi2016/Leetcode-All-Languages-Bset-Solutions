# 0946. Validate Stack Sequences

## Cpp

```cpp
class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        int n = pushed.size();
        vector<int> stk;
        stk.reserve(n);
        int j = 0;
        for (int x : pushed) {
            stk.push_back(x);
            while (!stk.empty() && j < n && stk.back() == popped[j]) {
                stk.pop_back();
                ++j;
            }
        }
        return j == n;
    }
};
```

## Java

```java
class Solution {
    public boolean validateStackSequences(int[] pushed, int[] popped) {
        int n = pushed.length;
        java.util.Deque<Integer> stack = new java.util.ArrayDeque<>();
        int j = 0;
        for (int x : pushed) {
            stack.push(x);
            while (!stack.isEmpty() && j < n && stack.peek() == popped[j]) {
                stack.pop();
                j++;
            }
        }
        return j == n;
    }
}
```

## Python

```python
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        j = 0
        for x in pushed:
            stack.append(x)
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
                if j == len(popped):
                    break
        return j == len(popped)
```

## Python3

```python
from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        for x in pushed:
            stack.append(x)
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
                if j == len(popped):
                    break
        return not stack
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

bool validateStackSequences(int* pushed, int pushedSize, int* popped, int poppedSize) {
    int *stack = (int *)malloc(pushedSize * sizeof(int));
    int top = -1;
    int j = 0;

    for (int i = 0; i < pushedSize; ++i) {
        stack[++top] = pushed[i];
        while (top >= 0 && j < poppedSize && stack[top] == popped[j]) {
            --top;
            ++j;
        }
    }

    free(stack);
    return j == poppedSize;
}
```

## Csharp

```csharp
public class Solution {
    public bool ValidateStackSequences(int[] pushed, int[] popped) {
        var stack = new Stack<int>();
        int j = 0;
        foreach (int x in pushed) {
            stack.Push(x);
            while (stack.Count > 0 && stack.Peek() == popped[j]) {
                stack.Pop();
                j++;
                if (j >= popped.Length) break;
            }
        }
        return stack.Count == 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} pushed
 * @param {number[]} popped
 * @return {boolean}
 */
var validateStackSequences = function(pushed, popped) {
    const stack = [];
    let j = 0;
    for (const x of pushed) {
        stack.push(x);
        while (stack.length && stack[stack.length - 1] === popped[j]) {
            stack.pop();
            j++;
        }
    }
    return j === popped.length;
};
```

## Typescript

```typescript
function validateStackSequences(pushed: number[], popped: number[]): boolean {
    const stack: number[] = [];
    let j = 0;
    for (const x of pushed) {
        stack.push(x);
        while (stack.length && stack[stack.length - 1] === popped[j]) {
            stack.pop();
            j++;
        }
    }
    return j === popped.length;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $pushed
     * @param Integer[] $popped
     * @return Boolean
     */
    function validateStackSequences($pushed, $popped) {
        $stack = [];
        $j = 0;
        $n = count($pushed);
        for ($i = 0; $i < $n; $i++) {
            $stack[] = $pushed[$i];
            while (!empty($stack) && $j < $n && $stack[count($stack) - 1] === $popped[$j]) {
                array_pop($stack);
                $j++;
            }
        }
        return $j === $n;
    }
}
```

## Swift

```swift
class Solution {
    func validateStackSequences(_ pushed: [Int], _ popped: [Int]) -> Bool {
        var stack = [Int]()
        var popIndex = 0
        for value in pushed {
            stack.append(value)
            while let top = stack.last, popIndex < popped.count && top == popped[popIndex] {
                stack.removeLast()
                popIndex += 1
            }
        }
        return popIndex == popped.count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun validateStackSequences(pushed: IntArray, popped: IntArray): Boolean {
        val stack = IntArray(pushed.size)
        var top = -1
        var j = 0
        for (x in pushed) {
            stack[++top] = x
            while (top >= 0 && j < popped.size && stack[top] == popped[j]) {
                top--
                j++
            }
        }
        return j == popped.size
    }
}
```

## Dart

```dart
class Solution {
  bool validateStackSequences(List<int> pushed, List<int> popped) {
    int n = pushed.length;
    List<int> stack = [];
    int j = 0;
    for (int x in pushed) {
      stack.add(x);
      while (stack.isNotEmpty && j < n && stack.last == popped[j]) {
        stack.removeLast();
        j++;
      }
    }
    return j == n;
  }
}
```

## Golang

```go
func validateStackSequences(pushed []int, popped []int) bool {
	stack := make([]int, 0, len(pushed))
	j := 0
	for _, x := range pushed {
		stack = append(stack, x)
		for len(stack) > 0 && j < len(popped) && stack[len(stack)-1] == popped[j] {
			stack = stack[:len(stack)-1]
			j++
		}
	}
	return j == len(popped)
}
```

## Ruby

```ruby
def validate_stack_sequences(pushed, popped)
  stack = []
  j = 0
  pushed.each do |x|
    stack << x
    while !stack.empty? && stack[-1] == popped[j]
      stack.pop
      j += 1
    end
  end
  j == popped.length
end
```

## Scala

```scala
object Solution {
    def validateStackSequences(pushed: Array[Int], popped: Array[Int]): Boolean = {
        val stack = new scala.collection.mutable.Stack[Int]()
        var j = 0
        for (x <- pushed) {
            stack.push(x)
            while (stack.nonEmpty && j < popped.length && stack.top == popped(j)) {
                stack.pop()
                j += 1
            }
        }
        stack.isEmpty
    }
}
```

## Rust

```rust
impl Solution {
    pub fn validate_stack_sequences(pushed: Vec<i32>, popped: Vec<i32>) -> bool {
        let mut stack = Vec::new();
        let mut j = 0usize;
        for &x in pushed.iter() {
            stack.push(x);
            while let Some(&top) = stack.last() {
                if j < popped.len() && top == popped[j] {
                    stack.pop();
                    j += 1;
                } else {
                    break;
                }
            }
        }
        j == popped.len()
    }
}
```

## Racket

```racket
(define/contract (validate-stack-sequences pushed popped)
  (-> (listof exact-integer?) (listof exact-integer?) boolean?)
  (let ((n (length popped)))
    (let recur ((ps pushed) (stack '()) (pop-idx 0))
      (cond
        [(null? ps)
         (let clean ((s stack) (i pop-idx))
           (if (and (not (null? s)) (< i n) (= (car s) (list-ref popped i)))
               (clean (cdr s) (+ i 1))
               (and (= i n) (null? s))))]
        [else
         (let ((new-stack (cons (car ps) stack)))
           (let inner ((s new-stack) (i pop-idx))
             (if (and (not (null? s)) (< i n) (= (car s) (list-ref popped i)))
                 (inner (cdr s) (+ i 1))
                 (recur (cdr ps) s i))))]))))
```

## Erlang

```erlang
-spec validate_stack_sequences([integer()], [integer()]) -> boolean().
validate_stack_sequences(Pushed, Popped) ->
    process(Pushed, Popped, []).

process([], PopRem, Stack) ->
    {S2, P2} = pop_while(Stack, PopRem),
    S2 == [] andalso P2 == [];
process([X|Xs], PopRem, Stack) ->
    NewStack = [X|Stack],
    {NewStack2, NewPopRem} = pop_while(NewStack, PopRem),
    process(Xs, NewPopRem, NewStack2).

pop_while(Stack, PopRem) ->
    case {Stack, PopRem} of
        {[S|Ss], [P|Ps]} when S =:= P ->
            pop_while(Ss, Ps);
        _ -> {Stack, PopRem}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec validate_stack_sequences(pushed :: [integer], popped :: [integer]) :: boolean
  def validate_stack_sequences(pushed, popped) do
    {stack, remaining} =
      Enum.reduce(pushed, {[], popped}, fn x, {stk, rem_pop} ->
        stk = [x | stk]
        pop_while_match(stk, rem_pop)
      end)

    stack == [] and remaining == []
  end

  defp pop_while_match([], pop), do: {[], pop}
  defp pop_while_match(stack, []), do: {stack, []}
  defp pop_while_match([top | rest_stack] = stack, [head | tail_pop] = pop) do
    if top == head do
      pop_while_match(rest_stack, tail_pop)
    else
      {stack, pop}
    end
  end
end
```
