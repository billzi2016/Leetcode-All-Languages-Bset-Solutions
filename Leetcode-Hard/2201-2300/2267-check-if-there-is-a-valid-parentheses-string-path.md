# 2267. Check if There Is a Valid Parentheses String Path

## Cpp

```cpp
class Solution {
public:
    bool hasValidPath(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        const int MAXB = 205; // enough for m+n <= 200
        vector<vector<bitset<MAXB>>> dp(m, vector<bitset<MAXB>>(n));
        if (grid[0][0] == ')') return false;
        dp[0][0][1] = true; // balance after first '('
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                for (int bal = 0; bal < MAXB; ++bal) {
                    if (!dp[i][j][bal]) continue;
                    // move down
                    int ni = i + 1, nj = j;
                    if (ni < m) {
                        char c = grid[ni][nj];
                        int nb = (c == '(') ? bal + 1 : bal - 1;
                        if (nb >= 0 && nb < MAXB) dp[ni][nj][nb] = true;
                    }
                    // move right
                    ni = i; nj = j + 1;
                    if (nj < n) {
                        char c = grid[ni][nj];
                        int nb = (c == '(') ? bal + 1 : bal - 1;
                        if (nb >= 0 && nb < MAXB) dp[ni][nj][nb] = true;
                    }
                }
            }
        }
        return dp[m - 1][n - 1][0];
    }
};
```

## Java

```java
class Solution {
    public boolean hasValidPath(char[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        if (grid[0][0] == ')') return false; // cannot start with a closing bracket
        int maxBal = m + n; // maximum possible balance
        boolean[][][] dp = new boolean[m][n][maxBal + 1];
        dp[0][0][1] = true; // starting with '(' gives balance 1

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                for (int bal = 0; bal <= maxBal; bal++) {
                    if (!dp[i][j][bal]) continue;
                    // move down
                    if (i + 1 < m) {
                        int nb = bal + (grid[i + 1][j] == '(' ? 1 : -1);
                        if (nb >= 0 && nb <= maxBal) dp[i + 1][j][nb] = true;
                    }
                    // move right
                    if (j + 1 < n) {
                        int nb = bal + (grid[i][j + 1] == '(' ? 1 : -1);
                        if (nb >= 0 && nb <= maxBal) dp[i][j + 1][nb] = true;
                    }
                }
            }
        }
        return dp[m - 1][n - 1][0];
    }
}
```

## Python

```python
class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        m = len(grid)
        n = len(grid[0])
        total_len = m + n - 1

        # Starting cell must be '('
        if grid[0][0] == ')':
            return False

        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(1)  # balance after first '('

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                cur_set = set()
                ch = grid[i][j]
                prev_balances = set()
                if i > 0:
                    prev_balances |= dp[i - 1][j]
                if j > 0:
                    prev_balances |= dp[i][j - 1]

                for bal in prev_balances:
                    if ch == '(':
                        nb = bal + 1
                    else:  # ')'
                        if bal == 0:
                            continue
                        nb = bal - 1

                    steps_done = i + j          # number of moves made so far
                    remaining_cells = total_len - (steps_done + 1)
                    if nb <= remaining_cells:
                        cur_set.add(nb)

                dp[i][j] = cur_set

        return 0 in dp[m - 1][n - 1]
```

## Python3

```python
class Solution:
    def hasValidPath(self, grid):
        from collections import deque
        m, n = len(grid), len(grid[0])
        max_bal = m + n  # maximum possible balance
        
        # dp[j][bal] indicates reachable at current row i, column j with given balance
        dp = [[False] * (max_bal + 1) for _ in range(n)]
        
        for i in range(m):
            new_dp = [[False] * (max_bal + 1) for _ in range(n)]
            for j in range(n):
                ch = grid[i][j]
                if i == 0 and j == 0:
                    if ch == '(':
                        new_dp[j][1] = True
                    # starting with ')' is impossible, leave all False
                else:
                    sources = []
                    if i > 0:
                        sources.append(dp[j])          # from top
                    if j > 0:
                        sources.append(new_dp[j - 1])   # from left
                    for src in sources:
                        if ch == '(':
                            for bal, ok in enumerate(src):
                                if ok and bal + 1 <= max_bal:
                                    new_dp[j][bal + 1] = True
                        else:  # ')'
                            for bal, ok in enumerate(src):
                                if ok and bal > 0:
                                    new_dp[j][bal - 1] = True
            dp = new_dp
        
        return dp[n - 1][0]
```

