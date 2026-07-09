# 0068. Text Justification

## Cpp

```cpp
class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> res;
        int n = words.size();
        int i = 0;
        while (i < n) {
            int start = i;
            int lineLen = 0; // total length of words without spaces
            // pack as many words as possible
            while (i < n && lineLen + words[i].size() + (i - start) <= maxWidth) {
                lineLen += words[i].size();
                ++i;
            }
            int gaps = i - start - 1; // number of spaces between words
            string line;
            // last line or a line with a single word -> left justified
            if (i == n || gaps == 0) {
                for (int j = start; j < i; ++j) {
                    line += words[j];
                    if (j != i - 1) line += ' ';
                }
                line.append(maxWidth - line.size(), ' ');
            } else {
                int totalSpaces = maxWidth - lineLen;
                int baseSpace = totalSpaces / gaps;
                int extra = totalSpaces % gaps; // leftmost slots get an extra space
                for (int j = start; j < i; ++j) {
                    line += words[j];
                    if (j != i - 1) {
                        int spaces = baseSpace + (extra > 0 ? 1 : 0);
                        line.append(spaces, ' ');
                        if (extra > 0) --extra;
                    }
                }
            }
            res.push_back(line);
        }
        return res;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> result = new ArrayList<>();
        int index = 0;
        while (index < words.length) {
            int lineLen = words[index].length();
            int last = index + 1;
            // Determine the range of words that fit on this line
            while (last < words.length && lineLen + 1 + words[last].length() <= maxWidth) {
                lineLen += 1 + words[last].length(); // plus one space
                last++;
            }

            StringBuilder sb = new StringBuilder();
            int numWords = last - index;

            // If this is the last line or the line contains only one word -> left justified
            if (last == words.length || numWords == 1) {
                for (int i = index; i < last; i++) {
                    sb.append(words[i]);
                    if (i < last - 1) sb.append(' ');
                }
                // Pad remaining spaces at the end
                int remaining = maxWidth - sb.length();
                while (remaining-- > 0) sb.append(' ');
            } else {
                // Fully justified line
                int sumLen = 0;
                for (int i = index; i < last; i++) sumLen += words[i].length();
                int totalSpaces = maxWidth - sumLen;
                int spacesPerGap = totalSpaces / (numWords - 1);
                int extraSpaces = totalSpaces % (numWords - 1);

                for (int i = index; i < last; i++) {
                    sb.append(words[i]);
                    if (i < last - 1) {
                        int spacesToApply = spacesPerGap + (extraSpaces > 0 ? 1 : 0);
                        extraSpaces--;
                        for (int s = 0; s < spacesToApply; s++) sb.append(' ');
                    }
                }
            }

            result.add(sb.toString());
            index = last;
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        i = 0
        n = len(words)
        while i < n:
            # determine the range of words for the current line
            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            line_words = words[i:j]
            num_words = j - i

            # check if this is the last line
            if j == n or num_words == 1:
                # left-justified
                line = ' '.join(line_words)
                line += ' ' * (maxWidth - len(line))
            else:
                total_spaces = maxWidth - sum(len(w) for w in line_words)
                gaps = num_words - 1
                base, extra = divmod(total_spaces, gaps)

                parts = []
                for k in range(gaps):
                    spaces = base + (1 if k < extra else 0)
                    parts.append(line_words[k] + ' ' * spaces)
                parts.append(line_words[-1])  # last word without extra spaces
                line = ''.join(parts)

            res.append(line)
            i = j

        return res
```

## Python3

```python
from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        n = len(words)
        i = 0
        while i < n:
            j = i
            line_len = 0
            # try to fit as many words as possible
            while j < n and line_len + len(words[j]) + (j - i) <= maxWidth:
                line_len += len(words[j])
                j += 1

            num_words = j - i
            # last line or a line with single word -> left justified
            if j == n or num_words == 1:
                line = ' '.join(words[i:j])
                line += ' ' * (maxWidth - len(line))
            else:
                total_spaces = maxWidth - line_len
                gaps = num_words - 1
                space_per_gap, extra = divmod(total_spaces, gaps)
                parts = []
                for k in range(i, j):
                    parts.append(words[k])
                    if k < j - 1:
                        spaces = space_per_gap + (1 if extra > 0 else 0)
                        extra -= 1 if extra > 0 else 0
                        parts.append(' ' * spaces)
                line = ''.join(parts)

            res.append(line)
            i = j
        return res
```

