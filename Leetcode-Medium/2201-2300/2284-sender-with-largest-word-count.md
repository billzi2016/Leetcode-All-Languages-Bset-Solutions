# 2284. Sender With Largest Word Count

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string largestWordCount(vector<string>& messages, vector<string>& senders) {
        unordered_map<string, int> total;
        for (size_t i = 0; i < messages.size(); ++i) {
            int spaces = 0;
            for (char c : messages[i]) if (c == ' ') ++spaces;
            int words = spaces + 1;
            total[senders[i]] += words;
        }
        string bestSender;
        int maxWords = -1;
        for (const auto& p : total) {
            const string& name = p.first;
            int cnt = p.second;
            if (cnt > maxWords || (cnt == maxWords && name > bestSender)) {
                maxWords = cnt;
                bestSender = name;
            }
        }
        return bestSender;
    }
};
```

## Java

```java
class Solution {
    public String largestWordCount(String[] messages, String[] senders) {
        java.util.Map<String, Integer> wordCounts = new java.util.HashMap<>();
        int maxCount = 0;
        String bestSender = "";
        for (int i = 0; i < messages.length; i++) {
            String msg = messages[i];
            // Count words: number of spaces + 1
            int count = 1;
            for (int j = 0; j < msg.length(); j++) {
                if (msg.charAt(j) == ' ') {
                    count++;
                }
            }
            String sender = senders[i];
            int total = wordCounts.getOrDefault(sender, 0) + count;
            wordCounts.put(sender, total);
            if (total > maxCount || (total == maxCount && sender.compareTo(bestSender) > 0)) {
                maxCount = total;
                bestSender = sender;
            }
        }
        return bestSender;
    }
}
```

## Python

```python
class Solution(object):
    def largestWordCount(self, messages, senders):
        """
        :type messages: List[str]
        :type senders: List[str]
        :rtype: str
        """
        counts = {}
        for msg, snd in zip(messages, senders):
            word_cnt = msg.count(' ') + 1
            counts[snd] = counts.get(snd, 0) + word_cnt

        best_sender = ""
        max_cnt = -1
        for snd, cnt in counts.items():
            if cnt > max_cnt or (cnt == max_cnt and snd > best_sender):
                max_cnt = cnt
                best_sender = snd
        return best_sender
```

## Python3

```python
from typing import List
from collections import defaultdict

class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        word_counts = defaultdict(int)
        for msg, sender in zip(messages, senders):
            # number of words is spaces + 1
            cnt = msg.count(' ') + 1
            word_counts[sender] += cnt

        best_sender = ""
        best_count = -1
        for sender, cnt in word_counts.items():
            if cnt > best_count or (cnt == best_count and sender > best_sender):
                best_sender = sender
                best_count = cnt
        return best_sender
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int countWords(const char *s) {
    int cnt = 1;
    while (*s) {
        if (*s == ' ') cnt++;
        s++;
    }
    return cnt;
}

