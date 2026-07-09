# 0079. Word Search

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int m = board.size();
        int n = board[0].size();

        // Frequency pruning
        vector<int> cntBoard(128, 0), cntWord(128, 0);
        for (auto &row : board)
            for (char c : row) cntBoard[c]++;
        for (char c : word) cntWord[c]++;
        for (int i = 0; i < 128; ++i)
            if (cntWord[i] > cntBoard[i]) return false;

        // Start from rarer end character to reduce branching
        if (cntBoard[word[0]] > cntBoard[word.back()])
            reverse(word.begin(), word.end());

        function<bool(int,int,int)> dfs = [&](int i, int j, int idx) -> bool {
            if (idx == (int)word.size()) return true;
            if (i < 0 || i >= m || j < 0 || j >= n || board[i][j] != word[idx]) return false;

            char saved = board[i][j];
            board[i][j] = '#'; // mark visited
            static const int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
            for (auto &d : dirs) {
                if (dfs(i + d[0], j + d[1], idx + 1)) {
                    board[i][j] = saved;
                    return true;
                }
            }
            board[i][j] = saved; // backtrack
            return false;
        };

        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                if (board[i][j] == word[0])
                    if (dfs(i, j, 0)) return true;

        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean exist(char[][] board, String word) {
        int m = board.length;
        int n = board[0].length;
        char[] w = word.toCharArray();

        // frequency pruning
        int[] cntBoard = new int[128];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                cntBoard[board[i][j]]++;
            }
        }
        int[] cntWord = new int[128];
        for (char c : w) cntWord[c]++;
        for (int i = 0; i < 128; i++) {
            if (cntWord[i] > cntBoard[i]) return false;
        }

        // start from rarer end character to reduce branching
        if (cntBoard[w[0]] > cntBoard[w[w.length - 1]]) {
            for (int l = 0, r = w.length - 1; l < r; l++, r--) {
                char tmp = w[l];
                w[l] = w[r];
                w[r] = tmp;
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (dfs(board, i, j, w, 0)) return true;
            }
        }
        return false;
    }

    private boolean dfs(char[][] board, int i, int j, char[] word, int idx) {
        if (idx == word.length) return true;
        int m = board.length, n = board[0].length;
        if (i < 0 || j < 0 || i >= m || j >= n || board[i][j] != word[idx]) return false;

        char temp = board[i][j];
        board[i][j] = '#'; // mark visited

        boolean found = dfs(board, i + 1, j, word, idx + 1) ||
                        dfs(board, i - 1, j, word, idx + 1) ||
                        dfs(board, i, j + 1, word, idx + 1) ||
                        dfs(board, i, j - 1, word, idx + 1);

        board[i][j] = temp; // restore
        return found;
    }
}
```

## Python

```python
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False

        m, n = len(board), len(board[0])
        L = len(word)

        # Early pruning by character frequency
        from collections import Counter
        board_counter = Counter(c for row in board for c in row)
        word_counter = Counter(word)
        for ch, cnt in word_counter.items():
            if board_counter[ch] < cnt:
                return False

        # Optional: reverse word to start with rarer character
        if board_counter[word[0]] > board_counter[word[-1]]:
            word = word[::-1]

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == L - 1:
                return True

            tmp = board[i][j]
            board[i][j] = '#'
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != '#':
                    if dfs(ni, nj, k + 1):
                        board[i][j] = tmp
                        return True
            board[i][j] = tmp
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False
```

## Python3

```python
from typing import List
from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        # Prune by character frequency
        cnt_board = Counter(c for row in board for c in row)
        cnt_word = Counter(word)
        for ch, need in cnt_word.items():
            if need > cnt_board.get(ch, 0):
                return False
        
        # Optional: start from rarer end of the word to reduce branching
        if cnt_word[word[0]] > cnt_word[word[-1]]:
            word = word[::-1]
        
        def dfs(i: int, j: int, k: int) -> bool:
            if k == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False
            
            tmp = board[i][j]
            board[i][j] = '#'
            found = (dfs(i + 1, j, k + 1) or
                     dfs(i - 1, j, k + 1) or
                     dfs(i, j + 1, k + 1) or
                     dfs(i, j - 1, k + 1))
            board[i][j] = tmp
            return found
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False
```

## C

```c
#include <stdbool.h>
#include <string.h>

