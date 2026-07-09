# 0043. Multiply Strings

## Cpp

```cpp
class Solution {
public:
    string multiply(string num1, string num2) {
        if (num1 == "0" || num2 == "0") return "0";
        int n = num1.size(), m = num2.size();
        vector<int> pos(n + m, 0);
        for (int i = n - 1; i >= 0; --i) {
            int a = num1[i] - '0';
            for (int j = m - 1; j >= 0; --j) {
                int b = num2[j] - '0';
                int sum = pos[i + j + 1] + a * b;
                pos[i + j + 1] = sum % 10;
                pos[i + j] += sum / 10;
            }
        }
        string result;
        int i = 0;
        while (i < pos.size() && pos[i] == 0) ++i;
        for (; i < pos.size(); ++i) result.push_back(pos[i] + '0');
        return result.empty() ? "0" : result;
    }
};
```

## Java

```java
class Solution {
    public String multiply(String num1, String num2) {
        if (num1.equals("0") || num2.equals("0")) return "0";
        int n = num1.length(), m = num2.length();
        int[] res = new int[n + m];
        for (int i = n - 1; i >= 0; i--) {
            int d1 = num1.charAt(i) - '0';
            for (int j = m - 1; j >= 0; j--) {
                int d2 = num2.charAt(j) - '0';
                res[i + j + 1] += d1 * d2;
            }
        }
        for (int i = res.length - 1; i > 0; i--) {
            int carry = res[i] / 10;
            res[i] %= 10;
            res[i - 1] += carry;
        }
        StringBuilder sb = new StringBuilder();
        int idx = 0;
        while (idx < res.length && res[idx] == 0) idx++;
        for (; idx < res.length; idx++) {
            sb.append(res[idx]);
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        n, m = len(num1), len(num2)
        res = [0] * (n + m)
        for i in range(n - 1, -1, -1):
            a = ord(num1[i]) - 48
            for j in range(m - 1, -1, -1):
                b = ord(num2[j]) - 48
                mul = a * b + res[i + j + 1]
                res[i + j + 1] = mul % 10
                res[i + j] += mul // 10
        i = 0
        while i < len(res) and res[i] == 0:
            i += 1
        return ''.join(map(str, res[i:]))
```

## Python3

```python
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        n, m = len(num1), len(num2)
        res = [0] * (n + m)
        for i in range(n - 1, -1, -1):
            d1 = ord(num1[i]) - 48
            for j in range(m - 1, -1, -1):
                d2 = ord(num2[j]) - 48
                mul = d1 * d2 + res[i + j + 1]
                res[i + j + 1] = mul % 10
                res[i + j] += mul // 10
        idx = 0
        while idx < len(res) and res[idx] == 0:
            idx += 1
        return ''.join(map(str, res[idx:]))
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* multiply(char* num1, char* num2) {
    if (!num1 || !num2) return NULL;
    if (num1[0] == '0' && num1[1] == '\0') {
        char *res = (char *)malloc(2);
        res[0] = '0';
        res[1] = '\0';
        return res;
    }
    if (num2[0] == '0' && num2[1] == '\0') {
        char *res = (char *)malloc(2);
        res[0] = '0';
        res[1] = '\0';
        return res;
    }

    int n = strlen(num1);
    int m = strlen(num2);
    int *pos = (int *)calloc(n + m, sizeof(int));
    if (!pos) return NULL;

    for (int i = n - 1; i >= 0; --i) {
        int d1 = num1[i] - '0';
        for (int j = m - 1; j >= 0; --j) {
            int d2 = num2[j] - '0';
            int sum = d1 * d2 + pos[i + j + 1];
            pos[i + j + 1] = sum % 10;
            pos[i + j] += sum / 10;
        }
    }

    int i = 0;
    while (i < n + m && pos[i] == 0) ++i;

    int len = n + m - i;
    if (len == 0) {
        char *res = (char *)malloc(2);
        res[0] = '0';
        res[1] = '\0';
        free(pos);
        return res;
    }

    char *result = (char *)malloc(len + 1);
    for (int k = 0; k < len; ++k) {
        result[k] = pos[i + k] + '0';
    }
    result[len] = '\0';

    free(pos);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public string Multiply(string num1, string num2)
    {
        if (num1 == "0" || num2 == "0")
            return "0";

        int n = num1.Length;
        int m = num2.Length;
        int[] pos = new int[n + m];

        for (int i = n - 1; i >= 0; i--)
        {
            int a = num1[i] - '0';
            for (int j = m - 1; j >= 0; j--)
            {
                int b = num2[j] - '0';
                int sum = a * b + pos[i + j + 1];
                pos[i + j + 1] = sum % 10;
                pos[i + j] += sum / 10;
            }
        }

        var sb = new System.Text.StringBuilder();
        int k = 0;
        while (k < pos.Length && pos[k] == 0)
            k++;

        for (; k < pos.Length; k++)
            sb.Append(pos[k]);

        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var multiply = function(num1, num2) {
    if (num1 === "0" || num2 === "0") return "0";
    const m = num1.length, n = num2.length;
    const res = new Array(m + n).fill(0);
    for (let i = m - 1; i >= 0; i--) {
        const d1 = num1.charCodeAt(i) - 48;
        for (let j = n - 1; j >= 0; j--) {
            const d2 = num2.charCodeAt(j) - 48;
            const sum = d1 * d2 + res[i + j + 1];
            res[i + j + 1] = sum % 10;
            res[i + j] += Math.floor(sum / 10);
        }
    }
    let idx = 0;
    while (idx < res.length - 1 && res[idx] === 0) idx++;
    return res.slice(idx).join('');
};
```

