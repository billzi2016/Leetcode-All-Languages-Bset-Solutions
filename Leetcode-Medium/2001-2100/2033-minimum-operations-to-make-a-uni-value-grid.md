# 2033. Minimum Operations to Make a Uni-Value Grid

## Cpp

```cpp
class Solution {
public:
    int minOperations(vector<vector<int>>& grid, int x) {
        long long ops = 0;
        vector<int> vals;
        int m = grid.size();
        int n = grid[0].size();
        vals.reserve((long long)m * n);
        int rem = grid[0][0] % x;
        for (auto& row : grid) {
            for (int v : row) {
                if (v % x != rem) return -1;
                vals.push_back(v);
            }
        }
        sort(vals.begin(), vals.end());
        int median = vals[vals.size() / 2];
        for (int v : vals) {
            ops += llabs((long long)v - median) / x;
        }
        return (int)ops;
    }
};
```

## Java

```java
class Solution {
    public int minOperations(int[][] grid, int x) {
        int m = grid.length;
        int n = grid[0].length;
        int total = m * n;
        int[] nums = new int[total];
        int idx = 0;
        int rem = ((grid[0][0] % x) + x) % x; // ensure non-negative
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (((grid[i][j] % x) + x) % x != rem) {
                    return -1;
                }
                nums[idx++] = grid[i][j];
            }
        }
        java.util.Arrays.sort(nums);
        int median = nums[total / 2];
        long ops = 0L;
        for (int v : nums) {
            ops += Math.abs(v - median) / x;
        }
        return (int) ops;
    }
}
```

## Python

```python
class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        nums = []
        mod = None
        for row in grid:
            for val in row:
                if mod is None:
                    mod = val % x
                elif val % x != mod:
                    return -1
                nums.append(val)
        nums.sort()
        median = nums[len(nums) // 2]
        ops = 0
        for v in nums:
            ops += abs(v - median) // x
        return ops
```

## Python3

```python
from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []
        first_mod = None
        for row in grid:
            for val in row:
                if first_mod is None:
                    first_mod = val % x
                elif val % x != first_mod:
                    return -1
                nums.append(val)
        nums.sort()
        median = nums[len(nums) // 2]
        ops = 0
        for v in nums:
            ops += abs(v - median) // x
        return ops
```

## C

```c
#include <stdlib.h>
#include <limits.h>

static int cmp_int(const void *a, const void *b) {
    int av = *(const int *)a;
    int bv = *(const int *)b;
    return (av > bv) - (av < bv);
}

int minOperations(int** grid, int gridSize, int* gridColSize, int x) {
    if (gridSize == 0) return 0;
    int cols = gridColSize[0];
    long totalElems = 0;
    for (int i = 0; i < gridSize; ++i) totalElems += gridColSize[i];
    
    int *arr = (int *)malloc(totalElems * sizeof(int));
    if (!arr) return -1; // allocation failure, though unlikely
    
    long idx = 0;
    int baseMod = grid[0][0] % x;
    for (int i = 0; i < gridSize; ++i) {
        int curCols = gridColSize[i];
        for (int j = 0; j < curCols; ++j) {
            int val = grid[i][j];
            if ((val % x + x) % x != baseMod) { // ensure positive remainder
                free(arr);
                return -1;
            }
            arr[idx++] = val;
        }
    }
    
    qsort(arr, totalElems, sizeof(int), cmp_int);
    
    int median = arr[totalElems / 2];
    long long ops = 0;
    for (long i = 0; i < totalElems; ++i) {
        ops += llabs((long long)arr[i] - median) / x;
    }
    
    free(arr);
    return (int)ops;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MinOperations(int[][] grid, int x) {
        int rows = grid.Length;
        int cols = grid[0].Length;
        List<int> values = new List<int>(rows * cols);
        int remainder = grid[0][0] % x;
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] % x != remainder) return -1;
                values.Add(grid[i][j]);
            }
        }
        
        values.Sort();
        int median = values[values.Count / 2];
        long operations = 0;
        foreach (int v in values) {
            operations += Math.Abs(v - median) / x;
        }
        return (int)operations;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @param {number} x
 * @return {number}
 */
var minOperations = function(grid, x) {
    const m = grid.length;
    const n = grid[0].length;
    const totalElements = m * n;
    const nums = new Array(totalElements);
    let idx = 0;
    const baseRem = ((grid[0][0] % x) + x) % x; // ensure non-negative
    for (let i = 0; i < m; ++i) {
        const row = grid[i];
        for (let j = 0; j < n; ++j) {
            const val = row[j];
            if (((val % x) + x) % x !== baseRem) return -1;
            nums[idx++] = val;
        }
    }
    nums.sort((a, b) => a - b);
    const median = nums[Math.floor(totalElements / 2)];
    let ops = 0;
    for (let i = 0; i < totalElements; ++i) {
        ops += Math.abs(nums[i] - median) / x;
    }
    return ops;
};
```

