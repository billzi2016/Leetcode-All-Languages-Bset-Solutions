# 1866. Number of Ways to Rearrange Sticks With K Sticks Visible

## Cpp

```cpp
class Solution {
public:
    int rearrangeSticks(int n, int k) {
        const int MOD = 1000000007;
        vector<vector<long long>> dp(n + 1, vector<long long>(k + 1, 0));
        dp[0][0] = 1;
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= min(i, k); ++j) {
                long long visible = dp[i - 1][j - 1];
                long long hidden = (dp[i - 1][j] * (i - 1)) % MOD;
                dp[i][j] = (visible + hidden) % MOD;
            }
        }
        return (int)dp[n][k];
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    public int rearrangeSticks(int n, int k) {
        if (k > n) return 0;
        long[][] dp = new long[n + 1][k + 1];
        dp[0][0] = 1;
        for (int i = 1; i <= n; i++) {
            int limit = Math.min(i, k);
            for (int j = 1; j <= limit; j++) {
                dp[i][j] = (dp[i - 1][j - 1] + (long) (i - 1) * dp[i - 1][j]) % MOD;
            }
        }
        return (int) dp[n][k];
    }
}
```

## Python

```python
class Solution(object):
    def rearrangeSticks(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        if k > n:
            return 0
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            maxj = min(i, k)
            for j in range(1, maxj + 1):
                dp[i][j] = (dp[i - 1][j - 1] + (i - 1) * dp[i - 1][j]) % MOD
        return dp[n][k]
```

## Python3

```python
class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        if k > n:
            return 0
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            max_j = min(i, k)
            for j in range(1, max_j + 1):
                dp[i][j] = (dp[i - 1][j - 1] + (i - 1) * dp[i - 1][j]) % MOD
        return dp[n][k]
```

## C

```c
#include <stddef.h>

static const int MOD = 1000000007;

int rearrangeSticks(int n, int k) {
    static int dp[1001][1001];
    // Initialize base case
    dp[1][1] = 1;
    for (int i = 2; i <= n; ++i) {
        dp[i][0] = 0; // not needed but safe
        for (int j = 1; j <= i; ++j) {
            long long term1 = dp[i - 1][j - 1];
            long long term2 = ((long long)(i - 1) * dp[i - 1][j]) % MOD;
            dp[i][j] = (int)((term1 + term2) % MOD);
        }
    }
    return dp[n][k];
}
```

## Csharp

```csharp
using System;

public class Solution {
    private const int MOD = 1000000007;
    
    public int RearrangeSticks(int n, int k) {
        int[,] dp = new int[n + 1, k + 1];
        dp[0, 0] = 1;
        
        for (int i = 1; i <= n; i++) {
            int maxJ = Math.Min(i, k);
            for (int j = 1; j <= maxJ; j++) {
                long ways = dp[i - 1, j - 1];
                ways += ((long)(i - 1) * dp[i - 1, j]) % MOD;
                dp[i, j] = (int)(ways % MOD);
            }
        }
        
        return dp[n, k];
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
var rearrangeSticks = function(n, k) {
    const MOD = 1000000007;
    // dp[i][j]: ways with i sticks and j visible
    const dp = Array.from({ length: n + 1 }, () => new Array(k + 1).fill(0));
    dp[0][0] = 1;
    for (let i = 1; i <= n; ++i) {
        const maxJ = Math.min(i, k);
        for (let j = 1; j <= maxJ; ++j) {
            // place the tallest stick at the end -> visible
            const addVisible = dp[i - 1][j - 1];
            // place it elsewhere -> not visible, (i-1) positions
            const addHidden = (dp[i - 1][j] * (i - 1)) % MOD;
            dp[i][j] = (addVisible + addHidden) % MOD;
        }
    }
    return dp[n][k];
};
```

## Typescript

