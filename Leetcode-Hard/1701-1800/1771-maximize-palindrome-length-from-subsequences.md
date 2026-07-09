# 1771. Maximize Palindrome Length From Subsequences

## Cpp

```cpp
class Solution {
public:
    int longestPalindrome(string word1, string word2) {
        string rev = word2;
        reverse(rev.begin(), rev.end());
        int n = word1.size(), m = rev.size();
        vector<int> dp(m + 1, 0), prev(m + 1, 0);
        for (int i = 1; i <= n; ++i) {
            swap(dp, prev);
            for (int j = 1; j <= m; ++j) {
                if (word1[i - 1] == rev[j - 1])
                    dp[j] = prev[j - 1] + 1;
                else
                    dp[j] = max(prev[j], dp[j - 1]);
            }
        }
        int L = dp[m];
        if (L == 0) return 0;
        int ans = 2 * L;
        if (L < n || L < (int)word2.size()) ++ans;
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int longestPalindrome(String word1, String word2) {
        String s = word1 + word2;
        int n = s.length();
        int split = word1.length() - 1; // last index belonging to word1
        int[][] dp = new int[n][n];
        int[][] both = new int[n][n];

        for (int i = n - 1; i >= 0; --i) {
            dp[i][i] = 1;
            for (int j = i + 1; j < n; ++j) {
                if (s.charAt(i) == s.charAt(j)) {
                    int inner = (i + 1 <= j - 1) ? dp[i + 1][j - 1] : 0;
                    dp[i][j] = inner + 2;

                    int cand = 0;
                    boolean leftSide = i <= split;
                    boolean rightSide = j > split;
                    if (leftSide && rightSide) {
                        cand = inner + 2; // outer pair already covers both sides
                    } else {
                        int innerBoth = (i + 1 <= j - 1) ? both[i + 1][j - 1] : 0;
                        if (innerBoth > 0) {
                            cand = innerBoth + 2;
                        }
                    }
                    int bestSkip = Math.max(both[i + 1][j], both[i][j - 1]);
                    both[i][j] = Math.max(cand, bestSkip);
                } else {
                    dp[i][j] = Math.max(dp[i + 1][j], dp[i][j - 1]);
                    both[i][j] = Math.max(both[i + 1][j], both[i][j - 1]);
                }
            }
        }
        return both[0][n - 1];
    }
}
```

## Python

```python
class Solution(object):
    def longestPalindrome(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n, m = len(word1), len(word2)
        # dp[i][j]: max palindrome length using word1[i:] and word2[:j]
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # base cases: when one side is empty, we can take at most one character from the other side
        for i in range(n):
            dp[i][0] = 1  # any single char from word1 suffix
        for j in range(1, m + 1):
            dp[n][j] = 1  # any single char from word2 prefix

        for i in range(n - 1, -1, -1):
            wi = word1[i]
            for j in range(1, m + 1):
                best = dp[i + 1][j] if dp[i + 1][j] > dp[i][j - 1] else dp[i][j - 1]
                if wi == word2[j - 1]:
                    cand = 2 + dp[i + 1][j - 1]
                    if cand > best:
                        best = cand
                dp[i][j] = best

        ans = dp[0][m]
        return ans if ans >= 2 else 0
```

## Python3

```python
class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        s = word1 + word2
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            si = s[i]
            for j in range(i + 1, n):
                if si == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2 if i + 1 <= j - 1 else 2
                else:
                    a = dp[i + 1][j]
                    b = dp[i][j - 1]
                    dp[i][j] = a if a > b else b
        ans = 0
        for i in range(n1):
            si = s[i]
            for j in range(n1, n):
                if si == s[j]:
                    inner = dp[i + 1][j - 1] if i + 1 <= j - 1 else 0
                    cur = inner + 2
                    if cur > ans:
                        ans = cur
        return ans
```

## C

