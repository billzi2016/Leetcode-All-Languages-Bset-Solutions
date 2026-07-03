# 0231. Power of Two

## Cpp

```cpp
class Solution {
public:
    bool isPowerOfTwo(int n) {
        return n > 0 && (n & (n - 1)) == 0;
    }
};
```

## Java

```java
class Solution {
    public boolean isPowerOfTwo(int n) {
        return n > 0 && (n & (n - 1)) == 0;
    }
}
```

## Python

```python
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (n & (n - 1)) == 0
```

## Python3

```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
```

## C

```c
#include <stdbool.h>

bool isPowerOfTwo(int n) {
    return n > 0 && (n & (n - 1)) == 0;
}
```

## Csharp

```csharp
public class Solution {
    public bool IsPowerOfTwo(int n) {
        return n > 0 && (n & (n - 1)) == 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function(n) {
    return n > 0 && (n & (n - 1)) === 0;
};
```

## Typescript

```typescript
function isPowerOfTwo(n: number): boolean {
    return n > 0 && (n & (n - 1)) === 0;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Boolean
     */
    function isPowerOfTwo($n) {
        return $n > 0 && ($n & ($n - 1)) === 0;
    }
}
```

## Swift

```swift
class Solution {
    func isPowerOfTwo(_ n: Int) -> Bool {
        return n > 0 && (n & (n - 1)) == 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isPowerOfTwo(n: Int): Boolean {
        return n > 0 && (n and (n - 1)) == 0
    }
}
```

## Dart

```dart
class Solution {
  bool isPowerOfTwo(int n) {
    return n > 0 && (n & (n - 1)) == 0;
  }
}
```

## Golang

```go
func isPowerOfTwo(n int) bool {
	if n <= 0 {
		return false
	}
	return n&(n-1) == 0
}
```

## Ruby

```ruby
# @param {Integer} n
# @return {Boolean}
def is_power_of_two(n)
  n > 0 && (n & (n - 1)).zero?
end
```

## Scala

```scala
object Solution {
    def isPowerOfTwo(n: Int): Boolean = {
        n > 0 && (n & (n - 1)) == 0
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_power_of_two(n: i32) -> bool {
        if n <= 0 {
            return false;
        }
        let x = n as u32;
        (x & (x - 1)) == 0
    }
}
```

## Racket

```racket
(define/contract (is-power-of-two n)
  (-> exact-integer? boolean?)
  (and (> n 0) (= (bitwise-and n (sub1 n)) 0)))
```

## Erlang

```erlang
-spec is_power_of_two(N :: integer()) -> boolean().
is_power_of_two(N) when N > 0 ->
    (N band (N - 1)) =:= 0;
is_power_of_two(_) ->
    false.
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec is_power_of_two(n :: integer) :: boolean
  def is_power_of_two(n) when n > 0 do
    (n &&& (n - 1)) == 0
  end

  def is_power_of_two(_), do: false
end
```
