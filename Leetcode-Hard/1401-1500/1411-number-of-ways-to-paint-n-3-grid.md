# 1411. Number of Ways to Paint N × 3 Grid

## Cpp

```cpp
class Solution {
public:
    int numOfWays(int n) {
        const long long MOD = 1000000007LL;
        if (n == 0) return 0;
        long long dp0 = 6; // patterns with all three colors distinct
        long long dp1 = 6; // patterns with first and third same
        for (int i = 2; i <= n; ++i) {
            long long ndp0 = (dp0 * 2 + dp1 * 2) % MOD;
            long long ndp1 = (dp0 * 2 + dp1) % MOD;
            dp0 = ndp0;
            dp1 = ndp1;
        }
        return static_cast<int>((dp0 + dp1) % MOD);
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;

    public int numOfWays(int n) {
        if (n == 1) return 12;
        long a = 6; // patterns with all three colors different
        long b = 6; // patterns with first and third same, middle different
        for (int i = 2; i <= n; i++) {
            long na = (a * 2 + b * 2) % MOD;
            long nb = (a * 2 + b * 3) % MOD;
            a = na;
            b = nb;
        }
        return (int) ((a + b) % MOD);
    }
}
```

## Python

```python
class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        if n == 0:
            return 0
        # dp_type0: rows with all three colors different
        # dp_type1: rows with first and third same, middle different
        dp0, dp1 = 6, 6  # for the first row
        for _ in range(2, n + 1):
            new_dp0 = (dp0 * 2 + dp1 * 2) % MOD
            new_dp1 = (dp0 * 2 + dp1) % MOD
            dp0, dp1 = new_dp0, new_dp1
        return (dp0 + dp1) % MOD
```

## Python3

```python
class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        a, b = 6, 6  # type A and type B counts for the first row
        for _ in range(2, n + 1):
            na = (2 * a + 2 * b) % MOD
            nb = (2 * a + 3 * b) % MOD
            a, b = na, nb
        return (a + b) % MOD
```

## C

```c
int numOfWays(int n) {
    const int MOD = 1000000007;
    long long a = 6; // patterns with all three colors different
    long long b = 6; // patterns with first and third colors same
    for (int i = 2; i <= n; ++i) {
        long long newA = (a * 2 + b * 2) % MOD;
        long long newB = (a * 2 + b * 3) % MOD;
        a = newA;
        b = newB;
    }
    return (int)((a + b) % MOD);
}
```

## Csharp

```csharp
public class Solution
{
    private const int MOD = 1000000007;
    public int NumOfWays(int n)
    {
        long a = 6; // patterns with all three colors different
        long b = 6; // patterns with first and third same, middle different

        for (int i = 2; i <= n; i++)
        {
            long na = (a * 2 + b * 2) % MOD;
            long nb = (a * 2 + b * 3) % MOD;
            a = na;
            b = nb;
        }

        return (int)((a + b) % MOD);
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var numOfWays = function(n) {
    const MOD = 1000000007;
    let a = 6; // last row all distinct colors
    let b = 6; // last row first and third same, middle different
    for (let i = 2; i <= n; ++i) {
        const newA = (3 * a + 2 * b) % MOD;
        const newB = (2 * a + 2 * b) % MOD;
        a = newA;
        b = newB;
    }
    return (a + b) % MOD;
};
```

## Typescript

```typescript
function numOfWays(n: number): number {
    const MOD = 1000000007;
    let a = 6; // all three colors different in the row
    let b = 6; // first and third same, middle different
    for (let i = 2; i <= n; i++) {
        const newA = ((a * 2) % MOD + (b * 2) % MOD) % MOD;
        const newB = ((a * 2) % MOD + (b * 3) % MOD) % MOD;
        a = newA;
        b = newB;
    }
    return (a + b) % MOD;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function numOfWays($n) {
        $mod = 1000000007;
        // For the first row: 6 patterns of type A (all distinct) and 6 of type B (ABA)
        $typeA = 6;
        $typeB = 6;

        for ($i = 2; $i <= $n; $i++) {
            $newA = ((($typeA * 2) % $mod) + (($typeB * 2) % $mod)) % $mod;
            $newB = ((($typeA * 2) % $mod) + (($typeB * 3) % $mod)) % $mod;
            $typeA = $newA;
            $typeB = $newB;
        }

        return ($typeA + $typeB) % $mod;
    }
}
```

## Swift

