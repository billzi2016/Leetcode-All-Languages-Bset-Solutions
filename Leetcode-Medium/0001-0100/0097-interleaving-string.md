# 0097. Interleaving String

## Cpp

```cpp
class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        int n = s1.size(), m = s2.size();
        if (n + m != (int)s3.size()) return false;
        // Ensure dp size corresponds to the shorter second string for O(min(n,m)) space
        if (m > n) {
            swap(s1, s2);
            swap(n, m);
        }
        vector<char> dp(m + 1, 0);
        dp[0] = 1;
        for (int j = 1; j <= m; ++j)
            dp[j] = dp[j - 1] && s2[j - 1] == s3[j - 1];
        for (int i = 1; i <= n; ++i) {
            dp[0] = dp[0] && s1[i - 1] == s3[i - 1];
            for (int j = 1; j <= m; ++j) {
                bool fromS1 = dp[j] && s1[i - 1] == s3[i + j - 1];
                bool fromS2 = dp[j - 1] && s2[j - 1] == s3[i + j - 1];
                dp[j] = fromS1 || fromS2;
            }
        }
        return dp[m];
    }
};
```

## Java

```java
class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        int n = s1.length(), m = s2.length();
        if (n + m != s3.length()) return false;
        // Ensure dp array size corresponds to the shorter string for O(min(n,m)) space
        if (m > n) { // swap to make s2 the shorter one
            String tmp = s1; s1 = s2; s2 = tmp;
            int tn = n; n = m; m = tn;
        }
        boolean[] dp = new boolean[m + 1];
        dp[0] = true;
        // Initialize first row (i=0)
        for (int j = 1; j <= m; ++j) {
            dp[j] = dp[j - 1] && s2.charAt(j - 1) == s3.charAt(j - 1);
        }
        for (int i = 1; i <= n; ++i) {
            // Update dp[0] for current i
            dp[0] = dp[0] && s1.charAt(i - 1) == s3.charAt(i - 1);
            for (int j = 1; j <= m; ++j) {
                int k = i + j - 1;
                boolean fromS1 = dp[j] && s1.charAt(i - 1) == s3.charAt(k);
                boolean fromS2 = dp[j - 1] && s2.charAt(j - 1) == s3.charAt(k);
                dp[j] = fromS1 || fromS2;
            }
        }
        return dp[m];
    }
}
```

## Python

```python
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n, m = len(s1), len(s2)
        if n + m != len(s3):
            return False

        # dp[j] means using first i chars of s1 and first j chars of s2 can form first i+j chars of s3
        dp = [False] * (m + 1)
        dp[0] = True

        # initialize first row (i=0)
        for j in range(1, m + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, n + 1):
            # update dp[0] for current i (j=0)
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, m + 1):
                k = i + j - 1
                dp[j] = (dp[j] and s1[i - 1] == s3[k]) or (dp[j - 1] and s2[j - 1] == s3[k])

        return dp[m]
```

## Python3

```python
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        if n + m != len(s3):
            return False

        # Ensure dp size corresponds to the shorter string for slight memory benefit
        if m > n:
            # swap to make m <= n
            s1, s2 = s2, s1
            n, m = m, n

        dp = [False] * (m + 1)
        dp[0] = True

        # Initialize first row (i=0)
        for j in range(1, m + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, n + 1):
            # Update dp[0] for current i (j=0)
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, m + 1):
                idx = i + j - 1
                from_s1 = dp[j] and s1[i - 1] == s3[idx]
                from_s2 = dp[j - 1] and s2[j - 1] == s3[idx]
                dp[j] = from_s1 or from_s2

        return dp[m]
```

## C

