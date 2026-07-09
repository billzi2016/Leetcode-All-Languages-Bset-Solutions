# 2117. Abbreviating the Product of a Range

## Cpp

```cpp
#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;
using boost::multiprecision::cpp_int;

class Solution {
public:
    string abbreviateProduct(int left, int right) {
        // count total factors of 2 and 5
        long long cnt2 = 0, cnt5 = 0;
        for (int i = left; i <= right; ++i) {
            int x = i;
            while ((x & 1) == 0) { cnt2++; x >>= 1; }
            while (x % 5 == 0) { cnt5++; x /= 5; }
        }
        long long C = min(cnt2, cnt5); // number of trailing zeros
        
        // sum of logs for leading digits
        long double sumLog = 0.0L;
        for (int i = left; i <= right; ++i) {
            sumLog += log10((long double)i);
        }
        long double logWithoutZeros = sumLog - C;
        long long totalDigits = (long long)floor(logWithoutZeros) + 1;
        
        // compute trailing five digits modulo 100000
        const int MOD = 100000;
        long long trailMod = 1;
        long long removed2 = 0, removed5 = 0;
        for (int i = left; i <= right; ++i) {
            long long x = i;
            while (removed2 < C && (x & 1LL) == 0) { x >>= 1; ++removed2; }
            while (removed5 < C && x % 5LL == 0) { x /= 5; ++removed5; }
            trailMod = (trailMod * (x % MOD)) % MOD;
        }
        
        if (totalDigits <= 10) {
            // compute exact product without trailing zeros using big integer
            cpp_int prod = 1;
            removed2 = removed5 = 0;
            for (int i = left; i <= right; ++i) {
                long long x = i;
                while (removed2 < C && (x & 1LL) == 0) { x >>= 1; ++removed2; }
                while (removed5 < C && x % 5LL == 0) { x /= 5; ++removed5; }
                prod *= x;
            }
            string s = prod.convert_to<string>();
            return s + "e" + to_string(C);
        } else {
            // leading five digits
            long double fractional = logWithoutZeros - floor(logWithoutZeros);
            int leading = (int)pow((long double)10.0, fractional + 4); // first 5 digits
            
            string trailStr = to_string(trailMod);
            while (trailStr.size() < 5) trailStr = "0" + trailStr;
            
            return to_string(leading) + trailStr + "e" + to_string(C);
        }
    }
};
```

## Java

```java
import java.math.BigInteger;

class Solution {
    public String abbreviateProduct(int left, int right) {
        final int MOD = 100000;
        long sumLog = 0L; // use double via casting later
        double logSum = 0.0;
        int totalTwo = 0, totalFive = 0;

        for (int i = left; i <= right; i++) {
            int x = i;
            while ((x & 1) == 0) { // divisible by 2
                totalTwo++;
                x >>= 1;
            }
            while (x % 5 == 0) {
                totalFive++;
                x /= 5;
            }
            logSum += Math.log10(i);
        }

        int zeros = Math.min(totalTwo, totalFive);

        // compute last five digits after removing trailing zeros
        long prodMod = 1;
        int removedTwo = 0, removedFive = 0;
        for (int i = left; i <= right; i++) {
            int x = i;
            while ((x & 1) == 0 && removedTwo < zeros) {
                x >>= 1;
                removedTwo++;
            }
            while (x % 5 == 0 && removedFive < zeros) {
                x /= 5;
                removedFive++;
            }
            prodMod = (prodMod * (x % MOD)) % MOD;
        }

        // total digits after removing zeros
        int totalDigits = (int)Math.floor(logSum - zeros) + 1;

        if (totalDigits <= 10) {
            BigInteger exact = BigInteger.ONE;
            for (int i = left; i <= right; i++) {
                exact = exact.multiply(BigInteger.valueOf(i));
            }
            // remove trailing zeros
            while (exact.mod(BigInteger.TEN).equals(BigInteger.ZERO)) {
                exact = exact.divide(BigInteger.TEN);
            }
            return exact.toString() + "e" + zeros;
        }

        // first five digits using logarithms
        double fractional = logSum - zeros;
        double intPart = Math.floor(fractional);
        fractional -= intPart; // now in [0,1)
        double leadingDouble = Math.pow(10.0, fractional + 4); // get first 5 digits
        int leading = (int)leadingDouble;
        if (leading >= 100000) {
            leading /= 10;
        }

        String firstFive = Integer.toString(leading);
        while (firstFive.length() < 5) {
            firstFive = "0" + firstFive;
        }
        String lastFive = String.format("%05d", prodMod);

        return firstFive + "..." + lastFive + "e" + zeros;
    }
}
```

## Python

