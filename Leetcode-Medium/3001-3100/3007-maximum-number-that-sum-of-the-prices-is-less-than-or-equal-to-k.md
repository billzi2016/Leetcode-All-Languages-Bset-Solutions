# 3007. Maximum Number That Sum of the Prices Is Less Than or Equal to K

## Cpp

```cpp
class Solution {
public:
    // count of numbers in [0, n] having bit b (0-indexed) set
    long long countSet(long long n, int b) {
        unsigned long long mask = 1ULL << b;
        unsigned long long cycle = mask << 1;               // 2^(b+1)
        unsigned long long full = (static_cast<unsigned long long>(n) + 1) / cycle;
        unsigned long long res = full * mask;
        unsigned long long rem = (static_cast<unsigned long long>(n) + 1) % cycle;
        if (rem > mask) res += rem - mask;
        return static_cast<long long>(res);
    }
    
    // total accumulated price from 1 to num
    long long totalPrice(long long num, int x) {
        long long total = 0;
        for (int pos = x; ; pos += x) {          // positions are 1‑based
            int b = pos - 1;                     // zero‑based bit index
            if (b >= 63) break;                  // shift would overflow
            unsigned long long mask = 1ULL << b;
            if (mask > static_cast<unsigned long long>(num)) break;
            total += countSet(num, b);
        }
        return total;
    }
    
    long long findMaximumNumber(long long k, int x) {
        long long lo = 0, hi = 4000000000000000000LL; // sufficiently large upper bound
        while (lo < hi) {
            long long mid = lo + (hi - lo + 1) / 2;
            if (totalPrice(mid, x) <= k)
                lo = mid;
            else
                hi = mid - 1;
        }
        return lo;
    }
};
```

## Java

```java
class Solution {
    public long findMaximumNumber(long k, int x) {
        long low = 0;
        long high = 1;
        while (accumulatedPrice(high, x) <= k) {
            if (high > Long.MAX_VALUE / 2) {
                high = Long.MAX_VALUE;
                break;
            }
            high <<= 1;
        }
        while (low < high) {
            long mid = low + (high - low + 1) / 2;
            if (accumulatedPrice(mid, x) <= k) {
                low = mid;
            } else {
                high = mid - 1;
            }
        }
        return low;
    }

    private long accumulatedPrice(long n, int x) {
        if (n <= 0) return 0L;
        long total = 0L;
        for (int mult = 1; ; mult++) {
            int pos = mult * x;          // 1‑based position
            if (pos > 60) break;         // beyond needed bits for long range
            int zeroPos = pos - 1;       // convert to 0‑based
            long block = 1L << zeroPos;  // size of a half cycle
            long cycle = block << 1;     // full cycle length
            long fullCycles = (n + 1) / cycle;
            long cnt = fullCycles * block;
            long remainder = (n + 1) % cycle;
            if (remainder > block) {
                cnt += remainder - block;
            }
            total += cnt;
        }
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def findMaximumNumber(self, k, x):
        """
        :type k: int
        :type x: int
        :rtype: int
        """
        def total_price(n):
            # sum of prices from 1 to n
            if n <= 0:
                return 0
            total = 0
            p = x - 1  # zero‑based bit index
            while (1 << p) <= n:
                cycle_len = 1 << (p + 1)
                full_cycles = (n + 1) // cycle_len
                total += full_cycles * (1 << p)
                rem = (n + 1) % cycle_len
                extra = rem - (1 << p)
                if extra > 0:
                    total += extra
                p += x
            return total

        # find an upper bound where price exceeds k
        lo, hi = 0, 1
        while total_price(hi) <= k:
            hi <<= 1

        # binary search for maximum cheap number
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if total_price(mid) <= k:
                lo = mid
            else:
                hi = mid - 1
        return lo
```

## Python3