## Typescript

```typescript
function multiply(num1: string, num2: string): string {
    if (num1 === "0" || num2 === "0") return "0";
    const n = num1.length;
    const m = num2.length;
    const ans = new Array(n + m).fill(0);
    for (let i = n - 1; i >= 0; i--) {
        const a = num1.charCodeAt(i) - 48;
        for (let j = m - 1; j >= 0; j--) {
            const b = num2.charCodeAt(j) - 48;
            const sum = a * b + ans[i + j + 1];
            ans[i + j + 1] = sum % 10;
            ans[i + j] += Math.floor(sum / 10);
        }
    }
    let idx = 0;
    while (idx < ans.length && ans[idx] === 0) idx++;
    return ans.slice(idx).join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String $num1
     * @param String $num2
     * @return String
     */
    function multiply($num1, $num2) {
        if ($num1 === "0" || $num2 === "0") {
            return "0";
        }

        $n = strlen($num1);
        $m = strlen($num2);
        $res = array_fill(0, $n + $m, 0);

        for ($i = $n - 1; $i >= 0; $i--) {
            $digit1 = intval($num1[$i]);
            for ($j = $m - 1; $j >= 0; $j--) {
                $digit2 = intval($num2[$j]);
                $mul = $digit1 * $digit2 + $res[$i + $j + 1];
                $res[$i + $j + 1] = $mul % 10;
                $res[$i + $j] += intdiv($mul, 10);
            }
        }

        $resultStr = '';
        $started = false;
        foreach ($res as $digit) {
            if (!$started && $digit == 0) {
                continue;
            }
            $started = true;
            $resultStr .= (string)$digit;
        }

        return $resultStr === '' ? '0' : $resultStr;
    }
}
```

## Swift

