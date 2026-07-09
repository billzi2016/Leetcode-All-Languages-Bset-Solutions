# 0790. Domino and Tromino Tiling

## Cpp

```cpp
class Solution {
public:
    int numTilings(int n) {
        const int MOD = 1000000007;
        if (n == 0) return 1;
        if (n == 1) return 1;
        if (n == 2) return 2;
        vector<long long> dp(n + 1), pref(n + 1);
        dp[0] = 1;
        dp[1] = 1;
        dp[2] = 2;
        pref[0] = dp[0];
        pref[1] = (pref[0] + dp[1]) % MOD;
        pref[2] = (pref[1] + dp[2]) % MOD;
        for (int i = 3; i <= n; ++i) {
            long long extra = pref[i - 3];
            dp[i] = (dp[i - 1] + dp[i - 2] + 2LL * extra) % MOD;
            pref[i] = (pref[i - 1] + dp[i]) % MOD;
        }
        return static_cast<int>(dp[n]);
    }
};
```

## Java

```java
class Solution {
    public int numTilings(int n) {
        final long MOD = 1_000_000_007L;
        if (n == 0) return 1;
        long[] dp = new long[n + 3];
        dp[0] = 1;
        dp[1] = 1;
        if (n >= 2) dp[2] = 2;
        long extra = 0; // sum of dp[0..i-3]
        for (int i = 3; i <= n; i++) {
            extra = (extra + dp[i - 3]) % MOD;
            dp[i] = (dp[i - 1] + dp[i - 2] + 2 * extra) % MOD;
        }
        return (int) dp[n];
    }
}
```

## Python

```python
class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        if n == 0:
            return 1
        if n == 1:
            return 1

        prev_f, cur_f = 1, 1          # f[i-2], f[i-1]
        prev_p, cur_p = 0, 0          # p[i-2], p[i-1]

        for i in range(2, n + 1):
            new_p = (prev_f + cur_p) % MOD               # p[i] = f[i-2] + p[i-1]
            new_f = (cur_f + prev_f + 2 * cur_p) % MOD   # f[i] = f[i-1] + f[i-2] + 2*p[i-1]

            prev_f, cur_f = cur_f, new_f
            prev_p, cur_p = cur_p, new_p

        return cur_f
```

## Python3

```python
class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 1, 1, 2
        for i in range(3, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD
        return dp[n]
```

## C

```c
int numTilings(int n) {
    const int MOD = 1000000007;
    if (n == 0) return 1;
    if (n == 1) return 1;
    if (n == 2) return 2;
    long long f0 = 1; // f[i-3]
    long long f1 = 1; // f[i-2]
    long long f2 = 2; // f[i-1]
    long long fn = 0;
    for (int i = 3; i <= n; ++i) {
        fn = (2 * f2 + f0) % MOD; // f[i] = 2*f[i-1] + f[i-3]
        f0 = f1;
        f1 = f2;
        f2 = fn;
    }
    return (int)f2;
}
```

## Csharp

```csharp
public class Solution {
    public int NumTilings(int n) {
        const long MOD = 1000000007L;
        if (n == 0) return 1;
        if (n == 1) return 1;
        if (n == 2) return 2;

        long dp0 = 1; // dp[0]
        long dp1 = 1; // dp[1]
        long dp2 = 2; // dp[2]

        for (int i = 3; i <= n; i++) {
            long cur = (2 * dp2 + dp0) % MOD;
            dp0 = dp1;
            dp1 = dp2;
            dp2 = cur;
        }

        return (int)dp2;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var numTilings = function(n) {
    const MOD = 1000000007;
    if (n === 0) return 1;
    if (n === 1) return 1;
    if (n === 2) return 2;
    const dp = new Array(n + 1);
    dp[0] = 1;
    dp[1] = 1;
    dp[2] = 2;
    for (let i = 3; i <= n; i++) {
        dp[i] = ((2 * dp[i - 1]) % MOD + dp[i - 3]) % MOD;
    }
    return dp[n];
};
```

## Typescript

```typescript
function numTilings(n: number): number {
    const MOD = 1_000_000_007;
    if (n === 0) return 1;
    if (n === 1) return 1;
    if (n === 2) return 2;

    let dpMinus3 = 1; // dp[0]
    let dpMinus2 = 1; // dp[1]
    let dpMinus1 = 2; // dp[2]

    for (let i = 3; i <= n; i++) {
        const current = ((2 * dpMinus1) % MOD + dpMinus3) % MOD;
        dpMinus3 = dpMinus2;
        dpMinus2 = dpMinus1;
        dpMinus1 = current;
    }

    return dpMinus1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function numTilings($n) {
        $mod = 1000000007;
        if ($n == 0) return 1;
        if ($n == 1) return 1;
        if ($n == 2) return 2;

        $dp0 = 1; // dp[0]
        $dp1 = 1; // dp[1]
        $dp2 = 2; // dp[2]

        for ($i = 3; $i <= $n; $i++) {
            $cur = ( (2 * $dp2) % $mod + $dp0 ) % $mod;
            $dp0 = $dp1;
            $dp1 = $dp2;
            $dp2 = $cur;
        }

        return $dp2;
    }
}
```

## Swift

