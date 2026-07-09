# 1745. Palindrome Partitioning IV

## Cpp

```cpp
class Solution {
public:
    bool checkPartitioning(string s) {
        int n = s.size();
        vector<vector<char>> pal(n, vector<char>(n, 0));
        for (int len = 1; len <= n; ++len) {
            for (int i = 0; i + len - 1 < n; ++i) {
                int j = i + len - 1;
                if (s[i] == s[j] && (len <= 2 || pal[i+1][j-1]))
                    pal[i][j] = 1;
            }
        }
        for (int i = 0; i < n - 2; ++i) {
            if (!pal[0][i]) continue;
            for (int j = i + 1; j < n - 1; ++j) {
                if (pal[i+1][j] && pal[j+1][n-1])
                    return true;
            }
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean checkPartitioning(String s) {
        int n = s.length();
        char[] ch = s.toCharArray();
        boolean[][] pal = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            pal[i][i] = true;
        }
        for (int len = 2; len <= n; len++) {
            for (int i = 0; i + len - 1 < n; i++) {
                int j = i + len - 1;
                if (ch[i] == ch[j]) {
                    if (len == 2) {
                        pal[i][j] = true;
                    } else {
                        pal[i][j] = pal[i + 1][j - 1];
                    }
                }
            }
        }
        for (int i = 1; i <= n - 2; i++) { // first cut after i characters
            if (!pal[0][i - 1]) continue;
            for (int j = i + 1; j <= n - 1; j++) { // second cut after j characters
                if (pal[i][j - 1] && pal[j][n - 1]) {
                    return true;
                }
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def checkPartitioning(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        # Precompute palindrome table
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n):
            is_pal[i][i] = True
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2 or is_pal[i + 1][j - 1]:
                        is_pal[i][j] = True

        # Try all possible cuts
        for i in range(1, n - 1):          # first cut after position i-1
            if not is_pal[0][i - 1]:
                continue
            for j in range(i + 1, n):      # second cut after position j-1
                if is_pal[i][j - 1] and is_pal[j][n - 1]:
                    return True
        return False
```

## Python3

```python
class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        # palindrome table pal[l][r] indicates s[l..r] is palindrome
        pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            pal[i][i] = True
            for j in range(i + 1, n):
                if s[i] == s[j] and (j - i < 2 or pal[i + 1][j - 1]):
                    pal[i][j] = True

        # try all possible first and second cut positions
        for i in range(1, n - 1):          # end of first part (exclusive)
            if not pal[0][i - 1]:
                continue
            for j in range(i + 1, n):      # end of second part (exclusive)
                if pal[i][j - 1] and pal[j][n - 1]:
                    return True
        return False
```

## C

```c
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

bool checkPartitioning(char* s) {
    int n = strlen(s);
    if (n < 3) return false;
    bool *pal = (bool*)malloc(n * n * sizeof(bool));
    if (!pal) return false;

    for (int i = 0; i < n; ++i)
        pal[i * n + i] = true;

    for (int len = 2; len <= n; ++len) {
        for (int i = 0; i + len - 1 < n; ++i) {
            int j = i + len - 1;
            if (s[i] == s[j]) {
                if (len == 2 || pal[(i + 1) * n + (j - 1)])
                    pal[i * n + j] = true;
                else
                    pal[i * n + j] = false;
            } else {
                pal[i * n + j] = false;
            }
        }
    }

    for (int i = 0; i <= n - 3; ++i) {
        if (!pal[0 * n + i]) continue;
        for (int j = i + 1; j <= n - 2; ++j) {
            if (pal[(i + 1) * n + j] && pal[(j + 1) * n + (n - 1)]) {
                free(pal);
                return true;
            }
        }
    }

    free(pal);
    return false;
}
```

## Csharp

