# 0115. Distinct Subsequences

## Cpp

```cpp
class Solution {
public:
    int numDistinct(string s, string t) {
        int n = t.size();
        vector<int> dp(n + 1, 0);
        dp[0] = 1;
        for (char sc : s) {
            for (int j = n; j >= 1; --j) {
                if (sc == t[j - 1]) {
                    dp[j] += dp[j - 1];
                }
            }
        }
        return dp[n];
    }
};
```

## Java

```java
class Solution {
    public int numDistinct(String s, String t) {
        int m = s.length();
        int n = t.length();
        if (n > m) return 0;
        int[][] dp = new int[m + 1][n + 1];
        // Empty target can be formed by deleting all characters
        for (int i = 0; i <= m; i++) {
            dp[i][0] = 1;
        }
        for (int i = 1; i <= m; i++) {
            char sc = s.charAt(i - 1);
            for (int j = 1; j <= n; j++) {
                char tc = t.charAt(j - 1);
                if (sc == tc) {
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                } else {
                    dp[i][j] = dp[i - 1][j];
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
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        if n == 0:
            return 1
        if m == 0:
            return 0

        dp = [0] * (n + 1)
        dp[0] = 1  # empty t can be formed from any prefix of s

        for i in range(1, m + 1):
            # update dp[j] using previous row values; iterate backwards
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[n]
```

## Python3

```python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(t)
        if n == 0:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 1
        for ch_s in s:
            for j in range(n, 0, -1):
                if ch_s == t[j - 1]:
                    dp[j] += dp[j - 1]
        return dp[n]
```

## C

```c
#include <string.h>
#include <stdlib.h>

int numDistinct(char* s, char* t) {
    int m = strlen(s);
    int n = strlen(t);
    if (n == 0) return 1;
    if (m == 0) return 0;

    int *dp = (int *)calloc(n + 1, sizeof(int));
    dp[0] = 1;

    for (int i = 1; i <= m; ++i) {
        for (int j = n; j >= 1; --j) {
            if (s[i - 1] == t[j - 1]) {
                dp[j] += dp[j - 1];
            }
        }
    }

    int result = dp[n];
    free(dp);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int NumDistinct(string s, string t)
    {
        int m = s.Length;
        int n = t.Length;
        if (n == 0) return 1;
        if (m == 0) return 0;

        long[] dp = new long[n + 1];
        dp[0] = 1;

        for (int i = 1; i <= m; i++)
        {
            for (int j = n; j >= 1; j--)
            {
                if (s[i - 1] == t[j - 1])
                {
                    dp[j] += dp[j - 1];
                }
            }
        }

        return (int)dp[n];
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var numDistinct = function(s, t) {
    const m = s.length, n = t.length;
    if (n > m) return 0;
    const dp = new Array(n + 1).fill(0);
    dp[0] = 1; // empty string
    
    for (let i = 0; i < m; i++) {
        const ch = s[i];
        for (let j = n; j >= 1; j--) {
            if (ch === t[j - 1]) {
                dp[j] += dp[j - 1];
            }
        }
    }
    
    return dp[n];
};
```

## Typescript

```typescript
function numDistinct(s: string, t: string): number {
    const m = s.length;
    const n = t.length;
    if (n === 0) return 1;
    if (m === 0) return 0;

    const dp: number[] = new Array(n + 1).fill(0);
    dp[0] = 1; // empty t

    for (let i = 1; i <= m; i++) {
        // iterate backwards to avoid overwriting needed values
        for (let j = n; j >= 1; j--) {
            if (s[i - 1] === t[j - 1]) {
                dp[j] += dp[j - 1];
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
     * @param String $t
     * @return Integer
     */
    function numDistinct($s, $t) {
        $n = strlen($s);
        $m = strlen($t);
        if ($m == 0) return 1;
        if ($n == 0 || $m > $n) return 0;

        $dp = array_fill(0, $m + 1, 0);
        $dp[0] = 1; // empty t

        for ($i = 1; $i <= $n; $i++) {
            for ($j = $m; $j >= 1; $j--) {
                if ($s[$i - 1] === $t[$j - 1]) {
                    $dp[$j] += $dp[$j - 1];
                }
            }
        }

        return $dp[$m];
    }
}
```

## Swift

```swift
class Solution {
    func numDistinct(_ s: String, _ t: String) -> Int {
        let m = s.count
        let n = t.count
        if n == 0 { return 1 }
        if m == 0 || n > m { return 0 }
        
        let sArr = Array(s)
        let tArr = Array(t)
        
        var prev = [Int](repeating: 0, count: n + 1)
        prev[0] = 1
        
        for i in 1...m {
            var cur = [Int](repeating: 0, count: n + 1)
            cur[0] = 1
            let si = sArr[i - 1]
            let maxJ = min(i, n)
            if maxJ >= 1 {
                for j in 1...maxJ {
                    if si == tArr[j - 1] {
                        cur[j] = prev[j - 1] + prev[j]
                    } else {
                        cur[j] = prev[j]
                    }
                }
            }
            prev = cur
        }
        
        return prev[n]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numDistinct(s: String, t: String): Int {
        val n = s.length
        val m = t.length
        if (m == 0) return 1
        if (n == 0) return 0
        val dp = LongArray(m + 1)
        dp[0] = 1L
        for (i in 1..n) {
            val sc = s[i - 1]
            for (j in m downTo 1) {
                if (sc == t[j - 1]) {
                    dp[j] += dp[j - 1]
                }
            }
        }
        return dp[m].toInt()
    }
}
```

## Dart

