# 0794. Valid Tic-Tac-Toe State

## Cpp

```cpp
class Solution {
public:
    bool validTicTacToe(vector<string>& board) {
        int cntX = 0, cntO = 0;
        for (auto& row : board) {
            for (char c : row) {
                if (c == 'X') ++cntX;
                else if (c == 'O') ++cntO;
            }
        }
        // X goes first
        if (!(cntX == cntO || cntX == cntO + 1)) return false;
        
        auto win = [&](char p) {
            // rows and columns
            for (int i = 0; i < 3; ++i) {
                if (board[i][0] == p && board[i][1] == p && board[i][2] == p) return true;
                if (board[0][i] == p && board[1][i] == p && board[2][i] == p) return true;
            }
            // diagonals
            if (board[0][0] == p && board[1][1] == p && board[2][2] == p) return true;
            if (board[0][2] == p && board[1][1] == p && board[2][0] == p) return true;
            return false;
        };
        
        bool xWin = win('X');
        bool oWin = win('O');
        
        if (xWin && oWin) return false;
        if (xWin && cntX != cntO + 1) return false;
        if (oWin && cntX != cntO) return false;
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean validTicTacToe(String[] board) {
        int xCount = 0, oCount = 0;
        for (String row : board) {
            for (char c : row.toCharArray()) {
                if (c == 'X') xCount++;
                else if (c == 'O') oCount++;
            }
        }
        // X goes first
        if (oCount > xCount || xCount - oCount > 1) return false;
        
        boolean xWin = win(board, 'X');
        boolean oWin = win(board, 'O');
        
        // both cannot win
        if (xWin && oWin) return false;
        // if X wins, must have one more X than O
        if (xWin && xCount != oCount + 1) return false;
        // if O wins, counts must be equal
        if (oWin && xCount != oCount) return false;
        
        return true;
    }
    
    private boolean win(String[] board, char player) {
        // rows
        for (int i = 0; i < 3; i++) {
            if (board[i].charAt(0) == player &&
                board[i].charAt(1) == player &&
                board[i].charAt(2) == player) return true;
        }
        // columns
        for (int j = 0; j < 3; j++) {
            if (board[0].charAt(j) == player &&
                board[1].charAt(j) == player &&
                board[2].charAt(j) == player) return true;
        }
        // diagonals
        if (board[0].charAt(0) == player &&
            board[1].charAt(1) == player &&
            board[2].charAt(2) == player) return true;
        if (board[0].charAt(2) == player &&
            board[1].charAt(1) == player &&
            board[2].charAt(0) == player) return true;
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        # Count X and O
        cntX = sum(row.count('X') for row in board)
        cntO = sum(row.count('O') for row in board)

        # Basic turn count validation
        if not (cntX == cntO or cntX == cntO + 1):
            return False

        def win(player):
            lines = []
            # rows
            lines.extend([board[i] for i in range(3)])
            # cols
            lines.extend([''.join(board[r][c] for r in range(3)) for c in range(3)])
            # diagonals
            lines.append(''.join(board[i][i] for i in range(3)))
            lines.append(''.join(board[i][2 - i] for i in range(3)))
            return any(line == player * 3 for line in lines)

        xWin = win('X')
        oWin = win('O')

        # Both cannot win
        if xWin and oWin:
            return False
        # If X wins, must have one more move than O
        if xWin and cntX != cntO + 1:
            return False
        # If O wins, counts must be equal
        if oWin and cntX != cntO:
            return False

        return True
```

## Python3

```python
from typing import List

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def win(p: str) -> bool:
            lines = []
            # rows
            for i in range(3):
                lines.append([board[i][j] for j in range(3)])
            # cols
            for j in range(3):
                lines.append([board[i][j] for i in range(3)])
            # diagonals
            lines.append([board[i][i] for i in range(3)])
            lines.append([board[i][2 - i] for i in range(3)])
            return any(all(cell == p for cell in line) for line in lines)

        cntX = sum(row.count('X') for row in board)
        cntO = sum(row.count('O') for row in board)

        # basic count rule
        if not (cntX == cntO or cntX == cntO + 1):
            return False

        x_win = win('X')
        o_win = win('O')

        # both cannot win
        if x_win and o_win:
            return False
        # if X wins, must have one more X than O
        if x_win and cntX != cntO + 1:
            return False
        # if O wins, counts must be equal
        if o_win and cntX != cntO:
            return False

        return True
```

