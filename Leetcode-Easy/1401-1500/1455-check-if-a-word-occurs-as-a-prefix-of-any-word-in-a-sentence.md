# 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int isPrefixOfWord(string sentence, string searchWord) {
        stringstream ss(sentence);
        string word;
        int index = 1;
        while (ss >> word) {
            if (word.size() >= searchWord.size() && word.compare(0, searchWord.size(), searchWord) == 0)
                return index;
            ++index;
        }
        return -1;
    }
};
```

## Java

```java
class Solution {
    public int isPrefixOfWord(String sentence, String searchWord) {
        String[] words = sentence.split(" ");
        for (int i = 0; i < words.length; i++) {
            if (words[i].startsWith(searchWord)) {
                return i + 1;
            }
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        for idx, word in enumerate(sentence.split()):
            if word.startswith(searchWord):
                return idx + 1
        return -1
```

## Python3

```python
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, word in enumerate(sentence.split(), 1):
            if word.startswith(searchWord):
                return i
        return -1
```

## C

```c
int isPrefixOfWord(char* sentence, char* searchWord) {
    int index = 1;
    char *ptr = sentence;
    while (*ptr) {
        while (*ptr && *ptr == ' ') ptr++;          // skip spaces
        if (!*ptr) break;                           // end of string

        char *s = ptr;
        char *w = searchWord;
        while (*w && *s && *w == *s) {              // compare characters
            w++;
            s++;
        }
        if (*w == '\0') return index;               // full match found

        while (*ptr && *ptr != ' ') ptr++;          // move to next word
        index++;
    }
    return -1;
}
```

## Csharp

```csharp
public class Solution
{
    public int IsPrefixOfWord(string sentence, string searchWord)
    {
        var words = sentence.Split(' ');
        for (int i = 0; i < words.Length; i++)
        {
            if (words[i].StartsWith(searchWord))
                return i + 1;
        }
        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} sentence
 * @param {string} searchWord
 * @return {number}
 */
var isPrefixOfWord = function(sentence, searchWord) {
    const words = sentence.split(' ');
    for (let i = 0; i < words.length; i++) {
        if (words[i].startsWith(searchWord)) {
            return i + 1;
        }
    }
    return -1;
};
```

## Typescript

```typescript
function isPrefixOfWord(sentence: string, searchWord: string): number {
    const words = sentence.split(' ');
    for (let i = 0; i < words.length; i++) {
        if (words[i].startsWith(searchWord)) {
            return i + 1;
        }
    }
    return -1;
}
```

## Php

```php
class Solution {

    /**
     * @param String $sentence
     * @param String $searchWord
     * @return Integer
     */
    function isPrefixOfWord($sentence, $searchWord) {
        $words = explode(' ', $sentence);
        foreach ($words as $idx => $word) {
            if (strpos($word, $searchWord) === 0) {
                return $idx + 1;
            }
        }
        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func isPrefixOfWord(_ sentence: String, _ searchWord: String) -> Int {
        var idx = 1
        for word in sentence.split(separator: " ") {
            if word.hasPrefix(searchWord) {
                return idx
            }
            idx += 1
        }
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isPrefixOfWord(sentence: String, searchWord: String): Int {
        var index = 1
        for (word in sentence.split(" ")) {
            if (word.startsWith(searchWord)) return index
            index++
        }
        return -1
    }
}
```

## Dart

```dart
class Solution {
  int isPrefixOfWord(String sentence, String searchWord) {
    List<String> words = sentence.split(' ');
    for (int i = 0; i < words.length; i++) {
      if (words[i].startsWith(searchWord)) {
        return i + 1;
      }
    }
    return -1;
  }
}
```

## Golang

```go
import "strings"

func isPrefixOfWord(sentence string, searchWord string) int {
	words := strings.Split(sentence, " ")
	for i, w := range words {
		if len(w) >= len(searchWord) && strings.HasPrefix(w, searchWord) {
			return i + 1
		}
	}
	return -1
}
```

## Ruby

```ruby
# @param {String} sentence
# @param {String} search_word
# @return {Integer}
def is_prefix_of_word(sentence, search_word)
  words = sentence.split(' ')
  words.each_with_index do |word, idx|
    return idx + 1 if word.start_with?(search_word)
  end
  -1
end
```

## Scala

```scala
object Solution {
    def isPrefixOfWord(sentence: String, searchWord: String): Int = {
        val words = sentence.split(" ")
        for (i <- words.indices) {
            if (words(i).startsWith(searchWord)) return i + 1
        }
        -1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_prefix_of_word(sentence: String, search_word: String) -> i32 {
        for (i, word) in sentence.split(' ').enumerate() {
            if word.starts_with(&search_word) {
                return (i as i32) + 1;
            }
        }
        -1
    }
}
```

## Racket

```racket
(require racket/string)

(define/contract (is-prefix-of-word sentence searchWord)
  (-> string? string? exact-integer?)
  (let loop ((words (string-split sentence " "))
             (idx   1))
    (cond
      [(null? words) -1]
      [(string-prefix? searchWord (car words)) idx]
      [else (loop (cdr words) (+ idx 1))])))
```

## Erlang

```erlang
-spec is_prefix_of_word(Sentence :: unicode:unicode_binary(), SearchWord :: unicode:unicode_binary()) -> integer().
is_prefix_of_word(Sentence, SearchWord) ->
    Words = binary:split(Sentence, <<" ">>, [global]),
    find(Words, SearchWord, 1).

find([], _SearchWord, _Idx) -> -1;
find([W|Rest], SearchWord, Idx) ->
    case W of
        <<SearchWord/binary, _/binary>> -> Idx;
        _ -> find(Rest, SearchWord, Idx + 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_prefix_of_word(sentence :: String.t(), search_word :: String.t()) :: integer()
  def is_prefix_of_word(sentence, search_word) do
    sentence
    |> String.split(" ")
    |> Enum.with_index(1)
    |> Enum.find(fn {word, _idx} -> String.starts_with?(word, search_word) end)
    |> case do
      nil -> -1
      {_word, idx} -> idx
    end
  end
end
```
