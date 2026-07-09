# 0903. Valid Permutations for DI Sequence

## Cpp

```cpp
class Solution {
public:
    int numPermsDISequence(string s) {
        const int MOD = 1000000007;
        int n = s.size();
        vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0));
        dp[0][0] = 1;
        for (int i = 1; i <= n; ++i) {
            // prefix sums of dp[i-1][*]
            vector<long long> pref(i, 0);
            pref[0] = dp[i - 1][0];
            for (int k = 1; k < i; ++k) {
                pref[k] = (pref[k - 1] + dp[i - 1][k]) % MOD;
            }
            if (s[i - 1] == 'I') {
                for (int j = 0; j <= i; ++j) {
                    if (j == 0) dp[i][j] = 0;
                    else dp[i][j] = pref[j - 1] % MOD;
                }
            } else { // 'D'
                long long total = pref[i - 1];
                for (int j = 0; j <= i; ++j) {
                    long long left = (j == 0) ? 0 : pref[j - 1];
                    dp[i][j] = (total - left + MOD) % MOD;
                }
            }
        }
        long long ans = 0;
        for (int j = 0; j <= n; ++j) {
            ans += dp[n][j];
            if (ans >= MOD) ans -= MOD;
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int numPermsDISequence(String s) {
        final int MOD = 1_000_000_007;
        int n = s.length();
        int[][] dp = new int[n + 1][n + 1];
        dp[0][0] = 1;
        for (int i = 1; i <= n; i++) {
            long[] pref = new long[i];
            pref[0] = dp[i - 1][0];
            for (int k = 1; k < i; k++) {
                pref[k] = (pref[k - 1] + dp[i - 1][k]) % MOD;
            }
            char c = s.charAt(i - 1);
            if (c == 'I') {
                for (int j = 0; j <= i; j++) {
                    if (j == 0) {
                        dp[i][j] = 0;
                    } else {
                        dp[i][j] = (int) pref[j - 1];
                    }
                }
            } else { // 'D'
                long total = pref[i - 1];
                for (int j = 0; j <= i; j++) {
                    long left = (j > 0) ? pref[j - 1] : 0;
                    dp[i][j] = (int) ((total - left + MOD) % MOD);
                }
            }
        }
        int ans = 0;
        for (int v : dp[n]) {
            ans += v;
            if (ans >= MOD) ans -= MOD;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def numPermsDISequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            prev = dp[i - 1]
            # prefix sums of prev[0..i-1]
            pref = [0] * i
            cur = 0
            for k in range(i):
                cur = (cur + prev[k]) % MOD
                pref[k] = cur
            total = pref[-1] if i > 0 else 0

            if s[i - 1] == 'I':
                for j in range(i + 1):
                    dp[i][j] = pref[j - 1] if j > 0 else 0
            else:  # 'D'
                for j in range(i + 1):
                    if j == 0:
                        dp[i][j] = total
                    else:
                        dp[i][j] = (total - pref[j - 1]) % MOD

        return sum(dp[n]) % MOD
```

## Python3

```python
class Solution:
    def numPermsDISequence(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = [1]  # ways for empty prefix
        for ch in s:
            m = len(dp)
            ndp = [0] * (m + 1)
            if ch == 'I':
                pref = 0
                for j in range(m + 1):
                    ndp[j] = pref
                    if j < m:
                        pref = (pref + dp[j]) % MOD
            else:  # 'D'
                suff = 0
                for j in range(m, -1, -1):
                    ndp[j] = suff
                    if j > 0:
                        suff = (suff + dp[j - 1]) % MOD
            dp = ndp
        return sum(dp) % MOD
```

## C

