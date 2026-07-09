# 2288. Apply Discount to Prices

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string discountPrices(string sentence, int discount) {
        vector<string> words;
        string cur;
        for (size_t i = 0; i <= sentence.size(); ++i) {
            if (i == sentence.size() || sentence[i] == ' ') {
                words.push_back(cur);
                cur.clear();
            } else {
                cur += sentence[i];
            }
        }

        for (string &w : words) {
            if (w.empty() || w[0] != '$' || w.size() == 1) continue;
            bool ok = true;
            for (size_t i = 1; i < w.size(); ++i) {
                if (!isdigit(w[i])) { ok = false; break; }
            }
            if (!ok) continue;

            long long price = stoll(w.substr(1));
            double discounted = price * (100 - discount) / 100.0;
            ostringstream oss;
            oss << '$' << fixed << setprecision(2) << discounted;
            w = oss.str();
        }

        string result;
        for (size_t i = 0; i < words.size(); ++i) {
            if (i) result += ' ';
            result += words[i];
        }
        return result;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public String discountPrices(String sentence, int discount) {
        String[] words = sentence.split(" ");
        for (int i = 0; i < words.length; i++) {
            String w = words[i];
            if (w.length() >= 2 && w.charAt(0) == '$') {
                boolean isPrice = true;
                for (int j = 1; j < w.length(); j++) {
                    char c = w.charAt(j);
                    if (!Character.isDigit(c)) {
                        isPrice = false;
                        break;
                    }
                }
                if (isPrice) {
                    long price = Long.parseLong(w.substring(1));
                    double discounted = price * (100 - discount) / 100.0;
                    words[i] = String.format("$%.2f", discounted);
                }
            }
        }
        return String.join(" ", words);
    }
}
```

## Python

```python
class Solution(object):
    def discountPrices(self, sentence, discount):
        """
        :type sentence: str
        :type discount: int
        :rtype: str
        """
        words = sentence.split(' ')
        res = []
        for w in words:
            if len(w) >= 2 and w[0] == '$' and w[1:].isdigit():
                price = int(w[1:])
                discounted_cents = price * (100 - discount)
                dollars = discounted_cents // 100
                cents = discounted_cents % 100
                res.append("${}.{:02d}".format(dollars, cents))
            else:
                res.append(w)
        return ' '.join(res)
```

## Python3

```python
class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        from decimal import Decimal, ROUND_HALF_UP, getcontext
        getcontext().prec = 30
        words = sentence.split(' ')
        for i, w in enumerate(words):
            if len(w) >= 2 and w[0] == '$' and w[1:].isdigit():
                original = Decimal(w[1:])
                factor = Decimal(100 - discount) / Decimal(100)
                new_price = (original * factor).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
                words[i] = f"${new_price}"
        return ' '.join(words)
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdio.h>

