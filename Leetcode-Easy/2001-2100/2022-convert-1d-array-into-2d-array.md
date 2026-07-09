# 2022. Convert 1D Array Into 2D Array

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> construct2DArray(vector<int>& original, int m, int n) {
        if ((long long)m * n != (int)original.size()) return {};
        vector<vector<int>> result(m, vector<int>(n));
        for (int i = 0; i < (int)original.size(); ++i) {
            result[i / n][i % n] = original[i];
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public int[][] construct2DArray(int[] original, int m, int n) {
        if (original.length != m * n) {
            return new int[0][];
        }
        int[][] result = new int[m][n];
        for (int i = 0; i < original.length; i++) {
            result[i / n][i % n] = original[i];
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        if len(original) != m * n:
            return []
        return [original[i * n:(i + 1) * n] for i in range(m)]
```

## Python3

```python
class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if len(original) != m * n:
            return []
        result = [[0] * n for _ in range(m)]
        for i, val in enumerate(original):
            result[i // n][i % n] = val
        return result
```

## C

```c
#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** construct2DArray(int* original, int originalSize, int m, int n, int* returnSize, int*** returnColumnSizes) {
    if (originalSize != m * n) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }
    
    int **result = (int **)malloc(m * sizeof(int *));
    int *colSizes = (int *)malloc(m * sizeof(int));
    for (int i = 0; i < m; ++i) {
        colSizes[i] = n;
        result[i] = (int *)malloc(n * sizeof(int));
        for (int j = 0; j < n; ++j) {
            result[i][j] = original[i * n + j];
        }
    }
    
    *returnSize = m;
    *returnColumnSizes = colSizes;
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int[][] Construct2DArray(int[] original, int m, int n)
    {
        if ((long)m * n != original.Length)
            return new int[0][];

        int[][] result = new int[m][];
        int index = 0;
        for (int i = 0; i < m; i++)
        {
            int[] row = new int[n];
            for (int j = 0; j < n; j++)
                row[j] = original[index++];
            result[i] = row;
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} original
 * @param {number} m
 * @param {number} n
 * @return {number[][]}
 */
var construct2DArray = function(original, m, n) {
    if (original.length !== m * n) return [];
    const result = new Array(m);
    let idx = 0;
    for (let i = 0; i < m; i++) {
        const row = new Array(n);
        for (let j = 0; j < n; j++) {
            row[j] = original[idx++];
        }
        result[i] = row;
    }
    return result;
};
```

## Typescript

```typescript
function construct2DArray(original: number[], m: number, n: number): number[][] {
    if (original.length !== m * n) return [];
    const result: number[][] = new Array(m);
    for (let i = 0; i < m; i++) {
        const row: number[] = new Array(n);
        for (let j = 0; j < n; j++) {
            row[j] = original[i * n + j];
        }
        result[i] = row;
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $original
     * @param Integer $m
     * @param Integer $n
     * @return Integer[][]
     */
    function construct2DArray($original, $m, $n) {
        if (count($original) !== $m * $n) {
            return [];
        }
        $result = [];
        $idx = 0;
        for ($i = 0; $i < $m; $i++) {
            $row = [];
            for ($j = 0; $j < $n; $j++) {
                $row[] = $original[$idx++];
            }
            $result[] = $row;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func construct2DArray(_ original: [Int], _ m: Int, _ n: Int) -> [[Int]] {
        guard original.count == m * n else { return [] }
        var result = Array(repeating: Array(repeating: 0, count: n), count: m)
        for i in 0..<original.count {
            let row = i / n
            let col = i % n
            result[row][col] = original[i]
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun construct2DArray(original: IntArray, m: Int, n: Int): Array<IntArray> {
        if (original.size != m * n) return arrayOf()
        val result = Array(m) { IntArray(n) }
        var idx = 0
        for (i in 0 until m) {
            for (j in 0 until n) {
                result[i][j] = original[idx++]
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> construct2DArray(List<int> original, int m, int n) {
    if (original.length != m * n) return [];
    List<List<int>> result = List.generate(m, (_) => List.filled(n, 0));
    for (int i = 0; i < original.length; i++) {
      int row = i ~/ n;
      int col = i % n;
      result[row][col] = original[i];
    }
    return result;
  }
}
```

## Golang

```go
func construct2DArray(original []int, m int, n int) [][]int {
	if len(original) != m*n {
		return [][]int{}
	}
	result := make([][]int, m)
	for i := 0; i < m; i++ {
		row := make([]int, n)
		copy(row, original[i*n:(i+1)*n])
		result[i] = row
	}
	return result
}
```

## Ruby

```ruby
def construct2_d_array(original, m, n)
  return [] unless original.length == m * n
  result = Array.new(m) { Array.new(n) }
  idx = 0
  (0...m).each do |i|
    (0...n).each do |j|
      result[i][j] = original[idx]
      idx += 1
    end
  end
  result
end
```

## Scala

```scala
object Solution {
    def construct2DArray(original: Array[Int], m: Int, n: Int): Array[Array[Int]] = {
        if (original.length != m * n) return Array.empty[Array[Int]]
        val result = Array.ofDim[Int](m, n)
        var i = 0
        while (i < original.length) {
            val row = i / n
            val col = i % n
            result(row)(col) = original(i)
            i += 1
        }
        result
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn construct2_d_array(original: Vec<i32>, m: i32, n: i32) -> Vec<Vec<i32>> {
        let rows = m as usize;
        let cols = n as usize;
        if original.len() != rows * cols {
            return vec![];
        }
        let mut result = Vec::with_capacity(rows);
        for r in 0..rows {
            let start = r * cols;
            let end = start + cols;
            result.push(original[start..end].to_vec());
        }
        result
    }
}
```

## Racket

```racket
(define/contract (construct2-d-array original m n)
  (-> (listof exact-integer?) exact-integer? exact-integer? (listof (listof exact-integer?)))
  (if (not (= (length original) (* m n)))
      '()
      (let loop ((remaining original) (rows-left m) (result '()))
        (if (= rows-left 0)
            (reverse result)
            (call-with-values
                (lambda ()
                  (let build ((i n) (lst remaining) (row '()))
                    (if (= i 0)
                        (values (reverse row) lst)
                        (build (- i 1) (cdr lst) (cons (car lst) row)))))
              (lambda (row rest)
                (loop rest (- rows-left 1) (cons row result)))))))
```

## Erlang

```erlang
-spec construct2_d_array(Original :: [integer()], M :: integer(), N :: integer()) -> [[integer()]].
construct2_d_array(Original, M, N) ->
    case M * N =:= length(Original) of
        true -> chunk(Original, N);
        false -> []
    end.

chunk([], _N) -> [];
chunk(List, N) ->
    {Row, Rest} = lists:split(N, List),
    [Row | chunk(Rest, N)].
```

## Elixir

```elixir
defmodule Solution do
  @spec construct2_d_array(original :: [integer], m :: integer, n :: integer) :: [[integer]]
  def construct2_d_array(original, m, n) do
    if length(original) != m * n do
      []
    else
      Enum.chunk_every(original, n)
    end
  end
end
```
