# 0877. Stone Game

## Cpp

```cpp
class Solution {
public:
    bool stoneGame(vector<int>& piles) {
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean stoneGame(int[] piles) {
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        return True
```

## Python3

```python
from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
```

## C

```c
#include <stdbool.h>

bool stoneGame(int* piles, int pilesSize) {
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool StoneGame(int[] piles) {
        // With optimal play and an even number of piles,
        // Alice can always guarantee a win.
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} piles
 * @return {boolean}
 */
var stoneGame = function(piles) {
    // With an even number of piles and optimal play,
    // Alice can always guarantee a win.
    return true;
};
```

## Typescript

```typescript
function stoneGame(piles: number[]): boolean {
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $piles
     * @return Boolean
     */
    function stoneGame($piles) {
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func stoneGame(_ piles: [Int]) -> Bool {
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun stoneGame(piles: IntArray): Boolean {
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool stoneGame(List<int> piles) {
    return true;
  }
}
```

## Golang

```go
func stoneGame(piles []int) bool {
    return true
}
```

## Ruby

```ruby
def stone_game(piles)
  true
end
```

## Scala

```scala
object Solution {
    def stoneGame(piles: Array[Int]): Boolean = true
}
```

## Rust

```rust
impl Solution {
    pub fn stone_game(_piles: Vec<i32>) -> bool {
        true
    }
}
```

## Racket

```racket
(define/contract (stone-game piles)
  (-> (listof exact-integer?) boolean?)
  #t)
```

## Erlang

```erlang
-module(solution).
-export([stone_game/1]).

-spec stone_game(Piles :: [integer()]) -> boolean().
stone_game(_Piles) ->
    true.
```

## Elixir

```elixir
defmodule Solution do
  @spec stone_game(piles :: [integer]) :: boolean
  def stone_game(_piles), do: true
end
```
