# 0037. Sudoku Solver

## Cpp

```cpp
class Solution {
public:
    void solveSudoku(std::vector<std::vector<char>>& board) {
        int row[9] = {0}, col[9] = {0}, box[9] = {0};
        std::vector<std::pair<int,int>> empties;
        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                if (board[i][j] == '.') {
                    empties.emplace_back(i, j);
                } else {
                    int d = board[i][j] - '1';
                    int bit = 1 << d;
                    row[i] |= bit;
                    col[j] |= bit;
                    box[(i/3)*3 + j/3] |= bit;
                }
            }
        }

        std::function<bool(int)> dfs = [&](int pos) -> bool {
            if (pos == (int)empties.size()) return true;

            // Choose cell with minimum candidates (MRV heuristic)
            int bestIdx = -1, minCnt = 10;
            for (int k = pos; k < (int)empties.size(); ++k) {
                auto [i, j] = empties[k];
                int used = row[i] | col[j] | box[(i/3)*3 + j/3];
                int availMask = (~used) & 0x1FF;
                int cnt = __builtin_popcount(availMask);
                if (cnt < minCnt) {
                    minCnt = cnt;
                    bestIdx = k;
                    if (cnt == 1) break;
                }
            }
            std::swap(empties[pos], empties[bestIdx]);
            auto [i, j] = empties[pos];
            int used = row[i] | col[j] | box[(i/3)*3 + j/3];
            int mask = (~used) & 0x1FF;

            while (mask) {
                int bit = mask & -mask;
                int d = __builtin_ctz(bit); // digit index 0..8
                board[i][j] = char('1' + d);
                row[i] |= bit; col[j] |= bit; box[(i/3)*3 + j/3] |= bit;

                if (dfs(pos + 1)) return true;

                row[i] ^= bit; col[j] ^= bit; box[(i/3)*3 + j/3] ^= bit;
                board[i][j] = '.';
                mask &= mask - 1;
            }

            std::swap(empties[pos], empties[bestIdx]); // restore order
            return false;
        };

        dfs(0);
    }
};
```

## Java

