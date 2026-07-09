# 2549. Count Distinct Numbers on Board

## Cpp

```cpp
class Solution {
public:
    int distinctIntegers(int n) {
        if (n == 1) return 1;
        return n - 1;
    }
};
```

## Java

```java
class Solution {
    public int distinctIntegers(int n) {
        if (n == 1) return 1;
        return n - 1;
    }
}
```

## Python

```python
class Solution(object):
    def distinctIntegers(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n - 1 if n > 1 else 1
```

## Python3

```python
class Solution:
    def distinctIntegers(self, n: int) -> int:
        return 1 if n == 1 else n - 1
```

## C

```c
int distinctIntegers(int n) {
    if (n == 1) return 1;
    return n - 1;
}
```

## Csharp

```csharp
public class Solution
{
    public int DistinctIntegers(int n)
    {
        return n == 1 ? 0 : n - 1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var distinctIntegers = function(n) {
    return n === 1 ? 1 : n - 1;
};
```

## Typescript

```typescript
function distinctIntegers(n: number): number {
    return n === 1 ? 0 : n - 1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function distinctIntegers($n) {
        if ($n == 1) {
            return 1;
        }
        return $n - 1;
    }
}
```

## Swift

```swift
class Solution {
    func distinctIntegers(_ n: Int) -> Int {
        return n == 1 ? 1 : n - 1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun distinctIntegers(n: Int): Int {
        return if (n == 1) 1 else n - 1
    }
}
```

## Dart

```dart
class Solution {
  int distinctIntegers(int n) {
    return n <= 1 ? 0 : n - 1;
  }
}
```

## Golang

```go
func distinctIntegers(n int) int {
	if n == 1 {
		return 0
	}
	return n - 1
}
```

## Ruby

```ruby
def distinct_integers(n)
  n == 1 ? 1 : n - 1
end
```

## Scala

```scala
object Solution {
    def distinctIntegers(n: Int): Int = {
        if (n == 1) 1 else n - 1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn distinct_integers(n: i32) -> i32 {
        if n == 1 { 1 } else { n - 1 }
    }
}
```

## Racket

```racket
(define/contract (distinct-integers n)
  (-> exact-integer? exact-integer?)
  (if (= n 1) 
      1
      (- n 1)))
```

## Erlang

```erlang
-spec distinct_integers(N :: integer()) -> integer().
distinct_integers(1) ->
    1;
distinct_integers(N) when N > 1 ->
    N - 1.
```

## Elixir

```elixir
defmodule Solution do
  @spec distinct_integers(n :: integer) :: integer
  def distinct_integers(1), do: 0
  def distinct_integers(n), do: n - 1
end
```
