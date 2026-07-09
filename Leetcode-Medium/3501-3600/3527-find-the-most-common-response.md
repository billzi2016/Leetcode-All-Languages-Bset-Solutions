# 3527. Find the Most Common Response

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string findCommonResponse(vector<vector<string>>& responses) {
        unordered_map<string, int> freq;
        for (auto& day : responses) {
            unordered_set<string> uniq;
            for (const string& s : day) {
                uniq.insert(s);
            }
            for (const string& s : uniq) {
                ++freq[s];
            }
        }
        int bestCount = -1;
        string answer;
        for (const auto& kv : freq) {
            if (kv.second > bestCount || (kv.second == bestCount && kv.first < answer)) {
                bestCount = kv.second;
                answer = kv.first;
            }
        }
        return answer;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public String findCommonResponse(List<List<String>> responses) {
        Map<String, Integer> freq = new HashMap<>();
        for (List<String> day : responses) {
            Set<String> seen = new HashSet<>(day);
            for (String resp : seen) {
                freq.put(resp, freq.getOrDefault(resp, 0) + 1);
            }
        }
        String best = "";
        int maxCount = -1;
        for (Map.Entry<String, Integer> e : freq.entrySet()) {
            String s = e.getKey();
            int cnt = e.getValue();
            if (cnt > maxCount || (cnt == maxCount && s.compareTo(best) < 0)) {
                maxCount = cnt;
                best = s;
            }
        }
        return best;
    }
}
```

## Python

```python
class Solution(object):
    def findCommonResponse(self, responses):
        """
        :type responses: List[List[str]]
        :rtype: str
        """
        counts = {}
        for day in responses:
            seen = set(day)
            for resp in seen:
                counts[resp] = counts.get(resp, 0) + 1

        best_resp = None
        best_cnt = -1
        for resp, cnt in counts.items():
            if cnt > best_cnt or (cnt == best_cnt and resp < best_resp):
                best_cnt = cnt
                best_resp = resp
        return best_resp
```

## Python3

```python
from typing import List
from collections import defaultdict

class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        cnt = defaultdict(int)
        for day in responses:
            for resp in set(day):
                cnt[resp] += 1
        best_resp = ""
        best_cnt = -1
        for resp, c in cnt.items():
            if c > best_cnt or (c == best_cnt and resp < best_resp):
                best_cnt = c
                best_resp = resp
        return best_resp
```

## C

```c
#include <stdlib.h>
#include <string.h>

#define HASH_SIZE 200003

typedef struct Node {
    char *key;
    int cnt;
    struct Node *next;
} Node;

static unsigned long hash_str(const char *s) {
    unsigned long h = 5381;
    while (*s) {
        h = (h * 33) ^ (unsigned char)*s++;
    }
    return h;
}

static Node* hashmap_get(Node **table, const char *key) {
    unsigned long idx = hash_str(key) % HASH_SIZE;
    Node *cur = table[idx];
    while (cur) {
        if (strcmp(cur->key, key) == 0) return cur;
        cur = cur->next;
    }
    // not found, create
    Node *node = (Node *)malloc(sizeof(Node));
    node->key = strdup(key);
    node->cnt = 0;
    node->next = table[idx];
    table[idx] = node;
    return node;
}

static int cmp_str(const void *a, const void *b) {
    const char * const *pa = (const char * const *)a;
    const char * const *pb = (const char * const *)b;
    return strcmp(*pa, *pb);
}

