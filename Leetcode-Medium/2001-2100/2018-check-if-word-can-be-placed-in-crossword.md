# 2018. Check if Word Can Be Placed In Crossword

## Cpp

```cpp
class Solution {
public:
    bool placeWordInCrossword(vector<vector<char>>& board, string word) {
        int m = board.size(), n = board[0].size();
        int L = word.size();

        auto canFit = [&](int i, int j, int di, int dj) -> bool {
            for (int k = 0; k < L; ++k) {
                char c = board[i + k*di][j + k*dj];
                if (c != ' ' && c != word[k]) return false;
            }
            return true;
        };

        // check rows
        for (int i = 0; i < m; ++i) {
            int j = 0;
            while (j < n) {
                while (j < n && board[i][j] == '#') ++j;
                if (j >= n) break;
                int start = j;
                while (j < n && board[i][j] != '#') ++j;
                int len = j - start;
                if (len == L) {
                    // forward
                    bool ok = true;
                    for (int k = 0; k < L; ++k) {
                        char c = board[i][start + k];
                        if (c != ' ' && c != word[k]) { ok = false; break; }
                    }
                    if (ok) return true;
                    // backward
                    ok = true;
                    for (int k = 0; k < L; ++k) {
                        char c = board[i][start + k];
                        if (c != ' ' && c != word[L-1-k]) { ok = false; break; }
                    }
                    if (ok) return true;
                }
            }
        }

        // check columns
        for (int j = 0; j < n; ++j) {
            int i = 0;
            while (i < m) {
                while (i < m && board[i][j] == '#') ++i;
                if (i >= m) break;
                int start = i;
                while (i < m && board[i][j] != '#') ++i;
                int len = i - start;
                if (len == L) {
                    // forward (top to bottom)
                    bool ok = true;
                    for (int k = 0; k < L; ++k) {
                        char c = board[start + k][j];
                        if (c != ' ' && c != word[k]) { ok = false; break; }
                    }
                    if (ok) return true;
                    // backward (bottom to top)
                    ok = true;
                    for (int k = 0; k < L; ++k) {
                        char c = board[start + k][j];
                        if (c != ' ' && c != word[L-1-k]) { ok = false; break; }
                    }
                    if (ok) return true;
                }
            }
        }

        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean placeWordInCrossword(char[][] board, String word) {
        int m = board.length;
        int n = board[0].length;
        int wlen = word.length();
        // check rows
        for (int i = 0; i < m; i++) {
            int j = 0;
            while (j < n) {
                if (board[i][j] == '#') {
                    j++;
                    continue;
                }
                int start = j;
                while (j < n && board[i][j] != '#') j++;
                int len = j - start;
                if (len == wlen && fits(board, i, start, 0, word)) return true;
                if (len == wlen && fitsReverse(board, i, start, 0, word)) return true;
            }
        }
        // check columns
        for (int j = 0; j < n; j++) {
            int i = 0;
            while (i < m) {
                if (board[i][j] == '#') {
                    i++;
                    continue;
                }
                int start = i;
                while (i < m && board[i][j] != '#') i++;
                int len = i - start;
                if (len == wlen && fits(board, start, j, 1, word)) return true;
                if (len == wlen && fitsReverse(board, start, j, 1, word)) return true;
            }
        }
        return false;
    }

    private boolean fits(char[][] board, int r, int c, int dir, String word) {
        // dir: 0 = horizontal, 1 = vertical
        for (int k = 0; k < word.length(); k++) {
            char ch = dir == 0 ? board[r][c + k] : board[r + k][c];
            if (ch != ' ' && ch != word.charAt(k)) return false;
        }
        return true;
    }

    private boolean fitsReverse(char[][] board, int r, int c, int dir, String word) {
        for (int k = 0; k < word.length(); k++) {
            char ch = dir == 0 ? board[r][c + k] : board[r + k][c];
            if (ch != ' ' && ch != word.charAt(word.length() - 1 - k)) return false;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def placeWordInCrossword(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        L = len(word)

        def match(seg, w):
            for a, b in zip(seg, w):
                if a != ' ' and a != b:
                    return False
            return True

        def check(lines):
            for line in lines:
                i = 0
                while i < len(line):
                    if line[i] == '#':
                        i += 1
                        continue
                    j = i
                    while j < len(line) and line[j] != '#':
                        j += 1
                    seg = line[i:j]
                    if len(seg) == L:
                        if match(seg, word) or match(seg, word[::-1]):
                            return True
                    i = j
            return False

        rows = board
        cols = [[board[i][j] for i in range(m)] for j in range(n)]

        return check(rows) or check(cols)
```

