# 2209. Minimum White Tiles After Covering With Carpets

## Cpp

```cpp
class Solution {
public:
    int minimumWhiteTiles(string floor, int numCarpets, int carpetLen) {
        int n = floor.size();
        const int INF = 1e9;
        vector<vector<int>> dp(n + 1, vector<int>(numCarpets + 1, INF));
        for (int j = 0; j <= numCarpets; ++j) dp[0][j] = 0;
        for (int i = 1; i <= n; ++i) {
            int isWhite = floor[i - 1] == '0' ? 1 : 0;
            for (int j = 0; j <= numCarpets; ++j) {
                // not placing carpet ending at i-1
                dp[i][j] = dp[i - 1][j] + isWhite;
                if (j > 0) {
                    int prev = max(0, i - carpetLen);
                    dp[i][j] = min(dp[i][j], dp[prev][j - 1]);
                }
            }
        }
        return dp[n][numCarpets];
    }
};
```

## Java

```java
class Solution {
    public int minimumWhiteTiles(String floor, int numCarpets, int carpetLen) {
        int n = floor.length();
        int INF = 1_000_000_0;
        int[][] dp = new int[n + 1][numCarpets + 1];
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= numCarpets; j++) {
                dp[i][j] = INF;
            }
        }
        // zero tiles need zero uncovered whites regardless of carpets used
        for (int j = 0; j <= numCarpets; j++) {
            dp[0][j] = 0;
        }

        for (int i = 1; i <= n; i++) {
            int isWhite = floor.charAt(i - 1) == '0' ? 1 : 0;
            for (int j = 0; j <= numCarpets; j++) {
                // option 1: do not place a carpet ending at i-1
                dp[i][j] = dp[i - 1][j] + isWhite;

                // option 2: place a carpet covering [i-carpetLen, i-1]
                if (j > 0) {
                    int start = Math.max(0, i - carpetLen);
                    dp[i][j] = Math.min(dp[i][j], dp[start][j - 1]);
                }
            }
        }

        return dp[n][numCarpets];
    }
}
```

## Python

```python
class Solution(object):
    def minimumWhiteTiles(self, floor, numCarpets, carpetLen):
        """
        :type floor: str
        :type numCarpets: int
        :type carpetLen: int
        :rtype: int
        """
        n = len(floor)
        # prefix sum of white tiles ('0')
        pre = [0] * (n + 1)
        for i, ch in enumerate(floor):
            pre[i + 1] = pre[i] + (ch == '0')
        total_white = pre[n]

        # dp[k][i]: max white tiles covered using k carpets within first i tiles
        dp = [[0] * (n + 1) for _ in range(numCarpets + 1)]

        for k in range(1, numCarpets + 1):
            for i in range(1, n + 1):
                # option 1: do not place a carpet ending at i-1
                best = dp[k][i - 1]
                # option 2: place a carpet covering [start, i-1]
                start = i - carpetLen
                if start < 0:
                    start = 0
                covered = pre[i] - pre[start]
                cand = dp[k - 1][start] + covered
                if cand > best:
                    best = cand
                dp[k][i] = best

        max_covered = dp[numCarpets][n]
        return total_white - max_covered
```

## Python3

```python
class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        # prefix count of white tiles ('0')
        pre = [0] * (n + 1)
        for i in range(1, n + 1):
            pre[i] = pre[i - 1] + (floor[i - 1] == '0')

        INF = 10 ** 9
        dp = [[INF] * (numCarpets + 1) for _ in range(n + 1)]
        for j in range(numCarpets + 1):
            dp[0][j] = 0

        for i in range(1, n + 1):
            dp[i][0] = pre[i]
            for j in range(1, numCarpets + 1):
                # option 1: do not place a carpet ending at i-1
                opt1 = dp[i - 1][j] + (floor[i - 1] == '0')
                # option 2: place a carpet covering up to i-1
                prev = max(0, i - carpetLen)
                opt2 = dp[prev][j - 1]
                dp[i][j] = min(opt1, opt2)

        return dp[n][numCarpets]
```

## C

