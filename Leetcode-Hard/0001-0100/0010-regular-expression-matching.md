# 0010. Regular Expression Matching

## Cpp

```cpp
class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.size(), n = p.size();
        vector<vector<char>> dp(m + 1, vector<char>(n + 1, 0));
        dp[m][n] = 1; // empty matches empty
        
        for (int i = m; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                bool first_match = (i < m && (p[j] == s[i] || p[j] == '.'));
                if (j + 1 < n && p[j + 1] == '*') {
                    dp[i][j] = dp[i][j + 2]; // zero occurrence
                    if (first_match) dp[i][j] = dp[i][j] || dp[i + 1][j];
                } else {
                    if (first_match) dp[i][j] = dp[i + 1][j + 1];
                }
            }
        }
        return dp[0][0];
    }
};
```

## Java

```java
class Solution {
    public boolean isMatch(String s, String p) {
        int m = s.length(), n = p.length();
        boolean[][] dp = new boolean[m + 1][n + 1];
        dp[m][n] = true;
        for (int i = m; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                boolean firstMatch = i < m && (p.charAt(j) == s.charAt(i) || p.charAt(j) == '.');
                if (j + 1 < n && p.charAt(j + 1) == '*') {
                    dp[i][j] = dp[i][j + 2] || (firstMatch && dp[i + 1][j]);
                } else {
                    dp[i][j] = firstMatch && dp[i + 1][j + 1];
                }
            }
        }
        return dp[0][0];
    }
}
```

## Python

```python
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[m][n] = True

        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):
                first_match = i < m and (p[j] == s[i] or p[j] == '.')
                if j + 1 < n and p[j + 1] == '*':
                    dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]
        return dp[0][0]
```

## Python3

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[m][n] = True

        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):
                first_match = i < m and (p[j] == s[i] or p[j] == '.')
                if j + 1 < n and p[j + 1] == '*':
                    dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]
        return dp[0][0]
```

## C

```c
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

