# 2930. Number of Strings Which Can Be Rearranged to Contain Substring

## Cpp

```cpp
class Solution {
public:
    static const int MOD = 1000000007;
    
    long long modPow(long long a, long long e) {
        long long res = 1 % MOD;
        a %= MOD;
        while (e > 0) {
            if (e & 1) res = res * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return res;
    }
    
    int stringCount(int n) {
        long long p26 = modPow(26, n);
        long long p25 = modPow(25, n);
        long long p24 = modPow(24, n);
        long long p23 = modPow(23, n);
        
        long long p25_n1 = (n == 0) ? 0 : modPow(25, n - 1);
        long long p24_n1 = (n == 0) ? 0 : modPow(24, n - 1);
        long long p23_n1 = (n == 0) ? 0 : modPow(23, n - 1);
        
        // A: no 'l'
        long long A = p25;
        // B: no 't'
        long long B = p25;
        // C: at most one 'e' -> 0 e or 1 e
        long long C = (p25 + (long long)n * p25_n1) % MOD;
        
        // AB: no 'l', no 't'
        long long AB = p24;
        // AC: no 'l', at most one 'e'
        long long AC = (p24 + (long long)n * p24_n1) % MOD;
        // BC: no 't', at most one 'e'
        long long BC = AC; // same as AC
        
        // ABC: no 'l', no 't', at most one 'e'
        long long ABC = (p23 + (long long)n * p23_n1) % MOD;
        
        long long ans = p26;
        ans = (ans - A - B - C) % MOD;
        ans = (ans + AB + AC + BC) % MOD;
        ans = (ans - ABC) % MOD;
        if (ans < 0) ans += MOD;
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    private static final long MOD = 1_000_000_007L;

    private long powMod(long base, int exp) {
        long result = 1;
        long b = base % MOD;
        int e = exp;
        while (e > 0) {
            if ((e & 1) == 1) {
                result = (result * b) % MOD;
            }
            b = (b * b) % MOD;
            e >>= 1;
        }
        return result;
    }

    public int stringCount(int n) {
        long p26 = powMod(26, n);
        long p25 = powMod(25, n);
        long p24 = powMod(24, n);
        long p23 = powMod(23, n);

        long p25_1 = powMod(25, n - 1);
        long p24_1 = powMod(24, n - 1);
        long p23_1 = powMod(23, n - 1);

        long nn = n % MOD;

        long term = (3 * p25) % MOD;
        term = (term + nn * p25_1) % MOD;

        long sub = (3 * p24) % MOD;
        sub = (sub + ((2 * nn) % MOD) * p24_1) % MOD;

        long add = (p23 + nn * p23_1) % MOD;

        long bad = (term - sub + MOD) % MOD;
        bad = (bad + add) % MOD;

        long ans = (p26 - bad + MOD) % MOD;
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def stringCount(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7

        pow26_n = pow(26, n, MOD)
        pow25_n = pow(25, n, MOD)
        pow24_n = pow(24, n, MOD)
        pow23_n = pow(23, n, MOD)

        # powers for n-1 (n >= 1 by constraints)
        pow25_nm1 = pow(25, n - 1, MOD)
        pow24_nm1 = pow(24, n - 1, MOD)
        pow23_nm1 = pow(23, n - 1, MOD)

        # sets
        no_l = pow25_n                       # A
        no_t = pow25_n                       # B (same as A)
        no_e_atmost1 = (pow25_n + n * pow25_nm1) % MOD   # C

        ab = pow24_n                         # A ∩ B
        ac = (pow24_n + n * pow24_nm1) % MOD  # A ∩ C
        bc = ac                               # B ∩ C (symmetry)

        abc = (pow23_n + n * pow23_nm1) % MOD  # A ∩ B ∩ C

        # inclusion-exclusion
        bad = (no_l + no_t + no_e_atmost1) % MOD
        good_pairs = (ab + ac + bc) % MOD

        ans = (pow26_n - bad + good_pairs - abc) % MOD
        return ans
```

## Python3

