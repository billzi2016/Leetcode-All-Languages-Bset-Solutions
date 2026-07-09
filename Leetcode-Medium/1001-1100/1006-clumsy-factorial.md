# 1006. Clumsy Factorial

## Cpp

```cpp
class Solution {
public:
    int clumsy(int n) {
        if (n <= 2) return n;
        if (n == 3) return 6;
        if (n == 4) return 7;
        switch (n % 4) {
            case 0: return n + 1;
            case 1: return n + 2;
            case 2: return n + 2;
            default: // case 3
                return n - 1;
        }
    }
};
```

## Java

```java
class Solution {
    public int clumsy(int n) {
        if (n <= 2) return n;
        if (n == 3) return 6;
        if (n == 4) return 7;
        int mod = n % 4;
        if (mod == 0) return n + 1;
        if (mod == 1 || mod == 2) return n + 2;
        return n - 1; // mod == 3
    }
}
```

## Python

```python
class Solution(object):
    def clumsy(self, n):
        """
        :type n: int
        :rtype: int
        """
        stack = [n]
        op = 0  # 0:* ,1:/ ,2:+ ,3:-
        for i in range(n - 1, 0, -1):
            if op % 4 == 0:
                stack.append(stack.pop() * i)
            elif op % 4 == 1:
                stack.append(stack.pop() // i)
            elif op % 4 == 2:
                stack.append(i)
            else:  # op % 4 == 3
                stack.append(-i)
            op += 1
        return sum(stack)
```

## Python3

```python
class Solution:
    def clumsy(self, n: int) -> int:
        if n <= 2:
            return n
        if n == 3:
            return 6
        if n == 4:
            return 7
        mod = n % 4
        if mod == 0:
            return n + 1
        if mod == 1 or mod == 2:
            return n + 2
        # mod == 3
        return n - 1
```

## C

```c
int clumsy(int n) {
    if (n <= 4) {
        if (n == 1) return 1;
        if (n == 2) return 2;
        if (n == 3) return 6;
        return 7; // n == 4
    }
    int r = n % 4;
    if (r == 0) return n + 1;
    if (r == 3) return n - 1;
    return n + 2;
}
```

## Csharp

```csharp
public class Solution {
    public int Clumsy(int n) {
        if (n <= 2) return n;
        if (n == 3) return 6;
        switch (n % 4) {
            case 0: return n + 1;
            case 3: return n - 1;
            default: return n + 2;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var clumsy = function(n) {
    if (n === 1) return 1;
    if (n === 2) return 2;
    if (n === 3) return 6;
    if (n === 4) return 7;
    const mod = n % 4;
    switch (mod) {
        case 0: return n + 1;
        case 1: return n + 2;
        case 2: return n + 2;
        default: // case 3
            return n - 1;
    }
};
```

## Typescript

```typescript
function clumsy(n: number): number {
    if (n <= 4) {
        switch (n) {
            case 1: return 1;
            case 2: return 2;
            case 3: return 6;
            case 4: return 7;
        }
    }
    const r = n % 4;
    if (r === 0) return n + 1;
    if (r === 1) return n + 2;
    if (r === 2) return n + 2;
    // r === 3
    return n - 1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function clumsy($n) {
        if ($n == 1) return 1;
        if ($n == 2) return 2;
        if ($n == 3) return 6;
        if ($n == 4) return 7;

        $mod = $n % 4;
        if ($mod == 0) {
            return $n + 1;
        } elseif ($mod == 1) {
            return $n + 2;
        } elseif ($mod == 2) {
            return $n + 2;
        } else { // $mod == 3
            return $n - 1;
        }
    }
}
```

## Swift

```swift
class Solution {
    func clumsy(_ n: Int) -> Int {
        if n <= 2 { return n }
        if n == 3 { return 3 }
        if n == 4 { return 7 }
        let r = n % 4
        if r == 0 {
            return n + 1
        } else if r == 3 {
            return n - 1
        } else {
            return n + 2
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun clumsy(n: Int): Int {
        if (n <= 2) return n
        if (n == 3) return 6
        if (n == 4) return 7
        return when (n % 4) {
            0 -> n + 1
            1, 2 -> n + 2
            else -> n - 1
        }
    }
}
```

## Dart

```dart
class Solution {
  int clumsy(int n) {
    if (n <= 2) return n;
    if (n == 3) return 6;
    if (n == 4) return 7;
    switch (n % 4) {
      case 0:
        return n + 1;
      case 1:
        return n + 2;
      case 2:
        return n + 2;
      default: // case 3
        return n - 1;
    }
  }
}
```

## Golang

```go
func clumsy(n int) int {
    if n <= 4 {
        switch n {
        case 1:
            return 1
        case 2:
            return 2
        case 3:
            return 6
        case 4:
            return 7
        }
    }
    switch n % 4 {
    case 0:
        return n + 1
    case 1, 2:
        return n + 2
    default: // case 3
        return n - 1
    }
}
```

## Ruby

```ruby
def clumsy(n)
  return n if n <= 2
  return 6 if n == 3
  return 7 if n == 4
  case n % 4
  when 0
    n + 1
  when 1, 2
    n + 2
  else
    n - 1
  end
end
```

## Scala

```scala
object Solution {
    def clumsy(n: Int): Int = {
        val stack = new java.util.ArrayDeque[Int]()
        var i = n
        stack.push(i)
        i -= 1
        var op = 0 // 0: *, 1: /, 2: +, 3: -
        while (i > 0) {
            op % 4 match {
                case 0 => // multiplication
                    val top = stack.pop()
                    stack.push(top * i)
                case 1 => // division
                    val top = stack.pop()
                    stack.push(top / i)
                case 2 => // addition
                    stack.push(i)
                case 3 => // subtraction
                    stack.push(-i)
            }
            i -= 1
            op += 1
        }
        var sum = 0
        val it = stack.iterator()
        while (it.hasNext) {
            sum += it.next()
        }
        sum
    }
}
```

## Rust

```rust
impl Solution {
    pub fn clumsy(n: i32) -> i32 {
        match n {
            1 => 1,
            2 => 2,
            3 => 6,
            4 => 7,
            _ => match n % 4 {
                0 => n + 1,
                1 => n + 2,
                2 => n + 2,
                _ => n - 1, // remainder 3
            },
        }
    }
}
```

## Racket

```racket
(define/contract (clumsy n)
  (-> exact-integer? exact-integer?)
  (cond
    [(= n 1) 1]
    [(= n 2) 2]
    [(= n 3) 6]
    [(= n 4) 7]
    [else
     (let ([r (remainder n 4)])
       (cond
         [(= r 0) (+ n 1)]
         [(or (= r 1) (= r 2)) (+ n 2)]
         [(= r 3) (- n 1)]))]))
```

## Erlang

```erlang
-spec clumsy(N :: integer()) -> integer().
clumsy(1) -> 1;
clumsy(2) -> 2;
clumsy(3) -> 6;
clumsy(4) -> 7;
clumsy(N) ->
    case N rem 4 of
        0 -> N + 1;
        1 -> N + 2;
        2 -> N + 2;
        3 -> N - 1
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec clumsy(n :: integer) :: integer
  def clumsy(n) do
    cond do
      n == 1 -> 1
      n == 2 -> 2
      n == 3 -> 6
      n == 4 -> 7
      true ->
        case rem(n, 4) do
          0 -> n + 1
          1 -> n + 2
          2 -> n + 2
          3 -> n - 1
        end
    end
  end
end
```
