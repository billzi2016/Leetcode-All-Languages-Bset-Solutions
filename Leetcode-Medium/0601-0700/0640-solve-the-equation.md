# 0640. Solve the Equation

## Cpp

```cpp
class Solution {
public:
    pair<int,int> parseSide(const string& s) {
        int coeffX = 0, constVal = 0;
        int n = s.size();
        int i = 0;
        while (i < n) {
            int sign = 1;
            if (s[i] == '+') { sign = 1; i++; }
            else if (s[i] == '-') { sign = -1; i++; }
            int start = i;
            while (i < n && s[i] != '+' && s[i] != '-') i++;
            string token = s.substr(start, i - start);
            if (!token.empty()) {
                if (token.back() == 'x') {
                    string numPart = token.substr(0, token.size() - 1);
                    int coeff = numPart.empty() ? 1 : stoi(numPart);
                    coeffX += sign * coeff;
                } else {
                    int val = stoi(token);
                    constVal += sign * val;
                }
            }
        }
        return {coeffX, constVal};
    }

    string solveEquation(string equation) {
        size_t pos = equation.find('=');
        string left = equation.substr(0, pos);
        string right = equation.substr(pos + 1);

        auto [leftCoeff, leftConst] = parseSide(left);
        auto [rightCoeff, rightConst] = parseSide(right);

        int a = leftCoeff - rightCoeff;          // coefficient of x after moving terms
        int b = rightConst - leftConst;          // constant term after moving

        if (a == 0) {
            if (b == 0) return "Infinite solutions";
            else return "No solution";
        } else {
            int x = b / a;
            return "x=" + to_string(x);
        }
    }
};
```

## Java

```java
class Solution {
    public String solveEquation(String equation) {
        String[] parts = equation.split("=");
        int[] left = parseSide(parts[0]);
        int[] right = parseSide(parts[1]);

        // (leftCoeff - rightCoeff) * x = rightConst - leftConst
        int coeffX = left[0] - right[0];
        int constVal = right[1] - left[1];

        if (coeffX == 0) {
            if (constVal == 0) {
                return "Infinite solutions";
            } else {
                return "No solution";
            }
        } else {
            int x = constVal / coeffX;
            return "x=" + x;
        }
    }

    private int[] parseSide(String s) {
        int coeff = 0;
        int constant = 0;
        int i = 0, n = s.length();
        while (i < n) {
            int sign = 1;
            char c = s.charAt(i);
            if (c == '+') {
                sign = 1;
                i++;
            } else if (c == '-') {
                sign = -1;
                i++;
            }
            int start = i;
            while (i < n && s.charAt(i) != '+' && s.charAt(i) != '-') {
                i++;
            }
            String token = s.substring(start, i);
            if (token.isEmpty()) continue;
            if (token.endsWith("x")) {
                String numPart = token.substring(0, token.length() - 1);
                int coeffVal = numPart.isEmpty() ? 1 : Integer.parseInt(numPart);
                coeff += sign * coeffVal;
            } else {
                int constVal = Integer.parseInt(token);
                constant += sign * constVal;
            }
        }
        return new int[]{coeff, constant};
    }
}
```

## Python

```python
class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        def parse(expr):
            coeff = 0
            const = 0
            i = 0
            n = len(expr)
            sign = 1
            while i < n:
                if expr[i] == '+':
                    sign = 1
                    i += 1
                elif expr[i] == '-':
                    sign = -1
                    i += 1
                # read term
                j = i
                while j < n and expr[j] not in '+-':
                    j += 1
                term = expr[i:j]
                if term.endswith('x'):
                    num_part = term[:-1]
                    if num_part == '':
                        val = 1
                    else:
                        val = int(num_part)
                    coeff += sign * val
                else:
                    const += sign * int(term)
                i = j
            return coeff, const

        left, right = equation.split('=')
        lc, lconst = parse(left)
        rc, rconst = parse(right)

        total_coeff = lc - rc
        total_const = rconst - lconst

        if total_coeff == 0:
            if total_const == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            x_val = total_const // total_coeff
            return "x=%d" % x_val
```

