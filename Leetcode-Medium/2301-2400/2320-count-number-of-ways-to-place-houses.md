# 2320. Count Number of Ways to Place Houses

## Cpp

```cpp
class Solution {
public:
    int countHousePlacements(int n) {
        const int MOD = 1000000007;
        if (n == 0) return 1; // though n>=1 per constraints
        long long prev2 = 1; // a[0]
        long long prev1 = 2; // a[1]
        for (int i = 2; i <= n; ++i) {
            long long cur = (prev1 + prev2) % MOD;
            prev2 = prev1;
            prev1 = cur;
        }
        long long waysOneSide = (n == 0 ? prev2 : prev1);
        return (int)((waysOneSide * waysOneSide) % MOD);
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    
    public int countHousePlacements(int n) {
        long waysOneSide;
        if (n == 0) {
            waysOneSide = 1;
        } else if (n == 1) {
            waysOneSide = 2;
        } else {
            long a = 1; // dp[0]
            long b = 2; // dp[1]
            for (int i = 2; i <= n; i++) {
                long c = (a + b) % MOD;
                a = b;
                b = c;
            }
            waysOneSide = b;
        }
        long result = (waysOneSide * waysOneSide) % MOD;
        return (int) result;
    }
}
```

## Python

```python
class Solution(object):
    def countHousePlacements(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        # dp[i] = number of ways for one side with i plots (no adjacent houses)
        # dp[0] = 1 (empty), dp[1] = 2 (empty or house)
        if n == 0:
            return 1
        prev, cur = 1, 2  # dp[0], dp[1]
        for i in range(2, n + 1):
            prev, cur = cur, (prev + cur) % MOD
        ways_one_side = cur
        return (ways_one_side * ways_one_side) % MOD
```

## Python3

```python
class Solution:
    def countHousePlacements(self, n: int) -> int:
        MOD = 10**9 + 7
        # f(0)=1 (empty), f(1)=2 (empty or house)
        if n == 0:
            return 1
        a, b = 1, 2  # f(i-2), f(i-1)
        for _ in range(2, n + 1):
            a, b = b, (a + b) % MOD
        ways_one_side = b
        return (ways_one_side * ways_one_side) % MOD
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

static const int MOD = 1000000007;

int countHousePlacements(int n) {
    long long f0 = 0, f1 = 1; // Fib(0), Fib(1)
    for (int i = 2; i <= n + 2; ++i) {
        long long fi = (f0 + f1) % MOD;
        f0 = f1;
        f1 = fi;
    }
    long long waysOneSide = (n == 0) ? 1 : f1; // for completeness
    long long ans = (waysOneSide * waysOneSide) % MOD;
    return static_cast<int>(ans);
}
```

## Csharp

```csharp
public class Solution {
    private const int MOD = 1000000007;
    public int CountHousePlacements(int n) {
        long a = 0; // Fib(0)
        long b = 1; // Fib(1)
        for (int i = 2; i <= n + 2; i++) {
            long c = (a + b) % MOD;
            a = b;
            b = c;
        }
        long waysOneSide = b; // Fib(n+2)
        long ans = (waysOneSide * waysOneSide) % MOD;
        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var countHousePlacements = function(n) {
    const MOD = 1000000007n;
    // dp[i] = number of ways for one side with i plots (no adjacent houses)
    // dp[0]=1, dp[1]=2, dp[i]=dp[i-1]+dp[i-2]
    let a = 1n; // dp[0]
    let b = 2n; // dp[1]
    if (n === 0) {
        return Number((a * a) % MOD);
    }
    for (let i = 2; i <= n; ++i) {
        const c = (a + b) % MOD;
        a = b;
        b = c;
    }
    const waysOneSide = b; // dp[n]
    const result = (waysOneSide * waysOneSide) % MOD;
    return Number(result);
};
```

## Typescript

```typescript
function countHousePlacements(n: number): number {
    const MOD = 1000000007n;
    // f[0] = 1, f[1] = 2
    let prev = 1n; // f[i-2]
    let curr = 2n; // f[i-1]
    if (n === 0) {
        const ans = (prev * prev) % MOD;
        return Number(ans);
    }
    for (let i = 2; i <= n; i++) {
        const next = (prev + curr) % MOD;
        prev = curr;
        curr = next;
    }
    const f = n === 1 ? curr : curr; // after loop, curr holds f[n]
    const ans = (f * f) % MOD;
    return Number(ans);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function countHousePlacements($n) {
        $MOD = 1000000007;
        // f[0] = 1, f[1] = 2
        if ($n == 0) {
            return 1; // not needed per constraints but safe
        }
        $prev = 1; // f[i-2]
        $curr = 2; // f[i-1] for i=1
        for ($i = 2; $i <= $n; $i++) {
            $next = ($curr + $prev) % $MOD;
            $prev = $curr;
            $curr = $next;
        }
        $waysOneSide = $curr; // f[n]
        $result = ($waysOneSide * $waysOneSide) % $MOD;
        return (int)$result;
    }
}
```

