# 0503. Next Greater Element II

## Cpp

```cpp
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(n, -1);
        stack<int> st; // store indices
        
        for (int i = 2 * n - 1; i >= 0; --i) {
            int idx = i % n;
            while (!st.empty() && nums[st.top()] <= nums[idx]) {
                st.pop();
            }
            if (i < n) {
                if (!st.empty()) result[idx] = nums[st.top()];
            }
            st.push(idx);
        }
        return result;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        Arrays.fill(res, -1);
        Deque<Integer> stack = new ArrayDeque<>();
        
        for (int i = 0; i < 2 * n; i++) {
            int idx = i % n;
            while (!stack.isEmpty() && nums[idx] > nums[stack.peek()]) {
                res[stack.pop()] = nums[idx];
            }
            if (i < n) {
                stack.push(idx);
            }
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []
        res = [-1] * n
        stack = []  # stores indices of elements in decreasing order

        for i in range(2 * n - 1, -1, -1):
            cur = nums[i % n]
            while stack and nums[stack[-1]] <= cur:
                stack.pop()
            if i < n:
                if stack:
                    res[i] = nums[stack[-1]]
            stack.append(i % n)

        return res
```

## Python3

```python
from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []  # indices of elements waiting for next greater
        
        for i in range(2 * n):
            cur = nums[i % n]
            while stack and cur > nums[stack[-1]]:
                idx = stack.pop()
                res[idx] = cur
            if i < n:
                stack.append(i)
        
        return res
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* nextGreaterElements(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    int* res = (int*)malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; ++i) {
        res[i] = -1;
    }
    if (numsSize == 0) {
        return res;
    }

    int* stack = (int*)malloc(numsSize * sizeof(int));
    int top = -1;

    for (int i = 0; i < 2 * numsSize; ++i) {
        int idx = i % numsSize;
        while (top >= 0 && nums[idx] > nums[stack[top]]) {
            res[stack[top]] = nums[idx];
            --top;
        }
        if (i < numsSize) {
            stack[++top] = idx;
        }
    }

    free(stack);
    return res;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[] NextGreaterElements(int[] nums) {
        int n = nums.Length;
        int[] result = new int[n];
        Array.Fill(result, -1);
        Stack<int> stack = new Stack<int>(); // stores indices

        for (int i = 2 * n - 1; i >= 0; i--) {
            int idx = i % n;
            while (stack.Count > 0 && nums[stack.Peek()] <= nums[idx]) {
                stack.Pop();
            }
            if (i < n) {
                result[idx] = stack.Count == 0 ? -1 : nums[stack.Peek()];
            }
            stack.Push(idx);
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var nextGreaterElements = function(nums) {
    const n = nums.length;
    const res = new Array(n).fill(-1);
    const stack = []; // store indices
    
    for (let i = 0; i < 2 * n; i++) {
        const idx = i % n;
        while (stack.length && nums[idx] > nums[stack[stack.length - 1]]) {
            const prevIdx = stack.pop();
            if (res[prevIdx] === -1) {
                res[prevIdx] = nums[idx];
            }
        }
        // Only push indices from the first pass to avoid duplicates
        if (i < n) {
            stack.push(idx);
        }
    }
    
    return res;
};
```

## Typescript

```typescript
function nextGreaterElements(nums: number[]): number[] {
    const n = nums.length;
    const result = new Array<number>(n).fill(-1);
    const stack: number[] = [];

    for (let i = 0; i < 2 * n; i++) {
        const idx = i % n;
        while (stack.length && nums[idx] > nums[stack[stack.length - 1]]) {
            const topIdx = stack.pop()!;
            result[topIdx] = nums[idx];
        }
        if (i < n) {
            stack.push(idx);
        }
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function nextGreaterElements($nums) {
        $n = count($nums);
        $res = array_fill(0, $n, -1);
        $stack = [];

        for ($i = 2 * $n - 1; $i >= 0; $i--) {
            $idx = $i % $n;
            while (!empty($stack) && $nums[$stack[count($stack) - 1]] <= $nums[$idx]) {
                array_pop($stack);
            }
            if ($i < $n) {
                $res[$idx] = empty($stack) ? -1 : $nums[$stack[count($stack) - 1]];
            }
            $stack[] = $idx;
        }

        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func nextGreaterElements(_ nums: [Int]) -> [Int] {
        let n = nums.count
        if n == 0 { return [] }
        var result = Array(repeating: -1, count: n)
        var stack = [Int]()
        for i in stride(from: 2 * n - 1, through: 0, by: -1) {
            let idx = i % n
            while let last = stack.last, nums[last] <= nums[idx] {
                stack.removeLast()
            }
            if let top = stack.last {
                result[idx] = nums[top]
            } else {
                result[idx] = -1
            }
            stack.append(idx)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun nextGreaterElements(nums: IntArray): IntArray {
        val n = nums.size
        val result = IntArray(n) { -1 }
        val stack = java.util.ArrayDeque<Int>()
        for (i in 0 until 2 * n) {
            val idx = i % n
            while (!stack.isEmpty() && nums[idx] > nums[stack.peekLast()]) {
                val prevIdx = stack.removeLast()
                result[prevIdx] = nums[idx]
            }
            if (i < n) {
                stack.addLast(idx)
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> nextGreaterElements(List<int> nums) {
    int n = nums.length;
    List<int> result = List.filled(n, -1);
    List<int> stack = [];

    for (int i = 0; i < 2 * n; ++i) {
      int idx = i % n;
      while (stack.isNotEmpty && nums[idx] > nums[stack.last]) {
        result[stack.removeLast()] = nums[idx];
      }
      if (i < n) {
        stack.add(idx);
      }
    }

    return result;
  }
}
```

