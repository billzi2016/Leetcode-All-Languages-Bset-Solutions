# 2232. Minimize Result by Adding Parentheses to Expression

## Cpp

```cpp
class Solution {
public:
    string minimizeResult(string expression) {
        int n = expression.size();
        int plusPos = expression.find('+');
        long long bestVal = LLONG_MAX;
        int bestI = 0, bestJ = n - 1;
        for (int i = 0; i < plusPos; ++i) { // position of '(' before i
            for (int j = plusPos + 1; j < n; ++j) { // position of ')' after j
                string aStr = expression.substr(0, i);
                string bStr = expression.substr(i, plusPos - i);
                string cStr = expression.substr(plusPos + 1, j - (plusPos + 1) + 1);
                string dStr = expression.substr(j + 1);
                
                long long a = aStr.empty() ? 1 : stoll(aStr);
                long long b = bStr.empty() ? 0 : stoll(bStr); // should never be empty
                long long c = cStr.empty() ? 0 : stoll(cStr); // should never be empty
                long long d = dStr.empty() ? 1 : stoll(dStr);
                
                long long val = a * (b + c) * d;
                if (val < bestVal) {
                    bestVal = val;
                    bestI = i;
                    bestJ = j;
                }
            }
        }
        string aStr = expression.substr(0, bestI);
        string bStr = expression.substr(bestI, plusPos - bestI);
        string cStr = expression.substr(plusPos + 1, bestJ - (plusPos + 1) + 1);
        string dStr = expression.substr(bestJ + 1);
        return aStr + "(" + bStr + "+" + cStr + ")" + dStr;
    }
};
```

## Java

```java
class Solution {
    public String minimizeResult(String expression) {
        int plusIdx = expression.indexOf('+');
        String left = expression.substring(0, plusIdx);
        String right = expression.substring(plusIdx + 1);
        long minVal = Long.MAX_VALUE;
        String best = "";
        for (int i = 0; i < left.length(); i++) {
            String aStr = left.substring(0, i);
            String bStr = left.substring(i);
            long a = aStr.isEmpty() ? 1 : Long.parseLong(aStr);
            long b = Long.parseLong(bStr);
            for (int j = 0; j < right.length(); j++) {
                String cStr = right.substring(0, j + 1);
                String dStr = right.substring(j + 1);
                long c = Long.parseLong(cStr);
                long d = dStr.isEmpty() ? 1 : Long.parseLong(dStr);
                long val = a * (b + c) * d;
                if (val < minVal) {
                    minVal = val;
                    best = aStr + "(" + bStr + "+" + cStr + ")" + dStr;
                }
            }
        }
        return best;
    }
}
```

## Python

```python
class Solution(object):
    def minimizeResult(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        plus = expression.index('+')
        n = len(expression)
        best_val = None
        best_expr = ""
        for i in range(0, plus):  # position of '(' before character i
            left = expression[:i]
            b = expression[i:plus]          # part of num1 inside parentheses
            if not b:
                continue
            for r in range(plus + 2, n + 1):   # r is exclusive end index after '+'
                c = expression[plus + 1:r]    # part of num2 inside parentheses
                if not c:
                    continue
                right = expression[r:]
                left_val = int(left) if left else 1
                right_val = int(right) if right else 1
                cur = left_val * (int(b) + int(c)) * right_val
                if best_val is None or cur < best_val:
                    best_val = cur
                    best_expr = left + '(' + b + '+' + c + ')' + right
        return best_expr
```

## Python3