```python
class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def accumulated(n: int) -> int:
            total = 0
            b = x - 1  # zero‑based bit index that is a multiple of x (1‑indexed)
            while b < 61:  # enough for n up to ~2^60
                cycle = 1 << (b + 1)
                full = (n + 1) // cycle
                total += full * (1 << b)
                rem = (n + 1) % cycle
                extra = rem - (1 << b)
                if extra > 0:
                    total += extra
                b += x
            return total

        lo, hi = 0, 1
        while accumulated(hi) <= k:
            hi <<= 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if accumulated(mid) <= k:
                lo = mid
            else:
                hi = mid - 1
        return lo
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

static unsigned long long countBit(unsigned long long n, int b) {
    unsigned long long cycle = 1ULL << (b + 1);
    unsigned long long full = (n + 1) / cycle;
    unsigned long long cnt = full * (1ULL << b);
    unsigned long long rem = (n + 1) % cycle;
    if (rem > (1ULL << b)) cnt += rem - (1ULL << b);
    return cnt;
}

static unsigned long long totalPrice(unsigned long long n, int x) {
    unsigned long long sum = 0;
    for (int b = x - 1; b < 63; b += x) {
        if ((1ULL << b) > n && ((n + 1) / (1ULL << (b + 1))) == 0) break;
        sum += countBit(n, b);
    }
    return sum;
}

long long findMaximumNumber(long long k, int x) {
    unsigned long long K = (unsigned long long)k;
    unsigned long long lo = 0, hi = 1;
    while (totalPrice(hi, x) <= K) {
        hi <<= 1;
    }
    while (lo < hi) {
        unsigned long long mid = lo + (hi - lo + 1) / 2;
        if (totalPrice(mid, x) <= K)
            lo = mid;
        else
            hi = mid - 1;
    }
    return (long long)lo;
}
```

## Csharp

```csharp
using System;

public class Solution
{
    public long FindMaximumNumber(long k, int x)
    {
        // Helper to compute accumulated price up to n
        long Accumulated(long n)
        {
            long total = 0;
            for (int m = 1; ; m++)
            {
                int bitIdx = m * x - 1; // zero‑based index
                if (bitIdx >= 63) break; // beyond 64‑bit range

                long cnt = CountOnes(n, bitIdx);
                total += cnt;
                if (total > k) break; // early stop, no need to continue
            }
            return total;
        }

        // Count of numbers in [1, n] having the bit at position idx set (0‑based)
        long CountOnes(long n, int idx)
        {
            if (n <= 0) return 0;
            long blockSize = 1L << (idx + 1);          // length of a full pattern
            long onesPerBlock = 1L << idx;             // number of ones in each full block
            long fullBlocks = (n + 1) / blockSize;
            long remainder = (n + 1) % blockSize;
            long extra = Math.Max(0, remainder - onesPerBlock);
            return fullBlocks * onesPerBlock + extra;
        }

        // Find an upper bound where accumulated price exceeds k
        long hi = 1;
        while (Accumulated(hi) <= k && hi < (long)4e18)
        {
            hi <<= 1;
        }
        long lo = 0;
        while (lo < hi)
        {
            long mid = lo + ((hi - lo + 1) >> 1);
            if (Accumulated(mid) <= k)
                lo = mid;
            else
                hi = mid - 1;
        }
        return lo;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} k
 * @param {number} x
 * @return {number}
 */
var findMaximumNumber = function(k, x) {
    const K = BigInt(k);
    const X = BigInt(x);

    // count of set bits at zero‑based position idx (idx+1 is 1‑based)
    const countOnes = (idx, n) => {
        const cycle = 1n << BigInt(idx + 1);          // length of a full 0/1 cycle
        const half = cycle >> 1n;                     // number of ones in each full cycle
        const total = n + 1n;                         // numbers from 0..n inclusive
        const fullCycles = total / cycle;
        let ones = fullCycles * half;
        const rem = total % cycle;
        if (rem > half) ones += rem - half;
        return ones;
    };

    // accumulated price for all numbers 1..n
    const accumulated = (n) => {
        let sum = 0n;
        // positions that are multiples of x: p = m*x (1‑based), idx = p-1
        for (let m = 1n; ; ++m) {
            const idx = m * X - 1n;   // zero‑based index
            if (idx > 60n) break;     // beyond needed bits (2^61 > 2e18)
            sum += countOnes(Number(idx), n);
            if (sum > K) break;       // early stop
        }
        return sum;
    };

    // find an upper bound
    let low = 0n, high = 1n;
    while (accumulated(high) <= K) {
        high <<= 1n;
    }

    // binary search for greatest n with accumulated(n) <= K
    while (low < high) {
        const mid = (low + high + 1n) >> 1n; // upper middle
        if (accumulated(mid) <= K) {
            low = mid;
        } else {
            high = mid - 1n;
        }
    }

    return Number(low);
};
```