```python
class Solution(object):
    def abbreviateProduct(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: str
        """
        import math

        MOD = 100000  # keep last five digits
        prod_mod = 1
        cnt2 = cnt5 = 0
        sum_log = 0.0

        for i in range(left, right + 1):
            x = i
            while x % 2 == 0:
                cnt2 += 1
                x //= 2
            while x % 5 == 0:
                cnt5 += 1
                x //= 5
            prod_mod = (prod_mod * (x % MOD)) % MOD
            sum_log += math.log10(i)

        trailing_zeros = min(cnt2, cnt5)
        extra_twos = cnt2 - trailing_zeros
        extra_fives = cnt5 - trailing_zeros

        if extra_twos:
            prod_mod = (prod_mod * pow(2, extra_twos, MOD)) % MOD
        if extra_fives:
            prod_mod = (prod_mod * pow(5, extra_fives, MOD)) % MOD

        log_without = sum_log - trailing_zeros
        total_digits = int(math.floor(log_without)) + 1

        if total_digits <= 10:
            # compute exact product after removing zeros
            prod = 1
            for i in range(left, right + 1):
                prod *= i
            while prod % 10 == 0:
                prod //= 10
            return str(prod) + "e" + str(trailing_zeros)
        else:
            frac = log_without - math.floor(log_without)
            leading5 = int(10 ** (frac + 4))
            trailing5_str = str(prod_mod).rjust(5, '0')
            return f"{leading5}...{trailing5_str}e{trailing_zeros}"
```

## Python3

```python
import math

class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        MOD = 100000

        total2 = total5 = 0
        log_sum = 0.0
        for i in range(left, right + 1):
            x = i
            while x % 2 == 0:
                total2 += 1
                x //= 2
            while x % 5 == 0:
                total5 += 1
                x //= 5
            log_sum += math.log10(i)

        zeros = min(total2, total5)
        remaining_digits = int(math.floor(log_sum)) + 1 - zeros

        # If the number after removing trailing zeros has at most 10 digits,
        # compute it exactly.
        if remaining_digits <= 10:
            rem2 = zeros
            rem5 = zeros
            exact = 1
            for i in range(left, right + 1):
                x = i
                while rem2 > 0 and x % 2 == 0:
                    x //= 2
                    rem2 -= 1
                while rem5 > 0 and x % 5 == 0:
                    x //= 5
                    rem5 -= 1
                exact *= x
            return f"{exact}e{zeros}"

        # Otherwise compute first five digits via logarithms and last five via modulo.
        exp_val = log_sum - zeros
        frac = exp_val - math.floor(exp_val)
        first_five = int(10 ** (frac + 4))

        rem2 = zeros
        rem5 = zeros
        prod_mod = 1
        for i in range(left, right + 1):
            x = i
            while rem2 > 0 and x % 2 == 0:
                x //= 2
                rem2 -= 1
            while rem5 > 0 and x % 5 == 0:
                x //= 5
                rem5 -= 1
            prod_mod = (prod_mod * (x % MOD)) % MOD

        last_five_str = f"{prod_mod:05d}"
        return f"{first_five}...{last_five_str}e{zeros}"
```

## C

```c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

static long long mod_pow(long long base, long long exp, long long mod) {
    long long res = 1;
    while (exp > 0) {
        if (exp & 1) res = (res * base) % mod;
        base = (base * base) % mod;
        exp >>= 1;
    }
    return res;
}

char* abbreviateProduct(int left, int right) {
    const long long MOD = 100000LL; // keep last 5 digits
    long long cnt2 = 0, cnt5 = 0;
    long double logSum = 0.0L;
    long long prodMod = 1;

    for (int i = left; i <= right; ++i) {
        int x = i;
        while ((x & 1) == 0) { // divisible by 2
            cnt2++;
            x >>= 1;
        }
        while (x % 5 == 0) {
            cnt5++;
            x /= 5;
        }
        prodMod = (prodMod * (x % MOD)) % MOD;
        logSum += log10((long double)i);
    }

    long long zeroCnt = cnt2 < cnt5 ? cnt2 : cnt5;
    long long extra2 = cnt2 - zeroCnt;
    long long extra5 = cnt5 - zeroCnt;

    // multiply remaining 2s and 5s into prodMod
    if (extra2) prodMod = (prodMod * mod_pow(2, extra2, MOD)) % MOD;
    if (extra5) prodMod = (prodMod * mod_pow(5, extra5, MOD)) % MOD;

    long double logWithoutZeros = logSum - zeroCnt;
    int totalDigits = (int)floor(logWithoutZeros) + 1;

    // buffer for result
    char* ans = (char*)malloc(64);
    if (!ans) return NULL;

    if (totalDigits <= 10) {
        __int128 exact = 1;
        for (int i = left; i <= right; ++i) {
            int x = i;
            while ((x & 1) == 0) { x >>= 1; }
            while (x % 5 == 0) { x /= 5; }
            exact *= (__int128)x;
        }
        if (extra2) {
            for (long long k = 0; k < extra2; ++k) exact *= 2;
        }
        if (extra5) {
            for (long long k = 0; k < extra5; ++k) exact *= 5;
        }

        // convert __int128 to string
        char numBuf[32];
        int idx = 0;
        if (exact == 0) {
            numBuf[idx++] = '0';
        } else {
            while (exact > 0) {
                int digit = exact % 10;
                numBuf[idx++] = '0' + digit;
                exact /= 10;
            }
            // reverse
            for (int i = 0; i < idx / 2; ++i) {
                char tmp = numBuf[i];
                numBuf[i] = numBuf[idx - 1 - i];
                numBuf[idx - 1 - i] = tmp;
            }
        }
        numBuf[idx] = '\0';
        sprintf(ans, "%s" "e%lld", numBuf, zeroCnt);
    } else {
        long double frac = logWithoutZeros - floor(logWithoutZeros);
        int first5 = (int)pow(10.0L, frac + 4.0L) + 1e-9; // leading five digits
        long long last5 = prodMod % MOD;
        sprintf(ans, "%d...%05llde%lld", first5, last5, zeroCnt);
    }

    return ans;
}
```