```python
class Solution:
    def stringCount(self, n: int) -> int:
        MOD = 10**9 + 7

        pow26_n = pow(26, n, MOD)
        pow25_n = pow(25, n, MOD)
        pow24_n = pow(24, n, MOD)
        pow23_n = pow(23, n, MOD)

        # when n == 1, exponent n-1 is 0, pow(x,0)=1
        pow25_nm1 = pow(25, n - 1, MOD) if n > 0 else 0
        pow24_nm1 = pow(24, n - 1, MOD) if n > 0 else 0
        pow23_nm1 = pow(23, n - 1, MOD) if n > 0 else 0

        A = pow25_n                     # no 'l'
        B = pow25_n                     # no 't'
        C = (pow25_n + n * pow25_nm1) % MOD   # at most one 'e'

        AB = pow24_n                    # no 'l' and no 't'
        AC = (pow24_n + n * pow24_nm1) % MOD  # no 'l', at most one 'e'
        BC = AC                         # symmetric

        ABC = (pow23_n + n * pow23_nm1) % MOD # no 'l','t', at most one 'e'

        ans = (pow26_n - A - B - C + AB + AC + BC - ABC) % MOD
        return ans
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

static const long long MOD = 1000000007LL;

static long long modPow(long long a, int e) {
    long long res = 1;
    a %= MOD;
    while (e > 0) {
        if (e & 1) res = (res * a) % MOD;
        a = (a * a) % MOD;
        e >>= 1;
    }
    return res;
}

int stringCount(int n) {
    long long pow26 = modPow(26, n);
    long long pow25 = modPow(25, n);
    long long pow24 = modPow(24, n);
    long long pow23 = modPow(23, n);

    long long pow25_n1 = (n >= 1) ? modPow(25, n - 1) : 0;
    long long pow24_n1 = (n >= 1) ? modPow(24, n - 1) : 0;
    long long pow23_n1 = (n >= 1) ? modPow(23, n - 1) : 0;

    long long termC   = (pow25 + (long long)n * pow25_n1) % MOD;          // |C|
    long long termAC  = (pow24 + (long long)n * pow24_n1) % MOD;          // |A∩C|
    long long termBC  = termAC;                                          // |B∩C| same as A∩C
    long long termABC = (pow23 + (long long)n * pow23_n1) % MOD;          // |A∩B∩C|

    long long ans = pow26;

    // subtract |A| + |B| + |C|
    long long sub = (2LL * pow25) % MOD;
    sub = (sub + termC) % MOD;
    ans = (ans - sub + MOD) % MOD;

    // add |A∩B| + |A∩C| + |B∩C|
    long long add = pow24;          // |A∩B|
    add = (add + termAC) % MOD;
    add = (add + termBC) % MOD;
    ans = (ans + add) % MOD;

    // subtract |A∩B∩C|
    ans = (ans - termABC + MOD) % MOD;

    return (int)ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    private const long MOD = 1000000007L;
    
    private long PowMod(long baseVal, int exp) {
        long result = 1L;
        long b = baseVal % MOD;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                result = (result * b) % MOD;
            }
            b = (b * b) % MOD;
            exp >>= 1;
        }
        return result;
    }
    
    public int StringCount(int n) {
        long p26 = PowMod(26, n);
        long p25 = PowMod(25, n);
        long p24 = PowMod(24, n);
        long p23 = PowMod(23, n);
        
        long p25_1 = n > 0 ? PowMod(25, n - 1) : 0;
        long p24_1 = n > 0 ? PowMod(24, n - 1) : 0;
        long p23_1 = n > 0 ? PowMod(23, n - 1) : 0;
        
        long termA = (3L * p25) % MOD;
        termA = (termA + (n * p25_1) % MOD) % MOD; // |A|+|B|+|C|
        
        long termB = (3L * p24) % MOD;
        termB = (termB + ((2L * n) % MOD) * p24_1 % MOD) % MOD; // |AB|+|AC|+|BC|
        
        long termC = (p23 + (n * p23_1) % MOD) % MOD; // |ABC|
        
        long ans = p26;
        ans = (ans - termA + MOD) % MOD;
        ans = (ans + termB) % MOD;
        ans = (ans - termC + MOD) % MOD;
        
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
var stringCount = function(n) {
    const MOD = 1000000007n;
    const nBig = BigInt(n);
    
    const modPow = (base, exp) => {
        let b = BigInt(base) % MOD;
        let e = BigInt(exp);
        let res = 1n;
        while (e > 0n) {
            if (e & 1n) res = (res * b) % MOD;
            b = (b * b) % MOD;
            e >>= 1n;
        }
        return res;
    };
    
    const pow26 = modPow(26, n);
    const pow25 = modPow(25, n);
    const pow24 = modPow(24, n);
    const pow23 = modPow(23, n);
    
    const pow25_n1 = n > 0 ? modPow(25, n - 1) : 0n;
    const pow24_n1 = n > 0 ? modPow(24, n - 1) : 0n;
    const pow23_n1 = n > 0 ? modPow(23, n - 1) : 0n;
    
    // |A|: at most 1 'e'
    const A = (pow25 + nBig * pow25_n1) % MOD;
    // |B| and |C|
    const B = pow25;
    const C = pow25;
    
    // |AB| and |AC|: no 'l'/'t' and at most 1 'e'
    const AB = (pow24 + nBig * pow24_n1) % MOD;
    const AC = AB; // same value
    // |BC|: no 'l' and no 't'
    const BC = pow24;
    
    // |ABC|: no 'l','t' and at most 1 'e'
    const ABC = (pow23 + nBig * pow23_n1) % MOD;
    
    const sumA = (A + B + C) % MOD;
    const sumAB = (AB + AC + BC) % MOD; // AB+AC+BC
    
    let ans = (pow26 - sumA + sumAB - ABC) % MOD;
    if (ans < 0n) ans += MOD;
    return Number(ans);
};
```

