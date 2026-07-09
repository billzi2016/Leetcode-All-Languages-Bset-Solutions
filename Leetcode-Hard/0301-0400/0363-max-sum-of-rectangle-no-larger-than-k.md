# 0363. Max Sum of Rectangle No Larger Than K

## Cpp

```cpp
class Solution {
public:
    int maxSumSubmatrix(vector<vector<int>>& matrix, int k) {
        int rows = matrix.size();
        int cols = matrix[0].size();
        int ans = INT_MIN;
        
        if (rows <= cols) {
            // iterate over left and right columns
            for (int left = 0; left < cols; ++left) {
                vector<int> sums(rows, 0);
                for (int right = left; right < cols; ++right) {
                    for (int i = 0; i < rows; ++i)
                        sums[i] += matrix[i][right];
                    
                    set<long long> prefix;
                    prefix.insert(0);
                    long long cur = 0;
                    for (int v : sums) {
                        cur += v;
                        auto it = prefix.lower_bound(cur - k);
                        if (it != prefix.end())
                            ans = max(ans, int(cur - *it));
                        prefix.insert(cur);
                    }
                }
            }
        } else {
            // iterate over top and bottom rows
            for (int top = 0; top < rows; ++top) {
                vector<int> sums(cols, 0);
                for (int bottom = top; bottom < rows; ++bottom) {
                    for (int j = 0; j < cols; ++j)
                        sums[j] += matrix[bottom][j];
                    
                    set<long long> prefix;
                    prefix.insert(0);
                    long long cur = 0;
                    for (int v : sums) {
                        cur += v;
                        auto it = prefix.lower_bound(cur - k);
                        if (it != prefix.end())
                            ans = max(ans, int(cur - *it));
                        prefix.insert(cur);
                    }
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxSumSubmatrix(int[][] matrix, int k) {
        int m = matrix.length;
        int n = matrix[0].length;
        int result = Integer.MIN_VALUE;

        if (m <= n) {
            // Iterate over pairs of rows
            for (int top = 0; top < m; top++) {
                int[] colSums = new int[n];
                for (int bottom = top; bottom < m; bottom++) {
                    for (int c = 0; c < n; c++) {
                        colSums[c] += matrix[bottom][c];
                    }
                    result = Math.max(result, maxSubArrayNoMoreThanK(colSums, k));
                    if (result == k) return k; // early exit
                }
            }
        } else {
            // Iterate over pairs of columns
            for (int left = 0; left < n; left++) {
                int[] rowSums = new int[m];
                for (int right = left; right < n; right++) {
                    for (int r = 0; r < m; r++) {
                        rowSums[r] += matrix[r][right];
                    }
                    result = Math.max(result, maxSubArrayNoMoreThanK(rowSums, k));
                    if (result == k) return k;
                }
            }
        }

        return result;
    }

    private int maxSubArrayNoMoreThanK(int[] nums, int k) {
        java.util.TreeSet<Integer> set = new java.util.TreeSet<>();
        set.add(0);
        int curSum = 0;
        int best = Integer.MIN_VALUE;
        for (int num : nums) {
            curSum += num;
            Integer target = set.ceiling(curSum - k);
            if (target != null) {
                best = Math.max(best, curSum - target);
                if (best == k) return k; // early exit
            }
            set.add(curSum);
        }
        return best;
    }
}
```

## Python

```python
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import bisect

        m, n = len(matrix), len(matrix[0])
        # Ensure we iterate over the smaller dimension for rows
        if m > n:
            matrix = [list(row) for row in zip(*matrix)]
            m, n = n, m

        max_sum = float('-inf')
        for top in range(m):
            col_sums = [0] * n
            for bottom in range(top, m):
                for c in range(n):
                    col_sums[c] += matrix[bottom][c]

                # Find the max subarray sum no larger than k using prefix sums + BST (bisect)
                prefix = [0]
                cur_sum = 0
                cur_max = float('-inf')
                for val in col_sums:
                    cur_sum += val
                    target = cur_sum - k
                    idx = bisect.bisect_left(prefix, target)
                    if idx < len(prefix):
                        cur_max = max(cur_max, cur_sum - prefix[idx])
                    bisect.insort(prefix, cur_sum)

                max_sum = max(max_sum, cur_max)
                if max_sum == k:
                    return k
        return int(max_sum)
```

