# 0712. Minimum ASCII Delete Sum for Two Strings

## Cpp

```cpp
class Solution {
public:
    int minimumDeleteSum(string s1, string s2) {
        int n = s1.size(), m = s2.size();
        vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= m; ++j) {
                if (s1[i - 1] == s2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + static_cast<int>(s1[i - 1]);
                } else {
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        int sum = 0;
        for (char c : s1) sum += static_cast<int>(c);
        for (char c : s2) sum += static_cast<int>(c);
        return sum - 2 * dp[n][m];
    }
};
```

## Java

```java
class Solution {
    public int minimumDeleteSum(String s1, String s2) {
        int n = s1.length(), m = s2.length();
        int[][] dp = new int[n + 1][m + 1];
        for (int i = 0; i < n; i++) {
            char c1 = s1.charAt(i);
            for (int j = 0; j < m; j++) {
                if (c1 == s2.charAt(j)) {
                    dp[i + 1][j + 1] = dp[i][j] + c1;
                } else {
                    dp[i + 1][j + 1] = Math.max(dp[i][j + 1], dp[i + 1][j]);
                }
            }
        }
        int total = 0;
        for (int i = 0; i < n; i++) total += s1.charAt(i);
        for (int j = 0; j < m; j++) total += s2.charAt(j);
        return total - 2 * dp[n][m];
    }
}
```

## Python

```python
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        n, m = len(s1), len(s2)
        dp = [0] * (m + 1)
        for i in range(1, n + 1):
            prev_diag = 0
            for j in range(1, m + 1):
                temp = dp[j]
                if s1[i - 1] == s2[j - 1]:
                    dp[j] = prev_diag + ord(s1[i - 1])
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev_diag = temp
        common_sum = dp[m]
        total = sum(map(ord, s1)) + sum(map(ord, s2))
        return total - 2 * common_sum
```

## Python3

```python
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        prev = [0] * (m + 1)
        for i in range(1, n + 1):
            cur = [0] * (m + 1)
            ch_val = ord(s1[i - 1])
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    cur[j] = prev[j - 1] + ch_val
                else:
                    cur[j] = max(prev[j], cur[j - 1])
            prev = cur
        common_sum = prev[m]
        total_sum = sum(map(ord, s1)) + sum(map(ord, s2))
        return total_sum - 2 * common_sum
```

## C