```swift
class Solution {
    func numTilings(_ n: Int) -> Int {
        let MOD = 1_000_000_007
        if n == 0 { return 1 }
        if n == 1 { return 1 }
        if n == 2 { return 2 }
        var dp = [Int](repeating: 0, count: n + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in 3...n {
            let val = ( (2 * dp[i - 1]) % MOD + dp[i - 3] ) % MOD
            dp[i] = val
        }
        return dp[n]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numTilings(n: Int): Int {
        val MOD = 1000000007L
        if (n == 0) return 1
        if (n == 1) return 1
        var aMinus2 = 1L // dp[0]
        var aMinus1 = 1L // dp[1]
        var bMinus1 = 0L // b[1]
        for (i in 2..n) {
            val aCurr = (aMinus1 + aMinus2 + 2L * bMinus1) % MOD
            val bCurr = (aMinus2 + bMinus1) % MOD
            aMinus2 = aMinus1
            aMinus1 = aCurr
            bMinus1 = bCurr
        }
        return aMinus1.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;
  int numTilings(int n) {
    if (n == 1) return 1;
    if (n == 2) return 2;
    int dp0 = 1; // dp[0]
    int dp1 = 1; // dp[1]
    int dp2 = 2; // dp[2]
    for (int i = 3; i <= n; ++i) {
      int cur = ((dp2 * 2) % _mod + dp0) % _mod;
      dp0 = dp1;
      dp1 = dp2;
      dp2 = cur;
    }
    return dp2;
  }
}
```

## Golang

```go
func numTilings(n int) int {
	const mod int64 = 1000000007
	if n == 0 {
		return 1
	}
	if n == 1 {
		return 1
	}
	if n == 2 {
		return 2
	}
	var a0, a1, a2 int64 = 1, 1, 2 // dp[0], dp[1], dp[2]
	for i := 3; i <= n; i++ {
		cur := (2*a2 + a0) % mod
		a0, a1, a2 = a1, a2, cur
	}
	return int(a2)
}
```

## Ruby

```ruby
def num_tilings(n)
  mod = 1_000_000_007
  return 1 if n == 0 || n == 1

  f_prev2 = 1   # f[0]
  f_prev1 = 1   # f[1]
  g_prev2 = 0   # g[0]
  g_prev1 = 1   # g[1]

  (2..n).each do
    f_curr = (f_prev1 + f_prev2 + 2 * g_prev1) % mod
    g_curr = (f_prev2 + g_prev1) % mod

    f_prev2, f_prev1 = f_prev1, f_curr
    g_prev2, g_prev1 = g_prev1, g_curr
  end

  f_prev1
end
```

## Scala

```scala
object Solution {
    def numTilings(n: Int): Int = {
        val MOD = 1000000007L
        if (n == 1) return 1
        if (n == 2) return 2

        var dpPrev2 = 1L // dp[0]
        var dpPrev1 = 1L // dp[1]
        var dpCurr = 2L  // dp[2]

        for (i <- 3 to n) {
            val newVal = ((dpCurr * 2) % MOD + dpPrev2) % MOD
            dpPrev2 = dpPrev1
            dpPrev1 = dpCurr
            dpCurr = newVal
        }
        dpCurr.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_tilings(n: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = n as usize;
        if n == 0 {
            return 1;
        }
        if n == 1 {
            return 1;
        }
        let mut f_prev2: i64 = 1; // f[0]
        let mut f_prev1: i64 = 1; // f[1]
        let mut extra: i64 = 0;   // sum of f[0..i-3] for current i
        for _ in 2..=n {
            let cur = (f_prev1 + f_prev2 + 2 * extra) % MOD;
            extra = (extra + f_prev2) % MOD;
            f_prev2 = f_prev1;
            f_prev1 = cur;
        }
        f_prev1 as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (num-tilings n)
  (-> exact-integer? exact-integer?)
  (cond
    [(<= n 0) 1]
    [(= n 1) 1]
    [(= n 2) 2]
    [else
     (let loop ((i 3) (f0 1) (f1 1) (f2 2))
       (if (> i n)
           f2
           (let ([fi (modulo (+ (* 2 f2) f0) MOD)])
             (loop (+ i 1) f1 f2 fi))))]))
```

## Erlang

```erlang
-module(solution).
-export([num_tilings/1]).

-spec num_tilings(N :: integer()) -> integer().
num_tilings(N) ->
    Mod = 1000000007,
    case N of
        0 -> 1;
        1 -> 1;
        2 -> 2;
        _ ->
            compute(N, 3, 1, 1, 2, Mod)
    end.

-spec compute(integer(), integer(), integer(), integer(), integer(), integer()) -> integer().
compute(N, I, D0, D1, D2, Mod) when I =< N ->
    New = (2 * D2 + D0) rem Mod,
    compute(N, I + 1, D1, D2, New, Mod);
compute(_, _, _, _, D2, _) -> D2.
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @spec num_tilings(n :: integer) :: integer
  def num_tilings(n) when is_integer(n) and n >= 0 do
    mod = 1_000_000_007

    case n do
      0 -> 1
      1 -> 1
      2 -> 2
      _ ->
        # dp[i-3], dp[i-2], dp[i-1]
        {dp_i_minus_3, dp_i_minus_2, dp_i_minus_1} = {1, 1, 2}

        {_a, _b, result} =
          Enum.reduce(3..n, {dp_i_minus_3, dp_i_minus_2, dp_i_minus_1}, fn _i,
                                                                          {a, b, c} ->
            cur = (2 * c + a) |> rem(mod)
            {b, c, cur}
          end)

        result
    end
  end
end
```
