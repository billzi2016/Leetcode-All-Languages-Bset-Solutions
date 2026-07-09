# 1653. Minimum Deletions to Make String Balanced

## Cpp

```cpp
class Solution {
public:
    int minimumDeletions(string s) {
        int bCount = 0;
        int deletions = 0;
        for (char c : s) {
            if (c == 'b') {
                ++bCount;
            } else { // c == 'a'
                deletions = min(deletions + 1, bCount);
            }
        }
        return deletions;
    }
};
```

## Java

```java
class Solution {
    public int minimumDeletions(String s) {
        int bCount = 0;
        int deletions = 0;
        for (char c : s.toCharArray()) {
            if (c == 'b') {
                bCount++;
            } else { // c == 'a'
                deletions = Math.min(deletions + 1, bCount);
            }
        }
        return deletions;
    }
}
```

## Python

```python
class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        deletions = 0
        b_count = 0
        for ch in s:
            if ch == 'b':
                b_count += 1
            else:  # ch == 'a'
                deletions = min(deletions + 1, b_count)
        return deletions
```

## Python3

```python
class Solution:
    def minimumDeletions(self, s: str) -> int:
        deletions = 0
        b_count = 0
        for ch in s:
            if ch == 'b':
                b_count += 1
            else:  # ch == 'a'
                deletions = min(deletions + 1, b_count)
        return deletions
```

## C

```c
int minimumDeletions(char* s) {
    int bCount = 0;
    int deletions = 0;
    for (char *p = s; *p; ++p) {
        if (*p == 'b') {
            bCount++;
        } else { // character is 'a'
            if (deletions + 1 < bCount)
                deletions = deletions + 1;
            else
                deletions = bCount;
        }
    }
    return deletions;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinimumDeletions(string s)
    {
        int bCount = 0;
        int deletions = 0;

        foreach (char c in s)
        {
            if (c == 'b')
            {
                bCount++;
            }
            else // c == 'a'
            {
                deletions = Math.Min(deletions + 1, bCount);
            }
        }

        return deletions;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minimumDeletions = function(s) {
    let bCount = 0;
    let deletions = 0;
    for (const ch of s) {
        if (ch === 'b') {
            bCount++;
        } else { // ch === 'a'
            deletions = Math.min(deletions + 1, bCount);
        }
    }
    return deletions;
};
```

## Typescript

```typescript
function minimumDeletions(s: string): number {
    let deletions = 0;
    let bCount = 0;
    for (const ch of s) {
        if (ch === 'b') {
            bCount++;
        } else { // ch === 'a'
            deletions = Math.min(deletions + 1, bCount);
        }
    }
    return deletions;
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function minimumDeletions($s) {
        $bCount = 0;
        $minDel = 0;
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            if ($s[$i] === 'b') {
                $bCount++;
            } else { // 'a'
                $minDel = min($minDel + 1, $bCount);
            }
        }
        return $minDel;
    }
}
```

## Swift

```swift
class Solution {
    func minimumDeletions(_ s: String) -> Int {
        var bCount = 0
        var deletions = 0
        for ch in s {
            if ch == "b" {
                bCount += 1
            } else { // 'a'
                deletions = min(deletions + 1, bCount)
            }
        }
        return deletions
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumDeletions(s: String): Int {
        var bCount = 0
        var deletions = 0
        for (c in s) {
            if (c == 'b') {
                bCount++
            } else { // c == 'a'
                deletions = kotlin.math.min(deletions + 1, bCount)
            }
        }
        return deletions
    }
}
```

## Dart

```dart
class Solution {
  int minimumDeletions(String s) {
    int minDel = 0;
    int bCount = 0;
    for (int i = 0; i < s.length; i++) {
      if (s[i] == 'b') {
        bCount++;
      } else { // s[i] == 'a'
        minDel = (minDel + 1) < bCount ? (minDel + 1) : bCount;
      }
    }
    return minDel;
  }
}
```

## Golang

```go
func minimumDeletions(s string) int {
    deletions, bCount := 0, 0
    for i := 0; i < len(s); i++ {
        if s[i] == 'b' {
            bCount++
        } else { // s[i] == 'a'
            if deletions+1 < bCount {
                deletions = deletions + 1
            } else {
                deletions = bCount
            }
        }
    }
    return deletions
}
```

## Ruby

```ruby
def minimum_deletions(s)
  min_del = 0
  b_count = 0
  s.each_char do |ch|
    if ch == 'b'
      b_count += 1
    else # ch == 'a'
      min_del = [min_del + 1, b_count].min
    end
  end
  min_del
end
```

## Scala

```scala
object Solution {
    def minimumDeletions(s: String): Int = {
        var bCount = 0
        var deletions = 0
        for (c <- s) {
            if (c == 'b') {
                bCount += 1
            } else { // c == 'a'
                deletions = math.min(deletions + 1, bCount)
            }
        }
        deletions
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_deletions(s: String) -> i32 {
        let mut b_count = 0usize;
        let mut min_del = 0usize;
        for &c in s.as_bytes() {
            if c == b'b' {
                b_count += 1;
            } else { // c == b'a'
                let opt1 = min_del + 1;
                let opt2 = b_count;
                min_del = if opt2 < opt1 { opt2 } else { opt1 };
            }
        }
        min_del as i32
    }
}
```

## Racket

```racket
#lang racket

(define/contract (minimum-deletions s)
  (-> string? exact-integer?)
  (let ((b-count 0)
        (min-del 0))
    (for ([i (in-range (string-length s))])
      (let ((ch (string-ref s i)))
        (cond [(char=? ch #\b) (set! b-count (+ b-count 1))]
              [(char=? ch #\a) (set! min-del (min (+ min-del 1) b-count))])))
    min-del))
```

## Erlang

```erlang
-module(solution).
-export([minimum_deletions/1]).

-spec minimum_deletions(S :: unicode:unicode_binary()) -> integer().
minimum_deletions(S) ->
    go(S, 0, 0).

go(<<>>, MinDel, _BCount) ->
    MinDel;
go(<<Char, Rest/binary>>, MinDel, BCount) ->
    case Char of
        $a ->
            NewMin = erlang:min(MinDel + 1, BCount),
            go(Rest, NewMin, BCount);
        $b ->
            go(Rest, MinDel, BCount + 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_deletions(s :: String.t()) :: integer()
  def minimum_deletions(s) do
    {min_del, _b_count} =
      :binary.bin_to_list(s)
      |> Enum.reduce({0, 0}, fn
        ?b, {md, bc} -> {md, bc + 1}
        ?a, {md, bc} -> {Enum.min(md + 1, bc), bc}
      end)

    min_del
  end
end
```