static bool dfs(char **board, int m, int *colSize, const char *word, int len,
                int idx, int i, int j) {
    if (idx == len) return true;
    if (i < 0 || i >= m) return false;
    if (j < 0 || j >= colSize[i]) return false;
    if (board[i][j] != word[idx]) return false;

    char temp = board[i][j];
    board[i][j] = '#'; // mark visited

    bool found = dfs(board, m, colSize, word, len, idx + 1, i - 1, j) ||
                 dfs(board, m, colSize, word, len, idx + 1, i + 1, j) ||
                 dfs(board, m, colSize, word, len, idx + 1, i, j - 1) ||
                 dfs(board, m, colSize, word, len, idx + 1, i, j + 1);

    board[i][j] = temp; // restore
    return found;
}

bool exist(char **board, int boardSize, int *boardColSize, char *word) {
    if (boardSize == 0 || !word) return false;
    int len = strlen(word);
    for (int i = 0; i < boardSize; ++i) {
        for (int j = 0; j < boardColSize[i]; ++j) {
            if (dfs(board, boardSize, boardColSize, word, len, 0, i, j))
                return true;
        }
    }
    return false;
}
```

## Csharp

```csharp
public class Solution
{
    public bool Exist(char[][] board, string word)
    {
        int rows = board.Length;
        int cols = board[0].Length;

        bool Dfs(int r, int c, int idx)
        {
            if (board[r][c] != word[idx]) return false;
            if (idx == word.Length - 1) return true;

            char temp = board[r][c];
            board[r][c] = '#';

            int[] dr = { -1, 1, 0, 0 };
            int[] dc = { 0, 0, -1, 1 };

            for (int k = 0; k < 4; ++k)
            {
                int nr = r + dr[k];
                int nc = c + dc[k];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && board[nr][nc] != '#')
                {
                    if (Dfs(nr, nc, idx + 1))
                    {
                        board[r][c] = temp;
                        return true;
                    }
                }
            }

            board[r][c] = temp;
            return false;
        }

        for (int i = 0; i < rows; ++i)
        {
            for (int j = 0; j < cols; ++j)
            {
                if (board[i][j] == word[0])
                {
                    if (Dfs(i, j, 0)) return true;
                }
            }
        }

        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
    const m = board.length, n = board[0].length;
    if (word.length > m * n) return false;

