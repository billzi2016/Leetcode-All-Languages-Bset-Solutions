# 1621. Number of Sets of K Non-Overlapping Line Segments

## Cpp

```cpp
class Solution {
public:
    int numberOfSets(int n, int k) {
        const int MOD = 1000000007;
        vector<vector<int>> dp(n, vector<int>(k + 1, 0));
        vector<vector<int>> pref(n, vector<int>(k + 1, 0));
        
        for (int i = 0; i < n; ++i) {
            dp[i][0] = 1;
        }
        for (int i = 0; i < n; ++i) {
            for (int j = 1; j <= k; ++j) {
                long long val = 0;
                if (i > 0) {
                    val += dp[i - 1][j];          // not using point i as right endpoint
                    val += pref[i - 1][j - 1];    // start a new segment ending at i
                }
                dp[i][j] = int(val % MOD);
            }
            for (int j = 0; j <= k; ++j) {
                long long sum = dp[i][j];
                if (i > 0) sum += pref[i - 1][j];
                pref[i][j] = int(sum % MOD);
            }
        }
        return dp[n - 1][k];
    }
};
```

## Java

```java
class Solution {
    private static final long MOD = 1_000_000_007L;

    public int numberOfSets(int n, int k) {
        int max = n + k; // sufficient for factorials
        long[] fact = new long[max + 1];
        long[] invFact = new long[max + 1];
        fact[0] = 1;
        for (int i = 1; i <= max; i++) {
            fact[i] = fact[i - 1] * i % MOD;
        }
        invFact[max] = modPow(fact[max], MOD - 2);
        for (int i = max; i >= 1; i--) {
            invFact[i - 1] = invFact[i] * i % MOD;
        }

        int N = n + k - 1;
        int R = 2 * k;
        if (R > N) return 0;

        long ans = fact[N];
        ans = ans * invFact[R] % MOD;
        ans = ans * invFact[N - R] % MOD;
        return (int) ans;
    }

    private long modPow(long base, long exp) {
        long result = 1;
        long b = base % MOD;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                result = result * b % MOD;
            }
            b = b * b % MOD;
            exp >>= 1;
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        pre = [[0] * (k + 1) for _ in range(n + 1)]

        # base case: zero segments
        for i in range(n + 1):
            dp[i][0] = 1
            pre[i][0] = (pre[i - 1][0] + 1) % MOD if i > 0 else 1

        for i in range(1, n + 1):
            max_j = min(k, i)  # cannot have more segments than points considered
            for j in range(1, max_j + 1):
                add = 0
                if i >= 2:
                    add = pre[i - 1][j - 1]
                    if j == 1:  # exclude the empty prefix counted when j-1 == 0
                        add = (add - 1) % MOD
                dp[i][j] = (dp[i - 1][j] + add) % MOD
            for j in range(k + 1):
                pre[i][j] = (pre[i - 1][j] + dp[i][j]) % MOD

        return dp[n][k]
```

## Python3

```python
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (k + 1) for _ in range(n)]
        pref = [[0] * (k + 1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = 1
            maxj = min(k, i)
            for j in range(1, maxj + 1):
                val = dp[i - 1][j] if i > 0 else 0
                add = pref[i - 1][j - 1] if i > 0 else 0
                dp[i][j] = (val + add) % MOD

            for j in range(k + 1):
                if i == 0:
                    pref[i][j] = dp[i][j]
                else:
                    pref[i][j] = (pref[i - 1][j] + dp[i][j]) % MOD

        return dp[n - 1][k]
```

## C

```c
int numberOfSets(int n, int k) {
    const int MOD = 1000000007;
    static int dp[1002][1002];
    static int pref[1002][1002];

    dp[0][0] = 1;
    pref[0][0] = 1;

    for (int i = 1; i <= n; ++i) {
        dp[i][0] = 1;
        pref[i][0] = 1;
    }

    for (int j = 1; j <= k; ++j) {
        // pref[0][j] stays 0
        for (int i = 1; i <= n; ++i) {
            long long val = dp[i - 1][j];
            if (i >= 2) {
                val += pref[i - 2][j - 1];
            }
            if (val >= MOD) val %= MOD;
            dp[i][j] = (int)(val % MOD);

            int sum = pref[i - 1][j] + dp[i][j];
            if (sum >= MOD) sum -= MOD;
            pref[i][j] = sum;
        }
    }

    return dp[n][k];
}
```