## Python3

```python
from bisect import bisect_left, insort
from typing import List

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        # Ensure we iterate over the smaller dimension for columns
        if rows > cols:
            matrix = [list(row) for row in zip(*matrix)]
            rows, cols = cols, rows

        max_sum = -float('inf')
        for left in range(cols):
            row_sums = [0] * rows
            for right in range(left, cols):
                for i in range(rows):
                    row_sums[i] += matrix[i][right]

                # Find the max subarray sum no larger than k using prefix sums + BST (sorted list)
                prefix = [0]
                cur_sum = 0
                cur_max = -float('inf')
                for val in row_sums:
                    cur_sum += val
                    target = cur_sum - k
                    idx = bisect_left(prefix, target)
                    if idx < len(prefix):
                        cur_max = max(cur_max, cur_sum - prefix[idx])
                    insort(prefix, cur_sum)

                max_sum = max(max_sum, cur_max)
                if max_sum == k:
                    return k
        return int(max_sum)
```

## C

```c
#include <limits.h>
#include <string.h>

int maxSumSubmatrix(int** matrix, int matrixSize, int* matrixColSize, int k) {
    int rows = matrixSize;
    int cols = matrixColSize[0];
    int maxSum = INT_MIN;

    if (rows <= cols) {
        // Iterate over pairs of rows
        for (int top = 0; top < rows; ++top) {
            int colSums[cols];
            memset(colSums, 0, sizeof(int) * cols);
            for (int bottom = top; bottom < rows; ++bottom) {
                for (int c = 0; c < cols; ++c)
                    colSums[c] += matrix[bottom][c];

                long long sorted[cols + 1];
                int sortedSize = 1;
                sorted[0] = 0;
                int prefix = 0;

                for (int c = 0; c < cols; ++c) {
                    prefix += colSums[c];
                    int target = prefix - k;

                    // lower_bound for target
                    int l = 0, r = sortedSize;
                    while (l < r) {
                        int m = (l + r) >> 1;
                        if (sorted[m] >= target)
                            r = m;
                        else
                            l = m + 1;
                    }
                    if (l < sortedSize) {
                        int cur = prefix - (int)sorted[l];
                        if (cur > maxSum) {
                            maxSum = cur;
                            if (maxSum == k)
                                return k;
                        }
                    }

                    // insert current prefix
                    l = 0, r = sortedSize;
                    while (l < r) {
                        int m = (l + r) >> 1;
                        if (sorted[m] >= prefix)
                            r = m;
                        else
                            l = m + 1;
                    }
                    memmove(&sorted[l + 1], &sorted[l],
                            sizeof(long long) * (sortedSize - l));
                    sorted[l] = prefix;
                    ++sortedSize;
                }
            }
        }
    } else {
        // Iterate over pairs of columns
        for (int left = 0; left < cols; ++left) {
            int rowSums[rows];
            memset(rowSums, 0, sizeof(int) * rows);
            for (int right = left; right < cols; ++right) {
                for (int r = 0; r < rows; ++r)
                    rowSums[r] += matrix[r][right];

                long long sorted[rows + 1];
                int sortedSize = 1;
                sorted[0] = 0;
                int prefix = 0;

                for (int r = 0; r < rows; ++r) {
                    prefix += rowSums[r];
                    int target = prefix - k;

                    // lower_bound for target
                    int l = 0, rr = sortedSize;
                    while (l < rr) {
                        int m = (l + rr) >> 1;
                        if (sorted[m] >= target)
                            rr = m;
                        else
                            l = m + 1;
                    }
                    if (l < sortedSize) {
                        int cur = prefix - (int)sorted[l];
                        if (cur > maxSum) {
                            maxSum = cur;
                            if (maxSum == k)
                                return k;
                        }
                    }

                    // insert current prefix
                    l = 0, rr = sortedSize;
                    while (l < rr) {
                        int m = (l + rr) >> 1;
                        if (sorted[m] >= prefix)
                            rr = m;
                        else
                            l = m + 1;
                    }
                    memmove(&sorted[l + 1], &sorted[l],
                            sizeof(long long) * (sortedSize - l));
                    sorted[l] = prefix;
                    ++sortedSize;
                }
            }
        }
    }

    return maxSum;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MaxSumSubmatrix(int[][] matrix, int k) {
        int rows = matrix.Length;
        int cols = matrix[0].Length;
        // Ensure we iterate over the smaller dimension for outer loops
        bool transposed = false;
        if (rows > cols) {
            // Transpose matrix to make rows <= cols
            int[][] trans = new int[cols][];
            for (int i = 0; i < cols; i++) {
                trans[i] = new int[rows];
                for (int j = 0; j < rows; j++) {
                    trans[i][j] = matrix[j][i];
                }
            }
            matrix = trans;
            int temp = rows;
            rows = cols;
            cols = temp;
            transposed = true;
        }

        int maxResult = int.MinValue;

        for (int left = 0; left < cols; left++) {
            int[] sums = new int[rows];
            for (int right = left; right < cols; right++) {
                for (int i = 0; i < rows; i++) {
                    sums[i] += matrix[i][right];
                }

                // Find the max subarray no larger than k using prefix sums + sorted list
                var prefixSums = new List<int>();
                prefixSums.Add(0);
                int curSum = 0;
                for (int i = 0; i < rows; i++) {
                    curSum += sums[i];
                    int target = curSum - k;

                    // binary search for smallest prefix >= target
                    int idx = prefixSums.BinarySearch(target);
                    if (idx < 0) idx = ~idx;
                    if (idx < prefixSums.Count) {
                        int candidate = curSum - prefixSums[idx];
                        if (candidate > maxResult) {
                            maxResult = candidate;
                            if (maxResult == k) return k; // early exit
                        }
                    }

                    // insert current sum into the sorted list
                    idx = prefixSums.BinarySearch(curSum);
                    if (idx < 0) idx = ~idx;
                    prefixSums.Insert(idx, curSum);
                }
            }
        }

        return maxResult;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} matrix
 * @param {number} k
 * @return {number}
 */
var maxSumSubmatrix = function(matrix, k) {
    const m = matrix.length;
    const n = matrix[0].length;

    // Ensure we iterate over the smaller dimension for column pairs
    let rows = m, cols = n;
    let mat = matrix;
    if (m > n) {
        // Transpose matrix
        rows = n;
        cols = m;
        mat = Array.from({ length: rows }, (_, i) => 
            Array.from({ length: cols }, (_, j) => matrix[j][i])
        );
    }

    let maxAns = -Infinity;

    const lowerBound = (arr, target) => {
        let l = 0, r = arr.length;
        while (l < r) {
            const mid = (l + r) >> 1;
            if (arr[mid] < target) l = mid + 1;
            else r = mid;
        }
        return l;
    };

    for (let left = 0; left < cols; ++left) {
        const rowSums = new Array(rows).fill(0);
        for (let right = left; right < cols; ++right) {
            for (let i = 0; i < rows; ++i) {
                rowSums[i] += mat[i][right];
            }

            // Find max subarray no larger than k using prefix sums + BST logic
            const sortedPrefix = [0];
            let curSum = 0;
            for (let sum of rowSums) {
                curSum += sum;
                const target = curSum - k;
                const idx = lowerBound(sortedPrefix, target);
                if (idx < sortedPrefix.length) {
                    const candidate = curSum - sortedPrefix[idx];
                    if (candidate > maxAns) maxAns = candidate;
                    if (maxAns === k) return k; // early exit
                }
                // insert curSum into sortedPrefix
                const pos = lowerBound(sortedPrefix, curSum);
                sortedPrefix.splice(pos, 0, curSum);
            }
        }
    }

    return maxAns;
};
```

