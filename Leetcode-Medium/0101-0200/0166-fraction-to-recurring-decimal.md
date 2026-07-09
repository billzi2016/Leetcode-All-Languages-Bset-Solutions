# 0166. Fraction to Recurring Decimal

## Cpp

```cpp
class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        if (numerator == 0) return "0";
        long long n = static_cast<long long>(numerator);
        long long d = static_cast<long long>(denominator);
        bool negative = (n < 0) ^ (d < 0);
        n = llabs(n);
        d = llabs(d);
        
        string result;
        if (negative) result.push_back('-');
        
        long long integerPart = n / d;
        result += to_string(integerPart);
        long long remainder = n % d;
        if (remainder == 0) return result;
        
        result.push_back('.');
        unordered_map<long long, int> pos;
        while (remainder != 0) {
            if (pos.find(remainder) != pos.end()) {
                int insertPos = pos[remainder];
                result.insert(insertPos, "(");
                result.push_back(')');
                break;
            }
            pos[remainder] = result.size();
            remainder *= 10;
            long long digit = remainder / d;
            result.push_back('0' + static_cast<char>(digit));
            remainder %= d;
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public String fractionToDecimal(int numerator, int denominator) {
        if (numerator == 0) return "0";
        StringBuilder sb = new StringBuilder();
        // Determine sign
        if ((numerator < 0) ^ (denominator < 0)) sb.append('-');
        long n = Math.abs((long) numerator);
        long d = Math.abs((long) denominator);
        // Integer part
        sb.append(n / d);
        long remainder = n % d;
        if (remainder == 0) return sb.toString();
        sb.append('.');
        java.util.Map<Long, Integer> seen = new java.util.HashMap<>();
        while (remainder != 0) {
            if (seen.containsKey(remainder)) {
                int index = seen.get(remainder);
                sb.insert(index, '(');
                sb.append(')');
                break;
            }
            seen.put(remainder, sb.length());
            remainder *= 10;
            sb.append(remainder / d);
            remainder %= d;
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"
        
        res = []
        # sign handling
        if (numerator < 0) ^ (denominator < 0):
            res.append('-')
        
        n, d = abs(numerator), abs(denominator)
        integer_part = n // d
        res.append(str(integer_part))
        remainder = n % d
        if remainder == 0:
            return ''.join(res)
        
        res.append('.')
        fraction = []
        seen = {}
        while remainder != 0:
            if remainder in seen:
                idx = seen[remainder]
                fraction.insert(idx, '(')
                fraction.append(')')
                break
            seen[remainder] = len(fraction)
            remainder *= 10
            digit = remainder // d
            fraction.append(str(digit))
            remainder %= d
        
        res.extend(fraction)
        return ''.join(res)
```

## Python3

