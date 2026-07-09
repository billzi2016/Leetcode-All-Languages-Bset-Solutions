# 2085. Count Common Words With One Occurrence

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countWords(vector<string>& words1, vector<string>& words2) {
        unordered_map<string,int> cnt1, cnt2;
        for (const auto& w : words1) ++cnt1[w];
        for (const auto& w : words2) ++cnt2[w];
        int ans = 0;
        for (const auto& [word, c] : cnt1) {
            if (c == 1 && cnt2[word] == 1) ++ans;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int countWords(String[] words1, String[] words2) {
        java.util.Map<String, Integer> freq1 = new java.util.HashMap<>();
        for (String w : words1) {
            freq1.put(w, freq1.getOrDefault(w, 0) + 1);
        }
        java.util.Map<String, Integer> freq2 = new java.util.HashMap<>();
        for (String w : words2) {
            freq2.put(w, freq2.getOrDefault(w, 0) + 1);
        }
        int count = 0;
        for (java.util.Map.Entry<String, Integer> entry : freq1.entrySet()) {
            if (entry.getValue() == 1 && freq2.getOrDefault(entry.getKey(), 0) == 1) {
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
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        from collections import Counter
        cnt1 = Counter(words1)
        cnt2 = Counter(words2)
        ans = 0
        for w in cnt1:
            if cnt1[w] == 1 and cnt2.get(w, 0) == 1:
                ans += 1
        return ans
```

## Python3

```python
from collections import Counter
from typing import List

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        cnt1 = Counter(words1)
        cnt2 = Counter(words2)
        ans = 0
        for word in cnt1:
            if cnt1[word] == 1 and cnt2.get(word, 0) == 1:
                ans += 1
        return ans
```

## C

```c
#include <string.h>

int countWords(char** words1, int words1Size, char** words2, int words2Size) {
    // Frequency maps using simple arrays (max 1000 unique entries each)
    char* uniq1[1000];
    int cnt1[1000];
    int u1 = 0;
    for (int i = 0; i < words1Size; ++i) {
        int found = -1;
        for (int j = 0; j < u1; ++j) {
            if (strcmp(words1[i], uniq1[j]) == 0) {
                found = j;
                break;
            }
        }
        if (found != -1) {
            cnt1[found]++;
        } else {
            uniq1[u1] = words1[i];
            cnt1[u1] = 1;
            u1++;
        }
    }

    char* uniq2[1000];
    int cnt2[1000];
    int u2 = 0;
    for (int i = 0; i < words2Size; ++i) {
        int found = -1;
        for (int j = 0; j < u2; ++j) {
            if (strcmp(words2[i], uniq2[j]) == 0) {
                found = j;
                break;
            }
        }
        if (found != -1) {
            cnt2[found]++;
        } else {
            uniq2[u2] = words2[i];
            cnt2[u2] = 1;
            u2++;
        }
    }

    int result = 0;
    for (int i = 0; i < u1; ++i) {
        if (cnt1[i] != 1) continue;
        for (int j = 0; j < u2; ++j) {
            if (cnt2[j] == 1 && strcmp(uniq1[i], uniq2[j]) == 0) {
                result++;
                break;
            }
        }
    }

    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int CountWords(string[] words1, string[] words2) {
        var count1 = new Dictionary<string, int>();
        foreach (var w in words1) {
            if (count1.ContainsKey(w)) count1[w]++;
            else count1[w] = 1;
        }
        
        var count2 = new Dictionary<string, int>();
        foreach (var w in words2) {
            if (count2.ContainsKey(w)) count2[w]++;
            else count2[w] = 1;
        }
        
        int result = 0;
        foreach (var kvp in count1) {
            if (kvp.Value == 1 && count2.TryGetValue(kvp.Key, out int v2) && v2 == 1) {
                result++;
            }
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words1
 * @param {string[]} words2
 * @return {number}
 */
var countWords = function(words1, words2) {
    const freq1 = new Map();
    for (const w of words1) {
        freq1.set(w, (freq1.get(w) || 0) + 1);
    }
    const freq2 = new Map();
    for (const w of words2) {
        freq2.set(w, (freq2.get(w) || 0) + 1);
    }
    let count = 0;
    for (const [word, c] of freq1.entries()) {
        if (c === 1 && freq2.get(word) === 1) {
            count++;
        }
    }
    return count;
};
```

## Typescript

```typescript
function countWords(words1: string[], words2: string[]): number {
    const freq1 = new Map<string, number>();
    for (const w of words1) {
        freq1.set(w, (freq1.get(w) ?? 0) + 1);
    }
    const freq2 = new Map<string, number>();
    for (const w of words2) {
        freq2.set(w, (freq2.get(w) ?? 0) + 1);
    }
    let count = 0;
    for (const [word, c] of freq1.entries()) {
        if (c === 1 && freq2.get(word) === 1) {
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
     * @param String[] $words1
     * @param String[] $words2
     * @return Integer
     */
    function countWords($words1, $words2) {
        $freq1 = [];
        foreach ($words1 as $w) {
            if (!isset($freq1[$w])) {
                $freq1[$w] = 0;
            }
            $freq1[$w]++;
        }

        $freq2 = [];
        foreach ($words2 as $w) {
            if (!isset($freq2[$w])) {
                $freq2[$w] = 0;
            }
            $freq2[$w]++;
        }

        $count = 0;
        foreach ($freq1 as $word => $c1) {
            if ($c1 === 1 && isset($freq2[$word]) && $freq2[$word] === 1) {
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
    func countWords(_ words1: [String], _ words2: [String]) -> Int {
        var freq1 = [String: Int]()
        for w in words1 {
            freq1[w, default: 0] += 1
        }
        var freq2 = [String: Int]()
        for w in words2 {
            freq2[w, default: 0] += 1
        }
        var count = 0
        for (word, c) in freq1 where c == 1 {
            if freq2[word] == 1 {
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
    fun countWords(words1: Array<String>, words2: Array<String>): Int {
        val freq1 = mutableMapOf<String, Int>()
        for (w in words1) {
            freq1[w] = freq1.getOrDefault(w, 0) + 1
        }
        val freq2 = mutableMapOf<String, Int>()
        for (w in words2) {
            freq2[w] = freq2.getOrDefault(w, 0) + 1
        }
        var count = 0
        for ((word, c1) in freq1) {
            if (c1 == 1 && freq2.getOrDefault(word, 0) == 1) {
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
  int countWords(List<String> words1, List<String> words2) {
    final Map<String, int> freq1 = {};
    for (var w in words1) {
      freq1[w] = (freq1[w] ?? 0) + 1;
    }

    final Map<String, int> freq2 = {};
    for (var w in words2) {
      freq2[w] = (freq2[w] ?? 0) + 1;
    }

    int count = 0;
    for (var entry in freq1.entries) {
      if (entry.value == 1 && (freq2[entry.key] ?? 0) == 1) {
        count++;
      }
    }
    return count;
  }
}
```

## Golang

```go
func countWords(words1 []string, words2 []string) int {
	freq1 := make(map[string]int)
	for _, w := range words1 {
		freq1[w]++
	}
	freq2 := make(map[string]int)
	for _, w := range words2 {
		freq2[w]++
	}
	count := 0
	for w, c1 := range freq1 {
		if c1 == 1 && freq2[w] == 1 {
			count++
		}
	}
	return count
}
```

## Ruby

```ruby
def count_words(words1, words2)
  freq1 = Hash.new(0)
  freq2 = Hash.new(0)

  words1.each { |w| freq1[w] += 1 }
  words2.each { |w| freq2[w] += 1 }

  ans = 0
  freq1.each do |word, cnt|
    ans += 1 if cnt == 1 && freq2[word] == 1
  end
  ans
end
```

## Scala

```scala
object Solution {
    def countWords(words1: Array[String], words2: Array[String]): Int = {
        val cnt1 = scala.collection.mutable.Map[String, Int]().withDefaultValue(0)
        for (w <- words1) cnt1(w) += 1
        val cnt2 = scala.collection.mutable.Map[String, Int]().withDefaultValue(0)
        for (w <- words2) cnt2(w) += 1

        var result = 0
        for ((word, c1) <- cnt1) {
            if (c1 == 1 && cnt2.getOrElse(word, 0) == 1) {
                result += 1
            }
        }
        result
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn count_words(words1: Vec<String>, words2: Vec<String>) -> i32 {
        let mut cnt1: HashMap<&str, i32> = HashMap::new();
        for w in &words1 {
            *cnt1.entry(w.as_str()).or_insert(0) += 1;
        }
        let mut cnt2: HashMap<&str, i32> = HashMap::new();
        for w in &words2 {
            *cnt2.entry(w.as_str()).or_insert(0) += 1;
        }

        let mut ans = 0;
        for (word, &c1) in cnt1.iter() {
            if c1 == 1 {
                if let Some(&c2) = cnt2.get(word) {
                    if c2 == 1 {
                        ans += 1;
                    }
                }
            }
        }
        ans
    }
}
```

## Racket

```racket
#lang racket

(define/contract (count-words words1 words2)
  (-> (listof string?) (listof string?) exact-integer?)
  (let ([h1 (make-hash)]
        [h2 (make-hash)])
    (for ([w words1])
      (hash-set! h1 w (+ 1 (hash-ref h1 w 0))))
    (for ([w words2])
      (hash-set! h2 w (+ 1 (hash-ref h2 w 0))))
    (for/sum ([k (in-hash-keys h1)])
      (if (and (= (hash-ref h1 k) 1)
               (hash-has-key? h2 k)
               (= (hash-ref h2 k) 1))
          1
          0))))
```

## Erlang

```erlang
-module(solution).
-export([count_words/2]).

-spec count_words(Words1 :: [unicode:unicode_binary()], Words2 :: [unicode:unicode_binary()]) -> integer().
count_words(Words1, Words2) ->
    Freq1 = lists:foldl(
        fun(W, Acc) ->
            maps:update_with(W, fun(C) -> C + 1 end, 1, Acc)
        end,
        #{},
        Words1
    ),
    Freq2 = lists:foldl(
        fun(W, Acc) ->
            maps:update_with(W, fun(C) -> C + 1 end, 1, Acc)
        end,
        #{},
        Words2
    ),
    maps:fold(
        fun(Key, Count1, Acc) ->
            case maps:get(Key, Freq2, 0) of
                1 when Count1 =:= 1 -> Acc + 1;
                _ -> Acc
            end
        end,
        0,
        Freq1
    ).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_words(words1 :: [String.t()], words2 :: [String.t()]) :: integer()
  def count_words(words1, words2) do
    freq1 = Enum.frequencies(words1)
    freq2 = Enum.frequencies(words2)

    Enum.reduce(freq1, 0, fn {word, cnt}, acc ->
      if cnt == 1 and Map.get(freq2, word, 0) == 1 do
        acc + 1
      else
        acc
      end
    end)
  end
end
```
