# 1023. Camelcase Matching

## Cpp

```cpp
class Solution {
public:
    vector<bool> camelMatch(vector<string>& queries, string pattern) {
        vector<bool> ans;
        for (const string& q : queries) {
            int i = 0, j = 0;
            while (i < (int)q.size()) {
                if (j < (int)pattern.size() && q[i] == pattern[j]) {
                    ++i; ++j;
                } else if (isupper(static_cast<unsigned char>(q[i]))) {
                    // uppercase not matching pattern
                    break;
                } else {
                    // lowercase can be skipped
                    ++i;
                }
            }
            bool ok = (j == (int)pattern.size());
            // also need to ensure no remaining unmatched uppercase letters in query
            while (ok && i < (int)q.size()) {
                if (isupper(static_cast<unsigned char>(q[i]))) {
                    ok = false;
                    break;
                }
                ++i;
            }
            ans.push_back(ok);
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<Boolean> camelMatch(String[] queries, String pattern) {
        List<Boolean> result = new ArrayList<>(queries.length);
        for (String query : queries) {
            result.add(matches(query, pattern));
        }
        return result;
    }

    private boolean matches(String query, String pattern) {
        int i = 0, j = 0;
        int n = query.length(), m = pattern.length();
        while (i < n) {
            char qc = query.charAt(i);
            if (j < m && qc == pattern.charAt(j)) {
                i++;
                j++;
            } else if (Character.isLowerCase(qc)) {
                i++; // extra lowercase can be ignored
            } else {
                return false; // uppercase mismatch
            }
        }
        // all remaining characters in pattern must have been matched
        return j == m;
    }
}
```

## Python

```python
class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        res = []
        plen = len(pattern)
        for word in queries:
            i = 0
            ok = True
            for ch in word:
                if i < plen and ch == pattern[i]:
                    i += 1
                elif ch.isupper():
                    ok = False
                    break
            res.append(ok and i == plen)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        m = len(pattern)
        res = []
        for word in queries:
            j = 0
            ok = True
            for ch in word:
                if j < m and ch == pattern[j]:
                    j += 1
                elif ch.isupper():
                    ok = False
                    break
            if ok and j == m:
                res.append(True)
            else:
                res.append(False)
        return res
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>
#include <ctype.h>

static bool match(const char *word, const char *pat) {
    while (*word) {
        if (*pat && *word == *pat) {
            ++word;
            ++pat;
        } else if (islower((unsigned char)*word)) {
            ++word; // can be inserted
        } else {
            return false; // uppercase mismatch
        }
    }
    return *pat == '\0';
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* camelMatch(char** queries, int queriesSize, char* pattern, int* returnSize) {
    bool *ans = (bool *)malloc(sizeof(bool) * queriesSize);
    for (int i = 0; i < queriesSize; ++i) {
        ans[i] = match(queries[i], pattern);
    }
    *returnSize = queriesSize;
    return ans;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<bool> CamelMatch(string[] queries, string pattern) {
        var result = new List<bool>(queries.Length);
        foreach (var query in queries) {
            int pIdx = 0;
            bool match = true;
            foreach (char ch in query) {
                if (pIdx < pattern.Length && ch == pattern[pIdx]) {
                    pIdx++;
                } else if (char.IsUpper(ch)) {
                    match = false;
                    break;
                }
            }
            result.Add(match && pIdx == pattern.Length);
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} queries
 * @param {string} pattern
 * @return {boolean[]}
 */
var camelMatch = function(queries, pattern) {
    const isLower = ch => ch >= 'a' && ch <= 'z';
    
    const matches = (word) => {
        let i = 0, j = 0;
        while (i < word.length) {
            if (j < pattern.length && word[i] === pattern[j]) {
                i++; j++;
            } else {
                if (isLower(word[i])) {
                    i++;
                } else {
                    return false;
                }
            }
        }
        return j === pattern.length;
    };
    
    const result = new Array(queries.length);
    for (let k = 0; k < queries.length; ++k) {
        result[k] = matches(queries[k]);
    }
    return result;
};
```

## Typescript

```typescript
function camelMatch(queries: string[], pattern: string): boolean[] {
    const matches = (query: string, pat: string): boolean => {
        let i = 0, j = 0;
        while (i < query.length) {
            if (j < pat.length && query[i] === pat[j]) {
                i++;
                j++;
            } else if (query[i] === query[i].toLowerCase()) {
                i++;
            } else {
                return false;
            }
        }
        return j === pat.length;
    };
    
    const result: boolean[] = [];
    for (const q of queries) {
        result.push(matches(q, pattern));
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $queries
     * @param String $pattern
     * @return Boolean[]
     */
    function camelMatch($queries, $pattern) {
        $pLen = strlen($pattern);
        $result = [];

        foreach ($queries as $query) {
            $i = 0;
            $j = 0;
            $qLen = strlen($query);
            $ok = true;

            while ($i < $qLen) {
                if ($j < $pLen && $query[$i] === $pattern[$j]) {
                    $i++;
                    $j++;
                } elseif (ctype_upper($query[$i])) {
                    $ok = false;
                    break;
                } else {
                    $i++;
                }
            }

            $result[] = ($ok && $j == $pLen);
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func camelMatch(_ queries: [String], _ pattern: String) -> [Bool] {
        let p = Array(pattern)
        return queries.map { query in
            let q = Array(query)
            var i = 0, j = 0
            while i < q.count && j < p.count {
                if q[i] == p[j] {
                    i += 1
                    j += 1
                } else {
                    if q[i].isUppercase { break }
                    i += 1
                }
            }
            // If pattern not fully matched, fail
            if j != p.count { return false }
            // Remaining characters in query must be lowercase
            while i < q.count {
                if q[i].isUppercase { return false }
                i += 1
            }
            return true
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun camelMatch(queries: Array<String>, pattern: String): List<Boolean> {
        val res = BooleanArray(queries.size)
        for (i in queries.indices) {
            res[i] = matches(queries[i], pattern)
        }
        return res.toList()
    }

    private fun matches(word: String, pattern: String): Boolean {
        var i = 0
        var j = 0
        val n = word.length
        val m = pattern.length
        while (i < n && j < m) {
            val wc = word[i]
            val pc = pattern[j]
            if (wc == pc) {
                i++; j++
            } else if (wc.isLowerCase()) {
                i++
            } else {
                return false
            }
        }
        if (j < m) return false
        while (i < n) {
            if (word[i].isUpperCase()) return false
            i++
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  List<bool> camelMatch(List<String> queries, String pattern) {
    bool matches(String query) {
      int i = 0;
      int j = 0;
      while (i < query.length) {
        if (j < pattern.length && query[i] == pattern[j]) {
          i++;
          j++;
        } else {
          int ch = query.codeUnitAt(i);
          // Uppercase letters must match pattern
          if (ch >= 65 && ch <= 90) {
            return false;
          }
          i++;
        }
      }
      return j == pattern.length;
    }

    List<bool> result = [];
    for (var q in queries) {
      result.add(matches(q));
    }
    return result;
  }
}
```