## Golang

```go
func nextGreaterElements(nums []int) []int {
    n := len(nums)
    if n == 0 {
        return []int{}
    }
    result := make([]int, n)
    for i := range result {
        result[i] = -1
    }
    stack := make([]int, 0)

    // Traverse twice to simulate circular array
    for i := 2*n - 1; i >= 0; i-- {
        idx := i % n
        // Maintain decreasing stack
        for len(stack) > 0 && nums[stack[len(stack)-1]] <= nums[idx] {
            stack = stack[:len(stack)-1]
        }
        if i < n { // only fill result in the first pass (original indices)
            if len(stack) > 0 {
                result[idx] = nums[stack[len(stack)-1]]
            }
        }
        stack = append(stack, idx)
    }

    return result
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[]}
def next_greater_elements(nums)
  n = nums.length
  return [] if n == 0

  res = Array.new(n, -1)
  stack = []

  (2 * n - 1).downto(0) do |i|
    idx = i % n
    while !stack.empty? && nums[stack[-1]] <= nums[idx]
      stack.pop
    end
    if i < n
      res[idx] = stack.empty? ? -1 : nums[stack[-1]]
    end
    stack << idx
  end

  res
end
```

## Scala

```scala
object Solution {
    def nextGreaterElements(nums: Array[Int]): Array[Int] = {
        val n = nums.length
        if (n == 0) return Array()
        val res = Array.fill(n)(-1)
        import scala.collection.mutable.Stack
        val stack = new Stack[Int]()
        for (i <- 0 until 2 * n) {
            val idx = i % n
            while (stack.nonEmpty && nums(idx) > nums(stack.top)) {
                res(stack.pop()) = nums(idx)
            }
            if (i < n) {
                stack.push(idx)
            }
        }
        res
    }
}
```

## Rust

```rust
impl Solution {
    pub fn next_greater_elements(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        if n == 0 {
            return vec![];
        }
        let mut res = vec![-1; n];
        let mut stack: Vec<usize> = Vec::new();

        for i in 0..(2 * n) {
            let cur = nums[i % n];
            while let Some(&idx) = stack.last() {
                if cur > nums[idx] {
                    res[idx] = cur;
                    stack.pop();
                } else {
                    break;
                }
            }
            if i < n {
                stack.push(i);
            }
        }

        res
    }
}
```

## Racket

```racket
(define/contract (next-greater-elements nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ((v (list->vector nums))
         (n (vector-length v)))
    (if (= n 0)
        '()
        (let ((res (make-vector n -1))
              (stack '()))
          (for ([i (in-range (- (* 2 n) 1) -1 -1)])
            (let* ((idx (remainder i n))
                   (cur (vector-ref v idx)))
              (let loop ()
                (when (and (pair? stack)
                           (<= (vector-ref v (car stack)) cur))
                  (set! stack (cdr stack))
                  (loop)))
              (when (< i n)
                (if (null? stack)
                    (vector-set! res idx -1)
                    (vector-set! res idx (vector-ref v (car stack)))))
              (set! stack (cons idx stack))))
          (vector->list res)))))
```

## Erlang

```erlang
-module(solution).
-export([next_greater_elements/1]).

-spec next_greater_elements(Nums :: [integer()]) -> [integer()].
next_greater_elements([]) ->
    [];
next_greater_elements(Nums) ->
    N = length(Nums),
    Tuple = list_to_tuple(Nums),
    ResultMap = loop(2 * N - 1, N, Tuple, [], #{}),
    [maps:get(I, ResultMap) || I <- lists:seq(0, N - 1)].

%% Recursive traversal from right to left over two passes
-spec loop(integer(), integer(), tuple(), [integer()], map()) -> map().
loop(-1, _N, _Tuple, _Stack, ResultMap) ->
    ResultMap;
loop(I, N, Tuple, Stack, ResultMap) ->
    Idx = I rem N,
    Val = element(Idx + 1, Tuple),
    NewStack = pop_while(Stack, Val),
    UpdatedMap =
        if
            I < N ->
                Next = case NewStack of
                           [] -> -1;
                           [H | _] -> H
                       end,
                maps:put(Idx, Next, ResultMap);
            true ->
                ResultMap
        end,
    loop(I - 1, N, Tuple, [Val | NewStack], UpdatedMap).

%% Pop elements from stack while they are <= Current value
-spec pop_while([integer()], integer()) -> [integer()].
pop_while([], _Val) ->
    [];
pop_while([H | T], Val) when H =< Val ->
    pop_while(T, Val);
pop_while(Stack, _Val) ->
    Stack.
```

## Elixir

```elixir
defmodule Solution do
  @spec next_greater_elements(nums :: [integer]) :: [integer]
  def next_greater_elements(nums) do
    n = length(nums)
    arr = List.to_tuple(nums)

    {_, result} =
      Enum.reduce((2 * n - 1)..0, {[], Tuple.duplicate(-1, n)}, fn i, {stack, res} ->
        idx = rem(i, n)
        val = elem(arr, idx)

        stack = pop_while(stack, val)

        res =
          if i < n do
            next = case stack do
              [] -> -1
              [top | _] -> top
            end

            put_elem(res, idx, next)
          else
            res
          end

        {[val | stack], res}
      end)

    Tuple.to_list(result)
  end

  defp pop_while([], _val), do: []
  defp pop_while([h | t] = stack, val) when h <= val, do: pop_while(t, val)
  defp pop_while(stack, _val), do: stack
end
```
