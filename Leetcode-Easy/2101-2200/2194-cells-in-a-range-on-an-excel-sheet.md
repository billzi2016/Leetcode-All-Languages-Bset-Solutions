# 2194. Cells in a Range on an Excel Sheet

## Cpp

```cpp
class Solution {
public:
    vector<string> cellsInRange(string s) {
        char c1 = s[0];
        int r1 = s[1] - '0';
        char c2 = s[3];
        int r2 = s[4] - '0';
        vector<string> res;
        for (char col = c1; col <= c2; ++col) {
            for (int row = r1; row <= r2; ++row) {
                res.push_back(string(1, col) + to_string(row));
            }
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public java.util.List<String> cellsInRange(String s) {
        java.util.List<String> res = new java.util.ArrayList<>();
        char colStart = s.charAt(0);
        char rowStart = s.charAt(1);
        char colEnd = s.charAt(3);
        char rowEnd = s.charAt(4);
        for (char c = colStart; c <= colEnd; c++) {
            for (char r = rowStart; r <= rowEnd; r++) {
                res.add("" + c + r);
            }
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        col_start = ord(s[0])
        row_start = int(s[1])
        col_end = ord(s[3])
        row_end = int(s[4])
        res = []
        for c in range(col_start, col_end + 1):
            for r in range(row_start, row_end + 1):
                res.append(chr(c) + str(r))
        return res
```

## Python3

```python
from typing import List

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        c_start, r_start = s[0], int(s[1])
        c_end, r_end = s[3], int(s[4])
        result = []
        for col in range(ord(c_start), ord(c_end) + 1):
            for row in range(r_start, r_end + 1):
                result.append(chr(col) + str(row))
        return result
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** cellsInRange(char* s, int* returnSize) {
    char startCol = s[0];
    char startRow = s[1];
    char endCol   = s[3];
    char endRow   = s[4];

    int colStart = startCol - 'A';
    int colEnd   = endCol   - 'A';
    int rowStart = startRow - '0';
    int rowEnd   = endRow   - '0';

    int total = (colEnd - colStart + 1) * (rowEnd - rowStart + 1);
    char **result = (char **)malloc(total * sizeof(char *));
    int idx = 0;

    for (int c = colStart; c <= colEnd; ++c) {
        for (int r = rowStart; r <= rowEnd; ++r) {
            result[idx] = (char *)malloc(3 * sizeof(char));
            result[idx][0] = 'A' + c;
            result[idx][1] = '0' + r;
            result[idx][2] = '\0';
            ++idx;
        }
    }

    *returnSize = total;
    return result;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<string> CellsInRange(string s) {
        var result = new List<string>();
        char startCol = s[0];
        char endCol = s[3];
        int startRow = s[1] - '0';
        int endRow = s[4] - '0';

        for (char col = startCol; col <= endCol; col++) {
            for (int row = startRow; row <= endRow; row++) {
                result.Add($"{col}{row}");
            }
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string[]}
 */
var cellsInRange = function(s) {
    const startCol = s.charCodeAt(0);
    const startRow = parseInt(s[1], 10);
    const endCol = s.charCodeAt(3);
    const endRow = parseInt(s[4], 10);
    
    const result = [];
    for (let c = startCol; c <= endCol; c++) {
        const colChar = String.fromCharCode(c);
        for (let r = startRow; r <= endRow; r++) {
            result.push(colChar + r);
        }
    }
    return result;
};
```

## Typescript

