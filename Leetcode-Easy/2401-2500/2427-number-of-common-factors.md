# 2427. Number of Common Factors

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int commonFactors(int a, int b) {
        int g = std::gcd(a, b);
        int cnt = 0;
        for (int i = 1; i * i <= g; ++i) {
            if (g % i == 0) {
                ++cnt;
                if (i != g / i) ++cnt;
            }
        }
        return cnt;
    }
};
```

## Java

```java
class Solution {
    public int commonFactors(int a, int b) {
        int g = gcd(a, b);
        int count = 0;
        for (int i = 1; i * i <= g; i++) {
            if (g % i == 0) {
                count += (i * i == g) ? 1 : 2;
            }
        }
        return count;
    }

    private int gcd(int x, int y) {
        while (y != 0) {
            int tmp = x % y;
            x = y;
            y = tmp;
        }
        return x;
    }
}
```

## Python

```python
class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        import math
        g = math.gcd(a, b)
        count = 0
        i = 1
        while i * i <= g:
            if g % i == 0:
                count += 1
                if i != g // i:
                    count += 1
            i += 1
        return count
```

## Python3

```python
import math

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        g = math.gcd(a, b)
        cnt = 0
        i = 1
        while i * i <= g:
            if g % i == 0:
                cnt += 2
                if i * i == g:
                    cnt -= 1
            i += 1
        return cnt
