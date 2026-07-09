# 1201. Ugly Number III

## Cpp

```cpp
class Solution {
public:
    long long gcd_ll(long long x, long long y) {
        while (y) {
            long long t = x % y;
            x = y;
            y = t;
        }
        return x;
    }
    
    long long lcm_ll(long long x, long long y) {
        if (x == 0 || y == 0) return 0;
        long long g = gcd_ll(x, y);
        // Use __int128 to avoid overflow during multiplication
        __int128 mul = (__int128)(x / g) * y;
        return (long long)mul;
    }
    
    long long countUgly(long long x, long long a, long long b, long long c,
                        long long ab, long long bc, long long ac, long long abc) {
        return x / a + x / b + x / c
               - x / ab - x / bc - x / ac
               + x / abc;
    }
    
    int nthUglyNumber(int n, int a, int b, int c) {
        long long A = a, B = b, C = c;
        long long AB = lcm_ll(A, B);
        long long AC = lcm_ll(A, C);
        long long BC = lcm_ll(B, C);
        long long ABC = lcm_ll(AB, C); // lcm of all three
        
        long long low = 1, high = 2000000000LL; // guaranteed upper bound
        while (low < high) {
            long long mid = low + (high - low) / 2;
            if (countUgly(mid, A, B, C, AB, BC, AC, ABC) >= n)
                high = mid;
            else
                low = mid + 1;
        }
        return static_cast<int>(low);
    }
};
```

## Java

```java
class Solution {
    private long gcd(long x, long y) {
        while (y != 0) {
            long t = x % y;
            x = y;
            y = t;
        }
        return x;
    }

    private long lcm(long x, long y) {
        return x / gcd(x, y) * y;
    }

    public int nthUglyNumber(int n, int a, int b, int c) {
        long A = a, B = b, C = c;
        long ab = lcm(A, B);
        long bc = lcm(B, C);
        long ac = lcm(A, C);
        long abc = lcm(ab, C);

        long low = 1, high = 2_000_000_000L;
        while (low < high) {
            long mid = low + (high - low) / 2;
            long count = mid / A + mid / B + mid / C
                       - mid / ab - mid / bc - mid / ac
                       + mid / abc;
            if (count >= n) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return (int) low;
    }
}
```

## Python

```python
class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        from math import gcd

        def lcm(x, y):
            return x // gcd(x, y) * y

        ab = lcm(a, b)
        bc = lcm(b, c)
        ac = lcm(a, c)
        abc = lcm(ab, c)

        def count(x):
            return (x // a + x // b + x // c
                    - x // ab - x // bc - x // ac
                    + x // abc)

        lo, hi = 1, min(a, b, c) * n  # upper bound sufficient
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= n:
                hi = mid
            else:
                lo = mid + 1
        return lo
```

## Python3

```python
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        from math import gcd

        def lcm(x, y):
            return x // gcd(x, y) * y

        ab = lcm(a, b)
        bc = lcm(b, c)
        ac = lcm(a, c)
        abc = lcm(ab, c)

        def count(x: int) -> int:
            return (
                x // a
                + x // b
                + x // c
                - x // ab
                - x // bc
                - x // ac
                + x // abc
            )

        lo, hi = 1, n * min(a, b, c)
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= n:
                hi = mid
            else:
                lo = mid + 1
        return lo
```

## C

```c
int nthUglyNumber(int n, int a, int b, int c) {
    long long A = a, B = b, C = c;
    
    // Greatest common divisor
    long long gcd(long long x, long long y) {
        while (y) {
            long long t = x % y;
            x = y;
            y = t;
        }
        return x;
    }
    
    // Least common multiple
    long long lcm(long long x, long long y) {
        return x / gcd(x, y) * y;
    }
    
    long long ab = lcm(A, B);
    long long bc = lcm(B, C);
    long long ac = lcm(A, C);
    long long abc = lcm(ab, C);
    
    auto count = [&](long long x) -> long long {
        return x / A + x / B + x / C
               - x / ab - x / bc - x / ac
               + x / abc;
    };
    
    long long low = 1, high = 2000000000LL; // guaranteed upper bound
    while (low < high) {
        long long mid = low + (high - low) / 2;
        if (count(mid) >= n)
            high = mid;
        else
            low = mid + 1;
    }
    return (int)low;
}
```

