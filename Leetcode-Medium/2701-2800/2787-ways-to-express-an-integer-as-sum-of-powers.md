# 2787. Ways to Express an Integer as Sum of Powers

## Cpp

```cpp
class Solution {
public:
    int numberOfWays(int n, int x) {
        const int MOD = 1000000007;
        vector<int> dp(n + 1, 0);
        dp[0] = 1;
        for (int i = 1; ; ++i) {
            long long val = 1;
            for (int k = 0; k < x; ++k) {
                val *= i;
                if (val > n) break;
            }
            if (val > n) break;
            int power = static_cast<int>(val);
            for (int j = n; j >= power; --j) {
                dp[j] += dp[j - power];
                if (dp[j] >= MOD) dp[j] -= MOD;
            }
        }
        return dp[n];
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;

    public int numberOfWays(int n, int x) {
        long[] dp = new long[n + 1];
        dp[0] = 1; // empty set

        for (int i = 1; ; i++) {
            long power = 1;
            for (int k = 0; k < x; k++) {
                power *= i;
                if (power > n) break;
            }
            if (power > n) break;

            int p = (int) power;
            for (int sum = n; sum >= p; sum--) {
                dp[sum] += dp[sum - p];
                if (dp[sum] >= MOD) dp[sum] -= MOD;
            }
        }

        return (int) dp[n];
    }
}
```

## Python

```python
class Solution(object):
    def numberOfWays(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1
        max_base = int(n ** (1.0 / x)) + 1
        for i in range(1, max_base + 1):
            power = i ** x
            if power > n:
                break
            for s in range(n, power - 1, -1):
                dp[s] = (dp[s] + dp[s - power]) % MOD
        return dp[n]
```

## Python3

```python
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10 ** 9 + 7
        # generate all i^x <= n
        powers = []
        i = 1
        while True:
            p = i ** x
            if p > n:
                break
            powers.append(p)
            i += 1

        dp = [0] * (n + 1)
        dp[0] = 1  # empty set

        for p in powers:
            for j in range(n, p - 1, -1):
                dp[j] = (dp[j] + dp[j - p]) % MOD

        return dp[n]
```

## C

```c
#include <stdio.h>

int numberOfWays(int n, int x) {
    const int MOD = 1000000007;
    long long dp[301] = {0};
    dp[0] = 1;

    for (int i = 1; ; ++i) {
        long long p = 1;
        for (int k = 0; k < x; ++k) {
            p *= i;
            if (p > n) break;
        }
        if (p > n) break;

        int power = (int)p;
        for (int j = n; j >= power; --j) {
            dp[j] += dp[j - power];
            if (dp[j] >= MOD) dp[j] -= MOD;
        }
    }

    return (int)(dp[n] % MOD);
}
```

## Csharp

```csharp
public class Solution {
    public int NumberOfWays(int n, int x) {
        const int MOD = 1000000007;
        int[] dp = new int[n + 1];
        dp[0] = 1;

        for (int i = 1; ; i++) {
            long pow = 1;
            for (int k = 0; k < x; k++) {
                pow *= i;
                if (pow > n) break;
            }
            if (pow > n) break;
            int p = (int)pow;

            for (int j = n; j >= p; j--) {
                dp[j] += dp[j - p];
                if (dp[j] >= MOD) dp[j] -= MOD;
            }
        }

        return dp[n];
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} x
 * @return {number}
 */
var numberOfWays = function(n, x) {
    const MOD = 1000000007;
    const dp = new Array(n + 1).fill(0);
    dp[0] = 1; // empty set
    
    const maxI = Math.floor(Math.pow(n, 1 / x));
    for (let i = 1; i <= maxI; i++) {
        const power = Math.pow(i, x);
        for (let sum = n; sum >= power; sum--) {
            dp[sum] += dp[sum - power];
            if (dp[sum] >= MOD) dp[sum] -= MOD;
        }
    }
    
    return dp[n];
};
```

## Typescript

