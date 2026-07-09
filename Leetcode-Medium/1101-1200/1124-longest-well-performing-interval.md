# 1124. Longest Well-Performing Interval

## Cpp

```cpp
class Solution {
public:
    int longestWPI(vector<int>& hours) {
        int n = hours.size();
        vector<int> pref(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            pref[i + 1] = pref[i] + (hours[i] > 8 ? 1 : -1);
        }
        vector<int> decStack;
        for (int i = 0; i <= n; ++i) {
            if (decStack.empty() || pref[i] < pref[decStack.back()]) {
                decStack.push_back(i);
            }
        }
        int ans = 0;
        for (int j = n; j >= 0; --j) {
            while (!decStack.empty() && pref[j] > pref[decStack.back()]) {
                ans = max(ans, j - decStack.back());
                decStack.pop_back();
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int longestWPI(int[] hours) {
        int n = hours.length;
        int[] prefix = new int[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + (hours[i] > 8 ? 1 : -1);
        }
        java.util.Stack<Integer> stack = new java.util.Stack<>();
        for (int i = 0; i <= n; i++) {
            if (stack.isEmpty() || prefix[i] < prefix[stack.peek()]) {
                stack.push(i);
            }
        }
        int ans = 0;
        for (int j = n; j >= 0; j--) {
            while (!stack.isEmpty() && prefix[stack.peek()] < prefix[j]) {
                ans = Math.max(ans, j - stack.pop());
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        n = len(hours)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + (1 if hours[i] > 8 else -1)

        # Build a stack of indices with decreasing prefix sums
        dec_stack = []
        for i in range(n + 1):
            if not dec_stack or pref[i] < pref[dec_stack[-1]]:
                dec_stack.append(i)

        ans = 0
        # Traverse from the end to find longest interval
        for j in range(n, -1, -1):
            while dec_stack and pref[j] > pref[dec_stack[-1]]:
                i = dec_stack.pop()
                if j - i > ans:
                    ans = j - i
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        pref = [0] * (n + 1)
        for i, h in enumerate(hours):
            pref[i + 1] = pref[i] + (1 if h > 8 else -1)

        stack = []
        for i in range(n + 1):
            if not stack or pref[i] < pref[stack[-1]]:
                stack.append(i)

        ans = 0
        for j in range(n, -1, -1):
            while stack and pref[j] > pref[stack[-1]]:
                ans = max(ans, j - stack.pop())
        return ans
```

## C

```c
int longestWPI(int* hours, int hoursSize) {
    int n = hoursSize;
    int *pref = (int *)malloc((n + 1) * sizeof(int));
    pref[0] = 0;
    for (int i = 0; i < n; ++i) {
        pref[i + 1] = pref[i] + (hours[i] > 8 ? 1 : -1);
    }

    int *stack = (int *)malloc((n + 1) * sizeof(int));
    int top = -1;
    for (int i = 0; i <= n; ++i) {
        if (top == -1 || pref[i] < pref[stack[top]]) {
            stack[++top] = i;
        }
    }

    int ans = 0;
    for (int j = n; j >= 0; --j) {
        while (top >= 0 && pref[j] > pref[stack[top]]) {
            int len = j - stack[top];
            if (len > ans) ans = len;
            --top;
        }
    }

    free(pref);
    free(stack);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int LongestWPI(int[] hours) {
        int n = hours.Length;
        int[] prefix = new int[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + (hours[i] > 8 ? 1 : -1);
        }

        List<int> stack = new List<int>();
        for (int i = 0; i <= n; i++) {
            if (stack.Count == 0 || prefix[i] < prefix[stack[stack.Count - 1]]) {
                stack.Add(i);
            }
        }

        int ans = 0;
        for (int j = n; j >= 0; j--) {
            while (stack.Count > 0 && prefix[j] > prefix[stack[stack.Count - 1]]) {
                int iIdx = stack[stack.Count - 1];
                stack.RemoveAt(stack.Count - 1);
                ans = Math.Max(ans, j - iIdx);
            }
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} hours
 * @return {number}
 */
var longestWPI = function(hours) {
    const n = hours.length;
    const prefix = new Array(n + 1);
    prefix[0] = 0;
    for (let i = 0; i < n; ++i) {
        prefix[i + 1] = prefix[i] + (hours[i] > 8 ? 1 : -1);
    }
    
    const stack = [];
    for (let i = 0; i <= n; ++i) {
        if (stack.length === 0 || prefix[i] < prefix[stack[stack.length - 1]]) {
            stack.push(i);
        }
    }
    
    let ans = 0;
    for (let j = n; j >= 0; --j) {
        while (stack.length && prefix[j] > prefix[stack[stack.length - 1]]) {
            const i = stack.pop();
            ans = Math.max(ans, j - i);
        }
    }
    
    return ans;
};
```

