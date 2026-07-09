# 0966. Vowel Spellchecker

## Cpp

```cpp
class Solution {
public:
    vector<string> spellchecker(vector<string>& wordlist, vector<string>& queries) {
        unordered_set<string> exact;
        unordered_map<string, string> capMap;
        unordered_map<string, string> vowelMap;
        
        auto toLower = [](const string& s) {
            string t = s;
            for (char &c : t) c = tolower(c);
            return t;
        };
        auto devowel = [&](const string& s) {
            string t = s;
            for (char &c : t) {
                if (c=='a' || c=='e' || c=='i' || c=='o' || c=='u')
                    c = '*';
            }
            return t;
        };
        
        for (const string& w : wordlist) {
            exact.insert(w);
            string low = toLower(w);
            if (!capMap.count(low)) capMap[low] = w;
            string dev = devowel(low);
            if (!vowelMap.count(dev)) vowelMap[dev] = w;
        }
        
        vector<string> ans;
        ans.reserve(queries.size());
        for (const string& q : queries) {
            if (exact.count(q)) {
                ans.push_back(q);
                continue;
            }
            string low = toLower(q);
            auto itCap = capMap.find(low);
            if (itCap != capMap.end()) {
                ans.push_back(itCap->second);
                continue;
            }
            string dev = devowel(low);
            auto itVow = vowelMap.find(dev);
            if (itVow != vowelMap.end()) {
                ans.push_back(itVow->second);
                continue;
            }
            ans.emplace_back("");
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public String[] spellchecker(String[] wordlist, String[] queries) {
        java.util.Set<String> exact = new java.util.HashSet<>();
        java.util.Map<String, String> lowerMap = new java.util.HashMap<>();
        java.util.Map<String, String> devowelMap = new java.util.HashMap<>();

        for (String w : wordlist) {
            exact.add(w);
            String low = w.toLowerCase();
            lowerMap.putIfAbsent(low, w);
            String devow = devowel(low);
            devowelMap.putIfAbsent(devow, w);
        }

        String[] ans = new String[queries.length];
        for (int i = 0; i < queries.length; i++) {
            String q = queries[i];
            if (exact.contains(q)) {
                ans[i] = q;
                continue;
            }
            String low = q.toLowerCase();
            if (lowerMap.containsKey(low)) {
                ans[i] = lowerMap.get(low);
                continue;
            }
            String devow = devowel(low);
            ans[i] = devowelMap.getOrDefault(devow, "");
        }
        return ans;
    }

    private String devowel(String s) {
        StringBuilder sb = new StringBuilder(s.length());
        for (char c : s.toCharArray()) {
            if (isVowel(c)) {
                sb.append('*');
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }

    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}
```

## Python

```python
class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        exact = set(wordlist)
        
        lower_map = {}
        devowel_map = {}
        vowels = set('aeiou')
        
        def devowel(word):
            return ''.join('*' if ch in vowels else ch for ch in word.lower())
        
        for w in wordlist:
            lw = w.lower()
            if lw not in lower_map:
                lower_map[lw] = w
            dv = devowel(w)
            if dv not in devowel_map:
                devowel_map[dv] = w
        
        res = []
        for q in queries:
            if q in exact:
                res.append(q)
                continue
            lw = q.lower()
            if lw in lower_map:
                res.append(lower_map[lw])
                continue
            dv = devowel(q)
            if dv in devowel_map:
                res.append(devowel_map[dv])
                continue
            res.append("")
        return res
```

## Python3

