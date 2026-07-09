# 0809. Expressive Words

## Cpp

```cpp
class Solution {
public:
    bool isStretchy(const string& s, const string& w) {
        int i = 0, j = 0;
        int n = s.size(), m = w.size();
        while (i < n && j < m) {
            if (s[i] != w[j]) return false;
            char c = s[i];
            int cntS = 0;
            while (i < n && s[i] == c) { ++cntS; ++i; }
            int cntW = 0;
            while (j < m && w[j] == c) { ++cntW; ++j; }
            if (cntS < cntW) return false;
            if (cntS < 3 && cntS != cntW) return false;
        }
        return i == n && j == m;
    }

    int expressiveWords(string s, vector<string>& words) {
        int ans = 0;
        for (const string& w : words) {
            if (isStretchy(s, w)) ++ans;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int expressiveWords(String s, String[] words) {
        int count = 0;
        for (String w : words) {
            if (isStretchy(s, w)) {
                count++;
            }
        }
        return count;
    }

    private boolean isStretchy(String s, String w) {
        int i = 0, j = 0;
        int n = s.length(), m = w.length();
        while (i < n && j < m) {
            char cs = s.charAt(i);
            char cw = w.charAt(j);
            if (cs != cw) return false;

            int i2 = i;
            while (i2 < n && s.charAt(i2) == cs) i2++;
            int cntS = i2 - i;

            int j2 = j;
            while (j2 < m && w.charAt(j2) == cw) j2++;
            int cntW = j2 - j;

            if (cntS < 3) {
                if (cntS != cntW) return false;
            } else {
                if (cntW > cntS) return false;
                // cntW can be any value from 1 up to cntS
            }

            i = i2;
            j = j2;
        }
        return i == n && j == m;
    }
}
```

## Python

```python
class Solution(object):
    def expressiveWords(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        def can_extend(word):
            i = j = 0
            n, m = len(s), len(word)
            while i < n and j < m:
                if s[i] != word[j]:
                    return False
                # count repeats in s
                cnt_s = 1
                while i + cnt_s < n and s[i + cnt_s] == s[i]:
                    cnt_s += 1
                # count repeats in word
                cnt_w = 1
                while j + cnt_w < m and word[j + cnt_w] == word[j]:
                    cnt_w += 1
                if cnt_s < cnt_w:
                    return False
                if cnt_s < 3 and cnt_s != cnt_w:
                    return False
                i += cnt_s
                j += cnt_w
            return i == n and j == m

        count = 0
        for w in words:
            if can_extend(w):
                count += 1
        return count
```

## Python3

```python
from typing import List

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def is_stretchy(word: str) -> bool:
            i = j = 0
            n, m = len(s), len(word)
            while i < n and j < m:
                if s[i] != word[j]:
                    return False
                ch = s[i]
                cnt_s = 0
                while i < n and s[i] == ch:
                    i += 1
                    cnt_s += 1
                cnt_w = 0
                while j < m and word[j] == ch:
                    j += 1
                    cnt_w += 1
                if cnt_s < 3:
                    if cnt_s != cnt_w:
                        return False
                else:
                    if cnt_w > cnt_s:
                        return False
            return i == n and j == m

        return sum(is_stretchy(w) for w in words)
```

## C

```c
#include <stdbool.h>

static bool isStretchy(const char *s, const char *w) {
    int i = 0, j = 0;
    while (s[i] && w[j]) {
        if (s[i] != w[j])
            return false;
        char c = s[i];
        int cntS = 0, cntW = 0;
        while (s[i] == c) { cntS++; i++; }
        while (w[j] == c) { cntW++; j++; }
        if (cntS < cntW)
            return false;
        if (cntS < 3 && cntS != cntW)
            return false;
    }
    return s[i] == '\0' && w[j] == '\0';
}

int expressiveWords(char* s, char** words, int wordsSize) {
    int count = 0;
    for (int k = 0; k < wordsSize; ++k) {
        if (isStretchy(s, words[k]))
            ++count;
    }
    return count;
}
```

## Csharp

