# 0782. Transform to Chessboard

## Cpp

```cpp
class Solution {
public:
    int movesToChessboard(vector<vector<int>>& board) {
        int n = board.size();
        // Validate the board can be transformed
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if ((board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]) != 0)
                    return -1;
            }
        }
        
        auto getMoves = [&](const vector<int>& line) -> int {
            int ones = 0, diff = 0;
            for (int i = 0; i < n; ++i) {
                ones += line[i];
                if (line[i] != (i & 1)) ++diff; // compare with pattern starting with 0
            }
            if (abs(ones - n / 2) > (n & 1)) return INT_MAX;
            if (n % 2 == 0) {
                return min(diff, n - diff) / 2;
            } else {
                // For odd n, the pattern must start with the majority value
                if (ones > n / 2) return (n - diff) / 2;
                else return diff / 2;
            }
        };
        
        vector<int> rowLine(n), colLine(n);
        for (int i = 0; i < n; ++i) {
            rowLine[i] = board[i][0];
            colLine[i] = board[0][i];
        }
        
        int rowMoves = getMoves(rowLine);
        int colMoves = getMoves(colLine);
        if (rowMoves == INT_MAX || colMoves == INT_MAX) return -1;
        return rowMoves + colMoves;
    }
};
```

## Java

```java
class Solution {
    public int movesToChessboard(int[][] board) {
        int n = board.length;
        // Validate the board can be transformed
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if ((board[i][j] ^ board[0][j] ^ board[i][0] ^ board[0][0]) != 0) {
                    return -1;
                }
            }
        }

        int rowSum = 0, colSum = 0;
        for (int i = 0; i < n; ++i) {
            rowSum += board[0][i];
            colSum += board[i][0];
        }

        if (n % 2 == 0) {
            if (rowSum != n / 2 || colSum != n / 2) return -1;
        } else {
            if (!(rowSum == n / 2 || rowSum == n / 2 + 1)) return -1;
            if (!(colSum == n / 2 || colSum == n / 2 + 1)) return -1;
        }

        int rowSwap = 0, colSwap = 0;
        for (int i = 0; i < n; ++i) {
            if (board[0][i] == i % 2) rowSwap++;
            if (board[i][0] == i % 2) colSwap++;
        }

        if (n % 2 == 0) {
            rowSwap = Math.min(rowSwap, n - rowSwap);
            colSwap = Math.min(colSwap, n - colSwap);
        } else {
            // For odd n, the number of swaps must match the majority value
            if (rowSwap % 2 == 1) rowSwap = n - rowSwap;
            if (colSwap % 2 == 1) colSwap = n - colSwap;
        }

        return (rowSwap + colSwap) / 2;
    }
}
```

## Python

```python
class Solution(object):
    def movesToChessboard(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        # helper to convert list of bits to integer mask
        def list_to_mask(lst):
            m = 0
            for b in lst:
                m = (m << 1) | b
            return m

        # row masks
        row_masks = [list_to_mask(row) for row in board]
        first_row_mask = row_masks[0]
        rev_row_mask = ((1 << n) - 1) ^ first_row_mask

        cnt_first_row = 0
        for mask in row_masks:
            if mask != first_row_mask and mask != rev_row_mask:
                return -1
            if mask == first_row_mask:
                cnt_first_row += 1

        # column masks
        col_masks = []
        for j in range(n):
            col = [board[i][j] for i in range(n)]
            col_masks.append(list_to_mask(col))
        first_col_mask = col_masks[0]
        rev_col_mask = ((1 << n) - 1) ^ first_col_mask

        cnt_first_col = 0
        for mask in col_masks:
            if mask != first_col_mask and mask != rev_col_mask:
                return -1
            if mask == first_col_mask:
                cnt_first_col += 1

        # check count constraints
        def valid_counts(cnt):
            if n % 2 == 0:
                return cnt == n // 2
            else:
                return cnt == n // 2 or cnt == (n // 2) + 1

        if not (valid_counts(cnt_first_row) and valid_counts(cnt_first_col)):
            return -1

        # function to compute minimal swaps for a list of masks given desired start mask at index 0
        def min_swaps(masks, start_mask):
            rev = ((1 << n) - 1) ^ start_mask
            mismatches = 0
            for i, m in enumerate(masks):
                expected = start_mask if (i % 2 == 0) else rev
                if m != expected:
                    mismatches += 1
            return mismatches // 2

        # row swaps
        if n % 2 == 0:
            row_swaps = min(min_swaps(row_masks, first_row_mask),
                            min_swaps(row_masks, rev_row_mask))
        else:
            # majority mask must be at even positions
            if cnt_first_row > n // 2:
                row_swaps = min_swaps(row_masks, first_row_mask)
            else:
                row_swaps = min_swaps(row_masks, rev_row_mask)

        # column swaps
        if n % 2 == 0:
            col_swaps = min(min_swaps(col_masks, first_col_mask),
                            min_swaps(col_masks, rev_col_mask))
        else:
            if cnt_first_col > n // 2:
                col_swaps = min_swaps(col_masks, first_col_mask)
            else:
                col_swaps = min_swaps(col_masks, rev_col_mask)

        return row_swaps + col_swaps
```

## Python3

