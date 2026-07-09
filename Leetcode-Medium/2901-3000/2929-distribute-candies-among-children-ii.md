# 2929. Distribute Candies Among Children II

## Cpp

```cpp
class Solution {
public:
    long long comb2(long long x) {
        if (x < 0) return 0;
        return x * (x - 1) / 2;
    }
    
    long long distributeCandies(int n, int limit) {
        long long N = n;
        long long L = limit;
        long long total = comb2(N + 2);
        long long sub1 = 3 * comb2(N - L + 1);
        long long add2 = 3 * comb2(N - 2 * L);
        long long sub3 = comb2(N - 3 * L - 1);
        return total - sub1 + add2 - sub3;
    }
};
```

## Java

```java
class Solution {
    public long distributeCandies(int n, int limit) {
        long total = comb2((long) n + 2);
        long L = (long) limit + 1;
        long subtract = 0, add = 0, subtractAgain = 0;

        if (n >= L) {
            subtract = 3L * comb2((long) n - L + 2);
        }
        if (n >= 2L * L / (limit + 1)) { // placeholder to avoid unused warning
            // This line will never be executed; actual condition below.
        }
        if (n >= 2L * L) {
            add = 3L * comb2((long) n - 2L * L + 2);
        }
        if (n >= 3L * L) {
            subtractAgain = comb2((long) n - 3L * L + 2);
        }

        return total - subtract + add - subtractAgain;
    }

    private long comb2(long k) {
        if (k < 2) return 0;
        return k * (k - 1) / 2;
    }
}
```

## Python

```python
class Solution(object):
    def distributeCandies(self, n, limit):
        """
        :type n: int
        :type limit: int
        :rtype: int
        """
        def ways(total):
            if total < 0:
                return 0
            # number of non‑negative integer solutions to x+y+z = total
            # is C(total+2, 2)
            t = total + 2
            return t * (t - 1) // 2

        L = limit + 1
        ans = ways(n)
        ans -= 3 * ways(n - L)
        ans += 3 * ways(n - 2 * L)
        ans -= ways(n - 3 * L)
        return ans
```

## Python3

```python
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def ways(rem: int) -> int:
            if rem < 0:
                return 0
            t = rem + 2
            return t * (t - 1) // 2

        total = ways(n)
        sub1 = ways(n - (limit + 1))
        sub2 = ways(n - 2 * (limit + 1))
        sub3 = ways(n - 3 * (limit + 1))

        return total - 3 * sub1 + 3 * sub2 - sub3
```

## C

```c
static inline long long comb2(long long x){
    if (x < 2) return 0;
    return x * (x - 1) / 2;
}

long long distributeCandies(int n, int limit) {
    long long N = n;
    long long L = limit;
    long long total = comb2(N + 2);
    long long a = comb2(N - (L + 1) + 2);
    long long b = comb2(N - 2 * (L + 1) + 2);
    long long c = comb2(N - 3 * (L + 1) + 2);
    return total - 3 * a + 3 * b - c;
}
```

## Csharp

```csharp
public class Solution {
    public long DistributeCandies(int n, int limit) {
        long total = Ways(n);
        long over1 = Ways(n - (limit + 1));
        long over2 = Ways(n - 2 * (limit + 1));
        long over3 = Ways(n - 3 * (limit + 1));
        return total - 3 * over1 + 3 * over2 - over3;
    }

    private static long Ways(int x) {
        if (x < 0) return 0;
        long k = (long)x + 2; // number of items to choose from
        return k * (k - 1) / 2; // C(k,2)
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} limit
 * @return {number}
 */
var distributeCandies = function(n, limit) {
    const s = limit + 1;
    const c2 = (m) => {
        if (m < 2) return 0;
        return m * (m - 1) / 2;
    };
    const total = c2(n + 2);
    const term1 = c2(n - s + 2);
    const term2 = c2(n - 2 * s + 2);
    const term3 = c2(n - 3 * s + 2);
    return total - 3 * term1 + 3 * term2 - term3;
};
```

## Typescript

```typescript
function distributeCandies(n: number, limit: number): number {
    const maxFirst = Math.min(n, limit);
    let total = 0;
    for (let i = 0; i <= maxFirst; i++) {
        const remaining = n - i;
        const low = Math.max(0, remaining - limit);
        const high = Math.min(limit, remaining);
        if (high >= low) {
            total += high - low + 1;
        }
    }
    return total;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @param Integer $limit
     * @return Integer
     */
    function distributeCandies($n, $limit) {
        $comb2 = function ($m) {
            if ($m < 0 || $m < 2) return 0;
            return intdiv($m * ($m - 1), 2);
        };
        $total = $comb2($n + 2);
        $sub1  = $comb2($n - $limit + 1);
        $sub2  = $comb2($n - 2 * $limit);
        $sub3  = $comb2($n - 3 * $limit - 1);
        $res   = $total - 3 * $sub1 + 3 * $sub2 - $sub3;
        return (int)$res;
    }
}
```