```c
#include <string.h>

int numPermsDISequence(char* s) {
    const int MOD = 1000000007;
    int n = (int)strlen(s);
    static long long dp[201][201];
    memset(dp, 0, sizeof(dp));
    dp[0][0] = 1;

    for (int i = 1; i <= n; ++i) {
        if (s[i - 1] == 'I') {
            long long prefix = 0;
            for (int j = 0; j <= i; ++j) {
                dp[i][j] = prefix % MOD;
                prefix = (prefix + dp[i - 1][j]) % MOD;
            }
        } else { // 'D'
            long long suffix = 0;
            for (int j = i - 1; j >= 0; --j) {
                suffix = (suffix + dp[i - 1][j]) % MOD;
                dp[i][j] = suffix;
            }
            dp[i][i] = 0;
        }
    }

    long long ans = 0;
    for (int j = 0; j <= n; ++j) {
        ans = (ans + dp[n][j]) % MOD;
    }
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int NumPermsDISequence(string s) {
        const int MOD = 1000000007;
        int n = s.Length;
        long[] dpPrev = new long[n + 1];
        dpPrev[0] = 1;

        for (int i = 1; i <= n; i++) {
            long[] dpCurr = new long[i + 1];
            if (s[i - 1] == 'I') {
                long sum = 0;
                for (int j = 0; j <= i; j++) {
                    dpCurr[j] = sum;
                    if (j < i) {
                        sum += dpPrev[j];
                        if (sum >= MOD) sum -= MOD;
                    }
                }
            } else { // 'D'
                long sum = 0;
                for (int j = i - 1; j >= 0; j--) {
                    sum += dpPrev[j];
                    if (sum >= MOD) sum -= MOD;
                    dpCurr[j] = sum;
                }
                // dpCurr[i] stays 0
            }
            dpPrev = dpCurr;
        }

        long ans = 0;
        foreach (var v in dpPrev) {
            ans += v;
            if (ans >= MOD) ans -= MOD;
        }
        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var numPermsDISequence = function(s) {
    const MOD = 1000000007;
    const n = s.length;
    // dp[i][j]: ways for first i+1 numbers, last number is j-th smallest among them
    const dp = Array.from({ length: n + 1 }, () => new Array(n + 1).fill(0));
    dp[0][0] = 1;
    for (let i = 0; i < n; i++) {
        // prefix sums of dp[i][*]
        const pref = new Array(i + 2).fill(0);
        let sum = 0;
        for (let j = 0; j <= i; j++) {
            sum = (sum + dp[i][j]) % MOD;
            pref[j] = sum;
        }
        pref[i + 1] = sum; // total sum up to i
        if (s[i] === 'I') {
            for (let k = 0; k <= i + 1; k++) {
                dp[i + 1][k] = k === 0 ? 0 : pref[k - 1];
            }
        } else { // 'D'
            const total = pref[i];
            for (let k = 0; k <= i + 1; k++) {
                const left = k === 0 ? 0 : pref[k - 1];
                dp[i + 1][k] = (total - left + MOD) % MOD;
            }
        }
    }
    let ans = 0;
    for (let j = 0; j <= n; j++) {
        ans = (ans + dp[n][j]) % MOD;
    }
    return ans;
};
```

## Typescript