```c
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

bool isInterleave(char* s1, char* s2, char* s3) {
    int n = strlen(s1);
    int m = strlen(s2);
    int l = strlen(s3);
    if (n + m != l) return false;

    bool *dp = (bool *)malloc((m + 1) * (n + 1) * sizeof(bool));
    if (!dp) return false; // allocation failure, treat as false

    #define IDX(i,j) ((i)*(n+1)+(j))

    dp[IDX(0,0)] = true;

    for (int j = 1; j <= n; ++j)
        dp[IDX(0,j)] = dp[IDX(0,j-1)] && s1[j-1] == s3[j-1];

    for (int i = 1; i <= m; ++i) {
        dp[IDX(i,0)] = dp[IDX(i-1,0)] && s2[i-1] == s3[i-1];
        for (int j = 1; j <= n; ++j) {
            bool fromS1 = dp[IDX(i,j-1)] && s1[j-1] == s3[i+j-1];
            bool fromS2 = dp[IDX(i-1,j)] && s2[i-1] == s3[i+j-1];
            dp[IDX(i,j)] = fromS1 || fromS2;
        }
    }

    bool result = dp[IDX(m,n)];
    free(dp);
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public bool IsInterleave(string s1, string s2, string s3) {
        int n = s1.Length;
        int m = s2.Length;
        if (n + m != s3.Length) return false;

        bool[] dp = new bool[m + 1];
        dp[0] = true;
        for (int j = 1; j <= m; ++j)
            dp[j] = dp[j - 1] && s2[j - 1] == s3[j - 1];

        for (int i = 1; i <= n; ++i) {
            dp[0] = dp[0] && s1[i - 1] == s3[i - 1];
            for (int j = 1; j <= m; ++j) {
                int k = i + j - 1;
                dp[j] = (dp[j] && s1[i - 1] == s3[k]) || (dp[j - 1] && s2[j - 1] == s3[k]);
            }
        }

        return dp[m];
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s1
 * @param {string} s2
 * @param {string} s3
 * @return {boolean}
 */
var isInterleave = function(s1, s2, s3) {
    const n = s1.length, m = s2.length;
    if (n + m !== s3.length) return false;

    // dp[j] -> using first i chars of s1 and first j chars of s2
    const dp = new Array(m + 1).fill(false);
    dp[0] = true;

    // initialize first row (i = 0)
    for (let j = 1; j <= m; ++j) {
        dp[j] = dp[j - 1] && s2.charAt(j - 1) === s3.charAt(j - 1);
    }

    for (let i = 1; i <= n; ++i) {
        // update dp[0] for current i
        dp[0] = dp[0] && s1.charAt(i - 1) === s3.charAt(i - 1);
        for (let j = 1; j <= m; ++j) {
            const fromS1 = dp[j] && s1.charAt(i - 1) === s3.charAt(i + j - 1);
            const fromS2 = dp[j - 1] && s2.charAt(j - 1) === s3.charAt(i + j - 1);
            dp[j] = fromS1 || fromS2;
        }
    }

    return dp[m];
};
```

## Typescript

```typescript
function isInterleave(s1: string, s2: string, s3: string): boolean {
    const n = s1.length, m = s2.length;
    if (n + m !== s3.length) return false;

    const dp: boolean[] = new Array(m + 1).fill(false);
    dp[0] = true;

    for (let j = 1; j <= m; ++j) {
        dp[j] = dp[j - 1] && s2.charAt(j - 1) === s3.charAt(j - 1);
    }

    for (let i = 1; i <= n; ++i) {
        dp[0] = dp[0] && s1.charAt(i - 1) === s3.charAt(i - 1);
        for (let j = 1; j <= m; ++j) {
            const k = i + j - 1;
            dp[j] =
                (dp[j] && s1.charAt(i - 1) === s3.charAt(k)) ||
                (dp[j - 1] && s2.charAt(j - 1) === s3.charAt(k));
        }
    }

    return dp[m];
}
```

## Php

```php
class Solution {

    /**
     * @param String $s1
     * @param String $s2
     * @param String $s3
     * @return Boolean
     */
    function isInterleave($s1, $s2, $s3) {
        $n = strlen($s1);
        $m = strlen($s2);
        if ($n + $m !== strlen($s3)) {
            return false;
        }

        // dp[j] means s1[0..i-1] and s2[0..j-1] can form s3[0..i+j-1]
        $dp = array_fill(0, $m + 1, false);
        $dp[0] = true;

        for ($j = 1; $j <= $m; $j++) {
            $dp[$j] = $dp[$j - 1] && $s2[$j - 1] === $s3[$j - 1];
        }

        for ($i = 1; $i <= $n; $i++) {
            $dp[0] = $dp[0] && $s1[$i - 1] === $s3[$i - 1];
            for ($j = 1; $j <= $m; $j++) {
                $c = $s3[$i + $j - 1];
                $dp[$j] = ($dp[$j] && $s1[$i - 1] === $c) || ($dp[$j - 1] && $s2[$j - 1] === $c);
            }
        }

        return $dp[$m];
    }
}
```