## Python3

```python
class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse(expr: str):
            i = 0
            n = len(expr)
            coeff = 0
            const = 0
            sign = 1
            while i < n:
                if expr[i] == '+':
                    sign = 1
                    i += 1
                elif expr[i] == '-':
                    sign = -1
                    i += 1
                # read number part
                j = i
                while j < n and expr[j].isdigit():
                    j += 1
                num_str = expr[i:j]
                if j < n and expr[j] == 'x':  # variable term
                    if num_str == '':
                        coeff += sign * 1
                    else:
                        coeff += sign * int(num_str)
                    j += 1
                else:  # constant term
                    if num_str != '':
                        const += sign * int(num_str)
                i = j
            return coeff, const

        left, right = equation.split('=')
        coeff_l, const_l = parse(left)
        coeff_r, const_r = parse(right)

        a = coeff_l - coeff_r          # coefficient of x after moving all to LHS
        b = const_r - const_l          # constant term after moving numbers to RHS

        if a == 0:
            if b == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            x_val = b // a
            return f"x={x_val}"
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdio.h>

static void parseSide(const char *s, long long *coeffX, long long *constVal) {
    int i = 0;
    int n = strlen(s);
    int sign = 1;
    while (i < n) {
        if (s[i] == '+') { sign = 1; i++; }
        else if (s[i] == '-') { sign = -1; i++; }

        long long num = 0;
        int hasNum = 0;
        while (i < n && isdigit(s[i])) {
            num = num * 10 + (s[i] - '0');
            i++;
            hasNum = 1;
        }
        if (i < n && s[i] == 'x') {
            long long coeff = hasNum ? num : 1;
            *coeffX += sign * coeff;
            i++; // skip 'x'
        } else {
            if (hasNum) {
                *constVal += sign * num;
            }
        }
    }
}

char* solveEquation(char* equation) {
    char *eq = equation;
    char *p = strchr(eq, '=');
    int leftLen = p - eq;

    char left[1005];
    strncpy(left, eq, leftLen);
    left[leftLen] = '\0';
    char right[1005];
    strcpy(right, p + 1);

    long long coeffL = 0, constL = 0;
    long long coeffR = 0, constR = 0;

    parseSide(left, &coeffL, &constL);
    parseSide(right, &coeffR, &constR);

    long long coeff = coeffL - coeffR;      // bring x terms to left
    long long constant = constR - constL;   // bring constants to right

    char *res;
    if (coeff == 0) {
        if (constant == 0) {
            res = (char *)malloc(20);
            strcpy(res, "Infinite solutions");
        } else {
            res = (char *)malloc(12);
            strcpy(res, "No solution");
        }
    } else {
        long long x = constant / coeff;
        char buf[50];
        sprintf(buf, "x=%lld", x);
        res = (char *)malloc(strlen(buf) + 1);
        strcpy(res, buf);
    }
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string SolveEquation(string equation)
    {
        var parts = equation.Split('=');
        var left = Parse(parts[0]);
        var right = Parse(parts[1]);

        int a = left.coeff - right.coeff;      // coefficient of x after moving all to LHS
        int b = left.constant - right.constant; // constant term after moving all to LHS

        if (a == 0)
        {
            if (b == 0) return "Infinite solutions";
            else return "No solution";
        }
        int x = -b / a;
        return $"x={x}";
    }

    private (int coeff, int constant) Parse(string expr)
    {
        int coeff = 0;
        int constant = 0;
        int i = 0;
        int n = expr.Length;
        int sign = 1; // current term sign

        while (i < n)
        {
            if (expr[i] == '+')
            {
                sign = 1;
                i++;
                continue;
            }
            else if (expr[i] == '-')
            {
                sign = -1;
                i++;
                continue;
            }

            int start = i;
            while (i < n && char.IsDigit(expr[i]))
                i++;

            bool hasNumber = i > start;

            if (i < n && expr[i] == 'x')
            {
                int coeffVal = hasNumber ? int.Parse(expr.Substring(start, i - start)) : 1;
                coeff += sign * coeffVal;
                i++; // skip 'x'
            }
            else
            {
                int val = int.Parse(expr.Substring(start, i - start));
                constant += sign * val;
            }
        }

        return (coeff, constant);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} equation
 * @return {string}
 */
var solveEquation = function(equation) {
    const [left, right] = equation.split('=');
    
    const parseSide = (s) => {
        let coeff = 0; // coefficient of x
        let constant = 0;
        let i = 0;
        while (i < s.length) {
            let sign = 1;
            if (s[i] === '+') {
                sign = 1;
                i++;
            } else if (s[i] === '-') {
                sign = -1;
                i++;
            }
            // read token
            let j = i;
            while (j < s.length && s[j] !== '+' && s[j] !== '-') {
                j++;
            }
            const token = s.slice(i, j);
            if (token.includes('x')) {
                const numPart = token.slice(0, -1); // remove 'x'
                const val = numPart === '' ? 1 : parseInt(numPart, 10);
                coeff += sign * val;
            } else {
                constant += sign * parseInt(token, 10);
            }
            i = j;
        }
        return [coeff, constant];
    };
    
    const [lc, lconst] = parseSide(left);
    const [rc, rconst] = parseSide(right);
    
    // (lc - rc) * x = rconst - lconst
    const coeff = lc - rc;
    const constVal = rconst - lconst;
    
    if (coeff === 0) {
        if (constVal === 0) return "Infinite solutions";
        else return "No solution";
    } else {
        const x = constVal / coeff;
        return `x=${x}`;
    }
};
```

