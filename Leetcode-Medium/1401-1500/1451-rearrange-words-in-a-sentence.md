# 1451. Rearrange Words in a Sentence

## Cpp

```cpp
class Solution {
public:
    string arrangeWords(string text) {
        vector<string> words;
        string word;
        // split and convert to lowercase
        for (size_t i = 0, n = text.size(); i <= n; ++i) {
            if (i == n || text[i] == ' ') {
                if (!word.empty()) {
                    for (char &c : word) c = tolower(c);
                    words.push_back(word);
                    word.clear();
                }
            } else {
                word += text[i];
            }
        }
        stable_sort(words.begin(), words.end(),
                    [](const string& a, const string& b){ return a.size() < b.size(); });
        // reconstruct with proper capitalization
        for (size_t i = 0; i < words.size(); ++i) {
            if (i == 0 && !words[i].empty())
                words[i][0] = toupper(words[i][0]);
        }
        string result;
        for (size_t i = 0; i < words.size(); ++i) {
            if (i) result += ' ';
            result += words[i];
        }
        return result;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static class Word {
        String text;
        int index;
        Word(String t, int i) { text = t; index = i; }
    }

    public String arrangeWords(String text) {
        String[] parts = text.split(" ");
        int n = parts.length;
        Word[] words = new Word[n];
        for (int i = 0; i < n; i++) {
            words[i] = new Word(parts[i].toLowerCase(), i);
        }
        Arrays.sort(words, (a, b) -> {
            int lenDiff = a.text.length() - b.text.length();
            return (lenDiff != 0) ? lenDiff : a.index - b.index;
        });
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            String w = words[i].text;
            if (i == 0) {
                w = Character.toUpperCase(w.charAt(0)) + w.substring(1);
            }
            sb.append(w);
            if (i < n - 1) sb.append(' ');
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def arrangeWords(self, text):
        """
        :type text: str
        :rtype: str
        """
        # Split the sentence into words and convert them to lowercase
        words = [w.lower() for w in text.split(' ')]
        # Stable sort by length using Python's stable sorting
        words.sort(key=len)
        # Capitalize the first word
        if words:
            words[0] = words[0].capitalize()
        return ' '.join(words)
```

## Python3

```python
class Solution:
    def arrangeWords(self, text: str) -> str:
        words = [w.lower() for w in text.split()]
        words.sort(key=len)
        if words:
            words[0] = words[0].capitalize()
        return " ".join(words)
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    char *word;
    int len;
    int idx;
} Word;

static int cmpWord(const void *a, const void *b) {
    const Word *wa = (const Word *)a;
    const Word *wb = (const Word *)b;
    if (wa->len != wb->len) return wa->len - wb->len;
    return wa->idx - wb->idx;
}

char* arrangeWords(char* text) {
    int n = strlen(text);
    int maxWords = n / 2 + 2;
    Word *arr = (Word *)malloc(sizeof(Word) * maxWords);
    int wcnt = 0;

    int i = 0;
    while (i < n) {
        int start = i;
        while (i < n && text[i] != ' ') i++;
        int l = i - start;
        char *w = (char *)malloc(l + 1);
        memcpy(w, text + start, l);
        w[l] = '\0';
        arr[wcnt].word = w;
        arr[wcnt].len = l;
        arr[wcnt].idx = wcnt;
        wcnt++;
        if (i < n && text[i] == ' ') i++; // skip space
    }

    qsort(arr, wcnt, sizeof(Word), cmpWord);

    int totalLen = 0;
    for (int k = 0; k < wcnt; ++k) totalLen += arr[k].len;
    totalLen += wcnt - 1; // spaces

    char *res = (char *)malloc(totalLen + 1);
    int pos = 0;

    for (int k = 0; k < wcnt; ++k) {
        char *src = arr[k].word;
        int l = arr[k].len;
        for (int j = 0; j < l; ++j) {
            char c = src[j];
            if (k == 0) { // first word
                if (j == 0) {
                    if (c >= 'a' && c <= 'z') c = c - 'a' + 'A';
                } else {
                    if (c >= 'A' && c <= 'Z') c = c - 'A' + 'a';
                }
            } else { // other words
                if (c >= 'A' && c <= 'Z') c = c - 'A' + 'a';
            }
            res[pos++] = c;
        }
        if (k != wcnt - 1) res[pos++] = ' ';
    }
    res[pos] = '\0';

    // free temporary allocations (optional for LeetCode)
    for (int k = 0; k < wcnt; ++k) free(arr[k].word);
    free(arr);

    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string ArrangeWords(string text)
    {
        var words = text.Split(' ');
        var indexedWords = new (string word, int index)[words.Length];
        for (int i = 0; i < words.Length; i++)
        {
            // convert to lowercase for uniform handling
            indexedWords[i] = (words[i].ToLower(), i);
        }

        var sorted = indexedWords
            .OrderBy(p => p.word.Length)
            .ThenBy(p => p.index)
            .Select(p => p.word)
            .ToArray();

        // capitalize first word
        if (sorted.Length > 0 && sorted[0].Length > 0)
        {
            var first = sorted[0];
            sorted[0] = char.ToUpper(first[0]) + first.Substring(1);
        }

        return string.Join(" ", sorted);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} text
 * @return {string}
 */
var arrangeWords = function(text) {
    const words = text.split(' ');
    const arr = words.map((w, i) => ({ word: w.toLowerCase(), idx: i }));
    arr.sort((a, b) => {
        if (a.word.length !== b.word.length) return a.word.length - b.word.length;
        return a.idx - b.idx;
    });
    const sorted = arr.map(item => item.word);
    sorted[0] = sorted[0][0].toUpperCase() + sorted[0].slice(1);
    return sorted.join(' ');
};
```