    // frequency pruning
    const cntBoard = {};
    for (let i = 0; i < m; ++i)
        for (let j = 0; j < n; ++j)
            cntBoard[board[i][j]] = (cntBoard[board[i][j]] || 0) + 1;
    const cntWord = {};
    for (const c of word)
        cntWord[c] = (cntWord[c] || 0) + 1;
    for (const c in cntWord)
        if ((cntBoard[c] || 0) < cntWord[c]) return false;

    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    function dfs(i, j, k) {
        if (k === word.length) return true;
        if (i < 0 || i >= m || j < 0 || j >= n || board[i][j] !== word[k]) return false;

        const temp = board[i][j];
        board[i][j] = '#'; // mark visited
        for (const [dx, dy] of dirs) {
            if (dfs(i + dx, j + dy, k + 1)) {
                board[i][j] = temp;
                return true;
            }
        }
        board[i][j] = temp; // restore
        return false;
    }

    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if (board[i][j] === word[0] && dfs(i, j, 0)) return true;
        }
    }
    return false;
};
```

## Typescript

```typescript
function exist(board: string[][], word: string): boolean {
    const m = board.length;
    const n = board[0].length;

    // Optional quick pruning: compare character frequencies
    const freqBoard: Record<string, number> = {};
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            const ch = board[i][j];
            freqBoard[ch] = (freqBoard[ch] ?? 0) + 1;
        }
    }
    const freqWord: Record<string, number> = {};
    for (const ch of word) {
        freqWord[ch] = (freqWord[ch] ?? 0) + 1;
        if ((freqBoard[ch] ?? 0) < freqWord[ch]) return false;
    }

    const dfs = (i: number, j: number, idx: number): boolean => {
        if (idx === word.length) return true;
        if (
            i < 0 || i >= m ||
            j < 0 || j >= n ||
            board[i][j] !== word[idx]
        ) {
            return false;
        }

        const temp = board[i][j];
        board[i][j] = '#'; // mark visited

        const found =
            dfs(i + 1, j, idx + 1) ||
            dfs(i - 1, j, idx + 1) ||
            dfs(i, j + 1, idx + 1) ||
            dfs(i, j - 1, idx + 1);

        board[i][j] = temp; // restore
        return found;
    };

    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if (board[i][j] === word[0]) {
                if (dfs(i, j, 0)) return true;
            }
        }
    }
    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param String[][] $board
     * @param String $word
     * @return Boolean
     */
    function exist($board, $word) {
        $rows = count($board);
        $cols = count($board[0]);
        $len  = strlen($word);

        // quick frequency prune
        $cntBoard = [];
        foreach ($board as $row) {
            foreach ($row as $ch) {
                $cntBoard[$ch] = ($cntBoard[$ch] ?? 0) + 1;
            }
        }
        $cntWord = [];
        for ($i = 0; $i < $len; $i++) {
            $c = $word[$i];
            $cntWord[$c] = ($cntWord[$c] ?? 0) + 1;
        }
        foreach ($cntWord as $c => $v) {
            if (!isset($cntBoard[$c]) || $cntBoard[$c] < $v) {
                return false;
            }
        }

        // optional reverse for better pruning
        $first = $word[0];
        $last  = $word[$len - 1];
        if ($cntBoard[$last] < $cntBoard[$first]) {
            $word = strrev($word);
        }

        $dfs = function($r, $c, $idx) use (&$board, $rows, $cols, $word, $len, &$dfs) {
            if ($idx == $len) {
                return true;
            }
            if ($r < 0 || $r >= $rows || $c < 0 || $c >= $cols || $board[$r][$c] !== $word[$idx]) {
                return false;
            }

            $temp = $board[$r][$c];
            $board[$r][$c] = '#';
            $nextIdx = $idx + 1;

            $found = $dfs($r + 1, $c, $nextIdx) ||
                     $dfs($r - 1, $c, $nextIdx) ||
                     $dfs($r, $c + 1, $nextIdx) ||
                     $dfs($r, $c - 1, $nextIdx);

            $board[$r][$c] = $temp;
            return $found;
        };

        for ($i = 0; $i < $rows; $i++) {
            for ($j = 0; $j < $cols; $j++) {
                if ($board[$i][$j] === $word[0]) {
                    if ($dfs($i, $j, 0)) {
                        return true;
                    }
                }
            }
        }

        return false;
    }
}
```

## Swift

```swift
class Solution {
    func exist(_ board: [[Character]], _ word: String) -> Bool {
        var board = board
        let rows = board.count
        guard rows > 0 else { return false }
        let cols = board[0].count
        let originalChars = Array(word)
        
        // Frequency pruning
        var freqBoard = [Character:Int]()
        for r in 0..<rows {
            for c in 0..<cols {
                freqBoard[board[r][c], default: 0] += 1
            }
        }
        var freqWord = [Character:Int]()
        for ch in originalChars {
            freqWord[ch, default: 0] += 1
        }
        for (ch, cnt) in freqWord {
            if freqBoard[ch, default: 0] < cnt { return false }
        }
        
        // Optional reversal to start with rarer character
        var chars = originalChars
        if let first = originalChars.first, let last = originalChars.last,
           freqBoard[last, default: 0] < freqBoard[first, default: 0] {
            chars = originalChars.reversed()
        }
        
        let directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        func dfs(_ i: Int, _ j: Int, _ idx: Int) -> Bool {
            if idx == chars.count { return true }
            if i < 0 || i >= rows || j < 0 || j >= cols { return false }
            if board[i][j] != chars[idx] { return false }
            
            let temp = board[i][j]
            board[i][j] = "#"
            for dir in directions {
                let ni = i + dir.0
                let nj = j + dir.1
                if dfs(ni, nj, idx + 1) {
                    board[i][j] = temp
                    return true
                }
            }
            board[i][j] = temp
            return false
        }
        
        for i in 0..<rows {
            for j in 0..<cols {
                if board[i][j] == chars[0] && dfs(i, j, 0) {
                    return true
                }
            }
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun exist(board: Array<CharArray>, word: String): Boolean {
        val m = board.size
        val n = board[0].size
        if (word.isEmpty()) return true

        // Count characters in board
        val boardCount = IntArray(128)
        for (i in 0 until m) {
            for (j in 0 until n) {
                boardCount[board[i][j].code]++
            }
        }

        // Quick prune: if any character appears less times than needed, return false
        val wordCount = IntArray(128)
        for (c in word) {
            wordCount[c.code]++
        }
        for (c in 0 until 128) {
            if (wordCount[c] > boardCount[c]) return false
        }

        // Choose direction of search to start with rarer end character
        var w = word
        if (boardCount[w[0].code] > boardCount[w[w.length - 1].code]) {
            w = w.reversed()
        }
        val chars = w.toCharArray()

        fun dfs(i: Int, j: Int, idx: Int): Boolean {
            if (board[i][j] != chars[idx]) return false
            if (idx == chars.lastIndex) return true

            val temp = board[i][j]
            board[i][j] = '#'

            val dirs = arrayOf(
                intArrayOf(1, 0),
                intArrayOf(-1, 0),
                intArrayOf(0, 1),
                intArrayOf(0, -1)
            )
            for (d in dirs) {
                val ni = i + d[0]
                val nj = j + d[1]
                if (ni in 0 until m && nj in 0 until n && board[ni][nj] != '#') {
                    if (dfs(ni, nj, idx + 1)) {
                        board[i][j] = temp
                        return true
                    }
                }
            }

            board[i][j] = temp
            return false
        }

        for (i in 0 until m) {
            for (j in 0 until n) {
                if (board[i][j] == chars[0]) {
                    if (dfs(i, j, 0)) return true
                }
            }
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool exist(List<List<String>> board, String word) {
    int m = board.length;
    int n = board[0].length;

    // Frequency pruning
    Map<String, int> boardCount = {};
    for (var row in board) {
      for (var ch in row) {
        boardCount[ch] = (boardCount[ch] ?? 0) + 1;
      }
    }
    Map<String, int> wordCount = {};
    for (int i = 0; i < word.length; i++) {
      String ch = word[i];
      wordCount[ch] = (wordCount[ch] ?? 0) + 1;
    }
    for (var entry in wordCount.entries) {
      if ((boardCount[entry.key] ?? 0) < entry.value) return false;
    }

    List<List<bool>> visited =
        List.generate(m, (_) => List.filled(n, false));

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (_dfs(board, word, 0, i, j, visited)) return true;
      }
    }
    return false;
  }

  bool _dfs(List<List<String>> board, String word, int idx, int r, int c,
      List<List<bool>> visited) {
    if (idx == word.length) return true;

    int m = board.length;
    int n = board[0].length;

    if (r < 0 || r >= m || c < 0 || c >= n) return false;
    if (visited[r][c]) return false;
    if (board[r][c] != word[idx]) return false;

    visited[r][c] = true;

    bool found = _dfs(board, word, idx + 1, r - 1, c, visited) ||
        _dfs(board, word, idx + 1, r + 1, c, visited) ||
        _dfs(board, word, idx + 1, r, c - 1, visited) ||
        _dfs(board, word, idx + 1, r, c + 1, visited);

    visited[r][c] = false;
    return found;
  }
}
```

## Golang

```go
func exist(board [][]byte, word string) bool {
	rows := len(board)
	cols := len(board[0])
	var dfs func(r, c, idx int) bool
	dfs = func(r, c, idx int) bool {
		if idx == len(word) {
			return true
		}
		if r < 0 || c < 0 || r >= rows || c >= cols || board[r][c] != word[idx] {
			return false
		}
		tmp := board[r][c]
		board[r][c] = '#'
		dirs := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
		for _, d := range dirs {
			if dfs(r+d[0], c+d[1], idx+1) {
				board[r][c] = tmp
				return true
			}
		}
		board[r][c] = tmp
		return false
	}

	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			if board[i][j] == word[0] && dfs(i, j, 0) {
				return true
			}
		}
	}
	return false
}
```

## Ruby

```ruby
def exist(board, word)
  rows = board.size
  cols = board[0].size

  # prune by character frequency
  freq_board = Hash.new(0)
  board.each { |row| row.each { |ch| freq_board[ch] += 1 } }
  freq_word = Hash.new(0)
  word.each_char { |ch| freq_word[ch] += 1 }
  return false if freq_word.any? { |ch, cnt| cnt > freq_board[ch] }

  # reverse word to start with rarer character
  if freq_board[word[0]] > freq_board[word[-1]]
    word = word.reverse
  end

  @board = board
  @word = word
  @rows = rows
  @cols = cols

  (0...rows).each do |i|
    (0...cols).each do |j|
      return true if dfs(i, j, 0)
    end
  end
  false