```typescript
function numPermsDISequence(s: string): number {
    const MOD = 1_000_000_007;
    const n = s.length;
    const dp: number[][] = Array.from({ length: n + 1 }, () => new Array(n + 1).fill(0));
    dp[0][0] = 1;

    for (let i = 1; i <= n; i++) {
        // prefix sums of dp[i-1]
        const pref: number[] = new Array(i).fill(0);
        pref[0] = dp[i - 1][0];
        for (let j = 1; j < i; j++) {
            pref[j] = (pref[j - 1] + dp[i - 1][j]) % MOD;
        }

        if (s.charAt(i - 1) === 'I') {
            // need previous rank < current rank
            for (let j = 0; j <= i; j++) {
                dp[i][j] = j === 0 ? 0 : pref[j - 1];
            }
        } else { // 'D'
            const total = pref[i - 1]; // sum of all dp[i-1][*]
            for (let j = 0; j <= i; j++) {
                const sub = j === 0 ? 0 : pref[j - 1];
                dp[i][j] = (total - sub + MOD) % MOD;
            }
        }
    }

    let ans = 0;
    for (let j = 0; j <= n; j++) {
        ans = (ans + dp[n][j]) % MOD;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function numPermsDISequence($s) {
        $mod = 1000000007;
        $n = strlen($s);
        // dp[i][j]: ways for first i characters, ending with rank j (0-indexed)
        $dp = array_fill(0, $n + 1, array_fill(0, $n + 1, 0));
        $dp[0][0] = 1;

        for ($i = 1; $i <= $n; $i++) {
            if ($s[$i - 1] === 'I') {
                $prefix = 0;
                // j ranges from 0 to i
                for ($j = 0; $j <= $i; $j++) {
                    $dp[$i][$j] = $prefix;
                    if ($j < $i) {
                        $prefix += $dp[$i - 1][$j];
                        if ($prefix >= $mod) $prefix -= $mod;
                    }
                }
            } else { // 'D'
                $suffix = 0;
                for ($j = $i; $j >= 0; $j--) {
                    if ($j < $i) {
                        $suffix += $dp[$i - 1][$j];
                        if ($suffix >= $mod) $suffix -= $mod;
                    }
                    $dp[$i][$j] = $suffix;
                }
            }
        }

        $ans = 0;
        for ($j = 0; $j <= $n; $j++) {
            $ans += $dp[$n][$j];
            if ($ans >= $mod) $ans -= $mod;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func numPermsDISequence(_ s: String) -> Int {
        let MOD = 1_000_000_007
        var dp = [Int](repeating: 0, count: 1)
        dp[0] = 1
        for ch in s {
            let m = dp.count
            var newdp = [Int](repeating: 0, count: m + 1)
            if ch == "I" {
                var prefix = 0
                for j in 0..<(m + 1) {
                    newdp[j] = prefix
                    if j < m {
                        prefix += dp[j]
                        if prefix >= MOD { prefix -= MOD }
                    }
                }
            } else { // 'D'
                var suffix = 0
                for j in stride(from: m, through: 0, by: -1) {
                    newdp[j] = suffix
                    if j > 0 {
                        suffix += dp[j - 1]
                        if suffix >= MOD { suffix -= MOD }
                    }
                }
            }
            dp = newdp
        }
        var ans = 0
        for v in dp {
            ans += v
            if ans >= MOD { ans -= MOD }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numPermsDISequence(s: String): Int {
        val MOD = 1_000_000_007L
        val n = s.length
        val dp = Array(n + 1) { LongArray(it + 1) }
        dp[0][0] = 1L
        for (i in 1..n) {
            val ch = s[i - 1]
            if (ch == 'I') {
                var prefix = 0L
                for (j in 0..i) {
                    dp[i][j] = prefix
                    if (j < i) {
                        prefix += dp[i - 1][j]
                        if (prefix >= MOD) prefix -= MOD
                    }
                }
            } else { // 'D'
                var suffix = 0L
                for (j in i downTo 0) {
                    if (j < i) {
                        suffix += dp[i - 1][j]
                        if (suffix >= MOD) suffix -= MOD
                    }
                    dp[i][j] = suffix
                }
            }
        }
        var ans = 0L
        for (v in dp[n]) {
            ans += v
            if (ans >= MOD) ans -= MOD
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int numPermsDISequence(String s) {
    int n = s.length;
    List<List<int>> dp = List.generate(n + 1, (_) => List.filled(n + 1, 0));
    dp[0][0] = 1;

    for (int i = 1; i <= n; ++i) {
      if (s[i - 1] == 'I') {
        int sum = 0;
        for (int j = 0; j <= i; ++j) {
          dp[i][j] = sum;
          if (j < i) {
            sum += dp[i - 1][j];
            if (sum >= _mod) sum -= _mod;
          }
        }
      } else { // 'D'
        int sum = 0;
        for (int j = i - 1; j >= 0; --j) {
          sum += dp[i - 1][j];
          if (sum >= _mod) sum -= _mod;
          dp[i][j] = sum;
        }
        dp[i][i] = 0;
      }
    }

    int ans = 0;
    for (int j = 0; j <= n; ++j) {
      ans += dp[n][j];
      if (ans >= _mod) ans -= _mod;
    }
    return ans;
  }
}
```

## Golang

