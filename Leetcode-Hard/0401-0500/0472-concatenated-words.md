# 0472. Concatenated Words

## Cpp

```cpp
class Solution {
public:
    bool canForm(const std::string& word, const std::unordered_set<std::string>& dict) {
        if (dict.empty()) return false;
        int n = word.size();
        std::vector<bool> dp(n + 1, false);
        dp[0] = true;
        for (int i = 1; i <= n; ++i) {
            // when checking the whole word we must ensure at least one split,
            // so start j from 1 if i == n to avoid using the whole word as a single piece.
            int start = (i == n) ? 1 : 0;
            for (int j = start; j < i; ++j) {
                if (!dp[j]) continue;
                if (dict.find(word.substr(j, i - j)) != dict.end()) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[n];
    }

    std::vector<std::string> findAllConcatenatedWordsInADict(std::vector<std::string>& words) {
        // sort by length to ensure building from shorter to longer
        std::sort(words.begin(), words.end(),
                  [](const std::string& a, const std::string& b) { return a.size() < b.size(); });

        std::unordered_set<std::string> dict;
        std::vector<std::string> ans;

        for (const auto& w : words) {
            if (w.empty()) continue; // skip empty strings
            if (canForm(w, dict)) ans.push_back(w);
            dict.insert(w);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        // Sort words by length so that shorter words are processed first
        Arrays.sort(words, (a, b) -> Integer.compare(a.length(), b.length()));
        Set<String> dict = new HashSet<>();
        List<String> result = new ArrayList<>();

        for (String word : words) {
            if (word.isEmpty()) continue;
            if (canForm(word, dict)) {
                result.add(word);
            }
            dict.add(word); // add after checking to avoid using the word itself
        }
        return result;
    }

    private boolean canForm(String word, Set<String> dict) {
        int n = word.length();
        if (dict.isEmpty()) return false;

        boolean[] dp = new boolean[n + 1];
        dp[0] = true;

        for (int i = 1; i <= n; i++) {
            // When checking the whole word, we must use at least two words,
            // so we don't allow using the word itself as a single piece.
            int start = (i == n) ? 1 : 0;
            for (int j = start; j < i; j++) {
                if (!dp[j]) continue;
                if (dict.contains(word.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[n];
    }
}
```

## Python

```python
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # sort by length so that when checking a word, all possible components are already in the set
        words.sort(key=len)
        dict_set = set()
        result = []

        def can_form(word):
            if not dict_set:
                return False
            n = len(word)
            dp = [False] * (n + 1)
            dp[0] = True
            for i in range(1, n + 1):
                for j in range(0, i):
                    if not dp[j]:
                        continue
                    if word[j:i] in dict_set:
                        dp[i] = True
                        break
            return dp[n]

        for w in words:
            if w and can_form(w):
                result.append(w)
            dict_set.add(w)

        return result
```

## Python3