## Csharp

```csharp
public class Solution
{
    private const long MOD = 1000000007L;

    public int NumberOfSets(int n, int k)
    {
        // The answer is C(n + k - 1, 2k) mod MOD
        int N = n + k - 1;
        int R = 2 * k;
        if (R > N) return 0;

        int max = N; // factorial up to N is enough
        long[] fact = new long[max + 1];
        long[] invFact = new long[max + 1];

        fact[0] = 1;
        for (int i = 1; i <= max; i++)
            fact[i] = fact[i - 1] * i % MOD;

        invFact[max] = ModPow(fact[max], MOD - 2);
        for (int i = max; i >= 1; i--)
            invFact[i - 1] = invFact[i] * i % MOD;

        long ans = fact[N];
        ans = ans * invFact[R] % MOD;
        ans = ans * invFact[N - R] % MOD;

        return (int)ans;
    }

    private static long ModPow(long baseVal, long exp)
    {
        long result = 1;
        long b = baseVal % MOD;
        while (exp > 0)
        {
            if ((exp & 1) == 1)
                result = result * b % MOD;
            b = b * b % MOD;
            exp >>= 1;
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var numberOfSets = function(n, k) {
    const MOD = 1000000007;
    // dp[i][j]: ways using first i points (0..i-1) with exactly j segments
    const dp = Array.from({ length: n + 1 }, () => new Array(k + 1).fill(0));
    const pre = Array.from({ length: n + 1 }, () => new Array(k + 1).fill(0));

    // base case: zero segments -> exactly one way (choose nothing)
    for (let i = 0; i <= n; ++i) {
        dp[i][0] = 1;
        pre[i][0] = (i === 0 ? 1 : (pre[i - 1][0] + 1) % MOD);
    }

    // fill DP
    for (let i = 1; i <= n; ++i) {
        for (let j = 1; j <= k; ++j) {
            let val = dp[i - 1][j]; // do not end a segment at point i-1
            if (i >= 2) {
                val += pre[i - 2][j - 1];
                if (val >= MOD) val -= MOD;
            }
            dp[i][j] = val % MOD;
        }
        // update prefix sums for this i
        for (let j = 0; j <= k; ++j) {
            let sum = pre[i - 1][j] + dp[i][j];
            if (sum >= MOD) sum -= MOD;
            pre[i][j] = sum;
        }
    }

    return dp[n][k] % MOD;
};
```

## Typescript