```swift
class Solution {
    func multiply(_ num1: String, _ num2: String) -> String {
        if num1 == "0" || num2 == "0" { return "0" }
        
        let n1 = Array(num1.reversed()).map { Int(String($0))! }
        let n2 = Array(num2.reversed()).map { Int(String($0))! }
        var result = [Int](repeating: 0, count: n1.count + n2.count)
        
        for i in 0..<n2.count {
            for j in 0..<n1.count {
                let mul = n2[i] * n1[j] + result[i + j]
                result[i + j] = mul % 10
                result[i + j + 1] += mul / 10
            }
        }
        
        // Normalize any values >= 10 that may have accumulated
        for k in 0..<result.count - 1 {
            if result[k] >= 10 {
                result[k + 1] += result[k] / 10
                result[k] %= 10
            }
        }
        
        // Remove leading zeros (from the most significant side)
        while result.last == 0 && result.count > 1 {
            result.removeLast()
        }
        
        return result.reversed().map { String($0) }.joined()
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun multiply(num1: String, num2: String): String {
        if (num1 == "0" || num2 == "0") return "0"
        val n = num1.length
        val m = num2.length
        val result = IntArray(n + m)
        for (i in n - 1 downTo 0) {
            val d1 = num1[i] - '0'
            for (j in m - 1 downTo 0) {
                val d2 = num2[j] - '0'
                val sum = d1 * d2 + result[i + j + 1]
                result[i + j + 1] = sum % 10
                result[i + j] += sum / 10
            }
        }
        val sb = StringBuilder()
        var i = 0
        while (i < result.size && result[i] == 0) i++
        for (; i < result.size; i++) {
            sb.append(result[i])
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String multiply(String num1, String num2) {
    if (num1 == "0" || num2 == "0") return "0";

    int n = num1.length;
    int m = num2.length;
    List<int> ans = List.filled(n + m, 0);

    for (int i = n - 1; i >= 0; i--) {
      int d1 = num1.codeUnitAt(i) - 48;
      for (int j = m - 1; j >= 0; j--) {
        int d2 = num2.codeUnitAt(j) - 48;
        int mul = d1 * d2 + ans[i + j + 1];
        ans[i + j + 1] = mul % 10;
        ans[i + j] += mul ~/ 10;
      }
    }

    StringBuffer sb = StringBuffer();
    int idx = 0;
    while (idx < ans.length && ans[idx] == 0) idx++;
    for (; idx < ans.length; idx++) {
      sb.writeCharCode(ans[idx] + 48);
    }
    return sb.isEmpty ? "0" : sb.toString();
  }
}
```

## Golang

```go
package main

import "strings"

func multiply(num1 string, num2 string) string {
	if num1 == "0" || num2 == "0" {
		return "0"
	}
	n, m := len(num1), len(num2)
	res := make([]int, n+m)

	for i := n - 1; i >= 0; i-- {
		d1 := int(num1[i] - '0')
		for j := m - 1; j >= 0; j-- {
			d2 := int(num2[j] - '0')
			mul := d1 * d2
			p1, p2 := i+j, i+j+1
			sum := mul + res[p2]
			res[p2] = sum % 10
			res[p1] += sum / 10
		}
	}

	idx := 0
	for idx < len(res) && res[idx] == 0 {
		idx++
	}
	var sb strings.Builder
	for ; idx < len(res); idx++ {
		sb.WriteByte(byte(res[idx] + '0'))
	}
	return sb.String()
}
```

## Ruby

```ruby
def multiply(num1, num2)
  return "0" if num1 == "0" || num2 == "0"

  n = num1.length
  m = num2.length
  ans = Array.new(n + m, 0)

  (n - 1).downto(0) do |i|
    (m - 1).downto(0) do |j|
      mul = (num1[i].ord - 48) * (num2[j].ord - 48) + ans[i + j + 1]
      ans[i + j + 1] = mul % 10
      ans[i + j] += mul / 10
    end
  end

  idx = 0
  idx += 1 while idx < ans.length && ans[idx] == 0
  ans[idx..-1].join
end
```

## Scala