```csharp
public class Solution
{
    public int ExpressiveWords(string s, string[] words)
    {
        int result = 0;
        foreach (var w in words)
        {
            if (IsStretchy(s, w))
                result++;
        }
        return result;
    }

    private bool IsStretchy(string s, string w)
    {
        int i = 0, j = 0;
        while (i < s.Length && j < w.Length)
        {
            if (s[i] != w[j])
                return false;

            char ch = s[i];
            int cntS = 0;
            while (i + cntS < s.Length && s[i + cntS] == ch) cntS++;

            int cntW = 0;
            while (j + cntW < w.Length && w[j + cntW] == ch) cntW++;

            if (cntS < 3)
            {
                if (cntS != cntW)
                    return false;
            }
            else
            {
                if (cntW > cntS || cntW < 1)
                    return false;
            }

            i += cntS;
            j += cntW;
        }

        return i == s.Length && j == w.Length;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string[]} words
 * @return {number}
 */
var expressiveWords = function(s, words) {
    const isStretchy = (target, word) => {
        let i = 0, j = 0;
        while (i < target.length && j < word.length) {
            if (target[i] !== word[j]) return false;
            const ch = target[i];
            let cntT = 0;
            while (i < target.length && target[i] === ch) {
                cntT++;
                i++;
            }
            let cntW = 0;
            while (j < word.length && word[j] === ch) {
                cntW++;
                j++;
            }
            if (cntT < cntW) return false; // cannot delete chars
            if (cntT !== cntW && cntT < 3) return false; // need stretchable group
        }
        return i === target.length && j === word.length;
    };
    
    let count = 0;
    for (const w of words) {
        if (isStretchy(s, w)) count++;
    }
    return count;
};
```

## Typescript

```typescript
function expressiveWords(s: string, words: string[]): number {
    const canStretch = (src: string, tgt: string): boolean => {
        let i = 0, j = 0;
        const n = src.length, m = tgt.length;
        while (i < n && j < m) {
            if (src[i] !== tgt[j]) return false;

            let cntS = 0;
            const ch = src[i];
            while (i < n && src[i] === ch) {
                i++;
                cntS++;
            }

            let cntT = 0;
            while (j < m && tgt[j] === ch) {
                j++;
                cntT++;
            }

            if (cntS < 3) {
                if (cntS !== cntT) return false;
            } else {
                if (cntT > cntS) return false; // cannot shrink
                // cntT can be any positive number <= cntS
            }
        }
        return i === n && j === m;
    };

    let count = 0;
    for (const w of words) {
        if (canStretch(s, w)) count++;
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String[] $words
     * @return Integer
     */
    function expressiveWords($s, $words) {
        $count = 0;
        foreach ($words as $w) {
            if ($this->isStretchy($s, $w)) {
                $count++;
            }
        }
        return $count;
    }

    private function isStretchy(string $s, string $word): bool {
        $i = 0;
        $j = 0;
        $n = strlen($s);
        $m = strlen($word);

        while ($i < $n && $j < $m) {
            if ($s[$i] !== $word[$j]) {
                return false;
            }

            $ch = $s[$i];
            $cntS = 0;
            while ($i < $n && $s[$i] === $ch) {
                $cntS++;
                $i++;
            }

            $cntW = 0;
            while ($j < $m && $word[$j] === $ch) {
                $cntW++;
                $j++;
            }

            if ($cntS < 3) {
                if ($cntS !== $cntW) {
                    return false;
                }
            } else {
                if ($cntW > $cntS || $cntW < 1) {
                    return false;
                }
            }
        }

        return $i === $n && $j === $m;
    }
}
```

## Swift

```swift
class Solution {
    func expressiveWords(_ s: String, _ words: [String]) -> Int {
        let sArr = Array(s)
        var result = 0
        for word in words {
            if isStretchy(sArr, Array(word)) {
                result += 1
            }
        }
        return result
    }
    
    private func isStretchy(_ s: [Character], _ w: [Character]) -> Bool {
        var i = 0, j = 0
        let n = s.count, m = w.count
        
        while i < n && j < m {
            if s[i] != w[j] { return false }
            let ch = s[i]
            
            var cntS = 0
            while i + cntS < n && s[i + cntS] == ch {
                cntS += 1
            }
            var cntW = 0
            while j + cntW < m && w[j + cntW] == ch {
                cntW += 1
            }
            
            if cntS < 3 {
                if cntS != cntW { return false }
            } else {
                if cntW > cntS || cntW == 0 { return false }
            }
            
            i += cntS
            j += cntW
        }
        
        return i == n && j == m
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun expressiveWords(s: String, words: Array<String>): Int {
        var count = 0
        for (w in words) {
            if (isStretchy(s, w)) count++
        }
        return count
    }

    private fun isStretchy(s: String, w: String): Boolean {
        var i = 0
        var j = 0
        val n = s.length
        val m = w.length
        while (i < n && j < m) {
            if (s[i] != w[j]) return false
            val ch = s[i]
            var cntS = 0
            while (i < n && s[i] == ch) {
                cntS++
                i++
            }
            var cntW = 0
            while (j < m && w[j] == ch) {
                cntW++
                j++
            }
            if (cntS < 3) {
                if (cntS != cntW) return false
            } else {
                if (cntW > cntS) return false
            }
        }
        return i == n && j == m
    }
}
```

