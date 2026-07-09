# 0902. Numbers At Most N Given Digit Set

## Cpp

```cpp
class Solution {
public:
    int atMostNGivenDigitSet(vector<string>& digits, int n) {
        string s = to_string(n);
        int L = s.size();
        int m = digits.size();
        vector<long long> pow(L + 1, 1);
        for (int i = 1; i <= L; ++i) pow[i] = pow[i - 1] * m;
        
        long long ans = 0;
        // numbers with length less than L
        for (int len = 1; len < L; ++len) ans += pow[len];
        
        // numbers with the same length as n
        for (int i = 0; i < L; ++i) {
            char cur = s[i];
            int smaller = 0;
            for (const string& d : digits) {
                if (d[0] < cur) ++smaller;
                else break; // digits are sorted
            }
            ans += (long long)smaller * pow[L - i - 1];
            
            bool exists = false;
            for (const string& d : digits) {
                if (d[0] == cur) { exists = true; break; }
            }
            if (!exists) return (int)ans;
        }
        // n itself can be formed
        ans += 1;
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int atMostNGivenDigitSet(String[] digits, int n) {
        String s = Integer.toString(n);
        int lenN = s.length();
        int base = digits.length;
        long[] pow = new long[lenN + 1];
        pow[0] = 1;
        for (int i = 1; i <= lenN; i++) {
            pow[i] = pow[i - 1] * base;
        }

        long ans = 0;
        // numbers with length less than lenN
        for (int l = 1; l < lenN; l++) {
            ans += pow[l];
        }

        // numbers with the same length
        for (int i = 0; i < lenN; i++) {
            char cur = s.charAt(i);
            int smaller = 0;
            boolean match = false;
            for (String d : digits) {
                char dc = d.charAt(0);
                if (dc < cur) {
                    smaller++;
                } else if (dc == cur) {
                    match = true;
                    break;
                }
            }
            ans += smaller * pow[lenN - i - 1];
            if (!match) {
                return (int) ans;
            }
        }

        // n itself is valid
        ans += 1;
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def atMostNGivenDigitSet(self, digits, n):
        """
        :type digits: List[str]
        :type n: int
        :rtype: int
        """
        s = str(n)
        K = len(s)
        D = len(digits)

        # precompute powers of D up to K
        powD = [1] * (K + 1)
        for i in range(1, K + 1):
            powD[i] = powD[i - 1] * D

        total = 0
        # numbers with length less than K
        for l in range(1, K):
            total += powD[l]

        # numbers with the same length as n
        for i, ch in enumerate(s):
            cnt_less = 0
            for d in digits:
                if d < ch:
                    cnt_less += 1
                else:
                    break  # digits are sorted
            remaining = K - i - 1
            total += cnt_less * powD[remaining]
            if ch not in digits:
                return total

        # n itself can be formed
        total += 1
        return total
```

## Python3

```python
from typing import List
import bisect

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        L = len(s)
        D = len(digits)
        ans = 0

        # numbers with length less than L
        for k in range(1, L):
            ans += D ** k

        digit_set = set(digits)

        for i, ch in enumerate(s):
            cnt_less = bisect.bisect_left(digits, ch)  # digits are sorted
            ans += cnt_less * (D ** (L - i - 1))
            if ch not in digit_set:
                break
        else:
            ans += 1  # n itself is valid

        return ans
```

## C