## Typescript

```typescript
function solveEquation(equation: string): string {
    const [left, right] = equation.split('=');

    const parseSide = (s: string): [number, number] => {
        let coeffX = 0;
        let constant = 0;
        let i = 0;
        const n = s.length;
        while (i < n) {
            let sign = 1;
            if (s[i] === '+') {
                sign = 1;
                i++;
            } else if (s[i] === '-') {
                sign = -1;
                i++;
            }
            // read token
            let j = i;
            while (j < n && s[j] !== '+' && s[j] !== '-') j++;
            const token = s.slice(i, j);
            if (token.includes('x')) {
                const numPart = token.replace('x', '');
                const coeff = numPart === '' ? 1 : parseInt(numPart, 10);
                coeffX += sign * coeff;
            } else {
                constant += sign * parseInt(token, 10);
            }
            i = j;
        }
        return [coeffX, constant];
    };

    const [lc, lcst] = parseSide(left);
    const [rc, rcst] = parseSide(right);

    // (lc - rc) * x = rcst - lcst
    const coeff = lc - rc;
    const constVal = rcst - lcst;

    if (coeff === 0) {
        if (constVal === 0) return "Infinite solutions";
        else return "No solution";
    } else {
        const x = Math.trunc(constVal / coeff);
        return `x=${x}`;
    }
}
```

## Php

```php
class Solution {

    /**
     * @param String $equation
     * @return String
     */
    function solveEquation($equation) {
        list($left, $right) = explode('=', $equation, 2);
        [$lc, $ln] = $this->parseSide($left);
        [$rc, $rn] = $this->parseSide($right);

        // bring all x terms to left, numbers to right
        $coeff = $lc - $rc;
        $const = $rn - $ln;

        if ($coeff == 0) {
            if ($const == 0) {
                return "Infinite solutions";
            } else {
                return "No solution";
            }
        }

        $x = intdiv($const, $coeff);
        return "x=" . $x;
    }

    private function parseSide(string $s): array {
        $coeff = 0;
        $constant = 0;

        // Ensure the string starts with a sign for easy splitting
        if ($s[0] !== '+' && $s[0] !== '-') {
            $s = '+' . $s;
        }

        // Split while keeping the sign attached to each token
        $tokens = preg_split('/(?=[+-])/', $s);
        foreach ($tokens as $token) {
            if ($token === '' ) continue;
            $sign = $token[0];
            $term = substr($token, 1);

            if (strpos($term, 'x') !== false) {
                // Coefficient of x
                $numPart = str_replace('x', '', $term);
                $coef = ($numPart === '') ? 1 : intval($numPart);
                if ($sign === '-') $coef = -$coef;
                $coeff += $coef;
            } else {
                // Constant term
                $val = intval($term);
                if ($sign === '-') $val = -$val;
                $constant += $val;
            }
        }

        return [$coeff, $constant];
    }
}
```

