# 2914. Minimum Number of Changes to Make Binary String Beautiful

## Cpp

```cpp
class Solution {
public:
    int minChanges(string s) {
        int changes = 0;
        for (int i = 0; i < (int)s.size(); i += 2) {
            if (s[i] != s[i + 1]) ++changes;
        }
        return changes;
    }
};
```

## Java

```java
class Solution {
    public int minChanges(String s) {
        int changes = 0;
        for (int i = 0; i < s.length(); i += 2) {
            if (s.charAt(i) != s.charAt(i + 1)) {
                changes++;
            }
        }
        return changes;
    }
}
```

## Python

```python
class Solution(object):
    def minChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        changes = 0
        n = len(s)
        for i in range(0, n, 2):
            if s[i] != s[i + 1]:
                changes += 1
        return changes
```

## Python3

```python
class Solution:
    def minChanges(self, s: str) -> int:
        ans = 0
        # iterate over pairs
        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                ans += 1
        return ans
```

## C

```c
#include <stddef.h>

int minChanges(char* s) {
    int changes = 0;
    for (size_t i = 0; s[i] != '\0' && s[i + 1] != '\0'; i += 2) {
        if (s[i] != s[i + 1]) {
            ++changes;
        }
    }
    return changes;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinChanges(string s)
    {
        int changes = 0;
        for (int i = 0; i < s.Length; i += 2)
        {
            if (s[i] != s[i + 1])
                changes++;
        }
        return changes;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minChanges = function(s) {
    let changes = 0;
    for (let i = 0; i < s.length; i += 2) {
        if (s[i] !== s[i + 1]) changes++;
    }
    return changes;
};
```

## Typescript

```typescript
function minChanges(s: string): number {
    let changes = 0;
    for (let i = 0; i < s.length; i += 2) {
        if (s[i] !== s[i + 1]) {
            changes++;
        }
    }
    return changes;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minChanges($s) {
        $n = strlen($s);
        $changes = 0;
        for ($i = 0; $i < $n; $i += 2) {
            if ($s[$i] !== $s[$i + 1]) {
                $changes++;
            }
        }
        return $changes;
    }
}
```

## Swift

```swift
class Solution {
    func minChanges(_ s: String) -> Int {
        let bytes = Array(s.utf8)
        var changes = 0
        var i = 0
        while i < bytes.count {
            if bytes[i] != bytes[i + 1] {
                changes += 1
            }
            i += 2
        }
        return changes
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minChanges(s: String): Int {
        var changes = 0
        var i = 0
        val n = s.length
        while (i < n) {
            if (s[i] != s[i + 1]) changes++
            i += 2
        }
        return changes
    }
}
```

## Dart

```dart
class Solution {
  int minChanges(String s) {
    int changes = 0;
    for (int i = 0; i < s.length; i += 2) {
      if (s[i] != s[i + 1]) {
        changes++;
      }
    }
    return changes;
  }
}
```

## Golang

```go
func minChanges(s string) int {
    changes := 0
    for i := 0; i < len(s); i += 2 {
        if s[i] != s[i+1] {
            changes++
        }
    }
    return changes
}
```

## Ruby

```ruby
def min_changes(s)
  changes = 0
  i = 0
  n = s.length
  while i < n
    changes += 1 if s.getbyte(i) != s.getbyte(i + 1)
    i += 2
  end
  changes
end
```

## Scala

```scala
object Solution {
    def minChanges(s: String): Int = {
        var changes = 0
        var i = 0
        val n = s.length
        while (i < n) {
            if (s.charAt(i) != s.charAt(i + 1)) changes += 1
            i += 2
        }
        changes
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_changes(s: String) -> i32 {
        let bytes = s.as_bytes();
        let mut ans = 0;
        for i in (0..bytes.len()).step_by(2) {
            if bytes[i] != bytes[i + 1] {
                ans += 1;
            }
        }
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (min-changes s)
  (-> string? exact-integer?)
  (let* ([n (string-length s)]
         [cnt (for/sum ([i (in-range 0 n 2)])
                (if (char=? (string-ref s i) (string-ref s (+ i 1))) 0 1))])
    cnt))
```

## Erlang

```erlang
-spec min_changes(S :: unicode:unicode_binary()) -> integer().
min_changes(S) ->
    min_changes(S, 0).

min_changes(<<>>, Acc) -> 
    Acc;
min_changes(<<C1, C2, Rest/binary>>, Acc) ->
    NewAcc = case C1 =:= C2 of
                true -> Acc;
                false -> Acc + 1
            end,
    min_changes(Rest, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_changes(s :: String.t()) :: integer()
  def min_changes(s) do
    count_pairs(s, 0)
  end

  defp count_pairs(<<>>, acc), do: acc

  defp count_pairs(<<c1, c2, rest::binary>>, acc) do
    count_pairs(rest, if c1 == c2, do: acc, else: acc + 1)
  end
end
```
