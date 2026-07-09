# 1901. Find a Peak Element II

## Cpp

```cpp
class Solution {
public:
    vector<int> findPeakGrid(vector<vector<int>>& mat) {
        int m = mat.size();
        int n = mat[0].size();
        int left = 0, right = n - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            // find row with max element in column mid
            int maxRow = 0;
            for (int i = 1; i < m; ++i) {
                if (mat[i][mid] > mat[maxRow][mid]) {
                    maxRow = i;
                }
            }
            int leftVal = (mid - 1 >= 0) ? mat[maxRow][mid - 1] : -1;
            int rightVal = (mid + 1 < n) ? mat[maxRow][mid + 1] : -1;
            int cur = mat[maxRow][mid];
            if (cur > leftVal && cur > rightVal) {
                return {maxRow, mid};
            } else if (leftVal > cur) {
                right = mid - 1;
            } else { // rightVal > cur
                left = mid + 1;
            }
        }
        return {}; // should never reach here
    }
};
```

## Java

```java
class Solution {
    public int[] findPeakGrid(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;
        int left = 0, right = n - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            // Find the row with maximum element in column mid
            int maxRow = 0;
            for (int i = 1; i < m; i++) {
                if (mat[i][mid] > mat[maxRow][mid]) {
                    maxRow = i;
                }
            }
            int leftVal = (mid - 1 >= 0) ? mat[maxRow][mid - 1] : -1;
            int rightVal = (mid + 1 < n) ? mat[maxRow][mid + 1] : -1;
            int cur = mat[maxRow][mid];
            if (cur > leftVal && cur > rightVal) {
                return new int[]{maxRow, mid};
            } else if (rightVal > cur) {
                left = mid + 1;
            } else { // leftVal > cur
                right = mid - 1;
            }
        }
        // Should never reach here due to problem guarantees
        return new int[]{0, 0};
    }
}
```

## Python

```python
class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        m = len(mat)
        n = len(mat[0])
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            # find row with max element in column mid
            max_row = 0
            for i in range(1, m):
                if mat[i][mid] > mat[max_row][mid]:
                    max_row = i
            left_val = mat[max_row][mid - 1] if mid - 1 >= 0 else -1
            right_val = mat[max_row][mid + 1] if mid + 1 < n else -1
            cur = mat[max_row][mid]
            if cur > left_val and cur > right_val:
                return [max_row, mid]
            elif left_val > cur:
                right = mid - 1
            else:  # right_val > cur
                left = mid + 1
        return []
```

## Python3

```python
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        left, right = 0, n - 1
        while True:
            mid = (left + right) // 2
            # Find row with max element in column mid
            max_row = 0
            for i in range(1, m):
                if mat[i][mid] > mat[max_row][mid]:
                    max_row = i
            cur = mat[max_row][mid]
            left_val = mat[max_row][mid - 1] if mid - 1 >= 0 else -1
            right_val = mat[max_row][mid + 1] if mid + 1 < n else -1

            if cur > left_val and cur > right_val:
                return [max_row, mid]
            elif left_val > cur:
                right = mid - 1
            else:  # right_val > cur
                left = mid + 1
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findPeakGrid(int** mat, int matSize, int* matColSize, int* returnSize) {
    int m = matSize;
    int n = matColSize[0];
    int left = 0, right = n - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        // Find the row with maximum value in column mid
        int maxRow = 0;
        for (int i = 1; i < m; ++i) {
            if (mat[i][mid] > mat[maxRow][mid]) {
                maxRow = i;
            }
        }

        int cur = mat[maxRow][mid];
        int leftVal = (mid - 1 >= 0) ? mat[maxRow][mid - 1] : -1;
        int rightVal = (mid + 1 < n) ? mat[maxRow][mid + 1] : -1;

        if (cur > leftVal && cur > rightVal) {
            int* ans = (int*)malloc(2 * sizeof(int));
            ans[0] = maxRow;
            ans[1] = mid;
            *returnSize = 2;
            return ans;
        } else if (leftVal > cur) {
            right = mid - 1;
        } else { // rightVal > cur
            left = mid + 1;
        }
    }

    // Should never reach here because a peak always exists
    *returnSize = 0;
    return NULL;
}
```

## Csharp

