# 0085. Maximal Rectangle

## Cpp

```cpp
class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) return 0;
        int rows = matrix.size(), cols = matrix[0].size();
        vector<int> heights(cols, 0);
        int maxArea = 0;
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                if (matrix[i][j] == '1')
                    heights[j] += 1;
                else
                    heights[j] = 0;
            }
            maxArea = max(maxArea, largestRectangleArea(heights));
        }
        return maxArea;
    }
private:
    int largestRectangleArea(const vector<int>& h) {
        vector<int> heights = h;
        heights.push_back(0); // sentinel
        stack<int> st;
        int maxA = 0;
        for (int i = 0; i < (int)heights.size(); ++i) {
            while (!st.empty() && heights[i] < heights[st.top()]) {
                int height = heights[st.top()];
                st.pop();
                int width = st.empty() ? i : i - st.top() - 1;
                maxA = max(maxA, height * width);
            }
            st.push(i);
        }
        return maxA;
    }
};
```

## Java

```java
class Solution {
    public int maximalRectangle(char[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) return 0;
        int rows = matrix.length, cols = matrix[0].length;
        int[] heights = new int[cols];
        int maxArea = 0;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (matrix[r][c] == '1') {
                    heights[c] += 1;
                } else {
                    heights[c] = 0;
                }
            }
            maxArea = Math.max(maxArea, largestRectangleArea(heights));
        }
        return maxArea;
    }

    private int largestRectangleArea(int[] heights) {
        int n = heights.length;
        java.util.Stack<Integer> stack = new java.util.Stack<>();
        int max = 0;
        for (int i = 0; i <= n; i++) {
            int curHeight = (i == n) ? 0 : heights[i];
            while (!stack.isEmpty() && curHeight < heights[stack.peek()]) {
                int height = heights[stack.pop()];
                int width = stack.isEmpty() ? i : i - stack.peek() - 1;
                max = Math.max(max, height * width);
            }
            stack.push(i);
        }
        return max;
    }
}
```

## Python

```python
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        heights = [0] * (n + 1)  # extra sentinel
        max_area = 0

        for row in matrix:
            for i in range(n):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0

            stack = []
            for i in range(n + 1):
                while stack and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * width)
                stack.append(i)

        return max_area
```

## Python3

```python
class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        heights = [0] * (n + 1)  # extra sentinel zero
        max_area = 0

        for row in matrix:
            for i in range(n):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0

            stack = []
            for i, h in enumerate(heights):
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)

        return max_area
```

## C

```c
#include <stdlib.h>

int maximalRectangle(char** matrix, int matrixSize, int* matrixColSize) {
    if (matrixSize == 0 || matrixColSize == NULL || matrixColSize[0] == 0) return 0;
    int cols = matrixColSize[0];
    int *heights = (int*)calloc(cols, sizeof(int));
    int maxArea = 0;

    for (int i = 0; i < matrixSize; ++i) {
        for (int j = 0; j < cols; ++j) {
            if (matrix[i][j] == '1')
                heights[j] += 1;
            else
                heights[j] = 0;
        }

        int *stack = (int*)malloc((cols + 1) * sizeof(int));
        int top = 0;
        for (int j = 0; j <= cols; ++j) {
            int curHeight = (j == cols) ? 0 : heights[j];
            while (top > 0 && curHeight < heights[stack[top - 1]]) {
                int h = heights[stack[--top]];
                int width = top == 0 ? j : j - stack[top - 1] - 1;
                int area = h * width;
                if (area > maxArea) maxArea = area;
            }
            stack[top++] = j;
        }
        free(stack);
    }

    free(heights);
    return maxArea;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaximalRectangle(char[][] matrix)
    {
        if (matrix == null || matrix.Length == 0 || matrix[0].Length == 0)
            return 0;

        int rows = matrix.Length;
        int cols = matrix[0].Length;
        int[] heights = new int[cols];
        int maxArea = 0;

        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                if (matrix[i][j] == '1')
                    heights[j] += 1;
                else
                    heights[j] = 0;
            }

            maxArea = Math.Max(maxArea, LargestRectangleArea(heights));
        }

        return maxArea;
    }

    private int LargestRectangleArea(int[] heights)
    {
        int n = heights.Length;
        var stack = new System.Collections.Generic.Stack<int>();
        stack.Push(-1);
        int maxArea = 0;

        for (int i = 0; i < n; i++)
        {
            while (stack.Peek() != -1 && heights[i] < heights[stack.Peek()])
            {
                int height = heights[stack.Pop()];
                int width = i - stack.Peek() - 1;
                maxArea = Math.Max(maxArea, height * width);
            }
            stack.Push(i);
        }

        while (stack.Peek() != -1)
        {
            int height = heights[stack.Pop()];
            int width = n - stack.Peek() - 1;
            maxArea = Math.Max(maxArea, height * width);
        }

        return maxArea;
    }
}
```

