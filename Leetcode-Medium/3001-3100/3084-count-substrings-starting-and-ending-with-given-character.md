# 3084. Count Substrings Starting and Ending with Given Character

## Cpp

```cpp
class Solution {
public:
    long long countSubstrings(string s, char c) {
        long long cnt = 0;
        for (char ch : s) if (ch == c) ++cnt;
        return cnt * (cnt + 1) / 2;
    }
};
```

## Java

```java
class Solution {
    public long countSubstrings(String s, char c) {
        long count = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == c) {
                count++;
            }
        }
        return count * (count + 1) / 2;
    }
}
```

## Python

```python
class Solution(object):
    def countSubstrings(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: int
        """
        m = s.count(c)
        return m * (m + 1) // 2
```

## Python3

```python
class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        m = s.count(c)
        return m * (m + 1) // 2
```

## C

```c
long long countSubstrings(char* s, char c) {
    long long m = 0;
    for (; *s; ++s) {
        if (*s == c) ++m;
    }
    return m * (m + 1) / 2;
}
```

## Csharp

```csharp
public class Solution {
    public long CountSubstrings(string s, char c) {
        long count = 0;
        foreach (char ch in s) {
            if (ch == c) count++;
        }
        return count * (count + 1) / 2;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {character} c
 * @return {number}
 */
var countSubstrings = function(s, c) {
    let m = 0;
    for (let i = 0; i < s.length; ++i) {
        if (s[i] === c) m++;
    }
    return m * (m + 1) / 2;
};
```

## Typescript

```typescript
function countSubstrings(s: string, c: string): number {
    let m = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === c) m++;
    }
    return m * (m + 1) / 2;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String $c
     * @return Integer
     */
    function countSubstrings($s, $c) {
        $m = substr_count($s, $c);
        return intdiv($m * ($m + 1), 2);
    }
}
```

## Swift

```swift
class Solution {
    func countSubstrings(_ s: String, _ c: Character) -> Int {
        var count = 0
        for ch in s {
            if ch == c { count += 1 }
        }
        return count * (count + 1) / 2
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countSubstrings(s: String, c: Char): Long {
        var m = 0L
        for (ch in s) {
            if (ch == c) m++
        }
        return m * (m + 1) / 2
    }
}
```

## Dart

```dart
class Solution {
  int countSubstrings(String s, String c) {
    int m = 0;
    for (int i = 0; i < s.length; i++) {
      if (s[i] == c) m++;
    }
    return m * (m + 1) ~/ 2;
  }
}
```

## Golang

```go
func countSubstrings(s string, c byte) int64 {
	var cnt int64
	for i := 0; i < len(s); i++ {
		if s[i] == c {
			cnt++
		}
	}
	return cnt * (cnt + 1) / 2
}
```

## Ruby

```ruby
def count_substrings(s, c)
  m = s.count(c)
  m * (m + 1) / 2
end
```

## Scala

```scala
object Solution {
    def countSubstrings(s: String, c: Char): Long = {
        var m: Long = 0L
        for (ch <- s) {
            if (ch == c) m += 1
        }
        m * (m + 1) / 2
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_substrings(s: String, c: char) -> i64 {
        let m = s.chars().filter(|&ch| ch == c).count() as i64;
        m * (m + 1) / 2
    }
}
```

## Racket

```racket
(define/contract (count-substrings s c)
  (-> string? char? exact-integer?)
  (let* ((len (string-length s))
         (cnt (for/sum ([i (in-range len)])
                (if (char=? (string-ref s i) c) 1 0))))
    (quotient (* cnt (+ cnt 1)) 2)))
```

## Erlang

```erlang
-module(solution).
-export([count_substrings/2]).

-spec count_substrings(S :: unicode:unicode_binary(), C :: char()) -> integer().
count_substrings(S, C) ->
    Count = count_occurrences(S, C, 0),
    (Count * (Count + 1)) div 2.

count_occurrences(<<>>, _Char, Acc) -> Acc;
count_occurrences(Bin, Char, Acc) ->
    case Bin of
        <<Char, Rest/binary>> ->
            count_occurrences(Rest, Char, Acc + 1);
        <<_, Rest/binary>> ->
            count_occurrences(Rest, Char, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_substrings(s :: String.t(), c :: char()) :: integer()
  def count_substrings(s, c) do
    c_code = hd(String.to_charlist(c))

    m =
      s
      |> String.to_charlist()
      |> Enum.count(fn ch -> ch == c_code end)

    div(m * (m + 1), 2)
  end
end
```
