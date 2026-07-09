# 0006. Zigzag Conversion

## Cpp

```cpp
class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1 || numRows >= (int)s.size()) return s;
        vector<string> rows(min(numRows, (int)s.size()));
        int curRow = 0;
        bool goingDown = false;
        for (char c : s) {
            rows[curRow] += c;
            if (curRow == 0 || curRow == numRows - 1) goingDown = !goingDown;
            curRow += goingDown ? 1 : -1;
        }
        string result;
        result.reserve(s.size());
        for (const string& row : rows) result += row;
        return result;
    }
};
```

## Java

```java
class Solution {
    public String convert(String s, int numRows) {
        if (numRows == 1 || numRows >= s.length()) {
            return s;
        }
        StringBuilder[] rows = new StringBuilder[numRows];
        for (int i = 0; i < numRows; i++) {
            rows[i] = new StringBuilder();
        }
        int curRow = 0;
        boolean goingDown = false;
        for (char c : s.toCharArray()) {
            rows[curRow].append(c);
            if (curRow == 0 || curRow == numRows - 1) {
                goingDown = !goingDown;
            }
            curRow += goingDown ? 1 : -1;
        }
        StringBuilder result = new StringBuilder(s.length());
        for (StringBuilder row : rows) {
            result.append(row);
        }
        return result.toString();
    }
}
```

## Python

```python
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [''] * numRows
        cur = 0
        step = 1
        for ch in s:
            rows[cur] += ch
            if cur == 0:
                step = 1
            elif cur == numRows - 1:
                step = -1
            cur += step
        return ''.join(rows)
```

## Python3

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [''] * numRows
        cur = 0
        step = -1
        for ch in s:
            rows[cur] += ch
            if cur == 0 or cur == numRows - 1:
                step = -step
            cur += step
        return ''.join(rows)
```

## C

```c
#include <stdlib.h>
#include <string.h>

static char *copy_string(const char *src) {
    size_t len = strlen(src);
    char *dst = (char *)malloc(len + 1);
    if (dst) memcpy(dst, src, len + 1);
    return dst;
}

char* convert(char* s, int numRows) {
    if (!s) return NULL;
    int n = (int)strlen(s);
    if (numRows == 1 || numRows >= n) {
        return copy_string(s);
    }

    char **rows = (char **)malloc(numRows * sizeof(char *));
    int *pos = (int *)calloc(numRows, sizeof(int));
    for (int i = 0; i < numRows; ++i) {
        rows[i] = (char *)calloc(n + 1, 1);
    }

    int curRow = 0;
    int dir = -1; // will flip to 1 on first iteration
    for (int i = 0; i < n; ++i) {
        rows[curRow][pos[curRow]++] = s[i];
        if (curRow == 0 || curRow == numRows - 1) dir = -dir;
        curRow += dir;
    }

    char *result = (char *)malloc(n + 1);
    int idx = 0;
    for (int i = 0; i < numRows; ++i) {
        if (pos[i] > 0) {
            memcpy(result + idx, rows[i], pos[i]);
            idx += pos[i];
        }
        free(rows[i]);
    }
    result[n] = '\0';

    free(rows);
    free(pos);
    return result;
}
```

## Csharp

```csharp
using System.Text;

