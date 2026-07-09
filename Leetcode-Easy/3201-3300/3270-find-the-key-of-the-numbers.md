# 3270. Find the Key of the Numbers

## Cpp

```cpp
class Solution {
public:
    int generateKey(int num1, int num2, int num3) {
        int result = 0;
        int place = 1;
        for (int i = 0; i < 4; ++i) {
            int d1 = num1 % 10;
            int d2 = num2 % 10;
            int d3 = num3 % 10;
            int mn = std::min(d1, std::min(d2, d3));
            result += mn * place;
            place *= 10;
            num1 /= 10;
            num2 /= 10;
            num3 /= 10;
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public int generateKey(int num1, int num2, int num3) {
        int result = 0;
        int place = 1; // units, tens, hundreds, thousands
        for (int i = 0; i < 4; i++) {
            int d1 = (num1 / place) % 10;
            int d2 = (num2 / place) % 10;
            int d3 = (num3 / place) % 10;
            int minDigit = Math.min(d1, Math.min(d2, d3));
            result += minDigit * place;
            place *= 10;
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def generateKey(self, num1, num2, num3):
        """
        :type num1: int
        :type num2: int
        :type num3: int
        :rtype: int
        """
        s1 = f"{num1:04d}"
        s2 = f"{num2:04d}"
        s3 = f"{num3:04d}"
        key_digits = [str(min(int(s1[i]), int(s2[i]), int(s3[i]))) for i in range(4)]
        return int(''.join(key_digits))
```

## Python3

```python
class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        s1 = f"{num1:04d}"
        s2 = f"{num2:04d}"
        s3 = f"{num3:04d}"
        key_digits = [str(min(int(s1[i]), int(s2[i]), int(s3[i]))) for i in range(4)]
        return int(''.join(key_digits))
```

## C

```c
int generateKey(int num1, int num2, int num3) {
    int result = 0;
    int factor = 1;
    for (int i = 0; i < 4; ++i) {
        int d1 = (num1 / factor) % 10;
        int d2 = (num2 / factor) % 10;
        int d3 = (num3 / factor) % 10;
        int mn = d1;
        if (d2 < mn) mn = d2;
        if (d3 < mn) mn = d3;
        result += mn * factor;
        factor *= 10;
    }
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int GenerateKey(int num1, int num2, int num3) {
        int[] pow = { 1, 10, 100, 1000 };
        int result = 0;
        for (int i = 0; i < 4; i++) {
            int d1 = (num1 / pow[i]) % 10;
            int d2 = (num2 / pow[i]) % 10;
            int d3 = (num3 / pow[i]) % 10;
            int min = Math.Min(d1, Math.Min(d2, d3));
            result += min * pow[i];
        }
        return result;
    }
}
```

## Javascript

```javascript
var generateKey = function(num1, num2, num3) {
    let result = 0;
    for (let p = 3; p >= 0; --p) {
        const base = Math.pow(10, p);
        const d1 = Math.floor(num1 / base) % 10;
        const d2 = Math.floor(num2 / base) % 10;
        const d3 = Math.floor(num3 / base) % 10;
        const minDigit = Math.min(d1, d2, d3);
        result = result * 10 + minDigit;
    }
    return result;
};
```

## Typescript

```typescript
function generateKey(num1: number, num2: number, num3: number): number {
    const s1 = num1.toString().padStart(4, '0');
    const s2 = num2.toString().padStart(4, '0');
    const s3 = num3.toString().padStart(4, '0');
    let result = '';
    for (let i = 0; i < 4; i++) {
        const d1 = s1.charCodeAt(i) - 48;
        const d2 = s2.charCodeAt(i) - 48;
        const d3 = s3.charCodeAt(i) - 48;
        const minDigit = Math.min(d1, d2, d3);
        result += String.fromCharCode(48 + minDigit);
    }
    return Number(result);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $num1
     * @param Integer $num2
     * @param Integer $num3
     * @return Integer
     */
    function generateKey($num1, $num2, $num3) {
        $s1 = str_pad((string)$num1, 4, '0', STR_PAD_LEFT);
        $s2 = str_pad((string)$num2, 4, '0', STR_PAD_LEFT);
        $s3 = str_pad((string)$num3, 4, '0', STR_PAD_LEFT);
        $key = '';
        for ($i = 0; $i < 4; $i++) {
            $minDigit = min(intval($s1[$i]), intval($s2[$i]), intval($s3[$i]));
            $key .= (string)$minDigit;
        }
        return intval($key);
    }
}
```

## Swift

