# 1359. Count All Valid Pickup and Delivery Options

## Cpp

```cpp
class Solution {
public:
    int countOrders(int n) {
        const long long MOD = 1000000007LL;
        long long dp = 1;
        for (int i = 1; i <= n; ++i) {
            dp = dp * (2LL * i - 1) % MOD;
            dp = dp * i % MOD;
        }
        return static_cast<int>(dp);
    }
};
```

## Java

```java
class Solution {
    private static final long MOD = 1_000_000_007L;
    public int countOrders(int n) {
        long ans = 1L;
        for (int i = 1; i <= n; i++) {
            ans = ans * (2L * i - 1) % MOD;
            ans = ans * i % MOD;
        }
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def countOrders(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        res = 1
        for i in range(1, n + 1):
            res = (res * (2 * i - 1) * i) % MOD
        return res
```

## Python3

```python
class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9 + 7
        ans = 1
        for i in range(2, n + 1):
            ans = ans * (2 * i - 1) % MOD
            ans = ans * i % MOD
        return ans
```

## C

```c
int countOrders(int n) {
    const int MOD = 1000000007;
    long long res = 1;
    for (int i = 1; i <= n; ++i) {
        res = res * (2LL * i - 1) % MOD;
        res = res * i % MOD;
    }
    return (int)res;
}
```

## Csharp

```csharp
public class Solution
{
    private const int MOD = 1000000007;
    public int CountOrders(int n)
    {
        long result = 1;
        for (int i = 1; i <= n; i++)
        {
            result = result * (2L * i - 1) % MOD;
            result = result * i % MOD;
        }
        return (int)result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var countOrders = function(n) {
    const MOD = 1000000007n;
    let ans = 1n;
    for (let i = 2; i <= n; ++i) {
        ans = (ans * BigInt(2 * i - 1)) % MOD;
        ans = (ans * BigInt(i)) % MOD;
    }
    return Number(ans);
};
```

## Typescript

```typescript
function countOrders(n: number): number {
    const MOD = 1000000007n;
    let ans = 1n;
    for (let i = 1; i <= n; i++) {
        ans = (ans * BigInt(i)) % MOD;
        ans = (ans * BigInt(2 * i - 1)) % MOD;
    }
    return Number(ans);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function countOrders($n) {
        $mod = 1000000007;
        $res = 1;
        for ($i = 1; $i <= $n; $i++) {
            $res = ($res * $i) % $mod;
            $res = ($res * (2 * $i - 1)) % $mod;
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func countOrders(_ n: Int) -> Int {
        let MOD = 1_000_000_007
        var result: Int64 = 1
        for i in 1...n {
            let i64 = Int64(i)
            result = (result * i64) % Int64(MOD)
            result = (result * Int64(2 * i - 1)) % Int64(MOD)
        }
        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countOrders(n: Int): Int {
        val MOD = 1_000_000_007L
        var ans = 1L
        for (i in 1..n) {
            ans = ans * (2L * i - 1) % MOD
            ans = ans * i % MOD
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int countOrders(int n) {
    int ans = 1;
    for (int i = 1; i <= n; ++i) {
      ans = ans * i % _mod;
      ans = ans * (2 * i - 1) % _mod;
    }
    return ans;
  }
}
```

## Golang

```go
func countOrders(n int) int {
	const MOD int64 = 1000000007
	res := int64(1)
	for i := 1; i <= n; i++ {
		res = res * int64(2*i-1) % MOD
		res = res * int64(i) % MOD
	}
	return int(res)
}
```

## Ruby

```ruby
MOD = 1_000_000_007
INV2 = (MOD + 1) / 2

def count_orders(n)
  ans = 1
  (1..n).each do |i|
    ans = (ans * (2 * i)) % MOD
    ans = (ans * (2 * i - 1)) % MOD
    ans = (ans * INV2) % MOD
  end
  ans
end
```

## Scala

```scala
object Solution {
  def countOrders(n: Int): Int = {
    val MOD = 1000000007L
    var ans = 1L
    var i = 2
    while (i <= n) {
      ans = ans * (2L * i - 1) % MOD
      ans = ans * i % MOD
      i += 1
    }
    ans.toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn count_orders(n: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut ans: i64 = 1;
        for i in 1..=n as i64 {
            ans = ans * i % MOD;
            ans = ans * (2 * i - 1) % MOD;
        }
        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (count-orders n)
  (-> exact-integer? exact-integer?)
  (let loop ((i 1) (res 1))
    (if (> i n)
        res
        (loop (+ i 1)
              (modulo (* res (- (* 2 i) 1) i) MOD)))) )
```

## Erlang

```erlang
-module(solution).
-export([count_orders/1]).

-define(MOD, 1000000007).
-define(INV2, 500000004).

count_orders(N) ->
    Fact = factorial(2 * N),
    InvPow = mod_pow(?INV2, N),
    (Fact * InvPow) rem ?MOD.

factorial(K) -> factorial(K, 1).

factorial(0, Acc) -> Acc;
factorial(N, Acc) when N > 0 ->
    NewAcc = (Acc * N) rem ?MOD,
    factorial(N - 1, NewAcc).

mod_pow(Base, Exp) -> mod_pow(Base rem ?MOD, Exp, 1).

mod_pow(_Base, 0, Acc) -> Acc;
mod_pow(Base, Exp, Acc) when (Exp band 1) =:= 1 ->
    NewAcc = (Acc * Base) rem ?MOD,
    mod_pow((Base * Base) rem ?MOD, Exp bsr 1, NewAcc);
mod_pow(Base, Exp, Acc) ->
    mod_pow((Base * Base) rem ?MOD, Exp bsr 1, Acc).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @spec count_orders(n :: integer) :: integer
  def count_orders(n) when n >= 0 do
    mod = 1_000_000_007

    Enum.reduce(1..n, 1, fn i, acc ->
      acc
      |> Kernel.*(2 * i - 1)
      |> rem(mod)
      |> Kernel.*(i)
      |> rem(mod)
    end)
  end
end
```