```python
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        sign = '-' if (numerator < 0) ^ (denominator < 0) else ''
        n, d = abs(numerator), abs(denominator)
        integer_part = n // d
        remainder = n % d
        result = [sign + str(integer_part)]
        if remainder == 0:
            return ''.join(result)
        result.append('.')
        seen = {}
        while remainder:
            if remainder in seen:
                idx = seen[remainder]
                result.insert(idx, '(')
                result.append(')')
                break
            seen[remainder] = len(result)
            remainder *= 10
            digit = remainder // d
            result.append(str(digit))
            remainder %= d
        return ''.join(result)
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

typedef struct {
    long long rem;
    int idx;
} Pair;

char* fractionToDecimal(int numerator, int denominator) {
    if (numerator == 0) {
        char *zero = malloc(2);
        zero[0] = '0';
        zero[1] = '\0';
        return zero;
    }

    long long num = llabs((long long)numerator);
    long long den = llabs((long long)denominator);
    int negative = ((numerator < 0) ^ (denominator < 0)) ? 1 : 0;

    char *res = malloc(20000);          // sufficient buffer per problem guarantee
    int pos = 0;
    if (negative) res[pos++] = '-';

    long long integerPart = num / den;
    pos += sprintf(res + pos, "%lld", integerPart);
    long long remainder = num % den;

    if (remainder == 0) {
        res[pos] = '\0';
        return res;
    }

    res[pos++] = '.';

    Pair *map = malloc(sizeof(Pair) * 20000);
    int mapSize = 0;

    while (remainder != 0) {
        int repeatIdx = -1;
        for (int i = 0; i < mapSize; ++i) {
            if (map[i].rem == remainder) {
                repeatIdx = map[i].idx;
                break;
            }
        }

        if (repeatIdx != -1) {
            memmove(res + repeatIdx + 1, res + repeatIdx, pos - repeatIdx);
            res[repeatIdx] = '(';
            pos++;                     // account for inserted '('
            res[pos++] = ')';
            res[pos] = '\0';
            free(map);
            return res;
        }

        map[mapSize].rem = remainder;
        map[mapSize].idx = pos;   // position where next digit will be placed
        ++mapSize;

        remainder *= 10;
        long long digit = remainder / den;
        res[pos++] = (char)('0' + digit);
        remainder %= den;
    }

    res[pos] = '\0';
    free(map);
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string FractionToDecimal(int numerator, int denominator)
    {
        if (numerator == 0) return "0";

        var sb = new System.Text.StringBuilder();

        // Determine sign.
        bool negative = (numerator < 0) ^ (denominator < 0);
        if (negative) sb.Append('-');

        long n = System.Math.Abs((long)numerator);
        long d = System.Math.Abs((long)denominator);

        // Integer part.
        sb.Append(n / d);
        long remainder = n % d;
        if (remainder == 0) return sb.ToString();

        sb.Append('.');

        var map = new System.Collections.Generic.Dictionary<long, int>();
        while (remainder != 0)
        {
            if (map.ContainsKey(remainder))
            {
                int insertPos = map[remainder];
                sb.Insert(insertPos, '(');
                sb.Append(')');
                break;
            }

            map[remainder] = sb.Length;
            remainder *= 10;
            sb.Append(remainder / d);
            remainder %= d;
        }

        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {number} numerator
 * @param {number} denominator
 * @return {string}
 */
var fractionToDecimal = function(numerator, denominator) {
    if (numerator === 0) return "0";
    let sign = '';
    if ((numerator < 0) ^ (denominator < 0)) sign = '-';
    
    const num = Math.abs(numerator);
    const den = Math.abs(denominator);
    
    const integerPart = Math.floor(num / den);
    let remainder = num % den;
    if (remainder === 0) return sign + integerPart.toString();
    
    let fraction = '';
    const seen = new Map(); // remainder -> position in fraction string
    
    while (remainder !== 0 && !seen.has(remainder)) {
        seen.set(remainder, fraction.length);
        remainder *= 10;
        const digit = Math.floor(remainder / den);
        fraction += digit.toString();
        remainder %= den;
    }
    
    if (remainder !== 0) { // repeating part found
        const idx = seen.get(remainder);
        fraction = fraction.slice(0, idx) + '(' + fraction.slice(idx) + ')';
    }
    
    return sign + integerPart.toString() + '.' + fraction;
};
```

## Typescript

```typescript
function fractionToDecimal(numerator: number, denominator: number): string {
    if (numerator === 0) return "0";
    const sign = (numerator < 0) !== (denominator < 0) ? "-" : "";
    let num = Math.abs(numerator);
    const den = Math.abs(denominator);
    const integerPart = Math.floor(num / den);
    let remainder = num % den;
    if (remainder === 0) return sign + integerPart.toString();
    let result = integerPart.toString() + ".";
    const seen = new Map<number, number>();
    while (remainder !== 0) {
        if (seen.has(remainder)) {
            const idx = seen.get(remainder)!;
            result = result.slice(0, idx) + "(" + result.slice(idx) + ")";
            break;
        }
        seen.set(remainder, result.length);
        remainder *= 10;
        const digit = Math.floor(remainder / den);
        result += digit.toString();
        remainder %= den;
    }
    return sign + result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $numerator
     * @param Integer $denominator
     * @return String
     */
    function fractionToDecimal($numerator, $denominator) {
        if ($numerator == 0) {
            return "0";
        }

        $sign = '';
        if (($numerator < 0) xor ($denominator < 0)) {
            $sign = '-';
        }

        $num = abs($numerator);
        $den = abs($denominator);

        $integerPart = intdiv($num, $den);
        $remainder = $num % $den;

        if ($remainder == 0) {
            return $sign . (string)$integerPart;
        }

        $fraction = '';
        $map = [];

        while ($remainder != 0) {
            if (isset($map[$remainder])) {
                $pos = $map[$remainder];
                $nonRepeating = substr($fraction, 0, $pos);
                $repeating = substr($fraction, $pos);
                $fraction = $nonRepeating . '(' . $repeating . ')';
                return $sign . (string)$integerPart . '.' . $fraction;
            }

            $map[$remainder] = strlen($fraction);
            $remainder *= 10;
            $digit = intdiv($remainder, $den);
            $fraction .= (string)$digit;
            $remainder %= $den;
        }

        return $sign . (string)$integerPart . '.' . $fraction;
    }
}
```

