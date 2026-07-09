# 2894. Divisible and Non-divisible Sums Difference

## Cpp

```cpp
class Solution {
public:
    int differenceOfSums(int n, int m) {
        long long total = 1LL * n * (n + 1) / 2;
        long long k = n / m;
        long long sumDivisible = k * (k + 1) / 2 * m;
        long long ans = total - 2 * sumDivisible;
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    public int differenceOfSums(int n, int m) {
        long total = (long) n * (n + 1) / 2;
        long k = n / m;
        long sumDivisible = k * (k + 1) / 2 * m;
        long result = total - 2 * sumDivisible;
        return (int) result;
    }
}
```

## Python

```python
class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        total = n * (n + 1) // 2
        k = n // m
        sum_divisible = k * (k + 1) // 2 * m
        return total - 2 * sum_divisible
```

## Python3

```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = n * (n + 1) // 2
        k = n // m
        sum_divisible = k * (k + 1) // 2 * m
        return total - 2 * sum_divisible
```

## C

```c
int differenceOfSums(int n, int m) {
    long long total = (long long)n * (n + 1) / 2;
    long long k = n / m;
    long long sumDivisible = k * (k + 1) / 2 * m;
    long long result = total - 2 * sumDivisible;
    return (int)result;
}
```

## Csharp

```csharp
public class Solution {
    public int DifferenceOfSums(int n, int m) {
        long total = (long)n * (n + 1) / 2;
        long k = n / m;
        long sumDivisible = k * (k + 1) / 2 * m;
        long result = total - 2 * sumDivisible;
        return (int)result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} m
 * @return {number}
 */
var differenceOfSums = function(n, m) {
    const total = n * (n + 1) / 2;
    const k = Math.floor(n / m);
    return total - k * (k + 1) * m;
};
```

## Typescript

```typescript
function differenceOfSums(n: number, m: number): number {
    const total = n * (n + 1) / 2;
    const k = Math.floor(n / m);
    const sumDivisible = (k * (k + 1) / 2) * m;
    return total - 2 * sumDivisible;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $m
     * @return Integer
     */
    function differenceOfSums($n, $m) {
        // total sum of 1..n
        $total = intdiv($n * ($n + 1), 2);
        // count of multiples of m up to n
        $k = intdiv($n, $m);
        // sum of all numbers divisible by m
        $sumDivisible = intdiv($k * ($k + 1), 2) * $m;
        // result: total - 2 * sumDivisible
        return $total - 2 * $sumDivisible;
    }
}
```

## Swift

```swift
class Solution {
    func differenceOfSums(_ n: Int, _ m: Int) -> Int {
        let total = n * (n + 1) / 2
        let k = n / m
        let sumDivisible = k * (k + 1) / 2 * m
        return total - 2 * sumDivisible
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun differenceOfSums(n: Int, m: Int): Int {
        val total = n.toLong() * (n + 1) / 2
        val k = n / m
        val sumDivisible = k.toLong() * (k + 1) * m / 2
        val result = total - 2 * sumDivisible
        return result.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int differenceOfSums(int n, int m) {
    int total = n * (n + 1) ~/ 2;
    int k = n ~/ m;
    int sumDivisible = k * (k + 1) ~/ 2 * m;
    return total - 2 * sumDivisible;
  }
}
```

## Golang

```go
func differenceOfSums(n int, m int) int {
	total := n * (n + 1) / 2
	k := n / m
	sumDivisible := k * (k + 1) / 2 * m
	return total - 2*sumDivisible
}
```

## Ruby

```ruby
def difference_of_sums(n, m)
  total = n * (n + 1) / 2
  k = n / m
  sum_divisible = k * (k + 1) / 2 * m
  total - 2 * sum_divisible
end
```

## Scala

```scala
object Solution {
    def differenceOfSums(n: Int, m: Int): Int = {
        val k = n / m
        val total = n.toLong * (n + 1) / 2
        val sub = k.toLong * (k + 1) * m
        (total - sub).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn difference_of_sums(n: i32, m: i32) -> i32 {
        let n64 = n as i64;
        let total = n64 * (n64 + 1) / 2;
        let k = n / m;
        let k64 = k as i64;
        let sum_divisible = k64 * (k64 + 1) / 2 * m as i64;
        (total - 2 * sum_divisible) as i32
    }
}
```

## Racket

```racket
(define/contract (difference-of-sums n m)
  (-> exact-integer? exact-integer? exact-integer?)
  (let* ([total   (quotient (* n (+ n 1)) 2)]
         [k       (quotient n m)]
         [sum-div (quotient (* k (+ k 1) m) 2)])
    (- total (* 2 sum-div))))
```

## Erlang

```erlang
-spec difference_of_sums(N :: integer(), M :: integer()) -> integer().
difference_of_sums(N, M) ->
    Total = N * (N + 1) div 2,
    K = N div M,
    SumDiv = (K * (K + 1) div 2) * M,
    Total - 2 * SumDiv.
```

## Elixir

```elixir
defmodule Solution do
  @spec difference_of_sums(n :: integer, m :: integer) :: integer
  def difference_of_sums(n, m) do
    total = div(n * (n + 1), 2)
    k = div(n, m)
    total - k * (k + 1) * m
  end
end
```