```go
func numPermsDISequence(s string) int {
	const mod = 1000000007
	n := len(s)
	dp := make([][]int, n+1)
	for i := 0; i <= n; i++ {
		dp[i] = make([]int, i+1)
	}
	dp[0][0] = 1

	for i := 1; i <= n; i++ {
		if s[i-1] == 'I' {
			prefix := 0
			for j := 0; j <= i; j++ {
				if j > 0 {
					prefix += dp[i-1][j-1]
					if prefix >= mod {
						prefix -= mod
					}
				}
				dp[i][j] = prefix
			}
		} else { // 'D'
			suffix := 0
			for j := i - 1; j >= 0; j-- {
				suffix += dp[i-1][j]
				if suffix >= mod {
					suffix -= mod
				}
				dp[i][j] = suffix
			}
			// dp[i][i] stays 0
		}
	}

	ans := 0
	for _, v := range dp[n] {
		ans += v
		if ans >= mod {
			ans -= mod
		}
	}
	return ans
}
```

## Ruby

```ruby
def num_perms_di_sequence(s)
  mod = 1_000_000_007
  n = s.length
  dp = Array.new(n + 1) { Array.new(n + 1, 0) }
  dp[0][0] = 1

  (1..n).each do |i|
    # prefix sums of previous row
    prefix = Array.new(i, 0)
    sum = 0
    (0...i).each do |j|
      sum += dp[i - 1][j]
      sum -= mod if sum >= mod
      prefix[j] = sum
    end

    if s[i - 1] == 'I'
      (0..i).each do |j|
        dp[i][j] = j.zero? ? 0 : prefix[j - 1]
      end
    else # 'D'
      total = prefix[i - 1]
      (0..i).each do |j|
        if j.zero?
          dp[i][j] = total
        else
          val = total - prefix[j - 1]
          val += mod if val < 0
          dp[i][j] = val
        end
      end
    end
  end

  ans = 0
  (0..n).each { |j| ans = (ans + dp[n][j]) % mod }
  ans
end
```

## Scala

```scala
object Solution {
    def numPermsDISequence(s: String): Int = {
        val MOD = 1000000007L
        val n = s.length
        val dp = Array.ofDim[Int](n + 1, n + 1)
        dp(0)(0) = 1
        for (i <- 1 to n) {
            // prefix sums of dp[i-1][*]
            val pre = new Array[Long](i)
            var sum: Long = 0L
            for (j <- 0 until i) {
                sum += dp(i - 1)(j)
                if (sum >= MOD) sum -= MOD
                pre(j) = sum
            }
            if (s.charAt(i - 1) == 'I') {
                for (j <- 0 to i) {
                    val v = if (j == 0) 0L else pre(j - 1)
                    dp(i)(j) = v.toInt
                }
            } else { // 'D'
                val total = pre(i - 1)
                for (j <- 0 to i) {
                    val left = if (j == 0) 0L else pre(j - 1)
                    var v = total - left
                    if (v < 0) v += MOD
                    dp(i)(j) = v.toInt
                }
            }
        }
        var ans: Long = 0L
        for (j <- 0 to n) {
            ans += dp(n)(j)
            if (ans >= MOD) ans -= MOD
        }
        ans.toInt
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn num_perms_di_sequence(s: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = s.len();
        let bytes = s.as_bytes();
        let mut dp = vec![vec![0i64; n + 1]; n + 1];
        dp[0][0] = 1;
        for i in 1..=n {
            // prefix sums of dp[i-1]
            let mut pre = vec![0i64; i + 1];
            for k in 0..i {
                pre[k + 1] = (pre[k] + dp[i - 1][k]) % MOD;
            }
            let total = pre[i];
            if bytes[i - 1] == b'I' {
                for j in 0..=i {
                    dp[i][j] = pre[j]; // sum of k < j
                }
            } else {
                for j in 0..=i {
                    let mut val = total - pre[j];
                    if val < 0 {
                        val += MOD;
                    }
                    dp[i][j] = val % MOD; // sum of k >= j
                }
            }
        }
        let mut ans = 0i64;
        for j in 0..=n {
            ans = (ans + dp[n][j]) % MOD;
        }
        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (num-perms-di-sequence s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (dp (make-vector (+ n 1) #f)))
    ;; allocate rows
    (for ([i (in-range (+ n 1))])
      (vector-set! dp i (make-vector (+ n 1) 0)))
    ;; base case
    (vector-set! (vector-ref dp 0) 0 1)
    ;; DP transitions
    (for ([i (in-range 1 (+ n 1))])
      (let* ((prev (vector-ref dp (- i 1)))
             (curr (vector-ref dp i))
             (pref (make-vector (+ i 1) 0))) ; pref[0]=0
        ;; build prefix sums of prev
        (for ([j (in-range i)])
          (let ((val (vector-ref prev j)))
            (vector-set! pref (+ j 1)
                         (modulo (+ (vector-ref pref j) val) MOD))))
        (let ((total (vector-ref pref i))) ; sum of all prev[0..i-1]
          (for ([j (in-range (+ i 1))])
            (let ((c (string-ref s (- i 1)))) ; current pattern char
              (cond [(char=? c #\I)
                     ;; sum_{k<j} prev[k] = pref[j]
                     (vector-set! curr j (modulo (vector-ref pref j) MOD))]
                    [else ; 'D'
                     ;; sum_{k>=j} prev[k] = total - pref[j]
                     (let ((val (- total (vector-ref pref j))))
                       (when (< val 0) (set! val (+ val MOD)))
                       (vector-set! curr j (modulo val MOD)))]))))))
    ;; accumulate answer from last row
    (let ((last (vector-ref dp n))
          (ans 0))
      (for ([j (in-range (+ n 1))])
        (set! ans (modulo (+ ans (vector-ref last j)) MOD)))
      ans)))
```

