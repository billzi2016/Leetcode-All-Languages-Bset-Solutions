# 0028. Find the Index of the First Occurrence in a String

## Cpp

```cpp
class Solution {
public:
    int strStr(string haystack, string needle) {
        if (needle.empty()) return 0;
        size_t pos = haystack.find(needle);
        return pos == string::npos ? -1 : static_cast<int>(pos);
    }
};
```

## Java

```java
class Solution {
    public int strStr(String haystack, String needle) {
        if (needle.length() == 0) return 0;
        return haystack.indexOf(needle);
    }
}
```

## Python

```python
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0
        if m > n:
            return -1
        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i
        return -1
```

## Python3

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Edge case: empty needle should return 0
        if not needle:
            return 0
        n_len = len(needle)
        h_len = len(haystack)
        # Simple sliding window search
        for i in range(h_len - n_len + 1):
            if haystack[i:i + n_len] == needle:
                return i
        return -1
```

## C

```c
#include <string.h>

int strStr(char* haystack, char* needle) {
    size_t hlen = strlen(haystack);
    size_t nlen = strlen(needle);
    if (nlen == 0) return 0;
    if (hlen < nlen) return -1;
    for (size_t i = 0; i <= hlen - nlen; ++i) {
        if (haystack[i] != needle[0]) continue;
        size_t j = 0;
        while (j < nlen && haystack[i + j] == needle[j]) {
            ++j;
        }
        if (j == nlen) return (int)i;
    }
    return -1;
}
```

## Csharp

```csharp
public class Solution {
    public int StrStr(string haystack, string needle) {
        if (needle.Length == 0) return 0;
        int n = haystack.Length, m = needle.Length;
        if (m > n) return -1;
        for (int i = 0; i <= n - m; i++) {
            int j = 0;
            while (j < m && haystack[i + j] == needle[j]) {
                j++;
            }
            if (j == m) return i;
        }
        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    const n = haystack.length;
    const m = needle.length;
    if (m === 0) return 0;
    for (let i = 0; i <= n - m; i++) {
        let j = 0;
        while (j < m && haystack[i + j] === needle[j]) {
            j++;
        }
        if (j === m) return i;
    }
    return -1;
};
```

## Typescript

```typescript
function strStr(haystack: string, needle: string): number {
    const n = haystack.length;
    const m = needle.length;
    if (m === 0) return 0;
    for (let i = 0; i <= n - m; i++) {
        let j = 0;
        while (j < m && haystack[i + j] === needle[j]) {
            j++;
        }
        if (j === m) return i;
    }
    return -1;
}
```

## Php

```php
class Solution {

    /**
     * @param String $haystack
     * @param String $needle
     * @return Integer
     */
    function strStr($haystack, $needle) {
        if ($needle === "") {
            return 0;
        }
        $pos = strpos($haystack, $needle);
        return $pos === false ? -1 : $pos;
    }
}
```

## Swift

```swift
class Solution {
    func strStr(_ haystack: String, _ needle: String) -> Int {
        if needle.isEmpty { return 0 }
        if let range = haystack.range(of: needle) {
            return haystack.distance(from: haystack.startIndex, to: range.lowerBound)
        }
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun strStr(haystack: String, needle: String): Int {
        return haystack.indexOf(needle)
    }
}
```

## Dart

```dart
class Solution {
  int strStr(String haystack, String needle) {
    if (needle.isEmpty) return 0;
    int n = haystack.length;
    int m = needle.length;
    if (m > n) return -1;
    for (int i = 0; i <= n - m; ++i) {
      int j = 0;
      while (j < m && haystack.codeUnitAt(i + j) == needle.codeUnitAt(j)) {
        j++;
      }
      if (j == m) return i;
    }
    return -1;
  }
}
```

## Golang

```go
func strStr(haystack string, needle string) int {
    n, m := len(haystack), len(needle)
    if m == 0 {
        return 0
    }

    // Build LPS array for KMP algorithm
    lps := make([]int, m)
    length := 0
    i := 1
    for i < m {
        if needle[i] == needle[length] {
            length++
            lps[i] = length
            i++
        } else {
            if length != 0 {
                length = lps[length-1]
            } else {
                lps[i] = 0
                i++
            }
        }
    }

    // Search using KMP
    i, j := 0, 0
    for i < n {
        if haystack[i] == needle[j] {
            i++
            j++
            if j == m {
                return i - j
            }
        } else {
            if j != 0 {
                j = lps[j-1]
            } else {
                i++
            }
        }
    }

    return -1
}
```

## Ruby

```ruby
def str_str(haystack, needle)
  return 0 if needle.empty?
  n = haystack.length
  m = needle.length
  return -1 if m > n
  (0..n - m).each do |i|
    return i if haystack[i, m] == needle
  end
  -1
end
```

## Scala

```scala
object Solution {
    def strStr(haystack: String, needle: String): Int = {
        haystack.indexOf(needle)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        if needle.is_empty() {
            return 0;
        }
        match haystack.find(&needle) {
            Some(idx) => idx as i32,
            None => -1,
        }
    }
}
```

## Racket

```racket
(require racket/string)

(define/contract (str-str haystack needle)
  (-> string? string? exact-integer?)
  (let ([pos (string-index-of haystack needle)])
    (if pos
        pos
        -1)))
```

## Erlang

```erlang
-spec str_str(Haystack :: unicode:unicode_binary(), Needle :: unicode:unicode_binary()) -> integer().
str_str(_Haystack, <<>>) ->
    0;
str_str(Haystack, Needle) ->
    case binary:match(Haystack, Needle) of
        {Pos, _Len} -> Pos;
        nomatch -> -1
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec str_str(haystack :: String.t(), needle :: String.t()) :: integer()
  def str_str(haystack, needle) do
    case String.index(haystack, needle) do
      nil -> -1
      idx -> idx
    end
  end
end
```