## Typescript

```typescript
function stringCount(n: number): number {
    const MOD = 1000000007n;
    const nBig = BigInt(n);
    const modPow = (base: bigint, exp: number): bigint => {
        let result = 1n;
        let b = base % MOD;
        let e = BigInt(exp);
        while (e > 0n) {
            if ((e & 1n) === 1n) result = (result * b) % MOD;
            b = (b * b) % MOD;
            e >>= 1n;
        }
        return result;
    };

    const p26 = modPow(26n, n);
    const p25 = modPow(25n, n);
    const p24 = modPow(24n, n);
    const p23 = modPow(23n, n);

    const pow25_n1 = n > 0 ? modPow(25n, n - 1) : 0n;
    const pow24_n1 = n > 0 ? modPow(24n, n - 1) : 0n;
    const pow23_n1 = n > 0 ? modPow(23n, n - 1) : 0n;

    const termA = (p25 + nBig * pow25_n1) % MOD;               // A: e <= 1
    const termAB = (p24 + nBig * pow24_n1) % MOD;              // AB: no l, e <= 1
    const termAC = termAB;                                    // same as AB (no t)
    const termABC = (p23 + nBig * pow23_n1) % MOD;             // ABC: no l, no t, e <= 1

    let ans = p26;
    // subtract A, B, C
    ans = (ans - (termA + p25 + p25) % MOD + MOD) % MOD;
    // add intersections AB, AC, BC
    const addIntersections = (termAB + termAC + p24) % MOD;
    ans = (ans + addIntersections) % MOD;
    // subtract ABC
    ans = (ans - termABC + MOD) % MOD;

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
    function stringCount($n) {
        $MOD = 1000000007;

        // fast exponentiation modulo MOD
        $modPow = function($base, $exp) use ($MOD) {
            $result = 1;
            $base %= $MOD;
            while ($exp > 0) {
                if ($exp & 1) {
                    $result = ($result * $base) % $MOD;
                }
                $base = ($base * $base) % $MOD;
                $exp >>= 1;
            }
            return $result;
        };

        // precompute needed powers
        $pow26   = $modPow(26, $n);
        $pow25_n = $modPow(25, $n);
        $pow24_n = $modPow(24, $n);
        $pow23_n = $modPow(23, $n);

        // n-1 powers (handle n=0 not needed as constraints n>=1)
        $pow25_nm1 = $modPow(25, $n - 1);
        $pow24_nm1 = $modPow(24, $n - 1);
        $pow23_nm1 = $modPow(23, $n - 1);

        // A = strings with zero 'l'
        $A = $pow25_n;
        // B = strings with zero 't' (same as A)
        $B = $pow25_n;
        // AB = zero both 'l' and 't'
        $AB = $pow24_n;

        // C = at most one 'e'
        $C = ($pow25_n + ($n % $MOD) * $pow25_nm1) % $MOD;

        // AC = zero 'l' and at most one 'e'
        $AC = ($pow24_n + ($n % $MOD) * $pow24_nm1) % $MOD;
        // BC = same as AC
        $BC = $AC;

        // ABC = zero 'l', zero 't', at most one 'e'
        $ABC = ($pow23_n + ($n % $MOD) * $pow23_nm1) % $MOD;

        // Inclusion-Exclusion for bad strings
        $bad = ($A + $B) % $MOD;
        $bad = ($bad + $C) % $MOD;
        $bad = ($bad - $AB) % $MOD;
        if ($bad < 0) $bad += $MOD;
        $bad = ($bad - $AC) % $MOD;
        if ($bad < 0) $bad += $MOD;
        $bad = ($bad - $BC) % $MOD;
        if ($bad < 0) $bad += $MOD;
        $bad = ($bad + $ABC) % $MOD;

        // Good strings = total - bad
        $good = ($pow26 - $bad) % $MOD;
        if ($good < 0) $good += $MOD;

        return (int)$good;
    }
}
```