## Javascript

```javascript
/**
 * @param {character[][]} matrix
 * @return {number}
 */
var maximalRectangle = function(matrix) {
    if (!matrix || matrix.length === 0 || matrix[0].length === 0) return 0;
    const cols = matrix[0].length;
    const heights = new Array(cols).fill(0);
    let maxArea = 0;

    const largestRectangleArea = (heights) => {
        const stack = [];
        let max = 0;
        for (let i = 0; i <= heights.length; i++) {
            const curHeight = i === heights.length ? 0 : heights[i];
            while (stack.length && curHeight < heights[stack[stack.length - 1]]) {
                const h = heights[stack.pop()];
                const left = stack.length ? stack[stack.length - 1] + 1 : 0;
                const width = i - left;
                max = Math.max(max, h * width);
            }
            stack.push(i);
        }
        return max;
    };

    for (let row = 0; row < matrix.length; row++) {
        for (let col = 0; col < cols; col++) {
            heights[col] = matrix[row][col] === '1' ? heights[col] + 1 : 0;
        }
        maxArea = Math.max(maxArea, largestRectangleArea(heights));
    }

    return maxArea;
};
```

## Typescript

```typescript
function maximalRectangle(matrix: string[][]): number {
    if (!matrix || matrix.length === 0 || matrix[0].length === 0) return 0;
    const rows = matrix.length;
    const cols = matrix[0].length;
    const heights = new Array<number>(cols).fill(0);
    let maxArea = 0;

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            heights[j] = matrix[i][j] === '1' ? heights[j] + 1 : 0;
        }

        const stack: number[] = [];
        for (let k = 0; k <= cols; k++) {
            const curHeight = k === cols ? 0 : heights[k];
            while (stack.length && curHeight < heights[stack[stack.length - 1]]) {
                const h = heights[stack.pop()!];
                const left = stack.length ? stack[stack.length - 1] + 1 : 0;
                const width = k - left;
                maxArea = Math.max(maxArea, h * width);
            }
            stack.push(k);
        }
    }

    return maxArea;
}
```

## Php

```php
class Solution {

    /**
     * @param String[][] $matrix
     * @return Integer
     */
    function maximalRectangle($matrix) {
        if (empty($matrix) || empty($matrix[0])) {
            return 0;
        }
        $rows = count($matrix);
        $cols = count($matrix[0]);
        $heights = array_fill(0, $cols, 0);
        $maxArea = 0;

        for ($i = 0; $i < $rows; $i++) {
            for ($j = 0; $j < $cols; $j++) {
                if ($matrix[$i][$j] === '1') {
                    $heights[$j] += 1;
                } else {
                    $heights[$j] = 0;
                }
            }
            $maxArea = max($maxArea, $this->largestRectangleArea($heights));
        }

        return $maxArea;
    }

    private function largestRectangleArea($heights) {
        $stack = [];
        $max = 0;
        $n = count($heights);
        for ($i = 0; $i <= $n; $i++) {
            $curHeight = ($i == $n) ? 0 : $heights[$i];
            while (!empty($stack) && $curHeight < $heights[end($stack)]) {
                $height = $heights[array_pop($stack)];
                $width = empty($stack) ? $i : $i - end($stack) - 1;
                $max = max($max, $height * $width);
            }
            $stack[] = $i;
        }
        return $max;
    }
}
```

## Swift

