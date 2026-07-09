# 0091. Decode Ways

## Cpp

```cpp
class Solution {
public:
    int numDecodings(string s) {
        if (s.empty() || s[0] == '0') return 0;
        int n = s.size();
        int prev2 = 1; // dp[i-2]
        int prev1 = 1; // dp[i-1] for first character
        for (int i = 1; i < n; ++i) {
            int cur = 0;
            if (s[i] != '0') cur += prev1;
            int two = (s[i - 1] - '0') * 10 + (s[i] - '0');
            if (two >= 10 && two <= 26) cur += prev2;
            prev2 = prev1;
            prev1 = cur;
        }
        return prev1;
    }
};
```

## Java

```java
class Solution {
    public int numDecodings(String s) {
        if (s == null || s.length() == 0 || s.charAt(0) == '0') return 0;
        int n = s.length();
        int prev2 = 1; // dp[i-2]
        int prev1 = 1; // dp[i-1] for first character
        for (int i = 1; i < n; i++) {
            int cur = 0;
            char c = s.charAt(i);
            if (c != '0') {
                cur += prev1;
            }
            int twoDigit = (s.charAt(i - 1) - '0') * 10 + (c - '0');
            if (twoDigit >= 10 && twoDigit <= 26) {
                cur += prev2;
            }
            if (cur == 0) return 0; // early exit for invalid string
            prev2 = prev1;
            prev1 = cur;
        }
        return prev1;
    }
}
```

## Python

```python
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        n = len(s)
        prev = 1  # dp[i-2]
        curr = 0 if s[0] == '0' else 1  # dp[i-1]
        for i in range(1, n):
            temp = 0
            if s[i] != '0':
                temp += curr
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                temp += prev
            prev, curr = curr, temp
        return curr
```

## Python3

```python
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        n = len(s)
        dp_prev2 = 1  # ways for empty prefix
        dp_prev1 = 1  # ways for first character (non-zero guaranteed)

        for i in range(2, n + 1):
            cur = 0
            if s[i - 1] != '0':
                cur += dp_prev1
            two_digit = int(s[i - 2:i])
            if 10 <= two_digit <= 26:
                cur += dp_prev2
            dp_prev2, dp_prev1 = dp_prev1, cur

        return dp_prev1 if n > 1 else dp_prev1
```

## C

```c
#include <string.h>

int numDecodings(char* s) {
    int n = strlen(s);
    if (n == 0) return 0;
    
    int dp_prev2 = 1; // ways for empty prefix
    int dp_prev1 = (s[0] != '0') ? 1 : 0; // ways for first character
    
    for (int i = 1; i < n; ++i) {
        int cur = 0;
        
        if (s[i] != '0')
            cur += dp_prev1;
        
        int two_digit = (s[i - 1] - '0') * 10 + (s[i] - '0');
        if (two_digit >= 10 && two_digit <= 26)
            cur += dp_prev2;
        
        dp_prev2 = dp_prev1;
        dp_prev1 = cur;
    }
    
    return dp_prev1;
}
```

## Csharp

```csharp
public class Solution {
    public int NumDecodings(string s) {
        if (string.IsNullOrEmpty(s) || s[0] == '0') return 0;
        int n = s.Length;
        int prev2 = 1; // dp[i-2]
        int prev1 = 1; // dp[i-1] for first character

        for (int i = 1; i < n; i++) {
            int cur = 0;

            if (s[i] != '0') {
                cur += prev1;
            }

            int twoDigit = (s[i - 1] - '0') * 10 + (s[i] - '0');
            if (twoDigit >= 10 && twoDigit <= 26) {
                cur += prev2;
            }

            prev2 = prev1;
            prev1 = cur;
        }

        return prev1;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var numDecodings = function(s) {
    const n = s.length;
    if (n === 0 || s[0] === '0') return 0;
    
    let prev = 1; // dp[i-2]
    let curr = 1; // dp[i-1]
    
    for (let i = 1; i < n; i++) {
        let temp = 0;
        
        // Single digit decode is possible if current char != '0'
        if (s[i] !== '0') {
            temp += curr;
        }
        
        // Two-digit decode check
        const twoDigit = (s.charCodeAt(i - 1) - 48) * 10 + (s.charCodeAt(i) - 48);
        if (twoDigit >= 10 && twoDigit <= 26) {
            temp += prev;
        }
        
        // If no decoding possible at this position, return 0 early
        if (temp === 0) return 0;
        
        prev = curr;
        curr = temp;
    }
    
    return curr;
};
```