```python
class Solution:
    def minimizeResult(self, expression: str) -> str:
        s = expression
        plus = s.index('+')
        best_val = None
        best_i = best_j = 0

        for i in range(0, plus):
            a_str = s[:i]
            b_str = s[i:plus]

            for j in range(plus + 1, len(s)):
                c_str = s[plus + 1:j + 1]
                d_str = s[j + 1:]

                a = int(a_str) if a_str else 1
                b = int(b_str)
                c = int(c_str)
                d = int(d_str) if d_str else 1

                val = a * (b + c) * d

                if best_val is None or val < best_val:
                    best_val = val
                    best_i, best_j = i, j

        # construct result with parentheses at best positions
        return s[:best_i] + '(' + s[best_i:best_j + 1] + ')' + s[best_j + 1:]
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <limits.h>

static int strToInt(const char *s, int l, int r) {
    int val = 0;
    for (int i = l; i < r; ++i) {
        val = val * 10 + (s[i] - '0');
    }
    return val;
}

char* minimizeResult(char* expression) {
    int n = strlen(expression);
    int plusPos = 0;
    while (plusPos < n && expression[plusPos] != '+') ++plusPos;

    long long bestVal = LLONG_MAX;
    int bestI = 0, bestJ = n; // positions for '(' and ')'

    for (int i = 0; i < plusPos; ++i) {               // '(' before index i
        for (int j = plusPos + 2; j <= n; ++j) {      // ')' after index j-1
            int a = (i == 0) ? 1 : strToInt(expression, 0, i);
            int b = strToInt(expression, i, plusPos);
            int c = strToInt(expression, plusPos + 1, j);
            int d = (j == n) ? 1 : strToInt(expression, j, n);

            long long cur = (long long)a * (b + c) * d;
            if (cur < bestVal) {
                bestVal = cur;
                bestI = i;
                bestJ = j;
            }
        }
    }

    // Build result string with parentheses
    char *res = (char *)malloc(n + 3); // original length + '(' + ')' + '\0'
    int pos = 0;

    memcpy(res + pos, expression, bestI);
    pos += bestI;

    res[pos++] = '(';
    memcpy(res + pos, expression + bestI, plusPos - bestI);
    pos += (plusPos - bestI);

    res[pos++] = '+';
    memcpy(res + pos, expression + plusPos + 1, bestJ - (plusPos + 1));
    pos += (bestJ - (plusPos + 1));

    res[pos++] = ')';
    memcpy(res + pos, expression + bestJ, n - bestJ);
    pos += (n - bestJ);

    res[pos] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string MinimizeResult(string expression) {
        int plusIdx = expression.IndexOf('+');
        long minVal = long.MaxValue;
        string best = "";
        int n = expression.Length;

        for (int i = 0; i < plusIdx; ++i) {               // position of '(' before character i
            for (int j = plusIdx + 1; j < n; ++j) {       // position of ')' after character j
                string aStr = expression.Substring(0, i);
                string bStr = expression.Substring(i, plusIdx - i);
                string cStr = expression.Substring(plusIdx + 1, j - plusIdx);
                string dStr = expression.Substring(j + 1);

                long a = aStr.Length == 0 ? 1 : long.Parse(aStr);
                long b = long.Parse(bStr);
                long c = long.Parse(cStr);
                long d = dStr.Length == 0 ? 1 : long.Parse(dStr);

                long val = a * (b + c) * d;
                if (val < minVal) {
                    minVal = val;
                    best = aStr + "(" + bStr + "+" + cStr + ")" + dStr;
                }
            }
        }

        return best;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} expression
 * @return {string}
 */
var minimizeResult = function(expression) {
    const plusIdx = expression.indexOf('+');
    let minVal = Number.MAX_SAFE_INTEGER;
    let best = '';
    for (let i = 0; i < plusIdx; ++i) {               // position of '('
        for (let j = plusIdx + 1; j < expression.length; ++j) { // position of ')'
            const aStr = expression.slice(0, i);
            const bStr = expression.slice(i, plusIdx);
            const cStr = expression.slice(plusIdx + 1, j + 1);
            const dStr = expression.slice(j + 1);
            
            const aVal = aStr.length ? parseInt(aStr, 10) : 1;
            const bVal = parseInt(bStr, 10);
            const cVal = parseInt(cStr, 10);
            const dVal = dStr.length ? parseInt(dStr, 10) : 1;
            
            const cur = aVal * (bVal + cVal) * dVal;
            if (cur < minVal) {
                minVal = cur;
                best = aStr + '(' + bStr + '+' + cStr + ')' + dStr;
            }
        }
    }
    return best;
};
```