```python
from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        exact = set(wordlist)
        lower_map = {}
        mask_map = {}

        vowels = set('aeiou')

        def devowel(word: str) -> str:
            return ''.join('*' if ch in vowels else ch for ch in word.lower())

        for w in wordlist:
            lw = w.lower()
            if lw not in lower_map:
                lower_map[lw] = w
            mw = devowel(w)
            if mw not in mask_map:
                mask_map[mw] = w

        result = []
        for q in queries:
            if q in exact:
                result.append(q)
            else:
                lw = q.lower()
                if lw in lower_map:
                    result.append(lower_map[lw])
                else:
                    mq = devowel(q)
                    result.append(mask_map.get(mq, ""))
        return result
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

static int isVowel(char c) {
    c = tolower(c);
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

static char *toLower(const char *s) {
    size_t len = strlen(s);
    char *res = (char *)malloc(len + 1);
    for (size_t i = 0; i < len; ++i) res[i] = tolower((unsigned char)s[i]);
    res[len] = '\0';
    return res;
}

static char *devowel(const char *s) {
    size_t len = strlen(s);
    char *res = (char *)malloc(len + 1);
    for (size_t i = 0; i < len; ++i) {
        char c = tolower((unsigned char)s[i]);
        res[i] = isVowel(c) ? '*' : c;
    }
    res[len] = '\0';
    return res;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** spellchecker(char** wordlist, int wordlistSize, char** queries, int queriesSize, int* returnSize) {
    // Preprocess wordlist
    char **lowerList = (char **)malloc(wordlistSize * sizeof(char *));
    char **devowelList = (char **)malloc(wordlistSize * sizeof(char *));
    for (int i = 0; i < wordlistSize; ++i) {
        lowerList[i] = toLower(wordlist[i]);
        devowelList[i] = devowel(wordlist[i]);
    }

    char **answer = (char **)malloc(queriesSize * sizeof(char *));
    const char *emptyStr = "";

    for (int q = 0; q < queriesSize; ++q) {
        const char *origQuery = queries[q];
        // Exact match
        int found = 0;
        for (int i = 0; i < wordlistSize; ++i) {
            if (strcmp(origQuery, wordlist[i]) == 0) {
                answer[q] = wordlist[i];
                found = 1;
                break;
            }
        }
        if (found) continue;

        // Case-insensitive match
        char *qLower = toLower(origQuery);
        for (int i = 0; i < wordlistSize; ++i) {
            if (strcmp(qLower, lowerList[i]) == 0) {
                answer[q] = wordlist[i];
                found = 1;
                break;
            }
        }
        free(qLower);
        if (found) continue;

        // Vowel error match
        char *qDevowel = devowel(origQuery);
        for (int i = 0; i < wordlistSize; ++i) {
            if (strcmp(qDevowel, devowelList[i]) == 0) {
                answer[q] = wordlist[i];
                found = 1;
                break;
            }
        }
        free(qDevowel);
        if (!found) answer[q] = (char *)emptyStr;
    }

    // Cleanup auxiliary arrays
    for (int i = 0; i < wordlistSize; ++i) {
        free(lowerList[i]);
        free(devowelList[i]);
    }
    free(lowerList);
    free(devowelList);

    *returnSize = queriesSize;
    return answer;
}
```

## Csharp

```csharp
public class Solution {
    public string[] Spellchecker(string[] wordlist, string[] queries) {
        var exact = new HashSet<string>(wordlist);
        var capMap = new Dictionary<string, string>();
        var vowelMap = new Dictionary<string, string>();

        foreach (var w in wordlist) {
            var lower = w.ToLowerInvariant();
            if (!capMap.ContainsKey(lower))
                capMap[lower] = w;

            var devowel = Devowel(lower);
            if (!vowelMap.ContainsKey(devowel))
                vowelMap[devowel] = w;
        }

        var result = new string[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            var q = queries[i];
            if (exact.Contains(q)) {
                result[i] = q;
                continue;
            }

            var lowerQ = q.ToLowerInvariant();
            if (capMap.TryGetValue(lowerQ, out var capMatch)) {
                result[i] = capMatch;
                continue;
            }

            var devowelQ = Devowel(lowerQ);
            if (vowelMap.TryGetValue(devowelQ, out var vowelMatch)) {
                result[i] = vowelMatch;
                continue;
            }

            result[i] = "";
        }
        return result;
    }

    private static string Devowel(string s) {
        char[] arr = s.ToCharArray();
        for (int i = 0; i < arr.Length; i++) {
            if (IsVowel(arr[i]))
                arr[i] = '*';
        }
        return new string(arr);
    }

    private static bool IsVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} wordlist
 * @param {string[]} queries
 * @return {string[]}
 */
var spellchecker = function(wordlist, queries) {
    const exactSet = new Set(wordlist);
    
    const lowerMap = new Map();   // lowercase -> first original word
    const vowelMap = new Map();   // devoweled lowercase -> first original word
    
    const isVowel = (ch) => 'aeiou'.includes(ch);
    const devowel = (s) => s.replace(/[aeiou]/gi, '*');
    
    for (const w of wordlist) {
        const low = w.toLowerCase();
        if (!lowerMap.has(low)) lowerMap.set(low, w);
        const dev = devowel(low);
        if (!vowelMap.has(dev)) vowelMap.set(dev, w);
    }
    
    const result = [];
    for (const q of queries) {
        if (exactSet.has(q)) {
            result.push(q);
            continue;
        }
        const low = q.toLowerCase();
        if (lowerMap.has(low)) {
            result.push(lowerMap.get(low));
            continue;
        }
        const dev = devowel(low);
        if (vowelMap.has(dev)) {
            result.push(vowelMap.get(dev));
        } else {
            result.push("");
        }
    }
    return result;
};
```

