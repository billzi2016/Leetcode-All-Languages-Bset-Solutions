# 2788. Split Strings by Separator

## Cpp

```cpp
class Solution {
public:
    vector<string> splitWordsBySeparator(vector<string>& words, char separator) {
        vector<string> result;
        for (const string& word : words) {
            string cur;
            for (char ch : word) {
                if (ch == separator) {
                    if (!cur.empty()) {
                        result.push_back(cur);
                        cur.clear();
                    }
                } else {
                    cur.push_back(ch);
                }
            }
            if (!cur.empty())
                result.push_back(cur);
        }
        return result;
    }
};
```

## Java

```java
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Pattern;

class Solution {
    public List<String> splitWordsBySeparator(List<String> words, char separator) {
        List<String> result = new ArrayList<>();
        String sepPattern = Pattern.quote(String.valueOf(separator));
        for (String word : words) {
            String[] parts = word.split(sepPattern, -1);
            for (String part : parts) {
                if (!part.isEmpty()) {
                    result.add(part);
                }
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """
        result = []
        for word in words:
            for part in word.split(separator):
                if part:
                    result.append(part)
        return result
```

## Python3

```python
from typing import List

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []
        for word in words:
            for part in word.split(separator):
                if part:
                    result.append(part)
        return result
```

## C

```c
#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** splitWordsBySeparator(char** words, int wordsSize, char separator, int* returnSize) {
    int total = 0;
    for (int i = 0; i < wordsSize; ++i) {
        const char *s = words[i];
        int len = 0;
        while (*s) {
            if (*s == separator) {
                if (len > 0) {
                    ++total;
                    len = 0;
                }
            } else {
                ++len;
            }
            ++s;
        }
        if (len > 0) ++total;
    }

    *returnSize = total;
    if (total == 0) return NULL;

    char **result = (char **)malloc(total * sizeof(char *));
    int idx = 0;

    for (int i = 0; i < wordsSize; ++i) {
        const char *s = words[i];
        int start = 0;
        int pos = 0;
        while (1) {
            if (s[pos] == separator || s[pos] == '\0') {
                int sublen = pos - start;
                if (sublen > 0) {
                    char *sub = (char *)malloc(sublen + 1);
                    memcpy(sub, s + start, sublen);
                    sub[sublen] = '\0';
                    result[idx++] = sub;
                }
                start = pos + 1;
            }
            if (s[pos] == '\0') break;
            ++pos;
        }
    }

    return result;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<string> SplitWordsBySeparator(IList<string> words, char separator) {
        var result = new List<string>();
        foreach (var word in words) {
            var parts = word.Split(separator);
            foreach (var part in parts) {
                if (!string.IsNullOrEmpty(part)) {
                    result.Add(part);
                }
            }
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @param {character} separator
 * @return {string[]}
 */
var splitWordsBySeparator = function(words, separator) {
    const result = [];
    for (const word of words) {
        const parts = word.split(separator);
        for (const part of parts) {
            if (part.length > 0) {
                result.push(part);
            }
        }
    }
    return result;
};
```

## Typescript

```typescript
function splitWordsBySeparator(words: string[], separator: string): string[] {
    const result: string[] = [];
    for (const w of words) {
        const parts = w.split(separator);
        for (const p of parts) {
            if (p.length > 0) {
                result.push(p);
            }
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $words
     * @param String $separator
     * @return String[]
     */
    function splitWordsBySeparator($words, $separator) {
        $result = [];
        foreach ($words as $word) {
            $parts = explode($separator, $word);
            foreach ($parts as $part) {
                if ($part !== '') {
                    $result[] = $part;
                }
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func splitWordsBySeparator(_ words: [String], _ separator: Character) -> [String] {
        var result = [String]()
        for word in words {
            let parts = word.split(separator: separator, omittingEmptySubsequences: true)
            for part in parts {
                result.append(String(part))
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun splitWordsBySeparator(words: List<String>, separator: Char): List<String> {
        val result = mutableListOf<String>()
        for (word in words) {
            for (part in word.split(separator)) {
                if (part.isNotEmpty()) {
                    result.add(part)
                }
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<String> splitWordsBySeparator(List<String> words, String separator) {
    List<String> result = [];
    for (var word in words) {
      var parts = word.split(separator);
      for (var part in parts) {
        if (part.isNotEmpty) {
          result.add(part);
        }
      }
    }
    return result;
  }
}
```

## Golang

```go
package main

import "strings"

func splitWordsBySeparator(words []string, separator byte) []string {
	var result []string
	sep := string(separator)
	for _, w := range words {
		parts := strings.Split(w, sep)
		for _, p := range parts {
			if p != "" {
				result = append(result, p)
			}
		}
	}
	return result
}
```

## Ruby

```ruby
def split_words_by_separator(words, separator)
  result = []
  words.each do |word|
    word.split(separator).each do |segment|
      result << segment unless segment.empty?
    end
  end
  result
end
```

## Scala

```scala
import java.util.regex.Pattern

object Solution {
  def splitWordsBySeparator(words: List[String], separator: Char): List[String] = {
    val sepPattern = Pattern.quote(separator.toString)
    words.flatMap(_.split(sepPattern).filter(_.nonEmpty))
  }
}
```

## Rust

```rust
impl Solution {
    pub fn split_words_by_separator(words: Vec<String>, separator: char) -> Vec<String> {
        let mut result = Vec::new();
        for w in words.iter() {
            for part in w.split(separator) {
                if !part.is_empty() {
                    result.push(part.to_string());
                }
            }
        }
        result
    }
}
```

## Racket

```racket
(require racket/string)

(define/contract (split-words-by-separator words separator)
  (-> (listof string?) char? (listof string?))
  (let ([sep (string separator)])
    (apply append
           (map (lambda (w) (string-split w sep #:omit-empty? #t)) words))))
```

## Erlang

```erlang
-spec split_words_by_separator(Words :: [unicode:unicode_binary()], Separator :: char()) -> [unicode:unicode_binary()].
split_words_by_separator(Words, Separator) ->
    SepBin = <<Separator>>,
    [Part || Word <- Words,
             Part <- binary:split(Word, SepBin, [global, trim_all])].
```

## Elixir

```elixir
defmodule Solution do
  @spec split_words_by_separator(words :: [String.t()], separator :: char) :: [String.t()]
  def split_words_by_separator(words, separator) do
    sep = <<separator>>
    Enum.flat_map(words, fn word -> String.split(word, sep, trim: true) end)
  end
end
```