```dart
class Solution {
  int numDistinct(String s, String t) {
    int m = s.length;
    int n = t.length;
    if (n == 0) return 1;
    if (m == 0) return 0;

    List<int> prev = List.filled(n + 1, 0);
    prev[0] = 1; // empty t

    for (int i = 1; i <= m; i++) {
      List<int> cur = List.filled(n + 1, 0);
      cur[0] = 1; // empty t
      for (int j = 1; j <= n; j++) {
        if (s.codeUnitAt(i - 1) == t.codeUnitAt(j - 1)) {
          cur[j] = prev[j - 1] + prev[j];
        } else {
          cur[j] = prev[j];
        }
      }
      prev = cur;
    }

    return prev[n];
  }
}
```

## Golang

```go
func numDistinct(s string, t string) int {
	m, n := len(s), len(t)
	if n == 0 {
		return 1
	}
	if m == 0 {
		return 0
	}
	dp := make([]int, n+1)
	dp[0] = 1
	for i := 1; i <= m; i++ {
		for j := n; j >= 1; j-- {
			if s[i-1] == t[j-1] {
				dp[j] += dp[j-1]
			}
		}
	}
	return dp[n]
}
```

## Ruby

```ruby
def num_distinct(s, t)
  m = s.length
  n = t.length
  return 0 if n > m
  dp = Array.new(n + 1, 0)
  dp[0] = 1
  s_bytes = s.bytes
  t_bytes = t.bytes
  s_bytes.each do |sc|
    n.downto(1) do |j|
      dp[j] += dp[j - 1] if sc == t_bytes[j - 1]
    end
  end
  dp[n]
end
```

## Scala

```scala
object Solution {
    def numDistinct(s: String, t: String): Int = {
        val n = s.length
        val m = t.length
        if (m == 0) return 1
        if (n == 0 || m > n) return 0

        val dp = new Array[Long](m + 1)
        dp(0) = 1L

        var i = 0
        while (i < n) {
            var j = m - 1
            while (j >= 0) {
                if (s.charAt(i) == t.charAt(j)) {
                    dp(j + 1) += dp(j)
                }
                j -= 1
            }
            i += 1
        }

        dp(m).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_distinct(s: String, t: String) -> i32 {
        let s_bytes = s.as_bytes();
        let t_bytes = t.as_bytes();
        let n = s_bytes.len();
        let m = t_bytes.len();

        // dp for empty target string: one way (choose nothing)
        let mut prev = vec![1i64; n + 1];

        for i in 1..=m {
            let mut cur = vec![0i64; n + 1];
            for j in 1..=n {
                if t_bytes[i - 1] == s_bytes[j - 1] {
                    cur[j] = cur[j - 1] + prev[j - 1];
                } else {
                    cur[j] = cur[j - 1];
                }
            }
            prev = cur;
        }

        prev[n] as i32
    }
}
```

## Racket

```racket
(define/contract (num-distinct s t)
  (-> string? string? exact-integer?)
  (let* ((n (string-length s))
         (m (string-length t))
         (dp (make-vector (+ m 1) 0)))
    (vector-set! dp 0 1)
    (for ([i (in-range n)])
      (let ((si (string-ref s i)))
        (for ([j (in-range m 0 -1)]) ; j = m .. 1
          (when (char=? si (string-ref t (- j 1)))
            (vector-set! dp j (+ (vector-ref dp j)
                                 (vector-ref dp (- j 1))))))))
    (vector-ref dp m)))
```

## Erlang

```erlang
-module(solution).
-export([num_distinct/2]).

-spec num_distinct(S :: unicode:unicode_binary(), T :: unicode:unicode_binary()) -> integer().
num_distinct(S, T) ->
    SList = unicode:characters_to_list(S),
    TList = unicode:characters_to_list(T),
    TTuple = list_to_tuple(TList),
    LenT = tuple_size(TTuple),
    DP0 = array:new(LenT + 1, [{default, 0}]),
    DP1 = array:set(0, 1, DP0),
    FinalDP = process_s(SList, TTuple, DP1),
    array:get(LenT, FinalDP).

process_s([], _TTuple, DP) -> DP;
process_s([Sc | Rest], TTuple, DP) ->
    LenT = tuple_size(TTuple),
    NewDP = update_char(Sc, LenT, TTuple, DP),
    process_s(Rest, TTuple, NewDP).

update_char(_Char, 0, _TTuple, DP) -> DP;
update_char(Char, J, TTuple, DP) ->
    update_j(J, Char, TTuple, DP).

update_j(0, _Char, _TTuple, DP) -> DP;
update_j(J, Char, TTuple, DP) ->
    TChar = element(J, TTuple),
    OldJ = array:get(J, DP),
    NewDP =
        if Char == TChar ->
                Prev = array:get(J - 1, DP),
                array:set(J, OldJ + Prev, DP);
           true -> DP
        end,
    update_j(J - 1, Char, TTuple, NewDP).
```

## Elixir

```elixir
defmodule Solution do
  @spec num_distinct(s :: String.t(), t :: String.t()) :: integer()
  def num_distinct(s, t) do
    n = String.length(t)

    if n == 0 do
      1
    else
      s_chars = String.graphemes(s)
      t_tuple = List.to_tuple(String.graphemes(t))

      dp = :erlang.make_tuple(n + 1, 0) |> put_elem(1, 1)

      final_dp =
        Enum.reduce(s_chars, dp, fn cs, dp_acc ->
          Enum.reduce(:lists.seq(n, 1, -1), dp_acc, fn j, dp_inner ->
            if cs == elem(t_tuple, j) do
              val = elem(dp_inner, j + 1) + elem(dp_inner, j)
              put_elem(dp_inner, j + 1, val)
            else
              dp_inner
            end
          end)
        end)

      elem(final_dp, n + 1)
    end
  end
end
```