## Typescript

```typescript
function minOperations(grid: number[][], x: number): number {
    const nums: number[] = [];
    const firstMod = ((grid[0][0] % x) + x) % x;
    for (let i = 0; i < grid.length; ++i) {
        const row = grid[i];
        for (let j = 0; j < row.length; ++j) {
            const val = row[j];
            if (((val % x) + x) % x !== firstMod) return -1;
            nums.push(val);
        }
    }
    nums.sort((a, b) => a - b);
    const median = nums[Math.floor(nums.length / 2)];
    let ops = 0;
    for (const v of nums) {
        ops += Math.abs(v - median) / x;
    }
    return ops;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $grid
     * @param Integer $x
     * @return Integer
     */
    function minOperations($grid, $x) {
        $arr = [];
        $mod = null;
        foreach ($grid as $row) {
            foreach ($row as $val) {
                if ($mod === null) {
                    $mod = $val % $x;
                } elseif (($val % $x) !== $mod) {
                    return -1;
                }
                $arr[] = $val;
            }
        }

        sort($arr);
        $n = count($arr);
        $median = $arr[intdiv($n, 2)];
        $ops = 0;
        foreach ($arr as $v) {
            $ops += intdiv(abs($v - $median), $x);
        }
        return $ops;
    }
}
```

## Swift

```swift
class Solution {
    func minOperations(_ grid: [[Int]], _ x: Int) -> Int {
        var values = [Int]()
        guard let firstRow = grid.first, let firstVal = firstRow.first else { return 0 }
        let targetRemainder = firstVal % x
        for row in grid {
            for v in row {
                if v % x != targetRemainder {
                    return -1
                }
                values.append(v)
            }
        }
        values.sort()
        let median = values[values.count / 2]
        var total: Int64 = 0
        for v in values {
            total += Int64(abs(v - median) / x)
        }
        return Int(total)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minOperations(grid: Array<IntArray>, x: Int): Int {
        val m = grid.size
        if (m == 0) return 0
        val n = grid[0].size
        val total = m * n
        val arr = IntArray(total)
        var idx = 0
        val rem = grid[0][0] % x
        for (row in grid) {
            for (v in row) {
                if (v % x != rem) return -1
                arr[idx++] = v
            }
        }
        java.util.Arrays.sort(arr)
        val median = arr[arr.size / 2]
        var ops = 0L
        for (value in arr) {
            ops += kotlin.math.abs(value - median).toLong() / x
        }
        return ops.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int minOperations(List<List<int>> grid, int x) {
    if (grid.isEmpty || grid[0].isEmpty) return 0;
    int mod = grid[0][0] % x;
    List<int> nums = [];
    for (var row in grid) {
      for (var val in row) {
        if (val % x != mod) return -1;
        nums.add(val);
      }
    }
    nums.sort();
    int median = nums[nums.length ~/ 2];
    int ops = 0;
    for (int v in nums) {
      ops += ((v - median).abs() ~/ x);
    }
    return ops;
  }
}
```

## Golang

```go
import "sort"

func minOperations(grid [][]int, x int) int {
	if len(grid) == 0 || len(grid[0]) == 0 {
		return 0
	}
	n := 0
	for _, row := range grid {
		n += len(row)
	}
	vals := make([]int, 0, n)

	baseMod := grid[0][0] % x
	for _, row := range grid {
		for _, v := range row {
			if v%x != baseMod {
				return -1
			}
			vals = append(vals, v)
		}
	}

	sort.Ints(vals)
	median := vals[len(vals)/2]

	var ops int64
	for _, v := range vals {
		diff := median - v
		if diff < 0 {
			diff = -diff
		}
		ops += int64(diff / x)
	}
	return int(ops)
}
```

