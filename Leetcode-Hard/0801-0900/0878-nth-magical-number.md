# 0878. Nth Magical Number

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int nthMagicalNumber(int n, int a, int b) {
        const long long MOD = 1000000007LL;
        long long g = std::gcd((long long)a, (long long)b);
        long long lcm = (long long)a / g * b;
        long long low = 1, high = (long long)n * min(a, b);
        while (low < high) {
            long long mid = low + (high - low) / 2;
            long long cnt = mid / a + mid / b - mid / lcm;
            if (cnt >= n) high = mid;
            else low = mid + 1;
        }
        return (int)(low % MOD);
    }
};
```

## Java

```java
class Solution {
    public int nthMagicalNumber(int n, int a, int b) {
        long MOD = 1_000_000_007L;
        long left = 1;
        long right = (long)Math.min(a, b) * n; // upper bound
        long lcm = lcm(a, b);
        while (left < right) {
            long mid = left + (right - left) / 2;
            long count = mid / a + mid / b - mid / lcm;
            if (count >= n) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return (int)(left % MOD);
    }

    private long gcd(long x, long y) {
        while (y != 0) {
            long t = x % y;
            x = y;
            y = t;
        }
        return x;
    }

    private long lcm(int a, int b) {
        return ((long)a / gcd(a, b)) * b;
    }
}
```

## Python

```python
class Solution(object):
    def nthMagicalNumber(self, n, a, b):
        """
        :type n: int
        :type a: int
        :type b: int
        :rtype: int
        """
        import math
        MOD = 10**9 + 7
        lcm = a // math.gcd(a, b) * b

        low, high = 1, n * min(a, b)
        while low < high:
            mid = (low + high) // 2
            cnt = mid // a + mid // b - mid // lcm
            if cnt >= n:
                high = mid
            else:
                low = mid + 1
        return low % MOD
```

## Python3

```python
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        import math
        MOD = 10**9 + 7
        lcm = a // math.gcd(a, b) * b

        low, high = 1, n * min(a, b)
        while low < high:
            mid = (low + high) // 2
            cnt = mid // a + mid // b - mid // lcm
            if cnt >= n:
                high = mid
            else:
                low = mid + 1
        return low % MOD
```

## C

```c
#include <stdint.h>

int nthMagicalNumber(int n, int a, int b) {
    const long long MOD = 1000000007LL;
    long long aa = a, bb = b;

    // Compute gcd
    long long x = aa, y = bb;
    while (y) {
        long long t = x % y;
        x = y;
        y = t;
    }
    long long g = x;
    long long lcm = aa / g * bb;

    long long low = 1;
    long long high = (long long)n * (aa < bb ? aa : bb);

    while (low < high) {
        long long mid = low + (high - low) / 2;
        long long cnt = mid / aa + mid / bb - mid / lcm;
        if (cnt >= n)
            high = mid;
        else
            low = mid + 1;
    }

    return (int)(low % MOD);
}
```

## Csharp

```csharp
using System;

public class Solution
{
    public int NthMagicalNumber(int n, int a, int b)
    {
        const long MOD = 1000000007L;
        long g = Gcd(a, b);
        long lcm = (long)a / g * b;

        long low = 1;
        long high = (long)n * Math.Min(a, b);

        while (low < high)
        {
            long mid = low + (high - low) / 2;
            long count = mid / a + mid / b - mid / lcm;

            if (count >= n)
                high = mid;
            else
                low = mid + 1;
        }

        return (int)(low % MOD);
    }