## Swift

```swift
class Solution {
    func fractionToDecimal(_ numerator: Int, _ denominator: Int) -> String {
        if numerator == 0 { return "0" }
        
        var result = ""
        let negative = (numerator < 0) != (denominator < 0)
        
        var n = Int64(numerator)
        var d = Int64(denominator)
        n = n >= 0 ? n : -n
        d = d >= 0 ? d : -d
        
        let integerPart = n / d
        var remainder = n % d
        result += (negative ? "-" : "") + String(integerPart)
        
        if remainder == 0 {
            return result
        }
        
        result += "."
        var fraction = ""
        var seen = [Int64: Int]()   // remainder -> position in fraction
        
        while remainder != 0 {
            if let idx = seen[remainder] {
                let insertPos = fraction.index(fraction.startIndex, offsetBy: idx)
                fraction.insert("(", at: insertPos)
                fraction.append(")")
                result += fraction
                return result
            }
            seen[remainder] = fraction.count
            remainder *= 10
            let digit = remainder / d
            fraction.append(String(digit))
            remainder %= d
        }
        
        result += fraction
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun fractionToDecimal(numerator: Int, denominator: Int): String {
        if (numerator == 0) return "0"
        val sb = StringBuilder()
        // Determine sign
        if ((numerator < 0) xor (denominator < 0)) sb.append('-')
        var n = kotlin.math.abs(numerator.toLong())
        var d = kotlin.math.abs(denominator.toLong())
        // Integer part
        sb.append(n / d)
        var remainder = n % d
        if (remainder == 0L) return sb.toString()
        sb.append('.')
        val seen = HashMap<Long, Int>()
        while (remainder != 0L) {
            if (seen.containsKey(remainder)) {
                val index = seen[remainder]!!
                sb.insert(index, '(')
                sb.append(')')
                break
            }
            seen[remainder] = sb.length
            remainder *= 10
            sb.append(remainder / d)
            remainder %= d
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String fractionToDecimal(int numerator, int denominator) {
    if (numerator == 0) return "0";

    StringBuffer sb = StringBuffer();

    bool negative = (numerator < 0) ^ (denominator < 0);
    if (negative) sb.write('-');

    int n = numerator.abs();
    int d = denominator.abs();

    int integerPart = n ~/ d;
    sb.write(integerPart);

    int remainder = n % d;
    if (remainder == 0) return sb.toString();

    sb.write('.');

    Map<int, int> seen = {};

    while (remainder != 0) {
      if (seen.containsKey(remainder)) {
        int index = seen[remainder]!;
        String result = sb.toString();
        return result.substring(0, index) + '(' + result.substring(index) + ')';
      }
      seen[remainder] = sb.length;
      remainder *= 10;
      int digit = remainder ~/ d;
      sb.write(digit);
      remainder %= d;
    }

    return sb.toString();
  }
}
```

## Golang