## Typescript

```typescript
function spellchecker(wordlist: string[], queries: string[]): string[] {
    const exact = new Set<string>(wordlist);
    const lowerMap = new Map<string, string>();
    const maskMap = new Map<string, string>();

    const isVowel = (c: string) => 'aeiou'.includes(c);

    const devowel = (s: string): string => {
        let res = '';
        for (const ch of s.toLowerCase()) {
            res += isVowel(ch) ? '*' : ch;
        }
        return res;
    };

    for (const w of wordlist) {
        const low = w.toLowerCase();
        if (!lowerMap.has(low)) lowerMap.set(low, w);
        const mask = devowel(w);
        if (!maskMap.has(mask)) maskMap.set(mask, w);
    }

    const answer: string[] = [];
    for (const q of queries) {
        if (exact.has(q)) {
            answer.push(q);
        } else {
            const low = q.toLowerCase();
            if (lowerMap.has(low)) {
                answer.push(lowerMap.get(low)!);
            } else {
                const mask = devowel(q);
                if (maskMap.has(mask)) {
                    answer.push(maskMap.get(mask)!);
                } else {
                    answer.push('');
                }
            }
        }
    }

    return answer;
}
```

## Php

```php
class Solution {
    /**
     * @param String[] $wordlist
     * @param String[] $queries
     * @return String[]
     */
    function spellchecker($wordlist, $queries) {
        $exact = [];
        $caseMap = [];
        $vowelMap = [];

        foreach ($wordlist as $w) {
            // exact match set
            $exact[$w] = true;

            // case-insensitive map (first occurrence)
            $lower = strtolower($w);
            if (!isset($caseMap[$lower])) {
                $caseMap[$lower] = $w;
            }

            // vowel-error map (first occurrence)
            $masked = $this->maskVowels($lower);
            if (!isset($vowelMap[$masked])) {
                $vowelMap[$masked] = $w;
            }
        }

        $result = [];
        foreach ($queries as $q) {
            if (isset($exact[$q])) {
                $result[] = $q;
                continue;
            }

            $lowerQ = strtolower($q);
            if (isset($caseMap[$lowerQ])) {
                $result[] = $caseMap[$lowerQ];
                continue;
            }

            $maskedQ = $this->maskVowels($lowerQ);
            if (isset($vowelMap[$maskedQ])) {
                $result[] = $vowelMap[$maskedQ];
                continue;
            }

            $result[] = "";
        }

        return $result;
    }

    private function maskVowels(string $s): string {
        // replace a, e, i, o, u with '*'
        return preg_replace('/[aeiou]/', '*', $s);
    }
}
```

## Swift