    private long Gcd(long x, long y)
    {
        while (y != 0)
        {
            long tmp = x % y;
            x = y;
            y = tmp;
        }
        return x;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var nthMagicalNumber = function(n, a, b) {
    const MOD = 1_000_000_007;
    
    const gcd = (x, y) => {
        while (y !== 0) {
            const t = x % y;
            x = y;
            y = t;
        }
        return x;
    };
    
    const lcm = a / gcd(a, b) * b; // safe within Number range
    
    let low = 1;
    let high = n * Math.min(a, b); // upper bound
    
    while (low < high) {
        const mid = Math.floor((low + high) / 2);
        const count = Math.floor(mid / a) + Math.floor(mid / b) - Math.floor(mid / lcm);
        if (count >= n) {
            high = mid;
        } else {
            low = mid + 1;
        }
    }
    
    return low % MOD;
};
```

## Typescript

```typescript
function nthMagicalNumber(n: number, a: number, b: number): number {
    const MOD = 1000000007n;
    const bigA = BigInt(a);
    const bigB = BigInt(b);

    function gcd(x: number, y: number): number {
        while (y !== 0) {
            const t = x % y;
            x = y;
            y = t;
        }
        return x;
    }

    const g = gcd(a, b);
    const lcm = (bigA / BigInt(g)) * bigB;

    let low = 1n;
    let high = BigInt(Math.min(a, b)) * BigInt(n);

    while (low < high) {
        const mid = (low + high) >> 1n; // divide by 2
        const count = mid / bigA + mid / bigB - mid / lcm;
        if (count >= BigInt(n)) {
            high = mid;
        } else {
            low = mid + 1n;
        }
    }

    return Number(low % MOD);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $a
     * @param Integer $b
     * @return Integer
     */
    function nthMagicalNumber($n, $a, $b) {
        $mod = 1000000007;
        $gcd = $this->gcd($a, $b);
        $lcm = intdiv($a, $gcd) * $b;

        $low = 1;
        $high = $n * min($a, $b); // upper bound

        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            $count = intdiv($mid, $a) + intdiv($mid, $b) - intdiv($mid, $lcm);
            if ($count >= $n) {
                $high = $mid;
            } else {
                $low = $mid + 1;
            }
        }

        return $low % $mod;
    }

    private function gcd($x, $y) {
        while ($y != 0) {
            $tmp = $x % $y;
            $x = $y;
            $y = $tmp;
        }
        return $x;
    }
}
```

## Swift

```swift
class Solution {
    func nthMagicalNumber(_ n: Int, _ a: Int, _ b: Int) -> Int {
        let MOD = 1_000_000_007
        let a64 = Int64(a)
        let b64 = Int64(b)
        let lcm = a64 / gcd(a64, b64) * b64
        
        var low: Int64 = 1
        var high: Int64 = Int64(n) * min(a64, b64)
        
        while low < high {
            let mid = (low + high) >> 1
            let count = mid / a64 + mid / b64 - mid / lcm
            if count >= Int64(n) {
                high = mid
            } else {
                low = mid + 1
            }
        }
        return Int(low % Int64(MOD))
    }
    
