# 0592. Fraction Addition and Subtraction

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string fractionAddition(string expression) {
        long long num = 0, den = 1; // current result numerator/denominator
        int n = expression.size();
        for (int i = 0; i < n; ) {
            int sign = 1;
            if (expression[i] == '+') { sign = 1; ++i; }
            else if (expression[i] == '-') { sign = -1; ++i; }

            long long a = 0;
            while (i < n && isdigit(expression[i])) {
                a = a * 10 + (expression[i] - '0');
                ++i;
            }
            a *= sign;

            // skip '/'
            if (i < n && expression[i] == '/') ++i;

            long long b = 0;
            while (i < n && isdigit(expression[i])) {
                b = b * 10 + (expression[i] - '0');
                ++i;
            }

            long long newNum = num * b + a * den;
            long long newDen = den * b;
            long long g = std::gcd(newNum, newDen);
            if (g != 0) {
                newNum /= g;
                newDen /= g;
            }
            num = newNum;
            den = newDen;
        }

        if (num == 0) return "0/1";
        return to_string(num) + "/" + to_string(den);
    }
};
```

## Java

```java
class Solution {
    public String fractionAddition(String expression) {
        long numerator = 0;
        long denominator = 1;
        int i = 0;
        int n = expression.length();
        while (i < n) {
            // sign
            int sign = 1;
            char c = expression.charAt(i);
            if (c == '+' || c == '-') {
                sign = (c == '+') ? 1 : -1;
                i++;
            }
            // parse numerator
            long curNum = 0;
            while (i < n && Character.isDigit(expression.charAt(i))) {
                curNum = curNum * 10 + (expression.charAt(i) - '0');
                i++;
            }
            // skip '/'
            i++; // expression.charAt(i-1) is '/', guaranteed
            // parse denominator
            long curDen = 0;
            while (i < n && Character.isDigit(expression.charAt(i))) {
                curDen = curDen * 10 + (expression.charAt(i) - '0');
                i++;
            }
            curNum *= sign;
            // add current fraction to result
            numerator = numerator * curDen + curNum * denominator;
            denominator = denominator * curDen;
            long g = gcd(Math.abs(numerator), denominator);
            if (g != 0) {
                numerator /= g;
                denominator /= g;
            }
        }
        if (numerator == 0) return "0/1";
        return numerator + "/" + denominator;
    }

    private long gcd(long a, long b) {
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return Math.abs(a);
    }
}
```

## Python

```python
class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        from math import gcd

        i, n = 0, len(expression)
        num, den = 0, 1  # running result

        while i < n:
            sign = 1
            if expression[i] == '+' or expression[i] == '-':
                sign = 1 if expression[i] == '+' else -1
                i += 1

            # parse numerator
            num_cur = 0
            while i < n and expression[i].isdigit():
                num_cur = num_cur * 10 + int(expression[i])
                i += 1
            num_cur *= sign

            # skip '/'
            i += 1  # assume always valid

            # parse denominator
            den_cur = 0
            while i < n and expression[i].isdigit():
                den_cur = den_cur * 10 + int(expression[i])
                i += 1

            # add current fraction to result
            num = num * den_cur + num_cur * den
            den = den * den_cur

            # reduce intermediate result to keep numbers small
            g = gcd(abs(num), den)
            if g > 1:
                num //= g
                den //= g

        # final reduction (in case)
        g = gcd(abs(num), den)
        num //= g
        den //= g
        return f"{num}/{den}"
```

## Python3

```python
class Solution:
    def fractionAddition(self, expression: str) -> str:
        import math
        num, den = 0, 1
        i, n = 0, len(expression)
        while i < n:
            sign = 1
            if expression[i] in '+-':
                if expression[i] == '-':
                    sign = -1
                i += 1
            j = i
            while j < n and expression[j].isdigit():
                j += 1
            cur_num = int(expression[i:j]) * sign
            i = j + 1  # skip '/'
            k = i
            while k < n and expression[k].isdigit():
                k += 1
            cur_den = int(expression[i:k])
            i = k
            num = num * cur_den + cur_num * den
            den = den * cur_den
            g = math.gcd(abs(num), den)
            if g > 1:
                num //= g
                den //= g
        return f"{num}/{den}"