```c
#include <string.h>
#include <stdlib.h>

int longestPalindrome(char* word1, char* word2) {
    int n = strlen(word1);
    int m = strlen(word2);
    if (n == 0 || m == 0) return 0;

    // reverse word2
    char *rev = (char *)malloc(m + 1);
    for (int i = 0; i < m; ++i) rev[i] = word2[m - 1 - i];
    rev[m] = '\0';

    int *prev = (int *)calloc(m + 1, sizeof(int));
    int *curr = (int *)calloc(m + 1, sizeof(int));

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (word1[i - 1] == rev[j - 1])
                curr[j] = prev[j - 1] + 1;
            else
                curr[j] = prev[j] > curr[j - 1] ? prev[j] : curr[j - 1];
        }
        int *tmp = prev; prev = curr; curr = tmp;
    }

    int k = prev[m]; // length of longest common subsequence

    free(prev);
    free(curr);
    free(rev);

    if (k == 0) return 0;
    int totalLen = n + m;
    int ans = 2 * k + ((totalLen > 2 * k) ? 1 : 0);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int LongestPalindrome(string word1, string word2) {
        string s = word1 + word2;
        int n1 = word1.Length;
        int n = s.Length;
        int[,] dp = new int[n, n];

        for (int i = n - 1; i >= 0; --i) {
            dp[i, i] = 1;
            for (int j = i + 1; j < n; ++j) {
                if (s[i] == s[j]) {
                    int inner = (i + 1 <= j - 1) ? dp[i + 1, j - 1] : 0;
                    dp[i, j] = inner + 2;
                } else {
                    dp[i, j] = Math.Max(dp[i + 1, j], dp[i, j - 1]);
                }
            }
        }

        int ans = 0;
        for (int i = 0; i < n1; ++i) {
            for (int j = n1; j < n; ++j) {
                if (dp[i, j] > ans) ans = dp[i, j];
            }
        }
        return ans;
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
var longestPalindrome = function(word1, word2) {
    const s = word1 + word2;
    const n = s.length;
    if (n === 0) return 0;

    // dp[i][j] = length of longest palindromic subsequence in s[i..j]
    const dp = Array.from({ length: n }, () => new Uint16Array(n));

    for (let i = 0; i < n; ++i) dp[i][i] = 1;

    for (let len = 2; len <= n; ++len) {
        for (let i = 0, j = len - 1; j < n; ++i, ++j) {
            if (s.charAt(i) === s.charAt(j)) {
                dp[i][j] = ((i + 1 <= j - 1) ? dp[i + 1][j - 1] : 0) + 2;
            } else {
                dp[i][j] = Math.max(dp[i + 1][j], dp[i][j - 1]);
            }
        }
    }

    let ans = 0;
    const split = word1.length; // boundary between the two strings
    for (let i = 0; i < split; ++i) {
        for (let j = split; j < n; ++j) {
            if (s.charAt(i) === s.charAt(j)) {
                const inner = (i + 1 <= j - 1) ? dp[i + 1][j - 1] : 0;
                ans = Math.max(ans, inner + 2);
            }
        }
    }

    return ans;
};
```

## Typescript

