# 0629. K Inverse Pairs Array

## Cpp

```cpp
class Solution {
public:
    int kInversePairs(int n, int k) {
        const int MOD = 1000000007;
        vector<int> dp(k + 1, 0), ndp(k + 1, 0);
        dp[0] = 1; // for n = 1
        
        for (int i = 2; i <= n; ++i) {
            long long windowSum = 0;
            for (int j = 0; j <= k; ++j) {
                windowSum += dp[j];
                if (j - i >= 0) windowSum -= dp[j - i];
                windowSum %= MOD;
                if (windowSum < 0) windowSum += MOD;
                ndp[j] = static_cast<int>(windowSum);
            }
            dp.swap(ndp);
        }
        return dp[k];
    }
};
```

## Java

```java
class Solution {
    public int kInversePairs(int n, int k) {
        final int MOD = 1_000_000_007;
        if (k > n * (n - 1) / 2) return 0;
        int[] prev = new int[k + 1];
        int[] cur = new int[k + 1];
        prev[0] = 1;
        for (int i = 1; i <= n; i++) {
            cur[0] = 1;
            for (int j = 1; j <= k; j++) {
                long val = ((long) cur[j - 1] + prev[j]) % MOD;
                if (j >= i) {
                    val = (val - prev[j - i] + MOD) % MOD;
                }
                cur[j] = (int) val;
            }
            int[] tmp = prev;
            prev = cur;
            cur = tmp;
        }
        return prev[k];
    }
}
```

## Python

```python
class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        max_inv = n * (n - 1) // 2
        if k > max_inv:
            return 0

        prev = [0] * (k + 1)
        prev[0] = 1  # empty permutation

        for i in range(1, n + 1):
            cur = [0] * (k + 1)
            cur[0] = 1
            for j in range(1, k + 1):
                val = (cur[j - 1] + prev[j]) % MOD
                if j >= i:
                    val -= prev[j - i]
                cur[j] = val % MOD
            prev = cur

        return prev[k]
```

## Python3

```python
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        if k == 0 or n == 1:
            return 1
        prev = [0] * (k + 1)
        prev[0] = 1
        for i in range(2, n + 1):
            cur = [0] * (k + 1)
            cur[0] = 1
            for j in range(1, k + 1):
                val = (cur[j - 1] + prev[j]) % MOD
                if j >= i:
                    val = (val - prev[j - i]) % MOD
                cur[j] = val
            prev = cur
        return prev[k] % MOD
```

## C

```c
#include <stdlib.h>
#include <string.h>

int kInversePairs(int n, int k) {
    const int MOD = 1000000007;
    if (k > n * (n - 1) / 2) return 0;

    int *prev = (int *)calloc(k + 1, sizeof(int));
    int *cur  = (int *)calloc(k + 1, sizeof(int));
    prev[0] = 1;  // for n = 1

    for (int i = 2; i <= n; ++i) {
        long long sum = 0;
        for (int j = 0; j <= k; ++j) {
            sum += prev[j];
            if (sum >= MOD) sum -= MOD;
            if (j >= i) {
                sum -= prev[j - i];
                if (sum < 0) sum += MOD;
            }
            cur[j] = (int)sum;
        }
        int *tmp = prev;
        prev = cur;
        cur = tmp;
        memset(cur, 0, (k + 1) * sizeof(int));
    }

    int result = prev[k];
    free(prev);
    free(cur);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    private const int MOD = 1000000007;
    public int KInversePairs(int n, int k)
    {
        int[] prev = new int[k + 1];
        prev[0] = 1;

        for (int i = 2; i <= n; ++i)
        {
            int[] cur = new int[k + 1];
            long windowSum = 0;
            for (int j = 0; j <= k; ++j)
            {
                windowSum += prev[j];
                if (j >= i)
                    windowSum -= prev[j - i];

                windowSum %= MOD;
                if (windowSum < 0) windowSum += MOD;

                cur[j] = (int)windowSum;
            }
            prev = cur;
        }

        return prev[k];
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
var kInversePairs = function(n, k) {
    const MOD = 1000000007;
    // Maximum possible inversions for length n
    if (k > (n * (n - 1)) >> 1) return 0;

    let prev = new Array(k + 1).fill(0);
    prev[0] = 1; // empty array has 0 inversions

    for (let i = 1; i <= n; i++) {
        const curr = new Array(k + 1).fill(0);
        curr[0] = 1; // only one way to have 0 inversions
        for (let j = 1; j <= k; j++) {
            let val = (curr[j - 1] + (prev[j] || 0)) % MOD;
            if (j >= i) {
                val = (val - prev[j - i] + MOD) % MOD;
            }
            curr[j] = val;
        }
        prev = curr;
    }

    return prev[k];
};
```

## Typescript

