# 2485. Find the Pivot Integer

## Cpp

```cpp
class Solution {
public:
    int pivotInteger(int n) {
        long long total = 1LL * n * (n + 1) / 2;
        long long x = static_cast<long long>(std::sqrt((double)total));
        if (x * x == total) return static_cast<int>(x);
        return -1;
    }
};
```

## Java

```java
class Solution {
    public int pivotInteger(int n) {
        long total = (long) n * (n + 1) / 2;
        long root = (long) Math.sqrt(total);
        if (root * root == total) {
            return (int) root;
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = n * (n + 1) // 2
        x = int(total ** 0.5)
        return x if x * x == total else -1
```

## Python3

```python
import math

class Solution:
    def pivotInteger(self, n: int) -> int:
        total = n * (n + 1) // 2
        x = math.isqrt(total)
        return x if x * x == total else -1
```

## C

```c
int pivotInteger(int n) {
    long long total = (long long)n * (n + 1) / 2;
    int x = (int)sqrt((double)total);
    if ((long long)x * x == total) return x;
    return -1;
}
```

## Csharp

```csharp
public class Solution
{
    public int PivotInteger(int n)
    {
        long total = (long)n * (n + 1) / 2;
        int x = (int)Math.Sqrt(total);
        return (long)x * x == total ? x : -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var pivotInteger = function(n) {
    const total = (n * (n + 1)) / 2;
    const root = Math.floor(Math.sqrt(total));
    return root * root === total ? root : -1;
};
```

## Typescript

```typescript
function pivotInteger(n: number): number {
    const total = (n * (n + 1)) / 2;
    const x = Math.floor(Math.sqrt(total));
    return x * x === total ? x : -1;
}
```

## Php

```php
<?php
class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function pivotInteger($n) {
        $total = $n * ($n + 1) / 2;
        $x = (int)sqrt($total);
        return ($x * $x == $total) ? $x : -1;
    }
}
?>
```

## Swift

```swift
class Solution {
    func pivotInteger(_ n: Int) -> Int {
        let total = Int64(n) * Int64(n + 1) / 2
        let root = Int64(Double(total).squareRoot())
        return root * root == total ? Int(root) : -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun pivotInteger(n: Int): Int {
        val total = n.toLong() * (n + 1) / 2
        val sqrt = kotlin.math.sqrt(total.toDouble()).toLong()
        return if (sqrt * sqrt == total) sqrt.toInt() else -1
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int pivotInteger(int n) {
    int total = n * (n + 1) ~/ 2;
    int root = sqrt(total).toInt();
    return root * root == total ? root : -1;
  }
}
```

## Golang

```go
import "math"

func pivotInteger(n int) int {
    total := int64(n) * int64(n+1) / 2
    x := int(math.Sqrt(float64(total)))
    if int64(x)*int64(x) == total {
        return x
    }
    return -1
}
```

## Ruby

```ruby
def pivot_integer(n)
  total = n * (n + 1) / 2
  x = Math.sqrt(total).to_i
  x * x == total ? x : -1
end
```

## Scala

```scala
object Solution {
    def pivotInteger(n: Int): Int = {
        val total = n.toLong * (n + 1L) / 2L
        val x = math.sqrt(total.toDouble).toLong
        if (x * x == total) x.toInt else -1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn pivot_integer(n: i32) -> i32 {
        let n = n as i64;
        let total = n * (n + 1) / 2;
        let x = (total as f64).sqrt() as i64;
        if x * x == total { x as i32 } else { -1 }
    }
}
```

## Racket

```racket
#lang racket
(provide pivot-integer)

(define/contract (pivot-integer n)
  (-> exact-integer? exact-integer?)
  (let* ([total (/ (* n (+ n 1)) 2)]
         [root (floor (sqrt total))])
    (if (= (* root root) total) root -1)))
```

## Erlang

```erlang
-spec pivot_integer(N :: integer()) -> integer().
pivot_integer(N) ->
    Total = N * (N + 1) div 2,
    X = trunc(math:sqrt(Total)),
    case X * X == Total of
        true -> X;
        false -> -1
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec pivot_integer(n :: integer) :: integer
  def pivot_integer(n) do
    total = div(n * (n + 1), 2)
    s = :math.sqrt(total) |> trunc()
    if s * s == total, do: s, else: -1
  end
end
```
