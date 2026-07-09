# 0537. Complex Number Multiplication

## Cpp

```cpp
class Solution {
public:
    string complexNumberMultiply(string num1, string num2) {
        auto parse = [](const string& s) -> pair<int,int> {
            size_t plusPos = s.find('+', 1); // start from index 1 to skip possible leading '-'
            int real = stoi(s.substr(0, plusPos));
            int imag = stoi(s.substr(plusPos + 1, s.size() - plusPos - 2)); // exclude trailing 'i'
            return {real, imag};
        };
        auto [a, b] = parse(num1);
        auto [c, d] = parse(num2);
        int real = a * c - b * d;
        int imag = a * d + b * c;
        return to_string(real) + "+" + to_string(imag) + "i";
    }
};
```

## Java

```java
class Solution {
    public String complexNumberMultiply(String num1, String num2) {
        int[] p1 = parse(num1);
        int[] p2 = parse(num2);
        int real = p1[0] * p2[0] - p1[1] * p2[1];
        int imag = p1[0] * p2[1] + p1[1] * p2[0];
        return real + "+" + imag + "i";
    }
    
    private int[] parse(String s) {
        int plusIdx = s.indexOf('+', 1); // skip possible leading sign
        int real = Integer.parseInt(s.substring(0, plusIdx));
        int imag = Integer.parseInt(s.substring(plusIdx + 1, s.length() - 1)); // exclude trailing 'i'
        return new int[]{real, imag};
    }
}
```

## Python

```python
class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def parse(s):
            real_str, imag_str = s.split('+')
            return int(real_str), int(imag_str[:-1])
        
        a, b = parse(num1)
        c, d = parse(num2)
        real = a * c - b * d
        imag = a * d + b * c
        return f"{real}+{imag}i"
```

## Python3

```python
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a_real, a_im = num1.split('+')
        b_real, b_im = num2.split('+')
        a_real = int(a_real)
        a_im = int(a_im[:-1])  # remove trailing 'i'
        b_real = int(b_real)
        b_im = int(b_im[:-1])
        real_part = a_real * b_real - a_im * b_im
        imag_part = a_real * b_im + a_im * b_real
        return f"{real_part}+{imag_part}i"
```

## C

```c
#include <stdio.h>
#include <stdlib.h>

char* complexNumberMultiply(char* num1, char* num2) {
    int a, b, c, d;
    sscanf(num1, "%d+%di", &a, &b);
    sscanf(num2, "%d+%di", &c, &d);
    int real = a * c - b * d;
    int imag = a * d + b * c;
    char* res = (char*)malloc(30);
    sprintf(res, "%d+%di", real, imag);
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string ComplexNumberMultiply(string num1, string num2)
    {
        (int a, int b) = Parse(num1);
        (int c, int d) = Parse(num2);

        int real = a * c - b * d;
        int imag = a * d + b * c;

        return $"{real}+{imag}i";
    }

    private (int, int) Parse(string s)
    {
        // Find the '+' that separates real and imaginary parts,
        // starting from index 1 to skip a possible leading sign.
        int plusIdx = s.IndexOf('+', 1);
        int real = int.Parse(s.Substring(0, plusIdx));
        // Exclude the trailing 'i' character.
        int imag = int.Parse(s.Substring(plusIdx + 1, s.Length - plusIdx - 2));
        return (real, imag);
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
var complexNumberMultiply = function(num1, num2) {
    const parse = (s) => {
        const plusIdx = s.indexOf('+');
        const real = parseInt(s.substring(0, plusIdx), 10);
        const imag = parseInt(s.substring(plusIdx + 1, s.length - 1), 10); // drop trailing 'i'
        return [real, imag];
    };
    
    const [a, b] = parse(num1);
    const [c, d] = parse(num2);
    
    const realPart = a * c - b * d;
    const imagPart = a * d + b * c;
    
    return `${realPart}+${imagPart}i`;
};
```

## Typescript

```typescript
function complexNumberMultiply(num1: string, num2: string): string {
    const parse = (s: string): [number, number] => {
        const plusIdx = s.indexOf('+', 1);
        const real = parseInt(s.slice(0, plusIdx), 10);
        const imag = parseInt(s.slice(plusIdx + 1, s.length - 1), 10);
        return [real, imag];
    };
    
    const [a, b] = parse(num1);
    const [c, d] = parse(num2);
    
    const realPart = a * c - b * d;
    const imagPart = a * d + b * c;
    
    return `${realPart}+${imagPart}i`;
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
    function complexNumberMultiply($num1, $num2) {
        // Parse first number
        $pos = strpos($num1, '+');
        $a = intval(substr($num1, 0, $pos));
        $b = intval(substr($num1, $pos + 1, -1)); // remove trailing 'i'

        // Parse second number
        $pos = strpos($num2, '+');
        $c = intval(substr($num2, 0, $pos));
        $d = intval(substr($num2, $pos + 1, -1));

        // Multiply: (a+bi)*(c+di) = (ac - bd) + (ad + bc)i
        $real = $a * $c - $b * $d;
        $imag = $a * $d + $b * $c;

        return $real . '+' . $imag . 'i';
    }
}
```

## Swift