## Python3

```python
class Solution:
    def placeWordInCrossword(self, board, word):
        m, n = len(board), len(board[0])
        L = len(word)

        def fits(segment):
            if len(segment) != L:
                return False
            # forward
            ok = True
            for c, w in zip(segment, word):
                if c != ' ' and c != w:
                    ok = False
                    break
            if ok:
                return True
            # backward
            ok = True
            for c, w in zip(segment, reversed(word)):
                if c != ' ' and c != w:
                    ok = False
                    break
            return ok

        # horizontal check
        for i in range(m):
            j = 0
            while j < n:
                # skip blocked cells
                while j < n and board[i][j] == '#':
                    j += 1
                if j >= n:
                    break
                start = j
                segment = []
                while j < n and board[i][j] != '#':
                    segment.append(board[i][j])
                    j += 1
                # now segment is from start to j-1, bounded by # or edges
                if fits(segment):
                    return True

        # vertical check
        for col in range(n):
            i = 0
            while i < m:
                while i < m and board[i][col] == '#':
                    i += 1
                if i >= m:
                    break
                segment = []
                while i < m and board[i][col] != '#':
                    segment.append(board[i][col])
                    i += 1
                if fits(segment):
                    return True

        return False
```

## C

```c
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

static bool canPlaceHorizontal(char **board, int row, int col, const char *word, int wlen, int cols) {
    if (col + wlen > cols) return false;
    if (col + wlen < cols && board[row][col + wlen] != '#') return false;
    for (int k = 0; k < wlen; ++k) {
        char c = board[row][col + k];
        if (c == '#') return false;
        if (c != ' ' && c != word[k]) return false;
    }
    return true;
}

static bool canPlaceVertical(char **board, int row, int col, const char *word, int wlen, int rows) {
    if (row + wlen > rows) return false;
    if (row + wlen < rows && board[row + wlen][col] != '#') return false;
    for (int k = 0; k < wlen; ++k) {
        char c = board[row + k][col];
        if (c == '#') return false;
        if (c != ' ' && c != word[k]) return false;
    }
    return true;
}

bool placeWordInCrossword(char** board, int boardSize, int* boardColSize, char* word) {
    int rows = boardSize;
    int cols = boardColSize[0];
    int wlen = (int)strlen(word);

    // reversed word
    char *rev = (char *)malloc(wlen + 1);
    for (int i = 0; i < wlen; ++i) rev[i] = word[wlen - 1 - i];
    rev[wlen] = '\0';

    // Horizontal placements
    for (int i = 0; i < rows; ++i) {
        int curCols = boardColSize[i];
        for (int j = 0; j < curCols; ++j) {
            if (j == 0 || board[i][j - 1] == '#') {
                if (canPlaceHorizontal(board, i, j, word, wlen, curCols) ||
                    canPlaceHorizontal(board, i, j, rev, wlen, curCols)) {
                    free(rev);
                    return true;
                }
            }
        }
    }

    // Vertical placements
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            if (i == 0 || board[i - 1][j] == '#') {
                if (canPlaceVertical(board, i, j, word, wlen, rows) ||
                    canPlaceVertical(board, i, j, rev, wlen, rows)) {
                    free(rev);
                    return true;
                }
            }
        }
    }

    free(rev);
    return false;
}
```

## Csharp

