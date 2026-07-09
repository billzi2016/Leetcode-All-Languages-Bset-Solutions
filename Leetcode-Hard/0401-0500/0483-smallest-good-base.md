# 0483. Smallest Good Base

## Cpp

```cpp
class Solution {
public:
    string smallestGoodBase(string n) {
        unsigned long long N = stoull(n);
        int maxL = 0;
        // maximum length when base is 2: N = 2^L - 1 => L <= log2(N+1)
        while ((1ULL << maxL) <= N + 1 && maxL < 64) ++maxL;
        --maxL; // adjust because loop exits after exceeding
        
        for (int L = maxL; L >= 2; --L) {
            unsigned long long low = 2;
            unsigned long long high = pow((long double)N, 1.0L / (L - 1)) + 1;
            if (high < 2) high = 2;
            while (low <= high) {
                unsigned long long mid = low + (high - low) / 2;
                __int128 cur = 1;
                __int128 sum = 1;
                bool overflow = false;
                for (int i = 1; i < L; ++i) {
                    cur *= (__int128)mid;
                    if (cur > (__int128)N) { overflow = true; break; }
                    sum += cur;
                    if (sum > (__int128)N) { overflow = true; break; }
                }
                if (!overflow && sum == (__int128)N) {
                    return to_string(mid);
                }
                if (overflow || sum > (__int128)N) {
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            }
        }
        // fallback: base N-1 gives representation "11"
        return to_string(N - 1);
    }
};
```

## Java

```java
class Solution {
    public String smallestGoodBase(String n) {
        long N = Long.parseLong(n);
        int maxM = (int) (Math.log(N) / Math.log(2));
        for (int m = maxM; m >= 2; m--) {
            long low = 2;
            long high = (long) Math.pow(N, 1.0 / m) + 1;
            while (low <= high) {
                long mid = low + (high - low) / 2;
                long sum = 1;
                long cur = 1;
                boolean overflow = false;
                for (int i = 0; i < m; i++) {
                    if (cur > N / mid) { // multiplication would exceed N
                        overflow = true;
                        break;
                    }
                    cur *= mid;
                    sum += cur;
                    if (sum > N) {
                        overflow = true;
                        break;
                    }
                }
                if (!overflow && sum == N) {
                    return Long.toString(mid);
                } else if (overflow || sum > N) {
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            }
        }
        // If no base found, the answer is N-1 (representation "11")
        return Long.toString(N - 1);
    }
}
```

## Python

```python
import math

class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        N = int(n)
        max_m = int(math.log2(N))  # maximum possible exponent (length-1)

        for m in range(max_m, 1, -1):  # try longer lengths first
            low, high = 2, int(N ** (1.0 / m)) + 1
            while low <= high:
                k = (low + high) // 2
                total = 1
                term = 1
                for _ in range(m):
                    term *= k
                    total += term
                    if total > N:
                        break
                if total == N:
                    return str(k)
                elif total < N:
                    low = k + 1
                else:
                    high = k - 1

        # fallback: representation "11" in base N-1
        return str(N - 1)
```

## Python3

```python
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        import math
        N = int(n)
        max_m = int(math.log2(N))  # maximum exponent (len-1)

        for m in range(max_m, 1, -1):
            low, high = 2, int(N ** (1.0 / m)) + 1
            while low <= high:
                k = (low + high) // 2
                total, cur = 1, 1
                for _ in range(m):
                    cur *= k
                    total += cur
                    if total > N:
                        break
                if total == N:
                    return str(k)
                if total < N:
                    low = k + 1
                else:
                    high = k - 1

        return str(N - 1)
```

## C

