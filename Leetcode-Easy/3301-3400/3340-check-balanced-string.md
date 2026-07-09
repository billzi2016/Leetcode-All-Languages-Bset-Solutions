# 3340. Check Balanced String

## Cpp

```cpp
class Solution {
public:
    bool isBalanced(string num) {
        int sumEven = 0, sumOdd = 0;
        for (int i = 0; i < (int)num.size(); ++i) {
            int digit = num[i] - '0';
            if (i % 2 == 0)
                sumEven += digit;
            else
                sumOdd += digit;
        }
        return sumEven == sumOdd;
    }
};
```

## Java

```java
class Solution {
    public boolean isBalanced(String num) {
        int evenSum = 0;
        int oddSum = 0;
        for (int i = 0; i < num.length(); i++) {
            int digit = num.charAt(i) - '0';
            if ((i & 1) == 0) {
                evenSum += digit;
            } else {
                oddSum += digit;
            }
        }
        return evenSum == oddSum;
    }
}
```

## Python

```python
class Solution(object):
    def isBalanced(self, num):
        """
        :type num: str
        :rtype: bool
        """
        even_sum = 0
        odd_sum = 0
        for i, ch in enumerate(num):
            if i % 2 == 0:
                even_sum += ord(ch) - 48
            else:
                odd_sum += ord(ch) - 48
        return even_sum == odd_sum
```

## Python3

```python
class Solution:
    def isBalanced(self, num: str) -> bool:
        even_sum = 0
        odd_sum = 0
        for i, ch in enumerate(num):
            digit = ord(ch) - 48
            if i % 2 == 0:
                even_sum += digit
            else:
                odd_sum += digit
        return even_sum == odd_sum
```

## C

```c
#include <stdbool.h>

bool isBalanced(char* num) {
    int sumEven = 0, sumOdd = 0;
    for (int i = 0; num[i] != '\0'; ++i) {
        int digit = num[i] - '0';
        if ((i & 1) == 0)
            sumEven += digit;
        else
            sumOdd += digit;
    }
    return sumEven == sumOdd;
}
```

## Csharp

```csharp
public class Solution {
    public bool IsBalanced(string num) {
        int evenSum = 0, oddSum = 0;
        for (int i = 0; i < num.Length; i++) {
            int digit = num[i] - '0';
            if ((i & 1) == 0)
                evenSum += digit;
            else
                oddSum += digit;
        }
        return evenSum == oddSum;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} num
 * @return {boolean}
 */
var isBalanced = function(num) {
    let evenSum = 0, oddSum = 0;
    for (let i = 0; i < num.length; ++i) {
        const digit = num.charCodeAt(i) - 48; // '0' => 48
        if ((i & 1) === 0) {
            evenSum += digit;
        } else {
            oddSum += digit;
        }
    }
    return evenSum === oddSum;
};
```

## Typescript

```typescript
function isBalanced(num: string): boolean {
    let evenSum = 0;
    let oddSum = 0;
    for (let i = 0; i < num.length; i++) {
        const digit = num.charCodeAt(i) - 48; // faster than parseInt
        if ((i & 1) === 0) {
            evenSum += digit;
        } else {
            oddSum += digit;
        }
    }
    return evenSum === oddSum;
}
```

## Php

```php
class Solution {

    /**
     * @param String $num
     * @return Boolean
     */
    function isBalanced($num) {
        $len = strlen($num);
        $evenSum = 0;
        $oddSum = 0;
        for ($i = 0; $i < $len; $i++) {
            $digit = intval($num[$i]);
            if (($i & 1) === 0) {
                $evenSum += $digit;
            } else {
                $oddSum += $digit;
            }
        }
        return $evenSum === $oddSum;
    }
}
```

## Swift

```swift
class Solution {
    func isBalanced(_ num: String) -> Bool {
        var evenSum = 0
        var oddSum = 0
        for (i, ch) in num.enumerated() {
            let digit = Int(String(ch))!
            if i % 2 == 0 {
                evenSum += digit
            } else {
                oddSum += digit
            }
        }
        return evenSum == oddSum
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isBalanced(num: String): Boolean {
        var evenSum = 0
        var oddSum = 0
        for (i in num.indices) {
            val digit = num[i] - '0'
            if (i % 2 == 0) {
                evenSum += digit
            } else {
                oddSum += digit
            }
        }
        return evenSum == oddSum
    }
}
```

## Dart

```dart
class Solution {
  bool isBalanced(String num) {
    int evenSum = 0;
    int oddSum = 0;
    for (int i = 0; i < num.length; i++) {
      int digit = num.codeUnitAt(i) - 48; // '0' ascii code is 48
      if (i % 2 == 0) {
        evenSum += digit;
      } else {
        oddSum += digit;
      }
    }
    return evenSum == oddSum;
  }
}
```

## Golang

```go
func isBalanced(num string) bool {
    sumEven, sumOdd := 0, 0
    for i, ch := range num {
        digit := int(ch - '0')
        if i%2 == 0 {
            sumEven += digit
        } else {
            sumOdd += digit
        }
    }
    return sumEven == sumOdd
}
```

## Ruby

```ruby
def is_balanced(num)
  even_sum = 0
  odd_sum = 0
  num.each_char.with_index do |ch, i|
    digit = ch.ord - 48
    if i.even?
      even_sum += digit
    else
      odd_sum += digit
    end
  end
  even_sum == odd_sum
end
```

## Scala

```scala
object Solution {
    def isBalanced(num: String): Boolean = {
        var evenSum = 0
        var oddSum = 0
        var i = 0
        while (i < num.length) {
            val digit = num.charAt(i) - '0'
            if ((i & 1) == 0) evenSum += digit else oddSum += digit
            i += 1
        }
        evenSum == oddSum
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_balanced(num: String) -> bool {
        let mut even_sum = 0i32;
        let mut odd_sum = 0i32;
        for (i, b) in num.bytes().enumerate() {
            let digit = (b - b'0') as i32;
            if i % 2 == 0 {
                even_sum += digit;
            } else {
                odd_sum += digit;
            }
        }
        even_sum == odd_sum
    }
}
```

## Racket

```racket
(define/contract (is-balanced num)
  (-> string? boolean?)
  (let* ((len (string-length num))
         (even-sum
          (for/sum ([i (in-range 0 len 2)])
            (- (char->integer (string-ref num i)) (char->integer #\0))))
         (odd-sum
          (for/sum ([i (in-range 1 len 2)])
            (- (char->integer (string-ref num i)) (char->integer #\0)))))
    (= even-sum odd-sum)))
```

## Erlang

```erlang
-spec is_balanced(Num :: unicode:unicode_binary()) -> boolean().
is_balanced(Num) ->
    Digits = binary_to_list(Num),
    {EvenSum, OddSum} = sums(Digits, 0, 0, 0),
    EvenSum == OddSum.

sums([], _, ES, OS) -> {ES, OS};
sums([C|Rest], Index, ES, OS) ->
    Digit = C - $0,
    case Index rem 2 of
        0 -> sums(Rest, Index + 1, ES + Digit, OS);
        1 -> sums(Rest, Index + 1, ES, OS + Digit)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_balanced(num :: String.t) :: boolean
  def is_balanced(num) do
    {even_sum, odd_sum} =
      num
      |> String.graphemes()
      |> Enum.with_index()
      |> Enum.reduce({0, 0}, fn {ch, idx}, {e, o} ->
        digit = String.to_integer(ch)

        if rem(idx, 2) == 0 do
          {e + digit, o}
        else
          {e, o + digit}
        end
      end)

    even_sum == odd_sum
  end
end
```
