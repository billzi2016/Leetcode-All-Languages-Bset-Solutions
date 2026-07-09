# 0084. Largest Rectangle in Histogram

## Cpp

```cpp
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        stack<int> st;
        st.push(-1);
        long long maxArea = 0;
        for (int i = 0; i <= n; ++i) {
            int curHeight = (i == n ? 0 : heights[i]);
            while (st.top() != -1 && curHeight < heights[st.top()]) {
                int height = heights[st.top()];
                st.pop();
                int width = i - st.top() - 1;
                maxArea = max(maxArea, 1LL * height * width);
            }
            st.push(i);
        }
        return (int)maxArea;
    }
};
```

## Java

```java
class Solution {
    public int largestRectangleArea(int[] heights) {
        int n = heights.length;
        java.util.Deque<Integer> stack = new java.util.ArrayDeque<>();
        stack.push(-1);
        int maxArea = 0;
        for (int i = 0; i <= n; i++) {
            int curHeight = (i == n) ? 0 : heights[i];
            while (stack.peek() != -1 && curHeight < heights[stack.peek()]) {
                int height = heights[stack.pop()];
                int width = i - stack.peek() - 1;
                int area = height * width;
                if (area > maxArea) {
                    maxArea = area;
                }
            }
            stack.push(i);
        }
        return maxArea;
    }
}
```

## Python

```python
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        max_area = 0
        # Append a sentinel to flush remaining bars
        for i, h in enumerate(heights + [0]):
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area
```

## Python3

```python
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        # Append a sentinel to flush remaining bars
        for i, h in enumerate(heights + [0]):
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area
```

## C

```c
#include <stdlib.h>

int largestRectangleArea(int* heights, int heightsSize) {
    if (heightsSize == 0) return 0;
    int *stack = (int *)malloc(sizeof(int) * (heightsSize + 1));
    int top = -1;
    int maxArea = 0;

    for (int i = 0; i <= heightsSize; ++i) {
        int curHeight = (i == heightsSize) ? 0 : heights[i];
        while (top >= 0 && curHeight < heights[stack[top]]) {
            int height = heights[stack[top--]];
            int width = (top == -1) ? i : i - stack[top] - 1;
            int area = height * width;
            if (area > maxArea) maxArea = area;
        }
        stack[++top] = i;
    }

    free(stack);
    return maxArea;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int LargestRectangleArea(int[] heights) {
        int n = heights.Length;
        var stack = new Stack<int>();
        stack.Push(-1); // sentinel
        int maxArea = 0;
        for (int i = 0; i <= n; i++) {
            int curHeight = (i == n) ? 0 : heights[i];
            while (stack.Peek() != -1 && curHeight < heights[stack.Peek()]) {
                int height = heights[stack.Pop()];
                int width = i - stack.Peek() - 1;
                int area = height * width;
                if (area > maxArea) maxArea = area;
            }
            stack.Push(i);
        }
        return maxArea;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} heights
 * @return {number}
 */
var largestRectangleArea = function(heights) {
    const n = heights.length;
    const stack = [];
    let maxArea = 0;
    for (let i = 0; i <= n; i++) {
        const curHeight = (i === n) ? 0 : heights[i];
        while (stack.length && curHeight < heights[stack[stack.length - 1]]) {
            const heightIdx = stack.pop();
            const height = heights[heightIdx];
            const width = stack.length ? i - stack[stack.length - 1] - 1 : i;
            const area = height * width;
            if (area > maxArea) maxArea = area;
        }
        stack.push(i);
    }
    return maxArea;
};
```

## Typescript

```typescript
function largestRectangleArea(heights: number[]): number {
    const n = heights.length;
    const stack: number[] = [];
    let maxArea = 0;
    for (let i = 0; i <= n; i++) {
        const curHeight = i === n ? 0 : heights[i];
        while (stack.length && curHeight < heights[stack[stack.length - 1]]) {
            const height = heights[stack.pop()!];
            const leftIndex = stack.length ? stack[stack.length - 1] : -1;
            const width = i - leftIndex - 1;
            const area = height * width;
            if (area > maxArea) maxArea = area;
        }
        stack.push(i);
    }
    return maxArea;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $heights
     * @return Integer
     */
    function largestRectangleArea($heights) {
        $stack = [];
        $maxArea = 0;
        $n = count($heights);
        for ($i = 0; $i <= $n; $i++) {
            $curHeight = ($i == $n) ? 0 : $heights[$i];
            while (!empty($stack) && $curHeight < $heights[end($stack)]) {
                $heightIdx = array_pop($stack);
                $height = $heights[$heightIdx];
                $width = empty($stack) ? $i : $i - end($stack) - 1;
                $area = $height * $width;
                if ($area > $maxArea) {
                    $maxArea = $area;
                }
            }
            $stack[] = $i;
        }
        return $maxArea;
    }
}
```