```python
class Solution:
    def movesToChessboard(self, board):
        from typing import List
        n = len(board)

        # Build masks for first row and first column
        rowMask = 0
        for j in range(n):
            rowMask |= (board[0][j] << j)
        colMask = 0
        for i in range(n):
            colMask |= (board[i][0] << i)

        revRowMask = ((1 << n) - 1) ^ rowMask
        revColMask = ((1 << n) - 1) ^ colMask

        rowCnt = 0
        for i in range(n):
            cur = 0
            for j in range(n):
                cur |= (board[i][j] << j)
            if cur == rowMask:
                rowCnt += 1
            elif cur != revRowMask:
                return -1

        colCnt = 0
        for j in range(n):
            cur = 0
            for i in range(n):
                cur |= (board[i][j] << i)
            if cur == colMask:
                colCnt += 1
            elif cur != revColMask:
                return -1

        def moves(mask, cnt):
            ones = bin(mask).count('1')
            if n % 2 == 0:
                # must have exactly half ones and half rows of each type
                if ones != n // 2 or cnt != n // 2:
                    return -1
                pattern0 = int('01' * (n // 2), 2)   # start with 0
                pattern1 = int('10' * (n // 2), 2)   # start with 1
                diff0 = bin(mask ^ pattern0).count('1')
                diff1 = bin(mask ^ pattern1).count('1')
                return min(diff0, diff1) // 2
            else:
                # ones count must be floor or ceil(n/2)
                if not (ones == n // 2 or ones == n // 2 + 1):
                    return -1
                if not (cnt == n // 2 or cnt == n // 2 + 1):
                    return -1
                # majority determines starting bit
                if ones > n // 2:
                    pattern = int('10' * (n // 2) + '1', 2)   # start with 1
                else:
                    pattern = int('01' * (n // 2) + '0', 2)   # start with 0
                diff = bin(mask ^ pattern).count('1')
                return diff // 2

        rowMoves = moves(rowMask, rowCnt)
        if rowMoves == -1:
            return -1
        colMoves = moves(colMask, colCnt)
        if colMoves == -1:
            return -1
        return rowMoves + colMoves
```

## C

```c
int getSwaps(int n, int cntSame, int *type) {
    int mism0 = 0;
    for (int i = 0; i < n; ++i) {
        if (type[i] != (i % 2)) mism0++;
    }
    if (n % 2 == 0) {
        int mism1 = 0;
        for (int i = 0; i < n; ++i) {
            if (type[i] != ((i + 1) % 2)) mism1++;
        }
        return (mism0 < mism1 ? mism0 : mism1) / 2;
    } else {
        if (!(cntSame == n / 2 || cntSame == n / 2 + 1)) return -1;
        int start = (cntSame > n / 2) ? 0 : 1; // majority type should be at even indices
        int mism = 0;
        for (int i = 0; i < n; ++i) {
            if (type[i] != ((i + start) % 2)) mism++;
        }
        return mism / 2;
    }
}

int movesToChessboard(int** board, int boardSize, int* boardColSize){
    int n = boardSize;
    int allOnesMask = (1 << n) - 1;

    /* rows */
    int firstRowMask = 0;
    for (int j = 0; j < n; ++j)
        if (board[0][j]) firstRowMask |= (1 << j);
    int complementRowMask = firstRowMask ^ allOnesMask;

    int rowType[31];
    int cntSameRows = 0;
    for (int i = 0; i < n; ++i) {
        int mask = 0;
        for (int j = 0; j < n; ++j)
            if (board[i][j]) mask |= (1 << j);
        if (mask == firstRowMask) {
            rowType[i] = 0;
            cntSameRows++;
        } else if (mask == complementRowMask) {
            rowType[i] = 1;
        } else {
            return -1;
        }
    }

    /* columns */
    int firstColMask = 0;
    for (int i = 0; i < n; ++i)
        if (board[i][0]) firstColMask |= (1 << i);
    int complementColMask = firstColMask ^ allOnesMask;

    int colType[31];
    int cntSameCols = 0;
    for (int j = 0; j < n; ++j) {
        int mask = 0;
        for (int i = 0; i < n; ++i)
            if (board[i][j]) mask |= (1 << i);
        if (mask == firstColMask) {
            colType[j] = 0;
            cntSameCols++;
        } else if (mask == complementColMask) {
            colType[j] = 1;
        } else {
            return -1;
        }
    }

    int rowSwaps = getSwaps(n, cntSameRows, rowType);
    if (rowSwaps < 0) return -1;
    int colSwaps = getSwaps(n, cntSameCols, colType);
    if (colSwaps < 0) return -1;

    return rowSwaps + colSwaps;
}
```

## Csharp

