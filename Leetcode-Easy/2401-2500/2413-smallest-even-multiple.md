# 2413. Smallest Even Multiple

## Cpp

```cpp
class Solution {
public:
    int smallestEvenMultiple(int n) {
        if (n % 2 == 0) return n;
        return n * 2;
    }
};
```

## Java

```java
class Solution {
    public int smallestEvenMultiple(int n) {
        if (n % 2 == 0) return n;
        return n * 2;
    }
}
```

## Python

```python
class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n if n % 2 == 0 else n * 2
```

## Python3

```python
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n % 2 == 0 else n * 2
```

## C

```c
int smallestEvenMultiple(int n) {
    return (n % 2 == 0) ? n : n * 2;
}
```

## Csharp

```csharp
public class Solution {
    public int SmallestEvenMultiple(int n) {
        return (n % 2 == 0) ? n : n * 2;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var smallestEvenMultiple = function(n) {
    return (n % 2 === 0) ? n : n * 2;
};
```

## Typescript

```typescript
function smallestEvenMultiple(n: number): number {
    return n % 2 === 0 ? n : n * 2;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function smallestEvenMultiple($n) {
        if ($n % 2 === 0) {
            return $n;
        }
        return $n * 2;
    }
}
```

## Swift

```swift
class Solution {
    func smallestEvenMultiple(_ n: Int) -> Int {
        return n % 2 == 0 ? n : n * 2
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun smallestEvenMultiple(n: Int): Int {
        return if (n % 2 == 0) n else n * 2
    }
}
```

## Dart

```dart
class Solution {
  int smallestEvenMultiple(int n) {
    return n % 2 == 0 ? n : n * 2;
  }
}
```

## Golang

```go
func smallestEvenMultiple(n int) int {
	if n%2 == 0 {
		return n
	}
	return n * 2
}
```

## Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def smallest_even_multiple(n)
  n.even? ? n : n * 2
end
```

## Scala

```scala
object Solution {
    def smallestEvenMultiple(n: Int): Int = {
        if (n % 2 == 0) n else n * 2
    }
}
```

## Rust

```rust
impl Solution {
    pub fn smallest_even_multiple(n: i32) -> i32 {
        if n % 2 == 0 { n } else { n * 2 }
    }
}
```

## Racket

```racket
(define/contract (smallest-even-multiple n)
  (-> exact-integer? exact-integer?)
  (if (even? n) n (* n 2)))
```

## Erlang

```erlang
-module(solution).
-export([smallest_even_multiple/1]).

-spec smallest_even_multiple(N :: integer()) -> integer().
smallest_even_multiple(N) when N rem 2 =:= 0 ->
    N;
smallest_even_multiple(N) ->
    N * 2.
```

## Elixir

```elixir
defmodule Solution do
  @spec smallest_even_multiple(n :: integer) :: integer
  def smallest_even_multiple(n) do
    if rem(n, 2) == 0, do: n, else: n * 2
  end
end
```