```c
int minimumDeleteSum(char* s1, char* s2) {
    int m = 0, n = 0;
    while (s1[m] != '\0') ++m;
    while (s2[n] != '\0') ++n;

    // Allocate DP table
    int **dp = (int **)malloc((m + 1) * sizeof(int *));
    for (int i = 0; i <= m; ++i) {
        dp[i] = (int *)malloc((n + 1) * sizeof(int));
    }

    // Base case: both strings empty
    dp[m][n] = 0;

    // Fill last row (s1 exhausted)
    for (int j = n - 1; j >= 0; --j) {
        dp[m][j] = dp[m][j + 1] + (int)s2[j];
    }

    // Fill last column (s2 exhausted)
    for (int i = m - 1; i >= 0; --i) {
        dp[i][n] = dp[i + 1][n] + (int)s1[i];
    }

    // Fill the rest
    for (int i = m - 1; i >= 0; --i) {
        for (int j = n - 1; j >= 0; --j) {
            if (s1[i] == s2[j]) {
                dp[i][j] = dp[i + 1][j + 1];
            } else {
                int delS1 = dp[i + 1][j] + (int)s1[i];
                int delS2 = dp[i][j + 1] + (int)s2[j];
                dp[i][j] = delS1 < delS2 ? delS1 : delS2;
            }
        }
    }

    int result = dp[0][0];

    // Free memory
    for (int i = 0; i <= m; ++i) {
        free(dp[i]);
    }
    free(dp);

    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinimumDeleteSum(string s1, string s2)
    {
        int n = s1.Length;
        int m = s2.Length;
        int[,] dp = new int[n + 1, m + 1];

        for (int i = 1; i <= n; i++)
            dp[i, 0] = dp[i - 1, 0] + (int)s1[i - 1];
        for (int j = 1; j <= m; j++)
            dp[0, j] = dp[0, j - 1] + (int)s2[j - 1];

        for (int i = 1; i <= n; i++)
        {
            char c1 = s1[i - 1];
            int ascii1 = (int)c1;
            for (int j = 1; j <= m; j++)
            {
                if (c1 == s2[j - 1])
                    dp[i, j] = dp[i - 1, j - 1];
                else
                {
                    int delFromS1 = dp[i - 1, j] + ascii1;
                    int delFromS2 = dp[i, j - 1] + (int)s2[j - 1];
                    dp[i, j] = delFromS1 < delFromS2 ? delFromS1 : delFromS2;
                }
            }
        }

        return dp[n, m];
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s1
 * @param {string} s2
 * @return {number}
 */
var minimumDeleteSum = function(s1, s2) {
    const n = s1.length;
    const m = s2.length;

    // total ASCII sum of both strings
    let total = 0;
    for (let i = 0; i < n; ++i) total += s1.charCodeAt(i);
    for (let j = 0; j < m; ++j) total += s2.charCodeAt(j);

    // dp[j] = max common ASCII sum for prefixes s1[0..i-1], s2[0..j-1]
    const dp = new Array(m + 1).fill(0);
    for (let i = 1; i <= n; ++i) {
        let prevDiag = 0; // dp[i-1][j-1]
        const chCode = s1.charCodeAt(i - 1);
        for (let j = 1; j <= m; ++j) {
            const temp = dp[j]; // store old dp[i-1][j] before overwrite
            if (chCode === s2.charCodeAt(j - 1)) {
                dp[j] = prevDiag + chCode;
            } else {
                dp[j] = Math.max(dp[j], dp[j - 1]);
            }
            prevDiag = temp; // move diagonal forward
        }
    }

    const commonAscii = dp[m];
    return total - 2 * commonAscii;
};
```

## Typescript

```typescript
function minimumDeleteSum(s1: string, s2: string): number {
    const m = s1.length;
    const n = s2.length;
    const dp: number[][] = new Array(m + 1);
    for (let i = 0; i <= m; i++) {
        dp[i] = new Array(n + 1).fill(0);
    }
    // Base cases when s1 is exhausted
    for (let j = n - 1; j >= 0; --j) {
        dp[m][j] = dp[m][j + 1] + s2.charCodeAt(j);
    }
    // Base cases when s2 is exhausted
    for (let i = m - 1; i >= 0; --i) {
        dp[i][n] = dp[i + 1][n] + s1.charCodeAt(i);
    }
    // Fill DP table
    for (let i = m - 1; i >= 0; --i) {
        const c1 = s1.charCodeAt(i);
        for (let j = n - 1; j >= 0; --j) {
            if (c1 === s2.charCodeAt(j)) {
                dp[i][j] = dp[i + 1][j + 1];
            } else {
                const delFromS1 = c1 + dp[i + 1][j];
                const delFromS2 = s2.charCodeAt(j) + dp[i][j + 1];
                dp[i][j] = delFromS1 < delFromS2 ? delFromS1 : delFromS2;
            }
        }
    }
    return dp[0][0];
}
```

## Php