## Csharp

```csharp
using System;
using System.Numerics;

public class Solution
{
    private const int MOD = 100000; // keep last five digits

    public string AbbreviateProduct(int left, int right)
    {
        double sumLog = 0.0;
        long totalTwo = 0, totalFive = 0;
        long prodMod = 1;

        for (int i = left; i <= right; i++)
        {
            sumLog += Math.Log10(i);

            int x = i;
            while ((x & 1) == 0)
            {
                totalTwo++;
                x >>= 1;
            }
            while (x % 5 == 0)
            {
                totalFive++;
                x /= 5;
            }

            prodMod = (prodMod * (x % MOD)) % MOD;
        }

        long zeros = Math.Min(totalTwo, totalFive);
        long extraTwo = totalTwo - zeros;
        long extraFive = totalFive - zeros;

        prodMod = (prodMod * ModPow(2, extraTwo, MOD)) % MOD;
        prodMod = (prodMod * ModPow(5, extraFive, MOD)) % MOD;

        double logWithoutZeros = sumLog - zeros;
        int digits = (int)Math.Floor(logWithoutZeros + 1e-12) + 1;

        if (digits <= 10)
        {
            BigInteger exact = new BigInteger(1);
            for (int i = left; i <= right; i++)
                exact *= i;
            while (exact % 10 == 0)
                exact /= 10;
            return exact.ToString() + "e" + zeros;
        }
        else
        {
            double fractional = logWithoutZeros - Math.Floor(logWithoutZeros);
            double leadingDouble = Math.Pow(10, fractional + 4); // first five digits
            int leading = (int)Math.Floor(leadingDouble + 1e-9);

            string trailing = prodMod.ToString().PadLeft(5, '0');
            return $"{leading}...{trailing}e{zeros}";
        }
    }

    private static long ModPow(long baseVal, long exp, int mod)
    {
        long result = 1;
        long b = baseVal % mod;
        while (exp > 0)
        {
            if ((exp & 1) == 1)
                result = (result * b) % mod;
            b = (b * b) % mod;
            exp >>= 1;
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} left
 * @param {number} right
 * @return {string}
 */
var abbreviateProduct = function(left, right) {
    const MOD = 100000;
    let total2 = 0, total5 = 0, sumLog = 0;
    let prodMod = 1;

    for (let i = left; i <= right; ++i) {
        let x = i;
        while ((x & 1) === 0) { // divisible by 2
            ++total2;
            x >>= 1;
        }
        while (x % 5 === 0) {
            ++total5;
            x /= 5;
        }
        prodMod = (prodMod * (x % MOD)) % MOD;
        sumLog += Math.log10(i);
    }

    const zeroCount = Math.min(total2, total5);
    const leftover2 = total2 - zeroCount;
    const leftover5 = total5 - zeroCount;

    const modPow = (base, exp) => {
        let res = 1;
        let b = base % MOD;
        while (exp > 0) {
            if (exp & 1) res = (res * b) % MOD;
            b = (b * b) % MOD;
            exp >>= 1;
        }
        return res;
    };

    prodMod = (prodMod * modPow(2, leftover2)) % MOD;
    prodMod = (prodMod * modPow(5, leftover5)) % MOD;

    const logVal = sumLog - zeroCount;
    const totalDigits = Math.floor(logVal) + 1;

    if (totalDigits <= 10) {
        // exact computation with BigInt
        let prodExact = 1n;
        for (let i = left; i <= right; ++i) {
            let x = BigInt(i);
            while ((x & 1n) === 0n) { x >>= 1n; }
            while (x % 5n === 0n) { x /= 5n; }
            prodExact *= x;
        }

        const powBig = (base, exp) => {
            let res = 1n;
            let b = BigInt(base);
            let e = exp;
            while (e > 0) {
                if (e & 1) res *= b;
                b *= b;
                e >>= 1;
            }
            return res;
        };

        prodExact *= powBig(2, leftover2);
        prodExact *= powBig(5, leftover5);

        return prodExact.toString() + 'e' + zeroCount;
    } else {
        const fractional = logVal - Math.floor(logVal);
        let leading = Math.floor(Math.pow(10, fractional + 4) + 1e-9);
        if (leading >= 100000) leading = 99999; // safety
        const lastFive = prodMod.toString().padStart(5, '0');
        return `${leading}...${lastFive}e${zeroCount}`;
    }
};
```

## Typescript

