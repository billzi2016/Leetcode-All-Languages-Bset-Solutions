# 0720. Longest Word in Dictionary

## Cpp

```cpp
class Solution {
public:
    string longestWord(vector<string>& words) {
        sort(words.begin(), words.end());
        unordered_set<string> good;
        string ans = "";
        for (const string& w : words) {
            if (w.size() == 1 || good.count(w.substr(0, w.size() - 1))) {
                good.insert(w);
                if (w.size() > ans.size() || (w.size() == ans.size() && w < ans)) {
                    ans = w;
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public String longestWord(String[] words) {
        Set<String> wordSet = new HashSet<>(Arrays.asList(words));
        Arrays.sort(words, (a, b) -> {
            if (a.length() != b.length()) return b.length() - a.length();
            return a.compareTo(b);
        });
        for (String w : words) {
            boolean good = true;
            for (int i = 1; i < w.length(); i++) {
                if (!wordSet.contains(w.substring(0, i))) {
                    good = false;
                    break;
                }
            }
            if (good) return w;
        }
        return "";
    }
}
```

## Python

```python
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # Sort lexicographically so that when lengths are equal,
        # the smaller word comes first.
        words.sort()
        # Set of words that can be built character by character.
        good = set([''])
        ans = ''
        for w in words:
            if w[:-1] in good:          # all prefixes except last char exist
                good.add(w)
                if len(w) > len(ans):
                    ans = w
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def longestWord(self, words: List[str]) -> str:
        word_set = set(words)
        # Sort by descending length and then lexicographically ascending
        for w in sorted(words, key=lambda x: (-len(x), x)):
            if all(w[:i] in word_set for i in range(1, len(w))):
                return w
        return ""
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct TrieNode {
    struct TrieNode *child[26];
    bool isEnd;
} TrieNode;

static TrieNode* newNode(void) {
    return (TrieNode*)calloc(1, sizeof(TrieNode));
}

static void insertWord(TrieNode *root, const char *word) {
    TrieNode *node = root;
    while (*word) {
        int idx = *word - 'a';
        if (!node->child[idx]) node->child[idx] = newNode();
        node = node->child[idx];
        word++;
    }
    node->isEnd = true;
}

static void dfs(TrieNode *node, char *path, int depth,
                char *best, int *bestLen) {
    if (depth > 0 && !node->isEnd) return; // safety

    if (depth > *bestLen ||
        (depth == *bestLen && strcmp(path, best) < 0)) {
        memcpy(best, path, depth);
        best[depth] = '\0';
        *bestLen = depth;
    }

    for (int i = 0; i < 26; ++i) {
        TrieNode *child = node->child[i];
        if (child && child->isEnd) {
            path[depth] = 'a' + i;
            dfs(child, path, depth + 1, best, bestLen);
        }
    }
}

char* longestWord(char** words, int wordsSize) {
    TrieNode *root = newNode();
    for (int i = 0; i < wordsSize; ++i) {
        insertWord(root, words[i]);
    }

    char path[31];
    char best[31] = "";
    int bestLen = 0;

    for (int i = 0; i < 26; ++i) {
        TrieNode *child = root->child[i];
        if (child && child->isEnd) {
            path[0] = 'a' + i;
            dfs(child, path, 1, best, &bestLen);
        }
    }

    char *result = (char*)malloc(bestLen + 1);
    strcpy(result, best);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public string LongestWord(string[] words)
    {
        var wordSet = new HashSet<string>(words);
        string ans = "";
        foreach (var w in words)
        {
            if (w.Length < ans.Length) continue;
            if (w.Length == ans.Length && string.CompareOrdinal(w, ans) >= 0) continue;

            bool ok = true;
            for (int i = 1; i < w.Length; ++i)
            {
                if (!wordSet.Contains(w.Substring(0, i)))
                {
                    ok = false;
                    break;
                }
            }

            if (ok) ans = w;
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @return {string}
 */
var longestWord = function(words) {
    // Sort lexicographically so that for equal lengths the smallest word comes first
    words.sort();
    
    const good = new Set(); // words whose all prefixes are present
    let ans = "";
    
    for (const w of words) {
        if (w.length === 1 || good.has(w.slice(0, -1))) {
            good.add(w);
            if (w.length > ans.length) {
                ans = w;
            }
        }
    }
    
    return ans;
};
```

## Typescript

```typescript
function longestWord(words: string[]): string {
    const wordSet = new Set<string>(words);
    words.sort((a, b) => {
        if (b.length !== a.length) return b.length - a.length;
        return a < b ? -1 : a > b ? 1 : 0;
    });
    for (const w of words) {
        let ok = true;
        for (let i = 1; i < w.length; ++i) {
            if (!wordSet.has(w.substring(0, i))) {
                ok = false;
                break;
            }
        }
        if (ok) return w;
    }
    return "";
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $words
     * @return String
     */
    function longestWord($words) {
        // Build a hash set for O(1) lookups
        $wordSet = array_flip($words);
        $ans = "";
        foreach ($words as $word) {
            $lenW = strlen($word);
            $lenA = strlen($ans);
            if ($lenW < $lenA) {
                continue;
            }
            if ($lenW == $lenA && strcmp($word, $ans) > 0) {
                continue;
            }
            $good = true;
            for ($k = 1; $k < $lenW; $k++) {
                $prefix = substr($word, 0, $k);
                if (!isset($wordSet[$prefix])) {
                    $good = false;
                    break;
                }
            }
            if ($good) {
                $ans = $word;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func longestWord(_ words: [String]) -> String {
        let wordSet = Set(words)
        let sortedWords = words.sorted { (a, b) -> Bool in
            if a.count != b.count {
                return a.count > b.count
            } else {
                return a < b
            }
        }
        
        for word in sortedWords {
            var allPrefixesExist = true
            // Check prefixes of length 1 to word.count - 1
            for i in 1..<word.count {
                let endIndex = word.index(word.startIndex, offsetBy: i)
                let prefix = String(word[..<endIndex])
                if !wordSet.contains(prefix) {
                    allPrefixesExist = false
                    break
                }
            }
            if allPrefixesExist {
                return word
            }
        }
        return ""
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestWord(words: Array<String>): String {
        val sorted = words.sorted()
        val good = HashSet<String>()
        var ans = ""
        for (w in sorted) {
            if (w.length == 1 || good.contains(w.substring(0, w.length - 1))) {
                good.add(w)
                if (w.length > ans.length) {
                    ans = w
                }
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  String longestWord(List<String> words) {
    // Sort by length ascending, then lexicographically.
    words.sort((a, b) {
      if (a.length != b.length) return a.length - b.length;
      return a.compareTo(b);
    });

    final Set<String> good = <String>{};
    String ans = "";

    for (final w in words) {
      if (w.length == 1 || good.contains(w.substring(0, w.length - 1))) {
        good.add(w);
        if (w.length > ans.length) {
          ans = w;
        }
      }
    }

    return ans;
  }
}
```