```typescript
function rearrangeSticks(n: number, k: number): number {
    const MOD = 1_000_000_007;
    if (k > n) return 0;

    let prev = new Array(k + 1).fill(0);
    prev[0] = 1; // dp[0][0] = 1

    for (let i = 1; i <= n; i++) {
        const cur = new Array(k + 1).fill(0);
        const limit = Math.min(i, k);
        for (let j = 1; j <= limit; j++) {
            const addPrev = prev[j - 1];
            const mulPrev = ((i - 1) * prev[j]) % MOD;
            cur[j] = (addPrev + mulPrev) % MOD;
        }
        prev = cur;
    }

    return prev[k];
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
    function rearrangeSticks($n, $k) {
        $mod = 1000000007;
        // dp[j] = ways for current i sticks with j visible
        $dp = array_fill(0, $k + 1, 0);
        $dp[0] = 1; // 0 sticks, 0 visible

        for ($i = 1; $i <= $n; $i++) {
            $new = array_fill(0, $k + 1, 0);
            $maxJ = min($i, $k);
            for ($j = 1; $j <= $maxJ; $j++) {
                // place the i-th (largest) stick at the end -> visible
                $val = $dp[$j - 1];
                // place it somewhere else among i-1 positions -> not visible
                $val += (($i - 1) * $dp[$j]) % $mod;
                if ($val >= $mod) {
                    $val %= $mod;
                }
                $new[$j] = $val;
            }
            $dp = $new;
        }

        return $dp[$k] % $mod;
    }
}
```

## Swift

```swift
class Solution {
    func rearrangeSticks(_ n: Int, _ k: Int) -> Int {
        let MOD = 1_000_000_007
        var dp = Array(repeating: Array(repeating: 0, count: k + 2), count: n + 2)
        dp[0][0] = 1
        if n == 0 { return 0 }
        for i in 1...n {
            let maxK = min(i, k)
            for j in 1...maxK {
                var val = dp[i - 1][j - 1]
                let add = (Int64(i - 1) * Int64(dp[i - 1][j])) % Int64(MOD)
                val = (val + Int(add)) % MOD
                dp[i][j] = val
            }
        }
        return dp[n][k]
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val MOD = 1_000_000_007L
    fun rearrangeSticks(n: Int, k: Int): Int {
        val dp = Array(n + 1) { LongArray(k + 1) }
        dp[1][1] = 1L
        for (i in 2..n) {
            val maxJ = if (i < k) i else k
            for (j in 1..maxJ) {
                val addVisible = dp[i - 1][j - 1]
                val notVisible = ((i - 1).toLong() * dp[i - 1][j]) % MOD
                dp[i][j] = (addVisible + notVisible) % MOD
            }
        }
        return dp[n][k].toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int rearrangeSticks(int n, int k) {
    List<List<int>> dp = List.generate(
        n + 1, (_) => List.filled(k + 1, 0, growable: false),
        growable: false);
    dp[0][0] = 1;
    for (int i = 1; i <= n; ++i) {
      int maxJ = i < k ? i : k;
      for (int j = 1; j <= maxJ; ++j) {
        int addPrev = dp[i - 1][j - 1];
        int mulPrev = ((i - 1) * dp[i - 1][j]) % _mod;
        dp[i][j] = (addPrev + mulPrev) % _mod;
      }
    }
    return dp[n][k];
  }
}
```

## Golang

```go
func rearrangeSticks(n int, k int) int {
	const MOD int64 = 1000000007
	dp := make([][]int64, n+1)
	for i := 0; i <= n; i++ {
		dp[i] = make([]int64, k+1)
	}
	dp[0][0] = 1
	for i := 1; i <= n; i++ {
		maxJ := k
		if i < maxJ {
			maxJ = i
		}
		for j := 1; j <= maxJ; j++ {
			dp[i][j] = (dp[i-1][j-1] + int64(i-1)*dp[i-1][j]) % MOD
		}
	}
	return int(dp[n][k])
}
```

## Ruby

```ruby
def rearrange_sticks(n, k)
  return 0 if k > n
  mod = 1_000_000_007
  dp = Array.new(k + 1, 0)
  dp[0] = 1
  (1..n).each do |i|
    ndp = Array.new(k + 1, 0)
    (1..k).each do |j|
      val = dp[j - 1]
      val += ((i - 1) * dp[j]) % mod
      ndp[j] = val % mod
    end
    dp = ndp
  end
  dp[k] % mod
end
```

## Scala