```swift
class Solution {
    func complexNumberMultiply(_ num1: String, _ num2: String) -> String {
        func parse(_ s: String) -> (Int, Int) {
            guard let plusIdx = s.firstIndex(of: "+") else { return (0, 0) }
            let realPart = String(s[..<plusIdx])
            var imagPart = String(s[s.index(after: plusIdx)...])
            imagPart.removeLast() // remove trailing 'i'
            let real = Int(realPart)!
            let imag = Int(imagPart)!
            return (real, imag)
        }
        
        let (a, b) = parse(num1)
        let (c, d) = parse(num2)
        
        let realResult = a * c - b * d
        let imagResult = a * d + b * c
        
        return "\(realResult)+\(imagResult)i"
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun complexNumberMultiply(num1: String, num2: String): String {
        fun parse(s: String): Pair<Int, Int> {
            val plusIdx = s.indexOf('+', 1) // start from 1 to skip possible leading '-'
            val real = s.substring(0, plusIdx).toInt()
            val imag = s.substring(plusIdx + 1, s.length - 1).toInt() // drop trailing 'i'
            return Pair(real, imag)
        }
        val (a, b) = parse(num1)
        val (c, d) = parse(num2)
        val realRes = a * c - b * d
        val imagRes = a * d + b * c
        return "${realRes}+${imagRes}i"
    }
}
```

## Dart

```dart
class Solution {
  String complexNumberMultiply(String num1, String num2) {
    // Helper to parse a complex string into its real and imaginary parts.
    List<int> parse(String s) {
      int plusIdx = s.indexOf('+', 1); // start search after possible leading sign
      int real = int.parse(s.substring(0, plusIdx));
      int imag = int.parse(s.substring(plusIdx + 1, s.length - 1)); // exclude trailing 'i'
      return [real, imag];
    }

    var a = parse(num1);
    var b = parse(num2);

    int realPart = a[0] * b[0] - a[1] * b[1];
    int imagPart = a[0] * b[1] + a[1] * b[0];

    return '${realPart}+${imagPart}i';
  }
}
```

## Golang

```go
import (
	"strconv"
	"strings"
)

func complexNumberMultiply(num1 string, num2 string) string {
	parse := func(s string) (int, int) {
		plusIdx := strings.Index(s, "+")
		realPart, _ := strconv.Atoi(s[:plusIdx])
		imagPart, _ := strconv.Atoi(s[plusIdx+1 : len(s)-1])
		return realPart, imagPart
	}
	a, b := parse(num1)
	c, d := parse(num2)
	realRes := a*c - b*d
	imagRes := a*d + b*c
	return strconv.Itoa(realRes) + "+" + strconv.Itoa(imagRes) + "i"
}
```

## Ruby

```ruby
def complex_number_multiply(num1, num2)
  a, b = num1.match(/(-?\d+)\+(-?\d+)i/).captures.map(&:to_i)
  c, d = num2.match(/(-?\d+)\+(-?\d+)i/).captures.map(&:to_i)
  real = a * c - b * d
  imag = a * d + b * c
  "#{real}+#{imag}i"
end
```

## Scala

```scala
object Solution {
  def complexNumberMultiply(num1: String, num2: String): String = {
    def parse(s: String): (Int, Int) = {
      val plusIdx = s.indexOf('+', 1)
      val real = s.substring(0, plusIdx).toInt
      val imag = s.substring(plusIdx + 1, s.length - 1).toInt
      (real, imag)
    }

    val (a, b) = parse(num1)
    val (c, d) = parse(num2)

    val realPart = a * c - b * d
    val imagPart = a * d + b * c

    s"$realPart+$imagPart" + "i"
  }
}
```

## Rust

```rust
impl Solution {
    pub fn complex_number_multiply(num1: String, num2: String) -> String {
        fn parse(s: &str) -> (i32, i32) {
            let plus = s.find('+').unwrap();
            let real = s[..plus].parse::<i32>().unwrap();
            let imag = s[plus + 1..s.len() - 1].parse::<i32>().unwrap(); // skip trailing 'i'
            (real, imag)
        }

        let (a, b) = parse(&num1);
        let (c, d) = parse(&num2);

        let real = a * c - b * d;
        let imag = a * d + b * c;

        format!("{}+{}i", real, imag)
    }
}
```

## Racket

```racket
(define/contract (complex-number-multiply num1 num2)
  (-> string? string? string?)
  (let* ([m1 (regexp-match #rx"^(-?\\d+)\\+(-?\\d+)i$" num1)]
         [a (string->number (list-ref m1 1))]
         [b (string->number (list-ref m1 2))]
         [m2 (regexp-match #rx"^(-?\\d+)\\+(-?\\d+)i$" num2)]
         [c (string->number (list-ref m2 1))]
         [d (string->number (list-ref m2 2))]
         [real (- (* a c) (* b d))]
         [imag (+ (* a d) (* b c))])
    (format "~a+~ai" real imag)))
```

## Erlang

```erlang
-spec complex_number_multiply(Num1 :: unicode:unicode_binary(), Num2 :: unicode:unicode_binary()) -> unicode:unicode_binary().
complex_number_multiply(Num1, Num2) ->
    {A, B} = parse_complex(Num1),
    {C, D} = parse_complex(Num2),
    Real = A * C - B * D,
    Imag = A * D + B * C,
    iolist_to_binary(io_lib:format("~p+~pi", [Real, Imag])).

parse_complex(Num) ->
    {ok, [RStr, IStr]} =
        re:run(
            Num,
            <<"^([-+]?[0-9]+)\\+([-+]?[0-9]+)i$">>,
            [{capture, [1, 2], list}]
        ),
    {list_to_integer(RStr), list_to_integer(IStr)}.
```

## Elixir

```elixir
defmodule Solution do
  @spec complex_number_multiply(num1 :: String.t(), num2 :: String.t()) :: String.t()
  def complex_number_multiply(num1, num2) do
    {a, b} = parse_complex(num1)
    {c, d} = parse_complex(num2)

    real = a * c - b * d
    imag = a * d + b * c

    "#{real}+#{imag}i"
  end

  defp parse_complex(str) do
    [real_part, imag_part] =
      str
      |> String.split("+", parts: 2)

    real = String.to_integer(real_part)
    imag = imag_part |> String.trim_trailing("i") |> String.to_integer()
    {real, imag}
  end
end
```
