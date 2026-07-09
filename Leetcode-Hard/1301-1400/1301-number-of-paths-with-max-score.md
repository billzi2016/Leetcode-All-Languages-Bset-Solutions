# 1301. Number of Paths with Max Score

## Cpp

```cpp
class Solution {
public:
    vector<int> pathsWithMaxScore(vector<string>& board) {
        const int MOD = 1000000007;
        int n = board.size();
        const int INF_NEG = -1e9;
        vector<vector<int>> dpScore(n, vector<int>(n, INF_NEG));
        vector<vector<int>> dpCount(n, vector<int>(n, 0));
        dpScore[n-1][n-1] = 0;
        dpCount[n-1][n-1] = 1;
        for (int i = n - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                if (board[i][j] == 'X') continue;
                if (i == n-1 && j == n-1) continue; // start cell already initialized
                int best = INF_NEG;
                long long ways = 0;
                const int di[3] = {1, 0, 1};
                const int dj[3] = {0, 1, 1};
                for (int k = 0; k < 3; ++k) {
                    int ni = i + di[k];
                    int nj = j + dj[k];
                    if (ni >= n || nj >= n) continue;
                    if (dpScore[ni][nj] == INF_NEG) continue;
                    if (dpScore[ni][nj] > best) {
                        best = dpScore[ni][nj];
                        ways = dpCount[ni][nj];
                    } else if (dpScore[ni][nj] == best) {
                        ways += dpCount[ni][nj];
                    }
                }
                if (best == INF_NEG) continue; // unreachable
                int add = 0;
                char c = board[i][j];
                if (c >= '0' && c <= '9') add = c - '0';
                dpScore[i][j] = best + add;
                dpCount[i][j] = ways % MOD;
            }
        }
        if (dpScore[0][0] == INF_NEG) return {0, 0};
        return {dpScore[0][0], dpCount[0][0]};
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    
    public int[] pathsWithMaxScore(List<String> board) {
        int n = board.size();
        int[][] dpScore = new int[n][n];
        int[][] dpCnt = new int[n][n];
        for (int i = 0; i < n; i++) {
            java.util.Arrays.fill(dpScore[i], -1);
        }
        dpScore[n - 1][n - 1] = 0;
        dpCnt[n - 1][n - 1] = 1;
        
        for (int i = n - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                char c = board.get(i).charAt(j);
                if (c == 'X') continue;
                if (i == n - 1 && j == n - 1) continue; // start cell already set
                
                int maxPrev = -1;
                // check down, right, diagonal
                if (i + 1 < n && dpScore[i + 1][j] > maxPrev) maxPrev = dpScore[i + 1][j];
                if (j + 1 < n && dpScore[i][j + 1] > maxPrev) maxPrev = dpScore[i][j + 1];
                if (i + 1 < n && j + 1 < n && dpScore[i + 1][j + 1] > maxPrev) maxPrev = dpScore[i + 1][j + 1];
                
                if (maxPrev == -1) continue; // unreachable
                
                int val = 0;
                if (c >= '0' && c <= '9') {
                    val = c - '0';
                }
                dpScore[i][j] = maxPrev + val;
                
                long cnt = 0;
                if (i + 1 < n && dpScore[i + 1][j] == maxPrev) cnt += dpCnt[i + 1][j];
                if (j + 1 < n && dpScore[i][j + 1] == maxPrev) cnt += dpCnt[i][j + 1];
                if (i + 1 < n && j + 1 < n && dpScore[i + 1][j + 1] == maxPrev) cnt += dpCnt[i + 1][j + 1];
                
                dpCnt[i][j] = (int)(cnt % MOD);
            }
        }
        
        if (dpCnt[0][0] == 0) return new int[]{0, 0};
        return new int[]{dpScore[0][0], dpCnt[0][0]};
    }
}
```

## Python