## Typescript

```typescript
function minimizeResult(expression: string): string {
    const plusIdx = expression.indexOf('+');
    let bestVal = Number.MAX_SAFE_INTEGER;
    let bestL = 0, bestR = expression.length - 1;

    const toNum = (s: string): number => s.length === 0 ? 1 : Number(s);

    for (let l = 0; l < plusIdx; ++l) {
        for (let r = plusIdx + 1; r < expression.length; ++r) {
            const aStr = expression.slice(0, l);
            const bStr = expression.slice(l, plusIdx);
            const cStr = expression.slice(plusIdx + 1, r + 1);
            const dStr = expression.slice(r + 1);

            const a = toNum(aStr);
            const b = toNum(bStr);
            const c = toNum(cStr);
            const d = toNum(dStr);

            const val = a * (b + c) * d;
            if (val < bestVal) {
                bestVal = val;
                bestL = l;
                bestR = r;
            }
        }
    }

    return (
        expression.slice(0, bestL) +
        '(' +
        expression.slice(bestL, plusIdx) +
        '+' +
        expression.slice(plusIdx + 1, bestR + 1) +
        ')' +
        expression.slice(bestR + 1)
    );
}
```

## Php

```php
class Solution {

    /**
     * @param String $expression
     * @return String
     */
    function minimizeResult($expression) {
        $plusPos = strpos($expression, '+');
        $left = substr($expression, 0, $plusPos);
        $right = substr($expression, $plusPos + 1);

        $minVal = PHP_INT_MAX;
        $best = "";

        $lenLeft = strlen($left);
        $lenRight = strlen($right);

        for ($i = 0; $i < $lenLeft; $i++) {
            $a = substr($left, 0, $i);
            $b = substr($left, $i); // at least one digit

            $aVal = ($a === '') ? 1 : intval($a);

            for ($j = 1; $j <= $lenRight; $j++) {
                $c = substr($right, 0, $j);
                $d = substr($right, $j); // may be empty

                $dVal = ($d === '') ? 1 : intval($d);

                $curVal = $aVal * (intval($b) + intval($c)) * $dVal;

                if ($curVal < $minVal) {
                    $minVal = $curVal;
                    $best = $a . '(' . $b . '+' . $c . ')' . $d;
                }
            }
        }

        return $best;
    }
}
```

## Swift