```csharp
public class Solution
{
    public bool CheckPartitioning(string s)
    {
        int n = s.Length;
        bool[,] pal = new bool[n, n];

        // Precompute palindrome table
        for (int i = n - 1; i >= 0; i--)
        {
            for (int j = i; j < n; j++)
            {
                if (s[i] == s[j] && (j - i < 2 || pal[i + 1, j - 1]))
                {
                    pal[i, j] = true;
                }
            }
        }

        // Try all possible two cuts
        for (int i = 1; i <= n - 2; i++)          // first cut after position i-1
        {
            if (!pal[0, i - 1]) continue;
            for (int j = i + 1; j <= n - 1; j++)   // second cut after position j-1
            {
                if (pal[i, j - 1] && pal[j, n - 1])
                    return true;
            }
        }

        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {boolean}
 */
var checkPartitioning = function(s) {
    const n = s.length;
    // pal[i][j] == 1 if s[i..j] is palindrome
    const pal = Array.from({ length: n }, () => new Uint8Array(n));
    
    for (let i = n - 1; i >= 0; --i) {
        for (let j = i; j < n; ++j) {
            if (s[i] === s[j] && (j - i < 2 || pal[i + 1][j - 1])) {
                pal[i][j] = 1;
            }
        }
    }
    
    // try all possible first and second cuts
    for (let i = 0; i <= n - 3; ++i) {          // first cut after index i
        if (!pal[0][i]) continue;
        for (let j = i + 1; j <= n - 2; ++j) {   // second cut after index j
            if (pal[i + 1][j] && pal[j + 1][n - 1]) {
                return true;
            }
        }
    }
    return false;
};
```

## Typescript

```typescript
function checkPartitioning(s: string): boolean {
    const n = s.length;
    const pal: boolean[][] = Array.from({ length: n }, () => Array(n).fill(false));
    for (let i = n - 1; i >= 0; --i) {
        for (let j = i; j < n; ++j) {
            if (s[i] === s[j] && (j - i < 2 || pal[i + 1][j - 1])) {
                pal[i][j] = true;
            }
        }
    }
    for (let i = 0; i <= n - 3; ++i) {
        if (!pal[0][i]) continue;
        for (let j = i + 1; j <= n - 2; ++j) {
            if (pal[i + 1][j] && pal[j + 1][n - 1]) {
                return true;
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
     * @param String $s
     * @return Boolean
     */
    function checkPartitioning($s) {
        $n = strlen($s);
        if ($n < 3) return false;

        // Precompute palindrome table
        $isPal = array_fill(0, $n, array_fill(0, $n, false));

        for ($center = 0; $center < $n; $center++) {
            // odd length palindromes
            $l = $center;
            $r = $center;
            while ($l >= 0 && $r < $n && $s[$l] === $s[$r]) {
                $isPal[$l][$r] = true;
                $l--;
                $r++;
            }
            // even length palindromes
            $l = $center;
            $r = $center + 1;
            while ($l >= 0 && $r < $n && $s[$l] === $s[$r]) {
                $isPal[$l][$r] = true;
                $l--;
                $r++;
            }
        }

        // Try all possible first and second cuts
        for ($i = 0; $i <= $n - 3; $i++) {
            if (!$isPal[0][$i]) continue;
            for ($j = $i + 1; $j <= $n - 2; $j++) {
                if ($isPal[$i + 1][$j] && $isPal[$j + 1][$n - 1]) {
                    return true;
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
    func checkPartitioning(_ s: String) -> Bool {
        let chars = Array(s)
        let n = chars.count
        if n < 3 { return false }
        
        var dp = Array(repeating: Array(repeating: false, count: n), repeatCount: n)
        for i in 0..<n {
            dp[i][i] = true
        }
        if n >= 2 {
            for i in 0..<(n - 1) {
                dp[i][i + 1] = chars[i] == chars[i + 1]
            }
        }
        if n > 2 {
            for len in 3...n {
                var i = 0
                while i + len - 1 < n {
                    let j = i + len - 1
                    dp[i][j] = (chars[i] == chars[j]) && dp[i + 1][j - 1]
                    i += 1
                }
            }
        }
        
        for i in 0..<(n - 2) {
            if !dp[0][i] { continue }
            for j in (i + 1)..<(n - 1) {
                if dp[i + 1][j] && dp[j + 1][n - 1] {
                    return true
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
    fun checkPartitioning(s: String): Boolean {
        val n = s.length
        if (n < 3) return false
        val isPal = Array(n) { BooleanArray(n) }
        for (len in 1..n) {
            var i = 0
            while (i + len <= n) {
                val j = i + len - 1
                if (s[i] == s[j] && (len <= 2 || isPal[i + 1][j - 1])) {
                    isPal[i][j] = true
                }
                i++
            }
        }
        for (i in 0 until n - 2) { // first cut after i
            if (!isPal[0][i]) continue
            for (j in i + 1 until n - 1) { // second cut after j
                if (isPal[i + 1][j] && isPal[j + 1][n - 1]) {
                    return true
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
  bool checkPartitioning(String s) {
    int n = s.length;
    // dp[i][j] is true if s[i..j] is a palindrome
    List<List<bool>> dp = List.generate(n, (_) => List.filled(n, false));

    for (int i = n - 1; i >= 0; --i) {
      dp[i][i] = true;
      for (int j = i + 1; j < n; ++j) {
        if (s.codeUnitAt(i) == s.codeUnitAt(j)) {
          if (j - i == 1 || dp[i + 1][j - 1]) {
            dp[i][j] = true;
          }
        }
      }
    }

    // try all possible first and second cuts
    for (int i = 0; i <= n - 3; ++i) {
      if (!dp[0][i]) continue; // first part not palindrome
      for (int j = i + 1; j <= n - 2; ++j) {
        if (dp[i + 1][j] && dp[j + 1][n - 1]) {
          return true;
        }
      }
    }

    return false;
  }
}
```