```csharp
public class Solution {
    public int[] FindPeakGrid(int[][] mat) {
        int m = mat.Length;
        int n = mat[0].Length;
        int left = 0, right = n - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            // Find the row with maximum element in column mid
            int maxRow = 0;
            for (int i = 1; i < m; i++) {
                if (mat[i][mid] > mat[maxRow][mid]) {
                    maxRow = i;
                }
            }

            int leftVal = (mid - 1 >= 0) ? mat[maxRow][mid - 1] : -1;
            int rightVal = (mid + 1 < n) ? mat[maxRow][mid + 1] : -1;
            int curVal = mat[maxRow][mid];

            if (curVal > leftVal && curVal > rightVal) {
                return new int[] { maxRow, mid };
            } else if (leftVal > curVal) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        // Should never reach here as a peak always exists
        return new int[0];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} mat
 * @return {number[]}
 */
var findPeakGrid = function(mat) {
    const m = mat.length;
    const n = mat[0].length;
    let left = 0, right = n - 1;
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        // Find the row with maximum value in column mid
        let maxRow = 0;
        for (let i = 1; i < m; i++) {
            if (mat[i][mid] > mat[maxRow][mid]) {
                maxRow = i;
            }
        }
        const cur = mat[maxRow][mid];
        const leftVal = mid - 1 >= 0 ? mat[maxRow][mid - 1] : -1;
        const rightVal = mid + 1 < n ? mat[maxRow][mid + 1] : -1;

        if (cur > leftVal && cur > rightVal) {
            return [maxRow, mid];
        } else if (rightVal > cur) {
            left = mid + 1;
        } else { // leftVal > cur
            right = mid - 1;
        }
    }
    // Fallback (should never be reached)
    return [0, 0];
};
```

## Typescript

```typescript
function findPeakGrid(mat: number[][]): number[] {
    const m = mat.length;
    const n = mat[0].length;
    let left = 0, right = n - 1;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        // Find the row index of the maximum element in column mid
        let maxRow = 0;
        for (let i = 1; i < m; i++) {
            if (mat[i][mid] > mat[maxRow][mid]) {
                maxRow = i;
            }
        }

        const leftVal = mid - 1 >= 0 ? mat[maxRow][mid - 1] : -1;
        const rightVal = mid + 1 < n ? mat[maxRow][mid + 1] : -1;
        const curVal = mat[maxRow][mid];

        if (curVal > leftVal && curVal > rightVal) {
            return [maxRow, mid];
        } else if (rightVal > curVal) {
            left = mid + 1;
        } else { // leftVal > curVal
            right = mid - 1;
        }
    }

    // Fallback (should never be reached with valid input)
    return [0, 0];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $mat
     * @return Integer[]
     */
    function findPeakGrid($mat) {
        $m = count($mat);
        $n = count($mat[0]);
        $left = 0;
        $right = $n - 1;

        while ($left <= $right) {
            $mid = intdiv($left + $right, 2);

            // Find the row with maximum value in column mid
            $maxRow = 0;
            for ($i = 1; $i < $m; $i++) {
                if ($mat[$i][$mid] > $mat[$maxRow][$mid]) {
                    $maxRow = $i;
                }
            }

            $leftVal = ($mid - 1 >= 0) ? $mat[$maxRow][$mid - 1] : -1;
            $rightVal = ($mid + 1 < $n) ? $mat[$maxRow][$mid + 1] : -1;

            if ($mat[$maxRow][$mid] > $leftVal && $mat[$maxRow][$mid] > $rightVal) {
                return [$maxRow, $mid];
            } elseif ($rightVal > $mat[$maxRow][$mid]) {
                $left = $mid + 1;
            } else { // left neighbor is greater
                $right = $mid - 1;
            }
        }

        // Fallback (should never be reached due to problem guarantees)
        return [0, 0];
    }
}
```

## Swift

```swift
class Solution {
    func findPeakGrid(_ mat: [[Int]]) -> [Int] {
        let m = mat.count
        let n = mat[0].count
        var left = 0
        var right = n - 1
        
        while left <= right {
            let mid = (left + right) / 2
            
            // Find the row with maximum element in column mid
            var maxRow = 0
            var maxVal = mat[0][mid]
            for i in 1..<m {
                if mat[i][mid] > maxVal {
                    maxVal = mat[i][mid]
                    maxRow = i
                }
            }
            
            let leftVal = mid - 1 >= 0 ? mat[maxRow][mid - 1] : -1
            let rightVal = mid + 1 < n ? mat[maxRow][mid + 1] : -1
            
            if maxVal > leftVal && maxVal > rightVal {
                return [maxRow, mid]
            } else if leftVal > maxVal {
                right = mid - 1
            } else {
                left = mid + 1
            }
        }
        
        // Should never reach here due to problem guarantees
        return []
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findPeakGrid(mat: Array<IntArray>): IntArray {
        val m = mat.size
        val n = mat[0].size
        var left = 0
        var right = n - 1
        while (left <= right) {
            val mid = (left + right) ushr 1
            var maxRow = 0
            for (i in 0 until m) {
                if (mat[i][mid] > mat[maxRow][mid]) {
                    maxRow = i
                }
            }
            val leftVal = if (mid - 1 >= 0) mat[maxRow][mid - 1] else -1
            val rightVal = if (mid + 1 < n) mat[maxRow][mid + 1] else -1
            val cur = mat[maxRow][mid]
            if (cur > leftVal && cur > rightVal) {
                return intArrayOf(maxRow, mid)
            } else if (rightVal > cur) {
                left = mid + 1
            } else {
                right = mid - 1
            }
        }
        return intArrayOf(0, 0)
    }
}
```