```swift
class Solution {
    func spellchecker(_ wordlist: [String], _ queries: [String]) -> [String] {
        var exactSet = Set<String>()
        var capMap = [String: String]()
        var vowelMap = [String: String]()
        
        for w in wordlist {
            exactSet.insert(w)
            let lower = w.lowercased()
            if capMap[lower] == nil {
                capMap[lower] = w
            }
            let devowelKey = devowel(lower)
            if vowelMap[devowelKey] == nil {
                vowelMap[devowelKey] = w
            }
        }
        
        var result = [String]()
        for q in queries {
            if exactSet.contains(q) {
                result.append(q)
                continue
            }
            let lowerQ = q.lowercased()
            if let cand = capMap[lowerQ] {
                result.append(cand)
                continue
            }
            let devowelQ = devowel(lowerQ)
            if let cand = vowelMap[devowelQ] {
                result.append(cand)
            } else {
                result.append("")
            }
        }
        return result
    }
    
    private func devowel(_ s: String) -> String {
        var res = ""
        for ch in s {
            if "aeiou".contains(ch) {
                res.append("*")
            } else {
                res.append(ch)
            }
        }
        return res
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun spellchecker(wordlist: Array<String>, queries: Array<String>): Array<String> {
        val exact = HashSet<String>()
        val capMap = HashMap<String, String>()
        val vowelMap = HashMap<String, String>()

        for (word in wordlist) {
            exact.add(word)
            val lower = word.lowercase()
            capMap.putIfAbsent(lower, word)
            val devow = devowel(lower)
            vowelMap.putIfAbsent(devow, word)
        }

        val result = ArrayList<String>(queries.size)
        for (q in queries) {
            if (exact.contains(q)) {
                result.add(q)
                continue
            }
            val lowerQ = q.lowercase()
            val capAns = capMap[lowerQ]
            if (capAns != null) {
                result.add(capAns)
                continue
            }
            val devowQ = devowel(lowerQ)
            val vowelAns = vowelMap[devowQ]
            if (vowelAns != null) {
                result.add(vowelAns)
            } else {
                result.add("")
            }
        }

        return result.toTypedArray()
    }

    private fun devowel(s: String): String {
        val sb = StringBuilder()
        for (ch in s) {
            when (ch) {
                'a', 'e', 'i', 'o', 'u' -> sb.append('*')
                else -> sb.append(ch)
            }
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  List<String> spellchecker(List<String> wordlist, List<String> queries) {
    final Set<String> exact = {};
    final Map<String, String> lowerMap = {};
    final Map<String, String> devowelMap = {};

    for (var w in wordlist) {
      exact.add(w);
      final low = w.toLowerCase();
      lowerMap.putIfAbsent(low, () => w);
      final dev = _devowel(low);
      devowelMap.putIfAbsent(dev, () => w);
    }

    List<String> result = [];
    for (var q in queries) {
      if (exact.contains(q)) {
        result.add(q);
        continue;
      }
      final low = q.toLowerCase();
      if (lowerMap.containsKey(low)) {
        result.add(lowerMap[low]!);
        continue;
      }
      final dev = _devowel(low);
      if (devowelMap.containsKey(dev)) {
        result.add(devowelMap[dev]!);
      } else {
        result.add("");
      }
    }
    return result;
  }

  String _devowel(String s) {
    const vowels = 'aeiou';
    final sb = StringBuffer();
    for (int i = 0; i < s.length; i++) {
      var ch = s[i];
      if (vowels.contains(ch)) {
        sb.write('*');
      } else {
        sb.write(ch);
      }
    }
    return sb.toString();
  }
}
```

## Golang

```go
package main

import "strings"

func spellchecker(wordlist []string, queries []string) []string {
	exact := make(map[string]struct{})
	lowerMap := make(map[string]string)
	vowelMap := make(map[string]string)

	for _, w := range wordlist {
		exact[w] = struct{}{}
		lw := strings.ToLower(w)
		if _, ok := lowerMap[lw]; !ok {
			lowerMap[lw] = w
		}
		dv := devowel(lw)
		if _, ok := vowelMap[dv]; !ok {
			vowelMap[dv] = w
		}
	}

	ans := make([]string, len(queries))
	for i, q := range queries {
		if _, ok := exact[q]; ok {
			ans[i] = q
			continue
		}
		lq := strings.ToLower(q)
		if v, ok := lowerMap[lq]; ok {
			ans[i] = v
			continue
		}
		dv := devowel(lq)
		if v, ok := vowelMap[dv]; ok {
			ans[i] = v
			continue
		}
		ans[i] = ""
	}
	return ans
}

func devowel(s string) string {
	var b strings.Builder
	for _, ch := range s {
		if isVowel(ch) {
			b.WriteByte('*')
		} else {
			b.WriteRune(ch)
		}
	}
	return b.String()
}

func isVowel(c rune) bool {
	switch c {
	case 'a', 'e', 'i', 'o', 'u':
		return true
	}
	return false
}
```