## C

```c
#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** fullJustify(char** words, int wordsSize, int maxWidth, int* returnSize) {
    char **result = (char **)malloc(sizeof(char *) * wordsSize);
    int lineCount = 0;
    int i = 0;

    while (i < wordsSize) {
        int start = i;
        int lineLen = strlen(words[i]);
        i++;

        // Determine how many words fit in the current line
        while (i < wordsSize && lineLen + 1 + strlen(words[i]) <= maxWidth) {
            lineLen += 1 + strlen(words[i]); // add one space plus word length
            i++;
        }
        int end = i; // exclusive index of next word
        int numWords = end - start;

        // Compute total characters of words in this line
        int sumWordLen = 0;
        for (int k = start; k < end; ++k) {
            sumWordLen += strlen(words[k]);
        }

        char *line = (char *)malloc(sizeof(char) * (maxWidth + 1));
        int pos = 0;

        // Check if this is the last line or a line with a single word
        if (end == wordsSize || numWords == 1) {
            for (int k = start; k < end; ++k) {
                int wlen = strlen(words[k]);
                memcpy(line + pos, words[k], wlen);
                pos += wlen;
                if (k != end - 1) {          // space between words
                    line[pos] = ' ';
                    pos++;
                }
            }
            while (pos < maxWidth) {
                line[pos++] = ' ';
            }
        } else {
            int totalSpaces = maxWidth - sumWordLen;
            int gaps = numWords - 1;
            int baseSpace = totalSpaces / gaps;
            int extra = totalSpaces % gaps; // leftmost gaps get an extra space

            for (int k = start; k < end; ++k) {
                int wlen = strlen(words[k]);
                memcpy(line + pos, words[k], wlen);
                pos += wlen;

                if (k != end - 1) {
                    int spaces = baseSpace + (extra > 0 ? 1 : 0);
                    if (extra > 0) extra--;
                    for (int s = 0; s < spaces; ++s) {
                        line[pos++] = ' ';
                    }
                }
            }
        }

        line[maxWidth] = '\0';
        result[lineCount++] = line;
    }

    *returnSize = lineCount;
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public IList<string> FullJustify(string[] words, int maxWidth) {
        var result = new List<string>();
        int n = words.Length;
        int index = 0;

        while (index < n) {
            int lineStart = index;
            int lineLen = words[index].Length;
            index++;

            // try to fit as many words as possible
            while (index < n && lineLen + 1 + words[index].Length <= maxWidth) {
                lineLen += 1 + words[index].Length; // 1 for at least one space
                index++;
            }

            int lineEnd = index; // exclusive
            int wordCount = lineEnd - lineStart;
            bool isLastLine = lineEnd == n;

            var sb = new System.Text.StringBuilder();

            if (isLastLine || wordCount == 1) {
                // left-justified
                for (int i = lineStart; i < lineEnd; i++) {
                    if (i > lineStart) sb.Append(' ');
                    sb.Append(words[i]);
                }
                // pad remaining spaces
                int remaining = maxWidth - sb.Length;
                sb.Append(' ', remaining);
            } else {
                // fully justified
                int totalWordsLen = 0;
                for (int i = lineStart; i < lineEnd; i++) totalWordsLen += words[i].Length;

                int totalSpaces = maxWidth - totalWordsLen;
                int gaps = wordCount - 1;
                int baseSpace = totalSpaces / gaps;
                int extra = totalSpaces % gaps; // leftmost gaps get an extra space

                for (int i = lineStart; i < lineEnd; i++) {
                    sb.Append(words[i]);
                    if (i < lineEnd - 1) {
                        int spacesToInsert = baseSpace + (extra > 0 ? 1 : 0);
                        sb.Append(' ', spacesToInsert);
                        if (extra > 0) extra--;
                    }
                }
            }

            result.Add(sb.ToString());
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @param {number} maxWidth
 * @return {string[]}
 */
var fullJustify = function(words, maxWidth) {
    const result = [];
    let i = 0;
    while (i < words.length) {
        // Determine the range of words that fit on the current line.
        let lineLen = words[i].length;
        let j = i + 1;
        while (j < words.length && lineLen + 1 + words[j].length <= maxWidth) {
            lineLen += 1 + words[j].length; // add one space plus word length
            j++;
        }
        const lineWords = words.slice(i, j);
        const isLastLine = j === words.length;
        let line = '';
        if (isLastLine || lineWords.length === 1) {
            // Left-justified: join with single spaces and pad the end.
            line = lineWords.join(' ');
            line += ' '.repeat(maxWidth - line.length);
        } else {
            const totalWordLen = lineWords.reduce((sum, w) => sum + w.length, 0);
            const totalSpaces = maxWidth - totalWordLen;
            const gaps = lineWords.length - 1;
            const spacePerGap = Math.floor(totalSpaces / gaps);
            let extra = totalSpaces % gaps; // leftmost gaps get an extra space
            for (let k = 0; k < lineWords.length; k++) {
                line += lineWords[k];
                if (k < gaps) {
                    const spaces = spacePerGap + (extra > 0 ? 1 : 0);
                    line += ' '.repeat(spaces);
                    if (extra > 0) extra--;
                }
            }
        }
        result.push(line);
        i = j;
    }
    return result;
};
```

