# 2075. Decode the Slanted Ciphertext

## Cpp

```cpp
class Solution {
public:
    string decodeCiphertext(string encodedText, int rows) {
        int n = encodedText.size();
        if (rows == 0) return "";
        int cols = n / rows;
        string res;
        res.reserve(n);
        for (int c = 0; c < cols; ++c) {
            for (int r = 0; r < rows; ++r) {
                res.push_back(encodedText[r * cols + c]);
            }
        }
        while (!res.empty() && res.back() == ' ') res.pop_back();
        return res;
    }
};
```

## Java

```java
class Solution {
    public String decodeCiphertext(String encodedText, int rows) {
        if (encodedText.isEmpty()) return "";
        int cols = encodedText.length() / rows;
        StringBuilder sb = new StringBuilder();
        // start from first row, each column
        for (int startCol = 0; startCol < cols; ++startCol) {
            int r = 0, c = startCol;
            while (r < rows && c >= 0) {
                char ch = encodedText.charAt(r * cols + c);
                if (ch != ' ') sb.append(ch);
                r++;
                c--;
            }
        }
        // then start from each row (except first) at last column
        for (int startRow = 1; startRow < rows; ++startRow) {
            int r = startRow, c = cols - 1;
            while (r < rows && c >= 0) {
                char ch = encodedText.charAt(r * cols + c);
                if (ch != ' ') sb.append(ch);
                r++;
                c--;
            }
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def decodeCiphertext(self, encodedText, rows):
        """
        :type encodedText: str
        :type rows: int
        :rtype: str
        """
        n = len(encodedText)
        if rows == 0 or n == 0:
            return ""
        cols = n // rows
        # build matrix row-wise
        mat = [list(encodedText[i*cols:(i+1)*cols]) for i in range(rows)]
        res = []
        # start from each column of the first row
        for c in range(cols):
            r, cc = 0, c
            while r < rows and cc < cols:
                res.append(mat[r][cc])
                r += 1
                cc += 1
        # then start from each row (except the first) of the first column
        for r_start in range(1, rows):
            r, c = r_start, 0
            while r < rows and c < cols:
                res.append(mat[r][c])
                r += 1
                c += 1
        return ''.join(res).rstrip(' ')
```

## Python3

```python
class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        if n == 0:
            return ""
        cols = n // rows
        res = []
        for d in range(cols):
            r, c = 0, d
            while r < rows and c < cols:
                res.append(encodedText[r * cols + c])
                r += 1
                c += 1
        return ''.join(res).rstrip()
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* decodeCiphertext(char* encodedText, int rows) {
    int L = strlen(encodedText);
    if (rows == 0) {
        char *empty = (char*)malloc(1);
        empty[0] = '\0';
        return empty;
    }
    int cols = rows ? L / rows : 0;
    char *res = (char*)malloc(L + 1);
    int pos = 0;

    // Start from each column of the first row
    for (int c = 0; c < cols; ++c) {
        int r = 0, cc = c;
        while (r < rows && cc < cols) {
            char ch = encodedText[r * cols + cc];
            if (ch != ' ') res[pos++] = ch;
            ++r;
            ++cc;
        }
    }

    // Start from each row of the first column (excluding the first row)
    for (int r = 1; r < rows; ++r) {
        int rr = r, c = 0;
        while (rr < rows && c < cols) {
            char ch = encodedText[rr * cols + c];
            if (ch != ' ') res[pos++] = ch;
            ++rr;
            ++c;
        }
    }

    res[pos] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string DecodeCiphertext(string encodedText, int rows) {
        if (rows == 0 || encodedText.Length == 0) return "";
        int n = encodedText.Length;
        int cols = n / rows;
        char[,] mat = new char[rows, cols];
        int idx = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                mat[i, j] = encodedText[idx++];
            }
        }
        var sb = new System.Text.StringBuilder();
        for (int j = 0; j < cols; j++) {
            for (int i = 0; i < rows; i++) {
                char c = mat[i, j];
                if (c != ' ') sb.Append(c);
            }
        }
        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} encodedText
 * @param {number} rows
 * @return {string}
 */
var decodeCiphertext = function(encodedText, rows) {
    const n = encodedText.length;
    if (rows === 1) return encodedText;
    const cols = Math.floor(n / rows);
    const result = [];

    // Diagonals starting from the first row
    for (let startCol = 0; startCol < cols; ++startCol) {
        let r = 0, c = startCol;
        while (r < rows && c < cols) {
            result.push(encodedText[r * cols + c]);
            r++;
            c++;
        }
    }

    // Diagonals starting from the first column (excluding the top-left cell)
    for (let startRow = 1; startRow < rows; ++startRow) {
        let r = startRow, c = 0;
        while (r < rows && c < cols) {
            result.push(encodedText[r * cols + c]);
            r++;
            c++;
        }
    }

    // Trim trailing spaces that were padding
    while (result.length && result[result.length - 1] === ' ') {
        result.pop();
    }

    return result.join('');
};
```

## Typescript