```scala
object Solution {
  private val MOD = 1000000007L
  def rearrangeSticks(n: Int, k: Int): Int = {
    val dp = Array.ofDim[Long](n + 1, k + 1)
    if (n >= 1 && k >= 1) dp(1)(1) = 1L
    for (i <- 2 to n) {
      val maxJ = math.min(i, k)
      for (j <- 1 to maxJ) {
        val a = dp(i - 1)(j - 1)
        val b = ((i - 1).toLong * dp(i - 1)(j)) % MOD
        dp(i)(j) = (a + b) % MOD
      }
    }
    dp(n)(k).toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn rearrange_sticks(n: i32, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n_usize = n as usize;
        let k_usize = k as usize;
        let mut dp = vec![vec![0i64; k_usize + 1]; n_usize + 1];
        dp[0][0] = 1;
        for i in 1..=n_usize {
            let max_j = std::cmp::min(i, k_usize);
            for j in 1..=max_j {
                let visible = dp[i - 1][j - 1];
                let hidden = ((i as i64 - 1) * dp[i - 1][j]) % MOD;
                dp[i][j] = (visible + hidden) % MOD;
            }
        }
        dp[n_usize][k_usize] as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (rearrange-sticks n k)
  (-> exact-integer? exact-integer? exact-integer?)
  (if (> k n)
      0
      (let* ([dp (make-vector (+ n 1) #f)])
        ;; allocate rows
        (for ([i (in-range (+ n 1))])
          (vector-set! dp i (make-vector (+ k 1) 0)))
        ;; base case: one stick, one visible
        (when (and (>= n 1) (>= k 1))
          (vector-set! (vector-ref dp 1) 1 1))
        ;; fill DP table
        (for ([i (in-range 2 (add1 n))])
          (let* ([row (vector-ref dp i)]
                 [prev (vector-ref dp (- i 1))]
                 [limit (min i k)])
            (for ([j (in-range 1 (add1 limit))])
              (define val1 (vector-ref prev (sub1 j))) ; dp[i-1][j-1]
              (define val2 (vector-ref prev j))        ; dp[i-1][j]
              (define res (+ val1 (modulo (* (- i 1) val2) MOD)))
              (vector-set! row j (modulo res MOD)))))
        (vector-ref (vector-ref dp n) k))))
```

## Erlang

```erlang
-module(solution).
-export([rearrange_sticks/2]).

-define(MOD, 1000000007).

rearrange_sticks(N, K) when K > N ->
    0;
rearrange_sticks(N, K) ->
    Init = lists:duplicate(K + 1, 0),
    Prev = setelement(1, Init, 1), % dp[0][0] = 1
    Final = loop(1, N, K, Prev),
    element(K + 1, Final).

loop(CurN, N, _K, Prev) when CurN > N ->
    Prev;
loop(CurN, N, K, Prev) ->
    Curr = [calc(I, CurN, Prev) || I <- lists:seq(0, K)],
    loop(CurN + 1, N, K, Curr).

calc(0, _N, _Prev) ->
    0;
calc(I, N, Prev) ->
    PrevI   = element(I + 1, Prev),
    PrevIm1 = element(I,     Prev),
    ((PrevIm1 + ((N - 1) * PrevI rem ?MOD)) rem ?MOD).
```

## Elixir

```elixir
defmodule Solution do
  @spec rearrange_sticks(n :: integer, k :: integer) :: integer
  def rearrange_sticks(n, k) do
    mod = 1_000_000_007

    # dp[i][j] -> number of ways for i sticks with j visible
    dp0 = :array.new(k + 1, default: 0)
    dp0 = :array.set(0, 1, dp0)

    dp_final =
      Enum.reduce(1..n, dp0, fn i, dp_prev ->
        maxj = if i < k, do: i, else: k
        new_dp = :array.new(k + 1, default: 0)

        Enum.reduce(1..maxj, new_dp, fn j, acc ->
          val1 = :array.get(j - 1, dp_prev)
          val2 = :array.get(j, dp_prev)
          term = (val1 + (i - 1) * val2) |> rem(mod)
          :array.set(j, term, acc)
        end)
      end)

    :array.get(k, dp_final)
  end
end
```