## Typescript

```typescript
function fullJustify(words: string[], maxWidth: number): string[] {
    const result: string[] = [];
    let index = 0;
    while (index < words.length) {
        let lineLen = words[index].length;
        let last = index + 1;
        while (
            last < words.length &&
            lineLen + 1 + words[last].length <= maxWidth
        ) {
            lineLen += 1 + words[last].length;
            last++;
        }
        const lineWords = words.slice(index, last);
        const isLastLine = last === words.length;
        let line = '';
        if (isLastLine || lineWords.length === 1) {
            line = lineWords.join(' ');
            line += ' '.repeat(maxWidth - line.length);
        } else {
            const totalWordLen = lineWords.reduce((sum, w) => sum + w.length, 0);
            const totalSpaces = maxWidth - totalWordLen;
            const gaps = lineWords.length - 1;
            const baseSpace = Math.floor(totalSpaces / gaps);
            let extra = totalSpaces % gaps; // left slots get an extra space
            for (let i = 0; i < lineWords.length; i++) {
                line += lineWords[i];
                if (i < gaps) {
                    const spaces = baseSpace + (extra > 0 ? 1 : 0);
                    line += ' '.repeat(spaces);
                    if (extra > 0) extra--;
                }
            }
        }
        result.push(line);
        index = last;
    }
    return result;
};
```

## Php