```c
#include <stdio.h>
#include <string.h>

int atMostNGivenDigitSet(char** digits, int digitsSize, int n) {
    char s[12];
    sprintf(s, "%d", n);
    int K = strlen(s);

    long long powArr[12];
    powArr[0] = 1;
    for (int i = 1; i <= K; ++i) {
        powArr[i] = powArr[i - 1] * digitsSize;
    }

    long long ans = 0;

    // numbers with length less than K
    for (int len = 1; len < K; ++len) {
        ans += powArr[len];
    }

    // numbers with the same length as n
    for (int i = 0; i < K; ++i) {
        int cntLess = 0;
        int hasEqual = 0;
        for (int j = 0; j < digitsSize; ++j) {
            char d = digits[j][0];
            if (d < s[i]) {
                cntLess++;
            } else if (d == s[i]) {
                hasEqual = 1;
            }
        }
        ans += (long long)cntLess * powArr[K - i - 1];
        if (!hasEqual) {
            return (int)ans;
        }
    }

    // n itself is valid
    ans += 1;
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int AtMostNGivenDigitSet(string[] digits, int n)
    {
        string s = n.ToString();
        int L = s.Length;
        int m = digits.Length;

        // Convert digit strings to chars for easy comparison (digits are sorted)
        char[] dchars = new char[m];
        for (int i = 0; i < m; i++)
            dchars[i] = digits[i][0];

        // Pre‑compute powers of m up to L
        long[] power = new long[L + 1];
        power[0] = 1;
        for (int i = 1; i <= L; i++)
            power[i] = power[i - 1] * m;

        long result = 0;

        // Count numbers with length less than L
        for (int len = 1; len < L; len++)
            result += power[len];

        // Process numbers with the same length as n
        bool prefixMatch = true;
        for (int i = 0; i < L; i++)
        {
            int cntLess = 0;
            while (cntLess < m && dchars[cntLess] < s[i])
                cntLess++;

            result += cntLess * power[L - i - 1];

            // Check if current digit of n exists in the set
            bool found = false;
            for (int j = 0; j < m; j++)
            {
                if (dchars[j] == s[i])
                {
                    found = true;
                    break;
                }
                if (dchars[j] > s[i]) // early exit thanks to sorting
                    break;
            }

            if (!found)
            {
                prefixMatch = false;
                break;
            }
        }

        if (prefixMatch)
            result += 1; // n itself is valid

        return (int)result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} digits
 * @param {number} n
 * @return {number}
 */
var atMostNGivenDigitSet = function(digits, n) {
    const s = n.toString();
    const K = s.length;
    const B = digits.length;
    let total = 0;

    // Count numbers with fewer digits than K
    for (let len = 1; len < K; ++len) {
        total += Math.pow(B, len);
    }

    // Process numbers with the same length as n
    for (let i = 0; i < K; ++i) {
        const ch = s[i];
        let cntLess = 0;
        for (const d of digits) {
            if (d < ch) cntLess++;
            else break; // digits are sorted
        }
        total += cntLess * Math.pow(B, K - i - 1);
        if (!digits.includes(ch)) {
            return total;
        }
    }

    // n itself can be formed using the digit set
    return total + 1;
};
```

## Typescript

```typescript
function atMostNGivenDigitSet(digits: string[], n: number): number {
    const s = n.toString();
    const L = s.length;
    const m = digits.length;
    let total = 0;

    // numbers with length less than L
    for (let k = 1; k < L; ++k) {
        total += Math.pow(m, k);
    }

    // helper: count digits smaller than ch (digits sorted)
    const countSmaller = (ch: string): number => {
        let cnt = 0;
        for (const d of digits) {
            if (d < ch) cnt++;
            else break; // since sorted
        }
        return cnt;
    };

    const digitSet = new Set(digits);

    // numbers with same length L
    for (let i = 0; i < L; ++i) {
        const cur = s[i];
        const smaller = countSmaller(cur);
        total += smaller * Math.pow(m, L - i - 1);
        if (!digitSet.has(cur)) {
            return total;
        }
    }

    // n itself is valid
    return total + 1;
}
```

## Php

```php
class Solution {
    /**
     * @param String[] $digits
     * @param Integer $n
     * @return Integer
     */
    function atMostNGivenDigitSet($digits, $n) {
        $s = strval($n);
        $len = strlen($s);
        $base = count($digits);
        $ans = 0;
        for ($i = 1; $i < $len; $i++) {
            $ans += (int)pow($base, $i);
        }
        for ($i = 0; $i < $len; $i++) {
            $c = $s[$i];
            $cntLess = 0;
            foreach ($digits as $d) {
                if ($d < $c) {
                    $cntLess++;
                } else {
                    break;
                }
            }
            $remaining = $len - $i - 1;
            $ans += $cntLess * (int)pow($base, $remaining);
            $found = false;
            foreach ($digits as $d) {
                if ($d == $c) {
                    $found = true;
                    break;
                }
            }
            if (!$found) {
                return $ans;
            }
        }
        $ans += 1;
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func atMostNGivenDigitSet(_ digits: [String], _ n: Int) -> Int {
        let s = Array(String(n))
        let m = s.count
        let dCount = digits.count
        
        // precompute powers of dCount
        var powArr = [Int](repeating: 1, count: m + 1)
        for i in 1...m {
            powArr[i] = powArr[i - 1] * dCount
        }
        
        var result = 0
        
        // numbers with length less than m
        if m > 1 {
            for k in 1..<m {
                result += powArr[k]
            }
        }
        
        // numbers with the same length as n
        for i in 0..<m {
            let cur = s[i]
            var cntLess = 0
            var exactMatch = false
            for dStr in digits {
                let dChar = dStr.first!
                if dChar < cur {
                    cntLess += 1
                } else if dChar == cur {
                    exactMatch = true
                    break
                } else {
                    break
                }
            }
            let remaining = m - i - 1
            result += cntLess * powArr[remaining]
            if !exactMatch {
                return result
            }
        }
        
        // n itself can be formed
        return result + 1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun atMostNGivenDigitSet(digits: Array<String>, n: Int): Int {
        val s = n.toString()
        val m = digits.size
        val len = s.length

        // precompute powers of m
        val pow = LongArray(len + 1)
        pow[0] = 1L
        for (i in 1..len) {
            pow[i] = pow[i - 1] * m
        }

        var ans = 0L

        // numbers with length less than len(s)
        for (l in 1 until len) {
            ans += pow[l]
        }

        // process numbers with the same length as n
        for (i in 0 until len) {
            val ch = s[i]
            var cntLess = 0
            for (d in digits) {
                if (d[0] < ch) cntLess++ else break
            }
            ans += cntLess * pow[len - i - 1]

            // check if current digit exists in the set
            var found = false
            for (d in digits) {
                if (d[0] == ch) { found = true; break }
            }
            if (!found) return ans.toInt()
        }

        // n itself can be formed
        ans += 1
        return ans.toInt()
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int atMostNGivenDigitSet(List<String> digits, int n) {
    String s = n.toString();
    int m = digits.length;

    // pre‑compute powers of m
    List<int> pow = List.filled(s.length + 1, 1);
    for (int i = 1; i <= s.length; ++i) {
      pow[i] = pow[i - 1] * m;
    }

    int total = 0;

    // numbers with fewer digits than n
    for (int len = 1; len < s.length; ++len) {
      total += pow[len];
    }

    // numbers with the same length as n
    for (int i = 0; i < s.length; ++i) {
      int curDigit = s.codeUnitAt(i) - 48; // convert char to int

      int smallerCount = 0;
      for (String d in digits) {
        int dv = d.codeUnitAt(0) - 48;
        if (dv < curDigit) {
          ++smallerCount;
        } else {
          break; // digits are sorted
        }
      }

      total += smallerCount * pow[s.length - i - 1];

      bool canMatch = false;
      for (String d in digits) {
        if (d == s[i]) {
          canMatch = true;
          break;
        }
      }
      if (!canMatch) {
        return total;
      }
    }

    // n itself can be formed using the digit set
    total += 1;
    return total;
  }
}
```

