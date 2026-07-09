# 1072. Flip Columns For Maximum Number of Equal Rows

## Cpp

```cpp
class Solution {
public:
    int maxEqualRowsAfterFlips(vector<vector<int>>& matrix) {
        unordered_map<string,int> freq;
        int best = 0;
        for (const auto& row : matrix) {
            string pattern;
            pattern.reserve(row.size());
            int first = row[0];
            for (int val : row) {
                pattern.push_back(val == first ? '0' : '1');
            }
            ++freq[pattern];
            best = max(best, freq[pattern]);
        }
        return best;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int maxEqualRowsAfterFlips(int[][] matrix) {
        Map<String, Integer> freq = new HashMap<>();
        int max = 0;
        for (int[] row : matrix) {
            StringBuilder sb = new StringBuilder();
            int first = row[0];
            for (int val : row) {
                sb.append(val == first ? '0' : '1');
            }
            String key = sb.toString();
            int count = freq.getOrDefault(key, 0) + 1;
            freq.put(key, count);
            if (count > max) {
                max = count;
            }
        }
        return max;
    }
}
```

## Python

```python
class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        freq = {}
        for row in matrix:
            first = row[0]
            pattern = tuple(x == first for x in row)
            freq[pattern] = freq.get(pattern, 0) + 1
        return max(freq.values()) if freq else 0
```

## Python3

```python
from typing import List
from collections import Counter

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        freq = Counter()
        for row in matrix:
            first = row[0]
            pattern = tuple(val ^ first for val in row)
            freq[pattern] += 1
        return max(freq.values()) if freq else 0
```

## C

```c
#include <stdbool.h>

int maxEqualRowsAfterFlips(int** matrix, int matrixSize, int* matrixColSize) {
    if (matrixSize == 0) return 0;
    int cols = matrixColSize[0];
    int best = 0;

    for (int i = 0; i < matrixSize; ++i) {
        int cnt = 0;
        for (int j = 0; j < matrixSize; ++j) {
            bool same = true, opposite = true;
            for (int k = 0; k < cols; ++k) {
                if (matrix[j][k] != matrix[i][k]) same = false;
                if (matrix[j][k] == matrix[i][k]) opposite = false;
                if (!same && !opposite) break;
            }
            if (same || opposite) cnt++;
        }
        if (cnt > best) best = cnt;
    }

    return best;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxEqualRowsAfterFlips(int[][] matrix) {
        var freq = new Dictionary<string, int>();
        int max = 0;
        foreach (var row in matrix) {
            var sb = new System.Text.StringBuilder(row.Length);
            int first = row[0];
            for (int i = 0; i < row.Length; i++) {
                sb.Append(row[i] == first ? '0' : '1');
            }
            string key = sb.ToString();
            if (freq.ContainsKey(key))
                freq[key]++;
            else
                freq[key] = 1;
            if (freq[key] > max) max = freq[key];
        }
        return max;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} matrix
 * @return {number}
 */
var maxEqualRowsAfterFlips = function(matrix) {
    const freq = new Map();
    let maxCount = 0;
    for (const row of matrix) {
        const first = row[0];
        let pattern = '';
        for (let i = 0; i < row.length; ++i) {
            pattern += (row[i] === first ? '0' : '1');
        }
        const cnt = (freq.get(pattern) || 0) + 1;
        freq.set(pattern, cnt);
        if (cnt > maxCount) maxCount = cnt;
    }
    return maxCount;
};
```

## Typescript

```typescript
function maxEqualRowsAfterFlips(matrix: number[][]): number {
    const freq = new Map<string, number>();
    let maxCount = 0;
    for (const row of matrix) {
        const first = row[0];
        let key = '';
        for (const val of row) {
            key += val === first ? '0' : '1';
        }
        const count = (freq.get(key) ?? 0) + 1;
        freq.set(key, count);
        if (count > maxCount) maxCount = count;
    }
    return maxCount;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $matrix
     * @return Integer
     */
    function maxEqualRowsAfterFlips($matrix) {
        $freq = [];
        $max = 0;
        foreach ($matrix as $row) {
            if (empty($row)) continue;
            $first = $row[0];
            $key = '';
            foreach ($row as $val) {
                $key .= ($val == $first) ? '0' : '1';
            }
            if (!isset($freq[$key])) {
                $freq[$key] = 0;
            }
            $freq[$key]++;
            if ($freq[$key] > $max) {
                $max = $freq[$key];
            }
        }
        return $max;
    }
}
```

## Swift