```

## C

```c
int commonFactors(int a, int b) {
    int count = 0;
    int limit = a < b ? a : b;
    for (int i = 1; i <= limit; ++i) {
        if (a % i == 0 && b % i == 0) {
            ++count;
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution
{
    public int CommonFactors(int a, int b)
    {
        int gcd = Gcd(a, b);
        int count = 0;
        for (int i = 1; i * i <= gcd; i++)
        {
            if (gcd % i == 0)
            {
                count++; // divisor i
                if (i != gcd / i) count++; // paired divisor
            }
        }
        return count;
    }

    private int Gcd(int x, int y)
    {
        while (y != 0)
        {
            int temp = x % y;
            x = y;
            y = temp;
        }
        return x;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var commonFactors = function(a, b) {
    const gcd = (x, y) => {
        while (y !== 0) {
            const t = x % y;
            x = y;
            y = t;
        }
        return x;
    };
    
    let g = gcd(a, b);
    let count = 0;
    for (let i = 1; i * i <= g; ++i) {
        if (g % i === 0) {
            count += (i * i === g) ? 1 : 2;
        }
    }
    return count;
};
```

## Typescript

```typescript
function commonFactors(a: number, b: number): number {
    const gcd = (x: number, y: number): number => {
        while (y !== 0) {
            const t = x % y;
            x = y;
            y = t;
        }
        return x;
    };
    const g = gcd(a, b);
    let count = 0;
    for (let i = 1; i * i <= g; i++) {
        if (g % i === 0) {
            count += i * i === g ? 1 : 2;
        }
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $a
     * @param Integer $b
     * @return Integer
     */
    function commonFactors($a, $b) {
        // Compute GCD using Euclidean algorithm
        $g = $this->gcd($a, $b);
        $count = 0;
        $limit = (int)sqrt($g);
        for ($i = 1; $i <= $limit; $i++) {
            if ($g % $i == 0) {
                $count++; // divisor i
                if ($i != $g / $i) {
                    $count++; // paired divisor g/i
                }
            }
        }
        return $count;
    }

    private function gcd($x, $y) {
        while ($y != 0) {
            $temp = $x % $y;
            $x = $y;
            $y = $temp;
        }
        return $x;
    }
}
```

## Swift

```swift
class Solution {
    func commonFactors(_ a: Int, _ b: Int) -> Int {
        let g = gcd(a, b)
        var count = 0
        var i = 1
        while i * i <= g {
            if g % i == 0 {
                count += 1
                if i != g / i {
                    count += 1
                }
            }
            i += 1
        }
        return count
    }
    
    private func gcd(_ x: Int, _ y: Int) -> Int {
        var a = x
        var b = y
        while b != 0 {
            let temp = a % b
            a = b
            b = temp
        }
        return a
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun commonFactors(a: Int, b: Int): Int {
        val g = gcd(a, b)
        var count = 0
        var i = 1
        while (i * i <= g) {
            if (g % i == 0) {
                count += if (i * i == g) 1 else 2
            }
            i++
        }
        return count
    }

    private tailrec fun gcd(x: Int, y: Int): Int = if (y == 0) x else gcd(y, x % y)
}
```

## Dart

```dart
class Solution {
  int commonFactors(int a, int b) {
    int g = _gcd(a, b);
    int count = 0;
    for (int i = 1; i * i <= g; i++) {
      if (g % i == 0) {
        count++;
        if (i != g ~/ i) count++;
      }
    }
    return count;
  }

  int _gcd(int a, int b) {
    while (b != 0) {
      int temp = a % b;
      a = b;
      b = temp;
    }
    return a;
  }
}
```

## Golang

```go
func commonFactors(a int, b int) int {
    // Compute greatest common divisor using Euclidean algorithm
    gcd := func(x, y int) int {
        for y != 0 {
            x, y = y, x%y
        }
        return x
    }(a, b)

    count := 0
    for i := 1; i*i <= gcd; i++ {
        if gcd%i == 0 {
            count += 2 // i and gcd/i are both factors
            if i*i == gcd {
                count-- // perfect square counted twice
            }
        }
    }
    return count
}
```

## Ruby

```ruby
def common_factors(a, b)
  g = a.gcd(b)
  count = 0
  i = 1
  while i * i <= g
    if g % i == 0
      count += 1
      count += 1 if i != g / i
    end
    i += 1
  end
  count
end
```

## Scala

```scala
object Solution {
    def commonFactors(a: Int, b: Int): Int = {
        @annotation.tailrec
        def gcd(x: Int, y: Int): Int =
            if (y == 0) x else gcd(y, x % y)

        val g = gcd(a, b)
        var count = 0
        val limit = math.sqrt(g).toInt
        for (i <- 1 to limit) {
            if (g % i == 0) {
                count += 1
                if (i != g / i) count += 1
            }
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn common_factors(a: i32, b: i32) -> i32 {
        // Compute gcd of a and b
        let mut x = a;
        let mut y = b;
        while y != 0 {
            let tmp = x % y;
            x = y;
            y = tmp;
        }
        let g = x;

        // Count divisors of the gcd
        let mut count = 0;
        let mut i = 1;
        while i * i <= g {
            if g % i == 0 {
                count += if i * i == g { 1 } else { 2 };
            }
            i += 1;
        }
        count
    }
}
```

## Racket

```racket
(define/contract (common-factors a b)
  (-> exact-integer? exact-integer? exact-integer?)
  (let ([limit (min a b)])
    (let loop ((i 1) (cnt 0))
      (if (> i limit)
          cnt
          (loop (add1 i)
                (if (and (= (remainder a i) 0) (= (remainder b i) 0))
                    (add1 cnt)
                    cnt))))))
```

## Erlang

```erlang
-module(solution).
-export([common_factors/2]).

-spec common_factors(A :: integer(), B :: integer()) -> integer().
common_factors(A, B) ->
    G = erlang:gcd(A, B),
    count_divisors(G, 1, 0).

count_divisors(N, I, Acc) when I * I > N ->
    Acc;
count_divisors(N, I, Acc) ->
    case N rem I of
        0 ->
            if I * I =:= N ->
                    count_divisors(N, I + 1, Acc + 1);
               true ->
                    count_divisors(N, I + 1, Acc + 2)
            end;
        _ ->
            count_divisors(N, I + 1, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec common_factors(a :: integer, b :: integer) :: integer
  def common_factors(a, b) do
    limit = min(a, b)

    1..limit
    |> Enum.count(fn x -> rem(a, x) == 0 and rem(b, x) == 0 end)
  end
end
```