## Csharp

```csharp
public class Solution {
    public int NthUglyNumber(int n, int a, int b, int c) {
        long A = a, B = b, C = c;
        long ab = Lcm(A, B);
        long ac = Lcm(A, C);
        long bc = Lcm(B, C);
        long abc = Lcm(ab, C);
        long low = 1, high = 2000000000L; // guaranteed upper bound
        while (low < high) {
            long mid = low + (high - low) / 2;
            if (Count(mid, A, B, C, ab, ac, bc, abc) >= n)
                high = mid;
            else
                low = mid + 1;
        }
        return (int)low;
    }

    private long Count(long x, long a, long b, long c,
                       long ab, long ac, long bc, long abc) {
        return x / a + x / b + x / c - x / ab - x / ac - x / bc + x / abc;
    }

    private long Gcd(long x, long y) {
        while (y != 0) {
            long t = x % y;
            x = y;
            y = t;
        }
        return x;
    }

    private long Lcm(long x, long y) {
        return x / Gcd(x, y) * y;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @return {number}
 */
var nthUglyNumber = function(n, a, b, c) {
    const A = BigInt(a), B = BigInt(b), C = BigInt(c);
    
    const gcd = (x, y) => {
        while (y !== 0n) {
            const t = x % y;
            x = y;
            y = t;
        }
        return x;
    };
    
    const lcm = (x, y) => (x / gcd(x, y)) * y;
    
    const AB = lcm(A, B);
    const AC = lcm(A, C);
    const BC = lcm(B, C);
    const ABC = lcm(AB, C);
    
    const count = (limit) => {
        const m = BigInt(limit);
        return Number(
            m / A + m / B + m / C
            - m / AB - m / AC - m / BC
            + m / ABC
        );
    };
    
    let low = 1, high = 2000000000; // upper bound given by constraints
    while (low < high) {
        const mid = Math.floor((low + high) / 2);
        if (count(mid) >= n) {
            high = mid;
        } else {
            low = mid + 1;
        }
    }
    return low;
};
```

## Typescript

```typescript
function nthUglyNumber(n: number, a: number, b: number, c: number): number {
    const gcd = (x: number, y: number): number => {
        while (y !== 0) {
            const t = x % y;
            x = y;
            y = t;
        }
        return x;
    };
    const lcm = (x: number, y: number): number => {
        const g = gcd(x, y);
        // use BigInt to avoid overflow
        const res = (BigInt(x) / BigInt(g)) * BigInt(y);
        // if result exceeds Number safe range, it will be large enough that k / lcm == 0 for our k <= 2e9
        return Number(res);
    };
    
    const lcmAB = lcm(a, b);
    const lcmAC = lcm(a, c);
    const lcmBC = lcm(b, c);
    const lcmABC = lcm(lcmAB, c);
    
    const count = (k: number): number => {
        const cntA = Math.floor(k / a);
        const cntB = Math.floor(k / b);
        const cntC = Math.floor(k / c);
        const cntAB = Math.floor(k / lcmAB);
        const cntAC = Math.floor(k / lcmAC);
        const cntBC = Math.floor(k / lcmBC);
        const cntABC = Math.floor(k / lcmABC);
        return cntA + cntB + cntC - cntAB - cntAC - cntBC + cntABC;
    };
    
    let low = 1, high = 2_000_000_000; // given guarantee
    while (low < high) {
        const mid = Math.floor((low + high) / 2);
        if (count(mid) >= n) {
            high = mid;
        } else {
            low = mid + 1;
        }
    }
    return low;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $a
     * @param Integer $b
     * @param Integer $c
     * @return Integer
     */
    function nthUglyNumber($n, $a, $b, $c) {
        // helper functions
        $gcd = function ($x, $y) {
            while ($y != 0) {
                $tmp = $x % $y;
                $x = $y;
                $y = $tmp;
            }
            return $x;
        };

        $lcm = function ($x, $y) use ($gcd) {
            return intdiv($x, $gcd($x, $y)) * $y;
        };

        // precompute lcms for inclusion-exclusion
        $ab   = $lcm($a, $b);
        $ac   = $lcm($a, $c);
        $bc   = $lcm($b, $c);
        $abc  = $lcm($ab, $c); // lcm of a,b,c

        // count ugly numbers <= x
        $countUgly = function ($x) use ($a, $b, $c, $ab, $ac, $bc, $abc) {
            return intdiv($x, $a) + intdiv($x, $b) + intdiv($x, $c)
                 - intdiv($x, $ab) - intdiv($x, $ac) - intdiv($x, $bc)
                 + intdiv($x, $abc);
        };

        $low = 1;
        $high = 2000000000; // problem guarantees answer <= 2*10^9

        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            if ($countUgly($mid) >= $n) {
                $high = $mid;
            } else {
                $low = $mid + 1;
            }
        }

        return $low;
    }
}
```