```php
class Solution {

    /**
     * @param String[] $words
     * @param Integer $maxWidth
     * @return String[]
     */
    function fullJustify($words, $maxWidth) {
        $n = count($words);
        $result = [];
        $i = 0;
        while ($i < $n) {
            $lineLen = strlen($words[$i]);
            $j = $i + 1;
            // try to fit as many words as possible
            while ($j < $n && $lineLen + 1 + strlen($words[$j]) <= $maxWidth) {
                $lineLen += 1 + strlen($words[$j]); // one space plus word length
                $j++;
            }

            $numWords = $j - $i;
            $isLastLine = ($j == $n);
            if ($numWords == 1 || $isLastLine) {
                // left-justified
                $line = implode(' ', array_slice($words, $i, $numWords));
                $line .= str_repeat(' ', $maxWidth - strlen($line));
            } else {
                // fully justified
                $totalWordLen = 0;
                for ($k = $i; $k < $j; $k++) {
                    $totalWordLen += strlen($words[$k]);
                }
                $spacesNeeded = $maxWidth - $totalWordLen;
                $gaps = $numWords - 1;
                $spacePerGap = intdiv($spacesNeeded, $gaps);
                $extraSpaces = $spacesNeeded % $gaps; // leftmost gaps get an extra space

                $line = '';
                for ($k = $i; $k < $j; $k++) {
                    $line .= $words[$k];
                    if ($k < $j - 1) {
                        $gapSpaces = $spacePerGap + ($extraSpaces > 0 ? 1 : 0);
                        $line .= str_repeat(' ', $gapSpaces);
                        if ($extraSpaces > 0) {
                            $extraSpaces--;
                        }
                    }
                }
            }

            $result[] = $line;
            $i = $j;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func fullJustify(_ words: [String], _ maxWidth: Int) -> [String] {
        var result = [String]()
        var index = 0
        let n = words.count
        
        while index < n {
            var lineLen = words[index].count
            var next = index + 1
            // Determine the range of words that fit on this line
            while next < n && lineLen + 1 + words[next].count <= maxWidth {
                lineLen += 1 + words[next].count
                next += 1
            }
            
            let isLastLine = (next == n)
            let wordCount = next - index
            var line = ""
            
            if isLastLine || wordCount == 1 {
                // Left-justified: single spaces between words, pad end
                for i in index..<next {
                    line += words[i]
                    if i != next - 1 {
                        line += " "
                    }
                }
                let remaining = maxWidth - line.count
                if remaining > 0 {
                    line += String(repeating: " ", count: remaining)
                }
            } else {
                // Fully justified
                var totalWordsLen = 0
                for i in index..<next {
                    totalWordsLen += words[i].count
                }
                let totalSpaces = maxWidth - totalWordsLen
                let gaps = wordCount - 1
                let spacePerGap = totalSpaces / gaps
                var extra = totalSpaces % gaps   // leftmost gaps get an extra space
                
                for i in index..<next {
                    line += words[i]
                    if i != next - 1 {
                        var spacesToInsert = spacePerGap
                        if extra > 0 {
                            spacesToInsert += 1
                            extra -= 1
                        }
                        line += String(repeating: " ", count: spacesToInsert)
                    }
                }
            }
            
            result.append(line)
            index = next
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun fullJustify(words: Array<String>, maxWidth: Int): List<String> {
        val result = mutableListOf<String>()
        var index = 0
        val n = words.size
        while (index < n) {
            val lineStart = index
            var lineLen = words[index].length
            index++
            while (index < n && lineLen + 1 + words[index].length <= maxWidth) {
                lineLen += 1 + words[index].length
                index++
            }
            val lineEnd = index // exclusive
            val numWords = lineEnd - lineStart
            val isLastLine = index == n
            val sb = StringBuilder()
            if (numWords == 1 || isLastLine) {
                for (j in lineStart until lineEnd) {
                    sb.append(words[j])
                    if (j != lineEnd - 1) sb.append(' ')
                }
                while (sb.length < maxWidth) sb.append(' ')
            } else {
                var wordsLen = 0
                for (j in lineStart until lineEnd) {
                    wordsLen += words[j].length
                }
                val totalSpaces = maxWidth - wordsLen
                val gaps = numWords - 1
                val spacePerGap = totalSpaces / gaps
                var extra = totalSpaces % gaps // leftmost gaps get an extra space
                for (j in lineStart until lineEnd) {
                    sb.append(words[j])
                    if (j != lineEnd - 1) {
                        var spaces = spacePerGap + if (extra > 0) { extra--; 1 } else 0
                        repeat(spaces) { sb.append(' ') }
                    }
                }
            }
            result.add(sb.toString())
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<String> fullJustify(List<String> words, int maxWidth) {
    List<String> result = [];
    int i = 0;
    while (i < words.length) {
      int j = i;
      int lineLen = 0;
      // Determine how many words fit into the current line.
      while (j < words.length &&
          lineLen + words[j].length + (j - i) <= maxWidth) {
        lineLen += words[j].length;
        j++;
      }

      bool isLastLine = j == words.length;
      int wordCount = j - i;
      StringBuffer sb = StringBuffer();

      if (isLastLine || wordCount == 1) {
        // Left-justified.
        for (int k = i; k < j; k++) {
          sb.write(words[k]);
          if (k < j - 1) sb.write(' ');
        }
        int remaining = maxWidth - sb.length;
        sb.write(' ' * remaining);
      } else {
        // Fully justified.
        int totalSpaces = maxWidth - lineLen;
        int gaps = wordCount - 1;
        int baseSpace = totalSpaces ~/ gaps;
        int extra = totalSpaces % gaps;

        for (int k = i; k < j; k++) {
          sb.write(words[k]);
          if (k < j - 1) {
            int spacesToAdd = baseSpace + (extra > 0 ? 1 : 0);
            sb.write(' ' * spacesToAdd);
            if (extra > 0) extra--;
          }
        }
      }

      result.add(sb.toString());
      i = j;
    }
    return result;
  }
}
```