```typescript
function abbreviateProduct(left: number, right: number): string {
    const MOD = 100000; // 10^5
    let cnt2 = 0;
    let cnt5 = 0;
    let prodMod = 1;

    for (let i = left; i <= right; ++i) {
        let x = i;
        while ((x & 1) === 0) { // divisible by 2
            cnt2++;
            x >>= 1;
        }
        while (x % 5 === 0) {
            cnt5++;
            x /= 5;
        }
        prodMod = (prodMod * (x % MOD)) % MOD;
    }

    const zeros = Math.min(cnt2, cnt5);
    const extra2 = cnt2 - zeros;
    const extra5 = cnt5 - zeros;

    function modPow(base: number, exp: number, mod: number): number {
        let result = 1 % mod;
        let b = base % mod;
        while (exp > 0) {
            if (exp & 1) result = (result * b) % mod;
            b = (b * b) % mod;
            exp >>= 1;
        }
        return result;
    }

    prodMod = (prodMod * modPow(2, extra2, MOD)) % MOD;
    prodMod = (prodMod * modPow(5, extra5, MOD)) % MOD;

    // compute total log10 to get first digits and digit count
    let sumLog = 0;
    for (let i = left; i <= right; ++i) {
        sumLog += Math.log10(i);
    }
    const totalDigits = Math.floor(sumLog) + 1;
    const digitsAfterRemoval = totalDigits - zeros;

    if (digitsAfterRemoval <= 10) {
        // exact computation using BigInt
        let prod = 1n;
        for (let i = left; i <= right; ++i) {
            prod *= BigInt(i);
        }
        while (prod % 10n === 0n) prod /= 10n;
        return prod.toString() + "e" + zeros;
    } else {
        const fractional = sumLog - Math.floor(sumLog);
        const firstFiveNum = Math.floor(Math.pow(10, fractional + 4));
        const firstStr = firstFiveNum.toString();
        const lastStr = prodMod.toString().padStart(5, '0');
        return `${firstStr}...${lastStr}e${zeros}`;
    }
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $left
     * @param Integer $right
     * @return String
     */
    function abbreviateProduct($left, $right) {
        $cnt2 = 0;
        $cnt5 = 0;
        $reduced = [];

        for ($i = $left; $i <= $right; ++$i) {
            $x = $i;
            while (($x & 1) == 0) { // divisible by 2
                $cnt2++;
                $x >>= 1;
            }
            while ($x % 5 == 0) {
                $cnt5++;
                $x /= 5;
            }
            $reduced[] = $x; // x now has no factor 2 or 5
        }

        $tz = min($cnt2, $cnt5);          // trailing zeros
        $extraTwos = $cnt2 - $tz;         // remaining factors of 2

        // last five digits after removing zeros
        $mod = 100000;
        $prodMod = 1;
        foreach ($reduced as $v) {
            $prodMod = ($prodMod * ($v % $mod)) % $mod;
        }
        $prodMod = $this->modPow(2, $extraTwos, $mod) * $prodMod % $mod;

        // logarithm to get leading digits and total length
        $logSum = 0.0;
        for ($i = $left; $i <= $right; ++$i) {
            $logSum += log10($i);
        }
        $logAdj = $logSum - $tz;                 // remove zeros from log
        $totalDigits = (int)floor($logAdj) + 1;

        if ($totalDigits <= 10) {
            // compute exact product (fits in 64‑bit)
            $full = 1;
            for ($i = $left; $i <= $right; ++$i) {
                $full *= $i;
            }
            while ($full % 10 == 0) {
                $full /= 10;
                $tz++;
            }
            return (string)$full . "e" . $tz;
        } else {
            $frac = $logAdj - floor($logAdj);
            $firstFive = (int)floor(pow(10, $frac + 4)); // first five digits
            $lastFiveStr = str_pad((string)$prodMod, 5, '0', STR_PAD_LEFT);
            return $firstFive . "..." . $lastFiveStr . "e" . $tz;
        }
    }

    private function modPow($base, $exp, $mod) {
        $result = 1;
        $base %= $mod;
        while ($exp > 0) {
            if ($exp & 1) {
                $result = ($result * $base) % $mod;
            }
            $base = ($base * $base) % $mod;
            $exp >>= 1;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func abbreviateProduct(_ left: Int, _ right: Int) -> String {
        let MOD = 100000
        var prodMod: Int64 = 1
        var cnt2 = 0
        var cnt5 = 0
        var sumLog = 0.0

        for i in left...right {
            var x = i
            while x % 2 == 0 {
                cnt2 += 1
                x /= 2
            }
            while x % 5 == 0 {
                cnt5 += 1
                x /= 5
            }
            prodMod = (prodMod * Int64(x % MOD)) % Int64(MOD)
            sumLog += log10(Double(i))
        }

        let zeros = min(cnt2, cnt5)
        var extraTwos = cnt2 - zeros

        for _ in 0..<extraTwos {
            prodMod = (prodMod * 2) % Int64(MOD)
        }

        let adjustedLog = sumLog - Double(zeros)
        let totalDigits = Int(floor(adjustedLog)) + 1

        if totalDigits <= 10 {
            var exact: UInt64 = 1
            for i in left...right {
                var x = i
                while x % 2 == 0 { x /= 2 }
                while x % 5 == 0 { x /= 5 }
                exact *= UInt64(x)
            }
            if extraTwos > 0 {
                for _ in 0..<extraTwos {
                    exact <<= 1
                }
            }
            return "\(exact)e\(zeros)"
        } else {
            let fractional = adjustedLog - floor(adjustedLog)
            let leadingDouble = pow(10.0, fractional + 4)
            let leading = Int(leadingDouble)
            let lastStr = String(format: "%05d", Int(prodMod))
            return "\(leading)...\(lastStr)e\(zeros)"
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun abbreviateProduct(left: Int, right: Int): String {
        var count5 = 0
        for (i in left..right) {
            var x = i
            while (x % 5 == 0) {
                count5++
                x /= 5
            }
        }
        val trailingZeros = count5

        var removedTwos = 0
        var prod = 1L
        val MOD_BIG = 1_000_000_000_000L // keep enough digits for later extraction
        for (i in left..right) {
            var x = i
            while (x % 5 == 0) {
                x /= 5
            }
            while (x % 2 == 0 && removedTwos < trailingZeros) {
                x /= 2
                removedTwos++
            }
            prod = (prod * x) % MOD_BIG
        }

        var sumLog = 0.0
        for (i in left..right) {
            sumLog += Math.log10(i.toDouble())
        }
        val adjustedLog = sumLog - trailingZeros
        val totalDigits = Math.floor(adjustedLog).toLong() + 1

        return if (totalDigits <= 10L) {
            "${prod}e$trailingZeros"
        } else {
            val fractional = adjustedLog - Math.floor(adjustedLog)
            val firstFive = Math.pow(10.0, fractional + 4).toLong()
            val lastFive = (prod % 100_000L).toInt()
            val lastStr = String.format("%05d", lastFive)
            "${firstFive}...${lastStr}e$trailingZeros"
        }
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  String abbreviateProduct(int left, int right) {
    const int MOD = 100000;
    int totalTwos = 0;
    int totalFives = 0;
    double sumLog = 0.0;
    int prodMod = 1;

    for (int i = left; i <= right; i++) {
      int x = i;
      while ((x & 1) == 0) { // divisible by 2
        totalTwos++;
        x >>= 1;
      }
      while (x % 5 == 0) {
        totalFives++;
        x ~/= 5;
      }
      prodMod = (prodMod * (x % MOD)) % MOD;
      sumLog += log(i) / ln10;
    }

    int zeroCount = totalTwos < totalFives ? totalTwos : totalFives;
    int extraTwos = totalTwos - zeroCount;
    int extraFives = totalFives - zeroCount;

    for (int i = 0; i < extraTwos; i++) {
      prodMod = (prodMod * 2) % MOD;
    }
    for (int i = 0; i < extraFives; i++) {
      prodMod = (prodMod * 5) % MOD;
    }

    int totalDigits = sumLog.floor() + 1;
    int effectiveDigits = totalDigits - zeroCount;

    if (effectiveDigits <= 10) {
      BigInt product = BigInt.one;
      for (int i = left; i <= right; i++) {
        product *= BigInt.from(i);
      }
      while (product % BigInt.from(10) == BigInt.zero) {
        product ~/= BigInt.from(10);
      }
      return '${product.toString()}e$zeroCount';
    } else {
      double logPrime = sumLog - zeroCount;
      double fractional = logPrime - logPrime.floor();
      int first5 = (pow(10, fractional + 4)).floor();
      String last5 = prodMod.toString().padLeft(5, '0');
      return '${first5}...${last5}e$zeroCount';
    }
  }
}
```

