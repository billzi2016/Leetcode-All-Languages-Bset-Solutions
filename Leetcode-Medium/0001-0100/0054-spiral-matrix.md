# 0054. Spiral Matrix

## Cpp

```cpp
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) return {};
        int m = matrix.size(), n = matrix[0].size();
        vector<int> res;
        res.reserve(m * n);
        int top = 0, bottom = m - 1, left = 0, right = n - 1;
        while (top <= bottom && left <= right) {
            for (int j = left; j <= right; ++j)
                res.push_back(matrix[top][j]);
            ++top;
            if (top > bottom) break;
            
            for (int i = top; i <= bottom; ++i)
                res.push_back(matrix[i][right]);
            --right;
            if (left > right) break;
            
            for (int j = right; j >= left; --j)
                res.push_back(matrix[bottom][j]);
            --bottom;
            if (top > bottom) break;
            
            for (int i = bottom; i >= top; --i)
                res.push_back(matrix[i][left]);
            ++left;
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> res = new ArrayList<>();
        if (matrix == null || matrix.length == 0) return res;
        int m = matrix.length, n = matrix[0].length;
        int top = 0, bottom = m - 1, left = 0, right = n - 1;
        while (top <= bottom && left <= right) {
            for (int j = left; j <= right; j++) res.add(matrix[top][j]);
            top++;
            for (int i = top; i <= bottom; i++) res.add(matrix[i][right]);
            right--;
            if (top <= bottom) {
                for (int j = right; j >= left; j--) res.add(matrix[bottom][j]);
                bottom--;
            }
            if (left <= right) {
                for (int i = bottom; i >= top; i--) res.add(matrix[i][left]);
                left++;
            }
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        res = []
        while top <= bottom and left <= right:
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res
```

