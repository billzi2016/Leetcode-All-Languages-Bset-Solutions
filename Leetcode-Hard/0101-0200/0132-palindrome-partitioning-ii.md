# 0132. Palindrome Partitioning II

## Cpp

```cpp
class Solution {
public:
    int minCut(string s) {
        int n = s.size();
        vector<int> cut(n + 1);
        for (int i = 0; i <= n; ++i) cut[i] = i - 1; // max cuts
        
        for (int center = 0; center < n; ++center) {
            // odd length palindromes
            for (int l = center, r = center; l >= 0 && r < n && s[l] == s[r]; --l, ++r) {
                cut[r + 1] = min(cut[r + 1], cut[l] + 1);
            }
            // even length palindromes
            for (int l = center - 1, r = center; l >= 0 && r < n && s[l] == s[r]; --l, ++r) {
                cut[r + 1] = min(cut[r + 1], cut[l] + 1);
            }
        }
        return cut[n];
    }
};
```

## Java

```java
class Solution {
    public int minCut(String s) {
        int n = s.length();
        if (n <= 1) return 0;
        char[] ch = s.toCharArray();
        boolean[][] pal = new boolean[n][n];
        // fill palindrome table
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                if (ch[i] == ch[j] && (j - i <= 2 || pal[i + 1][j - 1])) {
                    pal[i][j] = true;
                }
            }
        }
        int[] dp = new int[n + 1];
        dp[0] = -1; // empty string needs -1 cuts so that first palindrome adds 0
        for (int i = 1; i <= n; i++) {
            dp[i] = Integer.MAX_VALUE;
            for (int j = 0; j < i; j++) {
                if (pal[j][i - 1]) {
                    dp[i] = Math.min(dp[i], dp[j] + 1);
                }
            }
        }
        return dp[n];
    }
}
```

## Python

```python
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [i for i in range(n)]  # max cuts for prefix ending at i
        for i in range(n):
            # odd length palindromes centered at i
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                if l == 0:
                    dp[r] = 0
                else:
                    dp[r] = min(dp[r], dp[l - 1] + 1)
                l -= 1
                r += 1
            # even length palindromes centered between i-1 and i
            l, r = i - 1, i
            while l >= 0 and r < n and s[l] == s[r]:
                if l == 0:
                    dp[r] = 0
                else:
                    dp[r] = min(dp[r], dp[l - 1] + 1)
                l -= 1
                r += 1
        return dp[-1]
```

## Python3

```python
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            si = s[i]
            row_i = is_pal[i]
            for j in range(i, n):
                if si == s[j] and (j - i < 2 or is_pal[i + 1][j - 1]):
                    row_i[j] = True
        dp = [0] * n
        for i in range(n):
            if is_pal[0][i]:
                dp[i] = 0
                continue
            min_cut = i
            for j in range(i):
                if is_pal[j + 1][i]:
                    cut = dp[j] + 1
                    if cut < min_cut:
                        min_cut = cut
            dp[i] = min_cut
        return dp[-1]
```

## C

```c
#include <string.h>
#include <stdlib.h>

static inline int min(int a, int b) {
    return a < b ? a : b;
}

int minCut(char* s) {
    int n = (int)strlen(s);
    if (n == 0) return 0;

    int *dp = (int *)malloc((n + 1) * sizeof(int));
    for (int i = 0; i <= n; ++i) dp[i] = i - 1; // dp[0] = -1, max cuts otherwise

    for (int center = 0; center < n; ++center) {
        // odd length palindromes
        int l = center, r = center;
        while (l >= 0 && r < n && s[l] == s[r]) {
            dp[r + 1] = min(dp[r + 1], dp[l] + 1);
            --l; ++r;
        }
        // even length palindromes
        l = center - 1; r = center;
        while (l >= 0 && r < n && s[l] == s[r]) {
            dp[r + 1] = min(dp[r + 1], dp[l] + 1);
            --l; ++r;
        }
    }

    int result = dp[n];
    free(dp);
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int MinCut(string s) {
        int n = s.Length;
        bool[,] isPal = new bool[n, n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                if (s[i] == s[j] && (i - j < 2 || isPal[j + 1, i - 1])) {
                    isPal[j, i] = true;
                }
            }
        }

        int[] dp = new int[n + 1];
        dp[0] = -1; // base: empty string needs -1 cuts so first palindrome adds 0
        for (int i = 1; i <= n; i++) {
            dp[i] = int.MaxValue;
            for (int j = 0; j < i; j++) {
                if (isPal[j, i - 1]) {
                    dp[i] = Math.Min(dp[i], dp[j] + 1);
                }
            }
        }

        return dp[n];
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minCut = function(s) {
    const n = s.length;
    // cuts[i] = minimum cuts for prefix s[0..i-1]
    const cuts = new Array(n + 1);
    for (let i = 0; i <= n; i++) {
        cuts[i] = i - 1; // worst case: cut before each character
    }

    for (let center = 0; center < n; center++) {
        // odd length palindromes
        for (let l = center, r = center; l >= 0 && r < n && s[l] === s[r]; l--, r++) {
            cuts[r + 1] = Math.min(cuts[r + 1], cuts[l] + 1);
        }
        // even length palindromes
        for (let l = center, r = center + 1; l >= 0 && r < n && s[l] === s[r]; l--, r++) {
            cuts[r + 1] = Math.min(cuts[r + 1], cuts[l] + 1);
        }
    }

    return cuts[n];
};
```