## Swift

```swift
class Solution {
    private let MOD: Int64 = 1_000_000_007

    private func modPow(_ base: Int64, _ exp: Int) -> Int64 {
        var result: Int64 = 1
        var b = base % MOD
        var e = exp
        while e > 0 {
            if (e & 1) == 1 {
                result = (result * b) % MOD
            }
            b = (b * b) % MOD
            e >>= 1
        }
        return result
    }

    func stringCount(_ n: Int) -> Int {
        let n64 = Int64(n)
        // powers
        let p26 = modPow(26, n)
        let p25 = modPow(25, n)
        let p24 = modPow(24, n)
        let p23 = modPow(23, n)

        let p25_1 = modPow(25, max(0, n - 1))
        let p24_1 = modPow(24, max(0, n - 1))
        let p23_1 = modPow(23, max(0, n - 1))

        var ans = p26

        // subtract single violations
        ans = (ans - (3 * p25) % MOD + MOD) % MOD
        ans = (ans - (n64 % MOD) * p25_1 % MOD + MOD) % MOD

        // add pairwise intersections
        ans = (ans + (3 * p24) % MOD) % MOD
        ans = (ans + ((2 * n64) % MOD) * p24_1 % MOD) % MOD

        // subtract triple intersection
        ans = (ans - p23 + MOD) % MOD
        ans = (ans - (n64 % MOD) * p23_1 % MOD + MOD) % MOD

        return Int(ans)
    }
}
```

## Kotlin

```kotlin
import java.util.*

class Solution {
    private val MOD = 1_000_000_007L

    private fun modPow(base: Long, exp: Int): Long {
        var b = base % MOD
        var e = exp
        var res = 1L
        while (e > 0) {
            if ((e and 1) == 1) {
                res = (res * b) % MOD
            }
            b = (b * b) % MOD
            e = e shr 1
        }
        return res
    }

    fun stringCount(n: Int): Int {
        // total strings
        val pow26 = modPow(26L, n)
        val pow25 = modPow(25L, n)
        val pow24 = modPow(24L, n)
        val pow23 = modPow(23L, n)

        // helpers for n-1 powers (n >= 1 by constraints)
        val pow25_1 = if (n > 0) modPow(25L, n - 1) else 1L
        val pow24_1 = if (n > 0) modPow(24L, n - 1) else 1L
        val pow23_1 = if (n > 0) modPow(23L, n - 1) else 1L

        // |C| : at most one 'e'
        var termC = (pow25 + n.toLong() * pow25_1 % MOD) % MOD
        // |A ∩ C| and |B ∩ C|
        var termAC = (pow24 + n.toLong() * pow24_1 % MOD) % MOD
        // |A ∩ B ∩ C|
        var termABC = (pow23 + n.toLong() * pow23_1 % MOD) % MOD

        var ans = pow26
        // subtract |A|+|B|+|C|
        val subAB = (pow25 + pow25) % MOD
        val subAll = (subAB + termC) % MOD
        ans = (ans - subAll + MOD) % MOD

        // add intersections: |A∩B| + |A∩C| + |B∩C|
        val add = (pow24 + (termAC * 2 % MOD)) % MOD
        ans = (ans + add) % MOD

        // subtract triple intersection
        ans = (ans - termABC + MOD) % MOD

        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int _modPow(int base, int exp) {
    int result = 1;
    int b = base % _mod;
    while (exp > 0) {
      if ((exp & 1) == 1) {
        result = (result * b) % _mod;
      }
      b = (b * b) % _mod;
      exp >>= 1;
    }
    return result;
  }

  int stringCount(int n) {
    if (n < 4) return 0;

    int p26 = _modPow(26, n);
    int p25 = _modPow(25, n);
    int p24 = _modPow(24, n);
    int p23 = _modPow(23, n);

    int p25_1 = _modPow(25, n - 1);
    int p24_1 = _modPow(24, n - 1);
    int p23_1 = _modPow(23, n - 1);

    int nn = n % _mod;

    int ans = p26;
    ans = (ans - (3 * p25) % _mod + _mod) % _mod;
    ans = (ans - (nn * p25_1) % _mod + _mod) % _mod;
    ans = (ans + (3 * p24) % _mod) % _mod;
    ans = (ans + ((2 * nn) % _mod) * p24_1 % _mod) % _mod;
    ans = (ans - p23 + _mod) % _mod;
    ans = (ans - (nn * p23_1) % _mod + _mod) % _mod;

    return ans;
  }
}
```