```typescript
function numberOfSets(n: number, k: number): number {
    const MOD = 1_000_000_007;
    let dp = new Array(k + 1).fill(0);
    let open = new Array(k + 1).fill(0);
    dp[0] = 1;

    for (let i = 0; i < n; ++i) {
        const ndp = new Array(k + 1).fill(0);
        const nopen = new Array(k + 1).fill(0);
        for (let j = 0; j <= k; ++j) {
            const curDP = dp[j];
            if (curDP !== 0) {
                ndp[j] = (ndp[j] + curDP) % MOD;          // skip point i
                nopen[j] = (nopen[j] + curDP) % MOD;      // start new segment at i
            }
            const curOpen = open[j];
            if (curOpen !== 0) {
                nopen[j] = (nopen[j] + curOpen) % MOD;    // extend current open segment
                if (j + 1 <= k) {
                    ndp[j + 1] = (ndp[j + 1] + curOpen) % MOD; // close segment at i
                }
            }
        }
        dp = ndp;
        open = nopen;
    }

    return dp[k];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer
     */
    function numberOfSets($n, $k) {
        $mod = 1000000007;
        // dp[i][j]: ways using points 0..i with j segments, point i not open
        $dp = array_fill(0, $n, array_fill(0, $k + 1, 0));
        for ($i = 0; $i < $n; $i++) {
            $dp[$i][0] = 1;
        }

        // pref[i][j]: sum_{t=0..i} dp[t][j]
        $pref = array_fill(0, $n, array_fill(0, $k + 1, 0));
        for ($j = 0; $j <= $k; $j++) {
            $pref[0][$j] = $dp[0][$j];
        }

        for ($i = 1; $i < $n; $i++) {
            // compute dp[i][j] for j >= 1
            for ($j = 1; $j <= $k; $j++) {
                $add = $pref[$i - 1][$j - 1]; // sum_{p=0}^{i-1} dp[p][j-1]
                $dp[$i][$j] = ($dp[$i - 1][$j] + $add) % $mod;
            }
            // update prefix sums for this i
            for ($j = 0; $j <= $k; $j++) {
                $pref[$i][$j] = ($pref[$i - 1][$j] + $dp[$i][$j]) % $mod;
            }
        }

        return $dp[$n - 1][$k];
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    private let MOD = 1_000_000_007
    
    func numberOfSets(_ n: Int, _ k: Int) -> Int {
        if k == 0 { return 1 }
        var dp = Array(repeating: Array(repeating: 0, count: k + 1), count: n + 1)
        var pref = Array(repeating: Array(repeating: 0, count: k + 1), count: n + 1)
        
        dp[0][0] = 1
        pref[0][0] = 1
        
        if n >= 1 {
            for i in 1...n {
                dp[i][0] = 1
                let maxJ = min(k, i / 2)
                if maxJ >= 1 {
                    for j in 1...maxJ {
                        var val = dp[i - 1][j] + pref[i - 1][j - 1]
                        if val >= MOD { val -= MOD }
                        dp[i][j] = val
                    }
                }
                // update prefix sums
                for j in 0...k {
                    var sum = pref[i - 1][j] + dp[i][j]
                    if sum >= MOD { sum -= MOD }
                    pref[i][j] = sum
                }
            }
        }
        
        return dp[n][k]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfSets(n: Int, k: Int): Int {
        val MOD = 1_000_000_007L
        val dp = Array(n) { LongArray(k + 1) }
        val pref = Array(n) { LongArray(k + 1) }

        // base for i = 0
        dp[0][0] = 1L
        pref[0][0] = 1L

        for (i in 1 until n) {
            for (j in 0..k) {
                if (j == 0) {
                    dp[i][j] = 1L   // only one way to have zero segments
                } else {
                    val add = pref[i - 1][j - 1]
                    dp[i][j] = (dp[i - 1][j] + add) % MOD
                }
            }
            for (j in 0..k) {
                pref[i][j] = (pref[i - 1][j] + dp[i][j]) % MOD
            }
        }
        return dp[n - 1][k].toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int numberOfSets(int n, int k) {
    // dp[i][j]: ways using points 0..i with j segments
    List<List<int>> dp = List.generate(n, (_) => List.filled(k + 1, 0));
    List<List<int>> pref = List.generate(n, (_) => List.filled(k + 1, 0));

    // Base: zero segments -> one way (choose nothing)
    for (int i = 0; i < n; i++) {
      dp[i][0] = 1;
      pref[i][0] = (i == 0) ? 1 : (pref[i - 1][0] + 1) % _mod;
    }

    for (int seg = 1; seg <= k; seg++) {
      for (int i = 0; i < n; i++) {
        if (i == 0) {
          dp[i][seg] = 0; // cannot end a segment at point 0
        } else {
          int add = (i >= 2) ? pref[i - 2][seg - 1] : 0;
          dp[i][seg] = (dp[i - 1][seg] + add) % _mod;
        }
      }
      // build prefix sums for current seg
      for (int i = 0; i < n; i++) {
        pref[i][seg] = (i == 0) ? dp[i][seg] : (pref[i - 1][seg] + dp[i][seg]) % _mod;
      }
    }

    return dp[n - 1][k];
  }
}
```

## Golang

```go
func numberOfSets(n int, k int) int {
	const MOD int64 = 1000000007
	dp0 := make([]int64, k+2)
	dp1 := make([]int64, k+2)
	dp0[0] = 1

	for i := 0; i < n; i++ {
		ndp0 := make([]int64, k+2)
		ndp1 := make([]int64, k+2)
		for j := 0; j <= k; j++ {
			if dp0[j] != 0 {
				val := dp0[j]
				ndp0[j] = (ndp0[j] + val) % MOD          // skip point
				ndp1[j] = (ndp1[j] + val) % MOD          // start new segment
			}
			if dp1[j] != 0 {
				val := dp1[j]
				ndp1[j] = (ndp1[j] + val) % MOD          // keep segment open, skip point
				if j+1 <= k {
					ndp0[j+1] = (ndp0[j+1] + val) % MOD // close segment here
				}
			}
		}
		dp0, dp1 = ndp0, ndp1
	}
	return int(dp0[k] % MOD)
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def number_of_sets(n, k)
  dp = Array.new(n + 1) { Array.new(k + 1, 0) }
  pre = Array.new(n + 1) { Array.new(k + 1, 0) }

  dp[0][0] = 1
  pre[0][0] = 1

  (1..n).each do |i|
    dp[i][0] = 1
    pre[i][0] = (pre[i - 1][0] + dp[i][0]) % MOD
  end

  (1..k).each do |j|
    (1..n).each do |i|
      val = dp[i - 1][j]
      if i >= 2
        val += pre[i - 2][j - 1]
      end
      dp[i][j] = val % MOD
      pre[i][j] = (pre[i - 1][j] + dp[i][j]) % MOD
    end
  end

  dp[n][k]
end
```