```typescript
function longestPalindrome(word1: string, word2: string): number {
    const n = word1.length;
    const m = word2.length;
    const rev = word2.split('').reverse().join('');
    // dp[i][j] = LCS length of suffixes starting at i in word1 and j in rev
    const dp: Uint16Array[] = Array.from({ length: n + 1 }, () => new Uint16Array(m + 1));
    for (let i = n - 1; i >= 0; --i) {
        const wChar = word1.charCodeAt(i);
        for (let j = m - 1; j >= 0; --j) {
            if (wChar === rev.charCodeAt(j)) {
                dp[i][j] = dp[i + 1][j + 1] + 1;
            } else {
                const a = dp[i + 1][j];
                const b = dp[i][j + 1];
                dp[i][j] = a > b ? a : b;
            }
        }
    }
    const L = dp[0][0];
    if (L === 0) return 0;
    let ans = 2 * L; // even length
    // odd length with middle from word1
    const oddFromW1 = n > L ? 2 * L + 1 : 2 * L - 1;
    // odd length with middle from word2
    const oddFromW2 = m > L ? 2 * L + 1 : 2 * L - 1;
    if (oddFromW1 > ans) ans = oddFromW1;
    if (oddFromW2 > ans) ans = oddFromW2;
    return ans;
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
    function longestPalindrome($word1, $word2) {
        $n = strlen($word1);
        $m = strlen($word2);
        $rev2 = strrev($word2);

        // dp[i][j] = LCS length between word1[i..] and rev2[j..]
        $dp = array_fill(0, $n + 1, array_fill(0, $m + 1, 0));

        for ($i = $n - 1; $i >= 0; --$i) {
            $c1 = $word1[$i];
            for ($j = $m - 1; $j >= 0; --$j) {
                if ($c1 === $rev2[$j]) {
                    $dp[$i][$j] = 1 + $dp[$i + 1][$j + 1];
                } else {
                    $a = $dp[$i + 1][$j];
                    $b = $dp[$i][$j + 1];
                    $dp[$i][$j] = ($a > $b) ? $a : $b;
                }
            }
        }

        $ans = 0;
        for ($i = 0; $i < $n; ++$i) {
            $c1 = $word1[$i];
            for ($j = 0; $j < $m; ++$j) {
                if ($c1 === $word2[$j]) {
                    // inner LCS between word1[i+1..] and reverse(word2[0..j-1])
                    $inner = $dp[$i + 1][$m - $j];
                    $len = 2 + 2 * $inner;
                    if ($i + 1 < $n || $j > 0) {
                        $len += 1; // possible central character
                    }
                    if ($len > $ans) {
                        $ans = $len;
                    }
                }
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func longestPalindrome(_ word1: String, _ word2: String) -> Int {
        let a = Array(word1.utf8)
        let b = Array(word2.utf8)
        let n = a.count
        let m = b.count
        
        var dp = Array(repeating: Array(repeating: 0, count: m + 1), count: n + 1)
        
        if n == 0 || m == 0 { return 0 }
        
        for i in stride(from: n - 1, through: 0, by: -1) {
            for j in 1...m {
                var best = max(dp[i + 1][j], dp[i][j - 1])
                if a[i] == b[j - 1] {
                    best = max(best, 2 + dp[i + 1][j - 1])
                }
                dp[i][j] = best
            }
        }
        
        var ans = 0
        for i in 0...n {
            for j in 0...m {
                let val = dp[i][j]
                if val > ans { ans = val }
                if val > 0 {
                    // remaining characters that can serve as a middle character
                    let leftover = (n - i) + j - val
                    if leftover > 0 {
                        let cand = val + 1
                        if cand > ans { ans = cand }
                    }
                }
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestPalindrome(word1: String, word2: String): Int {
        val n1 = word1.length
        val s = word1 + word2
        val n = s.length
        val dp = Array(n) { IntArray(n) }
        var ans = 0
        for (i in n - 1 downTo 0) {
            dp[i][i] = 1
            for (j in i + 1 until n) {
                if (s[i] == s[j]) {
                    dp[i][j] = if (i + 1 <= j - 1) dp[i + 1][j - 1] + 2 else 2
                } else {
                    dp[i][j] = maxOf(dp[i + 1][j], dp[i][j - 1])
                }
                if (i < n1 && j >= n1) {
                    ans = maxOf(ans, dp[i][j])
                }
            }
        }
        return ans
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int longestPalindrome(String word1, String word2) {
    int n = word1.length;
    int m = word2.length;
    List<List<int>> dp = List.generate(n + 1, (_) => List.filled(m + 1, 0));

    for (int i = n - 1; i >= 0; --i) {
      for (int j = 1; j <= m; ++j) {
        if (word1[i] == word2[j - 1]) {
          int take = 1 + dp[i + 1][j - 1];
          int skipI = dp[i + 1][j];
          int skipJ = dp[i][j - 1];
          dp[i][j] = max(take, max(skipI, skipJ));
        } else {
          dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
        }
      }
    }

    int ans = 0;
    for (int i = 0; i < n; ++i) {
      for (int j = 1; j <= m; ++j) {
        if (word1[i] == word2[j - 1]) {
          int pairsInside = dp[i + 1][j - 1];
          int length = 2 * (1 + pairsInside);
          if (i + 1 < n || j - 1 > 0) {
            length += 1; // possible center character
          }
          ans = max(ans, length);
        }
      }
    }

    return ans;
  }
}
```

## Golang

