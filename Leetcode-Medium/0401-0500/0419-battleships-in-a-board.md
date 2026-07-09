# 0419. Battleships in a Board

## Cpp

```cpp
class Solution {
public:
    int countBattleships(vector<vector<char>>& board) {
        int m = board.size();
        if (m == 0) return 0;
        int n = board[0].size();
        int cnt = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (board[i][j] != 'X') continue;
                if (i > 0 && board[i-1][j] == 'X') continue;
                if (j > 0 && board[i][j-1] == 'X') continue;
                ++cnt;
            }
        }
        return cnt;
    }
};
```

## Java

```java
class Solution {
    public int countBattleships(char[][] board) {
        int m = board.length;
        if (m == 0) return 0;
        int n = board[0].length;
        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] != 'X') continue;
                if (i > 0 && board[i - 1][j] == 'X') continue;
                if (j > 0 && board[i][j - 1] == 'X') continue;
                count++;
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board:
            return 0
        m, n = len(board), len(board[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] != 'X':
                    continue
                if i > 0 and board[i - 1][j] == 'X':
                    continue
                if j > 0 and board[i][j - 1] == 'X':
                    continue
                count += 1
        return count
```

## Python3

```python
class Solution:
    def countBattleships(self, board):
        if not board or not board[0]:
            return 0
        rows, cols = len(board), len(board[0])
        count = 0
        for i in range(rows):
            for j in range(cols):
                if board[i][j] != 'X':
                    continue
                if i > 0 and board[i-1][j] == 'X':
                    continue
                if j > 0 and board[i][j-1] == 'X':
                    continue
                count += 1
        return count
```

## C

```c
int countBattleships(char** board, int boardSize, int* boardColSize) {
    int count = 0;
    for (int i = 0; i < boardSize; ++i) {
        int n = boardColSize[i];
        for (int j = 0; j < n; ++j) {
            if (board[i][j] != 'X') continue;
            if (i > 0 && board[i - 1][j] == 'X') continue;
            if (j > 0 && board[i][j - 1] == 'X') continue;
            ++count;
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int CountBattleships(char[][] board) {
        if (board == null || board.Length == 0) return 0;
        int rows = board.Length;
        int cols = board[0].Length;
        int count = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (board[i][j] != 'X') continue;
                if (i > 0 && board[i - 1][j] == 'X') continue;
                if (j > 0 && board[i][j - 1] == 'X') continue;
                count++;
            }
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {character[][]} board
 * @return {number}
 */
var countBattleships = function(board) {
    if (!board || board.length === 0) return 0;
    let m = board.length, n = board[0].length;
    let count = 0;
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if (board[i][j] !== 'X') continue;
            if (i > 0 && board[i - 1][j] === 'X') continue;
            if (j > 0 && board[i][j - 1] === 'X') continue;
            count++;
        }
    }
    return count;
};
```

## Typescript

```typescript
function countBattleships(board: string[][]): number {
    const m = board.length;
    if (m === 0) return 0;
    const n = board[0].length;
    let count = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (board[i][j] !== 'X') continue;
            if (i > 0 && board[i - 1][j] === 'X') continue;
            if (j > 0 && board[i][j - 1] === 'X') continue;
            count++;
        }
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param String[][] $board
     * @return Integer
     */
    function countBattleships($board) {
        $m = count($board);
        if ($m === 0) {
            return 0;
        }
        $n = count($board[0]);
        $count = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($board[$i][$j] !== 'X') {
                    continue;
                }
                if ($i > 0 && $board[$i - 1][$j] === 'X') {
                    continue;
                }
                if ($j > 0 && $board[$i][$j - 1] === 'X') {
                    continue;
                }
                $count++;
            }
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func countBattleships(_ board: [[Character]]) -> Int {
        var count = 0
        let rows = board.count
        if rows == 0 { return 0 }
        let cols = board[0].count
        
        for i in 0..<rows {
            for j in 0..<cols {
                if board[i][j] != "X" { continue }
                if i > 0 && board[i - 1][j] == "X" { continue }
                if j > 0 && board[i][j - 1] == "X" { continue }
                count += 1
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countBattleships(board: Array<CharArray>): Int {
        var count = 0
        val m = board.size
        if (m == 0) return 0
        val n = board[0].size
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (board[i][j] != 'X') continue
                if (i > 0 && board[i - 1][j] == 'X') continue
                if (j > 0 && board[i][j - 1] == 'X') continue
                count++
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int countBattleships(List<List<String>> board) {
    int rows = board.length;
    if (rows == 0) return 0;
    int cols = board[0].length;
    int count = 0;

    for (int i = 0; i < rows; ++i) {
      for (int j = 0; j < cols; ++j) {
        if (board[i][j] != 'X') continue;
        if (i > 0 && board[i - 1][j] == 'X') continue;
        if (j > 0 && board[i][j - 1] == 'X') continue;
        count++;
      }
    }

    return count;
  }
}
```