```java
class Solution {
    private int[] rows = new int[9];
    private int[] cols = new int[9];
    private int[] boxes = new int[9];
    private java.util.List<Integer> empties = new java.util.ArrayList<>();

    public void solveSudoku(char[][] board) {
        // Initialize masks and empty cells list
        for (int i = 0; i < 9; i++) {
            rows[i] = cols[i] = boxes[i] = 0;
        }
        empties.clear();
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char c = board[i][j];
                if (c == '.') {
                    empties.add(i * 9 + j);
                } else {
                    int d = c - '1';
                    int mask = 1 << d;
                    rows[i] |= mask;
                    cols[j] |= mask;
                    boxes[(i / 3) * 3 + j / 3] |= mask;
                }
            }
        }
        dfs(board, 0);
    }

    private boolean dfs(char[][] board, int idx) {
        if (idx == empties.size()) {
            return true; // solved
        }

        // Choose the cell with minimal possibilities among remaining cells
        int bestIdx = -1;
        int bestMask = 0;
        int minCount = 10;

        for (int k = idx; k < empties.size(); k++) {
            int pos = empties.get(k);
            int i = pos / 9, j = pos % 9;
            int mask = ~(rows[i] | cols[j] | boxes[(i / 3) * 3 + j / 3]) & 0x1FF;
            int cnt = Integer.bitCount(mask);
            if (cnt < minCount) {
                minCount = cnt;
                bestIdx = k;
                bestMask = mask;
                if (cnt == 1) break; // can't get better
            }
        }

        if (bestIdx == -1 || minCount == 0) return false;

        // Swap chosen cell to current index
        java.util.Collections.swap(empties, idx, bestIdx);
        int pos = empties.get(idx);
        int i = pos / 9, j = pos % 9;
        int boxIdx = (i / 3) * 3 + j / 3;

        int mask = bestMask;
        while (mask != 0) {
            int bit = mask & -mask; // lowest set bit
            int d = Integer.numberOfTrailingZeros(bit);
            board[i][j] = (char) ('1' + d);
            rows[i] |= bit;
            cols[j] |= bit;
            boxes[boxIdx] |= bit;

            if (dfs(board, idx + 1)) return true;

            // backtrack
            rows[i] &= ~bit;
            cols[j] &= ~bit;
            boxes[boxIdx] &= ~bit;
            board[i][j] = '.';

            mask ^= bit; // remove used bit
        }

        // Restore order before returning false
        java.util.Collections.swap(empties, idx, bestIdx);
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empties = []

        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c == '.':
                    empties.append((i, j))
                else:
                    bit = 1 << (int(c) - 1)
                    rows[i] |= bit
                    cols[j] |= bit
                    boxes[(i // 3) * 3 + j // 3] |= bit

        FULL_MASK = 0x1FF  # 9 bits set

        def dfs():
            if not empties:
                return True

            # Choose the empty cell with fewest possibilities
            min_idx = -1
            min_cnt = 10
            best_avail = 0
            for idx, (i, j) in enumerate(empties):
                used = rows[i] | cols[j] | boxes[(i // 3) * 3 + j // 3]
                avail = (~used) & FULL_MASK
                cnt = bin(avail).count('1')
                if cnt < min_cnt:
                    min_cnt = cnt
                    min_idx = idx
                    best_avail = avail
                    if cnt == 1:
                        break

            i, j = empties.pop(min_idx)
            bidx = (i // 3) * 3 + j // 3
            used = rows[i] | cols[j] | boxes[bidx]
            avail = (~used) & FULL_MASK

            while avail:
                bit = avail & -avail
                d = bit.bit_length() - 1  # digit index 0-8
                board[i][j] = str(d + 1)
                rows[i] |= bit
                cols[j] |= bit
                boxes[bidx] |= bit

                if dfs():
                    return True

                rows[i] ^= bit
                cols[j] ^= bit
                boxes[bidx] ^= bit
                board[i][j] = '.'

                avail &= avail - 1

            empties.insert(min_idx, (i, j))
            return False

        dfs()
```

## Python3

```python
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empties = []
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c == '.':
                    empties.append((i, j))
                else:
                    bit = 1 << (int(c) - 1)
                    rows[i] |= bit
                    cols[j] |= bit
                    boxes[(i // 3) * 3 + j // 3] |= bit

        FULL_MASK = 0x1FF  # bits 0-8 set

        def dfs() -> bool:
            if not empties:
                return True

            min_idx = -1
            min_mask = 0
            min_cnt = 10
            for idx in range(len(empties)):
                i, j = empties[idx]
                mask = FULL_MASK ^ (rows[i] | cols[j] | boxes[(i // 3) * 3 + j // 3])
                cnt = mask.bit_count()
                if cnt < min_cnt:
                    min_cnt = cnt
                    min_mask = mask
                    min_idx = idx
                    if cnt == 1:
                        break
            if min_cnt == 0:
                return False

            i, j = empties.pop(min_idx)
            b = (i // 3) * 3 + j // 3
            mask = min_mask
            while mask:
                bit = mask & -mask
                d = bit.bit_length() - 1
                board[i][j] = str(d + 1)
                rows[i] |= bit
                cols[j] |= bit
                boxes[b] |= bit

                if dfs():
                    return True

                board[i][j] = '.'
                rows[i] ^= bit
                cols[j] ^= bit
                boxes[b] ^= bit
                mask -= bit

            empties.insert(min_idx, (i, j))
            return False

        dfs()
```

## C