## Golang

```go
func stringCount(n int) int {
	const MOD int64 = 1000000007

	var modPow func(int64, int) int64
	modPow = func(a int64, e int) int64 {
		res := int64(1)
		base := a % MOD
		exp := e
		for exp > 0 {
			if exp&1 == 1 {
				res = res * base % MOD
			}
			base = base * base % MOD
			exp >>= 1
		}
		return res
	}

	n64 := int64(n)

	total := modPow(26, n)

	// A: strings with at most one 'e'
	aZero := modPow(25, n)
	aOne := n64 * modPow(25, n-1) % MOD
	A := (aZero + aOne) % MOD

	// B: no 'l', C: no 't' (both 25^n)
	B := modPow(25, n)
	C := B

	// AB and AC: at most one 'e' and missing one of {'l','t'} -> 24 letters total
	abZero := modPow(24, n)
	abOne := n64 * modPow(24, n-1) % MOD
	AB := (abZero + abOne) % MOD
	AC := AB

	// BC: missing both 'l' and 't' -> 24^n
	BC := modPow(24, n)

	// ABC: at most one 'e' and missing both 'l' and 't' -> 23 letters total
	abcZero := modPow(23, n)
	abcOne := n64 * modPow(23, n-1) % MOD
	ABC := (abcZero + abcOne) % MOD

	ans := total
	ans = (ans - ((A + B + C) % MOD) + MOD) % MOD
	ans = (ans + ((AB + AC + BC) % MOD)) % MOD
	ans = (ans - ABC + MOD) % MOD

	return int(ans)
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def mod_pow(a, e)
  res = 1
  a %= MOD
  while e > 0
    res = (res * a) % MOD if (e & 1) == 1
    a = (a * a) % MOD
    e >>= 1
  end
  res
end

# @param {Integer} n
# @return {Integer}
def string_count(n)
  return 0 if n < 4

  pow26 = mod_pow(26, n)
  pow25 = mod_pow(25, n)
  pow24 = mod_pow(24, n)
  pow23 = mod_pow(23, n)

  term25 = (n % MOD) * mod_pow(25, n - 1) % MOD
  term24 = (n % MOD) * mod_pow(24, n - 1) % MOD
  term23 = (n % MOD) * mod_pow(23, n - 1) % MOD

  a = pow25
  b = pow25
  d = (pow25 + term25) % MOD

  ab = pow24
  ad = (pow24 + term24) % MOD
  bd = ad

  abd = (pow23 + term23) % MOD

  bad = (a + b) % MOD
  bad = (bad + d) % MOD
  bad = (bad - ab - ad - bd) % MOD
  bad = (bad + abd) % MOD
  bad %= MOD
  bad += MOD if bad < 0

  good = pow26 - bad
  good %= MOD
  good += MOD if good < 0
  good
end
```

## Scala

