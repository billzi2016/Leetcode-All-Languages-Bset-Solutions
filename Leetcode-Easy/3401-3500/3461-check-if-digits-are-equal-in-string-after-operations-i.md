# 3461. Check If Digits Are Equal in String After Operations I

## Cpp

```cpp
class Solution {
public:
    bool hasSameDigits(string s) {
        while (s.size() > 2) {
            string t;
            t.reserve(s.size() - 1);
            for (size_t i = 0; i + 1 < s.size(); ++i) {
                int sum = (s[i] - '0') + (s[i + 1] - '0');
                t.push_back('0' + (sum % 10));
            }
            s.swap(t);
        }
        return s[0] == s[1];
    }
};
```

## Java

```java
class Solution {
    public boolean hasSameDigits(String s) {
        int n = s.length();
        int[] digits = new int[n];
        for (int i = 0; i < n; i++) {
            digits[i] = s.charAt(i) - '0';
        }
        while (n > 2) {
            int[] next = new int[n - 1];
            for (int i = 0; i < n - 1; i++) {
                next[i] = (digits[i] + digits[i + 1]) % 10;
            }
            digits = next;
            n--;
        }
        return digits[0] == digits[1];
    }
}
```

## Python

```python
class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        digits = [int(ch) for ch in s]
        while len(digits) > 2:
            digits = [(digits[i] + digits[i+1]) % 10 for i in range(len(digits)-1)]
        return digits[0] == digits[1]
```

## Python3

```python
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits = [int(ch) for ch in s]
        while len(digits) > 2:
            digits = [(digits[i] + digits[i + 1]) % 10 for i in range(len(digits) - 1)]
        return digits[0] == digits[1]
```

## C

```c
#include <stdbool.h>
#include <string.h>

bool hasSameDigits(char* s) {
    int n = strlen(s);
    int cur[101];
    for (int i = 0; i < n; ++i) {
        cur[i] = s[i] - '0';
    }
    while (n > 2) {
        for (int i = 0; i < n - 1; ++i) {
            cur[i] = (cur[i] + cur[i + 1]) % 10;
        }
        --n;
    }
    return cur[0] == cur[1];
}
```

## Csharp

```csharp
public class Solution {
    public bool HasSameDigits(string s) {
        var sb = new System.Text.StringBuilder(s);
        while (sb.Length > 2) {
            int a = sb[0] - '0';
            int b = sb[1] - '0';
            int c = (a + b) % 10;
            sb.Remove(0, 2);
            sb.Insert(0, (char)(c + '0'));
        }
        return sb[0] == sb[1];
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {boolean}
 */
var hasSameDigits = function(s) {
    let digits = s.split('').map(ch => ch.charCodeAt(0) - 48);
    while (digits.length > 2) {
        const next = [];
        for (let i = 0; i < digits.length - 1; ++i) {
            next.push((digits[i] + digits[i + 1]) % 10);
        }
        digits = next;
    }
    return digits[0] === digits[1];
};
```

## Typescript

```typescript
function hasSameDigits(s: string): boolean {
    let digits = s.split('').map(ch => ch.charCodeAt(0) - 48);
    while (digits.length > 2) {
        const next: number[] = new Array(digits.length - 1);
        for (let i = 0; i < next.length; i++) {
            next[i] = (digits[i] + digits[i + 1]) % 10;
        }
        digits = next;
    }
    return digits[0] === digits[1];
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function hasSameDigits($s) {
        $digits = array_map('intval', str_split($s));
        while (count($digits) > 2) {
            $n = count($digits);
            $next = [];
            for ($i = 0; $i < $n - 1; $i++) {
                $next[] = ($digits[$i] + $digits[$i + 1]) % 10;
            }
            $digits = $next;
        }
        return $digits[0] === $digits[1];
    }
}
```

## Swift