```c
int minimumWhiteTiles(char* floor, int numCarpets, int carpetLen) {
    int n = strlen(floor);
    static int pref[1005];
    for (int i = 1; i <= n; ++i) {
        pref[i] = pref[i - 1] + (floor[i - 1] == '0');
    }
    static int dp[1005][1005]; // automatically zero-initialized
    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j <= numCarpets; ++j) {
            int best = dp[i - 1][j];
            if (j > 0) {
                int left = i - carpetLen;
                if (left < 0) left = 0;
                int covered = pref[i] - pref[left];
                int cand = dp[left][j - 1] + covered;
                if (cand > best) best = cand;
            }
            dp[i][j] = best;
        }
    }
    return pref[n] - dp[n][numCarpets];
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumWhiteTiles(string floor, int numCarpets, int carpetLen) {
        int n = floor.Length;
        int[,] dp = new int[n + 1, numCarpets + 1];
        const int INF = 1000000; // larger than any possible answer

        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= numCarpets; j++) {
                dp[i, j] = INF;
            }
        }

        for (int j = 0; j <= numCarpets; j++) {
            dp[0, j] = 0; // no tiles -> zero white tiles visible
        }

        for (int i = 1; i <= n; i++) {
            int isWhite = floor[i - 1] == '0' ? 1 : 0;
            for (int j = 0; j <= numCarpets; j++) {
                // Option 1: do not place a carpet ending at position i-1
                dp[i, j] = dp[i - 1, j] + isWhite;

                // Option 2: place a carpet covering [i-carpetLen, i)
                if (j > 0) {
                    int prevIdx = i - carpetLen;
                    if (prevIdx < 0) prevIdx = 0;
                    dp[i, j] = Math.Min(dp[i, j], dp[prevIdx, j - 1]);
                }
            }
        }

        return dp[n, numCarpets];
    }
}
```

## Javascript

```javascript
/**
 * @param {string} floor
 * @param {number} numCarpets
 * @param {number} carpetLen
 * @return {number}
 */
var minimumWhiteTiles = function(floor, numCarpets, carpetLen) {
    const n = floor.length;
    const INF = Number.MAX_SAFE_INTEGER;
    // dp[i][j]: min uncovered white tiles for first i characters using j carpets
    const dp = Array.from({ length: n + 1 }, () => new Array(numCarpets + 1).fill(INF));
    for (let j = 0; j <= numCarpets; ++j) dp[0][j] = 0;
    
    for (let i = 1; i <= n; ++i) {
        const isWhite = floor[i - 1] === '0' ? 1 : 0;
        for (let j = 0; j <= numCarpets; ++j) {
            // option 1: do not place a carpet ending at i-1
            dp[i][j] = dp[i - 1][j] + isWhite;
            // option 2: place a carpet that ends at i-1 (covers up to carpetLen tiles)
            if (j > 0) {
                const prevIdx = i - carpetLen >= 0 ? i - carpetLen : 0;
                dp[i][j] = Math.min(dp[i][j], dp[prevIdx][j - 1]);
            }
        }
    }
    
    return dp[n][numCarpets];
};
```

## Typescript

```typescript
function minimumWhiteTiles(floor: string, numCarpets: number, carpetLen: number): number {
    const n = floor.length;
    const prefix = new Array(n + 1).fill(0);
    for (let i = 1; i <= n; i++) {
        prefix[i] = prefix[i - 1] + (floor[i - 1] === '0' ? 1 : 0);
    }

    const INF = 1 << 30;
    const dp: number[][] = Array.from({ length: numCarpets + 1 }, () => new Array(n + 1).fill(INF));

    // No carpets used
    for (let i = 0; i <= n; i++) {
        dp[0][i] = prefix[i];
    }

    for (let c = 1; c <= numCarpets; c++) {
        dp[c][0] = 0;
        for (let i = 1; i <= n; i++) {
            const notCover = dp[c][i - 1] + (floor[i - 1] === '0' ? 1 : 0);
            const startIdx = Math.max(0, i - carpetLen);
            const cover = dp[c - 1][startIdx];
            dp[c][i] = notCover < cover ? notCover : cover;
        }
    }

    return dp[numCarpets][n];
}
```

## Php

