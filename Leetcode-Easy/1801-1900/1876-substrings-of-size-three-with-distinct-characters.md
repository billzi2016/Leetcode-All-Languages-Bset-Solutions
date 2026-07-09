# 1876. Substrings of Size Three with Distinct Characters

## Cpp

```cpp
class Solution {
public:
    int countGoodSubstrings(string s) {
        int n = s.size();
        if (n < 3) return 0;
        int cnt = 0;
        for (int i = 0; i + 2 < n; ++i) {
            char a = s[i], b = s[i+1], c = s[i+2];
            if (a != b && a != c && b != c) ++cnt;
        }
        return cnt;
    }
};
```

## Java

```java
class Solution {
    public int countGoodSubstrings(String s) {
        int n = s.length();
        if (n < 3) return 0;
        int count = 0;
        for (int i = 0; i <= n - 3; i++) {
            char a = s.charAt(i);
            char b = s.charAt(i + 1);
            char c = s.charAt(i + 2);
            if (a != b && a != c && b != c) {
                count++;
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n < 3:
            return 0
        cnt = 0
        for i in range(n - 2):
            a, b, c = s[i], s[i + 1], s[i + 2]
            if a != b and a != c and b != c:
                cnt += 1
        return cnt
```

## Python3

```python
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        if n < 3:
            return 0
        cnt = 0
        for i in range(n - 2):
            a, b, c = s[i], s[i+1], s[i+2]
            if a != b and a != c and b != c:
                cnt += 1
        return cnt
```

## C

```c
#include <string.h>

int countGoodSubstrings(char* s) {
    int n = strlen(s);
    int cnt = 0;
    for (int i = 0; i + 2 < n; ++i) {
        char a = s[i], b = s[i+1], c = s[i+2];
        if (a != b && a != c && b != c)
            ++cnt;
    }
    return cnt;
}
```

## Csharp

```csharp
public class Solution {
    public int CountGoodSubstrings(string s) {
        int n = s.Length;
        if (n < 3) return 0;
        int count = 0;
        for (int i = 0; i <= n - 3; i++) {
            char a = s[i];
            char b = s[i + 1];
            char c = s[i + 2];
            if (a != b && a != c && b != c) count++;
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var countGoodSubstrings = function(s) {
    const n = s.length;
    let count = 0;
    for (let i = 0; i + 2 < n; i++) {
        if (s[i] !== s[i + 1] && s[i] !== s[i + 2] && s[i + 1] !== s[i + 2]) {
            count++;
        }
    }
    return count;
};
```

## Typescript

```typescript
function countGoodSubstrings(s: string): number {
    let count = 0;
    for (let i = 0; i + 2 < s.length; i++) {
        const a = s[i];
        const b = s[i + 1];
        const c = s[i + 2];
        if (a !== b && a !== c && b !== c) {
            count++;
        }
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function countGoodSubstrings($s) {
        $n = strlen($s);
        $count = 0;
        for ($i = 0; $i <= $n - 3; $i++) {
            $a = $s[$i];
            $b = $s[$i + 1];
            $c = $s[$i + 2];
            if ($a !== $b && $a !== $c && $b !== $c) {
                $count++;
            }
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func countGoodSubstrings(_ s: String) -> Int {
        let chars = Array(s)
        guard chars.count >= 3 else { return 0 }
        var result = 0
        for i in 0..<(chars.count - 2) {
            if chars[i] != chars[i + 1] &&
               chars[i] != chars[i + 2] &&
               chars[i + 1] != chars[i + 2] {
                result += 1
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countGoodSubstrings(s: String): Int {
        var count = 0
        for (i in 0 until s.length - 2) {
            val a = s[i]
            val b = s[i + 1]
            val c = s[i + 2]
            if (a != b && a != c && b != c) {
                count++
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int countGoodSubstrings(String s) {
    int n = s.length;
    int cnt = 0;
    for (int i = 0; i + 2 < n; i++) {
      if (s[i] != s[i + 1] && s[i] != s[i + 2] && s[i + 1] != s[i + 2]) {
        cnt++;
      }
    }
    return cnt;
  }
}
```

## Golang

```go
func countGoodSubstrings(s string) int {
    n := len(s)
    if n < 3 {
        return 0
    }
    cnt := 0
    for i := 0; i+2 < n; i++ {
        a, b, c := s[i], s[i+1], s[i+2]
        if a != b && b != c && a != c {
            cnt++
        }
    }
    return cnt
}
```

## Ruby

```ruby
def count_good_substrings(s)
  n = s.length
  return 0 if n < 3
  cnt = 0
  (0..n - 3).each do |i|
    a = s[i]
    b = s[i + 1]
    c = s[i + 2]
    cnt += 1 if a != b && a != c && b != c
  end
  cnt
end
```

## Scala

```scala
object Solution {
    def countGoodSubstrings(s: String): Int = {
        var cnt = 0
        for (i <- 0 until s.length - 2) {
            val a = s.charAt(i)
            val b = s.charAt(i + 1)
            val c = s.charAt(i + 2)
            if (a != b && a != c && b != c) cnt += 1
        }
        cnt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_good_substrings(s: String) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        if n < 3 {
            return 0;
        }
        let mut cnt = 0;
        for i in 0..n - 2 {
            let a = bytes[i];
            let b = bytes[i + 1];
            let c = bytes[i + 2];
            if a != b && a != c && b != c {
                cnt += 1;
            }
        }
        cnt as i32
    }
}
```

## Racket

```racket
(define/contract (count-good-substrings s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (limit (- n 2))) ; last starting index for a length‑3 substring
    (if (< n 3)
        0
        (for/sum ([i (in-range limit)])
          (let ((c1 (string-ref s i))
                (c2 (string-ref s (+ i 1)))
                (c3 (string-ref s (+ i 2))))
            (if (and (not (char=? c1 c2))
                     (not (char=? c1 c3))
                     (not (char=? c2 c3)))
                1
                0))))))
```

## Erlang

```erlang
-spec count_good_substrings(S :: unicode:unicode_binary()) -> integer().
count_good_substrings(S) ->
    L = unicode:characters_to_list(S),
    count(L, 0).

count([A,B,C|Rest], Acc) ->
    NewAcc = if A =/= B andalso A =/= C andalso B =/= C -> Acc + 1; true -> Acc end,
    count([B,C|Rest], NewAcc);
count(_, Acc) -> 
    Acc.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_good_substrings(s :: String.t) :: integer
  def count_good_substrings(s) do
    chars = String.graphemes(s)
    len = length(chars)

    if len < 3 do
      0
    else
      0..(len - 3)
      |> Enum.count(fn i ->
        a = Enum.at(chars, i)
        b = Enum.at(chars, i + 1)
        c = Enum.at(chars, i + 2)

        a != b and b != c and a != c
      end)
    end
  end
end
```