```swift
class Solution {
    func numOfWays(_ n: Int) -> Int {
        let MOD = 1_000_000_007
        var a = 6   // patterns like ABA (first and third same)
        var b = 6   // patterns with all three colors different
        
        if n == 1 { return (a + b) % MOD }
        
        for _ in 2...n {
            let newA = ((a * 3) % MOD + (b * 2) % MOD) % MOD
            let newB = ((a * 2) % MOD + (b * 2) % MOD) % MOD
            a = newA
            b = newB
        }
        return (a + b) % MOD
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numOfWays(n: Int): Int {
        val MOD = 1_000_000_007L
        var a = 6L // rows with three distinct colors
        var b = 6L // rows with pattern ABA (first and third same)
        for (i in 2..n) {
            val newA = (a * 3 + b * 2) % MOD
            val newB = (a * 2 + b * 2) % MOD
            a = newA
            b = newB
        }
        return ((a + b) % MOD).toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int numOfWays(int n) {
    if (n == 1) return 12;
    int a = 6; // type A: all three colors distinct
    int b = 6; // type B: first and third same, middle different
    for (int i = 2; i <= n; ++i) {
      int newA = ((a * 2) % _mod + (b * 2) % _mod) % _mod;
      int newB = ((a * 2) % _mod + (b * 3) % _mod) % _mod;
      a = newA;
      b = newB;
    }
    return (a + b) % _mod;
  }
}
```

## Golang

```go
func numOfWays(n int) int {
	const MOD = 1000000007
	if n <= 0 {
		return 0
	}
	a, b := int64(6), int64(6) // a: all distinct, b: first and third same
	for i := 2; i <= n; i++ {
		na := (2*a + 2*b) % MOD
		nb := (2*a + 3*b) % MOD
		a, b = na, nb
	}
	return int((a + b) % MOD)
}
```

## Ruby

```ruby
def num_of_ways(n)
  mod = 1_000_000_007
  a = 6  # patterns with three distinct colors
  b = 6  # patterns with first and third colors equal
  (2..n).each do |_|
    new_a = (a * 2 + b * 2) % mod
    new_b = (a * 2 + b * 3) % mod
    a, b = new_a, new_b
  end
  (a + b) % mod
end
```

## Scala

```scala
object Solution {
    def numOfWays(n: Int): Int = {
        val MOD = 1000000007L
        var a = 6L // patterns with three distinct colors
        var b = 6L // patterns where first and third colors are the same
        for (_ <- 2 to n) {
            val newA = (a * 2 + b * 2) % MOD
            val newB = (a * 3 + b * 2) % MOD
            a = newA
            b = newB
        }
        ((a + b) % MOD).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_of_ways(n: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        if n == 1 {
            return 12;
        }
        let mut a: i64 = 6; // type A (all distinct)
        let mut b: i64 = 6; // type B (first and third same)
        let mut i = 2;
        while i <= n {
            let new_a = (a * 2 + b * 2) % MOD;
            let new_b = (a * 2 + b * 3) % MOD;
            a = new_a;
            b = new_b;
            i += 1;
        }
        ((a + b) % MOD) as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (num-of-ways n)
  (-> exact-integer? exact-integer?)
  (let loop ((i 2) (a 6) (b 6))
    (if (> i n)
        (modulo (+ a b) MOD)
        (let* ((new-a (modulo (+ (* 3 a) (* 2 b)) MOD))
               (new-b (modulo (+ (* 2 a) (* 2 b)) MOD)))
          (loop (+ i 1) new-a new-b)))))
```

## Erlang

```erlang
-spec num_of_ways(N :: integer()) -> integer().
num_of_ways(N) when is_integer(N), N >= 1 ->
    Mod = 1000000007,
    DP0 = 6,   % patterns where col1 == col3
    DP1 = 6,   % patterns where all three are distinct
    case N of
        1 -> (DP0 + DP1) rem Mod;
        _ -> loop(N - 1, DP0, DP1, Mod)
    end.

loop(0, DP0, DP1, Mod) ->
    (DP0 + DP1) rem Mod;
loop(K, DP0, DP1, Mod) when K > 0 ->
    NewDP0 = (DP0 * 2 + DP1) rem Mod,
    NewDP1 = (DP0 * 2 + DP1 * 3) rem Mod,
    loop(K - 1, NewDP0, NewDP1, Mod).
```

## Elixir

```elixir
defmodule Solution do
  @spec num_of_ways(n :: integer) :: integer
  def num_of_ways(n) when n >= 1 do
    mod = 1_000_000_007
    a0 = 6
    b0 = 6

    if n == 1 do
      rem(a0 + b0, mod)
    else
      {a, b} =
        Enum.reduce(2..n, {a0, b0}, fn _, {prev_a, prev_b} ->
          new_a = rem(2 * prev_a + 2 * prev_b, mod)
          new_b = rem(2 * prev_a + prev_b, mod)
          {new_a, new_b}
        end)

      rem(a + b, mod)
    end
  end
end
```