## Typescript

```typescript
function maxSumSubmatrix(matrix: number[][], k: number): number {
    const m = matrix.length;
    const n = matrix[0].length;
    let best = -Infinity;

    // Helper to process a 1D array and update best
    const process = (arr: number[]) => {
        const prefixSums: number[] = [0];
        let cur = 0;
        for (const v of arr) {
            cur += v;
            const target = cur - k;

            // lower bound search for first >= target
            let l = 0, r = prefixSums.length;
            while (l < r) {
                const mid = (l + r) >> 1;
                if (prefixSums[mid] >= target) r = mid; else l = mid + 1;
            }
            if (l < prefixSums.length) {
                const cand = cur - prefixSums[l];
                if (cand > best) best = cand;
                if (best === k) return true; // early exit
            }

            // insert cur into sorted list
            let pos = 0, hi = prefixSums.length;
            while (pos < hi) {
                const mid = (pos + hi) >> 1;
                if (prefixSums[mid] > cur) hi = mid; else pos = mid + 1;
            }
            prefixSums.splice(pos, 0, cur);
        }
        return false;
    };

    if (m <= n) {
        // compress rows
        for (let top = 0; top < m; ++top) {
            const colSum = new Array(n).fill(0);
            for (let bottom = top; bottom < m; ++bottom) {
                for (let c = 0; c < n; ++c) colSum[c] += matrix[bottom][c];
                if (process(colSum)) return k;
            }
        }
    } else {
        // compress columns
        for (let left = 0; left < n; ++left) {
            const rowSum = new Array(m).fill(0);
            for (let right = left; right < n; ++right) {
                for (let r = 0; r < m; ++r) rowSum[r] += matrix[r][right];
                if (process(rowSum)) return k;
            }
        }
    }

    return best;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $matrix
     * @param Integer $k
     * @return Integer
     */
    function maxSumSubmatrix($matrix, $k) {
        $m = count($matrix);
        $n = count($matrix[0]);

        // Ensure we iterate over the smaller dimension as columns
        if ($m > $n) {
            $transposed = [];
            for ($i = 0; $i < $n; $i++) {
                $row = [];
                for ($j = 0; $j < $m; $j++) {
                    $row[] = $matrix[$j][$i];
                }
                $transposed[] = $row;
            }
            $matrix = $transposed;
            $tmp = $m;
            $m = $n;
            $n = $tmp;
        }

        $maxSum = PHP_INT_MIN;

        for ($left = 0; $left < $n; $left++) {
            $rowSums = array_fill(0, $m, 0);
            for ($right = $left; $right < $n; $right++) {
                for ($i = 0; $i < $m; $i++) {
                    $rowSums[$i] += $matrix[$i][$right];
                }
                $currMax = $this->maxSubArrayNoLargerThanK($rowSums, $k);
                if ($currMax > $maxSum) {
                    $maxSum = $currMax;
                    if ($maxSum == $k) {
                        return $k; // early exit
                    }
                }
            }
        }

        return $maxSum;
    }

    /**
     * Helper to find max subarray sum no larger than k using prefix sums + BST (simulated with sorted array)
     *
     * @param int[] $arr
     * @param int $k
     * @return int
     */
    private function maxSubArrayNoLargerThanK($arr, $k) {
        $prefix = 0;
        $sorted = [0];
        $best = PHP_INT_MIN;

        foreach ($arr as $num) {
            $prefix += $num;
            $target = $prefix - $k;

            // binary search for lower bound of target in $sorted
            $l = 0;
            $r = count($sorted);
            while ($l < $r) {
                $mid = intdiv($l + $r, 2);
                if ($sorted[$mid] < $target) {
                    $l = $mid + 1;
                } else {
                    $r = $mid;
                }
            }

            if ($l < count($sorted)) {
                $candidate = $prefix - $sorted[$l];
                if ($candidate > $best) {
                    $best = $candidate;
                }
            }

            // insert current prefix into sorted array
            $l = 0;
            $r = count($sorted);
            while ($l < $r) {
                $mid = intdiv($l + $r, 2);
                if ($sorted[$mid] <= $prefix) {
                    $l = $mid + 1;
                } else {
                    $r = $mid;
                }
            }
            array_splice($sorted, $l, 0, [$prefix]);
        }

        return $best;
    }
}
```

