# 3602. Hexadecimal and Hexatrigesimal Conversion

## Cpp

```cpp
class Solution {
public:
    string toBase(long long x, int b) {
        if (x == 0) return "0";
        const char* digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        string res;
        while (x > 0) {
            int d = x % b;
            res.push_back(digits[d]);
            x /= b;
        }
        reverse(res.begin(), res.end());
        return res;
    }

    string concatHex36(int n) {
        long long sq = 1LL * n * n;
        long long cu = sq * n; // n^3
        string hexPart = toBase(sq, 16);
        string base36Part = toBase(cu, 36);
        return hexPart + base36Part;
    }
};
```

## Java

```java
class Solution {
    private static final char[] DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ".toCharArray();

    private String toBase(long value, int base) {
        if (value == 0) return "0";
        StringBuilder sb = new StringBuilder();
        while (value > 0) {
            int rem = (int) (value % base);
            sb.append(DIGITS[rem]);
            value /= base;
        }
        return sb.reverse().toString();
    }

    public String concatHex36(int n) {
        long sq = (long) n * n;
        long cube = (long) n * n * n;
        String hex = toBase(sq, 16);
        String base36 = toBase(cube, 36);
        return hex + base36;
    }
}
```

## Python

```python
class Solution(object):
    def concatHex36(self, n):
        """
        :type n: int
        :rtype: str
        """
        # convert to uppercase hexadecimal
        hex_part = format(n * n, 'X')
        
        # convert to base-36 (hexatrigesimal)
        def to_base(x, b):
            if x == 0:
                return "0"
            digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            res = []
            while x > 0:
                res.append(digits[x % b])
                x //= b
            return ''.join(reversed(res))
        
        base36_part = to_base(n * n * n, 36)
        return hex_part + base36_part
```

## Python3

```python
class Solution:
    def concatHex36(self, n: int) -> str:
        def to_base(x: int, b: int) -> str:
            if x == 0:
                return "0"
            digits = []
            while x > 0:
                rem = x % b
                if rem < 10:
                    digits.append(chr(ord('0') + rem))
                else:
                    digits.append(chr(ord('A') + rem - 10))
                x //= b
            return ''.join(reversed(digits))

        hex_part = to_base(n * n, 16)
        base36_part = to_base(n * n * n, 36)
        return hex_part + base36_part
```

## C

```c
#include <stdlib.h>
#include <string.h>

static char* toBase(long long x, int base) {
    const char *digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    char buf[65];
    int idx = 0;
    if (x == 0) {
        buf[idx++] = '0';
    } else {
        while (x > 0) {
            int d = x % base;
            buf[idx++] = digits[d];
            x /= base;
        }
    }
    char *res = (char*)malloc(idx + 1);
    for (int i = 0; i < idx; ++i) {
        res[i] = buf[idx - 1 - i];
    }
    res[idx] = '\0';
    return res;
}

char* concatHex36(int n) {
    long long sq = (long long)n * n;
    long long cube = (long long)n * n * n;
    char *hex = toBase(sq, 16);
    char *base36 = toBase(cube, 36);
    size_t len1 = strlen(hex);
    size_t len2 = strlen(base36);
    char *result = (char*)malloc(len1 + len2 + 1);
    memcpy(result, hex, len1);
    memcpy(result + len1, base36, len2);
    result[len1 + len2] = '\0';
    free(hex);
    free(base36);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public string ConcatHex36(int n)
    {
        long square = (long)n * n;
        long cube = (long)n * n * n;

        string hex = ToBase(square, 16);
        string base36 = ToBase(cube, 36);

        return hex + base36;
    }

    private string ToBase(long value, int @base)
    {
        if (value == 0) return "0";

        var chars = new System.Text.StringBuilder();
        while (value > 0)
        {
            long rem = value % @base;
            char c = rem < 10 ? (char)('0' + rem) : (char)('A' + (rem - 10));
            chars.Append(c);
            value /= @base;
        }

        // reverse the built string
        var arr = chars.ToString().ToCharArray();
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
var concatHex36 = function(n) {
    const hex = (n * n).toString(16).toUpperCase();
    const base36 = (n * n * n).toString(36).toUpperCase();
    return hex + base36;
};
```

## Typescript