## Swift

```swift
class Solution {
    func solveEquation(_ equation: String) -> String {
        let sides = equation.split(separator: "=")
        let left = String(sides[0])
        let right = String(sides[1])
        
        let (coeffL, constL) = parseExpression(left)
        let (coeffR, constR) = parseExpression(right)
        
        // Bring all x terms to the left and constants to the right
        let netCoeff = coeffL - coeffR
        let netConst = constR - constL
        
        if netCoeff == 0 {
            return netConst == 0 ? "Infinite solutions" : "No solution"
        } else {
            let value = netConst / netCoeff
            return "x=\(value)"
        }
    }
    
    private func parseExpression(_ expr: String) -> (coeff: Int, constant: Int) {
        var coeff = 0
        var constant = 0
        var sign = 1
        var idx = expr.startIndex
        
        while idx < expr.endIndex {
            let ch = expr[idx]
            if ch == "+" {
                sign = 1
                idx = expr.index(after: idx)
                continue
            } else if ch == "-" {
                sign = -1
                idx = expr.index(after: idx)
                continue
            }
            
            var num = 0
            var hasNum = false
            while idx < expr.endIndex, let digit = expr[idx].wholeNumberValue {
                hasNum = true
                num = num * 10 + digit
                idx = expr.index(after: idx)
            }
            
            if idx < expr.endIndex && expr[idx] == "x" {
                let coeffVal = hasNum ? num : 1
                coeff += sign * coeffVal
                idx = expr.index(after: idx)
            } else {
                if hasNum {
                    constant += sign * num
                }
            }
        }
        
        return (coeff, constant)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun solveEquation(equation: String): String {
        val parts = equation.split("=")
        val left = parseSide(parts[0])
        val right = parseSide(parts[1])

        val coeffDiff = left.first - right.first
        val constDiff = right.second - left.second

        return when {
            coeffDiff == 0 && constDiff == 0 -> "Infinite solutions"
            coeffDiff == 0 -> "No solution"
            else -> "x=${constDiff / coeffDiff}"
        }
    }

    private fun parseSide(side: String): Pair<Int, Int> {
        var expr = side
        if (expr.isNotEmpty() && expr[0] != '+' && expr[0] != '-') {
            expr = "+$expr"
        }
        var i = 0
        var coeff = 0
        var const = 0
        while (i < expr.length) {
            val sign = if (expr[i] == '+') 1 else -1
            i++
            var j = i
            while (j < expr.length && expr[j] != '+' && expr[j] != '-') {
                j++
            }
            val token = expr.substring(i, j)
            if (token.contains('x')) {
                val idx = token.indexOf('x')
                val numStr = token.substring(0, idx)
                val coeffVal = if (numStr.isEmpty()) 1 else numStr.toInt()
                coeff += sign * coeffVal
            } else {
                const += sign * token.toInt()
            }
            i = j
        }
        return Pair(coeff, const)
    }
}
```

## Dart