```python
class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        n = len(board)
        # dp_score[i][j]: max score from (i,j) to end (excluding value at (i,j))
        dp_score = [[-10**9] * n for _ in range(n)]
        dp_cnt = [[0] * n for _ in range(n)]

        # starting point S at bottom-right
        dp_score[n-1][n-1] = 0
        dp_cnt[n-1][n-1] = 1

        for i in reversed(range(n)):
            for j in reversed(range(n)):
                if board[i][j] == 'X' or (i == n-1 and j == n-1):
                    continue
                max_next = -10**9
                ways = 0
                # check three possible moves: down, right, diagonal down-right
                for ni, nj in ((i+1, j), (i, j+1), (i+1, j+1)):
                    if ni < n and nj < n and dp_cnt[ni][nj] > 0:
                        if dp_score[ni][nj] > max_next:
                            max_next = dp_score[ni][nj]
                            ways = dp_cnt[ni][nj]
                        elif dp_score[ni][nj] == max_next:
                            ways = (ways + dp_cnt[ni][nj]) % MOD
                if ways == 0:  # no reachable neighbor
                    continue
                cell_val = 0
                ch = board[i][j]
                if ch.isdigit():
                    cell_val = int(ch)
                # 'E' also contributes 0
                dp_score[i][j] = max_next + cell_val
                dp_cnt[i][j] = ways % MOD

        if dp_cnt[0][0] == 0:
            return [0, 0]
        else:
            return [dp_score[0][0], dp_cnt[0][0] % MOD]
```

## Python3

```python
class Solution:
    def pathsWithMaxScore(self, board):
        from typing import List
        n = len(board)
        MOD = 10**9 + 7
        NEG_INF = -10**9

        dp_score = [[NEG_INF] * n for _ in range(n)]
        dp_cnt = [[0] * n for _ in range(n)]

        dp_score[n - 1][n - 1] = 0
        dp_cnt[n - 1][n - 1] = 1

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 'X' or (i == n - 1 and j == n - 1):
                    continue
                best = NEG_INF
                ways = 0
                for ni, nj in ((i + 1, j), (i, j + 1), (i + 1, j + 1)):
                    if ni < n and nj < n and dp_cnt[ni][nj]:
                        if dp_score[ni][nj] > best:
                            best = dp_score[ni][nj]
                            ways = dp_cnt[ni][nj]
                        elif dp_score[ni][nj] == best:
                            ways = (ways + dp_cnt[ni][nj]) % MOD
                if best == NEG_INF:
                    continue
                add = int(board[i][j]) if board[i][j].isdigit() else 0
                dp_score[i][j] = best + add
                dp_cnt[i][j] = ways % MOD

        return [0, 0] if dp_cnt[0][0] == 0 else [dp_score[0][0], dp_cnt[0][0]]
```

## C