## Swift

```swift
class Solution {
    func maxSumSubmatrix(_ matrix: [[Int]], _ k: Int) -> Int {
        let rows = matrix.count
        guard rows > 0 else { return 0 }
        let cols = matrix[0].count
        var result = Int.min

        for left in 0..<cols {
            var rowSums = [Int](repeating: 0, count: rows)
            for right in left..<cols {
                // accumulate sums between columns left and right for each row
                for r in 0..<rows {
                    rowSums[r] += matrix[r][right]
                }

                // find the max subarray sum no larger than k in rowSums
                var prefixSet = [Int]()
                prefixSet.append(0)   // prefix sum of empty subarray
                var curSum = 0

                for sum in rowSums {
                    curSum += sum
                    let target = curSum - k

                    // lower bound: first element >= target
                    var l = 0, r = prefixSet.count
                    while l < r {
                        let mid = (l + r) >> 1
                        if prefixSet[mid] < target {
                            l = mid + 1
                        } else {
                            r = mid
                        }
                    }
                    if l < prefixSet.count {
                        let candidate = curSum - prefixSet[l]
                        if candidate > result { result = candidate }
                        if result == k { return k } // early exit
                    }

                    // insert current prefix sum maintaining sorted order
                    var posL = 0, posR = prefixSet.count
                    while posL < posR {
                        let mid = (posL + posR) >> 1
                        if prefixSet[mid] < curSum {
                            posL = mid + 1
                        } else {
                            posR = mid
                        }
                    }
                    prefixSet.insert(curSum, at: posL)
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
    fun maxSumSubmatrix(matrix: Array<IntArray>, k: Int): Int {
        val rows = matrix.size
        val cols = matrix[0].size
        var result = Int.MIN_VALUE
        if (rows <= cols) {
            for (top in 0 until rows) {
                val sums = IntArray(cols)
                for (bottom in top until rows) {
                    for (c in 0 until cols) {
                        sums[c] += matrix[bottom][c]
                    }
                    var curSum = 0L
                    val set = java.util.TreeSet<Long>()
                    set.add(0L)
                    for (value in sums) {
                        curSum += value.toLong()
                        val target = curSum - k
                        val ceiling = set.ceiling(target)
                        if (ceiling != null) {
                            val candidate = (curSum - ceiling).toInt()
                            if (candidate > result) result = candidate
                            if (result == k) return k
                        }
                        set.add(curSum)
                    }
                }
            }
        } else {
            for (left in 0 until cols) {
                val sums = IntArray(rows)
                for (right in left until cols) {
                    for (r in 0 until rows) {
                        sums[r] += matrix[r][right]
                    }
                    var curSum = 0L
                    val set = java.util.TreeSet<Long>()
                    set.add(0L)
                    for (value in sums) {
                        curSum += value.toLong()
                        val target = curSum - k
                        val ceiling = set.ceiling(target)
                        if (ceiling != null) {
                            val candidate = (curSum - ceiling).toInt()
                            if (candidate > result) result = candidate
                            if (result == k) return k
                        }
                        set.add(curSum)
                    }
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
  int maxSumSubmatrix(List<List<int>> matrix, int k) {
    int rows = matrix.length;
    int cols = matrix[0].length;
    List<List<int>> mat = matrix;

    // Ensure the smaller dimension is used for the outer loops
    if (rows > cols) {
      List<List<int>> trans = List.generate(cols, (_) => List.filled(rows, 0));
      for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
          trans[j][i] = mat[i][j];
        }
      }
      mat = trans;
      int tmp = rows;
      rows = cols;
      cols = tmp;
    }

    int ans = -1 << 60; // Very small number
    List<int> sums = List.filled(rows, 0);

    for (int left = 0; left < cols; ++left) {
      for (int i = 0; i < rows; ++i) sums[i] = 0;
      for (int right = left; right < cols; ++right) {
        for (int i = 0; i < rows; ++i) {
          sums[i] += mat[i][right];
        }
        int curBest = _maxSubArrayNoMoreThanK(sums, k);
        if (curBest > ans) ans = curBest;
        if (ans == k) return ans; // early exit
      }
    }

    return ans;
  }

  int _maxSubArrayNoMoreThanK(List<int> arr, int k) {
    List<int> prefix = [0];
    int cur = 0;
    int best = -1 << 60;

    for (int num in arr) {
      cur += num;
      int target = cur - k;
      int idx = _lowerBound(prefix, target);
      if (idx < prefix.length) {
        int candidate = cur - prefix[idx];
        if (candidate > best) best = candidate;
      }
      int insIdx = _lowerBound(prefix, cur);
      prefix.insert(insIdx, cur);
    }

    return best;
  }

  int _lowerBound(List<int> list, int target) {
    int lo = 0, hi = list.length;
    while (lo < hi) {
      int mid = (lo + hi) >> 1;
      if (list[mid] < target) {
        lo = mid + 1;
      } else {
        hi = mid;
      }
    }
    return lo;
  }
}
```

