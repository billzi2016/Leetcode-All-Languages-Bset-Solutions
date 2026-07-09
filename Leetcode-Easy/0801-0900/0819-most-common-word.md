# 0819. Most Common Word

## Cpp

```cpp
class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        unordered_set<string> ban(banned.begin(), banned.end());
        unordered_map<string, int> freq;
        string word;
        for (char ch : paragraph) {
            if (isalpha(ch)) {
                word += tolower(ch);
            } else {
                if (!word.empty()) {
                    if (!ban.count(word))
                        ++freq[word];
                    word.clear();
                }
            }
        }
        if (!word.empty() && !ban.count(word))
            ++freq[word];
        string result;
        int maxCount = 0;
        for (const auto& p : freq) {
            if (p.second > maxCount) {
                maxCount = p.second;
                result = p.first;
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
    public String mostCommonWord(String paragraph, String[] banned) {
        Set<String> banSet = new HashSet<>(Arrays.asList(banned));
        Map<String, Integer> countMap = new HashMap<>();
        String cleaned = paragraph.toLowerCase().replaceAll("[!?',;.]", " ");
        String[] words = cleaned.split("\\s+");
        String result = "";
        int maxFreq = 0;
        for (String word : words) {
            if (word.isEmpty() || banSet.contains(word)) continue;
            int freq = countMap.getOrDefault(word, 0) + 1;
            countMap.put(word, freq);
            if (freq > maxFreq) {
                maxFreq = freq;
                result = word;
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        import collections
        # Create a set for O(1) look‑ups of banned words
        banned_set = set(banned)
        # Replace punctuation with spaces and convert to lowercase
        cleaned = []
        for ch in paragraph:
            if ch.isalpha():
                cleaned.append(ch.lower())
            else:
                cleaned.append(' ')
        words = ''.join(cleaned).split()
        freq = collections.Counter()
        max_word, max_count = "", 0
        for w in words:
            if w not in banned_set:
                cnt = freq[w] + 1
                freq[w] = cnt
                if cnt > max_count:
                    max_word, max_count = w, cnt
        return max_word
```

## Python3

```python
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set(banned)
        for ch in "!?',;.":
            paragraph = paragraph.replace(ch, ' ')
        words = paragraph.lower().split()
        freq = {}
        best_word = ''
        best_cnt = 0
        for w in words:
            if w not in banned_set:
                cnt = freq.get(w, 0) + 1
                freq[w] = cnt
                if cnt > best_cnt:
                    best_cnt = cnt
                    best_word = w
        return best_word
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char* mostCommonWord(char* paragraph, char** banned, int bannedSize) {
    // Maximum possible distinct words is limited by paragraph length
    typedef struct {
        char word[101];
        int count;
    } WordCount;

    WordCount words[500];
    int wordCnt = 0;
    int maxIdx = -1;
    int maxFreq = 0;

    char buf[101];
    int idx = 0;
    size_t len = strlen(paragraph);

    for (size_t i = 0; i <= len; ++i) {
        char ch = paragraph[i];
        if (isalpha(ch)) {
            buf[idx++] = tolower(ch);
        } else {
            if (idx > 0) {
                buf[idx] = '\0';
                idx = 0;

                // check banned
                int isBanned = 0;
                for (int b = 0; b < bannedSize; ++b) {
                    if (strcmp(buf, banned[b]) == 0) {
                        isBanned = 1;
                        break;
                    }
                }
                if (!isBanned) {
                    // find or insert
                    int found = -1;
                    for (int w = 0; w < wordCnt; ++w) {
                        if (strcmp(buf, words[w].word) == 0) {
                            found = w;
                            break;
                        }
                    }
                    if (found != -1) {
                        words[found].count++;
                    } else {
                        strcpy(words[wordCnt].word, buf);
                        words[wordCnt].count = 1;
                        found = wordCnt;
                        wordCnt++;
                    }
                    if (words[found].count > maxFreq) {
                        maxFreq = words[found].count;
                        maxIdx = found;
                    }
                }
            }
        }
    }

    // Allocate result
    char* result = NULL;
    if (maxIdx != -1) {
        size_t resLen = strlen(words[maxIdx].word);
        result = (char*)malloc(resLen + 1);
        strcpy(result, words[maxIdx].word);
    }
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public string MostCommonWord(string paragraph, string[] banned)
    {
        var bannedSet = new HashSet<string>(banned);
        var freq = new Dictionary<string, int>();
        var sb = new System.Text.StringBuilder();

        string mostCommon = "";
        int maxCount = 0;

        void ProcessWord()
        {
            if (sb.Length == 0) return;
            string word = sb.ToString();
            sb.Clear();

            if (bannedSet.Contains(word)) return;

            if (freq.TryGetValue(word, out int count))
                freq[word] = ++count;
            else
                freq[word] = 1;

            if (freq[word] > maxCount)
            {
                maxCount = freq[word];
                mostCommon = word;
            }
        }

        foreach (char ch in paragraph)
        {
            if (char.IsLetter(ch))
            {
                sb.Append(char.ToLowerInvariant(ch));
            }
            else
            {
                ProcessWord();
            }
        }

        // process the last word if any
        ProcessWord();

        return mostCommon;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} paragraph
 * @param {string[]} banned
 * @return {string}
 */
var mostCommonWord = function(paragraph, banned) {
    const bannedSet = new Set(banned);
    // Replace punctuation with spaces and convert to lowercase
    const words = paragraph.toLowerCase().replace(/[!?\',;.\"]/g, ' ').split(/\s+/);
    
    const freq = Object.create(null);
    let maxCount = 0;
    let result = '';
    
    for (const w of words) {
        if (!w || bannedSet.has(w)) continue;
        freq[w] = (freq[w] || 0) + 1;
        if (freq[w] > maxCount) {
            maxCount = freq[w];
            result = w;
        }
    }
    
    return result;
};
```

