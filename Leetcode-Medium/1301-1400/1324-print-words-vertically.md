# 1324. Print Words Vertically

## Cpp

```cpp
class Solution {
public:
    vector<string> printVertically(string s) {
        vector<string> words;
        string cur;
        for (char c : s) {
            if (c == ' ') {
                words.push_back(cur);
                cur.clear();
            } else {
                cur += c;
            }
        }
        if (!cur.empty()) words.push_back(cur);
        
        size_t max_len = 0;
        for (const auto& w : words) max_len = max(max_len, w.size());
        
        vector<string> result;
        for (size_t i = 0; i < max_len; ++i) {
            string row;
            for (const auto& w : words) {
                if (i < w.size()) row += w[i];
                else row += ' ';
            }
            while (!row.empty() && row.back() == ' ') row.pop_back();
            result.push_back(row);
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public java.util.List<String> printVertically(String s) {
        String[] words = s.split(" ");
        int maxLen = 0;
        for (String w : words) {
            if (w.length() > maxLen) maxLen = w.length();
        }
        java.util.List<String> result = new java.util.ArrayList<>();
        for (int i = 0; i < maxLen; i++) {
            StringBuilder sb = new StringBuilder();
            for (String w : words) {
                if (i < w.length()) {
                    sb.append(w.charAt(i));
                } else {
                    sb.append(' ');
                }
            }
            int end = sb.length() - 1;
            while (end >= 0 && sb.charAt(end) == ' ') {
                end--;
            }
            result.add(sb.substring(0, end + 1));
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        words = s.split()
        max_len = max(len(w) for w in words)
        result = []
        for i in range(max_len):
            col_chars = []
            for w in words:
                if i < len(w):
                    col_chars.append(w[i])
                else:
                    col_chars.append(' ')
            column = ''.join(col_chars).rstrip()
            result.append(column)
        return result
```

## Python3

```python
from typing import List

class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_len = max(len(w) for w in words)
        result = []
        for i in range(max_len):
            row_chars = [w[i] if i < len(w) else ' ' for w in words]
            row = ''.join(row_chars).rstrip()
            result.append(row)
        return result
```

## C

```c
#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char ** printVertically(char * s, int* returnSize){
    // Count words
    int wordCount = 1;
    for (int i = 0; s[i]; ++i) {
        if (s[i] == ' ') wordCount++;
    }
    
    // Split words using strtok (modifies s)
    char **words = (char **)malloc(wordCount * sizeof(char *));
    int *lens = (int *)malloc(wordCount * sizeof(int));
    int maxLen = 0;
    
    char *token = strtok(s, " ");
    for (int i = 0; i < wordCount && token != NULL; ++i) {
        words[i] = token;
        lens[i] = strlen(token);
        if (lens[i] > maxLen) maxLen = lens[i];
        token = strtok(NULL, " ");
    }
    
    // Prepare result
    char **result = (char **)malloc(maxLen * sizeof(char *));
    for (int row = 0; row < maxLen; ++row) {
        char *line = (char *)malloc(wordCount + 1); // max possible length + null
        int pos = 0;
        for (int w = 0; w < wordCount; ++w) {
            if (row < lens[w])
                line[pos++] = words[w][row];
            else
                line[pos++] = ' ';
        }
        line[pos] = '\0';
        // Trim trailing spaces
        int end = pos - 1;
        while (end >= 0 && line[end] == ' ') end--;
        line[end + 1] = '\0';
        result[row] = line;
    }
    
    *returnSize = maxLen;
    
    free(words);
    free(lens);
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public IList<string> PrintVertically(string s) {
        var words = s.Split(' ');
        int maxLen = 0;
        foreach (var w in words)
            if (w.Length > maxLen) maxLen = w.Length;

        var result = new List<string>();
        for (int i = 0; i < maxLen; i++) {
            var sb = new System.Text.StringBuilder();
            foreach (var w in words) {
                if (i < w.Length)
                    sb.Append(w[i]);
                else
                    sb.Append(' ');
            }
            int end = sb.Length - 1;
            while (end >= 0 && sb[end] == ' ') end--;
            result.Add(sb.ToString(0, end + 1));
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string[]}
 */
var printVertically = function(s) {
    const words = s.split(' ');
    const maxLen = Math.max(...words.map(w => w.length));
    const result = [];
    for (let i = 0; i < maxLen; i++) {
        let row = '';
        for (const w of words) {
            row += i < w.length ? w[i] : ' ';
        }
        row = row.replace(/\s+$/g, '');
        result.push(row);
    }
    return result;
};
```

