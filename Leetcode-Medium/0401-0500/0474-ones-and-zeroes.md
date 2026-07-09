# 0474. Ones and Zeroes

## Cpp

```cpp
class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        for (const string& s : strs) {
            int zeros = 0, ones = 0;
            for (char c : s) {
                if (c == '0') ++zeros;
                else ++ones;
            }
            for (int i = m; i >= zeros; --i) {
                for (int j = n; j >= ones; --j) {
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1);
                }
            }
        }
        return dp[m][n];
    }
};
```

## Java

```java
class Solution {
    public int findMaxForm(String[] strs, int m, int n) {
        int[][] dp = new int[m + 1][n + 1];
        for (String s : strs) {
            int zeros = 0, ones = 0;
            for (char c : s.toCharArray()) {
                if (c == '0') zeros++;
                else ones++;
            }
            for (int i = m; i >= zeros; i--) {
                for (int j = n; j >= ones; j--) {
                    dp[i][j] = Math.max(dp[i][j], dp[i - zeros][j - ones] + 1);
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
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # dp[i][j] = max number of strings using at most i zeros and j ones
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for s in strs:
            zeros = s.count('0')
            ones = len(s) - zeros
            # iterate backwards to avoid reuse within same iteration
            for i in range(m, zeros - 1, -1):
                row = dp[i]
                prev_row = dp[i - zeros]
                for j in range(n, ones - 1, -1):
                    # choose current string if it improves the count
                    candidate = prev_row[j - ones] + 1
                    if candidate > row[j]:
                        row[j] = candidate
        return dp[m][n]
```

## Python3

```python
from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            zeros = s.count('0')
            ones = len(s) - zeros
            for i in range(m, zeros - 1, -1):
                row = dp[i]
                prev_row = dp[i - zeros]
                for j in range(n, ones - 1, -1):
                    # max of not taking or taking this string
                    if prev_row[j - ones] + 1 > row[j]:
                        row[j] = prev_row[j - ones] + 1
        return dp[m][n]
```

## C

```c
#include <string.h>

int findMaxForm(char** strs, int strsSize, int m, int n) {
    static int dp[101][101];
    for (int i = 0; i <= m; ++i)
        for (int j = 0; j <= n; ++j)
            dp[i][j] = 0;

    for (int idx = 0; idx < strsSize; ++idx) {
        const char *s = strs[idx];
        int zeros = 0, ones = 0;
        while (*s) {
            if (*s == '0') ++zeros;
            else ++ones;
            ++s;
        }
        for (int i = m; i >= zeros; --i) {
            for (int j = n; j >= ones; --j) {
                int cand = dp[i - zeros][j - ones] + 1;
                if (cand > dp[i][j]) dp[i][j] = cand;
            }
        }
    }
    return dp[m][n];
}
```

## Csharp

```csharp
public class Solution
{
    public int FindMaxForm(string[] strs, int m, int n)
    {
        int[,] dp = new int[m + 1, n + 1];

        foreach (var s in strs)
        {
            int zeros = 0, ones = 0;
            foreach (char c in s)
            {
                if (c == '0') zeros++;
                else ones++;
            }

            for (int i = m; i >= zeros; i--)
            {
                for (int j = n; j >= ones; j--)
                {
                    dp[i, j] = Math.Max(dp[i, j], dp[i - zeros, j - ones] + 1);
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
 * @param {string[]} strs
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var findMaxForm = function(strs, m, n) {
    const dp = Array.from({ length: m + 1 }, () => Array(n + 1).fill(0));
    for (const s of strs) {
        let zeros = 0, ones = 0;
        for (let ch of s) {
            if (ch === '0') zeros++;
            else ones++;
        }
        for (let i = m; i >= zeros; i--) {
            for (let j = n; j >= ones; j--) {
                dp[i][j] = Math.max(dp[i][j], dp[i - zeros][j - ones] + 1);
            }
        }
    }
    return dp[m][n];
};
```

## Typescript

