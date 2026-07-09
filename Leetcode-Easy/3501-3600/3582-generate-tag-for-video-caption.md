# 3582. Generate Tag for Video Caption

## Cpp

```cpp
class Solution {
public:
    string generateTag(string caption) {
        vector<string> words;
        string w;
        std::istringstream iss(caption);
        while (iss >> w) {
            words.push_back(w);
        }
        string tag;
        for (size_t i = 0; i < words.size(); ++i) {
            string cur = words[i];
            if (i == 0) {
                for (char &c : cur) c = std::tolower(c);
            } else {
                if (!cur.empty()) cur[0] = std::toupper(cur[0]);
            }
            tag += cur;
        }
        tag = "#" + tag;
        if (tag.size() > 100) tag.resize(100);
        return tag;
    }
};
```

## Java

```java
class Solution {
    public String generateTag(String caption) {
        String[] words = caption.split(" ");
        StringBuilder sb = new StringBuilder();
        sb.append('#');
        for (int i = 0; i < words.length; i++) {
            String w = words[i];
            if (i == 0) {
                sb.append(w.toLowerCase());
            } else {
                if (!w.isEmpty()) {
                    char first = Character.toUpperCase(w.charAt(0));
                    sb.append(first);
                    if (w.length() > 1) {
                        sb.append(w.substring(1));
                    }
                }
            }
        }
        String result = sb.toString();
        if (result.length() > 100) {
            result = result.substring(0, 100);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def generateTag(self, caption):
        """
        :type caption: str
        :rtype: str
        """
        words = caption.split(' ')
        if not words:
            return "#"
        # first word lowercased
        first = words[0].lower()
        # subsequent words title-cased (first letter uppercase, rest lowercase)
        others = []
        for w in words[1:]:
            if w:
                others.append(w[0].upper() + w[1:].lower())
            else:
                others.append('')
        tag_body = first + ''.join(others)
        # prepend '#'
        result = "#" + tag_body
        # enforce max length 100 characters total
        if len(result) > 100:
            # truncate excess from the end of tag_body
            allowed_body_len = 99  # because '#' occupies one character
            result = "#" + tag_body[:allowed_body_len]
        return result
```

## Python3

```python
class Solution:
    def generateTag(self, caption: str) -> str:
        words = caption.split()
        if not words:
            return "#"
        # first word lowercased
        result_parts = [words[0].lower()]
        # subsequent words with capitalized first letter
        for w in words[1:]:
            if w:
                result_parts.append(w[0].upper() + w[1:])
            else:
                result_parts.append("")
        tag = "#" + "".join(result_parts)
        if len(tag) > 100:
            tag = tag[:100]
        return tag
```

## C

```c
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

char* generateTag(char* caption) {
    // Maximum tag length is 100 characters (including the leading '#')
    const int MAX_LEN = 100;
    char *res = (char*)malloc(MAX_LEN + 1); // extra for null terminator
    if (!res) return NULL;

    int idx = 0;
    res[idx++] = '#';

    int n = strlen(caption);
    int i = 0;
    int wordIdx = 0;

    while (i < n && idx < MAX_LEN + 1) {
        // skip spaces
        while (i < n && caption[i] == ' ') i++;
        if (i >= n) break;

        // find end of the word
        int start = i;
        while (i < n && caption[i] != ' ') i++;
        int len = i - start;

        const char *word = caption + start;

        if (wordIdx == 0) {
            for (int j = 0; j < len && idx < MAX_LEN + 1; ++j) {
                res[idx++] = (char)tolower((unsigned char)word[j]);
            }
        } else {
            // first character uppercase
            if (len > 0 && idx < MAX_LEN + 1) {
                res[idx++] = (char)toupper((unsigned char)word[0]);
            }
            for (int j = 1; j < len && idx < MAX_LEN + 1; ++j) {
                res[idx++] = word[j];
            }
        }
        wordIdx++;
    }

    // Ensure null termination
    if (idx > MAX_LEN) idx = MAX_LEN;
    res[idx] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string GenerateTag(string caption) {
        var words = caption.Split(' ', System.StringSplitOptions.RemoveEmptyEntries);
        if (words.Length == 0) return "#";
        var sb = new System.Text.StringBuilder();
        sb.Append(words[0].ToLower());
        for (int i = 1; i < words.Length; i++) {
            string w = words[i];
            if (w.Length > 0) {
                sb.Append(char.ToUpper(w[0]));
                if (w.Length > 1) sb.Append(w.Substring(1));
            }
        }
        string tag = "#" + sb.ToString();
        if (tag.Length > 100) tag = tag.Substring(0, 100);
        return tag;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} caption
 * @return {string}
 */
var generateTag = function(caption) {
    // Split by spaces (multiple spaces not expected per constraints)
    const words = caption.split(' ');
    if (words.length === 0) return "#";
    
    // Process first word: all lowercase
    let first = words[0].toLowerCase();
    
    // Process remaining words: capitalize first letter, keep rest as is
    const processed = [first];
    for (let i = 1; i < words.length; i++) {
        const w = words[i];
        if (w.length === 0) continue;
        const capitalized = w[0].toUpperCase() + w.slice(1);
        processed.push(capitalized);
    }
    
    // Ensure total length (including '#') does not exceed 100
    let totalLen = 1; // for '#'
    for (const p of processed) totalLen += p.length;
    if (totalLen > 100) {
        const excess = totalLen - 100;
        // Trim excess characters from the end of the first word
        processed[0] = processed[0].slice(0, Math.max(0, processed[0].length - excess));
    }
    
    return "#" + processed.join('');
};
```

