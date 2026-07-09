# 0524. Longest Word in Dictionary through Deleting

## Cpp

```cpp
class Solution {
public:
    bool isSubseq(const string& s, const string& w) {
        int i = 0, j = 0;
        while (i < (int)s.size() && j < (int)w.size()) {
            if (s[i] == w[j]) ++j;
            ++i;
        }
        return j == (int)w.size();
    }

    string findLongestWord(string s, vector<string>& dictionary) {
        sort(dictionary.begin(), dictionary.end(),
             [](const string& a, const string& b) {
                 if (a.size() != b.size()) return a.size() > b.size(); // longer first
                 return a < b; // lexicographically smaller first
             });
        for (const string& w : dictionary) {
            if (isSubseq(s, w)) return w;
        }
        return "";
    }
};
```

## Java

```java
class Solution {
    public String findLongestWord(String s, List<String> dictionary) {
        String best = "";
        for (String word : dictionary) {
            if (isSubsequence(word, s)) {
                if (word.length() > best.length() ||
                    (word.length() == best.length() && word.compareTo(best) < 0)) {
                    best = word;
                }
            }
        }
        return best;
    }

    private boolean isSubsequence(String target, String source) {
        int i = 0, j = 0;
        while (i < source.length() && j < target.length()) {
            if (source.charAt(i) == target.charAt(j)) {
                j++;
            }
            i++;
        }
        return j == target.length();
    }
}
```

## Python

```python
class Solution(object):
    def findLongestWord(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """
        def is_subseq(word):
            i = j = 0
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    j += 1
                i += 1
            return j == len(word)

        best = ""
        for word in dictionary:
            if is_subseq(word):
                if len(word) > len(best) or (len(word) == len(best) and word < best):
                    best = word
        return best
```

## Python3

```python
from typing import List

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def is_subseq(word: str) -> bool:
            i = 0
            for ch in s:
                if i < len(word) and ch == word[i]:
                    i += 1
                if i == len(word):
                    return True
            return i == len(word)

        best = ""
        for w in dictionary:
            if is_subseq(w):
                if len(w) > len(best) or (len(w) == len(best) and w < best):
                    best = w
        return best
```

## C

```c
#include <string.h>

char* findLongestWord(char* s, char** dictionary, int dictionarySize) {
    static char emptyStr[] = "";
    char *result = emptyStr;
    int maxlen = 0;

    for (int i = 0; i < dictionarySize; ++i) {
        char *word = dictionary[i];
        const char *p = s, *q = word;
        while (*p && *q) {
            if (*p == *q) q++;
            p++;
        }
        if (*q != '\0') continue;  // not a subsequence

        int len = 0;
        while (word[len]) ++len;

        if (len > maxlen || (len == maxlen && strcmp(word, result) < 0)) {
            result = word;
            maxlen = len;
        }
    }

    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public string FindLongestWord(string s, IList<string> dictionary)
    {
        string best = "";
        foreach (var word in dictionary)
        {
            if (IsSubsequence(word, s))
            {
                if (word.Length > best.Length ||
                    (word.Length == best.Length && string.CompareOrdinal(word, best) < 0))
                {
                    best = word;
                }
            }
        }
        return best;
    }

    private bool IsSubsequence(string word, string s)
    {
        int i = 0, j = 0;
        while (i < word.Length && j < s.Length)
        {
            if (word[i] == s[j]) i++;
            j++;
        }
        return i == word.Length;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string[]} dictionary
 * @return {string}
 */
var findLongestWord = function(s, dictionary) {
    // Sort by descending length, then ascending lexicographical order
    dictionary.sort((a, b) => {
        if (b.length !== a.length) return b.length - a.length;
        return a.localeCompare(b);
    });
    
    const isSubseq = (word) => {
        let i = 0, j = 0;
        while (i < s.length && j < word.length) {
            if (s[i] === word[j]) j++;
            i++;
        }
        return j === word.length;
    };
    
    for (const w of dictionary) {
        if (isSubseq(w)) return w;
    }
    return "";
};
```

## Typescript