## Erlang

```erlang
-module(solution).
-export([num_perms_di_sequence/1]).

-define(MOD, 1000000007).

-spec num_perms_di_sequence(S :: unicode:unicode_binary()) -> integer().
num_perms_di_sequence(S) ->
    Chars = binary_to_list(S),
    FinalDP = process(Chars, [1]),
    lists:foldl(fun(X, Acc) -> (Acc + X) rem ?MOD end, 0, FinalDP).

process([], DP) -> DP;
process([C | Rest], Prev) ->
    NewDP = case C of
        $I -> compute_I(Prev);
        $D -> compute_D(Prev)
    end,
    process(Rest, NewDP).

compute_I(Prev) ->
    go_I(Prev, 0, []).

go_I([], Cum, Acc) ->
    lists:reverse([Cum | Acc]);
go_I([H | T], Cum, Acc) ->
    NewAcc = [Cum | Acc],
    NewCum = (Cum + H) rem ?MOD,
    go_I(T, NewCum, NewAcc).

compute_D(Prev) ->
    Total = lists:foldl(fun(X, Acc) -> (Acc + X) rem ?MOD end, 0, Prev),
    go_D(Prev, Total, []).

go_D([], Cum, Acc) ->
    lists:reverse([Cum | Acc]);
go_D([H | T], Cum, Acc) ->
    NewAcc = [Cum | Acc],
    NewCum = ((Cum - H) rem ?MOD + ?MOD) rem ?MOD,
    go_D(T, NewCum, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @spec num_perms_di_sequence(s :: String.t()) :: integer()
  def num_perms_di_sequence(s) do
    mod = 1_000_000_007

    dp_final =
      String.graphemes(s)
      |> Enum.reduce([1], fn ch, dp_prev ->
        m = length(dp_prev) - 1
        new_len = m + 2

        for j <- 0..(new_len - 1) do
          sum =
            if ch == "I" do
              0..(j - 1)
              |> Enum.reduce(0, fn k, acc ->
                (acc + Enum.at(dp_prev, k)) rem mod
              end)
            else
              j..m
              |> Enum.reduce(0, fn k, acc ->
                (acc + Enum.at(dp_prev, k)) rem mod
              end)
            end

          sum
        end
      end)

    Enum.reduce(dp_final, 0, fn v, acc -> (acc + v) rem mod end)
  end
end
```