```swift
class Solution {
    func maximalRectangle(_ matrix: [[Character]]) -> Int {
        guard !matrix.isEmpty else { return 0 }
        let cols = matrix[0].count
        var heights = Array(repeating: 0, count: cols)
        var maxArea = 0
        
        for row in matrix {
            for (j, ch) in row.enumerated() {
                if ch == "1" {
                    heights[j] += 1
                } else {
                    heights[j] = 0
                }
            }
            maxArea = max(maxArea, largestRectangleArea(heights))
        }
        return maxArea
    }
    
    private func largestRectangleArea(_ heights: [Int]) -> Int {
        var stack = [Int]()
        var maxA = 0
        let n = heights.count
        
        for i in 0...n { // include sentinel at the end
            let curHeight = (i == n) ? 0 : heights[i]
            while let last = stack.last, curHeight < heights[last] {
                let height = heights[stack.removeLast()]
                let width: Int
                if let newLast = stack.last {
                    width = i - newLast - 1
                } else {
                    width = i
                }
                maxA = max(maxA, height * width)
            }
            stack.append(i)
        }
        return maxA
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximalRectangle(matrix: Array<CharArray>): Int {
        if (matrix.isEmpty() || matrix[0].isEmpty()) return 0
        val n = matrix[0].size
        val heights = IntArray(n)
        var maxArea = 0
        for (row in matrix) {
            for (j in 0 until n) {
                if (row[j] == '1') {
                    heights[j] += 1
                } else {
                    heights[j] = 0
                }
            }
            maxArea = kotlin.math.max(maxArea, largestRectangleArea(heights))
        }
        return maxArea
    }

    private fun largestRectangleArea(heights: IntArray): Int {
        val stack = java.util.ArrayDeque<Int>()
        var maxArea = 0
        for (i in heights.indices) {
            while (!stack.isEmpty() && heights[i] < heights[stack.peek()]) {
                val h = heights[stack.pop()]
                val width = if (stack.isEmpty()) i else i - stack.peek() - 1
                maxArea = kotlin.math.max(maxArea, h * width)
            }
            stack.push(i)
        }
        var i = heights.size
        while (!stack.isEmpty()) {
            val h = heights[stack.pop()]
            val width = if (stack.isEmpty()) i else i - stack.peek() - 1
            maxArea = kotlin.math.max(maxArea, h * width)
        }
        return maxArea
    }
}
```

## Dart

```dart
class Solution {
  int maximalRectangle(List<List<String>> matrix) {
    if (matrix.isEmpty || matrix[0].isEmpty) return 0;
    int cols = matrix[0].length;
    List<int> heights = List.filled(cols, 0);
    int maxArea = 0;
    for (var row in matrix) {
      for (int j = 0; j < cols; ++j) {
        if (row[j] == '1') {
          heights[j] += 1;
        } else {
          heights[j] = 0;
        }
      }
      maxArea = _largestRectangleArea(heights, maxArea);
    }
    return maxArea;
  }

  int _largestRectangleArea(List<int> heights, int currentMax) {
    List<int> stack = [];
    int maxArea = currentMax;
    for (int i = 0; i <= heights.length; ++i) {
      int curHeight = i == heights.length ? 0 : heights[i];
      while (stack.isNotEmpty && curHeight < heights[stack.last]) {
        int h = heights[stack.removeLast()];
        int width = stack.isEmpty ? i : i - stack.last - 1;
        int area = h * width;
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
func maximalRectangle(matrix [][]byte) int {
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return 0
	}
	cols := len(matrix[0])
	heights := make([]int, cols)
	maxArea := 0

	for _, row := range matrix {
		for j := 0; j < cols; j++ {
			if row[j] == '1' {
				heights[j]++
			} else {
				heights[j] = 0
			}
		}

		stack := []int{}
		for i := 0; i <= cols; i++ {
			var cur int
			if i == cols {
				cur = 0
			} else {
				cur = heights[i]
			}
			for len(stack) > 0 && cur < heights[stack[len(stack)-1]] {
				h := heights[stack[len(stack)-1]]
				stack = stack[:len(stack)-1]
				var width int
				if len(stack) == 0 {
					width = i
				} else {
					width = i - stack[len(stack)-1] - 1
				}
				area := h * width
				if area > maxArea {
					maxArea = area
				}
			}
			stack = append(stack, i)
		}
	}

	return maxArea
}
```