```c
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <string.h>

char* smallestGoodBase(char* n) {
    unsigned long long N = strtoull(n, NULL, 10);
    
    // Try lengths from large to small
    for (int m = 64; m >= 2; --m) {
        double approx = pow((double)N, 1.0 / (m - 1));
        unsigned long long low = 2;
        unsigned long long high = (unsigned long long)(approx) + 1;
        if (high < low) continue;
        
        while (low <= high) {
            unsigned long long mid = low + (high - low) / 2;
            __int128 sum = 1;
            __int128 term = 1;
            for (int i = 1; i < m; ++i) {
                term *= (__int128)mid;
                if (term > (__int128)N) { sum = (__int128)N + 1; break; }
                sum += term;
                if (sum > (__int128)N) break;
            }
            
            if (sum == (__int128)N) {
                char* res = (char*)malloc(32);
                sprintf(res, "%llu", mid);
                return res;
            } else if (sum < (__int128)N) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
    }
    
    // Fallback: base N-1 gives representation "11"
    char* res = (char*)malloc(32);
    sprintf(res, "%llu", N - 1);
    return res;
}
```

## Csharp

```csharp
using System;
using System.Numerics;

public class Solution {
    public string SmallestGoodBase(string n) {
        BigInteger N = BigInteger.Parse(n);
        // Maximum possible length of representation (m+1) is about log2(N)
        for (int m = 60; m >= 1; m--) { // m is number of exponents after the leading 1
            long low = 2;
            double approx = Math.Pow((double)N, 1.0 / m);
            long high = (long)approx + 1;
            if (high < 2) continue;

            while (low <= high) {
                long mid = low + (high - low) / 2;
                BigInteger sum = 1;
                BigInteger cur = 1;
                bool exceeded = false;

                for (int i = 0; i < m; i++) {
                    cur *= mid;
                    sum += cur;
                    if (sum > N) { exceeded = true; break; }
                }

                if (!exceeded && sum == N) {
                    return mid.ToString();
                }

                if (exceeded || sum > N) {
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            }
        }
        // If no base found, the answer is n-1
        return (N - 1).ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} n
 * @return {string}
 */
var smallestGoodBase = function(n) {
    const N = BigInt(n);
    
    // compute maximum possible length L (number of 1's)
    let maxLen = 0;
    let tmp = N + 1n;               // because 2^L - 1 <= N  => 2^L <= N+1
    while (tmp > 1n) {
        tmp >>= 1n;
        maxLen++;
    }
    
    // try lengths from large to small
    for (let L = maxLen; L >= 2; L--) {
        let low = 2n, high = N;
        while (low <= high) {
            const mid = (low + high) >> 1n;
            const cmp = compareSum(mid, L, N);
            if (cmp === 0) return mid.toString();          // found exact base
            else if (cmp < 0) low = mid + 1n;               // sum too small
            else high = mid - 1n;                           // sum too large
        }
    }
    
    // fallback: base N-1 gives representation "11"
    return (N - 1n).toString();
};

/**
 * Compare the geometric series sum_{i=0}^{L-1} k^i with target N.
 * @param {bigint} k base candidate
 * @param {number} L length of representation (>=2)
 * @param {bigint} N target number
 * @return {number} 0 if equal, -1 if sum < N, 1 if sum > N
 */
function compareSum(k, L, N) {
    let sum = 1n;
    let term = 1n;
    for (let i = 1; i < L; i++) {
        term *= k;
        if (term > N) return 1;          // exceeds target
        sum += term;
        if (sum > N) return 1;           // exceeds target
    }
    if (sum === N) return 0;
    return -1;
}
```

## Typescript

```typescript
function smallestGoodBase(n: string): string {
    const N = BigInt(n);

    // compute max possible length L (number of ones)
    let maxL = 0;
    let temp = N;
    while (temp > 0n) {
        temp >>= 1n; // divide by 2
        maxL++;
    }

    // compare sum_{i=0}^{L-1} k^i with N
    const compareSum = (k: bigint, L: number): number => {
        let sum = 0n;
        let term = 1n;
        for (let i = 0; i < L; i++) {
            sum += term;
            if (sum > N) return 1; // greater than N
            term *= k;
        }
        if (sum === N) return 0;
        return -1; // less than N
    };

    for (let L = maxL; L >= 2; L--) {
        let low = 2n;
        let high = N; // safe upper bound

        while (low <= high) {
            const mid = (low + high) >> 1n;
            const cmp = compareSum(mid, L);
            if (cmp === 0) {
                return mid.toString();
            } else if (cmp < 0) {
                low = mid + 1n;
            } else {
                high = mid - 1n;
            }
        }
    }

    // fallback: base N-1 always works (representation "11")
    return (N - 1n).toString();
}
```