```c
#include <stdlib.h>
#include <string.h>

#define MOD 1000000007

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* pathsWithMaxScore(char ** board, int boardSize, int* returnSize){
    int n = boardSize;
    int total = n * n;
    int *score = (int*)malloc(total * sizeof(int));
    long long *cnt = (long long*)malloc(total * sizeof(long long));
    for (int i = 0; i < total; ++i) {
        score[i] = -1;   // unreachable
        cnt[i] = 0;
    }

    // start at bottom-right 'S'
    int sr = n - 1, sc = n - 1;
    score[sr * n + sc] = 0;
    cnt[sr * n + sc] = 1;

    for (int i = n - 1; i >= 0; --i) {
        for (int j = n - 1; j >= 0; --j) {
            if (board[i][j] == 'X') continue;
            if (i == sr && j == sc) continue; // start already set

            int val = 0;
            char ch = board[i][j];
            if (ch >= '0' && ch <= '9')
                val = ch - '0';
            // else 'E' or other, value stays 0

            int best = -1;
            long long ways = 0;

            // down
            if (i + 1 < n) {
                int idx = (i + 1) * n + j;
                if (score[idx] != -1) {
                    if (score[idx] > best) {
                        best = score[idx];
                        ways = cnt[idx];
                    } else if (score[idx] == best) {
                        ways += cnt[idx];
                    }
                }
            }
            // right
            if (j + 1 < n) {
                int idx = i * n + (j + 1);
                if (score[idx] != -1) {
                    if (score[idx] > best) {
                        best = score[idx];
                        ways = cnt[idx];
                    } else if (score[idx] == best) {
                        ways += cnt[idx];
                    }
                }
            }
            // down-right diagonal
            if (i + 1 < n && j + 1 < n) {
                int idx = (i + 1) * n + (j + 1);
                if (score[idx] != -1) {
                    if (score[idx] > best) {
                        best = score[idx];
                        ways = cnt[idx];
                    } else if (score[idx] == best) {
                        ways += cnt[idx];
                    }
                }
            }

            if (best == -1) continue; // unreachable

            int idxCur = i * n + j;
            score[idxCur] = best + val;
            cnt[idxCur] = ways % MOD;
        }
    }

    int *res = (int*)malloc(2 * sizeof(int));
    *returnSize = 2;
    if (score[0] == -1) {
        res[0] = 0;
        res[1] = 0;
    } else {
        res[0] = score[0];
        res[1] = (int)(cnt[0] % MOD);
    }

    free(score);
    free(cnt);
    return res;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private const int MOD = 1000000007;
    public int[] PathsWithMaxScore(IList<string> board) {
        int n = board.Count;
        int[,] maxScore = new int[n, n];
        int[,] ways = new int[n, n];

        // Initialize scores to -1 (unreachable)
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                maxScore[i, j] = -1;
                ways[i, j] = 0;
            }
        }

        // Starting position 'S' at bottom-right
        maxScore[n - 1, n - 1] = 0;
        ways[n - 1, n - 1] = 1;

        for (int i = n - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if (board[i][j] == 'X') continue;
                if (i == n - 1 && j == n - 1) continue; // start cell already set

                int bestPrevScore = -1;
                long totalWays = 0;

                // Check three possible previous cells
                // Down (i+1, j)
                if (i + 1 < n && ways[i + 1, j] > 0) {
                    int s = maxScore[i + 1, j];
                    if (s > bestPrevScore) {
                        bestPrevScore = s;
                        totalWays = ways[i + 1, j];
                    } else if (s == bestPrevScore) {
                        totalWays += ways[i + 1, j];
                    }
                }
                // Right (i, j+1)
                if (j + 1 < n && ways[i, j + 1] > 0) {
                    int s = maxScore[i, j + 1];
                    if (s > bestPrevScore) {
                        bestPrevScore = s;
                        totalWays = ways[i, j + 1];
                    } else if (s == bestPrevScore) {
                        totalWays += ways[i, j + 1];
                    }
                }
                // Diagonal down-right (i+1, j+1)
                if (i + 1 < n && j + 1 < n && ways[i + 1, j + 1] > 0) {
                    int s = maxScore[i + 1, j + 1];
                    if (s > bestPrevScore) {
                        bestPrevScore = s;
                        totalWays = ways[i + 1, j + 1];
                    } else if (s == bestPrevScore) {
                        totalWays += ways[i + 1, j + 1];
                    }
                }

                if (bestPrevScore == -1) continue; // unreachable

                int cellValue = 0;
                char c = board[i][j];
                if (c >= '0' && c <= '9') {
                    cellValue = c - '0';
                }
                // 'S' and 'E' contribute 0

                maxScore[i, j] = bestPrevScore + cellValue;
                ways[i, j] = (int)(totalWays % MOD);
            }
        }

        if (ways[0, 0] == 0) return new int[] { 0, 0 };
        return new int[] { maxScore[0, 0], ways[0, 0] };
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} board
 * @return {number[]}
 */
var pathsWithMaxScore = function(board) {
    const MOD = 1000000007;
    const n = board.length;
    const dpScore = Array.from({ length: n }, () => Array(n).fill(-Infinity));
    const dpCount = Array.from({ length: n }, () => Array(n).fill(0));

    dpScore[n - 1][n - 1] = 0; // start at 'S'
    dpCount[n - 1][n - 1] = 1;

    for (let i = n - 1; i >= 0; --i) {
        for (let j = n - 1; j >= 0; --j) {
            if (board[i][j] === 'X' || (i === n - 1 && j === n - 1)) continue;

            let maxPrev = -Infinity;
            let ways = 0;

            const consider = (x, y) => {
                if (x < 0 || x >= n || y < 0 || y >= n) return;
                if (board[x][y] === 'X') return;
                if (dpScore[x][y] === -Infinity) return;
                const sc = dpScore[x][y];
                if (sc > maxPrev) {
                    maxPrev = sc;
                    ways = dpCount[x][y];
                } else if (sc === maxPrev) {
                    ways = (ways + dpCount[x][y]) % MOD;
                }
            };

            consider(i + 1, j);     // from down
            consider(i, j + 1);     // from right
            consider(i + 1, j + 1); // from diagonal

            if (maxPrev === -Infinity) continue;

            const ch = board[i][j];
            const add = (ch >= '0' && ch <= '9') ? Number(ch) : 0;
            dpScore[i][j] = maxPrev + add;
            dpCount[i][j] = ways % MOD;
        }
    }

    if (dpScore[0][0] === -Infinity) return [0, 0];
    return [dpScore[0][0], dpCount[0][0]];
};
```