```c
#include <stdbool.h>
#include <string.h>

static char **gboard;
static int rowMask[9];
static int colMask[9];
static int boxMask[9];

typedef struct {
    int r, c;
} Pos;

static Pos empties[81];
static int emptyCnt = 0;

static bool dfs(int idx) {
    if (idx == emptyCnt) return true;
    int r = empties[idx].r;
    int c = empties[idx].c;
    int b = (r / 3) * 3 + (c / 3);
    int used = rowMask[r] | colMask[c] | boxMask[b];
    for (int d = 1; d <= 9; ++d) {
        int bit = 1 << d;
        if ((used & bit) == 0) {
            // place digit
            gboard[r][c] = '0' + d;
            rowMask[r] |= bit;
            colMask[c] |= bit;
            boxMask[b] |= bit;
            if (dfs(idx + 1)) return true;
            // backtrack
            gboard[r][c] = '.';
            rowMask[r] &= ~bit;
            colMask[c] &= ~bit;
            boxMask[b] &= ~bit;
        }
    }
    return false;
}

void solveSudoku(char** board, int boardSize, int* boardColSize) {
    (void)boardSize; // unused, always 9
    (void)boardColSize; // column sizes are all 9

    gboard = board;
    memset(rowMask, 0, sizeof(rowMask));
    memset(colMask, 0, sizeof(colMask));
    memset(boxMask, 0, sizeof(boxMask));
    emptyCnt = 0;

    for (int r = 0; r < 9; ++r) {
        for (int c = 0; c < 9; ++c) {
            char ch = board[r][c];
            if (ch >= '1' && ch <= '9') {
                int d = ch - '0';
                int bit = 1 << d;
                rowMask[r] |= bit;
                colMask[c] |= bit;
                int b = (r / 3) * 3 + (c / 3);
                boxMask[b] |= bit;
            } else {
                empties[emptyCnt].r = r;
                empties[emptyCnt].c = c;
                ++emptyCnt;
            }
        }
    }

    dfs(0);
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private char[][] board;
    private int[] rows = new int[9];
    private int[] cols = new int[9];
    private int[] boxes = new int[9];
    private List<(int r, int c)> empties = new List<(int, int)>();

    public void SolveSudoku(char[][] board) {
        this.board = board;
        for (int i = 0; i < 9; i++) rows[i] = cols[i] = boxes[i] = 0;
        empties.Clear();

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char ch = board[i][j];
                if (ch == '.') {
                    empties.Add((i, j));
                } else {
                    int d = ch - '1';
                    int mask = 1 << d;
                    rows[i] |= mask;
                    cols[j] |= mask;
                    boxes[BoxIndex(i, j)] |= mask;
                }
            }
        }

        DFS(0);
    }

    private int BoxIndex(int r, int c) => (r / 3) * 3 + c / 3;

    private bool DFS(int pos) {
        if (pos == empties.Count) return true;

        // Choose the cell with fewest possibilities
        int bestPos = -1, minCount = 10;
        for (int k = pos; k < empties.Count; k++) {
            var (r, c) = empties[k];
            int used = rows[r] | cols[c] | boxes[BoxIndex(r, c)];
            int cnt = CountBits(~used & 0x1FF);
            if (cnt < minCount) {
                minCount = cnt;
                bestPos = k;
                if (cnt == 1) break;
            }
        }

        // Swap chosen cell to current position
        var tmp = empties[pos];
        empties[pos] = empties[bestPos];
        empties[bestPos] = tmp;

        var (row, col) = empties[pos];
        int usedMask = rows[row] | cols[col] | boxes[BoxIndex(row, col)];

        for (int d = 0; d < 9; d++) {
            int mask = 1 << d;
            if ((usedMask & mask) != 0) continue;

            board[row][col] = (char)('1' + d);
            rows[row] |= mask;
            cols[col] |= mask;
            boxes[BoxIndex(row, col)] |= mask;

            if (DFS(pos + 1)) return true;

            rows[row] ^= mask;
            cols[col] ^= mask;
            boxes[BoxIndex(row, col)] ^= mask;
            board[row][col] = '.';
        }

        // Restore order before backtracking
        tmp = empties[pos];
        empties[pos] = empties[bestPos];
        empties[bestPos] = tmp;

        return false;
    }

    private int CountBits(int x) {
        int cnt = 0;
        while (x != 0) {
            cnt++;
            x &= x - 1;
        }
        return cnt;
    }
}
```