## Swift

```swift
class Solution {
    func countHousePlacements(_ n: Int) -> Int {
        let MOD = 1_000_000_007
        if n == 0 { return 1 } // though n >= 1 per constraints
        var a = 1   // f[0]
        var b = 2   // f[1]
        if n == 1 {
            let ans = Int((Int64(b) * Int64(b)) % Int64(MOD))
            return ans
        }
        for _ in 2...n {
            let c = (a + b) % MOD
            a = b
            b = c
        }
        let ans = Int((Int64(b) * Int64(b)) % Int64(MOD))
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countHousePlacements(n: Int): Int {
        val MOD = 1_000_000_007L
        if (n == 0) return 1
        var fPrev = 1L   // f[0]
        var fCurr = 2L   // f[1]
        if (n == 1) {
            return ((fCurr * fCurr) % MOD).toInt()
        }
        var fNext = 0L
        for (i in 2..n) {
            fNext = (fCurr + fPrev) % MOD
            fPrev = fCurr
            fCurr = fNext
        }
        return ((fCurr * fCurr) % MOD).toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int countHousePlacements(int n) {
    // DP for one side: dp[i] = number of ways for i plots
    // dp[0] = 1, dp[1] = 2, dp[i] = (dp[i-1] + dp[i-2]) % MOD
    int dpPrev = 1; // dp[0]
    if (n == 0) {
      return (dpPrev * dpPrev) % _mod;
    }
    int dpCurr = 2; // dp[1]
    for (int i = 2; i <= n; ++i) {
      int next = (dpPrev + dpCurr) % _mod;
      dpPrev = dpCurr;
      dpCurr = next;
    }
    int waysOneSide = dpCurr; // dp[n]
    return (waysOneSide * waysOneSide) % _mod;
  }
}
```

## Golang

```go
func countHousePlacements(n int) int {
	const MOD = 1000000007
	if n == 0 {
		return 1
	}
	a, b := 1, 2 // f[0], f[1]
	for i := 2; i <= n; i++ {
		c := (a + b) % MOD
		a, b = b, c
	}
	res := int64(b) * int64(b) % MOD
	return int(res)
}
```

## Ruby

```ruby
def count_house_placements(n)
  mod = 1_000_000_007
  # f[0] = 1 (empty), f[1] = 2 (0 or 1)
  a = 1
  b = 2
  if n == 0
    return (a * a) % mod
  elsif n == 1
    return (b * b) % mod
  end
  (2..n).each do
    c = (a + b) % mod
    a = b
    b = c
  end
  (b * b) % mod
end
```

## Scala

```scala
object Solution {
    def countHousePlacements(n: Int): Int = {
        val MOD = 1000000007L
        if (n == 0) return 1
        var prev = 1L // a[0]
        var curr = 2L // a[1]
        for (i <- 2 to n) {
            val next = (prev + curr) % MOD
            prev = curr
            curr = next
        }
        ((curr * curr) % MOD).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_house_placements(n: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut f0: i64 = 0; // Fib(0)
        let mut f1: i64 = 1; // Fib(1)
        for _ in 0..(n + 2) {
            let f2 = (f0 + f1) % MOD;
            f0 = f1;
            f1 = f2;
        }
        let ways_one_side = f0; // Fib(n+2)
        let ans = (ways_one_side * ways_one_side) % MOD;
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (count-house-placements n)
  (-> exact-integer? exact-integer?)
  (let* ((mod 1000000007)
         (m (+ n 2))
         (fib
          (let loop ((i 0) (a 0) (b 1))
            (if (= i m)
                a
                (loop (+ i 1) b (remainder (+ a b) mod)))))
         (ans (remainder (* fib fib) mod)))
    ans))
```

## Erlang

```erlang
-spec count_house_placements(N :: integer()) -> integer().
count_house_placements(N) ->
    Mod = 1000000007,
    F = fib_mod(N + 2, Mod),
    (F * F) rem Mod.

fib_mod(0, _) -> 0;
fib_mod(1, _) -> 1;
fib_mod(K, Mod) when K >= 2 ->
    fib_iter(2, K, 0, 1, Mod).

fib_iter(I, K, A, B, Mod) when I > K ->
    B;
fib_iter(I, K, A, B, Mod) ->
    C = (A + B) rem Mod,
    fib_iter(I + 1, K, B, C, Mod).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @spec count_house_placements(n :: integer) :: integer
  def count_house_placements(n) do
    mod = 1_000_000_007
    f0 = 1
    f1 = 2

    f_n =
      cond do
        n == 0 -> f0
        n == 1 -> f1
        true ->
          {_, fn_val} =
            Enum.reduce(2..n, {f0, f1}, fn _, {prev2, prev1} ->
              cur = rem(prev1 + prev2, mod)
              {prev1, cur}
            end)

          fn_val
      end

    rem(f_n * f_n, mod)
  end
end
```