```python
from typing import List

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # Sort words by length so that when checking a word,
        # all possible component words are already in the set.
        words.sort(key=len)
        dict_set = set()
        result = []

        for word in words:
            if not word:
                continue
            if self._can_form(word, dict_set):
                result.append(word)
            dict_set.add(word)

        return result

    def _can_form(self, word: str, dict_set: set) -> bool:
        if not dict_set:
            return False
        n = len(word)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if not dp[j]:
                    continue
                if word[j:i] in dict_set:
                    dp[i] = True
                    break
        return dp[n]
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct TrieNode {
    int isEnd;
    struct TrieNode* child[26];
} TrieNode;

static TrieNode* newNode() {
    TrieNode* node = (TrieNode*)calloc(1, sizeof(TrieNode));
    return node;
}

static void insertWord(TrieNode* root, const char* word) {
    TrieNode* cur = root;
    for (const char* p = word; *p; ++p) {
        int idx = *p - 'a';
        if (!cur->child[idx]) cur->child[idx] = newNode();
        cur = cur->child[idx];
    }
    cur->isEnd = 1;
}

static bool canForm(TrieNode* root, const char* word) {
    int n = (int)strlen(word);
    if (n == 0) return false;
    bool* dp = (bool*)calloc(n + 1, sizeof(bool));
    dp[0] = true;

    for (int i = 0; i < n; ++i) {
        if (!dp[i]) continue;
        TrieNode* cur = root;
        for (int j = i; j < n; ++j) {
            int idx = word[j] - 'a';
            if (!cur->child[idx]) break;
            cur = cur->child[idx];
            if (cur->isEnd) dp[j + 1] = true;
        }
    }

    bool result = dp[n];
    free(dp);
    return result;
}

static int cmpLen(const void* a, const void* b) {
    const char* const *pa = (const char* const *)a;
    const char* const *pb = (const char* const *)b;
    size_t la = strlen(*pa);
    size_t lb = strlen(*pb);
    if (la < lb) return -1;
    if (la > lb) return 1;
    return strcmp(*pa, *pb);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** findAllConcatenatedWordsInADict(char** words, int wordsSize, int* returnSize) {
    char** sorted = (char**)malloc(wordsSize * sizeof(char*));
    memcpy(sorted, words, wordsSize * sizeof(char*));
    qsort(sorted, wordsSize, sizeof(char*), cmpLen);

    TrieNode* root = newNode();

    char** result = (char**)malloc(wordsSize * sizeof(char*));
    int cnt = 0;

    for (int i = 0; i < wordsSize; ++i) {
        const char* w = sorted[i];
        if (canForm(root, w)) {
            result[cnt++] = (char*)w;
        }
        insertWord(root, w);
    }

    free(sorted);
    *returnSize = cnt;
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public IList<string> FindAllConcatenatedWordsInADict(string[] words)
    {
        // Sort words by length so that when we check a word,
        // all possible components are already in the dictionary.
        Array.Sort(words, (a, b) => a.Length.CompareTo(b.Length));

        var dict = new HashSet<string>();
        var result = new List<string>();

        foreach (var word in words)
        {
            if (word.Length == 0) continue;

            if (CanForm(word, dict))
                result.Add(word);

            // Add the current word to dictionary for future checks.
            dict.Add(word);
        }

        return result;
    }

    private bool CanForm(string word, HashSet<string> dict)
    {
        if (dict.Count == 0) return false;

        int n = word.Length;
        var dp = new bool[n + 1];
        dp[0] = true;

        for (int i = 1; i <= n; i++)
        {
            for (int j = 0; j < i; j++)
            {
                if (!dp[j]) continue;

                // If the suffix word[j..i) exists in dict, mark dp[i].
                if (dict.Contains(word.Substring(j, i - j)))
                {
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[n];
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @return {string[]}
 */
var findAllConcatenatedWordsInADict = function(words) {
    // Sort by length so that when checking a word, all possible components are already in the set
    words.sort((a, b) => a.length - b.length);
    
    const dict = new Set();
    const result = [];
    
    for (const w of words) {
        if (w.length === 0) continue;
        if (canForm(w, dict)) {
            result.push(w);
        }
        dict.add(w);
    }
    
    return result;
};

/**
 * Check if word can be formed by concatenating at least two words from dict.
 * @param {string} word
 * @param {Set<string>} dict
 * @return {boolean}
 */
function canForm(word, dict) {
    if (dict.size === 0) return false;
    const n = word.length;
    const dp = new Array(n + 1).fill(false);
    dp[0] = true;
    
    for (let i = 1; i <= n; i++) {
        // For the final position, we must ensure at least two parts,
        // so we skip the case where the whole word is taken as a single component.
        const startJ = (i === n) ? 1 : 0;
        for (let j = startJ; j < i; j++) {
            if (!dp[j]) continue;
            if (dict.has(word.substring(j, i))) {
                dp[i] = true;
                break;
            }
        }
    }
    
    return dp[n];
}
```

## Typescript