## Dart

```dart
class Solution {
  int expressiveWords(String s, List<String> words) {
    int count = 0;
    for (var w in words) {
      if (_isStretchy(s, w)) count++;
    }
    return count;
  }

  bool _isStretchy(String s, String w) {
    int i = 0, j = 0;
    while (i < s.length && j < w.length) {
      if (s[i] != w[j]) return false;

      int ii = i;
      while (ii < s.length && s[ii] == s[i]) ii++;
      int cntS = ii - i;

      int jj = j;
      while (jj < w.length && w[jj] == w[j]) jj++;
      int cntW = jj - j;

      if (cntS < 3) {
        if (cntS != cntW) return false;
      } else {
        if (cntW > cntS || cntW < 1) return false;
      }

      i = ii;
      j = jj;
    }
    return i == s.length && j == w.length;
  }
}
```

## Golang

```go
func expressiveWords(s string, words []string) int {
    count := 0
    for _, w := range words {
        if isStretchy(s, w) {
            count++
        }
    }
    return count
}

func isStretchy(s, w string) bool {
    i, j := 0, 0
    n, m := len(s), len(w)
    for i < n && j < m {
        if s[i] != w[j] {
            return false
        }
        // Count consecutive characters in s
        ch := s[i]
        cntS := 0
        for i+cntS < n && s[i+cntS] == ch {
            cntS++
        }
        // Count consecutive characters in w
        cntW := 0
        for j+cntW < m && w[j+cntW] == ch {
            cntW++
        }

        if cntS < 3 {
            if cntS != cntW {
                return false
            }
        } else { // cntS >= 3
            if cntW > cntS || cntW < 1 {
                return false
            }
        }

        i += cntS
        j += cntW
    }
    return i == n && j == m
}
```

## Ruby

```ruby
def expressive_words(s, words)
  stretchy = lambda do |w|
    i = 0
    j = 0
    while i < s.length && j < w.length
      return false if s[i] != w[j]
      ch = s[i]

      cnt_s = 0
      while i < s.length && s[i] == ch
        cnt_s += 1
        i += 1
      end

      cnt_w = 0
      while j < w.length && w[j] == ch
        cnt_w += 1
        j += 1
      end

      if cnt_s < 3
        return false unless cnt_s == cnt_w
      else
        return false unless cnt_w <= cnt_s && cnt_w >= 1
      end
    end
    i == s.length && j == w.length
  end

  count = 0
  words.each { |w| count += 1 if stretchy.call(w) }
  count
end
```

## Scala

```scala
object Solution {
    def expressiveWords(s: String, words: Array[String]): Int = {
        var count = 0
        for (w <- words) {
            if (isStretchy(s, w)) count += 1
        }
        count
    }

    private def isStretchy(s: String, w: String): Boolean = {
        var i = 0
        var j = 0
        val n = s.length
        val m = w.length

        while (i < n && j < m) {
            if (s.charAt(i) != w.charAt(j)) return false

            val ch = s.charAt(i)
            var cntS = 0
            while (i + cntS < n && s.charAt(i + cntS) == ch) cntS += 1
            var cntW = 0
            while (j + cntW < m && w.charAt(j + cntW) == ch) cntW += 1

            if (cntS < 3) {
                if (cntS != cntW) return false
            } else {
                if (cntW > cntS || cntW == 0) return false
            }

            i += cntS
            j += cntW
        }
        i == n && j == m
    }
}
```

## Rust

```rust
fn is_stretchy(s: &[u8], w: &[u8]) -> bool {
    let (mut i, mut j) = (0usize, 0usize);
    while i < s.len() && j < w.len() {
        if s[i] != w[j] {
            return false;
        }
        let ch = s[i];
        let mut cnt_s = 0;
        while i + cnt_s < s.len() && s[i + cnt_s] == ch {
            cnt_s += 1;
        }
        let mut cnt_w = 0;
        while j + cnt_w < w.len() && w[j + cnt_w] == ch {
            cnt_w += 1;
        }
        if cnt_s < 3 {
            if cnt_s != cnt_w {
                return false;
            }
        } else {
            if cnt_w > cnt_s {
                return false;
            }
        }
        i += cnt_s;
        j += cnt_w;
    }
    i == s.len() && j == w.len()
}

impl Solution {
    pub fn expressive_words(s: String, words: Vec<String>) -> i32 {
        let s_bytes = s.as_bytes();
        let mut count = 0;
        for w in &words {
            if is_stretchy(s_bytes, w.as_bytes()) {
                count += 1;
            }
        }
        count as i32
    }
}
```