## C

```c
#include <stdbool.h>

static bool isWin(char **board, char player) {
    // rows
    for (int i = 0; i < 3; ++i) {
        if (board[i][0] == player && board[i][1] == player && board[i][2] == player)
            return true;
    }
    // columns
    for (int j = 0; j < 3; ++j) {
        if (board[0][j] == player && board[1][j] == player && board[2][j] == player)
            return true;
    }
    // diagonals
    if (board[0][0] == player && board[1][1] == player && board[2][2] == player)
        return true;
    if (board[0][2] == player && board[1][1] == player && board[2][0] == player)
        return true;
    return false;
}

bool validTicTacToe(char** board, int boardSize) {
    int cntX = 0, cntO = 0;
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            if (board[i][j] == 'X')
                ++cntX;
            else if (board[i][j] == 'O')
                ++cntO;
        }
    }

    // X starts first, so count condition must hold
    if (!(cntX == cntO || cntX == cntO + 1))
        return false;

    bool xWin = isWin(board, 'X');
    bool oWin = isWin(board, 'O');

    // both cannot win simultaneously
    if (xWin && oWin)
        return false;
    // if X wins, it must have one more move than O
    if (xWin && cntX != cntO + 1)
        return false;
    // if O wins, counts must be equal
    if (oWin && cntX != cntO)
        return false;

    return true;
}
```

## Csharp

```csharp
public class Solution
{
    public bool ValidTicTacToe(string[] board)
    {
        int xCount = 0, oCount = 0;
        foreach (var row in board)
        {
            foreach (char c in row)
            {
                if (c == 'X') xCount++;
                else if (c == 'O') oCount++;
            }
        }

        // X always goes first
        if (oCount > xCount || xCount - oCount > 1) return false;

        bool xWin = IsWin(board, 'X');
        bool oWin = IsWin(board, 'O');

        // both cannot win simultaneously
        if (xWin && oWin) return false;

        // if X wins, it must have one more move than O
        if (xWin && xCount != oCount + 1) return false;

        // if O wins, counts must be equal
        if (oWin && xCount != oCount) return false;

        return true;
    }

    private bool IsWin(string[] board, char player)
    {
        // rows
        for (int i = 0; i < 3; i++)
            if (board[i][0] == player && board[i][1] == player && board[i][2] == player)
                return true;

        // columns
        for (int j = 0; j < 3; j++)
            if (board[0][j] == player && board[1][j] == player && board[2][j] == player)
                return true;

        // diagonals
        if (board[0][0] == player && board[1][1] == player && board[2][2] == player)
            return true;
        if (board[0][2] == player && board[1][1] == player && board[2][0] == player)
            return true;

        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} board
 * @return {boolean}
 */
var validTicTacToe = function(board) {
    let xCount = 0, oCount = 0;
    for (let row of board) {
        for (let ch of row) {
            if (ch === 'X') xCount++;
            else if (ch === 'O') oCount++;
        }
    }
    // X always goes first
    if (!(xCount === oCount || xCount === oCount + 1)) return false;
    
    const win = (player) => {
        const lines = [
            [[0,0],[0,1],[0,2]],
            [[1,0],[1,1],[1,2]],
            [[2,0],[2,1],[2,2]],
            [[0,0],[1,0],[2,0]],
            [[0,1],[1,1],[2,1]],
            [[0,2],[1,2],[2,2]],
            [[0,0],[1,1],[2,2]],
            [[0,2],[1,1],[2,0]]
        ];
        for (let line of lines) {
            if (line.every(([r,c]) => board[r][c] === player)) return true;
        }
        return false;
    };
    
    const xWin = win('X');
    const oWin = win('O');
    
    // both cannot win
    if (xWin && oWin) return false;
    // if X wins, must have one more move than O
    if (xWin && xCount !== oCount + 1) return false;
    // if O wins, counts must be equal
    if (oWin && xCount !== oCount) return false;
    
    return true;
};
```

## Typescript