## Swift

```swift
class Solution {
    func isInterleave(_ s1: String, _ s2: String, _ s3: String) -> Bool {
        let n = s1.count
        let m = s2.count
        if n + m != s3.count { return false }
        let a1 = Array(s1)
        let a2 = Array(s2)
        let a3 = Array(s3)
        var dp = [Bool](repeating: false, count: m + 1)
        dp[0] = true
        if m > 0 {
            for j in 1...m {
                dp[j] = dp[j - 1] && a2[j - 1] == a3[j - 1]
            }
        }
        if n == 0 { return dp[m] }
        for i in 1...n {
            dp[0] = dp[0] && a1[i - 1] == a3[i - 1]
            if m > 0 {
                for j in 1...m {
                    let fromS1 = dp[j] && a1[i - 1] == a3[i + j - 1]
                    let fromS2 = dp[j - 1] && a2[j - 1] == a3[i + j - 1]
                    dp[j] = fromS1 || fromS2
                }
            }
        }
        return dp[m]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isInterleave(s1: String, s2: String, s3: String): Boolean {
        val n = s1.length
        val m = s2.length
        if (n + m != s3.length) return false
        val dp = BooleanArray(m + 1)
        dp[0] = true
        for (j in 1..m) {
            dp[j] = dp[j - 1] && s2[j - 1] == s3[j - 1]
        }
        for (i in 1..n) {
            dp[0] = dp[0] && s1[i - 1] == s3[i - 1]
            for (j in 1..m) {
                val k = i + j - 1
                dp[j] = (dp[j] && s1[i - 1] == s3[k]) || (dp[j - 1] && s2[j - 1] == s3[k])
            }
        }
        return dp[m]
    }
}
```

## Dart

```dart
class Solution {
  bool isInterleave(String s1, String s2, String s3) {
    int n = s1.length;
    int m = s2.length;
    if (n + m != s3.length) return false;

    List<bool> dp = List.filled(m + 1, false);
    dp[0] = true;
    for (int j = 1; j <= m; ++j) {
      dp[j] = dp[j - 1] && s2[j - 1] == s3[j - 1];
    }

    for (int i = 1; i <= n; ++i) {
      dp[0] = dp[0] && s1[i - 1] == s3[i - 1];
      for (int j = 1; j <= m; ++j) {
        bool fromS1 = dp[j] && s1[i - 1] == s3[i + j - 1];
        bool fromS2 = dp[j - 1] && s2[j - 1] == s3[i + j - 1];
        dp[j] = fromS1 || fromS2;
      }
    }

    return dp[m];
  }
}
```

## Golang

```go
func isInterleave(s1 string, s2 string, s3 string) bool {
    n, m := len(s1), len(s2)
    if n+m != len(s3) {
        return false
    }
    // dp[j] represents using first i chars of s1 and j chars of s2
    dp := make([]bool, m+1)
    dp[0] = true
    for j := 1; j <= m; j++ {
        dp[j] = dp[j-1] && s2[j-1] == s3[j-1]
    }
    for i := 1; i <= n; i++ {
        dp[0] = dp[0] && s1[i-1] == s3[i-1]
        for j := 1; j <= m; j++ {
            idx := i + j - 1
            fromS1 := dp[j] && s1[i-1] == s3[idx]
            fromS2 := dp[j-1] && s2[j-1] == s3[idx]
            dp[j] = fromS1 || fromS2
        }
    }
    return dp[m]
}
```

## Ruby