## Golang

```go
import "sort"

func maxSumSubmatrix(matrix [][]int, k int) int {
	m := len(matrix)
	n := len(matrix[0])
	ans := -1 << 31

	if m <= n {
		for left := 0; left < n; left++ {
			rowSums := make([]int, m)
			for right := left; right < n; right++ {
				for i := 0; i < m; i++ {
					rowSums[i] += matrix[i][right]
				}
				cum := 0
				sorted := []int{0}
				for _, v := range rowSums {
					cum += v
					target := cum - k
					idx := sort.SearchInts(sorted, target)
					if idx < len(sorted) {
						cand := cum - sorted[idx]
						if cand > ans {
							ans = cand
							if ans == k {
								return k
							}
						}
					}
					pos := sort.SearchInts(sorted, cum)
					sorted = append(sorted, 0)
					copy(sorted[pos+1:], sorted[pos:])
					sorted[pos] = cum
				}
			}
		}
	} else {
		for top := 0; top < m; top++ {
			colSums := make([]int, n)
			for bottom := top; bottom < m; bottom++ {
				for j := 0; j < n; j++ {
					colSums[j] += matrix[bottom][j]
				}
				cum := 0
				sorted := []int{0}
				for _, v := range colSums {
					cum += v
					target := cum - k
					idx := sort.SearchInts(sorted, target)
					if idx < len(sorted) {
						cand := cum - sorted[idx]
						if cand > ans {
							ans = cand
							if ans == k {
								return k
							}
						}
					}
					pos := sort.SearchInts(sorted, cum)
					sorted = append(sorted, 0)
					copy(sorted[pos+1:], sorted[pos:])
					sorted[pos] = cum
				}
			}
		}
	}
	return ans
}
```

