# 3120. Count the Number of Special Characters I

## Cpp

```cpp
class Solution {
public:
    int numberOfSpecialChars(string word) {
        bool lower[26] = {false};
        bool upper[26] = {false};
        for (char c : word) {
            if ('a' <= c && c <= 'z')
                lower[c - 'a'] = true;
            else
                upper[c - 'A'] = true;
        }
        int count = 0;
        for (int i = 0; i < 26; ++i)
            if (lower[i] && upper[i])
                ++count;
        return count;
    }
};
```

## Java

```java
class Solution {
    public int numberOfSpecialChars(String word) {
        boolean[] lower = new boolean[26];
        boolean[] upper = new boolean[26];
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (c >= 'a' && c <= 'z') {
                lower[c - 'a'] = true;
            } else { // uppercase
                upper[c - 'A'] = true;
            }
        }
        int count = 0;
        for (int i = 0; i < 26; i++) {
            if (lower[i] && upper[i]) {
                count++;
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        lower = set()
        upper = set()
        for ch in word:
            if 'a' <= ch <= 'z':
                lower.add(ch)
            else:
                upper.add(ch.lower())
        return len(lower & upper)
```

## Python3

```python
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = set()
        upper = set()
        for ch in word:
            if 'a' <= ch <= 'z':
                lower.add(ch)
            else:
                upper.add(ch.lower())
        return len(lower & upper)
```

## C

```c
#include <ctype.h>

int numberOfSpecialChars(char* word) {
    int lower[26] = {0}, upper[26] = {0};
    for (char *p = word; *p; ++p) {
        char c = *p;
        if (c >= 'a' && c <= 'z')
            lower[c - 'a'] = 1;
        else if (c >= 'A' && c <= 'Z')
            upper[c - 'A'] = 1;
    }
    int cnt = 0;
    for (int i = 0; i < 26; ++i)
        if (lower[i] && upper[i])
            ++cnt;
    return cnt;
}
```

## Csharp

```csharp
public class Solution {
    public int NumberOfSpecialChars(string word) {
        bool[] lower = new bool[26];
        bool[] upper = new bool[26];
        foreach (char c in word) {
            if (c >= 'a' && c <= 'z')
                lower[c - 'a'] = true;
            else if (c >= 'A' && c <= 'Z')
                upper[c - 'A'] = true;
        }
        int count = 0;
        for (int i = 0; i < 26; i++) {
            if (lower[i] && upper[i]) count++;
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word
 * @return {number}
 */
var numberOfSpecialChars = function(word) {
    const lower = new Array(26).fill(false);
    const upper = new Array(26).fill(false);
    for (const ch of word) {
        const code = ch.charCodeAt(0);
        if (code >= 97) { // 'a' to 'z'
            lower[code - 97] = true;
        } else { // 'A' to 'Z'
            upper[code - 65] = true;
        }
    }
    let count = 0;
    for (let i = 0; i < 26; i++) {
        if (lower[i] && upper[i]) count++;
    }
    return count;
};
```

## Typescript

```typescript
function numberOfSpecialChars(word: string): number {
    const lower = new Array(26).fill(false);
    const upper = new Array(26).fill(false);
    for (const ch of word) {
        const code = ch.charCodeAt(0);
        if (code >= 97) { // 'a' to 'z'
            lower[code - 97] = true;
        } else { // 'A' to 'Z'
            upper[code - 65] = true;
        }
    }
    let count = 0;
    for (let i = 0; i < 26; i++) {
        if (lower[i] && upper[i]) count++;
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param String $word
     * @return Integer
     */
    function numberOfSpecialChars($word) {
        $lower = array_fill(0, 26, false);
        $upper = array_fill(0, 26, false);
        $len = strlen($word);
        for ($i = 0; $i < $len; $i++) {
            $c = $word[$i];
            $ord = ord($c);
            if ($ord >= 97 && $ord <= 122) { // lowercase
                $lower[$ord - 97] = true;
            } elseif ($ord >= 65 && $ord <= 90) { // uppercase
                $upper[$ord - 65] = true;
            }
        }
        $count = 0;
        for ($i = 0; $i < 26; $i++) {
            if ($lower[$i] && $upper[$i]) {
                $count++;
            }
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func numberOfSpecialChars(_ word: String) -> Int {
        var lower = [Bool](repeating: false, count: 26)
        var upper = [Bool](repeating: false, count: 26)
        
        for scalar in word.unicodeScalars {
            let v = scalar.value
            if v >= 97 && v <= 122 { // 'a' to 'z'
                lower[Int(v - 97)] = true
            } else if v >= 65 && v <= 90 { // 'A' to 'Z'
                upper[Int(v - 65)] = true
            }
        }
        
        var count = 0
        for i in 0..<26 {
            if lower[i] && upper[i] {
                count += 1
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfSpecialChars(word: String): Int {
        val lower = BooleanArray(26)
        val upper = BooleanArray(26)
        for (ch in word) {
            if (ch.isLowerCase()) {
                lower[ch - 'a'] = true
            } else {
                upper[ch - 'A'] = true
            }
        }
        var count = 0
        for (i in 0 until 26) {
            if (lower[i] && upper[i]) count++
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int numberOfSpecialChars(String word) {
    List<bool> lower = List.filled(26, false);
    List<bool> upper = List.filled(26, false);
    for (int i = 0; i < word.length; i++) {
      int code = word.codeUnitAt(i);
      if (code >= 97 && code <= 122) {
        lower[code - 97] = true;
      } else if (code >= 65 && code <= 90) {
        upper[code - 65] = true;
      }
    }
    int count = 0;
    for (int i = 0; i < 26; i++) {
      if (lower[i] && upper[i]) count++;
    }
    return count;
  }
}
```