```typescript
function numberOfWays(n: number, x: number): number {
    const MOD = 1000000007;
    const dp = new Array<number>(n + 1).fill(0);
    dp[0] = 1;

    // maximum base whose x-th power does not exceed n
    const maxBase = Math.floor(Math.pow(n, 1 / x));

    for (let i = 1; i <= maxBase; ++i) {
        const pow = Math.pow(i, x);
        if (pow > n) continue;
        for (let sum = n; sum >= pow; --sum) {
            dp[sum] += dp[sum - pow];
            if (dp[sum] >= MOD) dp[sum] -= MOD;
        }
    }

    return dp[n];
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @param Integer $x
     * @return Integer
     */
    function numberOfWays($n, $x) {
        $mod = 1000000007;
        $dp = array_fill(0, $n + 1, 0);
        $dp[0] = 1;

        // maximum base whose x-th power does not exceed n
        $maxI = (int)floor(pow($n, 1.0 / $x));
        for ($i = 1; $i <= $maxI; $i++) {
            // compute i^x as integer
            $powVal = 1;
            for ($k = 0; $k < $x; $k++) {
                $powVal *= $i;
            }
            if ($powVal > $n) continue;

            for ($j = $n; $j >= $powVal; $j--) {
                $dp[$j] = ($dp[$j] + $dp[$j - $powVal]) % $mod;
            }
        }

        return $dp[$n];
    }
}
```

## Swift

```swift
class Solution {
    func numberOfWays(_ n: Int, _ x: Int) -> Int {
        let MOD = 1_000_000_007
        var dp = [Int](repeating: 0, count: n + 1)
        dp[0] = 1
        
        var i = 1
        while true {
            var power = 1
            for _ in 0..<x {
                power *= i
                if power > n { break }
            }
            if power > n { break }
            
            if power <= n {
                for sum in stride(from: n, through: power, by: -1) {
                    let newVal = (dp[sum] + dp[sum - power]) % MOD
                    dp[sum] = newVal
                }
            }
            i += 1
        }
        
        return dp[n]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfWays(n: Int, x: Int): Int {
        val MOD = 1_000_000_007L
        val dp = LongArray(n + 1)
        dp[0] = 1L
        var i = 1
        while (true) {
            var p = 1L
            repeat(x) { p *= i }
            if (p > n) break
            val power = p.toInt()
            for (j in n downTo power) {
                dp[j] = (dp[j] + dp[j - power]) % MOD
            }
            i++
        }
        return dp[n].toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int numberOfWays(int n, int x) {
    List<int> dp = List.filled(n + 1, 0);
    dp[0] = 1;

    for (int i = 1;; ++i) {
      int power = 1;
      bool overflow = false;
      for (int e = 0; e < x; ++e) {
        power *= i;
        if (power > n) {
          overflow = true;
          break;
        }
      }
      if (overflow) break;

      for (int sum = n; sum >= power; --sum) {
        dp[sum] += dp[sum - power];
        if (dp[sum] >= _mod) dp[sum] -= _mod;
      }
    }

    return dp[n];
  }
}
```

## Golang

```go
func numberOfWays(n int, x int) int {
	const MOD = 1000000007
	dp := make([]int, n+1)
	dp[0] = 1

	for i := 1; ; i++ {
		pow := 1
		for k := 0; k < x; k++ {
			pow *= i
			if pow > n {
				break
			}
		}
		if pow > n {
			break
		}
		for j := n; j >= pow; j-- {
			dp[j] += dp[j-pow]
			if dp[j] >= MOD {
				dp[j] -= MOD
			}
		}
	}
	return dp[n]
}
```

## Ruby

```ruby
def number_of_ways(n, x)
  mod = 1_000_000_007
  dp = Array.new(n + 1, 0)
  dp[0] = 1

  i = 1
  while (i ** x) <= n
    pow = i ** x
    j = n
    while j >= pow
      dp[j] += dp[j - pow]
      dp[j] -= mod if dp[j] >= mod
      j -= 1
    end
    i += 1
  end

  dp[n] % mod
end
```

## Scala

