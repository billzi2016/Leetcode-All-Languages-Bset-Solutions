# 1048. Longest String Chain

## Cpp

```cpp
class Solution {
public:
    int longestStrChain(vector<string>& words) {
        sort(words.begin(), words.end(),
             [](const string& a, const string& b){ return a.size() < b.size(); });
        unordered_map<string,int> dp;
        int ans = 1;
        for (const string& w : words) {
            int best = 1;
            for (int i = 0; i < (int)w.size(); ++i) {
                string prev = w.substr(0, i) + w.substr(i + 1);
                auto it = dp.find(prev);
                if (it != dp.end()) {
                    best = max(best, it->second + 1);
                }
            }
            dp[w] = best;
            ans = max(ans, best);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int longestStrChain(String[] words) {
        java.util.Arrays.sort(words, (a, b) -> a.length() - b.length());
        java.util.HashMap<String, Integer> dp = new java.util.HashMap<>();
        int maxLen = 1;
        for (String word : words) {
            int cur = 1;
            for (int i = 0; i < word.length(); i++) {
                String pred = word.substring(0, i) + word.substring(i + 1);
                Integer prev = dp.get(pred);
                if (prev != null) {
                    cur = Math.max(cur, prev + 1);
                }
            }
            dp.put(word, cur);
            maxLen = Math.max(maxLen, cur);
        }
        return maxLen;
    }
}
```

## Python

```python
class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key=len)
        dp = {}
        max_len = 1
        for w in words:
            cur = 1
            for i in range(len(w)):
                pred = w[:i] + w[i+1:]
                if pred in dp:
                    cur = max(cur, dp[pred] + 1)
            dp[w] = cur
            max_len = max(max_len, cur)
        return max_len
```

## Python3

```python
from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp = {}
        ans = 1
        for w in words:
            cur = 1
            for i in range(len(w)):
                pred = w[:i] + w[i+1:]
                if pred in dp:
                    cur = max(cur, dp[pred] + 1)
            dp[w] = cur
            ans = max(ans, cur)
        return ans
```

## C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int cmp_len(const void *a, const void *b) {
    const char *s1 = *(const char **)a;
    const char *s2 = *(const char **)b;
    size_t l1 = strlen(s1);
    size_t l2 = strlen(s2);
    if (l1 != l2) return (l1 < l2) ? -1 : 1;
    return strcmp(s1, s2);
}

static int isPredecessor(const char *shorter, const char *longer) {
    int i = 0, j = 0;
    while (shorter[i] && longer[j]) {
        if (shorter[i] == longer[j]) {
            ++i; ++j;
        } else {
            if (i != j) return 0;   // already skipped one character
            ++j;                     // skip the extra character in longer
        }
    }
    return 1;   // lengths differ by exactly one, so remaining chars are fine
}