```typescript
function findAllConcatenatedWordsInADict(words: string[]): string[] {
    const result: string[] = [];
    const dict = new Set<string>();
    
    // Process words from shortest to longest
    words.sort((a, b) => a.length - b.length);
    
    for (const word of words) {
        if (word.length === 0) continue;
        if (canForm(word, dict)) {
            result.push(word);
        }
        dict.add(word);
    }
    
    return result;
}

function canForm(word: string, dict: Set<string>): boolean {
    if (dict.size === 0) return false;
    const n = word.length;
    const dp = new Array<boolean>(n + 1).fill(false);
    dp[0] = true;
    
    for (let i = 1; i <= n; i++) {
        for (let j = 0; j < i; j++) {
            if (!dp[j]) continue;
            const sub = word.substring(j, i);
            if (dict.has(sub)) {
                dp[i] = true;
                break;
            }
        }
    }
    
    return dp[n];
}
```

## Php

```php
class Solution {
    /**
     * @param String[] $words
     * @return String[]
     */
    function findAllConcatenatedWordsInADict($words) {
        usort($words, function ($a, $b) {
            return strlen($a) <=> strlen($b);
        });

        $dict = [];
        $result = [];

        foreach ($words as $word) {
            if ($word === '') {
                continue;
            }
            if ($this->canForm($word, $dict)) {
                $result[] = $word;
            }
            $dict[$word] = true;
        }

        return $result;
    }

    private function canForm(string $word, array $dict): bool {
        $len = strlen($word);
        if (empty($dict)) {
            return false;
        }

        $dp = array_fill(0, $len + 1, false);
        $dp[0] = true;

        for ($i = 1; $i <= $len; $i++) {
            for ($j = 0; $j < $i; $j++) {
                if (!$dp[$j]) {
                    continue;
                }
                $sub = substr($word, $j, $i - $j);
                if (isset($dict[$sub])) {
                    $dp[$i] = true;
                    break;
                }
            }
        }

        return $dp[$len];
    }
}
```

## Swift

```swift
class Solution {
    func findAllConcatenatedWordsInADict(_ words: [String]) -> [String] {
        // Sort by length so that when checking a word, all possible components are already in the set
        let sortedWords = words.sorted { $0.count < $1.count }
        var dict = Set<String>()
        var result = [String]()
        
        for word in sortedWords {
            if word.isEmpty { continue }
            if canForm(word, using: dict) {
                result.append(word)
            } else {
                dict.insert(word)
            }
        }
        return result
    }
    
    private func canForm(_ word: String, using dict: Set<String>) -> Bool {
        if dict.isEmpty { return false }
        let chars = Array(word)
        let n = chars.count
        var dp = [Bool](repeating: false, count: n + 1)
        dp[0] = true
        
        for i in 1...n {
            // For each possible split point j
            for j in 0..<i {
                if !dp[j] { continue }
                let sub = String(chars[j..<i])
                if dict.contains(sub) {
                    dp[i] = true
                    break
                }
            }
        }
        return dp[n]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findAllConcatenatedWordsInADict(words: Array<String>): List<String> {
        val sorted = words.sortedBy { it.length }
        val dict = HashSet<String>()
        val result = mutableListOf<String>()
        for (word in sorted) {
            if (word.isNotEmpty() && canForm(word, dict)) {
                result.add(word)
            }
            dict.add(word)
        }
        return result
    }

    private fun canForm(word: String, dict: Set<String>): Boolean {
        if (dict.isEmpty()) return false
        val n = word.length
        val dp = BooleanArray(n + 1)
        dp[0] = true
        for (i in 1..n) {
            var j = 0
            while (j < i) {
                if (!dp[j]) {
                    j++
                    continue
                }
                if (dict.contains(word.substring(j, i))) {
                    dp[i] = true
                    break
                }
                j++
            }
        }
        return dp[n]
    }
}
```

## Dart

