# 0070. Climbing Stairs

## Cpp

```cpp
class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2) return n;
        int a = 1, b = 2;
        for (int i = 3; i <= n; ++i) {
            int c = a + b;
            a = b;
            b = c;
        }
        return b;
    }
};
```

## Java

```java
class Solution {
    public int climbStairs(int n) {
        if (n <= 2) return n;
        int first = 1, second = 2;
        for (int i = 3; i <= n; i++) {
            int third = first + second;
            first = second;
            second = third;
        }
        return second;
    }
}
```

## Python

```python
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b
```

## Python3

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b
```

## C

```c
int climbStairs(int n) {
    if (n <= 2) return n;
    int a = 1, b = 2, c;
    for (int i = 3; i <= n; ++i) {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}
```

## Csharp

```csharp
public class Solution {
    public int ClimbStairs(int n) {
        if (n <= 2) return n;
        int a = 1, b = 2;
        for (int i = 3; i <= n; i++) {
            int c = a + b;
            a = b;
            b = c;
        }
        return b;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    if (n <= 2) return n;
    let a = 1, b = 2;
    for (let i = 3; i <= n; i++) {
        const c = a + b;
        a = b;
        b = c;
    }
    return b;
};
```

## Typescript

```typescript
function climbStairs(n: number): number {
    if (n <= 2) return n;
    let a = 1, b = 2;
    for (let i = 3; i <= n; i++) {
        const c = a + b;
        a = b;
        b = c;
    }
    return b;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function climbStairs($n) {
        if ($n <= 2) {
            return $n;
        }
        $first = 1;
        $second = 2;
        for ($i = 3; $i <= $n; $i++) {
            $third = $first + $second;
            $first = $second;
            $second = $third;
        }
        return $second;
    }
}
```

## Swift

```swift
class Solution {
    func climbStairs(_ n: Int) -> Int {
        if n <= 2 { return n }
        var first = 1
        var second = 2
        for _ in 3...n {
            let third = first + second
            first = second
            second = third
        }
        return second
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun climbStairs(n: Int): Int {
        if (n <= 2) return n
        var a = 1
        var b = 2
        for (i in 3..n) {
            val c = a + b
            a = b
            b = c
        }
        return b
    }
}
```

## Dart

```dart
class Solution {
  int climbStairs(int n) {
    if (n <= 2) return n;
    int a = 1, b = 2;
    for (int i = 3; i <= n; ++i) {
      int c = a + b;
      a = b;
      b = c;
    }
    return b;
  }
}
```

## Golang

```go
func climbStairs(n int) int {
	if n <= 2 {
		return n
	}
	a, b := 1, 2
	for i := 3; i <= n; i++ {
		a, b = b, a+b
	}
	return b
}
```

## Ruby

```ruby
def climb_stairs(n)
  return n if n <= 2
  a, b = 1, 2
  (3..n).each { |_| a, b = b, a + b }
  b
end
```

## Scala

```scala
object Solution {
    def climbStairs(n: Int): Int = {
        if (n <= 2) return n
        var a = 1
        var b = 2
        var i = 3
        while (i <= n) {
            val c = a + b
            a = b
            b = c
            i += 1
        }
        b
    }
}
```

## Rust

```rust
impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        if n <= 2 {
            return n;
        }
        let mut a = 1;
        let mut b = 2;
        for _ in 3..=n {
            let c = a + b;
            a = b;
            b = c;
        }
        b
    }
}
```

## Racket

```racket
(define/contract (climb-stairs n)
  (-> exact-integer? exact-integer?)
  (let loop ((i 0) (a 1) (b 1))
    (if (= i n)
        a
        (loop (+ i 1) b (+ a b)))))
```

## Erlang

```erlang
-module(solution).
-export([climb_stairs/1]).

-spec climb_stairs(N :: integer()) -> integer().
climb_stairs(N) when N =< 0 ->
    0;
climb_stairs(1) ->
    1;
climb_stairs(2) ->
    2;
climb_stairs(N) ->
    climb(N, 3, 1, 2).

-spec climb(integer(), integer(), integer(), integer()) -> integer().
climb(N, I, A, B) when I =< N ->
    C = A + B,
    climb(N, I + 1, B, C);
climb(_N, _I, _A, B) ->
    B.
```

## Elixir

```elixir
defmodule Solution do
  @spec climb_stairs(n :: integer) :: integer
  def climb_stairs(n) when n <= 2, do: n

  def climb_stairs(n) do
    do_climb(n - 2, 1, 2)
  end

  defp do_climb(0, _a, b), do: b
  defp do_climb(k, a, b), do: do_climb(k - 1, b, a + b)
end
```