## Typescript

```typescript
function pathsWithMaxScore(board: string[]): number[] {
    const n = board.length;
    const MOD = 1000000007;
    const dpScore: number[][] = Array.from({ length: n }, () => Array(n).fill(-Infinity));
    const dpCount: number[][] = Array.from({ length: n }, () => Array(n).fill(0));

    // Start position 'S' at bottom-right
    dpScore[n - 1][n - 1] = 0;
    dpCount[n - 1][n - 1] = 1;

    for (let i = n - 1; i >= 0; i--) {
        for (let j = n - 1; j >= 0; j--) {
            if (board[i][j] === 'X') continue;
            // Skip the start cell, already initialized
            if (i === n - 1 && j === n - 1) continue;

            let maxPrev = -Infinity;
            let ways = 0;

            // From down (i+1, j)
            if (i + 1 < n && dpScore[i + 1][j] > -Infinity) {
                const sc = dpScore[i + 1][j];
                if (sc > maxPrev) {
                    maxPrev = sc;
                    ways = dpCount[i + 1][j];
                } else if (sc === maxPrev) {
                    ways = (ways + dpCount[i + 1][j]) % MOD;
                }
            }

            // From right (i, j+1)
            if (j + 1 < n && dpScore[i][j + 1] > -Infinity) {
                const sc = dpScore[i][j + 1];
                if (sc > maxPrev) {
                    maxPrev = sc;
                    ways = dpCount[i][j + 1];
                } else if (sc === maxPrev) {
                    ways = (ways + dpCount[i][j + 1]) % MOD;
                }
            }

            // From diagonal down-right (i+1, j+1)
            if (i + 1 < n && j + 1 < n && dpScore[i + 1][j + 1] > -Infinity) {
                const sc = dpScore[i + 1][j + 1];
                if (sc > maxPrev) {
                    maxPrev = sc;
                    ways = dpCount[i + 1][j + 1];
                } else if (sc === maxPrev) {
                    ways = (ways + dpCount[i + 1][j + 1]) % MOD;
                }
            }

            if (maxPrev === -Infinity) continue; // unreachable

            const ch = board[i][j];
            let add = 0;
            if (ch >= '0' && ch <= '9') {
                add = Number(ch);
            } // 'E' and 'S' contribute 0

            dpScore[i][j] = maxPrev + add;
            dpCount[i][j] = ways % MOD;
        }
    }

    const finalScore = dpScore[0][0];
    const finalWays = dpCount[0][0];

    if (finalScore < 0 || finalWays === 0) {
        return [0, 0];
    }
    return [finalScore, finalWays];
}
```

## Php

