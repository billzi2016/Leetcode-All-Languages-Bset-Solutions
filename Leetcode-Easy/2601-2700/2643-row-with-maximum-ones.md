# 2643. Row With Maximum Ones

## Cpp

```cpp
class Solution {
public:
    vector<int> rowAndMaximumOnes(vector<vector<int>>& mat) {
        int bestRow = 0;
        int bestCnt = -1;
        for (int i = 0; i < (int)mat.size(); ++i) {
            int cnt = 0;
            for (int val : mat[i]) cnt += val;
            if (cnt > bestCnt) {
                bestCnt = cnt;
                bestRow = i;
            }
        }
        return {bestRow, bestCnt};
    }
};
```

## Java

```java
class Solution {
    public int[] rowAndMaximumOnes(int[][] mat) {
        int bestRow = 0;
        int maxOnes = -1;
        for (int i = 0; i < mat.length; i++) {
            int count = 0;
            for (int val : mat[i]) {
                if (val == 1) count++;
            }
            if (count > maxOnes) {
                maxOnes = count;
                bestRow = i;
            }
        }
        return new int[]{bestRow, maxOnes};
    }
}
```

## Python

```python
class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        max_count = -1
        max_row = 0
        for i, row in enumerate(mat):
            cnt = sum(row)
            if cnt > max_count:
                max_count = cnt
                max_row = i
        return [max_row, max_count]
```

## Python3

```python
from typing import List

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_ones = -1
        row_index = 0
        for i, row in enumerate(mat):
            cnt = sum(row)
            if cnt > max_ones:
                max_ones = cnt
                row_index = i
        return [row_index, max_ones]
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* rowAndMaximumOnes(int** mat, int matSize, int* matColSize, int* returnSize) {
    int maxCount = -1;
    int maxRow = 0;
    
    for (int i = 0; i < matSize; ++i) {
        int count = 0;
        int cols = matColSize[i];
        for (int j = 0; j < cols; ++j) {
            if (mat[i][j] == 1) {
                ++count;
            }
        }
        if (count > maxCount) {
            maxCount = count;
            maxRow = i;
        }
    }
    
    int* result = (int*)malloc(2 * sizeof(int));
    result[0] = maxRow;
    result[1] = maxCount;
    *returnSize = 2;
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int[] RowAndMaximumOnes(int[][] mat) {
        int bestRow = 0;
        int maxOnes = -1;
        for (int i = 0; i < mat.Length; i++) {
            int count = 0;
            foreach (int val in mat[i]) {
                if (val == 1) count++;
            }
            if (count > maxOnes) {
                maxOnes = count;
                bestRow = i;
            }
        }
        return new int[] { bestRow, maxOnes };
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} mat
 * @return {number[]}
 */
var rowAndMaximumOnes = function(mat) {
    let maxRow = 0;
    let maxCnt = -1;
    for (let i = 0; i < mat.length; i++) {
        const cnt = mat[i].reduce((a, b) => a + b, 0);
        if (cnt > maxCnt) {
            maxCnt = cnt;
            maxRow = i;
        }
    }
    return [maxRow, maxCnt];
};
```

## Typescript

```typescript
function rowAndMaximumOnes(mat: number[][]): number[] {
    let bestRow = 0;
    let maxOnes = -1;
    for (let i = 0; i < mat.length; i++) {
        let count = 0;
        const row = mat[i];
        for (let j = 0; j < row.length; j++) {
            if (row[j] === 1) count++;
        }
        if (count > maxOnes) {
            maxOnes = count;
            bestRow = i;
        }
    }
    return [bestRow, maxOnes];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $mat
     * @return Integer[]
     */
    function rowAndMaximumOnes($mat) {
        $bestRow = 0;
        $maxOnes = -1;
        foreach ($mat as $i => $row) {
            $cnt = array_sum($row);
            if ($cnt > $maxOnes) {
                $maxOnes = $cnt;
                $bestRow = $i;
            }
        }
        return [$bestRow, $maxOnes];
    }
}
```

## Swift

