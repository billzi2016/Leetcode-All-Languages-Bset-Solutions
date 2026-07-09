# 1945. Sum of Digits of String After Convert

## Cpp

```cpp
class Solution {
public:
    int getLucky(string s, int k) {
        int sum = 0;
        for (char c : s) {
            int val = c - 'a' + 1;
            while (val > 0) {
                sum += val % 10;
                val /= 10;
            }
        }
        for (int i = 1; i < k; ++i) {
            int newSum = 0;
            while (sum > 0) {
                newSum += sum % 10;
                sum /= 10;
            }
            sum = newSum;
        }
        return sum;
    }
};
```

## Java

```java
class Solution {
    public int getLucky(String s, int k) {
        int sum = 0;
        for (int i = 0; i < s.length(); i++) {
            int val = s.charAt(i) - 'a' + 1;
            while (val > 0) {
                sum += val % 10;
                val /= 10;
            }
        }
        for (int i = 1; i < k; i++) {
            int next = 0;
            while (sum > 0) {
                next += sum % 10;
                sum /= 10;
            }
            sum = next;
        }
        return sum;
    }
}
```

## Python

```python
class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Convert string to concatenated numeric representation
        num_str = ''.join(str(ord(ch) - ord('a') + 1) for ch in s)
        # First digit sum
        cur = sum(int(d) for d in num_str)
        # Remaining k-1 transformations
        for _ in range(k - 1):
            nxt = 0
            while cur:
                nxt += cur % 10
                cur //= 10
            cur = nxt
        return cur
```

## Python3

```python
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        total = 0
        for ch in s:
            val = ord(ch) - ord('a') + 1
            if val >= 10:
                total += val // 10 + val % 10
            else:
                total += val
        for _ in range(k - 1):
            cur = 0
            while total > 0:
                cur += total % 10
                total //= 10
            total = cur
        return total
```

## C

```c
int getLucky(char* s, int k) {
    long long sum = 0;
    for (char *p = s; *p; ++p) {
        int val = (*p - 'a' + 1);
        if (val >= 10)
            sum += val / 10 + val % 10;
        else
            sum += val;
    }
    for (int i = 1; i < k; ++i) {
        long long next = 0;
        while (sum > 0) {
            next += sum % 10;
            sum /= 10;
        }
        sum = next;
    }
    return (int)sum;
}
```

## Csharp

```csharp
public class Solution {
    public int GetLucky(string s, int k) {
        int sum = 0;
        foreach (char ch in s) {
            int val = ch - 'a' + 1;
            if (val >= 10) {
                sum += val / 10 + val % 10;
            } else {
                sum += val;
            }
        }
        for (int i = 1; i < k; i++) {
            int temp = 0;
            while (sum > 0) {
                temp += sum % 10;
                sum /= 10;
            }
            sum = temp;
        }
        return sum;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var getLucky = function(s, k) {
    let sum = 0;
    for (let i = 0; i < s.length; ++i) {
        const val = s.charCodeAt(i) - 96; // 'a' -> 1 ... 'z' -> 26
        if (val >= 10) {
            sum += Math.floor(val / 10) + (val % 10);
        } else {
            sum += val;
        }
    }
    for (let iter = 1; iter < k; ++iter) {
        let cur = 0;
        while (sum > 0) {
            cur += sum % 10;
            sum = Math.floor(sum / 10);
        }
        sum = cur;
    }
    return sum;
};
```

## Typescript

```typescript
function getLucky(s: string, k: number): number {
    let sum = 0;
    for (let i = 0; i < s.length; i++) {
        const val = s.charCodeAt(i) - 96; // 'a' -> 1, ..., 'z' -> 26
        if (val >= 10) {
            sum += Math.floor(val / 10) + (val % 10);
        } else {
            sum += val;
        }
    }
    for (let i = 1; i < k; i++) {
        let cur = 0;
        while (sum > 0) {
            cur += sum % 10;
            sum = Math.floor(sum / 10);
        }
        sum = cur;
    }
    return sum;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function getLucky($s, $k) {
        // Convert each character to its alphabet position and concatenate
        $numStr = '';
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $pos = ord($s[$i]) - ord('a') + 1;
            $numStr .= (string)$pos;
        }

        // Perform the digit-sum transformation k times
        while ($k-- > 0) {
            $sum = 0;
            $nLen = strlen($numStr);
            for ($j = 0; $j < $nLen; $j++) {
                $sum += intval($numStr[$j]);
            }
            $numStr = (string)$sum;
        }

        return intval($numStr);
    }
}
```

## Swift