```php
class Solution {

    /**
     * @param String $floor
     * @param Integer $numCarpets
     * @param Integer $carpetLen
     * @return Integer
     */
    function minimumWhiteTiles($floor, $numCarpets, $carpetLen) {
        $n = strlen($floor);
        // dp[i][c] = min uncovered white tiles for first i characters using c carpets
        $dp = array_fill(0, $n + 1, array_fill(0, $numCarpets + 1, 0));

        // Base case: no carpets
        for ($i = 1; $i <= $n; $i++) {
            $dp[$i][0] = $dp[$i - 1][0] + ($floor[$i - 1] === '0' ? 1 : 0);
        }

        // Fill DP table
        for ($i = 1; $i <= $n; $i++) {
            $isWhite = ($floor[$i - 1] === '0') ? 1 : 0;
            for ($c = 1; $c <= $numCarpets; $c++) {
                // Option 1: do not place a carpet covering position i
                $best = $dp[$i - 1][$c] + $isWhite;

                // Option 2: place a carpet ending at i (covers up to carpetLen tiles)
                $prevIdx = $i - $carpetLen;
                if ($prevIdx < 0) {
                    $prevIdx = 0;
                }
                $best = min($best, $dp[$prevIdx][$c - 1]);

                $dp[$i][$c] = $best;
            }
        }

        return $dp[$n][$numCarpets];
    }
}
```

## Swift

```swift
class Solution {
    func minimumWhiteTiles(_ floor: String, _ numCarpets: Int, _ carpetLen: Int) -> Int {
        let n = floor.count
        let chars = Array(floor)
        let INF = Int.max / 2
        
        var dp = [[Int]](repeating: [Int](repeating: INF, count: numCarpets + 1), count: n + 1)
        for k in 0...numCarpets {
            dp[0][k] = 0
        }
        
        for i in 1...n {
            let isWhite = chars[i - 1] == "0" ? 1 : 0
            for k in 0...numCarpets {
                var best = dp[i - 1][k] + isWhite   // leave tile uncovered
                if k > 0 {
                    let start = max(0, i - carpetLen)
                    best = min(best, dp[start][k - 1]) // place a carpet covering [start, i)
                }
                dp[i][k] = best
            }
        }
        
        return dp[n][numCarpets]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumWhiteTiles(floor: String, numCarpets: Int, carpetLen: Int): Int {
        val n = floor.length
        val white = IntArray(n) { if (floor[it] == '0') 1 else 0 }
        val INF = 1_000_000
        val dp = Array(n + 1) { IntArray(numCarpets + 1) { INF } }
        for (j in 0..numCarpets) {
            dp[0][j] = 0
        }
        for (i in 1..n) {
            for (j in 0..numCarpets) {
                // Do not place a carpet covering position i-1
                dp[i][j] = dp[i - 1][j] + white[i - 1]
                if (j > 0) {
                    val prev = if (i - carpetLen >= 0) i - carpetLen else 0
                    dp[i][j] = kotlin.math.min(dp[i][j], dp[prev][j - 1])
                }
            }
        }
        return dp[n][numCarpets]
    }
}
```

## Dart

```dart
class Solution {
  int minimumWhiteTiles(String floor, int numCarpets, int carpetLen) {
    int n = floor.length;
    const int INF = 1 << 30;

    // dp[i][c] = min uncovered white tiles in first i positions using c carpets
    List<List<int>> dp = List.generate(n + 1,
        (_) => List.filled(numCarpets + 1, INF));

    for (int c = 0; c <= numCarpets; ++c) {
      dp[0][c] = 0;
    }

    for (int i = 1; i <= n; ++i) {
      int isWhite = floor.codeUnitAt(i - 1) == 48 ? 1 : 0; // '0' -> white
      for (int c = 0; c <= numCarpets; ++c) {
        // Option 1: do not place a carpet ending at i-1
        dp[i][c] = dp[i - 1][c] + isWhite;

        // Option 2: place a carpet covering [i-carpetLen, i)
        if (c > 0) {
          int start = i - carpetLen;
          if (start < 0) start = 0;
          if (dp[start][c - 1] < dp[i][c]) {
            dp[i][c] = dp[start][c - 1];
          }
        }
      }
    }

    return dp[n][numCarpets];
  }
}
```

## Golang