## Typescript

```typescript
function minCut(s: string): number {
    const n = s.length;
    // Precompute palindrome substrings
    const isPal: boolean[][] = Array.from({ length: n }, () => Array(n).fill(false));
    for (let center = 0; center < n; ++center) {
        // odd length palindromes
        let l = center, r = center;
        while (l >= 0 && r < n && s[l] === s[r]) {
            isPal[l][r] = true;
            --l; ++r;
        }
        // even length palindromes
        l = center; r = center + 1;
        while (l >= 0 && r < n && s[l] === s[r]) {
            isPal[l][r] = true;
            --l; ++r;
        }
    }

    const dp: number[] = new Array(n + 1);
    dp[0] = -1; // base case: no characters need -1 cuts so that a whole palindrome yields 0
    for (let i = 1; i <= n; ++i) {
        dp[i] = i - 1; // worst case: cut each character
        for (let j = 0; j < i; ++j) {
            if (isPal[j][i - 1]) {
                dp[i] = Math.min(dp[i], dp[j] + 1);
            }
        }
    }
    return dp[n];
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minCut($s) {
        $n = strlen($s);
        // dp[i] = minimum cuts for prefix s[0..i-1]
        $dp = array_fill(0, $n + 1, 0);
        for ($i = 0; $i <= $n; $i++) {
            $dp[$i] = $i - 1; // worst case: cut each character
        }

        for ($center = 0; $center < $n; $center++) {
            // odd length palindromes
            $l = $center;
            $r = $center;
            while ($l >= 0 && $r < $n && $s[$l] === $s[$r]) {
                $dp[$r + 1] = min($dp[$r + 1], $dp[$l] + 1);
                $l--;
                $r++;
            }

            // even length palindromes
            $l = $center;
            $r = $center + 1;
            while ($l >= 0 && $r < $n && $s[$l] === $s[$r]) {
                $dp[$r + 1] = min($dp[$r + 1], $dp[$l] + 1);
                $l--;
                $r++;
            }
        }

        return $dp[$n];
    }
}
```

## Swift

```swift
class Solution {
    func minCut(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        if n <= 1 { return 0 }
        
        var isPal = Array(repeating: Array(repeating: false, count: n), count: n)
        for i in stride(from: n - 1, through: 0, by: -1) {
            for j in i..<n {
                if chars[i] == chars[j] && (j - i < 2 || isPal[i + 1][j - 1]) {
                    isPal[i][j] = true
                }
            }
        }
        
        var dp = Array(repeating: Int.max, count: n + 1)
        dp[0] = -1   // base case: no cuts before the first character
        
        for i in 1...n {
            for j in 0..<i {
                if isPal[j][i - 1] {
                    dp[i] = min(dp[i], dp[j] + 1)
                }
            }
        }
        
        return dp[n]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minCut(s: String): Int {
        val n = s.length
        if (n <= 1) return 0
        val isPal = Array(n) { BooleanArray(n) }
        for (i in n - 1 downTo 0) {
            for (j in i until n) {
                if (s[i] == s[j] && (j - i < 2 || isPal[i + 1][j - 1])) {
                    isPal[i][j] = true
                }
            }
        }
        val dp = IntArray(n + 1) { Int.MAX_VALUE }
        dp[0] = -1
        for (i in 1..n) {
            var best = Int.MAX_VALUE
            for (j in 0 until i) {
                if (isPal[j][i - 1]) {
                    val cand = dp[j] + 1
                    if (cand < best) best = cand
                }
            }
            dp[i] = best
        }
        return dp[n]
    }
}
```