```php
class Solution {
    /**
     * @param String[] $board
     * @return Integer[]
     */
    function pathsWithMaxScore($board) {
        $n = count($board);
        $mod = 1000000007;
        $dpScore = array_fill(0, $n, array_fill(0, $n, -1));
        $dpCount = array_fill(0, $n, array_fill(0, $n, 0));
        $dpScore[$n-1][$n-1] = 0;
        $dpCount[$n-1][$n-1] = 1;

        for ($i = $n - 1; $i >= 0; --$i) {
            for ($j = $n - 1; $j >= 0; --$j) {
                if ($board[$i][$j] === 'X') continue;
                if ($dpScore[$i][$j] < 0) continue;

                $neighbors = [[$i-1,$j], [$i,$j-1], [$i-1,$j-1]];
                foreach ($neighbors as $nb) {
                    $ni = $nb[0];
                    $nj = $nb[1];
                    if ($ni < 0 || $nj < 0) continue;
                    if ($board[$ni][$nj] === 'X') continue;

                    $ch = $board[$ni][$nj];
                    $add = (ctype_digit($ch)) ? intval($ch) : 0;
                    $newScore = $dpScore[$i][$j] + $add;

                    if ($newScore > $dpScore[$ni][$nj]) {
                        $dpScore[$ni][$nj] = $newScore;
                        $dpCount[$ni][$nj] = $dpCount[$i][$j];
                    } elseif ($newScore == $dpScore[$ni][$nj]) {
                        $dpCount[$ni][$nj] = ($dpCount[$ni][$nj] + $dpCount[$i][$j]) % $mod;
                    }
                }
            }
        }

        if ($dpScore[0][0] < 0) {
            return [0, 0];
        } else {
            return [$dpScore[0][0], $dpCount[0][0] % $mod];
        }
    }
}
```

## Swift

```swift
class Solution {
    func pathsWithMaxScore(_ board: [String]) -> [Int] {
        let MOD = 1_000_000_007
        let n = board.count
        var grid = [[Character]]()
        for row in board {
            grid.append(Array(row))
        }
        
        var score = Array(repeating: Array(repeating: Int.min, count: n), count: n)
        var cnt = Array(repeating: Array(repeating: 0, count: n), count: n)
        
        // start position at bottom-right 'S'
        score[n-1][n-1] = 0
        cnt[n-1][n-1] = 1
        
        for i in stride(from: n - 1, through: 0, by: -1) {
            for j in stride(from: n - 1, through: 0, by: -1) {
                if grid[i][j] == "X" { continue }
                if i == n - 1 && j == n - 1 { continue } // start cell already initialized
                
                var best = Int.min
                var ways = 0
                
                let dirs = [(1, 0), (0, 1), (1, 1)] // down, right, down-right
                for (dx, dy) in dirs {
                    let ni = i + dx
                    let nj = j + dy
                    if ni < n && nj < n && score[ni][nj] != Int.min {
                        if score[ni][nj] > best {
                            best = score[ni][nj]
                            ways = cnt[ni][nj]
                        } else if score[ni][nj] == best {
                            ways = (ways + cnt[ni][nj]) % MOD
                        }
                    }
                }
                
                if best != Int.min {
                    var val = 0
                    if let num = grid[i][j].wholeNumberValue {
                        val = num
                    }
                    score[i][j] = best + val
                    cnt[i][j] = ways % MOD
                }
            }
        }
        
        if score[0][0] == Int.min {
            return [0, 0]
        } else {
            return [score[0][0], cnt[0][0]]
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun pathsWithMaxScore(board: List<String>): IntArray {
        val n = board.size
        val MOD = 1_000_000_007L
        val NEG = -1_000_000
        val score = Array(n) { IntArray(n) { NEG } }
        val cnt = Array(n) { LongArray(n) }

        score[n - 1][n - 1] = 0
        cnt[n - 1][n - 1] = 1L

        for (i in n - 1 downTo 0) {
            for (j in n - 1 downTo 0) {
                if (board[i][j] == 'X') continue
                if (i == n - 1 && j == n - 1) continue

                var best = NEG
                var ways = 0L

                // down
                if (i + 1 < n && cnt[i + 1][j] > 0) {
                    val cand = score[i + 1][j]
                    if (cand > best) {
                        best = cand
                        ways = cnt[i + 1][j]
                    } else if (cand == best) {
                        ways = (ways + cnt[i + 1][j]) % MOD
                    }
                }
                // right
                if (j + 1 < n && cnt[i][j + 1] > 0) {
                    val cand = score[i][j + 1]
                    if (cand > best) {
                        best = cand
                        ways = cnt[i][j + 1]
                    } else if (cand == best) {
                        ways = (ways + cnt[i][j + 1]) % MOD
                    }
                }
                // diagonal down-right
                if (i + 1 < n && j + 1 < n && cnt[i + 1][j + 1] > 0) {
                    val cand = score[i + 1][j + 1]
                    if (cand > best) {
                        best = cand
                        ways = cnt[i + 1][j + 1]
                    } else if (cand == best) {
                        ways = (ways + cnt[i + 1][j + 1]) % MOD
                    }
                }

                if (best != NEG) {
                    val add = when (board[i][j]) {
                        'E', 'S' -> 0
                        else -> board[i][j] - '0'
                    }
                    score[i][j] = best + add
                    cnt[i][j] = ways % MOD
                }
            }
        }

        return if (cnt[0][0] == 0L) {
            intArrayOf(0, 0)
        } else {
            intArrayOf(score[0][0], (cnt[0][0] % MOD).toInt())
        }
    }
}
```

