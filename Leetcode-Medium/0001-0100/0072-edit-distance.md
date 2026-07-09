# 0072. Edit Distance

## Cpp

```cpp
class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.size();
        int n = word2.size();
        vector<int> prev(n + 1), cur(n + 1);
        for (int j = 0; j <= n; ++j) prev[j] = j;
        for (int i = 1; i <= m; ++i) {
            cur[0] = i;
            for (int j = 1; j <= n; ++j) {
                if (word1[i - 1] == word2[j - 1]) {
                    cur[j] = prev[j - 1];
                } else {
                    cur[j] = 1 + min({prev[j - 1], prev[j], cur[j - 1]});
                }
            }
            swap(prev, cur);
        }
        return prev[n];
    }
};
```

## Java

```java
class Solution {
    public int minDistance(String word1, String word2) {
        int m = word1.length();
        int n = word2.length();
        int[][] dp = new int[m + 1][n + 1];
        
        for (int i = 0; i <= m; i++) {
            dp[i][0] = i;
        }
        for (int j = 0; j <= n; j++) {
            dp[0][j] = j;
        }
        
        for (int i = 1; i <= m; i++) {
            char c1 = word1.charAt(i - 1);
            for (int j = 1; j <= n; j++) {
                char c2 = word2.charAt(j - 1);
                if (c1 == c2) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    int replace = dp[i - 1][j - 1];
                    int delete = dp[i - 1][j];
                    int insert = dp[i][j - 1];
                    dp[i][j] = 1 + Math.min(replace, Math.min(delete, insert));
                }
            }
        }
        
        return dp[m][n];
    }
}
```

## Python

```python
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        if m < n:
            # ensure that we use O(min(m,n)) space by swapping
            word1, word2 = word2, word1
            m, n = n, m
        # now n <= m, dp size is n+1
        prev = list(range(n + 1))
        for i in range(1, m + 1):
            cur = [i] + [0] * n
            w1_char = word1[i - 1]
            for j in range(1, n + 1):
                if w1_char == word2[j - 1]:
                    cur[j] = prev[j - 1]
                else:
                    cur[j] = 1 + min(prev[j],      # deletion
                                    cur[j - 1],   # insertion
                                    prev[j - 1])  # replacement
            prev = cur
        return prev[n]
```

## Python3

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # Ensure the smaller string is used for columns to save space
        if n > m:
            word1, word2 = word2, word1
            m, n = n, m

        prev = list(range(n + 1))
        for i in range(1, m + 1):
            cur = [i] + [0] * n
            c1 = word1[i - 1]
            for j in range(1, n + 1):
                if c1 == word2[j - 1]:
                    cur[j] = prev[j - 1]
                else:
                    cur[j] = 1 + min(prev[j],      # deletion
                                    cur[j - 1],   # insertion
                                    prev[j - 1])  # replacement
            prev = cur
        return prev[n]
```

## C

```c
#include <stdlib.h>
#include <string.h>

static inline int min3(int a, int b, int c) {
    if (a < b) return a < c ? a : c;
    return b < c ? b : c;
}