## Typescript

```typescript
function findMaximumNumber(k: number, x: number): number {
    // Helper to compute accumulated price up to n
    const accumulated = (n: number): number => {
        let total = 0;
        for (let pos = x; ; pos += x) {
            const b = pos - 1; // zero‑based bit index
            const half = Math.pow(2, b);          // 2^b
            if (half > n) break;                  // no numbers have this bit set
            const cycle = half * 2;               // 2^(b+1)
            const fullCycles = Math.floor((n + 1) / cycle);
            let cnt = fullCycles * half;
            const remainder = (n + 1) % cycle;
            if (remainder > half) cnt += remainder - half;
            total += cnt;
        }
        return total;
    };

    // Find an upper bound where accumulated price exceeds k
    let low = 0;
    let high = 1;
    while (accumulated(high) <= k && high < Number.MAX_SAFE_INTEGER) {
        high *= 2;
    }
    if (high > Number.MAX_SAFE_INTEGER) high = Number.MAX_SAFE_INTEGER;

    // Binary search for the greatest cheap number
    while (low < high) {
        const mid = Math.floor((low + high + 1) / 2);
        if (accumulated(mid) <= k) {
            low = mid;
        } else {
            high = mid - 1;
        }
    }
    return low;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $k
     * @param Integer $x
     * @return Integer
     */
    function findMaximumNumber($k, $x) {
        // helper to compute accumulated price up to n (inclusive)
        $totalPrice = function(int $n) use ($x, $k): int {
            $sum = 0;
            // positions are 1-indexed; we need multiples of x
            for ($pos = $x; $pos <= 60; $pos += $x) {
                $len = 1 << $pos;               // length of a full cycle (2^pos)
                $half = $len >> 1;              // number of ones in each full cycle at this position
                $fullCycles = intdiv($n + 1, $len);
                $ones = $fullCycles * $half;
                $remainder = ($n + 1) % $len;
                $extra = $remainder - $half;
                if ($extra > 0) {
                    $ones += $extra;
                }
                $sum += $ones;
                // early stop if already exceeds k
                if ($sum > $k) {
                    break;
                }
            }
            return $sum;
        };

        // find an upper bound where totalPrice > k
        $low = 0;
        $high = 1;
        while ($totalPrice($high) <= $k) {
            $low = $high;
            $high <<= 1; // double the high bound
        }

        // binary search for greatest n with totalPrice(n) <= k
        while ($low < $high) {
            $mid = intdiv($low + $high + 1, 2);
            if ($totalPrice($mid) <= $k) {
                $low = $mid;
            } else {
                $high = $mid - 1;
            }
        }

        return $low;
    }
}
```

## Swift

