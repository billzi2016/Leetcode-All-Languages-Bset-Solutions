# 1160. Find Words That Can Be Formed by Characters

## Cpp

```cpp
class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
        vector<int> cnt(26, 0);
        for (char c : chars) cnt[c - 'a']++;
        int ans = 0;
        for (const string& w : words) {
            vector<int> wc(26, 0);
            bool good = true;
            for (char c : w) {
                int idx = c - 'a';
                if (++wc[idx] > cnt[idx]) {
                    good = false;
                    break;
                }
            }
            if (good) ans += w.size();
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int countCharacters(String[] words, String chars) {
        int[] charCount = new int[26];
        for (char c : chars.toCharArray()) {
            charCount[c - 'a']++;
        }
        int totalLength = 0;
        for (String word : words) {
            int[] wordCount = new int[26];
            boolean good = true;
            for (char c : word.toCharArray()) {
                int idx = c - 'a';
                wordCount[idx]++;
                if (wordCount[idx] > charCount[idx]) {
                    good = false;
                    break;
                }
            }
            if (good) {
                totalLength += word.length();
            }
        }
        return totalLength;
    }
}
```

## Python

```python
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        base = [0] * 26
        for c in chars:
            base[ord(c) - ord('a')] += 1

        total = 0
        for word in words:
            cnt = base[:]
            good = True
            for ch in word:
                idx = ord(ch) - ord('a')
                if cnt[idx] == 0:
                    good = False
                    break
                cnt[idx] -= 1
            if good:
                total += len(word)
        return total
```

## Python3

```python
from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # Frequency of characters in chars
        char_counts = [0] * 26
        for c in chars:
            char_counts[ord(c) - ord('a')] += 1

        total_len = 0
        for word in words:
            word_counts = [0] * 26
            for c in word:
                idx = ord(c) - ord('a')
                word_counts[idx] += 1
                # Early break if count exceeds available chars
                if word_counts[idx] > char_counts[idx]:
                    break
            else:
                # Completed loop without breaking, word is good
                total_len += len(word)
        return total_len
```

## C

```c
#include <string.h>

int countCharacters(char** words, int wordsSize, char* chars) {
    int cnt[26] = {0};
    for (char *p = chars; *p; ++p) {
        cnt[*p - 'a']++;
    }

    int ans = 0;
    for (int i = 0; i < wordsSize; ++i) {
        int wcnt[26] = {0};
        char *w = words[i];
        for (char *p = w; *p; ++p) {
            wcnt[*p - 'a']++;
        }

        int good = 1;
        for (int j = 0; j < 26; ++j) {
            if (wcnt[j] > cnt[j]) {
                good = 0;
                break;
            }
        }

        if (good) {
            ans += (int)strlen(w);
        }
    }

    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int CountCharacters(string[] words, string chars) {
        int[] charCount = new int[26];
        foreach (char c in chars) {
            charCount[c - 'a']++;
        }

        int totalLength = 0;
        foreach (string word in words) {
            int[] wordCount = new int[26];
            bool good = true;
            foreach (char c in word) {
                int idx = c - 'a';
                wordCount[idx]++;
                if (wordCount[idx] > charCount[idx]) {
                    good = false;
                    break;
                }
            }
            if (good) {
                totalLength += word.Length;
            }
        }

        return totalLength;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @param {string} chars
 * @return {number}
 */
var countCharacters = function(words, chars) {
    const base = 'a'.charCodeAt(0);
    const charCount = new Array(26).fill(0);
    for (let i = 0; i < chars.length; i++) {
        charCount[chars.charCodeAt(i) - base]++;
    }
    let total = 0;
    for (const word of words) {
        const need = new Array(26).fill(0);
        let ok = true;
        for (let i = 0; i < word.length; i++) {
            const idx = word.charCodeAt(i) - base;
            need[idx]++;
            if (need[idx] > charCount[idx]) {
                ok = false;
                break;
            }
        }
        if (ok) total += word.length;
    }
    return total;
};
```

## Typescript