```typescript
function validTicTacToe(board: string[]): boolean {
    const rows = board;
    let xCount = 0, oCount = 0;

    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            const c = rows[i][j];
            if (c === 'X') xCount++;
            else if (c === 'O') oCount++;
        }
    }

    // X always goes first
    if (!(xCount === oCount || xCount === oCount + 1)) return false;

    const winLines = [
        // rows
        [[0,0],[0,1],[0,2]],
        [[1,0],[1,1],[1,2]],
        [[2,0],[2,1],[2,2]],
        // cols
        [[0,0],[1,0],[2,0]],
        [[0,1],[1,1],[2,1]],
        [[0,2],[1,2],[2,2]],
        // diagonals
        [[0,0],[1,1],[2,2]],
        [[0,2],[1,1],[2,0]]
    ];

    const checkWin = (player: string): boolean => {
        for (const line of winLines) {
            if (line.every(([r,c]) => rows[r][c] === player)) return true;
        }
        return false;
    };

    const xWin = checkWin('X');
    const oWin = checkWin('O');

    // both cannot win
    if (xWin && oWin) return false;

    // if X wins, must have one more X than O
    if (xWin && xCount !== oCount + 1) return false;

    // if O wins, counts must be equal
    if (oWin && xCount !== oCount) return false;

    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $board
     * @return Boolean
     */
    function validTicTacToe($board) {
        $xCount = 0;
        $oCount = 0;
        foreach ($board as $row) {
            for ($i = 0; $i < 3; $i++) {
                if ($row[$i] === 'X') {
                    $xCount++;
                } elseif ($row[$i] === 'O') {
                    $oCount++;
                }
            }
        }

        // X goes first and players alternate
        if (!($xCount == $oCount || $xCount == $oCount + 1)) {
            return false;
        }

        $winX = $this->isWin($board, 'X');
        $winO = $this->isWin($board, 'O');

        // both cannot win
        if ($winX && $winO) {
            return false;
        }
        // if X wins, it must have one more move than O
        if ($winX && $xCount != $oCount + 1) {
            return false;
        }
        // if O wins, moves must be equal
        if ($winO && $xCount != $oCount) {
            return false;
        }

        return true;
    }

    private function isWin($board, $player) {
        // rows
        for ($i = 0; $i < 3; $i++) {
            if ($board[$i][0] === $player && $board[$i][1] === $player && $board[$i][2] === $player) {
                return true;
            }
        }
        // columns
        for ($j = 0; $j < 3; $j++) {
            if ($board[0][$j] === $player && $board[1][$j] === $player && $board[2][$j] === $player) {
                return true;
            }
        }
        // diagonals
        if ($board[0][0] === $player && $board[1][1] === $player && $board[2][2] === $player) {
            return true;
        }
        if ($board[0][2] === $player && $board[1][1] === $player && $board[2][0] === $player) {
            return true;
        }

        return false;
    }
}
```

## Swift

```swift
class Solution {
    func validTicTacToe(_ board: [String]) -> Bool {
        let b = board.map { Array($0) }
        var xCount = 0
        var oCount = 0
        for i in 0..<3 {
            for j in 0..<3 {
                if b[i][j] == "X" {
                    xCount += 1
                } else if b[i][j] == "O" {
                    oCount += 1
                }
            }
        }
        // X goes first
        if !(xCount == oCount || xCount == oCount + 1) {
            return false
        }
        let xWin = win(b, "X")
        let oWin = win(b, "O")
        // both cannot win
        if xWin && oWin {
            return false
        }
        // if X wins, it must have one more move than O
        if xWin && xCount != oCount + 1 {
            return false
        }
        // if O wins, counts must be equal
        if oWin && xCount != oCount {
            return false
        }
        return true
    }
    
    private func win(_ board: [[Character]], _ player: Character) -> Bool {
        // rows and columns
        for i in 0..<3 {
            if board[i][0] == player && board[i][1] == player && board[i][2] == player {
                return true
            }
            if board[0][i] == player && board[1][i] == player && board[2][i] == player {
                return true
            }
        }
        // diagonals
        if board[0][0] == player && board[1][1] == player && board[2][2] == player {
            return true
        }
        if board[0][2] == player && board[1][1] == player && board[2][0] == player {
            return true
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun validTicTacToe(board: Array<String>): Boolean {
        var xCount = 0
        var oCount = 0
        for (row in board) {
            for (c in row) {
                when (c) {
                    'X' -> xCount++
                    'O' -> oCount++
                }
            }
        }
        if (!(xCount == oCount || xCount == oCount + 1)) return false

        fun win(player: Char): Boolean {
            for (i in 0..2) {
                if (board[i][0] == player && board[i][1] == player && board[i][2] == player) return true
            }
            for (j in 0..2) {
                if (board[0][j] == player && board[1][j] == player && board[2][j] == player) return true
            }
            if (board[0][0] == player && board[1][1] == player && board[2][2] == player) return true
            if (board[0][2] == player && board[1][1] == player && board[2][0] == player) return true
            return false
        }

        val xWin = win('X')
        val oWin = win('O')

        if (xWin && oWin) return false
        if (xWin && xCount != oCount + 1) return false
        if (oWin && xCount != oCount) return false

        return true
    }
}
```