## Ruby

```ruby
require 'set'

def spellchecker(wordlist, queries)
  exact = Set.new(wordlist)

  cap_map = {}
  vowel_map = {}

  normalize = ->(s) { s.downcase }
  devowel = ->(s) { s.downcase.gsub(/[aeiou]/i, '*') }

  wordlist.each do |w|
    low = normalize.call(w)
    cap_map[low] ||= w
    dv = devowel.call(w)
    vowel_map[dv] ||= w
  end

  results = []

  queries.each do |q|
    if exact.include?(q)
      results << q
    elsif cap_map.key?(normalize.call(q))
      results << cap_map[normalize.call(q)]
    else
      dv = devowel.call(q)
      if vowel_map.key?(dv)
        results << vowel_map[dv]
      else
        results << ""
      end
    end
  end

  results
end
```

## Scala

```scala
object Solution {
  def spellchecker(wordlist: Array[String], queries: Array[String]): Array[String] = {
    import scala.collection.mutable

    val exact = mutable.HashSet[String]()
    val capMap = mutable.HashMap[String, String]()
    val vowelMap = mutable.HashMap[String, String]()

    def devowel(s: String): String = {
      s.toLowerCase.map {
        case c if "aeiou".contains(c) => '*'
        case c => c
      }.mkString
    }

    for (w <- wordlist) {
      exact.add(w)
      val lower = w.toLowerCase
      if (!capMap.contains(lower)) capMap(lower) = w
      val dev = devowel(w)
      if (!vowelMap.contains(dev)) vowelMap(dev) = w
    }

    queries.map { q =>
      if (exact.contains(q)) q
      else {
        val lower = q.toLowerCase
        capMap.getOrElse(lower, vowelMap.getOrElse(devowel(q), ""))
      }
    }
  }
}
```

## Rust

```rust
use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn spellchecker(wordlist: Vec<String>, queries: Vec<String>) -> Vec<String> {
        // exact match set
        let mut exact = HashSet::new();
        // lowercase to first original word
        let mut lower_map: HashMap<String, String> = HashMap::new();
        // devoweled (lowercase) to first original word
        let mut devowel_map: HashMap<String, String> = HashMap::new();

        for w in &wordlist {
            exact.insert(w.clone());

            let low = w.to_ascii_lowercase();
            lower_map.entry(low.clone()).or_insert_with(|| w.clone());

            let dev = Self::devowel(&low);
            devowel_map.entry(dev).or_insert_with(|| w.clone());
        }

        let mut result = Vec::with_capacity(queries.len());
        for q in queries {
            if exact.contains(&q) {
                result.push(q);
                continue;
            }
            let low = q.to_ascii_lowercase();
            if let Some(orig) = lower_map.get(&low) {
                result.push(orig.clone());
                continue;
            }
            let dev = Self::devowel(&low);
            if let Some(orig) = devowel_map.get(&dev) {
                result.push(orig.clone());
                continue;
            }
            result.push(String::new());
        }

        result
    }

    fn devowel(s: &str) -> String {
        s.chars()
            .map(|c| match c {
                'a' | 'e' | 'i' | 'o' | 'u' => '*',
                _ => c,
            })
            .collect()
    }
}
```

## Racket

