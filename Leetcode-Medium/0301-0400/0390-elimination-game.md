# 0390. Elimination Game

## Cpp

```cpp
class Solution {
public:
    int lastRemaining(int n) {
        long long head = 1;
        long long step = 1;
        long long remaining = n;
        bool left = true;
        while (remaining > 1) {
            if (left || (remaining % 2 == 1)) {
                head += step;
            }
            remaining >>= 1; // divide by 2
            step <<= 1;      // multiply by 2
            left = !left;
        }
        return static_cast<int>(head);
    }
};
```

## Java

```java
class Solution {
    public int lastRemaining(int n) {
        long head = 1;
        long step = 1;
        long remaining = n;
        boolean left = true;
        while (remaining > 1) {
            if (left || (remaining % 2 == 1)) {
                head += step;
            }
            remaining >>= 1; // divide by 2
            step <<= 1;      // multiply by 2
            left = !left;
        }
        return (int) head;
    }
}
```

## Python

```python
class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        head = 1
        step = 1
        remaining = n
        left = True
        while remaining > 1:
            if left or remaining % 2 == 1:
                head += step
            remaining //= 2
            step <<= 1
            left = not left
        return head
```

## Python3

```python
class Solution:
    def lastRemaining(self, n: int) -> int:
        head = 1
        step = 1
        remaining = n
        left = True
        while remaining > 1:
            if left or remaining % 2 == 1:
                head += step
            remaining //= 2
            step <<= 1
            left = not left
        return head
```

## C

```c
int lastRemaining(int n) {
    int head = 1;
    int step = 1;
    int remaining = n;
    int left = 1; // true
    
    while (remaining > 1) {
        if (left || (remaining % 2 == 1)) {
            head += step;
        }
        remaining >>= 1;      // divide by 2
        step <<= 1;           // multiply by 2
        left = !left;
    }
    
    return head;
}
```

## Csharp

```csharp
public class Solution
{
    public int LastRemaining(int n)
    {
        long head = 1;
        long step = 1;
        long remaining = n;
        bool leftToRight = true;

        while (remaining > 1)
        {
            if (leftToRight || (remaining % 2 == 1))
            {
                head += step;
            }
            remaining >>= 1; // divide by 2
            step <<= 1;      // multiply by 2
            leftToRight = !leftToRight;
        }

        return (int)head;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var lastRemaining = function(n) {
    let head = 1;
    let step = 1;
    let remaining = n;
    let left = true;
    
    while (remaining > 1) {
        if (left || remaining % 2 === 1) {
            head += step;
        }
        remaining = Math.floor(remaining / 2);
        step *= 2;
        left = !left;
    }
    
    return head;
};
```

## Typescript

```typescript
function lastRemaining(n: number): number {
    let head = 1;
    let step = 1;
    let remaining = n;
    let left = true;

    while (remaining > 1) {
        if (left || remaining % 2 === 1) {
            head += step;
        }
        remaining = Math.floor(remaining / 2);
        step *= 2;
        left = !left;
    }

    return head;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function lastRemaining($n) {
        $head = 1;
        $step = 1;
        $remaining = $n;
        $left = true;

        while ($remaining > 1) {
            if ($left || ($remaining % 2 == 1)) {
                $head += $step;
            }
            $remaining = intdiv($remaining, 2);
            $step <<= 1; // multiply by 2
            $left = !$left;
        }

        return $head;
    }
}
```

## Swift

```swift
class Solution {
    func lastRemaining(_ n: Int) -> Int {
        var head = 1
        var step = 1
        var remaining = n
        var left = true
        
        while remaining > 1 {
            if left || remaining % 2 == 1 {
                head += step
            }
            remaining /= 2
            step <<= 1
            left.toggle()
        }
        
        return head
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun lastRemaining(n: Int): Int {
        var head = 1L
        var step = 1L
        var remaining = n.toLong()
        var left = true
        while (remaining > 1) {
            if (left || remaining % 2L == 1L) {
                head += step
            }
            remaining /= 2
            step *= 2
            left = !left
        }
        return head.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int lastRemaining(int n) {
    int head = 1;
    int step = 1;
    int remaining = n;
    bool left = true;
    while (remaining > 1) {
      if (left || remaining % 2 == 1) {
        head += step;
      }
      remaining ~/= 2;
      step <<= 1;
      left = !left;
    }
    return head;
  }
}
```

## Golang

```go
func lastRemaining(n int) int {
    head, step := 1, 1
    left := true
    remaining := n
    for remaining > 1 {
        if left || remaining%2 == 1 {
            head += step
        }
        remaining /= 2
        step *= 2
        left = !left
    }
    return head
}
```

## Ruby

```ruby
def last_remaining(n)
  head = 1
  step = 1
  remaining = n
  left = true
  while remaining > 1
    if left || (remaining & 1) == 1
      head += step
    end
    remaining >>= 1
    step <<= 1
    left = !left
  end
  head
end
```

## Scala

```scala
object Solution {
    def lastRemaining(n: Int): Int = {
        var head: Long = 1L
        var step: Long = 1L
        var remaining = n
        var left = true
        while (remaining > 1) {
            if (left || (remaining % 2 == 1)) {
                head += step
            }
            remaining >>= 1
            step <<= 1
            left = !left
        }
        head.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn last_remaining(n: i32) -> i32 {
        let mut head: i64 = 1;
        let mut step: i64 = 1;
        let mut remaining: i64 = n as i64;
        let mut left = true;

        while remaining > 1 {
            if left || (remaining % 2 == 1) {
                head += step;
            }
            remaining /= 2;
            step *= 2;
            left = !left;
        }

        head as i32
    }
}
```

## Racket

```racket
(define/contract (last-remaining n)
  (-> exact-integer? exact-integer?)
  (let loop ((head 1) (step 1) (remain n) (left #t))
    (if (= remain 1)
        head
        (let* ((new-head (if (or left (= (remainder remain 2) 1))
                             (+ head step)
                             head))
               (new-step (* step 2))
               (new-remain (quotient remain 2)))
          (loop new-head new-step new-remain (not left))))))
```

## Erlang

```erlang
-module(solution).
-export([last_remaining/1]).

-spec last_remaining(N :: integer()) -> integer().
last_remaining(N) ->
    loop(1, 1, N, true).

loop(Head, _Step, 1, _Left) ->
    Head;
loop(Head, Step, Rem, Left) ->
    NewHead = case (Left orelse (Rem rem 2 == 1)) of
        true -> Head + Step;
        false -> Head
    end,
    loop(NewHead, Step * 2, Rem div 2, not Left).
```

## Elixir

```elixir
defmodule Solution do
  @spec last_remaining(n :: integer) :: integer
  def last_remaining(n) do
    loop(1, 1, n, true)
  end

  defp loop(head, _step, 1, _left), do: head

  defp loop(head, step, remaining, left) do
    new_head =
      if left or rem(remaining, 2) == 1 do
        head + step
      else
        head
      end

    loop(new_head, step * 2, div(remaining, 2), not left)
  end
end
```
