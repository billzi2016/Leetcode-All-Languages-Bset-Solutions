# 3417. Zigzag Grid Traversal With Skip

## Cpp

```cpp
class Solution {
public:
    vector<int> zigzagTraversal(vector<vector<int>>& grid) {
        int m = grid.size();
        if (m == 0) return {};
        int n = grid[0].size();
        vector<int> result;
        bool take = true;
        for (int i = 0; i < m; ++i) {
            if (i % 2 == 0) {
                for (int j = 0; j < n; ++j) {
                    if (take) result.push_back(grid[i][j]);
                    take = !take;
                }
            } else {
                for (int j = n - 1; j >= 0; --j) {
                    if (take) result.push_back(grid[i][j]);
                    take = !take;
                }
            }
        }
        return result;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<Integer> zigzagTraversal(int[][] grid) {
        List<Integer> result = new ArrayList<>();
        int rows = grid.length;
        if (rows == 0) return result;
        int cols = grid[0].length;
        int idx = 0; // overall visited cell count
        for (int i = 0; i < rows; i++) {
            if ((i & 1) == 0) { // left to right
                for (int j = 0; j < cols; j++) {
                    if ((idx & 1) == 0) result.add(grid[i][j]);
                    idx++;
                }
            } else { // right to left
                for (int j = cols - 1; j >= 0; j--) {
                    if ((idx & 1) == 0) result.add(grid[i][j]);
                    idx++;
                }
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def zigzagTraversal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m = len(grid)
        n = len(grid[0])
        traversal = []
        for i in range(m):
            if i % 2 == 0:
                # left to right
                for j in range(n):
                    traversal.append(grid[i][j])
            else:
                # right to left
                for j in range(n - 1, -1, -1):
                    traversal.append(grid[i][j])
        return traversal[::2]
```

## Python3

```python
from typing import List

class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        order = []
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            if i % 2 == 0:
                for j in range(cols):
                    order.append(grid[i][j])
            else:
                for j in range(cols - 1, -1, -1):
                    order.append(grid[i][j])
        return order[::2]
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* zigzagTraversal(int** grid, int gridSize, int* gridColSize, int* returnSize) {
    if (gridSize == 0 || gridColSize == NULL) {
        *returnSize = 0;
        return NULL;
    }
    int cols = gridColSize[0];
    int total = gridSize * cols;
    int resSize = (total + 1) / 2;               // ceil(total/2)
    int* result = (int*)malloc(resSize * sizeof(int));
    
    int idx = 0;
    int take = 1;   // 1 means take the current cell
    for (int i = 0; i < gridSize; ++i) {
        if ((i & 1) == 0) { // left to right
            for (int j = 0; j < cols; ++j) {
                if (take) {
                    result[idx++] = grid[i][j];
                }
                take ^= 1;
            }
        } else { // right to left
            for (int j = cols - 1; j >= 0; --j) {
                if (take) {
                    result[idx++] = grid[i][j];
                }
                take ^= 1;
            }
        }
    }
    
    *returnSize = resSize;
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public IList<int> ZigzagTraversal(int[][] grid)
    {
        var result = new List<int>();
        int visitedCount = 0;
        for (int i = 0; i < grid.Length; i++)
        {
            if (i % 2 == 0) // left to right
            {
                for (int j = 0; j < grid[i].Length; j++)
                {
                    if (visitedCount % 2 == 0)
                        result.Add(grid[i][j]);
                    visitedCount++;
                }
            }
            else // right to left
            {
                for (int j = grid[i].Length - 1; j >= 0; j--)
                {
                    if (visitedCount % 2 == 0)
                        result.Add(grid[i][j]);
                    visitedCount++;
                }
            }
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number[]}
 */
var zigzagTraversal = function(grid) {
    const result = [];
    let take = true; // whether to include current cell
    for (let i = 0; i < grid.length; i++) {
        if (i % 2 === 0) {
            // left to right
            for (let j = 0; j < grid[i].length; j++) {
                if (take) result.push(grid[i][j]);
                take = !take;
            }
        } else {
            // right to left
            for (let j = grid[i].length - 1; j >= 0; j--) {
                if (take) result.push(grid[i][j]);
                take = !take;
            }
        }
    }
    return result;
};
```

## Typescript