```php
class Solution {

    /**
     * @param String $s1
     * @param String $s2
     * @return Integer
     */
    function minimumDeleteSum($s1, $s2) {
        $n = strlen($s1);
        $m = strlen($s2);

        // dp for previous row
        $prev = array_fill(0, $m + 1, 0);
        for ($j = 1; $j <= $m; $j++) {
            $prev[$j] = $prev[$j - 1] + ord($s2[$j - 1]);
        }

        for ($i = 1; $i <= $n; $i++) {
            $curr = array_fill(0, $m + 1, 0);
            $curr[0] = $prev[0] + ord($s1[$i - 1]);

            $diag = $prev[0]; // dp[i-1][j-1] for j=1
            for ($j = 1; $j <= $m; $j++) {
                $temp = $prev[$j]; // store dp[i-1][j] before it gets overwritten
                if ($s1[$i - 1] === $s2[$j - 1]) {
                    $curr[$j] = $diag;
                } else {
                    $deleteFromS1 = $prev[$j] + ord($s1[$i - 1]);
                    $deleteFromS2 = $curr[$j - 1] + ord($s2[$j - 1]);
                    $curr[$j] = min($deleteFromS1, $deleteFromS2);
                }
                $diag = $temp; // update diag for next column
            }
            $prev = $curr;
        }

        return $prev[$m];
    }
}
```

## Swift

```swift
class Solution {
    func minimumDeleteSum(_ s1: String, _ s2: String) -> Int {
        let a = Array(s1.utf8)
        let b = Array(s2.utf8)
        let m = a.count
        let n = b.count
        var dp = [Int](repeating: 0, count: n + 1)
        for j in 1...n {
            dp[j] = dp[j - 1] + Int(b[j - 1])
        }
        for i in 1...m {
            var prev = dp[0]
            dp[0] += Int(a[i - 1])
            for j in 1...n {
                let temp = dp[j]
                if a[i - 1] == b[j - 1] {
                    dp[j] = prev
                } else {
                    let deleteA = dp[j] + Int(a[i - 1])
                    let deleteB = dp[j - 1] + Int(b[j - 1])
                    dp[j] = min(deleteA, deleteB)
                }
                prev = temp
            }
        }
        return dp[n]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumDeleteSum(s1: String, s2: String): Int {
        val m = s1.length
        val n = s2.length
        val dp = Array(m + 1) { IntArray(n + 1) }
        for (i in 1..m) {
            val c1 = s1[i - 1]
            val ascii1 = c1.code
            for (j in 1..n) {
                if (c1 == s2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + ascii1
                } else {
                    dp[i][j] = kotlin.math.max(dp[i - 1][j], dp[i][j - 1])
                }
            }
        }
        var total = 0
        for (c in s1) total += c.code
        for (c in s2) total += c.code
        return total - 2 * dp[m][n]
    }
}
```

## Dart

```dart
class Solution {
  int minimumDeleteSum(String s1, String s2) {
    int n = s1.length;
    int m = s2.length;

    // dp for prefixes: prev[j] is answer for first i-1 chars of s1 and first j chars of s2
    List<int> prev = List.filled(m + 1, 0);
    for (int j = 1; j <= m; ++j) {
      prev[j] = prev[j - 1] + s2.codeUnitAt(j - 1);
    }

    for (int i = 1; i <= n; ++i) {
      List<int> cur = List.filled(m + 1, 0);
      cur[0] = prev[0] + s1.codeUnitAt(i - 1);
      int codeS1 = s1.codeUnitAt(i - 1);
      for (int j = 1; j <= m; ++j) {
        if (codeS1 == s2.codeUnitAt(j - 1)) {
          cur[j] = prev[j - 1];
        } else {
          int deleteFromS1 = prev[j] + codeS1;
          int deleteFromS2 = cur[j - 1] + s2.codeUnitAt(j - 1);
          cur[j] = deleteFromS1 < deleteFromS2 ? deleteFromS1 : deleteFromS2;
        }
      }
      prev = cur;
    }

    return prev[m];
  }
}
```

## Golang

