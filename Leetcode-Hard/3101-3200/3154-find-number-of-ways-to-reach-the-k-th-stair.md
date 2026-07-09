# 3154. Find Number of Ways to Reach the K-th Stair

## Cpp

```cpp
class Solution {
public:
    long long comb(int n, int r) {
        if (r < 0 || r > n) return 0;
        if (r > n - r) r = n - r;
        long long res = 1;
        for (int i = 1; i <= r; ++i) {
            res = res * (n - r + i) / i;
        }
        return res;
    }

    int waysToReachStair(int k) {
        long long ans = 0;
        for (int x = 0;; ++x) {
            long long pow2 = 1LL << x;                 // 2^x
            if (pow2 > (long long)k + x + 1) break;    // no valid y possible
            long long y = pow2 - k;                     // number of first-type ops
            if (y < 0 || y > x + 1) continue;
            ans += comb(x + 1, (int)y);
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int waysToReachStair(int k) {
        long ans = 0;
        for (int x = 0; ; x++) {
            long pow = 1L << x; // 2^x
            if (pow > (long)k + x + 1) break; // further x will only increase pow
            long y = pow - k;
            if (y >= 0 && y <= x + 1) {
                ans += nCr(x + 1, (int) y);
            }
        }
        return (int) ans;
    }

    private long nCr(int n, int r) {
        if (r < 0 || r > n) return 0;
        r = Math.min(r, n - r);
        long res = 1;
        for (int i = 1; i <= r; i++) {
            res = res * (n - r + i) / i;
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def waysToReachStair(self, k):
        """
        :type k: int
        :rtype: int
        """
        def nCk(n, k):
            if k < 0 or k > n:
                return 0
            k = min(k, n - k)
            res = 1
            for i in range(1, k + 1):
                res = res * (n - k + i) // i
            return res

        ans = 0
        x = 0
        while True:
            pow2 = 1 << x
            # condition derived from y = pow2 - k <= x+1  => pow2 <= k + x + 1
            if pow2 > k + x + 1:
                break
            y = pow2 - k
            if 0 <= y <= x + 1:
                ans += nCk(x + 1, y)
            x += 1
        return ans
```

## Python3

```python
import math

class Solution:
    def waysToReachStair(self, k: int) -> int:
        ans = 0
        for x in range(32):
            pow2 = 1 << x
            y = pow2 - k
            if 0 <= y <= x + 1:
                ans += math.comb(x + 1, y)
        return ans
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

int waysToReachStair(int k) {
    long long ans = 0;
    for (int x = 0; x < 60; ++x) {
        long long pow2 = 1LL << x;
        if (pow2 >= k) {
            long long y = pow2 - k;
            if (y > x + 1) {
                // For larger x, y only grows faster than x+1, so we can stop.
                break;
            }
            int n = x + 1;
            int r = (int)y;
            if (r < 0 || r > n) continue;
            if (r > n - r) r = n - r;
            long long comb = 1;
            for (int i = 1; i <= r; ++i) {
                comb = comb * (n - r + i) / i;
            }
            ans += comb;
        }
    }
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int WaysToReachStair(int k) {
        long ans = 0;
        for (int x = 0; ; x++) {
            long pow = 1L << x;                     // 2^x
            if (pow - k > x + 1) break;             // cannot satisfy y <= x+1 any more
            if (pow >= k) {
                int y = (int)(pow - k);              // number of down moves
                ans += Combination(x + 1, y);
            }
        }
        return (int)ans;
    }

    private long Combination(int n, int r) {
        if (r < 0 || r > n) return 0;
        if (r > n - r) r = n - r;                  // use smaller side
        long res = 1;
        for (int i = 1; i <= r; i++) {
            res = res * (n - r + i) / i;
        }
        return res;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} k
 * @return {number}
 */
var waysToReachStair = function(k) {
    const nCr = (n, r) => {
        if (r < 0 || r > n) return 0;
        if (r === 0 || r === n) return 1;
        // take advantage of symmetry
        if (r > n - r) r = n - r;
        let res = 1;
        for (let i = 1; i <= r; ++i) {
            res = res * (n - r + i) / i;
        }
        return Math.round(res); // result is integer
    };
    
    let ans = 0;
    for (let x = 0; ; ++x) {
        const pow = Math.pow(2, x);
        if (pow < k) continue;               // need non‑negative y
        const y = pow - k;
        if (y > x + 1) {
            // once diff exceeds allowed positions and pow already >= k,
            // it will only get larger for bigger x.
            if (pow > k) break;
            else continue;
        }
        ans += nCr(x + 1, y);
    }
    return ans;
};
```

## Typescript

