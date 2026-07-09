# 0962. Maximum Width Ramp

## Cpp

```cpp
class Solution {
public:
    int maxWidthRamp(std::vector<int>& nums) {
        int n = nums.size();
        std::vector<int> st; // decreasing stack of indices
        for (int i = 0; i < n; ++i) {
            if (st.empty() || nums[i] < nums[st.back()]) {
                st.push_back(i);
            }
        }
        int ans = 0;
        for (int j = n - 1; j >= 0; --j) {
            while (!st.empty() && nums[st.back()] <= nums[j]) {
                ans = std::max(ans, j - st.back());
                st.pop_back();
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxWidthRamp(int[] nums) {
        int n = nums.length;
        java.util.Deque<Integer> stack = new java.util.ArrayDeque<>();
        // Build a decreasing stack of indices
        for (int i = 0; i < n; i++) {
            if (stack.isEmpty() || nums[i] < nums[stack.peek()]) {
                stack.push(i);
            }
        }
        int maxWidth = 0;
        // Scan from the right, trying to pop valid starts
        for (int j = n - 1; j >= 0; j--) {
            while (!stack.isEmpty() && nums[j] >= nums[stack.peek()]) {
                int i = stack.pop();
                maxWidth = Math.max(maxWidth, j - i);
            }
        }
        return maxWidth;
    }
}
```

## Python

```python
class Solution(object):
    def maxWidthRamp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        stack = []
        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)

        ans = 0
        for j in range(n - 1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                ans = max(ans, j - stack.pop())
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        for i, v in enumerate(nums):
            if not stack or v < nums[stack[-1]]:
                stack.append(i)
        ans = 0
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                ans = max(ans, j - stack[-1])
                stack.pop()
        return ans
```

## C

```c
#include <stdlib.h>

int maxWidthRamp(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    int *stack = (int *)malloc(numsSize * sizeof(int));
    int top = -1;

    // Build decreasing stack of indices
    for (int i = 0; i < numsSize; ++i) {
        if (top == -1 || nums[i] < nums[stack[top]]) {
            stack[++top] = i;
        }
    }

    int maxWidth = 0;
    // Scan from right to left
    for (int j = numsSize - 1; j >= 0; --j) {
        while (top >= 0 && nums[j] >= nums[stack[top]]) {
            int width = j - stack[top];
            if (width > maxWidth) maxWidth = width;
            top--;
        }
    }

    free(stack);
    return maxWidth;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxWidthRamp(int[] nums) {
        int n = nums.Length;
        var stack = new System.Collections.Generic.Stack<int>();
        for (int i = 0; i < n; i++) {
            if (stack.Count == 0 || nums[i] < nums[stack.Peek()]) {
                stack.Push(i);
            }
        }

        int maxWidth = 0;
        for (int j = n - 1; j >= 0; j--) {
            while (stack.Count > 0 && nums[j] >= nums[stack.Peek()]) {
                int iIdx = stack.Pop();
                int width = j - iIdx;
                if (width > maxWidth) maxWidth = width;
            }
        }

        return maxWidth;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxWidthRamp = function(nums) {
    const n = nums.length;
    const stack = [];
    // Build a decreasing stack of candidate left indices
    for (let i = 0; i < n; i++) {
        if (stack.length === 0 || nums[i] < nums[stack[stack.length - 1]]) {
            stack.push(i);
        }
    }
    let maxWidth = 0;
    // Scan from right to left, trying to pop valid ramps
    for (let j = n - 1; j >= 0; j--) {
        while (stack.length && nums[j] >= nums[stack[stack.length - 1]]) {
            const iIdx = stack.pop();
            const width = j - iIdx;
            if (width > maxWidth) maxWidth = width;
        }
    }
    return maxWidth;
};
```

## Typescript