## Swift

```swift
class Solution {
    func nthUglyNumber(_ n: Int, _ a: Int, _ b: Int, _ c: Int) -> Int {
        let A = Int64(a)
        let B = Int64(b)
        let C = Int64(c)
        
        func gcd(_ x: Int64, _ y: Int64) -> Int64 {
            var xx = x
            var yy = y
            while yy != 0 {
                let temp = xx % yy
                xx = yy
                yy = temp
            }
            return xx
        }
        
        func lcm(_ x: Int64, _ y: Int64) -> Int64 {
            return x / gcd(x, y) * y
        }
        
        let ab = lcm(A, B)
        let bc = lcm(B, C)
        let ac = lcm(A, C)
        let abc = lcm(ab, C)
        
        func count(_ x: Int64) -> Int64 {
            return x / A + x / B + x / C - x / ab - x / bc - x / ac + x / abc
        }
        
        var low: Int64 = 1
        var high: Int64 = 2_000_000_000
        
        while low < high {
            let mid = (low + high) / 2
            if count(mid) >= Int64(n) {
                high = mid
            } else {
                low = mid + 1
            }
        }
        
        return Int(low)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun nthUglyNumber(n: Int, a: Int, b: Int, c: Int): Int {
        val A = a.toLong()
        val B = b.toLong()
        val C = c.toLong()

        val lcmAB = lcm(A, B)
        val lcmAC = lcm(A, C)
        val lcmBC = lcm(B, C)
        val lcmABC = lcm(lcmAB, C)

        fun count(x: Long): Long {
            return x / A + x / B + x / C -
                    x / lcmAB - x / lcmAC - x / lcmBC +
                    x / lcmABC
        }

        var low = 1L
        var high = 2_000_000_000L
        while (low < high) {
            val mid = low + (high - low) / 2
            if (count(mid) >= n.toLong()) {
                high = mid
            } else {
                low = mid + 1
            }
        }
        return low.toInt()
    }

    private fun gcd(x: Long, y: Long): Long {
        var a = x
        var b = y
        while (b != 0L) {
            val t = a % b
            a = b
            b = t
        }
        return a
    }

    private fun lcm(x: Long, y: Long): Long {
        return x / gcd(x, y) * y
    }
}
```

## Dart