```go
func longestPalindrome(word1 string, word2 string) int {
    s := word1 + word2
    n := len(s)
    split := len(word1)

    dpLen := make([][]int, n)
    dpBoth := make([][]int, n)
    for i := 0; i < n; i++ {
        dpLen[i] = make([]int, n)
        dpBoth[i] = make([]int, n)
        dpLen[i][i] = 1
    }

    for length := 2; length <= n; length++ {
        for i := 0; i+length-1 < n; i++ {
            j := i + length - 1

            // Compute longest palindromic subsequence length
            if s[i] == s[j] {
                innerLen := 0
                if i+1 <= j-1 {
                    innerLen = dpLen[i+1][j-1]
                }
                dpLen[i][j] = 2 + innerLen
            } else {
                if dpLen[i+1][j] > dpLen[i][j-1] {
                    dpLen[i][j] = dpLen[i+1][j]
                } else {
                    dpLen[i][j] = dpLen[i][j-1]
                }
            }

            // Compute longest palindrome using both strings
            best := dpBoth[i+1][j]
            if dpBoth[i][j-1] > best {
                best = dpBoth[i][j-1]
            }

            if s[i] == s[j] {
                innerBoth := 0
                if i+1 <= j-1 {
                    innerBoth = dpBoth[i+1][j-1]
                }
                candidateLen := 2
                if i+1 <= j-1 {
                    candidateLen += dpLen[i+1][j-1]
                }

                usesBoth := false
                if i < split && j >= split {
                    usesBoth = true
                } else if innerBoth > 0 {
                    usesBoth = true
                }

                if usesBoth && candidateLen > best {
                    best = candidateLen
                }
            }

            dpBoth[i][j] = best
        }
    }

    return dpBoth[0][n-1]
}
```

## Ruby

```ruby
# @param {String} word1
# @param {String} word2
# @return {Integer}
def longest_palindrome(word1, word2)
  m = word1.length
  n = word2.length
  rev2 = word2.reverse

  # dp[i][j] = LCS length of word1[i..] and rev2[j..]
  dp = Array.new(m + 1) { Array.new(n + 1, 0) }

  (m - 1).downto(0) do |i|
    wi = word1[i]
    (n - 1).downto(0) do |j|
      if wi == rev2[j]
        dp[i][j] = 1 + dp[i + 1][j + 1]
      else
        a = dp[i + 1][j]
        b = dp[i][j + 1]
        dp[i][j] = a > b ? a : b
      end
    end
  end

  ans = 0
  (0...m).each do |i|
    wi = word1[i]
    (0...n).each do |j|
      next unless wi == word2[j]

      inner_len = dp[i + 1][n - j] # LCS of suffix after i and prefix before j
      total = 2 + inner_len * 2
      total += 1 if i + 1 < m || j > 0
      ans = total if total > ans
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def longestPalindrome(word1: String, word2: String): Int = {
        val n1 = word1.length
        val s = word1 + word2
        val N = s.length
        val dp = Array.ofDim[Int](N, N)
        var ans = 0
        for (i <- (0 until N).reverse) {
            dp(i)(i) = 1
            for (j <- i + 1 until N) {
                if (s.charAt(i) == s.charAt(j)) {
                    val inner = if (i + 1 <= j - 1) dp(i + 1)(j - 1) else 0
                    dp(i)(j) = inner + 2
                } else {
                    dp(i)(j) = math.max(dp(i + 1)(j), dp(i)(j - 1))
                }
                if (i < n1 && j >= n1) {
                    ans = math.max(ans, dp(i)(j))
                }
            }
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_palindrome(word1: String, word2: String) -> i32 {
        let n1 = word1.len();
        let mut chars: Vec<char> = word1.chars().collect();
        chars.extend(word2.chars());
        let n = chars.len();

        // dp[i][j] = longest palindromic subsequence length in chars[i..=j]
        let mut dp = vec![vec![0u16; n]; n];

        for i in (0..n).rev() {
            dp[i][i] = 1;
            for j in (i + 1)..n {
                if chars[i] == chars[j] {
                    let inner = if i + 1 <= j - 1 { dp[i + 1][j - 1] } else { 0 };
                    dp[i][j] = inner + 2;
                } else {
                    dp[i][j] = dp[i + 1][j].max(dp[i][j - 1]);
                }
            }
        }

        let mut ans: u16 = 0;
        for i in 0..n1 {
            for j in n1..n {
                ans = ans.max(dp[i][j]);
            }
        }
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (longest-palindrome word1 word2)
  (-> string? string? exact-integer?)
  (let* ((n (string-length word1))
         (m (string-length word2))
         (rev (list->string (reverse (string->list word2))))
         ;; dp[i][j] = LCS length of suffixes word1[i:] and rev[j:]
         (dp (make-vector (+ n 1) #f)))
    ;; initialise rows
    (for ([i (in-range (+ n 1))])
      (vector-set! dp i (make-vector (+ m 1) 0)))
    ;; fill DP bottom‑up
    (for ([i (in-range (- n 1) -1 -1)])
      (let ((row (vector-ref dp i))
            (next-row (vector-ref dp (+ i 1))))
        (for ([j (in-range (- m 1) -1 -1)])
          (if (char=? (string-ref word1 i) (string-ref rev j))
              (let ((val (+ 1 (vector-ref (vector-ref dp (+ i 1)) (+ j 1)))))
                (vector-set! row j val))
              (let ((val (max (vector-ref next-row j)
                              (vector-ref row (+ j 1)))))
                (vector-set! row j val))))))
    ;; compute answer
    (let ((ans 0))
      (for ([i (in-range n)])
        (for ([j (in-range m)])
          (let* ((l (vector-ref (vector-ref dp i) j)))
            (when (> l 0)
              (set! ans (max ans (* 2 l)))
              (when (> (+ (- n i) (- m j)) (* 2 l))
                (set! ans (max ans (+ (* 2 l) 1))))))))
      ans)))
```

