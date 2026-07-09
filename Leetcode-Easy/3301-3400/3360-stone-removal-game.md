# 3360. Stone Removal Game

## Cpp

```cpp
class Solution {
public:
    bool canAliceWin(int n) {
        return n % 2 == 0;
    }
};
```

## Java

```java
class Solution {
    public boolean canAliceWin(int n) {
        return n % 2 == 0;
    }
}
```

## Python

```python
class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 2 == 0
```

## Python3

```python
class Solution:
    def canAliceWin(self, n: int) -> bool:
        return n % 2 == 0
```

## C

```c
#include <stdbool.h>

bool canAliceWin(int n) {
    return (n % 2 == 0);
}
```

## Csharp

```csharp
public class Solution {
    public bool CanAliceWin(int n) {
        return n % 2 == 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {boolean}
 */
var canAliceWin = function(n) {
    const dp = new Array(n + 1).fill(false); // dp[i] = true if current player wins with i stones
    
    for (let i = 2; i <= n; i++) {
        let win = false;
        for (let d = 1; d * d <= i; d++) {
            if (i % d === 0) {
                const div1 = d;
                const div2 = i / d;
                
                if (div1 < i && !dp[i - div1]) { win = true; break; }
                if (div2 !== div1 && div2 < i && !dp[i - div2]) { win = true; break; }
            }
        }
        dp[i] = win;
    }
    
    return dp[n];
};
```

## Typescript

```typescript
function canAliceWin(n: number): boolean {
    return n % 2 === 0;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Boolean
     */
    function canAliceWin($n) {
        return $n % 2 === 0;
    }
}
```

## Swift

```swift
class Solution {
    func canAliceWin(_ n: Int) -> Bool {
        return n % 2 == 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canAliceWin(n: Int): Boolean {
        val win = BooleanArray(n + 1)
        // win[0] is irrelevant; win[1] stays false (no moves)
        for (i in 2..n) {
            var canWin = false
            var d = 1
            while (d * d <= i) {
                if (i % d == 0) {
                    val div1 = d
                    val div2 = i / d
                    // check proper divisor div1
                    if (div1 < i && !win[i - div1]) {
                        canWin = true
                        break
                    }
                    // check proper divisor div2 (different from div1)
                    if (div2 != div1 && div2 < i && !win[i - div2]) {
                        canWin = true
                        break
                    }
                }
                d++
            }
            win[i] = canWin
        }
        return win[n]
    }
}
```

## Dart

```dart
class Solution {
  bool canAliceWin(int n) {
    return n % 2 == 0;
  }
}
```

## Golang

```go
func canAliceWin(n int) bool {
    return n%2 == 0
}
```

## Ruby

```ruby
def can_alice_win(n)
  dp = Array.new(n + 1, false)
  (1..n).each do |i|
    win = false
    (1...i).each do |d|
      next unless i % d == 0
      if !dp[i - d]
        win = true
        break
      end
    end
    dp[i] = win
  end
  dp[n]
end
```

## Scala

```scala
object Solution {
    def canAliceWin(n: Int): Boolean = {
        n % 2 == 0
    }
}
```

## Rust

```rust
impl Solution {
    pub fn can_alice_win(n: i32) -> bool {
        n % 2 == 0
    }
}
```

## Racket

```racket
(define/contract (can-alice-win n)
  (-> exact-integer? boolean?)
  (even? n))
```

## Erlang

```erlang
-spec can_alice_win(N :: integer()) -> boolean().
can_alice_win(N) ->
    N rem 2 =:= 0.
```

## Elixir

```elixir
defmodule Solution do
  @spec can_alice_win(n :: integer) :: boolean
  def can_alice_win(n) when is_integer(n) and n > 0 do
    rem(n, 2) == 0
  end
end
```