```typescript
function findLongestWord(s: string, dictionary: string[]): string {
    let best = "";
    const isSubsequence = (word: string): boolean => {
        let i = 0, j = 0;
        while (i < s.length && j < word.length) {
            if (s[i] === word[j]) j++;
            i++;
        }
        return j === word.length;
    };
    for (const w of dictionary) {
        if (isSubsequence(w)) {
            if (w.length > best.length || (w.length === best.length && w < best)) {
                best = w;
            }
        }
    }
    return best;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String[] $dictionary
     * @return String
     */
    function findLongestWord($s, $dictionary) {
        $best = "";
        foreach ($dictionary as $word) {
            if ($this->isSubsequence($s, $word)) {
                if (strlen($word) > strlen($best) || (strlen($word) == strlen($best) && strcmp($word, $best) < 0)) {
                    $best = $word;
                }
            }
        }
        return $best;
    }

    private function isSubsequence(string $s, string $word): bool {
        $i = 0;
        $j = 0;
        $lenS = strlen($s);
        $lenW = strlen($word);
        while ($i < $lenS && $j < $lenW) {
            if ($s[$i] === $word[$j]) {
                $j++;
            }
            $i++;
        }
        return $j === $lenW;
    }
}
```

## Swift

```swift
class Solution {
    func findLongestWord(_ s: String, _ dictionary: [String]) -> String {
        let sChars = Array(s)
        
        func isSubsequence(_ word: String) -> Bool {
            let wChars = Array(word)
            var i = 0
            var j = 0
            while i < sChars.count && j < wChars.count {
                if sChars[i] == wChars[j] {
                    j += 1
                }
                i += 1
            }
            return j == wChars.count
        }
        
        var best = ""
        for word in dictionary {
            if isSubsequence(word) {
                if word.count > best.count || (word.count == best.count && word < best) {
                    best = word
                }
            }
        }
        return best
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findLongestWord(s: String, dictionary: List<String>): String {
        var best = ""
        for (word in dictionary) {
            if (isSubsequence(s, word)) {
                if (word.length > best.length || (word.length == best.length && word < best)) {
                    best = word
                }
            }
        }
        return best
    }

    private fun isSubsequence(s: String, w: String): Boolean {
        var i = 0
        for (c in s) {
            if (i < w.length && c == w[i]) {
                i++
            }
        }
        return i == w.length
    }
}
```

## Dart

```dart
class Solution {
  String findLongestWord(String s, List<String> dictionary) {
    String best = "";
    for (var word in dictionary) {
      if (_isSubsequence(s, word)) {
        if (word.length > best.length ||
            (word.length == best.length && word.compareTo(best) < 0)) {
          best = word;
        }
      }
    }
    return best;
  }

  bool _isSubsequence(String s, String t) {
    int i = 0, j = 0;
    while (i < s.length && j < t.length) {
      if (s[i] == t[j]) {
        j++;
      }
      i++;
    }
    return j == t.length;
  }
}
```

## Golang

```go
func findLongestWord(s string, dictionary []string) string {
    res := ""
    for _, word := range dictionary {
        // Quick length check: if word is shorter than current best, it can't beat it
        if len(word) < len(res) {
            continue
        }
        if isSubsequence(s, word) {
            if len(word) > len(res) || (len(word) == len(res) && word < res) {
                res = word
            }
        }
    }
    return res
}

func isSubsequence(s, w string) bool {
    i := 0
    for j := 0; j < len(s) && i < len(w); j++ {
        if s[j] == w[i] {
            i++
        }
    }
    return i == len(w)
}
```

## Ruby

```ruby
def find_longest_word(s, dictionary)
  sorted = dictionary.sort_by { |w| [-w.length, w] }
  sorted.each do |word|
    i = 0
    j = 0
    while i < s.length && j < word.length
      j += 1 if s[i] == word[j]
      i += 1
    end
    return word if j == word.length
  end
  ""
end
```

## Scala

```scala
object Solution {
  def findLongestWord(s: String, dictionary: List[String]): String = {
    var best = ""
    for (word <- dictionary) {
      if (isSubsequence(s, word)) {
        if (word.length > best.length || (word.length == best.length && word < best)) {
          best = word
        }
      }
    }
    best
  }

  private def isSubsequence(s: String, w: String): Boolean = {
    var i = 0
    var j = 0
    val n = s.length
    val m = w.length
    while (i < n && j < m) {
      if (s.charAt(i) == w.charAt(j)) j += 1
      i += 1
    }
    j == m
  }
}
```

