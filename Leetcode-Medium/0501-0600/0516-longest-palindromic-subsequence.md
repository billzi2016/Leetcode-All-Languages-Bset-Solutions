# 0516. Longest Palindromic Subsequence

## Cpp

```cpp
class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int n = s.size();
        vector<vector<int>> dp(n, vector<int>(n, 0));
        for (int i = 0; i < n; ++i) dp[i][i] = 1;
        for (int len = 2; len <= n; ++len) {
            for (int i = 0; i + len - 1 < n; ++i) {
                int j = i + len - 1;
                if (s[i] == s[j]) {
                    dp[i][j] = (len == 2) ? 2 : dp[i + 1][j - 1] + 2;
                } else {
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp[0][n - 1];
    }
};
```

## Java

```java
class Solution {
    public int longestPalindromeSubseq(String s) {
        int n = s.length();
        int[][] dp = new int[n][n];
        // Base case: single characters
        for (int i = 0; i < n; i++) {
            dp[i][i] = 1;
        }
        // Fill DP table
        for (int i = n - 2; i >= 0; i--) {
            char ci = s.charAt(i);
            for (int j = i + 1; j < n; j++) {
                if (ci == s.charAt(j)) {
                    dp[i][j] = dp[i + 1][j - 1] + 2;
                } else {
                    dp[i][j] = Math.max(dp[i + 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp[0][n - 1];
    }
}
```

## Python

```python
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0
        dp = [1] * n  # dp[i] is LPS length for substring i..current j
        for j in range(1, n):
            prev = 0
            for i in range(j - 1, -1, -1):
                temp = dp[i]
                if s[i] == s[j]:
                    dp[i] = prev + 2
                else:
                    dp[i] = max(dp[i], dp[i + 1])
                prev = temp
        return dp[0]
```

## Python3

```python
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        for i in range(n - 1, -1, -1):
            dp[i] = 1
            prev = 0
            for j in range(i + 1, n):
                temp = dp[j]
                if s[i] == s[j]:
                    dp[j] = prev + 2
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev = temp
        return dp[-1] if n else 0
```

## C

```c
#include <string.h>
#include <stdlib.h>

int longestPalindromeSubseq(char* s) {
    if (!s) return 0;
    int n = (int)strlen(s);
    if (n == 0) return 0;

    int *dp = (int *)malloc(n * n * sizeof(int));
    if (!dp) return 0; // allocation failure, though unlikely

    // Initialize diagonal (substrings of length 1)
    for (int i = 0; i < n; ++i) {
        dp[i * n + i] = 1;
    }

    // Build DP table for substrings of increasing length
    for (int len = 2; len <= n; ++len) {
        for (int i = 0; i + len - 1 < n; ++i) {
            int j = i + len - 1;
            if (s[i] == s[j]) {
                if (len == 2)
                    dp[i * n + j] = 2;
                else
                    dp[i * n + j] = dp[(i + 1) * n + (j - 1)] + 2;
            } else {
                int a = dp[(i + 1) * n + j];
                int b = dp[i * n + (j - 1)];
                dp[i * n + j] = (a > b) ? a : b;
            }
        }
    }

    int result = dp[0 * n + (n - 1)];
    free(dp);
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int LongestPalindromeSubseq(string s) {
        int n = s.Length;
        if (n == 0) return 0;
        char[] ch = s.ToCharArray();
        int[,] dp = new int[n, n];
        for (int i = n - 1; i >= 0; i--) {
            dp[i, i] = 1;
            for (int j = i + 1; j < n; j++) {
                if (ch[i] == ch[j]) {
                    dp[i, j] = ((i + 1 <= j - 1) ? dp[i + 1, j - 1] : 0) + 2;
                } else {
                    dp[i, j] = Math.Max(dp[i + 1, j], dp[i, j - 1]);
                }
            }
        }
        return dp[0, n - 1];
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var longestPalindromeSubseq = function(s) {
    const n = s.length;
    if (n === 0) return 0;
    // dp[i][j] will store the length of LPS in s[i..j]
    const dp = Array.from({length: n}, () => new Uint16Array(n));
    
    // substrings of length 1
    for (let i = 0; i < n; ++i) {
        dp[i][i] = 1;
    }
    
    // build the table bottom-up
    for (let len = 2; len <= n; ++len) {
        for (let i = 0; i + len - 1 < n; ++i) {
            const j = i + len - 1;
            if (s[i] === s[j]) {
                dp[i][j] = (len === 2 ? 2 : dp[i + 1][j - 1] + 2);
            } else {
                dp[i][j] = Math.max(dp[i + 1][j], dp[i][j - 1]);
            }
        }
    }
    
    return dp[0][n - 1];
};
```

## Typescript