```csharp
public class Solution
{
    public bool PlaceWordInCrossword(char[][] board, string word)
    {
        int m = board.Length;
        int n = board[0].Length;
        int wlen = word.Length;

        // Check rows
        for (int i = 0; i < m; i++)
        {
            int j = 0;
            while (j < n)
            {
                if (board[i][j] == '#')
                {
                    j++;
                    continue;
                }
                int start = j;
                while (j < n && board[i][j] != '#') j++;
                int len = j - start;
                if (len == wlen && IsFit(board, i, start, true, word))
                    return true;
            }
        }

        // Check columns
        for (int col = 0; col < n; col++)
        {
            int i = 0;
            while (i < m)
            {
                if (board[i][col] == '#')
                {
                    i++;
                    continue;
                }
                int start = i;
                while (i < m && board[i][col] != '#') i++;
                int len = i - start;
                if (len == wlen && IsFit(board, start, col, false, word))
                    return true;
            }
        }

        return false;
    }

    private bool IsFit(char[][] board, int rowOrStart, int colOrStart, bool horizontal, string word)
    {
        int len = word.Length;
        bool forwardOk = true, backwardOk = true;

        for (int k = 0; k < len; k++)
        {
            char cell = horizontal
                ? board[rowOrStart][colOrStart + k]
                : board[rowOrStart + k][colOrStart];

            if (cell != ' ')
            {
                if (cell != word[k]) forwardOk = false;
                if (cell != word[len - 1 - k]) backwardOk = false;
            }
        }

        return forwardOk || backwardOk;
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
var placeWordInCrossword = function(board, word) {
    const m = board.length;
    const n = board[0].length;
    const wlen = word.length;
    const rev = word.split('').reverse().join('');
    
    // check a segment of exact length wlen against target string
    const matches = (segmentStart, segmentEnd, getChar, target) => {
        for (let k = 0; k < wlen; ++k) {
            const ch = getChar(segmentStart + k);
            if (ch !== ' ' && ch !== target[k]) return false;
        }
        return true;
    };
    
    // rows
    for (let i = 0; i < m; ++i) {
        let j = 0;
        while (j < n) {
            if (board[i][j] === '#') { j++; continue; }
            const start = j;
            while (j < n && board[i][j] !== '#') j++;
            const len = j - start;
            if (len === wlen) {
                // forward
                if (matches(start, start + len,
                    k => board[i][k],
                    word)) return true;
                // backward
                if (matches(start, start + len,
                    k => board[i][k],
                    rev)) return true;
            }
        }
    }
    
    // columns
    for (let j = 0; j < n; ++j) {
        let i = 0;
        while (i < m) {
            if (board[i][j] === '#') { i++; continue; }
            const start = i;
            while (i < m && board[i][j] !== '#') i++;
            const len = i - start;
            if (len === wlen) {
                // forward (top to bottom)
                if (matches(start, start + len,
                    k => board[k][j],
                    word)) return true;
                // backward (bottom to top)
                if (matches(start, start + len,
                    k => board[k][j],
                    rev)) return true;
            }
        }
    }
    
    return false;
};
```

## Typescript

