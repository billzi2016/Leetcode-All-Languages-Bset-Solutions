# 0036. Valid Sudoku

## Cpp

```cpp
class Solution {
public:
    bool isValidSudoku(std::vector<std::vector<char>>& board) {
        int rows[9] = {0}, cols[9] = {0}, boxes[9] = {0};
        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                char c = board[i][j];
                if (c == '.') continue;
                int d = c - '1';
                int mask = 1 << d;
                if (rows[i] & mask) return false;
                rows[i] |= mask;
                if (cols[j] & mask) return false;
                cols[j] |= mask;
                int boxIdx = (i / 3) * 3 + j / 3;
                if (boxes[boxIdx] & mask) return false;
                boxes[boxIdx] |= mask;
            }
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean isValidSudoku(char[][] board) {
        // rows[row][digit], cols[col][digit], boxes[boxIndex][digit]
        boolean[][] rows = new boolean[9][10];
        boolean[][] cols = new boolean[9][10];
        boolean[][] boxes = new boolean[9][10];

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char c = board[i][j];
                if (c == '.') continue;
                int d = c - '0';
                if (rows[i][d]) return false;
                rows[i][d] = true;

                if (cols[j][d]) return false;
                cols[j][d] = true;

                int boxIndex = (i / 3) * 3 + j / 3;
                if (boxes[boxIndex][d]) return false;
                boxes[boxIndex][d] = true;
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                if val in rows[i]:
                    return False
                rows[i].add(val)

                if val in cols[j]:
                    return False
                cols[j].add(val)

                bi, bj = i // 3, j // 3
                if val in boxes[bi][bj]:
                    return False
                boxes[bi][bj].add(val)
        return True
```

## Python3

```python
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                if val in rows[i] or val in cols[j]:
                    return False
                box_idx = (i // 3) * 3 + (j // 3)
                if val in boxes[box_idx]:
                    return False
                rows[i].add(val)
                cols[j].add(val)
                boxes[box_idx].add(val)

        return True
```

## C

```c
#include <stdbool.h>

bool isValidSudoku(char** board, int boardSize, int* boardColSize) {
    int rows[9] = {0}, cols[9] = {0}, boxes[9] = {0};
    for (int i = 0; i < boardSize; ++i) {
        for (int j = 0; j < boardColSize[i]; ++j) {
            char c = board[i][j];
            if (c == '.') continue;
            int d = c - '1';
            int mask = 1 << d;
            if (rows[i] & mask) return false;
            rows[i] |= mask;
            if (cols[j] & mask) return false;
            cols[j] |= mask;
            int boxIdx = (i / 3) * 3 + j / 3;
            if (boxes[boxIdx] & mask) return false;
            boxes[boxIdx] |= mask;
        }
    }
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool IsValidSudoku(char[][] board) {
        int[] rows = new int[9];
        int[] cols = new int[9];
        int[] boxes = new int[9];

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char c = board[i][j];
                if (c == '.') continue;

                int d = c - '1';
                int mask = 1 << d;

                if ((rows[i] & mask) != 0) return false;
                rows[i] |= mask;

                if ((cols[j] & mask) != 0) return false;
                cols[j] |= mask;

                int boxIndex = (i / 3) * 3 + j / 3;
                if ((boxes[boxIndex] & mask) != 0) return false;
                boxes[boxIndex] |= mask;
            }
        }

        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    const rows = Array.from({ length: 9 }, () => new Set());
    const cols = Array.from({ length: 9 }, () => new Set());
    const boxes = Array.from({ length: 9 }, () => new Set());

    for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
            const val = board[i][j];
            if (val === '.') continue;

            // Row check
            if (rows[i].has(val)) return false;
            rows[i].add(val);

            // Column check
            if (cols[j].has(val)) return false;
            cols[j].add(val);

            // Box check
            const boxIndex = Math.floor(i / 3) * 3 + Math.floor(j / 3);
            if (boxes[boxIndex].has(val)) return false;
            boxes[boxIndex].add(val);
        }
    }

    return true;
};
```

## Typescript