## Php

```php
class Solution {

    /**
     * @param String $n
     * @return String
     */
    function smallestGoodBase($n) {
        $N = intval($n);
        // maximum possible length of representation (all 1's)
        $maxLen = (int)floor(log($N) / log(2)) + 1;
        for ($len = $maxLen; $len >= 2; $len--) {
            $low = 2;
            // upper bound for base: k^{len-1} <= N
            $high = (int)pow($N, 1.0 / ($len - 1)) + 1;
            if ($high < 2) $high = 2;
            while ($low <= $high) {
                $mid = intdiv($low + $high, 2);
                // compute sum = 1 + k + k^2 + ... + k^{len-1}
                $sum = 0;
                $term = 1;
                for ($i = 0; $i < $len; $i++) {
                    $sum += $term;
                    if ($sum > $N) break;
                    // avoid overflow, stop multiplying if term already exceeds N
                    if ($mid > 1 && $term > intdiv($N, $mid)) {
                        $term = $N + 1; // force sum to exceed N in next iteration
                    } else {
                        $term *= $mid;
                    }
                }
                if ($sum == $N) {
                    return (string)$mid;
                } elseif ($sum < $N) {
                    $low = $mid + 1;
                } else {
                    $high = $mid - 1;
                }
            }
        }
        // fallback: base N-1 yields "11"
        return (string)($N - 1);
    }
}
```

## Swift

```swift
class Solution {
    func smallestGoodBase(_ n: String) -> String {
        let N = UInt64(n)!
        // maximum possible exponent (m) where representation has m+1 ones
        var maxM = 0
        var temp = N + 1
        while temp > 1 {
            temp >>= 1
            maxM += 1
        }
        for m in stride(from: maxM, through: 1, by: -1) {
            let approx = pow(Double(N), 1.0 / Double(m))
            var low: UInt64 = 2
            var high: UInt64 = UInt64(approx) + 1
            if high < 2 { continue }
            while low <= high {
                let mid = (low + high) / 2
                let cmp = compareSum(mid, m, N)
                if cmp == 0 {
                    return String(mid)
                } else if cmp < 0 {
                    low = mid + 1
                } else {
                    high = mid - 1
                }
            }
        }
        // fallback: base n-1 always works (representation "11")
        return String(N - 1)
    }

    // compare sum_{i=0}^{m} k^i with n
    // returns -1 if sum < n, 0 if equal, 1 if greater
    private func compareSum(_ k: UInt64, _ m: Int, _ n: UInt64) -> Int {
        var sum: UInt64 = 1
        var term: UInt64 = 1
        for _ in 0..<m {
            // check overflow for term * k
            if term > n / k { return 1 }
            term *= k
            // check overflow for sum + term
            if sum > n - term { return 1 }
            sum += term
        }
        if sum == n { return 0 }
        return sum < n ? -1 : 1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun smallestGoodBase(n: String): String {
        val num = n.toLong()
        // maximum possible length of representation (all ones) is floor(log2(num+1))
        val maxLen = Math.floor(Math.log((num + 1).toDouble()) / Math.log(2.0)).toInt()
        for (len in maxLen downTo 2) {
            val base = findBase(num, len)
            if (base != -1L) return base.toString()
        }
        // fallback: representation "11" in base num-1
        return (num - 1).toString()
    }

    private fun findBase(n: Long, length: Int): Long {
        var low = 2L
        // upper bound for base is n^(1/(length-1))
        val highApprox = Math.pow(n.toDouble(), 1.0 / (length - 1)).toLong() + 1
        var high = if (highApprox > n) n else highApprox
        while (low <= high) {
            val mid = low + (high - low) / 2
            when (compare(mid, length, n)) {
                0 -> return mid
                -1 -> low = mid + 1
                1 -> high = mid - 1
            }
        }
        return -1L
    }

    // returns -1 if sum < n, 0 if equal, 1 if sum > n (or overflow)
    private fun compare(k: Long, length: Int, n: Long): Int {
        var sum = 0L
        var term = 1L
        for (i in 0 until length) {
            // check addition overflow beyond n
            if (sum > n - term) return 1
            sum += term
            if (i == length - 1) break
            // check multiplication overflow; if term*k would exceed n, the final sum will exceed n
            if (term > n / k) return 1
            term *= k
        }
        return when {
            sum < n -> -1
            sum == n -> 0
            else -> 1
        }
    }
}
```