## Typescript

```typescript
function printVertically(s: string): string[] {
    const words = s.split(' ');
    const maxLen = Math.max(...words.map(w => w.length));
    const result: string[] = [];
    for (let i = 0; i < maxLen; i++) {
        let column = '';
        for (const word of words) {
            column += i < word.length ? word[i] : ' ';
        }
        column = column.replace(/\s+$/g, '');
        result.push(column);
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String[]
     */
    function printVertically($s) {
        $words = explode(' ', $s);
        $maxLen = 0;
        foreach ($words as $w) {
            $len = strlen($w);
            if ($len > $maxLen) {
                $maxLen = $len;
            }
        }

        $result = [];
        for ($i = 0; $i < $maxLen; $i++) {
            $row = '';
            foreach ($words as $w) {
                if ($i < strlen($w)) {
                    $row .= $w[$i];
                } else {
                    $row .= ' ';
                }
            }
            $result[] = rtrim($row, ' ');
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func printVertically(_ s: String) -> [String] {
        // Split the string into words and convert each word to an array of characters
        let words = s.split(separator: " ").map { Array($0) }
        guard !words.isEmpty else { return [] }
        
        // Find the maximum length among all words
        let maxLen = words.map { $0.count }.max() ?? 0
        
        var result: [String] = []
        
        // Build each vertical line
        for i in 0..<maxLen {
            var row = ""
            for word in words {
                if i < word.count {
                    row.append(word[i])
                } else {
                    row.append(" ")
                }
            }
            // Trim trailing spaces
            while let last = row.last, last == " " {
                row.removeLast()
            }
            result.append(row)
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun printVertically(s: String): List<String> {
        val words = s.split(" ")
        var maxLen = 0
        for (w in words) if (w.length > maxLen) maxLen = w.length
        val result = mutableListOf<String>()
        for (i in 0 until maxLen) {
            val sb = StringBuilder()
            for (w in words) {
                if (i < w.length) sb.append(w[i]) else sb.append(' ')
            }
            result.add(sb.toString().trimEnd())
        }
        return result
    }
}
```

## Golang

```go
func printVertically(s string) []string {
	words := strings.Split(s, " ")
	maxLen := 0
	for _, w := range words {
		if len(w) > maxLen {
			maxLen = len(w)
		}
	}
	res := make([]string, 0, maxLen)
	for i := 0; i < maxLen; i++ {
		var sb strings.Builder
		for _, w := range words {
			if i < len(w) {
				sb.WriteByte(w[i])
			} else {
				sb.WriteByte(' ')
			}
		}
		row := sb.String()
		end := len(row) - 1
		for end >= 0 && row[end] == ' ' {
			end--
		}
		res = append(res, row[:end+1])
	}
	return res
}
```

## Ruby

```ruby
def print_vertically(s)
  words = s.split(' ')
  max_len = words.map(&:length).max
  result = []
  (0...max_len).each do |i|
    row = words.map { |w| i < w.length ? w[i] : ' ' }.join.rstrip
    result << row
  end
  result
end
```

## Scala

```scala
object Solution {
    def printVertically(s: String): List[String] = {
        val words = s.split(" ")
        val maxLen = words.map(_.length).max
        val res = scala.collection.mutable.ListBuffer[String]()
        for (i <- 0 until maxLen) {
            val sb = new StringBuilder
            for (w <- words) {
                if (i < w.length) sb.append(w.charAt(i))
                else sb.append(' ')
            }
            var end = sb.length - 1
            while (end >= 0 && sb.charAt(end) == ' ') end -= 1
            res += sb.substring(0, end + 1)
        }
        res.toList
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn print_vertically(s: String) -> Vec<String> {
        let words: Vec<&str> = s.split_whitespace().collect();
        let max_len = words.iter().map(|w| w.len()).max().unwrap_or(0);
        let mut result = Vec::new();

        for i in 0..max_len {
            let mut col = String::new();
            for w in &words {
                if i < w.len() {
                    col.push(w.as_bytes()[i] as char);
                } else {
                    col.push(' ');
                }
            }
            while col.ends_with(' ') {
                col.pop();
            }
            result.push(col);
        }

        result
    }
}
```