char* findCommonResponse(char*** responses, int responsesSize, int* responsesColSize) {
    Node *table[HASH_SIZE] = {0};

    for (int i = 0; i < responsesSize; ++i) {
        int n = responsesColSize[i];
        if (n == 0) continue;
        char **tmp = (char **)malloc(n * sizeof(char*));
        for (int j = 0; j < n; ++j) tmp[j] = responses[i][j];
        qsort(tmp, n, sizeof(char*), cmp_str);
        int k = 0;
        while (k < n) {
            char *cur = tmp[k];
            Node *node = hashmap_get(table, cur);
            node->cnt += 1;   // count this response for the current day
            int l = k + 1;
            while (l < n && strcmp(tmp[l], cur) == 0) ++l;
            k = l;
        }
        free(tmp);
    }

    int bestCnt = -1;
    char *bestStr = NULL;
    for (int i = 0; i < HASH_SIZE; ++i) {
        Node *cur = table[i];
        while (cur) {
            if (cur->cnt > bestCnt ||
               (cur->cnt == bestCnt && strcmp(cur->key, bestStr) < 0)) {
                bestCnt = cur->cnt;
                bestStr = cur->key;
            }
            cur = cur->next;
        }
    }

    return bestStr ? bestStr : NULL;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public string FindCommonResponse(IList<IList<string>> responses) {
        var globalCount = new Dictionary<string, int>();
        foreach (var day in responses) {
            var seenInDay = new HashSet<string>();
            foreach (var resp in day) {
                if (seenInDay.Add(resp)) { // added newly for this day
                    if (globalCount.ContainsKey(resp))
                        globalCount[resp]++;
                    else
                        globalCount[resp] = 1;
                }
            }
        }

        string best = null;
        int bestCnt = -1;
        foreach (var kvp in globalCount) {
            var resp = kvp.Key;
            var cnt = kvp.Value;
            if (cnt > bestCnt || (cnt == bestCnt && String.Compare(resp, best, StringComparison.Ordinal) < 0)) {
                bestCnt = cnt;
                best = resp;
            }
        }

        return best;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[][]} responses
 * @return {string}
 */
var findCommonResponse = function(responses) {
    const counts = new Map();
    for (const day of responses) {
        const seen = new Set();
        for (const r of day) {
            if (!seen.has(r)) {
                seen.add(r);
                counts.set(r, (counts.get(r) || 0) + 1);
            }
        }
    }
    let best = '';
    let bestCount = -1;
    for (const [resp, cnt] of counts.entries()) {
        if (cnt > bestCount || (cnt === bestCount && resp < best)) {
            bestCount = cnt;
            best = resp;
        }
    }
    return best;
};
```

## Typescript

```typescript
function findCommonResponse(responses: string[][]): string {
    const countMap = new Map<string, number>();
    for (const day of responses) {
        const seen = new Set<string>();
        for (const resp of day) {
            if (!seen.has(resp)) {
                seen.add(resp);
                countMap.set(resp, (countMap.get(resp) ?? 0) + 1);
            }
        }
    }
    let bestResp = "";
    let bestCnt = -1;
    for (const [resp, cnt] of countMap.entries()) {
        if (cnt > bestCnt || (cnt === bestCnt && resp < bestResp)) {
            bestCnt = cnt;
            bestResp = resp;
        }
    }
    return bestResp;
}
```

## Php

```php
class Solution {
    /**
     * @param String[][] $responses
     * @return String
     */
    function findCommonResponse($responses) {
        $globalCount = [];
        foreach ($responses as $day) {
            $unique = array_unique($day);
            foreach ($unique as $resp) {
                if (isset($globalCount[$resp])) {
                    $globalCount[$resp]++;
                } else {
                    $globalCount[$resp] = 1;
                }
            }
        }

        $best = '';
        $max = -1;
        foreach ($globalCount as $resp => $cnt) {
            if ($cnt > $max) {
                $max = $cnt;
                $best = $resp;
            } elseif ($cnt == $max && strcmp($resp, $best) < 0) {
                $best = $resp;
            }
        }

        return $best;
    }
}
```

## Swift

```swift
class Solution {
    func findCommonResponse(_ responses: [[String]]) -> String {
        var frequency = [String: Int]()
        
        for day in responses {
            var seen = Set<String>()
            for response in day {
                if !seen.contains(response) {
                    seen.insert(response)
                    frequency[response, default: 0] += 1
                }
            }
        }
        
        var bestResponse = ""
        var maxCount = -1
        
        for (resp, count) in frequency {
            if count > maxCount || (count == maxCount && resp < bestResponse) {
                maxCount = count
                bestResponse = resp
            }
        }
        
        return bestResponse
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findCommonResponse(responses: List<List<String>>): String {
        val countMap = mutableMapOf<String, Int>()
        for (day in responses) {
            val seenInDay = HashSet<String>()
            for (resp in day) {
                if (seenInDay.add(resp)) {
                    countMap[resp] = (countMap[resp] ?: 0) + 1
                }
            }
        }
        var bestResponse = ""
        var bestCount = -1
        for ((response, cnt) in countMap) {
            if (cnt > bestCount || (cnt == bestCount && response < bestResponse)) {
                bestCount = cnt
                bestResponse = response
            }
        }
        return bestResponse
    }
}
```

## Dart

```dart
class Solution {
  String findCommonResponse(List<List<String>> responses) {
    final Map<String, int> freq = {};
    for (var day in responses) {
      final Set<String> seen = {};
      for (var resp in day) {
        if (!seen.contains(resp)) {
          seen.add(resp);
          freq[resp] = (freq[resp] ?? 0) + 1;
        }
      }
    }

    String best = '';
    int bestCount = -1;
    for (var entry in freq.entries) {
      final resp = entry.key;
      final cnt = entry.value;
      if (cnt > bestCount || (cnt == bestCount && resp.compareTo(best) < 0)) {
        bestCount = cnt;
        best = resp;
      }
    }
    return best;
  }
}
```

## Golang

```go
func findCommonResponse(responses [][]string) string {
    // Global count of each unique response across days (duplicates within a day are ignored)
    globalCount := make(map[string]int)

    for _, day := range responses {
        seen := make(map[string]struct{})
        for _, resp := range day {
            if _, ok := seen[resp]; !ok {
                seen[resp] = struct{}{}
                globalCount[resp]++
            }
        }
    }

    // Determine the most common response with lexicographically smallest tie-breaker
    var best string
    maxCnt := -1
    for resp, cnt := range globalCount {
        if cnt > maxCnt || (cnt == maxCnt && resp < best) {
            best = resp
            maxCnt = cnt
        }
    }

    return best
}
```

## Ruby

```ruby
require 'set'

def find_common_response(responses)
  counts = Hash.new(0)
  responses.each do |day|
    day.uniq.each { |r| counts[r] += 1 }
  end
  max_cnt = -1
  result = nil
  counts.each do |resp, cnt|
    if cnt > max_cnt || (cnt == max_cnt && (result.nil? || resp < result))
      max_cnt = cnt
      result = resp
    end
  end
  result
end
```

## Scala

```scala
object Solution {
    def findCommonResponse(responses: List[List[String]]): String = {
        import scala.collection.mutable
        val cnt = mutable.HashMap.empty[String, Int]
        for (day <- responses) {
            val seen = mutable.HashSet.empty[String]
            for (r <- day) {
                if (!seen.contains(r)) {
                    seen.add(r)
                    cnt.update(r, cnt.getOrElse(r, 0) + 1)
                }
            }
        }
        var bestStr = ""
        var bestCnt = -1
        for ((s, c) <- cnt) {
            if (c > bestCnt || (c == bestCnt && s < bestStr)) {
                bestCnt = c
                bestStr = s
            }
        }
        bestStr
    }
}
```

## Rust

```rust
use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn find_common_response(responses: Vec<Vec<String>>) -> String {
        let mut counts: HashMap<String, usize> = HashMap::new();
        for day in &responses {
            let mut seen: HashSet<&str> = HashSet::new();
            for resp in day {
                seen.insert(resp.as_str());
            }
            for s in seen {
                *counts.entry(s.to_string()).or_insert(0) += 1;
            }
        }

        let mut best = String::new();
        let mut best_cnt = 0usize;
        for (k, &v) in counts.iter() {
            if v > best_cnt || (v == best_cnt && k < &best) {
                best_cnt = v;
                best = k.clone();
            }
        }
        best
    }
}
```

## Racket

```racket
(define/contract (find-common-response responses)
  (-> (listof (listof string?)) string?)
  (let ([global-count (make-hash)])
    (for ([day responses])
      (let ([seen (make-hash)])
        (for ([resp day])
          (unless (hash-has-key? seen resp)
            (hash-set! seen resp #t)
            (hash-update! global-count resp add1 0)))))
    (define best "")
    (define best-count -1)
    (for ([k (in-hash-keys global-count)])
      (let* ([cnt (hash-ref global-count k)]
             [better? (or (> cnt best-count)
                          (and (= cnt best-count) (string<? k best)))])
        (when better?
          (set! best k)
          (set! best-count cnt))))
    best))
```

## Erlang

```erlang
-spec find_common_response(Responses :: [[unicode:unicode_binary()]]) -> unicode:unicode_binary().
find_common_response(Responses) ->
    GlobalCount = lists:foldl(fun(Day, GAcc) -> process_day(Day, GAcc) end, #{}, Responses),
    {BestResp,_} = maps:fold(
        fun(Key, Count, {CurKey, CurCount}) ->
            case Count > CurCount of
                true -> {Key, Count};
                false when Count == CurCount ->
                    case binary:compare(Key, CurKey) of
                        lt -> {Key, Count};
                        _  -> {CurKey, CurCount}
                    end;
                false -> {CurKey, CurCount}
            end
        end,
        {<<>>, -1},
        GlobalCount),
    BestResp.

process_day(DayList, GlobalCount) ->
    process_day(DayList, #{}, GlobalCount).

process_day([], _DaySeen, GAcc) -> GAcc;
process_day([Resp|Rest], DaySeen, GAcc) ->
    case maps:is_key(Resp, DaySeen) of
        true ->
            process_day(Rest, DaySeen, GAcc);
        false ->
            NewDaySeen = maps:put(Resp, true, DaySeen),
            Prev = maps:get(Resp, GAcc, 0),
            NewGAcc = maps:put(Resp, Prev + 1, GAcc),
            process_day(Rest, NewDaySeen, NewGAcc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_common_response(responses :: [[String.t]]) :: String.t
  def find_common_response(responses) do
    counts =
      Enum.reduce(responses, %{}, fn day, acc ->
        uniq = MapSet.new(day)

        Enum.reduce(uniq, acc, fn resp, a ->
          Map.update(a, resp, 1, &(&1 + 1))
        end)
      end)

    {best_resp, _} =
      Enum.reduce(counts, {nil, -1}, fn {resp, cnt}, {best, best_cnt} ->
        cond do
          cnt > best_cnt -> {resp, cnt}
          cnt == best_cnt && (best == nil || resp < best) -> {resp, cnt}
          true -> {best, best_cnt}
        end
      end)

    best_resp
  end
end
```