```scala
object Solution {
    def numberOfWays(n: Int, x: Int): Int = {
        val MOD = 1000000007L
        val dp = Array.fill[Long](n + 1)(0L)
        dp(0) = 1L

        var i = 1
        while (i <= n) {
            // compute i^x, stop if it exceeds n
            var pow = 1L
            var cnt = 0
            while (cnt < x && pow <= n) {
                pow *= i
                cnt += 1
            }
            if (cnt == x && pow <= n) {
                val p = pow.toInt
                var j = n
                while (j >= p) {
                    dp(j) = (dp(j) + dp(j - p)) % MOD
                    j -= 1
                }
                i += 1
            } else {
                // i^x already exceeds n, larger i will also exceed
                i = n + 1
            }
        }

        dp(n).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_ways(n: i32, x: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n_usize = n as usize;
        let mut dp = vec![0i64; n_usize + 1];
        dp[0] = 1;

        let mut i = 1usize;
        loop {
            // compute i^x
            let mut power = 1usize;
            for _ in 0..x {
                power *= i;
            }
            if power > n_usize {
                break;
            }
            for j in (power..=n_usize).rev() {
                dp[j] = (dp[j] + dp[j - power]) % MOD;
            }
            i += 1;
        }

        dp[n_usize] as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (number-of-ways n x)
  (-> exact-integer? exact-integer? exact-integer?)
  (let ((dp (make-vector (+ n 1) 0)))
    (vector-set! dp 0 1)
    (let loop-i ((i 1))
      (define pow (expt i x))
      (when (<= pow n)
        (for ([j (in-range n (sub1 pow) -1)])
          (let* ((old (vector-ref dp j))
                 (add (vector-ref dp (- j pow)))
                 (new (+ old add)))
            (vector-set! dp j (modulo new MOD))))
        (loop-i (add1 i))))
    (vector-ref dp n)))
```

## Erlang

```erlang
-define(MOD, 1000000007).

-spec number_of_ways(N :: integer(), X :: integer()) -> integer().
number_of_ways(N, X) ->
    Arr0 = array:new(N + 1, {default, 0}),
    Arr1 = array:set(0, 1, Arr0),
    DPArr = process(1, N, X, Arr1),
    array:get(N, DPArr).

process(I, N, X, Arr) ->
    Power = pow_int(I, X),
    if
        Power > N -> Arr;
        true ->
            UpdatedArr = update_dp(Power, N, Arr),
            process(I + 1, N, X, UpdatedArr)
    end.

update_dp(Power, N, Arr) ->
    loop_j(N, Power, Arr).

loop_j(J, Power, Arr) when J < Power ->
    Arr;
loop_j(J, Power, Arr) ->
    ValJ = array:get(J, Arr),
    ValPrev = array:get(J - Power, Arr),
    NewVal = (ValJ + ValPrev) rem ?MOD,
    Arr1 = array:set(J, NewVal, Arr),
    loop_j(J - 1, Power, Arr1).

pow_int(_, 0) -> 1;
pow_int(B, E) when E band 1 =:= 1 ->
    B * pow_int(B * B, E bsr 1);
pow_int(B, E) ->
    pow_int(B * B, E bsr 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_ways(n :: integer, x :: integer) :: integer
  def number_of_ways(n, x) do
    mod = 1_000_000_007

    powers =
      1..n
      |> Enum.take_while(fn i -> :math.pow(i, x) <= n + 0.0 end)
      |> Enum.map(&trunc(:math.pow(&1, x)))

    dp =
      Enum.reduce(powers, %{0 => 1}, fn power, acc_dp ->
        additions =
          acc_dp
          |> Enum.reduce(%{}, fn {sum, cnt}, add_acc ->
            new_sum = sum + power

            if new_sum <= n do
              cur = Map.get(add_acc, new_sum, 0)
              Map.put(add_acc, new_sum, rem(cur + cnt, mod))
            else
              add_acc
            end
          end)

        Map.merge(acc_dp, additions, fn _k, v1, v2 -> rem(v1 + v2, mod) end)
      end)

    Map.get(dp, n, 0)
  end
end
```