## Typescript

```typescript
function mostCommonWord(paragraph: string, banned: string[]): string {
    const bannedSet = new Set(banned);
    const cleaned = paragraph.replace(/[!?',;.\"]/g, ' ').toLowerCase();
    const words = cleaned.split(/\s+/);
    const freq = new Map<string, number>();
    let maxCount = 0;
    let result = '';
    for (const w of words) {
        if (!w || bannedSet.has(w)) continue;
        const cnt = (freq.get(w) ?? 0) + 1;
        freq.set(w, cnt);
        if (cnt > maxCount) {
            maxCount = cnt;
            result = w;
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $paragraph
     * @param String[] $banned
     * @return String
     */
    function mostCommonWord($paragraph, $banned) {
        // Convert paragraph to lowercase and replace punctuation with spaces
        $lower = strtolower($paragraph);
        $clean = preg_replace("/[!?',;.]/", " ", $lower);

        // Split into words
        $words = preg_split('/\s+/', $clean, -1, PREG_SPLIT_NO_EMPTY);

        // Build banned set for O(1) lookups
        $bannedSet = array_flip($banned);

        $freq = [];
        $maxCount = 0;
        $result = "";

        foreach ($words as $word) {
            if (isset($bannedSet[$word])) {
                continue;
            }
            if (!isset($freq[$word])) {
                $freq[$word] = 0;
            }
            $freq[$word]++;

            if ($freq[$word] > $maxCount) {
                $maxCount = $freq[$word];
                $result = $word;
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func mostCommonWord(_ paragraph: String, _ banned: [String]) -> String {
        let lowercased = paragraph.lowercased()
        var cleaned = ""
        for ch in lowercased {
            if ch.isLetter {
                cleaned.append(ch)
            } else {
                cleaned.append(" ")
            }
        }
        let words = cleaned.split(separator: " ")
        let bannedSet = Set(banned)
        var freq = [String: Int]()
        var result = ""
        var maxCount = 0
        for wSub in words {
            let word = String(wSub)
            if bannedSet.contains(word) { continue }
            let count = (freq[word] ?? 0) + 1
            freq[word] = count
            if count > maxCount {
                maxCount = count
                result = word
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun mostCommonWord(paragraph: String, banned: Array<String>): String {
        val bannedSet = banned.toHashSet()
        val freq = HashMap<String, Int>()
        var maxCount = 0
        var answer = ""
        val sb = StringBuilder()

        for (ch in paragraph) {
            if (ch.isLetter()) {
                sb.append(ch.lowercaseChar())
            } else {
                if (sb.isNotEmpty()) {
                    val word = sb.toString()
                    if (!bannedSet.contains(word)) {
                        val cnt = freq.getOrDefault(word, 0) + 1
                        freq[word] = cnt
                        if (cnt > maxCount) {
                            maxCount = cnt
                            answer = word
                        }
                    }
                    sb.setLength(0)
                }
            }
        }

        // handle the last word if paragraph ends with a letter
        if (sb.isNotEmpty()) {
            val word = sb.toString()
            if (!bannedSet.contains(word)) {
                val cnt = freq.getOrDefault(word, 0) + 1
                freq[word] = cnt
                if (cnt > maxCount) {
                    answer = word
                }
            }
        }

        return answer
    }
}
```