## Typescript

```typescript
function longestWPI(hours: number[]): number {
    const n = hours.length;
    const pref = new Array<number>(n + 1);
    pref[0] = 0;
    for (let i = 0; i < n; i++) {
        pref[i + 1] = pref[i] + (hours[i] > 8 ? 1 : -1);
    }
    const stack: number[] = [];
    for (let i = 0; i <= n; i++) {
        if (stack.length === 0 || pref[i] < pref[stack[stack.length - 1]]) {
            stack.push(i);
        }
    }
    let ans = 0;
    for (let j = n; j >= 0; j--) {
        while (stack.length && pref[j] > pref[stack[stack.length - 1]]) {
            const i = stack.pop()!;
            ans = Math.max(ans, j - i);
        }
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $hours
     * @return Integer
     */
    function longestWPI($hours) {
        $n = count($hours);
        $pref = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            $val = $hours[$i] > 8 ? 1 : -1;
            $pref[$i + 1] = $pref[$i] + $val;
        }

        // Build a stack of indices with decreasing prefix sums
        $stack = [];
        for ($i = 0; $i <= $n; $i++) {
            if (empty($stack) || $pref[$i] < $pref[$stack[count($stack) - 1]]) {
                $stack[] = $i;
            }
        }

        $ans = 0;
        // Traverse from the end to find longest interval
        for ($j = $n; $j >= 0; $j--) {
            while (!empty($stack) && $pref[$j] > $pref[$stack[count($stack) - 1]]) {
                $iIdx = array_pop($stack);
                $ans = max($ans, $j - $iIdx);
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func longestWPI(_ hours: [Int]) -> Int {
        let n = hours.count
        var prefix = [Int](repeating: 0, count: n + 1)
        for i in 0..<n {
            prefix[i + 1] = prefix[i] + (hours[i] > 8 ? 1 : -1)
        }
        
        // Build a decreasing stack of indices
        var stack = [Int]()
        for i in 0...n {
            if stack.isEmpty || prefix[i] < prefix[stack.last!] {
                stack.append(i)
            }
        }
        
        var ans = 0
        var j = n
        while j >= 0 {
            while let last = stack.last, prefix[j] > prefix[last] {
                _ = stack.popLast()
                ans = max(ans, j - last)
            }
            j -= 1
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestWPI(hours: IntArray): Int {
        val n = hours.size
        val pref = IntArray(n + 1)
        for (i in 0 until n) {
            pref[i + 1] = pref[i] + if (hours[i] > 8) 1 else -1
        }
        val stack = java.util.ArrayDeque<Int>()
        for (i in 0..n) {
            if (stack.isEmpty() || pref[i] < pref[stack.peekLast()]) {
                stack.addLast(i)
            }
        }
        var ans = 0
        for (j in n downTo 0) {
            while (!stack.isEmpty() && pref[j] > pref[stack.peekLast()]) {
                val iIdx = stack.removeLast()
                ans = kotlin.math.max(ans, j - iIdx)
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int longestWPI(List<int> hours) {
    int n = hours.length;
    List<int> pref = List.filled(n + 1, 0);
    for (int i = 0; i < n; ++i) {
      pref[i + 1] = pref[i] + (hours[i] > 8 ? 1 : -1);
    }
    List<int> stack = [];
    for (int i = 0; i <= n; ++i) {
      if (stack.isEmpty || pref[i] < pref[stack.last]) {
        stack.add(i);
      }
    }
    int ans = 0;
    for (int j = n; j >= 0; --j) {
      while (stack.isNotEmpty && pref[j] > pref[stack.last]) {
        int length = j - stack.last;
        if (length > ans) ans = length;
        stack.removeLast();
      }
    }
    return ans;
  }
}
```

