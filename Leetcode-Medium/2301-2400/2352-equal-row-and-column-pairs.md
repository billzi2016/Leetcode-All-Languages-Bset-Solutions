# 2352. Equal Row and Column Pairs

## Cpp

```cpp
class Solution {
public:
    struct VecHash {
        size_t operator()(const std::vector<int>& v) const noexcept {
            size_t h = 0;
            for (int x : v) {
                // combine hash values
                h ^= std::hash<int>{}(x + 0x9e3779b9 + (h << 6) + (h >> 2));
            }
            return h;
        }
    };
    
    int equalPairs(std::vector<std::vector<int>>& grid) {
        int n = grid.size();
        std::unordered_map<std::vector<int>, int, VecHash> rowCount;
        for (int i = 0; i < n; ++i) {
            rowCount[grid[i]]++;
        }
        
        int ans = 0;
        std::vector<int> col(n);
        for (int j = 0; j < n; ++j) {
            for (int i = 0; i < n; ++i) {
                col[i] = grid[i][j];
            }
            auto it = rowCount.find(col);
            if (it != rowCount.end()) ans += it->second;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int equalPairs(int[][] grid) {
        int n = grid.length;
        java.util.Map<String, Integer> rowCount = new java.util.HashMap<>();
        StringBuilder sb = new StringBuilder();
        
        // Encode each row as a string and count occurrences
        for (int i = 0; i < n; i++) {
            sb.setLength(0);
            for (int j = 0; j < n; j++) {
                sb.append(grid[i][j]).append(',');
            }
            String key = sb.toString();
            rowCount.put(key, rowCount.getOrDefault(key, 0) + 1);
        }
        
        int ans = 0;
        // Encode each column and add matching row counts
        for (int j = 0; j < n; j++) {
            sb.setLength(0);
            for (int i = 0; i < n; i++) {
                sb.append(grid[i][j]).append(',');
            }
            String key = sb.toString();
            ans += rowCount.getOrDefault(key, 0);
        }
        
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        col_counts = {}
        for j in range(n):
            col = tuple(grid[i][j] for i in range(n))
            col_counts[col] = col_counts.get(col, 0) + 1

        ans = 0
        for i in range(n):
            row = tuple(grid[i])
            ans += col_counts.get(row, 0)

        return ans
```

## Python3

```python
from typing import List
from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_counter = Counter(tuple(row) for row in grid)
        ans = 0
        for c in range(n):
            col_tuple = tuple(grid[r][c] for r in range(n))
            ans += row_counter[col_tuple]
        return ans
```

## C

```c
int equalPairs(int** grid, int gridSize, int* gridColSize){
    int n = gridSize;
    int count = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            int same = 1;
            for (int k = 0; k < n; ++k) {
                if (grid[i][k] != grid[k][j]) {
                    same = 0;
                    break;
                }
            }
            if (same) ++count;
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int EqualPairs(int[][] grid) {
        int n = grid.Length;
        var rowCount = new Dictionary<string, int>();
        var sb = new System.Text.StringBuilder();

        for (int i = 0; i < n; i++) {
            sb.Clear();
            for (int j = 0; j < n; j++) {
                sb.Append(grid[i][j]);
                sb.Append(',');
            }
            string key = sb.ToString();
            if (rowCount.ContainsKey(key))
                rowCount[key]++;
            else
                rowCount[key] = 1;
        }

        int result = 0;
        for (int col = 0; col < n; col++) {
            sb.Clear();
            for (int row = 0; row < n; row++) {
                sb.Append(grid[row][col]);
                sb.Append(',');
            }
            string key = sb.ToString();
            if (rowCount.TryGetValue(key, out int cnt))
                result += cnt;
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var equalPairs = function(grid) {
    const n = grid.length;
    const rowCount = new Map();
    
    for (let i = 0; i < n; ++i) {
        const key = grid[i].join(',');
        rowCount.set(key, (rowCount.get(key) || 0) + 1);
    }
    
    let ans = 0;
    for (let j = 0; j < n; ++j) {
        const col = [];
        for (let i = 0; i < n; ++i) {
            col.push(grid[i][j]);
        }
        const key = col.join(',');
        if (rowCount.has(key)) {
            ans += rowCount.get(key);
        }
    }
    
    return ans;
};
```

## Typescript