```swift
class Solution {
    func maxEqualRowsAfterFlips(_ matrix: [[Int]]) -> Int {
        var patternCount = [String: Int]()
        var maxRows = 0
        
        for row in matrix {
            guard let first = row.first else { continue }
            var chars = [Character]()
            chars.reserveCapacity(row.count)
            
            for value in row {
                if value == first {
                    chars.append("0")
                } else {
                    chars.append("1")
                }
            }
            
            let pattern = String(chars)
            patternCount[pattern, default: 0] += 1
            if let cnt = patternCount[pattern] {
                maxRows = max(maxRows, cnt)
            }
        }
        
        return maxRows
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxEqualRowsAfterFlips(matrix: Array<IntArray>): Int {
        val freq = HashMap<String, Int>()
        var maxCount = 0
        for (row in matrix) {
            val first = row[0]
            val sb = StringBuilder()
            for (v in row) {
                if (v == first) sb.append('0') else sb.append('1')
            }
            val key = sb.toString()
            val cnt = (freq[key] ?: 0) + 1
            freq[key] = cnt
            if (cnt > maxCount) maxCount = cnt
        }
        return maxCount
    }
}
```

## Dart

```dart
class Solution {
  int maxEqualRowsAfterFlips(List<List<int>> matrix) {
    final Map<String, int> freq = {};
    int maxCount = 0;
    for (final row in matrix) {
      final int first = row[0];
      final StringBuffer sb = StringBuffer();
      for (final val in row) {
        sb.write(val == first ? '0' : '1');
      }
      final String key = sb.toString();
      freq[key] = (freq[key] ?? 0) + 1;
      if (freq[key]! > maxCount) {
        maxCount = freq[key]!;
      }
    }
    return maxCount;
  }
}
```

## Golang

```go
func maxEqualRowsAfterFlips(matrix [][]int) int {
    if len(matrix) == 0 {
        return 0
    }
    nCols := len(matrix[0])
    freq := make(map[string]int)
    maxCount := 0

    for _, row := range matrix {
        pattern := make([]byte, nCols)
        first := row[0]
        for j, v := range row {
            if v == first {
                pattern[j] = '0'
            } else {
                pattern[j] = '1'
            }
        }
        key := string(pattern)
        freq[key]++
        if freq[key] > maxCount {
            maxCount = freq[key]
        }
    }

    return maxCount
}
```

## Ruby

```ruby
def max_equal_rows_after_flips(matrix)
  freq = Hash.new(0)
  matrix.each do |row|
    first = row[0]
    key = row.map { |v| v ^ first }.join
    freq[key] += 1
  end
  freq.values.max || 0
end
```

## Scala

```scala
object Solution {
  def maxEqualRowsAfterFlips(matrix: Array[Array[Int]]): Int = {
    val freq = scala.collection.mutable.Map[String, Int]()
    var maxCount = 0
    for (row <- matrix) {
      val sb = new java.lang.StringBuilder()
      val first = row(0)
      var i = 0
      while (i < row.length) {
        if (row(i) == first) sb.append('1') else sb.append('0')
        i += 1
      }
      val key = sb.toString()
      val newCount = freq.getOrElse(key, 0) + 1
      freq.update(key, newCount)
      if (newCount > maxCount) maxCount = newCount
    }
    maxCount
  }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn max_equal_rows_after_flips(matrix: Vec<Vec<i32>>) -> i32 {
        let mut freq: HashMap<Vec<i32>, i32> = HashMap::new();
        let mut ans = 0;
        for row in matrix.iter() {
            if row.is_empty() {
                continue;
            }
            let first = row[0];
            let pattern: Vec<i32> = row.iter().map(|&v| if v == first { 0 } else { 1 }).collect();
            let counter = freq.entry(pattern).or_insert(0);
            *counter += 1;
            if *counter > ans {
                ans = *counter;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (max-equal-rows-after-flips matrix)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let ((freq (make-hash)))
    (for ([row matrix])
      (let* ((first (car row))
             (pattern (map (lambda (v) (if (= v first) 0 1)) row))
             (prev (hash-ref freq pattern 0)))
        (hash-set! freq pattern (+ prev 1))))
    (define max-count 0)
    (for ([cnt (in-hash-values freq)])
      (when (> cnt max-count)
        (set! max-count cnt)))
    max-count))
```

## Erlang

```erlang
-spec max_equal_rows_after_flips(Matrix :: [[integer()]]) -> integer().
max_equal_rows_after_flips([]) ->
    0;
max_equal_rows_after_flips(Matrix) ->
    CountMap = lists:foldl(
        fun(Row, Acc) ->
            [First | Rest] = Row,
            Pattern = [ (V bxor First) || V <- Rest ],
            FullPattern = [0 | Pattern],
            maps:update_with(FullPattern, fun(C) -> C + 1 end, 1, Acc)
        end,
        #{},
        Matrix
    ),
    lists:max([Count || {_Key, Count} <- maps:to_list(CountMap)]).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_equal_rows_after_flips(matrix :: [[integer]]) :: integer
  def max_equal_rows_after_flips(matrix) do
    freq =
      Enum.reduce(matrix, %{}, fn row, acc ->
        [first | _] = row

        pattern =
          row
          |> Enum.map(fn x -> if x == first, do: ?0, else: ?1 end)
          |> List.to_string()

        Map.update(acc, pattern, 1, &(&1 + 1))
      end)

    freq
    |> Map.values()
    |> Enum.max()
  end
end
```
