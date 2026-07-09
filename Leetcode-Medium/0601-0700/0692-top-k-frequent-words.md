# 0692. Top K Frequent Words

## Cpp

```cpp
class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> freq;
        for (const string& w : words) ++freq[w];
        
        vector<string> candidates;
        candidates.reserve(freq.size());
        for (const auto& p : freq) candidates.push_back(p.first);
        
        sort(candidates.begin(), candidates.end(),
            [&](const string& a, const string& b) {
                if (freq[a] != freq[b]) return freq[a] > freq[b];
                return a < b;
            });
        
        candidates.resize(k);
        return candidates;
    }
};
```

## Java

```java
class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> freqMap = new HashMap<>();
        for (String w : words) {
            freqMap.put(w, freqMap.getOrDefault(w, 0) + 1);
        }

        PriorityQueue<String> heap = new PriorityQueue<>((a, b) -> {
            int fa = freqMap.get(a);
            int fb = freqMap.get(b);
            if (fa != fb) return Integer.compare(fa, fb); // lower frequency first
            return b.compareTo(a); // higher lexicographical order first
        });

        for (String word : freqMap.keySet()) {
            heap.offer(word);
            if (heap.size() > k) {
                heap.poll();
            }
        }

        List<String> result = new ArrayList<>();
        while (!heap.isEmpty()) {
            result.add(heap.poll());
        }
        Collections.reverse(result);
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        from collections import Counter
        freq = Counter(words)
        # Sort by descending frequency and then lexicographically ascending
        sorted_words = sorted(freq.keys(), key=lambda w: (-freq[w], w))
        return sorted_words[:k]
```

## Python3

```python
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        return sorted(freq.keys(), key=lambda w: (-freq[w], w))[:k]
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    char *word;
    int count;
} WordFreq;

/* Comparator for qsort:
   - Higher frequency first.
   - If frequencies equal, lexicographically smaller word first.
*/
static int cmp(const void *a, const void *b) {
    const WordFreq *wa = (const WordFreq *)a;
    const WordFreq *wb = (const WordFreq *)b;
    if (wa->count != wb->count)
        return wb->count - wa->count;          // descending frequency
    return strcmp(wa->word, wb->word);         // ascending lexicographic
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** topKFrequent(char** words, int wordsSize, int k, int* returnSize) {
    if (wordsSize == 0 || k <= 0) {
        *returnSize = 0;
        return NULL;
    }

    // Allocate space for unique words (worst case: all are unique)
    WordFreq *uniq = (WordFreq *)malloc(wordsSize * sizeof(WordFreq));
    int uniqCount = 0;

    // Build frequency map using linear search (acceptable for n <= 500)
    for (int i = 0; i < wordsSize; ++i) {
        char *w = words[i];
        int found = -1;
        for (int j = 0; j < uniqCount; ++j) {
            if (strcmp(uniq[j].word, w) == 0) {
                found = j;
                break;
            }
        }
        if (found != -1) {
            uniq[found].count += 1;
        } else {
            uniq[uniqCount].word = w;
            uniq[uniqCount].count = 1;
            ++uniqCount;
        }
    }

    // Sort according to frequency and lexicographic order
    qsort(uniq, uniqCount, sizeof(WordFreq), cmp);

    // Prepare result array
    char **result = (char **)malloc(k * sizeof(char *));
    for (int i = 0; i < k; ++i) {
        result[i] = uniq[i].word;
    }

    *returnSize = k;

    free(uniq);
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public IList<string> TopKFrequent(string[] words, int k) {
        var freq = new Dictionary<string, int>();
        foreach (var w in words) {
            if (!freq.ContainsKey(w)) freq[w] = 0;
            freq[w]++;
        }
        
        var list = new List<string>(freq.Keys);
        list.Sort((a, b) => {
            int cmp = freq[b].CompareTo(freq[a]); // higher frequency first
            return cmp != 0 ? cmp : a.CompareTo(b); // lexicographically smaller first
        });
        
        return list.GetRange(0, k);
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @param {number} k
 * @return {string[]}
 */
var topKFrequent = function(words, k) {
    const freqMap = new Map();
    for (const w of words) {
        freqMap.set(w, (freqMap.get(w) || 0) + 1);
    }
    const uniqueWords = Array.from(freqMap.keys());
    uniqueWords.sort((a, b) => {
        const diff = freqMap.get(b) - freqMap.get(a);
        if (diff !== 0) return diff;
        return a < b ? -1 : a > b ? 1 : 0;
    });
    return uniqueWords.slice(0, k);
};
```