```typescript
function equalPairs(grid: number[][]): number {
    const n = grid.length;
    const rowMap = new Map<string, number>();
    for (let i = 0; i < n; i++) {
        const key = grid[i].join(',');
        rowMap.set(key, (rowMap.get(key) ?? 0) + 1);
    }
    let ans = 0;
    for (let j = 0; j < n; j++) {
        const col: number[] = [];
        for (let i = 0; i < n; i++) {
            col.push(grid[i][j]);
        }
        const key = col.join(',');
        if (rowMap.has(key)) {
            ans += rowMap.get(key)!;
        }
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function equalPairs($grid) {
        $n = count($grid);
        $colMap = [];

        // Build hashmap for columns
        for ($j = 0; $j < $n; $j++) {
            $colArr = [];
            for ($i = 0; $i < $n; $i++) {
                $colArr[] = $grid[$i][$j];
            }
            $key = implode(',', $colArr);
            if (isset($colMap[$key])) {
                $colMap[$key]++;
            } else {
                $colMap[$key] = 1;
            }
        }

        $ans = 0;
        // Compare each row with column hashmap
        for ($i = 0; $i < $n; $i++) {
            $rowKey = implode(',', $grid[$i]);
            if (isset($colMap[$rowKey])) {
                $ans += $colMap[$rowKey];
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func equalPairs(_ grid: [[Int]]) -> Int {
        let n = grid.count
        var rowCount = [Array<Int>: Int]()
        for row in grid {
            rowCount[row, default: 0] += 1
        }
        var result = 0
        for colIndex in 0..<n {
            var column = [Int]()
            column.reserveCapacity(n)
            for rowIndex in 0..<n {
                column.append(grid[rowIndex][colIndex])
            }
            if let cnt = rowCount[column] {
                result += cnt
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun equalPairs(grid: Array<IntArray>): Int {
        val n = grid.size
        val rowMap = HashMap<String, Int>()
        for (i in 0 until n) {
            val sb = StringBuilder()
            for (j in 0 until n) {
                sb.append(grid[i][j]).append(',')
            }
            val key = sb.toString()
            rowMap[key] = rowMap.getOrDefault(key, 0) + 1
        }
        var ans = 0
        for (j in 0 until n) {
            val sb = StringBuilder()
            for (i in 0 until n) {
                sb.append(grid[i][j]).append(',')
            }
            val key = sb.toString()
            ans += rowMap.getOrDefault(key, 0)
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int equalPairs(List<List<int>> grid) {
    int n = grid.length;
    Map<String, int> rowCount = {};
    for (int i = 0; i < n; ++i) {
      String key = grid[i].join(',');
      rowCount[key] = (rowCount[key] ?? 0) + 1;
    }
    int ans = 0;
    for (int j = 0; j < n; ++j) {
      List<int> col = [];
      for (int i = 0; i < n; ++i) {
        col.add(grid[i][j]);
      }
      String key = col.join(',');
      ans += rowCount[key] ?? 0;
    }
    return ans;
  }
}
```

## Golang

```go
import (
	"strconv"
	"strings"
)

func equalPairs(grid [][]int) int {
	n := len(grid)
	rowMap := make(map[string]int, n)
	var sb strings.Builder

	for i := 0; i < n; i++ {
		sb.Reset()
		for j := 0; j < n; j++ {
			if j > 0 {
				sb.WriteByte('#')
			}
			sb.WriteString(strconv.Itoa(grid[i][j]))
		}
		rowMap[sb.String()]++
	}

	ans := 0
	for c := 0; c < n; c++ {
		sb.Reset()
		for r := 0; r < n; r++ {
			if r > 0 {
				sb.WriteByte('#')
			}
			sb.WriteString(strconv.Itoa(grid[r][c]))
		}
		ans += rowMap[sb.String()]
	}

	return ans
}
```

## Ruby

```ruby
def equal_pairs(grid)
  row_counts = Hash.new(0)
  grid.each { |row| row_counts[row] += 1 }

  n = grid.size
  ans = 0

  (0...n).each do |j|
    col = Array.new(n) { |i| grid[i][j] }
    ans += row_counts[col]
  end

  ans
end
```

## Scala

```scala
object Solution {
  def equalPairs(grid: Array[Array[Int]]): Int = {
    val n = grid.length
    val rowMap = scala.collection.mutable.Map[Seq[Int], Int]()
    for (i <- 0 until n) {
      val seq = grid(i).toSeq
      rowMap(seq) = rowMap.getOrElse(seq, 0) + 1
    }
    var ans = 0
    for (j <- 0 until n) {
      val colSeq = (0 until n).map(i => grid(i)(j))
      ans += rowMap.getOrElse(colSeq, 0)
    }
    ans
  }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn equal_pairs(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let mut row_map: HashMap<Vec<i32>, i32> = HashMap::new();

        for r in 0..n {
            let row = grid[r].clone();
            *row_map.entry(row).or_insert(0) += 1;
        }

        let mut ans = 0i32;

        for c in 0..n {
            let mut col = Vec::with_capacity(n);
            for r in 0..n {
                col.push(grid[r][c]);
            }
            if let Some(cnt) = row_map.get(&col) {
                ans += *cnt;
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (equal-pairs grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length grid))
         (rows grid)
         (cols
          (for/list ([j (in-range n)])
            (map (lambda (row) (list-ref row j)) rows))))
    (let loop ((i 0) (cnt 0))
      (if (= i n)
          cnt
          (let inner ((j 0) (c cnt))
            (if (= j n)
                (loop (+ i 1) c)
                (let ((row (list-ref rows i))
                      (col (list-ref cols j)))
                  (inner (+ j 1) (if (equal? row col) (+ c 1) c)))))))))
```

## Erlang

```erlang
-module(solution).
-export([equal_pairs/1]).

-spec equal_pairs(Grid :: [[integer()]]) -> integer().
equal_pairs(Grid) ->
    RowMap = build_row_map(Grid, #{}),
    count_columns(Grid, RowMap).

build_row_map([], Map) -> Map;
build_row_map([Row|Rest], Map) ->
    Updated = maps:update_with(Row,
                               fun(C) -> C + 1 end,
                               1,
                               Map),
    build_row_map(Rest, Updated).

count_columns(Grid, RowMap) ->
    N = length(Grid),
    lists:foldl(fun(J, Acc) ->
        Col = [lists:nth(J+1, Row) || Row <- Grid],
        Acc + maps:get(Col, RowMap, 0)
    end, 0, lists:seq(0, N-1)).
```

## Elixir

```elixir
defmodule Solution do
  @spec equal_pairs(grid :: [[integer]]) :: integer
  def equal_pairs(grid) do
    n = length(grid)

    rows_map =
      Enum.reduce(grid, %{}, fn row, acc ->
        key = List.to_tuple(row)
        Map.update(acc, key, 1, &(&1 + 1))
      end)

    0..(n - 1)
    |> Enum.reduce(0, fn j, sum ->
      col =
        Enum.map(grid, fn row -> Enum.at(row, j) end)

      key = List.to_tuple(col)
      sum + Map.get(rows_map, key, 0)
    end)
  end
end
```
