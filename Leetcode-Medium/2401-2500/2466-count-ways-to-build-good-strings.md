# 2466. Count Ways To Build Good Strings

## Cpp

```cpp
class Solution {
public:
    int countGoodStrings(int low, int high, int zero, int one) {
        const int MOD = 1'000'000'007;
        vector<int> dp(high + 1);
        dp[0] = 1;
        for (int i = 1; i <= high; ++i) {
            long long val = 0;
            if (i >= zero) val += dp[i - zero];
            if (i >= one)  val += dp[i - one];
            dp[i] = val % MOD;
        }
        long long ans = 0;
        for (int i = low; i <= high; ++i) {
            ans += dp[i];
        }
        return ans % MOD;
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    
    public int countGoodStrings(int low, int high, int zero, int one) {
        int[] dp = new int[high + 1];
        dp[0] = 1;
        for (int i = 1; i <= high; i++) {
            long ways = 0;
            if (i >= zero) ways += dp[i - zero];
            if (i >= one)  ways += dp[i - one];
            dp[i] = (int)(ways % MOD);
        }
        long ans = 0;
        for (int i = low; i <= high; i++) {
            ans += dp[i];
            if (ans >= MOD) ans -= MOD;
        }
        return (int)(ans % MOD);
    }
}
```

## Python

```python
class Solution(object):
    def countGoodStrings(self, low, high, zero, one):
        """
        :type low: int
        :type high: int
        :type zero: int
        :type one: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1
        for i in range(1, high + 1):
            if i >= zero:
                dp[i] = (dp[i] + dp[i - zero]) % MOD
            if i >= one:
                dp[i] = (dp[i] + dp[i - one]) % MOD
        ans = sum(dp[low:high + 1]) % MOD
        return ans
```

## Python3

```python
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1
        for i in range(1, high + 1):
            if i >= zero:
                dp[i] = (dp[i] + dp[i - zero]) % MOD
            if i >= one:
                dp[i] = (dp[i] + dp[i - one]) % MOD
        return sum(dp[low:high + 1]) % MOD
```

## C

```c
int countGoodStrings(int low, int high, int zero, int one) {
    const int MOD = 1000000007;
    int *dp = (int *)calloc(high + 1, sizeof(int));
    dp[0] = 1;
    for (int i = 1; i <= high; ++i) {
        long long cur = 0;
        if (i >= zero) cur += dp[i - zero];
        if (i >= one)  cur += dp[i - one];
        dp[i] = (int)(cur % MOD);
    }
    long long ans = 0;
    for (int i = low; i <= high; ++i) {
        ans += dp[i];
        if (ans >= MOD) ans -= MOD;
    }
    free(dp);
    return (int)(ans % MOD);
}
```

## Csharp

```csharp
public class Solution {
    private const int MOD = 1000000007;
    public int CountGoodStrings(int low, int high, int zero, int one) {
        int[] dp = new int[high + 1];
        dp[0] = 1;
        for (int i = 1; i <= high; i++) {
            long sum = 0;
            if (i >= zero) sum += dp[i - zero];
            if (i >= one) sum += dp[i - one];
            dp[i] = (int)(sum % MOD);
        }
        long result = 0;
        for (int i = low; i <= high; i++) {
            result += dp[i];
        }
        return (int)(result % MOD);
    }
}
```

## Javascript

```javascript
/**
 * @param {number} low
 * @param {number} high
 * @param {number} zero
 * @param {number} one
 * @return {number}
 */
var countGoodStrings = function(low, high, zero, one) {
    const MOD = 1_000_000_007;
    const dp = new Array(high + 1).fill(0);
    dp[0] = 1;
    for (let len = 1; len <= high; ++len) {
        let val = 0;
        if (len >= zero) {
            val += dp[len - zero];
        }
        if (len >= one) {
            val += dp[len - one];
        }
        dp[len] = val % MOD;
    }
    let ans = 0;
    for (let i = low; i <= high; ++i) {
        ans += dp[i];
        if (ans >= MOD) ans -= MOD;
    }
    return ans;
};
```

## Typescript