```swift
class Solution {
    func generateKey(_ num1: Int, _ num2: Int, _ num3: Int) -> Int {
        var a = num1
        var b = num2
        var c = num3
        var result = 0
        var factor = 1
        
        for _ in 0..<4 {
            let d1 = a % 10
            let d2 = b % 10
            let d3 = c % 10
            let minDigit = min(d1, min(d2, d3))
            result += minDigit * factor
            
            factor *= 10
            a /= 10
            b /= 10
            c /= 10
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun generateKey(num1: Int, num2: Int, num3: Int): Int {
        var result = 0
        var factor = 1
        repeat(4) {
            val d1 = (num1 / factor) % 10
            val d2 = (num2 / factor) % 10
            val d3 = (num3 / factor) % 10
            val minDigit = kotlin.math.min(d1, kotlin.math.min(d2, d3))
            result += minDigit * factor
            factor *= 10
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  int generateKey(int num1, int num2, int num3) {
    int result = 0;
    int multiplier = 1;
    int divisor = 1;
    for (int i = 0; i < 4; ++i) {
      int d1 = (num1 ~/ divisor) % 10;
      int d2 = (num2 ~/ divisor) % 10;
      int d3 = (num3 ~/ divisor) % 10;
      int minDigit = d1;
      if (d2 < minDigit) minDigit = d2;
      if (d3 < minDigit) minDigit = d3;
      result += minDigit * multiplier;
      multiplier *= 10;
      divisor *= 10;
    }
    return result;
  }
}
```

## Golang

```go
func generateKey(num1 int, num2 int, num3 int) int {
    result := 0
    for d := 1000; d >= 1; d /= 10 {
        a := (num1 / d) % 10
        b := (num2 / d) % 10
        c := (num3 / d) % 10
        min := a
        if b < min {
            min = b
        }
        if c < min {
            min = c
        }
        result = result*10 + min
    }
    return result
}
```

## Ruby

```ruby
def generate_key(num1, num2, num3)
  s1 = format("%04d", num1)
  s2 = format("%04d", num2)
  s3 = format("%04d", num3)
  key = ''
  4.times do |i|
    key << [s1[i], s2[i], s3[i]].min
  end
  key.to_i
end
```

## Scala

```scala
object Solution {
    def generateKey(num1: Int, num2: Int, num3: Int): Int = {
        var result = 0
        var divisor = 1
        for (_ <- 0 until 4) {
            val d1 = (num1 / divisor) % 10
            val d2 = (num2 / divisor) % 10
            val d3 = (num3 / divisor) % 10
            val minDigit = math.min(d1, math.min(d2, d3))
            result += minDigit * divisor
            divisor *= 10
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn generate_key(num1: i32, num2: i32, num3: i32) -> i32 {
        let mut a = num1;
        let mut b = num2;
        let mut c = num3;
        let mut result = 0;
        let mut place = 1;
        for _ in 0..4 {
            let d1 = a % 10;
            let d2 = b % 10;
            let d3 = c % 10;
            let min_digit = std::cmp::min(d1, std::cmp::min(d2, d3));
            result += min_digit * place;
            place *= 10;
            a /= 10;
            b /= 10;
            c /= 10;
        }
        result
    }
}
```

## Racket

```racket
(define/contract (generate-key num1 num2 num3)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  (let loop ((i 3) (res 0))
    (if (< i 0)
        res
        (let* ([d1 (modulo (quotient num1 (expt 10 i)) 10)]
               [d2 (modulo (quotient num2 (expt 10 i)) 10)]
               [d3 (modulo (quotient num3 (expt 10 i)) 10)]
               [m (min d1 d2 d3)])
          (loop (- i 1) (+ (* res 10) m))))))
```

## Erlang

```erlang
-spec generate_key(Num1 :: integer(), Num2 :: integer(), Num3 :: integer()) -> integer().
generate_key(Num1, Num2, Num3) ->
    generate_key(Num1, Num2, Num3, 0, 1).

generate_key(_, _, _, Acc, Mult) when Mult > 1000 ->
    Acc;
generate_key(N1, N2, N3, Acc, Mult) ->
    D1 = (N1 div Mult) rem 10,
    D2 = (N2 div Mult) rem 10,
    D3 = (N3 div Mult) rem 10,
    MinD = min(D1, min(D2, D3)),
    generate_key(N1, N2, N3, Acc + MinD * Mult, Mult * 10).
```

## Elixir

```elixir
defmodule Solution do
  @spec generate_key(num1 :: integer, num2 :: integer, num3 :: integer) :: integer
  def generate_key(num1, num2, num3) do
    [1000, 100, 10, 1]
    |> Enum.reduce(0, fn p, acc ->
      d1 = div(num1, p) |> rem(10)
      d2 = div(num2, p) |> rem(10)
      d3 = div(num3, p) |> rem(10)

      min_digit = Enum.min([d1, d2, d3])
      acc * 10 + min_digit
    end)
  end
end
```
