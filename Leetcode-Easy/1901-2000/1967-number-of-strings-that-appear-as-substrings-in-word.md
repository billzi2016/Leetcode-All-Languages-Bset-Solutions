# 1967. Number of Strings That Appear as Substrings in Word

## Cpp

```cpp
class Solution {
public:
    int numOfStrings(vector<string>& patterns, string word) {
        int cnt = 0;
        for (const auto& p : patterns) {
            if (word.find(p) != string::npos) ++cnt;
        }
        return cnt;
    }
};
```

## Java

```java
class Solution {
    public int numOfStrings(String[] patterns, String word) {
        int count = 0;
        for (String p : patterns) {
            if (word.contains(p)) {
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
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        count = 0
        for p in patterns:
            if p in word:
                count += 1
        return count
```

## Python3

```python
from typing import List

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(p in word for p in patterns)
```

## C

```c
#include <string.h>

int numOfStrings(char** patterns, int patternsSize, char* word) {
    int count = 0;
    for (int i = 0; i < patternsSize; ++i) {
        if (strstr(word, patterns[i]) != NULL) {
            ++count;
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int NumOfStrings(string[] patterns, string word) {
        int count = 0;
        foreach (var p in patterns) {
            if (word.Contains(p)) {
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
 * @param {string[]} patterns
 * @param {string} word
 * @return {number}
 */
var numOfStrings = function(patterns, word) {
    let count = 0;
    for (const p of patterns) {
        if (word.includes(p)) count++;
    }
    return count;
};
```

## Typescript

```typescript
function numOfStrings(patterns: string[], word: string): number {
    let count = 0;
    for (const p of patterns) {
        if (word.includes(p)) {
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
     * @param String[] $patterns
     * @param String $word
     * @return Integer
     */
    function numOfStrings($patterns, $word) {
        $count = 0;
        foreach ($patterns as $p) {
            if (strpos($word, $p) !== false) {
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
    func numOfStrings(_ patterns: [String], _ word: String) -> Int {
        var count = 0
        for pattern in patterns {
            if word.contains(pattern) {
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
    fun numOfStrings(patterns: Array<String>, word: String): Int {
        var count = 0
        for (p in patterns) {
            if (word.contains(p)) count++
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int numOfStrings(List<String> patterns, String word) {
    int count = 0;
    for (var p in patterns) {
      if (word.contains(p)) {
        count++;
      }
    }
    return count;
  }
}
```

## Golang

```go
package main

import "strings"

func numOfStrings(patterns []string, word string) int {
	count := 0
	for _, p := range patterns {
		if strings.Contains(word, p) {
			count++
		}
	}
	return count
}
```

## Ruby

```ruby
# @param {String[]} patterns
# @param {String} word
# @return {Integer}
def num_of_strings(patterns, word)
  count = 0
  patterns.each do |p|
    count += 1 if word.include?(p)
  end
  count
end
```

## Scala

```scala
object Solution {
    def numOfStrings(patterns: Array[String], word: String): Int = {
        var count = 0
        for (p <- patterns) {
            if (word.contains(p)) count += 1
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_of_strings(patterns: Vec<String>, word: String) -> i32 {
        let mut count = 0;
        for p in patterns.iter() {
            if word.contains(p) {
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

(define/contract (num-of-strings patterns word)
  (-> (listof string?) string? exact-integer?)
  (let loop ((lst patterns) (cnt 0))
    (if (null? lst)
        cnt
        (loop (cdr lst)
              (+ cnt (if (string-contains? word (car lst)) 1 0))))))
```

## Erlang

```erlang
-spec num_of_strings(Patterns :: [unicode:unicode_binary()], Word :: unicode:unicode_binary()) -> integer().
num_of_strings(Patterns, Word) ->
    lists:foldl(
        fun(Pat, Acc) ->
            case binary:match(Word, Pat) of
                {_, _} -> Acc + 1;
                nomatch -> Acc
            end
        end,
        0,
        Patterns
    ).
```

## Elixir

```elixir
defmodule Solution do
  @spec num_of_strings(patterns :: [String.t()], word :: String.t()) :: integer()
  def num_of_strings(patterns, word) do
    Enum.count(patterns, fn pattern -> String.contains?(word, pattern) end)
  end
end
```