```typescript
function zigzagTraversal(grid: number[][]): number[] {
    const m = grid.length;
    if (m === 0) return [];
    const n = grid[0].length;
    const result: number[] = [];
    let visitedCount = 0;
    for (let i = 0; i < m; i++) {
        if (i % 2 === 0) {
            // left to right
            for (let j = 0; j < n; j++) {
                if (visitedCount % 2 === 0) result.push(grid[i][j]);
                visitedCount++;
            }
        } else {
            // right to left
            for (let j = n - 1; j >= 0; j--) {
                if (visitedCount % 2 === 0) result.push(grid[i][j]);
                visitedCount++;
            }
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer[]
     */
    function zigzagTraversal($grid) {
        $rows = count($grid);
        if ($rows == 0) return [];
        $cols = count($grid[0]);
        $result = [];
        $pos = 0; // overall position in traversal

        for ($i = 0; $i < $rows; $i++) {
            if ($i % 2 == 0) { // left to right
                for ($j = 0; $j < $cols; $j++) {
                    if ($pos % 2 == 0) {
                        $result[] = $grid[$i][$j];
                    }
                    $pos++;
                }
            } else { // right to left
                for ($j = $cols - 1; $j >= 0; $j--) {
                    if ($pos % 2 == 0) {
                        $result[] = $grid[$i][$j];
                    }
                    $pos++;
                }
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func zigzagTraversal(_ grid: [[Int]]) -> [Int] {
        var result = [Int]()
        var index = 0
        let rows = grid.count
        guard rows > 0 else { return result }
        let cols = grid[0].count
        
        for i in 0..<rows {
            if i % 2 == 0 {
                for j in 0..<cols {
                    if index % 2 == 0 {
                        result.append(grid[i][j])
                    }
                    index += 1
                }
            } else {
                for j in stride(from: cols - 1, through: 0, by: -1) {
                    if index % 2 == 0 {
                        result.append(grid[i][j])
                    }
                    index += 1
                }
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun zigzagTraversal(grid: Array<IntArray>): List<Int> {
        val result = mutableListOf<Int>()
        var pos = 0
        val rows = grid.size
        val cols = grid[0].size
        for (i in 0 until rows) {
            if (i % 2 == 0) {
                for (j in 0 until cols) {
                    if (pos % 2 == 0) result.add(grid[i][j])
                    pos++
                }
            } else {
                for (j in cols - 1 downTo 0) {
                    if (pos % 2 == 0) result.add(grid[i][j])
                    pos++
                }
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> zigzagTraversal(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;
    List<int> result = [];
    int count = 0;
    for (int i = 0; i < m; i++) {
      if (i % 2 == 0) {
        for (int j = 0; j < n; j++) {
          if (count % 2 == 0) result.add(grid[i][j]);
          count++;
        }
      } else {
        for (int j = n - 1; j >= 0; j--) {
          if (count % 2 == 0) result.add(grid[i][j]);
          count++;
        }
      }
    }
    return result;
  }
}
```

## Golang

```go
func zigzagTraversal(grid [][]int) []int {
	var result []int
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[i]); j++ {
			if (i+j)%2 == 0 {
				result = append(result, grid[i][j])
			}
		}
	}
	return result
}
```

## Ruby

```ruby
def zigzag_traversal(grid)
  result = []
  grid.each do |row|
    row.each_with_index do |val, idx|
      result << val if idx.even?
    end
  end
  result
end
```

## Scala

```scala
object Solution {
    def zigzagTraversal(grid: Array[Array[Int]]): List[Int] = {
        val result = scala.collection.mutable.ListBuffer[Int]()
        var take = true
        for (i <- grid.indices) {
            if (i % 2 == 0) {
                for (j <- grid(i).indices) {
                    if (take) result += grid(i)(j)
                    take = !take
                }
            } else {
                for (j <- grid(i).indices.reverse) {
                    if (take) result += grid(i)(j)
                    take = !take
                }
            }
        }
        result.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn zigzag_traversal(grid: Vec<Vec<i32>>) -> Vec<i32> {
        let mut result = Vec::new();
        for (i, row) in grid.iter().enumerate() {
            for (j, &val) in row.iter().enumerate() {
                if ((i + j) % 2) == 0 {
                    result.push(val);
                }
            }
        }
        result
    }
}
```

## Racket

```racket
(define/contract (zigzag-traversal grid)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  (let ((rows (length grid)))
    (let loop ((i 0) (acc '()))
      (if (= i rows)
          (reverse acc)
          (let* ((row (list-ref grid i))
                 (cols (length row))
                 (indices (if (even? i)
                              (build-list cols (lambda (k) k))               ; left → right
                              (build-list cols (lambda (k) (- cols 1 k)))))   ; right → left
            (define new-acc
              (foldl (lambda (j a)
                       (if (even? (+ i j))
                           (cons (list-ref row j) a)
                           a))
                     acc
                     indices))
            (loop (+ i 1) new-acc))))))
```

## Erlang

```erlang
-spec zigzag_traversal(Grid :: [[integer()]]) -> [integer()].
zigzag_traversal(Grid) ->
    Snake = snake_order(Grid, 0, []),
    take_alternate(Snake).

snake_order([], _, Acc) -> Acc;
snake_order([Row|Rest], Index, Acc) ->
    DirRow = case Index rem 2 of
        0 -> Row;
        _ -> lists:reverse(Row)
    end,
    snake_order(Rest, Index + 1, Acc ++ DirRow).

take_alternate(List) -> take_alternate(List, 0, []).

take_alternate([], _, Res) -> lists:reverse(Res);
take_alternate([H|T], I, Res) ->
    case I rem 2 of
        0 -> take_alternate(T, I + 1, [H | Res]);
        _ -> take_alternate(T, I + 1, Res)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec zigzag_traversal(grid :: [[integer]]) :: [integer]
  def zigzag_traversal(grid) do
    rows = length(grid)
    cols = length(hd(grid))

    {result_rev, _} =
      Enum.reduce(0..rows - 1, {[], true}, fn i, {acc, take_flag} ->
        col_indices =
          if rem(i, 2) == 0,
            do: Enum.to_list(0..cols - 1),
            else: Enum.to_list(Enum.reverse(0..cols - 1))

        Enum.reduce(col_indices, {acc, take_flag}, fn j, {a, flag} ->
          val = Enum.at(Enum.at(grid, i), j)

          if flag do
            {[val | a], false}
          else
            {a, true}
          end
        end)
      end)

    Enum.reverse(result_rev)
  end
end
```