```typescript
function findMaxForm(strs: string[], m: number, n: number): number {
    const dp: number[][] = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));

    for (const s of strs) {
        let zeros = 0;
        let ones = 0;
        for (const ch of s) {
            if (ch === '0') zeros++;
            else ones++;
        }

        for (let i = m; i >= zeros; i--) {
            for (let j = n; j >= ones; j--) {
                const candidate = dp[i - zeros][j - ones] + 1;
                if (candidate > dp[i][j]) dp[i][j] = candidate;
            }
        }
    }

    return dp[m][n];
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $strs
     * @param Integer $m
     * @param Integer $n
     * @return Integer
     */
    function findMaxForm($strs, $m, $n) {
        // Initialize DP table with zeros
        $dp = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));

        foreach ($strs as $s) {
            $zeroCount = substr_count($s, '0');
            $oneCount = strlen($s) - $zeroCount;

            // Traverse dp table backwards to avoid reuse within same iteration
            for ($i = $m; $i >= $zeroCount; $i--) {
                for ($j = $n; $j >= $oneCount; $j--) {
                    $candidate = $dp[$i - $zeroCount][$j - $oneCount] + 1;
                    if ($candidate > $dp[$i][$j]) {
                        $dp[$i][$j] = $candidate;
                    }
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
    func findMaxForm(_ strs: [String], _ m: Int, _ n: Int) -> Int {
        var dp = Array(repeating: Array(repeating: 0, count: n + 1), count: m + 1)
        
        for s in strs {
            var zeros = 0
            var ones = 0
            for ch in s {
                if ch == "0" {
                    zeros += 1
                } else {
                    ones += 1
                }
            }
            
            if zeros > m || ones > n { continue }
            
            for i in stride(from: m, through: zeros, by: -1) {
                for j in stride(from: n, through: ones, by: -1) {
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
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
    fun findMaxForm(strs: Array<String>, m: Int, n: Int): Int {
        val dp = Array(m + 1) { IntArray(n + 1) }
        for (s in strs) {
            var zeros = 0
            var ones = 0
            for (c in s) {
                if (c == '0') zeros++ else ones++
            }
            for (i in m downTo zeros) {
                for (j in n downTo ones) {
                    dp[i][j] = maxOf(dp[i][j], dp[i - zeros][j - ones] + 1)
                }
            }
        }
        return dp[m][n]
    }
}
```

## Dart

```dart
class Solution {
  int findMaxForm(List<String> strs, int m, int n) {
    // DP table where dp[i][j] is the max number of strings that can be formed
    // with i zeros and j ones.
    List<List<int>> dp = List.generate(m + 1, (_) => List.filled(n + 1, 0));

    for (String s in strs) {
      int zeros = 0;
      int ones = 0;
      for (int k = 0; k < s.length; ++k) {
        if (s.codeUnitAt(k) == 48) { // '0'
          zeros++;
        } else {
          ones++;
        }
      }

      // Update DP table in reverse to avoid reuse within the same iteration.
      for (int i = m; i >= zeros; --i) {
        for (int j = n; j >= ones; --j) {
          dp[i][j] = dp[i][j] > dp[i - zeros][j - ones] + 1
              ? dp[i][j]
              : dp[i - zeros][j - ones] + 1;
        }
      }
    }

    return dp[m][n];
  }
}
```

## Golang

```go
func findMaxForm(strs []string, m int, n int) int {
	dp := make([][]int, m+1)
	for i := range dp {
		dp[i] = make([]int, n+1)
	}
	for _, s := range strs {
		zeros, ones := 0, 0
		for _, ch := range s {
			if ch == '0' {
				zeros++
			} else {
				ones++
			}
		}
		for i := m; i >= zeros; i-- {
			for j := n; j >= ones; j-- {
				if dp[i-zeros][j-ones]+1 > dp[i][j] {
					dp[i][j] = dp[i-zeros][j-ones] + 1
				}
			}
		}
	}
	return dp[m][n]
}
```

## Ruby

```ruby
def find_max_form(strs, m, n)
  dp = Array.new(m + 1) { Array.new(n + 1, 0) }
  strs.each do |s|
    zeros = s.count('0')
    ones = s.length - zeros
    m.downto(zeros) do |i|
      n.downto(ones) do |j|
        dp[i][j] = [dp[i][j], dp[i - zeros][j - ones] + 1].max
      end
    end
  end
  dp[m][n]
end
```

## Scala

```scala
object Solution {
    def findMaxForm(strs: Array[String], m: Int, n: Int): Int = {
        val dp = Array.ofDim[Int](m + 1, n + 1)
        for (s <- strs) {
            var zeros = 0
            var ones = 0
            for (c <- s) {
                if (c == '0') zeros += 1 else ones += 1
            }
            var i = m
            while (i >= zeros) {
                var j = n
                while (j >= ones) {
                    dp(i)(j) = math.max(dp(i)(j), dp(i - zeros)(j - ones) + 1)
                    j -= 1
                }
                i -= 1
            }
        }
        dp(m)(n)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_max_form(strs: Vec<String>, m: i32, n: i32) -> i32 {
        let m = m as usize;
        let n = n as usize;
        let mut dp = vec![vec![0i32; n + 1]; m + 1];
        for s in strs.iter() {
            let mut zeros = 0usize;
            let mut ones = 0usize;
            for &b in s.as_bytes() {
                if b == b'0' {
                    zeros += 1;
                } else {
                    ones += 1;
                }
            }
            if zeros > m || ones > n {
                continue;
            }
            for i in (zeros..=m).rev() {
                for j in (ones..=n).rev() {
                    let candidate = dp[i - zeros][j - ones] + 1;
                    if candidate > dp[i][j] {
                        dp[i][j] = candidate;
                    }
                }
            }
        }
        dp[m][n]
    }
}
```

## Racket