```scala
object Solution {
    def multiply(num1: String, num2: String): String = {
        if (num1 == "0" || num2 == "0") return "0"
        val n1 = num1.reverse.map(c => c - '0').toArray
        val n2 = num2.reverse.map(c => c - '0').toArray
        val m = n1.length
        val n = n2.length
        val res = new Array[Int](m + n)

        for (i <- 0 until n) {
            var carry = 0
            val d2 = n2(i)
            for (j <- 0 until m) {
                val sum = res(i + j) + d2 * n1(j) + carry
                res(i + j) = sum % 10
                carry = sum / 10
            }
            var k = i + m
            while (carry > 0) {
                val sum = res(k) + carry
                res(k) = sum % 10
                carry = sum / 10
                k += 1
            }
        }

        var idx = res.length - 1
        while (idx > 0 && res(idx) == 0) idx -= 1

        val sb = new StringBuilder
        for (i <- idx to 0 by -1) {
            sb.append(res(i))
        }
        sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn multiply(num1: String, num2: String) -> String {
        if num1 == "0" || num2 == "0" {
            return "0".to_string();
        }
        let n = num1.len();
        let m = num2.len();
        let bytes1 = num1.as_bytes();
        let bytes2 = num2.as_bytes();

        // result[i] holds the i-th digit (least significant first)
        let mut result = vec![0u32; n + m];

        for i in 0..m {
            let d2 = (bytes2[m - 1 - i] - b'0') as u32;
            for j in 0..n {
                let d1 = (bytes1[n - 1 - j] - b'0') as u32;
                let idx = i + j;
                let sum = result[idx] + d2 * d1;
                result[idx] = sum % 10;
                result[idx + 1] += sum / 10;
            }
        }

        // Propagate any remaining carries
        for k in 0..result.len() - 1 {
            if result[k] >= 10 {
                let carry = result[k] / 10;
                result[k] %= 10;
                result[k + 1] += carry;
            }
        }

        // Remove leading zeros (from the most significant side)
        while result.len() > 1 && *result.last().unwrap() == 0 {
            result.pop();
        }

        // Build the final string
        let mut ans = String::with_capacity(result.len());
        for &digit in result.iter().rev() {
            ans.push((digit as u8 + b'0') as char);
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (multiply num1 num2)
  (-> string? string? string?)
  (if (or (string=? num1 "0") (string=? num2 "0"))
      "0"
      (let* ((n (string-length num1))
             (m (string-length num2))
             (zero-code (char->integer #\0))
             (ans (make-vector (+ n m) 0)))
        ;; multiply each digit
        (for ([i (in-range m)])
          (let* ((d2 (- (char->integer (string-ref num2 (- m i 1))) zero-code))
                 (carry 0))
            (for ([j (in-range n)])
              (let* ((d1 (- (char->integer (string-ref num1 (- n j 1))) zero-code))
                     (pos (+ i j))
                     (total (+ (vector-ref ans pos) (* d1 d2) carry))
                     (digit (modulo total 10))
                     (new-carry (quotient total 10)))
                (vector-set! ans pos digit)
                (set! carry new-carry)))
            (when (> carry 0)
              (let ([pos (+ i n)])
                (vector-set! ans pos (+ (vector-ref ans pos) carry))))))
        ;; normalize carries
        (for ([k (in-range (- (vector-length ans) 1))])
          (let* ((val (vector-ref ans k))
                 (carry (quotient val 10)))
            (when (> carry 0)
              (vector-set! ans (+ k 1) (+ (vector-ref ans (+ k 1)) carry)))
            (vector-set! ans k (modulo val 10))))
        ;; find most significant non‑zero digit
        (let loop ((idx (- (vector-length ans) 1)))
          (if (and (> idx 0) (= (vector-ref ans idx) 0))
              (loop (- idx 1))
              idx)
          )
        => (define msd-index
            (let loop ((idx (- (vector-length ans) 1)))
              (if (and (> idx 0) (= (vector-ref ans idx) 0))
                  (loop (- idx 1))
                  idx)))
        ;; build result string
        (let ((chars
               (let build ((i msd-index) (lst '()))
                 (if (< i 0)
                     lst
                     (build (- i 1)
                            (cons (integer->char (+ (vector-ref ans i) zero-code))
                                  lst))))))
          (list->string chars))))
```

## Erlang

