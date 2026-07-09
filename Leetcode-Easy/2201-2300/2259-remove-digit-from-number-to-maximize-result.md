# 2259. Remove Digit From Number to Maximize Result

## Cpp

```cpp
class Solution {
public:
    string removeDigit(string number, char digit) {
        string best;
        bool first = true;
        int n = number.size();
        for (int i = 0; i < n; ++i) {
            if (number[i] == digit) {
                string cand = number.substr(0, i) + number.substr(i + 1);
                if (first || cand > best) {
                    best = cand;
                    first = false;
                }
            }
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public String removeDigit(String number, char digit) {
        String best = "";
        int n = number.length();
        for (int i = 0; i < n; i++) {
            if (number.charAt(i) == digit) {
                String candidate = number.substring(0, i) + number.substring(i + 1);
                if (best.isEmpty() || candidate.compareTo(best) > 0) {
                    best = candidate;
                }
            }
        }
        return best;
    }
}
```

## Python

```python
class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        best = ""
        for i, ch in enumerate(number):
            if ch == digit:
                candidate = number[:i] + number[i+1:]
                if candidate > best:
                    best = candidate
        return best
```

## Python3

```python
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        best = ""
        for i, ch in enumerate(number):
            if ch == digit:
                candidate = number[:i] + number[i+1:]
                if candidate > best:
                    best = candidate
        return best
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* removeDigit(char* number, char digit) {
    int n = strlen(number);
    int idx = -1;
    for (int i = 0; i < n - 1; ++i) {
        if (number[i] == digit && number[i] < number[i + 1]) {
            idx = i;
            break;
        }
    }
    if (idx == -1) {
        for (int i = n - 1; i >= 0; --i) {
            if (number[i] == digit) {
                idx = i;
                break;
            }
        }
    }
    char* res = (char*)malloc(n); // length after removal is n-1, plus null terminator
    int pos = 0;
    for (int i = 0; i < n; ++i) {
        if (i != idx) {
            res[pos++] = number[i];
        }
    }
    res[pos] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string RemoveDigit(string number, char digit)
    {
        string best = "";
        for (int i = 0; i < number.Length; i++)
        {
            if (number[i] == digit)
            {
                string candidate = number.Remove(i, 1);
                if (best == "" || string.Compare(candidate, best, StringComparison.Ordinal) > 0)
                {
                    best = candidate;
                }
            }
        }
        return best;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} number
 * @param {character} digit
 * @return {string}
 */
var removeDigit = function(number, digit) {
    let best = "";
    for (let i = 0; i < number.length; ++i) {
        if (number[i] === digit) {
            const candidate = number.slice(0, i) + number.slice(i + 1);
            if (candidate > best) {
                best = candidate;
            }
        }
    }
    return best;
};
```

## Typescript

```typescript
function removeDigit(number: string, digit: string): string {
    let best = "";
    for (let i = 0; i < number.length; i++) {
        if (number[i] === digit) {
            const candidate = number.slice(0, i) + number.slice(i + 1);
            if (candidate > best) {
                best = candidate;
            }
        }
    }
    return best;
}
```

## Php

```php
class Solution {
    /**
     * @param String $number
     * @param String $digit
     * @return String
     */
    function removeDigit($number, $digit) {
        $len = strlen($number);
        for ($i = 0; $i < $len; $i++) {
            if ($number[$i] === $digit) {
                if ($i + 1 < $len && $number[$i + 1] > $digit) {
                    return substr($number, 0, $i) . substr($number, $i + 1);
                }
            }
        }
        $pos = strrpos($number, $digit);
        return substr($number, 0, $pos) . substr($number, $pos + 1);
    }
}
```

## Swift

```swift
class Solution {
    func removeDigit(_ number: String, _ digit: Character) -> String {
        let chars = Array(number)
        var best = ""
        for i in 0..<chars.count {
            if chars[i] == digit {
                var candidateChars = chars
                candidateChars.remove(at: i)
                let cand = String(candidateChars)
                if cand > best {
                    best = cand
                }
            }
        }
        return best
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun removeDigit(number: String, digit: Char): String {
        var best = ""
        for (i in number.indices) {
            if (number[i] == digit) {
                val candidate = number.removeRange(i, i + 1)
                if (candidate > best) {
                    best = candidate
                }
            }
        }
        return best
    }
}
```

## Dart

```dart
class Solution {
  String removeDigit(String number, String digit) {
    String best = "";
    for (int i = 0; i < number.length; i++) {
      if (number[i] == digit) {
        String candidate = number.substring(0, i) + number.substring(i + 1);
        if (candidate.compareTo(best) > 0) {
          best = candidate;
        }
      }
    }
    return best;
  }
}
```

## Golang

```go
func removeDigit(number string, digit byte) string {
    best := ""
    for i := 0; i < len(number); i++ {
        if number[i] == digit {
            candidate := number[:i] + number[i+1:]
            if best == "" || candidate > best {
                best = candidate
            }
        }
    }
    return best
}
```

## Ruby

```ruby
def remove_digit(number, digit)
  best = ""
  (0...number.length).each do |i|
    next unless number[i] == digit
    candidate = number[0...i] + number[(i + 1)..-1].to_s
    best = candidate if best.empty? || candidate > best
  end
  best
end
```

## Scala

```scala
object Solution {
    def removeDigit(number: String, digit: Char): String = {
        var best = ""
        for (i <- 0 until number.length if number(i) == digit) {
            val candidate = number.substring(0, i) + number.substring(i + 1)
            if (candidate > best) best = candidate
        }
        best
    }
}
```

## Rust

```rust
impl Solution {
    pub fn remove_digit(number: String, digit: char) -> String {
        let mut best = String::new();
        for (i, ch) in number.chars().enumerate() {
            if ch == digit {
                let mut candidate = number.clone();
                candidate.remove(i);
                if best.is_empty() || candidate > best {
                    best = candidate;
                }
            }
        }
        best
    }
}
```

## Racket

```racket
(define/contract (remove-digit number digit)
  (-> string? char? string?)
  (let* ([len (string-length number)]
         [candidates
          (for/list ([i (in-range len)]
                     #:when (char=? (string-ref number i) digit))
            (string-append (substring number 0 i)
                           (substring number (+ i 1) len)))])
    (foldl (lambda (cand best)
             (if (string>? cand best) cand best))
           (first candidates)
           (rest candidates))))
```

## Erlang

```erlang
-spec remove_digit(Number :: unicode:unicode_binary(), Digit :: char()) -> unicode:unicode_binary().
remove_digit(Number, Digit) ->
    Len = byte_size(Number),
    Indices = [I || I <- lists:seq(0, Len - 1), binary:at(Number, I) =:= Digit],
    Candidates = [
        << (binary:part(Number, 0, I))/binary,
           (binary:part(Number, I + 1, Len - I - 1))/binary >>
        || I <- Indices
    ],
    lists:max(Candidates).
```

## Elixir

```elixir
defmodule Solution do
  @spec remove_digit(number :: String.t(), digit :: char | String.t()) :: String.t()
  def remove_digit(number, digit) do
    chars = String.graphemes(number)

    digit_str =
      if is_integer(digit), do: <<digit::utf8>>, else: digit

    {best, _} =
      Enum.reduce(Enum.with_index(chars), {"", -1}, fn {c, idx}, {cur_best, _} ->
        if c == digit_str do
          candidate = chars |> List.delete_at(idx) |> Enum.join()

          if cur_best == "" or candidate > cur_best do
            {candidate, idx}
          else
            {cur_best, idx}
          end
        else
          {cur_best, idx}
        end
      end)

    best
  end
end
```