```typescript
function decodeCiphertext(encodedText: string, rows: number): string {
    const n = encodedText.length;
    if (n === 0) return "";
    const cols = Math.floor(n / rows);
    const mat: string[][] = new Array(rows);
    for (let i = 0; i < rows; ++i) {
        const slice = encodedText.slice(i * cols, (i + 1) * cols);
        mat[i] = slice.split('');
    }
    let res = "";
    // start from each column of the first row
    for (let startCol = 0; startCol < cols; ++startCol) {
        let r = 0, c = startCol;
        while (r < rows && c >= 0) {
            res += mat[r][c];
            ++r;
            --c;
        }
    }
    // then start from each row of the last column (excluding first row)
    for (let startRow = 1; startRow < rows; ++startRow) {
        let r = startRow, c = cols - 1;
        while (r < rows && c >= 0) {
            res += mat[r][c];
            ++r;
            --c;
        }
    }
    return res.replace(/ +$/g, "");
}
```

## Php

```php
class Solution {

    /**
     * @param String $encodedText
     * @param Integer $rows
     * @return String
     */
    function decodeCiphertext($encodedText, $rows) {
        $len = strlen($encodedText);
        if ($rows == 1 || $len == 0) {
            return $encodedText;
        }
        $cols = intdiv($len, $rows);
        $matrix = [];
        for ($i = 0; $i < $rows; $i++) {
            $matrix[$i] = substr($encodedText, $i * $cols, $cols);
        }

        $result = '';
        // start from top row, each column
        for ($startCol = 0; $startCol < $cols; $startCol++) {
            $r = 0;
            $c = $startCol;
            while ($r < $rows && $c < $cols) {
                $ch = $matrix[$r][$c];
                if ($ch !== ' ') {
                    $result .= $ch;
                }
                $r++;
                $c++;
            }
        }
        // start from rows 1..rows-1, first column
        for ($startRow = 1; $startRow < $rows; $startRow++) {
            $r = $startRow;
            $c = 0;
            while ($r < $rows && $c < $cols) {
                $ch = $matrix[$r][$c];
                if ($ch !== ' ') {
                    $result .= $ch;
                }
                $r++;
                $c++;
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func decodeCiphertext(_ encodedText: String, _ rows: Int) -> String {
        let n = encodedText.count
        if rows == 0 || n == 0 { return "" }
        let cols = n / rows
        let chars = Array(encodedText)
        var result = ""
        for startCol in 0..<cols {
            var r = 0
            var c = startCol
            while r < rows && c < cols {
                let ch = chars[r * cols + c]
                if ch != " " {
                    result.append(ch)
                }
                r += 1
                c += 1
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun decodeCiphertext(encodedText: String, rows: Int): String {
        val n = encodedText.length
        if (n == 0) return ""
        val cols = n / rows
        val sb = StringBuilder()
        for (c in 0 until cols) {
            var r = 0
            while (r < rows) {
                val ch = encodedText[r * cols + c]
                if (ch != ' ') sb.append(ch)
                r++
            }
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String decodeCiphertext(String encodedText, int rows) {
    int n = encodedText.length;
    if (n == 0) return "";
    int cols = n ~/ rows;

    StringBuffer sb = StringBuffer();

    // start from each column of the first row
    for (int cStart = 0; cStart < cols; ++cStart) {
      int r = 0, c = cStart;
      while (r < rows && c < cols) {
        sb.write(encodedText[r * cols + c]);
        r++;
        c++;
      }
    }

    // start from each row of the first column (excluding the top-left cell)
    for (int rStart = 1; rStart < rows; ++rStart) {
      int r = rStart, c = 0;
      while (r < rows && c < cols) {
        sb.write(encodedText[r * cols + c]);
        r++;
        c++;
      }
    }

    // remove trailing spaces
    String res = sb.toString();
    int end = res.length;
    while (end > 0 && res.codeUnitAt(end - 1) == 32) { // ASCII space
      end--;
    }
    return res.substring(0, end);
  }
}
```

## Golang

```go
import "strings"

func decodeCiphertext(encodedText string, rows int) string {
	if rows == 0 {
		return ""
	}
	n := len(encodedText)
	cols := n / rows

	var sb strings.Builder
	for c := 0; c < cols; c++ {
		i, j := 0, c
		for i < rows && j < cols {
			sb.WriteByte(encodedText[i*cols+j])
			i++
			j++
		}
	}
	for r := 1; r < rows; r++ {
		i, j := r, 0
		for i < rows && j < cols {
			sb.WriteByte(encodedText[i*cols+j])
			i++
			j++
		}
	}
	return strings.TrimRight(sb.String(), " ")
}
```

## Ruby

```ruby
def decode_ciphertext(encoded_text, rows)
  n = encoded_text.length
  return "" if n == 0
  cols = n / rows
  matrix = Array.new(rows) { |i| encoded_text[i * cols, cols] }
  result = +''
  (0...cols).each do |c|
    r = 0
    col = c
    while r < rows && col < cols
      b = matrix[r].getbyte(col)
      result << b.chr if b != 32 # space character
      r += 1
      col += 1
    end
  end
  result
end
```

## Scala