```dart
class Solution {
  int nthUglyNumber(int n, int a, int b, int c) {
    int _gcd(int x, int y) {
      while (y != 0) {
        int t = x % y;
        x = y;
        y = t;
      }
      return x;
    }

    int _lcm(int x, int y) => x ~/ _gcd(x, y) * y;

    final lcmAB = _lcm(a, b);
    final lcmAC = _lcm(a, c);
    final lcmBC = _lcm(b, c);
    final lcmABC = _lcm(lcmAB, c);

    int count(int x) {
      return x ~/ a + x ~/ b + x ~/ c
          - x ~/ lcmAB - x ~/ lcmAC - x ~/ lcmBC
          + x ~/ lcmABC;
    }

    int left = 1, right = 2000000000; // guaranteed upper bound
    while (left < right) {
      int mid = left + ((right - left) >> 1);
      if (count(mid) >= n) {
        right = mid;
      } else {
        left = mid + 1;
      }
    }
    return left;
  }
}
```

## Golang

```go
func nthUglyNumber(n int, a int, b int, c int) int {
	A := int64(a)
	B := int64(b)
	C := int64(c)

	lcmAB := lcm(A, B)
	lcmBC := lcm(B, C)
	lcmAC := lcm(A, C)
	lcmABC := lcm(lcmAB, C)

	count := func(x int64) int64 {
		return x/A + x/B + x/C - x/lcmAB - x/lcmBC - x/lcmAC + x/lcmABC
	}

	low, high := int64(1), int64(2000000000)
	for low < high {
		mid := (low + high) / 2
		if count(mid) >= int64(n) {
			high = mid
		} else {
			low = mid + 1
		}
	}
	return int(low)
}

func gcd(x, y int64) int64 {
	for y != 0 {
		x, y = y, x%y
	}
	return x
}

func lcm(x, y int64) int64 {
	return x / gcd(x, y) * y
}
```

## Ruby

```ruby
def nth_ugly_number(n, a, b, c)
  l_ab = a.lcm(b)
  l_ac = a.lcm(c)
  l_bc = b.lcm(c)
  l_abc = l_ab.lcm(c)

  count = ->(x) {
    x / a + x / b + x / c - x / l_ab - x / l_ac - x / l_bc + x / l_abc
  }

  left = 1
  right = 2_000_000_000
  while left < right
    mid = (left + right) / 2
    if count.call(mid) >= n
      right = mid
    else
      left = mid + 1
    end
  end
  left
end
```

## Scala

```scala
object Solution {
    def nthUglyNumber(n: Int, a: Int, b: Int, c: Int): Int = {
        val la = a.toLong
        val lb = b.toLong
        val lc = c.toLong

        def gcd(x: Long, y: Long): Long = {
            var xx = x
            var yy = y
            while (yy != 0) {
                val tmp = xx % yy
                xx = yy
                yy = tmp
            }
            xx
        }

        def lcm(x: Long, y: Long): Long = x / gcd(x, y) * y

        val ab = lcm(la, lb)
        val bc = lcm(lb, lc)
        val ac = lcm(la, lc)
        val abc = lcm(ab, lc)

        def count(limit: Long): Long = {
            limit / la + limit / lb + limit / lc -
            limit / ab - limit / bc - limit / ac +
            limit / abc
        }

        var left: Long = 1L
        var right: Long = 2000000000L // guaranteed upper bound

        while (left < right) {
            val mid = left + (right - left) / 2
            if (count(mid) >= n) right = mid
            else left = mid + 1
        }
        left.toInt
    }
}
```

## Rust

```rust
fn gcd(mut x: u64, mut y: u64) -> u64 {
    while y != 0 {
        let t = x % y;
        x = y;
        y = t;
    }
    x
}

fn lcm(x: u64, y: u64) -> u64 {
    if x == 0 || y == 0 {
        return 0;
    }
    x / gcd(x, y) * y
}

impl Solution {
    pub fn nth_ugly_number(n: i32, a: i32, b: i32, c: i32) -> i32 {
        let n = n as i64;
        let a = a as i64;
        let b = b as i64;
        let c = c as i64;

        let ab = lcm(a as u64, b as u64) as i64;
        let ac = lcm(a as u64, c as u64) as i64;
        let bc = lcm(b as u64, c as u64) as i64;
        let abc = lcm(ab as u64, c as u64) as i64;

        let mut left: i64 = 1;
        let mut right: i64 = 2_000_000_000; // guaranteed upper bound

        while left < right {
            let mid = left + (right - left) / 2;
            let count = mid / a + mid / b + mid / c
                - mid / ab - mid / ac - mid / bc
                + mid / abc;

            if count >= n {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        left as i32
    }
}
```