```typescript
function countGoodStrings(low: number, high: number, zero: number, one: number): number {
    const MOD = 1_000_000_007;
    const dp: number[] = new Array(high + 1).fill(0);
    dp[0] = 1;
    for (let i = 1; i <= high; i++) {
        let val = 0;
        if (i >= zero) val += dp[i - zero];
        if (i >= one) val += dp[i - one];
        dp[i] = val % MOD;
    }
    let ans = 0;
    for (let i = low; i <= high; i++) {
        ans = (ans + dp[i]) % MOD;
    }
    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $low
     * @param Integer $high
     * @param Integer $zero
     * @param Integer $one
     * @return Integer
     */
    function countGoodStrings($low, $high, $zero, $one) {
        $MOD = 1000000007;
        $dp = array_fill(0, $high + 1, 0);
        $dp[0] = 1;
        for ($i = 1; $i <= $high; $i++) {
            $val = 0;
            if ($i >= $zero) {
                $val += $dp[$i - $zero];
            }
            if ($i >= $one) {
                $val += $dp[$i - $one];
            }
            $dp[$i] = $val % $MOD;
        }
        $ans = 0;
        for ($i = $low; $i <= $high; $i++) {
            $ans = ($ans + $dp[$i]) % $MOD;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countGoodStrings(_ low: Int, _ high: Int, _ zero: Int, _ one: Int) -> Int {
        let MOD = 1_000_000_007
        var dp = [Int](repeating: 0, count: high + 1)
        dp[0] = 1
        if high >= 1 {
            for i in 1...high {
                var ways = 0
                if i >= zero {
                    ways += dp[i - zero]
                }
                if i >= one {
                    ways += dp[i - one]
                }
                if ways >= MOD { ways %= MOD }
                dp[i] = ways
            }
        }
        var ans = 0
        for i in low...high {
            ans += dp[i]
            if ans >= MOD { ans %= MOD }
        }
        return ans % MOD
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countGoodStrings(low: Int, high: Int, zero: Int, one: Int): Int {
        val MOD = 1_000_000_007L
        val dp = LongArray(high + 1)
        dp[0] = 1L
        for (i in 1..high) {
            var cur = 0L
            if (i >= zero) {
                cur += dp[i - zero]
            }
            if (i >= one) {
                cur += dp[i - one]
            }
            dp[i] = cur % MOD
        }
        var ans = 0L
        for (i in low..high) {
            ans += dp[i]
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

  int countGoodStrings(int low, int high, int zero, int one) {
    List<int> dp = List.filled(high + 1, 0);
    dp[0] = 1;
    for (int i = 1; i <= high; i++) {
      if (i >= zero) {
        dp[i] = (dp[i] + dp[i - zero]) % _mod;
      }
      if (i >= one) {
        dp[i] = (dp[i] + dp[i - one]) % _mod;
      }
    }
    int ans = 0;
    for (int i = low; i <= high; i++) {
      ans = (ans + dp[i]) % _mod;
    }
    return ans;
  }
}
```

## Golang

```go
func countGoodStrings(low int, high int, zero int, one int) int {
	const MOD int = 1000000007
	dp := make([]int, high+1)
	dp[0] = 1
	for i := 1; i <= high; i++ {
		if i >= zero {
			dp[i] += dp[i-zero]
			if dp[i] >= MOD {
				dp[i] -= MOD
			}
		}
		if i >= one {
			dp[i] += dp[i-one]
			if dp[i] >= MOD {
				dp[i] -= MOD
			}
		}
	}
	ans := 0
	for i := low; i <= high; i++ {
		ans += dp[i]
		if ans >= MOD {
			ans -= MOD
		}
	}
	return ans
}
```

## Ruby

```ruby
def count_good_strings(low, high, zero, one)
  mod = 1_000_000_007
  dp = Array.new(high + 1, 0)
  dp[0] = 1
  (1..high).each do |i|
    val = 0
    val += dp[i - zero] if i >= zero
    val += dp[i - one] if i >= one
    dp[i] = val % mod
  end
  ans = 0
  low.upto(high) { |i| ans = (ans + dp[i]) % mod }
  ans
end
```

## Scala