```swift
class Solution {
    func hasSameDigits(_ s: String) -> Bool {
        var digits = s.map { Int(String($0))! }
        while digits.count > 2 {
            var next = [Int]()
            for i in 0..<(digits.count - 1) {
                next.append((digits[i] + digits[i + 1]) % 10)
            }
            digits = next
        }
        return digits[0] == digits[1]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun hasSameDigits(s: String): Boolean {
        var digits = s.map { it - '0' }
        while (digits.size > 2) {
            val next = IntArray(digits.size - 1)
            for (i in digits.indices.dropLast(1)) {
                next[i] = (digits[i] + digits[i + 1]) % 10
            }
            digits = next.toList()
        }
        return digits[0] == digits[1]
    }
}
```

## Dart

```dart
class Solution {
  bool hasSameDigits(String s) {
    List<int> cur = s.codeUnits.map((c) => c - 48).toList();
    while (cur.length > 2) {
      List<int> next = List.filled(cur.length - 1, 0);
      for (int i = 0; i < cur.length - 1; i++) {
        next[i] = (cur[i] + cur[i + 1]) % 10;
      }
      cur = next;
    }
    return cur[0] == cur[1];
  }
}
```

## Golang

```go
func hasSameDigits(s string) bool {
	n := len(s)
	digits := make([]int, n)
	for i := 0; i < n; i++ {
		digits[i] = int(s[i] - '0')
	}
	for len(digits) > 2 {
		m := len(digits) - 1
		next := make([]int, m)
		for i := 0; i < m; i++ {
			next[i] = (digits[i] + digits[i+1]) % 10
		}
		digits = next
	}
	return digits[0] == digits[1]
}
```

## Ruby

```ruby
def has_same_digits(s)
  digits = s.chars.map { |c| c.ord - 48 }
  while digits.length > 2
    next_digits = []
    (0...digits.length - 1).each do |i|
      next_digits << (digits[i] + digits[i + 1]) % 10
    end
    digits = next_digits
  end
  digits[0] == digits[1]
end
```

## Scala

```scala
object Solution {
    def hasSameDigits(s: String): Boolean = {
        var cur = s.map(_.asDigit).toArray
        while (cur.length > 2) {
            val next = new Array[Int](cur.length - 1)
            for (i <- 0 until cur.length - 1) {
                next(i) = (cur(i) + cur(i + 1)) % 10
            }
            cur = next
        }
        cur(0) == cur(1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn has_same_digits(s: String) -> bool {
        let mut digits: Vec<u8> = s.bytes().map(|b| b - b'0').collect();
        while digits.len() > 2 {
            let n = digits.len();
            let mut next = Vec::with_capacity(n - 1);
            for i in 0..n - 1 {
                next.push((digits[i] + digits[i + 1]) % 10);
            }
            digits = next;
        }
        digits[0] == digits[1]
    }
}
```

## Racket

```racket
(define/contract (has-same-digits s)
  (-> string? boolean?)
  (let loop ((digits
              (map (lambda (c) (- (char->integer c) (char->integer #\0)))
                   (string->list s))))
    (if (= (length digits) 2)
        (= (first digits) (second digits))
        (loop
         (for/list ([i (in-range (- (length digits) 1))])
           (modulo (+ (list-ref digits i) (list-ref digits (+ i 1))) 10))))))
```

## Erlang

```erlang
-spec has_same_digits(S :: unicode:unicode_binary()) -> boolean().
has_same_digits(S) ->
    Digits = [C - $0 || C <- binary_to_list(S)],
    same_until_two(Digits).

same_until_two([A, B]) -> A == B;
same_until_two(Digits) ->
    Next = sums_mod10(Digits),
    same_until_two(Next).

sums_mod10([_]) -> [];
sums_mod10([X, Y | Rest]) ->
    [(X + Y) rem 10 | sums_mod10([Y | Rest])].
```

## Elixir

```elixir
defmodule Solution do
  @spec has_same_digits(s :: String.t()) :: boolean()
  def has_same_digits(s) do
    digits = String.graphemes(s) |> Enum.map(&String.to_integer/1)
    final = reduce_to_two(digits)
    [a, b] = final
    a == b
  end

  defp reduce_to_two(digits) when length(digits) <= 2, do: digits

  defp reduce_to_two(digits) do
    len = length(digits)

    next =
      for i <- 0..(len - 2) do
        rem(Enum.at(digits, i) + Enum.at(digits, i + 1), 10)
      end

    reduce_to_two(next)
  end
end
```
