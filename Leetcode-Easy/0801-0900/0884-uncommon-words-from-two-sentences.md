# 0884. Uncommon Words from Two Sentences

## Cpp

```cpp
class Solution {
public:
    vector<string> uncommonFromSentences(string s1, string s2) {
        unordered_map<string,int> cnt;
        auto add = [&](const string& str){
            size_t i=0, n=str.size();
            while(i<n){
                // skip spaces (though there shouldn't be consecutive)
                while(i<n && str[i]==' ') ++i;
                if(i>=n) break;
                size_t j=i;
                while(j<n && str[j]!=' ') ++j;
                cnt[str.substr(i,j-i)]++;
                i=j;
            }
        };
        add(s1);
        add(s2);
        vector<string> res;
        for (auto &p: cnt){
            if(p.second==1) res.push_back(p.first);
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public String[] uncommonFromSentences(String s1, String s2) {
        java.util.Map<String, Integer> count = new java.util.HashMap<>();
        for (String w : s1.split(" ")) {
            count.put(w, count.getOrDefault(w, 0) + 1);
        }
        for (String w : s2.split(" ")) {
            count.put(w, count.getOrDefault(w, 0) + 1);
        }
        java.util.List<String> result = new java.util.ArrayList<>();
        for (java.util.Map.Entry<String, Integer> entry : count.entrySet()) {
            if (entry.getValue() == 1) {
                result.add(entry.getKey());
            }
        }
        return result.toArray(new String[0]);
    }
}
```

## Python

```python
class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        from collections import Counter
        words = s1.split() + s2.split()
        cnt = Counter(words)
        return [word for word, c in cnt.items() if c == 1]
```

## Python3

```python
from typing import List
from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        cnt = Counter(s1.split()) + Counter(s2.split())
        return [word for word, c in cnt.items() if c == 1]
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    char *word;
    int count;
} WordCount;

static char* my_strdup(const char *s) {
    size_t len = strlen(s);
    char *dup = (char*)malloc(len + 1);
    if (dup) memcpy(dup, s, len + 1);
    return dup;
}

static void add_word(WordCount *arr, int *size, const char *w) {
    for (int i = 0; i < *size; ++i) {
        if (strcmp(arr[i].word, w) == 0) {
            arr[i].count++;
            return;
        }
    }
    arr[*size].word = my_strdup(w);
    arr[*size].count = 1;
    (*size)++;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** uncommonFromSentences(char* s1, char* s2, int* returnSize) {
    WordCount words[400];
    int wordCnt = 0;

    // Process first sentence
    char *buf1 = my_strdup(s1);
    char *token = strtok(buf1, " ");
    while (token) {
        add_word(words, &wordCnt, token);
        token = strtok(NULL, " ");
    }

    // Process second sentence
    char *buf2 = my_strdup(s2);
    token = strtok(buf2, " ");
    while (token) {
        add_word(words, &wordCnt, token);
        token = strtok(NULL, " ");
    }

    // Collect uncommon words
    int uncommonNum = 0;
    for (int i = 0; i < wordCnt; ++i) {
        if (words[i].count == 1) uncommonNum++;
    }

    char **result = (char**)malloc(sizeof(char*) * uncommonNum);
    int idx = 0;
    for (int i = 0; i < wordCnt; ++i) {
        if (words[i].count == 1) {
            result[idx++] = words[i].word; // transfer ownership
        } else {
            free(words[i].word); // not needed in result, free now
        }
    }

    *returnSize = uncommonNum;

    free(buf1);
    free(buf2);
    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public string[] UncommonFromSentences(string s1, string s2) {
        var count = new Dictionary<string, int>();
        foreach (var word in s1.Split(' ')) {
            if (count.ContainsKey(word))
                count[word]++;
            else
                count[word] = 1;
        }
        foreach (var word in s2.Split(' ')) {
            if (count.ContainsKey(word))
                count[word]++;
            else
                count[word] = 1;
        }

        var result = new List<string>();
        foreach (var kvp in count) {
            if (kvp.Value == 1)
                result.Add(kvp.Key);
        }
        return result.ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s1
 * @param {string} s2
 * @return {string[]}
 */
var uncommonFromSentences = function(s1, s2) {
    const count = new Map();
    const words = (s1 + ' ' + s2).trim().split(' ');
    for (const w of words) {
        if (w.length === 0) continue;
        count.set(w, (count.get(w) || 0) + 1);
    }
    const result = [];
    for (const [word, cnt] of count.entries()) {
        if (cnt === 1) result.push(word);
    }
    return result;
};
```

## Typescript

