# 2586. Count the Number of Vowel Strings in Range

## Cpp

```cpp
class Solution {
public:
    int vowelStrings(vector<string>& words, int left, int right) {
        auto isVowel = [](char c) {
            return c=='a' || c=='e' || c=='i' || c=='o' || c=='u';
        };
        int cnt = 0;
        for (int i = left; i <= right; ++i) {
            const string& w = words[i];
            if (!w.empty() && isVowel(w.front()) && isVowel(w.back())) {
                ++cnt;
            }
        }
        return cnt;
    }
};
```

## Java

```java
class Solution {
    public int vowelStrings(String[] words, int left, int right) {
        int count = 0;
        for (int i = left; i <= right; i++) {
            String w = words[i];
            if (isVowel(w.charAt(0)) && isVowel(w.charAt(w.length() - 1))) {
                count++;
            }
        }
        return count;
    }

    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}
```

## Python

```python
class Solution(object):
    def vowelStrings(self, words, left, right):
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """
        vowels = set('aeiou')
        count = 0
        for i in range(left, right + 1):
            w = words[i]
            if w[0] in vowels and w[-1] in vowels:
                count += 1
        return count
```

## Python3

```python
from typing import List

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels = set('aeiou')
        count = 0
        for i in range(left, right + 1):
            w = words[i]
            if w[0] in vowels and w[-1] in vowels:
                count += 1
        return count
```

## C

```c
#include <string.h>

static int isVowel(char c) {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

int vowelStrings(char** words, int wordsSize, int left, int right) {
    int count = 0;
    for (int i = left; i <= right && i < wordsSize; ++i) {
        char *w = words[i];
        if (w[0] && isVowel(w[0]) && isVowel(w[strlen(w) - 1])) {
            ++count;
        }
    }
    return count;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int VowelStrings(string[] words, int left, int right) {
        HashSet<char> vowels = new HashSet<char>{'a','e','i','o','u'};
        int count = 0;
        for (int i = left; i <= right; i++) {
            string w = words[i];
            if (w.Length > 0 && vowels.Contains(w[0]) && vowels.Contains(w[w.Length - 1])) {
                count++;
            }
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @param {number} left
 * @param {number} right
 * @return {number}
 */
var vowelStrings = function(words, left, right) {
    const vowels = new Set(['a','e','i','o','u']);
    let count = 0;
    for (let i = left; i <= right; ++i) {
        const w = words[i];
        if (vowels.has(w[0]) && vowels.has(w[w.length - 1])) {
            ++count;
        }
    }
    return count;
};
```

## Typescript

```typescript
function vowelStrings(words: string[], left: number, right: number): number {
    const vowels = new Set(['a', 'e', 'i', 'o', 'u']);
    let count = 0;
    for (let i = left; i <= right; i++) {
        const w = words[i];
        if (vowels.has(w[0]) && vowels.has(w[w.length - 1])) {
            count++;
        }
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $words
     * @param Integer $left
     * @param Integer $right
     * @return Integer
     */
    function vowelStrings($words, $left, $right) {
        $vowels = ['a' => true, 'e' => true, 'i' => true, 'o' => true, 'u' => true];
        $count = 0;
        for ($i = $left; $i <= $right; $i++) {
            $word = $words[$i];
            $first = $word[0];
            $last = $word[strlen($word) - 1];
            if (isset($vowels[$first]) && isset($vowels[$last])) {
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
    func vowelStrings(_ words: [String], _ left: Int, _ right: Int) -> Int {
        let vowels: Set<Character> = ["a", "e", "i", "o", "u"]
        var count = 0
        for i in left...right {
            let word = words[i]
            if let first = word.first, let last = word.last,
               vowels.contains(first), vowels.contains(last) {
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
    fun vowelStrings(words: Array<String>, left: Int, right: Int): Int {
        var count = 0
        val vowels = setOf('a', 'e', 'i', 'o', 'u')
        for (i in left..right) {
            val w = words[i]
            if (w.first() in vowels && w.last() in vowels) {
                count++
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int vowelStrings(List<String> words, int left, int right) {
    const vowels = {'a', 'e', 'i', 'o', 'u'};
    int count = 0;
    for (int i = left; i <= right; i++) {
      String w = words[i];
      if (vowels.contains(w[0]) && vowels.contains(w[w.length - 1])) {
        count++;
      }
    }
    return count;
  }
}
```