```typescript
function longestPalindromeSubseq(s: string): number {
    const n = s.length;
    if (n === 0) return 0;

    // dp[i][j] will hold the length of LPS in s[i..j]
    const dp: number[][] = Array.from({ length: n }, () => new Array(n).fill(0));

    // Subsequences of length 1 are palindromes of length 1
    for (let i = 0; i < n; i++) {
        dp[i][i] = 1;
    }

    // Build the table. cl is the length of substring.
    for (let cl = 2; cl <= n; cl++) {
        for (let i = 0; i <= n - cl; i++) {
            const j = i + cl - 1;
            if (s[i] === s[j]) {
                if (cl === 2) {
                    dp[i][j] = 2;
                } else {
                    dp[i][j] = dp[i + 1][j - 1] + 2;
                }
            } else {
                dp[i][j] = Math.max(dp[i + 1][j], dp[i][j - 1]);
            }
        }
    }

    return dp[0][n - 1];
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function longestPalindromeSubseq($s) {
        $n = strlen($s);
        if ($n == 0) return 0;
        // Initialize DP table
        $dp = array_fill(0, $n, array_fill(0, $n, 0));
        for ($i = 0; $i < $n; $i++) {
            $dp[$i][$i] = 1;
        }
        // Build the table
        for ($len = 2; $len <= $n; $len++) {
            for ($i = 0; $i + $len - 1 < $n; $i++) {
                $j = $i + $len - 1;
                if ($s[$i] === $s[$j]) {
                    if ($len == 2) {
                        $dp[$i][$j] = 2;
                    } else {
                        $dp[$i][$j] = $dp[$i + 1][$j - 1] + 2;
                    }
                } else {
                    $dp[$i][$j] = max($dp[$i + 1][$j], $dp[$i][$j - 1]);
                }
            }
        }
        return $dp[0][$n - 1];
    }
}
```

## Swift

```swift
class Solution {
    func longestPalindromeSubseq(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        if n == 0 { return 0 }
        var dp = [[Int]](repeating: [Int](repeating: 0, count: n), count: n)
        for i in 0..<n {
            dp[i][i] = 1
        }
        if n >= 2 {
            for len in 2...n {
                var i = 0
                while i + len - 1 < n {
                    let j = i + len - 1
                    if chars[i] == chars[j] {
                        dp[i][j] = (len == 2) ? 2 : dp[i+1][j-1] + 2
                    } else {
                        dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                    }
                    i += 1
                }
            }
        }
        return dp[0][n-1]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestPalindromeSubseq(s: String): Int {
        val n = s.length
        if (n == 0) return 0
        val dp = Array(n) { IntArray(n) }
        for (i in 0 until n) {
            dp[i][i] = 1
        }
        for (len in 2..n) {
            var i = 0
            while (i + len - 1 < n) {
                val j = i + len - 1
                if (s[i] == s[j]) {
                    dp[i][j] = if (len == 2) 2 else dp[i + 1][j - 1] + 2
                } else {
                    dp[i][j] = maxOf(dp[i + 1][j], dp[i][j - 1])
                }
                i++
            }
        }
        return dp[0][n - 1]
    }
}
```

## Dart

```dart
class Solution {
  int longestPalindromeSubseq(String s) {
    int n = s.length;
    if (n == 0) return 0;
    List<List<int>> dp = List.generate(n, (_) => List.filled(n, 0));
    for (int i = 0; i < n; i++) {
      dp[i][i] = 1;
    }
    for (int len = 2; len <= n; len++) {
      for (int i = 0; i + len - 1 < n; i++) {
        int j = i + len - 1;
        if (s.codeUnitAt(i) == s.codeUnitAt(j)) {
          dp[i][j] = (len == 2) ? 2 : dp[i + 1][j - 1] + 2;
        } else {
          dp[i][j] = dp[i + 1][j] > dp[i][j - 1] ? dp[i + 1][j] : dp[i][j - 1];
        }
      }
    }
    return dp[0][n - 1];
  }
}
```

## Golang

```go
func longestPalindromeSubseq(s string) int {
	n := len(s)
	if n == 0 {
		return 0
	}
	dp := make([][]int, n)
	for i := 0; i < n; i++ {
		row := make([]int, n)
		row[i] = 1
		dp[i] = row
	}
	for length := 2; length <= n; length++ {
		for i := 0; i+length-1 < n; i++ {
			j := i + length - 1
			if s[i] == s[j] {
				if length == 2 {
					dp[i][j] = 2
				} else {
					dp[i][j] = dp[i+1][j-1] + 2
				}
			} else {
				if dp[i+1][j] > dp[i][j-1] {
					dp[i][j] = dp[i+1][j]
				} else {
					dp[i][j] = dp[i][j-1]
				}
			}
		}
	}
	return dp[0][n-1]
}
```

## Ruby

```ruby
def longest_palindrome_subseq(s)
  t = s.reverse
  n = s.length
  prev = Array.new(n + 1, 0)
  curr = Array.new(n + 1, 0)

  (1..n).each do |i|
    (1..n).each do |j|
      if s[i - 1] == t[j - 1]
        curr[j] = prev[j - 1] + 1
      else
        a = prev[j]
        b = curr[j - 1]
        curr[j] = a > b ? a : b
      end
    end
    prev, curr = curr, prev
  end

  prev[n]
end
```

## Scala