## Scala

```scala
object Solution {
    def numberOfSets(n: Int, k: Int): Int = {
        val MOD = 1000000007L
        val dp = Array.ofDim[Long](n, k + 1)
        val pref = Array.ofDim[Long](n, k + 1)

        var i = 0
        while (i < n) {
            pref(i)(0) = 1L
            i += 1
        }

        var j = 1
        while (j <= k) {
            var cumPrev: Long = 0L
            i = 0
            while (i < n) {
                if (i > 0) dp(i)(j) = cumPrev else dp(i)(j) = 0L
                val leftPref = if (i > 0) pref(i - 1)(j) else 0L
                pref(i)(j) = (leftPref + dp(i)(j)) % MOD
                cumPrev = (cumPrev + pref(i)(j - 1)) % MOD
                i += 1
            }
            j += 1
        }

        val ans = if (n == 0) 0L else pref(n - 1)(k) % MOD
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_sets(n: i32, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = n as usize;
        let k = k as usize;
        if k == 0 {
            return 1;
        }
        // dp[i][j]: ways using points 0..i with j segments, no open segment at i
        let mut dp = vec![vec![0i64; k + 1]; n];
        let mut pref = vec![vec![0i64; k + 1]; n];
        dp[0][0] = 1;
        pref[0][0] = 1;
        for i in 1..n {
            for j in 0..=k {
                let mut val = dp[i - 1][j];
                if j > 0 && i >= 2 {
                    val = (val + pref[i - 2][j - 1]) % MOD;
                }
                dp[i][j] = val;
            }
            for j in 0..=k {
                pref[i][j] = (pref[i - 1][j] + dp[i][j]) % MOD;
            }
        }
        dp[n - 1][k] as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (number-of-sets n k)
  (-> exact-integer? exact-integer? exact-integer?)
  (let* ((dp (make-vector (+ n 1)))
         (pref (make-vector (+ n 1))))
    ;; initialize inner vectors
    (for ([i (in-range (+ n 1))])
      (vector-set! dp i (make-vector (+ k 1) 0))
      (vector-set! pref i (make-vector (+ k 1) 0)))
    ;; base case: zero points, zero segments -> 1 way
    (vector-set! (vector-ref dp 0) 0 1)
    (vector-set! (vector-ref pref 0) 0 1)
    ;; fill DP tables
    (for ([i (in-range 1 (+ n 1))])
      (let* ((dp-i (vector-ref dp i))
             (pref-i (vector-ref pref i))
             (dp-im1 (vector-ref dp (- i 1)))
             (pref-im1 (if (> i 0) (vector-ref pref (- i 1)) #f))
             (pref-im2 (if (>= (- i 2) 0) (vector-ref pref (- i 2)) #f)))
        ;; j = 0 -> exactly one way (choose nothing)
        (vector-set! dp-i 0 1)
        (vector-set! pref-i 0
                     (modulo (+ (if (> i 0) (vector-ref pref-im1 0) 0) 1) MOD))
        ;; other j values
        (for ([j (in-range 1 (+ k 1))])
          (let* ((term1 (vector-ref dp-im1 j))
                 (term2 (if pref-im2
                            (vector-ref pref-im2 (- j 1))
                            0))
                 (val (modulo (+ term1 term2) MOD)))
            (vector-set! dp-i j val)
            (let ((prev-pref (if (> i 0) (vector-ref pref-im1 j) 0)))
              (vector-set! pref-i j (modulo (+ prev-pref val) MOD))))))
      )
    ;; answer
    (vector-ref (vector-ref dp n) k)))
```

## Erlang