```scala
object Solution {
  def countGoodStrings(low: Int, high: Int, zero: Int, one: Int): Int = {
    val MOD = 1000000007L
    val dp = new Array[Long](high + 1)
    dp(0) = 1L
    for (i <- 1 to high) {
      var cur = 0L
      if (i >= zero) cur += dp(i - zero)
      if (i >= one) cur += dp(i - one)
      dp(i) = cur % MOD
    }
    var ans = 0L
    for (i <- low to high) {
      ans += dp(i)
      if (ans >= MOD) ans -= MOD
    }
    ans.toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn count_good_strings(low: i32, high: i32, zero: i32, one: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let low_usize = low as usize;
        let high_usize = high as usize;
        let zero_usize = zero as usize;
        let one_usize = one as usize;

        let mut dp = vec![0i64; high_usize + 1];
        dp[0] = 1;

        for len in 1..=high_usize {
            let mut val = 0i64;
            if len >= zero_usize {
                val += dp[len - zero_usize];
            }
            if len >= one_usize {
                val += dp[len - one_usize];
            }
            dp[len] = val % MOD;
        }

        let mut ans = 0i64;
        for len in low_usize..=high_usize {
            ans += dp[len];
            if ans >= MOD {
                ans -= MOD;
            }
        }

        (ans % MOD) as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (count-good-strings low high zero one)
  (-> exact-integer? exact-integer? exact-integer? exact-integer? exact-integer?)
  (let* ((dp (make-vector (+ high 1) 0)))
    (vector-set! dp 0 1)
    (for ([i (in-range 1 (+ high 1))])
      (let ((val (+ (if (>= i zero) (vector-ref dp (- i zero)) 0)
                    (if (>= i one)  (vector-ref dp (- i one))  0))))
        (vector-set! dp i (modulo val MOD))))
    (let ((ans 0))
      (for ([i (in-range low (+ high 1))])
        (set! ans (modulo (+ ans (vector-ref dp i)) MOD)))
      ans)))
```

## Erlang

```erlang
-module(solution).
-export([count_good_strings/4]).

-define(MOD, 1000000007).

count_good_strings(Low, High, Zero, One) ->
    Arr0 = array:new(High + 1, {default, 0}),
    Arr1 = array:set(0, 1, Arr0),
    FinalArr = fill_dp(1, High, Zero, One, Arr1),
    sum_range(Low, High, FinalArr).

fill_dp(I, Max, _Zero, _One, Arr) when I > Max ->
    Arr;
fill_dp(I, Max, Zero, One, Arr) ->
    Val0 = if I >= Zero -> array:get(I - Zero, Arr); true -> 0 end,
    Val1 = if I >= One -> array:get(I - One, Arr); true -> 0 end,
    Val = (Val0 + Val1) rem ?MOD,
    NewArr = array:set(I, Val, Arr),
    fill_dp(I + 1, Max, Zero, One, NewArr).

sum_range(Low, High, Arr) ->
    sum_range(Low, High, Arr, 0).

sum_range(I, High, _Arr, Acc) when I > High ->
    Acc;
sum_range(I, High, Arr, Acc) ->
    Val = array:get(I, Arr),
    NewAcc = (Acc + Val) rem ?MOD,
    sum_range(I + 1, High, Arr, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @spec count_good_strings(low :: integer, high :: integer, zero :: integer, one :: integer) :: integer
  def count_good_strings(low, high, zero, one) do
    mod = 1_000_000_007

    # Initialize DP array with size high + 1, dp[0] = 1
    dp =
      :array.new(high + 1, default: 0)
      |> :array.set(0, 1)

    # Fill DP values iteratively
    dp_filled =
      Enum.reduce(1..high, dp, fn i, arr ->
        val_zero = if i >= zero, do: :array.get(i - zero, arr), else: 0
        val_one = if i >= one, do: :array.get(i - one, arr), else: 0

        val = rem(val_zero + val_one, mod)
        :array.set(i, val, arr)
      end)

    # Sum results for lengths in [low, high]
    Enum.reduce(low..high, 0, fn i, acc ->
      (acc + :array.get(i, dp_filled)) |> rem(mod)
    end)
  end
end
```