## Typescript

```typescript
function generateTag(caption: string): string {
    const words = caption.split(' ').filter(w => w.length > 0);
    let tagBody = '';
    for (let i = 0; i < words.length; i++) {
        const w = words[i];
        if (i === 0) {
            tagBody += w.toLowerCase();
        } else {
            tagBody += w[0].toUpperCase() + w.slice(1);
        }
    }
    let result = '#' + tagBody;
    if (result.length > 100) {
        result = result.slice(0, 100);
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $caption
     * @return String
     */
    function generateTag($caption) {
        // Split by whitespace, ignore extra spaces
        $words = preg_split('/\s+/', trim($caption));
        $tagBody = '';
        foreach ($words as $index => $word) {
            if ($index === 0) {
                $tagBody .= strtolower($word);
            } else {
                $firstChar = strtoupper(substr($word, 0, 1));
                $rest = substr($word, 1);
                $tagBody .= $firstChar . $rest;
            }
        }
        $tag = '#' . $tagBody;
        if (strlen($tag) > 100) {
            $tag = substr($tag, 0, 100);
        }
        return $tag;
    }
}
```

## Swift

```swift
class Solution {
    func generateTag(_ caption: String) -> String {
        let words = caption.split(separator: " ")
        guard !words.isEmpty else { return "#" }
        
        var processed: [String] = []
        // first word lowercased
        processed.append(words[0].lowercased())
        
        // remaining words with first letter capitalized
        for w in words.dropFirst() {
            let s = String(w)
            if s.isEmpty {
                processed.append("")
            } else {
                let firstUpper = s.prefix(1).uppercased()
                let rest = s.dropFirst()
                processed.append(firstUpper + rest)
            }
        }
        
        var tagBody = processed.joined()
        // maximum total length is 100, including '#'
        if tagBody.count > 99 {
            let excess = tagBody.count - 99
            var firstPart = processed[0]
            if excess <= firstPart.count {
                firstPart.removeLast(excess)
            } else {
                firstPart = ""
            }
            let rest = processed.dropFirst().joined()
            tagBody = firstPart + rest
        }
        
        return "#" + tagBody
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun generateTag(caption: String): String {
        val words = caption.trim().split("\\s+".toRegex()).filter { it.isNotEmpty() }
        if (words.isEmpty()) return "#"
        val sb = StringBuilder()
        for ((index, w) in words.withIndex()) {
            if (index == 0) {
                sb.append(w.lowercase())
            } else {
                sb.append(w.replaceFirstChar { it.uppercaseChar() })
            }
        }
        var tag = "#" + sb.toString()
        if (tag.length > 100) {
            tag = tag.substring(0, 100)
        }
        return tag
    }
}
```

## Dart

```dart
class Solution {
  String generateTag(String caption) {
    List<String> parts = caption.split(' ');
    StringBuffer sb = StringBuffer('#');
    bool firstWordAdded = false;
    for (int i = 0; i < parts.length; i++) {
      String w = parts[i];
      if (w.isEmpty) continue; // skip extra spaces
      if (!firstWordAdded) {
        sb.write(w.toLowerCase());
        firstWordAdded = true;
      } else {
        String firstChar = w[0].toUpperCase();
        String rest = w.length > 1 ? w.substring(1) : '';
        sb.write(firstChar + rest);
      }
    }
    String tag = sb.toString();
    if (tag.length > 100) {
      tag = tag.substring(0, 100);
    }
    return tag;
  }
}
```

## Golang