## Dart

```dart
class Solution {
  bool validTicTacToe(List<String> board) {
    int countX = 0, countO = 0;
    for (var row in board) {
      for (int i = 0; i < 3; i++) {
        if (row[i] == 'X') countX++;
        else if (row[i] == 'O') countO++;
      }
    }

    // X always goes first
    if (!(countX == countO || countX == countO + 1)) return false;

    bool xWin = _wins(board, 'X');
    bool oWin = _wins(board, 'O');

    // both cannot win
    if (xWin && oWin) return false;
    // if X wins, must have one more move than O
    if (xWin && countX != countO + 1) return false;
    // if O wins, counts must be equal
    if (oWin && countX != countO) return false;

    return true;
  }

  bool _wins(List<String> board, String player) {
    // rows
    for (int i = 0; i < 3; i++) {
      if (board[i][0] == player &&
          board[i][1] == player &&
          board[i][2] == player) return true;
    }
    // columns
    for (int j = 0; j < 3; j++) {
      if (board[0][j] == player &&
          board[1][j] == player &&
          board[2][j] == player) return true;
    }
    // diagonals
    if (board[0][0] == player && board[1][1] == player && board[2][2] == player)
      return true;
    if (board[0][2] == player && board[1][1] == player && board[2][0] == player)
      return true;

    return false;
  }
}
```

## Golang

```go
func validTicTacToe(board []string) bool {
	cntX, cntO := 0, 0
	for _, row := range board {
		for i := 0; i < 3; i++ {
			switch row[i] {
			case 'X':
				cntX++
			case 'O':
				cntO++
			}
		}
	}
	if !(cntX == cntO || cntX == cntO+1) {
		return false
	}
	xWin := win(board, 'X')
	oWin := win(board, 'O')
	if xWin && oWin {
		return false
	}
	if xWin && cntX != cntO+1 {
		return false
	}
	if oWin && cntX != cntO {
		return false
	}
	return true
}

func win(b []string, p byte) bool {
	for i := 0; i < 3; i++ {
		if b[i][0] == p && b[i][1] == p && b[i][2] == p {
			return true
		}
	}
	for j := 0; j < 3; j++ {
		if b[0][j] == p && b[1][j] == p && b[2][j] == p {
			return true
		}
	}
	if b[0][0] == p && b[1][1] == p && b[2][2] == p {
		return true
	}
	if b[0][2] == p && b[1][1] == p && b[2][0] == p {
		return true
	}
	return false
}
```

## Ruby

```ruby
def player_win?(board, p)
  3.times do |i|
    return true if board[i][0] == p && board[i][1] == p && board[i][2] == p
  end
  3.times do |j|
    return true if board[0][j] == p && board[1][j] == p && board[2][j] == p
  end
  return true if board[0][0] == p && board[1][1] == p && board[2][2] == p
  return true if board[0][2] == p && board[1][1] == p && board[2][0] == p
  false
end

def valid_tic_tac_toe(board)
  x = board.join.count('X')
  o = board.join.count('O')
  return false unless (x == o) || (x == o + 1)

  x_win = player_win?(board, 'X')
  o_win = player_win?(board, 'O')

  return false if x_win && o_win
  if x_win
    return x == o + 1
  elsif o_win
    return x == o
  else
    true
  end
end
```