```dart
class Solution {
  String solveEquation(String equation) {
    List<String> parts = equation.split('=');
    var left = _parseSide(parts[0]);
    var right = _parseSide(parts[1]);

    int coeffX = left[0] - right[0];
    int constDiff = right[1] - left[1];

    if (coeffX == 0) {
      if (constDiff == 0) return "Infinite solutions";
      return "No solution";
    }
    int xVal = constDiff ~/ coeffX;
    return "x=$xVal";
  }

  List<int> _parseSide(String s) {
    int i = 0, n = s.length;
    int coeff = 0, constant = 0;

    while (i < n) {
      int sign = 1;
      if (s[i] == '+') {
        sign = 1;
        i++;
      } else if (s[i] == '-') {
        sign = -1;
        i++;
      }

      int numStart = i;
      while (i < n && _isDigit(s[i])) i++;
      bool hasNumber = i > numStart;
      String numStr = s.substring(numStart, i);

      bool isVar = false;
      if (i < n && s[i] == 'x') {
        isVar = true;
        i++; // consume 'x'
      }

      if (isVar) {
        int value = hasNumber ? int.parse(numStr) : 1;
        coeff += sign * value;
      } else {
        if (hasNumber) {
          int value = int.parse(numStr);
          constant += sign * value;
        }
      }
    }
    return [coeff, constant];
  }

  bool _isDigit(String ch) {
    int code = ch.codeUnitAt(0);
    return code >= 48 && code <= 57;
  }
}
```

## Golang

```go
package main

import (
	"fmt"
	"strconv"
)

func solveEquation(equation string) string {
	splitIdx := -1
	for i, ch := range equation {
		if ch == '=' {
			splitIdx = i
			break
		}
	}
	left := equation[:splitIdx]
	right := equation[splitIdx+1:]

	parse := func(s string) (int, int) {
		coeffX, constVal := 0, 0
		sign := 1
		n := len(s)
		i := 0
		for i < n {
			if s[i] == '+' {
				sign = 1
				i++
			} else if s[i] == '-' {
				sign = -1
				i++
			}
			start := i
			for i < n && s[i] >= '0' && s[i] <= '9' {
				i++
			}
			hasNum := i > start
			num := 0
			if hasNum {
				val, _ := strconv.Atoi(s[start:i])
				num = val
			}
			isX := false
			if i < n && s[i] == 'x' {
				isX = true
				i++
			}
			if isX {
				coeff := 1
				if hasNum {
					coeff = num
				}
				coeffX += sign * coeff
			} else {
				constVal += sign * num
			}
		}
		return coeffX, constVal
	}

	lc, lcst := parse(left)
	rc, rcst := parse(right)

	coeff := lc - rc
	constant := rcst - lcst

	if coeff == 0 {
		if constant == 0 {
			return "Infinite solutions"
		}
		return "No solution"
	}
	x := constant / coeff
	return fmt.Sprintf("x=%d", x)
}
```

## Ruby

```ruby
def solve_equation(equation)
  left_str, right_str = equation.split('=', 2)

  coeff_l, const_l = parse_side(left_str)
  coeff_r, const_r = parse_side(right_str)

  coeff = coeff_l - coeff_r
  const = const_r - const_l

  if coeff == 0
    return const == 0 ? "Infinite solutions" : "No solution"
  else
    x_val = const / coeff
    return "x=#{x_val}"
  end
end

def parse_side(s)
  coeff = 0
  const = 0
  s = '+' + s unless s.start_with?('+') || s.start_with?('-')
  tokens = s.scan(/[+-][^+-]+/)
  tokens.each do |t|
    if t.end_with?('x')
      num_str = t[0...-1] # remove 'x'
      if num_str == '+' || num_str == '-'
        coeff += (num_str == '+') ? 1 : -1
      else
        coeff += num_str.to_i
      end
    else
      const += t.to_i
    end
  end
  [coeff, const]
end
```

## Scala

