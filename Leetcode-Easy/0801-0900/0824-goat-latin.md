# 0824. Goat Latin

## Cpp

```cpp
class Solution {
public:
    string toGoatLatin(string sentence) {
        unordered_set<char> vowels = {'a','e','i','o','u','A','E','I','O','U'};
        istringstream iss(sentence);
        string word;
        string result;
        int index = 1;
        while (iss >> word) {
            string transformed;
            if (vowels.count(word[0])) {
                transformed = word + "ma";
            } else {
                transformed = word.substr(1) + word[0] + "ma";
            }
            transformed.append(index, 'a');
            if (!result.empty()) result.push_back(' ');
            result += transformed;
            ++index;
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public String toGoatLatin(String sentence) {
        String[] words = sentence.split(" ");
        StringBuilder result = new StringBuilder();
        int idx = 1;
        for (String w : words) {
            char first = w.charAt(0);
            if (isVowel(first)) {
                result.append(w);
            } else {
                result.append(w.substring(1)).append(first);
            }
            result.append("ma");
            for (int i = 0; i < idx; i++) {
                result.append('a');
            }
            if (idx < words.length) {
                result.append(' ');
            }
            idx++;
        }
        return result.toString();
    }

    private boolean isVowel(char c) {
        char lc = Character.toLowerCase(c);
        return lc == 'a' || lc == 'e' || lc == 'i' || lc == 'o' || lc == 'u';
    }
}
```

## Python

```python
class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')
        words = sentence.split()
        result = []
        for i, word in enumerate(words, 1):
            if word[0] in vowels:
                goat_word = word + "ma"
            else:
                goat_word = word[1:] + word[0] + "ma"
            goat_word += 'a' * i
            result.append(goat_word)
        return ' '.join(result)
```

## Python3

```python
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set('aeiouAEIOU')
        words = sentence.split()
        result = []
        for i, w in enumerate(words, 1):
            if w[0] in vowels:
                goat = w + "ma"
            else:
                goat = w[1:] + w[0] + "ma"
            goat += 'a' * i
            result.append(goat)
        return ' '.join(result)
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static bool isVowelChar(char c) {
    return c=='a'||c=='e'||c=='i'||c=='o'||c=='u'||
           c=='A'||c=='E'||c=='I'||c=='O'||c=='U';
}

char* toGoatLatin(char* sentence) {
    if (!sentence) return NULL;
    size_t n = strlen(sentence);
    size_t cap = n * 5 + 10;               // generous extra space
    char *res = (char*)malloc(cap);
    if (!res) return NULL;
    size_t len = 0;
    int wordIdx = 0;
    const char *p = sentence;

    while (*p) {
        const char *start = p;
        while (*p && *p != ' ') p++;
        size_t wlen = p - start;
        if (wlen == 0) { // should not happen, but skip spaces
            if (*p) p++;
            continue;
        }
        wordIdx++;

        bool vowel = isVowelChar(start[0]);

        if (!vowel) {
            // copy from second character onward
            for (size_t i = 1; i < wlen; ++i) {
                if (len + 1 >= cap) {
                    cap *= 2;
                    res = (char*)realloc(res, cap);
                }
                res[len++] = start[i];
            }
            // then first character
            if (len + 1 >= cap) {
                cap *= 2;
                res = (char*)realloc(res, cap);
            }
            res[len++] = start[0];
        } else {
            // copy whole word
            for (size_t i = 0; i < wlen; ++i) {
                if (len + 1 >= cap) {
                    cap *= 2;
                    res = (char*)realloc(res, cap);
                }
                res[len++] = start[i];
            }
        }

        // append "ma"
        const char *suffix = "ma";
        for (int i = 0; i < 2; ++i) {
            if (len + 1 >= cap) {
                cap *= 2;
                res = (char*)realloc(res, cap);
            }
            res[len++] = suffix[i];
        }

        // append wordIdx times 'a'
        for (int i = 0; i < wordIdx; ++i) {
            if (len + 1 >= cap) {
                cap *= 2;
                res = (char*)realloc(res, cap);
            }
            res[len++] = 'a';
        }

        // add space if not end of sentence
        if (*p == ' ') {
            if (len + 1 >= cap) {
                cap *= 2;
                res = (char*)realloc(res, cap);
            }
            res[len++] = ' ';
            p++; // skip the space
        }
    }

    // null-terminate
    if (len + 1 >= cap) {
        cap += 1;
        res = (char*)realloc(res, cap);
    }
    res[len] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string ToGoatLatin(string sentence) {
        var words = sentence.Split(' ');
        var sb = new System.Text.StringBuilder();
        for (int i = 0; i < words.Length; i++) {
            string word = words[i];
            char firstChar = word[0];
            bool isVowel = "aeiouAEIOU".IndexOf(firstChar) >= 0;
            if (!isVowel) {
                word = word.Substring(1) + firstChar;
            }
            sb.Append(word);
            sb.Append("ma");
            sb.Append(new string('a', i + 1));
            if (i != words.Length - 1) sb.Append(' ');
        }
        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} sentence
 * @return {string}
 */
var toGoatLatin = function(sentence) {
    const vowels = new Set(['a','e','i','o','u','A','E','I','O','U']);
    const words = sentence.split(' ');
    const result = [];
    
    for (let i = 0; i < words.length; i++) {
        let w = words[i];
        if (!vowels.has(w[0])) {
            w = w.slice(1) + w[0];
        }
        w += 'ma' + 'a'.repeat(i + 1);
        result.push(w);
    }
    
    return result.join(' ');
};
```