## Golang

```go
func pathsWithMaxScore(board []string) []int {
	const MOD int = 1000000007
	n := len(board)
	score := make([][]int, n)
	ways := make([][]int, n)
	for i := 0; i < n; i++ {
		score[i] = make([]int, n)
		ways[i] = make([]int, n)
		for j := 0; j < n; j++ {
			score[i][j] = -1
		}
	}
	score[n-1][n-1] = 0
	ways[n-1][n-1] = 1

	for i := n - 1; i >= 0; i-- {
		for j := n - 1; j >= 0; j-- {
			if board[i][j] == 'X' {
				continue
			}
			if i == n-1 && j == n-1 {
				continue
			}
			maxScore := -1
			cnt := 0
			val := 0
			c := board[i][j]
			if c >= '0' && c <= '9' {
				val = int(c - '0')
			}
			dirs := [3][2]int{{i + 1, j}, {i, j + 1}, {i + 1, j + 1}}
			for _, d := range dirs {
				ni, nj := d[0], d[1]
				if ni >= n || nj >= n {
					continue
				}
				if score[ni][nj] == -1 {
					continue
				}
				cand := score[ni][nj] + val
				if cand > maxScore {
					maxScore = cand
					cnt = ways[ni][nj]
				} else if cand == maxScore {
					cnt = (cnt + ways[ni][nj]) % MOD
				}
			}
			if maxScore >= 0 {
				score[i][j] = maxScore
				ways[i][j] = cnt % MOD
			}
		}
	}

	if score[0][0] == -1 {
		return []int{0, 0}
	}
	return []int{score[0][0], ways[0][0] % MOD}
}
```

## Ruby

```ruby
def paths_with_max_score(board)
  mod = 1_000_000_007
  n = board.size
  grid = board.map { |row| row.chars }

  dp = Array.new(n) { Array.new(n, -Float::INFINITY) }
  cnt = Array.new(n) { Array.new(n, 0) }

  dp[n - 1][n - 1] = 0
  cnt[n - 1][n - 1] = 1

  (n - 1).downto(0) do |i|
    (n - 1).downto(0) do |j|
      next if grid[i][j] == 'X'
      next if i == n - 1 && j == n - 1

      max_prev = -Float::INFINITY
      ways = 0

      [[i + 1, j], [i, j + 1], [i + 1, j + 1]].each do |ni, nj|
        next if ni >= n || nj >= n
        next if grid[ni][nj] == 'X'
        val = dp[ni][nj]
        if val > max_prev
          max_prev = val
          ways = cnt[ni][nj]
        elsif val == max_prev && val != -Float::INFINITY
          ways = (ways + cnt[ni][nj]) % mod
        end
      end

      next if max_prev == -Float::INFINITY

      add = 0
      ch = grid[i][j]
      if ('1'..'9').include?(ch)
        add = ch.ord - '0'.ord
      end

      dp[i][j] = max_prev + add
      cnt[i][j] = ways % mod
    end
  end

  if dp[0][0] == -Float::INFINITY
    [0, 0]
  else
    [dp[0][0].to_i, cnt[0][0] % mod]
  end
end
```

## Scala

