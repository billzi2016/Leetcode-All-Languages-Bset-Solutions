# 1227. Airplane Seat Assignment Probability

## Cpp

```cpp
class Solution {
public:
    double nthPersonGetsNthSeat(int n) {
        return n == 1 ? 1.0 : 0.5;
    }
};
```

## Java

```java
class Solution {
    public double nthPersonGetsNthSeat(int n) {
        return n == 1 ? 1.0 : 0.5;
    }
}
```

## Python

```python
class Solution(object):
    def nthPersonGetsNthSeat(self, n):
        """
        :type n: int
        :rtype: float
        """
        return 1.0 if n == 1 else 0.5
```

## Python3

```python
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1.0 if n == 1 else 0.5
```

## C

```c
double nthPersonGetsNthSeat(int n) {
    return n == 1 ? 1.0 : 0.5;
}
```

## Csharp

```csharp
public class Solution
{
    public double NthPersonGetsNthSeat(int n)
    {
        return n == 1 ? 1.0 : 0.5;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var nthPersonGetsNthSeat = function(n) {
    return n === 1 ? 1 : 0.5;
};
```

## Typescript

```typescript
function nthPersonGetsNthSeat(n: number): number {
    return n === 1 ? 1 : 0.5;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Float
     */
    function nthPersonGetsNthSeat($n) {
        if ($n == 1) {
            return 1.0;
        }
        return 0.5;
    }
}
```

## Swift

```swift
class Solution {
    func nthPersonGetsNthSeat(_ n: Int) -> Double {
        return n == 1 ? 1.0 : 0.5
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun nthPersonGetsNthSeat(n: Int): Double {
        return if (n == 1) 1.0 else 0.5
    }
}
```

## Dart

```dart
class Solution {
  double nthPersonGetsNthSeat(int n) {
    return n == 1 ? 1.0 : 0.5;
  }
}
```

## Golang

```go
func nthPersonGetsNthSeat(n int) float64 {
	if n == 1 {
		return 1.0
	}
	return 0.5
}
```

## Ruby

```ruby
def nth_person_gets_nth_seat(n)
  n == 1 ? 1.0 : 0.5
end
```

## Scala

```scala
object Solution {
    def nthPersonGetsNthSeat(n: Int): Double = {
        if (n == 1) 1.0 else 0.5
    }
}
```

## Rust

```rust
impl Solution {
    pub fn nth_person_gets_nth_seat(n: i32) -> f64 {
        if n == 1 { 1.0 } else { 0.5 }
    }
}
```

## Racket

```racket
(define/contract (nth-person-gets-nth-seat n)
  (-> exact-integer? flonum?)
  (if (= n 1) 1.0 0.5))
```

## Erlang

```erlang
-module(solution).
-export([nth_person_gets_nth_seat/1]).

-spec nth_person_gets_nth_seat(N :: integer()) -> float().
nth_person_gets_nth_seat(1) ->
    1.0;
nth_person_gets_nth_seat(N) when N >= 2 ->
    0.5.
```

## Elixir

```elixir
defmodule Solution do
  @spec nth_person_gets_nth_seat(n :: integer) :: float
  def nth_person_gets_nth_seat(1), do: 1.0
  def nth_person_gets_nth_seat(_n), do: 0.5
end
```