```csharp
public class Solution {
    public int MovesToChessboard(int[][] board) {
        int n = board.Length;
        // Validate rows: each row must be same as first row or its inverse
        for (int i = 0; i < n; i++) {
            int diff = board[i][0] ^ board[0][0];
            for (int j = 0; j < n; j++) {
                if ((board[i][j] ^ board[0][j]) != diff) return -1;
            }
        }
        // Validate columns: each column must be same as first column or its inverse
        for (int j = 0; j < n; j++) {
            int diff = board[0][j] ^ board[0][0];
            for (int i = 0; i < n; i++) {
                if ((board[i][j] ^ board[i][0]) != diff) return -1;
            }
        }

        // Count rows that match the first row pattern
        int rowsSame = 0;
        for (int i = 0; i < n; i++) {
            if (board[i][0] == board[0][0]) rowsSame++;
        }
        // Count columns that match the first column pattern
        int colsSame = 0;
        for (int j = 0; j < n; j++) {
            if (board[0][j] == board[0][0]) colsSame++;
        }

        // For a valid chessboard, counts must be balanced
        if (Math.Abs(rowsSame - n / 2) > (n % 2)) return -1;
        if (Math.Abs(colsSame - n / 2) > (n % 2)) return -1;

        int[] rowTypes = new int[n];
        for (int i = 0; i < n; i++) {
            rowTypes[i] = (board[i][0] == board[0][0]) ? 0 : 1;
        }
        int[] colTypes = new int[n];
        for (int j = 0; j < n; j++) {
            colTypes[j] = (board[0][j] == board[0][0]) ? 0 : 1;
        }

        int rowSwaps = GetMinSwaps(rowTypes, n);
        int colSwaps = GetMinSwaps(colTypes, n);

        return rowSwaps + colSwaps;
    }

    private int GetMinSwaps(int[] types, int n) {
        int mismatches = 0;
        for (int i = 0; i < n; i++) {
            if ((i % 2) != types[i]) mismatches++;
        }
        if (n % 2 == 0) {
            return Math.Min(mismatches, n - mismatches) / 2;
        } else {
            // For odd n, the pattern must start with the majority element
            if (mismatches % 2 == 0) return mismatches / 2;
            return (n - mismatches) / 2;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} board
 * @return {number}
 */
var movesToChessboard = function(board) {
    const n = board.length;
    // Check if transformation is possible using parity condition
    for (let i = 0; i < n; ++i) {
        for (let j = 0; j < n; ++j) {
            if ((board[i][j] ^ board[0][j] ^ board[i][0] ^ board[0][0]) !== 0) {
                return -1;
            }
        }
    }

    // Count ones in first row and first column
    let rowOnes = 0, colOnes = 0;
    for (let i = 0; i < n; ++i) {
        rowOnes += board[0][i];
        colOnes += board[i][0];
    }

    const half = Math.floor(n / 2);
    if (n % 2 === 0) {
        if (rowOnes !== half || colOnes !== half) return -1;
    } else {
        if (!(rowOnes === half || rowOnes === half + 1)) return -1;
        if (!(colOnes === half || colOnes === half + 1)) return -1;
    }

    // Compute mismatches for rows and columns against pattern starting with 0
    let rowSwap = 0, colSwap = 0;
    for (let i = 0; i < n; ++i) {
        if (board[i][0] !== (i % 2)) rowSwap++;
        if (board[0][i] !== (i % 2)) colSwap++;
    }

    let movesRow, movesCol;
    if (n % 2 === 0) {
        movesRow = Math.min(rowSwap, n - rowSwap) / 2;
        movesCol = Math.min(colSwap, n - colSwap) / 2;
    } else {
        // For odd n, pattern is forced by majority count
        if (rowOnes > half) {
            movesRow = (n - rowSwap) / 2; // start with 1
        } else {
            movesRow = rowSwap / 2;       // start with 0
        }
        if (colOnes > half) {
            movesCol = (n - colSwap) / 2;
        } else {
            movesCol = colSwap / 2;
        }
    }

    return movesRow + movesCol;
};
```

## Typescript