## Javascript

```javascript
/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solveSudoku = function(board) {
    const rows = new Array(9).fill(0);
    const cols = new Array(9).fill(0);
    const boxes = new Array(9).fill(0);
    const empties = [];

    for (let i = 0; i < 9; ++i) {
        for (let j = 0; j < 9; ++j) {
            const ch = board[i][j];
            if (ch === '.') {
                empties.push([i, j]);
            } else {
                const d = ch.charCodeAt(0) - 49; // 0‑based digit
                const mask = 1 << d;
                rows[i] |= mask;
                cols[j] |= mask;
                boxes[Math.floor(i / 3) * 3 + Math.floor(j / 3)] |= mask;
            }
        }
    }

    const bitCount = (x) => {
        let cnt = 0;
        while (x) {
            x &= x - 1;
            ++cnt;
        }
        return cnt;
    };

    const dfs = (k) => {
        if (k === empties.length) return true;

        // choose cell with minimum candidates
        let bestIdx = k, minCnt = 10;
        for (let i = k; i < empties.length; ++i) {
            const [r, c] = empties[i];
            const used = rows[r] | cols[c] | boxes[Math.floor(r / 3) * 3 + Math.floor(c / 3)];
            const avail = (~used) & 0x1FF;
            const cnt = bitCount(avail);
            if (cnt < minCnt) {
                minCnt = cnt;
                bestIdx = i;
                if (cnt === 1) break;
            }
        }

        // swap chosen cell to position k
        [empties[k], empties[bestIdx]] = [empties[bestIdx], empties[k]];
        const [r, c] = empties[k];
        const bIdx = Math.floor(r / 3) * 3 + Math.floor(c / 3);
        let mask = (~(rows[r] | cols[c] | boxes[bIdx])) & 0x1FF;

        while (mask) {
            const bit = mask & -mask;               // lowest set bit
            const d = Math.log2(bit);                // digit index 0‑based
            board[r][c] = String.fromCharCode(49 + d);
            rows[r] |= bit;
            cols[c] |= bit;
            boxes[bIdx] |= bit;

            if (dfs(k + 1)) return true;

            // backtrack
            rows[r] ^= bit;
            cols[c] ^= bit;
            boxes[bIdx] ^= bit;
            board[r][c] = '.';
            mask ^= bit;                             // remove tried bit
        }

        // restore order (optional)
        [empties[k], empties[bestIdx]] = [empties[bestIdx], empties[k]];
        return false;
    };

    dfs(0);
};
```

## Typescript

