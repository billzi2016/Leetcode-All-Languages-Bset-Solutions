# 3014. Minimum Number of Pushes to Type Word I

## Cpp

```cpp
class Solution {
public:
    int minimumPushes(string word) {
        int n = word.size();
        int pushes = 0;
        for (int i = 0; i < n; ++i) {
            pushes += i / 8 + 1;
        }
        return pushes;
    }
};
```

## Java

```java
class Solution {
    public int minimumPushes(String word) {
        int n = word.length();
        int pushes = 0;
        for (int i = 0; i < n; i++) {
            pushes += (i / 8) + 1;
        }
        return pushes;
    }
}
```

## Python

```python
class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        pushes = 0
        for i in range(len(word)):
            pushes += (i // 8) + 1
        return pushes
```

## Python3

```python
class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        base = n // 8
        extra = n % 8
        small = base * (base + 1) // 2
        big = (base + 1) * (base + 2) // 2
        return extra * big + (8 - extra) * small
```

## C

```c
#include <string.h>

int minimumPushes(char* word) {
    int n = strlen(word);
    int pushes = 0;
    for (int i = 0; i < n; ++i) {
        pushes += (i / 8) + 1;
    }
    return pushes;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumPushes(string word) {
        int pushes = 0;
        for (int i = 0; i < word.Length; i++) {
            pushes += (i / 8) + 1;
        }
        return pushes;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word
 * @return {number}
 */
var minimumPushes = function(word) {
    const n = word.length;
    let pushes = 0;
    for (let i = 0; i < n; ++i) {
        pushes += Math.floor(i / 8) + 1;
    }
    return pushes;
};
```

## Typescript

```typescript
function minimumPushes(word: string): number {
    const n = word.length;
    let total = 0;
    for (let i = 0; i < n; ++i) {
        total += Math.floor(i / 8) + 1;
    }
    return total;
}
```

## Php

```php
class Solution {
    /**
     * @param String $word
     * @return Integer
     */
    function minimumPushes($word) {
        $n = strlen($word);
        $pushes = 0;
        for ($i = 0; $i < $n; ++$i) {
            $pushes += intdiv($i, 8) + 1;
        }
        return $pushes;
    }
}
```

## Swift

```swift
class Solution {
    func minimumPushes(_ word: String) -> Int {
        let n = word.count
        var total = 0
        for i in 0..<n {
            total += i / 8 + 1
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumPushes(word: String): Int {
        var total = 0
        for ((i, _) in word.withIndex()) {
            total += i / 8 + 1
        }
        return total
    }
}
```

## Dart

```dart
class Solution {
  int minimumPushes(String word) {
    int pushes = 0;
    for (int i = 0; i < word.length; ++i) {
      pushes += (i ~/ 8) + 1;
    }
    return pushes;
  }
}
```

## Golang

```go
func minimumPushes(word string) int {
    n := len(word)
    total := 0
    for i := 0; i < n; i++ {
        total += i/8 + 1
    }
    return total
}
```

## Ruby

```ruby
def minimum_pushes(word)
  n = word.length
  groups = n / 8
  rem = n % 8
  4 * groups * (groups + 1) + rem * (groups + 1)
end
```

## Scala

```scala
object Solution {
    def minimumPushes(word: String): Int = {
        var total = 0
        for (i <- 0 until word.length) {
            total += i / 8 + 1
        }
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_pushes(word: String) -> i32 {
        let mut pushes = 0i32;
        for (i, _) in word.chars().enumerate() {
            pushes += ((i / 8) + 1) as i32;
        }
        pushes
    }
}
```

## Racket

```racket
(define/contract (minimum-pushes word)
  (-> string? exact-integer?)
  (let* ((n (string-length word))
         (q (quotient n 8))
         (r (remainder n 8))
         (sum-full (* 4 q (+ q 1))) ; 8 * (q*(q+1)/2) = 4*q*(q+1)
         (total (+ sum-full (* r (+ q 1)))))
    total))
```

## Erlang

```erlang
-module(solution).
-export([minimum_pushes/1]).

-spec minimum_pushes(Word :: unicode:unicode_binary()) -> integer().
minimum_pushes(Word) ->
    N = byte_size(Word),
    Q = N div 8,
    R = N rem 8,
    4 * Q * (Q + 1) + R * (Q + 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_pushes(word :: String.t()) :: integer()
  def minimum_pushes(word) do
    n = String.length(word)
    q = div(n, 8)
    r = rem(n, 8)

    cost_q = div(q * (q + 1), 2)
    cost_qp1 = div((q + 1) * (q + 2), 2)

    r * cost_qp1 + (8 - r) * cost_q
  end
end
```
