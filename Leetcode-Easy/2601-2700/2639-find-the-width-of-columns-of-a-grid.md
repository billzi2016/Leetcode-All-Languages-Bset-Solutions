# 2639. Find the Width of Columns of a Grid

## Cpp

```cpp
class Solution {
public:
    int numLength(int x) {
        int len = (x < 0);
        long long v = std::llabs(static_cast<long long>(x));
        if (v == 0) return len + 1;
        while (v > 0) {
            ++len;
            v /= 10;
        }
        return len;
    }

    vector<int> findColumnWidth(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<int> ans(n, 0);
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                ans[j] = max(ans[j], numLength(grid[i][j]));
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] findColumnWidth(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[] ans = new int[n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int len = length(grid[i][j]);
                if (len > ans[j]) {
                    ans[j] = len;
                }
            }
        }
        return ans;
    }

    private int length(int x) {
        long v = Math.abs((long) x);
        int cnt = 0;
        if (v == 0) {
            cnt = 1;
        } else {
            while (v > 0) {
                cnt++;
                v /= 10;
            }
        }
        if (x < 0) cnt++; // account for negative sign
        return cnt;
    }
}
```

## Python

```python
class Solution(object):
    def findColumnWidth(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        if not grid:
            return []
        m, n = len(grid), len(grid[0])
        ans = [0] * n
        for c in range(n):
            max_len = 0
            for r in range(m):
                cur_len = len(str(grid[r][c]))
                if cur_len > max_len:
                    max_len = cur_len
            ans[c] = max_len
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        if not grid:
            return []
        n = len(grid[0])
        ans = [0] * n
        for row in grid:
            for j, val in enumerate(row):
                length = len(str(val))
                if length > ans[j]:
                    ans[j] = length
        return ans
```

## C

```c
#include <stdlib.h>

static int numLength(int x) {
    if (x == 0) return 1;
    int len = 0;
    if (x < 0) {
        len++;          // sign
        x = -x;
    }
    while (x > 0) {
        len++;
        x /= 10;
    }
    return len;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findColumnWidth(int** grid, int gridSize, int* gridColSize, int* returnSize) {
    if (gridSize == 0 || gridColSize == NULL) {
        *returnSize = 0;
        return NULL;
    }
    
    int n = gridColSize[0];
    int* ans = (int*)malloc(sizeof(int) * n);
    for (int j = 0; j < n; ++j) ans[j] = 0;
    
    for (int i = 0; i < gridSize; ++i) {
        for (int j = 0; j < n; ++j) {
            int len = numLength(grid[i][j]);
            if (len > ans[j]) ans[j] = len;
        }
    }
    
    *returnSize = n;
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int[] FindColumnWidth(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        int[] ans = new int[n];
        for (int col = 0; col < n; col++) {
            int maxLen = 0;
            for (int row = 0; row < m; row++) {
                int len = grid[row][col].ToString().Length;
                if (len > maxLen) maxLen = len;
            }
            ans[col] = maxLen;
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number[]}
 */
var findColumnWidth = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    const ans = new Array(n).fill(0);
    
    for (let c = 0; c < n; ++c) {
        let maxLen = 0;
        for (let r = 0; r < m; ++r) {
            const len = grid[r][c].toString().length;
            if (len > maxLen) maxLen = len;
        }
        ans[c] = maxLen;
    }
    
    return ans;
};
```

## Typescript

```typescript
function findColumnWidth(grid: number[][]): number[] {
    const m = grid.length;
    if (m === 0) return [];
    const n = grid[0].length;
    const ans: number[] = new Array(n).fill(0);

    const digitLength = (x: number): number => {
        let len = 0;
        let y = Math.abs(x);
        do {
            len++;
            y = Math.floor(y / 10);
        } while (y > 0);
        return x < 0 ? len + 1 : len;
    };

    for (let col = 0; col < n; col++) {
        let maxLen = 0;
        for (let row = 0; row < m; row++) {
            const curLen = digitLength(grid[row][col]);
            if (curLen > maxLen) maxLen = curLen;
        }
        ans[col] = maxLen;
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer[]
     */
    function findColumnWidth($grid) {
        $m = count($grid);
        if ($m === 0) {
            return [];
        }
        $n = count($grid[0]);
        $ans = array_fill(0, $n, 0);
        for ($col = 0; $col < $n; $col++) {
            $maxLen = 0;
            for ($row = 0; $row < $m; $row++) {
                $len = strlen((string)$grid[$row][$col]);
                if ($len > $maxLen) {
                    $maxLen = $len;
                }
            }
            $ans[$col] = $maxLen;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func findColumnWidth(_ grid: [[Int]]) -> [Int] {
        guard let firstRow = grid.first else { return [] }
        var widths = Array(repeating: 0, count: firstRow.count)
        
        for row in grid {
            for (c, value) in row.enumerated() {
                let length = digitLength(value)
                if length > widths[c] {
                    widths[c] = length
                }
            }
        }
        return widths
    }
    
    private func digitLength(_ x: Int) -> Int {
        if x == 0 { return 1 }
        var len = 0
        var v = x
        if v < 0 {
            len += 1          // sign
            v = -v
        }
        while v > 0 {
            len += 1
            v /= 10
        }
        return len
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findColumnWidth(grid: Array<IntArray>): IntArray {
        val m = grid.size
        val n = grid[0].size
        val ans = IntArray(n)
        for (j in 0 until n) {
            var maxLen = 0
            for (i in 0 until m) {
                val len = grid[i][j].toString().length
                if (len > maxLen) maxLen = len
            }
            ans[j] = maxLen
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> findColumnWidth(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;
    List<int> ans = List.filled(n, 0);
    
    int numLength(int x) {
      if (x == 0) return 1;
      int cnt = 0;
      int y = x.abs();
      while (y > 0) {
        cnt++;
        y ~/= 10;
      }
      return x < 0 ? cnt + 1 : cnt;
    }
    
    for (int col = 0; col < n; ++col) {
      int maxLen = 0;
      for (int row = 0; row < m; ++row) {
        int len = numLength(grid[row][col]);
        if (len > maxLen) maxLen = len;
      }
      ans[col] = maxLen;
    }
    
    return ans;
  }
}
```