## Dart

```dart
import 'dart:math' as math;

class Solution {
  String smallestGoodBase(String nStr) {
    int n = int.parse(nStr);
    int maxLen = (math.log(n) / math.log(2)).floor() + 1;
    for (int m = maxLen; m >= 2; --m) {
      int low = 2;
      int high = (math.pow(n.toDouble(), 1.0 / (m - 1))).floor() + 1;
      if (high < low) continue;
      while (low <= high) {
        int mid = low + ((high - low) >> 1);
        int cmp = _compareSum(mid, m, n);
        if (cmp == 0) return mid.toString();
        if (cmp < 0) {
          low = mid + 1;
        } else {
          high = mid - 1;
        }
      }
    }
    return (n - 1).toString();
  }

  int _compareSum(int k, int m, int n) {
    int sum = 1;
    int term = 1;
    for (int i = 1; i < m; ++i) {
      if (term > n ~/ k) return 1;
      term *= k;
      if (sum > n - term) return 1;
      sum += term;
    }
    if (sum == n) return 0;
    return sum < n ? -1 : 1;
  }
}
```

## Golang

```go
package main

import (
	"math"
	"strconv"
)

func smallestGoodBase(n string) string {
	N, _ := strconv.ParseUint(n, 10, 64)

	// maximum possible length of all-ones representation (base 2)
	maxLen := 0
	for tmp := N; tmp > 0; tmp >>= 1 {
		maxLen++
	}

	// try lengths from longest to shortest
	for m := maxLen; m >= 2; m-- {
		low := uint64(2)
		highFloat := math.Pow(float64(N), 1.0/float64(m-1))
		high := uint64(highFloat) + 1
		if high < low {
			continue
		}
		for low <= high {
			mid := (low + high) / 2
			cmp := compareSum(mid, m, N)
			if cmp == 0 {
				return strconv.FormatUint(mid, 10)
			} else if cmp > 0 { // sum < N
				low = mid + 1
			} else { // sum > N
				high = mid - 1
			}
		}
	}

	// fallback: base n-1 gives representation "11"
	return strconv.FormatUint(N-1, 10)
}

// compareSum returns:
//   0 if 1 + k + ... + k^{m-1} == n
//   1 if the sum < n
//  -1 if the sum > n (or overflow beyond n)
func compareSum(k uint64, m int, n uint64) int {
	var sum uint64 = 1
	var term uint64 = 1
	for i := 0; i < m-1; i++ {
		if term > n/k {
			return -1
		}
		term *= k
		if sum > n-term {
			return -1
		}
		sum += term
	}
	if sum == n {
		return 0
	}
	if sum < n {
		return 1
	}
	return -1
}
```

## Ruby