end

def dfs(r, c, idx)
  return false unless r.between?(0, @rows - 1) && c.between?(0, @cols - 1)
  return false if @board[r][c] != @word[idx]

  return true if idx == @word.length - 1

  temp = @board[r][c]
  @board[r][c] = '#'

  [[1, 0], [-1, 0], [0, 1], [0, -1]].each do |dr, dc|
    if dfs(r + dr, c + dc, idx + 1)
      @board[r][c] = temp
      return true
    end
  end

  @board[r][c] = temp
  false
end
```

## Scala

```scala
object Solution {
  def exist(board: Array[Array[Char]], word: String): Boolean = {
    val m = board.length
    val n = board(0).length

    // Prune by character frequency
    val boardCount = scala.collection.mutable.Map[Char, Int]().withDefaultValue(0)
    for (row <- board; ch <- row) boardCount(ch) += 1
    val wordCount = scala.collection.mutable.Map[Char, Int]().withDefaultValue(0)
    for (ch <- word) wordCount(ch) += 1
    for ((ch, cnt) <- wordCount) if (boardCount(ch) < cnt) return false

    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))

    def dfs(i: Int, j: Int, idx: Int): Boolean = {
      if (idx == word.length) return true
      if (i < 0 || i >= m || j < 0 || j >= n || board(i)(j) != word.charAt(idx)) return false

      val temp = board(i)(j)
      board(i)(j) = '#'

      for ((dx, dy) <- dirs) {
        if (dfs(i + dx, j + dy, idx + 1)) {
          board(i)(j) = temp
          return true
        }
      }

      board(i)(j) = temp
      false
    }

    for (i <- 0 until m; j <- 0 until n) {
      if (board(i)(j) == word.charAt(0) && dfs(i, j, 0)) return true
    }
    false
  }
}
```

## Rust

```rust
impl Solution {
    pub fn exist(board: Vec<Vec<char>>, word: String) -> bool {
        let mut board = board;
        let rows = board.len();
        if rows == 0 {
            return false;
        }
        let cols = board[0].len();
        let w = word.as_bytes();

        fn dfs(board: &mut Vec<Vec<char>>, i: usize, j: usize, idx: usize, w: &[u8]) -> bool {
            if board[i][j] != w[idx] as char {
                return false;
            }
            if idx == w.len() - 1 {
                return true;
            }

            let temp = board[i][j];
            board[i][j] = '#';

            let dirs = [(0i32, 1i32), (1, 0), (-1, 0), (0, -1)];
            for (dx, dy) in dirs.iter() {
                let ni = i as i32 + dx;
                let nj = j as i32 + dy;
                if ni >= 0
                    && (ni as usize) < board.len()
                    && nj >= 0
                    && (nj as usize) < board[0].len()
                {
                    if dfs(board, ni as usize, nj as usize, idx + 1, w) {
                        board[i][j] = temp;
                        return true;
                    }
                }
            }

            board[i][j] = temp;
            false
        }

        for i in 0..rows {
            for j in 0..cols {
                if board[i][j] == w[0] as char && dfs(&mut board, i, j, 0, w) {
                    return true;
                }
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (exist board word)
  (-> (listof (listof char?)) string? boolean?)
  (let* ((m (length board))
         (n (if (> m 0) (length (first board)) 0))
         (board-vec (list->vector (map list->vector board)))
         (visited
           (let ((v (make-vector m)))
             (for ([i (in-range m)])
               (vector-set! v i (make-vector n #f)))
             v))
         (wordlen (string-length word))
         (first-char (if (> wordlen 0) (string-ref word 0) #\null)))
    (letrec ((dfs
              (lambda (i j idx)
                (cond
                  [(= idx wordlen) #t]
                  [(or (< i 0) (>= i m) (< j 0) (>= j n)) #f]
                  [else
                   (let* ((c (vector-ref (vector-ref board-vec i) j))
                          (target (string-ref word idx)))
                     (if (char=? c target)
                         (if (vector-ref (vector-ref visited i) j)
                             #f
                             (begin
                               (vector-set! (vector-ref visited i) j #t)
                               (let ((found (or (dfs (+ i 1) j (+ idx 1))
                                                (dfs (- i 1) j (+ idx 1))
                                                (dfs i (+ j 1) (+ idx 1))
                                                (dfs i (- j 1) (+ idx 1)))))
                                 (vector-set! (vector-ref visited i) j #f)
                                 found)))
                         #f))))))
      (for*/or ([i (in-range m)]
                [j (in-range n)])
        (and (char=? (vector-ref (vector-ref board-vec i) j) first-char)
             (dfs i j 0))))))
```

## Erlang

```erlang
-module(solution).
-export([exist/2]).

-spec exist(Board :: [[char()]], Word :: unicode:unicode_binary()) -> boolean().
exist(Board, Word) ->
    WordChars = unicode:characters_to_list(Word),
    case Board of
        [] -> false;
        _ ->
            M = length(Board),
            N = length(lists:nth(1, Board)),
            exist_loop(Board, WordChars, M, N)
    end.

exist_loop(Board, WordChars, M, N) ->
    lists:any(fun(R) ->
        lists:any(fun(C) ->
            case get_char(Board, R, C) of
                First when First =:= hd(WordChars) ->
                    dfs(Board, WordChars, R, C, #{});
                _ -> false
            end
        end, lists:seq(0, N - 1))
    end, lists:seq(0, M - 1)).

dfs(_Board, [], _Row, _Col, _Visited) ->
    true;
dfs(Board, [Char | Rest], Row, Col, Visited) ->
    case get_char(Board, Row, Col) of
        Char ->
            if Rest =:= [] -> true;
               true ->
                NewVisited = maps:put({Row, Col}, true, Visited),
                Neighbors = [{Row - 1, Col}, {Row + 1, Col},
                             {Row, Col - 1}, {Row, Col + 1}],
                lists:any(fun({NR, NC}) ->
                    case is_valid(NR, NC, Board) of
                        true ->
                            case maps:is_key({NR, NC}, NewVisited) of
                                false -> dfs(Board, Rest, NR, NC, NewVisited);
                                true -> false
                            end;
                        false -> false
                    end
                end, Neighbors)
            end;
        _Other -> false
    end.

is_valid(R, C, Board) ->
    R >= 0,
    C >= 0,
    M = length(Board),
    N = case Board of [] -> 0; [_|_] -> length(lists:nth(1, Board)) end,
    R < M andalso C < N.

get_char(Board, R, C) ->
    RowList = lists:nth(R + 1, Board),
    lists:nth(C + 1, RowList).
```

## Elixir

```elixir
defmodule Solution do
  @spec exist(board :: [[String.t()]], word :: String.t()) :: boolean()
  def exist(board, word) do
    chars = String.graphemes(word)
    rows = length(board)
    cols = if rows > 0, do: length(hd(board)), else: 0

    Enum.any?(0..rows - 1, fn i ->
      Enum.any?(0..cols - 1, fn j ->
        dfs(board, chars, i, j, 0, MapSet.new())
      end)
    end)
  end

  defp dfs(_board, chars, _i, _j, idx, _visited) when idx == length(chars), do: true

  defp dfs(board, chars, i, j, idx, visited) do
    rows = length(board)
    cols = if rows > 0, do: length(hd(board)), else: 0

    cond do
      i < 0 or i >= rows or j < 0 or j >= cols ->
        false

      MapSet.member?(visited, {i, j}) ->
        false

      true ->
        current_char = Enum.at(Enum.at(board, i), j)

        if current_char != Enum.at(chars, idx) do
          false
        else
          new_visited = MapSet.put(visited, {i, j})

          dfs(board, chars, i + 1, j, idx + 1, new_visited) ||
            dfs(board, chars, i - 1, j, idx + 1, new_visited) ||
            dfs(board, chars, i, j + 1, idx + 1, new_visited) ||
            dfs(board, chars, i, j - 1, idx + 1, new_visited)
        end
    end
  end
end
```
