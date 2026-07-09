# 2769. Find the Maximum Achievable Number

## Cpp

```cpp
class Solution {
public:
    int theMaximumAchievableX(int num, int t) {
        return num + t * (t + 1) / 2;
    }
};
```

## Java

```java
class Solution {
    public int theMaximumAchievableX(int num, int t) {
        return num + t * (t + 1) / 2;
    }
}
```

## Python

```python
class Solution(object):
    def theMaximumAchievableX(self, num, t):
        """
        :type num: int
        :type t: int
        :rtype: int
        """
        return num + t * (t + 1) // 2
```

## Python3

```python
class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + t * (t + 1) // 2
```

## C

```c
int theMaximumAchievableX(int num, int t) {
    return num + 2 * t;
}
```

## Csharp

```csharp
public class Solution {
    public int TheMaximumAchievableX(int num, int t) {
        return num + t * (t + 1) / 2;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} num
 * @param {number} t
 * @return {number}
 */
var theMaximumAchievableX = function(num, t) {
    return num + (t * (t + 1)) / 2;
};
```

## Typescript

```typescript
function theMaximumAchievableX(num: number, t: number): number {
    return num + 2 * t;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $num
     * @param Integer $t
     * @return Integer
     */
    function theMaximumAchievableX($num, $t) {
        return $num + intdiv($t * ($t + 1), 2);
    }
}
```

## Swift

```swift
class Solution {
    func theMaximumAchievableX(_ num: Int, _ t: Int) -> Int {
        return num + 2 * t
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun theMaximumAchievableX(num: Int, t: Int): Int {
        return num + t * (t + 1) / 2
    }
}
```

## Dart

```dart
class Solution {
  int theMaximumAchievableX(int num, int t) {
    return num + t * (t + 1) ~/ 2;
  }
}
```

## Golang

```go
func theMaximumAchievableX(num int, t int) int {
    return num + 2*t
}
```

## Ruby

```ruby
def the_maximum_achievable_x(num, t)
  num + t * (t + 1)
end
```

## Scala

```scala
object Solution {
    def theMaximumAchievableX(num: Int, t: Int): Int = {
        num + t * (t + 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn the_maximum_achievable_x(num: i32, t: i32) -> i32 {
        let t = t as i64;
        let num = num as i64;
        (num + t * (t + 1) / 2) as i32
    }
}
```

## Racket

```racket
(define/contract (the-maximum-achievable-x num t)
  (-> exact-integer? exact-integer? exact-integer?)
  (+ num (* t (+ t 1))))
```

## Erlang

```erlang
-spec the_maximum_achievable_x(Num :: integer(), T :: integer()) -> integer().
the_maximum_achievable_x(Num, T) ->
    Num + 2 * T.
```

## Elixir

```elixir
defmodule Solution do
  @spec the_maximum_achievable_x(num :: integer, t :: integer) :: integer
  def the_maximum_achievable_x(num, t) do
    num + div(t * (t + 1), 2)
  end
end
```
