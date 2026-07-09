# 1017. Convert to Base -2

## Cpp

```cpp
class Solution {
public:
    string baseNeg2(int n) {
        if (n == 0) return "0";
        string res;
        while (n != 0) {
            int rem = n % -2;
            n /= -2;
            if (rem < 0) {
                rem += 2;
                ++n;
            }
            res.push_back('0' + rem);
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
```

## Java

```java
class Solution {
    public String baseNeg2(int n) {
        if (n == 0) return "0";
        StringBuilder sb = new StringBuilder();
        while (n != 0) {
            int remainder = n % -2;
            n /= -2;
            if (remainder < 0) {
                remainder += 2;
                n += 1;
            }
            sb.append(remainder);
        }
        return sb.reverse().toString();
    }
}
```

## Python

```python
class Solution(object):
    def baseNeg2(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return "0"
        digits = []
        while n != 0:
            n, r = divmod(n, -2)
            if r < 0:
                n += 1
                r += 2
            digits.append(str(r))
        return ''.join(reversed(digits))
```

## Python3

```python
class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        digits = []
        while n != 0:
            r = n % -2
            n //= -2
            if r < 0:
                r += 2
                n += 1
            digits.append(str(r))
        return ''.join(reversed(digits))
```

## C

```c
#include <stdlib.h>

char* baseNeg2(int n) {
    if (n == 0) {
        char *res = (char*)malloc(2);
        res[0] = '0';
        res[1] = '\0';
        return res;
    }
    char buf[70];
    int idx = 0;
    while (n != 0) {
        int r = n % -2;
        n /= -2;
        if (r < 0) {
            r += 2;
            n += 1;
        }
        buf[idx++] = '0' + r;
    }
    char *res = (char*)malloc(idx + 1);
    for (int i = 0; i < idx; ++i) {
        res[i] = buf[idx - 1 - i];
    }
    res[idx] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string BaseNeg2(int n) {
        if (n == 0) return "0";
        var sb = new System.Text.StringBuilder();
        while (n != 0) {
            int bit = n & 1;
            sb.Append(bit);
            n = (n - bit) / -2;
        }
        // reverse the built string
        char[] arr = sb.ToString().ToCharArray();
        System.Array.Reverse(arr);
        return new string(arr);
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {string}
 */
var baseNeg2 = function(n) {
    if (n === 0) return "0";
    const digits = [];
    while (n !== 0) {
        let rem = n % -2;
        n = Math.trunc(n / -2);
        if (rem < 0) {
            rem += 2;
            n += 1;
        }
        digits.push(rem);
    }
    return digits.reverse().join('');
};
```

## Typescript

```typescript
function baseNeg2(n: number): string {
    if (n === 0) return "0";
    const digits: number[] = [];
    while (n !== 0) {
        const remainder = n & 1;
        digits.push(remainder);
        n = (n - remainder) / -2;
    }
    return digits.reverse().join('');
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @return String
     */
    function baseNeg2($n) {
        if ($n == 0) return "0";
        $res = "";
        while ($n != 0) {
            $rem = $n & 1;
            $res .= (string)$rem;
            $n = intdiv($n - $rem, -2);
        }
        return strrev($res);
    }
}
```

## Swift

```swift
class Solution {
    func baseNeg2(_ n: Int) -> String {
        if n == 0 { return "0" }
        var num = n
        var digits: [String] = []
        while num != 0 {
            var remainder = num % -2
            num /= -2
            if remainder < 0 {
                remainder += 2
                num += 1
            }
            digits.append(String(remainder))
        }
        return digits.reversed().joined()
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun baseNeg2(n: Int): String {
        if (n == 0) return "0"
        var num = n
        val sb = StringBuilder()
        while (num != 0) {
            var remainder = num % -2
            var quotient = num / -2
            if (remainder < 0) {
                remainder += 2
                quotient += 1
            }
            sb.append(remainder)
            num = quotient
        }
        return sb.reverse().toString()
    }
}
```

## Dart

```dart
class Solution {
  String baseNeg2(int n) {
    if (n == 0) return "0";
    List<int> digits = [];
    while (n != 0) {
      int remainder = n & 1;
      digits.add(remainder);
      n = (n - remainder) ~/ -2;
    }
    StringBuffer sb = StringBuffer();
    for (int i = digits.length - 1; i >= 0; i--) {
      sb.write(digits[i]);
    }
    return sb.toString();
  }
}
```

## Golang

```go
func baseNeg2(n int) string {
	if n == 0 {
		return "0"
	}
	var digits []byte
	for n != 0 {
		digit := n & 1
		digits = append(digits, byte('0'+digit))
		n = (n - digit) / -2
	}
	for i, j := 0, len(digits)-1; i < j; i, j = i+1, j-1 {
		digits[i], digits[j] = digits[j], digits[i]
	}
	return string(digits)
}
```

## Ruby

```ruby
# @param {Integer} n
# @return {String}
def base_neg2(n)
  return "0" if n == 0
  digits = []
  while n != 0
    r = n & 1
    digits << r.to_s
    n = (n - r) / -2
  end
  digits.reverse.join
end
```

## Scala

```scala
object Solution {
    def baseNeg2(n: Int): String = {
        if (n == 0) return "0"
        val sb = new StringBuilder
        var num = n
        while (num != 0) {
            var rem = num % -2
            var q = num / -2
            if (rem < 0) {
                rem += 2
                q += 1
            }
            sb.append(rem)
            num = q
        }
        sb.reverse.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn base_neg2(mut n: i32) -> String {
        if n == 0 {
            return "0".to_string();
        }
        let mut digits = Vec::new();
        while n != 0 {
            let mut rem = n % -2;
            n /= -2;
            if rem < 0 {
                rem += 2;
                n += 1;
            }
            digits.push((rem as u8 + b'0') as char);
        }
        digits.iter().rev().collect()
    }
}
```

## Racket

```racket
(define/contract (base-neg2 n)
  (-> exact-integer? string?)
  (cond [(zero? n) "0"]
        [else
         (let loop ((num n) (digits '()))
           (if (zero? num)
               (list->string (reverse digits))
               (let* ([r (remainder num -2)]
                      [adj-r (if (< r 0) (+ r 2) r)]
                      [next (/ (- num adj-r) -2)])
                 (loop next
                       (cons (if (= adj-r 0) #\0 #\1) digits))))])))
```

## Erlang

```erlang
-module(solution).
-export([base_neg2/1]).

-spec base_neg2(N :: integer()) -> unicode:unicode_binary().
base_neg2(0) ->
    <<"0">>;
base_neg2(N) when is_integer(N) ->
    list_to_binary(lists:reverse(build(N, []))).

build(0, Acc) ->
    Acc;
build(N, Acc) ->
    R = N band 1,
    NewN = (N - R) div -2,
    build(NewN, [R + $0 | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec base_neg2(n :: integer) :: String.t()
  def base_neg2(n) do
    digits = convert(n, [])
    Enum.map_join(digits, "", &Integer.to_string/1)
  end

  defp convert(0, []), do: [0]
  defp convert(0, acc), do: acc
  defp convert(n, acc) do
    r = Bitwise.band(n, 1)
    convert(div(n - r, -2), [r | acc])
  end
end
```