```swift
class Solution {
    func findMaximumNumber(_ k: Int, _ x: Int) -> Int {
        let K = UInt64(k)
        var low: UInt64 = 0
        var high: UInt64 = 1
        
        while totalPrice(high, x) <= K {
            if high > UInt64.max / 2 { // prevent overflow
                high = UInt64.max
                break
            }
            high <<= 1
        }
        
        while low + 1 < high {
            let mid = low + (high - low) / 2
            if totalPrice(mid, x) <= K {
                low = mid
            } else {
                high = mid
            }
        }
        return Int(low)
    }
    
    private func totalPrice(_ n: UInt64, _ x: Int) -> UInt64 {
        if n == 0 { return 0 }
        var sum: UInt64 = 0
        var pos = x // position counting from 1 (LSB)
        while pos <= 63 {
            let period = UInt64(1) << pos          // 2^pos
            let onesPerCycle = period >> 1         // 2^(pos-1)
            let fullCycles = (n + 1) / period
            let remainder = (n + 1) % period
            let extra = remainder > onesPerCycle ? remainder - onesPerCycle : UInt64(0)
            sum += fullCycles * onesPerCycle + extra
            pos += x
        }
        return sum
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findMaximumNumber(k: Long, x: Int): Long {
        fun countSetBits(n: Long, bitIdx: Int): Long {
            val period = 1L shl (bitIdx + 1)
            val fullCycles = (n + 1) / period
            var cnt = fullCycles * (1L shl bitIdx)
            val remainder = (n + 1) % period
            val extra = remainder - (1L shl bitIdx)
            if (extra > 0) cnt += extra
            return cnt
        }

        fun totalPrice(n: Long, xVal: Int): Long {
            var sum = 0L
            var pos = xVal // positions are 1‑based
            while (true) {
                val bitIdx = pos - 1
                if (bitIdx >= 63) break
                val power = 1L shl bitIdx
                if (power > n) break
                sum += countSetBits(n, bitIdx)
                pos += xVal
            }
            return sum
        }

        var lo = 0L
        var hi = 1L
        while (totalPrice(hi, x) <= k && hi < Long.MAX_VALUE / 2) {
            hi = hi shl 1
        }
        if (hi > Long.MAX_VALUE) hi = Long.MAX_VALUE

        while (lo < hi) {
            val mid = lo + (hi - lo + 1) / 2
            if (totalPrice(mid, x) <= k) {
                lo = mid
            } else {
                hi = mid - 1
            }
        }
        return lo
    }
}
```

## Dart

```dart
class Solution {
  int findMaximumNumber(int k, int x) {
    int totalPrice(int n) {
      if (n <= 0) return 0;
      int total = 0;
      for (int b = x - 1; ; b += x) {
        int bitVal = 1 << b; // 2^b
        if (bitVal > n) break;
        int cycleLen = bitVal << 1; // 2^{b+1}
        int fullCycles = (n + 1) ~/ cycleLen;
        int remainder = (n + 1) % cycleLen;
        int ones = fullCycles * bitVal +
            (remainder > bitVal ? remainder - bitVal : 0);
        total += ones;
      }
      return total;
    }

    int low = 0;
    int high = 1;
    while (totalPrice(high) <= k) {
      low = high;
      high <<= 1;
    }
    while (low < high) {
      int mid = (low + high + 1) >> 1;
      if (totalPrice(mid) <= k) {
        low = mid;
      } else {
        high = mid - 1;
      }
    }
    return low;
  }
}
```

## Golang

```go
func findMaximumNumber(k int64, x int) int64 {
	// helper: total accumulated price from 1 to n
	accPrice := func(n int64) int64 {
		if n <= 0 {
			return 0
		}
		var total int64 = 0
		for pos := x - 1; ; pos += x {
			if pos >= 63 { // shift would overflow, and 2^pos > any possible n
				break
			}
			bitVal := int64(1) << uint(pos)
			if bitVal > n {
				break
			}
			cycle := bitVal << 1 // 2^(pos+1)
			fullCycles := (n + 1) / cycle
			ones := fullCycles * bitVal
			rem := (n + 1) % cycle
			extra := rem - bitVal
			if extra > 0 {
				ones += extra
			}
			total += ones
		}
		return total
	}

	// exponential search for upper bound
	lo, hi := int64(0), int64(1)
	for accPrice(hi) <= k {
		hi <<= 1
		if hi < 0 { // overflow guard, shouldn't happen with given constraints
			hi = 1<<62 - 1
			break
		}
	}

	// binary search for greatest n with accumulated price <= k
	for lo < hi {
		mid := (lo + hi + 1) >> 1
		if accPrice(mid) <= k {
			lo = mid
		} else {
			hi = mid - 1
		}
	}
	return lo
}
```