```typescript
function movesToChessboard(board: number[][]): number {
    const n = board.length;
    // Validate the board pattern
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if ((board[i][j] ^ board[0][j] ^ board[i][0] ^ board[0][0]) !== 0) {
                return -1;
            }
        }
    }

    const rowSum = board[0].reduce((a, b) => a + b, 0);
    let colSum = 0;
    for (let i = 0; i < n; i++) colSum += board[i][0];

    if (n % 2 === 0) {
        if (rowSum !== n / 2 || colSum !== n / 2) return -1;
    } else {
        const halfLow = Math.floor(n / 2);
        const halfHigh = Math.ceil(n / 2);
        if (rowSum !== halfLow && rowSum !== halfHigh) return -1;
        if (colSum !== halfLow && colSum !== halfHigh) return -1;
    }

    const firstCol = board.map(row => row[0]);
    const firstRow = board[0].slice();

    const getSwaps = (arr: number[], ones: number): number => {
        const len = arr.length;
        let mismatchStartWithZero = 0;
        for (let i = 0; i < len; i++) {
            if (arr[i] !== (i % 2)) mismatchStartWithZero++;
        }
        if (len % 2 === 0) {
            return Math.min(mismatchStartWithZero, len - mismatchStartWithZero) / 2;
        } else {
            const targetStart = ones > Math.floor(len / 2) ? 1 : 0;
            let mismatches = 0;
            for (let i = 0; i < len; i++) {
                if (arr[i] !== ((i + targetStart) % 2)) mismatches++;
            }
            return mismatches / 2;
        }
    };

    const rowSwaps = getSwaps(firstCol, colSum);
    const colSwaps = getSwaps(firstRow, rowSum);

    return rowSwaps + colSwaps;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $board
     * @return Integer
     */
    function movesToChessboard($board) {
        $n = count($board);
        // build masks for first row and first column
        $rowMask = 0;
        $colMask = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($board[0][$i] == 1) {
                $rowMask |= (1 << $i);
            }
            if ($board[$i][0] == 1) {
                $colMask |= (1 << $i);
            }
        }

        $reverseRowMask = ((1 << $n) - 1) ^ $rowMask;
        $reverseColMask = ((1 << $n) - 1) ^ $colMask;

        $rowCnt = 0;
        $colCnt = 0;

        for ($i = 0; $i < $n; $i++) {
            // current row mask
            $curRowMask = 0;
            for ($j = 0; $j < $n; $j++) {
                if ($board[$i][$j] == 1) {
                    $curRowMask |= (1 << $j);
                }
            }
            if ($curRowMask === $rowMask) {
                $rowCnt++;
            } elseif ($curRowMask !== $reverseRowMask) {
                return -1;
            }

            // current column mask
            $curColMask = 0;
            for ($j = 0; $j < $n; $j++) {
                if ($board[$j][$i] == 1) {
                    $curColMask |= (1 << $j);
                }
            }
            if ($curColMask === $colMask) {
                $colCnt++;
            } elseif ($curColMask !== $reverseColMask) {
                return -1;
            }
        }

        // validate counts
        if (abs($rowCnt - intdiv($n, 2)) > $n % 2) {
            return -1;
        }
        if (abs($colCnt - intdiv($n, 2)) > $n % 2) {
            return -1;
        }

        // helper for popcount
        $bitCount = function ($x) {
            $cnt = 0;
            while ($x) {
                $cnt += $x & 1;
                $x >>= 1;
            }
            return $cnt;
        };

        // compute swaps needed for a mask (rows or columns)
        $getSwaps = function ($mask, $n) use (&$bitCount) {
            $ones = $bitCount($mask);
            // pattern where index 0 is 0, i.e., bits set at odd positions
            $pattern0 = 0;
            for ($i = 0; $i < $n; $i++) {
                if (($i & 1) == 1) {
                    $pattern0 |= (1 << $i);
                }
            }
            $pattern1 = ((1 << $n) - 1) ^ $pattern0; // complement within n bits

            if ($n % 2 == 0) {
                $cnt0 = $bitCount($mask ^ $pattern0);
                $cnt1 = $bitCount($mask ^ $pattern1);
                return min($cnt0, $cnt1) / 2;
            } else {
                // majority decides which pattern to use
                if ($ones * 2 < $n) { // more zeros, start with 0 at index 0
                    $cnt = $bitCount($mask ^ $pattern0);
                } else { // more ones, start with 1 at index 0
                    $cnt = $bitCount($mask ^ $pattern1);
                }
                return $cnt / 2;
            }
        };

        // swaps for rows are based on column mask, and vice versa
        $rowSwaps = $getSwaps($colMask, $n);
        $colSwaps = $getSwaps($rowMask, $n);

        return $rowSwaps + $colSwaps;
    }
}
```

## Swift