## Golang

```go
func countBattleships(board [][]byte) int {
	if len(board) == 0 || len(board[0]) == 0 {
		return 0
	}
	m, n := len(board), len(board[0])
	count := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if board[i][j] != 'X' {
				continue
			}
			if i > 0 && board[i-1][j] == 'X' {
				continue
			}
			if j > 0 && board[i][j-1] == 'X' {
				continue
			}
			count++
		}
	}
	return count
}
```

## Ruby

```ruby
def count_battleships(board)
  return 0 if board.nil? || board.empty?
  m = board.size
  n = board[0].size
  count = 0
  (0...m).each do |i|
    (0...n).each do |j|
      next unless board[i][j] == 'X'
      if (i == 0 || board[i - 1][j] != 'X') && (j == 0 || board[i][j - 1] != 'X')
        count += 1
      end
    end
  end
  count
end
```

## Scala

```scala
object Solution {
    def countBattleships(board: Array[Array[Char]]): Int = {
        var count = 0
        val m = board.length
        if (m == 0) return 0
        val n = board(0).length
        for (i <- 0 until m) {
            for (j <- 0 until n) {
                if (board(i)(j) == 'X') {
                    if (i > 0 && board(i - 1)(j) == 'X') {
                        // part of vertical ship, skip
                    } else if (j > 0 && board(i)(j - 1) == 'X') {
                        // part of horizontal ship, skip
                    } else {
                        count += 1
                    }
                }
            }
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_battleships(board: Vec<Vec<char>>) -> i32 {
        let m = board.len();
        if m == 0 {
            return 0;
        }
        let n = board[0].len();
        let mut cnt = 0;
        for i in 0..m {
            for j in 0..n {
                if board[i][j] != 'X' {
                    continue;
                }
                if i > 0 && board[i - 1][j] == 'X' {
                    continue;
                }
                if j > 0 && board[i][j - 1] == 'X' {
                    continue;
                }
                cnt += 1;
            }
        }
        cnt as i32
    }
}
```

## Racket

```racket
(define/contract (count-battleships board)
  (-> (listof (listof char?)) exact-integer?)
  (let* ((rows (length board))
         (cols (if (zero? rows) 0 (length (first board))))
         (vboard (list->vector (map list->vector board)))
         (cnt 0))
    (for ([i (in-range rows)])
      (for ([j (in-range cols)])
        (when (char=? (vector-ref (vector-ref vboard i) j) #\X)
          (let ((top   (if (= i 0) #\. (vector-ref (vector-ref vboard (- i 1)) j)))
                (left  (if (= j 0) #\. (vector-ref (vector-ref vboard i) (- j 1)))))
            (when (and (char=? top #\.) (char=? left #\.))
              (set! cnt (+ cnt 1)))))))
    cnt))
```

## Erlang

```erlang
-module(solution).
-export([count_battleships/1]).

-spec count_battleships(Board :: [[char()]]) -> integer().
count_battleships(Board) ->
    count_rows(Board, []).

count_rows([], _PrevRow) -> 0;
count_rows([CurrRow|RestRows], PrevRow) ->
    RowCount = process_row(CurrRow, PrevRow),
    RowCount + count_rows(RestRows, CurrRow).

process_row(Row, PrevRow) ->
    process_columns(Row, PrevRow, $., 0).

process_columns([], _PrevRow, _LeftChar, Acc) -> Acc;
process_columns([C|Cs], PrevRow, LeftChar, Acc) ->
    AboveChar = case PrevRow of
        [] -> $.;
        [P|_] -> P
    end,
    NewAcc = if C == $X andalso AboveChar == $. andalso LeftChar == $. ->
                 Acc + 1;
             true -> Acc
            end,
    NextPrevRow = case PrevRow of
        [] -> [];
        [_|Rest] -> Rest
    end,
    process_columns(Cs, NextPrevRow, C, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_battleships(board :: [[char]]) :: integer
  def count_battleships(board) do
    rows = length(board)
    cols = if rows == 0, do: 0, else: length(hd(board))

    Enum.reduce(0..rows - 1, 0, fn i, acc ->
      row = Enum.at(board, i)

      Enum.reduce(0..cols - 1, acc, fn j, cnt ->
        case Enum.at(row, j) do
          "X" ->
            up =
              if i > 0,
                do: board |> Enum.at(i - 1) |> Enum.at(j),
                else: "."

            left = if j > 0, do: Enum.at(row, j - 1), else: "."

            if up == "X" or left == "X", do: cnt, else: cnt + 1

          _ ->
            cnt
        end
      end)
    end)
  end
end
```