```typescript
/**
 Do not return anything, modify board in-place instead.
 */
function solveSudoku(board: string[][]): void {
    const ROWS = 9, COLS = 9;
    const rowMask: number[] = new Array(ROWS).fill(0);
    const colMask: number[] = new Array(COLS).fill(0);
    const boxMask: number[] = new Array(9).fill(0);

    // Initialize masks
    for (let r = 0; r < ROWS; ++r) {
        for (let c = 0; c < COLS; ++c) {
            const ch = board[r][c];
            if (ch !== '.') {
                const bit = 1 << (ch.charCodeAt(0) - 49); // '1' -> bit 0
                rowMask[r] |= bit;
                colMask[c] |= bit;
                const b = Math.floor(r / 3) * 3 + Math.floor(c / 3);
                boxMask[b] |= bit;
            }
        }
    }

    function countBits(x: number): number {
        let cnt = 0;
        while (x) { x &= x - 1; ++cnt; }
        return cnt;
    }

    function backtrack(): boolean {
        let minCount = 10;
        let tr = -1, tc = -1;

        // Find empty cell with fewest candidates
        for (let r = 0; r < ROWS; ++r) {
            for (let c = 0; c < COLS; ++c) {
                if (board[r][c] === '.') {
                    const b = Math.floor(r / 3) * 3 + Math.floor(c / 3);
                    const used = rowMask[r] | colMask[c] | boxMask[b];
                    const avail = (~used) & 0x1FF; // only lower 9 bits
                    const cnt = countBits(avail);
                    if (cnt < minCount) {
                        minCount = cnt;
                        tr = r; tc = c;
                        if (cnt === 1) break;
                    }
                }
            }
            if (minCount === 1) break;
        }

        // No empty cells left -> solved
        if (tr === -1) return true;

        const bIdx = Math.floor(tr / 3) * 3 + Math.floor(tc / 3);
        let availMask = (~(rowMask[tr] | colMask[tc] | boxMask[bIdx])) & 0x1FF;

        while (availMask) {
            const bit = availMask & -availMask; // lowest set bit
            const digit = Math.log2(bit); // 0..8
            board[tr][tc] = String.fromCharCode(49 + digit);
            rowMask[tr] |= bit;
            colMask[tc] |= bit;
            boxMask[bIdx] |= bit;

            if (backtrack()) return true;

            // undo
            board[tr][tc] = '.';
            rowMask[tr] ^= bit;
            colMask[tc] ^= bit;
            boxMask[bIdx] ^= bit;

            availMask &= availMask - 1; // remove used bit
        }

        return false;
    }

    backtrack();
}
```

## Php

```php
class Solution {
    /**
     * @param String[][] $board
     * @return NULL
     */
    function solveSudoku(&$board) {
        $rows = array_fill(0, 9, 0);
        $cols = array_fill(0, 9, 0);
        $boxes = array_fill(0, 9, 0);
        $empties = [];

        for ($i = 0; $i < 9; $i++) {
            for ($j = 0; $j < 9; $j++) {
                $c = $board[$i][$j];
                if ($c === '.') {
                    $empties[] = [$i, $j];
                } else {
                    $d = intval($c);
                    $bit = 1 << ($d - 1);
                    $rows[$i] |= $bit;
                    $cols[$j] |= $bit;
                    $boxIdx = intdiv($i, 3) * 3 + intdiv($j, 3);
                    $boxes[$boxIdx] |= $bit;
                }
            }
        }

        $dfs = function ($pos) use (&$board, &$rows, &$cols, &$boxes, &$empties, &$dfs) {
            if ($pos == count($empties)) {
                return true;
            }
            [$r, $c] = $empties[$pos];
            $boxIdx = intdiv($r, 3) * 3 + intdiv($c, 3);
            $available = (~($rows[$r] | $cols[$c] | $boxes[$boxIdx])) & 0x1FF;

            while ($available) {
                $bit = $available & -$available; // lowest set bit
                $d = 1;
                while ((($bit >> ($d - 1)) & 1) == 0) {
                    $d++;
                }

                $board[$r][$c] = (string)$d;
                $rows[$r] |= $bit;
                $cols[$c] |= $bit;
                $boxes[$boxIdx] |= $bit;

                if ($dfs($pos + 1)) {
                    return true;
                }

                $board[$r][$c] = '.';
                $rows[$r] ^= $bit;
                $cols[$c] ^= $bit;
                $boxes[$boxIdx] ^= $bit;

                $available &= ~$bit; // remove used bit
            }
            return false;
        };

        $dfs(0);
    }
}
```

## Swift