## C

```c
#include <stdbool.h>
#include <string.h>

bool hasValidPath(char** grid, int gridSize, int* gridColSize) {
    int m = gridSize;
    int n = gridColSize[0];
    int maxB = m + n; // maximum possible balance (length <= m+n-1)
    
    static bool dp[101][101][205]; // constraints guarantee sizes fit
    memset(dp, 0, sizeof(dp));
    
    if (grid[0][0] == ')') return false;
    dp[0][0][1] = true; // start with one '('
    
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (i == 0 && j == 0) continue;
            char c = grid[i][j];
            int delta = (c == '(') ? 1 : -1;
            for (int b = 0; b <= maxB; ++b) {
                bool reachable = false;
                if (i > 0 && dp[i-1][j][b]) reachable = true;
                if (j > 0 && dp[i][j-1][b]) reachable = true;
                if (!reachable) continue;
                int nb = b + delta;
                if (nb >= 0 && nb <= maxB) {
                    dp[i][j][nb] = true;
                }
            }
        }
    }
    
    return dp[m-1][n-1][0];
}
```

## Csharp

```csharp
public class Solution {
    public bool HasValidPath(char[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;

        // The first cell must be '(' otherwise balance becomes negative immediately.
        if (grid[0][0] == ')') return false;

        var dp = new HashSet<int>[m, n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                dp[i, j] = new HashSet<int>();
            }
        }

        // Starting balance after the first character.
        dp[0, 0].Add(1);

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                foreach (int bal in dp[i, j]) {
                    // Move down
                    if (i + 1 < m) {
                        int nb = bal + (grid[i + 1][j] == '(' ? 1 : -1);
                        if (nb >= 0 && nb <= (m - 1 - (i + 1)) + (n - 1 - j)) {
                            dp[i + 1, j].Add(nb);
                        }
                    }
                    // Move right
                    if (j + 1 < n) {
                        int nb = bal + (grid[i][j + 1] == '(' ? 1 : -1);
                        if (nb >= 0 && nb <= (m - 1 - i) + (n - 1 - (j + 1))) {
                            dp[i, j + 1].Add(nb);
                        }
                    }
                }
            }
        }

        return dp[m - 1, n - 1].Contains(0);
    }
}
```

## Javascript

```javascript
/**
 * @param {character[][]} grid
 * @return {boolean}
 */
var hasValidPath = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    // maximum possible balance is path length (m + n)
    const maxBal = m + n;
    
    // dp[i][j] is a Uint8Array where index b indicates if balance b is reachable at cell (i,j)
    const dp = Array.from({length: m}, () => 
        Array.from({length: n}, () => new Uint8Array(maxBal + 1))
    );
    
    // start cell must be '(' to have non‑negative balance
    if (grid[0][0] !== '(') return false;
    dp[0][0][1] = 1; // balance after reading first '('
    
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            const cur = dp[i][j];
            for (let b = 0; b <= maxBal; ++b) {
                if (!cur[b]) continue;
                
                // move down
                if (i + 1 < m) {
                    const nb = b + (grid[i + 1][j] === '(' ? 1 : -1);
                    if (nb >= 0 && nb <= maxBal) dp[i + 1][j][nb] = 1;
                }
                
                // move right
                if (j + 1 < n) {
                    const nb = b + (grid[i][j + 1] === '(' ? 1 : -1);
                    if (nb >= 0 && nb <= maxBal) dp[i][j + 1][nb] = 1;
                }
            }
        }
    }
    
    return dp[m - 1][n - 1][0] === 1;
};
```

## Typescript

```typescript
function hasValidPath(grid: string[][]): boolean {
    const m = grid.length;
    const n = grid[0].length;
    const totalLen = m + n - 1;
    if (totalLen % 2 === 1) return false; // cannot be balanced
    
    // dp[i][j] stores possible balances after reaching cell (i,j)
    const dp: Set<number>[][] = Array.from({ length: m }, () =>
        Array.from({ length: n }, () => new Set<number>())
    );
    
    if (grid[0][0] === '(') {
        dp[0][0].add(1);
    } else {
        return false; // starting with ')' is invalid
    }
    
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            const curSet = dp[i][j];
            if (!curSet.size) continue;
            
            // move down
            if (i + 1 < m) {
                const ch = grid[i + 1][j];
                for (const bal of curSet) {
                    const nb = bal + (ch === '(' ? 1 : -1);
                    if (nb >= 0 && nb <= totalLen) dp[i + 1][j].add(nb);
                }
            }
            // move right
            if (j + 1 < n) {
                const ch = grid[i][j + 1];
                for (const bal of curSet) {
                    const nb = bal + (ch === '(' ? 1 : -1);
                    if (nb >= 0 && nb <= totalLen) dp[i][j + 1].add(nb);
                }
            }
        }
    }
    
    return dp[m - 1][n - 1].has(0);
}
```