## Golang

```go
import "strconv"

func atMostNGivenDigitSet(digits []string, n int) int {
	s := strconv.Itoa(n)
	m := len(s)
	dlen := len(digits)

	// precompute powers of dlen
	pow := make([]int, m+1)
	pow[0] = 1
	for i := 1; i <= m; i++ {
		pow[i] = pow[i-1] * dlen
	}

	// numbers with length less than m
	total := 0
	for l := 1; l < m; l++ {
		total += pow[l]
	}

	// numbers with the same length as n
	for i := 0; i < m; i++ {
		cur := s[i]
		smallerCount := 0
		for _, dig := range digits {
			if dig[0] < cur {
				smallerCount++
			} else {
				break // digits are sorted
			}
		}
		remaining := m - i - 1
		total += smallerCount * pow[remaining]

		// if current digit not in the set, stop
		found := false
		for _, dig := range digits {
			if dig[0] == cur {
				found = true
				break
			}
		}
		if !found {
			return total
		}
	}

	// n itself is valid
	total++
	return total
}
```

## Ruby

```ruby
def at_most_n_given_digit_set(digits, n)
  m = digits.size
  s = n.to_s
  k = s.length

  total = 0
  (1...k).each { |len| total += m ** len }

  digit_vals = digits.map(&:to_i)

  (0...k).each do |i|
    cur = s[i].ord - 48
    cnt = digit_vals.count { |d| d < cur }
    total += cnt * (m ** (k - i - 1))
    return total unless digit_vals.include?(cur)
  end

  total + 1
end
```

## Scala

```scala
object Solution {
  def atMostNGivenDigitSet(digits: Array[String], n: Int): Int = {
    val D = digits.map(_.charAt(0)).sorted
    val s = n.toString
    val L = s.length
    val m = D.length

    // precompute powers of m
    val pow = new Array[Long](L + 1)
    pow(0) = 1L
    for (i <- 1 to L) {
      pow(i) = pow(i - 1) * m
    }

    var total: Long = 0L

    // numbers with length less than L
    for (k <- 1 until L) {
      total += pow(k)
    }

    var broken = false
    for (i <- 0 until L if !broken) {
      val c = s.charAt(i)

      // count digits in D smaller than c
      var cnt = 0
      var idx = 0
      while (idx < m && D(idx) < c) {
        cnt += 1
        idx += 1
      }
      total += cnt * pow(L - i - 1)

      // check if current digit exists in D
      var found = false
      var j = 0
      while (j < m && !found) {
        if (D(j) == c) found = true
        j += 1
      }
      if (!found) broken = true
    }

    if (!broken) total += 1

    total.toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn at_most_n_given_digit_set(digits: Vec<String>, n: i32) -> i32 {
        // Convert digit strings to their byte values for easy comparison
        let d_vals: Vec<u8> = digits.iter().map(|s| s.as_bytes()[0]).collect();
        let base = d_vals.len() as i64;

        let s = n.to_string();
        let k = s.len();
        let bytes = s.as_bytes();

        // Count numbers with length less than k
        let mut ans: i64 = 0;
        for len in 1..k {
            ans += base.pow(len as u32);
        }

        // Process numbers with the same length as n
        for (i, &b) in bytes.iter().enumerate() {
            // Count digits from D that are smaller than current digit of n
            let mut less_cnt = 0;
            for &d in &d_vals {
                if d < b {
                    less_cnt += 1;
                }
            }
            ans += (less_cnt as i64) * base.pow((k - i - 1) as u32);

            // If the current digit of n is not present in D, we cannot match further
            if !d_vals.contains(&b) {
                return ans as i32;
            }

            // If this is the last digit and all previous digits matched,
            // then n itself is a valid number.
            if i == k - 1 {
                ans += 1;
            }
        }

        ans as i32
    }
}
```