## Dart

```dart
class Solution {
  String mostCommonWord(String paragraph, List<String> banned) {
    final Set<String> banSet = Set.from(banned);
    final Map<String, int> freq = {};
    StringBuffer sb = StringBuffer();
    int maxCount = 0;
    String result = '';

    for (int i = 0; i < paragraph.length; i++) {
      final String ch = paragraph[i];
      if ((ch.codeUnitAt(0) >= 'a'.codeUnitAt(0) && ch.codeUnitAt(0) <= 'z'.codeUnitAt(0)) ||
          (ch.codeUnitAt(0) >= 'A'.codeUnitAt(0) && ch.codeUnitAt(0) <= 'Z'.codeUnitAt(0))) {
        sb.write(ch.toLowerCase());
      } else {
        if (sb.isNotEmpty) {
          final String word = sb.toString();
          if (!banSet.contains(word)) {
            final int cnt = (freq[word] ?? 0) + 1;
            freq[word] = cnt;
            if (cnt > maxCount) {
              maxCount = cnt;
              result = word;
            }
          }
          sb.clear();
        }
      }
    }

    // Handle the last word if there is any
    if (sb.isNotEmpty) {
      final String word = sb.toString();
      if (!banSet.contains(word)) {
        final int cnt = (freq[word] ?? 0) + 1;
        freq[word] = cnt;
        if (cnt > maxCount) {
          maxCount = cnt;
          result = word;
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

import (
	"strings"
	"unicode"
)

func mostCommonWord(paragraph string, banned []string) string {
	bannedSet := make(map[string]struct{}, len(banned))
	for _, w := range banned {
		bannedSet[w] = struct{}{}
	}

	freq := make(map[string]int)
	var sb strings.Builder
	maxCount := 0
	result := ""

	for _, ch := range paragraph {
		if unicode.IsLetter(ch) {
			sb.WriteRune(unicode.ToLower(ch))
		} else {
			if sb.Len() > 0 {
				word := sb.String()
				if _, ok := bannedSet[word]; !ok {
					freq[word]++
					if freq[word] > maxCount {
						maxCount = freq[word]
						result = word
					}
				}
				sb.Reset()
			}
		}
	}

	if sb.Len() > 0 {
		word := sb.String()
		if _, ok := bannedSet[word]; !ok {
			freq[word]++
			if freq[word] > maxCount {
				maxCount = freq[word]
				result = word
			}
		}
	}

	return result
}
```

## Ruby

```ruby
def most_common_word(paragraph, banned)
  require 'set'
  banned_set = Set.new(banned)

  freq = Hash.new(0)
  max_word = ''
  max_count = 0

  cleaned = paragraph.downcase.gsub(/[^a-z]/, ' ')
  cleaned.split.each do |word|
    next if banned_set.include?(word)
    freq[word] += 1
    if freq[word] > max_count
      max_count = freq[word]
      max_word = word
    end
  end

  max_word
end
```

## Scala