```swift
class Solution {
    func getLucky(_ s: String, _ k: Int) -> Int {
        var initialSum = 0
        let aValue = Unicode.Scalar("a").value
        for scalar in s.unicodeScalars {
            let val = Int(scalar.value - aValue + 1)
            if val >= 10 {
                initialSum += val / 10 + val % 10
            } else {
                initialSum += val
            }
        }
        var result = initialSum
        if k > 1 {
            for _ in 1..<k {
                var next = 0
                var x = result
                while x > 0 {
                    next += x % 10
                    x /= 10
                }
                result = next
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getLucky(s: String, k: Int): Int {
        var sum = 0
        for (ch in s) {
            val pos = ch - 'a' + 1
            if (pos >= 10) {
                sum += pos / 10
                sum += pos % 10
            } else {
                sum += pos
            }
        }
        var result = sum
        repeat(k - 1) {
            var temp = 0
            var x = result
            while (x > 0) {
                temp += x % 10
                x /= 10
            }
            result = temp
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  int getLucky(String s, int k) {
    int total = 0;
    for (int i = 0; i < s.length; i++) {
      int val = s.codeUnitAt(i) - 'a'.codeUnitAt(0) + 1;
      while (val > 0) {
        total += val % 10;
        val ~/= 10;
      }
    }
    k--;
    while (k > 0) {
      int next = 0;
      int temp = total;
      if (temp == 0) {
        next = 0;
      } else {
        while (temp > 0) {
          next += temp % 10;
          temp ~/= 10;
        }
      }
      total = next;
      k--;
    }
    return total;
  }
}
```

## Golang

```go
func getLucky(s string, k int) int {
    total := 0
    for _, ch := range s {
        v := int(ch-'a') + 1
        if v >= 10 {
            total += v/10 + v%10
        } else {
            total += v
        }
    }
    for i := 1; i < k; i++ {
        sum := 0
        t := total
        for t > 0 {
            sum += t % 10
            t /= 10
        }
        total = sum
    }
    return total
}
```

## Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {Integer}
def get_lucky(s, k)
  total = 0
  s.each_byte do |b|
    v = b - 96
    if v >= 10
      total += v / 10 + v % 10
    else
      total += v
    end
  end

  (k - 1).times do
    sum = 0
    while total > 0
      sum += total % 10
      total /= 10
    end
    total = sum
  end

  total
end
```

## Scala

```scala
object Solution {
    def getLucky(s: String, k: Int): Int = {
        var total = 0
        for (ch <- s) {
            val pos = ch - 'a' + 1
            if (pos >= 10) total += pos / 10 + pos % 10 else total += pos
        }
        var cur = total
        for (_ <- 1 until k) {
            var sum = 0
            var n = cur
            while (n > 0) {
                sum += n % 10
                n /= 10
            }
            cur = sum
        }
        cur
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_lucky(s: String, k: i32) -> i32 {
        let mut cur: i32 = 0;
        for b in s.bytes() {
            let mut val = (b - b'a' + 1) as i32;
            while val > 0 {
                cur += val % 10;
                val /= 10;
            }
        }
        for _ in 0..(k - 1) {
            let mut sum = 0;
            let mut x = cur;
            while x > 0 {
                sum += x % 10;
                x /= 10;
            }
            cur = sum;
        }
        cur
    }
}
```

## Racket

```racket
(define/contract (get-lucky s k)
  (-> string? exact-integer? exact-integer?)
  (letrec ((digit-sum
            (lambda (n)
              (let loop ((n n) (sum 0))
                (if (= n 0) sum
                    (loop (quotient n 10) (+ sum (remainder n 10)))))))
           (char-pos
            (lambda (c)
              (+ (- (char->integer c) (char->integer #\a)) 1))))
    (let ((init-sum
           (for/sum ([ch (in-string s)])
             (digit-sum (char-pos ch)))))
      (let loop ((i (- k 1)) (cur init-sum))
        (if (= i 0) cur
            (loop (- i 1) (digit-sum cur)))))))
```

## Erlang

```erlang
-module(solution).
-export([get_lucky/2]).

-spec get_lucky(unicode:unicode_binary(), integer()) -> integer().
get_lucky(S, K) ->
    Initial = lists:foldl(fun(Char, Acc) ->
        Pos = Char - $a + 1,
        DigitSum = if Pos < 10 -> Pos; true -> (Pos div 10) + (Pos rem 10) end,
        Acc + DigitSum
    end, 0, unicode:characters_to_list(S)),
    repeat_sum(Initial, K - 1).

repeat_sum(N, 0) ->
    N;
repeat_sum(N, Times) ->
    repeat_sum(digit_sum(N), Times - 1).

digit_sum(N) -> digit_sum(N, 0).
digit_sum(0, Acc) -> Acc;
digit_sum(N, Acc) -> digit_sum(N div 10, Acc + (N rem 10)).
```

## Elixir

```elixir
defmodule Solution do
  @spec get_lucky(s :: String.t(), k :: integer) :: integer
  def get_lucky(s, k) do
    init_sum =
      s
      |> String.to_charlist()
      |> Enum.reduce(0, fn ch, acc ->
        val = ch - ?a + 1
        ds = if val < 10, do: val, else: div(val, 10) + rem(val, 10)
        acc + ds
      end)

    Enum.reduce(1..(k - 1), init_sum, fn _, cur -> digit_sum(cur) end)
  end

  defp digit_sum(n) do
    Integer.digits(n) |> Enum.sum()
  end
end
```