## Ruby

```ruby
def find_maximum_number(k, x)
  # Helper to compute accumulated price up to n
  total_price = lambda do |n|
    return 0 if n <= 0
    sum = 0
    m = 1
    loop do
      p = m * x
      bit = 1 << (p - 1)          # value of the bit at position p
      break if bit > n            # higher bits contribute nothing
      cycle = bit << 1            # length of one full on/off cycle for this bit
      full_cycles = (n + 1) / cycle
      sum += full_cycles * bit    # ones contributed by complete cycles
      remainder = (n + 1) % cycle
      extra = remainder - bit
      sum += extra if extra > 0   # partial cycle contribution
      m += 1
    end
    sum
  end

  lo = 0
  hi = 1
  while total_price.call(hi) <= k
    hi <<= 1
  end

  while lo < hi
    mid = (lo + hi + 1) >> 1
    if total_price.call(mid) <= k
      lo = mid
    else
      hi = mid - 1
    end
  end
  lo
end
```

## Scala

```scala
object Solution {
  def findMaximumNumber(k: Long, x: Int): Long = {
    // compute accumulated price for numbers from 1 to n
    def total(n: Long): Long = {
      var sum = 0L
      var p = x               // position (1-indexed)
      while (p <= 60) {       // bits beyond 60 are irrelevant for given limits
        val b = p - 1         // zero‑based bit index
        val half = 1L << b    // length of consecutive ones in the pattern
        val cycle = half << 1 // total period length
        val fullCycles = (n + 1) / cycle
        var cnt = fullCycles * half
        val rem = (n + 1) % cycle
        if (rem > half) cnt += rem - half
        sum += cnt
        p += x
      }
      sum
    }

    // find an upper bound where total(hi) > k
    var lo = 0L
    var hi = 1L
    while (total(hi) <= k && hi < Long.MaxValue / 2) {
      hi <<= 1
    }

    // binary search for the greatest n with total(n) <= k
    while (lo < hi) {
      val mid = lo + (hi - lo + 1) / 2
      if (total(mid) <= k) lo = mid else hi = mid - 1
    }
    lo
  }
}
```

## Rust

```rust
impl Solution {
    pub fn find_maximum_number(k: i64, x: i32) -> i64 {
        // helper: count of set bits at position `pos` (1-indexed from LSB) in numbers 1..=n
        fn count_ones_at_pos(n: i64, pos: i32) -> i128 {
            if n <= 0 {
                return 0;
            }
            let len = 1i128 << (pos - 1); // length of consecutive ones block
            let cycle = len * 2;          // full cycle length
            let full_cycles = (n as i128) / cycle;
            let mut total = full_cycles * len;
            let rem = (n as i128) % cycle;
            if rem >= len {
                total += rem - len + 1;
            }
            total
        }

        // total accumulated price for numbers 1..=n
        fn total_price(n: i64, x: i32) -> i128 {
            let mut sum: i128 = 0;
            let mut pos = x;
            while (1i128 << (pos - 1)) <= n as i128 {
                sum += count_ones_at_pos(n, pos);
                pos += x;
            }
            sum
        }

        // find an upper bound where total_price > k
        let mut low: i64 = 0;
        let mut high: i64 = 1;
        while total_price(high, x) <= k as i128 {
            if high == i64::MAX {
                break;
            }
            // avoid overflow when doubling
            if high > i64::MAX / 2 {
                high = i64::MAX;
            } else {
                high *= 2;
            }
        }

        // binary search for the greatest n with total_price <= k
        while low < high {
            let mid = low + (high - low + 1) / 2;
            if total_price(mid, x) <= k as i128 {
                low = mid;
            } else {
                high = mid - 1;
            }
        }
        low
    }
}
```

## Racket

