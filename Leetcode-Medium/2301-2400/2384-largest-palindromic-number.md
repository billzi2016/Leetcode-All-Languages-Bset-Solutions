# 2384. Largest Palindromic Number

## Cpp

```cpp
class Solution {
public:
    string largestPalindromic(string num) {
        vector<int> cnt(10, 0);
        for (char c : num) cnt[c - '0']++;
        
        string left;
        // Build the left half using pairs from highest digit to lowest
        for (int d = 9; d >= 0; --d) {
            int pairs = cnt[d] / 2;
            if (pairs > 0) left.append(pairs, char('0' + d));
            cnt[d] -= pairs * 2; // keep at most one leftover
        }
        
        // Choose the middle digit: highest remaining digit with count > 0
        char mid = 0;
        for (int d = 9; d >= 0; --d) {
            if (cnt[d] > 0) { mid = char('0' + d); break; }
        }
        
        string right = left;
        reverse(right.begin(), right.end());
        
        string result = left;
        if (mid) result.push_back(mid);
        result += right;
        
        // If the result is empty or starts with '0', the answer should be "0"
        if (result.empty() || result[0] == '0') return "0";
        return result;
    }
};
```

## Java

```java
class Solution {
    public String largestPalindromic(String num) {
        int[] cnt = new int[10];
        for (char c : num.toCharArray()) {
            cnt[c - '0']++;
        }
        StringBuilder left = new StringBuilder();
        // Build the left half from highest digit to lowest
        for (int d = 9; d >= 0; d--) {
            int pairs = cnt[d] / 2;
            if (pairs > 0) {
                char ch = (char) ('0' + d);
                for (int i = 0; i < pairs; i++) {
                    left.append(ch);
                }
                cnt[d] -= pairs * 2;
            }
        }
        // Choose the middle digit (largest with an odd remaining count)
        char mid = '\0';
        for (int d = 9; d >= 0; d--) {
            if (cnt[d] % 2 == 1) {
                mid = (char) ('0' + d);
                break;
            }
        }
        String leftStr = left.toString();
        StringBuilder ans = new StringBuilder();
        ans.append(leftStr);
        if (mid != '\0') {
            ans.append(mid);
        }
        ans.append(new StringBuilder(leftStr).reverse());
        String res = ans.toString();
        // If the result starts with '0', the only valid palindrome is "0"
        if (res.length() == 0 || res.charAt(0) == '0') {
            return "0";
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def largestPalindromic(self, num):
        """
        :type num: str
        :rtype: str
        """
        cnt = [0] * 10
        for ch in num:
            cnt[int(ch)] += 1

        left_parts = []
        # build the left half using as many pairs as possible, from high to low digit
        for d in range(9, -1, -1):
            pairs = cnt[d] // 2
            if pairs:
                left_parts.append(str(d) * pairs)
                cnt[d] -= pairs * 2

        # choose the largest possible middle digit (if any)
        middle = ''
        for d in range(9, -1, -1):
            if cnt[d]:
                middle = str(d)
                break

        left = ''.join(left_parts)
        right = left[::-1]
        result = left + middle + right

        # avoid leading zeros; the only valid zero-only palindrome is "0"
        if result and result[0] == '0':
            return "0"
        return result
```

## Python3