```swift
class Solution {
    func minimizeResult(_ expression: String) -> String {
        let chars = Array(expression)
        guard let plusIdx = chars.firstIndex(of: "+") else { return expression }
        let n = chars.count
        var bestValue = Int.max
        var bestLeft = 0
        var bestRight = plusIdx + 1
        
        func makeString(_ l: Int, _ r: Int) -> String {
            // [l, r)
            return String(chars[l..<r])
        }
        
        for left in 0..<(plusIdx) {               // position of '(' before character at index left
            for right in (plusIdx + 1)..<n {      // position of ')' after character at index right
                let aStr = left > 0 ? makeString(0, left) : ""
                let bStr = makeString(left, plusIdx)
                let cStr = makeString(plusIdx + 1, right + 1)
                let dStr = (right + 1 < n) ? makeString(right + 1, n) : ""
                
                let aVal = aStr.isEmpty ? 1 : Int(aStr)!
                let bVal = Int(bStr)!   // non‑empty by loop bounds
                let cVal = Int(cStr)!   // non‑empty by loop bounds
                let dVal = dStr.isEmpty ? 1 : Int(dStr)!
                
                let value = aVal * (bVal + cVal) * dVal
                if value < bestValue {
                    bestValue = value
                    bestLeft = left
                    bestRight = right
                }
            }
        }
        
        // Build result using best positions
        let aStr = bestLeft > 0 ? makeString(0, bestLeft) : ""
        let bStr = makeString(bestLeft, plusIdx)
        let cStr = makeString(plusIdx + 1, bestRight + 1)
        let dStr = (bestRight + 1 < n) ? makeString(bestRight + 1, n) : ""
        
        return aStr + "(" + bStr + "+" + cStr + ")" + dStr
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimizeResult(expression: String): String {
        val plusIdx = expression.indexOf('+')
        var bestVal = Long.MAX_VALUE
        var bestL = 0
        var bestR = expression.length - 1

        for (l in 0 until plusIdx) {
            for (r in plusIdx + 1 until expression.length) {
                val aStr = expression.substring(0, l)
                val bStr = expression.substring(l, plusIdx)
                val cStr = expression.substring(plusIdx + 1, r + 1)
                val dStr = expression.substring(r + 1)

                val aVal = if (aStr.isEmpty()) 1L else aStr.toLong()
                val bVal = bStr.toLong()
                val cVal = cStr.toLong()
                val dVal = if (dStr.isEmpty()) 1L else dStr.toLong()

                val cur = aVal * (bVal + cVal) * dVal
                if (cur < bestVal) {
                    bestVal = cur
                    bestL = l
                    bestR = r
                }
            }
        }

        val sb = StringBuilder()
        sb.append(expression.substring(0, bestL))
        sb.append('(')
        sb.append(expression.substring(bestL, plusIdx))
        sb.append('+')
        sb.append(expression.substring(plusIdx + 1, bestR + 1))
        sb.append(')')
        sb.append(expression.substring(bestR + 1))
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String minimizeResult(String expression) {
    int plusIdx = expression.indexOf('+');
    String left = expression.substring(0, plusIdx);
    String right = expression.substring(plusIdx + 1);

    int bestVal = 1 << 60; // sufficiently large
    String bestExpr = '';

    for (int i = 0; i < left.length; i++) {
      String aStr = left.substring(0, i);
      String bStr = left.substring(i);
      int aVal = aStr.isEmpty ? 1 : int.parse(aStr);
      int bVal = int.parse(bStr);

      for (int j = 0; j < right.length; j++) {
        String cStr = right.substring(0, j + 1);
        String dStr = right.substring(j + 1);
        int cVal = int.parse(cStr);
        int dVal = dStr.isEmpty ? 1 : int.parse(dStr);

        int cur = aVal * (bVal + cVal) * dVal;
        if (cur < bestVal) {
          bestVal = cur;
          bestExpr = aStr + '(' + bStr + '+' + cStr + ')' + dStr;
        }
      }
    }

    return bestExpr;
  }
}
```

## Golang

```go
import (
	"strconv"
	"strings"
)

func minimizeResult(expression string) string {
	plus := strings.IndexByte(expression, '+')
	left := expression[:plus]
	right := expression[plus+1:]

	bestVal := int64(^uint64(0) >> 1) // max int64
	var ans string

	for i := 0; i < len(left); i++ { // split left into a|b, b must be non‑empty
		aStr := left[:i]
		bStr := left[i:]

		aVal := int64(1)
		if len(aStr) > 0 {
			v, _ := strconv.ParseInt(aStr, 10, 64)
			aVal = v
		}
		bVal, _ := strconv.ParseInt(bStr, 10, 64)

		for j := 1; j <= len(right); j++ { // split right into c|d, c must be non‑empty
			cStr := right[:j]
			dStr := right[j:]

			cVal, _ := strconv.ParseInt(cStr, 10, 64)
			dVal := int64(1)
			if len(dStr) > 0 {
				v, _ := strconv.ParseInt(dStr, 10, 64)
				dVal = v
			}

			val := aVal * (bVal + cVal) * dVal
			if val < bestVal {
				bestVal = val
				ans = aStr + "(" + bStr + "+" + cStr + ")" + dStr
			}
		}
	}
	return ans
}
```

## Ruby