## Dart

```dart
class Solution {
  int minCut(String s) {
    int n = s.length;
    List<List<bool>> isPal = List.generate(n, (_) => List.filled(n, false));
    for (int center = 0; center < n; ++center) {
      // odd length palindromes
      int l = center, r = center;
      while (l >= 0 && r < n && s[l] == s[r]) {
        isPal[l][r] = true;
        l--;
        r++;
      }
      // even length palindromes
      l = center;
      r = center + 1;
      while (l >= 0 && r < n && s[l] == s[r]) {
        isPal[l][r] = true;
        l--;
        r++;
      }
    }

    List<int> dp = List.filled(n + 1, 0);
    dp[0] = -1; // no cuts before the first character
    for (int i = 1; i <= n; ++i) {
      dp[i] = i - 1; // worst case: cut each character
      for (int j = 0; j < i; ++j) {
        if (isPal[j][i - 1]) {
          int candidate = dp[j] + 1;
          if (candidate < dp[i]) dp[i] = candidate;
        }
      }
    }
    return dp[n];
  }
}
```

## Golang

```go
func minCut(s string) int {
	n := len(s)
	if n <= 1 {
		return 0
	}
	pal := make([][]bool, n)
	for i := range pal {
		pal[i] = make([]bool, n)
	}
	for i := n - 1; i >= 0; i-- {
		for j := i; j < n; j++ {
			if s[i] == s[j] && (j-i < 2 || pal[i+1][j-1]) {
				pal[i][j] = true
			}
		}
	}
	cuts := make([]int, n)
	for i := 0; i < n; i++ {
		if pal[0][i] {
			cuts[i] = 0
			continue
		}
		min := i // worst case: cut each character
		for j := 1; j <= i; j++ {
			if pal[j][i] && cuts[j-1]+1 < min {
				min = cuts[j-1] + 1
			}
		}
		cuts[i] = min
	}
	return cuts[n-1]
}
```

## Ruby

```ruby
def min_cut(s)
  n = s.length
  dp = Array.new(n) { |i| i } # worst case cuts

  # odd length palindromes
  (0...n).each do |center|
    l = center
    r = center
    while l >= 0 && r < n && s[l] == s[r]
      if l == 0
        dp[r] = 0
      else
        cuts = dp[l - 1] + 1
        dp[r] = cuts if cuts < dp[r]
      end
      l -= 1
      r += 1
    end
  end

  # even length palindromes
  (0...n - 1).each do |center|
    l = center
    r = center + 1
    while l >= 0 && r < n && s[l] == s[r]
      if l == 0
        dp[r] = 0
      else
        cuts = dp[l - 1] + 1
        dp[r] = cuts if cuts < dp[r]
      end
      l -= 1
      r += 1
    end
  end

  dp[n - 1]
end
```

## Scala

```scala
object Solution {
    def minCut(s: String): Int = {
        val n = s.length
        if (n <= 1) return 0

        val isPal = Array.ofDim[Boolean](n, n)

        for (center <- 0 until n) {
            var l = center
            var r = center
            while (l >= 0 && r < n && s.charAt(l) == s.charAt(r)) {
                isPal(l)(r) = true
                l -= 1
                r += 1
            }
            l = center
            r = center + 1
            while (l >= 0 && r < n && s.charAt(l) == s.charAt(r)) {
                isPal(l)(r) = true
                l -= 1
                r += 1
            }
        }

        val dp = new Array[Int](n + 1)
        dp(0) = -1

        for (i <- 1 to n) {
            var best = Int.MaxValue
            var j = 0
            while (j < i) {
                if (isPal(j)(i - 1)) {
                    val cut = dp(j) + 1
                    if (cut < best) best = cut
                }
                j += 1
            }
            dp(i) = best
        }

        dp(n)
    }
}
```

## Rust