bool isMatch(char* s, char* p) {
    int m = strlen(s);
    int n = strlen(p);
    int rows = m + 1;
    int cols = n + 1;
    bool *dp = (bool *)calloc(rows * cols, sizeof(bool));
    
    // dp[m][n] = true
    dp[m * cols + n] = true;
    
    for (int i = m; i >= 0; --i) {
        for (int j = n - 1; j >= 0; --j) {
            bool first_match = (i < m) && (p[j] == s[i] || p[j] == '.');
            if (j + 1 < n && p[j + 1] == '*') {
                // skip "x*" or use it if first characters match
                dp[i * cols + j] = dp[i * cols + (j + 2)] ||
                                   (first_match && dp[(i + 1) * cols + j]);
            } else {
                dp[i * cols + j] = first_match && dp[(i + 1) * cols + (j + 1)];
            }
        }
    }
    
    bool result = dp[0];
    free(dp);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public bool IsMatch(string s, string p)
    {
        int m = s.Length;
        int n = p.Length;
        bool[,] dp = new bool[m + 1, n + 1];
        dp[m, n] = true;

        for (int i = m; i >= 0; --i)
        {
            for (int j = n - 1; j >= 0; --j)
            {
                bool firstMatch = (i < m) && (p[j] == s[i] || p[j] == '.');
                if (j + 1 < n && p[j + 1] == '*')
                {
                    dp[i, j] = dp[i, j + 2] || (firstMatch && dp[i + 1, j]);
                }
                else
                {
                    dp[i, j] = firstMatch && dp[i + 1, j + 1];
                }
            }
        }

        return dp[0, 0];
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {
    const m = s.length;
    const n = p.length;
    // dp[i][j] means s[i:] matches p[j:]
    const dp = Array.from({ length: m + 1 }, () => Array(n + 1).fill(false));
    dp[m][n] = true; // empty string matches empty pattern

    for (let i = m; i >= 0; i--) {
        for (let j = n - 1; j >= 0; j--) {
            const firstMatch = i < m && (p[j] === s[i] || p[j] === '.');
            if (j + 1 < n && p[j + 1] === '*') {
                dp[i][j] = dp[i][j + 2] || (firstMatch && dp[i + 1][j]);
            } else {
                dp[i][j] = firstMatch && dp[i + 1][j];
            }
        }
    }

    return dp[0][0];
};
```

## Typescript

```typescript
function isMatch(s: string, p: string): boolean {
    const m = s.length;
    const n = p.length;
    const memo: (boolean | undefined)[][] = Array.from({ length: m + 1 }, () => Array(n + 1).fill(undefined));

    function dp(i: number, j: number): boolean {
        if (memo[i][j] !== undefined) return memo[i][j] as boolean;

        let res: boolean;
        if (j === n) {
            res = i === m;
        } else {
            const firstMatch = i < m && (p[j] === s[i] || p[j] === '.');
            if (j + 1 < n && p[j + 1] === '*') {
                // Skip "x*" or use it if first characters match
                res = dp(i, j + 2) || (firstMatch && dp(i + 1, j));
            } else {
                res = firstMatch && dp(i + 1, j + 1);
            }
        }

        memo[i][j] = res;
        return res;
    }

    return dp(0, 0);
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String $p
     * @return Boolean
     */
    function isMatch($s, $p) {
        $lenS = strlen($s);
        $lenP = strlen($p);
        // dp[i][j] indicates if s[i:] matches p[j:]
        $dp = array_fill(0, $lenS + 1, array_fill(0, $lenP + 1, false));
        $dp[$lenS][$lenP] = true;

        for ($i = $lenS; $i >= 0; $i--) {
            for ($j = $lenP - 1; $j >= 0; $j--) {
                $firstMatch = ($i < $lenS) && ($p[$j] === $s[$i] || $p[$j] === '.');
                if ($j + 1 < $lenP && $p[$j + 1] === '*') {
                    // Zero occurrence
                    $dp[$i][$j] = $dp[$i][$j + 2];
                    // One or more occurrences
                    if ($firstMatch) {
                        $dp[$i][$j] = $dp[$i][$j] || $dp[$i + 1][$j];
                    }
                } else {
                    $dp[$i][$j] = $firstMatch && $dp[$i + 1][$j + 1];
                }
            }
        }

        return $dp[0][0];
    }
}
```

## Swift

```swift
class Solution {
    func isMatch(_ s: String, _ p: String) -> Bool {
        let sArr = Array(s)
        let pArr = Array(p)
        var memo = [[Int?]](
            repeating: [Int?](repeating: nil, count: pArr.count + 1),
            count: sArr.count + 1
        )
        
        func dp(_ i: Int, _ j: Int) -> Bool {
            if let cached = memo[i][j] {
                return cached == 1
            }
            var result: Bool
            if j == pArr.count {
                result = (i == sArr.count)
            } else {
                let firstMatch = i < sArr.count && (pArr[j] == sArr[i] || pArr[j] == ".")
                if j + 1 < pArr.count && pArr[j + 1] == "*" {
                    result = dp(i, j + 2) || (firstMatch && dp(i + 1, j))
                } else {
                    result = firstMatch && dp(i + 1, j + 1)
                }
            }
            memo[i][j] = result ? 1 : 0
            return result
        }
        
        return dp(0, 0)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isMatch(s: String, p: String): Boolean {
        val m = s.length
        val n = p.length
        val dp = Array(m + 1) { BooleanArray(n + 1) }
        dp[m][n] = true
        for (i in m downTo 0) {
            for (j in n - 1 downTo 0) {
                val firstMatch = i < m && (p[j] == s[i] || p[j] == '.')
                if (j + 1 < n && p[j + 1] == '*') {
                    dp[i][j] = dp[i][j + 2] || (firstMatch && dp[i + 1][j])
                } else {
                    dp[i][j] = firstMatch && dp[i + 1][j + 1]
                }
            }
        }
        return dp[0][0]
    }
}
```

## Dart

```dart
class Solution {
  bool isMatch(String s, String p) {
    int m = s.length;
    int n = p.length;
    List<List<bool>> dp = List.generate(m + 1, (_) => List.filled(n + 1, false));
    dp[m][n] = true;

    for (int i = m; i >= 0; --i) {
      for (int j = n - 1; j >= 0; --j) {
        bool firstMatch = i < m && (p[j] == s[i] || p[j] == '.');
        if (j + 1 < n && p[j + 1] == '*') {
          dp[i][j] = dp[i][j + 2] || (firstMatch && dp[i + 1][j]);
        } else {
          dp[i][j] = firstMatch && dp[i + 1][j + 1];
        }
      }
    }

    return dp[0][0];
  }
}
```

## Golang

```go
func isMatch(s string, p string) bool {
    m, n := len(s), len(p)
    dp := make([][]bool, m+1)
    for i := range dp {
        dp[i] = make([]bool, n+1)
    }
    dp[m][n] = true
    // Handle patterns that can match an empty string
    for j := n - 2; j >= 0; j-- {
        if p[j+1] == '*' && dp[m][j+2] {
            dp[m][j] = true
        }
    }
    for i := m - 1; i >= 0; i-- {
        for j := n - 1; j >= 0; j-- {
            firstMatch := p[j] == s[i] || p[j] == '.'
            if j+1 < n && p[j+1] == '*' {
                dp[i][j] = dp[i][j+2] || (firstMatch && dp[i+1][j])
            } else {
                dp[i][j] = firstMatch && dp[i+1][j+1]
            }
        }
    }
    return dp[0][0]
}
```

## Ruby

```ruby
def is_match(s, p)
  m = s.length
  n = p.length
  dp = Array.new(m + 1) { Array.new(n + 1, false) }
  dp[m][n] = true

  i = m
  while i >= 0
    j = n - 1
    while j >= 0
      first_match = i < m && (p[j] == s[i] || p[j] == '.')
      if j + 1 < n && p[j + 1] == '*'
        dp[i][j] = dp[i][j + 2] || (first_match && dp[i + 1][j])
      else
        dp[i][j] = first_match && dp[i + 1][j]
      end
      j -= 1
    end
    i -= 1
  end

  dp[0][0]
end
```

## Scala

```scala
object Solution {
    def isMatch(s: String, p: String): Boolean = {
        val m = s.length
        val n = p.length
        val dp = Array.ofDim[Boolean](m + 1, n + 1)
        dp(m)(n) = true

        for (i <- m to 0 by -1) {
            for (j <- n - 1 to 0 by -1) {
                val firstMatch = i < m && (p.charAt(j) == s.charAt(i) || p.charAt(j) == '.')
                if (j + 1 < n && p.charAt(j + 1) == '*') {
                    dp(i)(j) = dp(i)(j + 2) || (firstMatch && dp(i + 1)(j))
                } else {
                    dp(i)(j) = firstMatch && dp(i + 1)(j + 1)
                }
            }
        }

        dp(0)(0)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_match(s: String, p: String) -> bool {
        let s_bytes = s.as_bytes();
        let p_bytes = p.as_bytes();
        let n = s_bytes.len();
        let m = p_bytes.len();

        let mut dp = vec![vec![false; m + 1]; n + 1];
        dp[n][m] = true;

        for i in (0..=n).rev() {
            for j in (0..m).rev() {
                let first_match = i < n && (p_bytes[j] == b'.' || p_bytes[j] == s_bytes[i]);
                if j + 1 < m && p_bytes[j + 1] == b'*' {
                    dp[i][j] = dp[i][j + 2] || (first_match && dp[i + 1][j]);
                } else {
                    dp[i][j] = first_match && dp[i + 1][j + 1];
                }
            }
        }

        dp[0][0]
    }
}
```

## Racket

```racket
(define/contract (is-match s p)
  (-> string? string? boolean?)
  (let* ((m (string-length s))
         (n (string-length p))
         (dp (make-vector (+ m 1) #f)))
    ;; initialize rows
    (for ([i (in-range (+ m 1))])
      (vector-set! dp i (make-vector (+ n 1) #f)))
    ;; base case: empty pattern matches empty string
    (vector-set! (vector-ref dp m) n #t)
    ;; fill DP table bottom‑up
    (let loop-i ((i m))
      (when (>= i 0)
        (let ((row (vector-ref dp i)))
          (for ([j (in-range (sub1 n) -1 -1)])
            (define first-match
              (and (< i m)
                   (let* ((sc (string-ref s i))
                          (pc (string-ref p j)))
                     (or (char=? sc pc) (char=? pc #\.)))))
            (if (and (< (+ j 1) n) (char=? (string-ref p (+ j 1)) #\*))
                (let ((value (or (vector-ref row (+ j 2))
                                 (and first-match
                                      (vector-ref (vector-ref dp (+ i 1)) j)))))
                  (vector-set! row j value))
                (let ((value (and first-match
                                  (vector-ref (vector-ref dp (+ i 1)) (+ j 1)))))
                  (vector-set! row j value)))))
        (loop-i (- i 1))))
    (vector-ref (vector-ref dp 0) 0)))
```

## Erlang

```erlang
-spec is_match(S :: unicode:unicode_binary(), P :: unicode:unicode_binary()) -> boolean().
is_match(S, P) ->
    SList = binary_to_list(S),
    PList = binary_to_list(P),
    match(SList, PList).

match([], []) -> true;
match(_, []) -> false;
match(S, [PChar,$*|RestP]) ->
    case match(S, RestP) of
        true -> true;
        false ->
            case S of
                [] -> false;
                [SChar|RestS] when PChar =:= $. ; PChar =:= SChar ->
                    match(RestS, [PChar,$*|RestP])
            end
    end;
match([SChar|RestS], [PChar|RestP]) ->
    if (PChar =:= $.) orelse (PChar =:= SChar) ->
            match(RestS, RestP);
       true -> false
    end;
match(_, _) -> false.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_match(s :: String.t(), p :: String.t()) :: boolean()
  def is_match(s, p) do
    s_codes = :unicode.characters_to_list(s)
    p_codes = :unicode.characters_to_list(p)
    {result, _} = dp(0, 0, s_codes, p_codes, %{})
    result
  end

  defp dp(i, j, s, p, memo) do
    case Map.fetch(memo, {i, j}) do
      {:ok, val} ->
        {val, memo}

      :error ->
        m = length(s)
        n = length(p)

        cond do
          j == n ->
            res = i == m
            new_memo = Map.put(memo, {i, j}, res)
            {res, new_memo}

          true ->
            first_match =
              i < m and
                (Enum.at(p, j) == ?. or Enum.at(p, j) == Enum.at(s, i))

            if j + 1 < n and Enum.at(p, j + 1) == ?* do
              {skip_res, memo1} = dp(i, j + 2, s, p, memo)

              {use_res, memo2} =
                if first_match do
                  dp(i + 1, j, s, p, memo1)
                else
                  {false, memo1}
                end

              res = skip_res or use_res
              new_memo = Map.put(memo2, {i, j}, res)
              {res, new_memo}
            else
              if first_match do
                {next_res, memo1} = dp(i + 1, j + 1, s, p, memo)
                res = next_res
                new_memo = Map.put(memo1, {i, j}, res)
                {res, new_memo}
              else
                res = false
                new_memo = Map.put(memo, {i, j}, res)
                {res, new_memo}
              end
            end
        end
    end
  end
end
```
