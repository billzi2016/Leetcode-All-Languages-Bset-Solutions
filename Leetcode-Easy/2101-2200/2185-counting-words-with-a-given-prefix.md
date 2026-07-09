# 2185. Counting Words With a Given Prefix

## Cpp

```cpp
class Solution {
public:
    int prefixCount(std::vector<std::string>& words, std::string pref) {
        int count = 0;
        for (const auto& w : words) {
            if (w.size() >= pref.size() && w.compare(0, pref.size(), pref) == 0) {
                ++count;
            }
        }
        return count;
    }
};
```

## Java

```java
class Solution {
    public int prefixCount(String[] words, String pref) {
        int count = 0;
        for (String word : words) {
            if (word.startsWith(pref)) {
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
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        count = 0
        for w in words:
            if w.startswith(pref):
                count += 1
        return count
```

## Python3

```python
from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(1 for word in words if word.startswith(pref))
```

## C

```c
#include <string.h>

int prefixCount(char** words, int wordsSize, char* pref) {
    int count = 0;
    size_t prefLen = strlen(pref);
    for (int i = 0; i < wordsSize; ++i) {
        if (strncmp(words[i], pref, prefLen) == 0) {
            ++count;
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int PrefixCount(string[] words, string pref) {
        int count = 0;
        foreach (var word in words) {
            if (word.StartsWith(pref)) {
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
 * @param {string} pref
 * @return {number}
 */
var prefixCount = function(words, pref) {
    let count = 0;
    for (const w of words) {
        if (w.startsWith(pref)) count++;
    }
    return count;
};
```

## Typescript

```typescript
function prefixCount(words: string[], pref: string): number {
    let count = 0;
    for (const w of words) {
        if (w.startsWith(pref)) count++;
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $words
     * @param String $pref
     * @return Integer
     */
    function prefixCount($words, $pref) {
        $count = 0;
        $lenPref = strlen($pref);
        foreach ($words as $word) {
            if (substr($word, 0, $lenPref) === $pref) {
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
    func prefixCount(_ words: [String], _ pref: String) -> Int {
        var count = 0
        for word in words {
            if word.hasPrefix(pref) {
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
    fun prefixCount(words: Array<String>, pref: String): Int {
        var count = 0
        for (word in words) {
            if (word.startsWith(pref)) {
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
  int prefixCount(List<String> words, String pref) {
    int count = 0;
    for (var word in words) {
      if (word.startsWith(pref)) {
        count++;
      }
    }
    return count;
  }
}
```

## Golang

```go
func prefixCount(words []string, pref string) int {
	count := 0
	for _, w := range words {
		if len(w) >= len(pref) && w[:len(pref)] == pref {
			count++
		}
	}
	return count
}
```

## Ruby

```ruby
def prefix_count(words, pref)
  count = 0
  words.each do |word|
    count += 1 if word.start_with?(pref)
  end
  count
end
```

## Scala

```scala
object Solution {
    def prefixCount(words: Array[String], pref: String): Int = {
        var count = 0
        for (word <- words) {
            if (word.startsWith(pref)) count += 1
        }
        count
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn prefix_count(words: Vec<String>, pref: String) -> i32 {
        let mut count = 0;
        for w in words.iter() {
            if w.starts_with(&pref) {
                count += 1;
            }
        }
        count as i32
    }
}
```

## Racket

```racket
(require racket/string)

(define/contract (prefix-count words pref)
  (-> (listof string?) string? exact-integer?)
  (let loop ((ws words) (cnt 0))
    (if (null? ws)
        cnt
        (loop (cdr ws)
              (if (string-prefix? (car ws) pref)
                  (+ cnt 1)
                  cnt)))))
```

## Erlang

```erlang
-spec prefix_count(Words :: [unicode:unicode_binary()], Pref :: unicode:unicode_binary()) -> integer().
prefix_count(Words, Pref) ->
    PrefLen = byte_size(Pref),
    CountFun = fun(Word, Acc) ->
        case {byte_size(Word) >= PrefLen, binary:match(Word, Pref)} of
            {true, {0, PrefLen}} -> Acc + 1;
            _ -> Acc
        end
    end,
    lists:foldl(CountFun, 0, Words).
```

## Elixir

```elixir
defmodule Solution do
  @spec prefix_count(words :: [String.t()], pref :: String.t()) :: integer()
  def prefix_count(words, pref) do
    Enum.count(words, fn word -> String.starts_with?(word, pref) end)
  end
end
```
