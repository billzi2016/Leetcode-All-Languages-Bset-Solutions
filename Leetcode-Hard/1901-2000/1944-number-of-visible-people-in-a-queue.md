# 1944. Number of Visible People in a Queue

## Cpp

```cpp
class Solution {
public:
    vector<int> canSeePersonsCount(vector<int>& heights) {
        int n = heights.size();
        vector<int> answer(n);
        std::stack<int> st; // store heights in decreasing order
        for (int i = n - 1; i >= 0; --i) {
            int cnt = 0;
            while (!st.empty() && st.top() < heights[i]) {
                ++cnt;
                st.pop();
            }
            if (!st.empty()) {
                ++cnt; // can see the first taller person
            }
            answer[i] = cnt;
            st.push(heights[i]);
        }
        return answer;
    }
};
```

## Java

```java
class Solution {
    public int[] canSeePersonsCount(int[] heights) {
        int n = heights.length;
        int[] ans = new int[n];
        java.util.ArrayDeque<Integer> stack = new java.util.ArrayDeque<>();
        for (int i = n - 1; i >= 0; --i) {
            while (!stack.isEmpty() && heights[i] > stack.peek()) {
                stack.pop();
                ans[i]++;
            }
            if (!stack.isEmpty()) {
                ans[i]++;
            }
            stack.push(heights[i]);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        n = len(heights)
        ans = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            cnt = 0
            while stack and heights[i] > stack[-1]:
                stack.pop()
                cnt += 1
            if stack:
                cnt += 1
            ans[i] = cnt
            stack.append(heights[i])
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0] * n
        stack = []  # monotonic decreasing stack of heights to the right
        for i in range(n - 1, -1, -1):
            cnt = 0
            while stack and stack[-1] < heights[i]:
                stack.pop()
                cnt += 1
            if stack:
                cnt += 1
            ans[i] = cnt
            stack.append(heights[i])
        return ans
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* canSeePersonsCount(int* heights, int heightsSize, int* returnSize) {
    *returnSize = heightsSize;
    int* ans = (int*)calloc(heightsSize, sizeof(int));
    int* stack = (int*)malloc(heightsSize * sizeof(int));
    int top = -1;  // empty stack

    for (int i = heightsSize - 1; i >= 0; --i) {
        int cnt = 0;
        while (top >= 0 && heights[i] > stack[top]) {
            ++cnt;
            --top;  // pop smaller height
        }
        if (top >= 0) {
            ++cnt;   // can see the first taller person
        }
        ans[i] = cnt;
        stack[++top] = heights[i];  // push current height
    }

    free(stack);
    return ans;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int[] CanSeePersonsCount(int[] heights) {
        int n = heights.Length;
        int[] answer = new int[n];
        Stack<int> stack = new Stack<int>();
        
        for (int i = n - 1; i >= 0; i--) {
            while (stack.Count > 0 && stack.Peek() < heights[i]) {
                stack.Pop();
                answer[i]++;
            }
            if (stack.Count > 0) {
                // can see the first taller person
                answer[i]++;
            }
            stack.Push(heights[i]);
        }
        
        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} heights
 * @return {number[]}
 */
var canSeePersonsCount = function(heights) {
    const n = heights.length;
    const ans = new Array(n).fill(0);
    const stack = []; // monotonic decreasing stack of heights
    
    for (let i = n - 1; i >= 0; --i) {
        let cnt = 0;
        while (stack.length && stack[stack.length - 1] < heights[i]) {
            stack.pop();
            cnt++;
        }
        if (stack.length) {
            // can see the first taller person
            cnt++;
        }
        ans[i] = cnt;
        stack.push(heights[i]);
    }
    
    return ans;
};
```

## Typescript

```typescript
function canSeePersonsCount(heights: number[]): number[] {
    const n = heights.length;
    const ans = new Array<number>(n).fill(0);
    const stack: number[] = []; // store heights in decreasing order

    for (let i = n - 1; i >= 0; i--) {
        let cnt = 0;
        while (stack.length && stack[stack.length - 1] < heights[i]) {
            stack.pop();
            cnt++;
        }
        if (stack.length) cnt++; // can see the next taller person
        ans[i] = cnt;
        stack.push(heights[i]);
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $heights
     * @return Integer[]
     */
    function canSeePersonsCount($heights) {
        $n = count($heights);
        $ans = array_fill(0, $n, 0);
        $stack = []; // monotonic decreasing stack of heights

        for ($i = $n - 1; $i >= 0; --$i) {
            $cnt = 0;
            while (!empty($stack) && end($stack) < $heights[$i]) {
                array_pop($stack);
                $cnt++;
            }
            if (!empty($stack)) {
                // the first taller person is also visible
                $cnt++;
            }
            $ans[$i] = $cnt;
            $stack[] = $heights[$i];
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func canSeePersonsCount(_ heights: [Int]) -> [Int] {
        let n = heights.count
        var answer = Array(repeating: 0, count: n)
        var stack = [Int]() // monotonic decreasing stack of heights
        
        for i in stride(from: n - 1, through: 0, by: -1) {
            var cnt = 0
            while let last = stack.last, heights[i] > last {
                stack.removeLast()
                cnt += 1
            }
            if !stack.isEmpty {
                cnt += 1
            }
            answer[i] = cnt
            stack.append(heights[i])
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canSeePersonsCount(heights: IntArray): IntArray {
        val n = heights.size
        val ans = IntArray(n)
        val stack = IntArray(n) // store indices of a decreasing height stack
        var top = -1
        for (i in n - 1 downTo 0) {
            var cnt = 0
            while (top >= 0 && heights[stack[top]] < heights[i]) {
                cnt++
                top--
            }
            ans[i] = if (top >= 0) cnt + 1 else cnt
            stack[++top] = i
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> canSeePersonsCount(List<int> heights) {
    int n = heights.length;
    List<int> ans = List.filled(n, 0);
    List<int> stack = [];
    for (int i = n - 1; i >= 0; --i) {
      int cnt = 0;
      while (stack.isNotEmpty && stack.last < heights[i]) {
        stack.removeLast();
        cnt++;
      }
      if (stack.isNotEmpty) cnt++;
      ans[i] = cnt;
      stack.add(heights[i]);
    }
    return ans;
  }
}
```

