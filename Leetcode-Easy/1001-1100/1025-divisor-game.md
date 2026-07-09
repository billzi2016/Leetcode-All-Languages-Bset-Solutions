# 1025. Divisor Game

## Cpp

```cpp
class Solution {
public:
    bool divisorGame(int n) {
        return n % 2 == 0;
    }
};
```

## Java

```java
class Solution {
    public boolean divisorGame(int n) {
        return n % 2 == 0;
    }
}
```

## Python

```python
class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 2 == 0
```

## Python3

```python
class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0
```

## C

```c
#include <stdbool.h>

bool divisorGame(int n) {
    return n % 2 == 0;
}
```

## Csharp

```csharp
public class Solution {
    public bool DivisorGame(int n) {
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
var divisorGame = function(n) {
    return n % 2 === 0;
};
```

## Typescript

```typescript
function divisorGame(n: number): boolean {
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
    function divisorGame($n) {
        return $n % 2 == 0;
    }
}
```

## Swift

```swift
class Solution {
    func divisorGame(_ n: Int) -> Bool {
        return n % 2 == 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun divisorGame(n: Int): Boolean {
        return n % 2 == 0
    }
}
```

## Dart

```dart
class Solution {
  bool divisorGame(int n) {
    return n % 2 == 0;
  }
}
```

## Golang

```go
func divisorGame(n int) bool {
    return n%2 == 0
}
```

## Ruby

```ruby
# @param {Integer} n
# @return {Boolean}
def divisor_game(n)
  n.even?
end
```

## Scala

```scala
object Solution {
    def divisorGame(n: Int): Boolean = {
        n % 2 == 0
    }
}
```

## Rust

```rust
impl Solution {
    pub fn divisor_game(n: i32) -> bool {
        n % 2 == 0
    }
}
```

## Racket

```racket
(define/contract (divisor-game n)
  (-> exact-integer? boolean?)
  (even? n))
```

## Erlang

```erlang
-module(solution).
-export([divisor_game/1]).

-spec divisor_game(N :: integer()) -> boolean().
divisor_game(N) ->
    N rem 2 =:= 0.
```

## Elixir

```elixir
defmodule Solution do
  @spec divisor_game(n :: integer) :: boolean
  def divisor_game(n) do
    rem(n, 2) == 0
  end
end
```