## Scala

```scala
object Solution {
  def validTicTacToe(board: Array[String]): Boolean = {
    val grid: Array[Array[Char]] = board.map(_.toCharArray)

    var xCount = 0
    var oCount = 0
    for (i <- 0 until 3; j <- 0 until 3) {
      grid(i)(j) match {
        case 'X' => xCount += 1
        case 'O' => oCount += 1
        case _   => ()
      }
    }

    // basic count validation
    if (oCount > xCount || xCount - oCount > 1) return false

    def win(player: Char): Boolean = {
      // rows and columns
      for (i <- 0 until 3) {
        if (grid(i)(0) == player && grid(i)(1) == player && grid(i)(2) == player) return true
        if (grid(0)(i) == player && grid(1)(i) == player && grid(2)(i) == player) return true
      }
      // diagonals
      if (grid(0)(0) == player && grid(1)(1) == player && grid(2)(2) == player) return true
      if (grid(0)(2) == player && grid(1)(1) == player && grid(2)(0) == player) return true
      false
    }

    val xWin = win('X')
    val oWin = win('O')

    // both cannot win simultaneously
    if (xWin && oWin) return false

    // if X wins, it must have one more move than O
    if (xWin && xCount != oCount + 1) return false

    // if O wins, counts must be equal
    if (oWin && xCount != oCount) return false

    true
  }
}
```

## Rust

```rust
impl Solution {
    pub fn valid_tic_tac_toe(board: Vec<String>) -> bool {
        // Convert board to 2D char array and count X/O
        let mut b = vec![vec![' '; 3]; 3];
        let (mut x_cnt, mut o_cnt) = (0, 0);
        for i in 0..3 {
            let chars: Vec<char> = board[i].chars().collect();
            for j in 0..3 {
                b[i][j] = chars[j];
                match chars[j] {
                    'X' => x_cnt += 1,
                    'O' => o_cnt += 1,
                    _ => {}
                }
            }
        }

        // Basic turn count validation
        if !(x_cnt == o_cnt || x_cnt == o_cnt + 1) {
            return false;
        }

        let x_win = Self::win(&b, 'X');
        let o_win = Self::win(&b, 'O');

        // Both cannot win simultaneously
        if x_win && o_win {
            return false;
        }
        // If X wins, it must have one more move than O
        if x_win && x_cnt != o_cnt + 1 {
            return false;
        }
        // If O wins, moves must be equal
        if o_win && x_cnt != o_cnt {
            return false;
        }

        true
    }

    fn win(board: &Vec<Vec<char>>, player: char) -> bool {
        // rows
        for i in 0..3 {
            if board[i][0] == player && board[i][1] == player && board[i][2] == player {
                return true;
            }
        }
        // columns
        for j in 0..3 {
            if board[0][j] == player && board[1][j] == player && board[2][j] == player {
                return true;
            }
        }
        // diagonals
        if board[0][0] == player && board[1][1] == player && board[2][2] == player {
            return true;
        }
        if board[0][2] == player && board[1][1] == player && board[2][0] == player {
            return true;
        }
        false
    }
}
```

## Racket

```racket
(define/contract (valid-tic-tac-toe board)
  (-> (listof string?) boolean?)
  (let* ((rows (map string->list board))
         (count-player
          (lambda (p)
            (apply + (map (lambda (row)
                            (length (filter (lambda (c) (char=? c p)) row)))
                          rows))))
         (cntX (count-player #\X))
         (cntO (count-player #\O)))
    (cond
      [(or (< cntX cntO) (> (- cntX cntO) 1)) #f]
      [else
       (letrec ((cell (lambda (i j) (list-ref (list-ref rows i) j)))
                (win? (lambda (p)
                        (or
                         (ormap (lambda (i)
                                  (and (char=? (cell i 0) p)
                                       (char=? (cell i 1) p)
                                       (char=? (cell i 2) p)))
                                '(0 1 2))
                         (ormap (lambda (j)
                                  (and (char=? (cell 0 j) p)
                                       (char=? (cell 1 j) p)
                                       (char=? (cell 2 j) p)))
                                '(0 1 2))
                         (and (char=? (cell 0 0) p)
                              (char=? (cell 1 1) p)
                              (char=? (cell 2 2) p))
                         (and (char=? (cell 0 2) p)
                              (char=? (cell 1 1) p)
                              (char=? (cell 2 0) p))))))
         (let ((xwin (win? #\X))
               (owin (win? #\O)))
           (cond
             [(and xwin owin) #f]
             [xwin (if (= cntX (+ cntO 1)) #t #f)]
             [owin (if (= cntX cntO) #t #f)]
             [else #t])))])))
```