```python
class Solution:
    def largestPalindromic(self, num: str) -> str:
        cnt = [0] * 10
        for ch in num:
            cnt[ord(ch) - 48] += 1

        left_parts = []
        # build the left half using pairs of digits from high to low
        for d in range(9, -1, -1):
            pairs = cnt[d] // 2
            if pairs:
                if d == 0 and not left_parts:
                    # avoid leading zeros; keep them for possible middle digit
                    continue
                left_parts.append(str(d) * pairs)
                cnt[d] -= pairs * 2

        # choose the largest possible middle digit (if any)
        mid = ''
        for d in range(9, -1, -1):
            if cnt[d] > 0:
                mid = str(d)
                break

        left = ''.join(left_parts)
        res = left + mid + left[::-1]

        # handle the all‑zero case
        if not res or res[0] == '0':
            return "0"
        return res
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* largestPalindromic(char* num) {
    int cnt[10] = {0};
    int n = strlen(num);
    for (int i = 0; i < n; ++i) {
        cnt[num[i] - '0']++;
    }

    char *left = (char*)malloc(n + 1);
    int left_len = 0;

    // Add pairs from 9 to 1
    for (int d = 9; d >= 1; --d) {
        int pairs = cnt[d] / 2;
        if (pairs > 0) {
            memset(left + left_len, '0' + d, pairs);
            left_len += pairs;
            cnt[d] -= pairs * 2;
        }
    }

    // If we already have a non‑zero leading digit, we can use zero pairs
    if (left_len > 0) {
        int zero_pairs = cnt[0] / 2;
        if (zero_pairs > 0) {
            memset(left + left_len, '0', zero_pairs);
            left_len += zero_pairs;
            cnt[0] -= zero_pairs * 2;
        }
    }

    // Choose middle digit (largest remaining)
    char mid = 0;
    for (int d = 9; d >= 0; --d) {
        if (cnt[d] > 0) {
            mid = '0' + d;
            break;
        }
    }

    int total_len = left_len * 2 + (mid ? 1 : 0);
    char *res = (char*)malloc(total_len + 1);

    // Copy left part
    memcpy(res, left, left_len);
    int pos = left_len;

    // Middle digit if any
    if (mid) {
        res[pos++] = mid;
    }

    // Append reversed left part
    for (int i = left_len - 1; i >= 0; --i) {
        res[pos++] = left[i];
    }
    res[total_len] = '\0';

    free(left);
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string LargestPalindromic(string num) {
        int[] cnt = new int[10];
        foreach (char c in num) cnt[c - '0']++;

        var leftBuilder = new System.Text.StringBuilder();

        // Add pairs for digits 9 to 1
        for (int d = 9; d >= 1; d--) {
            int pairs = cnt[d] / 2;
            if (pairs > 0) {
                leftBuilder.Append(new string((char)('0' + d), pairs));
                cnt[d] -= pairs * 2;
            }
        }

        // Add zero pairs only if we already have a non‑zero digit on the sides
        int zeroPairs = cnt[0] / 2;
        if (zeroPairs > 0 && leftBuilder.Length > 0) {
            leftBuilder.Append(new string('0', zeroPairs));
            cnt[0] -= zeroPairs * 2;
        }

        // Choose the middle digit: highest remaining digit
        char middle = '\0';
        for (int d = 9; d >= 0; d--) {
            if (cnt[d] > 0) {
                middle = (char)('0' + d);
                break;
            }
        }

        string left = leftBuilder.ToString();

        // If no pairs were used, the answer is just the highest digit present
        if (left.Length == 0) {
            return middle == '\0' ? "0" : middle.ToString();
        }

        // Build right side by reversing left
        char[] revArr = left.ToCharArray();
        System.Array.Reverse(revArr);
        string right = new string(revArr);

        if (middle != '\0')
            return left + middle + right;
        else
            return left + right;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} num
 * @return {string}
 */
var largestPalindromic = function(num) {
    const cnt = new Array(10).fill(0);
    for (let i = 0; i < num.length; ++i) {
        cnt[num.charCodeAt(i) - 48]++;
    }
    
    let left = '';
    // add pairs for digits 9 to 1
    for (let d = 9; d >= 1; --d) {
        const pairs = Math.floor(cnt[d] / 2);
        if (pairs > 0) {
            left += String(d).repeat(pairs);
            cnt[d] -= pairs * 2;
        }
    }
    // add zero pairs only if we already have a non‑zero prefix
    if (left.length > 0) {
        const zeroPairs = Math.floor(cnt[0] / 2);
        if (zeroPairs > 0) {
            left += '0'.repeat(zeroPairs);
            cnt[0] -= zeroPairs * 2;
        }
    }
    
    // choose the middle digit: highest remaining digit
    let mid = '';
    for (let d = 9; d >= 0; --d) {
        if (cnt[d] > 0) {
            mid = String(d);
            break;
        }
    }
    
    const right = left.split('').reverse().join('');
    const result = left + mid + right;
    
    // handle the all‑zero case
    return result[0] === '0' ? '0' : result;
};
```

## Typescript