```typescript
function waysToReachStair(k: number): number {
    const comb = (n: number, r: number): number => {
        if (r < 0 || r > n) return 0;
        r = Math.min(r, n - r);
        let res = 1;
        for (let i = 1; i <= r; i++) {
            res = res * (n - r + i) / i;
        }
        return Math.round(res);
    };

    let ans = 0;
    // Since k ≤ 1e9, x up to about 31 is sufficient.
    for (let x = 0; x <= 31; x++) {
        const pow = 1 << x; // 2^x
        const y = pow - k;
        if (y < 0) continue;
        if (y > x + 1) continue;
        ans += comb(x + 1, y);
    }
    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $k
     * @return Integer
     */
    function waysToReachStair($k) {
        $ans = 0;
        for ($x = 0; ; $x++) {
            $pow = 1 << $x; // 2^x
            if ($pow > $k + $x + 1) {
                break;
            }
            $y = $pow - $k;
            if ($y >= 0 && $y <= $x + 1) {
                $ans += $this->nCr($x + 1, $y);
            }
        }
        return $ans;
    }

    private function nCr($n, $r) {
        if ($r < 0 || $r > $n) return 0;
        if ($r > $n - $r) $r = $n - $r;
        $res = 1;
        for ($i = 1; $i <= $r; $i++) {
            $res = intdiv($res * ($n - $r + $i), $i);
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    private let MOD: Int64 = 1_000_000_007
    private var fact = [Int64]()
    private var invFact = [Int64]()

    private func modPow(_ base: Int64, _ exp: Int64) -> Int64 {
        var result: Int64 = 1
        var b = base % MOD
        var e = exp
        while e > 0 {
            if e & 1 == 1 {
                result = (result * b) % MOD
            }
            b = (b * b) % MOD
            e >>= 1
        }
        return result
    }

    private func comb(_ n: Int, _ k: Int64) -> Int64 {
        if k < 0 || k > Int64(n) { return 0 }
        let ki = Int(k)
        var res = fact[n]
        res = (res * invFact[ki]) % MOD
        res = (res * invFact[n - ki]) % MOD
        return res
    }

    func waysToReachStair(_ k: Int) -> Int {
        // Precompute factorials up to 64 (enough for constraints)
        let maxN = 64
        fact = Array(repeating: 0, count: maxN + 1)
        invFact = Array(repeating: 0, count: maxN + 1)
        fact[0] = 1
        for i in 1...maxN {
            fact[i] = (fact[i - 1] * Int64(i)) % MOD
        }
        invFact[maxN] = modPow(fact[maxN], MOD - 2)
        if maxN > 0 {
            for i in stride(from: maxN, to: 0, by: -1) {
                invFact[i - 1] = (invFact[i] * Int64(i)) % MOD
            }
        }

        var ans: Int64 = 0
        let K = Int64(k)
        for i in 0...60 {               // enough because 2^60 > 10^18
            let powVal = Int64(1) << i   // 2^i
            if powVal < K { continue }   // need more jumps to reach at least k
            let diff = powVal - K        // number of down moves required
            if diff > Int64(i + 1) { break } // cannot place that many non‑consecutive downs
            ans += comb(i + 1, diff)
            if ans >= MOD { ans -= MOD }
        }
        return Int(ans % MOD)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun waysToReachStair(k: Int): Int {
        var ans = 0L
        val K = k.toLong()
        var x = 0
        while (true) {
            val pow = 1L shl x
            if (pow > K + x + 1) break
            val y = pow - K
            if (y >= 0 && y <= (x + 1).toLong()) {
                ans += comb(x + 1, y.toInt())
            }
            x++
        }
        return ans.toInt()
    }

    private fun comb(n: Int, r: Int): Long {
        var rr = r
        if (rr > n - rr) rr = n - rr
        var res = 1L
        for (i in 1..rr) {
            res = res * (n - rr + i).toLong() / i.toLong()
        }
        return res
    }
}
```

## Dart

```dart
class Solution {
  int waysToReachStair(int k) {
    int ans = 0;
    for (int x = 0; ; ++x) {
      int pow2 = 1 << x;
      if (pow2 > k + x + 1) break;
      int y = pow2 - k;
      if (y >= 0 && y <= x + 1) {
        ans += _combination(x + 1, y);
      }
    }
    return ans;
  }

  int _combination(int n, int r) {
    if (r < 0 || r > n) return 0;
    if (r > n - r) r = n - r;
    int res = 1;
    for (int i = 1; i <= r; ++i) {
      res = res * (n - r + i) ~/ i;
    }
    return res;
  }
}
```

## Golang

