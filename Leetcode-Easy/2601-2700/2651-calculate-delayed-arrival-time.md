# 2651. Calculate Delayed Arrival Time

## Cpp

```cpp
class Solution {
public:
    int findDelayedArrivalTime(int arrivalTime, int delayedTime) {
        return (arrivalTime + delayedTime) % 24;
    }
};
```

## Java

```java
class Solution {
    public int findDelayedArrivalTime(int arrivalTime, int delayedTime) {
        return (arrivalTime + delayedTime) % 24;
    }
}
```

## Python

```python
class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        """
        :type arrivalTime: int
        :type delayedTime: int
        :rtype: int
        """
        return (arrivalTime + delayedTime) % 24
```

## Python3

```python
class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime) % 24
```

## C

```c
int findDelayedArrivalTime(int arrivalTime, int delayedTime) {
    return (arrivalTime + delayedTime) % 24;
}
```

## Csharp

```csharp
public class Solution {
    public int FindDelayedArrivalTime(int arrivalTime, int delayedTime) {
        return (arrivalTime + delayedTime) % 24;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} arrivalTime
 * @param {number} delayedTime
 * @return {number}
 */
var findDelayedArrivalTime = function(arrivalTime, delayedTime) {
    return (arrivalTime + delayedTime) % 24;
};
```

## Typescript

```typescript
function findDelayedArrivalTime(arrivalTime: number, delayedTime: number): number {
    return (arrivalTime + delayedTime) % 24;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $arrivalTime
     * @param Integer $delayedTime
     * @return Integer
     */
    function findDelayedArrivalTime($arrivalTime, $delayedTime) {
        return ($arrivalTime + $delayedTime) % 24;
    }
}
```

## Swift

```swift
class Solution {
    func findDelayedArrivalTime(_ arrivalTime: Int, _ delayedTime: Int) -> Int {
        return (arrivalTime + delayedTime) % 24
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findDelayedArrivalTime(arrivalTime: Int, delayedTime: Int): Int {
        return (arrivalTime + delayedTime) % 24
    }
}
```

## Dart

```dart
class Solution {
  int findDelayedArrivalTime(int arrivalTime, int delayedTime) {
    return (arrivalTime + delayedTime) % 24;
  }
}
```

## Golang

```go
func findDelayedArrivalTime(arrivalTime int, delayedTime int) int {
    return (arrivalTime + delayedTime) % 24
}
```

## Ruby

```ruby
def find_delayed_arrival_time(arrival_time, delayed_time)
  (arrival_time + delayed_time) % 24
end
```

## Scala

```scala
object Solution {
    def findDelayedArrivalTime(arrivalTime: Int, delayedTime: Int): Int = {
        (arrivalTime + delayedTime) % 24
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_delayed_arrival_time(arrival_time: i32, delayed_time: i32) -> i32 {
        (arrival_time + delayed_time) % 24
    }
}
```

## Racket

```racket
(define/contract (find-delayed-arrival-time arrivalTime delayedTime)
  (-> exact-integer? exact-integer? exact-integer?)
  (modulo (+ arrivalTime delayedTime) 24))
```

## Erlang

```erlang
-spec find_delayed_arrival_time(ArrivalTime :: integer(), DelayedTime :: integer()) -> integer().
find_delayed_arrival_time(ArrivalTime, DelayedTime) ->
    (ArrivalTime + DelayedTime) rem 24.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_delayed_arrival_time(arrival_time :: integer, delayed_time :: integer) :: integer
  def find_delayed_arrival_time(arrival_time, delayed_time) do
    rem(arrival_time + delayed_time, 24)
  end
end
```