```swift
class Solution {
    func movesToChessboard(_ board: [[Int]]) -> Int {
        let n = board.count
        // Build masks for rows and columns
        var rowMask0 = 0
        for j in 0..<n {
            if board[0][j] == 1 {
                rowMask0 |= (1 << j)
            }
        }
        var colMask0 = 0
        for i in 0..<n {
            if board[i][0] == 1 {
                colMask0 |= (1 << i)
            }
        }
        let fullMask = (1 << n) - 1
        let revRowMask = fullMask ^ rowMask0
        let revColMask = fullMask ^ colMask0
        
        var rowVals = [Int]()
        var cntRowsSame = 0
        for i in 0..<n {
            var mask = 0
            for j in 0..<n {
                if board[i][j] == 1 {
                    mask |= (1 << j)
                }
            }
            if mask != rowMask0 && mask != revRowMask { return -1 }
            if mask == rowMask0 {
                cntRowsSame += 1
                rowVals.append(0)
            } else {
                rowVals.append(1)
            }
        }
        
        var colVals = [Int]()
        var cntColsSame = 0
        for j in 0..<n {
            var mask = 0
            for i in 0..<n {
                if board[i][j] == 1 {
                    mask |= (1 << i)
                }
            }
            if mask != colMask0 && mask != revColMask { return -1 }
            if mask == colMask0 {
                cntColsSame += 1
                colVals.append(0)
            } else {
                colVals.append(1)
            }
        }
        
        let half = n / 2
        // Validate counts
        if n % 2 == 0 {
            if cntRowsSame != half || cntColsSame != half { return -1 }
        } else {
            if !(cntRowsSame == half || cntRowsSame == half + 1) { return -1 }
            if !(cntColsSame == half || cntColsSame == half + 1) { return -1 }
        }
        
        func minSwaps(_ vals: [Int]) -> Int {
            let n = vals.count
            var swaps = Int.max
            if n % 2 == 0 {
                // pattern starting with 0
                var mism0 = 0
                for i in 0..<n {
                    if vals[i] != (i % 2) { mism0 += 1 }
                }
                // pattern starting with 1
                var mism1 = 0
                for i in 0..<n {
                    if vals[i] != ((i + 1) % 2) { mism1 += 1 }
                }
                swaps = min(mism0, mism1) / 2
            } else {
                // Determine which start matches the majority count
                let ones = vals.reduce(0, +)
                let targetOnesStart0 = n / 2   // floor
                var mism = 0
                if ones == targetOnesStart0 {
                    // start with 0 pattern
                    for i in 0..<n {
                        if vals[i] != (i % 2) { mism += 1 }
                    }
                } else {
                    // start with 1 pattern
                    for i in 0..<n {
                        if vals[i] != ((i + 1) % 2) { mism += 1 }
                    }
                }
                swaps = mism / 2
            }
            return swaps
        }
        
        let rowSwaps = minSwaps(rowVals)
        let colSwaps = minSwaps(colVals)
        return rowSwaps + colSwaps
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun movesToChessboard(board: Array<IntArray>): Int {
        val n = board.size
        var rowMask = 0
        for (j in 0 until n) {
            rowMask = (rowMask shl 1) or board[0][j]
        }
        val reverseRowMask = ((1 shl n) - 1) xor rowMask

        var colMask = 0
        for (i in 0 until n) {
            colMask = (colMask shl 1) or board[i][0]
        }
        val reverseColMask = ((1 shl n) - 1) xor colMask

        val rowsPattern = IntArray(n)
        var rowCntMask = 0
        for (i in 0 until n) {
            var curMask = 0
            for (j in 0 until n) {
                curMask = (curMask shl 1) or board[i][j]
            }
            if (curMask != rowMask && curMask != reverseRowMask) return -1
            if (curMask == rowMask) {
                rowsPattern[i] = 0
                rowCntMask++
            } else {
                rowsPattern[i] = 1
            }
        }

        val colsPattern = IntArray(n)
        var colCntMask = 0
        for (j in 0 until n) {
            var curMask = 0
            for (i in 0 until n) {
                curMask = (curMask shl 1) or board[i][j]
            }
            if (curMask != colMask && curMask != reverseColMask) return -1
            if (curMask == colMask) {
                colsPattern[j] = 0
                colCntMask++
            } else {
                colsPattern[j] = 1
            }
        }

        if (!validCount(rowCntMask, n) || !validCount(colCntMask, n)) return -1

        val rowSwaps = getSwaps(rowsPattern)
        val colSwaps = getSwaps(colsPattern)

        return rowSwaps + colSwaps
    }

    private fun validCount(cnt: Int, n: Int): Boolean {
        return if (n % 2 == 0) cnt == n / 2 else Math.abs(n / 2 - cnt) <= 1
    }

    private fun getSwaps(arr: IntArray): Int {
        val N = arr.size
        var matchPattern0 = 0 // matches pattern starting with 0 at even indices
        for (i in 0 until N) {
            if (arr[i] == (i % 2)) matchPattern0++
        }
        return if (N % 2 == 0) {
            Math.min(matchPattern0, N - matchPattern0) / 2
        } else {
            // For odd N, the correct pattern must start with the majority element.
            if ((matchPattern0 % 2) == 1) {
                (N - matchPattern0) / 2
            } else {
                matchPattern0 / 2
            }
        }
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int movesToChessboard(List<List<int>> board) {
    int n = board.length;
    // Validate the board pattern
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if ((board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]) != 0) {
          return -1;
        }
      }
    }

    int rowSum = 0, colSum = 0;
    for (int i = 0; i < n; i++) {
      rowSum += board[0][i];
      colSum += board[i][0];
    }

    // The number of ones in first row/column must be n/2 or (n+1)/2
    if (rowSum < n ~/ 2 || rowSum > (n + 1) ~/ 2) return -1;
    if (colSum < n ~/ 2 || colSum > (n + 1) ~/ 2) return -1;

    int rowSwap = 0, colSwap = 0;
    for (int i = 0; i < n; i++) {
      if (board[i][0] == i % 2) rowSwap++;
      if (board[0][i] == i % 2) colSwap++;
    }

    if (n % 2 == 0) {
      rowSwap = min(rowSwap, n - rowSwap);
      colSwap = min(colSwap, n - colSwap);
    } else {
      // For odd n, the swap count must be even; otherwise take the complement
      if (rowSwap % 2 == 1) rowSwap = n - rowSwap;
      if (colSwap % 2 == 1) colSwap = n - colSwap;
    }

    return (rowSwap + colSwap) ~/ 2;
  }
}
```

## Golang

```go
func movesToChessboard(board [][]int) int {
	n := len(board)
	// Validate that the board can be transformed
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if board[i][j] != (board[0][j]^board[i][0]^board[0][0]) {
				return -1
			}
		}
	}

	rowSum, colSum := 0, 0
	rowSwap, colSwap := 0, 0

	for i := 0; i < n; i++ {
		rowSum += board[0][i]
		colSum += board[i][0]

		if board[i][0] == i%2 {
			rowSwap++
		}
		if board[0][i] == i%2 {
			colSwap++
		}
	}

	// Check the counts of 1s are valid
	if n/2 > rowSum || rowSum > (n+1)/2 {
		return -1
	}
	if n/2 > colSum || colSum > (n+1)/2 {
		return -1
	}

	min := func(a, b int) int {
		if a < b {
			return a
		}
		return b
	}

	if n%2 == 0 {
		rowSwap = min(rowSwap, n-rowSwap)
		colSwap = min(colSwap, n-colSwap)
	} else {
		if rowSwap%2 == 1 {
			rowSwap = n - rowSwap
		}
		if colSwap%2 == 1 {
			colSwap = n - colSwap
		}
	}

	return (rowSwap + colSwap) / 2
}
```

