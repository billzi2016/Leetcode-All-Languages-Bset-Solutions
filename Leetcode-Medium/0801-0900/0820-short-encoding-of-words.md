# 0820. Short Encoding of Words

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minimumLengthEncoding(vector<string>& words) {
        unordered_set<string> uniq(words.begin(), words.end());
        for (const string& w : words) {
            for (size_t i = 1; i < w.size(); ++i) {
                uniq.erase(w.substr(i));
            }
        }
        int ans = 0;
        for (const string& w : uniq) {
            ans += w.size() + 1; // plus '#'
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int minimumLengthEncoding(String[] words) {
        Set<String> unique = new HashSet<>(Arrays.asList(words));
        for (String word : words) {
            int len = word.length();
            for (int i = 1; i < len; ++i) {
                unique.remove(word.substring(i));
            }
        }
        int result = 0;
        for (String w : unique) {
            result += w.length() + 1;
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        uniq = set(words)
        for w in list(uniq):
            # remove all proper suffixes of w
            for i in range(1, len(w)):
                suffix = w[i:]
                if suffix in uniq:
                    uniq.discard(suffix)
        return sum(len(w) + 1 for w in uniq)
```

## Python3

```python
from typing import List

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        unique_words = set(words)
        for word in list(unique_words):
            for i in range(1, len(word)):
                suffix = word[i:]
                if suffix in unique_words:
                    unique_words.discard(suffix)
        return sum(len(w) + 1 for w in unique_words)
```

## C

```c
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

static int cmp_str(const void *a, const void *b) {
    return strcmp(*(const char **)a, *(const char **)b);
}

static bool is_suffix(const char *word, const char *candidate) {
    size_t wlen = strlen(word);
    size_t clen = strlen(candidate);
    if (clen < wlen) return false;
    return strcmp(candidate + clen - wlen, word) == 0;
}

int minimumLengthEncoding(char** words, int wordsSize) {
    if (wordsSize == 0) return 0;

    // Sort words to facilitate duplicate removal
    char **sorted = (char **)malloc(wordsSize * sizeof(char *));
    for (int i = 0; i < wordsSize; ++i) sorted[i] = words[i];
    qsort(sorted, wordsSize, sizeof(char *), cmp_str);

    // Remove duplicates
    char **uniq = (char **)malloc(wordsSize * sizeof(char *));
    int uniqCount = 0;
    for (int i = 0; i < wordsSize; ++i) {
        if (i == 0 || strcmp(sorted[i], sorted[i - 1]) != 0) {
            uniq[uniqCount++] = sorted[i];
        }
    }

    free(sorted);

    int result = 0;
    for (int i = 0; i < uniqCount; ++i) {
        bool suffix = false;
        for (int j = 0; j < uniqCount; ++j) {
            if (i == j) continue;
            if (is_suffix(uniq[i], uniq[j])) {
                suffix = true;
                break;
            }
        }
        if (!suffix) {
            result += (int)strlen(uniq[i]) + 1; // plus '#'
        }
    }

    free(uniq);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinimumLengthEncoding(string[] words)
    {
        var uniq = new HashSet<string>(words);
        foreach (var word in words)
        {
            for (int i = 1; i < word.Length; ++i)
            {
                var suffix = word.Substring(i);
                if (uniq.Contains(suffix))
                    uniq.Remove(suffix);
            }
        }

        int result = 0;
        foreach (var w in uniq)
            result += w.Length + 1;

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @return {number}
 */
var minimumLengthEncoding = function(words) {
    const uniqueWords = new Set(words);
    for (const word of words) {
        for (let i = 1; i < word.length; ++i) {
            uniqueWords.delete(word.slice(i));
        }
    }
    let total = 0;
    for (const w of uniqueWords) {
        total += w.length + 1;
    }
    return total;
};
```

## Typescript

```typescript
function minimumLengthEncoding(words: string[]): number {
    const uniq = new Set<string>(words);
    for (const word of words) {
        for (let i = 1; i < word.length; ++i) {
            const suffix = word.substring(i);
            if (uniq.has(suffix)) {
                uniq.delete(suffix);
            }
        }
    }
    let total = 0;
    for (const w of uniq) {
        total += w.length + 1;
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $words
     * @return Integer
     */
    function minimumLengthEncoding($words) {
        // Remove duplicates
        $unique = array_unique($words);
        $toRemove = [];

        foreach ($unique as $word) {
            $len = strlen($word);
            for ($i = 1; $i < $len; $i++) {
                $suffix = substr($word, $i);
                $toRemove[$suffix] = true;
            }
        }

        $result = 0;
        foreach ($unique as $word) {
            if (!isset($toRemove[$word])) {
                $result += strlen($word) + 1; // plus '#'
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func minimumLengthEncoding(_ words: [String]) -> Int {
        let uniqueWords = Set(words)
        var filtered = uniqueWords
        
        for word in uniqueWords {
            if word.isEmpty { continue }
            var startIdx = word.index(word.startIndex, offsetBy: 1)
            while startIdx < word.endIndex {
                let suffix = String(word[startIdx...])
                filtered.remove(suffix)
                startIdx = word.index(after: startIdx)
            }
        }
        
        var result = 0
        for w in filtered {
            result += w.count + 1 // plus '#'
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumLengthEncoding(words: Array<String>): Int {
        val uniqueWords = HashSet<String>(words.asList())
        for (word in words) {
            for (i in 1 until word.length) {
                uniqueWords.remove(word.substring(i))
            }
        }
        var result = 0
        for (w in uniqueWords) {
            result += w.length + 1
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  int minimumLengthEncoding(List<String> words) {
    final Set<String> uniq = Set.from(words);
    for (final word in words) {
      for (int i = 1; i < word.length; ++i) {
        uniq.remove(word.substring(i));
      }
    }
    int result = 0;
    for (final w in uniq) {
      result += w.length + 1;
    }
    return result;
  }
}
```

## Golang

```go
func minimumLengthEncoding(words []string) int {
	unique := make(map[string]struct{})
	for _, w := range words {
		unique[w] = struct{}{}
	}
	for w := range unique {
		for i := 1; i < len(w); i++ {
			if _, ok := unique[w[i:]]; ok {
				delete(unique, w[i:])
			}
		}
	}
	ans := 0
	for w := range unique {
		ans += len(w) + 1
	}
	return ans
}
```

## Ruby

```ruby
require 'set'

def minimum_length_encoding(words)
  unique_words = words.uniq
  remaining = Set.new(unique_words)

  unique_words.each do |word|
    (1...word.length).each do |i|
      suffix = word[i..-1]
      remaining.delete(suffix)
    end
  end

  remaining.reduce(0) { |sum, w| sum + w.length + 1 }
end
```

## Scala

```scala
object Solution {
  def minimumLengthEncoding(words: Array[String]): Int = {
    val uniq = words.toSet
    val filtered = scala.collection.mutable.Set[String]() ++ uniq
    for (w <- uniq) {
      var i = 1
      while (i < w.length) {
        val suffix = w.substring(i)
        if (filtered.contains(suffix)) filtered -= suffix
        i += 1
      }
    }
    filtered.map(_.length + 1).sum
  }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn minimum_length_encoding(words: Vec<String>) -> i32 {
        let mut uniq: HashSet<String> = words.into_iter().collect();
        // Clone keys to iterate without borrowing issues
        let words_clone: Vec<String> = uniq.iter().cloned().collect();
        for word in words_clone.iter() {
            let w = word.as_str();
            for i in 1..w.len() {
                let suffix = &w[i..];
                uniq.remove(suffix);
            }
        }
        let mut ans = 0usize;
        for w in uniq.iter() {
            ans += w.len() + 1; // plus '#'
        }
        ans as i32
    }
}
```

## Racket

```racket
#lang racket

(require racket/list)

(define/contract (minimum-length-encoding words)
  (-> (listof string?) exact-integer?)
  (let* ([unique (remove-duplicates words)]
         [word-set (make-hash)])
    ;; insert all unique words
    (for ([w unique]) (hash-set! word-set w #t))
    ;; remove any word that is a proper suffix of another
    (for ([w unique])
      (let loop ((i 1) (len (string-length w)))
        (when (< i len)
          (define suffix (substring w i len))
          (when (hash-has-key? word-set suffix)
            (hash-remove! word-set suffix))
          (loop (+ i 1) len))))
    ;; sum lengths + 1 for remaining words
    (for/sum ([w (in-hash-keys word-set)])
      (+ (string-length w) 1))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_length_encoding/1]).

-spec minimum_length_encoding(Words :: [unicode:unicode_binary()]) -> integer().
minimum_length_encoding(Words) ->
    %% Build a map as a set of unique words
    InitMap = maps:from_list([{W, true} || W <- Words]),
    %% Remove all proper suffixes from the set
    FinalMap = lists:foldl(
        fun(Word, AccMap) ->
            Suffixes = proper_suffixes(Word),
            lists:foldl(fun(Suf, M) -> maps:remove(Suf, M) end,
                        AccMap, Suffixes)
        end,
        InitMap,
        maps:keys(InitMap)),
    %% Sum lengths + 1 for remaining words
    Remaining = maps:keys(FinalMap),
    lists:foldl(fun(W, Sum) -> Sum + byte_size(W) + 1 end, 0, Remaining).

%% Generate all proper suffixes of a word (excluding the word itself)
-spec proper_suffixes(unicode:unicode_binary()) -> [unicode:unicode_binary()].
proper_suffixes(Word) ->
    Len = byte_size(Word),
    proper_suffixes_loop(Word, 1, Len, []).

-spec proper_suffixes_loop(unicode:unicode_binary(), integer(), integer(),
                          [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
proper_suffixes_loop(_Word, Start, Len, Acc) when Start >= Len ->
    lists:reverse(Acc);
proper_suffixes_loop(Word, Start, Len, Acc) ->
    Suffix = binary:part(Word, {Start, Len - Start}),
    proper_suffixes_loop(Word, Start + 1, Len, [Suffix | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_length_encoding(words :: [String.t]) :: integer
  def minimum_length_encoding(words) do
    uniq = MapSet.new(words)

    suffixes =
      words
      |> Enum.flat_map(fn word ->
        len = String.length(word)

        if len > 1 do
          1..(len - 1)
          |> Enum.map(fn i -> binary_part(word, i, len - i) end)
        else
          []
        end
      end)

    to_remove = MapSet.new(suffixes) |> MapSet.intersection(uniq)
    remaining = MapSet.difference(uniq, to_remove)

    Enum.reduce(remaining, 0, fn w, acc -> acc + String.length(w) + 1 end)
  end
end
```