## Golang

```go
package main

import "strings"

func fullJustify(words []string, maxWidth int) []string {
	var res []string
	n := len(words)
	i := 0
	for i < n {
		lineLen := len(words[i])
		j := i + 1
		for j < n && lineLen+1+len(words[j]) <= maxWidth {
			lineLen += 1 + len(words[j])
			j++
		}
		lineWords := words[i:j]
		isLastLine := j == n
		var sb strings.Builder
		if isLastLine || len(lineWords) == 1 {
			for k, w := range lineWords {
				if k > 0 {
					sb.WriteByte(' ')
				}
				sb.WriteString(w)
			}
			remaining := maxWidth - sb.Len()
			sb.WriteString(strings.Repeat(" ", remaining))
		} else {
			totalWordLen := 0
			for _, w := range lineWords {
				totalWordLen += len(w)
			}
			totalSpaces := maxWidth - totalWordLen
			gaps := len(lineWords) - 1
			spacePerGap := totalSpaces / gaps
			extra := totalSpaces % gaps
			for k, w := range lineWords {
				sb.WriteString(w)
				if k < gaps {
					spaces := spacePerGap
					if k < extra {
						spaces++
					}
					sb.WriteString(strings.Repeat(" ", spaces))
				}
			}
		}
		res = append(res, sb.String())
		i = j
	}
	return res
}
```

## Ruby

```ruby
def full_justify(words, max_width)
  result = []
  i = 0
  n = words.length

  while i < n
    line_len = words[i].length
    j = i + 1
    while j < n && line_len + 1 + words[j].length <= max_width
      line_len += 1 + words[j].length
      j += 1
    end

    line_words = words[i...j]

    if j == n || line_words.size == 1
      line = line_words.join(' ')
      line << ' ' * (max_width - line.length)
    else
      total_chars = line_words.reduce(0) { |sum, w| sum + w.length }
      spaces_needed = max_width - total_chars
      gaps = line_words.size - 1
      space_per_gap = spaces_needed / gaps
      extra = spaces_needed % gaps

      line = ''
      line_words.each_with_index do |word, idx|
        line << word
        if idx < gaps
          spaces_to_add = space_per_gap + (idx < extra ? 1 : 0)
          line << ' ' * spaces_to_add
        end
      end
    end

    result << line
    i = j
  end

  result
end
```

## Scala