## Golang

```go
func longestWPI(hours []int) int {
    n := len(hours)
    pref := make([]int, n+1)
    for i := 0; i < n; i++ {
        if hours[i] > 8 {
            pref[i+1] = pref[i] + 1
        } else {
            pref[i+1] = pref[i] - 1
        }
    }

    // Build a decreasing stack of indices based on prefix sums
    stack := make([]int, 0)
    for i := 0; i <= n; i++ {
        if len(stack) == 0 || pref[i] < pref[stack[len(stack)-1]] {
            stack = append(stack, i)
        }
    }

    ans := 0
    // Scan from right to left to find longest well-performing interval
    for j := n; j >= 0; j-- {
        for len(stack) > 0 && pref[j] > pref[stack[len(stack)-1]] {
            if diff := j - stack[len(stack)-1]; diff > ans {
                ans = diff
            }
            stack = stack[:len(stack)-1]
        }
    }
    return ans
}
```

## Ruby

```ruby
def longest_wpi(hours)
  n = hours.length
  pref = Array.new(n + 1, 0)
  (0...n).each do |i|
    pref[i + 1] = pref[i] + (hours[i] > 8 ? 1 : -1)
  end

  stack = []
  (0..n).each do |i|
    if stack.empty? || pref[i] < pref[stack[-1]]
      stack << i
    end
  end

  ans = 0
  j = n
  while j >= 0
    while !stack.empty? && pref[j] > pref[stack[-1]]
      ans = [ans, j - stack.pop].max
    end
    j -= 1
  end

  ans
end
```

## Scala

```scala
object Solution {
    def longestWPI(hours: Array[Int]): Int = {
        val n = hours.length
        val pref = new Array[Int](n + 1)
        for (i <- 0 until n) {
            pref(i + 1) = pref(i) + (if (hours(i) > 8) 1 else -1)
        }
        // Build a decreasing stack of indices based on prefix sums
        val stack = scala.collection.mutable.ArrayBuffer[Int]()
        for (i <- 0 to n) {
            if (stack.isEmpty || pref(i) < pref(stack.last)) {
                stack.append(i)
            }
        }
        var ans = 0
        var j = n
        while (j >= 0 && stack.nonEmpty) {
            while (stack.nonEmpty && pref(j) > pref(stack.last)) {
                ans = math.max(ans, j - stack.last)
                stack.remove(stack.size - 1) // pop
            }
            j -= 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_wpi(hours: Vec<i32>) -> i32 {
        let n = hours.len();
        let mut pref = vec![0i32; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + if hours[i] > 8 { 1 } else { -1 };
        }
        // Build a decreasing stack of indices based on prefix sums
        let mut stack: Vec<usize> = Vec::new();
        for i in 0..=n {
            if stack.is_empty() || pref[i] < pref[*stack.last().unwrap()] {
                stack.push(i);
            }
        }
        let mut ans = 0i32;
        // Traverse from the end to find longest interval
        for j in (0..=n).rev() {
            while let Some(&i) = stack.last() {
                if pref[j] > pref[i] {
                    let len = (j - i) as i32;
                    if len > ans {
                        ans = len;
                    }
                    stack.pop();
                } else {
                    break;
                }
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (longest-wpi hours)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length hours))
         (hrs (list->vector hours))
         (pref (make-vector (+ n 1) 0)))
    ;; compute prefix sums where +1 for tiring day (>8), -1 otherwise
    (let loop ((i 0))
      (when (< i n)
        (define val (if (> (vector-ref hrs i) 8) 1 -1))
        (vector-set! pref (+ i 1) (+ (vector-ref pref i) val))
        (loop (+ i 1))))
    ;; build decreasing stack of indices
    (let ((stack '()))
      (for ([i (in-range 0 (+ n 1))])
        (when (or (null? stack)
                  (< (vector-ref pref i) (vector-ref pref (car stack))))
          (set! stack (cons i stack))))
      ;; scan from right to left to find longest interval
      (define ans 0)
      (let loop2 ((j n))
        (when (>= j 0)
          (let inner ()
            (when (and (not (null? stack))
                       (> (vector-ref pref j) (vector-ref pref (car stack))))
              (set! ans (max ans (- j (car stack))))
              (set! stack (cdr stack))
              (inner)))
          (loop2 (- j 1))))
      ans)))
```