```ruby
def is_interleave(s1, s2, s3)
  m = s1.length
  n = s2.length
  return false unless m + n == s3.length

  dp = Array.new(n + 1, false)
  dp[0] = true
  (1..n).each do |j|
    dp[j] = dp[j - 1] && s2.getbyte(j - 1) == s3.getbyte(j - 1)
  end

  (1..m).each do |i|
    dp[0] = dp[0] && s1.getbyte(i - 1) == s3.getbyte(i - 1)
    (1..n).each do |j|
      c = s3.getbyte(i + j - 1)
      dp[j] = (dp[j] && s1.getbyte(i - 1) == c) || (dp[j - 1] && s2.getbyte(j - 1) == c)
    end
  end

  dp[n]
end
```

## Scala

```scala
object Solution {
    def isInterleave(s1: String, s2: String, s3: String): Boolean = {
        val n = s1.length
        val m = s2.length
        if (n + m != s3.length) return false

        val dp = new Array[Boolean](m + 1)
        dp(0) = true
        for (j <- 1 to m) {
            dp(j) = dp(j - 1) && s2.charAt(j - 1) == s3.charAt(j - 1)
        }

        for (i <- 1 to n) {
            dp(0) = dp(0) && s1.charAt(i - 1) == s3.charAt(i - 1)
            for (j <- 1 to m) {
                val fromS1 = dp(j) && s1.charAt(i - 1) == s3.charAt(i + j - 1)
                val fromS2 = dp(j - 1) && s2.charAt(j - 1) == s3.charAt(i + j - 1)
                dp(j) = fromS1 || fromS2
            }
        }

        dp(m)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_interleave(s1: String, s2: String, s3: String) -> bool {
        let n = s1.len();
        let m = s2.len();
        if n + m != s3.len() {
            return false;
        }
        let s1b = s1.as_bytes();
        let s2b = s2.as_bytes();
        let s3b = s3.as_bytes();

        // dp[j] -> using first i chars of s1 and first j chars of s2
        let mut dp = vec![false; m + 1];
        dp[0] = true;

        for j in 1..=m {
            dp[j] = dp[j - 1] && s2b[j - 1] == s3b[j - 1];
        }

        for i in 1..=n {
            // update dp[0] for current i
            dp[0] = dp[0] && s1b[i - 1] == s3b[i - 1];
            for j in 1..=m {
                let k = i + j - 1;
                dp[j] = (dp[j] && s1b[i - 1] == s3b[k]) || (dp[j - 1] && s2b[j - 1] == s3b[k]);
            }
        }

        dp[m]
    }
}
```

## Racket

```racket
(define/contract (is-interleave s1 s2 s3)
  (-> string? string? string? boolean?)
  (let* ([n (string-length s1)]
         [m (string-length s2)]
         [l (string-length s3)])
    (if (not (= (+ n m) l))
        #false
        (let ([dp (make-vector (+ m 1) #false)])
          (vector-set! dp 0 #true)
          ;; initialize first row (i = 0)
          (for ([j (in-range 1 (add1 m))])
            (define prev (vector-ref dp (- j 1)))
            (define match? (char=? (string-ref s2 (- j 1))
                                   (string-ref s3 (- j 1))))
            (vector-set! dp j (and prev match?)))
          ;; iterate over i from 1 to n
          (for ([i (in-range 1 (add1 n))])
            ;; update dp[0] for current i
            (define prev0 (vector-ref dp 0))
            (define match0 (char=? (string-ref s1 (- i 1))
                                   (string-ref s3 (- i 1))))
            (vector-set! dp 0 (and prev0 match0))
            ;; update rest of the row
            (for ([j (in-range 1 (add1 m))])
              (define from-s1 (and (vector-ref dp j)
                                   (char=? (string-ref s1 (- i 1))
                                           (string-ref s3 (+ i j -1)))))
              (define from-s2 (and (vector-ref dp (- j 1))
                                   (char=? (string-ref s2 (- j 1))
                                           (string-ref s3 (+ i j -1)))))
              (vector-set! dp j (or from-s1 from-s2))))
          (vector-ref dp m)))))
```

## Erlang

