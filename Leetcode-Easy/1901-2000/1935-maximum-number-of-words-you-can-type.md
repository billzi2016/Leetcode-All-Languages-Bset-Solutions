# 1935. Maximum Number of Words You Can Type

## Cpp

```cpp
class Solution {
public:
    int canBeTypedWords(string text, string brokenLetters) {
        bool broken[26] = {false};
        for (char c : brokenLetters) broken[c - 'a'] = true;
        
        int count = 0;
        size_t i = 0, n = text.size();
        while (i < n) {
            // find end of word
            size_t j = i;
            bool ok = true;
            while (j < n && text[j] != ' ') {
                if (broken[text[j] - 'a']) {
                    ok = false;
                }
                ++j;
            }
            if (ok) ++count;
            i = j + 1; // skip space
        }
        return count;
    }
};
```

## Java

```java
class Solution {
    public int canBeTypedWords(String text, String brokenLetters) {
        boolean[] broken = new boolean[26];
        for (char c : brokenLetters.toCharArray()) {
            broken[c - 'a'] = true;
        }
        int count = 0;
        for (String word : text.split(" ")) {
            boolean canType = true;
            for (char c : word.toCharArray()) {
                if (broken[c - 'a']) {
                    canType = false;
                    break;
                }
            }
            if (canType) {
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
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        broken = set(brokenLetters)
        count = 0
        for word in text.split():
            if not any(ch in broken for ch in word):
                count += 1
        return count
```

## Python3

```python
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        count = 0
        for word in text.split():
            if not any(ch in broken for ch in word):
                count += 1
        return count
```

## C

```c
#include <stdbool.h>

int canBeTypedWords(char* text, char* brokenLetters) {
    bool broken[26] = {false};
    for (char *p = brokenLetters; *p; ++p) {
        broken[*p - 'a'] = true;
    }
    
    int count = 0;
    char *ptr = text;
    while (*ptr) {
        bool ok = true;
        while (*ptr && *ptr != ' ') {
            if (broken[*ptr - 'a']) {
                ok = false;
            }
            ++ptr;
        }
        if (ok) {
            ++count;
        }
        if (*ptr == ' ') {
            ++ptr; // skip space
        }
    }
    
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int CanBeTypedWords(string text, string brokenLetters) {
        var brokenSet = new HashSet<char>(brokenLetters);
        int count = 0;
        foreach (var word in text.Split(' ')) {
            bool canType = true;
            foreach (char c in word) {
                if (brokenSet.Contains(c)) {
                    canType = false;
                    break;
                }
            }
            if (canType) count++;
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} text
 * @param {string} brokenLetters
 * @return {number}
 */
var canBeTypedWords = function(text, brokenLetters) {
    const brokenSet = new Set(brokenLetters);
    let count = 0;
    for (const word of text.split(' ')) {
        let ok = true;
        for (let i = 0; i < word.length; i++) {
            if (brokenSet.has(word[i])) {
                ok = false;
                break;
            }
        }
        if (ok) count++;
    }
    return count;
};
```

## Typescript

```typescript
function canBeTypedWords(text: string, brokenLetters: string): number {
    const brokenSet = new Set(brokenLetters);
    let count = 0;
    for (const word of text.split(' ')) {
        let ok = true;
        for (const ch of word) {
            if (brokenSet.has(ch)) {
                ok = false;
                break;
            }
        }
        if (ok) count++;
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param String $text
     * @param String $brokenLetters
     * @return Integer
     */
    function canBeTypedWords($text, $brokenLetters) {
        // Build a set of broken letters for O(1) lookup
        $brokenSet = [];
        if ($brokenLetters !== '') {
            foreach (str_split($brokenLetters) as $ch) {
                $brokenSet[$ch] = true;
            }
        }

        $words = explode(' ', $text);
        $count = 0;

        foreach ($words as $word) {
            $canType = true;
            foreach (str_split($word) as $c) {
                if (isset($brokenSet[$c])) {
                    $canType = false;
                    break;
                }
            }
            if ($canType) {
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
    func canBeTypedWords(_ text: String, _ brokenLetters: String) -> Int {
        let brokenSet = Set(brokenLetters)
        var count = 0
        for word in text.split(separator: " ") {
            var canType = true
            for ch in word {
                if brokenSet.contains(ch) {
                    canType = false
                    break
                }
            }
            if canType { count += 1 }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canBeTypedWords(text: String, brokenLetters: String): Int {
        val broken = BooleanArray(26)
        for (c in brokenLetters) {
            broken[c - 'a'] = true
        }
        var count = 0
        var i = 0
        val n = text.length
        while (i < n) {
            var j = i
            var canType = true
            while (j < n && text[j] != ' ') {
                if (broken[text[j] - 'a']) {
                    canType = false
                }
                j++
            }
            if (canType) count++
            i = j + 1 // skip space
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int canBeTypedWords(String text, String brokenLetters) {
    final List<bool> broken = List.filled(26, false);
    for (int i = 0; i < brokenLetters.length; ++i) {
      broken[brokenLetters.codeUnitAt(i) - 97] = true;
    }

    int count = 0;
    for (final word in text.split(' ')) {
      bool canType = true;
      for (int j = 0; j < word.length; ++j) {
        if (broken[word.codeUnitAt(j) - 97]) {
          canType = false;
          break;
        }
      }
      if (canType) count++;
    }

    return count;
  }
}
```

