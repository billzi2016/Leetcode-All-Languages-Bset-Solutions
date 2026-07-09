# 2414. Length of the Longest Alphabetical Continuous Substring

## Cpp

```cpp
class Solution {
public:
    int longestContinuousSubstring(string s) {
        int n = s.size();
        if (n == 0) return 0;
        int maxLen = 1, curLen = 1;
        for (int i = 1; i < n; ++i) {
            if (s[i] - s[i-1] == 1) {
                ++curLen;
            } else {
                curLen = 1;
            }
            if (curLen > maxLen) maxLen = curLen;
        }
        return maxLen;
    }
};
```

## Java

```java
class Solution {
    public int longestContinuousSubstring(String s) {
        int n = s.length();
        int maxLen = 1;
        int curLen = 1;
        for (int i = 1; i < n; i++) {
            if (s.charAt(i) - s.charAt(i - 1) == 1) {
                curLen++;
            } else {
                curLen = 1;
            }
            if (curLen > maxLen) {
                maxLen = curLen;
            }
        }
        return maxLen;
    }
}
```

## Python

```python
class Solution(object):
    def longestContinuousSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 1
        cur_len = 1
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i-1]) == 1:
                cur_len += 1
            else:
                cur_len = 1
            if cur_len > max_len:
                max_len = cur_len
        return max_len
```

## Python3

```python
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_len = cur = 1
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i - 1]) == 1:
                cur += 1
            else:
                cur = 1
            if cur > max_len:
                max_len = cur
        return max_len
```

## C

```c
int longestContinuousSubstring(char* s) {
    if (!s || !*s) return 0;
    int maxLen = 1, curLen = 1;
    for (char *p = s + 1; *p; ++p) {
        if (*p == *(p - 1) + 1) {
            ++curLen;
        } else {
            curLen = 1;
        }
        if (curLen > maxLen) maxLen = curLen;
    }
    return maxLen;
}
```

## Csharp

```csharp
public class Solution
{
    public int LongestContinuousSubstring(string s)
    {
        if (string.IsNullOrEmpty(s)) return 0;

        int maxLen = 1, curLen = 1;
        for (int i = 1; i < s.Length; i++)
        {
            if (s[i] - s[i - 1] == 1)
                curLen++;
            else
                curLen = 1;

            if (curLen > maxLen) maxLen = curLen;
        }
        return maxLen;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var longestContinuousSubstring = function(s) {
    let maxLen = 0;
    let curLen = 0;
    for (let i = 0; i < s.length; i++) {
        if (i > 0 && s.charCodeAt(i) === s.charCodeAt(i - 1) + 1) {
            curLen += 1;
        } else {
            curLen = 1;
        }
        if (curLen > maxLen) maxLen = curLen;
    }
    return maxLen;
};
```

## Typescript

```typescript
function longestContinuousSubstring(s: string): number {
    const n = s.length;
    if (n === 0) return 0;
    let maxLen = 1;
    let curLen = 1;
    for (let i = 1; i < n; i++) {
        if (s.charCodeAt(i) - s.charCodeAt(i - 1) === 1) {
            curLen++;
        } else {
            curLen = 1;
        }
        if (curLen > maxLen) maxLen = curLen;
    }
    return maxLen;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function longestContinuousSubstring($s) {
        $n = strlen($s);
        if ($n == 0) return 0;
        $max = 1;
        $cur = 1;
        for ($i = 1; $i < $n; $i++) {
            if (ord($s[$i]) - ord($s[$i - 1]) === 1) {
                $cur++;
            } else {
                $cur = 1;
            }
            if ($cur > $max) {
                $max = $cur;
            }
        }
        return $max;
    }
}
```

## Swift

```swift
class Solution {
    func longestContinuousSubstring(_ s: String) -> Int {
        let bytes = Array(s.utf8)
        if bytes.isEmpty { return 0 }
        var maxLen = 1
        var cur = 1
        for i in 1..<bytes.count {
            if bytes[i] == bytes[i - 1] + 1 {
                cur += 1
            } else {
                cur = 1
            }
            if cur > maxLen { maxLen = cur }
        }
        return maxLen
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestContinuousSubstring(s: String): Int {
        var maxLen = 1
        var curLen = 1
        for (i in 1 until s.length) {
            if (s[i] - s[i - 1] == 1) {
                curLen++
            } else {
                curLen = 1
            }
            if (curLen > maxLen) maxLen = curLen
        }
        return maxLen
    }
}
```