```swift
class Solution {
    func solveSudoku(_ board: inout [[Character]]) {
        var rows = [Int](repeating: 0, count: 9)
        var cols = [Int](repeating: 0, count: 9)
        var boxes = [Int](repeating: 0, count: 9)
        var empties = [(Int, Int)]()
        
        for i in 0..<9 {
            for j in 0..<9 {
                let ch = board[i][j]
                if ch == "." {
                    empties.append((i, j))
                } else {
                    let digit = Int(ch.unicodeScalars.first!.value - 48) // 1...9
                    let bit = 1 << (digit - 1)
                    rows[i] |= bit
                    cols[j] |= bit
                    boxes[(i / 3) * 3 + j / 3] |= bit
                }
            }
        }
        
        func backtrack(_ idx: Int) -> Bool {
            if idx == empties.count { return true }
            let (r, c) = empties[idx]
            let b = (r / 3) * 3 + c / 3
            var avail = (~(rows[r] | cols[c] | boxes[b])) & 0x1FF
            while avail != 0 {
                let bit = avail & -avail
                let d = bit.trailingZeroBitCount // 0...8 representing digit-1
                board[r][c] = Character(UnicodeScalar(UInt32(d + 1 + 48))!)
                rows[r] |= bit
                cols[c] |= bit
                boxes[b] |= bit
                if backtrack(idx + 1) { return true }
                rows[r] ^= bit
                cols[c] ^= bit
                boxes[b] ^= bit
                board[r][c] = "."
                avail &= ~bit
            }
            return false
        }
        
        _ = backtrack(0)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun solveSudoku(board: Array<CharArray>) {
        val rows = IntArray(9)
        val cols = IntArray(9)
        val boxes = IntArray(9)
        val empties = mutableListOf<Pair<Int, Int>>()

        for (i in 0 until 9) {
            for (j in 0 until 9) {
                val c = board[i][j]
                if (c == '.') {
                    empties.add(Pair(i, j))
                } else {
                    val d = c - '1'
                    val mask = 1 shl d
                    rows[i] = rows[i] or mask
                    cols[j] = cols[j] or mask
                    boxes[(i / 3) * 3 + j / 3] = boxes[(i / 3) * 3 + j / 3] or mask
                }
            }
        }

        fun dfs(pos: Int): Boolean {
            if (pos == empties.size) return true
            val (i, j) = empties[pos]
            val boxIdx = (i / 3) * 3 + j / 3
            var used = rows[i] or cols[j] or boxes[boxIdx]
            var candidates = (~used) and 0x1FF // keep only lower 9 bits

            while (candidates != 0) {
                val bit = candidates and -candidates
                val d = Integer.numberOfTrailingZeros(bit)
                // place digit
                board[i][j] = ('1' + d)
                rows[i] = rows[i] or bit
                cols[j] = cols[j] or bit
                boxes[boxIdx] = boxes[boxIdx] or bit

                if (dfs(pos + 1)) return true

                // backtrack
                board[i][j] = '.'
                rows[i] = rows[i] xor bit
                cols[j] = cols[j] xor bit
                boxes[boxIdx] = boxes[boxIdx] xor bit

                candidates -= bit
            }
            return false
        }

        dfs(0)
    }
}
```

## Dart