```typescript
function largestPalindromic(num: string): string {
    const cnt = new Array(10).fill(0);
    for (const ch of num) {
        cnt[ch.charCodeAt(0) - 48]++;
    }

    let left = '';
    // build the left half using pairs from highest digit to lowest
    for (let d = 9; d >= 0; d--) {
        const pairs = Math.floor(cnt[d] / 2);
        if (pairs > 0) {
            left += String(d).repeat(pairs);
            cnt[d] -= pairs * 2;
        }
    }

    // choose the middle digit (largest remaining with odd count)
    let mid = '';
    for (let d = 9; d >= 0; d--) {
        if (cnt[d] > 0) {
            mid = String(d);
            break;
        }
    }

    const right = left.split('').reverse().join('');
    const result = left + mid + right;

    // If the result starts with '0', the only valid palindrome is "0"
    return result[0] === '0' ? '0' : result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $num
     * @return String
     */
    function largestPalindromic($num) {
        $cnt = array_fill(0, 10, 0);
        $n = strlen($num);
        for ($i = 0; $i < $n; $i++) {
            $d = intval($num[$i]);
            $cnt[$d]++;
        }

        $left = '';
        // build left half from largest to smallest digit
        for ($d = 9; $d >= 0; $d--) {
            $pair = intdiv($cnt[$d], 2);
            if ($d == 0 && $left === '') {
                // avoid leading zeros
                $pair = 0;
            }
            if ($pair > 0) {
                $left .= str_repeat((string)$d, $pair);
                $cnt[$d] -= $pair * 2;
            }
        }

        // choose middle digit (largest remaining)
        $mid = '';
        for ($d = 9; $d >= 0; $d--) {
            if ($cnt[$d] > 0) {
                $mid = (string)$d;
                break;
            }
        }

        $right = strrev($left);
        $result = $left . $mid . $right;

        // handle all-zero case
        if ($result === '' || $result[0] === '0') {
            return "0";
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func largestPalindromic(_ num: String) -> String {
        var cnt = [Int](repeating: 0, count: 10)
        for ch in num {
            if let d = ch.wholeNumberValue {
                cnt[d] += 1
            }
        }
        
        var left = ""
        // Build the left half from largest digit to smallest
        for d in stride(from: 9, through: 0, by: -1) {
            let pairs = cnt[d] / 2
            if pairs > 0 {
                let ch = Character("\(d)")
                left.append(String(repeating: ch, count: pairs))
                cnt[d] -= pairs * 2
            }
        }
        
        // Choose the middle digit (largest remaining digit)
        var middle = ""
        for d in stride(from: 9, through: 0, by: -1) {
            if cnt[d] > 0 {
                middle = "\(d)"
                break
            }
        }
        
        let right = String(left.reversed())
        var result = left + middle + right
        
        // If the result would start with '0', the only valid answer is "0"
        if result.first == "0" {
            return "0"
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun largestPalindromic(num: String): String {
        val cnt = IntArray(10)
        for (c in num) {
            cnt[c - '0']++
        }
        val left = StringBuilder()
        // add pairs from 9 to 1 first
        for (d in 9 downTo 1) {
            val pair = cnt[d] / 2
            repeat(pair) { left.append('0' + d) }
            cnt[d] -= pair * 2
        }
        // handle zeros only if we already have some non-zero digit on the sides
        if (left.isNotEmpty()) {
            val zeroPair = cnt[0] / 2
            repeat(zeroPair) { left.append('0') }
            cnt[0] -= zeroPair * 2
        }
        // choose middle digit, largest possible
        var middle = ""
        for (d in 9 downTo 0) {
            if (cnt[d] > 0) {
                middle = ('0' + d).toString()
                break
            }
        }
        val leftStr = left.toString()
        val rightStr = leftStr.reversed()
        // If result is empty (should not happen), return "0"
        return if (leftStr.isEmpty() && middle.isEmpty()) "0" else leftStr + middle + rightStr
    }
}
```

## Dart