```go
func minimumWhiteTiles(floor string, numCarpets int, carpetLen int) int {
    n := len(floor)
    const INF = int(1e9)

    dp := make([][]int, n+1)
    for i := 0; i <= n; i++ {
        dp[i] = make([]int, numCarpets+1)
        for j := 0; j <= numCarpets; j++ {
            dp[i][j] = INF
        }
    }
    for j := 0; j <= numCarpets; j++ {
        dp[0][j] = 0
    }

    for i := 1; i <= n; i++ {
        isWhite := 0
        if floor[i-1] == '0' {
            isWhite = 1
        }
        for j := 0; j <= numCarpets; j++ {
            // Do not place a carpet ending at position i-1
            if dp[i-1][j]+isWhite < dp[i][j] {
                dp[i][j] = dp[i-1][j] + isWhite
            }
            // Place a carpet covering up to carpetLen tiles ending at i-1
            if j > 0 {
                start := i - carpetLen
                if start < 0 {
                    start = 0
                }
                if dp[start][j-1] < dp[i][j] {
                    dp[i][j] = dp[start][j-1]
                }
            }
        }
    }

    return dp[n][numCarpets]
}
```

## Ruby

```ruby
def minimum_white_tiles(floor, num_carpets, carpet_len)
  n = floor.length
  pref = Array.new(n + 1, 0)
  (1..n).each do |i|
    pref[i] = pref[i - 1] + (floor[i - 1] == '0' ? 1 : 0)
  end

  dp = Array.new(num_carpets + 1) { Array.new(n + 1, 0) }

  (0..n).each do |i|
    dp[0][i] = pref[i]
  end

  (1..num_carpets).each do |j|
    dp[j][0] = 0
    (1..n).each do |i|
      # option: don't place a carpet ending at i-1
      best = dp[j][i - 1] + (floor[i - 1] == '0' ? 1 : 0)
      left = i - carpet_len
      left = 0 if left < 0
      # option: place a carpet covering [left, i)
      best = [best, dp[j - 1][left]].min
      dp[j][i] = best
    end
  end

  dp[num_carpets][n]
end
```

## Scala

```scala
object Solution {
    def minimumWhiteTiles(floor: String, numCarpets: Int, carpetLen: Int): Int = {
        val n = floor.length
        val pre = new Array[Int](n + 1)
        for (i <- 0 until n) {
            pre(i + 1) = pre(i) + (if (floor.charAt(i) == '0') 1 else 0)
        }
        val dp = Array.ofDim[Int](n + 1, numCarpets + 1)
        for (i <- 1 to n) {
            for (c <- 1 to numCarpets) {
                val without = dp(i - 1)(c)
                val start = math.max(0, i - carpetLen)
                val whites = pre(i) - pre(start)
                val withCarpet = dp(start)(c - 1) + whites
                dp(i)(c) = math.max(without, withCarpet)
            }
        }
        val totalWhite = pre(n)
        totalWhite - dp(n)(numCarpets)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_white_tiles(floor: String, num_carpets: i32, carpet_len: i32) -> i32 {
        let n = floor.len();
        let m = num_carpets as usize;
        let l = carpet_len as usize;
        let bytes = floor.as_bytes();

        // dp[i][k] = min uncovered whites for first i tiles using k carpets
        let mut dp = vec![vec![i32::MAX / 2; m + 1]; n + 1];
        for k in 0..=m {
            dp[0][k] = 0;
        }

        for i in 1..=n {
            let is_white = if bytes[i - 1] == b'0' { 1 } else { 0 };
            for k in 0..=m {
                // option: do not place carpet ending at i
                dp[i][k] = dp[i - 1][k] + is_white;
                // option: place a carpet covering up to L tiles ending at i
                if k > 0 {
                    let start = if i >= l { i - l } else { 0 };
                    let candidate = dp[start][k - 1];
                    if candidate < dp[i][k] {
                        dp[i][k] = candidate;
                    }
                }
            }
        }

        dp[n][m]
    }
}
```

## Racket