## Golang

```go
import (
	"fmt"
	"math"
)

func powMod(base int64, exp int, mod int64) int64 {
	res := int64(1)
	b := base % mod
	for exp > 0 {
		if exp&1 == 1 {
			res = (res * b) % mod
		}
		b = (b * b) % mod
		exp >>= 1
	}
	return res
}

func abbreviateProduct(left int, right int) string {
	const MOD int64 = 100000

	totalTwo, totalFive := 0, 0
	var prodMod int64 = 1
	logSum := 0.0

	for i := left; i <= right; i++ {
		x := i
		for x%2 == 0 {
			totalTwo++
			x /= 2
		}
		for x%5 == 0 {
			totalFive++
			x /= 5
		}
		prodMod = (prodMod * int64(x)) % MOD
		logSum += math.Log10(float64(i))
	}

	zeroCount := totalTwo
	if totalFive < zeroCount {
		zeroCount = totalFive
	}
	extraTwo := totalTwo - zeroCount
	extraFive := totalFive - zeroCount

	prodMod = (prodMod * powMod(2, extraTwo, MOD)) % MOD
	prodMod = (prodMod * powMod(5, extraFive, MOD)) % MOD

	digitsWithoutZeros := int(math.Floor(logSum-float64(zeroCount))) + 1

	if digitsWithoutZeros <= 10 {
		var exact uint64 = 1
		for i := left; i <= right; i++ {
			x := i
			for x%2 == 0 {
				x /= 2
			}
			for x%5 == 0 {
				x /= 5
			}
			exact *= uint64(x)
		}
		for ; extraTwo > 0; extraTwo-- {
			exact *= 2
		}
		for ; extraFive > 0; extraFive-- {
			exact *= 5
		}
		return fmt.Sprintf("%de%d", exact, zeroCount)
	}

	// first five digits
	logWithoutZeros := logSum - float64(zeroCount)
	intPart := math.Floor(logWithoutZeros)
	fracPart := logWithoutZeros - intPart
	firstFiveFloat := math.Pow(10, fracPart+4)
	firstFive := int(firstFiveFloat + 1e-9) // small epsilon
	if firstFive >= 100000 {
		firstFive = 99999
	}

	lastStr := fmt.Sprintf("%05d", prodMod)
	return fmt.Sprintf("%d...%se%d", firstFive, lastStr, zeroCount)
}
```