```typescript
function placeWordInCrossword(board: string[][], word: string): boolean {
    const m = board.length;
    const n = board[0].length;

    const canPlace = (segment: string[], w: string): boolean => {
        if (segment.length !== w.length) return false;
        let forward = true, backward = true;
        const len = w.length;
        for (let i = 0; i < len; i++) {
            const ch = segment[i];
            if (ch !== ' ') {
                if (ch !== w[i]) forward = false;
                if (ch !== w[len - 1 - i]) backward = false;
            }
        }
        return forward || backward;
    };

    // Check rows
    for (let i = 0; i < m; i++) {
        let start = 0;
        for (let j = 0; j <= n; j++) {
            if (j === n || board[i][j] === '#') {
                const len = j - start;
                if (len === word.length) {
                    const segment = board[i].slice(start, j);
                    if (canPlace(segment, word)) return true;
                }
                start = j + 1;
            }
        }
    }

    // Check columns
    for (let j = 0; j < n; j++) {
        let start = 0;
        for (let i = 0; i <= m; i++) {
            if (i === m || board[i][j] === '#') {
                const len = i - start;
                if (len === word.length) {
                    const segment: string[] = [];
                    for (let k = start; k < i; k++) segment.push(board[k][j]);
                    if (canPlace(segment, word)) return true;
                }
                start = i + 1;
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
    function placeWordInCrossword($board, $word) {
        $m = count($board);
        if ($m == 0) return false;
        $n = count($board[0]);
        $len = strlen($word);

        // check rows
        for ($i = 0; $i < $m; $i++) {
            $j = 0;
            while ($j < $n) {
                // skip blocked cells
                while ($j < $n && $board[$i][$j] === '#') $j++;
                if ($j >= $n) break;
                $start = $j;
                while ($j < $n && $board[$i][$j] !== '#') $j++;
                $end = $j - 1;
                $segmentLen = $end - $start + 1;
                if ($segmentLen === $len) {
                    // forward
                    $ok = true;
                    for ($k = 0; $k < $len; $k++) {
                        $c = $board[$i][$start + $k];
                        if ($c !== ' ' && $c !== $word[$k]) {
                            $ok = false;
                            break;
                        }
                    }
                    if ($ok) return true;

                    // reverse
                    $ok = true;
                    for ($k = 0; $k < $len; $k++) {
                        $c = $board[$i][$start + $k];
                        $w = $word[$len - 1 - $k];
                        if ($c !== ' ' && $c !== $w) {
                            $ok = false;
                            break;
                        }
                    }
                    if ($ok) return true;
                }
            }
        }

        // check columns
        for ($j = 0; $j < $n; $j++) {
            $i = 0;
            while ($i < $m) {
                while ($i < $m && $board[$i][$j] === '#') $i++;
                if ($i >= $m) break;
                $start = $i;
                while ($i < $m && $board[$i][$j] !== '#') $i++;
                $end = $i - 1;
                $segmentLen = $end - $start + 1;
                if ($segmentLen === $len) {
                    // forward (top to bottom)
                    $ok = true;
                    for ($k = 0; $k < $len; $k++) {
                        $c = $board[$start + $k][$j];
                        if ($c !== ' ' && $c !== $word[$k]) {
                            $ok = false;
                            break;
                        }
                    }
                    if ($ok) return true;

                    // reverse (bottom to top)
                    $ok = true;
                    for ($k = 0; $k < $len; $k++) {
                        $c = $board[$start + $k][$j];
                        $w = $word[$len - 1 - $k];
                        if ($c !== ' ' && $c !== $w) {
                            $ok = false;
                            break;
                        }
                    }
                    if ($ok) return true;
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
    func placeWordInCrossword(_ board: [[Character]], _ word: String) -> Bool {
        let m = board.count
        guard m > 0 else { return false }
        let n = board[0].count
        let wArr = Array(word)
        let lenW = wArr.count

        // Horizontal check
        for i in 0..<m {
            var j = 0
            while j < n {
                if board[i][j] == "#" {
                    j += 1
                    continue
                }
                let start = j
                while j < n && board[i][j] != "#" {
                    j += 1
                }
                let end = j - 1
                let segLen = end - start + 1
                if segLen == lenW {
                    var okFwd = true
                    for k in 0..<lenW {
                        let ch = board[i][start + k]
                        if ch != " " && ch != wArr[k] {
                            okFwd = false
                            break
                        }
                    }
                    if okFwd { return true }

                    var okRev = true
                    for k in 0..<lenW {
                        let ch = board[i][start + k]
                        if ch != " " && ch != wArr[lenW - 1 - k] {
                            okRev = false
                            break
                        }
                    }
                    if okRev { return true }
                }
            }
        }

        // Vertical check
        for j in 0..<n {
            var i = 0
            while i < m {
                if board[i][j] == "#" {
                    i += 1
                    continue
                }
                let start = i
                while i < m && board[i][j] != "#" {
                    i += 1
                }
                let end = i - 1
                let segLen = end - start + 1
                if segLen == lenW {
                    var okFwd = true
                    for k in 0..<lenW {
                        let ch = board[start + k][j]
                        if ch != " " && ch != wArr[k] {
                            okFwd = false
                            break
                        }
                    }
                    if okFwd { return true }

                    var okRev = true
                    for k in 0..<lenW {
                        let ch = board[start + k][j]
                        if ch != " " && ch != wArr[lenW - 1 - k] {
                            okRev = false
                            break
                        }
                    }
                    if okRev { return true }
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
    fun placeWordInCrossword(board: Array<CharArray>, word: String): Boolean {
        val m = board.size
        val n = board[0].size
        // Check rows
        for (i in 0 until m) {
            var j = 0
            while (j < n) {
                while (j < n && board[i][j] == '#') j++
                if (j >= n) break
                val start = j
                while (j < n && board[i][j] != '#') j++
                val len = j - start
                if (len == word.length) {
                    var ok = true
                    for (k in 0 until len) {
                        val c = board[i][start + k]
                        if (c != ' ' && c != word[k]) { ok = false; break }
                    }
                    if (ok) return true
                    ok = true
                    for (k in 0 until len) {
                        val c = board[i][start + k]
                        if (c != ' ' && c != word[len - 1 - k]) { ok = false; break }
                    }
                    if (ok) return true
                }
            }
        }
        // Check columns
        for (j in 0 until n) {
            var i = 0
            while (i < m) {
                while (i < m && board[i][j] == '#') i++
                if (i >= m) break
                val start = i
                while (i < m && board[i][j] != '#') i++
                val len = i - start
                if (len == word.length) {
                    var ok = true
                    for (k in 0 until len) {
                        val c = board[start + k][j]
                        if (c != ' ' && c != word[k]) { ok = false; break }
                    }
                    if (ok) return true
                    ok = true
                    for (k in 0 until len) {
                        val c = board[start + k][j]
                        if (c != ' ' && c != word[len - 1 - k]) { ok = false; break }
                    }
                    if (ok) return true
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
  bool placeWordInCrossword(List<List<String>> board, String word) {
    int m = board.length;
    int n = board[0].length;
    int wlen = word.length;

    // Check rows
    for (int i = 0; i < m; i++) {
      int start = 0;
      for (int j = 0; j <= n; j++) {
        if (j == n || board[i][j] == '#') {
          int len = j - start;
          if (len == wlen) {
            bool ok = true;
            for (int k = 0; k < wlen; k++) {
              String ch = board[i][start + k];
              if (ch != ' ' && ch != word[k]) {
                ok = false;
                break;
              }
            }
            if (ok) return true;

            ok = true;
            for (int k = 0; k < wlen; k++) {
              String ch = board[i][start + k];
              if (ch != ' ' && ch != word[wlen - 1 - k]) {
                ok = false;
                break;
              }
            }
            if (ok) return true;
          }
          start = j + 1;
        }
      }
    }

    // Check columns
    for (int j = 0; j < n; j++) {
      int start = 0;
      for (int i = 0; i <= m; i++) {
        if (i == m || board[i][j] == '#') {
          int len = i - start;
          if (len == wlen) {
            bool ok = true;
            for (int k = 0; k < wlen; k++) {
              String ch = board[start + k][j];
              if (ch != ' ' && ch != word[k]) {
                ok = false;
                break;
              }
            }
            if (ok) return true;

            ok = true;
            for (int k = 0; k < wlen; k++) {
              String ch = board[start + k][j];
              if (ch != ' ' && ch != word[wlen - 1 - k]) {
                ok = false;
                break;
              }
            }
            if (ok) return true;
          }
          start = i + 1;
        }
      }
    }

    return false;
  }
}
```