## Php

```php
class Solution {

    /**
     * @param String[][] $grid
     * @return Boolean
     */
    function hasValidPath($grid) {
        $m = count($grid);
        $n = count($grid[0]);

        // Length of any path must be even to have equal '(' and ')'
        if ((($m + $n - 1) & 1) == 1) {
            return false;
        }

        // dp[i][j] stores reachable balances at cell (i,j)
        $dp = array_fill(0, $m, array_fill(0, $n, []));

        if ($grid[0][0] === '(') {
            $dp[0][0][1] = true;
        } else {
            return false; // cannot start with ')'
        }

        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if (empty($dp[$i][$j])) continue;
                foreach ($dp[$i][$j] as $bal => $_) {
                    // Move right
                    $nj = $j + 1;
                    if ($nj < $n) {
                        $newBal = $bal + ($grid[$i][$nj] === '(' ? 1 : -1);
                        if ($newBal >= 0) {
                            $dp[$i][$nj][$newBal] = true;
                        }
                    }
                    // Move down
                    $ni = $i + 1;
                    if ($ni < $m) {
                        $newBal = $bal + ($grid[$ni][$j] === '(' ? 1 : -1);
                        if ($newBal >= 0) {
                            $dp[$ni][$j][$newBal] = true;
                        }
                    }
                }
            }
        }

        return isset($dp[$m - 1][$n - 1][0]);
    }
}
```

## Swift

```swift
class Solution {
    func hasValidPath(_ grid: [[Character]]) -> Bool {
        let m = grid.count
        let n = grid[0].count
        // If starting cell is ')', impossible to have a valid prefix.
        if grid[0][0] == ")" { return false }
        let maxLen = m + n - 1
        var dp = Array(repeating: Array(repeating: false, count: maxLen + 1), count: m * n)
        func idx(_ i: Int, _ j: Int) -> Int { i * n + j }
        // Starting balance after processing (0,0) which is '('
        dp[0][1] = true
        
        for i in 0..<m {
            for j in 0..<n {
                let curIdx = idx(i, j)
                for bal in 0...maxLen where dp[curIdx][bal] {
                    // Move right
                    if j + 1 < n {
                        let nb = grid[i][j + 1] == "(" ? bal + 1 : bal - 1
                        if nb >= 0 && nb <= maxLen {
                            dp[idx(i, j + 1)][nb] = true
                        }
                    }
                    // Move down
                    if i + 1 < m {
                        let nb = grid[i + 1][j] == "(" ? bal + 1 : bal - 1
                        if nb >= 0 && nb <= maxLen {
                            dp[idx(i + 1, j)][nb] = true
                        }
                    }
                }
            }
        }
        return dp[idx(m - 1, n - 1)][0]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun hasValidPath(grid: Array<CharArray>): Boolean {
        val m = grid.size
        val n = grid[0].size
        val maxBal = m + n // maximum possible balance
        val dp = Array(m) { Array(n) { BooleanArray(maxBal + 1) } }

        // Initialize start cell
        if (grid[0][0] == '(') {
            dp[0][0][1] = true
        } else {
            return false
        }

        for (i in 0 until m) {
            for (j in 0 until n) {
                if (i == 0 && j == 0) continue
                val ch = grid[i][j]
                val curArr = dp[i][j]

                // From top cell
                if (i > 0) {
                    val prevArr = dp[i - 1][j]
                    for (bal in 0..maxBal) {
                        if (!prevArr[bal]) continue
                        val nb = bal + if (ch == '(') 1 else -1
                        if (nb >= 0 && nb <= maxBal) {
                            curArr[nb] = true
                        }
                    }
                }

                // From left cell
                if (j > 0) {
                    val prevArr = dp[i][j - 1]
                    for (bal in 0..maxBal) {
                        if (!prevArr[bal]) continue
                        val nb = bal + if (ch == '(') 1 else -1
                        if (nb >= 0 && nb <= maxBal) {
                            curArr[nb] = true
                        }
                    }
                }
            }
        }

        return dp[m - 1][n - 1][0]
    }
}
```