## Ruby

```ruby
def abbreviate_product(left, right)
  total_two = 0
  total_five = 0
  sum_log = 0.0

  (left..right).each do |i|
    x = i
    while (x & 1) == 0
      total_two += 1
      x >>= 1
    end
    while x % 5 == 0
      total_five += 1
      x /= 5
    end
    sum_log += Math.log10(i)
  end

  zeros = [total_two, total_five].min

  # compute last five digits after removing zeros
  need_two = zeros
  need_five = zeros
  mod = 100_000
  tail = 1

  (left..right).each do |i|
    x = i
    while need_two > 0 && (x & 1) == 0
      x >>= 1
      need_two -= 1
    end
    while need_five > 0 && x % 5 == 0
      x /= 5
      need_five -= 1
    end
    tail = (tail * (x % mod)) % mod
  end

  # first five digits after removing zeros
  exp_val = sum_log - zeros
  int_part = exp_val.floor
  frac_part = exp_val - int_part
  leading = (10 ** (frac_part + 4)).floor
  leading /= 10 while leading >= 100_000

  digits_after_removal = int_part + 1

  if digits_after_removal <= 10
    prod = 1
    (left..right).each { |i| prod *= i }
    while prod % 10 == 0
      prod /= 10
    end
    return "#{prod}e#{zeros}"
  else
    tail_str = sprintf("%05d", tail)
    return "#{leading}...#{tail_str}e#{zeros}"
  end
end
```

## Scala

```scala
object Solution {
    def abbreviateProduct(left: Int, right: Int): String = {
        val MOD = 100000L
        var cnt2 = 0L
        var cnt5 = 0L
        var prodMod = 1L
        var sumLog = 0.0

        for (i <- left to right) {
            var x = i
            while (x % 2 == 0) {
                cnt2 += 1
                x /= 2
            }
            while (x % 5 == 0) {
                cnt5 += 1
                x /= 5
            }
            prodMod = (prodMod * (x % MOD)) % MOD
            sumLog += Math.log10(i.toDouble)
        }

        val zeros = math.min(cnt2, cnt5)
        var extra2 = cnt2 - zeros
        var extra5 = cnt5 - zeros

        def powMod(base: Long, exp: Long): Long = {
            var res = 1L
            var b = base % MOD
            var e = exp
            while (e > 0) {
                if ((e & 1L) == 1L) res = (res * b) % MOD
                b = (b * b) % MOD
                e >>= 1
            }
            res
        }

        prodMod = (prodMod * powMod(2, extra2)) % MOD
        prodMod = (prodMod * powMod(5, extra5)) % MOD

        val logQ = sumLog - zeros.toDouble
        val digitCount = Math.floor(logQ) + 1 // number of digits in Q

        if (digitCount <= 10) {
            var value = 1L
            for (i <- left to right) {
                value *= i.toLong
                while (value % 10 == 0) value /= 10
            }
            s"${value}e${zeros}"
        } else {
            val frac = logQ - Math.floor(logQ)
            val leading = Math.floor(Math.pow(10.0, frac + 4)).toLong
            val trailing = f"${prodMod}%05d"
            s"${leading}...${trailing}e${zeros}"
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn abbreviate_product(left: i32, right: i32) -> String {
        const MOD: u64 = 100_000;
        // total counts of factor 2 and 5
        let mut total_two: i64 = 0;
        let mut total_five: i64 = 0;
        for i in left..=right {
            let mut n = i as u64;
            while n % 2 == 0 {
                total_two += 1;
                n /= 2;
            }
            while n % 5 == 0 {
                total_five += 1;
                n /= 5;
            }
        }
        let c = std::cmp::min(total_two, total_five) as i64; // trailing zeros
        let excess_two = (total_two - c) as u32;
        let excess_five = (total_five - c) as u32;

        // sum of logs for leading digits
        let mut log_sum: f64 = 0.0;
        for i in left..=right {
            log_sum += (i as f64).log10();
        }
        let exp_without_zeros = log_sum - c as f64;
        let digit_cnt = exp_without_zeros.floor() as i64 + 1; // number of digits after removing zeros

        // compute last five digits modulo MOD
        let mut prod_mod: u64 = 1;
        let mut removed_two: i64 = 0;
        let mut removed_five: i64 = 0;
        for i in left..=right {
            let mut x = i as u64;
            while x % 2 == 0 && removed_two < c {
                x /= 2;
                removed_two += 1;
            }
            while x % 5 == 0 && removed_five < c {
                x /= 5;
                removed_five += 1;
            }
            prod_mod = (prod_mod * (x % MOD)) % MOD;
        }
        fn mod_pow(mut base: u64, mut exp: u32, modu: u64) -> u64 {
            let mut res = 1u64;
            while exp > 0 {
                if exp & 1 == 1 {
                    res = (res * base) % modu;
                }
                base = (base * base) % modu;
                exp >>= 1;
            }
            res
        }
        prod_mod = (prod_mod * mod_pow(2, excess_two, MOD)) % MOD;
        prod_mod = (prod_mod * mod_pow(5, excess_five, MOD)) % MOD;

        if digit_cnt <= 10 {
            // compute exact value using u128 (fits because ≤10 digits)
            let mut prod_exact: u128 = 1;
            let mut removed_two2: i64 = 0;
            let mut removed_five2: i64 = 0;
            for i in left..=right {
                let mut x = i as u128;
                while x % 2 == 0 && removed_two2 < c {
                    x /= 2;
                    removed_two2 += 1;
                }
                while x % 5 == 0 && removed_five2 < c {
                    x /= 5;
                    removed_five2 += 1;
                }
                prod_exact *= x;
            }
            for _ in 0..excess_two {
                prod_exact *= 2;
            }
            for _ in 0..excess_five {
                prod_exact *= 5;
            }
            return format!("{}e{}", prod_exact, c);
        } else {
            // first five digits
            let fractional = exp_without_zeros - exp_without_zeros.floor();
            let leading = (10f64.powf(fractional + 4.0)).floor() as u64; // 5 digits
            let trailing_str = format!("{:05}", prod_mod);
            return format!("{}...{}e{}", leading, trailing_str, c);
        }
    }
}
```

