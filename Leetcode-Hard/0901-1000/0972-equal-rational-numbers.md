# 0972. Equal Rational Numbers

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    pair<long long,long long> toFraction(const string& s) {
        size_t dotPos = s.find('.');
        string intPartStr, afterDot;
        if (dotPos == string::npos) {
            intPartStr = s;
            afterDot = "";
        } else {
            intPartStr = s.substr(0, dotPos);
            afterDot = s.substr(dotPos + 1);
        }
        long long integerPart = stoll(intPartStr.empty() ? "0" : intPartStr);

        string nonRep, rep;
        size_t lpar = afterDot.find('(');
        if (lpar != string::npos) {
            nonRep = afterDot.substr(0, lpar);
            size_t rpar = afterDot.find(')', lpar);
            rep = afterDot.substr(lpar + 1, rpar - lpar - 1);
        } else {
            nonRep = afterDot;
            rep = "";
        }

        long long N = nonRep.empty() ? 0 : stoll(nonRep);
        long long R = rep.empty() ? 0 : stoll(rep);
        int n = (int)nonRep.size();
        int r = (int)rep.size();

        long long numerator, denominator;
        if (r == 0) {
            long long pow10_n = 1;
            for (int i = 0; i < n; ++i) pow10_n *= 10;
            denominator = pow10_n;
            numerator = integerPart * denominator + N;
        } else {
            long long pow10_n = 1, pow10_r = 1;
            for (int i = 0; i < n; ++i) pow10_n *= 10;
            for (int i = 0; i < r; ++i) pow10_r *= 10;
            long long denom_frac = pow10_n * (pow10_r - 1);
            long long numer_frac = N * (pow10_r - 1) + R;
            denominator = denom_frac;
            numerator = integerPart * denominator + numer_frac;
        }

        long long g = std::gcd(numerator, denominator);
        numerator /= g;
        denominator /= g;
        return {numerator, denominator};
    }

    bool isRationalEqual(string s, string t) {
        auto f1 = toFraction(s);
        auto f2 = toFraction(t);
        return f1.first == f2.first && f1.second == f2.second;
    }
};
```

## Java

```java
class Solution {
    private static class Fraction {
        BigInteger num;
        BigInteger den;
        Fraction(BigInteger n, BigInteger d) {
            if (d.signum() < 0) {
                n = n.negate();
                d = d.negate();
            }
            BigInteger g = n.gcd(d);
            this.num = n.divide(g);
            this.den = d.divide(g);
        }
    }

    public boolean isRationalEqual(String s, String t) {
        Fraction f1 = parse(s);
        Fraction f2 = parse(t);
        return f1.num.equals(f2.num) && f1.den.equals(f2.den);
    }