## Typescript

```typescript
function arrangeWords(text: string): string {
    const words = text.split(' ');
    const data = words.map((w, i) => ({
        word: w.toLowerCase(),
        idx: i,
        len: w.length
    }));
    data.sort((a, b) => a.len - b.len || a.idx - b.idx);
    if (data.length > 0) {
        const first = data[0].word;
        data[0].word = first.charAt(0).toUpperCase() + first.slice(1);
    }
    return data.map(d => d.word).join(' ');
}
```

## Php

```php
class Solution {

    /**
     * @param String $text
     * @return String
     */
    function arrangeWords($text) {
        $words = explode(' ', $text);
        $arr = [];
        foreach ($words as $i => $w) {
            $arr[] = ['word' => $w, 'len' => strlen($w), 'idx' => $i];
        }
        usort($arr, function($a, $b) {
            if ($a['len'] === $b['len']) {
                return $a['idx'] <=> $b['idx'];
            }
            return $a['len'] <=> $b['len'];
        });
        foreach ($arr as $k => &$item) {
            $word = strtolower($item['word']);
            if ($k === 0) {
                $word = ucfirst($word);
            }
            $item = $word;
        }
        return implode(' ', $arr);
    }
}
```

## Swift

```swift
class Solution {
    func arrangeWords(_ text: String) -> String {
        let words = text.split(separator: " ").map { String($0) }
        var indexed = [(word: String, idx: Int)]()
        for (i, w) in words.enumerated() {
            indexed.append((w, i))
        }
        indexed.sort { a, b in
            if a.word.count != b.word.count {
                return a.word.count < b.word.count
            } else {
                return a.idx < b.idx
            }
        }
        var result = indexed.map { $0.word.lowercased() }
        if let first = result.first {
            let capitalized = first.prefix(1).uppercased() + first.dropFirst()
            result[0] = String(capitalized)
        }
        return result.joined(separator: " ")
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun arrangeWords(text: String): String {
        val words = text.split(" ")
        data class Word(val idx: Int, val w: String)
        val list = words.mapIndexed { i, s -> Word(i, s.lowercase()) }
        val sorted = list.sortedWith(compareBy<Word> { it.w.length }.thenBy { it.idx })
        if (sorted.isEmpty()) return ""
        val result = mutableListOf<String>()
        // Capitalize first word
        val first = sorted[0].w.replaceFirstChar { it.uppercase() }
        result.add(first)
        for (i in 1 until sorted.size) {
            result.add(sorted[i].w)
        }
        return result.joinToString(" ")
    }
}
```

## Dart

```dart
class Solution {
  String arrangeWords(String text) {
    List<String> words = text.split(' ');
    for (int i = 0; i < words.length; i++) {
      words[i] = words[i].toLowerCase();
    }
    List<int> order = List<int>.generate(words.length, (i) => i);
    order.sort((a, b) {
      int lenA = words[a].length;
      int lenB = words[b].length;
      if (lenA != lenB) return lenA - lenB;
      return a - b;
    });
    List<String> result = [];
    for (int i = 0; i < order.length; i++) {
      String w = words[order[i]];
      if (i == 0 && w.isNotEmpty) {
        w = w[0].toUpperCase() + w.substring(1);
      }
      result.add(w);
    }
    return result.join(' ');
  }
}
```

## Golang

