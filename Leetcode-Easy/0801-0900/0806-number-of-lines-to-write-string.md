# 0806. Number of Lines To Write String

## Cpp

```cpp
class Solution {
public:
    vector<int> numberOfLines(vector<int>& widths, string s) {
        int lines = 1;
        int cur = 0;
        for (char c : s) {
            int w = widths[c - 'a'];
            if (cur + w > 100) {
                ++lines;
                cur = w;
            } else {
                cur += w;
            }
        }
        return {lines, cur};
    }
};
```

## Java

```java
class Solution {
    public int[] numberOfLines(int[] widths, String s) {
        int lines = 1;
        int curWidth = 0;
        for (int i = 0; i < s.length(); i++) {
            int w = widths[s.charAt(i) - 'a'];
            if (curWidth + w > 100) {
                lines++;
                curWidth = w;
            } else {
                curWidth += w;
            }
        }
        return new int[]{lines, curWidth};
    }
}
```

## Python

```python
class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        lines = 1
        cur_width = 0
        for ch in s:
            w = widths[ord(ch) - ord('a')]
            if cur_width + w > 100:
                lines += 1
                cur_width = w
            else:
                cur_width += w
        return [lines, cur_width]
```

## Python3

```python
from typing import List

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        cur_width = 0
        for ch in s:
            w = widths[ord(ch) - ord('a')]
            if cur_width + w > 100:
                lines += 1
                cur_width = w
            else:
                cur_width += w
        return [lines, cur_width]
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* numberOfLines(int* widths, int widthsSize, char * s, int* returnSize){
    int lines = 1;
    int curWidth = 0;
    for (char *p = s; *p != '\0'; ++p) {
        int w = widths[*p - 'a'];
        if (curWidth + w > 100) {
            lines++;
            curWidth = w;
        } else {
            curWidth += w;
        }
    }
    int* result = (int*)malloc(2 * sizeof(int));
    result[0] = lines;
    result[1] = curWidth;
    *returnSize = 2;
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int[] NumberOfLines(int[] widths, string s) {
        int lines = 1;
        int curWidth = 0;
        foreach (char c in s) {
            int w = widths[c - 'a'];
            if (curWidth + w > 100) {
                lines++;
                curWidth = w;
            } else {
                curWidth += w;
            }
        }
        return new int[] { lines, curWidth };
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} widths
 * @param {string} s
 * @return {number[]}
 */
var numberOfLines = function(widths, s) {
    let lines = 1;
    let curWidth = 0;
    for (let i = 0; i < s.length; i++) {
        const w = widths[s.charCodeAt(i) - 97];
        if (curWidth + w > 100) {
            lines++;
            curWidth = w;
        } else {
            curWidth += w;
        }
    }
    return [lines, curWidth];
};
```

## Typescript

```typescript
function numberOfLines(widths: number[], s: string): number[] {
    let lines = 1;
    let cur = 0;
    for (let i = 0; i < s.length; i++) {
        const w = widths[s.charCodeAt(i) - 97];
        if (cur + w > 100) {
            lines++;
            cur = w;
        } else {
            cur += w;
        }
    }
    return [lines, cur];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $widths
     * @param String $s
     * @return Integer[]
     */
    function numberOfLines($widths, $s) {
        $lines = 1;
        $currWidth = 0;
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $idx = ord($s[$i]) - ord('a');
            $w = $widths[$idx];
            if ($currWidth + $w > 100) {
                $lines++;
                $currWidth = $w;
            } else {
                $currWidth += $w;
            }
        }
        return [$lines, $currWidth];
    }
}
```

## Swift

```swift
class Solution {
    func numberOfLines(_ widths: [Int], _ s: String) -> [Int] {
        var lines = 1
        var currentWidth = 0
        let aValue = UnicodeScalar("a").value
        for scalar in s.unicodeScalars {
            let index = Int(scalar.value - aValue)
            let w = widths[index]
            if currentWidth + w > 100 {
                lines += 1
                currentWidth = w
            } else {
                currentWidth += w
            }
        }
        return [lines, currentWidth]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfLines(widths: IntArray, s: String): IntArray {
        var lines = 1
        var curWidth = 0
        for (ch in s) {
            val w = widths[ch - 'a']
            if (curWidth + w > 100) {
                lines++
                curWidth = w
            } else {
                curWidth += w
            }
        }
        return intArrayOf(lines, curWidth)
    }
}
```

## Golang

```go
func numberOfLines(widths []int, s string) []int {
    lines, cur := 1, 0
    for i := 0; i < len(s); i++ {
        w := widths[s[i]-'a']
        if cur+w > 100 {
            lines++
            cur = w
        } else {
            cur += w
        }
    }
    return []int{lines, cur}
}
```

## Ruby

```ruby
# @param {Integer[]} widths
# @param {String} s
# @return {Integer[]}
def number_of_lines(widths, s)
  lines = 1
  cur_width = 0
  base = 'a'.ord
  s.each_char do |ch|
    w = widths[ch.ord - base]
    if cur_width + w > 100
      lines += 1
      cur_width = w
    else
      cur_width += w
    end
  end
  [lines, cur_width]
end
```

## Scala

```scala
object Solution {
    def numberOfLines(widths: Array[Int], s: String): Array[Int] = {
        var lines = 1
        var curWidth = 0
        for (ch <- s) {
            val w = widths(ch - 'a')
            if (curWidth + w > 100) {
                lines += 1
                curWidth = w
            } else {
                curWidth += w
            }
        }
        Array(lines, curWidth)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_lines(widths: Vec<i32>, s: String) -> Vec<i32> {
        let mut lines = 1;
        let mut cur_width = 0;
        for b in s.bytes() {
            let w = widths[(b - b'a') as usize];
            if cur_width + w > 100 {
                lines += 1;
                cur_width = w;
            } else {
                cur_width += w;
            }
        }
        vec![lines, cur_width]
    }
}
```