## Racket

```racket
(define (pow-mod base exp mod)
  (let loop ((b (modulo base mod)) (e exp) (res 1))
    (if (= e 0)
        res
        (loop (modulo (* b b) mod)
              (quotient e 2)
              (if (odd? e) (modulo (* res b) mod) res)))))

(define (abbreviate-product left right)
  (let* ((MOD 100000)
         (cnt2 0)
         (cnt5 0)
         (prod-mod 1)
         (sumlog 0.0))
    (for ([i (in-range left (+ right 1))])
      (set! sumlog (+ sumlog (log10 i)))
      ;; remove factors of 2
      (let loop ((x i))
        (if (= (remainder x 2) 0)
            (begin (set! cnt2 (+ cnt2 1))
                   (loop (/ x 2)))
            (let loop5 ((y x))
              (if (= (remainder y 5) 0)
                  (begin (set! cnt5 (+ cnt5 1))
                         (loop5 (/ y 5)))
                  (set! prod-mod
                        (modulo (* prod-mod (modulo y MOD)) MOD)))))))
    (let* ((zeros (min cnt2 cnt5))
           (extra2 (- cnt2 zeros))
           (extra5 (- cnt5 zeros))
           (prod-mod (modulo (* prod-mod
                               (pow-mod 2 extra2 MOD)
                               (pow-mod 5 extra5 MOD))
                             MOD))
           (log-noz (- sumlog zeros))
           (total-digits (+ (floor log-noz) 1)))
      (if (<= total-digits 10)
          ;; compute exact product and strip zeros
          (let ((exact 1))
            (for ([i (in-range left (+ right 1))])
              (set! exact (* exact i)))
            (let loop ((z 0) (n exact))
              (if (= (remainder n 10) 0)
                  (loop (+ z 1) (/ n 10))
                  (string-append (number->string n) "e" (number->string z)))))
          ;; abbreviated form
          (let* ((fraction (- log-noz (floor log-noz)))
                 (leading (inexact->exact (floor (expt 10 (+ fraction 4)))))
                 (last5-str (format "~5,'0d" prod-mod))
                 (result (string-append (number->string leading) "..."
                                         last5-str "e"
                                         (number->string zeros))))
            result)))))
```

## Erlang