```go
func minimumDeleteSum(s1 string, s2 string) int {
	m, n := len(s1), len(s2)
	// dpPrev represents dp[i-1][*], dpCurr represents dp[i][*]
	dpPrev := make([]int, n+1)
	for j := 1; j <= n; j++ {
		dpPrev[j] = dpPrev[j-1] + int(s2[j-1])
	}
	dpCurr := make([]int, n+1)

	for i := 1; i <= m; i++ {
		dpCurr[0] = dpPrev[0] + int(s1[i-1])
		for j := 1; j <= n; j++ {
			if s1[i-1] == s2[j-1] {
				dpCurr[j] = dpPrev[j-1]
			} else {
				costDelS1 := dpPrev[j] + int(s1[i-1])
				costDelS2 := dpCurr[j-1] + int(s2[j-1])
				if costDelS1 < costDelS2 {
					dpCurr[j] = costDelS1
				} else {
					dpCurr[j] = costDelS2
				}
			}
		}
		// swap dpPrev and dpCurr for next iteration
		dpPrev, dpCurr = dpCurr, dpPrev
	}
	return dpPrev[n]
}
```

## Ruby

```ruby
def minimum_delete_sum(s1, s2)
  n1 = s1.length
  n2 = s2.length

  prev = Array.new(n2 + 1, 0)
  (1..n2).each do |j|
    prev[j] = prev[j - 1] + s2.getbyte(j - 1)
  end

  i = 1
  while i <= n1
    cur = Array.new(n2 + 1, 0)
    cur[0] = prev[0] + s1.getbyte(i - 1)

    j = 1
    while j <= n2
      if s1.getbyte(i - 1) == s2.getbyte(j - 1)
        cur[j] = prev[j - 1]
      else
        del_s1 = prev[j] + s1.getbyte(i - 1)
        del_s2 = cur[j - 1] + s2.getbyte(j - 1)
        cur[j] = del_s1 < del_s2 ? del_s1 : del_s2
      end
      j += 1
    end

    prev = cur
    i += 1
  end

  prev[n2]
end
```

## Scala

```scala
object Solution {
    def minimumDeleteSum(s1: String, s2: String): Int = {
        val n = s1.length
        val m = s2.length
        // dp[i][j] stores max ASCII sum of common subsequence for prefixes of length i and j
        val dp = Array.ofDim[Int](n + 1, m + 1)

        var i = 1
        while (i <= n) {
            val c1 = s1.charAt(i - 1).toInt
            var j = 1
            while (j <= m) {
                if (c1 == s2.charAt(j - 1).toInt) {
                    dp(i)(j) = dp(i - 1)(j - 1) + c1
                } else {
                    val a = dp(i - 1)(j)
                    val b = dp(i)(j - 1)
                    dp(i)(j) = if (a > b) a else b
                }
                j += 1
            }
            i += 1
        }

        var total = 0
        var idx = 0
        while (idx < n) {
            total += s1.charAt(idx).toInt
            idx += 1
        }
        idx = 0
        while (idx < m) {
            total += s2.charAt(idx).toInt
            idx += 1
        }

        total - 2 * dp(n)(m)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_delete_sum(s1: String, s2: String) -> i32 {
        let b1 = s1.as_bytes();
        let b2 = s2.as_bytes();
        let n = b1.len();
        let m = b2.len();

        let mut dp = vec![vec![0i32; m + 1]; n + 1];

        for i in 1..=n {
            dp[i][0] = dp[i - 1][0] + b1[i - 1] as i32;
        }
        for j in 1..=m {
            dp[0][j] = dp[0][j - 1] + b2[j - 1] as i32;
        }

        for i in 1..=n {
            for j in 1..=m {
                if b1[i - 1] == b2[j - 1] {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    let del_s1 = dp[i - 1][j] + b1[i - 1] as i32;
                    let del_s2 = dp[i][j - 1] + b2[j - 1] as i32;
                    dp[i][j] = del_s1.min(del_s2);
                }
            }
        }

        dp[n][m]
    }
}
```

## Racket