```typescript
function maxWidthRamp(nums: number[]): number {
    const n = nums.length;
    const stack: number[] = [];
    for (let i = 0; i < n; i++) {
        if (stack.length === 0 || nums[i] < nums[stack[stack.length - 1]]) {
            stack.push(i);
        }
    }
    let maxWidth = 0;
    for (let j = n - 1; j >= 0; j--) {
        while (stack.length && nums[j] >= nums[stack[stack.length - 1]]) {
            const i = stack.pop()!;
            if (j - i > maxWidth) maxWidth = j - i;
        }
    }
    return maxWidth;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxWidthRamp($nums) {
        $n = count($nums);
        $stack = [];

        // Build decreasing stack of indices
        for ($i = 0; $i < $n; $i++) {
            if (empty($stack) || $nums[$i] < $nums[$stack[count($stack) - 1]]) {
                $stack[] = $i;
            }
        }

        $maxWidth = 0;

        // Scan from right to left, trying to pop valid ramps
        for ($j = $n - 1; $j >= 0; $j--) {
            while (!empty($stack) && $nums[$j] >= $nums[$stack[count($stack) - 1]]) {
                $iIdx = array_pop($stack);
                $width = $j - $iIdx;
                if ($width > $maxWidth) {
                    $maxWidth = $width;
                }
            }
        }

        return $maxWidth;
    }
}
```

## Swift

```swift
class Solution {
    func maxWidthRamp(_ nums: [Int]) -> Int {
        var stack = [Int]()
        for i in 0..<nums.count {
            if stack.isEmpty || nums[i] < nums[stack.last!] {
                stack.append(i)
            }
        }
        var ans = 0
        for j in stride(from: nums.count - 1, through: 0, by: -1) {
            while let last = stack.last, nums[j] >= nums[last] {
                ans = max(ans, j - last)
                stack.removeLast()
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxWidthRamp(nums: IntArray): Int {
        val n = nums.size
        val stack = mutableListOf<Int>()
        for (i in 0 until n) {
            if (stack.isEmpty() || nums[i] < nums[stack.last()]) {
                stack.add(i)
            }
        }
        var ans = 0
        for (j in n - 1 downTo 0) {
            while (stack.isNotEmpty() && nums[j] >= nums[stack.last()]) {
                val iIdx = stack.removeAt(stack.size - 1)
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
  int maxWidthRamp(List<int> nums) {
    int n = nums.length;
    List<int> stack = [];
    for (int i = 0; i < n; ++i) {
      if (stack.isEmpty || nums[i] < nums[stack.last]) {
        stack.add(i);
      }
    }
    int maxWidth = 0;
    for (int j = n - 1; j >= 0; --j) {
      while (stack.isNotEmpty && nums[j] >= nums[stack.last]) {
        int i = stack.removeLast();
        int width = j - i;
        if (width > maxWidth) {
          maxWidth = width;
        }
      }
    }
    return maxWidth;
  }
}
```

## Golang

```go
func maxWidthRamp(nums []int) int {
	n := len(nums)
	stack := make([]int, 0, n)

	// Build a decreasing stack of indices
	for i := 0; i < n; i++ {
		if len(stack) == 0 || nums[i] < nums[stack[len(stack)-1]] {
			stack = append(stack, i)
		}
	}

	maxWidth := 0
	// Traverse from the end and try to pop valid ramps
	for j := n - 1; j >= 0; j-- {
		for len(stack) > 0 && nums[j] >= nums[stack[len(stack)-1]] {
			width := j - stack[len(stack)-1]
			if width > maxWidth {
				maxWidth = width
			}
			stack = stack[:len(stack)-1]
		}
	}
	return maxWidth
}
```

## Ruby

```ruby
def max_width_ramp(nums)
  n = nums.length
  stack = []
  nums.each_with_index do |val, i|
    if stack.empty? || val < nums[stack[-1]]
      stack << i
    end
  end

  max_width = 0
  (n - 1).downto(0) do |j|
    while !stack.empty? && nums[j] >= nums[stack[-1]]
      i = stack.pop
      width = j - i
      max_width = width if width > max_width
    end
  end

  max_width
end
```

## Scala

```scala
object Solution {
    def maxWidthRamp(nums: Array[Int]): Int = {
        val n = nums.length
        val stack = new scala.collection.mutable.ArrayBuffer[Int]()
        // Build a decreasing stack of indices
        for (i <- 0 until n) {
            if (stack.isEmpty || nums(i) < nums(stack.last)) {
                stack.append(i)
            }
        }
        var ans = 0
        // Scan from the right, trying to pop valid starts
        for (j <- (n - 1) to 0 by -1) {
            while (stack.nonEmpty && nums(j) >= nums(stack.last)) {
                ans = math.max(ans, j - stack.last)
                stack.remove(stack.length - 1)
            }
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_width_ramp(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut stack: Vec<usize> = Vec::new();
        for (i, &v) in nums.iter().enumerate() {
            if stack.is_empty() || v < nums[*stack.last().unwrap()] {
                stack.push(i);
            }
        }
        let mut max_width = 0usize;
        for j in (0..n).rev() {
            while let Some(&i_idx) = stack.last() {
                if nums[j] >= nums[i_idx] {
                    let width = j - i_idx;
                    if width > max_width {
                        max_width = width;
                    }
                    stack.pop();
                } else {
                    break;
                }
            }
        }
        max_width as i32
    }
}
```