## Swift

```swift
class Solution {
    func largestRectangleArea(_ heights: [Int]) -> Int {
        var stack = [Int]()
        var maxArea = 0
        let n = heights.count
        
        for i in 0...n {
            let curHeight = (i == n) ? 0 : heights[i]
            while !stack.isEmpty && curHeight < heights[stack[stack.count - 1]] {
                let height = heights[stack.removeLast()]
                let leftIndex = stack.isEmpty ? -1 : stack.last!
                let width = i - leftIndex - 1
                maxArea = max(maxArea, height * width)
            }
            stack.append(i)
        }
        
        return maxArea
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun largestRectangleArea(heights: IntArray): Int {
        val n = heights.size
        val stack = IntArray(n + 1)
        var top = -1
        var maxArea = 0L
        for (i in 0..n) {
            val curHeight = if (i == n) 0 else heights[i]
            while (top >= 0 && curHeight < heights[stack[top]]) {
                val height = heights[stack[top--]]
                val leftIndex = if (top >= 0) stack[top] else -1
                val width = i - leftIndex - 1
                val area = height.toLong() * width
                if (area > maxArea) maxArea = area
            }
            stack[++top] = i
        }
        return maxArea.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int largestRectangleArea(List<int> heights) {
    List<int> h = List.from(heights)..add(0);
    List<int> stack = [];
    int maxArea = 0;

    for (int i = 0; i < h.length; i++) {
      while (stack.isNotEmpty && h[i] < h[stack.last]) {
        int height = h[stack.removeLast()];
        int width = stack.isEmpty ? i : i - stack.last - 1;
        int area = height * width;
        if (area > maxArea) maxArea = area;
      }
      stack.add(i);
    }

    return maxArea;
  }
}
```

## Golang

```go
func largestRectangleArea(heights []int) int {
	n := len(heights)
	stack := make([]int, 0, n+1)
	// sentinel index
	stack = append(stack, -1)
	maxArea := 0

	for i := 0; i <= n; i++ {
		var curHeight int
		if i == n {
			curHeight = 0 // sentinel height to flush stack
		} else {
			curHeight = heights[i]
		}
		for len(stack) > 1 && curHeight < heights[stack[len(stack)-1]] {
			topIdx := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			height := heights[topIdx]
			width := i - stack[len(stack)-1] - 1
			area := height * width
			if area > maxArea {
				maxArea = area
			}
		}
		stack = append(stack, i)
	}
	return maxArea
}
```

## Ruby

```ruby
def largest_rectangle_area(heights)
  stack = [-1]
  max_area = 0
  heights.each_with_index do |h, i|
    while stack.last != -1 && h < heights[stack[-1]]
      height = heights[stack.pop]
      width = i - stack[-1] - 1
      area = height * width
      max_area = area if area > max_area
    end
    stack << i
  end
  n = heights.length
  while stack.last != -1
    height = heights[stack.pop]
    width = n - stack[-1] - 1
    area = height * width
    max_area = area if area > max_area
  end
  max_area
end
```

## Scala