```scala
object Solution {
    def mostCommonWord(paragraph: String, banned: Array[String]): String = {
        val bannedSet = banned.toSet
        val cleaned = paragraph.toLowerCase.map { c =>
            if (c.isLetter) c else ' '
        }.mkString
        val words = cleaned.split("\\s+")
        val freq = scala.collection.mutable.Map[String, Int]().withDefaultValue(0)
        var bestWord = ""
        var bestCount = 0
        for (w <- words) {
            if (w.nonEmpty && !bannedSet.contains(w)) {
                val cnt = freq(w) + 1
                freq.update(w, cnt)
                if (cnt > bestCount) {
                    bestCount = cnt
                    bestWord = w
                }
            }
        }
        bestWord
    }
}
```

## Rust

```rust
use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn most_common_word(paragraph: String, banned: Vec<String>) -> String {
        let banned_set: HashSet<String> = banned.into_iter().collect();

        // Replace non‑letters with spaces and convert to lowercase
        let cleaned: String = paragraph
            .chars()
            .map(|c| if c.is_ascii_alphabetic() { c.to_ascii_lowercase() } else { ' ' })
            .collect();

        // Count frequencies of non‑banned words
        let mut freq: HashMap<String, usize> = HashMap::new();
        for word in cleaned.split_whitespace() {
            if !banned_set.contains(word) {
                *freq.entry(word.to_string()).or_insert(0) += 1;
            }
        }

        // Find the word with maximum frequency
        let mut answer = String::new();
        let mut max_cnt = 0usize;
        for (word, &cnt) in freq.iter() {
            if cnt > max_cnt {
                max_cnt = cnt;
                answer = word.clone();
            }
        }
        answer
    }
}
```

## Racket

```racket
(define/contract (most-common-word paragraph banned)
  (-> string? (listof string?) string?)
  (let* ((banned-set
          (let ((h (make-hash)))
            (for ([w banned])
              (hash-set! h w #t))
            h))
         (cleaned
          (list->string
           (map (lambda (c)
                  (if (char-alphabetic? c)
                      (char-downcase c)
                      #\space))
                (string->list paragraph))))
         (words
          (filter (lambda (w) (not (string=? w "")))
                  (regexp-split #px"\\s+" cleaned)))
         (freq (make-hash))
         (best-word "")
         (best-count 0))
    (for ([w words])
      (unless (hash-has-key? banned-set w)
        (let ((cnt (+ 1 (hash-ref freq w 0))))
          (hash-set! freq w cnt)
          (when (> cnt best-count)
            (set! best-count cnt)
            (set! best-word w)))))
    best-word))
```

## Erlang

```erlang
-spec most_common_word(Paragraph :: unicode:unicode_binary(), Banned :: [unicode:unicode_binary()]) -> unicode:unicode_binary().
most_common_word(Paragraph, Banned) ->
    BannedMap = maps:from_keys(Banned, true),
    Cleaned = re:replace(Paragraph, "[^a-zA-Z]+", " ", [{return, binary}, global]),
    Lower = unicode:characters_to_binary(string:to_lower(unicode:characters_to_list(Cleaned))),
    Words = binary:split(Lower, <<" ">>, [global, trim_all]),
    Counts = lists:foldl(
        fun(W, Acc) ->
            case maps:is_key(W, BannedMap) of
                true -> Acc;
                false ->
                    NewCnt = maps:get(W, Acc, 0) + 1,
                    maps:put(W, NewCnt, Acc)
            end
        end,
        #{},
        Words),
    {Result, _} = maps:fold(
        fun(K, V, {CurK, CurV}) ->
            if V > CurV -> {K, V}; true -> {CurK, CurV} end
        end,
        {"", 0},
        Counts),
    Result.
```

## Elixir

```elixir
defmodule Solution do
  @spec most_common_word(paragraph :: String.t(), banned :: [String.t()]) :: String.t()
  def most_common_word(paragraph, banned) do
    cleaned =
      paragraph
      |> String.replace(~r/[!?\',;.\"]/, " ")
      |> String.downcase()

    words = String.split(cleaned, ~r/\s+/, trim: true)

    banned_set = MapSet.new(banned)

    freq =
      Enum.reduce(words, %{}, fn word, acc ->
        if MapSet.member?(banned_set, word) do
          acc
        else
          Map.update(acc, word, 1, &(&1 + 1))
        end
      end)

    {result, _} = Enum.max_by(freq, fn {_word, count} -> count end)
    result
  end
end
```