## Ruby

```ruby
def min_operations(grid, x)
  nums = []
  base_mod = nil
  grid.each do |row|
    row.each do |v|
      if base_mod.nil?
        base_mod = v % x
      elsif v % x != base_mod
        return -1
      end
      nums << v
    end
  end

  nums.sort!
  median = nums[nums.length / 2]

  ops = 0
  nums.each do |v|
    ops += ((median - v).abs) / x
  end
  ops
end
```

## Scala

```scala
object Solution {
    def minOperations(grid: Array[Array[Int]], x: Int): Int = {
        val m = grid.length
        if (m == 0) return 0
        val n = grid(0).length
        val total = m * n
        val arr = new Array[Int](total)
        var idx = 0
        val baseRem = ((grid(0)(0) % x) + x) % x

        var i = 0
        while (i < m) {
            val row = grid(i)
            var j = 0
            while (j < n) {
                val v = row(j)
                if (((v % x) + x) % x != baseRem) return -1
                arr(idx) = v
                idx += 1
                j += 1
            }
            i += 1
        }

        java.util.Arrays.sort(arr)
        val median = arr(total / 2)

        var ops: Long = 0L
        var k = 0
        while (k < total) {
            ops += (Math.abs(arr(k) - median).toLong) / x
            k += 1
        }

        ops.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_operations(grid: Vec<Vec<i32>>, x: i32) -> i32 {
        if grid.is_empty() || grid[0].is_empty() {
            return 0;
        }
        let m = grid.len();
        let n = grid[0].len();
        let mut vals = Vec::with_capacity(m * n);
        // All numbers must have the same remainder modulo x
        let base_rem = ((grid[0][0] % x) + x) % x;
        for row in &grid {
            for &v in row {
                if ((v % x) + x) % x != base_rem {
                    return -1;
                }
                vals.push(v);
            }
        }

        vals.sort_unstable();
        let median = vals[vals.len() / 2];
        let mut ops: i64 = 0;
        let x_i64 = x as i64;
        for &v in &vals {
            ops += ((median - v).abs() as i64) / x_i64;
        }
        ops as i32
    }
}
```

## Racket

```racket
#lang racket

(define/contract (min-operations grid x)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ((flat (apply append grid))
         (first-rem (mod (car flat) x)))
    (if (not (andmap (lambda (v) (= (mod v x) first-rem)) flat))
        -1
        (let* ((sorted (sort flat <))
               (len (length sorted))
               (median (list-ref sorted (quotient len 2)))
               (ops (foldl (lambda (v acc)
                             (+ acc (/ (abs (- v median)) x)))
                           0
                           sorted)))
          ops))))
```

## Erlang

```erlang
-module(solution).
-export([min_operations/2]).

-spec min_operations(Grid :: [[integer()]], X :: integer()) -> integer().
min_operations(Grid, X) ->
    Flat = [V || Row <- Grid, V <- Row],
    Rem = hd(Flat) rem X,
    case lists:any(fun(V) -> V rem X =/= Rem end, Flat) of
        true -> -1;
        false ->
            Sorted = lists:sort(Flat),
            N = length(Sorted),
            MedianIdx = N div 2,
            Median = lists:nth(MedianIdx + 1, Sorted),
            lists:foldl(fun(V, Acc) -> Acc + (abs(Median - V) div X) end, 0, Flat)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_operations(grid :: [[integer]], x :: integer) :: integer
  def min_operations(grid, x) do
    nums = List.flatten(grid)

    case nums do
      [] ->
        0

      [first | _] ->
        base_rem = rem(first, x)

        if Enum.any?(nums, fn v -> rem(v, x) != base_rem end) do
          -1
        else
          sorted = Enum.sort(nums)
          len = length(sorted)
          median = Enum.at(sorted, div(len, 2))

          Enum.reduce(sorted, 0, fn v, acc ->
            acc + div(abs(median - v), x)
          end)
        end
    end
  end
end
```