```scala
object Solution {
    def largestRectangleArea(heights: Array[Int]): Int = {
        val n = heights.length
        var maxArea: Long = 0L
        val stack = new scala.collection.mutable.ArrayDeque[Int]()
        for (i <- 0 to n) {
            val curHeight = if (i == n) 0 else heights(i)
            while (stack.nonEmpty && curHeight < heights(stack.last)) {
                val hIdx = stack.removeLast()
                val height = heights(hIdx).toLong
                val width = if (stack.isEmpty) i else i - stack.last - 1
                val area = height * width
                if (area > maxArea) maxArea = area
            }
            if (i < n) {
                stack.append(i)
            }
        }
        maxArea.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn largest_rectangle_area(heights: Vec<i32>) -> i32 {
        let n = heights.len();
        let mut stack: Vec<usize> = Vec::new(); // indices with increasing heights
        let mut max_area: i64 = 0;

        for i in 0..=n {
            let cur_height = if i == n { 0 } else { heights[i] };
            while let Some(&top) = stack.last() {
                if cur_height < heights[top] {
                    stack.pop();
                    let height = heights[top] as i64;
                    let left_boundary = match stack.last() {
                        Some(&idx) => idx as i64,
                        None => -1,
                    };
                    let width = i as i64 - left_boundary - 1;
                    let area = height * width;
                    if area > max_area {
                        max_area = area;
                    }
                } else {
                    break;
                }
            }
            stack.push(i);
        }

        max_area as i32
    }
}
```

## Racket

```racket
(define/contract (largest-rectangle-area heights)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((len (length heights))
         (orig (list->vector heights))
         (v    (make-vector (+ len 1) 0))) ; extra sentinel 0
    ;; copy original heights into v
    (for ([i len])
      (vector-set! v i (vector-ref orig i)))
    (let ((stack (make-vector (+ len 1) -1)) ; stack of indices
          (top   -1)
          (max-area 0))
      (for ([i (+ len 1)])               ; iterate including sentinel
        (let ((curr (vector-ref v i)))
          ;; pop higher bars
          (let loop ()
            (when (and (> top -1)
                       (< curr (vector-ref v (vector-ref stack top))))
              (define idx   (vector-ref stack top))
              (set! top (- top 1))
              (define height (vector-ref v idx))
              (define width (if (= top -1)
                                i
                                (- i (vector-ref stack top) 1)))
              (set! max-area (max max-area (* height width)))
              (loop))))
          ;; push current index
          (set! top (+ top 1))
          (vector-set! stack top i)))
      max-area)))
```

## Erlang

```erlang
-module(solution).
-export([largest_rectangle_area/1]).

-spec largest_rectangle_area(Heights :: [integer()]) -> integer().
largest_rectangle_area(Heights) ->
    H = Heights ++ [0],
    process(H, 0, [], 0).

process([], _Idx, [], Max) ->
    Max;
process([H|Rest], Idx, Stack, Max) ->
    case Stack of
        [] ->
            process(Rest, Idx + 1, [{Idx, H}], Max);
        [{_, TopHeight} | _] when H >= TopHeight ->
            process(Rest, Idx + 1, [{Idx, H} | Stack], Max);
        _ ->
            {NewStack, NewMax, StartPos} = pop_until(H, Idx, Stack, Max, Idx),
            process(Rest, Idx + 1, [{StartPos, H} | NewStack], NewMax)
    end.

pop_until(_H, _Idx, [], Max, Start) ->
    {[], Max, Start};
pop_until(H, Idx, [{Pos, Height} | Tail], Max, Start) when Height > H ->
    Area = Height * (Idx - Pos),
    NewMax = if Area > Max -> Area; true -> Max end,
    NewStart = if Pos < Start -> Pos; true -> Start end,
    pop_until(H, Idx, Tail, NewMax, NewStart);
pop_until(_H, _Idx, Stack, Max, Start) ->
    {Stack, Max, Start}.
```

## Elixir

```elixir
defmodule Solution do
  @spec largest_rectangle_area(heights :: [integer]) :: integer
  def largest_rectangle_area(heights) do
    heights = heights ++ [0]
    htuple = List.to_tuple(heights)
    n = tuple_size(htuple)
    loop(0, n, htuple, [], 0)
  end

  defp loop(i, n, htuple, stack, max) when i < n do
    h = elem(htuple, i)

    cond do
      stack == [] or h >= elem(hd(stack), 1) ->
        loop(i + 1, n, htuple, [{i, h} | stack], max)

      true ->
        [{pop_i, pop_h} | rest] = stack
        width = if rest == [], do: i, else: i - elem(hd(rest), 0) - 1
        new_max = if pop_h * width > max, do: pop_h * width, else: max
        loop(i, n, htuple, rest, new_max)
    end
  end

  defp loop(_i, _n, _htuple, _stack, max), do: max
end
```