## Ruby

```ruby
def moves_to_chessboard(board)
  n = board.size
  # feasibility check using XOR condition
  (0...n).each do |i|
    (0...n).each do |j|
      if (board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]) == 1
        return -1
      end
    end
  end

  row_sum = board[0].sum
  col_sum = (0...n).map { |i| board[i][0] }.sum

  row_swap = (0...n).count { |i| board[0][i] != i % 2 }
  col_swap = (0...n).count { |i| board[i][0] != i % 2 }

  if n.odd?
    half = n / 2
    unless (row_sum == half || row_sum == half + 1) && (col_sum == half || col_sum == half + 1)
      return -1
    end
    row_swap = (row_swap % 2 == 1) ? n - row_swap : row_swap
    col_swap = (col_swap % 2 == 1) ? n - col_swap : col_swap
  else
    half = n / 2
    unless row_sum == half && col_sum == half
      return -1
    end
    row_swap = [row_swap, n - row_swap].min
    col_swap = [col_swap, n - col_swap].min
  end

  (row_swap + col_swap) / 2
end
```

## Scala

```scala
object Solution {
    def movesToChessboard(board: Array[Array[Int]]): Int = {
        val n = board.length
        // Build masks for first row and first column
        var rowMask = 0
        var colMask = 0
        for (j <- 0 until n) if (board(0)(j) == 1) rowMask |= (1 << j)
        for (i <- 0 until n) if (board(i)(0) == 1) colMask |= (1 << i)

        val reverseRowMask = ((1 << n) - 1) ^ rowMask
        val reverseColMask = ((1 << n) - 1) ^ colMask

        // Validate rows and count how many match the original mask
        var rowCnt = 0
        for (i <- 0 until n) {
            var curMask = 0
            for (j <- 0 until n) if (board(i)(j) == 1) curMask |= (1 << j)
            if (curMask != rowMask && curMask != reverseRowMask) return -1
            if (curMask == rowMask) rowCnt += 1
        }

        // Validate columns and count how many match the original mask
        var colCnt = 0
        for (j <- 0 until n) {
            var curMask = 0
            for (i <- 0 until n) if (board(i)(j) == 1) curMask |= (1 << i)
            if (curMask != colMask && curMask != reverseColMask) return -1
            if (curMask == colMask) colCnt += 1
        }

        // Check count feasibility
        if (n % 2 == 0) {
            if (rowCnt != n / 2 || colCnt != n / 2) return -1
        } else {
            if (!((rowCnt == n / 2) || (rowCnt == n / 2 + 1))) return -1
            if (!((colCnt == n / 2) || (colCnt == n / 2 + 1))) return -1
        }

        // Helper to compute minimal swaps for a mask
        def getMoves(mask: Int, onesInMask: Int): Int = {
            var pattern0 = 0 // start with 0 at index 0 -> ones at odd positions
            var pattern1 = 0 // start with 1 at index 0 -> ones at even positions
            for (i <- 0 until n) {
                if ((i & 1) == 1) pattern0 |= (1 << i)
                else pattern1 |= (1 << i)
            }
            if (n % 2 == 0) {
                val diff0 = Integer.bitCount(mask ^ pattern0)
                val diff1 = Integer.bitCount(mask ^ pattern1)
                Math.min(diff0, diff1) / 2
            } else {
                // For odd n, the pattern must have majority matching onesInMask
                if (onesInMask * 2 > n) { // more ones than zeros -> use pattern with more ones (pattern1)
                    Integer.bitCount(mask ^ pattern1) / 2
                } else {
                    Integer.bitCount(mask ^ pattern0) / 2
                }
            }
        }

        val rowSwaps = getMoves(rowMask, Integer.bitCount(rowMask))
        val colSwaps = getMoves(colMask, Integer.bitCount(colMask))

        Math.max(rowSwaps, colSwaps)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn moves_to_chessboard(board: Vec<Vec<i32>>) -> i32 {
        let n = board.len();
        // Check if the board can be transformed
        for i in 0..n {
            for j in 0..n {
                if (board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]) != 0 {
                    return -1;
                }
            }
        }

        // Count ones in first row and first column
        let mut row_sum = 0;
        for j in 0..n {
            row_sum += board[0][j];
        }
        let mut col_sum = 0;
        for i in 0..n {
            col_sum += board[i][0];
        }

        // Validate counts based on parity of n
        if n % 2 == 0 {
            if row_sum != (n / 2) as i32 || col_sum != (n / 2) as i32 {
                return -1;
            }
        } else {
            let half = n / 2;
            if !(row_sum == half as i32 || row_sum == (half + 1) as i32) {
                return -1;
            }
            if !(col_sum == half as i32 || col_sum == (half + 1) as i32) {
                return -1;
            }
        }

        // Compute swaps needed for rows
        let mut row_swap = 0;
        for i in 0..n {
            if board[i][0] != (i % 2) as i32 {
                row_swap += 1;
            }
        }
        // Compute swaps needed for columns
        let mut col_swap = 0;
        for j in 0..n {
            if board[0][j] != (j % 2) as i32 {
                col_swap += 1;
            }
        }

        // Adjust swap counts based on parity of n
        if n % 2 == 0 {
            row_swap = std::cmp::min(row_swap, n - row_swap);
            col_swap = std::cmp::min(col_swap, n - col_swap);
        } else {
            if row_swap % 2 == 1 {
                row_swap = n - row_swap;
            }
            if col_swap % 2 == 1 {
                col_swap = n - col_swap;
            }
        }

        let total_swaps = (row_swap / 2) + (col_swap / 2);
        total_swaps as i32
    }
}
```