```scala
object Solution {
    def longestPalindromeSubseq(s: String): Int = {
        val n = s.length
        if (n == 0) return 0
        val dp = Array.ofDim[Int](n, n)
        for (i <- 0 until n) dp(i)(i) = 1

        var len = 2
        while (len <= n) {
            var i = 0
            while (i + len - 1 < n) {
                val j = i + len - 1
                if (s.charAt(i) == s.charAt(j)) {
                    dp(i)(j) = if (len == 2) 2 else dp(i + 1)(j - 1) + 2
                } else {
                    dp(i)(j) = math.max(dp(i + 1)(j), dp(i)(j - 1))
                }
                i += 1
            }
            len += 1
        }

        dp(0)(n - 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_palindrome_subseq(s: String) -> i32 {
        let n = s.len();
        if n == 0 {
            return 0;
        }
        let bytes = s.as_bytes();
        let mut dp = vec![vec![0i32; n]; n];
        for i in 0..n {
            dp[i][i] = 1;
        }
        for len in 2..=n {
            for i in 0..=n - len {
                let j = i + len - 1;
                if bytes[i] == bytes[j] {
                    dp[i][j] = if len == 2 { 2 } else { dp[i + 1][j - 1] + 2 };
                } else {
                    dp[i][j] = dp[i + 1][j].max(dp[i][j - 1]);
                }
            }
        }
        dp[0][n - 1]
    }
}
```

## Racket

```racket
(define/contract (longest-palindrome-subseq s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (dp (make-vector n)))
    ;; initialize rows
    (for ([i (in-range n)])
      (vector-set! dp i (make-vector n 0)))
    ;; fill DP table bottom‑up
    (for ([i (in-range (sub1 n) -1 -1)]) ; i = n-1 .. 0
      (let* ((row (vector-ref dp i))
             (next-row (if (< i (sub1 n)) (vector-ref dp (add1 i)) #f)))
        (vector-set! row i 1)                     ; single character palindrome
        (for ([j (in-range (add1 i) n)])          ; j = i+1 .. n-1
          (if (char=? (string-ref s i) (string-ref s j))
              (let ((inner (if (= (+ i 1) j)
                               0
                               (vector-ref (vector-ref dp (add1 i)) (sub1 j)))))
                (vector-set! row j (+ inner 2)))
              (let ((val1 (vector-ref next-row j))
                    (val2 (vector-ref row (sub1 j))))
                (vector-set! row j (max val1 val2)))))))
    ;; answer is dp[0][n-1]
    (if (= n 0)
        0
        (vector-ref (vector-ref dp 0) (sub1 n)))))
```

## Erlang

```erlang
-spec longest_palindrome_subseq(S :: unicode:unicode_binary()) -> integer().
longest_palindrome_subseq(S) ->
    N = byte_size(S),
    DP0 = array:new(N, {default, 0}),
    DPFinal = loop_i(N - 1, N, S, DP0),
    array:get(N - 1, DPFinal).

loop_i(I, _N, _S, DP) when I < 0 -> DP;
loop_i(I, N, S, DP0) ->
    DP1 = array:set(I, 1, DP0),
    DP2 = loop_j(I + 1, I, N - 1, S, DP1, 0),
    loop_i(I - 1, N, S, DP2).

loop_j(J, _I, MaxJ, _S, DP, _Prev) when J > MaxJ -> DP;
loop_j(J, I, MaxJ, S, DPAcc, Prev) ->
    OldDj = array:get(J, DPAcc),
    Ci = binary:at(S, I),
    Cj = binary:at(S, J),
    NewVal =
        if
            Ci == Cj ->
                2 + Prev;
            true ->
                Dpjm1 = array:get(J - 1, DPAcc),
                erlang:max(OldDj, Dpjm1)
        end,
    DPNew = array:set(J, NewVal, DPAcc),
    loop_j(J + 1, I, MaxJ, S, DPNew, OldDj).
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_palindrome_subseq(s :: String.t()) :: integer
  def longest_palindrome_subseq(s) do
    n = String.length(s)
    if n == 0, do: 0, else:
      chars = s |> String.to_charlist() |> List.to_tuple()

      dp =
        Enum.reduce((n - 1)..0, %{}, fn i, acc ->
          acc = Map.put(acc, {i, i}, 1)

          if i + 1 <= n - 1 do
            Enum.reduce((i + 1)..(n - 1), acc, fn j, a2 ->
              ci = elem(chars, i)
              cj = elem(chars, j)

              cond do
                ci == cj ->
                  val =
                    if j == i + 1 do
                      2
                    else
                      Map.get(a2, {i + 1, j - 1}) + 2
                    end

                  Map.put(a2, {i, j}, val)

                true ->
                  left = Map.get(a2, {i + 1, j})
                  right = Map.get(a2, {i, j - 1})
                  val = if left > right, do: left, else: right
                  Map.put(a2, {i, j}, val)
              end
            end)
          else
            acc
          end
        end)

      Map.get(dp, {0, n - 1})
    end
  end
end
```
