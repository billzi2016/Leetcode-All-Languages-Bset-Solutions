# 1137. N-th Tribonacci Number

## Cpp

```cpp
class Solution {
public:
    int tribonacci(int n) {
        if (n == 0) return 0;
        if (n == 1 || n == 2) return 1;
        int t0 = 0, t1 = 1, t2 = 1;
        for (int i = 3; i <= n; ++i) {
            int t3 = t0 + t1 + t2;
            t0 = t1;
            t1 = t2;
            t2 = t3;
        }
        return t2;
    }
};
```

## Java

```java
class Solution {
    public int tribonacci(int n) {
        if (n == 0) return 0;
        if (n == 1 || n == 2) return 1;
        int[] t = new int[n + 1];
        t[0] = 0;
        t[1] = t[2] = 1;
        for (int i = 3; i <= n; i++) {
            t[i] = t[i - 1] + t[i - 2] + t[i - 3];
        }
        return t[n];
    }
}
```

## Python

```python
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n <= 2:
            return 1
        a, b, c = 0, 1, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c
```

## Python3

```python
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return 1
        a, b, c = 0, 1, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c
```

## C

```c
int tribonacci(int n) {
    if (n == 0) return 0;
    if (n == 1 || n == 2) return 1;
    int f[38];
    f[0] = 0;
    f[1] = f[2] = 1;
    for (int i = 3; i <= n; ++i) {
        f[i] = f[i - 1] + f[i - 2] + f[i - 3];
    }
    return f[n];
}
```

## Csharp

```csharp
public class Solution {
    public int Tribonacci(int n) {
        if (n == 0) return 0;
        if (n == 1 || n == 2) return 1;
        int a = 0, b = 1, c = 1;
        for (int i = 3; i <= n; i++) {
            int d = a + b + c;
            a = b;
            b = c;
            c = d;
        }
        return c;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var tribonacci = function(n) {
    if (n === 0) return 0;
    if (n === 1 || n === 2) return 1;
    let a = 0, b = 1, c = 1;
    for (let i = 3; i <= n; i++) {
        const d = a + b + c;
        a = b;
        b = c;
        c = d;
    }
    return c;
};
```

## Typescript

```typescript
function tribonacci(n: number): number {
    if (n === 0) return 0;
    if (n === 1 || n === 2) return 1;
    const dp: number[] = new Array(n + 1);
    dp[0] = 0;
    dp[1] = dp[2] = 1;
    for (let i = 3; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
    }
    return dp[n];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function tribonacci($n) {
        if ($n == 0) return 0;
        if ($n == 1 || $n == 2) return 1;
        $t0 = 0;
        $t1 = 1;
        $t2 = 1;
        for ($i = 3; $i <= $n; $i++) {
            $t3 = $t0 + $t1 + $t2;
            $t0 = $t1;
            $t1 = $t2;
            $t2 = $t3;
        }
        return $t2;
    }
}
```

## Swift

```swift
class Solution {
    func tribonacci(_ n: Int) -> Int {
        if n == 0 { return 0 }
        if n == 1 || n == 2 { return 1 }
        var dp = [Int](repeating: 0, count: n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        for i in 3...n {
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        }
        return dp[n]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun tribonacci(n: Int): Int {
        if (n == 0) return 0
        if (n == 1 || n == 2) return 1
        var a = 0
        var b = 1
        var c = 1
        var cur = 0
        for (i in 3..n) {
            cur = a + b + c
            a = b
            b = c
            c = cur
        }
        return c
    }
}
```

## Dart

```dart
class Solution {
  int tribonacci(int n) {
    if (n == 0) return 0;
    if (n == 1 || n == 2) return 1;
    int a = 0, b = 1, c = 1;
    for (int i = 3; i <= n; i++) {
      int d = a + b + c;
      a = b;
      b = c;
      c = d;
    }
    return c;
  }
}
```

## Golang

```go
func tribonacci(n int) int {
	if n == 0 {
		return 0
	}
	if n == 1 || n == 2 {
		return 1
	}
	var f [38]int
	f[0], f[1], f[2] = 0, 1, 1
	for i := 3; i <= n; i++ {
		f[i] = f[i-1] + f[i-2] + f[i-3]
	}
	return f[n]
}
```

## Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def tribonacci(n)
  return 0 if n == 0
  return 1 if n <= 2

  a, b, c = 0, 1, 1
  (3..n).each do |_|
    a, b, c = b, c, a + b + c
  end
  c
end
```

## Scala

```scala
object Solution {
    def tribonacci(n: Int): Int = {
        if (n == 0) return 0
        if (n <= 2) return 1
        var a = 0   // T0
        var b = 1   // T1
        var c = 1   // T2
        for (_ <- 3 to n) {
            val d = a + b + c
            a = b
            b = c
            c = d
        }
        c
    }
}
```

## Rust

```rust
impl Solution {
    pub fn tribonacci(n: i32) -> i32 {
        if n == 0 {
            return 0;
        }
        if n <= 2 {
            return 1;
        }
        let mut a = 0;
        let mut b = 1;
        let mut c = 1;
        for _ in 3..=n {
            let d = a + b + c;
            a = b;
            b = c;
            c = d;
        }
        c
    }
}
```

## Racket

```racket
(define/contract (tribonacci n)
  (-> exact-integer? exact-integer?)
  (cond [(= n 0) 0]
        [(or (= n 1) (= n 2)) 1]
        [else
         (let loop ((i 3) (a 0) (b 1) (c 1))
           (if (> i n)
               c
               (loop (+ i 1) b c (+ a b c))))]))
```

## Erlang

```erlang
-module(solution).
-export([tribonacci/1]).

-spec tribonacci(N :: integer()) -> integer().
tribonacci(0) -> 0;
tribonacci(1) -> 1;
tribonacci(2) -> 1;
tribonacci(N) when N > 2 ->
    trib_loop(3, N, 0, 1, 1).

trib_loop(I, N, A, B, C) when I =< N ->
    D = A + B + C,
    trib_loop(I + 1, N, B, C, D);
trib_loop(_, _, _, _, C) -> C.
```

## Elixir

```elixir
defmodule Solution do
  @spec tribonacci(n :: integer) :: integer
  def tribonacci(0), do: 0
  def tribonacci(1), do: 1
  def tribonacci(2), do: 1

  def tribonacci(n) when n > 2 do
    {_, _, result} =
      Enum.reduce(3..n, {0, 1, 1}, fn _i, {t0, t1, t2} ->
        t3 = t0 + t1 + t2
        {t1, t2, t3}
      end)

    result
  end
end
```