## Typescript

```typescript
function toGoatLatin(sentence: string): string {
    const vowels = new Set(['a', 'e', 'i', 'o', 'u']);
    const words = sentence.split(' ');
    const result: string[] = [];

    for (let i = 0; i < words.length; i++) {
        const word = words[i];
        const firstChar = word[0];
        const lowerFirst = firstChar.toLowerCase();
        let transformed: string;

        if (vowels.has(lowerFirst)) {
            transformed = word + "ma";
        } else {
            transformed = word.slice(1) + firstChar + "ma";
        }

        transformed += 'a'.repeat(i + 1);
        result.push(transformed);
    }

    return result.join(' ');
}
```

## Php

```php
class Solution {

    /**
     * @param String $sentence
     * @return String
     */
    function toGoatLatin($sentence) {
        $words = explode(' ', $sentence);
        $vowels = ['a','e','i','o','u'];
        foreach ($words as $idx => &$word) {
            $first = strtolower($word[0]);
            if (in_array($first, $vowels)) {
                $newWord = $word . 'ma';
            } else {
                $newWord = substr($word, 1) . $word[0] . 'ma';
            }
            $newWord .= str_repeat('a', $idx + 1);
            $word = $newWord;
        }
        return implode(' ', $words);
    }
}
```

## Swift

```swift
class Solution {
    func toGoatLatin(_ sentence: String) -> String {
        let vowels: Set<Character> = ["a","e","i","o","u","A","E","I","O","U"]
        var result: [String] = []
        let words = sentence.split(separator: " ")
        for (i, sub) in words.enumerated() {
            var word = String(sub)
            if let first = word.first, !vowels.contains(first) {
                word.removeFirst()
                word.append(first)
            }
            word += "ma"
            word += String(repeating: "a", count: i + 1)
            result.append(word)
        }
        return result.joined(separator: " ")
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun toGoatLatin(sentence: String): String {
        val vowels = setOf('a','e','i','o','u','A','E','I','O','U')
        val words = sentence.split(" ")
        val result = StringBuilder()
        for ((index, word) in words.withIndex()) {
            if (index > 0) result.append(' ')
            val transformed = if (vowels.contains(word[0])) {
                word + "ma"
            } else {
                word.substring(1) + word[0] + "ma"
            }
            result.append(transformed)
            repeat(index + 1) { result.append('a') }
        }
        return result.toString()
    }
}
```

## Dart

```dart
class Solution {
  String toGoatLatin(String sentence) {
    List<String> words = sentence.split(' ');
    Set<String> vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
    List<String> result = [];
    for (int i = 0; i < words.length; i++) {
      String w = words[i];
      String transformed;
      if (vowels.contains(w[0])) {
        transformed = w + 'ma';
      } else {
        transformed = w.substring(1) + w[0] + 'ma';
      }
      transformed += List.filled(i + 1, 'a').join();
      result.add(transformed);
    }
    return result.join(' ');
  }
}
```

## Golang

```go
package main

import (
	"strings"
)

func toGoatLatin(sentence string) string {
	words := strings.Split(sentence, " ")
	var b strings.Builder
	for i, w := range words {
		if i > 0 {
			b.WriteByte(' ')
		}
		first := w[0]
		isVowel := first == 'a' || first == 'e' || first == 'i' || first == 'o' || first == 'u' ||
			first == 'A' || first == 'E' || first == 'I' || first == 'O' || first == 'U'
		if isVowel {
			b.WriteString(w)
		} else {
			b.WriteString(w[1:])
			b.WriteByte(first)
		}
		b.WriteString("ma")
		b.WriteString(strings.Repeat("a", i+1))
	}
	return b.String()
}
```