## Golang

```go
func placeWordInCrossword(board [][]byte, word string) bool {
    m := len(board)
    n := len(board[0])
    wlen := len(word)

    // check rows
    for i := 0; i < m; i++ {
        j := 0
        for j < n {
            for j < n && board[i][j] == '#' {
                j++
            }
            start := j
            for j < n && board[i][j] != '#' {
                j++
            }
            end := j
            if end-start == wlen {
                seg := board[i][start:end]
                if match(seg, word) || matchReverse(seg, word) {
                    return true
                }
            }
        }
    }

    // check columns
    for col := 0; col < n; col++ {
        i := 0
        for i < m {
            for i < m && board[i][col] == '#' {
                i++
            }
            start := i
            for i < m && board[i][col] != '#' {
                i++
            }
            end := i
            if end-start == wlen {
                if matchCol(board, col, start, word) || matchColReverse(board, col, start, word) {
                    return true
                }
            }
        }
    }

    return false
}

func match(seg []byte, word string) bool {
    for i := 0; i < len(word); i++ {
        if seg[i] != ' ' && seg[i] != word[i] {
            return false
        }
    }
    return true
}

func matchReverse(seg []byte, word string) bool {
    l := len(word)
    for i := 0; i < l; i++ {
        if seg[i] != ' ' && seg[i] != word[l-1-i] {
            return false
        }
    }
    return true
}

func matchCol(board [][]byte, col, start int, word string) bool {
    for i := 0; i < len(word); i++ {
        c := board[start+i][col]
        if c != ' ' && c != word[i] {
            return false
        }
    }
    return true
}

func matchColReverse(board [][]byte, col, start int, word string) bool {
    l := len(word)
    for i := 0; i < l; i++ {
        c := board[start+i][col]
        if c != ' ' && c != word[l-1-i] {
            return false
        }
    }
    return true
}
```

