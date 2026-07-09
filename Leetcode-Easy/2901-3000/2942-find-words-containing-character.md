# 2942. Find Words Containing Character

## Cpp

```cpp
class Solution {
public:
    vector<int> findWordsContaining(vector<string>& words, char x) {
        vector<int> result;
        for (int i = 0; i < (int)words.size(); ++i) {
            if (words[i].find(x) != string::npos) {
                result.push_back(i);
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
    public List<Integer> findWordsContaining(String[] words, char x) {
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < words.length; i++) {
            if (words[i].indexOf(x) != -1) {
                result.add(i);
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        res = []
        for i, w in enumerate(words):
            if x in w:
                res.append(i)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for i, w in enumerate(words):
            if x in w:
                result.append(i)
        return result
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findWordsContaining(char** words, int wordsSize, char x, int* returnSize) {
    int* result = (int*)malloc(wordsSize * sizeof(int));
    int cnt = 0;
    for (int i = 0; i < wordsSize; ++i) {
        char* p = words[i];
        while (*p) {
            if (*p == x) {
                result[cnt++] = i;
                break;
            }
            ++p;
        }
    }
    *returnSize = cnt;
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public IList<int> FindWordsContaining(string[] words, char x)
    {
        var result = new List<int>();
        for (int i = 0; i < words.Length; i++)
        {
            if (words[i].IndexOf(x) >= 0)
                result.Add(i);
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @param {character} x
 * @return {number[]}
 */
var findWordsContaining = function(words, x) {
    const result = [];
    for (let i = 0; i < words.length; i++) {
        if (words[i].includes(x)) {
            result.push(i);
        }
    }
    return result;
};
```

## Typescript

```typescript
function findWordsContaining(words: string[], x: string): number[] {
    const result: number[] = [];
    for (let i = 0; i < words.length; i++) {
        if (words[i].includes(x)) {
            result.push(i);
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
     * @param String $x
     * @return Integer[]
     */
    function findWordsContaining($words, $x) {
        $result = [];
        foreach ($words as $index => $word) {
            if (strpos($word, $x) !== false) {
                $result[] = $index;
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func findWordsContaining(_ words: [String], _ x: Character) -> [Int] {
        var result = [Int]()
        for (index, word) in words.enumerated() {
            if word.contains(x) {
                result.append(index)
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findWordsContaining(words: Array<String>, x: Char): List<Int> {
        val result = mutableListOf<Int>()
        for (i in words.indices) {
            if (words[i].indexOf(x) != -1) {
                result.add(i)
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> findWordsContaining(List<String> words, String x) {
    List<int> result = [];
    for (int i = 0; i < words.length; i++) {
      if (words[i].contains(x)) {
        result.add(i);
      }
    }
    return result;
  }
}
```

## Golang

```go
import "strings"

func findWordsContaining(words []string, x byte) []int {
	res := []int{}
	for i, w := range words {
		if strings.IndexByte(w, x) != -1 {
			res = append(res, i)
		}
	}
	return res
}
```

## Ruby

```ruby
def find_words_containing(words, x)
  result = []
  words.each_with_index do |word, idx|
    result << idx if word.include?(x)
  end
  result
end
```

## Scala

```scala
object Solution {
    def findWordsContaining(words: Array[String], x: Char): List[Int] = {
        words.zipWithIndex.collect { case (w, i) if w.contains(x) => i }.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_words_containing(words: Vec<String>, x: char) -> Vec<i32> {
        let mut res = Vec::new();
        for (i, w) in words.iter().enumerate() {
            if w.contains(x) {
                res.push(i as i32);
            }
        }
        res
    }
}
```

## Racket

```racket
(define/contract (find-words-containing words x)
  (-> (listof string?) char? (listof exact-integer?))
  (define (string-contains-char? s ch)
    (for/or ([c (in-string s)]) (char=? c ch)))
  (let loop ((lst words) (idx 0) (acc '()))
    (cond [(null? lst) (reverse acc)]
          [(string-contains-char? (car lst) x)
           (loop (cdr lst) (+ idx 1) (cons idx acc))]
          [else
           (loop (cdr lst) (+ idx 1) acc)])))
```

## Erlang

```erlang
-spec find_words_containing(Words :: [unicode:unicode_binary()], X :: char()) -> [integer()].
find_words_containing(Words, X) ->
    find_words_containing(Words, X, 0, []).

find_words_containing([], _X, _Idx, Acc) ->
    lists:reverse(Acc);
find_words_containing([Word|Rest], X, Idx, Acc) ->
    case binary:match(Word, <<X>>) of
        {_,_} -> find_words_containing(Rest, X, Idx + 1, [Idx | Acc]);
        nomatch -> find_words_containing(Rest, X, Idx + 1, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_words_containing(words :: [String.t()], x :: String.t()) :: [integer()]
  def find_words_containing(words, x) do
    words
    |> Enum.with_index()
    |> Enum.filter(fn {word, _idx} -> String.contains?(word, x) end)
    |> Enum.map(fn {_word, idx} -> idx end)
  end
end
```