```go
import (
	"strconv"
	"strings"
)

func fractionToDecimal(numerator int, denominator int) string {
	if numerator == 0 {
		return "0"
	}
	var sb strings.Builder
	n := int64(numerator)
	d := int64(denominator)

	// sign handling
	if (n < 0) != (d < 0) {
		sb.WriteByte('-')
	}
	if n < 0 {
		n = -n
	}
	if d < 0 {
		d = -d
	}

	integerPart := n / d
	sb.WriteString(strconv.FormatInt(integerPart, 10))

	remainder := n % d
	if remainder == 0 {
		return sb.String()
	}
	sb.WriteByte('.')

	remPos := make(map[int64]int)
	var fraction []byte

	for remainder != 0 {
		if pos, ok := remPos[remainder]; ok {
			var res strings.Builder
			res.WriteString(sb.String())
			res.Write(fraction[:pos])
			res.WriteByte('(')
			res.Write(fraction[pos:])
			res.WriteByte(')')
			return res.String()
		}
		remPos[remainder] = len(fraction)

		remainder *= 10
		digit := remainder / d
		fraction = append(fraction, byte('0'+digit))
		remainder %= d
	}

	sb.Write(fraction)
	return sb.String()
}
```

## Ruby

```ruby
def fraction_to_decimal(numerator, denominator)
  return "0" if numerator == 0

  sign = (numerator < 0) ^ (denominator < 0) ? "-" : ""
  num = numerator.abs
  den = denominator.abs

  integer_part = num / den
  remainder = num % den

  result = sign + integer_part.to_s
  return result if remainder == 0

  result << "."
  seen = {}

  while remainder != 0
    if seen.key?(remainder)
      idx = seen[remainder]
      result.insert(idx, "(")
      result << ")"
      break
    end
    seen[remainder] = result.length
    remainder *= 10
    digit = remainder / den
    result << digit.to_s
    remainder %= den
  end

  result
end
```

## Scala

```scala
object Solution {
    def fractionToDecimal(numerator: Int, denominator: Int): String = {
        if (numerator == 0) return "0"
        val negative = (numerator < 0) ^ (denominator < 0)
        var n = math.abs(numerator.toLong)
        var d = math.abs(denominator.toLong)

        val sb = new StringBuilder
        sb.append(n / d)
        var remainder = n % d
        if (remainder == 0) {
            return (if (negative) "-" else "") + sb.toString()
        }

        sb.append('.')
        val seen = scala.collection.mutable.Map[Long, Int]()
        while (remainder != 0) {
            if (seen.contains(remainder)) {
                val idx = seen(remainder)
                sb.insert(idx, '(')
                sb.append(')')
                return (if (negative) "-" else "") + sb.toString()
            }
            seen(remainder) = sb.length
            remainder *= 10
            sb.append(remainder / d)
            remainder %= d
        }

        (if (negative) "-" else "") + sb.toString()
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn fraction_to_decimal(numerator: i32, denominator: i32) -> String {
        if numerator == 0 {
            return "0".to_string();
        }

        let mut result = String::new();

        // Determine sign
        let negative = (numerator < 0) ^ (denominator < 0);
        if negative {
            result.push('-');
        }

        // Use i64 to avoid overflow and work with absolute values
        let n = numerator as i64;
        let d = denominator as i64;
        let mut num = if n < 0 { -n } else { n };
        let den = if d < 0 { -d } else { d };

        // Integer part
        let int_part = num / den;
        result.push_str(&int_part.to_string());

        // Remainder after integer division
        let mut remainder = num % den;
        if remainder == 0 {
            return result;
        }

        result.push('.');

        let mut map: HashMap<i64, usize> = HashMap::new();
        let mut fraction = String::new();
        let mut repeat_start: Option<usize> = None;

        while remainder != 0 {
            if let Some(&pos) = map.get(&remainder) {
                repeat_start = Some(pos);
                break;
            }
            map.insert(remainder, fraction.len());
            remainder *= 10;
            let digit = remainder / den;
            fraction.push(std::char::from_digit(digit as u32, 10).unwrap());
            remainder %= den;
        }

        if let Some(start) = repeat_start {
            let (head, tail) = fraction.split_at(start);
            result.push_str(head);
            result.push('(');
            result.push_str(tail);
            result.push(')');
        } else {
            result.push_str(&fraction);
        }

        result
    }
}
```

## Racket