## Golang

```go
func longestWord(words []string) string {
    wordSet := make(map[string]bool, len(words))
    for _, w := range words {
        wordSet[w] = true
    }

    ans := ""
    for _, w := range words {
        if len(w) < len(ans) || (len(w) == len(ans) && w > ans) {
            continue
        }
        ok := true
        for i := 1; i < len(w); i++ {
            if !wordSet[w[:i]] {
                ok = false
                break
            }
        }
        if ok && (len(w) > len(ans) || (len(w) == len(ans) && w < ans)) {
            ans = w
        }
    }
    return ans
}
```

## Ruby

```ruby
require 'set'

def longest_word(words)
  word_set = Set.new(words)
  words.sort! do |a, b|
    if a.length == b.length
      a <=> b
    else
      b.length <=> a.length
    end
  end

  words.each do |word|
    valid = true
    (1...word.length).each do |i|
      unless word_set.include?(word[0, i])
        valid = false
        break
      end
    end
    return word if valid
  end

  ""
end
```

## Scala

```scala
object Solution {
  def longestWord(words: Array[String]): String = {
    val wordSet = words.toSet
    val sorted = words.sortWith { (a, b) =>
      if (a.length != b.length) a.length > b.length else a < b
    }
    for (w <- sorted) {
      var ok = true
      var i = 1
      while (i < w.length && ok) {
        if (!wordSet.contains(w.substring(0, i))) ok = false
        i += 1
      }
      if (ok) return w
    }
    ""
  }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_word(words: Vec<String>) -> String {
        use std::collections::HashSet;
        let mut set = HashSet::new();
        for w in &words {
            set.insert(w.clone());
        }
        let mut sorted = words.clone();
        sorted.sort_by(|a, b| {
            if a.len() != b.len() {
                b.len().cmp(&a.len())
            } else {
                a.cmp(b)
            }
        });
        for w in sorted {
            let mut ok = true;
            for i in 1..w.len() {
                if !set.contains(&w[0..i]) {
                    ok = false;
                    break;
                }
            }
            if ok {
                return w;
            }
        }
        String::new()
    }
}
```

## Racket

```racket
(define/contract (longest-word words)
  (-> (listof string?) string?)
  (let* ((word-set
          (let ((h (make-hash)))
            (for-each (lambda (w) (hash-set! h w #t)) words)
            h))
         (prefixes-ok?
          (lambda (w)
            (let loop ((k 1))
              (if (> k (string-length w))
                  #t
                  (and (hash-has-key? word-set (substring w 0 k))
                       (loop (+ k 1)))))))
         (better?
          (lambda (cand w)
            (or (> (string-length w) (string-length cand))
                (and (= (string-length w) (string-length cand))
                     (string<? w cand)))))
         (best
          (foldl
           (lambda (w cur)
             (if (prefixes-ok? w)
                 (if (better? cur w) w cur)
                 cur))
           "" ; initial best
           words)))
    best))
```

## Erlang

```erlang
-module(solution).
-export([longest_word/1]).
-spec longest_word(Words :: [unicode:unicode_binary()]) -> unicode:unicode_binary().
longest_word(Words) ->
    WordSet = maps:from_list([{W, true} || W <- Words]),
    lists:foldl(fun(Word, Acc) ->
        LenW = byte_size(Word),
        LenA = byte_size(Acc),
        case (LenW > LenA) orelse (LenW == LenA andalso Word < Acc) of
            true ->
                case all_prefixes_present(Word, WordSet) of
                    true -> Word;
                    false -> Acc
                end;
            false -> Acc
        end
    end, <<>>, Words).

all_prefixes_present(Word, Set) ->
    all_prefixes_present(Word, Set, 1).

all_prefixes_present(_Word, _Set, K) when K >= byte_size(_Word) ->
    true;
all_prefixes_present(Word, Set, K) ->
    Prefix = binary:part(Word, {0, K}),
    case maps:is_key(Prefix, Set) of
        true -> all_prefixes_present(Word, Set, K + 1);
        false -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_word(words :: [String.t]) :: String.t
  def longest_word(words) do
    set = MapSet.new(words)

    words
    |> Enum.sort_by(fn w -> {-String.length(w), w} end)
    |> Enum.find("", fn word -> good_word?(word, set) end)
  end

  defp good_word?(word, set) do
    len = String.length(word)

    1..(len - 1)
    |> Enum.all?(fn i -> MapSet.member?(set, String.slice(word, 0, i)) end)
  end
end
```
