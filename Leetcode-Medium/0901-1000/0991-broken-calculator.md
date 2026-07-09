# 0991. Broken Calculator

## Cpp

```cpp
class Solution {
public:
    int brokenCalc(int startValue, int target) {
        int ops = 0;
        while (target > startValue) {
            if (target % 2 == 1) {
                ++target; // make it even
            } else {
                target /= 2;
            }
            ++ops;
        }
        return ops + (startValue - target);
    }
};
```

## Java

```java
class Solution {
    public int brokenCalc(int startValue, int target) {
        int operations = 0;
        while (target > startValue) {
            if ((target & 1) == 0) {
                target >>= 1; // divide by 2 when even
            } else {
                target++;      // make it even
            }
            operations++;
        }
        return operations + (startValue - target);
    }
}
```

## Python

```python
class Solution(object):
    def brokenCalc(self, startValue, target):
        """
        :type startValue: int
        :type target: int
        :rtype: int
        """
        ops = 0
        while target > startValue:
            if target % 2 == 0:
                target //= 2
            else:
                target += 1
            ops += 1
        return ops + (startValue - target)
```

## Python3

```python
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        ops = 0
        while target > startValue:
            if target & 1:
                target += 1
            else:
                target //= 2
            ops += 1
        return ops + (startValue - target)
```

## C

```c
int brokenCalc(int startValue, int target) {
    int ops = 0;
    while (target > startValue) {
        if (target % 2 == 0) {
            target /= 2;
        } else {
            target += 1;
        }
        ++ops;
    }
    return ops + (startValue - target);
}
```

## Csharp

```csharp
public class Solution {
    public int BrokenCalc(int startValue, int target) {
        int ops = 0;
        while (target > startValue) {
            if ((target & 1) == 0) {
                target >>= 1;
            } else {
                target += 1;
            }
            ops++;
        }
        return ops + (startValue - target);
    }
}
```

## Javascript

```javascript
/**
 * @param {number} startValue
 * @param {number} target
 * @return {number}
 */
var brokenCalc = function(startValue, target) {
    let ops = 0;
    while (target > startValue) {
        if (target % 2 === 0) {
            target = target / 2;
        } else {
            target = target + 1;
        }
        ops++;
    }
    return ops + (startValue - target);
};
```

## Typescript

```typescript
function brokenCalc(startValue: number, target: number): number {
    let operations = 0;
    while (target > startValue) {
        if (target % 2 === 1) {
            target += 1;
        } else {
            target /= 2;
        }
        operations++;
    }
    return operations + (startValue - target);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $startValue
     * @param Integer $target
     * @return Integer
     */
    function brokenCalc($startValue, $target) {
        $operations = 0;
        while ($target > $startValue) {
            if ($target % 2 == 0) {
                $target = intdiv($target, 2);
            } else {
                $target += 1;
            }
            $operations++;
        }
        return $operations + ($startValue - $target);
    }
}
```

## Swift

```swift
class Solution {
    func brokenCalc(_ startValue: Int, _ target: Int) -> Int {
        var t = target
        var operations = 0
        while t > startValue {
            if t % 2 == 0 {
                t /= 2
            } else {
                t += 1
            }
            operations += 1
        }
        return operations + (startValue - t)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun brokenCalc(startValue: Int, target: Int): Int {
        var t = target
        var ops = 0
        while (t > startValue) {
            if ((t and 1) == 0) {
                t /= 2
            } else {
                t += 1
            }
            ops++
        }
        return ops + (startValue - t)
    }
}
```

## Dart

```dart
class Solution {
  int brokenCalc(int startValue, int target) {
    int ops = 0;
    while (target > startValue) {
      if ((target & 1) == 0) {
        target >>= 1;
      } else {
        target += 1;
      }
      ops++;
    }
    return ops + (startValue - target);
  }
}
```

## Golang

```go
func brokenCalc(startValue int, target int) int {
	steps := 0
	for target > startValue {
		if target%2 == 0 {
			target /= 2
		} else {
			target++
		}
		steps++
	}
	return steps + (startValue - target)
}
```

## Ruby

```ruby
def broken_calc(start_value, target)
  operations = 0
  while target > start_value
    if target.even?
      target /= 2
    else
      target += 1
    end
    operations += 1
  end
  operations + (start_value - target)
end
```

## Scala

```scala
object Solution {
    def brokenCalc(startValue: Int, target: Int): Int = {
        var ops = 0
        var cur = target.toLong
        val start = startValue.toLong
        while (cur > start) {
            if ((cur & 1L) == 0L) cur >>= 1
            else cur += 1
            ops += 1
        }
        ops + (start - cur).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn broken_calc(start_value: i32, target: i32) -> i32 {
        let mut ops: i32 = 0;
        let mut t: i64 = target as i64;
        let s: i64 = start_value as i64;

        while t > s {
            if t % 2 == 0 {
                t /= 2;
            } else {
                t += 1;
            }
            ops += 1;
        }

        ops + (s - t) as i32
    }
}
```

## Racket

```racket
(define/contract (broken-calc startValue target)
  (-> exact-integer? exact-integer? exact-integer?)
  (let loop ((t target) (cnt 0))
    (if (> t startValue)
        (if (even? t)
            (loop (/ t 2) (+ cnt 1))
            (loop (+ t 1) (+ cnt 1)))
        (+ cnt (- startValue t)))))
```

## Erlang

```erlang
-spec broken_calc(StartValue :: integer(), Target :: integer()) -> integer().
broken_calc(StartValue, Target) ->
    broken_calc_loop(StartValue, Target, 0).

broken_calc_loop(S, T, Steps) when T =< S ->
    Steps + (S - T);
broken_calc_loop(S, T, Steps) ->
    case T rem 2 of
        0 -> broken_calc_loop(S, T div 2, Steps + 1);
        _ -> broken_calc_loop(S, T + 1, Steps + 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec broken_calc(start_value :: integer, target :: integer) :: integer
  def broken_calc(start_value, target) do
    helper(start_value, target, 0)
  end

  defp helper(sv, t, cnt) when t <= sv do
    cnt + (sv - t)
  end

  defp helper(sv, t, cnt) do
    if rem(t, 2) == 0 do
      helper(sv, div(t, 2), cnt + 1)
    else
      helper(sv, t + 1, cnt + 1)
    end
  end
end
```