public class Solution {
    public string Convert(string s, int numRows) {
        if (numRows == 1 || numRows >= s.Length) return s;
        
        StringBuilder[] rows = new StringBuilder[numRows];
        for (int i = 0; i < numRows; i++) rows[i] = new StringBuilder();
        
        int curRow = 0;
        bool goingDown = false;
        
        foreach (char c in s) {
            rows[curRow].Append(c);
            if (curRow == 0 || curRow == numRows - 1) goingDown = !goingDown;
            curRow += goingDown ? 1 : -1;
        }
        
        StringBuilder result = new StringBuilder(s.Length);
        foreach (var sb in rows) result.Append(sb);
        return result.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    if (numRows === 1 || numRows >= s.length) return s;
    const rows = new Array(numRows).fill('');
    let curRow = 0;
    let goingDown = false;
    for (const ch of s) {
        rows[curRow] += ch;
        if (curRow === 0 || curRow === numRows - 1) goingDown = !goingDown;
        curRow += goingDown ? 1 : -1;
    }
    return rows.join('');
};
```

## Typescript

```typescript
function convert(s: string, numRows: number): string {
    if (numRows === 1 || numRows >= s.length) return s;
    const rows: string[] = new Array(numRows).fill('');
    let curRow = 0;
    let goingDown = false;
    for (const ch of s) {
        rows[curRow] += ch;
        if (curRow === 0 || curRow === numRows - 1) goingDown = !goingDown;
        curRow += goingDown ? 1 : -1;
    }
    return rows.join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $numRows
     * @return String
     */
    function convert($s, $numRows) {
        $len = strlen($s);
        if ($numRows <= 1 || $numRows >= $len) {
            return $s;
        }

        $rows = array_fill(0, $numRows, '');
        $currentRow = 0;
        $goingDown = false;

        for ($i = 0; $i < $len; $i++) {
            $rows[$currentRow] .= $s[$i];
            if ($currentRow == 0 || $currentRow == $numRows - 1) {
                $goingDown = !$goingDown;
            }
            $currentRow += $goingDown ? 1 : -1;
        }

        return implode('', $rows);
    }
}
```

## Swift

```swift
class Solution {
    func convert(_ s: String, _ numRows: Int) -> String {
        if numRows == 1 || numRows >= s.count {
            return s
        }
        var rows = Array(repeating: "", count: numRows)
        var currentRow = 0
        var goingDown = false
        
        for ch in s {
            rows[currentRow].append(ch)
            if currentRow == 0 || currentRow == numRows - 1 {
                goingDown.toggle()
            }
            currentRow += goingDown ? 1 : -1
        }
        
        return rows.joined()
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun convert(s: String, numRows: Int): String {
        if (numRows == 1 || numRows >= s.length) return s
        val rows = Array(numRows) { StringBuilder() }
        var curRow = 0
        var goingDown = false
        for (c in s) {
            rows[curRow].append(c)
            if (curRow == 0 || curRow == numRows - 1) goingDown = !goingDown
            curRow += if (goingDown) 1 else -1
        }
        val result = StringBuilder()
        for (row in rows) {
            result.append(row)
        }
        return result.toString()
    }
}
```

## Dart

```dart
class Solution {
  String convert(String s, int numRows) {
    if (numRows == 1 || numRows >= s.length) return s;
    List<StringBuffer> rows = List.generate(numRows, (_) => StringBuffer());
    int curRow = 0;
    bool goingDown = false;
    for (int i = 0; i < s.length; i++) {
      rows[curRow].write(s[i]);
      if (curRow == 0 || curRow == numRows - 1) {
        goingDown = !goingDown;
      }
      curRow += goingDown ? 1 : -1;
    }
    StringBuffer result = StringBuffer();
    for (var row in rows) {
      result.write(row);
    }
    return result.toString();
  }
}
```

## Golang

```go
func convert(s string, numRows int) string {
	if numRows <= 1 || numRows >= len(s) {
		return s
	}
	rows := make([][]byte, numRows)
	curRow, goingDown := 0, false
	for i := 0; i < len(s); i++ {
		rows[curRow] = append(rows[curRow], s[i])
		if curRow == 0 || curRow == numRows-1 {
			goingDown = !goingDown
		}
		if goingDown {
			curRow++
		} else {
			curRow--
		}
	}
	var result []byte
	for _, r := range rows {
		result = append(result, r...)
	}
	return string(result)
}
```

## Ruby

```ruby
def convert(s, num_rows)
  return s if num_rows == 1 || s.length <= num_rows
  rows = Array.new(num_rows) { '' }
  cur = 0
  step = 1
  s.each_char do |ch|
    rows[cur] << ch
    step = -1 if cur == num_rows - 1
    step = 1 if cur == 0
    cur += step
  end
  rows.join
end
```

## Scala

```scala
object Solution {
    def convert(s: String, numRows: Int): String = {
        if (numRows == 1 || numRows >= s.length) return s
        val rows = Array.fill(numRows)(new StringBuilder)
        var curRow = 0
        var goingDown = false
        for (c <- s) {
            rows(curRow).append(c)
            if (curRow == 0 || curRow == numRows - 1) goingDown = !goingDown
            curRow += (if (goingDown) 1 else -1)
        }
        val result = new StringBuilder
        for (row <- rows) result.append(row)
        result.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn convert(s: String, num_rows: i32) -> String {
        let n = s.len();
        let rows = num_rows as usize;
        if rows == 1 || rows >= n {
            return s;
        }
        let mut lines: Vec<String> = vec![String::new(); rows];
        let mut cur: usize = 0;
        let mut down = true;

        for ch in s.chars() {
            lines[cur].push(ch);
            if down {
                if cur + 1 == rows {
                    down = false;
                    cur -= 1;
                } else {
                    cur += 1;
                }
            } else {
                if cur == 0 {
                    down = true;
                    cur += 1;
                } else {
                    cur -= 1;
                }
            }
        }

        lines.concat()
    }
}
```

## Racket

```racket
(define/contract (convert s numRows)
  (-> string? exact-integer? string?)
  (let ((len (string-length s)))
    (if (or (= numRows 1) (>= numRows len))
        s
        (let* ((nrows numRows)
               (rows (make-vector nrows '())))
          ;; fill rows
          (let loop ((i 0) (row 0) (step 1))
            (if (= i len)
                (let ((result ""))
                  (for ([r (in-range nrows)])
                    (let* ((lst (vector-ref rows r))
                           (str (list->string (reverse lst))))
                      (set! result (string-append result str))))
                  result)
                (begin
                  (let* ((ch (string-ref s i))
                         (updated (cons ch (vector-ref rows row))))
                    (vector-set! rows row updated))
                  (define new-step
                    (cond [(= row 0) 1]
                          [(= row (- nrows 1)) -1]
                          [else step]))
                  (loop (+ i 1) (+ row new-step) new-step))))))))
```

## Erlang

```erlang
-module(solution).
-export([convert/2]).

-spec convert(S :: unicode:unicode_binary(), NumRows :: integer()) -> unicode:unicode_binary().
convert(S, NumRows) when NumRows =< 1 ->
    S;
convert(S, NumRows) ->
    Chars = unicode:characters_to_list(S),
    RowMap0 = maps:from_list([{I, []} || I <- lists:seq(0, NumRows - 1)]),
    {RowMap,_}=lists:foldl(
        fun(Char,{Map,{Idx,Dir}}) ->
            UpdatedMap = maps:update_with(
                Idx,
                fun(L) -> [Char|L] end,
                [],
                Map
            ),
            Next = next_idx_dir(Idx, Dir, NumRows),
            {UpdatedMap, Next}
        end,
        {RowMap0,{0,1}},
        Chars
    ),
    ResultChars = lists:foldl(
        fun(I, Acc) ->
            RowRev = maps:get(I, RowMap),
            Row = lists:reverse(RowRev),
            Row ++ Acc
        end,
        [],
        lists:seq(0, NumRows - 1)
    ),
    unicode:characters_to_binary(ResultChars).

-spec next_idx_dir(Index :: integer(), Dir :: integer(), NumRows :: integer()) -> {integer(), integer()}.
next_idx_dir(0, _Dir, _NumRows) ->
    {1, 1};
next_idx_dir(Index, _Dir, NumRows) when Index =:= NumRows - 1 ->
    {Index - 1, -1};
next_idx_dir(Index, Dir, _NumRows) ->
    {Index + Dir, Dir}.
```

## Elixir

```elixir
defmodule Solution do
  @spec convert(s :: String.t(), num_rows :: integer) :: String.t()
  def convert(s, num_rows) do
    cond do
      num_rows <= 1 or num_rows >= String.length(s) ->
        s

      true ->
        graphemes = String.graphemes(s)
        init_rows = List.duplicate([], num_rows)

        {rows, _, _} =
          Enum.reduce(graphemes, {init_rows, 0, 1}, fn ch, {rows_acc, cur, dir} ->
            rows_updated = List.update_at(rows_acc, cur, fn lst -> [ch | lst] end)

            new_dir =
              cond do
                cur == 0 -> 1
                cur == num_rows - 1 -> -1
                true -> dir
              end

            {rows_updated, cur + new_dir, new_dir}
          end)

        rows
        |> Enum.map(&Enum.reverse/1)
        |> Enum.join()
    end
  end
end
```
