# 2114. Maximum Number of Words Found in Sentences

## Cpp

```cpp
class Solution {
public:
    int mostWordsFound(std::vector<std::string>& sentences) {
        int maxWords = 0;
        for (const auto& s : sentences) {
            // Number of words is number of spaces + 1
            int words = std::count(s.begin(), s.end(), ' ') + 1;
            if (words > maxWords) maxWords = words;
        }
        return maxWords;
    }
};
```

## Java

```java
class Solution {
    public int mostWordsFound(String[] sentences) {
        int max = 0;
        for (String s : sentences) {
            int count = 1; // at least one word
            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i) == ' ') {
                    count++;
                }
            }
            if (count > max) {
                max = count;
            }
        }
        return max;
    }
}
```

## Python

```python
class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max_words = 0
        for s in sentences:
            # Number of words is number of spaces + 1
            count = s.count(' ') + 1
            if count > max_words:
                max_words = count
        return max_words
```

## Python3

```python
from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_count = 0
        for s in sentences:
            count = s.count(' ') + 1
            if count > max_count:
                max_count = count
        return max_count
```

## C

```c
int mostWordsFound(char** sentences, int sentencesSize) {
    int maxWords = 0;
    for (int i = 0; i < sentencesSize; ++i) {
        const char *p = sentences[i];
        int count = 1; // at least one word per sentence
        while (*p) {
            if (*p == ' ') ++count;
            ++p;
        }
        if (count > maxWords) maxWords = count;
    }
    return maxWords;
}
```

## Csharp

```csharp
public class Solution {
    public int MostWordsFound(string[] sentences) {
        int maxWords = 0;
        foreach (var sentence in sentences) {
            int count = 1; // at least one word
            foreach (char ch in sentence) {
                if (ch == ' ') count++;
            }
            if (count > maxWords) maxWords = count;
        }
        return maxWords;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} sentences
 * @return {number}
 */
var mostWordsFound = function(sentences) {
    let max = 0;
    for (const s of sentences) {
        let count = 1; // at least one word per sentence
        for (let i = 0; i < s.length; i++) {
            if (s[i] === ' ') count++;
        }
        if (count > max) max = count;
    }
    return max;
};
```

## Typescript

```typescript
function mostWordsFound(sentences: string[]): number {
    let max = 0;
    for (const s of sentences) {
        const words = s.split(' ').length;
        if (words > max) max = words;
    }
    return max;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $sentences
     * @return Integer
     */
    function mostWordsFound($sentences) {
        $max = 0;
        foreach ($sentences as $s) {
            // Number of words is number of spaces + 1
            $count = substr_count($s, ' ') + 1;
            if ($count > $max) {
                $max = $count;
            }
        }
        return $max;
    }
}
```

## Swift

```swift
class Solution {
    func mostWordsFound(_ sentences: [String]) -> Int {
        var maxCount = 0
        for sentence in sentences {
            let wordCount = sentence.split(separator: " ").count
            if wordCount > maxCount {
                maxCount = wordCount
            }
        }
        return maxCount
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun mostWordsFound(sentences: Array<String>): Int {
        var maxWords = 0
        for (sentence in sentences) {
            var count = 1
            for (ch in sentence) {
                if (ch == ' ') count++
            }
            if (count > maxWords) maxWords = count
        }
        return maxWords
    }
}
```

## Dart

```dart
class Solution {
  int mostWordsFound(List<String> sentences) {
    int maxCount = 0;
    for (var s in sentences) {
      // Number of words is number of spaces + 1
      int count = 1; // at least one word
      for (int i = 0; i < s.length; i++) {
        if (s[i] == ' ') count++;
      }
      if (count > maxCount) maxCount = count;
    }
    return maxCount;
  }
}
```

## Golang

```go
func mostWordsFound(sentences []string) int {
    maxCount := 0
    for _, s := range sentences {
        count := 1 // at least one word if the string is non‑empty
        for i := 0; i < len(s); i++ {
            if s[i] == ' ' {
                count++
            }
        }
        if count > maxCount {
            maxCount = count
        }
    }
    return maxCount
}
```

## Ruby

```ruby
def most_words_found(sentences)
  max = 0
  sentences.each do |s|
    words = s.count(' ') + 1
    max = words if words > max
  end
  max
end
```

## Scala

```scala
object Solution {
    def mostWordsFound(sentences: Array[String]): Int = {
        var maxCount = 0
        for (s <- sentences) {
            // Number of words is number of spaces + 1
            val count = s.count(_ == ' ') + 1
            if (count > maxCount) maxCount = count
        }
        maxCount
    }
}
```

## Rust

```rust
impl Solution {
    pub fn most_words_found(sentences: Vec<String>) -> i32 {
        let mut max_words = 0usize;
        for sentence in sentences {
            let count = sentence.split(' ').count();
            if count > max_words {
                max_words = count;
            }
        }
        max_words as i32
    }
}
```

## Racket

```racket
(define/contract (most-words-found sentences)
  (-> (listof string?) exact-integer?)
  (let loop ((lst sentences) (max 0))
    (if (null? lst)
        max
        (let* ([s (car lst)]
               [spaces (for/sum ([c (in-string s)]) (if (char=? c #\space) 1 0))]
               [words (+ spaces 1)])
          (loop (cdr lst) (max words max))))))
```

## Erlang

```erlang
-spec most_words_found(Sentences :: [unicode:unicode_binary()]) -> integer().
most_words_found(Sentences) ->
    lists:max([length(binary:split(S, <<" ">>, [global])) || S <- Sentences]).
```

## Elixir

```elixir
defmodule Solution do
  @spec most_words_found(sentences :: [String.t]) :: integer
  def most_words_found(sentences) do
    sentences
    |> Enum.map(&String.split(&1, " ") |> length)
    |> Enum.max()
  end
end
```