## Python3

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1
            if top > bottom:
                break

            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1
            if left > right:
                break

            for col in range(right, left - 1, -1):
                res.append(matrix[bottom][col])
            bottom -= 1
            if top > bottom:
                break

            for row in range(bottom, top - 1, -1):
                res.append(matrix[row][left])
            left += 1

        return res
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* spiralOrder(int** matrix, int matrixSize, int* matrixColSize, int* returnSize) {
    if (matrixSize == 0 || matrixColSize == NULL) {
        *returnSize = 0;
        return NULL;
    }
    
    int m = matrixSize;
    int n = matrixColSize[0];
    int total = m * n;
    int *res = (int *)malloc(total * sizeof(int));
    if (!res) {
        *returnSize = 0;
        return NULL;
    }
    
    int top = 0, bottom = m - 1;
    int left = 0, right = n - 1;
    int idx = 0;
    
    while (top <= bottom && left <= right) {
        // Traverse from Left to Right on the top row
        for (int col = left; col <= right; ++col) {
            res[idx++] = matrix[top][col];
        }
        top++;
        
        // Traverse from Top to Bottom on the rightmost column
        for (int row = top; row <= bottom; ++row) {
            res[idx++] = matrix[row][right];
        }
        right--;
        
        // Traverse from Right to Left on the bottom row, if still within bounds
        if (top <= bottom) {
            for (int col = right; col >= left; --col) {
                res[idx++] = matrix[bottom][col];
            }
            bottom--;
        }
        
        // Traverse from Bottom to Top on the leftmost column, if still within bounds
        if (left <= right) {
            for (int row = bottom; row >= top; --row) {
                res[idx++] = matrix[row][left];
            }
            left++;
        }
    }
    
    *returnSize = total;
    return res;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<int> SpiralOrder(int[][] matrix) {
        var result = new List<int>();
        if (matrix == null || matrix.Length == 0 || matrix[0].Length == 0)
            return result;
        
        int m = matrix.Length;
        int n = matrix[0].Length;
        int top = 0, bottom = m - 1, left = 0, right = n - 1;
        
        while (top <= bottom && left <= right) {
            // Move right
            for (int j = left; j <= right; j++) {
                result.Add(matrix[top][j]);
            }
            top++;
            if (top > bottom) break;
            
            // Move down
            for (int i = top; i <= bottom; i++) {
                result.Add(matrix[i][right]);
            }
            right--;
            if (left > right) break;
            
            // Move left
            for (int j = right; j >= left; j--) {
                result.Add(matrix[bottom][j]);
            }
            bottom--;
            if (top > bottom) break;
            
            // Move up
            for (int i = bottom; i >= top; i--) {
                result.Add(matrix[i][left]);
            }
            left++;
        }
        
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    const result = [];
    if (!matrix.length || !matrix[0].length) return result;

    let top = 0;
    let bottom = matrix.length - 1;
    let left = 0;
    let right = matrix[0].length - 1;

    while (top <= bottom && left <= right) {
        // Traverse from Left to Right on the top row
        for (let col = left; col <= right; col++) {
            result.push(matrix[top][col]);
        }
        top++;

        // Traverse from Top to Bottom on the rightmost column
        for (let row = top; row <= bottom; row++) {
            result.push(matrix[row][right]);
        }
        right--;

        // Traverse from Right to Left on the bottom row, if still within bounds
        if (top <= bottom) {
            for (let col = right; col >= left; col--) {
                result.push(matrix[bottom][col]);
            }
            bottom--;
        }

        // Traverse from Bottom to Top on the leftmost column, if still within bounds
        if (left <= right) {
            for (let row = bottom; row >= top; row--) {
                result.push(matrix[row][left]);
            }
            left++;
        }
    }

    return result;
};
```

## Typescript

```typescript
function spiralOrder(matrix: number[][]): number[] {
    const result: number[] = [];
    if (matrix.length === 0) return result;
    let top = 0, bottom = matrix.length - 1;
    let left = 0, right = matrix[0].length - 1;

    while (top <= bottom && left <= right) {
        for (let col = left; col <= right; col++) {
            result.push(matrix[top][col]);
        }
        top++;

        for (let row = top; row <= bottom; row++) {
            result.push(matrix[row][right]);
        }
        right--;

        if (top <= bottom) {
            for (let col = right; col >= left; col--) {
                result.push(matrix[bottom][col]);
            }
            bottom--;
        }

        if (left <= right) {
            for (let row = bottom; row >= top; row--) {
                result.push(matrix[row][left]);
            }
            left++;
        }
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $matrix
     * @return Integer[]
     */
    function spiralOrder($matrix) {
        $result = [];
        if (empty($matrix)) {
            return $result;
        }

        $top = 0;
        $bottom = count($matrix) - 1;
        $left = 0;
        $right = count($matrix[0]) - 1;

        while ($top <= $bottom && $left <= $right) {
            // Traverse from Left to Right on the top row
            for ($col = $left; $col <= $right; $col++) {
                $result[] = $matrix[$top][$col];
            }
            $top++;

            // Traverse from Top to Bottom on the rightmost column
            for ($row = $top; $row <= $bottom; $row++) {
                $result[] = $matrix[$row][$right];
            }
            $right--;

            // Traverse from Right to Left on the bottom row, if still within bounds
            if ($top <= $bottom) {
                for ($col = $right; $col >= $left; $col--) {
                    $result[] = $matrix[$bottom][$col];
                }
                $bottom--;
            }

            // Traverse from Bottom to Top on the leftmost column, if still within bounds
            if ($left <= $right) {
                for ($row = $bottom; $row >= $top; $row--) {
                    $result[] = $matrix[$row][$left];
                }
                $left++;
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func spiralOrder(_ matrix: [[Int]]) -> [Int] {
        guard !matrix.isEmpty && !matrix[0].isEmpty else { return [] }
        var top = 0
        var bottom = matrix.count - 1
        var left = 0
        var right = matrix[0].count - 1
        var result: [Int] = []
        
        while top <= bottom && left <= right {
            // Top row
            for col in left...right {
                result.append(matrix[top][col])
            }
            top += 1
            if top > bottom { break }
            
            // Right column
            for row in top...bottom {
                result.append(matrix[row][right])
            }
            right -= 1
            if left > right { break }
            
            // Bottom row
            if top <= bottom {
                for col in stride(from: right, through: left, by: -1) {
                    result.append(matrix[bottom][col])
                }
                bottom -= 1
            }
            if top > bottom { break }
            
            // Left column
            if left <= right {
                for row in stride(from: bottom, through: top, by: -1) {
                    result.append(matrix[row][left])
                }
                left += 1
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun spiralOrder(matrix: Array<IntArray>): List<Int> {
        if (matrix.isEmpty() || matrix[0].isEmpty()) return emptyList()
        val m = matrix.size
        val n = matrix[0].size
        var top = 0
        var bottom = m - 1
        var left = 0
        var right = n - 1
        val result = ArrayList<Int>(m * n)
        while (top <= bottom && left <= right) {
            for (j in left..right) result.add(matrix[top][j])
            top++
            if (top > bottom) break

            for (i in top..bottom) result.add(matrix[i][right])
            right--
            if (left > right) break

            for (j in right downTo left) result.add(matrix[bottom][j])
            bottom--
            if (top > bottom) break

            for (i in bottom downTo top) result.add(matrix[i][left])
            left++
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> spiralOrder(List<List<int>> matrix) {
    if (matrix.isEmpty || matrix[0].isEmpty) return [];
    int m = matrix.length;
    int n = matrix[0].length;
    int top = 0, bottom = m - 1, left = 0, right = n - 1;
    List<int> result = [];

    while (top <= bottom && left <= right) {
      // Traverse from Left to Right on the top row
      for (int col = left; col <= right; col++) {
        result.add(matrix[top][col]);
      }
      top++;
      if (top > bottom) break;

      // Traverse from Top to Bottom on the rightmost column
      for (int row = top; row <= bottom; row++) {
        result.add(matrix[row][right]);
      }
      right--;
      if (left > right) break;

      // Traverse from Right to Left on the bottom row
      for (int col = right; col >= left; col--) {
        result.add(matrix[bottom][col]);
      }
      bottom--;
      if (top > bottom) break;

      // Traverse from Bottom to Top on the leftmost column
      for (int row = bottom; row >= top; row--) {
        result.add(matrix[row][left]);
      }
      left++;
    }

    return result;
  }
}
```

## Golang

```go
func spiralOrder(matrix [][]int) []int {
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return []int{}
	}
	m, n := len(matrix), len(matrix[0])
	res := make([]int, 0, m*n)
	top, bottom := 0, m-1
	left, right := 0, n-1

	for top <= bottom && left <= right {
		for col := left; col <= right; col++ {
			res = append(res, matrix[top][col])
		}
		top++

		for row := top; row <= bottom; row++ {
			res = append(res, matrix[row][right])
		}
		right--

		if top <= bottom {
			for col := right; col >= left; col-- {
				res = append(res, matrix[bottom][col])
			}
			bottom--
		}

		if left <= right {
			for row := bottom; row >= top; row-- {
				res = append(res, matrix[row][left])
			}
			left++
		}
	}
	return res
}
```

## Ruby

```ruby
def spiral_order(matrix)
  return [] if matrix.empty?
  top = 0
  bottom = matrix.size - 1
  left = 0
  right = matrix[0].size - 1
  result = []

  while top <= bottom && left <= right
    (left..right).each { |j| result << matrix[top][j] }
    top += 1
    break if top > bottom

    (top..bottom).each { |i| result << matrix[i][right] }
    right -= 1
    break if left > right

    right.downto(left) { |j| result << matrix[bottom][j] }
    bottom -= 1
    break if top > bottom

    bottom.downto(top) { |i| result << matrix[i][left] }
    left += 1
  end

  result
end
```

## Scala

```scala
object Solution {
    def spiralOrder(matrix: Array[Array[Int]]): List[Int] = {
        if (matrix.isEmpty || matrix(0).isEmpty) return Nil
        var top = 0
        var bottom = matrix.length - 1
        var left = 0
        var right = matrix(0).length - 1
        val res = scala.collection.mutable.ListBuffer[Int]()
        while (top <= bottom && left <= right) {
            // top row
            for (j <- left to right) res += matrix(top)(j)
            top += 1
            if (top > bottom) return res.toList

            // right column
            for (i <- top to bottom) res += matrix(i)(right)
            right -= 1
            if (left > right) return res.toList

            // bottom row
            for (j <- right to left by -1) res += matrix(bottom)(j)
            bottom -= 1
            if (top > bottom) return res.toList

            // left column
            for (i <- bottom to top by -1) res += matrix(i)(left)
            left += 1
        }
        res.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn spiral_order(matrix: Vec<Vec<i32>>) -> Vec<i32> {
        if matrix.is_empty() || matrix[0].is_empty() {
            return vec![];
        }
        let m = matrix.len() as i32;
        let n = matrix[0].len() as i32;
        let mut top = 0;
        let mut bottom = m - 1;
        let mut left = 0;
        let mut right = n - 1;
        let mut res = Vec::with_capacity((m * n) as usize);
        while top <= bottom && left <= right {
            // Move right across the top row
            for col in left..=right {
                res.push(matrix[top as usize][col as usize]);
            }
            top += 1;
            if top > bottom { break; }

            // Move down the rightmost column
            for row in top..=bottom {
                res.push(matrix[row as usize][right as usize]);
            }
            right -= 1;
            if left > right { break; }

            // Move left across the bottom row
            for col in (left..=right).rev() {
                res.push(matrix[bottom as usize][col as usize]);
            }
            bottom -= 1;
            if top > bottom { break; }

            // Move up the leftmost column
            for row in (top..=bottom).rev() {
                res.push(matrix[row as usize][left as usize]);
            }
            left += 1;
        }
        res
    }
}
```

## Racket

```racket
(define/contract (spiral-order matrix)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ((m (length matrix))
         (n (if (= m 0) 0 (length (car matrix))))
         (top 0)
         (bottom (- m 1))
         (left 0)
         (right (- n 1))
         (result '()))
    (let loop ()
      (when (and (<= top bottom) (<= left right))
        ;; traverse top row
        (for ([j (in-range left (+ right 1))])
          (set! result (cons (list-ref (list-ref matrix top) j) result)))
        (set! top (+ top 1))
        ;; traverse right column
        (when (and (<= top bottom) (<= left right))
          (for ([i (in-range top (+ bottom 1))])
            (set! result (cons (list-ref (list-ref matrix i) right) result))))
        (set! right (- right 1))
        ;; traverse bottom row
        (when (and (<= top bottom) (<= left right))
          (for ([j (in-range right (+ left -1) -1)])
            (set! result (cons (list-ref (list-ref matrix bottom) j) result))))
        (set! bottom (- bottom 1))
        ;; traverse left column
        (when (and (<= top bottom) (<= left right))
          (for ([i (in-range bottom (+ top -1) -1)])
            (set! result (cons (list-ref (list-ref matrix i) left) result))))
        (set! left (+ left 1))
        (loop)))
    (reverse result)))
```

## Erlang

```erlang
-module(solution).
-export([spiral_order/1]).
-spec spiral_order(Matrix :: [[integer()]]) -> [integer()].
spiral_order(Matrix) ->
    case Matrix of
        [] -> [];
        _ ->
            Rows = length(Matrix),
            Cols = length(hd(Matrix)),
            loop(0, Rows - 1, 0, Cols - 1, Matrix, [])
    end.

loop(Top, Bottom, Left, Right, Mtx, Acc) when Top =< Bottom, Left =< Right ->
    Acc1 = add_row_left_to_right(Top, Left, Right, Mtx, Acc),
    NewTop = Top + 1,
    Acc2 = case NewTop =< Bottom of
               true -> add_col_top_to_bottom(NewTop, Bottom, Right, Mtx, Acc1);
               false -> Acc1
           end,
    NewRight = Right - 1,
    {Acc3, NewBottom} = case NewTop =< Bottom andalso Left =< NewRight of
                            true ->
                                {add_row_right_to_left(Bottom, NewRight, Left, Mtx, Acc2), Bottom - 1};
                            false -> {Acc2, Bottom}
                        end,
    Acc4 = case NewTop =< NewBottom andalso Left =< NewRight of
               true -> add_col_bottom_to_top(NewBottom, NewTop, Left, Mtx, Acc3);
               false -> Acc3
           end,
    loop(NewTop, NewBottom, Left + 1, NewRight, Mtx, Acc4);
loop(_, _, _, _, _Mtx, Acc) ->
    lists:reverse(Acc).

add_row_left_to_right(Row, L, R, Mtx, Acc) when L =< R ->
    Elem = get_elem(Row, L, Mtx),
    add_row_left_to_right(Row, L + 1, R, Mtx, [Elem | Acc]);
add_row_left_to_right(_, L, R, _, Acc) when L > R -> Acc.

add_row_right_to_left(Row, R, L, Mtx, Acc) when R >= L ->
    Elem = get_elem(Row, R, Mtx),
    add_row_right_to_left(Row, R - 1, L, Mtx, [Elem | Acc]);
add_row_right_to_left(_, R, L, _, Acc) when R < L -> Acc.

add_col_top_to_bottom(T, B, Col, Mtx, Acc) when T =< B ->
    Elem = get_elem(T, Col, Mtx),
    add_col_top_to_bottom(T + 1, B, Col, Mtx, [Elem | Acc]);
add_col_top_to_bottom(_, _, _, _, Acc) -> Acc.

add_col_bottom_to_top(B, T, Col, Mtx, Acc) when B >= T ->
    Elem = get_elem(B, Col, Mtx),
    add_col_bottom_to_top(B - 1, T, Col, Mtx, [Elem | Acc]);
add_col_bottom_to_top(_, _, _, _, Acc) -> Acc.

get_elem(I, J, Mtx) ->
    Row = lists:nth(I + 1, Mtx),
    lists:nth(J + 1, Row).
```

## Elixir

```elixir
defmodule Solution do
  @spec spiral_order(matrix :: [[integer]]) :: [integer]
  def spiral_order(matrix) do
    m = length(matrix)
    n = if m == 0, do: 0, else: length(hd(matrix))
    do_spiral(matrix, 0, m - 1, 0, n - 1, [])
  end

  defp do_spiral(_matrix, top, bottom, left, right, acc) when top > bottom or left > right,
    do: acc

  defp do_spiral(matrix, top, bottom, left, right, acc) do
    # top row
    top_row = Enum.slice(Enum.at(matrix, top), left..right)
    acc1 = acc ++ top_row

    # right column (excluding top row)
    right_col =
      if top < bottom do
        for i <- (top + 1)..bottom, do: Enum.at(Enum.at(matrix, i), right)
      else
        []
      end

    acc2 = acc1 ++ right_col

    # bottom row (right to left) if there is more than one row remaining
    acc3 =
      if top < bottom do
        bottom_row = Enum.slice(Enum.at(matrix, bottom), left..right) |> Enum.reverse()
        acc2 ++ bottom_row
      else
        acc2
      end

    # left column (upwards) if there is more than one column remaining
    left_col =
      if left < right do
        for i <- :lists.seq(bottom - 1, top + 1, -1), do: Enum.at(Enum.at(matrix, i), left)
      else
        []
      end

    acc4 = acc3 ++ left_col

    do_spiral(matrix, top + 1, bottom - 1, left + 1, right - 1, acc4)
  end
end
```