```typescript
function concatHex36(n: number): string {
    const hex = (n * n).toString(16).toUpperCase();
    const base36 = (n * n * n).toString(36).toUpperCase();
    return hex + base36;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return String
     */
    function concatHex36($n) {
        $hex = $this->toBase($n * $n, 16);
        $base36 = $this->toBase($n * $n * $n, 36);
        return $hex . $base36;
    }

    private function toBase(int $x, int $b): string {
        if ($x === 0) {
            return "0";
        }
        $digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ';
        $res = '';
        while ($x > 0) {
            $rem = $x % $b;
            $res = $digits[$rem] . $res;
            $x = intdiv($x, $b);
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func concatHex36(_ n: Int) -> String {
        func toBase(_ num: Int, _ base: Int) -> String {
            if num == 0 { return "0" }
            let digits = Array("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            var x = num
            var chars: [Character] = []
            while x > 0 {
                let rem = x % base
                chars.append(digits[rem])
                x /= base
            }
            return String(chars.reversed())
        }
        let hexPart = toBase(n * n, 16)
        let base36Part = toBase(n * n * n, 36)
        return hexPart + base36Part
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun concatHex36(n: Int): String {
        val sq = n.toLong() * n
        val cube = sq * n
        val hex = java.lang.Long.toString(sq, 16).uppercase()
        val base36 = java.lang.Long.toString(cube, 36).uppercase()
        return hex + base36
    }
}
```

## Dart

```dart
class Solution {
  String concatHex36(int n) {
    int sq = n * n;
    int cube = sq * n;
    String hex = sq.toRadixString(16).toUpperCase();
    String base36 = cube.toRadixString(36).toUpperCase();
    return hex + base36;
  }
}
```

## Golang

```go
func concatHex36(n int) string {
	toBase := func(x int64, base int) string {
		if x == 0 {
			return "0"
		}
		const digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		b := int64(base)
		var buf []byte
		for x > 0 {
			r := x % b
			buf = append(buf, digits[r])
			x /= b
		}
		// reverse
		for i, j := 0, len(buf)-1; i < j; i, j = i+1, j-1 {
			buf[i], buf[j] = buf[j], buf[i]
		}
		return string(buf)
	}
	n64 := int64(n)
	hexStr := toBase(n64*n64, 16)
	base36Str := toBase(n64*n64*n64, 36)
	return hexStr + base36Str
}
```

## Ruby

```ruby
def concat_hex36(n)
  (n * n).to_s(16).upcase + (n ** 3).to_s(36).upcase
end
```

## Scala

```scala
object Solution {
    def concatHex36(n: Int): String = {
        def toBase(value: Long, base: Int): String = {
            if (value == 0) return "0"
            val sb = new StringBuilder
            var v = value
            while (v > 0) {
                val d = (v % base).toInt
                val ch = if (d < 10) ('0' + d).toChar else ('A' + (d - 10)).toChar
                sb.append(ch)
                v /= base
            }
            sb.reverse.toString()
        }

        val hexPart = toBase(n.toLong * n, 16)
        val base36Part = toBase(n.toLong * n * n, 36)
        hexPart + base36Part
    }
}
```

## Rust

```rust
impl Solution {
    pub fn concat_hex36(n: i32) -> String {
        fn to_base(mut x: u64, base: u32) -> String {
            if x == 0 {
                return "0".to_string();
            }
            let mut digits = Vec::new();
            while x > 0 {
                let d = (x % base as u64) as u8;
                let ch = if d < 10 {
                    (b'0' + d) as char
                } else {
                    (b'A' + (d - 10)) as char
                };
                digits.push(ch);
                x /= base as u64;
            }
            digits.iter().rev().collect()
        }

        let n_u = n as u64;
        let n2 = n_u * n_u;
        let n3 = n2 * n_u;

        let hex = to_base(n2, 16);
        let base36 = to_base(n3, 36);
        format!("{}{}", hex, base36)
    }
}
```

## Racket

```racket
(define (digit-char d)
  (string-ref "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" d))

(define (to-base x b)
  (if (= x 0)
      "0"
      (let loop ((num x) (acc '()))
        (if (= num 0)
            (list->string acc)
            (loop (quotient num b)
                  (cons (digit-char (remainder num b)) acc))))))

(define/contract (concat-hex36 n)
  (-> exact-integer? string?)
  (let* ((sq (* n n))
         (cube (* n n n))
         (hex (to-base sq 16))
         (base36 (to-base cube 36)))
    (string-append hex base36)))
```

## Erlang

```erlang
-spec concat_hex36(N :: integer()) -> unicode:unicode_binary().
concat_hex36(N) ->
    Hex = to_base(N * N, 16),
    Base36 = to_base(N * N * N, 36),
    unicode:characters_to_binary(Hex ++ Base36).

to_base(0, _B) -> "0";
to_base(N, B) when N > 0 ->
    Digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    build(N, B, Digits, []).

build(0, _B, _Digits, Acc) ->
    lists:reverse(Acc);
build(N, B, Digits, Acc) ->
    Rem = N rem B,
    Char = lists:nth(Rem + 1, Digits),
    build(N div B, B, Digits, [Char | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec concat_hex36(n :: integer) :: String.t
  def concat_hex36(n) do
    hex = Integer.to_string(n * n, 16) |> String.upcase()
    base36 = Integer.to_string(n * n * n, 36) |> String.upcase()
    hex <> base36
  end
end
```