```racket
#lang racket

(require racket/list)

(define/contract (fraction-to-decimal numerator denominator)
  (-> exact-integer? exact-integer? string?)
  (let* ([sign
          (if (or (and (< numerator 0) (> denominator 0))
                  (and (> numerator 0) (< denominator 0)))
              "-"
              "")]
         [n (abs numerator)]
         [d (abs denominator)]
         [int-part (quotient n d)]
         [rem (remainder n d)])
    (if (= rem 0)
        (string-append sign (number->string int-part))
        (let-values ([(digits repeat-start)
                      (let loop ((r rem) (pos 0) (rem-pos (make-hash)) (acc '()))
                        (cond
                          [(hash-has-key? rem-pos r)
                           (values (reverse acc) (hash-ref rem-pos r))]
                          [(= r 0)
                           (values (reverse acc) #f)]
                          [else
                           (hash-set! rem-pos r pos)
                           (define r10 (* r 10))
                           (define digit (quotient r10 d))
                           (define new-rem (remainder r10 d))
                           (loop new-rem (+ pos 1) rem-pos (cons digit acc))]))])
          (define decimal-str
            (if repeat-start
                (let* ([before (take digits repeat-start)]
                       [repeat-part (drop digits repeat-start)])
                  (string-append
                   (apply string (map number->string before))
                   "("
                   (apply string (map number->string repeat-part))
                   ")"))
                (apply string (map number->string digits))))
          (string-append sign (number->string int-part) "." decimal-str)))))
```

## Erlang

```erlang
-spec fraction_to_decimal(Numerator :: integer(), Denominator :: integer()) -> unicode:unicode_binary().
fraction_to_decimal(Numerator, Denominator) ->
    case Numerator of
        0 -> <<"0">>;
        _ ->
            Sign = if (Numerator < 0) xor (Denominator < 0) -> "-"; true -> [] end,
            N = abs(Numerator),
            D = abs(Denominator),
            IntPart = N div D,
            Rem0 = N rem D,
            IntStr = integer_to_list(IntPart),
            Base = Sign ++ IntStr,
            case Rem0 of
                0 ->
                    iolist_to_binary(Base);
                _ ->
                    Fraction = process_fraction(Rem0, D, #{}, [], 0),
                    iolist_to_binary(Base ++ "." ++ Fraction)
            end
    end.

process_fraction(0, _D, _Map, Acc, _Idx) -> Acc;
process_fraction(R, D, Map, Acc, Idx) ->
    case maps:is_key(R, Map) of
        true ->
            Pos = maps:get(R, Map),
            {Prefix, Suffix} = lists:split(Pos, Acc),
            Prefix ++ [$\(] ++ Suffix ++ [$\)];
        false ->
            NewMap = maps:put(R, Idx, Map),
            R10 = R * 10,
            Digit = R10 div D,
            NewR = R10 rem D,
            Char = $0 + Digit,
            process_fraction(NewR, D, NewMap, Acc ++ [Char], Idx + 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec fraction_to_decimal(numerator :: integer, denominator :: integer) :: String.t()
  def fraction_to_decimal(numerator, denominator) do
    if numerator == 0 do
      "0"
    else
      sign = if (numerator < 0) != (denominator < 0), do: "-", else: ""
      n = abs(numerator)
      d = abs(denominator)

      integer_part = div(n, d)
      remainder = Integer.mod(n, d)

      if remainder == 0 do
        sign <> Integer.to_string(integer_part)
      else
        {fraction_str, _} = build_fraction(remainder, d, %{}, "")
        sign <> Integer.to_string(integer_part) <> "." <> fraction_str
      end
    end
  end

  defp build_fraction(0, _den, _seen, acc), do: {acc, nil}

  defp build_fraction(r, den, seen, acc) do
    case Map.get(seen, r) do
      nil ->
        pos = String.length(acc)
        seen = Map.put(seen, r, pos)

        new_r = r * 10
        digit = div(new_r, den)
        new_acc = acc <> Integer.to_string(digit)
        next_r = new_r - digit * den

        build_fraction(next_r, den, seen, new_acc)

      pos ->
        prefix = String.slice(acc, 0, pos)
        repeat_part = String.slice(acc, pos..-1)
        {prefix <> "(" <> repeat_part <> ")", :repeat}
    end
  end
end
```