```ruby
def minimize_result(expression)
  plus_idx = expression.index('+')
  left = expression[0...plus_idx]
  right = expression[(plus_idx + 1)..-1]

  min_val = Float::INFINITY
  best_expr = ""

  (0...left.length).each do |i|
    a_str = left[0...i]          # may be empty
    b_str = left[i..-1]          # non‑empty
    a_val = a_str.empty? ? 1 : a_str.to_i

    (0...right.length).each do |j|
      c_str = right[0..j]        # non‑empty
      d_str = right[(j + 1)..-1] || ""   # may be empty
      d_val = d_str.empty? ? 1 : d_str.to_i

      val = a_val * (b_str.to_i + c_str.to_i) * d_val

      if val < min_val
        min_val = val
        best_expr = "#{a_str}(#{b_str}+#{c_str})#{d_str}"
      end
    end
  end

  best_expr
end
```

## Scala

```scala
object Solution {
    def minimizeResult(expression: String): String = {
        val plusIdx = expression.indexOf('+')
        var bestVal: Long = Long.MaxValue
        var bestI = 0
        var bestJ = plusIdx + 1

        for (i <- 0 until plusIdx) { // i is start index of b, a length i
            val aStr = expression.substring(0, i)
            val leftMul: Long = if (aStr.isEmpty) 1L else aStr.toLong
            for (j <- plusIdx + 1 until expression.length) {
                val bStr = expression.substring(i, plusIdx)
                val cStr = expression.substring(plusIdx + 1, j + 1)
                val dStr = expression.substring(j + 1)
                val rightMul: Long = if (dStr.isEmpty) 1L else dStr.toLong
                val insideSum: Long = bStr.toLong + cStr.toLong
                val value = leftMul * insideSum * rightMul
                if (value < bestVal) {
                    bestVal = value
                    bestI = i
                    bestJ = j
                }
            }
        }

        val aStr = expression.substring(0, bestI)
        val bStr = expression.substring(bestI, plusIdx)
        val cStr = expression.substring(plusIdx + 1, bestJ + 1)
        val dStr = expression.substring(bestJ + 1)

        aStr + "(" + bStr + "+" + cStr + ")" + dStr
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimize_result(expression: String) -> String {
        let plus_pos = expression.find('+').unwrap();
        let left = &expression[..plus_pos];
        let right = &expression[plus_pos + 1..];
        let m = left.len();
        let n = right.len();

        let mut best_val: i64 = i64::MAX;
        let mut best_i: usize = 0;
        let mut best_j: usize = 1;

        for i in 0..m {
            let a_str = &left[..i];
            let b_str = &left[i..];
            let a_val: i64 = if a_str.is_empty() { 1 } else { a_str.parse().unwrap() };
            let b_val: i64 = b_str.parse().unwrap();

            for j in 1..=n {
                let c_str = &right[..j];
                let d_str = &right[j..];
                let c_val: i64 = c_str.parse().unwrap();
                let d_val: i64 = if d_str.is_empty() { 1 } else { d_str.parse().unwrap() };

                let val = a_val * (b_val + c_val) * d_val;
                if val < best_val {
                    best_val = val;
                    best_i = i;
                    best_j = j;
                }
            }
        }

        let mut result = String::new();
        result.push_str(&left[..best_i]);
        result.push('(');
        result.push_str(&left[best_i..]);
        result.push('+');
        result.push_str(&right[..best_j]);
        result.push(')');
        result.push_str(&right[best_j..]);
        result
    }
}
```

## Racket

```racket
#lang racket
(require racket/string)

(define/contract (minimize-result expression)
  (-> string? string?)
  (let* ([plus-pos (string-index-of expression "+")]
         [L (substring expression 0 plus-pos)]
         [R (substring expression (+ plus-pos 1))]
         [n (string-length L)]
         [m (string-length R)])
    (define best-val +inf.0)
    (define best-str "")
    (for ([i (in-range 0 n)]) ; i from 0 to n-1, ensures b non‑empty
      (let* ([aStr (substring L 0 i)]
             [bStr (substring L i n)])
        (for ([j (in-range 0 m)]) ; j from 0 to m-1, ensures c non‑empty
          (let* ([cStr (substring R 0 (+ j 1))]
                 [dStr (substring R (+ j 1) m)]
                 [a (if (string-empty? aStr) 1 (string->number aStr))]
                 [b (string->number bStr)]
                 [c (string->number cStr)]
                 [d (if (string-empty? dStr) 1 (string->number dStr))]
                 [val (* a (+ b c) d)])
            (when (< val best-val)
              (set! best-val val)
              (set! best-str (string-append aStr "(" bStr "+" cStr ")" dStr)))))))
    best-str))
```