```typescript
function kInversePairs(n: number, k: number): number {
    const MOD = 1000000007;
    if (k > (n * (n - 1)) / 2) return 0;

    let dpPrev = new Array(k + 1).fill(0);
    dpPrev[0] = 1; // base for n = 0

    for (let i = 1; i <= n; i++) {
        const dpCurr = new Array(k + 1).fill(0);
        dpCurr[0] = 1;
        for (let j = 1; j <= k; j++) {
            let val = (dpCurr[j - 1] + dpPrev[j]) % MOD;
            if (j >= i) {
                val = (val - dpPrev[j - i] + MOD) % MOD;
            }
            dpCurr[j] = val;
        }
        dpPrev = dpCurr;
    }

    return dpPrev[k];
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
    function kInversePairs($n, $k) {
        $MOD = 1000000007;
        // If k exceeds maximum possible inversions, answer is 0.
        if ($k > intdiv($n * ($n - 1), 2)) {
            return 0;
        }

        $dpPrev = array_fill(0, $k + 1, 0);
        $dpPrev[0] = 1; // empty permutation

        for ($i = 1; $i <= $n; $i++) {
            $dpCurr = array_fill(0, $k + 1, 0);
            $windowSum = 0;
            for ($j = 0; $j <= $k; $j++) {
                $windowSum = ($windowSum + $dpPrev[$j]) % $MOD;
                if ($j >= $i) {
                    $windowSum = ($windowSum - $dpPrev[$j - $i] + $MOD) % $MOD;
                }
                $dpCurr[$j] = $windowSum;
            }
            $dpPrev = $dpCurr;
        }

        return $dpPrev[$k];
    }
}
```

## Swift

```swift
class Solution {
    func kInversePairs(_ n: Int, _ k: Int) -> Int {
        let MOD = 1_000_000_007
        var dpPrev = [Int](repeating: 0, count: k + 1)
        dpPrev[0] = 1
        
        for num in 1...n {
            var dpCurr = [Int](repeating: 0, count: k + 1)
            var cumulative = 0
            for inv in 0...k {
                cumulative += dpPrev[inv]
                if cumulative >= MOD { cumulative -= MOD }
                if inv >= num {
                    cumulative -= dpPrev[inv - num]
                    if cumulative < 0 { cumulative += MOD }
                }
                dpCurr[inv] = cumulative
            }
            dpPrev = dpCurr
        }
        
        return dpPrev[k]
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val MOD = 1_000_000_007L
    fun kInversePairs(n: Int, k: Int): Int {
        if (k == 0) return 1
        var dpPrev = IntArray(k + 1)
        dpPrev[0] = 1
        for (num in 2..n) {
            val dpCurr = IntArray(k + 1)
            var windowSum = 0L
            for (inv in 0..k) {
                windowSum += dpPrev[inv].toLong()
                if (windowSum >= MOD) windowSum -= MOD
                if (inv >= num) {
                    windowSum -= dpPrev[inv - num].toLong()
                    if (windowSum < 0) windowSum += MOD
                }
                dpCurr[inv] = windowSum.toInt()
            }
            dpPrev = dpCurr
        }
        return dpPrev[k]
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  static const int _mod = 1000000007;

  int kInversePairs(int n, int k) {
    List<int> prev = List.filled(k + 1, 0);
    prev[0] = 1;

    for (int i = 1; i <= n; i++) {
      List<int> cur = List.filled(k + 1, 0);
      int limit = min(k, i * (i - 1) ~/ 2);
      int sum = 0;
      for (int j = 0; j <= limit; j++) {
        sum += prev[j];
        if (sum >= _mod) sum -= _mod;

        if (j - i >= 0) {
          sum -= prev[j - i];
          if (sum < 0) sum += _mod;
        }
        cur[j] = sum;
      }
      prev = cur;
    }

    return prev[k];
  }
}
```

## Golang

```go
func kInversePairs(n int, k int) int {
	const MOD = 1000000007
	dpPrev := make([]int, k+1)
	dpPrev[0] = 1

	for i := 2; i <= n; i++ {
		dpCurr := make([]int, k+1)
		for j := 0; j <= k; j++ {
			val := dpPrev[j]
			if j > 0 {
				val += dpCurr[j-1]
				if val >= MOD {
					val -= MOD
				}
			}
			if j >= i {
				val -= dpPrev[j-i]
				if val < 0 {
					val += MOD
				}
			}
			dpCurr[j] = val
		}
		dpPrev = dpCurr
	}
	return dpPrev[k]
}
```

## Ruby

```ruby
def k_inverse_pairs(n, k)
  mod = 1_000_000_007
  max_inv = n * (n - 1) / 2
  return 0 if k > max_inv

  prev = Array.new(k + 1, 0)
  prev[0] = 1

  (1..n).each do |i|
    cur = Array.new(k + 1, 0)
    cur[0] = 1
    sum = prev[0]

    (1..k).each do |j|
      sum += prev[j]
      sum -= prev[j - i] if j >= i
      sum %= mod
      cur[j] = sum
    end

    prev = cur
  end

  prev[k] % mod
end
```

## Scala