## Typescript

```typescript
function topKFrequent(words: string[], k: number): string[] {
    const freq = new Map<string, number>();
    for (const w of words) {
        freq.set(w, (freq.get(w) ?? 0) + 1);
    }
    const entries = Array.from(freq.entries());
    entries.sort((a, b) => {
        if (b[1] !== a[1]) return b[1] - a[1];
        return a[0] < b[0] ? -1 : a[0] > b[0] ? 1 : 0;
    });
    const result: string[] = [];
    for (let i = 0; i < k; ++i) {
        result.push(entries[i][0]);
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $words
     * @param Integer $k
     * @return String[]
     */
    function topKFrequent($words, $k) {
        $freq = [];
        foreach ($words as $w) {
            if (!isset($freq[$w])) {
                $freq[$w] = 0;
            }
            $freq[$w]++;
        }

        $unique = array_keys($freq);
        usort($unique, function($a, $b) use ($freq) {
            if ($freq[$a] == $freq[$b]) {
                return strcmp($a, $b);
            }
            // higher frequency first
            return $freq[$b] <=> $freq[$a];
        });

        return array_slice($unique, 0, $k);
    }
}
```

## Swift

```swift
class Solution {
    func topKFrequent(_ words: [String], _ k: Int) -> [String] {
        var count = [String: Int]()
        for w in words {
            count[w, default: 0] += 1
        }
        let sortedWords = count.keys.sorted { (a, b) -> Bool in
            if count[a]! == count[b]! {
                return a < b
            } else {
                return count[a]! > count[b]!
            }
        }
        return Array(sortedWords.prefix(k))
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun topKFrequent(words: Array<String>, k: Int): List<String> {
        val freq = HashMap<String, Int>()
        for (w in words) {
            freq[w] = freq.getOrDefault(w, 0) + 1
        }
        val pq = java.util.PriorityQueue<String> { a, b ->
            val fa = freq[a]!!
            val fb = freq[b]!!
            if (fa == fb) {
                // For same frequency, larger lexical order should come first in the min-heap so it gets removed earlier
                b.compareTo(a)
            } else {
                fa - fb // smaller frequency has higher priority (min-heap)
            }
        }
        for (key in freq.keys) {
            pq.offer(key)
            if (pq.size > k) pq.poll()
        }
        val result = mutableListOf<String>()
        while (!pq.isEmpty()) {
            result.add(pq.poll())
        }
        result.reverse()
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<String> topKFrequent(List<String> words, int k) {
    final Map<String, int> freq = {};
    for (final w in words) {
      freq[w] = (freq[w] ?? 0) + 1;
    }

    final List<String> candidates = freq.keys.toList();
    candidates.sort((a, b) {
      final int cmpFreq = freq[b]!.compareTo(freq[a]!);
      if (cmpFreq != 0) return cmpFreq;
      return a.compareTo(b);
    });

    return candidates.sublist(0, k);
  }
}
```

## Golang

```go
import "sort"

func topKFrequent(words []string, k int) []string {
	freq := make(map[string]int)
	for _, w := range words {
		freq[w]++
	}
	uniq := make([]string, 0, len(freq))
	for w := range freq {
		uniq = append(uniq, w)
	}
	sort.Slice(uniq, func(i, j int) bool {
		if freq[uniq[i]] != freq[uniq[j]] {
			return freq[uniq[i]] > freq[uniq[j]]
		}
		return uniq[i] < uniq[j]
	})
	return uniq[:k]
}
```

