# 2679. Sum in a Matrix

## Cpp

```cpp
class Solution {
public:
    int matrixSum(vector<vector<int>>& nums) {
        int maxCols = 0;
        for (auto& row : nums) {
            sort(row.begin(), row.end(), greater<int>());
            if ((int)row.size() > maxCols) maxCols = row.size();
        }
        long long ans = 0;
        for (int col = 0; col < maxCols; ++col) {
            int curMax = 0;
            for (auto& row : nums) {
                if (col < (int)row.size()) {
                    curMax = max(curMax, row[col]);
                }
            }
            ans += curMax;
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int matrixSum(int[][] nums) {
        for (int[] row : nums) {
            java.util.Arrays.sort(row);
        }
        int rows = nums.length;
        int cols = nums[0].length;
        int total = 0;
        for (int c = 0; c < cols; c++) {
            int maxVal = 0;
            for (int r = 0; r < rows; r++) {
                int val = nums[r][cols - 1 - c];
                if (val > maxVal) {
                    maxVal = val;
                }
            }
            total += maxVal;
        }
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def matrixSum(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        sorted_rows = [sorted(row, reverse=True) for row in nums]
        return sum(max(col) for col in zip(*sorted_rows))
```

## Python3

```python
from typing import List

class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        # Sort each row in descending order
        for row in nums:
            row.sort(reverse=True)
        # Sum the maximum of each column
        total = 0
        # Assuming all rows have the same length
        for col_vals in zip(*nums):
            total += max(col_vals)
        return total
```

## C

```c
#include <stdlib.h>

static int cmpDesc(const void *a, const void *b) {
    return *(const int *)b - *(const int *)a;
}

int matrixSum(int** nums, int numsSize, int* numsColSize) {
    if (numsSize == 0) return 0;

    int maxCols = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (numsColSize[i] > maxCols) maxCols = numsColSize[i];
        qsort(nums[i], numsColSize[i], sizeof(int), cmpDesc);
    }

    int total = 0;
    for (int col = 0; col < maxCols; ++col) {
        int colMax = 0;
        for (int row = 0; row < numsSize; ++row) {
            if (numsColSize[row] > col && nums[row][col] > colMax) {
                colMax = nums[row][col];
            }
        }
        total += colMax;
    }

    return total;
}
```

## Csharp

```csharp
public class Solution {
    public int MatrixSum(int[][] nums) {
        int maxLen = 0;
        foreach (var row in nums) {
            if (row.Length > maxLen) maxLen = row.Length;
            Array.Sort(row, (a, b) => b.CompareTo(a));
        }
        int result = 0;
        for (int col = 0; col < maxLen; ++col) {
            int best = 0;
            foreach (var row in nums) {
                if (col < row.Length && row[col] > best) {
                    best = row[col];
                }
            }
            result += best;
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} nums
 * @return {number}
 */
var matrixSum = function(nums) {
    // Sort each row in descending order
    for (let i = 0; i < nums.length; i++) {
        nums[i].sort((a, b) => b - a);
    }
    
    // Find the maximum row length
    let maxLen = 0;
    for (const row of nums) {
        if (row.length > maxLen) maxLen = row.length;
    }
    
    // Sum the maximum element of each column
    let total = 0;
    for (let col = 0; col < maxLen; col++) {
        let mx = 0;
        for (let i = 0; i < nums.length; i++) {
            if (col < nums[i].length && nums[i][col] > mx) {
                mx = nums[i][col];
            }
        }
        total += mx;
    }
    
    return total;
};
```

## Typescript

```typescript
function matrixSum(nums: number[][]): number {
    // Sort each row in descending order
    for (const row of nums) {
        row.sort((a, b) => b - a);
    }
    
    const m = nums.length;
    const n = nums[0].length;
    let total = 0;
    
    for (let col = 0; col < n; col++) {
        let maxVal = 0;
        for (let i = 0; i < m; i++) {
            if (nums[i][col] > maxVal) {
                maxVal = nums[i][col];
            }
        }
        total += maxVal;
    }
    
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $nums
     * @return Integer
     */
    function matrixSum($nums) {
        foreach ($nums as &$row) {
            rsort($row);
        }
        unset($row);
        $n = count($nums);
        if ($n === 0) return 0;
        $m = count($nums[0]);
        $ans = 0;
        for ($j = 0; $j < $m; $j++) {
            $maxVal = 0;
            foreach ($nums as $row) {
                if ($row[$j] > $maxVal) {
                    $maxVal = $row[$j];
                }
            }
            $ans += $maxVal;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func matrixSum(_ nums: [[Int]]) -> Int {
        var rows = nums.map { $0.sorted(by: >) }
        guard let firstRow = rows.first else { return 0 }
        let m = firstRow.count
        var total = 0
        for col in 0..<m {
            var maxVal = 0
            for row in rows {
                if row[col] > maxVal {
                    maxVal = row[col]
                }
            }
            total += maxVal
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun matrixSum(nums: Array<IntArray>): Int {
        val m = nums.size
        if (m == 0) return 0
        val n = nums[0].size
        for (row in nums) {
            row.sort()
        }
        var ans = 0
        for (j in 0 until n) {
            var colMax = 0
            for (i in 0 until m) {
                val value = nums[i][n - 1 - j]
                if (value > colMax) colMax = value
            }
            ans += colMax
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int matrixSum(List<List<int>> nums) {
    for (var row in nums) {
      row.sort((a, b) => b - a);
    }
    int rows = nums.length;
    int cols = nums[0].length;
    int total = 0;
    for (int c = 0; c < cols; ++c) {
      int maxVal = 0;
      for (int r = 0; r < rows; ++r) {
        if (nums[r][c] > maxVal) {
          maxVal = nums[r][c];
        }
      }
      total += maxVal;
    }
    return total;
  }
}
```