```ruby
def smallest_good_base(n)
  num = n.to_i
  max_len = Math.log2(num).to_i + 1

  max_len.downto(2) do |len|
    low = 2
    high = (num ** (1.0 / (len - 1))).floor
    next if high < low

    while low <= high
      mid = (low + high) / 2
      sum = 1
      term = 1
      (len - 1).times do
        term *= mid
        sum += term
        break if sum > num
      end

      if sum == num
        return mid.to_s
      elsif sum < num
        low = mid + 1
      else
        high = mid - 1
      end
    end
  end

  (num - 1).to_s
end
```

## Scala

```scala
object Solution {
    def smallestGoodBase(n: String): String = {
        val N = BigInt(n)
        // maximum possible length of representation (number of 1's)
        val maxLen = (Math.log(N.toDouble + 1) / Math.log(2)).toInt
        for (len <- maxLen to 2 by -1) {
            var low: Long = 2L
            var high: Long = (Math.pow(N.toDouble, 1.0 / (len - 1)) + 1e-10).toLong + 1
            while (low <= high) {
                val mid = (low + high) >>> 1
                val k = BigInt(mid)
                // sum = (k^len - 1) / (k - 1)
                val pow = k.pow(len)
                val sum = (pow - 1) / (k - 1)
                if (sum == N) {
                    return mid.toString
                } else if (sum < N) {
                    low = mid + 1
                } else {
                    high = mid - 1
                }
            }
        }
        (N - 1).toString
    }
}
```

## Rust

```rust
impl Solution {
    pub fn smallest_good_base(n: String) -> String {
        let n_val: u128 = n.parse().unwrap();
        // maximum possible exponent (m) when base = 2
        let max_m = 64; // enough for n up to 10^18
        for m in (1..=max_m).rev() {
            // upper bound for k using floating point approximation
            let mf = m as f64;
            let high_est = (n_val as f64).powf(1.0 / mf) as u128 + 1;
            if high_est < 2 {
                continue;
            }
            let mut low: u128 = 2;
            let mut high: u128 = high_est;
            while low <= high {
                let mid = (low + high) / 2;
                // compute sum = 1 + k + k^2 + ... + k^m, stop early if exceeds n_val
                let mut term = 1u128;
                let mut sum = 1u128;
                for _ in 0..m {
                    if term > n_val / mid {
                        sum = n_val + 1; // overflow or exceed limit
                        break;
                    }
                    term *= mid;
                    if sum > n_val - term {
                        sum = n_val + 1;
                        break;
                    }
                    sum += term;
                }
                if sum == n_val {
                    return mid.to_string();
                } else if sum < n_val {
                    low = mid + 1;
                } else {
                    if mid == 0 { break; }
                    high = mid - 1;
                }
            }
        }
        // fallback: base n-1 always works (representation "11")
        (n_val - 1).to_string()
    }
}
```

## Racket

```racket
(define/contract (smallest-good-base n)
  (-> string? string?)
  (let* ((N (string->number n))
         (max-m (exact-floor (log N 2))))
    (define (compare-sum k m N)
      (let loop ((i 0) (term 1) (sum 1))
        (if (= i m)
            (cond [(= sum N) 0]
                  [(< sum N) -1]
                  [else 1])
            (let ((new-term (* term k)))
              (let ((new-sum (+ sum new-term)))
                (if (> new-sum N)
                    1
                    (loop (add1 i) new-term new-sum)))))))
    (define (search m low high)
      (let recur ((l low) (h high))
        (if (> l h)
            #f
            (let* ((mid (quotient (+ l h) 2))
                   (cmp (compare-sum mid m N)))
              (cond [(= cmp 0) mid]
                    [(< cmp 0) (recur (add1 mid) h)]
                    [else (recur l (sub1 mid))])))))
    (let loop-m ((m max-m))
      (if (< m 2)
          (number->string (- N 1))
          (let* ((high (max 2 (exact-floor (expt N (/ 1.0 m)))))
                 (candidate (search m 2 high)))
            (if candidate
                (number->string candidate)
                (loop-m (sub1 m))))))))
```

## Erlang