## Ruby

```ruby
def place_word_in_crossword(board, word)
  m = board.size
  n = board[0].size
  wlen = word.length
  fwd = word.chars
  rev = fwd.reverse

  # horizontal placements
  (0...m).each do |i|
    (0..n - wlen).each do |j|
      next unless j == 0 || board[i][j - 1] == '#'
      next unless j + wlen == n || board[i][j + wlen] == '#'

      ok = true
      (0...wlen).each do |k|
        c = board[i][j + k]
        if c == '#'
          ok = false
          break
        end
        unless c == ' ' || c == fwd[k]
          ok = false
          break
        end
      end
      return true if ok

      ok = true
      (0...wlen).each do |k|
        c = board[i][j + k]
        if c == '#'
          ok = false
          break
        end
        unless c == ' ' || c == rev[k]
          ok = false
          break
        end
      end
      return true if ok
    end
  end

  # vertical placements
  (0...n).each do |j|
    (0..m - wlen).each do |i|
      next unless i == 0 || board[i - 1][j] == '#'
      next unless i + wlen == m || board[i + wlen][j] == '#'

      ok = true
      (0...wlen).each do |k|
        c = board[i + k][j]
        if c == '#'
          ok = false
          break
        end
        unless c == ' ' || c == fwd[k]
          ok = false
          break
        end
      end
      return true if ok

      ok = true
      (0...wlen).each do |k|
        c = board[i + k][j]
        if c == '#'
          ok = false
          break
        end
        unless c == ' ' || c == rev[k]
          ok = false
          break
        end
      end
      return true if ok
    end
  end

  false
end
```

## Scala

```scala
object Solution {
  def placeWordInCrossword(board: Array[Array[Char]], word: String): Boolean = {
    val rev = word.reverse
    val rows = board.length
    val cols = board(0).length

    // check each row
    for (r <- 0 until rows) {
      if (canPlace(board(r), word) || canPlace(board(r), rev)) return true
    }

    // check each column
    val colArr = new Array[Char](rows)
    for (c <- 0 until cols) {
      var i = 0
      while (i < rows) {
        colArr(i) = board(i)(c)
        i += 1
      }
      if (canPlace(colArr, word) || canPlace(colArr, rev)) return true
    }

    false
  }

  private def canPlace(line: Array[Char], word: String): Boolean = {
    val n = line.length
    val wlen = word.length
    var i = 0
    while (i <= n - wlen) {
      if ((i == 0 || line(i - 1) == '#') && (i + wlen == n || line(i + wlen) == '#')) {
        var ok = true
        var j = 0
        while (j < wlen && ok) {
          val c = line(i + j)
          if (c != ' ' && c != word.charAt(j)) ok = false
          j += 1
        }
        if (ok) return true
      }
      i += 1
    }
    false
  }
}
```