## Racket

```racket
#lang racket

(define (run-length str idx)
  (let ((len (string-length str))
        (c   (string-ref str idx)))
    (let loop ((i idx))
      (if (and (< i len) (char=? (string-ref str i) c))
          (loop (+ i 1))
          (- i idx)))))

(define (can-stretch? s w)
  (let ((n (string-length s))
        (m (string-length w)))
    (let loop ((i 0) (j 0))
      (cond
        [(and (= i n) (= j m)) #t]
        [(or (= i n) (= j m)) #f]
        [else
         (if (char=? (string-ref s i) (string-ref w j))
             (let* ((cntS (run-length s i))
                    (cntW (run-length w j)))
               (cond
                 [(< cntS 3)
                  (if (= cntS cntW)
                      (loop (+ i cntS) (+ j cntW))
                      #f)]
                 [else ; cntS >= 3
                  (if (and (<= cntW cntS) (>= cntW 1))
                      (loop (+ i cntS) (+ j cntW))
                      #f)]))
             #f))])))

(define/contract (expressive-words s words)
  (-> string? (listof string?) exact-integer?)
  (let loop ((ws words) (cnt 0))
    (if (null? ws)
        cnt
        (loop (cdr ws) (+ cnt (if (can-stretch? s (car ws)) 1 0))))))
```

## Erlang

```erlang
-spec expressive_words(S :: unicode:unicode_binary(), Words :: [unicode:unicode_binary()]) -> integer().
expressive_words(S, Words) ->
    Slist = binary_to_list(S),
    lists:foldl(fun(W, Acc) ->
        case is_stretchable(Slist, binary_to_list(W)) of
            true -> Acc + 1;
            false -> Acc
        end
    end, 0, Words).

is_stretchable([], []) -> true;
is_stretchable(_, []) -> false;
is_stretchable([], _) -> false;
is_stretchable([SChar|STail]=SList, [WChar|WTail]=WList) when SChar =:= WChar ->
    {CntS, RestS} = count_same(STail, SChar, 1),
    {CntW, RestW} = count_same(WTail, WChar, 1),
    case valid(CntS, CntW) of
        true -> is_stretchable(RestS, RestW);
        false -> false
    end;
is_stretchable(_, _) -> false.

count_same([Char|Rest], Char, Acc) ->
    count_same(Rest, Char, Acc + 1);
count_same(List, _Char, Acc) ->
    {Acc, List}.

valid(CntS, CntW) when CntS < 3 ->
    CntS =:= CntW;
valid(CntS, CntW) ->
    CntW =< CntS.
```

## Elixir

```elixir
defmodule Solution do
  @spec expressive_words(s :: String.t(), words :: [String.t()]) :: integer()
  def expressive_words(s, words) do
    s_groups = groups(s)

    Enum.count(words, fn w ->
      w_groups = groups(w)
      stretchy?(s_groups, w_groups)
    end)
  end

  defp groups(str) do
    str
    |> String.graphemes()
    |> do_groups([])
    |> Enum.reverse()
  end

  defp do_groups([], acc), do: acc

  defp do_groups([h | t], []) do
    do_groups(t, [{h, 1}])
  end

  defp do_groups([h | t], [{prev, cnt} | rest]) when h == prev do
    do_groups(t, [{prev, cnt + 1} | rest])
  end

  defp do_groups([h | t], [{prev, cnt} | rest]) do
    do_groups(t, [{h, 1}, {prev, cnt} | rest])
  end

  defp stretchy?(s_groups, w_groups) when length(s_groups) == length(w_groups) do
    Enum.zip(s_groups, w_groups)
    |> Enum.all?(fn {{sc, scnt}, {wc, wcnt}} ->
      sc == wc and
        if scnt < 3 do
          wcnt == scnt
        else
          wcnt <= scnt and wcnt >= 1
        end
    end)
  end

  defp stretchy?(_, _), do: false
end
```
