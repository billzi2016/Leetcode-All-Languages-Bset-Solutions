# 1768. Merge Strings Alternately

## Cpp

```cpp
class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string res;
        int i = 0, j = 0;
        int m = word1.size(), n = word2.size();
        while (i < m && j < n) {
            res.push_back(word1[i++]);
            res.push_back(word2[j++]);
        }
        if (i < m) res.append(word1.substr(i));
        if (j < n) res.append(word2.substr(j));
        return res;
    }
};
```

## Java

```java
class Solution {
    public String mergeAlternately(String word1, String word2) {
        int m = word1.length(), n = word2.length();
        StringBuilder sb = new StringBuilder(m + n);
        for (int i = 0; i < Math.max(m, n); i++) {
            if (i < m) sb.append(word1.charAt(i));
            if (i < n) sb.append(word2.charAt(i));
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i = j = 0
        m, n = len(word1), len(word2)
        res = []
        while i < m or j < n:
            if i < m:
                res.append(word1[i])
                i += 1
            if j < n:
                res.append(word2[j])
                j += 1
        return ''.join(res)
```

## Python3

```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        res = []
        for i in range(max(m, n)):
            if i < m:
                res.append(word1[i])
            if i < n:
                res.append(word2[i])
        return ''.join(res)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char *mergeAlternately(char *word1, char *word2) {
    size_t len1 = strlen(word1);
    size_t len2 = strlen(word2);
    char *res = (char *)malloc(len1 + len2 + 1);
    if (!res) return NULL;
    size_t i = 0, j = 0, k = 0;
    while (i < len1 && j < len2) {
        res[k++] = word1[i++];
        res[k++] = word2[j++];
    }
    while (i < len1) res[k++] = word1[i++];
    while (j < len2) res[k++] = word2[j++];
    res[k] = '\0';
    return res;
}
```

## Csharp

```csharp
using System.Text;

public class Solution {
    public string MergeAlternately(string word1, string word2) {
        int i = 0, j = 0;
        int m = word1.Length, n = word2.Length;
        StringBuilder sb = new StringBuilder(m + n);
        while (i < m || j < n) {
            if (i < m) sb.Append(word1[i++]);
            if (j < n) sb.Append(word2[j++]);
        }
        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    const m = word1.length;
    const n = word2.length;
    const maxLen = Math.max(m, n);
    const result = [];
    for (let i = 0; i < maxLen; i++) {
        if (i < m) result.push(word1[i]);
        if (i < n) result.push(word2[i]);
    }
    return result.join('');
};
```

## Typescript

```typescript
function mergeAlternately(word1: string, word2: string): string {
    const m = word1.length;
    const n = word2.length;
    const result: string[] = [];
    const maxLen = Math.max(m, n);
    for (let i = 0; i < maxLen; i++) {
        if (i < m) result.push(word1[i]);
        if (i < n) result.push(word2[i]);
    }
    return result.join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String $word1
     * @param String $word2
     * @return String
     */
    function mergeAlternately($word1, $word2) {
        $len1 = strlen($word1);
        $len2 = strlen($word2);
        $maxLen = max($len1, $len2);
        $result = '';
        for ($i = 0; $i < $maxLen; $i++) {
            if ($i < $len1) {
                $result .= $word1[$i];
            }
            if ($i < $len2) {
                $result .= $word2[$i];
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func mergeAlternately(_ word1: String, _ word2: String) -> String {
        let arr1 = Array(word1)
        let arr2 = Array(word2)
        var result = ""
        let m = arr1.count
        let n = arr2.count
        let maxLen = max(m, n)
        for i in 0..<maxLen {
            if i < m { result.append(arr1[i]) }
            if i < n { result.append(arr2[i]) }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun mergeAlternately(word1: String, word2: String): String {
        val sb = StringBuilder()
        val m = word1.length
        val n = word2.length
        val maxLen = if (m > n) m else n
        for (i in 0 until maxLen) {
            if (i < m) sb.append(word1[i])
            if (i < n) sb.append(word2[i])
        }
        return sb.toString()
    }
}
```

## Golang

```go
import "strings"

func mergeAlternately(word1 string, word2 string) string {
	var sb strings.Builder
	i, j := 0, 0
	n1, n2 := len(word1), len(word2)
	for i < n1 || j < n2 {
		if i < n1 {
			sb.WriteByte(word1[i])
			i++
		}
		if j < n2 {
			sb.WriteByte(word2[j])
			j++
		}
	}
	return sb.String()
}
```

## Ruby

```ruby
def merge_alternately(word1, word2)
  m = word1.length
  n = word2.length
  result = +''
  max_len = [m, n].max
  (0...max_len).each do |i|
    result << word1[i, 1] if i < m
    result << word2[i, 1] if i < n
  end
  result
end
```

## Scala

```scala
object Solution {
    def mergeAlternately(word1: String, word2: String): String = {
        val sb = new StringBuilder
        val m = word1.length
        val n = word2.length
        val maxLen = math.max(m, n)
        for (i <- 0 until maxLen) {
            if (i < m) sb.append(word1.charAt(i))
            if (i < n) sb.append(word2.charAt(i))
        }
        sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn merge_alternately(word1: String, word2: String) -> String {
        let b1 = word1.as_bytes();
        let b2 = word2.as_bytes();
        let mut merged = Vec::with_capacity(b1.len() + b2.len());
        let max_len = if b1.len() > b2.len() { b1.len() } else { b2.len() };
        for i in 0..max_len {
            if i < b1.len() {
                merged.push(b1[i]);
            }
            if i < b2.len() {
                merged.push(b2[i]);
            }
        }
        // SAFETY: input strings contain only valid UTF-8 lowercase letters.
        unsafe { String::from_utf8_unchecked(merged) }
    }
}
```

## Racket

```racket
(define/contract (merge-alternately word1 word2)
  (-> string? string? string?)
  (let* ((len1 (string-length word1))
         (len2 (string-length word2))
         (maxlen (max len1 len2)))
    (list->string
     (reverse
      (for/fold ([acc '()]) ([i (in-range maxlen)])
        (let ([acc (if (< i len1)
                       (cons (string-ref word1 i) acc)
                       acc)]
              [acc (if (< i len2)
                       (cons (string-ref word2 i) acc)
                       acc)])
          acc))))))
```