## Racket

```racket
#lang racket

(require racket/contract)

(define (list->bits lst)
  (let loop ((lst lst) (acc 0))
    (if (null? lst)
        acc
        (loop (cdr lst) (+ (* acc 2) (car lst))))))

(define (transpose m)
  (apply map list m))

(: compute-swaps (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer? exact-integer?))
(define (compute-swaps masks first-mask n all-ones same-count)
  (let* ((comp (bitwise-xor first-mask all-ones))
         (mismatches0
          (for/sum ([i (in-range n)])
            (if (= (list-ref masks i)
                   (if (even? i) first-mask comp))
                0 1)))
         (swaps0 (quotient mismatches0 2)))
    (if (even? n)
        (let* ((mismatches1
                (for/sum ([i (in-range n)])
                  (if (= (list-ref masks i)
                         (if (even? i) comp first-mask))
                      0 1)))
               (swaps1 (quotient mismatches1 2)))
          (min swaps0 swaps1))
        ;; odd n: pattern forced by majority count
        (if (>= same-count (add1 (quotient n 2))) ; first mask should be at even indices
            swaps0
            (let* ((mismatches1
                    (for/sum ([i (in-range n)])
                      (if (= (list-ref masks i)
                             (if (even? i) comp first-mask))
                          0 1)))
                   (swaps1 (quotient mismatches1 2)))
              swaps1)))))

(define/contract (moves-to-chessboard board)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length board))
         (all-ones (sub1 (arithmetic-shift 1 n)))
         (row-masks (map list->bits board))
         (first-row-mask (car row-masks))
         (row-comp (bitwise-xor first-row-mask all-ones))
         ;; check rows validity and count matches
         (rows-same-count
          (let loop ((lst row-masks) (cnt 0))
            (cond [(null? lst) cnt]
                  [else (define cur (car lst))
                        (if (or (= cur first-row-mask)
                                (= cur row-comp))
                            (loop (cdr lst) (+ cnt (if (= cur first-row-mask) 1 0)))
                            (begin
                              ;; invalid pattern
                              (set! rows-same-count -1)
                              (return -1)))]))))
    (if (= rows-same-count -1)
        -1
        (let* ((col-lists (transpose board))
               (col-masks (map list->bits col-lists))
               (first-col-mask (car col-masks))
               (col-comp (bitwise-xor first-col-mask all-ones))
               (cols-same-count
                (let loop ((lst col-masks) (cnt 0))
                  (cond [(null? lst) cnt]
                        [else (define cur (car lst))
                              (if (or (= cur first-col-mask)
                                      (= cur col-comp))
                                  (loop (cdr lst) (+ cnt (if (= cur first-col-mask) 1 0)))
                                  (begin
                                    (set! cols-same-count -1)
                                    (return -1)))]))))
          (if (or (= rows-same-count -1) (= cols-same-count -1))
              -1
              (let* ((valid-rows?
                      (or (and (even? n)
                               (= rows-same-count (/ n 2)))
                          (and (odd? n)
                               (or (= rows-same-count (add1 (quotient n 2)))
                                   (= rows-same-count (quotient n 2))))))
                     (valid-cols?
                      (or (and (even? n)
                               (= cols-same-count (/ n 2)))
                          (and (odd? n)
                               (or (= cols-same-count (add1 (quotient n 2)))
                                   (= cols-same-count (quotient n 2))))))
                     )
                (if (and valid-rows? valid-cols?)
                    (+ (compute-swaps row-masks first-row-mask n all-ones rows-same-count)
                       (compute-swaps col-masks first-col-mask n all-ones cols-same-count))
                    -1)))))))
```

## Erlang

