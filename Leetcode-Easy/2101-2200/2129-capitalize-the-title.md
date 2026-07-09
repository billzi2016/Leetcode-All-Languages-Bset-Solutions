# 2129. Capitalize the Title

## Cpp

```cpp
class Solution {
public:
    string capitalizeTitle(string title) {
        string result;
        int n = title.size();
        for (int i = 0; i < n; ) {
            int j = i;
            while (j < n && title[j] != ' ') ++j;
            string word = title.substr(i, j - i);
            if (word.length() <= 2) {
                for (char &c : word) c = tolower(c);
            } else {
                word[0] = toupper(word[0]);
                for (size_t k = 1; k < word.size(); ++k) word[k] = tolower(word[k]);
            }
            result += word;
            if (j < n) {
                result.push_back(' ');
                ++j;
            }
            i = j;
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public String capitalizeTitle(String title) {
        String[] words = title.split(" ");
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < words.length; i++) {
            String w = words[i];
            if (w.length() <= 2) {
                sb.append(w.toLowerCase());
            } else {
                sb.append(Character.toUpperCase(w.charAt(0)));
                sb.append(w.substring(1).toLowerCase());
            }
            if (i < words.length - 1) sb.append(' ');
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        words = title.split(' ')
        result = []
        for w in words:
            if len(w) <= 2:
                result.append(w.lower())
            else:
                result.append(w[0].upper() + w[1:].lower())
        return ' '.join(result)
```

## Python3

```python
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split(' ')
        result = []
        for w in words:
            if len(w) <= 2:
                result.append(w.lower())
            else:
                result.append(w[0].upper() + w[1:].lower())
        return ' '.join(result)
```

## C

```c
#include <string.h>
#include <ctype.h>

char* capitalizeTitle(char* title) {
    int n = strlen(title);
    int i = 0;
    while (i < n) {
        int start = i;
        while (i < n && title[i] != ' ') {
            i++;
        }
        int len = i - start;
        for (int j = start; j < i; ++j) {
            if (len <= 2) {
                title[j] = tolower((unsigned char)title[j]);
            } else {
                if (j == start)
                    title[j] = toupper((unsigned char)title[j]);
                else
                    title[j] = tolower((unsigned char)title[j]);
            }
        }
        // skip the space character
        i++;
    }
    return title;
}
```

## Csharp

```csharp
public class Solution {
    public string CapitalizeTitle(string title) {
        var words = title.Split(' ');
        for (int i = 0; i < words.Length; i++) {
            string w = words[i].ToLower();
            if (w.Length > 2) {
                w = char.ToUpper(w[0]) + w.Substring(1);
            }
            words[i] = w;
        }
        return string.Join(" ", words);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} title
 * @return {string}
 */
var capitalizeTitle = function(title) {
    return title.split(' ').map(word => {
        if (word.length <= 2) {
            return word.toLowerCase();
        }
        const lower = word.toLowerCase();
        return lower[0].toUpperCase() + lower.slice(1);
    }).join(' ');
};
```

## Typescript

```typescript
function capitalizeTitle(title: string): string {
    return title
        .split(' ')
        .map(word => {
            const lower = word.toLowerCase();
            if (lower.length <= 2) return lower;
            return lower[0].toUpperCase() + lower.slice(1);
        })
        .join(' ');
}
```

## Php

```php
class Solution {

    /**
     * @param String $title
     * @return String
     */
    function capitalizeTitle($title) {
        $words = explode(' ', $title);
        foreach ($words as &$w) {
            if (strlen($w) <= 2) {
                $w = strtolower($w);
            } else {
                $first = strtoupper($w[0]);
                $rest = strtolower(substr($w, 1));
                $w = $first . $rest;
            }
        }
        return implode(' ', $words);
    }
}
```

## Swift