```go
import (
	"sort"
	"strings"
	"unicode"
)

func arrangeWords(text string) string {
	words := strings.Split(text, " ")
	for i, w := range words {
		words[i] = strings.ToLower(w)
	}
	sort.SliceStable(words, func(i, j int) bool {
		return len(words[i]) < len(words[j])
	})
	if len(words) > 0 && len(words[0]) > 0 {
		runes := []rune(words[0])
		runes[0] = unicode.ToUpper(runes[0])
		words[0] = string(runes)
	}
	return strings.Join(words, " ")
}
```

## Ruby

```ruby
def arrange_words(text)
  words = text.split(' ')
  sorted = words.each_with_index.sort do |(w1, i1), (w2, i2)|
    if w1.length == w2.length
      i1 <=> i2
    else
      w1.length <=> w2.length
    end
  end.map { |w, _| w }

  sorted[0] = sorted[0].capitalize
  (1...sorted.size).each do |i|
    sorted[i] = sorted[i].downcase
  end

  sorted.join(' ')
end
```

## Scala

```scala
object Solution {
    def arrangeWords(text: String): String = {
        val words = text.split(" ").map(_.toLowerCase)
        val indexed = words.zipWithIndex
        val sorted = indexed.sortBy { case (w, idx) => (w.length, idx) }.map(_._1)
        if (sorted.isEmpty) ""
        else {
            val first = sorted.head
            val capitalizedFirst = first.charAt(0).toUpper + first.substring(1)
            (capitalizedFirst +: sorted.tail).mkString(" ")
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn arrange_words(text: String) -> String {
        use std::cmp::Ordering;
        // Split words and keep original indices
        let mut indexed: Vec<(usize, String)> = text
            .split_whitespace()
            .enumerate()
            .map(|(i, w)| (i, w.to_string()))
            .collect();

        // Sort by length, then by original position to maintain stability
        indexed.sort_by(|a, b| {
            let len_cmp = a.1.len().cmp(&b.1.len());
            if len_cmp == Ordering::Equal {
                a.0.cmp(&b.0)
            } else {
                len_cmp
            }
        });

        // Convert all words to lowercase
        let mut lower: Vec<String> = indexed.into_iter()
            .map(|(_, w)| w.to_lowercase())
            .collect();

        if lower.is_empty() {
            return String::new();
        }

        // Join with spaces
        let joined = lower.join(" ");

        // Capitalize the first character of the result
        let mut chars = joined.chars();
        let first = chars.next().unwrap().to_ascii_uppercase();
        let rest: String = chars.collect();

        format!("{}{}", first, rest)
    }
}
```

## Racket

```racket
#lang racket

(require racket/string)
(require racket/list)

(define/contract (arrange-words text)
  (-> string? string?)
  (let* ((words (string-split text " "))
         (lower-words (map string-downcase words))
         (sorted (stable-sort lower-words
                               (lambda (a b) (< (string-length a) (string-length b))))))
    (if (null? sorted)
        ""
        (let* ((first-word (car sorted))
               (capitalized-first (string-append (string-upcase (substring first-word 0 1))
                                                 (substring first-word 1)))
               (result (cons capitalized-first (cdr sorted))))
          (string-join result " ")))))
```

## Erlang

```erlang
-spec arrange_words(Text :: unicode:unicode_binary()) -> unicode:unicode_binary().
arrange_words(Text) ->
    Words = string:split(Text, <<" ">>, all),
    {_, TuplesRev} = lists:foldl(
        fun(Word, {Idx, Acc}) ->
            Len = byte_size(Word),
            {Idx + 1, [{Len, Idx, Word} | Acc]}
        end,
        {0, []},
        Words),
    Sorted = lists:keysort(1, lists:reverse(TuplesRev)),
    LowerWords = [string:to_lower(W) || {_L,_I,W} <- Sorted],
    case LowerWords of
        [] -> <<>>;
        [First|Rest] ->
            Capitalized = capitalize(First),
            string:join([Capitalized | Rest], <<" ">>)
    end.

capitalize(Word) when is_binary(Word) ->
    case Word of
        <<C, Rest/binary>> ->
            Upper = string:to_upper(<<C>>),
            <<Upper/binary, Rest/binary>>
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec arrange_words(text :: String.t()) :: String.t()
  def arrange_words(text) do
    words = String.split(text, " ")
    indexed = Enum.with_index(words)

    sorted =
      Enum.sort_by(indexed, fn {word, idx} ->
        {String.length(word), idx}
      end)

    sorted_words = Enum.map(sorted, fn {word, _idx} -> word end)

    case sorted_words do
      [] ->
        ""

      [first | rest] ->
        first_cap = first |> String.downcase() |> String.capitalize()
        rest_down = Enum.map(rest, &String.downcase/1)
        ([first_cap] ++ rest_down) |> Enum.join(" ")
    end
  end
end
```