```racket
(define/contract (spellchecker wordlist queries)
  (-> (listof string?) (listof string?) (listof string?))
  (let* ((exact      (make-hash))
         (case-map   (make-hash))
         (vowel-map  (make-hash))
         (is-vowel?  (lambda (c) (member c '(#\a #\e #\i #\o #\u))))
         (devowel
          (lambda (s)
            (list->string
             (for/list ([ch (in-string s)])
               (if (is-vowel? ch) #\* ch))))))
    ;; Build hash tables from wordlist preserving first occurrence.
    (for ([w wordlist])
      (hash-set! exact w #t)
      (let ([low (string-downcase w)]
            [dev (devowel (string-downcase w))])
        (unless (hash-has-key? case-map low)
          (hash-set! case-map low w))
        (unless (hash-has-key? vowel-map dev)
          (hash-set! vowel-map dev w))))
    ;; Resolve each query.
    (for/list ([q queries])
      (cond
        [(hash-has-key? exact q) q]
        [else
         (let* ((low       (string-downcase q))
                (case-word (hash-ref case-map low #f)))
           (if case-word
               case-word
               (let* ((dev       (devowel low))
                      (vowel-word (hash-ref vowel-map dev #f)))
                 (or vowel-word ""))))]))))
```

## Erlang

```erlang
-module(solution).
-export([spellchecker/2]).

-spec spellchecker(Wordlist :: [unicode:unicode_binary()], Queries :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
spellchecker(Wordlist, Queries) ->
    {ExactMap, CaseMap, VowelMap} = build_maps(Wordlist),
    lists:map(fun(Q) -> resolve_query(Q, ExactMap, CaseMap, VowelMap) end, Queries).

build_maps(Wordlist) ->
    Empty = #{},
    lists:foldl(
        fun(W, {Exact, Case, Vowel}) ->
            Exact1 = maps:put(W, true, Exact),
            Lower = string:to_lower(W),
            Case1 = case maps:is_key(Lower, Case) of
                        false -> maps:put(Lower, W, Case);
                        true  -> Case
                    end,
            Masked = mask_vowels(Lower),
            Vowel1 = case maps:is_key(Masked, Vowel) of
                         false -> maps:put(Masked, W, Vowel);
                         true  -> Vowel
                     end,
            {Exact1, Case1, Vowel1}
        end,
        {Empty, Empty, Empty},
        Wordlist).

resolve_query(Q, ExactMap, CaseMap, VowelMap) ->
    case maps:is_key(Q, ExactMap) of
        true -> Q;
        false ->
            Lower = string:to_lower(Q),
            case maps:find(Lower, CaseMap) of
                {ok, Orig} -> Orig;
                error ->
                    Masked = mask_vowels(Lower),
                    case maps:find(Masked, VowelMap) of
                        {ok, Orig2} -> Orig2;
                        error -> <<>>
                    end
            end
    end.

mask_vowels(Bin) ->
    List = unicode:characters_to_list(string:to_lower(Bin)),
    Masked = [if is_vowel(C) -> $*; true -> C end || C <- List],
    list_to_binary(Masked).

is_vowel(C) when C == $a; C == $e; C == $i; C == $o; C == $u -> true;
is_vowel(_) -> false.
```

## Elixir

```elixir
defmodule Solution do
  @spec spellchecker([String.t()], [String.t()]) :: [String.t()]
  def spellchecker(wordlist, queries) do
    exact = MapSet.new(wordlist)

    {lower_map, devowel_map} =
      Enum.reduce(wordlist, {%{}, %{}}, fn word, {lmap, dmap} ->
        lower = String.downcase(word)
        lmap = if Map.has_key?(lmap, lower), do: lmap, else: Map.put(lmap, lower, word)

        dev = devowel(lower)
        dmap = if Map.has_key?(dmap, dev), do: dmap, else: Map.put(dmap, dev, word)

        {lmap, dmap}
      end)

    Enum.map(queries, fn q ->
      cond do
        MapSet.member?(exact, q) ->
          q

        true ->
          lower = String.downcase(q)

          case Map.fetch(lower_map, lower) do
            {:ok, w} -> w
            :error ->
              dev = devowel(lower)

              case Map.fetch(devowel_map, dev) do
                {:ok, w2} -> w2
                :error -> ""
              end
          end
      end
    end)
  end

  defp devowel(s) do
    String.replace(s, ~r/[aeiou]/, "*")
  end
end
```