```swift
class Solution {
    func capitalizeTitle(_ title: String) -> String {
        let words = title.split(separator: " ")
        var transformed: [String] = []
        for wordSub in words {
            let word = String(wordSub)
            if word.count <= 2 {
                transformed.append(word.lowercased())
            } else {
                let first = word.prefix(1).uppercased()
                let rest = word.dropFirst().lowercased()
                transformed.append(first + rest)
            }
        }
        return transformed.joined(separator: " ")
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun capitalizeTitle(title: String): String {
        return title.split(' ').joinToString(" ") { word ->
            if (word.length <= 2) {
                word.lowercase()
            } else {
                word.substring(0, 1).uppercase() + word.substring(1).lowercase()
            }
        }
    }
}
```

## Dart

```dart
class Solution {
  String capitalizeTitle(String title) {
    List<String> words = title.split(' ');
    for (int i = 0; i < words.length; i++) {
      String w = words[i];
      if (w.length <= 2) {
        words[i] = w.toLowerCase();
      } else {
        String first = w[0].toUpperCase();
        String rest = w.substring(1).toLowerCase();
        words[i] = first + rest;
      }
    }
    return words.join(' ');
  }
}
```

## Golang

```go
import "strings"

func capitalizeTitle(title string) string {
	words := strings.Split(title, " ")
	for i, w := range words {
		lw := strings.ToLower(w)
		if len(lw) > 2 {
			b := []byte(lw)
			if b[0] >= 'a' && b[0] <= 'z' {
				b[0] = b[0] - ('a' - 'A')
			}
			words[i] = string(b)
		} else {
			words[i] = lw
		}
	}
	return strings.Join(words, " ")
}
```

## Ruby

```ruby
def capitalize_title(title)
  title.split(' ').map do |word|
    if word.length <= 2
      word.downcase
    else
      word[0].upcase + word[1..-1].downcase
    end
  end.join(' ')
end
```

## Scala

```scala
object Solution {
    def capitalizeTitle(title: String): String = {
        title.split(" ").map { w =>
            if (w.length <= 2) w.toLowerCase
            else w.head.toUpper + w.tail.toLowerCase
        }.mkString(" ")
    }
}
```

## Rust

```rust
impl Solution {
    pub fn capitalize_title(title: String) -> String {
        let words: Vec<String> = title
            .split(' ')
            .map(|w| {
                if w.chars().count() <= 2 {
                    w.to_ascii_lowercase()
                } else {
                    let mut chars = w.chars();
                    let first = chars.next().unwrap().to_ascii_uppercase();
                    let rest: String = chars.map(|c| c.to_ascii_lowercase()).collect();
                    format!("{}{}", first, rest)
                }
            })
            .collect();
        words.join(" ")
    }
}
```

## Racket

```racket
(require racket/string)

(define/contract (capitalize-title title)
  (-> string? string?)
  (let* ([words (string-split title " ")]
         [proc (lambda (w)
                 (if (<= (string-length w) 2)
                     (string-downcase w)
                     (string-append (string-upcase (substring w 0 1))
                                    (string-downcase (substring w 1)))) )]
         [new-words (map proc words)])
    (string-join new-words " ")))
```

## Erlang

```erlang
-spec capitalize_title(Title :: unicode:unicode_binary()) -> unicode:unicode_binary().
capitalize_title(Title) ->
    Words = binary:split(Title, <<" ">>, [global]),
    NewWords = [process_word(W) || W <- Words],
    string:join(NewWords, " ").

process_word(W) when byte_size(W) =< 2 ->
    string:lowercase(W);
process_word(W) ->
    <<F, Rest/binary>> = W,
    UpperF = string:uppercase(<<F>>),
    LowerRest = string:lowercase(Rest),
    <<UpperF/binary, LowerRest/binary>>.
```

## Elixir

```elixir
defmodule Solution do
  @spec capitalize_title(title :: String.t) :: String.t
  def capitalize_title(title) do
    title
    |> String.split(" ")
    |> Enum.map(fn word ->
      if String.length(word) <= 2 do
        String.downcase(word)
      else
        String.capitalize(word)
      end
    end)
    |> Enum.join(" ")
  end
end
```