```

## C

```c
#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>

static long long gcd_ll(long long a, long long b) {
    if (a < 0) a = -a;
    if (b < 0) b = -b;
    while (b) {
        long long t = a % b;
        a = b;
        b = t;
    }
    return a;
}

char* fractionAddition(char* expression) {
    long long num = 0;   // numerator of the running total
    long long den = 1;   // denominator of the running total

    char *p = expression;
    while (*p) {
        int sign = 1;
        if (*p == '+') {
            sign = 1;
            p++;
        } else if (*p == '-') {
            sign = -1;
            p++;
        }

        long long curNum = 0;
        while (isdigit(*p)) {
            curNum = curNum * 10 + (*p - '0');
            p++;
        }
        curNum *= sign;

        if (*p == '/') p++;   // skip '/'

        long long curDen = 0;
        while (isdigit(*p)) {
            curDen = curDen * 10 + (*p - '0');
            p++;
        }

        long long new_num = num * curDen + curNum * den;
        long long new_den = den * curDen;

        long long g = gcd_ll(new_num, new_den);
        if (g != 0) {
            new_num /= g;
            new_den /= g;
        }
        num = new_num;
        den = new_den;
    }

    long long final_gcd = gcd_ll(num, den);
    if (final_gcd != 0) {
        num /= final_gcd;
        den /= final_gcd;
    }

    if (den < 0) {   // keep denominator positive
        den = -den;
        num = -num;
    }

    char *result = (char *)malloc(50);
    sprintf(result, "%lld/%lld", num, den);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public string FractionAddition(string expression)
    {
        long num = 0;
        long den = 1;
        int i = 0;
        int n = expression.Length;

        while (i < n)
        {
            // sign
            int sign = 1;
            if (expression[i] == '+' || expression[i] == '-')
            {
                sign = expression[i] == '-' ? -1 : 1;
                i++;
            }

            // numerator
            long curNum = 0;
            while (i < n && char.IsDigit(expression[i]))
            {
                curNum = curNum * 10 + (expression[i] - '0');
                i++;
            }
            curNum *= sign;

            // skip '/'
            i++; // expression[i] is '/' guaranteed

            // denominator
            long curDen = 0;
            while (i < n && char.IsDigit(expression[i]))
            {
                curDen = curDen * 10 + (expression[i] - '0');
                i++;
            }

            // add curNum/curDen to num/den
            long newNum = num * curDen + curNum * den;
            long newDen = den * curDen;

            long g = Gcd(Math.Abs(newNum), newDen);
            num = newNum / g;
            den = newDen / g;
        }

        // final reduction (in case)
        long finalGcd = Gcd(Math.Abs(num), den);
        num /= finalGcd;
        den /= finalGcd;

        return $"{num}/{den}";
    }

    private long Gcd(long a, long b)
    {
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
 * @param {string} expression
 * @return {string}
 */
var fractionAddition = function(expression) {
    const gcd = (a, b) => {
        a = Math.abs(a);
        b = Math.abs(b);
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    
    const isDigit = ch => ch >= '0' && ch <= '9';
    
    let num = 0; // numerator of running total
    let den = 1; // denominator of running total
    let i = 0;
    const n = expression.length;
    
    while (i < n) {
        let sign = 1;
        if (expression[i] === '+') {
            sign = 1;
            i++;
        } else if (expression[i] === '-') {
            sign = -1;
            i++;
        }
        
        // parse numerator
        let a = 0;
        while (i < n && isDigit(expression[i])) {
            a = a * 10 + (expression.charCodeAt(i) - 48);
            i++;
        }
        a *= sign;
        
        // skip '/'
        i++; // assume valid '/'
        
        // parse denominator
        let b = 0;
        while (i < n && isDigit(expression[i])) {
            b = b * 10 + (expression.charCodeAt(i) - 48);
            i++;
        }
        
        // combine fractions: num/den + a/b
        num = num * b + a * den;
        den = den * b;
        
        const g = gcd(num, den);
        if (g !== 0) {
            num /= g;
            den /= g;
        }
    }
    
    if (den < 0) {
        den = -den;
        num = -num;
    }
    
    return `${num}/${den}`;
};
```

## Typescript

```typescript
function fractionAddition(expression: string): string {
    const gcd = (a: number, b: number): number => {
        a = Math.abs(a);
        b = Math.abs(b);
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };

    let i = 0;
    const n = expression.length;
    let num = 0; // numerator of accumulated result
    let den = 1; // denominator of accumulated result

    while (i < n) {
        // sign
        let sign = 1;
        if (expression[i] === '+' || expression[i] === '-') {
            sign = expression[i] === '-' ? -1 : 1;
            i++;
        }

        // numerator
        let curNum = 0;
        while (i < n && expression[i] >= '0' && expression[i] <= '9') {
            curNum = curNum * 10 + (expression.charCodeAt(i) - 48);
            i++;
        }
        curNum *= sign;

        // skip '/'
        i++; // assume valid input, so '/' exists

        // denominator
        let curDen = 0;
        while (i < n && expression[i] >= '0' && expression[i] <= '9') {
            curDen = curDen * 10 + (expression.charCodeAt(i) - 48);
            i++;
        }

        // combine fractions: num/den + curNum/curDen
        const newNum = num * curDen + curNum * den;
        const newDen = den * curDen;

        // reduce intermediate result to keep numbers small
        const g = gcd(newNum, newDen);
        num = newNum / g;
        den = newDen / g;
    }

    if (num === 0) {
        return "0/1";
    }
    const finalGcd = gcd(num, den);
    num /= finalGcd;
    den /= finalGcd;

    return `${num}/${den}`;
}
```

## Php

```php
class Solution {

    /**
     * @param String $expression
     * @return String
     */
    function fractionAddition($expression) {
        $len = strlen($expression);
        $i = 0;
        $num = 0;   // numerator of the running total
        $den = 1;   // denominator of the running total

        while ($i < $len) {
            $sign = 1;
            if ($expression[$i] === '+' || $expression[$i] === '-') {
                if ($expression[$i] === '-') {
                    $sign = -1;
                }
                $i++;
            }

            // parse numerator
            $currNum = 0;
            while ($i < $len && ctype_digit($expression[$i])) {
                $currNum = $currNum * 10 + intval($expression[$i]);
                $i++;
            }
            $currNum *= $sign;

            // skip '/'
            if ($i < $len && $expression[$i] === '/') {
                $i++;
            }

            // parse denominator
            $currDen = 0;
            while ($i < $len && ctype_digit($expression[$i])) {
                $currDen = $currDen * 10 + intval($expression[$i]);
                $i++;
            }

            // add current fraction to total
            $newNum = $num * $currDen + $currNum * $den;
            $newDen = $den * $currDen;

            $g = $this->gcd(abs($newNum), $newDen);
            $num = (int)($newNum / $g);
            $den = (int)($newDen / $g);
        }

        // ensure denominator positive
        if ($den < 0) {
            $den = -$den;
            $num = -$num;
        }

        return $num . '/' . $den;
    }

    private function gcd($a, $b) {
        while ($b != 0) {
            $tmp = $a % $b;
            $a = $b;
            $b = $tmp;
        }
        return $a == 0 ? 1 : abs($a);
    }
}
```

## Swift

```swift
class Solution {
    func fractionAddition(_ expression: String) -> String {
        var numeratorResult = 0
        var denominatorResult = 1
        let chars = Array(expression)
        var index = 0
        
        while index < chars.count {
            var sign = 1
            if chars[index] == "+" {
                sign = 1
                index += 1
            } else if chars[index] == "-" {
                sign = -1
                index += 1
            }
            
            // parse numerator
            var num = 0
            while index < chars.count, let digit = chars[index].wholeNumberValue {
                num = num * 10 + digit
                index += 1
            }
            num *= sign
            
            // skip '/'
            if index < chars.count && chars[index] == "/" {
                index += 1
            }
            
            // parse denominator
            var den = 0
            while index < chars.count, let digit = chars[index].wholeNumberValue {
                den = den * 10 + digit
                index += 1
            }
            
            // combine fractions: a/b + c/d = (a*d + c*b) / (b*d)
            let newNumerator = numeratorResult * den + num * denominatorResult
            let newDenominator = denominatorResult * den
            let g = gcd(abs(newNumerator), newDenominator)
            numeratorResult = newNumerator / g
            denominatorResult = newDenominator / g
        }
        
        return "\(numeratorResult)/\(denominatorResult)"
    }
    
    private func gcd(_ a: Int, _ b: Int) -> Int {
        var x = a
        var y = b
        while y != 0 {
            let temp = x % y
            x = y
            y = temp
        }
        return x == 0 ? 1 : x
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun fractionAddition(expression: String): String {
        var numerator = 0L
        var denominator = 1L
        var i = 0
        val n = expression.length

        while (i < n) {
            // sign
            var sign = 1
            if (expression[i] == '+') {
                sign = 1
                i++
            } else if (expression[i] == '-') {
                sign = -1
                i++
            }

            // parse numerator
            var curNum = 0L
            while (i < n && expression[i].isDigit()) {
                curNum = curNum * 10 + (expression[i] - '0')
                i++
            }
            curNum *= sign

            // skip '/'
            i++ // assume valid input, so this is '/'

            // parse denominator
            var curDen = 0L
            while (i < n && expression[i].isDigit()) {
                curDen = curDen * 10 + (expression[i] - '0')
                i++
            }

            // add fractions: numerator/denominator + curNum/curDen
            val newNumerator = numerator * curDen + curNum * denominator
            val newDenominator = denominator * curDen
            val g = gcd(kotlin.math.abs(newNumerator), newDenominator)
            numerator = newNumerator / g
            denominator = newDenominator / g
        }

        if (numerator == 0L) denominator = 1L
        return "${numerator}/${denominator}"
    }

    private fun gcd(a: Long, b: Long): Long {
        var x = a
        var y = b
        while (y != 0L) {
            val tmp = x % y
            x = y
            y = tmp
        }
        return kotlin.math.abs(x)
    }
}
```

## Dart

```dart
class Solution {
  String fractionAddition(String expression) {
    int i = 0;
    int n = expression.length;
    int num = 0; // numerator of the running total
    int den = 1; // denominator of the running total

    while (i < n) {
      int sign = 1;
      if (expression[i] == '+') {
        sign = 1;
        i++;
      } else if (expression[i] == '-') {
        sign = -1;
        i++;
      }

      // parse numerator
      int numer = 0;
      while (i < n && _isDigit(expression.codeUnitAt(i))) {
        numer = numer * 10 + (expression.codeUnitAt(i) - 48);
        i++;
      }

      // skip '/'
      i++;

      // parse denominator
      int denom = 0;
      while (i < n && _isDigit(expression.codeUnitAt(i))) {
        denom = denom * 10 + (expression.codeUnitAt(i) - 48);
        i++;
      }

      int currNum = sign * numer;
      int currDen = denom;

      // combine fractions: num/den + currNum/currDen
      int newNum = num * currDen + currNum * den;
      int newDen = den * currDen;

      int g = _gcd(newNum.abs(), newDen);
      num = newNum ~/ g;
      den = newDen ~/ g;
    }

    return '${num}/${den}';
  }

  bool _isDigit(int code) => code >= 48 && code <= 57;

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
import "strconv"

func fractionAddition(expression string) string {
	var num int64 = 0
	var den int64 = 1
	i, n := 0, len(expression)

	for i < n {
		sign := int64(1)
		if expression[i] == '+' {
			i++
		} else if expression[i] == '-' {
			sign = -1
			i++
		}

		var curNum int64 = 0
		for i < n && expression[i] >= '0' && expression[i] <= '9' {
			curNum = curNum*10 + int64(expression[i]-'0')
			i++
		}
		curNum *= sign

		if i < n && expression[i] == '/' {
			i++
		}

		var curDen int64 = 0
		for i < n && expression[i] >= '0' && expression[i] <= '9' {
			curDen = curDen*10 + int64(expression[i]-'0')
			i++
		}

		num = num*curDen + curNum*den
		den = den * curDen

		g := gcd(abs(num), den)
		if g != 0 {
			num /= g
			den /= g
		}
	}

	if num == 0 {
		return "0/1"
	}
	if den < 0 {
		den = -den
		num = -num
	}
	return strconv.FormatInt(num, 10) + "/" + strconv.FormatInt(den, 10)
}

func gcd(a, b int64) int64 {
	for b != 0 {
		a, b = b, a%b
	}
	if a < 0 {
		a = -a
	}
	return a
}

func abs(a int64) int64 {
	if a < 0 {
		return -a
	}
	return a
}
```

## Ruby

```ruby
def fraction_addition(expression)
  num = 0
  den = 1
  i = 0
  n = expression.length

  while i < n
    sign = 1
    if expression[i] == '+'
      i += 1
    elsif expression[i] == '-'
      sign = -1
      i += 1
    end

    # parse numerator
    cur_num = 0
    while i < n && expression[i] >= '0' && expression[i] <= '9'
      cur_num = cur_num * 10 + (expression[i].ord - 48)
      i += 1
    end
    cur_num *= sign

    # skip '/'
    i += 1

    # parse denominator
    cur_den = 0
    while i < n && expression[i] >= '0' && expression[i] <= '9'
      cur_den = cur_den * 10 + (expression[i].ord - 48)
      i += 1
    end

    # add fractions: num/den + cur_num/cur_den
    num = num * cur_den + cur_num * den
    den = den * cur_den

    g = num.gcd(den)
    num /= g
    den /= g
  end

  "#{num}/#{den}"
end
```

## Scala

```scala
object Solution {
    def fractionAddition(expression: String): String = {
        def gcd(a: Long, b: Long): Long = {
            var x = math.abs(a)
            var y = math.abs(b)
            while (y != 0) {
                val tmp = x % y
                x = y
                y = tmp
            }
            x
        }

        var numRes: Long = 0L
        var denRes: Long = 1L

        var i = 0
        val n = expression.length
        while (i < n) {
            var sign = 1
            if (expression.charAt(i) == '+') {
                sign = 1
                i += 1
            } else if (expression.charAt(i) == '-') {
                sign = -1
                i += 1
            }

            var num = 0L
            while (i < n && expression.charAt(i).isDigit) {
                num = num * 10 + (expression.charAt(i) - '0')
                i += 1
            }
            // skip '/'
            i += 1
            var den = 0L
            while (i < n && expression.charAt(i).isDigit) {
                den = den * 10 + (expression.charAt(i) - '0')
                i += 1
            }

            num *= sign

            val newNum = numRes * den + num * denRes
            val newDen = denRes * den
            val g = gcd(newNum, newDen)
            numRes = newNum / g
            denRes = newDen / g
        }

        if (numRes == 0) denRes = 1
        s"${numRes}/${denRes}"
    }
}
```

## Rust

```rust
impl Solution {
    pub fn fraction_addition(expression: String) -> String {
        fn gcd(mut a: i64, mut b: i64) -> i64 {
            while b != 0 {
                let r = a % b;
                a = b;
                b = r;
            }
            a.abs()
        }

        let bytes = expression.as_bytes();
        let mut i = 0usize;
        let mut num: i64 = 0;
        let mut den: i64 = 1;

        while i < bytes.len() {
            // sign
            let mut sign = 1i64;
            if bytes[i] == b'+' {
                i += 1;
            } else if bytes[i] == b'-' {
                sign = -1;
                i += 1;
            }

            // numerator
            let mut n: i64 = 0;
            while i < bytes.len() && (bytes[i] as char).is_ascii_digit() {
                n = n * 10 + (bytes[i] - b'0') as i64;
                i += 1;
            }
            n *= sign;

            // skip '/'
            if i < bytes.len() && bytes[i] == b'/' {
                i += 1;
            }

            // denominator
            let mut d: i64 = 0;
            while i < bytes.len() && (bytes[i] as char).is_ascii_digit() {
                d = d * 10 + (bytes[i] - b'0') as i64;
                i += 1;
            }

            // combine fractions
            let new_num = num * d + n * den;
            let new_den = den * d;
            let g = gcd(new_num.abs(), new_den);
            num = new_num / g;
            den = new_den / g;
        }

        if num == 0 {
            den = 1;
        }
        format!("{}/{}", num, den)
    }
}
```

## Racket

```racket
(define/contract (fraction-addition expression)
  (-> string? string?)
  (define (gcd a b)
    (let loop ((x (abs a)) (y (abs b)))
      (if (= x 0) y
          (loop (remainder y x) x))))
  (define len (string-length expression))
  (let loop ((i 0) (num 0) (den 1))
    (if (>= i len)
        (let* ((g (gcd num den))
               (n (/ num g))
               (d (/ den g)))
          (if (< d 0)
              (string-append (number->string (- n)) "/" (number->string (- d)))
              (string-append (number->string n) "/" (number->string d))))
        (begin
          ;; determine sign
          (define sign 1)
          (when (or (char=? (string-ref expression i) #\+)
                    (char=? (string-ref expression i) #\-))
            (set! sign (if (char=? (string-ref expression i) #\-) -1 1))
            (set! i (+ i 1)))
          ;; parse numerator up to '/'
          (define start-num i)
          (let ((j i))
            (let loop-num ((j j))
              (if (or (= j len) (char=? (string-ref expression j) #\/))
                  (begin
                    (define cur-num (* sign (string->number (substring expression start-num j))))
                    (set! i (+ j 1)) ; skip '/'
                    ;; parse denominator up to next '+' or '-' or end
                    (define start-den i)
                    (let ((k i))
                      (let loop-den ((k k))
                        (if (or (= k len)
                                (char=? (string-ref expression k) #\+)
                                (char=? (string-ref expression k) #\-))
                            (begin
                              (define cur-den (string->number (substring expression start-den k)))
                              ;; combine fractions
                              (define new-num (+ (* num cur-den) (* cur-num den)))
                              (define new-den (* den cur-den))
                              (loop k new-num new-den))
                            (loop-den (+ k 1))))))
                  (loop-num (+ j 1)))))))))))
```

## Erlang

```erlang
-module(solution).
-export([fraction_addition/1]).

-spec fraction_addition(Expression :: unicode:unicode_binary()) -> unicode:unicode_binary().
fraction_addition(Expression) ->
    List = binary_to_list(Expression),
    {Num, Den} = parse(List, 0, 1),
    G = gcd(abs(Num), Den),
    SimplNum = Num div G,
    SimplDen = Den div G,
    list_to_binary(integer_to_list(SimplNum) ++ "/" ++ integer_to_list(SimplDen)).

parse([], Num, Den) ->
    {Num, Den};
parse(Lst, AccNum, AccDen) ->
    % determine sign
    case Lst of
        [$+|Rest] -> Sign = 1, Rest1 = Rest;
        [$-|Rest] -> Sign = -1, Rest1 = Rest;
        _ -> Sign = 1, Rest1 = Lst
    end,
    {NumDigits, Rest2} = take_digits(Rest1),
    CurrNum = list_to_integer(NumDigits),
    % skip '/'
    [_Slash|Rest3] = Rest2,
    {DenDigits, Rest4} = take_digits(Rest3),
    CurrDen = list_to_integer(DenDigits),

    SignedCurrNum = Sign * CurrNum,
    NewNum = AccNum * CurrDen + SignedCurrNum * AccDen,
    NewDen = AccDen * CurrDen,
    parse(Rest4, NewNum, NewDen).

take_digits(List) -> take_digits(List, []).

take_digits([], Acc) ->
    {lists:reverse(Acc), []};
take_digits([H|T], Acc) when H >= $0, H =< $9 ->
    take_digits(T, [H|Acc]);
take_digits(Rest, Acc) ->
    {lists:reverse(Acc), Rest}.

gcd(0, B) -> B;
gcd(A, 0) -> A;
gcd(A, B) ->
    R = A rem B,
    gcd(B, R).
```

## Elixir

```elixir
defmodule Solution do
  @spec fraction_addition(expression :: String.t()) :: String.t()
  def fraction_addition(expression) do
    fractions = Regex.scan(~r/([+-]?\d+)\/(\d+)/, expression)

    {num, den} =
      Enum.reduce(fractions, {0, 1}, fn [_full, n_str, d_str], {acc_num, acc_den} ->
        n = String.to_integer(n_str)
        d = String.to_integer(d_str)

        new_num = acc_num * d + n * acc_den
        new_den = acc_den * d

        g = Integer.gcd(abs(new_num), new_den)
        {div(new_num, g), div(new_den, g)}
      end)

    if den < 0 do
      "#{-num}/#{-den}"
    else
      "#{num}/#{den}"
    end
  end
end
```
