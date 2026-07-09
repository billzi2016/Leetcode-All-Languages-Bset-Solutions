# 1975. Maximum Matrix Sum

## Cpp

```cpp
class Solution {
public:
    long long maxMatrixSum(vector<vector<int>>& matrix) {
        long long total = 0;
        int negCount = 0;
        int minAbs = INT_MAX;
        for (auto& row : matrix) {
            for (int val : row) {
                int a = std::abs(val);
                total += a;
                if (val < 0) ++negCount;
                if (a < minAbs) minAbs = a;
            }
        }
        if (negCount % 2 == 1) {
            total -= 2LL * minAbs;
        }
        return total;
    }
};
```

## Java

```java
class Solution {
    public long maxMatrixSum(int[][] matrix) {
        long total = 0L;
        int negCount = 0;
        int minAbs = Integer.MAX_VALUE;
        for (int[] row : matrix) {
            for (int val : row) {
                int absVal = Math.abs(val);
                total += absVal;
                if (val < 0) {
                    negCount++;
                }
                if (absVal < minAbs) {
                    minAbs = absVal;
                }
            }
        }
        if ((negCount & 1) == 1) {
            total -= 2L * minAbs;
        }
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        total = 0
        min_abs = float('inf')
        neg_cnt = 0
        for row in matrix:
            for val in row:
                if val < 0:
                    neg_cnt += 1
                a = abs(val)
                total += a
                if a < min_abs:
                    min_abs = a
        if neg_cnt % 2 == 1:
            total -= 2 * min_abs
        return total
```

## Python3

```python
from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        min_abs = float('inf')
        neg_cnt = 0
        for row in matrix:
            for val in row:
                if val < 0:
                    neg_cnt += 1
                a = abs(val)
                total += a
                if a < min_abs:
                    min_abs = a
        if neg_cnt % 2 == 1:
            total -= 2 * min_abs
        return total
```

## C

```c
#include <limits.h>

long long maxMatrixSum(int** matrix, int matrixSize, int* matrixColSize) {
    long long total = 0;
    int negCount = 0;
    int minAbs = INT_MAX;
    
    for (int i = 0; i < matrixSize; ++i) {
        int cols = matrixColSize[i];
        for (int j = 0; j < cols; ++j) {
            int val = matrix[i][j];
            if (val < 0) negCount++;
            int absVal = val >= 0 ? val : -val;
            total += absVal;
            if (absVal < minAbs) minAbs = absVal;
        }
    }
    
    if (negCount % 2 == 1) {
        total -= 2LL * minAbs;
    }
    
    return total;
}
```

## Csharp

```csharp
public class Solution
{
    public long MaxMatrixSum(int[][] matrix)
    {
        long total = 0;
        int negativeCount = 0;
        int minAbs = int.MaxValue;

        foreach (var row in matrix)
        {
            foreach (int val in row)
            {
                int absVal = Math.Abs(val);
                total += absVal;
                if (val < 0) negativeCount++;
                if (absVal < minAbs) minAbs = absVal;
            }
        }

        if ((negativeCount & 1) == 1)
        {
            total -= 2L * minAbs;
        }

        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} matrix
 * @return {number}
 */
var maxMatrixSum = function(matrix) {
    let total = 0;
    let minAbs = Infinity;
    let negCount = 0;
    
    for (let i = 0; i < matrix.length; i++) {
        const row = matrix[i];
        for (let j = 0; j < row.length; j++) {
            const val = row[j];
            const absVal = Math.abs(val);
            total += absVal;
            if (val < 0) negCount++;
            if (absVal < minAbs) minAbs = absVal;
        }
    }
    
    if (negCount % 2 === 1) {
        total -= 2 * minAbs;
    }
    
    return total;
};
```

## Typescript

```typescript
function maxMatrixSum(matrix: number[][]): number {
    let total = 0;
    let minAbs = Number.MAX_SAFE_INTEGER;
    let negCount = 0;
    for (const row of matrix) {
        for (const val of row) {
            const absVal = Math.abs(val);
            total += absVal;
            if (val < 0) negCount++;
            if (absVal < minAbs) minAbs = absVal;
        }
    }
    if (negCount % 2 === 1) {
        total -= 2 * minAbs;
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $matrix
     * @return Integer
     */
    function maxMatrixSum($matrix) {
        $total = 0;
        $negCount = 0;
        $minAbs = PHP_INT_MAX;

        foreach ($matrix as $row) {
            foreach ($row as $val) {
                if ($val < 0) {
                    $negCount++;
                }
                $absVal = abs($val);
                $total += $absVal;
                if ($absVal < $minAbs) {
                    $minAbs = $absVal;
                }
            }
        }

        if ($negCount % 2 == 1) {
            $total -= 2 * $minAbs;
        }

        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func maxMatrixSum(_ matrix: [[Int]]) -> Int {
        var total = 0
        var minAbs = Int.max
        var negativeCount = 0
        
        for row in matrix {
            for val in row {
                let a = abs(val)
                total += a
                if val < 0 { negativeCount += 1 }
                if a < minAbs { minAbs = a }
            }
        }
        
        if negativeCount % 2 == 1 {
            total -= 2 * minAbs
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxMatrixSum(matrix: Array<IntArray>): Long {
        var total = 0L
        var negativeCount = 0
        var minAbs = Int.MAX_VALUE
        for (row in matrix) {
            for (value in row) {
                val absVal = kotlin.math.abs(value)
                total += absVal.toLong()
                if (value < 0) negativeCount++
                if (absVal < minAbs) minAbs = absVal
            }
        }
        if (negativeCount % 2 == 1) {
            total -= 2L * minAbs
        }
        return total
    }
}
```

