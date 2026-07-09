# 3021. Alice and Bob Playing Flower Game

## Cpp

```cpp
class Solution {
public:
    long long flowerGame(int n, int m) {
        long long oddX = (n + 1LL) / 2;
        long long evenX = n / 2;
        long long oddY = (m + 1LL) / 2;
        long long evenY = m / 2;
        return oddX * evenY + evenX * oddY;
    }
};
```

## Java

```java
class Solution {
    public long flowerGame(int n, int m) {
        long oddN = (n + 1L) / 2;
        long evenN = n / 2L;
        long oddM = (m + 1L) / 2;
        long evenM = m / 2L;
        return oddN * evenM + evenN * oddM;
    }
}
```

## Python

```python
class Solution(object):
    def flowerGame(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        odd_n = (n + 1) // 2
        even_n = n // 2
        odd_m = (m + 1) // 2
        even_m = m // 2
        return odd_n * even_m + even_n * odd_m
```

## Python3

```python
class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        odd_n = (n + 1) // 2
        even_n = n // 2
        odd_m = (m + 1) // 2
        even_m = m // 2
        return odd_n * even_m + even_n * odd_m
```

## C

```c
long long flowerGame(int n, int m) {
    long long odd_n = (n + 1LL) / 2;
    long long even_n = n / 2;
    long long odd_m = (m + 1LL) / 2;
    long long even_m = m / 2;
    return odd_n * even_m + even_n * odd_m;
}
```

## Csharp

```csharp
public class Solution {
    public long FlowerGame(int n, int m) {
        long oddX = (n + 1L) / 2;
        long evenX = n / 2;
        long oddY = (m + 1L) / 2;
        long evenY = m / 2;
        return oddX * evenY + evenX * oddY;
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
var flowerGame = function(n, m) {
    const evenX = Math.floor(n / 2);
    const oddX = n - evenX;
    const evenY = Math.floor(m / 2);
    const oddY = m - evenY;
    return oddX * evenY + evenX * oddY;
};
```

## Typescript

```typescript
function flowerGame(n: number, m: number): number {
    const oddN = Math.floor((n + 1) / 2);
    const evenN = n - oddN;
    const oddM = Math.floor((m + 1) / 2);
    const evenM = m - oddM;
    return oddN * evenM + evenN * oddM;
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
    function flowerGame($n, $m) {
        // Count odds and evens in [1..n]
        $oddN = intdiv($n + 1, 2);
        $evenN = $n - $oddN;
        // Count odds and evens in [1..m]
        $oddM = intdiv($m + 1, 2);
        $evenM = $m - $oddM;

        // Pairs with different parity
        return $oddN * $evenM + $evenN * $oddM;
    }
}
```

## Swift

```swift
class Solution {
    func flowerGame(_ n: Int, _ m: Int) -> Int {
        let oddN = (n + 1) / 2
        let evenN = n / 2
        let oddM = (m + 1) / 2
        let evenM = m / 2
        return oddN * evenM + evenN * oddM
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun flowerGame(n: Int, m: Int): Long {
        val oddN = (n + 1) / 2
        val evenN = n / 2
        val oddM = (m + 1) / 2
        val evenM = m / 2
        return oddN.toLong() * evenM + evenN.toLong() * oddM
    }
}
```

## Dart

```dart
class Solution {
  int flowerGame(int n, int m) {
    int oddN = (n + 1) >> 1;
    int evenN = n >> 1;
    int oddM = (m + 1) >> 1;
    int evenM = m >> 1;
    return oddN * evenM + evenN * oddM;
  }
}
```

## Golang

```go
func flowerGame(n int, m int) int64 {
	oddN := (n + 1) / 2
	evenN := n / 2
	oddM := (m + 1) / 2
	evenM := m / 2
	return int64(oddN*evenM + evenN*oddM)
}
```

## Ruby

```ruby
def flower_game(n, m)
  odd_n = (n + 1) / 2
  even_n = n / 2
  odd_m = (m + 1) / 2
  even_m = m / 2
  odd_n * even_m + even_n * odd_m
end
```

## Scala

```scala
object Solution {
    def flowerGame(n: Int, m: Int): Long = {
        val oddN = (n + 1) / 2
        val evenN = n / 2
        val oddM = (m + 1) / 2
        val evenM = m / 2
        oddN.toLong * evenM + evenN.toLong * oddM
    }
}
```

## Rust

```rust
impl Solution {
    pub fn flower_game(n: i32, m: i32) -> i64 {
        let n = n as i64;
        let m = m as i64;
        let odd_n = (n + 1) / 2;
        let even_n = n / 2;
        let odd_m = (m + 1) / 2;
        let even_m = m / 2;
        odd_n * even_m + even_n * odd_m
    }
}
```

## Racket

```racket
(define/contract (flower-game n m)
  (-> exact-integer? exact-integer? exact-integer?)
  (let* ([odd-n (quotient (+ n 1) 2)]
         [even-n (quotient n 2)]
         [odd-m (quotient (+ m 1) 2)]
         [even-m (quotient m 2)])
    (+ (* odd-n even-m)
       (* even-n odd-m))))
```

## Erlang

```erlang
-spec flower_game(N :: integer(), M :: integer()) -> integer().
flower_game(N, M) ->
    OddN = (N + 1) div 2,
    EvenN = N div 2,
    OddM = (M + 1) div 2,
    EvenM = M div 2,
    OddN * EvenM + EvenN * OddM.
```

## Elixir

```elixir
defmodule Solution do
  @spec flower_game(n :: integer, m :: integer) :: integer
  def flower_game(n, m) do
    odds_n = div(n + 1, 2)
    evens_n = n - odds_n
    odds_m = div(m + 1, 2)
    evens_m = m - odds_m
    odds_n * evens_m + evens_n * odds_m
  end
end
```