```scala
object Solution {
    def decodeCiphertext(encodedText: String, rows: Int): String = {
        val n = encodedText.length
        if (n == 0) return ""
        val cols = n / rows
        val grid = Array.ofDim[Char](rows, cols)
        var idx = 0
        for (r <- 0 until rows) {
            for (c <- 0 until cols) {
                grid(r)(c) = encodedText.charAt(idx)
                idx += 1
            }
        }
        val sb = new StringBuilder()
        for (startCol <- 0 until cols) {
            var r = 0
            var c = startCol
            while (r < rows && c < cols) {
                sb.append(grid(r)(c))
                r += 1
                c += 1
            }
        }
        val res = sb.toString()
        var end = res.length - 1
        while (end >= 0 && res.charAt(end) == ' ') {
            end -= 1
        }
        if (end < 0) "" else res.substring(0, end + 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn decode_ciphertext(encoded_text: String, rows: i32) -> String {
        let r = rows as usize;
        if encoded_text.is_empty() || r == 0 {
            return String::new();
        }
        let n = encoded_text.len();
        let c = n / r; // number of columns
        let bytes = encoded_text.as_bytes();

        let mut result = String::with_capacity(n);

        // start from each column in the first row
        for start_col in 0..c {
            let mut row = 0usize;
            let mut col = start_col;
            while row < r && col < c {
                result.push(bytes[row * c + col] as char);
                row += 1;
                col += 1;
            }
        }

        // then start from each row (except the first) in the first column
        for start_row in 1..r {
            let mut row = start_row;
            let mut col = 0usize;
            while row < r && col < c {
                result.push(bytes[row * c + col] as char);
                row += 1;
                col += 1;
            }
        }

        // remove trailing spaces added during encoding
        while result.ends_with(' ') {
            result.pop();
        }

        result
    }
}
```

## Racket

```racket
(define/contract (decode-ciphertext encodedText rows)
  (-> string? exact-integer? string?)
  (let* ((n (string-length encodedText))
         (cols (quotient n rows))
         (out (open-output-string)))
    (for ([start-col (in-range cols)])
      (let loop ((r 0) (c start-col))
        (when (and (< r rows) (>= c 0))
          (let ((ch (string-ref encodedText (+ (* r cols) c))))
            (unless (char=? ch #\space)
              (write-char ch out)))
          (loop (+ r 1) (- c 1)))))
    (get-output-string out)))
```

## Erlang

```erlang
-module(solution).
-export([decode_ciphertext/2]).

-spec decode_ciphertext(EncodedText :: unicode:unicode_binary(), Rows :: integer()) -> unicode:unicode_binary().
decode_ciphertext(EncodedText, Rows) ->
    Len = byte_size(EncodedText),
    Cols = case Rows of
        0 -> 0;
        _ -> Len div Rows
    end,
    CharsRev = decode_offsets(0, Cols, Rows, Cols, EncodedText, []),
    list_to_binary(lists:reverse(CharsRev)).

decode_offsets(CurC, MaxC, _Rows, _Cols, _EncodedText, Acc) when CurC >= MaxC ->
    Acc;
decode_offsets(CurC, MaxC, Rows, Cols, EncodedText, Acc) ->
    Acc1 = decode_rows(CurC, 0, Rows, Cols, EncodedText, Acc),
    decode_offsets(CurC + 1, MaxC, Rows, Cols, EncodedText, Acc1).

decode_rows(_OffsetC, CurR, Rows, _Cols, _EncodedText, Acc) when CurR >= Rows ->
    Acc;
decode_rows(OffsetC, CurR, Rows, Cols, EncodedText, Acc) ->
    Index = CurR * Cols + ((OffsetC + CurR) rem Cols),
    Char = binary:at(EncodedText, Index),
    NewAcc = if Char =:= $  -> Acc; true -> [Char | Acc] end,
    decode_rows(OffsetC, CurR + 1, Rows, Cols, EncodedText, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec decode_ciphertext(encoded_text :: String.t(), rows :: integer) :: String.t()
  def decode_ciphertext(encoded_text, rows) do
    len = byte_size(encoded_text)

    if len == 0 do
      ""
    else
      cols = div(len, rows)

      row_bins =
        0..(rows - 1)
        |> Enum.map(fn i -> :binary.part(encoded_text, i * cols, cols) end)
        |> List.to_tuple()

      result_rev =
        0..(cols - 1)
        |> Enum.reduce([], fn c, acc ->
          collect(row_bins, rows, cols, 0, c, acc)
        end)

      result_rev =
        1..(rows - 1)
        |> Enum.reduce(result_rev, fn r_start, acc ->
          collect(row_bins, rows, cols, r_start, 0, acc)
        end)

      result_rev
      |> Enum.reverse()
      |> List.to_string()
    end
  end

  defp collect(matrix, rows, cols, r, c, acc) do
    if r < rows and c < cols do
      row_bin = elem(matrix, r)
      ch = :binary.at(row_bin, c)

      new_acc =
        if ch != ?\s do
          [ch | acc]
        else
          acc
        end

      collect(matrix, rows, cols, r + 1, c + 1, new_acc)
    else
      acc
    end
  end
end
```