## Ruby

```ruby
def to_goat_latin(sentence)
  vowels = ['a','e','i','o','u','A','E','I','O','U']
  words = sentence.split(' ')
  result = words.each_with_index.map do |word, idx|
    if vowels.include?(word[0])
      transformed = word + "ma"
    else
      transformed = word[1..-1] + word[0] + "ma"
    end
    transformed + 'a' * (idx + 1)
  end
  result.join(' ')
end
```

## Scala

```scala
object Solution {
    def toGoatLatin(sentence: String): String = {
        val vowels = Set('a','e','i','o','u','A','E','I','O','U')
        sentence.split(" ").zipWithIndex.map { case (word, idx) =>
            val transformed = if (vowels.contains(word.charAt(0))) {
                word + "ma"
            } else {
                word.substring(1) + word.charAt(0) + "ma"
            }
            transformed + ("a" * (idx + 1))
        }.mkString(" ")
    }
}
```

## Rust

```rust
impl Solution {
    pub fn to_goat_latin(sentence: String) -> String {
        let mut words = Vec::new();
        for (i, w) in sentence.split_whitespace().enumerate() {
            let idx = i + 1;
            let mut chars = w.chars();
            let first = chars.next().unwrap();
            let rest: String = chars.collect();
            let is_vowel = matches!(first.to_ascii_lowercase(), 'a' | 'e' | 'i' | 'o' | 'u');
            let mut transformed = String::new();
            if is_vowel {
                transformed.push_str(w);
            } else {
                transformed.push_str(&rest);
                transformed.push(first);
            }
            transformed.push_str("ma");
            transformed.extend(std::iter::repeat('a').take(idx));
            words.push(transformed);
        }
        words.join(" ")
    }
}
```

## Racket

```racket
(define/contract (to-goat-latin sentence)
  (-> string? string?)
  (let* ([words (string-split sentence)]
         [vowels '(#\a #\e #\i #\o #\u
                   #\A #\E #\I #\O #\U)]
         [transformed
          (for/list ([w words] [i (in-naturals 1)])
            (let* ([first-char (string-ref w 0)]
                   [base (if (member first-char vowels)
                             w
                             (string-append (substring w 1) (substring w 0 1)))])
              (string-append base "ma" (make-string i #\a))))])
    (string-join transformed " ")))
```

## Erlang

```erlang
-module(solution).
-export([to_goat_latin/1]).

-spec to_goat_latin(Sentence :: unicode:unicode_binary()) -> unicode:unicode_binary().
to_goat_latin(Sentence) ->
    Words = binary:split(Sentence, <<" ">>, [global]),
    {ProcessedRev, _} = lists:foldl(
        fun(Word, {Acc, Idx}) ->
            NewWord = goat_word(Word, Idx),
            {[NewWord | Acc], Idx + 1}
        end,
        {[], 1},
        Words
    ),
    Processed = lists:reverse(ProcessedRev),
    iolist_to_binary(lists:join(<<" ">>, Processed)).

goat_word(Word, Index) ->
    <<First:8, Rest/binary>> = Word,
    Base =
        if is_vowel(First) ->
                <<Word/binary, "ma">>;
           true ->
                <<Rest/binary, First, "ma">>
        end,
    As = list_to_binary(lists:duplicate(Index, $a)),
    <<Base/binary, As/binary>>.

is_vowel(C) when C =:= $a; C =:= $e; C =:= $i; C =:= $o; C =:= $u;
                C =:= $A; C =:= $E; C =:= $I; C =:= $O; C =:= $U -> true;
is_vowel(_) -> false.
```

## Elixir

```elixir
defmodule Solution do
  @spec to_goat_latin(sentence :: String.t()) :: String.t()
  def to_goat_latin(sentence) do
    vowels = MapSet.new(~w[a e i o u A E I O U])

    sentence
    |> String.split(" ")
    |> Enum.with_index(1)
    |> Enum.map(fn {word, idx} ->
      first_char = String.at(word, 0)

      transformed =
        if MapSet.member?(vowels, first_char) do
          word <> "ma"
        else
          rest = String.slice(word, 1..-1)
          rest <> first_char <> "ma"
        end

      transformed <> String.duplicate("a", idx)
    end)
    |> Enum.join(" ")
  end
end
```