```dart
class Solution {
  void solveSudoku(List<List<String>> board) {
    List<int> rows = List.filled(9, 0);
    List<int> cols = List.filled(9, 0);
    List<int> boxes = List.filled(9, 0);
    List<int> empties = [];

    for (int i = 0; i < 9; i++) {
      for (int j = 0; j < 9; j++) {
        String ch = board[i][j];
        if (ch == '.') {
          empties.add(i * 9 + j);
        } else {
          int d = int.parse(ch) - 1;
          int mask = 1 << d;
          rows[i] |= mask;
          cols[j] |= mask;
          boxes[(i ~/ 3) * 3 + (j ~/ 3)] |= mask;
        }
      }
    }

    bool dfs(int idx) {
      if (idx == empties.length) return true;

      // Choose the cell with minimal candidates
      int bestIdx = -1;
      int minCount = 10;
      for (int k = idx; k < empties.length; k++) {
        int pos = empties[k];
        int r = pos ~/ 9;
        int c = pos % 9;
        int used = rows[r] | cols[c] | boxes[(r ~/ 3) * 3 + (c ~/ 3)];
        int avail = (~used) & 0x1FF;
        int cnt = _bitCount(avail);
        if (cnt < minCount) {
          minCount = cnt;
          bestIdx = k;
          if (cnt == 1) break;
        }
      }

      // Swap to process this cell now
      int tmp = empties[idx];
      empties[idx] = empties[bestIdx];
      empties[bestIdx] = tmp;

      int pos = empties[idx];
      int r = pos ~/ 9;
      int c = pos % 9;
      int used = rows[r] | cols[c] | boxes[(r ~/ 3) * 3 + (c ~/ 3)];
      int avail = (~used) & 0x1FF;

      while (avail != 0) {
        int bit = avail & -avail;
        int d = bit.bitLength - 1; // digit index 0..8
        rows[r] |= bit;
        cols[c] |= bit;
        boxes[(r ~/ 3) * 3 + (c ~/ 3)] |= bit;
        board[r][c] = String.fromCharCode('1'.codeUnitAt(0) + d);
        if (dfs(idx + 1)) return true;
        rows[r] ^= bit;
        cols[c] ^= bit;
        boxes[(r ~/ 3) * 3 + (c ~/ 3)] ^= bit;
        board[r][c] = '.';
        avail &= ~bit;
      }

      // Restore swap before backtracking
      tmp = empties[idx];
      empties[idx] = empties[bestIdx];
      empties[bestIdx] = tmp;

      return false;
    }

    dfs(0);
  }

  int _bitCount(int n) {
    int cnt = 0;
    while (n != 0) {
      n &= n - 1;
      cnt++;
    }
    return cnt;
  }
}
```

## Golang

```go
import "math/bits"

func solveSudoku(board [][]byte) {
	rows := [9]int{}
	cols := [9]int{}
	boxes := [9]int{}

	type pos struct{ r, c int }
	empties := []pos{}

	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			if board[i][j] == '.' {
				empties = append(empties, pos{i, j})
			} else {
				d := int(board[i][j] - '1')
				mask := 1 << d
				rows[i] |= mask
				cols[j] |= mask
				boxIdx := (i/3)*3 + j/3
				boxes[boxIdx] |= mask
			}
		}
	}

	var dfs func(int) bool
	dfs = func(k int) bool {
		if k == len(empties) {
			return true
		}
		r, c := empties[k].r, empties[k].c
		boxIdx := (r/3)*3 + c/3
		available := ^(rows[r] | cols[c] | boxes[boxIdx]) & 0x1FF

		for m := available; m != 0; m &= m - 1 {
			bit := m & -m
			d := bits.TrailingZeros(uint(bit))

			rows[r] |= bit
			cols[c] |= bit
			boxes[boxIdx] |= bit
			board[r][c] = byte('1' + d)

			if dfs(k + 1) {
				return true
			}

			rows[r] &^= bit
			cols[c] &^= bit
			boxes[boxIdx] &^= bit
			board[r][c] = '.'
		}
		return false
	}

	dfs(0)
}
```

## Ruby

```ruby
def solve_sudoku(board)
  rows = Array.new(9, 0)
  cols = Array.new(9, 0)
  boxes = Array.new(9, 0)
  empties = []

  (0...9).each do |i|
    (0...9).each do |j|
      ch = board[i][j]
      if ch == '.'
        empties << [i, j]
      else
        d = ch.ord - '1'.ord
        bit = 1 << d
        rows[i] |= bit
        cols[j] |= bit
        boxes[(i / 3) * 3 + (j / 3)] |= bit
      end
    end
  end

  dfs = nil
  dfs = lambda do |idx|
    return true if idx == empties.size
    i, j = empties[idx]
    b_idx = (i / 3) * 3 + (j / 3)
    (1..9).each do |num|
      bit = 1 << (num - 1)
      next if (rows[i] & bit) != 0 || (cols[j] & bit) != 0 || (boxes[b_idx] & bit) != 0
      board[i][j] = num.to_s
      rows[i] |= bit
      cols[j] |= bit
      boxes[b_idx] |= bit
      return true if dfs.call(idx + 1)
      board[i][j] = '.'
      rows[i] ^= bit
      cols[j] ^= bit
      boxes[b_idx] ^= bit
    end
    false
  end

  dfs.call(0)
end
```

