# 1859. Sorting the Sentence

## Cpp

```cpp
class Solution {
public:
    string sortSentence(string s) {
        vector<string> ordered(10);
        int maxPos = 0;
        string word;
        for (int i = 0, n = s.size(); i <= n; ++i) {
            if (i == n || s[i] == ' ') {
                if (!word.empty()) {
                    int pos = word.back() - '0';
                    word.pop_back();
                    ordered[pos] = word;
                    maxPos = max(maxPos, pos);
                    word.clear();
                }
            } else {
                word.push_back(s[i]);
            }
        }
        string result;
        for (int i = 1; i <= maxPos; ++i) {
            if (!result.empty()) result.push_back(' ');
            result += ordered[i];
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public String sortSentence(String s) {
        String[] words = s.split(" ");
        String[] ordered = new String[words.length];
        for (String w : words) {
            int n = w.length();
            int idx = w.charAt(n - 1) - '0' - 1;
            ordered[idx] = w.substring(0, n - 1);
        }
        return String.join(" ", ordered);
    }
}
```

## Python

```python
class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        ordered = [None] * len(words)
        for w in words:
            pos = int(w[-1]) - 1
            ordered[pos] = w[:-1]
        return " ".join(ordered)
```

## Python3

```python
class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        ordered = [''] * len(words)
        for w in words:
            idx = int(w[-1]) - 1
            ordered[idx] = w[:-1]
        return ' '.join(ordered)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char *sortSentence(char *s) {
    if (!s) return NULL;

    /* Array to hold words at their correct positions (1‑based index). */
    char *ordered[10] = {0};   // indices 1..9
    int wordCount = 0;

    /* Make a mutable copy for tokenization. */
    char *copy = malloc(strlen(s) + 1);
    strcpy(copy, s);

    char *token = strtok(copy, " ");
    while (token) {
        int len = strlen(token);
        if (len == 0) {                     // safety check
            token = strtok(NULL, " ");
            continue;
        }
        int pos = token[len - 1] - '0';     // last character is the position digit

        /* Allocate space for the word without its trailing digit. */
        char *word = malloc(len);           // len includes space for '\0'
        memcpy(word, token, len - 1);
        word[len - 1] = '\0';

        ordered[pos] = word;
        ++wordCount;

        token = strtok(NULL, " ");
    }
    free(copy);

    /* Compute total length needed for the result string. */
    int totalLen = 0;
    for (int i = 1; i <= 9; ++i) {
        if (ordered[i]) totalLen += strlen(ordered[i]);
    }
    totalLen += (wordCount - 1) + 1;   // spaces between words and terminating '\0'

    char *result = malloc(totalLen);
    result[0] = '\0';
    int first = 1;
    for (int i = 1; i <= 9; ++i) {
        if (ordered[i]) {
            if (!first) strcat(result, " ");
            strcat(result, ordered[i]);
            first = 0;
        }
    }

    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public string SortSentence(string s)
    {
        var words = s.Split(' ');
        System.Array.Sort(words, (a, b) => a[^1].CompareTo(b[^1]));
        for (int i = 0; i < words.Length; i++)
        {
            words[i] = words[i][..^1];
        }
        return string.Join(" ", words);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var sortSentence = function(s) {
    const words = s.split(' ');
    const ordered = new Array(words.length);
    for (const w of words) {
        const idx = parseInt(w[w.length - 1], 10) - 1;
        ordered[idx] = w.slice(0, -1);
    }
    return ordered.join(' ');
};
```

## Typescript

```typescript
function sortSentence(s: string): string {
    const words = s.split(' ');
    const ordered: string[] = new Array(words.length);
    for (const w of words) {
        const idx = parseInt(w[w.length - 1]) - 1;
        ordered[idx] = w.slice(0, -1);
    }
    return ordered.join(' ');
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function sortSentence($s) {
        $words = explode(' ', $s);
        $ordered = array_fill(0, count($words), '');
        foreach ($words as $word) {
            $pos = intval(substr($word, -1)) - 1;
            $ordered[$pos] = substr($word, 0, -1);
        }
        return implode(' ', $ordered);
    }
}
```

## Swift

```swift
class Solution {
    func sortSentence(_ s: String) -> String {
        let words = s.split(separator: " ")
        var ordered = Array(repeating: "", count: words.count)
        for w in words {
            let word = String(w)
            guard let lastChar = word.last,
                  let pos = Int(String(lastChar)) else { continue }
            let cleanWord = String(word.dropLast())
            ordered[pos - 1] = cleanWord
        }
        return ordered.joined(separator: " ")
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sortSentence(s: String): String {
        val parts = s.split(' ')
        val ordered = Array(parts.size) { "" }
        for (word in parts) {
            val pos = word.last() - '0'
            ordered[pos - 1] = word.substring(0, word.length - 1)
        }
        return ordered.joinToString(" ")
    }
}
```

## Golang

```go
import "strings"

func sortSentence(s string) string {
	words := strings.Split(s, " ")
	res := make([]string, len(words))
	for _, w := range words {
		n := len(w)
		idx := int(w[n-1]-'0') - 1
		res[idx] = w[:n-1]
	}
	return strings.Join(res, " ")
}
```

## Ruby

```ruby
def sort_sentence(s)
  s.split(' ').sort_by { |word| word[-1].to_i }.map { |word| word[0...-1] }.join(' ')
end
```

## Scala

```scala
object Solution {
    def sortSentence(s: String): String = {
        val words = s.split(" ")
        val result = new Array[String](words.length)
        for (w <- words) {
            val idx = w.last - '0'
            result(idx - 1) = w.substring(0, w.length - 1)
        }
        result.mkString(" ")
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sort_sentence(s: String) -> String {
        let mut pairs: Vec<(usize, String)> = s
            .split_whitespace()
            .map(|w| {
                let len = w.len();
                let pos_char = w.as_bytes()[len - 1] as char;
                let pos = (pos_char as u8 - b'0') as usize;
                let word = &w[..len - 1];
                (pos, word.to_string())
            })
            .collect();

        pairs.sort_by_key(|k| k.0);
        pairs.into_iter().map(|(_, w)| w).collect::<Vec<_>>().join(" ")
    }
}
```

## Racket

```racket
(require racket/string)

(define/contract (sort-sentence s)
  (-> string? string?)
  (let* ((words (string-split s))
         (pairs (for/list ([w words])
                  (let* ((len (string-length w))
                         (pos (string->number (substring w (- len 1))))
                         (word (substring w 0 (- len 1))))
                    (cons pos word))))
         (sorted-pairs (sort pairs (lambda (a b) (< (car a) (car b)))))
         (ordered-words (map cdr sorted-pairs)))
    (string-join ordered-words " ")))
```