## Ruby

```ruby
def max_sum_submatrix(matrix, k)
  rows = matrix.length
  cols = matrix[0].length

  # Ensure the smaller dimension is used for the outer loops
  if rows > cols
    transposed = Array.new(cols) { Array.new(rows) }
    rows.times do |i|
      cols.times do |j|
        transposed[j][i] = matrix[i][j]
      end
    end
    matrix = transposed
    rows, cols = cols, rows
  end

  max_sum = -Float::INFINITY

  (0...cols).each do |left|
    sums = Array.new(rows, 0)
    (left...cols).each do |right|
      rows.times { |i| sums[i] += matrix[i][right] }

      # Find the best subarray sum no larger than k using prefix sums + binary search
      prefix_set = [0]
      cur_sum = 0
      best = -Float::INFINITY

      sums.each do |val|
        cur_sum += val
        target = cur_sum - k
        idx = prefix_set.bsearch_index { |x| x >= target }
        if idx
          candidate = cur_sum - prefix_set[idx]
          best = candidate if candidate > best
        end
        insert_idx = prefix_set.bsearch_index { |x| x > cur_sum } || prefix_set.length
        prefix_set.insert(insert_idx, cur_sum)
      end

      max_sum = best if best > max_sum
    end
  end

  max_sum.to_i
end
```

## Scala