```dart
class Solution {
  String largestPalindromic(String num) {
    List<int> cnt = List.filled(10, 0);
    for (int i = 0; i < num.length; ++i) {
      cnt[num.codeUnitAt(i) - 48]++;
    }

    // Find the middle digit (largest with odd count)
    String mid = '';
    for (int d = 9; d >= 0; --d) {
      if (cnt[d] % 2 == 1) {
        mid = String.fromCharCode(48 + d);
        break;
      }
    }

    // Build the left half using pairs, from high to low digit
    StringBuffer left = StringBuffer();
    for (int d = 9; d >= 1; --d) {
      int pairs = cnt[d] ~/ 2;
      if (pairs > 0) {
        String ch = String.fromCharCode(48 + d);
        for (int i = 0; i < pairs; ++i) left.write(ch);
      }
    }

    // Handle zeros separately to avoid leading zeroes
    int zeroPairs = cnt[0] ~/ 2;
    if (left.isNotEmpty && zeroPairs > 0) {
      for (int i = 0; i < zeroPairs; ++i) left.write('0');
    }

    String leftStr = left.toString();

    // If no non‑zero part was added
    if (leftStr.isEmpty) {
      if (mid.isNotEmpty) return mid;
      return '0';
    }

    String rightStr = leftStr.split('').reversed.join();
    return leftStr + mid + rightStr;
  }
}
```

## Golang

```go
package main

import (
	"strings"
)

func largestPalindromic(num string) string {
	cnt := [10]int{}
	for i := 0; i < len(num); i++ {
		cnt[num[i]-'0']++
	}

	var left strings.Builder
	// add pairs of digits from 9 to 1
	for d := 9; d >= 1; d-- {
		pairs := cnt[d] / 2
		if pairs > 0 {
			left.WriteString(strings.Repeat(string('0'+byte(d)), pairs))
		}
	}
	// add zero pairs only if we already have a non‑zero left part
	if left.Len() > 0 {
		pairsZero := cnt[0] / 2
		if pairsZero > 0 {
			left.WriteString(strings.Repeat("0", pairsZero))
		}
	}

	// choose the middle digit (largest with an odd remaining count)
	var mid byte = 0
	for d := 9; d >= 0; d-- {
		if cnt[d]%2 == 1 {
			mid = '0' + byte(d)
			break
		}
	}

	leftStr := left.String()
	revLeft := reverse(leftStr)

	var res strings.Builder
	res.WriteString(leftStr)
	if mid != 0 {
		res.WriteByte(mid)
	}
	res.WriteString(revLeft)

	if res.Len() == 0 {
		return "0"
	}
	return res.String()
}

func reverse(s string) string {
	b := []byte(s)
	for i, n := 0, len(b); i < n/2; i++ {
		b[i], b[n-1-i] = b[n-1-i], b[i]
	}
	return string(b)
}
```

## Ruby

```ruby
def largest_palindromic(num)
  cnt = Array.new(10, 0)
  num.each_byte { |b| cnt[b - 48] += 1 }

  left_parts = []
  9.downto(0) do |d|
    pairs = cnt[d] / 2
    left_parts << d.to_s * pairs if pairs > 0
  end
  left = left_parts.join

  mid = ''
  9.downto(0) do |d|
    if cnt[d].odd?
      mid = d.to_s
      break
    end
  end

  # Discard zero-only left part to avoid leading zeros
  if !left.empty? && left.each_char.none? { |ch| ch != '0' }
    left = ''
  end

  result = left + mid + left.reverse
  result.empty? ? "0" : result
end
```

## Scala

```scala
object Solution {
    def largestPalindromic(num: String): String = {
        val cnt = new Array[Int](10)
        for (ch <- num) {
            cnt(ch - '0') += 1
        }

        val leftBuilder = new StringBuilder
        for (d <- 9 to 0 by -1) {
            while (cnt(d) >= 2) {
                leftBuilder.append((d + '0').toChar)
                cnt(d) -= 2
            }
        }

        var middle = ""
        breakable {
            for (d <- 9 to 0 by -1) {
                if (cnt(d) > 0) {
                    middle = ((d + '0').toChar).toString
                    break
                }
            }
        }

        val left = leftBuilder.toString()
        val right = left.reverse
        val result = left + middle + right

        if (result.isEmpty || result.charAt(0) == '0') "0" else result
    }

    // Utility for breaking out of loops
    import scala.util.control.Breaks.{break, breakable}
}
```

## Rust

