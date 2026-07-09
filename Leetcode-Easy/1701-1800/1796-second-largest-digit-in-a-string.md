# 1796. Second Largest Digit in a String

## Cpp

```cpp
class Solution {
public:
    int secondHighest(string s) {
        int first = -1, second = -1;
        for (char c : s) {
            if (c < '0' || c > '9') continue;
            int d = c - '0';
            if (d > first) {
                second = first;
                first = d;
            } else if (d < first && d > second) {
                second = d;
            }
        }
        return second;
    }
};
```

## Java

```java
class Solution {
    public int secondHighest(String s) {
        int max = -1, second = -1;
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (ch >= '0' && ch <= '9') {
                int d = ch - '0';
                if (d > max) {
                    second = max;
                    max = d;
                } else if (d < max && d > second) {
                    second = d;
                }
            }
        }
        return second;
    }
}
```

## Python

```python
class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        digits = {int(ch) for ch in s if ch.isdigit()}
        if len(digits) < 2:
            return -1
        # Return the second largest element
        return sorted(digits)[-2]
```

## Python3

```python
class Solution:
    def secondHighest(self, s: str) -> int:
        digits = set()
        for ch in s:
            if '0' <= ch <= '9':
                digits.add(ord(ch) - 48)
        if len(digits) < 2:
            return -1
        first = max(digits)
        digits.remove(first)
        return max(digits)
```

## C

```c
int secondHighest(char* s) {
    int mask = 0;
    for (int i = 0; s[i]; ++i) {
        char c = s[i];
        if (c >= '0' && c <= '9') {
            mask |= 1 << (c - '0');
        }
    }
    int count = 0, result = -1;
    for (int d = 9; d >= 0; --d) {
        if (mask & (1 << d)) {
            ++count;
            if (count == 2) {
                result = d;
                break;
            }
        }
    }
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int SecondHighest(string s) {
        int first = -1, second = -1;
        foreach (char c in s) {
            if (c < '0' || c > '9') continue;
            int d = c - '0';
            if (d > first) {
                second = first;
                first = d;
            } else if (d < first && d > second) {
                second = d;
            }
        }
        return second;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var secondHighest = function(s) {
    const seen = new Set();
    for (const ch of s) {
        if (ch >= '0' && ch <= '9') {
            seen.add(ch.charCodeAt(0) - 48);
        }
    }
    let max1 = -1, max2 = -1;
    for (const d of seen) {
        if (d > max1) {
            max2 = max1;
            max1 = d;
        } else if (d < max1 && d > max2) {
            max2 = d;
        }
    }
    return max2;
};
```

## Typescript

```typescript
function secondHighest(s: string): number {
    let first = -1, second = -1;
    for (const ch of s) {
        const code = ch.charCodeAt(0);
        if (code >= 48 && code <= 57) {
            const d = code - 48;
            if (d > first) {
                second = first;
                first = d;
            } else if (d < first && d > second) {
                second = d;
            }
        }
    }
    return second;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function secondHighest($s) {
        $present = array_fill(0, 10, false);
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $ch = $s[$i];
            if ($ch >= '0' && $ch <= '9') {
                $digit = ord($ch) - 48;
                $present[$digit] = true;
            }
        }
        $found = 0;
        for ($d = 9; $d >= 0; $d--) {
            if ($present[$d]) {
                $found++;
                if ($found == 2) {
                    return $d;
                }
            }
        }
        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func secondHighest(_ s: String) -> Int {
        var present = [Bool](repeating: false, count: 10)
        for ch in s {
            if let digit = ch.wholeNumberValue {
                present[digit] = true
            }
        }
        var first = -1
        var second = -1
        for d in stride(from: 9, through: 0, by: -1) {
            if present[d] {
                if first == -1 {
                    first = d
                } else {
                    second = d
                    break
                }
            }
        }
        return second
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun secondHighest(s: String): Int {
        var first = -1
        var second = -1
        for (ch in s) {
            if (ch.isDigit()) {
                val d = ch - '0'
                if (d > first) {
                    second = first
                    first = d
                } else if (d < first && d > second) {
                    second = d
                }
            }
        }
        return second
    }
}
```

## Dart