char* largestWordCount(char** messages, int messagesSize, char** senders, int sendersSize) {
    // arrays to store unique sender names and their total word counts
    char **uniq = (char **)malloc(messagesSize * sizeof(char *));
    int *cnts = (int *)calloc(messagesSize, sizeof(int));
    int uniqCnt = 0;

    for (int i = 0; i < messagesSize; ++i) {
        int words = countWords(messages[i]);
        const char *sender = senders[i];
        int idx = -1;
        for (int j = 0; j < uniqCnt; ++j) {
            if (strcmp(uniq[j], sender) == 0) {
                idx = j;
                break;
            }
        }
        if (idx == -1) { // new sender
            uniq[idx = uniqCnt] = strdup(sender);
            cnts[uniqCnt++] = words;
        } else {
            cnts[idx] += words;
        }
    }

    int bestIdx = -1;
    int maxWords = -1;
    for (int i = 0; i < uniqCnt; ++i) {
        if (cnts[i] > maxWords ||
            (cnts[i] == maxWords && strcmp(uniq[i], uniq[bestIdx]) > 0)) {
            maxWords = cnts[i];
            bestIdx = i;
        }
    }

    char *result = strdup(uniq[bestIdx]);

    // clean up temporary allocations
    for (int i = 0; i < uniqCnt; ++i) free(uniq[i]);
    free(uniq);
    free(cnts);

    return result;
}
```

## Csharp

```csharp
public class Solution {
    public string LargestWordCount(string[] messages, string[] senders) {
        var wordCounts = new Dictionary<string, int>();
        for (int i = 0; i < messages.Length; i++) {
            int count = 1;
            foreach (char c in messages[i]) {
                if (c == ' ') count++;
            }
            if (!wordCounts.ContainsKey(senders[i])) {
                wordCounts[senders[i]] = count;
            } else {
                wordCounts[senders[i]] += count;
            }
        }

        string bestSender = "";
        int maxCount = -1;
        foreach (var kvp in wordCounts) {
            if (kvp.Value > maxCount ||
               (kvp.Value == maxCount && string.Compare(kvp.Key, bestSender) > 0)) {
                maxCount = kvp.Value;
                bestSender = kvp.Key;
            }
        }

        return bestSender;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} messages
 * @param {string[]} senders
 * @return {string}
 */
var largestWordCount = function(messages, senders) {
    const countMap = Object.create(null);
    
    for (let i = 0; i < messages.length; ++i) {
        const sender = senders[i];
        // number of words = spaces + 1
        const words = messages[i].split(' ').length;
        if (countMap[sender] === undefined) {
            countMap[sender] = words;
        } else {
            countMap[sender] += words;
        }
    }
    
    let bestSender = '';
    let maxWords = -1;
    for (const sender in countMap) {
        const total = countMap[sender];
        if (total > maxWords || (total === maxWords && sender > bestSender)) {
            maxWords = total;
            bestSender = sender;
        }
    }
    
    return bestSender;
};
```

## Typescript

```typescript
function largestWordCount(messages: string[], senders: string[]): string {
    const wordCounts = new Map<string, number>();
    for (let i = 0; i < messages.length; i++) {
        const count = messages[i].split(' ').length;
        const sender = senders[i];
        wordCounts.set(sender, (wordCounts.get(sender) ?? 0) + count);
    }
    let result = "";
    let maxCount = -1;
    for (const [sender, cnt] of wordCounts.entries()) {
        if (cnt > maxCount || (cnt === maxCount && sender > result)) {
            maxCount = cnt;
            result = sender;
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $messages
     * @param String[] $senders
     * @return String
     */
    function largestWordCount($messages, $senders) {
        $cnt = [];
        $n = count($messages);
        for ($i = 0; $i < $n; ++$i) {
            $sender = $senders[$i];
            $words = substr_count($messages[$i], ' ') + 1;
            if (!isset($cnt[$sender])) {
                $cnt[$sender] = 0;
            }
            $cnt[$sender] += $words;
        }

        $maxCount = -1;
        $result = '';
        foreach ($cnt as $sender => $total) {
            if ($total > $maxCount || ($total == $maxCount && strcmp($sender, $result) > 0)) {
                $maxCount = $total;
                $result = $sender;
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func largestWordCount(_ messages: [String], _ senders: [String]) -> String {
        var countMap = [String: Int]()
        for i in 0..<messages.count {
            let words = messages[i].split(separator: " ").count
            countMap[senders[i], default: 0] += words
        }
        
        var bestSender = ""
        var maxCount = -1
        for (sender, cnt) in countMap {
            if cnt > maxCount || (cnt == maxCount && sender > bestSender) {
                maxCount = cnt
                bestSender = sender
            }
        }
        return bestSender
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun largestWordCount(messages: Array<String>, senders: Array<String>): String {
        val wordCounts = HashMap<String, Int>()
        for (i in messages.indices) {
            val count = messages[i].count { it == ' ' } + 1
            val sender = senders[i]
            wordCounts[sender] = (wordCounts[sender] ?: 0) + count
        }
        var result = ""
        var maxCount = -1
        for ((sender, total) in wordCounts) {
            if (total > maxCount || (total == maxCount && sender > result)) {
                maxCount = total
                result = sender
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  String largestWordCount(List<String> messages, List<String> senders) {
    final Map<String, int> countMap = {};
    for (int i = 0; i < messages.length; i++) {
      int words = messages[i].split(' ').length;
      countMap[senders[i]] = (countMap[senders[i]] ?? 0) + words;
    }

    String bestSender = '';
    int maxWords = -1;
    for (var entry in countMap.entries) {
      if (entry.value > maxWords ||
          (entry.value == maxWords && entry.key.compareTo(bestSender) > 0)) {
        maxWords = entry.value;
        bestSender = entry.key;
      }
    }

    return bestSender;
  }
}
```

## Golang

```go
import "strings"

func largestWordCount(messages []string, senders []string) string {
	counts := make(map[string]int)
	for i, msg := range messages {
		words := strings.Count(msg, " ") + 1
		sender := senders[i]
		counts[sender] += words
	}
	maxCnt := -1
	ans := ""
	for s, c := range counts {
		if c > maxCnt || (c == maxCnt && s > ans) {
			maxCnt = c
			ans = s
		}
	}
	return ans
}
```

## Ruby

```ruby
def largest_word_count(messages, senders)
  counts = Hash.new(0)
  messages.each_with_index do |msg, i|
    word_cnt = msg.count(' ') + 1
    sender = senders[i]
    counts[sender] += word_cnt
  end

  best_sender = ''
  max_words = -1
  counts.each do |sender, cnt|
    if cnt > max_words || (cnt == max_words && sender > best_sender)
      max_words = cnt
      best_sender = sender
    end
  end
  best_sender
end
```

## Scala

```scala
object Solution {
    def largestWordCount(messages: Array[String], senders: Array[String]): String = {
        val wordCounts = scala.collection.mutable.Map[String, Int]().withDefaultValue(0)
        for (i <- messages.indices) {
            val count = messages(i).count(_ == ' ') + 1
            val sender = senders(i)
            wordCounts(sender) = wordCounts(sender) + count
        }
        var bestSender = ""
        var bestCount = -1
        for ((sender, cnt) <- wordCounts) {
            if (cnt > bestCount || (cnt == bestCount && sender > bestSender)) {
                bestCount = cnt
                bestSender = sender
            }
        }
        bestSender
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn largest_word_count(messages: Vec<String>, senders: Vec<String>) -> String {
        let mut counts: HashMap<String, i32> = HashMap::new();
        for (msg, snd) in messages.iter().zip(senders.iter()) {
            let word_cnt = msg.split_whitespace().count() as i32;
            *counts.entry(snd.clone()).or_insert(0) += word_cnt;
        }
        let mut best_sender = String::new();
        let mut best_count: i32 = -1;
        for (sender, &cnt) in counts.iter() {
            if cnt > best_count || (cnt == best_count && sender > &best_sender) {
                best_sender = sender.clone();
                best_count = cnt;
            }
        }
        best_sender
    }
}
```

## Racket

```racket
#lang racket

(require racket/string)
(require racket/hash)

(define/contract (largest-word-count messages senders)
  (-> (listof string?) (listof string?) string?)
  (let ([counts (make-hash)])
    (for ([msg messages] [snd senders])
      (define wc (+ 1 (string-count msg #\space)))
      (hash-update! counts snd (lambda (old) (+ old wc)) wc))
    (define best "")
    (define bestcnt -1)
    (for ([k (in-hash-keys counts)])
      (define cnt (hash-ref counts k))
      (cond [(> cnt bestcnt)
             (set! bestcnt cnt)
             (set! best k)]
            [(= cnt bestcnt)
             (when (string>? k best)
               (set! best k))]))
    best))
```

## Erlang

```erlang
-module(solution).
-export([largest_word_count/2]).

-spec largest_word_count(Messages :: [unicode:unicode_binary()], Senders :: [unicode:unicode_binary()]) -> unicode:unicode_binary().
largest_word_count(Messages, Senders) ->
    Map = build_map(Messages, Senders, #{}),
    {BestSender,_} = lists:foldl(
        fun({S,C}, {CurS, CurC}) ->
            if
                C > CurC -> {S, C};
                C == CurC andalso S > CurS -> {S, C};
                true -> {CurS, CurC}
            end
        end,
        {<<>>, -1},
        maps:to_list(Map)
    ),
    BestSender.

build_map([], [], Map) ->
    Map;
build_map([Msg|Msgs], [Sen|Sens], Map) ->
    WordCount = length(binary:split(Msg, <<" ">>, [global])),
    NewMap = case maps:is_key(Sen, Map) of
        true ->
            Prev = maps:get(Sen, Map),
            maps:put(Sen, Prev + WordCount, Map);
        false ->
            maps:put(Sen, WordCount, Map)
    end,
    build_map(Msgs, Sens, NewMap).
```

## Elixir

```elixir
defmodule Solution do
  @spec largest_word_count(messages :: [String.t()], senders :: [String.t()]) :: String.t()
  def largest_word_count(messages, senders) do
    counts =
      Enum.zip(messages, senders)
      |> Enum.reduce(%{}, fn {msg, sender}, acc ->
        wc = msg |> String.split(" ", trim: true) |> length()
        Map.update(acc, sender, wc, &(&1 + wc))
      end)

    {best_sender, _} = Enum.max_by(counts, fn {sender, cnt} -> {cnt, sender} end)
    best_sender
  end
end
```