int longestStrChain(char** words, int wordsSize) {
    if (wordsSize == 0) return 0;
    qsort(words, (size_t)wordsSize, sizeof(char *), cmp_len);
    
    int *dp = (int *)malloc(sizeof(int) * (size_t)wordsSize);
    int answer = 1;
    for (int i = 0; i < wordsSize; ++i) {
        dp[i] = 1;
        size_t len_i = strlen(words[i]);
        for (int j = 0; j < i; ++j) {
            if ((size_t)strlen(words[j]) + 1 != len_i) continue;
            if (isPredecessor(words[j], words[i])) {
                if (dp[j] + 1 > dp[i]) dp[i] = dp[j] + 1;
            }
        }
        if (dp[i] > answer) answer = dp[i];
    }
    free(dp);
    return answer;
}
```

## Csharp

```csharp
public class Solution
{
    public int LongestStrChain(string[] words)
    {
        Array.Sort(words, (a, b) => a.Length.CompareTo(b.Length));
        var dp = new Dictionary<string, int>();
        int best = 0;

        foreach (var w in words)
        {
            int cur = 1;
            for (int i = 0; i < w.Length; i++)
            {
                string pred = w.Remove(i, 1);
                if (dp.TryGetValue(pred, out int prev))
                {
                    cur = Math.Max(cur, prev + 1);
                }
            }

            if (dp.ContainsKey(w))
                dp[w] = Math.Max(dp[w], cur);
            else
                dp[w] = cur;

            best = Math.Max(best, dp[w]);
        }

        return best;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @return {number}
 */
var longestStrChain = function(words) {
    // Sort words by length (ascending)
    words.sort((a, b) => a.length - b.length);
    
    const dp = new Map(); // word -> longest chain ending with this word
    let maxLen = 1;
    
    for (const w of words) {
        let curBest = 1; // at least the word itself
        
        // Try removing each character to find a predecessor
        for (let i = 0; i < w.length; ++i) {
            const pred = w.slice(0, i) + w.slice(i + 1);
            if (dp.has(pred)) {
                curBest = Math.max(curBest, dp.get(pred) + 1);
            }
        }
        
        dp.set(w, curBest);
        maxLen = Math.max(maxLen, curBest);
    }
    
    return maxLen;
};
```

## Typescript

```typescript
function longestStrChain(words: string[]): number {
    words.sort((a, b) => a.length - b.length);
    const dp = new Map<string, number>();
    let maxLen = 1;
    for (const word of words) {
        let cur = 1;
        for (let i = 0; i < word.length; ++i) {
            const pred = word.slice(0, i) + word.slice(i + 1);
            const prevLen = dp.get(pred);
            if (prevLen !== undefined && prevLen + 1 > cur) {
                cur = prevLen + 1;
            }
        }
        dp.set(word, cur);
        if (cur > maxLen) maxLen = cur;
    }
    return maxLen;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $words
     * @return Integer
     */
    function longestStrChain($words) {
        usort($words, function($a, $b) {
            return strlen($a) - strlen($b);
        });

        $dp = [];
        $maxLen = 1;

        foreach ($words as $word) {
            $cur = 1;
            $len = strlen($word);
            for ($i = 0; $i < $len; $i++) {
                $prev = substr($word, 0, $i) . substr($word, $i + 1);
                if (isset($dp[$prev])) {
                    $cur = max($cur, $dp[$prev] + 1);
                }
            }
            $dp[$word] = $cur;
            if ($cur > $maxLen) {
                $maxLen = $cur;
            }
        }

        return $maxLen;
    }
}
```

## Swift

```swift
class Solution {
    func longestStrChain(_ words: [String]) -> Int {
        let sortedWords = words.sorted { $0.count < $1.count }
        var dp = [String: Int]()
        var result = 1
        
        for word in sortedWords {
            var best = 1
            let chars = Array(word)
            for i in 0..<chars.count {
                var predChars = chars
                predChars.remove(at: i)
                let predecessor = String(predChars)
                if let prevLen = dp[predecessor] {
                    best = max(best, prevLen + 1)
                }
            }
            dp[word] = best
            result = max(result, best)
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestStrChain(words: Array<String>): Int {
        val sorted = words.sortedBy { it.length }
        val dp = HashMap<String, Int>()
        var maxLen = 1
        for (word in sorted) {
            var best = 1
            for (i in word.indices) {
                val predecessor = word.removeRange(i, i + 1)
                val prevChain = dp[predecessor]
                if (prevChain != null && prevChain + 1 > best) {
                    best = prevChain + 1
                }
            }
            dp[word] = best
            if (best > maxLen) maxLen = best
        }
        return maxLen
    }
}
```

## Dart

```dart
class Solution {
  int longestStrChain(List<String> words) {
    words.sort((a, b) => a.length.compareTo(b.length));
    final Map<String, int> dp = {};
    int ans = 1;
    for (final w in words) {
      int best = 1;
      for (int i = 0; i < w.length; i++) {
        String pred = w.substring(0, i) + w.substring(i + 1);
        if (dp.containsKey(pred)) {
          int cand = dp[pred]! + 1;
          if (cand > best) best = cand;
        }
      }
      dp[w] = best;
      if (best > ans) ans = best;
    }
    return ans;
  }
}
```

## Golang

```go
import "sort"

func longestStrChain(words []string) int {
    sort.Slice(words, func(i, j int) bool {
        return len(words[i]) < len(words[j])
    })
    dp := make(map[string]int)
    maxLen := 1
    for _, w := range words {
        best := 1
        for i := 0; i < len(w); i++ {
            pred := w[:i] + w[i+1:]
            if v, ok := dp[pred]; ok && v+1 > best {
                best = v + 1
            }
        }
        dp[w] = best
        if best > maxLen {
            maxLen = best
        }
    }
    return maxLen
}
```

## Ruby

```ruby
def longest_str_chain(words)
  words.sort_by!(&:length)
  dp = {}
  best = 1
  words.each do |word|
    cur = 1
    (0...word.length).each do |i|
      pred = word[0, i] + word[i+1..-1]
      if dp.key?(pred)
        cur = [cur, dp[pred] + 1].max
      end
    end
    dp[word] = cur
    best = [best, cur].max
  end
  best
end
```

## Scala

```scala
object Solution {
    def longestStrChain(words: Array[String]): Int = {
        val sorted = words.sortBy(_.length)
        import scala.collection.mutable
        val dp = mutable.Map.empty[String, Int]
        var answer = 1
        for (w <- sorted) {
            var best = 1
            for (i <- 0 until w.length) {
                val pred = w.substring(0, i) + w.substring(i + 1)
                dp.get(pred).foreach { v =>
                    if (v + 1 > best) best = v + 1
                }
            }
            dp(w) = best
            if (best > answer) answer = best
        }
        answer
    }
}
```

## Rust

```rust
use std::collections::HashMap;

pub struct Solution;

impl Solution {
    pub fn longest_str_chain(words: Vec<String>) -> i32 {
        let mut words = words;
        words.sort_by_key(|w| w.len());
        let mut dp: HashMap<String, i32> = HashMap::new();
        let mut answer = 1i32;

        for word in &words {
            let mut best = 1i32;
            for i in 0..word.len() {
                let mut pred = String::with_capacity(word.len() - 1);
                pred.push_str(&word[0..i]);
                pred.push_str(&word[i + 1..]);
                if let Some(&len) = dp.get(&pred) {
                    best = best.max(len + 1);
                }
            }
            dp.insert(word.clone(), best);
            answer = answer.max(best);
        }

        answer
    }
}
```

## Racket

```racket
(define/contract (longest-str-chain words)
  (-> (listof string?) exact-integer?)
  (let* ((sorted (sort words < #:key string-length))
         (dp (make-hash))
         (maxlen 0))
    (for ([w sorted])
      (define best 1)
      (define len (string-length w))
      (for ([i (in-range len)])
        (define pred (string-append (substring w 0 i) (substring w (+ i 1) len)))
        (when (hash-has-key? dp pred)
          (set! best (max best (+ 1 (hash-ref dp pred))))))
      (hash-set! dp w best)
      (set! maxlen (max maxlen best)))
    maxlen))
```

## Erlang

```erlang
-module(solution).
-export([longest_str_chain/1]).

-spec longest_str_chain(Words :: [unicode:unicode_binary()]) -> integer().
longest_str_chain(Words) ->
    Sorted = lists:sort(fun(W1, W2) -> byte_size(W1) < byte_size(W2) end, Words),
    {_, MaxLen} = lists:foldl(
        fun(Word, {Map, Best}) ->
            MaxPrev = max_pred_len(Word, Map),
            Curr = MaxPrev + 1,
            {maps:put(Word, Curr, Map), max(Best, Curr)}
        end,
        {#{}, 0},
        Sorted),
    MaxLen.

max_pred_len(Word, Map) ->
    Len = byte_size(Word),
    Positions = lists:seq(0, Len - 1),
    lists:foldl(
        fun(I, Acc) ->
            Prefix = binary:part(Word, {0, I}),
            SuffixLen = Len - I - 1,
            Suffix = if
                SuffixLen > 0 -> binary:part(Word, {I + 1, SuffixLen});
                true -> <<>>
            end,
            Pred = <<Prefix/binary, Suffix/binary>>,
            Prev = maps:get(Pred, Map, 0),
            max(Acc, Prev)
        end,
        0,
        Positions).
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_str_chain(words :: [String.t]) :: integer
  def longest_str_chain(words) do
    sorted = Enum.sort_by(words, &String.length/1)

    {max_len, _} =
      Enum.reduce(sorted, {0, %{}}, fn word, {global_max, dp} ->
        len = String.length(word)

        best =
          0..(len - 1)
          |> Enum.reduce(1, fn i, acc ->
            pred = String.slice(word, 0, i) <> String.slice(word, i + 1, len - i - 1)

            case Map.get(dp, pred) do
              nil -> acc
              v when v + 1 > acc -> v + 1
              _ -> acc
            end
          end)

        dp = Map.put(dp, word, best)
        {max(global_max, best), dp}
      end)

    max_len
  end
end
```