```go
func waysToReachStair(k int) int {
    // compute combinations C(n, r)
    nCr := func(n, r int) int {
        if r < 0 || r > n {
            return 0
        }
        if r > n-r {
            r = n - r
        }
        res := 1
        for i := 1; i <= r; i++ {
            res = res * (n - r + i) / i
        }
        return res
    }

    ans := 0
    // x is the number of type‑1 operations performed
    for x := 0; x < 32; x++ { // enough because 2^31 > 1e9
        cur := (1 << (x + 1)) - 1 // position after x jumps without any down moves
        diff := cur - k           // number of required down moves
        if diff >= 0 && diff <= x+1 {
            ans += nCr(x+1, diff)
        }
    }
    return ans
}
```

## Ruby

```ruby
def comb(n, k)
  return 0 if k < 0 || k > n
  k = [k, n - k].min
  result = 1
  (1..k).each do |i|
    result = result * (n - k + i) / i
  end
  result
end

def ways_to_reach_stair(k)
  ans = 0
  (0..60).each do |x|
    pow = 1 << x
    next if pow < k
    y = pow - k
    n = x + 1
    next if y > n
    ans += comb(n, y)
  end
  ans
end
```

## Scala

```scala
object Solution {
  def waysToReachStair(k: Int): Int = {
    var ans: Long = 0L
    var x = 0
    while ((1L << x) - (x + 1) <= k) {
      val pow = 1L << x
      val y = pow - k
      if (y >= 0 && y <= x + 1) {
        ans += nCr(x + 1, y.toInt)
      }
      x += 1
    }
    ans.toInt
  }

  private def nCr(n: Int, r: Int): Long = {
    var res: Long = 1L
    var i = 1
    while (i <= r) {
      res = res * (n - r + i) / i
      i += 1
    }
    res
  }
}
```

## Rust

```rust
impl Solution {
    pub fn ways_to_reach_stair(k: i32) -> i32 {
        let k = k as i64;
        let mut ans: i64 = 0;

        // Since k ≤ 1e9, x up to 31 is enough (2^31 > 2e9)
        for x in 0..=31usize {
            let pow = 1i64 << x; // 2^x
            if pow < k {
                continue;
            }
            let y = pow - k; // number of first‑type operations
            if y as usize > x + 1 {
                continue;
            }

            let n = (x + 1) as i64;
            let r = y as i64;
            // compute C(n, r)
            let mut comb: i64 = 1;
            let rr = std::cmp::min(r, n - r);
            for i in 0..rr {
                comb = comb * (n - i) / (i + 1);
            }
            ans += comb;
        }

        ans as i32
    }
}
```

## Racket

```racket
(define/contract (choose n r)
  (-> exact-integer? exact-integer? exact-integer?)
  (if (< r 0) 0
      (let ((r (min r (- n r))))
        (let loop ((i 0) (res 1))
          (if (= i r)
              res
              (loop (+ i 1) (/ (* res (- n i)) (+ i 1)))))))

(define/contract (ways-to-reach-stair k)
  (-> exact-integer? exact-integer?)
  (let loop ((x 0) (pow 1) (ans 0))
    (cond
      [(> pow k)
       (let ((y (- pow k)))
         (if (> y (+ x 1))
             ans
             (loop (+ x 1) (* pow 2) (+ ans (choose (+ x 1) y)))))]
      [else
       (loop (+ x 1) (* pow 2) ans)])))
```

## Erlang

```erlang
-module(solution).
-export([ways_to_reach_stair/1]).

-spec ways_to_reach_stair(K :: integer()) -> integer().
ways_to_reach_stair(K) ->
    loop(0, K, 0).

loop(X, K, Acc) ->
    Pow = 1 bsl X,
    Diff = Pow - K,
    if
        Diff < 0 ->
            loop(X + 1, K, Acc);
        Diff > X + 1 ->
            Acc;
        true ->
            NewAcc = Acc + comb(X + 1, Diff),
            loop(X + 1, K, NewAcc)
    end.

comb(N, K) when K < 0; K > N -> 0;
comb(N, K) ->
    if
        K > N - K ->
            comb(N, N - K);
        true ->
            lists:foldl(
                fun(I, Acc) ->
                    Acc * (N - K + I) div I
                end,
                1,
                lists:seq(1, K)
            )
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec ways_to_reach_stair(k :: integer) :: integer
  def ways_to_reach_stair(k) when is_integer(k) and k >= 0 do
    max_x = 60

    Enum.reduce(0..max_x, 0, fn x, acc ->
      pow = 1 <<< x

      if pow < k do
        acc
      else
        y = pow - k

        if y <= x + 1 do
          acc + comb(x + 1, y)
        else
          acc
        end
      end
    end)
  end

  defp comb(n, r) when r < 0 or r > n, do: 0

  defp comb(n, r) do
    r = min(r, n - r)

    Enum.reduce(1..r, 1, fn i, acc ->
      div(acc * (n - r + i), i)
    end)
  end
end
```