## Typescript

```typescript
function numDecodings(s: string): number {
    const n = s.length;
    const dp = new Array(n + 1).fill(0);
    dp[0] = 1;

    for (let i = 1; i <= n; i++) {
        // Single digit decode (non-zero)
        if (s[i - 1] !== '0') {
            dp[i] += dp[i - 1];
        }

        // Two-digit decode within [10,26]
        if (i >= 2) {
            const two = parseInt(s.substring(i - 2, i), 10);
            if (two >= 10 && two <= 26) {
                dp[i] += dp[i - 2];
            }
        }
    }

    return dp[n];
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function numDecodings($s) {
        $n = strlen($s);
        if ($n == 0 || $s[0] === '0') {
            return 0;
        }

        $prev = 1; // dp[i-2]
        $curr = 1; // dp[i-1]

        for ($i = 1; $i < $n; $i++) {
            $temp = 0;

            if ($s[$i] !== '0') {
                $temp += $curr;
            }

            $two = intval($s[$i - 1] . $s[$i]);
            if ($two >= 10 && $two <= 26) {
                $temp += $prev;
            }

            $prev = $curr;
            $curr = $temp;
        }

        return $curr;
    }
}
```

## Swift

```swift
class Solution {
    func numDecodings(_ s: String) -> Int {
        let n = s.count
        if n == 0 { return 0 }
        let chars = Array(s)
        var dpMinusTwo = 1
        var dpMinusOne = chars[0] != "0" ? 1 : 0
        if n == 1 { return dpMinusOne }
        for i in 1..<n {
            var cur = 0
            if chars[i] != "0" {
                cur += dpMinusOne
            }
            let twoDigit = (Int(String(chars[i - 1]))! ) * 10 + Int(String(chars[i]))!
            if twoDigit >= 10 && twoDigit <= 26 {
                cur += dpMinusTwo
            }
            dpMinusTwo = dpMinusOne
            dpMinusOne = cur
        }
        return dpMinusOne
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numDecodings(s: String): Int {
        if (s.isEmpty() || s[0] == '0') return 0
        var prev = 1
        var curr = 1
        for (i in 1 until s.length) {
            var ways = 0
            if (s[i] != '0') ways += curr
            val twoDigit = (s[i - 1] - '0') * 10 + (s[i] - '0')
            if (twoDigit in 10..26) ways += prev
            prev = curr
            curr = ways
        }
        return curr
    }
}
```

## Dart

```dart
class Solution {
  int numDecodings(String s) {
    if (s.isEmpty || s[0] == '0') return 0;
    int a = 1; // dp[i-2]
    int b = 1; // dp[i-1]
    for (int i = 1; i < s.length; ++i) {
      int cur = 0;
      if (s[i] != '0') {
        cur += b;
      }
      int twoDigit = int.parse(s.substring(i - 1, i + 1));
      if (twoDigit >= 10 && twoDigit <= 26) {
        cur += a;
      }
      a = b;
      b = cur;
    }
    return b;
  }
}
```

## Golang

```go
func numDecodings(s string) int {
    n := len(s)
    if n == 0 || s[0] == '0' {
        return 0
    }
    prev2, prev1 := 1, 1 // dp[-1]=1, dp[0]=1
    for i := 1; i < n; i++ {
        cur := 0
        if s[i] != '0' {
            cur += prev1
        }
        two := (s[i-1]-'0')*10 + (s[i] - '0')
        if two >= 10 && two <= 26 {
            cur += prev2
        }
        if cur == 0 {
            return 0
        }
        prev2, prev1 = prev1, cur
    }
    return prev1
}
```

## Ruby