```erlang
-spec smallest_good_base(N :: unicode:unicode_binary()) -> unicode:unicode_binary().
smallest_good_base(N) ->
    NInt = binary_to_integer(N),
    MaxM = trunc(math:log(NInt) / math:log(2)),
    case find_base(NInt, MaxM) of
        undefined -> integer_to_binary(NInt - 1);
        K -> integer_to_binary(K)
    end.

find_base(_N, 0) ->
    undefined;
find_base(N, M) ->
    Low = 2,
    High0 = trunc(math:pow(N, 1.0 / M)),
    High = if High0 < 2 -> 2; true -> High0 end,
    case binary_search(N, M, Low, High) of
        {ok, K} -> K;
        not_found -> find_base(N, M - 1)
    end.

binary_search(_N, _M, L, H) when L > H ->
    not_found;
binary_search(N, M, L, H) ->
    Mid = (L + H) div 2,
    case geometric_sum(Mid, M, N) of
        equal -> {ok, Mid};
        less -> binary_search(N, M, Mid + 1, H);
        greater -> binary_search(N, M, L, Mid - 1)
    end.

geometric_sum(K, M, Limit) ->
    geometric_sum_loop(K, M, 0, 1, Limit).

geometric_sum_loop(_K, -1, Sum, _Term, Limit) ->
    if
        Sum == Limit -> equal;
        Sum < Limit -> less;
        true -> greater
    end;
geometric_sum_loop(K, I, Sum, Term, Limit) ->
    NewSum = Sum + Term,
    if
        NewSum > Limit -> greater;
        true ->
            NewTerm = Term * K,
            geometric_sum_loop(K, I - 1, NewSum, NewTerm, Limit)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec smallest_good_base(n :: String.t) :: String.t
  def smallest_good_base(n) do
    n_int = String.to_integer(n)
    max_m = :math.log2(n_int) |> trunc()

    result =
      Enum.reduce_while(max_m..2, nil, fn m, _acc ->
        low = 2
        high = integer_root(n_int, m)

        case binary_search(n_int, m, low, high) do
          nil -> {:cont, nil}
          k -> {:halt, Integer.to_string(k)}
        end
      end)

    result || Integer.to_string(n_int - 1)
  end

  defp integer_root(n, m) do
    approx = :math.pow(n, 1.0 / m) |> trunc()

    cond do
      pow_le?(approx + 1, m, n) -> approx + 1
      not pow_le?(approx, m, n) -> dec_root(approx, n, m)
      true -> approx
    end
  end

  defp dec_root(val, n, m) when val > 0 do
    if pow_le?(val, m, n), do: val, else: dec_root(val - 1, n, m)
  end

  defp pow_le?(base, exp, limit) do
    pow_le_rec(base, exp, limit, 1)
  end

  defp pow_le_rec(_base, 0, _limit, _acc), do: true

  defp pow_le_rec(base, exp, limit, acc) do
    new = acc * base

    if new > limit do
      false
    else
      pow_le_rec(base, exp - 1, limit, new)
    end
  end

  defp binary_search(_n, _m, low, high) when low > high, do: nil

  defp binary_search(n, m, low, high) do
    mid = div(low + high, 2)

    case compute_sum(mid, m, n) do
      {:ok, sum} ->
        cond do
          sum == n -> mid
          sum < n -> binary_search(n, m, mid + 1, high)
          true -> binary_search(n, m, low, mid - 1)
        end

      :greater ->
        binary_search(n, m, low, mid - 1)
    end
  end

  defp compute_sum(k, m, n) do
    do_compute_sum(k, m, n, 1, 1)
  end

  defp do_compute_sum(_k, 0, _n, sum, _term), do: {:ok, sum}

  defp do_compute_sum(k, remaining, n, sum, term) do
    new_term = term * k
    new_sum = sum + new_term

    if new_sum > n do
      :greater
    else
      do_compute_sum(k, remaining - 1, n, new_sum, new_term)
    end
  end
end
```