## Ruby

```ruby
def maximal_rectangle(matrix)
  return 0 if matrix.nil? || matrix.empty? || matrix[0].empty?
  cols = matrix[0].size
  heights = Array.new(cols, 0)
  max_area = 0

  matrix.each do |row|
    row.each_with_index do |val, j|
      heights[j] = val == '1' ? heights[j] + 1 : 0
    end

    stack = []
    extended = heights + [0]
    extended.each_with_index do |h, i|
      while !stack.empty? && h < extended[stack[-1]]
        height = extended[stack.pop]
        width = stack.empty? ? i : i - stack[-1] - 1
        area = height * width
        max_area = area if area > max_area
      end
      stack << i
    end
  end

  max_area
end
```

## Scala

```scala
object Solution {
  def maximalRectangle(matrix: Array[Array[Char]]): Int = {
    if (matrix.isEmpty || matrix.head.isEmpty) return 0
    val rows = matrix.length
    val cols = matrix(0).length
    val heights = new Array[Int](cols)
    var maxArea = 0

    def largestRectangleArea(h: Array[Int]): Int = {
      import java.util.ArrayDeque
      val stack = new ArrayDeque[Int]()
      var area = 0
      for (i <- 0 to h.length) {
        val curHeight = if (i == h.length) 0 else h(i)
        while (!stack.isEmpty && curHeight < h(stack.peek())) {
          val height = h(stack.pop())
          val leftIdx = if (stack.isEmpty) -1 else stack.peek()
          val width = i - leftIdx - 1
          area = math.max(area, height * width)
        }
        stack.push(i)
      }
      area
    }

    for (r <- 0 until rows) {
      for (c <- 0 until cols) {
        if (matrix(r)(c) == '1') heights(c) += 1 else heights(c) = 0
      }
      maxArea = math.max(maxArea, largestRectangleArea(heights))
    }

    maxArea
  }
}
```

## Rust

```rust
impl Solution {
    pub fn maximal_rectangle(matrix: Vec<Vec<char>>) -> i32 {
        if matrix.is_empty() || matrix[0].is_empty() {
            return 0;
        }
        let cols = matrix[0].len();
        let mut heights = vec![0i32; cols];
        let mut max_area = 0i32;
        for row in matrix.iter() {
            for (j, &c) in row.iter().enumerate() {
                if c == '1' {
                    heights[j] += 1;
                } else {
                    heights[j] = 0;
                }
            }
            let area = Self::largest_rectangle_area(&heights);
            if area > max_area {
                max_area = area;
            }
        }
        max_area
    }

    fn largest_rectangle_area(heights: &[i32]) -> i32 {
        let mut stack: Vec<usize> = Vec::new();
        let mut max_area = 0i32;
        for (i, &h) in heights.iter().enumerate() {
            while let Some(&top) = stack.last() {
                if h < heights[top] {
                    stack.pop();
                    let height = heights[top];
                    let width = if let Some(&prev) = stack.last() { i - prev - 1 } else { i };
                    max_area = max_area.max(height * width as i32);
                } else {
                    break;
                }
            }
            stack.push(i);
        }
        let n = heights.len();
        while let Some(top) = stack.pop() {
            let height = heights[top];
            let width = if let Some(&prev) = stack.last() { n - prev - 1 } else { n };
            max_area = max_area.max(height * width as i32);
        }
        max_area
    }
}
```

## Racket

```racket
(define (largest-rectangle-area heights)
  (let* ((n (vector-length heights))
         (stack '())
         (max-area 0))
    (for ([i (in-range (+ n 1))])
      (define cur-height (if (= i n) 0 (vector-ref heights i)))
      (let loop ()
        (when (and (not (null? stack))
                   (< cur-height (vector-ref heights (car stack))))
          (define top (car stack))
          (set! stack (cdr stack))
          (define h (vector-ref heights top))
          (define width (if (null? stack) i (- i (car stack) 1)))
          (define area (* h width))
          (when (> area max-area) (set! max-area area))
          (loop)))
      (set! stack (cons i stack)))
    max-area))

(define/contract (maximal-rectangle matrix)
  (-> (listof (listof char?)) exact-integer?)
  (if (null? matrix)
      0
      (let* ((cols (length (car matrix)))
             (heights (make-vector cols 0))
             (result (let loop ((rows matrix) (max-a 0))
                       (if (null? rows)
                           max-a
                           (begin
                             (for ([j (in-range cols)]
                                   [ch (in-list (car rows))])
                               (vector-set! heights j
                                 (if (char=? ch #\1)
                                     (+ 1 (vector-ref heights j))
                                     0)))
                             (define area (largest-rectangle-area heights))
                             (loop (cdr rows) (max max-a area)))))))
        result)))
```

