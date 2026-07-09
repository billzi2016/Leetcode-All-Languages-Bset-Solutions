# 2834. Find the Minimum Possible Sum of a Beautiful Array

## Cpp

```cpp
class Solution {
public:
    int minimumPossibleSum(int n, int target) {
        const long long MOD = 1000000007LL;
        long long k = target / 2; // maximum count of small numbers we can take
        if (n <= k) {
            long long nn = n;
            long long ans = nn % MOD * ((nn + 1) % MOD) % MOD;
            ans = ans * 500000004LL % MOD; // multiply by inverse of 2 modulo MOD
            return (int)ans;
        }
        long long sumSmall = k % MOD * ((k + 1) % MOD) % MOD;
        sumSmall = sumSmall * 500000004LL % MOD; // divide by 2
        
        long long extra = n - k; // number of large elements needed
        long long a = target % MOD;
        long long extraMod = extra % MOD;
        long long term = ( (2LL * a) % MOD + ((extra - 1) % MOD) ) % MOD;
        long long sumLarge = extraMod * term % MOD;
        sumLarge = sumLarge * 500000004LL % MOD; // divide by 2
        
        long long ans = (sumSmall + sumLarge) % MOD;
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    private static final long MOD = 1_000_000_007L;
    public int minimumPossibleSum(int n, int target) {
        long N = n;
        long T = target;
        long cntLow = T / 2; // numbers 1 .. floor(target/2)
        if (N <= cntLow) {
            long ans = N * (N + 1) / 2;
            return (int)(ans % MOD);
        }
        long lowSum = cntLow * (cntLow + 1) / 2;
        long rem = N - cntLow; // numbers taken from target, target+1, ...
        long highSum = rem * T + rem * (rem - 1) / 2;
        long ans = (lowSum + highSum) % MOD;
        return (int)ans;
    }
}
```

## Python

```python
class Solution(object):
    def minimumPossibleSum(self, n, target):
        """
        :type n: int
        :type target: int
        :rtype: int
        """
        MOD = 10**9 + 7
        half = target // 2
        if n <= half:
            ans = n * (n + 1) // 2
        else:
            k = n - half
            sum_small = half * (half + 1) // 2
            sum_extra = k * (2 * target + k - 1) // 2
            ans = sum_small + sum_extra
        return ans % MOD
```

## Python3

```python
class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        MOD = 10**9 + 7
        k = target // 2  # count of allowed numbers less than target
        if n <= k:
            ans = n * (n + 1) // 2
            return ans % MOD
        sum_low = k * (k + 1) // 2
        r = n - k
        sum_high = r * target + r * (r - 1) // 2
        ans = (sum_low + sum_high) % MOD
        return ans
```

## C

```c
#include <stdint.h>

static const int64_t MOD = 1000000007LL;
static const int64_t INV2 = 500000004LL; // modular inverse of 2 modulo MOD

int minimumPossibleSum(int n, int target) {
    int64_t N = n;
    int64_t T = target;
    int64_t m = T / 2; // floor division
    
    if (N <= m) {
        int64_t ans = (N % MOD) * ((N + 1) % MOD) % MOD;
        ans = ans * INV2 % MOD;
        return (int)ans;
    } else {
        int64_t sum_small = (m % MOD) * ((m + 1) % MOD) % MOD;
        sum_small = sum_small * INV2 % MOD;
        
        int64_t extra = N - m;
        int64_t first = T % MOD;
        int64_t last = (T + extra - 1) % MOD;
        int64_t sum_extra = (extra % MOD) * ((first + last) % MOD) % MOD;
        sum_extra = sum_extra * INV2 % MOD;
        
        int64_t ans = (sum_small + sum_extra) % MOD;
        return (int)ans;
    }
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumPossibleSum(int n, int target) {
        const long MOD = 1_000_000_007L;
        long nn = n;
        long tt = target;

        long cntSmall = (tt - 1) / 2;                 // numbers i where 2*i < target
        bool even = (tt % 2 == 0);
        long m = cntSmall + (even ? 1 : 0);           // total safe numbers before reaching 'target'

        if (nn <= m) {
            long ans = nn * (nn + 1) / 2;
            return (int)(ans % MOD);
        }

        // Sum of all safe numbers less than target
        long sumFirstPart = cntSmall * (cntSmall + 1) / 2; // sum of 1..cntSmall
        long sumAllowed = sumFirstPart;
        if (even) {
            sumAllowed += tt / 2;                     // include target/2 when target is even
        }

        long extraCount = nn - m;                    // numbers we need from >= target
        long first = tt;                             // start at 'target'
        long last = first + extraCount - 1;          // last number taken

        // Sum of arithmetic series: extraCount * (first + last) / 2
        long sumExtra = extraCount * (first + last) / 2;

        long total = (sumAllowed % MOD + sumExtra % MOD) % MOD;
        return (int)total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} target
 * @return {number}
 */
var minimumPossibleSum = function(n, target) {
    const MOD = 1000000007n;
    const bigN = BigInt(n);
    const bigTarget = BigInt(target);
    
    // k = floor(target / 2)
    const kNum = Math.floor(target / 2);
    const bigK = BigInt(kNum);
    
    let ans;
    if (bigN <= bigK) {
        // sum of first n natural numbers
        ans = bigN * (bigN + 1n) / 2n;
    } else {
        // sum of first k numbers
        const sumFirst = bigK * (bigK + 1n) / 2n;
        const remaining = bigN - bigK;               // count of numbers after k
        const first = bigTarget;                     // start from target
        const last = bigTarget + remaining - 1n;     // end value
        const sumSecond = (first + last) * remaining / 2n;
        ans = sumFirst + sumSecond;
    }
    
    return Number(ans % MOD);
};
```