## Rust

```rust
impl Solution {
    pub fn place_word_in_crossword(board: Vec<Vec<char>>, word: String) -> bool {
        let m = board.len();
        if m == 0 {
            return false;
        }
        let n = board[0].len();
        let w: Vec<char> = word.chars().collect();
        let dirs: [(i32, i32); 4] = [(0, 1), (0, -1), (1, 0), (-1, 0)];

        for i in 0..m {
            for j in 0..n {
                for &(dr, dc) in &dirs {
                    // Check cell before start
                    let pi = i as i32 - dr;
                    let pj = j as i32 - dc;
                    if pi >= 0 && pi < m as i32 && pj >= 0 && pj < n as i32 {
                        if board[pi as usize][pj as usize] != '#' {
                            continue;
                        }
                    }

                    // Try to place the word
                    let mut ok = true;
                    for (idx, &ch) in w.iter().enumerate() {
                        let r = i as i32 + dr * idx as i32;
                        let c = j as i32 + dc * idx as i32;
                        if r < 0 || r >= m as i32 || c < 0 || c >= n as i32 {
                            ok = false;
                            break;
                        }
                        let cell = board[r as usize][c as usize];
                        if cell == '#' {
                            ok = false;
                            break;
                        }
                        if cell != ' ' && cell != ch {
                            ok = false;
                            break;
                        }
                    }
                    if !ok {
                        continue;
                    }

                    // Check cell after the word
                    let fi = i as i32 + dr * w.len() as i32;
                    let fj = j as i32 + dc * w.len() as i32;
                    if fi >= 0 && fi < m as i32 && fj >= 0 && fj < n as i32 {
                        if board[fi as usize][fj as usize] != '#' {
                            continue;
                        }
                    }

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
(define/contract (place-word-in-crossword board word)
  (-> (listof (listof char?)) string? boolean?)
  (let* ((m (length board))
         (n (if (> m 0) (length (first board)) 0))
         (wordlen (string-length word)))
    (define (split-segments line)
      (let loop ((lst line) (curr '()) (res '()))
        (cond
          [(null? lst)
           (if (null? curr) (reverse res) (reverse (cons (reverse curr) res)))]
          [else
           (let ((ch (car lst)))
             (if (char=? ch #\#)
                 (loop (cdr lst) '() (if (null? curr) res (cons (reverse curr) res)))
                 (loop (cdr lst) (cons ch curr) res))))]))
    (define (seg-matches? seg)
      (or
       (for/and ([i (in-range wordlen)])
         (let ((c (list-ref seg i))
               (w (string-ref word i)))
           (or (char=? c #\space) (char=? c w))))
       (for/and ([i (in-range wordlen)])
         (let ((c (list-ref seg i))
               (w (string-ref word (- wordlen 1 i))))
           (or (char=? c #\space) (char=? c w))))))
    (define (check-lines lines)
      (for/or ([line lines])
        (let ((segs (split-segments line)))
          (for/or ([seg segs])
            (and (= (length seg) wordlen)
                 (seg-matches? seg))))))
    (if (check-lines board)
        #t
        (let ((cols (for/list ([j (in-range n)])
                      (for/list ([i (in-range m)])
                        (list-ref (list-ref board i) j)))))
          (check-lines cols)))) )
```

## Erlang

