# 1592. Rearrange Spaces Between Words

## Cpp

```cpp
class Solution {
public:
    string reorderSpaces(string text) {
        int totalSpaces = 0;
        vector<string> words;
        int n = text.size();
        for (int i = 0; i < n; ++i) {
            if (text[i] == ' ') {
                ++totalSpaces;
            } else {
                int j = i;
                while (j < n && text[j] != ' ') ++j;
                words.emplace_back(text.substr(i, j - i));
                i = j - 1;
            }
        }
        
        if (words.empty()) return string(totalSpaces, ' ');
        if (words.size() == 1) {
            return words[0] + string(totalSpaces, ' ');
        }
        
        int between = totalSpaces / (words.size() - 1);
        int endSpaces = totalSpaces % (words.size() - 1);
        string sep(between, ' ');
        string result;
        for (size_t i = 0; i < words.size(); ++i) {
            result += words[i];
            if (i != words.size() - 1) result += sep;
        }
        result.append(endSpaces, ' ');
        return result;
    }
};
```

## Java

```java
class Solution {
    public String reorderSpaces(String text) {
        int spaceCount = 0;
        for (char c : text.toCharArray()) {
            if (c == ' ') spaceCount++;
        }
        String trimmed = text.trim();
        // If after trimming there is no word (should not happen per constraints), handle gracefully
        if (trimmed.isEmpty()) {
            return " ".repeat(spaceCount);
        }
        String[] words = trimmed.split("\\s+");
        int nWords = words.length;
        if (nWords == 1) {
            StringBuilder sb = new StringBuilder();
            sb.append(words[0]);
            sb.append(" ".repeat(spaceCount));
            return sb.toString();
        }
        int between = spaceCount / (nWords - 1);
        int extra = spaceCount % (nWords - 1);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < nWords; i++) {
            sb.append(words[i]);
            if (i < nWords - 1) {
                sb.append(" ".repeat(between));
            }
        }
        sb.append(" ".repeat(extra));
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        total_spaces = text.count(' ')
        words = text.split()
        n = len(words)
        if n == 1:
            return words[0] + ' ' * total_spaces
        between = total_spaces // (n - 1)
        trailing = total_spaces % (n - 1)
        return (' ' * between).join(words) + ' ' * trailing
```

## Python3

```python
class Solution:
    def reorderSpaces(self, text: str) -> str:
        total_spaces = text.count(' ')
        words = text.split()
        n = len(words)
        if n == 1:
            return words[0] + ' ' * total_spaces
        between = total_spaces // (n - 1)
        trailing = total_spaces % (n - 1)
        return (' ' * between).join(words) + ' ' * trailing
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* reorderSpaces(char* text) {
    int n = strlen(text);
    int totalSpaces = 0;
    for (int i = 0; i < n; ++i) {
        if (text[i] == ' ') totalSpaces++;
    }

    // Extract words
    char* words[101];
    int lens[101];
    int wordCount = 0;

    int i = 0;
    while (i < n) {
        while (i < n && text[i] == ' ') i++;          // skip spaces
        if (i >= n) break;
        int start = i;
        while (i < n && text[i] != ' ') i++;           // end of word
        int len = i - start;
        char* w = (char*)malloc(len + 1);
        memcpy(w, &text[start], len);
        w[len] = '\0';
        words[wordCount] = w;
        lens[wordCount] = len;
        wordCount++;
    }

    int betweenSpaces = 0, trailingSpaces = 0;
    if (wordCount > 1) {
        betweenSpaces = totalSpaces / (wordCount - 1);
        trailingSpaces = totalSpaces % (wordCount - 1);
    } else {
        // all spaces go to the end
        trailingSpaces = totalSpaces;
    }

    char* res = (char*)malloc(n + 1);
    int pos = 0;
    for (int w = 0; w < wordCount; ++w) {
        memcpy(res + pos, words[w], lens[w]);
        pos += lens[w];
        if (w != wordCount - 1) {
            memset(res + pos, ' ', betweenSpaces);
            pos += betweenSpaces;
        }
    }
    if (trailingSpaces > 0) {
        memset(res + pos, ' ', trailingSpaces);
        pos += trailingSpaces;
    }
    res[pos] = '\0';

    // free allocated words
    for (int w = 0; w < wordCount; ++w) {
        free(words[w]);
    }

    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string ReorderSpaces(string text)
    {
        int spaceCount = 0;
        foreach (char c in text)
            if (c == ' ') spaceCount++;

        var words = text.Split(new char[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);
        int wordCount = words.Length;

        if (wordCount == 1)
            return words[0] + new string(' ', spaceCount);

        int spacesBetween = spaceCount / (wordCount - 1);
        int extraSpaces = spaceCount % (wordCount - 1);
        string separator = new string(' ', spacesBetween);

        var sb = new System.Text.StringBuilder();
        for (int i = 0; i < wordCount; i++)
        {
            sb.Append(words[i]);
            if (i != wordCount - 1)
                sb.Append(separator);
        }
        sb.Append(new string(' ', extraSpaces));
        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} text
 * @return {string}
 */
var reorderSpaces = function(text) {
    // Count total spaces
    let totalSpaces = 0;
    for (let ch of text) {
        if (ch === ' ') totalSpaces++;
    }
    
    // Extract words
    const words = text.match(/\S+/g) || [];
    const wordCount = words.length;
    
    if (wordCount === 1) {
        // All spaces go after the single word
        return words[0] + ' '.repeat(totalSpaces);
    }
    
    const between = Math.floor(totalSpaces / (wordCount - 1));
    const end = totalSpaces - between * (wordCount - 1);
    const sep = ' '.repeat(between);
    
    return words.join(sep) + ' '.repeat(end);
};
```