## Dart

```dart
class Solution {
  int longestContinuousSubstring(String s) {
    int maxLen = 0;
    int cur = 0;
    for (int i = 0; i < s.length; i++) {
      if (i == 0 || s.codeUnitAt(i) == s.codeUnitAt(i - 1) + 1) {
        cur++;
      } else {
        cur = 1;
      }
      if (cur > maxLen) {
        maxLen = cur;
      }
    }
    return maxLen;
  }
}
```

## Golang

```go
func longestContinuousSubstring(s string) int {
    if len(s) == 0 {
        return 0
    }
    maxLen, cur := 1, 1
    for i := 1; i < len(s); i++ {
        if s[i] == s[i-1]+1 {
            cur++
        } else {
            cur = 1
        }
        if cur > maxLen {
            maxLen = cur
        }
    }
    return maxLen
}
```

## Ruby

```ruby
def longest_continuous_substring(s)
  max_len = 1
  cur = 1
  (1...s.length).each do |i|
    if s[i].ord == s[i - 1].ord + 1
      cur += 1
    else
      cur = 1
    end
    max_len = cur if cur > max_len
  end
  max_len
end
```

## Scala

```scala
object Solution {
    def longestContinuousSubstring(s: String): Int = {
        var maxLen = 0
        var cur = 0
        var prevChar: Char = 0
        for (i <- s.indices) {
            val c = s.charAt(i)
            if (i == 0 || c - prevChar == 1) {
                cur += 1
            } else {
                cur = 1
            }
            if (cur > maxLen) maxLen = cur
            prevChar = c
        }
        maxLen
    }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_continuous_substring(s: String) -> i32 {
        let bytes = s.as_bytes();
        if bytes.is_empty() {
            return 0;
        }
        let mut max_len = 1usize;
        let mut cur = 1usize;
        for i in 1..bytes.len() {
            if bytes[i] == bytes[i - 1] + 1 {
                cur += 1;
            } else {
                cur = 1;
            }
            if cur > max_len {
                max_len = cur;
            }
        }
        max_len as i32
    }
}
```

## Racket

```racket
(define/contract (longest-continuous-substring s)
  (-> string? exact-integer?)
  (let* ((n (string-length s)))
    (if (= n 0)
        0
        (let loop ((i 1) (curr 1) (maxlen 1))
          (if (= i n)
              maxlen
              (let* ((c (string-ref s i))
                     (p (string-ref s (- i 1)))
                     (new-curr (if (= (char->integer c) (+ 1 (char->integer p)))
                                   (+ curr 1)
                                   1))
                     (new-max (if (> new-curr maxlen) new-curr maxlen)))
                (loop (+ i 1) new-curr new-max)))))))
```

## Erlang

```erlang
-spec longest_continuous_substring(S :: unicode:unicode_binary()) -> integer().
longest_continuous_substring(S) ->
    loop(S, -1, 0, 0).

loop(<<>>, _Prev, _Cur, Max) ->
    Max;
loop(<<C, Rest/binary>>, Prev, Cur, Max) ->
    NewCur = if
        Prev + 1 == C -> Cur + 1;
        true -> 1
    end,
    NewMax = erlang:max(NewCur, Max),
    loop(Rest, C, NewCur, NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_continuous_substring(s :: String.t()) :: integer()
  def longest_continuous_substring(s) do
    chars = String.to_charlist(s)

    {max_len, _, _} =
      Enum.reduce(chars, {0, nil, 0}, fn c, {max_len, prev, cur_len} ->
        new_cur =
          if prev != nil and c == prev + 1 do
            cur_len + 1
          else
            1
          end

        new_max = if new_cur > max_len, do: new_cur, else: max_len
        {new_max, c, new_cur}
      end)

    max_len
  end
end
```