## Golang

```go
func vowelStrings(words []string, left int, right int) int {
    count := 0
    for i := left; i <= right && i < len(words); i++ {
        w := words[i]
        if len(w) == 0 {
            continue
        }
        first := w[0]
        last := w[len(w)-1]
        if isVowel(first) && isVowel(last) {
            count++
        }
    }
    return count
}

func isVowel(c byte) bool {
    switch c {
    case 'a', 'e', 'i', 'o', 'u':
        return true
    }
    return false
}
```

## Ruby

```ruby
# @param {String[]} words
# @param {Integer} left
# @param {Integer} right
# @return {Integer}
def vowel_strings(words, left, right)
  vowels = {'a'=>true,'e'=>true,'i'=>true,'o'=>true,'u'=>true}
  count = 0
  (left..right).each do |i|
    w = words[i]
    if vowels[w[0]] && vowels[w[-1]]
      count += 1
    end
  end
  count
end
```

## Scala

```scala
object Solution {
    def vowelStrings(words: Array[String], left: Int, right: Int): Int = {
        val vowels = Set('a', 'e', 'i', 'o', 'u')
        var count = 0
        for (i <- left to right) {
            val w = words(i)
            if (vowels.contains(w.head) && vowels.contains(w.last)) {
                count += 1
            }
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn vowel_strings(words: Vec<String>, left: i32, right: i32) -> i32 {
        let vowels = [b'a', b'e', b'i', b'o', b'u'];
        let mut cnt = 0;
        for idx in left as usize..=right as usize {
            let w = &words[idx];
            let bytes = w.as_bytes();
            let first = bytes[0];
            let last = bytes[bytes.len() - 1];
            if vowels.contains(&first) && vowels.contains(&last) {
                cnt += 1;
            }
        }
        cnt as i32
    }
}
```

## Racket

```racket
(define/contract (vowel-strings words left right)
  (-> (listof string?) exact-integer? exact-integer? exact-integer?)
  (let* ([vowels (list #\a #\e #\i #\o #\u)]
         [is-vowel?
          (lambda (s)
            (and (member (string-ref s 0) vowels)
                 (member (string-ref s (sub1 (string-length s))) vowels)))])
    (for/sum ([i (in-range left (add1 right))])
      (if (is-vowel? (list-ref words i)) 1 0))))
```

## Erlang

```erlang
-spec vowel_strings(Words :: [unicode:unicode_binary()], Left :: integer(), Right :: integer()) -> integer().
vowel_strings(Words, Left, Right) ->
    vowel_strings(Words, Left, Right, 0).

%% Recursive helper iterating from index Left to Right (inclusive)
-spec vowel_strings([unicode:unicode_binary()], integer(), integer(), integer()) -> integer().
vowel_strings(_Words, L, R, Count) when L > R ->
    Count;
vowel_strings(Words, L, R, Count) ->
    Bin = lists:nth(L + 1, Words), % Erlang lists are 1‑based
    NewCount = case is_vowel_string(Bin) of
        true -> Count + 1;
        false -> Count
    end,
    vowel_strings(Words, L + 1, R, NewCount).

%% Checks whether a binary starts and ends with a vowel character.
-spec is_vowel_string(unicode:unicode_binary()) -> boolean().
is_vowel_string(Bin) ->
    First = binary:first(Bin),
    Last  = binary:last(Bin),
    Vowels = [$a, $e, $i, $o, $u],
    lists:member(First, Vowels) andalso lists:member(Last, Vowels).
```

## Elixir

```elixir
defmodule Solution do
  @spec vowel_strings(words :: [String.t()], left :: integer, right :: integer) :: integer
  def vowel_strings(words, left, right) do
    Enum.reduce(left..right, 0, fn i, acc ->
      word = Enum.at(words, i)

      if vowel_string?(word), do: acc + 1, else: acc
    end)
  end

  defp vowel_string?(word) do
    first = String.at(word, 0)
    last = String.at(word, -1)

    case {first, last} do
      {f, l} when not is_nil(f) and not is_nil(l) ->
        vowel_char?(f) and vowel_char?(l)

      _ ->
        false
    end
  end

  defp vowel_char?(c) when c in ["a", "e", "i", "o", "u"], do: true
  defp vowel_char?(_), do: false
end
```