```scala
object Solution {
    private val MOD = 1000000007

    def kInversePairs(n: Int, k: Int): Int = {
        if (k > n * (n - 1) / 2) return 0
        var prev = new Array[Int](k + 1)
        prev(0) = 1
        for (num <- 1 to n) {
            val cur = new Array[Int](k + 1)
            var windowSum: Long = 0L
            for (inv <- 0 to k) {
                windowSum += prev(inv)
                if (windowSum >= MOD) windowSum -= MOD
                if (inv - num >= 0) {
                    windowSum -= prev(inv - num)
                    if (windowSum < 0) windowSum += MOD
                }
                cur(inv) = windowSum.toInt
            }
            prev = cur
        }
        prev(k)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn k_inverse_pairs(n: i32, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = n as usize;
        let k = k as usize;
        // dp for size 1
        let mut dp_prev = vec![0i64; k + 1];
        dp_prev[0] = 1;
        if n == 1 {
            return dp_prev[k] as i32;
        }
        for size in 2..=n {
            let mut prefix = vec![0i64; k + 1];
            prefix[0] = dp_prev[0];
            for j in 1..=k {
                prefix[j] = (prefix[j - 1] + dp_prev[j]) % MOD;
            }
            let mut dp_cur = vec![0i64; k + 1];
            for inv in 0..=k {
                let max_add = if inv >= size - 1 { size - 1 } else { inv };
                // sum of dp_prev[inv - t] for t = 0..max_add
                // using prefix sums:
                // total = prefix[inv] - prefix[inv - max_add - 1] (if exists)
                let sub = if inv > max_add {
                    prefix[inv - max_add - 1]
                } else {
                    0
                };
                dp_cur[inv] = (prefix[inv] + MOD - sub) % MOD;
            }
            dp_prev = dp_cur;
        }
        dp_prev[k] as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (k-inverse-pairs n k)
  (-> exact-integer? exact-integer? exact-integer?)
  (if (> k (quotient (* n (- n 1)) 2))
      0
      (let* ((K k)
             (dpPrev (make-vector (+ K 1) 0))
             (dpCurr (make-vector (+ K 1) 0)))
        (vector-set! dpPrev 0 1)
        (for ([len (in-range 2 (+ n 1))])
          (let ((window-sum 0))
            (for ([inv (in-range 0 (+ K 1))])
              (set! window-sum (+ window-sum (vector-ref dpPrev inv)))
              (when (>= inv len)
                (set! window-sum (- window-sum (vector-ref dpPrev (- inv len)))))
              (vector-set! dpCurr inv (modulo window-sum MOD))))
          (let ((tmp dpPrev))
            (set! dpPrev dpCurr)
            (set! dpCurr tmp)))
        (vector-ref dpPrev K))))
```

## Erlang

```erlang
-module(solution).
-export([k_inverse_pairs/2]).

-define(MOD, 1000000007).

k_inverse_pairs(N, K) ->
    case N of
        0 -> if K =:= 0 -> 1; true -> 0 end;
        1 -> if K =:= 0 -> 1; true -> 0 end;
        _ ->
            MaxInv = N * (N - 1) div 2,
            if K > MaxInv -> 0;
               true ->
                   Prev0 = setelement(1, erlang:make_tuple(K + 1, 0), 1),
                   FinalPrev = loop(2, N, K, Prev0),
                   element(K + 1, FinalPrev)
            end
    end.

loop(CurN, MaxN, K, Prev) when CurN > MaxN ->
    Prev;
loop(CurN, MaxN, K, Prev) ->
    Cur = build_cur_tuple(CurN, K, Prev),
    loop(CurN + 1, MaxN, K, Cur).

build_cur_tuple(Ni, K, Prev) ->
    ListRev = build_cur_list(Ni, K, Prev, 0, 0, []),
    list_to_tuple(lists:reverse(ListRev)).

build_cur_list(_Ni, K, _Prev, _Sum, Index, Acc) when Index > K ->
    Acc;
build_cur_list(Ni, K, Prev, Sum, Index, Acc) ->
    PrevK = element(Index + 1, Prev),
    Sum1 = Sum + PrevK,
    Sum2 = if
        Index >= Ni -> Sum1 - element(Index - Ni + 1, Prev);
        true -> Sum1
    end,
    Val = ((Sum2 rem ?MOD) + ?MOD) rem ?MOD,
    build_cur_list(Ni, K, Prev, Sum2, Index + 1, [Val | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @mod 1_000_000_007

  @spec k_inverse_pairs(n :: integer, k :: integer) :: integer
  def k_inverse_pairs(n, k) do
    max_inv = div(n * (n - 1), 2)

    if k > max_inv do
      0
    else
      prev = :array.new(k + 1, default: 0) |> :array.set(0, 1)

      final_arr =
        Enum.reduce(1..n, prev, fn cur_n, prev_arr ->
          {curr_arr, _} =
            Enum.reduce(0..k, {:array.new(k + 1, default: 0), 0}, fn kk,
                                                                    {carr, sum_acc} ->
              sum = (sum_acc + :array.get(kk, prev_arr)) |> rem(@mod)

              sum =
                if kk >= cur_n do
                  (sum - :array.get(kk - cur_n, prev_arr) + @mod) |> rem(@mod)
                else
                  sum
                end

              carr = :array.set(kk, sum, carr)
              {carr, sum}
            end)

          curr_arr
        end)

      :array.get(k, final_arr)
    end
  end
end
```