    private func gcd(_ x: Int64, _ y: Int64) -> Int64 {
        var a = x
        var b = y
        while b != 0 {
            let temp = a % b
            a = b
            b = temp
        }
        return a
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun nthMagicalNumber(n: Int, a: Int, b: Int): Int {
        val mod = 1_000_000_007L
        val aa = a.toLong()
        val bb = b.toLong()
        val g = gcd(aa, bb)
        val lcm = aa / g * bb

        var low = 1L
        var high = n.toLong() * minOf(aa, bb)

        while (low < high) {
            val mid = (low + high) / 2
            val cnt = mid / aa + mid / bb - mid / lcm
            if (cnt >= n.toLong()) {
                high = mid
            } else {
                low = mid + 1
            }
        }
        return ((low % mod).toInt())
    }

    private fun gcd(x: Long, y: Long): Long {
        var a = x
        var b = y
        while (b != 0L) {
            val tmp = a % b
            a = b
            b = tmp
        }
        return a
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int nthMagicalNumber(int n, int a, int b) {
    int g = _gcd(a, b);
    int lcm = (a ~/ g) * b;
    int low = 1;
    int high = (a < b ? a : b) * n;

    while (low < high) {
      int mid = low + ((high - low) >> 1);
      int count = mid ~/ a + mid ~/ b - mid ~/ lcm;
      if (count >= n) {
        high = mid;
      } else {
        low = mid + 1;
      }
    }

    return low % _mod;
  }

  int _gcd(int x, int y) {
    while (y != 0) {
      int tmp = x % y;
      x = y;
      y = tmp;
    }
    return x;
  }
}
```

## Golang

```go
func nthMagicalNumber(n int, a int, b int) int {
	const MOD int64 = 1000000007
	// helper to compute gcd
	var gcd func(int64, int64) int64
	gcd = func(x, y int64) int64 {
		for y != 0 {
			x, y = y, x%y
		}
		return x
	}

	ai := int64(a)
	bi := int64(b)
	lcm := ai / gcd(ai, bi) * bi

	low, high := int64(1), int64(n)*min(ai, bi)
	for low < high {
		mid := (low + high) >> 1
		cnt := mid/ai + mid/bi - mid/lcm
		if cnt >= int64(n) {
			high = mid
		} else {
			low = mid + 1
		}
	}
	return int(low % MOD)
}

func min(x, y int64) int64 {
	if x < y {
		return x
	}
	return y
}
```

## Ruby

```ruby
def nth_magical_number(n, a, b)
  mod = 1_000_000_007
  lcm = a / a.gcd(b) * b
  left = 1
  right = n * [a, b].min
  while left < right
    mid = (left + right) / 2
    cnt = mid / a + mid / b - mid / lcm
    if cnt >= n
      right = mid
    else
      left = mid + 1
    end
  end
  left % mod
end
```

## Scala

```scala
object Solution {
    def nthMagicalNumber(n: Int, a: Int, b: Int): Int = {
        val MOD = 1000000007L
        val aa = a.toLong
        val bb = b.toLong
        val g = gcd(aa, bb)
        val lcm = aa / g * bb

        var left = 1L
        var right = n.toLong * math.min(aa, bb)

        while (left < right) {
            val mid = left + (right - left) / 2
            val count = mid / aa + mid / bb - mid / lcm
            if (count >= n) right = mid else left = mid + 1
        }

        ((left % MOD).toInt)
    }

    private def gcd(x: Long, y: Long): Long = {
        var a = x
        var b = y
        while (b != 0) {
            val t = a % b
            a = b
            b = t
        }
        a
    }
}
```

## Rust

```rust
impl Solution {
    pub fn nth_magical_number(n: i32, a: i32, b: i32) -> i32 {
        fn gcd(mut x: i64, mut y: i64) -> i64 {
            while y != 0 {
                let t = x % y;
                x = y;
                y = t;
            }
            x
        }
        const MOD: i64 = 1_000_000_007;
        let n = n as i64;
        let a = a as i64;
        let b = b as i64;
        let g = gcd(a, b);
        let l = a / g * b; // lcm
        let mut low: i64 = 1;
        let mut high: i64 = n * std::cmp::min(a, b);
        while low < high {
            let mid = (low + high) / 2;
            let cnt = mid / a + mid / b - mid / l;
            if cnt >= n {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        (low % MOD) as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (nth-magical-number n a b)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  (let* ([l (lcm a b)]
         [low 1]
         [high (* n (min a b))])
    (let loop ([lo low] [hi high])
      (if (= lo hi)
          (modulo lo MOD)
          (let* ([mid (quotient (+ lo hi) 2)]
                 [cnt (+ (quotient mid a)
                         (quotient mid b)
                         (- (quotient mid l)))])
            (if (>= cnt n)
                (loop lo mid)
                (loop (+ mid 1) hi)))))))
```

## Erlang

```erlang
-module(solution).
-export([nth_magical_number/3]).

-spec nth_magical_number(N :: integer(), A :: integer(), B :: integer()) -> integer().
nth_magical_number(N, A, B) ->
    Mod = 1000000007,
    L = lcm(A, B),
    MinAB = if A < B -> A; true -> B end,
    High0 = N * MinAB,
    binary_search(1, High0, N, A, B, L, Mod).

binary_search(Low, High, N, A, B, LCM, Mod) when Low < High ->
    Mid = (Low + High) div 2,
    Count = Mid div A + Mid div B - Mid div LCM,
    if
        Count >= N -> binary_search(Low, Mid, N, A, B, LCM, Mod);
        true       -> binary_search(Mid + 1, High, N, A, B, LCM, Mod)
    end;
binary_search(Ans, _High, _N, _A, _B, _LCM, Mod) ->
    Ans rem Mod.

lcm(A, B) ->
    (A div gcd(A, B)) * B.

gcd(X, 0) -> X;
gcd(X, Y) -> gcd(Y, X rem Y).
```

## Elixir

```elixir
defmodule Solution do
  @spec nth_magical_number(n :: integer, a :: integer, b :: integer) :: integer
  def nth_magical_number(n, a, b) do
    mod = 1_000_000_007
    lcm = div(a, Integer.gcd(a, b)) * b
    low = 1
    high = n * min(a, b)

    result = binary_search(low, high, n, a, b, lcm)
    rem(result, mod)
  end

  defp binary_search(low, high, n, a, b, lcm) do
    if low < high do
      mid = div(low + high, 2)

      cnt = div(mid, a) + div(mid, b) - div(mid, lcm)

      if cnt >= n do
        binary_search(low, mid, n, a, b, lcm)
      else
        binary_search(mid + 1, high, n, a, b, lcm)
      end
    else
      low
    end
  end
end
```