## Golang

```go
func camelMatch(queries []string, pattern string) []bool {
    res := make([]bool, len(queries))
    for i, q := range queries {
        res[i] = match(q, pattern)
    }
    return res
}
func match(word, pat string) bool {
    j, m := 0, len(pat)
    for i := 0; i < len(word); i++ {
        c := word[i]
        if j < m && c == pat[j] {
            j++
        } else {
            if c >= 'A' && c <= 'Z' {
                return false
            }
        }
    }
    return j == m
}
```

## Ruby

```ruby
def camel_match(queries, pattern)
  queries.map do |q|
    i = j = 0
    while i < q.length
      qc = q.getbyte(i)
      if j < pattern.length && qc == pattern.getbyte(j)
        i += 1
        j += 1
      elsif qc >= 97 && qc <= 122 # lowercase letter
        i += 1
      else
        break
      end
    end
    i == q.length && j == pattern.length
  end
end
```

## Scala

```scala
object Solution {
  def camelMatch(queries: Array[String], pattern: String): List[Boolean] = {
    queries.map(q => matches(q, pattern)).toList
  }

  private def matches(word: String, pattern: String): Boolean = {
    var i = 0
    var j = 0
    val n = word.length
    val m = pattern.length

    while (i < n) {
      if (j < m && word(i) == pattern(j)) {
        i += 1
        j += 1
      } else if (word(i).isUpper) {
        return false
      } else {
        i += 1
      }
    }

    j == m
  }
}
```

## Rust

```rust
impl Solution {
    pub fn camel_match(queries: Vec<String>, pattern: String) -> Vec<bool> {
        let pat_chars: Vec<char> = pattern.chars().collect();
        queries
            .iter()
            .map(|q| {
                let mut i = 0usize;
                for ch in q.chars() {
                    if i < pat_chars.len() && ch == pat_chars[i] {
                        i += 1;
                    } else if ch.is_ascii_uppercase() {
                        return false;
                    }
                }
                i == pat_chars.len()
            })
            .collect()
    }
}
```

## Racket

```racket
(define (uppercase? c)
  (and (>= (char->integer c) (char->integer #\A))
       (<= (char->integer c) (char->integer #\Z))))

(define (match-word word pattern)
  (let loop ((i 0) (j 0)
             (n (string-length word))
             (m (string-length pattern)))
    (cond
      [(= i n) (= j m)]
      [else
       (define c (string-ref word i))
       (if (and (< j m) (char=? c (string-ref pattern j)))
           (loop (+ i 1) (+ j 1) n m)
           (if (uppercase? c)
               #f
               (loop (+ i 1) j n m)))])))

(define/contract (camel-match queries pattern)
  (-> (listof string?) string? (listof boolean?))
  (map (lambda (q) (match-word q pattern)) queries))
```

## Erlang

```erlang
-module(solution).
-export([camel_match/2]).

-spec camel_match(Queries :: [unicode:unicode_binary()], Pattern :: unicode:unicode_binary()) -> [boolean()].
camel_match(Queries, Pattern) ->
    PatList = unicode:characters_to_list(Pattern),
    lists:map(fun(Q) ->
        Qlist = unicode:characters_to_list(Q),
        match_word(Qlist, PatList)
    end, Queries).

match_word([], []) -> true;
match_word([], [_|_]) -> false;
match_word([Qc|Qs], []) ->
    if Qc >= $a, Qc =< $z -> match_word(Qs, []);
       true -> false
    end;
match_word([Qc|Qs], [Pc|Ps]) ->
    case Qc of
        Pc -> match_word(Qs, Ps);
        _ when Qc >= $a, Qc =< $z -> match_word(Qs, [Pc|Ps]);
        _ -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec camel_match(queries :: [String.t()], pattern :: String.t()) :: [boolean()]
  def camel_match(queries, pattern) do
    Enum.map(queries, fn query -> match?(query, pattern) end)
  end

  defp match?(query, pattern) do
    q_chars = String.to_charlist(query)
    p_chars = String.to_charlist(pattern)
    go(q_chars, p_chars)
  end

  defp go([], []), do: true
  defp go([], _), do: false

  defp go([qc | rest_q], p) do
    cond do
      p != [] and qc == hd(p) ->
        go(rest_q, tl(p))

      qc >= ?A and qc <= ?Z ->
        false

      true ->
        go(rest_q, p)
    end
  end
end
```