```ruby
def num_decodings(s)
  return 0 if s.empty? || s[0] == '0'
  n = s.length
  prev = 1
  curr = 1
  (1...n).each do |i|
    temp = 0
    temp += curr if s[i] != '0'
    two = (s[i - 1].ord - 48) * 10 + (s[i].ord - 48)
    temp += prev if two >= 10 && two <= 26
    return 0 if temp == 0
    prev, curr = curr, temp
  end
  curr
end
```

## Scala

```scala
object Solution {
    def numDecodings(s: String): Int = {
        val n = s.length
        if (n == 0) return 0
        var prev = 1 // dp[i-2]
        var curr = if (s.charAt(0) != '0') 1 else 0 // dp[i-1]
        for (i <- 1 until n) {
            var temp = 0
            val c = s.charAt(i)
            if (c != '0') {
                temp += curr
            }
            val two = (s.charAt(i - 1) - '0') * 10 + (c - '0')
            if (two >= 10 && two <= 26) {
                temp += prev
            }
            prev = curr
            curr = temp
        }
        curr
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_decodings(s: String) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        if n == 0 {
            return 0;
        }
        let mut dp = vec![0i64; n + 1];
        dp[0] = 1;
        for i in 1..=n {
            // Single digit decode (non-zero)
            if bytes[i - 1] != b'0' {
                dp[i] += dp[i - 1];
            }
            // Two-digit decode within [10,26]
            if i >= 2 {
                let two = (bytes[i - 2] - b'0') * 10 + (bytes[i - 1] - b'0');
                if two >= 10 && two <= 26 {
                    dp[i] += dp[i - 2];
                }
            }
        }
        dp[n] as i32
    }
}
```

## Racket

```racket
(define/contract (num-decodings s)
  (-> string? exact-integer?)
  (let* ((n (string-length s)))
    (if (= n 0)
        0
        (let ((first-char (string-ref s 0)))
          (if (char=? first-char #\0)
              0
              (let loop ((i 1) (prev 1) (cur 1))
                (if (= i n)
                    cur
                    (let* ((c (string-ref s i))
                           (p (string-ref s (- i 1)))
                           (digit (- (char->integer c) (char->integer #\0)))
                           (two-digit (+ (* (- (char->integer p) (char->integer #\0)) 10) digit))
                           (ways (+ (if (= digit 0) 0 cur)
                                    (if (and (>= two-digit 10) (<= two-digit 26)) prev 0))))
                      (loop (+ i 1) cur ways))))))))))
```

## Erlang

```erlang
-module(solution).
-export([num_decodings/1]).

-spec num_decodings(S :: unicode:unicode_binary()) -> integer().
num_decodings(S) ->
    L = binary_to_list(S),
    case L of
        [] -> 0;
        [First|Rest] ->
            if First == $0 -> 0; true ->
                decode(Rest, First, 1, 1)
            end
    end.

decode([], _PrevChar, _Prev2, Prev1) ->
    Prev1;
decode([Curr|Tail], PrevChar, Prev2, Prev1) ->
    Single = if Curr =/= $0 -> Prev1; true -> 0 end,
    Double = case {PrevChar, Curr} of
                {$1,_} -> Prev2;
                {$2, C} when C >= $0, C =< $6 -> Prev2;
                _ -> 0
            end,
    CurWays = Single + Double,
    if CurWays == 0 ->
            0;
       true ->
            decode(Tail, Curr, Prev1, CurWays)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec num_decodings(s :: String.t) :: integer
  def num_decodings(s) do
    chars = String.graphemes(s)

    case chars do
      [] -> 0
      ["0" | _] -> 0
      [first | rest] ->
        {_, result, _} =
          Enum.reduce(rest, {first, 1, 1}, fn c, {prev_char, dp_prev, dp_before} ->
            single = if c != "0", do: dp_prev, else: 0

            two_val = String.to_integer(prev_char <> c)

            double = if two_val >= 10 and two_val <= 26, do: dp_before, else: 0

            ways = single + double

            {c, ways, dp_prev}
          end)

        result
    end
  end
end
```