## Golang

```go
func numberOfSpecialChars(word string) int {
	var lower, upper [26]bool
	for _, ch := range word {
		if ch >= 'a' && ch <= 'z' {
			lower[ch-'a'] = true
		} else if ch >= 'A' && ch <= 'Z' {
			upper[ch-'A'] = true
		}
	}
	cnt := 0
	for i := 0; i < 26; i++ {
		if lower[i] && upper[i] {
			cnt++
		}
	}
	return cnt
}
```

## Ruby

```ruby
def number_of_special_chars(word)
  lower = Array.new(26, false)
  upper = Array.new(26, false)

  word.each_char do |ch|
    if ch >= 'a' && ch <= 'z'
      lower[ch.ord - 97] = true
    else
      upper[ch.ord - 65] = true
    end
  end

  count = 0
  26.times { |i| count += 1 if lower[i] && upper[i] }
  count
end
```

## Scala

```scala
object Solution {
    def numberOfSpecialChars(word: String): Int = {
        val lower = Array.fill(26)(false)
        val upper = Array.fill(26)(false)

        for (c <- word) {
            if (c >= 'a' && c <= 'z')
                lower(c - 'a') = true
            else if (c >= 'A' && c <= 'Z')
                upper(c - 'A') = true
        }

        var count = 0
        for (i <- 0 until 26) {
            if (lower(i) && upper(i)) count += 1
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_special_chars(word: String) -> i32 {
        let mut lower = [false; 26];
        let mut upper = [false; 26];
        for b in word.bytes() {
            if (b'a'..=b'z').contains(&b) {
                lower[(b - b'a') as usize] = true;
            } else if (b'A'..=b'Z').contains(&b) {
                upper[(b - b'A') as usize] = true;
            }
        }
        let mut cnt = 0;
        for i in 0..26 {
            if lower[i] && upper[i] {
                cnt += 1;
            }
        }
        cnt as i32
    }
}
```

## Racket

```racket
(define/contract (number-of-special-chars word)
  (-> string? exact-integer?)
  (let* ([lower (make-vector 26 #f)]
         [upper (make-vector 26 #f)])
    (for ([c (in-string word)])
      (let* ([idx (- (char->integer (char-downcase c))
                     (char->integer #\a))])
        (if (char-lower-case? c)
            (vector-set! lower idx #t)
            (vector-set! upper idx #t))))
    (for/sum ([i (in-range 26)])
      (if (and (vector-ref lower i) (vector-ref upper i)) 1 0))))
```

## Erlang

```erlang
-module(solution).
-export([number_of_special_chars/1]).

-spec number_of_special_chars(unicode:unicode_binary()) -> integer().
number_of_special_chars(Word) ->
    Chars = unicode:characters_to_list(Word),
    {LowerMap, UpperMap} = lists:foldl(
        fun(C, {L, U}) ->
            if
                C >= $a, C =< $z ->
                    {maps:put(C, true, L), U};
                C >= $A, C =< $Z ->
                    {L, maps:put(C, true, U)};
                true ->
                    {L, U}
            end
        end,
        {#{}, #{}},
        Chars),
    maps:fold(
        fun(Lc, _Val, Acc) ->
            Up = Lc - 32,
            case maps:is_key(Up, UpperMap) of
                true -> Acc + 1;
                false -> Acc
            end
        end,
        0,
        LowerMap).
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_special_chars(word :: String.t()) :: integer()
  def number_of_special_chars(word) do
    {lower_set, upper_set} =
      word
      |> String.to_charlist()
      |> Enum.reduce({MapSet.new(), MapSet.new()}, fn char, {lset, uset} ->
        cond do
          char >= ?a and char <= ?z -> {MapSet.put(lset, char), uset}
          char >= ?A and char <= ?Z -> {lset, MapSet.put(uset, char)}
          true -> {lset, uset}
        end
      end)

    Enum.count(lower_set, fn lc ->
      uc = lc - (?a - ?A)
      MapSet.member?(upper_set, uc)
    end)
  end
end
```