```rust
use std::cmp::min;

impl Solution {
    pub fn min_cut(s: String) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        if n == 0 {
            return 0;
        }
        // palindrome[i][j] is true if s[i..=j] is a palindrome
        let mut palindrome = vec![vec![false; n]; n];
        for i in (0..n).rev() {
            for j in i..n {
                if bytes[i] == bytes[j] && (j - i < 2 || palindrome[i + 1][j - 1]) {
                    palindrome[i][j] = true;
                }
            }
        }

        // dp[i]: min cuts needed for s[0..=i]
        let mut dp = vec![0usize; n];
        for i in 0..n {
            if palindrome[0][i] {
                dp[i] = 0;
            } else {
                dp[i] = i; // worst case: cut each character
                for j in 1..=i {
                    if palindrome[j][i] {
                        dp[i] = min(dp[i], dp[j - 1] + 1);
                    }
                }
            }
        }

        dp[n - 1] as i32
    }
}
```

## Racket

```racket
(define/contract (min-cut s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (pal (make-vector n)))
    ;; initialize palindrome table
    (for ([i (in-range n)])
      (vector-set! pal i (make-vector n #f)))
    ;; fill palindrome table using center expansion
    (for ([center (in-range n)])
      ;; odd length palindromes
      (let loop ((l center) (r center))
        (when (and (>= l 0) (< r n)
                   (char=? (string-ref s l) (string-ref s r)))
          (vector-set! (vector-ref pal l) r #t)
          (loop (- l 1) (+ r 1))))
      ;; even length palindromes
      (let loop ((l center) (r (+ center 1)))
        (when (and (>= l 0) (< r n)
                   (char=? (string-ref s l) (string-ref s r)))
          (vector-set! (vector-ref pal l) r #t)
          (loop (- l 1) (+ r 1)))))
    ;; dynamic programming for minimum cuts
    (let ((dp (make-vector (+ n 1) 0)))
      (vector-set! dp 0 -1) ; base case: empty string needs -1 cuts
      (for ([i (in-range 1 (+ n 1))])
        (vector-set! dp i (- i 1)) ; worst case: cut before each character
        (for ([j (in-range 0 i)])
          (when (vector-ref (vector-ref pal j) (- i 1))
            (let ((cand (+ 1 (vector-ref dp j))))
              (when (< cand (vector-ref dp i))
                (vector-set! dp i cand))))))
      (vector-ref dp n))))
```

## Erlang

```erlang
-module(solution).
-export([min_cut/1]).

-spec min_cut(S :: unicode:unicode_binary()) -> integer().
min_cut(S) ->
    L = binary:bin_to_list(S),
    N = length(L),
    T = list_to_tuple(L),
    InitCuts = maps:from_list([{I, I-1} || I <- lists:seq(0, N)]),
    FinalCuts = loop(0, N, T, InitCuts),
    maps:get(N, FinalCuts).

loop(I, N, _T, Cuts) when I >= N ->
    Cuts;
loop(I, N, T, Cuts) ->
    Cuts1 = expand(I, I, T, N, Cuts),
    Cuts2 = expand(I, I+1, T, N, Cuts1),
    loop(I + 1, N, T, Cuts2).

expand(L, R, _T, N, Cuts) when L < 0; R >= N ->
    Cuts;
expand(L, R, T, N, Cuts) ->
    case element(T, L + 1) =:= element(T, R + 1) of
        true ->
            NewCut = maps:get(L, Cuts) + 1,
            RightIdx = R + 1,
            Existing = maps:get(RightIdx, Cuts),
            UpdatedCuts = if NewCut < Existing -> maps:put(RightIdx, NewCut, Cuts); true -> Cuts end,
            expand(L - 1, R + 1, T, N, UpdatedCuts);
        false ->
            Cuts
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_cut(s :: String.t()) :: integer()
  def min_cut(s) do
    n = byte_size(s)

    # cuts[i] = minimum cuts for prefix of length i (0..n)
    cuts = :array.from_list(Enum.map(0..n, fn i -> i - 1 end))

    final_cuts =
      Enum.reduce(0..(n - 1), cuts, fn i, acc ->
        acc = expand(s, n, i, i, acc)       # odd length palindromes
        expand(s, n, i, i + 1, acc)         # even length palindromes
      end)

    :array.get(n, final_cuts)
  end

  defp expand(_s, _n, l, r, cuts) when l < 0 or r >= _n do
    cuts
  end

  defp expand(s, n, l, r, cuts) do
    if :binary.at(s, l) == :binary.at(s, r) do
      cur = :array.get(r + 1, cuts)
      left = :array.get(l, cuts)
      new_val = if left + 1 < cur, do: left + 1, else: cur
      cuts2 = :array.set(r + 1, new_val, cuts)
      expand(s, n, l - 1, r + 1, cuts2)
    else
      cuts
    end
  end
end
```