```racket
(define/contract (find-max-form strs m n)
  (-> (listof string?) exact-integer? exact-integer? exact-integer?)
  (let ((dp (make-vector (add1 m))))
    ;; initialize dp rows
    (for ([i (in-range (add1 m))])
      (vector-set! dp i (make-vector (add1 n) 0)))
    ;; helper to count zeros and ones in a string
    (define (count-zero-one s)
      (let loop ((idx 0) (z 0) (o 0))
        (if (= idx (string-length s))
            (values z o)
            (let ((ch (string-ref s idx)))
              (if (char=? ch #\0)
                  (loop (+ idx 1) (+ z 1) o)
                  (loop (+ idx 1) z (+ o 1)))))))
    ;; process each string
    (for ([s strs])
      (let-values ([(z o) (count-zero-one s)])
        (for ([i (in-range m -1 -1)])          ; i from m down to 0
          (when (>= i z)
            (let ((row (vector-ref dp i))
                  (prev-row (vector-ref dp (- i z))))
              (for ([j (in-range n -1 -1)])    ; j from n down to 0
                (when (>= j o)
                  (define cand (+ (vector-ref prev-row (- j o)) 1))
                  (define cur (vector-ref row j))
                  (when (> cand cur)
                    (vector-set! row j cand)))))))))
    (vector-ref (vector-ref dp m) n)))
```

## Erlang

```erlang
-export([find_max_form/3]).

-spec find_max_form(Strs :: [unicode:unicode_binary()], M :: integer(), N :: integer()) -> integer().
find_max_form(Strs, M, N) ->
    Counts = [count(S) || S <- Strs],
    InitRow = erlang:make_tuple(N + 1, 0),
    DP0 = list_to_tuple([InitRow || _ <- lists:seq(0, M)]),
    FinalDP = lists:foldl(fun({Z, O}, DPTuple) ->
        update_dp(DPTuple, Z, O, M, N)
    end, DP0, Counts),
    FinalRow = element(M + 1, FinalDP),
    element(N + 1, FinalRow).

%% Count zeros and ones in a binary string
-spec count(unicode:unicode_binary()) -> {integer(), integer()}.
count(Str) ->
    count(Str, 0, 0).

count(<<>>, Z, O) ->
    {Z, O};
count(<<$0, Rest/binary>>, Z, O) ->
    count(Rest, Z + 1, O);
count(<<$1, Rest/binary>>, Z, O) ->
    count(Rest, Z, O + 1).

%% Update DP table with a string having Z zeros and O ones
-spec update_dp(tuple(), integer(), integer(), integer(), integer()) -> tuple().
update_dp(DPTuple, Z, O, M, N) ->
    Rows = [if I >= Z ->
                update_row(I, Z, O, DPTuple, N)
            else
                element(I + 1, DPTuple)
            end || I <- lists:seq(0, M)],
    list_to_tuple(Rows).

%% Update a single row i of DP table
-spec update_row(integer(), integer(), integer(), tuple(), integer()) -> tuple().
update_row(I, Z, O, DPTuple, N) ->
    RowOld = element(I + 1, DPTuple),
    PrevRow = element(I - Z + 1, DPTuple), % I >= Z guaranteed
    NewRow = lists:foldl(fun(J, AccRow) ->
                if J >= O ->
                    ValWithout = element(J + 1, RowOld),
                    ValWithPrev = element(J - O + 1, PrevRow) + 1,
                    MaxVal = erlang:max(ValWithout, ValWithPrev),
                    setelement(J + 1, AccRow, MaxVal)
                ; true ->
                    AccRow
                end
            end, RowOld, lists:seq(0, N)),
    NewRow.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_max_form(strs :: [String.t()], m :: integer, n :: integer) :: integer
  def find_max_form(strs, m, n) do
    counts =
      Enum.map(strs, fn s ->
        {zeros, ones} =
          String.to_charlist(s)
          |> Enum.reduce({0, 0}, fn
            ?0, {z, o} -> {z + 1, o}
            ?1, {z, o} -> {z, o + 1}
          end)

        {zeros, ones}
      end)

    dp =
      for _i <- 0..m do
        for _j <- 0..n, do: 0
      end

    final_dp =
      Enum.reduce(counts, dp, fn {z, o}, acc_dp ->
        if z > m or o > n do
          acc_dp
        else
          i_range = Enum.to_list(z..m) |> Enum.reverse()
          j_range = Enum.to_list(o..n) |> Enum.reverse()

          Enum.reduce(i_range, acc_dp, fn i, dp_i_acc ->
            row = Enum.at(dp_i_acc, i)

            new_row =
              Enum.reduce(j_range, row, fn j, row_acc ->
                cur = Enum.at(row_acc, j)
                prev = Enum.at(Enum.at(dp_i_acc, i - z), j - o) + 1

                if prev > cur do
                  List.replace_at(row_acc, j, prev)
                else
                  row_acc
                end
              end)

            List.replace_at(dp_i_acc, i, new_row)
          end)
        end
      end)

    Enum.at(Enum.at(final_dp, m), n)
  end
end
```