```erlang
-module(solution).
-export([is_interleave/3]).

-spec is_interleave(S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary(), S3 :: unicode:unicode_binary()) -> boolean().
is_interleave(S1, S2, S3) ->
    S1List = unicode:characters_to_list(S1),
    S2List = unicode:characters_to_list(S2),
    S3List = unicode:characters_to_list(S3),
    N = length(S1List),
    M = length(S2List),
    L = length(S3List),
    case N + M == L of
        false -> false;
        true ->
            S1T = list_to_tuple(S1List),
            S2T = list_to_tuple(S2List),
            S3T = list_to_tuple(S3List),
            BaseRow = build_base_row(M, S2T, S3T),
            FinalRow = loop_i(1, N, BaseRow, S1T, S2T, S3T, M),
            lists:nth(M + 1, FinalRow)
    end.

build_base_row(M, S2T, S3T) ->
    build_base_row_loop(1, M, true, [true], S2T, S3T).

build_base_row_loop(J, M, PrevVal, AccRev, _S2T, _S3T) when J > M ->
    lists:reverse(AccRev);
build_base_row_loop(J, M, PrevVal, AccRev, S2T, S3T) ->
    Char2 = element(J, S2T),
    Char3 = element(J, S3T),
    Val = (PrevVal andalso Char2 == Char3),
    build_base_row_loop(J + 1, M, Val, [Val | AccRev], S2T, S3T).

loop_i(I, N, PrevRow, _S1T, _S2T, _S3T, _M) when I > N ->
    PrevRow;
loop_i(I, N, PrevRow, S1T, S2T, S3T, M) ->
    CurrRow = build_row(I, PrevRow, S1T, S2T, S3T, M),
    loop_i(I + 1, N, CurrRow, S1T, S2T, S3T, M).

build_row(I, PrevRow, S1T, S2T, S3T, M) ->
    Char1 = element(I, S1T),
    [Prev0 | PrevRest] = PrevRow,
    Char3_0 = element(I, S3T),
    Val0 = (Prev0 andalso Char1 == Char3_0),
    build_row_loop(1, M, PrevRest, S2T, S3T, I, Char1, Val0, [Val0]).

build_row_loop(J, M, _PrevIter, _S2T, _S3T, _I, _Char1, _LeftVal, AccRev) when J > M ->
    lists:reverse(AccRev);
build_row_loop(J, M, PrevIter, S2T, S3T, I, Char1, LeftVal, AccRev) ->
    [PrevJ | RestPrev] = PrevIter,
    Char2 = element(J, S2T),
    Char3 = element(I + J, S3T),
    TopOk = (PrevJ andalso Char1 == Char3),
    LeftOk = (LeftVal andalso Char2 == Char3),
    Val = TopOk orelse LeftOk,
    build_row_loop(J + 1, M, RestPrev, S2T, S3T, I, Char1, Val, [Val | AccRev]).
```

## Elixir

```elixir
defmodule Solution do
  @spec is_interleave(String.t(), String.t(), String.t()) :: boolean()
  def is_interleave(s1, s2, s3) do
    n = String.length(s1)
    m = String.length(s2)

    if n + m != String.length(s3) do
      false
    else
      s1c = String.to_charlist(s1)
      s2c = String.to_charlist(s2)
      s3c = String.to_charlist(s3)

      dp0 = :array.new(m + 1, false)
      dp = :array.set(0, true, dp0)

      dp =
        Enum.reduce(1..m, dp, fn j, acc ->
          prev = :array.get(j - 1, acc)
          cond = prev && Enum.at(s2c, j - 1) == Enum.at(s3c, j - 1)
          :array.set(j, cond, acc)
        end)

      dp =
        Enum.reduce(1..n, dp, fn i, acc ->
          first_prev = :array.get(0, acc)
          first_cond = first_prev && Enum.at(s1c, i - 1) == Enum.at(s3c, i - 1)
          acc = :array.set(0, first_cond, acc)

          Enum.reduce(1..m, acc, fn j, inner_acc ->
            idx = i + j - 1
            c3 = Enum.at(s3c, idx)

            from_s1 = (:array.get(j, inner_acc) && Enum.at(s1c, i - 1) == c3)
            from_s2 = (:array.get(j - 1, inner_acc) && Enum.at(s2c, j - 1) == c3)

            :array.set(j, from_s1 || from_s2, inner_acc)
          end)
        end)

      :array.get(m, dp)
    end
  end
end
```