## Erlang

```erlang
-export([longest_palindrome/2]).
-spec longest_palindrome(Word1 :: unicode:unicode_binary(), Word2 :: unicode:unicode_binary()) -> integer().
longest_palindrome(Word1, Word2) ->
    W1 = binary_to_list(Word1),
    W2 = binary_to_list(Word2),
    RevW2 = lists:reverse(W2),
    Lcs = lcs(W1, RevW2),
    case Lcs of
        0 -> 0;
        _ ->
            LenSum = length(W1) + length(W2),
            if LenSum > 2 * Lcs -> 2 * Lcs + 1; true -> 2 * Lcs end
    end.

lcs(W1, W2Rev) ->
    M = length(W2Rev),
    ZeroRow = lists:duplicate(M + 1, 0),
    lcs_rows(W1, W2Rev, ZeroRow).

lcs_rows([], _W2Rev, Prev) ->
    lists:last(Prev);
lcs_rows([C | Rest], W2Rev, Prev) ->
    NewRow = lcs_row(C, W2Rev, Prev),
    lcs_rows(Rest, W2Rev, NewRow).

lcs_row(CharC, W2Rev, PrevRow) ->
    {NewRow, _} = lcs_row_loop(CharC, W2Rev, PrevRow, 0, []),
    NewRow.

lcs_row_loop(_CharC, [], [_Prev0 | _RestPrev], _Left, Acc) ->
    {lists:reverse([0 | Acc]), ok};
lcs_row_loop(CharC, [W2Char | RestW2],
              [PrevDiag | [PrevJ | RestPrevTail]],
              Left, Acc) ->
    Val = if CharC == W2Char -> PrevDiag + 1;
             true -> erlang:max(PrevJ, Left)
          end,
    lcs_row_loop(CharC, RestW2, RestPrevTail, Val, [Val | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_palindrome(word1 :: String.t(), word2 :: String.t()) :: integer()
  def longest_palindrome(word1, word2) do
    w1_chars = String.to_charlist(word1)
    rev_w2_chars = String.to_charlist(String.reverse(word2))
    lcs_len = lcs(w1_chars, rev_w2_chars)

    if lcs_len == 0 do
      0
    else
      base = 2 * lcs_len

      if String.length(word1) > lcs_len or String.length(word2) > lcs_len do
        base + 1
      else
        base
      end
    end
  end

  defp lcs(w1, w2_rev) do
    m = length(w2_rev)
    init_row = :erlang.make_tuple(m + 1, 0)

    Enum.reduce(0..(length(w1) - 1), init_row, fn i, prev_row ->
      c1 = Enum.at(w1, i)
      cur_row = :erlang.make_tuple(m + 1, 0)

      {cur_row, _} =
        Enum.reduce(0..(m - 1), {cur_row, prev_row}, fn j, {c_acc, p_row} ->
          c2 = Enum.at(w2_rev, j)

          val =
            if c1 == c2 do
              elem(p_row, j) + 1
            else
              max(elem(p_row, j + 1), elem(c_acc, j))
            end

          {put_elem(c_acc, j + 1, val), p_row}
        end)

      cur_row
    end)
    |> then(fn final_row -> elem(final_row, m) end)
  end
end
```