```go
package main

import (
	"strings"
	"unicode"
)

func generateTag(caption string) string {
	words := strings.Fields(caption)
	var sb strings.Builder
	sb.WriteByte('#')
	for i, w := range words {
		if i == 0 {
			sb.WriteString(strings.ToLower(w))
		} else {
			runes := []rune(w)
			if len(runes) > 0 {
				runes[0] = unicode.ToUpper(runes[0])
			}
			sb.WriteString(string(runes))
		}
	}
	tag := sb.String()
	if len(tag) > 100 {
		tag = tag[:100]
	}
	return tag
}
```

## Ruby

```ruby
def generate_tag(caption)
  words = caption.split(' ')
  return "" if words.empty?
  processed = words.each_with_index.map do |w, i|
    if i == 0
      w.downcase
    else
      w[0].upcase + w[1..-1]
    end
  end
  tag = "#" + processed.join
  tag.length > 100 ? tag[0, 100] : tag
end
```

## Scala

```scala
object Solution {
    def generateTag(caption: String): String = {
        val words = caption.split(" ").filter(_.nonEmpty)
        if (words.isEmpty) return "#"
        val sb = new StringBuilder
        // first word in lowercase
        sb.append(words(0).toLowerCase)
        // remaining words with first letter capitalized
        for (i <- 1 until words.length) {
            val w = words(i)
            if (w.nonEmpty) {
                sb.append(w.charAt(0).toUpper)
                if (w.length > 1) sb.append(w.substring(1))
            }
        }
        var body = sb.toString()
        // ensure total length including '#' does not exceed 100
        if (body.length > 99) body = body.substring(0, 99)
        "#" + body
    }
}
```

## Rust

```rust
impl Solution {
    pub fn generate_tag(caption: String) -> String {
        let mut tag = String::with_capacity(101);
        tag.push('#');
        for (i, word) in caption.split_whitespace().enumerate() {
            if i == 0 {
                tag.push_str(&word.to_ascii_lowercase());
            } else {
                let mut chars = word.chars();
                if let Some(first) = chars.next() {
                    // capitalize first character
                    for c in first.to_ascii_uppercase().to_string().chars() {
                        tag.push(c);
                    }
                    // keep the rest as is
                    tag.extend(chars);
                }
            }
        }
        if tag.len() > 100 {
            tag.truncate(100);
        }
        tag
    }
}
```

## Racket

```racket
#lang racket
(require racket/string)

(define/contract (generate-tag caption)
  (-> string? string?)
  (let* ([words (string-split caption)]
         [first-word (if (null? words) "" (string-downcase (car words)))]
         [processed-rest (map (lambda (w)
                                (if (zero? (string-length w))
                                    ""
                                    (string-append
                                     (string-upcase (substring w 0 1))
                                     (substring w 1))))
                              (cdr words))]
         [combined (apply string-append (cons first-word processed-rest))]
         [tag (string-append "#" combined)])
    (let ([maxlen 100])
      (if (> (string-length tag) maxlen)
          (substring tag 0 maxlen)
          tag))))
```

## Erlang

```erlang
-spec generate_tag(Caption :: unicode:unicode_binary()) -> unicode:unicode_binary().
generate_tag(Caption) ->
    Words = string:tokens(Caption, " "),
    case Words of
        [] -> <<"#">>;
        [First | Rest] ->
            LowerFirst = string:lowercase(First),
            Caps = [capitalize(W) || W <- Rest],
            Processed = [LowerFirst | Caps],
            Body = lists:foldl(fun (W, Acc) -> <<Acc/binary, W/binary>> end, <<>>, Processed),
            Tag0 = <<"#", Body/binary>>,
            case byte_size(Tag0) > 100 of
                true -> binary:part(Tag0, {0, 100});
                false -> Tag0
            end
    end.

capitalize(W) ->
    case W of
        <<FirstChar, Rest/binary>> ->
            Upper = if FirstChar >= $a, FirstChar =< $z -> FirstChar - 32;
                       true -> FirstChar
                    end,
            <<Upper, Rest/binary>>;
        _ -> <<>>
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec generate_tag(caption :: String.t) :: String.t
  def generate_tag(caption) do
    words =
      caption
      |> String.split(" ", trim: true)

    processed_words =
      words
      |> Enum.with_index()
      |> Enum.map(fn {word, idx} ->
        if idx == 0 do
          String.downcase(word)
        else
          case word do
            "" -> ""
            _ ->
              <<first::binary-size(1), rest::binary>> = word
              String.upcase(first) <> rest
          end
        end
      end)

    tag = "#" <> Enum.join(processed_words, "")

    if String.length(tag) > 100 do
      String.slice(tag, 0, 100)
    else
      tag
    end
  end
end
```