## Rust

```rust
impl Solution {
    pub fn find_longest_word(s: String, dictionary: Vec<String>) -> String {
        let s_bytes = s.as_bytes();
        let mut best = String::new();

        for word in dictionary.iter() {
            let w_bytes = word.as_bytes();
            let mut i = 0usize;
            for &c in s_bytes {
                if i < w_bytes.len() && c == w_bytes[i] {
                    i += 1;
                }
            }
            if i == w_bytes.len() {
                if best.is_empty()
                    || word.len() > best.len()
                    || (word.len() == best.len() && word < &best)
                {
                    best = word.clone();
                }
            }
        }

        best
    }
}
```

## Racket

```racket
#lang racket

(require rackunit)

;; Helper: check if `sub` is a subsequence of `s`
(define (subseq? s sub)
  (let loop ((i 0) (j 0)
             (n (string-length s))
             (m (string-length sub)))
    (cond [(= j m) #t]                     ; all chars matched
          [(= i n) #f]                     ; reached end of s without full match
          [else (if (char=? (string-ref s i)
                            (string-ref sub j))
                    (loop (+ i 1) (+ j 1) n m)
                    (loop (+ i 1) j n m))])))

;; Main function
(define/contract (find-longest-word s dictionary)
  (-> string? (listof string?) string?)
  (let loop ((rest dictionary) (best ""))
    (if (null? rest)
        best
        (let* ((word (car rest))
               (candidate
                (and (subseq? s word)
                     (or (> (string-length word) (string-length best))
                         (and (= (string-length word) (string-length best))
                              (string<? word best))))))
          (loop (cdr rest) (if candidate word best))))))

;; Example tests (can be removed in submission)
(check-equal? (find-longest-word "abpcplea" '("ale" "apple" "monkey" "plea")) "apple")
(check-equal? (find-longest-word "abpcplea" '("a" "b" "c")) "a")
```

## Erlang

```erlang
-module(solution).
-export([find_longest_word/2]).

-spec find_longest_word(S :: unicode:unicode_binary(), Dictionary :: [unicode:unicode_binary()]) -> unicode:unicode_binary().
find_longest_word(S, Dictionary) ->
    lists:foldl(fun(W, Acc) ->
        case is_subseq(S, W) of
            true -> better(W, Acc);
            false -> Acc
        end
    end, <<>>, Dictionary).

-spec is_subseq(unicode:unicode_binary(), unicode:unicode_binary()) -> boolean().
is_subseq(_, <<"">>) -> true;
is_subseq(<<>>, _) -> false;
is_subseq(<<C, RestS/binary>>, <<C, RestW/binary>>) ->
    is_subseq(RestS, RestW);
is_subseq(<<_, RestS/binary>>, Word) ->
    is_subseq(RestS, Word).

-spec better(unicode:unicode_binary(), unicode:unicode_binary()) -> unicode:unicode_binary().
better(New, <<>>) -> New;
better(New, Old) ->
    LenN = byte_size(New),
    LenO = byte_size(Old),
    if
        LenN > LenO -> New;
        LenN < LenO -> Old;
        true ->
            case New < Old of
                true -> New;
                false -> Old
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_longest_word(String.t(), [String.t()]) :: String.t()
  def find_longest_word(s, dictionary) do
    s_chars = String.graphemes(s)

    Enum.reduce(dictionary, "", fn word, best ->
      if is_subsequence?(s_chars, word) do
        cond do
          String.length(word) > String.length(best) -> word
          String.length(word) == String.length(best) and word < best -> word
          true -> best
        end
      else
        best
      end
    end)
  end

  defp is_subsequence?(s_chars, word) do
    w_chars = String.graphemes(word)
    subseq_check(s_chars, w_chars)
  end

  defp subseq_check(_, []), do: true
  defp subseq_check([], _), do: false
  defp subseq_check([sh | st], [wh | wt]) do
    if sh == wh do
      subseq_check(st, wt)
    else
      subseq_check(st, [wh | wt])
    end
  end
end
```