```dart
class Solution {
  List<String> findAllConcatenatedWordsInADict(List<String> words) {
    // Sort words by length so that shorter words are processed first.
    words.sort((a, b) => a.length.compareTo(b.length));
    final Set<String> dict = <String>{};
    final List<String> result = <String>[];

    for (final String word in words) {
      if (word.isEmpty) continue;
      if (_canForm(word, dict)) {
        result.add(word);
      }
      dict.add(word);
    }

    return result;
  }

  bool _canForm(String word, Set<String> dict) {
    if (dict.isEmpty) return false;

    final int n = word.length;
    final List<bool> dp = List<bool>.filled(n + 1, false);
    dp[0] = true;

    for (int i = 1; i <= n; ++i) {
      for (int j = 0; j < i; ++j) {
        if (!dp[j]) continue;
        if (dict.contains(word.substring(j, i))) {
          dp[i] = true;
          break;
        }
      }
    }

    return dp[n];
  }
}
```

## Golang

```go
import "sort"

func findAllConcatenatedWordsInADict(words []string) []string {
	sort.Slice(words, func(i, j int) bool { return len(words[i]) < len(words[j]) })
	dict := make(map[string]struct{})
	var res []string
	for _, w := range words {
		if w == "" {
			continue
		}
		if canForm(w, dict) {
			res = append(res, w)
		}
		dict[w] = struct{}{}
	}
	return res
}

func canForm(word string, dict map[string]struct{}) bool {
	n := len(word)
	if n == 0 {
		return false
	}
	dp := make([]bool, n+1)
	dp[0] = true
	for i := 1; i <= n; i++ {
		for j := 0; j < i; j++ {
			if !dp[j] {
				continue
			}
			if _, ok := dict[word[j:i]]; ok {
				dp[i] = true
				break
			}
		}
	}
	return dp[n]
}
```

## Ruby

```ruby
def find_all_concatenated_words_in_a_dict(words)
  words.sort_by!(&:length)
  dict = {}
  result = []

  words.each do |word|
    next if word.empty?
    if can_form?(word, dict)
      result << word
    end
    dict[word] = true
  end

  result
end

def can_form?(word, dict)
  return false if dict.empty?

  n = word.length
  dp = Array.new(n + 1, false)
  dp[0] = true

  (1..n).each do |i|
    (0...i).each do |j|
      next unless dp[j]
      if dict.key?(word[j, i - j])
        dp[i] = true
        break
      end
    end
  end

  dp[n]
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable

  def findAllConcatenatedWordsInADict(words: Array[String]): List[String] = {
    val sorted = words.sortBy(_.length)
    val dict = mutable.HashSet.empty[String]
    val result = mutable.ListBuffer.empty[String]

    for (word <- sorted) {
      if (canForm(word, dict)) result += word
      dict += word
    }
    result.toList
  }

  private def canForm(word: String, dict: mutable.Set[String]): Boolean = {
    if (dict.isEmpty) return false
    val n = word.length
    val dp = new Array[Boolean](n + 1)
    dp(0) = true

    for (i <- 1 to n) {
      var jStart = if (i == n) 1 else 0 // ensure at least two words are used
      var j = jStart
      while (j < i && !dp(i)) {
        if (dp(j) && dict.contains(word.substring(j, i))) dp(i) = true
        j += 1
      }
    }
    dp(n)
  }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn find_all_concatenated_words_in_a_dict(words: Vec<String>) -> Vec<String> {
        let mut sorted = words.clone();
        sorted.sort_by_key(|w| w.len());

        let mut dict: HashSet<String> = HashSet::new();
        let mut result: Vec<String> = Vec::new();

        for word in sorted.iter() {
            if word.is_empty() {
                continue;
            }
            let n = word.len();
            let mut dp = vec![false; n + 1];
            dp[0] = true;

            for i in 1..=n {
                for j in 0..i {
                    if !dp[j] {
                        continue;
                    }
                    if dict.contains(&word[j..i]) {
                        dp[i] = true;
                        break;
                    }
                }
            }

            if dp[n] {
                result.push(word.clone());
            }
            dict.insert(word.clone());
        }

        result
    }
}
```