```dart
class Solution {
  int secondHighest(String s) {
    int first = -1;
    int second = -1;
    for (int i = 0; i < s.length; ++i) {
      int code = s.codeUnitAt(i);
      if (code >= 48 && code <= 57) {
        int d = code - 48;
        if (d > first) {
          second = first;
          first = d;
        } else if (d < first && d > second) {
          second = d;
        }
      }
    }
    return second;
  }
}
```

## Golang

```go
func secondHighest(s string) int {
    var seen [10]bool
    for _, ch := range s {
        if ch >= '0' && ch <= '9' {
            seen[ch-'0'] = true
        }
    }
    count := 0
    for d := 9; d >= 0; d-- {
        if seen[d] {
            count++
            if count == 2 {
                return d
            }
        }
    }
    return -1
}
```

## Ruby

```ruby
def second_highest(s)
  max1 = -1
  max2 = -1
  s.each_char do |ch|
    next unless ch >= '0' && ch <= '9'
    d = ch.ord - 48
    if d > max1
      max2 = max1
      max1 = d
    elsif d != max1 && d > max2
      max2 = d
    end
  end
  max2
end
```

## Scala

```scala
object Solution {
    def secondHighest(s: String): Int = {
        var first = -1
        var second = -1
        for (ch <- s) {
            if (ch >= '0' && ch <= '9') {
                val d = ch - '0'
                if (d > first) {
                    second = first
                    first = d
                } else if (d < first && d > second) {
                    second = d
                }
            }
        }
        second
    }
}
```

## Rust

```rust
impl Solution {
    pub fn second_highest(s: String) -> i32 {
        let mut present = [false; 10];
        for b in s.bytes() {
            if b >= b'0' && b <= b'9' {
                present[(b - b'0') as usize] = true;
            }
        }

        // Find the largest digit
        for i in (0..=9).rev() {
            if present[i] {
                // Find the next smaller digit
                for j in (0..i).rev() {
                    if present[j] {
                        return j as i32;
                    }
                }
                break;
            }
        }
        -1
    }
}
```

## Racket

```racket
(require racket/contract)

(define/contract (second-highest s)
  (-> string? exact-integer?)
  (let* ([len (string-length s)]
         [present (make-vector 10 #f)])
    (for ([i (in-range len)])
      (let ([c (string-ref s i)])
        (when (and (char>=? c #\0) (char<=? c #\9))
          (vector-set! present (- (char->integer c) (char->integer #\0)) #t))))
    (let loop ((d 9) (found '()))
      (if (< d 0)
          (if (>= (length found) 2)
              (list-ref found 1)
              -1)
          (if (vector-ref present d)
              (loop (- d 1) (cons d found))
              (loop (- d 1) found))))))
```

## Erlang

```erlang
-module(solution).
-export([second_highest/1]).

-spec second_highest(S :: unicode:unicode_binary()) -> integer().
second_highest(S) ->
    Mask = build_mask(S, 0),
    find_second(Mask).

build_mask(<<>>, Acc) ->
    Acc;
build_mask(<<C, Rest/binary>>, Acc) when C >= $0, C =< $9 ->
    D = C - $0,
    NewAcc = Acc bor (1 bsl D),
    build_mask(Rest, NewAcc);
build_mask(<<_, Rest/binary>>, Acc) ->
    build_mask(Rest, Acc).

find_second(Mask) ->
    find_second(Mask, 9, undefined).

find_second(_Mask, -1, _First) ->
    -1;
find_second(Mask, D, First) ->
    case (Mask band (1 bsl D)) =:= 0 of
        true ->
            find_second(Mask, D-1, First);
        false ->
            case First of
                undefined ->
                    find_second(Mask, D-1, D);
                _ ->
                    D
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec second_highest(s :: String.t) :: integer
  def second_highest(s) do
    digits =
      s
      |> String.graphemes()
      |> Enum.reduce(MapSet.new(), fn ch, acc ->
        case ch do
          <<c>> when c >= ?0 and c <= ?9 -> MapSet.put(acc, c - ?0)
          _ -> acc
        end
      end)

    if MapSet.size(digits) < 2 do
      -1
    else
      digits
      |> Enum.sort(:desc)
      |> Enum.at(1)
    end
  end
end
```