## Dart

```dart
class Solution {
  List<int> findPeakGrid(List<List<int>> mat) {
    int m = mat.length;
    int n = mat[0].length;
    int left = 0, right = n - 1;

    while (left <= right) {
      int mid = left + ((right - left) >> 1);
      // Find the row with maximum element in column mid
      int maxRow = 0;
      for (int i = 1; i < m; i++) {
        if (mat[i][mid] > mat[maxRow][mid]) {
          maxRow = i;
        }
      }

      int leftVal = (mid - 1 >= 0) ? mat[maxRow][mid - 1] : -1;
      int rightVal = (mid + 1 < n) ? mat[maxRow][mid + 1] : -1;

      if (mat[maxRow][mid] > leftVal && mat[maxRow][mid] > rightVal) {
        return [maxRow, mid];
      } else if (rightVal > mat[maxRow][mid]) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }

    // Fallback (should never be reached due to problem guarantees)
    return [0, 0];
  }
}
```

## Golang

```go
func findPeakGrid(mat [][]int) []int {
	m, n := len(mat), len(mat[0])
	low, high := 0, n-1
	for low <= high {
		mid := (low + high) / 2
		maxRow := 0
		for i := 1; i < m; i++ {
			if mat[i][mid] > mat[maxRow][mid] {
				maxRow = i
			}
		}
		leftVal, rightVal := -1, -1
		if mid-1 >= 0 {
			leftVal = mat[maxRow][mid-1]
		}
		if mid+1 < n {
			rightVal = mat[maxRow][mid+1]
		}
		cur := mat[maxRow][mid]
		if cur > leftVal && cur > rightVal {
			return []int{maxRow, mid}
		} else if leftVal > cur {
			high = mid - 1
		} else {
			low = mid + 1
		}
	}
	return []int{}
}
```

## Ruby

```ruby
def find_peak_grid(mat)
  m = mat.length
  n = mat[0].length
  left = 0
  right = n - 1

  while left <= right
    mid = (left + right) / 2

    # Find the row with maximum value in column mid
    max_row = 0
    (0...m).each do |i|
      max_row = i if mat[i][mid] > mat[max_row][mid]
    end

    left_val = mid - 1 >= 0 ? mat[max_row][mid - 1] : -1
    right_val = mid + 1 < n ? mat[max_row][mid + 1] : -1
    cur = mat[max_row][mid]

    if cur > left_val && cur > right_val
      return [max_row, mid]
    elsif left_val > cur
      right = mid - 1
    else
      left = mid + 1
    end
  end
end
```

## Scala

```scala
object Solution {
    def findPeakGrid(mat: Array[Array[Int]]): Array[Int] = {
        val m = mat.length
        val n = mat(0).length
        var lo = 0
        var hi = n - 1

        while (lo <= hi) {
            val mid = lo + (hi - lo) / 2

            // Find the row index of the maximum element in column mid
            var maxRow = 0
            var i = 1
            while (i < m) {
                if (mat(i)(mid) > mat(maxRow)(mid)) maxRow = i
                i += 1
            }

            val leftVal = if (mid - 1 >= 0) mat(maxRow)(mid - 1) else -1
            val rightVal = if (mid + 1 < n) mat(maxRow)(mid + 1) else -1
            val cur = mat(maxRow)(mid)

            if (cur > leftVal && cur > rightVal) {
                return Array(maxRow, mid)
            } else if (leftVal > cur) {
                hi = mid - 1
            } else {
                lo = mid + 1
            }
        }

        // Fallback (should never be reached due to problem guarantees)
        Array(0, 0)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_peak_grid(mat: Vec<Vec<i32>>) -> Vec<i32> {
        let m = mat.len();
        let n = mat[0].len();
        let mut left = 0usize;
        let mut right = n - 1;
        while left <= right {
            let mid = (left + right) / 2;
            // Find the row with maximum value in column mid
            let mut max_row = 0usize;
            for i in 1..m {
                if mat[i][mid] > mat[max_row][mid] {
                    max_row = i;
                }
            }
            let cur = mat[max_row][mid];
            let left_val = if mid == 0 { -1 } else { mat[max_row][mid - 1] };
            let right_val = if mid + 1 >= n { -1 } else { mat[max_row][mid + 1] };
            if cur > left_val && cur > right_val {
                return vec![max_row as i32, mid as i32];
            } else if left_val > cur {
                // Move to the left half
                if mid == 0 {
                    break;
                }
                right = mid - 1;
            } else {
                // Move to the right half
                left = mid + 1;
            }
        }
        // Fallback (should never be reached with valid input)
        vec![0, 0]
    }
}
```

