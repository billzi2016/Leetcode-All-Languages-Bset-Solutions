# 2278. Percentage of Letter in String

## Cpp

```cpp
class Solution {
public:
    int percentageLetter(string s, char letter) {
        int cnt = 0;
        for (char c : s) if (c == letter) ++cnt;
        return cnt * 100 / static_cast<int>(s.size());
    }
};
```

## Java

```java
class Solution {
    public int percentageLetter(String s, char letter) {
        int count = 0;
        for (char c : s.toCharArray()) {
            if (c == letter) {
                count++;
            }
        }
        return count * 100 / s.length();
    }
}
```

## Python

```python
class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        return s.count(letter) * 100 // len(s)
```

## Python3

```python
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return (s.count(letter) * 100) // len(s)
```

## C

```c
int percentageLetter(char* s, char letter) {
    int total = 0, cnt = 0;
    for (char *p = s; *p != '\0'; ++p) {
        ++total;
        if (*p == letter) ++cnt;
    }
    return cnt * 100 / total;
}
```

## Csharp

```csharp
public class Solution {
    public int PercentageLetter(string s, char letter) {
        int count = 0;
        foreach (char c in s) {
            if (c == letter) count++;
        }
        return count * 100 / s.Length;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {character} letter
 * @return {number}
 */
var percentageLetter = function(s, letter) {
    let count = 0;
    for (let ch of s) {
        if (ch === letter) count++;
    }
    return Math.floor((count * 100) / s.length);
};
```

## Typescript

```typescript
function percentageLetter(s: string, letter: string): number {
    let count = 0;
    for (const ch of s) {
        if (ch === letter) count++;
    }
    return Math.floor((count * 100) / s.length);
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String $letter
     * @return Integer
     */
    function percentageLetter($s, $letter) {
        $total = strlen($s);
        $count = 0;
        // Since both are lowercase letters, we can use substr_count for simplicity
        $count = substr_count($s, $letter);
        return intdiv($count * 100, $total);
    }
}
```

## Swift

```swift
class Solution {
    func percentageLetter(_ s: String, _ letter: Character) -> Int {
        let total = s.count
        let count = s.reduce(0) { $1 == letter ? $0 + 1 : $0 }
        return count * 100 / total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun percentageLetter(s: String, letter: Char): Int {
        var count = 0
        for (c in s) {
            if (c == letter) count++
        }
        return count * 100 / s.length
    }
}
```

## Dart

```dart
class Solution {
  int percentageLetter(String s, String letter) {
    int count = 0;
    for (int i = 0; i < s.length; i++) {
      if (s[i] == letter) {
        count++;
      }
    }
    return (count * 100) ~/ s.length;
  }
}
```

## Golang

```go
func percentageLetter(s string, letter byte) int {
	count := 0
	for i := 0; i < len(s); i++ {
		if s[i] == letter {
			count++
		}
	}
	return count * 100 / len(s)
}
```

## Ruby

```ruby
# @param {String} s
# @param {Character} letter
# @return {Integer}
def percentage_letter(s, letter)
  (s.count(letter) * 100) / s.length
end
```

## Scala

```scala
object Solution {
    def percentageLetter(s: String, letter: Char): Int = {
        val count = s.count(_ == letter)
        (count * 100) / s.length
    }
}
```

## Rust

```rust
impl Solution {
    pub fn percentage_letter(s: String, letter: char) -> i32 {
        let total = s.len() as i32;
        let count = s.chars().filter(|&c| c == letter).count() as i32;
        (count * 100) / total
    }
}
```

## Racket

```racket
(define/contract (percentage-letter s letter)
  (-> string? char? exact-integer?)
  (let* ((len (string-length s))
         (cnt (for/sum ([i (in-range len)])
                (if (char=? (string-ref s i) letter) 1 0))))
    (quotient (* cnt 100) len)))
```

## Erlang

```erlang
-module(solution).
-export([percentage_letter/2]).

-spec percentage_letter(S :: unicode:unicode_binary(), Letter :: char()) -> integer().
percentage_letter(S, Letter) ->
    Len = byte_size(S),
    Count = count_occurrences(S, Letter, 0),
    (Count * 100) div Len.

count_occurrences(<<>>, _Letter, Acc) -> Acc;
count_occurrences(<<Char, Rest/binary>>, Letter, Acc) ->
    NewAcc = case Char of
        Letter -> Acc + 1;
        _ -> Acc
    end,
    count_occurrences(Rest, Letter, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec percentage_letter(s :: String.t(), letter :: char) :: integer
  def percentage_letter(s, letter) do
    target =
      case letter do
        <<c>> -> c
        _ when is_integer(letter) -> letter
        _ -> List.first(String.to_charlist(to_string(letter)))
      end

    total = String.length(s)

    count =
      s
      |> String.to_charlist()
      |> Enum.count(fn c -> c == target end)

    div(count * 100, total)
  end
end
```