```scala
object Solution {
  private val MOD = 1000000007L

  private def modPow(base: Long, exp: Int): Long = {
    var result = 1L
    var b = base % MOD
    var e = exp
    while (e > 0) {
      if ((e & 1) == 1) result = (result * b) % MOD
      b = (b * b) % MOD
      e >>= 1
    }
    result
  }

  def stringCount(n: Int): Int = {
    val pow26 = modPow(26, n)
    val pow25 = modPow(25, n)
    val pow24 = modPow(24, n)
    val pow23 = modPow(23, n)

    val pow25_1 = if (n > 0) modPow(25, n - 1) else 1L
    val pow24_1 = if (n > 0) modPow(24, n - 1) else 1L
    val pow23_1 = if (n > 0) modPow(23, n - 1) else 1L

    val termA   = (pow25 + n.toLong * pow25_1 % MOD) % MOD               // A
    val termAB  = (pow24 + n.toLong * pow24_1 % MOD) % MOD               // AB and AC
    val termABC = (pow23 + n.toLong * pow23_1 % MOD) % MOD               // ABC

    var ans = pow26
    ans = (ans - termA + MOD) % MOD                     // subtract A
    ans = (ans - (2L * pow25 % MOD) + MOD) % MOD        // subtract B and C
    ans = (ans + (3L * pow24 % MOD)) % MOD              // add BC and two AB/AC contributions of 24^n
    ans = (ans + (2L * n % MOD) * pow24_1 % MOD) % MOD   // add 2*n*24^{n-1}
    ans = (ans - termABC + MOD) % MOD                   // subtract ABC

    ans.toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn string_count(n: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        fn mod_pow(mut base: i64, mut exp: i32) -> i64 {
            let mut res: i64 = 1;
            while exp > 0 {
                if (exp & 1) == 1 {
                    res = res * base % MOD;
                }
                base = base * base % MOD;
                exp >>= 1;
            }
            res
        }

        if n < 4 {
            return 0;
        }
        let ni = n as i64;

        let p26 = mod_pow(26, n);
        let p25 = mod_pow(25, n);
        let p24 = mod_pow(24, n);
        let p23 = mod_pow(23, n);

        let p25_n1 = mod_pow(25, n - 1);
        let p24_n1 = mod_pow(24, n - 1);
        let p23_n1 = mod_pow(23, n - 1);

        // A: no 'l'
        let a = p25;
        // B: no 't'
        let b = p25;
        // C: at most one 'e' => 0 e + exactly 1 e
        let c = (p25 + ni % MOD * p25_n1 % MOD) % MOD;

        // A ∩ B: no l, no t
        let ab = p24;
        // A ∩ C and B ∩ C: no l (or t) and at most one e
        let ac = (p24 + ni % MOD * p24_n1 % MOD) % MOD;
        let bc = ac; // same as ac

        // A ∩ B ∩ C: no l, no t, at most one e
        let abc = (p23 + ni % MOD * p23_n1 % MOD) % MOD;

        let mut ans = p26;
        ans = (ans - a + MOD) % MOD;
        ans = (ans - b + MOD) % MOD;
        ans = (ans - c + MOD) % MOD;
        ans = (ans + ab) % MOD;
        ans = (ans + ac) % MOD;
        ans = (ans + bc) % MOD;
        ans = (ans - abc + MOD) % MOD;

        ans as i32
    }
}
```

## Racket

```racket
(define/contract (string-count n)
  (-> exact-integer? exact-integer?)
  (let* ((MOD 1000000007)
         (modpow
          (lambda (base exp)
            (let loop ((result 1) (b (remainder base MOD)) (e exp))
              (if (= e 0)
                  result
                  (if (odd? e)
                      (loop (remainder (* result b) MOD)
                            (remainder (* b b) MOD)
                            (quotient e 2))
                      (loop result
                            (remainder (* b b) MOD)
                            (quotient e 2)))))))
         (pow26 (modpow 26 n))
         (pow25 (modpow 25 n))
         (pow24 (modpow 24 n))
         (pow23 (modpow 23 n))
         (pow25_1 (if (= n 0) 1 (modpow 5 (- n 1)))) ; placeholder, will be overwritten
         (pow24_1 (if (= n 0) 1 (modpow 4 (- n 1)))) ; placeholder, will be overwritten
         (pow23_1 (if (= n 0) 1 (modpow 3 (- n 1)))) ; placeholder, will be overwritten
         ;; correct powers for bases 25,24,23
         (pow25_1 (if (= n 0) 1 (modpow 25 (- n 1))))
         (pow24_1 (if (= n 0) 1 (modpow 24 (- n 1))))
         (pow23_1 (if (= n 0) 1 (modpow 23 (- n 1))))
         (termA (remainder (+ (* 3 pow25)
                               (remainder (* n pow25_1) MOD))
                           MOD))
         (termB (remainder (+ (* 3 pow24)
                               (remainder (* (* 2 n) pow24_1) MOD))
                           MOD))
         (termC (remainder (+ pow23
                               (remainder (* n pow23_1) MOD))
                           MOD))
         (bad (remainder (+ (remainder (- termA termB) MOD)
                            termC)
                         MOD))
         (ans (remainder (- pow26 bad) MOD)))
    (if (< ans 0) (+ ans MOD) ans)))
```