## Dart

```dart
class Solution {
  bool hasValidPath(List<List<String>> grid) {
    int m = grid.length;
    int n = grid[0].length;
    int maxLen = m + n - 1;
    int maxBal = maxLen; // maximum possible balance

    // dp[i][j][b] == true if we can reach cell (i,j) with balance b
    List<List<List<bool>>> dp = List.generate(
        m, (_) => List.generate(n, (_) => List.filled(maxBal + 1, false)));

    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        String c = grid[i][j];
        if (i == 0 && j == 0) {
          // start cell
          if (c == '(') dp[0][0][1] = true;
          continue;
        }

        List<bool> cur = dp[i][j];

        // from top
        if (i > 0) {
          List<bool> prevTop = dp[i - 1][j];
          for (int bPrev = 0; bPrev <= maxBal; ++bPrev) {
            if (!prevTop[bPrev]) continue;
            int b = c == '(' ? bPrev + 1 : bPrev - 1;
            if (b >= 0 && b <= maxBal) cur[b] = true;
          }
        }

        // from left
        if (j > 0) {
          List<bool> prevLeft = dp[i][j - 1];
          for (int bPrev = 0; bPrev <= maxBal; ++bPrev) {
            if (!prevLeft[bPrev]) continue;
            int b = c == '(' ? bPrev + 1 : bPrev - 1;
            if (b >= 0 && b <= maxBal) cur[b] = true;
          }
        }
      }
    }

    return dp[m - 1][n - 1][0];
  }
}
```

## Golang

```go
func hasValidPath(grid [][]byte) bool {
	m, n := len(grid), len(grid[0])
	maxBal := m + n // upper bound for balance

	// dp[i][j][k] == true if we can reach cell (i,j) with balance k
	dp := make([][][]bool, m)
	for i := 0; i < m; i++ {
		dp[i] = make([][]bool, n)
		for j := 0; j < n; j++ {
			dp[i][j] = make([]bool, maxBal+1)
		}
	}

	// start cell must be '('
	if grid[0][0] != '(' {
		return false
	}
	dp[0][0][1] = true // balance 1 after first '('

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if i == 0 && j == 0 {
				continue
			}
			cur := grid[i][j]
			// from top
			if i > 0 {
				prev := dp[i-1][j]
				for bal := 0; bal <= maxBal; bal++ {
					if !prev[bal] {
						continue
					}
					newBal := bal
					if cur == '(' {
						newBal = bal + 1
					} else { // ')'
						if bal == 0 {
							continue
						}
						newBal = bal - 1
					}
					if newBal <= maxBal {
						dp[i][j][newBal] = true
					}
				}
			}
			// from left
			if j > 0 {
				prev := dp[i][j-1]
				for bal := 0; bal <= maxBal; bal++ {
					if !prev[bal] {
						continue
					}
					newBal := bal
					if cur == '(' {
						newBal = bal + 1
					} else { // ')'
						if bal == 0 {
							continue
						}
						newBal = bal - 1
					}
					if newBal <= maxBal {
						dp[i][j][newBal] = true
					}
				}
			}
		}
	}

	return dp[m-1][n-1][0]
}
```

## Ruby

```ruby
def has_valid_path(grid)
  m = grid.size
  n = grid[0].size
  max_len = m + n # maximum possible balance
  dp = Array.new(m) { Array.new(n) { Array.new(max_len + 1, false) } }

  start_bal = grid[0][0] == '(' ? 1 : -1
  return false if start_bal < 0
  dp[0][0][start_bal] = true

  (0...m).each do |i|
    (0...n).each do |j|
      next if i.zero? && j.zero?
      delta = grid[i][j] == '(' ? 1 : -1

      if i > 0
        prev = dp[i - 1][j]
        (0..max_len).each do |b|
          next unless prev[b]
          nb = b + delta
          next if nb < 0 || nb > max_len
          dp[i][j][nb] = true
        end
      end

      if j > 0
        prev = dp[i][j - 1]
        (0..max_len).each do |b|
          next unless prev[b]
          nb = b + delta
          next if nb < 0 || nb > max_len
          dp[i][j][nb] = true
        end
      end
    end
  end

  dp[m - 1][n - 1][0]
end
```

## Scala