## Typescript

```typescript
function minimumPossibleSum(n: number, target: number): number {
    const MOD = 1000000007n;
    const safe = Math.floor(target / 2);
    if (n <= safe) {
        const nn = BigInt(n);
        const sum = (nn * (nn + 1n) / 2n) % MOD;
        return Number(sum);
    } else {
        const safeBig = BigInt(safe);
        const sumSafe = (safeBig * (safeBig + 1n) / 2n) % MOD;

        const r = n - safe; // remaining count
        const rBig = BigInt(r);
        const targetBig = BigInt(target);

        let extra = (rBig * targetBig) % MOD;
        extra = (extra + (rBig * (rBig - 1n) / 2n)) % MOD;

        const total = (sumSafe + extra) % MOD;
        return Number(total);
    }
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $target
     * @return Integer
     */
    function minimumPossibleSum($n, $target) {
        $MOD = 1000000007;
        // maximum count of numbers we can take below target
        $cntSmall = intdiv($target, 2); // floor(target/2)

        if ($n <= $cntSmall) {
            $sum = intdiv($n * ($n + 1), 2);
            return $sum % $MOD;
        }

        // sum of all selectable numbers below target
        $sumSmall = intdiv($cntSmall * ($cntSmall + 1), 2);

        // remaining numbers are taken starting from target upwards
        $r = $n - $cntSmall; // count of numbers >= target
        $sumLarge = intdiv($r * (2 * $target + $r - 1), 2);

        $total = ($sumSmall + $sumLarge) % $MOD;
        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func minimumPossibleSum(_ n: Int, _ target: Int) -> Int {
        let MOD: Int64 = 1_000_000_007
        let n64 = Int64(n)
        let t64 = Int64(target)
        let cntSmall = t64 / 2   // number of allowed numbers less than target
        
        if n64 <= cntSmall {
            let ans = (n64 * (n64 + 1) / 2) % MOD
            return Int(ans)
        } else {
            let need = n64 - cntSmall
            let sumSmall = cntSmall * (cntSmall + 1) / 2
            let add = need * t64 + need * (need - 1) / 2
            let ans = (sumSmall + add) % MOD
            return Int(ans)
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumPossibleSum(n: Int, target: Int): Int {
        val MOD = 1_000_000_007L
        val nL = n.toLong()
        val tL = target.toLong()
        val limit = tL / 2 // floor(target/2)

        return if (nL <= limit) {
            ((nL * (nL + 1) / 2) % MOD).toInt()
        } else {
            val sumSmall = limit * (limit + 1) / 2
            val rem = nL - limit // at least 1
            var largeSum = tL
            if (rem > 1) {
                val rMinus1 = rem - 1
                val sumNext = rMinus1 * (2L * tL + rem) / 2
                largeSum += sumNext
            }
            ((sumSmall + largeSum) % MOD).toInt()
        }
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int minimumPossibleSum(int n, int target) {
    int safe = target ~/ 2; // count of guaranteed safe numbers
    if (n <= safe) {
      int ans = ((n * (n + 1)) ~/ 2) % _mod;
      return ans;
    }
    int r = n - safe; // additional numbers needed beyond the safe ones

    int sumSmall = ((safe * (safe + 1)) ~/ 2) % _mod;

    // Sum of r consecutive integers starting from target:
    // r * (first + last) / 2 where first = target, last = target + r - 1
    int sumExtra = ((r * (2 * target + r - 1)) ~/ 2) % _mod;

    return (sumSmall + sumExtra) % _mod;
  }
}
```