## Golang

```go
import "strings"

func canBeTypedWords(text string, brokenLetters string) int {
	broken := [26]bool{}
	for _, ch := range brokenLetters {
		broken[ch-'a'] = true
	}
	count := 0
	for _, word := range strings.Split(text, " ") {
		ok := true
		for _, c := range word {
			if broken[c-'a'] {
				ok = false
				break
			}
		}
		if ok {
			count++
		}
	}
	return count
}
```

## Ruby

```ruby
# @param {String} text
# @param {String} broken_letters
# @return {Integer}
def can_be_typed_words(text, broken_letters)
  broken = {}
  broken_letters.each_char { |c| broken[c] = true }
  count = 0
  text.split(' ').each do |word|
    can_type = true
    word.each_char do |ch|
      if broken.key?(ch)
        can_type = false
        break
      end
    end
    count += 1 if can_type
  end
  count
end
```

## Scala

```scala
object Solution {
    def canBeTypedWords(text: String, brokenLetters: String): Int = {
        val broken = brokenLetters.toSet
        var count = 0
        for (word <- text.split(" ")) {
            var ok = true
            var i = 0
            while (i < word.length && ok) {
                if (broken.contains(word.charAt(i))) ok = false
                i += 1
            }
            if (ok) count += 1
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn can_be_typed_words(text: String, broken_letters: String) -> i32 {
        use std::collections::HashSet;
        let broken: HashSet<char> = broken_letters.chars().collect();
        let mut count = 0;
        for word in text.split(' ') {
            if !word.chars().any(|c| broken.contains(&c)) {
                count += 1;
            }
        }
        count as i32
    }
}
```

## Racket

```racket
#lang racket

(require racket/string)

(define/contract (can-be-typed-words text brokenLetters)
  (-> string? string? exact-integer?)
  (let* ([broken-set (let ([h (make-hash)])
                       (for ([c (in-string brokenLetters)]) (hash-set! h c #t))
                       h)]
         [words (string-split text " ")])
    (for/fold ([cnt 0]) ([w words])
      (if (ormap (lambda (c) (hash-has-key? broken-set c)) (in-string w))
          cnt
          (add1 cnt)))))
```

## Erlang

```erlang
-spec can_be_typed_words(Text :: unicode:unicode_binary(), BrokenLetters :: unicode:unicode_binary()) -> integer().
can_be_typed_words(Text, BrokenLetters) ->
    BrokenSet = maps:from_list([ {C,true} || <<C>> <- BrokenLetters ]),
    Words = binary:split(Text, <<" ">>, [global]),
    count_typable(Words, BrokenSet, 0).

count_typable([], _Set, Acc) -> Acc;
count_typable([Word|Rest], Set, Acc) ->
    case word_ok(Word, Set) of
        true -> count_typable(Rest, Set, Acc + 1);
        false -> count_typable(Rest, Set, Acc)
    end.

word_ok(<<>>, _Set) -> true;
word_ok(<<C, Rest/binary>>, Set) ->
    case maps:is_key(C, Set) of
        true -> false;
        false -> word_ok(Rest, Set)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec can_be_typed_words(text :: String.t(), broken_letters :: String.t()) :: integer()
  def can_be_typed_words(text, broken_letters) do
    broken_set = MapSet.new(String.graphemes(broken_letters))

    text
    |> String.split(" ")
    |> Enum.count(fn word ->
      not Enum.any?(String.graphemes(word), &MapSet.member?(broken_set, &1))
    end)
  end
end
```