## Golang

```go
import "sort"

func matrixSum(nums [][]int) int {
	for _, row := range nums {
		sort.Slice(row, func(i, j int) bool { return row[i] > row[j] })
	}
	maxCols := 0
	for _, row := range nums {
		if len(row) > maxCols {
			maxCols = len(row)
		}
	}
	ans := 0
	for col := 0; col < maxCols; col++ {
		curMax := 0
		for _, row := range nums {
			if col < len(row) && row[col] > curMax {
				curMax = row[col]
			}
		}
		ans += curMax
	}
	return ans
}
```

## Ruby

```ruby
def matrix_sum(nums)
  nums.each { |row| row.sort!.reverse! }
  cols = nums[0].size
  total = 0
  (0...cols).each do |c|
    max_val = 0
    nums.each do |row|
      val = row[c]
      max_val = val if val > max_val
    end
    total += max_val
  end
  total
end
```

## Scala

```scala
object Solution {
  def matrixSum(nums: Array[Array[Int]]): Int = {
    if (nums.isEmpty) return 0
    val cols = nums(0).length
    val maxVals = new Array[Int](cols)
    for (row <- nums) {
      val sorted = row.sorted(Ordering[Int].reverse)
      var j = 0
      while (j < cols) {
        if (sorted(j) > maxVals(j)) maxVals(j) = sorted(j)
        j += 1
      }
    }
    var sum = 0
    var i = 0
    while (i < cols) {
      sum += maxVals(i)
      i += 1
    }
    sum
  }
}
```

## Rust

```rust
impl Solution {
    pub fn matrix_sum(mut nums: Vec<Vec<i32>>) -> i32 {
        for row in nums.iter_mut() {
            row.sort_unstable_by(|a, b| b.cmp(a));
        }
        let max_len = nums.iter().map(|r| r.len()).max().unwrap_or(0);
        let mut ans = 0;
        for col in 0..max_len {
            let mut col_max = 0;
            for row in &nums {
                if col < row.len() && row[col] > col_max {
                    col_max = row[col];
                }
            }
            ans += col_max;
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (matrix-sum nums)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((sorted-rows (map (lambda (row) (sort row >)) nums))
         (col-count (if (null? sorted-rows) 0 (length (car sorted-rows)))))
    (let loop ((j 0) (acc 0))
      (if (= j col-count)
          acc
          (let ((max-val (apply max (map (lambda (row) (list-ref row j)) sorted-rows))))
            (loop (+ j 1) (+ acc max-val)))))))
```

## Erlang

```erlang
-spec matrix_sum(Nums :: [[integer()]]) -> integer().
matrix_sum(Nums) ->
    MaxLen = lists:max([length(Row) || Row <- Nums]),
    sum_columns(0, MaxLen - 1, Nums, 0).

sum_columns(CurIdx, MaxIdx, _Rows, Acc) when CurIdx > MaxIdx ->
    Acc;
sum_columns(CurIdx, MaxIdx, Rows, Acc) ->
    ColMax = max_in_column(CurIdx, Rows, 0),
    sum_columns(CurIdx + 1, MaxIdx, Rows, Acc + ColMax).

max_in_column(_Idx, [], Max) ->
    Max;
max_in_column(Idx, [Row | Rest], Max) ->
    case Idx < length(Row) of
        true ->
            Val = lists:nth(Idx + 1, Row),
            NewMax = if Val > Max -> Val; true -> Max end,
            max_in_column(Idx, Rest, NewMax);
        false ->
            max_in_column(Idx, Rest, Max)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec matrix_sum(nums :: [[integer]]) :: integer
  def matrix_sum(nums) do
    sorted_rows = Enum.map(nums, &Enum.sort(&1, :desc))
    n = sorted_rows |> hd() |> length()

    0..(n - 1)
    |> Enum.reduce(0, fn j, acc ->
      max_val =
        sorted_rows
        |> Enum.map(fn row -> Enum.at(row, j) end)
        |> Enum.max()

      acc + max_val
    end)
  end
end
```