## Erlang

```erlang
-spec valid_tic_tac_toe(Board :: [unicode:unicode_binary()]) -> boolean().
valid_tic_tac_toe(Board) ->
    Rows = [binary_to_list(Row) || Row <- Board],
    {CountX, CountO} = count_marks(Rows, 0, 0),
    case (CountX == CountO) orelse (CountX == CountO + 1) of
        false -> false;
        true ->
            XWin = player_wins($X, Rows),
            OWin = player_wins($O, Rows),
            cond_check(CountX, CountO, XWin, OWin)
    end.

count_marks([], CX, CO) -> {CX, CO};
count_marks([Row|Rest], CX, CO) ->
    {NewCX, NewCO} = count_row(Row, CX, CO),
    count_marks(Rest, NewCX, NewCO).

count_row([], CX, CO) -> {CX, CO};
count_row([C|Rest], CX, CO) ->
    case C of
        $X -> count_row(Rest, CX+1, CO);
        $O -> count_row(Rest, CX, CO+1);
        _  -> count_row(Rest, CX, CO)
    end.

player_wins(Player, Rows) ->
    [Row0, Row1, Row2] = Rows,
    [R0C0,R0C1,R0C2] = Row0,
    [R1C0,R1C1,R1C2] = Row1,
    [R2C0,R2C1,R2C2] = Row2,
    Lines = [
        [R0C0,R0C1,R0C2],
        [R1C0,R1C1,R1C2],
        [R2C0,R2C1,R2C2],
        [R0C0,R1C0,R2C0],
        [R0C1,R1C1,R2C1],
        [R0C2,R1C2,R2C2],
        [R0C0,R1C1,R2C2],
        [R0C2,R1C1,R2C0]
    ],
    lists:any(fun(Line) -> all_equal(Player, Line) end, Lines).

all_equal(P, Line) ->
    lists:foldl(fun(C, Acc) -> Acc andalso C == P end, true, Line).

cond_check(CountX, CountO, XWin, OWin) ->
    case {XWin, OWin} of
        {true, true} -> false;
        {true, false} -> CountX =:= CountO + 1;
        {false, true} -> CountX =:= CountO;
        {false, false} -> true
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec valid_tic_tac_toe(board :: [String.t()]) :: boolean()
  def valid_tic_tac_toe(board) do
    count_x = Enum.reduce(board, 0, fn row, acc ->
      acc + String.graphemes(row) |> Enum.count(&(&1 == "X"))
    end)

    count_o = Enum.reduce(board, 0, fn row, acc ->
      acc + String.graphemes(row) |> Enum.count(&(&1 == "O"))
    end)

    # basic turn count validation
    if not (count_x == count_o or count_x == count_o + 1) do
      false
    else
      x_win = win?(board, "X")
      o_win = win?(board, "O")

      cond do
        x_win and o_win -> false
        x_win -> count_x == count_o + 1
        o_win -> count_x == count_o
        true -> true
      end
    end
  end

  defp win?(board, player) do
    lines = [
      [{0, 0}, {0, 1}, {0, 2}],
      [{1, 0}, {1, 1}, {1, 2}],
      [{2, 0}, {2, 1}, {2, 2}],
      [{0, 0}, {1, 0}, {2, 0}],
      [{0, 1}, {1, 1}, {2, 1}],
      [{0, 2}, {1, 2}, {2, 2}],
      [{0, 0}, {1, 1}, {2, 2}],
      [{0, 2}, {1, 1}, {2, 0}]
    ]

    Enum.any?(lines, fn line ->
      Enum.all?(line, fn {i, j} ->
        String.at(Enum.at(board, i), j) == player
      end)
    end)
  end
end
```