```scala
object Solution {
  import java.util.TreeSet

  def maxSumSubmatrix(matrix: Array[Array[Int]], k: Int): Int = {
    val rows = matrix.length
    val cols = matrix(0).length
    var result = Int.MinValue

    if (rows <= cols) {
      // iterate over left and right columns
      for (left <- 0 until cols) {
        val rowSums = new Array[Int](rows)
        for (right <- left until cols) {
          var r = 0
          while (r < rows) {
            rowSums(r) += matrix(r)(right)
            r += 1
          }
          // find max subarray sum <= k in rowSums
          val set = new TreeSet[Int]()
          set.add(0)
          var curSum = 0
          var best = Int.MinValue
          for (v <- rowSums) {
            curSum += v
            val target = curSum - k
            val ceiling = set.ceiling(target)
            if (ceiling != null) {
              val candidate = curSum - ceiling
              if (candidate > best) best = candidate
            }
            set.add(curSum)
          }
          if (best > result) result = best
        }
      }
    } else {
      // iterate over top and bottom rows
      for (top <- 0 until rows) {
        val colSums = new Array[Int](cols)
        for (bottom <- top until rows) {
          var c = 0
          while (c < cols) {
            colSums(c) += matrix(bottom)(c)
            c += 1
          }
          // find max subarray sum <= k in colSums
          val set = new TreeSet[Int]()
          set.add(0)
          var curSum = 0
          var best = Int.MinValue
          for (v <- colSums) {
            curSum += v
            val target = curSum - k
            val ceiling = set.ceiling(target)
            if (ceiling != null) {
              val candidate = curSum - ceiling
              if (candidate > best) best = candidate
            }
            set.add(curSum)
          }
          if (best > result) result = best
        }
      }
    }

    result
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_sum_submatrix(matrix: Vec<Vec<i32>>, k: i32) -> i32 {
        let m = matrix.len();
        if m == 0 {
            return 0;
        }
        let n = matrix[0].len();
        let k_i64 = k as i64;
        let mut result = i64::MIN;

        if m <= n {
            // compress rows
            for top in 0..m {
                let mut col_sums = vec![0i64; n];
                for bottom in top..m {
                    for c in 0..n {
                        col_sums[c] += matrix[bottom][c] as i64;
                    }
                    use std::collections::BTreeSet;
                    let mut set = BTreeSet::new();
                    set.insert(0i64);
                    let mut cur = 0i64;
                    for &val in &col_sums {
                        cur += val;
                        let target = cur - k_i64;
                        if let Some(&s) = set.range(target..).next() {
                            let candidate = cur - s;
                            if candidate <= k_i64 && candidate > result {
                                result = candidate;
                            }
                        }
                        set.insert(cur);
                    }
                }
            }
        } else {
            // compress columns
            for left in 0..n {
                let mut row_sums = vec![0i64; m];
                for right in left..n {
                    for r in 0..m {
                        row_sums[r] += matrix[r][right] as i64;
                    }
                    use std::collections::BTreeSet;
                    let mut set = BTreeSet::new();
                    set.insert(0i64);
                    let mut cur = 0i64;
                    for &val in &row_sums {
                        cur += val;
                        let target = cur - k_i64;
                        if let Some(&s) = set.range(target..).next() {
                            let candidate = cur - s;
                            if candidate <= k_i64 && candidate > result {
                                result = candidate;
                            }
                        }
                        set.insert(cur);
                    }
                }
            }
        }

        result as i32
    }
}
```

## Racket

```racket
(define (max-subarray-no-larger-than-k arr k)
  (let loop ((i 0) (prefix 0) (sorted '(0)) (best -1000000000))
    (if (= i (length arr))
        best
        (let* ((prefix (+ prefix (list-ref arr i)))
               (target (- prefix k))
               ;; find first element in sorted >= target
               (candidate (let find ((lst sorted))
                            (cond [(null? lst) #f]
                                  [(>= (car lst) target) (car lst)]
                                  [else (find (cdr lst))])))
               (best2 (if candidate (max best (- prefix candidate)) best))
               ;; insert current prefix into sorted list keeping order
               (new-sorted (let insert ((lst sorted))
                             (cond [(null? lst) (list prefix)]
                                   [(<= prefix (car lst)) (cons prefix lst)]
                                   [else (cons (car lst) (insert (cdr lst)))]))))
          (loop (+ i 1) prefix new-sorted best2)))))

(define/contract (max-sum-submatrix matrix k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ((rows (length matrix))
         (cols (if (null? matrix) 0 (length (car matrix))))
         (transpose? (> rows cols)))
    ;; transpose if rows > cols to reduce the number of column pairs
    (define mat
      (if transpose?
          (let loop ((c 0) (res '()))
            (if (= c cols)
                (reverse res)
                (loop (+ c 1)
                      (cons (map (lambda (row) (list-ref row c)) matrix) res))))
          matrix))
    (define m (length mat))
    (define n (if (null? mat) 0 (length (car mat))))
    (let ((best -1000000000))
      (for ([left (in-range n)])
        (define row-sums (make-vector m 0))
        (for ([right (in-range left n)])
          ;; update cumulative sums for each row between columns left..right
          (for ([i (in-range m)])
            (vector-set! row-sums i (+ (vector-ref row-sums i)
                                      (list-ref (list-ref mat i) right))))
          ;; compute best subarray sum <= k for current row-sums
          (define cur (max-subarray-no-larger-than-k (vector->list row-sums) k))
          (when (> cur best) (set! best cur))))
      best)))
```

## Erlang

