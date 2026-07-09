# 1078. Occurrences After Bigram

## Cpp

```cpp
class Solution {
public:
    vector<string> findOcurrences(string text, string first, string second) {
        vector<string> words;
        string cur;
        for (char c : text) {
            if (c == ' ') {
                words.push_back(cur);
                cur.clear();
            } else {
                cur += c;
            }
        }
        if (!cur.empty()) words.push_back(cur);
        
        vector<string> ans;
        for (size_t i = 0; i + 2 < words.size(); ++i) {
            if (words[i] == first && words[i + 1] == second) {
                ans.push_back(words[i + 2]);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public String[] findOcurrences(String text, String first, String second) {
        String[] words = text.split(" ");
        java.util.List<String> res = new java.util.ArrayList<>();
        for (int i = 0; i + 2 < words.length; i++) {
            if (words[i].equals(first) && words[i + 1].equals(second)) {
                res.add(words[i + 2]);
            }
        }
        return res.toArray(new String[0]);
    }
}
```

## Python

```python
class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        words = text.split()
        res = []
        for i in range(len(words) - 2):
            if words[i] == first and words[i + 1] == second:
                res.append(words[i + 2])
        return res
```

## Python3

```python
from typing import List

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        res = []
        for i in range(len(words) - 2):
            if words[i] == first and words[i + 1] == second:
                res.append(words[i + 2])
        return res
```

## C

```c
#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** findOcurrences(char* text, char* first, char* second, int* returnSize) {
    if (!text || !first || !second) {
        *returnSize = 0;
        return NULL;
    }

    // Duplicate the input string to safely tokenize
    char *buf = strdup(text);
    if (!buf) {
        *returnSize = 0;
        return NULL;
    }

    // Store pointers to each word (they point inside buf)
    int capWords = 128;
    char **words = (char **)malloc(capWords * sizeof(char *));
    int n = 0;

    char *token = strtok(buf, " ");
    while (token) {
        if (n >= capWords) {
            capWords <<= 1;
            words = (char **)realloc(words, capWords * sizeof(char *));
        }
        words[n++] = token;
        token = strtok(NULL, " ");
    }

    // Prepare result array
    char **result = (char **)malloc(n * sizeof(char *));
    int cnt = 0;

    for (int i = 0; i + 2 < n; ++i) {
        if (strcmp(words[i], first) == 0 && strcmp(words[i + 1], second) == 0) {
            result[cnt++] = strdup(words[i + 2]);
        }
    }

    // Clean up
    free(buf);
    free(words);

    *returnSize = cnt;
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public string[] FindOcurrences(string text, string first, string second)
    {
        var words = text.Split(' ');
        var result = new List<string>();
        for (int i = 0; i + 2 < words.Length; i++)
        {
            if (words[i] == first && words[i + 1] == second)
                result.Add(words[i + 2]);
        }
        return result.ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} text
 * @param {string} first
 * @param {string} second
 * @return {string[]}
 */
var findOcurrences = function(text, first, second) {
    const words = text.split(' ');
    const res = [];
    for (let i = 0; i + 2 < words.length; i++) {
        if (words[i] === first && words[i + 1] === second) {
            res.push(words[i + 2]);
        }
    }
    return res;
};
```

## Typescript

```typescript
function findOcurrences(text: string, first: string, second: string): string[] {
    const words = text.split(' ');
    const result: string[] = [];
    for (let i = 0; i + 2 < words.length; i++) {
        if (words[i] === first && words[i + 1] === second) {
            result.push(words[i + 2]);
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $text
     * @param String $first
     * @param String $second
     * @return String[]
     */
    function findOcurrences($text, $first, $second) {
        $words = explode(' ', $text);
        $n = count($words);
        $result = [];
        for ($i = 0; $i + 2 < $n; $i++) {
            if ($words[$i] === $first && $words[$i + 1] === $second) {
                $result[] = $words[$i + 2];
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func findOcurrences(_ text: String, _ first: String, _ second: String) -> [String] {
        let words = text.split(separator: " ").map(String.init)
        var result = [String]()
        guard words.count >= 3 else { return result }
        for i in 0..<(words.count - 2) {
            if words[i] == first && words[i + 1] == second {
                result.append(words[i + 2])
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findOcurrences(text: String, first: String, second: String): Array<String> {
        val words = text.split(' ')
        val result = mutableListOf<String>()
        for (i in 0 until words.size - 2) {
            if (words[i] == first && words[i + 1] == second) {
                result.add(words[i + 2])
            }
        }
        return result.toTypedArray()
    }
}
```

