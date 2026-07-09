# 2652. Sum Multiples

## Cpp

```cpp
class Solution {
public:
    int sumOfMultiples(int n) {
        int total = 0;
        for (int i = 1; i <= n; ++i) {
            if (i % 3 == 0 || i % 5 == 0 || i % 7 == 0) {
                total += i;
            }
        }
        return total;
    }
};
```

## Java

```java
class Solution {
    public int sumOfMultiples(int n) {
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            if (i % 3 == 0 || i % 5 == 0 || i % 7 == 0) {
                sum += i;
            }
        }
        return sum;
    }
}
```

## Python

```python
class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        for i in range(1, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                total += i
        return total
```

## Python3

```python
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        total = 0
        for i in range(1, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                total += i
        return total
```

## C

```c
int sumOfMultiples(int n) {
    int sum = 0;
    for (int i = 1; i <= n; ++i) {
        if (i % 3 == 0 || i % 5 == 0 || i % 7 == 0)
            sum += i;
    }
    return sum;
}
```

## Csharp

```csharp
public class Solution {
    public int SumOfMultiples(int n) {
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            if (i % 3 == 0 || i % 5 == 0 || i % 7 == 0) {
                sum += i;
            }
        }
        return sum;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var sumOfMultiples = function(n) {
    let sum = 0;
    for (let i = 1; i <= n; i++) {
        if (i % 3 === 0 || i % 5 === 0 || i % 7 === 0) {
            sum += i;
        }
    }
    return sum;
};
```

## Typescript

```typescript
function sumOfMultiples(n: number): number {
    let sum = 0;
    for (let i = 1; i <= n; i++) {
        if (i % 3 === 0 || i % 5 === 0 || i % 7 === 0) {
            sum += i;
        }
    }
    return sum;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function sumOfMultiples($n) {
        $sum = 0;
        for ($i = 1; $i <= $n; $i++) {
            if ($i % 3 == 0 || $i % 5 == 0 || $i % 7 == 0) {
                $sum += $i;
            }
        }
        return $sum;
    }
}
```

## Swift

```swift
class Solution {
    func sumOfMultiples(_ n: Int) -> Int {
        var total = 0
        for i in 1...n {
            if i % 3 == 0 || i % 5 == 0 || i % 7 == 0 {
                total += i
            }
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sumOfMultiples(n: Int): Int {
        var sum = 0
        for (i in 1..n) {
            if (i % 3 == 0 || i % 5 == 0 || i % 7 == 0) {
                sum += i
            }
        }
        return sum
    }
}
```

## Dart

```dart
class Solution {
  int sumOfMultiples(int n) {
    int total = 0;
    for (int i = 1; i <= n; i++) {
      if (i % 3 == 0 || i % 5 == 0 || i % 7 == 0) {
        total += i;
      }
    }
    return total;
  }
}
```

## Golang

```go
func sumOfMultiples(n int) int {
    sum := 0
    for i := 1; i <= n; i++ {
        if i%3 == 0 || i%5 == 0 || i%7 == 0 {
            sum += i
        }
    }
    return sum
}
```

## Ruby

```ruby
def sum_of_multiples(n)
  sum = 0
  (1..n).each do |i|
    sum += i if i % 3 == 0 || i % 5 == 0 || i % 7 == 0
  end
  sum
end
```

## Scala

```scala
object Solution {
    def sumOfMultiples(n: Int): Int = {
        var sum = 0
        var i = 1
        while (i <= n) {
            if (i % 3 == 0 || i % 5 == 0 || i % 7 == 0) sum += i
            i += 1
        }
        sum
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sum_of_multiples(n: i32) -> i32 {
        let mut sum = 0;
        for i in 1..=n {
            if i % 3 == 0 || i % 5 == 0 || i % 7 == 0 {
                sum += i;
            }
        }
        sum
    }
}
```

## Racket

```racket
(define/contract (sum-of-multiples n)
  (-> exact-integer? exact-integer?)
  (for/sum ([i (in-range 1 (add1 n))]
            #:when (or (= (remainder i 3) 0)
                       (= (remainder i 5) 0)
                       (= (remainder i 7) 0)))
    i))
```

## Erlang

```erlang
-module(solution).
-export([sum_of_multiples/1]).

-spec sum_of_multiples(N :: integer()) -> integer().
sum_of_multiples(N) ->
    lists:foldl(fun(X, Acc) -> X + Acc end, 0,
        [I || I <- lists:seq(1, N),
              (I rem 3 =:= 0) orelse (I rem 5 =:= 0) orelse (I rem 7 =:= 0)]).
```

## Elixir

```elixir
defmodule Solution do
  @spec sum_of_multiples(n :: integer) :: integer
  def sum_of_multiples(n) do
    1..n
    |> Enum.filter(fn x -> rem(x, 3) == 0 or rem(x, 5) == 0 or rem(x, 7) == 0 end)
    |> Enum.sum()
  end
end
```
