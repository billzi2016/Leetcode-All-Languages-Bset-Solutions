# 2255. Count Prefixes of a Given String

## Cpp

```cpp
class Solution {
public:
    int countPrefixes(vector<string>& words, string s) {
        int ans = 0;
        for (const auto& w : words) {
            if (w.size() <= s.size() && s.compare(0, w.size(), w) == 0) {
                ++ans;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int countPrefixes(String[] words, String s) {
        int count = 0;
        for (String w : words) {
            if (s.startsWith(w)) {
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
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        cnt = 0
        for w in words:
            if s.startswith(w):
                cnt += 1
        return cnt
```

## Python3

```python
from typing import List

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        for w in words:
            if s.startswith(w):
                count += 1
        return count
```

## C

```c
#include <stddef.h>

int countPrefixes(char** words, int wordsSize, char* s) {
    int count = 0;
    for (int i = 0; i < wordsSize; ++i) {
        char *w = words[i];
        int j = 0;
        while (w[j] && s[j] && w[j] == s[j]) {
            ++j;
        }
        if (w[j] == '\0') {
            ++count;
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int CountPrefixes(string[] words, string s) {
        int count = 0;
        foreach (var w in words) {
            if (s.StartsWith(w)) count++;
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @param {string} s
 * @return {number}
 */
var countPrefixes = function(words, s) {
    let count = 0;
    for (const w of words) {
        if (s.startsWith(w)) count++;
    }
    return count;
};
```

## Typescript

```typescript
function countPrefixes(words: string[], s: string): number {
    let count = 0;
    for (const w of words) {
        if (s.startsWith(w)) {
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
     * @param String $s
     * @return Integer
     */
    function countPrefixes($words, $s) {
        $count = 0;
        foreach ($words as $w) {
            if (strncmp($s, $w, strlen($w)) === 0) {
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
    func countPrefixes(_ words: [String], _ s: String) -> Int {
        var count = 0
        for word in words {
            if s.hasPrefix(word) {
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
    fun countPrefixes(words: Array<String>, s: String): Int {
        var count = 0
        for (word in words) {
            if (s.startsWith(word)) {
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
  int countPrefixes(List<String> words, String s) {
    int count = 0;
    for (var word in words) {
      if (s.startsWith(word)) {
        count++;
      }
    }
    return count;
  }
}
```

## Golang

```go
func countPrefixes(words []string, s string) int {
    count := 0
    for _, w := range words {
        if len(w) <= len(s) && s[:len(w)] == w {
            count++
        }
    }
    return count
}
```

## Ruby

```ruby
def count_prefixes(words, s)
  count = 0
  words.each { |word| count += 1 if s.start_with?(word) }
  count
end
```

## Scala

```scala
object Solution {
    def countPrefixes(words: Array[String], s: String): Int = {
        var count = 0
        for (w <- words) {
            if (s.startsWith(w)) count += 1
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_prefixes(words: Vec<String>, s: String) -> i32 {
        let mut count = 0;
        for w in &words {
            if s.starts_with(w) {
                count += 1;
            }
        }
        count
    }
}
```

## Racket

```racket
#lang racket
(require racket/string)

(define/contract (count-prefixes words s)
  (-> (listof string?) string? exact-integer?)
  (let loop ((lst words) (cnt 0))
    (cond [(null? lst) cnt]
          [else (loop (cdr lst)
                      (+ cnt (if (string-prefix? (car lst) s) 1 0)))])))
```

## Erlang

```erlang
-spec count_prefixes(Words :: [unicode:unicode_binary()], S :: unicode:unicode_binary()) -> integer().
count_prefixes(Words, S) ->
    LenS = byte_size(S),
    lists:foldl(
        fun(W, Acc) ->
            LenW = byte_size(W),
            if
                LenW =< LenS,
                binary:part(S, 0, LenW) =:= W -> Acc + 1;
                true -> Acc
            end
        end,
        0,
        Words
    ).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_prefixes(words :: [String.t()], s :: String.t()) :: integer()
  def count_prefixes(words, s) do
    Enum.count(words, fn w -> String.starts_with?(s, w) end)
  end
end
```