```swift
class Solution {
    func rowAndMaximumOnes(_ mat: [[Int]]) -> [Int] {
        var bestRow = 0
        var bestCount = -1
        for (i, row) in mat.enumerated() {
            let count = row.reduce(0, +)
            if count > bestCount {
                bestCount = count
                bestRow = i
            }
        }
        return [bestRow, bestCount]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun rowAndMaximumOnes(mat: Array<IntArray>): IntArray {
        var bestRow = 0
        var bestCount = -1
        for (i in mat.indices) {
            var cnt = 0
            for (v in mat[i]) {
                if (v == 1) cnt++
            }
            if (cnt > bestCount) {
                bestCount = cnt
                bestRow = i
            }
        }
        return intArrayOf(bestRow, bestCount)
    }
}
```

## Dart

```dart
class Solution {
  List<int> rowAndMaximumOnes(List<List<int>> mat) {
    int bestRow = 0;
    int bestCount = -1;
    for (int i = 0; i < mat.length; i++) {
      int cnt = 0;
      for (int val in mat[i]) {
        if (val == 1) cnt++;
      }
      if (cnt > bestCount) {
        bestCount = cnt;
        bestRow = i;
      }
    }
    return [bestRow, bestCount];
  }
}
```

## Golang

```go
func rowAndMaximumOnes(mat [][]int) []int {
    maxCount := -1
    rowIndex := 0
    for i, row := range mat {
        count := 0
        for _, val := range row {
            if val == 1 {
                count++
            }
        }
        if count > maxCount {
            maxCount = count
            rowIndex = i
        }
    }
    return []int{rowIndex, maxCount}
}
```

## Ruby

```ruby
def row_and_maximum_ones(mat)
  best_idx = 0
  best_cnt = -1
  mat.each_with_index do |row, i|
    cnt = row.sum
    if cnt > best_cnt
      best_cnt = cnt
      best_idx = i
    end
  end
  [best_idx, best_cnt]
end
```

## Scala

```scala
object Solution {
    def rowAndMaximumOnes(mat: Array[Array[Int]]): Array[Int] = {
        var bestRow = 0
        var bestCount = -1
        for (i <- mat.indices) {
            val cnt = mat(i).count(_ == 1)
            if (cnt > bestCount) {
                bestCount = cnt
                bestRow = i
            }
        }
        Array(bestRow, bestCount)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn row_and_maximum_ones(mat: Vec<Vec<i32>>) -> Vec<i32> {
        let mut best_row = 0usize;
        let mut best_cnt = 0usize;
        for (i, row) in mat.iter().enumerate() {
            let cnt = row.iter().filter(|&&x| x == 1).count();
            if cnt > best_cnt {
                best_cnt = cnt;
                best_row = i;
            }
        }
        vec![best_row as i32, best_cnt as i32]
    }
}
```

## Racket

```racket
(define/contract (row-and-maximum-ones mat)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  (let loop ((rows mat) (idx 0) (best-idx -1) (best-count -1))
    (if (null? rows)
        (list best-idx best-count)
        (let* ((row (car rows))
               (cnt (foldl + 0 row)))
          (if (> cnt best-count)
              (loop (cdr rows) (+ idx 1) idx cnt)
              (loop (cdr rows) (+ idx 1) best-idx best-count))))))
```

## Erlang

```erlang
-spec row_and_maximum_ones(Mat :: [[integer()]]) -> [integer()].
row_and_maximum_ones(Mat) ->
    {Idx, Count} = row_and_maximum_ones(Mat, 0, -1, -1),
    [Idx, Count].

row_and_maximum_ones([], _CurrIdx, BestIdx, BestCnt) ->
    {BestIdx, BestCnt};
row_and_maximum_ones([Row|Rest], CurrIdx, BestIdx, BestCnt) ->
    Ones = count_ones(Row),
    if
        Ones > BestCnt ->
            row_and_maximum_ones(Rest, CurrIdx + 1, CurrIdx, Ones);
        true ->
            row_and_maximum_ones(Rest, CurrIdx + 1, BestIdx, BestCnt)
    end.

count_ones(Row) ->
    length([X || X <- Row, X =:= 1]).
```

## Elixir

```elixir
defmodule Solution do
  @spec row_and_maximum_ones(mat :: [[integer]]) :: [integer]
  def row_and_maximum_ones(mat) do
    {best_idx, best_cnt} =
      mat
      |> Enum.with_index()
      |> Enum.reduce({0, -1}, fn {row, idx}, {cur_idx, cur_cnt} ->
        cnt = Enum.count(row, &(&1 == 1))

        if cnt > cur_cnt do
          {idx, cnt}
        else
          {cur_idx, cur_cnt}
        end
      end)

    [best_idx, best_cnt]
  end
end
```