## Racket

```racket
(define/contract (at-most-n-given-digit-set digits n)
  (-> (listof string?) exact-integer? exact-integer?)
  (let* ((dlen (length digits))
         (s    (number->string n))
         (k    (string-length s)))
    ;; power helper
    (define (pow b e) (expt b e))
    ;; count numbers with length < k
    (define total-short
      (for/sum ([len (in-range 1 k)])
        (pow dlen len)))
    ;; process numbers with the same length as n
    (let loop ((pos 0) (acc total-short))
      (if (= pos k)
          (+ acc 1) ; all previous digits matched, so n itself is valid
          (let* ((cur-char (string-ref s pos))
                 (cur-str  (string cur-char))
                 ;; count of allowed digits smaller than current digit
                 (less-count
                  (length
                   (filter (lambda (d)
                             (< (char->integer (string-ref d 0))
                                (char->integer cur-char)))
                           digits))))
            (define new-acc (+ acc (* less-count (pow dlen (- k pos 1)))))
            (if (member cur-str digits)
                (loop (+ pos 1) new-acc)
                new-acc)))))
```

## Erlang

```erlang
-spec at_most_n_given_digit_set([binary()], integer()) -> integer().
at_most_n_given_digit_set(Digits, N) ->
    DigitsInt = [binary_to_integer(D) || D <- Digits],
    Base = length(DigitsInt),
    Slist = integer_to_list(N),
    SDigits = [C - $0 || C <- Slist],
    K = length(SDigits),

    CountLess = count_fewer(Base, K - 1, 0),
    CountSame = count_same_loop(DigitsInt, Base, SDigits, K - 1),

    CountLess + CountSame.

%% count numbers with lengths from 1 to Len (inclusive)
count_fewer(_, 0, Acc) -> Acc;
count_fewer(Base, Len, Acc) ->
    count_fewer(Base, Len - 1, Acc + pow(Base, Len)).

%% process numbers having the same length as N
count_same_loop(_DigitsInt, _Base, [], _Exp) -> 1; % all digits matched, include N itself
count_same_loop(DigitsInt, Base, [Cur|Rest], Exp) ->
    CntLess = length([D || D <- DigitsInt, D < Cur]),
    Add = CntLess * pow(Base, Exp),
    case lists:member(Cur, DigitsInt) of
        true -> Add + count_same_loop(DigitsInt, Base, Rest, Exp - 1);
        false -> Add
    end.

pow(_, 0) -> 1;
pow(Base, Exp) when Exp > 0 ->
    Base * pow(Base, Exp - 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec at_most_n_given_digit_set(digits :: [String.t()], n :: integer) :: integer
  def at_most_n_given_digit_set(digits, n) do
    d_ints = Enum.map(digits, &String.to_integer/1)
    s = Integer.to_string(n)
    k = String.length(s)
    m = length(d_ints)

    # numbers with fewer digits than n
    total_fewer =
      1..(k - 1)
      |> Enum.reduce(0, fn len, acc -> acc + pow(m, len) end)

    # numbers with the same number of digits
    {total_same, all_match} =
      s
      |> String.graphemes()
      |> Enum.with_index()
      |> Enum.reduce({total_fewer, true}, fn {ch, idx}, {acc, still_equal} ->
        cur = String.to_integer(ch)

        less_cnt = Enum.count(d_ints, fn d -> d < cur end)
        acc = acc + less_cnt * pow(m, k - idx - 1)

        if still_equal && Enum.member?(d_ints, cur) do
          {acc, true}
        else
          {acc, false}
        end
      end)

    if all_match do
      total_same + 1
    else
      total_same
    end
  end

  defp pow(_base, 0), do: 1
  defp pow(base, exp) when exp > 0 do
    Enum.reduce(1..exp, 1, fn _, acc -> acc * base end)
  end
end
```