## Erlang

```erlang
-module(solution).
-export([minimize_result/1]).

-spec minimize_result(Expression :: unicode:unicode_binary()) -> unicode:unicode_binary().
minimize_result(Expression) ->
    ExprList = binary_to_list(Expression),
    PlusIdx = find_plus(ExprList, 0),
    {Left, Rest} = lists:split(PlusIdx, ExprList),
    [_Plus | Right] = Rest,
    {BestVal, BestExpr} = iterate(Left, Right),
    list_to_binary(BestExpr).

find_plus([ $+ | _], Index) -> Index;
find_plus([_ | Rest], Index) -> find_plus(Rest, Index + 1).

iterate(Left, Right) ->
    Llen = length(Left),
    RlenMinus1 = length(Right) - 1,
    loop_i(0, Llen, Left, Right, RlenMinus1, 1 bsl 62, []).

loop_i(I, Llen, _Left, _Right, _RlenMinus1, MinVal, BestExpr) when I > Llen - 1 ->
    {MinVal, BestExpr};
loop_i(I, Llen, Left, Right, RlenMinus1, MinVal, BestExpr) ->
    A = lists:sublist(Left, I),
    B = lists:nthtail(I, Left),
    {NewMin, NewBest} = loop_k(0, RlenMinus1, A, B, Right, MinVal, BestExpr),
    loop_i(I + 1, Llen, Left, Right, RlenMinus1, NewMin, NewBest).

loop_k(K, _RlenMinus1, _A, _B, _Right, MinVal, BestExpr) when K > _RlenMinus1 ->
    {MinVal, BestExpr};
loop_k(K, RlenMinus1, A, B, Right, MinVal, BestExpr) ->
    C = lists:sublist(Right, K + 1),
    D = lists:nthtail(K + 1, Right),

    AVal = case A of [] -> 1; _ -> list_to_integer(A) end,
    BVal = list_to_integer(B),
    CVal = list_to_integer(C),
    DVal = case D of [] -> 1; _ -> list_to_integer(D) end,

    Val = AVal * (BVal + CVal) * DVal,
    Expr = A ++ [$(] ++ B ++ [$+,] ++ C ++ [$)] ++ D,

    {TmpMin, TmpBest} =
        if
            Val < MinVal -> {Val, Expr};
            true -> {MinVal, BestExpr}
        end,
    loop_k(K + 1, RlenMinus1, A, B, Right, TmpMin, TmpBest).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimize_result(expression :: String.t()) :: String.t()
  def minimize_result(expression) do
    [left, right] = String.split(expression, "+")
    l_len = String.length(left)
    r_len = String.length(right)

    {_, best_expr} =
      Enum.reduce(0..(l_len - 1), {nil, ""}, fn i, {min_val, ans} ->
        a_str = if i == 0, do: "", else: String.slice(left, 0, i)
        b_str = String.slice(left, i, l_len - i)

        Enum.reduce(1..r_len, {min_val, ans}, fn j, {cur_min, cur_ans} ->
          c_str = String.slice(right, 0, j)
          d_str = if j == r_len, do: "", else: String.slice(right, j, r_len - j)

          a_val = if a_str == "", do: 1, else: String.to_integer(a_str)
          b_val = String.to_integer(b_str)
          c_val = String.to_integer(c_str)
          d_val = if d_str == "", do: 1, else: String.to_integer(d_str)

          val = a_val * (b_val + c_val) * d_val
          expr = a_str <> "(" <> b_str <> "+" <> c_str <> ")" <> d_str

          cond do
            cur_min == nil or val < cur_min -> {val, expr}
            true -> {cur_min, cur_ans}
          end
        end)
      end)

    best_expr
  end
end
```