```erlang
-spec abbreviate_product(Left :: integer(), Right :: integer()) -> unicode:unicode_binary().
abbreviate_product(Left, Right) ->
    Ln10 = math:log(10),
    {Cnt2, Cnt5, LogSum} = count_factors_and_log(Left, Right, 0, 0, 0.0, Ln10),
    Zeros = min(Cnt2, Cnt5),

    StrippedLog = LogSum - Zeros,
    TotalDigits = trunc(math:floor(StrippedLog)) + 1,

    Result =
        if
            TotalDigits =< 10 ->
                Exact = compute_exact(Left, Right, Zeros, 0, 0, 1),
                integer_to_list(Exact) ++ "e" ++ integer_to_list(Zeros);
            true ->
                First5 = first_five_digits(LogSum, Zeros),
                LastMod = compute_mod_last5(Left, Right, Zeros, 0, 0, 1),
                LastStr = lists:flatten(io_lib:format("~5..0B", [LastMod])),
                integer_to_list(First5) ++ "..." ++ LastStr ++ "e" ++ integer_to_list(Zeros)
        end,
    list_to_binary(Result).

%% count total factors of 2 and 5 and sum of logs
count_factors_and_log(L, R, C2, C5, Sum, Ln10) when L > R ->
    {C2, C5, Sum};
count_factors_and_log(L, R, C2, C5, Sum, Ln10) ->
    {T, F} = count_twos_fives(L),
    NewC2 = C2 + T,
    NewC5 = C5 + F,
    NewSum = Sum + math:log(L) / Ln10,
    count_factors_and_log(L + 1, R, NewC2, NewC5, NewSum, Ln10).

%% count twos and fives in a single number
count_twos_fives(N) ->
    {T, N1} = remove_factor(N, 2, 0),
    {F, _N2} = remove_factor(N1, 5, 0),
    {T, F}.

remove_factor(N, Factor, Acc) when N rem Factor =:= 0 ->
    remove_factor(N div Factor, Factor, Acc + 1);
remove_factor(N, _Factor, Acc) ->
    {Acc, N}.

%% compute exact product after removing Z zeros (used when total digits <=10)
compute_exact(L, R, Z, Rem2, Rem5, Acc) when L > R ->
    Acc;
compute_exact(L, R, Z, Rem2, Rem5, Acc) ->
    X = L,
    {X1, NewRem2} = remove_up_to(X, 2, Rem2, Z),
    {X2, NewRem5} = remove_up_to(X1, 5, Rem5, Z),
    compute_exact(L + 1, R, Z, NewRem2, NewRem5, Acc * X2).

%% compute last five digits modulo 100000 after removing Z zeros
compute_mod_last5(L, R, Z, Rem2, Rem5, Acc) when L > R ->
    Acc rem 100000;
compute_mod_last5(L, R, Z, Rem2, Rem5, Acc) ->
    X = L,
    {X1, NewRem2} = remove_up_to(X, 2, Rem2, Z),
    {X2, NewRem5} = remove_up_to(X1, 5, Rem5, Z),
    NewAcc = (Acc * (X2 rem 100000)) rem 100000,
    compute_mod_last5(L + 1, R, Z, NewRem2, NewRem5, NewAcc).

%% remove factors of a given prime up to total needed removals
remove_up_to(N, Factor, RemovedSoFar, Total) when RemovedSoFar < Total, N rem Factor =:= 0 ->
    remove_up_to(N div Factor, Factor, RemovedSoFar + 1, Total);
remove_up_to(N, _Factor, RemovedSoFar, _Total) ->
    {N, RemovedSoFar}.

%% first five digits after removing trailing zeros
first_five_digits(LogSum, Z) ->
    StrippedLog = LogSum - Z,
    IPart = trunc(StrippedLog),
    Fraction = StrippedLog - IPart,
    Pow = math:pow(10, Fraction + 4),
    trunc(Pow).
```

## Elixir

```elixir
defmodule Solution do
  @spec abbreviate_product(left :: integer, right :: integer) :: String.t()
  def abbreviate_product(left, right) do
    mod = 100_000

    {cnt2, cnt5, prod_mod} =
      Enum.reduce(left..right, {0, 0, 1}, fn i, {c2, c5, p} ->
        {c2_i, rest} = remove_factor(i, 2)
        {c5_i, rest2} = remove_factor(rest, 5)

        new_c2 = c2 + c2_i
        new_c5 = c5 + c5_i

        new_p = rem(p * rem(rest2, mod), mod)
        {new_c2, new_c5, new_p}
      end)

    zeros = min(cnt2, cnt5)
    extra2 = cnt2 - zeros
    extra5 = cnt5 - zeros

    prod_mod =
      Enum.reduce(1..extra2, prod_mod, fn _, acc -> rem(acc * 2, mod) end)

    prod_mod =
      Enum.reduce(1..extra5, prod_mod, fn _, acc -> rem(acc * 5, mod) end)

    total_log = Enum.reduce(left..right, 0.0, fn i, acc -> acc + :math.log10(i) end)
    log_without_zeros = total_log - zeros
    digits = trunc(:math.floor(log_without_zeros)) + 1

    if digits <= 10 do
      product =
        Enum.reduce(left..right, 1, fn i, acc -> acc * i end)

      product_no_zero = remove_trailing_zeros(product)
      "#{product_no_zero}e#{zeros}"
    else
      f = log_without_zeros - trunc(:math.floor(log_without_zeros))
      leading5 = trunc(:math.pow(10, f + 4))

      last5_str =
        prod_mod
        |> Integer.to_string()
        |> String.pad_leading(5, "0")

      "#{leading5}...#{last5_str}e#{zeros}"
    end
  end

  defp remove_factor(num, prime) do
    if rem(num, prime) == 0 do
      {cnt, rest} = remove_factor(div(num, prime), prime)
      {cnt + 1, rest}
    else
      {0, num}
    end
  end

  defp remove_trailing_zeros(n) do
    if rem(n, 10) == 0 do
      remove_trailing_zeros(div(n, 10))
    else
      n
    end
  end
end
```