## Dart

```dart
class Solution {
  int maxMatrixSum(List<List<int>> matrix) {
    int total = 0;
    int minAbs = 1 << 60;
    int negCount = 0;

    for (var row in matrix) {
      for (var val in row) {
        int absVal = val.abs();
        total += absVal;
        if (val < 0) negCount++;
        if (absVal < minAbs) minAbs = absVal;
      }
    }

    if ((negCount & 1) == 1) {
      total -= 2 * minAbs;
    }

    return total;
  }
}
```

## Golang

```go
func maxMatrixSum(matrix [][]int) int64 {
	var total int64
	negCount := 0
	minAbs := int(^uint(0) >> 1) // MaxInt

	for _, row := range matrix {
		for _, v := range row {
			if v < 0 {
				negCount++
			}
			absVal := v
			if absVal < 0 {
				absVal = -absVal
			}
			total += int64(absVal)
			if absVal < minAbs {
				minAbs = absVal
			}
		}
	}

	if negCount%2 == 1 {
		total -= int64(2 * minAbs)
	}
	return total
}
```

## Ruby

```ruby
def max_matrix_sum(matrix)
  total = 0
  negative_count = 0
  min_abs = Float::INFINITY

  matrix.each do |row|
    row.each do |val|
      abs_val = val.abs
      total += abs_val
      negative_count += 1 if val < 0
      min_abs = abs_val if abs_val < min_abs
    end
  end

  total -= 2 * min_abs if negative_count.odd?
  total
end
```

## Scala

```scala
object Solution {
  def maxMatrixSum(matrix: Array[Array[Int]]): Long = {
    var total: Long = 0L
    var minAbs: Int = Int.MaxValue
    var negCount = 0
    var i = 0
    while (i < matrix.length) {
      val row = matrix(i)
      var j = 0
      while (j < row.length) {
        val v = row(j)
        val av = if (v >= 0) v else -v
        total += av.toLong
        if (v < 0) negCount += 1
        if (av < minAbs) minAbs = av
        j += 1
      }
      i += 1
    }
    if ((negCount & 1) == 1) {
      total -= 2L * minAbs
    }
    total
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_matrix_sum(matrix: Vec<Vec<i32>>) -> i64 {
        let mut total: i64 = 0;
        let mut min_abs: i32 = i32::MAX;
        let mut neg_parity: u8 = 0; // 0 for even, 1 for odd

        for row in matrix.iter() {
            for &val in row.iter() {
                let av = val.abs();
                total += av as i64;
                if val < 0 {
                    neg_parity ^= 1;
                }
                if av < min_abs {
                    min_abs = av;
                }
            }
        }

        if neg_parity == 1 {
            total -= (2 * min_abs) as i64;
        }
        total
    }
}
```

## Racket

```racket
(define/contract (max-matrix-sum matrix)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let ((total 0)
        (neg-count 0)
        (min-abs +inf.0))
    (for ([row matrix])
      (for ([val row])
        (set! total (+ total (abs val)))
        (when (< val 0) (set! neg-count (+ neg-count 1)))
        (let ((a (abs val)))
          (when (< a min-abs) (set! min-abs a)))))
    (if (odd? neg-count)
        (- total (* 2 min-abs))
        total)))
```

## Erlang

```erlang
-module(solution).
-export([max_matrix_sum/1]).

-spec max_matrix_sum(Matrix :: [[integer()]]) -> integer().
max_matrix_sum(Matrix) ->
    Flat = lists:flatten(Matrix),
    {Sum, NegCnt, MinAbs} = lists:foldl(
        fun(Elem, {S, N, M}) ->
            Abs = erlang:abs(Elem),
            NewS = S + Abs,
            NewN = if Elem < 0 -> N + 1; true -> N end,
            NewM = if Abs < M -> Abs; true -> M end,
            {NewS, NewN, NewM}
        end,
        {0, 0, 1 bsl 31},
        Flat
    ),
    case NegCnt rem 2 of
        1 -> Sum - 2 * MinAbs;
        _ -> Sum
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_matrix_sum(matrix :: [[integer]]) :: integer
  def max_matrix_sum(matrix) do
    {total, neg_cnt, min_abs} =
      Enum.reduce(matrix, {0, 0, 1 <<< 60}, fn row, acc ->
        Enum.reduce(row, acc, fn val, {sum, cnt, cur_min} ->
          a = Kernel.abs(val)
          sum = sum + a
          cnt = if val < 0, do: cnt + 1, else: cnt
          cur_min = if a < cur_min, do: a, else: cur_min
          {sum, cnt, cur_min}
        end)
      end)

    if rem(neg_cnt, 2) == 0 do
      total
    else
      total - 2 * min_abs
    end
  end
end
```