```racket
(define/contract (find-maximum-number k x)
  (-> exact-integer? exact-integer? exact-integer?)
  (define (total-price n x)
    (let loop ((m 1) (sum 0))
      (let* ((p (* m x))
             (idx (- p 1)))
        (if (> (arithmetic-shift 1 idx) n)
            sum
            (let* ((len (arithmetic-shift 1 (+ idx 1)))   ; 2^(idx+1)
                   (half (arithmetic-shift 1 idx))       ; 2^idx
                   (full (quotient (+ n 1) len))
                   (rem (remainder (+ n 1) len))
                   (extra (max 0 (- rem half))))
              (loop (+ m 1) (+ sum (+ (* full half) extra)))))))))
  ;; find an upper bound where total-price > k
  (let find-high ((high 1))
    (if (<= (total-price high x) k)
        (find-high (* high 2))
        (let binary-search ((low 0) (hi high))
          (if (= (+ low 1) hi)
              low
              (let ((mid (quotient (+ low hi) 2)))
                (if (<= (total-price mid x) k)
                    (binary-search mid hi)
                    (binary-search low mid))))))))
```
```

## Erlang

```erlang
-spec find_maximum_number(K :: integer(), X :: integer()) -> integer().
find_maximum_number(K, X) ->
    %% Find an upper bound where total price exceeds K
    Upper0 = 1,
    Upper = find_upper(Upper0, K, X),
    binary_search(0, Upper, K, X).

%% Double the upper bound until total_price > K
-spec find_upper(integer(), integer(), integer()) -> integer().
find_upper(Upper, K, X) ->
    case total_price(Upper, X) =< K of
        true -> find_upper(Upper bsl 1, K, X);
        false -> Upper
    end.

%% Binary search for the maximum cheap number
-spec binary_search(integer(), integer(), integer(), integer()) -> integer().
binary_search(Low, High, K, X) when Low < High ->
    Mid = (Low + High + 1) div 2,
    case total_price(Mid, X) =< K of
        true -> binary_search(Mid, High, K, X);
        false -> binary_search(Low, Mid - 1, K, X)
    end;
binary_search(Low, _High, _K, _X) ->
    Low.

%% Compute accumulated price up to N for given X
-spec total_price(integer(), integer()) -> integer().
total_price(N, X) ->
    total_price(N, X, X, 0).

-spec total_price(integer(), integer(), integer(), integer()) -> integer().
total_price(N, X, Pos, Acc) ->
    Half = 1 bsl (Pos - 1),
    case Half =< N of
        true ->
            Block = Half bsl 1,
            FullCycles = N div Block,
            Rem = N rem Block,
            Count = FullCycles * Half + max(0, Rem - Half + 1),
            total_price(N, X, Pos + X, Acc + Count);
        false ->
            Acc
    end.

-spec max(integer(), integer()) -> integer().
max(A, B) when A >= B -> A;
max(_A, B) -> B.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_maximum_number(k :: integer, x :: integer) :: integer
  def find_maximum_number(k, x) do
    high = find_high(k, x, 1)
    binary_search(0, high, k, x)
  end

  # Find an upper bound where total price exceeds k
  defp find_high(k, x, h) do
    if total_price(h, x) <= k do
      find_high(k, x, h * 2)
    else
      h
    end
  end

  # Binary search for the greatest n with total_price(n) <= k
  defp binary_search(lo, hi, k, x) when lo < hi do
    mid = div(lo + hi + 1, 2)

    if total_price(mid, x) <= k do
      binary_search(mid, hi, k, x)
    else
      binary_search(lo, mid - 1, k, x)
    end
  end

  defp binary_search(lo, _hi, _k, _x), do: lo

  # Compute accumulated price for numbers 1..n
  defp total_price(n, x) when n <= 0, do: 0

  defp total_price(n, x) do
    Stream.iterate(x, &(&1 + x))
    |> Enum.reduce_while(0, fn p, acc ->
      bit_val = 1 <<< (p - 1)

      if bit_val > n do
        {:halt, acc}
      else
        period = 1 <<< p
        half = bit_val

        full_cycles = div(n + 1, period)
        remainder = rem(n + 1, period)
        extra = max(0, remainder - half)

        cnt = full_cycles * half + extra
        {:cont, acc + cnt}
      end
    end)
  end
end
```