```scala
object Solution {
  def solveEquation(equation: String): String = {
    val parts = equation.split("=")
    val (lc, lv) = parseSide(parts(0))
    val (rc, rv) = parseSide(parts(1))

    // Move all x terms to left and constants to right
    val a = lc - rc          // coefficient of x
    val b = rv - lv          // constant term

    if (a == 0) {
      if (b == 0) "Infinite solutions" else "No solution"
    } else {
      s"x=${b / a}"
    }
  }

  private def parseSide(s: String): (Int, Int) = {
    var coeffX = 0
    var constVal = 0
    var i = 0
    val n = s.length
    while (i < n) {
      var sign = 1
      if (s.charAt(i) == '+') {
        sign = 1
        i += 1
      } else if (s.charAt(i) == '-') {
        sign = -1
        i += 1
      }
      var j = i
      while (j < n && s.charAt(j) != '+' && s.charAt(j) != '-') {
        j += 1
      }
      val token = s.substring(i, j)
      if (token.contains('x')) {
        val coeffStr = token.dropRight(1) // remove 'x'
        val coeff = if (coeffStr.isEmpty) 1 else coeffStr.toInt
        coeffX += sign * coeff
      } else {
        constVal += sign * token.toInt
      }
      i = j
    }
    (coeffX, constVal)
  }
}
```

## Rust

```rust
impl Solution {
    pub fn solve_equation(equation: String) -> String {
        fn parse(side: &str) -> (i32, i32) {
            let bytes = side.as_bytes();
            let mut i = 0;
            let n = bytes.len();
            let mut coeff = 0;
            let mut constant = 0;
            while i < n {
                // sign
                let mut sign = 1;
                if bytes[i] == b'+' {
                    sign = 1;
                    i += 1;
                } else if bytes[i] == b'-' {
                    sign = -1;
                    i += 1;
                }
                // number part
                let start = i;
                while i < n && bytes[i].is_ascii_digit() {
                    i += 1;
                }
                let has_number = i > start;
                let mut num: i32 = 0;
                if has_number {
                    for &c in &bytes[start..i] {
                        num = num * 10 + (c - b'0') as i32;
                    }
                }
                // variable check
                if i < n && bytes[i] == b'x' {
                    let coeff_val = if has_number { num } else { 1 };
                    coeff += sign * coeff_val;
                    i += 1; // skip 'x'
                } else {
                    constant += sign * num;
                }
            }
            (coeff, constant)
        }

        let parts: Vec<&str> = equation.split('=').collect();
        let (lc, lconst) = parse(parts[0]);
        let (rc, rconst) = parse(parts[1]);

        let coeff = lc - rc;
        let const_term = rconst - lconst;

        if coeff == 0 {
            if const_term == 0 {
                "Infinite solutions".to_string()
            } else {
                "No solution".to_string()
            }
        } else {
            let x = const_term / coeff;
            format!("x={}", x)
        }
    }
}
```

## Racket

```racket
(define (parse-side s)
  (let ((n (string-length s)))
    (let loop ((i 0) (sign 1) (coeff 0) (const 0))
      (if (= i n)
          (list coeff const)
          (let ((ch (string-ref s i)))
            (cond
              [(char=? ch #\+) (loop (+ i 1) 1 coeff const)]
              [(char=? ch #\-) (loop (+ i 1) -1 coeff const)]
              [else
               (let ((start i))
                 (let inner ((j i))
                   (if (or (= j n)
                           (let ((c (string-ref s j)))
                             (or (char=? c #\+) (char=? c #\-))))
                       (let ((token (substring s start j)))
                         (if (string-contains token "x")
                             (let* ((len (string-length token))
                                    (coeff-str (substring token 0 (- len 1)))
                                    (num (if (= (string-length coeff-str) 0)
                                             1
                                             (string->number coeff-str))))
                               (loop j 1 (+ coeff (* sign num)) const))
                             (let ((num (string->number token)))
                               (loop j 1 coeff (+ const (* sign num))))))
                       (inner (+ j 1))))])))))))
                     
(define/contract (solve-equation equation)
  (-> string? string?)
  (let* ((parts (regexp-split #rx"=" equation))
         (left (list-ref parts 0))
         (right (list-ref parts 1))
         (lvals (parse-side left))
         (rvals (parse-side right))
         (a1 (first lvals)) (b1 (second lvals))
         (a2 (first rvals)) (b2 (second rvals))
         (coeff (- a1 a2))
         (const (- b2 b1)))
    (cond
      [(= coeff 0)
       (if (= const 0)
           "Infinite solutions"
           "No solution")]
      [else
       (string-append "x=" (number->string (/ const coeff)))])))
```

