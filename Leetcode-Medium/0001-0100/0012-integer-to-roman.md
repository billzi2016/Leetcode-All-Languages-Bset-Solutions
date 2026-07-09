# 0012. Integer to Roman

## Cpp

```cpp
class Solution {
public:
    string intToRoman(int num) {
        static const vector<pair<int, string>> vals = {
            {1000, "M"}, {900, "CM"}, {500, "D"}, {400, "CD"},
            {100,  "C"}, {90,  "XC"}, {50,  "L"}, {40,  "XL"},
            {10,   "X"}, {9,   "IX"}, {5,   "V"}, {4,   "IV"},
            {1,    "I"}
        };
        string res;
        for (const auto& [value, symbol] : vals) {
            while (num >= value) {
                res += symbol;
                num -= value;
            }
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public String intToRoman(int num) {
        int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] symbols = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < values.length && num > 0; i++) {
            while (num >= values[i]) {
                num -= values[i];
                sb.append(symbols[i]);
            }
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        vals = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
            (1, "I")
        ]
        res = []
        for value, symbol in vals:
            if num == 0:
                break
            count, num = divmod(num, value)
            res.append(symbol * count)
        return "".join(res)
```

## Python3

```python
class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        result = []
        for v, s in zip(values, symbols):
            if num == 0:
                break
            count, num = divmod(num, v)
            result.append(s * count)
        return "".join(result)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* intToRoman(int num) {
    static const int values[] = {1000,900,500,400,100,90,50,40,10,9,5,4,1};
    static const char *symbols[] = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
    char *res = (char *)malloc(20); // sufficient for max length + null terminator
    char *p = res;
    
    for (int i = 0; i < 13; ++i) {
        while (num >= values[i]) {
            const char *s = symbols[i];
            while (*s) {
                *p++ = *s++;
            }
            num -= values[i];
        }
    }
    *p = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string IntToRoman(int num)
    {
        int[] values = { 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 };
        string[] symbols = { "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" };

        var result = new System.Text.StringBuilder();

        for (int i = 0; i < values.Length && num > 0; i++)
        {
            while (num >= values[i])
            {
                num -= values[i];
                result.Append(symbols[i]);
            }
        }

        return result.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    const values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
    const symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];
    let result = "";
    for (let i = 0; i < values.length; i++) {
        while (num >= values[i]) {
            num -= values[i];
            result += symbols[i];
        }
    }
    return result;
};
```

## Typescript

```typescript
function intToRoman(num: number): string {
    const values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
    const symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];
    let result = "";
    for (let i = 0; i < values.length && num > 0; i++) {
        while (num >= values[i]) {
            num -= values[i];
            result += symbols[i];
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $num
     * @return String
     */
    function intToRoman($num) {
        $values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
        $symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];
        $result = "";
        for ($i = 0; $i < count($values); $i++) {
            while ($num >= $values[$i]) {
                $result .= $symbols[$i];
                $num -= $values[$i];
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func intToRoman(_ num: Int) -> String {
        let values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        let symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        var n = num
        var result = ""
        for i in 0..<values.count {
            while n >= values[i] {
                n -= values[i]
                result += symbols[i]
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun intToRoman(num: Int): String {
        val values = intArrayOf(1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        val symbols = arrayOf("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
        var n = num
        val sb = StringBuilder()
        for (i in values.indices) {
            while (n >= values[i]) {
                n -= values[i]
                sb.append(symbols[i])
            }
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String intToRoman(int num) {
    final List<int> values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
    final List<String> symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];
    StringBuffer sb = StringBuffer();
    for (int i = 0; i < values.length && num > 0; i++) {
      while (num >= values[i]) {
        sb.write(symbols[i]);
        num -= values[i];
      }
    }
    return sb.toString();
  }
}
```

## Golang

```go
func intToRoman(num int) string {
    values := []int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}
    symbols := []string{"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"}
    var result string
    for i := 0; i < len(values); i++ {
        for num >= values[i] {
            result += symbols[i]
            num -= values[i]
        }
    }
    return result
}
```

## Ruby

```ruby
def int_to_roman(num)
  values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
  symbols = %w[M CM D CD C XC L XL X IX V IV I]
  result = +''
  values.each_with_index do |v, i|
    while num >= v
      result << symbols[i]
      num -= v
    end
  end
  result
end
```

## Scala

```scala
object Solution {
    def intToRoman(num: Int): String = {
        val values = Array(1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        val symbols = Array("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
        var n = num
        val sb = new StringBuilder
        for (i <- values.indices) {
            while (n >= values(i)) {
                sb.append(symbols(i))
                n -= values(i)
            }
        }
        sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn int_to_roman(mut num: i32) -> String {
        let values = [
            1000, 900, 500, 400, 100, 90,
            50, 40, 10, 9, 5, 4, 1,
        ];
        let symbols = [
            "M", "CM", "D", "CD", "C", "XC",
            "L", "XL", "X", "IX", "V", "IV", "I",
        ];
        let mut result = String::new();
        for (i, &v) in values.iter().enumerate() {
            while num >= v {
                result.push_str(symbols[i]);
                num -= v;
            }
        }
        result
    }
}
```

## Racket

```racket
(define/contract (int-to-roman num)
  (-> exact-integer? string?)
  (let* ((values '(1000 900 500 400 100 90 50 40 10 9 5 4 1))
         (symbols '("M" "CM" "D" "CD" "C" "XC" "L" "XL" "X" "IX" "V" "IV" "I")))
    (let loop ((n num) (i 0) (acc ""))
      (if (= n 0)
          acc
          (let* ((v (list-ref values i))
                 (s (list-ref symbols i)))
            (if (>= n v)
                (loop (- n v) i (string-append acc s))
                (loop n (+ i 1) acc)))))))
```

## Erlang

```erlang
-module(solution).
-export([int_to_roman/1]).

-spec int_to_roman(Num :: integer()) -> unicode:unicode_binary().
int_to_roman(Num) ->
    iolist_to_binary(build(Num, values())).

values() ->
    [{1000, <<"M">>},
     {900,  <<"CM">>},
     {500,  <<"D">>},
     {400,  <<"CD">>},
     {100,  <<"C">>},
     {90,   <<"XC">>},
     {50,   <<"L">>},
     {40,   <<"XL">>},
     {10,   <<"X">>},
     {9,    <<"IX">>},
     {5,    <<"V">>},
     {4,    <<"IV">>},
     {1,    <<"I">>}].

build(0, _) -> [];
build(N, [{Val, Sym}|Rest]) when N >= Val ->
    [Sym | build(N - Val, [{Val, Sym}|Rest])];
build(N, [_|Rest]) ->
    build(N, Rest).
```

## Elixir

```elixir
defmodule Solution do
  @spec int_to_roman(num :: integer) :: String.t()
  def int_to_roman(num) do
    vals = [
      {1000, "M"},
      {900, "CM"},
      {500, "D"},
      {400, "CD"},
      {100, "C"},
      {90, "XC"},
      {50, "L"},
      {40, "XL"},
      {10, "X"},
      {9, "IX"},
      {5, "V"},
      {4, "IV"},
      {1, "I"}
    ]

    do_convert(num, vals)
  end

  defp do_convert(0, _), do: ""

  defp do_convert(num, [{value, sym} | rest]) when num >= value do
    sym <> do_convert(num - value, [{value, sym} | rest])
  end

  defp do_convert(num, [_ | rest]), do: do_convert(num, rest)
end
```