## Swift

```swift
class Solution {
    func distributeCandies(_ n: Int, _ limit: Int) -> Int {
        let N = Int64(n)
        let L = Int64(limit)
        
        func ways(_ m: Int64) -> Int64 {
            if m < 0 { return 0 }
            let a = m + 2
            return a * (a - 1) / 2
        }
        
        let total = ways(N)
        let bad1 = 3 * ways(N - (L + 1))
        let bad2 = 3 * ways(N - 2 * (L + 1))
        let bad3 = ways(N - 3 * (L + 1))
        
        let result = total - bad1 + bad2 - bad3
        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun distributeCandies(n: Int, limit: Int): Long {
        val nn = n.toLong()
        val ll = limit.toLong()
        fun comb(m: Long): Long {
            return if (m < 2) 0L else m * (m - 1) / 2
        }
        val total = comb(nn + 2)
        val term1 = comb(nn - ll + 1)
        val term2 = comb(nn - 2 * ll)
        val term3 = comb(nn - 3 * ll - 1)
        return total - 3L * term1 + 3L * term2 - term3
    }
}
```

## Dart

```dart
class Solution {
  int _comb2(int x) {
    if (x < 0) return 0;
    // C(x, 2) = x * (x - 1) / 2
    return x * (x - 1) ~/ 2;
  }

  int distributeCandies(int n, int limit) {
    int step = limit + 1;

    int ans = _comb2(n + 2);
    ans -= 3 * _comb2(n - step + 2);
    ans += 3 * _comb2(n - 2 * step + 2);
    ans -= _comb2(n - 3 * step + 2);

    return ans;
  }
}
```

## Golang

```go
func distributeCandies(n int, limit int) int64 {
    maxFirst := limit
    if n < maxFirst {
        maxFirst = n
    }
    var total int64
    for i := 0; i <= maxFirst; i++ {
        remaining := n - i

        low := 0
        if remaining-limit > 0 {
            low = remaining - limit
        }

        high := limit
        if remaining < high {
            high = remaining
        }

        if low <= high {
            total += int64(high-low+1)
        }
    }
    return total
}
```

## Ruby

```ruby
def distribute_candies(n, limit)
  max_i = [n, limit].min
  total = 0
  i = 0
  while i <= max_i
    remaining = n - i
    low = [0, remaining - limit].max
    high = [limit, remaining].min
    if low <= high
      total += (high - low + 1)
    end
    i += 1
  end
  total
end
```

## Scala

```scala
object Solution {
    def distributeCandies(n: Int, limit: Int): Long = {
        val maxI = math.min(limit, n)
        var ans: Long = 0L
        var i = 0
        while (i <= maxI) {
            val remaining = n - i
            val low = math.max(0, remaining - limit)
            val high = math.min(limit, remaining)
            if (high >= low) {
                ans += (high - low + 1).toLong
            }
            i += 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn distribute_candies(n: i32, limit: i32) -> i64 {
        fn ways(rem: i64) -> i64 {
            if rem < 0 {
                0
            } else {
                let m = rem + 2;
                m * (m - 1) / 2
            }
        }

        let n64 = n as i64;
        let l = limit as i64 + 1;

        ways(n64)
            - 3 * ways(n64 - l)
            + 3 * ways(n64 - 2 * l)
            - ways(n64 - 3 * l)
    }
}
```

## Racket

```racket
(define/contract (distribute-candies n limit)
  (-> exact-integer? exact-integer? exact-integer?)
  (let* ((max-i (min n limit)))
    (for/sum ([i (in-range (+ max-i 1))])
      (let* ((rem (- n i))
             (low (max 0 (- rem limit)))
             (high (min limit rem))
             (cnt (max 0 (+ (- high low) 1))))
        cnt))))
```

## Erlang

```erlang
-module(solution).
-export([distribute_candies/2]).

-spec distribute_candies(integer(), integer()) -> integer().
distribute_candies(N, Limit) ->
    C0 = comb2(N + 2),
    C1 = comb2(N - Limit + 1),
    C2 = comb2(N - 2 * Limit),
    C3 = comb2(N - 3 * Limit - 1),
    C0 - 3 * C1 + 3 * C2 - C3.

comb2(K) when K < 2 -> 0;
comb2(K) -> (K * (K - 1)) div 2.
```

## Elixir

```elixir
defmodule Solution do
  @spec distribute_candies(integer, integer) :: integer
  def distribute_candies(n, limit) do
    l = limit + 1

    total = c2(n + 2)
    sub1 = c2(n - l + 2)
    add2 = c2(n - 2 * l + 2)
    sub3 = c2(n - 3 * l + 2)

    total - 3 * sub1 + 3 * add2 - sub3
  end

  defp c2(m) when m < 2, do: 0
  defp c2(m), do: div(m * (m - 1), 2)
end
```