## Racket

```racket
(define/contract (nth-ugly-number n a b c)
  (-> exact-integer? exact-integer? exact-integer? exact-integer? exact-integer?)
  (letrec ((gcd (lambda (x y) (if (= y 0) x (gcd y (remainder x y)))))
           (lcm (lambda (x y) (/ (* x y) (gcd x y))))
           (ab   (lcm a b))
           (ac   (lcm a c))
           (bc   (lcm b c))
           (abc  (lcm ab c))
           (cnt  (lambda (x)
                   (+ (quotient x a)
                      (quotient x b)
                      (quotient x c)
                      (- (quotient x ab) (quotient x ac) (quotient x bc))
                      (quotient x abc))))
           (search (lambda (low high)
                     (if (= low high)
                         low
                         (let ((mid (quotient (+ low high) 2)))
                           (if (>= (cnt mid) n)
                               (search low mid)
                               (search (+ mid 1) high)))))))
    (search 1 (* 2 1000000000))))
```

## Erlang

```erlang
-module(solution).
-export([nth_ugly_number/4]).

-spec nth_ugly_number(N :: integer(), A :: integer(), B :: integer(), C :: integer()) -> integer().
nth_ugly_number(N, A, B, C) ->
    LAB = lcm(A, B),
    LBC = lcm(B, C),
    LCA = lcm(C, A),
    LABC = lcm(LAB, C),
    Low = 1,
    High = 2000000000,
    binary_search(N, Low, High, A, B, C, LAB, LBC, LCA, LABC).

binary_search(N, Low, High, A, B, C, LAB, LBC, LCA, LABC) when Low < High ->
    Mid = (Low + High) div 2,
    Count = count_ugly(Mid, A, B, C, LAB, LBC, LCA, LABC),
    if
        Count >= N -> binary_search(N, Low, Mid, A, B, C, LAB, LBC, LCA, LABC);
        true       -> binary_search(N, Mid + 1, High, A, B, C, LAB, LBC, LCA, LABC)
    end;
binary_search(_, Low, _, _, _, _, _, _, _, _) ->
    Low.

count_ugly(K, A, B, C, LAB, LBC, LCA, LABC) ->
    (K div A) + (K div B) + (K div C)
    - (K div LAB) - (K div LBC) - (K div LCA)
    + (K div LABC).

gcd(X, 0) -> X;
gcd(X, Y) -> gcd(Y, X rem Y).

lcm(X, Y) ->
    X div gcd(X, Y) * Y.
```

## Elixir

```elixir
defmodule Solution do
  @spec nth_ugly_number(integer, integer, integer, integer) :: integer
  def nth_ugly_number(n, a, b, c) do
    lcm_ab = lcm(a, b)
    lcm_ac = lcm(a, c)
    lcm_bc = lcm(b, c)
    lcm_abc = lcm(lcm_ab, c)

    count = fn x ->
      div(x, a) + div(x, b) + div(x, c) -
        div(x, lcm_ab) - div(x, lcm_ac) - div(x, lcm_bc) +
        div(x, lcm_abc)
    end

    binary_search(1, 2_000_000_000, n, count)
  end

  defp binary_search(low, high, n, count_fun) do
    if low < high do
      mid = div(low + high, 2)

      if count_fun.(mid) >= n do
        binary_search(low, mid, n, count_fun)
      else
        binary_search(mid + 1, high, n, count_fun)
      end
    else
      low
    end
  end

  defp lcm(x, y) do
    div(x * y, Integer.gcd(x, y))
  end
end
```