## Racket

```racket
(define/contract (max-width-ramp nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (vec (list->vector nums)))
    (let ((max-width 0)
          (stack '()))
      ;; Build a decreasing stack of candidate left indices
      (for ([i (in-range n)])
        (let ((val (vector-ref vec i)))
          (when (or (null? stack)
                    (< val (vector-ref vec (car stack))))
            (set! stack (cons i stack)))))
      ;; Scan from right to left, trying to pop valid ramps
      (for ([j (in-range (sub1 n) -1 -1)])
        (let ((valj (vector-ref vec j)))
          (let loop ()
            (when (and (not (null? stack))
                       (>= valj (vector-ref vec (car stack))))
              (let ((i (car stack)))
                (when (> (- j i) max-width)
                  (set! max-width (- j i)))
                (set! stack (cdr stack))
                (loop))))))
      max-width)))
```

## Erlang

```erlang
-module(solution).
-export([max_width_ramp/1]).

-spec max_width_ramp(Nums :: [integer()]) -> integer().
max_width_ramp(Nums) ->
    Tuple = list_to_tuple(Nums),
    N = tuple_size(Tuple),
    Stack = build_stack(0, N, Tuple, []),
    process(N - 1, Stack, Tuple, 0).

%% Build a monotonic decreasing stack of indices
-spec build_stack(integer(), integer(), tuple(), [integer()]) -> [integer()].
build_stack(I, N, _Tuple, Stack) when I >= N ->
    Stack;
build_stack(I, N, Tuple, Stack) ->
    Val = element(I + 1, Tuple),
    case Stack of
        [] ->
            build_stack(I + 1, N, Tuple, [I]);
        [Top | _] ->
            TopVal = element(Top + 1, Tuple),
            if
                Val < TopVal ->
                    build_stack(I + 1, N, Tuple, [I | Stack]);
                true ->
                    build_stack(I + 1, N, Tuple, Stack)
            end
    end.

%% Process from right to left to find maximum width ramp
-spec process(integer(), [integer()], tuple(), integer()) -> integer().
process(J, _Stack, _Tuple, Max) when J < 0 ->
    Max;
process(_J, [], _Tuple, Max) ->
    Max;
process(J, [Top | Rest] = Stack, Tuple, Max) ->
    CurVal = element(J + 1, Tuple),
    TopVal = element(Top + 1, Tuple),
    if
        CurVal >= TopVal ->
            Width = J - Top,
            NewMax = case Width > Max of true -> Width; false -> Max end,
            process(J, Rest, Tuple, NewMax);
        true ->
            process(J - 1, Stack, Tuple, Max)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_width_ramp(nums :: [integer]) :: integer
  def max_width_ramp(nums) do
    n = length(nums)
    arr = List.to_tuple(nums)

    # Build monotonic decreasing stack of candidate left indices
    stack =
      0..(n - 1)
      |> Enum.reduce([], fn i, acc ->
        case acc do
          [] -> [i]
          [top | _] when elem(arr, i) < elem(arr, top) -> [i | acc]
          _ -> acc
        end
      end)

    # Process from right to left, popping while condition holds
    process(n - 1, arr, stack, 0)
  end

  defp process(i, _arr, stack, max_width) when i < 0 do
    max_width
  end

  defp process(i, arr, stack, max_width) do
    val = elem(arr, i)

    {new_stack, new_max} = pop_while(stack, val, i, arr, max_width)
    process(i - 1, arr, new_stack, new_max)
  end

  defp pop_while([], _val, _i, _arr, max), do: {[], max}

  defp pop_while([h | t] = stack, val, i, arr, max) do
    if val >= elem(arr, h) do
      width = i - h
      new_max = if width > max, do: width, else: max
      pop_while(t, val, i, arr, new_max)
    else
      {stack, max}
    end
  end
end
```
