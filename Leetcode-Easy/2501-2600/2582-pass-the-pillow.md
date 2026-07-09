# 2582. Pass the Pillow

## Cpp

```cpp
class Solution {
public:
    int passThePillow(int n, int time) {
        int cycle = n - 1;
        int fullRounds = time / cycle;
        int extra = time % cycle;
        if (fullRounds % 2 == 0) {
            return extra + 1;
        } else {
            return n - extra;
        }
    }
};
```

## Java

```java
class Solution {
    public int passThePillow(int n, int time) {
        int cycle = n - 1;
        int fullRounds = time / cycle;
        int extra = time % cycle;
        if (fullRounds % 2 == 0) {
            return extra + 1;
        } else {
            return n - extra;
        }
    }
}
```

## Python

```python
class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        cycle = n - 1
        full_rounds = time // cycle
        extra = time % cycle
        if full_rounds % 2 == 0:
            return extra + 1
        else:
            return n - extra
```

## Python3

```python
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        full = time // (n - 1)
        rem = time % (n - 1)
        if full % 2 == 0:
            return rem + 1
        else:
            return n - rem
```

## C

```c
int passThePillow(int n, int time) {
    int cycle = n - 1;
    int fullRounds = time / cycle;
    int extra = time % cycle;
    if (fullRounds % 2 == 0)
        return extra + 1;
    else
        return n - extra;
}
```

## Csharp

```csharp
public class Solution {
    public int PassThePillow(int n, int time) {
        int cycle = n - 1;
        int fullRounds = time / cycle;
        int extra = time % cycle;
        if (fullRounds % 2 == 0) {
            return extra + 1;
        } else {
            return n - extra;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} time
 * @return {number}
 */
var passThePillow = function(n, time) {
    const cycle = n - 1;
    const fullRounds = Math.floor(time / cycle);
    const extra = time % cycle;
    if (fullRounds % 2 === 0) {
        return extra + 1;
    } else {
        return n - extra;
    }
};
```

## Typescript

```typescript
function passThePillow(n: number, time: number): number {
    const cycle = n - 1;
    const fullRounds = Math.floor(time / cycle);
    const extra = time % cycle;
    return fullRounds % 2 === 0 ? extra + 1 : n - extra;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $time
     * @return Integer
     */
    function passThePillow($n, $time) {
        $cycle = $n - 1;
        $fullRounds = intdiv($time, $cycle);
        $extra = $time % $cycle;

        if ($fullRounds % 2 == 0) {
            return $extra + 1;
        } else {
            return $n - $extra;
        }
    }
}
```

## Swift

```swift
class Solution {
    func passThePillow(_ n: Int, _ time: Int) -> Int {
        let cycle = n - 1
        let fullRounds = time / cycle
        let extra = time % cycle
        if fullRounds % 2 == 0 {
            return extra + 1
        } else {
            return n - extra
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun passThePillow(n: Int, time: Int): Int {
        val cycle = n - 1
        val fullRounds = time / cycle
        val extra = time % cycle
        return if (fullRounds % 2 == 0) extra + 1 else n - extra
    }
}
```

## Dart

```dart
class Solution {
  int passThePillow(int n, int time) {
    int cycle = n - 1;
    int fullRounds = time ~/ cycle;
    int extra = time % cycle;
    if (fullRounds % 2 == 0) {
      return extra + 1;
    } else {
      return n - extra;
    }
  }
}
```

## Golang

```go
func passThePillow(n int, time int) int {
	period := n - 1
	fullRounds := time / period
	extra := time % period
	if fullRounds%2 == 0 {
		return extra + 1
	}
	return n - extra
}
```

## Ruby

```ruby
def pass_the_pillow(n, time)
  cycle = n - 1
  full_rounds = time / cycle
  extra_time = time % cycle
  if full_rounds.even?
    extra_time + 1
  else
    n - extra_time
  end
end
```

## Scala

```scala
object Solution {
    def passThePillow(n: Int, time: Int): Int = {
        val cycle = n - 1
        val fullRounds = time / cycle
        val extra = time % cycle
        if (fullRounds % 2 == 0) extra + 1 else n - extra
    }
}
```

## Rust

```rust
impl Solution {
    pub fn pass_the_pillow(n: i32, time: i32) -> i32 {
        let n = n as i64;
        let time = time as i64;
        let cycle = n - 1;
        let full_rounds = time / cycle;
        let extra_time = time % cycle;
        let position = if full_rounds % 2 == 0 {
            extra_time + 1
        } else {
            n - extra_time
        };
        position as i32
    }
}
```

## Racket

```racket
(define/contract (pass-the-pillow n time)
  (-> exact-integer? exact-integer? exact-integer?)
  (let* ([cycle (- n 1)]
         [fullRounds (quotient time cycle)]
         [extraTime (remainder time cycle)])
    (if (even? fullRounds)
        (+ extraTime 1)
        (- n extraTime))))
```

## Erlang

```erlang
-spec pass_the_pillow(N :: integer(), Time :: integer()) -> integer().
pass_the_pillow(N, Time) ->
    Cycle = N - 1,
    FullRounds = Time div Cycle,
    Extra = Time rem Cycle,
    case FullRounds rem 2 of
        0 -> Extra + 1;
        _ -> N - Extra
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec pass_the_pillow(n :: integer, time :: integer) :: integer
  def pass_the_pillow(n, time) do
    cycle = div(time, n - 1)
    rem_time = rem(time, n - 1)

    if rem(cycle, 2) == 0 do
      rem_time + 1
    else
      n - rem_time
    end
  end
end
```