```scala
object Solution {
    def hasValidPath(grid: Array[Array[Char]]): Boolean = {
        val m = grid.length
        val n = grid(0).length
        // maximum possible balance is path length (m + n)
        val maxBal = m + n
        // dp[i][j][b] == true if we can reach cell (i,j) with balance b
        val dp = Array.ofDim[Boolean](m, n, maxBal + 1)

        // start cell must be '(' to have non-negative balance
        if (grid(0)(0) != '(') return false
        dp(0)(0)(1) = true

        for (i <- 0 until m) {
            for (j <- 0 until n) {
                if (i == 0 && j == 0) {
                    // already initialized
                } else {
                    val delta = if (grid(i)(j) == '(') 1 else -1

                    // from top
                    if (i > 0) {
                        var b = 0
                        while (b <= maxBal) {
                            if (dp(i - 1)(j)(b)) {
                                val nb = b + delta
                                if (nb >= 0 && nb <= maxBal) dp(i)(j)(nb) = true
                            }
                            b += 1
                        }
                    }

                    // from left
                    if (j > 0) {
                        var b = 0
                        while (b <= maxBal) {
                            if (dp(i)(j - 1)(b)) {
                                val nb = b + delta
                                if (nb >= 0 && nb <= maxBal) dp(i)(j)(nb) = true
                            }
                            b += 1
                        }
                    }
                }
            }
        }

        dp(m - 1)(n - 1)(0)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn has_valid_path(grid: Vec<Vec<char>>) -> bool {
        let m = grid.len();
        if m == 0 {
            return false;
        }
        let n = grid[0].len();
        // Upper bound for balance (cannot exceed total steps)
        let max_bal = m + n;
        // The path must start with '('
        if grid[0][0] != '(' {
            return false;
        }
        let mut dp = vec![vec![vec![false; max_bal + 1]; n]; m];
        dp[0][0][1] = true; // balance after first '('

        for i in 0..m {
            for j in 0..n {
                for b in 0..=max_bal {
                    if !dp[i][j][b] {
                        continue;
                    }
                    // Move down
                    if i + 1 < m {
                        let c = grid[i + 1][j];
                        let nb = if c == '(' {
                            b + 1
                        } else {
                            if b == 0 { continue; } else { b - 1 }
                        };
                        if nb <= max_bal {
                            dp[i + 1][j][nb] = true;
                        }
                    }
                    // Move right
                    if j + 1 < n {
                        let c = grid[i][j + 1];
                        let nb = if c == '(' {
                            b + 1
                        } else {
                            if b == 0 { continue; } else { b - 1 }
                        };
                        if nb <= max_bal {
                            dp[i][j + 1][nb] = true;
                        }
                    }
                }
            }
        }

        dp[m - 1][n - 1][0]
    }
}
```

## Racket

```racket
(define/contract (has-valid-path grid)
  (-> (listof (listof char?)) boolean?)
  (let* ([rows (length grid)]
         [cols (if (zero? rows) 0 (length (first grid)))]
         [maxBal (+ rows cols -1)])
    (if (= rows 0)
        #f
        (let ([start-char (list-ref (list-ref grid 0) 0)])
          (if (char=? start-char #\))
              #f
              (let* ([dp (make-vector rows)])
                ;; allocate column vectors
                (for ([i (in-range rows)])
                  (vector-set! dp i (make-vector cols)))
                ;; allocate balance vectors for each cell
                (for ([i (in-range rows)]
                      [j (in-range cols)])
                  (vector-set! (vector-ref dp i) j (make-vector (+ maxBal 1) #f)))
                ;; initial balance after first '('
                (let ([start-bal 1])
                  (vector-set! (vector-ref (vector-ref dp 0) 0) start-bal #t))
                ;; DP propagation
                (for ([i (in-range rows)])
                  (for ([j (in-range cols)])
                    (let ([bal-vec (vector-ref (vector-ref dp i) j)])
                      (for ([bal (in-range (+ maxBal 1))])
                        (when (vector-ref bal-vec bal)
                          ;; move down
                          (when (< i (- rows 1))
                            (let* ([c (list-ref (list-ref grid (+ i 1)) j)]
                                   [new-bal (if (char=? c #\() (+ bal 1) (- bal 1))])
                              (when (and (>= new-bal 0) (<= new-bal maxBal))
                                (vector-set! (vector-ref (vector-ref dp (+ i 1)) j)
                                             new-bal
                                             #t))))
                          ;; move right
                          (when (< j (- cols 1))
                            (let* ([c (list-ref (list-ref grid i) (+ j 1))]
                                   [new-bal (if (char=? c #\() (+ bal 1) (- bal 1))])
                              (when (and (>= new-bal 0) (<= new-bal maxBal))
                                (vector-set! (vector-ref (vector-ref dp i) (+ j 1))
                                             new-bal
                                             #t))))))))))
                ;; check if zero balance reachable at bottom‑right
                (let ([final-vec (vector-ref (vector-ref dp (- rows 1)) (- cols 1))])
                  (vector-ref final-vec 0)))))))
```

