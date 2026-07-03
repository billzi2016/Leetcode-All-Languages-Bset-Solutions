# 0118. Pascal's Triangle

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> triangle;
        if (numRows <= 0) return triangle;
        for (int i = 0; i < numRows; ++i) {
            vector<int> row(i + 1, 1);
            for (int j = 1; j < i; ++j) {
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
            }
            triangle.push_back(std::move(row));
        }
        return triangle;
    }
};
```

## Java

```java
class Solution {
    public java.util.List<java.util.List<Integer>> generate(int numRows) {
        java.util.List<java.util.List<Integer>> triangle = new java.util.ArrayList<>();
        for (int i = 0; i < numRows; i++) {
            java.util.List<Integer> row = new java.util.ArrayList<>(i + 1);
            for (int j = 0; j <= i; j++) {
                if (j == 0 || j == i) {
                    row.add(1);
                } else {
                    int val = triangle.get(i - 1).get(j - 1) + triangle.get(i - 1).get(j);
                    row.add(val);
                }
            }
            triangle.add(row);
        }
        return triangle;
    }
}
```

## Python

```python
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)
        return triangle
```

## Python3

```python
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle: List[List[int]] = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)
        return triangle
```

## C

```c
#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** generate(int numRows, int* returnSize, int*** returnColumnSizes) {
    // Adjust signature to match LeetCode's expected parameters
    // The original description had int** returnColumnSizes, but actual LeetCode uses int**.
    // We'll keep the given prototype and cast appropriately.
    (void)returnColumnSizes; // suppress unused warning if not used directly
    *returnSize = numRows;
    int **triangle = (int **)malloc(numRows * sizeof(int *));
    int *colSizes = (int *)malloc(numRows * sizeof(int));

    for (int i = 0; i < numRows; ++i) {
        int size = i + 1;
        colSizes[i] = size;
        triangle[i] = (int *)malloc(size * sizeof(int));
        triangle[i][0] = 1;
        triangle[i][size - 1] = 1;
        for (int j = 1; j < size - 1; ++j) {
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
        }
    }

    *returnColumnSizes = colSizes;
    return triangle;
}
```

## Csharp

```csharp
public class Solution {
    public IList<IList<int>> Generate(int numRows) {
        var triangle = new List<IList<int>>();
        for (int i = 0; i < numRows; i++) {
            var row = new List<int>(i + 1);
            for (int j = 0; j <= i; j++) {
                if (j == 0 || j == i) {
                    row.Add(1);
                } else {
                    int val = triangle[i - 1][j - 1] + triangle[i - 1][j];
                    row.Add(val);
                }
            }
            triangle.Add(row);
        }
        return triangle;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
    const triangle = [];
    for (let i = 0; i < numRows; i++) {
        const row = new Array(i + 1);
        row[0] = 1;
        row[i] = 1;
        for (let j = 1; j < i; j++) {
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
        }
        triangle.push(row);
    }
    return triangle;
};
```

## Typescript

```typescript
function generate(numRows: number): number[][] {
    const triangle: number[][] = [];
    for (let i = 0; i < numRows; i++) {
        const row: number[] = new Array(i + 1).fill(1);
        if (i > 1) {
            const prev = triangle[i - 1];
            for (let j = 1; j < i; j++) {
                row[j] = prev[j - 1] + prev[j];
            }
        }
        triangle.push(row);
    }
    return triangle;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $numRows
     * @return Integer[][]
     */
    function generate($numRows) {
        $triangle = [];
        for ($i = 0; $i < $numRows; $i++) {
            $row = array_fill(0, $i + 1, 1);
            for ($j = 1; $j < $i; $j++) {
                $row[$j] = $triangle[$i - 1][$j - 1] + $triangle[$i - 1][$j];
            }
            $triangle[] = $row;
        }
        return $triangle;
    }
}
```

## Swift

```swift
class Solution {
    func generate(_ numRows: Int) -> [[Int]] {
        var triangle = [[Int]]()
        for i in 0..<numRows {
            var row = Array(repeating: 1, count: i + 1)
            if i >= 2 {
                let prev = triangle[i - 1]
                for j in 1..<i {
                    row[j] = prev[j - 1] + prev[j]
                }
            }
            triangle.append(row)
        }
        return triangle
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun generate(numRows: Int): List<List<Int>> {
        val triangle = mutableListOf<MutableList<Int>>()
        for (i in 0 until numRows) {
            val row = MutableList(i + 1) { 1 }
            for (j in 1 until i) {
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            }
            triangle.add(row)
        }
        return triangle
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> generate(int numRows) {
    List<List<int>> result = [];
    for (int i = 0; i < numRows; i++) {
      List<int> row = List.filled(i + 1, 1);
      if (i >= 2) {
        for (int j = 1; j < i; j++) {
          row[j] = result[i - 1][j - 1] + result[i - 1][j];
        }
      }
      result.add(row);
    }
    return result;
  }
}
```

## Golang

```go
func generate(numRows int) [][]int {
	if numRows <= 0 {
		return [][]int{}
	}
	res := make([][]int, numRows)
	for i := 0; i < numRows; i++ {
		row := make([]int, i+1)
		row[0], row[i] = 1, 1
		for j := 1; j < i; j++ {
			row[j] = res[i-1][j-1] + res[i-1][j]
		}
		res[i] = row
	}
	return res
}
```

## Ruby

```ruby
def generate(num_rows)
  return [] if num_rows <= 0
  triangle = []
  (0...num_rows).each do |i|
    row = Array.new(i + 1, 1)
    (1...i).each do |j|
      row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    end
    triangle << row
  end
  triangle
end
```

## Scala

```scala
object Solution {
    def generate(numRows: Int): List[List[Int]] = {
        val result = scala.collection.mutable.ListBuffer[List[Int]]()
        for (i <- 0 until numRows) {
            val row = new Array[Int](i + 1)
            row(0) = 1
            row(i) = 1
            for (j <- 1 until i) {
                row(j) = result(i - 1)(j - 1) + result(i - 1)(j)
            }
            result += row.toList
        }
        result.toList
    }
}
```

## Rust

```rust
struct Solution;

impl Solution {
    pub fn generate(num_rows: i32) -> Vec<Vec<i32>> {
        let n = num_rows as usize;
        let mut res: Vec<Vec<i32>> = Vec::with_capacity(n);
        for i in 0..n {
            let mut row = vec![1; i + 1];
            if i >= 2 {
                let prev = &res[i - 1];
                for j in 1..i {
                    row[j] = prev[j - 1] + prev[j];
                }
            }
            res.push(row);
        }
        res
    }
}
```

## Racket

```racket
(define/contract (generate numRows)
  (-> exact-integer? (listof (listof exact-integer?)))
  (define (next-row prev)
    (if (null? prev)
        '(1)
        (let ((middle (map + prev (cdr prev))))
          (cons 1 (append middle '(1))))))
  (let loop ((i 0) (prev '()) (acc '()))
    (if (= i numRows)
        (reverse acc)
        (let ((row (if (= i 0) '(1) (next-row prev))))
          (loop (+ i 1) row (cons row acc))))))
```

## Erlang

```erlang
-spec generate(NumRows :: integer()) -> [[integer()]].
-export([generate/1]).
 
generate(NumRows) when NumRows =< 0 ->
    [];
generate(NumRows) ->
    gen(NumRows, [], []).

gen(0, _Prev, Acc) ->
    lists:reverse(Acc);
gen(N, [], Acc) ->
    Row = [1],
    gen(N-1, Row, [Row|Acc]);
gen(N, Prev, Acc) ->
    Row = next_row(Prev),
    gen(N-1, Row, [Row|Acc]).

next_row(Prev) ->
    Middle = lists:zipwith(fun(A,B) -> A + B end, Prev, tl(Prev)),
    [1 | Middle] ++ [1].
```

## Elixir

```elixir
defmodule Solution do
  @spec generate(num_rows :: integer) :: [[integer]]
  def generate(num_rows) when num_rows <= 0, do: []

  def generate(num_rows) do
    1..num_rows
    |> Enum.reduce([], fn _i, acc ->
      case acc do
        [] -> [[1] | acc]
        [prev | _] ->
          middle =
            prev
            |> Enum.zip(tl(prev))
            |> Enum.map(fn {a, b} -> a + b end)

          new_row = [1] ++ middle ++ [1]
          [new_row | acc]
      end
    end)
    |> Enum.reverse()
  end
end
```