## Golang

```go
func findColumnWidth(grid [][]int) []int {
    if len(grid) == 0 || len(grid[0]) == 0 {
        return []int{}
    }
    m, n := len(grid), len(grid[0])
    ans := make([]int, n)

    // helper to compute length of an integer as defined
    numLen := func(x int) int {
        if x == 0 {
            return 1
        }
        if x < 0 {
            x = -x
            cnt := 0
            for x > 0 {
                cnt++
                x /= 10
            }
            return cnt + 1 // include sign
        }
        cnt := 0
        for x > 0 {
            cnt++
            x /= 10
        }
        return cnt
    }

    for c := 0; c < n; c++ {
        maxW := 0
        for r := 0; r < m; r++ {
            w := numLen(grid[r][c])
            if w > maxW {
                maxW = w
            }
        }
        ans[c] = maxW
    }
    return ans
}
```

## Ruby

```ruby
def find_column_width(grid)
  m = grid.size
  n = grid[0].size
  ans = Array.new(n, 0)
  (0...n).each do |c|
    max_len = 0
    (0...m).each do |r|
      val = grid[r][c]
      len = val.abs.to_s.length
      len += 1 if val < 0
      max_len = len if len > max_len
    end
    ans[c] = max_len
  end
  ans
end
```

## Scala

```scala
object Solution {
    def findColumnWidth(grid: Array[Array[Int]]): Array[Int] = {
        val m = grid.length
        if (m == 0) return Array.emptyIntArray
        val n = grid(0).length
        val ans = new Array[Int](n)

        def digitCount(x: Long): Int = {
            if (x == 0L) return 1
            var cnt = 0
            var num = x
            while (num > 0) {
                cnt += 1
                num /= 10
            }
            cnt
        }

        for (j <- 0 until n) {
            var maxLen = 0
            for (i <- 0 until m) {
                val v = grid(i)(j).toLong
                val len = if (v < 0) digitCount(-v) + 1 else digitCount(v)
                if (len > maxLen) maxLen = len
            }
            ans(j) = maxLen
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_column_width(grid: Vec<Vec<i32>>) -> Vec<i32> {
        let m = grid.len();
        if m == 0 {
            return vec![];
        }
        let n = grid[0].len();
        let mut ans = Vec::with_capacity(n);
        for col in 0..n {
            let mut max_len = 0;
            for row in 0..m {
                let x = grid[row][col];
                // compute length
                let len = if x == 0 {
                    1
                } else {
                    let mut len = 0;
                    let mut v: i64 = x as i64;
                    if v < 0 {
                        len += 1; // sign
                        v = -v;
                    }
                    while v > 0 {
                        len += 1;
                        v /= 10;
                    }
                    len
                };
                if len > max_len {
                    max_len = len;
                }
            }
            ans.push(max_len);
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (find-column-width grid)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ((n (if (null? grid) 0 (length (car grid)))))
    (build-list n
      (lambda (j)
        (apply max
               (map (lambda (row)
                      (string-length (number->string (list-ref row j))))
                    grid))))))
```

## Erlang

```erlang
-spec find_column_width(Grid :: [[integer()]]) -> [integer()].
find_column_width(Grid) ->
    case Grid of
        [] -> [];
        [First|Rest] ->
            N = length(First),
            Init = lists:duplicate(N, 0),
            Maxes = lists:foldl(fun(Row, Acc) -> update_row(Row, Acc) end,
                                Init, [First|Rest]),
            Maxes
    end.

update_row(Row, Acc) ->
    lists:zipwith(
        fun(Elem, Max) ->
            Len = int_len(Elem),
            if Len > Max -> Len; true -> Max end
        end,
        Row, Acc).

int_len(N) when is_integer(N) ->
    Abs = if N < 0 -> -N; true -> N end,
    Digits = case Abs of
        0 -> 1;
        _ -> digit_count(Abs)
    end,
    if N < 0 -> Digits + 1; true -> Digits end.

digit_count(N) when N > 0 ->
    digit_count(N, 0).

digit_count(0, Acc) -> Acc;
digit_count(N, Acc) ->
    digit_count(N div 10, Acc + 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_column_width(grid :: [[integer]]) :: [integer]
  def find_column_width(grid) do
    grid
    |> List.zip()
    |> Enum.map(fn col_tuple ->
      col_tuple
      |> Tuple.to_list()
      |> Enum.map(&Integer.to_string/1)
      |> Enum.map(&String.length/1)
      |> Enum.max()
    end)
  end
end
```