```typescript
function cellsInRange(s: string): string[] {
    const res: string[] = [];
    const colStart = s.charCodeAt(0);
    const rowStart = parseInt(s[1]);
    const colEnd = s.charCodeAt(3);
    const rowEnd = parseInt(s[4]);

    for (let c = colStart; c <= colEnd; c++) {
        const col = String.fromCharCode(c);
        for (let r = rowStart; r <= rowEnd; r++) {
            res.push(col + r);
        }
    }
    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String[]
     */
    function cellsInRange($s) {
        $c1 = $s[0];
        $r1 = intval($s[1]);
        $c2 = $s[3];
        $r2 = intval($s[4]);

        $result = [];
        for ($col = ord($c1); $col <= ord($c2); $col++) {
            $colChar = chr($col);
            for ($row = $r1; $row <= $r2; $row++) {
                $result[] = $colChar . $row;
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func cellsInRange(_ s: String) -> [String] {
        let chars = Array(s)
        if chars.count != 5 { return [] }
        let colStart = chars[0]
        let rowStart = Int(String(chars[1]))!
        let colEnd = chars[3]
        let rowEnd = Int(String(chars[4]))!
        
        var result: [String] = []
        let startVal = colStart.unicodeScalars.first!.value
        let endVal = colEnd.unicodeScalars.first!.value
        
        for code in startVal...endVal {
            let colChar = Character(UnicodeScalar(code)!)
            for row in rowStart...rowEnd {
                result.append("\(colChar)\(row)")
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun cellsInRange(s: String): List<String> {
        val result = ArrayList<String>()
        for (col in s[0]..s[3]) {
            for (row in s[1]..s[4]) {
                result.add("" + col + row)
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<String> cellsInRange(String s) {
    int startCol = s.codeUnitAt(0);
    int endCol = s.codeUnitAt(3);
    int startRow = s.codeUnitAt(1);
    int endRow = s.codeUnitAt(4);
    List<String> result = [];
    for (int c = startCol; c <= endCol; c++) {
      for (int r = startRow; r <= endRow; r++) {
        result.add(String.fromCharCode(c) + String.fromCharCode(r));
      }
    }
    return result;
  }
}
```

## Golang

```go
func cellsInRange(s string) []string {
    startCol := s[0]
    endCol := s[3]
    startRow := s[1]
    endRow := s[4]

    result := make([]string, 0, int(endCol-startCol+1)*int(endRow-startRow+1))
    for c := startCol; c <= endCol; c++ {
        for r := startRow; r <= endRow; r++ {
            result = append(result, string([]byte{c, r}))
        }
    }
    return result
}
```

## Ruby

```ruby
def cells_in_range(s)
  col_start = s[0]
  row_start = s[1].to_i
  col_end   = s[3]
  row_end   = s[4].to_i

  result = []
  (col_start..col_end).each do |c|
    (row_start..row_end).each do |r|
      result << "#{c}#{r}"
    end
  end
  result
end
```

## Scala

```scala
object Solution {
    def cellsInRange(s: String): List[String] = {
        val startCol = s.charAt(0)
        val endCol   = s.charAt(3)
        val startRow = s.charAt(1) - '0'
        val endRow   = s.charAt(4) - '0'

        val buf = scala.collection.mutable.ListBuffer[String]()
        for (c <- startCol to endCol) {
            for (r <- startRow to endRow) {
                buf += s"$c$r"
            }
        }
        buf.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn cells_in_range(s: String) -> Vec<String> {
        let b = s.as_bytes();
        let start_col = b[0];
        let end_col = b[3];
        let start_row = b[1];
        let end_row = b[4];

        let mut res = Vec::new();
        for col in start_col..=end_col {
            for row in start_row..=end_row {
                res.push(format!("{}{}", col as char, row as char));
            }
        }
        res
    }
}
```

## Racket

```racket
(define/contract (cells-in-range s)
  (-> string? (listof string?))
  (let* ([c1 (string-ref s 0)]
         [r1 (char->integer (string-ref s 1))]
         [c2 (string-ref s 3)]
         [r2 (char->integer (string-ref s 4))])
    (let* ([row-start (- r1 (char->integer #\0))]
           [row-end   (- r2 (char->integer #\0))]
           [col-start (char->integer c1)]
           [col-end   (char->integer c2)])
      (for*/list ([col (in-range col-start (+ col-end 1))]
                  [row (in-range row-start (+ row-end 1))])
        (string-append (string (integer->char col))
                       (number->string row))))))
```

## Erlang

```erlang
-spec cells_in_range(S :: unicode:unicode_binary()) -> [unicode:unicode_binary()].
cells_in_range(S) ->
    <<C1, R1, $:, C2, R2>> = S,
    [<<C,R>> || C <- lists:seq(C1, C2), R <- lists:seq(R1, R2)].
```

## Elixir

```elixir
defmodule Solution do
  @spec cells_in_range(s :: String.t) :: [String.t]
  def cells_in_range(s) do
    col_start = :binary.part(s, 0, 1) |> :binary.decode_unsigned()
    col_end   = :binary.part(s, 3, 1) |> :binary.decode_unsigned()
    row_start = :binary.part(s, 1, 1) |> String.to_integer()
    row_end   = :binary.part(s, 4, 1) |> String.to_integer()

    Enum.flat_map(col_start..col_end, fn col_code ->
      col = <<col_code>>
      Enum.map(row_start..row_end, fn row -> "#{col}#{row}" end)
    end)
  end
end
```