```typescript
function isValidSudoku(board: string[][]): boolean {
    const rows: Set<string>[] = Array.from({ length: 9 }, () => new Set());
    const cols: Set<string>[] = Array.from({ length: 9 }, () => new Set());
    const boxes: Set<string>[] = Array.from({ length: 9 }, () => new Set());

    for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
            const val = board[i][j];
            if (val === '.') continue;

            if (rows[i].has(val)) return false;
            rows[i].add(val);

            if (cols[j].has(val)) return false;
            cols[j].add(val);

            const boxIdx = Math.floor(i / 3) * 3 + Math.floor(j / 3);
            if (boxes[boxIdx].has(val)) return false;
            boxes[boxIdx].add(val);
        }
    }

    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param String[][] $board
     * @return Boolean
     */
    function isValidSudoku($board) {
        $rows = [];
        $cols = [];
        $boxes = [];

        for ($i = 0; $i < 9; $i++) {
            $rows[$i] = [];
            $cols[$i] = [];
            $boxes[$i] = [];
        }

        for ($i = 0; $i < 9; $i++) {
            for ($j = 0; $j < 9; $j++) {
                $c = $board[$i][$j];
                if ($c === '.') {
                    continue;
                }
                // Check row
                if (isset($rows[$i][$c])) {
                    return false;
                }
                $rows[$i][$c] = true;

                // Check column
                if (isset($cols[$j][$c])) {
                    return false;
                }
                $cols[$j][$c] = true;

                // Check 3x3 sub-box
                $boxIdx = intdiv($i, 3) * 3 + intdiv($j, 3);
                if (isset($boxes[$boxIdx][$c])) {
                    return false;
                }
                $boxes[$boxIdx][$c] = true;
            }
        }

        return true;
    }
}
```

## Swift

```swift
class Solution {
    func isValidSudoku(_ board: [[Character]]) -> Bool {
        var rows = Array(repeating: Array(repeating: false, count: 9), count: 9)
        var cols = Array(repeating: Array(repeating: false, count: 9), count: 9)
        var boxes = Array(repeating: Array(repeating: false, count: 9), count: 9)
        
        for i in 0..<9 {
            for j in 0..<9 {
                let ch = board[i][j]
                if ch == "." { continue }
                guard let ascii = ch.asciiValue else { return false }
                let num = Int(ascii - Character("1").asciiValue!) // 0-based index
                if rows[i][num] || cols[j][num] || boxes[(i/3)*3 + j/3][num] {
                    return false
                }
                rows[i][num] = true
                cols[j][num] = true
                boxes[(i/3)*3 + j/3][num] = true
            }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isValidSudoku(board: Array<CharArray>): Boolean {
        val rows = Array(9) { BooleanArray(9) }
        val cols = Array(9) { BooleanArray(9) }
        val boxes = Array(9) { BooleanArray(9) }

        for (i in 0 until 9) {
            for (j in 0 until 9) {
                val c = board[i][j]
                if (c == '.') continue
                val num = c - '1' // 0..8
                if (rows[i][num]) return false
                rows[i][num] = true

                if (cols[j][num]) return false
                cols[j][num] = true

                val boxIndex = (i / 3) * 3 + j / 3
                if (boxes[boxIndex][num]) return false
                boxes[boxIndex][num] = true
            }
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool isValidSudoku(List<List<String>> board) {
    List<Set<String>> rows = List.generate(9, (_) => <String>{});
    List<Set<String>> cols = List.generate(9, (_) => <String>{});
    List<Set<String>> boxes = List.generate(9, (_) => <String>{});

    for (int i = 0; i < 9; i++) {
      for (int j = 0; j < 9; j++) {
        String val = board[i][j];
        if (val == '.') continue;

        if (rows[i].contains(val)) return false;
        rows[i].add(val);

        if (cols[j].contains(val)) return false;
        cols[j].add(val);

        int boxIndex = (i ~/ 3) * 3 + (j ~/ 3);
        if (boxes[boxIndex].contains(val)) return false;
        boxes[boxIndex].add(val);
      }
    }

    return true;
  }
}
```

## Golang

```go
func isValidSudoku(board [][]byte) bool {
	var rows, cols, boxes [9]int
	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			c := board[i][j]
			if c == '.' {
				continue
			}
			d := int(c - '1')
			mask := 1 << d
			if rows[i]&mask != 0 || cols[j]&mask != 0 {
				return false
			}
			rows[i] |= mask
			cols[j] |= mask
			boxIdx := (i/3)*3 + j/3
			if boxes[boxIdx]&mask != 0 {
				return false
			}
			boxes[boxIdx] |= mask
		}
	}
	return true
}
```

## Ruby

```ruby
def is_valid_sudoku(board)
  rows = Array.new(9) { {} }
  cols = Array.new(9) { {} }
  boxes = Array.new(9) { {} }

  board.each_with_index do |row, i|
    row.each_with_index do |c, j|
      next if c == '.'
      return false if rows[i][c]
      rows[i][c] = true
      return false if cols[j][c]
      cols[j][c] = true
      box_idx = (i / 3) * 3 + (j / 3)
      return false if boxes[box_idx][c]
      boxes[box_idx][c] = true
    end
  end

  true
end
```

## Scala