## Typescript

```typescript
function reorderSpaces(text: string): string {
    let spaceCount = 0;
    for (const ch of text) {
        if (ch === ' ') spaceCount++;
    }
    const words = text.trim().split(/\s+/);
    const n = words.length;
    if (n === 1) {
        return words[0] + ' '.repeat(spaceCount);
    }
    const between = Math.floor(spaceCount / (n - 1));
    const extra = spaceCount % (n - 1);
    return words.join(' '.repeat(between)) + ' '.repeat(extra);
}
```

## Php

```php
class Solution {
    /**
     * @param String $text
     * @return String
     */
    function reorderSpaces($text) {
        $totalSpaces = substr_count($text, ' ');
        $words = preg_split('/\s+/', trim($text));
        $wordCount = count($words);
        if ($wordCount == 1) {
            return $words[0] . str_repeat(' ', $totalSpaces);
        }
        $between = intdiv($totalSpaces, $wordCount - 1);
        $trailing = $totalSpaces - $between * ($wordCount - 1);
        $sep = str_repeat(' ', $between);
        return implode($sep, $words) . str_repeat(' ', $trailing);
    }
}
```

## Swift

```swift
class Solution {
    func reorderSpaces(_ text: String) -> String {
        let totalSpaces = text.filter { $0 == " " }.count
        let words = text.split(separator: " ").map(String.init)
        let wordCount = words.count
        
        if wordCount == 1 {
            return words[0] + String(repeating: " ", count: totalSpaces)
        }
        
        let spacesBetween = totalSpaces / (wordCount - 1)
        let extraSpaces = totalSpaces % (wordCount - 1)
        let separator = String(repeating: " ", count: spacesBetween)
        var result = words.joined(separator: separator)
        result += String(repeating: " ", count: extraSpaces)
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun reorderSpaces(text: String): String {
        var spaceCount = 0
        for (c in text) {
            if (c == ' ') spaceCount++
        }
        val words = text.trim().split(Regex("\\s+")).filter { it.isNotEmpty() }
        val n = words.size
        return if (n == 1) {
            words[0] + " ".repeat(spaceCount)
        } else {
            val between = spaceCount / (n - 1)
            val extra = spaceCount % (n - 1)
            val sb = StringBuilder()
            for (i in 0 until n) {
                sb.append(words[i])
                if (i != n - 1) repeat(between) { sb.append(' ') }
            }
            repeat(extra) { sb.append(' ') }
            sb.toString()
        }
    }
}
```

## Dart

```dart
class Solution {
  String reorderSpaces(String text) {
    int spaceCount = 0;
    for (int i = 0; i < text.length; i++) {
      if (text[i] == ' ') spaceCount++;
    }

    List<String> words = [];
    RegExp wordReg = RegExp(r'\S+');
    for (final match in wordReg.allMatches(text)) {
      words.add(match.group(0)!);
    }

    int wordCount = words.length;
    if (wordCount == 1) {
      return words[0] + _repeat(' ', spaceCount);
    }

    int spacesBetween = spaceCount ~/ (wordCount - 1);
    int extraSpaces = spaceCount % (wordCount - 1);

    String between = _repeat(' ', spacesBetween);
    String result = words.join(between) + _repeat(' ', extraSpaces);
    return result;
  }

  String _repeat(String s, int n) {
    if (n <= 0) return '';
    return List.filled(n, s).join();
  }
}
```

## Golang