## Racket

```racket
(define/contract (find-peak-grid mat)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ((m (length mat))
         (n (if (= m 0) 0 (length (car mat)))))
    (let recur ((left 0) (right (- n 1)))
      (let ((mid (quotient (+ left right) 2)))
        ;; find row with maximum value in column mid
        (define max-row
          (let loop ((i 0)
                     (best-i 0)
                     (best-val (list-ref (list-ref mat 0) mid)))
            (if (= i m)
                best-i
                (let ((val (list-ref (list-ref mat i) mid)))
                  (if (> val best-val)
                      (loop (+ i 1) i val)
                      (loop (+ i 1) best-i best-val))))))
        (define cur-val (list-ref (list-ref mat max-row) mid))
        (define left-val
          (if (= mid 0)
              -1
              (list-ref (list-ref mat max-row) (- mid 1))))
        (define right-val
          (if (= mid (- n 1))
              -1
              (list-ref (list-ref mat max-row) (+ mid 1))))
        (cond ((and (> cur-val left-val) (> cur-val right-val))
               (list max-row mid))
              ((> left-val cur-val)
               (recur left (- mid 1)))
              (else
               (recur (+ mid 1) right)))))))
```

## Erlang

```erlang
-module(solution).
-export([find_peak_grid/1]).

-spec find_peak_grid(Mat :: [[integer()]]) -> [integer()].
find_peak_grid([]) ->
    [];
find_peak_grid(Mat) ->
    N = length(hd(Mat)),
    bin_search(Mat, 0, N - 1).

%% binary search on columns
bin_search(_Mat, Low, High) when Low > High ->
    []; % should not happen
bin_search(Mat, Low, High) ->
    Mid = (Low + High) div 2,
    {MaxRow, MaxVal} = find_max_in_column(Mat, Mid),
    LeftVal = case Mid of
                  0 -> -1;
                  _ -> get(Mat, MaxRow, Mid - 1)
              end,
    RightVal = case Mid of
                   N when N =:= length(hd(Mat)) - 1 -> -1;
                   _ -> get(Mat, MaxRow, Mid + 1)
               end,
    case {MaxVal > LeftVal, MaxVal > RightVal} of
        {true, true} ->
            [MaxRow, Mid];
        {false, _} when LeftVal > MaxVal ->
            bin_search(Mat, Low, Mid - 1);
        _ ->
            bin_search(Mat, Mid + 1, High)
    end.

%% get element at (I,J) zero‑based
get(Mat, I, J) ->
    Row = lists:nth(I + 1, Mat),
    lists:nth(J + 1, Row).

%% find max value in column ColIdx, return {RowIdx, Value}
find_max_in_column(Mat, ColIdx) ->
    find_max_in_column(Mat, ColIdx, 0, -1, -1).

find_max_in_column([], _ColIdx, _RowIdx, MaxRow, MaxVal) ->
    {MaxRow, MaxVal};
find_max_in_column([Row | Rest], ColIdx, RowIdx, MaxRow, MaxVal) ->
    Val = lists:nth(ColIdx + 1, Row),
    if
        Val > MaxVal ->
            find_max_in_column(Rest, ColIdx, RowIdx + 1, RowIdx, Val);
        true ->
            find_max_in_column(Rest, ColIdx, RowIdx + 1, MaxRow, MaxVal)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_peak_grid(mat :: [[integer]]) :: [integer]
  def find_peak_grid(mat) do
    m = length(mat)
    n = length(List.first(mat))
    binary_search(0, n - 1, mat, m, n)
  end

  defp binary_search(left, right, _mat, _m, _n) when left > right, do: []

  defp binary_search(left, right, mat, m, n) do
    mid = div(left + right, 2)

    # find the row with maximum value in column mid
    {max_row, _} =
      Enum.with_index(mat)
      |> Enum.reduce({0, elem(Enum.at(mat, 0), mid)}, fn {row, idx}, {cur_max_idx, cur_max_val} ->
        val = Enum.at(row, mid)

        if val > cur_max_val do
          {idx, val}
        else
          {cur_max_idx, cur_max_val}
        end
      end)

    cur = Enum.at(Enum.at(mat, max_row), mid)
    left_val = if mid - 1 >= 0, do: Enum.at(Enum.at(mat, max_row), mid - 1), else: -1
    right_val = if mid + 1 < n, do: Enum.at(Enum.at(mat, max_row), mid + 1), else: -1

    cond do
      cur > left_val and cur > right_val ->
        [max_row, mid]

      left_val > cur ->
        binary_search(left, mid - 1, mat, m, n)

      true ->
        binary_search(mid + 1, right, mat, m, n)
    end
  end
end
```