## Erlang

```erlang
-spec has_valid_path(Grid :: [[char()]]) -> boolean().
has_valid_path(Grid) ->
    M = length(Grid),
    N = length(lists:nth(1, Grid)),
    case get_char(Grid, 0, 0) of
        $) -> false;
        $( ->
            StartSet = sets:add_element(1, sets:new()),
            DP0 = maps:put({0,0}, StartSet, #{}),
            DP = fill_rows(0, M, N, Grid, DP0),
            case maps:get({M-1,N-1}, DP, undefined) of
                undefined -> false;
                EndSet -> sets:is_element(0, EndSet)
            end
    end.

fill_rows(I, M, _N, _Grid, DP) when I >= M ->
    DP;
fill_rows(I, M, N, Grid, DP) ->
    DP1 = fill_cols(I, 0, N, Grid, DP),
    fill_rows(I + 1, M, N, Grid, DP1).

fill_cols(_I, J, N, _Grid, DP) when J >= N ->
    DP;
fill_cols(I, J, N, Grid, DP) ->
    case {I,J} of
        {0,0} ->
            fill_cols(I, J + 1, N, Grid, DP);
        _ ->
            Char = get_char(Grid, I, J),
            SetTop   = if I > 0 -> maps:get({I-1,J}, DP, undefined); true -> undefined end,
            SetLeft  = if J > 0 -> maps:get({I,J-1}, DP, undefined); true -> undefined end,
            NewSet = combine_sets(SetTop, SetLeft, Char),
            DP2 = case sets:size(NewSet) of
                      0 -> DP;
                      _ -> maps:put({I,J}, NewSet, DP)
                  end,
            fill_cols(I, J + 1, N, Grid, DP2)
    end.

combine_sets(undefined, undefined, _Char) ->
    sets:new();
combine_sets(SetPrev, undefined, Char) ->
    apply_char_set(SetPrev, Char);
combine_sets(undefined, SetPrev, Char) ->
    apply_char_set(SetPrev, Char);
combine_sets(Set1, Set2, Char) ->
    S1 = apply_char_set(Set1, Char),
    S2 = apply_char_set(Set2, Char),
    sets:union(S1, S2).

apply_char_set(SetPrev, Char) ->
    lists:foldl(
        fun(Bal, Acc) ->
            NewBal = if Char == $( -> Bal + 1; true -> Bal - 1 end,
            case NewBal >= 0 of
                true -> sets:add_element(NewBal, Acc);
                false -> Acc
            end
        end,
        sets:new(),
        sets:to_list(SetPrev)
    ).

get_char(Grid, I, J) ->
    Row = lists:nth(I + 1, Grid),
    Cell = lists:nth(J + 1, Row),
    case Cell of
        [C] -> C;
        C when is_integer(C) -> C
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec has_valid_path(grid :: [[String.t()]]) :: boolean
  def has_valid_path(grid) do
    import Bitwise

    n = length(hd(grid))
    # previous row masks, initially all zero
    prev = :erlang.make_tuple(n, 0)

    final_prev =
      Enum.with_index(grid)
      |> Enum.reduce(prev, fn {row, i}, prev_acc ->
        cur_initial = :erlang.make_tuple(n, 0)

        {cur, _} =
          Enum.reduce(0..(n - 1), {cur_initial, 0}, fn j, {c_acc, left_mask} ->
            top_mask = if i == 0, do: 0, else: elem(prev_acc, j)

            combined =
              cond do
                i == 0 and j == 0 -> 1
                i == 0 -> left_mask
                j == 0 -> top_mask
                true -> Bitwise.bor(top_mask, left_mask)
              end

            ch = Enum.at(row, j)

            mask =
              if ch == "(" do
                combined <<< 1
              else
                combined >>> 1
              end

            {put_elem(c_acc, j, mask), mask}
          end)

        cur
      end)

    final_mask = elem(final_prev, n - 1)
    (final_mask &&& 1) != 0
  end
end
```