## Golang

```go
func minimumPossibleSum(n int, target int) int {
	const MOD int64 = 1000000007
	nn := int64(n)
	tt := int64(target)

	smallCount := tt / 2 // numbers we can take without conflict

	if nn <= smallCount {
		sum := nn * (nn + 1) / 2 % MOD
		return int(sum)
	}

	// sum of the first smallCount natural numbers
	sumSmall := smallCount * (smallCount + 1) / 2 % MOD

	rem := nn - smallCount // remaining numbers needed, start from target upwards
	// arithmetic series: target, target+1, ..., target+rem-1
	sumLarge := rem * (2*tt + rem - 1) / 2 % MOD

	ans := (sumSmall + sumLarge) % MOD
	return int(ans)
}
```

## Ruby

```ruby
def minimum_possible_sum(n, target)
  mod = 1_000_000_007
  cnt = target.even? ? target / 2 : (target - 1) / 2

  if n <= cnt
    ans = n * (n + 1) / 2
    return ans % mod
  end

  sum_small = cnt * (cnt + 1) / 2
  rem = n - cnt
  sum_large = rem * target + rem * (rem - 1) / 2
  (sum_small + sum_large) % mod
end
```

## Scala

```scala
object Solution {
    def minimumPossibleSum(n: Int, target: Int): Int = {
        val MOD = 1000000007L
        val limit = target / 2 // floor(target/2)
        if (n <= limit) {
            val nn = n.toLong
            ((nn * (nn + 1) / 2) % MOD).toInt
        } else {
            val lim = limit.toLong
            val sumSmall = (lim * (lim + 1) / 2) % MOD
            val remaining = n - limit
            val r = remaining.toLong
            val a = target.toLong
            // sum of arithmetic series: a, a+1, ..., a+r-1
            val sumRemaining = r * (2 * a + r - 1) / 2
            ((sumSmall + (sumRemaining % MOD)) % MOD).toInt
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_possible_sum(n: i32, target: i32) -> i32 {
        const MOD: i128 = 1_000_000_007;
        let n = n as i128;
        let target = target as i128;
        let k = target / 2; // maximum count we can take from [1, target-1]

        if n <= k {
            ((n * (n + 1) / 2) % MOD) as i32
        } else {
            let sum_first_k = k * (k + 1) / 2 % MOD;
            let rem = n - k;
            // extra numbers start from target and increase by 1
            let extra = (rem * target + rem * (rem - 1) / 2) % MOD;
            ((sum_first_k + extra) % MOD) as i32
        }
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (minimum-possible-sum n target)
  (-> exact-integer? exact-integer? exact-integer?)
  (let* ((k (quotient target 2))                     ; floor(target/2)
         (sum
          (if (<= n k)
              (quotient (* n (+ n 1)) 2)            ; sum of first n integers
              (let* ((sum-small (quotient (* k (+ k 1)) 2))   ; sum 1..k
                     (r (- n k))
                     (extra (+ (* r target)
                               (quotient (* r (- r 1)) 2)))) ; sum of r numbers starting at target
                (+ sum-small extra)))))
    (modulo sum MOD)))
```

## Erlang

```erlang
-spec minimum_possible_sum(N :: integer(), Target :: integer()) -> integer().
minimum_possible_sum(N, Target) ->
    Mod = 1000000007,
    SmallCnt = Target div 2,
    if
        N =< SmallCnt ->
            (N * (N + 1) div 2) rem Mod;
        true ->
            SumSmall = (SmallCnt * (SmallCnt + 1) div 2) rem Mod,
            Rem = N - SmallCnt,
            SumExtraFull = Rem * (2 * Target + Rem - 1) div 2,
            SumExtra = SumExtraFull rem Mod,
            (SumSmall + SumExtra) rem Mod
    end.
```

## Elixir

```elixir
defmodule Solution do
  @mod 1_000_000_007

  @spec minimum_possible_sum(n :: integer, target :: integer) :: integer
  def minimum_possible_sum(n, target) do
    k = div(target - 1, 2)

    if n <= k do
      sum = div(n * (n + 1), 2)
      rem(sum, @mod)
    else
      r = n - k
      sum_small = div(k * (k + 1), 2)
      sum_extra = r * target + div(r * (r - 1), 2)
      total = sum_small + sum_extra
      rem(total, @mod)
    end
  end
end
```