```scala
object Solution {
    def fullJustify(words: Array[String], maxWidth: Int): List[String] = {
        import scala.collection.mutable.ListBuffer
        val res = ListBuffer[String]()
        var i = 0
        val n = words.length

        while (i < n) {
            var lineLen = words(i).length
            var j = i + 1
            while (j < n && lineLen + 1 + words(j).length <= maxWidth) {
                lineLen += 1 + words(j).length
                j += 1
            }

            val numWords = j - i
            val isLastLine = j == n

            if (isLastLine || numWords == 1) {
                var line = words.slice(i, j).mkString(" ")
                line += " " * (maxWidth - line.length)
                res += line
            } else {
                val totalChars = (i until j).map(words(_).length).sum
                val totalSpaces = maxWidth - totalChars
                val gaps = numWords - 1
                val spacePerGap = totalSpaces / gaps
                var extra = totalSpaces % gaps

                val sb = new StringBuilder
                for (k <- i until j) {
                    sb.append(words(k))
                    if (k < j - 1) {
                        val spaces = spacePerGap + (if (extra > 0) 1 else 0)
                        if (extra > 0) extra -= 1
                        sb.append(" " * spaces)
                    }
                }
                res += sb.toString()
            }

            i = j
        }

        res.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn full_justify(words: Vec<String>, max_width: i32) -> Vec<String> {
        let max_width = max_width as usize;
        let mut result: Vec<String> = Vec::new();
        let mut index = 0usize;

        while index < words.len() {
            // Determine the range of words that fit on this line.
            let mut line_len = words[index].len(); // length of words only
            let mut next = index + 1;
            while next < words.len()
                && line_len + 1 + words[next].len() <= max_width
            {
                line_len += 1 + words[next].len();
                next += 1;
            }

            let is_last_line = next == words.len();
            let word_count = next - index;
            let mut line = String::new();

            if is_last_line || word_count == 1 {
                // Left-justified: single spaces between words, pad end.
                for i in index..next {
                    line.push_str(&words[i]);
                    if i + 1 < next {
                        line.push(' ');
                    }
                }
                let remaining = max_width - line.len();
                line.extend(std::iter::repeat(' ').take(remaining));
            } else {
                // Fully justified.
                let total_word_len: usize = words[index..next].iter().map(|w| w.len()).sum();
                let total_spaces = max_width - total_word_len;
                let gaps = word_count - 1;
                let base_space = total_spaces / gaps;
                let extra = total_spaces % gaps; // leftmost gaps get an extra space

                for i in index..next {
                    line.push_str(&words[i]);
                    if i < next - 1 {
                        let spaces = base_space + if (i - index) < extra { 1 } else { 0 };
                        line.extend(std::iter::repeat(' ').take(spaces));
                    }
                }
            }

            result.push(line);
            index = next;
        }

        result
    }
}
```

## Racket

```racket
(define/contract (full-justify words maxWidth)
  (-> (listof string?) exact-integer? (listof string?))
  
  ;; left‑justified line (last line or single word)
  (define (left-justify ws w)
    (let* ((joined
            (foldl (lambda (word acc)
                     (if (string=? acc "")
                         word
                         (string-append acc " " word)))
                   "" ws))
           (spaces (- w (string-length joined))))
      (string-append joined (make-string spaces #\space))))
  
  ;; fully justified line
  (define (format-line ws last? w)
    (if (or last? (= (length ws) 1))
        (left-justify ws w)
        (let* ((total-words-len (apply + (map string-length ws)))
               (total-spaces   (- w total-words-len))
               (gaps           (- (length ws) 1))
               (base           (quotient total-spaces gaps))
               (extra          (remainder total-spaces gaps)))
          (let loop ((idx 0) (acc ""))
            (if (= idx (length ws))
                acc
                (let* ((word (list-ref ws idx))
                       (space-count (if (< idx gaps)
                                        (+ base (if (< idx extra) 1 0))
                                        0)))
                  (loop (+ idx 1)
                        (string-append acc word
                                       (if (= idx (- (length ws) 1))
                                           ""
                                           (make-string space-count #\space))))))))))
  
  ;; main greedy packing loop
  (let rec ((i 0) (out '()))
    (if (>= i (length words))
        (reverse out)
        (let* ((start i)
               (curr-len (string-length (list-ref words i)))
               (j (+ i 1)))
          (let inner ((j j) (len curr-len))
            (if (or (>= j (length words))
                    (> (+ len 1 (string-length (list-ref words j))) maxWidth))
                (let* ((line-words (sublist words start j))
                       (is-last (= j (length words)))
                       (line (format-line line-words is-last maxWidth)))
                  (rec j (cons line out)))
                (inner (+ j 1) (+ len 1 (string-length (list-ref words j))))))))))
```

## Erlang