## Golang

```go
func canSeePersonsCount(heights []int) []int {
    n := len(heights)
    ans := make([]int, n)
    stack := make([]int, 0, n)

    for i := n - 1; i >= 0; i-- {
        cnt := 0
        for len(stack) > 0 && stack[len(stack)-1] < heights[i] {
            cnt++
            stack = stack[:len(stack)-1]
        }
        if len(stack) > 0 {
            cnt++ // can see the next taller person
        }
        ans[i] = cnt
        stack = append(stack, heights[i])
    }

    return ans
}
```

## Ruby

```ruby
def can_see_persons_count(heights)
  n = heights.length
  ans = Array.new(n, 0)
  stack = [] # monotonic decreasing stack of heights
  
  (n - 1).downto(0) do |i|
    cnt = 0
    while !stack.empty? && heights[i] > stack[-1]
      stack.pop
      cnt += 1
    end
    cnt += 1 unless stack.empty?
    ans[i] = cnt
    stack << heights[i]
  end
  
  ans
end
```

## Scala

```scala
object Solution {
    def canSeePersonsCount(heights: Array[Int]): Array[Int] = {
        val n = heights.length
        val answer = new Array[Int](n)
        val stack = new java.util.ArrayDeque[Int]()
        var i = n - 1
        while (i >= 0) {
            var cnt = 0
            while (!stack.isEmpty && stack.peek() < heights(i)) {
                stack.pop()
                cnt += 1
            }
            if (!stack.isEmpty) cnt += 1
            answer(i) = cnt
            stack.push(heights(i))
            i -= 1
        }
        answer
    }
}
```

## Rust

```rust
impl Solution {
    pub fn can_see_persons_count(heights: Vec<i32>) -> Vec<i32> {
        let n = heights.len();
        let mut answer = vec![0i32; n];
        let mut stack: Vec<i32> = Vec::new(); // monotonic decreasing stack

        for i in (0..n).rev() {
            let h = heights[i];
            let mut cnt = 0;

            while let Some(&top) = stack.last() {
                if top < h {
                    stack.pop();
                    cnt += 1;
                } else {
                    break;
                }
            }

            if !stack.is_empty() {
                // can see the first taller person
                cnt += 1;
            }

            answer[i] = cnt as i32;
            stack.push(h);
        }

        answer
    }
}
```

## Racket

```racket
(define/contract (can-see-persons-count heights)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ((n (length heights))
         (hvec (list->vector heights))
         (ans (make-vector n 0))
         (stack '())) ; monotonic decreasing stack of heights
    (for ([i (in-range (- n 1) -1 -1)]) ; iterate from right to left
      (let ((hi (vector-ref hvec i))
            (cnt 0))
        ;; pop all shorter people; each popped one is visible
        (let loop ()
          (when (and (pair? stack) (< (car stack) hi))
            (set! cnt (+ cnt 1))
            (set! stack (cdr stack))
            (loop)))
        ;; if a taller person remains, it is also visible
        (when (pair? stack)
          (set! cnt (+ cnt 1)))
        (vector-set! ans i cnt)
        ;; push current height onto the stack
        (set! stack (cons hi stack))))
    (vector->list ans)))
```

## Erlang

```erlang
-module(solution).
-export([can_see_persons_count/1]).

-spec can_see_persons_count(Heights :: [integer()]) -> [integer()].
can_see_persons_count(Heights) ->
    Rev = lists:reverse(Heights),
    {AnsRev, _Stack} = lists:foldl(
        fun(H, {Acc, Stack}) ->
            {Cnt, NewStack} = pop_smaller(H, Stack, 0),
            Count =
                case NewStack of
                    [] -> Cnt;
                    _  -> Cnt + 1
                end,
            {[Count | Acc], [H | NewStack]}
        end,
        {[], []},
        Rev),
    lists:reverse(AnsRev).

pop_smaller(_H, [], C) ->
    {C, []};
pop_smaller(H, [Top|Rest] = Stack, C) when Top < H ->
    pop_smaller(H, Rest, C + 1);
pop_smaller(_H, Stack, C) ->
    {C, Stack}.
```

## Elixir

```elixir
defmodule Solution do
  @spec can_see_persons_count(heights :: [integer]) :: [integer]
  def can_see_persons_count(heights) do
    {answers_rev, _stack} =
      Enum.reduce(Enum.with_index(Enum.reverse(heights)), {[], []}, fn {h, _rev_idx},
                                                                    {ans_acc, stack} ->
        {cnt, rest_stack} = pop_smaller(h, stack, 0)
        visible = if rest_stack != [], do: 1, else: 0
        total = cnt + visible
        {[total | ans_acc], [h | rest_stack]}
      end)

    Enum.reverse(answers_rev)
  end

  defp pop_smaller(_h, [], cnt), do: {cnt, []}
  defp pop_smaller(h, [top | tail] = stack, cnt) when top < h,
    do: pop_smaller(h, tail, cnt + 1)

  defp pop_smaller(_h, stack, cnt), do: {cnt, stack}
end
```
