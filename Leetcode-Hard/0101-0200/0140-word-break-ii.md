# 0140. Word Break II

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> dict(wordDict.begin(), wordDict.end());
        int n = s.size();
        unordered_map<int, vector<string>> memo;
        
        function<vector<string>(int)> dfs = [&](int start) -> vector<string> {
            if (memo.count(start)) return memo[start];
            vector<string> res;
            if (start == n) {
                res.push_back("");
                return memo[start] = res;
            }
            for (int end = start + 1; end <= n; ++end) {
                string word = s.substr(start, end - start);
                if (dict.find(word) != dict.end()) {
                    vector<string> suffixes = dfs(end);
                    for (const string& suf : suffixes) {
                        res.push_back(suf.empty() ? word : word + " " + suf);
                    }
                }
            }
            return memo[start] = res;
        };
        
        return dfs(0);
    }
};
```

## Java

```java
class Solution {
    public List<String> wordBreak(String s, List<String> wordDict) {
        Set<String> dict = new HashSet<>(wordDict);
        Map<Integer, List<String>> memo = new HashMap<>();
        return dfs(s, 0, dict, memo);
    }

    private List<String> dfs(String s, int start, Set<String> dict, Map<Integer, List<String>> memo) {
        if (memo.containsKey(start)) {
            return memo.get(start);
        }
        List<String> res = new ArrayList<>();
        if (start == s.length()) {
            res.add("");
            memo.put(start, res);
            return res;
        }
        for (int end = start + 1; end <= s.length(); end++) {
            String word = s.substring(start, end);
            if (!dict.contains(word)) continue;
            List<String> sublist = dfs(s, end, dict, memo);
            for (String sub : sublist) {
                if (sub.isEmpty()) {
                    res.add(word);
                } else {
                    res.add(word + " " + sub);
                }
            }
        }
        memo.put(start, res);
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        word_set = set(wordDict)
        memo = {}

        def dfs(start):
            if start == len(s):
                return ['']
            if start in memo:
                return memo[start]

            sentences = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    following = dfs(end)
                    for sub in following:
                        if sub:
                            sentences.append(word + ' ' + sub)
                        else:
                            sentences.append(word)
            memo[start] = sentences
            return sentences

        return dfs(0)
```

## Python3

```python
class Solution:
    def wordBreak(self, s: str, wordDict):
        from functools import lru_cache

        word_set = set(wordDict)
        n = len(s)

        @lru_cache(maxsize=None)
        def dfs(i):
            if i == n:
                return [""]
            sentences = []
            for j in range(i + 1, n + 1):
                w = s[i:j]
                if w in word_set:
                    following = dfs(j)
                    for sub in following:
                        if sub:
                            sentences.append(w + " " + sub)
                        else:
                            sentences.append(w)
            return sentences

        return dfs(0)
```

## C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char **list;
    int size;
    int capacity;
} StringVector;

static StringVector* dfs(char *s, int start, char **wordDict, int wordDictSize,
                         StringVector dp[], int visited[]) {
    if (visited[start]) return &dp[start];
    visited[start] = 1;

    int n = strlen(s);
    StringVector *vec = &dp[start];
    vec->size = 0;
    vec->capacity = 4;
    vec->list = malloc(vec->capacity * sizeof(char*));

    if (start == n) {
        // base case: empty suffix
        free(vec->list);
        vec->capacity = 1;
        vec->list = malloc(sizeof(char*));
        vec->list[0] = strdup("");
        vec->size = 1;
        return vec;
    }

    for (int i = 0; i < wordDictSize; ++i) {
        char *w = wordDict[i];
        int wlen = strlen(w);
        if (start + wlen > n) continue;
        if (strncmp(s + start, w, wlen) != 0) continue;

        StringVector *nextVec = dfs(s, start + wlen, wordDict, wordDictSize, dp, visited);
        for (int j = 0; j < nextVec->size; ++j) {
            char *suffix = nextVec->list[j];
            int needSpace = suffix[0] != '\0';
            int totalLen = wlen + needSpace + strlen(suffix);
            char *sentence = malloc(totalLen + 1);
            memcpy(sentence, w, wlen);
            if (needSpace) {
                sentence[wlen] = ' ';
                strcpy(sentence + wlen + 1, suffix);
            } else {
                sentence[wlen] = '\0';
            }

            if (vec->size == vec->capacity) {
                vec->capacity <<= 1;
                vec->list = realloc(vec->list, vec->capacity * sizeof(char*));
            }
            vec->list[vec->size++] = sentence;
        }
    }
    return vec;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** wordBreak(char* s, char** wordDict, int wordDictSize, int* returnSize) {
    int len = strlen(s);
    StringVector *dp = calloc(len + 1, sizeof(StringVector));
    int *visited = calloc(len + 1, sizeof(int));

    StringVector *resVec = dfs(s, 0, wordDict, wordDictSize, dp, visited);

    if (resVec->size == 0) {
        *returnSize = 0;
        free(dp);
        free(visited);
        return NULL;
    }

    char **result = resVec->list;   // transfer ownership
    *returnSize = resVec->size;

    /* Cleanup auxiliary structures (except the result strings). */
    for (int i = 1; i <= len; ++i) {
        if (dp[i].list) free(dp[i].list);
    }
    free(dp);
    free(visited);
    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private string _s;
    private HashSet<string> _dict;
    private Dictionary<int, List<string>> _memo;

    public IList<string> WordBreak(string s, IList<string> wordDict) {
        _s = s;
        _dict = new HashSet<string>(wordDict);
        _memo = new Dictionary<int, List<string>>();
        return Backtrack(0);
    }

    private List<string> Backtrack(int start) {
        if (start == _s.Length) {
            return new List<string> { "" };
        }
        if (_memo.ContainsKey(start)) {
            return _memo[start];
        }

        var result = new List<string>();
        for (int end = start + 1; end <= _s.Length; end++) {
            string word = _s.Substring(start, end - start);
            if (_dict.Contains(word)) {
                var sublist = Backtrack(end);
                foreach (var sub in sublist) {
                    string sentence = sub.Length == 0 ? word : word + " " + sub;
                    result.Add(sentence);
                }
            }
        }

        _memo[start] = result;
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {string[]}
 */
var wordBreak = function(s, wordDict) {
    const dict = new Set(wordDict);
    const memo = new Map();

    const dfs = (start) => {
        if (memo.has(start)) return memo.get(start);
        const res = [];
        if (start === s.length) {
            res.push('');
            memo.set(start, res);
            return res;
        }
        for (let end = start + 1; end <= s.length; end++) {
            const word = s.slice(start, end);
            if (!dict.has(word)) continue;
            const sublist = dfs(end);
            for (const sub of sublist) {
                res.push(sub ? word + ' ' + sub : word);
            }
        }
        memo.set(start, res);
        return res;
    };

    return dfs(0);
};
```

## Typescript

```typescript
function wordBreak(s: string, wordDict: string[]): string[] {
    const wordSet = new Set<string>(wordDict);
    const memo = new Map<number, string[]>();

    function dfs(start: number): string[] {
        if (memo.has(start)) return memo.get(start)!;
        if (start === s.length) return [''];

        const sentences: string[] = [];

        for (let end = start + 1; end <= s.length; ++end) {
            const word = s.slice(start, end);
            if (!wordSet.has(word)) continue;

            const following = dfs(end);
            for (const sub of following) {
                sentences.push(sub ? `${word} ${sub}` : word);
            }
        }

        memo.set(start, sentences);
        return sentences;
    }

    return dfs(0);
}
```

## Php

```php
class Solution {
    private string $s;
    private int $len;
    private array $dict;
    private array $memo = [];

    /**
     * @param String $s
     * @param String[] $wordDict
     * @return String[]
     */
    public function wordBreak($s, $wordDict) {
        $this->s = $s;
        $this->len = strlen($s);
        $this->dict = array_flip($wordDict); // O(1) look‑up
        $this->memo = [];
        return $this->dfs(0);
    }

    private function dfs(int $start): array {
        if (isset($this->memo[$start])) {
            return $this->memo[$start];
        }

        $result = [];

        if ($start === $this->len) {
            // empty string denotes a valid termination
            $result[] = "";
        } else {
            for ($end = $start + 1; $end <= $this->len; $end++) {
                $word = substr($this->s, $start, $end - $start);
                if (isset($this->dict[$word])) {
                    $subSentences = $this->dfs($end);
                    foreach ($subSentences as $sub) {
                        if ($sub === "") {
                            $result[] = $word;
                        } else {
                            $result[] = $word . ' ' . $sub;
                        }
                    }
                }
            }
        }

        $this->memo[$start] = $result;
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func wordBreak(_ s: String, _ wordDict: [String]) -> [String] {
        let dict = Set(wordDict)
        let chars = Array(s)
        let n = chars.count
        var memo = [Int: [String]]()
        
        func dfs(_ start: Int) -> [String] {
            if let cached = memo[start] {
                return cached
            }
            var res = [String]()
            if start == n {
                res.append("")
            } else {
                for end in (start + 1)...n {
                    let word = String(chars[start..<end])
                    if dict.contains(word) {
                        let sublist = dfs(end)
                        for sub in sublist {
                            if sub.isEmpty {
                                res.append(word)
                            } else {
                                res.append(word + " " + sub)
                            }
                        }
                    }
                }
            }
            memo[start] = res
            return res
        }
        
        return dfs(0)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun wordBreak(s: String, wordDict: List<String>): List<String> {
        val dict = HashSet(wordDict)
        val memo = HashMap<Int, List<String>>()

        fun dfs(start: Int): List<String> {
            if (memo.containsKey(start)) return memo[start]!!

            val result = mutableListOf<String>()
            if (start == s.length) {
                result.add("")
            } else {
                for (end in start + 1..s.length) {
                    val word = s.substring(start, end)
                    if (dict.contains(word)) {
                        val subSentences = dfs(end)
                        for (sub in subSentences) {
                            if (sub.isEmpty()) {
                                result.add(word)
                            } else {
                                result.add("$word $sub")
                            }
                        }
                    }
                }
            }

            memo[start] = result
            return result
        }

        return dfs(0)
    }
}
```

## Dart

```dart
class Solution {
  List<String> wordBreak(String s, List<String> wordDict) {
    final Set<String> dict = Set.from(wordDict);
    final Map<String, List<String>> memo = {};

    List<String> dfs(String sub) {
      if (memo.containsKey(sub)) return memo[sub]!;
      List<String> res = [];
      if (sub.isEmpty) {
        res.add('');
        memo[sub] = res;
        return res;
      }
      for (int i = 1; i <= sub.length; ++i) {
        String prefix = sub.substring(0, i);
        if (dict.contains(prefix)) {
          List<String> suffixes = dfs(sub.substring(i));
          for (String suffix in suffixes) {
            if (suffix.isEmpty) {
              res.add(prefix);
            } else {
              res.add('$prefix $suffix');
            }
          }
        }
      }
      memo[sub] = res;
      return res;
    }

    return dfs(s);
  }
}
```

## Golang

```go
func wordBreak(s string, wordDict []string) []string {
	dict := make(map[string]bool)
	for _, w := range wordDict {
		dict[w] = true
	}
	memo := make(map[string][]string)

	var dfs func(string) []string
	dfs = func(str string) []string {
		if val, ok := memo[str]; ok {
			return val
		}
		if len(str) == 0 {
			return []string{""}
		}
		var res []string
		for i := 1; i <= len(str); i++ {
			prefix := str[:i]
			if dict[prefix] {
				suffixes := dfs(str[i:])
				for _, suf := range suffixes {
					if suf == "" {
						res = append(res, prefix)
					} else {
						res = append(res, prefix+" "+suf)
					}
				}
			}
		}
		memo[str] = res
		return res
	}

	return dfs(s)
}
```

## Ruby

```ruby
def word_break(s, word_dict)
  dict = {}
  word_dict.each { |w| dict[w] = true }
  n = s.length
  memo = {}

  dfs = lambda do |start|
    return [''] if start == n
    return memo[start] if memo.key?(start)

    res = []
    (start + 1).upto(n) do |i|
      word = s[start...i]
      next unless dict[word]

      sub_sentences = dfs.call(i)
      sub_sentences.each do |sub|
        if sub.empty?
          res << word
        else
          res << "#{word} #{sub}"
        end
      end
    end

    memo[start] = res
  end

  dfs.call(0)
end
```

## Scala

```scala
object Solution {
  def wordBreak(s: String, wordDict: List[String]): List[String] = {
    val dict = wordDict.toSet
    import scala.collection.mutable

    val memo = mutable.Map[Int, List[String]]()

    def dfs(start: Int): List[String] = {
      if (memo.contains(start)) return memo(start)
      if (start == s.length) {
        memo(start) = List("")
        return memo(start)
      }
      var res = List.empty[String]
      for (end <- start + 1 to s.length) {
        val word = s.substring(start, end)
        if (dict.contains(word)) {
          val sublist = dfs(end)
          for (sub <- sublist) {
            val sentence = if (sub.isEmpty) word else word + " " + sub
            res ::= sentence
          }
        }
      }
      memo(start) = res
      res
    }

    dfs(0)
  }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn word_break(s: String, word_dict: Vec<String>) -> Vec<String> {
        let dict: HashSet<String> = word_dict.into_iter().collect();
        let n = s.len();
        let mut memo: Vec<Option<Vec<String>>> = vec![None; n + 1];

        fn dfs(
            i: usize,
            s: &str,
            dict: &HashSet<String>,
            memo: &mut Vec<Option<Vec<String>>>,
        ) -> Vec<String> {
            if let Some(res) = &memo[i] {
                return res.clone();
            }
            let mut result = Vec::new();
            if i == s.len() {
                result.push(String::new());
            } else {
                for j in i + 1..=s.len() {
                    let word = &s[i..j];
                    if dict.contains(word) {
                        let subs = dfs(j, s, dict, memo);
                        for sub in subs {
                            let mut sentence = String::new();
                            sentence.push_str(word);
                            if !sub.is_empty() {
                                sentence.push(' ');
                                sentence.push_str(&sub);
                            }
                            result.push(sentence);
                        }
                    }
                }
            }
            memo[i] = Some(result.clone());
            result
        }

        dfs(0, &s, &dict, &mut memo)
    }
}
```

## Racket

```racket
(define/contract (word-break s wordDict)
  (-> string? (listof string?) (listof string?))
  (let* ((n (string-length s))
         (dict (let ((h (make-hash)))
                 (for ([w wordDict])
                   (hash-set! h w #t))
                 h))
         (memo (make-hash)))
    (define (dfs i)
      (if (= i n)
          (list "")
          (let ((cached (hash-ref memo i #f)))
            (if cached
                cached
                (let ((results '()))
                  (for ([j (in-range (+ i 1) (+ n 1))])
                    (define sub (substring s i j))
                    (when (hash-has-key? dict sub)
                      (for ([suffix (dfs j)])
                        (if (string=? suffix "")
                            (set! results (cons sub results))
                            (set! results (cons (string-append sub " " suffix) results)))))))
                  (hash-set! memo i (reverse results))
                  (hash-ref memo i))))))
    (dfs 0)))
```

## Erlang

```erlang
-module(solution).
-export([word_break/2]).

-spec word_break(S :: unicode:unicode_binary(), WordDict :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
word_break(S, WordDict) ->
    WordMap = maps:from_list([{W, true} || W <- WordDict]),
    {Res, _} = dfs(S, WordMap, #{}),
    Res.

dfs(<<>>, _WordMap, Memo) ->
    {[<<>>], Memo};
dfs(Str, WordMap, Memo) ->
    case maps:find(Str, Memo) of
        {ok, Val} -> {Val, Memo};
        error ->
            Size = byte_size(Str),
            {Results, FinalMemo} = dfs_loop(1, Size, Str, WordMap, Memo, []),
            NewMemo = maps:put(Str, Results, FinalMemo),
            {Results, NewMemo}
    end.

dfs_loop(I, Size, _Str, _WordMap, Memo, Acc) when I > Size ->
    {Acc, Memo};
dfs_loop(I, Size, Str, WordMap, Memo, Acc) ->
    Prefix = binary:part(Str, 0, I),
    case maps:is_key(Prefix, WordMap) of
        true ->
            RestLen = Size - I,
            Rest = binary:part(Str, I, RestLen),
            {SubSentences, Memo1} = dfs(Rest, WordMap, Memo),
            Combined = [ if Sub == <<>> -> Prefix; true -> <<Prefix/binary, " ", Sub/binary>> end || Sub <- SubSentences ],
            dfs_loop(I + 1, Size, Str, WordMap, Memo1, Acc ++ Combined);
        false ->
            dfs_loop(I + 1, Size, Str, WordMap, Memo, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec word_break(s :: String.t(), word_dict :: [String.t()]) :: [String.t()]
  def word_break(s, word_dict) do
    set = MapSet.new(word_dict)
    n = String.length(s)

    # Initialize dp map with empty lists for each index and base case at n
    dp =
      0..n
      |> Enum.reduce(%{}, fn i, acc -> Map.put(acc, i, []) end)
      |> Map.put(n, [""])

    indices = Enum.to_list(0..(n - 1)) |> Enum.reverse()

    final_dp =
      Enum.reduce(indices, dp, fn i, dp_acc ->
        results =
          Enum.reduce((i + 1)..n, [], fn j, res_acc ->
            word = String.slice(s, i, j - i)

            if MapSet.member?(set, word) do
              suffixes = Map.get(dp_acc, j)

              combined =
                Enum.map(suffixes, fn suffix ->
                  if suffix == "" do
                    word
                  else
                    word <> " " <> suffix
                  end
                end)

              res_acc ++ combined
            else
              res_acc
            end
          end)

        Map.put(dp_acc, i, results)
      end)

    Map.get(final_dp, 0)
  end
end
```