int minDistance(char* word1, char* word2) {
    size_t len1 = strlen(word1);
    size_t len2 = strlen(word2);
    
    // Ensure the smaller string is used for column dimension to save memory
    if (len2 > len1) {
        // swap pointers and lengths
        char *tmpStr = word1;
        word1 = word2;
        word2 = tmpStr;
        size_t tmpLen = len1;
        len1 = len2;
        len2 = tmpLen;
    }
    
    int *prev = (int *)malloc((len2 + 1) * sizeof(int));
    int *cur  = (int *)malloc((len2 + 1) * sizeof(int));
    if (!prev || !cur) {
        // allocation failure, though unlikely in LeetCode environment
        free(prev);
        free(cur);
        return 0;
    }
    
    for (size_t j = 0; j <= len2; ++j)
        prev[j] = (int)j;
    
    for (size_t i = 1; i <= len1; ++i) {
        cur[0] = (int)i;
        char c1 = word1[i - 1];
        for (size_t j = 1; j <= len2; ++j) {
            char c2 = word2[j - 1];
            int cost = (c1 == c2) ? prev[j - 1] : prev[j - 1] + 1;
            cur[j] = min3(cost, prev[j] + 1, cur[j - 1] + 1);
        }
        // swap rows
        int *tmp = prev;
        prev = cur;
        cur = tmp;
    }
    
    int result = prev[len2];
    free(prev);
    free(cur);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinDistance(string word1, string word2)
    {
        int m = word1.Length;
        int n = word2.Length;

        // If one of the strings is empty
        if (m == 0) return n;
        if (n == 0) return m;

        int[,] dp = new int[m + 1, n + 1];

        for (int i = 0; i <= m; i++)
            dp[i, 0] = i;
        for (int j = 0; j <= n; j++)
            dp[0, j] = j;

        for (int i = 1; i <= m; i++)
        {
            char c1 = word1[i - 1];
            for (int j = 1; j <= n; j++)
            {
                char c2 = word2[j - 1];
                if (c1 == c2)
                {
                    dp[i, j] = dp[i - 1, j - 1];
                }
                else
                {
                    int insert = dp[i, j - 1] + 1;
                    int delete = dp[i - 1, j] + 1;
                    int replace = dp[i - 1, j - 1] + 1;
                    dp[i, j] = Math.Min(insert, Math.Min(delete, replace));
                }
            }
        }

        return dp[m, n];
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var minDistance = function(word1, word2) {
    const m = word1.length;
    const n = word2.length;
    
    // If one of the strings is empty
    if (m === 0) return n;
    if (n === 0) return m;
    
    // Use two rows to save space
    let prev = new Array(n + 1);
    for (let j = 0; j <= n; ++j) {
        prev[j] = j; // insert all characters of word2 into empty string
    }
    
    for (let i = 1; i <= m; ++i) {
        const curr = new Array(n + 1);
        curr[0] = i; // delete all characters up to i from word1
        
        for (let j = 1; j <= n; ++j) {
            if (word1[i - 1] === word2[j - 1]) {
                curr[j] = prev[j - 1]; // no operation needed
            } else {
                const replaceCost = prev[j - 1];
                const deleteCost = prev[j];
                const insertCost = curr[j - 1];
                curr[j] = 1 + Math.min(replaceCost, deleteCost, insertCost);
            }
        }
        prev = curr;
    }
    
    return prev[n];
};
```

## Typescript

```typescript
function minDistance(word1: string, word2: string): number {
    const m = word1.length;
    const n = word2.length;

    // dp for previous row
    let prev: number[] = new Array(n + 1);
    for (let j = 0; j <= n; ++j) {
        prev[j] = j; // insert all characters of word2 into empty word1
    }

    for (let i = 1; i <= m; ++i) {
        const cur: number[] = new Array(n + 1);
        cur[0] = i; // delete all characters up to i from word1

        for (let j = 1; j <= n; ++j) {
            if (word1[i - 1] === word2[j - 1]) {
                cur[j] = prev[j - 1]; // no operation needed
            } else {
                const replaceCost = prev[j - 1];
                const deleteCost = prev[j];
                const insertCost = cur[j - 1];
                cur[j] = 1 + Math.min(replaceCost, deleteCost, insertCost);
            }
        }

        prev = cur;
    }

    return prev[n];
}
```

## Php

```php
class Solution {

    /**
     * @param String $word1
     * @param String $word2
     * @return Integer
     */
    function minDistance($word1, $word2) {
        $m = strlen($word1);
        $n = strlen($word2);

        // Initialize DP table
        $dp = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));

        for ($i = 0; $i <= $m; $i++) {
            $dp[$i][0] = $i;
        }
        for ($j = 0; $j <= $n; $j++) {
            $dp[0][$j] = $j;
        }

        for ($i = 1; $i <= $m; $i++) {
            $c1 = $word1[$i - 1];
            for ($j = 1; $j <= $n; $j++) {
                $c2 = $word2[$j - 1];
                if ($c1 === $c2) {
                    $dp[$i][$j] = $dp[$i - 1][$j - 1];
                } else {
                    $dp[$i][$j] = 1 + min(
                        $dp[$i - 1][$j],    // deletion
                        $dp[$i][$j - 1],    // insertion
                        $dp[$i - 1][$j - 1] // replacement
                    );
                }
            }
        }

        return $dp[$m][$n];
    }
}
```

## Swift

```swift
class Solution {
    func minDistance(_ word1: String, _ word2: String) -> Int {
        let chars1 = Array(word1)
        let chars2 = Array(word2)
        let m = chars1.count
        let n = chars2.count
        
        var dp = Array(repeating: Array(repeating: 0, count: n + 1), count: m + 1)
        
        for i in 0...m {
            dp[i][0] = i
        }
        for j in 0...n {
            dp[0][j] = j
        }
        
        if m == 0 || n == 0 { return dp[m][n] }
        
        for i in 1...m {
            for j in 1...n {
                if chars1[i - 1] == chars2[j - 1] {
                    dp[i][j] = dp[i - 1][j - 1]
                } else {
                    let deleteCost = dp[i - 1][j]
                    let insertCost = dp[i][j - 1]
                    let replaceCost = dp[i - 1][j - 1]
                    dp[i][j] = 1 + min(deleteCost, insertCost, replaceCost)
                }
            }
        }
        
        return dp[m][n]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minDistance(word1: String, word2: String): Int {
        val m = word1.length
        val n = word2.length
        if (m == 0) return n
        if (n == 0) return m

        // Use the shorter string for DP columns to save space
        var s1 = word1
        var s2 = word2
        var len1 = m
        var len2 = n
        if (n < m) {
            s1 = word2
            s2 = word1
            len1 = n
            len2 = m
        }

        val dp = IntArray(len1 + 1) { it } // dp[j] = j for empty prefix of s2

        for (i in 1..len2) {
            var prev = dp[0]          // dp[i-1][j-1]
            dp[0] = i                 // dp[i][0] = i deletions
            for (j in 1..len1) {
                val temp = dp[j]      // store dp[i-1][j] before overwriting
                if (s2[i - 1] == s1[j - 1]) {
                    dp[j] = prev       // characters match, no operation needed
                } else {
                    dp[j] = 1 + minOf(prev, dp[j - 1], dp[j])
                }
                prev = temp           // move diagonal forward
            }
        }
        return dp[len1]
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int minDistance(String word1, String word2) {
    int m = word1.length;
    int n = word2.length;

    // Ensure the DP array is sized by the shorter string to save space
    if (n > m) {
      // swap to make n <= m
      return minDistance(word2, word1);
    }

    List<int> dp = List.filled(n + 1, 0);
    for (int j = 0; j <= n; ++j) {
      dp[j] = j;
    }

    for (int i = 1; i <= m; ++i) {
      int prevDiagonal = dp[0];
      dp[0] = i;
      for (int j = 1; j <= n; ++j) {
        int temp = dp[j]; // value from previous row (i-1, j)
        if (word1.codeUnitAt(i - 1) == word2.codeUnitAt(j - 1)) {
          dp[j] = prevDiagonal;
        } else {
          dp[j] = 1 + min(prevDiagonal, min(dp[j - 1], dp[j]));
        }
        prevDiagonal = temp;
      }
    }

    return dp[n];
  }
}
```

## Golang

```go
func minDistance(word1 string, word2 string) int {
	m, n := len(word1), len(word2)
	if m == 0 {
		return n
	}
	if n == 0 {
		return m
	}

	dp := make([]int, n+1)
	for j := 0; j <= n; j++ {
		dp[j] = j
	}

	for i := 1; i <= m; i++ {
		prev := dp[0]
		dp[0] = i
		for j := 1; j <= n; j++ {
			temp := dp[j]
			if word1[i-1] == word2[j-1] {
				dp[j] = prev
			} else {
				del, ins, rep := temp, dp[j-1], prev
				minv := del
				if ins < minv {
					minv = ins
				}
				if rep < minv {
					minv = rep
				}
				dp[j] = 1 + minv
			}
			prev = temp
		}
	}
	return dp[n]
}
```

## Ruby

```ruby
def min_distance(word1, word2)
  m = word1.length
  n = word2.length
  return n if m == 0
  return m if n == 0

  dp = Array.new(n + 1) { |j| j }

  (1..m).each do |i|
    prev = dp[0]
    dp[0] = i
    (1..n).each do |j|
      temp = dp[j]
      if word1.getbyte(i - 1) == word2.getbyte(j - 1)
        dp[j] = prev
      else
        dp[j] = 1 + [dp[j], dp[j - 1], prev].min
      end
      prev = temp
    end
  end

  dp[n]
end
```

## Scala

```scala
object Solution {
    def minDistance(word1: String, word2: String): Int = {
        val m = word1.length
        val n = word2.length
        if (m == 0) return n
        if (n == 0) return m

        var prev = new Array[Int](n + 1)
        for (j <- 0 to n) prev(j) = j

        for (i <- 1 to m) {
            val cur = new Array[Int](n + 1)
            cur(0) = i
            for (j <- 1 to n) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    cur(j) = prev(j - 1)
                } else {
                    val replaceCost = prev(j - 1)
                    val deleteCost = prev(j)
                    val insertCost = cur(j - 1)
                    cur(j) = 1 + math.min(replaceCost, math.min(deleteCost, insertCost))
                }
            }
            prev = cur
        }

        prev(n)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_distance(word1: String, word2: String) -> i32 {
        let a = word1.as_bytes();
        let b = word2.as_bytes();
        let m = a.len();
        let n = b.len();
        let mut dp = vec![vec![0usize; n + 1]; m + 1];
        for i in 0..=m {
            dp[i][0] = i;
        }
        for j in 0..=n {
            dp[0][j] = j;
        }
        for i in 1..=m {
            for j in 1..=n {
                if a[i - 1] == b[j - 1] {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    let del = dp[i - 1][j];
                    let ins = dp[i][j - 1];
                    let rep = dp[i - 1][j - 1];
                    dp[i][j] = 1 + std::cmp::min(del, std::cmp::min(ins, rep));
                }
            }
        }
        dp[m][n] as i32
    }
}
```

## Racket

```racket
(define/contract (min-distance word1 word2)
  (-> string? string? exact-integer?)
  (let* ((m (string-length word1))
         (n (string-length word2))
         (prev (make-vector (+ n 1) 0))
         (cur (make-vector (+ n 1) 0)))
    ;; initialize first row: converting empty word1 to prefix of word2
    (for ([j (in-range (+ n 1))])
      (vector-set! prev j j))
    ;; iterate over characters of word1
    (for ([i (in-range 1 (+ m 1))])
      (vector-set! cur 0 i) ; delete i chars to get empty word2
      (let ((c1 (string-ref word1 (sub1 i))))
        (for ([j (in-range 1 (+ n 1))])
          (let* ((c2 (string-ref word2 (sub1 j)))
                 (cost (if (char=? c1 c2)
                           (vector-ref prev (sub1 j))
                           (+ 1 (min (vector-ref prev (sub1 j))   ; replace
                                     (vector-ref prev j)           ; delete
                                     (vector-ref cur (sub1 j))))))) ; insert
            (vector-set! cur j cost))))
      ;; swap rows for next iteration
      (let ((tmp prev))
        (set! prev cur)
        (set! cur tmp)))
    (vector-ref prev n)))
```

## Erlang

```erlang
-export([min_distance/2]).

-spec min_distance(Word1 :: unicode:unicode_binary(), Word2 :: unicode:unicode_binary()) -> integer().
min_distance(Word1, Word2) ->
    W1 = unicode:characters_to_list(Word1),
    W2 = unicode:characters_to_list(Word2),
    N = length(W2),
    Prev0 = lists:seq(0, N),                     % dp[0][j] = j
    FinalPrev =
        case W1 of
            [] -> Prev0;
            _  -> compute_rows(W1, W2, Prev0, 1)
        end,
    %% dp[M][N] is at position N+1 (since index starts at 1 for j=0)
    lists:nth(N + 1, FinalPrev).

%% Recursively process each row of the DP table
-spec compute_rows([integer()], [integer()], [integer()], integer()) -> [integer()].
compute_rows([], _W2, Prev, _RowIdx) ->
    Prev;
compute_rows([C|Rest], W2, Prev, RowIdx) ->
    PrevTail = tl(Prev),          % dp[i-1][j] for j>=1
    PrevHead = Prev,              % dp[i-1][j-1] for j>=1 (includes dp[i-1][0])
    CurTailRev = process_row(C, W2, PrevTail, PrevHead, RowIdx, []),
    Cur = [RowIdx | lists:reverse(CurTailRev)],
    compute_rows(Rest, W2, Cur, RowIdx + 1).

%% Build the current row (excluding column 0) in reverse order
-spec process_row(integer(), [integer()], [integer()], [integer()], integer(), [integer()]) -> [integer()].
process_row(_CharI, [], [], [], _Left, Acc) ->
    Acc;
process_row(CharI, [Cj|RestC], [PrevJ|RestPrevJ], [PrevJ1|RestPrevJ1], Left, Acc) ->
    Cost = if CharI == Cj -> 0; true -> 1 end,
    Up   = PrevJ,
    Diag = PrevJ1,
    MinVal = min3(Up + 1, Left + 1, Diag + Cost),
    process_row(CharI, RestC, RestPrevJ, RestPrevJ1, MinVal, [MinVal | Acc]).

-spec min3(integer(), integer(), integer()) -> integer().
min3(A, B, C) ->
    min(min(A, B), C).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_distance(word1 :: String.t(), word2 :: String.t()) :: integer()
  def min_distance(word1, word2) do
    a = :binary.bin_to_list(word1)
    b = :binary.bin_to_list(word2)

    n = length(a)
    m = length(b)

    # initial row: dp[0][j] = j
    prev_row = List.to_tuple(Enum.to_list(0..m))

    final_row =
      Enum.reduce(1..n, prev_row, fn i, prev ->
        w1c = Enum.at(a, i - 1)

        {rev_vals, _} =
          Enum.reduce(1..m, {[], 0}, fn j, {rev, left} ->
            up = elem(prev, j)
            diag = left
            w2c = Enum.at(b, j - 1)

            cost =
              if w1c == w2c do
                diag
              else
                min12 = if diag < left, do: diag, else: left
                min123 = if min12 < up, do: min12, else: up
                1 + min123
              end

            {[cost | rev], cost}
          end)

        curr_tuple = List.to_tuple([i] ++ Enum.reverse(rev_vals))
        curr_tuple
      end)

    elem(final_row, m)
  end
end
```