```scala
object Solution {
    def pathsWithMaxScore(board: List[String]): Array[Int] = {
        val MOD = 1000000007
        val n = board.length
        val INF = Int.MinValue / 4
        val score = Array.fill(n, n)(INF)
        val cnt = Array.ofDim[Long](n, n)

        score(n - 1)(n - 1) = 0
        cnt(n - 1)(n - 1) = 1

        for (i <- (0 until n).reverse) {
            for (j <- (0 until n).reverse) {
                if (!(i == n - 1 && j == n - 1)) {
                    val ch = board(i)(j)
                    if (ch != 'X') {
                        var maxPrev = INF
                        var ways: Long = 0L

                        // from down
                        if (i + 1 < n && score(i + 1)(j) != INF) {
                            val s = score(i + 1)(j)
                            if (s > maxPrev) { maxPrev = s; ways = cnt(i + 1)(j) }
                            else if (s == maxPrev) { ways = (ways + cnt(i + 1)(j)) % MOD }
                        }
                        // from right
                        if (j + 1 < n && score(i)(j + 1) != INF) {
                            val s = score(i)(j + 1)
                            if (s > maxPrev) { maxPrev = s; ways = cnt(i)(j + 1) }
                            else if (s == maxPrev) { ways = (ways + cnt(i)(j + 1)) % MOD }
                        }
                        // from down-right
                        if (i + 1 < n && j + 1 < n && score(i + 1)(j + 1) != INF) {
                            val s = score(i + 1)(j + 1)
                            if (s > maxPrev) { maxPrev = s; ways = cnt(i + 1)(j + 1) }
                            else if (s == maxPrev) { ways = (ways + cnt(i + 1)(j + 1)) % MOD }
                        }

                        if (maxPrev != INF) {
                            val add = if (ch >= '0' && ch <= '9') ch - '0' else 0
                            score(i)(j) = maxPrev + add
                            cnt(i)(j) = ways % MOD
                        }
                    }
                }
            }
        }

        if (score(0)(0) == INF) Array(0, 0)
        else Array(score(0)(0), (cnt(0)(0) % MOD).toInt)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn paths_with_max_score(board: Vec<String>) -> Vec<i32> {
        const MOD: i64 = 1_000_000_007;
        let n = board.len();
        let mut dp_score = vec![vec![-1_i32; n]; n];
        let mut dp_cnt = vec![vec![0_i64; n]; n];

        for i in (0..n).rev() {
            for j in (0..n).rev() {
                let ch = board[i].as_bytes()[j] as char;
                if ch == 'X' {
                    continue;
                }
                if i == n - 1 && j == n - 1 {
                    // Start cell 'S'
                    dp_score[i][j] = 0;
                    dp_cnt[i][j] = 1;
                    continue;
                }

                let mut best = -1_i32;
                let mut ways: i64 = 0;

                // down
                if i + 1 < n && dp_score[i + 1][j] != -1 {
                    let s = dp_score[i + 1][j];
                    if s > best {
                        best = s;
                        ways = dp_cnt[i + 1][j];
                    } else if s == best {
                        ways = (ways + dp_cnt[i + 1][j]) % MOD;
                    }
                }
                // right
                if j + 1 < n && dp_score[i][j + 1] != -1 {
                    let s = dp_score[i][j + 1];
                    if s > best {
                        best = s;
                        ways = dp_cnt[i][j + 1];
                    } else if s == best {
                        ways = (ways + dp_cnt[i][j + 1]) % MOD;
                    }
                }
                // down-right diagonal
                if i + 1 < n && j + 1 < n && dp_score[i + 1][j + 1] != -1 {
                    let s = dp_score[i + 1][j + 1];
                    if s > best {
                        best = s;
                        ways = dp_cnt[i + 1][j + 1];
                    } else if s == best {
                        ways = (ways + dp_cnt[i + 1][j + 1]) % MOD;
                    }
                }

                if best == -1 {
                    continue; // unreachable
                }

                let add = match ch {
                    'E' | 'S' => 0,
                    _ => ch.to_digit(10).unwrap() as i32,
                };
                dp_score[i][j] = best + add;
                dp_cnt[i][j] = ways % MOD;
            }
        }

        if dp_score[0][0] == -1 {
            vec![0, 0]
        } else {
            vec![dp_score[0][0], dp_cnt[0][0] as i32]
        }
    }
}
```