```racket
(define/contract (minimum-delete-sum s1 s2)
  (-> string? string? exact-integer?)
  (let* ([n (string-length s1)]
         [m (string-length s2)]
         [prev (make-vector (+ m 1) 0)])
    ;; initialize for empty s1
    (for ([j (in-range 1 (+ m 1))])
      (vector-set! prev j
                   (+ (vector-ref prev (- j 1))
                      (char->integer (string-ref s2 (- j 1))))))
    (let loop-i ([i 1] [prev prev])
      (if (> i n)
          (vector-ref prev m)
          (let ([cur (make-vector (+ m 1) 0)])
            ;; delete s1[i-1] to match empty prefix of s2
            (vector-set! cur 0
                         (+ (vector-ref prev 0)
                            (char->integer (string-ref s1 (- i 1)))))
            (for ([j (in-range 1 (+ m 1))])
              (let* ([c1 (string-ref s1 (- i 1))]
                     [c2 (string-ref s2 (- j 1))]
                     [del-from-s1 (+ (vector-ref prev j)
                                     (char->integer c1))]
                     [del-from-s2 (+ (vector-ref cur (- j 1))
                                     (char->integer c2))])
                (if (char=? c1 c2)
                    (vector-set! cur j (vector-ref prev (- j 1)))
                    (vector-set! cur j (min del-from-s1 del-from-s2)))))
            (loop-i (+ i 1) cur))))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_delete_sum/2]).

-spec minimum_delete_sum(S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary()) -> integer().
minimum_delete_sum(S1, S2) ->
    A = binary_to_list(S1),
    B = binary_to_list(S2),
    DP0 = dp_prev_init(B),
    FinalDP = process_rows(A, B, DP0),
    lists:last(FinalDP).

dp_prev_init(B) -> dp_prev_init(B, 0, [0]).
dp_prev_init([], _Acc, List) ->
    lists:reverse(List);
dp_prev_init([C|Rest], Acc, List) ->
    NewAcc = Acc + C,
    dp_prev_init(Rest, NewAcc, [NewAcc | List]).

process_rows([], _B, DPPrev) -> DPPrev;
process_rows([AChar|ARest], B, DPPrev) ->
    Curr = compute_curr_row(AChar, B, DPPrev),
    process_rows(ARest, B, Curr).

compute_curr_row(AChar, BList, DPPrev) ->
    [Prev0|RestPrev] = DPPrev,
    Curr0 = Prev0 + AChar,
    RestCurr = row_loop(BList, RestPrev, Curr0, Prev0, AChar),
    [Curr0 | RestCurr].

row_loop([], [], _CurrPrev, _PrevDiag, _AChar) ->
    [];
row_loop([BChar|BRest], [DPPrevJ|DPPrevRest], CurrPrev, PrevDiag, AChar) ->
    Curr =
        if
            AChar =:= BChar -> PrevDiag;
            true ->
                DelA = DPPrevJ + AChar,
                DelB = CurrPrev + BChar,
                erlang:min(DelA, DelB)
        end,
    Rest = row_loop(BRest, DPPrevRest, Curr, DPPrevJ, AChar),
    [Curr | Rest].
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_delete_sum(s1 :: String.t(), s2 :: String.t()) :: integer()
  def minimum_delete_sum(s1, s2) do
    a = :binary.bin_to_list(s1)
    b = :binary.bin_to_list(s2)

    total = Enum.sum(a) + Enum.sum(b)
    m = length(b)

    prev_row = :array.new(m + 1, default: 0)

    final_row =
      Enum.reduce(a, prev_row, fn ca, prev ->
        cur = :array.new(m + 1, default: 0)

        cur_filled =
          Enum.reduce(1..m, cur, fn j, acc ->
            cb = Enum.at(b, j - 1)

            if ca == cb do
              val = :array.get(j - 1, prev) + ca
              :array.set(j, val, acc)
            else
              left = :array.get(j - 1, acc)
              up = :array.get(j, prev)
              val = if left > up, do: left, else: up
              :array.set(j, val, acc)
            end
          end)

        cur_filled
      end)

    lcs_sum = :array.get(m, final_row)
    total - 2 * lcs_sum
  end
end
```