```erlang
-module(solution).
-export([full_justify/2]).

-spec full_justify(Words :: [unicode:unicode_binary()], MaxWidth :: integer()) -> [unicode:unicode_binary()].
full_justify(Words, MaxWidth) ->
    Lines = build_lines(Words, [], 0, MaxWidth, []),
    lists:reverse(Lines).

build_lines([], CurrWords, _CurrLen, MaxWidth, Acc) when CurrWords =/= [] ->
    Line = justify_line(lists:reverse(CurrWords), MaxWidth, true),
    [Line | Acc];
build_lines([], [], _CurrLen, _MaxWidth, Acc) ->
    Acc;
build_lines([Word|Rest], CurrWords, CurrLen, MaxWidth, Acc) ->
    WordLen = byte_size(Word),
    case CurrWords of
        [] ->
            build_lines(Rest, [Word], WordLen, MaxWidth, Acc);
        _ ->
            NewLen = CurrLen + 1 + WordLen,
            if NewLen =< MaxWidth ->
                    build_lines(Rest, [Word|CurrWords], NewLen, MaxWidth, Acc);
               true ->
                    Line = justify_line(lists:reverse(CurrWords), MaxWidth, false),
                    build_lines([Word|Rest], [], 0, MaxWidth, [Line | Acc])
            end
    end.

justify_line(Words, MaxWidth, IsLast) ->
    case {length(Words), IsLast} of
        {1, _} ->
            pad_right(lists:nth(1, Words), MaxWidth);
        {_, true} ->
            Joined = join_words(Words, <<" ">>),
            pad_right(iolist_to_binary(Joined), MaxWidth);
        _ ->
            TotalWordsLen = total_len(Words),
            Gaps = length(Words) - 1,
            SpacesNeeded = MaxWidth - TotalWordsLen,
            Base = SpacesNeeded div Gaps,
            Extra = SpacesNeeded rem Gaps,
            iolist_to_binary(build_full_line(Words, Base, Extra))
    end.

total_len(Words) ->
    lists:foldl(fun(W, Acc) -> Acc + byte_size(W) end, 0, Words).

pad_right(Str, MaxWidth) ->
    PadSize = MaxWidth - byte_size(Str),
    Pad = binary:copy(<<" ">>, PadSize),
    <<Str/binary, Pad/binary>>.

join_words([W], _Sep) -> W;
join_words([W|Rest], Sep) ->
    [W, Sep, join_words(Rest, Sep)].

build_full_line([Word], _Base, _Extra) ->
    Word;
build_full_line([Word|Rest], Base, Extra) when Rest =/= [] ->
    SpaceCount = Base + (if Extra > 0 -> 1; true -> 0 end),
    NewExtra = if Extra > 0 -> Extra - 1; true -> Extra end,
    [Word, binary:copy(<<" ">>, SpaceCount), build_full_line(Rest, Base, NewExtra)].
```

## Elixir

```elixir
defmodule Solution do
  @spec full_justify(words :: [String.t()], max_width :: integer) :: [String.t()]
  def full_justify(words, max_width) do
    {lines_rev, cur_words, cur_len} =
      Enum.reduce(words, {[], [], 0}, fn word, {res_rev, cur, len} ->
        wlen = String.length(word)

        if len + wlen + length(cur) <= max_width do
          {res_rev, cur ++ [word], len + wlen}
        else
          line = justify_line(cur, len, max_width, false)
          {[line | res_rev], [word], wlen}
        end
      end)

    last_line = justify_line(cur_words, cur_len, max_width, true)
    Enum.reverse(lines_rev) ++ [last_line]
  end

  defp justify_line(words, letters_len, max_width, last?) do
    cond do
      last? or length(words) == 1 ->
        line = Enum.join(words, " ")
        pad = max_width - String.length(line)
        line <> String.duplicate(" ", pad)

      true ->
        total_spaces = max_width - letters_len
        gaps = length(words) - 1
        space_per_gap = div(total_spaces, gaps)
        extra = rem(total_spaces, gaps)

        Enum.reduce(Enum.with_index(words), "", fn {word, idx}, acc ->
          if idx < gaps do
            spaces = space_per_gap + (if idx < extra, do: 1, else: 0)
            acc <> word <> String.duplicate(" ", spaces)
          else
            acc <> word
          end
        end)
    end
  end
end
```