## Erlang

```erlang
-module(solution).
-export([maximal_rectangle/1]).

-spec maximal_rectangle(Matrix :: [[char()]]) -> integer().
maximal_rectangle([]) ->
    0;
maximal_rectangle(Matrix) ->
    Cols = length(hd(Matrix)),
    Heights0 = lists:duplicate(Cols, 0),
    maximal_rectangle_rows(Matrix, Heights0, 0).

maximal_rectangle_rows([], _Heights, Max) ->
    Max;
maximal_rectangle_rows([Row|Rest], Heights, Max) ->
    NewHeights = update_heights(Row, Heights, []),
    Area = largest_rectangle(NewHeights),
    NewMax = erlang:max(Max, Area),
    maximal_rectangle_rows(Rest, NewHeights, NewMax).

update_heights([], [], Acc) ->
    lists:reverse(Acc);
update_heights([Cell|RestRow], [H|RestHeight], Acc) ->
    NewH = case Cell of
               $1 -> H + 1;
               _ -> 0
           end,
    update_heights(RestRow, RestHeight, [NewH|Acc]).

largest_rectangle(Heights) ->
    Tuple = list_to_tuple(Heights),
    N = tuple_size(Tuple),
    loop_histogram(0, Tuple, N, [], 0).

loop_histogram(I, _Tuple, N, _Stack, Max) when I > N ->
    Max;
loop_histogram(I, Tuple, N, Stack, Max) ->
    CurH = if I == N -> 0; true -> element(I+1, Tuple) end,
    case Stack of
        [] ->
            loop_histogram(I+1, Tuple, N, [I|Stack], Max);
        [_|_] ->
            TopIdx = hd(Stack),
            TopH = element(TopIdx+1, Tuple),
            if CurH >= TopH ->
                loop_histogram(I+1, Tuple, N, [I|Stack], Max);
               true ->
                NewStack = tl(Stack),
                Height = TopH,
                Width = case NewStack of
                            [] -> I;
                            [_|_] -> I - hd(NewStack) - 1
                        end,
                Area = Height * Width,
                NewMax = erlang:max(Max, Area),
                loop_histogram(I, Tuple, N, NewStack, NewMax)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximal_rectangle(matrix :: [[char]]) :: integer
  def maximal_rectangle(matrix) do
    case matrix do
      [] -> 0
      [_ | _] = rows when hd(rows) == [] -> 0
      _ ->
        cols = length(hd(matrix))
        init_heights = List.duplicate(0, cols)

        {max_area, _} =
          Enum.reduce(matrix, {0, init_heights}, fn row, {global_max, heights} ->
            new_heights =
              Enum.with_index(row)
              |> Enum.map(fn {val, idx} ->
                if val == "1" or val == ?1 do
                  Enum.at(heights, idx) + 1
                else
                  0
                end
              end)

            area = largest_rectangle(new_heights)
            new_max = if area > global_max, do: area, else: global_max
            {new_max, new_heights}
          end)

        max_area
    end
  end

  defp largest_rectangle(heights) do
    heights = heights ++ [0]
    compute(heights, 0, [], 0)
  end

  defp compute(heights, i, stack, max) when i < length(heights) do
    h = Enum.at(heights, i)

    cond do
      stack == [] or h >= Enum.at(heights, hd(stack)) ->
        compute(heights, i + 1, [i | stack], max)

      true ->
        [top | rest] = stack
        height = Enum.at(heights, top)
        left = if rest == [], do: -1, else: hd(rest)
        width = i - left - 1
        new_max = if height * width > max, do: height * width, else: max
        compute(heights, i, rest, new_max)
    end
  end

  defp compute(_heights, _i, _stack, max), do: max
end
```