```go
func reorderSpaces(text string) string {
    // Count total spaces
    spaceCount := 0
    for _, ch := range text {
        if ch == ' ' {
            spaceCount++
        }
    }

    // Extract words
    words := strings.Fields(text)
    wordCount := len(words)

    // Determine spacing
    betweenSpaces, endSpaces := 0, spaceCount
    if wordCount > 1 {
        betweenSpaces = spaceCount / (wordCount - 1)
        endSpaces = spaceCount % (wordCount - 1)
    }

    // Build result
    var sb strings.Builder
    for i, w := range words {
        sb.WriteString(w)
        if i < wordCount-1 {
            sb.WriteString(strings.Repeat(" ", betweenSpaces))
        }
    }
    sb.WriteString(strings.Repeat(" ", endSpaces))

    return sb.String()
}
```

## Ruby

```ruby
# @param {String} text
# @return {String}
def reorder_spaces(text)
  total_spaces = text.count(' ')
  words = text.split(/\s+/)
  word_count = words.size

  if word_count == 1
    return words[0] + ' ' * total_spaces
  end

  spaces_between = total_spaces / (word_count - 1)
  trailing_spaces = total_spaces % (word_count - 1)

  words.join(' ' * spaces_between) + ' ' * trailing_spaces
end
```

## Scala

```scala
object Solution {
    def reorderSpaces(text: String): String = {
        val spaceCount = text.count(_ == ' ')
        val words = text.split("\\s+").filter(_.nonEmpty)
        val n = words.length
        if (n == 1) {
            words(0) + (" " * spaceCount)
        } else {
            val between = spaceCount / (n - 1)
            val extra = spaceCount % (n - 1)
            val sb = new StringBuilder
            for (i <- 0 until n) {
                sb.append(words(i))
                if (i != n - 1) sb.append(" " * between)
            }
            sb.append(" " * extra)
            sb.toString()
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn reorder_spaces(text: String) -> String {
        let total_spaces = text.chars().filter(|&c| c == ' ').count();
        let words: Vec<&str> = text.split_whitespace().collect();
        let n = words.len();

        if n == 0 {
            return " ".repeat(total_spaces);
        }

        let between = if n > 1 { total_spaces / (n - 1) } else { 0 };
        let trailing = if n > 1 { total_spaces % (n - 1) } else { total_spaces };

        let mut result = String::with_capacity(text.len());
        for i in 0..n {
            result.push_str(words[i]);
            if i != n - 1 {
                for _ in 0..between {
                    result.push(' ');
                }
            }
        }
        for _ in 0..trailing {
            result.push(' ');
        }
        result
    }
}
```

## Racket

```racket
(require racket/string)

(define/contract (reorder-spaces text)
  (-> string? string?)
  (let* ([spaces (for/sum ([c (in-string text)]) (if (char=? c #\space) 1 0))]
         [words (string-split text)]
         [n-words (length words)])
    (if (= n-words 1)
        (string-append (first words) (make-string spaces #\space))
        (let* ([sep-count (quotient spaces (- n-words 1))]
               [trailing (remainder spaces (- n-words 1))]
               [sep (make-string sep-count #\space)]
               [joined (string-join words sep)])
          (string-append joined (make-string trailing #\space))))))
```

## Erlang

```erlang
-module(solution).
-export([reorder_spaces/1]).

-spec reorder_spaces(Text :: unicode:unicode_binary()) -> unicode:unicode_binary().
reorder_spaces(Text) ->
    CharList = unicode:characters_to_list(Text),
    TotalSpaces = length([C || C <- CharList, C == $ ]),
    Words = string:tokens(CharList, " "),
    case length(Words) of
        1 ->
            Word = hd(Words),
            Result = Word ++ lists:duplicate(TotalSpaces, $ ),
            unicode:characters_to_binary(Result);
        N when N > 1 ->
            SpacesBetween = TotalSpaces div (N - 1),
            ExtraEnd = TotalSpaces rem (N - 1),
            Sep = lists:duplicate(SpacesBetween, $ ),
            Joined = string:join(Words, Sep),
            Result = Joined ++ lists:duplicate(ExtraEnd, $ ),
            unicode:characters_to_binary(Result)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec reorder_spaces(text :: String.t()) :: String.t()
  def reorder_spaces(text) do
    space_count = text |> String.graphemes() |> Enum.count(&(&1 == " "))
    words = String.split(text, ~r/\s+/, trim: true)
    word_cnt = length(words)

    if word_cnt == 1 do
      hd(words) <> String.duplicate(" ", space_count)
    else
      between = div(space_count, word_cnt - 1)
      extra = rem(space_count, word_cnt - 1)
      sep = String.duplicate(" ", between)
      Enum.join(words, sep) <> String.duplicate(" ", extra)
    end
  end
end
```