## Golang

```go
func checkPartitioning(s string) bool {
    n := len(s)
    if n < 3 {
        return false
    }
    dp := make([][]bool, n)
    for i := range dp {
        dp[i] = make([]bool, n)
    }
    // Precompute palindrome table
    for i := n - 1; i >= 0; i-- {
        for j := i; j < n; j++ {
            if s[i] == s[j] && (j-i < 2 || dp[i+1][j-1]) {
                dp[i][j] = true
            }
        }
    }
    // Try all possible cuts
    for i := 1; i <= n-2; i++ { // first cut after index i-1
        if !dp[0][i-1] {
            continue
        }
        for j := i + 1; j <= n-1; j++ { // second cut after index j-1
            if dp[i][j-1] && dp[j][n-1] {
                return true
            }
        }
    }
    return false
}
```

## Ruby

```ruby
def check_partitioning(s)
  n = s.length
  return false if n < 3

  is_pal = Array.new(n) { Array.new(n, false) }
  (0...n).each { |i| is_pal[i][i] = true }

  (2..n).each do |len|
    (0..(n - len)).each do |l|
      r = l + len - 1
      if s[l] == s[r]
        is_pal[l][r] = true if len == 2 || is_pal[l + 1][r - 1]
      end
    end
  end

  (0..(n - 3)).each do |i|
    next unless is_pal[0][i]
    ((i + 1)..(n - 2)).each do |j|
      return true if is_pal[i + 1][j] && is_pal[j + 1][n - 1]
    end
  end

  false
end
```

## Scala

```scala
object Solution {
    def checkPartitioning(s: String): Boolean = {
        val n = s.length
        val isPal = Array.ofDim[Boolean](n, n)
        var i = 0
        while (i < n) {
            isPal(i)(i) = true
            i += 1
        }
        var len = 2
        while (len <= n) {
            var l = 0
            while (l + len <= n) {
                val r = l + len - 1
                if (s(l) == s(r)) {
                    if (len == 2) isPal(l)(r) = true
                    else isPal(l)(r) = isPal(l + 1)(r - 1)
                }
                l += 1
            }
            len += 1
        }
        var firstCut = 0
        while (firstCut < n - 2) {
            if (isPal(0)(firstCut)) {
                var secondCut = firstCut + 1
                while (secondCut < n - 1) {
                    if (isPal(firstCut + 1)(secondCut) && isPal(secondCut + 1)(n - 1))
                        return true
                    secondCut += 1
                }
            }
            firstCut += 1
        }
        false
    }
}
```

## Rust

```rust
impl Solution {
    pub fn check_partitioning(s: String) -> bool {
        let bytes = s.as_bytes();
        let n = bytes.len();
        if n < 3 {
            return false;
        }
        // dp[i][j] == true if s[i..=j] is a palindrome
        let mut dp = vec![vec![false; n]; n];
        for i in (0..n).rev() {
            for j in i..n {
                if bytes[i] == bytes[j] && (j - i <= 1 || dp[i + 1][j - 1]) {
                    dp[i][j] = true;
                }
            }
        }

        // try all possible two cut positions
        for i in 0..=n - 3 {
            if !dp[0][i] {
                continue;
            }
            for j in i + 1..=n - 2 {
                if dp[i + 1][j] && dp[j + 1][n - 1] {
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
(define/contract (check-partitioning s)
  (-> string? boolean?)
  (let* ((n (string-length s))
         (pal? (make-vector n)))
    ;; initialize rows
    (for ([i (in-range n)])
      (vector-set! pal? i (make-vector n #f)))
    ;; odd length palindromes
    (for ([c (in-range n)])
      (let loop ((l c) (r c))
        (when (and (>= l 0) (< r n)
                   (char=? (string-ref s l) (string-ref s r)))
          (vector-set! (vector-ref pal? l) r #t)
          (loop (sub1 l) (add1 r)))))
    ;; even length palindromes
    (for ([c (in-range (- n 1))])
      (let loop ((l c) (r (add1 c)))
        (when (and (>= l 0) (< r n)
                   (char=? (string-ref s l) (string-ref s r)))
          (vector-set! (vector-ref pal? l) r #t)
          (loop (sub1 l) (add1 r)))))
    ;; try all split positions
    (let loop-i ((i 0))
      (if (> i (- n 3))
          #f
          (if (not (vector-ref (vector-ref pal? 0) i))
              (loop-i (add1 i))
              (let loop-j ((j (add1 i)))
                (cond
                  [(> j (- n 2)) (loop-i (add1 i))]
                  [(and (vector-ref (vector-ref pal? (add1 i)) j)
                        (vector-ref (vector-ref pal? (add1 j)) (sub1 n))) #t]
                  [else (loop-j (add1 j))]))))))))
```

