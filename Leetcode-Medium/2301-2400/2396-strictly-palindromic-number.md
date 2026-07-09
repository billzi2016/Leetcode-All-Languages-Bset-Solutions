# 2396. Strictly Palindromic Number

## Cpp

```cpp
class Solution {
public:
    bool isStrictlyPalindromic(int n) {
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean isStrictlyPalindromic(int n) {
        // For any n >= 4, the representation in base (n-2) is always "12", which is not a palindrome.
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def isStrictlyPalindromic(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return False
```

## Python3

```python
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        return False
```

## C

```c
bool isStrictlyPalindromic(int n) {
    return false;
}
```

## Csharp

```csharp
public class Solution {
    public bool IsStrictlyPalindromic(int n) {
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {boolean}
 */
var isStrictlyPalindromic = function(n) {
    return false;
};
```

## Typescript

```typescript
function isStrictlyPalindromic(n: number): boolean {
    // For any integer n >= 4, its representation in base (n-2) is always "12",
    // which is not a palindrome. Hence no strictly palindromic numbers exist.
    return false;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @return Boolean
     */
    function isStrictlyPalindromic($n) {
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func isStrictlyPalindromic(_ n: Int) -> Bool {
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isStrictlyPalindromic(n: Int): Boolean {
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool isStrictlyPalindromic(int n) {
    return false;
  }
}
```

## Golang

```go
func isStrictlyPalindromic(n int) bool {
    return false
}
```

## Ruby

```ruby
def is_strictly_palindromic(n)
  false
end
```

## Scala

```scala
object Solution {
    def isStrictlyPalindromic(n: Int): Boolean = {
        false
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_strictly_palindromic(_n: i32) -> bool {
        false
    }
}
```

## Racket

```racket
(define/contract (is-strictly-palindromic n)
  (-> exact-integer? boolean?)
  #f)
```

## Erlang

```erlang
-module(solution).
-export([is_strictly_palindromic/1]).

-spec is_strictly_palindromic(N :: integer()) -> boolean().
is_strictly_palindromic(_N) ->
    false.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_strictly_palindromic(n :: integer) :: boolean
  def is_strictly_palindromic(_n), do: false
end
```