## Erlang

```erlang
-spec longest_wpi(Hours :: [integer()]) -> integer().
longest_wpi(Hours) ->
    PrefList = build_prefix(Hours, 0, 0, [{0,0}]),
    Stack = build_stack(PrefList),
    RevPref = lists:reverse(PrefList),
    process_rev(RevPref, Stack, 0).

build_prefix([], _Sum, _Idx, Acc) ->
    lists:reverse(Acc);
build_prefix([H|T], Sum, Idx, Acc) ->
    Val = if H > 8 -> 1; true -> -1 end,
    NewSum = Sum + Val,
    NewIdx = Idx + 1,
    build_prefix(T, NewSum, NewIdx, [{NewIdx, NewSum}|Acc]).

build_stack(PrefList) ->
    build_stack(PrefList, []).

build_stack([], Stack) ->
    Stack;
build_stack([{Idx,Pref}=Curr|Rest], []) ->
    build_stack(Rest, [Curr]);
build_stack([{Idx,Pref}=Curr|Rest], [{_,TopPref}|_]=Stack) when Pref < TopPref ->
    build_stack(Rest, [Curr|Stack]);
build_stack([_|Rest], Stack) ->
    build_stack(Rest, Stack).

process_rev([], _Stack, Ans) ->
    Ans;
process_rev([{IdxJ,PrefJ}|Rest], Stack, Ans) ->
    {NewStack, NewAns} = pop_while(PrefJ, IdxJ, Stack, Ans),
    process_rev(Rest, NewStack, NewAns).

pop_while(_PrefJ,_IdxJ, [], Ans) ->
    {[], Ans};
pop_while(PrefJ, IdxJ, [{IdxI,PrefI}|Tail], Ans) when PrefJ > PrefI ->
    Len = IdxJ - IdxI,
    NewAns = erlang:max(Ans, Len),
    pop_while(PrefJ, IdxJ, Tail, NewAns);
pop_while(_PrefJ,_IdxJ, Stack, Ans) ->
    {Stack, Ans}.
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_wpi(hours :: [integer]) :: integer
  def longest_wpi(hours) do
    {pref_rev, _} =
      Enum.reduce(hours, {[0], 0}, fn h, {list, acc} ->
        new_acc = acc + if h > 8, do: 1, else: -1
        {[new_acc | list], new_acc}
      end)

    pref_list = Enum.reverse(pref_rev)
    pref = List.to_tuple(pref_list)
    n = tuple_size(pref) - 1

    stack =
      Enum.reduce(0..n, [], fn i, acc ->
        if acc == [] or elem(pref, i) < elem(pref, hd(acc)) do
          [i | acc]
        else
          acc
        end
      end)

    process(n, pref, stack, 0)
  end

  defp process(j, _pref, [], ans), do: ans
  defp process(j, pref, [_ | _] = stack, ans) when j < 0, do: ans

  defp process(j, pref, [i | rest] = stack, ans) do
    if elem(pref, j) > elem(pref, i) do
      new_ans = max(ans, j - i)
      process(j, pref, rest, new_ans)
    else
      process(j - 1, pref, stack, ans)
    end
  end
end
```