```typescript
function countCharacters(words: string[], chars: string): number {
    const charCount = new Array(26).fill(0);
    for (const c of chars) {
        charCount[c.charCodeAt(0) - 97]++;
    }
    let total = 0;
    for (const word of words) {
        const wordCount = new Array(26).fill(0);
        for (const c of word) {
            wordCount[c.charCodeAt(0) - 97]++;
        }
        let good = true;
        for (let i = 0; i < 26; i++) {
            if (wordCount[i] > charCount[i]) {
                good = false;
                break;
            }
        }
        if (good) total += word.length;
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $words
     * @param String $chars
     * @return Integer
     */
    function countCharacters($words, $chars) {
        $counts = array_fill(0, 26, 0);
        $lenChars = strlen($chars);
        for ($i = 0; $i < $lenChars; $i++) {
            $idx = ord($chars[$i]) - 97;
            $counts[$idx]++;
        }

        $ans = 0;
        foreach ($words as $word) {
            $wordCount = array_fill(0, 26, 0);
            $lenWord = strlen($word);
            for ($j = 0; $j < $lenWord; $j++) {
                $idx = ord($word[$j]) - 97;
                $wordCount[$idx]++;
            }

            $good = true;
            for ($k = 0; $k < 26; $k++) {
                if ($wordCount[$k] > $counts[$k]) {
                    $good = false;
                    break;
                }
            }

            if ($good) {
                $ans += $lenWord;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countCharacters(_ words: [String], _ chars: String) -> Int {
        var charCounts = [Int](repeating: 0, count: 26)
        for byte in chars.utf8 {
            let idx = Int(byte) - 97
            if idx >= 0 && idx < 26 {
                charCounts[idx] += 1
            }
        }

        var total = 0

        for word in words {
            var wordCounts = [Int](repeating: 0, count: 26)
            var good = true
            for byte in word.utf8 {
                let idx = Int(byte) - 97
                if idx < 0 || idx >= 26 { continue }
                wordCounts[idx] += 1
                if wordCounts[idx] > charCounts[idx] {
                    good = false
                    break
                }
            }
            if good {
                total += word.count
            }
        }

        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countCharacters(words: Array<String>, chars: String): Int {
        val charCount = IntArray(26)
        for (c in chars) {
            charCount[c - 'a']++
        }
        var total = 0
        for (word in words) {
            val wordCount = IntArray(26)
            for (c in word) {
                wordCount[c - 'a']++
            }
            var good = true
            for (i in 0 until 26) {
                if (wordCount[i] > charCount[i]) {
                    good = false
                    break
                }
            }
            if (good) total += word.length
        }
        return total
    }
}
```

## Dart

```dart
class Solution {
  int countCharacters(List<String> words, String chars) {
    List<int> charCount = List.filled(26, 0);
    for (int i = 0; i < chars.length; i++) {
      charCount[chars.codeUnitAt(i) - 97]++;
    }

    int totalLength = 0;
    for (String word in words) {
      List<int> wordCount = List.filled(26, 0);
      bool good = true;
      for (int i = 0; i < word.length; i++) {
        int idx = word.codeUnitAt(i) - 97;
        wordCount[idx]++;
        if (wordCount[idx] > charCount[idx]) {
          good = false;
          break;
        }
      }
      if (good) totalLength += word.length;
    }

    return totalLength;
  }
}
```

## Golang

```go
func countCharacters(words []string, chars string) int {
    var charCount [26]int
    for _, c := range chars {
        idx := int(c - 'a')
        charCount[idx]++
    }
    total := 0
    for _, w := range words {
        var wordCount [26]int
        good := true
        for _, c := range w {
            idx := int(c - 'a')
            wordCount[idx]++
            if wordCount[idx] > charCount[idx] {
                good = false
                break
            }
        }
        if good {
            total += len(w)
        }
    }
    return total
}
```

## Ruby

```ruby
def count_characters(words, chars)
  char_counts = Array.new(26, 0)
  chars.each_byte { |b| char_counts[b - 97] += 1 }

  total_length = 0
  words.each do |word|
    word_counts = Array.new(26, 0)
    word.each_byte { |b| word_counts[b - 97] += 1 }

    good = true
    26.times do |i|
      if word_counts[i] > char_counts[i]
        good = false
        break
      end
    end

    total_length += word.length if good
  end

  total_length
end
```

