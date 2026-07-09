# 2119. A Number After a Double Reversal

## Cpp

```cpp
class Solution {
public:
    bool isSameAfterReversals(int num) {
        return num == 0 || num % 10 != 0;
    }
};
```

## Java

```java
class Solution {
    public boolean isSameAfterReversals(int num) {
        return num == 0 || num % 10 != 0;
    }
}
```

## Python

```python
class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num == 0 or num % 10 != 0
```

## Python3

```python
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num == 0 or num % 10 != 0
```

## C

```c
bool isSameAfterReversals(int num) {
    return (num == 0) || (num % 10 != 0);
}
```

## Csharp

```csharp
public class Solution
{
    public bool IsSameAfterReversals(int num)
    {
        if (num == 0) return true;
        return num % 10 != 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} num
 * @return {boolean}
 */
var isSameAfterReversals = function(num) {
    return num === 0 || num % 10 !== 0;
};
```

## Typescript

```typescript
function isSameAfterReversals(num: number): boolean {
    return num === 0 || num % 10 !== 0;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $num
     * @return Boolean
     */
    function isSameAfterReversals($num) {
        return $num == 0 || $num % 10 != 0;
    }
}
```

## Swift

```swift
class Solution {
    func isSameAfterReversals(_ num: Int) -> Bool {
        return num == 0 || num % 10 != 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isSameAfterReversals(num: Int): Boolean {
        return num == 0 || num % 10 != 0
    }
}
```

## Dart

```dart
class Solution {
  bool isSameAfterReversals(int num) {
    return num == 0 || num % 10 != 0;
  }
}
```

## Golang

```go
func isSameAfterReversals(num int) bool {
	if num == 0 {
		return true
	}
	return num%10 != 0
}
```

## Ruby

```ruby
# @param {Integer} num
# @return {Boolean}
def is_same_after_reversals(num)
  return true if num == 0
  num % 10 != 0
end
```

## Scala

```scala
object Solution {
    def isSameAfterReversals(num: Int): Boolean = {
        num == 0 || num % 10 != 0
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_same_after_reversals(num: i32) -> bool {
        num == 0 || num % 10 != 0
    }
}
```

## Racket

```racket
(define/contract (is-same-after-reversals num)
  (-> exact-integer? boolean?)
  (or (= num 0) (not (= (remainder num 10) 0))))
```

## Erlang

```erlang
-module(solution).
-export([is_same_after_reversals/1]).

-spec is_same_after_reversals(Num :: integer()) -> boolean().
is_same_after_reversals(0) ->
    true;
is_same_after_reversals(Num) when Num > 0 ->
    (Num rem 10) =/= 0.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_same_after_reversals(num :: integer) :: boolean
  def is_same_after_reversals(num) do
    num == 0 or rem(num, 10) != 0
  end
end
```