## Ruby

```ruby
def top_k_frequent(words, k)
  freq = Hash.new(0)
  words.each { |w| freq[w] += 1 }
  sorted = freq.keys.sort do |a, b|
    if freq[a] == freq[b]
      a <=> b
    else
      freq[b] <=> freq[a]
    end
  end
  sorted[0, k]
end
```

## Scala

```scala
object Solution {
    def topKFrequent(words: Array[String], k: Int): List[String] = {
        val freq = scala.collection.mutable.Map.empty[String, Int]
        for (w <- words) {
            freq(w) = freq.getOrElse(w, 0) + 1
        }
        val sorted = freq.toSeq.sortWith { case ((w1, c1), (w2, c2)) =>
            if (c1 != c2) c1 > c2 else w1 < w2
        }
        sorted.take(k).map(_._1).toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn top_k_frequent(words: Vec<String>, k: i32) -> Vec<String> {
        use std::collections::HashMap;
        let mut freq: HashMap<String, usize> = HashMap::new();
        for w in words.iter() {
            *freq.entry(w.clone()).or_insert(0) += 1;
        }
        let mut uniq: Vec<String> = freq.keys().cloned().collect();
        uniq.sort_unstable_by(|a, b| {
            let ca = freq.get(a).unwrap();
            let cb = freq.get(b).unwrap();
            if ca != cb {
                cb.cmp(ca) // higher frequency first
            } else {
                a.cmp(b) // lexicographically smaller first
            }
        });
        uniq.truncate(k as usize);
        uniq
    }
}
```

## Racket

```racket
#lang racket
(require racket/list)

(define/contract (top-k-frequent words k)
  (-> (listof string?) exact-integer? (listof string?))
  (let* ([freq (make-hash)])
    (for ([w words])
      (hash-set! freq w (+ 1 (hash-ref freq w 0))))
    (define pairs
      (hash-map freq (lambda (key val) (cons key val))))
    (define sorted-pairs
      (sort pairs
            (lambda (a b)
              (let ([cnt-a (cdr a)] [cnt-b (cdr b)]
                    [word-a (car a)] [word-b (car b)])
                (or (> cnt-a cnt-b)
                    (and (= cnt-a cnt-b) (string<? word-a word-b)))))))
    (map car (take sorted-pairs k))))
```

## Erlang

```erlang
-spec top_k_frequent(Words :: [unicode:unicode_binary()], K :: integer()) -> [unicode:unicode_binary()].
top_k_frequent(Words, K) ->
    FreqMap = lists:foldl(
        fun(W, Acc) ->
            Count = maps:get(W, Acc, 0),
            maps:put(W, Count + 1, Acc)
        end,
        #{},
        Words
    ),
    Sorted = lists:sort(
        fun({W1, C1}, {W2, C2}) ->
            case C1 =:= C2 of
                true -> W1 < W2;
                false -> C1 > C2
            end
        end,
        maps:to_list(FreqMap)
    ),
    TopK = lists:sublist(Sorted, K),
    [Word || {Word, _} <- TopK].
```

## Elixir

```elixir
defmodule Solution do
  @spec top_k_frequent(words :: [String.t()], k :: integer) :: [String.t()]
  def top_k_frequent(words, k) do
    freq_map =
      Enum.reduce(words, %{}, fn word, acc ->
        Map.update(acc, word, 1, &(&1 + 1))
      end)

    freq_map
    |> Enum.map(fn {word, cnt} -> {word, cnt} end)
    |> Enum.sort_by(fn {word, cnt} -> {-cnt, word} end)
    |> Enum.take(k)
    |> Enum.map(fn {word, _cnt} -> word end)
  end
end
```
