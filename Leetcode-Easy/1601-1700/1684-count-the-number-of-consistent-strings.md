# 1684. Count the Number of Consistent Strings

## Cpp

```cpp
class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        int mask = 0;
        for (char c : allowed) {
            mask |= 1 << (c - 'a');
        }
        int cnt = 0;
        for (const string& w : words) {
            bool ok = true;
            for (char c : w) {
                if ((mask & (1 << (c - 'a'))) == 0) {
                    ok = false;
                    break;
                }
            }
            if (ok) ++cnt;
        }
        return cnt;
    }
};
```

## Java

```java
class Solution {
    public int countConsistentStrings(String allowed, String[] words) {
        int mask = 0;
        for (int i = 0; i < allowed.length(); ++i) {
            mask |= 1 << (allowed.charAt(i) - 'a');
        }
        int count = 0;
        outer:
        for (String word : words) {
            for (int j = 0; j < word.length(); ++j) {
                if ((mask & (1 << (word.charAt(j) - 'a'))) == 0) {
                    continue outer;
                }
            }
            count++;
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        mask = 0
        for c in allowed:
            mask |= 1 << (ord(c) - ord('a'))
        cnt = 0
        for w in words:
            ok = True
            for ch in w:
                if not (mask >> (ord(ch) - ord('a')) & 1):
                    ok = False
                    break
            if ok:
                cnt += 1
        return cnt
```

## Python3

```python
from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        mask = 0
        for c in allowed:
            mask |= 1 << (ord(c) - ord('a'))
        consistent = 0
        for word in words:
            for ch in word:
                if not (mask >> (ord(ch) - ord('a')) & 1):
                    break
            else:
                consistent += 1
        return consistent
```

## C

```c
int countConsistentStrings(char *allowed, char **words, int wordsSize){
    unsigned int mask = 0;
    for (char *p = allowed; *p; ++p)
        mask |= 1u << (*p - 'a');
    
    int result = 0;
    for (int i = 0; i < wordsSize; ++i) {
        char *w = words[i];
        int ok = 1;
        for (char *c = w; *c; ++c) {
            if (((mask >> (*c - 'a')) & 1u) == 0) {
                ok = 0;
                break;
            }
        }
        if (ok)
            ++result;
    }
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int CountConsistentStrings(string allowed, string[] words)
    {
        int mask = 0;
        foreach (char c in allowed)
        {
            mask |= 1 << (c - 'a');
        }

        int count = 0;
        foreach (string word in words)
        {
            bool consistent = true;
            foreach (char ch in word)
            {
                if ((mask & (1 << (ch - 'a'))) == 0)
                {
                    consistent = false;
                    break;
                }
            }
            if (consistent) count++;
        }

        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} allowed
 * @param {string[]} words
 * @return {number}
 */
var countConsistentStrings = function(allowed, words) {
    let mask = 0;
    for (let i = 0; i < allowed.length; ++i) {
        mask |= 1 << (allowed.charCodeAt(i) - 97);
    }
    let cnt = 0;
    wordLoop: for (const w of words) {
        for (let j = 0; j < w.length; ++j) {
            if (((mask >> (w.charCodeAt(j) - 97)) & 1) === 0) {
                continue wordLoop;
            }
        }
        ++cnt;
    }
    return cnt;
};
```

## Typescript

```typescript
function countConsistentStrings(allowed: string, words: string[]): number {
    let mask = 0;
    for (let i = 0; i < allowed.length; ++i) {
        mask |= 1 << (allowed.charCodeAt(i) - 97);
    }
    let count = 0;
    for (const word of words) {
        let ok = true;
        for (let i = 0; i < word.length; ++i) {
            if ((mask & (1 << (word.charCodeAt(i) - 97))) === 0) {
                ok = false;
                break;
            }
        }
        if (ok) ++count;
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param String $allowed
     * @param String[] $words
     * @return Integer
     */
    function countConsistentStrings($allowed, $words) {
        $mask = 0;
        $lenAllowed = strlen($allowed);
        for ($i = 0; $i < $lenAllowed; $i++) {
            $bit = ord($allowed[$i]) - 97; // 'a' ASCII is 97
            $mask |= (1 << $bit);
        }

        $consistentCount = 0;
        foreach ($words as $word) {
            $isConsistent = true;
            $lenWord = strlen($word);
            for ($j = 0; $j < $lenWord; $j++) {
                $bit = ord($word[$j]) - 97;
                if ((($mask >> $bit) & 1) === 0) {
                    $isConsistent = false;
                    break;
                }
            }
            if ($isConsistent) {
                $consistentCount++;
            }
        }

        return $consistentCount;
    }
}
```

## Swift

```swift
class Solution {
    func countConsistentStrings(_ allowed: String, _ words: [String]) -> Int {
        var mask = 0
        for ch in allowed.unicodeScalars {
            let idx = Int(ch.value - 97)
            mask |= (1 << idx)
        }
        var result = 0
        wordLoop: for word in words {
            for ch in word.unicodeScalars {
                let idx = Int(ch.value - 97)
                if (mask & (1 << idx)) == 0 {
                    continue wordLoop
                }
            }
            result += 1
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countConsistentStrings(allowed: String, words: Array<String>): Int {
        var mask = 0
        for (c in allowed) {
            mask = mask or (1 shl (c - 'a'))
        }
        var count = 0
        for (word in words) {
            var ok = true
            for (ch in word) {
                if ((mask and (1 shl (ch - 'a'))) == 0) {
                    ok = false
                    break
                }
            }
            if (ok) count++
        }
        return count
    }
}
```

## Golang

```go
func countConsistentStrings(allowed string, words []string) int {
    var allowedSet [26]bool
    for _, ch := range allowed {
        allowedSet[ch-'a'] = true
    }

    consistentCount := 0
    for _, word := range words {
        isConsistent := true
        for _, ch := range word {
            if !allowedSet[ch-'a'] {
                isConsistent = false
                break
            }
        }
        if isConsistent {
            consistentCount++
        }
    }
    return consistentCount
}
```

## Ruby

```ruby
def count_consistent_strings(allowed, words)
  mask = 0
  allowed.each_byte { |b| mask |= 1 << (b - 97) }
  count = 0
  words.each do |word|
    ok = true
    word.each_byte do |b|
      if ((mask >> (b - 97)) & 1).zero?
        ok = false
        break
      end
    end
    count += 1 if ok
  end
  count
end
```

## Scala

```scala
object Solution {
    def countConsistentStrings(allowed: String, words: Array[String]): Int = {
        var mask = 0
        for (c <- allowed) {
            mask |= 1 << (c - 'a')
        }
        var count = 0
        for (w <- words) {
            var ok = true
            var i = 0
            while (i < w.length && ok) {
                val bit = (mask >> (w.charAt(i) - 'a')) & 1
                if (bit == 0) ok = false
                i += 1
            }
            if (ok) count += 1
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_consistent_strings(allowed: String, words: Vec<String>) -> i32 {
        let mut allowed_set = [false; 26];
        for b in allowed.bytes() {
            allowed_set[(b - b'a') as usize] = true;
        }

        let mut count = 0i32;
        for word in words.iter() {
            let mut ok = true;
            for b in word.bytes() {
                if !allowed_set[(b - b'a') as usize] {
                    ok = false;
                    break;
                }
            }
            if ok {
                count += 1;
            }
        }
        count
    }
}
```