```erlang
-module(solution).
-export([place_word_in_crossword/2]).

-spec place_word_in_crossword(Board :: [[char()]], Word :: unicode:unicode_binary()) -> boolean().
place_word_in_crossword(Board, Word) ->
    WordList = unicode:characters_to_list(Word),
    RevWord = lists:reverse(WordList),
    Len = length(WordList),
    case any_line_ok(Board, WordList, RevWord, Len) of
        true -> true;
        false ->
            Cols = transpose(Board),
            any_line_ok(Cols, WordList, RevWord, Len)
    end.

%% check all lines (rows or columns)
any_line_ok([], _W, _RW, _Len) -> false;
any_line_ok([Line | Rest], W, RW, Len) ->
    case line_has_word(Line, W, RW, Len) of
        true -> true;
        false -> any_line_ok(Rest, W, RW, Len)
    end.

%% does a single line contain the word in either direction?
line_has_word(Line, W, RW, Len) ->
    Segments = split_on_hash(Line),
    has_matching_segment(Segments, W, RW, Len).

has_matching_segment([], _W, _RW, _Len) -> false;
has_matching_segment([Seg | Rest], W, RW, Len) ->
    case length(Seg) == Len of
        true ->
            case matches_seg(Seg, W) orelse matches_seg(Seg, RW) of
                true -> true;
                false -> has_matching_segment(Rest, W, RW, Len)
            end;
        false -> has_matching_segment(Rest, W, RW, Len)
    end.

%% segment matches word (allow spaces)
matches_seg(Seg, Word) ->
    lists:all(
      fun({Cell, Char}) -> Cell == $  orelse Cell == Char end,
      lists:zip(Seg, Word)
    ).

%% split a line into maximal segments without '#'
split_on_hash(Line) -> split_on_hash(Line, [], []).

split_on_hash([], [], Acc) ->
    lists:reverse(Acc);
split_on_hash([], Curr, Acc) ->
    lists:reverse([lists:reverse(Curr) | Acc]);
split_on_hash([H | T], Curr, Acc) when H == $# ->
    case Curr of
        [] -> split_on_hash(T, [], Acc);
        _  -> split_on_hash(T, [], [lists:reverse(Curr) | Acc])
    end;
split_on_hash([H | T], Curr, Acc) ->
    split_on_hash(T, [H | Curr], Acc).

%% transpose matrix to get columns as rows
transpose([]) -> [];
transpose([[] | _]) -> [];
transpose(Matrix) -> transpose(Matrix, []).

transpose([], Acc) -> lists:reverse(Acc);
transpose(Matrix, Acc) ->
    {Col, Rest} = extract_column(Matrix),
    transpose(Rest, [Col | Acc]).

extract_column([]) -> {[], []};
extract_column([[H | T] | Rows]) ->
    {RestCol, RestRows} = extract_column(Rows),
    {[H | RestCol], [T | RestRows]}.
```

## Elixir

```elixir
defmodule Solution do
  @spec place_word_in_crossword(board :: [[char]], word :: String.t()) :: boolean
  def place_word_in_crossword(board, word) do
    wlen = String.length(word)
    rev_word = String.reverse(word)

    # check rows
    row_ok? =
      Enum.any?(board, fn row ->
        segs = String.split(Enum.join(row), "#", trim: true)

        Enum.any?(segs, fn seg ->
          String.length(seg) == wlen and
            (match_segment?(seg, word) or match_segment?(seg, rev_word))
        end)
      end)

    if row_ok?, do: true, else check_columns(board, wlen, word, rev_word)
  end

  defp check_columns(board, wlen, word, rev_word) do
    m = length(board)
    n = board |> List.first() |> length()

    Enum.any?(0..(n - 1), fn col ->
      column_chars =
        for r <- 0..(m - 1) do
          Enum.at(Enum.at(board, r), col)
        end

      segs = String.split(Enum.join(column_chars), "#", trim: true)

      Enum.any?(segs, fn seg ->
        String.length(seg) == wlen and
          (match_segment?(seg, word) or match_segment?(seg, rev_word))
      end)
    end)
  end

  defp match_segment?(segment, word) do
    seg_chars = String.graphemes(segment)
    w_chars = String.graphemes(word)

    Enum.zip(seg_chars, w_chars)
    |> Enum.all?(fn {c_seg, c_w} -> c_seg == " " or c_seg == c_w end)
  end
end
```