## Scala

```scala
object Solution {
  def solveSudoku(board: Array[Array[Char]]): Unit = {
    val rows = Array.fill(9)(0)
    val cols = Array.fill(9)(0)
    val boxes = Array.fill(9)(0)
    import scala.collection.mutable.ArrayBuffer
    val empties = new ArrayBuffer[(Int, Int)]()

    for (i <- 0 until 9; j <- 0 until 9) {
      board(i)(j) match {
        case c if c != '.' =>
          val d = c - '1'
          val bit = 1 << d
          rows(i) |= bit
          cols(j) |= bit
          boxes((i / 3) * 3 + j / 3) |= bit
        case _ => empties.append((i, j))
      }
    }

    def dfs(pos: Int): Boolean = {
      if (pos == empties.length) return true
      val (r, c) = empties(pos)
      val used = rows(r) | cols(c) | boxes((r / 3) * 3 + c / 3)
      var mask = (~used) & 0x1FF // lower 9 bits

      while (mask != 0) {
        val bit = mask & -mask
        val d = Integer.numberOfTrailingZeros(bit)
        board(r)(c) = ('1' + d).toChar
        rows(r) |= bit
        cols(c) |= bit
        boxes((r / 3) * 3 + c / 3) |= bit

        if (dfs(pos + 1)) return true

        board(r)(c) = '.'
        rows(r) ^= bit
        cols(c) ^= bit
        boxes((r / 3) * 3 + c / 3) ^= bit

        mask ^= bit
      }
      false
    }

    dfs(0)
  }
}
```

## Rust

```rust
impl Solution {
    pub fn solve_sudoku(board: &mut Vec<Vec<char>>) {
        const FULL_MASK: u16 = 0x1FF; // lower 9 bits set
        let mut rows = [0u16; 9];
        let mut cols = [0u16; 9];
        let mut boxes = [0u16; 9];
        let mut empties: Vec<(usize, usize)> = Vec::new();

        for i in 0..9 {
            for j in 0..9 {
                let ch = board[i][j];
                if ch != '.' {
                    let d = (ch as u8 - b'1') as usize;
                    let mask: u16 = 1 << d;
                    rows[i] |= mask;
                    cols[j] |= mask;
                    boxes[(i / 3) * 3 + j / 3] |= mask;
                } else {
                    empties.push((i, j));
                }
            }
        }

        fn dfs(
            idx: usize,
            board: &mut Vec<Vec<char>>,
            empties: &Vec<(usize, usize)>,
            rows: &mut [u16; 9],
            cols: &mut [u16; 9],
            boxes: &mut [u16; 9],
        ) -> bool {
            if idx == empties.len() {
                return true;
            }
            let (r, c) = empties[idx];
            let b_idx = (r / 3) * 3 + c / 3;
            let used = rows[r] | cols[c] | boxes[b_idx];
            let mut avail = (!used) & 0x1FF; // only lower 9 bits

            while avail != 0 {
                let bit = avail & (!avail + 1); // lowest set bit
                let d = bit.trailing_zeros() as usize; // digit index 0..8

                // place digit
                board[r][c] = (b'1' + d as u8) as char;
                rows[r] |= bit;
                cols[c] |= bit;
                boxes[b_idx] |= bit;

                if dfs(idx + 1, board, empties, rows, cols, boxes) {
                    return true;
                }

                // undo
                rows[r] &= !bit;
                cols[c] &= !bit;
                boxes[b_idx] &= !bit;
                board[r][c] = '.';

                avail ^= bit; // remove this bit
            }
            false
        }

        dfs(0, board, &empties, &mut rows, &mut cols, &mut boxes);
    }
}
```