```racket
(define/contract (minimum-white-tiles floor numCarpets carpetLen)
  (-> string? exact-integer? exact-integer? exact-integer?)
  (let* ([n (string-length floor)]
         [pref (make-vector (+ n 1) 0)])
    ;; prefix sum of white tiles ('0')
    (for ([i (in-range n)])
      (define w (if (char=? (string-ref floor i) #\0) 1 0))
      (vector-set! pref (add1 i) (+ (vector-ref pref i) w)))
    ;; DP rows: rows[c][i] = min uncovered whites for first i tiles using c carpets
    (define rows (make-vector (add1 numCarpets)))
    ;; row 0: no carpet
    (define row0 (make-vector (add1 n) 0))
    (for ([i (in-range (add1 n))])
      (vector-set! row0 i (vector-ref pref i))) ; uncovered whites = total whites so far
    (vector-set! rows 0 row0)
    ;; compute for each number of carpets
    (for ([c (in-range 1 (add1 numCarpets))])
      (define prev (vector-ref rows (sub1 c)))
      (define cur (make-vector (add1 n) 0))
      (vector-set! cur 0 0)
      (for ([i (in-range 1 (add1 n))])
        (define not-cover
          (+ (vector-ref cur (sub1 i))
             (if (char=? (string-ref floor (sub1 i)) #\0) 1 0)))
        (define cover-idx (max 0 (- i carpetLen)))
        (define cover (vector-ref prev cover-idx))
        (vector-set! cur i (if (< not-cover cover) not-cover cover)))
      (vector-set! rows c cur))
    (vector-ref (vector-ref rows numCarpets) n)))
```

## Erlang

```erlang
-module(solution).
-export([minimum_white_tiles/3]).

-spec minimum_white_tiles(Floor :: unicode:unicode_binary(), NumCarpets :: integer(), CarpetLen :: integer()) -> integer().
minimum_white_tiles(Floor, NumCarpets, CarpetLen) ->
    N = byte_size(Floor),
    FloorList = binary:bin_to_list(Floor),

    % prefix sum of white tiles ('0')
    {_, RevPref} = lists:foldl(fun(Char, {Prev, Acc}) ->
        New = Prev + if Char == $0 -> 1; true -> 0 end,
        {New, [New | Acc]}
    end, {0, []}, FloorList),
    PrefList = [0 | lists:reverse(RevPref)],
    PrefTuple = list_to_tuple(PrefList),

    TotalWhite = element(N + 1, PrefTuple),

    ZeroRow = list_to_tuple(lists:duplicate(NumCarpets + 1, 0)),
    DP0 = array:new(N + 1, [{default, ZeroRow}]),

    Loop = fun F(Idx, DPAcc) when Idx < 0 ->
                DPAcc;
            F(Idx, DPAcc) ->
                RowNext = array:get(Idx + 1, DPAcc),
                CoverEnd = erlang:min(Idx + CarpetLen, N),

                PrefI = element(Idx + 1, PrefTuple),
                PrefCover = element(CoverEnd + 1, PrefTuple),
                CoveredWhite = PrefCover - PrefI,

                RowCover = array:get(CoverEnd, DPAcc),

                Values = [0 |
                    [max(element(K + 1, RowNext), CoveredWhite + element(K, RowCover))
                     || K <- lists:seq(1, NumCarpets)]],
                NewRow = list_to_tuple(Values),
                F(Idx - 1, array:set(Idx, NewRow, DPAcc))
        end,
    DPF = Loop(N - 1, DP0),

    MaxCovered = element(NumCarpets + 1, array:get(0, DPF)),
    TotalWhite - MaxCovered.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_white_tiles(floor :: String.t, num_carpets :: integer, carpet_len :: integer) :: integer
  def minimum_white_tiles(floor, num_carpets, carpet_len) do
    n = String.length(floor)
    chars = String.graphemes(floor)

    row_len = num_carpets + 1
    base_row = :array.from_list(List.duplicate(0, row_len))
    rows0 = :array.set(0, base_row, :array.new(n + 1))

    max_val = n + 5

    final_rows =
      Enum.reduce(1..n, rows0, fn i, rows_acc ->
        is_white = if Enum.at(chars, i - 1) == "0", do: 1, else: 0
        prev_row = :array.get(i - 1, rows_acc)

        new_row =
          Enum.reduce(0..num_carpets, :array.new(row_len), fn j, row_acc ->
            opt1 = (:array.get(j, prev_row) + is_white)

            opt2 =
              if j > 0 do
                start = max(0, i - carpet_len)
                start_row = :array.get(start, rows_acc)
                :array.get(j - 1, start_row)
              else
                max_val
              end

            best = if opt1 < opt2, do: opt1, else: opt2
            :array.set(j, best, row_acc)
          end)

        :array.set(i, new_row, rows_acc)
      end)

    final_rows
    |> :array.get(n)
    |> :array.get(num_carpets)
  end
end
```