    private Fraction parse(String s) {
        int dotPos = s.indexOf('.');
        String intPartStr;
        String afterDot = "";
        if (dotPos == -1) {
            intPartStr = s;
        } else {
            intPartStr = s.substring(0, dotPos);
            afterDot = s.substring(dotPos + 1);
        }

        String nonRepeat = "";
        String repeat = "";

        int lParen = afterDot.indexOf('(');
        if (lParen != -1) {
            int rParen = afterDot.indexOf(')', lParen);
            nonRepeat = afterDot.substring(0, lParen);
            repeat = afterDot.substring(lParen + 1, rParen);
        } else {
            nonRepeat = afterDot;
        }

        BigInteger I = new BigInteger(intPartStr);
        int n = nonRepeat.length();
        int r = repeat.length();

        BigInteger tenPowN = BigInteger.TEN.pow(n);

        if (r == 0) { // no repeating part
            BigInteger NR = n == 0 ? BigInteger.ZERO : new BigInteger(nonRepeat);
            BigInteger denom = tenPowN;
            BigInteger num = I.multiply(denom).add(NR);
            return new Fraction(num, denom);
        } else {
            BigInteger NR = n == 0 ? BigInteger.ZERO : new BigInteger(nonRepeat);
            BigInteger R = new BigInteger(repeat);
            BigInteger tenPowR = BigInteger.TEN.pow(r);
            BigInteger repeatDenomFactor = tenPowR.subtract(BigInteger.ONE); // 10^r - 1
            BigInteger denom = tenPowN.multiply(repeatDenomFactor);
            BigInteger numFractionPart = NR.multiply(repeatDenomFactor).add(R);
            BigInteger num = I.multiply(denom).add(numFractionPart);
            return new Fraction(num, denom);
        }
    }
}
```

## Python

```python
class Solution(object):
    def isRationalEqual(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def parse(num):
            if '.' in num:
                int_part, rest = num.split('.', 1)
            else:
                int_part, rest = num, ''
            if '(' in rest:
                idx = rest.find('(')
                nonrep = rest[:idx]
                rep = rest[idx+1:-1]  # strip parentheses
            else:
                nonrep = rest
                rep = ''
            a = int(int_part)

            n = len(nonrep)
            pow_n = 10 ** n

            if not rep:  # terminating decimal
                denom = pow_n
                frac_num = int(nonrep) if nonrep else 0
                numer = a * denom + frac_num
                return numer, denom

            k = len(rep)
            pow_k = 10 ** k
            num_nonrep = int(nonrep) if nonrep else 0
            bc_str = nonrep + rep
            num_bc = int(bc_str) if bc_str else 0

            denom = pow_n * (pow_k - 1)
            frac_num = num_bc - num_nonrep
            numer = a * denom + frac_num
            return numer, denom

        n1, d1 = parse(s)
        n2, d2 = parse(t)
        return n1 * d2 == n2 * d1
```

## Python3

```python
import math

class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def to_fraction(num_str: str):
            # split integer and fractional parts
            if '.' in num_str:
                int_part, frac = num_str.split('.', 1)
            else:
                int_part, frac = num_str, ''
            # split non-repeating and repeating parts
            if '(' in frac:
                nonrep, rep = frac.split('(', 1)
                rep = rep.rstrip(')')
            else:
                nonrep, rep = frac, ''
            A = int(int_part) if int_part else 0

            n = len(nonrep)
            if rep:
                rlen = len(rep)
                pow10_n = 10 ** n
                pow10_r = 10 ** rlen
                # integer values of parts
                nonrep_val = int(nonrep) if nonrep else 0
                combined_val = int((nonrep + rep)) if (nonrep + rep) else 0
                num_frac = combined_val - nonrep_val
                den_frac = pow10_n * (pow10_r - 1)
            else:
                if n == 0:
                    return A, 1
                num_frac = int(nonrep)
                den_frac = 10 ** n

            num_total = A * den_frac + num_frac
            g = math.gcd(num_total, den_frac)
            return num_total // g, den_frac // g

        n1, d1 = to_fraction(s)
        n2, d2 = to_fraction(t)
        return n1 == n2 and d1 == d2
```

## C

```c
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <string.h>

static long long pow10_int(int k) {
    long long r = 1;
    while (k--) r *= 10;
    return r;
}

static long long str_to_ll(const char *s, int len) {
    long long v = 0;
    for (int i = 0; i < len; ++i) {
        v = v * 10 + (s[i] - '0');
    }
    return v;
}

static long long gcd_ll(long long a, long long b) {
    while (b) {
        long long t = a % b;
        a = b;
        b = t;
    }
    return a < 0 ? -a : a;
}

typedef struct {
    long long num;
    long long den;
} Fraction;

static Fraction parse(const char *s) {
    const char *dot = strchr(s, '.');
    const char *lparen = NULL;
    const char *rparen = NULL;
    int int_len, non_len = 0, rep_len = 0;
    long long I = 0, A = 0, B = 0;

    if (!dot) {
        // pure integer
        int_len = (int)strlen(s);
        I = str_to_ll(s, int_len);
        return (Fraction){I, 1};
    }

    int_len = (int)(dot - s);
    I = str_to_ll(s, int_len);

    const char *after_dot = dot + 1;
    lparen = strchr(after_dot, '(');
    if (lparen) {
        rparen = strchr(lparen, ')');
        non_len = (int)(lparen - after_dot);
        rep_len = (int)(rparen - lparen - 1);
        if (non_len > 0)
            A = str_to_ll(after_dot, non_len);
        if (rep_len > 0)
            B = str_to_ll(lparen + 1, rep_len);
    } else {
        // no repeating part
        const char *end = after_dot + strlen(after_dot);
        non_len = (int)(end - after_dot);
        if (non_len > 0)
            A = str_to_ll(after_dot, non_len);
    }

    Fraction f;
    if (rep_len == 0) {
        long long den = pow10_int(non_len);
        long long num = I * den + A;
        long long g = gcd_ll(num, den);
        f.num = num / g;
        f.den = den / g;
    } else {
        long long powA = pow10_int(non_len);
        long long powB = pow10_int(rep_len);
        long long AB = A * powB + B;               // concatenated A and B
        long long numeratorFraction = AB - A;
        long long denominatorFraction = powA * (powB - 1);
        long long num = I * denominatorFraction + numeratorFraction;
        long long den = denominatorFraction;
        long long g = gcd_ll(num, den);
        f.num = num / g;
        f.den = den / g;
    }
    return f;
}

bool isRationalEqual(char* s, char* t) {
    Fraction f1 = parse(s);
    Fraction f2 = parse(t);
    __int128 left = (__int128)f1.num * f2.den;
    __int128 right = (__int128)f2.num * f1.den;
    return left == right;
}
```

## Csharp

```csharp
using System;

public class Solution
{
    public bool IsRationalEqual(string s, string t)
    {
        var f1 = GetFraction(s);
        var f2 = GetFraction(t);
        return f1.num == f2.num && f1.den == f2.den;
    }

    private (long num, long den) GetFraction(string str)
    {
        int dotIdx = str.IndexOf('.');
        int lParenIdx = str.IndexOf('(');
        int rParenIdx = str.IndexOf(')');

        string intPartStr;
        if (dotIdx != -1)
            intPartStr = str.Substring(0, dotIdx);
        else if (lParenIdx != -1)
            intPartStr = str.Substring(0, lParenIdx);
        else
            intPartStr = str;

        long integerPart = ParseLong(intPartStr);

        string nonRep = "";
        if (dotIdx != -1)
        {
            int start = dotIdx + 1;
            int end = (lParenIdx != -1) ? lParenIdx : str.Length;
            if (end > start)
                nonRep = str.Substring(start, end - start);
        }

        string rep = "";
        if (lParenIdx != -1 && rParenIdx != -1 && rParenIdx > lParenIdx + 1)
            rep = str.Substring(lParenIdx + 1, rParenIdx - lParenIdx - 1);

        int n = nonRep.Length;
        int r = rep.Length;

        long powN = Pow10(n);
        if (r == 0)
        {
            long denominator = powN;
            long numerator = integerPart * denominator + ParseLong(nonRep);
            long g = Gcd(numerator, denominator);
            return (numerator / g, denominator / g);
        }
        else
        {
            long powR = Pow10(r);
            long denominator = powN * (powR - 1);
            long bVal = ParseLong(nonRep);
            long cVal = ParseLong(rep);
            long numerator = integerPart * denominator + bVal * (powR - 1) + cVal;
            long g = Gcd(numerator, denominator);
            return (numerator / g, denominator / g);
        }
    }

    private static long Pow10(int exp)
    {
        long result = 1;
        for (int i = 0; i < exp; i++) result *= 10;
        return result;
    }

    private static long ParseLong(string s)
    {
        if (string.IsNullOrEmpty(s)) return 0;
        return long.Parse(s);
    }

    private static long Gcd(long a, long b)
    {
        a = Math.Abs(a);
        b = Math.Abs(b);
        while (b != 0)
        {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isRationalEqual = function(s, t) {
    const toFraction = (str) => {
        let intPart = "", nonRep = "", rep = "";
        const dotIdx = str.indexOf('.');
        if (dotIdx === -1) {
            intPart = str;
        } else {
            intPart = str.substring(0, dotIdx);
            const after = str.substring(dotIdx + 1);
            const lpar = after.indexOf('(');
            if (lpar !== -1) {
                nonRep = after.substring(0, lpar);
                const rpar = after.indexOf(')', lpar);
                rep = after.substring(lpar + 1, rpar);
            } else {
                nonRep = after;
            }
        }

        const toBigInt = (s) => s === "" ? 0n : BigInt(s);

        if (rep === "") { // terminating decimal
            const n = nonRep.length;
            const pow10n = 10n ** BigInt(n);
            const numerator = toBigInt(intPart) * pow10n + toBigInt(nonRep);
            const denominator = pow10n;
            return reduce(numerator, denominator);
        } else { // repeating decimal
            const n = nonRep.length;
            const r = rep.length;
            const pow10_n = 10n ** BigInt(n);
            const pow10_nr = 10n ** BigInt(n + r);

            const N = toBigInt(intPart + nonRep + rep);
            const M = toBigInt(intPart + nonRep);
            const numerator = N - M;
            const denominator = pow10_nr - pow10_n;
            return reduce(numerator, denominator);
        }
    };

    const gcd = (a, b) => {
        while (b !== 0n) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };

    const reduce = (num, den) => {
        if (num === 0n) return [0n, 1n];
        const g = gcd(num < 0n ? -num : num, den);
        return [num / g, den / g];
    };

    const [n1, d1] = toFraction(s);
    const [n2, d2] = toFraction(t);
    return n1 * d2 === n2 * d1;
};
```

## Typescript

```typescript
function isRationalEqual(s: string, t: string): boolean {
    const parse = (str: string): [bigint, bigint] => {
        // split integer and fractional parts
        const dotIdx = str.indexOf('.');
        let intPartStr: string;
        let fracPart: string;
        if (dotIdx === -1) {
            intPartStr = str;
            fracPart = "";
        } else {
            intPartStr = str.substring(0, dotIdx);
            fracPart = str.substring(dotIdx + 1);
        }
        if (intPartStr.length === 0) intPartStr = "0";

        // extract non‑repeating and repeating parts
        let nonrep = "";
        let rep = "";
        const lparen = fracPart.indexOf('(');
        if (lparen !== -1) {
            nonrep = fracPart.substring(0, lparen);
            const rparen = fracPart.indexOf(')', lparen);
            rep = fracPart.substring(lparen + 1, rparen);
        } else {
            nonrep = fracPart;
        }

        const I = BigInt(intPartStr);
        const a = nonrep.length;
        const b = rep.length;

        // helper for power of 10
        const pow10 = (exp: number): bigint => 10n ** BigInt(exp);

        let num: bigint, den: bigint;

        if (b === 0) { // no repeating part
            if (a === 0) {
                // pure integer
                return [I, 1n];
            }
            const powA = pow10(a);
            const nonrepNum = BigInt(nonrep);
            den = powA;
            num = I * den + nonrepNum;
        } else { // has repeating part
            const powA = pow10(a);
            const powB = pow10(b);
            den = powA * (powB - 1n); // denominator for fractional part
            const nonrepNum = a === 0 ? 0n : BigInt(nonrep);
            const repNum = BigInt(rep);
            const fracNum = nonrepNum * (powB - 1n) + repNum;
            num = I * den + fracNum;
        }

        // reduce fraction
        const gcd = (x: bigint, y: bigint): bigint => {
            let a = x < 0n ? -x : x;
            let b = y < 0n ? -y : y;
            while (b !== 0n) {
                const t = a % b;
                a = b;
                b = t;
            }
            return a;
        };
        const g = gcd(num, den);
        return [num / g, den / g];
    };

    const f1 = parse(s);
    const f2 = parse(t);
    return f1[0] === f2[0] && f1[1] === f2[1];
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @param String $t
     * @return Boolean
     */
    function isRationalEqual($s, $t) {
        $f1 = $this->parse($s);
        $f2 = $this->parse($t);
        return $f1[0] == $f2[0] && $f1[1] == $f2[1];
    }

    private function parse(string $s): array {
        if (strpos($s, '.') !== false) {
            [$intPart, $after] = explode('.', $s, 2);
            $nonrep = '';
            $rep = '';
            $posParen = strpos($after, '(');
            if ($posParen !== false) {
                $nonrep = substr($after, 0, $posParen);
                $endParen = strpos($after, ')', $posParen);
                $rep = substr($after, $posParen + 1, $endParen - $posParen - 1);
            } else {
                $nonrep = $after;
            }
        } else {
            $intPart = $s;
            $nonrep = '';
            $rep = '';
        }

        $I = intval($intPart);
        $n = strlen($nonrep);
        $k = strlen($rep);

        if ($k > 0) {
            $fullStr = $nonrep . $rep;
            $num1 = $fullStr === '' ? 0 : intval($fullStr);
            $num2 = $nonrep === '' ? 0 : intval($nonrep);
            $numerator_frac = $num1 - $num2;
            $denominator_frac = $this->pow10($n + $k) - $this->pow10($n);
        } elseif ($n > 0) {
            $numerator_frac = $nonrep === '' ? 0 : intval($nonrep);
            $denominator_frac = $this->pow10($n);
        } else {
            return [$I, 1];
        }

        $numerator_total = $I * $denominator_frac + $numerator_frac;
        $denominator_total = $denominator_frac;

        $g = $this->gcd($numerator_total, $denominator_total);
        return [intdiv($numerator_total, $g), intdiv($denominator_total, $g)];
    }

    private function pow10(int $e): int {
        $r = 1;
        while ($e-- > 0) {
            $r *= 10;
        }
        return $r;
    }

    private function gcd(int $a, int $b): int {
        while ($b != 0) {
            $tmp = $a % $b;
            $a = $b;
            $b = $tmp;
        }
        return $a;
    }
}
```

## Swift

```swift
class Solution {
    func isRationalEqual(_ s: String, _ t: String) -> Bool {
        let f1 = fraction(from: s)
        let f2 = fraction(from: t)
        return f1.num == f2.num && f1.den == f2.den
    }
    
    private func fraction(from str: String) -> (num: Int64, den: Int64) {
        var intPartStr = ""
        var fracPart = ""
        if let dotIdx = str.firstIndex(of: ".") {
            intPartStr = String(str[..<dotIdx])
            let afterDotIdx = str.index(after: dotIdx)
            if afterDotIdx < str.endIndex {
                fracPart = String(str[afterDotIdx...])
            }
        } else {
            intPartStr = str
        }
        
        let a = Int64(intPartStr) ?? 0
        
        if let lParenIdx = fracPart.firstIndex(of: "(") {
            // repeating part exists
            let nonRepStr = String(fracPart[..<lParenIdx])
            let rParenIdx = fracPart.firstIndex(of: ")")!
            let repStart = fracPart.index(after: lParenIdx)
            let repStr = String(fracPart[repStart..<rParenIdx])
            
            let m = nonRepStr.count
            let k = repStr.count
            
            let pow10m = intPow10(m)
            let pow10k = intPow10(k)
            
            let bn: Int64 = nonRepStr.isEmpty ? 0 : Int64(nonRepStr)!
            let cn: Int64 = Int64(repStr)!
            
            // denominator D = 10^m * (10^k - 1)
            let denom = pow10m * (pow10k - 1)
            var numerator = a * denom
            numerator += bn * (pow10k - 1) + cn
            
            let g = gcd(abs(numerator), denom)
            return (numerator / g, denom / g)
        } else {
            // no repeating part
            let nonRepStr = fracPart
            let m = nonRepStr.count
            let pow10m = intPow10(m)
            
            let bn: Int64 = nonRepStr.isEmpty ? 0 : Int64(nonRepStr)!
            var numerator = a * pow10m + bn
            var denominator = pow10m
            
            let g = gcd(abs(numerator), denominator)
            return (numerator / g, denominator / g)
        }
    }
    
    private func intPow10(_ n: Int) -> Int64 {
        var result: Int64 = 1
        for _ in 0..<n { result *= 10 }
        return result
    }
    
    private func gcd(_ a: Int64, _ b: Int64) -> Int64 {
        var x = a
        var y = b
        while y != 0 {
            let temp = x % y
            x = y
            y = temp
        }
        return x
    }
    
    private func abs(_ v: Int64) -> Int64 { v >= 0 ? v : -v }
}
```

## Kotlin

```kotlin
import java.math.BigInteger

class Solution {
    fun isRationalEqual(s: String, t: String): Boolean {
        val f1 = parseFraction(s)
        val f2 = parseFraction(t)
        return f1.first == f2.first && f1.second == f2.second
    }

    private fun parseFraction(str: String): Pair<BigInteger, BigInteger> {
        val dotIdx = str.indexOf('.')
        val intPartStr: String
        val fracPart: String

        if (dotIdx == -1) {
            intPartStr = str
            fracPart = ""
        } else {
            intPartStr = str.substring(0, dotIdx)
            fracPart = str.substring(dotIdx + 1)
        }

        var nonRep = ""
        var repeat = ""

        if (fracPart.isNotEmpty()) {
            val parenIdx = fracPart.indexOf('(')
            if (parenIdx != -1) {
                nonRep = fracPart.substring(0, parenIdx)
                repeat = fracPart.substring(parenIdx + 1, fracPart.length - 1) // exclude ')'
            } else {
                nonRep = fracPart
            }
        }

        val integerPart = if (intPartStr.isEmpty()) BigInteger.ZERO else BigInteger(intPartStr)

        return if (repeat.isEmpty()) {
            // terminating decimal
            if (nonRep.isEmpty()) {
                Pair(integerPart, BigInteger.ONE)
            } else {
                val n = nonRep.length
                val denom = BigInteger.TEN.pow(n)
                val numFrac = BigInteger(nonRep)
                var numerator = integerPart.multiply(denom).add(numFrac)
                var denominator = denom
                val g = numerator.gcd(denominator)
                numerator = numerator.divide(g)
                denominator = denominator.divide(g)
                Pair(numerator, denominator)
            }
        } else {
            // repeating decimal
            val n = nonRep.length
            val k = repeat.length
            val powN = BigInteger.TEN.pow(n)
            val powK = BigInteger.TEN.pow(k)

            val concat = if (nonRep.isEmpty()) repeat else nonRep + repeat
            val x = BigInteger(concat)
            val y = if (nonRep.isEmpty()) BigInteger.ZERO else BigInteger(nonRep)

            val numeratorFrac = x.subtract(y) // x - y
            val denominatorFrac = powN.multiply(powK.subtract(BigInteger.ONE))

            var numerator = integerPart.multiply(denominatorFrac).add(numeratorFrac)
            var denominator = denominatorFrac

            val g = numerator.gcd(denominator)
            numerator = numerator.divide(g)
            denominator = denominator.divide(g)

            Pair(numerator, denominator)
        }
    }
}
```

## Dart

```dart
class Solution {
  bool isRationalEqual(String s, String t) {
    var f1 = _toFraction(s);
    var f2 = _toFraction(t);
    return f1[0] == f2[0] && f1[1] == f2[1];
  }

  List<int> _toFraction(String str) {
    int dotIdx = str.indexOf('.');
    String integerPart;
    String afterDot = '';
    if (dotIdx == -1) {
      integerPart = str;
    } else {
      integerPart = str.substring(0, dotIdx);
      afterDot = str.substring(dotIdx + 1);
    }

    String nonRep = '';
    String rep = '';
    int parenStart = afterDot.indexOf('(');
    if (parenStart != -1) {
      nonRep = afterDot.substring(0, parenStart);
      int parenEnd = afterDot.indexOf(')', parenStart);
      rep = afterDot.substring(parenStart + 1, parenEnd);
    } else {
      nonRep = afterDot;
    }

    int A = int.parse(integerPart);
    int bLen = nonRep.length;
    int cLen = rep.length;

    if (cLen == 0) {
      int denom = _pow10(bLen);
      int num = A * denom + (nonRep.isEmpty ? 0 : int.parse(nonRep));
      int g = _gcd(num, denom);
      return [num ~/ g, denom ~/ g];
    } else {
      String concat = nonRep + rep;
      int N = int.parse(concat);
      int M = nonRep.isEmpty ? 0 : int.parse(nonRep);
      int powB = _pow10(bLen);
      int powC = _pow10(cLen);
      int denom = powB * (powC - 1);
      int num = A * denom + (N - M);
      int g = _gcd(num, denom);
      return [num ~/ g, denom ~/ g];
    }
  }

  int _pow10(int n) {
    int res = 1;
    for (int i = 0; i < n; i++) res *= 10;
    return res;
  }

  int _gcd(int a, int b) {
    while (b != 0) {
      int tmp = a % b;
      a = b;
      b = tmp;
    }
    return a.abs();
  }
}
```

## Golang

```go
import (
	"strconv"
	"strings"
)

func isRationalEqual(s string, t string) bool {
	num1, den1 := parseFraction(s)
	num2, den2 := parseFraction(t)
	return num1 == num2 && den1 == den2
}

func parseFraction(str string) (int64, int64) {
	// split repeating part
	repStart := strings.IndexByte(str, '(')
	var repStr string
	prefix := str
	if repStart != -1 {
		repStr = str[repStart+1 : len(str)-1] // assume ends with ')'
		prefix = str[:repStart]
	}
	// split integer and non‑repeating part
	dotIdx := strings.IndexByte(prefix, '.')
	var intPartStr, nonRepStr string
	if dotIdx != -1 {
		intPartStr = prefix[:dotIdx]
		nonRepStr = prefix[dotIdx+1:]
	} else {
		intPartStr = prefix
		nonRepStr = ""
	}
	intPart := parseInt(intPartStr)
	n := len(nonRepStr)
	r := len(repStr)

	if r == 0 { // terminating decimal
		den := pow10(n)
		num := intPart*den + parseInt(nonRepStr)
		g := gcd(num, den)
		return num / g, den / g
	}

	// repeating decimal
	N := parseInt(nonRepStr)          // non‑repeating digits as integer (0 if empty)
	R := parseInt(repStr)             // repeating digits as integer
	powN := pow10(n)                  // 10^n
	powR := pow10(r)                  // 10^r
	den := powN * (powR - 1)          // denominator
	num := intPart*den + N*(powR-1) + R // numerator
	g := gcd(num, den)
	return num / g, den / g
}

func parseInt(s string) int64 {
	if s == "" {
		return 0
	}
	val, _ := strconv.ParseInt(s, 10, 64)
	return val
}

func pow10(e int) int64 {
	var res int64 = 1
	for i := 0; i < e; i++ {
		res *= 10
	}
	return res
}

func gcd(a, b int64) int64 {
	if a < 0 {
		a = -a
	}
	if b < 0 {
		b = -b
	}
	for b != 0 {
		a, b = b, a%b
	}
	if a == 0 {
		return 1
	}
	return a
}
```

## Ruby

```ruby
def parse_fraction(str)
  int_part = ''
  frac_part = ''
  if str.include?('.')
    int_part, rest = str.split('.', 2)
    frac_part = rest
  else
    int_part = str
    frac_part = ''
  end

  non_repeat = ''
  repeat = ''

  if idx = frac_part.index('(')
    non_repeat = frac_part[0...idx]
    repeat = frac_part[(idx + 1)...-1] # exclude '(' and ')'
  else
    non_repeat = frac_part
    repeat = ''
  end

  a = int_part.to_i
  b_len = non_repeat.length
  pow_b = 10 ** b_len
  b_int = b_len > 0 ? non_repeat.to_i : 0

  if repeat.empty?
    denom = pow_b
    num = a * denom + b_int
  else
    c_len = repeat.length
    pow_c = 10 ** c_len
    repeat_int = repeat.to_i
    denom = pow_b * (pow_c - 1)
    frac_num = b_int * (pow_c - 1) + repeat_int
    num = a * denom + frac_num
  end

  g = num.gcd(denom)
  [num / g, denom / g]
end

# @param {String} s
# @param {String} t
# @return {Boolean}
def is_rational_equal(s, t)
  n1, d1 = parse_fraction(s)
  n2, d2 = parse_fraction(t)
  n1 == n2 && d1 == d2
end
```

## Scala

```scala
object Solution {
  import scala.math.BigInt

  private def parseFraction(str: String): (BigInt, BigInt) = {
    val dotIdx = str.indexOf('.')
    var intPartStr = ""
    var nonRep = ""
    var rep = ""

    if (dotIdx == -1) {
      intPartStr = str
    } else {
      intPartStr = str.substring(0, dotIdx)
      val afterDot = str.substring(dotIdx + 1)
      val parenIdx = afterDot.indexOf('(')
      if (parenIdx == -1) {
        nonRep = afterDot // may be empty
      } else {
        nonRep = afterDot.substring(0, parenIdx)
        val closeIdx = afterDot.indexOf(')', parenIdx)
        rep = afterDot.substring(parenIdx + 1, closeIdx)
      }
    }

    val a = BigInt(intPartStr)
    val lenB = nonRep.length
    val powB = BigInt(10).pow(lenB)

    if (rep.isEmpty) {
      // No repeating part
      val bVal = if (nonRep.isEmpty) BigInt(0) else BigInt(nonRep)
      val denom = powB
      val numer = a * denom + bVal
      val g = numer.gcd(denom)
      (numer / g, denom / g)
    } else {
      // With repeating part
      val lenC = rep.length
      val powC = BigInt(10).pow(lenC)
      val cVal = BigInt(rep)
      val bVal = if (nonRep.isEmpty) BigInt(0) else BigInt(nonRep)

      val denom = powB * (powC - 1)
      val numer = a * denom + bVal * (powC - 1) + cVal
      val g = numer.gcd(denom)
      (numer / g, denom / g)
    }
  }

  def isRationalEqual(s: String, t: String): Boolean = {
    val (n1, d1) = parseFraction(s)
    val (n2, d2) = parseFraction(t)
    n1 == n2 && d1 == d2
  }
}
```

## Rust

```rust
impl Solution {
    pub fn is_rational_equal(s: String, t: String) -> bool {
        fn gcd(mut a: i128, mut b: i128) -> i128 {
            while b != 0 {
                let r = a % b;
                a = b;
                b = r;
            }
            a.abs()
        }

        fn parse(num_str: &str) -> (i128, i128) {
            // split integer and fractional part
            let (int_part, frac_part) = if let Some(dot_idx) = num_str.find('.') {
                (&num_str[..dot_idx], &num_str[dot_idx + 1..])
            } else {
                (num_str, "")
            };
            let a: i128 = int_part.parse().unwrap();

            // split non‑repeating and repeating parts
            let (nonrep, rep) = if let Some(lparen) = frac_part.find('(') {
                let rparen = frac_part.find(')').unwrap();
                (&frac_part[..lparen], &frac_part[lparen + 1..rparen])
            } else {
                (frac_part, "")
            };

            let lenb = nonrep.len() as u32;
            let lenc = rep.len() as u32;

            let b: i128 = if nonrep.is_empty() { 0 } else { nonrep.parse().unwrap() };
            let c: i128 = if rep.is_empty() { 0 } else { rep.parse().unwrap() };

            let pow10_lenb = 10_i128.pow(lenb);
            if lenc == 0 {
                // No repeating part
                let denom = pow10_lenb;
                let num = a * denom + b;
                let g = gcd(num, denom);
                (num / g, denom / g)
            } else {
                // With repeating part
                let pow10_lenc = 10_i128.pow(lenc);
                let repeat_factor = pow10_lenc - 1; // 10^k - 1
                let denom = pow10_lenb * repeat_factor;
                let num = a * denom + b * repeat_factor + c;
                let g = gcd(num, denom);
                (num / g, denom / g)
            }
        }

        let (n1, d1) = parse(&s);
        let (n2, d2) = parse(&t);
        n1 == n2 && d1 == d2
    }
}
```

## Racket

```racket
(define/contract (is-rational-equal s t)
  (-> string? string? boolean?)
  (define (str->bigint st)
    (if (= (string-length st) 0)
        0
        (string->number st)))
  (define (parse-rational str)
    ;; extract repeating part if any
    (let* ((open-pos (string-index-of str #\())
           (close-pos (and open-pos (string-index-of str #\) open-pos))))
      (let* ((rep-str (if open-pos
                          (substring str (+ open-pos 1) close-pos)
                          ""))
             (rep-exists? (not (zero? (string-length rep-str))))
             ;; remove parentheses for further processing
             (clean-str (if open-pos
                            (string-append (substring str 0 open-pos)
                                           (substring str (+ close-pos 1)))
                            str))
             (dot-pos (string-index-of clean-str #\.))
             (int-str (cond [(and dot-pos (> dot-pos 0)) (substring clean-str 0 dot-pos)]
                           [dot-pos ""]
                           [else clean-str]))
             (frac-part (if dot-pos
                            (substring clean-str (+ dot-pos 1))
                            ""))
             (nonrep-str frac-part)
             (len-nr (string-length nonrep-str))
             (int-part (str->bigint int-str))
             (nonrep-val (str->bigint nonrep-str))
             (den-nr (expt 10 len-nr))
             (base (+ int-part (/ nonrep-val den-nr))))
        (if rep-exists?
            (let* ((len-r (string-length rep-str))
                   (rep-val (str->bigint rep-str))
                   (den-rep (* den-nr (- (expt 10 len-r) 1)))
                   (add (/ rep-val den-rep)))
              (+ base add))
            base))))
  (= (parse-rational s) (parse-rational t)))
```

## Erlang

```erlang
-module(solution).
-export([is_rational_equal/2]).

-spec is_rational_equal(unicode:unicode_binary(), unicode:unicode_binary()) -> boolean().
is_rational_equal(S, T) ->
    {N1, D1} = fraction(S),
    {N2, D2} = fraction(T),
    N1 * D2 =:= N2 * D1.

fraction(Str) ->
    Pattern = <<"^(\\d+)(?:\\.(\\d*)(?:\\((\\d+)\\))?)?$">>,
    case re:run(Str, Pattern, [{capture, all_but_first, binary}]) of
        {match, [IntBin, NonRepBinOrUndef, RepBinOrUndef]} ->
            Int = binary_to_integer(IntBin),
            NonRepBin = case NonRepBinOrUndef of undefined -> <<>>; _ -> NonRepBinOrUndef end,
            RepBin = case RepBinOrUndef of undefined -> <<>>; _ -> RepBinOrUndef end,
            ALen = byte_size(NonRepBin),
            BLen = byte_size(RepBin),
            NonRepInt = if ALen == 0 -> 0; true -> binary_to_integer(NonRepBin) end,
            RepInt = if BLen == 0 -> 0; true -> binary_to_integer(RepBin) end,
            case BLen of
                0 ->
                    Den = pow10(ALen),
                    Num = Int * Den + NonRepInt,
                    {Num, Den};
                _ ->
                    PowA = pow10(ALen),
                    PowB = pow10(BLen),
                    Den = PowA * (PowB - 1),
                    NumFrac = NonRepInt * (PowB - 1) + RepInt,
                    Num = Int * Den + NumFrac,
                    {Num, Den}
            end
    end.

pow10(N) when N >= 0 -> pow10(N, 1).

pow10(0, Acc) -> Acc;
pow10(N, Acc) when N > 0 -> pow10(N - 1, Acc * 10).
```

## Elixir

```elixir
defmodule Solution do
  @spec is_rational_equal(s :: String.t(), t :: String.t()) :: boolean()
  def is_rational_equal(s, t) do
    {n1, d1} = s |> parse_fraction() |> reduce()
    {n2, d2} = t |> parse_fraction() |> reduce()
    n1 == n2 and d1 == d2
  end

  defp parse_fraction(str) do
    case String.split(str, ".", parts: 2) do
      [int_part] ->
        i = String.to_integer(int_part)
        {i, 1}

      [int_part, rest] ->
        {nonrep, rep} = extract_parts(rest)
        build_fraction(int_part, nonrep, rep)
    end
  end

  defp extract_parts(rest) do
    if String.contains?(rest, "(") do
      [nonrep, rep_with_paren] = String.split(rest, "(", parts: 2)
      rep = String.trim_trailing(rep_with_paren, ")")
      {nonrep, rep}
    else
      {rest, ""}
    end
  end

  defp build_fraction(int_str, nonrep, rep) do
    i = String.to_integer(int_str)
    n_len = byte_size(nonrep)
    k_len = byte_size(rep)

    cond do
      k_len == 0 ->
        if n_len == 0 do
          {i, 1}
        else
          a = String.to_integer(nonrep)
          denom = pow10(n_len)
          num = i * denom + a
          {num, denom}
        end

      true ->
        a = if n_len == 0, do: 0, else: String.to_integer(nonrep)
        b = String.to_integer(rep)

        pow_n = pow10(n_len)
        pow_k = pow10(k_len)

        numerator_frac = a * (pow_k - 1) + b
        denominator_frac = pow_n * (pow_k - 1)

        num = i * denominator_frac + numerator_frac
        den = denominator_frac
        {num, den}
    end
  end

  defp pow10(0), do: 1
  defp pow10(n) when n > 0, do: 10 * pow10(n - 1)

  defp reduce({num, den}) do
    g = Integer.gcd(num, den)
    {div(num, g), div(den, g)}
  end
end
```