## Scala

```scala
object Solution {
    def countCharacters(words: Array[String], chars: String): Int = {
        val charCount = new Array[Int](26)
        for (c <- chars) {
            charCount(c - 'a') += 1
        }
        var total = 0
        for (word <- words) {
            val wordCount = new Array[Int](26)
            var good = true
            for (c <- word) {
                val idx = c - 'a'
                wordCount(idx) += 1
                if (wordCount(idx) > charCount(idx)) {
                    good = false
                }
            }
            if (good) total += word.length
        }
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_characters(words: Vec<String>, chars: String) -> i32 {
        let mut cnt = [0i32; 26];
        for b in chars.bytes() {
            cnt[(b - b'a') as usize] += 1;
        }
        let mut ans = 0i32;
        for w in words.iter() {
            let mut wc = [0i32; 26];
            for b in w.bytes() {
                wc[(b - b'a') as usize] += 1;
            }
            let mut good = true;
            for i in 0..26 {
                if wc[i] > cnt[i] {
                    good = false;
                    break;
                }
            }
            if good {
                ans += w.len() as i32;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (count-characters words chars)
  (-> (listof string?) string? exact-integer?)
  (let* ([base-count (make-vector 26 0)]
         [char-index (lambda (c) (- (char->integer c) (char->integer #\a)))])
    ;; count characters in `chars`
    (for ([c (in-string chars)])
      (let* ([i (char-index c)]
             [new (+ 1 (vector-ref base-count i))])
        (vector-set! base-count i new)))
    (define total 0)
    ;; process each word
    (for ([w words])
      (let ([word-count (make-vector 26 0)])
        (for ([c (in-string w)])
          (let* ([i (char-index c)]
                 [new (+ 1 (vector-ref word-count i))])
            (vector-set! word-count i new)))
        (define good #t)
        (for ([i (in-range 26)] #:break (not good))
          (when (> (vector-ref word-count i) (vector-ref base-count i))
            (set! good #f)))
        (when good
          (set! total (+ total (string-length w))))))
    total))
```

## Erlang

```erlang
-spec count_characters(Words :: [unicode:unicode_binary()], Chars :: unicode:unicode_binary()) -> integer().
count_characters(Words, Chars) ->
    CharCounts = build_counts(Chars),
    lists:foldl(fun(Word, Acc) ->
        case check_word(Word, CharCounts) of
            true -> Acc + byte_size(Word);
            false -> Acc
        end
    end, 0, Words).

build_counts(Binary) ->
    build_counts(Binary, empty_counts()).

build_counts(<<>>, Counts) -> Counts;
build_counts(<<C, Rest/binary>>, Counts) ->
    Index = C - $a,
    Pos = Index + 1,
    Old = element(Pos, Counts),
    NewCounts = setelement(Pos, Counts, Old + 1),
    build_counts(Rest, NewCounts).

empty_counts() ->
    {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}.

check_word(Word, CharCounts) ->
    WordCounts = build_counts(Word),
    compare_counts(CharCounts, WordCounts).

compare_counts(C1, C2) ->
    compare_counts(C1, C2, 1, tuple_size(C1)).

compare_counts(_, _, I, N) when I > N -> true;
compare_counts(C1, C2, I, N) ->
    if element(I, C1) < element(I, C2) ->
            false;
       true ->
            compare_counts(C1, C2, I + 1, N)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_characters(words :: [String.t()], chars :: String.t()) :: integer()
  def count_characters(words, chars) do
    global_counts = char_counts(chars)

    Enum.reduce(words, 0, fn word, acc ->
      if good_word?(word, global_counts) do
        acc + String.length(word)
      else
        acc
      end
    end)
  end

  defp char_counts(str) do
    str
    |> String.to_charlist()
    |> Enum.reduce(%{}, fn c, m ->
      Map.update(m, c, 1, &(&1 + 1))
    end)
  end

  defp good_word?(word, global_counts) do
    word_counts = char_counts(word)

    Enum.all?(word_counts, fn {c, cnt} ->
      Map.get(global_counts, c, 0) >= cnt
    end)
  end
end
```