```erlang
-spec multiply(Num1 :: unicode:unicode_binary(), Num2 :: unicode:unicode_binary()) -> unicode:unicode_binary().
multiply(Num1, Num2) ->
    case {Num1, Num2} of
        {<<"0">>, _} -> <<"0">>;
        {_, <<"0">>} -> <<"0">>;
        _ ->
            Digits1 = lists:reverse([C - $0 || <<C>> <= Num1]),
            Digits2 = lists:reverse([C - $0 || <<C>> <= Num2]),
            Len1 = length(Digits1),
            Len2 = length(Digits2),
            Res0 = array:new(Len1 + Len2, {default, 0}),
            Res = mul_digits(Digits2, Digits1, Res0, Len2, 0),
            ListRes = [array:get(I, Res) || I <- lists:seq(0, Len1 + Len2 - 1)],
            Trimmed = trim_leading_zeros(lists:reverse(ListRes)),
            list_to_binary([D + $0 || D <- Trimmed])
    end.

mul_digits(_Digits2, _Digits1, Res, Len2, I) when I >= Len2 -> Res;
mul_digits(Digits2, Digits1, Res, Len2, I) ->
    D2 = lists:nth(I + 1, Digits2),
    Res1 = mul_one_digit(D2, Digits1, Res, I, 0),
    mul_digits(Digits2, Digits1, Res1, Len2, I + 1).

mul_one_digit(_D2, [], Res, _Ioff, _J) -> Res;
mul_one_digit(D2, [D1 | Rest], Res, Ioff, J) ->
    Pos = Ioff + J,
    Existing = array:get(Pos, Res),
    Prod = D2 * D1 + Existing,
    NewDigit = Prod rem 10,
    Carry = Prod div 10,
    ResTmp = array:set(Pos, NewDigit, Res),
    ResAfterCarry = propagate_carry(ResTmp, Pos + 1, Carry),
    mul_one_digit(D2, Rest, ResAfterCarry, Ioff, J + 1).

propagate_carry(Res, _Pos, 0) -> Res;
propagate_carry(Res, Pos, Carry) ->
    Existing = array:get(Pos, Res),
    Sum = Existing + Carry,
    NewDigit = Sum rem 10,
    NewCarry = Sum div 10,
    ResTmp = array:set(Pos, NewDigit, Res),
    propagate_carry(ResTmp, Pos + 1, NewCarry).

trim_leading_zeros([0]) -> [0];
trim_leading_zeros([0 | Rest]) -> trim_leading_zeros(Rest);
trim_leading_zeros(L) -> L.
```

## Elixir

```elixir
defmodule Solution do
  @spec multiply(num1 :: String.t(), num2 :: String.t()) :: String.t()
  def multiply(num1, num2) do
    if num1 == "0" or num2 == "0" do
      "0"
    else
      rev1 = String.graphemes(num1) |> Enum.map(&String.to_integer/1) |> Enum.reverse()
      rev2 = String.graphemes(num2) |> Enum.map(&String.to_integer/1) |> Enum.reverse()

      n = length(rev1)
      m = length(rev2)
      len = n + m

      # initialize answer array with zeros
      ans = :array.new(len, default: 0)

      # accumulate raw products into the answer positions
      ans =
        Enum.with_index(rev2)
        |> Enum.reduce(ans, fn {d2, i}, acc ->
          Enum.with_index(rev1)
          |> Enum.reduce(acc, fn {d1, j}, acc2 ->
            idx = i + j
            cur = :array.get(idx, acc2)
            :array.set(idx, cur + d1 * d2, acc2)
          end)
        end)

      # propagate carries
      ans =
        Enum.reduce(0..len - 1, ans, fn i, acc ->
          val = :array.get(i, acc)
          carry = div(val, 10)
          new_val = rem(val, 10)
          acc = :array.set(i, new_val, acc)

          if i + 1 < len do
            next = :array.get(i + 1, acc) + carry
            :array.set(i + 1, next, acc)
          else
            acc
          end
        end)

      # find most significant non‑zero digit
      last =
        Enum.reduce_while((len - 1)..0, nil, fn i, _ ->
          if :array.get(i, ans) != 0 do
            {:halt, i}
          else
            {:cont, nil}
          end
        end)

      case last do
        nil -> "0"
        l ->
          digits =
            Enum.map(0..l, fn i -> :array.get(i, ans) end)
            |> Enum.reverse()

          Enum.map_join(digits, &Integer.to_string/1)
      end
    end
  end
end
```