```erlang
-spec max_sum_submatrix(Matrix :: [[integer()]], K :: integer()) -> integer().
max_sum_submatrix(Matrix, K) ->
    Rows = length(Matrix),
    Cols = case Matrix of [] -> 0; [First|_] -> length(First) end,
    max_left(0, Cols, Rows, Matrix, K, -1000000000).

%% iterate over left column index
max_left(Left, Cols, _Rows, _Matrix, _K, Max) when Left >= Cols ->
    Max;
max_left(Left, Cols, Rows, Matrix, K, Max) ->
    ZeroSums = lists:duplicate(Rows, 0),
    NewMax = max_right(Left, Left, Cols, Rows, Matrix, K, Max, ZeroSums),
    max_left(Left + 1, Cols, Rows, Matrix, K, NewMax).

%% iterate over right column index, updating row sums
max_right(_Left, Right, Cols, _Rows, _Matrix, _K, Max, _Sums) when Right >= Cols ->
    Max;
max_right(Left, Right, Cols, Rows, Matrix, K, Max, Sums) ->
    Updated = add_column(Matrix, Right, Sums),
    CurrBest = max_subarray_no_larger_than_k(Updated, K),
    NewMax = if CurrBest > Max -> CurrBest; true -> Max end,
    max_right(Left, Right + 1, Cols, Rows, Matrix, K, NewMax, Updated).

%% add values of column ColIdx to each row sum
add_column([], _ColIdx, []) ->
    [];
add_column([Row|RestRows], ColIdx, [Sum|RestSums]) ->
    Val = lists:nth(ColIdx + 1, Row),
    [Sum + Val | add_column(RestRows, ColIdx, RestSums)].

%% find max subarray sum no larger than K using prefix sums and ordered set
max_subarray_no_larger_than_k(Sums, K) ->
    Tree0 = gb_trees:insert(0, true, gb_trees:empty()),
    max_sub_iter(Sums, 0, K, Tree0, -1000000000).

max_sub_iter([], _Prefix, _K, _Tree, Best) ->
    Best;
max_sub_iter([Val|Rest], Prefix, K, Tree, Best) ->
    NewPrefix = Prefix + Val,
    Target = NewPrefix - K,
    Iter = gb_trees:iterator_from(Target, Tree),
    Best1 = case gb_trees:next(Iter) of
        none -> Best;
        {Key,_Val,_} ->
            Candidate = NewPrefix - Key,
            if Candidate > Best -> Candidate; true -> Best end
    end,
    Tree2 = gb_trees:insert(NewPrefix, true, Tree),
    max_sub_iter(Rest, NewPrefix, K, Tree2, Best1).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_sum_submatrix(matrix :: [[integer]], k :: integer) :: integer
  def max_sum_submatrix(matrix, k) do
    m = length(matrix)
    n = matrix |> hd() |> length()

    {rows, cols, mat} =
      if m <= n do
        {m, n, matrix}
      else
        {n, m, transpose(matrix)}
      end

    Enum.reduce(0..(rows - 1), -1_000_000_000, fn top, global_best ->
      sums = List.duplicate(0, cols)

      {_final_sums, best_for_top} =
        Enum.reduce(top..(rows - 1), {sums, global_best}, fn bottom, {cur_sums, cur_best} ->
          row_vals = Enum.at(mat, bottom)
          new_sums = add_lists(cur_sums, row_vals)

          candidate = max_subarray_no_larger_than_k(new_sums, k)
          new_best = if candidate > cur_best, do: candidate, else: cur_best

          {new_sums, new_best}
        end)

      best_for_top
    end)
  end

  defp transpose(matrix) do
    matrix |> List.zip() |> Enum.map(&Tuple.to_list/1)
  end

  defp add_lists(a, b) do
    Enum.zip_with([a, b], fn [x, y] -> x + y end)
  end

  defp max_subarray_no_larger_than_k(arr, k) do
    tree = :gb_trees.empty()
    tree = :gb_trees.insert(0, true, tree)

    {_, _, best} =
      Enum.reduce(arr, {tree, 0, -1_000_000_000}, fn x, {t, pref, best} ->
        pref = pref + x
        target = pref - k

        it = :gb_trees.iterator_from(target, t)

        best =
          case :gb_trees.next(it) do
            :'$end_of_table' -> best
            {ceil_key, _val, _rest} ->
              cand = pref - ceil_key
              if cand > best, do: cand, else: best
          end

        t = :gb_trees.insert(pref, true, t)
        {t, pref, best}
      end)

    best
  end
end
```