```scala
object Solution {
    def isValidSudoku(board: Array[Array[Char]]): Boolean = {
        val rows = Array.fill(9)(scala.collection.mutable.Set[Char]())
        val cols = Array.fill(9)(scala.collection.mutable.Set[Char]())
        val boxes = Array.fill(9)(scala.collection.mutable.Set[Char]())

        for (i <- 0 until 9; j <- 0 until 9) {
            val c = board(i)(j)
            if (c != '.') {
                if (!rows(i).add(c)) return false
                if (!cols(j).add(c)) return false
                val boxIdx = (i / 3) * 3 + (j / 3)
                if (!boxes(boxIdx).add(c)) return false
            }
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        let mut rows = [[false; 9]; 9];
        let mut cols = [[false; 9]; 9];
        let mut boxes = [[false; 9]; 9];

        for i in 0..9 {
            for j in 0..9 {
                let c = board[i][j];
                if c == '.' {
                    continue;
                }
                let idx = (c as u8 - b'1') as usize;
                let box_idx = (i / 3) * 3 + (j / 3);
                if rows[i][idx] || cols[j][idx] || boxes[box_idx][idx] {
                    return false;
                }
                rows[i][idx] = true;
                cols[j][idx] = true;
                boxes[box_idx][idx] = true;
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (is-valid-sudoku board)
  (-> (listof (listof char?)) boolean?)
  (let* ([rows  (make-vector 9 (make-hash))]
         [cols  (make-vector 9 (make-hash))]
         [boxes (make-vector 9 (make-hash))])
    (for/and ([i (in-range 9)])
      (for/and ([j (in-range 9)])
        (let* ([c (list-ref (list-ref board i) j)])
          (if (char=? c #\.)
              #t
              (let* ([key c]
                     [box-index (+ (* (quotient i 3) 3)
                                   (quotient j 3))])
                (cond
                  [(hash-has-key? (vector-ref rows i) key) #f]
                  [(hash-has-key? (vector-ref cols j) key) #f]
                  [(hash-has-key? (vector-ref boxes box-index) key) #f]
                  [else
                   (hash-set! (vector-ref rows i)  key #t)
                   (hash-set! (vector-ref cols j)  key #t)
                   (hash-set! (vector-ref boxes box-index) key #t)
                   #t])))))))))
```

## Erlang

```erlang
-spec is_valid_sudoku(Board :: [[char()]]) -> boolean().
is_valid_sudoku(Board) ->
    loop_rows(Board, 0, #{}).

%% Loop over rows
loop_rows(_, 9, _) ->
    true;
loop_rows(Board, RowIdx, Seen) ->
    Row = lists:nth(RowIdx + 1, Board),
    case loop_cols(Row, RowIdx, 0, Seen) of
        {false, _} -> false;
        {true, NewSeen} -> loop_rows(Board, RowIdx + 1, NewSeen)
    end.

%% Loop over columns in a row
loop_cols(_, _, 9, Seen) ->
    {true, Seen};
loop_cols(Row, RowIdx, ColIdx, Seen) ->
    Cell = lists:nth(ColIdx + 1, Row),
    if
        Cell == $. ->                                   % empty cell
            loop_cols(Row, RowIdx, ColIdx + 1, Seen);
        true ->
            Digit = Cell,
            BoxIdx = (RowIdx div 3) * 3 + (ColIdx div 3),
            KeyR = {row, RowIdx, Digit},
            KeyC = {col, ColIdx, Digit},
            KeyB = {box, BoxIdx, Digit},
            case maps:is_key(KeyR, Seen) orelse
                 maps:is_key(KeyC, Seen) orelse
                 maps:is_key(KeyB, Seen) of
                true ->
                    {false, Seen};
                false ->
                    NewSeen1 = maps:put(KeyR, true, Seen),
                    NewSeen2 = maps:put(KeyC, true, NewSeen1),
                    NewSeen3 = maps:put(KeyB, true, NewSeen2),
                    loop_cols(Row, RowIdx, ColIdx + 1, NewSeen3)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_valid_sudoku(board :: [[char]]) :: boolean
  def is_valid_sudoku(board) do
    rows_ok =
      Enum.all?(0..8, fn i ->
        row = Enum.at(board, i)
        digits = Enum.filter(row, &(&1 != "."))
        length(digits) == MapSet.size(MapSet.new(digits))
      end)

    cols_ok =
      Enum.all?(0..8, fn j ->
        col =
          for i <- 0..8 do
            board |> Enum.at(i) |> Enum.at(j)
          end

        digits = Enum.filter(col, &(&1 != "."))
        length(digits) == MapSet.size(MapSet.new(digits))
      end)

    boxes_ok =
      Enum.all?(0..2, fn bi ->
        Enum.all?(0..2, fn bj ->
          start_i = bi * 3
          start_j = bj * 3

          digits =
            for di <- 0..2,
                dj <- 0..2 do
              board |> Enum.at(start_i + di) |> Enum.at(start_j + dj)
            end
            |> Enum.filter(&(&1 != "."))

          length(digits) == MapSet.size(MapSet.new(digits))
        end)
      end)

    rows_ok and cols_ok and boxes_ok
  end
end
```