char* discountPrices(char* sentence, int discount) {
    int n = strlen(sentence);
    int bufSize = n * 2 + 10; // enough space for added characters
    char *res = (char*)malloc(bufSize);
    int ri = 0;
    int i = 0;

    while (i < n) {
        int start = i;
        while (i < n && sentence[i] != ' ') i++;
        int wlen = i - start;

        // Check if word is a price
        int isPrice = 0;
        if (wlen >= 2 && sentence[start] == '$') {
            int allDigits = 1;
            for (int k = start + 1; k < start + wlen; ++k) {
                if (!isdigit((unsigned char)sentence[k])) {
                    allDigits = 0;
                    break;
                }
            }
            if (allDigits) isPrice = 1;
        }

        if (isPrice) {
            // Extract numeric part
            char numStr[32];
            memcpy(numStr, sentence + start + 1, wlen - 1);
            numStr[wlen - 1] = '\0';
            long long price = atoll(numStr);

            // Apply discount using integer arithmetic (cents)
            long long discountedCents = price * (100 - discount); // price in cents after discount
            long long dollars = discountedCents / 100;
            long long cents = discountedCents % 100;

            char tmp[32];
            int len = snprintf(tmp, sizeof(tmp), "$%lld.%02lld", dollars, cents);
            memcpy(res + ri, tmp, len);
            ri += len;
        } else {
            // Copy original word
            memcpy(res + ri, sentence + start, wlen);
            ri += wlen;
        }

        if (i < n) { // copy space
            res[ri++] = ' ';
            i++; // skip the space
        }
    }

    res[ri] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string DiscountPrices(string sentence, int discount)
    {
        var words = sentence.Split(' ');
        var sb = new System.Text.StringBuilder();

        for (int i = 0; i < words.Length; i++)
        {
            string w = words[i];
            if (IsPrice(w))
            {
                decimal price = decimal.Parse(w.Substring(1));
                decimal discounted = price * (100 - discount) / 100m;
                w = "$" + discounted.ToString("0.00");
            }

            sb.Append(w);
            if (i + 1 < words.Length)
                sb.Append(' ');
        }

        return sb.ToString();
    }

    private bool IsPrice(string word)
    {
        if (word.Length < 2 || word[0] != '$')
            return false;
        for (int i = 1; i < word.Length; i++)
        {
            char c = word[i];
            if (c < '0' || c > '9')
                return false;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} sentence
 * @param {number} discount
 * @return {string}
 */
var discountPrices = function(sentence, discount) {
    const words = sentence.split(' ');
    const factor = (100 - discount) / 100;
    for (let i = 0; i < words.length; i++) {
        const w = words[i];
        if (/^\$\d+$/.test(w)) {
            const price = Number(w.slice(1));
            const newPrice = (price * factor).toFixed(2);
            words[i] = '$' + newPrice;
        }
    }
    return words.join(' ');
};
```

## Typescript

```typescript
function discountPrices(sentence: string, discount: number): string {
    const words = sentence.split(' ');
    for (let i = 0; i < words.length; i++) {
        const w = words[i];
        if (w.length > 1 && w[0] === '$') {
            const numPart = w.slice(1);
            if (/^\d+$/.test(numPart)) {
                const price = Number(numPart);
                const discounted = (price * (100 - discount) / 100).toFixed(2);
                words[i] = `$${discounted}`;
            }
        }
    }
    return words.join(' ');
}
```

## Php

```php
class Solution {

    /**
     * @param String $sentence
     * @param Integer $discount
     * @return String
     */
    function discountPrices($sentence, $discount) {
        $words = explode(' ', $sentence);
        foreach ($words as &$word) {
            if (preg_match('/^\$[0-9]+$/', $word)) {
                $num = substr($word, 1);
                $price = intval($num);
                $newPrice = $price * (100 - $discount) / 100.0;
                $word = '$' . number_format($newPrice, 2, '.', '');
            }
        }
        return implode(' ', $words);
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    func discountPrices(_ sentence: String, _ discount: Int) -> String {
        var words = sentence.split(separator: " ").map { String($0) }
        let factor = Double(100 - discount) / 100.0
        
        for i in 0..<words.count {
            let word = words[i]
            guard word.hasPrefix("$"), word.count > 1 else { continue }
            let numPart = word.dropFirst()
            
            var isNumber = true
            for ch in numPart {
                if ch < "0" || ch > "9" {
                    isNumber = false
                    break
                }
            }
            if !isNumber { continue }
            
            if let original = Double(numPart) {
                let discounted = original * factor
                let formatted = String(format: "$%.2f", discounted)
                words[i] = formatted
            }
        }
        
        return words.joined(separator: " ")
    }
}
```

## Kotlin

```kotlin
import java.util.Locale

class Solution {
    fun discountPrices(sentence: String, discount: Int): String {
        val words = sentence.split(' ')
        val result = StringBuilder()
        for ((i, w) in words.withIndex()) {
            var newWord = w
            if (w.length > 1 && w[0] == '$') {
                val numPart = w.substring(1)
                if (numPart.all { it.isDigit() }) {
                    val price = numPart.toLong()
                    val discounted = price * (100 - discount) / 100.0
                    newWord = "$" + String.format(Locale.US, "%.2f", discounted)
                }
            }
            result.append(newWord)
            if (i != words.lastIndex) result.append(' ')
        }
        return result.toString()
    }
}
```

## Dart

```dart
class Solution {
  String discountPrices(String sentence, int discount) {
    List<String> words = sentence.split(' ');
    for (int i = 0; i < words.length; i++) {
      String w = words[i];
      if (_isPrice(w)) {
        int original = int.parse(w.substring(1));
        double discounted = original * (100 - discount) / 100.0;
        String formatted = '\$' + discounted.toStringAsFixed(2);
        words[i] = formatted;
      }
    }
    return words.join(' ');
  }

  bool _isPrice(String w) {
    if (w.length < 2 || w[0] != '\$') return false;
    for (int i = 1; i < w.length; i++) {
      int code = w.codeUnitAt(i);
      if (code < 48 || code > 57) return false; // not a digit
    }
    return true;
  }
}
```

## Golang

```go
package main

import (
	"fmt"
	"strconv"
	"strings"
)

func discountPrices(sentence string, discount int) string {
	words := strings.Split(sentence, " ")
	for i, w := range words {
		if len(w) >= 2 && w[0] == '$' {
			numPart := w[1:]
			valid := true
			for _, ch := range numPart {
				if ch < '0' || ch > '9' {
					valid = false
					break
				}
			}
			if valid && len(numPart) > 0 {
				price, err := strconv.ParseInt(numPart, 10, 64)
				if err == nil {
					discountedCents := price * int64(100-discount)
					dollars := discountedCents / 100
					cents := discountedCents % 100
					words[i] = fmt.Sprintf("$%d.%02d", dollars, cents)
				}
			}
		}
	}
	return strings.Join(words, " ")
}
```

## Ruby

```ruby
def discount_prices(sentence, discount)
  factor = (100 - discount) / 100.0
  sentence.split(' ').map do |word|
    if word.start_with?('$') && word.length > 1 && word[1..-1].match?(/\A\d+\z/)
      price = word[1..-1].to_i
      discounted = price * factor
      "$#{format('%.2f', discounted)}"
    else
      word
    end
  end.join(' ')
end
```

## Scala

```scala
object Solution {
    def discountPrices(sentence: String, discount: Int): String = {
        val words = sentence.split(" ")
        val factor = (100 - discount).toDouble / 100.0
        for (i <- words.indices) {
            val w = words(i)
            if (w.length > 1 && w.charAt(0) == '$') {
                var j = 1
                var ok = true
                while (j < w.length && ok) {
                    if (!w.charAt(j).isDigit) ok = false
                    j += 1
                }
                if (ok) {
                    val price = w.substring(1).toLong
                    val discounted = price * factor
                    words(i) = f"$$${discounted}%.2f"
                }
            }
        }
        words.mkString(" ")
    }
}
```

## Rust

```rust
impl Solution {
    pub fn discount_prices(sentence: String, discount: i32) -> String {
        let factor = (100 - discount) as f64 / 100.0;
        let mut words: Vec<String> = sentence
            .split_whitespace()
            .map(|w| w.to_string())
            .collect();

        for word in &mut words {
            if let Some(rest) = word.strip_prefix('$') {
                if !rest.is_empty() && rest.chars().all(|c| c.is_ascii_digit()) {
                    // safe to unwrap because we checked all digits
                    let price: f64 = rest.parse::<f64>().unwrap();
                    let new_price = price * factor;
                    *word = format!("${:.2}", new_price);
                }
            }
        }

        words.join(" ")
    }
}
```

## Racket

```racket
(require racket/string)

(define/contract (discount-prices sentence discount)
  (-> string? exact-integer? string?)
  (let* ([words (string-split sentence " ")]
         [new-words
          (map (lambda (w)
                 (if (and (> (string-length w) 1)
                          (char=? (string-ref w 0) #\$))
                     (let ([rest (substring w 1)])
                       (if (and (not (zero? (string-length rest)))
                                (for/and ([c (in-string rest)])
                                  (and (char>=? c #\0) (char<=? c #\9))))
                           (let* ([price (string->number rest)]
                                  [factor (/ (- 100 discount) 100.0)]
                                  [new-price (* price factor)])
                             (format "$~,.2f" new-price))
                           w))
                     w))
               words)])
    (string-join new-words " ")))
```

## Erlang

```erlang
-spec discount_prices(unicode:unicode_binary(), integer()) -> unicode:unicode_binary().
discount_prices(Sentence, Discount) ->
    Words = binary:split(Sentence, <<" ">>, [global]),
    NewWords = [process_word(W, Discount) || W <- Words],
    binary:join(NewWords, <<" ">>).

process_word(Word, Discount) ->
    case Word of
        <<$$, Rest/binary>> when byte_size(Rest) > 0 ->
            case is_digits(Rest) of
                true -> format_price(Rest, Discount);
                false -> Word
            end;
        _ -> Word
    end.

is_digits(<<>>) -> true;
is_digits(<<C, Rest/binary>>) when C >= $0, C =< $9 -> is_digits(Rest);
is_digits(_) -> false.

format_price(Rest, Discount) ->
    Value = erlang:binary_to_integer(Rest),
    Discounted = (Value * (100 - Discount)) / 100.0,
    Formatted = io_lib:format("$~.2f", [Discounted]),
    list_to_binary(Formatted).
```

## Elixir

```elixir
defmodule Solution do
  @spec discount_prices(sentence :: String.t(), discount :: integer) :: String.t()
  def discount_prices(sentence, discount) do
    sentence
    |> String.split(" ")
    |> Enum.map(&process_word(&1, discount))
    |> Enum.join(" ")
  end

  defp process_word(word, discount) do
    if price_word?(word) do
      amount = word |> String.slice(1..-1) |> String.to_integer()
      discounted = amount * (100 - discount) / 100.0
      formatted = :io_lib.format("~.2f", [discounted]) |> List.to_string()
      "$" <> formatted
    else
      word
    end
  end

  defp price_word?(<<?$ , rest::binary>>) when byte_size(rest) > 0 do
    String.match?(rest, ~r/^\d+$/)
  end

  defp price_word?(_), do: false
end
```
