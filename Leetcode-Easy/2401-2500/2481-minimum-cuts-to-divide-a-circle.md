# 2481. Minimum Cuts to Divide a Circle

## Cpp

```cpp
class Solution {
public:
    int numberOfCuts(int n) {
        if (n == 1) return 0;
        if (n % 2 == 0) return n / 2;
        return n;
    }
};
```

## Java

```java
class Solution {
    public int numberOfCuts(int n) {
        if (n == 1) return 0;
        return (n % 2 == 0) ? n / 2 : n;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfCuts(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        return n // 2 if n % 2 == 0 else n
```

## Python3

```python
class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1:
            return 0
        if n % 2 == 0:
            return n // 2
        return n
```

## C

```c
int numberOfCuts(int n) {
    if (n == 1) return 0;
    return (n % 2 == 0) ? n / 2 : n;
}
```

## Csharp

```csharp
public class Solution {
    public int NumberOfCuts(int n) {
        if (n == 1) return 0;
        return (n % 2 == 0) ? n / 2 : n;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var numberOfCuts = function(n) {
    if (n === 1) return 0;
    return n % 2 === 0 ? n / 2 : n;
};
```

## Typescript

```typescript
function numberOfCuts(n: number): number {
    if (n === 1) return 0;
    return n % 2 === 0 ? n / 2 : n;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function numberOfCuts($n) {
        if ($n == 1) {
            return 0;
        }
        if ($n % 2 == 0) {
            return intdiv($n, 2);
        }
        return $n;
    }
}
```

## Swift

```swift
class Solution {
    func numberOfCuts(_ n: Int) -> Int {
        if n == 1 { return 0 }
        return n % 2 == 0 ? n / 2 : n
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfCuts(n: Int): Int {
        return if (n == 1) 0 else if (n % 2 == 0) n / 2 else n
    }
}
```

## Dart

```dart
class Solution {
  int numberOfCuts(int n) {
    if (n == 1) return 0;
    return n % 2 == 0 ? n ~/ 2 : n;
  }
}
```

## Golang

```go
func numberOfCuts(n int) int {
	if n == 1 {
		return 0
	}
	if n%2 == 0 {
		return n / 2
	}
	return n
}
```

## Ruby

```ruby
def number_of_cuts(n)
  return 0 if n == 1
  n.even? ? n / 2 : n
end
```

## Scala

```scala
object Solution {
    def numberOfCuts(n: Int): Int = {
        if (n == 1) 0
        else if (n % 2 == 0) n / 2
        else n
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_cuts(n: i32) -> i32 {
        if n == 1 {
            0
        } else if n % 2 == 0 {
            n / 2
        } else {
            n
        }
    }
}
```

## Racket

```racket
(define/contract (number-of-cuts n)
  (-> exact-integer? exact-integer?)
  (cond [(= n 1) 0]
        [(even? n) (/ n 2)]
        [else n]))
```

## Erlang

```erlang
-spec number_of_cuts(N :: integer()) -> integer().
number_of_cuts(1) ->
    0;
number_of_cuts(N) when N rem 2 =:= 0 ->
    N div 2;
number_of_cuts(N) ->
    N.
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_cuts(n :: integer) :: integer
  def number_of_cuts(1), do: 0
  def number_of_cuts(n) when rem(n, 2) == 0, do: div(n, 2)
  def number_of_cuts(n), do: n
end
```