## Racket

```racket
(define/contract (find-all-concatenated-words-in-a-dict words)
  (-> (listof string?) (listof string?))
  (let* ((sorted (sort words < #:key (lambda (s) (string-length s))))
         (dict   (make-hash))
         (result '()))
    (define (can-form? w)
      (let* ((len (string-length w))
             (dp  (make-vector (+ len 1) #f)))
        (vector-set! dp 0 #t)
        (for ([i (in-range 1 (+ len 1))])
          (let loop ((j 0))
            (when (and (not (vector-ref dp i)) (< j i))
              (when (and (vector-ref dp j)
                         (hash-has-key? dict (substring w j i)))
                (vector-set! dp i #t))
              (unless (vector-ref dp i) (loop (+ j 1))))))
        (vector-ref dp len)))
    (for ([w sorted])
      (when (and (> (string-length w) 0) (can-form? w))
        (set! result (cons w result)))
      (hash-set! dict w #t))
    (reverse result)))
```

## Erlang

```erlang
-module(solution).
-export([find_all_concatenated_words_in_a_dict/1]).

-spec find_all_concatenated_words_in_a_dict(Words :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
find_all_concatenated_words_in_a_dict(Words) ->
    Sorted = lists:sort(fun(A, B) -> byte_size(A) < byte_size(B) end, Words),
    process(Sorted, #{}, []).

process([], _Set, Acc) ->
    lists:reverse(Acc);
process([Word | Rest], Set, Acc) ->
    case can_form(Word, Set) of
        true  -> NewSet = maps:put(Word, true, Set),
                 process(Rest, NewSet, [Word | Acc]);
        false -> NewSet = maps:put(Word, true, Set),
                 process(Rest, NewSet, Acc)
    end.

can_form(Word, Set) ->
    Len = byte_size(Word),
    DP0 = #{0 => true},
    can_form_loop(Word, Set, Len, 1, DP0).

can_form_loop(_Word, _Set, Len, I, DPMap) when I > Len ->
    maps:get(Len, DPMap, false);
can_form_loop(Word, Set, Len, I, DPMap) ->
    case find_split(I, Word, Set, DPMap, 0) of
        true  -> NewDP = maps:put(I, true, DPMap);
        false -> NewDP = DPMap
    end,
    can_form_loop(Word, Set, Len, I + 1, NewDP).

find_split(I, _Word, _Set, _DPMap, J) when J >= I ->
    false;
find_split(I, Word, Set, DPMap, J) ->
    case maps:get(J, DPMap, false) of
        true ->
            Sub = binary:part(Word, {J, I - J}),
            if maps:is_key(Sub, Set) -> true;
               true -> find_split(I, Word, Set, DPMap, J + 1)
            end;
        false ->
            find_split(I, Word, Set, DPMap, J + 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_all_concatenated_words_in_a_dict(words :: [String.t()]) :: [String.t()]
  def find_all_concatenated_words_in_a_dict(words) do
    sorted = Enum.sort_by(words, &String.length/1)

    {result, _dict} =
      Enum.reduce(sorted, {[], MapSet.new()}, fn word, {res, dict} ->
        if can_form?(word, dict) do
          {[word | res], MapSet.put(dict, word)}
        else
          {res, MapSet.put(dict, word)}
        end
      end)

    Enum.reverse(result)
  end

  defp can_form?(word, dict) do
    len = String.length(word)
    # dp tuple where index i indicates if prefix of length i can be formed
    dp = :erlang.make_tuple(len + 1, false) |> put_elem(0, true)

    dp =
      Enum.reduce(1..len, dp, fn i, acc ->
        start_j = if i == len, do: 1, else: 0

        found =
          Enum.any?(start_j..(i - 1), fn j ->
            if elem(acc, j) do
              sub = String.slice(word, j, i - j)
              MapSet.member?(dict, sub)
            else
              false
            end
          end)

        put_elem(acc, i, found)
      end)

    elem(dp, len)
  end
end
```