## Dart

```dart
class Solution {
  List<String> findOcurrences(String text, String first, String second) {
    List<String> words = text.split(' ');
    List<String> result = [];
    for (int i = 0; i + 2 < words.length; i++) {
      if (words[i] == first && words[i + 1] == second) {
        result.add(words[i + 2]);
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

func findOcurrences(text string, first string, second string) []string {
	words := strings.Split(text, " ")
	var result []string
	for i := 0; i+2 < len(words); i++ {
		if words[i] == first && words[i+1] == second {
			result = append(result, words[i+2])
		}
	}
	return result
}
```

## Ruby

```ruby
def find_ocurrences(text, first, second)
  words = text.split(' ')
  res = []
  (0..words.length - 3).each do |i|
    if words[i] == first && words[i + 1] == second
      res << words[i + 2]
    end
  end
  res
end
```

## Scala

```scala
object Solution {
    def findOcurrences(text: String, first: String, second: String): Array[String] = {
        val words = text.split(" ")
        val result = scala.collection.mutable.ArrayBuffer[String]()
        var i = 0
        while (i + 2 < words.length) {
            if (words(i) == first && words(i + 1) == second) {
                result += words(i + 2)
            }
            i += 1
        }
        result.toArray
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_ocurrences(text: String, first: String, second: String) -> Vec<String> {
        let words: Vec<&str> = text.split_whitespace().collect();
        let mut result = Vec::new();
        for i in 0..words.len() {
            if i + 2 < words.len()
                && words[i] == first
                && words[i + 1] == second
            {
                result.push(words[i + 2].to_string());
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

(define/contract (find-ocurrences text first second)
  (-> string? string? string? (listof string?))
  (let* ([words (string-split text " ")]
         [n (length words)])
    (for/list ([i (in-range (- n 2))]
               #:when (and (string=? (list-ref words i) first)
                           (string=? (list-ref words (+ i 1)) second)))
      (list-ref words (+ i 2)))))
```

## Erlang

```erlang
-module(solution).
-export([find_ocurrences/3]).

-spec find_ocurrences(Text :: unicode:unicode_binary(),
                      First :: unicode:unicode_binary(),
                      Second :: unicode:unicode_binary()) ->
    [unicode:unicode_binary()].
find_ocurrences(Text, First, Second) ->
    Words = binary:split(Text, <<" ">>, [global]),
    find_occ(Words, First, Second).

-spec find_occ([binary()], binary(), binary()) -> [binary()].
find_occ([F,S,T|Rest], First, Second) ->
    case (F =:= First andalso S =:= Second) of
        true  -> [T | find_occ([S,T|Rest], First, Second)];
        false -> find_occ([S,T|Rest], First, Second)
    end;
find_occ(_, _, _) -> [].
```

## Elixir

```elixir
defmodule Solution do
  @spec find_ocurrences(text :: String.t, first :: String.t, second :: String.t) :: [String.t]
  def find_ocurrences(text, first, second) do
    text
    |> String.split()
    |> Enum.chunk_every(3, 1, [])
    |> Enum.filter(fn
      [w1, w2, _] -> w1 == first and w2 == second
      _ -> false
    end)
    |> Enum.map(fn [_ , _, w3] -> w3 end)
  end
end
```