```typescript
function uncommonFromSentences(s1: string, s2: string): string[] {
    const count = new Map<string, number>();
    for (const w of s1.split(' ')) {
        count.set(w, (count.get(w) ?? 0) + 1);
    }
    for (const w of s2.split(' ')) {
        count.set(w, (count.get(w) ?? 0) + 1);
    }
    const result: string[] = [];
    for (const [word, cnt] of count) {
        if (cnt === 1) result.push(word);
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s1
     * @param String $s2
     * @return String[]
     */
    function uncommonFromSentences($s1, $s2) {
        $words = array_merge(explode(' ', $s1), explode(' ', $s2));
        $count = [];
        foreach ($words as $w) {
            if (isset($count[$w])) {
                $count[$w]++;
            } else {
                $count[$w] = 1;
            }
        }
        $result = [];
        foreach ($count as $word => $freq) {
            if ($freq === 1) {
                $result[] = $word;
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func uncommonFromSentences(_ s1: String, _ s2: String) -> [String] {
        var freq = [String: Int]()
        for w in s1.split(separator: " ") {
            let word = String(w)
            freq[word, default: 0] += 1
        }
        for w in s2.split(separator: " ") {
            let word = String(w)
            freq[word, default: 0] += 1
        }
        var result = [String]()
        for (word, count) in freq where count == 1 {
            result.append(word)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun uncommonFromSentences(s1: String, s2: String): Array<String> {
        val count = HashMap<String, Int>()
        for (word in s1.split(" ")) {
            count[word] = count.getOrDefault(word, 0) + 1
        }
        for (word in s2.split(" ")) {
            count[word] = count.getOrDefault(word, 0) + 1
        }
        val result = mutableListOf<String>()
        for ((k, v) in count) {
            if (v == 1) result.add(k)
        }
        return result.toTypedArray()
    }
}
```

## Dart

```dart
class Solution {
  List<String> uncommonFromSentences(String s1, String s2) {
    final Map<String, int> count = {};
    for (var word in s1.split(' ')) {
      count[word] = (count[word] ?? 0) + 1;
    }
    for (var word in s2.split(' ')) {
      count[word] = (count[word] ?? 0) + 1;
    }
    final List<String> result = [];
    count.forEach((word, freq) {
      if (freq == 1) result.add(word);
    });
    return result;
  }
}
```

## Golang

```go
package main

import "strings"

func uncommonFromSentences(s1 string, s2 string) []string {
	count := make(map[string]int)
	for _, w := range strings.Split(s1, " ") {
		count[w]++
	}
	for _, w := range strings.Split(s2, " ") {
		count[w]++
	}
	res := []string{}
	for w, c := range count {
		if c == 1 {
			res = append(res, w)
		}
	}
	return res
}
```

## Ruby

```ruby
def uncommon_from_sentences(s1, s2)
  counts = Hash.new(0)
  (s1.split + s2.split).each { |word| counts[word] += 1 }
  counts.select { |_k, v| v == 1 }.keys
end
```

## Scala

```scala
object Solution {
    def uncommonFromSentences(s1: String, s2: String): Array[String] = {
        val counts = scala.collection.mutable.Map[String, Int]().withDefaultValue(0)
        for (w <- (s1 + " " + s2).split(" ")) {
            counts(w) += 1
        }
        counts.filter(_._2 == 1).keys.toArray
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn uncommon_from_sentences(s1: String, s2: String) -> Vec<String> {
        let mut cnt: HashMap<String, i32> = HashMap::new();
        for w in s1.split_whitespace().chain(s2.split_whitespace()) {
            *cnt.entry(w.to_string()).or_insert(0) += 1;
        }
        cnt.into_iter()
            .filter_map(|(k, v)| if v == 1 { Some(k) } else { None })
            .collect()
    }
}
```

## Racket

```racket
(require racket/string)

(define/contract (uncommon-from-sentences s1 s2)
  (-> string? string? (listof string?))
  (let* ([words (append (string-split s1) (string-split s2))]
         [cnt   (make-hash)])
    (for ([w words])
      (hash-set! cnt w (+ 1 (hash-ref cnt w 0))))
    (for/list ([(k v) (in-hash cnt)] #:when (= v 1)) k)))
```

## Erlang

```erlang
-module(solution).
-export([uncommon_from_sentences/2]).

-spec uncommon_from_sentences(S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary()) -> [unicode:unicode_binary()].
uncommon_from_sentences(S1, S2) ->
    Words1 = binary:split(S1, <<" ">>, [global]),
    Words2 = binary:split(S2, <<" ">>, [global]),
    CountMap = count_words(Words1 ++ Words2, #{}),
    [Word || {Word, 1} <- maps:to_list(CountMap)].

count_words([], Map) -> Map;
count_words([W|Rest], Map) ->
    Count = maps:get(W, Map, 0),
    NewMap = maps:put(W, Count + 1, Map),
    count_words(Rest, NewMap).
```

## Elixir

```elixir
defmodule Solution do
  @spec uncommon_from_sentences(s1 :: String.t(), s2 :: String.t()) :: [String.t()]
  def uncommon_from_sentences(s1, s2) do
    words = String.split(s1 <> " " <> s2, " ", trim: true)

    counts =
      Enum.reduce(words, %{}, fn word, acc ->
        Map.update(acc, word, 1, &(&1 + 1))
      end)

    counts
    |> Enum.filter(fn {_word, cnt} -> cnt == 1 end)
    |> Enum.map(fn {word, _cnt} -> word end)
  end
end
```