```rust
impl Solution {
    pub fn largest_palindromic(num: String) -> String {
        let mut cnt = [0usize; 10];
        for b in num.bytes() {
            cnt[(b - b'0') as usize] += 1;
        }

        // Build the left half using the maximum possible pairs from high to low digits
        let mut left = String::new();
        for d in (0..=9).rev() {
            let pair = cnt[d] / 2;
            if pair > 0 {
                for _ in 0..pair {
                    left.push((b'0' + d as u8) as char);
                }
            }
            cnt[d] %= 2; // keep only the leftover (0 or 1)
        }

        // Choose the largest possible middle digit, if any
        let mut middle = String::new();
        for d in (0..=9).rev() {
            if cnt[d] > 0 {
                middle.push((b'0' + d as u8) as char);
                break;
            }
        }

        // Right half is the reverse of left
        let right: String = left.chars().rev().collect();

        let result = format!("{}{}{}", left, middle, right);

        // If the result would start with '0', the only valid answer is "0"
        if result.starts_with('0') {
            "0".to_string()
        } else {
            result
        }
    }
}
```

## Racket

```racket
(define/contract (largest-palindromic num)
  (-> string? string?)
  (let* ([counts (make-vector 10 0)]
         [join
          (lambda (lst)
            (if (null? lst) "" (apply string-append lst)))])
    ;; count digits
    (for ([c (in-string num)])
      (let* ([d (- (char->integer c) (char->integer #\0))])
        (vector-set! counts d (+ 1 (vector-ref counts d)))))
    ;; build left parts (stored in ascending order)
    (define left-parts '())
    (for ([d (in-range 9 -1 -1)])
      (let* ([cnt (vector-ref counts d)]
             [pairs (quotient cnt 2)])
        (when (> pairs 0)
          (set! left-parts
                (cons (make-string pairs
                                   (integer->char (+ (char->integer #\0) d)))
                      left-parts))
          (vector-set! counts d (- cnt (* 2 pairs))))))
    ;; middle digit (largest remaining)
    (define middle "")
    (for ([d (in-range 9 -1 -1)])
      (when (> (vector-ref counts d) 0)
        (set! middle
              (string (integer->char (+ (char->integer #\0) d))))
        (break)))
    ;; construct palindrome
    (define left-str  (join (reverse left-parts))) ; descending order
    (define right-str (join left-parts))           ; mirror
    (define result (string-append left-str middle right-str))
    (cond [(zero? (string-length result)) "0"]
          [(and (> (string-length result) 1)
                (char=? (string-ref result 0) #\0))
           (if (> (string-length middle) 0) middle "0")]
          [else result])))
```

## Erlang

```erlang
-spec largest_palindromic(Num :: unicode:unicode_binary()) -> unicode:unicode_binary().
largest_palindromic(Num) ->
    Counts = lists:foldl(
        fun(C, Acc) ->
            D = C - $0,
            maps:update_with(D, fun(V) -> V + 1 end, 1, Acc)
        end,
        #{},
        binary_to_list(Num)),
    Left = lists:foldl(
        fun(Digit, Acc) ->
            Count = maps:get(Digit, Counts, 0),
            PairCount = Count div 2,
            Acc ++ lists:duplicate(PairCount, $0 + Digit)
        end,
        [],
        lists:seq(9, 0, -1)),
    Middle =
        case [Digit || Digit <- lists:seq(9, 0, -1), (maps:get(Digit, Counts, 0) rem 2) =:= 1] of
            [] -> [];
            [First | _] -> [$0 + First]
        end,
    PalList = Left ++ Middle ++ lists:reverse(Left),
    case PalList of
        [] -> <<"">>;
        [H | _] when H == $0 -> <<"0">>;
        _ -> list_to_binary(PalList)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec largest_palindromic(num :: String.t) :: String.t
  def largest_palindromic(num) do
    counts =
      Enum.reduce(String.graphemes(num), %{}, fn ch, acc ->
        d = String.to_integer(ch)
        Map.update(acc, d, 1, &(&1 + 1))
      end)

    {parts, mid_digit} =
      Enum.reduce(9..0, {[], nil}, fn d, {ps, m} ->
        cnt = Map.get(counts, d, 0)
        pair = div(cnt, 2)

        ps =
          if pair > 0 do
            [String.duplicate(Integer.to_string(d), pair) | ps]
          else
            ps
          end

        m =
          if rem(cnt, 2) == 1 and is_nil(m) do
            Integer.to_string(d)
          else
            m
          end

        {ps, m}
      end)

    left = parts |> Enum.reverse() |> Enum.join()

    left =
      if left != "" and String.at(left, 0) == "0" do
        ""
      else
        left
      end

    middle = mid_digit || ""

    result = left <> middle <> String.reverse(left)

    if result == "", do: "0", else: result
  end
end
```