```erlang
-module(solution).
-export([moves_to_chessboard/1]).

-spec moves_to_chessboard(Board :: [[integer()]]) -> integer().
moves_to_chessboard(Board) ->
    N = length(Board),
    FirstRow = hd(Board),
    ComplementRow = [1 - X || X <- FirstRow],
    {RowsSameCount, RowValid} = validate_lines(Board, FirstRow, ComplementRow, 0, true),
    case RowValid of
        false -> -1;
        true ->
            Columns = get_columns(Board, N),
            FirstCol = hd(Columns),
            ComplementCol = [1 - X || X <- FirstCol],
            {ColsSameCount, ColValid} = validate_lines(Columns, FirstCol, ComplementCol, 0, true),
            case ColValid of
                false -> -1;
                true ->
                    RowPatternList = [if Row == FirstRow -> 1; true -> 0 end || Row <- Board],
                    ColPatternList = [if Col == FirstCol -> 1; true -> 0 end || Col <- Columns],
                    RowSwaps = compute_swaps(RowPatternList, N, RowsSameCount),
                    ColSwaps = compute_swaps(ColPatternList, N, ColsSameCount),
                    RowSwaps + ColSwaps
            end
    end.

validate_lines([], _Pattern, _Complement, SameCnt, Valid) ->
    {SameCnt, Valid};
validate_lines([Line | Rest], Pattern, Complement, SameCnt, Valid) ->
    case Line of
        Pattern ->
            validate_lines(Rest, Pattern, Complement, SameCnt + 1, Valid);
        Complement ->
            validate_lines(Rest, Pattern, Complement, SameCnt, Valid);
        _ ->
            validate_lines(Rest, Pattern, Complement, SameCnt, false)
    end.

get_columns(Board, N) ->
    [column_at(I, Board) || I <- lists:seq(0, N - 1)].

column_at(Index, Board) ->
    [lists:nth(Index + 1, Row) || Row <- Board].

compute_swaps(PatternList, N, SameCount) ->
    MismatchEven = mismatches(lists:zip(lists:seq(0, N - 1), PatternList), true, 0),
    SwapsEven = MismatchEven div 2,
    MismatchOdd = mismatches(lists:zip(lists:seq(0, N - 1), PatternList), false, 0),
    SwapsOdd = MismatchOdd div 2,
    case N rem 2 of
        0 -> erlang:min(SwapsEven, SwapsOdd);
        _ ->
            if SameCount > N div 2 -> SwapsEven; true -> SwapsOdd end
    end.

mismatches([], _StartEven, Acc) ->
    Acc;
mismatches([{Idx, Val} | Rest], StartEven, Acc) ->
    Expected = case {StartEven, Idx rem 2} of
        {true, 0} -> 1;
        {true, 1} -> 0;
        {false, 0} -> 0;
        {false, 1} -> 1
    end,
    NewAcc = if Val =/= Expected -> Acc + 1; true -> Acc end,
    mismatches(Rest, StartEven, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec moves_to_chessboard(board :: [[integer]]) :: integer
  def moves_to_chessboard(board) do
    n = length(board)
    mask = (1 <<< n) - 1

    rows = Enum.map(board, &row_to_int(&1))
    first_row = hd(rows)
    comp_first_row = Bitwise.bxor(first_row, mask)

    # validate rows pattern and count same rows
    case validate_patterns(rows, first_row, comp_first_row) do
      {:error, _} -> -1
      {:ok, same_rows} ->
        cols = build_columns(board, n)
        first_col = hd(cols)
        comp_first_col = Bitwise.bxor(first_col, mask)

        case validate_patterns(cols, first_col, comp_first_col) do
          {:error, _} -> -1
          {:ok, same_cols} ->
            # check ones count condition
            if !valid_ones?(first_row, n) or !valid_ones?(first_col, n) do
              -1
            else
              row_swaps = min_swaps(rows, first_row, comp_first_row, same_rows, n)
              col_swaps = min_swaps(cols, first_col, comp_first_col, same_cols, n)
              row_swaps + col_swaps
            end
        end
    end
  end

  defp row_to_int(row) do
    Enum.reduce(row, 0, fn bit, acc -> (acc <<< 1) ||| bit end)
  end

  defp build_columns(board, n) do
    for j <- 0..(n - 1) do
      col_bits =
        board
        |> Enum.map(fn row -> Enum.at(row, j) end)

      row_to_int(col_bits)
    end
  end

  defp validate_patterns(list, a, b) do
    {ok, cnt} =
      Enum.reduce_while(list, {0, 0}, fn x, {_valid, count} ->
        cond do
          x == a -> {:cont, {true, count + 1}}
          x == b -> {:cont, {true, count}}
          true -> {:halt, {:error, :invalid}}
        end
      end)

    case ok do
      :error -> {:error, :invalid}
      true -> {:ok, cnt}
    end
  end

  defp valid_ones?(mask_int, n) do
    ones = bit_count(mask_int)
    if rem(n, 2) == 0 do
      ones == div(n, 2)
    else
      ones == div(n, 2) or ones == div(n, 2) + 1
    end
  end

  defp bit_count(0), do: 0
  defp bit_count(x), do: (x &&& 1) + bit_count(x >>> 1)

  defp min_swaps(list, a, b, same_cnt, n) do
    pattern =
      Enum.map(list, fn x -> if x == a, do: 0, else: 1 end)

    mism0 = count_mismatches(pattern, fn idx -> rem(idx, 2) end)
    mism1 = count_mismatches(pattern, fn idx -> Bitwise.bxor(rem(idx, 2), 1) end)

    if rem(n, 2) == 0 do
      div(min(mism0, mism1), 2)
    else
      # For odd n, the number of ones must match the required count
      if same_cnt * 2 < n do
        div(mism1, 2)
      else
        div(mism0, 2)
      end
    end
  end

  defp count_mismatches(pattern, expected_fun) do
    Enum.with_index(pattern)
    |> Enum.count(fn {val, idx} -> val != expected_fun.(idx) end)
  end
end
```