## Erlang

```erlang
-module(solution).
-export([solve_equation/1]).

-spec solve_equation(Equation :: unicode:unicode_binary()) -> unicode:unicode_binary().
solve_equation(Equation) ->
    [Left, Right] = binary:split(Equation, <<"=">>, []),
    {CoeffL, ConstL} = parse_side(Left),
    {CoeffR, ConstR} = parse_side(Right),
    A = CoeffL - CoeffR,
    B = ConstR - ConstL,
    case A of
        0 ->
            case B of
                0 -> <<"Infinite solutions">>;
                _ -> <<"No solution">>
            end;
        _ ->
            X = B div A,
            <<"x=", (integer_to_binary(X))/binary>>
    end.

parse_side(Bin) ->
    Bin2 = case binary:at(Bin, 0) of
               $- -> Bin;
               _  -> <<"+", Bin/binary>>
           end,
    Tokens = re:split(Bin2, <<"(?=[\\+\\-])">>, [{return, binary}]),
    parse_tokens(Tokens, 0, 0).

parse_tokens([], CoeffX, Const) ->
    {CoeffX, Const};
parse_tokens([Token | Rest], CoeffXAcc, ConstAcc) ->
    Sign = case binary:at(Token, 0) of
               $+ -> 1;
               $- -> -1
           end,
    Len = byte_size(Token),
    TermBin = binary:part(Token, 1, Len - 1),
    case is_x_term(TermBin) of
        true ->
            Coef = coeff_of_x(TermBin),
            NewCoeffX = CoeffXAcc + Sign * Coef,
            parse_tokens(Rest, NewCoeffX, ConstAcc);
        false ->
            Num = binary_to_integer(TermBin),
            NewConst = ConstAcc + Sign * Num,
            parse_tokens(Rest, CoeffXAcc, NewConst)
    end.

is_x_term(Bin) ->
    case byte_size(Bin) of
        0 -> false;
        Size -> binary:at(Bin, Size - 1) == $x
    end.

coeff_of_x(Bin) ->
    Size = byte_size(Bin),
    case Size of
        1 -> 1; % only 'x'
        _ ->
            NumBin = binary:part(Bin, 0, Size - 1),
            binary_to_integer(NumBin)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec solve_equation(equation :: String.t()) :: String.t()
  def solve_equation(equation) do
    [left_str, right_str] = String.split(equation, "=", parts: 2)

    {lx, lc} = parse_expr(left_str)
    {rx, rc} = parse_expr(right_str)

    coeff = lx - rx
    const = rc - lc

    cond do
      coeff == 0 and const == 0 -> "Infinite solutions"
      coeff == 0 -> "No solution"
      true ->
        value = div(const, coeff)
        "x=#{value}"
    end
  end

  defp parse_expr(expr) do
    terms =
      Regex.scan(~r/[+-]?[^+-]+/, expr)
      |> List.flatten()

    Enum.reduce(terms, {0, 0}, fn term, {cx, c} ->
      {sign, rest} = case String.at(term, 0) do
        "+" -> {1, String.slice(term, 1..-1)}
        "-" -> {-1, String.slice(term, 1..-1)}
        _   -> {1, term}
      end

      if String.contains?(rest, "x") do
        coeff_str = String.replace(rest, "x", "")
        coeff =
          case coeff_str do
            "" -> 1
            _  -> String.to_integer(coeff_str)
          end

        {cx + sign * coeff, c}
      else
        const = String.to_integer(rest)
        {cx, c + sign * const}
      end
    end)
  end
end
```
