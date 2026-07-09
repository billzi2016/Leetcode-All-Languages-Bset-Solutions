# 1408. String Matching in an Array

## Cpp

```cpp
class Solution {
public:
    vector<string> stringMatching(vector<string>& words) {
        vector<string> result;
        int n = words.size();
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i == j) continue;
                if (words[j].find(words[i]) != string::npos) {
                    result.push_back(words[i]);
                    break;
                }
            }
        }
        return result;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<String> stringMatching(String[] words) {
        List<String> result = new ArrayList<>();
        for (int i = 0; i < words.length; i++) {
            for (int j = 0; j < words.length; j++) {
                if (i == j) continue;
                if (words[j].contains(words[i])) {
                    result.add(words[i]);
                    break;
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
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        for i, w in enumerate(words):
            for j, other in enumerate(words):
                if i != j and w in other:
                    result.append(w)
                    break
        return result
```

## Python3

```python
from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for i, w in enumerate(words):
            for j, other in enumerate(words):
                if i != j and w in other:
                    result.append(w)
                    break
        return result
```

## C

```c
#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** stringMatching(char** words, int wordsSize, int* returnSize) {
    char **result = (char **)malloc(wordsSize * sizeof(char *));
    int count = 0;
    
    for (int i = 0; i < wordsSize; ++i) {
        for (int j = 0; j < wordsSize; ++j) {
            if (i == j) continue;
            if (strstr(words[j], words[i]) != NULL) {
                result[count++] = words[i];
                break;
            }
        }
    }
    
    *returnSize = count;
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public IList<string> StringMatching(string[] words)
    {
        var result = new List<string>();
        int n = words.Length;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (i == j) continue;
                if (words[j].Contains(words[i]))
                {
                    result.Add(words[i]);
                    break;
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
 * @return {string[]}
 */
var stringMatching = function(words) {
    const result = [];
    for (let i = 0; i < words.length; i++) {
        for (let j = 0; j < words.length; j++) {
            if (i !== j && words[j].includes(words[i])) {
                result.push(words[i]);
                break;
            }
        }
    }
    return result;
};
```

## Typescript

```typescript
function stringMatching(words: string[]): string[] {
    const result: string[] = [];
    const n = words.length;
    for (let i = 0; i < n; i++) {
        const sub = words[i];
        for (let j = 0; j < n; j++) {
            if (i === j) continue;
            if (words[j].includes(sub)) {
                result.push(sub);
                break;
            }
        }
    }
    return result;
}
```

## Php

```php
<?php
class Solution {
    /**
     * @param String[] $words
     * @return String[]
     */
    function stringMatching($words) {
        $n = count($words);
        $result = [];
        for ($i = 0; $i < $n; $i++) {
            $sub = $words[$i];
            for ($j = 0; $j < $n; $j++) {
                if ($i === $j) continue;
                if (strpos($words[$j], $sub) !== false) {
                    $result[] = $sub;
                    break;
                }
            }
        }
        return $result;
    }
}
?>
```

## Swift

```swift
class Solution {
    func stringMatching(_ words: [String]) -> [String] {
        var result = [String]()
        for i in 0..<words.count {
            let w = words[i]
            for j in 0..<words.count where i != j {
                if words[j].contains(w) {
                    result.append(w)
                    break
                }
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun stringMatching(words: Array<String>): List<String> {
        val result = mutableListOf<String>()
        for (i in words.indices) {
            for (j in words.indices) {
                if (i != j && words[j].contains(words[i])) {
                    result.add(words[i])
                    break
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
  List<String> stringMatching(List<String> words) {
    List<String> result = [];
    int n = words.length;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        if (i == j) continue;
        if (words[j].contains(words[i])) {
          result.add(words[i]);
          break;
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

func stringMatching(words []string) []string {
	var res []string
	n := len(words)
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if i == j {
				continue
			}
			if strings.Contains(words[j], words[i]) {
				res = append(res, words[i])
				break
			}
		}
	}
	return res
}
```

## Ruby

```ruby
def string_matching(words)
  result = []
  words.each_with_index do |word, i|
    words.each_with_index do |other, j|
      next if i == j
      if other.include?(word)
        result << word
        break
      end
    end
  end
  result
end
```

## Scala

```scala
object Solution {
  def stringMatching(words: Array[String]): List[String] = {
    val result = scala.collection.mutable.ListBuffer[String]()
    for (i <- words.indices) {
      var added = false
      for (j <- words.indices if i != j && !added) {
        if (words(j).contains(words(i))) {
          result += words(i)
          added = true
        }
      }
    }
    result.toList
  }
}
```

## Rust

```rust
impl Solution {
    pub fn string_matching(words: Vec<String>) -> Vec<String> {
        let mut result = Vec::new();
        for i in 0..words.len() {
            for j in 0..words.len() {
                if i != j && words[j].contains(&words[i]) {
                    result.push(words[i].clone());
                    break;
                }
            }
        }
        result
    }
}
```

## Racket

```racket
#lang racket
(require racket/string)

(define/contract (string-matching words)
  (-> (listof string?) (listof string?))
  (filter
   (lambda (w)
     (ormap (lambda (other)
              (and (not (string=? w other))
                   (string-contains? other w)))
            words))
   words))
```

## Erlang

```erlang
-spec string_matching([unicode:unicode_binary()]) -> [unicode:unicode_binary()].
string_matching(Words) ->
    lists:foldl(fun(Word, Acc) ->
        case is_substring(Word, Words) of
            true -> [Word | Acc];
            false -> Acc
        end
    end, [], Words).

is_substring(Word, Words) ->
    lists:any(fun(Other) ->
        Word =/= Other andalso binary:match(Other, Word) =/= nomatch
    end, Words).
```

## Elixir

```elixir
defmodule Solution do
  @spec string_matching(words :: [String.t]) :: [String.t]
  def string_matching(words) do
    Enum.filter(words, fn w ->
      Enum.any?(words, fn other -> w != other && String.contains?(other, w) end)
    end)
  end
end
```