```erlang
-module(solution).
-export([number_of_sets/2]).

-define(MOD, 1000000007).

number_of_sets(N, K) ->
    Mod = ?MOD,
    SizeK = K + 1,
    %% dp row for i = 0
    Dp0 = array:set(0, 1, array:new(SizeK, {default, 0})),
    %% pref row for i = 0 (cumulative over rows)
    Pref0 = Dp0,
    %% outer array storing pref rows indexed by i (0..N)
    PrefRows0 = array:set(0, Pref0, array:new(N + 1, {default, undefined})),
    loop(1, N, K, Mod, Dp0, PrefRows0).

loop(I, N, _K, _Mod, DpPrev, _PrefRows) when I > N ->
    %% finished, answer is dp[N][K]
    array:get(_K = length(array:to_list(DpPrev)) - 1, DpPrev);
loop(I, N, K, Mod, DpPrev, PrefRows) ->
    SizeK = K + 1,
    %% compute current dp row
    DpCurr0 = array:new(SizeK, {default, 0}),
    DpCurr = dp_row(0, I, K, Mod, DpPrev, PrefRows, DpCurr0),
    %% compute current pref row using previous pref row (i-1)
    PrevPrefRow = array:get(I - 1, PrefRows),
    PrefCurr0 = array:new(SizeK, {default, 0}),
    PrefCurr = pref_row(0, K, Mod, DpCurr, PrevPrefRow, PrefCurr0),
    %% store current pref row
    NewPrefRows = array:set(I, PrefCurr, PrefRows),
    loop(I + 1, N, K, Mod, DpCurr, NewPrefRows).

dp_row(J, _I, K, _Mod, _DpPrev, _PrefRows, Acc) when J > K ->
    Acc;
dp_row(J, I, K, Mod, DpPrev, PrefRows, Acc) ->
    Val = case J of
        0 -> 1;
        _ ->
            PrevVal = array:get(J, DpPrev),
            Add = if
                I >= 2 ->
                    PrefRowI2 = array:get(I - 2, PrefRows),
                    array:get(J - 1, PrefRowI2);
                true -> 0
            end,
            (PrevVal + Add) rem Mod
    end,
    NewAcc = array:set(J, Val, Acc),
    dp_row(J + 1, I, K, Mod, DpPrev, PrefRows, NewAcc).

pref_row(J, _K, _Mod, _DpCurr, _PrevPrefRow, Acc) when J > _K ->
    Acc;
pref_row(J, K, Mod, DpCurr, PrevPrefRow, Acc) ->
    Prev = array:get(J, PrevPrefRow),
    Curr = array:get(J, DpCurr),
    Val = (Prev + Curr) rem Mod,
    NewAcc = array:set(J, Val, Acc),
    pref_row(J + 1, K, Mod, DpCurr, PrevPrefRow, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @mod 1_000_000_007

  @spec number_of_sets(integer, integer) :: integer
  def number_of_sets(n, k) do
    # row0: dp[0][0] = 1, others 0
    row0 = List.duplicate(0, k + 1) |> List.replace_at(0, 1)

    dp_arr =
      :array.set(
        0,
        row0,
        :array.new(n + 1)
      )

    pref_arr =
      :array.set(
        0,
        row0,
        :array.new(n + 1)
      )

    {dp_arr, pref_arr} =
      Enum.reduce(1..n, {dp_arr, pref_arr}, fn i, {dp_a, pref_a} ->
        prev_dp = :array.get(i - 1, dp_a)
        prev_pref = :array.get(i - 1, pref_a)

        pref_i_2 =
          if i >= 2 do
            :array.get(i - 2, pref_a)
          else
            nil
          end

        dp_cur =
          Enum.map(0..k, fn j ->
            cond do
              j == 0 ->
                1

              true ->
                val = Enum.at(prev_dp, j)

                add =
                  if i >= 2 do
                    Enum.at(pref_i_2, j - 1)
                  else
                    0
                  end

                rem(val + add, @mod)
            end
          end)

        pref_cur =
          Enum.map(0..k, fn j ->
            prev = Enum.at(prev_pref, j)
            cur = Enum.at(dp_cur, j)
            rem(prev + cur, @mod)
          end)

        {
          :array.set(i, dp_cur, dp_a),
          :array.set(i, pref_cur, pref_a)
        }
      end)

    final_row = :array.get(n, dp_arr)
    Enum.at(final_row, k)
  end
end
```