## Erlang

```erlang
-module(solution).
-export([check_partitioning/1]).

-spec check_partitioning(S :: unicode:unicode_binary()) -> boolean().
check_partitioning(S) ->
    Chars = string:to_charlist(S),
    N = length(Chars),
    Tuple = list_to_tuple(Chars),
    Tab = ets:new(pal_tab, [set, private]),
    build_pal(Tuple, N, Tab),
    Result = find_split(N, Tab),
    ets:delete(Tab),
    Result.

build_pal(_Tuple, 0, _Tab) -> ok;
build_pal(Tuple, N, Tab) ->
    lists:foreach(
      fun(Len) ->
          MaxI = N - Len,
          build_len(0, MaxI, Len, Tuple, Tab)
      end,
      lists:seq(1, N)
    ).

build_len(I, MaxI, _Len, _Tuple, _Tab) when I > MaxI -> ok;
build_len(I, MaxI, Len, Tuple, Tab) ->
    J = I + Len - 1,
    Ci = element(I + 1, Tuple),
    Cj = element(J + 1, Tuple),
    case Ci == Cj of
        true ->
            PalInner = if Len =< 2 -> true;
                          true -> ets:lookup(Tab, {I + 1, J - 1}) =/= [] end,
            case PalInner of
                true -> ets:insert(Tab, {{I, J}, true});
                false -> ok
            end;
        false -> ok
    end,
    build_len(I + 1, MaxI, Len, Tuple, Tab).

find_split(N, Tab) ->
    find_i(0, N - 3, N, Tab).

find_i(I, MaxI, _N, _Tab) when I > MaxI -> false;
find_i(I, MaxI, N, Tab) ->
    case ets:lookup(Tab, {0, I}) of
        [] -> find_i(I + 1, MaxI, N, Tab);
        _  ->
            case find_j(I + 1, N - 2, I, N, Tab) of
                true -> true;
                false -> find_i(I + 1, MaxI, N, Tab)
            end
    end.

find_j(J, MaxJ, _I, _N, _Tab) when J > MaxJ -> false;
find_j(J, MaxJ, I, N, Tab) ->
    case ets:lookup(Tab, {I + 1, J}) of
        [] -> find_j(J + 1, MaxJ, I, N, Tab);
        _  ->
            case ets:lookup(Tab, {J + 1, N - 1}) of
                [] -> find_j(J + 1, MaxJ, I, N, Tab);
                _  -> true
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec check_partitioning(s :: String.t()) :: boolean()
  def check_partitioning(s) do
    n = String.length(s)
    chars = s |> String.to_charlist() |> List.to_tuple()
    table = :ets.new(:pal, [:set, :private])

    # substrings of length 1
    for i <- 0..(n - 1) do
      :ets.insert(table, {{i, i}, true})
    end

    # substrings of length 2
    for i <- 0..(n - 2) do
      if elem(chars, i) == elem(chars, i + 1) do
        :ets.insert(table, {{i, i + 1}, true})
      end
    end

    # substrings of length >= 3
    for len <- 3..n do
      max_i = n - len
      for i <- 0..max_i do
        j = i + len - 1
        if elem(chars, i) == elem(chars, j) and :ets.member?(table, {i + 1, j - 1}) do
          :ets.insert(table, {{i, j}, true})
        end
      end
    end

    Enum.any?(0..(n - 3), fn i ->
      if :ets.member?(table, {0, i}) do
        Enum.any?((i + 1)..(n - 2), fn j ->
          :ets.member?(table, {i + 1, j}) and :ets.member?(table, {j + 1, n - 1})
        end)
      else
        false
      end
    end)
  end
end
```