## Erlang

```erlang
-module(solution).
-export([string_count/1]).

-define(MOD, 1000000007).

-spec string_count(N :: integer()) -> integer().
string_count(N) ->
    Mod = ?MOD,
    Pow26 = mod_pow(26, N),
    Pow25 = mod_pow(25, N),
    Pow24 = mod_pow(24, N),
    Pow23 = mod_pow(23, N),

    Pow25_1 = if N > 0 -> mod_pow(25, N - 1); true -> 0 end,
    Pow24_1 = if N > 0 -> mod_pow(24, N - 1); true -> 0 end,
    Pow23_1 = if N > 0 -> mod_pow(23, N - 1); true -> 0 end,

    Nmod = N rem Mod,

    TermC   = (Pow25 + (Nmod * Pow25_1) rem Mod) rem Mod,
    TermAC  = (Pow24 + (Nmod * Pow24_1) rem Mod) rem Mod,
    TermABC = (Pow23 + (Nmod * Pow23_1) rem Mod) rem Mod,

    Bad0 = ((Pow25 + Pow25) rem Mod + TermC) rem Mod,
    Subtract = (Pow24 + (2 * TermAC) rem Mod) rem Mod,
    Bad1 = (Bad0 - Subtract) rem Mod,
    Bad  = (Bad1 + TermABC) rem Mod,

    AnsTmp = (Pow26 - Bad) rem Mod,
    if
        AnsTmp < 0 -> AnsTmp + Mod;
        true       -> AnsTmp
    end.

-spec mod_pow(Base :: integer(), Exp :: integer()) -> integer().
mod_pow(_, 0) ->
    1;
mod_pow(Base, Exp) when Exp rem 2 =:= 0 ->
    Half = mod_pow(Base, Exp div 2),
    (Half * Half) rem ?MOD;
mod_pow(Base, Exp) ->
    Rest = mod_pow(Base, Exp - 1),
    ((Base rem ?MOD) * Rest) rem ?MOD.
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @modulus 1_000_000_007

  defp mod_pow(base, exp) when exp >= 0 do
    pow_mod(rem(base, @modulus), exp, 1)
  end

  defp pow_mod(_base, 0, acc), do: acc

  defp pow_mod(base, exp, acc) do
    new_acc =
      if Bitwise.band(exp, 1) == 1 do
        rem(acc * base, @modulus)
      else
        acc
      end

    new_base = rem(base * base, @modulus)
    pow_mod(new_base, div(exp, 2), new_acc)
  end

  @spec string_count(n :: integer) :: integer
  def string_count(n) do
    mod = @modulus
    p26 = mod_pow(26, n)
    p25 = mod_pow(25, n)
    p25m = if n > 0, do: mod_pow(25, n - 1), else: 0
    p24 = mod_pow(24, n)
    p24m = if n > 0, do: mod_pow(24, n - 1), else: 0
    p23 = mod_pow(23, n)
    p23m = if n > 0, do: mod_pow(23, n - 1), else: 0

    ans = p26
    ans = (ans - rem(3 * p25, mod) + mod) |> rem(mod)
    ans = (ans - rem(rem(n, mod) * p25m, mod) + mod) |> rem(mod)
    ans = (ans + rem(3 * p24, mod)) |> rem(mod)
    ans = (ans + rem(rem(2 * n, mod) * p24m, mod)) |> rem(mod)
    ans = (ans - p23 + mod) |> rem(mod)
    ans = (ans - rem(rem(n, mod) * p23m, mod) + mod) |> rem(mod)

    ans
  end
end
```
